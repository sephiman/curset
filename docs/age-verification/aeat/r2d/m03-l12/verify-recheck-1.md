# Re-check 1 — `m03-l12`

Blind re-check of the 5 rows of `pending.md` against the snapshot (LGT BOE-A-2003-23186 consolidated 2024-12-21, RGR
BOE-A-2005-14803 consolidated 2024-01-31). «Normativa» check: every LGT and RGR article cited in the prose is listed in
the LGT and RGR lines (art. 43.1.f LGT now listed), and every listed article is cited (art. 109 LGT as «artículos 109 y
siguientes LGT»).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `9e171bed7d` | PASS | art. 107.4.b RGR | first sentence of 107.4.b; the list under «(art. 107.4 RGR)» has the article's two criteria a) and b) | — |
| `04a2761a59` | PASS | art. 107.4.b RGR | second sentence of 107.4.b | — |
| `ca0d6f2c82` | PASS | art. 116.3 RGR | lead-in; «en el caso anterior» rendered as the 116.2 condition (importe insuficiente); the list that follows has the article's three rules a)–c) in order | — |
| `922d647da5` | PASS | art. 126.1 RGR | verbatim, with «LGT» for the full name of Ley 58/2003 | — |
| `b5a446a8a0` | PASS | «Normativa» LGT line | every listed LGT article is cited in the prose and every LGT article cited in the prose is listed, 43.1.f included; LGT has no `cambios_pendientes` in `normativa.yaml` | — |

PASS 5 · FAIL 0
