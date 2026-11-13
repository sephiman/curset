"""Build the kept AEAT questions into exercise YAML and course.yaml entries (C2's builder, AEAT-parameterised).

Run from backend/: `uv run python ../docs/age-verification/aeat/bank/tools/build_exercises.py [--course-dir DIR]`.
Default DIR is `content/aeat-agentes-hacienda` (the live build); pass a scratch copy to rehearse. Kept =
`<lesson>.kept-derived.json` + every `<lesson>.authored*.draft.json`, minus `drops.tsv`, `held.tsv` and the RDL 29/2026
holds. Also writes `provenance/<lesson>.md`: one line per question, «verificado en C1|C2: <report>» or
«verificado: PASS · <report>», never neither. Sets `exercise_types: [quiz]` and `lesson_practice: true`.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path

from tradeschool.citations.course import CourseCitations

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rdl_held import held_reason  # noqa: E402

ROOT = Path(__file__).resolve().parents[5]
BANK = ROOT / "docs" / "age-verification" / "aeat" / "bank"
_spec = importlib.util.spec_from_file_location("c1_build", ROOT / "docs/age-verification/bank/tools/build_exercises.py")
assert _spec and _spec.loader
c1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c1)
HEADER = (
    "# SPDX-License-Identifier: AGPL-3.0-only\n"
    "# Question bank, {lesson}: fixed multiple-choice questions (AEAT round R3). Generated from\n"
    "# docs/age-verification/aeat/bank/ (kept derived + authored minus drops.tsv and held.tsv) by\n"
    "# docs/age-verification/aeat/bank/tools/build_exercises.py; edit the drafts and rebuild, not this file.\n"
)
ID_CELL = re.compile(r"^[\w-]+-q\d+$")


def tsv_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open(encoding="utf-8") as handle:
        return {row["id"] for row in csv.DictReader(handle, delimiter="\t")}


def verified() -> dict[str, str]:
    """Question id → report whose table gives it PASS in its «verdict» column (later reports win, rechecks included)."""
    out: dict[str, str] = {}
    for report in sorted((BANK / "verify").glob("*.md")):
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
            if column is not None and len(cells) > column and ID_CELL.match(cells[0]):
                if cells[column] == "PASS":
                    out[cells[0]] = str(report.relative_to(ROOT))
                else:
                    out.pop(cells[0], None)
    return out


def kept(lesson: str, drops: set[str]) -> list[dict[str, object]]:
    questions: list[dict[str, object]] = []
    derived = BANK / f"{lesson}.kept-derived.json"
    if derived.exists():
        questions += json.loads(derived.read_text(encoding="utf-8"))
    for draft in sorted(BANK.glob(f"{lesson}.authored*.draft.json")):
        questions += json.loads(draft.read_text(encoding="utf-8"))
    return [q for q in questions if q["id"] not in drops]


def main(course_dir: Path) -> None:
    drops = tsv_ids(BANK / "drops.tsv") | tsv_ids(BANK / "held.tsv")
    passes = verified()
    markdown = {"es": {p.stem: p.read_text(encoding="utf-8") for p in (course_dir / "es" / "lessons").glob("*.md")}}
    citations = CourseCitations.build(course_dir, course_dir.name, markdown)
    course_yaml = (course_dir / "course.yaml").read_text(encoding="utf-8")
    course_yaml = course_yaml.replace("exercise_types: []", "exercise_types: [quiz]")
    if "lesson_practice:" not in course_yaml:
        course_yaml = course_yaml.replace("  option_labels: letters", "  # Questions are practised per tema from its «Practicar» page.\n  lesson_practice: true\n  option_labels: letters")
    out = course_dir / "exercises"
    out.mkdir(exist_ok=True)
    for old in out.glob("m0?-l??-ex-*.yaml"):
        old.unlink()
    (BANK / "provenance").mkdir(exist_ok=True)
    held_rdl: list[str] = []
    total = 0
    for lesson in sorted(p.stem for p in (course_dir / "es" / "lessons").glob("m0[123]-l*.md")):
        questions = []
        for q in kept(lesson, drops):
            if reason := held_reason(str(q["citation"])):
                held_rdl.append(f"{q['id']}\t{reason}")
                continue
            questions.append(q)
        if not questions:
            continue
        sections = [h[3:].strip() for h in markdown["es"][lesson].splitlines() if h.startswith("## ")]
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
            body = HEADER.format(lesson=lesson) + "type: quiz\nvariants:\n" + "\n".join(variants) + "\n"
            (out / f"{exercise_id}.yaml").write_text(body, encoding="utf-8")
            exercise_ids.append(exercise_id)
        course_yaml = c1.manifest_entries(course_yaml, lesson, exercise_ids)
        (BANK / "provenance" / f"{lesson}.md").write_text(
            f"# Provenance — {lesson} ({len(questions)} questions)\n\n" + "\n".join(records) + "\n", encoding="utf-8"
        )
        total += len(questions)
        print(f"{lesson}: {len(questions)} questions in {len(exercise_ids)} exercises")
    (course_dir / "course.yaml").write_text(course_yaml, encoding="utf-8")
    (BANK / "held-rdl-29-2026.tsv").write_text("id\treason\n" + "\n".join(held_rdl) + ("\n" if held_rdl else ""), encoding="utf-8")
    print(f"total {total}; held by RDL 29/2026: {len(held_rdl)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--course-dir", type=Path, default=ROOT / "content" / "aeat-agentes-hacienda")
    main(parser.parse_args().course_dir)
