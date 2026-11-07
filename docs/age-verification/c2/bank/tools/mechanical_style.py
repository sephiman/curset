"""The C2 checklist items a script decides (style guide § 12: 2, 3, 6 capitals, 14, 21), per question.

Item 6 here flags candidates only; the model check rules on them (a «no» inside a premise is not a negative stem).

Usage: `python3 mechanical_style.py <json> …` → prints counts per item; `--tsv` prints id, item, detail per failure.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ARTICLE_OPTION = re.compile(r"^(el |la )?(art(ículo|\.)|apartado|letra|disposición)\s", re.I)
COMBINED = re.compile(r"^(ninguna de las|todas (las anteriores|son correctas|ellas son)|[abcd]\) y [abcd]\)|las respuestas [abcd])", re.I)
# A stem that asks for the one option that is not: «¿cuál … no es …?», «señale la incorrecta».
LOWER_NEGATIVE = re.compile(r"(cuál|qué|señale|indique)[^.?:]*\b(no (es|son|está|forma|corresponde|puede|se)|incorrecta|falsa)\b", re.I)
CAPS_NEGATIVE = re.compile(r"\b(NO|INCORRECTA|FALSA)\b")
PATH_OR_FORMULA = re.compile(r"[>›»]|=[A-ZÁÉÍÓÚ.]+\(|\bseleccionar\b|\bhacer clic\b|\bpestaña\b", re.I)


def words(text: str) -> int:
    return len(text.split())


def failures(q: dict[str, object]) -> list[tuple[str, str]]:
    tema = str(q["tema"])
    ofimatica = tema.startswith("II.") and int(tema.split(".")[1]) >= 5
    early_ii = tema.startswith("II.") and not ofimatica
    prompt = str(q["prompt"]).strip()
    options = [str(o).strip() for o in q["options"].values()]  # type: ignore[union-attr]
    out: list[tuple[str, str]] = []
    if not (prompt.endswith(":") or prompt.endswith("?")):
        out.append(("2", "stem ends neither in «:» nor «?»"))
    if any(ARTICLE_OPTION.match(o) or COMBINED.match(o) for o in options):
        out.append(("3", "article-number, «ninguna/todas» or combined option"))
    if LOWER_NEGATIVE.search(prompt) and not CAPS_NEGATIVE.search(prompt):
        out.append(("6", "negative stem without capitals"))
    n = words(prompt)
    if ofimatica:
        cap = 50 if PATH_OR_FORMULA.search(prompt) else 35
        if not 15 <= n <= cap:
            out.append(("21", f"stem {n} words (15–{cap})"))
        if any(words(o) > 20 for o in options):
            out.append(("21", "option over 20 words"))
    else:
        cap = 55 if early_ii else 40
        if not 20 <= n <= cap:
            out.append(("14", f"stem {n} words (20–{cap})"))
        if any(words(o) > 40 for o in options):
            out.append(("14", "option over 40 words"))
    return out


if __name__ == "__main__":
    tsv = "--tsv" in sys.argv
    counts: Counter[str] = Counter()
    total = 0
    for name in [a for a in sys.argv[1:] if a != "--tsv"]:
        for q in json.loads(Path(name).read_text(encoding="utf-8")):
            total += 1
            found = failures(q)
            for item, detail in found:
                counts[item] += 1
                if tsv:
                    print(f"{q['id']}\t{item}\t{detail}")
            counts["any"] += bool(found)
    if not tsv:
        print(f"{total} questions; failing: {dict(counts)}")
