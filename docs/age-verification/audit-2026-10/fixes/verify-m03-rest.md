# R2b fixes — bloque III (m03-l01, m03-l04, m03-l05): blind verification

Verifier, 2026-10-17, to the «Verifier (blind)» section of `spec.md` (this folder). Scope: every change to m03-l01,
m03-l04 and m03-l05 in `fix-m03.md`. m03-l03 is verified separately. Checked: the lessons as they stand (`git diff`
against HEAD for the changed lines). The source articles were read by the verifier with `pdftotext -layout` from
`content/age-administrativo-c1/sources/normativa/`: LCSP arts. 49.1, 62.1–2, 65.1, 66.1, 88.1.a), 99.1, 131.2, 135.1,
145.1, 196.1–2, 223.2, 229.5–6 and 323.3; LRJSP art. 30.1; Ley 50/1997 art. 26.2. Also checked: the questionnaires
and keys in `SP/exams/`, the coverage reports `coverage/m03-l01.md`, `m03-l04.md` and `m03-l05.md`, the scope report
`scope/m03.md`, the ledger's III.4 note on ministry names and `docs/prose-voice.md`. The questions checked were
conv2025 extraordinario P1 reserva 4 (key d); conv2020 S II 1 (key C); conv2020_X S II 6 (key D); conv2022_X S II 5
(key c), P1 20, P1 30, P1 res. 5, S I res. 4, S II 6 and S II 16; conv2025 modelo A S II 4; conv2025_X S I 5; conv2024
modelo A P1 22; conv2024_X S I 8 and S II 7; conv2022 S I 14.

| # | Lesson | Change | PASS/FAIL | Reason | Replacement (for FAIL) |
|---|---|---|---|---|---|
| l01-1 | m03-l01 | note, «El procedimiento de elaboración» | PASS | conv2025 extraordinario, primera parte, «Preguntas de reserva» 4 exists. It asks when the consulta pública under art. 26 Ley 50/1997 may be skipped, and the definitive key is d (aspectos parciales). Art. 26.2.e) Ley 50/1997 is in the section's list and in «Lo que más cae». The scope report marks the section «unmapped … keep» on this question. The note follows the spec form and sits right after the ### heading. No subsection has a note of its own. Wrap ≤ 120. | — |
| l04-1 | m03-l04 | coverage + restore, art. 62 LCSP | PASS | Art. 62.1 is verbatim from «los órganos de contratación deberán designar…» onward. The «Con independencia de…» clause and the last sentence are whole facts, so leaving them out is allowed. Art. 62.2 is verbatim up to «Director Facultativo»; the lesson leaves out «conforme con lo dispuesto en los artículos 237 a 246». Row 2024 extr. S II 7 (key d «El Director Facultativo») is now stated. Wrap ≤ 120. | — |
| l04-2 | m03-l04 | coverage + restore, arts. 229.5 and 323.3 LCSP | PASS | The organ, the adscription to the DG and the saving for contratos basados with entidades adheridas match art. 229.5, and art. 323.3 names the Junta. The lesson omits «del Ministerio de Hacienda y Función Pública». That follows the standing III.4 convention in `docs/age-theory-ledger.md` («Ministry name … is omitted, not given a «hoy»»). The sentence remains true. Row 2022 extr. S II 16 (key c) is now stated. | — |
| l04-3 | m03-l04 | coverage + restore, «### Condiciones de aptitud», arts. 65.1 and 66.1 | PASS | Art. 65.1 is verbatim, with «esta Ley» changed to «la LCSP». Art. 66.1 is verbatim. The heading is the title of art. 65. Row 2022 extr. P1 res. 5 (key a, «Españolas o extranjeras») and row 2025 ord. S II 4 (key a) are now stated. | — |
| l04-4 | m03-l04 | coverage, art. 88.1.a) LCSP | PASS | «uno o varios medios, a elección del órgano de contratación», «cinco últimos años», the certificate contents (importe, fechas, lugar) and «últimos diez años» are all in art. 88.1 and 88.1.a). The sentences left out are whole facts. Row 2022 extr. S II 6 is now stated: option a (three years) is the false one. Art. 88 governs solvency, which sits under art. 65.1's aptitude conditions, so it fits the subsection. | — |
| l04-5 | m03-l04 | coverage + restore, art. 99.1 LCSP | PASS | This is the first sentence of art. 99.1, verbatim. Row 2022 extr. P1 20 (key d «Determinado») is now stated. The arts. 100.1 and 101 text is unchanged. The line break before «es el importe total» was already ragged at HEAD, and every line is ≤ 120. | — |
| l04-6 | m03-l04 | coverage + restore, arts. 131.2 and 145.1 LCSP | PASS | The first sentence is art. 131.2, verbatim. «que se adjudicarán mediante este último procedimiento» is resolved correctly as «por el procedimiento restringido». The second sentence faithfully shortens art. 145.1, párr. 2: the justification in the expediente, coste-eficacia, precio o coste and ciclo de vida are all kept. Rows 2024 ord. P1 22 (key b) and 2022 extr. P1 30 (key c) are now stated. | — |
| l04-7 | m03-l04 | coverage, art. 135.1 LCSP | PASS | The perfil de contratante, the exception for negociados sin publicidad, the BOE for the AGE and its entities, and the DOUE for harmonised contracts all match art. 135.1 párrs. 1–2. The 2022 extr. S I res. 4 partial is now closed: the open procedure comes from art. 131.2 and the DOUE from art. 135.1. | — |
| l04-8 | m03-l04 | coverage + restore, art. 223.2 LCSP | PASS | Verbatim. Row 2025 extr. S I 5 (key b) is now stated. Placed in «### Acuerdos marco», the nearest section of the same chapter (racionalización técnica). Optional, not required: a heading «### Sistemas dinámicos de adquisición» would make it easier to find. | — |
| l04-9 | m03-l04 | restore, art. 196 LCSP | PASS | Art. 196.1 is verbatim. Art. 196.2 is a faithful shortening: it keeps «inmediata y directa», «dentro de los límites señalados en las leyes», the vicios del proyecto in obras, the repetition against the redactor and the suministro de fabricación. Only the reference to art. 315 is dropped. conv2024_X S I 8 (key d «consecuencia inmediata y directa») exists and is now stated in the owner lesson too. «También lo será» copies the law's «También será la Administración responsable». | — |
| l04-10 | m03-l04 | coverage + restore, art. 49.1 LCSP | PASS | Verbatim, with «resolver el recurso» changed to «resolverlo». Row 2022 ord. S I 14 (key c) is now stated. The art. 45.1 and art. 50.1 text is kept. | — |
| l04-11 | m03-l04 | «Lo que más cae» line, arts. 131.2 and 145.1 | PASS | The line matches arts. 131.2 and 145.1. The block now has 9 lines (≤ 10). Two questions ask it (2024 ord. P1 22, 2022 extr. P1 30), which meets the rule's threshold. The line is unwrapped, as every line of the block is. | — |
| l04-12 | m03-l04 | Normativa, LCSP line | PASS | 49, 62, 65–66, 88, 99, 131, 135, 145, 196, 223 and 229 are added, and 323 (for 323.3) was already listed. No article was dropped. Every article cited in the lesson is on the line. Wrap ≤ 120. | — |
| l05-1 | m03-l05 | restore, art. 30.1 LRJSP | PASS | Verbatim, all six plazos included. The «éstas» accent is the BOE text's. The text sits in «Principios de la potestad sancionadora» (LRJSP capítulo III, arts. 25–31), after the art. 29.3 list. The sentence matches m03-l03's except for the pointer. conv2020 S II 1 (key C, graves two years), conv2020_X S II 6 (key D, sanción muy grave three years) and conv2022_X S II 5 (key c, graves two years) exist and ask this fact. | — |
| l05-2 | m03-l05 | «Lo que más cae» line, art. 30.1 | PASS | All six plazos are right. The wording matches m03-l03 line 420. The block now has 9 lines (≤ 10). Three questions ask it. | — |
| l05-3 | m03-l05 | Normativa, LRJSP line | PASS | «arts. 4.1, 25.1, 27.1, 29.3 y 30.1» matches the articles cited. | — |

## Re-check of rows marked covered

- m03-l01 (5 covered): the only change in this lesson is the note. CC 2.1, art. 26.2.e) Ley 50/1997, CE 86.1 and art.
  24.2 Ley 50/1997 are still stated (2024 extr. P1 17 is in m01-l03).
- m03-l04 (51 covered): the diff adds text only, except two rewrapped paragraphs (arts. 100.1/101, arts. 45.1/50.1)
  and the Normativa line. Every removed line comes back word for word. A spot check of ten quotes from the report
  found each one still present.
- m03-l05 (2 bracketed rows): art. 29.3.a) LRJSP and art. 63.1 LPAC are still stated.

The new paragraphs were checked against the voice page: no fillers, rhetorical questions, «no solo… sino también»,
closers or split-opener tics. The enumerations come from the articles, so they are not rhetorical triads. No list
marker sits mid-sentence, and every new or changed prose line is ≤ 120 characters. The over-long prose lines in m03-l04
(127, 155, 268, 285, 328, 329 at HEAD) were there before the fix.

## Counts

- Changes verified: 16 (m03-l01: 1; m03-l04: 12; m03-l05: 3).
- PASS: 16.
- FAIL: 0.
- Covered rows lost: 0.
