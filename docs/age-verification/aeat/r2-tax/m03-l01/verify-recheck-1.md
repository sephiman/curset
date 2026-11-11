# Verification re-check 1 — `m03-l01` (blind)

Verifier: opus, 2026-11-11. Sources: snapshot PDFs in `content/aeat-agentes-hacienda/sources/normativa/` (LIRPF, LIS, LIVA, TRLIRNR, Ley 19/1991, Ley 29/1987, TRLITPAJD, Ley 38/1992, Ley 38/2022, Convenio Económico) and `normativa.yaml` (`short`, `title`). `pending.md` announces 7 sentences but lists 6 rows; the 6 listed are checked. The 31.1 CE replacement (`6532f9aaa3`) is now in «Lo que más cae» (line 191) word for word as art. 31.1 CE.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `7d9c48f1b0` | PASS | titles in `normativa.yaml`; art. 1 of each law, art. 3 Ley 38/2022 | every full title matches `title`; «la fija su propia ley» is true for all nine (the ITSGF in art. 3 Ley 38/2022) | — |
| `10e558e720` | PASS | art. 1 Convenio Económico («Potestades de Navarra») | art. 1 cited in the prose (line 160); heading matches | — |
| `15b48a0d6f` | PASS | art. 1 LIS («Naturaleza») | cited at line 39 | — |
| `069f2eff7b` | PASS | art. 1 LIVA, letras a)–c) | cited at line 43 (art. 1 and art. 1.a)–c)) | — |
| `b3c620aa0b` | PASS | art. 1 TRLIRNR («Naturaleza y objeto») | cited at line 47 | — |
| `5004d40e19` | PASS | art. 1 Ley 19/1991 («Naturaleza y objeto del Impuesto») | cited at line 51 | — |
| `d664f68b9c` | PASS | art. 1 Ley 29/1987 («Naturaleza y objeto») | cited at line 55 | — |

Every norm named in the prose has its «Normativa» line; no line ends in a bare «art. N.»; no cited precept has a cambio pendiente.

PASS 6 · FAIL 0
