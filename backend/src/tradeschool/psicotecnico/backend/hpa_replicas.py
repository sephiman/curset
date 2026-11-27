# SPDX-License-Identifier: AGPL-3.0-only
"""`hpa-desired-replicas`: the replica count a HorizontalPodAutoscaler asks for from the metric ratio."""

from __future__ import annotations

import random
from dataclasses import dataclass
from fractions import Fraction
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.source_line import source_line

RULE = "Rule: the desired replicas are the current replicas times current metric / desired metric."


@dataclass(frozen=True)
class Autoscale:
    replicas: int
    current: int
    target: int

    @property
    def ratio(self) -> Fraction:
        return Fraction(self.current, self.target)


def desired(s: Autoscale) -> int:
    return int(s.replicas * s.ratio)


class HpaReplicasGenerator(BackendGenerator[Autoscale]):
    id: ClassVar[str] = "hpa-desired-replicas"
    levels: ClassVar[tuple[int, ...]] = (1,)
    citation: ClassVar[Citation] = Citation(
        "m10-l03", "k8s-hpa#algorithm-details", confirmed="k8s-hpa#algorithm-details"
    )

    def scenario(self, rng: random.Random, level: int) -> Autoscale | None:
        replicas = rng.randint(2, 6)
        target = rng.choice((50, 100, 200))
        ratio = rng.choice((Fraction(2), Fraction(3)))
        if (replicas * ratio).denominator != 1:
            return None
        return Autoscale(replicas, int(target * ratio), target)

    def stem(self, s: Autoscale) -> str:
        return (
            f"A HorizontalPodAutoscaler targets an average of {code(f'{s.target}m')} CPU per Pod. "
            f"{s.replicas} Pods currently average {code(f'{s.current}m')}. "
            f"How many replicas does it ask for?"
        )

    def correct(self, s: Autoscale) -> str:
        return str(desired(s))

    def mistakes(self, s: Autoscale) -> list[str]:
        scaled = desired(s)
        inverted = s.replicas * Fraction(s.target, s.current)
        listed = [
            scaled - s.replicas,
            s.replicas,
            s.replicas * s.current,
            s.current // s.target,
            scaled + s.replicas,
        ]
        return [str(m) for m in listed if m > 0] + ([str(inverted)] if inverted.denominator == 1 else [])

    def explanation(self, s: Autoscale) -> str:
        return f"{self._steps(s)} {source_line(self.citation)}"

    def _steps(self, s: Autoscale) -> str:
        key = desired(s)
        return (
            f"{RULE} Inputs: {s.replicas} replicas, current {s.current}m, desired {s.target}m. "
            f"Step 1: the ratio is {s.current} / {s.target} = {float(s.ratio):g}. "
            f"Step 2: {s.replicas} x {float(s.ratio):g} = {key}. "
            f"Result: {key} replica{'' if key == 1 else 's'}."
        )
