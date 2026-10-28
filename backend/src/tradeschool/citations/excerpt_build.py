# SPDX-License-Identifier: AGPL-3.0-only
"""Build time only: every question of a course with its excerpt or the reason it has none.

`scripts/extract_excerpts.py` runs this and writes `excerpts.json`; the tests run it over the fixture
course. PDF pages come from a reader the caller passes (pypdf is a build-time dependency).
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

from tradeschool.citations.excerpt_store import SolvedQuestion, solved_questions
from tradeschool.citations.excerpts import (
    NO_CITATION,
    NO_FACT,
    NO_FILE,
    NO_NORM,
    NO_PARSE,
    NOT_TEXT,
    Block,
    Excerpt,
    NoExcerpt,
    html_blocks,
    norm_excerpt,
    page_excerpt,
    pdf_blocks,
    source_citation,
    text_blocks,
)
from tradeschool.citations.grammar import collapse, parse_segment, segments
from tradeschool.citations.lesson import resolve_segment
from tradeschool.citations.sources import sha256
from tradeschool.content.yaml_file import read_yaml

if TYPE_CHECKING:
    from tradeschool.content.registry import CourseRegistry

OTHER_SOURCES = "sources/otros"
NORM_SOURCES = "sources/normativa"


@dataclass
class SourceText:
    blocks: list[Block]
    title: str = ""


@dataclass
class SourceTexts:
    """Each source file read once, as paragraphs."""

    course_dir: Path
    read_pdf: Callable[[Path], list[str]]
    _read: dict[str, SourceText | None] = field(default_factory=dict)
    digests: dict[str, str] = field(default_factory=dict)

    def get(self, file: str) -> SourceText | None:
        if file not in self._read:
            self._read[file] = self._load(file)
        return self._read[file]

    def _load(self, file: str) -> SourceText | None:
        path = self.course_dir / file
        if not path.is_file():
            return None
        self.digests[file] = sha256(path)
        suffix = path.suffix.lower()
        if suffix == ".pdf":
            return SourceText(pdf_blocks(self.read_pdf(path)))
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:  # a page saved in its site's legacy encoding
            text = raw.decode("cp1252", errors="replace")
        if suffix in (".html", ".htm", ".xml"):
            blocks, title = html_blocks(text)
            return SourceText(blocks, title)
        return SourceText(text_blocks(text))


def _attributions(course_dir: Path) -> dict[str, str]:
    """A saved page's title and consultation date, from `sources/otros/fuentes.yaml` when it lists it."""
    raw = (
        read_yaml(course_dir / OTHER_SOURCES / "fuentes.yaml")
        if (course_dir / OTHER_SOURCES / "fuentes.yaml").exists()
        else None
    )
    entries = raw.get("fuentes", []) if isinstance(raw, dict) else []
    out: dict[str, str] = {}
    for entry in entries:
        if isinstance(entry, dict) and entry.get("file") and entry.get("title"):
            dated = f", consultado el {entry['consultado']}" if entry.get("consultado") else ""
            out[f"{OTHER_SOURCES}/{entry['file']}"] = f"{entry['title']}{dated}"
    return out


def excerpt_for(
    registry: CourseRegistry, texts: SourceTexts, attributions: dict[str, str], question: SolvedQuestion
) -> Excerpt | NoExcerpt:
    citation = collapse(question.citation or "")
    if not citation:
        return NoExcerpt(NO_CITATION)
    if (cited := source_citation(citation)) is not None:
        # A `fuente:` may name a norm's own file, kept with the norms.
        file = next(
            (
                f"{folder}/{cited.file}"
                for folder in (OTHER_SOURCES, NORM_SOURCES)
                if texts.get(f"{folder}/{cited.file}")
            ),
            f"{OTHER_SOURCES}/{cited.file}",
        )
        source = texts.get(file)
        if source is None:
            return NoExcerpt(NO_FILE)
        title = source.title or cited.file
        return page_excerpt(
            source.blocks, cited.label, question.explanation, file, attributions.get(file, title), title
        )
    pieces = [parse_segment(text) for _, text in segments(citation)]
    segment = next((piece for piece in pieces if piece is not None), None)
    norms = registry.citations.norms
    if segment is None or not segment.units or norms is None:
        return NoExcerpt(NO_PARSE)
    named = resolve_segment(segment, norms)
    norm = named[0] if named else None
    if norm is None:
        return NoExcerpt(NO_NORM)
    if norm.file is None:
        return NoExcerpt(NO_FILE)
    source = texts.get(norm.file)
    if source is None:
        return NoExcerpt(NO_FILE)
    if not source.blocks:
        return NoExcerpt(NOT_TEXT)
    index = registry.citations.sources
    entry = index.files.get(norm.file)
    units = entry.get("units") if isinstance(entry, dict) else None
    place = units.get(segment.units[0].slug) if isinstance(units, dict) else None
    fragment = index.fragment(norm.file, segment.units[0])
    return norm_excerpt(source.blocks, segment, norm.file, place, fragment, question.explanation)


EXCLUSIONS_FILE = "excerpt-exclusions.yaml"


def _exclusions(course_dir: Path) -> set[str]:
    """Questions a blind verifier found no citable sentence for: built as «sin extracto» (`no-fact`)."""
    path = course_dir / EXCLUSIONS_FILE
    raw = read_yaml(path) if path.exists() else None
    entries = raw.get("questions", []) if isinstance(raw, dict) else []
    return {str(entry["question"]) for entry in entries if isinstance(entry, dict) and entry.get("question")}


def build_excerpts(registry: CourseRegistry, texts: SourceTexts) -> dict[str, object]:
    """`excerpts.json`: per question key its citation and excerpt (or `none`: the reason), and the
    digest of every source read, so a changed source is caught."""
    attributions = _attributions(texts.course_dir)
    excluded = _exclusions(texts.course_dir)
    questions: dict[str, object] = {}
    for question in solved_questions(registry.manifest, registry.exercise_configs, registry.languages[0]):
        found = excerpt_for(registry, texts, attributions, question)
        if question.key in excluded and isinstance(found, Excerpt):
            found = NoExcerpt(NO_FACT, found.file, found.fragment)
        entry: dict[str, object] = {"citation": collapse(question.citation or "")}
        if isinstance(found, Excerpt):
            entry["excerpt"] = found.as_json()
        else:
            entry["none"] = found.reason
            if found.file:
                entry["source"] = {"file": found.file, "fragment": found.fragment}
        questions[question.key] = entry
    return {"sources": dict(sorted(texts.digests.items())), "questions": questions}
