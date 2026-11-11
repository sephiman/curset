"""Draft an AEAT common-tema lesson by copying C1/C2 lesson sections verbatim, as `derivation.yaml` maps them.

Selector: `<course>:<lesson>#<heading path>`, the path being heading texts joined by « / » (enough of the path
to be unique; a leading «## » pins the level). The section is copied with every deeper heading under it; `without` drops sub-sections.
`as` replaces the selected heading line (its sub-headings shift with it). Writers fill the «PENDIENTE» blocks.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
CONTENT = ROOT / "content"
COURSES = {"c1": "age-administrativo-c1", "c2": "age-auxiliar-c2"}
TARGET = CONTENT / "aeat-agentes-hacienda"
MAP = ROOT / "docs/age-verification/aeat/r2/derivation.yaml"
REPORT = ROOT / "docs/age-verification/aeat/r2/derivation.md"
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
CROSS_REF = re.compile(r"\bm0\d-l\d\d\b")
FUENTE = re.compile(r"fuente:\s*([^\s);,]+)")
PENDING = "PENDIENTE"


@dataclass(frozen=True)
class Section:
    level: int
    path: tuple[str, ...]
    start: int
    end: int  # exclusive


def sections(lines: list[str]) -> list[Section]:
    heads: list[tuple[int, int, str]] = []
    fence = False
    for i, line in enumerate(lines):
        if line.startswith(("```", "~~~")):
            fence = not fence
        match = None if fence else HEADING.match(line)
        if match:
            heads.append((i, len(match[1]), match[2].strip()))
    found: list[Section] = []
    stack: list[tuple[int, str]] = []
    for k, (i, level, text) in enumerate(heads):
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, text))
        end = next((j for j, lv, _ in heads[k + 1 :] if lv <= level), len(lines))
        found.append(Section(level, tuple(t for _, t in stack), i, end))
    return found


def select(found: list[Section], path: str) -> Section:
    level = HEADING.match(path)  # «## Title» pins the heading level
    want = tuple(p.strip() for p in (level[2] if level else path).split(" / "))
    hits = [s for s in found if s.path[-len(want) :] == want and (not level or s.level == len(level[1]))]
    if len(hits) != 1:
        raise LookupError(f"«{path}»: {len(hits)} matches")
    return hits[0]


def copy(lines: list[str], section: Section, without: list[str], heading: str | None) -> list[str]:
    inner = sections(lines[section.start : section.end])
    drop = [select(inner, w) for w in without]
    keep = [
        line
        for i, line in enumerate(lines[section.start : section.end])
        if not any(d.start <= i < d.end for d in drop)
    ]
    if heading is None:
        return keep
    shift = len(heading.split(" ", 1)[0]) - section.level
    out = [heading]
    for line in keep[1:]:
        match = HEADING.match(line)
        out.append(f"{'#' * (len(match[1]) + shift)} {match[2]}" if match and shift else line)
    return out


def lesson_title(lesson_id: str) -> str:
    manifest = yaml.safe_load((TARGET / "course.yaml").read_text())
    for block in manifest["blocks"]:
        for module in block["modules"]:
            for lesson in module["lessons"]:
                if lesson["id"] == lesson_id:
                    return " ".join(str(lesson["title"]["es"]).split())
    raise LookupError(lesson_id)


def derive(lesson_id: str, plan: list[dict[str, object]]) -> tuple[str, list[str]]:
    title = lesson_title(lesson_id)
    body = [f"# {title}", "", f"{PENDING}: introducción (normas que rigen el tema, con título completo y sigla).", ""]
    notes: list[str] = []
    for item in plan:
        if "new" in item:
            body += [str(item["new"]), "", f"{PENDING}: {item.get('brief', 'texto nuevo')}", ""]
            notes.append(f"- nuevo · {item['new']} · {item.get('brief', '')}")
            continue
        selector = str(item["take"])
        tag, rest = selector.split(":", 1)
        lesson, path = rest.split("#", 1)
        lines = (CONTENT / COURSES[tag] / "es" / "lessons" / f"{lesson}.md").read_text().splitlines()
        section = select(sections(lines), path)
        without = [str(w) for w in item.get("without", [])]  # type: ignore[attr-defined]
        heading = item.get("as")
        chunk = copy(lines, section, without, str(heading) if heading else None)
        while chunk and not chunk[-1].strip():
            chunk.pop()
        body += chunk + [""]
        words = sum(len(line.split()) for line in chunk if not HEADING.match(line))
        notes.append(f"- {selector}" + (f" (sin: {', '.join(without)})" if without else "") + f" · {words} palabras")
        for n, line in enumerate(chunk):
            for ref in CROSS_REF.findall(line):
                notes.append(f"  - referencia a lección {ref}: «{line.strip()[:90]}»")
            for fuente in FUENTE.findall(line):
                if not (TARGET / "sources" / "otros" / fuente).exists():
                    notes.append(f"  - fuente ausente en AEAT: {fuente}")
    body += ["## Lo que más cae", "", f"{PENDING}: diez líneas.", "", "## Normativa", "", f"{PENDING}.", ""]
    return "\n".join(body), notes


def main(lesson_ids: list[str]) -> None:
    plan = yaml.safe_load(MAP.read_text())
    report = ["# Derivación R2 (borradores por script)", "", f"Generado por `tools/derive_draft.py` desde `derivation.yaml`.", ""]
    for lesson_id in lesson_ids or list(plan):
        text, notes = derive(lesson_id, plan[lesson_id])
        (TARGET / "es" / "lessons" / f"{lesson_id}.md").write_text(text)
        words = len(text.split())
        report += [f"## {lesson_id} — {words} palabras", ""] + notes + [""]
        print(f"{lesson_id}: {words} words", file=sys.stderr)
    if not lesson_ids:
        REPORT.write_text("\n".join(report))


if __name__ == "__main__":
    main(sys.argv[1:])
