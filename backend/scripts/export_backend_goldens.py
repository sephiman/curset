# SPDX-License-Identifier: AGPL-3.0-only
"""Write the backend-in-depth generator goldens and fingerprints; `--check` verifies, `--citations` lists."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tradeschool.content.registry import load_registry
from tradeschool.psicotecnico.backend.catalogue import unfilled_citations
from tradeschool.psicotecnico.goldens import fingerprint, golden_items, solved_key
from tradeschool.psicotecnico.item import Item

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content" / "backend-in-depth"
REVIEW_DIR = ROOT / "docs" / "backend-verification" / "s1" / "generator-goldens"
FINGERPRINTS = ROOT / "backend" / "tests" / "goldens" / "backend-generators-fingerprints.json"


def render(title: str, generator: str, items: list[Item]) -> str:
    lines = [
        f"# {title} (`{generator}`): 50 goldens",
        "",
        "Generated items for the blind review (ambiguity, realism, key). Regenerate with "
        "`uv run python scripts/export_backend_goldens.py`.",
        "",
    ]
    for number, item in enumerate(items, start=1):
        key = solved_key(item)
        lines += [f"## {number}. seed {item.seed}, level {item.difficulty}", "", item.stem, ""]
        lines += [f"{chr(97 + i)}) {option}" for i, option in enumerate(item.options)]
        lines += ["", f"**Key: {chr(97 + key)}**", "", f"Explanation: {item.explanation}", ""]
    return "\n".join(lines).rstrip() + "\n"


def list_citations() -> int:
    rows = unfilled_citations()
    for generator, citation in rows:
        print(f"{generator}\t{citation.lesson}\t{citation.suggested}")
    print(f"{len(rows)} unfilled", file=sys.stderr)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--citations", action="store_true", help="list generators whose citation is unfilled")
    arguments = parser.parse_args()
    if arguments.citations:
        return list_citations()
    registry = load_registry(COURSE, check_excerpts=False)
    digests: dict[str, str] = {}
    stale: list[str] = []
    for use in registry.generator_uses():
        items = golden_items(use)
        digests[use.generator] = fingerprint(items)
        page = REVIEW_DIR / f"{use.generator}.md"
        text = render(use.title.get("en"), use.generator, items)
        if arguments.check:
            if not page.exists() or page.read_text(encoding="utf-8") != text:
                stale.append(str(page))
        else:
            REVIEW_DIR.mkdir(parents=True, exist_ok=True)
            page.write_text(text, encoding="utf-8")
    document = json.dumps(digests, indent=2, sort_keys=True) + "\n"
    if arguments.check:
        if not FINGERPRINTS.exists() or FINGERPRINTS.read_text(encoding="utf-8") != document:
            stale.append(str(FINGERPRINTS))
        print("stale: " + ", ".join(stale) if stale else "goldens up to date")
        return 1 if stale else 0
    FINGERPRINTS.write_text(document, encoding="utf-8")
    print(f"wrote {len(digests)} review pages and {FINGERPRINTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
