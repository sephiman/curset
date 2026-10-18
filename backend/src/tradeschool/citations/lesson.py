# SPDX-License-Identifier: AGPL-3.0-only
"""A lesson's citations in reading order, the anchors they give it, and where a question's citation lands.

Three sections are read apart. Prose citations are the parentheticals of the text; one that names no
norm (an `arts.` range with nothing after it) takes the norm of the prose citation before it. Esquema
rows carry their own citation, which must name its norm. The closing «Normativa» block links each norm
it lists, by the name written before the colon. Headings and code are not read: the web cannot mark
text there either.

An anchor is `<norm slug>-<unit>` (`ce-art-67`, `ley-19-2013-da-cuarta`) or `fuente-<file>`. The first
prose citation of an anchor carries it; a question citing the same unit opens the lesson there.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Literal

from tradeschool.citations.grammar import (
    Segment,
    Unit,
    collapse,
    parentheticals,
    parse_segment,
    segments,
    slug,
)
from tradeschool.citations.norms import Norm, NormIndex
from tradeschool.content.esquema import Esquema, esquema_lines, parse_esquemas

Section = Literal["prose", "esquema", "normativa"]

_HEADING = re.compile(r"^#{1,6}\s")
_FENCE = re.compile(r"^(```|~~~)")
_DIRECTIVE_FENCE = re.compile(r"^:{2,}")
_NORMATIVA = re.compile(r"^##\s+Normativa\s*$")
_NORMATIVA_ITEM = re.compile(r"^-\s+(?P<norm>[^:\n]+?):\s")
_OTHER_SOURCES = "sources/otros"


@dataclass(frozen=True)
class LessonCitation:
    section: Section
    #: As the reader sees it: whitespace collapsed, no backticks. The web marks exactly this text.
    text: str
    line: int
    norm: Norm | None = None
    #: The resolved norm's slug, or the slug of the name as written when no norm answers to it.
    norm_slug: str = ""
    #: The norm was not written here: it is the previous prose citation's.
    implicit: bool = False
    units: tuple[Unit, ...] = ()
    ranges: tuple[tuple[int, int], ...] = ()
    #: A `fuente:` file, course-relative (`sources/otros/…`).
    source_file: str | None = None

    @property
    def anchors(self) -> tuple[str, ...]:
        if self.source_file is not None:
            return (f"fuente-{slug(self.source_file.rsplit('/', 1)[-1])}",)
        prefix = f"{self.norm_slug}-" if self.norm_slug else ""
        return tuple(f"{prefix}{unit.slug}" for unit in self.units)

    def covers(self, norm_slug: str, unit: Unit) -> bool:
        """Whether this citation cites `unit` of the norm, by name or inside an `arts.` range."""
        if self.norm_slug != norm_slug:
            return False
        if unit in self.units:
            return True
        number = unit.number.split(" ")[0]
        return (
            unit.kind == "art" and number.isdigit() and any(lo <= int(number) <= hi for lo, hi in self.ranges)
        )


@dataclass
class LessonCitations:
    lesson_id: str
    items: list[LessonCitation] = field(default_factory=list)
    esquemas: list[Esquema] = field(default_factory=list)

    @property
    def prose(self) -> list[LessonCitation]:
        return [c for c in self.items if c.section == "prose"]

    def first_ids(self) -> list[tuple[str, ...]]:
        """Per item, the anchors it is the first prose citation of — the DOM ids the web gives it."""
        seen: set[str] = set()
        out: list[tuple[str, ...]] = []
        for item in self.items:
            if item.section != "prose":
                out.append(())
                continue
            fresh = tuple(anchor for anchor in item.anchors if anchor not in seen)
            seen.update(fresh)
            out.append(fresh)
        return out

    def anchor_for(self, norm_slug: str, unit: Unit) -> str | None:
        """The anchor a cited unit opens at: its own, or the first prose citation whose range holds it."""
        own = f"{norm_slug}-{unit.slug}"
        prose = self.prose
        if any(own in c.anchors for c in prose):
            return own
        for citation in prose:
            if citation.covers(norm_slug, unit):
                return citation.anchors[0]
        return None


def resolve_segment(segment: Segment, index: NormIndex) -> tuple[Norm | None, str] | None:
    """(norm, slug) for the norm a segment names — the slug of the written name when no norm answers —
    or None when it names none (a bare qualifier such as «, accesibilidad universal» is not a norm)."""
    written = segment.norm_text
    if written.startswith(","):
        written = written.rsplit(",", 1)[1].strip()
        norm = index.resolve(written) if written else None
        return (norm, norm.slug) if norm is not None else None
    if not written:
        return None
    norm = index.resolve(written)
    return (norm, norm.slug) if norm is not None else (None, slug(written.split(",")[0]))


def _line_of(offsets: list[int], position: int) -> int:
    line = 0
    while line + 1 < len(offsets) and offsets[line + 1] <= position:
        line += 1
    return line


def _prose_chunks(lines: list[str], skip: set[int]) -> list[tuple[int, str]]:
    """Runs of readable lines as (first line number, text), split at everything the scan must not read."""
    chunks: list[tuple[int, str]] = []
    current: list[str] = []
    start = 0
    in_code = False

    def flush() -> None:
        if current:
            chunks.append((start, "\n".join(current)))
            current.clear()

    for number, line in enumerate(lines, start=1):
        if _FENCE.match(line.strip()):
            in_code = not in_code
            flush()
            continue
        if in_code or number in skip or _HEADING.match(line) or _DIRECTIVE_FENCE.match(line):
            flush()
            continue
        if not current:
            start = number
        current.append(line)
    flush()
    return chunks


def _normativa_lines(lines: list[str]) -> set[int]:
    inside = False
    found: set[int] = set()
    for number, line in enumerate(lines, start=1):
        if _NORMATIVA.match(line):
            inside = True
            continue
        if inside and re.match(r"^#{1,2}\s", line):
            inside = False
        if inside:
            found.add(number)
    return found


def scan_lesson(lesson_id: str, markdown: str, index: NormIndex) -> LessonCitations:
    lines = markdown.splitlines()
    esquemas = parse_esquemas(markdown)
    normativa = _normativa_lines(lines)
    found: list[tuple[int, int, LessonCitation]] = []

    previous: tuple[Norm | None, str] = (None, "")
    for first_line, chunk in _prose_chunks(lines, esquema_lines(esquemas) | normativa):
        offsets = [0] + [m.end() for m in re.finditer("\n", chunk)]
        for paren in parentheticals(chunk):
            for offset, piece in segments(paren.inner):
                segment = parse_segment(piece)
                if segment is None:
                    continue
                position = paren.start + offset
                line = first_line + _line_of(offsets, position)
                if segment.files:
                    for file in segment.files:
                        citation = LessonCitation("prose", file, line, source_file=f"{_OTHER_SOURCES}/{file}")
                        found.append((line, position, citation))
                    continue
                named = resolve_segment(segment, index)
                implicit = named is None
                norm, norm_slug = previous if named is None else named
                previous = (norm, norm_slug)
                text = collapse(segment.text)
                citation = LessonCitation(
                    "prose", text, line, norm, norm_slug, implicit, segment.units, segment.ranges
                )
                found.append((line, position, citation))

    for esquema in esquemas:
        for row in esquema.rows:
            segment = parse_segment(row.citation) if row.citation else None
            if segment is None:
                continue
            norm, norm_slug = resolve_segment(segment, index) or (None, "")
            citation = LessonCitation(
                "esquema",
                collapse(segment.text),
                row.line,
                norm,
                norm_slug,
                False,
                segment.units,
                segment.ranges,
            )
            found.append((row.line, 0, citation))

    for number in sorted(normativa):
        item = _NORMATIVA_ITEM.match(lines[number - 1])
        if item is None:
            continue
        written = collapse(item["norm"])
        norm = index.resolve(written)
        found.append(
            (number, 0, LessonCitation("normativa", written, number, norm, norm.slug if norm else ""))
        )

    found.sort(key=lambda entry: (entry[0], entry[1]))
    return LessonCitations(lesson_id, [citation for _, _, citation in found], esquemas)
