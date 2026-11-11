# m03-l07 — notas del redactor

## 1. Fuentes
- LGT (`BOE-A-2003-23186_lgt_2024-12-21.pdf`): arts. 31, 57, 99.7 (solo la mención), 104, 117–140, leídos enteros en esos rangos.
- RGAT (`BOE-A-2007-15984_rgat_2026-10-07.pdf`): arts. 122–137 (devolución, rectificación, ejecución, declaración, beneficios fiscales), 153 (control de presentación), 155–165 (verificación, valores, TPC, comprobación limitada); texto del snapshot.
- LIRPF (`BOE-A-2006-20764_lirpf_2026-11-11.pdf`): art. 103.1 y 103.4 para el ejemplo 1.
- Ningún precepto citado tiene cambio pendiente ni RDL sin convalidar en `normativa.yaml`.

## 2. Preguntas del pack (15 coverage, 4 reference; 19 en total)
- 2025-29, 2023-74 (140.1, 140.2): «Efectos de la regularización».
- 2025-43 (31.2): «Ejemplo: intereses de una devolución del IRPF» y «Devoluciones derivadas de la normativa». Pack: «31.2 y 103 LIRPF»; la base de 200 euros sale de 103.4 LIRPF («cantidad pendiente de devolución») y 127 LGT («devolución que finalmente se pueda practicar»).
- 2024-4, 2022X-35 (117.1.d y l): «La gestión tributaria» (lista completa).
- 2024-52 (120.4): «Rectificación de autoliquidaciones». El pack cita 120.4; el texto de la opción b también está en 120.3 (rectificación mediante autoliquidación rectificativa).
- 2024-64 (133.2), 2024-87 (131): «Procedimiento de verificación de datos». La opción b de 2024-87 es la letra de 163.c RGAT (comprobación limitada), que la lección da en «Iniciación» de comprobación limitada.
- 2023-42 (reference, anulada; 162 RGAT), 2022-49, 2020-55 (159.1): «Tasación pericial contradictoria» y «Procedimiento» de comprobación de valores. La lección da 162.1 entera.
- 2023-67 (153.6): «Control de la presentación de declaraciones». El pack pone la caducidad como letra d); el texto de 153.6 también.
- 2023-90, 2020-53 (136.3, 136.4, 136.2.c): «Objeto y actuaciones».
- 2022-47 (128.1, 128.4 RGAT): «Rectificación de autoliquidaciones», terminación. La opción c está en 128.1 casi literal; a) y b/d se desmienten con 128.1 (sin «siempre») y 128.4 (seis meses).
- 2022-48 (137 RGAT): «Beneficios fiscales de carácter rogado». La lección da 137.1, 137.2 y 137.3 (la opción b del enunciado, falsa, contradice 137.3).
- 2022X-52 (129.1): «Tramitación» y ejemplo 2.
- 2022X-54 (135.1): «Tasación pericial contradictoria».
- 2021-57 (131 RGAT, reference): «Ejecución de las devoluciones» (131.1, 131.3, 131.4, 131.5).
- No está: nada.

## 3. «Lo que más cae» → preguntas
1: 2025-29. 2: 2023-90, 2020-53. 3: 2022-49, 2020-55 (y 2023-42 en sentido amplio). 4: 2024-64. 5: 2024-87. 6: 2023-74. 7: 2024-4, 2022X-35. 8: 2022X-52. 9: 2025-43. 10: 2022-48.
Quedan fuera de las diez líneas, pero están en el cuerpo: 2024-52 (120.4), 2023-67 (153.6), 2022-47 (128 RGAT), 2022X-54 (135.1), 2021-57 (131 RGAT).

## 4. Ejemplos
- Ejemplo 1 (intereses del IRPF, art. 31.2 LGT): fechas comprobadas con `python3 datetime`: 10-06-2025 martes, 30-06-2025 lunes, 01-10-2025 miércoles, 31-12-2025 miércoles, 02-03-2026 lunes. Seis meses «siguientes al término del plazo»: del 01-07 al 31-12-2025, como el pack. No calculo el importe de los intereses: no hay tipo anual de 2025 en `cifras_anuales` (solo 2026) y el artículo no fija el criterio de días.
- Ejemplo 2 (plazo del art. 129.1 LGT): 15-09-2025 lunes, 12-11-2025 miércoles, 13-11-2025 jueves, comprobados. No calculo la fecha de fin del plazo de seis meses para no fijar un criterio de cómputo que la LGT no da.

## 5. Resumen para course.yaml
La lección recorre los procedimientos de gestión tributaria de la LGT y el RGAT: devolución, rectificación de autoliquidaciones, procedimiento iniciado mediante declaración, verificación de datos, comprobación de valores y comprobación limitada. Da los supuestos, los trámites y las formas de terminación de cada uno. Resuelve con dos ejemplos los intereses de una devolución y el plazo de notificación de una declaración extemporánea.

## 6. Propuestas de glosario (ninguna existe en `glossary.yaml`)
```yaml
- id: g-declaracion-tributaria
  es: declaración tributaria
  origin: m03-l07
  definition: {es: «Todo documento presentado ante la Administración tributaria donde se reconozca o manifieste la realización de cualquier hecho relevante para la aplicación de los tributos» (art. 119.1 LGT).}
- id: g-autoliquidacion
  es: autoliquidación
  origin: m03-l07
  definition: {es: Declaración en la que los obligados tributarios, además de comunicar los datos necesarios para la liquidación del tributo, realizan por sí mismos las operaciones de calificación y cuantificación necesarias para determinar e ingresar el importe de la deuda tributaria o, en su caso, determinar la cantidad que resulte a devolver o a compensar (art. 120.1 LGT).}
- id: g-comunicacion-de-datos
  es: comunicación de datos
  origin: m03-l07
  definition: {es: «La declaración presentada por el obligado tributario ante la Administración para que ésta determine la cantidad que, en su caso, resulte a devolver» (art. 121 LGT).}
```
(Las tres definiciones salen de arts. 119–121, que son de III.6; la lección de III.7 solo las usa. Propuesta para el coordinador: si `m03-l06` las propone, no duplicar.)

## 7. Pendiente
- Citas sin resolver: ninguna (`cites.py`: 132 citas, 0 sin resolver).
- Fuera de la lección: LGT 135.3 (honorarios del perito tercero, lista de colegios, depósito) salvo lo que cita 162.1.d; RGAT 161 (plazos de la TPC), 132 (pago o compensación de devoluciones), 134 (aduanero), 138–152 (cuenta corriente, censos, domicilio): el programa no los nombra y ninguna pregunta los pidió.
- Ambigüedad: «Lo que más cae» solo admite diez líneas y hay quince hechos de cobertura; quedan seis en el cuerpo (ver 3).
