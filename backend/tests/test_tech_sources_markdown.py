# SPDX-License-Identifier: AGPL-3.0-only
"""Markdown sources: anchors from `#` headings, and registering a repo file without fetching."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pytest
import yaml
from scripts import tech_sources
from scripts.tech_sources import markdown_anchors

DOC = """# Title

intro

## 4. Content classes

**F — fact.** Verifiable.

```
## not a heading
```

### Sub

deep text

## 4. Content classes

again
"""


def test_markdown_anchors_follow_headings_skip_fences_and_deduplicate() -> None:
    anchors = markdown_anchors(DOC)
    assert [a.anchor for a in anchors] == ["title", "4-content-classes", "sub", "4-content-classes~2"]
    assert [a.level for a in anchors] == [1, 2, 3, 2]
    classes = anchors[1]
    assert "## not a heading" in classes.text and "deep text" not in classes.text


def test_register_file_stores_a_course_tier_entry_with_a_course_relative_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "req.md").write_text(DOC, encoding="utf-8")
    (tmp_path / "content" / "c" / "sources").mkdir(parents=True)
    monkeypatch.setattr(tech_sources, "REPO", tmp_path)
    monkeypatch.setattr(tech_sources, "CONTENT", tmp_path / "content")
    tech_sources.register_file(
        argparse.Namespace(
            course="c",
            id="req",
            file="docs/req.md",
            product="curset",
            version="1.2",
            title="Req",
            licence="AGPL-3.0-only",
        )
    )
    (entry,) = yaml.safe_load((tmp_path / "content/c/sources/sources.yaml").read_text())["sources"]
    assert (entry["tier"], entry["path"], entry["url"], entry["storage"]) == (
        "course",
        "../../docs/req.md",
        "docs/req.md",
        "repo",
    )
    anchors = json.loads((tmp_path / "content/c/sources/anchors/req.json").read_text())["anchors"]
    assert "4-content-classes" in [a["anchor"] for a in anchors]
