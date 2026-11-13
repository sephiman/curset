# SPDX-License-Identifier: AGPL-3.0-only
"""The `spaced` practice scheduler: its pure rule, and the rounds it serves through the real endpoints."""

from __future__ import annotations

import random
import uuid
from datetime import UTC, datetime, timedelta

from httpx import AsyncClient
from sqlalchemy import update

from pipeline_courses import FIXTURE_CONTENT
from tradeschool.attempts.models import Attempt
from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.db import get_sessionmaker
from tradeschool.exercises.quiz import QuizConfig
from tradeschool.practice.spaced import RETURN_AFTER_DAYS, Answer, due_at, spaced_order

NOW = datetime(2026, 6, 1, 12, tzinfo=UTC)
OPOS = "/api/courses/fixture-oposiciones"


def _right(days_ago: float) -> Answer:
    return Answer(NOW - timedelta(days=days_ago), True)


def _wrong(days_ago: float) -> Answer:
    return Answer(NOW - timedelta(days=days_ago), False)


def test_a_question_never_failed_is_never_due() -> None:
    assert due_at([_right(10), _right(2)]) is None


def test_a_failed_question_returns_after_one_day() -> None:
    assert due_at([_wrong(0)]) == NOW + timedelta(days=RETURN_AFTER_DAYS[0])


def test_each_correct_answer_after_a_failure_lengthens_the_wait() -> None:
    waits = [
        due_at([_wrong(20), *[_right(20 - n) for n in range(1, run + 1)]])
        for run in range(len(RETURN_AFTER_DAYS))
    ]
    gaps = [(due - NOW).days + 20 - run for run, due in enumerate(waits) if due]
    assert gaps == list(RETURN_AFTER_DAYS)


def test_a_new_failure_resets_the_wait() -> None:
    answers = [_wrong(30), _right(25), _right(20), _right(15), _wrong(1)]
    assert due_at(answers) == NOW - timedelta(days=1) + timedelta(days=RETURN_AFTER_DAYS[0])


def test_the_wait_stops_growing_after_the_last_step() -> None:
    answers = [_wrong(100), *[_right(90 - n) for n in range(12)]]
    assert due_at(answers) == answers[-1].at + timedelta(days=RETURN_AFTER_DAYS[-1])


def test_unseen_questions_come_first_then_due_ones_then_the_rest() -> None:
    history = {
        "due-late": [_wrong(9)],
        "due-soon": [_wrong(2)],
        "not-due": [_wrong(0)],
        "right-old": [_right(30)],
    }
    ids = ["right-old", "not-due", "due-soon", "new-a", "due-late", "new-b"]
    order = spaced_order(ids, history, NOW, None, random.Random(1))
    assert set(order[:2]) == {"new-a", "new-b"}
    assert order[2:] == ["due-late", "due-soon", "right-old", "not-due"]


def test_a_round_is_cut_to_the_requested_count() -> None:
    assert len(spaced_order([f"q{n}" for n in range(30)], {}, NOW, 20, random.Random(1))) == 20


def _registry() -> CourseRegistry:
    return load_registry(FIXTURE_CONTENT / "fixture-oposiciones")


async def _sign_up(client: AsyncClient, name: str) -> None:
    email = f"{name}@example.com"
    body = {
        "email": email,
        "name": name,
        "password": "correcthorse",
        "locale": "es",
        "courses": ["fixture-oposiciones"],
    }
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"email": email, "password": "correcthorse"})


def _option(registry: CourseRegistry, exercise_id: str, question_id: str, *, correct: bool) -> str:
    config = registry.exercise_configs[exercise_id][1]
    assert isinstance(config, QuizConfig)
    variant = next(v for v in config.variants if v.id == question_id)
    return next(o.id for o in variant.options if o.correct is correct)


async def _answer(
    client: AsyncClient, registry: CourseRegistry, question: dict[str, str], *, correct: bool
) -> str:
    exercise_id, question_id = question["exerciseId"], question["questionId"]
    opened = await client.post(f"{OPOS}/exercises/{exercise_id}/attempts", json={"variantId": question_id})
    attempt_id = str(opened.json()["attemptId"])
    option = _option(registry, exercise_id, question_id, correct=correct)
    await client.post(f"{OPOS}/attempts/{attempt_id}/answer", json={"answer": {"optionId": option}})
    return attempt_id


async def _backdate(attempt_id: str, days: int) -> None:
    async with get_sessionmaker()() as session:
        attempt = await session.get(Attempt, uuid.UUID(attempt_id))
        assert attempt is not None and attempt.answered_at is not None
        await session.execute(
            update(Attempt)
            .where(Attempt.id == attempt.id)
            .values(answered_at=attempt.answered_at - timedelta(days=days))
        )
        await session.commit()


async def _round(client: AsyncClient) -> list[dict[str, str]]:
    drawn = await client.post(f"{OPOS}/lessons/m02-l1/practice", json={"all": True})
    questions: list[dict[str, str]] = drawn.json()["questions"]
    return questions


async def test_an_answered_question_is_served_after_every_unseen_one(spaced_client: AsyncClient) -> None:
    await _sign_up(spaced_client, "nuevas")
    first = (await _round(spaced_client))[0]
    await _answer(spaced_client, _registry(), first, correct=True)
    order = [q["questionId"] for q in await _round(spaced_client)]
    assert order[-1] == first["questionId"]


async def test_a_failed_question_returns_ahead_of_other_seen_ones_once_its_day_has_passed(
    spaced_client: AsyncClient,
) -> None:
    await _sign_up(spaced_client, "falladas")
    registry = _registry()
    right, failed = (await _round(spaced_client))[:2]
    await _answer(spaced_client, registry, right, correct=True)
    wrong_attempt = await _answer(spaced_client, registry, failed, correct=False)
    await _backdate(wrong_attempt, days=2)
    order = [q["questionId"] for q in await _round(spaced_client)]
    assert order[-2:] == [failed["questionId"], right["questionId"]]


async def test_the_mixed_review_draws_across_lessons_unseen_first(spaced_client: AsyncClient) -> None:
    await _sign_up(spaced_client, "mixto")
    first = (await _round(spaced_client))[0]
    await _answer(spaced_client, _registry(), first, correct=True)
    review = (await spaced_client.post(f"{OPOS}/practice/review", json={"count": 100})).json()["questions"]
    lessons_with_questions = {q["questionId"] for q in review}
    assert len(lessons_with_questions) == len(review) > len(await _round(spaced_client))
    assert review[-1]["questionId"] == first["questionId"]


async def test_options_keep_their_order_when_an_attempt_is_reopened(spaced_client: AsyncClient) -> None:
    await _sign_up(spaced_client, "opciones")
    registry = _registry()
    question = (await _round(spaced_client))[0]
    opened = await spaced_client.post(
        f"{OPOS}/exercises/{question['exerciseId']}/attempts", json={"variantId": question["questionId"]}
    )
    shown = [o["id"] for o in opened.json()["payload"]["options"]]
    attempt_id = opened.json()["attemptId"]
    option = _option(registry, question["exerciseId"], question["questionId"], correct=True)
    await spaced_client.post(f"{OPOS}/attempts/{attempt_id}/answer", json={"answer": {"optionId": option}})
    reviewed = (await spaced_client.get(f"{OPOS}/attempts/{attempt_id}")).json()
    assert [o["id"] for o in reviewed["payload"]["options"]] == shown


async def test_the_mixed_review_is_refused_by_a_course_that_did_not_opt_in(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "sinrepaso")
    refused = await multi_client.post(f"{OPOS}/practice/review")
    assert refused.status_code == 409 and refused.json()["code"] == "PRACTICE_NOT_AVAILABLE"


async def test_a_course_without_the_scheduler_still_draws_the_weighted_random_order(
    multi_client: AsyncClient,
) -> None:
    await _sign_up(multi_client, "aleatorio")
    registry = _registry()
    first = (await multi_client.post(f"{OPOS}/lessons/m02-l1/practice", json={"all": True})).json()[
        "questions"
    ][0]
    await _answer(multi_client, registry, first, correct=True)
    seen_first = {
        (await multi_client.post(f"{OPOS}/lessons/m02-l1/practice", json={"all": True})).json()["questions"][
            0
        ]["questionId"]
        for _ in range(30)
    }
    assert len(seen_first) > 1


async def test_the_mixed_review_keeps_two_exercises_that_share_a_variant_id_apart(
    shared_variant_client: AsyncClient,
) -> None:
    course = "/api/courses/fixture-tecnico"
    body = {"email": "c@example.com", "name": "c", "password": "correcthorse", "locale": "en"}
    await shared_variant_client.post("/api/auth/register", json={**body, "courses": ["fixture-tecnico"]})
    await shared_variant_client.post(
        "/api/auth/login", json={"email": body["email"], "password": "correcthorse"}
    )
    review = (await shared_variant_client.post(f"{course}/practice/review", json={"count": 100})).json()
    served = [(q["exerciseId"], q["questionId"]) for q in review["questions"]]
    first = served[0][1]
    assert sorted(e for e, q in served if q == first) == ["m01-ex-1", "m01-ex-2"]
    assert len(served) == len(set(served))
