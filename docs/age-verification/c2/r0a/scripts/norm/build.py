import yaml, json, re, shutil, hashlib, os, copy, sys
sys.path.insert(0, '.')
from c2sel import SEL
C1 = '/home/juanjo/PycharmProjects/curset/content/age-administrativo-c1/sources'
C2 = '/home/juanjo/PycharmProjects/curset/content/age-auxiliar-c2/sources'
os.makedirs(C2 + '/normativa', exist_ok=True)
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
cur = json.load(open('currency.json'))
d = yaml.safe_load(open(C1 + '/normativa.yaml'))
by = {e['short']: e for e in d}
TODAY = '2026-11-05'
copied, fresh = [], []

def copy_c1(rel):
    name = os.path.basename(rel)
    src, dst = f'{C1}/normativa/{name}', f'{C2}/normativa/{name}'
    shutil.copy2(src, dst)
    assert sha(src) == sha(dst)
    copied.append((name, sha(dst)))
    return f'sources/normativa/{name}'

def place_fresh(src, name):
    dst = f'{C2}/normativa/{name}'
    shutil.copy2(src, dst)
    fresh.append((name, sha(dst)))
    return f'sources/normativa/{name}'

LEY4 = 'BOE-A-2026-20528'
RDL31 = {'norma': 'Real Decreto-ley 31/2026, de 20 de octubre', 'boe_id': 'BOE-A-2026-21872', 'publicada': '2026-10-21'}
out = []
for s, temas in SEL.items():
    e = copy.deepcopy(by[s])
    e['temas'] = temas
    e['origen'] = 'copiado de age-administrativo-c1 (mismo nombre y sha256)'
    # every C1 normativa file the entry references (main file, cambios_pendientes, correcciones, notes)
    refs = set(re.findall(r'(?:sources/normativa/)?((?:BOE-A|CELEX)-[\w.-]+\.(?:pdf|html))', yaml.safe_dump(e, allow_unicode=True)))
    i = e.get('boe_id')
    c = cur.get(i) if i else None
    if c and c['ultima'] and c['ultima'] != e['consolidated_as_of']:
        # boe.es has a newer consolidation than C1's snapshot: fresh download
        e['consolidated_as_of'] = c['ultima']
        slug = re.sub(r'^(BOE-A-\d+-\d+)_(.*)_\d{4}-\d\d-\d\d\.pdf$', r'\2', os.path.basename(e['file']))
        e['file'] = place_fresh(f'dl/{i}-consolidado.pdf', f'{i}_{slug}_{c["ultima"]}.pdf')
        e['origen'] = f'descarga nueva el {TODAY}: boe.es tiene una consolidación posterior a la copia de C1 ({by[s]["consolidated_as_of"]})'
        e['version_vigente'] = {'consolidated_as_of': c['ultima']}
        refs.discard(os.path.basename(by[s]['file']))
    for r in sorted(refs):
        if os.path.exists(f'{C1}/normativa/{r}'):
            copy_c1(r)
    # Ley 4/2026 took effect on 2026-10-23: no longer pending
    cps = e.get('cambios_pendientes') or []
    keep = []
    for cp in cps:
        if cp.get('boe_id') == LEY4:
            e.setdefault('amended_2025_2026', []) or None
            e['amended_2025_2026'] = [a.replace('PENDIENTE: publicada 03-10-2026, en vigor 23-10-2026', 'publicada 03-10-2026, en vigor desde 23-10-2026') for a in (e.get('amended_2025_2026') or [])]
            e['version_vigente'] = {'consolidated_as_of': e['consolidated_as_of'],
                                    'note': 'Ley 4/2026 en vigor desde el 23-10-2026: la redacción que el fichero integra es la vigente el ' + TODAY + '.'}
        else:
            keep.append(cp)
    e['cambios_pendientes'] = keep
    e['tags'] = ['cambio-pendiente'] if keep else []
    out.append(e)

# RDL 31/2026 on the three Seguridad Social norms
def add_rdl31(short, amend, pend):
    e = next(x for x in out if x['short'] == short)
    e['amended_2025_2026'] = (e.get('amended_2025_2026') or []) + [amend]
    rdl = place_fresh('dl/BOE-A-2026-21872.pdf', 'BOE-A-2026-21872_rdl-31-2026_2026-10-21.pdf')
    if pend:
        e['cambios_pendientes'] = (e.get('cambios_pendientes') or []) + [dict(RDL31, precepto_modificador='véase la disposición final cuarta', en_vigor=p[0], articulos=p[1], file=rdl) for p in pend]
        e['tags'] = ['cambio-pendiente']
        e['version_vigente'] = {'consolidated_as_of': e['consolidated_as_of'],
                                'note': 'Sin comprobar si el consolidado de boe.es integra ya la redacción futura de los preceptos de cambios_pendientes o la muestra con aviso; leer el precepto antes de citarlo.'}
    e['note'] = ((e.get('note') or '') + ' RDL 31/2026 (BOE-A-2026-21872), en vigor el 21-10-2026; pendiente de convalidación por el Congreso (art. 86.2 CE) a la fecha de este fichero.').strip()

add_rdl31('LGSS (RDL 8/2015)',
          'Real Decreto-ley 31/2026, de 20 de octubre (BOE-A-2026-21872): determinados preceptos, DA 64 y DT 48 añadidas, DA 40 suprimida, con los efectos de su DF 4.ª (art. 61.2 desde 01-11-2026; arts. 190–192 desde 23-10-2026)',
          [('2026-12-01', ['arts. 144.4, 169.1.a), 171, 172 y 173.1']), ('2027-01-01', ['art. 309'])])
add_rdl31('RDL 4/2000 (TR Seguridad Social Funcionarios Civiles)',
          'Real Decreto-ley 31/2026, de 20 de octubre (BOE-A-2026-21872): art. 19.1 (PENDIENTE: efectos desde 01-12-2026, según el análisis de boe.es)',
          [('2026-12-01', ['art. 19.1'])])
add_rdl31('RDL 670/1987 (TR Clases Pasivas)',
          'Real Decreto-ley 31/2026, de 20 de octubre (BOE-A-2026-21872): arts. 38, 41 y 42, DT 16 añadida, DA 20 suprimida; art. 27.2 con efectos desde 01-11-2026',
          [])

NEWE = [
 dict(short='RD 210/2024 (estructura del MTDFP)', title='Real Decreto 210/2024, de 27 de febrero, por el que se establece la estructura orgánica básica del Ministerio para la Transformación Digital y de la Función Pública.',
      boe_id='BOE-A-2024-3796', consolidated_as_of='2026-06-12', temas=['I.8', 'II.2'], slug='rd-210-2024-estructura-mtdfp', date='2026-06-12',
      note='Citado en conv2025, segunda parte, reserva 4 (gestión del Centro de Información Administrativa). No estaba en C1.'),
 dict(short='Orden TDF/379/2024 (directivos públicos profesionales)', title='Orden TDF/379/2024, de 26 de abril, para la regulación de especialidades de los procedimientos de provisión de puestos del personal directivo público profesional y las herramientas para su gestión en el marco de lo dispuesto en el Real Decreto-ley 6/2023, de 19 de diciembre, por el que se aprueban medidas urgentes para la ejecución del Plan de Recuperación, Transformación y Resiliencia en materia de servicio público de justicia, función pública, régimen local y mecenazgo.',
      boe_id='BOE-A-2024-8609', consolidated_as_of='2024-04-30', temas=['I.13'], slug='orden-tdf-379-2024-directivos', date='2024-04-30',
      note='Citada en conv2024 modelo A, primera parte, 29. Sin modificaciones: la fecha es la de publicación. No estaba en C1.'),
 dict(short='Orden PCM/1382/2021 (REG-AGE)', title='Orden PCM/1382/2021, de 9 de diciembre, por la que se regula el Registro Electrónico General en el ámbito de la Administración General del Estado.',
      boe_id='BOE-A-2021-20477', consolidated_as_of='2021-12-11', temas=['II.3'], slug='orden-pcm-1382-2021-reg-age', date='2021-12-11',
      note='Citada en conv2024 modelo A, segunda parte, 9. Sin modificaciones: la fecha es la de publicación. No estaba en C1.'),
]
for n in NEWE:
    f = place_fresh(f'dl/{n["boe_id"]}-consolidado.pdf', f'{n["boe_id"]}_{n["slug"]}_{n["date"]}.pdf')
    out.append({'short': n['short'], 'title': n['title'], 'boe_id': n['boe_id'], 'url': f'https://www.boe.es/buscar/act.php?id={n["boe_id"]}',
                'consolidated_as_of': n['consolidated_as_of'], 'temas': n['temas'], 'amended_2025_2026': None, 'note': n['note'],
                'unverified': False, 'file': f, 'tags': [], 'version_vigente': {'consolidated_as_of': n['consolidated_as_of']},
                'cambios_pendientes': [], 'origen': f'descarga nueva el {TODAY} (C1 no la tiene)'})
out.append({'short': 'Resolución de la SEFP de 7 de mayo de 2024 (adecuación de puestos a la DT 6.ª del RDL 6/2023)',
            'title': None, 'boe_id': None, 'url': None, 'consolidated_as_of': None, 'temas': ['I.14'], 'amended_2025_2026': None,
            'note': 'Citada en conv2024 modelo A, primera parte, 30 (intervalo de niveles del subgrupo C2). No localizada en boe.es (búsqueda por título en la API de legislación consolidada, 2026-11-05). Probablemente publicada solo en la web de Función Pública; sin texto en sources/.',
            'unverified': True, 'file': None, 'tags': [], 'version_vigente': None, 'cambios_pendientes': [], 'origen': 'no localizada'})

for e in out:
    if e.get('boe_id') == LEY4:
        e['note'] = ('En vigor el 23-10-2026 (disposición final vigesimoctava), ya en vigor el ' + TODAY + '; las normas que modifica no la llevan en cambios_pendientes (en C1, construido el 2026-10-16, sí). '
                     'Consolidado de boe.es sin modificaciones. Se conserva la publicación original (BOE-A-2026-20528_ley-4-2026_2026-10-03.pdf).')
    e['amended_2025_2026'] = [a.replace('; boe.es ya muestra la versión futura en el texto consolidado', '; el texto consolidado ya la integra').replace('preceptos en cambios_pendientes', 'preceptos modificados') for a in (e.get('amended_2025_2026') or [])] or e.get('amended_2025_2026')
order = lambda t: (0 if t.startswith('I.') else 1, int(t.split('.')[1]))
out.sort(key=lambda e: order(min(e['temas'], key=order)))
HEADER = open('header.txt').read()
body = ''
last = None
for e in out:
    b = min(e['temas'], key=order).split('.')[0]
    if b != last:
        body += '\n# ' + '=' * 70 + f'\n# Bloque {b}. ' + ('Organización pública' if b == 'I' else 'Actividad administrativa y ofimática') + '\n# ' + '=' * 70 + '\n\n'
        last = b
    body += yaml.safe_dump([e], allow_unicode=True, sort_keys=False, width=200) + '\n'
open(C2 + '/normativa.yaml', 'w').write(HEADER + body)
json.dump({'copied': sorted(set(copied)), 'fresh': sorted(set(fresh)), 'entries': len(out)}, open('build_report.json', 'w'), indent=1)
print('entries', len(out), 'copied files', len(set(copied)), 'fresh files', len(set(fresh)))
