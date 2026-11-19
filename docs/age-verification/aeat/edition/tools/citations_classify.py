"""citations_classify.py: sort every row of the citations golden by what explains it against HEAD; read only «ANYTHING ELSE».

Each current row (the registry's own scan, equal to the golden) falls in one class:
  layer citation without anchor   — inside overview / Preguntas / Caso / Para / Término, never a first anchor;
  unchanged                       — the same row existed in HEAD;
  anchor moved with its sentence  — as in HEAD except for the first-anchor column, and the sentence that now holds the first
                                    citation of that anchor is a restored/moved literal sentence (a line absent from HEAD, present in the R2d pool);
  literal sentence moved/restored — its line is in HEAD or in the R2d pool lesson (step-2 defect sweep);
  normativa line new in step 0    — the «Normativa» block rebuilt from the registry scan;
  esquema / Normativa row (new)   — a table row or Normativa line new against HEAD, whose line is in HEAD or the pool;
and every HEAD row that has no current counterpart (removed rows) must be a reformatted twin (same lesson, section, norm, target).
"""

from __future__ import annotations

import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "backend" / "tests"))

from pipeline_courses import course_dir, pipeline_courses  # noqa: E402

GOLDEN = "content/aeat-agentes-hacienda/citations.es.txt"
POOL_COMMIT = "8f5434d"


def git_lines(commit: str, path: str) -> set[str]:
    out = subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True, text=True, cwd=ROOT).stdout
    return {line.strip() for line in out.split("\n") if line.strip()}


def squash(text: str) -> str:
    return " ".join(text.split())


def pre_lines(lesson: str) -> set[str]:
    path = ROOT / "docs/age-verification/aeat/edition/pre" / f"{lesson}.md"
    return {line.strip() for line in path.read_text(encoding="utf-8").split("\n") if line.strip()} if path.exists() else set()


def whole(commit: str, path: str) -> str:
    return squash(subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True, text=True, cwd=ROOT).stdout)


def current_rows() -> list[tuple[str, bool, str]]:
    course = next(c for c in pipeline_courses() if c.slug == "aeat-agentes-hacienda")
    rows: list[tuple[str, bool, str]] = []
    texts: dict[str, list[str]] = {}
    for _module, lesson in course.manifest.iter_lessons():
        found = course.citations.lesson(lesson.id, "es")
        payload = course.citations.lesson_payload(lesson.id, "es")
        texts[lesson.id] = (course_dir(course) / "es" / "lessons" / f"{lesson.id}.md").read_text(encoding="utf-8").split("\n")
        for item, shipped in zip(found.items, payload, strict=True):
            named = item.norm.slug if item.norm else (f"?{item.norm_slug}" if item.norm_slug else "-")
            target = str(shipped["href"]).removeprefix(f"/api/courses/{course.slug}/") if shipped["href"] else "-"
            row = "\t".join([lesson.key, item.section, ",".join(item.anchors) or "-", ",".join(shipped["ids"]) or "-", named, target, item.text])
            rows.append((row, item.layer, texts[lesson.id][item.line - 1].strip()))
    return rows


def without_ids(row: str) -> str:
    cells = row.split("\t")
    return "\t".join(cells[:3] + cells[4:])


def main() -> int:
    golden = [line for line in (ROOT / GOLDEN).read_text(encoding="utf-8").split("\n") if line and not line.startswith("#")]
    scanned = current_rows()
    assert [r for r, _l, _t in scanned] == golden, "the scan no longer reproduces the golden"
    old_text = subprocess.run(["git", "show", f"HEAD:{GOLDEN}"], capture_output=True, text=True, check=True, cwd=ROOT).stdout
    old_rows = [line for line in old_text.split("\n") if line and not line.startswith("#")]
    exact, loose = Counter(old_rows), Counter(without_ids(r) for r in old_rows)
    head: dict[str, set[str]] = {}
    pool: dict[str, set[str]] = {}
    bodies: dict[str, str] = {}
    earlier: dict[str, set[str]] = {}
    first_line: dict[tuple[str, str], str] = {}
    for row, layer, text in scanned:
        cells = row.split("\t")
        if cells[1] == "prose" and not layer and cells[3] != "-":
            for anchor in cells[3].split(","):
                first_line[(cells[0], anchor)] = text
    classes: dict[str, list[str]] = defaultdict(list)
    left: list[tuple[str, bool, str]] = []
    for row, layer, text in scanned:
        key = row.split("\t")[0]
        if key not in head:
            path = f"content/aeat-agentes-hacienda/es/lessons/{key}.md"
            head[key], pool[key] = git_lines("HEAD", path), git_lines(POOL_COMMIT, path)
            bodies[key] = whole("HEAD", path) + " " + whole(POOL_COMMIT, path)
            earlier[key] = pre_lines(key)
        cells = row.split("\t")
        if layer:
            classes["layer citation without anchor" if cells[3] == "-" else "ANYTHING ELSE: layer citation that is a first anchor"].append(row)
        elif exact[row] > 0:
            exact[row] -= 1
            loose[without_ids(row)] -= 1
            classes["unchanged"].append(row)
        elif loose[without_ids(row)] > 0:
            loose[without_ids(row)] -= 1
            anchors = [a for a in cells[2].split(",") if a != "-"]
            held = [first_line.get((key, a), "") for a in anchors]
            restored = any(h and (h in head[key] or h in pool[key]) for h in held)
            classes["anchor moved with its sentence"if restored else "ANYTHING ELSE: first-anchor column changed, no restored sentence holds it"].append(row)
        elif cells[1] == "esquema" and text in earlier[key]:
            classes["esquema row restored whole from the pre-R2d lesson (edition/pre)"].append(row)
        elif text in head[key] or text in pool[key]:
            classes["literal sentence moved, restored or repeated (its line is in HEAD or the R2d pool)" if cells[1] == "prose" else f"{cells[1]} row from HEAD or the pool"].append(row)
        elif cells[1] == "prose" and squash(text).removeprefix("- ") in bodies[key]:
            classes["literal sentence re-laid (same words inside a HEAD or pool line, list marker or line break differs)"].append(row)
        elif cells[1] == "normativa":
            classes["normativa line new in step 0 (rebuilt from the scan; blind-checked in normativa-check/)"].append(row)
        else:
            classes["ANYTHING ELSE: line in neither HEAD nor the pool"].append(row)
    removed = [r for r, n in exact.items() for _ in range(n)]
    twins = Counter(c for row, _l, _t in scanned for c in [tuple(row.split("\t")[:2] + row.split("\t")[4:6])])
    for row in removed:
        cells = row.split("\t")
        classes["removed row (reformatted)" if twins[tuple(cells[:2] + cells[4:6])] else "ANYTHING ELSE: removed row"].append(row)
    for name in sorted(classes, key=lambda n: (n.startswith("ANYTHING"), n)):
        print(f"{len(classes[name]):6d}  {name}")
    for name in sorted(classes):
        if name.startswith("ANYTHING"):
            print(f"\n== {name}")
            print("\n".join(r[:400] for r in classes[name]))
    return 1 if any(n.startswith("ANYTHING") for n in classes) else 0


if __name__ == "__main__":
    raise SystemExit(main())
