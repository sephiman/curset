# SPDX-License-Identifier: AGPL-3.0-only
"""`:::judgement{source="…" ref="…"}` (class J): `source` names who the text attributes the judgement to
(required); `ref` is an optional `source_id#anchor` citation (docs/backend-verification/s1/contracts.md)."""

from __future__ import annotations

import re

from tradeschool.citations.tech import TechSourceIndex, parse_ref

_FENCED_CODE = re.compile(r"^```.*?^```[ \t]*$", re.DOTALL | re.MULTILINE)
_OPENING = re.compile(r"^:::judgement(?P<attrs>\{(?:[^}\"']|\"[^\"]*\"|'[^']*')*\})?[ \t]*$", re.MULTILINE)
_ATTRIBUTE = re.compile(r"\s*(?P<name>[\w-]+)=(?:\"(?P<double>[^\"]*)\"|'(?P<single>[^']*)')\s*")
ALLOWED = {"source", "ref"}


def judgement_problems(lesson_id: str, markdown: str, tech: TechSourceIndex | None) -> list[str]:
    prose = _FENCED_CODE.sub("", markdown)
    problems: list[str] = []
    for opening in _OPENING.finditer(prose):
        where = f"lesson {lesson_id}, judgement {opening.group(0)!r}"
        attributes = _attributes(opening.group("attrs") or "{}")
        if attributes is None:
            problems.append(f'{where}: attributes must be name="value" pairs')
            continue
        if unknown := sorted(set(attributes) - ALLOWED):
            problems.append(f"{where}: unknown attribute {', '.join(unknown)}")
        if not attributes.get("source", "").strip():
            problems.append(f"{where}: `source` is required")
        if ref := attributes.get("ref"):
            problems += _ref_problem(where, ref, tech)
    return problems


def _attributes(braced: str) -> dict[str, str] | None:
    inner, found, position = braced[1:-1], {}, 0
    while position < len(inner):
        match = _ATTRIBUTE.match(inner, position)
        if match is None:
            return None
        found[match["name"]] = match["double"] if match["double"] is not None else match["single"]
        position = match.end()
    return found


def _ref_problem(where: str, ref: str, tech: TechSourceIndex | None) -> list[str]:
    parsed = parse_ref(ref)
    if parsed is None:
        return [f"{where}: `ref` «{ref}» is not source_id#anchor"]
    if tech is not None and (why := tech.problem(parsed)):
        return [f"{where}: `ref` {why}"]
    return []
