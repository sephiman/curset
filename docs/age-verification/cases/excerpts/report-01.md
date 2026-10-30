# Report 01 — case excerpts R4 (batch-01, items 1–60)

| n | key | verdict | note |
|---|---|---|---|
| 1 | sp-01/q21 | yes | twenty days present; their kind (hábiles) comes from art. 30.2 LPAC, not in excerpt |
| 2 | sp-01/q41 | yes | ten days present; hábiles from art. 30.2 LPAC |
| 3 | sp-01/q43 | yes |  |
| 4 | sp-01/q24 | yes |  |
| 5 | sp-01/q25 | yes | three months present; prórroga to next hábil day is art. 30.5 LPAC |
| 6 | sp-01/q26 | no | text cut at 159.4.f) 3.º; the seven días hábiles to constitute the garantía are in 4.º of the same letter; excerpt_full null (unit too long) |
| 7 | sp-01/q27 | yes |  |
| 8 | sp-01/q28 | yes |  |
| 9 | sp-01/q29 | yes |  |
| 10 | sp-01/q30 | yes | thirty days present; naturales from DA 12.ª LCSP |
| 11 | sp-01/q31 | yes |  |
| 12 | sp-01/q32 | yes |  |
| 13 | sp-01/q33 | yes |  |
| 14 | sp-01/q34 | yes |  |
| 15 | sp-01/q35 | yes |  |
| 16 | sp-01/q42 | yes |  |
| 17 | sp-01/q37 | yes |  |
| 18 | sp-01/q38 | full-only | text (56.4) says the limits apply to the whole ejercicio but not the President's 10 % / 500.000 € limit the key subtracts from; that is art. 56.3.a), in excerpt_full |
| 19 | sp-01/q39 | yes |  |
| 20 | sp-01/q40 | yes |  |
| 21 | sp-02/q21 | yes |  |
| 22 | sp-02/q22 | yes |  |
| 23 | sp-02/q03 | yes |  |
| 24 | sp-02/q04 | yes |  |
| 25 | sp-02/q05 | yes |  |
| 26 | sp-02/q06 | yes |  |
| 27 | sp-02/q07 | yes |  |
| 28 | sp-02/q08 | yes |  |
| 29 | sp-02/q26 | yes | thirty days present; naturales from DA 12.ª LCSP |
| 30 | sp-02/q10 | yes |  |
| 31 | sp-02/q24 | yes |  |
| 32 | sp-02/q12 | yes |  |
| 33 | sp-02/q13 | yes |  |
| 34 | sp-02/q14 | yes |  |
| 35 | sp-02/q15 | yes |  |
| 36 | sp-02/q25 | yes |  |
| 37 | sp-02/q17 | yes | 0,26 €/km present; FLAG garbled: BOE page header/footer («Núm. 169 Lunes 17 de julio de 2023 Sec. I. Pág. 103029 cve: BOE-A-2023-16462 Verificable en https://www.boe.es») inside the sentence |
| 38 | sp-02/q18 | yes |  |
| 39 | sp-02/q19 | yes |  |
| 40 | sp-02/q20 | yes |  |
| 41 | sp-03/q21 | yes |  |
| 42 | sp-03/q22 | yes | three months present; prórroga is art. 30.5 LPAC |
| 43 | sp-03/q23 | yes | ten days present; hábiles from art. 30.2 LPAC |
| 44 | sp-03/q24 | yes | twenty days present; hábiles from art. 30.2 LPAC |
| 45 | sp-03/q25 | full-only | text gives four years for «la causa a) del apartado anterior» without saying it is the error de hecho; that is in art. 125.1.a), shown in full |
| 46 | sp-03/q26 | yes |  |
| 47 | sp-03/q27 | yes |  |
| 48 | sp-03/q28 | yes |  |
| 49 | sp-03/q29 | no | text cut at 159.6.d); «no se requerirá la constitución de garantía definitiva» is in letter f) of the same apartado; excerpt_full null |
| 50 | sp-03/q30 | yes |  |
| 51 | sp-03/q31 | yes |  |
| 52 | sp-03/q32 | yes |  |
| 53 | sp-03/q33 | yes |  |
| 54 | sp-03/q34 | yes |  |
| 55 | sp-03/q35 | yes |  |
| 56 | sp-03/q36 | yes |  |
| 57 | sp-03/q37 | yes |  |
| 58 | sp-03/q38 | yes |  |
| 59 | sp-03/q39 | yes |  |
| 60 | sp-03/q40 | yes |  |

Totals: yes 56, full-only 2, no 2.

## Misses by cause

- **Cut before the fact, excerpt_full null (unit too long)** — 6 `sp-01/q26` (art. 159.4.f) 4.º), 49 `sp-03/q29` (art. 159.6.f)). The extractor takes the head of a long apartado/letter instead of the sub-item the key needs; for 159.6 the cited unit is the apartado, so the excerpt should reach the letter the explanation names.
- **Cross-reference left unresolved** — 45 `sp-03/q25`: art. 125.2 says «causa a) del apartado anterior»; the reader needs art. 125.1.a) (error de hecho), present only in excerpt_full.
- **Cited apartado holds only half the rule** — 18 `sp-01/q38`: art. 56.4 LGP aggregates the limits; the 500.000 € figure is in art. 56.3.a), only in excerpt_full.

## Flags

- **Garbled**: 37 `sp-02/q17` (Orden HFP/793/2023 art. 1) — BOE page header, cve and «Verificable en» footer inside the sentence.
- **Kind of day / computation rule outside the excerpt** (judged yes per spec, since the plazo is there; noted for the coordinator): 1, 2, 43, 44 (días hábiles by art. 30.2 LPAC), 10, 29 (días naturales by DA 12.ª LCSP), 5, 42 (prórroga by art. 30.5 LPAC).
