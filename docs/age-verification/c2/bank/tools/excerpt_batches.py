"""Write blind excerpt-check batches for C2 questions: one JSON object per line, up to 60 per batch.

Run from the repo root: `python3 docs/age-verification/c2/bank/tools/excerpt_batches.py <ids.txt> <out-dir> [start-batch]`.
Reads the built `exercises/*.yaml` and `excerpts.json`; fields as in docs/age-verification/excerpts/verifier-spec.md, plus
`none` (the build's reason when no excerpt was found) and `flag`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
COURSE = ROOT / "content" / "age-auxiliar-c2"
BATCH = 60


def questions_by_id() -> dict[str, dict[str, object]]:
    out: dict[str, dict[str, object]] = {}
    for path in sorted((COURSE / "exercises").glob("*.yaml")):
        exercise = yaml.safe_load(path.read_text(encoding="utf-8"))
        for q in exercise.get("variants") or []:
            out[q["id"]] = q
    return out


def item(n: int, qid: str, q: dict[str, object], entry: dict[str, object]) -> dict[str, object]:
    excerpt = entry.get("excerpt") or {}
    options = q["options"]
    assert isinstance(options, list) and isinstance(excerpt, dict)
    return {
        "n": n,
        "key": qid,
        "prompt": q["prompt"]["es"],  # type: ignore[index]
        "options": [{"id": o["id"], "text": o["text"]["es"], "correct": bool(o.get("correct"))} for o in options],
        "explanation": q["explanation"]["es"],  # type: ignore[index]
        "citation": q["citation"],
        "excerpt_heading": excerpt.get("heading"),
        "excerpt_text": excerpt.get("text"),
        "excerpt_full": excerpt.get("full"),
        "flag": excerpt.get("flag"),
        "none": entry.get("none"),
        "source_file": (excerpt.get("source") or entry.get("source") or {}).get("file"),
    }


def main(ids_file: str, out_dir: str, start: int = 1) -> None:
    ids = [line.strip() for line in Path(ids_file).read_text(encoding="utf-8").splitlines() if line.strip()]
    excerpts = json.loads((COURSE / "excerpts.json").read_text(encoding="utf-8"))["questions"]
    questions = questions_by_id()
    items = [item(n, qid, questions[qid], excerpts[qid]) for n, qid in enumerate(ids, start=1)]
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for i in range(0, len(items), BATCH):
        lines = [json.dumps(it, ensure_ascii=False) for it in items[i:i + BATCH]]
        (out / f"batch-{start + i // BATCH:02d}.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(items)} items in {-(-len(items) // BATCH)} batches from batch-{start:02d}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], *(int(a) for a in sys.argv[3:4]))
