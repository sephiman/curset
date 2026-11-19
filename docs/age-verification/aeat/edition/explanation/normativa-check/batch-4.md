# Normativa block check, batch 4 (m03-l13 to m03-l20)

Blind verification of the «## Normativa» block of each lesson against the citations in the lesson body
(prose, esquema tables, «Lo que más cae»). Verifier: opus, 2026-11-19. No lesson file was edited.

## Method

- A citation is an abbreviated reference «art./arts. N[.x] <norm>» in a parenthesis or in the last
  (Cita) column of an esquema table, or a disposición cited the same way («(disposición adicional
  decimosexta LIRPF)»). A citation without a norm name in a series takes the norm of the next or
  previous name in the same parenthesis or cell.
- Spelled-out cross-references inside reproduced norm text («los artículos 86 y 87 LGT», «el artículo
  80 de esta Ley», «disposición adicional undécima LIRPF» inside a list of reductions) are mentions,
  not citations; they are listed under Observations and do not decide PASS/FAIL.
- Extraction was done with a script over the whole lesson up to «## Normativa», then every segment
  the script could not attribute to a norm (citations such as «art. 10.2.a) LIRPF», «art. 233.4.b)–e)
  CAU», «art. único.2 Orden HFP/792/2023») was read by hand. Sub-ranges such as «arts. 191.3–4 LGT»
  were read as one article. The set of cited articles per norm was compared with the set the block
  line expands to (ranges expanded); every label was checked against `short` in
  `content/aeat-agentes-hacienda/sources/normativa.yaml`.

## Results

| Lesson | Line | Result | Notes |
|---|---|---|---|
| m03-l13 | LGT (Ley 58/2003): arts. 27, 62, 178–212, 201 bis y 206 bis. | PASS | 27 (art. 27.2), 62 (art. 62.2.b), every article 178 to 212 cited, 201 bis and 206 bis cited. |
| m03-l13 | RGRST (RD 2063/2004): arts. 2, 5, 7, 20, 22–24 y 29. | PASS | 2, 5.1, 7.2, 20.1, 22.1, 23.4, 24.2, 29.2. |
| m03-l14 | LGT (Ley 58/2003): arts. 7, 213–245, 241 bis, 241 ter y 247–249 y disposición adicional duodécima. | PASS | Every article 213 to 245, 241 bis, 241 ter, 247 to 249 and 7 cited; DA duodécima cited at line 260. 246 is not cited and not listed. |
| m03-l14 | RGRVA (RD 520/2005): arts. 14, 16, 21, 22, 25, 28–30, 35, 36, 39, 61 y 64. | PASS | Exact match. |
| m03-l14 | Ley 39/2015 (LPAC): art. 30. | PASS | arts. 30.4 and 30.5 LPAC. |
| m03-l15 | LIRPF (Ley 35/2006): arts. 1–14, 16–23, 25–39, 42, 43 y 85 y disposición adicional 55.ª. | PASS | Exact match (15, 24, 40, 41 not cited); DA 55.ª cited at line 755. |
| m03-l15 | RIRPF (RD 439/2007): arts. 2, 9, 12, 14, 15, 21–23, 25, 29, 33 y 40–42. | PASS | 9 (art. 9.A/B …), 14 (art. 14.2.a RIRPF, line 333) included. |
| m03-l15 | Orden HAC/1425/2025 (módulos 2026): arts. 1–3 y disposición adicional primera. | PASS | arts. 1, 2, 3 (3.1.a/b in the esquema at lines 539 and 541); DA primera at line 546. |
| m03-l15 | LGT (Ley 58/2003): art. 35. | PASS | |
| m03-l15 | Orden HFP/792/2023 (dietas y gastos de locomoción en el IRPF): art. único. | PASS | «art. único.2 Orden HFP/792/2023», line 230. |
| m03-l15 | Orden HAC/1161/2026 (módulos 2027): disposición adicional cuarta y disposición adicional primera. | PASS | DA cuarta (line 548), DA primera (line 550), in that order; no article cited. |
| m03-l15 | «nombrada/nombrado en…» line | not checked as a citation line | Spot-checked: each named norm sits under the citation the line gives (Ley 22/2009 under art. 3.2, RDL 29/2026 under 7.ñ), 23.2, 85.1 and DA 55.ª, etc.). No contradiction found. |
| m03-l16 | LIRPF (Ley 35/2006): arts. 15, 17, 18, 20, 44–63, 66–69, 79–84, 81 bis, 96–98 y 102–104, disposición adicional decimosexta y disposición adicional sexagésima primera. | PASS | Exact match; DA decimosexta (line 116), DA sexagésima primera.1 (lines 302, 307–308). |
| m03-l16 | RIRPF (RD 439/2007): arts. 49, 61, 62 y 66. | PASS | |
| m03-l17 | LIS (Ley 27/2014): arts. 1–13, 15–18, 20–34, 30 bis, 40, 41, 105, 109–111 y 124–127, disposición adicional decimoquinta y disposición transitoria cuadragésima cuarta. | PASS | Exact match (14 and 19 not cited); DA decimoquinta.1 (lines 320, 355), DT cuadragésima cuarta.2 (lines 382–385). |
| m03-l17 | LGT (Ley 58/2003): art. 66. | PASS | art. 66.a) LGT, line 457. |
| m03-l17 | LIRPF (Ley 35/2006): art. 68. | PASS | |
| m03-l18 | LIVA (Ley 37/1992): arts. 1–13, 8 bis, 9 bis, 20–25 y 68–73. | PASS | Exact match. |
| m03-l18 | RIVA (RD 1624/1992): arts. 8, 9 y 13. | PASS | |
| m03-l19 | LIVA (Ley 37/1992): arts. 9, 20, 75–89, 92–110, 115–119 y 119 bis. | PASS | Exact match (90, 91, 111–114 not cited). |
| m03-l19 | RIVA (RD 1624/1992): art. 30. | PASS | |
| m03-l19 | RD 1619/2012 (Reglamento de facturación): art. 15. | PASS | art. 15.3 RD 1619/2012. |
| m03-l20 | Reglamento Delegado (UE) 2015/2446 (CAU, normas de desarrollo): arts. 5–7, 77, 80, 135–138 y 140. | PASS | Text cites it as «Reglamento Delegado del CAU». |
| m03-l20 | Reglamento de Ejecución (UE) 2015/2447 (CAU, normas de ejecución): art. 221. | PASS | Text: «Reglamento de Ejecución del CAU». |
| m03-l20 | Código Aduanero de la Unión (Reglamento (UE) 952/2013): arts. 4, 5, 9, 18–21, 39, 70–72, 77–87, 103, 124, 144, 149, 158–163, 233, 237 y 240. | PASS | 71, 72 and 233 confirmed by hand (art. 71.1.e), 72.a), 233.4.a) and 233.4.b)–e) CAU). |

Totals: 24 article/disposición lines, 24 PASS, 0 FAIL. No cited norm lacks a line; no line carries a
label that differs from its `short` in normativa.yaml; no listed article is uncited and no cited
article is missing.

## Observations (not failures)

- m03-l16: «disposición adicional undécima LIRPF» appears inside reproduced text (lines 59, 426:
  «las reducciones de los artículos 51, 53, 54, 55 y disposición adicional undécima LIRPF (art. 50.1
  LIRPF)»), never as a citation. Under the convention above it is correctly absent from the LIRPF line;
  if the coordinator counts in-text disposiciones with a norm name as citations, the line would gain
  «disposición adicional undécima».
- Norms mentioned only in reproduced text, with no line and no «nombrado en» line (allowed by rule 5,
  listed for consistency with m03-l15, which does carry such a line):
  - m03-l13: Reglamento (UE) 952/2013, artículo 127 (inside arts. 198.4 and 199.7 LGT).
  - m03-l17: Ley 9/2012 (DA décima), Ley 27/1984 (art. 22), Ley 7/1985 (art. 36), Código de Comercio
    (art. 42), the ley de Organización y Funcionamiento de la Administración General del Estado and the
    ley de las Agencias estatales (disposiciones adicionales, lines 72–73).
  - m03-l18: Ley 24/1988 (art. 108), Ley de Contratos del Sector Público (art. 32), Código Civil (art. 334).
  - m03-l19: LGT («artículos 26 y 27 de la Ley General Tributaria», «artículos 124 a 127 de la LGT»),
    RGAT (art. 74), Ley 10/2014 (DA tercera), Ley 49/2002 (art. 2), Ley 22/2003 (art. 21),
    Directiva 2006/112/CE (art. 226), TR Ley de Contratos del Sector Público (art. 235).
  - m03-l20: Reglamentos (CE) (arts. 35–41, 115–121) and Directivas (UE) named inside reproduced articles of the
    Reglamento Delegado.
- m03-l20 never spells out the numbers of the three customs regulations in the body («CAU»,
  «Reglamento Delegado del CAU», «Reglamento de Ejecución del CAU»); the block labels are the only
  place the reader sees 952/2013, 2015/2446 and 2015/2447. The labels are correct.
