# SPDX-License-Identifier: AGPL-3.0-only
"""The generator contract: `generate`, `solve` and the property tests every build runs."""

from __future__ import annotations

import random
from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence
from dataclasses import replace
from fractions import Fraction
from typing import ClassVar

from tradeschool.psicotecnico.item import OPTION_COUNT, Item, Params

LEVELS = (1, 2, 3)
#: Seeds per level the load-time check runs; the test suite runs far more.
LOAD_CHECK_SEEDS = 40
RANK_ATTEMPTS = 200
_RANK_SALT = 0x4C454E


class UnsolvableItem(Exception):
    """The options do not hold exactly one answer under the item's own rule."""


class GeneratorLoadError(RuntimeError):
    """A generator failed its property tests, so it does not load."""


class ItemGenerator(ABC):
    id: ClassVar[str]
    #: The difficulty levels this generator builds; each has its own knobs inside the generator.
    levels: ClassVar[tuple[int, ...]] = LEVELS

    @abstractmethod
    def build(self, seed: int, params: Params) -> Item:
        """One item from one seed, before the answer's length rank is balanced."""

    def generate(self, seed: int, params: Params) -> Item:
        """`build`, redrawn until the key sits where the seed puts it when options are ordered by length."""
        draw = random.Random(seed ^ _RANK_SALT)
        target = draw.randrange(OPTION_COUNT)
        tiebreak = [draw.random() for _ in range(OPTION_COUNT)]
        proposals = [self.build(seed, params)]
        for attempt in range(1, RANK_ATTEMPTS):
            if _is_balanced(proposals[-1], target, tiebreak):
                break
            proposals.append(self.build(seed * 1_000_003 + attempt, params))
        item = next(
            (p for p in proposals if _is_balanced(p, target, tiebreak)),
            next((p for p in proposals if _is_balanced(p, target, tiebreak)), proposals[0]),
        )
        return replace(item, seed=seed)

    @abstractmethod
    def solve(self, item: Item) -> int:
        """The index of the one correct option, recomputed from the item; `UnsolvableItem` otherwise."""

    def check_extra(self, item: Item) -> list[str]:
        """Rules specific to this type (series, ordering, plausibility); empty when the item holds."""
        return []

    def check(self, item: Item) -> list[str]:
        return check_item(self, item)


def _is_balanced(item: Item, target: int, tiebreak: Sequence[float]) -> bool:
    """The key sits at position `target` when the options are ordered by length, ties broken at random."""
    lengths = [len(option) for option in item.options]
    if len(set(lengths)) == 1:
        return True
    order = sorted(range(len(lengths)), key=lambda i: (lengths[i], tiebreak[i]))
    return order.index(item.key) == target


def check_item(generator: ItemGenerator, item: Item) -> list[str]:
    problems: list[str] = []
    if len(item.options) != OPTION_COUNT:
        problems.append(f"{len(item.options)} options, not {OPTION_COUNT}")
    if len(set(item.options)) != len(item.options):
        problems.append("two options are the same text")
    if not 0 <= item.key < len(item.options):
        return [*problems, f"key {item.key} is outside the options"]
    if any(not option.strip() for option in item.options):
        problems.append("an option is empty")
    try:
        solved = generator.solve(item)
    except UnsolvableItem as exc:
        problems.append(f"unsolvable: {exc}")
    else:
        if solved != item.key:
            problems.append(f"solver says option {solved}, the item keys option {item.key}")
    if not item.explanation.strip():
        problems.append("no explanation")
    return problems + generator.check_extra(item)


def seeds_for(level: int, count: int, base: int = 0) -> Sequence[int]:
    rng = random.Random(1_000_003 * level + base)
    return [rng.randrange(2**62) for _ in range(count)]


def verify(generator: ItemGenerator, per_level: int = LOAD_CHECK_SEEDS, base: int = 0) -> list[str]:
    """Property-test one generator over seeded items at every level; the first failures, labelled."""
    failures: list[str] = []
    for level in generator.levels:
        for seed in seeds_for(level, per_level, base):
            params = Params(level)
            try:
                item = generator.generate(seed, params)
                repeat = generator.generate(seed, params)
            except Exception as exc:
                failures.append(f"{generator.id} level {level} seed {seed}: generate raised {exc!r}")
                continue
            problems = generator.check(item)
            if item != repeat:
                problems.append("the same seed built two different items")
            failures += [f"{generator.id} level {level} seed {seed}: {p}" for p in problems]
    return failures[:20]


def deal(rng: random.Random, answer: str, distractors: Sequence[str]) -> tuple[tuple[str, ...], int]:
    """The answer and three distractors, seeded; from a larger pool, the answer's length rank is uniform."""
    pool = [d for d in dict.fromkeys(distractors) if d != answer]
    if len(pool) < OPTION_COUNT - 1:
        raise ValueError(f"{len(pool)} distractors for an answer, three needed")
    same_length = [d for d in pool if len(d) == len(answer)]
    if len(same_length) >= OPTION_COUNT - 1:
        pool = same_length  # options of one length say nothing about which is the answer
    chosen = pool if len(pool) == OPTION_COUNT - 1 else _balanced_pick(rng, answer, pool)
    options = [answer, *chosen]
    rng.shuffle(options)
    return tuple(options), options.index(answer)


def deal_choosing(
    rng: random.Random, answers: Sequence[str], distractors: Sequence[str]
) -> tuple[tuple[str, ...], int, str]:
    """`deal` when any of several answers would do: the one that lets the length rank come out as drawn."""
    need = OPTION_COUNT - 1
    rank = rng.randrange(need + 1)
    order = list(answers)
    rng.shuffle(order)
    for answer in order:
        pool = [d for d in dict.fromkeys(distractors) if d != answer]
        shorter = sum(1 for d in pool if len(d) < len(answer))
        if len(pool) >= need and rank <= shorter and need - rank <= len(pool) - shorter:
            options, slot = deal(rng, answer, pool)
            return options, slot, answer
    options, slot = deal(rng, order[0], distractors)
    return options, slot, order[0]


def _balanced_pick(rng: random.Random, answer: str, pool: list[str]) -> list[str]:
    shorter = [d for d in pool if len(d) < len(answer)]
    rest = [d for d in pool if len(d) >= len(answer)]
    need = OPTION_COUNT - 1
    feasible = [r for r in range(need + 1) if r <= len(shorter) and need - r <= len(rest)]
    rank = rng.randrange(need + 1)
    if rank not in feasible:
        rank = rng.choice(feasible)
    return rng.sample(shorter, rank) + rng.sample(rest, need - rank)


def int_fact(facts: Mapping[str, object], name: str) -> int:
    value = facts[name]
    if not isinstance(value, int):
        raise UnsolvableItem(f"fact {name!r} is not a whole number")
    return value


def str_fact(facts: Mapping[str, object], name: str) -> str:
    value = facts[name]
    if not isinstance(value, str):
        raise UnsolvableItem(f"fact {name!r} is not text")
    return value


def pick_wrong(
    rng: random.Random, key: Fraction, candidates: Sequence[Fraction], *, cap: Fraction | None = None
) -> list[Fraction]:
    """Near misses of `key`: candidates within a believable band, topped up with small random offsets."""
    low, high = key * Fraction(1, 2), key * Fraction(9, 5)
    kept: list[Fraction] = [
        c for c in candidates if low <= c <= high and c != key and (cap is None or c <= cap)
    ]
    step = max(key / 25, Fraction(1, 2))
    offsets = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 7, -7]
    rng.shuffle(offsets)
    kept.extend(key + offset * step for offset in offsets)
    return [c for c in dict.fromkeys(kept) if c > 0 and c != key and (cap is None or c <= cap)]
