# Fix brief — `m01-l01`

## overview (draft.md, the OVERVIEW block) — FAIL

«La parte más extensa es el Tribunal Constitucional: composición, Pleno y Salas, recursos y sentencias (arts. 159 a 165 CE)»: los arts. 159–165 CE no regulan Pleno y Salas (la CE solo menciona el «Tribunal en pleno» para proponer al Presidente, art. 160; las Salas no aparecen y el art. 165 remite el funcionamiento a una ley orgánica, la LOTC), así que la cita atribuye a la CE una materia que está en la LOTC. Menor: «los principios y valores superiores del título preliminar (art. 1.1 CE)» — el art. 1.1 solo enuncia los valores superiores; el resto de afirmaciones (arts. 53, 55, 56, 57, 59, 60, 62, 167, 168) concuerda con su artículo.

## caso:### Composición#1

Current: El Gobierno propone a Irene, abogada con dieciséis años de ejercicio profesional y jurista de reconocida competencia, para una de las dos plazas que le corresponden (art. 159.1 CE). Cumple el requisito de más de quince años (art. 159.2 CE) y el Rey la nombra (art. 159.1 CE). Su mandato dura nueve años (art. 159.3 CE). Mientras sea miembro, no puede ejercer ninguna actividad profesional (art. 159.4 CE).

Blind verifier: PASS — Dos a propuesta del Gobierno y nombramiento por el Rey (art. 159.1); abogada, jurista de reconocida competencia, 16 > 15 años (art. 159.2); nueve años (art. 159.3); incompatible con cualquier actividad profesional (art. 159.4).
Student reader: REWRITE — It only restates the rules on Irene; add a candidate who fails (exactly fifteen years) so the "más de quince" boundary is applied, and drop the closing sentence on incompatibility.

## caso:### Presidente y Vicepresidente#1

Current: El Pleno del Tribunal elige a Elena, Magistrada, por votación secreta, y en la primera votación obtiene la mayoría absoluta (art. 9.1–2 LOTC). El Rey la nombra Presidenta entre los miembros del Tribunal, a propuesta del Pleno, por tres años (art. 160 CE). Al terminar ese período puede ser reelegida una sola vez (art. 9.3 LOTC).

Blind verifier: PASS — Elección por el Pleno en votación secreta y mayoría absoluta en primera votación (art. 9.1–2 LOTC, leído del PDF); nombramiento por el Rey entre sus miembros a propuesta del Pleno por tres años (art. 160 CE); reelección por una sola vez (art. 9.3 LOTC).
Student reader: REWRITE — It covers only the easy path (absolute majority first round); the hard part is the second vote, tie and seniority/age tie-breaks, which the case never uses.

## caso:### Recurso de amparo#1

Current: La Administración vulnera un derecho del artículo 14 de Tomás, que agota la vía judicial. Le notifican la resolución judicial el lunes 9 de noviembre de 2026. El plazo para el amparo es de veinte días desde la notificación (art. 43.2 LOTC). Tomás presenta la demanda el viernes 20 de noviembre, a los once días, y justifica la especial trascendencia constitucional del recurso (art. 49.1 LOTC).

Blind verifier: FAIL — «Tomás presenta la demanda el viernes 20 de noviembre, a los once días»: 11 son días naturales, pero el plazo de veinte días del art. 43.2 LOTC se computa en días hábiles (art. 80 LOTC → art. 185.1 LOPJ excluye los inhábiles; art. 182.1: sábados y domingos inhábiles), así que el 20-11-2026 es el 9.º día hábil (10–13 y 16–20 de noviembre). El resultado (en plazo) es correcto, pero el recuento deja la idea errónea de que el plazo corre en días naturales. Resto correcto: violación por la Administración y vía judicial agotada (art. 43.1), especial trascendencia (art. 49.1).
Student reader: KEEP — Notification date, filing on day eleven and the 20-day rule show how to pick the right deadline for an administrative violation.

