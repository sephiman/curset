"""Script-derived C2 candidates from C1's kept questions (bank and cases); no model involved.

Run from backend/: `uv run python ../docs/age-verification/c2/bank/tools/derive_candidates.py bloque-ii`.
A C1 question becomes a candidate when its citation resolves to an anchor of a C2 lesson its C1 lesson maps to, and
every file its citation names has the same sha256 in both snapshots. Stem, options, key, explanation and citation are
copied verbatim; the record is «verificado en C1: <report>». Writes `<bloque>/<lesson>.derived.json` and
`<bloque>/derivation.md`.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

from tradeschool.citations.course import CourseCitations
from tradeschool.citations.grammar import parse_segment, segments
from tradeschool.citations.lesson import resolve_segment

ROOT = Path(__file__).resolve().parents[5]
C1 = ROOT / "content" / "age-administrativo-c1"
C2 = ROOT / "content" / "age-auxiliar-c2"
C1_BANK = ROOT / "docs" / "age-verification" / "bank"
C1_REPORT_DIRS = [ROOT / "docs" / "age-verification" / d for d in ("bank", "cases", "audit-2026-11", "audit-2026-10")]
OUT = ROOT / "docs" / "age-verification" / "c2" / "bank"

# C1 lesson → C2 lessons (bloque specs, «Mapping»), in the order tried.
MAPPING: dict[str, tuple[str, ...]] = {
    "m01-l01": ("m01-l01", "m01-l02", "m01-l03"),
    "m01-l02": ("m01-l02",),
    "m01-l03": ("m01-l03",),
    "m01-l04": ("m01-l04",),
    "m01-l05": ("m01-l05",),
    "m01-l06": ("m01-l06",),
    "m01-l07": ("m01-l07",),
    "m01-l08": ("m01-l08",),
    "m01-l09": ("m01-l09",),
    "m01-l10": ("m01-l09",),
    "m01-l11": ("m01-l10",),
    "m03-l03": ("m01-l11",),
    "m03-l02": ("m01-l11",),
    "m02-l04": ("m01-l12",),
    "m04-l01": ("m01-l13",),
    "m04-l02": ("m01-l13",),
    "m04-l03": ("m01-l13",),
    "m04-l04": ("m01-l13",),
    "m04-l05": ("m01-l13", "m01-l14"),
    "m05-l04": ("m01-l14",),
    "m04-l06": ("m01-l14",),
    "m04-l07": ("m01-l14",),
    "m05-l01": ("m01-l15",),
    "m05-l02": ("m01-l15",),
    "m05-l03": ("m01-l15",),
    "m03-l07": ("m01-l16",),
    "m02-l01": ("m02-l01", "m02-l02"),
    "m02-l02": ("m02-l03",),
    "m02-l03": ("m02-l04",),
    "m06-l01": ("m02-l05",),
    "m06-l02": ("m02-l06",),
    "m06-l03": ("m02-l07",),
    "m06-l04": ("m02-l08",),
    "m06-l05": ("m02-l09",),
    "m06-l06": ("m02-l10",),
    "m06-l07": ("m02-l11",),
    "m06-l08": ("m02-l12",),
}
BLOQUE_MODULE = {"bloque-i": "m01", "bloque-ii": "m02"}


def tema(lesson: str) -> str:
    return f"{'I' if lesson.startswith('m01') else 'II'}.{int(lesson[-2:])}"


def citations_of(course: Path) -> tuple[CourseCitations, dict[str, str]]:
    markdown = {p.stem: p.read_text(encoding="utf-8") for p in (course / "es" / "lessons").glob("*.md")}
    return CourseCitations.build(course, course.name, {"es": markdown}), markdown


def sha(course: Path, relative: str) -> str | None:
    path = course / relative
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def cited_files(cc: CourseCitations, citation: str) -> list[str] | None:
    """Course-relative files every segment of the citation names; None when one names no file."""
    files: list[str] = []
    for _, raw in segments(citation):
        segment = parse_segment(raw)
        if segment is None:
            continue
        if segment.files:
            files += [f"sources/otros/{f}" for f in segment.files]
            continue
        named = resolve_segment(segment, cc.norms) if cc.norms else None
        if named is None:
            continue
        if named[0] is None or named[0].file is None:
            return None
        files.append(named[0].file)
    return files or None


def heading_at(markdown: str, line: int) -> str:
    title = ""
    for number, text in enumerate(markdown.splitlines(), start=1):
        if number > line + 1:
            break
        if text.startswith("## ") or text.startswith("### "):
            title = text.lstrip("#").strip()
    return title


def anchor_line(cc: CourseCitations, lesson: str, anchor: str) -> int:
    found = cc.lesson(lesson, "es")
    assert found is not None
    for citation in found.prose:
        if anchor in citation.anchors:
            return citation.line
    return 0


def c1_questions() -> list[dict[str, object]]:
    """Every kept C1 question as published (built YAML), with its draft metadata where there is one."""
    meta: dict[str, dict[str, object]] = {}
    for draft in C1_BANK.glob("bloque-*/m0?-l??.draft.json"):
        for q in json.loads(draft.read_text(encoding="utf-8")):
            meta[str(q["id"])] = q
    out: list[dict[str, object]] = []
    for path in sorted((C1 / "exercises").glob("*.yaml")):
        if path.name.startswith("ofi-"):
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        case = path.stem if doc["type"] == "case" else None
        for v in doc.get("variants") or doc.get("questions") or []:
            lesson = v.get("lesson") or path.stem.split("-ex-")[0]
            options = {o["id"]: o["text"]["es"] for o in v["options"]}
            correct = next(o["id"] for o in v["options"] if o.get("correct"))
            c1_id = f"{case}/{v['id']}" if case else v["id"]
            out.append(
                {
                    "c1_id": c1_id,
                    "c1_lesson": lesson,
                    "case": case,
                    "prompt": v["prompt"]["es"],
                    "options": options,
                    "correct": correct,
                    "explanation": v["explanation"]["es"],
                    "citation": v["citation"],
                    "difficulty": v["difficulty"],
                    "tags": v.get("tags", []),
                    "c1_section": meta.get(v["id"], {}).get("section") if not case else None,
                    "distractor_pattern": meta.get(v["id"], {}).get("distractor_pattern") if not case else None,
                }
            )
    return out


ROW = re.compile(r"^\|\s*([\w/-]+?)\s*\|(.*)\|\s*$")


def c1_reports() -> dict[str, str]:
    """C1 question id → the newest report (by mtime) whose table row for it ends in PASS."""
    best: dict[str, tuple[float, str]] = {}
    for folder in C1_REPORT_DIRS:
        for report in folder.rglob("*.md"):
            mtime = report.stat().st_mtime
            prefix = report.name.split(".")[0] if report.parent.name == "cases" else ""
            for line in report.read_text(encoding="utf-8").splitlines():
                m = ROW.match(line)
                if not m or "PASS" not in m.group(2):
                    continue
                cells = [c.strip() for c in m.group(2).split("|")]
                if "PASS" not in cells:
                    continue
                qid = m.group(1)
                if prefix.startswith("sp-") and re.fullmatch(r"q\d+", qid):
                    qid = f"{prefix}/{qid}"
                if qid not in best or mtime > best[qid][0]:
                    best[qid] = (mtime, str(report.relative_to(ROOT)))
    return {qid: path for qid, (_, path) in best.items()}


def main(bloque: str) -> None:
    module = BLOQUE_MODULE[bloque]
    c1_cc, _ = citations_of(C1)
    c2_cc, c2_md = citations_of(C2)
    reports = c1_reports()
    folder = OUT / bloque
    folder.mkdir(parents=True, exist_ok=True)
    per_lesson: dict[str, list[dict[str, object]]] = defaultdict(list)
    reasons: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for q in c1_questions():
        targets = [t for t in MAPPING.get(str(q["c1_lesson"]), ()) if t.startswith(module)]
        if not targets:
            continue
        citation = str(q["citation"])
        home = targets[0]
        anchor = None
        for target in targets:
            anchor = c2_cc.question_link(target, citation, "es").anchor
            if anchor:
                home = target
                break
        if anchor is None:
            reasons[home]["no C2 anchor"] += 1
            continue
        files1, files2 = cited_files(c1_cc, citation), cited_files(c2_cc, citation)
        if not files1 or not files2:
            reasons[home]["citation names no file"] += 1
            continue
        if [Path(f).name for f in files1] != [Path(f).name for f in files2] or any(
            sha(C1, a) is None or sha(C1, a) != sha(C2, b) for a, b in zip(files1, files2, strict=True)
        ):
            reasons[home]["cited file differs"] += 1
            continue
        report = reports.get(str(q["c1_id"]))
        if report is None:
            reasons[home]["no C1 report found"] += 1
            continue
        line = anchor_line(c2_cc, home, anchor)
        section = str(q["c1_section"] or "")
        headings = {h.lstrip("#").strip() for h in c2_md[home].splitlines() if h.startswith("##")}
        if section not in headings:
            section = heading_at(c2_md[home], line)
        per_lesson[home].append(
            {
                **q,
                "lesson": home,
                "tema": tema(home),
                "section": section,
                "anchor": anchor,
                "provenance": f"verificado en C1: {report}",
            }
        )
    lines = [
        f"# Derivation — {bloque} (C1 → C2 candidates)",
        "",
        "Generated by `tools/derive_candidates.py`; no model. A candidate is a kept C1 question whose citation "
        "resolves to an anchor of the mapped C2 lesson, every cited file with the same sha256 in both snapshots.",
        "",
        "| Tema | Lesson | Candidates | of them from cases | C2 anchors covered | C2 anchors in lesson | "
        "Rejected: no anchor / file differs / no file / no report |",
        "|---|---|---|---|---|---|---|",
    ]
    total = 0
    for lesson in sorted(set(per_lesson) | set(reasons)):
        found = per_lesson.get(lesson, [])
        for n, q in enumerate(found, start=1):
            q["id"] = f"{lesson}-q{n:03d}"
        (folder / f"{lesson}.derived.json").write_text(
            json.dumps(found, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )
        cited = c2_cc.lesson(lesson, "es")
        all_anchors = {a for c in (cited.prose if cited else []) for a in c.anchors}
        r = reasons[lesson]
        lines.append(
            f"| {tema(lesson)} | {lesson} | {len(found)} | {sum(1 for q in found if q['case'])} | "
            f"{len({q['anchor'] for q in found})} | {len(all_anchors)} | {r['no C2 anchor']} / "
            f"{r['cited file differs']} / {r['citation names no file']} / {r['no C1 report found']} |"
        )
        total += len(found)
    lines += ["", f"Total candidates: {total}.", ""]
    (folder / "derivation.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main(sys.argv[1])
