"""Script-derived AEAT candidates from the kept C1 and C2 questions; no model involved.

Run from backend/: `uv run python ../docs/age-verification/aeat/bank/tools/derive_candidates.py`.
A C1 or C2 question becomes a candidate when its citation resolves to an anchor of an AEAT common lesson (I.1–II.5)
that the R2 derivation took from the question's lesson, and every file the citation names has the same sha256 in both
snapshots. Text is verbatim; the record names the origin course and its verification report. A question present in
both origins (same stem and key) is taken once, from C1. Writes `derived/<lesson>.derived.json` and `derivation.md`.
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
AEAT = ROOT / "content" / "aeat-agentes-hacienda"
C2_TOOLS = ROOT / "docs/age-verification/c2/bank/tools/derive_candidates.py"
_spec = importlib.util.spec_from_file_location("c2_derive", C2_TOOLS)
assert _spec and _spec.loader
c2d = importlib.util.module_from_spec(_spec)
sys.modules["c2_derive"] = c2d
_spec.loader.exec_module(c2d)

OUT = ROOT / "docs" / "age-verification" / "aeat" / "bank"
DERIVATION = ROOT / "docs" / "age-verification" / "aeat" / "r2" / "derivation.yaml"
C2_BANK = ROOT / "docs" / "age-verification" / "c2" / "bank"
PROVENANCE_LINE = re.compile(r"^- ([\w-]+): (.+)$")


def tema(lesson: str) -> str:
    return f"{'I' if lesson.startswith('m01') else 'II'}.{int(lesson[-2:])}"


def feeders() -> dict[str, list[str]]:
    """«c1:m01-l05» / «c2:m01-l03» → the AEAT lessons whose derivation took sections from it."""
    doc = yaml.safe_load(DERIVATION.read_text(encoding="utf-8"))
    out: dict[str, list[str]] = defaultdict(list)
    for lesson, items in doc.items():
        if not lesson.startswith(("m01-", "m02-")):
            continue
        for item in items:
            origin = str(item.get("take", "")).split("#")[0]
            if origin and lesson not in out[origin]:
                out[origin].append(lesson)
    return out


def c2_records() -> dict[str, str]:
    records: dict[str, str] = {}
    for path in C2_BANK.glob("bloque-*/provenance/*.md"):
        for line in path.read_text(encoding="utf-8").splitlines():
            m = PROVENANCE_LINE.match(line)
            if m:
                records[m.group(1)] = m.group(2)
    return records


def c2_questions() -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for path in sorted((c2d.C2 / "exercises").glob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if doc.get("type") != "quiz" or not path.name.startswith(("m01-", "m02-")):
            continue
        for v in doc.get("variants") or []:
            options = {o["id"]: o["text"]["es"] for o in v["options"]}
            out.append(
                {
                    "origin_id": v["id"],
                    "origin_lesson": path.stem.split("-ex-")[0],
                    "case": None,
                    "prompt": v["prompt"]["es"],
                    "options": options,
                    "correct": next(o["id"] for o in v["options"] if o.get("correct")),
                    "explanation": v["explanation"]["es"],
                    "citation": v["citation"],
                    "difficulty": v["difficulty"],
                    "tags": v.get("tags", []),
                }
            )
    return out


def key_of(q: dict[str, object]) -> str:
    options = q["options"]
    assert isinstance(options, dict)
    return re.sub(r"\W+", " ", f"{q['prompt']} {options[q['correct']]}").lower().strip()


def main() -> None:
    feed = feeders()
    aeat_cc, aeat_md = c2d.citations_of(AEAT)
    c1_cc, _ = c2d.citations_of(c2d.C1)
    c2_cc, _ = c2d.citations_of(c2d.C2)
    c1_reports, c2_rec = c2d.c1_reports(), c2_records()
    sources: list[tuple[str, dict[str, object]]] = []
    for q in c2d.c1_questions():
        sources.append(("c1", {**q, "origin_id": q["c1_id"], "origin_lesson": q["c1_lesson"]}))
    for q in c2_questions():
        sources.append(("c2", q))
    folder = OUT / "derived"
    folder.mkdir(parents=True, exist_ok=True)
    per_lesson: dict[str, list[dict[str, object]]] = defaultdict(list)
    seen: set[str] = set()
    reasons: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for origin, q in sources:
        targets = feed.get(f"{origin}:{q['origin_lesson']}", [])
        if not targets:
            continue
        citation = str(q["citation"])
        home, anchor = targets[0], None
        for target in targets:
            anchor = aeat_cc.question_link(target, citation, "es").anchor
            if anchor:
                home = target
                break
        if anchor is None:
            reasons[home]["no AEAT anchor"] += 1
            continue
        cc = c1_cc if origin == "c1" else c2_cc
        course = c2d.C1 if origin == "c1" else c2d.C2
        files_o, files_a = c2d.cited_files(cc, citation), c2d.cited_files(aeat_cc, citation)
        if not files_o or not files_a:
            reasons[home]["citation names no file"] += 1
            continue
        if [Path(f).name for f in files_o] != [Path(f).name for f in files_a] or any(
            c2d.sha(course, a) is None or c2d.sha(course, a) != c2d.sha(AEAT, b) for a, b in zip(files_o, files_a, strict=True)
        ):
            reasons[home]["cited file differs"] += 1
            continue
        record = (
            c1_reports.get(str(q["origin_id"])) if origin == "c1" else c2_rec.get(str(q["origin_id"]))
        )
        if record is None:
            reasons[home]["no origin report"] += 1
            continue
        if origin == "c2" and not record.startswith(("verificado en C1", "verificado: PASS")):
            reasons[home]["odd record"] += 1
            continue
        fingerprint = key_of(q)
        if fingerprint in seen:
            reasons[home]["same question in both origins"] += 1
            continue
        seen.add(fingerprint)
        line = c2d.anchor_line(aeat_cc, home, anchor)
        provenance = (
            f"verificado en C1: {record}" if origin == "c1" else f"verificado en C2: {record.removeprefix('verificado en C1: ')}"
            if record.startswith("verificado en C1") else f"verificado en C2: {record.removeprefix('verificado: PASS · ')}"
        )
        per_lesson[home].append(
            {
                "origin": origin,
                "origin_id": q["origin_id"],
                "prompt": q["prompt"],
                "options": q["options"],
                "correct": q["correct"],
                "explanation": q["explanation"],
                "citation": citation,
                "difficulty": q["difficulty"],
                "tags": q["tags"],
                "lesson": home,
                "tema": tema(home),
                "section": c2d.heading_at(aeat_md[home], line),
                "anchor": anchor,
                "provenance": provenance,
            }
        )
    lines = [
        "# Derivation — AEAT common temas (C1 and C2 banks → AEAT candidates)",
        "",
        "Generated by `tools/derive_candidates.py`; no model. A candidate is a kept C1 or C2 question whose citation",
        "resolves to an anchor of an AEAT lesson the R2 derivation fed from the question's lesson, every cited file with the",
        "same sha256 in both snapshots, with a PASS report found for its id in its origin course.",
        "",
        "| Tema | Lesson | From C1 | From C2 | Anchors covered | Rejected: no anchor / file differs / no file / no report / duplicate |",
        "|---|---|---|---|---|---|",
    ]
    total = 0
    for lesson in sorted(set(per_lesson) | set(reasons)):
        found = per_lesson.get(lesson, [])
        for n, q in enumerate(found, start=1):
            q["id"] = f"{lesson}-q{n:04d}"
        (folder / f"{lesson}.derived.json").write_text(json.dumps(found, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        r = reasons[lesson]
        lines.append(
            f"| {tema(lesson)} | {lesson} | {sum(1 for q in found if q['origin'] == 'c1')} | "
            f"{sum(1 for q in found if q['origin'] == 'c2')} | {len({q['anchor'] for q in found})} | "
            f"{r['no AEAT anchor']} / {r['cited file differs']} / {r['citation names no file']} / "
            f"{r['no origin report'] + r['odd record']} / {r['same question in both origins']} |"
        )
        total += len(found)
    lines += ["", f"Total candidates: {total}.", ""]
    (OUT / "derivation.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
