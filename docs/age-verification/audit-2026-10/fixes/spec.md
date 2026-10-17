# R2b fixes, bloques I–V — writer and verifier spec (2026-10-17)

Course `content/age-administrativo-c1` (C below). Nothing is committed. SP is given in your prompt (questionnaire and
key texts in `SP/exams/`). Reports of this round: `docs/age-verification/audit-2026-10/` (scope `scope/mBB.md`,
coverage `coverage/mBB-lTT.md` and `coverage/mBB.md`).

## Read first

- `docs/age-administrativo-course-requirements.md` R4.2–R4.5 (v1.5: no word ceilings; a fact an official exam asked is
  never cut for length) and section 4b.
- `docs/prose-voice.md` (its «never does» list is a hard constraint) and `CLAUDE.md` (no invented vocabulary;
  Peninsular Spanish, «tú»).
- Your bloque's section of `docs/age-theory-ledger.md` (writer's notes, «Cuts», «Cut for length», «Open items»,
  standing conventions: «(hoy: …)» for old ministry names, «(desde …)» for cambio-pendiente wording, cross-references
  written bare as m03-l03, never in «»).
- The lesson you edit, whole, before editing it.

## R2 rules (unchanged)

- Every fact is copied from the article, verbatim or as a faithful shortening that keeps every number, plazo, organ,
  majority and exception; never approximated. Cited inline as the lesson already does: «(art. N norma)».
- Sources: the consolidated texts in `C/sources/normativa/` (`pdftotext -layout`). If the article is not there, download
  the official text from boe.es (`curl -sSL`, quote URLs; consolidated PDF `https://www.boe.es/buscar/pdf/<año>/<ID>-consolidado.pdf`
  or the original `https://www.boe.es/boe/dias/<…>/pdfs/<ID>.pdf`) into `C/sources/normativa/` named
  `<BOE-ID>_<short>_<YYYY-MM-DD>.pdf`, and write in your fix file the `normativa.yaml` entry it needs (short, title,
  boe_id, url, consolidated_as_of, temas, file). Do not edit `normativa.yaml` yourself; the coordinator merges.
- Never an official exam or key as the source of a fact. A disputed key («Clave oficial discutida») is never followed:
  the lesson states what the norm says.
- Cut whole facts only, never a clause of a kept sentence. Do not cut for length at all in this round.
- Keep the «Normativa» block in step: every article newly cited is added to its norm's line; an article no longer cited
  anywhere in the lesson is removed. «Lo que más cae»: at most ten lines; add a fact there when it is one the exams ask
  repeatedly (two or more questions) or the coverage report marks as asked in a key position; if the block is full, say
  which line it replaces and why.
- Hard wrap at 120 characters, as the lesson does. No list marker in the middle of a sentence.

## What you do, per lesson

1. **Coverage.** Every partial and miss in `coverage/mBB-lTT.md` for your lessons: state the missing fact in the
   section where it belongs, cited. Where another lesson already states it, still state it here (the owner lesson must
   carry it) and point to the other lesson once if useful. Disputed keys: the norm's fact only.
2. **Scope — sections kept by exam evidence.** At the start of each such section (right after its heading) add
   ```
   :::note{type=info}
   Fuera del enunciado literal del programa; preguntado en <examen>.
   :::
   ```
   <examen> names each question as «la convocatoria 2025 (llamamiento extraordinario), primera parte, pregunta 17»;
   several joined with «; ». Use modelo A numbering; ordinario exams are «la convocatoria 2024 (modelo A)», «la
   convocatoria 2022»; conv2020 is «la convocatoria de la OEP 2020 (examen de 2022)». Reserve questions: «primera parte,
   pregunta de reserva 3». A subsection under a section that already carries the note gets none.
3. **Scope — sections removed.** Delete the section (heading and body). Then: remove from «Normativa» the articles it
   alone cited; remove or rewrite «Lo que más cae» lines resting on it; fix any cross-reference in any lesson that
   pointed to it (`grep -rn` the course); check `C/glossary.yaml` for entries whose only second lesson was this
   section (list them: they move to the waiting list; the coordinator edits the glossary).
4. **Scope — gaps and cross-references** listed for your lessons in the prompt: write the missing section under these
   rules; add the missing pointers.
5. **Cuts restored.** Using your bloque's cut lists in the ledger (writer's notes «Cuts»/«Cuts of note», «Cut for
   length», the «Second blind pass» and «Coordinator restorations» paragraphs), check every cut item against the
   questionnaires of every exam in `SP/exams/` (2020 to 2025, annulled questions included, not `función retirada` or
   `norma modificada`; use `docs/age-official-exams-ledger.md` for tema and estado). Restore every item an exam asked,
   in its place in the norm's order, under these rules. Items no exam asked stay out: list them with «not asked».

## Your fix file

`docs/age-verification/audit-2026-10/fixes/fix-mBB.md` (one per bloque): per lesson, a numbered list of every change:
kind (coverage / note / removal / gap / pointer / restore), the exam rows it answers, old text → new text (exact), the
article passage it rests on quoted from the source file (file name), and Normativa / «Lo que más cae» edits. Then the
cut items checked with their verdict (restored / not asked, with the questions found), new sources with their
`normativa.yaml` entries, glossary entries affected by removals, and `wc -w` before and after per lesson.

## Verifier (blind)

You did not write these changes. For each numbered change in `fix-mBB.md`: open the lesson as it stands and the cited
source file yourself (not the passage the writer quoted), and check: (1) every number, plazo, organ, majority,
exception and date in the new text is in the article as written; the citation points to the article that says it;
(2) the fact the exam row asks (coverage report) is now stated; (3) a removal removed the whole section and left no
dangling reference, Normativa line or «Lo que más cae» line; (4) a note names questions that exist and ask that content
(open the questionnaire); (5) form: voice page, wrap, no list marker mid-sentence, Normativa in step. Also re-check that
every row the coverage report marked covered is still covered (no edit removed it). Write
`docs/age-verification/audit-2026-10/fixes/verify-mBB.md`: a table `| # | Lesson | Change | PASS/FAIL | Reason | Replacement
(for FAIL) |`, then counts. Edit nothing else.
