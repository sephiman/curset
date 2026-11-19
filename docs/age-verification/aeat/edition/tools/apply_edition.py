"""apply_edition.py: FAIL rows of the blind verifier reports (r2d/<lesson>/verify-edition*.md) → edition/patches.json.

old = the pending sentence's text (current lesson), new = the verifier's replacement (empty = drop the sentence).
finalize.py applies the patches after assembly, so a rebuild does not lose them. Rows already patched are skipped.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lesson_model import ROOT, parse  # noqa: E402

AEAT = ROOT / "docs/age-verification/aeat"
EDITION = AEAT / "edition"
CONTENT = ROOT / "content/aeat-agentes-hacienda/es/lessons"
ROW = re.compile(r"^\|\s*`(?P<id>[0-9a-f]{10})`\s*\|\s*(?P<verdict>PASS|FAIL)\s*\|(?P<rest>.*)\|\s*$")


def main(argv: list[str]) -> int:
    report_name = argv[0] if argv else "verify-edition.md"
    path = EDITION / "patches.json"
    patches: dict[str, list[dict[str, str]]] = json.loads(path.read_text()) if path.exists() else {}
    added = failed_without = 0
    for report in sorted(AEAT.glob(f"r2d/m0*/{report_name}")):
        lesson = report.parent.name
        text = (CONTENT / f"{lesson}.md").read_text()
        by_id = {s.id: s.text for s in parse(text).prose_sentences} | {
            s.id: s.text for e in parse(text).esquemas for s in e.sentences
        }
        # Normativa lines are bullets: their sentence ids come from provenance.sentences on the whole file
        from scripts.provenance import sentences  # noqa: E402

        by_id |= {s.id: s.text for s in sentences(text)}
        for line in report.read_text().splitlines():
            m = ROW.match(line)
            if not m or m["verdict"] != "FAIL":
                continue
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", m["rest"])]
            replacement = cells[-1].strip().strip("`") if cells else ""
            old = by_id.get(m["id"])
            if old is None:
                continue
            if replacement.lower() in ("", "—", "-", "drop", "(drop)", "drop the sentence"):
                replacement = ""
            replacement = re.sub(r"^- ", "", replacement) if not old.startswith("|") else replacement
            if any(p["old"] == old for p in patches.get(lesson, [])):
                continue
            if replacement == old:
                continue
            patches.setdefault(lesson, []).append({"old": old, "new": replacement})
            added += 1
    path.write_text(json.dumps(patches, ensure_ascii=False, indent=1) + "\n")
    print(f"patches added {added}; total {sum(len(v) for v in patches.values())}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
