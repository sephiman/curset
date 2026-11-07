"""Writer's hand-back checks on a C2 draft: anchors in its C2 lesson, the mechanical C2 style items, the mix.

Run from backend/: `uv run python ../docs/age-verification/c2/bank/tools/check_draft.py <draft.json> …`.
Also run the C1 lint on it: `python3 docs/age-verification/bank/tools/lint_drafts.py ../c2/bank/<bloque> <stem>`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from c2_stats import report  # noqa: E402
from derive_candidates import C2, citations_of  # noqa: E402
from mechanical_style import failures  # noqa: E402

if __name__ == "__main__":
    cc, _ = citations_of(C2)
    questions: list[dict[str, object]] = []
    for name in sys.argv[1:]:
        questions += json.loads(Path(name).read_text(encoding="utf-8"))
    misses = 0
    for q in questions:
        lesson = str(q["id"]).rsplit("-q", 1)[0]
        if cc.question_link(lesson, str(q["citation"]), "es").anchor is None:
            misses += 1
            print(f"ANCHOR MISS {q['id']}: «{q['citation']}»")
        for item, detail in failures(q):
            print(f"STYLE {item} {q['id']}: {detail}")
        options = q["options"]
        assert isinstance(options, dict) and sorted(options) == ["a", "b", "c", "d"], q["id"]
        assert q["correct"] in options, q["id"]
    print(f"{len(questions)} questions, {misses} anchor misses")
    print("\n".join(report(questions)))
