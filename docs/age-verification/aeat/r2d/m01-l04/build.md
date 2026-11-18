# Build — I.4 (`m01-l04`), 2026-11-17

Builder: Sonnet. Method: HEAD text kept; whole pool sentences added byte-identical; esquema rows built from pool
items. Scratch build script: `/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/82b57970-32c9-4fcd-9a63-714f54d4eded/scratchpad/b-m01-l04/build.py`.

## Size

| | words |
|---|---|
| HEAD (`wc -w`) | 9684 |
| built, whole file | 31149 |
| built, esquema rows excluded (all `:::esquema` rows, new and old) | 21799 |
| esquema rows only | 9350 |

Ratio excl. rows to HEAD: 2.25. Ratio to the 1.6 target (15494): 1.41. The target is passed: the range is 179
article rows, 76 of them «not treated» in HEAD; every added article is kept to its rule/conditions/exceptions
sentences and every enumeration is an esquema (rows excluded from the count).

## Sentences added

Non-row sentences: 403 byte-identical from the pool. (a) 6 · (b) 6 · (c) 361 · (d) 9 · (e) 21. Esquema rows: 302
(rows from pool items, or from HEAD items), plus the HEAD esquemas untouched.

- (a) art. 18 TUE: 18.1, 18.3, 18.4 (R2b removal).
- (b) review item 13, arts. 156–158 CE: 156.2, 157.2, 157.3, 158.1, 158.2 and the 157.1 lead-in/rows (not in pool).
- (c) every other article of the ranges (arts. 156–158 aside): CE DA 1.ª, DA 3.ª, DT 4.ª, 142, 149.2, 151.3, 152.1
  párr. 2–3, 152.3; Estatutos arts. 3–5, 7–19, 21–24, 26–27, 29–40, DA, DT 3.ª; LBRL arts. 1–2, 4–10, 13–14, 16–18,
  19.3, 20.1.c)/20.2–3, 23.4, 24, 24 bis, 25–30, 32–38, 41.2, 42–44, 121.1; TUE 13.1, 13.3, 17.1–17.3, 17.6–17.7,
  19.1–19.3; TFUE arts. 223–228, 230, 232–233, 236–242, 244–246, 248–249, 251, 253–281.
- (d) three «No confundir» blocks (Consejo Europeo / Consejo; art. 153.b / art. 155.1; art. 26.1 / art. 36.1.c LBRL).
- (e) HEAD sentences replaced by their pool version: 149.1 lead, «El examen mezcla materias de las dos listas:»,
  14.2 and 18.1 Estatutos, leads of 21.1, 22.1 (+ 21.2, 22.2 completed), 16.6 TUE (two formations), 17.2, 17.6, 258,
  263 TFUE, 50 ter, the Parlamento/Comisión rows of the sedes table, art. 36.1 and 25.2 leads.
- HEAD sentences not carried (replaced by the esquemas that hold their content in full): the five-pair comparison
  table of arts. 148.1/149.1 (the paragraph before it stays), «Aquí van diecisiete», «Entre sus funciones están»,
  «entre otras materias» ×2, «Entre sus atribuciones están», «entre otras», «entre otras atribuciones», «Entre ellas
  están», «entre otras, estas» (36.1), and the five old Normativa lines.

## Enumerations as esquemas

arts. 149.1 CE; 151.2 CE; 157.1 CE; 5.2, 12.1, 18.2, 21.1, 22.1, 35.1, 36, 37.2, DA 3.ª (revision cases) of the
Estatutos; 4.1, 16.2, 18.1, 121.1 (title X), 21.1, 21.3, 22.2, 25.2 (a)–p) plus q) from the Ley 4/2026 sentence),
26.2, 27.3, 33.2, 34.1, 36.1, 36.2, 44.3 LBRL; 244, 263, 267 TFUE; art. 50 ter Estatuto TJUE. Multi-sentence items
give one row per sentence under the same marker (a row must be one verified sentence). The lists whose items each
cite their own article (arts. 269–273 TFUE, 17.1, 17.6, 17.7, 16.6 TUE) and the HEAD lists that were already
complete (143.1, 144, 147.2, 148.1, 152.1, 153 CE, 13.1 TUE, 6 Estatutos) stay prose lists.

## Checks

- build_check: `m01-l04: HEAD 374 · added byte-identical 435 · esquema rows from items 302 · not in pool 10`
- cites.py: 793 citations, 0 unresolved. `index_sources.py --course aeat-agentes-hacienda`: exit 0, no validation error.
- split_paragraphs: 18 paragraphs split.
- Every esquema row's citation cell appears in the prose (checked before writing the lesson file).

## «not in pool» (10)

Kept because dropping them breaks a complete enumeration, or they are new Normativa lines:
1. art. 151.2 CE 4.º, two rows: «Los plenos de ambas Cámaras deciden sobre el texto mediante un voto de ratificación.»
   and «Aprobado el Estatuto, el Rey lo sanciona y lo promulga como ley.» (no PASS verdict).
2. art. 157.1 CE: the lead-in and rows a), c), d) (no PASS verdict; b) and e) matched a verified sentence).
3. Four Normativa lines: CE, LOREG, TRLRHL, the closing «no figuran en `normativa.yaml`» line (rebuilt from what
   the lesson cites; the pool has the same lines without a PASS verdict).

## Pool sentences left out (reason per sentence)

- 156.1 CE «Las Comunidades Autónomas gozan de autonomía financiera…» (no PASS verdict, not an enumeration).
- Estatutos art. 8: «Tanto en la documentación…» and «La circunscripción electoral es el término municipal…» (no PASS
  verdict; the other art. 8 sentences give the rule).
- art. 18.2 TUE «Está al frente de la política exterior…» (no PASS verdict) and «Actúa del mismo modo…» (it refers to
  the first, would not stand alone).
- LBRL 13.1 «Simultáneamente a la petición del dictamen…» (procedure); 17.2–17.4 (INE, Consejo de Empadronamiento:
  organisational detail, the map allows it); 25.4 last sentence (informe del Ministerio: procedure); 27.1 memoria
  económica sentence (repeats 27.1 párr. 2); 36.2.a) five sentences (plan content, financing, coordination,
  subsidies: development of the plan); 
- DA 3.ª Estatutos «Para determinar la financiación que en cada año del quinquenio…» (procedure of the
  evolution rules).
- 255 TFUE «El Consejo adopta una decisión por la que se establecen las normas de funcionamiento del comité…»;
  257 TFUE «Se pronuncian mediante reglamentos…» and «El reglamento fija las normas relativas a la composición…»
  (procedure).
- 17.7 TUE «Las demás personalidades se seleccionan a partir de las propuestas…» (repeats HEAD).
- 228.1 TFUE «Cuando comprueba un caso de mala administración, lo pone en conocimiento…» (procedure).

## Pool gaps (article of the range with no PASS sentence left)

- art. 156.1 CE (only its non-PASS sentence exists in the pool; 156.2 is treated).
- art. 18.2 TUE (same).

## Sentences that do not stand on their own where they now sit

- Rows that continue an item under the marker of the item (the splitter makes each sentence one row): e.g. 149.1
  8.ª, 16.ª, 23.ª second sentences; 151.2 4.º and 5.º; 21.1 Estatutos 24 «Policía local en los términos…»; 22.1 2.ª
  «Defensa de los consumidores y usuarios.»; 36.9.º «El alcance y términos de la cesión los determina la ley.»;
  21.1 LBRL h) «Esta atribución se entiende sin perjuicio…» and 34.1 LBRL h) (same); 25.2 LBRL a), g), n) second
  sentences; 36.1 LBRL b), c), h) second sentences.
- Prose sentences that refer to the esquema just above them: «Esas potestades pueden aplicarse…» (4.2 LBRL),
  «En esas materias, la competencia…» (21.2, 22.2 Estatutos), «En los supuestos de los párrafos c) y d)…» (121.1),
  «Los párrafos ñ) y p) … están derogados» and the same for 22.2, 33.2, 34.1.
- «Estos requisitos deben cumplirse…» (143.2, HEAD), «Se hace mediante medidas…» (28 LBRL), «Para ello son
  necesarios y vinculantes los informes…» (7.4 LBRL).

## New Normativa lines (not in pool)

CE (adds the 18.1/105 «nombrado» marks as the pool line has them), LOREG, TRLRHL, closing line: as the pool lines
`CE: arts. 2, 18.1 …`, `LOREG …`, `TRLRHL …` and the final `no figuran en normativa.yaml` line, no new wording.
