import json, re, statistics as st, difflib
from collections import Counter
M = {q['id']: q for q in json.load(open('work/master.json'))}
OV = json.load(open('work/overrides.json'))
C = {}
for f in ['class_p1_know', 'class_p2_new', 'class_p2_old']:
    for c in json.load(open(f'work/{f}.json')):
        c.update(OV.get(c['id'], {})); C[c['id']] = c
EX = ['2025', '2024', '2024X', '2022', '2020', '2020X']
EXL = {'2025': '2025', '2024': '2024 ord.', '2024X': '2024 extr.', '2022': '2022', '2020': 'OEP 2020 ord.', '2020X': 'OEP 2020 extr.'}
OFI = {f'II.{n}' for n in range(5, 13)}
SETS = {'I': lambda c: M[c['id']]['kind'] == 'conocimiento',
        'II.1-4': lambda c: M[c['id']]['kind'] == 'bloque II' and c['tema'] not in OFI,
        'ofi': lambda c: M[c['id']]['kind'] == 'bloque II' and c['tema'] in OFI}
w = lambda s: len(s.split())
NEGCAP = re.compile(r'\b(NO|FALSA|INCORRECTA|INCORRECTO|EXCEPTO|FALSO)\b')
def pct(n, d): return f'{n} ({round(100*n/d) if d else 0}%)'
out = {}
for sname, f in SETS.items():
    res = {}
    for field in ['stem_form', 'option_type', 'distractor']:
        cats = Counter(c[field] for c in C.values() if f(c))
        t = ['| Category | ' + ' | '.join(EXL[e] for e in EX) + ' |', '|---|' + '---|' * len(EX)]
        for cat, _ in cats.most_common():
            row = []
            for e in EX:
                L = [c for c in C.values() if f(c) and c['id'].startswith(e + '-')]
                row.append(pct(sum(c[field] == cat for c in L), len(L)))
            t.append(f'| {cat} | ' + ' | '.join(row) + ' |')
        res[field] = '\n'.join(t)
    # text measures
    t = ['| Measure | ' + ' | '.join(EXL[e] for e in EX) + ' |', '|---|' + '---|' * len(EX)]
    meas = {}
    for e in EX:
        qs = [M[c['id']] for c in C.values() if f(c) and c['id'].startswith(e + '-')]
        keyed = [q for q in qs if q['key'].lower() in 'abcd']
        lng = lambda q: list(map(w, q['opts'].values()))
        longest = sum(1 for q in keyed if w(q['opts'][q['key'].lower()]) == max(lng(q)) and lng(q).count(max(lng(q))) == 1)
        meas[e] = {
            'Questions': len(qs),
            'Negative stems (capitals)': sum(bool(NEGCAP.search(q['stem'])) for q in qs),
            'Negative stems (any, classifier)': sum(C[q['id']]['negative'] for q in qs),
            'Stems naming an article': sum(bool(re.search(r'\bart[íi]culo\s+\d', q['stem'], re.I)) for q in qs),
            'Stems naming the application/version': sum(bool(re.search(r'Windows|Word|Excel|Access|Outlook|Office|Microsoft|Copilot|Edge', q['stem'])) for q in qs),
            'Options «Ninguna…» / «Todas…»': f"{sum(any(re.match(r'ningun', o, re.I) for o in q['opts'].values()) for q in qs)} / {sum(any(re.match(r'todas', o, re.I) for o in q['opts'].values()) for q in qs)}",
            'Stem words, mean / median': f"{round(st.mean(w(q['stem']) for q in qs))} / {round(st.median(w(q['stem']) for q in qs))}",
            'Option words, mean / median': f"{round(st.mean(w(o) for q in qs for o in q['opts'].values()))} / {round(st.median(w(o) for q in qs for o in q['opts'].values()))}",
            'Keyed option is the longest': pct(longest, len(keyed)),
            'Key a / b / c / d / anulada': '/'.join(str(sum(q['key'].lower() == k for q in qs)) for k in 'abcd') + '/' + str(len(qs) - len(keyed)),
        }
    for k in meas['2025']:
        t.append(f'| {k} | ' + ' | '.join(str(meas[e][k]) for e in EX) + ' |')
    res['text'] = '\n'.join(t)
    out[sname] = res
# questions per tema per exam
temas = [f'I.{n}' for n in range(1, 17)] + [f'II.{n}' for n in range(1, 13)]
PA = {'2020', '2020X'}  # «programa anterior»: shown, never counted (R3.4, as in C1)
t = ['| Tema | ' + ' | '.join(EXL[e] + (' (programa anterior)' if e in PA else '') for e in EX) + ' | Total 2022–2025 |', '|---|' + '---|' * (len(EX) + 1)]
for tm in temas:
    cnt = Counter(c['id'].split('-')[0] for c in C.values() if c['tema'] == tm)
    t.append(f'| {tm} | ' + ' | '.join(str(cnt[e]) for e in EX) + f' | {sum(n for e, n in cnt.items() if e not in PA)} |')
out['per_tema'] = '\n'.join(t)
# repeated questions across exams
L = [q for q in M.values() if q['kind'] != 'psicotecnico']
norm = lambda s: re.sub(r'\W+', ' ', s.lower()).strip()
reps = []
for i, a in enumerate(L):
    for b in L[i + 1:]:
        if a['exam'] == b['exam']: continue
        r = difflib.SequenceMatcher(None, norm(a['stem']), norm(b['stem'])).ratio()
        if r > 0.8:
            ro = difflib.SequenceMatcher(None, norm(' '.join(a['opts'].values())), norm(' '.join(b['opts'].values()))).ratio()
            reps.append((a['id'], b['id'], round(r, 2), round(ro, 2), a['stem'][:90]))
out['repeats'] = reps
json.dump(out, open('work/style_stats.json', 'w'), ensure_ascii=False, indent=1)
for k in ['I', 'II.1-4', 'ofi']:
    print('##', k); print(out[k]['text']); print(out[k]['stem_form']); print(out[k]['option_type']); print(out[k]['distractor'])
print(out['per_tema'])
for r in reps: print(r)
