# Scope, coverage and currency audit — aeat-agentes-hacienda

Requirements v1.1, R4.6 (C1's section 4b) and R3.5. Method: C2's audit (`docs/age-c2-scope-audit.md`, Run 1). Each run
appends a dated section; nothing above a later run's header is rewritten.

---

# Run 1 — R2b, 2026-11-11

First run, after R2 closed for the three parts. Programme: `content/aeat-agentes-hacienda/sources/programa.md` (Anexo I,
32 temas). Exams: the 680 first-exercise questions of OEP 2020–2025 parsed in R0a
(`docs/age-verification/aeat/r0a/parsed/master.json`, estados in `docs/aeat-official-exams-ledger.md`); OEP 2022–2025 with
the 2022 extraordinario for coverage, OEP 2020–2021 as evidence for keeping a section. Questions of other courses' exams
are not evidence here. Working reports: `docs/age-verification/aeat/r2b/` (`scope/`, `currency/`, `tools/`, `verify/`).
Nothing is committed.

## Verdict per part

- **Intro lesson (m00-l01) — dentro de alcance.** 9 sections: 5 mapped to Base 6 and R4.1, 4 instrumental (how the
  course is built, what it does not cover).
- **I. Organización del Estado y funcionamiento de la AGE — dentro de alcance, cubierto y al día.** 381 sections
  (I.1–I.7): 364 mapped, 3 instrumental, 9 kept by exam evidence (8 notes), 5 removed; no gaps. Coverage of its
  coverage questions unchanged by the cuts.
- **II. Derecho Administrativo General — dentro de alcance, cubierto y al día.** 67 sections: 66 mapped, 1
  instrumental; no removals. Two facts an AEAT question needs were missing and are written (art. 107.4 LPAC, CCAA half;
  art. 39.4 LPAC); the II.1 note naming an Auxiliar exam was wrong (the section maps to «El Reglamento») and is gone.
- **III. Organización de la Hacienda Pública y Derecho Tributario — dentro de alcance, cubierto y al día.** 501
  sections: 467 mapped, 3 instrumental, 3 assigned to another tema (each covered there), 20 kept by exam evidence (13
  notes), 8 removed; no gaps.
- **Coverage:** 137 / 137 (parts I–II) and 315 / 315 (part III) still hold after the cuts.
- **Currency:** every norm at its latest boe.es / Cellar consolidation; 13 norms named inside other norms entered with
  snapshots; annual figures re-checked for 2026; RDL 29/2026 not due (19-11-2026), revert list not applied.

## Part A — scope

Auditor spec: `r2b/scope/spec.md` (C2's, with the AEAT inputs). Reports (four blind Opus auditors):
`scope/a-m00-m01-l04.md`, `scope/b-m01-l05-m02.md`, `scope/c-m03-l01-l10.md`, `scope/d-m03-l11-l20.md`. Sections are every
`##`, `###` and `####` heading except «Lo que más cae», «Normativa» and «Fuentes». Counts before the fixes.

| Tema | Lesson | Sections | Mapped | Instrumental | Other tema | Kept (exam) | Removed | Gaps |
|---|---|---|---|---|---|---|---|---|
| intro | m00-l01 | 9 | 5 | 4 | 0 | 0 | 0 | 0 |
| I.1 | m01-l01 | 43 | 43 | 0 | 0 | 0 | 0 | 0 |
| I.2 | m01-l02 | 54 | 53 | 0 | 0 | 1 | 0 | 0 |
| I.3 | m01-l03 | 53 | 48 | 1 | 0 | 3 | 1 | 0 |
| I.4 | m01-l04 | 81 | 73 | 1 | 0 | 3 | 4 | 0 |
| I.5 | m01-l05 | 58 | 58 | 0 | 0 | 0 | 0 | 0 |
| I.6 | m01-l06 | 13 | 13 | 0 | 0 | 0 | 0 | 0 |
| I.7 | m01-l07 | 79 | 76 | 1 | 0 | 2 | 0 | 0 |
| II.1 | m02-l01 | 17 | 17 | 0 | 0 | 0 | 0 | 0 |
| II.2 | m02-l02 | 27 | 26 | 1 | 0 | 0 | 0 | 0 |
| II.3 | m02-l03 | 10 | 10 | 0 | 0 | 0 | 0 | 0 |
| II.4 | m02-l04 | 7 | 7 | 0 | 0 | 0 | 0 | 0 |
| II.5 | m02-l05 | 6 | 6 | 0 | 0 | 0 | 0 | 0 |
| III.1 | m03-l01 | 23 | 22 | 0 | 1 | 0 | 0 | 0 |
| III.2 | m03-l02 | 11 | 11 | 0 | 0 | 0 | 0 | 0 |
| III.3 | m03-l03 | 21 | 19 | 1 | 0 | 1 | 0 | 0 |
| III.4 | m03-l04 | 24 | 23 | 0 | 0 | 1 | 0 | 0 |
| III.5 | m03-l05 | 36 | 31 | 0 | 0 | 0 | 5 | 0 |
| III.6 | m03-l06 | 17 | 17 | 0 | 0 | 0 | 0 | 0 |
| III.7 | m03-l07 | 32 | 32 | 0 | 0 | 0 | 0 | 0 |
| III.8 | m03-l08 | 31 | 31 | 0 | 0 | 0 | 0 | 0 |
| III.9 | m03-l09 | 20 | 20 | 0 | 0 | 0 | 0 | 0 |
| III.10 | m03-l10 | 12 | 12 | 0 | 0 | 0 | 0 | 0 |
| III.11 | m03-l11 | 20 | 19 | 0 | 0 | 1 | 0 | 0 |
| III.12 | m03-l12 | 40 | 39 | 0 | 1 | 0 | 0 | 0 |
| III.13 | m03-l13 | 33 | 24 | 0 | 0 | 7 | 2 | 0 |
| III.14 | m03-l14 | 26 | 26 | 0 | 0 | 0 | 0 | 0 |
| III.15 | m03-l15 | 25 | 25 | 0 | 0 | 0 | 0 | 0 |
| III.16 | m03-l16 | 29 | 29 | 0 | 0 | 0 | 0 | 0 |
| III.17 | m03-l17 | 33 | 30 | 0 | 1 | 2 | 0 | 0 |
| III.18 | m03-l18 | 20 | 19 | 0 | 0 | 1 | 0 | 0 |
| III.19 | m03-l19 | 27 | 24 | 2 | 0 | 1 | 0 | 0 |
| III.20 | m03-l20 | 21 | 14 | 0 | 0 | 6 | 1 | 0 |
| **Total** | | **958** | **902** | **11** | **3** | **29** | **13** | **0** |

Instrumental: m00-l01 (four sections on what the course covers), I.3 composition of the Gobierno, I.4 one, I.7
«Cuerpos, escalas y grupos de clasificación», II.2 «Órgano, procedimiento y contenido», III.3 «Tipo de gravamen» (art.
55 LGT, needed for the cuota íntegra), III.19 «Cuotas deducibles» and «Operaciones que originan el derecho a la
deducción». Other tema: III.1 «Los tributos» (III.3 covers it), III.12 «Tercerías» (III.11 S5c; m03-l11 points there),
III.17 «Pago fraccionado» (III.6; m03-l06 covers it, m03-l17 points there).

### Sections removed

Each maps to no programme sentence and no admissible AEAT question of 2020–2025 asks its content. Removed whole, with
the precepts only it cited from «Normativa» and the esquema rows that rested only on it. No coverage question rested on
them, no «Lo que más cae» line pointed at them, and no glossary entry lost its use, so the glossary waiting list stays
empty.

| Lesson | Section | Note |
|---|---|---|
| m01-l03 | «La Comisión General de Secretarios de Estado y Subsecretarios» (art. 8 Ley 50/1997) | its node left the Gobierno `arbol`, which was then dropped (R2c, four per lesson) |
| m01-l04 | El Consejo Europeo: «Funciones», «Reuniones y votaciones», «El Presidente», «El Alto Representante» (arts. 15.1, 15.3–15.6, 18 TUE; 235 TFUE) | the programme names «El Consejo», not the Consejo Europeo; 2022-8, 2021-10, 2025-79 and 2020-34 use these facts only as wrong options. «Composición» stays (2025-50). Four esquema rows (votación, Presidente's mandate) went with them |
| m03-l05 | «Consultas tributarias escritas», «Efectos de las contestaciones a consultas» (arts. 88–89 LGT) | the 2025 programme dropped «la consulta tributaria»; the only questions (2021-46, 2021-47) are `fuera de temario`. Art. 85.2 still names the instrument |
| m03-l05 | «Medios y valoración de la prueba», «Valor probatorio de las diligencias», «Presunciones» (arts. 106–108 LGT) | the programme now says «Carga de la prueba» (art. 105, kept); no question asks arts. 106–108. Código Civil and LEC «Normativa» lines went with art. 106.1 |
| m03-l13 | arts. 195 and 196–197 LGT (two `###`) | no question asks them; their three rows left the art. 194–197 table, whose lead now says «del artículo 194 LGT» |
| m03-l20 | «Declaraciones en aduana normales» (arts. 162–163 CAU) | sección 2 of the CAU chapter; the programme names only sección 1, «disposiciones generales» |

Also removed at sentence level: the list of motivos de oposición a la providencia de apremio (art. 167.3 LGT, m03-l11).
The programme keeps «Providencia de apremio: concepto y plazos para el pago» and the ledger rules 2022X-70 `fuera de
temario` for that reason.

### Sections kept by exam evidence

Each now opens with `:::note{type=info}` «Fuera del enunciado literal del programa; preguntado en …» (a container note
covers its `###`). Every cited stem was re-read by the coordinator.

| Lesson | Section | Asked in |
|---|---|---|
| m01-l02 | «El Ministerio Fiscal» | OEP 2024, 56; OEP 2020, 9 |
| m01-l03 | «Las Comisiones Delegadas del Gobierno» | OEP 2023, 84 |
| m01-l03 | «Competencia de los órganos» | OEP 2020, 7 and 12 |
| m01-l03 | «Inscripción en el Inventario de Entidades» | OEP 2023, 35 |
| m01-l04 | «Las sedes» | OEP 2024, 62 |
| m01-l04 | «El Consejo Europeo» (with «Composición») | OEP 2025, 50 |
| m01-l07 | «Órganos de selección» | OEP 2021, 20 |
| m01-l07 | «Acceso de las personas con discapacidad» | OEP 2022 extraordinario, 17 |
| m03-l03 | «Vigencia, sujeción, interpretación y calificación» | OEP 2022 extraordinario, 33 |
| m03-l04 | «Obligaciones y deberes de la Administración tributaria» | OEP 2025, 43 |
| m03-l11 | «Conservación de actuaciones» | OEP 2020, 79 |
| m03-l13 | «Infracciones y sanciones en particular» (arts. 191–194, 198–206) | OEP 2022, 73; 2022 extr., 83; OEP 2023, 70; OEP 2024, 74; OEP 2025, 10 and 14; OEP 2020, 78; OEP 2021, 93 |
| m03-l13 | «Recursos contra sanciones» | OEP 2022, 70; 2022 extr., 86 |
| m03-l17 | «Valoración de los elementos patrimoniales» | OEP 2024, 86 |
| m03-l17 | «Efectos de la valoración contable diferente a la fiscal» | OEP 2024, 94 |
| m03-l18 | «Adquisiciones intracomunitarias de bienes» | OEP 2025, 8 |
| m03-l19 | «Requisitos formales, nacimiento, ejercicio y caducidad» | OEP 2022, 96; OEP 2023, 80 |
| m03-l20 | «Definiciones» | OEP 2022, 98; OEP 2025, 76 |
| m03-l20 | «Valor en aduana» | OEP 2022, 100; OEP 2023, 68; OEP 2024, 85 |
| m03-l20 | «Depósito temporal» | OEP 2022 extr., 98; OEP 2025, 64 |
| m03-l20 | «Regímenes de tránsito y de depósito» (with «Tránsito de la Unión», «Depósito aduanero») | OEP 2023, 73; OEP 2025, 33 |

### Gaps and missing facts

No programme sentence lacks a covering section. Facts an AEAT question needs, found missing and written under the R2
rules (blind-checked):

- m02-l02: art. 107.4 LPAC now names «la Administración General del Estado o … las Comunidades Autónomas» (2023-71);
  art. 39.4 LPAC added (option of 2024-69 and 2023-44).
- m02-l04 (found by the R2c writer): art. 80.2 LPAC «salvo que una disposición o el cumplimiento del resto de los plazos
  del procedimiento permita o exija otro plazo mayor o menor» and art. 95.1 «acordará el archivo de las actuaciones,
  notificándoselo al interesado», both shortened past the article in the inherited prose.

Not written: the degree of affinity of a sister's spouse (2024-68). No norm in the course's snapshots states it
(Código Civil arts. 915–919 count consanguinity only), and the course states nothing an official source does not.

### Noted, not acted on

From the auditors' reports (no coverage question asks what is missing): I.3 moción de censura and cuestión de confianza
procedure (arts. 112–113 CE); I.2 control of the Gobierno and art. 134 CE; I.4 CCAA financing (arts. 156–158 CE, listed
in «Normativa» only); m00-l01 «Conservación de calificaciones»; II.1 S3 and II.3 S1 thin; II.1 «La ley» carries arts.
75.2–3 and 92.3 CE (I.2 matter, asked as II.1 [I.2]); I.6 the registry-sex paragraph (Ley 4/2023, unasked); II.4 art.
81.3 LPAC; m03-l14 does not point to m03-l13 «Recursos contra sanciones»; three reference questions no lesson answers
(2021-38 ONIF, 2020-59 art. 57.1 RGAT, 2021-68 aplazamiento organs); 2021-13 (Ley 37/2007, excluded by normativa.yaml).
The ledger classifies retenciones questions inconsistently (2021-59, 2021-61, 2022-89 `fuera de temario`; 2023-64 and
later `vigente`): for stage 2.

## Part B — coverage 2022–2025

The per-lesson coverage checks ran in R2 (`aeat/r2/coverage/`, `aeat/r2-tax/<lesson>/coverage.md`): 137 / 137 and 315 /
315. After the cuts: no coverage question's norm or evidence cites a removed precept (packs searched for the removed
articles and terms), and every COVERED report line's quoted passage outside the removed sections is still in its lesson.
The only coverage questions touching removed material, 2025-50 and 2025-79 (I.4), are answered by kept text (art. 15.2
TUE, «Composición»; art. 17.8 TUE).

## Part C — currency

`r2b/currency/normativa.md` and `pages.md`. All 96 BOE entries at their latest consolidation on 2026-11-11; the EU texts
at their latest Cellar versions; the RGPD corrigenda copied from C1 (same sha256), so the RGPD note is true. 13 norms the
lessons name only inside other norms entered with snapshots (11 boe.es downloads, 2 C1 copies). Annual figures: every
value found in the stored text of its norm; no 2026 Ley de Presupuestos; Ley 31/2022's DA 42.ª and 90.ª unchanged.
RDL 29/2026: not convalidated or derogated on 2026-11-11; deadline 19-11-2026; revert list not applied. No «(desde …)»
mark is past. Saved pages: 10 same text, 1 changed with no place resting on the changed lines, 1 not read (403; the
site refuses automated clients, not worked around).

## Prose gaps found by the esquema check (R2c)

Rows the blind verifiers failed because the prose left out the same rule; the prose was fixed first (writer notes
`aeat/r2c/prose-gaps.md`), then re-checked by verifiers who had not seen the earlier reports: art. 27.2 (regularisation
of other periods, a)–d)) and 27.4 LGT (m03-l03); art. 17.2 párr. 2 RGAT (m03-l04); art. 40.2–3 LIS and LIS DA 14.ª.1
(pagos fraccionados of contribuyentes with a cifra de negocios of at least 10 millones, m03-l06); art. 235.1 párr. 4 and
242.2 párr. 2 LGT (m03-l14); arts. 58.1–2 and 59.1 LIRPF (m03-l16); LIS DA 15.ª.1 (limits for grandes empresas on arts.
26.1 and 11.12, m03-l17; the «70 por ciento» statements now refer to «el límite del artículo 26.1»); art. 99.Tres last
paragraph and 99.Cinco párr. 3 LIVA (m03-l19); arts. 80.2 and 95.1 LPAC (m02-l04).

## Closing checks

All on the final tree (2026-11-11), with `docs/age-verification/aeat/tools/close_round.sh`.

- **Blind checks of every edit:** R2b notes, Normativa lines and prose sentences; R2c rows and titles: first pass 38
  FAIL, re-check 1: 11, re-check 2: 3, re-check 3: 2, re-check 4: 1, each fixed or, after two failed re-checks, dropped
  (one m03-l03 recargo row, then its esquema; one m03-l17 «Lo que más cae» line, replaced by a narrower one that passed).
  Reports: `aeat/r2/verify/r2bc*.md`, `aeat/r2-tax/<lesson>/verify-r2bc*.md`. `test_provenance.py` passes on every
  lesson and the glossary.
- **Goldens** regenerated and read: `citations.es.txt` 4,504 → 4,471 prose citations (the cuts), 256 → 438 esquema rows,
  192 → 190 Normativa norms (the Código Civil and LEC lines went with art. 106 LGT), 18 → 5 naming a norm normativa.yaml
  lacks (the 13 entered; the 5 left are worded «disposición transitoria cuadragésima cuarta» LIS and «art. 89.Uno y
  Tres LIVA», parser items for section M); `glossary-links.es.txt` 340 → 338 web marks (two lost with the III.5 and III.11
  cuts, `g-comunicacion-de-datos` gains its first mark in m03-l04, `g-devengo`'s first mark in m03-l15 moves into an
  esquema label); `lesson-refs.es.txt` unchanged.
- **crypto-futures, C1, C2:** unchanged. **Android bundle** re-exported: byte-identical to `dist/bundle`.
- **Full suites:** backend 3,144 passed, 23 skipped, 1 failed: the frozen citations golden, on the two-norm Ceuta/Melilla
  parenthetical of m01-l04 (`preámbulo LO 1/1995 y preámbulo LO 2/1995` anchored to Melilla instead of Ceuta), the known
  platform nondeterminism (tax part, decision 26); the only failure; rerun once: `test_citations.py`,
  `test_provenance.py`, `test_esquema.py`, `test_saved_pages.py` 1,159 passed. Frontend 738 passed, 114 skipped; `tsc -b`
  clean. `ruff`, `ruff format`, `mypy` clean on the two new round tools.
