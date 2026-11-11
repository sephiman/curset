"""cites.py <lesson…>: a tax lesson's citations the parser cannot resolve (unknown norm name, or no unit read)."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "backend"))

from tests.pipeline_courses import pipeline_courses  # noqa: E402

course = next(c for c in pipeline_courses() if c.slug == "aeat-agentes-hacienda")
for lesson_id in sys.argv[1:]:
    citations = course.citations.lesson(lesson_id, "es")
    if citations is None:
        print(f"{lesson_id}: no citations loaded")
        continue
    bad = [
        c
        for c in citations.items
        if c.section != "normativa" and c.source_file is None and (c.norm is None or not c.units)
    ]
    print(f"{lesson_id}: {len(citations.items)} citations, {len(bad)} unresolved")
    for c in bad:
        why = "unknown norm" if c.norm is None else "no unit"
        print(f"  l.{c.line} [{c.section}] {why}: {c.text}")
