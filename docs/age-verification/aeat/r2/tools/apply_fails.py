"""Apply every FAIL replacement of a verify report to its lesson: apply_fails.py <lesson id> <verify report>."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
lesson_id, report = sys.argv[1], Path(sys.argv[2])
lesson = ROOT / "content/aeat-agentes-hacienda/es/lessons" / f"{lesson_id}.md"
pending = ROOT / "docs/age-verification/aeat/r2/pending" / f"{lesson_id}.md"


def cells(row: str) -> list[str]:
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", row.strip().strip("|"))]


texts = {cells(r)[0].strip("`"): cells(r)[2] for r in pending.read_text().splitlines() if r.startswith("| `")}
text = lesson.read_text()
for row in report.read_text().splitlines():
    if not row.startswith("| `"):
        continue
    c = cells(row)
    if c[1] != "FAIL":
        continue
    old, new = texts[c[0].strip("`")], c[-1]
    new = new.removeprefix("- ")  # the pending text of a list item carries no marker; the lesson keeps its own
    pattern = r"\s+".join(re.escape(t) for t in old.split())
    found = list(re.finditer(pattern, text))
    if len(found) != 1:
        print(f"{c[0]}: {len(found)} matches, not applied")
        continue
    start, end = found[0].start(), found[0].end()
    if new.strip().lower() == "drop" or new.strip().lower().startswith(("(delete", "delete", "(drop")):
        line_start = text.rfind("\n", 0, start) + 1
        item_end = end
        while text.startswith("\n  ", item_end):  # wrapped continuation lines of the same item
            item_end = text.index("\n", item_end + 1) if "\n" in text[item_end + 1 :] else len(text)
        if text[line_start:start].strip() == "-" and text[end:item_end].strip() == "":
            start, end = line_start, item_end + 1  # the whole list item, with its newline
        else:
            end += 1 if text[end : end + 1] == " " else 0
        new = ""
    text = text[:start] + new + text[end:]
    print(f"{c[0]}: applied")
lesson.write_text(text)
