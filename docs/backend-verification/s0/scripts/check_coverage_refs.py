# SPDX-License-Identifier: AGPL-3.0-only
"""Every `source#anchor` in the judged coverage TSVs resolves to a stored anchor; prints the ones that do not."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
ANCHORS = REPO / "content" / "backend-in-depth" / "sources" / "anchors"
COVERAGE = REPO / "docs" / "backend-verification" / "s0" / "coverage"


def main() -> None:
    known: dict[str, set[str]] = {}
    for path in ANCHORS.glob("*.json"):
        known[path.stem] = {a["anchor"] for a in json.loads(path.read_text(encoding="utf-8"))["anchors"]}
    broken = 0
    total = 0
    for tsv in sorted(COVERAGE.glob("m*.final.tsv")):
        with tsv.open(encoding="utf-8") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                for ref in filter(None, (r.strip() for r in row["tier_a"].split(";"))):
                    total += 1
                    source, _, anchor = ref.partition("#")
                    if anchor not in known.get(source, set()):
                        broken += 1
                        print(f"{tsv.name}\t{row['bullet']}\t{ref}")
    print(f"{total} refs, {broken} unresolved", file=sys.stderr)
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
