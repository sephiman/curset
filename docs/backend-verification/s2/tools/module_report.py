# SPDX-License-Identifier: AGPL-3.0-only
"""Per-lesson counts of an S2 module and its stop-gate figures, from the verdict, question and lint files.

    python module_report.py MODULE_DIR
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class LessonCounts:
    lesson: str
    sentences: int
    deleted: int
    rows: int
    written: int
    lint_fixed: int
    passed: int
    discarded: int


def verdict_lines(path: Path) -> list[list[str]]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.split("\t") for line in lines if line and not line.startswith("#")]


def lesson_counts(module_dir: Path, lesson: str, lint: dict[str, int]) -> LessonCounts:
    rows = verdict_lines(module_dir / f"{lesson}.verdicts.tsv")
    first = [r for r in rows if "recheck" not in r]
    sentences = [r for r in first if r[0].startswith(("S", "J"))]
    # a sentence is deleted when its recheck failed (second failure)
    deleted = {r[0] for r in rows if len(r) > 2 and r[0].startswith(("S", "J")) and r[1] == "recheck" and r[2] == "fail"}
    final: dict[str, str] = {}
    for r in rows:
        if f"{lesson}-q" not in r[0] or len(r) < 2:
            continue
        # a recheck line replaces the first verdict
        final[r[0]] = r[2] if r[1] == "recheck" and len(r) > 2 else r[1]
    failed_q = {qid for qid, verdict in final.items() if verdict == "fail"}
    passed_q = {qid for qid, verdict in final.items() if verdict == "pass"}
    candidates = module_dir / f"{lesson}.questions.json"
    written = len(json.loads(candidates.read_text(encoding="utf-8"))) if candidates.exists() else 0
    return LessonCounts(
        lesson=lesson,
        sentences=len(sentences),
        deleted=len(deleted),
        rows=sum(1 for r in first if r[0].startswith("R")),
        written=written,
        lint_fixed=lint.get(lesson, 0),
        passed=len(passed_q),
        discarded=len(failed_q),
    )


def lint_fixes(module_dir: Path) -> dict[str, int]:
    path = module_dir / "lint.tsv"
    totals: dict[str, int] = {}
    if not path.exists():
        return totals
    for line in path.read_text(encoding="utf-8").splitlines():
        lesson, _, count = line.partition("\t")
        if count.strip().isdigit():
            totals[lesson] = totals.get(lesson, 0) + int(count)
    return totals


def main(argv: list[str]) -> int:
    module_dir = Path(argv[1])
    lint = lint_fixes(module_dir)
    lessons = sorted({p.name.split(".")[0] for p in module_dir.glob("m*-l*.questions.json")})
    counts = [lesson_counts(module_dir, lesson, lint) for lesson in lessons]
    print("lesson\tsentences\tdeleted\trows\tq_written\tlint_fixed\tq_passed\tq_discarded")
    for c in counts:
        print(
            f"{c.lesson}\t{c.sentences}\t{c.deleted}\t{c.rows}\t{c.written}\t{c.lint_fixed}\t{c.passed}\t{c.discarded}"
        )
    verified = sum(c.passed + c.discarded for c in counts)
    sentences = sum(c.sentences for c in counts)
    pass_rate = sum(c.passed for c in counts) / verified if verified else 0.0
    deleted_share = sum(c.deleted for c in counts) / sentences if sentences else 0.0
    print(f"# gate: question pass rate {pass_rate:.0%} (stop under 60 %), deleted sentences {deleted_share:.1%} (stop over 5 %)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
