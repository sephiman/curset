# SPDX-License-Identifier: AGPL-3.0-only
"""A generated item: what the learner sees, the key, and the facts the solver recomputes from."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field

OPTION_COUNT = 4


@dataclass(frozen=True)
class Table:
    """A table shown above the stem, rendered like an esquema `tabla`."""

    title: str
    header: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]


@dataclass(frozen=True)
class Item:
    generator: str
    seed: int
    difficulty: int
    stem: str
    options: tuple[str, ...]
    #: Index into `options` of the answer the generator built the item around.
    key: int
    explanation: str
    table: Table | None = None
    #: Plain data the solver recomputes the answer from, never read back from `key`.
    facts: Mapping[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class Params:
    difficulty: int = 2
