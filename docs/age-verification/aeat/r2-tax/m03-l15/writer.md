# Writer notes: m03-l15 (III.15, IRPF I)

## 1. Sources
All from `content/aeat-agentes-hacienda/sources/normativa/`, read as `pdftotext -layout`.
- LIRPF `BOE-A-2006-20764_lirpf_2026-11-11.pdf`: arts. 1–14, 16–20, 21–26, 27–32, 33–39, 42–43, 85, DA 55.ª (art. 85.1 and art. 24 read with their «Redacción anterior»).
- RDL 29/2026 `BOE-A-2026-20823_rdl-29-2026_2026-10-07.pdf`, art. 6: primero (DA 55.ª), segundo Uno (7.ñ), Dos (23.2), Tres (67.1), Cuatro (68.6), tercero Uno–Dos (arts. 24, 85.1).
- RIRPF `BOE-A-2007-6820_rirpf_2026-10-07.pdf`: arts. 2.1, 14.1–3.
- Orden HAC/1425/2025 `BOE-A-2025-25272_...pdf`: arts. 3.1.a)–b), DA 1.ª–3.ª. Orden HAC/1161/2026 `BOE-A-2026-23174_...pdf`: DA 1.ª, 4.ª.
- LGT `BOE-A-2003-23186`: art. 35.4 (only to confirm the wording).

## 2. Pack questions (coverage 22 of 22 stated; whole pack 32 of 32 stated or explained)
| id | lesson section |
|---|---|
| 2025-7 | Rendimientos del trabajo en especie (art. 43.1.1.º a), b), c)) |
| 2025-31 | Estimación objetiva (arts. 31.1.1.ª, 31.1.5.ª; 30.2.4.ª and 30.2.5.ª.c) are in Estimación directa, as the distractors) |
| 2025-71 | Rendimiento neto (art. 19.2.d)) |
| 2024-16 | Rentas exentas (arts. 7.f), 7.ñ), 7.x); herencia: art. 6.4) |
| 2024-44 | Rendimientos del capital mobiliario (art. 25.3; 17.2.d), 17.2.e) in trabajo) |
| 2024-70 | Rentas en especie (arts. 42.2.b), 42.3) |
| 2023-1, 2022-83, 2020-80 (ref) | Rendimiento neto (art. 19.2.f)) |
| 2023-45, 2021-95 (ref) | Ganancias y pérdidas (arts. 33.3.b), 33.4.b), 33.4.d), 33.5) |
| 2023-55 | Rentas exentas (art. 7.z); the question's letter in the pack is h) but the snapshot has the wording in z)) |
| 2023-61 | Rentas exentas (art. 7.g); the pack says f) |
| 2023-69 | Imputación temporal (art. 14.2.a)) |
| 2023-81 | Reducciones (art. 32.3) |
| 2022-79 | Concepto y métodos (arts. 16.2–3) |
| 2022-80, 2020-85 (ref) | Rentas exentas (art. 7.r), 7.d); 7.i) not listed: not asked as a coverage fact, left out) |
| 2022-81 | Período impositivo y devengo (arts. 12–13) |
| 2022-84 | Ganancias y pérdidas (art. 33.5.e)) |
| 2022-85 | Imputación de rentas inmobiliarias (arts. 85.1, 85.3) |
| 2022X-87 | Rentas exentas, becas (art. 7.j) LIRPF; art. 2.1 RIRPF) |
| 2022X-94 | Rendimientos íntegros (art. 17.1.d)) |
| 2022X-95 | Rendimientos del capital mobiliario (arts. 25.1, 25.4, 25.5) |
| 2022X-96, 2021-100 (ref) | Rendimientos del capital inmobiliario (art. 23.1.a), 23.1.b); RIRPF 14.2.a)) |
| 2025-53 (ref) | Imputación de rentas inmobiliarias (art. 85.1, text up to 31-12-2026) |
| 2023-53 (ref) | Rendimientos del capital inmobiliario (art. 23.2.a).1.º, 90 %) |
| 2021-99 (ref) | Rendimiento neto del trabajo (art. 19.2.a)–f); pensiones compensatorias are not in the list) |
| 2021-60 (ref) | no está: DA 33.ª (gravamen especial de loterías), not in the programme |
| 2023-11, 2022X-43 (ref) | no está: tema III.4 (libros registro, art. 68 RIRPF) |

## 3. Lo que más cae
1 art. 19.2.f) traslado: 2023-1. 2 art. 19.2.f) 3.500/7.750: 2022-83, 2020-80. 3 art. 19.2.d): 2025-71, 2021-99. 4 art. 7.g): 2023-61, 2020-85. 5 art. 7.x): 2024-16. 6 art. 7.z): 2023-55. 7 art. 7.r): 2022-80. 8 art. 7.j)/RIRPF 2.1: 2022X-87. 9 art. 14.2.a): 2023-69. 10 art. 33.4.d): 2023-45. Cut for the ten-line limit (stated in the body): 25.1, 25.3, 17.1.d), 42.2.b), 43.1.1.º.c), 31.1.5.ª, 32.3, 33.5.e), 85.3, 16.2, 12–13, RIRPF 14.2.a).

## 4. Worked examples
One: imputación of a property at 1,1 % in 2026 (valor catastral 90.000 euros, 365 days, result 990 euros). Arithmetic: 90.000 × 0,011 = 990 (checked with `python3 -c "print(90000*0.011)"`). Year 2026 has 365 days (`datetime.date(2026,12,31).timetuple().tm_yday`). No weekday or deadline is involved.

## 5. Course summary
El IRPF grava la renta de las personas físicas: rendimientos del trabajo, del capital y de actividades económicas, ganancias y pérdidas patrimoniales e imputaciones de renta. La LIRPF regula quién es contribuyente, las rentas exentas, el período impositivo y el devengo, y cómo se calcula cada clase de renta. El artículo 85 LIRPF imputa renta a los inmuebles no afectos ni arrendados, con los porcentajes en vigor en 2026.

## 6. Glossary proposals
```yaml
- id: g-renta-en-especie
  es: renta en especie
  origin: m03-l15
  definition: {es: «La utilización, consumo u obtención, para fines particulares, de bienes, derechos o servicios de forma gratuita o por precio inferior al normal de mercado, aun cuando no supongan un gasto real para quien las conceda» (art. 42.1 LIRPF).}
- id: g-ganancias-y-perdidas-patrimoniales
  es: ganancias y pérdidas patrimoniales
  origin: m03-l15
  definition: {es: «Las variaciones en el valor del patrimonio del contribuyente que se pongan de manifiesto con ocasión de cualquier alteración en la composición de aquél, salvo que por esta Ley se califiquen como rendimientos» (art. 33.1 LIRPF).}
- id: g-periodo-impositivo
  es: período impositivo
  origin: m03-l15
  definition: {es: En el IRPF, «el año natural»; es inferior al año natural cuando fallece el contribuyente en un día distinto al 31 de diciembre (arts. 12.1 y 13.1 LIRPF).}
```
`g-hecho-imponible`, `g-devengo` and `g-contribuyente` already exist.

## 7. Unresolved citations, facts left out, ambiguities
- `cites.py`: 0 unresolved. Final run: 154 citations. `tests/test_citations.py` (frozen golden `citations.es.txt`) now fails: it needs `UPDATE_CITATIONS=1` after the group; I touched no other file.
- DA 55.ª and the art. 85.1 scale: the RDL 29/2026 marks follow the spec. The lesson states art. 85.1 and art. 24 in the text in force until 31-12-2026 (the snapshot's «Redacción anterior») with «(desde 01-01-2027, …)»; the 2027 scale (1,1 % to 100.000 euros, 1,5 %, 2 %, 3 %) and the 2027 art. 24 «porcentaje medio efectivo» are NOT in the lesson ("Nothing else about them"). Decision for the coordinator: the exam of 2027 will apply the 2027 text, so the scale may have to be added if the RDL is convalidated.
- Art. 7.ñ) and 23.2 are marked as the revert list says; in the snapshot their wording shows no difference I could detect against the pre-RDL one (the RDL restates them whole); the mark follows the RDL's own «Se modifica la letra ñ» / «Se modifica el apartado 2». Art. 23.2 is summarised (range 100–15 %, the 90 % case, the rule of the greatest reduction), not listed in full.
- Art. 7: list is selective («entre otras»). Left out: 7.a–c, e (180.000 euros; it names the Estatuto de los Trabajadores, a norm not in `normativa.yaml`), h, i, k, l, m, o, p, q, s–u, w, y. Letters in the pack that do not match the snapshot: 2023-61 key B is 7.g) (pack says f), 2023-55 key C is in 7.z) (pack says h).
- 2024-16 key D wording: the question says «asistencia personalizada»; the snapshot's 7.x) says «de asistencia personal y de cuidados y apoyos en viviendas». The lesson quotes the snapshot. 7.x) was changed by Ley 4/2026 (in force, no mark).
- Estimación objetiva: the DT 32.ª text (250.000/125.000 euros for 2016–2024) is not in the snapshot PDF, so it is not cited; the 2026 limits come from art. 31.1.3.ª LIRPF and art. 3.1 Orden HAC/1425/2025. The 250.000 euros agrarian figure appears in both the LIRPF and art. 3.1.b) of the order.
- The parser does not resolve «art. 31.1.3.ª b) a´)»: cited as «art. 31.1.3.ª.b)» and the a´)/b´) letters named in the table cell.
- 2025-53 (reference) states key B with the pre-2027 text; true until 31-12-2026.
- Norms named in the articles but not in the lesson: Ley 22/2009 (kept, art. 46), Ley 39/2006, Ley 29/1994, Ley 12/2023, Catastro, Estatuto de los Trabajadores (paraphrased to avoid listing norms without article).
