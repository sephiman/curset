"""Write the blind excerpt-check batches for the case questions: one JSON object per line, 60 per batch.

Run from the repo root after build_cases.py and extract_excerpts.py:
`python3 docs/age-verification/cases/tools/excerpt_batches.py [sp-01 …]`. Reads the built `exercises/sp-*.yaml` and
`excerpts.json`; writes `docs/age-verification/cases/excerpts/batch-NN.jsonl` in the fields of
docs/age-verification/excerpts/verifier-spec.md, plus the scenario so the checker sees the question as a learner does.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
COURSE = ROOT / "content" / "age-administrativo-c1"
OUT = ROOT / "docs" / "age-verification" / "cases" / "excerpts"
BATCH = 60


def main() -> None:
    excerpts = json.loads((COURSE / "excerpts.json").read_text(encoding="utf-8"))["questions"]
    items = []
    only = set(sys.argv[1:])  # case ids to batch; all built cases when none given
    for path in sorted((COURSE / "exercises").glob("sp-*.yaml")):
        if only and path.stem not in only:
            continue
        case = yaml.safe_load(path.read_text(encoding="utf-8"))
        for q in case["questions"]:
            key = f"{path.stem}/{q['id']}"
            entry = excerpts[key]
            excerpt = entry.get("excerpt") or {}
            items.append({
                "n": len(items) + 1,
                "key": key,
                "scenario": case["scenario"]["es"],
                "prompt": q["prompt"]["es"],
                "options": [{"id": o["id"], "text": o["text"]["es"], "correct": bool(o.get("correct"))}
                            for o in q["options"]],
                "explanation": q["explanation"]["es"],
                "citation": q["citation"],
                "excerpt_heading": excerpt.get("heading"),
                "excerpt_text": excerpt.get("text"),
                "excerpt_full": excerpt.get("full"),
                "none": entry.get("none"),
            })
    OUT.mkdir(exist_ok=True)
    for start in range(0, len(items), BATCH):
        lines = [json.dumps(i, ensure_ascii=False) for i in items[start:start + BATCH]]
        (OUT / f"batch-{start // BATCH + 1:02d}.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(items)} case questions in {-(-len(items) // BATCH)} batches; "
          f"{sum(1 for i in items if i['none'])} without excerpt")


if __name__ == "__main__":
    main()
