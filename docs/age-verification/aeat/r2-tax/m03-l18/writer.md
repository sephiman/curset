# m03-l18 — notas del redactor

## 1. Fuentes
- LIVA (`BOE-A-1992-28740_liva_2026-10-07.pdf`, `pdftotext -layout`): arts. 1–3, 4–7, 8–9, 11–13, 20 (apartados Uno y Dos), 21, 22 (Uno y Trece; los demás apartados solo como «entre otras»), 23–25 (solo títulos), 68–70.
- Código de Comercio (art. 3), Concierto Económico (Ley 12/2002) y Convenio Económico con Navarra (Ley 28/1990): nombrados dentro del art. 5.Tres y 2.Uno; listados «nombrado en» sin precepto (Concierto, Convenio).
- RIVA y RD 1619/2012: no se citan (ninguna pregunta de este pack las pide). El plan decía «RIVA as asked»: nada pedido.
- RDL 29/2026, art. 7 (`BOE-A-2026-20823_rdl-29-2026_2026-10-07.pdf`, líneas 4146–4230 del texto): cambia solo 20.Uno.23.º e´) y los arts. 91.Uno.2.2.º, 91.Uno.2.10.º y 91.Dos.1.6.º, todos con efectos desde 01-12-2026. La lección no cita el art. 20.Uno.23.º (ninguna pregunta lo pide) ni el 91: no hay marca RDL en el texto y retiré del bloque «Normativa» la línea «Cambio pendiente por el RDL 29/2026» del stub, porque la spec la admite solo para preceptos citados.
- Los arts. 3.Uno (mar territorial) y 5.Tres/6.Tres.c) nombran la Ley 10/1977 y el Código Civil; los omití (no son del programa ni de ninguna pregunta); 7.8.º C)–E) menciona la Ley de Contratos del Sector Público (no está en `normativa.yaml`): solo cito 7.8.º A) y F) y una frase estructural sobre C)–E).

## 2. Preguntas del pack (15 coverage + 3 reference = 18)
- 2025-8 (13.2.ª): «Adquisiciones intracomunitarias de bienes». 2025-49 (7.8.º A; 9.1.º a)): «Operaciones no sujetas», «autoconsumo»; las opciones a)–c) las desmienten 7.9.º, 7.2.º/7.3.º, 7.8.º A).
- 2025-55 y 2022X-89 (12): «Operaciones asimiladas a las prestaciones de servicios». 2025-66, 2023-36, 2022-91, 2021-97 (reference) (8.Dos.1.º–7.º; 8.Dos.5.º párrafo de asimilación; 11.Dos.2.º y 16.º): «Entregas de bienes» y «Prestaciones de servicios».
- 2025-74 (9.1.º c)): «Operaciones asimiladas a las entregas de bienes: autoconsumo».
- 2024-93 (21.2.º, 21.2.º B), 22.Trece): «Exportaciones y operaciones asimiladas». 2024-95 (7.5.º; 20.Uno.14.º a) para la d), 7.2.º/7.3.º), 2022-92 (7.6.º; 20.Uno.3.º, 4.º, 14.º para a)–c)), 2020-98 (reference; 7.2.º; 20.Uno.20.º y 22.º A para a) y c)): «Operaciones no sujetas» y «Exenciones en operaciones interiores».
- 2024-97 (20.Dos): «Renuncia a las exenciones». 2023-21 y 2020-94 (reference) (20.Uno.22.º A): «Segundas y ulteriores entregas de edificaciones».
- 2023-93 (20.Uno.18.º a); 7.2.º, 7.4.º): «Exenciones en operaciones interiores». 2022-90 (20.Uno.5.º; 20.Uno.2.º c); 7.4.º): ídem.
- Cobertura: los 15 coverage tienen su hecho en la lección.

## 3. «Lo que más cae» → preguntas
1: 2023-36, 2022-91, 2025-66. 2: 2024-95, 2022-92. 3: 2025-49, 2023-93, 2020-98. 4: 2025-74, 2025-49. 5: 2025-55, 2022X-89. 6: 2023-21, 2020-94. 7: 2024-97. 8: 2022-90, 2023-93. 9: 2024-93. 10: 2025-8.

## 4. Ejemplos
Ninguno: el plan no lista ejemplos para III.18 y no hay regla de cómputo aplicada paso a paso.

## 5. Resumen para `course.yaml`
El IVA es un tributo indirecto que recae sobre el consumo y grava las entregas de bienes y prestaciones de servicios de empresarios o profesionales, las adquisiciones intracomunitarias y las importaciones. La lección recorre el hecho imponible, el concepto de empresario o profesional, las operaciones no sujetas, el autoconsumo, las exenciones del artículo 20, las exportaciones y el lugar de realización de entregas y servicios. Cada regla va con el artículo de la LIVA que la fija.

## 6. Propuestas de glosario (ids no existentes en `glossary.yaml`)
```yaml
- id: g-empresario-o-profesional
  es: empresario o profesional
  origin: m03-l18
  definition:
    es: «Las actividades empresariales o profesionales son las que impliquen la ordenación por cuenta propia de factores de producción materiales y humanos o de uno de ellos, con la finalidad de intervenir en la producción o distribución de bienes o servicios» (art. 5.Dos LIVA). Las sociedades mercantiles se reputan empresarios o profesionales, salvo prueba en contrario (art. 5.Uno.b) LIVA).
- id: g-edificaciones
  es: edificaciones
  origin: m03-l18
  definition:
    es: A efectos del IVA, las construcciones unidas permanentemente al suelo o a otros inmuebles, efectuadas tanto sobre la superficie como en el subsuelo, que sean susceptibles de utilización autónoma e independiente (art. 6.Uno LIVA).
- id: g-autoconsumo-de-bienes
  es: autoconsumo de bienes
  origin: m03-l18
  definition:
    es: Operación asimilada a las entregas de bienes a título oneroso; incluye, sin contraprestación, la transferencia de bienes corporales del patrimonio empresarial o profesional al patrimonio personal o al consumo particular del sujeto pasivo (art. 9.1.º a) LIVA).
- id: g-medios-de-transporte-nuevos
  es: medios de transporte nuevos
  origin: m03-l18
  definition:
    es: Los vehículos terrestres a motor, embarcaciones y aeronaves que superen los umbrales del art. 13.2.ª LIVA y cuya entrega se efectúe antes de los tres meses siguientes a su primera puesta en servicio (seis para los vehículos terrestres), o que no superen 6.000 kilómetros, 100 horas de navegación o 40 horas de vuelo (art. 13.2.ª LIVA).
- id: g-sede-de-la-actividad-economica
  es: sede de la actividad económica
  origin: m03-l18
  definition:
    es: El lugar en el que los empresarios o profesionales centralizan la gestión y el ejercicio habitual de su actividad empresarial o profesional (art. 69.Tres.1.º LIVA).
```

## 7. Citas sin resolver, hechos omitidos, ambigüedades
- `cites.py m03-l18`: 104 citas, 0 sin resolver. La gramática exige la letra pegada con punto tras el ordinal («art. 20.Uno.18.º.a) LIVA», «art. 22.Uno»): la forma con espacio («18.º a)») y los apartados Trece/Catorce (no están en la lista de apartados deletreados) no se leen. Por eso el apartado Trece del art. 22 va en el texto y la cita es «art. 22 LIVA».
- Omitido por no estar en el programa ni en ninguna pregunta: art. 10 (transformación), art. 8 bis, art. 9.2.º–3.º salvo la transferencia intracomunitaria, 13.1.ª b)–g), 14 (adquisiciones no sujetas), apartados de los arts. 20, 22 y 25 no pedidos, 68.Tres–Seis (solo una frase de estructura), 69.Dos letras salvo a), c), d), 70.Uno.4.º y 6.º–9.º, 71–74.
- 2022X-89, opción c) «Los transportes» y d) «prestaciones de hospitalización» son prestaciones de servicios del art. 11.Dos (8.º, 11.º) y no autoconsumos; la lección lista esos números en el art. 11.
- 2024-95: la opción d) «servicios de biblioteca prestados por entidades de derecho público» es una exención (20.Uno.14.º a)), no una no sujeción; está.
- 2024-93: el pack dice «21 y 22»: la exención de las tiendas libres es el art. 21.2.º B) y la del transporte aéreo el 22.Trece.
- Una nota: el texto extraído de la LIVA pierde el exponente en «48 cm³»; escribí «cm³» (el texto del art. 13.2.ª dice «48 cm» con superíndice).
- Palabras: 5.983.
