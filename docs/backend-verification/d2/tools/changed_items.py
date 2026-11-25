# SPDX-License-Identifier: AGPL-3.0-only
"""List the items of a lesson that are new or changed against its previous text, numbered, for the blind check.

    python changed_items.py PREVIOUS.md CURRENT.md [OUT.tsv]

Item = one sentence of prose, one table row of an esquema, one bullet of Key points, one diagram block.
Columns: id, kind (plain | precise | judgement | row | keypoint | diagram), section, text. `plain` is an uncited
sentence outside a judgement block; `precise` ends with a citation parenthetical. Items whose text is
byte-identical to one in PREVIOUS are not listed (they kept their earlier verification). Prints the counts.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CITED = re.compile(r"\(`[^`]+`(?:; `[^`]+`)*\)\.?$")
SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z`\"“(])")


def items(text: str) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    section, mode, fence, diagram = "", "", False, []
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            fence = not fence
            continue
        if fence or not line or line.startswith("<!--"):
            continue
        if line.startswith("## "):
            section = line[3:]
            mode = "keypoint" if section == "Key points" else "skip" if section == "Sources" else ""
            continue
        if line.startswith(":::diagram"):
            diagram = [line]
            mode = "diagram"
            continue
        if mode == "diagram":
            diagram.append(line)
            if line == ":::":
                out.append(("diagram", section, "\n".join(diagram)))
                mode = ""
            continue
        mode = _after(line, mode)
        if mode == "skip" or line.startswith(":::") or line.startswith("# "):
            continue
        out += _line_items(line, section, mode)
    return out


def _after(line: str, mode: str) -> str:
    if line.startswith(":::judgement"):
        return "judgement"
    if line.startswith(":::esquema"):
        return "esquema"
    if line == ":::" and mode in ("judgement", "esquema"):
        return ""
    return mode


def _line_items(line: str, section: str, mode: str) -> list[tuple[str, str, str]]:
    if mode == "esquema":
        if line.startswith("|") and not set(line) <= set("|- :") and not line.startswith("| ---"):
            return [("row", section, line)]
        return []
    if mode == "keypoint":
        return [("keypoint", section, line.lstrip("- "))]
    kind = "judgement" if mode == "judgement" else None
    parts = SPLIT.split(line.lstrip("-* ").strip())
    return [(kind or ("precise" if CITED.search(p) else "plain"), section, p) for p in parts if p]


def main() -> int:
    previous = {text for _, _, text in items(Path(sys.argv[1]).read_text(encoding="utf-8"))}
    current = items(Path(sys.argv[2]).read_text(encoding="utf-8"))
    stem = Path(sys.argv[2]).stem
    lines, counts = [], {}
    for n, (kind, section, text) in enumerate(current, 1):
        if text in previous:
            continue
        counts[kind] = counts.get(kind, 0) + 1
        lines.append(f"{stem}-s{n:03d}\t{kind}\t{section}\t{text.replace(chr(10), ' ⏎ ')}")
    if len(sys.argv) > 3:
        Path(sys.argv[3]).write_text("\n".join(lines) + "\n", encoding="utf-8")
    total = len(current)
    print(f"{stem}: {total} items, {len(lines)} new or changed {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
