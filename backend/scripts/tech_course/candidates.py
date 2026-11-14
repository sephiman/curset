# SPDX-License-Identifier: AGPL-3.0-only
"""Question candidate files, `docs/backend-verification/s2/<module>/<lesson>.questions.json`."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

from scripts.tech_course.lessons import REPO

S2_DIR = REPO / "docs" / "backend-verification" / "s2"
_SUFFIX = ".questions.json"
_MODULE = re.compile(r"^m\d{2}$")


@dataclass(frozen=True)
class Candidate:
    id: str
    stem: str
    key: str
    distractors: tuple[str, ...]
    explanation: str
    citation: str
    has_extract: bool
    extract: str | None
    snippet: str | None

    @property
    def options(self) -> tuple[str, ...]:
        return (self.key, *self.distractors)


def _text(value: object) -> str:
    return value if isinstance(value, str) else ""


def candidate_of(raw: dict[str, object]) -> Candidate:
    extract, snippet = raw.get("extract"), raw.get("snippet")
    distractors = raw.get("distractors")
    return Candidate(
        id=_text(raw.get("id")),
        stem=_text(raw.get("stem")),
        key=_text(raw.get("key")),
        distractors=tuple(_text(d) for d in distractors) if isinstance(distractors, list) else (),
        explanation=_text(raw.get("explanation")),
        citation=_text(raw.get("citation")),
        has_extract="extract" in raw,
        extract=extract if isinstance(extract, str) else None,
        snippet=snippet if isinstance(snippet, str) and snippet.strip() else None,
    )


def read_raw(path: Path) -> list[dict[str, object]]:
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return [entry for entry in loaded if isinstance(entry, dict)]


def write_raw(path: Path, entries: list[dict[str, object]]) -> None:
    path.write_text(json.dumps(entries, indent=1, ensure_ascii=False), encoding="utf-8")


def read_candidates(path: Path) -> list[Candidate]:
    return [candidate_of(raw) for raw in read_raw(path)]


def lesson_of(path: Path) -> str:
    return path.name.removesuffix(_SUFFIX)


def add_selection_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--lesson", help="one lesson id, e.g. m06-l04")
    parser.add_argument("--module", help="one module, e.g. m06")
    parser.add_argument("paths", nargs="*", type=Path, help="candidate files; default every file")


def select_files(
    lesson: str | None, module: str | None, paths: list[Path], root: Path = S2_DIR
) -> list[Path]:
    if paths:
        return sorted(paths)
    if module is not None and not _MODULE.match(module):
        raise SystemExit(f"not a module id: {module}")
    folder = root / module if module else root
    pattern = f"{lesson}{_SUFFIX}" if lesson else f"*{_SUFFIX}"
    return sorted(folder.glob(pattern) if module else folder.glob(f"m*/{pattern}"))


def failed_ids(verdicts: Path) -> frozenset[str]:
    if not verdicts.is_file():
        return frozenset()
    final: dict[str, str] = {}
    for line in verdicts.read_text(encoding="utf-8").splitlines():
        row = [cell.strip() for cell in line.split("\t")]
        # a `recheck` line, written after a re-verification, replaces the first verdict
        verdict = row[2] if len(row) > 2 and row[1] == "recheck" else row[1] if len(row) > 1 else ""
        if verdict in ("pass", "fail"):
            final[row[0]] = verdict
    return frozenset(qid for qid, verdict in final.items() if verdict == "fail")
