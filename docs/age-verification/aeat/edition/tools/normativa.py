"""normativa.py: rebuild a lesson's «Normativa» lines from what the assembled lesson cites, exactly.

One line per norm of the pool's «Normativa» (its label kept) that the assembled text still cites in parentheses or
prose: «arts.» then the article units as cited (paragraph level, ranges as written), sorted. A pool line's non-article
tokens (disposiciones, preámbulo) stay when the assembled text names them. Derived text, not a verified sentence: it
goes to the blind check like any new line.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lesson_model import references_full  # noqa: E402

AMBIGUOUS = {"RD", "LO", "RDL", "RDLeg", "Ley", "Orden", "Real", "Decreto", "Reglamento", "Resolución"}
SUFFIX = ("bis", "ter", "quater")


def article_tokens(body: str) -> list[str]:
    """«29.1», «201 bis.3», «34–52», «8.Dos.4.º» as written, one per unit; «152.1 y 2» is 152.1 and 152.2."""
    raw = body.split()
    tokens = [t.rstrip(",;") for t in raw]
    out: list[str] = []
    glue = False  # after «,» or «y» following a dotted unit: a bare number or ordinal is a sibling of that unit
    i = 0
    while i < len(tokens):
        bare = tokens[i]
        nxt = tokens[i + 1] if i + 1 < len(tokens) else ""
        if re.match(r"^\d", bare):
            same_article = len({o.split(".")[0].split(" ")[0] for o in out}) == 1
            sibling = glue and out and "." in out[-1] and nxt.split(".")[0] not in SUFFIX
            if sibling and same_article and re.fullmatch(r"\d+", bare) and not raw[i - 1].endswith(","):
                out.append(out[-1].rsplit(".", 1)[0] + "." + bare)
            elif sibling and re.fullmatch(r"\d+\.[ºª]", bare) and re.search(r"\.\d+\.[ºª]$", out[-1]):
                out.append(out[-1].rsplit(".", 2)[0] + "." + bare)
            else:
                out.append(bare)
            glue = raw[i].endswith(",") and "." in bare
        elif out and bare.split(".")[0] in SUFFIX:
            out[-1] = f"{out[-1]} {bare}"
        elif bare in ("y", "and") and out and "." in out[-1]:
            glue = True
        elif bare != "y":
            glue = False
        i += 1
    return out


def cited(text: str) -> list[tuple[str, str, list[str]]]:
    """(norm token, 24 characters after it, article tokens) for each reference in the text."""
    return [(norm, tail, article_tokens(body)) for body, norm, tail in references_full(text)]


def _matches(label: str, norm: str, tail: str) -> bool:
    if norm in AMBIGUOUS:
        number = re.search(r"\d+/\d+|\d+", tail)
        return bool(number) and f"{norm} {number.group(0)}" in label
    return bool(re.search(rf"(?<![\w]){re.escape(norm)}(?![\w])", label))


def _sort_key(token: str) -> tuple[int, str]:
    m = re.match(r"\d+", token)
    return (int(m.group(0)) if m else 0, token)


def _other_tokens(old_rest: str, body: str) -> list[str]:
    """Pool tokens that are not article numbers (disposiciones, preámbulo) and that the text still names."""
    kept = []
    for clause in old_rest.split(";"):
        if "nombrad" in clause:
            continue
        for token in re.split(r",\s+|\s+y\s+(?=disposici|preámbulo)", clause.split(":")[-1].strip().rstrip(".")):
            token = re.sub(r"^arts?\.\s+", "", token).strip()
            if token and not re.match(r"^\d", token) and re.match(r"(disposici|preámbulo)", token):
                if token[:28] in body:
                    kept.append(token)
    return kept


def rebuild_line(line: str, body: str, body_cites: list[tuple[str, str, list[str]]]) -> str | None:
    label, _, rest = line[2:].partition(":")
    tokens: set[str] = set()
    for norm, tail, found in body_cites:
        if _matches(label, norm, tail):
            tokens.update(found)
    pieces = sorted(tokens, key=_sort_key) + _other_tokens(rest, body)
    if not pieces:
        return None
    word = "art." if len(pieces) == 1 and re.match(r"^\d", pieces[0]) and not re.search(r"[\N{EN DASH}-]", pieces[0]) else "arts."
    listing = pieces[0] if len(pieces) == 1 else ", ".join(pieces[:-1]) + f" y {pieces[-1]}"
    text = f"- {label}: {word} {listing}" if re.match(r"^\d", pieces[0]) else f"- {label}: {listing}"
    # «art. 89.» would read as a list marker: a line that ends in a bare article number takes no final period
    return text if re.search(r"\sart\. \d+$", text) else text + "."


def derive(body_text: str, pool_lines: list[str]) -> list[str]:
    body_cites = cited(body_text)
    out = []
    for line in pool_lines:
        if not line.startswith("- "):
            continue
        new = rebuild_line(line, body_text, body_cites)
        if new:
            out.append(new)
    return out
