# SPDX-License-Identifier: AGPL-3.0-only
"""`union-find-sets`: the sets a disjoint-set structure holds after a sequence of `union` calls."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Kind = Literal["count", "largest"]
Sets = list[frozenset[int]]
Unions = tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class Merges:
    kind: Kind
    size: int
    unions: Unions


def merge_all(size: int, unions: Unions, *, move_only: str | None = None) -> Sets:
    """`move_only` "a" or "b" models a union that relinks one element instead of joining both sets."""
    sets: Sets = [frozenset({v}) for v in range(size)]

    def holder(v: int) -> frozenset[int]:
        return next(group for group in sets if v in group)

    for a, b in unions:
        ga, gb = holder(a), holder(b)
        if ga == gb:
            continue
        if move_only is None:
            sets.remove(ga)
            sets.remove(gb)
            sets.append(ga | gb)
            continue
        mover, target = (a, gb) if move_only == "a" else (b, ga)
        source = ga if move_only == "a" else gb
        sets.remove(source)
        sets.remove(target)
        sets.extend([source - {mover}, target | {mover}] if len(source) > 1 else [target | {mover}])
    return sets


def _largest(sets: Sets) -> int:
    return max(len(group) for group in sets)


class UnionFindGenerator(BackendGenerator[Merges]):
    id: ClassVar[str] = "union-find-sets"
    citation: ClassVar[Citation] = Citation(
        "m02-l04", "erickson-union-find#p1", confirmed="erickson-union-find#p1"
    )

    def scenario(self, rng: random.Random, level: int) -> Merges | None:
        size = 7 if level == 1 else 8
        count = rng.randint(4, 6) if level == 1 else rng.randint(5, 7)
        unions = tuple((a, b) for a, b in (rng.sample(range(size), 2) for _ in range(count)))
        kind: Kind = "count" if level == 1 else "largest"
        return Merges(kind, size, unions)

    def stem(self, s: Merges) -> str:
        calls = ", ".join(code(f"union({a},{b})") for a, b in s.unions)
        ask = "How many sets remain?" if s.kind == "count" else "What size is the largest set?"
        return (
            f"A union-find structure starts with {s.size} singleton sets, one per element 0 to "
            f"{s.size - 1}. Each {code('union(a,b)')} merges the whole sets of a and b. "
            f"It runs {calls}. {ask}"
        )

    def _render(self, s: Merges, sets: Sets) -> str:
        return str(len(sets) if s.kind == "count" else _largest(sets))

    def correct(self, s: Merges) -> str:
        return self._render(s, merge_all(s.size, s.unions))

    def mistakes(self, s: Merges) -> list[str]:
        runs = [
            merge_all(s.size, s.unions[:-1]),
            merge_all(s.size, s.unions[1:]),
            merge_all(s.size, s.unions, move_only="a"),
            merge_all(s.size, s.unions, move_only="b"),
        ]
        wrong = [self._render(s, sets) for sets in runs]
        if s.kind == "count":
            touched = {v for pair in s.unions for v in pair}
            return [*wrong, str(s.size - len(s.unions)), str(len(touched)), str(s.size)]
        return [*wrong, str(len(s.unions) + 1), str(len(merge_all(s.size, s.unions)))]

    def explanation(self, s: Merges) -> str:
        return f"{self._working(s)} Source: {code(self.citation.confirmed)}."

    def _working(self, s: Merges) -> str:
        steps = []
        for i in range(1, len(s.unions) + 1):
            a, b = s.unions[i - 1]
            sets = merge_all(s.size, s.unions[:i])
            same = len(sets) == len(merge_all(s.size, s.unions[: i - 1]))
            note = " (already in one set, nothing changes)" if same else ""
            tally = f"{len(sets)} {'set' if len(sets) == 1 else 'sets'}, largest {_largest(sets)}"
            steps.append(f"{i}. {code(f'union({a},{b})')}{note} leaves {tally}")
        final = self._render(s, merge_all(s.size, s.unions))
        return (
            f"A union replaces the two sets of its arguments with their union, and a union of two elements "
            f"already in one set changes nothing. Start with {s.size} sets of one element. "
            f"{'; '.join(steps)}. Result: {final}."
        )
