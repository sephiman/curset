# SPDX-License-Identifier: AGPL-3.0-only
"""S0 skeleton for backend-in-depth: course.yaml blocks and the 68 lesson stubs, from programme.md and the
coverage TSVs (docs/backend-verification/s0/coverage/mNN.tsv). Re-runnable; m00-l01 is never overwritten."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
COURSE = REPO / "content" / "backend-in-depth"
COVERAGE = REPO / "docs" / "backend-verification" / "s0" / "coverage"


def programme() -> list[tuple[str, str, list[tuple[str, str, list[tuple[str, str, str]]]]]]:
    modules: list[tuple[str, str, list[tuple[str, str, list[tuple[str, str, str]]]]]] = []
    for line in (COURSE / "programme.md").read_text(encoding="utf-8").split("\n"):
        if m := re.match(r"### Module (\d+) — (.*)$", line):
            modules.append((m.group(1), m.group(2), []))
        elif m := re.match(r"- \*\*(\d+)\.(\d+) (.*)\*\*$", line):
            modules[-1][2].append((m.group(2), m.group(3), []))
        elif m := re.match(r"  - `([\d.a-z]+)` \[([FJ])\] (.*)$", line):
            modules[-1][2][-1][2].append((m.group(1), m.group(2), m.group(3)))
    return modules


def coverage() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    finals = {p.name.split(".")[0] for p in COVERAGE.glob("m*.final.tsv")}
    drafts = [p for p in COVERAGE.glob("m??.tsv") if p.stem not in finals]
    for tsv in sorted([*COVERAGE.glob("m*.final.tsv"), *drafts]):
        with tsv.open(encoding="utf-8") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                rows[row["bullet"]] = row
    return rows


def yaml_text(text: str) -> str:
    return "'" + text.replace("'", "''") + "'"


def stub(title: str, bullets: list[tuple[str, str, str]], rows: dict[str, dict[str, str]]) -> str:
    lines = [f"# {title}", "", ":::note{type=info}", "Lesson not written yet.", ":::", "", "## Sources", ""]
    for bullet, _mark, _text in bullets:
        row = rows.get(bullet, {})
        cls = row.get("class") or row.get("proposed_class") or "pending"
        refs = [r for r in (row.get("tier_a", "") + "; " + row.get("tier_bc", "")).split("; ") if r.strip()]
        listed = ", ".join(f"`{r.strip()}`" for r in refs) if refs else "no source yet"
        lines.append(f"- `{bullet}` ({cls}): {listed}")
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = coverage()
    out = ["blocks:", "- id: block-a", "  title:", "    en: About this course", "  modules:", "  - id: m00",
           "    title:", "      en: How this course works", "    summary:",
           "      en: What the course covers, how its content is sourced and verified, and how to practise.",
           "    lessons:", "    - id: m00-l01", "      title:", "        en: How this course works",
           "      summary:", "        en: Summary pending.", "- id: block-b", "  title:", "    en: Programme",
           "  modules:"]
    lessons = 0
    for number, title, subsections in programme():
        out += [f"  - id: m{number}", "    title:", f"      en: {yaml_text(title)}", "    summary:",
                "      en: Summary pending.", "    lessons:"]
        for sub, sub_title, bullets in subsections:
            lesson_id = f"m{number}-l{int(sub):02d}"
            out += [f"    - id: {lesson_id}", "      title:", f"        en: {yaml_text(sub_title)}",
                    "      summary:", "        en: Summary pending."]
            path = COURSE / "en" / "lessons" / f"{lesson_id}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(stub(sub_title, bullets, rows), encoding="utf-8")
            lessons += 1
    head = (COURSE / "course.yaml").read_text(encoding="utf-8").split("blocks:\n")[0]
    (COURSE / "course.yaml").write_text(head + "\n".join(out) + "\n", encoding="utf-8")
    print(f"{lessons} stubs", file=sys.stderr)


if __name__ == "__main__":
    main()
