# Re-check 2 — `m03-l15` (blind)

Verifier: opus, 2026-11-11. Sources: LIRPF snapshot (`BOE-A-2006-20764_lirpf_2026-11-11.pdf`: arts. 3.2, 7.a), 14.2.d), 18.2, 85.1 with the «Redacción anterior» printed under it); RDL 29/2026 (`BOE-A-2026-20823_rdl-29-2026_2026-10-07.pdf`), art. 6.tercero («Con efectos desde 1 de enero de 2027»), Dos (new art. 85.1: scale 1,1 / 1,5 / 2 / 3 % on the sum of valores catastrales); `normativa.yaml` LIRPF entry (`cambios_pendientes`: art. 85.1); spec rule on unconvalidated RDLs (text in force plus the mark, nothing else); the revert list. Pending line numbers match the current file.

The art. 85.1 sentences at l. 268, 270 and 274 and the example steps at l. 280, 282 and 283 state the «Redacción anterior», which is the wording in force in 2026, with the plain citation. The l. 270 sentence on the 2027 wording carries only the mark and states nothing of the new content, within the spec's «nothing else about them».

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `9f982c9f0d` | PASS | art. 7.a) LIRPF | word for word; the list is introduced as «entre otras» (l. 31) | — |
| `cd43b093d0` | PASS | art. 14.2.d) LIRPF | option, the more-than-one-year condition, the efectos cambiarios rule and the rentas vitalicias o temporales exclusion all match | — |
| `86d0193b7c` | PASS | art. 18.2 LIRPF | 30 %, more than two years or notoriously irregular, single period, five-period exclusion and the extinción de relación laboral carve-out of the second paragraph all match | — |
| `af3dbb30cf` | PASS | art. 85.1 LIRPF (wording in force, «Redacción anterior») | first paragraph of the wording in force: 2 % on the valor catastral, proportional to days | — |
| `e965df0f1c` | PASS | art. 85.1 LIRPF (wording in force) | second paragraph: 1,1 % when the values entered into force in the period or the ten prior periods | — |
| `7843caf2ae` | PASS | art. 85.1 LIRPF (wording in force) | third paragraph: 1,1 % on 50 % of the greater of the two values | — |
| `c0181cab92` | PASS | art. 85.1 LIRPF | fourth paragraph; same in both wordings | — |
| `b523d7905b` | PASS | RDL 29/2026, art. 6.tercero.Dos; art. 85.1 LIRPF | the RDL rewrites art. 85.1 «con efectos desde 1 de enero de 2027»; mark matches `normativa.yaml` (pendiente de convalidación); states nothing of the new content | — |
| `14f8fcf91b` | PASS | art. 85.1 LIRPF (wording in force) | «generadores de rendimientos del capital» are excluded from imputation | — |
| `67818a41b0` | PASS | art. 85.1 LIRPF (wording in force) | the conditions of the first paragraph, applied to the second home of the example | — |
| `4c090e9c1f` | PASS | art. 85.1 LIRPF (wording in force) | 90.000 × 0,011 = 990, recomputed; the 1,1 % rests on step 2 (DA 55.ª, values in force since 01-01-2019) | — |
| `b57c5547f1` | PASS | art. 85.1 LIRPF (wording in force) | 2026 is not a leap year: 365 days, full year of ownership, no prorrateo | — |
| `bd308d9b59` | PASS | art. 3.2 LIRPF | art. 3.2 names art. 46 of Ley 22/2009; l. 11 names it in prose with «(art. 3.2 LIRPF)» | — |

PASS 13 · FAIL 0
