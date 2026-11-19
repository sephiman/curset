# Fix brief — `m01-l05`

## overview (draft.md, the OVERVIEW block) — FAIL

«el sigilo como infracción grave (art. 29.2.d Ley 19/2013)» drops the article's condition: what is grave is «no guardar el debido sigilo [...] cuando causen perjuicio a la Administración o se utilice en provecho propio» (and it is the breach of sigilo, not the sigilo, that is the infraction). Also «la solicitud de acceso no se motiva» turns art. 17.3 («no está obligado a motivar [...] Sin embargo, podrá exponer los motivos») into a bar; the rest (38.4, 14.2, 24.2) is supported.

## caso:### Tramitación#1

Current: Julia solicita acceso a información y su solicitud no la identifica de forma suficiente. Se le pide que la concrete en un plazo de diez días; si no lo hace, se le tiene por desistida, y mientras tanto el plazo para resolver queda suspendido (art. 19.2 Ley 19/2013). En otra solicitud la información puede afectar a terceros debidamente identificados: se les concede un plazo de quince días para alegaciones, con suspensión del plazo para resolver (art. 19.3 Ley 19/2013).

Blind verifier: PASS — 10 days to specify, desistimiento and suspension (19.2); 15 days for identified third parties with suspension (19.3). Incomplete (end of suspension, informing the applicant) but nothing false.
Student reader: REWRITE — Two unrelated requests in one paragraph with no dates or outcome; split them and say what happens to the deadline to resolve.

## caso:### Reclamación ante el Consejo de Transparencia y Buen Gobierno#1

Current: El lunes 8 de febrero de 2027 se notifica a Nuria la resolución que le deniega el acceso. La reclamación ante el Consejo de Transparencia y Buen Gobierno procede frente a toda resolución expresa o presunta (art. 24.1 Ley 19/2013). Se interpone en un mes desde el día siguiente al de la notificación; vence el lunes 8 de marzo de 2027 (art. 24.2 Ley 19/2013; art. 30.4 LPAC). El Consejo resuelve y notifica en tres meses (art. 24.4 Ley 19/2013).

Blind verifier: FAIL — Dates correct (08-02-2027 Monday → 08-03-2027 Monday). But «La reclamación [...] procede frente a toda resolución» replaces art. 24.1's «podrá interponerse [...] con carácter potestativo y previo a su impugnación en vía contencioso-administrativa», dropping the modal and the potestativo character; and «El Consejo resuelve y notifica en tres meses» drops «plazo máximo» and the consequence «transcurrido el cual, la reclamación se entenderá desestimada» (24.4).
Student reader: KEEP — The one-month deadline from the day after notification (8 Feb to 8 Mar) is clear and correct.

## caso:### Ejercicio de los derechos#1

Current: Tomás ejerce el lunes 8 de febrero de 2027 su derecho de acceso ante un responsable. Este le informa de sus actuaciones sin dilación indebida y, en cualquier caso, en un mes desde la recepción, hasta el lunes 8 de marzo de 2027 (art. 12.3 RGPD). El plazo podrá prorrogarse otros dos meses en caso necesario, por la complejidad y el número de solicitudes; la prórroga se comunica en ese primer mes, con los motivos (art. 12.3 RGPD).

Blind verifier: FAIL — Dates correct (08-02-2027 Monday → 08-03-2027 Monday), but «sin dilación indebida» is not in the cited Spanish text of art. 12.3 RGPD, which reads «[...] artículos 15 a 22, y, en cualquier caso, en el plazo de un mes a partir de la recepción de la solicitud» (the phrase appears in 12.4, for non-action).
Student reader: KEEP — The one-month term (8 Feb to 8 Mar) and the extension with reasons are clear.

## caso:### Acceso#1

Current: Rosa ejerce el derecho de acceso ante el mismo responsable el lunes 11 de enero de 2027 y otra vez el lunes 22 de marzo de 2027. Entre las dos fechas pasan menos de seis meses. Se podrá considerar repetitivo el ejercicio del derecho de acceso en más de una ocasión durante el plazo de seis meses (art. 13.3 LOPDGDD). La segunda solicitud podrá considerarse repetitiva, a menos que Rosa tenga una causa legítima (art. 13.3 LOPDGDD).

Blind verifier: FAIL — Dates correct (11-01-2027 and 22-03-2027 are Mondays, under six months), but the case omits the source the article names: art. 13.3 LOPDGDD allows treating the request as repetitive «a los efectos establecidos en el artículo 12.5 del Reglamento (UE) 2016/679»; without it the reader does not know what «repetitiva» triggers (canon or refusal under RGPD 12.5).
Student reader: KEEP — Two requests under six months apart show the repetitive-request rule and its legitimate-cause exception.

