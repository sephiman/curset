# SPDX-License-Identifier: AGPL-3.0-only
"""`keyset-next-page`: the ids a row-comparison next page returns (keys ascending)."""

from __future__ import annotations

import random
from dataclasses import dataclass, replace
from typing import ClassVar, cast

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.item import Item, Params

Row = tuple[int, int]
ANCHOR = "pg-functions-comparisons#ROW-WISE-COMPARISON"


@dataclass(frozen=True)
class Page:
    #: Rows `(score, id)` in sort order, ids unique.
    rows: tuple[Row, ...]
    last: Row
    limit: int


def next_page_rows(rows: tuple[Row, ...], last: Row) -> tuple[Row, ...]:
    """Row comparison compares left to right, so tuple order is the SQL order."""
    return tuple(row for row in rows if row > last)


def ids_after(rows: tuple[Row, ...], last: Row, limit: int) -> tuple[int, ...]:
    return tuple(row[1] for row in next_page_rows(rows, last)[:limit])


def _ids(keep: list[Row] | tuple[Row, ...], limit: int) -> str:
    return code(", ".join(str(row[1]) for row in keep[:limit]))


def _wrong_filters(s: Page) -> list[tuple[str, str, list[Row]]]:
    """Each wrong filter as (condition, what it does in every item, the rows it keeps)."""
    score, ident = s.last
    return [
        (f"score > {score}", "compares only the score", [r for r in s.rows if r[0] > score]),
        (f"score >= {score}", "compares only the score and keeps ties", [r for r in s.rows if r[0] >= score]),
        (
            f"score > {score} AND id > {ident}",
            "tests the score and the id separately",
            [r for r in s.rows if r[0] > score and r[1] > ident],
        ),
        (
            f"(score, id) >= ({score}, {ident})",
            "uses `>=` instead of `>`",
            [r for r in s.rows if r >= s.last],
        ),
        (f"id > {ident}", "compares only the id", [r for r in s.rows if r[1] > ident]),
    ]


class KeysetNextPageGenerator(BackendGenerator[Page]):
    id: ClassVar[str] = "keyset-next-page"
    citation: ClassVar[Citation] = Citation("m06-l03", ANCHOR, confirmed=ANCHOR)
    levels: ClassVar[tuple[int, ...]] = (2,)

    def scenario(self, rng: random.Random, level: int) -> Page | None:
        ids = rng.sample(range(10, 100), 6)
        scores = sorted(rng.choice((50, 70, 90)) for _ in ids)
        rows = tuple(sorted(zip(scores, ids, strict=True)))
        last = rows[rng.randint(0, 2)]
        limit = rng.choice((2, 3))
        if len(next_page_rows(rows, last)) < limit or not any(r[0] == last[0] and r != last for r in rows):
            return None
        return Page(rows, last, limit)

    def stem(self, s: Page) -> str:
        listed = ", ".join(code(f"({a}, {b})") for a, b in s.rows)
        return (
            f"Rows {code('(score, id)')}: {listed}. The page before ended at {code(str(s.last))}. "
            f"Which ids does {code(f'WHERE (score, id) > {s.last} ORDER BY score, id LIMIT {s.limit}')} "
            "return?"
        )

    def correct(self, s: Page) -> str:
        return _ids(next_page_rows(s.rows, s.last), s.limit)

    def mistakes(self, s: Page) -> list[str]:
        return [text for _, _, text in self._candidates(s)]

    def build(self, seed: int, params: Params) -> Item:
        item = super().build(seed, params)
        page = cast(Page, item.facts["scenario"])
        return replace(item, explanation=self._explain(page, item.options))

    def explanation(self, s: Page) -> str:
        return self._explain(s, self.mistakes(s))

    def _explain(self, s: Page, shown: tuple[str, ...] | list[str]) -> str:
        rule = (
            "A row constructor comparison compares its elements left to right and "
            "stops at the first unequal pair, "
            f"so {code('(score, id) > (a, b)')} keeps a row with a larger score, "
            "or with the same score and a larger id."
        )
        kept = ", ".join(str(r) for r in next_page_rows(s.rows, s.last))
        body = (
            f"Rows after {code(str(s.last))}: {kept}. The first {s.limit} in sort order have ids "
            f"{self.correct(s)}."
        )
        wrong = " ".join(
            f"{text} is what {code(f'WHERE {cond}')} returns under the same {code('ORDER BY')} and "
            f"{code('LIMIT')}, since it {does}."
            for cond, does, text in self._candidates(s)
            if text in shown and text != self.correct(s)
        )
        return f"{rule} {body} Wrong options: {wrong} Source: `{ANCHOR}`."

    def _candidates(self, s: Page) -> list[tuple[str, str, str]]:
        """Condition, description and ids of the wrong filters whose ids no other wrong filter shares."""
        full = [
            (cond, does, _ids(keep, s.limit))
            for cond, does, keep in _wrong_filters(s)
            if len(keep) >= s.limit
        ]
        texts = [text for _, _, text in full]
        return [row for row in full if texts.count(row[2]) == 1]
