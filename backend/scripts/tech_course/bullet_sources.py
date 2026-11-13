# SPDX-License-Identifier: AGPL-3.0-only
"""The source entries the S0 coverage report gives each programme bullet, and which are stored."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

from scripts.tech_course.lessons import REPO, course_dir
from scripts.tech_course.programme import lesson_of

S0 = REPO / "docs" / "backend-verification" / "s0"
CANDIDATE = "candidate:"


@dataclass(frozen=True)
class Row:
    bullet: str
    kind: str
    entries: tuple[str, ...]
    rule: str
    note: str


@dataclass(frozen=True)
class Storage:
    source_ids: frozenset[str]
    url_ids: dict[str, str]
    tier_b_keys: frozenset[str]
    anchors_dir: Path

    def is_stored(self, entry: str) -> bool:
        if entry.startswith(CANDIDATE):
            return False
        if "#" in entry:
            source, anchor = entry.split("#", 1)
            return anchor in self._anchors(source)
        return entry in self.source_ids or entry in self.url_ids or entry in self.tier_b_keys

    def _anchors(self, source: str) -> set[str]:
        path = self.anchors_dir / f"{source}.json"
        if not path.is_file():
            return set()
        return {item["anchor"] for item in json.loads(path.read_text(encoding="utf-8"))["anchors"]}

    def rendered(self, entry: str) -> str:
        """The stored form of an entry (a registry url becomes its id); an unstored one keeps `candidate:`."""
        if self.is_stored(entry):
            return self.url_ids.get(entry, entry)
        return entry if entry.startswith(CANDIDATE) else f"{CANDIDATE} {entry}"


def load_storage(course: str, s0: Path = S0) -> Storage:
    root = course_dir(course) / "sources"
    sources = yaml.safe_load((root / "sources.yaml").read_text(encoding="utf-8"))["sources"]
    tier_b = yaml.safe_load((s0 / "tier-b.yaml").read_text(encoding="utf-8")) or []
    return Storage(
        frozenset(item["id"] for item in sources),
        {item["url"]: item["id"] for item in sources if item.get("url")},
        frozenset(item["key"] for item in tier_b),
        root / "anchors",
    )


def _split(cell: str) -> list[str]:
    return [_without_attribution(part) for part in cell.split(";") if part.strip()]


def _without_attribution(entry: str) -> str:
    return re.sub(r"\s+\([^()]*\)$", "", entry.strip())


def _table(path: Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    header = lines[0].split("\t")
    return [
        dict(zip(header, line.split("\t") + [""] * len(header), strict=False)) for line in lines[1:] if line
    ]


def _merged(*groups: list[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(entry for group in groups for entry in group))


def load_rows(s0: Path = S0) -> dict[str, Row]:
    """The final report rows by bullet, with the gaps file's extra entries appended."""
    rows: dict[str, Row] = {}
    for report in sorted((s0 / "coverage").glob("m*.final.tsv")):
        for cells in _table(report):
            entries = _merged(_split(cells["tier_a"]), _split(cells["tier_bc"]))
            rows[cells["bullet"]] = Row(
                cells["bullet"], cells["class"], entries, cells["rule"], cells["note"]
            )
    gaps = s0 / "coverage" / "gaps.tsv"
    for cells in _table(gaps) if gaps.is_file() else []:
        row = rows.get(cells["bullet"])
        if row is not None:
            rows[row.bullet] = Row(
                row.bullet, row.kind, _merged(list(row.entries), _split(cells["tier_bc"])), row.rule, row.note
            )
    return rows


def default_rule_reasons(s0: Path = S0) -> dict[str, str]:
    path = s0 / "default-rules.tsv"
    return {cells["bullet"]: cells["reason"] for cells in _table(path)} if path.is_file() else {}


def has_stored_source(row: Row | None, storage: Storage) -> bool:
    return row is not None and any(storage.is_stored(entry) for entry in row.entries)


def is_dropped(row: Row, storage: Storage) -> bool:
    return row.kind == "drop" or ("R2" in row.rule.split(",") and not has_stored_source(row, storage))


def rows_of_lesson(rows: dict[str, Row], lesson: str) -> list[Row]:
    return [row for row in rows.values() if lesson_of(row.bullet) == lesson]
