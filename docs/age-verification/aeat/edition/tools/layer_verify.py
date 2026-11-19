"""layer_verify.py <lesson…>: the blind verifier's input for the cases (and purpose sentences) of a lesson's layer.

Each CASO/PARA with the text of the articles it cites; the lesson itself is not shown. Writes explanation/<lesson>/verify-input.md.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys

from article_text import article, cited_units
from layer import parse
from explanation import LAYER
from normativa import COURSE


def preambulos(lesson: str, text: str) -> list[str]:
    from normativa import load_index
    from tradeschool.citations.lesson import scan_lesson

    index, _ = load_index()
    out: list[str] = []
    for item in scan_lesson(lesson, text, index).prose:
        if item.norm is None or not item.norm.file:
            continue
        pages = subprocess.run(["pdftotext", "-layout", str(COURSE / item.norm.file), "-"], capture_output=True, text=True, check=False).stdout
        heads = list(re.finditer(r"^\s*(?:PRE[ÁA]MBULO|EXPOSICI[ÓO]N DE MOTIVOS|Pre[áa]mbulo|Exposici[óo]n de motivos)\s*$", pages, re.M))
        ends = [m.start() for m in re.finditer(r"^\s*(?:Art[ií]culo 1\.|T[ÍI]TULO PRELIMINAR|T[ÍI]TULO I\b|CAP[ÍI]TULO I\b)", pages, re.M)]
        heads += list(re.finditer(r"^\s{10,}I\s*$", pages, re.M))
        spans = [(h.start(), next((e for e in ends if e > h.start() + 500), len(pages))) for h in heads]
        start, end = max(spans, key=lambda span: span[1] - span[0], default=(0, 60000))
        out += [f"### Preámbulo / exposición de motivos de {item.norm.short} (text before the first article)", "", pages[start:end][:90000], ""]
        break
    return out


def build(lesson: str) -> str:
    out = [f"# Verifier input — `{lesson}`", ""]
    only = None
    if os.environ.get("RECHECK"):
        path = LAYER / lesson / "recheck-keys.txt"
        only = set(path.read_text(encoding="utf-8").split("\n")) if path.exists() else set()
    second = bool(os.environ.get("SECOND"))
    dropped_path = LAYER / lesson / "dropped.txt"
    dropped = set(dropped_path.read_text(encoding="utf-8").split("\n")) if dropped_path.exists() else set()
    for part in parse(lesson)[0]:
        if part.kind == "pq" or (only is not None and part.key not in only):
            continue
        if second and (part.kind != "caso" or part.key in dropped):
            continue
        out += [f"## KEY: {part.key}", "", f"{part.kind.upper()}: {part.text}", ""]
        for norm, number, pdf in cited_units(lesson, part.text):
            out += [f"### {norm}, artículo {number}", "", article(pdf, number), ""]
        if part.kind == "para":
            out += preambulos(lesson, part.text)
    path = LAYER / lesson / ("layer-verify2-input.md" if second else "layer-verify-input.md")
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return str(path)


if __name__ == "__main__":
    for name in sys.argv[1:]:
        print(build(name))
