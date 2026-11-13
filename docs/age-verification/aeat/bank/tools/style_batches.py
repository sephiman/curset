"""Write the style-check input batches (≤ 60 candidates each) of the pooled derived questions.

Usage: `python3 style_batches.py [lesson …]` → `style/input/<lesson>.b<k>.md`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[1]
SIZE = 60

if __name__ == "__main__":
    out = BANK / "style" / "input"
    out.mkdir(parents=True, exist_ok=True)
    for pool in sorted(BANK.glob("m0?-l??.pool.json")):
        lesson = pool.name.split(".")[0]
        if sys.argv[1:] and lesson not in sys.argv[1:]:
            continue
        qs = json.loads(pool.read_text(encoding="utf-8"))
        for k, start in enumerate(range(0, len(qs), SIZE), start=1):
            lines = [f"# Style-check input — {lesson}, batch {k} ({len(qs[start:start + SIZE])} candidates)", ""]
            for q in qs[start:start + SIZE]:
                lines.append(f"## {q['id']}  (tema {q['tema']}; origin {q['origin']} {q['origin_id']})")
                lines.append(f"Stem: {q['prompt']}")
                for key in "abcd":
                    lines.append(f"- {key}) {'✓ ' if key == q['correct'] else ''}{q['options'][key]}")
                lines.append(f"Citation: {q['citation']}")
                lines.append(f"Explanation: {q['explanation']}")
                lines.append("")
            (out / f"{lesson}.b{k}.md").write_text("\n".join(lines), encoding="utf-8")
            print(f"{lesson}.b{k}: {len(qs[start:start + SIZE])}")
