# SPDX-License-Identifier: AGPL-3.0-only
"""Append the verified glossary candidates of a module to the course glossary, citation kept as a comment.

    python merge_glossary.py MODULE_DIR [--course backend-in-depth]

A candidate whose id has a `fail` line in its lesson's verdict file is left out; an id already present is skipped.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[4]


def failed(verdicts: Path) -> set[str]:
    if not verdicts.exists():
        sys.exit(f"{verdicts}: no verdict file, refusing to merge unverified terms")
    final: dict[str, bool] = {}
    for line in verdicts.read_text().splitlines():
        p = line.split("\t")
        if len(p) > 1 and ("fail" in p[1:3] or "pass" in p[1:3]):
            final[p[0]] = "fail" in p[1:4]  # a later recheck line replaces the first verdict
    return {term for term, failed_ in final.items() if failed_}


def entry_text(candidate: dict[str, object]) -> str:
    entry = {
        "id": candidate["id"],
        "en": candidate["term"]["en"],  # type: ignore[index]
        "origin": candidate["origin"],
        "definition": candidate["definition"],
    }
    body = yaml.safe_dump([entry], allow_unicode=True, sort_keys=False, width=110)
    return f"# {candidate['citation']}\n{body}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("module_dir", type=Path)
    parser.add_argument("--course", default="backend-in-depth")
    args = parser.parse_args()
    glossary = REPO / "content" / args.course / "glossary.yaml"
    text = glossary.read_text(encoding="utf-8")
    present = {t["id"] for t in (yaml.safe_load(text) or {}).get("terms") or []}
    blocks: list[str] = []
    for fragment in sorted(args.module_dir.glob("*.glossary.yaml")):
        lesson = fragment.name.removesuffix(".glossary.yaml")
        dropped = failed(args.module_dir / f"{lesson}.verdicts.tsv")
        for candidate in yaml.safe_load(fragment.read_text(encoding="utf-8")) or []:
            if candidate["id"] in dropped or candidate["id"] in present:
                print(f"skip {candidate['id']}")
                continue
            blocks.append(entry_text(candidate))
            present.add(candidate["id"])
    if not blocks:
        return 0
    text = text.replace("terms: []\n", "terms:\n")
    glossary.write_text(text.rstrip("\n") + "\n\n" + "\n".join(blocks), encoding="utf-8")
    print(f"merged {len(blocks)} terms")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
