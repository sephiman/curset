"""Re-wrap over-long paragraph and list-item lines of lessons to 118 columns; tables, headings and fences untouched."""

import sys
import textwrap
from pathlib import Path

for name in sys.argv[1:]:
    path = Path(name)
    out = []
    for line in path.read_text().split("\n"):
        s = line.lstrip()
        if len(line) <= 120 or s.startswith(("|", "#", ":::", "```")):
            out.append(line)
            continue
        indent = line[: len(line) - len(s)]
        first, rest = (indent, indent + "  ") if s.startswith("- ") else (indent, indent)
        wrapped = textwrap.wrap(s, width=118 - len(indent), break_long_words=False, break_on_hyphens=False)
        out.append(first + wrapped[0])
        out += [rest + w for w in wrapped[1:]]
    path.write_text("\n".join(out))
