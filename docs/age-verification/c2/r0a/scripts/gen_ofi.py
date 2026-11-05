import json, re
from collections import Counter, defaultdict
M = {q['id']: q for q in json.load(open('work/master.json'))}
OV = json.load(open('work/overrides.json'))
C = []
for f in ['class_p2_new', 'class_p2_old', 'class_p1_know']:
    for c in json.load(open(f'work/{f}.json')):
        c.update(OV.get(c['id'], {}))
        if c.get('app'): C.append(c)
REP = {r['file']: r for r in json.load(open('ms/copy_report.json'))}
# normalise families/apps across the two part-2 classifiers
FAM = {('Outlook', 'Libreta de direcciones y contactos'): ('Outlook', 'Libreta de direcciones y grupos de contactos'),
       ('otros', 'IA y Copilot'): ('Copilot', 'IA y Copilot'),
       ('otros', 'Software, nube y otros conceptos'): ('hardware/software', 'Software, nube y otros conceptos'),
       ('Outlook', 'Correo: protocolos y conceptos'): ('Internet y navegadores', 'Correo: protocolos y conceptos')}
for c in C:
    c['app'], c['family'] = FAM.get((c['app'], c['family']), (c['app'], c['family']))
    c['programme_feature'] = c['programme_feature'].replace('"Este equipo" y "Acceso rápido"', '«Este equipo» y «Acceso rápido»')
EX = ['2025', '2024', '2024X', '2022', '2020', '2020X']
EXL = {'2025': '2025', '2024': '2024 ord.', '2024X': '2024 extr.', '2022': '2022', '2020': 'OEP 2020 ord.', '2020X': 'OEP 2020 extr.'}
CONV = {'2025': '2025', '2024': '2024', '2024X': '2024', '2022': '2022', '2020': '2020', '2020X': '2020'}
APPS = ['Windows', 'Word', 'Excel', 'Access', 'Outlook', 'Internet y navegadores', 'hardware/software', 'seguridad', 'Copilot', 'PowerPoint', 'Teams/OneDrive/SharePoint', 'otros']
ex = lambda c: c['id'].split('-')[0]
def num(c):
    e, s, n = c['id'].split('-')
    q = M[c['id']]
    t = {'P2': 'P2', 'R2': 'P2 res.', 'P1': 'P1', 'R1': 'P1 res.'}[s] + f' {n}'
    if q['modeloB']:
        b = q['modeloB'].split('.')
        t += f' (B {b[1]})'
    return t
def short_status(c):
    s = c['status']
    for k in ['vigente-con-nota', 'vigente', 'anulada', 'norma modificada', 'función retirada', 'dudosa']:
        if s.startswith(k): return k
    return s
cell = lambda s: (s or '').replace('|', '\\|').replace('\n', ' ')

# programme sentences II.5–II.12
prog = open('/home/juanjo/PycharmProjects/curset/content/age-auxiliar-c2/sources/programa.md').read()
blk = prog.split('### II. Actividad administrativa y ofimática')[1].split('\n---')[0]
temas = {}
for m in re.finditer(r'\n(\d+)\. (.*?)(?=\n\n|\Z)', blk, re.S):
    n = int(m.group(1))
    if n >= 5: temas[f'II.{n}'] = re.sub(r'\s+', ' ', m.group(2)).strip()
def sentences(t):
    head, _, rest = t.partition(': ')
    parts = [p.strip().rstrip('.') for p in re.split(r'\.\s+', t) if p.strip()]
    return parts

o = []
o.append('# Ofimática in the official exams — index (Auxiliar, C2)\n')
o.append('Round R0a, 2026-11-05. Every question on temas II.5–II.12 of the 2025 programme (informática básica, Windows, Word, Excel, Access, Outlook, Internet) in the six distinct Auxiliar questionnaires: 2025, 2024 ordinario and extraordinario, 2022, OEP 2020 ordinario and extraordinario (files `conv2020_*`). Bloque II temas II.1–II.4 (atención al público, información, registro y archivo, administración electrónica) are not ofimática and are not indexed here; they are in the ledger. Modelo B repeats modelo A in another order: B numbers are given next to A\'s and questions are not counted twice. There are no Auxiliar extraordinarios for 2025 or 2022.\n')
o.append('Classification per question (tema, application, feature family, feature, programme feature, form, version, status) comes from the round\'s per-exam pass, checked against Windows 11 and Microsoft 365 desktop, the versions Anexo I 2.2 fixes. Feature families group features that test the same thing; they are this index\'s grouping, reusing the names of C1\'s index (`docs/age-ofimatica-index.md`) where one fits. Full question text: `content/age-auxiliar-c2/sources/examenes-oficiales/`. Status per question: `docs/age-c2-official-exams-ledger.md`, which is authoritative.\n')
o.append('Forms: `atajo`, `ruta de menú/cinta`, `función o fórmula`, `resultado de fórmula`, `concepto/definición`, `comportamiento`, `configuración`, `otro` (as in C1).\n')
o.append('**Versions.** 2025 asks about Windows 11 and Microsoft 365. 2024 mixes Windows 10 and 365. 2022 and OEP 2020 name Windows 10 and Office/Excel 2019. The course follows 2025. Older questions are indexed by feature anyway, because most features persist; the «Versión» column gives the version the stem names and section 6 lists the ones whose answer depends on it.\n')
o.append('## 1. Counts\n')
o.append('### Per application and exam\n')
o.append('| Application | ' + ' | '.join(EXL[e] for e in EX) + ' | Total |')
o.append('|---|' + '---|' * (len(EX) + 1))
for a in APPS:
    cnt = Counter(ex(c) for c in C if c['app'] == a)
    o.append(f'| {a} | ' + ' | '.join(str(cnt[e]) for e in EX) + f' | {sum(cnt.values())} |')
tot = Counter(ex(c) for c in C)
o.append('| **All** | ' + ' | '.join(f'**{tot[e]}**' for e in EX) + f' | **{len(C)}** |\n')
o.append('Counts include part-2 reserves. No part-1 question is on bloque II.\n')
o.append('### Per tema and exam\n')
o.append('The OEP 2020 sets are «programa anterior» (as in C1, R3.4): their columns are shown for reference and left out of the total, which covers 2022–2025 only.\n')
PA = {'2020', '2020X'}
o.append('| Tema | ' + ' | '.join(EXL[e] + (' (programa anterior)' if e in PA else '') for e in EX) + ' | Total 2022–2025 |')
o.append('|---|' + '---|' * (len(EX) + 1))
for t in temas:
    cnt = Counter(ex(c) for c in C if c['tema'] == t)
    o.append(f'| {t} | ' + ' | '.join(str(cnt[e]) for e in EX) + f' | {sum(n for e, n in cnt.items() if e not in PA)} |')
o.append('')
o.append('### Share of part 2\n')
o.append('Of the 55 part-2 questions (50 + 5 reserves) of each exam, the ofimática share (II.5–II.12): ' + '; '.join(f'{EXL[e]} {tot[e]} ({round(100*tot[e]/55)} %)' for e in EX) + '. The rest are II.1–II.4.\n')
o.append('### Per form\n')
o.append('| Form | ' + ' | '.join(EXL[e] for e in EX) + ' | Total |')
o.append('|---|' + '---|' * (len(EX) + 1))
for f, _ in Counter(c['form'] for c in C).most_common():
    cnt = Counter(ex(c) for c in C if c['form'] == f)
    o.append(f'| {f} | ' + ' | '.join(str(cnt[e]) for e in EX) + f' | {sum(cnt.values())} |')
o.append('')
o.append('## 2. Index by application\n')
for a in APPS:
    L = [c for c in C if c['app'] == a]
    o.append(f'### {a} ({len(L)})\n')
    if not L:
        o.append('No question.\n'); continue
    o.append('| Exam | Nº | Tema | Family | Feature | Form | Versión | Status |')
    o.append('|---|---|---|---|---|---|---|---|')
    for c in sorted(L, key=lambda c: (c['family'], EX.index(ex(c)), c['id'])):
        o.append(f'| {EXL[ex(c)]} | {num(c)} | {c["tema"]} | {cell(c["family"])} | {cell(c["feature"])} | {c["form"]} | {cell(c.get("version_named") or "")} | {short_status(c)} |')
    o.append('')
fam = defaultdict(list)
for c in C: fam[(c['app'], c['family'])].append(c)
o.append('## 3. Recurring feature families\n')
o.append('Recurring = asked in two or more convocatorias (2025, 2024, 2022, OEP 2020; ordinario and extraordinario of one convocatoria count once). Sorted by number of convocatorias, then questions.\n')
o.append('| Application | Family | Convocatorias | Questions | Features asked |')
o.append('|---|---|---|---|---|')
rows = []
for (a, f), L in fam.items():
    cv = sorted({CONV[ex(c)] for c in L}, reverse=True)
    rows.append((len(cv), len(L), a, f, cv, L))
for ncv, n, a, f, cv, L in sorted(rows, key=lambda r: (-r[0], -r[1], r[2])):
    if ncv < 2: continue
    feats = '; '.join(sorted({c['feature'] for c in L}))
    o.append(f'| {a} | {cell(f)} | {ncv}: {", ".join(cv)} | {n} | {cell(feats)} |')
o.append('')
o.append('## 4. Feature families asked in one convocatoria only\n')
o.append('| Application | Family | Convocatoria | Questions | Features asked |')
o.append('|---|---|---|---|---|')
for ncv, n, a, f, cv, L in sorted(rows, key=lambda r: (r[2], r[3])):
    if ncv != 1: continue
    o.append(f'| {a} | {cell(f)} | {cv[0]} | {n} | {cell("; ".join(sorted({c["feature"] for c in L})))} |')
o.append('')
o.append('## 5. Programme features: asked and never asked\n')
o.append('Each tema of II.5–II.12 split into the phrases of its official text (`sources/programa.md`); the first phrase is the tema\'s title and covers the whole tema, so it is not counted. «Questions» counts the questions whose feature falls under that phrase (one phrase per question, the classifier\'s choice). A phrase with 0 has never been asked in 2020–2025.\n')
pfc = Counter((c['tema'], c['programme_feature'].strip().rstrip('.')) for c in C)
o.append('| Tema | Programme phrase | Questions | Exams |')
o.append('|---|---|---|---|')
never = []
for t, txt in temas.items():
    for j, ph in enumerate(sentences(txt)):
        if j == 0:
            o.append(f'| {t} | {cell(ph)} (título del tema) | — | — |'); continue
        k = [kk for kk in pfc if kk[0] == t and (kk[1].lower() in ph.lower() or ph.lower() in kk[1].lower())]
        n = sum(pfc[kk] for kk in k)
        exs = sorted({EXL[ex(c)] for c in C if c['tema'] == t and any(c['programme_feature'].strip().rstrip('.') == kk[1] for kk in k)}, key=lambda x: list(EXL.values()).index(x))
        o.append(f'| {t} | {cell(ph)} | {n} | {", ".join(exs)} |')
        if n == 0: never.append((t, ph))
o.append('')
o.append('Never asked: ' + '; '.join(f'{t} «{ph}»' for t, ph in never) + '.\n' if never else 'Every programme phrase has been asked at least once.\n')
unmatched = [(t, p, n) for (t, p), n in pfc.items() if not any(p.lower() in s.lower() or s.lower() in p.lower() for s in sentences(temas[t]))]
if unmatched:
    o.append('Questions whose programme phrase the classifier gave in its own words (counted under no phrase above): ' + '; '.join(f'{t} «{p}» ({n})' for t, p, n in unmatched) + '.\n')
o.append('Programme items with no question at all in 2020–2025, read from the table: Copilot is in II.6 since the 2025 programme and has been asked twice (2024 and 2025, conceptual); PowerPoint and Teams/OneDrive/SharePoint are not in the Auxiliar programme and never appear.\n')
o.append('## 6. Retired features, changed labels and version-specific questions\n')
o.append('### Retired (excluded from the practice set)\n')
for c in C:
    if short_status(c) == 'función retirada':
        o.append(f'- {EXL[ex(c)]} {num(c)} — {c["feature"]}. {c.get("nota", "")}')
o.append('')
o.append('### Changed labels («Etiqueta actual»; kept with a note)\n')
for c in C:
    n = (c.get('nota', '') or '') + ' ' + (c.get('nota_clave', '') or '')
    if 'Etiqueta actual' in n:
        o.append(f'- {EXL[ex(c)]} {num(c)} — {c["feature"]}. {n.strip()}')
o.append('')
o.append('### Answer depends on the version the stem names\n')
o.append('Questions whose stem names Windows 10 or Office/Excel 2019 (or an earlier interface) and whose answer, path or label differs in Windows 11 / Microsoft 365 desktop. They stay indexed by feature; authored questions use Windows 11 / Microsoft 365 only.\n')
for c in C:
    if c.get('version_specific'):
        o.append(f'- {EXL[ex(c)]} {num(c)} [{c.get("version_named") or "sin versión"}] — {c["feature"]}: {c["version_specific"]}')
o.append('')
o.append('### Classic and new Outlook\n')
o.append('Keys that hold for classic Outlook and differ in the new Outlook carry a note in the ledger. The bank must say which Outlook a question is about when the two differ (as in C1).\n')
o.append('## 7. Saved Microsoft pages\n')
o.append('Pages of C1 (`content/age-administrativo-c1/sources/otros/`) that cover the features of this index, as named per question by the classifiers. Each was fetched live on 2026-11-05 and compared with C1\'s copy. No live page matches C1\'s stored sha256 byte for byte: the HTML carries build hashes, tracking pixels and an `updated_at` stamp that change on every deploy. The comparison is therefore on the visible text of the article (`<main>` or `<article>`, scripts and tags removed). A page whose text is unchanged was copied from C1 into `content/age-auxiliar-c2/sources/otros/` (same name, same sha256 as C1\'s file). A page whose text changed was saved fresh. Pages the server refused (HTTP 403 to an automated request) were also copied from C1 (Juanjo, 2026-11-05) and are marked «live check pending (403 on 2026-11-05)» in `content/age-auxiliar-c2/sources/otros/fuentes.yaml`; the monthly currency audit retries them. The one page whose URL now serves another page was dropped; the only question it covered, OEP 2020 extr. P2 15 (Grupos de envío y recepción), has no saved source. ' + f'{sum(1 for c in C if not c.get("ms_page"))} questions of this index have no `ms-*` page in C1 (`ms_page` null); those pages would be fetched fresh when the lessons need them.\n')
used = defaultdict(list)
for c in C:
    if c.get('ms_page'): used[c['ms_page']].append(c)
o.append('| File | URL | Action | sha256 (C2 copy) | Features | Reason |')
o.append('|---|---|---|---|---|---|')
for f in sorted(REP):
    r = REP[f]
    feats = '; '.join(sorted({c['feature'] for c in used[f]}))
    o.append(f'| `{f}` | {r["url"]} | {r["action"]} | {r.get("sha256", "")[:16] + "…" if r.get("sha256") else "—"} | {cell(feats)} | {cell(r["reason"])} |')
o.append('')
n_null = sum(1 for c in C if not c.get('ms_page'))
open('/home/juanjo/PycharmProjects/curset/docs/age-c2-ofimatica-index.md', 'w').write('\n'.join(o) + '\n')
print('ok', len(C), 'never', never, 'unmatched', unmatched)
