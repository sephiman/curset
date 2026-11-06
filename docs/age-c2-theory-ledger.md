# Theory ledger — age-auxiliar-c2

Round R2, bloque I (temas I.1–I.16), started 2026-11-06. Nothing committed. Requirements v1.2 (R2.3 provenance, section 4);
method as C1's R2 (`docs/age-theory-ledger.md`, whose standing conventions apply).

## How this round runs

- **Spec:** `docs/age-verification/c2/bloque-i/spec.md` (mapping C2 tema → C1 lessons, depth rule, provenance rule for
  writers, conventions, structure, verifier and coverage formats).
- **Question packs:** `docs/age-verification/c2/bloque-i/questions/<lesson>.md`, built by
  `docs/age-verification/c2/bloque-i/tools/question_packs.py` from the official-exams ledger and the R0a parsed
  questionnaires. «coverage» = vigente or vigente-con-nota, 2022–2025, first tema; «reference» = OEP 2020, second tema,
  or excluded.
- **Writers** (sonnet): derive each lesson from its C1 lesson(s), keeping kept sentences byte-identical; notes in
  `docs/age-verification/c2/bloque-i/writer/`.
- **Provenance** (`backend/scripts/provenance.py`): splits a lesson into sentences (paragraphs and list items at sentence
  ends, one per table row; wrapped lines joined), finds each sentence's governing citations (its own; else the next cited
  sentence of its paragraph, else the previous; a list item or row without one takes the last citation of the paragraph
  that introduces it), and inherits C1's verification only when a C1 sentence has the same text and the same governing
  citations, each resolving to a file with the same sha256 in both snapshots. The C1 report is chosen by `git blame` of
  the C1 lines (newest commit): R2 commits → `docs/age-theory-ledger.md` (C1 did not keep per-sentence tables), r2b →
  `docs/age-scope-audit.md`, esquema rounds → `docs/age-verification/bloque-*/esquemas`, the November audit →
  `docs/age-verification/audit-2026-11`.
- **Verifiers** (opus, blind): the non-inherited sentences of each lesson, `pending/<lesson>.md` → `verify/<lesson>.md`. `pending/` is a working folder (`provenance.py plan` rebuilds it) and was removed at close; the records quote every sentence.
- **Records:** `docs/age-verification/c2/bloque-i/<lesson>.md`, one line per sentence, «verificado en C1: <report>» or
  «verificado: PASS · <report>». `backend/tests/test_provenance.py` audits every written bloque I lesson and the glossary
  in the pipeline (unit tests written and run failing first).

## Sources added this round

- `content/age-auxiliar-c2/sources/otros/`: `boe-analisis-ce.xml` (I.1, the CE reforms), `ue-consejo.html`,
  `ue-parlamento-europeo.html`, `ue-comision-europea.html`, `curia-tribunal-de-justicia.html`,
  `curia-tribunal-general.html` (I.10, head-counts) and `ue-paises.html` (I.10, accession years, for 2025-P1-17),
  copied from C1 with the same sha256 and indexed in `fuentes.yaml` (origen «copia de C1»). No live re-check this
  round; C1's comprobación is carried over in each entry. `ue-paises.html` is page 1 of 2 of the live list (Alemania to
  Lituania): the lesson marks its lists «entre otros».
- `content/age-auxiliar-c2/sources/normativa/BOE-A-2024-519_rd-1-2024-comisiones-delegadas_2026-04-01.pdf`: Real
  Decreto 1/2024, de 9 de enero, por el que se establecen las Comisiones Delegadas del Gobierno (I.6, for 2025-P1-10,
  art. 6.4.a). New download: BOE open-data metadata read 2026-11-06 (estatus_derogacion N, vigencia_agotada N,
  fecha_actualizacion 2026-04-01). New `normativa.yaml` entry, tema I.6.
- `fuentes.yaml` `lessons:` now lists the lessons that cite each file (15 files cited); `source-index.json` rebuilt
  (`scripts/index_sources.py`, C2 only changed).
- Not found: the Council presidency order (2024X-P1-18). consilium.europa.eu answers 403 to curl and to the
  Playwright fetcher of `docs/age-verification/tools/fetch_rendered.mjs`; EUR-Lex (Decisión (UE) 2016/1316) is behind a
  WAF per C1's ledger. Open item.

## Summary

Words are `wc -w` of the lesson file, everything counted. «Sentences» are the provenance units (paragraph and list-item
sentences, table rows, «Lo que más cae» and «Normativa» lines; a sentence repeated verbatim in one lesson counts once).
«FAIL (fixed)» counts FAIL rows over the first pass and the re-checks; every one was fixed and its replacement passed a
re-check by a verifier other than the one that proposed it. «Coverage» is the coverage check as run, before its fixes
(see «Coverage»).

| Tema | Lesson | Words | Sentences | Inherited from C1 | Verified here | FAIL (fixed) | Coverage (covered / questions) | Glossary |
|---|---|---|---|---|---|---|---|---|
| I.1 | `m01-l01` | 2,374 | 124 | 106 | 18 | 2 | 7 / 7 | 8 |
| I.2 | `m01-l02` | 3,128 | 162 | 154 | 8 | 1 | 9 / 9 | 7 |
| I.3 | `m01-l03` | 4,083 | 189 | 177 | 12 | 0 | 6 / 6 | 14 |
| I.4 | `m01-l04` | 2,947 | 144 | 133 | 11 | 1 | 6 / 7 | 6 |
| I.5 | `m01-l05` | 2,592 | 122 | 110 | 12 | 1 | 10 / 10 | 10 |
| I.6 | `m01-l06` | 2,064 | 111 | 76 | 35 | 0 | 3 / 3 | 3 |
| I.7 | `m01-l07` | 3,690 | 152 | 139 | 13 | 1 | 7 / 7 | 4 |
| I.8 | `m01-l08` | 3,699 | 161 | 142 | 19 | 1 | 11 / 11 | 10 |
| I.9 | `m01-l09` | 5,137 | 252 | 235 | 17 | 1 | 6 / 6 | 14 |
| I.10 | `m01-l10` | 3,304 | 160 | 147 | 13 | 2 | 6 / 8 | 2 |
| I.11 | `m01-l11` | 8,010 | 282 | 219 | 63 | 3 | 15 / 15 | 16 |
| I.12 | `m01-l12` | 3,542 | 119 | 94 | 25 | 2 | 3 / 3 | 10 |
| I.13 | `m01-l13` | 12,249 | 402 | 353 | 49 | 1 | 8 / 8 | 25 |
| I.14 | `m01-l14` | 11,445 | 404 | 355 | 49 | 2 | 10 / 10 | 18 |
| I.15 | `m01-l15` | 3,417 | 118 | 91 | 27 | 2 | 8 / 8 | 18 |
| I.16 | `m01-l16` | 3,436 | 97 | 61 | 36 | 5 | 8 / 8 | 8 |
| **Total** | | 75,117 | 2999 | 2592 | 407 | 25 | | 173 |

Every written lesson passes `test_provenance.py`: 2,999 sentences, 2,592 inherited from C1 (86 %), 407 verified in
this round. The first pass sent 407 sentences to four Opus verifiers; 25 FAILs, all fixed and re-checked PASS.

### FAIL classes

Same as C1: a dropped condition or exception of the article (I.5 art. 102.2 CE «en el ejercicio de sus funciones»; I.4
art. 65.1.º LOPJ «salvo que corresponda… al Tribunal Central de Instancia»; I.10 art. 1.4 Reglamento interno «salvo
Asuntos Exteriores»; I.11 arts. 24.1, 39.2–3 and 70.4 LPAC; I.12 art. 4.2.b) LOPDGDD, twice: the first replacement still
dropped «en nombre propio»; I.13 art. 69.2 TREBEP; I.14 art. 96.1.b) TREBEP; I.16 arts. 12.2 LO 3/2007, 4.2 and 2.j)
RDL 1/2013), a selective list that read as complete (I.15 ingresos corrientes; I.16 infracciones graves), an
approximation (I.1 the reform majorities), and «Normativa» lines out of step with the prose (I.1, I.10). New in C2: an old
ministry name kept without its «(hoy: …)» note in a new sentence (I.14 art. 10.2 LGSS), and a structure sentence
written as a statement of the law (I.15 «fases del ciclo»). I.2's intro made the LOTC read as part of the CE.

### Per tema

- **I.1** (from C1 m01-l01 without TC and reforma). New: «Características» (disposición derogatoria 3, arts. 167–168,
  137), arts. 8.1, 19, 20.1.d, 27.1/27.4, 32.1, 37.1. No doctrinal list of «características» (escrita, rígida…): no
  source in `sources/normativa`.
- **I.2** (C1 m01-l01 TC and reforma + m01-l02). New: intro, five «Lo que más cae» lines, Normativa.
- **I.3** (C1 m01-l03; the Defensor del Pueblo from C1 m01-l01). New: «Pérdida de la condición de Diputado» (art. 22
  Reglamento del Congreso, for 2020-P1-8). Cambio pendiente of art. 23 «en vigor en la XVI legislatura», as C1.
- **I.4** (C1 m01-l04). New: arts. 120.1–2 and 125 CE, art. 65.1.º LOPJ in the LO 1/2025 wording, and (coverage fix)
  the second sentence of art. 122.2 CE.
- **I.5** (C1 m01-l05). Cut: Gobierno–Cortes relations, Secretariado and Gabinetes. New: Plan Anual Normativo (art. 25
  Ley 50/1997). The one C1 esquema the writer had copied was removed (esquemas are round R2c).
- **I.6** (C1 m01-l06). 35 of 111 sentences verified: the fresh copies of two Portal pages have a different sha256 from
  C1's, so every sentence citing them was re-verified. New: the ten IV Plan compromisos, the Comisión Delegada del
  Gobierno para la Agenda 2030 (RD 1/2024, new source). The inherited line «se articula en cinco ejes» was questioned by a
  verifier; the IV Plan PDF says «cinco ejes o áreas», so it stands.
- **I.7** (C1 m01-l07). Cut: art. 22, DA 4.ª, DA 6.ª, DF 9.ª. New: arts. 29.1.d and 29.2.d.
- **I.8** (C1 m01-l08). «Otros órganos administrativos» read as art. 5 LRJSP (órgano administrativo), the unidades
  administrativas (art. 56) and the órganos colegiados of the periférica (arts. 78–79); the only pack question that uses
  the idea is 2024-P1-11 (art. 5.1). Ministry list stays dated «a 16-10-2026».
- **I.9** (C1 m01-l09 + m01-l10). Cut: financiación (arts. 156–158), the 151.2 procedure, municipios de gran población,
  comarcas, áreas metropolitanas, mancomunidades, art. 4 LBRL. New: art. 149.1.15.ª and 17.ª.
- **I.10** (C1 m01-l11). Cut: valores, competencias, ingreso y retirada. New: art. 240.3 TFUE, accession years
  (`ue-paises.html`), the two órganos jurisdiccionales of the TJUE (Curia pages).
- **I.11** (C1 m03-l03 + parts of m03-l02). New from the LJCA PDF: arts. 12.1.a, 18, 19.1.d/e/f/k, 19.2, 20, 21.1, 22,
  23.3, 24, 26, 27.1, 28, 29.2; from the LPAC: arts. 3, 5, 11, 32.4–5, 48.3, 70, 81.3, 99–100, 106.2; art. 22.10
  LO 3/1980. Cut: LRJSP órganos colegiados, convenios and organismos públicos, electronic relations, motivación, the
  grado-de-parentesco paragraph (cited the Código Civil, which C2 does not have).
- **I.12** (C1 m02-l04). Cut: videovigilancia, AEPD and autoridades de control, sanciones, derechos digitales. New: art.
  4.9 and 18.1 RGPD, art. 4.1–2 LOPDGDD.
- **I.13** (C1 m04-l01 to m04-l04 + provisión of m04-l05). 12,249 words: every area the writer kept is named by the
  programme sentence or asked by a pack question (adquisición and jubilación by OEP 2020 questions). Not named and not
  asked, kept: «Las competencias en materia de personal» and «Rehabilitación» (candidate trims for the reviewer). New:
  art. 75 TREBEP, RCP asientos (RD 2073/1999 arts. 10.1, 14.4, 15.1), «Programación de efectivos» (art. 69 TREBEP, arts.
  107–108 RDL 6/2023), art. 88.2 TREBEP, art. 2 Orden TDF/379/2024, arts. 61.1 and 64.4 RD 364/1995. Cut: everything
  citing Ley 53/1984 (not in C2), LPAC cómputo sentences.
- **I.14** (C1 m04-l05, m05-l04 funcionarios only, m04-l06 disciplinario only, m04-l07). 11,445 words. New: art. 16 TREBEP
  (with the DF 4.ª.1 caveat), arts. 29, 37.1–2, 53.5, 54.1 TREBEP, art. 5.1–2 RD 462/2002, arts. 10.2–3 and 250.2 LGSS. Cut:
  incompatibilidades, personal laboral pay, nóminas, devengo and pago (Ley 33/1987, Orden PRE/1576/2002 not in C2), the
  2026 pay tables (no SEPG source saved in C2).
- **I.15** (C1 m05-l01, l02, part of l03). «Fases del ciclo presupuestario» (decision left open by R1): elaboración and
  aprobación (art. 134.1 CE), ejecución (art. 73.1 LGP), control (art. 140 LGP), presented as the lesson's structure. CE is
  cited (arts. 134.1–4, 135.3) and listed in Normativa; `normativa.yaml` still tags CE without I.15 (the tag is metadata
  only; not changed). Cut: everything resting on the IOC and the Orden de documentos contables, modificaciones
  presupuestarias, plurianuales, vinculación.
- **I.16** (C1 m03-l07). Every kept sentence on RDL 1/2013 and Ley 39/2006 checked against the Ley 4/2026 wording. New:
  arts. 10, 12.2–3 LO 3/2007; art. 9.1/9.3 Ley 4/2023; arts. 2.j), 4.1–2, 95 RDL 1/2013; arts. 7, 9.1–2 Ley 39/2006.

## Coverage

Coverage check (two Opus checkers, `docs/age-verification/c2/bloque-i/coverage/`): 134 «coverage» questions (vigente
or vigente-con-nota, 2022–2025, first tema), 131 COVERED as checked, 3 MISS. Before the check, two misses the writers
reported were fixed with new sources: 2025-P1-17 (Eslovenia, 2004; `ue-paises.html`) and 2025-P1-10 (Comisión Delegada
del Gobierno para la Agenda 2030; RD 1/2024).

| Question | Tema | Fix |
|---|---|---|
| 2024X-P1-3 | I.4 | Added the second sentence of art. 122.2 CE (CGPJ: estatuto by ley orgánica). Verified PASS. |
| 2024-P1-14 | I.10 | Added «la institución la forman dos órganos jurisdiccionales» from the two Curia pages. Verified PASS. |
| 2024X-P1-18 | I.10 | **Open.** Presidency trio from 1-1-2025 (Polonia, Dinamarca, Chipre): no source reachable (see «Sources»). The lesson gives the rule (trios of three States for eighteen months). |

After the fixes: 133 of 134 covered. No pack question is marked «Clave oficial discutida». Reference questions whose
fact is not in the lesson (informational): 2024X-R1-1 (I.6, dudosa; Comisión Permanente del Consejo de Desarrollo
Sostenible, order not in sources), 2020X-P1-18 (I.12, «responsable del fichero» of the repealed RD 1720/2007), 2024-P1-18
(I.13, dudosa; Resolución de 7-05-2014 not in sources), 2020X-R1-1 (I.14, art. 27 TREBEP, personal laboral pay).

## Glossary

- `content/age-auxiliar-c2/glossary.yaml`: 173 entries, all copied from C1 under R2.3 and inherited
  (`docs/age-verification/c2/bloque-i/glossary.md`; `test_provenance.py` checks term, definitions, citations and
  cited-file sha256 against C1). Built by `tools/glossary_candidates.py`: of C1's 277 entries, 176 have their term in a C2
  bloque I lesson; 175 have identical cited files. Kept under C1's own rule: the C2 lesson that inherits the C1 origin
  uses the term, or two C2 lessons do, or (single-lesson terms) the definition cites the article that defines it.
- Not copied: `g-subvencion` (cited file differs; C2 does not teach subvenciones), `g-competencia-exclusiva` (its EU
  sense has no C2 lesson), `g-plantilla` (the only use is a false friend in I.9).
- Origin is the C2 lesson; C1's `link_except` lists (C1 lesson ids) were dropped and redone from C2's
  `glossary-links.es.txt`: 10 entries now carry `link_except` (inviolabilidad del domicilio in I.1; «funciones
  directivas» in I.13; «oposición» as an objection in I.7, I.11, I.12; the ministry name «Agenda 2030» in I.8; Seguridad
  Social «servicios comunes» in I.7, I.13, I.15; moción de censura and cuestión de confianza of the Alcalde (I.9) and of
  the Commission (I.10); «Ministro interesado» (I.8) and the RGPD «interesado» (I.12); the LPAC trámite of información
  pública (I.11); convenios colectivos (I.14)). `glossary-links.es.txt` read line by line: 128 web marks.
- No glossary definition was written or changed in C2, so none needed its own verification.

## Course summaries

`course.yaml`: module `m01` and the 16 lesson summaries, written by the coordinator in C1's factual style (no «La
lección…» openers), at most three sentences each. Blind check (`verify/summaries.md`): 14 PASS, 3 FAIL (`m01` put the
EU under the Constitution and left out the TC; `m01-l10` read as covering all seven institutions; `m01-l14` gave the 2011
Régimen General rule to every funcionario), replaced; the `m01-l05` investidura sentence was also tightened after a
note. Re-check (`verify/summaries-recheck-1.md`): 4 PASS.

## Checks and suites

Run on the final tree:

- `test_provenance.py`: unit tests written and run failing first (import error, then the course test failing on the
  first written lesson without a record); 28 pass. The course test runs in the pipeline for every written C2 bloque I
  lesson and the glossary.
- Citations golden regenerated (`UPDATE_CITATIONS=1`) and read: 1,896 prose citations, 0 esquema rows, 91 Normativa
  norms, 3 «naming a norm normativa.yaml lacks» (the three «Otras fuentes» lines, C1's form). One prose citation, «(art.
  26.1.b y c LBRL)», resolved to no norm; rewritten «(art. 26.1.b) y c) LBRL)» and re-verified.
- `lesson-refs.es.txt` (5 references, 0 dangling) and `glossary-links.es.txt` regenerated and read.
- List-shape: three «Normativa» lines ending in «art. N.» read as stray list markers (I.8, I.13, I.14); reworded with a
  gloss or reordered, re-verified.
- Never-coins and i18n: in the backend and frontend suites below.
- crypto-futures and C1: no file under `content/crypto-futures/` or `content/age-administrativo-c1/` changed.
- Android bundle: re-exported to a scratch folder, byte-identical to `dist/bundle/`.
- Frontend (`npx vitest run`): 715 passed, 81 skipped, 0 failed. `tsc -b` clean.
- Backend (`uv run pytest`, Docker running): 1,646 passed, 23 skipped, 0 failed (28 of them `test_provenance.py`).
- `ruff check`, `ruff format`, `mypy` clean on `scripts/provenance.py` and `tests/test_provenance.py`.

## Open items

1. ~~2024X-P1-18~~: closed (decision 3 below).
2. ~~I.10 intro~~: fixed in C1 and inherited (decision 2 below).
3. ~~I.13 and I.14 length~~: the two candidate sections cut (decision 1 below).
4. **RDL 31/2026**: still unconvalidated on 2026-11-05; if derogated, the RDL 4/2000, LGSS and RDL 670/1987 entries
   revert (I.14 cites RDL 4/2000 art. 19.1, first paragraph only, unchanged by the RDL).
5. **Esquemas** are round R2c. The provenance audit already reads table rows, so esquema rows will need their own
   records then.
6. **Pipeline coupling:** an edit to a C1 sentence that C2 inherits now fails C2's provenance test until C2's record is
   redone (`provenance.py record`). That is the intent of R2.3, but C1 rounds need to know it.
7. **Writer notes** (`writer/`) list further unresolved points per tema (I.1 no doctrinal «características»; I.4 the
   past LO 1/2025 transitory dates kept; I.11 cut LRJSP parts restorable from C1 m03-l03; I.14 the RDL 6/2023 /
   DF 4.ª.1 question; I.15 CE not tagged I.15 in `normativa.yaml`).

## Decisions after bloque I (Juanjo, 2026-11-06), applied before bloque II

1. **Scope cuts in I.13.** «Las competencias en materia de personal» (Ley 30/1984 arts. 2–3, RD 829/2023 arts. 22.2–3,
   RD 1009/2023 art. 21.C) and «Rehabilitación» (art. 68.1 TREBEP) removed: neither named by the C2 programme nor asked
   in 2020–2025 (both sections were in I.13 only; I.14 has neither). Changed with them: the intro sentence that named the
   competencias («Varias reglas siguen en la Ley 30/1984…»), the TREBEP «Normativa» line (no 68.1), the Ley 30/1984 line
   (no arts. 2–3; a verifier then asked it to list the BOE notes the prose cites, as I.14's line does), and the RD 829/2023
   and RD 1009/2023 lines (removed). Re-verified: `verify/m01-l13-recheck-3.md` (1 FAIL, fixed) and `-recheck-4.md`.
   I.13 is now 343 inherited + 50 verified sentences. Glossary: no entry lost its second lesson (only
   `g-potestad-reglamentaria` went from three lessons to two), so the waiting list stays empty.
2. **I.10 intro fixed in C1 first.** C1 `m01-l11`: «La lección sigue sus versiones consolidadas a 15 de marzo de 2025,
   cuyo texto de base se publicó en el Diario Oficial de la Unión Europea C 202, de 7 de junio de 2016.» Blind check PASS
   (`docs/age-verification/bloque-i/m01-l11-intro-2026-11-06.md`); note in `docs/age-theory-ledger.md`. C2 `m01-l10`
   carries the same sentence and inherits it. `provenance.py` now takes the report of a C1 sentence changed outside a C1
   round from `_C1_SENTENCE_REPORTS`, and for a C1 sentence whose lines are uncommitted only because a neighbour was
   re-flowed it blames the sentence where it sits in HEAD. Follow-up the verifier suggested, not applied (only one C1
   sentence was authorised): the next sentence could read «Esas versiones todavía cuentan al Reino Unido (art. 52.1
   TUE).»; as written it is still true.
3. **Council presidency trio (2024X-P1-18) closed.** With the e2e Playwright Chromium, a full browser user agent and a
   wait for «networkidle», both sites served the pages (the earlier attempt without the wait got 403): the Decisión (UE)
   2016/1316 PDF from EUR-Lex (3 pages, annex with the order 2016–2030) and the Council presidency page, saved as
   `eurlex-decision-2016-1316.pdf` and `consilium-presidencia.html` with URL, date and sha256 in `fuentes.yaml`. I.10
   «La Presidencia» now states the order (Polonia enero-junio 2025, Dinamarca julio-diciembre 2025, Chipre enero-junio
   2026) and the trio. Verified PASS (`verify/m01-l10-recheck-4.md`). Coverage: 134 of 134.
4. **CLAUDE.md**: a round that edits a C1 lesson sentence inherited by C2 must rerun `provenance.py` for C2 and update its
   records in the same round.


# Bloque II — temas II.1–II.12 (2026-11-06)

Spec: `docs/age-verification/c2/bloque-ii/spec.md` (bloque I's spec plus the mapping and the ofimática rules: C1's bloque VI
rules, items derived from C1's m06 lessons, C2's own `docs/age-c2-ofimatica-index.md` as the coverage map, no word
ceiling). Same pipeline as bloque I: four Sonnet writers (II.1–II.4, II.5–II.7, II.8–II.9, II.10–II.12), blind Opus
verifiers, re-checks always by a verifier other than the one that proposed the fix, coverage check, then a fix pass for
the coverage MISSes (two Sonnet writers) verified the same way. Records: `docs/age-verification/c2/bloque-ii/<lesson>.md`;
`test_provenance.py` now audits `m01` and `m02` (`BLOQUE_DIRS` in `provenance.py`).

## Summary

«Coverage» here counts both tables of the coverage report as run, before the fix pass: the pack's coverage questions
plus, for II.5–II.12, the index's recurring families and programme features (see «Coverage» for what the fix pass closed).

| Tema | Lesson | Words | Sentences | Inherited from C1 | Verified here | FAIL (fixed) | Coverage (covered / questions) | Glossary |
|---|---|---|---|---|---|---|---|---|
| II.1 | `m02-l01` | 2,288 | 81 | 37 | 44 | 2 | 8 / 8 | 2 |
| II.2 | `m02-l02` | 3,022 | 101 | 83 | 18 | 0 | 11 / 11 | 3 |
| II.3 | `m02-l03` | 4,388 | 149 | 87 | 62 | 1 | 11 / 11 | 12 |
| II.4 | `m02-l04` | 4,328 | 148 | 113 | 35 | 5 | 14 / 16 | 6 |
| II.5 | `m02-l05` | 2,005 | 98 | 50 | 48 | 10 | 19 / 30 | 5 |
| II.6 | `m02-l06` | 1,889 | 90 | 51 | 39 | 8 | 21 / 23 | 5 |
| II.7 | `m02-l07` | 1,976 | 92 | 69 | 23 | 6 | 24 / 35 | 5 |
| II.8 | `m02-l08` | 2,467 | 127 | 68 | 59 | 12 | 21 / 32 | 5 |
| II.9 | `m02-l09` | 2,246 | 119 | 64 | 55 | 8 | 31 / 43 | 2 |
| II.10 | `m02-l10` | 2,411 | 115 | 68 | 47 | 4 | 25 / 33 | 5 |
| II.11 | `m02-l11` | 2,448 | 128 | 73 | 55 | 8 | 25 / 35 | 4 |
| II.12 | `m02-l12` | 2,044 | 107 | 66 | 41 | 2 | 29 / 30 | 5 |
| **Total** | | 31,512 | 1355 | 829 | 526 | 66 | | 59 |

All 28 written lessons pass `test_provenance.py` (40 tests). Bloque II: 1,355 sentences, 829 inherited from C1 (61 %),
526 verified here, 66 FAILs fixed and re-checked PASS.

## Sources added (bloque II)

- **Copied from C1, same sha256 (R4.2):** the 142 `sources/otros/` files that C1's m02 and m06 lessons cite and C2 lacked
  (`fuentes.yaml`, comment «Ronda R2, bloque II»). 62 of them end up uncited (C2 cut those items) and keep
  `lessons: []`, as R0a's unused pages do. `ms-copilot-introduccion.html` is R0a's fresh copy (different sha256).
- **New pages saved by the writers** (official Microsoft pages in Spanish; RFCs, W3C, Apache, Google, WordPress.org
  España, Python, Intel, HP, Moodle and the SGAD catalogue where no Microsoft page applies): 99 kept, each recorded in a
  writer fragment `docs/age-verification/c2/bloque-ii/writer/*-fuentes.yaml` and merged into `fuentes.yaml` after a
  sha256 check. Dropped after verification as inadmissible for a general concept: `lenovo-flops.html`,
  `lenovo-perifericos.html`, `corsair-disipador-termico.html` (files removed). `moodle-open-source.html` (English) was
  replaced by the Spanish page `moodle-codigo-abierto.html`. Weak but kept, with the verifier's note: `hp-plotter-designjet.html`
  (a vendor page; the page says «plotter»), `intel-4004-aniversario.pdf` (the maker's press release),
  `wordpress-cms.html` (the CMS label is only in its title), the SGAD catalogue PDF (a RedIRIS mirror copy of the
  Ministerio's 2016 edition; hacienda.gob.es timed out).
- **New norms:** Reforma del artículo 49 CE, de 15 de febrero de 2024 (BOE-A-2024-3099, for 2025-P2-2) and Ley 34/2002
  (LSSI, consolidated 18-12-2025, for 2024-R2-1: its DA 5.ª, now repealed). New page: `boe-ce-1978-original.pdf`, the
  BOE of 29-12-1978, for the original wording of art. 49 («disminuidos físicos, sensoriales y psíquicos»).
- `source-index.json` rebuilt for C2 only.

## Per tema

- **II.1, II.2** split C1's m02-l01: II.1 keeps the whole art. 4 RD 208/1996 list; II.2 the servicios de información,
  cartas de servicios, quejas y sugerencias and the derecho de petición (LO 4/2001; no pack asks it, kept as C1's
  section because the programme names «peticiones»). RD 366/2007 art. 13: today's wording, with the RD 707/2026 change
  (02-01-2027) as cambio pendiente.
- **II.3** (C1 m02-l02): new «El acceso a los documentos», «El Sistema de Archivos», REG-AGE (Orden PCM/1382/2021). Cut:
  Patrimonio Documental (art. 49.2–5 Ley 16/1985), art. 55.
- **II.4** (C1 m02-l03): new «Principios» (art. 2 RD 203/2021), art. 11 LPAC, Orden HAP/1949/2014 arts. 2 and 4. The
  disputed key 2024X-P2-9 is stated with both sources (the portal page and the Orden). Cut: RD 1112/2018 arts. 12–13 plazos,
  STC 100/2019.
- **II.5–II.12** (C1 m06-l01 … m06-l08): list-shaped, C1 items kept byte-identical where C2 needs them (II.5 also cut the
  ENS item: C2 has no ENS entry and the programme does not name it). Retired features not described. Outlook items name
  «Outlook clásico» / «nuevo Outlook» where pages differ. Where two Microsoft pages disagree, both are stated with
  their sources (Outlook «no leído»: Ctrl+U on one page, Ctrl+S on the Spanish-layout shortcuts page; Enviar y recibir:
  «Alt+J, S» and «Alt, J, S» on the same page).

### FAIL classes (bloque II)

Garbled machine-translated paths quoted as labels (II.6 «Propiedades de red & Internet», II.8 «Seguimiento de
cambios», II.9 «Información del archivo ›»); facts that a page gives only in its Windows 10, macOS or web tab (II.7
Bibliotecas, Acceso rápido, Liberador; II.8 Editor, «Luego por», Ordenar tabla); partial lists read as complete (II.6
desktop icons, II.7 limpieza, II.10 formats and views); the client not named for an Outlook feature (five items); US-keyboard
shortcuts from `ms-word-atajos.html` / `ms-word-subrayar.html` (exam style §12 item 18); a dated source stated as current
(II.12 RFC 1591); and inadmissible vendor pages (II.5).

## Coverage (bloque II)

Coverage check: `docs/age-verification/c2/bloque-ii/coverage/`. II.1–II.3 and II.12 had no MISS among the pack's coverage
questions. The fix pass (`writer/<lesson>-fixes.md`) closed, among others: 2025-P2-2 (old art. 49 wording),
2024X-R2-2 (GEISER, SGAD catalogue), 2024-R2-1 (partly: the LSSI DA 5.ª is repealed and its text is not in the BOE
consolidation; the lesson states its title and that it is repealed), II.5 data types, CAD, binary and other numeral
systems, Windows as a multi-user system, input and output devices, OCR, Moodle; II.6 Red e Internet (VPN, acceso
telefónico), Autoguardado and the Enlace Móvil iPhone/Android difference (disputed key 2024-P2-18: both stated);
II.7 the default libraries; II.8 Diseño › Formato del documento; II.9 «#####» (the page states both causes, so the key
2025-P2-34 is now supported), TRUNCAR decimals, DIAS, DIASEM, RENDTO and CUPON.DIAS; II.10 HTML import (partly), DifFecha,
report export; II.11 the classic ribbon tabs.

Still MISS (coverage questions), «sin fuente»: no admissible official page states the fact.

| Tema | Questions | Why |
|---|---|---|
| II.5 | 2024-P2-15 (disipador), 2024X-P2-32 (FLOPS) | only vendor glossaries (dropped as inadmissible) |
| II.7 | 2025-R2-1, 2024-P2-20 (Agrupar por), 2024X-P2-40 (Agregar columnas), 2024-P2-19 (energy in Task Manager), 2024X-P2-42 (Diagnóstico de memoria), 2024-R2-3 (Centro de movilidad), 2022-P2-22 (drag Este equipo) | only Microsoft Q&A / Community threads |
| II.8 | 2024-P2-27 (Ctrl+<), 2024X-P2-13 (Ctrl+G), 2022-P2-35 (nota al pie), 2024X-P2-11 (3D model), 2024X-P2-12 (Tab in the last cell) | Spanish-keyboard shortcuts: no Spanish-layout page (R0a open item, check on a Spanish-locale install); the others only on Mac/web tabs or not on any page |
| II.9 | 2024-R2-4 (Inmovilizar fila superior / primera columna) | only the Mac page lists them |
| II.10 | 2025-P2-25 (deleting a record cannot be undone), 2024X-P2-22 («Único»), 2022-P2-45 (form types); 2025-P2-38 partly | not on any saved or found page |
| II.11 | 2024X-P2-25 (member address in a group), 2022-P2-50 (Carpeta › Marcar todos como leídos) | the label is only on Outlook.com/web pages |

Ledger notes owed (official-exams ledger, not changed here): 2022-P2-46 (Outlook Ctrl+3 = Contactos in Outlook 2019; the
current page gives Ctrl+3 = Copilot, Ctrl+4 = People) has no «Etiqueta actual» note.

## Glossary (bloque II)

59 entries copied from C1 (origin the C2 lesson; all inherited, recorded in `docs/age-verification/c2/bloque-i/glossary.md`
under «Bloque II»): `glossary.yaml` now has 232. Not copied: `g-copia-de-seguridad` (only one C2 lesson, origin outside
its C1 mapping). `link_except` added after reading `glossary-links.es.txt` (169 web marks): «interesados» and Seguridad
Social «Servicios Comunes» (II.2), group-policy «directiva» (II.6, II.7), ribbon key tips «accesos directos» (II.8),
«acceso rápido» as a shortcut or the Quick Access Toolbar (II.6, II.8, II.9), a page title «Información general» (II.9).

## Summaries (bloque II)

`course.yaml`: module `m02` and the 12 lesson summaries (writers' proposals; the four «La lección…» openers rewritten).
Blind check `verify/summaries.md` (bloque II folder): 12 PASS, 1 FAIL (`m02-l03` left out the Ley 16/1985), replaced and
re-checked PASS (`verify/summaries-recheck-1.md`).

## Unconfirmed Spanish labels (from the writers and verifiers)

«Corregido» (Access number format; the page's label), «ChartDesign» (Excel; printed untranslated on the page), «Tiempo»
vs the exam's «Hora» (Word field), «Más subrayados», «De un archivo» / «Desde archivo» (Access HTML import), «Único»,
«Retrasar entrega» path, «Aplicaciones predeterminadas» (garbled path), «VPN de red & Internet» (garbled path, quoted as
printed). Garbled paths are read only in their single coherent order, with the verifier's note.

## Tool fixes this bloque

- `provenance.py`: `BLOQUE_DIRS` (m01 → bloque-i, m02 → bloque-ii); `_BLOQUE` gained m06 (a writer's fix: C1 bloque VI
  lessons had no report folder).
- `apply_fails.py`: a replacement for a list item no longer doubles the «- » marker (it did once, II.1 line 138, caught
  by a re-check); «drop» removes the whole item.
- The sentence splitter cuts at «Si... Entonces...»; verifiers checked whole sentences there.
- `tools/rewrap.py`: over-long lines re-wrapped to ~118 columns; Fuentes lists put in order of first citation. Neither
  changes sentence text, so records stay valid.

## Checks and suites (bloque II, final tree)

- `test_provenance.py`: 40 pass (all 28 written lessons and the glossary).
- Citations golden regenerated and read: 2,699 prose citations (560 of them a source file), 0 esquema rows, 119
  Normativa norms, 6 «naming a norm normativa.yaml lacks» (all six are «Otras fuentes» lines, C1's form).
  `lesson-refs.es.txt`: 9 references, 0 dangling. `glossary-links.es.txt`: 169 web marks, read.
- PDF draft test: failed once because the II.4 writer had changed the `#` title line (it dropped «La información
  administrativa.»); restored from the committed stub; passes.
- List-shape guard: passes.
- crypto-futures: unchanged. C1: only `m01-l11` (the authorised intro sentence). Android bundle re-exported to a scratch
  folder: byte-identical to `dist/bundle/`.
- Backend (`uv run pytest`): 1,658 passed, 23 skipped, 0 failed (run before the II.4 title restore, which no backend
  test reads; the provenance, manifest, glossary and citation tests were re-run after it: 147 passed).
- Frontend (`npx vitest run`): 715 passed, 81 skipped, 0 failed. `tsc -b` clean. `ruff`, `ruff format`, `mypy` clean on
  `scripts/provenance.py` and `tests/test_provenance.py`.

## Where to resume

Bloques I and II are complete (R2 done). Next: R2b (scope, coverage and currency audit), then R2c (esquemas).
