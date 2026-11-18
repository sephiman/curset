"""rdl29_convalidated.py <lesson…>: drop the RDL 29/2026 pending marks (convalidated 12-11-2026)."""

from __future__ import annotations

import datetime
import re
import sys
from pathlib import Path

LESSONS = Path(__file__).resolve().parents[5] / "content/aeat-agentes-hacienda/es/lessons"
TODAY = datetime.date(2026, 11, 14)
RDL = "Real Decreto-ley 29/2026"
CONVALIDATED = "convalidado el 12-11-2026 (BOE-A-2026-23755)"
INLINE = [
    (f"redacción del {RDL}, convalidación pendiente", f"redacción del {RDL}"),
    (f", {RDL}, convalidación pendiente)", f", {RDL})"),
    (f"convalidación pendiente del {RDL}", RDL),
]
PENDING = re.compile(
    rf"Cambio pendiente por el {RDL}(, de 6 de octubre)?, sin convalidar, "
    rf"con efectos desde el (\d\d)-(\d\d)-(\d{{4}})"
)


def _pending(match: re.Match[str]) -> str:
    day, month, year = int(match[2]), int(match[3]), int(match[4])
    date = f"{match[2]}-{match[3]}-{match[4]}"
    if datetime.date(year, month, day) <= TODAY:
        return f"Redacción del {RDL}, de 6 de octubre, {CONVALIDATED}, en vigor desde el {date}"
    return f"Cambio pendiente por el {RDL}, de 6 de octubre, {CONVALIDATED}, con efectos desde el {date}"


def convert(text: str) -> str:
    for old, new in INLINE:
        text = text.replace(old, new)
    return PENDING.sub(_pending, text)


if __name__ == "__main__":
    for lesson in sys.argv[1:]:
        path = LESSONS / f"{lesson}.md"
        before = path.read_text()
        after = convert(before)
        path.write_text(after)
        left = [
            line
            for line in after.splitlines()
            if RDL in line
            and ("pendiente de conv" in line or "sin convalidar" in line or "convalidación pendiente" in line)
        ]
        print(f"{lesson}: changed {before != after}; RDL 29/2026 marks left: {len(left)}")
        for line in left:
            print("   ", line[:200])
