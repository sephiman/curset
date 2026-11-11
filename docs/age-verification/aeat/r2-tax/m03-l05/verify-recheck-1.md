# Verification re-check 1 — `m03-l05` (blind)

Verifier: opus, 2026-11-11. Sources: snapshot PDFs of the LGT (2024-12-21: arts. 86.1, 88.6, 104.1–2, 112.1), RGAT (2026-10-07: arts. 72.1, 91.5, 102.5, 103.f), 104), LPAC (2024-11-06: art. 14.2.a)); `normativa.yaml` entries of LGT, RGAT, LPAC, LEC, Código Civil, LOFCA, Concierto (Ley 12/2002) and Convenio con Navarra (Ley 28/1990). Worked example recomputed with `python3` (`datetime`): 15-01-2026 jueves; 15-07-2026 miércoles; 10-04-2026 viernes; 30-04-2026 jueves; 11–30 April 2026 = 20 días naturales; 15-07-2026 + 20 días = 04-08-2026 martes; 03-08-2026 lunes; 05-08-2026 miércoles. Step 7 now applies the second paragraph of art. 104.2 LGT to a sociedad limitada obliged to the electronic channel (art. 14.2.a) LPAC); the paper attempt is gone, the paragraph above the example (l.231) states both limbs of art. 104.2, and the result line follows from step 7: the example reads coherently.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `9efa0004de` | PASS | art. 88.6 LGT | words of the article, the narrowing «que reúnan los requisitos establecidos en virtud del apartado 2» kept | — |
| `fb6f14cb23` | PASS | art. 72.1 RGAT | letters a)–d) all present, «al menos» kept; letter c) tied to the case in which b) cannot be certified | — |
| `7ab6f206aa` | PASS | art. 91.5 RGAT | both limbs (three days from the notificación del requerimiento; before the fecha de comparecencia if the circumstance arises later) | — |
| `91b27f4f51` | PASS | art. 102.5 RGAT | only interrupciones justificadas and dilaciones, días naturales; the procedimiento inspector goes to arts. 150 LGT and 184 RGAT («tiene sus propias reglas» is true) | — |
| `1625b8d75a` | PASS | art. 103.f) RGAT | the three Juntas Arbitrales of the letter (art. 24 LOFCA, art. 66 Ley 12/2002, art. 51 Ley 25/2003) and the period, complete | — |
| `599e4b7ecb` | PASS | art. 104 RGAT | the article says «entre otras»; the lesson's a)–g) omit h) and i), and the lead-in now says the list is a selection. Style note only: «que no es una lista cerrada» follows «el reglamento», so its antecedent reads loosely | — |
| `abbc704913` | PASS | art. 104.b) RGAT | cómputo and the closing rule («se aplicará lo dispuesto en el párrafo a)») kept | — |
| `08ae560aae` | PASS | art. 104.b) RGAT | fact right; the blacklisted opener is gone | — |
| `3616c20c36` | PASS | art. 14.2.a) LPAC | «estarán obligados a relacionarse a través de medios electrónicos… a) Las personas jurídicas»; 03-08-2026 is a lunes | — |
| `0d88da34e3` | PASS | art. 104.2 LGT, second paragraph | «la obligación de notificar dentro del plazo máximo… se entenderá cumplida con la puesta a disposición de la notificación… en la dirección electrónica habilitada»; 05-08-2026 is a miércoles, after the deadline, which does not matter under that paragraph | — |
| `3398dcf051` | PASS | arts. 104.1–2 LGT (steps 1–7) | 04-08-2026 recomputed; the puesta a disposición of 03-08 meets it | — |
| `39260f4afd` | PASS | art. 112.1 LGT | «Será suficiente un solo intento cuando el destinatario conste como desconocido en dicho domicilio o lugar»; blacklisted opener gone | — |
| `f837ec721b` | PASS | art. 86.1 LGT | «dicho año» is the año precedente; now stated so | — |
| `2120cb8956` | PASS | Código Civil «Normativa» line | one norm per line, `short` «Código Civil», named in art. 106.1 LGT (l.289) | — |

Not pending, blocking: the «Normativa» block does not yet match the prose.
- LPAC line (l.355) reads «LPAC (Ley 39/2015): arts. 30.4 y 43.2.»: it lacks art. 14.2, now cited in step 7 (l.279), and starts with «LPAC (Ley 39/2015)» while the `short` is «Ley 39/2015 (LPAC)». Replacement: «- Ley 39/2015 (LPAC): arts. 14.2, 30.4 y 43.2.»
- No LEC line, although l.289 names «la Ley 1/2000, de 7 de enero, de Enjuiciamiento Civil» (the first check asked for it). Add: «- LEC (Ley 1/2000): sin artículos concretos, citada en el art. 106.1 LGT.»
- No line for the Ley 25/2003 (Convenio con Navarra modification), named with its art. 51 in letter f) (l.244). It is not in `normativa.yaml`; the nearest entry is «Convenio Económico con Navarra (Ley 28/1990)». Add a line naming it as the other lines do, e.g. «- Ley 25/2003 (modificación del Convenio Económico con Navarra): art. 51, citado en el art. 103 RGAT.», or have the coordinator decide how a norm absent from `normativa.yaml` is listed.

PASS 14 · FAIL 0
