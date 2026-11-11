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

R2, common part: done. Next: R2 tax temas (III.1–III.20) in groups, then R2b (scope, coverage, currency), R2c
(esquemas), M (platform: published course without exercises), P (publication). Before the tax temas: the RDL 29/2026
convalidación outcome (19-11-2026) and the CAU XHTML indexer.
