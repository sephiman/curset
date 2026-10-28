# SPDX-License-Identifier: AGPL-3.0-only
"""Lesson practice: a round of a lesson's questions, each opened and answered as a practice attempt."""

from __future__ import annotations

import random
import uuid
from collections import Counter

import pytest
from httpx import AsyncClient

from pipeline_courses import FIXTURE_CONTENT
from tradeschool.attempts.models import Attempt
from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.db import get_sessionmaker
from tradeschool.exercises.quiz import QuizConfig
from tradeschool.practice import router as practice_router
from tradeschool.practice.order import practice_order

OPOS = "/api/courses/fixture-oposiciones"
CRYPTO = "/api/courses/crypto-futures"


def _registry() -> CourseRegistry:
    return load_registry(FIXTURE_CONTENT / "fixture-oposiciones")


def test_a_mastered_question_comes_up_less_often() -> None:
    ids = [f"q{n:02d}" for n in range(40)]
    rand = random.Random(11)
    seen = Counter(qid for _ in range(2000) for qid in practice_order(ids, {"q00"}, 20, rand))
    others = sum(seen[qid] for qid in ids[1:]) / 39
    assert seen["q00"] < others / 2


def test_a_round_holds_each_question_once_and_all_of_them_when_asked() -> None:
    ids = [f"q{n:02d}" for n in range(40)]
    twenty = practice_order(ids, set(), 20, random.Random(3))
    assert len(twenty) == len(set(twenty)) == 20 and set(twenty) <= set(ids)
    assert sorted(practice_order(ids, {"q01"}, None, random.Random(3))) == ids


async def _sign_up(client: AsyncClient, username: str) -> None:
    body = {
        "username": username,
        "password": "correcthorse",
        "locale": "es",
        "courses": ["fixture-oposiciones"],
    }
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"username": username, "password": "correcthorse"})


def _correct(registry: CourseRegistry, exercise_id: str, question_id: str) -> str:
    config = registry.exercise_configs[exercise_id][1]
    assert isinstance(config, QuizConfig)
    variant = next(v for v in config.variants if v.id == question_id)
    return next(option.id for option in variant.options if option.correct)


async def _practise(
    client: AsyncClient, exercise_id: str, question_id: str, option: str
) -> dict[str, object]:
    opened = await client.post(f"{OPOS}/exercises/{exercise_id}/attempts", json={"variantId": question_id})
    assert opened.status_code == 201
    attempt_id = opened.json()["attemptId"]
    graded = await client.post(f"{OPOS}/attempts/{attempt_id}/answer", json={"answer": {"optionId": option}})
    return {"attemptId": attempt_id, **graded.json()}


async def test_a_round_draws_twenty_of_the_lessons_questions_or_all_of_them(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "practica")
    lesson = {q.variant_id for q in _registry().lesson_questions("m02-l1")}
    twenty = (await multi_client.post(f"{OPOS}/lessons/m02-l1/practice")).json()["questions"]
    every = (await multi_client.post(f"{OPOS}/lessons/m02-l1/practice", json={"all": True})).json()[
        "questions"
    ]
    assert len({q["questionId"] for q in twenty}) == 20 and {q["questionId"] for q in twenty} <= lesson
    assert {q["questionId"] for q in every} == lesson and len(every) == len(lesson)


async def test_a_practised_question_is_stored_by_its_id_counts_in_stats_and_can_be_reported(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "repaso")
    first = (await multi_client.post(f"{OPOS}/lessons/m02-l1/practice")).json()["questions"][0]
    exercise_id, question_id = first["exerciseId"], first["questionId"]
    graded = await _practise(
        multi_client, exercise_id, question_id, _correct(_registry(), exercise_id, question_id)
    )
    assert graded["correct"] is True and graded["explanation"]

    async with get_sessionmaker()() as session:
        attempt = await session.get(Attempt, uuid.UUID(str(graded["attemptId"])))
    assert attempt is not None and attempt.variant_id == question_id and attempt.exam_session_id is None

    stats = (await multi_client.get(f"{OPOS}/stats/me")).json()
    assert next(m for m in stats["modules"] if m["id"] == "m02")["answered"] == 1
    report = await multi_client.post(
        f"{OPOS}/attempts/{graded['attemptId']}/report", json={"message": "La respuesta correcta no es esa."}
    )
    assert report.status_code == 202


async def test_a_question_answered_right_twice_comes_up_less_often(
    multi_client: AsyncClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    await _sign_up(multi_client, "dominado")
    registry = _registry()
    mastered = registry.lesson_questions("m02-l1")[0]
    assert mastered.variant_id is not None
    for _ in range(2):
        option = _correct(registry, mastered.exercise_id, mastered.variant_id)
        await _practise(multi_client, mastered.exercise_id, mastered.variant_id, option)

    seeded = random.Random(5)
    monkeypatch.setattr(practice_router.random, "SystemRandom", lambda: seeded)
    seen: Counter[str] = Counter()
    for _ in range(60):
        drawn = (await multi_client.post(f"{OPOS}/lessons/m02-l1/practice")).json()["questions"]
        seen.update(q["questionId"] for q in drawn)
    others = [n for qid, n in seen.items() if qid != mastered.variant_id]
    assert seen[mastered.variant_id] < sum(others) / len(others) / 2


async def test_a_question_outside_the_exercise_cannot_be_opened(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "intruso")
    opened = await multi_client.post(f"{OPOS}/exercises/m02-ex-1/attempts", json={"variantId": "alzada-01"})
    assert opened.status_code == 404 and opened.json()["code"] == "QUESTION_NOT_FOUND"


async def test_a_course_without_lesson_practice_keeps_its_embedded_quizzes(multi_client: AsyncClient) -> None:
    body = {"username": "trader", "password": "correcthorse", "locale": "en", "courses": ["crypto-futures"]}
    await multi_client.post("/api/auth/register", json=body)
    await multi_client.post("/api/auth/login", json={"username": "trader", "password": "correcthorse"})
    refused = await multi_client.post(f"{CRYPTO}/lessons/m01-l1/practice")
    assert refused.status_code == 409 and refused.json()["code"] == "PRACTICE_NOT_AVAILABLE"
    course = (await multi_client.get(CRYPTO)).json()
    assert "lessonPractice" not in course["course"]
    lessons = [lesson for block in course["blocks"] for m in block["modules"] for lesson in m["lessons"]]
    assert all("practiceQuestions" not in lesson for lesson in lessons)
