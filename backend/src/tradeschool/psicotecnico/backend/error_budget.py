# SPDX-License-Identifier: AGPL-3.0-only
"""`error-budget-minutes`: the minutes of full outage an availability SLO allows over its window."""

from __future__ import annotations

import random
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation
from tradeschool.psicotecnico.backend.source_line import source_line

RULE = (
    "Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the "
    "whole window uses exactly the error budget, so the budget is the window times (100% - SLO)."
)
SLOS = ("98", "99", "99.5", "99.75")
MINUTES_PER_DAY = 1440


@dataclass(frozen=True)
class Slo:
    percent: str
    days: int

    @property
    def error_fraction(self) -> Fraction:
        return (100 - Fraction(Decimal(self.percent))) / 100


def budget_minutes(s: Slo) -> Fraction:
    return s.days * MINUTES_PER_DAY * s.error_fraction


def minutes(value: Fraction) -> str:
    text = format(Decimal(value.numerator) / Decimal(value.denominator), ",f")
    return text.rstrip("0").rstrip(".") if "." in text else text


class ErrorBudgetGenerator(BackendGenerator[Slo]):
    id: ClassVar[str] = "error-budget-minutes"
    forms: ClassVar[tuple[str, ...]] = ("{} minutes", "about {} minutes", "approximately {} minutes")
    min_separation: ClassVar[Fraction | None] = Fraction(1, 5)
    # the budget rule is class J: the Workbook's burn-rate paragraph states it, so the stem attributes it
    citation: ClassVar[Citation] = Citation(
        "m10-l01",
        "sre-workbook-slo-alerting#4-alert-on-burn-rate",
        confirmed="sre-workbook-slo-alerting#4-alert-on-burn-rate",
    )

    def scenario(self, rng: random.Random, level: int) -> Slo | None:
        if level == 1:
            return Slo(rng.choice(SLOS), 30)
        return Slo(rng.choice(SLOS), rng.choice((30, 60, 90)))

    def stem(self, s: Slo) -> str:
        return (
            f"According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, "
            f"held for the whole "
            f"window, uses exactly the error budget. An SLO of {s.percent}% over {s.days} days "
            f"allows how many "
            f"minutes of full outage?"
        )

    def correct(self, s: Slo) -> str:
        return minutes(budget_minutes(s))

    def mistakes(self, s: Slo) -> list[str]:
        budget = budget_minutes(s)
        listed = [
            budget * 100,
            budget / 60,
            budget * 60,
            Fraction(30 * MINUTES_PER_DAY) * s.error_fraction,
            s.days * s.error_fraction,
        ]
        return [minutes(m) for m in listed if m != budget]

    def explanation(self, s: Slo) -> str:
        return f"{self._steps(s)} {source_line(self.citation)}"

    def _steps(self, s: Slo) -> str:
        window = s.days * MINUTES_PER_DAY
        error = 100 - Fraction(Decimal(s.percent))
        budget = budget_minutes(s)
        return (
            f"{RULE} Inputs: SLO {s.percent}%, window {s.days} days. "
            f"Step 1: the window is {s.days} x {MINUTES_PER_DAY} = {window} minutes. "
            f"Step 2: the allowed error rate is 100% - {s.percent}% = {float(error):g}%. "
            f"Step 3: {window} x {float(error):g}% = {minutes(budget)} minutes. "
            f"Result: {minutes(budget)} minutes."
        )
