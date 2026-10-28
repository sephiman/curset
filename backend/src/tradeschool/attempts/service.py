# SPDX-License-Identifier: AGPL-3.0-only
"""Attempt lifecycle: open a seeded scenario, answer it (graded server-side), review it from its seed."""

from __future__ import annotations

import logging
import secrets
import uuid
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime

from sqlalchemy import or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from tradeschool.attempts.models import Attempt, AttemptState
from tradeschool.citations.course import QuestionLink
from tradeschool.citations.excerpt_store import SolutionText
from tradeschool.content.registry import CourseRegistry, QuestionRef
from tradeschool.errors import AppError
from tradeschool.exercises.base import GeneratedInstance, GradeResult, InvalidAnswerError
from tradeschool.exercises.case import question_seeds
from tradeschool.exercises.quiz import QuizConfig
from tradeschool.exercises.registry import get_generator
from tradeschool.exercises.types import ExerciseType

logger = logging.getLogger("tradeschool.attempts")

_SEED_SPACE = 2**62


@dataclass
class OpenedAttempt:
    attempt: Attempt
    instance: GeneratedInstance
    exercise_type: ExerciseType
    # The display id the API speaks; the attempt row itself stores the permanent key.
    exercise_id: str


def _resolve(registry: CourseRegistry, exercise_id: str) -> tuple[ExerciseType, object]:
    config = registry.get_exercise_config(exercise_id)
    if config is None:
        # Distinguish "no such exercise in the course" from "declared but not yet playable".
        known = any(ex.id == exercise_id for _, _, ex in registry.manifest.iter_exercises())
        if known:
            raise AppError(
                "EXERCISE_NOT_AVAILABLE", f"Exercise {exercise_id!r} is not available.", status_code=409
            )
        raise AppError("EXERCISE_NOT_FOUND", f"No exercise {exercise_id!r}.", status_code=404)
    return config


def question_ref(registry: CourseRegistry, attempt: Attempt) -> QuestionRef:
    """The question a stored attempt showed, in the exercise that holds it today; a key the manifest
    dropped keeps its raw form."""
    return registry.locate(attempt.exercise_id, attempt.question_id, attempt.variant_id)


def _resolve_attempt(registry: CourseRegistry, attempt: Attempt) -> tuple[ExerciseType, object]:
    """What grades this one attempt: the question it showed, or its exercise when the seed is the question."""
    ref = question_ref(registry, attempt)
    _resolve(registry, ref.exercise_id)
    found = registry.attempt_config(ref)
    if found is None:
        raise AppError("EXERCISE_NOT_AVAILABLE", "This question is no longer available.", status_code=409)
    return found


def _only_question(registry: CourseRegistry, exercise_id: str, variant_id: str) -> object:
    found = registry.attempt_config(QuestionRef(exercise_id, variant_id=variant_id))
    if found is None:
        raise AppError(
            "QUESTION_NOT_FOUND", f"No question {variant_id!r} in {exercise_id!r}.", status_code=404
        )
    return found[1]


async def open_attempt(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    exercise_id: str,
    locale: str,
    variant_id: str | None = None,
) -> OpenedAttempt:
    exercise_type, config = _resolve(registry, exercise_id)
    if variant_id is not None:
        config = _only_question(registry, exercise_id, variant_id)
    if exercise_type is ExerciseType.CASE:
        raise AppError(
            "EXERCISE_IS_A_CASE", "A case is opened as a case, question by question.", status_code=409
        )
    exercise_key = registry.exercise_key(exercise_id)  # attempts store the permanent key
    generator = get_generator(exercise_type)
    seed = secrets.randbelow(_SEED_SPACE)
    instance = generator.generate(config, seed, locale)  # type: ignore[arg-type]

    # Abandoned rule (§3.4): opening a new practice attempt abandons any prior unanswered practice one
    # for this exercise. Scoped to practice (exam_session_id IS NULL) so it never disturbs an in-flight
    # exam question for the same exercise (and exam sampling never abandons a practice attempt).
    await session.execute(
        update(Attempt)
        .where(
            Attempt.user_id == user_id,
            Attempt.course_id == registry.slug,
            Attempt.exercise_id == exercise_key,
            Attempt.state == AttemptState.OPEN,
            Attempt.exam_session_id.is_(None),
        )
        .values(state=AttemptState.ABANDONED)
    )
    attempt = Attempt(
        user_id=user_id,
        course_id=registry.slug,
        exercise_id=exercise_key,
        variant_id=variant_id or registry.drawn_variant_id(exercise_id, seed),
        seed=seed,
        instance_snapshot={
            "type": exercise_type.value,
            "prompt": instance.prompt,
            "payload": instance.payload,
        },
        state=AttemptState.OPEN,
    )
    session.add(attempt)
    await session.commit()
    await session.refresh(attempt)
    logger.info(
        "attempt_opened attempt=%s exercise=%s variant=%s type=%s",
        attempt.id,
        exercise_key,
        attempt.variant_id,
        exercise_type.value,
    )
    return OpenedAttempt(
        attempt=attempt, instance=instance, exercise_type=exercise_type, exercise_id=exercise_id
    )


@dataclass
class OpenedCaseQuestion:
    attempt: Attempt
    question_id: str
    lesson_id: str | None
    instance: GeneratedInstance


@dataclass
class OpenedCase:
    exercise_id: str
    title: str
    scenario: str
    questions: list[OpenedCaseQuestion]


async def open_case(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    exercise_id: str,
    locale: str,
) -> OpenedCase:
    """A case in practice: one open attempt per question, each graded on its own as it is answered."""
    _resolve(registry, exercise_id)
    case = registry.case_config(exercise_id)
    if case is None:
        raise AppError("EXERCISE_NOT_A_CASE", f"{exercise_id!r} is not a case.", status_code=409)
    exercise_key = registry.exercise_key(exercise_id)
    # Same abandoned rule as a single exercise: reopening a case abandons its unanswered questions.
    await session.execute(
        update(Attempt)
        .where(
            Attempt.user_id == user_id,
            Attempt.course_id == registry.slug,
            Attempt.exercise_id == exercise_key,
            Attempt.state == AttemptState.OPEN,
            Attempt.exam_session_id.is_(None),
        )
        .values(state=AttemptState.ABANDONED)
    )
    quiz = get_generator(ExerciseType.QUIZ)
    opened: list[OpenedCaseQuestion] = []
    seeds = question_seeds(secrets.randbelow(_SEED_SPACE), len(case.questions))
    for question, seed in zip(case.questions, seeds, strict=True):
        instance = quiz.generate(question.as_quiz(), seed, locale)
        attempt = Attempt(
            user_id=user_id,
            course_id=registry.slug,
            exercise_id=exercise_key,
            question_id=question.id,
            seed=seed,
            instance_snapshot={
                "type": ExerciseType.QUIZ.value,
                "prompt": instance.prompt,
                "payload": instance.payload,
            },
            state=AttemptState.OPEN,
        )
        session.add(attempt)
        opened.append(
            OpenedCaseQuestion(
                attempt, question.id, registry.question_lesson_id(exercise_id, question.id), instance
            )
        )
    await session.commit()
    logger.info("case_opened exercise=%s questions=%d", exercise_key, len(opened))
    return OpenedCase(exercise_id, case.title.get(locale), case.scenario.get(locale), opened)


async def load_owned(
    session: AsyncSession, registry: CourseRegistry, user_id: uuid.UUID, attempt_id: uuid.UUID
) -> Attempt:
    """The user's attempt IN this course; another course's attempt 404s exactly like an unknown id."""
    attempt = await session.get(Attempt, attempt_id)
    if attempt is None or attempt.user_id != user_id or attempt.course_id != registry.slug:
        raise AppError("ATTEMPT_NOT_FOUND", "No such attempt.", status_code=404)
    return attempt


async def submit_answer(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    attempt_id: uuid.UUID,
    answer: Mapping[str, object],
    locale: str,
) -> tuple[Attempt, GradeResult]:
    attempt = await load_owned(session, registry, user_id, attempt_id)
    if attempt.state != AttemptState.OPEN:
        raise AppError("ATTEMPT_ALREADY_RESOLVED", "This attempt is already resolved.", status_code=409)

    exercise_type, config = _resolve_attempt(registry, attempt)
    generator = get_generator(exercise_type)
    try:
        result = generator.grade(config, attempt.seed, answer, locale)  # type: ignore[arg-type]
    except InvalidAnswerError as exc:
        raise AppError("INVALID_ANSWER", str(exc), status_code=400) from exc

    attempt.given_answer = dict(answer)
    attempt.is_correct = result.correct
    attempt.state = AttemptState.ANSWERED
    attempt.answered_at = datetime.now(UTC)
    await session.commit()
    logger.info(
        "attempt_answered attempt=%s exercise=%s question=%s correct=%s",
        attempt.id,
        attempt.exercise_id,
        attempt.question_id,
        result.correct,
    )
    return attempt, result


@dataclass
class AttemptReview:
    attempt: Attempt
    exercise_type: ExerciseType
    instance: GeneratedInstance
    result: GradeResult | None
    exercise_id: str  # display id, as everywhere the API speaks


async def review_attempt(
    session: AsyncSession,
    registry: CourseRegistry,
    user_id: uuid.UUID,
    attempt_id: uuid.UUID,
    locale: str,
) -> AttemptReview:
    attempt = await load_owned(session, registry, user_id, attempt_id)
    display_id = question_ref(registry, attempt).exercise_id
    exercise_type, config = _resolve_attempt(registry, attempt)
    generator = get_generator(exercise_type)
    # Replay the exact scenario from the seed, localized to the requested language.
    instance = generator.generate(config, attempt.seed, locale)  # type: ignore[arg-type]
    result: GradeResult | None = None
    if attempt.state == AttemptState.ANSWERED and attempt.given_answer is not None:
        result = generator.grade(config, attempt.seed, attempt.given_answer, locale)  # type: ignore[arg-type]
    return AttemptReview(
        attempt=attempt,
        exercise_type=exercise_type,
        instance=instance,
        result=result,
        exercise_id=display_id,
    )


def answer_link(registry: CourseRegistry, attempt: Attempt, locale: str) -> QuestionLink | None:
    """Where «Ver en la lección» goes once the attempt is answered; None while its answer is hidden."""
    if attempt.state != AttemptState.ANSWERED:
        return None
    return registry.question_link(question_ref(registry, attempt), locale)


def answer_excerpt(registry: CourseRegistry, attempt: Attempt) -> SolutionText | None:
    """The cited text of the norm for the solution panel; None while the attempt's answer is hidden."""
    if attempt.state != AttemptState.ANSWERED:
        return None
    return registry.question_excerpt(question_ref(registry, attempt))


async def user_attempts(
    session: AsyncSession, registry: CourseRegistry, user_id: uuid.UUID, exercise_id: str
) -> list[Attempt]:
    try:
        exercise_key = registry.exercise_key(exercise_id)
    except KeyError:
        return []  # unknown exercise = empty history, exactly as before keys existed
    config = registry.get_exercise_config(exercise_id)
    held = [v.id for v in config[1].variants] if config and isinstance(config[1], QuizConfig) else []
    # Practice history only — exam attempts live in their own lane (never shown on the exercise player).
    # A question a rebuild moved here brings its attempts; one it moved away takes them along.
    rows = await session.scalars(
        select(Attempt)
        .where(
            Attempt.user_id == user_id,
            Attempt.course_id == registry.slug,
            or_(Attempt.exercise_id == exercise_key, Attempt.variant_id.in_(held)),
            Attempt.exam_session_id.is_(None),
        )
        .order_by(Attempt.created_at.desc())
    )
    return [a for a in rows.all() if question_ref(registry, a).exercise_id == exercise_id]
