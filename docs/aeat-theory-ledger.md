# Theory ledger — aeat-agentes-hacienda

Round R2, common part (temas I.1–I.7 and II.1–II.5), 2026-11-11. Nothing committed. Requirements v1.1 (R2.3, section 4);
method: C2's R2 (`docs/age-c2-theory-ledger.md`), with C1's standing conventions (`docs/age-theory-ledger.md`).
Working files: `docs/age-verification/aeat/r2/`.

## How this round ran

- **Question packs** (`r2/tools/question_packs.py` → `r2/questions/<lesson>.md`): from R0a's classification and the
  parsed questionnaires. «coverage» = vigente or vigente-con-nota, OEP 2022–2025 with the 2022 extraordinario, first
  tema (137 questions over the 12 temas); «reference» = OEP 2020–2021, second tema or excluded.
- **Script derivation** (`r2/derivation.yaml` → `r2/tools/derive_draft.py`): each programme phrase mapped to C1/C2 lesson
  sections, C2 first (already at an exam depth like this one), C1 where C2 lacks the section; whole sections copied
  verbatim into the lesson, `PENDIENTE` blocks for the rest. A section is cut when the AEAT programme does not name it
  and no AEAT question (2020–2025) asked its facts (e.g. Agenda 2030, Administración en el exterior, RCP, OEP,
  retribuciones, responsabilidad del Gobierno, las partes del contencioso). Before any writing the drafts inherited
  2,558 sentences. Report: `r2/derivation.md`.
- **Writers** (2 × Sonnet, one run each: I.1–I.6; I.7 and II.1–II.5): intros, the five `new` sections (tipos de entes
  públicos, Ciudades Autónomas, funcionamiento electrónico del sector público, ordenamiento jurídico de la UE, derechos
  del interesado), gap sentences for pack questions, cross-reference fixes, «Lo que más cae», «Normativa». Notes:
  `r2/writer/<lesson>.md`. Spec: `r2/spec.md`.
- **Provenance** (`backend/scripts/provenance.py --course aeat-agentes-hacienda`, driver `r2/tools/prov.py`): a
  sentence inherits from C1 (searched first) or C2 when the text, governing citations and cited-file sha256 are
  identical; a C2 sentence that C2 itself inherited from C1 is recorded against C1. A C2 origin also needs its PASS in
  the C2 report the record names. Records: `r2/<lesson>.md` («verificado en C1», «verificado en C2» or «verificado:
  PASS»).
- **Verifiers** (Opus, blind, never the agent that proposed a fix): first pass 2 × 6 lessons; re-checks by other agents
  (`verify/<lesson>-recheck-N.md`). FAIL replacements applied by `r2/tools/apply_fails.py`.
- **Coverage** (2 × Opus): `r2/coverage/<lesson>.md`.

## Sources added

- `sources/normativa/`: LO 3/1980 (Consejo de Estado), Orden TDF/379/2024 and Resolución de 14-04-2026 (jornada y
  horarios), copied from C2 with the same sha256 so the copied sentences citing them inherit; LO 1/1995 and LO 2/1995
  (Estatutos de Ceuta y Melilla), new downloads (boe.es «Última actualización, publicada el 14/03/1995»; open data:
  not derogated). Five new `normativa.yaml` entries; header note.
- `sources/otros/`: 11 saved pages copied from C2, same sha256 (EU institution pages, OECD recommendation, Portal de
  la Transparencia, PAG portada, Cl@ve, INCIBE glossary), with `fuentes.yaml` (origen «copia de C2»; C2's comprobación
  carried over, no live re-check).
- RD 2271/2004 was not added: I.7's discapacidad section was cut to what art. 59 TREBEP says.
- `source-index.json` rebuilt (`scripts/index_sources.py --course aeat-agentes-hacienda`).

## Per tema

Words: `wc -w` of the lesson file. Sentences: provenance units (paragraph and list-item sentences, table rows, «Lo que
más cae» and «Normativa» lines). FAIL: rows failed in first pass + re-checks (each replaced and re-verified).

| Tema | Lesson | Words | Sentences | From C1 | From C2 | Verified here | FAIL (fixed) | Coverage | Glossary (origin) |
|---|---|---|---|---|---|---|---|---|---|
| I.1 | `m01-l01` | 5,843 | 290 | 271 | 8 | 11 | 1 | 9 / 9 | 18 |
| I.2 | `m01-l02` | 8,879 | 366 | 337 | 12 | 17 | 1 | 9 / 9 | 24 |
| I.3 | `m01-l03` | 7,635 | 327 | 229 | 4 | 94 | 5 | 13 / 13 | 21 |
| I.4 | `m01-l04` | 11,103 | 476 | 396 | 30 | 50 | 4 | 13 / 13 | 15 |
| I.5 | `m01-l05` | 9,880 | 345 | 253 | 23 | 69 | 3 | 10 / 10 | 22 |
| I.6 | `m01-l06` | 4,601 | 133 | 55 | 24 | 54 | 5 | 9 / 9 | 6 |
| I.7 | `m01-l07` | 18,865 | 618 | 540 | 29 | 49 | 5 | 10 / 10 | 27 |
| II.1 | `m02-l01` | 3,009 | 120 | 88 | 0 | 32 | 1 | 9 / 9 | 3 |
| II.2 | `m02-l02` | 3,788 | 135 | 116 | 3 | 16 | 3 | 14 / 14 | 6 |
| II.3 | `m02-l03` | 3,884 | 128 | 54 | 13 | 61 | 3 | 14 / 14 | 2 |
| II.4 | `m02-l04` | 2,336 | 79 | 41 | 13 | 25 | 0 | 15 / 15 | 0 |
| II.5 | `m02-l05` | 2,439 | 87 | 42 | 7 | 38 | 1 | 12 / 12 | 2 |
| **Total** | | **82,162** | **3,104** | **2,422** | **166** | **516** | **32** | **137 / 137** | **146 + 1 (m00-l01)** |

Inherited: 2,588 of 3,104 sentences (83 %). I.6 inherits least: this course's Ley 39/2006 is a newer consolidation
(2026-11-11, RDL 36/2026) than C2's, so every dependencia sentence was checked here. I.7 is the longest lesson: the
programme names seven areas of the personal tema, each kept at C2's depth.

### FAIL classes

- Clause dropped from the article (13): «quirúrgica» (48.a TREBEP), «Excepcionalmente» (39.3 LPAC), the second ground
  of inadmisión (126.1 LPAC), art. 84.2 LRJSP exceptions, art. 87.3 CE «prerrogativa de gracia», art. 155.1 CE second
  supuesto, art. 20.1.b LBRL small municipios, art. 10.2.c LPAC notice to the SGAD, art. 5.6 LPAC longer period, art.
  31.2.b LPAC scope, art. 5.1.c Ley 39/2006 current residence and the guarda rule, Grado II «necesidades de apoyo
  extenso», art. 30.1 LO 1/2004 functions.
- Wrong or overreaching cross-reference (4): II.1 treaties, II.2 lesividad and DEHú, I.7 incompatibilidades placed in
  the TREBEP.
- «Normativa» incomplete or overreaching (7): I.3 LRJSP range «1–3», I.5 art. 26 Ley 19/2013, I.7 (three rounds: Ley
  40/2015 and RDL 1/2013 lines, then the four and the two laws the copied prose names inside other norms' text — Ley
  22/1993, Ley 29/2011, Ley 7/1988, Ley 30/1992, Código Penal, Estatuto de los Trabajadores).
- Voice (1): a look-ahead closer in I.5, deleted. Intro scope (1): I.3 named CE título V without citing it. Other (6):
  I.1 refrendo of art. 64.1, I.4 Ceuta/Melilla arts. 21.2 and 25, I.3 avocación (10.2) and art. 104 LRJSP.
- Tooling (1, fixed): `apply_fails.py` pasted a verifier's «(delete the sentence…)» instruction into I.5 as text; it now
  drops on that wording too. The re-check caught it.

Coordinator ruling: a bare mention of the Constitución, with no content cited, needs no «Normativa» line (I.7).

## Coverage

137 of 137 coverage questions COVERED in their own lesson; no MISS, no COVERED-ELSEWHERE; no official key found wrong
against this course's snapshot. Not blocking, noted by the checkers:

- II.2 2023-71: the lesson gives art. 107.4 LPAC for the AGE only (the article adds «o de las Comunidades Autónomas»);
  art. 39.4 LPAC (basis of two distractors) is not stated.
- I.7 2024-68: the lesson gives four días hábiles for second-degree relatives but does not say a sister's spouse is
  second degree by affinity.
- I.4 2024-62 (seat of the Tribunal de Cuentas Europeo): only in a table row.
- R0a pack evidence cites the wrong apartado three times (2023-52 56.2, 2022-26 96.3, 2022X-30 125.2); the lessons cite
  the right one.
- Reference questions not covered: 2021-13 (Ley 37/2007, not in this course's norms), 2021-35 (art. 134.6 CE), 2020-4
  (annulled).

## Glossary

`glossary.yaml`: 147 entries (142 from C2, 5 from C1), all inherited (`r2/glossary.md`; `test_provenance.py` checks
term, definitions, citations and cited-file sha256 against the named course). Built by
`r2/tools/glossary_candidates.py --write`: a C2/C1 entry whose term an AEAT m01/m02 lesson uses, identical cited files,
kept when two lessons use it or the definition cites its article. Not copied (cited file differs here, or one lesson
only): `g-derecho-de-peticion`, `g-alto-cargo` (LO 4/2001 and Ley 3/2015 not in this course), `g-situacion-de-dependencia`,
`g-incapacidad-temporal`, `g-regimen-general-de-la-seguridad-social` (newer Ley 39/2006 / LGSS here), `g-agenda-2030`,
`g-plantilla`, `g-competencia-exclusiva`, `g-subvencion`. C2's `link_except` lists name C2 lessons and were dropped;
origins and `link_except` redone after reading `glossary-links.es.txt` (`r2/glossary-overrides.yaml`, applied by the
tool): oposición (sistema selectivo; origin m00-l01), directiva, convenio, interesado, información pública, servicios
comunes, moción de censura and cuestión de confianza (Alcalde), inviolabilidad parlamentaria.

## Summaries

`course.yaml`: modules `m01`, `m02` and the 12 lesson summaries, from the writers' proposals edited by the
coordinator. Blind check (`verify/summaries.md`): 7 PASS, 7 FAIL, replaced; re-check (`summaries-recheck-1.md`): 4 PASS,
3 FAIL (I.2 «Juzgados y Tribunales», I.3 Administración en el exterior and defensa del Estado, I.4 self-description),
replaced; re-check 2: 3 PASS. The II.3 replacement was tightened by the coordinator («salvo las excepciones del
artículo 24.1 de la LPAC»; the verifier's «una norma» was wider than the article) before the re-check.

## Programme phrases the R1 handoff listed without a mapping (common part)

- I.4 «Ciudades Autónomas»: Estatutos of Ceuta and Melilla added and snapshotted; new section in `m01-l04`.
- I.5 «participación en la rendición de cuentas»: C2's Gobierno Abierto principles (participación, rendición de
  cuentas) and art. 133 LPAC, copied.
- I.6 whole tema, I.7 «Régimen jurídico del personal»: norms already tagged; the lessons' «Normativa» lines pin the
  articles.
- II.1 «ordenamiento jurídico de la Unión Europea»: new section (arts. 1 TUE, 288–291 TFUE); TUE/TFUE notes in
  `normativa.yaml` name the articles.
- The tax-part phrases (III.1, III.2, III.6, III.20, the bare reglamentos) are for the tax rounds.

## Tool changes

- `provenance.py`: `--course aeat-agentes-hacienda` with `c1:`/`c2:` sources; «verificado en C2» records (C2 PASS
  required); glossary records name their origin course. Bug fixed: `_latest_verdicts` let the base report win over its
  re-checks («m01-l07.md» sorts after «m01-l07-recheck-4.md»), so an unchanged sentence re-checked PASS stayed FAIL;
  re-checks now win, highest number last. Tests written and run failing first:
  `test_a_sentence_inherited_from_c2_names_c2_and_needs_the_c2_pass`,
  `test_a_glossary_entry_inherits_from_the_course_its_record_names`, `test_a_recheck_pass_overrides_the_first_report_fail`,
  and the AEAT course audits (per lesson and glossary). C2's records were not re-run; C2's test still passes, but a
  C2 sentence left pending by the old ordering would only show on C2's next `plan`.
- `docs/age-verification/aeat/tools/close_round.sh`: C2's, with C2 added to the unchanged-courses check.

## Checks and suites

- `test_provenance.py` + `test_citations.py`: 128 passed (12 AEAT lessons and the glossary audited).
- Goldens regenerated and read: `citations.es.txt`, `lesson-refs.es.txt`, `glossary-links.es.txt` (AEAT only).
- List-shape: five «Normativa» lines ending «art. N.» read as list markers; four replaced by C2's verbatim lines
  (inherited), one glossed and verified (`m01-l07-recheck-5.md`).
- `close_round.sh`: crypto-futures, C1 and C2 unchanged; Android bundle byte-identical; backend 3,125 passed, 23
  skipped; frontend failed 1 (list-shape, fixed above) then 738 passed, 114 skipped; `tsc -b` clean. The list-shape fix
  touched only «Normativa» lines; provenance, citation, glossary, refs and the full frontend suite were rerun after it.
- `ruff check`, `ruff format`, `mypy` clean on `scripts/provenance.py` and `tests/test_provenance.py`.

## Open items

1. RDL 29/2026 convalidación deadline 19-11-2026; I.7's «Normativa» carries the RDL 31/2026 cambio pendiente on RDL
   4/2000 art. 19.1 (en vigor 01-12-2026).
2. Two dated copied sentences kept as C2 has them: «Estructura vigente a 16-10-2026» (I.3) and the Commission count «a
   fecha de 16-10-2026» (I.4). The elections of 29-11-2026 may change the ministry list.
3. Coverage notes above (107.4, 39.4 LPAC; affinity degree) are optional additions for R2b.
4. Esquemas: the copied C2 sections carry C2's esquema rows (inherited); AEAT's own esquemas are R2c.
5. Glossary entries skipped for a differing cited file could be verified here if wanted (derecho de petición, alto cargo).

## Handoff (R2 common part → tax temas)

1. Temas I.1–I.7 and II.1–II.5 are written; every sentence has a provenance record, and `test_provenance.py` audits them.
2. Inherited 2,588 sentences (2,422 from C1, 166 from C2) and verified 516 blind, with 32 FAILs, all fixed and re-checked.
3. Coverage is 137 of 137.
4. The glossary has 147 entries, all inherited.
5. Course summaries for `m01`, `m02` and the 12 lessons are blind-checked.
6. Derivation is reproducible. Running `derive_draft.py` again would overwrite the written lessons, so don't do it.
   `derivation.yaml` documents what came from where.
7. New sources: two Statutes downloaded; three norms and 11 pages copied from C2, same sha256.
8. Tool fixes: `provenance.py` now takes an AEAT target and C2 origins, and re-check ordering is fixed. `apply_fails.py`
   drops on a «delete» instruction.
9. Suites: backend 3,125 passed; frontend 738 passed; `tsc -b` clean; Android bundle byte-identical.
10. C1, C2 and crypto-futures are unchanged.
11. Nothing is committed.
12. The tax temas (m03, 20 lessons) are written new (R4.3). No derivation applies: C1/C2 have no tax lessons.
13. For the tax temas, use the same spec shape with `r2/tools/question_packs.py III.n` (packs per tema), writers by
    groups of temas and blind verifiers.
14. Tax-specific rules (R4.4): every amount and plazo comes verbatim with its article. Worked examples only apply the
    norm step by step, with fictional taxpayers and every date stated. Annual figures name their year and norm
    (`cifras_anuales`).
15. Open from R1 for the tax part: III.1, III.2, III.6 and III.20 have no pinned mapping, and the reglamentos are listed
    bare.
16. The CAU XHTML files index 0 units, so III.20 citations cannot link until `index_sources.py` reads Cellar XHTML.
17. RDL 29/2026's convalidación decides LIRPF, LIVA, RIRPF and TRLRHL wording for III.15, III.16, III.18 and III.19.
    Its revert list is `r1/rdl-29-2026-revert-list.md`.
18. The heaviest part III temas by questions are III.4, III.12, III.15, III.8, III.5, III.13 and III.19.
19. Before verifying the tax temas, check that `verify/` file names keep re-checks sorting after their base report;
    the fixed `_latest_verdicts` handles «-recheck-N».
20. The writer spec's «Normativa» rule is enforced strictly by the verifiers: list every norm the prose names, including
    those named inside another norm's text. Tell writers up front.
21. Records are written only after every pending sentence has a PASS. Run `prov.py plan` first, then `prov.py record`.
22. Remove `r2/pending/` at close; it is a working folder.

## Where to resume

Tax part in progress: see «Tax part — where to resume» at the end of this file.

R2, common part: done. Next: R2 tax temas (III.1–III.20) in groups, then R2b (scope, coverage, currency), R2c
(esquemas), M (platform: published course without exercises), P (publication). Before the tax temas: the RDL 29/2026
convalidación outcome (19-11-2026) and the CAU XHTML indexer.

---

# Tax part (R2, III.1–III.20, `m03-l01` … `m03-l20`)

Started 2026-11-11. Plan: `docs/aeat-tax-plan.md` (groups G1–G10, per-tema norms, questions asked, depth). Spec:
`docs/age-verification/aeat/r2-tax/spec.md`. Working files and reports: `docs/age-verification/aeat/r2-tax/<lesson>/`
(`writer.md`, `pending.md`, `verify.md`, `verify-recheck-N.md`, `coverage.md`). Facts asked per tema:
`r2-tax/asked-digest.md`. Packs: `r2/questions/m03-lNN.md` (315 coverage questions).

## Tax part — how it runs

- Writers (Sonnet), one run per group, temas in sequence; blind verifiers (Opus), batches of 60; re-checks by a
  different verifier; coverage (Opus) after each group; at most four agents at once.
- `r2-tax/tools/taxprov.py plan|record|apply`: provenance for the tax lessons with the functions of
  `backend/scripts/provenance.py`. Every C1 and C2 lesson is a candidate origin (no derivation map); verdicts come from
  `r2-tax/<lesson>/verify*.md`, re-checks winning in number order; records go to `r2/<lesson>.md`, where
  `test_provenance.py` reads them.
- `r2-tax/tools/cites.py <lesson>`: the lesson's prose citations the parser leaves unresolved.

## Tax part — per tema

Words: `wc -w`. Sentences: provenance units of the record. FAIL: rows failed in first pass and re-checks, each fixed and
re-verified by a different verifier (no sentence needed dropping). Coverage: coverage questions with their fact in the
lesson after the misses were fixed. Examples: `### Ejemplo` sections, every step recomputed by the verifier.

| Tema | Lesson | Words | Sentences | Inherited | Verified here | FAIL (fixed) | Coverage | Glossary | Examples |
|---|---|---|---|---|---|---|---|---|---|
| III.1 | `m03-l01` | 3,595 | 151 | 8 | 143 | 8 | 9 / 9 | 3 | 0 |
| III.2 | `m03-l02` | 3,275 | 140 | 0 | 140 | 3 | 9 / 9 | 0 | 0 |
| III.3 | `m03-l03` | 4,512 | 165 | 0 | 165 | 1 | 13 / 13 | 7 | 2 |
| III.4 | `m03-l04` | 11,689 | 371 | 0 | 371 | 10 | 32 / 32 | 7 | 1 |
| III.5 | `m03-l05` | 9,796 | 304 | 0 | 304 | 15 | 21 / 21 | 3 | 2 |
| III.6 | `m03-l06` | 4,394 | 136 | 0 | 136 | 5 | 8 / 8 | 3 | 0 |
| III.7 | `m03-l07` | 6,762 | 256 | 0 | 256 | 5 | 15 / 15 | 0 | 2 |
| III.8 | `m03-l08` | 8,278 | 291 | 0 | 291 | 6 | 22 / 22 | 1 | 1 |
| III.9 | `m03-l09` | 5,261 | 178 | 0 | 178 | 6 | 15 / 15 | 1 | 2 |
| III.10 | `m03-l10` | 3,593 | 108 | 0 | 108 | 4 | 10 / 10 | 2 | 0 |
| III.11 | `m03-l11` | 4,858 | 155 | 0 | 155 | 6 | 11 / 11 | 4 | 1 |
| III.12 | `m03-l12` | 9,534 | 286 | 0 | 286 | 8 | 24 / 24 | 1 | 1 |
| III.13 | `m03-l13` | 9,150 | 273 | 0 | 273 | 8 | 20 / 20 | 3 | 1 |
| III.14 | `m03-l14` | 7,476 | 237 | 0 | 237 | 6 | 18 / 18 | 0 | 1 |
| III.15 | `m03-l15` | 8,070 | 253 | 0 | 253 | 16 | 22 / 22 | 2 | 1 |
| III.16 | `m03-l16` | 6,437 | 210 | 0 | 210 | 9 | 14 / 14 | 1 | 3 |
| III.17 | `m03-l17` | 8,221 | 230 | 0 | 230 | 15 | 8 / 8 | 0 | 0 |
| III.18 | `m03-l18` | 6,063 | 166 | 0 | 166 | 7 | 15 / 15 | 2 | 0 |
| III.19 | `m03-l19` | 9,101 | 270 | 0 | 270 | 11 | 18 / 18 | 1 | 2 |
| III.20 | `m03-l20` | 5,046 | 130 | 0 | 130 | 4 | 11 / 11 | 5 | 0 |
| **Total** | | **135,111** | **4,310** | **8** | **4,302** | **153** | **315 / 315** | **46** | **20** |

## Tax part — decisions taken without asking

1. Reports live in `r2-tax/<lesson id>/` (lesson ids, as the packs and records are named), not one folder per tema
   code.
2. `provenance.py` reads verdicts only from `r2/verify/`; instead of changing it, the round tool `taxprov.py` reuses its
   functions and reads `r2-tax/`. The record format and place are unchanged, so `test_provenance.py` audits the tax
   lessons as it does the common ones.
3. Ten groups instead of the brief's list: «Especiales» has no tema in the 2025 programme (dropped; Ley 38/1992 enters
   only for III.1, art. 1); «customs and the rest» is III.20 alone; Sociedades is its own group.
4. New norms for facts official questions asked (2022X-29 TRLITPAJD, 2023-87 Ley 38/2022, 2022X-45 Código de Comercio,
   RD 1676/2009, Orden EHA/586/2011) and the art. 1 of each state tax for III.1 «impuestos de titularidad estatal y sus
   características» (IP, ISD, IIEE, IRNR). The `normativa.yaml` header listed Ley 38/1992, TRLIRNR and Ley 38/2022 as not
   entering; they enter for III.1 only.

5. III.4 prescripción example: art. 67.1 LGT does not say whether a plazo counted in years ends on the anniversary or
   on the day before, so the example gives the dies a quo and the interrupción but no exact last day (no norm in the
   snapshot fixes it; the course does not choose).
6. Official-key notes found by the III.4 writer, for the exams ledger (stage 2): 2024-43, where the key counts art. 66
   bis.2's ten years from the end of the período impositivo and the article counts them from the end of the plazo
   reglamentario de presentación (candidate «Clave oficial discutida»). The R0a evidence cites RGAT 3.3 for 2021-54 (the
   text is 3.2.a)) and 20.3 for 2024-49 (it is 20.2). The III.2 writer found the same for 2022-34 and 2023-56 (the
   Director General's rank is in art. 103.Tres.1 and the jefatura in Tres.3). The lessons cite the right paragraphs.
7. III.8: LGT art. 159 (conflicto en la aplicación de la norma) is left out: the programme does not name it and no
   coverage question asked it. Concierto and Convenio, named inside art. 150.3 LGT, are listed in «Normativa» «sin
   precepto citado» (the common part's strict rule).
8. Glossary: terms whose defining article belongs to another tema have their origin in that tema (declaración,
   autoliquidación and comunicación de datos → III.6, not III.7). Too-generic terms («comunicaciones») are not
   proposed. Course summaries state facts without citations, as the common part's do.
9. Pack errors found by the III.8 writer: the 15-day ratification of medidas cautelares is in art. 146.3, not 146.2,
   and the informe razonado is in 158.1, not 158.3. In 2022X-53, option d says 30 days and art. 150.4 says 60.
   Unsourced reference facts left out: 2022-55 (internal AEAT instruction) and 2020-59 (RGAT 57.1).
10. III.3 coverage miss 2024-66 (precios públicos): Ley 8/1989 (BOE-A-1989-8508, consolidated 2017-11-09) downloaded and
    entered; art. 24 added to III.3, re-checked by a different verifier.
11. III.7 example (interest on an IRPF refund): the verifier passed a six-month count «julio a diciembre»; a strict
    date-to-date count ends on 30-12 with the same result. Kept, noted in the report.
12. Official keys judged doubtful by the coverage checkers (for the exams ledger, stage 2): 2022X-69 (key A; the
    snapshot gives C: arts. 161.2 and 65.5 LGT, art. 46.1.a) RGR), 2025-20 (art. 104.1 LGT, already noted in the ledger),
    2024-43 (art. 66 bis.2 LGT). The lessons state the norm, never the disputed key.
13. III.12 coverage miss 2024-26: art. 595.1 LEC (tercería de dominio, adquisición después de trabado el embargo)
    added in the LEC's own words («ejecutado», not «obligado al pago»); the LEC «Normativa» line gains 595.1.
14. III.13: the plan's «art. 209 plazo de tres meses» was wrong; art. 209.2 LGT gives six months, and the writer
    followed the article. Glossary terms that are labels rather than the norm's terms («regularización voluntaria
    (orden sancionador)») and definitions that are not definitions (medidas cautelares, anotación preventiva,
    diligencia de embargo) were not staged.
15. `g-sustituto-del-contribuyente` keeps its id. Its term is «sustituto», the word art. 36.3 LGT defines, because the
    platform rejects a term the prose never uses («sustituto del contribuyente» appears only in the plural).
16. «Normativa» lines start with the `short` name exactly: «Ley 39/2015 (LPAC)», not «LPAC (Ley 39/2015)» (III.9,
    III.11 corrected and re-checked).
17. RDL 29/2026 in III.15–III.16: arts. 24 and 85.1 stay in the text in force with «desde 01-01-2027» only (the 2027
    scale is not written: «nothing else»); art. 85 named in III.16 without the mark (the change is III.15's).
    2022X-88 (art. 57.2 LIRPF) flagged by the writer as a doubtful key. III.20 follows the consolidated CAU («efectúe
    actividades», art. 5.5), not the original wording quoted in 2022-98. No CAU reglamento (2015/2446, 2015/2447) is cited:
    the CAU states every fact asked, so nothing from III.20 goes to section M.
18. Parser (for section M): «art. 31.1.3.ª b) a´)» is not read; the lesson cites «art. 31.1.3.ª.b)». A «disposición
    adicional» needs the numeric form («disposición adicional 55.ª») in III.15.
19. III.17: norms the LIS names by title and that normativa.yaml lacks (Ley 9/2012, Ley 49/2002, Ley 27/1984, LO 8/2007,
    Ley 34/1998, Ley 19/1994) are listed in «Normativa» «nombrada en el art. N LIS», as Ley 25/2003 in III.5. The LIS
    rates for 2026 come from its DT 44.ª (19 %/21 %, art. 101 entities 23 %) and are stated with it.
20. `taxprov.py apply` pasted a verifier's «— add after it: «…»» instruction into III.17's «Normativa»; the
    block was repaired by hand and re-checked. `apply` now refuses a replacement that holds an instruction («add after», «replace the»), and verifiers are told to put only the replacement text in that column.
21. III.13 coverage miss 2022-46 (art. 27.2 LGT): the fact is III.3's, and III.13 now states it once, cited.
22. Art. 85.1 LIRPF in III.15: the first writer put «desde 01-01-2027» on the 2026 rule. The re-checker read art.
    6.tercero RDL 29/2026: the 2026 rule is the «Redacción anterior». So the 2026 sentences cite a plain «(art. 85.1
    LIRPF)», and one sentence says a new wording applies from 01-01-2027 (RDL 29/2026, convalidación pendiente). The
    2027 scale is not written.
23. III.15 coverage miss 2022-80: art. 7.a) LIRPF (terrorism benefits) added to the exempt list. III.16 had a repeated
    «Cambio pendiente» sentence; the duplicate was removed.
24. More official keys judged doubtful (stage 2, exams ledger): 2025-24 (art. 80.Cuatro LIVA: options a) and c) both
    hold), 2023-80 (art. 99.Tres LIVA: the four years run from the nacimiento del derecho, not «se soportó»),
    2022X-88 (art. 57.2 LIRPF: over 75 adds 1.150 + 1.400 euros). 2022X-93 holds: 500.000 pesetas = 3.005,06 euros;
    the lesson keeps the snapshot's pesetas.
25. Glossary definitions keep the article's exclusions («no tendrán la consideración de…»), as the extras checks ruled.
26. Platform nondeterminism (for section M): the citations golden flips run to run on the common part's parentheticals
    citing two norms with the same unit («art. 1 LO 1/1995 y art. 1 LO 2/1995», 19 in `m01-l04`, committed in R2
    common part): the anchor goes to Ceuta or Melilla at random. Not patched (platform); not worked around in content
    (19 inherited sentences would lose their verification). `test_citations.py` frozen-golden test fails about half
    the runs.

## Programme phrases the R1 handoff listed without a mapping (tax part)

- III.1 «impuestos de titularidad estatal y sus características»: art. 1 of each state tax law (LIRPF, LIS, LIVA,
  TRLIRNR, Ley 19/1991, Ley 29/1987, TRLITPAJD, Ley 38/1992) and art. 3 Ley 38/2022, downloaded this round; Haciendas
  autonómica y local: CE arts. 156–157, LOFCA, Ley 22/2009 art. 25, TRLRHL arts. 59–60, Concierto and Convenio art. 1.
- III.2: art. 103 Ley 31/1990, Orden de 2 de junio de 1994 (apartados primero–decimotercero), Orden PRE/3581/2007,
  Resoluciones de 13-01-2021; the lesson's «Normativa» pins the apartados.
- III.6 «pagos a cuenta»: LGT art. 23, LIRPF arts. 99–101, RIRPF arts. 75–76 and 108–112, LIS art. 40, Orden
  EHA/586/2011.
- III.20 «Inclusión… disposiciones generales»: CAU arts. 158–163 suffice; the Reglamentos 2015/2446 and 2015/2447 are
  not cited, so no citation waits on the XHTML indexer.
- Reglamentos: each lesson's «Normativa» lists the RGAT, RGR, RIRPF, RIS, RIVA, RGRST and RGRVA articles it cites.

## Tax part — sources added

Downloaded from boe.es on 2026-11-11, entered in `normativa.yaml` (origen «descarga nueva»; no pending changes; RDLs
29, 31, 33, 35 and 36/2026 read and none touches them), `source-index.json` rebuilt:

- III.1: Ley 19/1991 (BOE-A-1991-14392, 2023-12-28), Ley 29/1987 (BOE-A-1987-28141, 2022-12-28), TRLITPAJD
  (BOE-A-1993-25359, 2026-03-21), Ley 38/1992 (BOE-A-1992-28741, 2026-09-30), TRLIRNR (BOE-A-2004-4527, 2023-05-25),
  Ley 38/2022 (BOE-A-2022-22684, 2024-12-21).
- III.4: Código de Comercio (BOE-A-1885-6627, 2023-05-09); RD 1676/2009 (BOE-A-2009-19438, 2017-12-30).
- III.6: Orden EHA/586/2011 (BOE-A-2011-4948, never amended).
- **Models orders** (R0a handoff: «RIRPF art. 67 and RGAT art. 49 depend on an order approving the models (RD
  117/2024)»). It is more than one order:
  - RIRPF art. 67.4 → Orden HAC/1398/2003 (BOE-A-2003-11044, 2025-01-31; presentación telemática por entidades con
    acuerdos).
  - RIRPF art. 67 bis (the article RD 117/2024 modified) → the yearly order of the IRPF and Patrimonio models. In force:
    Orden HAC/277/2026 (BOE-A-2026-7041, exercise 2025). This is an annual figure, and the 2026 campaign's order will
    replace it.
  - RGAT art. 49 → Orden HAC/342/2021 (BOE-A-2021-5780, models 234–236, 2024-03-22).
  - RGAT art. 49 ter (enters into force with its order, DF 11.ª d) RD 117/2024) → Orden HAC/266/2024 (BOE-A-2024-5722,
    model 239). It is not consolidated on boe.es, so the diario PDF is stored.
  - **Not obtained:** the order of model 238 (DAC7, RGAT art. 54 ter). The boe.es consolidated search found nothing.
    No lesson states a fact resting on it.

## Tax part — checks and suites

- Final `close_round.sh` (after the last publish): C1, C2 and crypto-futures unchanged; Android bundle byte-identical;
  backend 3,145 passed, 23 skipped; frontend 738 passed, 114 skipped; `tsc -b` clean. The run before it failed only
  the frozen citations golden (decision 26, intermittent; it passed on this run).
- Goldens regenerated and read: `citations.es.txt` (4,504 prose citations, 192 Normativa norms, 18 naming a norm
  normativa.yaml lacks, all «nombrado en» lines), `glossary-links.es.txt` (46 new terms; the stubs' RDL lines gone).
- `test_provenance.py`: every m01–m03 lesson and the glossary (193 entries: 147 inherited, 46 verified) audited.

## Tax part — where to resume

R2 tax part: done (all 20 temas written, verified, recorded, covered; glossary and summaries published). Open for
later rounds: section M (decision 26, parser items of decision 18), the RDL 29/2026 convalidación (19-11-2026; revert
list), the doubtful official keys for stage 2 (decisions 6, 12, 24), R2b, R2c.

## Handoff (R2 tax part → R2b / R2c / M)

1. Temas III.1–III.20 (`m03-l01` … `m03-l20`) are written, 135,111 words, structured by the governing norm.
2. 4,310 sentences: 8 inherited from C1, 4,302 verified blind (Opus); 153 FAILs, all fixed and re-checked by a
   different verifier; no sentence dropped.
3. Coverage: 315 / 315 vigente first-exercise questions of OEP 2022–2025 have their fact in their lesson (5 misses found
   and fixed: 2022-33, 2024-66, 2024-26, 2022-46, 2022-80).
4. 20 worked examples (art. 27 and 28 recargos, art. 62 plazos, prescripción, plazos de resolución and notificación,
   inspection period, sanctions and reductions, recursos, IRPF, prorrata, bienes de inversión), each step recomputed.
5. Glossary: 46 new verified entries (193 total); course.yaml: module m03 and all 20 lesson summaries, blind-checked.
6. Records in `aeat/r2/m03-lNN.md`; reports in `aeat/r2-tax/<lesson>/`; `test_provenance.py` audits all of them.
7. New sources (boe.es): 9 tax laws/orders for facts asked + Ley 8/1989 + the models orders (HAC/1398/2003,
   HAC/277/2026, HAC/342/2021, HAC/266/2024). Not obtained: the model 238 order (no fact rests on it).
8. Annual figures carry year and norm (Ley 31/2022 prorrogada, Orden HFP/311/2023, módulos orders, LIS DT 44.ª).
9. RDL 29/2026: marks only on precepts it changed (checked against its text); convalidación deadline 19-11-2026;
   revert list `r1/rdl-29-2026-revert-list.md` now also concerns III.15–III.16 sentences.
10. 26 decisions taken without asking are logged above, with reasons.
11. Doubtful official keys for stage 2: 2024-43, 2022X-69, 2025-20, 2025-24, 2023-80, 2022X-88.
12. Pack evidence cites wrong apartados in about a dozen questions; the lessons cite the snapshot.
13. Section M: the citations golden flips on two-norm parentheticals of `m01-l04` (decision 26); the parser misses
    «art. 31.1.3.ª b) a´)», LIVA apartados from «Trece» and letters after «18.º » with a space.
14. The CAU reglamentos 2015/2446 and 2015/2447 are not cited: the CAU states every fact asked; nothing waits on the
    XHTML indexer.
15. Norms named only inside other norms' text are listed «nombrado en…» in «Normativa» (12 not in normativa.yaml).
16. Round tools: `r2-tax/tools/taxprov.py`, `cites.py`, `publish.py`; provenance.py and the platform untouched.
17. Final close_round: C1, C2, crypto-futures unchanged; Android byte-identical; backend 3,145 passed; frontend 738
    passed; tsc clean. Goldens regenerated and read.
18. Nothing is committed.
19. Next: R2b (scope, coverage, currency for the whole course), R2c (esquemas, incl. R4.5 tax esquemas), M, P.

---

# R2b (scope, coverage, currency) and R2c (esquemas)

Started 2026-11-11. Working files: `docs/age-verification/aeat/r2b/` (`scope/`, `currency/`, `tools/`, `verify/`),
`docs/age-verification/aeat/r2c/` (spec, writer notes). Audit document: `docs/aeat-scope-audit.md`.

## R2b / R2c — where to resume

(Updated as the round goes; the last entry wins.)

- 2026-11-11, first pass: scope auditors A (m00, I.1–I.4), B (I.5–II.5), C (III.1–III.10) done, D (III.11–III.20)
  running. Cuts and notes of A, B, C applied; III.11–III.20 pending D. Currency done (`r2b/currency/normativa.md`,
  `pages.md`; 13 norms entered; RDL 29/2026 not due). Common-part esquemas trimmed to four per lesson. Tax esquema
  writers running (R2c spec). Next: D's cuts, one blind batch for every R2b edit, esquema verification, records, close.
- 2026-11-11, second pass: all four scope reports in; every cut and note applied (A–D), plus the m02-l02 (107.4, 39.4)
  and m02-l04 (80.2, 95.1) prose fixes. Tax esquemas written (writer notes in `r2c/`), common esquemas trimmed, m02-l04
  given one. Coverage re-checked after the cuts: holds. `docs/aeat-scope-audit.md` drafted. Running: two blind Opus
  verifiers over every pending item (spec `r2b/verify/spec.md`; reports `r2/verify/r2bc.md`,
  `r2-tax/<lesson>/verify-r2bc.md`). Next: apply FAILs, re-check by a different verifier, records, goldens, close.

## R2b / R2c — decisions taken without asking

1. Scope evidence is AEAT questions only. A note naming an Administrativo or Auxiliar exam (m02-l01 «El procedimiento
   de elaboración», inherited from C2) was re-audited: the section maps to II.1 «El Reglamento» (arts. 25–26 Ley 50/1997),
   so the note was removed rather than re-pointed.
2. Four auditors instead of three (the course has 958 sections); two at a time, as the concurrency rule allows.
3. The Consejo Europeo is not «El Consejo» of I.4: its subsections no AEAT question needs were cut, «Composición» kept
   under a note (2025-50). Wrong options alone (2022-8, 2021-10, 2025-79, 2020-34) are not evidence.
4. III.5 consultas tributarias (arts. 88–89 LGT) cut: the 2025 programme dropped «la consulta tributaria» and the only
   questions are `fuera de temario`. The auditor flagged it as a judgement call (art. 85.2.c names consultas as an
   información instrument); the deliberate deletion from the programme decided it.
5. III.11: the list of motivos de oposición (art. 167.3 LGT) cut at sentence level, though its section stays mapped;
   the programme keeps «concepto y plazos» and the ledger rules 2022X-70 out for that reason.
6. Container notes: one «Fuera del enunciado…» note on a `##` covers its `###` (III.13 «Infracciones y sanciones en
   particular», III.20 «Regímenes de tránsito y de depósito»), as C2 did.
7. Optional additions of the common-part handoff, by the same rule: art. 107.4 LPAC completed and art. 39.4 LPAC
   added (asked; mapped to II.2 «eficacia»); the degree of affinity (2024-68) not written: no norm in the snapshots
   states it.
8. The 13 norms named inside other norms: the handoff said 12; the golden listed 13 (Ley 30/1992, derogated, included
   so every name has a snapshot). `short` set to the exact «Normativa» wording so lines resolve; m03-l05's Ley 25/2003
   line rewritten to start with the new short (tax decision 16) and re-checked.
9. RGPD: the copied `version_vigente` note named corrigenda files this course did not hold; the two PDFs were copied
   from C1 (same sha256) rather than editing the note, because m01-l05's art. 9.1 sentence follows the corrected text.
10. consilium-presidencia.html: 403 in plain and browser fetch; the site's bot check is not worked around. Recorded as
    not read (as C2's R2b did); the sentence resting on it is inherited from C2.
11. «Cambio pendiente … sin convalidar, con efectos desde el <past date>» in the «Normativa» of III.15–III.16 is not a
    stale «(desde …)» mark: the pending element is the convalidación (RDL 29/2026, deadline 19-11-2026, not reached).
12. Common-part esquemas: the derivation had copied every C2/C1 esquema of the merged lessons (I.2: 6, I.3: 5, I.4: 8,
    I.7: 9). Trimmed to four per lesson, keeping the subjects the AEAT questions ask most (organs, majorities, plazos;
    counts in this round's notes); kept rows unchanged and inherited. No common esquema was re-derived from C1/C2 beyond
    m02-l04, where no C1/C2 esquema could be copied byte-identical and a new one was written and checked.
13. Esquema rows failed «drop» because the prose lacks the same rule: the prose is fixed first (brief), by a writer
    other than the esquema writers, and both prose and row go to a re-check by a verifier who saw neither report.
14. Two inherited m02-l04 sentences (arts. 80.2 and 95.1 LPAC) were shortened past the article in C1/C2's wording; fixed
    here (they lose inheritance and are verified here). C1 and C2 are not touched; the same wording there is listed for
    their next round.
- 2026-11-11, third pass: first blind pass done (38 FAIL: replacements applied; ten «drop» rows fixed through the prose
  by a separate writer, `r2c/prose-gaps.md`); re-check 1 done (11 FAIL; replacements applied; LIS DA 14.ª (III.6), LIVA
  99.Tres/99.Cinco (III.19) and DA 15.ª on art. 11.12 LIS (III.17) sent to the prose-gap writer). Records written for
  every lesson except m03-l03, l06, l15, l17, l19. Next: re-check 2 by a fourth verifier on those five, records, close.
15. Two failed re-checks → drop, counted per item lineage: the m03-l03 «Presentación … 12 meses» row (failed in pass 1,
    re-check 3 and re-check 4) was dropped; the esquema, left with the art. 27.5 row alone, was removed (the prose keeps
    every rule of art. 27; m03-l03 keeps two esquemas). The m03-l17 «Lo que más cae» line on bases negativas (failed
    re-checks 1 and 2) was dropped and replaced by a narrower line naming the limits without figures (PASS), so the block
    keeps ten lines.
16. LIS DA 14.ª and 15.ª: found by the esquema verifiers as prose gaps (the lessons gave the five-sevenths percentage and
    the 70 % limits as general). Fixed in the prose in the DA's words; they are not RDL marks (in force since 2024).
17. The 5 citations the golden still counts as «naming a norm normativa.yaml lacks» are parser cases (worded DT
    numeral, «89.Uno y Tres»), not missing norms: section M, with the tax part's decision 18.

## R2b / R2c — results

- **Scope** (four blind Opus auditors, `r2b/scope/`): 958 sections; 902 mapped, 11 instrumental, 3 other tema, 29 kept
  by AEAT exam evidence (21 notes; container notes cover their `###`), 13 removed (5 in part I, 8 in part III) plus the
  art. 167.3 list; no gaps. Facts missing and written: arts. 107.4 and 39.4 LPAC. Wrong note removed: m02-l01. Detail and
  tables: `docs/aeat-scope-audit.md`.
- **Coverage:** 137 / 137 and 315 / 315 hold after the cuts.
- **Currency** (`r2b/currency/`): norms and EU texts current; 13 norms entered (11 downloads, 2 C1 copies); RGPD corrigenda
  copied from C1; annual figures re-found in their norms for 2026; RDL 29/2026 pending (19-11-2026); no past «desde».
- **R2c esquemas** (spec `r2c/spec.md`; writers' notes `r2c/writer-*.md`, prose fixes `r2c/prose-gaps.md`):

| Part | Lessons | Esquemas | Rows | Inherited | Verified here |
|---|---|---|---|---|---|
| I–II (common) | 12 | 33 | 218 | 204 | 14 (m02-l04, new) |
| III (tax) | 20 | 48 | 287 | 0 | 287 |
| **Total** | **32** | **81** | **505** | **204** | **301** |

  Rows count table rows (headers included) and list items. Common part: four lessons trimmed to four esquemas (I.2, I.3,
  I.4, I.7; 12 esquemas removed); the kept rows are byte-identical to C2/C1 (provenance «verificado en C1/C2»). Tax part,
  per R4.5: plazos de pago (III.9; III.11 states the providencia plazos and the art. 28 recargos as a table of its own),
  the art. 27 recargos (prose only after the drop above), infracciones, sanciones and reducciones (III.13), gestión,
  inspección and recaudación plazos and effects (III.5, III.7, III.8, III.11, III.12), recursos and reclamaciones (III.14),
  órganos of the AEAT (III.2, two `arbol`), structure of IRPF, IS, IVA and the deuda aduanera (III.15–III.20). All but one
  are `tabla` (one `plazos` in III.5): the norms rarely state an order. Verification passes: 1st 38 FAIL; re-checks 11, 3,
  2, 1; each by a verifier who had not seen the earlier reports.
- **Records:** every m01–m03 lesson re-recorded (`aeat/r2/<lesson>.md`); `test_provenance.py` passes.

## Open items after R2b / R2c

1. RDL 29/2026: re-check the BOE from 18-11-2026; if derogated or lapsed, apply `r1/rdl-29-2026-revert-list.md` (III.1,
   III.15, III.16, III.18) with blind checks. RDL 31/2026 (about 04-12-2026), RDL 33, 35, 36/2026 likewise.
2. `consilium-presidencia.html` not read live (403); one inherited m01-l04 sentence rests on it.
3. Section M (platform, not patched): the Ceuta/Melilla two-norm golden flip; the parser cases of tax decision 18 and
   decision 17 above.
4. C1 m03-l03 and C2 m01-l11 carry the same shortened arts. 80.2 and 95.1 LPAC sentences fixed here in m02-l04: for their
   next round (with the C2 provenance rerun).
5. Stage 2: the ledger's inconsistent retenciones classification (2021-59, 2021-61, 2022-89 vs 2023-64 onwards); the
   doubtful keys of the tax part.
6. Noted by the auditors, not acted on (no coverage question): `docs/aeat-scope-audit.md`, «Noted, not acted on».

## Handoff (R2b / R2c → M / P)

1. R2b and R2c are done for all three parts; nothing is committed.
2. Scope: 958 sections audited by four blind auditors against the 2025 programme and the 680 AEAT questions.
3. 13 sections removed (I.3 Comisión General; four Consejo Europeo subsections; III.5 consultas and prueba arts.
   106–108; III.13 arts. 195–197; III.20 arts. 162–163) and the art. 167.3 list.
4. 29 sections kept on AEAT exam evidence, each under a «Fuera del enunciado literal…» note (21 notes).
5. The m02-l01 note citing an Auxiliar exam was wrong and is gone.
6. Facts added: arts. 107.4 and 39.4 LPAC (II.2); the affinity degree (2024-68) not written: no norm states it.
7. Coverage 137/137 and 315/315 hold after the cuts.
8. Currency: all norms current on boe.es and Cellar; 11 saved pages checked (1 changed, nothing rests on it; 1 403).
9. 13 norms named inside other norms entered with snapshots; the Normativa lines now resolve.
10. Annual figures re-found in their norms for 2026; no PGE 2026; status «no contrastado con la sede» unchanged.
11. RDL 29/2026 not convalidated or derogated; deadline 19-11-2026; revert list not applied.
12. Esquemas: 81 in 32 lessons (33 common, 48 tax), 505 rows: 204 inherited, 301 verified blind.
13. Common lessons trimmed to four esquemas each; m02-l04 has a new one.
14. The esquema check found 16 prose gaps (incl. LIS DA 14.ª and DA 15.ª for grandes empresas); all fixed and checked.
15. FAIL handling: replacement in the article's words, re-check by a different verifier; two items dropped after two
    failed re-checks.
16. Opus runs: 4 scope auditors, 2 first-pass verifiers, 4 re-checkers; writers on Sonnet; at most four agents at once.
17. Records redone for every lesson; `test_provenance.py`, `test_citations.py`, `test_esquema.py` pass.
18. Goldens regenerated and read (citations, glossary links; lesson refs unchanged).
19. Close: C1, C2, crypto-futures unchanged; Android byte-identical; frontend 738 passed; `tsc -b` clean.
20. Backend 3,144 passed; the only failure was the known Ceuta/Melilla golden flip; rerun once: passed (recorded).
21. Audit document: `docs/aeat-scope-audit.md` (Run 1), verdict «dentro de alcance, cubierto y al día» per part.
22. Reports: `aeat/r2b/` (scope, currency, verify spec), `aeat/r2c/`, `aeat/r2/verify/r2bc*`,
    `aeat/r2-tax/<lesson>/verify-r2bc*`.
23. Round tools: `r2b/tools/check_norms.py`, `eu_versions.py` (lint and mypy clean); taxprov/prov reused.
24. Working folders `r2/pending/` and `r2-tax/*/pending.md` removed.
25. 17 decisions taken without asking are logged above.
26. Open: RDL 29/2026 re-check from 18-11; the 403 page; section M items; C1/C2 80.2/95.1 wording.
27. Next: M (published course without exercises, R5.1), then P (publication).
28. Before P: re-run `check_pages.py` and the norm check if more than a month has passed.
29. Before stage 2: the doubtful keys and the retenciones classification.
30. Nothing in C1, C2 or crypto-futures was changed by this round.

## R2b / R2c — where to resume (final)

R2b and R2c are done (2026-11-11), closed with `close_round.sh`. Next: M, then P. Watch RDL 29/2026 from 18-11-2026.

---

# P — publication (stage 1, theory only), 2026-11-12

Nothing committed. Close: `close_round.sh`.

## Decisions taken without asking

1. m03-l03 art. 27 esquema rebuilt as a table of the article's rules, one row per paragraph (cuándo se exige, porcentaje,
   base y exclusiones, 12 meses, liquidaciones de declaraciones, cuándo no se exigen, requisito del 27.4, reducción del
   25 %), each row in the article's words with its conditions. Earlier attempts put every condition into one row's label
   and failed; here each condition is its own row, and the title says «Algunas reglas» (art. 27.3 and the comprobación
   paragraph are left out). Blind pass: 9 PASS (header and 8 rows), title FAIL (no «Algunas»); fixed and re-checked PASS
   by a second verifier. Reports: `r2-tax/m03-l03/verify-r2bc-recheck-5.md` and `-6.md` (named in the r2bc series so
   `taxprov.py` reads them after the old FAIL of the same row id). m03-l03 has three esquemas again.
2. The five citations: resolve with no content change (`cites.py` over m03-l01–l20: none unresolved; golden «0 naming
   a norm normativa.yaml lacks»).
3. Glyph: a calculator (display bar over four keys), same box, stroke and radius; accent ochre `#88521d`/`#d48f4a`
   (5.35:1 on paper, 5.98:1 on ink, 7.83:1 on black; luminance at the mean of the other three, within the 15 % test).
4. RDL 29/2026: BOE analysis shows no convalidation or derogation (only RDL 28/2026 related); sumarios to 12-11 carry no
   acuerdo; deadline 19-11-2026 not reached. Marks left; revert list not applied.
5. e2e: `signIn` and the global setup now activate four real courses, so counts changed (selector 4, sign-up 5, Cuenta 5
   with 4 active). The tax-lesson test matches «Practicar» by role: the lesson's own text says «practicar» (art. 54 LGT).

## Results

- Backend 3,192 passed, 21 skipped; frontend 752 passed, 116 skipped; `tsc -b` and `npm run lint` clean; e2e 99 passed
  (first run 97: the loose «Practicar» text match above), including `aeat-agentes.spec.ts` at 390 and 1280 px (selector,
  course page, tax lesson with esquema and example, Exámenes, Progreso) and the course PDF export (3.2 min).
- Goldens regenerated and read: only `citations.es.txt` changed (the eight esquema rows). C1, C2, crypto-futures
  unchanged; Android bundle byte-identical.

## Handoff (P → stage 2 / watch)

1. `aeat-agentes-hacienda` is `status: published`, `exercise_types: []`, no exams; glyph `calculator`, accent ochre.
2. 33 lessons, 193 glossary entries, 81 + 0 esquemas (m03-l03 keeps three), records for every lesson.
3. Platform: delta M behaviour confirmed in the browser tests; no migration, no new setting.
4. Deploy steps: `docs/deploy-aeat.md`. README and `docs/identity.md` updated.
5. Watch RDL 29/2026 from 18-11-2026 (revert list `r1/rdl-29-2026-revert-list.md`); RDL 31/2026 about 04-12-2026.
6. Elections of 29-11-2026 may change two dated copied sentences (m01-l03, m01-l04).
7. Open: `consilium-presidencia.html` not read live (403); C1/C2 80.2 and 95.1 LPAC wording; doubtful official keys
   and the retenciones classification for stage 2.
8. The browser checks ran on the throwaway e2e stack (Playwright), not on a deploy host.
9. Next: stage 2 on Juanjo's go-ahead. Nothing is committed.

---

# R2d — coverage by programme, after the external review (started 2026-11-14)

Requirements v1.2 (R4.7–R4.9); review `docs/aeat-external-review-2026-11.md` present. Working folder
`docs/age-verification/aeat/r2d/` (`spec-map.md`, `words-before.tsv`, `base-commit.txt`). Nothing committed.

## R2d — where to resume

- 2026-11-14, usage window cut during step 1. Eight Opus map auditors were launched per `r2d/spec-map.md`, writing
  `r2d/<lesson>-map.md`: III.18–III.20; III.15–III.17; III.9, III.11, III.10, III.6; III.13, III.12; III.14, III.5;
  III.8, III.7; III.1–III.4; II.5–II.1, I.6. Not yet launched: I.1–I.3, I.4–I.5, I.7.
- On resume: list `r2d/*-map.md`; a map without its «## Counts» section is incomplete — relaunch that tema with the
  same spec. Then launch the three remaining common groups, then write `docs/aeat-coverage-plan.md`.
- Decided so far (for «Decisions taken without asking»): map and report folders are named by lesson id
  (`r2d/m03-l18-map.md`, `r2d/m03-l18/`), as the tax part's decision 1; map auditors run on Opus, up to eight at once
  (no writers run in step 1); verdicts of this round must be read by a round driver (to write: `r2d/tools/r2dprov.py`,
  merging `r2/verify/*.md`, `r2-tax/<lesson>/verify*.md` and `r2d/<lesson>/verify*.md`, records into `r2/<lesson>.md`),
  because `provenance.py` reads only `r2/verify/` and is not patched in this round.
- 2026-11-14, after the reset: the eight map auditors produced no file before the cut and were resumed. Written:
  `r2d/spec-write.md`, `r2d/spec-verify.md`, `r2d/tools/r2dprov.py` (plan/record/apply; reads `r2/verify/*.md` for
  common lessons, `r2-tax/<lesson>/verify*.md`, then `r2d/<lesson>/verify*.md`, which win; pending files in
  `r2d/<lesson>/pending.md`). `taxprov.py` gained two keyword parameters (verdict source, pending folder; defaults keep
  its behaviour), the `_C1_SENTENCE_REPORTS` table and a retry over other C1 lessons when the first origin has no
  report. On the unchanged tree every lesson plans 0 pending except one sentence each in m01-l03 (l. 324) and m01-l07
  (l. 887), which occur twice with different citations (taxprov refuses inheritance then; provenance.py did not): they
  go to this round's blind check of I.3 and I.7.
- 2026-11-14, step 1 nearly done: maps written for every tema except I.2–I.5 (two auditors running). Cross-tema
  decisions in `r2d/coordinator-notes.md`; per-map «Coordinator notes» override the work list (III.5 arts. 106–108 and
  III.20 arts. 162–163 CAU restored against the maps, because the brief names them; I.6 depth rule; I.7 TREBEP range).
  32 sources downloaded (boe.es, sha256, `r2d/sources.md`) and merged into normativa.yaml; source index rebuilt.
  Step 2 running: writers (Sonnet) W1 III.9→III.11→III.12, W2 III.18→III.19→III.20, W3 III.13→III.14→III.5,
  W4 III.17→III.16→III.15. Not started: III.20 done by W2; III.6–III.8, III.10, III.1–III.4, common part. On resume:
  check each `r2d/<lesson>/writer.md` for the last item done; relaunch with the same brief for the rest.
- 2026-11-14: step 1 closed (32 maps; `docs/aeat-coverage-plan.md` «Before»). W1 done: III.9 (5,839 → 15,379 words),
  III.11 (5,202 → 9,861), III.12 (10,048 → ~21,000); pending 289 / 139 / 320 sentences, three blind Opus verifiers
  running (`r2d/<lesson>/verify.md`). W5 started: III.6 → III.7 → III.8 → III.10. Sources batch 3 merged (LOREG,
  EOMF, LO 3/1984, LO 2/1980); batch 4 (norms named inside quoted articles) running. Owed to step 4 (glossary):
  `g-recargo-ejecutivo` (III.9), `g-diligencia` (III.11), `g-oposicion`, `g-acta-de-inspeccion` (III.12).
- 2026-11-14: first blind pass III.9 286/3, III.11 136/3, III.12 316/4 (PASS/FAIL); replacements applied with
  `r2dprov.py apply`; five more III.9 sentences the verifier flagged outside its pending set (arts. 52.2, 52.4.a,
  53.2, 54.2.b RGR; 63.4 LGT: narrowing clauses dropped by R2) fixed by the coordinator in the articles' words; III.12
  Normativa LGT gains 43.1.f. Re-check 1 (different Opus) running on 12 + 3 + 5 rows. W2 done: III.18 6,276 → 29,835,
  III.19 9,706 → 31,232, III.20 5,369 → 16,041 words (whole articles copied by script from the snapshots); pending
  524 / 582 / 290, three blind verifiers running. W6 started: III.1 → III.4. Sources batch 4 merged (10 norms named
  inside quoted articles); the order fixing the card-payment limit of art. 36.2 RGR not identified (art. 36.2 names
  none). Open: art. 20.Uno.23.º e´) LIVA wording in force until 30-11-2026 (only the RDL 29/2026 wording is in the
  snapshot; fetch the LIVA art. 20 block versions from the BOE API).
- 2026-11-14: re-check 1 of III.9/11/12: 20/20 PASS — those three temas are verified. III.20 first pass 275/15
  (formatting debris from the scripted copy: consolidation marks, headings; one list lead-in without items; one
  «No confundir» cut); applied, two «—————» lines dropped by hand (two matches), re-check pending (8 rows). III.18:
  the wording of art. 20.Uno.23.º e´) in force until 30-11-2026 added from the BOE API block versions
  (`BOE-A-1992-28740_liva-art20-versiones_2026-11-14.xml`, new normativa entry); the BOE note attributes the change to
  art. 7.1 RDL 26/2026, the RDL 29/2026 text (art. 7.Uno) states it from 01-12-2026: the lesson keeps the RDL 29/2026
  mark (decision). W4 done: III.17 9,476 → 21,123, III.16 7,142 → 14,778, III.15 8,514 → 13,340 (part: 11 items open);
  W7 finishes III.15 then II.5 → II.1. Verifiers running: III.18, III.19, III.16, III.17 + III.20 re-check.
- 2026-11-14: W3 done: III.13 9,732 → 23,575, III.14 8,571 → 27,020, III.5 9,583 → ~24,190 words (W3 handed III.5 to a
  Sonnet sub-writer of its own when its context ran low; the cap of eight agents held because W3 waited for it).
  III.5 states both art. 104.h) RGAT and DA 3.ª.2 RD 1363/2010 (which names 104.i)): two official sources disagree.
- 2026-11-14: III.18 first pass 511/13: six text replacements applied; structural fixes by the coordinator (duplicate
  art. 22.Uno/Cuatro block removed, art. 9.1.º d) moved after the c) exceptions, two missing blank lines, the 23.º
  «La exención no comprenderá» list un-nested from letter b), the pre-01-12-2026 e´) wording moved out of the list of
  circumstances, Normativa: art. 12 whole + TFUE, Código Civil, LAU lines); re-check pending. III.19 first pass
  541/41 (structure, paragraph-level citations, PDF line-break artefacts, «nombrado en» lines): queued for a fixer
  writer. Decision: «nombrado en» lines are kept for every norm the copied law text names, and each such norm gets a
  snapshot (sources batch 5), as R2b did.
- 2026-11-14: first passes III.16 133/33, III.17 327/38, III.13 311/29, III.14 455/28; re-check of III.20 8/0 with
  3 extra rows (footnote marks, j bis) for the III.19/III.20 fixer. Replacements applied; two verifier instructions
  had been applied as text in III.16 (esquema header overwritten; «[Normativa: …]» notes): repaired by hand, and
  `taxprov.apply` now refuses instruction-like replacements and table-row replacements by prose. III.13: eight
  duplicated trailing citations removed. Running: III.5 first pass; re-check 1 of III.13/14/16/17/18.
- 2026-11-14 (after the second usage reset): all first-wave writers done. Words: III.1 3,794 → 14,803; III.2 4,145 →
  29,146; III.3 5,714 → 6,430; III.4 12,741 → 57,559; III.6 5,484 → 22,607; III.7 7,624 → 16,409; III.8 9,018 →
  21,769; III.10 3,956 → 6,811; III.15 → 25,995; I.1 5,843 → 13,393; I.2 8,509 → 13,610; I.3 7,325 → 14,762; II.1
  2,988 → 4,355; II.2 3,843 → 5,358; II.3 3,884 → 6,522; II.4 2,852 → 6,046; II.5 2,439 → 6,210. Three writers ran
  sub-writers of their own despite the brief (cap of eight agents exceeded for short spells; later briefs forbid it).
  III.5 first pass 433/9 and re-check 1 of III.13/14/16/17/18 (147/17) applied; `<br>`-joined Normativa lines and a
  leftover instruction repaired. Pending first passes: III.4 1,227; III.2 540; III.8 405; III.6 365; III.15 360;
  III.1 338; I.3 301; I.1 288; III.7 253; I.2 211; III.10 101; II.x 348; III.3 47. Running: verifiers III.4, III.2+3,
  III.8+10, III.6+7; writers I.4→I.5, I.6→I.7, fixer III.19/III.20, leftovers (II.1–II.5, I.2, I.3, III.7, III.1).
  Decisions: art. 116 RGR stays in both III.10 and III.12 (keep verified content); «Lo que más cae» lines unchanged
  unless their anchor moved (2022X-54 not added to III.7's ten; art. 10 RIRPF 500 € not added to III.15's).
- 2026-11-14: first passes III.8 392/13, III.10 93/8, III.6 354/11, III.7 249/4, III.2 509/31, III.3 46/1, III.4
  1,170/57 applied. Fixers: III.19 (41 rows + Normativa), III.20 (3), III.16/III.17 citation forms, fix queue for
  III.6/7/8/10. Coordinator: III.2 `arbol` rebuilt (apply had flattened the nested list into one line; new root
  «Organización central de la Agencia» per the verifier's note); III.2 «apartado undécimo bis/ter/quater» citations
  kept in the prose form «según el apartado …» (the parser cannot read «bis/ter/quater» apartados: platform item);
  RD 238/2026 entered in normativa.yaml as its own entry (file existed). Decision: norms named only inside copied
  article text with no snapshot are listed in one «… no figuran en `normativa.yaml`» line per lesson (the m03-l17 form)
  instead of being downloaded one by one; the list goes to the handoff for a later currency round.
  Running: verifiers III.15+III.1, I.1+I.2, re-check of 13 tax lessons; writers I.4→I.5, I.6→I.7, leftovers, fixer
  III.2/III.4/III.8.
- 2026-11-14: first passes I.1 270/18, I.2 204/7, III.15 334/26 (estimación objetiva paragraph checked against the
  three RDLs and three derogation resolutions), III.1 323/15 applied. III.2/III.4/III.8 fix queue done; RGAT note in
  normativa.yaml corrected (the boe.es notice closes art. 49 ter, not art. 49). Leftovers writer done for II.1–II.5,
  I.2 (Congress stage RC 108–123 added so m02-l01's pointer holds), I.3, III.7, III.1 (counts in each writer.md
  «Leftovers»). I.4 9,684 → 27,513 words (first writer); I.5 9,880 → 21,464 and a second writer finishing it.
  Running: verifiers I.4, II.1–II.5 + I.3, re-check of 13 tax lessons, re-check III.2/III.4; writers I.6→I.7, I.5
  finish, fixers III.15/I.1 and III.1/I.2/I.3.
- 2026-11-14: I.4 first pass 662/54 applied. Course-wide: bullets «- N. …» (16 in I.4, 4 in III.1, 6 in III.2)
  rendered as a nested ordered list (the review's «all "1."» defect) — dot escaped («- N\. …»), the verifier's fix.
  Re-check of 13 tax lessons 136/20 applied; hand fixes: III.19 bare «(Derogado)», III.20 incisos nested, III.18
  duplicated «Cambio pendiente» note. Ruling recorded in `spec-verify.md`: «Normativa» lists the articles the lesson
  cites in citations and every norm it names; articles of the same law named only inside copied text need no listing.
- 2026-11-14: first passes II.5 127/5, II.4 187/9, II.3 151/6, II.2 52/4, II.1 124/7, I.3 366/9; re-check III.2 35/7,
  III.4 30/7; all applied. A «(hoy: Ministerio para la Transformación Digital…)» note a fixer added to m01-l03 l. 699
  (art. 69.3 LRJSP) was unsupported (RD 1009/2023 places the Delegaciones' DG elsewhere): removed. I.6 4,601 → 32,121
  and I.7 17,952 → 35,136 words; I.5 → 30,882 (second writer done). Running: verifiers I.6, I.5, re-check round 3;
  writers: glossary (step 4), fixer III.1/I.2/I.3, I.7 leftovers + fix queue.

## R2d — where to resume (2026-11-14, evening)

- Step 1 done (maps, `docs/aeat-coverage-plan.md` «Before»). Step 2 done for all 32 temas (writers' notes in
  `r2d/<lesson>/writer.md`; I.7 has a «Second writer» running for its leftovers). Step 3: every lesson has a first
  blind pass; re-checks run in rounds (`verify-recheck-N.md`); fixes the apply tool cannot make go through
  `r2d/fix-queue.md` to a fixer writer. Step 4: glossary writer running (`r2d/glossary-owed.md` → `r2d/glossary/`).
- To resume: `cd backend && uv run python ../docs/age-verification/aeat/r2d/tools/r2dprov.py plan <all lessons>`;
  every lesson with pending rows gets a re-check by a verifier who has not checked that lesson's last pass; apply
  with `r2dprov.py apply` (refuses instruction-like replacements); structural notes → fix-queue → fixer; repeat until
  0 pending. Then `r2dprov.py record` for every lesson, glossary record, step 5 (scope audit Run 2, coverage, currency,
  RDL 29/2026 on the BOE, C1/C2 list, platform list, facts for the bank), `close_round.sh`, handoff.
- Lists for the handoff kept as found: C2 m01-l12 l. 155 has the uncorrected RGPD art. 18.1.a) («durante un plazo»;
  corrigendum 2021: «en un plazo») — fixed in this course's m01-l05; C1/C2 arts. 80.2/95.1 LPAC (from R2b).
- 2026-11-14: **RDL 29/2026 convalidated** (Resolución de 12-11-2026 del Congreso, BOE-A-2026-23755, BOE 13-11-2026;
  `r2d/currency-rdl.md`; resolution saved with sha256). RDL 31, 33, 35, 36/2026 still pending; RDL 28/2026 derogated
  (BOE-A-2026-23754; no course content rests on it). normativa.yaml: header line, notes, entries for RDL 29/2026 and the
  resolution; revert list annotated «no longer applicable»; course.yaml III.15 summary mark removed. Lesson marks
  («convalidación pendiente» / «sin convalidar» for RDL 29/2026 only) to be removed after the running fixer finishes,
  then blind check of every changed sentence.
- 2026-11-14 (late): RDL 29/2026 marks removed from III.4, III.6, III.15, III.16, III.18 by
  `r2d/tools/rdl29_convalidated.py` (in-text «convalidación pendiente» dropped; «Normativa» «Cambio pendiente … sin
  convalidar» → «Redacción … convalidado el 12-11-2026 (BOE-A-2026-23755), en vigor desde …» when effects started, else
  «Cambio pendiente … convalidado …, con efectos desde …»); changed sentences go through the round-5 re-check. I.6
  first pass 898/31, I.5 640/13, I.7 903/26, round-4 re-check (11 lessons) all applied. Glossary: writer (199 → 204
  after restoring g-recusacion, g-oposicion and the three complementos under the keep rule; g-convenio removed: no
  lesson uses the LRJSP sense), blind check 186/18, fixer running (3 definitions, link_except for 10 entries, three
  lesson sentences to ground restored entries). Summaries: 20 rewritten, blind check running. Step 5: scope audit Run 2
  started (`r2d/spec-audit.md`, two Opus auditors, reports `r2d/audit/<lesson>.md`).
- 2026-11-17 (after the usage pause): coverage re-checked — 374 of 452 coverage questions confirmed by script (their
  R2/R2-tax COVERED quote still verbatim in the lesson), the other 78 by a blind Opus check
  (`r2d/coverage-recheck.md`): 78 COVERED, 0 MISS. Coverage 137/137 and 315/315 hold. BOE re-read 16–17-11: no
  further convalidation or derogation. `r2d/bank-facts.md` (facts with no pack question, per tema) and
  `r2d/c1-c2-list.md` (151 inherited sentences changed here: 134 from C1, 17 from C2) written. Round-5 re-check
  (17 lessons) 134/20 applied; final fixer running; glossary/summaries re-check running; scope audit Run 2 resumed.
- 2026-11-17: **depth correction (Juanjo)**. Words before → after in `r2d/words.md` (228,756 → 694,151; 28 lessons more
  than doubled or exceed 15,000 words). Reduction pass `r2d/spec-reduce.md`: only R2d-added text is reduced; articles
  an official question asks or «Lo que más cae» covers keep full treatment; other added articles → rule, conditions,
  exceptions in 2–4 verbatim fragments with citation; legal enumerations complete but moved into `tabla` esquemas; maps
  unchanged (reduced = still treated). Reworded/moved sentences show as pending in `r2dprov.py plan` and get a blind
  check; nothing else is re-verified. Reducers running: III.4+III.18, III.2+III.19. Before it, long multi-rule
  paragraphs (step 2f) were split by `r2d/tools/split_paragraphs.py` in the tax lessons (sentence ids kept: 0 new
  pending except in III.15/III.20 from fixes). Glossary re-check 1: 16/2 (applied); summaries re-check 1: 3/5 (applied).
- 2026-11-17: **reduction pass stopped and discarded (Juanjo)**; replaced by the build pass (`r2d/spec-build.md`): base
  = HEAD lesson; add only whole sentences byte-identical to verified pool sentences (`r2d/expansion/`, frozen copy of the
  700,896-word expansion incl. audit additions); enumerations as esquemas from verified items; completeness over size
  (1.6 × HEAD words excl. esquema rows is a target, not a limit; no article «not treated» inside a range).
  `r2d/tools/build_check.py` proves byte-identity per sentence and writes `r2d/<lesson>/verify-build.md` (PASS rows
  pointing to the report where the twin passed). The seven lessons the reducers had touched (III.2, III.4, III.5,
  III.18, III.19, I.6, I.7) were restored from the reducers' own pre-reduction copies (each byte-equal to the pool);
  the stopped verifier wrote no report; «Reduction pass» notes marked DISCARDED. Builders running: III.18, III.9, III.13.

- 2026-11-17 (build pass): III.5, III.16, III.17 built (2.33×, 2.11×, 1.78× HEAD excl. rows; nothing left out for size). Reader-fixer spec `r2d/spec-fix.md` added (move / add pool sentence before rewording). Launched: Opus re-check of III.13/9/11/12 pending rows; fixers III.14+III.18, III.17+III.16 (read+fix), III.5 (read+fix); builders III.19, III.20. III.15 builder still running. Decision: HEAD esquema «Plazo máximo de resolución y cómputo» (III.5) kept — the build does not cut. III.16 gaps: arts. 49–52 and 61.2, 61.4–6 RIRPF not in the pool → listed. Glossary links g-convenio/g-servicios-comunes (III.5, III.17) left to step 4.

### R2d build pass — where to resume (2026-11-17, usage limit reached)

- Fully through (built, flags fixed, Opus PASS): III.13, III.9, III.11, III.12, III.5, III.18.
- Built, Opus owed/running when stopped: III.15 (74 rows, recheck-4), III.16 (3, recheck-6), III.17 (2, recheck-6),
  III.14 (1, DA undécima.8: second re-check — a FAIL drops it). Check whether those report files exist; rerun what is missing.
- III.20: recheck-5 PASS 50 · FAIL 6, replacements applied; still to do by hand: move the art. 221.2 RE paragraph rows
  (2.º–4.º párrafos, under row c)) out of the table into prose after it; then re-check the 6 by a different verifier.
- Built, reader-fixer was running (may be partial: rerun `spec-fix.md` from step 1 if standalone.md lacks «## Fixes»):
  III.6, III.10, III.7. III.8 built (validation exit 0), reader-fixer not started.
- III.1 built: 3.62× HEAD; 25 «not in pool» are new esquema header rows `| Apartado | Contenido | Cita |` → extend
  build_check to accept header rows (they are not sentences of the law), then reader-fixer. Pool gaps in build.md → add to pool-gaps.md.
- III.19 builder was running: check build.md exists, else rerun.
- Not started: III.2–III.4, II.1–II.5, I.1–I.7, m00-l01. Then pool-gaps writer batch, close-out steps (see summary list).

- 2026-11-17 (resumed): III.14, III.16, III.17 fully through (recheck-6 PASS, written before the stop). III.7 and III.10
  reader-fixers had finished. III.20: art. 221.2 RE paragraphs 2–4 moved out of row c) into prose by the coordinator.
  III.1: 25 new esquema headers set to the verified `| Elemento | Contenido | Cita |` (decision: no new header text).
  III.19 reset to HEAD and rebuilt from scratch. Running: Opus III.15 (74) and III.10/III.7/III.20; reader-fixers
  III.6, III.8, III.1; builders III.19, III.2, III.3.

### R2d — where to resume (2026-11-18, usage limit reached)

- Fully through (build + flags + Opus + gap fill): every lesson except I.2, I.3, I.7 (m00-l01 unchanged by design).
- I.3: recheck-5 applied for 2 rows; 4 extra rows in `r2d/m01-l03/verify-recheck-5.md` (e55bac9867, 513ed2b33a,
  21e2f228a0, 3abfcea0d7 — art. 100.1/106.1 LRJSP Ley 7/2007 cuts) were not in pending.md: apply their replacements by
  hand. Also owed: move the art. 10.1–10.2 paragraph after 9.7; add «Código Civil: nombrado en el art. 119.2 LRJSP»;
  add art. 110.1 LRJSP places to the LGP, Ley 33/2003 and LPAC lines. Then one Opus re-check.
- III.19: DA 3.ª Ley 10/2014 sentence replaced (recheck-7 FAIL 1 = failed re-check 1); re-check owed.
- I.2: structural fixer done (moves, Normativa, art. 93.6 LOPJ, RS 92.3/160.2 closings, 17.3 LO 3/1981 rewrite). Owed:
  drop the Mandato copy of art. 582.1 LOPJ (id 6387614a14, wrapped over lines ~1747–1749; the Estatuto copy stays);
  then one Opus re-check of every pending row (`r2dprov.py plan m01-l02`).
- I.7: reader-fixer was stopped mid-run → rerun spec-fix on m01-l07 (check standalone.md progress), then Opus (~440 rows).
- Glossary g-silencio-administrativo and the 8 summaries replaced in course.yaml: re-check owed (different verifier).
- Then close-out: glossary_record.py, r2dprov record all lessons + test_provenance, scripted Normativa pass (norms named
  without a line), coverage 452/452, word counts, coverage plan «After», scope audit «Run 2», close_round.sh, handoff.
- Decisions to report «for Juanjo»: r2d/coordinator-notes.md (all sections), dropped.md, c1-c2-list.md, pool-gaps.md.
- I.7 caution: the stopped reader-fixer's last note was «My sed mangled it; fix ed.py directly» (its scratch script). Before rerunning, diff m01-l07.md against the gap-fill result (cites.py, index_sources.py, build_check) and repair or restore.

- 2026-11-18 (resumed again): I.7 reader-fixer had finished (70 flags; lesson validates) → Opus I.7 in 2 parts running.
  I.2: art. 582.1 Mandato duplicate removed → Opus re-check (166 rows) running. I.3: 4 extra replacements applied by
  hand, art. 10 LRJSP paragraph moved after 9.7, Normativa entries added → re-check running together with III.19,
  g-silencio-administrativo and the 8 summaries.
