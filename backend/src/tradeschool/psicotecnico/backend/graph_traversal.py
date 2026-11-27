# SPDX-License-Identifier: AGPL-3.0-only
"""`graph-traversal-order`: the order a queue-based BFS or a recursive DFS visits a small graph."""

from __future__ import annotations

import random
from collections import deque
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Kind = Literal["bfs", "dfs"]
Adjacency = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class Traversal:
    kind: Kind
    edges: tuple[tuple[int, int], ...]
    vertices: int
    start: int = 0


def adjacency_of(s: Traversal, *, descending: bool = False) -> Adjacency:
    return tuple(
        tuple(sorted({b if a == v else a for a, b in s.edges if v in (a, b)}, reverse=descending))
        for v in range(s.vertices)
    )


def bfs_order(adjacency: Adjacency, start: int) -> list[int]:
    seen, order, queue = {start}, [], deque([start])
    while queue:
        v = queue.popleft()
        order.append(v)
        for w in adjacency[v]:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    return order


def dfs_order(adjacency: Adjacency, start: int) -> list[int]:
    order: list[int] = []

    def visit(v: int) -> None:
        order.append(v)
        for w in adjacency[v]:
            if w not in order:
                visit(w)

    visit(start)
    return order


def stack_pop_order(adjacency: Adjacency, start: int) -> list[int]:
    """A stack that takes the newest of all pushed neighbours, marking a vertex when popped."""
    seen: list[int] = []
    stack = [start]
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.append(v)
        stack.extend(adjacency[v])
    return seen


def _postorder(adjacency: Adjacency, start: int) -> list[int]:
    """Vertices in the order the recursion finishes them, taken for the visit order."""
    done: list[int] = []
    seen: set[int] = set()

    def visit(v: int) -> None:
        seen.add(v)
        for w in adjacency[v]:
            if w not in seen:
                visit(w)
        done.append(v)

    visit(start)
    return done


def _levels_reversed(adjacency: Adjacency, start: int) -> list[int]:
    """Breadth-first levels, each read right to left."""
    seen, level = {start}, [start]
    order: list[int] = []
    while level:
        order.extend(reversed(level))
        following: list[int] = []
        for v in level:
            for w in adjacency[v]:
                if w not in seen:
                    seen.add(w)
                    following.append(w)
        level = following
    return order


def _words(items: list[int]) -> str:
    if not items:
        return "nothing"
    return ", ".join(map(str, items[:-1])) + (" and " if len(items) > 1 else "") + str(items[-1])


def _text(order: list[int]) -> str:
    return code(", ".join(map(str, order)))


def _order(s: Traversal) -> list[int]:
    walk = bfs_order if s.kind == "bfs" else dfs_order
    return walk(adjacency_of(s), s.start)


class GraphTraversalGenerator(BackendGenerator[Traversal]):
    id: ClassVar[str] = "graph-traversal-order"
    citation: ClassVar[Citation] = Citation(
        "m02-l04",
        "ods-12-3-graph-traversal#SECTION001531000000000000000",
        confirmed="ods-12-3-graph-traversal#SECTION001531000000000000000; "
        "ods-12-3-graph-traversal#SECTION001532000000000000000",
    )

    def scenario(self, rng: random.Random, level: int) -> Traversal | None:
        vertices = 6 if level == 1 else 7
        pool = [(a, b) for a in range(vertices) for b in range(a + 1, vertices)]
        edges = tuple(sorted(rng.sample(pool, vertices + rng.randint(-1, 0))))
        scenario = Traversal(rng.choice(("bfs", "dfs")), edges, vertices)
        reached = len(_order(scenario))
        wanted = range(5, vertices) if level == 1 else range(4, vertices)
        return scenario if reached in wanted else None

    def stem(self, s: Traversal) -> str:
        edges = ", ".join(code(f"{a}-{b}") for a, b in s.edges)
        walk = "a queue-based breadth-first" if s.kind == "bfs" else "a recursive depth-first"
        return (
            f"An undirected graph on vertices 0 to {s.vertices - 1} has edges {edges}. Neighbours are taken "
            f"in increasing order. In what order does {walk} search from {code(s.start)} visit the vertices?"
        )

    def correct(self, s: Traversal) -> str:
        return _text(_order(s))

    def mistakes(self, s: Traversal) -> list[str]:
        up, down = adjacency_of(s), adjacency_of(s, descending=True)
        other = dfs_order if s.kind == "bfs" else bfs_order
        walk = bfs_order if s.kind == "bfs" else dfs_order
        reached = _order(s)
        return [
            _text(other(up, s.start)),
            _text(walk(down, s.start)),
            _text(stack_pop_order(up, s.start)),
            _text(sorted(reached)),
            _text(_postorder(up, s.start) if s.kind == "dfs" else _levels_reversed(up, s.start)),
        ]

    def _anchor(self, s: Traversal) -> str:
        bfs, dfs = (ref.strip() for ref in str(self.citation.confirmed).split(";"))
        return bfs if s.kind == "bfs" else dfs

    def explanation(self, s: Traversal) -> str:
        return f"{self._working(s)} Source: {code(self._anchor(s))}."

    def _working(self, s: Traversal) -> str:
        up = adjacency_of(s)
        if s.kind == "bfs":
            steps: list[str] = []
            seen, queue = {s.start}, deque([s.start])
            while queue:
                v = queue.popleft()
                fresh = [w for w in up[v] if w not in seen]
                seen.update(fresh)
                queue.extend(fresh)
                steps.append(f"{len(steps) + 1}. take {v} from the queue, then add {_words(fresh)}")
            rule = (
                "A breadth-first search takes the oldest vertex of a queue and appends its unseen neighbours"
            )
        else:
            steps = []
            order: list[int] = []

            def visit(v: int, depth: int) -> None:
                order.append(v)
                steps.append(f"{len(steps) + 1}. enter {v} at depth {depth}")
                for w in up[v]:
                    if w not in order:
                        visit(w, depth + 1)

            visit(s.start, 0)
            rule = "A recursive depth-first search enters the first unseen neighbour before the next one"
        unreached = [v for v in range(s.vertices) if v not in _order(s)]
        names = ", ".join(map(str, unreached))
        tail = f" Not reachable from {s.start}, so never visited: {names}." if unreached else ""
        return f"{rule}. Steps: {'; '.join(steps)}. Visit order: {_text(_order(s))}.{tail}"
