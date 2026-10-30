# SPDX-License-Identifier: AGPL-3.0-only
"""Tests for the AGE Administrativo C1 simulation presets (round R5).

Covers:
- «Simulacro oficial» draw counts per source (40 from m01-m05 + 30 from m06 + 5 reserve)
- Reserve questions placed last in part 1
- Pair drawn from the ten R4 pairs and offered in part 2
- Only the chosen case graded
- Refusal / ungraded when 0 or 2 cases marked
- Part 2 not graded when part 1 < 25 (minimum_raw = 95/3, printed 31,67)
- Hand-computed raw and transformed scores per part and in total (with blanks and wrongs)
- Auto-submission on deadline (100 minutes)
- «Parte 1» and «Parte 2» alone presets (50 minutes each)
"""

from __future__ import annotations

import random
import uuid
from collections.abc import Sequence
from datetime import timedelta
from fractions import Fraction
from pathlib import Path

import pytest
from httpx import AsyncClient
from sqlalchemy import select, update

from tradeschool.attempts.models import Attempt
from tradeschool.attempts.service import question_ref
from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.db import get_sessionmaker
from tradeschool.exams.draw import (
    counted_questions,
    draw_part,
    pool_shortfalls,
)
from tradeschool.exams.models import ExamSession
from tradeschool.exams.presets import PartScoring
from tradeschool.exams.print_export import build_exam_print
from tradeschool.exams.scoring import Tally, raw_score, transformed_score
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator

CONTENT_DIR = Path(__file__).resolve().parent.parent.parent / "content" / "age-administrativo-c1"
AGE_API = "/api/courses/age-administrativo-c1"
PASSWORD = "correcthorse"

CPS_P1 = PartScoring(max=50, pass_minimum=25, minimum_raw=Fraction(95, 3))
CPS_P2 = PartScoring(max=50, pass_minimum=25, minimum_raw=Fraction(38, 3))

EXPECTED_PAIRS = [
    {"sp-01", "sp-05"},
    {"sp-02", "sp-10"},
    {"sp-03", "sp-04"},
    {"sp-06", "sp-08"},
    {"sp-07", "sp-18"},
    {"sp-09", "sp-20"},
    {"sp-11", "sp-16"},
    {"sp-12", "sp-14"},
    {"sp-13", "sp-19"},
    {"sp-15", "sp-17"},
]


class _SeededRng:
    def __init__(self, seed: int) -> None:
        self._rng = random.Random(seed)

    def choice(self, seq: Sequence[str]) -> str:
        return self._rng.choice(seq)

    def randbelow(self, n: int) -> int:
        return self._rng.randrange(n)


@pytest.fixture(scope="module")
def registry() -> CourseRegistry:
    return load_registry(CONTENT_DIR)


def test_hand_computed_scoring_examples_with_blanks_and_wrongs() -> None:
    # Example 1: Part 1 (70 questions) with 50 correct, 12 wrong, 8 blank.
    # Raw = 50 - 12/3 = 46.
    p1_tally = Tally(correct=50, wrong=12, blank=8)
    p1_raw = raw_score(p1_tally, Fraction(1, 3), "free")
    assert p1_raw == 46
    p1_trans = float(transformed_score(p1_raw, 70, CPS_P1))
    # 25 + (46 - 95/3) * 25 / (70 - 95/3) = 34.35
    assert p1_trans == pytest.approx(34.35, abs=0.01)

    # Example 1: Part 2 (20 questions) with 16 correct, 3 wrong, 1 blank.
    # Raw = 16 - 3/3 = 15.
    p2_tally = Tally(correct=16, wrong=3, blank=1)
    p2_raw = raw_score(p2_tally, Fraction(1, 3), "free")
    assert p2_raw == 15
    p2_trans = float(transformed_score(p2_raw, 20, CPS_P2))
    # 25 + (15 - 38/3) * 25 / (20 - 38/3) = 32.95
    assert p2_trans == pytest.approx(32.95, abs=0.01)

    # Total score
    total_raw = float(p1_raw + p2_raw)
    total_trans = round(p1_trans + p2_trans, 2)
    assert total_raw == 61.0
    assert total_trans == pytest.approx(67.30, abs=0.01)

    # Example 2: Part 1 below minimum_raw (28 correct, 6 wrong, 36 blank)
    # Raw = 28 - 2 = 26 < 95/3.
    p1_fail_tally = Tally(correct=28, wrong=6, blank=36)
    p1_fail_raw = raw_score(p1_fail_tally, Fraction(1, 3), "free")
    assert p1_fail_raw == 26
    p1_fail_trans = float(transformed_score(p1_fail_raw, 70, CPS_P1))
    # 25 * 26 / (95/3) = 20.53 (< 25, failing)
    assert p1_fail_trans == pytest.approx(20.53, abs=0.01)


def test_simulacro_preset_draws_expected_counts_and_reserves_last(registry: CourseRegistry) -> None:
    preset = next(p for p in registry.manifest.exams if p.id == "simulacro")
    assert pool_shortfalls(registry, preset, None) == []

    # Part 1 draw
    p1 = preset.parts[0]
    assert p1.id == "parte-1"
    assert p1.reserve == 5
    assert counted_questions(registry, p1, None) == 70

    drawn_p1 = draw_part(registry, p1, None, _SeededRng(42)).questions
    assert len(drawn_p1) == 75
    # First 70 are ordinary, last 5 are reserve
    assert [q.reserve for q in drawn_p1] == [False] * 70 + [True] * 5

    # Check sources: 40 from m01-m05, 30 from m06 among the 70 counted
    counted = drawn_p1[:70]
    m01_m05 = sum(1 for q in counted if q.exercise_id.startswith(("m01-", "m02-", "m03-", "m04-", "m05-")))
    m06 = sum(1 for q in counted if q.exercise_id.startswith("m06-"))
    assert m01_m05 == 40
    assert m06 == 30

    # Part 2 draw: must draw a pair from the 10 R4 pairs
    p2 = preset.parts[1]
    assert p2.id == "parte-2"
    assert p2.choose == 2
    assert p2.questions == 20
    assert p2.case_pairs is not None
    assert len(p2.case_pairs) == 10

    drawn_p2 = draw_part(registry, p2, None, _SeededRng(42))
    assert len(drawn_p2.cases) == 2
    assert set(drawn_p2.cases) in EXPECTED_PAIRS
    # 20 questions per case
    assert len(drawn_p2.questions) == 40
    case_a_qs = [q for q in drawn_p2.questions if q.exercise_id == drawn_p2.cases[0]]
    case_b_qs = [q for q in drawn_p2.questions if q.exercise_id == drawn_p2.cases[1]]
    assert len(case_a_qs) == 20
    assert len(case_b_qs) == 20


def test_parte_1_and_parte_2_alone_presets(registry: CourseRegistry) -> None:
    p1_preset = next(p for p in registry.manifest.exams if p.id == "parte-1")
    p2_preset = next(p for p in registry.manifest.exams if p.id == "parte-2")

    assert p1_preset.time_limit_minutes == 50
    assert p1_preset.pause == "never"
    assert pool_shortfalls(registry, p1_preset, None) == []

    assert p2_preset.time_limit_minutes == 50
    assert p2_preset.pause == "never"
    assert pool_shortfalls(registry, p2_preset, None) == []


async def _sign_up(client: AsyncClient, username: str) -> None:
    body = {
        "username": username,
        "password": PASSWORD,
        "locale": "es",
        "courses": ["age-administrativo-c1"],
    }
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"username": username, "password": PASSWORD})


async def _correct_options(registry: CourseRegistry, exam_id: str) -> dict[str, str]:
    async with get_sessionmaker()() as session:
        attempts = (
            await session.scalars(select(Attempt).where(Attempt.exam_session_id == uuid.UUID(exam_id)))
        ).all()
    out: dict[str, str] = {}
    for attempt in attempts:
        config = registry.attempt_config(question_ref(registry, attempt))
        assert config is not None
        graded = QuizGenerator().grade(config[1], attempt.seed, {"optionId": ""}, "es")
        out[str(attempt.id)] = str(graded.correct_answer["optionId"])  # type: ignore[index]
    return out


def _wrong(correct: str) -> str:
    return next(option for option in "abcd" if option != correct)


async def _answer(client: AsyncClient, exam: dict[str, object], attempt_id: str, option: str) -> int:
    url = f"{AGE_API}/exams/{exam['id']}/questions/{attempt_id}/answer"
    return (await client.post(url, json={"answer": {"optionId": option}})).status_code


async def _answer_pattern(
    client: AsyncClient,
    exam: dict[str, object],
    attempts: list[str],
    correct: dict[str, str],
    right: int,
    wrong: int,
) -> None:
    for index, attempt_id in enumerate(attempts):
        if index < right:
            assert await _answer(client, exam, attempt_id, correct[attempt_id]) == 204
        elif index < right + wrong:
            assert await _answer(client, exam, attempt_id, _wrong(correct[attempt_id])) == 204


def _part(
    exam: dict[str, object], part_id: str, *, reserve: bool = False, case: str | None = None
) -> list[str]:
    questions = exam["questions"]
    assert isinstance(questions, list)
    return [
        q["attemptId"]
        for q in questions
        if q["partId"] == part_id and q["reserve"] is reserve and (case is None or q["exerciseId"] == case)
    ]


async def test_simulacro_end_to_end_grades_only_marked_case_and_computes_cps_scores(
    multi_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(multi_client, "simulacro_passer")
    resp = await multi_client.post(f"{AGE_API}/exams", json={"presetId": "simulacro"})
    assert resp.status_code == 201
    exam = resp.json()

    # Offered cases in part 2
    part2_info = next(p for p in exam["parts"] if p["id"] == "parte-2")
    offered_cases = [c["exerciseId"] for c in part2_info["cases"]]
    assert len(offered_cases) == 2
    assert set(offered_cases) in EXPECTED_PAIRS

    chosen_case = offered_cases[0]
    correct = await _correct_options(registry, str(exam["id"]))

    # Part 1: 50 correct, 12 wrong, 8 blank -> raw = 46, transformed = 34.35
    await _answer_pattern(multi_client, exam, _part(exam, "parte-1"), correct, 50, 12)
    # Part 2: chosen case: 16 correct, 3 wrong, 1 blank -> raw = 15, transformed = 32.95
    await _answer_pattern(multi_client, exam, _part(exam, "parte-2", case=chosen_case), correct, 16, 3)

    # Mark the chosen case
    mark_url = f"{AGE_API}/exams/{exam['id']}/parts/parte-2/cases"
    mark_resp = await multi_client.put(mark_url, json={"exerciseIds": [chosen_case]})
    assert mark_resp.status_code == 204

    # Submit
    submit_resp = await multi_client.post(f"{AGE_API}/exams/{exam['id']}/submit")
    assert submit_resp.status_code == 200
    submitted = submit_resp.json()
    result = submitted["result"]

    assert result["raw"] == 61.0
    assert result["transformed"] == pytest.approx(67.30, abs=0.01)

    p1_res = result["parts"][0]
    assert p1_res["id"] == "parte-1"
    assert p1_res["raw"] == 46.0
    assert p1_res["transformed"] == pytest.approx(34.35, abs=0.01)
    assert p1_res["passed"] is True

    p2_res = result["parts"][1]
    assert p2_res["id"] == "parte-2"
    assert p2_res["graded"] is True
    assert p2_res["case"] == chosen_case
    assert p2_res["raw"] == 15.0
    assert p2_res["transformed"] == pytest.approx(32.95, abs=0.01)


@pytest.mark.parametrize(
    ("marked", "reason"),
    [([], "no-case-marked"), ("two", "several-cases-marked")],
)
async def test_simulacro_refuses_to_grade_part_2_when_no_case_or_two_marked(
    multi_client: AsyncClient, registry: CourseRegistry, marked: list[str] | str, reason: str
) -> None:
    await _sign_up(multi_client, f"marker_{reason}")
    exam = (await multi_client.post(f"{AGE_API}/exams", json={"presetId": "simulacro"})).json()
    part2_info = next(p for p in exam["parts"] if p["id"] == "parte-2")
    offered_cases = [c["exerciseId"] for c in part2_info["cases"]]
    marked_cases = offered_cases if marked == "two" else []

    correct = await _correct_options(registry, str(exam["id"]))

    # Part 1 passes
    await _answer_pattern(multi_client, exam, _part(exam, "parte-1"), correct, 50, 0)
    await multi_client.put(
        f"{AGE_API}/exams/{exam['id']}/parts/parte-2/cases", json={"exerciseIds": marked_cases}
    )
    submitted = (await multi_client.post(f"{AGE_API}/exams/{exam['id']}/submit")).json()
    result = submitted["result"]

    p2_res = result["parts"][1]
    assert p2_res["graded"] is False
    assert p2_res["reason"] == reason
    assert "transformed" not in p2_res


async def test_simulacro_refuses_to_grade_part_2_when_part_1_fails(
    multi_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(multi_client, "part1_failer")
    exam = (await multi_client.post(f"{AGE_API}/exams", json={"presetId": "simulacro"})).json()
    correct = await _correct_options(registry, str(exam["id"]))

    part2_info = next(p for p in exam["parts"] if p["id"] == "parte-2")
    chosen_case = part2_info["cases"][0]["exerciseId"]

    # Part 1 fails: raw 26 < 95/3
    await _answer_pattern(multi_client, exam, _part(exam, "parte-1"), correct, 28, 6)
    # Part 2 answered fully correct
    await _answer_pattern(multi_client, exam, _part(exam, "parte-2", case=chosen_case), correct, 20, 0)
    await multi_client.put(
        f"{AGE_API}/exams/{exam['id']}/parts/parte-2/cases", json={"exerciseIds": [chosen_case]}
    )

    submitted = (await multi_client.post(f"{AGE_API}/exams/{exam['id']}/submit")).json()
    result = submitted["result"]

    p1_res = result["parts"][0]
    assert p1_res["raw"] == 26.0
    assert p1_res["graded"] is True

    p2_res = result["parts"][1]
    # Part 2 ungraded because requires_previous_pass was not met!
    assert p2_res["graded"] is False
    assert p2_res["reason"] == "previous-part-not-passed"
    assert "transformed" not in p2_res
    assert result["transformed"] == p1_res["transformed"]


async def test_simulacro_auto_submits_at_deadline(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "times_out")
    exam = (await multi_client.post(f"{AGE_API}/exams", json={"presetId": "simulacro"})).json()
    q_id = exam["questions"][0]["attemptId"]
    assert await _answer(multi_client, exam, q_id, "a") == 204

    # Fast forward deadline by moving created_at back by 101 minutes
    exam_uuid = uuid.UUID(str(exam["id"]))
    async with get_sessionmaker()() as session:
        await session.execute(
            update(ExamSession)
            .where(ExamSession.id == exam_uuid)
            .values(created_at=ExamSession.created_at - timedelta(minutes=101))
        )
        await session.commit()

    # Answering now fails with EXAM_TIME_UP because deadline passed
    ans_resp = await multi_client.post(
        f"{AGE_API}/exams/{exam['id']}/questions/{q_id}/answer", json={"answer": {"optionId": "b"}}
    )
    assert ans_resp.status_code == 409
    assert ans_resp.json()["code"] == "EXAM_TIME_UP"

    # Submitting now records autoSubmitted: True in DB
    submitted = (await multi_client.post(f"{AGE_API}/exams/{exam['id']}/submit")).json()
    assert submitted["status"] == "submitted"
    assert submitted["finishedAt"] is not None

    async with get_sessionmaker()() as session:
        stored = await session.get(ExamSession, exam_uuid)
        assert stored is not None
        assert stored.rules.get("autoSubmitted") is True


@pytest.mark.parametrize(
    ("preset_id", "part_id", "cut", "counted"),
    [
        ("simulacro", "parte-1", Fraction(95, 3), 70),
        ("simulacro", "parte-2", Fraction(38, 3), 20),
        ("parte-1", "parte-1", Fraction(95, 3), 70),
        ("parte-2", "parte-2", Fraction(38, 3), 20),
    ],
)
def test_a_raw_score_equal_to_the_published_cut_earns_exactly_the_pass_minimum(
    registry: CourseRegistry, preset_id: str, part_id: str, cut: Fraction, counted: int
) -> None:
    # The CPS prints the cuts as 31,67 and 12,67; the reachable raw scores 95/3 and 38/3 are what pass.
    preset = next(p for p in registry.manifest.exams if p.id == preset_id)
    part = next(p for p in preset.parts if p.id == part_id)
    assert part.scoring is not None
    assert transformed_score(cut, counted, part.scoring) == 25
    assert transformed_score(cut - Fraction(1, 3), counted, part.scoring) < 25


def _correct_option_id(
    registry: CourseRegistry, part_kind: str, case_id: str | None, question_id: str
) -> str:
    """The correct option as the content declares it, independent of the print export's own key."""
    if part_kind == "cases":
        assert case_id is not None
        case = registry.case_config(case_id)
        assert case is not None
        question = next(q for q in case.questions if q.id == question_id)
        return next(o.id for o in question.options if o.correct)
    exercise_id, variant_id = question_id.split("/")
    config = registry.get_exercise_config(exercise_id)
    assert config is not None and isinstance(config[1], QuizConfig)
    variant = next(v for v in config[1].variants if v.id == variant_id)
    return next(o.id for o in variant.options if o.correct)


def test_the_printed_key_letter_is_the_letter_printed_next_to_the_correct_option(
    registry: CourseRegistry,
) -> None:
    doc = build_exam_print(registry, "simulacro", "es", seed=7)
    printed: list[tuple[str, str | None, dict[str, object]]] = []
    for part in doc["parts"]:
        if part["kind"] == "cases":
            printed += [("cases", case["id"], q) for case in part["cases"] for q in case["questions"]]
        else:
            printed += [("questions", None, q) for q in part["questions"]]
    keys = [key for group in doc["keySheet"] for key in group["keys"]]

    assert len(printed) == len(keys) == 75 + 2 * 20
    for (kind, case_id, question), key in zip(printed, keys, strict=True):
        assert key["number"] == question["number"]
        options = question["options"]
        assert isinstance(options, list)
        assert [o["letter"] for o in options] == ["A", "B", "C", "D"]
        correct_id = _correct_option_id(registry, kind, case_id, str(question["id"]))
        letter_beside_correct = next(o["letter"] for o in options if o["id"] == correct_id)
        assert key["correctLetter"] == letter_beside_correct, question["number"]
