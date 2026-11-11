"""Split an authored draft into verifier batches of at most 60, grouped by cited unit (article or page) in order.

Run from the repo root: `python3 docs/age-verification/c2/bank/tools/verify_batches.py <draft.json> <first-batch-no>`.
Prints one line per batch: `v<k>: <first id> … <last id> (<n>)` and writes `verify/<lesson>[.<tag>].v<k>.ids` (one id per line).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BATCH = 60


def unit(citation: str) -> str:
    """Article number and norm, or the page file: neighbours sort together."""
    page = re.match(r"fuente: `([^`]+)`", citation)
    if page:
        return page.group(1)
    art = re.match(r"art\.\s*(\d+)", citation)
    norm = citation.split(" ", 2)[-1]
    return f"{norm}|{int(art.group(1)):04d}" if art else citation


def main(draft: str, first: int) -> None:
    path = Path(draft)
    stem = path.name.removesuffix(".draft.json")
    lesson = stem.split(".")[0]
    tag = stem.split(".authored", 1)[1].lstrip("-")  # «r1» for a replacement draft, empty for the first draft
    prefix = f"{lesson}.{tag}" if tag else lesson
    questions = json.loads(path.read_text(encoding="utf-8"))
    questions.sort(key=lambda q: (unit(str(q["citation"])), str(q["id"])))
    out = path.parent / "verify"
    out.mkdir(exist_ok=True)
    for k, start in enumerate(range(0, len(questions), BATCH), start=first):
        part = questions[start:start + BATCH]
        (out / f"{prefix}.v{k}.ids").write_text("\n".join(str(q["id"]) for q in part) + "\n", encoding="utf-8")
        print(f"v{k}: {part[0]['id']} … {part[-1]['id']} ({len(part)})")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
