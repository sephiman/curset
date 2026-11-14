# SPDX-License-Identifier: AGPL-3.0-only
"""The audit scripts of a technical course (requirements 8.3): scope, coverage, quota, citations, extracts."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from scripts import tech_sources
from scripts.tech_course import (
    anchor_text,
    check_citations,
    check_coverage,
    check_extracts,
    check_scope,
    lesson_quota,
    lessons,
    programme,
)
from scripts.tech_course.lessons import Lesson
from scripts.tech_course.questions import Question

from tradeschool.citations.tech import TechSourceIndex

PAGE = (
    "<html><body><h2 id='A'>Alpha</h2><p>The lock is  taken\nbefore the write.</p>"
    "<h2 id='B'>Beta</h2><p>Other.</p></body></html>"
)

LESSON = """# Title

## Locks
<!-- bullets: 6.2.a 6.2.b -->

A row lock blocks writers (`src#A`; `src#B`). Plain sentence.

```java snippet=m06-l02/Lock.java
class Lock {}
```

:::esquema{kind=tabla title="Locks"}
| Lock | Source |
|---|---|
| row | `src#A` |
| table | `src#B` |
:::

:::judgement{source="Someone, Book" ref="src#B"}
According to Someone, prefer rows.
:::

## Key points

- Restates (`src#A`).
"""


def _course(root: Path, lesson_files: dict[str, str], stored: str = PAGE, storage: str = "repo") -> Path:
    course = root / "content" / "tc"
    (course / "en" / "lessons").mkdir(parents=True)
    for name, body in lesson_files.items():
        (course / "en" / "lessons" / f"{name}.md").write_text(body, encoding="utf-8")
    (course / "sources" / "docs").mkdir(parents=True)
    page = course / "sources" / "docs" / "src.html"
    page.write_text(PAGE, encoding="utf-8")
    (course / "sources" / "sources.yaml").write_text(
        "sources:\n- id: src\n  tier: A\n  title: S\n  url: https://x.test\n  licence: MIT\n"
        f"  extract_allowed: true\n  storage: {storage}\n  path: sources/docs/src.html\n",
        encoding="utf-8",
    )
    tech_sources.write_anchors(course / "sources", "src", page)
    page.write_text(stored, encoding="utf-8")
    (course / "programme.md").write_text(
        "  - `6.2.a` [F] one\n  - `6.2.b` [F] two\n  - `6.2.c` [F] three\n  - `6.3.a` [F] four\n",
        encoding="utf-8",
    )
    return course


@pytest.fixture
def at_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(lessons, "REPO", tmp_path)
    return tmp_path


# --- reading a lesson ----------------------------------------------------------------------------------


def test_a_lesson_reports_sections_bullets_citations_snippets_and_fact_sentences() -> None:
    lesson = Lesson("m06-l02", LESSON)
    assert [(s.title, s.bullets, s.audited) for s in lesson.sections()] == [
        ("Locks", ("6.2.a", "6.2.b"), True),
        ("Key points", (), False),
    ]
    assert [str(c.ref) for c in lesson.prose_citations()] == ["src#A", "src#B", "src#A"]
    assert [str(c.ref) for c in lesson.esquema_citations()] == ["src#A", "src#B"]
    assert [str(c.ref) for c in lesson.judgement_citations()] == ["src#B"]
    assert [(b.path, b.body) for b in lesson.snippet_blocks()] == [("m06-l02/Lock.java", "class Lock {}")]
    assert lesson.fact_sentences() == 1 + 2
    assert lesson.snippet_count() == 1
    assert not lesson.pending
    assert Lesson("m06-l03", "# T\n\n:::note\nLesson not written yet.\n:::\n").pending


def test_a_parenthetical_that_looks_like_a_citation_but_does_not_parse_is_reported() -> None:
    lesson = Lesson("m01-l01", "## S\n\nA claim (`SRC#A`) and another (`src#`) and fine (`src#A`).\n")
    assert [text for _, text in lesson.malformed_citations()] == ["`SRC#A`", "`src#`"]


def test_a_malformed_prose_citation_fails_the_citation_audit(at_root: Path) -> None:
    _course(at_root, {"m06-l02": "## S\n\nClaim (`SRC#A`).\n"})
    (problem,) = check_citations.audit("tc").problems
    assert "lesson m06-l02 line 3" in problem and "is not source_id#anchor" in problem


def test_a_parenthetical_that_is_not_only_citations_is_not_one() -> None:
    lesson = Lesson("m01-l01", "## S\n\nCall it (`foo()`; `bar#baz`) and (see `src#A` above).\n")
    assert lesson.prose_citations() == []


# --- scope, coverage, quota ----------------------------------------------------------------------------


def test_scope_flags_a_section_without_bullets_a_foreign_bullet_and_an_unknown_one() -> None:
    body = "## One\n<!-- bullets: 6.3.a 9.9.z -->\n\ntext\n\n## Two\n\ntext\n"
    problems = check_scope.scope_problems([Lesson("m06-l02", body)], {"6.3.a", "6.2.a"})
    assert problems == [
        "lesson m06-l02 line 1 «One»: 6.3.a belongs to m06-l03",
        "lesson m06-l02 line 1 «One»: 9.9.z is not in the programme",
        "lesson m06-l02 line 6 «Two»: declares no bullet",
    ]


def test_scope_skips_pending_lessons_and_the_exempt_first_lesson() -> None:
    pending = Lesson("m06-l02", ":::note\nLesson not written yet.\n:::\n")
    intro = Lesson("m00-l01", "## Who\n\ntext\n")
    assert check_scope.scope_problems([pending, intro], set()) == []


def test_coverage_separates_covered_dropped_pending_and_uncovered() -> None:
    written = Lesson("m06-l02", "## S\n<!-- bullets: 6.2.a -->\n\ntext\n")
    pending = Lesson("m06-l03", ":::note\nLesson not written yet.\n:::\n")
    found = check_coverage.coverage(
        [written, pending], ["6.2.a", "6.2.b", "6.2.c", "6.3.a"], dropped={"6.2.c"}
    )
    assert (found.covered, found.uncovered, found.dropped, found.pending) == (
        ["6.2.a"],
        ["6.2.b"],
        ["6.2.c"],
        ["6.3.a"],
    )


@pytest.mark.parametrize(
    ("facts", "snippets", "expected"), [(0, 0, 10), (7, 2, 10), (12, 3, 15), (40, 5, 30)]
)
def test_the_quota_is_clamped_between_ten_and_thirty(facts: int, snippets: int, expected: int) -> None:
    assert lesson_quota.quota(facts, snippets) == expected


def test_the_quota_row_of_a_pending_lesson_says_pending() -> None:
    row = lesson_quota.quota_row(Lesson("m06-l03", "Lesson not written yet."), 0)
    assert row == ["m06-l03", "pending", "-", "-", "-", "0"]


def test_programme_ids_map_to_their_lesson() -> None:
    assert programme.lesson_of("6.2.a") == "m06-l02"


# --- citations audit -----------------------------------------------------------------------------------


def test_a_course_whose_citations_all_resolve_and_hash_as_recorded_passes(at_root: Path) -> None:
    _course(at_root, {"m06-l02": LESSON})
    result = check_citations.audit("tc")
    assert result.problems == []
    assert sorted(str(ref) for ref in result.cited) == ["src#A", "src#B"]


def test_a_stored_page_that_changed_since_its_anchors_were_recorded_fails_the_version_audit(
    at_root: Path,
) -> None:
    _course(at_root, {"m06-l02": LESSON}, stored=PAGE.replace("before the write", "after the write"))
    (problem,) = check_citations.audit("tc").problems
    assert problem.startswith("lesson m06-l02 line ") and "src#A" in problem and "stored text" in problem


def test_an_unknown_anchor_in_a_lesson_or_question_fails(at_root: Path) -> None:
    course = _course(at_root, {"m06-l02": "## S\n\nClaim (`src#NOPE`).\n"})
    (course / "exercises").mkdir()
    (course / "exercises" / "m06-l02-ex-1.yaml").write_text(
        "type: quiz\nvariants:\n- id: q1\n  citation: 'src#A; src#GONE'\n- id: q2\n  citation: 'bad'\n",
        encoding="utf-8",
    )
    problems = check_citations.audit("tc").problems
    assert any("lesson m06-l02 line 3" in p and "no anchor «NOPE»" in p for p in problems)
    assert any("question m06-l02-ex-1/q1" in p and "GONE" in p for p in problems)
    assert any("question m06-l02-ex-1/q2" in p and "is not source_id#anchor" in p for p in problems)


def test_a_local_source_with_no_local_folder_is_skipped_with_one_warning_and_never_fails(
    at_root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _course(at_root, {"m06-l02": LESSON}, storage="local")
    monkeypatch.setenv("CURSET_SOURCES_LOCAL", str(at_root / "absent"))
    result = check_citations.audit("tc")
    assert result.problems == [] and result.skipped == 2
    assert capsys.readouterr().err.count("warning") == 1


# --- extracts ------------------------------------------------------------------------------------------


def _extract_problems(at_root: Path, extract: str, storage: str = "repo", allowed: bool = True) -> list[str]:
    course = _course(at_root, {}, storage="repo")
    index = TechSourceIndex.load(course)
    assert index is not None
    if not allowed:
        index = TechSourceIndex(
            index.course_dir,
            {k: type(v)(**{**v.__dict__, "extract_allowed": False}) for k, v in index.sources.items()},
            index.anchors,
        )
    question = Question("ex/q1", "m06-l02", "src#A", extract, None)
    return check_extracts.extract_problems([question], index, anchor_text.AnchorStore(index, "tc"))


def test_an_extract_that_is_a_literal_substring_of_its_anchor_passes_whatever_the_whitespace(
    at_root: Path,
) -> None:
    assert _extract_problems(at_root, "The lock is taken before the write.") == []


def test_an_extract_that_is_not_in_the_anchor_fails(at_root: Path) -> None:
    (problem,) = _extract_problems(at_root, "The lock is released after the write.")
    assert "not a literal substring of src#A" in problem


def _two_source_index(course: Path) -> TechSourceIndex:
    index = TechSourceIndex.load(course)
    assert index is not None
    other = type(index.sources["src"])(**{**index.sources["src"].__dict__, "id": "loc", "storage": "local"})
    return TechSourceIndex(
        index.course_dir, {**index.sources, "loc": other}, {**index.anchors, "loc": ("A",)}
    )


def test_an_extract_copied_from_a_later_citation_fails_because_the_panel_credits_the_first(
    at_root: Path,
) -> None:
    index = _two_source_index(_course(at_root, {}))
    question = Question("ex/q1", "m06-l02", "src#B; src#A", "The lock is taken before the write.", None)
    (problem,) = check_extracts.extract_problems([question], index, anchor_text.AnchorStore(index, "tc"))
    assert "not a literal substring of src#B" in problem


def test_a_question_whose_local_copy_is_missing_does_not_stop_the_checks_of_the_others(
    at_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    index = _two_source_index(_course(at_root, {}))
    monkeypatch.setenv("CURSET_SOURCES_LOCAL", str(at_root / "absent"))
    questions = [
        Question("ex/q1", "m06-l02", "loc#A", "anything", None),
        Question("ex/q2", "m06-l02", "src#A", "The lock is released after the write.", None),
    ]
    (problem,) = check_extracts.extract_problems(questions, index, anchor_text.AnchorStore(index, "tc"))
    assert problem.startswith("question ex/q2")


def test_an_extract_of_a_source_that_forbids_extracts_fails(at_root: Path) -> None:
    (problem,) = _extract_problems(at_root, "The lock is taken", allowed=False)
    assert "does not allow extracts" in problem


def test_the_real_course_audits_pass() -> None:
    assert check_citations.main(["--course", "backend-in-depth"]) == 0
    assert check_scope.main(["--course", "backend-in-depth"]) == 0
    assert check_coverage.main(["--course", "backend-in-depth"]) == 0
    assert check_extracts.main(["--course", "backend-in-depth"]) == 0


def test_the_anchor_hashes_recorded_for_the_courses_own_requirements_still_hold() -> None:
    entries = json.loads(
        (Path(lessons.REPO) / "content/backend-in-depth/sources/anchors/course-requirements.json").read_text()
    )
    assert any(a["anchor"] == "4-content-classes" for a in entries["anchors"])
