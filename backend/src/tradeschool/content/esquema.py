# SPDX-License-Identifier: AGPL-3.0-only
"""The `:::esquema` lesson block: a rule's shape laid out as rows, each a verbatim fragment with its citation.

Written as Markdown the reader's parser already knows, so glossary marks, list shape and reading time
see its words as they see prose:

    :::esquema{kind=tabla title="Recursos administrativos"}
    | Recurso | Plazo | Artículo |
    |---|---|---|
    | Alzada | Un mes | art. 122.1 LPAC |
    :::

`tabla` is a GFM table with a header row whose last column is the citation. `plazos` (paso — plazo),
`pasos` (paso — documento — órgano) and `arbol` (nodo, optionally — detalle; nesting is the parent) are
lists whose every item ends in its citation in parentheses. There is no free prose in the block.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Literal

EsquemaKind = Literal["tabla", "plazos", "arbol", "pasos"]
KINDS: tuple[EsquemaKind, ...] = ("tabla", "plazos", "arbol", "pasos")
#: Label/detail fields of a list row, besides its citation.
FIELDS: dict[str, tuple[int, int]] = {"plazos": (2, 2), "pasos": (3, 3), "arbol": (1, 2)}
FIELD_SEPARATOR = " — "

_OPEN = re.compile(r"^:::esquema(?:\{(?P<attrs>[^}\n]*)\})?[ \t]*$")
_CLOSE = re.compile(r"^:::[ \t]*$")
_ATTR = re.compile(r'(?P<key>[a-z]+)=(?:"(?P<quoted>[^"]*)"|(?P<bare>[^\s"]+))')
_LIST_ITEM = re.compile(r"^(?P<indent>[ \t]*)(?:[-*+]|\d+\.)[ \t]+(?P<text>.*)$")
_TABLE_RULE = re.compile(r"^\|?[ \t]*:?-{2,}:?[ \t]*(\|[ \t]*:?-{2,}:?[ \t]*)*\|?[ \t]*$")
_TRAILING_CITATION = re.compile(r"\((?P<citation>[^()]*(?:\([^()]*\)[^()]*)*)\)\s*$")


class EsquemaError(ValueError):
    """An esquema that breaks its own format; the message names the lesson line."""


@dataclass(frozen=True)
class EsquemaRow:
    #: Line in the lesson file (1-based), so a failing check names the row.
    line: int
    #: The row's text fields: table cells (citation column excluded) or label/detail.
    fields: tuple[str, ...]
    #: The citation as written, without parentheses; empty when the row has none.
    citation: str
    #: `arbol`: index of the parent row, None for a root.
    parent: int | None = None


@dataclass
class Esquema:
    kind: EsquemaKind
    title: str
    line: int
    #: `tabla` only: the header cells, citation column included.
    header: tuple[str, ...] = ()
    rows: list[EsquemaRow] = field(default_factory=list)
    #: Line spans (start, end) inclusive of the fences — the region prose scanners skip.
    end_line: int = 0


def _attrs(raw: str) -> dict[str, str]:
    return {m["key"]: m["quoted"] if m["quoted"] is not None else m["bare"] for m in _ATTR.finditer(raw)}


def _cells(line: str) -> list[str]:
    inner = line.strip()
    inner = inner[1:] if inner.startswith("|") else inner
    inner = inner[:-1] if inner.endswith("|") else inner
    return [cell.strip() for cell in inner.split("|")]


def _table(esquema: Esquema, lines: list[tuple[int, str]]) -> None:
    if len(lines) < 3 or not _TABLE_RULE.match(lines[1][1]):
        raise EsquemaError(f"line {esquema.line}: a tabla esquema is a table with a header row")
    esquema.header = tuple(_cells(lines[0][1]))
    for number, text in lines[2:]:
        cells = _cells(text)
        if len(cells) != len(esquema.header):
            raise EsquemaError(
                f"line {number}: {len(cells)} cells under a {len(esquema.header)}-column header"
            )
        esquema.rows.append(EsquemaRow(number, tuple(cells[:-1]), cells[-1]))


def _list(esquema: Esquema, lines: list[tuple[int, str]]) -> None:
    low, high = FIELDS[esquema.kind]
    stack: list[tuple[int, int]] = []  # (indent, row index) of the open ancestors
    for number, text in lines:
        item = _LIST_ITEM.match(text)
        if item is None:
            if esquema.rows and text.startswith((" ", "\t")):
                raise EsquemaError(f"line {number}: an esquema row is one line")
            raise EsquemaError(f"line {number}: an esquema holds rows only, no free prose")
        body = item["text"].strip()
        cited = _TRAILING_CITATION.search(body)
        citation = cited["citation"].strip() if cited else ""
        label = body[: cited.start()].strip() if cited else body
        fields = tuple(part.strip() for part in label.split(FIELD_SEPARATOR))
        if not low <= len(fields) <= high:
            raise EsquemaError(
                f"line {number}: a {esquema.kind} row has {low} to {high} fields, found {len(fields)}"
            )
        indent = len(item["indent"].expandtabs(4))
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1] if stack and esquema.kind == "arbol" else None
        if indent and esquema.kind != "arbol":
            raise EsquemaError(f"line {number}: only an arbol esquema nests")
        esquema.rows.append(EsquemaRow(number, fields, citation, parent))
        stack.append((indent, len(esquema.rows) - 1))


def parse_esquemas(markdown: str) -> list[Esquema]:
    """Every esquema in a lesson, in order. Raises EsquemaError on a malformed block."""
    found: list[Esquema] = []
    lines = markdown.splitlines()
    index = 0
    while index < len(lines):
        opened = _OPEN.match(lines[index])
        if opened is None:
            index += 1
            continue
        attrs = _attrs(opened["attrs"] or "")
        start = index + 1
        kind = attrs.get("kind", "")
        if kind not in KINDS:
            raise EsquemaError(f"line {start}: esquema kind must be one of {', '.join(KINDS)}, not {kind!r}")
        if not attrs.get("title"):
            raise EsquemaError(f"line {start}: an esquema needs a title")
        body: list[tuple[int, str]] = []
        index += 1
        while index < len(lines) and not _CLOSE.match(lines[index]):
            if lines[index].strip():
                body.append((index + 1, lines[index]))
            index += 1
        if index == len(lines):
            raise EsquemaError(f"line {start}: esquema never closed with :::")
        esquema = Esquema(kind=kind, title=attrs["title"], line=start, end_line=index + 1)
        if not body:
            raise EsquemaError(f"line {start}: an esquema without rows")
        (_table if kind == "tabla" else _list)(esquema, body)
        found.append(esquema)
        index += 1
    return found


def esquema_lines(esquemas: list[Esquema]) -> set[int]:
    """1-based lesson lines inside esquema blocks, fences included."""
    return {line for e in esquemas for line in range(e.line, e.end_line + 1)}
