# SPDX-License-Identifier: AGPL-3.0-only
"""refresh_stub_sources and source_guard over a small course on disk."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from scripts.tech_course import bullet_sources, lessons, refresh_stub_sources, source_guard

STUB = "# Title\n\n:::note{type=info}\nLesson not written yet.\n:::\n\n## Sources\n\n- `1.1.a` (J): old\n"
HEADER = "bullet\tclass\ttier_a\ttier_bc\trule\tpinned\tnote\n"


def row(bullet: str, kind: str, tier_a: str = "", tier_bc: str = "", rule: str = "", note: str = "") -> str:
    return f"{bullet}\t{kind}\t{tier_a}\t{tier_bc}\t{rule}\t\t{note}\n"


@pytest.fixture
def world(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, Path]:
    course = tmp_path / "content" / "backend-in-depth"
    (course / "en" / "lessons").mkdir(parents=True)
    (course / "sources" / "anchors").mkdir(parents=True)
    (course / "sources" / "sources.yaml").write_text(
        "sources:\n- id: jls\n  tier: A\n  url: https://example.org/jls\n- id: fowler\n  tier: C\n  url: https://example.org/f\n"
    )
    (course / "sources" / "anchors" / "jls.json").write_text(
        json.dumps({"source": "jls", "anchors": [{"anchor": "ok"}]})
    )
    s0 = tmp_path / "s0"
    (s0 / "coverage").mkdir(parents=True)
    (s0 / "tier-b.yaml").write_text("- key: book\n")
    (s0 / "default-rules.tsv").write_text("bullet\trule\treason\n1.1.c\tR2\tNo source states it.\n")
    (s0 / "coverage" / "gaps.tsv").write_text("bullet\ttier_bc\tnote\n1.1.b\thttps://example.org/f\tn\n")
    (s0 / "coverage" / "m01.final.tsv").write_text(
        HEADER
        + row("1.1.a", "F", "jls#ok; jls#missing", "book; https://example.org/loose")
        + row("1.1.b", "J", tier_bc="candidate: https://example.org/x")
        + row("1.1.c", "J", rule="R2", note="note")
    )
    monkeypatch.setattr(lessons, "REPO", tmp_path)
    return course / "en" / "lessons", s0


def test_stub_sources_follow_the_report_and_mark_unstored_entries(world: tuple[Path, Path]) -> None:
    folder, s0 = world
    (folder / "m01-l01.md").write_text(STUB)
    refresh_stub_sources.main([], s0)
    assert (folder / "m01-l01.md").read_text().split("## Sources\n\n")[1] == (
        "- `1.1.a` (F): `jls#ok`, `candidate: jls#missing`, `book`, `candidate: https://example.org/loose`\n"
        "- `1.1.b` (J): `candidate: https://example.org/x`, `fowler`\n"
        "- `1.1.c` (dropped): No source states it.\n"
    )


def test_refresh_is_idempotent_and_check_passes_afterwards(world: tuple[Path, Path]) -> None:
    folder, s0 = world
    (folder / "m01-l01.md").write_text(STUB)
    assert refresh_stub_sources.main(["--check"], s0) == 1
    assert (folder / "m01-l01.md").read_text() == STUB
    refresh_stub_sources.main([], s0)
    once = (folder / "m01-l01.md").read_text()
    refresh_stub_sources.main([], s0)
    assert (folder / "m01-l01.md").read_text() == once
    assert refresh_stub_sources.main(["--check"], s0) == 0


def test_written_lessons_are_left_untouched(world: tuple[Path, Path]) -> None:
    folder, s0 = world
    written = "# T\n\n## Sources\n\n- `1.1.a` (J): hand written\n"
    (folder / "m01-l01.md").write_text(written)
    refresh_stub_sources.main([], s0)
    assert (folder / "m01-l01.md").read_text() == written


def test_sources_block_keeps_the_sections_after_it(world: tuple[Path, Path]) -> None:
    folder, s0 = world
    (folder / "m01-l01.md").write_text(STUB + "\n## Extra\n\ntext\n")
    refresh_stub_sources.main([], s0)
    assert (folder / "m01-l01.md").read_text().endswith("\n\n## Extra\n\ntext\n")


def write_programme(course: Path, bullets: list[str]) -> None:
    (course / "programme.md").write_text("\n".join(f"- `{bullet}` text" for bullet in bullets) + "\n")


def guard(world: tuple[Path, Path], capsys: pytest.CaptureFixture[str]) -> list[str]:
    source_guard.main([], world[1])
    return capsys.readouterr().out.splitlines()


@pytest.mark.parametrize(("bullets", "expected"), [(5, "write"), (4, "fetch")])
def test_lesson_needs_a_fetch_when_unsourced_exceed_a_fifth(
    world: tuple[Path, Path], capsys: pytest.CaptureFixture[str], bullets: int, expected: str
) -> None:
    folder, s0 = world
    (folder / "m01-l01.md").write_text(STUB)
    ids = ["1.1.a", "1.1.b", "1.1.c", "1.1.d", "1.1.e"][:bullets]
    write_programme(folder.parent.parent, ids)
    (s0 / "coverage" / "m01.final.tsv").write_text(
        HEADER + "".join(row(bullet, "F", "jls#ok") for bullet in ids[:-1]) + row(ids[-1], "J")
    )
    (s0 / "coverage" / "gaps.tsv").write_text("bullet\ttier_bc\tnote\n")
    line = guard(world, capsys)[0].split("\t")
    assert line[:5] == ["m01-l01", str(bullets), "1", f"{100 // bullets}", expected]
    assert line[5] == ids[-1]


def test_guard_ignores_dropped_bullets_and_skips_only_when_nothing_is_sourced(
    world: tuple[Path, Path], capsys: pytest.CaptureFixture[str]
) -> None:
    folder, s0 = world
    (folder / "m01-l01.md").write_text(STUB)
    write_programme(folder.parent.parent, ["1.1.a", "1.1.b", "1.1.c"])
    (s0 / "coverage" / "m01.final.tsv").write_text(
        HEADER + row("1.1.a", "J") + row("1.1.b", "J") + row("1.1.c", "drop")
    )
    (s0 / "coverage" / "gaps.tsv").write_text("bullet\ttier_bc\tnote\n")
    assert guard(world, capsys)[0].split("\t") == ["m01-l01", "2", "2", "100", "skip", "1.1.a 1.1.b"]


def test_dropped_bullets_include_r2_bullets_without_a_stored_source(world: tuple[Path, Path]) -> None:
    assert bullet_sources.dropped_bullets("backend-in-depth", world[1]) == {"1.1.c"}
