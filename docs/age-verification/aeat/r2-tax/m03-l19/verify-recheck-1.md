# Verification re-check 1 — `m03-l19` (blind)

Verifier: opus, 2026-11-11. Source: LIVA snapshot (`BOE-A-1992-28740_liva_2026-10-07.pdf`: arts. 75, 78, 80, 84, 89, 93, 95, 96, 103 and 104). Input: `m03-l19/pending.md` (11 sentences); line numbers match the current file. For the «Normativa» line: every parenthetical LIVA citation above «## Normativa» was extracted and matched against the list, both ways. Running-text references inside restated rules («artículo 7.8.º», «artículo 21», «artículo 25», «artículo 71», «artículo 121» and others) are read as named, not cited, the same reading the `m03-l18` block uses; LIVA itself is listed.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `1a72a4fe35` | PASS | art. 75.Uno LIVA | the list gives 1.º–5.º and 7.º; 2.º bis and 8.º are left out (6.º suprimido), so «entre otros supuestos» is right | — |
| `153a903540` | PASS | art. 78.Dos.1.º LIVA | the three paragraphs of 1.º after the first are all kept: interest for the later period excluded, only exempt interest (20.Uno.18.º c)) shown separately in the invoice counts, never the excess over the market rate | — |
| `08a0b6318b` | PASS | art. 80.Cinco.2.ª LIVA | rule and its exception (insolvency declared by a court of another Estado miembro); «en los términos que fija el propio número» covers the Reglamento (UE) 2015/848 condition; «Tampoco» is not on the opener blacklist | — |
| `a2dbf9f86a` | PASS | art. 84.Uno.2.º LIVA | the list of l. 100–106 gives all of letters a)–g), so no «entre otros» is owed; «Esos supuestos…» keeps the noun, not the «Eso + verb» tic | — |
| `45d11a06fc` | PASS | art. 89.Uno y 89.Tres LIVA | duty of 89.Uno with the two cases of 89.Tres (1.º and 2.º); «sin fichero» in `pending.md` is the parser not resolving «89.Uno y Tres», not a content defect | — |
| `cb42bef056` | PASS | art. 93.Cinco LIVA | criterio razonable y homogéneo, kept in time save causas razonables, and the last paragraph (gestión de servicios públicos, art. 78.Dos.3.º a)) all present; the next sentence carries the «no serán deducibles en proporción alguna» paragraph | — |
| `72ca62005d` | PASS | art. 96.Uno.5.º LIVA | both exclusions of 5.º (a) muestras and objetos publicitarios of art. 7.2.º and 4.º; b) goods for onerous delivery later used for atenciones) kept | — |
| `9c52a85663` | PASS | arts. 80.Cuatro.A y 80.Cinco.1.ª LIVA | conditions 1.ª–4.ª all present, with «cualquier otro medio que acredite fehacientemente la reclamación», the 6.010.121,04 euros of the año natural inmediato anterior and «exceda de 50 euros» (= «superior a 50 euros», base IVA excluido); the vinculadas case is stated as one case, not as the list | — |
| `787bc30905` | PASS | arts. 93.Cuatro y 95.Tres.2.ª LIVA | 93.Cuatro literal in substance; 50 por 100 for turismos; the 100 por 100 list is a)–f) and the sentence gives b), c) and e) under «entre otros» | — |
| `365ae5a856` | PASS | arts. 103.Dos.2.º, 104.Dos y 104.Tres.3.º LIVA | 10 por ciento o más; 104.Tres.3.º now reads «entregas y exportaciones de los bienes de inversión que el sujeto pasivo haya utilizado en su actividad»; rounding to the unidad superior is 104.Dos | — |
| `3d14d8248e` | PASS | Normativa LIVA | every listed apartado is cited in the prose (89.Tres via l. 122; 93.Tres absent from both); every parenthetical citation falls inside the list (9.1.º c) at l. 209/216, 20.Uno.26.º at l. 270, 108.Dos.5.º and 109.1.º–3.º inside 108.Uno–Dos and 109); no RDL 29/2026 precept (20.Uno.23.º, 91) is cited, so no cambio-pendiente note is owed | — |

PASS 11 · FAIL 0
