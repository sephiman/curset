# Lesson fixes m02: blind check (session 5, 2026-10-23)

Checked against `lesson-fixes/m02/writer.md`, judged from `git diff HEAD -- <lesson>` and from the norms read with
`pdftotext -layout` (files named in `sources/normativa.yaml`; none of the articles used has `cambios_pendientes`).
Hunks recorded in `bloque-ii/prose-gaps/writer.md` (m02-l01 art. 2.1 and LO 4/2001 arts. 9–10 with their esquema;
m02-l03 art. 6.1 RD 203/2021, arts. 12.3–13.6 RD 1112/2018 with their esquema, art. 6 RD 127/2015, the `fuente:`
rewrites) were left out. Resolver: `CourseCitations.build(...)._anchor(lesson, citation, 'es')` from `backend/`
(script `lesson-fixes-check-m02/anchors.py` in the scratchpad), and each new prose citation was also read back from
`scan_lesson`'s items with its norm and anchor.

## Done items

| # | Item | Lesson, lines | Faithful | Cited | Placed and scoped | Voice | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | Art. 3.2 RD 208/1996, «(hoy: …)» for LO 5/1992 and art. 37 Ley 30/1992 | m02-l01, 208–214; Normativa 390–393 | PASS | PASS | PASS | PASS | PASS | The RD's words are kept as written: «con las limitaciones y en los términos establecidos en la Ley Orgánica 5/1992, de 29 de octubre, … y en el artículo 37 de la Ley 30/1992, de 26 de noviembre». The LOPDGDD preamble states «La Ley Orgánica 5/1992 fue reemplazada por la Ley Orgánica 15/1999», its DDU.1 repeals LO 15/1999, and art. 1 names the Reglamento (UE) 2016/679 and «esta ley orgánica»; LPAC DDU.2.a) repeals Ley 30/1992 and art. 13.d) gives the right «al acceso a la información pública, archivos y registros». Citations resolve: `boe-a-1996-4997-art-3`, `boe-a-2018-16673-art-1`, `boe-a-2015-10565-art-13`. Long sentence, but it is the RD's own clause plus two short notes. |
| 2 | Art. 17.2 RD 951/2005, «Ministerio de Administraciones Públicas» (hoy: Política Territorial y Memoria Democrática) | m02-l01, 285–288; Normativa 390–391 | PASS | PASS | PASS | PASS | PASS | Art. 17.2: «corresponderá a la Inspección General de Servicios del Ministerio de Administraciones Públicas», quoted as written. Art. 12.1 RD 829/2023: MPTMD has «organización territorial del Estado», which covers the servicios periféricos integrados en las Delegaciones y Subdelegaciones; this matches the ledger's I.8 decision. Resolves to `boe-a-2005-14836-art-17` and `boe-a-2023-23537-art-12`. Watch point, not a fail: no file in `sources/` names the Inspección General de Servicios that does this today (RD 1009/2023 art. 11 lists only the MPTMD's directive organs). |
| 4 | STC 100/2019 on arts. 12–13 RD 1112/2018 | m02-l03, 161–163 | PASS | PASS | PASS | PASS | PASS | BOE notes in the consolidated RD: under art. 12, «se declara que los apartados 1, 3, 4 y 6 invaden las competencias autonómicas y carecen de carácter de legislación básica, por Sentencia del TC 100/2019, de 18 de julio»; under art. 13, «el inciso destacado del apartado 1 y los apartados 2 a 6». `pdftohtml -xml` shows the bold inciso as `<b>de veinte días hábiles</b>` in 13.1 párr. 2. Nothing wider than the note. The sentence comes right after the 12.3–13.6 plazos it qualifies. Resolves to `boe-a-2018-12699-art-12` and `-art-13`. |
| 5 | Art. 18.1 RD 1112/2018, «Ministerio de Política Territorial y Función Pública» (hoy: Transformación Digital y Función Pública) | m02-l03, 175–177 | PASS | PASS | PASS | PASS | PASS | Art. 18.1: «El órgano encargado de realizar el seguimiento y presentación de informes ante la Comisión Europea es el Ministerio de Política Territorial y Función Pública.» Art. 22.2 RD 829/2023: «administración pública, función pública, y gobernanza pública», the same ministry as the lesson's other notes (l. 117–119, 310). Resolves to `boe-a-2018-12699-art-18` and `boe-a-2023-23537-art-22`. |

## Not done items

| # | Item | Reason given | Reason true? | Note |
|---|---|---|---|---|
| 3 | Art. 9.1 RD 208/1996, «Gobiernos Civiles» (m02-l01, 166–168) | No file in `sources/` names the successor | Yes | I converted every PDF in `sources/normativa/` to text and searched it. «Gobiernos/Gobernadores Civiles» appears only as an old name: art. 9.1 RD 208/1996 and the other files the record lists. No file pairs it with «Subdelegaciones» or a «se entenderán» clause. LOFAGE (Ley 6/1997) is not in `sources/` (`normativa.yaml` names it only as derogated by the LRJSP). The record is also right that the words are in art. 9.1 RD 208/1996, not in LO 4/2001. |
| 6 | DUE and the cese trámites (DA 3.ª.1.d) TRLSC) | TRLSC not in `sources/` | Yes | `normativa.yaml` has no RDL 1/2010 and no `BOE-A-2010-10544` file. The DA 3.ª text exists only in Ley 14/2013 DF 6.ª, which is the 2013 amending text, not the TRLSC as consolidated today. RD 127/2015 has «Facilitar la tramitación del cese de la actividad» (art. 4.1.g), which the lesson already states, but nothing that ties the DUE to the cese. |

## Record errors (no lesson effect)

- Item 1 says «DA 3.ª Ley 4/2026 on RDL 1/2013». The DA 3.ª in `BOE-A-2026-20528` is about references in **Ley 39/2006** («Las referencias que se efectúan en la Ley 39/2006, de 14 de diciembre, …»). The mapping it gives (LO 15/1999 → RGPD and LO 3/2018; Ley 30/1992 → Ley 39/2015) is the same, so the finding stands.
- The summary's «Done: 5 items» should read 4 items (1, 2, 4 and 5), which together make 5 additions.

## Counts

Done items checked: 4. PASS: 4. FAIL: 0. Not-done reasons checked: 2, both true.
