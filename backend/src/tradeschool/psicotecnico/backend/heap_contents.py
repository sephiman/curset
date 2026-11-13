# SPDX-License-Identifier: AGPL-3.0-only
"""`binary-heap-contents`: an array-backed binary heap after insertions and removals of the root."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Operation = tuple[str, int]


@dataclass(frozen=True)
class HeapRun:
    minimum: bool
    operations: tuple[Operation, ...]


def _first(a: int, b: int, minimum: bool) -> bool:
    return a < b if minimum else a > b


def apply(
    s: HeapRun, *, minimum: bool | None = None, sift_up: bool = True, sift_down: bool = True
) -> list[int]:
    is_min = s.minimum if minimum is None else minimum
    heap: list[int] = []
    for name, value in s.operations:
        if name == "add":
            heap.append(value)
            i = len(heap) - 1
            while sift_up and i > 0 and _first(heap[i], heap[(i - 1) // 2], is_min):
                heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
                i = (i - 1) // 2
        elif heap:
            heap[0] = heap[-1]
            heap.pop()
            i = 0
            while (
                sift_down
                and (child := _best_child(heap, i, is_min)) is not None
                and _first(heap[child], heap[i], is_min)
            ):
                heap[i], heap[child] = heap[child], heap[i]
                i = child
    return heap


def _best_child(heap: list[int], i: int, minimum: bool) -> int | None:
    children = [c for c in (2 * i + 1, 2 * i + 2) if c < len(heap)]
    if not children:
        return None
    return min(children, key=lambda c: heap[c]) if minimum else max(children, key=lambda c: heap[c])


def _text(values: list[int]) -> str:
    return code("[" + ", ".join(map(str, values)) + "]")


class HeapContentsGenerator(BackendGenerator[HeapRun]):
    id: ClassVar[str] = "binary-heap-contents"
    forms: ClassVar[tuple[str, ...]] = ("{}", "the array {}", "the whole array {}")
    citation: ClassVar[Citation] = Citation(
        "m02-l03", "javadoc-priorityqueue#class-priorityqueue-e; javadoc-priorityqueue#poll()"
    )

    def scenario(self, rng: random.Random, level: int) -> HeapRun | None:
        values = rng.sample(range(1, 60), 9)
        operations: list[Operation] = [("add", v) for v in values[:5]]
        if level == 1:
            operations += [("add", v) for v in values[5:7]] + [("remove", 0)]
        else:
            tail = [
                ("add", values[5]),
                ("remove", 0),
                ("add", values[6]),
                ("remove", 0),
                ("add", values[7]),
                ("remove", 0),
            ]
            operations += tail
        scenario = HeapRun(rng.random() < 0.5, tuple(operations))
        return scenario if len({*self.mistakes(scenario), self.correct(scenario)}) >= 4 else None

    def stem(self, s: HeapRun) -> str:
        steps = ", ".join(
            code(f"add({v})") if name == "add" else code("removeRoot()") for name, v in s.operations
        )
        kind = "min-heap" if s.minimum else "max-heap"
        return (
            f"An empty array-backed binary {kind} (children of index {code('i')} at {code('2i + 1')} "
            f"and {code('2i + 2')}) "
            f"takes these operations in order: {steps}. {code('removeRoot()')} moves the last element to the "
            f"root "
            f"and sifts it down. What does the array hold afterwards?"
        )

    def correct(self, s: HeapRun) -> str:
        return _text(apply(s))

    def mistakes(self, s: HeapRun) -> list[str]:
        return [
            _text(apply(s, minimum=not s.minimum)),
            _text(apply(s, sift_down=False)),
            _text(apply(s, sift_up=False)),
            _text(sorted(apply(s), reverse=not s.minimum)),
        ]

    def explanation(self, s: HeapRun) -> str:
        steps = []
        for i in range(1, len(s.operations) + 1):
            name, value = s.operations[i - 1]
            action = f"add({value})" if name == "add" else "removeRoot()"
            steps.append(f"{code(action)} gives {_text(apply(HeapRun(s.minimum, s.operations[:i])))}")
        order = "smaller" if s.minimum else "larger"
        return (
            f"An add appends at the end and sifts up while it is {order} than its parent; a removal puts the "
            f"last "
            f"element at the root and sifts it down towards the {order} child. " + "; ".join(steps) + "."
        )
