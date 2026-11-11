# Verification re-check 1 — `m03-l13` (blind)

Verifier: opus, 2026-11-11. Sources: snapshot PDFs of the LGT (2024-12-21: arts. 184, 187, 191–206) and RGRST (2019-09-20: art. 7); `normativa.yaml` entries of the LGT and RGRST; lesson prose for the «Normativa» line (LGT citations extracted from the whole prose above «## Normativa», parenthetical and running-text forms, including «apartado N del artículo M»). Pending line numbers match the current file.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `809b48a216` | PASS | arts. 184.2–3, 191.3–4, 192.3–4, 193.3–4 LGT | ocultación makes the infracción grave (base > 3.000 euros) and medios fraudulentos make it muy grave in each of the three articles; the sentence does not claim they are the only determinants | — |
| `e5ec091216` | PASS | art. 7.2 RGRST | the three cases of art. 7.2: acta de conformidad, conformidad with the inspector-jefe's rectified proposal «en el plazo concedido al efecto», and express conformidad after an acta de disconformidad «antes de que se dicte el acto administrativo de liquidación» | — |
| `d45dd16042` | PASS | art. 192.3 LGT | base > 3.000 and ocultación; «cualquiera que sea la cuantía de la base» the two supuestos a) and b) word for word («facturas, justificantes o documentos falsos o falseados, sin que ello sea constitutivo de medio fraudulento»; >10 % and ≤50 %); 50 to 100 per cent graduated with the increments of art. 187.1.a and b | — |
| `962da40ea7` | PASS | art. 193.3 LGT | «será grave cuando la base de la sanción sea superior a 3.000 euros y exista ocultación», multa del 50 al 100 por ciento; no longer phrased as a necessary condition, and the next sentence of the paragraph sends the remaining causes and the increments to art. 192 | — |
| `eaa2e18669` | PASS | art. 196.1 LGT | narrowing clause restored: no infracción for the part of the bases or resultados that gave rise to a sanction on the entity under arts. 191, 192 or 193 | — |
| `e63e74d1fc` | PASS | art. 197.1 LGT | narrowing clause restored for the cantidades incorrectamente imputadas | — |
| `18c29d393b` | PASS | art. 198.1 LGT | leve; documents of the obligaciones aduaneras included; 200 euros, 400 for declaraciones censales and the designation of representative «cuando así lo establezca la normativa»; 20 euros per dato or conjunto de datos for the declaraciones of arts. 93 and 94, mínimo 300, máximo 20.000 | — |
| `44dc5e98e9` | PASS | arts. 199, 200, 201, 201 bis, 202, 203, 204, 205, 206 LGT | each item matches the article's heading, in order; 201 bis now included (art. 206 bis lies outside «199 a 206») | — |
| `ec37bf58de` | PASS | LGT (Ley 58/2003) | both directions hold: every listed article is cited in the prose (42 via «párrafos a) y c) del apartado 1 y … apartado 2 del artículo 42», 43 via «apartado 1 del artículo 43», 156.3 and 161.1.b via the «apartado/párrafo» forms, 201 bis at l. 277, 201.4 at l. 140, 202.3 at l. 106) and every LGT article cited in the prose is listed (10.2 to 212.3); no cambio pendiente; ends in «212.1–3.» | — |

Aside, outside the pending rows: the «Código Aduanero de la Unión (Reglamento (UE) 952/2013): art. 127.» line (l. 365) ends in «art. N.» alone, which the spec's list-shape rule forbids; it passed in `verify.md` (`a529120829`).

PASS 9 · FAIL 0
