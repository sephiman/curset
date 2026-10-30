# SPDX-License-Identifier: AGPL-3.0-only
"""Part scores: raw = correct - penalty * wrong, then the preset's two-piece linear transform.

The transform is the CPS formula. With d the raw score, M the preset's `minimum_raw`, N the maximum raw
score (the counted questions), P the pass minimum and E the maximum:

    d < M:   t = P * d / M                        (from 0 at d = 0 up to P at d = M)
    d >= M:  t = P + (d - M) * (E - P) / (N - M)  (from P at d = M up to E at d = N)

A negative raw score transforms to 0. Raw scores are exact fractions; both are stored rounded to 4 places.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Literal

from tradeschool.exams.presets import PartScoring

#: Why a part carries no score. The real exam leaves a part ungraded for exactly these reasons.
NotGraded = Literal["no-case-marked", "several-cases-marked", "previous-part-not-passed"]


@dataclass(frozen=True)
class Tally:
    correct: int
    wrong: int
    blank: int

    @property
    def questions(self) -> int:
        return self.correct + self.wrong + self.blank


def raw_score(tally: Tally, penalty: Fraction, blank: Literal["free", "wrong"]) -> Fraction:
    penalized = tally.wrong + (tally.blank if blank == "wrong" else 0)
    return tally.correct - penalty * penalized


def transformed_score(raw: Fraction, max_raw: int, scoring: PartScoring) -> Fraction:
    minimum = scoring.minimum_raw
    # Through `str`, so a declared 25.5 is that decimal and not its nearest binary double.
    pass_minimum = Fraction(str(scoring.pass_minimum))
    top = Fraction(str(scoring.max))
    if raw <= 0:
        return Fraction(0)
    if raw < minimum:
        return pass_minimum * raw / minimum
    return pass_minimum + (raw - minimum) * (top - pass_minimum) / (max_raw - minimum)


def rounded(value: Fraction) -> float:
    return round(float(value), 4)
