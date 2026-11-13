# SPDX-License-Identifier: AGPL-3.0-only
"""`lru-cache-contents`: the keys an LRU cache holds after a sequence of `get` and `put` calls."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Operation = tuple[str, str]


@dataclass(frozen=True)
class CacheRun:
    capacity: int
    operations: tuple[Operation, ...]


def replay(
    s: CacheRun, *, get_refreshes: bool = True, put_refreshes: bool = True, evict_newest: bool = False
) -> list[str]:
    """Keys from least to most recently used."""
    order: list[str] = []
    for name, key in s.operations:
        if key in order:
            if (name == "get" and get_refreshes) or (name == "put" and put_refreshes):
                order.remove(key)
                order.append(key)
        elif name == "put":
            if len(order) == s.capacity:
                order.pop(-1 if evict_newest else 0)
            order.append(key)
    return order


def _text(keys: list[str]) -> str:
    return code("[" + ", ".join(keys) + "]")


class LruCacheGenerator(BackendGenerator[CacheRun]):
    id: ClassVar[str] = "lru-cache-contents"
    citation: ClassVar[Citation] = Citation("m02-l06", "javadoc-linkedhashmap#class-linkedhashmap-k-v")

    def scenario(self, rng: random.Random, level: int) -> CacheRun | None:
        capacity = rng.choice((3, 4))
        keys = "ABCDEFG"[: capacity + (2 if level == 1 else 3)]
        count = rng.randint(7, 9) if level == 1 else rng.randint(9, 11)
        operations = tuple((rng.choice(("put", "put", "get")), rng.choice(keys)) for _ in range(count))
        scenario = CacheRun(capacity, operations)
        return scenario if len(replay(scenario)) == capacity else None

    def stem(self, s: CacheRun) -> str:
        calls = ", ".join(code(f"{name}({key})") for name, key in s.operations)
        return (
            f"An LRU cache of capacity {s.capacity} starts empty. A {code('get')} of a missing key changes "
            f"nothing; "
            f"a {code('put')} of a new key evicts the least recently used entry when the cache is full. Both "
            f"{code('get')} and {code('put')} of an existing key count as a use. After {calls}, which keys "
            f"does it "
            f"hold, from least to most recently used?"
        )

    def correct(self, s: CacheRun) -> str:
        return _text(replay(s))

    def mistakes(self, s: CacheRun) -> list[str]:
        right = replay(s)
        return [
            _text(replay(s, evict_newest=True)),
            _text(replay(s, get_refreshes=False)),
            _text(replay(s, put_refreshes=False)),
            _text(list(reversed(right))),
            _text(replay(s, get_refreshes=False, put_refreshes=False)),
        ]

    def explanation(self, s: CacheRun) -> str:
        steps = []
        for i in range(1, len(s.operations) + 1):
            name, key = s.operations[i - 1]
            state = replay(CacheRun(s.capacity, s.operations[:i]))
            steps.append(f"{code(f'{name}({key})')} gives {_text(state)}")
        return "Keep the keys ordered by last use, oldest first: " + "; ".join(steps) + "."
