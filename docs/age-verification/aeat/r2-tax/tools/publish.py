"""publish.py: copy staged glossary entries and summaries whose latest blind verdict is PASS into the course.

Verdicts come from r2-tax/extras-verify*.md (a later report wins). Glossary entries go to glossary.yaml with a
«verificado: PASS» line in r2/glossary.md; summaries replace «Resumen pendiente.» in course.yaml. Idempotent.
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
TAX = ROOT / "docs/age-verification/aeat/r2-tax"
COURSE = ROOT / "content/aeat-agentes-hacienda"
RECORD = ROOT / "docs/age-verification/aeat/r2/glossary.md"
ROW = re.compile(r"^\|\s*`?(?P<id>(?:g|sum)-[^`|\s]+)`?\s*\|\s*(?P<verdict>PASS|FAIL)\b")


def verdicts() -> dict[str, tuple[str, str]]:
    def order(path: Path) -> int:
        tail = path.stem.removeprefix("extras-verify")
        return int(tail[1:]) if tail.startswith("-") else 1

    out: dict[str, tuple[str, str]] = {}
    for report in sorted(TAX.glob("extras-verify*.md"), key=order):
        for line in report.read_text().splitlines():
            match = ROW.match(line)
            if match:
                out[match["id"]] = (match["verdict"], str(report.relative_to(ROOT)))
    return out


def wrap(text: str, indent: int) -> str:
    words, lines, line = text.split(), [], ""
    for word in words:
        if line and len(line) + 1 + len(word) > 118 - indent:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}" if line else word
    lines.append(line)
    return ("\n" + " " * indent).join(lines)


def quoted(text: str) -> str:
    return "'" + text.replace("'", "''") + "'"


def publish_glossary(found: dict[str, tuple[str, str]]) -> None:
    glossary = COURSE / "glossary.yaml"
    text = glossary.read_text()
    have = set(re.findall(r"^- id: (g-[a-z0-9-]+)$", text, re.M))
    record = RECORD.read_text()
    added = 0
    for staged in sorted(TAX.glob("glossary-staged*.yaml")):
        for entry in yaml.safe_load(staged.read_text()) or []:
            gid = entry["id"]
            verdict, report = found.get(gid, ("", ""))
            if verdict != "PASS" or gid in have:
                continue
            definition = wrap(quoted(entry["definition"]["es"]), 6)
            text = text.rstrip("\n") + (
                f"\n- id: {gid}\n  es: {entry['es']}\n  origin: {entry['origin']}\n  definition:\n"
                f"    es: {definition}\n"
            )
            record = record.rstrip("\n") + f"\n- `{gid}` · verificado: PASS · {report}\n"
            have.add(gid)
            added += 1
    total = len(re.findall(r"^- `g-", record, re.M))
    verified = len(re.findall(r"^- `g-[^`]+` · verificado: PASS", record, re.M))
    record = re.sub(
        r"^Entradas: \d+ · heredadas: \d+ · verificadas: \d+\.",
        f"Entradas: {total} · heredadas: {total - verified} · verificadas: {verified}.",
        record,
        flags=re.M,
    )
    glossary.write_text(text)
    RECORD.write_text(record)
    print(f"glossary: {added} added")


def publish_summaries(found: dict[str, tuple[str, str]]) -> None:
    manifest = COURSE / "course.yaml"
    text = manifest.read_text()
    done = 0
    for staged in sorted(TAX.glob("summaries-staged*.yaml")):
        for lesson, summary in (yaml.safe_load(staged.read_text()) or {}).items():
            if found.get(f"sum-{lesson}", ("",))[0] != "PASS":
                continue
            pattern = re.compile(
                rf"(    - id: {lesson}\n(?:        .*\n|      title:\n)*?      summary:\n        es: )Resumen pendiente\.\n"
            )
            new, count = pattern.subn(lambda m: m.group(1) + wrap(quoted(summary), 10) + "\n", text)
            if count:
                text, done = new, done + 1
    manifest.write_text(text)
    print(f"summaries: {done} written")


if __name__ == "__main__":
    found = verdicts()
    publish_glossary(found)
    publish_summaries(found)
    sys.exit(0)
