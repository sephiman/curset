"""taxprov.py plan|record|apply <lesson…>: provenance for the AEAT tax lessons (m03), reports under r2-tax/<lesson>/.

plan: r2-tax/<lesson>/pending.md lists the sentences with neither a C1/C2 origin nor a PASS. record: writes the
provenance record where test_provenance.py reads it (aeat/r2/<lesson>.md). apply <lesson> <report>: applies the
report's FAIL replacements to the lesson. Every C1 and C2 lesson is a candidate origin (the tax temas have no map).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "backend"))

from scripts.provenance import (  # noqa: E402
    INHERITED,
    INHERITED_C2,
    VERIFIED,
    LessonText,
    Sentence,
    _c2_record,
    c1_report,
    find_origin,
    report_verdicts,
)
from tests.pipeline_courses import course_dir, pipeline_courses  # noqa: E402

TAX = ROOT / "docs/age-verification/aeat/r2-tax"
RECORDS = ROOT / "docs/age-verification/aeat/r2"


def _order(report: Path) -> tuple[str, int]:
    base, _, number = report.stem.partition("-recheck-")
    return base, int(number) if number.isdigit() else 0


def verdicts(lesson_id: str) -> dict[str, tuple[str, str]]:
    """Sentence id → (verdict, report); re-checks win over the report they re-check, highest number last."""
    out: dict[str, tuple[str, str]] = {}
    for report in sorted((TAX / lesson_id).glob("verify*.md"), key=_order):
        for sid, verdict in report_verdicts(report).items():
            out[sid] = (verdict, str(report.relative_to(ROOT)))
    return out


def lessons_of(course: object) -> list[LessonText]:
    root = course_dir(course)
    found = []
    for path in sorted((root / "es" / "lessons").glob("m*.md")):
        citations = course.citations.lesson(path.stem, "es")  # type: ignore[attr-defined]
        if citations is not None:
            found.append(LessonText(path.stem, path.read_text(), citations, root))
    return found


def main(command: str, lesson_ids: list[str]) -> int:
    courses = {c.slug: c for c in pipeline_courses()}
    target, c1, c2 = (
        courses["aeat-agentes-hacienda"],
        courses["age-administrativo-c1"],
        courses["age-auxiliar-c2"],
    )
    c1_lessons, c2_lessons = lessons_of(c1), lessons_of(c2)
    c1_by_id = {lt.lesson_id: lt for lt in c1_lessons}
    targets = {lt.lesson_id: lt for lt in lessons_of(target)}
    status = 0
    for lesson_id in lesson_ids:
        lesson = targets[lesson_id]
        found = verdicts(lesson_id)
        entries: list[str] = []
        pending: list[str] = []
        seen: set[str] = set()
        inherited = verified = 0
        keyed = lesson.keyed()
        for sentence, keys in keyed:
            if sentence.id in seen:
                continue
            seen.add(sentence.id)
            # The audit checks every occurrence: a repeated sentence inherits only if each occurrence does.
            others = [k for s2, k in keyed if s2.id == sentence.id and k != keys]
            entry = None if others else _inherited_entry(sentence, keys, c1_lessons, c2_lessons, c1_by_id)
            if entry is not None:
                entries += [entry, f"  > {sentence.text}"]
                inherited += 1
            elif found.get(sentence.id, ("", ""))[0] == "PASS":
                entries += [
                    f"- `{sentence.id}` · {VERIFIED}: PASS · {found[sentence.id][1]}",
                    f"  > {sentence.text}",
                ]
                verified += 1
            else:
                cited = (
                    ", ".join(sorted({t for t, _ in keys}))
                    if keys
                    else ("—" if keys is not None else "sin fichero")
                )
                pending.append(
                    f"| `{sentence.id}` | {sentence.first_line} | {sentence.text.replace('|', '\\|')} | {cited} |"
                )
        if command == "plan":
            (TAX / lesson_id).mkdir(parents=True, exist_ok=True)
            (TAX / lesson_id / "pending.md").write_text(
                f"# Pending sentences — `{lesson_id}`\n\n{len(pending)} to verify; {inherited} inherited; {verified} "
                f"already PASS.\n\n| id | line | sentence | governing citations |\n|---|---|---|---|\n"
                + "\n".join(pending)
                + "\n"
            )
            print(f"{lesson_id}: {inherited} inherited, {verified} verified, {len(pending)} pending")
            continue
        if pending:
            print(f"{lesson_id}: {len(pending)} sentences have neither provenance nor a PASS")
            status = 1
            continue
        (RECORDS / f"{lesson_id}.md").write_text(
            f"# Registro de procedencia — `{lesson_id}`\n\nR2.3: cada frase lleva «{INHERITED}» o «{INHERITED_C2}»: "
            f"<informe> (idéntica a C1 o a C2, misma cita, mismo sha256) o «{VERIFIED}: PASS · <informe>». Generado por "
            f"`docs/age-verification/aeat/r2-tax/tools/taxprov.py` (funciones de `backend/scripts/provenance.py`); lo "
            f"comprueba `backend/tests/test_provenance.py`.\n\nFrases: {inherited + verified} · heredadas: {inherited} · "
            f"verificadas: {verified}.\n\n" + "\n".join(entries) + "\n"
        )
        print(f"{lesson_id}: record written ({inherited} inherited, {verified} verified)")
    return status


def _inherited_entry(
    sentence: Sentence,
    keys: frozenset[tuple[str, str]] | None,
    c1_lessons: list[LessonText],
    c2_lessons: list[LessonText],
    c1_by_id: dict[str, LessonText],
) -> str | None:
    origin = find_origin(sentence, keys, c1_lessons)
    if origin is not None:
        return _c1_entry(sentence, origin)
    origin = find_origin(sentence, keys, c2_lessons)
    if origin is None:
        return None
    record = _c2_record(ROOT, origin.lesson_id, sentence.id)
    if record is None:
        return None
    if record.inherited:
        source = c1_by_id.get(record.detail)
        c1_origin = find_origin(sentence, keys, [source]) if source else None
        return _c1_entry(sentence, c1_origin) if c1_origin else None
    if record.detail != "PASS":
        return None
    return (
        f"- `{sentence.id}` · {INHERITED_C2}: {record.report} · C2 {origin.lesson_id} l.{origin.first_line}"
    )


def _c1_entry(sentence: Sentence, origin: object) -> str | None:
    c1_file = ROOT / "content/age-administrativo-c1/es/lessons" / f"{origin.lesson_id}.md"  # type: ignore[attr-defined]
    try:
        report, sha = c1_report(
            ROOT, c1_file, Sentence(sentence.text, origin.first_line, origin.last_line, 0, "")
        )  # type: ignore[attr-defined]
    except LookupError:
        return None
    return f"- `{sentence.id}` · {INHERITED}: {report} · C1 {origin.lesson_id} l.{origin.first_line} · {sha}"  # type: ignore[attr-defined]


def apply(lesson_id: str, report: Path) -> None:
    """Replace each FAIL sentence by the report's replacement; «drop»/«delete» removes it (a list item whole)."""
    lesson = ROOT / "content/aeat-agentes-hacienda/es/lessons" / f"{lesson_id}.md"

    def cells(row: str) -> list[str]:
        return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", row.strip().strip("|"))]

    pending = TAX / lesson_id / "pending.md"
    texts = {
        cells(r)[0].strip("`"): cells(r)[2] for r in pending.read_text().splitlines() if r.startswith("| `")
    }
    text = lesson.read_text()
    for row in report.read_text().splitlines():
        if not row.startswith("| `"):
            continue
        c = cells(row)
        if c[1] != "FAIL":
            continue
        sid = c[0].strip("`")
        if sid not in texts:
            print(f"{sid}: not in pending.md, not applied")
            continue
        old, new = texts[sid], c[-1].removeprefix("- ")
        if re.search(r"\badd (after|before)\b|\breplace (the|with)\b", new, re.I):
            print(f"{sid}: the replacement holds an instruction, not applied")
            continue
        found = list(re.finditer(r"\s+".join(re.escape(t) for t in old.split()), text))
        if len(found) != 1:
            print(f"{sid}: {len(found)} matches, not applied")
            continue
        start, end = found[0].start(), found[0].end()
        if new.strip().lower() == "drop" or new.strip().lower().startswith(("(delete", "delete", "(drop")):
            line_start = text.rfind("\n", 0, start) + 1
            item_end = end
            while text.startswith("\n  ", item_end):
                item_end = text.index("\n", item_end + 1) if "\n" in text[item_end + 1 :] else len(text)
            if text[line_start:start].strip() == "-" and text[end:item_end].strip() == "":
                start, end = line_start, item_end + 1
            else:
                end += 1 if text[end : end + 1] == " " else 0
            new = ""
        text = text[:start] + new + text[end:]
        print(f"{sid}: applied")
    lesson.write_text(text)


if __name__ == "__main__":
    if sys.argv[1] == "apply":
        apply(sys.argv[2], Path(sys.argv[3]))
        raise SystemExit(0)
    raise SystemExit(main(sys.argv[1], sys.argv[2:]))
