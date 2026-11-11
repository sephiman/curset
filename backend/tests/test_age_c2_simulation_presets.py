# SPDX-License-Identifier: AGPL-3.0-only
"""The age-auxiliar-c2 presets (round R5): draw counts, scoring with the 2025 cut-offs, the clock."""

from __future__ import annotations

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
from tradeschool.exams.draw import SeededRand, counted_questions, draw_part, pool_shortfalls
from tradeschool.exams.models import ExamSession
from tradeschool.exams.presets import ExamPreset, PartScoring
from tradeschool.exams.print_export import build_exam_print
from tradeschool.exams.scoring import Tally, raw_score, transformed_score
from tradeschool.exercises.psicotecnico import PsicotecnicoConfig, build_item
from tradeschool.exercises.registry import get_generator
from tradeschool.psicotecnico.registry import load_generator
from tradeschool.psicotecnico.weights import apportion

CONTENT_DIR = Path(__file__).resolve().parent.parent.parent / "content" / "age-auxiliar-c2"
API = "/api/courses/age-auxiliar-c2"
PASSWORD = "correcthorse"

#: The sistema general cut-offs of the CPS note of 15-10-2026 (sources/programa.md), as exact fractions.
CUT_PART_1 = Fraction(29)
CUT_PART_2 = Fraction(64, 3)


@pytest.fixture(scope="module")
def registry() -> CourseRegistry:
    return load_registry(CONTENT_DIR)


def _preset(registry: CourseRegistry, preset_id: str) -> ExamPreset:
    return next(p for p in registry.manifest.exams if p.id == preset_id)


def _scoring(registry: CourseRegistry, preset_id: str, part_id: str) -> PartScoring:
    part = next(p for p in _preset(registry, preset_id).parts if p.id == part_id)
    assert part.scoring is not None
    return part.scoring


def test_the_declared_cut_offs_are_the_published_ones_as_exact_fractions(registry: CourseRegistry) -> None:
    assert _scoring(registry, "simulacro", "parte-1").minimum_raw == CUT_PART_1
    assert _scoring(registry, "simulacro", "parte-2").minimum_raw == CUT_PART_2
    assert _scoring(registry, "parte-1", "parte-1").minimum_raw == CUT_PART_1
    assert _scoring(registry, "parte-2", "parte-2").minimum_raw == CUT_PART_2


def test_a_raw_score_equal_to_the_cut_earns_exactly_25_and_a_third_below_it_less(
    registry: CourseRegistry,
) -> None:
    part_1 = _scoring(registry, "simulacro", "parte-1")
    part_2 = _scoring(registry, "simulacro", "parte-2")
    assert transformed_score(CUT_PART_1, 60, part_1) == 25
    assert transformed_score(CUT_PART_2, 50, part_2) == 25
    assert transformed_score(CUT_PART_1 - Fraction(1, 3), 60, part_1) < 25
    assert transformed_score(CUT_PART_2 - Fraction(1, 3), 50, part_2) < 25
    # The maximum raw score is the maximum mark.
    assert transformed_score(Fraction(60), 60, part_1) == 50
    assert transformed_score(Fraction(50), 50, part_2) == 50


def test_hand_computed_scores_at_the_minimum_a_third_below_it_and_with_blanks_and_wrongs(
    registry: CourseRegistry,
) -> None:
    part_1 = _scoring(registry, "simulacro", "parte-1")
    part_2 = _scoring(registry, "simulacro", "parte-2")
    penalty = Fraction(1, 3)

    # Exactly the minimum: 29 right, nothing wrong: 29 raw, 25 marks.
    at_minimum = raw_score(Tally(correct=29, wrong=0, blank=31), penalty, "free")
    assert at_minimum == 29
    assert transformed_score(at_minimum, 60, part_1) == 25

    # A third below it: 20 right, 2 wrong = 58/3 raw, two thirds of 29: 25 * (58/3) / 29 = 50/3.
    a_third_below = raw_score(Tally(correct=20, wrong=2, blank=38), penalty, "free")
    assert a_third_below == Fraction(58, 3)
    assert float(transformed_score(a_third_below, 60, part_1)) == pytest.approx(50 / 3)

    # A third of a point below the cut. Part 1: 29 right, 1 wrong = 86/3 raw, 25 * (86/3) / 29 = 2150/87
    # = 24.7126. Part 2: 21 right, nothing wrong = 21 = 64/3 - 1/3 raw, 25 * 21 / (64/3) = 1575/64 = 24.6094.
    one_below = raw_score(Tally(correct=29, wrong=1, blank=30), penalty, "free")
    assert one_below == CUT_PART_1 - Fraction(1, 3)
    assert transformed_score(one_below, 60, part_1) == Fraction(2150, 87)
    one_below_2 = raw_score(Tally(correct=21, wrong=0, blank=29), penalty, "free")
    assert one_below_2 == CUT_PART_2 - Fraction(1, 3)
    assert transformed_score(one_below_2, 50, part_2) == Fraction(1575, 64)
    # Exactly the part 2 cut: 22 right, 2 wrong = 64/3, 25 marks.
    assert transformed_score(raw_score(Tally(22, 2, 26), penalty, "free"), 50, part_2) == 25

    # With blanks and wrongs. Part 1: 40 right, 9 wrong, 11 blank: raw 37, 25 + (37 - 29) * 25 / 31 = 31.4516.
    p1 = raw_score(Tally(correct=40, wrong=9, blank=11), penalty, "free")
    assert p1 == 37
    assert float(transformed_score(p1, 60, part_1)) == pytest.approx(25 + 200 / 31)
    # Part 2: 38 right, 6 wrong, 6 blank: raw 36, 25 + (36 - 64/3) * 25 / (50 - 64/3) = 37.7907.
    p2 = raw_score(Tally(correct=38, wrong=6, blank=6), penalty, "free")
    assert p2 == 36
    assert float(transformed_score(p2, 50, part_2)) == pytest.approx(25 + 1100 / 86)

    # Blanks are free: the same 20 right with 40 blank leaves 20 raw.
    assert raw_score(Tally(correct=20, wrong=0, blank=40), penalty, "free") == 20


def test_every_preset_the_course_declares_can_be_supplied(registry: CourseRegistry) -> None:
    ids = [preset.id for preset in registry.manifest.exams]
    assert ids[:6] == ["simulacro", "parte-1", "parte-2", "psicotecnicos", "bloque", "tema"]
    for preset in registry.manifest.exams:
        if not preset.parametric:
            assert pool_shortfalls(registry, preset, None) == [], preset.id


def test_the_simulacro_draws_30_from_bloque_i_and_30_generated_with_5_reserve_last(
    registry: CourseRegistry,
) -> None:
    preset = _preset(registry, "simulacro")
    assert (preset.time_limit_minutes, preset.pause) == (90, "never")
    part_1, part_2 = preset.parts
    assert counted_questions(registry, part_1, None) == 60
    assert counted_questions(registry, part_2, None) == 50

    drawn_1 = draw_part(registry, part_1, None, SeededRand(42)).questions
    assert [q.reserve for q in drawn_1] == [False] * 60 + [True] * 5
    counted = drawn_1[:60]
    generated = [q for q in counted if registry.generator_use(q.exercise_id) is not None]
    stored = [q for q in counted if registry.generator_use(q.exercise_id) is None]
    assert len(generated) == 30
    assert len(stored) == 30
    assert all(q.exercise_id.startswith("m01-") for q in stored)
    assert all(q.exercise_id.startswith("m01-") for q in drawn_1[60:])
    assert len({(q.exercise_id, q.variant_id) for q in stored}) == 30

    drawn_2 = draw_part(registry, part_2, None, SeededRand(42)).questions
    assert [q.reserve for q in drawn_2] == [False] * 50 + [True] * 5
    assert all(q.exercise_id.startswith("m02-") for q in drawn_2)
    assert len({(q.exercise_id, q.variant_id) for q in drawn_2}) == 55


def test_the_generated_items_follow_the_generator_weights(registry: CourseRegistry) -> None:
    uses = registry.generator_uses()
    expected = dict(
        zip((use.exercise_id for use in uses), apportion([use.weight for use in uses], 30), strict=True)
    )
    for preset_id, part_id in (
        ("simulacro", "parte-1"),
        ("parte-1", "parte-1"),
        ("psicotecnicos", "psicotecnicos"),
    ):
        part = next(p for p in _preset(registry, preset_id).parts if p.id == part_id)
        for seed in (1, 2, 3):
            drawn = draw_part(registry, part, None, SeededRand(seed)).questions
            counts = Counter(
                q.exercise_id for q in drawn if registry.generator_use(q.exercise_id) is not None
            )
            assert {key: count for key, count in counts.items() if count} == {
                k: v for k, v in expected.items() if v
            }
    assert sum(expected.values()) == 30
    # The weights are the index's totals (docs/age-c2-psicotecnico-index.md, section 1).
    assert sum(use.weight for use in uses) == 175
    assert next(use.weight for use in uses if use.generator == "tablas-lectura") == 62


def test_the_psicotecnicos_preset_is_30_generated_items_timed_as_the_part_share(
    registry: CourseRegistry,
) -> None:
    preset = _preset(registry, "psicotecnicos")
    assert preset.time_limit_minutes == 25
    (part,) = preset.parts
    assert counted_questions(registry, part, None) == 30
    assert part.scoring is None


def test_the_parts_alone_get_their_share_of_the_90_minutes(registry: CourseRegistry) -> None:
    assert _preset(registry, "parte-1").time_limit_minutes == 49
    assert _preset(registry, "parte-2").time_limit_minutes == 41
    assert 49 + 41 == 90


def test_bloque_and_tema_are_parametric_over_the_bloques_and_the_temas(registry: CourseRegistry) -> None:
    from tradeschool.exams.draw import preset_targets

    assert preset_targets(registry, _preset(registry, "bloque")) == ["m01", "m02"]
    temas = preset_targets(registry, _preset(registry, "tema"))
    assert len(temas) == 28
    assert temas[0] == "m01-l01" and temas[-1] == "m02-l12"
    assert not any(t.startswith(("m00", "ps")) for t in temas)


def test_the_calibration_items_are_never_drawn(registry: CourseRegistry) -> None:
    assert registry.is_official("ps-calibracion")
    for seed in range(5):
        for part in _preset(registry, "simulacro").parts:
            drawn = draw_part(registry, part, None, SeededRand(seed)).questions
            assert all(q.exercise_id != "ps-calibracion" for q in drawn)


def test_the_same_seed_prints_the_same_paper_with_a_key_sheet_from_the_solver(
    registry: CourseRegistry,
) -> None:
    paper = build_exam_print(registry, "simulacro", "es", seed=7)
    assert paper == build_exam_print(registry, "simulacro", "es", seed=7)
    assert paper != build_exam_print(registry, "simulacro", "es", seed=8)
    assert paper["seed"] == 7

    part_1 = paper["parts"][0]["questions"]
    keys_1 = paper["keySheet"][0]["keys"]
    assert len(part_1) == len(keys_1) == 65
    assert [q["reserve"] for q in part_1] == [False] * 60 + [True] * 5
    generated = [(q, k) for q, k in zip(part_1, keys_1, strict=True) if q["id"].startswith("gen:")]
    assert len(generated) == 30
    for question, key in generated:
        generator_id, seed = question["id"].removeprefix("gen:").rsplit(":", 1)
        use = next(u for u in registry.generator_uses() if u.generator == generator_id)
        config = PsicotecnicoConfig(type="psicotecnico", generator=use.generator, difficulty=use.difficulty)
        item = build_item(config, int(seed))
        solved = load_generator(generator_id).solve(item)
        assert [o["text"] for o in question["options"]] == list(item.options)
        assert [o["letter"] for o in question["options"]] == ["A", "B", "C", "D"]
        assert key["correctLetter"] == "ABCD"[solved]
        assert key["number"] == question["number"]
    assert len(paper["parts"][1]["questions"]) == len(paper["keySheet"][1]["keys"]) == 55


@pytest.mark.parametrize("preset_id", ["simulacro", "parte-1"])
def test_part_1_puts_the_bloque_i_questions_first_and_the_psicotecnicos_after(
    registry: CourseRegistry, preset_id: str
) -> None:
    part = _preset(registry, preset_id).parts[0]
    assert part.order == "by-source"
    shuffled_within = False
    for seed in (1, 2, 3):
        drawn = draw_part(registry, part, None, SeededRand(seed)).questions
        assert all(registry.generator_use(q.exercise_id) is None for q in drawn[:30])
        assert all(registry.generator_use(q.exercise_id) is not None for q in drawn[30:60])
        assert all(q.exercise_id.startswith("m01-") for q in drawn[60:])
        stored = [q.exercise_id for q in drawn[:30]]
        types = [q.exercise_id for q in drawn[30:60]]
        shuffled_within |= stored != sorted(stored) and types != sorted(types)
    assert shuffled_within
    printed = build_exam_print(registry, preset_id, "es", seed=7)["parts"][0]["questions"]
    assert not any(q["id"].startswith("gen:") for q in printed[:30])
    assert all(q["id"].startswith("gen:") for q in printed[30:60])


def test_only_the_two_part_1_presets_print_by_source(registry: CourseRegistry) -> None:
    by_source = {p.id for p in registry.manifest.exams for part in p.parts if part.order == "by-source"}
    assert by_source == {"simulacro", "parte-1"}


async def _sign_up(client: AsyncClient, name: str) -> None:
    email = f"{name}@example.com"
    body = {
        "email": email,
        "name": name,
        "password": PASSWORD,
        "locale": "es",
        "courses": ["age-auxiliar-c2"],
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


def _attempts(exam: dict[str, object], part_id: str, *, reserve: bool = False) -> list[str]:
    questions = exam["questions"]
    assert isinstance(questions, list)
    return [q["attemptId"] for q in questions if q["partId"] == part_id and q["reserve"] is reserve]


async def _answer(client: AsyncClient, exam: dict[str, object], attempt_id: str, option: str) -> int:
    url = f"{API}/exams/{exam['id']}/questions/{attempt_id}/answer"
    return (await client.post(url, json={"answer": {"optionId": option}})).status_code


async def _answer_pattern(
    client: AsyncClient,
    exam: dict[str, object],
    attempts: list[str],
    options: dict[str, tuple[str, str]],
    right: int,
    wrong: int,
) -> None:
    for index, attempt_id in enumerate(attempts):
        if index < right:
            assert await _answer(client, exam, attempt_id, options[attempt_id][0]) == 204
        elif index < right + wrong:
            assert await _answer(client, exam, attempt_id, options[attempt_id][1]) == 204


async def test_a_sitting_scores_each_part_with_the_cps_transformation(
    c2_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(c2_client, "c2_simulacro")
    resp = await c2_client.post(f"{API}/exams", json={"presetId": "simulacro"})
    assert resp.status_code == 201
    exam = resp.json()
    assert len(exam["questions"]) == 65 + 55
    options = await _options(registry, str(exam["id"]))

    await _answer_pattern(c2_client, exam, _attempts(exam, "parte-1"), options, 40, 9)
    await _answer_pattern(c2_client, exam, _attempts(exam, "parte-2"), options, 38, 6)
    submitted = (await c2_client.post(f"{API}/exams/{exam['id']}/submit")).json()
    result = submitted["result"]

    part_1, part_2 = result["parts"]
    assert part_1["raw"] == 37.0 and part_1["passed"] is True
    assert part_1["transformed"] == pytest.approx(25 + 200 / 31, abs=0.01)
    assert part_2["graded"] is True and part_2["raw"] == 36.0
    assert part_2["transformed"] == pytest.approx(25 + 1100 / 86, abs=0.01)
    assert result["transformed"] == pytest.approx(25 + 200 / 31 + 25 + 1100 / 86, abs=0.02)
    # The psicotécnico types are rows of the results' «Por tema» table, in a group of their own.
    groups = {group["moduleId"]: group for group in submitted["byLesson"]["groups"]}
    assert groups["psicotecnicos"]["questions"] == 30
    type_rows = groups["psicotecnicos"]["lessons"]
    assert {row["kind"] for row in type_rows} == {"type"}
    assert sum(row["questions"] for row in type_rows) == 30
    assert {row["title"] for row in type_rows} >= {"Lectura de tablas", "Sinónimos"}


async def test_part_2_is_not_graded_when_part_1_stays_below_its_minimum(
    c2_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(c2_client, "c2_part_1_fails")
    exam = (await c2_client.post(f"{API}/exams", json={"presetId": "simulacro"})).json()
    options = await _options(registry, str(exam["id"]))

    # 28 right and 3 wrong: raw 27, below 29.
    await _answer_pattern(c2_client, exam, _attempts(exam, "parte-1"), options, 28, 3)
    await _answer_pattern(c2_client, exam, _attempts(exam, "parte-2"), options, 50, 0)
    result = (await c2_client.post(f"{API}/exams/{exam['id']}/submit")).json()["result"]

    assert result["parts"][0]["raw"] == 27.0
    assert result["parts"][0]["passed"] is False
    assert result["parts"][1]["graded"] is False
    assert result["parts"][1]["reason"] == "previous-part-not-passed"


@pytest.mark.parametrize(("right", "wrong", "graded"), [(29, 0, True), (29, 1, False)])
async def test_part_2_is_graded_from_exactly_the_part_1_cut_and_not_a_third_below_it(
    c2_client: AsyncClient, registry: CourseRegistry, right: int, wrong: int, graded: bool
) -> None:
    await _sign_up(c2_client, f"c2_cut_{right}_{wrong}")
    exam = (await c2_client.post(f"{API}/exams", json={"presetId": "simulacro"})).json()
    options = await _options(registry, str(exam["id"]))
    await _answer_pattern(c2_client, exam, _attempts(exam, "parte-1"), options, right, wrong)
    # Part 2 at exactly its cut: 22 right, 2 wrong = 64/3, 25 marks.
    await _answer_pattern(c2_client, exam, _attempts(exam, "parte-2"), options, 22, 2)
    result = (await c2_client.post(f"{API}/exams/{exam['id']}/submit")).json()["result"]
    part_1, part_2 = result["parts"]
    assert part_1["passed"] is graded
    assert part_1["transformed"] == pytest.approx(25 if graded else 2150 / 87, abs=1e-4)
    assert part_2["graded"] is graded
    if graded:
        assert part_2["raw"] == pytest.approx(64 / 3, abs=1e-4)
        assert part_2["transformed"] == 25 and part_2["passed"] is True
    else:
        assert part_2["reason"] == "previous-part-not-passed"


async def test_a_sitting_is_submitted_when_the_90_minutes_run_out(c2_client: AsyncClient) -> None:
    await _sign_up(c2_client, "c2_times_out")
    exam = (await c2_client.post(f"{API}/exams", json={"presetId": "simulacro"})).json()
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
    # Still inside the 90 minutes.
    assert await _answer(c2_client, exam, attempt_id, "a") in (204, 400)

    async with get_sessionmaker()() as session:
        await session.execute(
            update(ExamSession)
            .where(ExamSession.id == exam_uuid)
            .values(created_at=ExamSession.created_at - timedelta(minutes=2))
        )
        await session.commit()
    late = await c2_client.post(
        f"{API}/exams/{exam['id']}/questions/{attempt_id}/answer", json={"answer": {"optionId": "b"}}
    )
    assert late.status_code == 409 and late.json()["code"] == "EXAM_TIME_UP"

    submitted = (await c2_client.post(f"{API}/exams/{exam['id']}/submit")).json()
    assert submitted["status"] == "submitted"
    async with get_sessionmaker()() as session:
        stored = await session.get(ExamSession, exam_uuid)
        assert stored is not None and stored.rules.get("autoSubmitted") is True


async def test_the_exam_list_offers_the_presets_and_the_sitting_never_pauses(c2_client: AsyncClient) -> None:
    await _sign_up(c2_client, "c2_presets")
    presets = (await c2_client.get(f"{API}/exams/presets")).json()
    by_id = {p["id"]: p for p in presets}
    assert {"simulacro", "parte-1", "parte-2", "psicotecnicos", "bloque", "tema"} <= set(by_id)
    assert by_id["simulacro"]["pause"] == "never"
    assert by_id["simulacro"]["timeLimitMinutes"] == 90


async def test_the_print_endpoint_regenerates_the_same_paper_from_its_seed(c2_client: AsyncClient) -> None:
    await _sign_up(c2_client, "c2_print")
    first = (await c2_client.get(f"{API}/exams/presets/simulacro/print?seed=11")).json()
    again = (await c2_client.get(f"{API}/exams/presets/simulacro/print?seed=11")).json()
    assert first == again
    assert first["seed"] == 11
    assert first["timeLimitMinutes"] == 90
    generated = [q for q in first["parts"][0]["questions"] if q["id"].startswith("gen:")]
    assert len(generated) == 30
