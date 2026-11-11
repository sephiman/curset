# m03-l19 — notas del redactor

## 1. Fuentes
- LIVA (`BOE-A-1992-28740_liva_2026-10-07.pdf`, `pdftotext -layout`): arts. 9.1.º c) (definición de sectores diferenciados), 20.Uno.26.º, 75–77, 78–83, 84–87, 88–89, 92–101, 102–106, 107–110, 115–119 (88–89 y 92–110 completos en lo que cito; 111–114, 117 bis, 119.Dos y siguientes no).
- RD 1619/2012 (`BOE-A-2012-14696_..._2026-03-31.pdf`): art. 15.3. El RD 238/2026 cambia los arts. 8.1, 8 bis, 9 y 10: la lección no los cita y quité del bloque «Normativa» la línea «Cambio pendiente» del stub.
- LGT: arts. 124–127, nombrados en el art. 115.Tres LIVA; listados «nombrado en».
- RDL 29/2026: art. 7 cambia 20.Uno.23.º e´) y 91.Uno.2.2.º, 91.Uno.2.10.º, 91.Dos.1.6.º (desde 01-12-2026). Esta lección no cita ninguno de esos preceptos (los tipos, art. 90–91, salieron del programa 2025; las preguntas 2022-94 y 2022X-92 son reference y fuera de temario), así que no hay marca RDL y se quitó la línea de cambio pendiente del stub.
- RIVA: no se cita (el pack solo trae RIVA en preguntas reference de III.4: 2022-44, 2021-48, 2021-52).
- Omitidos por nombrar normas ajenas al curso: art. 80.Tres (plazo de dos meses, remite a la Ley Concursal), art. 9.1.º c) c') (Ley 10/2014), art. 99.Tres tercer párrafo en adelante (Ley Concursal 86.3). La lección dice «con el plazo que el propio apartado fija».

## 2. Preguntas del pack (18 coverage + 11 reference = 29)
- 2025-5 y 2022X-90, 2022-93 (75.Uno.1.º, 75.Uno.4.º, 75.Dos): «Devengo del impuesto». 2025-5: pacto de reserva de dominio, devengo en la posesión (1 de junio; los pagos posteriores no son anticipados). 2022-93: pago anticipado devenga por lo cobrado (75.Dos) y el resto en la puesta a disposición (75.Uno.1.º; frase «En consecuencia…»).
- 2025-38, 2022-97, 2022X-91, 2025-60 (78.Dos.1.º, 3.º, 6.º; 78.Tres.1.º–3.º; 80.Uno.2.º): «Base imponible: regla general» y «Modificación». 2025-60: 100 + 10 + 10 − 5 = 115, no está calculado en la lección; sí las reglas que lo dan.
- 2025-24 (80.Cuatro.A, 80.Cinco.1.ª c) y d)): «Modificación de la base imponible». Ver sección 7.
- 2024-25 y 2025-22 (103.Uno–Dos; 104.Uno, Dos, Tres.3.º; 105.Cuatro): «Regla de prorrata». 2025-22 desmentidas: a) por 104.Uno (no se computan las cuotas de 95 y 96), c) por 103.Uno–Dos, d) por 105.Cuatro (la regularización es en la última declaración, sin umbral).
- 2024-77 (89.Uno), 2022-95 (88.Cuatro), 2022-42 reference (15.3 RD 1619/2012): «Repercusión» y «Rectificación».
- 2024-100 (95.Tres.2.ª), 2023-50 (93.Dos, 93.Cuatro, 93.Cinco), 2021-98 reference (94.Tres, 97.Tres): «Requisitos subjetivos» y «Limitaciones».
- 2023-80 y 2022-96 (99.Tres, 99.Cuatro, 98.Uno): «Requisitos formales, nacimiento, ejercicio y caducidad».
- 2023-29 (84.Uno.2.º e)): «Inversión del sujeto pasivo».
- 2022X-93 (108.Uno, 108.Dos.5.º), 2023-24 reference (anulada; 107.Uno, 109, 110.Uno): «Regularización de deducciones por bienes de inversión».
- No está: 2022-44, 2021-48, 2021-52 (RIVA 62.6, 61.2, 71.3: obligaciones formales de III.4), 2021-53 y 2020-100 (RD 1619/2012 arts. 3 y 4.2: III.4; los cita m03-l04), 2022-94 y 2022X-92 (tipos del art. 91, fuera de temario y art. 91 afectado por el RDL 29/2026), 2021-96 (art. 5.Uno.c, está en `m03-l18`, apartado «Concepto de empresario o profesional»).
- Cobertura: los 18 coverage tienen su hecho en la lección.

## 3. «Lo que más cae» → preguntas
1: 2025-5, 2022X-90. 2: 2022-93. 3: 2025-38, 2022-97, 2022X-91, 2025-60. 4: 2025-60. 5: 2025-24. 6: 2023-29. 7: 2022-95, 2024-77. 8: 2023-50, 2024-100. 9: 2023-80, 2022-96. 10: 2024-25, 2025-22.
Quedan sin línea propia (están en el cuerpo): 2022X-93 (108) y 2023-24 (107–110).

## 4. Ejemplos
1. Prorrata general (arts. 102–105): Lucía Martín, año 2025. 640.000 / 900.000 × 100 = 71,11 → 72 %; 45.000 × 65 % = 29.250; 45.000 × 72 % = 32.400; diferencia 3.150. Comprobado con `python3` (math.ceil y productos).
2. Regularización de un bien de inversión (arts. 107–109): Talleres Ribera, S.L., cuota 21.000, 80 % en 2024: 16.800 deducidos; 2025 (85 %, 5 puntos) no; 2026 (60 %, 20 puntos): 16.800 − 12.600 = 4.200 / 5 = 840 ingreso; 2027 (70 %, 10 puntos) no; 2028 (95 %, 15 puntos): 16.800 − 19.950 = −3.150 / 5 = −630 deducción. Comprobado con `python3`.
Fechas: los ejemplos usan solo años naturales, ninguna fecha de calendario ni día hábil; no hubo nada que verificar con `datetime`.

## 5. Resumen para `course.yaml`
El IVA se devenga, entre otros casos, en la puesta a disposición de los bienes y, en los pagos anticipados, en el cobro; la base imponible es la contraprestación total, con las inclusiones, exclusiones y modificaciones del artículo 78 a 80. El sujeto pasivo es normalmente quien entrega o presta, y en las operaciones del artículo 84.Uno.2.º lo es el empresario destinatario; la repercusión se hace en factura y se pierde al año del devengo. La deducción exige requisitos subjetivos y formales, tiene limitaciones, se calcula con la prorrata del artículo 104 y se regulariza en los bienes de inversión durante cuatro años (nueve en terrenos y edificaciones).

## 6. Propuestas de glosario (ids no existentes)
```yaml
- id: g-bienes-de-inversion
  es: bienes de inversión
  origin: m03-l19
  definition:
    es: «Los bienes corporales, muebles, semovientes o inmuebles que, por su naturaleza y función, estén normalmente destinados a ser utilizados por un período de tiempo superior a un año como instrumentos de trabajo o medios de explotación» (art. 108.Uno LIVA).
- id: g-regla-de-prorrata
  es: regla de prorrata
  origin: m03-l19
  definition:
    es: Regla que se aplica cuando el sujeto pasivo efectúa conjuntamente operaciones que originan el derecho a la deducción y otras de análoga naturaleza que no lo habilitan; tiene dos modalidades, general y especial (arts. 102.Uno y 103.Uno LIVA).
- id: g-sectores-diferenciados
  es: sectores diferenciados de la actividad empresarial o profesional
  origin: m03-l19
  definition:
    es: Entre otros, los sectores en los que las actividades económicas realizadas y los regímenes de deducción aplicables sean distintos, las actividades de los regímenes especiales simplificado, de agricultura, ganadería y pesca, de oro de inversión y de recargo de equivalencia, el arrendamiento financiero y la cesión de créditos o préstamos, con excepción del «factoring» (art. 9.1.º c) LIVA).
```

## 7. Citas sin resolver, hechos omitidos, ambigüedades
- `cites.py m03-l19`: 167 citas, 0 sin resolver (misma regla de letra pegada con punto: «art. 84.Uno.2.º.e)»).
- 2022X-93, opción a): «igual o superior a quinientas mil pesetas (3.005,06 euros)». El art. 108.Dos.5.º del snapshot dice «inferior a quinientas mil pesetas» y no trae el equivalente en euros; la lección cita solo las pesetas (no inventé la conversión). Puede decidir si añade «3.005,06 euros» con fuente (conversión legal) en otra ronda.
- 2025-24: el ledger discute la clave (opción c: 12 meses exactos entre devengo y último vencimiento, no «superior a un año»). La lección enuncia el art. 80.Cuatro.A.1.ª tal cual y no elige.
- 2023-80: clave D cuenta los cuatro años «desde que se soportó»; el art. 99.Tres dice «a partir del nacimiento del mencionado derecho». La lección cita el artículo.
- 2023-24 (anulada): la lección da 107.Uno, 109 y 110.Uno; no estudia el caso.
- Omitido: 79.Cinco–Diez (vinculadas, comisionistas, oro, no pedidos), 84.Uno.2.º c) y g) resumidos con «entre otros», 91 y tipos, 111–114 (cuotas previas al inicio, rectificación de deducciones), 117 bis, 119.Dos y siguientes, 120 y siguientes.
- Palabras: 8.866.
