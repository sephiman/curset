# SPDX-License-Identifier: AGPL-3.0-only
"""`hashmap-resize-point`: when a chained hash table doubles and which bucket a key lands in afterwards."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Kind = Literal["first-resize", "buckets", "bucket-index", "second-resize"]
LOAD_FACTORS = ((1, 2), (3, 4))


@dataclass(frozen=True)
class Table:
    kind: Kind
    capacity: int
    load_num: int
    load_den: int
    entries: int
    key: int

    @property
    def load_text(self) -> str:
        return str(self.load_num / self.load_den)


def threshold(capacity: int, load_num: int, load_den: int) -> int:
    return capacity * load_num // load_den


def buckets_after(
    capacity: int, load_num: int, load_den: int, entries: int, *, at_threshold: bool = False
) -> int:
    """Buckets after `entries` inserts; `at_threshold` models a table that grows on reaching the limit."""
    buckets = capacity
    for count in range(1, entries + 1):
        limit = threshold(buckets, load_num, load_den)
        if count > limit or (at_threshold and count == limit):
            buckets *= 2
    return buckets


def _linear_buckets(s: Table) -> int:
    buckets = s.capacity
    for count in range(1, s.entries + 1):
        if count > threshold(buckets, s.load_num, s.load_den):
            buckets += s.capacity
    return buckets


def _resolved(s: Table) -> int:
    return buckets_after(s.capacity, s.load_num, s.load_den, s.entries)


WORDINGS: dict[Kind, tuple[str, ...]] = {
    "first-resize": ("{}", "insert {}", "insert number {}"),
    "buckets": ("{}", "{} buckets", "{} buckets in total"),
    "bucket-index": ("{}", "bucket {}", "bucket number {}"),
    "second-resize": ("{}", "insert {}", "insert number {}"),
}


def _worded(kind: Kind, value: int, salt: int) -> str:
    """The wording follows the value, so an option's length carries no information about the key."""
    options = WORDINGS[kind]
    return options[(value * 7 + salt) % len(options)].format(value)


def _salt(s: Table) -> int:
    return s.key + s.entries + s.capacity


class HashMapResizeGenerator(BackendGenerator[Table]):
    id: ClassVar[str] = "hashmap-resize-point"
    citation: ClassVar[Citation] = Citation(
        "m02-l01", "javadoc-hashmap#class-hashmap-k-v", confirmed="javadoc-hashmap#class-hashmap-k-v"
    )

    def scenario(self, rng: random.Random, level: int) -> Table | None:
        capacity = rng.choice((8, 16, 32))
        load_num, load_den = rng.choice(LOAD_FACTORS)
        limit = threshold(capacity, load_num, load_den)
        if level == 1:
            kind: Kind = rng.choice(("first-resize", "buckets"))
            entries = 2 * limit + rng.randint(1, 2) if kind == "buckets" else 0
        else:
            kind = rng.choice(("bucket-index", "second-resize", "second-resize"))
            entries = rng.choice((1, 2)) * limit + rng.randint(1, 3) if kind == "bucket-index" else 0
        key = rng.randint(3 * capacity, 12 * capacity)
        return Table(kind, capacity, load_num, load_den, entries, key)

    def stem(self, s: Table) -> str:
        base = (
            f"A table follows the {code('HashMap')} rule: {s.capacity} buckets, load factor "
            f"{code(s.load_text)}, buckets double once entries exceed load factor times buckets."
        )
        if s.kind == "first-resize":
            return f"{base} Which numbered insert, counting from 1, doubles it for the first time?"
        if s.kind == "second-resize":
            return f"{base} Which numbered insert, counting from 1, doubles it for the second time?"
        if s.kind == "buckets":
            return f"{base} After {s.entries} distinct keys are inserted, how many buckets does it have?"
        return (
            f"{base} The bucket is {code('key mod buckets')}. After {s.entries} distinct keys, in "
            f"which bucket does key {code(s.key)} sit?"
        )

    def correct(self, s: Table) -> str:
        if s.kind == "first-resize":
            return _worded(s.kind, threshold(s.capacity, s.load_num, s.load_den) + 1, _salt(s))
        if s.kind == "second-resize":
            return _worded(s.kind, threshold(2 * s.capacity, s.load_num, s.load_den) + 1, _salt(s))
        if s.kind == "buckets":
            return _worded(s.kind, _resolved(s), _salt(s))
        return _worded(s.kind, s.key % _resolved(s), _salt(s))

    def mistakes(self, s: Table) -> list[str]:
        limit = threshold(s.capacity, s.load_num, s.load_den)
        if s.kind == "first-resize":
            wrong = [limit, s.capacity, s.capacity + 1, 2 * limit + 1, s.capacity // 2 + 1]
            return [_worded(s.kind, v, _salt(s)) for v in wrong]
        early = buckets_after(s.capacity, s.load_num, s.load_den, s.entries, at_threshold=True)
        if s.kind == "second-resize":
            doubled = threshold(2 * s.capacity, s.load_num, s.load_den)
            wrong = [doubled, limit + 1, 2 * limit + 1, 2 * s.capacity + 1, s.capacity * 2]
            return [_worded(s.kind, v, _salt(s)) for v in wrong]
        if s.kind == "buckets":
            wrong = [early, s.capacity, _resolved(s) * 2, _linear_buckets(s)]
            return [_worded(s.kind, v, _salt(s)) for v in wrong]
        moduli = [early, s.capacity, _resolved(s) * 2, _linear_buckets(s), limit, s.entries]
        return [_worded(s.kind, s.key % m, _salt(s)) for m in moduli]

    def explanation(self, s: Table) -> str:
        return f"{self._working(s)} Source: {code(self.citation.confirmed)}."

    def _working(self, s: Table) -> str:
        limit = threshold(s.capacity, s.load_num, s.load_den)
        rule = (
            f"The table doubles when its entries exceed {code('load factor x buckets')}. "
            f"With {s.capacity} buckets that limit is {s.capacity} x {s.load_text} = {limit}."
        )
        if s.kind == "first-resize":
            return (
                f"{rule} Entry {limit} still fits, so entry {limit + 1} is the first to exceed it. "
                f"Answer: {limit + 1}."
            )
        if s.kind == "second-resize":
            doubled = threshold(2 * s.capacity, s.load_num, s.load_den)
            return (
                f"{rule} The first doubling gives {2 * s.capacity} buckets, so the limit becomes "
                f"{2 * s.capacity} x {s.load_text} = {doubled}. Entry {doubled} still fits, so entry "
                f"{doubled + 1} doubles the table again. Answer: {doubled + 1}."
            )
        steps, buckets = [], s.capacity
        for count in range(1, s.entries + 1):
            if count > threshold(buckets, s.load_num, s.load_den):
                buckets *= 2
                steps.append(
                    f"entry {count} exceeds {threshold(buckets // 2, s.load_num, s.load_den)}, "
                    f"so the table has {buckets} buckets"
                )
        grown = (
            "; ".join(f"{i}. {step}" for i, step in enumerate(steps, 1)) + "."
            if steps
            else "No insert exceeds the limit."
        )
        final = _resolved(s)
        if s.kind == "buckets":
            return f"{rule} {grown} After {s.entries} entries the table has {final} buckets."
        return (
            f"{rule} {grown} The table has {final} buckets, so the key {s.key} goes to bucket "
            f"{s.key} mod {final} = {s.key % final}."
        )
