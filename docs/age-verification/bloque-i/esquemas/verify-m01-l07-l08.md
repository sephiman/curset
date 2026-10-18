# Verification — esquemas of m01-l07 and m01-l08 (2026-10-18)

I am a blind reviewer. I wrote neither these esquemas nor the lessons, and I did not read the writer's notes.
Scope: the `:::esquema` blocks that `git diff C/es/lessons/m01-l07.md C/es/lessons/m01-l08.md` shows as added.
Rules: `spec.md` (this folder), the `::esquema` section of `docs/platform-delta-handoff.md`, `docs/prose-voice.md`;
format from `../../bloque-v/esquemas/verify-m05-l03.md`.

- Diff: `git diff --numstat` gives 13 added / 0 deleted lines for m01-l07 and 17 / 0 for m01-l08. Only esquema
  blocks and their blank separator lines are added; no prose line changed.
- m01-l06: `git diff` and `git status --short` are empty for `C/es/lessons/m01-l06.md`. No diff.
- Sources: scratchpad `txt/BOE-A-2013-12887_ley-transparencia_2022-07-09.txt` (arts. 19, 20, 23, 24) and
  `txt/BOE-A-2015-10566_lrjsp_2024-08-02.txt` (arts. 55, 69, 70, 72), read with `art.py`. No norm wording taken from
  memory.
- Platform: I ran `CourseCitations.build(...).problems([], "es")` from the backend on both lessons (no problems) and
  printed `parse_segment` for each row citation (see plazos row 2).
- Glossary: no glossary term has its first occurrence inside an esquema in either lesson (checked by regex over
  `glossary.yaml`: silencio administrativo, órganos superiores, órganos directivos, servicios comunes, Delegado del
  Gobierno, Subdelegado del Gobierno and provincia all first appear in prose above the esquema). No mark moves.

Line numbers are those of the current files.

## m01-l07 — tabla «Los dos plazos del artículo 19 que suspenden el plazo para resolver» (l. 167–172)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Solicitud que no identifica de forma suficiente la información — diez días para concretarla — desistido; plazo para resolver suspendido | art. 19.2 Ley 19/2013 | PASS | 19.2: «Cuando la solicitud no identifique de forma suficiente la información, se pedirá al solicitante que la concrete en un plazo de diez días, con indicación de que, en caso de no hacerlo, se le tendrá por desistido, así como de la suspensión del plazo para dictar resolución.» A faithful shortening, word for word the prose at l. 159–161. | — |
| 2 | Información que puede afectar a terceros debidamente identificados — quince días para alegaciones — suspensión del plazo para resolver | art. 19.3 Ley 19/2013 | PASS | 19.3: «…se les concederá un plazo de quince días para que puedan realizar las alegaciones que estimen oportunas. El solicitante deberá ser informado de esta circunstancia, así como de la suspensión del plazo para dictar resolución hasta que se hayan recibido las alegaciones o haya transcurrido el plazo para su presentación.» Faithful shortening, same as the prose at l. 163–165. The end of the suspension («hasta que…») is missing from row and prose alike; see Notes. | — |

Title: art. 19 has exactly two plazos (19.2 and 19.3); 19.1 and 19.4 carry none. «Los dos plazos» is complete. PASS.

## m01-l07 — plazos «Plazos de la resolución de acceso y de la reclamación ante el Consejo de Transparencia y Buen Gobierno» (l. 223–227)

| # | step (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Resolución de la solicitud, notificada al solicitante y terceros que lo pidieron — un mes desde la recepción por el órgano competente, ampliable otro mes (volumen o complejidad, previa notificación); silencio desestimatorio | arts. 20.1 y 20.4 Ley 19/2013 | PASS | 20.1: «…deberá notificarse al solicitante y a los terceros afectados que así lo hayan solicitado en el plazo máximo de un mes desde la recepción de la solicitud por el órgano competente para resolver. Este plazo podrá ampliarse por otro mes en el caso de que el volumen o la complejidad de la información que se solicita así lo hagan necesario y previa notificación al solicitante.» 20.4: «Transcurrido el plazo máximo para resolver sin que se haya dictado y notificado resolución expresa se entenderá que la solicitud ha sido desestimada.» Keeps both conditions of the extension. In prose at l. 176–179 and l. 185–186. | — |
| 2 | Reclamación ante el CTBG, potestativa y previa a la vía contencioso-administrativa, salvo contra los órganos del art. 2.1.f) — un mes desde el día siguiente a la notificación o a los efectos del silencio | arts. 23.2 y 24.1–2 Ley 19/2013 | FAIL | Text PASS: 23.2: «…contra las resoluciones dictadas por los órganos previstos en el artículo 2.1.f) sólo cabrá la interposición de recurso contencioso-administrativo.» 24.1: «…con carácter potestativo y previo a su impugnación en vía contencioso-administrativa.» 24.2: «…en el plazo de un mes a contar desde el día siguiente al de la notificación del acto impugnado o desde el día siguiente a aquel en que se produzcan los efectos del silencio administrativo.» Faithful, keeps the 23.2 exception; in prose at l. 202–210. Citation FAIL: `parse_segment("arts. 23.2 y 24.1–2 Ley 19/2013")` returns units art. 23, art. 24 **and art. 2**, with range `(24, 2)`: «24.1–2» is read as an article range 24 → 2, not as apartados 1–2 of art. 24. The load passes only because the prose cites art. 2.1 at l. 21. (Contrast `art. 90.2–3 CE` in m01-l03, which parses as art. 90 alone: the en-dash range after a second article in an «arts. … y …» list is the trigger.) | Same row, citation `(arts. 23.2, 24.1 y 24.2 Ley 19/2013)` — parses as art. 23 and art. 24 only. |
| 3 | Resolución y notificación de la reclamación — tres meses; silencio desestimatorio | art. 24.4 Ley 19/2013 | PASS | 24.4: «El plazo máximo para resolver y notificar la resolución será de tres meses, transcurrido el cual, la reclamación se entenderá desestimada.» Verbatim shortening, same as the prose at l. 213–214. | — |

Order: 1 → 2 is supported by 24.1 («Frente a toda resolución expresa o presunta») and 24.2, whose plazo runs from the
notification of the act or the effects of the silence that step 1 describes. Step 2's label carries «potestativa» and
the 23.2 exception, so the timeline does not claim that a reclamación always follows. 2 → 3: 24.4 is the plazo to
resolve the reclamación interposed under 24.1–2. No false order. PASS.

## m01-l08 — arbol «Órganos superiores y directivos de la Administración General del Estado» (l. 51–60)

| # | node (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Administración General del Estado (root) | art. 55.2 LRJSP | PASS | 55.2: «La Administración General del Estado comprende:». Prose l. 32. | — |
| 2 | Organización Central — integra los Ministerios y los servicios comunes | art. 55.2 LRJSP | PASS | 55.2.a): «La Organización Central, que integra los Ministerios y los servicios comunes.» Verbatim; child of the root per «comprende». Prose l. 34. Citation without the letter, as list rows require. | — |
| 3 | Órganos superiores — Ministros y Secretarios de Estado (under Organización Central) | art. 55.3 LRJSP | PASS | 55.3: «En la organización central son órganos superiores y órganos directivos: a) Órganos superiores: 1.º Los Ministros. 2.º Los Secretarios de Estado.» The text places them in the organización central. Prose l. 40–42. | — |
| 4 | Órganos directivos — Subsecretarios y Secretarios generales; SGT y Directores generales; Subdirectores generales (under Organización Central) | art. 55.3 LRJSP | PASS | 55.3.b): «1.º Los Subsecretarios y Secretarios generales. 2.º Los Secretarios generales técnicos y Directores generales. 3.º Los Subdirectores generales.» Complete and verbatim. Prose l. 43–44. The tree does not put the directivos under the superiores, which 55.3 does not say. | — |
| 5 | Organización Territorial | art. 55.2 LRJSP | PASS | 55.2.b): «La Organización Territorial.» Prose l. 35. | — |
| 6 | Órganos directivos — Delegados, rango de Subsecretario; Subdelegados en las provincias, nivel de Subdirector general (under Territorial) | art. 55.4 LRJSP | PASS | 55.4: «En la organización territorial de la Administración General del Estado son órganos directivos tanto los Delegados del Gobierno en las Comunidades Autónomas, que tendrán rango de Subsecretario, como los Subdelegados del Gobierno en las provincias, los cuales tendrán nivel de Subdirector general.» Faithful; placement stated by «En la organización territorial». Prose l. 46–48. | — |
| 7 | Administración General del Estado en el exterior | art. 55.2 LRJSP | PASS | 55.2.c): «La Administración General del Estado en el exterior.» Prose l. 36. | — |
| 8 | Órganos directivos — embajadores y representantes permanentes ante Organizaciones internacionales (under exterior) | art. 55.5 LRJSP | PASS | 55.5: «En la Administración General del Estado en el exterior son órganos directivos los embajadores y representantes permanentes ante Organizaciones internacionales.» Verbatim. Prose l. 48–49. | — |

Nesting: the three branches are the three letters of 55.2, in order; each organ class sits under the organización
that 55.3, 55.4 and 55.5 name. Title: 55.3–55.5 list every órgano superior and directivo of the three
organizaciones; the title does not overclaim (55.8 leaves the Organismos públicos' directivos to their statutes, which
are outside the AGE as the title names it). PASS.

## m01-l08 — arbol «El Delegado del Gobierno, los Subdelegados y los Directores Insulares» (l. 301–305)

| # | node (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Delegado del Gobierno en la CA — órgano directivo, rango de Subsecretario; depende orgánicamente del Presidente y funcionalmente del Ministerio competente (root) | art. 72.3 LRJSP | PASS | 72.3: «Los Delegados del Gobierno son órganos directivos con rango de Subsecretario que dependen orgánicamente del Presidente del Gobierno y funcionalmente del Ministerio competente por razón de la materia.» Verbatim. Prose l. 259–261. | — |
| 2 | Subdelegado en cada provincia de las CCAA pluriprovinciales — bajo la inmediata dependencia del Delegado (child of Delegado) | art. 69.4 LRJSP | PASS | 69.4: «En cada una de las provincias de las Comunidades Autónomas pluriprovinciales, existirá un Subdelegado del Gobierno, que estará bajo la inmediata dependencia del Delegado del Gobierno.» Verbatim; the dependency is stated. Prose l. 247–248. | — |
| 3 | Director Insular, en las islas que determine un reglamento — lo nombra el Delegado; depende del Delegado o del Subdelegado de la provincia, si existe (child of Delegado, sibling of Subdelegado) | art. 70 LRJSP | FAIL | Text PASS: 70: «Reglamentariamente se determinarán las islas en las que existirá un Director Insular … Serán nombrados por el Delegado del Gobierno … Los Directores Insulares dependen jerárquicamente del Delegado del Gobierno en la Comunidad Autónoma o del Subdelegado del Gobierno en la provincia, cuando este cargo exista…». Prose l. 296–299. Dependency FAIL: art. 70 makes the Director Insular depend on the Delegado only where the province has no Subdelegado; where one exists (both Canary provinces, under node 2's «pluriprovinciales»), he depends on the Subdelegado. The tree draws him directly under the Delegado and level with the Subdelegado in every case. The node's own text says otherwise, so tree and text contradict each other; the position claims a dependency the article gives only in one case. | Drop node 3 and retitle `title="El Delegado del Gobierno y los Subdelegados"`; the Director Insular stays in the prose at l. 296–299. (Alternative, if the writer prefers to keep it: split the node in two, one under the Subdelegado «— lo nombra el Delegado del Gobierno; depende del Subdelegado de la provincia, si existe (art. 70 LRJSP)» and one under the Delegado for the province without Subdelegado. That second label needs «si no existe», a negation that is neither in art. 70's nor the prose's words, so I do not recommend it.) |

## Placement

- m01-l07 tabla (l. 167): right after the two paragraphs it summarises (l. 159–165), before «### Resolución». PASS.
- m01-l07 plazos (l. 223): after every paragraph it summarises (Resolución l. 176–189, Reclamación l. 199–221), at
  the end of the Reclamación section, before «## Título II». It does not replace the bullet list at l. 206–216: that
  list also covers 24.3 and 24.5, which the timeline leaves out. PASS.
- m01-l08 arbol 1 (l. 51): after «Las tres organizaciones» and «Órganos superiores y órganos directivos» (l. 28–49),
  before the 55.6 paragraph. The prose has two short lists (l. 34–36, l. 42–44); the tree joins them with 55.4–55.5,
  which the lists do not carry, so it is not a duplicate. PASS.
- m01-l08 arbol 2 (l. 301): after the Subdelegados (l. 247–248), Delegados (l. 259–261) and Directores Insulares
  (l. 296–299) paragraphs it summarises, before «### Servicios territoriales». PASS.

## Notes

- l07 tabla row 2 and prose l. 163–165: art. 19.3 bounds the suspension («hasta que se hayan recibido las alegaciones
  o haya transcurrido el plazo para su presentación»). Neither row nor prose says when the suspension ends. I did not
  fail the row, since it states no end that the article contradicts, but the writer may list it in the ledger as a
  prose gap; if it is added to the prose, the row's «Efecto» cell can take it verbatim.
- l07 plazos row 2: the CTBG is the competent body only outside the DA 4.ª / art. 24.6 case (CCAA organ). The title
  names the Consejo and the prose states the exception just above (l. 218–221), so the row does not read wider.
- l08 arbol 2 node 2: 69.4 párr. 2 (Subdelegaciones by Real Decreto in uniprovincial CCAA) is outside the node, which
  narrows to the pluriprovincial case. Narrower, not wider.
- Voice: titles and labels carry no filler, triad or closer. Nothing from the «never does» list.

## Totals

16 rows: 14 PASS, 2 FAIL.

- m01-l07 tabla: 2/2 PASS.
- m01-l07 plazos: 2 PASS, 1 FAIL (row 2, citation «24.1–2» parses as arts. 24 → 2).
- m01-l08 arbol 1: 8/8 PASS.
- m01-l08 arbol 2: 2 PASS, 1 FAIL (node 3, Director Insular drawn under the Delegado although art. 70 places him under
  the Subdelegado where one exists).
- m01-l06: no diff.
