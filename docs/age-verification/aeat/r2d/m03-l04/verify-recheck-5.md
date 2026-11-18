# m03-l04 — blind re-check 5 (R2d)

2026-11-18. Opus verifier, blind (no writer.md, build.md, standalone.md or earlier verify*.md opened). 19 rows from
`pending.md`; every id was recomputed against the lesson as it stands (`provenance.sentences` + `sentence_id`) and all 19
match the current text. Norm texts: `content/aeat-agentes-hacienda/sources/normativa/` (RGAT 2026-10-07, RIVA 2026-02-28,
LIVA 2026-10-07, RD 1619/2012 2026-03-31, LGT 2024-12-21, Código de Comercio 2023-05-09, RD 1676/2009 2017-12-30).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `f0d4365381` | PASS | art. 11.2 RGAT | Plazo «un mes», «sin perjuicio…» and «sin que a estos efectos deba darse de alta» all kept. | — |
| `d00611b70b` | PASS | art. 2.3 RGAT, párrafo segundo | «apartado anterior» correctly resolved as art. 2.2; «periodicidad mensual» and the Censo de Obligados Tributarios of art. 4 kept. | — |
| `5b9fa4b13d` | PASS | art. 3.7 RGAT, párrafo segundo | The article says «el Registro a que se refiere el citado párrafo anterior»; the sentence names it by the head of its full name, which the preceding paragraph gives in full. The article's lead clause («Lo dispuesto en el párrafo anterior será independiente de la persona o entidad a cuyo favor preste servicios el depósito fiscal») is not a condition of this rule. | — |
| `425695ffca` | PASS | art. 19.2 RGAT | The obligation and its scope («que realicen o participen en operaciones de naturaleza o con trascendencia tributaria») are in the preceding bullet; L/K letters, nine characters, «menores de 14 años» exact. | — |
| `0f52674658` | PASS | art. 23.4 RGAT | Organ, the three possible applicants and the art. 22.3 and 4 scope match. | — |
| `6f686c4b44` | PASS | art. 69 bis.1.b) RIVA | Four natural days from accounting entry, «en todo caso, antes del día 16 del mes siguiente al periodo de liquidación…» exact; the 62.6 RIVA scope from the article's lead-in kept. | — |
| `74132be7f4` | PASS | art. 164.Uno.6.º LIVA | Verbatim («de esta ley» → «de la LIVA»). Esquema order checked: 1.º–6.º, the two further paragraphs of 6.º as «6.º)» rows, then 7.º, in the article's order. | — |
| `2c3ef0920f` | PASS | art. 32 RGAT | Lead-in to the a)–e) esquema; all five letters present, in order, with the second paragraph of b) after b). | — |
| `b43fe3b4a9` | FAIL | arts. 37–54 ter RGAT | Wrong unit: arts. 49 bis, 50, 53 and 54 RGAT are not divided into apartados (the lesson gives their whole text, cited «art. 49 bis RGAT», «art. 50 RGAT», «art. 53 RGAT», «art. 54 RGAT»), so they have no «primer apartado». Every other article in the range is present with its apartado 1. Structural, for the note column only: the BOE notice on art. 49 ter (line 893) sits before art. 49 bis (line 895). | De cada uno de los artículos 37 a 54 ter del RGAT, salvo el artículo 37 bis, se recoge a continuación su apartado 1 o, en los artículos 49 bis, 50, 53 y 54, que no se dividen en apartados, su texto. |
| `f629e8fd3a` | PASS | art. 38.1.b) RGAT, párrafo segundo | «No se incluirán en esta declaración informativa…» resolved to the letter b) declaration; art. 41 reference kept. | — |
| `6843a854e5` | PASS | art. 7.1.a) RD 1619/2012, último párrafo | Verbatim («este artículo» → «artículo 7 de este Reglamento»); the citation names the Reglamento. | — |
| `51e1aacc00` | PASS | art. 13.2 RD 1619/2012 | First sentence of art. 13.2; the «No obstante… antes del día 16 del mes siguiente» exception follows in the same paragraph under the same citation, so nothing is lost. «Estas facturas» resolved to the art. 13.1 recapitulative invoices. | — |
| `58e1a7b1e4` | PASS | art. 40.5 LGT | Verbatim, with «este artículo» resolved to art. 40 LGT. | — |
| `afab10569b` | PASS | art. 112.2.b) RGAT, second sentence | «en estos casos» resolved to the b) cases; the condition («cuando se haya presentado recurso o reclamación económico-administrativa en el que se alegue dicha falta o insuficiencia») kept. | — |
| `86663b3552` | PASS | art. 59.2.b) RGAT, second sentence | «A estos efectos se remitirán a dicho órgano los antecedentes que sean necesarios»; «a estos efectos» resolved to continuing and finishing the procedures in course, the norm's own preceding sentence. | — |
| `73a3bb8af9` | PASS | arts. 68.6 and 68.7 LGT | Worked example, step 5. The parenthesis lists all six art. 68.7 causes (five in the first paragraph, concurso in the second). Rule applied correctly: art. 68.6 «salvo lo establecido en el apartado siguiente». Dates recomputed with python3: 30-06-2022 Thursday, 01-07-2022 Friday, 14-03-2025 Friday, 15-09-2026 Tuesday, as the example says. | — |
| `2f47266235` | PASS | Normativa, RD 1619/2012 | Both ways. Cited in the lesson: 2.1, 3.1, 3.3, 4.1–4, 5.1–4, 6.1–5, 7.1–5, 8.1–4, 8 bis.1–3, 9.1–2, 10.1–2, 11.1–3, 12.1–2, 13.1–3, 14.1–4, 15.1–6, 17, 18, 19.1–4, 20.1–2, 21.1–2, 22.1–2, 23, 24, so the list matches exactly. DA 4.ª is named in the art. 34.1 RGAT row (line 682), DA 3.ª and 6.ª in art. 4.1 RD 1007/2023 (line 1302). Art. 16.1 is named in art. 3.3 and also in the art. 19.1.d) row. Inside copied text of the same Reglamento, so listing it is not required; the entry is accurate as far as it goes. The cambio-pendiente note matches `normativa.yaml` (RD 238/2026: arts. 8.1, 8 bis, 9, 10; DF 4.ª deferral). | — |
| `8e76f8fe10` | PASS | Normativa, Código de Comercio | Cited: 25.1, 25.2, 28.1, 28.2, 29.1, 30.1, 31, so it matches. Art. 42 is named at line 565 under (art. 120.3 LIS). Other mentions are of the Code as a whole inside copied LIVA, LIRPF, RIRPF and LIS text. | — |
| `29e6e0ee20` | PASS | Normativa, final «no figuran» line | Every listed norm was found at a place the line names: DA 5.ª.8 LGT; RGAT 3.6, 3.8, 14.4, 15, 31.1, 32, 33.1, 33.3, 33.5, 39 quater.1, 42.1, 42 bis.1, 42 ter.1, 42 quater.1, 43.1, 44.1.b), 45.1, 46.1, 47.1, 48.1, 49.1, 49 ter, 53, 54 bis.1, 54 ter.1, 111.7; Reglamento de facturación 5.4, 6.1.j), 8 bis.1, 8 bis.3, 10.1.a) (Reglamento (UE) 910/2014), 10.1.b) (Recomendación 94/820/CE), 10.2, 19.4; 104.5 LIRPF; RD 1676/2009 3.1.f) and 4.5; 76.2.d) RGRVA. No norm the prose names is missing from all Normativa lines. Not listed, and not counted as a norm: the OCDE «Acuerdo Multilateral entre Autoridades competentes…» named in art. 54 ter.1 RGAT (line 950). | — |

Esquema order (requested check): DA 5.ª.3 LGT a)–k); art. 9.3 RGAT a)–v); art. 22.4 RGAT a)–f); art. 32 RGAT a)–e);
art. 34.2 RGAT a), b), b) second paragraph (row with an empty Elemento cell), c); art. 54 RGAT a)–i); art. 4.1 RD 1676/2009
a), b) 1.º–3.º, c)–e). All are in the norm's order. In the art. 164 LIVA esquema, the two «6.º)» paragraph rows sit
between 6.º and 7.º.

PASS 18 · FAIL 1
