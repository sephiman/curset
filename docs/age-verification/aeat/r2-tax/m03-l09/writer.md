# Notas del redactor — III.9 (`m03-l09`)

## 1. Fuentes
- LGT (`BOE-A-2003-23186_lgt_2024-12-21.pdf`): arts. 7.2, 26 (apartados 1–6), 59–65, 82 (pdftotext, texto completo de cada artículo).
- RGR (`BOE-A-2005-14803_rgr_2024-01-31.pdf`): arts. 13, 16, 17, 19, 20, 28, 29, 32–54, 68 (texto completo); art. 72 solo como remisión del art. 53.3.
- Orden HFP/311/2023 (`BOE-A-2023-8119_...pdf`): íntegra (arts. 1–2, disposiciones derogatoria y final).
- Ley 31/2022: `cifras_anuales` de `normativa.yaml` (disposición adicional cuadragésima segunda, Uno y Dos; prórroga). No se abrió el HTML.
- LPAC art. 30.2 (`lpac.txt` de scratchpad, extraído del PDF/HTML del snapshot).
- `cambios_pendientes` de LGT, RGR, Orden HFP/311/2023 y Ley 31/2022: vacíos; no hay marcas de RDL.

## 2. Preguntas del pack (id → sección)
- 2025-44 → Aplazamiento / Efectos de la solicitud (65.5)
- 2025-48 → Intereses (65.4)
- 2025-57 → Régimen legal (65.1)
- 2024-55 → Inadmisión (47.3)
- 2024-58 → Plazos de pago (62.2, 62.3 «dos meses», 62.4)
- 2024-89 → Régimen legal (65.2.b, inadmisión) y Garantías (Orden 311/2023 art. 2; 82.1 sin plazo de 10 días para aportar garantía)
- 2023-9 → Legitimación (33.1)
- 2023-20 (anulada, reference) → Medios de pago en efectivo (38.1–3)
- 2023-76 → Garantías (48.6)
- 2022-58 → Tramitación y resolución (52.1–2)
- 2022-60 → Plazos de pago (68.2)
- 2022X-60 → Imputación (63.1)
- 2022X-61 → Garantías (48.2)
- 2022X-65 → Plazos de pago (tabla 62.2, 62.1, 62.3 con 1 de septiembre)
- 2022X-66 → Plazos de pago (62.4)
- 2022X-67 → Legitimación y lugar (28.1)
- 2022X-69 (reference, tema III.11) → Solicitud (46.1.a) y Efectos de la solicitud (65.5)
- 2021-63 (reference) → Tramitación y resolución (52.4.a) y Plazos (62.2)
- 2021-64 (reference) → no está: es la Orden EHA/1658/2009, fuera del programa y de las normas de la lección; además el ledger señala la clave como discutida.
- 2021-67 (reference) → Imputación (63.3)
- 2021-68 (reference) → no está: la distribución de competencias por importes está en una resolución interna de la AEAT que no está en el snapshot; solo se da el art. 45.1 RGR.
- 2021-71 → Legitimación y lugar (17.2, 20.2)
- 2021-72, 2020-54 → Legitimación y lugar (13.3)
- 2021-73 → Legitimación y lugar (el hecho, día 18, está en el art. 29.1 RGR del snapshot, no en el 19 que cita el pack; el art. 19 no lo contiene)
- 2020-65 → Tramitación y resolución (52.4)
- 2020-67 → Falta de pago (54.2)
- 2020-69, 2020-76 → Plazos de pago (62.2, 62.3). La liquidación de cuenta corriente tributaria no se menciona en la lección (art. 142.3 RGAT remite al 62.2, es de III.10 y no se cita allí).
- 2020-73 → Legitimación y lugar (16.2)

## 3. «Lo que más cae» → preguntas
1 → 2020-76, 2022X-65, 2024-58 (62.3); 2 → 2020-69, 2021-63, 2022X-65, 2024-58 (62.2); 3 → 2022X-66, 2024-58; 4 → 2025-44, 2022X-69; 5 → 2023-76; 6 → 2022X-61; 7 → 2025-48; 8 → 2024-89; 9 → 2024-55; 10 → 2022X-60.

## 4. Ejemplos
- Plazos del art. 62.2: fechas comprobadas con `python3 -c "import datetime…"`: jueves 14-01-2027, sábado 20-02-2027, lunes 22-02-2027; martes 20-04-2027, sábado 05-06-2027, lunes 07-06-2027. Sábado inhábil por art. 30.2 LPAC (supletoria, art. 7.2 LGT). No he mirado festivos locales (ningún festivo nacional cae en 22-02 ni 07-06 de 2027).
- Intereses del aplazamiento: miércoles 15-04-2026, jueves 12-03-2026, lunes 20-04-2026, lunes 20-07-2026 comprobados; 21-04 a 20-07-2026 = 91 días con ambos extremos incluidos (python: `(d(2026,7,20)-d(2026,4,21)).days+1`). El día-base anual no lo fija ninguna norma del snapshot (grep de 365/366 en LGT y RGR sin resultado); el ejemplo da días y tipos y no cifra en euros.

## 5. Resumen para `course.yaml`
La deuda tributaria se extingue por pago, prescripción, compensación, condonación y los demás medios que prevén las leyes. El pago se rige por la LGT y el RGR en forma, momento, plazos, imputación y consignación, y el aplazamiento y fraccionamiento exige solicitud, garantía (con el límite exento de 50.000 euros) e intereses de demora.

## 6. Glosario propuesto
- id: g-efectos-timbrados
  es: efectos timbrados
  origin: m03-l09
  definition: {es: «Tienen la condición de efectos timbrados: el papel timbrado común, el papel timbrado de pagos al Estado, los documentos timbrados especiales, los timbres móviles y los aprobados por orden del Ministro de Economía y Hacienda» (art. 39.1 RGR).}
- (ninguno más: «consignación», «imputación» y «aplazamiento» no están definidos por la norma.)

## 7. Citas sin resolver, omisiones, ambigüedades
- cites.py: 142 citas, 0 sin resolver.
- Pack 2024-58: el «evidencia R0a» y la clave D son coherentes con el snapshot (el art. 62.3 dice «dos meses»; la pregunta pone «un mes» en el distractor).
- Omitido por falta de programa/preguntas: pago en especie (art. 40 RGR, solo se cita art. 60.2 LGT), art. 62.5–9 LGT (el 62.5 es de III.11), art. 65.6 LGT (créditos de otros Estados), arts. 46.2, 46.4–5, 49 y 50 RGR (contenido de la solicitud, medidas cautelares, dispensa), 48.4 y 48.8–11, 51.1, 52.3, 54.3–5 RGR, art. 35.2, 36.1–2, 38.4–5 y 41–42 RGR.
- Dos fuentes que difieren: ninguna.
