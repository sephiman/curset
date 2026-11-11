# Writer notes: m03-l05 (III.5, Información y asistencia; colaboración social; carácter reservado; normas comunes)

## 1. Sources
- LGT `BOE-A-2003-23186_lgt_2024-12-21.pdf`: arts. 85–92 (sección 2.ª y 3.ª), 93–95 bis (93–94 read, not used), 97–112; 113–116 read, left out.
- RGAT `BOE-A-2007-15984_rgat_2026-10-07.pdf`: arts. 62–65, 69–75, 77–79, 91, 102–104 (66–68, 76, 80–90, 92–101 read or skipped, not used).
- LPAC `BOE-A-2015-10565_lpac_2024-11-06.pdf`: arts. 30.4 (cómputo of months) and 43.2 (electronic notification rejected after ten días naturales).

## 2. Pack questions (coverage 21 of 21 stated; whole pack 33 of 35 stated)
| id | lesson section |
|---|---|
| 2025-20 | Plazo máximo de resolución (art. 104.1 LGT). The official key D and the ledger note (the question assumes another plazo set by a ley or EU norm; the article says the plazo is that other one) are not resolved: the lesson states the article. |
| 2025-54, 2022-41, 2022X-48 | Lugar de práctica (art. 110.1 LGT) |
| 2025-62, 2023-88 | Los certificados tributarios (art. 73.1 RGAT: 20 días; art. 73.4: 10 días, not 15; art. 73.2: papel o telemático) |
| 2025-68, 2023-77 | Plazo máximo de resolución (art. 104.1.a–b), cumplimiento de la obligación (art. 104.2), exclusions from the cómputo |
| 2024-7 | Publicidad de situaciones de incumplimiento relevante (art. 95 bis.1) |
| 2024-24, 2023-99 | Certificados (arts. 70.4, 73.4, 75.1, 75.2 RGAT); RGAT 75.2 as the snapshot says: 12 meses periódicas, tres meses no periódicas |
| 2024-84 | Actuaciones de asistencia tributaria (art. 77.1 RGAT; art. 78.1 for the programas informáticos distractor) |
| 2023-18, 2022X-42 | Acuerdos previos de valoración (art. 91.1–6 LGT) |
| 2023-49 | Fases, desarrollo (art. 91.1–6 RGAT) |
| 2023-57 | Liquidaciones, concepto y clases (art. 101.4.b) LGT) |
| 2022-38 | Publicaciones (art. 86.1 LGT) |
| 2022-39, 2022X-41 | Información previa a la adquisición o transmisión (art. 90 LGT; art. 69 RGAT) |
| 2022X-46 | Períodos de interrupción justificada (art. 103.c) RGAT) |
| 2022X-47 | art. 104.2 LGT, notificación electrónica; art. 43.2 LPAC for the «diez días naturales» distractor |
| 2022-43 (ref, anulada) | art. 104.1–3 LGT; dos intentos vs un intento in art. 104.2; tres meses de caducidad in art. 104.3 |
| 2021-44, 2021-46, 2021-47 (ref) | arts. 90.3, 88, 89 LGT |
| 2021-50 (ref) | art. 103.3 LGT |
| 2021-55, 2020-52 (ref) | art. 104 RGAT (letras a–g stated; h–i left out, see 7) |
| 2020-40 (ref) | art. 95.3 LGT |
| 2020-50 (ref) | art. 64.1 RGAT |
| 2020-51 (ref) | art. 99.8 LGT |
| 2020-56 (ref) | arts. 70.5, 73.1, 75 RGAT |
| 2020-58 (ref) | art. 112.3 LGT |
| 2022X-50, 2022X-51 (ref) | no está: fuera de temario (arts. 93.4 LGT and 30.3 RGAT, programa 2024) |

## 3. Lo que más cae
1 art. 104.1 LGT: 2025-20, 2025-68, 2023-77. 2 art. 104.2: 2023-77, 2022X-47. 3 art. 110.1: 2025-54, 2022-41, 2022X-48. 4 art. 73.1 RGAT: 2025-62, 2023-88. 5 art. 90.2 LGT: 2022-39, 2022X-41. 6 arts. 91.4–5 LGT: 2023-18, 2022X-42. 7 art. 75.2 RGAT: 2024-24, 2023-99. 8 art. 95 bis.1: 2024-7. 9 art. 86.1: 2022-38. 10 art. 101.4.b): 2023-57. Not in the ten (but stated in the body): RGAT 77.1 (2024-84), 91.4 (2023-49), 103.c) (2022X-46), 70.4 (2023-99).

## 4. Worked examples
Two: plazo de resolución (Talleres Ribera, S.L.; arts. 104.1–2 LGT, 30.4 LPAC, 102.5 and 104.b RGAT) and notificación por comparecencia (Lucía Martín; arts. 110.2, 112.1–2 LGT). Every date and weekday checked with `python3 -I` (`datetime.date.strftime('%A')`): 15-01-2026 Thursday, 15-07-2026 Wednesday, 10-04-2026 Friday, 30-04-2026 Thursday, 03-08-2026 Monday, 04-08-2026 Tuesday, 05-08-2026 Wednesday, 03-03-2026 Tuesday, 04-03-2026 Wednesday, 16-03-2026 Monday, 17-03-2026 Tuesday, 31-03-2026 Tuesday, 01-04-2026 Wednesday. 15 July + 20 days = 4 August; 17 March + 14 days = 31 March (day 15 of the plazo). The dilación of 20 días counts both 11 and 30 April (art. 104.b RGAT: «desde el día siguiente … hasta la fecha en que se aporten»); the verifier may read the end date as excluded.

## 5. Course summary
El obligado tributario recibe información y asistencia de la Administración (consultas, información previa de valores, acuerdos previos de valoración, certificados), y los datos tributarios son reservados. Las actuaciones y procedimientos siguen las normas comunes de la LGT: iniciación, desarrollo y terminación, liquidaciones provisionales y definitivas, resolución en seis meses salvo plazo propio y notificación en el lugar y forma que fijan los arts. 109–112.

## 6. Glossary proposals (no existing ids for these slugs in glossary.yaml)
```yaml
- id: g-liquidacion-tributaria
  es: liquidación tributaria
  origin: m03-l05
  definition: {es: «Acto resolutorio mediante el cual el órgano competente de la Administración realiza las operaciones de cuantificación necesarias y determina el importe de la deuda tributaria o de la cantidad que, en su caso, resulte a devolver o a compensar de acuerdo con la normativa tributaria» (art. 101.1 LGT).}
- id: g-certificado-tributario
  es: certificado tributario
  origin: m03-l05
  definition: {es: «El documento expedido por la Administración tributaria que acredite hechos relativos a la situación tributaria de un obligado tributario» (art. 70.1 RGAT).}
- id: g-diligencias
  es: diligencias
  origin: m03-l05
  definition: {es: «Los documentos públicos que se extienden para hacer constar hechos, así como las manifestaciones del obligado tributario o persona con la que se entiendan las actuaciones»; no pueden contener propuestas de liquidaciones tributarias (art. 99.7 LGT).}
- id: g-comunicaciones-administrativas
  es: comunicaciones
  origin: m03-l05
  definition: {es: «Los documentos a través de los cuales la Administración notifica al obligado tributario el inicio del procedimiento u otros hechos o circunstancias relativos al mismo o efectúa los requerimientos que sean necesarios a cualquier persona o entidad» (art. 99.7 LGT).}
```

## 7. Unresolved, left out, ambiguities
- cites.py: 0 unresolved.
- Left out (programme does not name, no coverage question): LGT arts. 93–94 (obligaciones de información; reference questions 2022X-50 and 2022X-51 are fuera de temario), 96, 113–116; RGAT arts. 66–68 (iniciación y tramitación de consultas), 74, 76, 80–90, 92–101, 105–116; art. 104.h) and i) RGAT (retraso en la notificación por el RD 1363/2010; libros registro del IVA); art. 90 RGAT; the rest of LGT 95 bis.3 and .6.
- Ambiguity: 2025-20 (ledger note: the key D reads the question as «ni»); the lesson states art. 104.1 as written.
- The artículo 106.1 LGT names the Código Civil and the LEC without article: listed in «Normativa» as «sin artículos concretos».
- The Juntas Arbitrales (art. 103.f) RGAT): the Convenio de Navarra (Ley 25/2003 in the RGAT text) is not in `normativa.yaml`; the lesson says «entre otras» and cites only LOFCA art. 24 and Ley 12/2002 art. 66.
