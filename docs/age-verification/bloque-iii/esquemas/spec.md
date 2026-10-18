# R2c esquemas, bloque III (m03-l01…m03-l07) — spec, 2026-10-18

Course `content/age-administrativo-c1` (C below). Nothing is committed. Norm texts: `pdftotext -layout` of the PDFs in
`C/sources/normativa/`, in the session scratchpad (`txt/*.txt`, and `txt/*.clean` with page headers, blank lines and
index dot-leaders removed). Lessons before this round: scratchpad `before/`.

## Rule

An esquema lays out what the prose already says (requirements § 4a; `docs/platform-delta-handoff.md`, `::esquema`).

- Every cell, node or step is a verbatim fragment of the norm, or of the lesson's own verbatim quotation of it, with
  its citation. No new fact, no reworded fact, no citation the prose does not already carry.
- Row labels and column headers name the step, figure or case («Interposición», «Conversión», «Regla general»); the
  fact sits in the other fields and is checked like a sentence. A label may carry the condition the fact depends on,
  in the norm's words, so that the row never reads wider than the article.
- An esquema follows the paragraphs it summarises and never replaces them. The prose is not touched.
- Format: `tabla` is a GFM table whose last column is the citation; `plazos` is `paso — plazo (cita)`; `pasos` is
  `paso — documento — órgano (cita)`; `arbol` is `nodo [— detalle] (cita)`, nesting as the tree. Every row names its
  norm (no implicit norm). The load fails if a row's citation is not also cited in the lesson's prose.

## Choice per lesson

One to four per lesson where the tema has lists of plazos, organs, kinds or phases that the reader must hold
together; none where the prose is narrative or already a list of its own (a list in the prose is not repeated as an
esquema). The ledger section «Esquemas bloque III» records each esquema and each list left as prose, with why.

## Verification

A reviewer who did not write the esquemas checks every row against the cited article, exactly as a sentence: is each
field a verbatim fragment (or faithful verbatim shortening that keeps every number, plazo, organ, condition and
exception)? does the row read wider than the article? is the citation right? does the lesson's prose already state
the fact (no new fact)? does the order of a `plazos` or `pasos` esquema claim a sequence the norm or prose does not
state? PASS/FAIL per row, with the passage and a replacement for each FAIL. Fixes are re-checked by another reviewer
who sees only the fixed row, the article and the prose (blind to the first verdict's reasoning).

Reports: `verify-<lesson>.md` per lesson (or group), `fixes.md`, `recheck.md`.
