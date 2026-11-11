# Writer notes: m03-l16 (III.16, IRPF II)

## 1. Sources
- LIRPF `BOE-A-2006-20764_lirpf_2026-11-11.pdf`: arts. 44–70 (68 headings only), 79–84, 96–98, 103.
- RDL 29/2026 `BOE-A-2026-20823_rdl-29-2026_2026-10-07.pdf`, art. 6.segundo Tres (art. 67.1) and Cuatro (art. 68.6 added).
- LGT: arts. 26.6, 31, 124–127 are cited only as art. 103.4–5 LIRPF refers to them (their text was not read: no fact beyond the reference is stated).
- RIRPF and the módulos orders: not needed for III.16.

## 2. Pack questions (coverage 14 of 14 stated; whole pack 23 of 23 stated or explained)
| id | lesson section |
|---|---|
| 2025-21 | Base liquidable general y del ahorro (art. 50.1; the distractors: arts. 18.2, 20 stated as reductions of rendimientos; art. 32.3 is in III.15) |
| 2025-69 | Deducciones por familia numerosa o discapacidad (art. 81 bis.1, 81 bis.3; the pack says 81 bis.4 for the abono anticipado, the snapshot has it in apartado 3) |
| 2025-78, 2023-59, 2022-88 | Tributación familiar (art. 82.1.1.ª y 2.ª) |
| 2024-51 | Reducciones por previsión social (art. 52.1) |
| 2024-57 | art. 81 bis.1.c), 81 bis.3, and the clause on pensionistas |
| 2024-75 | Deducción por maternidad (art. 81.1–2) |
| 2024-79, 2022-87, 2020-68 (ref) | Obligación de declarar (art. 96.2–3; example with three pagadores) |
| 2023-58, 2022X-88 | Mínimo por discapacidad (art. 60.1); Mínimo del contribuyente (art. 57.1–2) |
| 2022-86 | Clases de renta (art. 46) |
| 2022X-59, 2025-43 (ref) | Autoliquidación (art. 97.6) and Devolución (art. 103.1, 103.4; art. 31.2 LGT only as a reference) |
| 2023-30 | no está: question annulled (art. 79 is stated in full anyway) |
| 2022-82 | no está: annulled; Ley 22/2009 art. 46 (competencias normativas) is outside III.16's articles |
| 2025-15, 2025-65, 2024-5, 2023-91, 2024-78 (ref) | no está: tema III.6 (`m03-l06`) |

## 3. Lo que más cae
1 art. 82.1.2.ª: 2025-78, 2023-59. 2 art. 82.1.1.ª: 2022-88. 3 art. 81 bis.3: 2025-69, 2024-57. 4 art. 81 bis.1.c): 2024-57, 2025-69. 5 art. 96.3.a): 2024-79, 2020-68. 6 art. 96.2.c): 2022-87. 7 art. 50.1: 2025-21. 8 art. 52.1: 2024-51. 9 art. 60.1: 2023-58. 10 arts. 97.6 y 103.1: 2022X-59. Cut for the ten-line limit (stated in the body): art. 57.2 (2022X-88), art. 81.2 (2024-75), art. 46 (2022-86).

## 4. Worked examples
Four. (a) art. 48 integración: 25 % × 20.000 = 5.000; 20.000 − 5.000 = 15.000; 8.000 − 5.000 = 3.000. (b) art. 63.1: 12.450 × 9,5 % = 1.182,75; 7.750 × 12 % = 930 → 2.112,75 at 20.200; 9.800 × 15 % = 1.470; 2.112,75 + 1.470 = 3.582,75; 5.550 × 9,5 % = 527,25; 3.582,75 − 527,25 = 3.055,50. (c) art. 96: 700 + 300 = 1.000 ≤ 1.500; 18.000 ≤ 22.000. All verified with `python3`. No dates involved.

## 5. Course summary
La renta se clasifica en general y del ahorro; sus saldos se integran y compensan en las bases imponibles, y las reducciones dan las bases liquidables. El mínimo personal y familiar no tributa; la escala del artículo 63 da la cuota íntegra estatal y las deducciones, la cuota líquida y la diferencial. La declaración es obligatoria salvo en los límites del artículo 96, y la tributación conjunta es una opción por unidad familiar.

## 6. Glossary proposals
```yaml
- id: g-renta-general
  es: renta general
  origin: m03-l16
  definition: {es: «Los rendimientos y las ganancias y pérdidas patrimoniales que no tengan la consideración de renta del ahorro», más las imputaciones de renta de los artículos 85, 91, 92 y 95 LIRPF y otras que el artículo enumera (art. 45 LIRPF).}
- id: g-renta-del-ahorro
  es: renta del ahorro
  origin: m03-l16
  definition: {es: Los rendimientos del capital mobiliario de los apartados 1, 2 y 3 del artículo 25 LIRPF, con la excepción del artículo 46.a), y las ganancias y pérdidas patrimoniales que se pongan de manifiesto con ocasión de transmisiones de elementos patrimoniales (art. 46 LIRPF).}
- id: g-minimo-personal-y-familiar
  es: mínimo personal y familiar
  origin: m03-l16
  definition: {es: «La parte de la base liquidable que, por destinarse a satisfacer las necesidades básicas personales y familiares del contribuyente, no se somete a tributación por este Impuesto» (art. 56.1 LIRPF).}
```
`g-base-liquidable`, `g-cuota-liquida` and `g-cuota-diferencial` already exist.

## 7. Unresolved citations, facts left out, ambiguities
- `cites.py`: 0 unresolved (131 citations).
- RDL 29/2026: marks on art. 67.1 and art. 68.6 only (the apartados the RDL changed). Art. 68 is a list of headings; its content is not stated.
- 2022X-88: the official key B (1.400) and the arithmetic reading differ. The lesson states art. 57.2 as written («se aumentará adicionalmente en 1.400») and the total 5.550 + 1.150 + 1.400 = 8.100; it does not choose.
- 2024-79 / 2022-87: the thresholds are the snapshot's (22.000; 15.876; 1.500; 1.600; 1.000). Option 2022-87.a) (ganancias de IIC with a base de retención not fixed by the amount to integrate) is covered by the narrowing sentence of art. 96.2.b).
- Left out: arts. 61 bis (suprimido), 64–65, 69–70, 80 bis (suprimido), 80.2–3, 81.3, 81 bis.4, 84.2 (rest), 84.3–4, 96.5–9, 97.3–5, 99–101 and 104–105 (pagos a cuenta: `m03-l06`; obligaciones formales: no question and not named in the programme), 51.6–9 and 52's table.
- The text of arts. 56.3 and 81 bis.1.c) names Ley 22/2009 and Ley 40/2003; the lesson paraphrases the second and omits the first to avoid listing norms without an article.
- `tests/test_citations.py` golden (`citations.es.txt`) needs `UPDATE_CITATIONS=1` after the group.
