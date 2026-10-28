"""Rewrite `covers` official codes to the short form (P1, P1R, S1, S2, S1R, S2R). Usage: normalise_covers.py bloque-iii."""
import json
import re
import sys
from pathlib import Path

PARTS = [('Primera parte — preguntas de reserva', 'P1R'), ('Supuesto II — preguntas de reserva', 'S2R'),
         ('Supuesto I — preguntas de reserva', 'S1R'), ('Primera parte', 'P1'), ('Supuesto II', 'S2'),
         ('Supuesto I', 'S1'), ('SIIR', 'S2R'), ('SIR', 'S1R'), ('SII', 'S2'), ('SI', 'S1')]


def short(code):
    m = re.fullmatch(r'official:([^·]+)·(.+)·(\d+)', code.strip())
    if not m:
        return code
    part = m.group(2).strip()
    part = dict(PARTS).get(part, part)
    return f'official:{m.group(1).strip()}·{part}·{m.group(3)}'


for f in sorted((Path(__file__).resolve().parents[1] / sys.argv[1]).glob('*.draft.json')):
    qs = json.loads(f.read_text(encoding='utf-8'))
    changed = 0
    for q in qs:
        new = [short(c) for c in q.get('covers', [])]
        changed += new != q.get('covers', [])
        q['covers'] = new
    if changed:
        f.write_text(json.dumps(qs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f.name, 'changed', changed)
