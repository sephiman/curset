"""Mechanical checks of a case draft. Usage (from backend/): uv run python ../docs/age-verification/cases/tools/case_check.py sp-01 [sp-02 …] [--anchors].

Kept questions = the draft minus drops.tsv, a replacement («replaces») standing in its dropped question's place.
Flags: fields, weekday of every dated phrase, national festivos named in a date, stem 20–50 words, options 5–20 (40),
the bank's lint patterns, explanations naming letters, lowercase negatives. Stats: tema slots, computations, stem
forms, key position, key longest/shortest, length z-scores (the platform guard's null), difficulty.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from datetime import date, timedelta
from math import sqrt
from pathlib import Path
from statistics import fmean

ROOT = Path(__file__).resolve().parents[4]
CASES = ROOT / "docs" / "age-verification" / "cases"
FIELDS = {"id", "bloque", "tema", "lesson", "section", "citation", "stem_form", "names_article", "negative", "prompt",
          "options", "correct", "difficulty", "tags", "distractor_pattern", "computes", "depends_on", "explanation",
          "source_quote"}
FORMS = ["directa", "senale", "enunciado", "art-pregunta", "art-completar", "cual", "norma-sin-art"]
MONTHS = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
          "noviembre", "diciembre"]
DAYS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
DATED = re.compile(rf"\b({'|'.join(DAYS)}),?\s+(?:día\s+)?(\d{{1,2}})\s+de\s+({'|'.join(MONTHS)})(?:\s+de\s+(\d{{4}}))?",
                   re.I)
LINT = [
    (r"\bde el\b", "«de el»"), (r"\ba el\b", "«a el»"),
    (r"\bde (Constitución|Ley Orgánica|Ley|Real Decreto|Reglamento)\b", "norm title without its article"),
    (r"[“”\"]", "English quotes"), (r"  ", "double space"),
]
EXPLANATION = re.compile(
    r"\b(la|opción|respuesta) ([abcd])\)?(?=[\s,.;])|\b(primera|segunda|tercera|cuarta|última) (opción|alternativa)"
    r"|\b(la|en la) (primera|segunda|tercera|cuarta|última)\b", re.I)
ARTICLE_OPTION = re.compile(r"^(el |la )?(art(ículo|\.)|apartado|letra|disposición)\s", re.I)
#: Amounts (1.234 / 12,50): the figures a repeated amount question shares, never dates or years.
FIGURE = re.compile(r"\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+,\d+")
NEGATIVE_LOWER = re.compile(r"\b(no|incorrecta|falsa)\b")


def easter(year: int) -> date:
    a, b, c = year % 19, year // 100, year % 100
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l_ = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l_) // 451
    month, day = divmod(h + l_ - 7 * m + 114, 31)
    return date(year, month, day + 1)


def festivos(year: int) -> dict[date, str]:
    fixed = {(1, 1): "Año Nuevo", (1, 6): "Epifanía", (5, 1): "Fiesta del Trabajo", (8, 15): "Asunción",
             (10, 12): "Fiesta Nacional", (11, 1): "Todos los Santos", (12, 6): "Constitución",
             (12, 8): "Inmaculada", (12, 25): "Navidad"}
    out = {date(year, m, d): n for (m, d), n in fixed.items()}
    out[easter(year) - timedelta(days=2)] = "Viernes Santo"
    out[easter(year) - timedelta(days=3)] = "Jueves Santo (regional)"
    if year == 2027:  # Madrid, Decreto 82/2026 and the city's local days (plan.md)
        out.update({date(2027, 3, 19): "San José (Madrid)", date(2027, 8, 16): "Asunción moved (Madrid)",
                    date(2027, 11, 9): "Almudena (Madrid city)"})
    return out


def drops() -> set[str]:
    """drops.tsv is append-only; a restore in restored.tsv cancels the drops up to its «upto» line, not later ones."""
    with (CASES / "drops.tsv").open(encoding="utf-8") as handle:
        lines = [(n, row["id"]) for n, row in enumerate(csv.DictReader(handle, delimiter="\t"), start=2)]
    upto: dict[str, int] = {}
    path = CASES / "restored.tsv"
    if path.exists():
        with path.open(encoding="utf-8") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                upto[row["id"]] = max(upto.get(row["id"], 0), int(row.get("upto") or 10**9))
    return {qid for n, qid in lines if n > upto.get(qid, 0)}


def kept(case: dict) -> list[dict]:
    """Authored order, each dropped question replaced by the live replacement that names it (transitively)."""
    dropped = drops()
    by_replaced = {q["replaces"]: q for q in case["questions"] if q.get("replaces")}
    out = []
    for q in case["questions"]:
        if q.get("replaces"):
            continue
        current = q
        while f"{case['case']}/{current['id']}" in dropped and current["id"] in by_replaced:
            current = by_replaced[current["id"]]
        if f"{case['case']}/{current['id']}" not in dropped:
            out.append(current)
    return out


#: «3 de marzo de 2027» with no weekday before it, and a dated phrase with its year run into the next word.
FULL_DATE = re.compile(rf"\b\d{{1,2}} de ({'|'.join(MONTHS)}) de \d{{4}}", re.I)
WEEKDAY_BEFORE = re.compile(rf"\b({'|'.join(DAYS)}),?\s+(día\s+)?$", re.I)
YEAR_RUN_ON = re.compile(rf"\b({'|'.join(DAYS)}),?\s+\d{{1,2}} de ({'|'.join(MONTHS)}) de \d{{4}} (?!y\b|o\b)\w", re.I)


def check_dates(text: str, default_year: int, where: str) -> list[str]:
    issues = []
    for match in FULL_DATE.finditer(text):
        if not WEEKDAY_BEFORE.search(text[max(0, match.start() - 16) : match.start()]):
            issues.append(f"{where}: «{match.group(0)}» has no weekday")
    for match in YEAR_RUN_ON.finditer(text):
        issues.append(f"{where}: «{match.group(0)}» needs a comma after the year")
    for match in DATED.finditer(text):
        weekday, day, month, year = match.groups()
        y = int(year) if year else default_year
        try:
            d = date(y, MONTHS.index(month.lower()) + 1, int(day))
        except ValueError:
            issues.append(f"{where}: impossible date «{match.group(0)}»")
            continue
        if DAYS[d.weekday()] != weekday.lower():
            issues.append(f"{where}: «{match.group(0)}» is a {DAYS[d.weekday()]}{'' if year else f' (year {y} assumed)'}")
        if d in festivos(y):
            issues.append(f"{where}: «{match.group(0)}» is {festivos(y)[d]} (named? fine; counted? check)")
    return issues


def longest(lengths: list[int], k: int) -> float:
    m = max(lengths)
    return float(lengths.count(m) == 1 and lengths.index(m) == k)


def edge(lengths: list[int], k: int) -> float:
    return lengths[k] - fmean([x for i, x in enumerate(lengths) if i != k])


def zscore(rows: list[tuple[list[int], int]], stat) -> float:
    obs = sum(stat(L, k) for L, k in rows)
    mean = var = 0.0
    for L, _ in rows:
        vals = [stat(L, i) for i in range(len(L))]
        mu = fmean(vals)
        mean += mu
        var += fmean([(v - mu) ** 2 for v in vals])
    return (obs - mean) / sqrt(var) if var else 0.0


def slots(case_id: str) -> Counter:
    with (CASES / "slots.tsv").open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["case"] == case_id:
                return Counter({p.split()[0]: int(p.split()[1]) for p in row["slots"].split(" · ")})
    return Counter()


def check(case_id: str, citations) -> tuple[list[tuple[list[int], int]], int]:
    case = json.loads((CASES / f"{case_id}.draft.json").read_text(encoding="utf-8"))
    questions = kept(case)
    flags: list[str] = []
    years = Counter(int(y) for y in re.findall(r"\b(20[2-3]\d)\b", case["scenario"]))
    year = years.most_common(1)[0][0] if years else 2027
    words = len(case["scenario"].split())
    if not 300 <= words <= 550:
        flags.append(f"scenario {words} words (300–550)")
    if not case["scenario"].rstrip().endswith("Se plantean las siguientes cuestiones:"):
        flags.append("scenario does not end with «Se plantean las siguientes cuestiones:»")
    flags += check_dates(case["scenario"], year, "scenario")
    for pattern, label in LINT:
        if re.search(pattern, case["scenario"]):
            flags.append(f"scenario: {label}")
    ids = [q["id"] for q in case["questions"]]
    if len(set(ids)) != len(ids):
        flags.append("duplicate question ids")
    for q in questions:
        qid = q["id"]
        missing = FIELDS - q.keys()
        if missing:
            flags.append(f"{qid}: missing {sorted(missing)}")
            continue
        if sorted(q["options"]) != ["a", "b", "c", "d"] or q["correct"] not in "abcd":
            flags.append(f"{qid}: options/correct malformed")
            continue
        n = len(q["prompt"].split())
        if not 20 <= n <= 50:
            flags.append(f"{qid}: stem {n} words (20–50)")
        if not q["prompt"].rstrip().endswith((":", "?")):
            flags.append(f"{qid}: stem ends neither in «:» nor «?»")
        for key, text in q["options"].items():
            w = len(text.split())
            if w < 5 or w > 40:
                flags.append(f"{qid}: option {key} {w} words")
            if ARTICLE_OPTION.match(text.strip()):
                flags.append(f"{qid}: option {key} is an article reference")
        if len(set(q["options"].values())) < 4:
            flags.append(f"{qid}: two options identical")
        texts = [q["prompt"], *q["options"].values(), q["explanation"]]
        for pattern, label in LINT:
            if any(re.search(pattern, t) for t in texts):
                flags.append(f"{qid}: {label}")
        if q["negative"] and NEGATIVE_LOWER.search(q["prompt"]):
            flags.append(f"{qid}: negative stem in lowercase")
        if EXPLANATION.search(q["explanation"]):
            flags.append(f"{qid}: explanation may name an option by letter or position")
        if not q["depends_on"]:
            flags.append(f"{qid}: depends_on empty")
        for t, where in ((q["prompt"], "stem"), (q["explanation"], "explanation"),
                         *((o, f"option {k}") for k, o in q["options"].items())):
            flags += check_dates(t, year, f"{qid} {where}")
        if q["computes"] == "date" and "cómputo" not in q["tags"]:
            flags.append(f"{qid}: date computation without tag cómputo")
        if q["stem_form"] not in FORMS:
            flags.append(f"{qid}: stem_form {q['stem_form']!r}")
        if citations is not None and citations._anchor(q["lesson"], q["citation"], "es") is None:
            flags.append(f"{qid}: citation «{q['citation']}» has no anchor in {q['lesson']}")
    n = len(questions)
    rows = [([len(q["options"][o]) for o in "abcd"], "abcd".index(q["correct"])) for q in questions if "options" in q]
    tema = Counter(q.get("tema") for q in questions)
    want = slots(case_id)
    computes = Counter(q.get("computes") for q in questions)
    forms = Counter(q.get("stem_form") for q in questions)
    shortest = sum(1 for L, k in rows if L.count(min(L)) == 1 and L.index(min(L)) == k)
    print(f"{case_id} «{case['title']}»: scenario {words} words; kept {n} of {len(case['questions'])} authored")
    print(f"  temas {dict(sorted(tema.items()))}" + ("" if tema == want else f"  (slots {dict(sorted(want.items()))})"))
    print(f"  computes date {computes['date']} amount {computes['amount']} (≥10 written, ≥9 kept)"
          f"  negative {sum(bool(q.get('negative')) for q in questions)}"
          f"  difficulty {dict(sorted(Counter(q.get('difficulty') for q in questions).items()))}")
    print("  forms " + " / ".join(f"{f} {forms[f]}" for f in FORMS if forms[f]))
    print(f"  keypos {dict(sorted(Counter(q.get('correct') for q in questions).items()))}"
          f"  key-longest {sum(longest(L, k) for L, k in rows):.0f}  key-shortest {shortest}"
          f"  length-edge z {zscore(rows, edge):+.2f}  longest z {zscore(rows, longest):+.2f}")
    for f in flags:
        print("  FLAG", f)
    print(f"  {len(flags)} flags")
    return rows, len(flags)


def figures(options: frozenset[str]) -> list[set[str]]:
    """Each option's amounts, less those every option shares (the statutory rate, not the case's figures)."""
    sets = [set(FIGURE.findall(o)) for o in options]
    common = set.intersection(*sets) if sets else set()
    return [f - common for f in sets]


def report_duplicates(case_ids: list[str]) -> None:
    """A kept question of the cases checked whose option set another case's kept question already has."""
    seen: dict[frozenset[str], str] = {}
    stems: list[tuple[str, str, set[str], frozenset[str]]] = []
    for draft in sorted(CASES.glob("sp-[0-9][0-9].draft.json")):
        case = json.loads(draft.read_text(encoding="utf-8"))
        for q in kept(case):
            options = frozenset(q.get("options", {}).values())
            where = f"{case['case']}/{q['id']}"
            words = {w for w in re.findall(r"\w{4,}", q.get("prompt", "").lower())}
            if case["case"] in case_ids:
                if options in seen:
                    print(f"DUPLICATE {where}: same option set as {seen[options]}")
                # Same rule, same question with new names and figures (sp-12/q16 against sp-02/q18).
                for other, citation, other_words, other_options in stems:
                    overlap = len(words & other_words) / max(1, len(words | other_words))
                    shared = len(options & other_options)
                    # Options built from the same figures, worded differently (sp-14/q18 against sp-05/q16).
                    mine, theirs = figures(options), figures(other_options)
                    by_figures = sum(1 for m in mine if m and any(m & t for t in theirs))
                    shared = max(shared, by_figures if by_figures >= 3 else 0)
                    if not other.startswith(case["case"]) and citation == q.get("citation") and ((overlap >= 0.4 and shared) or shared >= 2):
                        print(f"DUPLICATE {where}: same citation, {overlap:.0%} of the stem's words and {shared} identical option(s) as {other}")
            seen.setdefault(options, where)
            stems.append((where, q.get("citation", ""), words, options))


def main(argv: list[str]) -> None:
    citations = None
    if "--anchors" in argv:
        from tradeschool.citations.course import CourseCitations

        course = ROOT / "content" / "age-administrativo-c1"
        markdown = {"es": {p.stem: p.read_text(encoding="utf-8") for p in (course / "es" / "lessons").glob("*.md")}}
        citations = CourseCitations.build(course, course.name, markdown)
    every: list[tuple[list[int], int]] = []
    report_duplicates([a for a in argv if not a.startswith("--")])
    for case_id in [a for a in argv if not a.startswith("--")]:
        rows, _ = check(case_id, citations)
        every += rows
    if len(every) > 20:
        print(f"ALL {len(every)}: length-edge z {zscore(every, edge):+.2f}  longest z {zscore(every, longest):+.2f}")


if __name__ == "__main__":
    main(sys.argv[1:])
