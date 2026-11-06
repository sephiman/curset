"""Per-tema numbers for docs/age-c2-theory-ledger.md, from the lessons, records, verify and coverage reports."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
B = ROOT / "docs/age-verification/c2/bloque-i"
glossary = (ROOT / "content/age-auxiliar-c2/glossary.yaml").read_text()
print("| Tema | Lesson | Words | Sentences | Inherited from C1 | Verified here | FAIL (fixed) | Coverage (covered / questions) | Glossary |")
print("|---|---|---|---|---|---|---|---|---|")
tot = [0] * 6
for n in range(1, 17):
    lid = f"m01-l{n:02d}"
    words = len((ROOT / f"content/age-auxiliar-c2/es/lessons/{lid}.md").read_text().split())
    rec = (B / f"{lid}.md").read_text()
    inh, ver = rec.count("· verificado en C1:"), rec.count("· verificado: PASS")
    fails = sum(len(re.findall(r"^\| `[0-9a-f]{10}` \| FAIL", p.read_text(), re.M)) for p in B.glob(f"verify/{lid}*.md"))
    cov = (B / f"coverage/{lid}.md").read_text()
    covered = len(re.findall(r"^\|[^|]*\|\s*\**COVERED", cov, re.M))
    miss = len(re.findall(r"^\|[^|]*\|\s*\**MISS", cov, re.M))
    gl = glossary.count(f"origin: {lid}\n")
    print(f"| I.{n} | `{lid}` | {words:,} | {inh + ver} | {inh} | {ver} | {fails} | {covered} / {covered + miss} | {gl} |")
    for i, v in enumerate((words, inh + ver, inh, ver, fails, gl)):
        tot[i] += v
print(f"| **Total** | | {tot[0]:,} | {tot[1]} | {tot[2]} | {tot[3]} | {tot[4]} | | {tot[5]} |")
