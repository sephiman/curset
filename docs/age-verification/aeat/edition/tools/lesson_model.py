"""lesson_model.py: a lesson as headings, prose blocks and esquemas, rebuildable from a set of kept sentence ids.

Unit of selection: a sentence (paragraph or list item split by provenance.sentences) outside an esquema, or a whole
esquema (a «:::esquema» directive). Kept sentences are written back byte-identical (whitespace collapsed, as the
sentence id is computed); a block whose sentences are all kept is copied line by line.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "backend"))

from scripts.provenance import Sentence, sentences  # noqa: E402

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
ESQUEMA = re.compile(r"^:::esquema\b")
NOTE = re.compile(r"^:::note\b")
CLOSE = re.compile(r"^:::\s*$")


def words(text: str) -> int:
    return len(text.split())


@dataclass
class Block:
    first: int
    last: int
    kind: str
    sentences: list[Sentence]
    section: int
    note: int | None


@dataclass
class Esquema:
    first: int
    last: int
    title: str
    kind: str
    section: int
    sentences: list[Sentence] = field(default_factory=list)


@dataclass
class Note:
    first: int
    last: int
    type: str
    section: int


@dataclass
class Section:
    index: int
    line: int
    level: int
    title: str
    parent: int | None


@dataclass
class Lesson:
    lines: list[str]
    sections: list[Section]
    blocks: list[Block]
    esquemas: list[Esquema]
    notes: list[Note]

    @property
    def prose_sentences(self) -> list[Sentence]:
        return [s for b in self.blocks for s in b.sentences]


def parse(text: str) -> Lesson:
    lines = text.split("\n")
    sections: list[Section] = []
    stack: list[Section] = []
    esquemas: list[Esquema] = []
    notes: list[Note] = []
    tag_of_line: dict[int, tuple[str, int]] = {}
    in_esquema: Esquema | None = None
    in_note: Note | None = None
    for number, raw in enumerate(lines, start=1):
        m = HEADING.match(raw)
        if m and in_esquema is None and in_note is None:
            level = len(m.group(1))
            while stack and stack[-1].level >= level:
                stack.pop()
            section = Section(len(sections), number, level, m.group(2).strip(), stack[-1].index if stack else None)
            sections.append(section)
            stack.append(section)
            continue
        current = stack[-1].index if stack else -1
        if ESQUEMA.match(raw):
            title = re.search(r'title="([^"]*)"', raw)
            kind = re.search(r"kind=(\w+)", raw)
            in_esquema = Esquema(number, number, title.group(1) if title else "", kind.group(1) if kind else "", current)
            esquemas.append(in_esquema)
            continue
        if NOTE.match(raw):
            kind = re.search(r"type=(\w+)", raw)
            in_note = Note(number, number, kind.group(1) if kind else "", current)
            notes.append(in_note)
            continue
        if CLOSE.match(raw):
            if in_esquema is not None:
                in_esquema.last = number
                in_esquema = None
            elif in_note is not None:
                in_note.last = number
                in_note = None
            continue
        if in_esquema is not None:
            tag_of_line[number] = ("esq", len(esquemas) - 1)
        elif in_note is not None:
            tag_of_line[number] = ("note", len(notes) - 1)
    by_block: dict[int, list[Sentence]] = {}
    for s in sentences(text):
        by_block.setdefault(s.block, []).append(s)
    section_at = _section_lookup(sections, len(lines))
    blocks: list[Block] = []
    for group in by_block.values():
        first = group[0].first_line
        last = max(s.last_line for s in group)
        tag = tag_of_line.get(first)
        if tag and tag[0] == "esq":
            esquemas[tag[1]].sentences.extend(group)
            continue
        blocks.append(Block(first, last, group[0].kind, group, section_at[first], tag[1] if tag else None))
    # A table outside a «:::esquema» is an esquema too (kind «suelta»): rows are not prose and are kept whole.
    prose: list[Block] = []
    loose: Esquema | None = None
    for b in blocks:
        if b.kind != "row":
            prose.append(b)
            loose = None
            continue
        if loose is not None and b.first - loose.last <= 2:
            loose.last = b.last
            loose.sentences.extend(b.sentences)
        else:
            loose = Esquema(b.first, b.last, "", "suelta", b.section, list(b.sentences))
            esquemas.append(loose)
    esquemas.sort(key=lambda e: e.first)
    return Lesson(lines, sections, prose, esquemas, notes)


def _section_lookup(sections: list[Section], n: int) -> list[int]:
    at = [-1] * (n + 2)
    current = -1
    heads = {s.line: s.index for s in sections}
    for line in range(1, n + 1):
        current = heads.get(line, current)
        at[line] = current
    return at


def section_path(lesson: Lesson, index: int) -> list[str]:
    path: list[str] = []
    cursor: int | None = index
    while cursor is not None and cursor >= 0:
        path.append(lesson.sections[cursor].title)
        cursor = lesson.sections[cursor].parent
    return path[::-1]


def key(s: Sentence) -> tuple[int, str]:
    return (s.block, s.id)


def rebuild(
    lesson: Lesson, keep: set[tuple[int, str]], keep_esquemas: set[int], swap: dict[str, str] | None = None
) -> str:
    """Only kept sentences, esquemas and notes with a kept sentence; headings where content is kept below them."""
    n = len(lesson.lines)
    replace: dict[int, str] = {}
    drop: set[int] = set()
    kept: set[int] = set()
    for b in lesson.blocks:
        kept_here = [s for s in b.sentences if key(s) in keep]
        span = range(b.first, b.last + 1)
        swapped = bool(swap) and any(s.id in swap for s in kept_here)  # type: ignore[operator]
        if len(kept_here) == len(b.sentences) and not swapped:
            kept.update(span)
            continue
        drop.update(span)
        if not kept_here:
            continue
        marker = ""
        if b.kind == "item":
            m = re.match(r"^(\s*(?:[-*]|\d+\.)\s+)", lesson.lines[b.first - 1])
            marker = m.group(1) if m else "- "
        replace[b.first] = marker + " ".join((swap or {}).get(s.id, s.text) for s in kept_here)
        kept.add(b.first)
    for i, e in enumerate(lesson.esquemas):
        (kept if i in keep_esquemas else drop).update(range(e.first, e.last + 1))
    for i, nt in enumerate(lesson.notes):
        inside = [s for b in lesson.blocks if b.note == i for s in b.sentences]
        if any(key(s) in keep for s in inside):
            kept.update((nt.first, nt.last))
        else:
            drop.update(range(nt.first, nt.last + 1))
    section_at = _section_lookup(lesson.sections, n)
    head_lines = {s.line: s.index for s in lesson.sections}
    populated: set[int] = set()
    for line in kept:
        if line in head_lines or not lesson.lines[line - 1].strip():
            continue
        sec = section_at[line]
        while sec >= 0:
            populated.add(sec)
            parent = lesson.sections[sec].parent
            sec = parent if parent is not None else -1
    out: list[str] = []
    for number in range(1, n + 1):
        raw = lesson.lines[number - 1]
        if number in head_lines:
            if number == 1 or head_lines[number] in populated:
                out.append(raw)
            continue
        if number in replace:
            out.append(replace[number])
            continue
        if number in drop:
            continue
        out.append(raw)
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return text.rstrip("\n") + "\n"


_ARTICLE = re.compile(r"\d+(?:\.\d+)*[\w.ºª)(\N{EN DASH}\-]*")
_NORM = re.compile(r"[A-ZÁÉÍÓÚ][A-Za-zÁÉÍÓÚ/0-9]+")
_SEPARATORS = {"y", "and", "to", "a", "\N{EN DASH}", "-", "bis", "ter", "quater"}
_SUFFIX = re.compile(r"(?:bis|ter|quater)(?:\.\d+)?[\w.ºª)(\N{EN DASH}\-]*")


def references(text: str) -> list[tuple[str, str]]:
    """(article list, norm) pairs after «art.» / «arts.»: a token scan, linear in the window."""
    found: list[tuple[str, str]] = []
    for m in re.finditer(r"\barts?\.\s+", text):
        body: list[str] = []
        for token in text[m.end() : m.end() + 200].split():
            bare = token.rstrip(",;")
            if _ARTICLE.fullmatch(bare):
                body.append(bare)
            elif bare in _SEPARATORS or bare == "" or (body and _SUFFIX.fullmatch(bare)):
                body.append(bare)
            elif body and _NORM.fullmatch(bare.rstrip(").:")):
                found.append((" ".join(body), bare.rstrip(").:")))
                break
            else:
                break
    return found


def references_full(text: str) -> list[tuple[str, str, str]]:
    """(article list, norm, 24 characters after the norm) for each reference; same scan as `references`."""
    found: list[tuple[str, str, str]] = []
    for m in re.finditer(r"\barts?\.\s+", text):
        window = text[m.end() : m.end() + 240]
        body: list[str] = []
        for tok in re.finditer(r"\S+", window):
            token = tok.group(0)
            bare = token.rstrip(",;")
            if _ARTICLE.fullmatch(bare):
                body.append(token)
            elif bare in _SEPARATORS or bare == "" or (body and _SUFFIX.fullmatch(bare)):
                body.append(token)
            elif body and _NORM.fullmatch(bare.rstrip(").:")):
                found.append((" ".join(body), bare.rstrip(").:"), window[tok.end() : tok.end() + 24]))
                break
            else:
                break
    return found
