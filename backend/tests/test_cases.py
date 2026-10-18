# SPDX-License-Identifier: AGPL-3.0-only
"""The case exercise (delta B): practice question by question, stats per tema, reports, print, shuffle."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
import yaml
from httpx import AsyncClient
from sqlalchemy import select

from conftest import FIXTURE_CONTENT, RecordingMailer
from tradeschool.content.print_export import build_print_exercise
from tradeschool.content.registry import ContentError, CourseRegistry, load_registry
from tradeschool.db import get_sessionmaker
from tradeschool.exercises.case import CaseConfig, CaseGenerator
from tradeschool.reports.models import QuestionReport

OPOS = "/api/courses/fixture-oposiciones"
COURSE = FIXTURE_CONTENT / "fixture-oposiciones"
PASSWORD = "correcthorse"


@pytest.fixture(scope="module")
def registry() -> CourseRegistry:
    return load_registry(COURSE)


async def _sign_up(client: AsyncClient, username: str) -> None:
    body = {"username": username, "password": PASSWORD, "locale": "es", "courses": ["fixture-oposiciones"]}
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"username": username, "password": PASSWORD})


async def test_a_case_opens_with_its_scenario_and_one_attempt_per_question_in_order(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "reader")
    case = (await multi_client.post(f"{OPOS}/exercises/m02-ex-3/case-attempts")).json()
    assert case["title"] == "El permiso denegado"
    assert case["scenario"].startswith("Una funcionaria")
    assert [q["questionId"] for q in case["questions"]] == [f"q{n:02d}" for n in range(1, 21)]
    assert len({q["attemptId"] for q in case["questions"]}) == 20
    # The statement only: four options each, never a correct flag.
    assert all(len(q["payload"]["options"]) == 4 for q in case["questions"])
    assert all("correct" not in option for q in case["questions"] for option in q["payload"]["options"])
    # A case is never opened as a single exercise.
    single = await multi_client.post(f"{OPOS}/exercises/m02-ex-3/attempts")
    assert single.json()["code"] == "EXERCISE_IS_A_CASE"


async def test_each_case_question_is_graded_alone_and_counts_under_its_own_tema(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "solver")
    case = (await multi_client.post(f"{OPOS}/exercises/m02-ex-3/case-attempts")).json()
    for question in case["questions"]:
        graded = await multi_client.post(
            f"{OPOS}/attempts/{question['attemptId']}/answer", json={"answer": {"optionId": "a"}}
        )
        assert graded.status_code == 200
        link = graded.json()["lessonLink"]
        # «Ver en la lección» goes to the lesson the question names, at what it cites.
        assert link["lessonId"] == question["lessonId"] and link["anchor"]

    stats = (await multi_client.get(f"{OPOS}/stats/me")).json()
    by_module = {m["id"]: m for m in stats["modules"]}
    # q01 to q14 belong to m01's lessons and q15 to q20 to m02-l1: counted there, not as one unit in m02-l2.
    assert by_module["m01"]["firstSeen"] == 14 and by_module["m02"]["firstSeen"] == 6
    assert stats["exercise"]["answered"] == 20
    # The two cases' forty questions are units of their temas, on top of the banks' own exercises.
    assert by_module["m01"]["exercisesTotal"] == 3 + 2 * 14
    assert by_module["m02"]["exercisesTotal"] == 2 + 2 * 6


async def test_a_case_question_report_names_the_case_its_citation_and_its_lesson_anchor(
    multi_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _sign_up(multi_client, "caseReporter")
    case = (await multi_client.post(f"{OPOS}/exercises/m02-ex-3/case-attempts")).json()
    question = case["questions"][15]  # q16: m02-l1, cites art. 10.1 LRJSP
    await multi_client.post(
        f"{OPOS}/attempts/{question['attemptId']}/answer", json={"answer": {"optionId": "b"}}
    )
    sent = await multi_client.post(
        f"{OPOS}/attempts/{question['attemptId']}/report",
        json={"message": "La clave no coincide con el artículo."},
    )
    assert sent.status_code == 202

    async with get_sessionmaker()() as session:
        [report] = (await session.scalars(select(QuestionReport))).all()
    assert (report.exercise_id, report.variant_id, report.case_title) == (
        "m02-ex-3",
        "q16",
        "El permiso denegado",
    )
    assert report.citation == "art. 10.1 LRJSP"
    assert report.lesson_anchor is not None
    assert report.lesson_anchor.endswith("/courses/fixture-oposiciones/lessons/m02-l1#lrjsp-art-10")
    body = mailer.outbox[0].body
    assert "El permiso denegado" in body and "art. 10.1 LRJSP" in body and report.lesson_anchor in body


def test_answer_shuffles_are_per_question_and_the_question_order_is_fixed(registry: CourseRegistry) -> None:
    config = registry.case_config("m02-ex-3")
    assert config is not None
    orders = set()
    for seed in range(40):
        instance = CaseGenerator().generate(config, seed, "es")
        questions = instance.payload["questions"]
        assert isinstance(questions, list)
        assert [q["id"] for q in questions] == [q.id for q in config.questions]
        orders.add(tuple(tuple(o["id"] for o in q["payload"]["options"]) for q in questions[:3]))
    # Each question shuffles on its own seed: three questions of one case do not move together.
    assert len(orders) > 30


def test_the_printed_case_is_its_scenario_then_its_questions_with_one_key_entry_each(
    registry: CourseRegistry,
) -> None:
    printed = build_print_exercise(registry, "m02-ex-4", "es")
    payload, answer = printed["payload"], printed["answer"]
    assert isinstance(payload, dict) and isinstance(answer, dict)
    assert printed["type"] == "case" and str(payload["scenario"]).startswith("Una empresa")
    questions = payload["questions"]
    keys = answer["questions"]
    assert isinstance(questions, list) and isinstance(keys, list)
    # The bijection: every printed question has exactly one key entry, under the same number.
    assert (
        [q["number"] for q in questions] == [k["number"] for k in keys] == [f"2.4.{n}" for n in range(1, 21)]
    )
    for question, key in zip(questions, keys, strict=True):
        shown = {option["id"] for option in question["payload"]["options"]}
        assert key["optionIds"][0] in shown


def _copy_course(tmp_path: Path) -> Path:
    target = tmp_path / "fixture-oposiciones"
    shutil.copytree(COURSE, target)
    return target


def _edit_case(course: Path, edit: object) -> None:
    path = course / "exercises" / "m02-ex-3.yaml"
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    edit(raw)  # type: ignore[operator]
    path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")


@pytest.mark.parametrize(
    ("edit", "message"),
    [
        (lambda raw: raw.update(questions=raw["questions"][:9]), "10 to 25 questions"),
        (lambda raw: raw["scenario"].update(es="Mira la figura.\n\n::figure{id=fig-x}"), "text only"),
        (lambda raw: raw["questions"][0].update(lesson="m09-l9"), "a lesson the course does not have"),
    ],
)
def test_a_malformed_case_fails_the_load(tmp_path: Path, edit: object, message: str) -> None:
    course = _copy_course(tmp_path)
    _edit_case(course, edit)
    with pytest.raises((ContentError, ValueError), match=message):
        load_registry(course)


def test_the_case_config_is_parsed_as_written(registry: CourseRegistry) -> None:
    config = registry.case_config("m02-ex-3")
    assert isinstance(config, CaseConfig)
    assert config.questions[15].lesson == "m02-l1" and config.questions[15].citation == "art. 10.1 LRJSP"
