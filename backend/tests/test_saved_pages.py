# SPDX-License-Identifier: AGPL-3.0-only
from __future__ import annotations

import hashlib
from pathlib import Path

import pytest
import yaml

from pipeline_courses import course_dir, pipeline_courses
from tradeschool.citations.excerpts import html_blocks
from tradeschool.citations.saved_pages import has_stripped_content, strip_page

PAGE = (
    b"<html><head><title>Ayuda</title><style>p{color:red}</style>"
    b'<script src="https://js.monitor.azure.com/scripts/c/ms.analytics-web-4.min.js"></script></head>'
    b'<body><main data-bi-area="body"><h1 onclick="track()">Atajos</h1><!-- <script> en un comentario -->'
    b'<p data-m=\'{"cN":"x"}\' class="intro">Ctrl+C copia.</p>'
    b'<iframe src="https://www.youtube.com/embed/x">Su navegador no soporta iframes.</iframe>'
    b'<noscript><img src="https://px.ads/1x1.gif"></noscript>'
    b'<a href="/es-es/word" data-linktype="relative-path" ping="https://t.example/p">Word</a></main></body></html>'
)


def test_strips_scripts_styles_frames_and_tracking_attributes_and_keeps_the_rest() -> None:
    assert strip_page(PAGE) == (
        b"<html><head><title>Ayuda</title></head>"
        b"<body><main><h1>Atajos</h1><!-- <script> en un comentario -->"
        b'<p class="intro">Ctrl+C copia.</p>'
        b'<a href="/es-es/word" data-linktype="relative-path">Word</a></main></body></html>'
    )


def test_stripping_keeps_every_visible_paragraph() -> None:
    blocks, title = html_blocks(strip_page(PAGE).decode())
    assert (title, [block.text for block in blocks]) == ("Ayuda", ["Atajos", "Ctrl+C copia.", "Word"])


def test_an_unclosed_script_loses_only_its_start_tag() -> None:
    assert strip_page(b"<p>Antes</p><script src=a.js><p>Despu\xe9s</p>") == b"<p>Antes</p><p>Despu\xe9s</p>"


def test_a_closing_tag_inside_a_script_string_ends_it_as_a_browser_would() -> None:
    assert strip_page(b'<script>var s = "</script>";</script><p>x</p>') == b'";</script><p>x</p>'


def test_stripping_twice_changes_nothing() -> None:
    once = strip_page(PAGE)
    assert strip_page(once) == once


def _saved_pages() -> list[tuple[str, Path, str | None]]:
    found: list[tuple[str, Path, str | None]] = []
    for course in pipeline_courses():
        otros = course_dir(course) / "sources" / "otros"
        fuentes = otros / "fuentes.yaml"
        if not fuentes.exists():
            continue
        entries = yaml.safe_load(fuentes.read_text(encoding="utf-8"))["fuentes"]
        recorded = {e["file"]: e.get("sha256") for e in entries}
        for page in sorted(p for p in otros.rglob("*") if p.suffix.lower() in (".html", ".htm")):
            found.append((course.slug, page, recorded.get(page.relative_to(otros).as_posix())))
    return found


SAVED = _saved_pages()


@pytest.mark.parametrize(("slug", "page", "recorded"), SAVED, ids=[f"{s}/{p.name}" for s, p, _ in SAVED])
def test_every_saved_page_is_stripped_and_its_sha256_recorded(
    slug: str, page: Path, recorded: str | None
) -> None:
    raw = page.read_bytes()
    fix = f"run scripts/strip_saved_pages.py --course {slug} --files {page.name}"
    assert not has_stripped_content(raw), fix
    assert recorded == hashlib.sha256(raw).hexdigest()
