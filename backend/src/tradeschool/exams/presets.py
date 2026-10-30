# SPDX-License-Identifier: AGPL-3.0-only
"""Exam presets: the rules of a course's exams, declared in its `course.yaml` under `exams:`.

Nothing about an exam is a literal in the engine: how many questions, drawn from where, the time, the
penalty, the blank rule, the score range, the pass minimum and whether a part waits on the one before.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Literal, Self

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from tradeschool.content.text import LocalizedText

#: The penalties an official exam uses; anything else is an authoring mistake, not a policy.
PENALTIES = (Fraction(0), Fraction(1, 4), Fraction(1, 3))

#: `random`: `questions` distinct questions from the pool. `per-module`: one question from each module
#: with a bank, in course order (the count follows the course). `all`: every question of the pool.
DrawMode = Literal["random", "per-module", "all"]


class PresetSource(BaseModel):
    """Where a part draws from: exactly one field set.

    `each` makes the preset parametric: the exam list offers one sitting per block, module or lesson,
    and the learner picks which when starting it.
    """

    model_config = ConfigDict(extra="forbid")
    course: bool = False
    cases: bool = False
    block: str | None = None
    module: str | None = None
    #: A set of modules drawn as one pool (AGE bloques I to V).
    modules: list[str] | None = None
    lesson: str | None = None
    each: Literal["block", "module", "lesson"] | None = None

    @model_validator(mode="before")
    @classmethod
    def _from_word(cls, raw: object) -> object:
        # `source: course` and `source: cases` read as words; scoped sources are mappings.
        if raw in ("course", "cases"):
            return {raw: True}
        return raw

    @model_validator(mode="after")
    def _exactly_one(self) -> Self:
        chosen = [
            name
            for name in ("course", "cases", "block", "module", "modules", "lesson", "each")
            if getattr(self, name)
        ]
        if len(chosen) != 1:
            names = "course, cases, block, module, modules, lesson, each"
            raise ValueError(f"a part's source names one of {names}; got {chosen}")
        return self


class PartScoring(BaseModel):
    """The transformed score: a two-piece linear map pinned at (minimum_raw → pass_minimum, max raw → max)."""

    model_config = ConfigDict(extra="forbid")
    max: float = Field(gt=0)
    pass_minimum: float = Field(ge=0)
    #: The raw score that earns exactly `pass_minimum` (the CPS «nota de corte»).
    minimum_raw: float = Field(gt=0)

    @model_validator(mode="after")
    def _ordered(self) -> Self:
        if self.pass_minimum > self.max:
            raise ValueError("pass_minimum exceeds max")
        return self


def _count_problem(draw: DrawMode, questions: int | None, reserve: int) -> str | None:
    """Why a draw mode and a count do not go together, if they do not."""
    if draw == "per-module" and questions is not None:
        return "a per-module draw takes its count from the course"
    if draw == "all" and questions is not None:
        return "an `all` draw takes every question of its pool"
    if draw == "random" and questions is None:
        return "a random draw needs `questions`"
    if draw != "random" and reserve:
        return f"a {draw} draw has no reserve questions"
    return None


class PartSource(BaseModel):
    """One source of a composite part: where it draws from, how, and how many (A8)."""

    model_config = ConfigDict(extra="forbid")
    source: PresetSource
    draw: DrawMode = "random"
    questions: int | None = Field(default=None, ge=1)


class PresetPart(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    title: LocalizedText | None = None
    #: One source, drawn with `draw` and `questions` — or `sources`, never both.
    source: PresetSource | None = None
    draw: DrawMode = "random"
    #: Counted questions (per case, for a case part); absent for a per-module or `all` draw.
    questions: int | None = Field(default=None, ge=1)
    #: Several sources, each with its own draw and count, shuffled together into one part.
    sources: list[PartSource] | None = Field(default=None, min_length=2)
    #: Case parts only: how many cases are offered; the learner marks one and only that one is graded.
    choose: int | None = Field(default=None, ge=2)
    #: Extra questions shown at the end of the part, counted only if one before them is voided.
    reserve: int = Field(default=0, ge=0)
    #: What a wrong answer costs, as a fraction of a correct one.
    penalty: Fraction = Fraction(0)
    #: `free`: a blank costs nothing. `wrong`: a blank is penalized like a wrong answer.
    blank: Literal["free", "wrong"] = "free"
    scoring: PartScoring | None = None
    #: Graded only if the part before it reached its `pass_minimum`.
    requires_previous_pass: bool = False

    @field_validator("penalty", mode="before")
    @classmethod
    def _fraction(cls, raw: object) -> Fraction:
        try:
            value = Fraction(str(raw).strip())
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(f"penalty {raw!r} is not a fraction") from exc
        if value not in PENALTIES:
            raise ValueError(f"penalty {raw!r} must be one of 0, 1/4, 1/3")
        return value

    @model_validator(mode="after")
    def _consistent(self) -> Self:
        if self.sources is not None:
            return self._composite()
        if self.source is None:
            raise ValueError(f"part {self.id!r} declares `source` or `sources`")
        if self.source.cases:
            if self.choose is None or self.questions is None:
                raise ValueError(f"part {self.id!r}: a case part needs `choose` and `questions`")
            if self.draw != "random":
                raise ValueError(f"part {self.id!r}: a case part draws cases, not one question per module")
        elif self.choose is not None:
            raise ValueError(f"part {self.id!r}: `choose` belongs to a case part")
        if problem := _count_problem(self.draw, self.questions, self.reserve):
            raise ValueError(f"part {self.id!r}: {problem}")
        return self

    def _composite(self) -> Self:
        assert self.sources is not None
        # Read off the values, not the fields set: a stored snapshot dumps every field with its default.
        own = [
            name
            for name, unset in (("source", None), ("draw", "random"), ("questions", None), ("choose", None))
            if getattr(self, name) != unset
        ]
        if own:
            raise ValueError(f"part {self.id!r} declares `source` or `sources`, not both ({sorted(own)})")
        for number, entry in enumerate(self.sources, start=1):
            if entry.source.cases or entry.source.each:
                raise ValueError(
                    f"part {self.id!r} source {number}: a composite part draws questions from fixed sources"
                )
            reserve = self.reserve if entry.draw == "per-module" else 0
            if problem := _count_problem(entry.draw, entry.questions, reserve):
                raise ValueError(f"part {self.id!r} source {number}: {problem}")
        return self

    @property
    def cases(self) -> bool:
        return self.source is not None and self.source.cases

    @property
    def each(self) -> Literal["block", "module", "lesson"] | None:
        return self.source.each if self.source is not None else None

    @property
    def draws(self) -> list[PartSource]:
        """The part's sources: its `sources`, or its one `source` with the part's own draw and count."""
        if self.sources is not None:
            return self.sources
        assert self.source is not None
        return [PartSource(source=self.source, draw=self.draw, questions=self.questions)]


class ExamPreset(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    #: Bumped whenever the rules change; a past exam keeps the version it was taken with.
    version: int = Field(ge=1)
    title: LocalizedText
    #: For the whole exam, parts running together; absent means untimed.
    time_limit_minutes: int | None = Field(default=None, ge=1)
    #: `between-questions`: pause enabled between questions; `never`: no pause control and time keeps running.
    pause: Literal["between-questions", "never"] | None = None
    parts: list[PresetPart] = Field(min_length=1)

    @model_validator(mode="after")
    def _parts(self) -> Self:
        if self.pause is None:
            title_text = (
                " ".join(self.title.values()).lower()
                if isinstance(self.title, dict)
                else str(self.title).lower()
            )
            if "simulacro" in self.id.lower() or "simulacro" in title_text:
                self.pause = "never"
            else:
                self.pause = "between-questions"
        ids = [part.id for part in self.parts]
        if len(set(ids)) != len(ids):
            raise ValueError(f"preset {self.id!r}: duplicate part id")
        if any(part.each for part in self.parts) and len(self.parts) > 1:
            raise ValueError(f"preset {self.id!r}: a parametric (`each`) preset has one part")
        if self.parts[0].requires_previous_pass:
            raise ValueError(f"preset {self.id!r}: the first part has no previous part to pass")
        for before, part in zip(self.parts, self.parts[1:], strict=False):
            if part.requires_previous_pass and before.scoring is None:
                raise ValueError(
                    f"preset {self.id!r}: part {part.id!r} waits on {before.id!r}, which has no pass minimum"
                )
        return self

    @property
    def parametric(self) -> Literal["block", "module", "lesson"] | None:
        return self.parts[0].each
