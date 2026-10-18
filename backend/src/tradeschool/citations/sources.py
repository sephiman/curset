# SPDX-License-Identifier: AGPL-3.0-only
"""Where a cited unit opens in its source: the page of a PDF, the anchor of an HTML page.

The page index is built once, at generation time, by `scripts/index_sources.py` into the course's
`source-index.json` (sha256 per file, so a stale index is caught); serving only reads it. A unit is
found by the heading the consolidated text prints for it: «Artículo 67.», «Disposición adicional
cuarta.», «Preámbulo», «ANEXO I».
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from tradeschool.citations.grammar import LATIN, Unit

INDEX_FILE = "source-index.json"
SERVED_FOLDERS = ("normativa", "otros")

_HEADINGS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(rf"^\s*Art[íi]culo\s+(\d+)(?:\s+({LATIN}))?\b"), "art"),
    (
        re.compile(
            r"^\s*Disposici[óo]n\s+(adicional|transitoria|final|derogatoria)(?:\s+([a-záéíóúñ]+|\d+))?\b",
            re.I,
        ),
        "disp",
    ),
    (re.compile(r"^\s*(PRE[ÁA]MBULO|Pre[áa]mbulo)\b"), "preambulo"),
    (re.compile(r"^\s*ANEXO(?:\s+([IVXL]+|\d+|ÚNICO))?\b"), "anexo"),
)
_DISPOSICION = {"adicional": "da", "transitoria": "dt", "final": "df", "derogatoria": "dd"}
# An index page lists its entries with dot leaders and a page number; its headings are not the units.
_LEADER = re.compile(r"(\.\s?){4,}\s*\d+\s*$")


def heading_unit(line: str) -> Unit | None:
    """The unit a heading line opens, if it is one."""
    for pattern, kind in _HEADINGS:
        match = pattern.match(line)
        if match is None:
            continue
        if kind == "art":
            return Unit("art", f"{match[1]} {match[2]}" if match[2] else match[1])
        if kind == "disp":
            ordinal = (match[2] or "").lower()
            return Unit(_DISPOSICION[match[1].lower()], "" if ordinal in ("de", "del") else ordinal)
        if kind == "anexo":
            return Unit("anexo", (match[1] or "").lower())
        return Unit("preambulo")
    return None


def index_pdf_pages(pages: list[str]) -> dict[str, int]:
    """unit slug → first page (1-based) whose body opens it; index pages are skipped."""
    units: dict[str, int] = {}
    for number, text in enumerate(pages, start=1):
        lines = text.splitlines()
        if sum(1 for line in lines if _LEADER.search(line)) >= 3:
            continue
        for line in lines:
            unit = heading_unit(line)
            if unit is not None:
                units.setdefault(unit.slug, number)
    return units


_HTML_BLOCK = re.compile(r'id="(?P<id>[^"]+)"(?P<after>.{0,600}?)<h5[^>]*>(?P<head>[^<]+)', re.S)


def index_html(html: str) -> dict[str, str]:
    """unit slug → the element id a BOE page gives the block that opens it."""
    units: dict[str, str] = {}
    for match in _HTML_BLOCK.finditer(html):
        if "id=" in match["after"]:
            continue  # the heading belongs to a later block
        unit = heading_unit(match["head"])
        if unit is not None:
            units.setdefault(unit.slug, match["id"])
    return units


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@dataclass
class SourceIndex:
    """file (course-relative) → its digest and where each unit starts."""

    files: dict[str, dict[str, object]] = field(default_factory=dict)

    @classmethod
    def load(cls, course_dir: Path) -> SourceIndex:
        path = course_dir / INDEX_FILE
        if not path.exists():
            return cls()
        raw = json.loads(path.read_text(encoding="utf-8"))
        return cls(dict(raw.get("files", {})))

    def fragment(self, file: str, unit: Unit) -> str:
        """`#page=N` for a PDF, `#<id>` for an HTML page; empty when the index does not place it."""
        entry = self.files.get(file)
        units = entry.get("units") if isinstance(entry, dict) else None
        place = units.get(unit.slug) if isinstance(units, dict) else None
        if place is None:
            return ""
        return f"#page={place}" if file.lower().endswith(".pdf") else f"#{place}"


def source_url(course: str, file: str) -> str:
    """The URL the platform serves a course source at; `file` is course-relative (`sources/…`)."""
    return f"/api/courses/{course}/{file}"
