# Scope, coverage and currency audit — age-auxiliar-c2

Requirements v1.2: R4.1 takes C1's section 4b (`docs/age-administrativo-course-requirements.md`). Method: C1's audit
(`docs/age-scope-audit.md`, Run 1 for scope, Run 2 for currency). Each run appends a dated section; nothing above a
later run's header is rewritten.

---

# Run 1 — R2b, 2026-11-06

First run, after R2 closed for both bloques. Programme: `content/age-auxiliar-c2/sources/programa.md` (Anexo I,
punto 3). Exams: the eight Auxiliar questionnaires parsed in R0a (`docs/age-verification/c2/r0a/parsed/`); 2022–2025
for coverage, the OEP 2020 sets («programa anterior») as evidence for keeping a section, as in C1. Working reports in
`docs/age-verification/c2/r2b/` (`scope/`, `currency/`, `tools/`). Nothing is committed.

## Verdict per bloque

- **Intro lessons (m00-l01, ps-l01) — dentro de alcance.** 29 sections, all mapped to Anexo I and R4.1 / R6.4.
- **Bloque I — dentro de alcance, cubierto y al día.** 473 sections: 460 mapped, 1 instrumental, 7 kept by exam
  evidence (6 with the note; the seventh is a parent heading whose own text maps), 5 removed; no gaps. Coverage
  134/134, unchanged by the cuts. No norm newer; RDL 31/2026 still unconvalidated (its pending marks stay). Two
  prose gaps found by the esquema check are open (theory ledger, «Open items after R2b / R2c»).
- **Bloque II — dentro de alcance y al día; cubierto salvo «sin fuente oficial».** 116 sections: 112 mapped, 4 kept
  by exam evidence (2 notes); no removals, no gaps. The coverage MISSes are the «sin fuente oficial» facts below (no
  admissible page states them), unchanged by this run. Saved pages: 312 of 325 read the same live, 10 changed with
  every place resting on them PASS, 1 not read (403), and the V Plan and CE análisis checked by hand.

## Part A — scope

Auditor spec: `r2b/scope/spec.md` (C1's, with the C2 inputs). Reports: `scope/m01-a.md` (m00-l01, ps-l01, I.1–I.9),
`scope/m01-b.md` (I.10–I.16), `scope/m02.md` (II.1–II.12), three blind Opus auditors. Sections are every `##`, `###`
and `####` heading except «Lo que más cae», «Normativa» and «Fuentes». Counts before the fixes.

| Tema | Lesson | Sections | Mapped | Instrumental | Other tema | Kept (exam) | Removed | Gaps |
|---|---|---|---|---|---|---|---|---|
| intro | m00-l01 | 9 | 9 | 0 | 0 | 0 | 0 | 0 |
| psicotécnicos | ps-l01 | 20 | 20 | 0 | 0 | 0 | 0 | 0 |
| I.1 | m01-l01 | 13 | 12 | 0 | 0 | 0 | 1 | 0 |
| I.2 | m01-l02 | 32 | 32 | 0 | 0 | 0 | 0 | 0 |
| I.3 | m01-l03 | 32 | 32 | 0 | 0 | 0 | 0 | 0 |
| I.4 | m01-l04 | 22 | 22 | 0 | 0 | 0 | 0 | 0 |
| I.5 | m01-l05 | 22 | 21 | 0 | 0 | 1 | 0 | 0 |
| I.6 | m01-l06 | 9 | 8 | 0 | 0 | 1 | 0 | 0 |
| I.7 | m01-l07 | 24 | 24 | 0 | 0 | 0 | 0 | 0 |
| I.8 | m01-l08 | 32 | 32 | 0 | 0 | 0 | 0 | 0 |
| I.9 | m01-l09 | 47 | 47 | 0 | 0 | 0 | 0 | 0 |
| I.10 | m01-l10 | 29 | 29 | 0 | 0 | 0 | 0 | 0 |
| I.11 | m01-l11 | 40 | 40 | 0 | 0 | 0 | 0 | 0 |
| I.12 | m01-l12 | 25 | 25 | 0 | 0 | 0 | 0 | 0 |
| I.13 | m01-l13 | 60 | 56 | 0 | 0 | 1 | 3 | 0 |
| I.14 | m01-l14 | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| I.15 | m01-l15 | 23 | 17 | 1 | 0 | 4 | 1 | 0 |
| I.16 | m01-l16 | 13 | 13 | 0 | 0 | 0 | 0 | 0 |
| II.1 | m02-l01 | 9 | 9 | 0 | 0 | 0 | 0 | 0 |
| II.2 | m02-l02 | 20 | 19 | 0 | 0 | 1 | 0 | 0 |
| II.3 | m02-l03 | 21 | 18 | 0 | 0 | 3 | 0 | 0 |
| II.4 | m02-l04 | 21 | 21 | 0 | 0 | 0 | 0 | 0 |
| II.5–II.12 | m02-l05…l12 | 45 | 45 | 0 | 0 | 0 | 0 | 0 |
| **Total** | | **618** | **601** | **1** | **0** | **11** | **5** | **0** |

The only instrumental section is I.15 «El sector público estatal» (art. 2 LGP, the sector art. 32 LGP refers to;
asked in convocatoria 2024 modelo A, P1 24).

### Sections removed

Each maps to no programme sentence and no Auxiliar question of 2020–2025 asks its content. Removed whole, with the
precepts only it cited from the «Normativa» lines. No coverage question rested on them (`c2/bloque-i/coverage/`), no
«Lo que más cae» line pointed at them, and no glossary entry lost its second lesson (`g-personal-eventual` is still
used in m01-l13 and m01-l08), so the glossary waiting list stays empty.

| Lesson | Section | Note |
|---|---|---|
| m01-l01 | «Las reformas» (the four CE reforms) | C1 keeps it on Administrativo questions; no Auxiliar question asks it (searched «reformad», «veces», «13.2», «135», «69.3»). The «Otras fuentes» line went with it; `boe-analisis-ce.xml` now serves m02-l01 only (`fuentes.yaml`). |
| m01-l13 | «Personal eventual» (art. 12 TREBEP; art. 20.2 Ley 30/1984) | Not personal funcionario (I.13 S1). The class stays named in the art. 8.2 list. |
| m01-l13 | «Personal directivo» (art. 13.1 TREBEP; art. 123.3 RDL 6/2023) | convocatoria 2024 modelo A, P1 29 is answered by the provisión rule (Orden TDF/379/2024), which stays. |
| m01-l13 | «Causas de pérdida» (arts. 63–66 TREBEP) | Art. 63 stays in «Normativa»: the excedencia paragraph still names it. |
| m01-l15 | «Principios y reglas de gestión presupuestaria» (arts. 27, 34.1 LGP) | Art. 34.1 stays, stated in «Ejecución». |

### Sections kept by exam evidence

Each now opens with `:::note{type=info}` «Fuera del enunciado literal del programa; preguntado en …».

| Lesson | Section | Asked in |
|---|---|---|
| m01-l05 | «El Plan Anual Normativo» | convocatoria 2024 (modelo A), primera parte, reserva 1 |
| m01-l06 | «Los planes de Gobierno Abierto» | convocatoria 2024 (modelo A), P1 9; convocatoria 2022, P1 12 (`norma modificada`) |
| m01-l13 | «Jubilación» (art. 67 TREBEP) | OEP 2020 (llamamiento extraordinario), P1 23 |
| m01-l15 | «Principios de la programación presupuestaria» | convocatoria 2022, P1 27 |
| m01-l15 | «Programación plurianual» | convocatoria 2025 (modelo A), P1 28; convocatoria 2024 (llamamiento extraordinario), P1 29; OEP 2020 (llamamiento extraordinario), P1 24 |
| m01-l15 | «Las modificaciones de los créditos» | OEP 2020 (llamamiento extraordinario), P1 26 |
| m02-l02 | «Las cartas de servicios» | convocatoria 2025 (modelo A), P2 5 and reserva 5 |
| m02-l03 | «El Sistema de Archivos» (note on the `##`, covering both its `###`) | convocatoria 2024 (llamamiento extraordinario), P2 4; convocatoria 2022, P2 6 |

The eleventh, I.15 «Los principios presupuestarios», is the `##` over two kept `###`; its own text (art. 134.2 CE)
maps to I.15 S2a, so it carries no note. Every cited stem was re-read by the coordinator; the notes and the changed
«Normativa» lines were checked blind (`c2/bloque-i/verify/r2b-scope.md`, `c2/bloque-ii/verify/r2b-scope.md`: 12 PASS).

### Gaps

None. Every programme sentence and element is covered by a section of its own lesson, except II.4 S2 «La información
administrativa», which m02-l02 covers whole («Los servicios de información administrativa», «Información general y
particular al ciudadano»); m02-l04 points there for art. 10 RD 208/1996 only.

### Noted, not acted on (no question asks what is missing)

From the auditors' reports: m00-l01 does not give the 1.700 plazas (R4.1 does not ask it); m01-l03 has no section on
treaties (arts. 93–96) or control of the Government (arts. 109–111); m01-l08 «Otros órganos administrativos» read as
art. 5 LRJSP and the territorial collegiate organs; m01-l09 no CCAA financing (arts. 156–158; no sentence names it);
m01-l04's heading names «Oficinas de Justicia», which the body never mentions; I.11 «Competencia», «Abstención y
recusación» and «Prescripción de infracciones y sanciones» rest on S1 naming the LRJSP whole; I.14 no art. 27 TREBEP
(personal laboral pay, OEP 2020 extr. R1 1); II.1 «Conceptos del RDL 1/2013» overlaps I.16 S3; ofimática items
outside the literal sentence each carry an exam question (`scope/m02.md`).

## Part B — coverage 2022–2025

The per-lesson coverage check ran in R2, per bloque (`c2/bloque-i/coverage/`, `c2/bloque-ii/coverage/`). Bloque I:
134 of 134 coverage questions covered. After the scope cuts: no coverage question's covering lines fall in a removed
section (the reports and the cut sections' key terms checked), so nothing regressed.

«Sin fuente oficial» facts, as the theory ledger has them (bloque II coverage questions still MISS: no admissible
official page states the fact):

| Tema | Questions | Why |
|---|---|---|
| II.5 | 2024-P2-15 (disipador), 2024X-P2-32 (FLOPS) | only vendor glossaries (dropped as inadmissible) |
| II.7 | 2025-R2-1, 2024-P2-20, 2024X-P2-40, 2024-P2-19, 2024X-P2-42, 2024-R2-3, 2022-P2-22 | only Microsoft Q&A / Community threads |
| II.8 | 2024-P2-27, 2024X-P2-13, 2022-P2-35, 2024X-P2-11, 2024X-P2-12 | Spanish-keyboard shortcuts with no Spanish-layout page; the rest only on Mac/web tabs or no page |
| II.9 | 2024-R2-4 | only the Mac page lists them |
| II.10 | 2025-P2-25, 2024X-P2-22, 2022-P2-45; 2025-P2-38 partly | not on any saved or found page |
| II.11 | 2024X-P2-25, 2022-P2-50 | the label is only on Outlook.com/web pages |

## Part C — currency

Norms (`r2b/currency/normativa.md`): all 78 BOE entries at their latest consolidation on 2026-11-06 (five are never
consolidated); the EU texts at their latest Cellar versions. Ley 34/2002's stored date corrected (2025-12-18 was the
API's metadata date; act.php says 23-01-2025 and the PDF is byte-identical). **RDL 31/2026**: not convalidated on
boe.es on 2026-11-06 (no later reference or «convalidación» in its análisis; no BOE resolution found); plazo about
04-12-2026. No cambio pendiente has passed and no «(desde …)» mark refers to a past date (pending: Reglamento del
Congreso, XVI legislatura; RDL 31/2026, 01-12-2026 and 01-01-2027; RD 707/2026, 02-01-2027).

Saved pages (`r2b/currency/pages.md`, `pages-live*/`): `check_pages.py --course age-auxiliar-c2` over all 325
entries, support.microsoft.com through the e2e Playwright Chromium on a 403, re-tried at 20 s and 60 s. 312 same text,
10 changed (23 places in lessons and glossary rest on them, all PASS blind), 3 not read by the tool: the V Plan page
(same text at its recorded `url_actual`), the CE análisis (API header; adds Declaración 1/2026, the only C2 place
citing it, m02-l01, unaffected) and `consilium-presidencia.html` (403 throughout). `fuentes.yaml` carries each
result in `comprobacion`. Pages are now compared after stripping both copies (ledger, «Saved pages stripped»).
Extractor limit found: elements whose id contains «copilot» are skipped, so Copilot pages' tab panels are outside
the text compared (checked by hand for the one place that needs them).

## Closing checks

All on the final tree (2026-11-06), with `docs/age-verification/c2/tools/close_round.sh` (new this round: the
ledger's closing checks as one script).

- **Blind checks of every edit:** R2b notes and Normativa lines 12/12 PASS; changed pages 23/23 PASS; esquemas and
  their fixes in the theory ledger (R2c). `test_provenance.py` 41 pass (every C2 lesson and the glossary).
- **Goldens** regenerated and read: `citations.es.txt` 2,699 → 2,682 prose citations (the 17 gone are the removed
  sections' and the I.1 «Otras fuentes» line), 0 → 266 esquema rows, 119 → 118 Normativa norms, 6 → 5 «naming a norm
  normativa.yaml lacks»; `glossary-links.es.txt` 169 → 168 web marks (`g-credito-presupuestario` and
  `g-separacion-del-servicio` lost their m01-l13 marks with the cuts, the second still marked in m01-l08;
  `g-suspension-provisional` gains one in m01-l13; `g-silencio-administrativo` moves within m01-l11);
  `g-credito-presupuestario` stays (single lesson, its definition cites art. 35.1 LGP). `lesson-refs.es.txt`
  unchanged.
- **crypto-futures:** unchanged. **C1:** only the stripped saved pages (226 and `fuentes.yaml`) and the per-file
  digests of `excerpts.json` (no question's excerpt changed), by Juanjo's instruction of this round.
- **Android bundle** re-exported to a scratch folder: byte-identical to `dist/bundle`.
- **Full suites:** backend `uv run pytest` 2,194 passed, 23 skipped; frontend `npx vitest run` 715 passed, 81
  skipped; `tsc -b` clean. `ruff`, `ruff format`, `mypy` clean on every Python file touched.

### Re-close after the prose-gap fixes (2026-11-06)

m01-l04 (art. 630.1 LOPJ three-fifths sentences and rows restored from C1; «la LOPJ» for «la ley») and m01-l16
(«(hoy: …)» gloss, art. 20.2 RD 829/2023; esquema row restored): blind checks PASS
(`c2/bloque-i/verify/prose-gaps-2026-11-06.md`, `prose-gaps-recheck-2026-11-06.md`), records redone,
`close_round.sh` rerun: citations golden +6 lines, all from these two fixes (3 prose and 3 esquema citations);
crypto-futures unchanged, C1 as above; Android bundle byte-identical; backend 2,194 passed / 23 skipped; frontend
715 / 81; `tsc -b` clean. The «copilot» extractor bug goes to platform delta L7.
