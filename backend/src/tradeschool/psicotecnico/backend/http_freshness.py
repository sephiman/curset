# SPDX-License-Identifier: AGPL-3.0-only
"""`http-response-freshness`: how long until, or how long since, a cached response is stale."""

from __future__ import annotations

import random
from dataclasses import dataclass
from fractions import Fraction
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code, separated
from tradeschool.psicotecnico.backend.cited_source import source_line
from tradeschool.psicotecnico.item import OPTION_COUNT

Kind = Literal["until-stale", "since-stale"]

LIFETIMES = (60, 90, 120, 180, 240, 300, 600)


@dataclass(frozen=True)
class Cached:
    kind: Kind
    max_age: int
    #: None when the response carries no `s-maxage`; then the cache is any cache, else a shared one.
    s_maxage: int | None
    age: int


def lifetime(s: Cached, *, shared_overrides: bool = True) -> int:
    if s.s_maxage is not None and shared_overrides:
        return s.s_maxage
    return s.max_age


def _span(seconds: int) -> str:
    return f"{seconds} seconds"


def _answer(s: Cached) -> int:
    return lifetime(s) - s.age if s.kind == "until-stale" else s.age - lifetime(s)


class HttpFreshnessGenerator(BackendGenerator[Cached]):
    id: ClassVar[str] = "http-response-freshness"
    min_separation: ClassVar[Fraction | None] = Fraction(1, 5)
    citation: ClassVar[Citation] = Citation(
        "m07-l03",
        "rfc9111#section-4.2",
        confirmed="rfc9111#section-4.2; rfc9111#section-5.2.2.10",
    )

    def scenario(self, rng: random.Random, level: int) -> Cached | None:
        if level == 1:
            max_age = rng.choice(LIFETIMES)
            drawn = Cached("until-stale", max_age, None, rng.randrange(15, max_age, 15))
            return drawn if self._has_same_length_mistakes(drawn) else None
        kind: Kind = rng.choice(("until-stale", "since-stale"))
        s_maxage = rng.choice(LIFETIMES[:-1])
        max_age = rng.choice([v for v in LIFETIMES if v != s_maxage])
        age = (
            rng.randrange(15, s_maxage, 15)
            if kind == "until-stale"
            else s_maxage + rng.randrange(15, 300, 15)
        )
        drawn = Cached(kind, max_age, s_maxage, age)
        return drawn if age != max_age and self._has_same_length_mistakes(drawn) else None

    def _has_same_length_mistakes(self, s: Cached) -> bool:
        """Options of one length say nothing about the key, so keep draws that can supply three."""
        answer = self.correct(s)
        wrong = separated(answer, list(dict.fromkeys(self.mistakes(s))), Fraction(1, 5))
        return sum(len(option) == len(answer) for option in wrong) >= OPTION_COUNT - 1

    def stem(self, s: Cached) -> str:
        cache = "A shared cache" if s.s_maxage is not None else "A cache"
        directives = f"max-age={s.max_age}" + (f", s-maxage={s.s_maxage}" if s.s_maxage is not None else "")
        question = (
            "In how many seconds does the response become stale?"
            if s.kind == "until-stale"
            else "How many seconds ago did the response become stale?"
        )
        return (
            f"{cache} holds a response with {code(f'Cache-Control: {directives}')}. "
            f"The age of the response is {s.age} seconds. {question}"
        )

    def correct(self, s: Cached) -> str:
        return _span(_answer(s))

    def mistakes(self, s: Cached) -> list[str]:
        used = lifetime(s)
        unused = lifetime(s, shared_overrides=False)
        candidates = [
            unused - s.age if s.kind == "until-stale" else s.age - unused,
            used,
            s.age,
            used + s.age,
            unused,
            abs(unused - s.age),
            s.age - used if s.kind == "until-stale" else used - s.age,
        ]
        return [_span(value) for value in candidates if value > 0]

    def explanation(self, s: Cached) -> str:
        used = lifetime(s)
        shared = s.s_maxage is not None
        source = (
            f"{code(f's-maxage={used}')}, which a shared cache lets override {code(f'max-age={s.max_age}')}"
            if shared
            else code(f"max-age={used}")
        )
        if s.kind == "until-stale":
            step2 = (
                f"the response turns stale when its age reaches {used}: "
                f"{used} - {s.age} = {_answer(s)} seconds from now"
            )
        else:
            step2 = (
                f"the response turned stale when its age reached {used}: "
                f"{s.age} - {used} = {_answer(s)} seconds ago"
            )
        directives = code(f"max-age={s.max_age}") + (f", {code(f's-maxage={s.s_maxage}')}" if shared else "")
        misread = (
            f"use {code('max-age')} where {code('s-maxage')} applies, answer with the lifetime or the "
            f"age alone, or add where they should subtract"
            if shared
            else "answer with the lifetime or the age alone, or add where they should subtract"
        )
        return (
            f"Inputs: {directives}, age {s.age} seconds. "
            f"Rule: a response is fresh while its freshness lifetime is greater than its age, and a shared "
            f"cache takes the lifetime from {code('s-maxage')} when present, ahead of {code('max-age')}. "
            f"Step 1: the freshness lifetime is {used} seconds, from {source}. "
            f"Step 2: {step2}. "
            f"Result: {_span(_answer(s))}. The other options {misread}. {source_line(self.citation)}"
        )
