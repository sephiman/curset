# SPDX-License-Identifier: AGPL-3.0-only
"""Where a cited unit opens in its source: the page of a PDF, the anchor of an HTML page.

The page index is built once, at generation time, by `scripts/index_sources.py` into the course's
`source-index.json` (sha256 per file, so a stale index is caught); serving only reads it. A unit is
found by the heading the consolidated text prints for it: «Artículo 67.», «Disposición adicional
cuarta.», «Preámbulo», «ANEXO I», «Regla 34.», «Sexto.» (an apartado of an orden). An annex's notes
(«34. Fecha del gasto: …») are its numbered lines in an unbroken run from 1.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from tradeschool.citations.grammar import LATIN, ORDINAL_WORD, Unit, slug

INDEX_FILE = "source-index.json"
SERVED_FOLDERS = ("normativa", "otros")

_HEADINGS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(rf"^\s*Art[íi]culo\s+(\d+)(?:\s+({LATIN}))?\b"), "art"),
    # Older laws spell the number out: «Artículo treinta y tres.», «Artículo decimoquinto.».
    (
        re.compile(
            rf"^\s*Art[íi]culo\s+([a-záéíóúñ]+(?:\s+(?:y\s+)?(?!{LATIN}\b)[a-záéíóúñ]+){{0,3}})(?:\s+({LATIN}))?\s*\."
        ),
        "spelled",
    ),
    (
        re.compile(
            r"^\s*Disposici[óo]n\s+(adicional|transitoria|final|derogatoria)"
            r"(?:\s+((?:vig|trig|cuadrag)[ée]sim[ao]\s+[a-záéíóúñ]+|[a-záéíóúñ]+|\d+))?\b",
            re.I,
        ),
        "disp",
    ),
    (re.compile(r"^\s*(PRE[ÁA]MBULO|Pre[áa]mbulo)\b"), "preambulo"),
    (re.compile(r"^\s*ANEXO(?:\s+([IVXL]+|\d+|ÚNICO))?\b"), "anexo"),
    (re.compile(rf"^\s*Regla\s+(\d+)(?:\s+({LATIN}))?\."), "regla"),
    (re.compile(rf"^\s*({ORDINAL_WORD})\.\s+[A-ZÁÉÍÓÚ]", re.I), "apartado"),
)
_DISPOSICION = {"adicional": "da", "transitoria": "dt", "final": "df", "derogatoria": "dd"}
# An index page lists its entries with dot leaders and a page number; its headings are not the units.
_LEADER = re.compile(r"(\.\s?){4,}\s*\d+\s*$")
_NUMBERED_LINE = re.compile(r"^\s*(\d{1,3})\.\s")


# Accents dropped: «veintidós», «décimo» and «vigésimo» are looked up as «veintidos», «decimo», «vigesimo».
_NUMBER_WORDS = {
    "uno": 1, "primero": 1, "dos": 2, "segundo": 2, "tres": 3, "tercero": 3, "cuatro": 4, "cuarto": 4,
    "cinco": 5, "quinto": 5, "seis": 6, "sexto": 6, "siete": 7, "septimo": 7, "ocho": 8, "octavo": 8,
    "nueve": 9, "noveno": 9, "diez": 10, "decimo": 10, "once": 11, "undecimo": 11, "doce": 12,
    "duodecimo": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciseis": 16, "diecisiete": 17,
    "dieciocho": 18, "diecinueve": 19, "veinte": 20, "vigesimo": 20, "treinta": 30, "trigesimo": 30,
    "cuarenta": 40, "cuadragesimo": 40, "cincuenta": 50, "quincuagesimo": 50, "sesenta": 60,
    "sexagesimo": 60, "setenta": 70, "septuagesimo": 70, "ochenta": 80, "octogesimo": 80, "noventa": 90,
    "nonagesimo": 90, "cien": 100, "ciento": 100, "centesimo": 100,
}  # fmt: skip
# Compounds written as one word: «veintitrés», «decimoquinto», «vigesimoprimero».
_PREFIXES = (("veinti", 20), ("decimo", 10), ("vigesimo", 20), ("trigesimo", 30))


def _word_number(word: str) -> int | None:
    if word in _NUMBER_WORDS:
        return _NUMBER_WORDS[word]
    for prefix, value in _PREFIXES:
        rest = _NUMBER_WORDS.get(word.removeprefix(prefix)) if word.startswith(prefix) else None
        if rest is not None and rest < 10:
            return value + rest
    return None


def _compound_ordinal(ordinal: str) -> str:
    """«vigésima sexta» as a citation writes it: «vigesimosexta»."""
    if " " not in ordinal:
        return ordinal
    tens, unit = ordinal.split()
    return tens.replace("é", "e")[:-1] + "o" + unit


def spelled_number(words: str) -> int | None:
    """«treinta y tres» → 33, «decimoquinto» → 15, «ciento dos» → 102; None when a word is not a number."""
    total = 0
    for word in slug(words).split("-"):
        if word == "y":
            continue
        value = _word_number(word)
        if value is None:
            return None
        total += value
    return total or None


def heading_unit(line: str) -> Unit | None:
    """The unit a heading line opens, if it is one."""
    for pattern, kind in _HEADINGS:
        match = pattern.match(line)
        if match is None:
            continue
        if kind == "art":
            return Unit("art", f"{match[1]} {match[2]}" if match[2] else match[1])
        if kind == "spelled":
            number = spelled_number(match[1])
            if number is None:
                continue
            return Unit("art", f"{number} {match[2]}" if match[2] else str(number))
        if kind == "disp":
            ordinal = _compound_ordinal((match[2] or "").lower())
            return Unit(_DISPOSICION[match[1].lower()], "" if ordinal in ("de", "del") else ordinal)
        if kind == "anexo":
            return Unit("anexo", (match[1] or "").lower())
        if kind == "regla":
            return Unit("regla", f"{match[1]} {match[2]}" if match[2] else match[1])
        if kind == "apartado":
            return Unit("apartado", match[1].lower())
        return Unit("preambulo")
    return None


def index_pdf_pages(pages: list[str]) -> dict[str, int]:
    """unit slug → first page (1-based) whose body opens it; index pages are skipped."""
    units: dict[str, int] = {}
    annex: Unit | None = None
    next_note = 1
    for number, text in enumerate(pages, start=1):
        lines = text.splitlines()
        if sum(1 for line in lines if _LEADER.search(line)) >= 3:
            continue
        for line in lines:
            unit = heading_unit(line)
            if unit is not None:
                units.setdefault(unit.slug, number)
                annex, next_note = (unit, 1) if unit.kind == "anexo" else (annex, next_note)
                continue
            note = _NUMBERED_LINE.match(line)
            if annex is not None and note is not None and int(note[1]) == next_note:
                units.setdefault(Unit("nota", note[1], annex).slug, number)
                next_note += 1
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
