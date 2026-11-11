# m03-l03 — notas del redactor

## 1. Fuentes
- LGT (`BOE-A-2003-23186_lgt_2024-12-21.pdf`): arts. 1–16, 17–28 (art. 26: interés de demora; art. 27: recargos), 49–58. Texto del snapshot, leído entero en esos rangos.
- Ley 31/2022 (`cifras_anuales` de `normativa.yaml`, DA cuadragésima segunda, Uno y Dos): 4,0625 % interés de demora y 3,25 % interés legal para 2026, por prórroga. No he abierto el HTML; las cifras y el texto salen de `normativa.yaml`.
- Código Civil: solo nombrado en el art. 12.1 LGT.

## 2. Preguntas del pack (13 coverage, 9 reference)
- 2025-4, 2024-96, 2023-47, 2021-33 (56): sección «Cuota tributaria» (56.1, 56.3, 56.4, 56.5, 56.6). El distractor «aumentarse de oficio» queda desmentido por 56.3 («reducirse»).
- 2025-26, 2020-48 (54, 55.1): «Base liquidable», «Tipo de gravamen».
- 2024-18, 2024-61, 2023-95, 2022-46, 2021-58 (27.2): sección «Recargos por declaración extemporánea» y dos ejemplos. La reducción del 25 % (27.5) está en la lección; el 40 % del distractor de 2022-46 es falso en este snapshot.
- 2024-66, 2020-35, 2020-46 (2.2): sección «Los tributos». El precio público no tiene definición en la LGT; la lección lo dice.
- 2022-61 (25.2), 2021-41 (58): «Obligaciones accesorias», «Deuda tributaria».
- 2022X-32, 2021-40, 2022X-37, 2020-42 (20, 21.1, 22): «Hecho imponible», «Devengo». 2021-40 (exención/no sujeción): frase de 20.2 y 22, sin atribuir a la LGT una definición de no sujeción que no tiene.
- 2022X-33 (10.1), 2022X-36 (8.a): «Vigencia…», «Reserva de ley».
- No está: nada.

## 3. «Lo que más cae» → preguntas
1: 2024-18, 2024-61, 2022-46, 2021-58. 2: 2023-95. 3: 2025-4, 2020-48. 4: 2023-47, 2021-33. 5: 2024-96. 6: 2022X-32. 7: 2022X-37, 2020-42. 8: 2022-61. 9: 2024-66, 2020-35. 10: 2025-26.

## 4. Ejemplos
Dos ejemplos del art. 27.2 (menos de 12 meses; más de 12 meses). Fechas comprobadas con `python3 datetime`: 20-04-2026 lunes, 22-07-2026 miércoles; 20-01-2025 lunes, 20-03-2026 viernes. Meses completos y 12 meses contados de fecha a fecha. En el segundo no calculo el importe de los intereses: el artículo no fija el criterio de cómputo de días y no lo invento; doy período y tipo anual.

## 5. Resumen para course.yaml
La lección recorre la LGT desde sus principios y fuentes hasta la deuda tributaria. Explica el hecho imponible, el devengo, la base, el tipo y las tres cuotas, con los intereses de 2026. Resuelve con dos ejemplos el recargo por declaración extemporánea del artículo 27.2.

## 6. Propuestas de glosario (ninguna existe en `glossary.yaml`)
```yaml
- id: g-hecho-imponible
  es: hecho imponible
  origin: m03-l03
  definition: {es: «El presupuesto fijado por la ley para configurar cada tributo y cuya realización origina el nacimiento de la obligación tributaria principal» (art. 20.1 LGT).}
- id: g-devengo
  es: devengo
  origin: m03-l03
  definition: {es: «El momento en el que se entiende realizado el hecho imponible y en el que se produce el nacimiento de la obligación tributaria principal» (art. 21.1 LGT).}
- id: g-base-liquidable
  es: base liquidable
  origin: m03-l03
  definition: {es: «La magnitud resultante de practicar, en su caso, en la base imponible las reducciones establecidas en la ley» (art. 54 LGT).}
- id: g-tipo-de-gravamen
  es: tipo de gravamen
  origin: m03-l03
  definition: {es: «La cifra, coeficiente o porcentaje que se aplica a la base liquidable para obtener como resultado la cuota íntegra» (art. 55.1 LGT).}
- id: g-cuota-liquida
  es: cuota líquida
  origin: m03-l03
  definition: {es: «El resultado de aplicar sobre la cuota íntegra las deducciones, bonificaciones, adiciones o coeficientes previstos, en su caso, en la ley de cada tributo» (art. 56.5 LGT).}
- id: g-cuota-diferencial
  es: cuota diferencial
  origin: m03-l03
  definition: {es: «El resultado de minorar la cuota líquida en el importe de las deducciones, pagos fraccionados, retenciones, ingresos a cuenta y cuotas, conforme a la normativa de cada tributo» (art. 56.6 LGT).}
- id: g-deuda-tributaria
  es: deuda tributaria
  origin: m03-l03
  definition: {es: «La cuota o cantidad a ingresar que resulte de la obligación tributaria principal o de las obligaciones de realizar pagos a cuenta», más, en su caso, el interés de demora y los recargos (art. 58.1–2 LGT).}
```

## 7. Pendiente
- Citaciones sin resolver: ninguna (`cites.py`: 111 citaciones, 0 sin resolver).
- En la sección de cuota tributaria no incluyo el art. 57 (comprobación de valores): no lo nombra el programa y ninguna pregunta lo pide.
- Art. 28 (recargos del período ejecutivo) solo aparece nombrado en 25.1, 26.2.d) y 58.2: es materia de III.9.
