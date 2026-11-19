"""finalize_layer.py <lesson…>: drop every case/purpose that is cut or still FAIL after its recheck, then re-apply the layer and the terms.

Cut set = explanation/<lesson>/cut-keys.txt ∪ keys whose latest layer-verifier verdict is FAIL. They go to dropped.txt (apply skips them).
An overview whose latest verdict is FAIL is reported (it cannot be dropped).
"""

from __future__ import annotations

import subprocess
import sys

from explanation import LAYER
from fails import latest
from layer import parse


def finalize(lesson: str) -> tuple[list[str], list[str]]:
    verdicts = latest(lesson, "layer-verifier-*.md")
    keys = {p.key for p in parse(lesson)[0]}
    cut_path = LAYER / lesson / "cut-keys.txt"
    cuts = {k for k in (cut_path.read_text(encoding="utf-8").split("\n") if cut_path.exists() else []) if k in keys}
    cuts |= {k for k, (v, _r) in verdicts.items() if v == "FAIL" and k in keys}
    dropped_path = LAYER / lesson / "dropped.txt"
    have = set(dropped_path.read_text(encoding="utf-8").split("\n")) if dropped_path.exists() else set()
    dropped_path.write_text("\n".join(sorted(have | cuts)).strip("\n") + "\n", encoding="utf-8")
    overview = latest(lesson, "verifier-*.md").get("overview")
    bad = ["overview"] if overview and overview[0] == "FAIL" else []
    return sorted(cuts), bad


if __name__ == "__main__":
    base = ["uv", "run", "--project", "backend", "python", "docs/age-verification/aeat/edition/tools"]
    for name in sys.argv[1:]:
        cuts, bad = finalize(name)
        for command in ("strip", "apply", "apply-terms"):
            subprocess.run([*base[:-1], base[-1] + "/layer.py", command, name], check=True, stdout=subprocess.DEVNULL)
        print(f"{name}: cut {len(cuts)}" + (f", OVERVIEW STILL FAIL" if bad else ""))
