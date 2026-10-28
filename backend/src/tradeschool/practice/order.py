# SPDX-License-Identifier: AGPL-3.0-only
"""The order a practice round serves a lesson's questions in: random, mastered ones less likely."""

from __future__ import annotations

from collections.abc import Collection, Sequence
from typing import Protocol

#: A question answered correctly this many times in practice counts as mastered.
MASTERED_AFTER = 2
#: How much likelier an unmastered question is to come up than a mastered one.
FRESH_WEIGHT, MASTERED_WEIGHT = 4.0, 1.0


class Rand(Protocol):
    def random(self) -> float: ...


def practice_order(
    question_ids: Sequence[str], mastered: Collection[str], count: int | None, rand: Rand
) -> list[str]:
    """`count` questions (all when None) without repeats, as a weighted random order: each question
    gets the key u^(1/w) and the largest keys come first (Efraimidis-Spirakis)."""
    keyed = [
        (rand.random() ** (1 / (MASTERED_WEIGHT if qid in mastered else FRESH_WEIGHT)), qid)
        for qid in question_ids
    ]
    ordered = [qid for _, qid in sorted(keyed, reverse=True)]
    return ordered if count is None else ordered[:count]
