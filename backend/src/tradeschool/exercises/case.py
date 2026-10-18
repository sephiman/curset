# SPDX-License-Identifier: AGPL-3.0-only
"""The case exercise (supuesto práctico): one scenario, an ordered list of multiple-choice questions on it.

Each question is an ordinary single-choice quiz with one variant, so the option shuffle, grading,
reports and bias guards are the quiz's own. A case is opened with one seed; each question gets its own
seed derived from it, and each answered question is its own attempt.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import ClassVar, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

from tradeschool.content.text import LocalizedText
from tradeschool.exercises.base import (
    ExerciseGenerator,
    GeneratedInstance,
    GradeResult,
    InvalidAnswerError,
    rng_for,
)
from tradeschool.exercises.quiz import QuizConfig, QuizGenerator, QuizKind, QuizOption, QuizVariant
from tradeschool.exercises.types import ExerciseType

MIN_QUESTIONS = 10
MAX_QUESTIONS = 25
_SEED_SPACE = 2**62
# A scenario is text only: no figure directive, no image, no raw HTML image.
_FIGURE = re.compile(r"(^::figure\b|!\[|<img\b)", re.MULTILINE)


class CaseQuestion(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    #: The lesson (permanent KEY) the question belongs to: its stats and its «Ver en la lección» go there.
    lesson: str
    prompt: LocalizedText
    options: list[QuizOption]
    explanation: LocalizedText | None = None
    citation: str | None = None
    difficulty: int | None = Field(default=None, ge=1, le=3)
    tags: list[str] = Field(default_factory=list)

    def as_quiz(self) -> QuizConfig:
        """The question as the one-variant quiz that grades it."""
        variant = QuizVariant(
            id=self.id,
            kind=QuizKind.SINGLE_CHOICE,
            prompt=self.prompt,
            explanation=self.explanation,
            options=self.options,
            citation=self.citation,
            difficulty=self.difficulty,
            tags=self.tags,
        )
        return QuizConfig(type="quiz", variants=[variant])


class CaseConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: Literal["case"]
    title: LocalizedText
    #: One page of Markdown, no figures.
    scenario: LocalizedText
    questions: list[CaseQuestion]

    @model_validator(mode="after")
    def _check(self) -> Self:
        if not MIN_QUESTIONS <= len(self.questions) <= MAX_QUESTIONS:
            raise ValueError(
                f"a case has {MIN_QUESTIONS} to {MAX_QUESTIONS} questions, not {len(self.questions)}"
            )
        ids = [q.id for q in self.questions]
        if len(set(ids)) != len(ids):
            raise ValueError("duplicate case question ids")
        for locale in self.scenario.languages():
            if _FIGURE.search(self.scenario.get(locale)):
                raise ValueError("a case scenario is text only: no figures or images")
        for question in self.questions:
            question.as_quiz()  # the quiz's own single-choice rules: two options or more, one correct
        return self

    def question(self, question_id: str) -> CaseQuestion:
        for question in self.questions:
            if question.id == question_id:
                return question
        raise KeyError(question_id)


def question_seeds(seed: int, count: int) -> list[int]:
    """One seed per question, derived from the case's seed, so a case replays from one number."""
    rng = rng_for(seed)
    return [rng.randrange(_SEED_SPACE) for _ in range(count)]


class CaseGenerator(ExerciseGenerator):
    type: ClassVar[ExerciseType] = ExerciseType.CASE
    _quiz: ClassVar[QuizGenerator] = QuizGenerator()

    def parse_config(self, raw: Mapping[str, object]) -> CaseConfig:
        return CaseConfig.model_validate(dict(raw))

    def generate(self, config: BaseModel, seed: int, locale: str) -> GeneratedInstance:
        """The whole case: scenario first, then every question in its fixed order."""
        assert isinstance(config, CaseConfig)
        questions: list[dict[str, object]] = []
        for question, question_seed in zip(
            config.questions, question_seeds(seed, len(config.questions)), strict=True
        ):
            instance = self._quiz.generate(question.as_quiz(), question_seed, locale)
            questions.append({"id": question.id, "prompt": instance.prompt, "payload": instance.payload})
        return GeneratedInstance(
            prompt=config.title.get(locale),
            payload={"scenario": config.scenario.get(locale), "questions": questions},
        )

    def grade(self, config: BaseModel, seed: int, answer: Mapping[str, object], locale: str) -> GradeResult:
        """One question of the case, named by `questionId`."""
        assert isinstance(config, CaseConfig)
        question_id = answer.get("questionId")
        if not isinstance(question_id, str):
            raise InvalidAnswerError("expected a 'questionId' string")
        try:
            index = [q.id for q in config.questions].index(question_id)
        except ValueError as exc:
            raise InvalidAnswerError(f"no question {question_id!r} in this case") from exc
        question_seed = question_seeds(seed, len(config.questions))[index]
        return self._quiz.grade(config.questions[index].as_quiz(), question_seed, answer, locale)
