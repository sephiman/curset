# Notas del redactor — III.14 (`m03-l14`)

## 1. Fuentes
- LGT (`BOE-A-2003-23186_lgt_2024-12-21.pdf`): arts. 213–249 leídos completos; citados todos salvo 241 ter y 230.2/4 (omitidos).
- RGRVA (`BOE-A-2005-8662_rgrva_2023-04-05.pdf`): arts. 21–27 (reposición), 28–36, 60–61, 64–65 y 74 leídos. La numeración del plan («RGRVA 21–25 reposición, 28–34 tribunales») coincide con el snapshot; las cuantías están en los arts. 35, 36 y 64.
- LPAC (`BOE-A-2015-10565_lpac_2024-11-06.pdf`): solo el art. 30.4–5 para el ejemplo.
- Ley 22/2009: solo el inciso «salvo los supuestos a los que se refiere el artículo 59.1.c) último párrafo» del art. 229.1.e LGT, citado como aparece.

## 2. Preguntas del pack (26: 18 coverage + 8 reference)
- 2025-23 → Reposición (222.2) · 2025-47 → Nulidad (217.6) · 2025-52 → Procedimiento general (234.3, 234.4, 234.5) · 2025-70 → Procedimientos especiales (216)
- 2024-14 → Resolución de la reposición (225.1, 225.4, 225.5, 225.6) · 2024-22 → Nulidad (217.1) · 2024-60 → Nulidad (217.2) · 2024-72 → Recurso extraordinario de revisión (244.1, 244.6; la rectificación de errores de hecho es art. 220.1)
- 2023-3 → Resolución de la reposición (225.1, 225.4) · 2023-83 → Suspensión (233.1, 233.4, 233.5, 233.10) · 2023-94 → Reposición (222.2)
- 2022-70 → Suspensión en reposición (224.1, que remite al 212.3; el 212.3 lo explica `m03-l13`) · 2022-75 → Revocación (219) · 2022-76 → Iniciación y Tramitación (235.1, 235.3, 235.4, 236.6) · 2022-77 → Medios de revisión (213.3) · 2022-78 → Devolución de ingresos indebidos (221.1) · 2022X-84 → 213.3 · 2022X-85 → Revocación (219.5)
- Reference: 2022X-86 → 233.1 y 224.1 (y 212.3 en m03-l13) · 2021-90 → 221.1.c · 2021-91 → 225.4 (dos meses) · 2021-94 → 244.4 · 2020-75 → Actos reclamables (227.1–5; la inadmisibilidad de disposiciones normativas no figura expresamente: no está) · 2020-81 → Reposición (222.1, 222.2, 223.1) · 2020-88 → Los Tribunales (36 RGRVA) · 2020-71 → no está: art. 74 RGRVA (coste de las garantías), fuera de la profundidad «standard» y del programa.

## 3. «Lo que más cae» → preguntas
1 → 2025-47, 2024-22, 2024-60; 2 → 2022-77, 2022X-84; 3 → 2022-75, 2022X-85; 4 → 2025-23, 2023-94; 5 → 2024-14, 2023-3; 6 → 2023-83; 7 → 2024-72; 8 → 2022-78; 9 → 2022-76; 10 → 2025-52. (216, 2025-70, queda en el cuerpo; no entra en las diez líneas.)

## 4. Ejemplo
Plazos de reposición y reclamación (Lucía Martín). Fechas comprobadas con `python3 datetime`: 30-01-2026 viernes; 28-02-2026 sábado; 02-03-2026 lunes; 13-02-2026 viernes; 13-03-2026 viernes. Cómputo según 223.1 y 235.1 LGT y 30.4–5 LPAC (febrero no tiene día 30: expira el 28). No hay festivos nacionales el 2 y el 13 de marzo.

## 5. Resumen para `course.yaml`
Los actos tributarios se revisan por procedimientos especiales (nulidad, lesividad, revocación, rectificación de errores, devolución de ingresos indebidos), por el recurso de reposición, que es potestativo, se interpone en un mes y se resuelve en un mes, y por reclamaciones económico-administrativas ante el Tribunal Económico-Administrativo Central y los tribunales regionales y locales. La reclamación se interpone en un mes, el procedimiento general dura un año y el abreviado seis meses. Lo que pone fin a la vía económico-administrativa se recurre ante la jurisdicción contencioso-administrativa.

## 6. Glosario propuesto
Ninguno nuevo: `g-declaracion-de-lesividad` y `g-recurso-potestativo-de-reposicion` ya existen en `glossary.yaml`. Los demás términos del tema (nulidad de pleno derecho, revocación, reclamación económico-administrativa) los enumera la ley sin definirlos.

## 7. Citas sin resolver, omisiones, ambigüedades
- cites.py: 181 citas, 0 sin resolver.
- Pack 2022-76: la nota R0a cita el art. 235.3 para la opción d; en el snapshot el escrito se dirige al tribunal en los casos de retenciones, repercusiones, etc. en el art. 235.4 (el 235.3 fija el plazo de remisión de un mes). La lección cita 235.4.
- Pack 2025-70: la evidencia R0a transcribe «d) Rectificación de errores»; correcto en el art. 216.
- Omitido: art. 241 ter (recurso contra la ejecución), 230.2 y 230.4, 233.8, 233.9, 233.11–13, 233.15, 235.1 párrafos sobre silencio con resolución posterior y facturas, 236.2, 236.4, 236.5, 239.1–2 y 239.5–8, 240.2, 241.2, 246.1, 247.1 y 247.3; RGRVA arts. 1–20 (procedimientos especiales), 23–27 salvo los citados, 31, 34, 37–59, 62–63 y 65–79; los intereses de demora no llevan cifra, no hay cifras anuales.
- Dos fuentes que difieren: ninguna. El pack 2024-14 opción c («pondrá fin a la vía administrativa») no se recoge porque el art. 225 LGT no lo dice.
