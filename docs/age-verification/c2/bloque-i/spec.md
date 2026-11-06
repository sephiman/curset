# C2 round R2, bloque I — writer and verifier spec

2026-11-06. Course `age-auxiliar-c2`, bloque I (temas I.1–I.16, lessons `m01-l01` … `m01-l16`). Theory only.

Read once per agent run: this file; `docs/prose-voice.md`; `CLAUDE.md`; `docs/age-c2-exam-style.md` §§ 2–8 (what the
Auxiliar exams ask); the per-tema question pack `docs/age-verification/c2/bloque-i/questions/<lesson>.md`;
`content/age-auxiliar-c2/sources/normativa.yaml` (which norms the course has, their `short` names, `cambios_pendientes`,
`cambios_aplicados`); `content/age-auxiliar-c2/sources/otros/fuentes.yaml`; `content/age-auxiliar-c2/es/lessons/m00-l01.md`
(the register). Norm texts: `pdftotext -layout content/age-auxiliar-c2/sources/normativa/<file> -` (never C1's copy: the
C2 snapshot is the source of truth; most files are byte-identical to C1's).

## Mapping: C2 tema → C1 source lessons (`content/age-administrativo-c1/es/lessons/`)

| C2 | Programme (short) | C1 lessons |
|---|---|---|
| I.1 `m01-l01` | CE: características, principios y valores, derechos y deberes, garantía y suspensión | m01-l01 (without TC and reforma) |
| I.2 `m01-l02` | TC, reforma de la CE, Corona | m01-l01 (TC, reforma), m01-l02 |
| I.3 `m01-l03` | Cortes Generales, Defensor del Pueblo | m01-l03, m01-l01 (Defensor del Pueblo, if there) |
| I.4 `m01-l04` | Poder Judicial | m01-l04 |
| I.5 `m01-l05` | Gobierno | m01-l05 |
| I.6 `m01-l06` | Gobierno Abierto, Agenda 2030 | m01-l06 |
| I.7 `m01-l07` | Ley 19/2013 | m01-l07 |
| I.8 `m01-l08` | AGE (+ «Otros órganos administrativos») | m01-l08 |
| I.9 `m01-l09` | CCAA y Administración local | m01-l09, m01-l10 |
| I.10 `m01-l10` | Unión Europea | m01-l11 |
| I.11 `m01-l11` | LPAC, LRJSP, revisión, recursos, LJCA | m03-l03 (and m03-l02 where a question asks acto/eficacia) |
| I.12 `m01-l12` | Protección de datos | m02-l04 |
| I.13 `m01-l13` | Funcionarios: clases, régimen, RCP, programación, OEP, selección, provisión, situaciones | m04-l01, m04-l02, m04-l03, m04-l04, m04-l05 (provisión) |
| I.14 `m01-l14` | Derechos y deberes, carrera, promoción, retribuciones, disciplinario, Seguridad Social | m04-l05, m05-l04, m04-l06 (disciplinario only), m04-l07 |
| I.15 `m01-l15` | Presupuesto: contenido, elaboración, estructura, ciclo | m05-l01, m05-l02, m05-l03 (only what the ciclo needs) |
| I.16 `m01-l16` | Igualdad, LGTBI, discapacidad y dependencia | m03-l07 |

## Writer

Output: `content/age-auxiliar-c2/es/lessons/<lesson>.md` (replace the stub) and notes in
`docs/age-verification/c2/bloque-i/writer/<lesson>.md`.

### Depth

R4.1 of the C2 requirements: depth is the C2 exam's. Keep, from the C1 lesson(s):

1. every fact any question of the pack asks or uses as a distractor (coverage and reference questions alike; a fact
   an official Auxiliar question asked is never cut);
2. for each element the C2 programme sentence names, the core articles that define it: what it is, composition,
   designation, mandate, main functions, the plazos and mayorías of its main acts;
3. the sentence that gives the article context of a kept fact when the fact reads wrong without it.

Cut what C2's programme does not name and no Auxiliar question asked: procedural detail, secondary lists, cross-
references to C1 temas C2 does not have. Cut whole sentences, never a clause of a kept sentence (a cut clause made
most C1 FAILs). No word ceiling, no word floor.

### Provenance: keep kept sentences byte-identical

A C2 sentence identical to a C1 sentence (same words, punctuation and inline citation, and the same governing
citation) inherits C1's verification. Everything else goes to a blind verifier. So:

- Copy kept sentences exactly, with their citation parenthesis. Line wrapping does not matter (lines are joined).
- A sentence with no citation of its own is governed by the next cited sentence of its paragraph (or, if none, the
  previous one); a list item without a citation by the last citation of the paragraph that introduces the list. If
  you cut the sentence that carries the citation, the uncited sentence no longer inherits. Prefer keeping paragraphs
  whole or cutting from the end.
- Do not "improve" a kept sentence. If a word must change (a C1 cross-reference such as «en m04-l09», a C1-only lesson
  id, a fact that is now wrong), change it: it becomes a new sentence and is verified.
- C1 cross-references to its own lessons («está en m03-l03») must become C2 lesson ids or be dropped.
- Do not copy `:::esquema` blocks (esquemas are round R2c of C2). Plain markdown tables in the prose may stay.

### New text

Where C2's programme names something no C1 lesson covers (I.1 «Características», I.8 «Otros órganos
administrativos», I.13 Registro Central de Personal and programación de efectivos if C1 lacks them, I.15 «Fases del
ciclo presupuestario», anything a pack question asks and C1 does not state), write it from the norm text in
`content/age-auxiliar-c2/sources/normativa/`:

- every plazo, mayoría, órgano, número, excepción and fecha copied from the article, never approximated; quote the
  article's words for the key element;
- inline citation in C1's form, «(art. 56.1 CE)», «(arts. 3 y 4 LRJSP)», «(art. 13.2 Ley 50/1997)», using a `short`
  name or alias from C2's `normativa.yaml`; a page from `sources/otros/` is cited «(fuente: <file>)»;
- the norm in its version in force today (2026-11-06); a precept with a pending change («cambios_pendientes») in force
  before the exam is written in the forthcoming wording with «(desde DD-MM-AAAA)»; the Normativa block says
  «Cambio pendiente: <norma>, en vigor el <fecha> (<preceptos>).»

### Standing conventions (C1 theory ledger)

- Old ministry names: quote the law as written, then «(hoy: <current name>)» once, after the first such mention, with
  the RD 829/2023 article that gives the function to the current department.
- Head-counts and other non-legal facts come from a saved file in `sources/otros/`, stated «a fecha de» its
  consultation date and cited «(fuente: <file>)».
- TREBEP and the pre-TREBEP texts (Ley 30/1984, RD 364/1995, RD 365/1995, RD 33/1986): where the rules differ, state both,
  each cited; never pick a winner the texts do not name. Quote the disposición derogatoria única TREBEP with its opening
  paragraph («con el alcance establecido en el apartado 2 de la disposición final cuarta») whenever a letter of it is
  used. DF 4.ª.1 TREBEP defers arts. 16–20 and 78–84 to the leyes de Función Pública: keep C1's caveat wherever those
  articles are stated.
- Reglamento del Congreso art. 23: «(desde la XVI legislatura)».
- I.15: if the text cites CE art. 134, the Normativa block lists it («CE: art. 134…»).

### Structure

```
# <title exactly as in content/age-auxiliar-c2/course.yaml>

<intro paragraph: the governing norms, named once with their full title and the short name in brackets>

## <section following the norm's structure: título, capítulo, artículo order>
### <sub-sections as needed>

## Lo que más cae

- <ten lines, each one fact an official Auxiliar question of the pack asked, with its citation> (art. N norma).

## Normativa

- <short>: arts. <list, ranges with «–»>. [Cambio pendiente: <norma>, en vigor el <fecha> (<preceptos>).]
```

- «Lo que más cae»: exactly ten lines; each states a fact that a coverage question of the pack (2022–2025, vigente)
  asks, the most repeated first; fall back to reference questions only when there are fewer than ten coverage facts.
  A C1 «Lo que más cae» line may be reused verbatim when it states such a fact.
- «Normativa»: every norm the lesson cites, with exactly the articles cited (C1's form, see C1 m01-l03 and m04-l07).
  The line starts with the `short` name of `normativa.yaml`, then «:».
- Voice: `docs/prose-voice.md`, including the never-does list (hard constraint). Peninsular Spanish. No invented
  vocabulary: only terms used outside the course in the same sense.

### Writer's notes (`writer/<lesson>.md`)

1. Sections kept, cut and new, with one line of reason each (for cuts: «no lo pide el programa C2 ni ninguna pregunta»).
2. Every question of the pack: id → the lesson section that states its fact (or «no está: <reason>»).
3. «Lo que más cae»: line → question id(s).
4. New sentences: the article (file and page) each one rests on.
5. Course summary for `course.yaml`: at most three sentences, plain facts, in the voice.
6. Glossary: C1 glossary ids (`content/age-administrativo-c1/glossary.yaml`) whose term this lesson uses in the same
   sense.
7. Ambiguities found, not resolved.

## Verifier (blind)

Input: `docs/age-verification/c2/bloque-i/pending/<lesson>.md` (the sentences that did not inherit, each with an id,
its line and its governing citations) and the lesson file for context. You did not write the lesson. For each pending
sentence open the cited article in `content/age-auxiliar-c2/sources/normativa/` (or the cited `sources/otros/` file)
and check:

1. every number, plazo, mayoría, órgano, date, exception and list stated matches the article in force; nothing is
   approximated; a list presented as complete is complete, a selective one says so («entre otros»);
2. the citation names the article that holds the fact (a sentence without its own citation is checked against its
   governing citation);
3. «(hoy: …)» notes, «(desde …)» marks and cambio-pendiente lines are right (`normativa.yaml`);
4. a C2 cross-reference (`m01-lNN`) points at the lesson that has the fact;
5. voice: nothing from the prose-voice never-does list; no invented term.

Structure-only sentences («El artículo 62 enumera diez funciones.») pass when true. A «Lo que más cae» line passes when
its fact matches its citation. A «Normativa» line passes when every listed article is cited in the lesson's prose and
every norm cited in the prose is listed.

Output: `docs/age-verification/c2/bloque-i/verify/<lesson>.md` (a re-check: `<lesson>-recheck-N.md`), one table row per
pending id, in this exact shape (the provenance audit reads it):

```
| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `0123456789` | PASS | art. 56.1 CE | — | — |
| `abcdef0123` | FAIL | art. 99.3 CE | says «dos meses»; the article says «dos meses a partir de la primera votación» | <full replacement sentence, citation included> |
```

A FAIL gives the full replacement sentence, faithful to the article. Do not edit the lesson.

## Coverage check (after the bloque)

Per lesson, every «coverage» question of the pack: the lesson states the fact that makes the official key right
(quote the lesson sentence and its line) → `COVERED`, or does not → `MISS` with the article that holds the fact.
Output `docs/age-verification/c2/bloque-i/coverage/<lesson>.md`.
