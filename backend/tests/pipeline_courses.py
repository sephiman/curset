# SPDX-License-Identifier: AGPL-3.0-only
"""The courses every per-course pipeline step runs over, and what each figure step says about them.

The published courses under `content/`, plus the published test fixtures. The Spanish-only fixture
course has no figures, so it is the proof that a figure step names it ("no figures") rather than
failing on it or reporting an empty result.
"""

from __future__ import annotations

from functools import cache
from pathlib import Path

from tradeschool.content.registry import CourseRegistry, load_catalog

REPO_CONTENT = Path(__file__).resolve().parents[2] / "content"
FIXTURE_CONTENT = Path(__file__).resolve().parent / "fixtures" / "content"
NO_FIGURES = "no figures"


@cache
def pipeline_courses() -> tuple[CourseRegistry, ...]:
    courses = [*load_catalog(REPO_CONTENT).published(), *load_catalog(FIXTURE_CONTENT).published()]
    return tuple(sorted(courses, key=lambda course: course.slug))


def course_dir(course: CourseRegistry) -> Path:
    for root in (REPO_CONTENT, FIXTURE_CONTENT):
        if (root / course.slug / "course.yaml").exists():
            return root / course.slug
    raise LookupError(course.slug)


def figure_step_line(course: CourseRegistry) -> str:
    """One line per course for the figure steps: how many figures it checked, or that it has none."""
    return (
        f"{course.slug}: {len(course.figures)} figures"
        if course.has_figures
        else f"{course.slug}: {NO_FIGURES}"
    )
