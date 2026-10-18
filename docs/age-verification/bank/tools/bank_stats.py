"""Kept-question statistics per tema: drafts minus drops.tsv."""
import json, sys, csv
from collections import Counter
from pathlib import Path
D = Path('/home/juanjo/PycharmProjects/curset/docs/age-verification/bank/bloque-i')
drops = {r['id'] for r in csv.DictReader(open(D/'drops.tsv'), delimiter='\t')}
FORMS = ['art-completar','art-pregunta','directa','cual','enunciado','senale','norma-sin-art']
for lesson in sys.argv[1:]:
    qs = json.load(open(D/f'{lesson}.draft.json'))
    kept = [q for q in qs if q['id'] not in drops]
    n = len(kept)
    def longest(q):
        L = {k: len(v) for k, v in q['options'].items()}; m = max(L.values())
        return list(L.values()).count(m) == 1 and L[q['correct']] == m
    sf = Counter(q['stem_form'] for q in kept); df = Counter(q['difficulty'] for q in kept)
    print(f"{lesson}: authored {len(qs)} dropped {len(qs)-n} kept {n}")
    print('  forms', ' / '.join(f"{f} {100*sf[f]/n:.0f}%" for f in FORMS))
    print(f"  names_article {100*sum(q['names_article'] for q in kept)/n:.0f}%  negative {sum(q['negative'] for q in kept)}"
          f"  key-longest {100*sum(map(longest,kept))/n:.0f}%  diff {df[1]}/{df[2]}/{df[3]}"
          f"  keypos {dict(sorted(Counter(q['correct'] for q in kept).items()))}")
    lmc = Counter(c for q in kept for c in q.get('covers', []) if c.startswith('lmc'))
    print('  lmc covered', sorted(lmc, key=lambda s: int(s.split('-')[1])))
