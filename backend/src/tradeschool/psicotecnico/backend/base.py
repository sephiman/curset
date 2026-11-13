# SPDX-License-Identifier: AGPL-3.0-only
"""The shape every backend-in-depth generator shares: a scenario, a computed key and computed mistakes."""

from __future__ import annotations

import random
import re
from abc import abstractmethod
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import ClassVar, cast

from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal
from tradeschool.psicotecnico.item import OPTION_COUNT, Item, Params
from tradeschool.psicotecnico.spanish import round_half_up

BUILD_ATTEMPTS = 500


@dataclass(frozen=True)
class Citation:
    """The F fact a generator's rule comes from; `confirmed` stays empty until the module session fills it."""

    lesson: str
    #: A `source_id#anchor` the rule was implemented from, or a note when no stored anchor states it.
    suggested: str
    confirmed: str | None = None

    @property
    def unfilled(self) -> bool:
        return self.confirmed is None


_NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?")


def _number(option: str) -> Fraction:
    return Fraction(_NUMBER.findall(option)[0].replace(",", ""))


def separated(answer: str, distractors: list[str], margin: Fraction) -> list[str]:
    """The distractors that sit at least `margin` (relative) away from the answer and from each other."""
    kept: list[str] = []
    for option in distractors:
        value = _number(option)
        if all(abs(value - _number(o)) >= margin * max(value, _number(o)) for o in (answer, *kept)):
            kept.append(option)
    return kept


def code(text: object) -> str:
    return f"`{text}`"


def grouped(value: Fraction | int, decimals: int = 0) -> str:
    rounded = round_half_up(Fraction(value), decimals)
    return format(Decimal(rounded.numerator) / Decimal(rounded.denominator), f",.{decimals}f")


class CitedGenerator(ItemGenerator):
    """What the exporter needs of any backend generator, whatever its scenario type."""

    levels: ClassVar[tuple[int, ...]] = (1, 2)
    citation: ClassVar[Citation]
    #: Equivalent wordings of an option, one drawn per option so that length says nothing about the key.
    forms: ClassVar[tuple[str, ...]] = ("{}",)
    #: Hedged forms ("about 1,500") make close numbers both defensible: distractors keep this relative gap.
    min_separation: ClassVar[Fraction | None] = None

    def correct_options(self, text: str) -> set[str]:
        return {form.format(text) for form in self.forms}


class BackendGenerator[S](CitedGenerator):
    """One scenario type `S`; the key and every distractor are computed from it, never written by hand."""

    @abstractmethod
    def scenario(self, rng: random.Random, level: int) -> S | None:
        """A fresh scenario, or None when this draw is not usable (the build draws again)."""

    @abstractmethod
    def stem(self, scenario: S) -> str: ...

    @abstractmethod
    def correct(self, scenario: S) -> str: ...

    @abstractmethod
    def mistakes(self, scenario: S) -> list[str]:
        """The answers a typical misreading of the rule produces."""

    @abstractmethod
    def explanation(self, scenario: S) -> str: ...

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        for _ in range(BUILD_ATTEMPTS):
            drawn = self.scenario(rng, params.difficulty)
            if drawn is None:
                continue
            answer = self.correct(drawn)
            wrong = [m for m in dict.fromkeys(self.mistakes(drawn)) if m != answer]
            if self.min_separation is not None:
                wrong = separated(answer, wrong, self.min_separation)
            if len(wrong) < OPTION_COUNT - 1:
                continue
            options, slot = deal(rng, answer, wrong)
            options = tuple(rng.choice(self.forms).format(option) for option in options)
            return Item(
                generator=self.id,
                seed=seed,
                difficulty=params.difficulty,
                stem=self.stem(drawn),
                options=options,
                key=slot,
                explanation=self.explanation(drawn),
                facts={"scenario": drawn},
            )
        raise RuntimeError(f"no usable {self.id} scenario for seed {seed}")

    def solve(self, item: Item) -> int:
        expected = self.correct_options(self.correct(cast(S, item.facts["scenario"])))
        hits = [i for i, option in enumerate(item.options) if option in expected]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options read as the key")
        return hits[0]

    def check_extra(self, item: Item) -> list[str]:
        problems = []
        if "TODO" in item.explanation or "TODO" in item.stem:
            problems.append("a citation placeholder reached the learner's text")
        if any(f"option {letter}" in item.explanation.lower() for letter in "abcd"):
            problems.append("the explanation refers to an option by letter")
        return problems
