# R2c esquemas, bloques I (m01-l01…m01-l11) and II (m02-l01…m02-l04), and the bloque V open items — spec, 2026-10-18

Course `content/age-administrativo-c1` (C below). Nothing is committed. Norm texts: `pdftotext -layout` of the PDFs in
`C/sources/normativa/` and `C/sources/otros/` (the latter prefixed `otros-`), and a tag-stripped text of the Ley
31/2022 HTML (`ley31.txt`), in the session scratchpad `txt/`; `art.py <file part> <heading regex> [lines]` prints an
article body with page headers removed. HTML sources (`sources/otros/*.html`, the Ley 31/2022) are read directly.
Lessons before this round: scratchpad `before/`. Bloque II uses this spec; its reports go to `../../bloque-ii/esquemas/`.

Same rule, format and verification as bloques III–V (`../../bloque-iii/esquemas/spec.md`,
`../../bloque-iv/esquemas/spec.md`, `../../bloque-v/esquemas/spec.md`), with the round prompt's choices per subject.

## Rule

- Every cell, node or step is a verbatim fragment of the norm, or of the lesson's own verbatim quotation or faithful
  shortening, with its citation. No new fact, no reworded fact, no citation the prose does not already carry; no order
  the text does not support; one norm per row.
- Labels and headers name the step, organ, figure, norm or case; a label may carry the condition the fact depends on,
  in the norm's or the prose's words, so that the row never reads wider than the article.
- Where the prose has the same gap as a row (a condition or exception of the article that the prose leaves out), the
  row is removed and the gap listed in the ledger. The bloque I–II prose is not touched.
- `plazos` renders as a timeline and `pasos` as a numbered stepper: both claim an order. A row may only follow another
  when the norm or the prose says so. An `arbol` claims dependency: a child node sits under a parent only when the text
  says it belongs to, depends on or is part of it.
- A title must not make a selective list read as complete.
- An esquema follows the paragraphs it summarises and never replaces them. One to four per lesson; none where the
  prose is narrative or already a list or table of its own.
- Non-normative sources (`sources/otros/`, I.6 and I.11): a row may cite the file only if the prose cites the same
  file for the same fact, and keeps the prose's «a fecha de».

## Choices per subject (round prompt)

- Bloque I: `arbol` for the Cortes, the Gobierno, the Poder Judicial, the AGE's organs (central and periférica) and the
  EU institutions; `tabla` for majorities and plazos (reforma constitucional, leyes orgánicas, moción de censura and
  cuestión de confianza, estados de alarma/excepción/sitio, article per row), for the derechos fundamentales and their
  guarantees, and for the Comunidades Autónomas' competences; `plazos` for the legislative procedure and the
  investidura. Bloque I is 11–13 part-1 questions per exam, almost all organs, majorities and plazos
  (`docs/age-exam-style.md` §§ 2–3): those come first.
- Bloque II: `pasos` for registro and atención al ciudadano; `tabla` for the derechos of art. 13 LPAC and of the
  RGPD/LOPDGDD (derecho, artículo, plazo de respuesta); `arbol` for the administración electrónica organs and systems.
- Where the text cannot carry the kind asked (no stated order, a fact the prose lacks, a citation the grammar cannot
  read), the writer changes the kind or drops the esquema and says why in the ledger.

## Platform limits (from bloques III–V)

- A row's citation is parsed as one segment naming one norm: «art. 134.4 CE; art. 38.1 LGP» does not resolve.
- A list-row (`plazos`, `pasos`, `arbol`) citation cannot end in a letter written «f)»: cite the apartado without the
  letter. Tables may cite the letter.
- An article ending in an uppercase letter and «)» («art. 21.C)») closes the citation and takes the previous norm.
- «regla … IOC» and ordinal «apartado sexto…» are not citation leads.
- The list field separator is « — »: no em dash with spaces inside a field. `plazos` rows have 2 fields, `pasos` 3,
  `arbol` 1–2.
- The load fails when a row cites a norm and article the prose does not cite (matched by anchor: norm + article).
- Glossary marks see esquema text as prose: a label that writes a glossary term can move its first mark or spend a
  book's single PDF link; every mark that moves or appears is reported.

## Bloque V open items (closed first)

1. m05-l02, art. 10.Seis Ley 31/2022: the prose states the MRR exception as the law does (servicio 50 of each sección;
   MRR credits of the entidades of art. 1.a) 2.º–4.º); the «Incorporación, durante la vigencia de la Ley 31/2022» row
   returns.
2. m05-l06, art. 34.5 LGS: a verbatim sentence, cited; the «Del gasto al pago de la subvención» table (art. 34.1–5).
3. m05-l04: «(art. 23.Uno.B Ley 31/2022)» and «(art. 23.Uno.D Ley 31/2022)»; both now open Ley 31/2022 (`#a2-5`) in
   `citations.es.txt`; the Ley 31/2022 row of the pagas table returns and the title names the three norms.

Each is checked blind like an R2 sentence or row (`verify-m05.md` in this folder).

## Verification

A reviewer who did not write the esquemas checks every row against the cited article, exactly as a sentence: verbatim
fragment or faithful verbatim shortening that keeps every number, plazo, organ, majority, condition and exception; no
wider reading than the article; right citation; fact already in the lesson's prose; no false order in a `plazos` or
`pasos` list and no false dependency in an `arbol`; title not reading a selective list as complete; placement after
the paragraphs summarised. PASS/FAIL per row, with the passage and a replacement for each FAIL; a FAIL whose
replacement would need a clause the prose lacks says so. Fixes are re-checked by another reviewer who has not seen
the first report and appends to a new file (`recheck.md`), never the first reviewer's.

Reports: bloque I `verify-m05.md`, `verify-m01-<lessons>.md`, `fixes.md`, `recheck.md` here; bloque II the same names
under `../../bloque-ii/esquemas/`.
