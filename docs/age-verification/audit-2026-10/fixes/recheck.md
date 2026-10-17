# R2b fixes — closing blind re-check (recheck-queue.md, 17 rows)

Verifier, 2026-10-17. Checked: each row of `recheck-queue.md` against the file as it stands (`git diff` against HEAD
where useful), the replacement text in the origin report (`verify-m01.md`, `verify-m02.md`, `verify-m03-l03.md`,
`verify-m04-a.md`, `verify-m04-b.md`, `verify-m05-b.md`; bloque VI `coverage/recheck.md` F1), and the cited sources read
with `pdftotext -layout`: LPAC art. 53.1.a); INCIBE glossary 2.1.30; TUE art. 19.3 and Protocolo n.º 3 art. 50 ter;
TFUE art. 256.3; LRJSP art. 93.2; Código Civil art. 918; Resolución de 20-01-2014 anexo IV art. 23 (concepto 233) and
Orden HAC/557/2026 anexo II (artículo 23, conceptos 230–233); RLGS art. 56 and LGS art. 34; RD 364/1995 arts. 25, 47.1,
50.1 and 50.5; TREBEP arts. 30 and 89.3; RD 365/1995 art. 17; RD 829/2023 art. 22.2–3; RD 1009/2023 art. 21.C); ET
art. 68.e); IV Convenio único art. 86.1.d). Form: prose and Normativa lines ≤ 120 in every touched block (long lines
left in these lessons are the title line, tables, «Lo que más cae» items and pre-existing lines outside the edits);
«Lo que más cae» ≤ 10 items in every touched lesson; `docs/prose-voice.md` «never does» list.

| # | Lesson | PASS/FAIL | Reason | Replacement (for FAIL) |
|---|---|---|---|---|
| 1 | m02-l03 | PASS | Paragraph is the verifier's wording word for word, wrapped ≤ 120. Art. 53.1.a), párr. 2 refers to the list of párr. 1, which carries «en caso de que la Administración no dicte ni notifique resolución expresa en plazo», the órgano «para su instrucción, en su caso, y resolución» and the actos de trámite, all as written. Normativa LPAC line has 53.1.a). | — |
| 2 | m02-l03 | PASS | Sentence present as asked, after the certificado sentence. INCIBE 2.1.30 prints «La Autoridad de Certificación (AC o CA, por sus siglas en inglés, Certification Authority)». Wrap ≤ 120 (the path cannot join the previous line). Normativa «Otras fuentes» names `incibe-glosario-ciberseguridad.pdf`, consulted 17-10-2026 as in `fuentes.yaml`, whose entry lists m02-l03. | — |
| 3 | m06-l03 | PASS | Line 124 reads `  (fuente: \`ms-win-directivas-explorador.html\`).`, joined as F1 asked; no stray line. The item (lines 122–124: Mayús+Supr; directiva «No mover archivos eliminados a la papelera de reciclaje» habilitada, scoped to the Explorador) is intact and its two sources are cited. Block has 10 items. | — |
| 4 | m01-l11 | PASS | «Los recursos», first paragraph, is the verifier's replacement word for word (only the line breaks differ, all ≤ 120). Checked: art. 19.3 TUE a) and b); art. 256.3 TFUE párr. 1 verbatim; art. 50 ter: «una o varias», letters a)–f), the second-paragraph exception (Derecho primario, Derecho internacional público, principios generales, Carta) and the transfer «tras verificar … exclusivamente». Present tense. Normativa TUE line has Protocolo n.º 3, art. 50 ter; TFUE line has 256. | — |
| 5 | glossary | PASS | `g-competencia-exclusiva` has no `link_except` (diff against HEAD removes exactly `link_except: [m01-l06]`); its two senses (m01-l09, m01-l11) are unchanged. `grep -i` finds no «competencia(s) exclusiva(s)» in m01-l06.md. | — |
| 6 | m03-l03 | PASS | `### Organismos públicos` follows the consorcios paragraph and precedes «## Procedimiento administrativo común…»; the three lines are unchanged and appear only there (no copy left in «Convenios», which now ends on art. 123.2). Text is art. 93.2 LRJSP verbatim. Normativa LRJSP line has 93.2. | — |
| 7 | normativa.yaml | PASS | Código Civil entry: `temas: ["III.1", "III.3"]`; note is the verifier's text word for word («Título preliminar (arts. 1-7 …), para III.1; art. 918 (cómputo de grados de parentesco), para III.3.»). III.3 is m03-l03 (as in the LO 1/2025 and other III.3 entries). The amended_2025_2026 LO 1/2025 articles (51–73) do not include 918. | — |
| 8 | m05-l04 | PASS | «Esas asistencias son las del artículo 1.1.d) RD 462/2002.» is gone; the paragraph ends on «(anexo IV, art. 23, concepto 233, Resolución de 20-01-2014).», rewrapped ≤ 120. Concepto 233 text matches the Resolución («entre otros gastos», órganos colegiados y consejos de administración, tribunales, centros de formación y perfeccionamiento). Codes 230–233 match anexo II Orden HAC/557/2026. Normativa unchanged: RD 462/2002 art. 1.1 still cited (line 64). | — |
| 9 | m05-l06 | PASS | The three RLGS blocks now follow the art. 34.4 LGS paragraph and precede «### Documentos contables de las subvenciones»; LGS art. 34.1–4 reads as one run. Content checked against art. 56.1 a)–b), 56.2 first sentence and 56.3. Normativa RD 887/2006 line «arts. 56.1–3 … y 70.3» in step. | — |
| 10 | m03-l03 | PASS | Normativa line reads «- Código Civil: art. 918 (cómputo de grados de parentesco).»; no line now ends on a bare «número.». Art. 918 is the grade count the lesson uses (line 85, LQMC line). | — |
| 11 | m04-l05 | PASS | Remoción paragraph is the verifier's rewrap line for line (all ≤ 120). Checked against art. 50.1 (both causes; 42.3/74.2 bar; imputable), art. 50.5 (mismo municipio, dos niveles, efectos del día siguiente al cese, Ministerio para las Administraciones Públicas) and RD 829/2023 art. 22.2 (función pública). | — |
| 12 | m04-l05 | PASS | Block has 10 items: art. 47.1 line restored as worded in HEAD (matches art. 47.1); art. 64.3 line gone from the block and still in the text (table, line 119); art. 30 line is the verifier's wording word for word (deducción proporcional, sin carácter sancionador, sin perjuicio de la sanción disciplinaria; no devenga ni percibe; no es sanción ni afecta a prestaciones sociales), matching TREBEP art. 30.1–2. It sits in the 47.1 line's old slot (second), one of the two places the verifier allowed. | — |
| 13 | m04-l08 | PASS | Crédito horario block (art. 68.e) paragraph, table, art. 86.1.d) sentence) is now at the end of «### Derechos y deberes», after art. 5 ET's f), before «### Jornada y horas extraordinarias»; «Sus deberes básicos» follows art. 4.1 again. Scale and «a salvo de lo que dispongan los convenios colectivos» match ET art. 68 and 68.e); Convenio art. 86.1.d) has the same five steps. Normativa ET has 68.e), Convenio has 86.1.d). | — |
| 14 | m04-l03 | PASS | The art. 25.1 paragraph is byte-identical to HEAD and to the verifier's text; the only «(hoy: …)» note in the lesson is at art. 27.1 (line 55). Art. 25.1–2 RD 364/1995 checked. | — |
| 15 | m04-l03 | PASS | Paragraph is the verifier's wording word for word. RD 829/2023 art. 22.3.c) (Secretaría de Estado de Función Pública, órgano superior) and RD 1009/2023 art. 21.C) (DG de Función Pública con rango de subsecretaría, DG de Gobernanza Pública, Oficina de Conflictos de Intereses con rango de Dirección General) match. Normativa lists RD 829/2023 art. 22.3.c) and RD 1009/2023 art. 21.C). | — |
| 16 | m04-l03 | PASS | TREBEP Normativa line is the verifier's three lines exactly, all ≤ 120. 75.2 is gone and no longer cited in the lesson; nor is Ley 30/1984 (its intro mention went with the section). | — |
| 17 | m04-l04 | PASS | Agrupación familiar paragraph is the verifier's reflow word for word, all lines ≤ 120, no short mid-paragraph line. Checked against TREBEP art. 89.3 (both paragraphs) and RD 365/1995 art. 17.1–2 (dos a quince años; reingreso o interés particular de oficio). | — |

## Counts

17 rows checked: **17 PASS, 0 FAIL**.

Note on row 12 (not a FAIL): the «Lo que más cae» block of m04-l05 groups RD 364/1995 lines before TREBEP lines; the
art. 30 TREBEP line now sits between arts. 41.2 and 47.1 RD 364/1995. The verifier allowed that slot, so it stands.

## Rows 18–20

Sources: `glossary.yaml` (diff against HEAD), m01-l01, m04-l05, m06-l02; `sources/otros/ms-win-idioma.html`
(page text, «voz»); RD 364/1995 (BOE-A-1995-8729, consolidated) art. 54.1 and RD 829/2023 (BOE-A-2023-23537) art. 22
(`pdftotext -layout`); `docs/age-theory-ledger.md` «Decisions applied after bloque I», item 1; `docs/prose-voice.md`.

| # | PASS/FAIL | Reason | Replacement |
|---|---|---|---|
| 18 | PASS | Diff adds only `m01-l01` to g-convenio's `link_except` and `m04-l05` to g-servicios-comunes's. m01-l01 has one «convenio» (line 31, «tratados o convenios» of art. 94.1.e CE): international treaties, not the art. 47.1 LRJSP agreement of the definition. m04-l05 has one «servicios comunes» (line 72, «Entidades Gestoras y Servicios Comunes de la Seguridad Social», art. 51.2 RD 364/1995): the Social Security body, not a Ministry's servicios comunes under the Subsecretario (arts. 63.1, 68.1 LRJSP). No other use of either term in those lessons, so no link in the entry's own sense is lost. | — |
| 19 | PASS | The added sentence «Para instalar la voz de un idioma, ese idioma debe estar establecido como idioma para mostrar» restates the page's «Instalar la voz de un idioma» section: «Asegúrese de que el idioma en el que se va a usar la voz está establecido como idioma para mostrar» (both the Windows 11 and Windows 10 versions). No coined term; the item still cites `ms-win-idioma.html`; lines ≤ 120; nothing from the «never does» list. | — |
| 20 | PASS | Art. 54.1 RD 364/1995 reads «previa autorización del Secretario de Estado para la Administración Pública», quoted as written. Art. 22.3.c) RD 829/2023 lists «La Secretaría de Estado de Función Pública» as an órgano superior of the Ministerio para la Transformación Digital y de la Función Pública (22.2: función pública). This is the lesson's first mention of the old organ (line 11 names the current Secretaría; line 62 is the RD 829/2023 title); the later «Secretaría de Estado para la Administración Pública» at art. 48.2 (line 103) has no note, as item 1 requires (once, at first mention). The short «RD 829/2023» follows its full title at line 62. Lines 76–82 are ≤ 120 (max 120). Normativa: «RD 829/2023 (departamentos ministeriales): arts. 22.2 y 22.3.c).», and the RD 364/1995 line keeps 54.1. | — |

3 rows checked: **3 PASS, 0 FAIL**.
