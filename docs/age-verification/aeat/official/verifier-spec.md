# Blind check of the «Exámenes oficiales» exercises (R5)

You verify built quiz exercises against the official PDFs. You do not edit content: you only write your report.
Work in `/home/juanjo/PycharmProjects/curset`. Run `pdftotext -layout <pdf> -` to read a PDF; if a sheet or a table
reads badly, render the page (`pdftoppm -r 110 -png -f N -l N <pdf> /tmp/x`) and look at the image.

## Inputs, per exam in your list

- Questionnaire: `content/aeat-agentes-hacienda/sources/examenes-oficiales/*_conv<YEAR>[_extraordinario]_tipo<A|B>_cuestionario.pdf`.
- Answer sheet beside it: `*_plantilla-definitiva.pdf` (the 2022 extraordinario: `*_plantilla-provisional.pdf`, which the
  Tribunal declared definitive «sin modificación alguna»). The header of the OEP 2022 sheets reads «PROVISIONAL»; their
  content carries the annulments, so use them.
- Built exercise: `content/aeat-agentes-hacienda/exercises/ofi-conv<YEAR>-<a|b|x>.yaml`. Each variant's `tags` are
  `[convYEAR_TIPO, Qn]`, with `n` the number printed in that paper.
- Ledger: `docs/aeat-official-exams-ledger.md`, section of the OEP. It lists tipo A only; its «Tipo B» column gives the
  tipo B number of the same question. Statuses: `vigente` and `vigente-con-nota` are included; `anulada`,
  `norma modificada`, `fuera de temario` are excluded.

## What to check, for every variant

1. **Stem**: identical to the printed stem (word for word, punctuation included). Ignore line breaks, runs of spaces and
   the question number/marker. The papers contain their own typos: a printed typo must be kept, and a YAML that «fixes»
   it is a FAIL.
2. **Options**: four options, same texts and same order as printed; the letters are the printed ones (A–D = a–d).
3. **Key**: the option with `correct: true` has the letter the answer sheet gives for question `n`. Read the sheet
   yourself, not the ledger.
4. **Note** (variants with an `explanation`): the question is `vigente-con-nota` in the ledger, the note is the ledger's
   «Nota de clave» (plus an «Errata» sentence of the Nota column), and its letter references fit this paper's options.
   A variant without an explanation must not be `vigente-con-nota`.

## What to check, per exam

5. Every printed number missing from the YAML is excluded in the ledger (tipo B: through the «Tipo B» column; a number
   printed twice in the paper maps to the row the ledger names), and the sheet says `ANULADA` where the ledger says
   `anulada`. No included ledger row is missing.
6. Count: printed questions = YAML variants + excluded.

## Report

Write `docs/age-verification/aeat/official/verify/report-<exam slug>.tsv` per exam, header
`exam<TAB>tag<TAB>check<TAB>verdict<TAB>detail`: one row per FAIL (check is stem, options, key, note, excluded or
count; detail quotes the PDF text and the YAML text that differ), and a last row `<slug> SUMMARY` with the numbers of
variants checked and of FAILs. A PASS needs no row. Do not guess: if you cannot read something, say so in a row with
verdict `UNREAD`. Finish with one line per exam: variants checked, FAILs, UNREADs.
