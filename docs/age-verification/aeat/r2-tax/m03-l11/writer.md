# Notas del redactor — III.11 (`m03-l11`)

## 1. Fuentes
- LGT (`BOE-A-2003-23186_lgt_2024-12-21.pdf`): arts. 28 (completo salvo 28.6), 62.5, 77–82 (82 solo el apartado 1), 160–168 (162 omitido: lo toma III.12).
- RGR (`BOE-A-2005-14803_rgr_2024-01-31.pdf`): arts. 46.1, 64–67, 69–74, 77.1. La numeración del plan (RGR 69–76) se comprobó: 69 recaudación ejecutiva, 70–71 providencia, 72 interés de demora, 73 suspensión, 74 ejecución de garantías; 75–76 son embargo (III.12).
- LPAC art. 30.2 y LGT art. 7.2 para los días hábiles (como en `m03-l09`).
- Ley 31/2022: no se cita. El plan la listaba para el interés, pero la lección no da ningún tipo de interés (28.5 LGT y 72 RGR solo regulan la compatibilidad y el devengo), así que no hay cifra anual que fechar.

## 2. Preguntas del pack (id → sección)
- 2025-41 → Plazos de pago de las deudas apremiadas (62.5.a) y ejemplo
- 2024-9 → Carácter del procedimiento (163.1–3)
- 2024-32 → Recargos (28.2, 28.5) y Iniciación (161.1.a); el plazo voluntario del 62.2 está en `m03-l09`
- 2024-35 → Medidas cautelares (81.1, 81.3, 81.4.c, 81.7 con la letra d)
- 2023-5 → Plazos de pago de las deudas apremiadas (62.5.a)
- 2023-38 → Recargos (28.5)
- 2022-35 → Recargos (28.1, 28.2, 28.4, 28.5)
- 2022-62 → Ejecución de garantías (168)
- 2022-64 → Concurrencia de procedimientos (164.1)
- 2022X-68 → Recargos (28.2) y Plazos
- 2022X-69 → Iniciación del período ejecutivo (161.1.b, 161.2, 46.1.a RGR). La clave oficial (A) está en discusión (nota del pack); la lección da la norma: la solicitud presentada con la autoliquidación extemporánea es en período voluntario e impide el inicio (161.2). No se recoge la clave A.
- 2022X-70 (reference) → La providencia de apremio (167.3 completo)
- 2021-82 (reference) → no está en esta lección: tercerías (119.2 RGR) están en `m03-l12`
- 2020-61 (reference) → Recargos (28.5)
- 2020-63 (reference) → Plazos (62.5.b)
- 2020-79 (reference) → Carácter (163), Conservación (166.1)
- 2020-89 (reference, anulada) → Ejecución de garantías (168; 74.2)

## 3. «Lo que más cae» → preguntas
1 → 2025-41, 2023-5, 2020-63; 2 → 2023-38, 2022-35, 2020-61; 3 → 2022X-68, 2024-32; 4 → 2022-35; 5 → 2024-9, 2020-79; 6 → 2024-35; 7 → 2024-35; 8 → 2022-64; 9 → 2022-62, 2020-89; 10 → 2022X-69.

## 4. Ejemplos
Uno: recargos del art. 28 con los plazos del 62.5 (Lucía Martín, providencia notificada el miércoles 10-06-2026; Talleres Ribera, S.L., el martes 16-06-2026). Fechas comprobadas con `python3 -c "import datetime…"`: 10-06-2026 miércoles; 20-06-2026 sábado (inhábil) → lunes 22-06-2026; 9-06-2026 martes; 23-06-2026 martes; 16-06-2026 martes; 5-07-2026 domingo (inhábil) → lunes 6-07-2026. Importes: 4.000 × 5 % = 200; × 10 % = 400; × 20 % = 800.

## 5. Resumen para `course.yaml`
El período ejecutivo se inicia al vencer el plazo de ingreso y se cobra por el procedimiento de apremio, que arranca con la providencia notificada al obligado. Los recargos son del 5 %, 10 % o 20 % según cuándo se pague (art. 28 LGT) y el pago de la deuda apremiada se hace en los plazos del art. 62.5 LGT. La deuda se asegura con prelación, hipoteca legal tácita, afección, retención y medidas cautelares, y si está garantizada se ejecuta primero la garantía (art. 168 LGT).

## 6. Glosario propuesto
- id: g-providencia-de-apremio
  es: providencia de apremio
  origin: m03-l11
  definition: {es: «La providencia de apremio es el acto de la Administración que ordena la ejecución contra el patrimonio del obligado al pago» (art. 70.1 RGR).}
- id: g-recargo-ejecutivo
  es: recargo ejecutivo
  origin: m03-l11
  definition: {es: «El recargo ejecutivo será del cinco por ciento y se aplicará cuando se satisfaga la totalidad de la deuda no ingresada en periodo voluntario antes de la notificación de la providencia de apremio» (art. 28.2 LGT).}
- id: g-recargo-de-apremio-reducido
  es: recargo de apremio reducido
  origin: m03-l11
  definition: {es: «El recargo de apremio reducido será del 10 por ciento y se aplicará cuando se satisfaga la totalidad de la deuda no ingresada en periodo voluntario y el propio recargo antes de la finalización del plazo previsto en el apartado 5 del artículo 62» (art. 28.3 LGT).}
- id: g-recargo-de-apremio-ordinario
  es: recargo de apremio ordinario
  origin: m03-l11
  definition: {es: «El recargo de apremio ordinario será del 20 por ciento y será aplicable cuando no concurran las circunstancias a las que se refieren los apartados 2 y 3» del artículo 28 (art. 28.4 LGT).}
- id: g-medidas-cautelares
  es: medidas cautelares
  origin: m03-l11
  definition: {es: La Administración tributaria puede adoptarlas «cuando existan indicios racionales de que, en otro caso, dicho cobro se vería frustrado o gravemente dificultado» (art. 81.1 LGT).}

## 7. Citas sin resolver, omisiones, ambigüedades
- cites.py: 115 citas, 0 sin resolver.
- Los nombres de la Ley Concursal, la Ley General Presupuestaria y la ley de conflictos jurisdiccionales (arts. 77.2, 161.2, 163.2, 164.2 LGT) se dan sin número ni título («normativa concursal», «legislación de conflictos jurisdiccionales») para no abrir líneas de «Normativa» sin artículo citado; el contenido de cada regla no cambia.
- Omitido: art. 28.6 LGT (asistencia mutua), 81.2, 81.5, 81.6, 81.9 y la letra e) de 81.7 (24 meses, con delito contra la Hacienda Pública; cubierta por «entre otros supuestos»), art. 82.2 (dispensa de garantías, ya en `m03-l09`), 164.3–4, 80 bis; RGR 64.2, 66.1, 66.3–4, 68, 70.3–4, 72.3–5, 73.3–4, 74.6–7. Ninguna pregunta del pack los pide.
- El art. 162 LGT (facultades) lo toma `m03-l12`.
- Dos fuentes que difieren: ninguna. La clave oficial de 2022X-69 difiere de la norma (ver §2).
