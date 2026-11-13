# SPDX-License-Identifier: AGPL-3.0-only
"""`composite-index-usage`: which predicates bound the scan of a PostgreSQL multicolumn B-tree index."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code

COLUMNS = ("tenant_id", "status", "created_at", "region", "user_id", "category")
EQ, RANGE = "=", ">"


@dataclass(frozen=True)
class IndexedQuery:
    index: tuple[str, ...]
    #: Column -> operator; columns not in the query are absent.
    predicates: tuple[tuple[str, str], ...]


def bounding(index: tuple[str, ...], predicates: dict[str, str]) -> list[str]:
    """Equality on leading columns, then any inequality on the first column without equality."""
    bounded: list[str] = []
    for column in index:
        operator = predicates.get(column)
        if operator is None:
            break
        bounded.append(column)
        if operator != EQ:
            break
    return bounded


def _prefix_ignoring_ranges(index: tuple[str, ...], predicates: dict[str, str]) -> list[str]:
    """The mistake of letting the prefix run on after an inequality column."""
    prefix: list[str] = []
    for column in index:
        if column not in predicates:
            break
        prefix.append(column)
    return prefix


def _columns(columns: list[str]) -> str:
    if not columns:
        return "None of them"
    names = [code(c) for c in columns]
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + f" and {names[-1]}"


class CompositeIndexGenerator(BackendGenerator[IndexedQuery]):
    id: ClassVar[str] = "composite-index-usage"
    citation: ClassVar[Citation] = Citation("m06-l03", "pg-indexes-multicolumn#INDEXES-MULTICOLUMN")

    def scenario(self, rng: random.Random, level: int) -> IndexedQuery:
        index = tuple(rng.sample(COLUMNS, rng.choice((3, 4))))
        size = rng.randint(2, len(index))
        chosen = rng.sample(index, size)
        ops = {c: (EQ if level == 1 or rng.random() < 0.6 else RANGE) for c in chosen}
        return IndexedQuery(index, tuple((c, ops[c]) for c in index if c in ops))

    def stem(self, s: IndexedQuery) -> str:
        where = " AND ".join(f"{c} {op} ?" for c, op in s.predicates)
        return (
            f"A PostgreSQL 18 table has a B-tree index on {code('(' + ', '.join(s.index) + ')')}. A query "
            f"runs "
            f"{code('WHERE ' + where)}. Which columns' conditions are guaranteed to limit the portion of the "
            f"index "
            f"that is scanned, ignoring skip scan?"
        )

    def correct(self, s: IndexedQuery) -> str:
        return _columns(bounding(s.index, dict(s.predicates)))

    def mistakes(self, s: IndexedQuery) -> list[str]:
        predicates = dict(s.predicates)
        present = [c for c in s.index if c in predicates]
        bounded = bounding(s.index, predicates)
        return [
            _columns(present),
            _columns(present[:1]),
            _columns([c for c in present if predicates[c] == EQ]),
            _columns(_prefix_ignoring_ranges(s.index, predicates)),
            _columns(bounded[:-1]),
            _columns(present[-1:]),
            _columns(list(s.index)),
            _columns(list(s.index[:1])),
        ]

    def explanation(self, s: IndexedQuery) -> str:
        predicates = dict(s.predicates)
        steps = []
        for column in s.index:
            operator = predicates.get(column)
            if operator is None:
                steps.append(f"{code(column)} has no condition, so the leading prefix ends here")
                break
            if operator == EQ:
                steps.append(
                    f"{code(column)} has an equality, so it bounds the scan and the next column counts too"
                )
            else:
                steps.append(
                    f"{code(column)} has an inequality, which still bounds the scan but ends the prefix"
                )
                break
        ending = (
            " Conditions on later columns are only checked inside the index: they save table visits but do "
            "not shrink the scanned range."
        )
        return (
            "The rule: equality conditions on leading columns, plus an inequality on the first column "
            "without "
            "an "
            "equality, limit the scanned range. Going through the index in order: "
            + "; ".join(steps)
            + "."
            + ending
        )
