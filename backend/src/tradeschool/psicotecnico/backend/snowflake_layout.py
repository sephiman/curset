# SPDX-License-Identifier: AGPL-3.0-only
"""`snowflake-layout`: ids per millisecond across machines under the 41/10/12-bit layout."""

from __future__ import annotations

import random
from dataclasses import dataclass, replace
from fractions import Fraction
from typing import ClassVar, cast

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code, grouped
from tradeschool.psicotecnico.backend.option_forms import plain_option
from tradeschool.psicotecnico.item import Item, Params

ANCHOR = "snowflake-readme#top"
SEQUENCE_BITS = 12
MACHINE_BITS = 10
PER_MS = 2**SEQUENCE_BITS
MACHINES = 2**MACHINE_BITS
RELEASE = "Twitter's 2010 Snowflake"


@dataclass(frozen=True)
class Fleet:
    machines: int


class SnowflakeLayoutGenerator(BackendGenerator[Fleet]):
    id: ClassVar[str] = "snowflake-layout"
    forms: ClassVar[tuple[str, ...]] = (
        "{}",
        "{} ids",
        "{} ids in total",
        "{} distinct ids",
        "{} distinct ids per millisecond",
        "{} ids in one millisecond",
    )
    citation: ClassVar[Citation] = Citation("m09-l04", ANCHOR, confirmed=ANCHOR)
    levels: ClassVar[tuple[int, ...]] = (1,)
    min_separation: ClassVar[Fraction | None] = Fraction(1, 10)

    def scenario(self, rng: random.Random, level: int) -> Fleet:
        return Fleet(rng.choice((3, 5, 6, 7)))

    def stem(self, s: Fleet) -> str:
        return (
            f"{s.machines} machines run {RELEASE}, each with its own configured machine id, "
            "and each generates as many ids as every millisecond allows. "
            "At most how many distinct ids do they produce in one millisecond?"
        )

    def correct(self, s: Fleet) -> str:
        return grouped(s.machines * PER_MS)

    def mistakes(self, s: Fleet) -> list[str]:
        return [text for _, text in self._candidates(s)]

    def build(self, seed: int, params: Params) -> Item:
        item = super().build(seed, params)
        fleet = cast(Fleet, item.facts["scenario"])
        return replace(
            item, explanation=self._explain(fleet, tuple(plain_option(o, self.forms) for o in item.options))
        )

    def explanation(self, s: Fleet) -> str:
        return self._explain(s, tuple(self.mistakes(s)))

    def _candidates(self, s: Fleet) -> list[tuple[str, str]]:
        n = s.machines
        named = [
            ("counts one machine only", grouped(PER_MS)),
            (
                f"multiplies by the 10-bit machine field ({grouped(MACHINES)} values) "
                "instead of the sequence number",
                grouped(n * MACHINES),
            ),
            (f"multiplies by the 12 bits instead of the {code('2^12')} values", grouped(n * SEQUENCE_BITS)),
            ("adds the machines instead of multiplying", grouped(n + PER_MS)),
        ]
        named.append(("counts a whole second of 1,000 milliseconds", grouped(n * PER_MS * 1000)))
        return named

    def _explain(self, s: Fleet, shown: tuple[str, ...]) -> str:
        layout = "The layout is a 41-bit time, a 10-bit machine id and a 12-bit sequence number."
        per_ms = f"Each machine produces at most {code('2^12')} = {grouped(PER_MS)} ids in a millisecond"
        product = code(f"{s.machines} × {grouped(PER_MS)}")
        steps = f"{per_ms}, and the machine id keeps the machines apart: {product}."
        reasons: dict[str, list[str]] = {}
        for reason, text in self._candidates(s):
            if text in shown and text != self.correct(s):
                reasons.setdefault(text, []).append(reason)
        wrong = " ".join(f"{text} {' and '.join(found)}." for text, found in reasons.items())
        result = f"The result is {self.correct(s)}."
        return f"{layout} {steps} {result} Wrong options: {wrong} Source: `{ANCHOR}`."
