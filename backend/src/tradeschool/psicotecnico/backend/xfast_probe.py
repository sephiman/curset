# SPDX-License-Identifier: AGPL-3.0-only
"""`xfast-level-probes`: the levels the binary search of an X-fast trie probes, and the `l` it ends with."""

from __future__ import annotations

import random
from dataclasses import dataclass, replace
from typing import ClassVar, cast

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.option_forms import plain_option
from tradeschool.psicotecnico.item import Item, Params

ANCHOR = "ods-13-2-xfasttrie-searching-in#SECTION001620000000000000000"


@dataclass(frozen=True)
class Search:
    w: int
    #: A node matches `x` at levels 0 to `depth` only.
    depth: int


def probe_levels(w: int, depth: int) -> tuple[int, ...]:
    """The loop of the listing: l = 0, h = w + 1, while h - l > 1 probe i = (l + h) / 2."""
    low, high, probed = 0, w + 1, []
    while high - low > 1:
        i = (low + high) // 2
        probed.append(i)
        if i <= depth:
            low = i
        else:
            high = i
    return tuple(probed)


def final_l(w: int, depth: int) -> int:
    low, high = 0, w + 1
    while high - low > 1:
        i = (low + high) // 2
        low, high = (i, high) if i <= depth else (low, i)
    return low


def _variant(
    w: int, depth: int, *, start_h: int, ceil: bool = False, swapped: bool = False
) -> tuple[int, ...]:
    low, high, probed = 0, start_h, []
    while high - low > 1:
        i = (low + high + (1 if ceil else 0)) // 2
        probed.append(i)
        if (i <= depth) != swapped:
            low = i
        else:
            high = i
    return tuple(probed)


def _text(levels: tuple[int, ...]) -> str:
    return code(", ".join(str(level) for level in levels))


class XFastProbeGenerator(BackendGenerator[Search]):
    id: ClassVar[str] = "xfast-level-probes"
    forms: ClassVar[tuple[str, ...]] = ("{}", "the levels {}", "exactly the levels {}", "levels {}, in order")
    citation: ClassVar[Citation] = Citation("m02-l02", ANCHOR, confirmed=ANCHOR)
    levels: ClassVar[tuple[int, ...]] = (2,)

    def scenario(self, rng: random.Random, level: int) -> Search:
        w = rng.choice((7, 8, 11, 12, 15))
        return Search(w, rng.randint(1, w - 1))

    def stem(self, s: Search) -> str:
        return (
            f"In the Open Data Structures X-fast trie, the search starts at {code('l = 0')}, "
            f"{code('h = w + 1')} with {code(f'w = {s.w}')}. "
            f"Nodes match {code('x')} at levels 0 to {s.depth} only. "
            f"Which levels {code('i')} are probed, in order?"
        )

    def correct(self, s: Search) -> str:
        return _text(probe_levels(s.w, s.depth))

    def mistakes(self, s: Search) -> list[str]:
        return [text for _, text in self._candidates(s)]

    def build(self, seed: int, params: Params) -> Item:
        item = super().build(seed, params)
        search = cast(Search, item.facts["scenario"])
        return replace(
            item, explanation=self._explain(search, tuple(plain_option(o, self.forms) for o in item.options))
        )

    def explanation(self, s: Search) -> str:
        return self._explain(s, tuple(self.mistakes(s)))

    def _candidates(self, s: Search) -> list[tuple[str, str]]:
        probes = probe_levels(s.w, s.depth)
        ceil = _variant(s.w, s.depth, start_h=s.w + 1, ceil=True)
        short = _variant(s.w, s.depth, start_h=s.w)
        swapped = _variant(s.w, s.depth, start_h=s.w + 1, swapped=True)
        return [
            ("comes from rounding the middle up", _text(ceil)),
            ("comes from starting with `h = w` instead of `h = w + 1`", _text(short)),
            ("comes from swapping the two updates", _text(swapped)),
            ("comes from scanning the levels one by one", _text(tuple(range(1, s.depth + 2)))),
            ("is the right probes in reverse order", _text(tuple(reversed(probes)))),
        ]

    def _explain(self, s: Search, shown: tuple[str, ...]) -> str:
        steps = []
        low, high = 0, s.w + 1
        for i in probe_levels(s.w, s.depth):
            hit = i <= s.depth
            outcome = (
                f"a node matches, so {code(f'l = {i}')}" if hit else f"no node matches, so {code(f'h = {i}')}"
            )
            steps.append(f"{code(f'i = ({low} + {high}) / 2 = {i}')}, {outcome}")
            low, high = (i, high) if hit else (low, i)
        rule = (
            f"The search sets {code('l = i')} when level i holds a matching node "
            f"and {code('h = i')} otherwise, and loops while {code('h - l > 1')}."
        )
        end = (
            f"The loop ends with {code(f'l = {final_l(s.w, s.depth)}')} and {code(f'h = {high}')}, "
            f"so {code('u')} is at level {low}."
        )
        reasons: dict[str, list[str]] = {}
        for reason, text in self._candidates(s):
            if text in shown and text != self.correct(s):
                reasons.setdefault(text, []).append(reason)
        wrong = " ".join(f"{text} {' and '.join(found)}." for text, found in reasons.items())
        walk = f"Here {code(f'w = {s.w}')}: {'; '.join(steps)}."
        return f"{rule} {walk} {end} Wrong options: {wrong} Source: `{ANCHOR}`."
