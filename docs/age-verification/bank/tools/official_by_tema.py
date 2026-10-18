"""Split the official questionnaires into questions and file them by the exams ledger's tema."""
import re, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path('/home/juanjo/PycharmProjects/curset')
LEDGER = (ROOT / 'docs/age-official-exams-ledger.md').read_text()
EX = Path(sys.argv[1])
OUT = Path(sys.argv[2])
FILES = {
    'conv2025_A': '2026-05-23_conv2025_modeloA_cuestionario.txt',
    'conv2025_X': '2026-07-24_conv2025_extraordinario_cuestionario.txt',
    'conv2024_A': 'conv2024_modeloA_cuestionario.txt',
    'conv2024_X': 'conv2024_extraordinario_cuestionario.txt',
    'conv2022': 'conv2022_cuestionario.txt',
    'conv2022_X': 'conv2022_extraordinario_cuestionario.txt',
    'conv2020': 'conv2020_cuestionario.txt',
    'conv2020_X': 'conv2020_extraordinario_cuestionario.txt',
}
SECTIONS = ['Primera parte', 'Primera parte — preguntas de reserva', 'Supuesto I',
            'Supuesto I — preguntas de reserva', 'Supuesto II', 'Supuesto II — preguntas de reserva']

def ledger_tables(code):
    m = re.search(rf'^## {re.escape(code)} — .*?(?=^## |\Z)', LEDGER, re.S | re.M)
    body = m.group(0)
    out = {}
    for sec in SECTIONS:
        sm = re.search(rf'^### {re.escape(sec)}\n(.*?)(?=^### |\Z)', body, re.S | re.M)
        rows = {}
        if sm:
            for line in sm.group(1).splitlines():
                c = [x.strip() for x in line.strip().strip('|').split('|')]
                if len(c) >= 4 and c[0].isdigit():
                    rows[int(c[0])] = (c[1], c[2], c[3], c[5] if len(c) > 5 else '')
        out[sec] = rows
    return out

QSTART = re.compile(r'^\s{0,6}(\d{1,2})\.\s+\S')

def split_sections(text):
    lines = text.splitlines()
    cur = None  # nothing before the PRIMERA PARTE heading is a question (cover instructions)
    secs = defaultdict(list)
    sup = None
    for ln in lines:
        s = ln.strip()
        if s == 'PRIMERA PARTE': cur = 'Primera parte'; continue
        if cur is None: continue
        if re.fullmatch(r'SUPUESTO I', s): cur = sup = 'Supuesto I'; continue
        if re.fullmatch(r'SUPUESTO II', s): cur = sup = 'Supuesto II'; continue
        if re.match(r'(?i)preguntas de reserva', s):
            cur = (sup or 'Primera parte') + ' — preguntas de reserva'; continue
        if 'ADVO' in s and len(s) < 140 and not QSTART.match(ln): continue
        secs[cur].append(ln.rstrip())
    return secs

def questions(lines):
    qs = {}; cur = None; expect = 1
    for ln in lines:
        m = QSTART.match(ln)
        if m and int(m.group(1)) == expect:
            cur = expect; qs[cur] = [ln.strip()]; expect += 1
        elif cur is not None and ln.strip():
            qs[cur].append(ln.strip())
    return qs

by_tema = defaultdict(list)
for code, fname in FILES.items():
    tables = ledger_tables(code)
    secs = split_sections((EX / fname).read_text())
    for sec in SECTIONS:
        qs = questions(secs.get(sec, []))
        for n, (tema, estado, clave, nota) in tables[sec].items():
            main = tema.split()[0]
            alt = re.findall(r'\(o ([IV]+\.\d+)\)', tema)
            text = '\n'.join(qs.get(n, ['(texto no extraído)']))
            for t in [main] + alt:
                by_tema[t].append((code, sec, n, tema, estado, clave, nota, text))

OUT.mkdir(parents=True, exist_ok=True)
for t, items in by_tema.items():
    if not re.fullmatch(r'[IV]+\.\d+', t): continue
    parts = [f'# Official questions filed under tema {t}\n',
             'Generated from the questionnaires in sources/examenes-oficiales/ (pdftotext -layout) and the tema, estado and',
             'key columns of docs/age-official-exams-ledger.md. Reference for authors and verifiers: the facts asked, and the',
             'texts no authored question may reproduce (R5.5). Official keys are never a source of facts.\n']
    for code, sec, n, tema, estado, clave, nota, text in items:
        parts.append(f'## {code} · {sec} · {n} — tema {tema} · {estado} · clave {clave}' + (f' · {nota}' if nota else ''))
        parts.append('```\n' + text + '\n```\n')
    (OUT / f'{t}.md').write_text('\n'.join(parts))
print(sorted((t, len(v)) for t, v in by_tema.items()))
