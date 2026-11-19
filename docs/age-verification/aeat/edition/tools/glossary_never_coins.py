"""glossary_never_coins.py: move to the waiting list every entry the backend says appears in no lesson's prose (loop to a fixed point)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
COURSE = ROOT / "content/aeat-agentes-hacienda"
WAITING = ROOT / "docs/age-verification/aeat/edition/glossary-waiting.md"


def offenders() -> list[str]:
    from tradeschool.content.registry import load_registry

    try:
        load_registry(COURSE, check_excerpts=False)
    except Exception as exc:  # noqa: BLE001
        text = str(exc)
        if "never appear" not in text:
            raise
        return re.findall(r"(g-[\w-]+) \(es:", text)
    return []


def main() -> int:
    while ids := offenders():
        path = COURSE / "glossary.yaml"
        lines = path.read_text().split("\n")
        starts = [i for i, l in enumerate(lines) if l.startswith("- id: ")]
        spans = {lines[s].split(": ", 1)[1].strip(): (s, starts[k + 1] if k + 1 < len(starts) else len(lines))
                 for k, s in enumerate(starts)}
        log = WAITING.read_text() if WAITING.exists() else "# Glossary entries waiting (edition step 1)\n"
        drop: set[int] = set()
        for eid in ids:
            a, b = spans[eid]
            log += f"\n## {eid} (appears in no lesson's prose)\n\n```yaml\n" + "\n".join(lines[a:b]) + "\n```\n"
            drop.update(range(a, b))
        path.write_text("\n".join(l for i, l in enumerate(lines) if i not in drop))
        WAITING.write_text(log)
        print("moved", ids)
    print("glossary validates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
