"""Build a C2 bloque's kept questions into exercise YAML and course.yaml entries (C1's builder, course-parameterised).

Run from backend/: `uv run python ../docs/age-verification/c2/bank/tools/build_exercises.py bloque-ii m02`.
Kept = `<lesson>.kept-derived.json` + every `<lesson>.authored*.draft.json`, minus `drops.tsv` and `held.tsv`; ordered by lesson
section then id. Also writes `<bloque>/provenance/<lesson>.md`: one line per question, «verificado en C1: <report>» or
«verificado: PASS · <report>», never neither.
"""

from __future__ import annotations

import csv
import importlib.util
import json
import re
import sys
from pathlib import Path

from tradeschool.citations.course import CourseCitations

ROOT = Path(__file__).resolve().parents[5]
COURSE = ROOT / "content" / "age-auxiliar-c2"
BANK = ROOT / "docs" / "age-verification" / "c2" / "bank"
_spec = importlib.util.spec_from_file_location("c1_build", ROOT / "docs/age-verification/bank/tools/build_exercises.py")
assert _spec and _spec.loader
c1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c1)
HEADER = (
    "# SPDX-License-Identifier: AGPL-3.0-only\n"
    "# Question bank, {lesson}: fixed multiple-choice questions (C2 round R3). Generated from\n"
    "# docs/age-verification/c2/bank/{bloque}/ (kept derived + authored minus drops.tsv) by\n"
    "# docs/age-verification/c2/bank/tools/build_exercises.py; edit the drafts and rebuild, not this file.\n"
)
ID_CELL = re.compile(r"^[\w-]+-q\d+$")


def verified(folder: Path) -> dict[str, str]:
    """Question id → report whose table gives it a PASS in its «verdict» (or «final verdict») column."""
    out: dict[str, str] = {}
    for report in sorted((folder / "verify").glob("*.md")) if (folder / "verify").exists() else []:
        column: int | None = None
        for line in report.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                column = None
                continue
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
            heads = [c.lower() for c in cells]
            if "verdict" in heads or "final verdict" in heads:
                column = heads.index("final verdict") if "final verdict" in heads else heads.index("verdict")
                continue
            if column is not None and len(cells) > column and ID_CELL.match(cells[0]) and cells[column] == "PASS":
                out[cells[0]] = str(report.relative_to(ROOT))
    return out


def kept(folder: Path, lesson: str, drops: set[str]) -> list[dict[str, object]]:
    questions: list[dict[str, object]] = []
    derived = folder / f"{lesson}.kept-derived.json"
    if derived.exists():
        questions += json.loads(derived.read_text(encoding="utf-8"))
    for draft in sorted(folder.glob(f"{lesson}.authored*.draft.json")):
        questions += json.loads(draft.read_text(encoding="utf-8"))
    return [q for q in questions if q["id"] not in drops]


def main(bloque: str, module: str) -> None:
    folder = BANK / bloque
    with (folder / "drops.tsv").open(encoding="utf-8") as handle:
        drops = {row["id"] for row in csv.DictReader(handle, delimiter="\t")}
    with (folder / "held.tsv").open(encoding="utf-8") as handle:
        drops |= {row["id"] for row in csv.DictReader(handle, delimiter="\t")}  # held for variant rounds
    passes = verified(folder)
    markdown = {"es": {p.stem: p.read_text(encoding="utf-8") for p in (COURSE / "es" / "lessons").glob("*.md")}}
    citations = CourseCitations.build(COURSE, COURSE.name, markdown)
    course_yaml = (COURSE / "course.yaml").read_text(encoding="utf-8")
    out = COURSE / "exercises"
    out.mkdir(exist_ok=True)
    for old in out.glob(f"{module}-l*-ex-*.yaml"):
        old.unlink()
    (folder / "provenance").mkdir(exist_ok=True)
    lessons = sorted({p.name.split(".")[0] for p in folder.glob(f"{module}-l*.json")})
    total = 0
    for lesson in lessons:
        sections = [h[3:].strip() for h in markdown["es"][lesson].splitlines() if h.startswith("## ")]
        questions = kept(folder, lesson, drops)
        questions.sort(key=lambda q: (sections.index(str(q["section"])) if q["section"] in sections else 99, q["id"]))
        records = []
        for q in questions:
            record = q.get("provenance") or (f"verificado: PASS · {passes[str(q['id'])]}" if q["id"] in passes else None)
            if record is None:
                sys.exit(f"{q['id']}: neither a provenance record nor its own verification")
            records.append(f"- {q['id']}: {record}")
        exercise_ids = []
        for n, chunk in enumerate(c1.group(questions), start=1):
            exercise_id = f"{lesson}-ex-{n}"
            variants = []
            for q in chunk:
                anchor = citations.question_link(lesson, str(q["citation"]), "es").anchor
                if anchor is None:
                    sys.exit(f"{q['id']}: citation «{q['citation']}» resolves to no anchor in {lesson}")
                variants.append(c1.variant_yaml(q, anchor))
            body = HEADER.format(lesson=lesson, bloque=bloque) + "type: quiz\nvariants:\n" + "\n".join(variants) + "\n"
            (out / f"{exercise_id}.yaml").write_text(body, encoding="utf-8")
            exercise_ids.append(exercise_id)
        course_yaml = c1.manifest_entries(course_yaml, lesson, exercise_ids)
        (folder / "provenance" / f"{lesson}.md").write_text(
            f"# Provenance — {lesson} ({len(questions)} questions)\n\n" + "\n".join(records) + "\n", encoding="utf-8"
        )
        total += len(questions)
        print(f"{lesson}: {len(questions)} questions in {len(exercise_ids)} exercises")
    (COURSE / "course.yaml").write_text(course_yaml, encoding="utf-8")
    print(f"total {total}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
