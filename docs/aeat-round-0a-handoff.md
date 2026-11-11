# Handoff — aeat-agentes-hacienda, round R0a (2026-11-11)

Nothing committed. Nothing under `es/`, `glossary/`, `exercises/`; no `course.yaml`. Working data and scripts: `docs/age-verification/aeat/r0a/` (README; per-file URL, date and sha256 in `sources-manifest.tsv`).

**Counts.**
- Sources: 6 BOE convocatorias (OEP 2020–2025) and 68 AEAT files, all by plain fetch from `sede.agenciatributaria.gob.es/Sede/trabajar-agencia-tributaria/convocatorias-ofertas-empleo-publico-<año>/…-agentes-libre.html` (OEP 2020: `cuerpo-general-administrativo-turno-libre.html`); no page refused. The sede has no Agentes pages before OEP 2020.
- First exercise: 13 questionnaires (OEP 2020–2025, tipos A and B) plus the 2022 extraordinario; 680 distinct questions. Each has 100 questions (80 in 2025), every key sheet pairs with its questionnaire, and tipo B keys name the same option text as tipo A.
- Ledger: 629 vigente, 7 vigente-con-nota, 11 anulada, 5 norma modificada, 28 fuera de temario, 0 dudosa.
- `normativa.yaml`: 86 entries (77 BOE, 9 EU); 53 files copied from C2/C1 with the same sha256 (asserted), 41 fresh; all 32 temas covered.
- `programa.md`: 91 paragraphs, all verbatim by script.

**Exam rules (BOE-A-2025-27056, base 6.2, acceso libre).**
- First exercise: «80 preguntas», four options, one correct, a wrong answer costs «un cuarto», «una hora y media», marked 0–10 with 5 to pass. Criteria: raw score A − E/4; pass mark the best 1.416 (general) / 147 (discapacidad), never below 50 %. 2025 cut-off: 41,00 of 80 general; 32,00 (40 %) discapacidad.
- Second exercise: «diez supuestos prácticos» on the Materias específicas (III.1–III.20), «dos horas y treinta minutos», 0–30 with 15 to pass, answers «breves y razonadas». Both exercises are eliminatory; ties go to the second exercise first.
- Programme: **32 temas** (I 7 + II 5 + III 20). The 2024 convocatoria had 34 temas, 100 questions and 1 h 40, which is where the public summaries' other figures come from.
- Promoción interna: no reduced programme. Both of its exercises cover only the 20 specific temas: 50 questions in 1 h, apto/no apto; forma «A» exempt.

**Could not be obtained.**
- Second-exercise answer sheets exist only for OEP 2023 (the test part); the other papers are written exercises.
- Exam dates of the 2023 and 2024 second-exercise extraordinarios: not published. Those files carry no date prefix.
- The 2022X definitive answer sheet is not online. The provisional is used: the Tribunal's resolution says it became definitive «sin modificación alguna».
- No raw cut-off for the second exercise has been published in any year.

**Unverified norms.**
- Interés de demora 4,0625 %, interés legal 3,25 % and IPREM 600 €/mes are taken from Ley 31/2022 (PGE 2023, prorrogued; there is no PGE for 2024–2026). They have not been checked against the AEAT sede.
- RIRPF art. 67 and RGAT art. 49 depend on an order approving the models (RD 117/2024); that order has not been looked up.
- RDL 29/2026 has not been convalidated. It sets LIRPF arts. 24 and 85.1 (scale 1,1–3 % from 2027), the imputación at 1,1 % for 2026, LIVA art. 91 and TRLRHL art. 107.4. RDL 26/2026, with the same content, was derogated by Congress on 02-10-2026. RDL 31, 33, 35 and 36/2026 are also unconvalidated.
- The LIVA consolidated PDF already prints the RDL 29/2026 wording with no warning, so the wording in force until 01-12-2026 is not in the file.
- Estimación objetiva limits for 2026 are 150.000 € (LIRPF art. 31, LIVA arts. 122 and 124). The extensions to 250.000 € (RDL 9/2024, 16/2025, 2/2026) were all derogated.

**Classification doubts.**
- Every exam is classified against the 2025 programme; dropped topics are `fuera de temario` (IRNR, IIEE, contrabando, retenciones, declaraciones informativas, consulta tributaria, delito fiscal, IVA tipos).
- 50 questions keep a 2025 tema with «cobertura discutible» in the note. Most are on NIF, censos, libros, SII, retenciones-as-pagos a cuenta and customs regimes.
- Per-tema totals use OEP 2022–2025 (R4.6); 2020–2021 are outside the totals.
- 2025-53 (LIRPF 85.1) is `norma modificada` only through the unconvalidated RDL 29/2026; the override says so.
- 2023 tipo B printed A-42 twice and left out A-30; both were annulled. The 2022 resolution says «80» for the annulled A-82.

**Decisions for Juanjo.**
- Keep or drop the two EU customs XHTML files in `sources/normativa/` (29 MB and 37 MB; Cellar has no Spanish PDF of the consolidated Reglamentos 2015/2446 and 2015/2447).
- C1 and C2 are now behind boe.es for Ley 39/2006 (RDL 36/2026) and LGSS (RDL 35/2026). They are read-only here; their currency audit should pick these up.
