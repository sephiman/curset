# SPDX-License-Identifier: AGPL-3.0-only
"""`topological-order-valid`: which ordering of a directed acyclic graph points every edge forward."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Edges = tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class Dag:
    vertices: int
    edges: Edges


def is_topological(edges: Edges, order: tuple[int, ...]) -> bool:
    position = {v: i for i, v in enumerate(order)}
    return all(position[a] < position[b] for a, b in edges)


def reverse_postorder(s: Dag) -> tuple[int, ...]:
    seen: set[int] = set()
    post: list[int] = []

    def visit(v: int) -> None:
        seen.add(v)
        for a, b in s.edges:
            if a == v and b not in seen:
                visit(b)
        post.append(v)

    for v in range(s.vertices):
        if v not in seen:
            visit(v)
    return tuple(reversed(post))


def _text(order: tuple[int, ...]) -> str:
    return code(", ".join(map(str, order)))


def _violated(edges: Edges, order: tuple[int, ...]) -> tuple[int, int]:
    position = {v: i for i, v in enumerate(order)}
    return next((a, b) for a, b in edges if position[a] > position[b])


class TopologicalOrderGenerator(BackendGenerator[Dag]):
    id: ClassVar[str] = "topological-order-valid"
    citation: ClassVar[Citation] = Citation("m02-l04", "erickson-dfs#p8", confirmed="erickson-dfs#p8")

    def scenario(self, rng: random.Random, level: int) -> Dag | None:
        vertices = 5 if level == 1 else 6
        hidden = rng.sample(range(vertices), vertices)
        pool = [(hidden[i], hidden[j]) for i in range(vertices) for j in range(i + 1, vertices)]
        edges = tuple(sorted(rng.sample(pool, vertices + rng.randint(0, 2))))
        return Dag(vertices, edges)

    def stem(self, s: Dag) -> str:
        edges = ", ".join(code(f"{a}->{b}") for a, b in s.edges)
        return (
            f"A directed graph on vertices 0 to {s.vertices - 1} has edges {edges}. Which ordering of the "
            f"vertices is a topological ordering, with every edge pointing from left to right?"
        )

    def correct(self, s: Dag) -> str:
        return _text(reverse_postorder(s))

    def mistakes(self, s: Dag) -> list[str]:
        right = reverse_postorder(s)
        swapped = list(right)
        a, b = s.edges[0]
        swapped[right.index(a)], swapped[right.index(b)] = b, a
        source_last = (*right[1:], right[0])
        candidates = [
            tuple(reversed(right)),
            tuple(swapped),
            tuple(range(s.vertices)),
            source_last,
            tuple(sorted(range(s.vertices), key=lambda v: (-sum(x == v for x, _ in s.edges), v))),
        ]
        return [_text(c) for c in candidates if not is_topological(s.edges, c)]

    def explanation(self, s: Dag) -> str:
        return f"{self._working(s)} Source: {code(self.citation.confirmed)}."

    def _working(self, s: Dag) -> str:
        right = reverse_postorder(s)
        position = {v: i + 1 for i, v in enumerate(right)}
        checks = "; ".join(
            f"{i}. {code(f'{a}->{b}')} has {a} at place {position[a]} and {b} at place {position[b]}"
            for i, (a, b) in enumerate(s.edges, 1)
        )
        reverse = tuple(reversed(right))
        a, b = _violated(s.edges, reverse)
        return (
            f"An ordering is topological when every edge's tail comes before its head. The reversed "
            f"postorder of a depth-first search is one: {_text(right)}. Checking each edge: {checks}. "
            f"Every tail is left of its head. The postorder itself, {_text(reverse)}, fails on "
            f"{code(f'{a}->{b}')}."
        )
