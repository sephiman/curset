"""coverage_map.py: category (a) — the sentences and esquemas every official question rests on.

Rows come from the R2 / R2-tax coverage reports; the R2d re-check and final re-check rows replace them (newest
wins). Each quote's fragments (split at «…» and at bracketed completions) are looked up in the pool lesson.
Writes edition/coverage-a.json: {lesson: {question: {"sentences": [id], "esquemas": [index], "quote": str}}} and
prints the questions whose quote is not found.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lesson_model import ROOT, parse  # noqa: E402
from scripts.provenance import _split  # noqa: E402

AEAT = ROOT / "docs/age-verification/aeat"
POOL = AEAT / "pool"
QUOTE = re.compile(r"«(.+?)»")


def norm(text: str) -> str:
    text = text.replace("\N{NO-BREAK SPACE}", " ").replace("\\|", "|").replace("\\*", "*")
    return " ".join(text.split())


def rows_of(report: Path) -> list[tuple[str, str, str]]:
    out = []
    for line in report.read_text().splitlines():
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if len(cells) < 3:
            continue
        for tag in ("m0",):
            pass
        # re-check tables start with the lesson id; the R2 / tax reports start with the question
        if cells[0].startswith("m0") and re.match(r"^\d{4}", cells[1]):
            lesson, question, rest = cells[0], cells[1], cells[2:]
        elif re.match(r"^\d{4}", cells[0]):
            lesson, question, rest = "", cells[0], cells[1:]
        else:
            continue
        verdict = next((i for i, c in enumerate(rest) if c.startswith("COVERED")), None)
        if verdict is None:
            continue
        cell = rest[verdict + 1] if verdict + 1 < len(rest) else ""
        out.append((lesson, question, cell))
    return out


def question_id(raw: str) -> str:
    return re.match(r"^(\d{4}X?-\d+)", raw).group(1)  # type: ignore[union-attr]


def collect() -> dict[str, dict[str, str]]:
    quotes: dict[str, dict[str, str]] = {}
    for path in sorted(POOL.glob("m0*.md")):
        lesson = path.stem
        for report in (AEAT / "r2/coverage" / f"{lesson}.md", AEAT / "r2-tax" / lesson / "coverage.md"):
            if report.exists():
                for _l, question, cell in rows_of(report):
                    quotes.setdefault(lesson, {})[question_id(question)] = cell
    for name in ("coverage-recheck.md", "coverage-final.md"):
        for lesson, question, cell in rows_of(AEAT / "r2d" / name):
            quotes.setdefault(lesson, {})[question_id(question)] = cell
    return quotes


def fragments(cell: str) -> list[list[str]]:
    """Each fragment with its variants (as written, and without a «a)» / «2.» marker): any variant may hit."""
    found: list[list[str]] = []
    for quote in QUOTE.findall(cell):
        for part in re.split(r"…|\[[^\]]*\]", quote):
            part = re.sub(r"^(?:[-*]\s+)?(?:\d+\.º?\)?\s+|[a-z]\)\s+)?", "", norm(part)).strip(" ,.;:()«»")
            part = re.sub(r"\s+[-–]\s+(?=[a-z0-9]+[.)]\s)", "\n", part)
            part = re.sub(r"^[|\s]+|[|\s]+$", "", part) if part.startswith("|") else part
            for piece in [p for chunk in part.split("\n") for p in _split(chunk)]:
                piece = piece.strip(" ,.;:()«»")
                piece = re.sub(r"^[-*]\s+", "", piece)
                bare = re.sub(r"^(?:\d+\.º?\)?|[a-z]\))\s+", "", piece)
                if len(bare) >= 12:
                    found.append([piece, bare])
    return found


def main() -> int:
    quotes = collect()
    result: dict[str, dict[str, dict[str, object]]] = {}
    missing: list[str] = []
    total = 0
    for lesson, by_question in sorted(quotes.items()):
        model = parse((POOL / f"{lesson}.md").read_text())
        flat = [(s, None) for s in model.prose_sentences] + [
            (s, i) for i, e in enumerate(model.esquemas) for s in e.sentences
        ]
        for question, cell in by_question.items():
            total += 1
            ids: set[str] = set()
            esq: set[int] = set()
            for variants in fragments(cell):
                hit = False
                for s, esq_index in flat:
                    if any(v in norm(s.text) for v in variants):
                        hit = True
                        if esq_index is None:
                            ids.add(s.id)
                        else:
                            esq.add(esq_index)
                if not hit:
                    missing.append(f"{lesson} {question}: {variants[0][:70]}")
            result.setdefault(lesson, {})[question] = {
                "sentences": sorted(ids),
                "esquemas": sorted(esq),
                "quote": cell,
            }
    (AEAT / "edition/coverage-a.json").write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n")
    print(f"questions {total}; fragments not found {len(missing)}")
    print("\n".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())
