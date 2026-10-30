"""Build the kept questions of every case draft into `case` exercises and course.yaml entries.

Run from backend/: `uv run python ../docs/age-verification/cases/tools/build_cases.py`.
Kept = the draft minus drops.tsv, a replacement in its dropped question's place (case_check.kept). Options keep their
authored order (the platform shuffles per learner). Each question gets a `# anchor:` comment from the platform's own
resolver in the lesson it names; a citation that resolves to nothing stops the build. The cases are listed, in case
order, under m00-l01 («Cómo es el examen»): each question counts under its own tema, the case itself under none.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from tradeschool.citations.course import CourseCitations

sys.path.insert(0, str(Path(__file__).resolve().parent))
from case_check import kept  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]
COURSE = ROOT / "content" / "age-administrativo-c1"
CASES = ROOT / "docs" / "age-verification" / "cases"
HOST_LESSON = "m00-l01"
QUESTIONS = 20
HEADER = (
    "# SPDX-License-Identifier: AGPL-3.0-only\n"
    "# Supuesto práctico {case} (round R4). Generated from docs/age-verification/cases/{case}.draft.json minus\n"
    "# drops.tsv by docs/age-verification/cases/tools/build_cases.py; edit the draft and rebuild, not this file.\n"
)


def scalar(text: object) -> str:
    return json.dumps(str(text), ensure_ascii=False)


def question_yaml(q: dict[str, object], anchor: str) -> str:
    options = q["options"]
    assert isinstance(options, dict) and sorted(options) == ["a", "b", "c", "d"], q["id"]
    lines = [
        f"# anchor: {anchor}",
        f"- id: {q['id']}",
        f"  lesson: {q['lesson']}",
        "  prompt:",
        f"    es: {scalar(q['prompt'])}",
        "  options:",
    ]
    for key in "abcd":
        lines.append(f"  - id: {key}")
        if key == q["correct"]:
            lines.append("    correct: true")
        lines += ["    text:", f"      es: {scalar(options[key])}"]
    lines += [
        "  explanation:",
        f"    es: {scalar(q['explanation'])}",
        f"  citation: {scalar(q['citation'])}",
        f"  difficulty: {int(str(q['difficulty']))}",
        "  tags:",
    ]
    tags = q["tags"]
    assert isinstance(tags, list)
    lines += [f"  - {scalar(tag)}" for tag in tags]
    return "\n".join(lines)


def manifest_entries(course_yaml: str, case_ids: list[str]) -> str:
    """Replace (or add) the `exercises:` list of the host lesson with the cases."""
    start = course_yaml.index(f"    - id: {HOST_LESSON}\n")
    nxt = re.compile(r"^(    - id: |  - id: |- id: |exams:)", re.M).search(course_yaml, start + 1)
    end = nxt.start() if nxt else len(course_yaml)
    block = re.sub(r"      exercises:\n(?:      - id: .*\n        type: case\n)*", "", course_yaml[start:end])
    entries = "      exercises:\n" + "".join(f"      - id: {c}\n        type: case\n" for c in case_ids)
    return course_yaml[:start] + block.rstrip("\n") + "\n" + entries + course_yaml[end:]


def main() -> None:
    markdown = {"es": {p.stem: p.read_text(encoding="utf-8") for p in (COURSE / "es" / "lessons").glob("*.md")}}
    citations = CourseCitations.build(COURSE, COURSE.name, markdown)
    out = COURSE / "exercises"
    for old in out.glob("sp-*.yaml"):
        old.unlink()
    case_ids = []
    for draft in sorted(CASES.glob("sp-[0-9][0-9].draft.json")):
        case = json.loads(draft.read_text(encoding="utf-8"))
        questions = kept(case)
        if len(questions) != QUESTIONS:
            print(f"{case['case']}: {len(questions)} kept questions, not {QUESTIONS}; not built")
            continue
        blocks = []
        for q in questions:
            anchor = citations.question_link(q["lesson"], str(q["citation"]), "es").anchor
            if anchor is None:
                sys.exit(f"{case['case']}/{q['id']}: citation «{q['citation']}» resolves to no anchor in {q['lesson']}")
            blocks.append(question_yaml(q, anchor))
        body = (
            HEADER.format(case=case["case"])
            + "type: case\n"
            + f"title:\n  es: {scalar(case['title'])}\n"
            + f"scenario:\n  es: {scalar(case['scenario'])}\n"
            + "questions:\n"
            + "\n".join(blocks)
            + "\n"
        )
        (out / f"{case['case']}.yaml").write_text(body, encoding="utf-8")
        case_ids.append(case["case"])
        print(f"{case['case']}: built, {len(questions)} questions")
    course_yaml = (COURSE / "course.yaml").read_text(encoding="utf-8")
    course_yaml = manifest_entries(course_yaml, case_ids)
    if case_ids:
        course_yaml = course_yaml.replace("  exercise_types: [quiz]\n", "  exercise_types: [quiz, case]\n")
    (COURSE / "course.yaml").write_text(course_yaml, encoding="utf-8")
    print(f"{len(case_ids)} cases")


if __name__ == "__main__":
    main()
