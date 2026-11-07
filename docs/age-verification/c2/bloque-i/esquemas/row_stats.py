# SPDX-License-Identifier: AGPL-3.0-only
"""Per C2 bloque I lesson: esquemas, and their rows inherited from C1 or verified here (from the provenance records)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO / "backend"))
sys.path.insert(0, str(REPO / "backend" / "src"))

from scripts.provenance import parse_record, sentences  # noqa: E402
from tradeschool.content.esquema import esquema_lines, parse_esquemas  # noqa: E402

LESSONS = REPO / "content" / "age-auxiliar-c2" / "es" / "lessons"
RECORDS = REPO / "docs" / "age-verification" / "c2" / "bloque-i"

print("| Lesson | Esquemas | Rows | Inherited from C1 | Verified here |")
print("|---|---|---|---|---|")
for n in range(1, 17):
    lesson = f"m01-l{n:02d}"
    markdown = (LESSONS / f"{lesson}.md").read_text(encoding="utf-8")
    esquemas = parse_esquemas(markdown)
    lines = esquema_lines(esquemas)
    inherited_ids = {r.sentence_id for r in parse_record((RECORDS / f"{lesson}.md").read_text(encoding="utf-8")) if r.inherited}
    rows = {s.id for s in sentences(markdown) if s.first_line in lines}
    inherited = len(rows & inherited_ids)
    print(f"| {lesson} | {len(esquemas)} | {len(rows)} | {inherited} | {len(rows) - inherited} |")
