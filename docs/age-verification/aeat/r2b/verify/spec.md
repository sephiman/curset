# Blind check of the R2b and R2c edits (AEAT) — verifier spec, 2026-11-11

You did not write these edits. Course `content/aeat-agentes-hacienda`. Read once: this file;
`docs/age-verification/aeat/r2c/spec.md` (sections «Rule», «Syntax», «Verifier»); `docs/age-verification/bloque-i/esquemas/spec.md`
(«Rule», «Verification»); `docs/prose-voice.md`. Norm texts: `content/aeat-agentes-hacienda/sources/normativa/` (`pdftotext
-layout <file> -`; `.html` files: strip tags with `python3 -I`). The snapshot is the source of truth, never memory. Edit
nothing except your report(s).

## What is pending

Per lesson, the pending file lists every sentence or row with neither provenance nor a PASS:
`docs/age-verification/aeat/r2-tax/<lesson>/pending.md` (m03) and `docs/age-verification/aeat/r2/pending/<lesson>.md`
(m01, m02). Each has an id (10 hex), its line and text. Kinds:

1. **Esquema rows and table headers** (new): check as the R2c spec «Verifier» says — verbatim or faithful shortening
   keeping every number, plazo, organ, condition and exception; no wider reading than the article; right citation; the
   fact and that citation already in the lesson's prose; no false order (`plazos`, `pasos`) or dependency (`arbol`);
   annual figures keep year and norm as the prose has them. Read the row in its esquema in the lesson file.
2. **Scope notes** «Fuera del enunciado literal del programa; preguntado en …»: check against
   `docs/age-verification/aeat/r0a/parsed/master.json` (ids `<exam>-<n>`, `2022X` = llamamiento extraordinario of OEP
   2022) and `docs/aeat-official-exams-ledger.md` that each named exam and question number exists, that answering it
   needs the content of the section the note heads (not a word in common), and that its ledger estado is vigente or
   vigente-con-nota. The section must indeed fall outside the literal programme sentence of its tema
   (`content/aeat-agentes-hacienda/sources/programa.md`, Anexo I); a note on a section the programme names is a FAIL.
3. **«Normativa» lines** changed by removals: every precept listed is cited in the lesson's prose, and every precept the
   prose cites for that norm is listed; the line starts with the norm's `short` from `sources/normativa.yaml`.
4. **Prose sentences** changed (m02-l02 arts. 39.4 and 107.4 LPAC; m02-l04 arts. 80.2 and 95.1 LPAC): against the
   article, as R2 verified sentences: verbatim or faithful, nothing dropped or added, voice rules.

Also check **every esquema title** in your lessons that is new or changed (all esquema titles in m03 lessons; in m01-l04
«Algunas reglas…» was dropped, so only m02-l04's new title in the common part): accurate for its rows, «Algunos/Algunas»
where the rows are selective, voice.

## Report

One file per lesson for m03: `docs/age-verification/aeat/r2-tax/<lesson>/verify-r2bc.md`; one file for your common-part
lessons: `docs/age-verification/aeat/r2/verify/r2bc.md`. Table:

`| \`<id>\` | PASS|FAIL | reason (with the passage of the norm or the exam id) | replacement |`

and titles as `| title <lesson> «…» | PASS|FAIL | reason | replacement |`. The replacement column holds only the
replacement text (the whole row or sentence as it should read), no instructions; for a row whose fix would need a
clause the prose lacks, write «drop» and say so in the reason. Write each lesson's report as soon as it is done.
