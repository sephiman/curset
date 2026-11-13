"""Append the FAIL rows (minus `style/overrides.tsv`, coordinator rulings) of `style/*.md` to `drops.tsv` (idempotent).

Usage: `python3 collect_style.py`.
"""

from __future__ import annotations

import re
from pathlib import Path

BANK = Path(__file__).resolve().parents[1]
ROW = re.compile(r"^\|\s*([\w-]+-q\d+)\s*\|\s*(PASS|FAIL)\s*\|\s*([^|]*)\|\s*(.*?)\s*\|\s*$")
PART = {"1": "I", "2": "II", "3": "III"}

if __name__ == "__main__":
    drops = BANK / "drops.tsv"
    present = {line.split("\t")[0] for line in drops.read_text(encoding="utf-8").splitlines()[1:]}
    overrides_path = BANK / "style" / "overrides.tsv"
    overrides = (
        {line.split("\t")[0] for line in overrides_path.read_text(encoding="utf-8").splitlines()[1:] if line}
        if overrides_path.exists() else set()
    )
    kept_rows = [line for line in drops.read_text(encoding="utf-8").splitlines(keepends=True) if line.split("\t")[0] not in overrides]
    drops.write_text("".join(kept_rows), encoding="utf-8")
    present -= overrides
    added, checked = [], 0
    for report in sorted((BANK / "style").glob("*.md")):
        for line in report.read_text(encoding="utf-8").splitlines():
            m = ROW.match(line)
            if not m:
                continue
            checked += 1
            qid, verdict, items, reason = m.groups()
            if verdict == "FAIL" and qid not in present and qid not in overrides:
                tema = f"{PART[qid[2]]}.{int(qid[5:7])}"
                added.append(f"{qid}\t{tema}\tstyle/{report.name}\t{items.strip()}\t{reason}")
                present.add(qid)
    with drops.open("a", encoding="utf-8") as handle:
        handle.writelines(row + "\n" for row in added)
    print(f"{checked} rows read, {len(added)} drops added")
