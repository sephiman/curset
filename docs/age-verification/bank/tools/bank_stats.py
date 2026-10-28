"""Kept-question statistics per tema: drafts minus drops.tsv. Usage: bank_stats.py bloque-ii m02-l01 [m02-l02 …].

The length-edge and longest-is-correct z-scores use the platform guard's null (test_quiz_answer_bias.py): the key
equally likely in any of the four slots. A draft file that does not exist yet is skipped.
"""
import csv
import json
import sys
from collections import Counter
from math import sqrt
from pathlib import Path
from statistics import fmean

D = Path(__file__).resolve().parents[1] / sys.argv[1]
drops = {r['id'] for r in csv.DictReader(open(D / 'drops.tsv'), delimiter='\t')} if (D / 'drops.tsv').exists() else set()
FORMS = ['art-completar', 'art-pregunta', 'directa', 'cual', 'enunciado', 'senale', 'norma-sin-art']


def longest(lengths, k):
    m = max(lengths)
    return float(lengths.count(m) == 1 and lengths.index(m) == k)


def edge(lengths, k):
    return lengths[k] - fmean([x for i, x in enumerate(lengths) if i != k])


def z(rows, stat):
    obs = sum(stat(L, k) for L, k in rows)
    mean = var = 0.0
    for L, _ in rows:
        vals = [stat(L, i) for i in range(len(L))]
        mu = fmean(vals)
        mean += mu
        var += fmean([(v - mu) ** 2 for v in vals])
    return (obs - mean) / sqrt(var) if var else 0.0


everything = []
for lesson in sys.argv[2:]:
    f = D / f'{lesson}.draft.json'
    if not f.exists():
        continue
    qs = json.load(open(f))
    kept = [q for q in qs if q['id'] not in drops]
    n = len(kept)
    rows = [([len(q['options'][o]) for o in 'abcd'], 'abcd'.index(q['correct'])) for q in kept]
    everything += rows
    shortest = sum(1 for L, k in rows if L.count(min(L)) == 1 and L.index(min(L)) == k)
    sf = Counter(q['stem_form'] for q in kept)
    df = Counter(q['difficulty'] for q in kept)
    print(f"{lesson}: authored {len(qs)} dropped {len(qs) - n} kept {n}")
    print('  forms', ' / '.join(f"{f} {100 * sf[f] / n:.0f}%" for f in FORMS))
    print(f"  names_article {100 * sum(q['names_article'] for q in kept) / n:.0f}%  negative {sum(q['negative'] for q in kept)}"
          f"  key-longest {100 * sum(longest(L, k) for L, k in rows) / n:.0f}%  key-shortest {100 * shortest / n:.0f}%"
          f"  diff {df[1]}/{df[2]}/{df[3]}  keypos {dict(sorted(Counter(q['correct'] for q in kept).items()))}")
    print(f"  length-edge z {z(rows, edge):+.2f}  longest-is-correct z {z(rows, longest):+.2f}")
    lmc = Counter(c for q in kept for c in q.get('covers', []) if c.startswith('lmc'))
    print('  lmc covered', sorted(lmc, key=lambda s: int(s.split('-')[1])))
if len(sys.argv) > 3 and everything:
    print(f"ALL {len(everything)}: length-edge z {z(everything, edge):+.2f}  longest-is-correct z {z(everything, longest):+.2f}")
