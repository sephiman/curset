# SPDX-License-Identifier: AGPL-3.0-only
"""Clock, pause, and per-question time in exams (delta section G)."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta

import pytest
from httpx import AsyncClient

from conftest import FIXTURE_CONTENT
from tradeschool.content.registry import CourseRegistry, load_registry
from tradeschool.db import get_sessionmaker
from tradeschool.exams.models import ExamSession

OPOS = "/api/courses/fixture-oposiciones"
PASSWORD = "correcthorse"


@pytest.fixture(scope="module")
def registry() -> CourseRegistry:
    return load_registry(FIXTURE_CONTENT / "fixture-oposiciones")


async def _sign_up(client: AsyncClient, username: str) -> None:
    body = {"username": username, "password": PASSWORD, "locale": "es", "courses": ["fixture-oposiciones"]}
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"username": username, "password": PASSWORD})


async def test_pause_allowed_and_refused_by_preset(multi_client: AsyncClient) -> None:
    """Simulacro defaults to never pause; Tema defaults to between-questions."""
    await _sign_up(multi_client, "pause_preset_user")

    # 1. Simulacro (pause: never)
    simulacro = (await multi_client.post(f"{OPOS}/exams", json={"presetId": "simulacro"})).json()
    assert simulacro["pause"] == "never"

    first_q = simulacro["questions"][0]
    # Answer first question
    await multi_client.post(
        f"{OPOS}/exams/{simulacro['id']}/questions/{first_q['attemptId']}/answer",
        json={"answer": {"optionId": "a"}, "timeSeconds": 15.0},
    )
    # Attempting to pause should fail with 409 EXAM_PAUSE_NOT_ALLOWED
    resp = await multi_client.post(
        f"{OPOS}/exams/{simulacro['id']}/pause", json={"attemptId": first_q["attemptId"]}
    )
    assert resp.status_code == 409
    assert resp.json()["code"] == "EXAM_PAUSE_NOT_ALLOWED"

    # 2. Tema (pause: between-questions)
    tema = (await multi_client.post(f"{OPOS}/exams", json={"presetId": "tema", "target": "m01-l1"})).json()
    assert tema["pause"] == "between-questions"


async def test_pause_only_after_answering_and_guards(multi_client: AsyncClient) -> None:
    """Pause control only enabled once question answered; pausing stops actions; resume unpauses."""
    await _sign_up(multi_client, "pause_guard_user")
    tema = (await multi_client.post(f"{OPOS}/exams", json={"presetId": "tema", "target": "m01-l1"})).json()
    first_q = tema["questions"][0]
    second_q = tema["questions"][1]

    # Trying to pause before answering first question -> 409 EXAM_PAUSE_NOT_ANSWERED
    resp = await multi_client.post(
        f"{OPOS}/exams/{tema['id']}/pause", json={"attemptId": first_q["attemptId"]}
    )
    assert resp.status_code == 409
    assert resp.json()["code"] == "EXAM_PAUSE_NOT_ANSWERED"

    # Answer first question
    ans_resp = await multi_client.post(
        f"{OPOS}/exams/{tema['id']}/questions/{first_q['attemptId']}/answer",
        json={"answer": {"optionId": "a"}, "timeSeconds": 12.5, "clockUsedSeconds": 12.5},
    )
    assert ans_resp.status_code == 204

    # Now pausing on first question succeeds
    pause_resp = await multi_client.post(
        f"{OPOS}/exams/{tema['id']}/pause", json={"attemptId": first_q["attemptId"]}
    )
    assert pause_resp.status_code == 204

    # Exam state is paused
    view = (await multi_client.get(f"{OPOS}/exams/{tema['id']}")).json()
    assert view["paused"] is True

    # Answering while paused returns 409 EXAM_PAUSED
    ans_paused = await multi_client.post(
        f"{OPOS}/exams/{tema['id']}/questions/{second_q['attemptId']}/answer",
        json={"answer": {"optionId": "b"}, "timeSeconds": 5.0},
    )
    assert ans_paused.status_code == 409
    assert ans_paused.json()["code"] == "EXAM_PAUSED"

    # Resume succeeds
    resume_resp = await multi_client.post(f"{OPOS}/exams/{tema['id']}/resume")
    assert resume_resp.status_code == 204

    view_after = (await multi_client.get(f"{OPOS}/exams/{tema['id']}")).json()
    assert view_after["paused"] is False

    # Second question is still unanswered, trying to pause on second question returns 409
    pause_q2 = await multi_client.post(
        f"{OPOS}/exams/{tema['id']}/pause", json={"attemptId": second_q["attemptId"]}
    )
    assert pause_q2.status_code == 409
    assert pause_q2.json()["code"] == "EXAM_PAUSE_NOT_ANSWERED"


async def test_per_question_times_and_aggregations(multi_client: AsyncClient) -> None:
    """Per-question time stored with attempt, aggregated per part, per lesson in review and progress."""
    await _sign_up(multi_client, "timing_user")

    tema = (await multi_client.post(f"{OPOS}/exams", json={"presetId": "tema", "target": "m01-l1"})).json()
    exam_id = tema["id"]

    # Answer 2 questions with time_seconds
    q0 = tema["questions"][0]
    q1 = tema["questions"][1]
    await multi_client.post(
        f"{OPOS}/exams/{exam_id}/questions/{q0['attemptId']}/answer",
        json={"answer": {"optionId": "a"}, "timeSeconds": 10.0, "clockUsedSeconds": 10.0},
    )
    await multi_client.post(
        f"{OPOS}/exams/{exam_id}/questions/{q1['attemptId']}/answer",
        json={"answer": {"optionId": "b"}, "timeSeconds": 20.0, "clockUsedSeconds": 30.0},
    )

    # Submit
    submitted = (await multi_client.post(f"{OPOS}/exams/{exam_id}/submit")).json()
    result = submitted["result"]
    assert "totalActiveSeconds" in result
    assert result["totalActiveSeconds"] >= 30.0
    assert result["parts"][0]["activeSeconds"] >= 30.0

    # Review questions contain timeSeconds
    review = (await multi_client.get(f"{OPOS}/exams/{exam_id}/review")).json()
    rev_q0 = next(q for q in review["questions"] if q["attemptId"] == q0["attemptId"])
    rev_q1 = next(q for q in review["questions"] if q["attemptId"] == q1["attemptId"])
    rev_q2 = next(q for q in review["questions"] if q["attemptId"] == tema["questions"][2]["attemptId"])

    assert rev_q0["timeSeconds"] == 10.0
    assert rev_q1["timeSeconds"] == 20.0
    assert rev_q2["timeSeconds"] is None

    # byLesson table shows averageSeconds
    by_lesson = submitted["byLesson"]
    [m01_group] = [g for g in by_lesson["groups"] if g["moduleId"] == "m01"]
    [l1_row] = [row for row in m01_group["lessons"] if row["lessonId"] == "m01-l1"]
    assert l1_row["averageSeconds"] == 15.0  # (10 + 20) / 2

    # Progress (/stats/me/by-lesson) also shows cumulative averageSeconds
    progress_table = (await multi_client.get(f"{OPOS}/stats/me/by-lesson")).json()
    [p_l1_row] = [
        row for g in progress_table["groups"] for row in g["lessons"] if row["lessonId"] == "m01-l1"
    ]
    assert p_l1_row["averageSeconds"] == 15.0


async def test_time_limit_auto_submit(multi_client: AsyncClient) -> None:
    """When exam deadline passes, submitting records autoSubmitted: True."""
    await _sign_up(multi_client, "timeout_user")

    exam = (await multi_client.post(f"{OPOS}/exams", json={"presetId": "simulacro"})).json()
    exam_id = uuid.UUID(exam["id"])

    # Fast forward the clock in DB so deadline is in the past
    past = datetime.now(UTC) - timedelta(minutes=120)
    async with get_sessionmaker()() as session:
        stored = await session.get(ExamSession, exam_id)
        assert stored is not None
        stored.created_at = past
        clock = dict(stored.rules.get("clock", {}))
        clock["startedAt"] = past.isoformat()
        clock["lastResumedAt"] = past.isoformat()
        stored.rules = {**stored.rules, "clock": clock}
        await session.commit()

    # Now call submit
    submitted = (await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")).json()
    assert submitted["result"]["autoSubmitted"] is True


async def test_reload_resumes_correct_time_and_never_counts_while_closed(
    multi_client: AsyncClient,
) -> None:
    """Pause freezes active time across reloads; never keeps ticking wall-clock time."""
    await _sign_up(multi_client, "reload_user")

    # 1. Preset with between-questions (Tema): paused exam stays frozen
    tema = (await multi_client.post(f"{OPOS}/exams", json={"presetId": "tema", "target": "m01-l1"})).json()
    q0 = tema["questions"][0]
    await multi_client.post(
        f"{OPOS}/exams/{tema['id']}/questions/{q0['attemptId']}/answer",
        json={"answer": {"optionId": "a"}, "timeSeconds": 14.0, "clockUsedSeconds": 14.0},
    )
    await multi_client.post(f"{OPOS}/exams/{tema['id']}/pause", json={"attemptId": q0["attemptId"]})

    # Simulate passing 10 minutes while paused
    async with get_sessionmaker()() as session:
        stored = await session.get(ExamSession, uuid.UUID(tema["id"]))
        assert stored is not None
        stored.created_at = stored.created_at - timedelta(minutes=10)
        await session.commit()

    # Reload sitting: active time is still 14.0, not + 10 minutes
    view = (await multi_client.get(f"{OPOS}/exams/{tema['id']}")).json()
    assert view["paused"] is True
    assert view["activeSeconds"] == 14.0

    # 2. Preset with never (Simulacro): time keeps running while closed
    simulacro = (await multi_client.post(f"{OPOS}/exams", json={"presetId": "simulacro"})).json()
    # Simulate 5 minutes passed with tab closed
    five_min_ago = datetime.now(UTC) - timedelta(minutes=5)
    async with get_sessionmaker()() as session:
        stored_sim = await session.get(ExamSession, uuid.UUID(simulacro["id"]))
        assert stored_sim is not None
        stored_sim.created_at = five_min_ago
        clock = dict(stored_sim.rules.get("clock", {}))
        clock["startedAt"] = five_min_ago.isoformat()
        clock["lastResumedAt"] = five_min_ago.isoformat()
        stored_sim.rules = {**stored_sim.rules, "clock": clock}
        await session.commit()

    # Reload sitting: active time reflects the 5 minutes (approx 300s)
    sim_view = (await multi_client.get(f"{OPOS}/exams/{simulacro['id']}")).json()
    assert sim_view["paused"] is False
    assert 295.0 <= sim_view["activeSeconds"] <= 305.0
