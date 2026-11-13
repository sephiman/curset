"""Split the built bank's excerpts into «inherits» and «to blind-check», and write verifier batches of 60.

Run from the repo root: `python3 docs/age-verification/aeat/bank/tools/excerpt_prepare.py`.
A derived question inherits its origin's check only when its excerpt (heading, text, full, flag, file, or the same
«none») is byte-identical to the origin course's entry for the origin question. Everything else (authored, or derived
with a different excerpt) goes to `excerpts/batches/batch-NN.jsonl`, grouped by lesson. Writes `excerpts/inherit.tsv`.
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
BANK = ROOT / "docs" / "age-verification" / "aeat" / "bank"
COURSE = ROOT / "content" / "aeat-agentes-hacienda"
ORIGIN = {"c1": ROOT / "content/age-administrativo-c1", "c2": ROOT / "content/age-auxiliar-c2"}
FIELDS = ("heading", "text", "full", "flag")
BATCH = 60


def shape(entry: dict[str, object]) -> dict[str, object]:
    if "none" in entry:
        return {"none": entry["none"]}
    excerpt = entry["excerpt"]
    assert isinstance(excerpt, dict)
    return {**{f: excerpt.get(f) for f in FIELDS}, "file": excerpt["source"]["file"]}


def questions_by_id() -> dict[str, dict[str, object]]:
    out: dict[str, dict[str, object]] = {}
    for path in sorted((COURSE / "exercises").glob("*.yaml")):
        for q in yaml.safe_load(path.read_text(encoding="utf-8")).get("variants") or []:
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


def main() -> None:
    mine = json.loads((COURSE / "excerpts.json").read_text(encoding="utf-8"))["questions"]
    theirs = {k: json.loads((p / "excerpts.json").read_text(encoding="utf-8"))["questions"] for k, p in ORIGIN.items()}
    c1 = {**theirs["c1"], **{key.rsplit("/", 1)[-1]: v for key, v in theirs["c1"].items() if not key.startswith("sp-")}}
    origin_entries = {"c1": c1, "c2": theirs["c2"]}
    derived: dict[str, tuple[str, str]] = {}
    for path in BANK.glob("m0?-l??.kept-derived.json"):
        for q in json.loads(path.read_text(encoding="utf-8")):
            derived[str(q["id"])] = (str(q["origin"]), str(q["origin_id"]))
    inherit_rows, todo = ["id\torigin\torigin_id\tstatus"], []
    for qid in sorted(mine):
        if qid in derived:
            origin, origin_id = derived[qid]
            theirs_entry = origin_entries[origin].get(origin_id)
            same = theirs_entry is not None and shape(mine[qid]) == shape(theirs_entry)
            inherit_rows.append(f"{qid}\t{origin}\t{origin_id}\t{'identical' if same else 'differs'}")
            if same:
                continue
        todo.append(qid)
    out = BANK / "excerpts"
    (out / "batches").mkdir(parents=True, exist_ok=True)
    (out / "inherit.tsv").write_text("\n".join(inherit_rows) + "\n", encoding="utf-8")
    questions = questions_by_id()
    items = [item(n, qid, questions[qid], mine[qid]) for n, qid in enumerate(todo, start=1)]
    for old in (out / "batches").glob("batch-*.jsonl"):
        old.unlink()
    for i in range(0, len(items), BATCH):
        lines = [json.dumps(it, ensure_ascii=False) for it in items[i:i + BATCH]]
        (out / "batches" / f"batch-{1 + i // BATCH:02d}.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    derived_ok = sum(1 for r in inherit_rows[1:] if r.endswith("identical"))
    print(f"{len(mine)} excerpt entries; inherit {derived_ok}; to blind-check {len(todo)} in {-(-len(todo) // BATCH)} batches")


if __name__ == "__main__":
    main()
