# SPDX-License-Identifier: AGPL-3.0-only
"""Form checks of amendment 17 that `lint_questions` does not make, on round D4 attributed-question candidates.

    python attributed_form.py FILE.questions.json ...

Per question: the stem opens "According to … in …,"; the shortest option is at least MIN_RATIO of the longest;
the refutation map uses one source for the key and every wrong option, never `exclusive`; the citation names that
source; the source backs a `:::judgement` block of the lesson. Per lesson: the key is the longest option in at most
40 % of the questions. Exit 1 on any failure.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[4]
LESSONS = REPO / "content" / "backend-in-depth" / "en" / "lessons"
MIN_RATIO = 0.6
KEY_LONGEST_LIMIT = 0.40
_STEM = re.compile(r"^According to [^,]+? in [^,]+,")
_JUDGEMENT_REF = re.compile(r':::judgement\{[^}]*ref="([^"#]+)#')


def _length(text: str) -> int:
    return len(" ".join(text.split()))


def judgement_sources(lesson: str) -> set[str]:
    return set(_JUDGEMENT_REF.findall((LESSONS / f"{lesson}.md").read_text(encoding="utf-8")))


def question_failures(q: dict[str, object], refutation: dict[str, object] | None, allowed: set[str]) -> list[str]:
    failures: list[str] = []
    stem, key = str(q["stem"]), str(q["key"])
    options = [key, *(str(d) for d in q["distractors"])]  # type: ignore[union-attr]
    if not _STEM.match(stem):
        failures.append("stem does not open 'According to AUTHOR in WORK,'")
    lengths = [_length(o) for o in options]
    if min(lengths) < MIN_RATIO * max(lengths):
        failures.append(f"option lengths {lengths}: shortest under {MIN_RATIO:.0%} of longest")
    source = str(q["citation"]).split(";")[0].split("#")[0].strip()
    if source not in allowed:
        failures.append(f"citation source {source} backs no judgement block of the lesson")
    if refutation is None:
        return [*failures, "no refutation map entry"]
    entries = [refutation.get("key", {}), *refutation.get("wrong", [])]  # type: ignore[list-item]
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        if entry.get("exclusive"):
            failures.append("exclusive is not allowed in this round")
        anchored = str(entry.get("anchor", "")).split("#")[0]
        if anchored != source:
            failures.append(f"refutation from {anchored or 'no anchor'}, not {source}")
    return failures


def check_file(path: Path) -> int:
    lesson = path.name.removesuffix(".questions.json")
    questions = json.loads(path.read_text(encoding="utf-8"))
    map_path = path.with_name(f"{lesson}.refutations.yaml")
    refutations = yaml.safe_load(map_path.read_text(encoding="utf-8")) if map_path.is_file() else {}
    allowed = judgement_sources(lesson)
    failed = 0
    longest = 0
    for q in questions:
        problems = question_failures(q, (refutations or {}).get(q["id"]), allowed)
        options = [q["key"], *q["distractors"]]
        if _length(q["key"]) == max(_length(o) for o in options):
            longest += 1
        for problem in problems:
            print(f"{q['id']}\t{problem}")
        failed += bool(problems)
    if questions and longest / len(questions) > KEY_LONGEST_LIMIT:
        print(f"{lesson}\tkey longest in {longest}/{len(questions)} questions, over {KEY_LONGEST_LIMIT:.0%}")
        failed += 1
    print(f"{lesson}\t{len(questions)} questions, {failed} failing")
    return failed


def main(argv: list[str]) -> int:
    return 1 if sum(check_file(Path(a)) for a in argv) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
