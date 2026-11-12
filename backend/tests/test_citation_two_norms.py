# SPDX-License-Identifier: AGPL-3.0-only
"""A citation that names two norms («art. 1 LO 1/1995 y art. 1 LO 2/1995») anchors both, in document order."""

from __future__ import annotations

import os
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest
import yaml

from tradeschool.citations.grammar import parse_segment
from tradeschool.citations.lesson import scan_lesson
from tradeschool.citations.norms import NormIndex

CEUTA = "boe-a-1995-6358"
MELILLA = "boe-a-1995-6359"
_NORMS = [
    {"short": "LO 1/1995", "title": "Ley Orgánica 1/1995, Estatuto de Ceuta.", "boe_id": "BOE-A-1995-6358"},
    {"short": "LO 2/1995", "title": "Ley Orgánica 2/1995, Estatuto de Melilla.", "boe_id": "BOE-A-1995-6359"},
]
_LESSON = (
    "Las ciudades autónomas (art. 1 LO 1/1995 y art. 1 LO 2/1995) y su preámbulo "
    "(preámbulo LO 1/1995 y preámbulo LO 2/1995).\n"
)


def test_a_segment_naming_two_norms_splits_into_two_cited_groups() -> None:
    segment = parse_segment("art. 1 LO 1/1995 y art. 1 LO 2/1995")
    assert segment is not None
    assert [(s.norm_text, [u.slug for u in s.units]) for s in (segment, *segment.also)] == [
        ("LO 1/1995", ["art-1"]),
        ("LO 2/1995", ["art-1"]),
    ]


def test_one_norm_named_once_stays_one_group() -> None:
    segment = parse_segment("art. 44.2 y art. 33.1 LOTC")
    assert segment is not None
    assert segment.also == ()


def _anchors(tmp_path: Path) -> list[tuple[str, ...]]:
    path = tmp_path / "normativa.yaml"
    path.write_text(yaml.safe_dump(_NORMS, allow_unicode=True), encoding="utf-8")
    scanned = scan_lesson("l", _LESSON, NormIndex.load(path, [_LESSON]))
    return [citation.anchors for citation in scanned.prose]


def test_each_norm_of_a_two_norm_citation_gets_its_own_anchor_in_document_order(tmp_path: Path) -> None:
    assert _anchors(tmp_path) == [
        (f"{CEUTA}-art-1", f"{MELILLA}-art-1"),
        (f"{CEUTA}-preambulo", f"{MELILLA}-preambulo"),
    ]


@pytest.mark.parametrize("seed", range(20))
def test_the_anchors_do_not_depend_on_the_hash_seed(tmp_path: Path, seed: int) -> None:
    script = textwrap.dedent(
        f"""
        import sys
        from pathlib import Path
        sys.path.insert(0, {str(Path(__file__).parent)!r})
        import test_citation_two_norms as t
        print(t._anchors(Path({str(tmp_path)!r})))
        """
    )
    run = subprocess.run(
        [sys.executable, "-c", script],
        env={**os.environ, "PYTHONHASHSEED": str(seed)},
        capture_output=True,
        text=True,
        check=True,
    )
    expected = [(f"{CEUTA}-art-1", f"{MELILLA}-art-1"), (f"{CEUTA}-preambulo", f"{MELILLA}-preambulo")]
    assert run.stdout.strip() == str(expected)
