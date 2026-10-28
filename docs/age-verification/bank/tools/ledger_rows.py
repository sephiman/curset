"""Per-tema ledger rows for a bloque: counts, drops by check, mix. Usage: ledger_rows.py bloque-iii m03 III."""
import csv
import json
import sys
from collections import Counter
from pathlib import Path

folder = Path(__file__).resolve().parents[1] / sys.argv[1]
module, roman = sys.argv[2], sys.argv[3]
plan = (Path(__file__).resolve().parents[3] / 'age-bank-plan.md').read_text(encoding='utf-8')
quota = {}
for line in plan.splitlines():
    cells = [c.strip() for c in line.strip('|').split('|')]
    if len(cells) == 6 and cells[1].startswith('`m'):
        quota[cells[1].strip('`')] = int(cells[5])
drops = list(csv.DictReader(open(folder / 'drops.tsv'), delimiter='\t'))
CHECKS = ['key', 'unique', 'citation', 'style', 'official']
FORMS = ['art-completar', 'art-pregunta', 'directa', 'cual', 'enunciado', 'senale', 'norma-sin-art']
print('| Tema | Quota | Authored | Dropped (key / unique / citation / style / official) | Kept | LMC covered |')
print('|---|---|---|---|---|---|')
mix = []
total = Counter()
for draft in sorted(folder.glob(f'{module}-l*.draft.json')):
    if '.part-' in draft.name:
        continue
    lesson = draft.name.split('.')[0]
    qs = json.loads(draft.read_text(encoding='utf-8'))
    ids = {q['id'] for q in qs}
    dropped = {r['id']: r['check'] for r in drops if r['id'] in ids}
    kept = [q for q in qs if q['id'] not in dropped]
    by = Counter(dropped.values())
    lessons_md = (Path(__file__).resolve().parents[3].parent / 'content/age-administrativo-c1/es/lessons' / f'{lesson}.md').read_text()
    block = lessons_md.split('## Lo que más cae')[1].split('## Normativa')[0]
    n_lmc = sum(1 for l in block.splitlines() if l.startswith('- '))
    lmc = {c for q in kept for c in q.get('covers', []) if c.startswith('lmc-')}
    tema = qs[0]['tema']
    print(f"| {tema} | {quota[lesson]} | {len(qs)} | {len(dropped)} ({' / '.join(str(by[c]) for c in CHECKS)}) | {len(kept)} | {len(lmc)}/{n_lmc} |")
    total.update(quota=quota[lesson], authored=len(qs), dropped=len(dropped), kept=len(kept), lmc=len(lmc), nlmc=n_lmc, **{c: by[c] for c in CHECKS})
    n = len(kept)
    sf = Counter(q['stem_form'] for q in kept)
    df = Counter(q['difficulty'] for q in kept)
    def longest(q):
        L = [len(q['options'][o]) for o in 'abcd']
        return L.count(max(L)) == 1 and 'abcd'[L.index(max(L))] == q['correct']
    kp = Counter(q['correct'] for q in kept)
    mix.append(f"| {tema} | {' / '.join(f'{100 * sf[f] / n:.0f}' for f in FORMS)} % | {100 * sum(q['names_article'] for q in kept) / n:.0f} % | "
               f"{sum(q['negative'] for q in kept)} | {100 * sum(map(longest, kept)) / n:.0f} % | {df[1]}/{df[2]}/{df[3]} | {kp['a']}/{kp['b']}/{kp['c']}/{kp['d']} |")
print(f"| **Bloque {roman}** | **{total['quota']}** | **{total['authored']}** | **{total['dropped']} ({' / '.join(str(total[c]) for c in CHECKS)})** | **{total['kept']}** | **{total['lmc']}/{total['nlmc']}** |")
print()
print('| Tema | art-compl. / art-preg. / directa / cuál / enunc. / señale / norma | Names article | Negative | Key longest | Diff 1/2/3 | Key a/b/c/d |')
print('|---|---|---|---|---|---|---|')
print('\n'.join(mix))
