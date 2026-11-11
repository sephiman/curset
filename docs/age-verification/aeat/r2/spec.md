# AEAT round R2, common part — writer and verifier spec

2026-11-11. Course `aeat-agentes-hacienda`, temas I.1–I.7 (`m01-l01` … `m01-l07`) and II.1–II.5 (`m02-l01` …
`m02-l05`). Theory only. Requirements: `docs/aeat-agentes-course-requirements.md` (R2.3, section 4).

Read once per agent run: this file; `docs/prose-voice.md`; `CLAUDE.md`; `docs/aeat-exam-style.md` §§ 2–8; the tema's
question pack `docs/age-verification/aeat/r2/questions/<lesson>.md`; `content/aeat-agentes-hacienda/sources/normativa.yaml`
(the norms this course has, their `short` names and aliases, `cambios_pendientes`). Norm texts: `pdftotext -layout
content/aeat-agentes-hacienda/sources/normativa/<file> -` (this course's snapshot is the source of truth).

## How the lessons were drafted

`tools/derive_draft.py` copied whole sections of C1 and C2 lessons into each lesson, verbatim, as
`derivation.yaml` maps them to the programme's phrases (C2 first, C1 where C2 lacks the section). A copied sentence
that keeps its exact text and its governing citation inherits C1's or C2's verification (R2.3); everything else is
checked by a blind verifier. The draft has `PENDIENTE` blocks: the introduction, the `new` sections, «Lo que más cae»
and «Normativa».

## Writer

You edit `content/aeat-agentes-hacienda/es/lessons/<lesson>.md` in place and write notes to
`docs/age-verification/aeat/r2/writer/<lesson>.md`. You did not choose the copied sections; do not rewrite them.

### What you write

1. **Introduction** (replaces the first `PENDIENTE`): one short paragraph naming the norms that govern the tema, each
   once with its full title and the short name in brackets, as the C1/C2 lessons open.
2. **New sections** (each `PENDIENTE` under a heading): the brief in `derivation.yaml` says what. Write from the norm
   text, each sentence with its inline citation.
3. **Gaps the exam asks.** Go through every question of the pack (coverage and reference). If the lesson does not
   state the fact that makes the official key right, add it: one or two sentences, cited, in the section where it
   belongs (a new `###` if none fits). A fact an official AEAT question asked is never cut.
4. **Cross-references.** Copied sentences that point to C1/C2 lesson ids (`m01-l13`, «está en m03-l03») are wrong here.
   Rewrite them to this course's lessons (I.1 `m01-l01` … I.7 `m01-l07`, II.1 `m02-l01` … II.5 `m02-l05`; tax temas
   `m03-lNN`) or drop the cross-reference clause. The sentence becomes new and is verified.
5. **Trims the map asks for** (I.7: «Acceso de las personas con discapacidad» keeps only what art. 59 TREBEP says;
   sentences citing RD 2271/2004, which this course does not have, go). Cut whole sentences, never a clause of a kept
   sentence. When you cut the sentence that carries a paragraph's citation, the uncited sentences around it stop
   inheriting: keep paragraphs whole or cut from the end.
6. **«Lo que más cae»**: exactly ten lines, each one fact a coverage question of the pack asked, with its citation, the
   most repeated first; reference questions only if there are fewer than ten coverage facts. Reuse a «Lo que más cae»
   line of the source C1/C2 lesson verbatim when it states such a fact (it then inherits).
7. **«Normativa»**: one line per norm the lesson cites, starting with the `short` name from `normativa.yaml` and «:»,
   then exactly the articles cited in the prose (C1's form: «- CE: arts. 1–9, 14–29, 53–55.»). Cambio-pendiente
   lines as C1: «Cambio pendiente: <norma>, en vigor el <fecha> (<preceptos>).»

### Rules for every new sentence

- Every plazo, mayoría, órgano, número, excepción and fecha copied from the article, never approximated; quote the
  article's words for the key element. Inline citation in C1's form, «(art. 56.1 CE)», «(arts. 3 y 4 LRJSP)», using a
  `short` name or alias from this course's `normativa.yaml`; a page from `sources/otros/` is cited «(fuente: <file>)».
- The norm in force today (2026-11-11); a precept with a `cambios_pendientes` entry in force before the exam is
  written in the forthcoming wording with «(desde DD-MM-AAAA)».
- Standing conventions (C1 theory ledger): old ministry names quoted, then «(hoy: <current name>)» once with the RD
  829/2023 article; TREBEP vs pre-TREBEP texts: state both where they differ, never pick a winner; Reglamento del
  Congreso art. 23 «(desde la XVI legislatura)».
- Do not edit a copied sentence to improve it. Change one only when it is wrong here (a cross-reference, a fact now
  wrong in this course's snapshot): it then becomes new.
- Do not add `:::esquema` blocks. Keep the copied ones as they are.
- Voice: `docs/prose-voice.md`, including the never-does list (a hard constraint). Peninsular Spanish, «tú». No
  invented vocabulary: only terms used outside the course in the same sense.

### Writer's notes (`writer/<lesson>.md`)

1. New sections and gap sentences: the article (file, page) each rests on.
2. Every question of the pack: id → the lesson section that states its fact, or «no está: <reason>».
3. «Lo que más cae»: line → question id(s).
4. Course summary for `course.yaml`: at most three sentences, plain facts, in the voice.
5. Glossary: ids from `content/age-auxiliar-c2/glossary.yaml` or `content/age-administrativo-c1/glossary.yaml` whose
   term this lesson uses in the same sense.
6. Ambiguities found, not resolved.

## Verifier (blind)

Input: `docs/age-verification/aeat/r2/pending/<lesson>.md` (the sentences that did not inherit, each with an id, its
line and its governing citations) and the lesson file for context. You did not write the lesson. For each pending
sentence open the cited article in `content/aeat-agentes-hacienda/sources/normativa/` (or the cited `sources/otros/`
file) and check:

1. every number, plazo, mayoría, órgano, date, exception and list stated matches the article in force; nothing is
   approximated; a list presented as complete is complete, a selective one says so («entre otros»);
2. the citation names the article that holds the fact (a sentence without its own citation is checked against its
   governing citation);
3. «(hoy: …)» notes, «(desde …)» marks and cambio-pendiente lines are right (`normativa.yaml`);
4. a cross-reference (`m0N-lNN`) points at the lesson of this course that has the fact;
5. voice: nothing from the prose-voice never-does list; no invented term.

Structure-only sentences («El artículo 62 enumera diez funciones.») pass when true. A «Lo que más cae» line passes
when its fact matches its citation. A «Normativa» line passes when every listed article is cited in the lesson's prose
and every norm cited in the prose is listed. A sentence copied from C1/C2 that only lost its inheritance (its cited
file is a newer consolidation here, or its governing citation changed) is checked the same way.

Output: `docs/age-verification/aeat/r2/verify/<lesson>.md` (a re-check: `<lesson>-recheck-N.md`), one table row per
pending id, in this exact shape (the provenance audit reads it):

```
| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `0123456789` | PASS | art. 56.1 CE | — | — |
| `abcdef0123` | FAIL | art. 99.3 CE | says «dos meses»; the article says «dos meses a partir de la primera votación» | <full replacement sentence, citation included> |
```

A FAIL gives the full replacement sentence, faithful to the article. Do not edit the lesson.

## Coverage check (after the last tema)

Per lesson, every «coverage» question of the pack: the lesson states the fact that makes the official key right
(quote the lesson sentence and its line) → `COVERED`, or does not → `MISS` with the article that holds the fact.
Output `docs/age-verification/aeat/r2/coverage/<lesson>.md`.
