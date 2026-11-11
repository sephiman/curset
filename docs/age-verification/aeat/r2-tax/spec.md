# AEAT round R2, tax part — writer and verifier spec

2026-11-11. Course `aeat-agentes-hacienda`, temas III.1–III.20 (`m03-l01` … `m03-l20`). Theory only. Requirements:
`docs/aeat-agentes-course-requirements.md` (R3.5, R4.2–R4.5). Plan: `docs/aeat-tax-plan.md`. The tax lessons are
written new: C1 and C2 have no tax lessons.

Read once per agent run: this file; `docs/prose-voice.md`; `CLAUDE.md` (writing rule); `docs/aeat-exam-style.md` §§ 2,
8–9; your temas' entries in `docs/aeat-tax-plan.md`; each tema's question pack
`docs/age-verification/aeat/r2/questions/<lesson>.md`; the `normativa.yaml` entries of the norms your temas use
(`short`, `aliases`, `note`, `cambios_pendientes`, `cifras_anuales`) and its header (lines 1–75: unconvalidated RDLs);
`docs/age-verification/aeat/r1/rdl-29-2026-revert-list.md` if your temas are III.1, III.4, III.15, III.16 or III.18.
Norm texts: `pdftotext -layout content/aeat-agentes-hacienda/sources/normativa/<file> -` (grep the article you need);
for an `.html` file strip the tags (`python3 -I -c` with `html.parser`). This course's snapshot is the source of truth,
never memory.

## Writer

You write `content/aeat-agentes-hacienda/es/lessons/<lesson>.md` and notes in
`docs/age-verification/aeat/r2-tax/<lesson>/writer.md`. Touch no other file.

### Lesson shape

1. Keep the `# ` title line exactly. Delete the `:::note{type=info}` «Tema sin redactar.» block.
2. **Introduction**: one short paragraph naming the norms that govern the tema, each once with its full title and the
   short name in brackets: «La Ley 58/2003, de 17 de diciembre, General Tributaria (LGT), regula…». C1/C2 lessons open
   this way (see `content/aeat-agentes-hacienda/es/lessons/m02-l05.md`).
3. **Body**: `##` sections in the order of the governing norm (its títulos, capítulos and articles), each matched to a
   phrase of the programme; `###` for sub-parts. Lists with the norm's own letters («- a) …») when the article lists.
   Tables only where the norm itself compares (plazos, percentages by case); every table row carries its citation in a
   «Cita» column.
4. **Worked examples** (`### Ejemplo: <what it applies>`), only where the plan lists them or the norm's own rule is
   applied step by step (interest, recargos of art. 27 LGT, plazos of art. 62 LGT, reductions of sanctions,
   prescripción, cómputo of plazos): a fictional taxpayer («Lucía Martín», «Talleres Ribera, S.L.»), every date stated
   with its weekday when a día hábil matters, numbered steps, each step citing the paragraph it applies; round
   numbers; the result stated once. Check every calendar date with `python3 -c "import datetime; …"` and say in your
   notes that you did. No tax advice, no planning, no «te conviene».
5. **«Lo que más cae»**: exactly ten lines, each one fact a coverage question of the pack asked, with its citation, the
   most repeated first. Use reference questions only if there are fewer than ten coverage facts.
6. **«Normativa»**: one line per norm the lesson cites, starting with the `short` name from `normativa.yaml` and «:»,
   then exactly the articles cited in the prose, in order, ranges with «–» («- LGT (Ley 58/2003): arts. 26.1–2, 27.1–6,
   62.2 y 104.1.»). List every norm the prose names, including one named inside another norm's text (the verifiers
   enforce this strictly). Cambio-pendiente lines as the R1 stubs: «Cambio pendiente por el <norma>, sin convalidar,
   con efectos desde el DD-MM-AAAA (<preceptos>).», only for precepts the lesson cites. A «Normativa» line must not end
   in «art. N.» alone (the list-shape check reads it as a list marker): end it with the article and its paragraph or
   with «y …».

### Rules for every sentence

- **Verbatim facts**: every amount, percentage, plazo, threshold, date, organ, mayoría, exception and list exactly as the
  article says, never approximated; quote the article's words for the key element («en el plazo de seis meses desde el
  fallecimiento»). A list presented as complete is complete; a selective one says so («entre otros»). Clauses that
  narrow a rule («salvo…», «en su caso», «cuando…») stay in.
- **A fact an official question asked is never cut.** Go through every question of the pack, coverage and reference:
  the lesson states the fact that makes the official key right, and the facts that make the distractors wrong when
  the article states them. The pack's «evidencia R0a» quotes the article; check it against the snapshot (R0a cited the
  wrong apartado three times in the common part).
- **Leave out** a fact the programme does not name and no coverage question asked (plan: «Depth»). Depth: full,
  standard or focused, as the plan says per tema.
- **Citations** inline in C1's form: «(art. 27.2 LGT)», «(arts. 66–68 LGT)», «(art. 20.Uno.18.º a) LIVA)», «(art. 7.f)
  LIRPF)», «(apartado primero.2 Orden de 2 de junio de 1994)», «(disposición adicional sexta LGT)». The norm is named by
  its `short` name, the parenthesis of the short name or an `aliases` entry of `normativa.yaml`. After writing, run
  `cd backend && uv run python ../docs/age-verification/aeat/r2-tax/tools/cites.py <lesson>` and fix every unresolved
  citation it lists (a name the parser does not know, or a unit it cannot read). Never edit `normativa.yaml` or any
  platform file to make a citation resolve; if the CAU reglamentos 2015/2446 and 2015/2447 show «no unit», keep the
  citation as written (the indexer does not read their XHTML) and list it in your notes.
- **Annual figures** (interés de demora, interés legal, IPREM, limits and module thresholds, rates set by a budget law
  or a yearly order) carry the year and the norm that sets them, as `cifras_anuales` records: «El interés de demora
  para 2026 es el 4,0625 % (disposición adicional cuadragésima segunda.Dos Ley 31/2022, prorrogada para 2026)». If only
  the prorogued budget law exists, say so.
- **RDL 29/2026 and the other unconvalidated RDLs** (header of `normativa.yaml`): a precept they changed is written in
  the text in force, followed by «(redacción del Real Decreto-ley 29/2026, convalidación pendiente)» or, for changes
  with later effects, «(desde DD-MM-AAAA, Real Decreto-ley 29/2026, convalidación pendiente)». Nothing else about them.
- **Two official sources disagree** (a regulation and its law, two orders): state both with their citations; do not
  choose.
- **Cross-references** to other lessons by id only when the other lesson states the fact: III.1 `m03-l01` … III.20
  `m03-l20`; common part I.1 `m01-l01` … II.5 `m02-l05`. Keep them rare.
- **Voice**: `docs/prose-voice.md`, the never-does list is a hard constraint: no fillers («es importante señalar», «cabe
  destacar», «en este sentido», «a la hora de»), no rhetorical questions, no triads for rhythm, no «no solo… sino
  también», no closing summaries, no look-ahead closers, no stacked hedges, no repeated paragraph openers, no synonym
  rotation (repeat «obligado tributario»). Avoid the blacklist split openers («Es…», «Eso…», «Por eso…», «Así…», «Y…»,
  «También es…»). Peninsular Spanish, «tú». One fact per sentence where the article allows; a long sentence that
  quotes one rule is fine.
- **No invented vocabulary**: only terms the norm or ordinary Spanish legal usage uses in the same sense. No coined
  labels for groups of rules.
- No `:::esquema` blocks (round R2c).

### Writer's notes (`r2-tax/<lesson>/writer.md`)

1. Sources: for each section, the norm file and the pages read.
2. Every question of the pack: id → the lesson section that states its fact, or «no está: <reason>».
3. «Lo que más cae»: line → question id(s).
4. Worked examples: the dates checked and how.
5. Course summary for `course.yaml`: at most three sentences, plain facts, in the voice.
6. Glossary proposals: defined legal terms the lesson teaches, each with the article that defines it, as YAML ready to
   paste: `- id: g-<slug>` / `es: <term>` / `origin: <lesson>` / `definition: {es: <one or two sentences quoting the
   definition, with its citation>}`. Never-coins: only a term the norm itself defines or uses as a term («hecho
   imponible», «devengo», «sustituto del contribuyente», «domicilio fiscal»…), at most eight per lesson. Check
   `content/aeat-agentes-hacienda/glossary.yaml` for an existing id first.
7. Unresolved citations and why; facts left out for lack of a source; ambiguities not resolved.

## Verifier (blind)

You did not write the lesson. Input: `docs/age-verification/aeat/r2-tax/<lesson>/pending.md` (the sentences to verify,
each with an id, its line and its governing citations) and the lesson file for context. Work in batches of 60 rows,
in order, writing your report after each batch so a cut loses at most one batch.

For each pending sentence open the cited article in `content/aeat-agentes-hacienda/sources/normativa/` and check:

1. every number, amount, percentage, plazo, threshold, organ, date, condition, exception and list matches the article in
   force in this snapshot; nothing approximated; a complete-looking list is complete, a selective one says so; a
   narrowing clause of the article is not dropped when the sentence states the rule;
2. the citation names the article (and paragraph) that holds the fact; a sentence without its own citation is checked
   against its governing citation;
3. annual figures name their year and the norm that sets them, as `normativa.yaml` `cifras_anuales` records;
   «convalidación pendiente», «(desde …)» and «Cambio pendiente» marks are right (`normativa.yaml`);
4. **worked examples**: recompute every step yourself from the article (amounts, percentages, dates, weekdays with
   `python3`); the step's citation is the paragraph applied; FAIL any step whose arithmetic, date or rule is wrong;
5. a cross-reference (`m0N-lNN`) points at the lesson of this course that has the fact;
6. voice: nothing from the prose-voice never-does list; no invented term.

Structure-only sentences («El artículo 62 regula los plazos de pago.») pass when true. A «Lo que más cae» line passes
when its fact matches its citation. A «Normativa» line passes when every listed article is cited in the lesson's prose,
every norm cited (or named) in the prose is listed, and its cambio-pendiente note is right. A glossary entry passes when
its definition matches the cited article and the term is the norm's own.

Output: `docs/age-verification/aeat/r2-tax/<lesson>/verify.md` (a re-check: `verify-recheck-N.md`), one table row per
pending id, in this exact shape (the provenance tool reads it):

```
| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `0123456789` | PASS | art. 27.2 LGT | — | — |
| `abcdef0123` | FAIL | art. 62.2 LGT | says «el día 5»; the article says «hasta el día 5 del segundo mes posterior o, si éste no fuera hábil, hasta el inmediato hábil siguiente» | <full replacement sentence, citation included, or «drop»> |
```

A FAIL gives the full replacement sentence, faithful to the article, in the lesson's voice, or «drop» when the sentence
cannot be made right. Never edit the lesson. End the report with one line: «PASS n · FAIL m».

## Coverage check (after each group)

Per lesson, every «coverage» question of the pack: the lesson states the fact that makes the official key right (quote
the lesson sentence and its line) → `COVERED`, or does not → `MISS` with the article that holds the fact and the
sentence that would cover it. Output `docs/age-verification/aeat/r2-tax/<lesson>/coverage.md`, ending «COVERED n ·
MISS m».
