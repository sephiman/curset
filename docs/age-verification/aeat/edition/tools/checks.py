"""checks.py: identity of kept text against the pool, coverage of the 452 questions, in the assembled lessons.

identity: every sentence and esquema row of an assembled lesson must equal (same collapsed text) a sentence or row of its
pool lesson (the verified form: R2d tags give each one's report); «Normativa» lines are derived and counted apart.
coverage: every question's quote fragments (coverage-a.json) must be found in the assembled lesson.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import coverage_map  # noqa: E402
import finalize  # noqa: E402
from lesson_model import ROOT, parse  # noqa: E402

AEAT = ROOT / "docs/age-verification/aeat"
CONTENT = ROOT / "content/aeat-agentes-hacienda/es/lessons"


def identity() -> tuple[int, int, list[str]]:
    checked = matched = 0
    bad: list[str] = []
    for path in sorted(CONTENT.glob("m0*.md")):
        lesson = path.stem
        if lesson == "m00-l01":
            continue
        text = path.read_text()
        cut = text.find("\n## Normativa")
        now = parse(text[:cut] if cut >= 0 else text)
        pool_text = (AEAT / "pool" / f"{lesson}.md").read_text()
        pool = parse(pool_text)
        pre = parse((AEAT / "edition/pre" / f"{lesson}.md").read_text())
        known = {s.text for s in pre.prose_sentences} | {s.text for s in pool.prose_sentences} | {s.text for e in pool.esquemas for s in e.sentences}
        known |= {finalize.fix_markers(t)[0] for t in known if t.startswith('|')}  # list-marker fixes of table rows
        for sentence in now.prose_sentences + [s for e in now.esquemas for s in e.sentences]:
            checked += 1
            if sentence.text in known:
                matched += 1
            else:
                bad.append(f"{lesson}:{sentence.first_line} {sentence.text[:90]}")
    return checked, matched, bad


def coverage() -> tuple[int, int, list[str]]:
    quotes = coverage_map.collect()
    total = held = 0
    missing: list[str] = []
    for lesson, by_question in sorted(quotes.items()):
        text = coverage_map.norm((CONTENT / f"{lesson}.md").read_text())
        for question, cell in by_question.items():
            total += 1
            if all(any(v in text for v in variants) for variants in coverage_map.fragments(cell)):
                held += 1
            else:
                missing.append(f"{lesson} {question}")
    return total, held, missing


def main() -> int:
    c, m, bad = identity()
    print(f"identity: checked {c}, matched {m}, not matched {len(bad)}")
    print("\n".join(bad[:40]))
    t, h, miss = coverage()
    print(f"coverage: {t} questions, {h} covered, {len(miss)} not: {', '.join(miss)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
