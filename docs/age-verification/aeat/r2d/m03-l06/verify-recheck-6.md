# Verify re-check 6 — `m03-l06` (R2d, blind, Opus)

2026-11-18. Rows of `pending.md` read against the lesson as it stands (all ten ids unchanged) and the RIRPF (BOE-A-2007-6820), RIS (BOE-A-2015-7771) and TRLIRNR (BOE-A-2004-4527) PDFs in `sources/normativa/`; Normativa lines checked both ways against every citation and every norm named in lines 1–916 and against `normativa.yaml`.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `e74f7134ce` | PASS | art. 89.B).1 RIRPF, párrafo segundo | All data of the comunicación, «superior a ciento ochenta y tres días», the count from «comienzo de la prestación del trabajo» and «durante el año natural … o, en su defecto, en el siguiente» kept. | — |
| `d40e86bcc4` | PASS | art. 91.4 RIRPF, último párrafo | «deuda pública con rendimiento mixto, cuyos cupones e importe de amortización se calculan con referencia a un índice de precios» → 40 por ciento in place of the first paragraph's 80 por ciento; matches. | — |
| `bf3eff88af` | PASS | art. 92.6 RIRPF | Subrogation in the valor de adquisición with «en tanto medie una justificación suficiente del referido coste»; «A los efectos previstos en este artículo» rendered as «del artículo 92 RIRPF». | — |
| `659f44aab0` | PASS | art. 62.7 RIS, párrafo segundo | Directiva 2009/65/CE IIC, EU domicile, CNMV registration for marketing by residents, comercializadoras/intermediarios and subsidiarily the colocación/distribución entities «que intervengan en el pago de las rentas»; matches. | — |
| `568c311241` | PASS | art. 62.7 RIS, párrafo tercero | Equivalent organismos registered in another State, «con independencia de cualquier limitación …», adquisición/cesión/rescate, entidad depositaria or gestión de cobro; matches. | — |
| `a84b041048` | PASS | art. 62.7 RIS, párrafo cuarto | Subsidiary pago a cuenta by the socio o partícipe under arts. 64.8, 65.1 and 66 RIS; matches. | — |
| `2f75d070ed` | PASS | art. 63.3 RIS, último párrafo | Same 40 por ciento rule as RIRPF 91.4; matches RIS wording. | — |
| `9a85f68070` | PASS | art. 63.4 RIS | Both paragraphs: acreditación of prior acquisition and price; instrumento de giro first endoso through fedatario/institución financiera «salvo que el mismo endosatario o adquirente sea una institución financiera»; consignación of its character and first holder. | — |
| `a392db6194` | PASS | Normativa: TRLIRNR | Cited: 23.1, 23.2, 31.1, 31.3, 31.4. Named inside other norms' text: 24.2 (99.2 LIRPF, 76.2 RIRPF), 32 (89.B) RIRPF), 14.1.h) (61 RIS); inside TRLIRNR's own text: 5.c), 30, 14, 14.1.d), 31.5. All listed; nothing cited is missing. | — |
| `ea92f4d528` | PASS | Normativa: named norms | Every norm named in the prose and absent from `normativa.yaml` is listed (Ley 35/2003 also as «Ley de Instituciones de Inversión Colectiva»; Ley 6/2023 also as «Ley de los Mercados de Valores y de los Servicios de Inversión»; TRLIS in 99.2 LIRPF, 76.2 RIRPF, 31.4.d) TRLIRNR), each «nombrada en» place checked (lines 155, 157, 181, 185, 301, 336, 346, 349, 671–679, 759, 773, 786–795, 825–830, 858, 902); none is in `normativa.yaml` (the yaml's «RDL 6/2023» is a different norm). Not blocking: arts. 55.7 and DA 2.ª Ley 35/2003 are also named in art. 100.1 LIRPF and art. 76.2 RIRPF, which the line attaches only to the second group. The RDs inside the official titles of the RIRPF and RIVA (304/2004, 1041/1990, 338/1990, 2402/1985, 1326/1987) are read as part of those titles. | — |

PASS 10 · FAIL 0
