# Verification re-check 1 — `m03-l09` (blind)

Verifier: opus, 2026-11-11. Sources: snapshot PDFs of the LGT (2024-12-21: arts. 7.2, 63.3–4), RGR (2024-01-31: art. 68.2), LPAC (2024-11-06: art. 30.2), Orden HFP/311/2023 (2023-03-31: arts. 1–2, disposición derogatoria única, disposición final única); `normativa.yaml` entry of the Orden (`cifras_anuales`: 50.000 euros, no anual, desde 15-04-2023).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `051472d344` | PASS | art. 68.2 RGR | both quotations word for word («sin realizar el ingreso o sin presentar solicitud de aplazamiento, fraccionamiento o compensación»; «el mismo día de la presentación de la autoliquidación») | — |
| `38d383ed60` | PASS | art. 30.2 LPAC; art. 7.2 LGT | narrowing clause «Siempre que por Ley o en el Derecho de la Unión Europea no se exprese otro cómputo» kept; 7.2 LGT makes the general administrative law supletorio | — |
| `ccd6f6b62f` | PASS | art. 63.3 LGT | «salvo lo dispuesto en el apartado siguiente» kept as «salvo lo dispuesto en el artículo 63.4 LGT»; quotation exact. Minor: the article says «varias deudas tributarias»; the paragraph opens on «Las deudas tributarias» (63.1), so the scope is clear | — |
| `790ab75128` | PASS | art. 2 Orden HFP/311/2023 | words of the first paragraph, the trabas clause kept; the art. 1 scope (AEAT and AGE state debts, minus customs and concursal debts) is the lesson's own frame | — |
| `86e735b14f` | PASS | art. 2, second paragraph, Orden HFP/311/2023 | the step now says nothing else is accumulated, so «en conjunto» = 10.000 euros ≤ 50.000 | — |
| `794adfb41a` | PASS | Orden HFP/311/2023 | `short` right; art. 2, disposición derogatoria única and disposición final única all cited at l.153; the Orden HAP/2178/2015 (derogated, not in `normativa.yaml`) listed where it is named | — |

Not pending: the LPAC line (l.226) starts «LPAC (Ley 39/2015)», while the `short` is «Ley 39/2015 (LPAC)» (the same point was fixed in `m03-l05`). Replacement: «- Ley 39/2015 (LPAC): art. 30.2.»

PASS 6 · FAIL 0
