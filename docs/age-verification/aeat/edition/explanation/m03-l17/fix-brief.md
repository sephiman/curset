# Fix brief — `m03-l17`

## caso:### Actividad económica y entidad patrimonial#1

Current: Lucía, S.L. alquila un local y no emplea a nadie con contrato laboral y jornada completa para ordenar el arrendamiento: no hay actividad económica (art. 5.1 LIS). Con una persona empleada con contrato laboral y jornada completa sí la habría (art. 5.1 LIS). Su activo suma 900.000 euros y 500.000 son valores: más de la mitad, así que es entidad patrimonial (art. 5.2 LIS).

Blind verifier: FAIL — El arrendamiento sin empleado a jornada completa no es actividad económica (art. 5.1), pero «Su activo suma 900.000 euros y 500.000 son valores: más de la mitad, así que es entidad patrimonial» trata cualquier valor como computable y una sola cifra de activo como la medida: el art. 5.2 excluye como valores los de las letras a) a d) (p. ej., participaciones de al menos el 5 % poseídas un año con organización de medios) y mide activo y valores por la media de los balances trimestrales del ejercicio.
Student reader: KEEP — The 900.000 / 500.000 arithmetic and the with/without employee contrast let me apply both tests to new facts.

## caso:### Contribuyentes del impuesto#1

Current: Textil Norte, S.L., sociedad mercantil residente en territorio español con domicilio fiscal en Las Palmas, es contribuyente (arts. 2.1, 7.1.a) y 8.1 LIS). Una sociedad civil sin objeto mercantil queda excluida de la letra a) y sus rentas se atribuyen a los socios (arts. 6.1 y 7.1.a) LIS). Textil Norte obtiene 80.000 euros en Madrid y 20.000 en Portugal de un pagador portugués: se grava por los 100.000 euros (art. 7.2 LIS).

Blind verifier: PASS — Persona jurídica residente, por tanto contribuyente (arts. 2.1, 7.1.a y 8.1); la sociedad civil sin objeto mercantil queda excluida de la letra a) y sus rentas se atribuyen (art. 6.1); se grava la renta mundial, 80.000 + 20.000 = 100.000 (art. 7.2).
Student reader: REWRITE — The sociedad civil sentence is a bare rule with no facts; give it a concrete civil partnership (or drop it) and keep the 80.000 + 20.000 example.

## caso:### Exenciones#1

Current: El Colegio de Ingenieros de Soria es un colegio profesional del artículo 9.3.c) y tiene el régimen del capítulo XIV (arts. 9.3 y 109 LIS). En 2026 recibe 30.000 euros de cuotas de colegiados, sin derecho a una prestación de actividad económica, y 12.000 euros de cursos de pago. Las cuotas están exentas (art. 110.1.a LIS). La exención no alcanza a los rendimientos de actividades económicas (art. 110.2 LIS).

Blind verifier: PASS — Colegio profesional del art. 9.3.c) al que se aplica el capítulo XIV (art. 109); las cuotas de colegiados sin derecho a una prestación de actividad económica están exentas (art. 110.1.a); la exención no alcanza a los rendimientos de actividades económicas (art. 110.2).
Student reader: REWRITE — It never says what happens to the 12.000 euros of paid courses; state they are not exempt (economic activity) and are taxed.

## caso:## Reglas de imputación temporal#1

Current: Ruiz y Cía, S.L. presta un servicio en noviembre de 2026 y lo cobra en febrero de 2027: el ingreso se imputa al período en que se devenga, con independencia del cobro (art. 11.1 LIS). Vende un inmueble por 300.000 euros con tres pagos anuales iguales, el último a los dos años: es operación a plazos y la renta se entiende obtenida a medida que son exigibles los cobros, salvo que aplique el criterio del devengo (art. 11.4 LIS).

Blind verifier: PASS — Imputación por devengo con independencia del cobro (art. 11.1); tres plazos anuales con el último a los dos años: más de un año entre devengo y vencimiento, así que es operación a plazos y la renta se imputa conforme sean exigibles los cobros, salvo que se opte por el devengo (art. 11.4).
Student reader: REWRITE — The instalment sale says "a medida que son exigibles" but never says how much goes to each year (100.000 per year); add the split.

## caso:### Reserva de capitalización#1

Current: Delta, S.L., con el tipo general del artículo 29.1, incrementa sus fondos propios en 200.000 euros en 2026. La reducción es el 20 por ciento del incremento: 40.000 euros (art. 25.1 LIS). Debe mantener el incremento 3 años desde el cierre del jueves 31 de diciembre de 2026 y dotar una reserva (art. 25.1 LIS). Con base positiva previa de 150.000 euros y 5.000.000 de cifra de negocios, no puede superar 30.000 euros, el 20 por ciento (art. 25.1 LIS).

Blind verifier: FAIL — «La reducción es el 20 por ciento del incremento: 40.000» omite que el art. 25.1 eleva el porcentaje al 23, 26,5 o 30 % según aumente la plantilla media; y «no puede superar 30.000 euros» calla que el exceso de 10.000 se aplica en los períodos que terminen en los 2 años siguientes (art. 25.1, último párrafo), así que el lector entiende que se pierde. Tampoco recoge la salvedad de las pérdidas contables en el mantenimiento del incremento (art. 25.1.a).
Student reader: KEEP — Computing 40.000 and then capping it at 20 % of 150.000 = 30.000 is exactly the sequence I would repeat.

## caso:### Tipo de gravamen#1

Current: Café Sol, S.L. tuvo en el período impositivo inmediato anterior un importe neto de la cifra de negocios de 3.000.000 euros. No es inferior a 1 millón de euros, por lo que aplica el tipo general del 25 por ciento (art. 29.1 LIS). Una entidad con cifra de negocios inferior a 1 millón aplicaría la escala del artículo 29.1, salvo que deba tributar a un tipo diferente del general (art. 29.1 LIS).

Blind verifier: FAIL — «No es inferior a 1 millón de euros, por lo que aplica el tipo general del 25 por ciento» omite que el mismo art. 29.1 fija el 20 % para las entidades que cumplan el art. 101; con una cifra de negocios de 3 millones, Café Sol está por debajo del umbral de reducida dimensión, así que la conclusión depende de una condición que el caso no menciona.
Student reader: REWRITE — Only the 25 % branch is worked and the scale branch is left abstract; add a sub-1M entity with a base over 50.000 (and note the 2026 rates).

## caso:### Tributación mínima#1

Current: Gran Textil, S.L. tuvo una cifra de negocios de 25.000.000 euros en los 12 meses anteriores al inicio del período, al menos 20 millones. Su base imponible es de 10.000.000 euros, sin ajustes del artículo 105 LIS. Por superar ese umbral, su cuota líquida mínima se calcula con el artículo 30 bis (art. 30 bis.1 LIS). No puede ser inferior al 15 por ciento de la base, 1.500.000 euros, aunque las deducciones la dejaran en 800.000 (art. 30 bis.1 LIS).

Blind verifier: FAIL — «No puede ser inferior al 15 por ciento de la base, 1.500.000 euros, aunque las deducciones la dejaran en 800.000» es falso para las bonificaciones y las deducciones por doble imposición (arts. 31, 32, 100): según el art. 30 bis.2.a, si estas dejan la cuota por debajo del mínimo, esa cuantía pasa a ser la cuota líquida mínima. Además, esa regla está en el apartado 2, no en el 30 bis.1 que se cita.
Student reader: KEEP — 15 % of 10.000.000 as a floor against 800.000 after deductions is clear.

## caso:### Doble imposición jurídica: impuesto soportado por el contribuyente#1

Current: Bahía, S.L. integra una renta positiva de 100.000 euros obtenida y gravada en Francia por un impuesto idéntico o análogo, y pagó allí 30.000 euros. En España esa renta correspondería a una cuota íntegra de 25.000 euros. Se deduce la menor de las dos cantidades: 25.000 euros (art. 31.1 LIS). Si hubiera pagado 18.000 euros, deduciría 18.000 (art. 31.1.a LIS).

Blind verifier: FAIL — El cálculo de la menor cantidad es correcto (art. 31.1), pero la renta se grava en Francia, con la que España tiene convenio, y el art. 31.1.a dispone que «siendo de aplicación un convenio, la deducción no podrá exceder del impuesto que corresponda según aquél». El caso toma los 30.000 o los 18.000 pagados sin ese límite, así que el lector deduce lo pagado en el extranjero sin tope.
Student reader: KEEP — Both outcomes (25.000 and 18.000) show the lower-of rule.

## caso:### Doble imposición económica internacional: dividendos y participaciones en beneficios#1

Current: Atlas, S.L. posee desde el 2 de marzo de 2026 el 6 por ciento de una sociedad alemana, que distribuye un dividendo exigible el lunes 15 de marzo de 2027. Atlas lo incluye en su base imponible. Se deduce el impuesto efectivamente pagado por la alemana respecto de esos beneficios (art. 32.1 LIS). La participación supera el 5 por ciento y se poseyó de forma ininterrumpida el año anterior a esa fecha (art. 32.1 LIS).

Blind verifier: FAIL — «Se deduce el impuesto efectivamente pagado por la alemana respecto de esos beneficios» omite «en la cuantía correspondiente de tales dividendos» y que esa cuantía se incluya en la base (art. 32.1), así como el límite de la cuota española del art. 32.4; con un 6 % el lector entendería que deduce todo el impuesto pagado por la filial. Fechas y requisitos de participación correctos: 15-3-2027 es lunes, ≥ 5 % y tenencia de un año.
Student reader: KEEP — The 6 % holding and the more-than-a-year dates test both requirements on facts.

