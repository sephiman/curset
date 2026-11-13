# SPDX-License-Identifier: AGPL-3.0-only
"""Esquema rows of a course with `sources/sources.yaml` cite `source_id#anchor`; others keep the norm rule."""

from __future__ import annotations

import json
from pathlib import Path

from tradeschool.citations.course import CourseCitations

TABLE = """# Lesson

:::esquema{{kind=tabla title="Isolation"}}
| Level | Anomaly | Source |
|---|---|---|
| Serializable | none | {cell} |
:::
"""

LIST = """:::esquema{kind=plazos title="Steps"}
1. begin — commit (`pg-iso#XACT-SERIALIZABLE`)
:::
"""


def _course(tmp_path: Path) -> Path:
    sources = tmp_path / "sources"
    (sources / "anchors").mkdir(parents=True)
    (sources / "sources.yaml").write_text(
        "sources:\n- id: pg-iso\n  tier: A\n  title: PostgreSQL isolation\n  url: https://example.org/iso\n"
        "  licence: PostgreSQL\n  extract_allowed: true\n  storage: repo\n  path: sources/docs/pg-iso.html\n",
        encoding="utf-8",
    )
    anchors = {
        "source": "pg-iso",
        "anchors": [{"anchor": "XACT-SERIALIZABLE", "title": "", "level": 3, "sha256": "x"}],
    }
    (sources / "anchors" / "pg-iso.json").write_text(json.dumps(anchors), encoding="utf-8")
    return tmp_path


def _problems(course: Path, body: str) -> list[str]:
    built = CourseCitations.build(course, "tech", {"en": {"m01-l01": body}})
    return built.problems([], "en")


def test_a_row_citing_a_registered_anchor_loads(tmp_path: Path) -> None:
    course = _course(tmp_path)
    assert _problems(course, TABLE.format(cell="`pg-iso#XACT-SERIALIZABLE`")) == []
    assert _problems(course, LIST) == []


def test_a_row_citing_an_unknown_anchor_names_lesson_line_esquema_and_row(tmp_path: Path) -> None:
    (problem,) = _problems(_course(tmp_path), TABLE.format(cell="`pg-iso#NOPE`"))
    assert problem == (
        "lesson m01-l01 line 6, esquema «Isolation», row «Serializable — none»: no anchor «NOPE» in pg-iso"
    )


def test_a_row_citing_an_unknown_source_is_refused(tmp_path: Path) -> None:
    (problem,) = _problems(_course(tmp_path), TABLE.format(cell="`other#XACT-SERIALIZABLE`"))
    assert "unknown source «other»" in problem


def test_a_row_without_a_citation_is_refused(tmp_path: Path) -> None:
    (problem,) = _problems(_course(tmp_path), TABLE.format(cell="art. 1 CE"))
    assert "no citation (source_id#anchor)" in problem


def test_a_course_without_sources_yaml_still_wants_a_norm_and_article(tmp_path: Path) -> None:
    (problem,) = _problems(tmp_path, TABLE.format(cell="`pg-iso#XACT-SERIALIZABLE`"))
    assert "no citation (norm and article)" in problem
