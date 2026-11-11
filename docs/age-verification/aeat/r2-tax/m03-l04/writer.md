# m03-l04 — notas del redactor

## 1. Fuentes
- LGT (`BOE-A-2003-23186_lgt_2024-12-21.pdf`): arts. 29–48, 66–70, DA 6.ª (completos en esos rangos).
- RGAT (`BOE-A-2007-15984_rgat_2026-10-07.pdf`): arts. 2, 3, 11, 17, 18, 19, 20, 29, 59, 110–113.
- RD 1619/2012 (`BOE-A-2012-14696_..._2026-03-31.pdf`): arts. 2, 3, 4, 15. El RD 238/2026 cambia los arts. 8.1, 8 bis, 9 y 10: la lección no los cita, sin marca de cambio pendiente.
- RIVA (`BOE-A-1992-28925_riva_2026-02-28.pdf`): arts. 40, 61.2, 62, 69 bis, 71.3.
- RIRPF (`BOE-A-2007-6820_rirpf_2026-10-07.pdf`): art. 68. Los cambios del RDL 29/2026 en el RIRPF (arts. 41 bis, 69, 75, 76, 93, 94, DA 8) no tocan el 68; el RGAT art. 39 quater (RDL 29/2026) no se cita.
- Código de Comercio art. 30.1 y RD 1676/2009 art. 4.1: ya están en `normativa.yaml` (`short` «Código de Comercio» y «RD 1676/2009 (Consejo para la Defensa del Contribuyente)»); texto leído en los PDF de `sources/normativa`.

## 2. Preguntas del pack (32 coverage)
- 2025-2 (RGAT 29.2): «Libros registro». 2025-30, 2024-43, 2023-40, 2025-36, 2021-65 (66, 66 bis, 67.1, 67.2): «Plazos de prescripción» / «Cómputo». 2025-63, 2020-38 (69.2–3): «Extensión y efectos».
- 2024-8, 2022-36, 2022-59, 2021-66, 2021-69, 2020-70 (68): «Interrupción». La opción b de 2024-8 la desmiente 68.8 («incluidos los responsables»).
- 2024-23, 2021-51, 2020-47 (DA 6.ª): «Número de identificación fiscal». 2024-49 y 2023-82: RGAT 20.2 (M) y 19.2 (L, K); la nota del pack dice «art. 20.3» pero el texto del snapshot es el 20.2.
- 2024-39 (RIVA 40.1), 2021-48 (RIVA 61.2), 2022-44 y 2021-52 (RIVA 62.6, 69 bis.1, 71.3.1.º): «Libros registro» (IVA). 2023-11, 2022X-43 (RIRPF 68.2–5, 68.10): «Libros registro» (IRPF). 2022X-45 (Código de Comercio 30.1): «Libros registro».
- 2024-88, 2023-16, 2020-100, 2021-53, 2022-42 (RD 1619/2012 3, 4, 15.3): «Facturación». 2023-16: la opción a (500 euros) la desmiente 4.1.a) (400 euros).
- 2024-59, 2021-45 (48.2.c, 48.1): «Domicilio fiscal». 2023-41 (RGAT 59.2), 2023-46 (113), 2021-45 (RGAT 17.1–2).
- 2023-23, 2022-37, 2021-43 (112.1 RGAT; 46.7 LGT), 2022X-38 (111.1, 111.5–6): «Representación».
- 2022-40, 2020-49 (RGAT 11.3–4): «Declaraciones censales». 2022X-44 (RGAT 3.5), 2021-54 (RGAT 3.2.a; el pack dice «3.3», el texto del snapshot lo tiene en el art. 3.2.a) párrafo segundo).
- 2023-96 (RD 1676/2009 4.1.b): «Derechos y garantías». 2021-42 (34.1).
- 2022X-39, 2022X-40, 2020-41, 2020-44 (35–38): «Los obligados tributarios». 2021-86, 2020-87, 2022X-79 (42, 43): «Responsables». 2021-87 (39.1): «Sucesores».
- No está: 2021-49 (Orden EHA/1274/2007, modelo 037, preceptos suprimidos; fuera del snapshot y del programa; es pregunta reference).

Cobertura: los 32 coverage tienen su hecho en la lección.

## 3. «Lo que más cae» → preguntas
1: 2024-8, 2022-59. 2: 2022-59, 2022-36. 3: 2025-30, 2023-40. 4: 2025-36, 2021-65. 5: 2024-43. 6: 2025-63, 2020-38. 7: 2024-88, 2023-16, 2020-100. 8: 2023-23, 2022-37, 2021-43. 9: 2022X-79. 10: 2024-49, 2023-82.

## 4. Ejemplo
Cómputo de la prescripción del art. 66.a) con una interrupción por comprobación limitada (68.1.a, 68.6). Fechas comprobadas con `python3 datetime`: 30-06-2022 jueves, 14-03-2025 viernes, 15-09-2026 martes, 01-07-2022 viernes. El art. 67.1 no dice si el último día del plazo es la fecha de aniversario o el día anterior; por eso el ejemplo no fija el último día: compara períodos (más de cuatro años desde 01-07-2022; «no termina antes de marzo de 2029» desde 14-03-2025). Pregunta de decisión: ¿lo quiere con fecha exacta de fin?

## 5. Resumen para course.yaml
La lección reúne las obligaciones formales (censos, número de identificación fiscal, libros registro y facturas), los derechos y garantías del artículo 34 y los obligados tributarios, con sucesores y responsables. Sigue con la capacidad de obrar, la representación y el domicilio fiscal. Cierra con los plazos de prescripción, su cómputo, su interrupción y sus efectos.

## 6. Propuestas de glosario
```yaml
- id: g-obligado-tributario
  es: obligado tributario
  origin: m03-l04
  definition: {es: «Las personas físicas o jurídicas y las entidades a las que la normativa tributaria impone el cumplimiento de obligaciones tributarias» (art. 35.1 LGT).}
- id: g-sujeto-pasivo
  es: sujeto pasivo
  origin: m03-l04
  definition: {es: «El obligado tributario que, según la ley, debe cumplir la obligación tributaria principal, así como las obligaciones formales inherentes a la misma, sea como contribuyente o como sustituto del mismo» (art. 36.1 LGT).}
- id: g-contribuyente
  es: contribuyente
  origin: m03-l04
  definition: {es: «El sujeto pasivo que realiza el hecho imponible» (art. 36.2 LGT).}
- id: g-sustituto-del-contribuyente
  es: sustituto del contribuyente
  origin: m03-l04
  definition: {es: «El sujeto pasivo que, por imposición de la ley y en lugar del contribuyente, está obligado a cumplir la obligación tributaria principal, así como las obligaciones formales inherentes a la misma» (art. 36.3 LGT).}
- id: g-retenedor
  es: retenedor
  origin: m03-l04
  definition: {es: «La persona o entidad a quien la ley de cada tributo impone la obligación de detraer e ingresar en la Administración tributaria, con ocasión de los pagos que deba realizar a otros obligados tributarios, una parte de su importe a cuenta del tributo que corresponda a estos» (art. 37.2 LGT).}
- id: g-domicilio-fiscal
  es: domicilio fiscal
  origin: m03-l04
  definition: {es: «El lugar de localización del obligado tributario en sus relaciones con la Administración tributaria» (art. 48.1 LGT).}
- id: g-obligaciones-tributarias-conexas
  es: obligaciones tributarias conexas
  origin: m03-l04
  definition: {es: «Aquellas en las que alguno de sus elementos resulten afectados o se determinen en función de los correspondientes a otra obligación o período distinto» (art. 68.9 LGT).}
```
Ninguno de estos ids existe en `glossary.yaml` (`g-hecho-imponible` y `g-devengo` se proponen en m03-l03).

## 7. Pendiente
- Citaciones sin resolver: ninguna (`cites.py`: 224 citaciones, 0 sin resolver).
- Fuera por falta de fuente o por no pedirse: RGAT arts. 4–10, 12–16 y 21–28 (contenido de cada censo, alta y modificación, NIF de personas jurídicas); el programa no los nombra y ninguna pregunta coverage los pide.
- Discrepancias entre el pack y el snapshot: RGAT 3.5/3.3 y 20.3/20.2 (arriba). Pregunta 2024-43 (clave B): la B cuenta los diez años «desde el día siguiente a aquel en que finalice el período impositivo»; el art. 66 bis.2 los cuenta desde el fin del plazo reglamentario de presentación. La lección da el texto del artículo; no hay opción literal.
- El pack 2021-87 (sanciones a los sucesores): la lección dice «en ningún caso» para personas físicas (39.1) y recoge 40.5 para sociedades.
