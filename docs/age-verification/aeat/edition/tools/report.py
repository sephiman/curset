"""report.py: edition/report.md — per tema words pre-R2d / pool / now, kept by origin, reserve, overruns with their reason."""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lesson_model import ROOT, parse, words  # noqa: E402

AEAT = ROOT / "docs/age-verification/aeat"
EDITION = AEAT / "edition"
WORK = ROOT / "docs/_work/age-verification/aeat/edition"
CONTENT = ROOT / "content/aeat-agentes-hacienda/es/lessons"
ORDER = ["HEAD", "R2b restore", "review item", "No confundir", "gap fill", "range coverage", "reworded"]


def prose(text: str) -> int:
    return sum(words(s.text) for s in parse(text).prose_sentences)


def main() -> int:
    budget = json.loads((EDITION / "budget.json").read_text())
    rows = [
        "| Lesson | Pre-R2d | Pool | Now | Now / pre | Budget | Overrun | Sentences kept / pool | Esquemas kept / pool | Rows kept / pool |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    origin_rows = ["| Lesson | " + " | ".join(ORDER) + " | rows |", "|---|" + "---:|" * (len(ORDER) + 1)]
    reasons: list[str] = []
    tot = dict(pre=0, pool=0, now=0, budget=0, over=0, sk=0, st=0, ek=0, et=0, rk=0, rt=0)
    for lesson, info in budget.items():
        text = (CONTENT / f"{lesson}.md").read_text()
        pre = int(info["pre_prose"])
        pool = int(info["pool_prose"])
        now = prose(text)
        if lesson == "m00-l01":
            rows.append(f"| {lesson} | {pre:,} | {pool:,} | {now:,} | 1.00 | — | 0 | unchanged | — | — |")
            tot["pre"] += pre
            tot["pool"] += pool
            tot["now"] += now
            continue
        sel = json.loads((WORK / "selection" / f"{lesson}.json").read_text())
        b = int(info["budget"])
        over = max(now - b, 0)
        model = parse(text)
        pool_model = parse((AEAT / "pool" / f"{lesson}.md").read_text())
        rows_kept = sum(len(e.sentences) for e in model.esquemas)
        rows_total = sum(len(e.sentences) for e in pool_model.esquemas)
        rows.append(
            f"| {lesson} | {pre:,} | {pool:,} | {now:,} | {now / pre:.2f} | {b:,} | {over:,} | "
            f"{sel['sentences_kept']}/{sel['sentences_total']} | {len(model.esquemas)}/{len(pool_model.esquemas)} | {rows_kept:,}/{rows_total:,} |"
        )
        ko = sel["kept_by_origin"]
        origin_rows.append(
            f"| {lesson} | " + " | ".join(str(ko.get(o, 0)) for o in ORDER) + f" | {sum(v for k, v in ko.items() if k.startswith('row:'))} |"
        )
        cw = sel["by_class_words"]
        if over:
            forced = {k: cw.get(k, 0) for k in ("a", "b", "c", "restore", "lead-in", "items", "note") if cw.get(k)}
            reasons.append(
                f"- {lesson}: +{over:,} words over {b:,}. Forced words (never cut): {forced}; derived «Lo que más cae» items "
                f"{sel['derived_kept']}, «Normativa» {sel['normativa_words']} (counted in Now)."
            )
        tot["pre"] += pre; tot["pool"] += pool; tot["now"] += now; tot["budget"] += b; tot["over"] += over
        tot["sk"] += sel["sentences_kept"]; tot["st"] += sel["sentences_total"]
        tot["ek"] += len(model.esquemas); tot["et"] += len(pool_model.esquemas); tot["rk"] += rows_kept; tot["rt"] += rows_total
    rows.append(
        f"| **Total** | **{tot['pre']:,}** | **{tot['pool']:,}** | **{tot['now']:,}** | **{tot['now'] / tot['pre']:.2f}** | "
        f"**{tot['budget']:,}** | **{tot['over']:,}** | {tot['sk']}/{tot['st']} | {tot['ek']}/{tot['et']} | {tot['rk']:,}/{tot['rt']:,} |"
    )
    out = ["# Edition step 1 — report", "", "Words are prose (paragraphs and list items, no esquema rows, no headings), «Lo que más cae» and «Normativa» included in Now.", "",
           *rows, "", "## Sentences kept by origin tag (rows apart)", "", *origin_rows, "", "## Overruns and why", "",
           *(reasons or ["None."])]
    (EDITION / "report.md").write_text("\n".join(out) + "\n")
    print("\n".join(out[:50]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
