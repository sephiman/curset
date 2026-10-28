# SPDX-License-Identifier: AGPL-3.0-only
"""Draw a lesson's practice round. Its attempts are ordinary practice attempts, opened per question."""

from __future__ import annotations

import uuid

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.attempts.models import Attempt, AttemptState
from tradeschool.content.registry import CourseRegistry, QuestionRef
from tradeschool.errors import AppError
from tradeschool.practice.order import MASTERED_AFTER, Rand, practice_order

#: «20 al azar», the default round.
ROUND_SIZE = 20


async def _mastered(
    session: AsyncSession, registry: CourseRegistry, user_id: uuid.UUID, question_ids: list[str]
) -> set[str]:
    """Questions the learner has answered correctly at least MASTERED_AFTER times in practice."""
    rows = await session.execute(
        select(Attempt.variant_id)
        .where(
            Attempt.user_id == user_id,
            Attempt.course_id == registry.slug,
            Attempt.exam_session_id.is_(None),
            Attempt.state == AttemptState.ANSWERED,
            Attempt.is_correct.is_(True),
            Attempt.variant_id.in_(question_ids),
        )
        .group_by(Attempt.variant_id)
        .having(func.count() >= MASTERED_AFTER)
    )
    return {str(variant_id) for (variant_id,) in rows.all()}


async def draw_round(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    lesson_id: str,
    every: bool,
    rand: Rand,
) -> list[QuestionRef]:
    if not registry.manifest.course.lesson_practice:
        raise AppError("PRACTICE_NOT_AVAILABLE", "This course has no lesson practice.", status_code=409)
    if registry.lesson_location(lesson_id) is None:
        raise AppError("LESSON_NOT_FOUND", f"No lesson {lesson_id!r}.", status_code=404)
    questions = registry.lesson_questions(lesson_id)
    if not questions:
        raise AppError("PRACTICE_EMPTY", "This lesson has no questions to practise.", status_code=409)
    by_id = {q.variant_id: q for q in questions if q.variant_id is not None}
    mastered = await _mastered(session, registry, user_id, list(by_id))
    order = practice_order(list(by_id), mastered, None if every else ROUND_SIZE, rand)
    return [by_id[qid] for qid in order]
