# SPDX-License-Identifier: AGPL-3.0-only
"""`rate-limiter-state`: which requests a token bucket or a sliding-window log rejects."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Kind = Literal["token-bucket", "sliding-window"]


@dataclass(frozen=True)
class Limiter:
    kind: Kind
    #: Bucket capacity, or requests allowed per window.
    limit: int
    #: Tokens per second, or the window length in seconds.
    rate: int
    times: tuple[int, ...]


def rejected_by_bucket(s: Limiter, *, start_full: bool = True, capped: bool = True) -> list[int]:
    tokens = s.limit if start_full else 0
    last = 0
    rejected: list[int] = []
    for number, now in enumerate(s.times, start=1):
        tokens += s.rate * (now - last)
        tokens = min(tokens, s.limit) if capped else tokens
        last = now
        if tokens >= 1:
            tokens -= 1
        else:
            rejected.append(number)
    return rejected


def rejected_by_window(s: Limiter, *, closed_edge: bool = False) -> list[int]:
    accepted: list[int] = []
    rejected: list[int] = []
    for number, now in enumerate(s.times, start=1):
        inside = [t for t in accepted if (now - t <= s.rate if closed_edge else now - t < s.rate)]
        if len(inside) < s.limit:
            accepted.append(now)
        else:
            rejected.append(number)
    return rejected


def rejected_by_fixed_window(s: Limiter) -> list[int]:
    counts: dict[int, int] = {}
    rejected: list[int] = []
    for number, now in enumerate(s.times, start=1):
        slot = now // s.rate
        if counts.get(slot, 0) < s.limit:
            counts[slot] = counts.get(slot, 0) + 1
        else:
            rejected.append(number)
    return rejected


def _text(rejected: list[int]) -> str:
    if not rejected:
        return "none"
    return ("request " if len(rejected) == 1 else "requests ") + ", ".join(f"#{n}" for n in rejected)


class RateLimiterGenerator(BackendGenerator[Limiter]):
    id: ClassVar[str] = "rate-limiter-state"
    citation: ClassVar[Citation] = Citation(
        "m08-l04",
        "rfc2697#section-3",
        confirmed="rfc2697#section-3; redis-ratelimiting-algorithms#how-it-works-3; "
        "redis-ratelimiting-algorithms#how-it-works-1",
    )

    def scenario(self, rng: random.Random, level: int) -> Limiter | None:
        kind: Kind = "token-bucket" if level == 1 else "sliding-window"
        count = rng.randint(7, 10)
        clock = 0
        times = []
        for _ in range(count):
            clock += rng.choice((0, 0, 1, 1, 2, 3))
            times.append(clock)
        rate = rng.choice((1, 2)) if kind == "token-bucket" else rng.choice((3, 4, 5))
        limit = rng.randint(2, 4)
        scenario = Limiter(kind, limit, rate, tuple(times))
        return scenario if self.correct(scenario) != "none" else None

    def stem(self, s: Limiter) -> str:
        arrivals = ", ".join(str(t) for t in s.times)
        if s.kind == "token-bucket":
            return (
                f"A token bucket holds at most {s.limit} tokens, starts full and gains {s.rate} per second, "
                f"credited whole at each request. Each accepted request costs one token. Requests arrive at "
                f"seconds "
                f"{arrivals}. Which requests are rejected?"
            )
        return (
            f"A sliding-window limiter allows {s.limit} accepted requests per {s.rate} seconds. A request "
            f"at second "
            f"{code('t')} counts the accepted ones with timestamps in {code(f'(t - {s.rate}, t]')}; rejected "
            f"requests "
            f"are not counted. Requests arrive at seconds {arrivals}. Which requests are rejected?"
        )

    def correct(self, s: Limiter) -> str:
        return _text(rejected_by_bucket(s) if s.kind == "token-bucket" else rejected_by_window(s))

    def mistakes(self, s: Limiter) -> list[str]:
        if s.kind == "token-bucket":
            return [
                _text(rejected_by_bucket(s, start_full=False)),
                _text(rejected_by_bucket(s, capped=False)),
                _text(rejected_by_bucket(s, start_full=False, capped=False)),
                _text(rejected_by_window(Limiter("sliding-window", s.limit, 1 + s.limit // s.rate, s.times))),
                _text(rejected_by_bucket(Limiter(s.kind, s.limit + 1, s.rate, s.times))),
            ]
        return [
            _text(rejected_by_window(s, closed_edge=True)),
            _text(rejected_by_fixed_window(s)),
            _text(rejected_by_window(Limiter(s.kind, s.limit, s.rate + 1, s.times))),
            _text(rejected_by_window(Limiter(s.kind, s.limit + 1, s.rate, s.times))),
            _text(rejected_by_window(Limiter(s.kind, s.limit - 1, s.rate, s.times))),
        ]

    def explanation(self, s: Limiter) -> str:
        steps: list[str] = []
        if s.kind == "token-bucket":
            tokens, last = s.limit, 0
            for number, now in enumerate(s.times, start=1):
                tokens = min(s.limit, tokens + s.rate * (now - last))
                last = now
                verdict = "accepted" if tokens >= 1 else "rejected"
                steps.append(
                    f"#{number} at {now}: {tokens} {'token' if tokens == 1 else 'tokens'}, {verdict}"
                )
                tokens -= 1 if tokens >= 1 else 0
            return "Tokens before each request, capped at the capacity: " + "; ".join(steps) + "."
        accepted: list[int] = []
        for number, now in enumerate(s.times, start=1):
            inside = [t for t in accepted if now - t < s.rate]
            verdict = "accepted" if len(inside) < s.limit else "rejected"
            if verdict == "accepted":
                accepted.append(now)
            steps.append(f"#{number} at {now}: {len(inside)} in the window, {verdict}")
        return (
            "A timestamp exactly one window old has left the window. Request by request: "
            + "; ".join(steps)
            + "."
        )
