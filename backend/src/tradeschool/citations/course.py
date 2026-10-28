# SPDX-License-Identifier: AGPL-3.0-only
"""A course's citations: every lesson scanned once at load, the links shipped with a lesson, the anchor a
question opens at, and the cross-reference checks.

A course with `sources/normativa.yaml` gets citation links; one without gets none, and its lessons are
not scanned unless an esquema needs checking. The checks fail the load, naming the question or the row:

* a question's citation must resolve to an anchor in its own lesson;
* an esquema row needs a citation, and what it cites must also be cited in the same lesson's prose.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path

from tradeschool.citations.grammar import Segment, collapse, parse_segment, segments, slug
from tradeschool.citations.lesson import LessonCitation, LessonCitations, resolve_segment, scan_lesson
from tradeschool.citations.norms import NormIndex
from tradeschool.citations.sources import SourceIndex, source_url
from tradeschool.content.esquema import EsquemaError, parse_esquemas

NORMATIVA = Path("sources") / "normativa.yaml"


@dataclass(frozen=True)
class CitedQuestion:
    """A question that carries a citation, and the lesson that must cite the same thing."""

    label: str  # `exercise/variant` or `case/question`, for the check's message
    lesson_id: str
    citation: str


@dataclass(frozen=True)
class QuestionLink:
    lesson_id: str
    #: The lesson anchor of the cited article; None opens the lesson at its top.
    anchor: str | None
    citation: str | None


@dataclass
class CourseCitations:
    slug: str
    norms: NormIndex | None
    sources: SourceIndex
    #: locale → lesson id → its citations, for the lessons that were scanned.
    lessons: dict[str, dict[str, LessonCitations]] = field(default_factory=dict)

    @property
    def links(self) -> bool:
        """Only a course that keeps its norms links citations to them."""
        return self.norms is not None

    @classmethod
    def build(cls, course_dir: Path, slug: str, markdown: dict[str, dict[str, str]]) -> CourseCitations:
        normativa = course_dir / NORMATIVA
        prose = [body for lessons in markdown.values() for body in lessons.values()]
        norms = NormIndex.load(normativa, prose) if normativa.exists() else None
        built = cls(slug, norms, SourceIndex.load(course_dir) if norms else SourceIndex())
        scan_with = norms or NormIndex([], {})
        for locale, lessons in markdown.items():
            for lesson_id, body in lessons.items():
                try:
                    if norms is None and not parse_esquemas(body):
                        continue
                    built.lessons.setdefault(locale, {})[lesson_id] = scan_lesson(lesson_id, body, scan_with)
                except EsquemaError as exc:
                    raise ValueError(f"lesson {lesson_id} ({locale}): {exc}") from exc
        return built

    def lesson(self, lesson_id: str, locale: str) -> LessonCitations | None:
        return self.lessons.get(locale, {}).get(lesson_id)

    # --- links -----------------------------------------------------------------------------------
    def _href(self, citation: LessonCitation) -> str | None:
        if citation.source_file is not None:
            return source_url(self.slug, citation.source_file)
        norm = citation.norm
        if norm is None or norm.file is None:
            return None
        fragment = self.sources.fragment(norm.file, citation.units[0]) if citation.units else ""
        return source_url(self.slug, norm.file) + fragment

    def _title(self, citation: LessonCitation) -> str | None:
        if citation.norm is None:
            return None
        dated = (
            f" (texto consolidado a {citation.norm.consolidated_as_of})"
            if citation.norm.consolidated_as_of
            else ""
        )
        return f"{citation.norm.title}{dated}"

    def lesson_payload(self, lesson_id: str, locale: str) -> list[dict[str, object]]:
        """What the web marks in a lesson: each citation's exact text, its DOM ids and where it opens."""
        found = self.lesson(lesson_id, locale) if self.links else None
        if found is None:
            return []
        return [
            {
                "text": citation.text,
                "section": citation.section,
                "ids": list(ids),
                "href": self._href(citation),
                "title": self._title(citation),
            }
            for citation, ids in zip(found.items, found.first_ids(), strict=True)
        ]

    def normativa_payload(self, lesson_id: str, locale: str) -> list[dict[str, object]]:
        """The «Normativa» block's norms with title and consolidation date — what the PDF prints."""
        found = self.lesson(lesson_id, locale) if self.links else None
        return [
            {
                "name": c.text,
                "title": c.norm.title if c.norm else None,
                "consolidatedAsOf": c.norm.consolidated_as_of if c.norm else None,
            }
            for c in (found.items if found else [])
            if c.section == "normativa"
        ]

    def question_link(self, lesson_id: str, citation: str | None, locale: str) -> QuestionLink:
        if not citation or not self.links:
            return QuestionLink(lesson_id, None, citation)
        return QuestionLink(lesson_id, self._anchor(lesson_id, citation, locale), citation)

    def _anchor(self, lesson_id: str, citation: str, locale: str) -> str | None:
        segment = parse_segment(citation) or _labelled_source(citation)
        found = self.lesson(lesson_id, locale)
        if segment is not None and found is not None and segment.files:
            return _source_anchor(found, segment.files)
        named = resolve_segment(segment, self.norms or NormIndex([], {})) if segment else None
        if segment is None or found is None or named is None:
            return None
        for unit in segment.units:
            if anchor := found.anchor_for(named[1], unit):
                return anchor
        return None

    # --- checks ----------------------------------------------------------------------------------
    def problems(self, questions: Iterable[CitedQuestion], locale: str) -> list[str]:
        problems: list[str] = []
        for question in questions:
            if self.links and self._anchor(question.lesson_id, question.citation, locale) is None:
                problems.append(
                    f"question {question.label} cites «{collapse(question.citation)}», "
                    f"which its lesson {question.lesson_id} never cites"
                )
        for lesson_id, found in self.lessons.get(locale, {}).items():
            problems += _esquema_problems(lesson_id, found, self.norms or NormIndex([], {}))
        return problems


def _labelled_source(citation: str) -> Segment | None:
    """The file segment of a `fuente:` citation with the page's label after it («fuente: `f`; «Abrir»»)."""
    pieces = segments(citation)
    first = parse_segment(pieces[0][1]) if pieces else None
    return first if first is not None and first.files else None


def _source_anchor(found: LessonCitations, files: tuple[str, ...]) -> str | None:
    """The first cited file's anchor, when the lesson's prose cites that file."""
    wanted = {f"fuente-{slug(file)}" for file in files}
    for citation in found.prose:
        for anchor in citation.anchors:
            if anchor in wanted:
                return anchor
    return None


def _esquema_problems(lesson_id: str, found: LessonCitations, norms: NormIndex) -> list[str]:
    problems: list[str] = []
    for esquema in found.esquemas:
        for row in esquema.rows:
            row_text = " — ".join(row.fields)
            where = f"lesson {lesson_id} line {row.line}, esquema «{esquema.title}», row «{row_text}»"
            segment: Segment | None = parse_segment(row.citation) if row.citation else None
            named = resolve_segment(segment, norms) if segment else None
            if segment is None or named is None:
                problems.append(f"{where}: no citation (norm and article)")
                continue
            missing = [unit for unit in segment.units if found.anchor_for(named[1], unit) is None]
            if missing:
                problems.append(f"{where}: cites «{segment.text}», which the lesson's prose never cites")
    return problems
