"""Pair every tipo B question with its tipo A question and check that both keys name the same option text."""

import json
import re
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PARSED = ROOT / "docs/age-verification/aeat/r0a/parsed"
OUT = ROOT / "docs/age-verification/aeat/r0a/checks/pairing.json"


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return re.sub(r"[^\w]+", " ", text).strip()


def keyed_text(q: dict[str, str]) -> str:
    return norm(q[q["key"]]) if q["key"] in "ABCD" else "ANULADA"


def main() -> None:
    report: dict[str, object] = {}
    for conv in ("conv2020", "conv2021", "conv2022", "conv2023", "conv2024", "conv2025"):
        a = json.loads((PARSED / f"{conv}_A.json").read_text())
        b = json.loads((PARSED / f"{conv}_B.json").read_text())
        pairs, disagreements, weak = [], [], []
        for qb in b:
            best = max(a, key=lambda qa: SequenceMatcher(None, norm(qa["stem"]), norm(qb["stem"])).ratio())
            ratio = SequenceMatcher(None, norm(best["stem"]), norm(qb["stem"])).ratio()
            options_same = sorted(norm(best[k]) for k in "ABCD") == sorted(norm(qb[k]) for k in "ABCD")
            pairs.append({"B": qb["n"], "A": best["n"], "stem_ratio": round(ratio, 3), "options_same": options_same})
            if ratio < 0.95 or not options_same:
                weak.append(pairs[-1])
            if keyed_text(best) != keyed_text(qb):
                disagreements.append({"B": qb["n"], "A": best["n"], "keyA": best["key"], "keyB": qb["key"]})
        a_hits = sorted(p["A"] for p in pairs)
        report[conv] = {
            "pairs": pairs,
            "bijective": a_hits == list(range(1, len(a) + 1)),
            "weak": weak,
            "key_disagreements": disagreements,
        }
        print(conv, "bijective", report[conv]["bijective"], "weak", len(weak), "key disagreements", disagreements)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
