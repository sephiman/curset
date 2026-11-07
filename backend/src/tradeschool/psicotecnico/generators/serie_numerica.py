# SPDX-License-Identifier: AGPL-3.0-only
"""`serie-numerica`: every rule of the family that explains the series must continue it the same way."""

from __future__ import annotations

import random
from collections.abc import Callable
from fractions import Fraction
from itertools import pairwise
from typing import ClassVar

from tradeschool.psicotecnico.contract import ItemGenerator, UnsolvableItem, deal
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.spanish import number

Fit = Callable[[list[int]], int | None]


def _geometric(terms: list[int]) -> int | None:
    if len(terms) < 3 or 0 in terms:
        return None
    ratio = Fraction(terms[1], terms[0])
    if ratio == 1 or any(Fraction(b, a) != ratio for a, b in pairwise(terms)):
        return None
    nxt = terms[-1] * ratio
    return int(nxt) if nxt.denominator == 1 else None


def _arithmetic(terms: list[int]) -> int | None:
    if len(terms) < 3:
        return None
    step = terms[1] - terms[0]
    if step == 0 or any(b - a != step for a, b in pairwise(terms)):
        return None
    return terms[-1] + step


def _alternating(terms: list[int]) -> int | None:
    diffs = [b - a for a, b in pairwise(terms)]
    if len(diffs) < 4 or diffs[0] == diffs[1] or any(diffs[i] != diffs[i - 2] for i in range(2, len(diffs))):
        return None
    return terms[-1] + diffs[-2]


def _recurrent(terms: list[int]) -> int | None:
    if len(terms) < 4 or terms[1] == terms[0]:
        return None
    ratio = Fraction(terms[2] - terms[1], terms[1] - terms[0])
    if ratio.denominator != 1 or ratio < 2:
        return None
    offset = terms[1] - ratio * terms[0]
    if offset.denominator != 1 or abs(offset) > 12:
        return None
    if any(b != ratio * a + offset for a, b in pairwise(terms)):
        return None
    return int(ratio * terms[-1] + offset)


def _interleaved(terms: list[int]) -> int | None:
    if len(terms) < 6:
        return None
    parts = [terms[0::2], terms[1::2]]
    follows = []
    for part in parts:
        fits = {f(part) for f in (_arithmetic, _geometric)} - {None}
        if len(fits) != 1:
            return None
        follows.append(fits.pop())
    return follows[len(terms) % 2]


def _product_chain(terms: list[int]) -> int | None:
    """a, f₁, a·f₁, f₂, a·f₁·f₂, f₃, …: every even position is the product of the two before it."""
    if len(terms) < 6 or len(terms) % 2:
        return None
    if any(terms[i] != terms[i - 2] * terms[i - 1] for i in range(2, len(terms), 2)):
        return None
    return terms[-2] * terms[-1]


FAMILY: tuple[Fit, ...] = (_geometric, _arithmetic, _alternating, _recurrent, _interleaved, _product_chain)


def continuations(terms: list[int]) -> set[int]:
    return {c for fit in FAMILY if (c := fit(terms)) is not None}


def _geometric_up(rng: random.Random, level: int) -> list[int]:
    ratio, start = rng.choice([2, 3, 4, 5]), rng.randint(1, 6)
    return [start * ratio**i for i in range(rng.randint(5, 6))]


def _geometric_down(rng: random.Random, level: int) -> list[int]:
    ratio, start, length = rng.choice([2, 3, 4]), rng.randint(1, 4), rng.randint(5, 6)
    return [start * ratio ** (length - 1 - i) for i in range(length)]


def _arith(rng: random.Random, level: int) -> list[int]:
    start, step = rng.randint(2, 30), rng.choice([3, 4, 6, 7, 9, 11])
    return [start + step * i for i in range(rng.randint(5, 6))]


def _alt(rng: random.Random, level: int) -> list[int]:
    a, b = rng.sample(range(1, 9), 2)
    out = [rng.randint(1, 20)]
    for i in range(5):
        out.append(out[-1] + (a if i % 2 == 0 else b))
    return out


def _rec(rng: random.Random, level: int) -> list[int]:
    p, q = rng.choice([2, 2, 3]), rng.choice([1, 2, 3, -1, 4, 5])
    out = [rng.randint(1, 4)]
    for _ in range(4 if p == 3 else 5):
        out.append(p * out[-1] + q)
    return out


def _inter(rng: random.Random, level: int) -> list[int]:
    def sub() -> list[int]:
        if rng.random() < 0.5:
            start, step = rng.randint(1, 20), rng.choice([2, 3, 5, 6])
            return [start + step * i for i in range(4)]
        start, ratio = rng.randint(1, 5), rng.choice([2, 3])
        return [start * ratio**i for i in range(4)]

    first, second = sub(), sub()
    return [v for pair in zip(first, second, strict=True) for v in pair][:6]


def _chain(rng: random.Random, level: int) -> list[int]:
    start, factor = rng.randint(2, 7), rng.randint(2, 4)
    out = [start]
    for i in range(3):
        out += [factor + i, out[-1] * (factor + i)]
    return out[:6]


_BY_LEVEL: dict[int, list[Callable[[random.Random, int], list[int]]]] = {
    1: [_geometric_up, _geometric_down, _arith],
    2: [_alt, _rec, _inter, _chain],
    3: [_inter, _rec, _chain, _alt],
}


def _rule_text(terms: list[int], answer: int) -> str:
    kinds = {fit(terms): fit for fit in FAMILY if fit(terms) is not None}
    fit = kinds[answer]
    shown = ", ".join(str(t) for t in terms)
    text = {
        "_geometric": "cada término es el anterior multiplicado (o dividido) por una razón constante",
        "_arithmetic": "cada término suma una cantidad constante al anterior",
        "_alternating": "se suman alternativamente dos cantidades fijas",
        "_recurrent": "cada término es el anterior multiplicado por una constante más otra constante",
        "_interleaved": "son dos series intercaladas, cada una con su propia regla",
        "_product_chain": "cada término en posición par es el producto de los dos anteriores",
    }[fit.__name__]
    return f"En {shown}, {text}; el que sigue es {number(answer)}."


class SerieNumericaGenerator(ItemGenerator):
    id: ClassVar[str] = "serie-numerica"

    def build(self, seed: int, params: Params) -> Item:
        rng = random.Random(seed)
        for _ in range(500):
            terms = rng.choice(_BY_LEVEL[params.difficulty])(rng, params.difficulty)
            found = continuations(terms)
            if len(found) != 1 or len(set(terms)) < len(terms) - 1 or max(map(abs, terms)) > 4000:
                continue
            answer = next(iter(found))
            wrong = self._wrong(rng, terms, answer)
            if len(wrong) < 3:
                continue
            options, slot = deal(rng, number(answer), [number(w) for w in wrong[:6]])
            return Item(
                generator=self.id,
                seed=seed,
                difficulty=params.difficulty,
                stem="¿Qué número continúa la secuencia " + ", ".join(str(t) for t in terms) + ", _?",
                options=options,
                key=slot,
                explanation=_rule_text(terms, answer),
                facts={"terms": terms},
            )
        raise RuntimeError(f"no series for seed {seed}")

    @staticmethod
    def _wrong(rng: random.Random, terms: list[int], answer: int) -> list[int]:
        pool = {
            terms[-1] + (terms[-1] - terms[-2]),
            terms[-1] * 2,
            terms[-1] + terms[-2],
            terms[-1] * (terms[-1] // max(terms[-2], 1) or 2),
        }
        unit = max(1, 10 ** (len(str(abs(answer))) - 2))
        pool |= {answer + k * unit for k in (-4, -2, -1, 1, 2, 4)}
        near = [v for v in pool if v > 0 and v != answer and answer / 2 <= v <= answer * 2]
        rng.shuffle(near)
        return near

    def solve(self, item: Item) -> int:
        terms = item.facts["terms"]
        assert isinstance(terms, list)
        found = continuations([int(t) for t in terms])
        if len(found) != 1:
            raise UnsolvableItem(f"rules of the family give {sorted(found)}")
        expected = number(next(iter(found)))
        hits = [i for i, option in enumerate(item.options) if option == expected]
        if len(hits) != 1:
            raise UnsolvableItem(f"{len(hits)} options read {expected}")
        return hits[0]
