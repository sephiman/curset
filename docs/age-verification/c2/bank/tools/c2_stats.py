"""Per-tema mix of C2 questions against the 2025 exam: stem forms, article naming, key-longest, negatives.

Usage: `python3 c2_stats.py <json> [<json> …]` (derived, draft or kept files; a list of questions each).
Stem forms are the style guide's categories (§ Statistics), classified from the stem text alone.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

NORM = re.compile(
    r"\b(Constituci[óo]n|Ley|Real Decreto|Reglamento|Orden [A-Z]+/|Directiva|Tratado|Decreto|Resoluci[óo]n|Carta)\b"
)
ARTICLE = re.compile(r"\bart[íi]culos?\b|\bart\.\s*\d|\bdisposici[óo]n (adicional|transitoria|final)", re.I)
NEGATIVE = re.compile(r"\b(NO|INCORRECTA|FALSA)\b")

# 2025 shares (%) per set, style guide § Statistics.
TARGET = {
    "I": {"art-completar": 41, "norma-completar": 6, "cual": 22, "art-pregunta": 6, "señale": 12,
          "norma-pregunta": 6, "enunciado": 3, "directa": 3},
    "II.1-4": {"norma-completar": 58, "señale": 0, "norma-pregunta": 0, "directa": 33, "art-completar": 8,
               "art-pregunta": 0, "cual": 0, "enunciado": 0},
    "ofimatica": {"cual": 37, "directa": 56, "enunciado": 2, "señale": 5},
}
ARTICLE_SHARE = {"I": 69, "II.1-4": 8, "ofimatica": 0}  # 2025: 22/32, 1/12, 0/43


def set_of(tema: str) -> str:
    if tema.startswith("I."):
        return "I"
    return "II.1-4" if int(tema.split(".")[1]) <= 4 else "ofimatica"


def stem_form(prompt: str, kind: str) -> str:
    text = prompt.strip()
    if re.match(r"^(Señale|Marque|Indique)\b", text):
        return "señale"
    if re.search(r"¿\s*(Cuál|Cuáles|Qué) de (las|los|estas|estos) (siguientes|opciones)", text) or re.search(
        r"¿\s*[Cc]uál de las siguientes", text
    ):
        return "cual"
    question = text.endswith("?")
    if kind != "ofimatica":
        if ARTICLE.search(text):
            return "art-pregunta" if question else "art-completar"
        if NORM.search(text):
            return "norma-pregunta" if question else "norma-completar"
    return "directa" if question else "enunciado"


def longest_is_key(q: dict[str, object]) -> bool:
    options = q["options"]
    assert isinstance(options, dict)
    lengths = {k: len(str(v)) for k, v in options.items()}
    return lengths[str(q["correct"])] == max(lengths.values()) and list(lengths.values()).count(max(lengths.values())) == 1


def report(questions: list[dict[str, object]]) -> list[str]:
    by_tema: dict[str, list[dict[str, object]]] = {}
    for q in questions:
        by_tema.setdefault(str(q["tema"]), []).append(q)
    out = []
    for tema in sorted(by_tema, key=lambda t: (len(t.split(".")[0]), int(t.split(".")[1]))):
        qs = by_tema[tema]
        kind = set_of(tema)
        forms = Counter(stem_form(str(q["prompt"]), kind) for q in qs)
        n = len(qs)
        mix = []
        off = []
        for form, target in TARGET[kind].items():
            share = round(100 * forms.get(form, 0) / n)
            mix.append(f"{form} {share}/{target}")
            if abs(share - target) > 10:
                off.append(form)
        articles = round(100 * sum(1 for q in qs if ARTICLE.search(str(q["prompt"]))) / n)
        longest = round(100 * sum(1 for q in qs if longest_is_key(q)) / n)
        negatives = sum(1 for q in qs if NEGATIVE.search(str(q["prompt"])))
        out.append(
            f"{tema}: n={n} · " + ", ".join(mix) + f" · article {articles}/{ARTICLE_SHARE[kind]} · key longest "
            f"{longest} % · negatives {negatives}" + (f" · OFF ±10: {', '.join(off)}" if off else "")
        )
    return out


if __name__ == "__main__":
    loaded: list[dict[str, object]] = []
    for name in sys.argv[1:]:
        loaded += json.loads(Path(name).read_text(encoding="utf-8"))
    print("\n".join(report(loaded)))
