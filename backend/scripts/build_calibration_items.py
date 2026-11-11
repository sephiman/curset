# SPDX-License-Identifier: AGPL-3.0-only
"""Write the stored psicotécnico calibration items of age-auxiliar-c2: one frozen item per generator level."""

from __future__ import annotations

import random
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tradeschool.content.registry import load_registry
from tradeschool.psicotecnico.item import Item, Params
from tradeschool.psicotecnico.registry import load_generator

COURSE = Path(__file__).resolve().parents[2] / "content" / "age-auxiliar-c2"
OUTPUT = COURSE / "exercises" / "ps-calibracion.yaml"
_SEED_BASE = "2026-11-11:calibration"


def calibration_seed(generator: str, level: int) -> int:
    return random.Random(f"{_SEED_BASE}:{generator}:{level}").randrange(2**62)


def calibration_item(generator: str, level: int) -> Item:
    return load_generator(generator).generate(calibration_seed(generator, level), Params(level))


def variant_id(generator: str, level: int) -> str:
    return f"cal-{generator}-n{level}"


def variant(item: Item) -> dict[str, object]:
    key = load_generator(item.generator).solve(item)
    out: dict[str, object] = {
        "id": variant_id(item.generator, item.difficulty),
        "prompt": {"es": item.stem},
    }
    if item.table is not None:
        out["table"] = {
            "title": item.table.title,
            "header": list(item.table.header),
            "rows": [list(row) for row in item.table.rows],
        }
    out["options"] = [
        {"id": "abcd"[i], "text": {"es": text}} | ({"correct": True} if i == key else {})
        for i, text in enumerate(item.options)
    ]
    out["explanation"] = {"es": item.explanation}
    out["difficulty"] = item.difficulty
    out["tags"] = [item.generator, f"seed:{item.seed}"]
    return out


def main() -> int:
    registry = load_registry(COURSE, check_excerpts=False)
    variants = [
        variant(calibration_item(use.generator, level))
        for use in registry.manifest.course.practice_generators
        for level in load_generator(use.generator).levels
    ]
    header = (
        "# SPDX-License-Identifier: AGPL-3.0-only\n"
        "# Psicotécnico calibration items (round R5): one item frozen per generator level, key from\n"
        "# the solver. Never drawn: tests only. Rebuild with scripts/build_calibration_items.py.\n"
    )
    body = yaml.dump(
        {"type": "quiz", "shuffle": False, "variants": variants},
        allow_unicode=True,
        sort_keys=False,
        width=120,
    )
    OUTPUT.write_text(header + body, encoding="utf-8")
    print(f"{len(variants)} calibration items -> {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
