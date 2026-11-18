"""glossary_record.py: rewrite the AEAT glossary record after R2d; unchanged entries keep their HEAD line."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "backend"))

from scripts.provenance import report_verdicts  # noqa: E402

GLOSSARY = "content/aeat-agentes-hacienda/glossary.yaml"
RECORD = ROOT / "docs/age-verification/aeat/r2/glossary.md"
REPORTS = ROOT / "docs/age-verification/aeat/r2d/glossary"


def _entries(text: str) -> dict[str, dict[str, object]]:
    return {str(t["id"]): t for t in yaml.safe_load(text)["terms"]}


def _order(report: Path) -> tuple[str, int]:
    base, _, number = report.stem.partition("-recheck-")
    return base, int(number) if number.isdigit() else 0


def _r2d_verdicts() -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    for report in sorted(REPORTS.glob("verify*.md"), key=_order):
        for gid, verdict in report_verdicts(report).items():
            out[gid] = (verdict, str(report.relative_to(ROOT)))
    return out


def main() -> int:
    head = subprocess.run(
        ["git", "show", f"HEAD:{GLOSSARY}"], cwd=ROOT, capture_output=True, text=True
    ).stdout
    before, now = _entries(head), _entries((ROOT / GLOSSARY).read_text())
    head_record = subprocess.run(
        ["git", "show", "HEAD:docs/age-verification/aeat/r2/glossary.md"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    ).stdout
    old_lines = {
        m[1]: line for line in head_record.splitlines() if (m := re.match(r"- `(g-[\w-]+)` · ", line))
    }
    preamble = head_record.split("\n- `", 1)[0].split("\nEntradas:")[0]
    verdicts = _r2d_verdicts()
    lines: list[str] = []
    missing: list[str] = []
    inherited = verified = 0
    for gid, entry in now.items():
        old = before.get(gid)
        skip = ("origin", "link_except")
        core = {k: v for k, v in entry.items() if k not in skip}
        same = old is not None and {k: v for k, v in old.items() if k not in skip} == core
        if same and gid in old_lines:
            lines.append(old_lines[gid])
            inherited += "verificado: PASS" not in old_lines[gid]
            verified += "verificado: PASS" in old_lines[gid]
        elif verdicts.get(gid, ("", ""))[0] == "PASS":
            lines.append(f"- `{gid}` · verificado: PASS · {verdicts[gid][1]}")
            verified += 1
        else:
            missing.append(gid)
    if missing:
        print("no PASS for:", ", ".join(missing))
        return 1
    RECORD.write_text(
        f"{preamble}\nEntradas: {inherited + verified} · heredadas: {inherited} · "
        f"verificadas: {verified}.\n\n"
        + "\n".join(lines)
        + "\n"
    )
    print(f"record written: {inherited} inherited, {verified} verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
