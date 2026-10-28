# SPDX-License-Identifier: AGPL-3.0-only
"""Exam presets end to end on the Spanish-only fixture course (delta A, B3, D).

Its «Simulacro» is the acceptance preset: part 1 draws 40 questions from module m01 and 30 from m02
shuffled into one part (+2 reserve; the AGE «40 from bloques I to V + 30 from bloque VI», A8), part 2
offers two cases of 20 and grades the one marked, 100 minutes, a third off per wrong answer, blanks
free, 0 to 50 per part with the pass minimum at 25, part 2 graded only if part 1 reaches it.
"""

from __future__ import annotations

import uuid
from datetime import timedelta

import pytest
from httpx import AsyncClient
from sqlalchemy import select, update

from conftest import FIXTURE_CONTENT
from tradeschool.attempts.models import Attempt
from tradeschool.attempts.service import question_ref
from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.db import get_sessionmaker
from tradeschool.exams.models import ExamSession
from tradeschool.exercises.quiz import QuizGenerator

OPOS = "/api/courses/fixture-oposiciones"
PASSWORD = "correcthorse"


@pytest.fixture(scope="module")
def registry() -> CourseRegistry:
    return load_registry(FIXTURE_CONTENT / "fixture-oposiciones")


async def _sign_up(client: AsyncClient, username: str) -> None:
    body = {"username": username, "password": PASSWORD, "locale": "es", "courses": ["fixture-oposiciones"]}
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"username": username, "password": PASSWORD})


async def _correct_options(registry: CourseRegistry, exam_id: str) -> dict[str, str]:
    """attempt id → the option that grades correct, read the way the server grades it (seed + config)."""
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
    url = f"{OPOS}/exams/{exam['id']}/questions/{attempt_id}/answer"
    return (await client.post(url, json={"answer": {"optionId": option}})).status_code


async def _answer_pattern(
    client: AsyncClient,
    exam: dict[str, object],
    attempts: list[str],
    correct: dict[str, str],
    right: int,
    wrong: int,
) -> None:
    """The first `right` correct, the next `wrong` wrong, the rest left blank."""
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


async def _start_simulacro(client: AsyncClient) -> dict[str, object]:
    response = await client.post(f"{OPOS}/exams", json={"presetId": "simulacro"})
    assert response.status_code == 201, response.text
    return dict(response.json())


async def test_the_exam_list_shows_each_preset_with_parts_questions_and_time(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "lister")
    presets = (await multi_client.get(f"{OPOS}/exams/presets")).json()
    simulacro, tema = presets
    assert (simulacro["id"], simulacro["title"], simulacro["timeLimitMinutes"], simulacro["questions"]) == (
        "simulacro",
        "Simulacro",
        100,
        90,
    )
    assert [(p["kind"], p["questions"], p["choose"], p["penalty"]) for p in simulacro["parts"]] == [
        ("questions", 70, None, "1/3"),
        ("cases", 20, 2, "1/3"),
    ]
    # A parametric preset lists what it can be sat on: the lesson made only of cases has no pool.
    assert [t["id"] for t in tema["targets"]] == ["m01-l1", "m01-l2", "m02-l1"]


async def test_the_simulacro_draws_its_parts_offers_two_cases_and_runs_on_a_clock(
    multi_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(multi_client, "drawer")
    exam = await _start_simulacro(multi_client)
    assert len(_part(exam, "parte-1")) == 70 and len(_part(exam, "parte-1", reserve=True)) == 2
    part_two = exam["parts"][1]  # type: ignore[index]
    assert part_two["kind"] == "cases" and part_two["choose"] == 2
    assert {case["exerciseId"] for case in part_two["cases"]} == {"m02-ex-3", "m02-ex-4"}
    assert all(case["scenario"] for case in part_two["cases"])
    for case in part_two["cases"]:
        assert len(_part(exam, "parte-2", case=case["exerciseId"])) == 20
    # No question is drawn twice, and reserves come after the part's counted questions.
    drawn = [(q["exerciseId"], q["prompt"]) for q in exam["questions"] if q["partId"] == "parte-1"]  # type: ignore[union-attr]
    assert len(set(drawn)) == 72
    indices = [q["index"] for q in exam["questions"] if q["partId"] == "parte-1"]  # type: ignore[union-attr]
    assert indices == sorted(indices)
    # 100 minutes from the start, as the server counts it.
    assert exam["deadline"] is not None
    async with get_sessionmaker()() as session:
        stored = await session.get(ExamSession, uuid.UUID(str(exam["id"])))
        assert stored is not None
        assert stored.rules["presetId"] == "simulacro" and stored.rules["presetVersion"] == 2
        assert (stored.created_at + timedelta(minutes=100)).isoformat()[:19] == str(exam["deadline"])[:19]
    # Nothing is revealed while it runs: no answers, no lesson links.
    assert all(q["correctAnswer"] is None and q["lessonAnchor"] is None for q in exam["questions"])  # type: ignore[union-attr]


def _module(exercise_id: str) -> str:
    return exercise_id.split("-")[0]


async def test_a_composite_part_draws_each_sources_count_shuffled_into_one_part(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "composite")
    exam = await _start_simulacro(multi_client)
    questions = [q for q in exam["questions"] if q["partId"] == "parte-1"]  # type: ignore[union-attr]
    counted = [_module(q["exerciseId"]) for q in questions if not q["reserve"]]
    assert (counted.count("m01"), counted.count("m02")) == (40, 30)
    # Shuffled together, not one source after the other: m02 questions sit among the first forty.
    assert "m02" in counted[:40] and "m01" in counted[40:]
    # One part: one clock, one score row, the reserves still last.
    assert [part["id"] for part in exam["parts"]] == ["parte-1", "parte-2"]  # type: ignore[index]
    assert [q["reserve"] for q in questions] == [False] * 70 + [True] * 2
    presets = (await multi_client.get(f"{OPOS}/exams/presets")).json()
    assert presets[0]["parts"][0]["questions"] == 70


async def test_results_by_lesson_attribute_each_composite_question_to_its_lesson(
    multi_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(multi_client, "attributor")
    exam = await _start_simulacro(multi_client)
    counted = [q for q in exam["questions"] if q["partId"] == "parte-1" and not q["reserve"]]  # type: ignore[union-attr]
    expected: dict[str, int] = {}
    for question in counted:
        lesson_id = registry.question_lesson_id(question["exerciseId"], None)
        assert lesson_id is not None
        expected[lesson_id] = expected.get(lesson_id, 0) + 1
    submitted = (await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")).json()
    table = submitted["byLesson"]
    rows = {row["lessonId"]: row for group in table["groups"] for row in group["lessons"]}
    # Part 2 is not graded (all blank), so the table holds part 1 alone, each question under its lesson.
    assert {lesson_id: row["questions"] for lesson_id, row in rows.items()} == expected
    assert {group["moduleId"]: group["questions"] for group in table["groups"]} == {"m01": 40, "m02": 30}
    assert submitted["result"]["parts"][0]["questions"] == 70


async def test_only_the_marked_case_is_graded_and_scores_raw_and_transformed(
    multi_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(multi_client, "grader")
    exam = await _start_simulacro(multi_client)
    correct = await _correct_options(registry, str(exam["id"]))

    # Part 1: 50 right, 12 wrong, 8 blank → raw 50 - 12/3 = 46; both reserves right, and never counted.
    await _answer_pattern(multi_client, exam, _part(exam, "parte-1"), correct, 50, 12)
    await _answer_pattern(multi_client, exam, _part(exam, "parte-1", reserve=True), correct, 2, 0)
    # Part 2: case m02-ex-3 marked, 15 right, 3 wrong, 2 blank → raw 14. The other case all wrong: ignored.
    await _answer_pattern(multi_client, exam, _part(exam, "parte-2", case="m02-ex-3"), correct, 15, 3)
    await _answer_pattern(multi_client, exam, _part(exam, "parte-2", case="m02-ex-4"), correct, 0, 20)
    marks = await multi_client.put(
        f"{OPOS}/exams/{exam['id']}/parts/parte-2/cases", json={"exerciseIds": ["m02-ex-3"]}
    )
    assert marks.status_code == 204

    result = (await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")).json()["result"]
    one, two = result["parts"]
    assert (one["graded"], one["correct"], one["wrong"], one["blank"], one["questions"]) == (
        True,
        50,
        12,
        8,
        70,
    )
    assert one["raw"] == 46.0
    assert one["transformed"] == pytest.approx(25 + (46 - 35) * 25 / 35, abs=1e-4)
    assert (two["graded"], two["case"], two["correct"], two["wrong"], two["blank"]) == (
        True,
        "m02-ex-3",
        15,
        3,
        2,
    )
    assert two["raw"] == 14.0
    assert two["transformed"] == pytest.approx(35.0)
    assert result["raw"] == 60.0
    assert result["transformed"] == pytest.approx(one["transformed"] + 35.0, abs=1e-4)
    assert result["max"] == 100.0
    # The unscored summary counts the same 90 questions: the reserves and the other case are not in it.
    assert result["total"] == 90 and result["correct"] == 65


@pytest.mark.parametrize(
    ("marked", "reason"),
    [([], "no-case-marked"), (["m02-ex-3", "m02-ex-4"], "several-cases-marked")],
)
async def test_a_case_part_with_no_case_or_two_marked_is_not_graded(
    multi_client: AsyncClient, registry: CourseRegistry, marked: list[str], reason: str
) -> None:
    await _sign_up(multi_client, f"marker{len(marked)}")
    exam = await _start_simulacro(multi_client)
    correct = await _correct_options(registry, str(exam["id"]))
    await _answer_pattern(multi_client, exam, _part(exam, "parte-1"), correct, 70, 0)
    await _answer_pattern(multi_client, exam, _part(exam, "parte-2"), correct, 40, 0)
    await multi_client.put(f"{OPOS}/exams/{exam['id']}/parts/parte-2/cases", json={"exerciseIds": marked})

    result = (await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")).json()["result"]
    one, two = result["parts"]
    assert one["graded"] and one["transformed"] == 50.0
    assert (two["graded"], two["reason"]) == (False, reason)
    assert "transformed" not in two
    assert result["transformed"] == 50.0


async def test_part_two_waits_on_part_one_reaching_its_minimum(
    multi_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(multi_client, "waiter")
    exam = await _start_simulacro(multi_client)
    correct = await _correct_options(registry, str(exam["id"]))
    # 30 right, 30 wrong → raw 20 < 35: part 1 transforms below 25.
    await _answer_pattern(multi_client, exam, _part(exam, "parte-1"), correct, 30, 30)
    await _answer_pattern(multi_client, exam, _part(exam, "parte-2", case="m02-ex-4"), correct, 20, 0)
    await multi_client.put(
        f"{OPOS}/exams/{exam['id']}/parts/parte-2/cases", json={"exerciseIds": ["m02-ex-4"]}
    )

    result = (await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")).json()["result"]
    one, two = result["parts"]
    assert one["raw"] == 20.0 and one["transformed"] == pytest.approx(25 * 20 / 35, abs=1e-4)
    assert (two["graded"], two["reason"]) == (False, "previous-part-not-passed")


async def test_answers_and_marks_stop_when_the_time_is_up_but_submission_still_grades(
    multi_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(multi_client, "latecomer")
    exam = await _start_simulacro(multi_client)
    first = _part(exam, "parte-1")[0]
    assert await _answer(multi_client, exam, first, "a") == 204
    async with get_sessionmaker()() as session:
        await session.execute(
            update(ExamSession)
            .where(ExamSession.id == uuid.UUID(str(exam["id"])))
            .values(created_at=ExamSession.created_at - timedelta(minutes=101))
        )
        await session.commit()

    late = await multi_client.post(
        f"{OPOS}/exams/{exam['id']}/questions/{first}/answer", json={"answer": {"optionId": "b"}}
    )
    assert (late.status_code, late.json()["code"]) == (409, "EXAM_TIME_UP")
    marks = await multi_client.put(f"{OPOS}/exams/{exam['id']}/parts/parte-2/cases", json={"exerciseIds": []})
    assert marks.json()["code"] == "EXAM_TIME_UP"
    submitted = await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")
    assert submitted.status_code == 200
    reviewed = next(q for q in submitted.json()["questions"] if q["attemptId"] == first)
    assert reviewed["givenAnswer"] == {"optionId": "a"}


async def test_only_offered_cases_can_be_marked(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "intruder")
    exam = await _start_simulacro(multi_client)
    url = f"{OPOS}/exams/{exam['id']}/parts/parte-2/cases"
    assert (await multi_client.put(url, json={"exerciseIds": ["m01-ex-1"]})).json()[
        "code"
    ] == "EXAM_CASE_NOT_OFFERED"
    assert (
        await multi_client.put(f"{OPOS}/exams/{exam['id']}/parts/parte-1/cases", json={"exerciseIds": []})
    ).status_code == 404


async def test_results_by_lesson_group_by_module_rank_only_on_three_questions_and_skip_reserves(
    multi_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(multi_client, "tabler")
    exam = await _start_simulacro(multi_client)
    correct = await _correct_options(registry, str(exam["id"]))
    # Part 1 passes (raw 50 - 10/3 >= 35), so the marked case counts too.
    await _answer_pattern(multi_client, exam, _part(exam, "parte-1"), correct, 50, 10)
    await _answer_pattern(multi_client, exam, _part(exam, "parte-1", reserve=True), correct, 2, 0)
    await _answer_pattern(multi_client, exam, _part(exam, "parte-2", case="m02-ex-3"), correct, 10, 5)
    await multi_client.put(
        f"{OPOS}/exams/{exam['id']}/parts/parte-2/cases", json={"exerciseIds": ["m02-ex-3"]}
    )
    submitted = (await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")).json()

    table = submitted["byLesson"]
    rows = [row for group in table["groups"] for row in group["lessons"]]
    # 70 + the marked case's 20: no reserve, no question of the case left unmarked.
    assert sum(row["questions"] for row in rows) == 90
    assert sum(row["blank"] for row in rows) == 10 + 5
    assert [group["moduleId"] for group in table["groups"]] == ["m01", "m02"]
    for group in table["groups"]:
        assert group["questions"] == sum(row["questions"] for row in group["lessons"])
    for row in rows:
        assert row["pct"] == pytest.approx(row["correct"] / row["questions"], abs=1e-4)
    # Three lessons hold three questions or more, so the lists rank lessons, one entry each, never shared.
    lists = table["lists"]
    assert lists["level"] == "lesson"
    assert len(lists["best"]) == len(lists["worst"]) == 1
    assert lists["best"][0]["lessonId"] != lists["worst"][0]["lessonId"]
    assert all(entry["questions"] >= table["threshold"] for entry in lists["best"] + lists["worst"])


async def test_a_tema_exam_shows_the_table_without_lists(
    multi_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(multi_client, "tema")
    exam = (await multi_client.post(f"{OPOS}/exams", json={"presetId": "tema", "target": "m01-l2"})).json()
    assert len(exam["questions"]) == 20 and exam["targetTitle"] == "El recurso potestativo de reposición"
    submitted = (await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")).json()
    table = submitted["byLesson"]
    assert [row["lessonId"] for group in table["groups"] for row in group["lessons"]] == ["m01-l2"]
    assert table["groups"][0]["lessons"][0]["blank"] == 20
    assert table["lists"] is None
    # Unscored per part, but penalized: the blank rule leaves raw at 0.
    assert submitted["result"]["parts"][0]["raw"] == 0.0


async def test_a_lesson_that_cannot_supply_a_tema_exam_is_refused(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "refused")
    empty = await multi_client.post(f"{OPOS}/exams", json={"presetId": "tema", "target": "m02-l2"})
    assert (empty.status_code, empty.json()["code"]) == (409, "EXAM_EMPTY")
    unknown = await multi_client.post(f"{OPOS}/exams", json={"presetId": "tema", "target": "m09-l9"})
    assert (unknown.status_code, unknown.json()["code"]) == (400, "EXAM_BAD_SCOPE")


async def test_the_progress_tab_adds_up_practice_and_every_exam_per_lesson(
    multi_client: AsyncClient, registry: CourseRegistry
) -> None:
    await _sign_up(multi_client, "cumulative")
    opened = (await multi_client.post(f"{OPOS}/exercises/m01-ex-1/attempts")).json()
    await multi_client.post(
        f"{OPOS}/attempts/{opened['attemptId']}/answer", json={"answer": {"optionId": "a"}}
    )
    exam = (await multi_client.post(f"{OPOS}/exams", json={"presetId": "tema", "target": "m01-l1"})).json()
    await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")

    table = (await multi_client.get(f"{OPOS}/stats/me/by-lesson")).json()
    [row] = [row for group in table["groups"] for row in group["lessons"]]
    assert row["lessonId"] == "m01-l1"
    assert (row["questions"], row["correct"], row["blank"]) == (21, 1, 20)
    assert table["lists"] is None  # one lesson is not a ranking
    # It replaces nothing: the existing statistics are still there.
    assert (await multi_client.get(f"{OPOS}/stats/me")).json()["exercise"]["answered"] == 1
