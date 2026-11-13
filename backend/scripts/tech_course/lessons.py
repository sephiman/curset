# SPDX-License-Identifier: AGPL-3.0-only
"""A technical course's lessons on disk: sections with their bullet metadata, citations, snippet blocks."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from tradeschool.citations.tech import SourceRef, parse_ref, parse_refs
from tradeschool.content.esquema import Esquema, esquema_lines, parse_esquemas

REPO = Path(__file__).resolve().parents[3]
DEFAULT_COURSE = "backend-in-depth"
LOCALE = "en"
PENDING_MARK = "Lesson not written yet."
#: Requirements amendment 4.
EXEMPT_FROM_SCOPE = frozenset({"m00-l01"})
UNCOUNTED_SECTIONS = frozenset({"key points", "sources"})

_FENCE = re.compile(r"^(```|~~~)")
_SNIPPET_OPEN = re.compile(r"^```(?P<lang>\w+)[ \t]+snippet=(?P<path>\S+)[ \t]*$")
_SECTION = re.compile(r"^## (?P<title>.+?)\s*$")
_BULLETS = re.compile(r"^<!--\s*bullets:\s*(?P<ids>[^>]*?)\s*-->$")
_CITATION_PARENTHETICAL = re.compile(r"\(\s*(`[^`\n]+`(?:\s*;\s*`[^`\n]+`)*)\s*\)")
_JUDGEMENT_REF = re.compile(r'^:::judgement\{[^}\n]*\bref="(?P<ref>[^"]*)"')


def add_course_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--course", default=DEFAULT_COURSE)


def course_dir(course: str) -> Path:
    return REPO / "content" / course


@dataclass(frozen=True)
class Section:
    title: str
    line: int
    bullets: tuple[str, ...]

    @property
    def audited(self) -> bool:
        return self.title.lower() not in UNCOUNTED_SECTIONS


@dataclass(frozen=True)
class SnippetBlock:
    line: int
    path: str
    body: str


@dataclass(frozen=True)
class Cited:
    ref: SourceRef
    line: int
    section: str


@dataclass(frozen=True)
class Lesson:
    id: str
    text: str

    @property
    def lines(self) -> list[str]:
        return self.text.splitlines()

    @property
    def pending(self) -> bool:
        return PENDING_MARK in self.text

    def esquemas(self) -> list[Esquema]:
        return parse_esquemas(self.text)

    def sections(self) -> list[Section]:
        lines, found, fenced = self.lines, [], False
        for number, line in enumerate(lines, 1):
            fenced ^= bool(_FENCE.match(line))
            heading = None if fenced else _SECTION.match(line)
            if heading is None:
                continue
            following = _BULLETS.match(lines[number].strip()) if number < len(lines) else None
            bullets = tuple(following["ids"].split()) if following else ()
            found.append(Section(heading["title"], number, bullets))
        return found

    def section_at(self, line: int) -> str:
        title = ""
        for section in self.sections():
            if section.line > line:
                break
            title = section.title
        return title

    def snippet_blocks(self) -> list[SnippetBlock]:
        found: list[SnippetBlock] = []
        lines, index = self.lines, 0
        while index < len(lines):
            opened = _SNIPPET_OPEN.match(lines[index])
            index += 1
            if opened is None:
                continue
            start, body = index, []
            while index < len(lines) and not lines[index].startswith("```"):
                body.append(lines[index])
                index += 1
            found.append(SnippetBlock(start, opened["path"], "\n".join(body)))
            index += 1
        return found

    def _prose(self) -> str:
        """The lesson with code fences and esquema blocks blanked, line numbers kept."""
        hidden = esquema_lines(self.esquemas())
        fenced, kept = False, []
        for number, line in enumerate(self.lines, 1):
            was_fenced = fenced
            fenced ^= bool(_FENCE.match(line))
            kept.append("" if was_fenced or fenced or number in hidden else line)
        return "\n".join(kept)

    def prose_citations(self) -> list[Cited]:
        """Parentheticals holding only inline-code citations, in the prose."""
        prose, found = self._prose(), []
        for match in _CITATION_PARENTHETICAL.finditer(prose):
            refs = parse_refs(match[1])
            line = prose.count("\n", 0, match.start()) + 1
            found += [Cited(ref, line, self.section_at(line)) for ref in refs or []]
        return found

    def malformed_citations(self) -> list[tuple[int, str]]:
        """(line, text) of prose parentheticals with `#` in inline code that do not parse as citations."""
        prose = self._prose()
        return [
            (prose.count("\n", 0, match.start()) + 1, match[1])
            for match in _CITATION_PARENTHETICAL.finditer(prose)
            if "#" in match[1] and parse_refs(match[1]) is None
        ]

    def esquema_citations(self) -> list[Cited]:
        found: list[Cited] = []
        for esquema in self.esquemas():
            for row in esquema.rows:
                found += [Cited(ref, row.line, esquema.title) for ref in parse_refs(row.citation) or []]
        return found

    def judgement_citations(self) -> list[Cited]:
        found: list[Cited] = []
        for number, line in enumerate(self.lines, 1):
            opened = _JUDGEMENT_REF.match(line)
            ref = parse_ref(opened["ref"]) if opened else None
            if ref is not None:
                found.append(Cited(ref, number, self.section_at(number)))
        return found

    def citations(self) -> list[Cited]:
        return [*self.prose_citations(), *self.esquema_citations(), *self.judgement_citations()]

    def fact_sentences(self) -> int:
        """Prose parentheticals (outside Key points and Sources) plus esquema rows: the F facts."""
        prose = self._prose()
        sentences = sum(
            1
            for match in _CITATION_PARENTHETICAL.finditer(prose)
            if parse_refs(match[1])
            and self.section_at(prose.count("\n", 0, match.start()) + 1).lower() not in UNCOUNTED_SECTIONS
        )
        return sentences + sum(len(esquema.rows) for esquema in self.esquemas())

    def snippet_count(self) -> int:
        return len({block.path for block in self.snippet_blocks()})


def read_lessons(course: str, locale: str = LOCALE) -> list[Lesson]:
    folder = course_dir(course) / locale / "lessons"
    return [Lesson(path.stem, path.read_text(encoding="utf-8")) for path in sorted(folder.glob("*.md"))]


def written(lessons: list[Lesson]) -> list[Lesson]:
    return [lesson for lesson in lessons if not lesson.pending]
