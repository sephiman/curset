"""Mechanical style checks a verifier fails on. Usage: lint_drafts.py bloque-iv m04-l05.part-2 [stem …].

Flags: contraction slips («de el», «a el»), a norm title without its article («de Constitución»), English quotes,
double spaces, stems over 40 words (50 when tagged `cómputo`), options under five words, lowercase negatives,
and explanations that name an option by letter or position.
"""
import json
import re
import sys
from pathlib import Path

D = Path(__file__).resolve().parents[1] / sys.argv[1]
PATTERNS = [
    (r'\bde el\b', '«de el» → «del»'),
    (r'\ba el\b', '«a el» → «al»'),
    (r'\bdl\b', '«dl» typo'),
    (r'\bde (Constitución|Ley Orgánica|Ley|Real Decreto|Reglamento)\b', 'norm title without its article'),
    (r'(?<!47/2003, de 26 de noviembre, )\b[Ll]a Ley General Presupuestaria\b', 'LGP by short name: use its BOE title or name no norm'),
    (r'(?<!9/2017, de 8 de noviembre, )\b[Ll]a Ley de Contratos del Sector Público\b', 'LCSP by short name: use its BOE title or name no norm'),
    (r'[“”]', 'English quotes'),
    (r'  ', 'double space'),
]
EXPLANATION = re.compile(
    r'\b(la|opción|respuesta) ([abcd])\)?(?=[\s,.;])|\b(primera|segunda|tercera|cuarta|última) (opción|alternativa)'
    r'|\b(la|en la) (primera|segunda|tercera|cuarta|última)\b', re.I)
ARTICLE_OPTION = re.compile(r'^(el |la )?(art(ículo|\.)|apartado|letra|disposición)\s', re.I)
NEGATIVE = re.compile(r'\b(no|incorrecta|falsa)\b')
found = 0
for stem in sys.argv[2:]:
    for q in json.loads((D / f'{stem}.draft.json').read_text(encoding='utf-8')):
        issues = []
        texts = [q['prompt'], *q['options'].values(), q['explanation']]
        for pattern, label in PATTERNS:
            if any(re.search(pattern, t) for t in texts):
                issues.append(label)
        limit = 50 if 'cómputo' in q.get('tags', []) else 40
        if len(q['prompt'].split()) < 15:
            issues.append(f"stem {len(q['prompt'].split())} words (under 15)")
        if any(ARTICLE_OPTION.match(o.strip()) for o in q['options'].values()):
            issues.append('an option is an article/apartado reference')
        if len(q['prompt'].split()) > limit:
            issues.append(f"stem {len(q['prompt'].split())} words")
        short = [o for o in q['options'].values() if len(o.split()) < 5]
        if short:
            issues.append(f'options under five words: {short}')
        if q.get('negative') and NEGATIVE.search(q['prompt']):
            issues.append('negative stem in lowercase')
        if EXPLANATION.search(q['explanation']):
            issues.append('explanation may name an option by letter or position')
        if issues:
            found += 1
            print(q['id'], '; '.join(issues))
print(f'{found} questions flagged')
