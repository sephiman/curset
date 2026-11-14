# SPDX-License-Identifier: AGPL-3.0-only
"""Every module card of a published course carries a real summary in each of its languages."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

import pytest
import yaml

CONTENT = Path(__file__).resolve().parents[2] / "content"
PLACEHOLDER = "Summary pending."


def _published_manifests() -> list[Path]:
    manifests = sorted(CONTENT.glob("*/course.yaml"))
    return [
        m
        for m in manifests
        if yaml.safe_load(m.read_text(encoding="utf-8"))["course"]["status"] == "published"
    ]


def modules_without_summary(manifest: Mapping[str, object]) -> list[str]:
    blocks = manifest["blocks"]
    assert isinstance(blocks, list)
    missing = []
    for block in blocks:
        for module in block["modules"]:
            summary = module.get("summary") or {}
            texts = [text.strip() for text in summary.values()]
            if not texts or any(not text or text == PLACEHOLDER for text in texts):
                missing.append(module["id"])
    return missing


@pytest.mark.parametrize("manifest", _published_manifests(), ids=lambda path: path.parent.name)
def test_every_module_of_a_published_course_has_a_summary(manifest: Path) -> None:
    assert modules_without_summary(yaml.safe_load(manifest.read_text(encoding="utf-8"))) == []


def test_a_module_left_with_the_placeholder_summary_is_reported() -> None:
    manifest = {
        "blocks": [
            {
                "modules": [
                    {"id": "m01", "summary": {"en": "Locks and indexes."}},
                    {"id": "m02", "summary": {"en": PLACEHOLDER}},
                ]
            },
            {"modules": [{"id": "m03"}]},
        ]
    }
    assert modules_without_summary(manifest) == ["m02", "m03"]
