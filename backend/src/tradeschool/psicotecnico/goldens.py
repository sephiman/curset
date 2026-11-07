# SPDX-License-Identifier: AGPL-3.0-only
"""The 50 seeded goldens per generator that a blind reader reviews, and the digest that pins them."""

from __future__ import annotations

import hashlib
import json
import random
from collections.abc import Sequence

from tradeschool.content.schema import GeneratorUse
from tradeschool.exercises.psicotecnico import PsicotecnicoConfig, build_item
from tradeschool.psicotecnico.item import Item
from tradeschool.psicotecnico.registry import load_generator

GOLDEN_COUNT = 50
_GOLDEN_BASE = 20261107


def golden_seeds(generator: str) -> list[int]:
    rng = random.Random(f"{_GOLDEN_BASE}:{generator}")
    return [rng.randrange(2**62) for _ in range(GOLDEN_COUNT)]


def golden_items(use: GeneratorUse) -> list[Item]:
    """The goldens as the course declares the generator, so the level mix is the one a learner meets."""
    config = PsicotecnicoConfig(type="psicotecnico", generator=use.generator, difficulty=use.difficulty)
    return [build_item(config, seed) for seed in golden_seeds(use.generator)]


def solved_key(item: Item) -> int:
    return load_generator(item.generator).solve(item)


def fingerprint(items: Sequence[Item]) -> str:
    """A digest of what the learner sees and the solver's key, over every golden."""
    document = [
        {
            "seed": item.seed,
            "level": item.difficulty,
            "stem": item.stem,
            "table": None
            if item.table is None
            else [item.table.title, list(item.table.header), [list(r) for r in item.table.rows]],
            "options": list(item.options),
            "key": solved_key(item),
            "explanation": item.explanation,
        }
        for item in items
    ]
    return hashlib.sha256(json.dumps(document, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
