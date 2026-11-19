"""budget.py: docs/aeat-edition-plan.md (budget table) and edition/budget.json.

Prose words = words of the sentences of paragraphs and list items, excluding esquema rows, headings, fences and the
glossary. Budget of this step = 1.1 × the pre-R2d lesson's prose words (the explanation layer takes the rest, up to
1.4). Concepts = the lesson title (the programme sentence, verbatim) split at sentence ends, then at commas, colons
and « y ». Asked facts = the official questions of the coverage map, each with the article its quote cites.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lesson_model import ROOT, parse, words  # noqa: E402

AEAT = ROOT / "docs/age-verification/aeat"
EDITION = AEAT / "edition"
WORK = ROOT / "docs/_work/age-verification/aeat/edition"
FACTOR = 1.1
CITE = re.compile(r"\((arts?\.[^()]*?)\)")


def prose_words(text: str) -> int:
    return sum(words(s.text) for s in parse(text).prose_sentences)


def programme_sentences(title: str) -> list[str]:
    parts = re.split(r"(?<=[.])\s+(?=[A-ZÁÉÍÓÚ])", title.strip())
    return [p.strip() for p in parts if p.strip()]


def concepts(sentence: str) -> list[str]:
    head, _, tail = sentence.rstrip(".").partition(":")
    pieces = [head] + ([tail] if tail else [])
    out: list[str] = []
    for piece in pieces:
        out += [c.strip() for c in re.split(r",|\s+y\s+(?=el |la |los |las |un |una )", piece) if c.strip()]
    return out


def main() -> int:
    coverage = json.loads((EDITION / "coverage-a.json").read_text())
    table: dict[str, dict[str, object]] = {}
    for path in sorted((AEAT / "pool").glob("m0*.md")):
        lesson = path.stem
        pool_text = path.read_text()
        pre_text = (WORK / "pre" / path.name).read_text()
        title = pool_text.splitlines()[0].lstrip("# ").strip()
        sentences = programme_sentences(title)
        asked = {}
        for question, info in coverage.get(lesson, {}).items():
            cites = CITE.findall(str(info["quote"]))
            asked[question] = cites[0] if cites else ""
        pre = prose_words(pre_text)
        table[lesson] = {
            "title": title,
            "pre_words_total": len(pre_text.split()),
            "pre_prose": pre,
            "pool_prose": prose_words(pool_text),
            "budget": round(pre * FACTOR),
            "programme_sentences": [{"sentence": s, "concepts": concepts(s)} for s in sentences],
            "asked": asked,
        }
    (EDITION / "budget.json").write_text(json.dumps(table, ensure_ascii=False, indent=1) + "\n")
    lines = [
        "# Edition plan — step 1 (assembly from verified sentences)",
        "",
        "Pool = the R2d lessons (copied to `docs/age-verification/aeat/pool/`). Pre-R2d = the lessons at "
        "`docs/age-verification/aeat/r2d/base-commit.txt` (copied to `edition/pre/`). Prose words = paragraphs and list "
        "items, without esquema rows, headings or glossary. Budget of this step = 1.1 × pre-R2d prose; the explanation "
        "layer comes later and takes the rest up to 1.4. `Concepts` = programme sentences split at commas and colons "
        "(mechanical); `Asked` = official questions of OEP 2022–2025 whose fact the lesson must state.",
        "",
        "| Lesson | Pre-R2d prose | Budget (×1.1) | Pool prose | Programme sentences | Concepts | Asked |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    totals = [0, 0, 0, 0, 0, 0]
    for lesson, row in table.items():
        ps = row["programme_sentences"]
        n_concepts = sum(len(p["concepts"]) for p in ps)  # type: ignore[index]
        values = [row["pre_prose"], row["budget"], row["pool_prose"], len(ps), n_concepts, len(row["asked"])]  # type: ignore[arg-type]
        lines.append(f"| {lesson} | " + " | ".join(f"{v:,}" for v in values) + " |")
        totals = [t + v for t, v in zip(totals, values)]  # type: ignore[misc]
    lines.append("| **Total** | " + " | ".join(f"**{t:,}**" for t in totals) + " |")
    lines += ["", "## Concepts and asked facts per lesson", ""]
    for lesson, row in table.items():
        lines.append(f"### {lesson}")
        for p in row["programme_sentences"]:  # type: ignore[attr-defined]
            lines.append(f"- «{p['sentence']}» → " + "; ".join(p["concepts"]))
        asked = row["asked"]
        if asked:
            lines.append("- Asked: " + ", ".join(f"{q} ({c})" if c else q for q, c in asked.items()))  # type: ignore[attr-defined]
        lines.append("")
    (ROOT / "docs/aeat-edition-plan.md").write_text("\n".join(lines))
    print("\n".join(lines[:50]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
