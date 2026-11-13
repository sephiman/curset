# SPDX-License-Identifier: AGPL-3.0-only
"""The aeat-agentes-hacienda presets (round R5): the 2025 draw, the BOE mark, the clock, «Bloque», «Tema»."""

from __future__ import annotations

import re
import uuid
from collections import Counter
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
from tradeschool.exams.draw import SeededRand, counted_questions, draw_part, pool_shortfalls, preset_targets
from tradeschool.exams.models import ExamSession
from tradeschool.exams.presets import ExamPreset, PartScoring
from tradeschool.exams.print_export import build_exam_print
from tradeschool.exams.scoring import Tally, raw_score, transformed_score
from tradeschool.exercises.registry import get_generator

ROOT = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = ROOT / "content" / "aeat-agentes-hacienda"
LEDGER = ROOT / "docs" / "aeat-official-exams-ledger.md"
API = "/api/courses/aeat-agentes-hacienda"
PASSWORD = "correcthorse"
PENALTY = Fraction(1, 4)

#: Criterion 2 of the 2025 criteria (sources/programa.md): 50 % of the maximum; the Tribunal may lower it.
FLOOR = Fraction(40)


@pytest.fixture(scope="module")
def registry() -> CourseRegistry:
    return load_registry(CONTENT_DIR)


def _preset(registry: CourseRegistry, preset_id: str) -> ExamPreset:
    return next(p for p in registry.manifest.exams if p.id == preset_id)


def _scoring(registry: CourseRegistry) -> PartScoring:
    (part,) = _preset(registry, "primer-ejercicio").parts
    assert part.scoring is not None
    return part.scoring


def _paper_2025_parts() -> list[str]:
    """The programme part (I, II, III) of each of the 80 questions of the 2025 paper, in printed order."""
    lines = LEDGER.read_text(encoding="utf-8").split("## OEP 2025, 21-03-2026")[1].split("## OEP 2024")[0]
    parts = [m.group(1) for m in re.finditer(r"^\| \d+ \| \d+ \| (I{1,3})\.\d+", lines, re.MULTILINE)]
    assert len(parts) == 80
    return parts


def test_the_draw_is_the_2025_papers_proportions_per_part_of_the_programme(registry: CourseRegistry) -> None:
    paper = Counter(_paper_2025_parts())
    assert paper == {"I": 8, "II": 10, "III": 62}
    (part,) = _preset(registry, "primer-ejercicio").parts
    assert {entry.source.module: entry.questions for entry in part.draws} == {
        "m01": paper["I"],
        "m02": paper["II"],
        "m03": paper["III"],
    }
    assert counted_questions(registry, part, None) == 80


def test_the_paper_prints_the_parts_mixed_so_the_preset_draws_them_shuffled(registry: CourseRegistry) -> None:
    parts = _paper_2025_parts()
    assert parts != sorted(parts)
    (part,) = _preset(registry, "primer-ejercicio").parts
    assert part.order == "shuffled"


def test_the_preset_carries_the_boes_rules(registry: CourseRegistry) -> None:
    preset = _preset(registry, "primer-ejercicio")
    assert (preset.time_limit_minutes, preset.pause) == (90, "never")
    (part,) = preset.parts
    assert (part.penalty, part.blank, part.reserve) == (PENALTY, "free", 0)
    scoring = _scoring(registry)
    assert (scoring.max, scoring.pass_minimum, scoring.minimum_raw) == (10, 5, FLOOR)
    assert part.scoring is not None and part.requires_previous_pass is False


def test_the_description_says_the_pass_raw_score_is_the_tribunals_and_gives_2025_as_information(
    registry: CourseRegistry,
) -> None:
    description = _preset(registry, "primer-ejercicio").description
    assert description is not None
    text = description.get("es")
    assert "la fija el Tribunal después de cada examen" in text
    assert "40 puntos directos" in text and "41,00" in text
    assert "Cada convocatoria fija la suya." in text


@pytest.mark.parametrize("seed", [1, 2, 3, 4, 5])
def test_each_draw_has_80_distinct_questions_8_10_and_62_from_the_three_parts(
    registry: CourseRegistry, seed: int
) -> None:
    (part,) = _preset(registry, "primer-ejercicio").parts
    drawn = draw_part(registry, part, None, SeededRand(seed)).questions
    assert len(drawn) == 80 and not any(q.reserve for q in drawn)
    assert len({(q.exercise_id, q.variant_id) for q in drawn}) == 80
    assert Counter(q.exercise_id.split("-")[0] for q in drawn) == {"m01": 8, "m02": 10, "m03": 62}


def test_every_preset_the_course_declares_can_be_supplied(registry: CourseRegistry) -> None:
    ids = [preset.id for preset in registry.manifest.exams]
    assert ids[:3] == ["primer-ejercicio", "bloque", "tema"]
    for preset in registry.manifest.exams:
        if not preset.parametric:
            assert pool_shortfalls(registry, preset, None) == [], preset.id


def test_a_raw_score_equal_to_the_floor_earns_exactly_5_and_80_earns_10(registry: CourseRegistry) -> None:
    scoring = _scoring(registry)
    assert transformed_score(FLOOR, 80, scoring) == 5
    assert transformed_score(Fraction(80), 80, scoring) == 10
    assert transformed_score(Fraction(0), 80, scoring) == 0


def test_hand_computed_marks_at_the_floor_one_answer_below_it_and_with_blanks_and_wrongs(
    registry: CourseRegistry,
) -> None:
    scoring = _scoring(registry)

    def mark(correct: int, wrong: int, blank: int) -> Fraction:
        assert correct + wrong + blank == 80
        return transformed_score(raw_score(Tally(correct, wrong, blank), PENALTY, "free"), 80, scoring)

    # Exactly at the floor: 40 right and nothing else, or 44 right and 16 wrong (44 - 16/4 = 40).
    assert mark(40, 0, 40) == 5
    assert mark(44, 16, 20) == 5
    # One answer below: 39 right, raw 39, 5 * 39 / 40 = 39/8.
    # Or 40 right and 1 wrong, raw 39.75, 5 * 39.75 / 40 = 159/32.
    assert mark(39, 0, 41) == Fraction(39, 8)
    assert mark(40, 1, 39) == Fraction(159, 32)
    # One answer above: 41 right, raw 41, 5 + 1 * 5 / 40 = 41/8.
    assert mark(41, 0, 39) == Fraction(41, 8)
    # Blanks and wrongs: 50 right, 20 wrong, 10 blank, raw 45, 5 + 5 * 5 / 40 = 45/8.
    assert mark(50, 20, 10) == Fraction(45, 8)
    # Blanks are free: the same 60 right with 20 blank is 60 raw, 5 + 20 * 5 / 40 = 15/2.
    assert mark(60, 0, 20) == Fraction(15, 2)
    # All wrong: raw -20, no negative mark.
    assert mark(0, 80, 0) == 0
    assert mark(80, 0, 0) == 10


def test_the_marks_pass_the_boes_five_from_the_floor_and_not_a_hair_below(registry: CourseRegistry) -> None:
    scoring = _scoring(registry)
    assert transformed_score(FLOOR, 80, scoring) >= Fraction(str(scoring.pass_minimum))
    assert transformed_score(FLOOR - PENALTY, 80, scoring) < Fraction(str(scoring.pass_minimum))


def test_bloque_and_tema_are_parametric_over_the_parts_and_the_temas_with_the_courses_time_estimate(
    registry: CourseRegistry,
) -> None:
    assert preset_targets(registry, _preset(registry, "bloque")) == ["m01", "m02", "m03"]
    temas = preset_targets(registry, _preset(registry, "tema"))
    assert len(temas) == 32
    assert temas[0] == "m01-l01" and temas[-1] == "m03-l20"
    assert not any(t.startswith("m00") for t in temas)
    bloque, tema = _preset(registry, "bloque"), _preset(registry, "tema")
    assert (bloque.time_limit_minutes, tema.time_limit_minutes) == (45, 11)
    assert (bloque.pause, tema.pause) == ("between-questions", "between-questions")
    # 90 minutes for 80 questions: 1.125 minutes each.
    assert bloque.time_limit_minutes == 40 * 90 / 80
    assert tema.time_limit_minutes == round(10 * 90 / 80)
    for preset in (bloque, tema):
        assert preset.description is not None
        assert "estimación del curso" in preset.description.get("es")
        assert "90 minutos que la convocatoria da para las 80 preguntas" in preset.description.get("es")
        (part,) = preset.parts
        assert part.penalty == PENALTY and part.scoring is None


def test_a_bloque_sitting_draws_40_from_the_part_and_a_tema_sitting_10_from_the_tema(
    registry: CourseRegistry,
) -> None:
    bloque = _preset(registry, "bloque").parts[0]
    drawn = draw_part(registry, bloque, "m02", SeededRand(1)).questions
    assert len(drawn) == 40 and {q.exercise_id.split("-")[0] for q in drawn} == {"m02"}
    tema = _preset(registry, "tema").parts[0]
    drawn = draw_part(registry, tema, "m03-l04", SeededRand(1)).questions
    assert len(drawn) == 10 and {q.exercise_id.rsplit("-ex-", 1)[0] for q in drawn} == {"m03-l04"}


def test_the_same_seed_prints_the_same_paper_with_a_key_sheet(registry: CourseRegistry) -> None:
    paper = build_exam_print(registry, "primer-ejercicio", "es", seed=7)
    assert paper == build_exam_print(registry, "primer-ejercicio", "es", seed=7)
    assert paper != build_exam_print(registry, "primer-ejercicio", "es", seed=8)
    questions = paper["parts"][0]["questions"]
    keys = paper["keySheet"][0]["keys"]
    assert len(questions) == len(keys) == 80
    assert [o["letter"] for o in questions[0]["options"]] == ["A", "B", "C", "D"]
    assert {k["correctLetter"] for k in keys} <= set("ABCD")
    assert paper["timeLimitMinutes"] == 90


async def _sign_up(client: AsyncClient, name: str) -> None:
    email = f"{name}@example.com"
    body = {
        "email": email,
        "name": name,
        "password": PASSWORD,
        "locale": "es",
        "courses": ["aeat-agentes-hacienda"],
    }
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"email": email, "password": PASSWORD})


async def _options(registry: CourseRegistry, exam_id: str) -> dict[str, tuple[str, str]]:
    """Per attempt: the correct option id and a wrong one, from the content and not from the answer API."""
    async with get_sessionmaker()() as session:
        attempts = (
            await session.scalars(select(Attempt).where(Attempt.exam_session_id == uuid.UUID(exam_id)))
        ).all()
    out: dict[str, tuple[str, str]] = {}
    for attempt in attempts:
        found = registry.attempt_config(question_ref(registry, attempt))
        assert found is not None
        generator = get_generator(found[0])
        graded = generator.grade(found[1], attempt.seed, {"optionId": ""}, "es")
        correct = str(graded.correct_answer["optionId"])  # type: ignore[index]
        shown = generator.generate(found[1], attempt.seed, "es").payload["options"]
        assert isinstance(shown, list)
        wrong = next(str(o["id"]) for o in shown if o["id"] != correct)
        out[str(attempt.id)] = (correct, wrong)
    return out


async def _answer(client: AsyncClient, exam: dict[str, object], attempt_id: str, option: str) -> int:
    url = f"{API}/exams/{exam['id']}/questions/{attempt_id}/answer"
    return (await client.post(url, json={"answer": {"optionId": option}})).status_code


async def _sit(
    client: AsyncClient, registry: CourseRegistry, name: str, right: int, wrong: int
) -> dict[str, object]:
    await _sign_up(client, name)
    exam = (await client.post(f"{API}/exams", json={"presetId": "primer-ejercicio"})).json()
    options = await _options(registry, str(exam["id"]))
    attempts = [q["attemptId"] for q in exam["questions"]]
    assert len(attempts) == 80
    for index, attempt_id in enumerate(attempts):
        if index < right:
            assert await _answer(client, exam, attempt_id, options[attempt_id][0]) == 204
        elif index < right + wrong:
            assert await _answer(client, exam, attempt_id, options[attempt_id][1]) == 204
    submitted = (await client.post(f"{API}/exams/{exam['id']}/submit")).json()
    result: dict[str, object] = submitted["result"]
    return result


@pytest.mark.parametrize(
    ("right", "wrong", "raw", "mark", "passed"),
    [
        (40, 0, 40.0, 5.0, True),
        (44, 16, 40.0, 5.0, True),
        (39, 0, 39.0, 4.875, False),
        (40, 1, 39.75, 4.9688, False),
        (50, 20, 45.0, 5.625, True),
        (80, 0, 80.0, 10.0, True),
    ],
)
async def test_a_sitting_is_marked_exactly_as_the_hand_computed_examples(
    aeat_client: AsyncClient,
    registry: CourseRegistry,
    right: int,
    wrong: int,
    raw: float,
    mark: float,
    passed: bool,
) -> None:
    result = await _sit(aeat_client, registry, f"aeat_{right}_{wrong}", right, wrong)
    parts = result["parts"]
    assert isinstance(parts, list)
    (part,) = parts
    assert part["questions"] == 80
    assert (part["correct"], part["wrong"], part["blank"]) == (right, wrong, 80 - right - wrong)
    assert part["raw"] == raw
    assert part["transformed"] == pytest.approx(mark, abs=1e-4)
    assert part["max"] == 10 and part["passed"] is passed
    assert result["transformed"] == part["transformed"]


async def test_the_results_split_the_sitting_by_tema_across_the_three_parts(
    aeat_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(aeat_client, "aeat_by_tema")
    exam = (await aeat_client.post(f"{API}/exams", json={"presetId": "primer-ejercicio"})).json()
    submitted = (await aeat_client.post(f"{API}/exams/{exam['id']}/submit")).json()
    assert submitted["result"]["parts"][0]["blank"] == 80
    groups = {group["moduleId"]: group for group in submitted["byLesson"]["groups"]}
    assert {key: groups[key]["questions"] for key in ("m01", "m02", "m03")} == {
        "m01": 8,
        "m02": 10,
        "m03": 62,
    }
    rows = [row for group in groups.values() for row in group["lessons"]]
    assert sum(row["questions"] for row in rows) == 80
    assert all(row["lessonId"].startswith(("m01-", "m02-", "m03-")) for row in rows)


async def test_a_sitting_is_submitted_when_the_90_minutes_run_out(aeat_client: AsyncClient) -> None:
    await _sign_up(aeat_client, "aeat_times_out")
    exam = (await aeat_client.post(f"{API}/exams", json={"presetId": "primer-ejercicio"})).json()
    attempt_id = exam["questions"][0]["attemptId"]
    assert exam["deadline"] is not None

    exam_uuid = uuid.UUID(str(exam["id"]))
    async with get_sessionmaker()() as session:
        await session.execute(
            update(ExamSession)
            .where(ExamSession.id == exam_uuid)
            .values(created_at=ExamSession.created_at - timedelta(minutes=89, seconds=30))
        )
        await session.commit()
    assert await _answer(aeat_client, exam, attempt_id, "a") in (204, 400)

    async with get_sessionmaker()() as session:
        await session.execute(
            update(ExamSession)
            .where(ExamSession.id == exam_uuid)
            .values(created_at=ExamSession.created_at - timedelta(minutes=2))
        )
        await session.commit()
    late = await aeat_client.post(
        f"{API}/exams/{exam['id']}/questions/{attempt_id}/answer", json={"answer": {"optionId": "b"}}
    )
    assert late.status_code == 409 and late.json()["code"] == "EXAM_TIME_UP"

    submitted = (await aeat_client.post(f"{API}/exams/{exam['id']}/submit")).json()
    assert submitted["status"] == "submitted"
    async with get_sessionmaker()() as session:
        stored = await session.get(ExamSession, exam_uuid)
        assert stored is not None and stored.rules.get("autoSubmitted") is True


async def test_the_exam_list_offers_the_presets_and_the_sittings_that_simulate_the_paper_never_pause(
    aeat_client: AsyncClient,
) -> None:
    await _sign_up(aeat_client, "aeat_presets")
    presets = (await aeat_client.get(f"{API}/exams/presets")).json()
    by_id = {p["id"]: p for p in presets}
    assert len(presets) == 16
    assert by_id["primer-ejercicio"]["pause"] == "never"
    assert by_id["primer-ejercicio"]["timeLimitMinutes"] == 90
    assert by_id["bloque"]["pause"] == by_id["tema"]["pause"] == "between-questions"
    official = [p for p in presets if p["id"].startswith("conv")]
    assert len(official) == 13 and all(p["pause"] == "never" for p in official)


async def test_an_official_set_is_sat_in_printed_order_and_marked_with_a_quarter_penalty(
    aeat_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(aeat_client, "aeat_official")
    exam = (await aeat_client.post(f"{API}/exams", json={"presetId": "conv2025-a"})).json()
    assert [q["exerciseId"] for q in exam["questions"]] == ["ofi-conv2025-a"] * 79
    assert [q["questionId"] or q["variantId"] for q in exam["questions"]][:3] == ["q001", "q002", "q003"]
    options = await _options(registry, str(exam["id"]))
    attempts = [q["attemptId"] for q in exam["questions"]]
    # 60 right, 8 wrong, 11 blank: raw 60 - 8/4 = 58.
    for index, attempt_id in enumerate(attempts[:68]):
        pick = options[attempt_id][0] if index < 60 else options[attempt_id][1]
        assert await _answer(aeat_client, exam, attempt_id, pick) == 204
    result = (await aeat_client.post(f"{API}/exams/{exam['id']}/submit")).json()["result"]
    (part,) = result["parts"]
    assert (part["correct"], part["wrong"], part["blank"], part["raw"]) == (60, 8, 11, 58.0)
    assert "transformed" not in part
