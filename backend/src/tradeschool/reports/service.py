# SPDX-License-Identifier: AGPL-3.0-only
"""Filing a question report (stored first, mailed second) and retrying the ones not yet mailed."""

from __future__ import annotations

import asyncio
import logging
import uuid
from datetime import UTC, datetime

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from tradeschool.attempts.models import Attempt, AttemptState
from tradeschool.attempts.service import load_owned
from tradeschool.auth.mail import Mailer
from tradeschool.auth.models import User
from tradeschool.content.registry import CourseRegistry
from tradeschool.errors import AppError
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator
from tradeschool.exercises.registry import get_generator
from tradeschool.exercises.reveal import dummy_answer
from tradeschool.exercises.types import ExerciseType
from tradeschool.reports.answers import describe_correct, describe_given
from tradeschool.reports.mail import report_mail
from tradeschool.reports.models import QuestionReport

logger = logging.getLogger("tradeschool.reports")

DAILY_LIMIT = 10
MESSAGE_MIN = 5
MESSAGE_MAX = 1000


def _start_of_day() -> datetime:
    return datetime.now(UTC).replace(hour=0, minute=0, second=0, microsecond=0)


async def _reportable(
    session: AsyncSession, registry: CourseRegistry, user: User, attempt_id: uuid.UUID
) -> Attempt:
    """An answered multiple-choice attempt of this course; never one whose answer is still hidden."""
    attempt = await load_owned(session, registry, user.id, attempt_id)
    exercise_id = registry.exercise_id_for_key(attempt.exercise_id)
    config = registry.get_exercise_config(exercise_id) if exercise_id else None
    # OPEN covers an exam in progress too: its attempts only become ANSWERED when it is submitted.
    if attempt.state != AttemptState.ANSWERED or config is None or config[0] is not ExerciseType.QUIZ:
        raise AppError("REPORT_NOT_AVAILABLE", "This question cannot be reported.", status_code=409)
    return attempt


async def _check_limits(session: AsyncSession, user_id: uuid.UUID, attempt_id: uuid.UUID) -> None:
    already = await session.scalar(select(QuestionReport.id).where(QuestionReport.attempt_id == attempt_id))
    if already is not None:
        raise AppError("REPORT_ALREADY_SENT", "This question has already been reported.", status_code=409)
    today = await session.scalar(
        select(func.count(QuestionReport.id)).where(
            QuestionReport.user_id == user_id, QuestionReport.created_at >= _start_of_day()
        )
    )
    if (today or 0) >= DAILY_LIMIT:
        raise AppError(
            "REPORT_LIMIT_REACHED",
            f"You can send {DAILY_LIMIT} reports a day.",
            status_code=429,
            extra={"limit": DAILY_LIMIT},
        )


async def file_report(
    session: AsyncSession,
    registry: CourseRegistry,
    user: User,
    attempt_id: uuid.UUID,
    message: str,
    locale: str,
    public_url: str,
) -> QuestionReport:
    """Store the report with every field filled in by the server; the client sent only text + attempt."""
    attempt = await _reportable(session, registry, user, attempt_id)
    await _check_limits(session, user.id, attempt.id)

    exercise_id = registry.exercise_id_for_key(attempt.exercise_id) or attempt.exercise_id
    _, config = registry.get_exercise_config(exercise_id) or (None, None)
    assert isinstance(config, QuizConfig)
    generator = get_generator(ExerciseType.QUIZ)
    assert isinstance(generator, QuizGenerator)
    instance = generator.generate(config, attempt.seed, locale)
    graded = generator.grade(
        config, attempt.seed, attempt.given_answer or dummy_answer(instance.payload), locale
    )
    location = registry.exercise_location(exercise_id)
    lesson_id = registry.exercise_lesson_id(exercise_id) or ""

    report = QuestionReport(
        user_id=user.id,
        attempt_id=attempt.id,
        message=message,
        course_id=registry.slug,
        module_id=location[1] if location else "",
        lesson_id=lesson_id,
        exercise_id=exercise_id,
        variant_id=generator.variant(config, attempt.seed).id,
        seed=attempt.seed,
        reading_locale=locale,
        prompt=instance.prompt,
        given_answer=describe_given(instance.payload, attempt.given_answer, locale),
        correct_answer=describe_correct(graded.correct_answer, locale),
        username=user.username,
        link=f"{public_url.rstrip('/')}/courses/{registry.slug}/lessons/{lesson_id}#ex-{exercise_id}",
    )
    session.add(report)
    await session.commit()
    await session.refresh(report)
    return report


async def deliver_pending(sessionmaker: async_sessionmaker[AsyncSession], mailer: Mailer, to: str) -> int:
    """Mail every stored report the server has not accepted yet; a failure stays pending for next time."""
    if not (mailer.enabled and to):
        return 0
    delivered = 0
    async with sessionmaker() as session:
        pending = (
            await session.scalars(
                select(QuestionReport.id)
                .where(QuestionReport.emailed_at.is_(None))
                .order_by(QuestionReport.created_at)
            )
        ).all()
    for report_id in pending:
        async with sessionmaker() as session:
            # Row-locked while it is mailed, so two concurrent runs never send one report twice.
            report = await session.scalar(
                select(QuestionReport)
                .where(QuestionReport.id == report_id, QuestionReport.emailed_at.is_(None))
                .with_for_update(skip_locked=True)
            )
            if report is None:
                continue
            subject, body = report_mail(report)
            accepted = await asyncio.to_thread(mailer.deliver, to, subject, body)
            report.email_attempts += 1
            if accepted:
                report.emailed_at = datetime.now(UTC)
                delivered += 1
            else:
                logger.warning("question report %s not mailed (attempt %d)", report.id, report.email_attempts)
            await session.commit()
    return delivered
