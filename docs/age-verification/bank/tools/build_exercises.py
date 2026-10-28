"""Build the kept questions of a bloque into exercise YAML and course.yaml entries.

Run from backend/: `uv run python ../docs/age-verification/bank/tools/build_exercises.py bloque-i m01`.
Kept = every question in `<bloque>/mBB-lTT.draft.json` whose id is not in `<bloque>/drops.tsv`. Options keep their
authored order (positions are balanced per tema; the platform shuffles per learner). Questions are grouped by lesson
section, in lesson order, into exercises of MIN_PER..MAX_PER variants. Each variant gets a `# anchor:` comment from the
platform's own resolver; a citation that resolves to nothing stops the build. Question ids pass through verbatim:
a drop may regroup a tema's exercises, but a question's key is its id, so attempts and stats never notice.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

from tradeschool.citations.course import CourseCitations

ROOT = Path(__file__).resolve().parents[4]
COURSE = ROOT / "content" / "age-administrativo-c1"
BANK = ROOT / "docs" / "age-verification" / "bank"
MIN_PER, MAX_PER = 12, 25
HEADER = (
    "# SPDX-License-Identifier: AGPL-3.0-only\n"
    "# Question bank, {lesson}: fixed multiple-choice questions (round R3). Generated from\n"
    "# docs/age-verification/bank/{bloque}/{lesson}.draft.json minus drops.tsv by\n"
    "# docs/age-verification/bank/tools/build_exercises.py; edit the draft and rebuild, not this file.\n"
)


def kept_questions(bloque: str, lesson: str) -> list[dict[str, object]]:
    folder = BANK / bloque
    with (folder / "drops.tsv").open(encoding="utf-8") as handle:
        drops = {row["id"] for row in csv.DictReader(handle, delimiter="\t")}
    drafts = json.loads((folder / f"{lesson}.draft.json").read_text(encoding="utf-8"))
    return [q for q in drafts if q["id"] not in drops]


def group(questions: list[dict[str, object]]) -> list[list[dict[str, object]]]:
    """Consecutive sections merged until a group holds MIN_PER; a group never passes MAX_PER."""
    sections: list[list[dict[str, object]]] = []
    for q in questions:
        if sections and sections[-1][0]["section"] == q["section"]:
            sections[-1].append(q)
        else:
            sections.append([q])
    groups: list[list[dict[str, object]]] = [[]]
    for section in sections:
        for q in section:
            if len(groups[-1]) >= MAX_PER:
                groups.append([])
            groups[-1].append(q)
        if len(groups[-1]) >= MIN_PER:
            groups.append([])
    groups = [g for g in groups if g]
    if len(groups) > 1 and len(groups[-1]) < MIN_PER and len(groups[-2]) + len(groups[-1]) <= MAX_PER:
        groups[-2].extend(groups.pop())
    return groups


def scalar(text: object) -> str:
    return json.dumps(str(text), ensure_ascii=False)


def variant_yaml(q: dict[str, object], anchor: str) -> str:
    options = q["options"]
    assert isinstance(options, dict) and sorted(options) == ["a", "b", "c", "d"], q["id"]
    lines = [f"# anchor: {anchor}", f"- id: {q['id']}", "  prompt:", f"    es: {scalar(q['prompt'])}", "  options:"]
    for key in "abcd":
        lines.append(f"  - id: {key}")
        if key == q["correct"]:
            lines.append("    correct: true")
        lines += ["    text:", f"      es: {scalar(options[key])}"]
    lines += [
        "  explanation:",
        f"    es: {scalar(q['explanation'])}",
        f"  citation: {scalar(q['citation'])}",
        f"  difficulty: {int(q['difficulty'])}",  # type: ignore[call-overload]
        "  tags:",
    ]
    lines += [f"  - {scalar(tag)}" for tag in q["tags"]]  # type: ignore[union-attr]
    return "\n".join(lines)


def manifest_entries(course_yaml: str, lesson: str, exercise_ids: list[str]) -> str:
    """Replace (or add) the `exercises:` list of one lesson block in course.yaml."""
    start = course_yaml.index(f"    - id: {lesson}\n")
    nxt = re.compile(r"^(    - id: |  - id: |- id: |exams:)", re.M).search(course_yaml, start + 1)
    end = nxt.start() if nxt else len(course_yaml)
    block = re.sub(r"      exercises:\n(?:      - id: .*\n        type: quiz\n)*", "", course_yaml[start:end])
    entries = "      exercises:\n" + "".join(f"      - id: {e}\n        type: quiz\n" for e in exercise_ids)
    return course_yaml[:start] + block.rstrip("\n") + "\n" + entries + course_yaml[end:]


def main(bloque: str, module: str) -> None:
    markdown = {"es": {p.stem: p.read_text(encoding="utf-8") for p in (COURSE / "es" / "lessons").glob("*.md")}}
    citations = CourseCitations.build(COURSE, COURSE.name, markdown)
    course_yaml = (COURSE / "course.yaml").read_text(encoding="utf-8")
    out = COURSE / "exercises"
    out.mkdir(exist_ok=True)
    for old in out.glob(f"{module}-l*-ex-*.yaml"):
        old.unlink()
    total = 0
    for draft in sorted((BANK / bloque).glob(f"{module}-l*.draft.json")):
        if draft.name.count(".") > 2:  # parts and .s5/.s7 records are already merged into the lesson draft
            continue
        lesson = draft.name.split(".")[0]
        questions = kept_questions(bloque, lesson)
        exercise_ids = []
        for n, chunk in enumerate(group(questions), start=1):
            exercise_id = f"{lesson}-ex-{n}"
            variants = []
            for q in chunk:
                anchor = citations.question_link(lesson, str(q["citation"]), "es").anchor
                if anchor is None:
                    sys.exit(f"{q['id']}: citation «{q['citation']}» resolves to no anchor in {lesson}")
                variants.append(variant_yaml(q, anchor))
            body = HEADER.format(lesson=lesson, bloque=bloque) + "type: quiz\nvariants:\n" + "\n".join(variants) + "\n"
            (out / f"{exercise_id}.yaml").write_text(body, encoding="utf-8")
            exercise_ids.append(exercise_id)
        course_yaml = manifest_entries(course_yaml, lesson, exercise_ids)
        total += len(questions)
        print(f"{lesson}: {len(questions)} questions in {len(exercise_ids)} exercises")
    (COURSE / "course.yaml").write_text(course_yaml, encoding="utf-8")
    print(f"total {total}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
