"""tag_origins.py: one JSON per lesson with the origin tag and report of every sentence and esquema row.

Tags, first match wins: HEAD (pre-R2d text) · «No confundir» (inside such a note) · gap fill (in
`r2d/<lesson>/gaps.md`) · reworded (not byte-identical to a verified pool or C1/C2 sentence) · R2b restore /
review item (cited article listed in the map's «R2b removals» / confirmed «Review items») · range coverage
(any other pool sentence). The report is the one the provenance record gives for the sentence id.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "backend"))
sys.path.insert(0, str(ROOT / "docs/age-verification/aeat/r2d/tools"))

import build_check  # noqa: E402
from scripts.provenance import parse_record, sentences  # noqa: E402

LESSONS = ROOT / "content/aeat-agentes-hacienda/es/lessons"
R2D = ROOT / "docs/age-verification/aeat/r2d"
RECORDS = ROOT / "docs/age-verification/aeat/r2"
BASE = (
    (R2D_DIR := Path(__file__).resolve().parents[1]).joinpath("base-commit.txt").read_text().strip()
)  # pre-R2d commit: «HEAD» tags mean its text
CITE = re.compile(r"\(arts?\.\s*([^()]*?)\)")
ART = re.compile(r"(\d+(?:\s(?:bis|ter|quater))?)")


REF = re.compile(
    r"arts?\.\s+((?:\d+[\w.ºª)(]*(?:\s(?:bis|ter|quater))?|\s*(?:,|y|and|to|a|\N{EN DASH}|-)\s*)+?)"
    r"\s*([A-ZÁÉÍÓÚ][A-Za-zÁÉÍÓÚ/0-9]+)"
)


def _keys(text: str) -> set[str]:
    """Rough «article norm» keys of the article references in a text («195 LGT»); ranges expanded."""
    keys: set[str] = set()
    for body, norm in REF.findall(text):
        body = re.sub(r"(\d+)[.\w)(ºª]*", r"\1", body)
        for a, b in re.findall(r"(\d+)\s*(?:\N{EN DASH}|-|to|a)\s*(\d+)", body):
            if int(b) - int(a) < 300:
                keys.update(f"{n} {norm}" for n in range(int(a), int(b) + 1))
        keys.update(f"{n} {norm}" for n in re.findall(r"\d+", body))
    return keys


def _map_keys(lesson: str, heading: str) -> set[str]:
    path = R2D / f"{lesson}-map.md"
    text = path.read_text() if path.exists() else ""
    start = text.find(heading)
    if start < 0:
        return set()
    end = text.find("\n## ", start + 4)
    section = text[start : end if end > 0 else None]
    if heading == "## Review items":
        section = "\n".join(line for line in section.splitlines() if "| confirmed" in line)
    return _keys(section)


def _gap_starts(lesson: str) -> list[str]:
    path = R2D / lesson / "gaps.md"
    if not path.exists():
        return []
    starts = []
    for line in path.read_text().splitlines():
        cells = [c.strip(" `«»") for c in line.strip().strip("|").split("|")]
        for cell in cells:
            if len(cell) >= 30 and not cell.startswith("---"):
                starts.append(" ".join(cell.split())[:40])
    return starts


def _confundir_lines(text: str) -> set[int]:
    lines: set[int] = set()
    inside = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith(":::note") and "warning" in line:
            inside = True
            block: list[int] = []
            confundir = False
        elif inside and line.strip() == ":::":
            inside = False
            if confundir:
                lines.update(block)
        elif inside:
            block.append(number)
            confundir = confundir or "No confundir" in line
    return lines


_STRIPPED: dict[int, set[str]] = {}


def _row_in_pool(row: str, pool: dict[str, tuple[str, str]]) -> bool:
    """Fast path for an esquema row: a cell, marker-stripped, equals a pool text; else the full check."""
    if id(pool) not in _STRIPPED:
        _STRIPPED[id(pool)] = {build_check.MARKER.sub("", text, count=1) for text in pool} | set(pool)
    stripped = _STRIPPED[id(pool)]
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    if any(c in stripped or build_check.MARKER.sub("", c, count=1) in stripped for c in cells):
        return True
    return build_check._row_twin(row, pool) is not None


def tag(lesson: str, pool: dict[str, tuple[str, str]]) -> list[dict[str, object]]:
    path = LESSONS / f"{lesson}.md"
    text = path.read_text()
    head_text = subprocess.run(
        ["git", "show", f"{BASE}:content/aeat-agentes-hacienda/es/lessons/{lesson}.md"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    ).stdout
    head = {s.text for s in sentences(head_text)}
    record_path = RECORDS / f"{lesson}.md"
    records = (
        {r.sentence_id: r for r in parse_record(record_path.read_text())} if record_path.exists() else {}
    )
    r2b = _map_keys(lesson, "## R2b removals")
    review = _map_keys(lesson, "## Review items")
    gaps = _gap_starts(lesson)
    confundir = _confundir_lines(text)
    out: list[dict[str, object]] = []
    for s in sentences(text):
        record = records.get(s.id)
        report = (
            (f"inherited from {record.origin} {record.detail}" if record.inherited else record.report)
            if record
            else ""
        )
        flat = " ".join(s.text.split())
        if s.text in head:
            origin = "HEAD"
        elif s.first_line in confundir:
            origin = "No confundir"
        elif any(flat.startswith(g) or g in flat for g in gaps):
            origin = "gap fill"
        elif s.text not in pool and (s.kind != "row" or not _row_in_pool(s.text, pool)):
            origin = "reworded"
        else:
            keys = _keys(s.text)
            origin = "R2b restore" if keys & r2b else "review item" if keys & review else "range coverage"
        out.append({"id": s.id, "line": s.first_line, "kind": s.kind, "origin": origin, "report": report})
    return out


def main(argv: list[str]) -> int:
    pool = build_check._pool()
    target = R2D / "tags"
    target.mkdir(exist_ok=True)
    lessons = argv or sorted(p.stem for p in LESSONS.glob("m0*.md"))
    for lesson in lessons:
        rows = tag(lesson, pool)
        (target / f"{lesson}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n")
        counts: dict[str, int] = {}
        for row in rows:
            counts[str(row["origin"])] = counts.get(str(row["origin"]), 0) + 1
        print(lesson, len(rows), counts)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
