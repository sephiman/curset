"""article_text.py <lesson> : the text of every article a lesson's explanation layer cites, from the consolidated PDFs.

Prints, per norm and article, the PDF text between «Artículo N.» and the next «Artículo». Disposiciones and annexes are
cut from their heading to the next one. Used to feed the blind verifiers; the lesson's own sentences are never shown.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from functools import cache
from pathlib import Path

from normativa import COURSE, load_index

UNIT_HEADING = {
    "art": lambda n: rf"^\s*Art[ií]culo\s+{re.escape(n)}\.?(?:\s|$)",
}


@cache
def source_index() -> dict[str, dict[str, object]]:
    return json.loads((COURSE / "source-index.json").read_text())["files"]


@cache
def page_text(pdf: str, page: int) -> str:
    out = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(COURSE / pdf), "-"],
                         capture_output=True, text=True, check=False)
    return out.stdout


def article(pdf: str, number: str) -> str:
    units = source_index()[pdf]["units"]
    unit = "art-" + re.sub(r"\s+", "-", number)
    if unit not in units:
        return f"[no se encuentra el artículo {number} en el índice de la fuente]"
    start = int(units[unit])
    text = "".join(page_text(pdf, p) for p in range(start, start + 4))
    heading = re.search(UNIT_HEADING["art"](number), text, re.M)
    if not heading:
        return f"[encabezado del artículo {number} no localizado en la página {start}]"
    body = text[heading.start():]
    nxt = re.search(r"^\s*Art[ií]culo\s+\d+[\w ]*\.", body[10:], re.M)
    clean = body[: nxt.start() + 10] if nxt else body
    return re.sub(r"[ \t]+", " ", clean).strip()


def cited_units(lesson: str, text: str) -> list[tuple[str, str, str]]:
    from tradeschool.citations.lesson import scan_lesson

    index, _ = load_index()
    found = scan_lesson(lesson, text, index)
    seen: dict[tuple[str, str], str] = {}
    for item in found.items:
        if item.section == "normativa":
            continue
        for group in (item, *item.also):
            if group.norm is None or not group.norm.file:
                continue
            for unit in group.units:
                if unit.kind == "art":
                    seen.setdefault((group.norm.short, unit.number), group.norm.file)
    return [(norm, number, pdf) for (norm, number), pdf in seen.items()]


if __name__ == "__main__":
    lesson = sys.argv[1]
    body = (COURSE / "es" / "lessons" / f"{lesson}.md").read_text()
    for norm, number, pdf in cited_units(lesson, body):
        print(f"## {norm}, artículo {number}\n{article(pdf, number)}\n")
