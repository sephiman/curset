# SPDX-License-Identifier: AGPL-3.0-only
""" "Report this question": answered multiple-choice only, stored before mailed, retried, rate-limited."""

from __future__ import annotations

from httpx import AsyncClient
from sqlalchemy import select

from conftest import REPORT_ADDRESS, RecordingMailer
from tradeschool.db import get_sessionmaker
from tradeschool.reports.models import QuestionReport
from tradeschool.reports.service import DAILY_LIMIT, deliver_pending

CRYPTO = "/api/courses/crypto-futures"
OPOS = "/api/courses/fixture-oposiciones"
PASSWORD = "correcthorse"
MESSAGE = "The second option is also correct under the current rules."


async def _sign_up(client: AsyncClient, username: str, locale: str = "en") -> None:
    courses = ["crypto-futures", "fixture-oposiciones"]
    body = {"username": username, "password": PASSWORD, "locale": locale, "courses": courses}
    await client.post("/api/auth/register", json=body)
    await client.post("/api/auth/login", json={"username": username, "password": PASSWORD})


async def _answered_opos_attempt(client: AsyncClient, option: str = "b") -> str:
    opened = (await client.post(f"{OPOS}/exercises/m01-ex-1/attempts")).json()
    await client.post(f"{OPOS}/attempts/{opened['attemptId']}/answer", json={"answer": {"optionId": option}})
    return str(opened["attemptId"])


async def _reports() -> list[QuestionReport]:
    async with get_sessionmaker()() as session:
        return list((await session.scalars(select(QuestionReport))).all())


async def test_a_report_is_stored_and_mailed_with_every_field(
    multi_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _sign_up(multi_client, "reporter")
    attempt_id = await _answered_opos_attempt(multi_client)

    response = await multi_client.post(f"{OPOS}/attempts/{attempt_id}/report", json={"message": MESSAGE})
    assert response.status_code == 202

    [report] = await _reports()
    assert (report.course_id, report.module_id, report.lesson_id, report.exercise_id) == (
        "fixture-oposiciones",
        "m01",
        "m01-l1",
        "m01-ex-1",
    )
    assert report.variant_id == "plazo-alzada"
    assert report.username == "reporter"
    assert report.link.endswith("/courses/fixture-oposiciones/lessons/m01-l1#ex-m01-ex-1")
    assert report.emailed_at is not None

    [mail] = mailer.outbox
    assert mail.to == REPORT_ADDRESS
    for expected in (
        MESSAGE,
        "fixture-oposiciones",
        "m01-ex-1",
        "plazo-alzada",
        str(report.seed),
        "reporter",
        report.link,
    ):
        assert expected in mail.body, expected


async def test_a_spanish_only_course_is_reported_in_spanish_even_from_an_english_account(
    multi_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _sign_up(multi_client, "english", locale="en")
    attempt_id = await _answered_opos_attempt(multi_client, option="b")
    await multi_client.post(f"{OPOS}/attempts/{attempt_id}/report", json={"message": MESSAGE})

    [report] = await _reports()
    assert report.reading_locale == "es"
    assert report.prompt.startswith("¿Cuál es el plazo")
    assert report.given_answer == "Tres meses."
    assert report.correct_answer == "Un mes."
    assert "Tres meses." in mailer.outbox[0].body


async def test_an_unanswered_question_cannot_be_reported(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "eager")
    opened = (await multi_client.post(f"{OPOS}/exercises/m01-ex-1/attempts")).json()
    response = await multi_client.post(
        f"{OPOS}/attempts/{opened['attemptId']}/report", json={"message": MESSAGE}
    )
    assert response.status_code == 409
    assert response.json()["code"] == "REPORT_NOT_AVAILABLE"
    assert await _reports() == []


async def test_an_exam_question_is_reportable_only_after_submission(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "examinee")
    exam = (await multi_client.post(f"{OPOS}/exams", json={"scope": "global"})).json()
    question = exam["questions"][0]["attemptId"]
    in_progress = await multi_client.post(f"{OPOS}/attempts/{question}/report", json={"message": MESSAGE})
    assert in_progress.status_code == 409

    await multi_client.post(f"{OPOS}/exams/{exam['id']}/submit")
    reviewed = await multi_client.post(f"{OPOS}/attempts/{question}/report", json={"message": MESSAGE})
    assert reviewed.status_code == 202


async def test_one_report_per_attempt(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "twice")
    attempt_id = await _answered_opos_attempt(multi_client)
    assert (
        await multi_client.post(f"{OPOS}/attempts/{attempt_id}/report", json={"message": MESSAGE})
    ).status_code == 202
    again = await multi_client.post(f"{OPOS}/attempts/{attempt_id}/report", json={"message": MESSAGE})
    assert again.status_code == 409
    assert again.json()["code"] == "REPORT_ALREADY_SENT"


async def test_the_daily_limit_returns_a_clear_notice(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "prolific")
    for _ in range(DAILY_LIMIT):
        attempt_id = await _answered_opos_attempt(multi_client)
        assert (
            await multi_client.post(f"{OPOS}/attempts/{attempt_id}/report", json={"message": MESSAGE})
        ).status_code == 202
    attempt_id = await _answered_opos_attempt(multi_client)
    over = await multi_client.post(f"{OPOS}/attempts/{attempt_id}/report", json={"message": MESSAGE})
    assert over.status_code == 429
    assert over.json()["code"] == "REPORT_LIMIT_REACHED"
    assert over.json()["limit"] == DAILY_LIMIT


async def test_the_message_must_say_something_and_not_too_much(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "terse")
    attempt_id = await _answered_opos_attempt(multi_client)
    for message in ("Bad", "   ab   ", "x" * 1001):
        response = await multi_client.post(f"{OPOS}/attempts/{attempt_id}/report", json={"message": message})
        assert response.status_code == 422, message


async def test_a_calculation_is_not_a_multiple_choice_question(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "calculator")
    opened = (await multi_client.post(f"{CRYPTO}/exercises/m04-ex-1/attempts")).json()
    assert opened["type"] == "calculation"
    first = opened["payload"]["options"][0]["id"]
    await multi_client.post(
        f"{CRYPTO}/attempts/{opened['attemptId']}/answer", json={"answer": {"optionId": first}}
    )
    response = await multi_client.post(
        f"{CRYPTO}/attempts/{opened['attemptId']}/report", json={"message": MESSAGE}
    )
    assert response.status_code == 409


async def test_a_mail_failure_keeps_the_report_and_a_later_run_delivers_it(
    multi_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _sign_up(multi_client, "unlucky")
    attempt_id = await _answered_opos_attempt(multi_client)
    mailer.refusing = True
    assert (
        await multi_client.post(f"{OPOS}/attempts/{attempt_id}/report", json={"message": MESSAGE})
    ).status_code == 202
    [pending] = await _reports()
    assert pending.emailed_at is None and pending.email_attempts == 1
    assert mailer.outbox == []

    mailer.refusing = False
    assert await deliver_pending(get_sessionmaker(), mailer, REPORT_ADDRESS) == 1
    [delivered] = await _reports()
    assert delivered.emailed_at is not None and delivered.email_attempts == 2
    assert len(mailer.outbox) == 1


async def test_reporting_touches_neither_the_attempt_nor_progress(multi_client: AsyncClient) -> None:
    await _sign_up(multi_client, "neutral")
    attempt_id = await _answered_opos_attempt(multi_client, option="a")
    before_attempt = (await multi_client.get(f"{OPOS}/attempts/{attempt_id}")).json()
    before_stats = (await multi_client.get(f"{OPOS}/stats/me")).json()
    await multi_client.post(f"{OPOS}/attempts/{attempt_id}/report", json={"message": MESSAGE})
    assert (await multi_client.get(f"{OPOS}/attempts/{attempt_id}")).json() == before_attempt
    assert (await multi_client.get(f"{OPOS}/stats/me")).json() == before_stats
