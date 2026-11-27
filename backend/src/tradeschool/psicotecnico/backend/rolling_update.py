# SPDX-License-Identifier: AGPL-3.0-only
"""`rolling-update-bounds`: the most Pods and the fewest available Pods a rolling update allows."""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.source_line import source_line

Kind = Literal["max-total", "min-available"]

RULE = (
    "Rule: at most `replicas + maxSurge` Pods exist and at least `replicas - maxUnavailable` are available, "
    "where a percentage `maxSurge` rounds up and a percentage `maxUnavailable` rounds down."
)


@dataclass(frozen=True)
class Rollout:
    kind: Kind
    replicas: int
    surge: int
    unavailable: int
    percent: bool

    def pods(self, setting: int, *, up: bool) -> int:
        if not self.percent:
            return setting
        exact = self.replicas * setting / 100
        return math.ceil(exact) if up else math.floor(exact)


def surge_pods(s: Rollout, *, up: bool = True) -> int:
    return s.pods(s.surge, up=up)


def unavailable_pods(s: Rollout, *, up: bool = False) -> int:
    return s.pods(s.unavailable, up=up)


def _pods(count: int) -> str:
    return f"{count} Pod" + ("" if count == 1 else "s")


def _setting(value: int, percent: bool) -> str:
    return f"{value}%" if percent else str(value)


class RollingUpdateBoundsGenerator(BackendGenerator[Rollout]):
    id: ClassVar[str] = "rolling-update-bounds"
    citation: ClassVar[Citation] = Citation(
        "m10-l05",
        "k8s-deployment#max-surge",
        confirmed="k8s-deployment#max-surge; k8s-deployment#max-unavailable",
    )

    def scenario(self, rng: random.Random, level: int) -> Rollout | None:
        kind: Kind = rng.choice(("max-total", "min-available"))
        if level == 1:
            return Rollout(kind, rng.randint(12, 16), rng.randint(1, 3), rng.randint(0, 2), False)
        replicas = rng.choice((21, 22, 23, 24, 26, 27, 29))
        surge, unavailable = rng.choice((10, 25, 30, 50)), rng.choice((10, 25, 30, 50))
        scenario = Rollout(kind, replicas, surge, unavailable, True)
        fractional = (replicas * (surge if kind == "max-total" else unavailable)) % 100 != 0
        return scenario if fractional else None

    def stem(self, s: Rollout) -> str:
        surge, unavailable = (
            code(f"maxSurge: {_setting(s.surge, s.percent)}"),
            code(f"maxUnavailable: {_setting(s.unavailable, s.percent)}"),
        )
        ask = (
            "At most how many Pods of the Deployment exist at any moment during the update?"
            if s.kind == "max-total"
            else "At least how many Pods are available at all times during the update?"
        )
        deployment = f"A Deployment with {code(f'replicas: {s.replicas}')}"
        return f"{deployment} rolls out with {surge} and {unavailable}. {ask}"

    def correct(self, s: Rollout) -> str:
        if s.kind == "max-total":
            return _pods(s.replicas + surge_pods(s))
        return _pods(s.replicas - unavailable_pods(s))

    def mistakes(self, s: Rollout) -> list[str]:
        both = surge_pods(s) + unavailable_pods(s)
        if s.kind == "max-total":
            listed = [
                s.replicas + surge_pods(s, up=False),
                s.replicas + unavailable_pods(s),
                s.replicas - surge_pods(s),
                s.replicas + both,
                s.replicas + s.surge,
            ]
        else:
            listed = [
                s.replicas - unavailable_pods(s, up=True),
                s.replicas - surge_pods(s),
                s.replicas + unavailable_pods(s),
                s.replicas - both,
                s.replicas - s.unavailable,
            ]
        return [_pods(m) for m in listed if m >= 10]

    def explanation(self, s: Rollout) -> str:
        return f"{self._steps(s)} {source_line(self.citation)}"

    def _steps(self, s: Rollout) -> str:
        if s.kind == "max-total":
            extra = surge_pods(s)
            step = (
                f"Step 1: {code('maxSurge')} {_setting(s.surge, s.percent)} of {s.replicas} Pods, "
                f"rounded up, is {_pods(extra)}. "
                if s.percent
                else f"Step 1: {code('maxSurge')} is {_pods(extra)}. "
            )
            return (
                f"{RULE} Inputs: {s.replicas} replicas, surge {_setting(s.surge, s.percent)}. {step}"
                f"Step 2: {s.replicas} + {extra} = {s.replicas + extra}. Result: {_pods(s.replicas + extra)}."
            )
        down = unavailable_pods(s)
        step = (
            f"Step 1: {code('maxUnavailable')} {_setting(s.unavailable, s.percent)} of {s.replicas} "
            f"Pods, rounded down, is {_pods(down)}. "
            if s.percent
            else f"Step 1: {code('maxUnavailable')} is {_pods(down)}. "
        )
        return (
            f"{RULE} Inputs: {s.replicas} replicas, unavailable {_setting(s.unavailable, s.percent)}. {step}"
            f"Step 2: {s.replicas} - {down} = {s.replicas - down}. Result: {_pods(s.replicas - down)}."
        )
