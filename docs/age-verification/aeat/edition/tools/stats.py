"""stats.py: per-lesson table for the handoff (sections, Preguntas, cases written / first check / kept, PARA, Término, words, ratio)."""

from __future__ import annotations

import json
import re
from explanation import LAYER, LESSONS, HEADING
from fails import ROW
from layer import parse
from budget import prose_words

PILOT = {"m03-l09", "m03-l13", "m02-l03"}


def first_check(lesson: str) -> dict[str, str]:
    first: dict[str, str] = {}
    files = sorted((LAYER / lesson).glob("layer-verifier-[0-9].md"), key=lambda p: p.stem)
    if lesson in PILOT:
        files = [f for f in files if f.stem.endswith("2")] or files
    for path in files:
        for line in path.read_text(encoding="utf-8").splitlines():
            m = ROW.match(line)
            if m and m["key"].strip().lower() != "key":
                first.setdefault(m["key"].strip(), m["verdict"])
    return first


def main() -> None:
    budget = json.load(open(LAYER / "budget-v2.json"))
    pre = json.load(open(LAYER.parent / "budget.json"))
    rows = []
    for lesson in sorted(budget):
        text = (LESSONS / f"{lesson}.md").read_text(encoding="utf-8")
        lines = text.split("\n")
        sections = sum(1 for l in lines if HEADING.match(l))
        pq = sum(1 for l in lines if l.startswith("**Preguntas que responde:**"))
        kept = sum(1 for l in lines if l.startswith("**Caso.**"))
        para = sum(1 for l in lines if l.startswith("**Para qué sirve.**"))
        term = sum(1 for l in lines if l.startswith("**Término"))
        parts = parse(lesson)[0]
        cases = [p.key for p in parts if p.kind == "caso"]
        fc = first_check(lesson)
        passed = sum(1 for k in cases if fc.get(k) == "PASS")
        words = prose_words(text)
        base = pre[lesson]["pre_prose"]
        rows.append((lesson, sections, pq, len(cases), passed, kept, para, term, words, base, round(words / base, 2), budget[lesson]["cap"]))
    print("| lesson | sections | Preguntas | cases written | first check PASS | kept | Para | Término | words | pre-R2d | ratio | cap |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for r in rows:
        print("| " + " | ".join(str(x) for x in r) + " |")
    tot = [sum(r[i] for r in rows) for i in (1, 2, 3, 4, 5, 6, 7, 8, 9)]
    print("| total | " + " | ".join(str(x) for x in tot[:7]) + f" | {tot[7]} | {tot[8]} | {round(tot[7] / tot[8], 2)} | |")


main()
