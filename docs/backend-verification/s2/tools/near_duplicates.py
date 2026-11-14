# SPDX-License-Identifier: AGPL-3.0-only
"""Cross-lesson near-duplicate scan of kept questions: pairs whose stem+key word sets overlap heavily.

    python near_duplicates.py MODULE_DIR [MODULE_DIR ...] [--threshold 0.6]
"""

from __future__ import annotations

import argparse
import json
import re
from itertools import combinations
from pathlib import Path

STOP = frozenset(
    "a an the of to in on for and or is are be by with which what when does do that this it its as at from "
    "following statement correct true java".split()
)


def words(text: str) -> frozenset[str]:
    return frozenset(w for w in re.findall(r"[a-z0-9_]+", text.lower()) if w not in STOP and len(w) > 2)


def failed(verdicts: Path) -> set[str]:
    final: dict[str, str] = {}
    if verdicts.is_file():
        for line in verdicts.read_text(encoding="utf-8").splitlines():
            row = line.split("\t")
            verdict = row[2] if len(row) > 2 and row[1] == "recheck" else row[1] if len(row) > 1 else ""
            if verdict in ("pass", "fail"):
                final[row[0]] = verdict
    return {qid for qid, verdict in final.items() if verdict == "fail"}


def kept(folder: Path) -> list[tuple[str, frozenset[str], str]]:
    found = []
    for path in sorted(folder.glob("*.questions.json")):
        dropped = failed(path.with_name(path.name.replace(".questions.json", ".verdicts.tsv")))
        for q in json.loads(path.read_text(encoding="utf-8")):
            if q["id"] not in dropped:
                found.append((q["id"], words(q["stem"] + " " + q["key"]), " ".join(q["key"].split()).lower()))
    return found


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folders", nargs="+", type=Path)
    parser.add_argument("--threshold", type=float, default=0.6)
    args = parser.parse_args()
    questions = [q for folder in args.folders for q in kept(folder)]
    pairs = 0
    for (left, lw, lk), (right, rw, rk) in combinations(questions, 2):
        overlap = len(lw & rw) / max(1, len(lw | rw))
        if overlap >= args.threshold or (lk and lk == rk):
            pairs += 1
            print(f"{left}\t{right}\t{overlap:.2f}\t{'same key' if lk == rk else ''}")
    print(f"# {len(questions)} questions, {pairs} candidate pairs at >= {args.threshold}")


if __name__ == "__main__":
    main()
