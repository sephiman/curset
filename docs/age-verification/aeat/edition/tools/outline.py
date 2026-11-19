"""outline.py <lesson…>: edition/outline/<lesson>.txt — the compact view the concept readers work from.

One line per prose sentence outside esquemas: `id origin words | first 18 words`; headings as section lines;
esquemas as one line with title, kind, rows and the articles their rows cite. Origin letters: H pre-R2d text,
C R2b restore / review item, N «No confundir», G gap fill, K range coverage, W reworded; `A` is added when an
official question rests on the sentence.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lesson_model import ROOT, parse, words  # noqa: E402

AEAT = ROOT / "docs/age-verification/aeat"
EDITION = AEAT / "edition"
LETTER = {
    "HEAD": "H",
    "R2b restore": "C",
    "review item": "C",
    "No confundir": "N",
    "gap fill": "G",
    "range coverage": "K",
    "reworded": "W",
}


def origins(lesson: str) -> dict[str, str]:
    path = AEAT / "r2d/tags" / f"{lesson}.json"
    return {row["id"]: row["origin"] for row in json.loads(path.read_text())}


def covered(lesson: str) -> set[str]:
    data = json.loads((EDITION / "coverage-a.json").read_text()).get(lesson, {})
    return {i for info in data.values() for i in info["sentences"]}


def header(lesson: str) -> str:
    import select_lesson

    info = json.loads((EDITION / "budget.json").read_text())[lesson]
    sel = select_lesson.Selection(lesson, int(info["budget"]))
    sel.picks = []
    sel.run()
    forced = {}
    for b, s in sel.all:
        label = sel.cls.get(select_lesson.key(s))
        if label in ("a", "c", "d", "lead-in", "note"):
            forced[label] = forced.get(label, 0) + words(s.text)
    total = sum(forced.values())
    lines = [f"BUDGET {info['budget']} words of prose; already kept by rule: {forced} = {total}; headroom {int(info['budget']) - total}"]
    for p in info["programme_sentences"]:
        lines.append(f"PROGRAMME «{p['sentence']}» concepts: " + "; ".join(p["concepts"]))
    return "\n".join(lines) + "\n"


def build(lesson: str) -> str:
    model = parse((AEAT / "pool" / f"{lesson}.md").read_text())
    tag = origins(lesson)
    asked = covered(lesson)
    events: list[tuple[int, str]] = []
    for s in model.sections:
        events.append((s.line, f"{'#' * s.level} {s.title}"))
    for b in model.blocks:
        for s in b.sentences:
            letter = LETTER.get(tag.get(s.id, ""), "W") + ("A" if s.id in asked else "")
            head = " ".join(s.text.split()[:18])
            events.append((s.first_line, f"{s.id} {letter} {words(s.text)} | {head}"))
    for i, e in enumerate(model.esquemas):
        rows = len(e.sentences)
        flag = "A" if i in {x for info in json.loads((EDITION / "coverage-a.json").read_text()).get(lesson, {}).values() for x in info["esquemas"]} else ""
        events.append((e.first, f"[esquema {i}{flag}] {e.kind} «{e.title}» {rows} rows"))
    events.sort(key=lambda x: x[0])
    return header(lesson) + "\n".join(text for _, text in events) + "\n"


def main(argv: list[str]) -> int:
    out = EDITION / "outline"
    out.mkdir(exist_ok=True)
    lessons = argv or sorted(p.stem for p in (AEAT / "pool").glob("m0*.md") if p.stem != "m00-l01")
    for lesson in lessons:
        text = build(lesson)
        (out / f"{lesson}.txt").write_text(text)
        print(lesson, len(text.splitlines()), "lines", len(text.split()), "tokens-ish")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
