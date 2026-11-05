import json, os, csv
from collections import Counter
M = json.load(open('work/master.json'))
CL = {}
for f in ['class_p1_know', 'class_psico', 'class_p2_new', 'class_p2_old']:
    p = f'work/{f}.json'
    if os.path.exists(p):
        for c in json.load(open(p)): CL[c['id']] = c
OV = json.load(open('work/overrides.json'))
for i, o in OV.items(): CL[i].update(o)
LAB = list(csv.reader(open('work/laboratorios.tsv'), delimiter='\t'))
EXAMS = [
 ('2025', 'A', 'conv2025_A', 'Convocatoria 2025 — ejercicio único, modelo A', '2026-05-23_conv2025_modeloA', 'Fecha del examen: 23-05-2026 (del nombre del fichero; el cuestionario no imprime fecha).'),
 ('2025', 'B', 'conv2025_B', 'Convocatoria 2025 — ejercicio único, modelo B', '2026-05-23_conv2025_modeloB', 'Fecha del examen: 23-05-2026 (ídem). Repite el modelo A en otro orden; la columna «Nota» da el número del modelo A.'),
 ('2024', 'A', 'conv2024_A', 'Convocatoria 2024 (OEP 2023-2024) — ejercicio único, modelo A', 'conv2024_modeloA', 'Fecha del examen: no impresa; PDF creado el 07-11-2024.'),
 ('2024', 'B', 'conv2024_B', 'Convocatoria 2024 (OEP 2023-2024) — ejercicio único, modelo B', 'conv2024_modeloB', 'Fecha del examen: la del modelo A. Repite el modelo A en otro orden.'),
 ('2024X', None, 'conv2024_X', 'Convocatoria 2024 — llamamiento extraordinario', 'conv2024_extraordinario', 'Fecha del examen: no impresa; PDF creado el 10-02-2025. Misprint: segunda parte, «39.¿Cuál…» sin espacio.'),
 ('2022', None, 'conv2022', 'Convocatoria 2022 (OEP 2021-2022) — ejercicio único', 'conv2022', 'Fecha del examen: no impresa; PDF creado el 19-09-2023. Misprint: segunda parte, reserva 5 impresa «5    En Excel 2019…» sin punto. No hay llamamiento extraordinario publicado.'),
 ('2020', None, 'conv2020', 'OEP 2020 — ejercicio único (programa anterior)', 'conv2020', 'Fecha del examen: no impresa; PDF creado el 27-01-2022. Portada «CUESTIONARIO 19 / AUX–LI», pie «2019 AUX-LI»; la plantilla dice «Oferta de Empleo Público de 2020».'),
 ('2020X', None, 'conv2020_X', 'OEP 2020 — ejercicio extraordinario (programa anterior)', 'conv2020_extraordinario', 'Fecha del examen: no impresa; PDF creado el 28-03-2022. Mismo rótulo «CUESTIONARIO 19 / AUX–LI … EXTRAORDINARIO».'),
]
SECS = [('P1', 'Primera parte'), ('R1', 'Primera parte — preguntas de reserva'), ('P2', 'Segunda parte'), ('R2', 'Segunda parte — preguntas de reserva')]
ab = {'2025': json.load(open('work/ab_2025.json')), '2024': json.load(open('work/ab_2024.json'))}
bkey = {}
for e, stem in [('2025', '2026-05-23_conv2025_modeloB'), ('2024', 'conv2024_modeloB')]:
    bkey[e] = json.load(open(f'keys/{stem}_plantilla-definitiva.json'))
LABQ = {'2024-P1-55', '2024-P1-56', '2024-P1-57', '2024-P1-58', '2024-P1-59', '2024-P1-60'}

def status_bucket(s):
    for k in ['vigente-con-nota', 'vigente', 'anulada', 'norma modificada', 'función retirada', 'dudosa', 'fuera de temario']:
        if s.startswith(k): return k
    return s

def row(q, c, num, extra=''):
    if q['kind'] == 'psicotecnico':
        tema = f'psico: {c["type"]}'
    else:
        tema = c['tema'] + (f' (o {c["tema_alt"]})' if c.get('tema_alt') else '')
    key = q['key'].lower() if q['key'].lower() in 'abcd' else 'Anulada'
    notes = [x for x in [c.get('nota', '')] if x]
    if q['id'] in LABQ: notes.insert(0, 'Tabla «Cuadro Laboratorios» transcrita de la imagen (véase la transcripción al final).')
    if extra: notes.insert(0, extra)
    cell = lambda s: (s or '').replace('|', '\\|').replace('\n', ' ')
    return f'| {num} | {cell(tema)} | {cell(c["status"])} | {key} | {cell(c.get("nota_clave", ""))} | {cell(" ".join(notes))} |'

o = []
summary = []
body = []
for ex, mod, lab, title, stem, info in EXAMS:
    qs = [q for q in M if q['exam'] == ex]
    body.append(f'## {lab} — {title}\n')
    body.append(f'- {info}')
    body.append(f'- Cuestionario: `sources/examenes-oficiales/{stem}_cuestionario.pdf`. Plantilla definitiva: `sources/examenes-oficiales/{stem}_plantilla-definitiva.pdf`.\n')
    cnt = Counter()
    for sec, sname in SECS:
        body.append(f'### {sname}\n')
        body.append('| Nº | Tema / tipo | Estado | Clave | Nota de clave | Nota |')
        body.append('|---|---|---|---|---|---|')
        if mod == 'B':
            inv = {v: k for k, v in ab[ex].items()}
            items = sorted(((int(v.split('.')[1]), k) for k, v in ab[ex].items() if v.split('.')[0] == sec))
            for nb, ka in items:
                q = next(x for x in qs if f"{x['sec']}.{x['n']}" == ka)
                c = CL[q['id']]
                kb = bkey[ex][f'{sec}.{nb}']
                q2 = dict(q, key=kb)
                body.append(row(q2, c, nb, f'= modelo A {ka.replace(".", " ")}.'))
                cnt[status_bucket(c['status'])] += 1
        else:
            for q in sorted([x for x in qs if x['sec'] == sec], key=lambda x: x['n']):
                c = CL[q['id']]
                extra = f'Modelo B: {q["modeloB"].replace(".", " ")}.' if q.get('modeloB') else ''
                body.append(row(q, c, q['n'], extra))
                cnt[status_bucket(c['status'])] += 1
        body.append('')
    summary.append((lab, sum(cnt.values()), cnt))

cols = ['vigente', 'vigente-con-nota', 'anulada', 'norma modificada', 'función retirada', 'dudosa', 'fuera de temario']
o.append('# Ledger de exámenes oficiales — Auxiliar Administrativo del Estado (C2), ingreso libre\n')
o.append('Round R0a, 2026-11-05. Input for the «Exámenes oficiales» practice set (requirements v1.1, R5.2, which takes C1\'s R5.5). The set is not built here.\n')
o.append('Columns: **Nº** as numbered by position in the questionnaire. **Tema / tipo**: for bloque I and bloque II questions, the tema of the 2025 programme (`content/age-auxiliar-c2/sources/programa.md`) as `bloque.tema`, a second tema in brackets when the choice is debatable; for psicotécnico questions, `psico:` and the type of `docs/age-c2-psicotecnico-index.md`. **Estado**: see below. **Clave**: as printed on the definitive answer sheet. **Nota de clave**: «Clave oficial discutida» and the reason. **Nota**: why a question is excluded or doubtful, the current name or label the practice set shows, errata in the official text, the modelo B number (in modelo A tables) or the modelo A question it repeats (in modelo B tables), and the transcription mark of the image table.\n')
o.append('Estado (same rules as `docs/age-official-exams-ledger.md`, C1):\n')
o.append('- `vigente`: enters the practice set with the official key, no note.')
o.append('- `vigente-con-nota`: enters with the official key and a visible note: «Clave oficial discutida» (the key is not supported by the text in force, or not unique), «Denominación actual» (an organ renamed since), «Etiqueta actual» (a Windows 11 / Microsoft 365 label that changed; «sin confirmar en la interfaz española» when not checked on a Spanish-locale install).')
o.append('- `norma modificada: …`, `función retirada`, `fuera de temario`: excluded from the set, with the reason. «(cambio-pendiente, desde DD-MM-YYYY)» marks a change already published that takes effect later.')
o.append('- `dudosa`: could not be settled; excluded from the set.')
o.append('- `anulada`: voided on the definitive answer sheet; not in the set.\n')
o.append('Status was checked against the consolidated texts in `content/age-auxiliar-c2/sources/normativa/` (version in force on 2026-11-05), ofimática against Windows 11 and Microsoft 365 desktop (Anexo I 2.2), and every psicotécnico item was recomputed (arithmetic and tables in Python, verbal items against the DLE). Official keys are never a source of facts for authored questions.\n')
o.append('**Software versions.** The 2025 convocatoria fixes Windows 11 and Microsoft 365 desktop. The 2022 and OEP 2020 questionnaires name Windows 10 and Office/Excel 2019: their questions are kept when the feature still exists, with an «Etiqueta actual» note when a label changed, and excluded as `función retirada` when it does not.\n')
o.append('**Naming.** The files `conv2020_*` are the OEP 2020 exams (cover «CUESTIONARIO 19 / AUX–LI», answer sheets «Oferta de Empleo Público de 2020»), the same pattern as in C1. The 2020 sets are «programa anterior», as in C1 (R3.4; Juanjo, 2026-11-05): their questions are classified against the 2025 programme and go into the practice set, filtered as above, but never into tema counts or programme structure.\n')
o.append('**Not published.** The INAP page publishes no Auxiliar extraordinario for 2025 or 2022.\n')
o.append('## Summary\n')
o.append('| Questionnaire | Questions | ' + ' | '.join(cols) + ' |')
o.append('|---|---|' + '---|' * len(cols))
tot = Counter()
for lab, n, cnt in summary:
    o.append(f'| {lab} | {n} | ' + ' | '.join(str(cnt[k]) for k in cols) + ' |')
    tot.update(cnt)
o.append(f'| **Total** | {sum(n for _, n, _ in summary)} | ' + ' | '.join(str(tot[k]) for k in cols) + ' |\n')
d = Counter(status_bucket(CL[q['id']]['status']) for q in M)
o.append(f'Distinct questions (modelo B not counted): {len(M)}. ' + ', '.join(f'{k} {d[k]}' for k in cols) + '.\n')
o.append('Modelo B repeats modelo A in a different order; its rows duplicate modelo A\'s classification and only the number and key letter change.\n')
# distinct list of excluded and noted
o.append('## Excluded and noted questions (distinct)\n')
for q in M:
    c = CL[q['id']]
    b = status_bucket(c['status'])
    if b in ('vigente',) and not c.get('nota_clave'): continue
    if b == 'anulada':
        n = c.get('nota', '') or 'Anulada en la plantilla definitiva (motivo no publicado).'
        if not n.lower().startswith('anulada'): n = 'Anulada en la plantilla definitiva. ' + n
        o.append(f'- {q["id"]}: {n}'); continue
    o.append(f'- {q["id"]}: {c["status"]}. ' + ' '.join(x for x in [c.get('nota_clave', ''), c.get('nota', '')] if x))
o.append('')
o += body
o.append('## Transcription of the image table «Cuadro Laboratorios» (conv2024, primera parte, 55–60)\n')
o.append('The table is an embedded image in both modelos (the same image, byte for byte). Transcribed from the render `content/age-auxiliar-c2/sources/examenes-oficiales/renders/conv2024_modeloA_cuestionario_p07.png` (modelo B: `…modeloB_cuestionario_p07.png`). Check: the transcription reproduces the six official keys (55 b, 56 a, 57 b, 58 d, 59 a, 60 c in modelo A).\n')
o.append('| ' + ' | '.join(LAB[0]) + ' |')
o.append('|' + '---|' * len(LAB[0]))
for r in LAB[1:]: o.append('| ' + ' | '.join(r) + ' |')
o.append('')
open('/home/juanjo/PycharmProjects/curset/docs/age-c2-official-exams-ledger.md', 'w').write('\n'.join(o) + '\n')
print('missing classes:', [q['id'] for q in M if q['id'] not in CL][:5], sum(q['id'] not in CL for q in M))
