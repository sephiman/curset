"""normativa.py: a lesson's «Normativa» block from the citations the lesson contains, through the registry's norm index.

One line per norm (by id, never by name similarity): «arts.» then the cited articles, runs of three or more merged into a
range, then the cited disposiciones. Lines that name a norm without citing it («nombrado en…») are kept as they stand.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "backend" / "src"))

from tradeschool.citations.grammar import _DISPOSICION  # noqa: E402
from tradeschool.citations.lesson import LessonCitation, scan_lesson  # noqa: E402
from tradeschool.citations.norms import Norm, NormIndex  # noqa: E402

COURSE = ROOT / "content" / "aeat-agentes-hacienda"
LESSONS = COURSE / "es" / "lessons"
NORM_KINDS = {"da": "adicional", "dt": "transitoria", "df": "final", "dd": "derogatoria"}
EN_DASH = "\N{EN DASH}"


def load_index() -> tuple[NormIndex, dict[str, str]]:
    markdown = {p.stem: p.read_text(encoding="utf-8") for p in LESSONS.glob("*.md")}
    return NormIndex.load(COURSE / "sources" / "normativa.yaml", markdown.values()), markdown


def _groups(citation: LessonCitation) -> list[LessonCitation]:
    return [citation, *citation.also]


def _disposiciones(citation: LessonCitation) -> list[str]:
    """«disposición adicional cuarta» per disposición unit, in the order the citation names them."""
    named = [
        f"disposición {m['kind']}" + (f" {m['ord']}" if m["ord"] else "")
        for m in (_DISPOSICION.match(part) for part in re.split(r"(?=disposici[oó]n)", citation.text) if part)
        if m
    ]
    units = [u for u in citation.units if u.kind in NORM_KINDS]
    if len(named) == len(units):
        return named
    return [f"disposición {NORM_KINDS[u.kind]} {u.number}" for u in units]


def _article_sort(number: str) -> tuple[int, str]:
    head = re.match(r"\d+", number)
    return (int(head.group(0)) if head else 0, number)


def _article_pieces(plain: set[int], suffixed: set[str]) -> list[str]:
    runs: list[list[int]] = []
    for value in sorted(plain):
        if runs and runs[-1][-1] == value - 1:
            runs[-1].append(value)
        else:
            runs.append([value])
    pieces = [(run[0], f"{run[0]}{EN_DASH}{run[-1]}") if len(run) >= 3 else None for run in runs]
    out: list[tuple[tuple[int, str], str]] = []
    for run, piece in zip(runs, pieces, strict=True):
        if piece:
            out.append(((run[0], ""), piece[1]))
        else:
            out.extend(((value, ""), str(value)) for value in run)
    out.extend((_article_sort(s), s) for s in suffixed)
    return [text for _, text in sorted(out)]


def _line(norm: Norm, arts: set[int], suffixed: set[str], others: list[str]) -> str:
    pieces = _article_pieces(arts, suffixed)
    parts: list[str] = []
    if pieces:
        label = "art." if len(pieces) == 1 and EN_DASH not in pieces[0] else "arts."
        parts.append(f"{label} {', '.join(pieces[:-1])} y {pieces[-1]}" if len(pieces) > 1 else f"{label} {pieces[0]}")
    parts.extend(others)
    body = parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + f" y {parts[-1]}"
    # a line that ends in a bare article number would read as a list marker
    return f"- {norm.short}: {body}" if re.search(r"\bart\. \d+$", body) else f"- {norm.short}: {body}."


def derive(lesson_id: str, text: str, index: NormIndex, existing: list[str]) -> list[str]:
    found = scan_lesson(lesson_id, text, index)
    arts: dict[str, set[int]] = {}
    suffixed: dict[str, set[str]] = {}
    others: dict[str, list[str]] = {}
    norms: dict[str, Norm] = {}
    for item in found.items:
        if item.section == "normativa":
            continue
        for group in _groups(item):
            if group.norm is None:
                continue
            slug = group.norm.slug
            norms[slug] = group.norm
            plain = arts.setdefault(slug, set())
            for lo, hi in group.ranges:
                plain.update(range(lo, hi + 1))
            for unit in group.units:
                if unit.kind == "art":
                    head = unit.number
                    (plain.add(int(head)) if head.isdigit() else suffixed.setdefault(slug, set()).add(head))
                elif unit.kind in NORM_KINDS:
                    continue
                else:
                    label = unit.kind if unit.kind != "preambulo" else "preámbulo"
                    piece = label if not unit.number else f"{label} {unit.number}"
                    others.setdefault(slug, [])
                    if piece not in others[slug]:
                        others[slug].append(piece)
            for piece in _disposiciones(group):
                bucket = others.setdefault(slug, [])
                if piece not in bucket:
                    bucket.append(piece)
    kept = [line for line in existing if " nombrad" in line or "Otras fuentes" in line or "no figura" in line]
    order = {Norm_label: i for i, Norm_label in enumerate(re.match(r"- ([^:]+):", line)[1] for line in existing if re.match(r"- ([^:]+):", line))}
    lines = [_line(norms[s], {a for a in arts.get(s, set()) if a}, suffixed.get(s, set()), others.get(s, [])) for s in norms]
    lines = [x for x in lines if not x.endswith(": .")]
    lines.sort(key=lambda x: order.get(re.match(r"- ([^:]+):", x)[1], len(order)))
    return lines + [k for k in kept if re.match(r"- ([^:]+?)[:,]", k)[1] not in {re.match(r"- ([^:]+):", x)[1] for x in lines}]


def block_lines(text: str) -> list[str]:
    start = text.find("\n## Normativa")
    return [x for x in text[start:].splitlines() if x.startswith("- ")] if start >= 0 else []


def rewrite(lesson_id: str, index: NormIndex, markdown: dict[str, str], write: bool) -> list[str]:
    text = markdown[lesson_id]
    cut = text.find("\n## Normativa")
    body = text[:cut] if cut >= 0 else text
    lines = derive(lesson_id, text, index, block_lines(text))
    if write and lines:
        (LESSONS / f"{lesson_id}.md").write_text(body.rstrip("\n") + "\n\n## Normativa\n\n" + "\n".join(lines) + "\n", encoding="utf-8")
    return lines


if __name__ == "__main__":
    idx, md = load_index()
    write = "--write" in sys.argv
    ids = [a for a in sys.argv[1:] if not a.startswith("--")] or sorted(k for k in md if k != "m00-l01")
    for lesson in ids:
        for line in rewrite(lesson, idx, md, write):
            print(f"{lesson}\t{line[:230]}")
