# Build — I.3 (`m01-l03`), 2026-11-17

- Words: HEAD 7,325 (wc) = 7,160 excluding table/esquema rows + 165 in rows. Built 18,997 (wc) = 12,524 excluding rows + 6,473 in rows (esquema rows of the new enumerations; the HEAD «Cuadro de nombramientos» stays).
- Ratio excluding rows: 1.75 × HEAD (7,160); 1.09 × the 1.6 target (11,456). The target is passed: the lesson adds Ley 50/1997 arts. 8–10, 14, 16–17, 19, 24.1 and the DA, LRJSP arts. 19–22, 55 bis, 56, 77–80 and 108 bis–108 sexies, CE arts. 98.3–4, 102, 112–115, and every enumeration of those and of arts. 61–63, 66, 68, 73, 75 as esquemas; nothing was shortened for size (the two procedure-only sentences left out are listed below).
- build_check: `m01-l03: HEAD 293 · added byte-identical 212 · esquema rows from items 207 · not in pool 7`.
- cites.py: 578 citations, 0 unresolved. `index_sources.py --course aeat-agentes-hacienda`: see the coordinator's run (it prints no validation error naming m01-l03 when run after this build).
- Readability: `split_paragraphs.py` run (6 paragraphs split).
- The base was HEAD's text; the pool lesson (`expansion/m01-l03.md`) supplied every added sentence. Every esquema row citation is the unit the lead-in sentence cites (checked against the prose before the lesson file was written).

## Sentences added (new to HEAD): 192 prose/list-item sentences + 234 esquema rows

(a) R2b removal inside a range: «La Comisión General de Secretarios de Estado y Subsecretarios» (art. 8 Ley 50/1997): 11 sentences + 3 rows (8.5 esquema).
(b) Confirmed review items: 1–2 arts. 112–115 CE (cuestión de confianza, moción de censura, disolución, art. 114 and 115.2–3): 16 sentences; 6 arts. 19–22 LRJSP (órganos colegiados de la AGE): 19 sentences + 37 rows; 8 Comisiones Delegadas (6.2 esquema, 6.3, 6.4.b/d): 6 sentences + 3 rows; 11 the 22 ministerios as an esquema (the pool's list in place of HEAD's running paragraph): 23 rows.
(c) Articles HEAD does not treat or treats in part, rule/conditions/exceptions sentences: arts. 98.3–4, 102 CE; Ley 50/1997 4.1.a/c, 4.2, 5.1.k, 5.2, 7.3, 8, 9, 10, 12.1–12.4, 13.2–3, 14, 15.2–4, 16, 17, 18.3, 19, 20.1, 20.4 párr. 2, 21.2–3, 24.1, 29.1/29.4, DA 1.ª–3.ª, 2.2.n); LRJSP 3.1 a)–k), 3.2–3.4, 54.1 párr. 2, 55.7–55.11.b, 55 bis, 56, 57.1–2, 62.1 párr. 2, 63.2, 64.2, 66.1, 68.1–3, 69.3, 70 clauses, 71.2–4, 72.2/72.4 clauses, 73.2–73.4, 77–80, 108 bis–108 sexies, and the «Contenido del título II de la LRJSP» sub-section (chapter level, 10 sentences).
(d) «No confundir»: three blocks (arts. 112 / 113.1–2 CE; art. 103.1 CE / art. 3.1 LRJSP; arts. 98.1, 103.1, 100.1, 106.1 LRJSP): 11 sentences.
(e) HEAD sentences replaced by the pool's completed form: 68.1 (two sentences), the 61, 62.2, 63.1, 73.1 and 75 lead-ins and their lists (HEAD's sentences «Los Ministros dirigen…», «Entre sus funciones están…», «Les corresponde también otorgar…», «Nombran y separan…», «Dirigen y coordinan las Secretarías…», the three 62.2 items, «Los Subsecretarios ostentan…», the six 63.1 items, «Entre sus competencias (art. 73 LRJSP)» and its five items, and the 75.a.1.º, 75.b and 75.c sentences are now the pool's lead-ins and esquema rows); the Normativa lines (below).
Lost from HEAD: only the sentences of (e) and HEAD's three Normativa lines (replaced by the new Normativa).

## Enumerations as esquemas (`| Elemento | Contenido | Cita |`, one row per item, multi-sentence items one row per sentence)

Arts. 17, 6.2, 8.5, 9.1, 9.2, 20.1, 24.1 Ley 50/1997; 3.1, 19.2, 19.3, 19.4, 20.2, 21.1, 22.1, 61 (a–t), 62.2 (a–k), 63.1 (a–q), 66.1, 68.3, 73.1 (a–e with 1.º–4.º), 75 (a–f with 1.º–2.º), 79.1 (a–c with 1.º–4.º), 108 quater.1, 108 quinquies.1 LRJSP; art. 1 RD 829/2023 (the 22 departments). The HEAD lists and esquemas (2.2, 5.1 Ley 50/1997, 55.2, 55.3, 59, 84.1, 128.1 LRJSP, investidura, 55 tree, organización interna, delegados) stay as they were; 2.2.n) and 5.1.k) are appended as the last bullet of their lists.

## «Not in pool» (7): kept, and why

1. `El Presidente del Gobierno ejerce también cuantas otras atribuciones le confieran la Constitución y las leyes (art. 2.2.n) Ley 50/1997).` — last FAIL was about its place (a separate paragraph); it is now the last bullet of the 2.2 list, as the verifier asked. Kept because dropping it leaves the art. 2.2 enumeration (a)–m) incomplete. Needs a re-check of its new place.
2–3. Rows `b)` and `d)` of the art. 24.1 Ley 50/1997 esquema (Reales Decretos del Presidente; Acuerdos del Consejo de Ministros): the pool's items have no PASS verdict (added by the third writer after the checks); a)–f) is one enumeration, so b) and d) stay.
4–7. The four new «Normativa» lines: `CE: arts. 97–104, 107 y 112–115.`, `Ley 40/2015 (LRJSP): arts. 2–3, 8–10, 13–14, 19–22 y 54–139.`, the LPAC line and the line «Ley 3/2015, RDLeg 3/2011, … no figuran en `normativa.yaml`» (rebuilt from what the lesson cites; the pool's text for them has no PASS).

## Pool sentences left out

- Every pool sentence with no PASS verdict (98, added after the blind checks) except the three kept above: art. 104.2 CE; the LO 3/1980 paragraph (arts. 1–2); the whole Ley 3/2015 block (arts. 1–2, the two esquemas a)–g) and a)–e), declaración responsable, títulos I–IV); the Reglamento del Congreso sentences (arts. 170–172, 173–174, 175–179) and their two sub-headings; arts. 1, 2.1 (+esquema), 2.3, 4, 5 (+esquema 5.3), 6, 7 and 9.2 a), b), d) (+esquema) LRJSP; arts. 15–18 LRJSP; the art. 24 LRJSP recusación paragraph; art. 8.3 second sentence and 8.4 second sentence Ley 50/1997. The headings «Órganos administrativos» and both «Procedimiento…» sub-sections were removed because all their content went.
- PASS sentences dropped as procedure only (state no rule, condition or exception): «El Consejo Rector aprueba la propuesta de contrato inicial de gestión, en el plazo de tres meses desde su constitución (art. 108 ter.4 LRJSP).» (who drafts and when) and «El Consejo Rector elabora y aprueba el anteproyecto de presupuesto de la agencia estatal… (art. 108 sexies.1 LRJSP).» (who drafts).
- HEAD's «Estructura vigente…» paragraph with the 22 departments was replaced by the pool's esquema (review item 11); HEAD's esquema «Organización interna de los Ministerios» stays (HEAD esquemas stay).

## Pool gaps (articles or apartados of the ranges with no verified pool sentence; no prose of my own)

- CE: arts. 105 and 106 (no sentence at all); 103.3; 104.2.
- Reglamento del Congreso arts. 170–172, 173–174, 175–179.
- LO 3/1980 arts. 1–2 (map: in doubt); Ley 3/2015 (idoneidad, altos cargos; source also missing).
- Ley 50/1997: clauses of 2.2 b), f), g), h), j); 5.1.e) and 5.1.h) clauses (5.1.e only in «Lo que más cae»); 8.3 second sentence, 8.4 second sentence; 10.2.
- LRJSP, whole articles: 1, 4, 5, 6, 7, 15, 16, 17, 18. Apartados: 2.1, 2.3; 8.1 first-sentence clause, 8.3; 9.2 a), b), d), 9.3, 9.5–9.7; 13.2 first sentence, 13.3, 13.4; 69.2 clause; 76.1 clause «de la que dependerán…», 76.2; 83.1 «reglamentariamente», 83.2.a; 84.3; 89.2 párr. 2; 91.1 rest, 91.2; 100.1 rest; 106.1 rest, 106.2; 110.1 rest, 110.2; 118.2–3; 119.2–3; 120.2 b)–g); 133.2–3 (the last ones sit at chapter level in «Contenido del título II de la LRJSP»).

## Sentences that do not stand on their own where they now sit (they lean on the sentence before, in the lesson or in the previous esquema row)

114.2 CE «El Rey le nombrará…»; 113.3 second sentence and 113.4 «sus signatarios»; 102.2 «Si la acusación fuere…»; 14.2 Ley 50/1997 «Es de aplicación, asimismo…»; 8.2 «No se entiende por ausencia… En ese caso…»; 9.3 «Su Director ejerce…»; 16.3 «Cesan automáticamente…» and «En el supuesto del Gobierno en funciones continúan…»; 19 Ley 50/1997 (refers to art. 18); 62.1 párr. 2 «Pueden ostentar…»; 20.3 LRJSP «Su régimen jurídico…»; 21.2–21.3 LRJSP «Puede haber representantes… / Pueden participar…»; 22.2–22.4 LRJSP «En esos supuestos… / En los demás supuestos… / La modificación y supresión…»; 73.4 «En relación con los servicios territoriales…»; 78.2–78.3 «Se encarga de… / Mediante Real Decreto se regulan sus atribuciones…»; 108 ter.2 «Su actuación se produce…», 108 ter.4 second and third sentences, 108 quinquies.5 «Su contratación…»; the esquema rows 61.l second sentence, 62.2.j «Todo ello dentro de la cuantía…», 63.1.g «En los mismos términos…» and «A tales efectos…», 63.1.i «Todo ello…», 19.3.a «La información sobre los temas…», 19.3.c «No podrán abstenerse…», 73.1.c.1.º «Realizará también estas funciones…», 73.1.d.1.º second and third sentences, 73.1.e.4.º second sentence, 75.a row «En concreto les corresponde:», 75.a.2.º «Realizará también…», 75.b «A estos efectos…», 79.1.c row «Desarrolla, en todo caso, las siguientes funciones:».

## Normativa (new lines, the one place of new text)

`CE: arts. 97–104, 107 y 112–115.` · `Ley 40/2015 (LRJSP): arts. 2–3, 8–10, 13–14, 19–22 y 54–139.` (HEAD's longer list replaced; 81–139 are all cited by the chapter-level sub-section) · LPAC line and the Ley 3/2015 / RDLeg 3/2011 / … line rebuilt from what the lesson names; the Reglamento del Congreso and LO 3/1980 lines of the pool are gone with their sentences. The Ley 50/1997 line is `arts. 1–21, 24 y 29, y disposiciones adicionales primera, segunda y tercera.` (the pool's, still exact).
