"""glossary_waiting.py [--write]: entries whose origin lesson no longer uses the term go to edition/glossary-waiting.md.

Surface forms are the entry's `match` list or its term head and naive plural (as frontend/src/lib/glossary/terms.ts).
Entries are removed from glossary.yaml as whole text blocks; nothing else in the file changes.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
COURSE = ROOT / "content/aeat-agentes-hacienda"
EDITION = ROOT / "docs/age-verification/aeat/edition"


def variants(entry: dict) -> list[str]:
    if entry.get("match"):
        return [str(m).split(" (")[0].strip() for m in entry["match"]]
    head = str(entry["es"]).split(" (")[0].strip()
    plural = head + ("s" if re.search(r"[aeiouáéíóú]$", head, re.I) else "es")
    return [head] if head.isupper() else [head, plural]


def uses(term_variants: list[str], text: str) -> bool:
    return any(re.search(rf"(?<![\w]){re.escape(v)}(?![\w])", text, re.I) for v in term_variants)


def main(argv: list[str]) -> int:
    path = COURSE / "glossary.yaml"
    raw = path.read_text()
    data = yaml.safe_load(raw)
    lessons = {p.stem: p.read_text() for p in (COURSE / "es/lessons").glob("m0*.md")}
    waiting = []
    for entry in data["terms"]:
        origins = [o for o in [entry.get("origin"), *[s.get("origin") for s in entry.get("senses", [])]] if o]
        forms = variants(entry)
        if entry.get("aliasOf"):
            continue
        if not all(uses(forms, lessons.get(o, "")) for o in origins):
            waiting.append(entry["id"])
    lines = raw.split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith("- id: ")]
    blocks = {lines[s].split(": ", 1)[1].strip(): (s, (starts[k + 1] if k + 1 < len(starts) else len(lines)))
              for k, s in enumerate(starts)}
    log = ["# Glossary entries waiting (edition step 1)", "",
           "Entries whose origin lesson no longer uses the term after the assembly. Back in the glossary when a lesson "
           "of the explanation layer or the reserve view teaches the term.", ""]
    for eid in waiting:
        a, b = blocks[eid]
        log += [f"## {eid}", "", "```yaml", *lines[a:b], "```", ""]
    if "--write" in argv:
        drop = {i for eid in waiting for i in range(*blocks[eid])}
        path.write_text("\n".join(l for i, l in enumerate(lines) if i not in drop))
        (EDITION / "glossary-waiting.md").write_text("\n".join(log))
    print(len(data["terms"]), "entries;", len(waiting), "waiting:", ", ".join(waiting))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
