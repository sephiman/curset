# R2c esquemas, bloque V (m05-l01…m05-l06), and the bloque IV open items — spec, 2026-10-18

Course `content/age-administrativo-c1` (C below). Nothing is committed. Norm texts: `pdftotext -layout` of the PDFs in
`C/sources/normativa/` (and a tag-stripped text of the Ley 31/2022 HTML), in the session scratchpad `txt/*.txt`;
`art.py <file part> <heading regex> [lines]` prints an article body with page headers removed. Lessons before this
round: scratchpad `before/`.

Same rule, format and verification as bloques III and IV (`../../bloque-iii/esquemas/spec.md`,
`../../bloque-iv/esquemas/spec.md`), with the round prompt's additions: kinds per subject (`tabla` for modificaciones,
créditos, indemnizaciones and the clasificación del gasto; `pasos` for the fases del gasto, pagos a justificar and
anticipos de caja fija; `plazos` for the budget cycle and the justificación de libramientos; `arbol` for the estructura
de los PGE), no order between rows that the text does not support, and a list-type row cites the apartado without
the letter.

## Rule

- Every cell, node or step is a verbatim fragment of the norm, or of the lesson's own verbatim quotation or faithful
  shortening, with its citation. No new fact, no reworded fact, no citation the prose does not already carry.
- Labels and headers name the step, figure, norm or case; a label may carry the condition the fact depends on, in the
  norm's or the prose's words, so that the row never reads wider than the article.
- Where the prose has the same gap as a row (a condition or exception of the article that the prose leaves out), the
  row is removed and the gap listed in the ledger; the bloque V prose is not touched.
- Rules of two norms for the same act sit side by side in a `tabla`, one row per norm. The esquema does not say which
  applies.
- `plazos` renders as a timeline and `pasos` as a numbered stepper: both claim an order. A row may only follow another
  when the norm or the prose says so.

## Platform limits found this round (they decide some kinds)

- A row's citation is parsed as one segment: it names one norm. «art. 134.4 CE; art. 38.1 LGP» does not resolve.
- «regla … IOC» and «apartado sexto…» (an ordinal word) are not citation leads, so no row can rest on the Instrucción de
  operatoria contable or on the Orden de documentos contables / Orden PRE/1576/2002 apartados. The documentos
  contables of each fase stay in the prose table of m05-l03.
- A prose citation whose article ends in an uppercase letter and «)» («art. 21.C)», «art. 23.Uno.B)») closes there and
  takes the previous citation's norm.

## Bloque IV open items (closed first)

1. Prose sentences, verbatim or faithful shortenings, cited: m04-l02 (33 % threshold and the DA 19.ª conditions of the
   former 5 % cupo), m04-l03 (relación complementaria, art. 61.8 párr. 2 TREBEP and art. 114.10 párrs. 2–3 RDL
   6/2023), m04-l05 (disposición final cuarta.1 TREBEP on art. 18). Each is checked blind like an R2 sentence (facts
   against the norm, voice page).
2. The rows and the table that bloque IV removed for those gaps come back and are checked like any row.
3. «(art. 21.C) Real Decreto 1009/2023, …)» in m04-l01 and m04-l03 becomes «(art. 21.C RD 1009/2023)»; both now resolve
   to RD 1009/2023 (`citations.es.txt`). m04-l01 gains the `arbol` of the Secretaría de Estado de Función Pública.

## Verification

A reviewer who did not write the esquemas checks every row against the cited article, exactly as a sentence: verbatim
fragment or faithful verbatim shortening that keeps every number, plazo, organ, condition and exception; no wider
reading than the article; right citation; fact already in the lesson's prose; no false order in a `plazos` or `pasos`
list; placement after the paragraphs summarised. PASS/FAIL per row, with the passage and a replacement for each FAIL;
a FAIL whose replacement would need a clause the prose lacks says so. Fixes are re-checked by another reviewer who sees
only the fixed rows, the article and the prose.

Reports: `verify-m04.md`, `verify-m05-l01-l02.md`, `verify-m05-l03.md`, `verify-m05-l04-l06.md`, `verify-m05-l05.md`,
`fixes.md`, `recheck.md`.
