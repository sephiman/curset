"""restore_esquemas.py <lesson> <title prefix>…: put an esquema of the pre-R2d lesson back in the lesson, whole, after the paragraph it followed.

The block is copied byte for byte from edition/pre/<lesson>.md. Its place is the line that preceded it there (looked up in the current
lesson; if that line is gone, the end of the literal text of the same heading, before the explanation layer's «Caso.»). Reports where it went.
"""

from __future__ import annotations

import re
import sys

from explanation import LESSONS
from lesson_model import ROOT

PRE = ROOT / "docs/age-verification/aeat/edition/pre"
LAYER_LEADS = ("**Caso.**", "**Preguntas que responde:**", "**Para qué sirve.**", "**Término")


def block_in(lines: list[str], prefix: str) -> tuple[int, int]:
    for i, line in enumerate(lines):
        if line.startswith(":::esquema") and f'title="{prefix}' in line:
            return i, next(j for j in range(i, len(lines)) if lines[j] == ":::")
    raise SystemExit(f"no esquema starting «{prefix}»")


def anchor_line(pre: list[str], start: int, now: list[str]) -> tuple[int, str]:
    k = start - 1
    while k >= 0 and not pre[k].strip():
        k -= 1
    previous = pre[k]
    if previous in now:
        return now.index(previous), "after its paragraph"
    heading = next(pre[h] for h in range(start, -1, -1) if re.match(r"#{2,4} ", pre[h]))
    h = now.index(heading)
    end = next((e for e in range(h + 1, len(now)) if re.match(r"#{2,4} ", now[e])), len(now))
    for e in range(h + 1, end):
        if now[e].startswith(LAYER_LEADS) and now[e].startswith("**Caso.**"):
            end = e
            break
    while not now[end - 1].strip():
        end -= 1
    if now[end - 1] == ":::":
        opener = max(o for o in range(h, end) if now[o].startswith(":::") and now[o] != ":::")
        if now[opener].startswith(":::note"):
            end = opener
            while not now[end - 1].strip():
                end -= 1
    return end - 1, "end of its heading (the paragraph before it is gone)"


def restore(lesson: str, prefix: str) -> str:
    pre = (PRE / f"{lesson}.md").read_text(encoding="utf-8").split("\n")
    path = LESSONS / f"{lesson}.md"
    now = path.read_text(encoding="utf-8").split("\n")
    start, end = block_in(pre, prefix)
    title = re.search(r'title="([^"]*)"', pre[start]).group(1)
    if any(line.startswith(":::esquema") and f'title="{title}"' in line for line in now):
        return f"{lesson}: «{title[:60]}» already there"
    at, how = anchor_line(pre, start, now)
    now[at + 1 : at + 1] = ["", *pre[start : end + 1]]
    path.write_text("\n".join(now), encoding="utf-8")
    return f"{lesson}: «{title[:60]}» {end - start - 1} lines, {how} (line {at + 1})"


if __name__ == "__main__":
    for prefix in sys.argv[2:]:
        print(restore(sys.argv[1], prefix))
