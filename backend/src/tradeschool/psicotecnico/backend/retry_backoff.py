# SPDX-License-Identifier: AGPL-3.0-only
"""`retry-backoff-bounds`: exponential backoff with full jitter, each wait drawn from [0, bound]."""

from __future__ import annotations

import random
from dataclasses import dataclass
from fractions import Fraction
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code, grouped

Kind = Literal["bound", "worst-total", "mean-total"]


@dataclass(frozen=True)
class Backoff:
    kind: Kind
    base_ms: int
    cap_ms: int
    retry: int


def bound(s: Backoff, retry: int, *, capped: bool = True, off_by_one: bool = False) -> int:
    uncapped = s.base_ms * 2 ** (retry if off_by_one else retry - 1)
    return int(min(s.cap_ms, uncapped)) if capped else uncapped


def _ms(value: int | Fraction) -> str:
    return f"{grouped(value, 0 if Fraction(value).denominator == 1 else 1)} ms"


def _total(s: Backoff, **flags: bool) -> int:
    return sum(bound(s, n, **flags) for n in range(1, s.retry + 1))


class RetryBackoffGenerator(BackendGenerator[Backoff]):
    id: ClassVar[str] = "retry-backoff-bounds"
    forms: ClassVar[tuple[str, ...]] = ("{}", "about {}", "approximately {}")
    min_separation: ClassVar[Fraction | None] = Fraction(1, 5)
    citation: ClassVar[Citation] = Citation(
        "m08-l04", "resilience4j-retry#use-a-custom-intervalfunction; formula: textbook, no stored anchor"
    )

    def scenario(self, rng: random.Random, level: int) -> Backoff | None:
        base = rng.choice((50, 100, 200, 250, 500))
        retry = rng.randint(3, 7)
        cap = base * 2 ** rng.randint(1, max(1, retry - 2))
        kind: Kind = "bound" if level == 1 else rng.choice(("worst-total", "mean-total"))
        scenario = Backoff(kind, base, cap, retry)
        return scenario if bound(scenario, retry) != bound(scenario, retry, capped=False) else None

    def stem(self, s: Backoff) -> str:
        rule = (
            f"A client retries with exponential backoff and full jitter: the wait before retry {code('n')} "
            f"(first retry {code('n = 1')}) is drawn uniformly from "
            f"{code(f'[0, min({s.cap_ms}, {s.base_ms} * 2^(n-1))]')} "
            f"ms."
        )
        if s.kind == "bound":
            return f"{rule} What is the largest wait the client can draw before retry {s.retry}?"
        if s.kind == "worst-total":
            return (
                f"{rule} What is the largest total wait the client can accumulate over its first {s.retry} "
                f"retries?"
            )
        return f"{rule} What is the expected total wait over the first {s.retry} retries?"

    def correct(self, s: Backoff) -> str:
        if s.kind == "bound":
            return _ms(bound(s, s.retry))
        if s.kind == "worst-total":
            return _ms(_total(s))
        return _ms(Fraction(_total(s), 2))

    def mistakes(self, s: Backoff) -> list[str]:
        if s.kind == "bound":
            return [
                _ms(bound(s, s.retry, capped=False)),
                _ms(bound(s, s.retry, off_by_one=True)),
                _ms(Fraction(bound(s, s.retry), 2)),
                _ms(s.cap_ms * 2),
                _ms(s.base_ms * s.retry),
            ]
        total = _total(s)
        return [
            _ms(_total(s, capped=False)),
            _ms(_total(s, off_by_one=True)),
            _ms(Fraction(total, 2)) if s.kind == "worst-total" else _ms(total),
            _ms(Fraction(_total(s, capped=False), 2)),
            _ms(s.cap_ms * s.retry),
            _ms(bound(s, s.retry)),
        ]

    def explanation(self, s: Backoff) -> str:
        bounds = [bound(s, n) for n in range(1, s.retry + 1)]
        uncapped = [s.base_ms * 2 ** (n - 1) for n in range(1, s.retry + 1)]
        listing = ", ".join(
            f"retry {n}: min({s.cap_ms}, {u}) = {b}"
            for n, (u, b) in enumerate(zip(uncapped, bounds, strict=True), 1)
        )
        if s.kind == "bound":
            return (
                f"The draw before retry {s.retry} is bounded by "
                f"min({s.cap_ms}, {s.base_ms} x 2^{s.retry - 1}) "
                f"= min({s.cap_ms}, {uncapped[-1]}) = {bounds[-1]} ms: the cap stops the doubling, "
                f"and jitter "
                f"only lowers the draw, never raises the bound."
            )
        total = sum(bounds)
        if s.kind == "worst-total":
            return (
                f"Upper bounds in ms, {listing}. The worst case draws every bound: "
                f"{' + '.join(map(str, bounds))} "
                f"= {total} ms."
            )
        return (
            f"Upper bounds in ms, {listing}. A uniform draw from 0 to a bound averages half of it, so the "
            f"expected "
            f"total is half of {' + '.join(map(str, bounds))} = {total} ms, that is "
            f"{_ms(Fraction(total, 2))}."
        )
