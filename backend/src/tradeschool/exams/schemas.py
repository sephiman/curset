# SPDX-License-Identifier: AGPL-3.0-only
"""Exam request/response schemas. No solution fields are populated until a session is submitted."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import Literal, Self

from pydantic import BaseModel, model_validator

from tradeschool.attempts.schemas import ExcerptOut, NoExcerptOut, missing_reason
from tradeschool.content.registry import CourseRegistry
from tradeschool.exams.draw import counted_questions, preset_targets
from tradeschool.exams.models import ExamSession
from tradeschool.exams.presets import ExamPreset
from tradeschool.exams.service import (
    ExamCaseView,
    ExamPartView,
    ExamQuestionView,
    ExamView,
    session_preset,
    target_of,
    target_title,
)


class ExamStartRequest(BaseModel):
    presetId: str | None = None
    target: str | None = None
    # The pre-preset request: `scope` names crypto-futures' two presets, `blockId` the block exam's target.
    scope: Literal["global", "block"] | None = None
    blockId: str | None = None

    @model_validator(mode="after")
    def _preset(self) -> Self:
        if self.presetId is None:
            if self.scope is None:
                raise ValueError("name the exam with presetId")
            self.presetId, self.target = self.scope, self.blockId if self.scope == "block" else None
        return self


class ExamAnswerRequest(BaseModel):
    answer: dict[str, object] | None = None
    timeSeconds: float | None = None
    clockUsedSeconds: float | None = None


class ExamPauseRequest(BaseModel):
    attemptId: uuid.UUID | None = None


class CaseMarksRequest(BaseModel):
    exerciseIds: list[str]


class ExamQuestionOut(BaseModel):
    index: int
    attemptId: uuid.UUID
    moduleId: str
    moduleTitle: str
    blockId: str
    blockTitle: str
    exerciseId: str
    type: str
    prompt: str
    payload: dict[str, object]
    answered: bool
    givenAnswer: dict[str, object] | None
    partId: str
    lessonId: str | None
    questionId: str | None
    reserve: bool
    # Reveal-only (populated on a submitted session's review):
    lessonAnchor: str | None = None
    citation: str | None = None
    timeSeconds: float | None = None
    excerpt: ExcerptOut | None = None
    noExcerpt: NoExcerptOut | None = None
    isCorrect: bool | None = None
    unanswered: bool | None = None
    correctAnswer: object | None = None
    solutionSteps: list[str] = []
    explanation: str | None = None

    @classmethod
    def build(cls, q: ExamQuestionView) -> ExamQuestionOut:
        return cls(
            index=q.index,
            attemptId=q.attempt_id,
            moduleId=q.module_id,
            moduleTitle=q.module_title,
            blockId=q.block_id,
            blockTitle=q.block_title,
            exerciseId=q.exercise_id,
            type=q.exercise_type.value,
            prompt=q.instance.prompt,
            payload=q.instance.payload,
            answered=q.answered,
            givenAnswer=q.given_answer,
            partId=q.part_id,
            lessonId=q.lesson_id,
            questionId=q.question_id,
            reserve=q.reserve,
            lessonAnchor=q.lesson_anchor,
            citation=q.citation,
            timeSeconds=q.time_seconds,
            excerpt=ExcerptOut.build(q.excerpt),
            noExcerpt=missing_reason(q.excerpt),
            isCorrect=q.is_correct,
            unanswered=q.unanswered if q.result is not None else None,
            correctAnswer=q.result.correct_answer if q.result else None,
            solutionSteps=q.result.solution_steps if q.result else [],
            explanation=q.result.explanation if q.result else None,
        )


class ExamCaseOut(BaseModel):
    exerciseId: str
    title: str
    scenario: str

    @classmethod
    def build(cls, case: ExamCaseView) -> ExamCaseOut:
        return cls(exerciseId=case.exercise_id, title=case.title, scenario=case.scenario)


class ExamPartOut(BaseModel):
    id: str
    title: str | None
    kind: str
    counted: int
    reserve: int
    choose: int | None
    penalty: str
    cases: list[ExamCaseOut]
    marked: list[str]

    @classmethod
    def build(cls, part: ExamPartView) -> ExamPartOut:
        return cls(
            id=part.id,
            title=part.title,
            kind=part.kind,
            counted=part.counted,
            reserve=part.reserve,
            choose=part.choose,
            penalty=part.penalty,
            cases=[ExamCaseOut.build(case) for case in part.cases],
            marked=part.marked,
        )


class ExamSessionOut(BaseModel):
    id: uuid.UUID
    presetId: str
    presetVersion: int
    presetTitle: str
    target: str | None
    targetTitle: str | None
    status: str
    createdAt: datetime
    finishedAt: datetime | None
    #: When the clock runs out (absent: untimed), and the server's own now, so a skewed client clock
    #: cannot shorten or stretch the sitting.
    deadline: datetime | None
    serverNow: datetime
    pause: Literal["between-questions", "never"] = "between-questions"
    paused: bool = False
    activeSeconds: float = 0.0
    parts: list[ExamPartOut]
    result: dict[str, object] | None
    byLesson: dict[str, object] | None
    questions: list[ExamQuestionOut]

    @classmethod
    def build(cls, view: ExamView) -> ExamSessionOut:
        return cls(
            id=view.id,
            presetId=view.preset_id,
            presetVersion=view.preset_version,
            presetTitle=view.preset_title,
            target=view.target,
            targetTitle=view.target_title,
            status=view.status,
            createdAt=view.created_at,
            finishedAt=view.finished_at,
            deadline=view.deadline,
            serverNow=datetime.now(UTC),
            pause=view.pause,
            paused=view.paused,
            activeSeconds=view.active_seconds,
            parts=[ExamPartOut.build(part) for part in view.parts],
            result=view.result,
            byLesson=view.by_lesson,
            questions=[ExamQuestionOut.build(q) for q in view.questions],
        )


class ExamHistoryItem(BaseModel):
    id: uuid.UUID
    presetId: str
    presetVersion: int
    presetTitle: str
    target: str | None
    targetTitle: str | None
    createdAt: datetime
    finishedAt: datetime | None
    score: float | None
    correct: int
    total: int
    # A scored preset's totals; absent on an unscored one.
    raw: float | None
    transformed: float | None
    max: float | None

    @classmethod
    def build(cls, exam: ExamSession, registry: CourseRegistry, locale: str) -> ExamHistoryItem:
        preset = session_preset(registry, exam)
        result = exam.rules.get("result")
        blob: dict[str, object] = result if isinstance(result, dict) else {}
        target = target_of(exam)

        def number(key: str) -> float | None:
            value = blob.get(key)
            return float(value) if isinstance(value, (int, float)) else None

        return cls(
            id=exam.id,
            presetId=preset.id,
            presetVersion=preset.version,
            presetTitle=preset.title.get(locale),
            target=target,
            targetTitle=target_title(registry, preset, target, locale),
            createdAt=exam.created_at,
            finishedAt=exam.finished_at,
            score=number("score"),
            correct=int(number("correct") or 0),
            total=int(number("total") or 0),
            raw=number("raw"),
            transformed=number("transformed"),
            max=number("max"),
        )


class PresetPartOut(BaseModel):
    id: str
    title: str | None
    kind: str
    questions: int
    reserve: int
    choose: int | None
    penalty: str
    max: float | None


class PresetTargetOut(BaseModel):
    id: str
    title: str
    questions: int


class PresetOut(BaseModel):
    """One entry of the Exams tab: title, parts, question count and time."""

    id: str
    version: int
    title: str
    timeLimitMinutes: int | None
    pause: Literal["between-questions", "never"] = "between-questions"
    questions: int
    parts: list[PresetPartOut]
    #: A parametric preset's choices (one sitting per block, module or lesson); absent otherwise.
    targets: list[PresetTargetOut] | None

    @classmethod
    def build(cls, preset: ExamPreset, registry: CourseRegistry, locale: str) -> PresetOut:
        def parts_for(target: str | None) -> list[PresetPartOut]:
            return [
                PresetPartOut(
                    id=part.id,
                    title=part.title.get(locale) if part.title else None,
                    kind="cases" if part.cases else "questions",
                    questions=counted_questions(registry, part, target),
                    reserve=part.reserve,
                    choose=part.choose,
                    penalty=str(part.penalty),
                    max=part.scoring.max if part.scoring else None,
                )
                for part in preset.parts
            ]

        # A parametric per-module part counts 0 here: its count is each target's, listed with the target.
        parts = parts_for(None)
        targets = None
        if preset.parametric is not None:
            targets = [
                PresetTargetOut(
                    id=target,
                    title=target_title(registry, preset, target, locale) or target,
                    questions=sum(p.questions for p in parts_for(target)),
                )
                for target in preset_targets(registry, preset)
            ]
        return cls(
            id=preset.id,
            version=preset.version,
            title=preset.title.get(locale),
            timeLimitMinutes=preset.time_limit_minutes,
            pause=preset.pause,
            questions=sum(p.questions for p in parts),
            parts=parts,
            targets=targets,
        )
