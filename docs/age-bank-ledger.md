# Question bank ledger — age-administrativo-c1

Round R3 (requirements § 5). Plan and quotas: `docs/age-bank-plan.md`. Working files:
`docs/age-verification/bank/` (official questions per tema in `official/`, bloque I in `bloque-i/`). Nothing committed.

## Session 2 (2026-10-18) — summary

Bloque I is closed: **676 questions** in `content/age-administrativo-c1/exercises/` (40 quiz exercises, `m01-lTT-ex-N`),
listed under their lessons in `course.yaml`, loader and cross-reference check green. Stop here; bloque II is next.

- **Platform:** a question may cite a saved source page («fuente: `file`») its lesson cites
  (`citations/course.py`, `_source_anchor`); tests `test_a_question_citing_a_source_file_its_lesson_cites_opens_at_that_citation`
  (failed before the fix) and `…_never_cites_fails_the_load`. `content/README.md` documents it. The answer-bias guards
  (`test_quiz_answer_bias.py`) now run the single-choice checks and the generator deal over age-administrativo-c1 too.
- **Lessons** (blind-checked, `bloque-i/lesson-fixes/`: writer, verify 4/5 PASS, recheck PASS):
  - m01-l01 «Lo que más cae» line 6 is now art. 13.2 CE (asked in conv2020_X P1 1); «Las reformas» gives only date and
    article, as `boe-analisis-ce.xml` does.
  - m01-l02: the «Nombramientos en otros poderes» table cites in parentheses (six citations, no fact changed); the tutela
    sentence limits «español de nacimiento» to the testamentary tutor (art. 60.1 CE); art. 151.2 CE is stated as rules
    4.º and 5.º.
  - Markup: a source citation is read only when its parenthetical starts with «fuente:», so m01-l01, m01-l06 and m01-l11
    now write «(fuente: `file`; label)» (39 citations).
  - No kept question rested on the old wide readings (I.2 q052–q053 test the testamentary tutor; I.1 q010 tests «four
    reforms, one article each»; the I.9 art. 151.2 questions were verified against the CE).
- **Explanations:** the platform shuffles options per learner and the PDF prints the shuffled letters, so 66 kept
  explanations that named options by letter or position were rewritten to name them by content
  (`explanation-refs.json`, blind check `explanation-refs.verify.md`, 66/66 PASS). No other word changed. Verify-spec now
  checks this.
- **New questions** (verified as usual; `additions.verify-1` … `-5`): 36 authored, 7 dropped, 29 kept. I.1 q065 (new
  lmc-6; q013 re-tagged to it); I.2 q065, q067–q071 (the six appointment rows); I.4 q069–q073 (article share 49 → 53 %);
  I.11 q063–q072 (article share 49 → 54 %, and the industria half of lmc-10); I.7 q062–q064 and I.9 q063–q066 (short
  keys, see below). Dropped: I.4 q065–q068 (explanations named options by letter), I.2 q066 (official copy), I.1 q066
  and I.7 q065 (no norm named in the stem, and another norm in force makes a distractor true).
- **Length edge.** Built as it stood, the bank failed the course-wide length-edge guard (z = +3.07: keys about 1.6
  characters longer than distractors on average, I.11 and I.7 the heaviest). Verified options were not rewritten; the
  new questions carry keys shorter than their distractors instead. Final: length edge z = +0.60, longest-is-correct
  z = +0.44, authored position a/b/c/d 170/170/170/166 (z ≤ 0.27). Verifiers noted that in the new questions the key is
  often the shortest option; the aggregate guard is the authority, and each tema's key-shortest share is for the
  bloque II writers to keep in mind.
- **Goldens:** `citations.es.txt` 3,271 → 3,334 prose citations (427 → 466 source files), 1,464 → 1,482 anchors,
  496 → 510 esquema rows, every moved row in m01 (prose-gap citations, the 39 source citations now read, restored
  rows, the six table citations, art. 151.2.4.º/5.º, art. 13.2). `glossary-links.es.txt` 319 → 320 web marks:
  g-estatuto-de-autonomia new in m01-l07 (Ciudades con Estatuto de Autonomía, same sense); g-provincia's first mark moves
  to m01-l02 (art. 151.2 sentence); g-personas-con-discapacidad moves within m01-l01; g-estabilidad-presupuestaria loses
  its m01-l01 mark (the reform topics were removed; its origin m05-l01 still states it). `lesson-refs.es.txt` unchanged.
- **Suites:** backend `ruff check`, `ruff format --check`, `mypy src` (strict) clean; `pytest` 1,495 passed, 20 skipped
  (+6: two citation tests, four AGE bias cases). Frontend `npm run build` clean; `vitest` 593 passed, 51 skipped.
- **Unchanged:** crypto-futures content and goldens; Android bundle re-exported to scratch, byte-identical to
  `dist/bundle`, label catalogs identical to `dist/i18n`; `verify_golden_stability.py` exit 0, digest `f0ae701b…bcaea`.

## Session 1 (2026-10-18) — summary and where to resume

- Plan written: `docs/age-bank-plan.md` (quotas, target mixes, repository shape, verification).
- Bloque I prose gaps closed (theory ledger «Esquemas bloque I», open item 1) and blocked esquema rows restored; see
  «Bloque I prose gaps» below.
- Official questions split by tema into `docs/age-verification/bank/official/<tema>.md` (generated from the
  questionnaires and the exams ledger's tema column; cover pages excluded).
- **Bloque I authored and verified:** 690 questions written by 11 writers, every one checked blind in two batches
  (plus a check of each replacement): 43 dropped (key 0, unique 7, citation 3, style 23, official 10), **647 kept**
  against a quota of 605. Every tema is at or above its quota; every «Lo que más cae» line is tested except I.1 lmc-6
  (open item 8).
- **Paused by the user:** code changes, test runs and golden regeneration (another task is changing the test suite).
  Pending until released: answer-bias guards over AGE, the YAML build into `content/age-administrativo-c1/exercises/`
  and `course.yaml`, loader, cross-reference check, `citations.es.txt` and the other goldens (they also move for the
  prose-gap citations, e.g. the new art. 76 LOTC anchor).

**Resume (session 2):** done (see «Session 2» above).

**Resume (session 3): bloque II.** Read this ledger, `docs/age-bank-plan.md` and the theory ledger «Esquemas bloque II»
open item 1 (prose gaps). Before authoring: close those gaps blind-checked, restore the rows they block, and rewrite
the 13 bare `sources/otros/` citations in m02-l02 / m02-l03 to «(fuente: `file`; label)». Copy `bloque-i/spec.md` and
`verify-spec.md` to `bloque-ii/` with these lessons learned: explanations name options by content, never by letter;
a stem that names no norm is checked against every norm in force; keep the key-longest share near a quarter and the key
not systematically shorter either (watch `bank_stats.py` and the course-wide length-edge guard after each build).
Build with `uv run python ../docs/age-verification/bank/tools/build_exercises.py bloque-ii m02` from `backend/`.

## Bloque I prose gaps

Writer record `docs/age-verification/bank/bloque-i/prose-gaps/writer.md`; blind check `verify.md` (39 items, 37 PASS,
2 FAIL: two m01-l11 esquema rows, art. 235.1 TFUE condition cut and art. 238.3 TFUE blocking minority placed after the
72 % case); the reviewer's replacements applied and re-checked by a new reviewer, `recheck.md` (6 items, 6 PASS).

- Sentences added or completed: m01-l01 (arts. 76, 33.2, 35.2 LOTC; art. 7.2 LO 3/1981), m01-l03 (art. 93.1 RS; arts.
  41.1, 46.2 RC), m01-l04 (arts. 595.1, 630.1 LOPJ, the CNI Magistrate), m01-l07 (art. 19.3, DA 4.ª.3 Ley 19/2013),
  m01-l09 (medio ambiente and ferrocarriles pairs), m01-l11 (arts. 235.1, 238.2, 238.3 TFUE).
- Rows restored: 14 (m01-l01 4, m01-l03 1, m01-l04 3, m01-l09 2, m01-l11 4 including the split 235.1 row), plus the
  m01-l07 19.3 cell and the 16.4 TUE label. Not restored: a 41.1 RC row (a Mesa's composition, not a majority).
- Tests and goldens not run (pause above).

## Per tema

| Tema | Quota | Authored | Dropped (key / unique / citation / style / official) | Kept | LMC covered | Verification files |
|---|---|---|---|---|---|---|
| I.1 | 57 | 66 | 7 (0 / 1 / 3 / 1 / 2) | 59 | 10/10 | `m01-l01.verify-1.md`, `-2`, `additions.verify-2.md` |
| I.2 | 55 | 71 | 7 (0 / 2 / 0 / 4 / 1) | 64 | 10/10 | `m01-l02.verify-1.md`, `-2`, `-3`, `additions.verify-2.md`, `-5` |
| I.3 | 56 | 64 | 4 (0 / 2 / 0 / 1 / 1) | 60 | 10/10 | `m01-l03.verify-1.md`, `-2`, `replacements.verify-1.md` |
| I.4 | 54 | 73 | 9 (0 / 0 / 0 / 6 / 3) | 64 | 10/10 | `m01-l04.verify-1.md`, `-2`, `-3`, `additions.verify-1.md`, `-2`, `-4` |
| I.5 | 54 | 61 | 4 (0 / 1 / 0 / 3 / 0) | 57 | 10/10 | `m01-l05.verify-1.md`, `-2` |
| I.6 | 54 | 61 | 0 | 61 | 9/9 | `m01-l06.verify-1.md`, `-2` |
| I.7 | 54 | 65 | 5 (0 / 1 / 0 / 4 / 0) | 60 | 10/10 | `m01-l07.verify-1.md`, `-2`, `additions.verify-3.md` |
| I.8 | 58 | 66 | 2 (0 / 0 / 0 / 2 / 0) | 64 | 10/10 | `m01-l08.verify-1.md`, `-2`, `replacements.verify-1.md` |
| I.9 | 54 | 66 | 4 (0 / 1 / 0 / 2 / 1) | 62 | 10/10 | `m01-l09.verify-1.md`, `-2`, `replacements.verify-1.md`, `additions.verify-3.md` |
| I.10 | 54 | 61 | 3 (0 / 1 / 0 / 1 / 1) | 58 | 10/10 | `m01-l10.verify-1.md`, `-2` |
| I.11 | 55 | 72 | 5 (0 / 0 / 0 / 3 / 2) | 67 | 10/10 | `m01-l11.verify-1.md`, `-2`, `additions.verify-1.md`, `-3` |
| **Bloque I** | **605** | **726** | **50 (0 / 9 / 3 / 27 / 11)** | **676** | **108/108** | |

Drop log with reasons: `docs/age-verification/bank/bloque-i/drops.tsv`. Working tools in `docs/age-verification/bank/tools/`:
`official_by_tema.py` (needs the questionnaires as `pdftotext -layout` text), `bank_stats.py` (kept-set mix per tema),
`check_anchors.py` (resolves every draft citation with the platform's resolver; run with `uv run` from `backend/`).

### Mix of kept questions

| Tema | art-compl. / art-preg. / directa / cuál / enunc. / señale / norma | Names article | Negative | Key longest | Diff 1/2/3 | Key a/b/c/d (authored) |
|---|---|---|---|---|---|---|
| I.1 | 42 / 15 / 20 / 10 / 7 / 3 / 2 % | 58 % | 1 | 25 % | 18/28/13 | 15/15/14/15 |
| I.2 | 42 / 12 / 23 / 16 / 5 / 2 / 0 % | 55 % | 1 | 22 % | 19/33/12 | 16/16/18/14 |
| I.3 | 38 / 15 / 23 / 13 / 5 / 3 / 2 % | 53 % | 0 | 25 % | 19/28/13 | 14/15/16/15 |
| I.4 | 31 / 22 / 20 / 16 / 6 / 3 / 2 % | 53 % | 0 | 20 % | 18/33/13 | 16/16/16/16 |
| I.5 | 37 / 14 / 21 / 16 / 7 / 4 / 2 % | 51 % | 0 | 21 % | 18/28/11 | 14/14/14/15 |
| I.6 (profile G) | 21 / 5 / 38 / 21 / 7 / 3 / 5 % | 26 % | 0 | 26 % | 20/29/12 | 16/15/15/15 |
| I.7 | 38 / 13 / 22 / 17 / 7 / 2 / 2 % | 52 % | 1 | 27 % | 17/32/11 | 14/16/15/15 |
| I.8 | 39 / 16 / 22 / 14 / 5 / 3 / 2 % | 55 % | 1 | 22 % | 20/31/13 | 17/16/16/15 |
| I.9 | 37 / 16 / 21 / 16 / 5 / 3 / 2 % | 53 % | 0 | 23 % | 19/29/14 | 16/15/15/16 |
| I.10 | 36 / 16 / 22 / 14 / 7 / 3 / 2 % | 52 % | 0 | 26 % | 18/28/12 | 15/16/12/15 |
| I.11 | 36 / 18 / 24 / 10 / 7 / 3 / 1 % | 54 % | 0 | 22 % | 19/36/12 | 17/16/19/15 |

Every form is within ±10 points of its profile (N, or G for I.6). The article share is 51–58 % in profile-N temas. Key-longest is counted by characters, as the platform guard counts it. Difficulty 1 runs 17–20 per tema (about 30 %). Authored key positions are kept as written (balanced per tema; 170/170/170/166 over the bloque); the platform shuffles per learner.

### Coverage of official questions

Each writer mapped every official question filed under its tema (`official/I.TT.md`) to kept questions in its
`writer-notes.md`. Official facts no lesson states (so no question is possible) are in open item 3; the rest are covered
from a new angle. Ten drafts were dropped as light rewordings of an official question; each lost fact got a replacement
from another angle where it carried a «Lo que más cae» line (I.3 q064, I.4 q062–q064, I.9 q062).

### Rulings recorded in `verify-spec.md`

Short organ or quantity options of the kind the style guide's § 3 shows do not fail checklist 10 on length; «lightly
reworded» includes same fact and angle with the official key and an official distractor carried over; a descriptive
norm name counts as the «no norm named» form. The two I.11 short-option drops (q053, q059) predate the first ruling and
stand.

## Open items

1. **Closed (session 2).** ~~m01-l02 table without parenthesised citations.~~ Six citations in parentheses; six appointment questions kept. «Nombramientos en otros poderes» cites arts. 122.3, 123.2,
   124.4, 152.1, 159.1 and 160 CE in bare cells; the resolver does not read them, so no question can test those six
   appointments. A prose fix (parenthesised citations) unblocks them.
2. **Closed (session 2).** ~~m01-l02 sentences wider than the norm~~ — rewritten and blind-checked. (verifier notes, `m01-l02.verify-2.md`): the tutela sentence asks
   «español de nacimiento» of every tutor (art. 60.1 CE asks it of the testamentary tutor); the art. 151.2 sentence
   gives sanción after ratification, true only under rule 4.º (rule 5.º puts a provincial referendum first). One-sentence
   R2 fixes with their own blind check.
3. **Official facts the lessons do not state** (no question possible): I.1 — arts. 107, 103.1, 103.3, 117.1 CE; I.3 —
   art. 134.3 CE (conv2024_A P1 35), art. 82.3 CE (an option of conv2022_X P1 8); I.4 — art. 120.2 CE (conv2020 P1 3);
   I.5 — art. 94.1 CE, art. 26 Ley 50/1997, art. 124 CE, art. 86 CE; I.7 — art. 29.2.d Ley 19/2013 (sigilo, conv2020
   P1 5); I.8 — arts. 20.1, 89, 93 LRJSP, arts. 8, 9 Ley 50/1997 (filed under other temas first); I.10 — arts. 133, 147,
   152, 153 CE (conv2020_X P1 11). Writer notes list each. For the scope audit to weigh.
4. **Reading of checklist item 2:** I.10 stems that say «la legislación básica estatal de régimen local» without the
   BOE title were passed as the «no norm named» form (style guide § 2). Kept as the round's reading.
5. **`covers` code for reserve questions:** `official:<code>·P1R·<n>` (writers' convention, now standard).
6. **Closed (session 2).** ~~Platform: question citations to source files.~~ `CourseCitations._anchor` resolves only norm segments, so a question
   citing «fuente: `file`» fails the load even when its lesson cites the file (48 in I.6, 4 in I.11, 1 in I.1; bloque VI
   will need it throughout). Fix when code is released: resolve a `files` segment to `fuente-<file>` when the lesson's
   prose cites it, plus a test that fails before.
7. **Lesson citation forms fixed this session (markup only, no fact changed):** m01-l01, m01-l06, m01-l11 cited saved
   pages as bare `sources/otros/<file>` inside the parenthesis, which the grammar does not read; now «fuente: `<file>`»
   as in the m06 lessons (38 citations). m01-l09 «(disp. trans. 2.ª / 5.ª CE)» → «(disposición transitoria segunda /
   quinta CE)», and I.9 q019 and q022 normalised to the same form. m02-l02 and m02-l03 still carry 13 bare paths
   (bloque II round). Goldens not regenerated (pause).
8. **Closed (session 2):** line replaced by art. 13.2 CE. ~~I.1 lmc-6 («La Constitución tiene un título preliminar y diez títulos (CE)»)** has no citable unit: «(CE)» is not a
   citation and no article states it. Its two questions (q002, q003) were dropped at the resolver. Needs a lesson
   decision: a different «Lo que más cae» fact, or a citable unit for the structure.
9. **RD 33/1986 art. 47.1 vs art. 61.s LRJSP** (separación del servicio: Consejo de Ministros vs Ministro). The
   consolidated RD 33/1986 file (1991) predates the LRJSP; I.8 asks it only as a distractor wrong under both. Matters
   for IV.6.
10. **Closed (session 2).** ~~I.1 «Las reformas» paragraph~~ — now date and article only. cites `boe-analisis-ce.xml` for what each reform was about; the page gives only
    article and date (verifier note, `m01-l01.verify-1.md`). Wider than the source; R2 fix.
12. **Smaller lesson notes from verifiers** (no verdict changed): m01-l07 art. 2.1 qualifier read as covering the whole
    list, mutuas left out; art. 15.2 condition left out; m01-l08 art. 69.2 «sin perjuicio…» left out; m01-l11 opening
    sentence says 2016 DOUE versions while «Normativa» says 15-03-2025; m01-l01 «Antes de plantearla» (art. 35.2 LOTC
    says «Antes de adoptar mediante auto su decisión definitiva»); m01-l10 art. 21.1 «salvo los supuestos…» left out.
11. **m01-l07 l. 72** names «Ministerio de la Presidencia» (art. 10.1 Ley 19/2013) without «(hoy: …)» (convention 1).

## Ten I.5 questions for the reader

Ten kept I.5 questions drawn with `random.Random(20261018).sample(kept, 10)` over the 57 kept, shown as authored (the
platform shuffles the options per learner). The key is marked **(clave)**.

**1. `m01-l05-q005`** · art. 107 CE · dificultad 1

> Según la Constitución Española de 1978, ¿qué órgano es el supremo órgano consultivo del Gobierno?
>
> a) El Consejo Económico y Social, cuya composición regula una ley ordinaria.
>
> b) La Comisión General de Secretarios de Estado y Subsecretarios, que preside un Vicepresidente.
>
> c) El Secretariado del Gobierno, como órgano de apoyo del Consejo de Ministros.
>
> d) El Consejo de Estado, cuya composición y competencia regula una ley orgánica. **(clave)**

*Explicación.* El artículo 107 dice: «El Consejo de Estado es el supremo órgano consultivo del Gobierno. Una ley orgánica regulará su composición y competencia». El Consejo Económico y Social es un órgano consultivo en materia socioeconómica, no el supremo órgano consultivo del Gobierno. La Comisión General de Secretarios de Estado y Subsecretarios es un órgano de colaboración del Gobierno y el Secretariado del Gobierno es un órgano de apoyo (arts. 8 y 9 Ley 50/1997); ninguno es consultivo.

**2. `m01-l05-q008`** · art. 2.2 Ley 50/1997 · dificultad 3

> De acuerdo con el artículo 2.2 de la Ley 50/1997, de 27 de noviembre, del Gobierno, corresponde al Presidente del Gobierno crear, modificar y suprimir, por Real Decreto:
>
> a) Los órganos directivos de los Departamentos Ministeriales.
>
> b) Los Departamentos Ministeriales y las Subsecretarías de cada uno de ellos.
>
> c) Los Departamentos Ministeriales, así como las Secretarías de Estado. **(clave)**
>
> d) Las Comisiones Delegadas del Gobierno y sus respectivas Secretarías.

*Explicación.* El artículo 2.2.j) atribuye al Presidente crear, modificar y suprimir, por Real Decreto, «los Departamentos Ministeriales, así como las Secretarías de Estado». Los órganos directivos de los Departamentos los crea el Consejo de Ministros (art. 5.1.i). Las Subsecretarías no figuran en esta letra. Las Comisiones Delegadas las crea el Consejo de Ministros mediante Real Decreto, a propuesta del Presidente (art. 6.1).

**3. `m01-l05-q013`** · art. 18.1 Ley 50/1997 · dificultad 1

> De acuerdo con el artículo 18.1 de la Ley 50/1997, de 27 de noviembre, del Gobierno, en las reuniones del Consejo de Ministros:
>
> a) El Presidente del Gobierno las convoca y preside, y actúa como Secretario el Director del Secretariado del Gobierno.
>
> b) El Presidente del Gobierno las convoca y preside, y actúa como Secretario el Ministro de la Presidencia. **(clave)**
>
> c) El Presidente del Gobierno las convoca y preside, y actúa como Secretario el Subsecretario de la Presidencia.
>
> d) El Vicepresidente primero las convoca y preside, y actúa como Secretario el Ministro de la Presidencia.

*Explicación.* El artículo 18.1 dice: «El Presidente del Gobierno convoca y preside las reuniones del Consejo de Ministros, actuando como Secretario el Ministro de la Presidencia». El Director del Secretariado del Gobierno suple al Secretario de la Comisión General de Secretarios de Estado y Subsecretarios (art. 8.3). El Subsecretario de la Presidencia es el Secretario de esa Comisión, no del Consejo. El Consejo lo convoca y preside el Presidente, no un Vicepresidente.

**4. `m01-l05-q023`** · art. 8.2 Ley 50/1997 · dificultad 2

> De acuerdo con el artículo 8.2 de la Ley 50/1997, de 27 de noviembre, del Gobierno, la Presidencia de la Comisión General de Secretarios de Estado y Subsecretarios corresponde:
>
> a) Al Presidente del Gobierno o, en su defecto, a un Vicepresidente del Gobierno.
>
> b) A un Vicepresidente del Gobierno o, en su defecto, al Ministro de la Presidencia. **(clave)**
>
> c) Al Ministro de la Presidencia o, en su defecto, al Subsecretario de la Presidencia.
>
> d) Al Subsecretario de la Presidencia o, en su defecto, al Director del Secretariado del Gobierno.

*Explicación.* El artículo 8.2 dice que la Presidencia «corresponde a un Vicepresidente del Gobierno o, en su defecto, al Ministro de la Presidencia». El Presidente del Gobierno no preside esta Comisión. El Subsecretario de la Presidencia ejerce la Secretaría, no la Presidencia, y el Director del Secretariado del Gobierno lo suple como Secretario (art. 8.3).

**5. `m01-l05-q032`** · art. 99.3 CE · dificultad 1

> Según el artículo 99.3 de la Constitución Española de 1978, ¿qué mayoría necesita el candidato a la Presidencia del Gobierno en la primera votación de investidura?
>
> a) La mayoría simple de los miembros del Congreso de los Diputados.
>
> b) La mayoría absoluta de los miembros del Congreso de los Diputados. **(clave)**
>
> c) La mayoría de tres quintos de los miembros del Congreso de los Diputados.
>
> d) La mayoría absoluta de los miembros de cada una de las Cámaras.

*Explicación.* El artículo 99.3 dice que el Rey nombrará Presidente al candidato si el Congreso, «por el voto de la mayoría absoluta de sus miembros», le otorga su confianza. La mayoría simple basta solo en la segunda votación, cuarenta y ocho horas después. Los tres quintos no se exigen en la investidura. El Senado no vota la investidura.

**6. `m01-l05-q035`** · art. 100 CE · dificultad 2

> ¿Cuál de las siguientes afirmaciones sobre el nombramiento de los miembros del Gobierno se ajusta a la Constitución Española de 1978?
>
> a) Los Ministros son nombrados por el Rey, a propuesta del Presidente, y separados por el Congreso de los Diputados.
>
> b) Los Vicepresidentes son nombrados por el Rey, previa votación de investidura en el Congreso de los Diputados.
>
> c) Los demás miembros del Gobierno son nombrados y separados por el Rey, a propuesta de su Presidente. **(clave)**
>
> d) Los Ministros son nombrados por el Presidente del Gobierno, previa deliberación del Consejo de Ministros.

*Explicación.* El artículo 100 dice: «Los demás miembros del Gobierno serán nombrados y separados por el Rey, a propuesta de su Presidente». El Congreso no separa a los Ministros; exige la responsabilidad política del Gobierno en su conjunto (art. 113.1). Solo el candidato a Presidente se somete a investidura (art. 99). Los Ministros los nombra el Rey, no el Presidente, y la ley no exige deliberación del Consejo.

**7. `m01-l05-q037`** · art. 101.2 CE · dificultad 2

> Tras la celebración de elecciones generales el Gobierno cesa, pero el Gobierno cesante continuará en funciones:
>
> a) Hasta la votación de investidura del nuevo Presidente en el Congreso.
>
> b) Hasta la constitución de las nuevas Cortes Generales tras las elecciones.
>
> c) Hasta la toma de posesión del nuevo Gobierno. **(clave)**
>
> d) Durante un plazo máximo de dos meses desde las elecciones.

*Explicación.* El artículo 101.2 dice que el Gobierno cesante «continuará en funciones hasta la toma de posesión del nuevo Gobierno». La investidura y la constitución de las Cortes son pasos anteriores, y no ponen fin a las funciones. La Constitución no fija un plazo máximo de dos meses; los dos meses del artículo 99.5 se cuentan desde la primera votación de investidura.

**8. `m01-l05-q053`** · art. 113.4 CE · dificultad 3

> Según el artículo 113.4 de la Constitución Española de 1978, ¿qué consecuencia tiene para sus signatarios que la moción de censura no sea aprobada por el Congreso?
>
> a) No podrán presentar otra durante el resto de la legislatura.
>
> b) No podrán presentar otra durante el mismo período de sesiones. **(clave)**
>
> c) No podrán presentar otra hasta que transcurra un año desde la votación.
>
> d) No podrán presentar otra hasta que transcurran dos meses desde la votación.

*Explicación.* El artículo 113.4 dice que, si la moción no fuere aprobada, «sus signatarios no podrán presentar otra durante el mismo período de sesiones». La limitación no dura toda la legislatura. El año es el plazo entre disoluciones (art. 115.3) y los dos meses son los de la investidura (art. 99.5).

**9. `m01-l05-q055`** · art. 115.2 CE · dificultad 2

> La propuesta de disolución del Congreso, del Senado o de las Cortes Generales queda vedada al Presidente del Gobierno cuando:
>
> a) Esté en trámite una cuestión de confianza ante el Congreso.
>
> b) Esté en trámite el Proyecto de Ley de Presupuestos Generales del Estado.
>
> c) Falten menos de seis meses para el término de la legislatura.
>
> d) Esté en trámite una moción de censura. **(clave)**

*Explicación.* El artículo 115.2 dice: «La propuesta de disolución no podrá presentarse cuando esté en trámite una moción de censura». La Constitución no impide la disolución durante una cuestión de confianza ni durante la tramitación de los Presupuestos. Tampoco fija un límite por la proximidad del fin de la legislatura.

**10. `m01-l05-q059`** · art. 116.3 CE · dificultad 2

> ¿Cuál de las siguientes afirmaciones sobre la declaración de los estados de alarma, de excepción y de sitio es correcta según la Constitución Española de 1978?
>
> a) El estado de alarma lo declara el Gobierno mediante decreto acordado en Consejo de Ministros, previa autorización del Congreso.
>
> b) El estado de excepción lo declara el Gobierno mediante decreto acordado en Consejo de Ministros, previa autorización del Congreso. **(clave)**
>
> c) El estado de sitio lo declara el Gobierno mediante decreto acordado en Consejo de Ministros, dando cuenta al Congreso.
>
> d) El estado de excepción lo declara el Congreso por mayoría absoluta, a propuesta exclusiva del Gobierno.

*Explicación.* El artículo 116.3 dice que el estado de excepción «será declarado por el Gobierno mediante decreto acordado en Consejo de Ministros, previa autorización del Congreso de los Diputados». El estado de alarma no exige autorización previa: el Gobierno lo declara dando cuenta al Congreso (art. 116.2). El estado de sitio lo declara la mayoría absoluta del Congreso, a propuesta exclusiva del Gobierno (art. 116.4), y esa no es la regla del estado de excepción.

