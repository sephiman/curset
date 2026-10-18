# R2c esquemas, bloque IV (m04-l01…m04-l09) — spec, 2026-10-18

Course `content/age-administrativo-c1` (C below). Nothing is committed. Norm texts: `pdftotext -layout` of the PDFs in
`C/sources/normativa/`, in the session scratchpad (`txt/*.txt`, and `txt/*.clean` with page headers, blank lines and
index dot-leaders removed; `art.py <file part> <article>` prints the last heading match). Lessons before this round:
scratchpad `before/`.

Same rule, format and verification as bloque III (`../../bloque-iii/esquemas/spec.md`), with the round prompt's two
additions: kinds per subject (`tabla` for situaciones, permisos, faltas and sanciones, TREBEP-vs-earlier-rule pairs;
`plazos` for the disciplinary procedure and provisión; `arbol` for clases de personal and órganos de selección; `pasos`
for phases with a document and an organ), and no order between rows that the text does not support.

## Rule

- Every cell, node or step is a verbatim fragment of the norm, or of the lesson's own verbatim quotation or faithful
  shortening, with its citation. No new fact, no reworded fact, no citation the prose does not already carry.
- Labels and headers name the step, figure, norm or case; a label may carry the condition the fact depends on, in the
  norm's or the prose's words, so that the row never reads wider than the article.
- A pair or trio of rules from different norms (TREBEP and RD 364/1995, RD 365/1995, Ley 30/1984, RDL 6/2023; ET and
  Convenio único) goes side by side in one `tabla`, one row per norm, each with its own citation. The esquema states
  both; it does not say which applies (the prose does not either).
- In a list-type esquema a citation never ends in a letter («f)»): it cites the apartado (parser limit, platform item).
- An esquema follows the paragraphs it summarises and never replaces them. The prose is not touched: the lesson diff
  only adds lines.

## Choice per lesson

One to four per lesson where the tema has lists of plazos, organs, kinds, phases or conditions the reader must hold
together. A list or table already in the prose is not repeated as an esquema. The ledger section «Esquemas bloque IV»
records each esquema and each list left as prose, with why.

## Verification

A reviewer who did not write the esquemas checks every row against the cited article, exactly as a sentence: verbatim
fragment or faithful verbatim shortening that keeps every number, plazo, organ, condition and exception; no wider
reading than the article; right citation; fact already in the lesson's prose; no false order in a `plazos` or `pasos`
list (a numbered row put before another with no text for it); placement after the paragraphs summarised. PASS/FAIL
per row, with the passage and a replacement for each FAIL. Fixes are re-checked by another reviewer who sees only the
fixed rows, the article and the prose (blind to the first verdict's reasoning).

Reports: `verify-<lessons>.md`, `verify-m03-l05.md` (the art. 69.3 sentence and the «Efectos» column), `fixes.md`,
`recheck.md`.
