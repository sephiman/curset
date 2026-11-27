# SPDX-License-Identifier: AGPL-3.0-only
"""`partition-owner`: the PostgreSQL partition that receives a row under range or hash partitioning."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

Kind = Literal["range", "hash"]


@dataclass(frozen=True)
class Placement:
    kind: Kind
    #: Range: the ascending bounds, partition i holds [bounds[i], bounds[i+1]). Hash: unused.
    bounds: tuple[int, ...]
    modulus: int
    value: int


def range_owner(bounds: tuple[int, ...], value: int) -> int:
    """Partition i covers `FROM (bounds[i]) TO (bounds[i+1])`: lower bound inclusive, upper exclusive."""
    return next(i for i in range(len(bounds) - 1) if bounds[i] <= value < bounds[i + 1])


def _name(index: int) -> str:
    return code(f"p{index}")


def _partition_count(s: Placement) -> int:
    return s.modulus if s.kind == "hash" else len(s.bounds) - 1


class PartitionOwnerGenerator(BackendGenerator[Placement]):
    id: ClassVar[str] = "partition-owner"
    citation: ClassVar[Citation] = Citation(
        "m09-l02",
        "pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW",
        confirmed="pg-ddl-partitioning#DDL-PARTITIONING-OVERVIEW",
    )

    def scenario(self, rng: random.Random, level: int) -> Placement | None:
        if level == 2:
            modulus = rng.choice((3, 4, 5, 6, 7))
            return Placement("hash", (), modulus, rng.randint(20, 99))
        count = rng.randint(4, 5)
        bounds = [rng.choice((0, 100))]
        for _ in range(count):
            bounds.append(bounds[-1] + rng.choice((50, 100, 150)))
        value = rng.choice(bounds[1:-1])
        return Placement("range", tuple(bounds), 0, value)

    def stem(self, s: Placement) -> str:
        if s.kind == "hash":
            parts = f"{_name(0)} to {_name(s.modulus - 1)} take remainders 0 to {s.modulus - 1}"
            return (
                f"A table is hash partitioned with modulus {s.modulus}: {parts}. The hash value of a new "
                f"row's partition key is {code(s.value)}. Which partition receives the row?"
            )
        parts = ", ".join(
            f"{_name(i)} {code(f'FROM ({s.bounds[i]}) TO ({s.bounds[i + 1]})')}"
            for i in range(len(s.bounds) - 1)
        )
        return f"A range-partitioned table has {parts}. Which partition gets {code(f'id = {s.value}')}?"

    def _owner(self, s: Placement) -> int:
        return s.value % s.modulus if s.kind == "hash" else range_owner(s.bounds, s.value)

    def correct(self, s: Placement) -> str:
        return _name(self._owner(s))

    def mistakes(self, s: Placement) -> list[str]:
        count = _partition_count(s)
        owner = self._owner(s)
        if s.kind == "hash":
            wrong = [
                (s.value // s.modulus) % s.modulus,
                (owner + 1) % count,
                count - 1 - owner,
                s.value % (s.modulus + 1),
            ]
            return [_name(i) for i in wrong if 0 <= i < count]
        upper_inclusive = next(i for i in range(count) if s.bounds[i] < s.value <= s.bounds[i + 1])
        wrong = [upper_inclusive, owner + 1, owner - 1, s.value % count]
        return [_name(i) for i in wrong if 0 <= i < count]

    def explanation(self, s: Placement) -> str:
        return f"{self._working(s)} Source: {code(self.citation.confirmed)}."

    def _working(self, s: Placement) -> str:
        owner = self._owner(s)
        if s.kind == "hash":
            return (
                f"A hash partition holds the rows whose hash value divided by the modulus leaves its "
                f"remainder. 1. Divide {s.value} by {s.modulus}: {s.value // s.modulus} with remainder "
                f"{s.value % s.modulus}. 2. The partition with remainder {owner} is {_name(owner)}."
            )
        low, high = s.bounds[owner], s.bounds[owner + 1]
        return (
            f"A range partition holds the keys from its lower bound, inclusive, up to its upper bound, "
            f"exclusive, so {code('TO (n)')} excludes n and the next partition starts at n. "
            f"1. The key is {s.value}. 2. {_name(owner)} covers {low} up to but not including {high}, "
            f"and {low} <= {s.value} < {high}. 3. A key equal to a bound belongs to the partition that "
            f"starts there."
        )
