# SPDX-License-Identifier: AGPL-3.0-only
"""Read the saved DLE pages of the psicotécnico word banks into `psicotecnico/dle_relations.json`.

Run from backend/ after saving or replacing a page under `content/age-auxiliar-c2/sources/otros/dle/`:
`uv run python scripts/dle_relations.py` (`--check` fails when the JSON is stale). Per page: whether the
DLE has the word, the lemmas shown, and each main sense (complex forms left out) with its number, text,
category (the abbreviation's title) and «Sinónimos y afines» / «Antónimos y opuestos» lists, every gendered
head split («heterodoxo, heterodoxa»).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PAGES = REPO / "content" / "age-auxiliar-c2" / "sources" / "otros" / "dle"
OUT = REPO / "backend" / "src" / "tradeschool" / "psicotecnico" / "dle_relations.json"
_VOID = {"br", "img", "meta", "link", "input", "hr", "wbr", "source"}


class _Sense:
    def __init__(self, form: str | None) -> None:
        self.n, self.text, self.form, self.category = "", "", form, ""
        self.syn: list[str] = []
        self.ant: list[str] = []


class _Article:
    def __init__(self) -> None:
        self.lemma = ""
        self.senses: list[_Sense] = []


class DlePage(HTMLParser):
    """The articles of one DLE page; senses under an `h3.k*` heading belong to a complex form."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.articles: list[_Article] = []
        self._stack: list[str] = []
        self._capture: tuple[str, int] | None = None  # (field, depth) of the open n_acep/definition span
        self._list: tuple[str, int] | None = None  # (syn|ant, depth) of the open word list
        self._anchor: str | None = None
        self._form: str | None = None
        self._in_title = self._in_form = False
        self._sense: _Sense | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in _VOID:
            return
        attributes = dict(attrs)
        cls = attributes.get("class") or ""
        self._stack.append(tag)
        depth = len(self._stack)
        if tag == "article":
            self.articles.append(_Article())
            self._form = None
        elif not self.articles:
            return
        elif tag == "h1" and "c-page-header__title" in cls:
            self._in_title = True
        elif tag == "h3" and re.fullmatch(r"k\d*", cls.strip()):
            self._form, self._in_form = "", True
        elif tag == "div" and cls.strip() == "c-definitions__item":
            self._sense = _Sense(self._form)
            self.articles[-1].senses.append(self._sense)
        elif self._sense is None:
            return
        elif tag == "abbr" and not self._sense.category and not self._sense.text and self._list is None:
            self._sense.category = attributes.get("title") or ""
        elif tag == "span" and "n_acep" in cls:
            self._capture = ("n", depth)
        elif tag == "span" and "dle24-definition" in cls:
            self._capture = ("text", depth)
        elif tag == "div" and "c-word-list--sinonimos" in cls:
            self._list = ("syn", depth)
        elif tag == "div" and "c-word-list--antonimos" in cls:
            self._list = ("ant", depth)
        elif tag == "a" and self._list is not None:
            self._anchor = ""

    def handle_endtag(self, tag: str) -> None:
        while self._stack:
            closed = self._stack.pop()
            depth = len(self._stack) + 1
            if self._capture and self._capture[1] == depth:
                self._capture = None
            if self._list and self._list[1] == depth:
                self._list = None
            if closed == "h1":
                self._in_title = False
            if closed == "h3":
                self._in_form = False
            if closed == "a" and self._anchor is not None and self._list and self._sense:
                target = self._sense.syn if self._list[0] == "syn" else self._sense.ant
                target.extend(head.strip() for head in self._anchor.split(","))
                self._anchor = None
            if closed == tag:
                return

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.articles[-1].lemma += data
        if self._in_form and self._form is not None:
            self._form += data
        if self._anchor is not None:
            self._anchor += data
        elif self._capture and self._sense is not None:
            field = self._capture[0]
            setattr(self._sense, field, getattr(self._sense, field) + data)


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def read_page(path: Path) -> dict[str, object]:
    html = path.read_text(encoding="utf-8")
    parser = DlePage()
    parser.feed(re.sub(r"<svg\b.*?</svg>", "", html, flags=re.S))
    senses = [
        {"n": _clean(s.n), "category": s.category, "text": _clean(s.text), "syn": s.syn, "ant": s.ant}
        for article in parser.articles
        for s in article.senses
        if s.form is None and _clean(s.text)
    ]
    return {
        "file": f"dle/{path.name}",
        "absent": "no está en el <i>Diccionario</i>" in html,
        "lemmas": [_clean(a.lemma) for a in parser.articles if _clean(a.lemma)],
        "senses": senses,
    }


def build() -> str:
    pages = {path.stem: read_page(path) for path in sorted(PAGES.glob("*.html"))}
    return json.dumps({"consultado": "2026-11-07", "pages": pages}, ensure_ascii=False, indent=1) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true")
    document = build()
    if parser.parse_args().check:
        stale = not OUT.exists() or OUT.read_text(encoding="utf-8") != document
        print(f"stale: {OUT}" if stale else "dle_relations.json up to date")
        return 1 if stale else 0
    OUT.write_text(document, encoding="utf-8")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
