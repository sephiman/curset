"""Per-tema mix of AEAT questions against the 2025 first exercise: stem forms, article naming, key-longest, negatives.

Usage: `python3 aeat_stats.py <json> [<json> …]` (derived, draft or kept files; each a list of questions).
Stem forms are the style guide's categories (§ 2); a question's own `stem_form` field wins when a writer set it.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ARTICLE = re.compile(r"\bart[íi]culos?\b|\bart\.\s*\d|\bdisposici[óo]n (adicional|transitoria|final)", re.I)
NEGATIVE = re.compile(r"\b(NO|INCORRECTA|FALSA)\b")
DATED = re.compile(r"\b\d{1,2} de [a-zé]+ de (19|20)\d\d\b|\b\d[\d.]*(,\d+)? euros\b")
SENIOR = re.compile(r"^(Señale|Marque|Indique)\b|\bseñale la (respuesta|afirmación|opción)|\bindique cuál\b", re.I)

# 2025 shares (%), style guide § 2.
TARGET = {"art-completar": 39, "señale": 23, "directa": 11, "supuesto": 10, "art-pregunta": 9, "cual": 9, "otra": 0}
FORMS = tuple(TARGET)
ARTICLE_SHARE = 91


def stem_form(prompt: str) -> str:
    text = prompt.strip()
    words = len(text.split())
    if DATED.search(text) and words >= 45 and text.endswith("?") and not ARTICLE.search(text.split("¿")[-1]):
        return "supuesto"
    if SENIOR.search(text):
        return "señale"
    if re.search(r"¿\s*(Cuál|Cuáles|Qué) de (las|los|estas|estos) (siguientes|opciones)", text, re.I):
        return "cual"
    question = text.endswith("?")
    if ARTICLE.search(text):
        return "art-pregunta" if question else "art-completar"
    return "directa" if question else "otra"


def form_of(q: dict[str, object]) -> str:
    return str(q.get("stem_form") or stem_form(str(q["prompt"])))


def longest_is_key(q: dict[str, object]) -> bool:
    options = q["options"]
    assert isinstance(options, dict)
    lengths = {k: len(str(v)) for k, v in options.items()}
    top = max(lengths.values())
    return lengths[str(q["correct"])] == top and list(lengths.values()).count(top) == 1


def report(questions: list[dict[str, object]]) -> list[str]:
    by_tema: dict[str, list[dict[str, object]]] = {}
    for q in questions:
        by_tema.setdefault(str(q["tema"]), []).append(q)
    out = []
    for tema in sorted(by_tema, key=lambda t: (len(t.split(".")[0]), int(t.split(".")[1]))):
        qs = by_tema[tema]
        forms = Counter(form_of(q) for q in qs)
        n = len(qs)
        mix, off = [], []
        for form, target in TARGET.items():
            share = round(100 * forms.get(form, 0) / n)
            mix.append(f"{form} {share}/{target}")
            if abs(share - target) > 10:
                off.append(form)
        articles = round(100 * sum(1 for q in qs if ARTICLE.search(str(q["prompt"]))) / n)
        longest = round(100 * sum(1 for q in qs if longest_is_key(q)) / n)
        negatives = sum(1 for q in qs if NEGATIVE.search(str(q["prompt"])))
        out.append(
            f"{tema}: n={n} · " + ", ".join(mix) + f" · article {articles}/{ARTICLE_SHARE} · key longest "
            f"{longest} % · negatives {negatives}" + (f" · OFF ±10: {', '.join(off)}" if off else "")
        )
    return out


if __name__ == "__main__":
    loaded: list[dict[str, object]] = []
    for name in sys.argv[1:]:
        loaded += json.loads(Path(name).read_text(encoding="utf-8"))
    print("\n".join(report(loaded)))
