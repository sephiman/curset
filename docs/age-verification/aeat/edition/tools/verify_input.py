"""verify_input.py <lesson>: the blind verifier's input — each explanation paragraph with the text of the articles it cites.

The lesson's literal sentences are not included: the verifier checks the paragraph against the norm only.
"""

from __future__ import annotations

import sys

from article_text import article, cited_units
from explanation import LAYER, parse_draft


def build(lesson: str) -> str:
    out = [f"# Verifier input — `{lesson}`", ""]
    for entry in parse_draft(LAYER / lesson / "draft.md"):
        if entry.kind not in ("overview", "after"):
            continue
        out += [f"## KEY: {entry.key}", "", entry.text, ""]
        for norm, number, pdf in cited_units(lesson, entry.text):
            out += [f"### {norm}, artículo {number}", "", article(pdf, number), ""]
    path = LAYER / lesson / "verify-input.md"
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return str(path)


if __name__ == "__main__":
    for lesson in sys.argv[1:]:
        print(build(lesson))
