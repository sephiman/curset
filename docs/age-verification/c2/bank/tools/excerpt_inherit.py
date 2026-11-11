"""Which derived questions may inherit C1's excerpt check: their excerpt (heading, text, full, file, flag) is byte-identical to C1's.

Run from the repo root: `python3 docs/age-verification/c2/bank/tools/excerpt_inherit.py bloque-ii`. Prints the counts and
writes `excerpts/<bloque>-inherit.tsv` (`id c1_id status`), status `identical` or what differs.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
BANK = ROOT / "docs" / "age-verification" / "c2" / "bank"
FIELDS = ("heading", "text", "full", "flag")


def entry_shape(entry: dict[str, object]) -> dict[str, object]:
    if "none" in entry:
        return {"none": entry["none"]}
    excerpt = entry["excerpt"]
    assert isinstance(excerpt, dict)
    return {**{f: excerpt.get(f) for f in FIELDS}, "file": excerpt["source"]["file"]}


def main(bloque: str) -> None:
    c1 = json.loads((ROOT / "content/age-administrativo-c1/excerpts.json").read_text(encoding="utf-8"))["questions"]
    c2 = json.loads((ROOT / "content/age-auxiliar-c2/excerpts.json").read_text(encoding="utf-8"))["questions"]
    c1_by_id = {**c1, **{key.rsplit("/", 1)[-1]: value for key, value in c1.items() if not key.startswith("sp-")}}
    rows: list[str] = []
    for path in sorted((BANK / bloque).glob("*.kept-derived.json")):
        for q in json.loads(path.read_text(encoding="utf-8")):
            if q["id"] not in c2:
                continue  # held or dropped: not built
            mine, theirs = entry_shape(c2[q["id"]]), c1_by_id.get(q["c1_id"])
            if theirs is None:
                status = "C1 has no entry"
            else:
                diff = [k for k, v in mine.items() if entry_shape(theirs).get(k) != v]
                status = "identical" if not diff and mine.keys() == entry_shape(theirs).keys() else "differs: " + ",".join(diff or ["kind"])
            rows.append(f"{q['id']}\t{q['c1_id']}\t{status}")
    out = BANK / "excerpts" / f"{bloque}-inherit.tsv"
    out.write_text("id\tc1_id\tstatus\n" + "\n".join(rows) + "\n", encoding="utf-8")
    counts: dict[str, int] = {}
    for row in rows:
        status = row.split("\t")[2]
        counts[status] = counts.get(status, 0) + 1
    print(f"{len(rows)} derived questions built")
    for status, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {n:5d}  {status}")


if __name__ == "__main__":
    main(sys.argv[1])
