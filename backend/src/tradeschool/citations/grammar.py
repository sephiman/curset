# SPDX-License-Identifier: AGPL-3.0-only
"""The citation grammar: what a parenthetical such as «(art. 14.2.d) y e) LPAC)» cites, as written.

This is the ONE parser of citations. The web never detects a citation: the backend ships each lesson's
citations with their exact text and the annotator marks those spans (see `lib/citations/annotate.ts`).

A parenthetical is split at top-level «;» into segments. A segment cites when it starts with a lead —
`art.`/`arts.`, `disposición …`, `DA`/`DT`/`DF`/`DD`, `anexo`, `apartado(s)`, `preámbulo` or
`fuente:` — and anything else in it («m05-l05», «no toca los artículos citados») is prose.

Articles: under a singular `art.` the first number is THE article and what follows is its paragraphs,
letters and ordinals («14.2.d) y e)» is article 14); a later `art.` starts another. Under `arts.`
every listed number is an article and two numbers joined by an en dash are a range. An article keeps a
Latin suffix written right after its number («610 bis.2» is article 610 bis; «12.2 bis» is article 12).
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field

LATIN = r"(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies)"
# A disposición's ordinal is one lowercase word («cuarta», «vigesimoctava», «única») or a number.
_ORDINAL = r"(?!(?:de|del|la|los|las|y|e)\b)[a-záéíóúñ]+|\d+(?:\.ª)?"
# What may follow a unit before the norm: «.1», «.4.a)», « b) y f)».
_SUB = r"(?:\.(?:\d+|[a-zñ]\)?|[A-Z]\b)|\s[a-zñ]\)(?:\s+[ye]\s+[a-zñ]\))*)*"
_SPELLED = r"(?:Uno|Dos|Tres|Cuatro|Cinco|Seis|Siete|Ocho|Nueve|Diez|Once|Doce)"

# One article designator: 14 · 14.2 · 4.1.b) · 148.1.8.ª · 610 bis.2 · 12.2 bis · 61.ñ — or a bare letter
# paragraph continuing the article before it («e)» in «14.2.d) y e)»).
_ITEM = (
    rf"(?:\d+(?:\s{LATIN}\b)?(?:\.(?:\d+|[a-zñ]\)?|[A-Z]\b|{_SPELLED}\b|[ºª])|\s{LATIN}\b|[ºª])*\)?"
    r"|[a-zñ]\))"
)
# The en dash (U+2013) is how the lessons write a range; a hyphen is accepted too.
_DASH = "[\u2013-]"
_SEP = rf"(?:\s*,\s*|\s+[ye]\s+|\s*{_DASH}\s*)"
_ARTICLE_SEGMENT = re.compile(
    rf"^(?P<lead>arts?\.)\s+(?P<designators>{_ITEM}(?:{_SEP}(?:arts?\.\s+)?{_ITEM})*)(?P<rest>.*)$", re.DOTALL
)
_ITEM_OR_SEP = re.compile(rf"(?P<sep>{_SEP})?(?P<art>arts?\.\s+)?(?P<item>{_ITEM})")
_ARTICLE_NUMBER = re.compile(rf"^(\d+)(?:\s({LATIN})\b)?")

_KIND = {"adicional": "da", "transitoria": "dt", "final": "df", "derogatoria": "dd"}
_DISPOSICION = re.compile(
    r"^disposici(?:ón|ones)\s+(?P<kind>adicional|transitoria|final|derogatoria)(?:es)?"
    rf"(?:\s+(?P<ord>{_ORDINAL})\b{_SUB})?(?P<rest>.*)$",
    re.DOTALL,
)
_DISPOSICION_SHORT = re.compile(r"^(?P<kind>DA|DT|DF|DD)\s+(?P<ord>\d+|\w+)\b(?P<rest>.*)$", re.DOTALL)
_ANEXO = re.compile(r"^anexo(?:\s+(?P<num>[IVXL]+|\d+|único)\b)?(?P<rest>.*)$", re.DOTALL)
_APARTADO = re.compile(
    rf"^apartados?\s+(?P<num>\d+){_SUB}(?:{_DASH}\d+{_SUB})?(?:\s+(?:y|a)\s+\d+{_SUB})?(?P<rest>.*)$",
    re.DOTALL,
)
# «art. 205.1.a) y disposición transitoria séptima LGSS»: one norm, two units.
_AND_MORE = re.compile(r"^\s*(?:,|y|e)\s+(?=disposici|anexo|apartado)")
_PREAMBULO = re.compile(r"^preámbulo\b(?P<rest>.*)$", re.DOTALL)
_SOURCE = re.compile(r"^fuente:\s*(?P<files>`[^`]+`(?:\s*(?:,|y)\s*`[^`]+`)*)\s*$", re.DOTALL)
_SOURCE_FILE = re.compile(r"`([^`]+)`")

#: How a parenthetical has to start for it to be read as a citation at all.
LEAD = re.compile(
    r"^(?:arts?\.\s|disposici(?:ón|ones)\s|D[ATFD]\s\w|anexo\b|apartados?\s|preámbulo\b|fuente:)"
)
_CONNECTOR = re.compile(r"^(?:del|de\s+la|de\s+los|de)\s+", re.IGNORECASE)


def slug(text: str) -> str:
    """ASCII, lowercase, hyphen-joined: «Ley 19/2013» → `ley-19-2013`, «única» → `unica`."""
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")


def collapse(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class Unit:
    """One thing cited inside a norm: `art`/`da`/`dt`/`df`/`dd`/`anexo`/`apartado`/`preambulo`."""

    kind: str
    number: str = ""

    @property
    def slug(self) -> str:
        return f"{self.kind}-{slug(self.number)}" if self.number else self.kind


@dataclass(frozen=True)
class Segment:
    """A citing segment as written: what it cites and the norm text it names (empty: none named)."""

    text: str
    units: tuple[Unit, ...] = ()
    #: Article ranges cited by `arts. a` en dash `b`, as (first, last).
    ranges: tuple[tuple[int, int], ...] = ()
    norm_text: str = ""
    #: A `fuente:` segment cites files, not a norm.
    files: tuple[str, ...] = ()


@dataclass
class _Articles:
    units: list[Unit] = field(default_factory=list)
    ranges: list[tuple[int, int]] = field(default_factory=list)


def _article_number(item: str) -> str | None:
    match = _ARTICLE_NUMBER.match(item)
    if match is None:
        return None
    return f"{match[1]} {match[2]}" if match[2] else match[1]


def _articles(lead: str, designators: str) -> _Articles:
    plural = lead == "arts."
    found = _Articles()
    previous: str | None = None
    for match in _ITEM_OR_SEP.finditer(designators):
        number = _article_number(match["item"])
        starts_article = previous is None or plural or match["art"] is not None
        if number is None or not starts_article:
            continue
        sep = match["sep"] or ""
        if (
            plural
            and previous is not None
            and sep.strip() in ("\u2013", "-")
            and previous.isdigit()
            and number.isdigit()
        ):
            found.ranges.append((int(previous), int(number)))
        if Unit("art", number) not in found.units:
            found.units.append(Unit("art", number))
        previous = number
    return found


def _norm_text(rest: str) -> str:
    """The norm named after the units, connectors dropped; empty when none is named.

    A qualifier may sit between the units and the norm («cuarta.1, párrafo segundo, TREBEP»); the text
    then starts with a comma and is kept whole, for resolution to try what follows the last one.
    """
    text = collapse(rest)
    return text if text.startswith(",") else _CONNECTOR.sub("", text)


def parse_segment(raw: str) -> Segment | None:
    """The segment's citation, or None when it does not start with a lead."""
    text = collapse(raw)
    if not LEAD.match(text):
        return None
    if source := _SOURCE.match(text):
        return Segment(text, files=tuple(_SOURCE_FILE.findall(source["files"])))
    if article := _ARTICLE_SEGMENT.match(text):
        found = _articles(article["lead"], article["designators"])
        if not found.units:
            return None
        rest = article["rest"]
        if more := _AND_MORE.match(rest):
            other = parse_segment(rest[more.end() :])
            if other is not None:
                return Segment(text, tuple(found.units) + other.units, tuple(found.ranges), other.norm_text)
        return Segment(text, tuple(found.units), tuple(found.ranges), _norm_text(rest))
    if disposicion := _DISPOSICION.match(text):
        unit = Unit(_KIND[disposicion["kind"]], disposicion["ord"] or "")
        return Segment(text, (unit,), norm_text=_norm_text(disposicion["rest"]))
    if short := _DISPOSICION_SHORT.match(text):
        return Segment(
            text, (Unit(short["kind"].lower(), short["ord"]),), norm_text=_norm_text(short["rest"])
        )
    if anexo := _ANEXO.match(text):
        return Segment(text, (Unit("anexo", anexo["num"] or ""),), norm_text=_norm_text(anexo["rest"]))
    if apartado := _APARTADO.match(text):
        return Segment(text, (Unit("apartado", apartado["num"]),), norm_text=_norm_text(apartado["rest"]))
    if preambulo := _PREAMBULO.match(text):
        return Segment(text, (Unit("preambulo"),), norm_text=_norm_text(preambulo["rest"]))
    return None


def _letter_paren_continues(text: str, at: int) -> bool:
    """Whether the «)» at `at` closes a letter paragraph («b)») and the citation goes on after it."""
    if at < 2 or not re.match(r"[a-zñ]", text[at - 1]) or text[at - 2] not in ". \n":
        return False
    return bool(
        re.match(
            r"(?:\s+[ye]\s+[a-zñ\d]|\s*,\s*[a-zñ\d]|\s+[A-ZÁÉÍÓÚ]|\s+(?:del|de)\s|\.\d|\s+bis\b)",
            text[at + 1 : at + 40],
        )
    )


@dataclass(frozen=True)
class Parenthetical:
    """A citing parenthetical: where its inside starts in the text, and its inside."""

    start: int
    inner: str


def parentheticals(text: str) -> list[Parenthetical]:
    """Every parenthetical whose inside starts with a lead, in order, closing parens matched."""
    found: list[Parenthetical] = []
    index = 0
    while (open_at := text.find("(", index)) >= 0:
        inner_start = open_at + 1
        if not LEAD.match(text[inner_start : inner_start + 20]):
            index = inner_start
            continue
        depth = 0
        cursor = inner_start
        while cursor < len(text):
            char = text[cursor]
            if char == "(":
                depth += 1
            elif char == ")":
                if depth:
                    depth -= 1
                elif not _letter_paren_continues(text, cursor):
                    break
            elif char == "\n" and text[cursor + 1 : cursor + 2] == "\n":
                break  # a paragraph never continues a parenthetical
            cursor += 1
        found.append(Parenthetical(inner_start, text[inner_start:cursor]))
        index = cursor
    return found


def segments(inner: str) -> list[tuple[int, str]]:
    """The top-level `;`-separated pieces of a parenthetical, with their offsets inside it."""
    pieces: list[tuple[int, str]] = []
    depth = 0
    start = 0
    for at, char in enumerate(inner):
        if char == "(":
            depth += 1
        elif char == ")" and depth:
            depth -= 1
        elif char == ";" and depth == 0:
            pieces.append((start, inner[start:at]))
            start = at + 1
    pieces.append((start, inner[start:]))
    return pieces
