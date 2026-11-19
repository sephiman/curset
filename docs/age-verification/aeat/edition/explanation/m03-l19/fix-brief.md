# Fix brief — `m03-l19`

## caso:### Adquisiciones intracomunitarias e importaciones#1

Current: Electro Sur, S.L. adquiere mercancías en Francia y paga un anticipo el lunes 1 de marzo de 2027. Las entregas de bienes similares se considerarían efectuadas el lunes 15 de marzo de 2027, y entonces se devenga el impuesto (art. 76 LIVA). El anticipo no adelanta el devengo, porque no se aplica el apartado Dos del artículo 75, relativo a los pagos anticipados (art. 76 LIVA).

Blind verifier: PASS — El 1-3-2027 y el 15-3-2027 son lunes; el devengo se produce cuando se consideren efectuadas las entregas similares y en las adquisiciones intracomunitarias no se aplica el art. 75.Dos (art. 76).
Student reader: REWRITE — "Las entregas de bienes similares se considerarían efectuadas el 15 de marzo" is unexplained; say the accrual is the 15th of the following month (or the invoice date, if earlier) and why the 1 March advance changes nothing.

## caso:### Reglas especiales#1

Current: Talleres Mora entrega un coche a Ana y recibe a cambio una máquina. Las partes acordaron expresar el valor en 6.000 euros: esa es la base imponible (art. 79.Uno LIVA). Otra operación se fija en 5.000 dólares y se devenga el lunes 5 de abril de 2027: se aplica el tipo de cambio vendedor fijado por el Banco de España vigente en el momento del devengo (art. 79.Once LIVA).

Blind verifier: FAIL — «Las partes acordaron expresar el valor en 6.000 euros: esa es la base imponible» omite el segundo párrafo del mismo art. 79.Uno: «Salvo que se acredite lo contrario, la base imponible coincidirá con los importes que resulten de aplicar las reglas previstas en los apartados tres y cuatro». El lector queda con la idea de que el importe pactado es definitivo. La rama del tipo de cambio es correcta: el 5-4-2027 es lunes (art. 79.Once).
Student reader: KEEP — Agreed value for a barter and the exchange rate at accrual are both applied.

## caso:### Modificación de la base imponible#1

Current: Papelería Luz repercute el martes 10 de febrero de 2026 una cuota sobre una base de 4.000 euros a Comercial Ruiz, empresario, y no cobra. Con un volumen de operaciones superior a 6.010.121,04 euros el año anterior, el crédito es incobrable al transcurrir un año desde el devengo, el jueves 11 de febrero de 2027 (art. 80.Cuatro LIVA). Además deben constar los Libros Registros y haberse instado el cobro por requerimiento notarial (art. 80.Cuatro LIVA).

Blind verifier: FAIL — «haberse instado el cobro por requerimiento notarial» presenta una sola vía como el requisito, cuando la condición 4.ª del art. 80.Cuatro.A admite la reclamación judicial, el requerimiento notarial o cualquier otro medio fehaciente. Además, el caso omite que la modificación debe hacerse en los seis meses siguientes al fin del plazo (art. 80.Cuatro.B). Las fechas y el plazo de un año son correctos: el 10-2-2026 es martes y el 11-2-2027, jueves; el volumen supera 6.010.121,04 €.
Student reader: REWRITE — It stops at the requirements and never says what Papelería Luz does (reduce the base 4.000 to 0 within the deadline, issue a rectifying invoice); add the outcome.

## caso:## Sujetos pasivos#1

Current: Inmuebles Zeta, S.L., en proceso concursal, entrega en 2027 un local a Comercial Tajo, S.A., empresario. Sujeto pasivo es el empresario para quien se realiza la operación, Comercial Tajo (art. 84.Uno.2.º.e LIVA). Una comunidad de bienes sin personalidad jurídica que realiza operaciones sujetas, por constituir una unidad económica, también es sujeto pasivo (art. 84.Tres LIVA).

Blind verifier: FAIL — El art. 84.Uno.2.º.e exige que la entrega se efectúe «como consecuencia de un proceso concursal», y el caso solo dice que la vendedora está «en proceso concursal»; tampoco dice que la entrega esté sujeta y no exenta. El lector puede concluir que cualquier entrega de un inmueble por una sociedad en concurso invierte el sujeto pasivo. La comunidad de bienes como sujeto pasivo (art. 84.Tres) es correcta.
Student reader: KEEP — Reverse-charge case on a bankruptcy sale plus the comunidad de bienes are easy to follow.

## caso:### Rectificación de las cuotas repercutidas#1

Current: Mueblería Pino calculó mal una cuota devengada el miércoles 20 de mayo de 2026 y lo advierte el viernes 12 de noviembre de 2027. No han transcurrido cuatro años desde el devengo, así que debe rectificarla al advertirlo (art. 89.Uno LIVA). Si la rectificación aumenta la cuota y no hubo requerimiento previo, presenta una declaración-liquidación rectificativa con el recargo y los intereses de demora que procedan (art. 89.Cinco LIVA).

Blind verifier: FAIL — El 20-5-2026 es miércoles y el 12-11-2027, viernes, dentro de los cuatro años. Pero «debe rectificarla al advertirlo» y la rama de aumento con declaración rectificativa omiten el art. 89.Tres.1.º: la rectificación al alza que no se deba al art. 80 no procede cuando el destinatario no actúa como empresario o profesional. El caso no dice quién es el destinatario; además, el art. 89.Cinco permite incluir la diferencia en el período corriente si hay error fundado de derecho.
Student reader: KEEP — The four-year window and the surcharge on an increase are both applied.

## caso:### Ejercicio del derecho a deducir#1

Current: Mueblería Pino recibe la factura el lunes 3 de mayo de 2027, y entonces se entienden soportadas las cuotas (art. 99.Cuatro LIVA). Puede deducirlas en la declaración-liquidación de ese período o en las siguientes, antes de que pasen cuatro años desde el nacimiento del derecho (art. 99.Tres LIVA). Si sus deducciones superan las cuotas devengadas, puede compensar el exceso en declaraciones posteriores u optar por la devolución cuando proceda (art. 99.Cinco LIVA).

Blind verifier: FAIL — El 3-5-2027 es lunes y los apartados Cuatro y Tres están bien aplicados, pero «puede compensar el exceso en declaraciones posteriores» omite el límite del art. 99.Cinco: «siempre que no hubiesen transcurrido cuatro años contados a partir de la presentación de la declaración-liquidación en que se origine dicho exceso». El lector entiende que la compensación no tiene límite temporal.
Student reader: KEEP — When quotas are borne, the four-year window and the carry-forward/refund option are in order.

## caso:## Régimen de deducciones en sectores diferenciados#1

Current: Comercial Lago tiene una actividad principal, con mayor volumen de operaciones el año anterior, y otra con un grupo distinto en la CNAE. El porcentaje de deducción de la segunda sería 40 y el de la principal 100: difieren en más de 50 puntos, así que los regímenes son distintos (art. 9.1.º.c LIVA). Son sectores diferenciados y aplica separadamente las deducciones a cada uno (art. 101.Uno LIVA).

Blind verifier: FAIL — De «otra con un grupo distinto en la CNAE» el caso salta a que son actividades distintas sin la regla del mismo art. 9.1.º.c).a'): «no se reputará distinta la actividad accesoria a otra cuando, en el año precedente, su volumen de operaciones no excediera del 15 por 100 … y contribuya a su realización». El cálculo de los 60 puntos de diferencia (> 50) y la aplicación separada (art. 101.Uno) son correctos.
Student reader: KEEP — The 40 against 100 percentage gap above 50 points makes the test visible.

