# SPDX-License-Identifier: AGPL-3.0-only
"""Provenance of age-auxiliar-c2 lesson sentences (R2.3): inherited from C1 when identical, else verified."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_BACKEND = Path(__file__).resolve().parents[1]
if str(_BACKEND) not in sys.path:
    sys.path.insert(0, str(_BACKEND))

from scripts.provenance import (  # noqa: E402
    BLOQUE_DIRS,
    GlossaryEntry,
    LessonText,
    Record,
    audit_glossary,
    audit_lesson,
    c1_report,
    parse_glossary_record,
    parse_record,
    sentence_id,
    sentences,
)
from tests.pipeline_courses import REPO_CONTENT, course_dir, pipeline_courses  # noqa: E402

from tradeschool.citations.lesson import scan_lesson  # noqa: E402
from tradeschool.citations.norms import NormIndex  # noqa: E402
from tradeschool.content.registry import CourseRegistry  # noqa: E402
from tradeschool.content.yaml_file import read_yaml  # noqa: E402

REPO = REPO_CONTENT.parent
C2_RECORDS = REPO / "docs" / "age-verification" / "c2"
RECORDS = C2_RECORDS / "bloque-i"
REPORT = "docs/report.md"


def _course(root: Path, ce_bytes: bytes) -> NormIndex:
    (root / "sources" / "normativa").mkdir(parents=True, exist_ok=True)
    (root / "sources" / "normativa" / "ce.pdf").write_bytes(ce_bytes)
    (root / "sources" / "normativa.yaml").write_text(
        "- short: CE\n  title: Constitución Española.\n  file: sources/normativa/ce.pdf\n"
    )
    return NormIndex.load(root / "sources" / "normativa.yaml", [])


def _lesson(root: Path, index: NormIndex, lesson_id: str, markdown: str) -> LessonText:
    return LessonText(lesson_id, markdown, scan_lesson(lesson_id, markdown, index), root)


def _entry(text: str, kind: str, rest: str) -> str:
    return f"- `{sentence_id(text)}` · {kind}: {rest}\n  > {text}\n"


SOURCE = """# Corona

El Rey es el Jefe del Estado. Arbitra y modera el funcionamiento regular de las instituciones
(art. 56.1 CE).

Corresponde al Rey (art. 62 CE):

- sancionar y promulgar las leyes;
- convocar a referéndum.
"""


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    (tmp_path / "docs").mkdir()
    (tmp_path / REPORT).write_text("| id | verdict |\n|---|---|\n")
    return tmp_path


def _setup(repo: Path, target_md: str, *, same_file: bool = True) -> tuple[LessonText, LessonText]:
    c1 = _course(repo / "c1", b"ce text")
    c2 = _course(repo / "c2", b"ce text" if same_file else b"ce text, newer")
    return _lesson(repo / "c2", c2, "m01-l02", target_md), _lesson(repo / "c1", c1, "m01-l02", SOURCE)


def _inherit_all(lesson: LessonText) -> list[Record]:
    return parse_record(
        "".join(
            _entry(s.text, "verificado en C1", f"{REPORT} · C1 m01-l02") for s in sentences(lesson.markdown)
        )
    )


def test_a_paragraph_splits_into_sentences_and_a_list_into_items() -> None:
    texts = [s.text for s in sentences(SOURCE)]
    assert texts == [
        "El Rey es el Jefe del Estado.",
        "Arbitra y modera el funcionamiento regular de las instituciones (art. 56.1 CE).",
        "Corresponde al Rey (art. 62 CE):",
        "sancionar y promulgar las leyes;",
        "convocar a referéndum.",
    ]


def test_an_article_abbreviation_does_not_end_a_sentence() -> None:
    texts = [s.text for s in sentences("Lo dicen los arts. Primero y segundo de la ley. Fin.\n")]
    assert texts == ["Lo dicen los arts. Primero y segundo de la ley.", "Fin."]


def test_identical_sentences_with_the_same_cited_file_inherit(repo: Path) -> None:
    target, source = _setup(repo, SOURCE)
    audit = audit_lesson(target, _inherit_all(target), lambda _: source, repo)
    assert audit.problems == []
    assert audit.inherited == 5


def test_a_cited_file_with_another_sha256_breaks_inheritance(repo: Path) -> None:
    target, source = _setup(repo, SOURCE, same_file=False)
    audit = audit_lesson(target, _inherit_all(target), lambda _: source, repo)
    assert len(audit.problems) == 5
    assert "no identical counterpart" in audit.problems[0]


def test_a_sentence_whose_governing_citation_was_cut_does_not_inherit(repo: Path) -> None:
    # The first sentence is kept verbatim, but the sentence that carried its citation is gone.
    target, source = _setup(repo, "# Corona\n\nEl Rey es el Jefe del Estado. Lo dice el texto (art. 1 CE).\n")
    record = parse_record(
        _entry("El Rey es el Jefe del Estado.", "verificado en C1", f"{REPORT} · C1 m01-l02")
    )
    audit = audit_lesson(target, record, lambda _: source, repo)
    assert any("no identical counterpart" in p for p in audit.problems)


def test_a_changed_sentence_needs_a_pass_in_its_report(repo: Path) -> None:
    changed = "El Rey es el Jefe del Estado (art. 56.1 CE)."
    target, source = _setup(repo, f"# Corona\n\n{changed}\n")
    record = parse_record(_entry(changed, "verificado", f"PASS · {REPORT}"))
    assert audit_lesson(target, record, lambda _: source, repo).problems == [
        f"m01-l02: {sentence_id(changed)} has no PASS in {REPORT}"
    ]
    (repo / REPORT).write_text(f"| `{sentence_id(changed)}` | PASS | ok |\n")
    assert audit_lesson(target, record, lambda _: source, repo).verified == 1


def test_a_sentence_without_a_record_and_a_record_without_a_sentence_both_fail(repo: Path) -> None:
    target, source = _setup(repo, "# Corona\n\nUna frase (art. 1 CE).\n")
    record = parse_record(_entry("Otra frase.", "verificado", f"PASS · {REPORT}"))
    problems = audit_lesson(target, record, lambda _: source, repo).problems
    assert any("is not a sentence of the lesson" in p for p in problems)
    assert any("has no record" in p for p in problems)


def test_a_record_naming_a_missing_report_fails(repo: Path) -> None:
    target, source = _setup(repo, SOURCE)
    records = parse_record(
        "".join(_entry(s.text, "verificado en C1", "docs/nope.md · C1 m01-l02") for s in sentences(SOURCE))
    )
    assert all("missing report" in p for p in audit_lesson(target, records, lambda _: source, repo).problems)


# --------------------------------------------------------------------------------- the course itself


def _written_lessons() -> list[str]:
    course = next(c for c in pipeline_courses() if c.slug == "age-auxiliar-c2")
    lessons = course_dir(course) / "es" / "lessons"
    return sorted(
        path.stem for path in lessons.glob("m0[12]-l*.md") if "Tema sin redactar." not in path.read_text()
    )


@pytest.mark.parametrize("lesson_id", _written_lessons())
def test_every_sentence_of_a_written_c2_lesson_is_inherited_or_verified(lesson_id: str) -> None:
    courses = {c.slug: c for c in pipeline_courses()}
    c2, c1 = courses["age-auxiliar-c2"], courses["age-administrativo-c1"]

    def text_of(course: CourseRegistry, lid: str) -> LessonText | None:
        root = course_dir(course)
        path = root / "es" / "lessons" / f"{lid}.md"
        citations = course.citations.lesson(lid, "es")
        if not path.exists() or citations is None:
            return None
        return LessonText(lid, path.read_text(), citations, root)

    record_path = C2_RECORDS / BLOQUE_DIRS[lesson_id[:3]] / f"{lesson_id}.md"
    assert record_path.exists(), f"{lesson_id} is written but has no provenance record"
    lesson = text_of(c2, lesson_id)
    assert lesson is not None
    c1_lessons: dict[str, LessonText | None] = {}

    def c1_lesson(lid: str) -> LessonText | None:
        if lid not in c1_lessons:
            c1_lessons[lid] = text_of(c1, lid)
        return c1_lessons[lid]

    audit = audit_lesson(lesson, parse_record(record_path.read_text()), c1_lesson, REPO)
    assert audit.problems == []


# ------------------------------------------------------------------------------------------- glossary


def _term(definition: str, term: str = "refrendo") -> dict[str, object]:
    return {"id": "g-refrendo", "es": term, "origin": "m01-l02", "definition": {"es": definition}}


def _glossary_audit(
    repo: Path, c2_entry: dict[str, object], *, same_file: bool = True, record: str = ""
) -> list[str]:
    c1 = _course(repo / "c1", b"ce text")
    c2 = _course(repo / "c2", b"ce text" if same_file else b"ce text, newer")
    c1_entry = _term("Firma que valida los actos del Rey (art. 64.1 CE).")
    record = record or f"- `g-refrendo` · verificado en C1: {REPORT} · C1 m01-l02\n"
    audit = audit_glossary(
        [GlossaryEntry.of(c2_entry, c2, repo / "c2")],
        {"g-refrendo": GlossaryEntry.of(c1_entry, c1, repo / "c1")},
        parse_glossary_record(record),
        repo,
    )
    return audit.problems


def test_a_glossary_entry_copied_verbatim_with_the_same_cited_file_inherits(repo: Path) -> None:
    assert _glossary_audit(repo, _term("Firma que valida los actos del Rey (art. 64.1 CE).")) == []


def test_a_glossary_entry_with_another_definition_or_file_needs_its_own_pass(repo: Path) -> None:
    changed = _term("Firma que valida los actos del Rey (art. 64 CE).")
    assert any("differs from C1" in p for p in _glossary_audit(repo, changed))
    same_text = _term("Firma que valida los actos del Rey (art. 64.1 CE).")
    assert any("differs from C1" in p for p in _glossary_audit(repo, same_text, same_file=False))


def test_a_verified_glossary_entry_needs_a_pass_row(repo: Path) -> None:
    entry = _term("Otra definición (art. 64.1 CE).")
    record = f"- `g-refrendo` · verificado: PASS · {REPORT}\n"
    assert any("no PASS" in p for p in _glossary_audit(repo, entry, record=record))
    (repo / REPORT).write_text("| `g-refrendo` | PASS | ok |\n")
    assert _glossary_audit(repo, entry, record=record) == []


def test_every_c2_glossary_entry_is_inherited_or_verified() -> None:
    courses = {c.slug: c for c in pipeline_courses()}
    c2, c1 = courses["age-auxiliar-c2"], courses["age-administrativo-c1"]

    def entries(course: CourseRegistry) -> list[GlossaryEntry]:
        root = course_dir(course)
        raw = read_yaml(root / "glossary.yaml")
        terms = raw.get("terms") if isinstance(raw, dict) else None
        norms = course.citations.norms
        assert norms is not None
        return [GlossaryEntry.of(term, norms, root) for term in terms or []]

    c2_entries = entries(c2)
    if not c2_entries:
        pytest.skip("age-auxiliar-c2 has no glossary entries yet")
    record = RECORDS / "glossary.md"
    assert record.exists(), "age-auxiliar-c2 has glossary entries but no glossary provenance record"
    c1_entries = {entry.id: entry for entry in entries(c1)}
    audit = audit_glossary(c2_entries, c1_entries, parse_glossary_record(record.read_text()), REPO)
    assert audit.problems == []


def test_a_c1_sentence_only_reflowed_by_a_c2_commit_keeps_the_report_from_before_it() -> None:
    c1_lesson = REPO_CONTENT / "age-administrativo-c1" / "es" / "lessons" / "m01-l11.md"
    text = (
        "Los dos tratados tienen el mismo valor jurídico, y la Unión sustituye y sucede a la"
        " Comunidad Europea (art. 1 TUE)."
    )
    found = next(s for s in sentences(c1_lesson.read_text()) if s.text == text)
    report, _ = c1_report(REPO_CONTENT.parent, c1_lesson, found)
    assert report == "docs/age-theory-ledger.md"
