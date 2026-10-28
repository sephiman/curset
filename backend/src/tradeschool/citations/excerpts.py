# SPDX-License-Identifier: AGPL-3.0-only
"""The norm's own text for a question's solution panel (delta F): extracted once, at build time, from the
course's snapshot (`scripts/extract_excerpts.py` writes `excerpts.json`); serving only reads it.

Unit of extraction (F2), pinned here because the build script and the tests both rely on it:

* A norm citation gives the cited paragraph(s) when it names them («art. 30.4» → apartado 4), else the
  whole unit (article, disposición, regla, annex note). An apartado longer than the cap that is cited by
  letter («94.1.e») keeps its opening words and the cited letters only.
* The excerpt is capped at `WORD_CAP` words, cut at the last sentence end that keeps at least half of it,
  else at the cap, and marked «[…]». The whole unit rides along as `full` when it differs from the
  excerpt and has at most `FULL_CAP` words; a longer one is reached by its source link only.
* A PDF unit runs from its heading to the next heading of any unit or of a título, capítulo or sección.
  An HTML norm's unit is the BOE block whose id the source index gives it.
* A saved documentation page (`fuente:` citation) gives one paragraph of the section the cited label opens
  (the paragraphs after the label when the label is inline): whole when it has fewer than `WHOLE_PARAGRAPH`
  words, else at most `SENTENCE_CAP` of its sentences (F2 as amended on 2026-10-30). The paragraph and the
  sentences are the ones holding what the explanation states (its quotes, its first sentence's words,
  codes and numbers); with nothing found, the section's first paragraph. With no label, the whole page.
"""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable
from dataclasses import dataclass, field
from html.parser import HTMLParser
from itertools import takewhile

from tradeschool.citations.grammar import (
    LATIN,
    Segment,
    Unit,
    cited_parts,
    collapse,
    parse_segment,
    segments,
)
from tradeschool.citations.sources import heading_unit, spelled_number

WORD_CAP = 200
FULL_CAP = 1500
SENTENCE_CAP = 2
WHOLE_PARAGRAPH = 120
ELLIPSIS = "[…]"


@dataclass(frozen=True)
class Block:
    """One paragraph of a source as a reader sees it."""

    text: str
    #: A heading's level (h1 to h6 in HTML; 1 for a PDF unit heading); 0: body text.
    level: int = 0
    #: The PDF page it starts on (1-based).
    page: int | None = None
    #: The id of the HTML element (a BOE block) it sits in.
    anchor: str | None = None
    #: A table row's header row, when the table has three or more columns.
    header: str | None = None


@dataclass(frozen=True)
class Excerpt:
    heading: str
    text: str
    #: The whole unit, when it is not `text` already and fits `FULL_CAP`.
    full: str | None
    #: The unit is longer than `FULL_CAP`: «Ver artículo completo» is the source link.
    full_too_long: bool
    #: Course-relative source file and where it opens (`#page=N`, `#a1-22`, or empty).
    file: str
    fragment: str
    #: A documentation page's title and consultation date.
    attribution: str | None = None
    #: Why the build doubts this excerpt (`links-only`, `fallback`): listed in the build report.
    flag: str | None = None

    def as_json(self) -> dict[str, object]:
        out: dict[str, object] = {"heading": self.heading, "text": self.text}
        if self.full is not None:
            out["full"] = self.full
        if self.full_too_long:
            out["fullTooLong"] = True
        out["source"] = {"file": self.file, "fragment": self.fragment}
        if self.attribution:
            out["attribution"] = self.attribution
        if self.flag:
            out["flag"] = self.flag
        return out


@dataclass(frozen=True)
class NoExcerpt:
    reason: str
    #: The source the extractor looked in, when it has one: the panel still links it.
    file: str | None = None
    fragment: str = ""


# Reasons a question has no excerpt, as the build report prints them.
NO_CITATION = "the question cites nothing"
NO_NORM = "the citation names no norm of normativa.yaml"
NO_FILE = "the norm has no source file"
NOT_TEXT = "source not text-extractable"
NO_HEADING = "heading not found"
NO_LABEL = "label not found"
NO_MATCH = "no paragraph of the page holds what the explanation says"
NO_PARSE = "citation not understood"
NO_FACT = "a verifier found the fact neither in the excerpt nor elsewhere on the page"


# --- reading a source ----------------------------------------------------------------------------------

_FOOTER = re.compile(
    r"^\s*(?:BOLETÍN OFICIAL DEL ESTADO|LEGISLACIÓN CONSOLIDADA|Página \d+(?: de \d+)?"
    r"|.*\bL \d+/\d+.*Diario Oficial de la Unión Europea.*"
    r"|.*Diario Oficial de la Unión Europea.*\bL \d+/\d+.*"
    r"|[▼►◄]\s*[A-Z]\d*)\s*$"
)
# EUR-Lex consolidated texts mark each amendment inline: «►M2», «▼B», «◄».
_MARKER = re.compile(r"[▼►◄]\s?(?:[A-Z]\d*\b)?\s?")
_LEADER = re.compile(r"(\.\s?){4,}\s*\d+\s*$")
_STRUCTURE = re.compile(r"^(?:T[ÍI]TULO|CAP[ÍI]TULO|SECCIÓN|Sección|SUBSECCIÓN|Subsección|LIBRO|PARTE)\b")
# A unit heading: «Artículo 30.  Cómputo de plazos.» (BOE) or a bare «Artículo 15» line (DOUE).
_ARTICLE_HEADING = re.compile(rf"^Art[íi]culo\s+(?:\d+|único|[a-záéíóúñ ]+?)(?:\s+{LATIN})?\s*(?:\.|$)")
_SHORT_TITLE = 12
_TERMINAL_COLON = re.compile(r":\s*$")
_DANGLING = re.compile(
    r"\b(?:artículo|artículos|apartado|apartados|art\.|arts\.|de|del|la|el|los|las|y|o|en|a)$"
)
_BARE_HEADING = re.compile(rf"^Art[íi]culo\s+\S+(?:\s+{LATIN})?$")
_TERMINAL = re.compile(r"[.:;»”\"]\s*$")
_STARTS_PART = re.compile(r"^(?:\d{1,3}\.\s|\d{1,3}(?:\.\d{1,3})+\s|\d{1,3}\.ª\s|[a-zñ]\)\s|\(\d+\)\s)")


def _is_heading(text: str) -> bool:
    if _STRUCTURE.match(text):
        return True
    unit = heading_unit(text)
    if unit is None:
        return False
    if unit.kind == "apartado":
        # «Sexto.  Delimitación.» heads an orden's apartado; «Primero. En única instancia, de los …» is
        # a spelled paragraph of an article, and a wrapped «tercero. El …» is not a heading at all.
        return text[:1].isupper() and len(text.split()) <= _SHORT_TITLE
    return unit.kind != "art" or bool(_ARTICLE_HEADING.match(text))


def _page_lines(pages: list[str]) -> list[tuple[int, str]]:
    """(page, line) with running footers, amendment markers and index pages dropped."""
    lines: list[tuple[int, str]] = []
    for number, page in enumerate(pages, start=1):
        kept = [line for line in page.splitlines() if not _FOOTER.match(line)]
        if sum(1 for line in kept if _LEADER.search(line)) >= 3:
            continue
        lines += [(number, _MARKER.sub("", line)) for line in kept]
    return lines


def _soft(line: str) -> bool:
    """A wrapped line ends in one space; the end of a paragraph in none (BOE) or two (EUR-Lex)."""
    return line.endswith(" ") and not line.endswith("  ")


def _soft_wraps(lines: list[tuple[int, str]]) -> bool:
    """Whether trailing spaces tell wraps from paragraph ends — not when nearly every line has one (DOUE)."""
    soft = sum(1 for _, line in lines if _soft(line))
    return 0 < soft < 0.9 * len(lines)


@dataclass
class _Paragraphs:
    blocks: list[Block] = field(default_factory=list)
    lines: list[str] = field(default_factory=list)
    page: int = 0

    def close(self) -> None:
        text = collapse(" ".join(self.lines))
        self.lines.clear()
        if text:
            self.blocks.append(Block(text, 1 if _is_heading(text) else 0, self.page))

    def add(self, page: int, line: str) -> None:
        if not self.lines:
            self.page = page
        if self.lines and self.lines[-1].endswith("\xad"):  # a word hyphenated across the wrap
            self.lines[-1] = self.lines[-1].rstrip("\xad").rstrip() + line.lstrip()
            return
        self.lines.append(line)


def pdf_blocks(pages: list[str]) -> list[Block]:
    """A PDF's paragraphs: wrapped lines rejoined, running footers and index pages dropped.

    A paragraph ends at a line without the trailing space of a soft wrap, where the PDF marks wraps that
    way; elsewhere at a line ending in «.», «:» or «;». A unit heading, an apartado («4. ») or a letter
    («a) ») always starts one, and a page that opens in lower case continues the paragraph before it.
    """
    lines = _page_lines(pages)
    signal = _soft_wraps(lines)
    out = _Paragraphs()
    previous_page = 0
    wrapped = False
    for page, raw in lines:
        text = raw.strip()
        new_page, previous_page = page != previous_page, page
        # A line that continues a soft-wrapped one is never a heading, whatever it starts with.
        continues, wrapped = wrapped and bool(out.lines), signal and _soft(raw)
        if not text:
            out.close()
            continue
        if (not continues or _ARTICLE_HEADING.match(text)) and _is_heading(text):
            out.close()
            out.add(page, text)
            # Only a BOE heading whose title wraps («Artículo 30.  Cómputo de …» + soft wrap) goes on.
            if not (signal and _soft(raw)) or _BARE_HEADING.match(text):
                out.close()
            continue
        dangling = bool(out.lines) and bool(_DANGLING.search(out.lines[-1]))
        if (
            out.lines
            and not dangling
            and (_STARTS_PART.match(text) or (not signal and _TERMINAL.search(out.lines[-1])))
        ):
            out.close()
        last = out.blocks[-1] if out.blocks else None
        if (
            new_page
            and not out.lines
            and last is not None
            and not last.level
            and re.match(r"^[a-záéíóúñ]", text)
            and not _TERMINAL.search(last.text)
        ):
            out.blocks.pop()
            out.add(last.page or page, last.text)
        out.add(page, text)
        # A hard break after a word that cannot end a sentence («… en el artículo» / «11.2 del …»).
        if signal and not _soft(raw) and not _DANGLING.search(text):
            out.close()
    out.close()
    return out.blocks


_SKIP = {"script", "style", "noscript", "svg", "template", "select"}
# Page furniture inside the article: the help pages' «Obtener ayuda con Copilot» prompts, banners.
_FURNITURE = re.compile(r"copilot|banner", re.I)
_BLOCK = {
    "p", "div", "section", "article", "main", "header", "footer", "aside", "table", "tr", "ul", "ol",
    "li", "dt", "dd", "td", "th", "caption", "blockquote", "pre", "figcaption", "summary", "details",
    "h1", "h2", "h3", "h4", "h5", "h6", "br", "hr", "body", "title", "dl",
}  # fmt: skip


class _BlockParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[Block] = []
        self.title = ""
        self._text: list[str] = []
        self._skip = 0
        self._level = 0
        self._ids: list[str | None] = []
        self._in_title = False
        #: Inside a table row: its cells make one block, «shortcut — what it does».
        self._row = 0
        #: The current table's first row, kept as the header of the rows below it when it has 3+ cells.
        self._header: str | None = None
        self._first_row = False

    def _flush(self) -> None:
        text = collapse("".join(self._text))
        self._text.clear()
        if not text:
            return
        if self._in_title:
            self.title = self.title or text
            return
        anchor = next((i for i in reversed(self._ids) if i), None)
        header = None
        if self._row and self._first_row:
            self._first_row = False
            self._header = text if text.count(" — ") >= 2 else None
        elif self._row:
            header = self._header
        self.blocks.append(Block(text, self._level, anchor=anchor, header=header))

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in _SKIP:
            self._skip += 1
            return
        if tag == "title":
            self._in_title = True
        if tag == "table":
            self._first_row, self._header = True, None
        if tag == "tr":
            self._flush()
            self._row += 1
            return
        if self._row and tag in ("td", "th"):
            if "".join(self._text).strip():
                self._text.append(" — ")
            return
        if tag == "dd" and "".join(self._text).strip():
            self._text.append(" — ")  # a term and its definition stay one block
            return
        if self._row and tag in _BLOCK:
            self._text.append(" ")
            return
        if tag in _BLOCK:
            self._flush()
            if tag in ("div", "section", "article"):
                block_id = dict(attrs).get("id")
                self._ids.append(block_id)
                if block_id and _FURNITURE.search(block_id):
                    self._skip += 1
            if re.fullmatch(r"h[1-6]", tag):
                self._level = int(tag[1])

    def handle_endtag(self, tag: str) -> None:
        if tag in _SKIP:
            self._skip = max(0, self._skip - 1)
            return
        if tag == "tr":
            self._flush()
            self._row = max(0, self._row - 1)
            return
        if tag == "dt" or (self._row and tag in _BLOCK):
            if self._row:
                self._text.append(" ")
            return
        if tag in _BLOCK:
            self._flush()
            if tag in ("div", "section", "article") and self._ids:
                block_id = self._ids.pop()
                if block_id and _FURNITURE.search(block_id):
                    self._skip = max(0, self._skip - 1)
            if re.fullmatch(r"h[1-6]", tag):
                self._level = 0
            if tag == "title":
                self._in_title = False

    def handle_data(self, data: str) -> None:
        if not self._skip:
            self._text.append(data)


def html_blocks(html: str) -> tuple[list[Block], str]:
    """An HTML or XML page's paragraphs in reading order, and its <title>."""
    parser = _BlockParser()
    parser.feed(html)
    parser.close()
    parser._flush()
    return parser.blocks, parser.title


def text_blocks(text: str) -> list[Block]:
    """A plain-text file's paragraphs: runs of lines between blank lines."""
    return [Block(collapse(p)) for p in re.split(r"\n\s*\n", text) if p.strip()]


# --- norms ---------------------------------------------------------------------------------------------


def _words(text: str) -> int:
    return len(text.split())


def capped(text: str, cap: int = WORD_CAP) -> tuple[str, bool]:
    """`text` cut to `cap` words — at a sentence end when that keeps at least half — and whether it was."""
    words = text.split(" ")
    if _words(text) <= cap:
        return text, False
    head = " ".join(words[:cap])
    ends = [m.end() for m in re.finditer(r"[.;:](?=\s|$)", head)]
    cut = ends[-1] if ends and _words(head[: ends[-1]]) >= cap // 2 else len(head)
    return f"{head[:cut].rstrip()} {ELLIPSIS}", True


def _opens_annex(block: Block) -> bool:
    found = heading_unit(block.text) if block.level else None
    return found is not None and found.kind == "anexo"


def _unit_blocks(blocks: list[Block], unit: Unit, place: object, occurrence: int = 0) -> list[Block] | None:
    """The unit's heading block and its body up to the next heading, or None when its heading is absent.
    `occurrence` 1, 2, … takes a later heading of the same unit (an annexed reglamento's own articles)."""
    if unit.kind == "nota":
        return _note_blocks(blocks, unit, place) if not occurrence else None
    starts = [
        at
        for at, block in enumerate(blocks)
        if block.level
        and not (isinstance(place, int) and block.page is not None and block.page < place)
        and not (isinstance(place, str) and block.anchor != place)
        and (found := heading_unit(block.text)) is not None
        and found.slug == unit.slug
    ]
    if occurrence >= max(len(starts), 1):
        return None
    if not starts:
        return _untitled_preamble(blocks) if unit.kind == "preambulo" else None
    start = starts[occurrence]
    # An annex holds its own capítulos and artículos: it runs to the next annex.
    ends = _opens_annex if unit.kind == "anexo" else (lambda block: bool(block.level))
    end = next((at for at in range(start + 1, len(blocks)) if ends(blocks[at])), len(blocks))
    return blocks[start:end]


_TEXT_HEAD = re.compile(r"^(?:TEXTO CONSOLIDADO|Última modificación|Sabed:|Hago saber)", re.I)


def _untitled_preamble(blocks: list[Block]) -> list[Block] | None:
    """A preamble the text prints without a heading: from the enacting formula to the first heading."""
    first_heading = next((at for at, block in enumerate(blocks) if block.level), len(blocks))
    opening = [at for at, block in enumerate(blocks[:first_heading]) if _TEXT_HEAD.match(block.text)]
    body = blocks[(opening[-1] + 1 if opening else 0) : first_heading]
    return [Block(""), *body] if body else None


_NUMBERED = re.compile(r"^(\d{1,3})\.\s")


def _note_blocks(blocks: list[Block], unit: Unit, place: object) -> list[Block] | None:
    """An annex note: the numbered paragraph «34. …» of its annex, up to the next numbered one."""
    annex = unit.within
    start = None
    in_annex = annex is None
    for at, block in enumerate(blocks):
        found = heading_unit(block.text) if block.level else None
        if found is not None and found.kind == "anexo":
            in_annex = annex is None or found.slug == annex.slug
            continue
        if isinstance(place, int) and block.page is not None and block.page < place:
            continue
        match = _NUMBERED.match(block.text)
        if in_annex and match and match[1] == unit.number:
            start = at
            break
    if start is None:
        return None
    end = start + 1
    while end < len(blocks) and not blocks[end].level and not _NUMBERED.match(blocks[end].text):
        end += 1
    return [Block(""), *blocks[start:end]]


_DOTTED = re.compile(r"^(\d+(?:\.\d+)*)\.?\s")
_DOTTED_PATHS = re.compile(r"(?<![\w.])\d+(?:\.\d+)*")


def _dotted_paths(segment: Segment) -> list[str]:
    """The numbered apartados a segment cites in a text numbered «9.», «9.7», «5.1.4»."""
    cited = segment.text[: len(segment.text) - len(segment.norm_text)] if segment.norm_text else segment.text
    return _DOTTED_PATHS.findall(cited)


def _dotted_section(blocks: list[Block], path: str) -> list[Block]:
    """Apartado `path` of a text numbered by dotted paths, with every sub-apartado under it."""
    start = next((at for at, b in enumerate(blocks) if (m := _DOTTED.match(b.text)) and m[1] == path), None)
    if start is None:
        return []
    end = start + 1
    while end < len(blocks) and not blocks[end].level:
        match = _DOTTED.match(blocks[end].text)
        if match and not match[1].startswith(f"{path}."):
            break
        end += 1
    return blocks[start:end]


_ORDINAL_PATH = re.compile(r"^apartados?\s+[a-záéíóúñ]+\.(?P<path>\d+(?:\.\d+)+)")
_LETTER = re.compile(r"^([a-zñ])\)\s")
# An apartado is numbered «4.» or, in older laws, spelled «Tres.».
_APARTADO_START = re.compile(r"^(\d{1,3}|[A-ZÁÉÍÓÚ][a-záéíóúñ]+(?:\s+y\s+[a-záéíóúñ]+)?)\.\s")


def _apartado_number(block: Block, spelled: bool) -> int | None:
    """The block's apartado number, counting only spelled («Dos.») or only numbered («2.») apartados:
    an article numbered «Uno.», «Dos.» keeps «1.», «2.» for the paragraphs inside them."""
    match = _APARTADO_START.match(block.text)
    if match is None or match[1].isdigit() == spelled:
        return None
    return int(match[1]) if match[1].isdigit() else spelled_number(match[1])


def _apartado(body: list[Block], number: str) -> list[Block]:
    """The blocks of apartado `number` of a unit's body: «4. …» up to the next higher-numbered apartado.

    A list numbered from 1 again inside the apartado (under a letter) is followed item by item, so its
    «2.» does not end apartado 1.
    """
    wanted = int(number) if number.isdigit() else spelled_number(number)
    if wanted is None:
        return []
    spelled = not number.isdigit()
    if not spelled and not any(_apartado_number(block, False) for block in body):
        spelled = True  # «art. 22.3» of a law that spells its apartados «Tres.»
    start = next((at for at, block in enumerate(body) if _apartado_number(block, spelled) == wanted), None)
    if start is None:
        return []
    end = start + 1
    nested: int | None = None
    while end < len(body):
        found = _apartado_number(body[end], spelled)
        if found is not None and (
            (nested is None and found <= wanted) or (nested is not None and found in (nested + 1, 1))
        ):
            nested = found
        elif found is not None and found > wanted:
            break
        end += 1
    return body[start:end]


def _letters(blocks: list[Block], letters: Iterable[str]) -> list[Block]:
    """The opening words of an apartado (before its first letter) and the cited letters' blocks."""
    wanted = set(letters)
    out: list[Block] = []
    current: str | None = None
    for block in blocks:
        match = _LETTER.match(block.text)
        if match:
            current = match[1]
        if current is None or current in wanted:
            out.append(block)
    return out


# The consolidated text's editorial notes are not the norm: «Téngase en cuenta…», «Se modifica … Ref. BOE-…».
_NOTE = re.compile(
    r"^(?:Téngase en cuenta\b|Redacción anterior\b|Ref\. BOE-|"
    r"Se (?:modifica|añade|deroga|suprime|da nueva redacción|renumera)\b.*Ref\. BOE-)"
)


def _join(blocks: Iterable[Block]) -> str:
    return "\n\n".join(block.text for block in blocks if block.text and not _NOTE.match(block.text))


def _heading(citation: str) -> str:
    text = collapse(citation)
    return text[:1].upper() + text[1:]


def _focus(selection: list[Block], wanted: list[str]) -> list[Block]:
    """A selection longer than the cap whose opening misses what the explanation quotes: the paragraph
    that holds the quote instead, so the excerpt shows the text the key rests on."""
    if not wanted or _words(_join(selection)) <= WORD_CAP:
        return selection
    opening = _score(capped(_join(selection))[0], wanted)
    best = max(selection, key=lambda block: _score(block.text, wanted))
    if _score(best.text, wanted) <= opening:
        return selection
    # The opening words («Serán objeto de anotación …:») say what the quoted item is an item of.
    return (
        [selection[0], best]
        if best is not selection[0] and _TERMINAL_COLON.search(selection[0].text)
        else [best]
    )


def _cited_selection(unit: Unit, segment: Segment, body: list[Block]) -> list[Block]:
    """The apartados and letters the segment names in `unit`; empty when it cites the unit whole."""
    if unit.kind == "apartado" and unit.number.isdigit():
        return [block for path in _dotted_paths(segment) for block in _dotted_section(body, path)]
    if unit.kind == "anexo":
        return _annex_part(body, segment)
    if unit.kind == "apartado" and (deep := _ORDINAL_PATH.match(segment.text)):
        return _dotted_section(body, deep["path"])  # «apartado octavo.2.2»: sub-apartado 2.2 of octavo
    part = cited_parts(segment.text).get(unit.slug)
    if part is None:
        return []
    chosen: list[Block] = []
    for paragraph in part.paragraphs:
        apartado = _apartado(body, paragraph)
        letters = [letter for p, letter in part.letters if p == paragraph]
        if letters and _words(_join(apartado)) > WORD_CAP:
            apartado = _letters(apartado, letters)
        chosen += [block for block in apartado if block not in chosen]
    if not part.paragraphs and part.letters and _words(_join(body)) > WORD_CAP:
        chosen = _letters(body, [letter for _, letter in part.letters])
    return chosen


_IN_ANNEX = re.compile(r"^anexo\s+\S+,\s+(?P<kind>arts?\.|capítulo)\s+(?P<number>\d+)", re.I)


def _annex_part(body: list[Block], segment: Segment) -> list[Block]:
    """What «anexo IV, art. 63, …» or «anexo IV, capítulo 6, …» names inside its annex."""
    match = _IN_ANNEX.match(segment.text)
    if match is None:
        return []
    word = r"Art[íi]culo" if match["kind"].lower().startswith("art") else r"(?:CAPÍTULO|Capítulo)"
    opens = re.compile(rf"^{word}\s+{match['number']}\b")
    start = next((at for at, block in enumerate(body) if block.level and opens.match(block.text)), None)
    if start is None:
        return []
    same_kind = re.compile(rf"^{word}\b")
    end = next(
        (at for at in range(start + 1, len(body)) if body[at].level and same_kind.match(body[at].text)),
        len(body),
    )
    return body[start:end]


def _numbered_unit(blocks: list[Block], unit: Unit, segment: Segment) -> list[Block] | None:
    """A numbered apartado of a resolución or orden («apartado 9.7»): its top-level section."""
    paths = _dotted_paths(segment)
    section = _dotted_section(blocks, paths[0].split(".")[0]) if paths else []
    return [Block(""), *section] if section else None


def norm_excerpt(
    blocks: list[Block], segment: Segment, file: str, place: object, fragment: str, explanation: str = ""
) -> Excerpt | NoExcerpt:
    """The cited paragraphs of the segment's first unit the source holds, capped, with the whole unit."""
    wanted = quotes(explanation)
    for unit in segment.units:
        found = _unit_blocks(blocks, unit, place if unit == segment.units[0] else None)
        if found is None and unit.kind == "apartado" and unit.number.isdigit():
            found = _numbered_unit(blocks, unit, segment)
        if found is None:
            continue
        cited = _cited_selection(unit, segment, found[1:])
        if not cited and unit.slug in cited_parts(segment.text):
            # The cited apartado is not under this heading: a later one of the same unit may hold it.
            later = _unit_blocks(blocks, unit, place, occurrence=1)
            if later is not None and (in_later := _cited_selection(unit, segment, later[1:])):
                found, cited = later, in_later
        heading, body = found[0], found[1:]
        whole = body or found
        selection = _focus(cited or whole, wanted)
        text, cut = capped(_join(selection))
        full_text = _join([heading, *body])
        shows_all = not cut and selection == whole
        too_long = not shows_all and _words(full_text) > FULL_CAP
        return Excerpt(
            heading=_heading(segment.text),
            text=text,
            full=None if shows_all or too_long else full_text,
            full_too_long=too_long,
            file=file,
            fragment=fragment,
        )
    return NoExcerpt(NO_HEADING, file, fragment)


# --- documentation pages -------------------------------------------------------------------------------

_QUOTE = re.compile(r"«([^«»]{8,})»")
# Never after a lone initial: «S. Crocker» is one name, not two sentences.
_SENTENCE_END = re.compile(r"(?<=[.!?…])(?:(?<!\b[A-Z]\.)\s+(?=[«\"“¿¡(A-ZÁÉÍÓÚÑ])|\s+(?=[0-9]))")
_SHINGLE = 4


def normalized(text: str) -> str:
    folded = unicodedata.normalize("NFKC", text).casefold()
    folded = re.sub("[«»\u201c\u201d\"'\u2018\u2019`]", "", folded)
    return " ".join(re.findall(r"\w+", folded))


def quotes(explanation: str) -> list[str]:
    """The fragments an explanation quotes from its source, split at ellipses."""
    found: list[str] = []
    for match in _QUOTE.finditer(explanation):
        for piece in re.split(r"\[…\]|\(…\)|…|\.\.\.", match[1]):
            if len(normalized(piece).split()) >= 2:
                found.append(normalized(piece))
    return found


def _shingles(text: str) -> set[tuple[str, ...]]:
    words = text.split()
    size = min(_SHINGLE, len(words))
    return {tuple(words[at : at + size]) for at in range(len(words) - size + 1)}


def _score(text: str, wanted: list[str]) -> int:
    """How much of the quoted text `text` holds: whole fragments count their length, else shared shingles."""
    plain = normalized(text)
    score = 0
    for quote in wanted:
        if quote in plain:
            score += 10 * len(quote.split())
            continue
        mine = _shingles(plain)
        score += sum(1 for shingle in _shingles(quote) if shingle in mine)
    return score


def sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENTENCE_END.split(text) if s.strip()]


_MIN_OVERLAP = 3
_MIN_STEMS = 2
_ARGUMENT_LABEL = re.compile(r"^\S+(?:\s\S+)?\s(?:Obligatorio|Opcional)\.$")


# A code («&p», «#N/A», «Ctrl+C» aside) or a number of two digits or more («2011»): what the key often is.
_KEY_TOKEN = re.compile(r"[&#@%$]\w+|\b\d{2,}\b")


def key_tokens(text: str) -> frozenset[str]:
    return frozenset(_KEY_TOKEN.findall(text.lower()))


@dataclass(frozen=True)
class _Wanted:
    """What the explanation says the source holds: the text it quotes, the codes and numbers its first
    sentence states, else that sentence's content words (an explanation that paraphrases, or quotes only
    the wrong options)."""

    quoted: list[str]
    words: frozenset[str]
    keys: frozenset[str]
    #: What the first sentence quotes: the text the key rests on; later quotes are often the distractors'.
    first_quoted: list[str]
    #: The first sentence itself, for an explanation that paraphrases the source word for word.
    first: str

    @classmethod
    def of(cls, explanation: str, label: str | None = None) -> _Wanted:
        first = sentences(explanation)[0] if explanation.strip() else ""
        words = frozenset(w for w in normalized(first).split() if len(w) >= 5)
        # A quote the cited label already holds («Firewall y protección de red») names where the fact is,
        # not the fact.
        named = normalized(label or "")

        def facts(found: list[str]) -> list[str]:
            return [quote for quote in found if not (named and quote in named)]

        return cls(
            facts(quotes(explanation)), words, key_tokens(first), facts(quotes(first)), normalized(first)
        )

    def quotes_in(self, text: str) -> int:
        return _score(text, self.quoted)

    def first_quotes_in(self, text: str) -> int:
        return _score(text, self.first_quoted)

    def keys_in(self, text: str) -> frozenset[str]:
        return self.keys & key_tokens(text)

    def stem_overlap(self, text: str) -> int:
        stems = {word[:5] for word in self.words}
        return len(stems & {word[:5] for word in normalized(text).split() if len(word) >= 5})

    def overlap(self, text: str) -> int:
        return len(self.words & set(normalized(text).split()))

    def score(self, text: str) -> int:
        overlap = self.overlap(text)
        return (
            200 * _score(text, self.first_quoted)
            + 100 * _score(text, self.quoted)
            + (overlap if overlap >= _MIN_OVERLAP else 0)
        )

    def support(self, text: str) -> int:
        """`score` without the later quotes: what the explanation itself states the source says."""
        overlap = self.overlap(text)
        return 200 * _score(text, self.first_quoted) + (overlap if overlap >= _MIN_OVERLAP else 0)

    def support_rank(self, text: str) -> tuple[int, int, int, int]:
        return (self.support(text), *self.rank(text)[1:])

    def in_section(self, text: str) -> bool:
        """Under the cited label a line may answer by the code or number alone, if it shares a word
        with the explanation («&p — Imprimir el número de página»). Elsewhere on the page a bare number
        matches menus and tables, so it never qualifies a paragraph there."""
        return bool(self.score(text)) or (bool(self.keys_in(text)) and self.overlap(text) >= 1)

    def adds_to(self, picked: str, text: str) -> bool:
        """Whether `text` is the other half of the fact: new words of the explanation, not a wrong option's
        quoted text, and not the pick again."""
        if normalized(text) in normalized(picked):
            return False
        later_quotes = [quote for quote in self.quoted if quote not in self.first_quoted]
        if _score(text, later_quotes):
            return False
        shown = set(normalized(picked).split())
        return len((self.words & set(normalized(text).split())) - shown) >= 2

    def rank(self, text: str) -> tuple[int, int, int, int]:
        """`score`, then the codes and numbers it shares, then the runs of words it shares with the first
        sentence («el valor que se devuelve si la fórmula se evalúa como un error»), then the explanation's
        words below the threshold: «&p — Imprimir el número de página» over «Pies de página: página &p»."""
        runs = len(_shingles(normalized(text)) & _shingles(self.first)) if self.first else 0
        return self.score(text), len(self.keys_in(text)), runs, self.overlap(text)


def _best_sentences(paragraph: str, wanted: _Wanted) -> str:
    """At most `SENTENCE_CAP` sentences of the paragraph: those that hold what the explanation says."""
    found = sentences(paragraph)
    if len(found) <= SENTENCE_CAP:
        return paragraph
    scores = [wanted.score(sentence) for sentence in found]
    best = max(
        range(len(found)), key=lambda at: (wanted.rank(found[at]), wanted.stem_overlap(found[at]), -at)
    )
    if scores[best] == 0:
        # Nothing scores (a page in another language): the sentence sharing most stems, with the next one.
        stems = [wanted.stem_overlap(sentence) for sentence in found]
        first = max(range(len(found)), key=lambda at: (stems[at], -at)) if max(stems) >= _MIN_STEMS else 0
        return " ".join(found[first : first + SENTENCE_CAP])
    after = best + 1 if best + 1 < len(found) else None
    before = best - 1 if best > 0 else None
    second = max(
        (at for at in (before, after) if at is not None),
        key=lambda at: (scores[at], at == after),
    )
    picked = sorted({best, second} if scores[second] > 0 else {best})
    # An argument row opens with its name («value_if_error Obligatorio.»): it says what the chosen
    # sentence describes, so it takes the second place.
    if best > 0 and _ARGUMENT_LABEL.match(found[0]):
        picked = sorted({0, best})
    return " ".join(found[at] for at in picked)


def _label_index(blocks: list[Block], label: str) -> int | None:
    """Where the cited label is: a block that is it, else one that starts with it (a glossary entry),
    else one that holds it; headings first at each step."""
    wanted = normalized(label)
    if not wanted:
        return None
    tests = (
        lambda plain: plain == wanted,
        lambda plain: plain.startswith(wanted),
        lambda plain: wanted in plain,
    )
    for test in tests:
        for prefer_heading in (True, False):
            for at, block in enumerate(blocks):
                if bool(block.level) == prefer_heading and test(normalized(block.text)):
                    return at
    return None


def _title_like(block: Block) -> bool:
    return not block.level and len(block.text.split()) <= _SHORT_TITLE and not _TERMINAL.search(block.text)


def _section(blocks: list[Block], at: int) -> list[Block]:
    """The paragraphs a heading opens, up to the next heading of its level or above. A short paragraph
    that is only the label stands for a heading: up to the next such title."""
    head = blocks[at]
    if not head.level and not _title_like(head):
        # A label inside a paragraph: that paragraph and the ones after it, up to the next heading.
        return [head, *takewhile(lambda block: not block.level, blocks[at + 1 :])]
    out: list[Block] = []
    for block in blocks[at + 1 :]:
        if block.level and (not head.level or block.level <= head.level):
            break
        if not head.level and _title_like(block):
            break
        if not block.level:
            out.append(block)
    return out


_LIST_REACH = 20
# «"winver":» is an item of its own; a lead-in is a sentence: «ejecute una de las acciones siguientes:».
_LEAD_IN_WORDS = 4


def _continued(
    blocks: list[Block], paragraph: Block, text: str, wanted: _Wanted, section: list[Block], body: list[Block]
) -> str:
    """A pick that ends its paragraph short of two sentences takes the next step with it: after «…:» the
    item of the list below that holds what the explanation says, else the next paragraph's first sentence."""
    colon = text.rstrip().endswith(":")
    if not paragraph.text.endswith(text) or (len(sentences(text)) >= SENTENCE_CAP and not colon):
        return text
    if not colon and wanted.keys and wanted.keys <= key_tokens(text):
        return text  # it already holds the code or number the key rests on
    at = next(i for i, block in enumerate(blocks) if block is paragraph)
    following: list[Block] = []
    for block in blocks[at + 1 : at + 1 + _LIST_REACH]:
        if block.level or (not colon and _title_like(block)):
            break
        following.append(block)
    if not following:
        return text
    if colon:  # the pick's best sentence (often the one that opens the list), and the list's best item
        item = max(following, key=lambda block: (wanted.rank(block.text), -following.index(block)))
        whole = text == paragraph.text and _words(text) < WHOLE_PARAGRAPH
        return f"{text if whole else max(sentences(text), key=wanted.rank)} {item.text}"
    # The other half of a two-part fact may sit further down the section: it beats the next line when it
    # matches the explanation better, and is shown after «[…]».
    quoted_elsewhere = [
        block for block in body if block not in section and _score(block.text, wanted.first_quoted)
    ]
    elsewhere = [
        block
        for block in [*section, *quoted_elsewhere]
        if block is not paragraph and block is not following[0] and wanted.adds_to(text, block.text)
    ]
    other = max(elsewhere, key=lambda block: wanted.rank(block.text), default=None)
    if other is not None and wanted.score(other.text) > wanted.score(following[0].text):
        second = max(sentences(other.text), key=wanted.rank)
        later = blocks.index(other) > at
        return f"{text} {ELLIPSIS} {second}" if later else f"{second} {ELLIPSIS} {text}"
    step = sentences(following[0].text)[0]
    # «¿Busca información sobre …?» opens a see-also line, not the next step; a repeat adds nothing.
    if step.endswith("?") or normalized(step) in normalized(text):
        return text
    # A next step that only opens a list («… ejecute una de las acciones siguientes:») gives way to the
    # list's item that matches the explanation.
    if step.rstrip().endswith(":") and len(step.split()) >= _LEAD_IN_WORDS and len(following) > 1:
        items = following[1:]
        item = max(items, key=lambda block: (wanted.rank(block.text), -items.index(block)))
        return f"{text} {item.text}"
    return f"{text} {step}"


def _with_missing_key(body: list[Block], paragraph: Block, text: str, wanted: _Wanted) -> str:
    """A pick that lacks a code or number the explanation states («fundada en septiembre de 2011» in an
    earlier paragraph) gives up its weaker sentence to the page's sentence that holds it."""
    missing = wanted.keys - key_tokens(text)
    if not missing:
        return text
    # Ties go to the earlier sentence; words count by their first five letters, so a page in another
    # language still answers («transition» for «transición»).
    found = [
        (len(missing & key_tokens(sentence)), wanted.stem_overlap(sentence), -at, sentence)
        for at, block in enumerate(body)
        for sentence in sentences(block.text)
    ]
    hits, _, minus_at, donor = max(found, default=(0, 0, 0, ""))
    donor_at = -minus_at
    if not hits or donor in text:
        return text
    kept = max(sentences(text), key=wanted.rank)
    here = next((at for at, block in enumerate(body) if block is paragraph), donor_at)
    if donor_at == here:
        order = paragraph.text.find(donor) < paragraph.text.find(kept)
        return f"{donor} {kept}" if order else f"{kept} {donor}"
    return f"{donor}\n\n{kept}" if donor_at < here else f"{kept}\n\n{donor}"


# Build-report flags: the cited section holds only link titles; nothing in it matched the explanation.
LINKS_ONLY = "links-only"
FALLBACK = "fallback"


# A label that is the page's own text, cited to point at the fact itself (re-citations of 2026-10-30): a
# sentence of ten words or more, a shorter one ending like a sentence, or a table row («cell — cell»).
SENTENCE_LABEL = 10
_SHORT_SENTENCE = 6
_SENTENCE_STOP = re.compile(r"[.:!?]\s*$")


def _cites_a_sentence(block: Block, label: str) -> bool:
    """A heading of ten words or a short heading-like label does not count; a sentence or a row does."""
    if block.level:
        return False
    words = len(normalized(label).split())
    ends = bool(_SENTENCE_STOP.search(label))
    return " — " in label or (ends and (words >= SENTENCE_LABEL or words >= _SHORT_SENTENCE))


def _sentence_excerpt(
    blocks: list[Block], at: int, label: str, file: str, attribution: str | None, title: str
) -> Excerpt:
    """The paragraph or row holding the cited text, under the nearest heading above it: whole under
    `WHOLE_PARAGRAPH` words, else the sentences the label spans (two at most). A row of a table with three
    or more columns comes after its header row, which names the columns."""
    block = blocks[at]
    if _words(block.text) < WHOLE_PARAGRAPH:
        text = block.text
    else:
        wanted = _shingles(normalized(label))
        held = [sentence for sentence in sentences(block.text) if _shingles(normalized(sentence)) & wanted]
        text = " ".join(held[:SENTENCE_CAP]) or block.text
    if block.header and block.header != block.text:
        text = f"{block.header}\n\n{text}"
    if text.rstrip().endswith(":"):  # a lead-in: the list it opens, up to the next heading
        items = list(takewhile(lambda b: not b.level, blocks[at + 1 : at + 1 + _LIST_REACH]))
        text = "\n\n".join([text, *(item.text for item in items)])
    heading = next((b.text for b in reversed(blocks[:at]) if b.level), title)
    shown, _ = capped(text)
    return Excerpt(
        heading=heading,
        text=shown,
        full=None,
        full_too_long=False,
        file=file,
        fragment="",
        attribution=attribution,
    )


def page_excerpt(
    blocks: list[Block], label: str | None, explanation: str, file: str, attribution: str | None, title: str
) -> Excerpt | NoExcerpt:
    """At most two sentences of the paragraph the label opens that hold what the explanation says."""
    if not blocks:
        return NoExcerpt(NOT_TEXT)
    wanted = _Wanted.of(explanation, label)
    body = [block for block in blocks if not block.level]
    at = _label_index(blocks, label) if label else None
    section = _section(blocks, at) if at is not None else []
    # The quoted text wins wherever it is on the page the label names; failing that, the explanation's
    # words, in the section first.
    # Outside the cited section only what the explanation states counts (its first sentence's quotes and
    # words), never a later quote: that is often a wrong option's text, found elsewhere on the page.
    candidates, rank = next(
        (
            (found, rank)
            for pool, test, rank in (
                (section, wanted.quotes_in, wanted.rank),
                (body, wanted.first_quotes_in, wanted.rank),
                (section, wanted.in_section, wanted.rank),
                (body, wanted.support, wanted.support_rank),
            )
            if (found := [block for block in pool if test(block.text)])
        ),
        ([], wanted.rank),
    )
    if label and at is not None and _cites_a_sentence(blocks[at], label):
        return _sentence_excerpt(blocks, at, label, file, attribution, title)
    flag = (
        LINKS_ONLY
        if section and all(_title_like(block) and " — " not in block.text for block in section)
        else None
    )
    if candidates:
        paragraph = max(candidates, key=lambda block: rank(block.text))
    elif section:
        paragraph = section[0]
        flag = flag or FALLBACK
    else:
        # Neither the label nor what the explanation says is on the page: nothing answers for the key.
        return NoExcerpt(NO_LABEL if label and at is None else NO_MATCH, file)
    # F2 (amended 2026-10-30): a paragraph under 120 words is shown whole; a longer one, two sentences.
    whole = _words(paragraph.text) < WHOLE_PARAGRAPH
    chosen = paragraph.text if whole else _best_sentences(paragraph.text, wanted)
    picked = _continued(blocks, paragraph, chosen, wanted, section, body)
    text, _ = capped(_with_missing_key(section or body, paragraph, picked, wanted))
    return Excerpt(
        heading=label or title,
        text=text,
        full=None,
        full_too_long=False,
        file=file,
        fragment="",
        attribution=attribution,
        flag=flag,
    )


# --- citations -----------------------------------------------------------------------------------------

_LABEL = re.compile(r"«(?P<label>.+)»\s*$", re.DOTALL)


@dataclass(frozen=True)
class SourceCitation:
    """A `fuente:` citation: the cited file and the label after it, if any."""

    file: str
    label: str | None


def source_citation(citation: str) -> SourceCitation | None:
    pieces = segments(collapse(citation))
    first = parse_segment(pieces[0][1]) if pieces else None
    if first is None or not first.files:
        return None
    label = None
    if len(pieces) > 1 and (match := _LABEL.search(pieces[1][1].strip())):
        label = match["label"]
    return SourceCitation(first.files[0], label)
