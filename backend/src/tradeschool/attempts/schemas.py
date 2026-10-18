# SPDX-License-Identifier: AGPL-3.0-only
"""Attempt request/response schemas."""

from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel

from tradeschool.attempts.models import Attempt, AttemptState
from tradeschool.attempts.service import AttemptReview, OpenedAttempt, OpenedCase
from tradeschool.citations.course import QuestionLink
from tradeschool.exercises.base import GradeResult


class AnswerRequest(BaseModel):
    answer: dict[str, object]


class AttemptInstance(BaseModel):
    """The statement as shown to the learner — never carries the solution (§3.1)."""

    attemptId: uuid.UUID
    exerciseId: str
    type: str
    prompt: str
    payload: dict[str, object]
    state: AttemptState

    @classmethod
    def from_opened(cls, opened: OpenedAttempt) -> AttemptInstance:
        return cls(
            attemptId=opened.attempt.id,
            exerciseId=opened.exercise_id,  # display id; the row stores the permanent key
            type=opened.exercise_type.value,
            prompt=opened.instance.prompt,
            payload=opened.instance.payload,
            state=opened.attempt.state,
        )


class CaseQuestionInstance(BaseModel):
    """One question of an opened case: its own attempt, answered and graded on its own."""

    attemptId: uuid.UUID
    questionId: str
    lessonId: str | None
    prompt: str
    payload: dict[str, object]


class CaseInstance(BaseModel):
    """A case as opened in practice: the scenario first, then its questions in their fixed order."""

    exerciseId: str
    title: str
    scenario: str
    questions: list[CaseQuestionInstance]

    @classmethod
    def from_opened(cls, opened: OpenedCase) -> CaseInstance:
        return cls(
            exerciseId=opened.exercise_id,
            title=opened.title,
            scenario=opened.scenario,
            questions=[
                CaseQuestionInstance(
                    attemptId=q.attempt.id,
                    questionId=q.question_id,
                    lessonId=q.lesson_id,
                    prompt=q.instance.prompt,
                    payload=q.instance.payload,
                )
                for q in opened.questions
            ],
        )


class LessonLinkOut(BaseModel):
    """«Ver en la lección»: the lesson, at the anchor of what the question cites (None: its top)."""

    lessonId: str
    anchor: str | None
    citation: str | None

    @classmethod
    def build(cls, link: QuestionLink | None) -> LessonLinkOut | None:
        return cls(lessonId=link.lesson_id, anchor=link.anchor, citation=link.citation) if link else None


class GradeResponse(BaseModel):
    attemptId: uuid.UUID
    correct: bool
    correctAnswer: object
    solutionSteps: list[str]
    explanation: str | None
    lessonLink: LessonLinkOut | None = None

    @classmethod
    def build(cls, attempt: Attempt, result: GradeResult, link: QuestionLink | None = None) -> GradeResponse:
        return cls(
            attemptId=attempt.id,
            correct=result.correct,
            correctAnswer=result.correct_answer,
            solutionSteps=result.solution_steps,
            explanation=result.explanation,
            lessonLink=LessonLinkOut.build(link),
        )


class AttemptReviewResponse(BaseModel):
    attemptId: uuid.UUID
    exerciseId: str
    questionId: str | None
    type: str
    prompt: str
    payload: dict[str, object]
    state: AttemptState
    givenAnswer: dict[str, object] | None
    isCorrect: bool | None
    correctAnswer: object | None
    solutionSteps: list[str]
    explanation: str | None
    createdAt: datetime
    answeredAt: datetime | None
    lessonLink: LessonLinkOut | None = None

    @classmethod
    def build(cls, review: AttemptReview, link: QuestionLink | None = None) -> AttemptReviewResponse:
        a = review.attempt
        r = review.result
        return cls(
            attemptId=a.id,
            exerciseId=review.exercise_id,  # display id; the row stores the permanent key
            questionId=a.question_id,
            type=review.exercise_type.value,
            prompt=review.instance.prompt,
            payload=review.instance.payload,
            state=a.state,
            givenAnswer=a.given_answer,
            isCorrect=a.is_correct,
            correctAnswer=r.correct_answer if r else None,
            solutionSteps=r.solution_steps if r else [],
            explanation=r.explanation if r else None,
            createdAt=a.created_at,
            answeredAt=a.answered_at,
            lessonLink=LessonLinkOut.build(link),
        )


class AttemptSummary(BaseModel):
    attemptId: uuid.UUID
    exerciseId: str
    state: AttemptState
    isCorrect: bool | None
    createdAt: datetime
    answeredAt: datetime | None

    @classmethod
    def build(cls, attempt: Attempt, exercise_id: str) -> AttemptSummary:
        # `exercise_id` is the display id the listing was filtered by; the row stores the key.
        return cls(
            attemptId=attempt.id,
            exerciseId=exercise_id,
            state=attempt.state,
            isCorrect=attempt.is_correct,
            createdAt=attempt.created_at,
            answeredAt=attempt.answered_at,
        )
