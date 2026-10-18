# SPDX-License-Identifier: AGPL-3.0-only
"""The norms a course cites, from its `sources/normativa.yaml`, and how a written norm name resolves.

A lesson writes a norm many ways («LPAC», «Ley 39/2015», «Ley 39/2015, de 1 de octubre, del…»). Each
entry answers to: its `short` name, the head and the parenthesis of that name («Ley 39/2015 (LPAC)»),
the long and short number forms («Ley Orgánica 2/1979» = «LO 2/1979»), its title, any `aliases` the
entry lists, and the abbreviations the lessons themselves declare in prose («…Públicas (LPAC)»).

Every norm has one anchor slug, from its official id so two norms never share one: `boe-a-2015-10565`,
or `celex-12016m-txt` for an EU norm. An entry with neither falls back to the acronym in its short name
(`ce`), else its number form (`lo-3-1981`), else its short name (`codigo-civil`).
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

import yaml

from tradeschool.citations.grammar import LEAD, collapse, slug

_LONG_TO_SHORT = {
    "Ley Orgánica": "LO",
    "Real Decreto Legislativo": "RDL",
    "Real Decreto-ley": "RDL",
    "Real Decreto": "RD",
}
_SHORT_TO_LONG = {
    "LO": ["Ley Orgánica"],
    "RD": ["Real Decreto"],
    "RDL": ["Real Decreto Legislativo", "Real Decreto-ley"],
}
NUMBER_FORM = re.compile(
    r"\b(?P<kind>Ley Orgánica|Real Decreto Legislativo|Real Decreto-ley|Real Decreto|Decreto|Ley|LO|RDL|RD)"
    r" (?P<number>\d+/\d{4})\b|\bOrden [A-Z]+/\d+/\d{4}\b"
)
_ACRONYM = re.compile(r"^[A-ZÁÉÍÓÚ]{2,}$")
_SHORT_PARTS = re.compile(r"^(?P<head>.*?)\s*\((?P<paren>.*)\)\s*$")
# An abbreviation a lesson declares right after a norm's number form: «Ley 39/2015, de …, del … (LPAC)».
_DECLARED = re.compile(
    rf"(?P<form>{NUMBER_FORM.pattern})[^()\n]{{0,300}}?\((?P<abbr>[A-ZÁÉÍÓÚ][A-ZÁÉÍÓÚ0-9]+)\)"
)


def normalize(name: str) -> str:
    return collapse(name).rstrip(".").casefold()


def number_forms(text: str) -> set[str]:
    """Every spelling of each number form in `text`: «LO 2/1979» gives itself and «Ley Orgánica 2/1979»."""
    forms: set[str] = set()
    for match in NUMBER_FORM.finditer(text):
        if match["kind"] is None:
            forms.add(match[0])
            continue
        kind, number = match["kind"], match["number"]
        forms.add(f"{kind} {number}")
        if kind in _LONG_TO_SHORT:
            forms.add(f"{_LONG_TO_SHORT[kind]} {number}")
        for long_kind in _SHORT_TO_LONG.get(kind, []):
            forms.add(f"{long_kind} {number}")
    return forms


@dataclass(frozen=True)
class Norm:
    slug: str
    short: str
    title: str
    #: Course-relative path of its consolidated text (`sources/normativa/…`), if the course keeps one.
    file: str | None
    consolidated_as_of: str | None
    aliases: frozenset[str]


def _short_parts(short: str) -> tuple[str, str | None]:
    match = _SHORT_PARTS.match(short)
    return (match["head"], match["paren"]) if match else (short, None)


def norm_slug(entry: dict[str, object]) -> str:
    if entry.get("boe_id"):
        return slug(str(entry["boe_id"]))
    if entry.get("celex"):
        return f"celex-{slug(str(entry['celex']))}"
    return _name_slug(str(entry["short"]))


def _name_slug(short: str) -> str:
    head, paren = _short_parts(short)
    for candidate in (paren, head):
        if candidate and _ACRONYM.match(candidate):
            return slug(candidate)
    for candidate in (head, paren):
        if candidate and NUMBER_FORM.fullmatch(candidate):
            forms = sorted(number_forms(candidate), key=len)
            return slug(forms[0])
    return slug(head)


_MONTHS = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
]
_LONG_DATE = re.compile(rf"\b(\d{{1,2}}) de ({'|'.join(_MONTHS)}) de (\d{{4}})\b")
_TITLE_HEAD = re.compile(r",| por (?:la|el) que | sobre ")


def _date_forms(name: str) -> set[str]:
    """«Orden de 30 de julio de 1992» also as «Orden de 30-7-1992» and «Orden de 30-07-1992»."""
    forms: set[str] = set()
    for match in _LONG_DATE.finditer(name):
        day, month, year = int(match[1]), _MONTHS.index(match[2]) + 1, match[3]
        for numeric in (f"{day}-{month}-{year}", f"{day:02d}-{month:02d}-{year}"):
            forms.add(name[: match.start()] + numeric + name[match.end() :])
    return forms


def _declared_aliases(entry: dict[str, object]) -> set[str]:
    """What the entry itself says it is called: its short name, its parenthesis and `aliases`."""
    short = str(entry["short"])
    head, paren = _short_parts(short)
    listed = entry.get("aliases")
    names = {short, head, *(str(a) for a in listed if a)} if isinstance(listed, list) else {short, head}
    if paren:
        names.add(paren)
    return {normalize(name) for name in names | number_forms(short)}


def _derived_aliases(entry: dict[str, object]) -> set[str]:
    """Names worked out from the title: whole, its dated head, the number and date spellings."""
    title = str(entry.get("title") or "").rstrip(".")
    head = _TITLE_HEAD.split(title, maxsplit=1)[0].strip()
    names = {title, head} | number_forms(title[:80])
    for name in [*names, str(entry["short"])]:
        names |= _date_forms(name)
    return {normalize(name) for name in names if name}


@dataclass
class NormIndex:
    norms: list[Norm]
    _by_alias: dict[str, Norm]

    @classmethod
    def load(cls, path: Path, prose: Iterable[str]) -> NormIndex:
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        if not isinstance(raw, list):
            raise ValueError(f"{path} must be a list of norms")
        norms: list[Norm] = []
        declared: dict[str, Norm] = {}
        derived: dict[str, set[str]] = {}
        by_slug: dict[str, Norm] = {}
        for entry in raw:
            if not isinstance(entry, dict) or "short" not in entry:
                raise ValueError(f"{path}: every norm needs a `short` name")
            own = _declared_aliases(entry)
            norm = Norm(
                slug=norm_slug(entry),
                short=str(entry["short"]),
                title=str(entry.get("title") or entry["short"]).rstrip().rstrip("."),
                file=str(entry["file"]) if entry.get("file") else None,
                consolidated_as_of=str(entry["consolidated_as_of"])
                if entry.get("consolidated_as_of")
                else None,
                aliases=frozenset(own | _derived_aliases(entry)),
            )
            norms.append(norm)
            by_slug.setdefault(norm.slug, norm)
            for alias in own:
                declared.setdefault(alias, norm)
            for alias in _derived_aliases(entry):
                derived.setdefault(alias, set()).add(norm.slug)
        # A derived name two norms share («Orden de 1 de febrero de 1996») names neither.
        by_alias = {alias: by_slug[next(iter(slugs))] for alias, slugs in derived.items() if len(slugs) == 1}
        by_alias.update(declared)
        index = cls(norms, by_alias)
        index._declare(prose)
        return index

    def _declare(self, prose: Iterable[str]) -> None:
        """Abbreviations the lessons declare after a norm's number form become aliases of that norm."""
        for text in prose:
            for match in _DECLARED.finditer(text):
                if LEAD.match(match["abbr"]):
                    continue
                norm = self._exact(match["form"])
                if norm is not None:
                    self._by_alias.setdefault(normalize(match["abbr"]), norm)

    def _exact(self, name: str) -> Norm | None:
        return self._by_alias.get(normalize(name))

    def resolve(self, written: str) -> Norm | None:
        """The norm a written name means: whole, then cut back at commas and parentheses, then by its
        number form, then by the one norm whose short name contains it. None when nothing answers."""
        text = collapse(written)
        candidates = [text]
        for cut in (", ", " ("):
            candidates += [text[:at] for at in _positions(text, cut)]
        for candidate in candidates:
            if (norm := self._exact(candidate)) is not None:
                return norm
        for form in number_forms(text):
            if (norm := self._exact(form)) is not None:
                return norm
        needle = normalize(text.split(",")[0])
        if len(needle) >= 6:
            containing = {n.slug: n for n in self.norms if needle in normalize(n.short)}
            if len(containing) == 1:
                return next(iter(containing.values()))
        return None


def _positions(text: str, cut: str) -> list[int]:
    """Where `cut` occurs, last first, so the longest prefix is tried before shorter ones."""
    return sorted((m.start() for m in re.finditer(re.escape(cut), text)), reverse=True)
