# SPDX-License-Identifier: AGPL-3.0-only
"""`consistent-hashing-owner`: which node owns a key on a ring before and after a node joins or leaves."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

RING = 100
Kind = Literal["owner", "moved"]
NAMES = "ABCDEFGH"


@dataclass(frozen=True)
class Ring:
    kind: Kind
    nodes: tuple[tuple[str, int], ...]
    joins: bool
    changing: tuple[str, int]
    keys: tuple[int, ...]


def owner(nodes: tuple[tuple[str, int], ...], key: int, *, clockwise: bool = True) -> str:
    ordered = sorted(nodes, key=lambda n: n[1])
    if clockwise:
        return next((name for name, at in ordered if at >= key), ordered[0][0])
    return next((name for name, at in reversed(ordered) if at <= key), ordered[-1][0])


def after(s: Ring) -> tuple[tuple[str, int], ...]:
    if s.joins:
        return (*s.nodes, s.changing)
    return tuple(n for n in s.nodes if n != s.changing)


def moved(s: Ring, *, clockwise: bool = True) -> list[int]:
    return [
        k for k in s.keys if owner(s.nodes, k, clockwise=clockwise) != owner(after(s), k, clockwise=clockwise)
    ]


def _ring_text(nodes: tuple[tuple[str, int], ...]) -> str:
    return ", ".join(f"{code(name)} at {at}" for name, at in sorted(nodes, key=lambda n: n[1]))


class ConsistentHashingGenerator(BackendGenerator[Ring]):
    id: ClassVar[str] = "consistent-hashing-owner"
    citation: ClassVar[Citation] = Citation(
        "m09-l02", "paper-dynamo#p5", confirmed="paper-dynamo-columns#p10; paper-dynamo-columns#p11"
    )

    def scenario(self, rng: random.Random, level: int) -> Ring | None:
        joins = rng.random() < 0.5
        count = rng.randint(4, 5) if not joins else rng.randint(3, 4)
        positions = rng.sample(range(RING), count + (1 if joins else 0))
        names = NAMES[: count + 1]
        placed = tuple(zip(names, positions, strict=False))
        changing = placed[-1] if joins else rng.choice(placed)
        nodes = placed[:-1] if joins else placed
        kind: Kind = "owner" if level == 1 else "moved"
        keys = tuple(rng.sample(range(RING), 1 if kind == "owner" else rng.randint(6, 8)))
        scenario = Ring(kind, nodes, joins, changing, keys)
        if kind == "owner":
            return scenario if owner(nodes, keys[0]) != owner(after(scenario), keys[0]) else None
        return scenario if 2 <= len(moved(scenario)) < len(keys) - 1 else None

    def stem(self, s: Ring) -> str:
        change = (
            f"node {code(s.changing[0])} joins at position {s.changing[1]}"
            if s.joins
            else f"node {code(s.changing[0])} leaves"
        )
        setup = (
            f"A ring has positions 0 to {RING - 1}. A key belongs to the first node found going clockwise "
            f"(towards "
            f"higher positions, wrapping from {RING - 1} to 0) from the key's position, a node at the key's "
            f"own "
            f"position included. Nodes: {_ring_text(s.nodes)}. Then {change}."
        )
        if s.kind == "owner":
            return f"{setup} Which node owns the key at position {s.keys[0]} afterwards?"
        return (
            f"{setup} Of the keys at positions {', '.join(map(str, sorted(s.keys)))}, how many change owner?"
        )

    def correct(self, s: Ring) -> str:
        if s.kind == "owner":
            return f"Node {code(owner(after(s), s.keys[0]))}"
        return str(len(moved(s)))

    def mistakes(self, s: Ring) -> list[str]:
        if s.kind == "owner":
            key = s.keys[0]
            before = owner(s.nodes, key)
            reverse = owner(after(s), key, clockwise=False)
            successor = [n for n, _ in sorted(after(s), key=lambda n: n[1])]
            right = owner(after(s), key)
            next_one = successor[(successor.index(right) + 1) % len(successor)]
            return [f"Node {code(n)}" for n in (before, reverse, next_one, s.changing[0])]
        count = len(moved(s))
        everything = len(s.keys)
        return [
            str(len(moved(s, clockwise=False))),
            str(everything),
            str(count + 1),
            str(max(0, count - 1)),
            str(everything // len(after(s))),
        ]

    def explanation(self, s: Ring) -> str:
        if s.kind == "owner":
            key = s.keys[0]
            before, now = owner(s.nodes, key), owner(after(s), key)
            return (
                f"Before the change the first node clockwise from {key} was {code(before)}. The ring then "
                f"holds "
                f"{_ring_text(after(s))}; going clockwise from {key} the first node is {code(now)}, so it "
                f"owns the key. "
                f"Counterclockwise would give {code(owner(after(s), key, clockwise=False))}, which is not "
                f"the rule."
            )
        steps = "; ".join(
            f"{k}: {code(owner(s.nodes, k))} to {code(owner(after(s), k))}" for k in sorted(s.keys)
        )
        return (
            f"Compute the clockwise owner of each key before and after. {steps}. "
            f"{len(moved(s))} of them end up with a different owner; only the keys in the arc next to the "
            f"{'new' if s.joins else 'departed'} node move."
        )
