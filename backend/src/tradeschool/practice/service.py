# SPDX-License-Identifier: AGPL-3.0-only
"""Draw a lesson's practice round. Its attempts are ordinary practice attempts, opened per question."""

from __future__ import annotations

import uuid
from collections import Counter
from collections.abc import Iterable, Sequence
from datetime import UTC, datetime

from sqlalchemy import func, select, tuple_
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.attempts.models import Attempt, AttemptState
from tradeschool.content.registry import CourseRegistry, QuestionRef
from tradeschool.content.schema import PracticePreset
from tradeschool.errors import AppError
from tradeschool.practice.order import MASTERED_AFTER, Rand, practice_order
from tradeschool.practice.spaced import Answer, spaced_order
from tradeschool.psicotecnico.weights import apportion

#: «20 al azar», the default round.
ROUND_SIZE = 20

#: A practice set serves at most this many questions of one family.
FAMILY_CAP = 2

#: (exercise id, variant id): a variant id alone is unique only within its exercise.
type QuestionKey = tuple[str, str]


def _key(question: QuestionRef) -> QuestionKey | None:
    return None if question.variant_id is None else (question.exercise_id, question.variant_id)


def _by_key(questions: Iterable[QuestionRef]) -> dict[QuestionKey, QuestionRef]:
    return {key: q for q in questions if (key := _key(q)) is not None}


def _pool(stored: Iterable[QuestionRef], generated: Iterable[QuestionRef]) -> dict[QuestionKey, QuestionRef]:
    """Stored questions by key, plus FAMILY_CAP never-seen slots per generated family."""
    slots = {(q.exercise_id, f"#{slot}"): q for q in generated for slot in range(FAMILY_CAP)}
    return {**_by_key(stored), **slots}


def _capped(
    order: Sequence[QuestionKey], questions: dict[QuestionKey, QuestionRef], count: int | None
) -> list[QuestionRef]:
    """The first `count` of `order` (all when None), at most FAMILY_CAP per family."""
    taken: list[QuestionRef] = []
    per_family: Counter[str] = Counter()
    for key in order:
        question = questions[key]
        if question.family is not None:
            if per_family[question.family] >= FAMILY_CAP:
                continue
            per_family[question.family] += 1
        taken.append(question)
        if count is not None and len(taken) == count:
            break
    return taken


async def _mastered(
    session: AsyncSession, registry: CourseRegistry, user_id: uuid.UUID, keys: list[QuestionKey]
) -> set[QuestionKey]:
    """Questions the learner has answered correctly at least MASTERED_AFTER times in practice."""
    rows = await session.execute(
        select(Attempt.exercise_id, Attempt.variant_id)
        .where(
            Attempt.user_id == user_id,
            Attempt.course_id == registry.slug,
            Attempt.exam_session_id.is_(None),
            Attempt.state == AttemptState.ANSWERED,
            Attempt.is_correct.is_(True),
            tuple_(Attempt.exercise_id, Attempt.variant_id).in_(keys),
        )
        .group_by(Attempt.exercise_id, Attempt.variant_id)
        .having(func.count() >= MASTERED_AFTER)
    )
    return {(exercise_id, str(variant_id)) for exercise_id, variant_id in rows.all()}


async def _history(
    session: AsyncSession, registry: CourseRegistry, user_id: uuid.UUID, keys: list[QuestionKey]
) -> dict[QuestionKey, list[Answer]]:
    rows = await session.execute(
        select(Attempt.exercise_id, Attempt.variant_id, Attempt.answered_at, Attempt.is_correct).where(
            Attempt.user_id == user_id,
            Attempt.course_id == registry.slug,
            Attempt.exam_session_id.is_(None),
            Attempt.state == AttemptState.ANSWERED,
            Attempt.answered_at.is_not(None),
            tuple_(Attempt.exercise_id, Attempt.variant_id).in_(keys),
        )
    )
    history: dict[QuestionKey, list[Answer]] = {}
    for exercise_id, variant_id, answered_at, is_correct in rows.all():
        history.setdefault((exercise_id, str(variant_id)), []).append(Answer(answered_at, bool(is_correct)))
    return history


async def _ordered(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    questions: dict[QuestionKey, QuestionRef],
    count: int | None,
    rand: Rand,
) -> list[QuestionRef]:
    keys = [key for key, q in questions.items() if q.variant_id is not None]
    generated = [key for key, q in questions.items() if q.variant_id is None]
    if registry.manifest.course.practice_scheduler == "spaced":
        history = await _history(session, registry, user_id, keys)
        order = spaced_order([*keys, *generated], history, datetime.now(UTC), None, rand)
    else:
        mastered = await _mastered(session, registry, user_id, keys)
        order = practice_order([*keys, *generated], mastered, None, rand)
    return _capped(order, questions, count)


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
    if not questions and not registry.generated_questions({lesson_id}):
        raise AppError("PRACTICE_EMPTY", "This lesson has no questions to practise.", status_code=409)
    pool = _pool(questions, registry.generated_questions({lesson_id}))
    return await _ordered(session, registry, user_id, pool, None if every else ROUND_SIZE, rand)


async def draw_review_round(
    session: AsyncSession, registry: CourseRegistry, user_id: uuid.UUID, count: int, rand: Rand
) -> list[QuestionRef]:
    """The mixed review: the scheduler's pick across every lesson of a course that opted in."""
    if registry.manifest.course.practice_scheduler != "spaced":
        raise AppError("PRACTICE_NOT_AVAILABLE", "This course has no mixed review.", status_code=409)
    pool = _pool(
        (q for _, lesson in registry.manifest.iter_lessons() for q in registry.lesson_questions(lesson.id)),
        registry.generated_questions(),
    )
    if not pool:
        raise AppError("PRACTICE_EMPTY", "This course has no questions to review.", status_code=409)
    return await _ordered(session, registry, user_id, pool, count, rand)


def _require_preset(registry: CourseRegistry, preset: PracticePreset) -> None:
    if preset not in registry.manifest.course.practice_presets:
        raise AppError("PRACTICE_NOT_AVAILABLE", f"This course has no {preset} practice.", status_code=409)


async def draw_module_round(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    module_id: str,
    every: bool,
    rand: Rand,
) -> list[QuestionRef]:
    _require_preset(registry, "module")
    if registry.module_block(module_id) is None:
        raise AppError("MODULE_NOT_FOUND", f"No module {module_id!r}.", status_code=404)
    lesson_ids = set(registry.module_lesson_ids(module_id))
    pool = _pool(registry.module_questions(module_id), registry.generated_questions(lesson_ids))
    if not pool:
        raise AppError("PRACTICE_EMPTY", "This module has no questions to practise.", status_code=409)
    return await _ordered(session, registry, user_id, pool, None if every else ROUND_SIZE, rand)


async def draw_code_reading_round(
    session: AsyncSession, registry: CourseRegistry, user_id: uuid.UUID, count: int, rand: Rand
) -> list[QuestionRef]:
    _require_preset(registry, "code-reading")
    pool = _pool(registry.code_reading_questions(), registry.generated_questions(code_reading_only=True))
    if not pool:
        raise AppError("PRACTICE_EMPTY", "This course has no code-reading questions.", status_code=409)
    return await _ordered(session, registry, user_id, pool, count, rand)


def draw_generated_round(
    registry: CourseRegistry, generator: str | None, count: int, rand: Rand
) -> list[str]:
    """The generated exercises of a «Psicotécnicos» round: one type, or all in the course's weights."""
    uses = registry.generator_uses()
    if not uses:
        raise AppError("PSICOTECNICOS_NOT_AVAILABLE", "This course has no psicotécnicos.", status_code=409)
    if generator is not None:
        chosen = next((use for use in uses if use.generator == generator), None)
        if chosen is None:
            raise AppError("GENERATOR_NOT_FOUND", f"No psicotécnico type {generator!r}.", status_code=404)
        return [chosen.exercise_id] * count
    shares = apportion([use.weight for use in uses], count)
    capped = "generators" in registry.manifest.course.practice_presets
    items = [
        use.exercise_id
        for use, share in zip(uses, shares, strict=True)
        for _ in range(min(share, FAMILY_CAP) if capped else share)
    ]
    return sorted(items, key=lambda _: rand.random())
