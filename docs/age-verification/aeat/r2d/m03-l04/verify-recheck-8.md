# Verify re-check 8 — `m03-l04` (R2d, blind, Opus)

2026-11-18. Rows from `pending.md` (6), read as they stand in the lesson (all ids current). Sources: RGAT
`BOE-A-2007-15984_rgat_2026-10-07.pdf`, RD 1619/2012 `BOE-A-2012-14696_..._2026-03-31.pdf`, RIVA
`BOE-A-1992-28925_riva_2026-02-28.pdf`, LIVA `BOE-A-1992-28740_liva_2026-10-07.pdf`; `normativa.yaml` entries for RGAT,
RD 1619/2012, RIVA, LIVA and RDL 29/2026. Normativa lines checked both ways against every parenthetical / «Cita» citation of
the lesson (lines 1–2189) and every article of the norm named inside other norms' copied text.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `013684e651` | PASS | art. 8.2 RGAT | First half of art. 8.2 párr. 1 in the article's words, TRLIRNR spelled out with its approving RDL as the article does; «actividades claramente diferentes», «gestión … separado», «mismos datos … mismas condiciones» kept; the second half follows in the next sentence of the paragraph | — |
| `6a1f5093b5` | PASS | art. 2.2.f) RD 1619/2012 | Verbatim (only «Impuesto» lower-cased); art. 2.2 not touched by the RD 238/2026 deferred changes (arts. 8.1, 8 bis, 9, 10) | — |
| `952d852cc1` | PASS | art. 37 bis.1 RGAT; LGT | Line 863 copies art. 37 bis.1 RGAT, which names «artículos 1.2 y 29.bis» LGT; 29 bis is in the main LGT line, 1.2 nowhere else. Every other LGT article named inside RGAT/RD 1619/other copied text (35, 35.4, 35.6, 40, 46.2, 46.5, 48.3, 84, 93, 94, 94.1–2, 95, 104, 114, 219, 29.2.j), DA 5.ª and 6.ª) is in the main LGT line; 26, 148, 150.4, 175, 176, 188.3, 221 appear only inside LGT's own text | — |
| `a96d7bded6` | PASS | RGAT citations, lines 37–2188 | Every cited RGAT article/apartado (incl. 3.2.a), 4.2.l), 5.a)–c), 59.2.b), arts. 19.2 y 20.2) falls in the list and every listed item is cited; RGAT is named in other norms' text only at 1077 (title, inside art. 54 ter.1 RGAT itself). The following sentence's RDL 29/2026 note (art. 39 quater, in force 08-10-2026, convalidated 12-11-2026, BOE-A-2026-23755) matches `normativa.yaml` | — |
| `092e9b3b01` | FAIL | RIVA citations; arts. 3.4, 5.b), 10.2 RGAT; art. 6.1 RD 1619/2012 | Cited part right (40.1, 61.1–3, 62.1–6, 62 bis.1–2, 63.1, 64.1, 65.1, 66.1, 67, 68.1–4, 68 bis, 69.1–5, 69 bis.1, 70.1, 71.3; 40.1, 62.6 and 69 named in RGAT/RD 1007/RD 1619 text are inside those ranges). Art. 30 RIVA is also named in art. 10.2 RGAT (line 303, letter k): «Registro de devolución mensual a que se refiere el artículo 30 del Reglamento del Impuesto sobre el Valor Añadido»), which the line omits | RIVA (RD 1624/1992): arts. 40.1, 61.1–3, 62.1–6, 62 bis.1–2, 63.1, 64.1, 65.1, 66.1, 67, 68.1–4, 68 bis, 69, 69 bis.1, 70 y 71.3; art. 30, nombrado en los arts. 3.4, 5.b) y 10.2 RGAT; art. 61 quinquies.2 y disposición adicional quinta, nombrados en el art. 6.1 RD 1619/2012. |
| `46445daa2e` | PASS | LIVA citations (164–166) and LIVA articles named in RGAT, RIVA and RD 1619/2012 text | Every item named in the lesson is listed (incl. 20.Uno.2.º…28.º and 20.uno.16.º/18.º under «20», 84.uno.2.º e) under «84.uno», 68.Tres.a) under «68.tres.a) y cinco», capítulos IX, X, XI título IX, anexo quinto) and every listed item occurs. The following «Cambio pendiente» sentence (RDL 29/2026 art. 7, efectos 01-12-2026, art. 20.Uno.23.º e´)) matches `normativa.yaml`; art. 91 is not cited, so not needed | — |

Out-of-scope observation (no pending row): the final «no figuran» line does not list the «Acuerdo Multilateral entre
Autoridades competentes … en el ámbito de la OCDE» named in art. 54 ter.1 RGAT (line 1077).

PASS 5 · FAIL 1
