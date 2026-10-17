# Helper scripts used by writers and verifiers

Scratch helpers, kept here as text so a later round can reuse them.

## fuentes_order.py

```python
"""Reorder a lesson's Fuentes block by first citation in the body; report cited-but-unlisted and listed-but-uncited."""
import re, sys
p = sys.argv[1]; s = open(p, encoding="utf-8").read()
body, fu = s.split("\n## Fuentes\n", 1)
cited = []
for m in re.finditer(r"`([^`]+\.(?:html|pdf|txt|json))`", body):
    if m.group(1) not in cited: cited.append(m.group(1))
entries = re.split(r"\n(?=- `)", fu.strip("\n"))
by = {re.match(r"- `([^`]+)`", e).group(1): e for e in entries}
print("missing in Fuentes:", [c for c in cited if c not in by]); print("uncited:", [b for b in by if b not in cited])
new = "\n".join(by[c] for c in cited if c in by)
if "--write" in sys.argv:
    open(p, "w", encoding="utf-8").write(body + "\n## Fuentes\n\n" + new + "\n")
print("in order:", [b for b in by] == [c for c in cited if c in by])
```

## pagetext.py

```python
"""Print the readable text of a saved HTML page, one block per line. Usage: python3 -I pagetext.py FILE [GREP]"""

import re
import sys
from html.parser import HTMLParser

BLOCK = {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "br", "td", "th", "section", "article", "dt", "dd", "table", "ul", "ol"}
SKIP = {"script", "style", "noscript", "svg", "template"}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in SKIP:
            self.skip_depth += 1
        elif tag in BLOCK:
            self.parts.append("\n")
        if tag in ("td", "th"):
            self.parts.append(" | ")

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP and self.skip_depth:
            self.skip_depth -= 1
        elif tag in BLOCK:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)


def page_text(path: str) -> str:
    extractor = TextExtractor()
    with open(path, encoding="utf-8", errors="replace") as handle:
        extractor.feed(handle.read())
    lines = (re.sub(r"[ \t\r\f\v\xa0]+", " ", line).strip() for line in "".join(extractor.parts).split("\n"))
    return "\n".join(line for line in lines if line)


if __name__ == "__main__":
    text = page_text(sys.argv[1])
    if len(sys.argv) > 2:
        pattern = re.compile(sys.argv[2], re.IGNORECASE)
        rows = text.split("\n")
        for i, row in enumerate(rows):
            if pattern.search(row):
                print(f"{i}: " + " / ".join(rows[max(0, i - 1) : i + 2]))
    else:
        print(text)
```

## rewrap.py

```python
"""Re-wrap list items (and their 2-space continuation lines) whose lines exceed 120 chars. Usage: rewrap.py FILE"""
import re, sys, textwrap
p = sys.argv[1]; lines = open(p, encoding="utf-8").read().split("\n")
out, i = [], 0
while i < len(lines):
    line = lines[i]
    if line.startswith("- "):
        j = i + 1
        while j < len(lines) and lines[j].startswith("  ") and not lines[j].startswith("  - "):
            j += 1
        block = lines[i:j]
        if any(len(b) > 120 for b in block):
            text = " ".join(b.strip() for b in block)[2:]
            # never break inside a code span: protect spaces in `...`
            prot = re.sub(r"`[^`]*`", lambda m: m.group(0).replace(" ", "\x00"), text)
            w = textwrap.wrap(prot, width=120, initial_indent="- ", subsequent_indent="  ", break_long_words=False, break_on_hyphens=False)
            block = [x.replace("\x00", " ") for x in w]
        out.extend(block); i = j
    else:
        out.append(line); i += 1
open(p, "w", encoding="utf-8").write("\n".join(out))
```
