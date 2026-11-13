"""The AEAT checklist items a script decides (style guide § 12: 3, 4, 5, 10 lengths, 2 acronyms), per question.

Usage: `python3 mechanical_style.py <json> …` → counts per item; `--tsv` prints id, item, detail per failure.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ARTICLE_OPTION = re.compile(r"^(el |la )?(art(ículo|\.)|apartado|letra|disposición)\s", re.I)
COMBINED = re.compile(r"^(ninguna de las|todas (las anteriores|son correctas|ellas son)|[abcd]\) y [abcd]\)|las respuestas [abcd])", re.I)
LOWER_NEGATIVE = re.compile(r"(cuál|qué|señale|indique)[^.?:]*\b(no (es|son|está|forma|corresponde|puede|se)|incorrecta|falsa)\b", re.I)
CAPS_NEGATIVE = re.compile(r"\b(NO|INCORRECTA|FALSA)\b")
# Short names of norms: 2025 stems print the full BOE title (§ 2). The explanation and citation may use them.
ACRONYM = re.compile(r"\b(LGT|RGAT|RGR|RGSVR|LIRPF|RIRPF|LIVA|RIVA|LIS|RIS|LPAC|LRJSP|LOPJ|LOTC|LOREG|EBEP|TREBEP|LRBRL|CAU|TRLRHL|LGP|LOFCA|LCSP|LTBG|LOPDGDD|RGPD|CE|TFUE|TUE|LEC|LJCA|LOEPSF|RGIT)\b")
OPTION_WORDS = (5, 30)
STATEMENT_MAX = 60


def words(text: str) -> int:
    return len(text.split())


def failures(q: dict[str, object]) -> list[tuple[str, str]]:
    prompt = str(q["prompt"]).strip()
    options = [str(o).strip() for o in q["options"].values()]  # type: ignore[union-attr]
    out: list[tuple[str, str]] = []
    if not (prompt.endswith(":") or prompt.endswith("?")):
        out.append(("2", "stem ends neither in «:» nor «?»"))
    if ACRONYM.search(prompt):
        out.append(("2", f"short norm name in the stem: {ACRONYM.search(prompt).group(0)}"))  # type: ignore[union-attr]
    if any(ARTICLE_OPTION.match(o) or COMBINED.match(o) for o in options):
        out.append(("4", "article-number, «ninguna/todas» or combined option"))
    if LOWER_NEGATIVE.search(prompt) and not CAPS_NEGATIVE.search(prompt):
        out.append(("5", "negative stem without capitals"))
    if re.search(r"\b[Dd]e el\b|\b[Aa] el\b", prompt):
        out.append(("8", "«de el»/«a el» instead of «del»/«al»"))
    n = words(prompt)
    longest_ok = 110 if str(q.get("stem_form")) == "supuesto" else 60
    if not 20 <= n <= longest_ok:
        out.append(("10", f"stem {n} words (20–{longest_ok})"))
    if any(words(o) > STATEMENT_MAX for o in options):
        out.append(("10", f"option over {STATEMENT_MAX} words"))
    elif sorted(words(o) for o in options)[2] < OPTION_WORDS[0]:
        out.append(("10", "options too short (median under 5 words)"))
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
