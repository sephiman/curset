# SPDX-License-Identifier: AGPL-3.0-only
"""Citations of a course built on technical sources (`sources/sources.yaml`): `source_id#anchor`, written as
inline code, several joined by `; ` (docs/backend-verification/s1/contracts.md).

Stored-outside-git copies resolve under `$CURSET_SOURCES_LOCAL` (requirements amendment 2); this module only
reads the registry and the anchor index, both in the repo, so it never needs the local folder.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

SOURCES_FILE = Path("sources") / "sources.yaml"
ANCHORS_DIR = Path("sources") / "anchors"
LOCAL_ENV = "CURSET_SOURCES_LOCAL"
_INLINE_CODE = re.compile(r"`([^`\n]+)`")
_REF = re.compile(r"^(?P<source>[a-z0-9][a-z0-9._-]*)#(?P<anchor>\S(?:.*\S)?)$")


@dataclass(frozen=True)
class SourceRef:
    source_id: str
    anchor: str

    def __str__(self) -> str:
        return f"{self.source_id}#{self.anchor}"


@dataclass(frozen=True)
class TechSource:
    id: str
    tier: str
    title: str
    url: str
    licence: str
    extract_allowed: bool
    #: `repo` (under the course folder) or `local` (under the local-sources folder).
    storage: str
    #: Course-relative for `repo`, relative to the local-sources folder for `local`.
    path: str


def parse_ref(text: str) -> SourceRef | None:
    """One citation, with or without its backticks; None when it is not `source_id#anchor`."""
    match = _REF.match(text.strip().strip("`").strip())
    return SourceRef(match["source"], match["anchor"]) if match else None


def parse_refs(text: str) -> list[SourceRef] | None:
    """Every citation of a `; `-joined list written as inline code; None when anything else is in it."""
    spans = _INLINE_CODE.findall(text)
    leftover = _INLINE_CODE.sub("", text).replace(";", "").strip()
    if not spans or leftover:
        return None
    refs = [parse_ref(span) for span in spans]
    return [ref for ref in refs if ref is not None] if all(refs) else None


def local_sources_dir(course_slug: str) -> Path:
    default = Path.home() / "PycharmProjects" / "curset-saved-originals" / course_slug / "local"
    configured = os.environ.get(LOCAL_ENV)
    return Path(configured).expanduser() if configured else default


@dataclass(frozen=True)
class TechSourceIndex:
    course_dir: Path
    sources: dict[str, TechSource]
    #: source id → its anchors, in page order.
    anchors: dict[str, tuple[str, ...]]

    @classmethod
    def load(cls, course_dir: Path) -> TechSourceIndex | None:
        """None for a course without `sources/sources.yaml`."""
        registry = course_dir / SOURCES_FILE
        if not registry.exists():
            return None
        loaded = yaml.safe_load(registry.read_text(encoding="utf-8")) or {}
        entries: list[dict[str, object]] = loaded.get("sources", [])
        sources = {str(e["id"]): _source(e) for e in entries}
        anchors = {sid: _anchors(course_dir / ANCHORS_DIR / f"{sid}.json") for sid in sources}
        return cls(course_dir, sources, anchors)

    def problem(self, ref: SourceRef) -> str | None:
        """Why the citation does not resolve, or None when it does."""
        if ref.source_id not in self.sources:
            return f"unknown source «{ref.source_id}»"
        if ref.anchor not in self.anchors[ref.source_id]:
            return f"no anchor «{ref.anchor}» in {ref.source_id}"
        return None

    def file_of(self, source_id: str, course_slug: str) -> Path:
        source = self.sources[source_id]
        if source.storage == "local":
            return local_sources_dir(course_slug) / source.path
        return self.course_dir / source.path


def _source(entry: dict[str, object]) -> TechSource:
    return TechSource(
        id=str(entry["id"]),
        tier=str(entry.get("tier", "")),
        title=str(entry.get("title", "")),
        url=str(entry.get("url", "")),
        licence=str(entry.get("licence", "")),
        extract_allowed=bool(entry.get("extract_allowed", False)),
        storage=str(entry.get("storage", "repo")),
        path=str(entry.get("path", "")),
    )


def _anchors(path: Path) -> tuple[str, ...]:
    if not path.exists():
        return ()
    rows = json.loads(path.read_text(encoding="utf-8"))["anchors"]
    return tuple(str(row["anchor"]) for row in rows)
