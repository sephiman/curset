# SPDX-License-Identifier: AGPL-3.0-only
"""Each course's glyph and accent (docs/identity.md): the file exists, is clean, and the accent reads."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import pytest
from httpx import AsyncClient

from tradeschool.content.registry import ContentError, load_catalog, load_registry
from tradeschool.content.schema import CourseStatus, ManifestCourse

REPO = Path(__file__).resolve().parents[2]
IDENTITY = json.loads((REPO / "frontend/src/assets/identity/identity.json").read_text(encoding="utf-8"))
COURSES = sorted(path.parent for path in (REPO / "content").glob("*/course.yaml"))
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "content"
TEXT_CONTRAST = 4.5


def _luminance(hex_colour: str) -> float:
    """WCAG 2.x relative luminance."""

    def channel(value: int) -> float:
        c = value / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (int(hex_colour[i : i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def _contrast(a: str, b: str) -> float:
    high, low = sorted((_luminance(a), _luminance(b)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def _identity_of(course_dir: Path) -> ManifestCourse:
    course = load_registry(course_dir).manifest.course
    if course.status is CourseStatus.DRAFT and course.glyph is None and course.color is None:
        pytest.skip("a draft gets its glyph and accent in its own identity round")
    return course


@pytest.mark.parametrize("course_dir", COURSES, ids=lambda path: path.name)
def test_every_published_course_declares_a_glyph_that_exists_and_is_a_clean_svg(course_dir: Path) -> None:
    course = _identity_of(course_dir)
    assert course.glyph is not None and course.color is not None
    path = course_dir / "identity" / f"{course.glyph}.svg"
    source = path.read_text(encoding="utf-8")
    # The platform mark's box: the dropdown and settings read as one family.
    assert re.search(r'<svg[^>]*\sviewBox="0 0 24 24"', source)
    assert not re.search(r"<script|\son\w+=", source, re.IGNORECASE)
    assert not re.search(r'(?:href|src)="(?!#)', source)
    # Only currentColor: the accent comes from the course's colour, never from the file.
    assert not re.search(r"#[0-9a-fA-F]{3,6}\b|rgb\(", source)
    assert path.stat().st_size < 20 * 1024


@pytest.mark.parametrize("course_dir", COURSES, ids=lambda path: path.name)
def test_each_accent_shade_passes_text_contrast_on_the_background_it_is_drawn_on(course_dir: Path) -> None:
    color = _identity_of(course_dir).color
    assert color is not None
    assert _contrast(color.light, IDENTITY["colors"]["paper"]) >= TEXT_CONTRAST
    assert _contrast(color.dark, IDENTITY["colors"]["ink"]) >= TEXT_CONTRAST
    assert _contrast(color.dark, IDENTITY["colors"]["black"]) >= TEXT_CONTRAST


@pytest.mark.parametrize("shade", ["light", "dark"])
def test_no_course_accent_is_much_lighter_than_another(shade: str) -> None:
    colors = [load_registry(course_dir).manifest.course.color for course_dir in COURSES]
    luminances = [_luminance(getattr(color, shade)) for color in colors if color is not None]
    assert max(luminances) / min(luminances) < 1.15


def test_a_declared_glyph_without_its_file_fails_the_course(tmp_path: Path) -> None:
    root = tmp_path / "content"
    shutil.copytree(FIXTURES / "fixture-oposiciones", root / "fixture-oposiciones")
    manifest = root / "fixture-oposiciones" / "course.yaml"
    text = manifest.read_text(encoding="utf-8")
    declared = text.replace("  status: published", "  status: published\n  glyph: missing")
    manifest.write_text(declared, encoding="utf-8")
    with pytest.raises(ContentError, match="course glyph 'missing' not found"):
        load_catalog(root)


async def test_the_catalogue_carries_glyph_and_accent_and_serves_the_glyph_without_an_account(
    multi_client: AsyncClient,
) -> None:
    catalogue = {course["slug"]: course for course in (await multi_client.get("/api/courses?lang=es")).json()}
    assert catalogue["crypto-futures"]["glyph"] == "candlestick"
    assert catalogue["crypto-futures"]["color"] == {"light": "#0f6b68", "dark": "#19afaa"}
    assert catalogue["fixture-oposiciones"]["glyph"] is None

    glyph = await multi_client.get("/api/courses/crypto-futures/glyph.svg")
    assert glyph.status_code == 200
    assert glyph.headers["content-type"] == "image/svg+xml"
    served = REPO / "content/crypto-futures/identity/candlestick.svg"
    assert glyph.text == served.read_text(encoding="utf-8")


async def test_a_course_without_a_glyph_answers_404(multi_client: AsyncClient) -> None:
    assert (await multi_client.get("/api/courses/fixture-oposiciones/glyph.svg")).status_code == 404
