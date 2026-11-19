# Fix brief — `m03-l18`

## caso:### Territorialidad#1

Current: Una empresa de Barcelona entrega el 16 de marzo de 2027, martes, mercancías a un cliente de Mónaco. El ámbito espacial del impuesto es el territorio español, incluidas las islas adyacentes y el mar territorial hasta el límite de 12 millas náuticas (art. 3.Uno LIVA). Una operación con el Principado de Mónaco tiene la misma consideración que una efectuada con Francia (art. 3.Tres LIVA).

Blind verifier: PASS — El 16-3-2027 es martes; el ámbito espacial incluye las islas adyacentes y el mar territorial hasta 12 millas (art. 3.Uno); las operaciones con Mónaco se tratan como las efectuadas con Francia (art. 3.Tres).
Student reader: REWRITE — It says Mónaco is treated like France but never says what follows for the Barcelona delivery; add the consequence (treated as a delivery to another Member State) or the case teaches nothing applicable.

## caso:### Operaciones asimiladas a las entregas de bienes: autoconsumo#1

Current: Vinos Mar, S.L. transfiere el lunes 12 de abril de 2027 un bien corporal de su empresa de Valencia a un almacén suyo de Lyon, para afectarlo a las necesidades de su empresa allí. Es una operación asimilada a las entregas de bienes a título oneroso (art. 9.3.º LIVA). Si la transferencia se hiciera en el marco de un acuerdo de ventas de bienes en consigna del artículo 9 bis, no tendría esa consideración (art. 9.3.º LIVA).

Blind verifier: FAIL — El 12-4-2027 es lunes y la regla general del art. 9.3.º está bien, pero el caso presenta la venta en consigna como la única salvedad («Si la transferencia se hiciera en el marco de un acuerdo de ventas de bienes en consigna … no tendría esa consideración»). El mismo número 3.º excluye además las transferencias para las operaciones de las letras a) a h), entre ellas el uso temporal en servicios o durante 24 meses como máximo y los trabajos con reexpedición, y el caso no las descarta: lista parcial presentada como completa.
Student reader: KEEP — Transfer to an own warehouse in Lyon, with the consignment exception, is plain.

## caso:### Exenciones en operaciones interiores#1

Current: Clínica Sonrisa presta a Hugo en 2027 servicios de odontología y le coloca una prótesis dental, cualquiera que sea la persona a cuyo cargo se realicen: están exentos (art. 20.Uno.5.º LIVA). Un veterinario trata además al perro de Hugo: los servicios veterinarios quedan fuera de la exención de la asistencia sanitaria (art. 20.Uno.2.º LIVA).

Blind verifier: FAIL — El art. 20.Uno.5.º exime los servicios prestados «en el ámbito de sus respectivas profesiones por estomatólogos, odontólogos, mecánicos dentistas y protésicos dentales» y la colocación de prótesis «realizadas por los mismos». El caso solo dice «Clínica Sonrisa presta … servicios de odontología» y omite que los presten esos profesionales, condición de la que depende la exención. La exclusión de los servicios veterinarios (art. 20.Uno.2.º.c) es correcta.
Student reader: KEEP — The dental/veterinary contrast shows what is inside and outside the health exemption.

## caso:### Segundas y ulteriores entregas de edificaciones#1

Current: Promotora Sol terminó una edificación el 1 de marzo de 2024; la usó ininterrumpidamente Gloria en arrendamiento sin opción de compra desde el lunes 1 de abril de 2024. El martes 15 de septiembre de 2026 la vende a Inés. Tras una utilización ininterrumpida de dos años o más sin opción de compra, no es primera entrega, salvo que el adquirente sea quien usó la edificación (art. 20.Uno.22.º.A LIVA). Si compra Gloria, lo es (art. 20.Uno.22.º.A LIVA).

Blind verifier: FAIL — Defecto de la entrada: el texto del art. 20 termina en 20.Uno.18.º y no contiene el número 22.º citado, así que el paso no se puede verificar con el artículo de entrada. Fechas comprobadas: el 1-4-2024 es lunes y el 15-9-2026, martes; más de dos años de uso ininterrumpido. El contenido coincide con la regla conocida del 22.º.A, pero hay que regenerar la entrada y volver a verificarlo.
Student reader: KEEP — The dates show the two-year test and the sale to the former tenant is a good exception.

## caso:### Renuncia a las exenciones#1

Current: Inmobiliaria Pino, S.L. entrega el jueves 3 de junio de 2027 un local con exención del número 22.º. El adquirente, Comercial Tajo, S.A., actúa en sus actividades empresariales y tiene derecho a deducir total o parcialmente el impuesto soportado: Pino puede renunciar a la exención (art. 20.Dos LIVA). Cabe también cuando, por su destino previsible, el local se use en operaciones que originen derecho a deducción (art. 20.Dos LIVA).

Blind verifier: FAIL — Defecto de la entrada: el texto del art. 20 termina en 20.Uno.18.º y no incluye el apartado Dos citado, así que ningún paso se puede verificar con el artículo de entrada. El 3-6-2027 es jueves. Hay que regenerar la entrada y volver a verificarlo.
Student reader: KEEP — It states the condition (buyer entitled to deduct) and a clear outcome.

## caso:### Entregas de bienes#1

Current: Muebles Sol, S.L. vende el lunes 12 de abril de 2027 un armario que se pone a disposición del adquirente en Toledo, sin expedición ni transporte (art. 68.Uno LIVA). Se entiende realizada en el territorio de aplicación del impuesto porque el bien se pone a disposición del adquirente en dicho territorio (art. 68.Uno LIVA).

Blind verifier: PASS — El 12-4-2027 es lunes; un bien sin expedición ni transporte puesto a disposición del adquirente en Toledo: se localiza en el territorio de aplicación (art. 68.Uno).
Student reader: REWRITE — A cabinet handed over in Toledo is trivial and shows none of the harder rules (transport, installation); use a shipped-goods case.

## caso:### Límite cuantitativo aplicable a determinadas ventas a distancia intracomunitarias de bienes y prestaciones de servicios#1

Current: Tienda Norte vendió en 2026 a distancia bienes por 9.000 euros, excluido el impuesto, por debajo del límite de 10.000 euros del año natural precedente (art. 73.Uno LIVA). El martes 14 de septiembre de 2027 las operaciones del año en curso superan ese límite: se aplica lo establecido en el artículo 68.Tres.a) (art. 73.Uno LIVA).

Blind verifier: PASS — 9.000 < 10.000 en el año precedente; el 14-9-2027 es martes; cuando se supera el límite en el año en curso se aplica el art. 68.Tres.a) (art. 73.Uno).
Student reader: REWRITE — It says "se aplica el artículo 68.Tres.a)" without saying what that means; state where the sales are taxed once the limit is exceeded.

