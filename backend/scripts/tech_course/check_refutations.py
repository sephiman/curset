# SPDX-License-Identifier: AGPL-3.0-only
"""Every option of every question names its evidence in the sidecar `<lesson>.refutations.yaml`.

uv run python -m scripts.tech_course.check_refutations [--exclude-failed] [--lesson ID | --module mNN | FILE]

The sidecar sits beside `<lesson>.questions.json` and is never read by the platform loader:

    m02-l01-q01:
      key: {anchor: "src#anchor", sentence: "literal sentence of the anchor"}
      wrong:
        - {option: "text of a distractor", anchor: "src#anchor", sentence: "…"}
        - {option: "…", execution: "m02-l01/Foo.java", mistake: "off-by-one"}
        - {option: "…", anchor: "…", sentence: "…", exclusive: true}

Rules: the key and each distractor have exactly one entry; a sentence is a literal substring of its anchor
(whitespace collapsed); an execution entry names a snippet with a run record, whose output equals the key
and differs from every wrong option; two wrong options share a sentence only when both are `exclusive: true`.
Lessons listed in `refutations-exempt.tsv` (verified before the sidecar existed) are skipped.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

from scripts.tech_course.anchor_text import AnchorStore, collapse
from scripts.tech_course.candidates import (
    S2_DIR,
    Candidate,
    add_selection_arguments,
    failed_ids,
    lesson_of,
    read_candidates,
    select_files,
)
from scripts.tech_course.fill_keys import MissingRecordError, recorded_key
from scripts.tech_course.lessons import add_course_argument, course_dir
from tradeschool.citations.tech import TechSourceIndex, parse_ref

EXEMPT_FILE = S2_DIR / "refutations-exempt.tsv"
SUFFIX = ".refutations.yaml"


@dataclass(frozen=True)
class Evidence:
    option: str
    anchor: str
    sentence: str
    execution: str
    exclusive: bool

    @property
    def is_execution(self) -> bool:
        return bool(self.execution)


def _text(raw: dict[str, object], name: str) -> str:
    value = raw.get(name)
    return value if isinstance(value, str) else ""


def evidence_of(raw: object) -> Evidence | None:
    if not isinstance(raw, dict):
        return None
    return Evidence(
        option=" ".join(_text(raw, "option").split()),
        anchor=_text(raw, "anchor").strip(),
        sentence=_text(raw, "sentence"),
        execution=_text(raw, "execution").strip(),
        exclusive=raw.get("exclusive") is True,
    )


@dataclass(frozen=True)
class Checker:
    index: TechSourceIndex
    store: AnchorStore
    snippets_root: Path

    def evidence_problems(self, qid: str, role: str, ev: Evidence) -> list[str]:
        if ev.is_execution:
            return self._execution_problems(qid, role, ev)
        ref = parse_ref(ev.anchor)
        if ref is None:
            return [f"{qid} {role}: anchor is not source_id#anchor: {ev.anchor!r}"]
        if not ev.sentence.strip():
            return [f"{qid} {role}: no sentence and no execution"]
        if self.index.problem(ref):
            return [f"{qid} {role}: {ev.anchor} does not resolve"]
        anchor = self.store.anchor(ref)
        if anchor is None or collapse(ev.sentence) in collapse(anchor.text):
            return []
        return [f"{qid} {role}: sentence is not a literal substring of {ev.anchor}"]

    def _execution_problems(self, qid: str, role: str, ev: Evidence) -> list[str]:
        try:
            recorded_key(self.snippets_root, ev.execution)
        except MissingRecordError as exc:
            return [f"{qid} {role}: {exc}"]
        return []

    def recorded(self, snippet: str) -> str | None:
        try:
            return " ".join(recorded_key(self.snippets_root, snippet).split())
        except MissingRecordError:
            return None


def question_problems(q: Candidate, raw: object, checker: Checker) -> list[str]:
    if not isinstance(raw, dict):
        return [f"{q.id}: no refutation entry"]
    problems: list[str] = []
    key = evidence_of(raw.get("key"))
    if key is None:
        problems.append(f"{q.id} key: no entry")
    else:
        problems += checker.evidence_problems(q.id, "key", key)
        problems += _execution_key_problems(q, key, checker)
    wrong_raw = raw.get("wrong")
    wrong = [evidence_of(item) for item in wrong_raw] if isinstance(wrong_raw, list) else []
    entries = [ev for ev in wrong if ev is not None]
    problems += _coverage_problems(q, entries)
    for ev in entries:
        problems += checker.evidence_problems(q.id, f"wrong {ev.option[:40]!r}", ev)
        problems += _execution_wrong_problems(q, ev, checker)
    problems += _shared_sentence_problems(q.id, entries)
    return problems


def _execution_key_problems(q: Candidate, key: Evidence, checker: Checker) -> list[str]:
    if not key.is_execution:
        return []
    output = checker.recorded(key.execution)
    if output is None or output == " ".join(q.key.split()):
        return []
    return [f"{q.id} key: differs from the recorded output of {key.execution}"]


def _execution_wrong_problems(q: Candidate, ev: Evidence, checker: Checker) -> list[str]:
    if not ev.is_execution:
        return []
    if checker.recorded(ev.execution) == ev.option:
        return [f"{q.id} wrong {ev.option[:40]!r}: equals the recorded output of {ev.execution}"]
    return []


def _coverage_problems(q: Candidate, entries: list[Evidence]) -> list[str]:
    distractors = [" ".join(d.split()) for d in q.distractors]
    named = [ev.option for ev in entries]
    problems = [f"{q.id}: no refutation for {d[:40]!r}" for d in distractors if d not in named]
    problems += [
        f"{q.id}: refutation for an option not in the question: {n[:40]!r}"
        for n in named
        if n not in distractors
    ]
    problems += [f"{q.id}: two refutations for {n[:40]!r}" for n in set(named) if named.count(n) > 1]
    return problems


def _shared_sentence_problems(qid: str, entries: list[Evidence]) -> list[str]:
    by_sentence: dict[tuple[str, str], list[Evidence]] = {}
    for ev in entries:
        if not ev.is_execution:
            by_sentence.setdefault((ev.anchor, collapse(ev.sentence)), []).append(ev)
    return [
        f"{qid}: wrong options share a sentence of {anchor} without exclusive: true"
        for (anchor, _), group in by_sentence.items()
        if len(group) > 1 and not all(ev.exclusive for ev in group)
    ]


def exempt_lessons(path: Path = EXEMPT_FILE) -> frozenset[str]:
    if not path.is_file():
        return frozenset()
    lines = (line.split("\t")[0].strip() for line in path.read_text(encoding="utf-8").splitlines())
    return frozenset(line for line in lines if line and not line.startswith("#"))


def lesson_problems(path: Path, checker: Checker, skipped: frozenset[str]) -> tuple[int, list[str]]:
    lesson = lesson_of(path)
    questions = [q for q in read_candidates(path) if q.id not in skipped]
    sidecar = path.with_name(f"{lesson}{SUFFIX}")
    if not sidecar.is_file():
        return len(questions), [f"{lesson}: no {sidecar.name}"] if questions else []
    loaded = yaml.safe_load(sidecar.read_text(encoding="utf-8")) or {}
    if not isinstance(loaded, dict):
        return len(questions), [f"{lesson}: {sidecar.name} is not a mapping of question ids"]
    problems = [p for q in questions for p in question_problems(q, loaded.get(q.id), checker)]
    return len(questions), problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    add_selection_arguments(parser)
    parser.add_argument("--exclude-failed", action="store_true", help="skip questions with a fail verdict")
    args = parser.parse_args(argv)
    index = TechSourceIndex.load(course_dir(args.course))
    if index is None:
        raise SystemExit(f"{args.course} has no sources/sources.yaml")
    checker = Checker(index, AnchorStore(index, args.course), course_dir(args.course) / "snippets")
    exempt = exempt_lessons()
    seen = 0
    problems: list[str] = []
    for path in select_files(args.lesson, args.module, args.paths):
        if lesson_of(path) in exempt:
            continue
        skipped = (
            failed_ids(path.with_name(f"{lesson_of(path)}.verdicts.tsv"))
            if args.exclude_failed
            else frozenset()
        )
        count, found = lesson_problems(path, checker, skipped)
        seen += count
        problems += found
    for problem in problems:
        print(f"FAIL {problem}")
    print(f"check_refutations: {seen} questions, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
