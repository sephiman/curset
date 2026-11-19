# Fix brief — `m03-l12`

## caso:## Facultades de la recaudación#1

Current: El lunes 2 de marzo de 2026 un funcionario de recaudación requiere a Víctor una relación de bienes y derechos de su patrimonio en cuantía suficiente para cubrir una deuda de 18.000 euros (art. 162.1 LGT). Víctor no cumple el requerimiento. Previo apercibimiento, el órgano competente puede acordar la ejecución subsidiaria de lo requerido (art. 162.2 LGT).

Blind verifier: FAIL — «Víctor no cumple el requerimiento. Previo apercibimiento, el órgano competente puede acordar la ejecución subsidiaria de lo requerido (art. 162.2 LGT)»: 162.2 allows ejecución subsidiaria of the resolutions or requerimientos dictated «al efecto» of the actuaciones materiales of apremio; it does not attach it to the 162.1 duty to declare a relación de bienes, which is a personal act nobody else can perform. The case teaches a wrong consequence for not providing the list. Weekday (lunes 2-3-2026) correct.
Student reader: CUT — It narrates the rule without a decision or number; the 18.000 and the weekday add nothing.

## caso:### Establecimientos mercantiles e industriales#1

Current: El martes 10 de marzo de 2026 se embarga el bar de Paula, en un local arrendado. El embargo se inicia mediante personación en el establecimiento (art. 90.1 RGR). Se extiende diligencia con el inventario de los bienes y derechos existentes y de los que se embargan (art. 90.2 RGR). Al estar arrendado el inmueble, se notifica al arrendador (art. 90.4 RGR). Puede acordarse el precinto o el nombramiento de un funcionario administrador o interventor (art. 90.6 RGR).

Blind verifier: FAIL — «Puede acordarse el precinto o el nombramiento de un funcionario administrador o interventor (art. 90.6 RGR)» drops the conditions of 90.6.b: the nombramiento requires that the continuity of the persons running the business could harm the obligado's solvency and prior audiencia of the titular; the case presents it as a free option alongside the precinto.
Student reader: CUT — A list of steps restated with a bar as the example.

## caso:### Formas de enajenación#1

Current: En 2026 se enajenan bienes embargados a Silvia. Las formas de enajenación son la subasta pública, el concurso o la adjudicación directa (art. 100.1 RGR). La subasta es el procedimiento ordinario y procede siempre que no sea expresamente aplicable otra forma (art. 100.2 RGR). Es única y se realiza por medios electrónicos en el Portal de Subastas de la Agencia Estatal Boletín Oficial del Estado (art. 100.2 RGR).

Blind verifier: FAIL — «Es única y se realiza por medios electrónicos en el Portal de Subastas de la Agencia Estatal Boletín Oficial del Estado (art. 100.2 RGR)» drops the exception in the same paragraph: «con la única excepción de aquellos supuestos en los cuales la ejecución material se encargue ... a empresas o profesionales especializados». Also 100.1 «salvo los procedimientos específicos de realización» is dropped. The reader is left with an absolute rule the article qualifies.
Student reader: CUT — It copies the list of forms and the rule on subasta.

## caso:### Desarrollo de la subasta#1

Current: Una subasta sin cargas con tipo de 90.000 euros se abre el lunes 9 de marzo de 2026. Las pujas duran veinte días naturales desde la apertura, hasta el domingo 29 de marzo (art. 104.2 RGR). La puja mínima es el 10 por ciento del tipo, 9.000 euros (art. 104.3 RGR). Con una puja a las 23:30 del 29 de marzo, la subasta no se cierra hasta pasada una hora, con ampliación máxima de 24 horas (art. 104.3 RGR).

Blind verifier: PASS — 20 días naturales from lunes 9-3-2026 → domingo 29-3-2026; puja mínima 10 % = 9.000 (no cargas, so the 25 % exception does not apply); one-hour extension with a 24-hour cap (104.2, 104.3).
Student reader: REWRITE — The last-minute bid at 23:30 is explained without the closing time, so the extension cannot be followed; state when the period ends.

## caso:### Enajenación por concurso#1

Current: La subasta de las existencias embargadas a una empresa, por su magnitud, podría producir perturbaciones nocivas en el mercado, y procede el concurso (art. 106.1 RGR). Terminado el plazo de admisión de ofertas el viernes 6 de marzo de 2026, el órgano competente decide adjudicarlo o declararlo desierto en cinco días, hábiles, hasta el viernes 13 de marzo (art. 106.3 RGR; art. 30.2 LPAC). Si lo declara desierto, puede procederse a la adjudicación directa (art. 106.3 RGR).

Blind verifier: FAIL — «podría producir perturbaciones nocivas en el mercado, y procede el concurso (art. 106.1 RGR)»: 106.1 says the enajenación «sólo podrá celebrarse por concurso» in those cases (a restriction, not a rule that it applies), and 106.2 requires that the concurso «deberá ser autorizado por el órgano competente», a condition the case omits. Day count (viernes 6-3 → viernes 13-3, five hábiles) is right.
Student reader: KEEP — Why concurso applies and the five working days to 13 March are clear.

## caso:### Costas del procedimiento de apremio#1

Current: En un apremio contra Iván la Administración abona 600 euros a un perito ajeno que valora los bienes embargados y 300 a un registrador por una anotación. Ambos gastos son costas y se exigen al obligado al pago (art. 113.1 y 113.2 RGR). Los gastos ordinarios de los órganos de la Administración no pueden incluirse como costas (art. 113.3 RGR).

Blind verifier: PASS — Perito ajeno (113.2.a) and registrador (113.2.b) are costas exigible to the obligado (113.1); gastos ordinarios excluded (113.3).
Student reader: REWRITE — It shows only costs, not the excluded ordinary expenses; add one expense that does not count.

## caso:### Responsabilidad solidaria#1

Current: El período voluntario de pago original de una deuda termina el viernes 20 de noviembre de 2026. A Ismael se le declara y notifica la responsabilidad el lunes 2 de noviembre: basta requerirle el pago una vez transcurrido ese período (art. 175.1.a LGT). A Marga no se le había notificado antes: transcurrido el período, el órgano competente dicta el acto de declaración de responsabilidad y se le notifica (art. 175.1.b LGT).

Blind verifier: PASS — 175.1.a (declared and notified before vencimiento of the original voluntary period, viernes 20-11-2026 → requerimiento after it) and 175.1.b (otherwise acto de declaración after the period) correct; lunes 2-11-2026 correct.
Student reader: REWRITE — "A Marga no se le había notificado antes" does not say before what, so the contrast with Ismael is unclear.

## caso:## Procedimiento de recaudación frente a los sucesores#1

Current: Dolores falleció el martes 3 de marzo de 2026, en período voluntario. El procedimiento continúa con sus herederos sin más requisitos que la constancia del fallecimiento y la notificación (art. 177.1 LGT), y se les requiere el pago dentro del plazo del artículo 62.2 LGT (art. 127.1.a RGR). Ricardo falleció el miércoles 10 de junio de 2026, después del plazo del artículo 62.5 LGT: se requiere a su sucesor la deuda y el recargo de apremio ordinario (art. 127.1.d RGR).

Blind verifier: PASS — 177.1 LGT and 127.1.a RGR (death in voluntary period → plazo del 62.2) and 127.1.d (after the 62.5 plazo → deuda and recargo de apremio ordinario); martes 3-3 and miércoles 10-6-2026 correct.
Student reader: REWRITE — It leans on art. 62.2 and 62.5 deadlines the reader is not told; state which dates they are.

