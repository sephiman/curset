"""fails.py <lesson…>: merge the blind verifiers' FAIL rows and the reader's REWRITE/CUT rows into explanation/<lesson>/fix-brief.md.

Latest verifier file wins per key (layer-verifier-N, verifier-N); `cut` lists the keys the reader marked CUT (to be dropped, not rewritten).
Also writes recheck-keys.txt (keys to rewrite) and prints per-lesson counts.
"""

from __future__ import annotations

import re
import sys

from explanation import LAYER
from layer import parse

ROW = re.compile(r"^\|\s*`?(?P<key>[^|`]+?)`?\s*\|\s*(?P<verdict>PASS|FAIL|KEEP|REWRITE|CUT)\b[^|]*\|\s*(?P<reason>.*?)\s*\|?\s*$")


def latest(lesson: str, pattern: str) -> dict[str, tuple[str, str]]:
    found: dict[str, tuple[str, str]] = {}
    for path in sorted((LAYER / lesson).glob(pattern), key=lambda p: (len(p.stem), p.stem)):
        for line in path.read_text(encoding="utf-8").splitlines():
            match = ROW.match(line)
            if match and match["key"].strip() not in ("key", "KEY"):
                found[match["key"].strip()] = (match["verdict"], match["reason"])
    return found


def build(lesson: str) -> tuple[int, int, int, int]:
    verdicts = latest(lesson, "layer-verifier-*.md")
    overview = latest(lesson, "verifier-*.md").get("overview")
    reader = latest(lesson, "layer-reader-*.md")
    texts = {p.key: p.text for p in parse(lesson)[0]}
    rewrite: list[str] = []
    cut: list[str] = []
    body = [f"# Fix brief — `{lesson}`", ""]
    if overview and overview[0] == "FAIL":
        rewrite.append("overview")
        body += ["## overview (draft.md, the OVERVIEW block) — FAIL", "", overview[1], ""]
    for key, text in texts.items():
        verdict, reason = verdicts.get(key, ("", ""))
        seen, why = reader.get(key, ("", ""))
        if seen == "CUT" and verdict != "FAIL":
            cut.append(key)
            continue
        if verdict == "FAIL" or seen == "REWRITE" or (seen == "CUT" and verdict == "FAIL"):
            rewrite.append(key)
            body += [f"## {key}", "", f"Current: {text}", "", f"Blind verifier: {verdict or '-'} — {reason}", f"Student reader: {seen or '-'} — {why}", ""]
    (LAYER / lesson / "fix-brief.md").write_text("\n".join(body) + "\n", encoding="utf-8")
    (LAYER / lesson / "recheck-keys.txt").write_text("\n".join(rewrite) + "\n", encoding="utf-8")
    (LAYER / lesson / "cut-keys.txt").write_text("\n".join(cut) + "\n", encoding="utf-8")
    cases = [k for k in texts if k.startswith("caso:")]
    failed = sum(1 for k in cases if verdicts.get(k, ("",))[0] == "FAIL")
    return len(cases), failed, len(rewrite), len(cut)


if __name__ == "__main__":
    for name in sys.argv[1:]:
        cases, failed, rewrite, cut = build(name)
        print(f"{name}: cases {cases}, first-check FAIL {failed}, to rewrite {rewrite}, reader CUT {cut}")
