"""split_paragraphs.py <lesson…>: turn prose paragraphs over 120 words that string several cited rules into lists."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "backend"))

from scripts.provenance import _split  # noqa: E402

LESSONS = ROOT / "content/aeat-agentes-hacienda/es/lessons"
CITED_END = re.compile(r"\)[.:]?$")
SKIP = ("#", "-", "|", ":::", ">", "*", "!", "[")


def _items(paragraph: str) -> list[str] | None:
    sentences = [s.strip() for s in _split(paragraph) if s.strip()]
    if " ".join(sentences).split() != paragraph.split():
        return None  # the splitter would lose or reorder words: leave the paragraph alone
    items: list[str] = []
    pending: list[str] = []
    for sentence in sentences:
        pending.append(sentence)
        if CITED_END.search(sentence):
            items.append(" ".join(pending))
            pending = []
    if pending:
        if not items:
            return None
        items[-1] = f"{items[-1]} {' '.join(pending)}"
    return items if len(items) >= 2 else None


def split(text: str) -> tuple[str, int]:
    blocks = text.split("\n\n")
    changed = 0
    in_directive = False
    for i, block in enumerate(blocks):
        stripped = block.strip()
        if stripped.startswith(":::"):
            in_directive = not stripped.endswith(":::") or stripped == ":::"
        if in_directive or not stripped or stripped.startswith(SKIP) or "\n" in stripped:
            continue
        if len(stripped.split()) <= 120:
            continue
        items = _items(stripped)
        if items is None:
            continue
        lead = ""
        if items[0].endswith(":") and not CITED_END.search(items[0][:-1]):
            lead, items = items[0], items[1:]
        listed = "\n".join(f"- {item}" for item in items)
        blocks[i] = f"{lead}\n\n{listed}" if lead else listed
        changed += 1
    return "\n\n".join(blocks), changed


if __name__ == "__main__":
    for lesson in sys.argv[1:]:
        path = LESSONS / f"{lesson}.md"
        text, changed = split(path.read_text())
        path.write_text(text)
        print(f"{lesson}: {changed} paragraphs split")
