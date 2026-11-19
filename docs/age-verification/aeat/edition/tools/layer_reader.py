"""layer_reader.py <lesson…>: the student reader's input — each section's literal text next to its case (no verdicts shown)."""

from __future__ import annotations

import sys

from explanation import LAYER, LESSONS, section_bodies
from layer import LAYER_LINE, parse


def build(lesson: str) -> str:
    lines = (LESSONS / f"{lesson}.md").read_text(encoding="utf-8").split("\n")
    bodies = {(h, n): b for _, h, n, b in section_bodies(lines)}
    out = [f"# Reader input — `{lesson}`", ""]
    for part in parse(lesson)[0]:
        if part.kind != "caso":
            continue
        body = "\n".join(l for l in bodies[(part.heading, part.occurrence)].split("\n") if not LAYER_LINE.match(l))
        out += [f"## KEY: {part.key}", "", "### The section as the lesson gives it", "", body.strip(), "", "### The case", "", part.text, ""]
    path = LAYER / lesson / "reader-input.md"
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return str(path)


if __name__ == "__main__":
    for name in sys.argv[1:]:
        print(build(name))
