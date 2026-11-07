# SPDX-License-Identifier: AGPL-3.0-only
"""Write the psicotécnico goldens (50 per generator) and their fingerprints; `--check` verifies them."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tradeschool.content.registry import load_registry
from tradeschool.psicotecnico.goldens import fingerprint, golden_items, solved_key
from tradeschool.psicotecnico.item import Item

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content" / "age-auxiliar-c2"
REVIEW_DIR = ROOT / "docs" / "age-verification" / "c2" / "psicotecnicos"
FINGERPRINTS = ROOT / "backend" / "tests" / "goldens" / "psicotecnico-fingerprints.json"


def _table(item: Item) -> list[str]:
    if item.table is None:
        return []
    header = "| " + " | ".join(item.table.header) + " |"
    rule = "|" + "|".join("---" for _ in item.table.header) + "|"
    rows = ["| " + " | ".join(row) + " |" for row in item.table.rows]
    return [f"Tabla «{item.table.title}»:", "", header, rule, *rows, ""]


def render(title: str, generator: str, items: list[Item]) -> str:
    lines = [
        f"# {title} (`{generator}`) — 50 goldens",
        "",
        "Generated items for the blind review (ambiguity, realism, key). Each is `seed`, difficulty level, "
        "stem, "
        "options in the order shown, the key the solver computes and the explanation shown after answering. "
        "Regenerate with `uv run python scripts/export_psicotecnico_goldens.py`.",
        "",
    ]
    for number, item in enumerate(items, start=1):
        key = solved_key(item)
        lines += [
            f"## {number}. seed {item.seed} · nivel {item.difficulty}",
            "",
            *_table(item),
            item.stem,
            "",
        ]
        lines += [f"{chr(97 + i)}) {option}" for i, option in enumerate(item.options)]
        lines += ["", f"**Clave: {chr(97 + key)}**", "", f"Explicación: {item.explanation}", ""]
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    check = parser.parse_args().check
    registry = load_registry(COURSE, check_excerpts=False)
    digests: dict[str, str] = {}
    stale: list[str] = []
    for use in registry.generator_uses():
        items = golden_items(use)
        digests[use.generator] = fingerprint(items)
        page = REVIEW_DIR / f"{use.generator}.md"
        text = render(use.title.get("es"), use.generator, items)
        if check:
            if not page.exists() or page.read_text(encoding="utf-8") != text:
                stale.append(str(page))
        else:
            REVIEW_DIR.mkdir(parents=True, exist_ok=True)
            page.write_text(text, encoding="utf-8")
    document = json.dumps(digests, indent=2, sort_keys=True) + "\n"
    if check:
        if not FINGERPRINTS.exists() or FINGERPRINTS.read_text(encoding="utf-8") != document:
            stale.append(str(FINGERPRINTS))
        print("stale: " + ", ".join(stale) if stale else "goldens up to date")
        return 1 if stale else 0
    FINGERPRINTS.write_text(document, encoding="utf-8")
    print(f"wrote {len(digests)} review pages and {FINGERPRINTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
