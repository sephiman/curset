# R2b fixes — bloque I (m01-l01 … m01-l11): blind verification

Verifier, 2026-10-17, to the «Verifier (blind)» section of `spec.md` (this folder). Checked: the lessons as they stand
(`git diff` against HEAD for the changed lines), the source articles read by the verifier with `pdftotext -layout` from
`content/age-administrativo-c1/sources/normativa/` (CE arts. 94.1 and 134.7 and the heading of título III, capítulo
tercero, in `BOE-A-1978-31229_ce_2026-05-20.pdf`; Ley 19/2013 arts. 10.1, 11 and 19.1–19.2 in
`BOE-A-2013-12887_ley-transparencia_2022-07-09.pdf`; TUE art. 19.3 and Protocolo n.º 3, art. 50 ter, in
`CELEX-02016M-20250315_tue_2025-03-15.pdf`; TFUE art. 256 in `CELEX-02016E-20250315_tfue_2025-03-15.pdf`), the
questionnaires in `SP/exams/` (conv2025_X P1 12 and 19; conv2025_A first reserve block 3; conv2024_A P1 8; conv2024_X
first reserve block 1; conv2022 P1 15, 26, 29 and first reserve block 1; conv2022_X P1 22; conv2020 P1 1; conv2020_X
P1 5 and 7), `scope/m01.md`, `coverage/m01*.md` and `docs/prose-voice.md`. m01-l04, l05, l08, l09 and l10 are unchanged
against HEAD. E1 is the coordinator's change from `currency/verify-eu.md` #16, not in `fix-m01.md`.

| # | Lesson | Change | PASS/FAIL | Reason | Replacement (for FAIL) |
|---|---|---|---|---|---|
| l01-1 | m01-l01 | coverage, art. 94.1.e CE, after the table in «Estructura» | PASS | Letter e) is copied whole («supongan modificación o derogación de alguna ley o exijan medidas legislativas para su ejecución»; «previa autorización de las Cortes Generales»). «Capítulo tercero del título III … tratados internacionales» matches the CE heading. conv2025_X P1 19 exists; key d is now stated. The pointer is correct: m01-l03 line 343 gives the full art. 94.1 list. The citation form «94.1.e» matches the lesson («162.1.a»). Normativa adds 94.1 in order. Wrap ≤ 120. | — |
| l01-2 | m01-l01 | note, «Las reformas» | PASS | conv2022 P1 26 and conv2020 P1 1 exist and ask how many times the CE was reformed, which the section states. Note names follow the spec («la convocatoria 2022»; «la convocatoria de la OEP 2020 (examen de 2022)»). Placed right after the heading. | — |
| l02-1 | m01-l02 | pointer, «La reforma del título II» → m01-l01 | PASS | m01-l01 has «### Procedimiento agravado» (art. 168). The form «m01-l01, el tema de …» matches the course's existing pointers. Wrap ≤ 120. | — |
| l03-1 | m01-l03 | coverage, art. 134.7 CE | PASS | Faithful to art. 134.7 («no puede crear tributos. Podrá modificarlos cuando una ley tributaria sustantiva así lo prevea»). conv2022 P1 15 exists; key c is now stated. Normativa CE line adds 134.7. | — |
| l03-2 | m01-l03 | pointer → m05-l01 | PASS | m05-l01 has «Elaboración» and «Remisión a las Cortes y aprobación» under «El ciclo presupuestario». The pointer form matches the course. Wrap ≤ 120. | — |
| l06-1 | m01-l06 | note, «La Alianza para el Gobierno Abierto» | PASS | conv2022_X P1 22 exists and asks Spain's OGP membership (estado `dudosa`; the scope report still keeps the section on it). Note form and placement are correct. | — |
| l06-2 | m01-l06 | removal, «El Gobierno Abierto en España» | PASS | Heading and whole body are gone. The child «Los planes» is promoted to ##, so it does not fall under «Principios informadores». No text left refers to the removed organs. The Foro is still named in «Los planes» and «Lo que más cae» as the body that approved the plans, which reads on its own. The source html is still cited at lines 17, 30, 205 and 215, so Normativa is right to stay unchanged. No «Lo que más cae» line rested on the section. No lesson pointed to it (the Gobernanza Pública hits in m02-l03, m04-l01 and m04-l03 are their own facts). Glossary: `g-competencia-exclusiva` still has `link_except: [m01-l06]`, now stale, as the fix file says. | — |
| l06-3 | m01-l06 | note, «Los planes de Gobierno Abierto» | PASS | conv2024_A P1 8 (ejes), conv2024_X first reserve block 1 (fecha del IV Plan) and conv2022 P1 29 (plan vigente) exist and ask this section. One note for the three; spec wording. | — |
| l07-1 | m01-l07 | restore, art. 11 Ley 19/2013 | PASS | A faithful shortening of art. 11, with all three principles. conv2020_X P1 5 (key a) exists and is now stated. Normativa «5–10, 12–20» → «5–20» adds only 11, which is now cited. The Normativa line is unwrapped (125 characters), as the block's other lines in the bloque are. | — |
| l07-2 | m01-l07 | restore, art. 19.1 Ley 19/2013 | PASS | Art. 19.1 nearly verbatim, with the condition «si lo conoce» kept. It is placed before art. 19.2, in the norm's order. conv2020_X P1 7 (key d) exists and is now stated. | — |
| l11-1 | m01-l11 | note, «Las competencias de la Unión» | PASS | conv2025_A first reserve block 3 (art. 3 TFUE) and conv2022 first reserve block 1 (art. 4 TFUE; option a needs art. 6) exist. One note on the ## covers its three ###, as the spec allows. | — |
| l11-2 | m01-l11 | note, «Ingreso y retirada» | PASS | conv2025_X P1 12 exists and asks art. 49 TUE (Consejo, unanimidad), which the section states. Spec wording. | — |
| E1 | m01-l11 | currency, «Los recursos»: art. 19.3 TUE subject, art. 256.3 TFUE, art. 50 ter Estatuto | FAIL | The art. 19.3 sentence now has the correct subject. The art. 256.3 sentence is para. 1 verbatim, and the six subject areas match art. 50 ter letters a)–f). The problem is that art. 50 ter is shortened without its exception. The second paragraph says «No obstante … el Tribunal de Justicia seguirá siendo competente» for petitions that raise independent questions of interpretation of primary law, public international law, general principles or the Charter. Without it, «la transfiere al Tribunal General si está comprendida exclusivamente en esas materias» overstates the transfer (R2: a shortening keeps every exception). Two smaller points. «en una o varias de» was dropped, so the list joined by «y» can read as cumulative. «será competente» is the Treaty's future tense, while the paragraph and the lesson state the law in the present. Normativa: TUE line adds Protocolo n.º 3, art. 50 ter; TFUE line adds 256; both are in step. Optional: art. 256.3, para. 2 (the Tribunal General may refer a case needing a decision of principle to the Tribunal de Justicia). | El Tribunal de Justicia de la Unión Europea se pronuncia sobre los recursos de un Estado miembro, de una<br>institución o de personas físicas o jurídicas, y con carácter prejudicial, a petición de los órganos<br>jurisdiccionales nacionales (art. 19.3 TUE). El Tribunal General es competente para conocer de las<br>cuestiones prejudiciales, planteadas en virtud del artículo 267, en materias específicas determinadas por<br>el Estatuto (art. 256.3 TFUE). El Estatuto le da las que estén comprendidas exclusivamente en una o<br>varias de estas materias: el sistema común del impuesto sobre el valor añadido, los impuestos especiales,<br>el código aduanero, la clasificación arancelaria de las mercancías en la nomenclatura combinada, la<br>compensación y asistencia a los pasajeros en caso de denegación de embarque o de retraso o cancelación de<br>los servicios de transporte, y el régimen de comercio de derechos de emisión de gases de efecto<br>invernadero. El Tribunal de Justicia sigue siendo competente para las peticiones que susciten cuestiones<br>independientes de interpretación del Derecho primario, el Derecho internacional público, los principios<br>generales del Derecho de la Unión o la Carta de los Derechos Fundamentales de la Unión Europea. Toda<br>petición se presenta ante el Tribunal de Justicia, que la transfiere al Tribunal General tras verificar<br>que está comprendida exclusivamente en esas materias (art. 50 ter Estatuto del Tribunal de Justicia de la<br>Unión Europea, Protocolo n.º 3). |

## Covered rows re-checked

Every row that `coverage/m01-l01.md` … `m01-l11.md` marks covered was re-found in the lessons as they stand: 10 + 8 +
10 + 6 + 7 + 5 + 6 + 13 + 7 + 7 + 9 quotes, including the m01-l01 rows covered in m01-l05 and m01-l08. No edit removed
or weakened one. The m01-l06 rows all rest on «Lo que más cae» lines that the removal did not touch. The two misses in
`coverage/m01.md` (conv2025_X P1 19, art. 94.1; conv2022 P1 15, art. 134.7) are now covered (l01-1, l03-1).

## Other checks

- Cut items: spot-checked the «not asked» verdicts of I.2 (abdicación), I.4 (jurado, acción popular, policía judicial),
  I.5 (Plan Anual Normativo) and I.7 (art. 21, unidades de información) against every questionnaire: no hits.
- Form: every new prose line is ≤ 120 characters. No list marker sits mid-sentence. No filler, rhetorical question or
  summary closer appears. The new sentences state one fact each.
- Not part of this round, seen in passing: further down «Los recursos», «esta puede recurrir al Tribunal (art. 258
  TFUE)» still uses the bare «el Tribunal», which `verify-eu.md` #16 found ambiguous in the paragraph above.

## Counts

13 changes checked (12 from `fix-m01.md` plus E1): **12 PASS, 1 FAIL** (E1).
