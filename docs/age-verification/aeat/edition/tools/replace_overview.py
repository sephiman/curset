"""replace_overview.py <lesson…>: after draft.md's OVERVIEW changed, swap the old overview paragraph of the lesson for the new one."""

from __future__ import annotations

import re
import sys

from explanation import LAYER, LESSONS


def run(lesson: str) -> int:
    draft = (LAYER / lesson / "draft.md").read_text(encoding="utf-8")
    match = re.search(r"=== OVERVIEW\n(.*?)(?=\n=== |\Z)", draft, re.S)
    if not match:
        return 0
    overview = re.sub(r"\s+", " ", match.group(1)).strip()
    lines = (LESSONS / f"{lesson}.md").read_text(encoding="utf-8").split("\n")
    end = next(i for i, line in enumerate(lines) if line.startswith("## "))
    out: list[str] = []
    removed = 0
    i = 0
    while i < len(lines):
        if 0 < i < end and lines[i].strip():
            j = i
            while j < len(lines) and lines[j].strip():
                j += 1
            para = re.sub(r"\s+", " ", " ".join(lines[i:j])).strip()
            if "Lo que más cae" in para and para != overview:
                removed += 1
                i = j + 1
                continue
            out += lines[i:j]
            i = j
            continue
        out.append(lines[i])
        i += 1
    if removed:
        (LESSONS / f"{lesson}.md").write_text("\n".join(out), encoding="utf-8")
    return removed


if __name__ == "__main__":
    for name in sys.argv[1:]:
        print(name, run(name))
