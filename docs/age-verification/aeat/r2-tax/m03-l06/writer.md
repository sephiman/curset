# Writer notes: m03-l06 (III.6, Declaraciones; autoliquidaciones; comunicaciones de datos; pagos a cuenta)

## 1. Sources
- LGT `BOE-A-2003-23186_lgt_2024-12-21.pdf`: arts. 23, 98.1, 98.3, 119–122.
- LIRPF `BOE-A-2006-20764_lirpf_2026-11-11.pdf`: arts. 99, 101 (100 read, not used).
- RIRPF `BOE-A-2007-6820_rirpf_2026-10-07.pdf`: arts. 74–77 read; 75, 76, 108.1, 109–112 used (110.1 as a pointer only).
- LIS `BOE-A-2014-12328_lis_2026-09-02.pdf`: arts. 40–41.
- Orden EHA/586/2011 `BOE-A-2011-4948_orden-eha-586-2011-modelo-111_2011-03-18.pdf`: title and art. 1.1 (present in `normativa.yaml`).

## 2. Pack questions (coverage 8 of 8 stated; whole pack 12 of 18 stated)
| id | lesson section |
|---|---|
| 2025-13 | Rectificación de las opciones (art. 119.3 LGT) |
| 2025-15 | Importe de los pagos a cuenta, table (art. 101.8 LIRPF; the distractors: 101.3 cursos 15 %, 101.5.a) profesionales 15 %, 101.5.b) agrícolas 2 %) |
| 2025-65, 2022-89 (ref) | Obligados a practicar retención e ingreso a cuenta (art. 99.2 LIRPF) |
| 2024-5, 2023-91, 2021-59 (ref) | Rentas sujetas (art. 75.1–3 RIRPF; letras b, c, d, g and the 300 euros of f) |
| 2024-40, 2022-45 (ref) | El pago fraccionado del IS (art. 40.1 LIS) |
| 2024-78 | art. 112 RIRPF |
| 2023-64 | Declaración e ingreso de las retenciones (art. 1.1 Orden EHA/586/2011, by the title) |
| 2021-61 (ref) | Importe de los pagos a cuenta, table (arts. 101.1, 101.3, 101.4, 101.8) |
| 2024-18, 2024-61, 2023-95 (ref) | no está: tema III.3 (art. 27 LGT) |
| 2023-54, 2022X-49, 2020-74 (ref) | no está: fuera de temario (declaraciones informativas) |

## 3. Lo que más cae
Fewer than ten coverage facts (8); two lines use reference questions. 1 art. 99.2 LIRPF: 2025-65, 2022-89. 2 art. 75.3.c) RIRPF: 2024-5, 2021-59. 3 art. 75.3.d) RIRPF: 2023-91. 4 art. 40.1 LIS: 2024-40, 2022-45. 5 art. 101.8 LIRPF: 2025-15, 2021-61. 6 art. 119.3 LGT: 2025-13. 7 art. 112 RIRPF: 2024-78. 8 art. 1.1 Orden EHA/586/2011: 2023-64. 9 art. 101.3 LIRPF: 2021-61 (reference). 10 art. 101.1 LIRPF atrasos: 2021-61 (reference).

## 4. Worked examples
None (the plan lists none).

## 5. Course summary
La declaración tributaria es todo documento presentado ante la Administración donde se reconozca o manifieste un hecho relevante para la aplicación de los tributos. La autoliquidación y la comunicación de datos son declaraciones, y pueden presentarse complementarias o sustitutivas. Los pagos a cuenta son las retenciones, los ingresos a cuenta y los pagos fraccionados, con su regulación en el IRPF y en el IS.

## 6. Glossary proposals
```yaml
- id: g-declaracion-tributaria
  es: declaración tributaria
  origin: m03-l06
  definition: {es: «Todo documento presentado ante la Administración tributaria donde se reconozca o manifieste la realización de cualquier hecho relevante para la aplicación de los tributos» (art. 119.1 LGT).}
- id: g-autoliquidacion
  es: autoliquidación
  origin: m03-l06
  definition: {es: Declaración en la que el obligado tributario, además de comunicar los datos necesarios para la liquidación, realiza por sí mismo las operaciones de calificación y cuantificación necesarias para determinar e ingresar la deuda tributaria o determinar la cantidad que resulte a devolver o a compensar (art. 120.1 LGT).}
- id: g-comunicacion-de-datos
  es: comunicación de datos
  origin: m03-l06
  definition: {es: «La declaración presentada por el obligado tributario ante la Administración para que ésta determine la cantidad que, en su caso, resulte a devolver» (art. 121 LGT).}
```

## 7. Unresolved, left out, ambiguities
- cites.py: 0 unresolved.
- RDL 29/2026 changed arts. 75 and 76 RIRPF (`normativa.yaml`, `r1/rdl-29-2026-revert-list.md`); the revert list does not say which letters. The lesson marks arts. 75.1, 75.3 and 76.1 «redacción del Real Decreto-ley 29/2026, convalidación pendiente» and states 75.3 «entre otras», without letters h)–k) (Cuentas de Ahorro e Inversión Financia Europa). The verifier should check the marks against the earlier wording, which is not in the snapshot.
- Left out: the scale and the 60 % reduction for Ceuta y Melilla of art. 101 LIRPF; arts. 99.3, 99.5–6, 99.8–11 and 100 LIRPF; RIRPF arts. 77–107 and 110.1–3 detail; LIS DA 14.ª (pago fraccionado mínimo) and the 24 % rates, not asked; letra f) of art. 75.3 RIRPF names the Real Decreto-ley 16/1977, shortened to «la normativa estatal y autonómica sobre el juego»; art. 99.2 LIRPF second paragraph (entidades vinculadas) and the fondos de pensiones de la UE, not asked.
- The LIS percentage of 18 % (art. 40.2) is stated as the article says; art. 40.4 allows the Ley de Presupuestos to change it and no cifras_anuales record exists.
