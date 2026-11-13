"""Writer's hand-back checks on an AEAT draft: anchors in its lesson, mechanical style, RDL 29/2026 hold, official copies, mix.

Run from backend/: `uv run python ../docs/age-verification/aeat/bank/tools/check_draft.py <draft.json> …`.
«OFFICIAL SIMILAR» lists a question whose stem + options are ≥ 0.80 similar to one of the 680 official questions.
"""

from __future__ import annotations

import difflib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aeat_stats import report  # noqa: E402
from mechanical_style import failures  # noqa: E402
from rdl_held import held_reason  # noqa: E402

ROOT = Path(__file__).resolve().parents[5]
PARSED = ROOT / "docs" / "age-verification" / "aeat" / "r0a" / "parsed"
THRESHOLD = 0.80


def official() -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for path in sorted(PARSED.glob("conv*_A.json")) + sorted(PARSED.glob("conv2022_X.json")):
        for q in json.loads(path.read_text(encoding="utf-8")):
            out.append((f"{path.stem}-{q['n']}", " ".join([q["stem"], *(q.get(k, "") for k in "ABCD")])))
    return out


def main(names: list[str]) -> None:
    from derive_candidates import AEAT, c2d  # noqa: PLC0415  (imports tradeschool: needs backend/)

    cc, _ = c2d.citations_of(AEAT)
    exams = official()
    questions: list[dict[str, object]] = []
    for name in names:
        questions += json.loads(Path(name).read_text(encoding="utf-8"))
    misses = 0
    for q in questions:
        lesson = str(q["id"]).rsplit("-q", 1)[0]
        if cc.question_link(lesson, str(q["citation"]), "es").anchor is None:
            misses += 1
            print(f"ANCHOR MISS {q['id']}: «{q['citation']}»")
        for item, detail in failures(q):
            print(f"STYLE {item} {q['id']}: {detail}")
        if reason := held_reason(str(q["citation"])):
            print(f"HELD RDL 29/2026 {q['id']}: {reason}")
        options = q["options"]
        assert isinstance(options, dict) and sorted(options) == ["a", "b", "c", "d"], q["id"]
        assert q["correct"] in options, q["id"]
        text = " ".join([str(q["prompt"]), *(str(options[k]) for k in "abcd")])
        for exam_id, exam_text in exams:
            if difflib.SequenceMatcher(None, text, exam_text, autojunk=False).quick_ratio() >= THRESHOLD and (
                difflib.SequenceMatcher(None, text, exam_text, autojunk=False).ratio() >= THRESHOLD
            ):
                print(f"OFFICIAL SIMILAR {q['id']} ~ {exam_id}")
    print(f"{len(questions)} questions, {misses} anchor misses")
    print("\n".join(report(questions)))


if __name__ == "__main__":
    main(sys.argv[1:])
