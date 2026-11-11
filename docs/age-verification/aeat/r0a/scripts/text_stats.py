"""Text statistics of the first-exercise questions per exam: lengths, key balance, longest-option-is-key rate."""

import json
import statistics
from collections import Counter
from pathlib import Path

R0A = Path(__file__).resolve().parents[1]


def words(text: str) -> int:
    return len(text.split())


def main() -> None:
    master = json.loads((R0A / "parsed/master.json").read_text())
    out: dict[str, dict[str, object]] = {}
    for exam in sorted({q["exam"] for q in master}):
        qs = [q for q in master if q["exam"] == exam]
        keyed = [q for q in qs if q["key"] in "ABCD"]
        stem = [words(q["stem"]) for q in qs]
        opts = [words(v) for q in qs for v in q["opts"].values()]
        longest_is_key = sum(
            1 for q in keyed
            if words(q["opts"][q["key"].lower()]) == max(words(v) for v in q["opts"].values())
        )
        out[exam] = {
            "questions": len(qs),
            "anuladas": len(qs) - len(keyed),
            "stem_words_median": statistics.median(stem),
            "stem_words_max": max(stem),
            "option_words_median": statistics.median(opts),
            "option_words_max": max(opts),
            "key_distribution": dict(sorted(Counter(q["key"] for q in keyed).items())),
            "longest_option_is_key": f"{longest_is_key}/{len(keyed)}",
            "cites_article_in_stem": sum(1 for q in qs if "artículo" in q["stem"].lower() or "art." in q["stem"].lower()),
            "negative_marker_upper": sum(
                1 for q in qs if any(w in q["stem"] for w in ("NO ", "INCORRECTA", "FALSA", "EXCEPTO", "CORRECTA"))
            ),
        }
    (R0A / "checks/textstats.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for exam, row in out.items():
        print(exam, row)


if __name__ == "__main__":
    main()
