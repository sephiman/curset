# R2b fixes — bloque IV, share B (m04-l03, m04-l04, m04-l07, m04-l09): blind verification

Verifier, 2026-10-17, to the «Verifier (blind)» section of `spec.md` (this folder). Share: changes 1–4, 14–16 and 21
of `fix-m04.md`. m04-l05 and m04-l08 belong to the other verifier. What was checked:

- The lessons as they stand, against HEAD with `git diff`.
- The source articles, read by the verifier with `pdftotext -layout` from `content/age-administrativo-c1/sources/normativa/`:
  - RD 364/1995 arts. 25.1–2 and 27.1;
  - RD 829/2023 art. 22.1–3;
  - RD 1009/2023 art. 21;
  - TREBEP arts. 89.1 and 89.3;
  - RD 365/1995 art. 17;
  - RDL 4/2000, preámbulo and disposición derogatoria única a).1;
  - Ley 29/1975 (`BOE-A-1975-13887_…pdf`), preámbulo apartado cinco, arts. primero to cuarto and diez;
  - IV Convenio único art. 70.
- The questionnaires and keys in `SP/exams/`:
  - conv2025 modelo A, Supuesto I, reserva 3 («La Secretaria de Estado de Función Pública», key b);
  - conv2022 extraordinario Sup. II 9 (key b) and P1 33 (key c);
  - conv2022 P1 32 (b, 1975).
- The coverage reports `coverage/m04-l03.md`, `m04-l04.md`, `m04-l07.md` and `m04-l09.md`, and `scope/m04.md`.
- The standing convention in `docs/age-theory-ledger.md`, «Decisions applied after bloque I», item 1. The bloque I
  cross-cutting note says the «(hoy: …)» is added «once».
- `docs/prose-voice.md`.

| # | Lesson | Change | PASS/FAIL | Reason | Replacement (for FAIL) |
|---|---|---|---|---|---|
| 1 | m04-l03 | removal, «Cuerpos y escalas» | FAIL (form only) | The heading and both paragraphs are gone. «## El personal funcionario…» now opens on «### Grupos de clasificación». The section alone cited three things: art. 75.2 TREBEP, art. 26 Ley 30/1984 with its BOE note, and art. 22.2 RD 829/2023. None of them appears anywhere else in the lesson. Its «Ministro de la Presidencia (hoy: …)» note went with it. Disposición final cuarta.2 TREBEP stays, still quoted in «Sistemas selectivos». No «Lo que más cae» line rested on the section. The course has no pointer to it: every `m04-l03` reference found by `grep -rn` names the lesson only, and `lesson-refs.es.txt` has none into this section. `glossary-links.es.txt` has no link inside the section, so no glossary entry is affected. The scope verdict is remove: no question asked this content. The Normativa edit is correct but was not rewrapped. Its first line now ends at 96 characters on «disposición adicional», and «decimoséptima.4;» fits on that line. | `- TREBEP (RDL 5/2015): arts. 9.2, 10, 56.1, 57.1–3, 57.5, 61.6, 61.8 y 76; disposición adicional decimoséptima.4;`<br>`  disposición derogatoria única f); disposición final cuarta.2. Cambio pendiente: Ley 4/2026, de 1 de octubre, en vigor`<br>`  el 23-10-2026 (art. 49.e)); ninguno de los artículos citados aquí cambia.` |
| 2 | m04-l03 | removal, Ley 30/1984 in the intro | PASS | The lesson no longer cites Ley 30/1984 anywhere, and the intro now ends «…Administración general del Estado (RD 364/1995).». The Ley 30/1984 Normativa line is deleted. | — |
| 3a | m04-l03 | coverage, «(hoy: Secretaría de Estado de Función Pública)» at art. 27.1 | PASS | Art. 27.1 RD 364/1995 reads «…cuando se trate de Cuerpos y Escalas dependientes de la Secretaría de Estado para la Administración Pública» (verbatim in the lesson). After the removal this is the lesson's first mention of the old organ, so this is the convention's place for the note. Art. 22.3.c) RD 829/2023 lists «La Secretaría de Estado de Función Pública» among the ministry's órganos superiores, and 22.2 gives the ministry función pública. The note therefore names today's holder of the function. RD 829/2023 gets its full title at its first mention in the lesson, now this one. The wrap is ≤ 120. | — |
| 3b | m04-l03 | coverage, «(hoy: titular de la Secretaría de Estado de Función Pública)» at art. 25.1 | FAIL | Art. 25.1 is quoted correctly («serán nombrados funcionarios de carrera por el Secretario de Estado para la Administración Pública…»). The convention, though, adds «(hoy: …)» once, after the first mention in a lesson (ledger, decision 1 and the bloque I cross-cutting note: «add "(hoy: …)" once»). This is a second note on the same organ, already mapped at art. 27.1 (3a). Row conv2025_A Sup. I reserva 3 stays covered without it: 3a maps the Secretaría, the new paragraph 3c places it in today's ministry, and the «Lo que más cae» line 3d states «hoy titular de la Secretaría de Estado de Función Pública». | Revert the paragraph to its HEAD text:<br>Los aspirantes que superen el proceso selectivo, cuyo número no puede exceder en ningún caso del de plazas convocadas,<br>son nombrados funcionarios de carrera por el Secretario de Estado para la Administración Pública. Cualquier resolución<br>que lo contravenga es nula de pleno derecho (art. 25.1 RD 364/1995). Los nombramientos se publican en el «Boletín<br>Oficial del Estado» (art. 25.2 RD 364/1995). Ninguno de los textos citados dice si el artículo 25.1 del RD 364/1995 se<br>opone a los artículos 61.8 TREBEP y 114.10 RDL 6/2023; las cláusulas de derogación son las citadas en los sistemas<br>selectivos. |
| 3c | m04-l03 | coverage, new paragraph, RD 829/2023 art. 22.3.c) and RD 1009/2023 art. 21.C) | FAIL | The first sentence matches art. 22.3.c). In the second, art. 21.C) RD 1009/2023 reads: «…de la que dependen la Dirección General de Función Pública, con rango de subsecretaría, y la Dirección General de Gobernanza Pública. Asimismo, depende de esta Secretaría de Estado la Oficina de Conflictos de Intereses, con rango de Dirección General.» «De ella dependen …» presents a closed list and drops the third organ. The R2 rule says a shortening keeps every organ. m04-l01 («Los órganos de hoy») states all three, and the cited Normativa label matches m04-l01. | La Secretaría de Estado de Función Pública es un órgano superior del Ministerio para la Transformación Digital y de la<br>Función Pública (art. 22.3.c) RD 829/2023). De ella dependen la Dirección General de Función Pública, con rango de<br>subsecretaría, y la Dirección General de Gobernanza Pública, y también la Oficina de Conflictos de Intereses, con rango<br>de Dirección General (art. 21.C) Real Decreto 1009/2023, de 5 de diciembre, por el que se establece la estructura<br>orgánica básica de los departamentos ministeriales). |
| 3d | m04-l03 | «Lo que más cae», art. 25.1 line | PASS | The line now answers the reserva 3 key (b, «La Secretaria de Estado de Función Pública»), and both citations are right. A «Lo que más cae» line stands alone, so carrying the mapping there is not a second in-text note. The block has 8 lines and stays unwrapped like every line of the block. | — |
| 3e | m04-l03 | Normativa, RD 829/2023 and RD 1009/2023 | PASS | The lesson cites RD 829/2023 art. 22.3.c) at 27.1, in the new paragraph and in «Lo que más cae», and no longer cites art. 22.2. It cites RD 1009/2023 art. 21.C) in the new paragraph, and the label is as in m04-l01. The RD 364/1995 line (4.1, 22.3, 24.1, 25 y 27.1) is still in step. | — |
| 4 | m04-l04 | coverage, art. 89.3 TREBEP (agrupación familiar) | FAIL (form only) | The new text is art. 89.3, first paragraph, almost verbatim. It keeps every employer: AAPP, organismos públicos and entidades de derecho público, Órganos Constitucionales or Poder Judicial and similar CCAA bodies, UE and organizaciones internacionales. Art. 89.1.b) creates the modality, and 89.3 is its only rule. RD 365/1995 art. 17.1 also has a closed, all-public list. «El artículo no menciona otros empleadores: el puesto del cónyuge en una empresa privada no da lugar a esta excedencia» is therefore sound, and it is the fact conv2022_X Sup. II 9 asks (key b «No, no está contemplada en el EBEP»). The partial row is now covered, and Normativa already cites 89.3. The paragraph was not reflowed, though: the line «TREBEP). El RD 365/1995 le da una duración mínima de dos» is 56 characters in mid-paragraph. | Puede concederse sin el periodo mínimo de servicios a los funcionarios cuyo cónyuge resida en otra localidad por haber<br>obtenido y estar desempeñando un puesto de trabajo de carácter definitivo como funcionario de carrera o como laboral<br>fijo en cualquiera de las Administraciones Públicas, organismos públicos y entidades de derecho público dependientes o<br>vinculados a ellas, en los Órganos Constitucionales o del Poder Judicial y órganos similares de las comunidades<br>autónomas, así como en la Unión Europea o en organizaciones internacionales (art. 89.3 TREBEP). El artículo no menciona<br>otros empleadores: el puesto del cónyuge en una empresa privada no da lugar a esta excedencia. No se devengan<br>retribuciones ni computa el tiempo a efectos de ascensos, trienios y derechos de Seguridad Social (art. 89.3 TREBEP). El<br>RD 365/1995 le da una duración mínima de dos años y máxima de quince. Antes de los quince años hay que pedir el<br>reingreso o se declara de oficio la de interés particular (art. 17 RD 365/1995). |
| 14 | m04-l07 | coverage, Ley 29/1975 (Mutualidad General única) | PASS | Each sentence checks against the Ley 29/1975 file: (1) «La Ley 29/1975 creó una Mutualidad General única…» matches the preámbulo, apartado Cinco («La nueva Ley crea una Mutualidad General única para todos los funcionarios de carrera de la Administración Civil del Estado»). (2) The second sentence copies art. diez.uno with its five situations. «Los demás incluidos obligatoriamente en su campo de aplicación» faithfully renders «los demás comprendidos en el artículo tercero, uno», and tercero.uno is the «obligatoriamente incluidos» list. The past tense fits a repealed law. (3) RDL 4/2000 disposición derogatoria única a).1 repeals the Ley 29/1975 «en su totalidad». The source file's sha256 matches the fix file, and its `normativa.yaml` entry is present. conv2022 P1 32 (b, 1975, «organismo único») is now stated, and the partial row is covered. The paragraph is in step with voice and ≤ 120. | — |
| 15 | m04-l07 | «Lo que más cae», Ley 29/1975 line | PASS | Both clauses are cited to the right texts (preámbulo RDL 4/2000; preámbulo Ley 29/1975). The block has 8 lines. | — |
| 16 | m04-l07 | Normativa | PASS | «disposición derogatoria única a).1» is added to the RDL 4/2000 line, and the new Ley 29/1975 line has preámbulo, tercero.uno and diez.uno. Both match the in-text citations, and both lines are ≤ 120. | — |
| 21 | m04-l09 | restore, pointer to m04-l08 (complemento hasta el 100 %) | PASS | m04-l08 states art. 70 Convenio único («…complementa la prestación económica de la Seguridad Social hasta el 100 % del salario del Convenio durante todo el tiempo de la situación (art. 70 Convenio único)»), checked against art. 70. The pointer is bare (m04-l08), as the convention requires. conv2022_X P1 33 exists and asks this (key c). The pointer adds no article, so Normativa is unchanged. The wrap is ≤ 120. | — |

## Covered rows re-checked

The verifier re-found, in the lessons as they stand, every quote the coverage reports mark covered:

- m04-l03: 8;
- m04-l04: 28;
- m04-l07: 5;
- m04-l09: 7.

No edit removed or weakened a covered row. In particular, all eight m04-l03 «Lo que más cae» quotes survive the edits.
The three partial rows (m04-l03 reserva 3, m04-l04 Sup. II 9, m04-l07 P1 32) are now covered. That holds for m04-l03
whether or not 3b is applied (see 3a, 3c, 3d).

## Other checks

- Cut items in this share were spot-checked against the questionnaires: m04-l03 DT 3.ª.2; m04-l07 cotización, prestaciones list, gran invalidez and prórroga; m04-l09 lactante, desempleo scale, arts. 155.1 and 195.1. No hit beyond those the fix file names (conv2024_X P1 38 grupo A/E sueldo ratio, conv2024_A Sup. I 15 LGSS grados, conv2022_X P1 9 art. 264), so «not asked» stands.
- Voice: none of the new sentences uses a filler, a triad, a rhetorical question or a summary closer. «El artículo no menciona otros empleadores: …» (4) follows the lesson's own «El artículo no dice…» pattern.
- No list marker appears mid-sentence in the changed text.

## Counts

- Changes checked: 12 rows (8 numbered changes; change 3 split into 5 parts).
- PASS: 8 (2, 3a, 3d, 3e, 14, 15, 16, 21).
- FAIL: 4. Two are substantive: 3b (a second «(hoy: …)» against the convention) and 3c (art. 21.C) shortening drops the Oficina de Conflictos de Intereses). Two are form only: 1 (Normativa line not rewrapped) and 4 (paragraph not reflowed).
