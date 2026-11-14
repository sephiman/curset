# SPDX-License-Identifier: AGPL-3.0-only
"""`circuit-breaker-state`: a Resilience4j-style breaker after a call sequence, thresholds per its docs."""

from __future__ import annotations

import random
from collections import deque
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

OPEN, CLOSED, HALF_OPEN = "OPEN", "CLOSED", "HALF_OPEN"


@dataclass(frozen=True)
class Breaker:
    window: int
    minimum: int
    threshold: int
    #: True for a failed call, in order.
    calls: tuple[bool, ...]
    #: When set, the breaker waits out its open state and these calls probe it half open.
    probes: tuple[bool, ...] = ()


@dataclass(frozen=True)
class Reading:
    tripped_at: int | None
    rejected: int


def _trips(failures: int, recorded: int, threshold: int, strict: bool) -> bool:
    rate = failures * 100
    return rate > threshold * recorded if strict else rate >= threshold * recorded


def run_closed(
    s: Breaker, *, strict: bool = False, minimum: int | None = None, windowed: bool = True
) -> Reading:
    floor = s.minimum if minimum is None else minimum
    window: deque[bool] = deque(maxlen=s.window if windowed else None)
    for number, failed in enumerate(s.calls, start=1):
        window.append(failed)
        if len(window) >= floor and _trips(sum(window), len(window), s.threshold, strict):
            return Reading(number, len(s.calls) - number)
    return Reading(None, 0)


def probe_state(s: Breaker, *, strict: bool = False) -> str:
    return OPEN if _trips(sum(s.probes), len(s.probes), s.threshold, strict) else CLOSED


def _answer(state: str, rejected: int) -> str:
    return f"{state}; {rejected} {'call' if rejected == 1 else 'calls'} rejected"


def _noun(count: int) -> str:
    return "failure" if count == 1 else "failures"


def _outcomes(calls: tuple[bool, ...]) -> str:
    return " ".join("F" if failed else "S" for failed in calls)


class CircuitBreakerGenerator(BackendGenerator[Breaker]):
    id: ClassVar[str] = "circuit-breaker-state"
    forms: ClassVar[tuple[str, ...]] = ("{}", "{} in total", "{} over the whole sequence")
    citation: ClassVar[Citation] = Citation(
        "m08-l04",
        "resilience4j-circuitbreaker#failure-rate-and-slow-call-rate-thresholds",
        confirmed="resilience4j-circuitbreaker#failure-rate-and-slow-call-rate-thresholds",
    )

    def scenario(self, rng: random.Random, level: int) -> Breaker | None:
        window = rng.choice((4, 5, 6, 8))
        minimum = rng.randint(max(2, window - 2), window)
        threshold = rng.choice((40, 50, 60))
        rate = rng.choice((0.3, 0.45, 0.6))
        calls = tuple(rng.random() < rate for _ in range(rng.randint(window + 2, window + 6)))
        scenario = Breaker(window, minimum, threshold, calls)
        if level == 1:
            return scenario
        if run_closed(scenario).tripped_at is None:
            return None
        return Breaker(
            window, minimum, threshold, calls, tuple(rng.random() < 0.5 for _ in range(rng.choice((2, 3, 4))))
        )

    def stem(self, s: Breaker) -> str:
        config = (
            f"A circuit breaker uses a count-based window of the last {code(s.window)} calls, "
            f"{code(f'minimumNumberOfCalls = {s.minimum}')} and "
            f"{code(f'failureRateThreshold = {s.threshold}')}. "
            f"It starts CLOSED, rejects calls made while OPEN, and calls arrive with outcomes "
            f"(S success, F failure) {_outcomes(s.calls)}."
        )
        if not s.probes:
            return f"{config} What is the state after the last call, and how many calls were rejected?"
        return (
            f"{config} Once it opens, {code('waitDurationInOpenState')} elapses after the last call and it "
            f"becomes HALF_OPEN with {code(f'permittedNumberOfCallsInHalfOpenState = {len(s.probes)}')}. "
            f"Those "
            f"calls "
            f"have outcomes {_outcomes(s.probes)}. What is the state once they complete, and how many of the "
            f"first "
            f"calls were rejected?"
        )

    def correct(self, s: Breaker) -> str:
        rejected = run_closed(s).rejected
        if s.probes:
            return _answer(probe_state(s), rejected)
        return _answer(OPEN if run_closed(s).tripped_at else CLOSED, rejected)

    def mistakes(self, s: Breaker) -> list[str]:
        readings = [
            run_closed(s, strict=True),
            run_closed(s, minimum=1),
            run_closed(s, windowed=False),
            run_closed(s, strict=True, windowed=False),
        ]
        if s.probes:
            states = [
                probe_state(s, strict=True),
                HALF_OPEN,
                CLOSED if s.probes[0] is False else OPEN,
                OPEN if any(s.probes) else CLOSED,
            ]
            rejected = run_closed(s).rejected
            return [_answer(state, rejected) for state in states] + [
                _answer(probe_state(s), n) for n in (rejected + 1, rejected - 1)
            ]
        answers = [_answer(OPEN if x.tripped_at else CLOSED, x.rejected) for x in readings]
        real = run_closed(s)
        answers += [_answer(OPEN, real.rejected + 1), _answer(HALF_OPEN, real.rejected)]
        if real.tripped_at is not None:
            answers.append(_answer(OPEN, real.rejected - 1) if real.rejected else _answer(CLOSED, 0))
        return answers

    def explanation(self, s: Breaker) -> str:
        reading = run_closed(s)
        if reading.tripped_at is None:
            return (
                f"Window of the last {s.window} calls, rate = failures / calls recorded, evaluated only once "
                f"{s.minimum} calls are recorded. After the last call the failure rate never reaches "
                f"{s.threshold}%, so the breaker stays CLOSED and rejects nothing."
            )
        window = s.calls[max(0, reading.tripped_at - s.window) : reading.tripped_at]
        failed = sum(window)
        opened = (
            f"After call {reading.tripped_at} the window holds {_outcomes(window)}: "
            f"{failed} {_noun(failed)} out of "
            f"{len(window)} is {failed * 100 / len(window):.0f}%, which is at least {s.threshold}% with at "
            f"least "
            f"{s.minimum} calls recorded, so the breaker opens (the threshold is reached with `>=`, "
            f"not exceeded). "
            f"The {reading.rejected} later calls are rejected."
        )
        if not s.probes:
            return opened
        probe_failed = sum(s.probes)
        verdict = OPEN if probe_state(s) == OPEN else CLOSED
        return (
            f"{opened} In HALF_OPEN the {len(s.probes)} permitted calls are evaluated together: "
            f"{probe_failed} "
            f"{_noun(probe_failed)} out of {len(s.probes)} is {probe_failed * 100 / len(s.probes):.0f}%, "
            f"{'at least' if verdict == OPEN else 'below'} {s.threshold}%, so the breaker goes back "
            f"to {verdict}."
        )
