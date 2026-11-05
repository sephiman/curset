import json
from collections import Counter, defaultdict
M = {q['id']: q for q in json.load(open('work/master.json'))}
C = json.load(open('work/class_psico.json'))
EX = ['2025', '2024', '2024X', '2022', '2020', '2020X']
EXL = {'2025': '2025 ord. (A/B)', '2024': '2024 ord. (A/B)', '2024X': '2024 extr.', '2022': '2022', '2020': 'OEP 2020 ord.', '2020X': 'OEP 2020 extr.'}
txt = open('txt/2026-05-23_conv2025_modeloA_cuestionario.txt').read().split('\n')
PRESTAMOS = '```text\n' + '\n'.join(l.rstrip() for l in txt[319:335] if l.strip()) + '\n```\n\n  > Responda a las siguientes preguntas según la tabla llamada Préstamos:'

def ref(i):
    e, s, n = i.split('-')
    part = {'P1': 'parte 1', 'R1': 'parte 1, reserva'}[s]
    b = M[i]['modeloB']
    bb = f' (modelo B {b.replace("P1.", "").replace("R1.", "reserva ")})' if b else ''
    return f'{EXL[e]}, {part} {n}{bb}'

def quote(i, table=None):
    q = M[i]
    out = f'{ref(i)}; clave {q["key"].lower()}:\n\n'
    if table: out += table + '\n'
    out += f'  > {q["stem"]}\n'
    for k in 'abcd': out += f'  > {k}) {q["opts"][k]}\n'
    return out

TYPES = [
 ('tablas-lectura', 'Lectura de tablas', '2025-P1-51', PRESTAMOS,
  'Questions on a table given once before a set of six. Every exam has two such sets; in 2024 four items of the «Biblioteca» set are filing items (administrativo-clasificacion) and in 2024X the «Archivos» set is all code items (atencion-codificacion). Operations: filter on 1–5 conditions; sum by group and max/min; mean by group; ratio per row and max/min; ratio of group sums; share of a group in the total (options with 2 decimals); count of rows meeting conditions.',
  'Tables of 7–12 rows × 5–9 columns (2022 «Flores»: three linked 10-row tables). Conditions per question 1–5. Options are names from the table or numbers with 0–2 decimals. Unwritten conventions the tribunal applies: «Proyector y Megafonía» counts as «Proyector» (2020, 33); «asistentes» = alumnos + ponentes (2022 «Ponencias»).',
  'The slowest items of part 1: group sums and ratios over 10 rows without a calculator. Level 3 when the four candidate ratios are close (2025 «Desplazamientos» 57–60, 2020 «Academia», 2020X «Excursiones», 2024X «Academia»). Filter items with one row passing all conditions are level 1.'),
 ('atencion-codificacion', 'Codificación y equivalencias', '2024-P1-38', None,
  'Decode a string by an equivalence table: 4-digit binary or 0/2 blocks to letters; digits standing for letters inside a word; the value of a word when letter classes carry values (consonante mayúscula, vocal minúscula…). 2024X adds a six-position filing code with 4 values per position, asked as «cuál es FALSO/CIERTO».',
  'Binary/0-2 blocks: 6 equivalences, 4 blocks of 4 digits. Digit words: 4 equivalences, 8 characters. Letter values: 4–5 classes, words of 6–8 letters. Filing code: 6 positions × 4 values.',
  'Level 1 when the string splits cleanly into blocks; level 2 for the letter-class sums and the negative code questions.'),
 ('verbal-sinonimos', 'Sinónimos', '2025-P1-38', None,
  'One word in capitals, four single-word options, one synonym («sinónimo o afín», «significado más parecido»). 2020 and 2020X also ask «¿Qué pareja de SINÓNIMOS es INCORRECTA?» with four pairs.',
  'Four options; stem words of everyday to cultured register (HEREJE, DESLAVAZADO, ACÉRRIMO, SIBILINO). The antonym of the stem word often appears among the distractors.',
  'Level 1 for common words; level 2 when the stem word is rare (DESLAVAZADO, ACÉRRIMO).'),
 ('verbal-antonimos', 'Antónimos', '2025-P1-35', None,
  'One word in capitals, four options, one antonym («antónimo u opuesto»). Distractors are usually synonyms of the stem word.',
  'Four options. The same item can return: VENTURA → «Desdicha» is 2024 reserve 3 and 2025, 36.',
  'Nearly all level 1: three distractors are synonyms, so the odd one out is the key.'),
 ('calculo-ecuaciones', 'Ecuaciones', '2025-P1-48', None,
  '«Halla el valor de x en la siguiente ecuación»: one linear equation with a bracket.',
  'Form a(bx ± c) = dx (+ e). Coefficients up to 32, constants up to 832. The solution is an integer once (2025, 48); otherwise options carry 2 decimals (3 in 2025, 46), often negative. Two official options truncate instead of rounding (2020, 41: −0,6757 printed −0,67; 2020 reserve 2: −3,0476 printed −3,04).',
  'Level 2 by default: a division to 2 decimals by hand. Level 1 when the answer is an integer and options can be substituted.'),
 ('verbal-definicion', 'Definiciones', '2024X-P1-42', None,
  'Two directions: the word that matches a definition, or the definition that matches a word. Definitions are the DLE\'s.',
  'Four options; the words are often rare (alfaguara, hebetar, venada).',
  'Level 1–2; level 3 for rare words (hebetar, venada).'),
 ('verbal-ortografia', 'Ortografía', '2025-P1-32', None,
  'Two forms: which of four words is misspelt (or which one is right: 2025 reserve 3), and how many spelling errors a sentence has (2020, 2020X).',
  'Word form: 4 words, one wrong (b/v, h, s/x, tildes). Sentence form: 15–17 words with 4–6 errors, options are counts.',
  'Level 1 for the word form; level 2 for counting errors in a sentence.'),
 ('calculo-problemas', 'Problemas aritméticos', '2024X-P1-39', None,
  'Short word problems of 1–4 steps: capacity filling, sharing among a subgroup, unit price, sums of products, two numbers from ratio and sum, and the «operadores que faltan» item (four numbers, three gaps, a target result).',
  '1–4 steps; integer or 1-decimal results. Operator items: 4 numbers, 3 gaps. The tribunal evaluates operator items left to right, not by precedence (2022, 39).',
  'Level 1–2. Two official keys are disputed (2022, 39 and 2022 reserve 5).'),
 ('calculo-porcentajes', 'Porcentajes', '2025-P1-40', None,
  'Price after a discount or an increase, the complement of a percentage of a total, the share of a part, simple probability as a percentage.',
  'Percentages 4–64 %; bases from 45 to 47 million; options with 2 decimals.',
  'Level 1 for one multiplication; level 2 for large bases (2024X, 32) or two steps (2022, 32).'),
 ('serie-numerica', 'Series numéricas', '2025-P1-44', None,
  '«¿Qué número continúa la secuencia…?»: geometric series and interleaved series where one subsequence drives the other.',
  'Length 4–7. Rules seen: ÷3, ÷4; interleaved product (5, 3, 15, 4, 60, 5 → ×3, ×4, ×5); interleaved constant divisor or factor; sum with interleaved addends; aₙ₊₁ = 2aₙ + 3. 2020, 53 was annulled: two rules fit.',
  'Level 1 for geometric series; level 2 when interleaved.'),
 ('administrativo-clasificacion', 'Clasificación y archivo', '2020-P1-40', None,
  'Where an item is filed under a stated scheme: cabinet and drawer by type and size; drawer or folder for a surname by alphabetical ranges; shelf location of a title by topic and initial (2024 «Biblioteca»).',
  '6–8 alphabetical ranges, or 8 cabinets × 3 drawers, or a 10-row classification table with two criteria.',
  'Level 1–2. Alphabetical-range items need the ordering rules of administrativo-ordenacion.'),
 ('calculo-fracciones-proporciones', 'Fracciones y repartos', '2025-P1-43', None,
  'What remains of a total after fractions are used; proportional sharing among 3–4 parts.',
  'Denominators 8, 9 or 18; totals chosen to divide exactly (616 / 8 = 77). Sharing among 3–4 parts with 1–2 decimals.',
  'Level 1 when the total divides exactly; level 2 for proportional sharing.'),
 ('administrativo-ordenacion', 'Ordenación alfabética', '2024X-P1-46', None,
  '«¿Qué serie indica el orden alfabético correcto…?»: four orderings of the same 4–5 words.',
  '4–5 words sharing a 2–4 letter prefix; the order is decided at the 3rd–5th letter.',
  'Level 1–2.'),
 ('serie-alfanumerica', 'Series alfanuméricas', '2020X-R1-4', None,
  'Letters with digits between them that give the jump to the next letter.',
  'Length 7; jumps n = 2–5. One series wraps from Z to A (2020X); one only works counting Ñ (2020, 50: without Ñ the answer would be Q).',
  'Level 2: the alphabet convention (Ñ, wrap) decides the key.'),
 ('verbal-analogia', 'Analogías', '2020X-P1-39', None,
  '«¿Qué par de palabras NO mantiene la relación que encontramos entre A y B?»: four pairs, container–contents.',
  'Four pairs, negative stem.',
  'Level 3, and both official items have a disputed key: more than one pair breaks the relation (see the ledger).'),
 ('verbal-intrusa', 'Palabra intrusa', '2024X-P1-47', None,
  '«Señale la palabra que NO pertenece al grupo»: four words, one outside the category.',
  'Four words; one category (colectivos de animales, …).',
  'Level 1–2.'),
]
by = defaultdict(list)
for c in C: by[c['type']].append(c)
exams_of = lambda t: [e for e in EX if any(c['id'].startswith(e + '-') for c in by[t])]
assert set(by) == {t[0] for t in TYPES}, set(by) ^ {t[0] for t in TYPES}

o = []
o.append('# Psicotécnicos in the official exams — index\n')
o.append('Round R0a, 2026-11-05. Every psicotécnico question of the six distinct Auxiliar questionnaires (2025 ordinario, 2024 ordinario and extraordinario, 2022, OEP 2020 ordinario and extraordinario), part 1, questions 31–60, and the psicotécnico reserve questions. Modelo B (2025, 2024) repeats modelo A in another order: its numbers are given next to A\'s and its questions are not counted twice. There are no Auxiliar extraordinarios for 2025 or 2022 (the INAP page publishes none). Input for R6.1–R6.5 of `docs/age-auxiliar-course-requirements.md`: this index fixes which psicotécnico types exist and their weights.\n')
o.append('Classification is one pass per question (type, subtype, parameters, rule, difficulty) with every arithmetic, table and count item recomputed in Python and every verbal item decided against the DLE. The computed answer matches the official key in 192 of 193 non-annulled items; the four disputed keys and the two annulled items are listed in section 5 and in `docs/age-c2-official-exams-ledger.md`. Rendered pages of the whole psicotécnico section show no chart, drawing or picture item: the only visual content is tables. One table is an image (2024 «Cuadro Laboratorios», questions 55–60); it is transcribed in the ledger and its render is in `content/age-auxiliar-c2/sources/examenes-oficiales/renders/`.\n')
o.append('Anexo I 2.1 calls these «preguntas de carácter psicotécnico dirigidas a evaluar aptitudes administrativas, numéricas o verbales». The types below are this index\'s grouping, not an official one.\n')
o.append('## 1. Counts per type and exam\n')
o.append('Part 1, questions 31–60 plus psicotécnico reserves (2025 and 2024: reserves 3–5; 2024X: 2 and 4; 2022: 3 and 5; OEP 2020: 1 and 2; OEP 2020 extr.: 3–5). «Exams» counts the distinct questionnaires (of six) that ask the type.\n')
o.append('| Type | ' + ' | '.join(EXL[e] for e in EX) + ' | Total | Exams |')
o.append('|---|' + '---|' * (len(EX) + 2))
for t, name, *_ in sorted(TYPES, key=lambda x: -len(by[x[0]])):
    cnt = Counter(c['id'].split('-')[0] for c in by[t])
    o.append(f'| {name} (`{t}`) | ' + ' | '.join(str(cnt[e]) for e in EX) + f' | {len(by[t])} | {len(exams_of(t))} |')
tot = Counter(c['id'].split('-')[0] for c in C)
o.append('| **Total** | ' + ' | '.join(f'**{tot[e]}**' for e in EX) + f' | **{len(C)}** | |\n')
o.append('### Weights in the 30 scored questions\n')
o.append('Questions 31–60 only (no reserves): the weights R6.5 asks for («the type weights of the last official exam»). 2025 is the last one.\n')
o.append('| Type | ' + ' | '.join(EXL[e] for e in EX) + ' |')
o.append('|---|' + '---|' * len(EX))
for t, name, *_ in sorted(TYPES, key=lambda x: -len(by[x[0]])):
    cnt = Counter(c['id'].split('-')[0] for c in by[t] if '-P1-' in c['id'])
    o.append(f'| {name} | ' + ' | '.join(str(cnt[e]) if cnt[e] else '–' for e in EX) + ' |')
o.append('')
o.append('Every exam has two six-question sets on a table (12 of 30). In 2025, 2022 and both OEP 2020 exams all 12 are table reading. In 2024 four of the twelve are filing-location items on the «Biblioteca» table; in 2024X the second set is six code items on a filing-code table. Outside the tables, verbal items take 7–9 of the 30 questions and calculation (cálculo plus series) 3–9; codes and filing/ordering items fill the rest.\n')
o.append('## 2. First generator batch: recurring types\n')
o.append('Recurring = asked in 3 or more of the six questionnaires. These go to the first generator batch (R3p); the rest wait for the open decision 1 of the requirements.\n')
o.append('| Type | Exams | Questions | First batch |')
o.append('|---|---|---|---|')
for t, name, *_ in sorted(TYPES, key=lambda x: (-len(exams_of(x[0])), -len(by[x[0]]))):
    n = len(exams_of(t))
    o.append(f'| {name} (`{t}`) | {n}: {", ".join(EXL[e] for e in exams_of(t))} | {len(by[t])} | {"yes" if n >= 3 else "no"} |')
o.append('')
o.append('Types that R6.1 of the requirements lists and that no Auxiliar questionnaire of 2020–2025 asks: counting symbols, finding differences and comparing copied data (attention and perception other than codes), error detection in copied records, spatial reasoning, logical reasoning (syllogisms, order puzzles). They have no official example to copy a style from.\n')
o.append('## 3. Types\n')
o.append('Each type: what is asked, the parameters that vary inside the type, the difficulty note, and one official question verbatim with its definitive key. Difficulty is the classifier\'s 1–3 for a C2 candidate without a calculator (90 minutes for 110 questions).\n')
for t, name, ex, table, what, params, diff in TYPES:
    dc = Counter(c['difficulty'] for c in by[t])
    subs = Counter(c['subtype'] for c in by[t])
    o.append(f'### {name} (`{t}`) — {len(by[t])} questions, {len(exams_of(t))} exams\n')
    o.append(f'**What is asked.** {what}\n')
    o.append(f'**Subtypes** (classifier\'s labels): ' + '; '.join(f'{k} ({v})' for k, v in subs.most_common()) + '.\n')
    o.append(f'**Parameters.** {params}\n')
    o.append(f'**Difficulty.** Levels 1/2/3: {dc[1]}/{dc[2]}/{dc[3]}. {diff}\n')
    o.append('**Example.** ' + quote(ex, table))
    o.append('Questions: ' + ', '.join(f'{c["id"]}' for c in by[t]) + '.\n')
o.append('## 4. Format\n')
o.append('- Four options, one correct, as in bloque I. Options are one word or one number in most types (mean option length 1–3 words).')
o.append('- Stems are short (mean 17–23 words), except table items, which add the table once before the set and repeat «según los datos del cuadro…» or «Responda a las siguientes preguntas según la tabla llamada…».')
o.append('- Numbers use the Spanish decimal comma and thousands point; money as «41,40 €», percentages as «25,83 %».')
o.append("- Psicotécnico items are questions 31–60, grouped by kind. Since 2022 the two table sets close the section (49–60); in the OEP 2020 exams the table sets sit in the middle (2020: 31–36 and 44–49; 2020 extr.: 46–51 and 55–60). The part-1 reserve mixes bloque I and psicotécnico items.")
o.append('- No calculator (cover instructions of the OEP 2020 questionnaires: «no puede utilizar calculadora ni ningún otro dispositivo electrónico»).\n')
o.append('## 5. Keys, notes and anomalies\n')
for c in C:
    if c['status'] != 'vigente' or c['nota_clave'] or c['nota']:
        extra = ('Anulada en la plantilla definitiva. Lectura de la ronda: ' + c['rule'] + '.') if c['status'] == 'anulada' else ''
        o.append(f'- {c["id"]} ({c["type"]}), {c["status"]}. ' + ' '.join(x.rstrip('.') + '.' for x in [extra.rstrip('.'), c['nota_clave'], c['nota']] if x))
o.append('')
o.append('Repeated items: 2024X reserve 4 is identical to 2024X, 36. 2024 reserve 3 (antónimo de VENTURA) repeats 2025, 36.\n')
open('/home/juanjo/PycharmProjects/curset/docs/age-c2-psicotecnico-index.md', 'w').write('\n'.join(o) + '\n')
print('ok', len(o))
