# SPDX-License-Identifier: AGPL-3.0-only
"""The psicotécnico exercise: any seed is a fresh four-option item from a generator, keyed by its solver."""

from __future__ import annotations

import random
from collections.abc import Mapping
from typing import ClassVar, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

from tradeschool.exercises.base import ExerciseGenerator, GeneratedInstance, GradeResult, InvalidAnswerError
from tradeschool.exercises.types import ExerciseType
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.registry import load_generator

DEFAULT_LEVELS = {1: 1, 2: 1, 3: 1}
_LEVEL_SALT = 0x5EED


class PsicotecnicoConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: Literal["psicotecnico"]
    generator: str
    #: Level -> weight: how often each difficulty is drawn.
    difficulty: dict[int, int] = Field(default_factory=lambda: dict(DEFAULT_LEVELS))

    @model_validator(mode="after")
    def _levels(self) -> Self:
        generator = load_generator(self.generator)
        if not self.difficulty or any(w < 1 for w in self.difficulty.values()):
            raise ValueError(f"{self.generator}: every difficulty weight is 1 or more")
        unknown = sorted(set(self.difficulty) - set(generator.levels))
        if unknown:
            raise ValueError(f"{self.generator} has no difficulty level {unknown}")
        return self

    def level_for(self, seed: int) -> int:
        rng = random.Random(seed ^ _LEVEL_SALT)
        levels = sorted(self.difficulty)
        return rng.choices(levels, weights=[self.difficulty[level] for level in levels])[0]


def build_item(config: PsicotecnicoConfig, seed: int) -> Item:
    return load_generator(config.generator).generate(seed, Params(config.level_for(seed)))


def option_id(index: int) -> str:
    return f"o{index}"


class PsicotecnicoGenerator(ExerciseGenerator):
    type: ClassVar[ExerciseType] = ExerciseType.PSICOTECNICO

    def parse_config(self, raw: Mapping[str, object]) -> PsicotecnicoConfig:
        return PsicotecnicoConfig.model_validate(dict(raw))

    def generate(self, config: BaseModel, seed: int, locale: str) -> GeneratedInstance:
        assert isinstance(config, PsicotecnicoConfig)
        item = build_item(config, seed)
        payload: dict[str, object] = {
            "kind": "single_choice",
            "generator": item.generator,
            "options": [{"id": option_id(i), "text": text} for i, text in enumerate(item.options)],
        }
        if item.table is not None:
            payload["table"] = {
                "title": item.table.title,
                "header": list(item.table.header),
                "rows": [list(row) for row in item.table.rows],
            }
        return GeneratedInstance(prompt=item.stem, payload=payload)

    def grade(self, config: BaseModel, seed: int, answer: Mapping[str, object], locale: str) -> GradeResult:
        assert isinstance(config, PsicotecnicoConfig)
        selected = answer.get("optionId")
        if not isinstance(selected, str):
            raise InvalidAnswerError("expected an 'optionId' string")
        item = build_item(config, seed)
        key = load_generator(config.generator).solve(item)
        return GradeResult(
            correct=selected == option_id(key),
            correct_answer={"optionId": option_id(key), "text": item.options[key]},
            explanation=item.explanation,
        )
