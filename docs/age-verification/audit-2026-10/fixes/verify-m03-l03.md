# R2b blind verification — m03-l03 (bloque III, tema III.3)

Verifier: blind, 2026-10-17. Spec: `spec.md` («Verifier (blind)»). Changes checked: m03-l03 items 1–15 of `fix-m03.md`
(m03-l01, m03-l04 and m03-l05 belong to another verifier). Lesson read as it stands:
`content/age-administrativo-c1/es/lessons/m03-l03.md`. Sources opened directly with `pdftotext -layout`:
`BOE-A-2015-10565_lpac_2024-11-06.pdf` (arts. 14, 16.4, 17.2, 63.1, 66.1, 85, 88.1), `BOE-A-2015-10566_lrjsp_2024-08-02.pdf`
(arts. 14, 30.1, 51, 53.1, 93.2, 123), `BOE-A-1889-4763_codigo-civil_2025-01-03.pdf` (art. 918),
`BOE-A-2023-23537_rd-829-2023-departamentos_2023-12-29.pdf` (arts. 5, 22). Questions opened in `SP/exams/`:
conv2024_X P1 res. 3, S I 7, S I res. 2, S II 12; conv2025_X S I 17, S I res. 5, S II 7, S II 19, S II res. 5; conv2025_A
S II 14; conv2022 S II 2, S II 18; conv2022_X P1 29, S I res. 3; conv2020 S II 1, S II 5; conv2020_X S II 6.
Form checked against `docs/prose-voice.md` and the spec's R2 rules.

| # | Lesson | Change | PASS/FAIL | Reason | Replacement (for FAIL) |
|---|---|---|---|---|---|
| 1 | m03-l03 | coverage: art. 14.1 and 14.2.d)–e) LPAC in «Interesados y representación» | PASS | Both apartados match the file (14.1 shortened without loss; d) and e) verbatim, «entre otros» renders «al menos»). conv2024_X S I res. 2 (representative of a non-obliged person) and S II 12 (employee; option b quotes 14.1) now answered. Old pointer kept as «La lista completa está en m02-l03»; m02-l03 line 23 has art. 14.2. Wrap ≤ 120; «y e) LPAC)» at line start is not a list marker. | — |
| 2 | m03-l03 | coverage: new «### Registros y archivo», arts. 16.4 (last párrafo) and 17.2 LPAC | PASS | Verbatim; the interoperability paragraph is the closing párrafo of apartado 4 (apartado 5 follows it). conv2025_X S I res. 5 (option c, «transmisión telemática de los asientos registrales») and conv2024_X P1 res. 3 (option c quotes 17.2) answered. Heading words are the titles of arts. 16 and 17. | — |
| 3 | m03-l03 | coverage + restore: art. 14.1–14.2 LRJSP in «Competencia» | PASS | Matches the file; «Asimismo» → «También» is a faithful rendering. conv2022 S II 2 option a («decline su competencia y remita las actuaciones») answered. | — |
| 4 | m03-l03 | coverage: art. 918 CC paragraph after the 23.2 list | PASS | Art. 918 párr. tercero: dos / tres / cuatro grados as written; «tío, hermano de su padre o madre» shortened to «tío» without changing a number. conv2025_X S I 17 and conv2022_X S I res. 3 (cousin, fourth degree, option a) now fully answered. | — |
| 5 | m03-l03 | coverage + restore: new «### Potestad sancionadora», art. 30.1 LRJSP | PASS | Verbatim (tres años / dos años / seis meses; tres años / dos años / al año). Answers conv2022_X S II 5 and the restore rows conv2020 S II 1 and conv2020_X S II 6 (both ask the no-ley prescription). Pointer to m03-l05 is valid (its «### Principios de la potestad sancionadora»). | — |
| 6 | m03-l03 | coverage: art. 51.1–51.2 LRJSP and list a)–e) in «Convenios» | PASS | Every cause and the c) mechanism (requerimiento, comunicación al responsable del mecanismo de seguimiento, persistence → resolución, indemnización si se hubiera previsto) are in the file. conv2025_A S II 14 (unilateral AGE decision is not a cause) answered. List markers start lines only. | — |
| 7 | m03-l03 | coverage + restore: art. 53.1 LRJSP | PASS | Tres meses, 600.000 euros, remisión electrónica, Tribunal de Cuentas u órgano externo autonómico: as in the file. conv2025_X S II 19 option a answered. | — |
| 8 | m03-l03 | coverage: art. 93.2 LRJSP sentence placed in «Convenios» | FAIL | Text is verbatim and answers conv2025_X S II 7 (option a quotes it). But the statutes of organismos públicos are not a convenio: the spec puts a missing fact «in the section where it belongs», and the writer opened its own subsection for art. 30.1 in the same lesson. On the missing «(hoy: …)»: no FAIL, see the section below. | Delete lines 129–131 from «Convenios» and add, after the consortia paragraph (end of «Convenios», before «## Procedimiento administrativo común…»): the heading «### Organismos públicos», a blank line, then the same three lines unchanged: «Los estatutos de los organismos públicos se aprobarán por Real Decreto del Consejo de Ministros a propuesta conjunta del Ministerio de Hacienda y Administraciones Públicas y del Ministerio al que el organismo esté vinculado o sea dependiente (art. 93.2 LRJSP).» The heading is the LRJSP's own term (título II, capítulo III). |
| 9 | m03-l03 | coverage: art. 123.1–123.2.a)–b) LRJSP (consortia) | PASS | Matches the file: creación autorizada por ley, autorización previa del Consejo de Ministros, competencia indelegable del titular del departamento ministerial; organismos autónomos with informe previo. conv2025_X S II res. 5 option d answered. Placement in «Convenios» holds: the sentence is about the convenio de creación. | — |
| 10 | m03-l03 | coverage + restore: art. 63.1 LPAC in «Iniciación» | PASS | Verbatim. conv2022_X P1 29 option b («Siempre de oficio, por acuerdo del órgano competente») answered; also backs conv2022_X S II 4. | — |
| 11 | m03-l03 | coverage + restore: art. 66.1.b) LPAC | PASS | Verbatim content of letra b) first sentence. conv2024_X S I 7 option c answered. | — |
| 12 | m03-l03 | restore: art. 85.1–85.3 LPAC in «Terminación» | PASS | 85.1, 85.2 (pecuniaria / no pecuniaria justificada, pago voluntario anterior a la resolución, salvo reposición e indemnización) and 85.3 (al menos 20 %, acumulables, en la notificación de iniciación, condicionada al desistimiento o renuncia, incremento reglamentario) all in the file. conv2020 S II 5 (pago voluntario) found. | — |
| 13 | m03-l03 | coverage + restore: art. 88.1 LPAC | PASS | Both párrafos; «plazo no superior a quince días» as in the file. conv2022 S II 18 options all turn on cuestiones conexas; the lesson states the norm, not the disputed key. | — |
| 14 | m03-l03 | «Lo que más cae»: 23.2.b) line rewritten; lesividad line replaced by 30.1 | PASS | Ten lines. Both new lines rest on the body (art. 918 CC; art. 30.1 LRJSP, three questions). The dropped lesividad fact stays in the body (line 296, art. 107.2 LPAC), and no coverage row quoted the dropped line. | — |
| 15 | m03-l03 | Normativa: LPAC, LRJSP lines extended; «Código Civil: art. 918.» added | PASS | Every newly cited article is in its line (14.1–14.2, 16.4, 17.2, 63.1, 66.1, 82–85, 88.1; 14.1–14.2, 30.1, 51, 53.1, 93.2, 123.1–123.2; CC 918). Nothing lost its last citation (107.2 still cited at line 297). | — |
| 15a | — | `normativa.yaml`, Código Civil entry (writer: «No `normativa.yaml` entry needed») | FAIL | The existing entry says `temas: ["III.1"]` and note «Solo el título preliminar (arts. 1-7 …), para III.1.» The lesson now cites art. 918 for III.3, so the entry is out of step. Coordinator edit (the writer may not touch the file). | In the «Código Civil» entry: `temas: ["III.1", "III.3"]`; note: «Título preliminar (arts. 1-7: fuentes, jerarquía, aplicación de las normas), para III.1; art. 918 (cómputo de grados de parentesco), para III.3.» |

## Art. 93.2 LRJSP without «(hoy: …)»

Convention 1 (`docs/age-theory-ledger.md`, «Decisions applied after bloque I») asks for «(hoy: <current name>)» after
the first mention of an old ministry name in a lesson, «as the exam ledger does», naming «the department whose RD
829/2023 competences cover the function the law gives in that sentence». This is the first mention of «Ministerio de
Hacienda y Administraciones Públicas» in m03-l03, so the convention applies unless no department clearly matches.

- The function is the joint proposal of organismos públicos' statutes, which art. 93.1 LRJSP fills with structure and
  competences (b) and with patrimonio, presupuesto, recursos humanos and contratación (c, d). RD 829/2023 splits the old
  ministry: art. 5.1 gives Hacienda «hacienda pública, de presupuestos y de gastos»; art. 22.2 gives Transformación
  Digital y Función Pública «administración pública, función pública». Neither article names the statutes, so a
  single «hoy» name is not supported by a source.
- The ledger already accepts quoting without «hoy» when the match is unclear: bloque II, «Ministerio de Administraciones
  Públicas» (art. 17.2 RD 951/2005, Política Territorial vs Función Pública), and the «Ministerio de Justicia» note
  removed at art. 32.8 LRJSP.
- The exam ledger, which the convention points to, marks conv2025_X S II 7 `vigente` with no «Denominación actual»
  note, and the question's key option quotes the law's name as written. The distractors b and c name «Ministerio de
  Hacienda», so a one-ministry «hoy» would also blur the key.

Verdict: the convention does not require a note here; no replacement. One correction to the writer's rationale: m01-l08
at art. 59.1–2 is not the same treatment. Those are later mentions after the lesson's first «(hoy: Ministerio para la
Transformación Digital y de la Función Pública)» at art. 54.2. III.4 omitted the name instead of quoting it. The
apt precedent is the RD 951/2005 case above.

## Covered rows re-checked

The diff removes only the old pointer sentence after art. 5.6, two «Lo que más cae» lines and the old Normativa lines.
Every row the coverage report marked covered still finds its quote in the lesson. The 107.2 rows (conv2025_A S I 3–4)
quote the body, which is unchanged. The two partial rows quoted the old 23.2.b) line, and the new line still states
the rule.

## Side notes (no verdict)

- `lesson-refs.es.txt` is generated: the m03-l03 → m02-l03 snippet changed and m03-l03 → m03-l05 is new. Regenerate
  with `lib/refs/report.test.ts`.
- The new pointer «Los principios de la potestad sancionadora están en m03-l05.» lacks the «, el tema de …» tail the
  lesson's other two pointers carry. Optional, not a rule.

## Counts

- Checked: 16 rows (items 1–15 plus 15a).
- PASS: 14.
- FAIL: 2 (#8 placement; #15a `normativa.yaml` Código Civil entry).
- «(hoy: …)» at art. 93.2: no note required.
- Covered rows lost: 0.
