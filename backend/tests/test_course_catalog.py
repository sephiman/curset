# SPDX-License-Identifier: AGPL-3.0-only
"""Loading several courses: each validates on its own terms, and a broken one names itself."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from tradeschool.content.registry import ContentError, load_catalog

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "content"
SPANISH_ONLY = "fixture-oposiciones"


def _root_with(tmp_path: Path, *courses: str) -> Path:
    root = tmp_path / "content"
    root.mkdir()
    for course in courses:
        shutil.copytree(FIXTURES / course, root / course)
    return root


def test_drafts_load_but_only_published_courses_are_offered(tmp_path: Path) -> None:
    catalog = load_catalog(_root_with(tmp_path, SPANISH_ONLY, "fixture-borrador"))
    assert set(catalog.courses) == {SPANISH_ONLY, "fixture-borrador"}
    assert catalog.published_slugs() == {SPANISH_ONLY}


def test_a_test_only_course_has_no_figures_and_one_language(tmp_path: Path) -> None:
    course = load_catalog(_root_with(tmp_path, SPANISH_ONLY)).courses[SPANISH_ONLY]
    assert course.has_figures is False
    assert course.languages == ["es"]
    assert course.course_export_all()["locales"] == ["es"]


def test_a_course_that_does_not_validate_fails_startup_by_name(tmp_path: Path) -> None:
    root = _root_with(tmp_path, SPANISH_ONLY)
    (root / SPANISH_ONLY / "es" / "lessons" / "m01-l1.md").unlink()
    with pytest.raises(ContentError, match=f"course '{SPANISH_ONLY}' does not validate"):
        load_catalog(root)


def test_a_spanish_only_course_has_no_english_tree(tmp_path: Path) -> None:
    root = _root_with(tmp_path, SPANISH_ONLY)
    shutil.copytree(root / SPANISH_ONLY / "es", root / SPANISH_ONLY / "en")
    with pytest.raises(ContentError, match="does not declare 'en'"):
        load_catalog(root)


def test_a_spanish_only_course_carries_no_stray_translation(tmp_path: Path) -> None:
    root = _root_with(tmp_path, SPANISH_ONLY)
    exercise = root / SPANISH_ONLY / "exercises" / "m01-ex-1.yaml"
    exercise.write_text(
        exercise.read_text(encoding="utf-8").replace(
            '      es: "Un mes."', '      es: "Un mes."\n          en: "One month."'
        ),
        encoding="utf-8",
    )
    with pytest.raises(ContentError, match=r"exercise m01-ex-1: .* has \['en', 'es'\]"):
        load_catalog(root)


def test_a_course_without_figures_carries_no_figure_coupling(tmp_path: Path) -> None:
    root = _root_with(tmp_path, SPANISH_ONLY)
    (root / SPANISH_ONLY / "figure-coupling.yaml").write_text("{}\n", encoding="utf-8")
    with pytest.raises(ContentError, match=r"has no figures but carries figure-coupling\.yaml"):
        load_catalog(root)


def test_an_exercise_kind_the_course_does_not_declare_is_rejected(tmp_path: Path) -> None:
    root = _root_with(tmp_path, SPANISH_ONLY)
    manifest = root / SPANISH_ONLY / "course.yaml"
    manifest.write_text(
        manifest.read_text(encoding="utf-8").replace("        type: quiz", "        type: calculation"),
        encoding="utf-8",
    )
    with pytest.raises(ContentError, match="does not declare in exercise_types"):
        load_catalog(root)


def test_a_course_directory_is_named_after_its_slug(tmp_path: Path) -> None:
    root = _root_with(tmp_path, SPANISH_ONLY)
    (root / SPANISH_ONLY).rename(root / "renamed")
    with pytest.raises(ContentError, match="must match its directory"):
        load_catalog(root)
