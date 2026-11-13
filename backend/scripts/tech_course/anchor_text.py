# SPDX-License-Identifier: AGPL-3.0-only
"""The stored text of a source's anchors, recomputed from the stored file; `storage: local` copies resolve
through `$CURSET_SOURCES_LOCAL` and are skipped (never failed) when that folder is absent."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field

from scripts.tech_sources import Anchor, anchors_of
from tradeschool.citations.tech import SourceRef, TechSourceIndex, local_sources_dir


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


@dataclass
class AnchorStore:
    index: TechSourceIndex
    course: str
    skipped_local: int = 0
    _loaded: dict[str, dict[str, Anchor] | None] = field(default_factory=dict)
    _warned: bool = False

    def _anchors(self, source_id: str) -> dict[str, Anchor] | None:
        """The recomputed anchors of a source; None when its local copy cannot be read here."""
        if source_id not in self._loaded:
            self._loaded[source_id] = self._read(source_id)
        return self._loaded[source_id]

    def _read(self, source_id: str) -> dict[str, Anchor] | None:
        if self.index.sources[source_id].storage == "local" and not local_sources_dir(self.course).is_dir():
            self._warn_once()
            return None
        path = self.index.file_of(source_id, self.course)
        if not path.is_file():
            raise FileNotFoundError(f"{source_id}: stored file {path} is missing")
        return {anchor.anchor: anchor for anchor in anchors_of(path)}

    def _warn_once(self) -> None:
        if not self._warned:
            folder = local_sources_dir(self.course)
            print(
                f"warning: {folder} is absent; content checks of local sources are skipped", file=sys.stderr
            )
            self._warned = True

    def anchor(self, ref: SourceRef) -> Anchor | None:
        """The anchor recomputed from the stored file, or None when it cannot be read here."""
        found = self._anchors(ref.source_id)
        if found is None:
            self.skipped_local += 1
            return None
        if ref.anchor not in found:
            raise KeyError(f"{ref}: the stored file has no such anchor")
        return found[ref.anchor]

    def recorded_digest(self, ref: SourceRef) -> str | None:
        path = self.index.course_dir / "sources" / "anchors" / f"{ref.source_id}.json"
        rows = json.loads(path.read_text(encoding="utf-8"))["anchors"]
        return next((str(row["sha256"]) for row in rows if row["anchor"] == ref.anchor), None)
