# SPDX-License-Identifier: AGPL-3.0-only
"""`:::diagram{kind="…" caption="…"}` blocks: text inside the lesson file, drawn as SVG when the course loads.

Contract in docs/backend-verification/s1/contracts.md. The body is `description: …`, `id: label` node lines
and `a -> b: label` edge lines (`-->` is a dashed return); a timeline node reads `id: when | label`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from html import escape

KINDS = ("sequence", "state", "flow", "structure", "timeline")
MAX_NODES = 12

_FENCED_CODE = re.compile(r"^[ \t]*(```|~~~).*?^[ \t]*\1[ \t]*$", re.DOTALL | re.MULTILINE)
_OPENING = re.compile(r"^[ \t]*:::diagram", re.MULTILINE)
_BLOCK = re.compile(
    r"^:::diagram(?P<attrs>\{(?:[^}\"']|\"[^\"]*\"|'[^']*')*\})?[ \t]*\n(?P<body>.*?)^:::[ \t]*$",
    re.DOTALL | re.MULTILINE,
)
_ATTRIBUTE = re.compile(r"\s*(?P<name>[\w-]+)=(?:\"(?P<double>[^\"]*)\"|'(?P<single>[^']*)')\s*")
_ID = r"[a-z][a-z0-9_]*"
_NODE = re.compile(rf"^(?P<id>{_ID}):\s*(?P<label>\S.*)$")
_EDGE = re.compile(rf"^(?P<src>{_ID})\s*(?P<arrow>-->|->)\s*(?P<dst>{_ID})(?:\s*:\s*(?P<label>.*))?$")
_ALLOWED_ATTRIBUTES = {"kind", "caption"}


@dataclass(frozen=True)
class Node:
    id: str
    label: str
    when: str = ""


@dataclass(frozen=True)
class Edge:
    src: str
    dst: str
    label: str
    dashed: bool


@dataclass(frozen=True)
class Diagram:
    id: str
    kind: str
    caption: str
    description: str
    nodes: tuple[Node, ...]
    edges: tuple[Edge, ...]


@dataclass(frozen=True)
class Block:
    """A diagram block as found in a lesson file, with the span of text it occupies."""

    start: int
    end: int
    attributes: dict[str, str] | None
    body: str


def blocks_of(markdown: str) -> list[Block]:
    # fenced code may show the syntax; blank it out so it is neither parsed nor substituted
    masked = _FENCED_CODE.sub(lambda m: " " * len(m.group(0)), markdown)
    return [
        Block(m.start(), m.end(), _attributes(m.group("attrs") or "{}"), m.group("body"))
        for m in _BLOCK.finditer(masked)
    ]


def _attributes(braced: str) -> dict[str, str] | None:
    inner, found, position = braced[1:-1], {}, 0
    while position < len(inner):
        match = _ATTRIBUTE.match(inner, position)
        if match is None:
            return None
        found[match["name"]] = match["double"] if match["double"] is not None else match["single"]
        position = match.end()
    return found


def parse_block(diagram_id: str, block: Block) -> Diagram | list[str]:
    """The diagram, or every problem found in the block."""
    lesson_id, _, number = diagram_id.rpartition("-d")
    where = f"lesson {lesson_id}, diagram {number}"
    if block.attributes is None:
        return [f'{where}: attributes must be name="value" pairs']
    attributes = block.attributes
    problems = [f"{where}: unknown attribute {a}" for a in sorted(set(attributes) - _ALLOWED_ATTRIBUTES)]
    kind, caption = attributes.get("kind", ""), attributes.get("caption", "").strip()
    if kind not in KINDS:
        problems.append(f"{where}: `kind` must be one of {', '.join(KINDS)}")
    if not caption:
        problems.append(f"{where}: `caption` is required")
    description, nodes, edges = "", [], []
    for line_no, raw in enumerate(block.body.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("description:"):
            description = line.removeprefix("description:").strip()
        elif edge := _EDGE.match(line):
            edges.append(
                Edge(edge["src"], edge["dst"], (edge["label"] or "").strip(), edge["arrow"] == "-->")
            )
        elif node := _NODE.match(line):
            when, bar, label = node["label"].partition("|")
            if kind != "timeline" or not bar:
                when, label = "", node["label"]
            nodes.append(Node(node["id"], label.strip(), when.strip()))
        else:
            problems.append(f"{where}, line {line_no}: not a node, an edge or the description: {line[:50]!r}")
    if not description:
        problems.append(f"{where}: `description:` line is required")
    problems += _structure_problems(where, kind, nodes, edges)
    if problems:
        return problems
    return Diagram(diagram_id, kind, caption, description, tuple(nodes), tuple(edges))


def _structure_problems(where: str, kind: str, nodes: list[Node], edges: list[Edge]) -> list[str]:
    ids = [n.id for n in nodes]
    problems = [f"{where}: node {i} declared twice" for i in sorted(set(ids)) if ids.count(i) > 1]
    if not nodes:
        problems.append(f"{where}: no nodes")
    if len(nodes) > MAX_NODES:
        problems.append(f"{where}: {len(nodes)} nodes, at most {MAX_NODES}")
    problems += [f"{where}: node {n.id} has an empty label" for n in nodes if not n.label]
    for edge in edges:
        problems += [
            f"{where}: edge {edge.src} -> {edge.dst} names undeclared node {i}"
            for i in (edge.src, edge.dst)
            if i not in ids
        ]
    if kind == "timeline" and edges:
        problems.append(f"{where}: a timeline has events, not edges")
    if kind == "timeline" and any(not n.when for n in nodes):
        problems.append(f"{where}: every timeline event reads `id: when | label`")
    if kind in ("sequence", "state", "flow", "structure") and nodes and not edges:
        problems.append(f"{where}: a {kind} diagram needs at least one edge")
    return problems


def problems_in(lesson_id: str, markdown: str) -> list[str]:
    blocks = blocks_of(markdown)
    problems = [
        problem
        for number, block in enumerate(blocks, start=1)
        for problem in _problems_of(parse_block(f"{lesson_id}-d{number}", block))
    ]
    masked = _FENCED_CODE.sub(lambda m: " " * len(m.group(0)), markdown)
    if len(_OPENING.findall(masked)) != len(blocks):
        problems.append(
            f"lesson {lesson_id}: a `:::diagram` opening is indented or its closing `:::` is missing"
        )
    return problems


def _problems_of(parsed: Diagram | list[str]) -> list[str]:
    return parsed if isinstance(parsed, list) else []


def locale_problems(markdown: dict[str, dict[str, str]]) -> list[str]:
    """Languages of one lesson must draw the same number of diagrams: the placeholders pair up by id."""
    problems = []
    lesson_ids = {lid for lessons in markdown.values() for lid in lessons}
    for lesson_id in sorted(lesson_ids):
        counts = {
            loc: len(blocks_of(lessons[lesson_id]))
            for loc, lessons in markdown.items()
            if lesson_id in lessons
        }
        if len(set(counts.values())) > 1:
            problems.append(f"lesson {lesson_id}: languages hold different numbers of diagrams {counts}")
    return problems


def diagrams_in(lesson_id: str, markdown: str) -> list[Diagram]:
    parsed = [parse_block(f"{lesson_id}-d{n}", b) for n, b in enumerate(blocks_of(markdown), start=1)]
    return [p for p in parsed if isinstance(p, Diagram)]


def with_placeholders(lesson_id: str, markdown: str) -> str:
    """The lesson text with each diagram block replaced by a `::diagram{id="…"}` leaf directive."""
    out, position = [], 0
    for number, block in enumerate(blocks_of(markdown), start=1):
        out += [markdown[position : block.start], f'::diagram{{id="{lesson_id}-d{number}"}}']
        position = block.end
    return "".join(out) + markdown[position:]


def without_blocks(markdown: str) -> str:
    """The lesson text with every diagram block removed, for what counts only prose (reading time)."""
    out, position = [], 0
    for block in blocks_of(markdown):
        out.append(markdown[position : block.start])
        position = block.end
    return "".join(out) + markdown[position:]


# --- drawing ------------------------------------------------------------------------------------

CHAR = 7.4
LINE = 16
PAD_X = 12
PAD_Y = 8
GAP_X = 28
GAP_Y = 46
MARGIN = 14
WRAP = 24


@dataclass(frozen=True)
class Palette:
    ink: str
    fill: str
    line: str
    accent: str


#: Web colours are CSS variables defined in index.css per theme; print colours are fixed light values.
WEB = Palette("var(--diagram-ink)", "var(--diagram-fill)", "var(--diagram-line)", "var(--diagram-accent)")
PRINT = Palette("#111827", "#f3f4f6", "#6b7280", "#4f46e5")


def _wrap(text: str, width: int = WRAP) -> list[str]:
    lines: list[str] = []
    for word in text.split():
        if lines and len(lines[-1]) + 1 + len(word) <= width:
            lines[-1] += f" {word}"
        else:
            lines.append(word)
    return lines or [""]


def _text(
    x: float, y: float, lines: list[str], p: Palette, anchor: str = "middle", bold: bool = False
) -> str:
    weight = ' font-weight="600"' if bold else ""
    spans = "".join(
        f'<tspan x="{x:.1f}" dy="{0 if i == 0 else LINE}">{escape(line)}</tspan>'
        for i, line in enumerate(lines)
    )
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" fill="{p.ink}"{weight}>{spans}</text>'


def _box(x: float, y: float, w: float, h: float, lines: list[str], p: Palette, rounded: bool) -> str:
    radius = 14 if rounded else 4
    top = y + PAD_Y + 11 + (h - 2 * PAD_Y - len(lines) * LINE) / 2
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{radius}" fill="{p.fill}" '
        f'stroke="{p.line}" stroke-width="1.5"/>' + _text(x + w / 2, top, lines, p)
    )


def _svg(width: float, height: float, d: Diagram, body: str, p: Palette) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}" width="{width:.0f}" '
        f'height="{height:.0f}" role="img" font-family="system-ui, sans-serif" font-size="13">'
        f"<title>{escape(d.caption)}</title><desc>{escape(d.description)}</desc>"
        f'<defs><marker id="{d.id}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{p.line}"/>'
        f"</marker></defs>{body}</svg>"
    )


def _line(
    x1: float, y1: float, x2: float, y2: float, d: Diagram, p: Palette, dashed: bool, arrow: bool = True
) -> str:
    dash = ' stroke-dasharray="5 4"' if dashed else ""
    end = f' marker-end="url(#{d.id}-arrow)"' if arrow else ""
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{p.line}" stroke-width="1.5"{dash}{end}/>'
    )


def render(d: Diagram, p: Palette) -> str:
    drawn = {"sequence": _sequence, "timeline": _timeline}.get(d.kind, _layered)(d, p)
    width, height, body = drawn
    return _svg(width, height, d, body, p)


def _size(label: str) -> tuple[list[str], float, float]:
    lines = _wrap(label)
    return lines, max(len(line) for line in lines) * CHAR + 2 * PAD_X, len(lines) * LINE + 2 * PAD_Y


def _layers(d: Diagram) -> tuple[dict[str, int], set[tuple[str, str]]]:
    """Layer per node by longest path over the forward edges; `back` holds the edges that close a cycle."""
    order = {n.id: i for i, n in enumerate(d.nodes)}
    back: set[tuple[str, str]] = set()
    state: dict[str, int] = {}

    def visit(node: str) -> None:
        state[node] = 1
        for e in d.edges:
            if e.src != node:
                continue
            if state.get(e.dst) == 1 or e.src == e.dst:
                back.add((e.src, e.dst))
            elif e.dst not in state:
                visit(e.dst)
        state[node] = 2

    for n in d.nodes:
        if n.id not in state:
            visit(n.id)
    layer = {n.id: 0 for n in d.nodes}
    for _ in d.nodes:
        for e in d.edges:
            if (e.src, e.dst) not in back and layer[e.dst] < layer[e.src] + 1:
                layer[e.dst] = layer[e.src] + 1
    return dict(sorted(layer.items(), key=lambda kv: order[kv[0]])), back


def _layered(d: Diagram, p: Palette) -> tuple[float, float, str]:
    layer, back = _layers(d)
    sizes = {n.id: _size(n.label) for n in d.nodes}
    rows: dict[int, list[str]] = {}
    for node_id, row in layer.items():
        rows.setdefault(row, []).append(node_id)
    row_width = {r: sum(sizes[i][1] for i in ids) + GAP_X * (len(ids) - 1) for r, ids in rows.items()}
    inner = max(row_width.values())
    label_width = max((max(len(w) for w in _wrap(e.label, 28)) * CHAR for e in d.edges if e.label), default=0)
    looping = any(layer[e.dst] - layer[e.src] != 1 or (e.src, e.dst) in back for e in d.edges)
    # a label beside a straight edge is drawn from the edge's x, so it needs room even without loops
    right = 56 + label_width if looping else 0.0
    pos: dict[str, tuple[float, float, float, float]] = {}
    y = float(MARGIN)
    for r in sorted(rows):
        row_height = max(sizes[i][2] for i in rows[r])
        x = MARGIN + (inner - row_width[r]) / 2
        for node_id in rows[r]:
            _, w, h = sizes[node_id]
            pos[node_id] = (x, y + (row_height - h) / 2, w, h)
            x += w + GAP_X
        y += row_height + GAP_Y
    parts: list[str] = []
    for e in d.edges:
        parts.append(_layered_edge(d, p, e, pos, layer, back, MARGIN + inner))
    for n in d.nodes:
        x, ny, w, h = pos[n.id]
        parts.append(_box(x, ny, w, h, sizes[n.id][0], p, rounded=d.kind == "state"))
    label_room = label_width + 14 if right == 0 else 0
    width = MARGIN * 2 + inner + right + label_room
    return width, y - GAP_Y + MARGIN, "".join(parts)


def _layered_edge(
    d: Diagram,
    p: Palette,
    e: Edge,
    pos: dict[str, tuple[float, float, float, float]],
    layer: dict[str, int],
    back: set[tuple[str, str]],
    edge_x: float,
) -> str:
    sx, sy, sw, sh = pos[e.src]
    tx, ty, tw, th = pos[e.dst]
    arrow = d.kind != "structure"
    dash = ' stroke-dasharray="5 4"' if e.dashed else ""
    end = f' marker-end="url(#{d.id}-arrow)"' if arrow else ""
    if layer[e.dst] - layer[e.src] == 1 and (e.src, e.dst) not in back:
        x1, y1, x2, y2 = sx + sw / 2, sy + sh, tx + tw / 2, ty
        label = _text(max(x1, x2) + 6, (y1 + y2) / 2 + 4, _wrap(e.label, 28), p, "start") if e.label else ""
        return _line(x1, y1, x2, y2, d, p, e.dashed, arrow) + label
    # a back edge, a self edge or an edge that skips rows loops out on the right of the diagram
    out = edge_x + 30 + 8 * (layer[e.src] % 3)
    y1, y2 = sy + sh / 2, ty + th / 2
    path = f"M{sx + sw:.1f},{y1:.1f} L{out:.1f},{y1:.1f} L{out:.1f},{y2:.1f} L{tx + tw:.1f},{y2:.1f}"
    label = _text(out + 6, (y1 + y2) / 2 + 4, _wrap(e.label, 28), p, "start") if e.label else ""
    return f'<path d="{path}" fill="none" stroke="{p.line}" stroke-width="1.5"{dash}{end}/>' + label


def _sequence(d: Diagram, p: Palette) -> tuple[float, float, str]:
    index = {n.id: i for i, n in enumerate(d.nodes)}
    labels = [_wrap(e.label, 30) if e.label else [] for e in d.edges]
    spacing = 150.0
    for e, lines in zip(d.edges, labels, strict=True):
        span = max(abs(index[e.dst] - index[e.src]), 1)
        spacing = max(spacing, (max((len(line) for line in lines), default=0) * CHAR + 28) / span)
    sizes = [_size(n.label) for n in d.nodes]
    head = max(s[2] for s in sizes)
    centre = [MARGIN + spacing / 2 + i * spacing for i in range(len(d.nodes))]
    rows, y = [], MARGIN + head + 20.0
    for lines in labels:
        y += 30 + max(len(lines) - 1, 0) * LINE
        rows.append(y)
    height = y + 16
    parts = []
    for i in range(len(d.nodes)):
        lines, w, _ = sizes[i]
        parts.append(_line(centre[i], MARGIN + head, centre[i], height - 6, d, p, True, arrow=False))
        parts.append(_box(centre[i] - w / 2, MARGIN, w, head, lines, p, rounded=False))
    for e, lines, y in zip(d.edges, labels, rows, strict=True):
        x1, x2 = centre[index[e.src]], centre[index[e.dst]]
        if x1 == x2:
            parts.append(_self_message(d, p, e, x1, y))
            continue
        parts.append(_line(x1, y, x2, y, d, p, e.dashed))
        if lines:
            parts.append(_text((x1 + x2) / 2, y - 7 - (len(lines) - 1) * LINE, lines, p))
    return MARGIN * 2 + spacing * len(d.nodes), height, "".join(parts)


def _self_message(d: Diagram, p: Palette, e: Edge, x: float, y: float) -> str:
    dash = ' stroke-dasharray="5 4"' if e.dashed else ""
    path = (
        f"M{x:.1f},{y - 8:.1f} L{x + 34:.1f},{y - 8:.1f} L{x + 34:.1f},{y + 8:.1f} L{x + 2:.1f},{y + 8:.1f}"
    )
    arrow = (
        f'<path d="{path}" fill="none" stroke="{p.line}" stroke-width="1.5"{dash} '
        f'marker-end="url(#{d.id}-arrow)"/>'
    )
    return arrow + (_text(x + 42, y + 4, _wrap(e.label, 30), p, "start") if e.label else "")


def _timeline(d: Diagram, p: Palette) -> tuple[float, float, str]:
    when_width = max(len(n.when) for n in d.nodes) * CHAR
    axis = MARGIN + when_width + 18
    parts, y, last_dot = [], float(MARGIN), float(MARGIN)
    rows = [(n, _wrap(n.label, 40)) for n in d.nodes]
    for n, lines in rows:
        height = max(len(lines) * LINE, LINE) + 14
        last_dot = y + 8
        parts.append(_text(MARGIN + when_width, y + 12, [n.when], p, "end", bold=True))
        parts.append(f'<circle cx="{axis:.1f}" cy="{y + 8:.1f}" r="5" fill="{p.accent}"/>')
        parts.append(_text(axis + 16, y + 12, lines, p, "start"))
        y += height
    parts.insert(0, _line(axis, MARGIN + 8, axis, last_dot, d, p, False, arrow=False))
    widest = max(len(line) for _, lines in rows for line in lines)
    return axis + 16 + widest * CHAR + MARGIN, y + MARGIN - 6, "".join(parts)


def rendered(diagram: Diagram) -> dict[str, str]:
    """The payload the web and the PDF exporter read: caption, description and the two drawings."""
    return {
        "id": diagram.id,
        "kind": diagram.kind,
        "caption": diagram.caption,
        "description": diagram.description,
        "svg": render(diagram, WEB),
        "svgPrint": render(diagram, PRINT),
    }
