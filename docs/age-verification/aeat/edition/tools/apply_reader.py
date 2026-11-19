"""apply_reader.py: reader flags → edition/restore/<lesson>.reader.json (the reserve sentences that solve them).

An id that is an esquema row restores its whole esquema. Flags without a restore id are listed in
edition/reader-unsolved.md for rewording and a blind check.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lesson_model import ROOT, parse  # noqa: E402

EDITION = ROOT / "docs/age-verification/aeat/edition"
POOL = ROOT / "docs/age-verification/aeat/pool"


def main() -> int:
    unsolved: list[str] = ["# Reader flags with no restore sentence", ""]
    total = solved = 0
    for path in sorted((EDITION / "reader").glob("m0*.json")):
        lesson = path.stem
        data = json.loads(path.read_text())
        model = parse((POOL / f"{lesson}.md").read_text())
        prose = {s.id for s in model.prose_sentences}
        row_to_esq = {s.id: i for i, e in enumerate(model.esquemas) for s in e.sentences}
        sentences: set[str] = set()
        esquemas: set[int] = set()
        for flag in data.get("flags", []):
            total += 1
            ids = flag.get("restore") or []
            found = False
            for i in ids:
                if i in prose:
                    sentences.add(i)
                    found = True
                elif i in row_to_esq:
                    esquemas.add(row_to_esq[i])
                    found = True
            if found:
                solved += 1
            else:
                unsolved.append(f"- {lesson}:{flag.get('line')} «{flag.get('starts')}» — {flag.get('problem')}")
        (EDITION / "restore" / f"{lesson}.reader.json").write_text(
            json.dumps({"sentences": sorted(sentences), "esquemas": sorted(esquemas)}, indent=1) + "\n"
        )
    (EDITION / "reader-unsolved.md").write_text("\n".join(unsolved) + "\n")
    print(f"flags {total}, solved by restore {solved}, unsolved {total - solved}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
