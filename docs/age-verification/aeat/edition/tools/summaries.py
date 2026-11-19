"""summaries.py [--write]: keep the sentences of each lesson summary (course.yaml) that the assembled lesson still carries.

A summary sentence stays when at least 60 % of its content words (7+ letters, compared by their first six letters) occur
in the lesson text; otherwise it goes to edition/summaries-dropped.md. A summary is never emptied: if no sentence
passes, the first stays. Sentences are cut whole and never reworded. Only the YAML scalar is rewritten, in place.
"""

from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lesson_model import ROOT  # noqa: E402
from scripts.provenance import _split  # noqa: E402

COURSE = ROOT / "content/aeat-agentes-hacienda"
EDITION = ROOT / "docs/age-verification/aeat/edition"
WORD = re.compile(r"[a-záéíóúñü]{7,}")
THRESHOLD = 0.6


def stems(text: str) -> set[str]:
    return {w[:6] for w in WORD.findall(text.lower())}


def keep_sentences(summary: str, lesson_text: str) -> tuple[list[str], list[str]]:
    have = stems(lesson_text)
    kept, dropped = [], []
    for sentence in _split(summary):
        words = stems(sentence)
        if not words or len(words & have) / len(words) >= THRESHOLD:
            kept.append(sentence)
        else:
            dropped.append(sentence)
    if not kept and dropped:
        kept, dropped = dropped[:1], dropped[1:]
    return kept, dropped


def scalar_span(lines: list[str], start: int) -> tuple[int, int, str]:
    """Lines [start, end) of the YAML scalar whose key line is lines[start]; its text."""
    key_line = lines[start]
    indent = len(key_line) - len(key_line.lstrip())
    end = start + 1
    while end < len(lines) and (not lines[end].strip() or len(lines[end]) - len(lines[end].lstrip()) > indent):
        end += 1
    body = key_line.split("es:", 1)[1].strip() + " " + " ".join(l.strip() for l in lines[start + 1 : end])
    body = body.strip()
    if body.startswith("'") and body.endswith("'"):
        body = body[1:-1].replace("''", "'")
    return start, end, " ".join(body.split())


def emit(indent: int, text: str) -> list[str]:
    quoted = "'" + text.replace("'", "''") + "'"
    wrapped = textwrap.wrap(quoted, width=118 - indent - 4, break_long_words=False, break_on_hyphens=False)
    pad = " " * indent
    return [f"{pad}es: {wrapped[0]}"] + [f"{pad}  {w}" for w in wrapped[1:]]


def main(argv: list[str]) -> int:
    write = "--write" in argv
    lines = (COURSE / "course.yaml").read_text().split("\n")
    log: list[str] = ["# Summary sentences left out by the edition", ""]
    i = 0
    edits: list[tuple[int, int, list[str]]] = []
    current = ""
    while i < len(lines):
        m = re.match(r"^\s*- id: (m\d\d-l\d\d)\s*$", lines[i])
        if m:
            current = m.group(1)
        elif re.match(r"^\s*- id: \S+\s*$", lines[i]):
            current = ""  # a block or module: its summary is not a lesson's
        if current and lines[i].strip() == "summary:" and i + 1 < len(lines) and lines[i + 1].strip().startswith("es:"):
            if current == "m00-l01":
                i += 2
                continue
            start, end, summary = scalar_span(lines, i + 1)
            lesson_text = (COURSE / "es/lessons" / f"{current}.md").read_text()
            kept, dropped = keep_sentences(summary, lesson_text)
            if dropped:
                log.append(f"## {current}")
                log += [f"- {s}" for s in dropped]
                indent = len(lines[start]) - len(lines[start].lstrip())
                edits.append((start, end, emit(indent, " ".join(kept))))
            i = end
            continue
        i += 1
    for start, end, new in reversed(edits):
        lines[start:end] = new
    (EDITION / "summaries-dropped.md").write_text("\n".join(log) + "\n")
    if write:
        (COURSE / "course.yaml").write_text("\n".join(lines))
    print(f"summaries with dropped sentences: {len(edits)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
