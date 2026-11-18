"""coverage_check.py: is every quoted coverage passage of the official questions still verbatim in its lesson?

Rows come from the R2 / R2-tax coverage reports; a row re-checked in R2d uses its newer quote.
A quote is split at «…»; every fragment of 12+ characters must appear in the lesson (whitespace normalised).
Writes `r2d/coverage-final-input.md` with the rows that no longer match, for a blind re-check.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
AEAT = ROOT / "docs/age-verification/aeat"
LESSONS = ROOT / "content/aeat-agentes-hacienda/es/lessons"
QUOTE = re.compile(r"«(.+?)»")


def _norm(text: str) -> str:
    return " ".join(text.replace("\N{NO-BREAK SPACE}", " ").split())


def _rows(report: Path) -> list[tuple[str, str, str]]:
    rows = []
    for line in report.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not re.match(r"^\d{4}", cells[0]):
            continue
        verdicts = [i for i, c in enumerate(cells) if c.startswith("COVERED")]
        if verdicts and verdicts[0] + 1 < len(cells):
            rows.append((cells[0], cells[verdicts[0]], cells[verdicts[0] + 1]))
    return rows


def _reports(lesson: str) -> list[Path]:
    common = AEAT / "r2/coverage" / f"{lesson}.md"
    tax = AEAT / "r2-tax" / lesson / "coverage.md"
    return [p for p in (common, tax) if p.exists()]


def _rechecked() -> dict[tuple[str, str], str]:
    out = {}
    for line in (AEAT / "r2d/coverage-recheck.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[0].startswith("m0") and re.match(r"^\d{4}", cells[1]):
            out[(cells[0], cells[1])] = cells[3]
    return out


def _holds(quote_cell: str, lesson_text: str) -> bool:
    quotes = QUOTE.findall(quote_cell)
    if not quotes:
        return False
    for quote in quotes:
        for fragment in re.split(r"…", quote):
            fragment = _norm(fragment).strip(" ,.;:")
            if len(fragment) >= 12 and fragment not in lesson_text:
                return False
    return True


def main() -> int:
    rechecked = _rechecked()
    total = held = 0
    missing: list[str] = []
    for path in sorted(LESSONS.glob("m0*.md")):
        lesson = path.stem
        text = _norm(path.read_text())
        for report in _reports(lesson):
            for question, _verdict, cell in _rows(report):
                total += 1
                cell = rechecked.get((lesson, question), cell)
                if _holds(cell, text):
                    held += 1
                else:
                    missing.append(f"| {lesson} | {question} | {report.relative_to(ROOT)} |")
    (AEAT / "r2d/coverage-final-input.md").write_text(
        "# R2d final coverage re-check input\n\nCoverage rows whose quoted passage is no longer "
        "verbatim in the built lesson. For each: does the lesson still state the fact behind the official "
        "key?\n\n"
        "| lesson | question | old report |\n|---|---|---|\n" + "\n".join(missing) + "\n"
    )
    print(f"coverage rows {total}: quote holds {held}, to re-check {len(missing)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
