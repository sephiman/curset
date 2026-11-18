# Build — `m03-l19` (III.19, IVA II), 2026-11-17, restart after the stopped first builder

## Size

| | words |
|---|---|
| HEAD, excluding esquema rows | 9211 (wc -w 9706 with the HEAD esquema) |
| Built, excluding esquema rows | 16425 (wc -w 33361 with the esquemas) |
| Esquema rows, built | 16544 (HEAD: 481) |

Ratio to HEAD (excl. rows): 1.78. Ratio to the 1.6 target: 1.11. Over target by completeness: the range is 89 articles
and every article keeps the sentences that state its rule, conditions and exceptions; every legal enumeration is an
esquema (40 esquemas, rows excluded from the size).

## How it was built

Base: HEAD (`git show HEAD:…`). Sentence set: the pool in its own order (the pool already states every apartado in the
law's words). The 95 HEAD sentences that the pool holds byte-identical stay as they were (intro, examples, «Lo que más
cae», the HEAD esquema «Algunos plazos…», the flat lists 79.Tres, 9.1.º c), 106.Uno). Lists were turned into esquemas
by a script from the pool's list lines (one row per sentence of an item or sub-item; label = `2.º`, `2.º a)`,
`2.º a) a´)`, `c) guion 2`; citation cell = the lead-in's unit; an item's trailing inline citation is cut from the row,
which leaves a verbatim contiguous part of the verified item). 36 of the 40 are new from pool lists.

## Sentences added (704: 307 prose, 397 esquema rows)

- (a) R2b removals: 0 (the map has none for this tema).
- (b) Review items: about 48 (art. 79.Cinco–Nueve vinculación and comisión; art. 87 Dos–Cinco with the esquemas for
  Dos and Cinco.2; art. 89.Tres 1.º–2.º and 89.Cinco incl. a)–b)).
- (c) Articles HEAD did not treat or treated in part: about 650 sentences/rows (arts. 75–77, 78.Dos.3.º, 79–83,
  84.Uno.2.º a´)–e´) and guiones, 86.Dos–Tres, 88.Uno, 93.Tres, 94, 95.Tres.2.ª second paragraph and 5.ª, 96, 97–99,
  101–105, 107, 110–114, 115–119 bis; RIVA 23 bis, 24, 24 bis, 24 ter, 25, 27, 28, 29, 30, 31, 32; RD 1619/2012 art.
  15). Enumerations as esquemas: 75.Uno (incl. 2.º bis, 5.º a)–e), 8.º a)–d)), 78.Dos, 78.Tres, 79.Cinco (three), 80.Uno,
  80.Cuatro, 80.Cinco, 24.2 RIVA, 83.Uno, 83.Dos, 84.Uno (incl. 2.º a)–g) and sub-items), 86.Dos, 87.Dos, 87.Cinco,
  89.Tres, 89.Cinco, 92.Uno, 94.Uno, 95.Dos, 95.Tres, 95.Cuatro, 96.Uno, 96.Dos, 97.Uno, 103.Dos, 104.Dos, 104.Tres,
  28.1 RIVA, 108.Dos, 110.Uno, 112.Tres, 114.Dos, 27.2 RIVA, 119.Dos, 119 bis.Uno, 30.3 RIVA, 31.1 RIVA.
- (d) «No confundir»: 3 blocks (87, 89/88, 103/107), as the pool has them.
- (e) HEAD sentences replaced by their pool form: 185 of HEAD's 280. They are HEAD's paraphrases of the same apartado
  (list items, `con el plazo que el propio apartado fija`, `salvo en los casos que el propio apartado enumera`, `entre
  otros supuestos` at art. 75.Uno), now stated in the law's words, so no apartado is stated twice. Also: the
  `m03-l18` id in the III.18 remisión (the pool version has the tema number alone); the «Fuera del enunciado
  literal…» note on arts. 97–100 is gone (coordinator notes); the three HEAD «Normativa» lines are rebuilt.

## Pool sentences left out (25), each because it states no rule, condition or exception

- Art. 79.Cinco: «La vinculación podrá probarse por cualquiera de los medios admitidos en derecho» (evidence means).
- Art. 87.Cinco.2: «Para la calificación del precio … estudiará la documentación …» (procedure).
- Art. 15.4 RD 1619/2012: «El Departamento de Gestión Tributaria … podrá autorizar otros procedimientos …»
  (procedure); art. 15.5: «En particular, los datos que se regulan en los párrafos f) y h) …» and «Cuando lo que se
  expida sea una factura simplificada rectificativa …» (how the data express the rectification: development).
- Art. 101.Dos: «Reglamentariamente se establecerán los requisitos y el procedimiento …» (pointer).
- Art. 28.2 RIVA: «Las solicitudes, la renuncia, y la opción y revocación … se formularán … ante el órgano competente»
  (procedure).
- Art. 27.2 RIVA: «La acreditación … por cualquiera de los medios de prueba admitidos en derecho» (evidence means).
- Art. 115.Tres: «Reglamentariamente se determinarán el procedimiento y la forma de pago …» (pointer).
- Art. 117 bis: «La recepción y la tramitación … reglamentariamente» (pointer).
- Art. 119.Siete: «La Administración tributaria, en el procedimiento específico …, podrá exigir … información
  adicional» (procedure); «La tramitación del procedimiento de devolución se regirá …» (pointer); «La falta de pago
  … medidas cautelares … artículo 81 LGT» (procedure).
- Art. 119 bis.Dos: «La tramitación del procedimiento de devolución se regirá …» (pointer).
- Art. 30 RIVA: 30.2 «El registro … se gestionará por la Agencia Estatal …» (management); 30.11 two sentences
  (compatibilidad con el servicio de notificaciones electrónicas); 30.12 «La devolución … exclusivamente por
  transferencia bancaria …» (payment procedure).
- Art. 31 RIVA: 31.7 five sentences (requerimiento de información adicional o ulterior, originales de facturas, plazo
  de un mes: procedure); 31.10 (recurso); 31.11 (idioma).

## Esquemas

40 in all: 36 built from pool lists, the HEAD «Algunos plazos…» (kept) and the three «No confundir» are notes, not
esquemas. HEAD flat lists kept as bullets: 79.Tres (3 items, HEAD's own text, no lead-in in the pool), 9.1.º c)
a´)–d´), 106.Uno 1.ª–3.ª, the two worked examples, «Lo que más cae», «Normativa». Row cells carry the pool item's text
without its marker and without its trailing inline citation; the citation cell repeats the lead-in's unit, so finer
units named only inside an item (e.g. 84.Uno.2.º.e), 75.Uno.8.º) are no longer cited as such in the rows. HEAD's
«Lo que más cae» cites 75.Uno.1.º, 75.Uno.4.º, 78.Dos.1.º/.3.º/.6.º, 80.Cuatro.A, 80.Cinco.1.ª, 84.Uno.2.º.e),
93.Cuatro, 95.Tres.2.ª, 99.Tres–Cuatro, 103.Dos.2.º and 104.Tres.3.º, which keep those units in prose.

## Pool gaps (no prose of my own)

- Art. 30 bis RIVA, art. 30 ter RIVA, art. 31 bis RIVA: no sentence in the verified pool (the pool's «RIVA» range is
  23 bis, 24–25, 27–32 only 30.1–30.12, 31.1–31.11, 32.1–32.2). Need a writer + verifier round.
- Art. 9.1.º c) c´): «a que remite el propio precepto» stays; no pool sentence names DA 3.ª Ley 10/2014.
- «Lo que más cae» line 8 keeps «entre otros» (HEAD's ten lines, no pool version; art. 95.Tres.2.ª a)–f) is now whole
  in the esquema). Fix needs new text.

## Sentences that do not stand on their own where they now sit

- Art. 31.8 RIVA «No obstante, cuando sea necesaria la solicitud de información adicional o ulterior …» and «En todo
  caso, cuando sea necesaria la solicitud de información adicional …»: the 31.7 sentences that introduce those
  requests are left out (procedure).
- Art. 119.Seis «No obstante, no se devengarán intereses de demora si el solicitante no atiende … los requerimientos de
  información adicional o ulterior»: antecedent in 119.Siete, left out.
- Art. 28.2 RIVA «En el caso de las citadas solicitudes, la Administración dispondrá del plazo de un mes …»: «las
  citadas solicitudes» pointed to the left-out first sentence of 28.2; they are now the 28.1 rows.
- Esquema rows that begin «No obstante …», «Lo dispuesto en el párrafo anterior …», «A efectos de las letras a) y b)
  anteriores …» (75.Uno.1.º, 2.º, 7.º, 8.º; 80.Cuatro, 80.Cinco, 114.Dos): they refer to the preceding paragraph of
  the same item, which is the row above with the same label.
- The HEAD sentence «En consecuencia, el pago anticipado …» was moved to follow art. 75.Dos (it followed 75.Dos in
  HEAD; 75.Tres and 23 bis RIVA now come after it).

## Checks

- build_check: `m03-l19: HEAD 95 · added byte-identical 344 · esquema rows from items 358 · not in pool 2`.
- «not in pool» (2, both new «Normativa» lines): `RIVA (RD 1624/1992): arts. 23 bis, 24.1–24.3, 24 bis, 24 ter,
  25.1, 27.1–27.4, 28.1–28.2, 29, 30.1, 30.3–30.10, 31.1–31.6, 31.8–31.9, 32.1–32.2, 61 bis.5, 71.5 y 78.` and the
  `LGT (Ley 58/2003): …` line without «art. 81» and «título V, nombrado en el art. 31.10 RIVA».
- New «Normativa» lines (the one place for new text): RIVA line (30.1, 30.3–30.10, 31.1–31.6, 31.8–31.9 for the left-out
  articles' numbers) and LGT line as above; the «Concierto Económico … Convenio Económico» line is removed (named only
  in the left-out 30.2 RIVA). The LIVA line and the others are the pool's own.
- cites.py: 710 citations, 0 unresolved.
- split_paragraphs: 3 paragraphs split on the first run, 0 on the last.
- index_sources (`--course aeat-agentes-hacienda`): ran to the end, exit 0, no validation error.
