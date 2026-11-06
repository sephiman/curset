"""C1 glossary entries that C2's bloque I can copy under R2.3: term used in a C2 lesson, cited files identical."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "backend"))
from scripts.provenance import GlossaryEntry  # noqa: E402
from tests.pipeline_courses import course_dir, pipeline_courses  # noqa: E402
from tradeschool.content.yaml_file import read_yaml  # noqa: E402

courses = {c.slug: c for c in pipeline_courses()}
c1, c2 = courses["age-administrativo-c1"], courses["age-auxiliar-c2"]
r1, r2 = course_dir(c1), course_dir(c2)
lessons = {p.stem: p.read_text().lower() for p in sorted((r2 / "es/lessons").glob("m01-l*.md"))}
terms = read_yaml(r1 / "glossary.yaml")["terms"]  # type: ignore[index]
for raw in terms:
    if raw.get("alias_of"):
        continue
    term = str(raw["es"]).lower()
    pattern = re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)")
    using = [lid for lid, text in lessons.items() if pattern.search(text)]
    if not using:
        continue
    e1 = GlossaryEntry.of(raw, c1.citations.norms, r1)
    e2 = GlossaryEntry.of(raw, c2.citations.norms, r2)
    status = "copy" if e1.keys is not None and e1 == e2 else "cited-file-differs"
    print(f"{raw['id']}\t{raw.get('origin')}\t{status}\t{','.join(using)}")
