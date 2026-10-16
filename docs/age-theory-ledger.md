# Theory ledger — age-administrativo-c1

Round R2, bloque I (temas I.1–I.11), 2026-10-16. Nothing committed. Prompt: write each tema's lesson, Normativa and
«Lo que más cae» blocks, course.yaml summary and glossary entries, then verify every fact-bearing sentence against the
consolidated text in `sources/normativa/`.

## How this round ran

- One writer per tema drafted the lesson from the norm texts (`pdftotext` of `sources/normativa/*.pdf`), to a shared
  spec: structure follows the governing norm, every plazo, mayoría, órgano, número, excepción and fecha is copied from
  the article and cited inline «(art. N norma)», cambio-pendiente norms in their forthcoming wording with
  «(desde DD-MM-AAAA)». Word cap 4,000 (`wc -w`, everything counted).
- A separate reviewer that had not written the lesson re-opened the cited article for every sentence carrying a
  number, plazo, majority, organ, date or exception, and checked every citation. It wrote PASS/FAIL per sentence and a
  replacement for each FAIL. The writer fixed every FAIL against the article before the tema was closed. The
  per-sentence tables are working files, not kept in the repo; their counts and every FAIL are below.
- Facts that rest on no text in `sources/normativa/` are listed per tema under the writer's notes, with the outside
  source used. Ambiguous or inconsistent consolidated texts are listed, not resolved.
- The per-tema «Writer's notes» were written before the five decisions of the section «Decisions applied after
  bloque I». Where a note says otherwise (a dated art. 23 marker, no EU head-counts, the LBRL file), that section rules.

## Summary

| Tema | Lesson | Words | Citations | Sentences checked | FAIL (fixed) | Unverifiable | Glossary entries |
|---|---|---|---|---|---|---|---|
| I.1 | `m01-l01` | 3,991 | 133 | 155 | 2 | 0 | 8 |
| I.2 | `m01-l02` | 2,489 | 71 | 100 | 5 | 0 | 5 |
| I.3 | `m01-l03` | 3,609 | 97 | 134 | 1 | 1 | 13 |
| I.4 | `m01-l04` | 3,173 | 118 | 133 | 3 | 0 | 7 |
| I.5 | `m01-l05` | 3,300 | 92 | 129 | 1 | 0 | 7 |
| I.6 | `m01-l06` | 2,177 | 12 | 99 | 6 | 0 | 2 |
| I.7 | `m01-l07` | 3,651 | 94 | 107 | 3 | 0 | 5 |
| I.8 | `m01-l08` | 3,577 | 113 | 128 | 5 | 0 | 10 |
| I.9 | `m01-l09` | 3,692 | 70 | 82 | 5 | 0 | 5 |
| I.10 | `m01-l10` | 2,979 | 73 | 101 | 1 | 0 | 11 |
| I.11 | `m01-l11` | 3,902 | 115 | 134 | 3 | 0 | 7 |
| **Total** | | | | **1,302** | **35** | **1** | **79** |

«Competencia exclusiva» counts in I.9 and I.11 (one entry, two senses), so the column sums to 80.

The one unverifiable item was the «(desde 23-12-2026)» date on Reglamento del Congreso art. 23 (I.3): the reform says
«en la XVI legislatura». After decision 5 below the marker reads «(desde la XVI legislatura)», which the reform states;
it passed in the second verification pass.

## Glossary

- `glossary.yaml` now holds 79 entries, all with origin in bloque I. The writers proposed 93 candidates. Duplicates
  were merged, with one origin each: ley orgánica (I.1), Diputación Permanente (I.3), estado de sitio (I.5, the first
  lesson that uses the singular), publicidad activa (I.7), alto cargo and Delegado del Gobierno (I.8). «Competencia
  exclusiva» is one entry with two senses: the Estado's under art. 149.1 CE (I.9) and the Union's under art. 2.1 TFUE
  (I.11).
- Every kept entry either appears in two or more bloque I lessons or cites the article that defines it.
- **Waiting** (one lesson only and no defining article in the sources): mayoría absoluta (used in seven lessons, but no
  article in the sources defines it), Gobierno Abierto, Objetivos de Desarrollo Sostenible, libre designación (defined
  in the TREBEP/RD 364/1995, so it can enter with IV.5), recurso por incumplimiento, recurso de anulación.
- **False friends** (`link_except`): inviolabilidad (I.1 domicilio, I.2 the Rey), mandato imperativo (I.1, the Defensor
  del Pueblo), refrendo (I.7, the Congress endorsing the CTBG President), Agenda 2030 (I.8, a ministry name), servicios
  comunes (I.7, Seguridad Social), moción de censura (I.10 Alcalde, I.11 Comisión), cuestión de confianza (I.10),
  competencia exclusiva (I.6, a website sentence about Gobierno Abierto).
- **Glossary verification:** the definitions got their own blind pass against the cited articles: 79 checked, 64
  PASS, 15 FAIL, all replaced with the reviewer's article-faithful wording: refrendo, regencia, mandato imperativo,
  suplicatorio, Tribunal de Instancia, consulta pública, publicidad activa, autoridad administrativa independiente,
  silencio administrativo, alto cargo, órganos directivos, servicios comunes, Subdelegado del Gobierno, competencia
  exclusiva (sense I.9) and municipios de gran población.
- `glossary-links.es.txt` regenerated and read line by line: 50 web marks, the false friends above removed.
  `lesson-refs.es.txt`: 4 references, 0 dangling.

## Cross-cutting points for the reviewer

- **Stale organ names inside consolidated laws.** The LRJSP, Ley 2/2014, Ley 19/2013 and Ley 50/1997 still name
  departments that no longer exist. Decision 1 below applies: the lessons quote the law and add «(hoy: …)» once.
- **RD 806/2026 dissolved the Cortes.** A government formed after the 29-11-2026 elections may restructure ministries
  before the exam. I.8's list is dated (decision 2); see «Open items».
- **EU texts are 2016 versions** (DOUE C 202) and still count the United Kingdom. I.11 now gives today's head-counts
  «a fecha de 16-10-2026» from saved official pages (decision 3).
- **Outside sources are saved, not fetched.** Every non-legal page or document a lesson cites is a dated copy in
  `content/age-administrativo-c1/sources/otros/`, indexed in `fuentes.yaml` (URL, date consulted, sha256, citing
  lessons). The 2026 CE reform (BOE-A-2026-10881) that I.3 cites for Formentera is now in `sources/normativa/`.
- **V Plan page title.** The saved Portal page «Diseño del V Plan de Gobierno Abierto» says «2024-2028» in its HTML
  `<title>`, while its heading, its text and the V Plan PDF say 2025-2029 (vigencia 6-10-2025 to 6-10-2029). The lesson
  follows the heading and the PDF.
- **Future-merged consolidated files (decision 4).** Checked file by file: only RD 366/2007 and the Reglamento del
  Congreso print the new wording with a «Téngase en cuenta… entra en vigor» notice and the «Redacción anterior». The
  ten files amended by Ley 4/2026 or RD 813/2026 (the LBRL among them) carry the new wording only, with no notice and
  no previous wording. The R1 handoff note and the ten `version_vigente` notes in `normativa.yaml` are corrected.

## Decisions applied after bloque I (standing conventions from now on)

1. **Old ministry names.** Quote the law as written; after the first such mention in a lesson add «(hoy: <current
   name>)», as the exam ledger does. Applied: I.5 (Ministro de la Presidencia), I.7 (Ministro de Hacienda y
   Administraciones Públicas), I.8 (Ministerio de Hacienda y Administraciones Públicas, at art. 54.2 LRJSP; Ministerio
   de Asuntos Exteriores y de Cooperación). The «hoy» name is the department whose RD 829/2023 competences cover the
   function the law gives in that sentence.
2. **I.8 ministry list** stays, headed «Estructura vigente a 16-10-2026 (RD 829/2023, de 20 de noviembre).»
3. **Head-counts and other non-legal facts** come from official pages saved as files under `sources/otros/`, stated «a
   fecha de» the consultation and cited by file. Applied: I.11 (27 Estados miembros, 720 diputados, 27 comisarios, 27
   jueces y 11 abogados generales, 54 jueces del Tribunal General), I.6 (every UN, OECD and Portal de la Transparencia
   citation), I.1 (the four CE reforms, from the saved BOE analysis). The OECD Recommendation has no official Spanish
   text: the lesson cites the official English PDF and the Portal's Spanish wording.
4. **LBRL note** checked against the file and corrected (see above).
5. **Reglamento del Congreso art. 23**: «(desde la XVI legislatura)» instead of a date (I.3).

**Second verification pass** (the sentences these decisions changed): 50 checked, 46 PASS, 4 FAIL, all fixed:
- I.8: the «hoy» note covered «varios artículos» of the título, but the Delegaciones del Gobierno (art. 69.3 LRJSP) fall
  under Política Territorial (art. 12.1 RD 829/2023). The note now sits on art. 54.2 LRJSP only, quoted.
- I.6: the V Plan passage on the OGP copresidency is in its «prólogo», not a «presentación».
- I.11: «el número de miembros no está en los tratados» was wrong (art. 19.2 TUE, art. 252 TFUE). Removed.
- I.11: `ue-paises.html` does not state 27 in its text; the 27 Estados now cite `ue-consejo.html` («15 países de los 27
  miembros actuales»).
- I.3, outside this pass: the Formentera sentence said «convocadas»; it now quotes the transitional provision («la
  convocatoria de las primeras elecciones al Senado que se celebren tras la entrada en vigor»).

## I.1 — `m01-l01`

La Constitución Española de 1978: estructura y contenido. Derechos y deberes fundamentales. Su garantía y suspensión. El Tribunal Constitucional. El Defensor del Pueblo. Reforma de la Constitución.

- **Final figures:** 3,991 words (`wc -w`), 133 parenthesised citations.
- **Verification:** 155 sentences checked, 153 PASS, 2 FAIL (all fixed before closing the tema), 0 unverifiable.
- **Glossary entries with origin here (8):** ley orgánica, recurso de amparo, recurso de inconstitucionalidad, cuestión de inconstitucionalidad, estado de alarma, estado de excepción, Defensor del Pueblo, principios rectores de la política social y económica.
- **Lo que más cae, as in the lesson:**

- Los proyectos de reforma constitucional se aprueban por mayoría de tres quintos de cada una de las Cámaras (art. 167.1 CE).
- Los miembros del Tribunal Constitucional se designan por nueve años y se renuevan por terceras partes cada tres (art. 159.3 CE).
- El Tribunal Constitucional tiene 12 miembros: cuatro a propuesta del Congreso, cuatro del Senado, dos del Gobierno y dos del Consejo General del Poder Judicial (art. 159.1 CE).
- El ejercicio del derecho de reunión no necesita autorización previa (art. 21.1 CE).
- La detención preventiva dura como máximo setenta y dos horas, y el plazo máximo de la prisión provisional lo determina la ley (art. 17.2 y 17.4 CE).
- La Constitución tiene un título preliminar y diez títulos (CE).
- La suspensión de los derechos y libertades está en el capítulo quinto del título I (art. 55 CE).
- El estado de alarma dura un plazo máximo de quince días, y el de excepción no más de treinta días prorrogables por otro plazo igual (art. 116.2–3 CE).
- Una Comisión Mixta Congreso-Senado se relaciona con el Defensor del Pueblo, que es elegido para cinco años (art. 2.1–2 LO 3/1981).
- El recurso de amparo frente a resoluciones judiciales se interpone en 30 días, y el de inconstitucionalidad en tres meses (art. 44.2 y art. 33.1 LOTC).

### Writer's notes and verification detail

- **Lo que más cae** (sources):
  1. Reforma ordinaria, tres quintos de cada Cámara (art. 167.1 CE): conv2025_A P1 1.
  2. TC, nueve años, renovación por terceras partes cada tres (art. 159.3 CE): conv2025_X P1 1.
  3. TC, 12 miembros y quién los propone (art. 159.1 CE): option type «cantidad / órgano».
  4. Reunión sin autorización previa (art. 21.1 CE): conv2025_X P1 29.
  5. Detención 72 horas; prisión provisional por ley (art. 17.2 y 17.4 CE): conv2024_X P1 1.
  6. Título preliminar y diez títulos: conv2024_A P1 2.
  7. Suspensión en el capítulo quinto del título I (art. 55 CE): conv2022_X P1 1.
  8. Alarma quince días, excepción treinta prorrogables (art. 116.2–3 CE): conv2022 P1 33 (who declares), option type «plazo».
  9. Comisión Mixta Congreso-Senado; cinco años (art. 2 LO 3/1981): conv2024_A P1 1.
  10. Amparo 30 días frente a resoluciones judiciales; inconstitucionalidad tres meses (arts. 44.2 y 33.1 LOTC): option type «plazo».
- **Ambiguities / outside sources:**
  - The number and dates of the CE reforms are not in the consolidated PDF. Taken from the BOE consolidated-legislation API (`/legislacion-consolidada/id/BOE-A-1978-31229/analisis`, read 2026-10-16): 13.2 (27-08-1992), 135 (27-09-2011), 49 (15-02-2024), 69.3 (19-05-2026). The lesson does not say which procedure each followed; no source in sources/normativa states it.
  - The sanción date (27-12-1978) and BOE núm. 311 come from the PDF header and signature block, not from an article.
  - LO 3/1981 consolidated text dates from 2009-11-04; no later change is recorded in normativa.yaml.
- **Normativa:** R1 gave CE títulos I, IX and X. The lesson also cites the preámbulo, título preliminar, arts. 81, 87 and 116, the disposición derogatoria and the disposición final. LOTC and LO 3/1981 now carry the articles actually cited.
- **Verification:** 155 sentences checked, 153 PASS, 2 FAIL, 0 UNVERIFIABLE. Fixed:
  - Line 5 (inference): «la ratificó en referéndum» → «la ratificó (preámbulo CE)»; the CE text does not name the referéndum.
  - Line 260 (scope): «solo pueden recurrir leyes del Estado» → «leyes, disposiciones o actos con fuerza de ley del Estado» (art. 32.2 LOTC).

## I.2 — `m01-l02`

La Jefatura del Estado. La Corona: funciones constitucionales del Rey. Sucesión y regencia.

- **Final figures:** 2,489 words (`wc -w`), 71 parenthesised citations.
- **Verification:** 100 sentences checked, 95 PASS, 5 FAIL (all fixed before closing the tema), 0 unverifiable.
- **Glossary entries with origin here (5):** Monarquía parlamentaria, refrendo, Regencia, derecho de gracia, sesión conjunta.
- **Lo que más cae, as in the lesson:**

- Corresponde al Rey sancionar y promulgar las leyes (art. 62.a CE).
- El Rey ejerce el derecho de gracia con arreglo a la ley, que no podrá autorizar indultos generales (art. 62.i CE).
- Corresponde al Rey el mando supremo de las Fuerzas Armadas (art. 62.h CE).
- Al Rey corresponde, previa autorización de las Cortes Generales, declarar la guerra y hacer la paz (art. 63.3 CE).
- Los actos del Rey los refrendan el Presidente del Gobierno y, en su caso, los Ministros competentes (art. 64.1 CE).
- La propuesta y el nombramiento del Presidente del Gobierno y la disolución del artículo 99 los refrenda el Presidente del Congreso (art. 64.1 CE).
- El Rey nombra y releva libremente a los miembros civiles y militares de su Casa (art. 65.2 CE).
- Extinguidas todas las líneas llamadas en Derecho, las Cortes Generales proveen a la sucesión en la forma que más convenga a los intereses de España (art. 57.3 CE).
- La Regencia nombrada por las Cortes Generales se compone de una, tres o cinco personas (art. 59.3 CE).
- El Rey sanciona las leyes en el plazo de quince días (art. 91 CE).

### Writer's notes and verification detail

- Words: 2.489 (wc -w, after verification fixes). Above the ~1,800 target, inside the 1,500–4,000 range: the table of nominations and the
  list of the Rey's functions outside título II (arts. 90–160) take the extra length.
- Citations: 71 parenthesised «(art…)» citations, plus 6 article cells in the nominations table.

#### Lo que más cae

| Line | Motivated by |
|---|---|
| Sancionar y promulgar las leyes (62.a) | conv2025_A P1 2; conv2022_X P1 10 (distractor «aprobar y refrendar») |
| Derecho de gracia, no indultos generales (62.i) | conv2022_X P1 13 (distractor «podrá autorizar indultos generales») |
| Mando supremo de las Fuerzas Armadas (62.h) | conv2025_X P1 2 |
| Guerra y paz, previa autorización de las Cortes Generales (63.3) | conv2024_A P1 3; conv2022_X P1 13 |
| Refrendo: Presidente del Gobierno y, en su caso, Ministros (64.1) | conv2025_X P1 reserva 5 |
| Refrendo del Presidente del Congreso, tres actos (64.1) | style guide: órgano |
| Casa del Rey, nombra y releva libremente (65.2) | conv2024_X P1 2 |
| Extinción de líneas: Cortes Generales, intereses de España (57.3) | conv2022 P1 34 |
| Regencia de una, tres o cinco personas (59.3) | style guide: cantidad |
| Sanción en quince días (91) | style guide: plazo |

#### Normativa

- CE: arts. 1.3, 12, 56–65 (título II), 74.1, 90.2, 91, 92.2, 99, 100, 114, 115.1, 117.1, 122.3, 123.2, 124.4, 151.2,
  152.1, 159.1, 160 y 168. The R1 range (arts. 56–65) is kept; the other articles are the Rey's functions outside
  título II and the reform rule for título II.

#### Ambiguities (not resolved)

- Art. 74.1 CE: «competencias no legislativas que el Título II atribuye expresamente a las Cortes Generales». The CE
  does not list them. The lesson lists the cases in which título II names the Cortes Generales (57.3, 57.4, 59.2,
  59.3, 60.1, 63.3; after verification) and does not claim that each is a «competencia» in the sense of 74.1; the juramento (61.1) in
  particular is a proclamation «ante las Cortes Generales», not an act of theirs. 57.5 (ley orgánica) is left out
  because it is legislative.
- Art. 56.3 CE cites «el artículo 65, 2» (comma notation of the original). The lesson writes «art. 65.2».
- Art. 59.4 asks «español» for the Regencia, art. 60.1 «español de nacimiento» for the tutor. The lesson states the
  difference as the text gives it.
- The LO 3/2014 (abdicación de Juan Carlos I) is the ley orgánica of art. 57.5 actually used; it is not in
  sources/normativa/, so the lesson does not mention it.

#### Verification

Separate reviewer pass (SP/out/I.2/verification.md): 100 sentences checked, 95 PASS, 5 FAIL, 0 unverifiable. All
five fixed; re-checked against CE arts. 62, 91, 122.3, 151–152, 61.1 and 63.3.

| # | Line | Reason | Fix |
|---|---|---|---|
| 28 | 66 | «No las aprueba: las aprueban las Cortes Generales» cited to art. 62, which does not say it | Split the citations: 62.a, 91, 62.f |
| 48 | 124–125 | «En todos los casos la propuesta o la elección es de otro órgano»: 122.3 names no organ for the 12 judicial members of the CGPJ | Reworded with the exception: those twelve are left by the CE to the ley orgánica |
| 54 | 134 | «Comunidad Autónoma del artículo 152»: 152.1 refers to Estatutos approved by the procedure of art. 151 | «cuyo Estatuto se aprobó por el procedimiento del artículo 151», still cited 152.1 |
| 80 | 234–242 | List of título II cases involving the Cortes omitted 63.3 | Added «autorizar al Rey a declarar la guerra y hacer la paz (art. 63.3 CE)» |
| 86 | 242 | «recibir el juramento del Rey»: 61.1 gives the Cortes no act | Item deleted |

Normativa line unchanged (91 and 62–63 were already listed).

## I.3 — `m01-l03`

Las Cortes Generales: composición, atribuciones y funcionamiento del Congreso de los Diputados y del Senado.

- **Final figures:** 3,609 words (`wc -w`), 97 parenthesised citations.
- **Verification:** 134 sentences checked, 132 PASS, 1 FAIL (all fixed before closing the tema), 1 unverifiable.
- **Glossary entries with origin here (13):** mandato imperativo, inviolabilidad, inmunidad, suplicatorio, Diputación Permanente, Grupo Parlamentario, Grupo Mixto, Junta de Portavoces, Comisión Mixta, ley de bases, iniciativa popular, veto, referéndum consultivo.
- **Lo que más cae, as in the lesson:**

- Nadie podrá ser miembro de las dos Cámaras simultáneamente, ni acumular el acta de una Asamblea de
  Comunidad Autónoma con la de Diputado al Congreso (art. 67.1 CE).
- El Congreso se compone de un mínimo de 300 y un máximo de 400 Diputados (art. 68.1 CE).
- Ceuta y Melilla eligen cada una dos Senadores y un Diputado (arts. 68.2 y 69.4 CE).
- En las causas contra Diputados y Senadores es competente la Sala de lo Penal del Tribunal Supremo (art.
  71.3 CE).
- Los períodos ordinarios de sesiones van de septiembre a diciembre y de febrero a junio (art. 73.1 CE).
- No se delegan en las Comisiones la reforma constitucional, las cuestiones internacionales, las leyes
  orgánicas y de bases y los Presupuestos Generales del Estado (art. 75.3 CE).
- La Diputación Permanente tiene un mínimo de veintiún miembros y sigue en funciones hasta la
  constitución de las nuevas Cortes Generales (arts. 78.1 y 78.3 CE).
- El voto de Senadores y Diputados es personal e indelegable (art. 79.3 CE).
- El Senado tiene dos meses para vetar o enmendar, veinte días naturales en los proyectos urgentes, y el
  veto exige mayoría absoluta (arts. 90.2 y 90.3 CE).
- Grupo Parlamentario del Congreso: quince diputados, o cinco escaños con una media del 10 por 100 o el 3
  por 100 nacional (art. 23.1 Reglamento del Congreso, desde 23-12-2026).

### Writer's notes and verification detail

- Words (wc -w): 3,567. Parenthesised citations: 90.
- Sources read: CE título III (arts. 66–96) plus arts. 145.2, 155.1 and 158.2 (consolidated 2026-05-20); Reglamento del
  Congreso (consolidated 2026-07-28) arts. 1–89; Reforma del Reglamento del Congreso de 23-07-2026 (BOE-A-2026-16353);
  Reglamento del Senado (consolidated 2025-11-14) arts. 1–100.

#### Lo que más cae

| Line | Motivated by |
|---|---|
| Incompatibility of both Cámaras and the autonomic acta (art. 67.1 CE) | conv2025_A P1 3; conv2024_X P1 3 |
| Congreso 300–400 Diputados (art. 68.1 CE) | conv2025_X P1 3 |
| Ceuta y Melilla: two Senadores and one Diputado each (arts. 68.2 y 69.4 CE) | conv2024_X P1 4 |
| Sala de lo Penal del Tribunal Supremo for causas against parlamentarios (art. 71.3 CE) | conv2024_A P1 4 |
| Periods of sessions (art. 73.1 CE) | style guide: plazos / dates |
| Matters not delegable to Comisiones (art. 75.3 CE) | conv2022 P1 8 |
| Diputación Permanente: minimum 21, until the new Cortes are constituted (arts. 78.1 y 78.3 CE) | conv2022_X P1 16 and 19 |
| Voto personal e indelegable (art. 79.3 CE) | conv2022_X P1 19 |
| Senate veto/amendments: two months, twenty natural days if urgent, absolute majority (arts. 90.2 y 90.3 CE) | conv2024_A P1 18 |
| Grupo Parlamentario thresholds, forthcoming wording (art. 23.1 Reglamento del Congreso, desde 23-12-2026) | style guide: quantities; cambio-pendiente |

#### Normativa

- CE: arts. 66–92 y 94–96 (título III), 145.2, 155.1 y 158.2. Art. 93 is not cited (no exam question; dropped for length).
- Reglamento del Congreso: arts. 10, 14, 23–25, 30, 37, 39, 41, 43, 46, 57 y 85, with the R1 cambio-pendiente sentence.
- Reglamento del Senado: arts. 5, 27–28, 53, 55 y 93.
- R1 listed both Reglamentos without range; the ranges above are the articles the lesson cites.

#### Ambiguities and facts without a source in sources/normativa/

1. **Effective date of the new art. 23 Reglamento del Congreso.** The reform's disposición final says only «entrará en
   vigor en la XVI legislatura» — a condition, not a date. The lesson writes «(desde 23-12-2026)», taking the date of
   the constitutive session from normativa.yaml (RD 806/2026, BOE-A-2026-20742, which is not in sources/normativa/).
   Whether «XVI legislatura» starts on election day (29-11-2026) or at the constitutive session is not stated; not
   resolved here. The marker «(desde 23-12-2026)» stays because the round requires a date: the reform says «en la XVI
   legislatura», and 23-12-2026 is the constitutive session set by RD 806/2026 (art. 5, fetched by the reviewer).
2. **Formentera.** The sentence rests on the Reforma del artículo 69.3 CE de 19-05-2026 (BOE-A-2026-10881), fetched
   from boe.es by the reviewer; the amending text is not in sources/normativa/. Its disposición transitoria única
   postpones the new circunscripción to the first Senate elections convened after 20-05-2026 (fixed after verification).
3. **Sesión constitutiva of 23-12-2026** (stated in the Grupos paragraph): source is normativa.yaml, not a downloaded
   norm.
4. **Glossary `g-mayoria-absoluta`**: the definition («mayoría de los miembros de derecho, no de los presentes») is the
   standard meaning but no article in sources defines it. Keep only if the 2+-lessons rule applies (it will).
5. **Reglamento del Congreso name.** The consolidated text says the Reglamento is renamed «Reglamento del Congreso de 10
   de febrero de 1982» (Reforma de 22-07-2025, BOE-A-2025-15844). The lesson uses that name.
6. Reglamento del Senado: normativa.yaml notes pending recursos de inconstitucionalidad against arts. 107.3, 108.6,
   116.3, 122, 126 ter 1, 129.5, 133, 143.2 and 143.5. None of these is cited.

#### Verification

Blind pass (SP/out/I.3/verification.md): 134 sentences checked, 132 PASS, 1 FAIL (fixed), 1 UNVERIFIABLE.

- FAIL, row 29 (Formentera): the reform is in force since 20-05-2026, but its disposición transitoria única defers the
  new circunscripción to the first Senate elections convened afterwards. Replaced with the reviewer's text.
- UNVERIFIABLE, row 78: «(desde 23-12-2026)» on art. 23 Reglamento del Congreso; kept, listed as ambiguity 1.

## I.4 — `m01-l04`

El Poder Judicial. El Consejo General del Poder Judicial. El Tribunal Supremo. La organización judicial española.

- **Final figures:** 3,173 words (`wc -w`), 118 parenthesised citations.
- **Verification:** 133 sentences checked, 130 PASS, 3 FAIL (all fixed before closing the tema), 0 unverifiable.
- **Glossary entries with origin here (7):** potestad jurisdiccional, Consejo General del Poder Judicial, Ministerio Fiscal, orden jurisdiccional, partido judicial, Tribunal de Instancia, juez de paz.
- **Lo que más cae, as in the lesson:**

- Jueces y Magistrados: independientes, inamovibles, responsables y sometidos únicamente al imperio de la ley (art. 117.1 CE).
- La potestad jurisdiccional corresponde exclusivamente a los Juzgados y Tribunales determinados por las leyes (art. 117.3 CE).
- CGPJ: el Presidente del Tribunal Supremo y veinte miembros nombrados por el Rey por cinco años (art. 122.3 CE).
- Juristas del CGPJ: abogados y otros juristas con más de quince años de ejercicio, elegidos por tres quintos (art. 122.3 CE).
- El Presidente del Tribunal Supremo lo nombra el Rey, a propuesta del Consejo General del Poder Judicial (art. 123.2 CE).
- El Fiscal General del Estado lo nombra el Rey, a propuesta del Gobierno, oído el Consejo General del Poder Judicial (art. 124.4 CE).
- Presidente del Tribunal Supremo y del CGPJ: elegido por tres quintos de los miembros del Pleno (art. 586.3 LOPJ).
- El Tribunal Supremo tiene cinco Salas; la Quinta es la de lo Militar (art. 55 LOPJ).
- Jueces de Paz: nombrados por cuatro años por la Sala de Gobierno del Tribunal Superior de Justicia (art. 101.1 LOPJ).
- Comisión Permanente del CGPJ: el Presidente y siete Vocales, elegidos anualmente (art. 601 LOPJ).

### Writer's notes and verification detail

- Words: 3,100 (`wc -w`, everything). Target was about 2,500; trimmed from a 4,357 first draft. Body without the two end blocks is about 2,850.
- Citations: 118 parenthesised «(art…)» citations, plus 2 to LO 1/2025 transitional provisions.
- Texts used: CE (2026-05-20), LOPJ (2025-02-17, already carries LO 1/2025 and LO 3/2024 on the CGPJ), Ley 38/1988 (2025-01-03), LO 1/2025 (2025-06-04).

#### Lo que más cae

| Fact | Source |
|---|---|
| Jueces y Magistrados independientes, inamovibles, responsables y sometidos únicamente al imperio de la ley (art. 117.1 CE) | conv2022 P1 27 |
| Potestad jurisdiccional exclusiva de los Juzgados y Tribunales (art. 117.3 CE) | conv2024_X P1 5 |
| CGPJ: Presidente del TS + veinte miembros, cinco años (art. 122.3 CE) | style guide: quantities/organs |
| Juristas del CGPJ: más de quince años, tres quintos (art. 122.3 CE) | conv2025_X P1 4 |
| Presidente del TS: el Rey, a propuesta del CGPJ (art. 123.2 CE) | conv2025_A P1 4; conv2022_X P1 25 |
| Fiscal General: el Rey, a propuesta del Gobierno, oído el CGPJ (art. 124.4 CE) | conv2024_A P1 6 |
| Presidente del TS y del CGPJ: tres quintos del Pleno (art. 586.3 LOPJ) | style guide: majorities |
| Cinco Salas del TS, la Quinta de lo Militar (art. 55 LOPJ) | style guide: organs |
| Jueces de Paz: cuatro años, Sala de Gobierno del TSJ (art. 101.1 LOPJ) | style guide: plazos/organs |
| Comisión Permanente: Presidente + siete Vocales, anual (art. 601 LOPJ) | style guide: quantities |

#### Normativa

- CE: arts. 117–124 y 127 (título VI). Arts. 125–126 dropped from the text in the trim, so the R1 range 117–127 narrows.
- LOPJ: the article list in the lesson. R1 gave the norm alone.
- Ley 38/1988: arts. 1 y 2 (jurisdicción nacional; Ceuta y Melilla in the TSJ de Andalucía).
- LO 1/2025: disposiciones transitorias primera y segunda (dates of constitution of the Tribunales de Instancia and of the Tribunal Central de Instancia).

#### Ambiguities and notes (not resolved)

- LO 1/2025, DT 1.ª, points 1.º and 2.º: «… y los Juzgados de Violencia sobre la Mujer, en aquellos partidos judiciales donde no exista otro tipo de Juzgados» — the qualifier can read as applying to both kinds of Juzgado or only to the Violencia ones. The lesson keeps the norm's wording and word order.
- Date of the organisation described: the three phases ended on 31-12-2025, so the planta of 2027 is the Tribunales de Instancia one. The DT 1.ª keeps the old regime «hasta la definitiva implantación» in each partido; the lesson does not state that implantation is complete everywhere, only the legal dates.
- CE art. 122.3 says «doce entre Jueces y Magistrados … cuatro a propuesta del Congreso … y cuatro a propuesta del Senado», while LOPJ art. 567.2 has each Chamber elect ten (six judicial + four jurists). Both are stated, each with its own citation; the CE grid is only the «juristas» split by Chamber.
- LOPJ art. 101.3 and 101.5 still say «Juez de Primera Instancia e Instrucción» after LO 1/2025 (the organ no longer exists as such). Not used in the lesson.
- LOPJ art. 589.4 says «De no alcanzarse mayoría absoluta …» right after 589.2 requires three fifths for the Vicepresidente. Not used beyond 589.2.
- The consolidated LOPJ is of 2025-02-17; normativa.yaml lists no pending change. Not re-checked against BOE for 2025-2026 amendments in this round.

#### Verification

133 sentences checked: 130 PASS, 3 FAIL, all fixed. Report: SP/out/I.4/verification.md.

| FAIL | Fix |
|---|---|
| Art. 573.1 LOPJ: candidature open to any Juez o Magistrado en servicio activo; the norm's exception was dropped | Added «salvo que se halle en alguna de las situaciones que, conforme a la LOPJ, se lo impidan» |
| Art. 561.2 LOPJ: «improrrogable» stated without the same apartado's exceptional prórroga | Added the prórroga the órgano remitente may grant: quince días, diez if urgency was stated |
| Art. 102 LOPJ: requirements for juez de paz dropped the incapacidad/incompatibilidad condition and its exception | Added «no estén incursos en las causas de incapacidad o de incompatibilidad … a excepción del ejercicio de actividades profesionales o mercantiles» |

Also reworded the two constitution-date sentences (transitional provisions 1 and 2 of LO 1/2025) so they state the dates the law fixes, not completed events.

## I.5 — `m01-l05`

El Gobierno y la Administración. El Presidente del Gobierno. El Consejo de Ministros. Designación, causas de cese y responsabilidad del Gobierno. Las funciones del Gobierno. Relaciones entre el Gobierno y las Cortes Generales.

- **Final figures:** 3,300 words (`wc -w`), 92 parenthesised citations.
- **Verification:** 129 sentences checked, 128 PASS, 1 FAIL (all fixed before closing the tema), 0 unverifiable.
- **Glossary entries with origin here (7):** estado de sitio, cuestión de confianza, moción de censura, Gobierno en funciones, Ministros sin cartera, Comisiones Delegadas del Gobierno, investidura.
- **Lo que más cae, as in the lesson:**

- La cuestión de confianza se entiende otorgada con la mayoría simple de los Diputados (art. 112 CE).
- La moción de censura se adopta por mayoría absoluta del Congreso, la propone al menos la décima parte de los Diputados e incluye un candidato (art. 113.1–2 CE).
- La moción de censura no puede votarse hasta pasados cinco días desde su presentación (art. 113.3 CE).
- El Gobierno se compone del Presidente, de los Vicepresidentes, en su caso, de los Ministros y de los demás miembros que establezca la ley (art. 98.1 CE).
- Las deliberaciones del Consejo de Ministros son secretas (art. 5.3 Ley 50/1997).
- El Ministro de la Presidencia actúa como Secretario del Consejo de Ministros (art. 18.1 Ley 50/1997).
- La Comisión General de Secretarios de Estado y Subsecretarios no puede adoptar en ningún caso decisiones o acuerdos por delegación del Gobierno (art. 8.4 Ley 50/1997).
- En la investidura basta la mayoría simple en una segunda votación cuarenta y ocho horas después de la primera (art. 99.3 CE).
- La responsabilidad criminal de los miembros del Gobierno se exige ante la Sala de lo Penal del Tribunal Supremo (art. 102.1 CE).
- El Presidente en funciones no puede plantear la cuestión de confianza (art. 21.4 Ley 50/1997).

### Writer's notes and verification detail

- Words (wc -w): 3.289 (3,298 before the verification fix). Draft 1 ran to 4,513; cut per the 4,000 cap by dropping secondary detail (art. 105 CE, art. 24.1 forms of decisions, Plan Anual Normativo, Gabinetes appointments, disp. adic. 3.ª, part of the delegation rules). Every plazo, mayoría and órgano the exams ask stays.
- Citations: 92 parenthesised «(art…)» citations.
- Norms: CE títulos IV–V; Ley 50/1997 (consolidated 2025-01-03). No cambio-pendiente norm in this tema.

#### Lo que más cae (source)

1. Cuestión de confianza: mayoría simple de los Diputados (art. 112 CE) — conv2025_A P1 5.
2. Moción de censura: mayoría absoluta; décima parte de los Diputados; candidato (art. 113.1–2 CE) — style guide: mayoría/cantidad.
3. Moción de censura: no se vota hasta pasados cinco días (art. 113.3 CE) — style guide: plazo; conv2022_X P1 7 asks the EU analogue.
4. Composición del Gobierno según art. 98.1 CE — conv2025_X P1 5.
5. Deliberaciones del Consejo de Ministros secretas (art. 5.3 Ley 50/1997) — conv2024_A P1 7.
6. Ministro de la Presidencia, Secretario del Consejo de Ministros (art. 18.1 Ley 50/1997) — conv2022 P1 28.
7. La Comisión General de Secretarios de Estado y Subsecretarios no adopta acuerdos por delegación del Gobierno (art. 8.4 Ley 50/1997) — conv2024_A P1 5.
8. Investidura: mayoría simple en segunda votación a las cuarenta y ocho horas (art. 99.3 CE) — style guide: plazo/mayoría.
9. Responsabilidad criminal ante la Sala de lo Penal del Tribunal Supremo (art. 102.1 CE) — style guide: órgano (conv2024_A P1 4 asks the same for Diputados, art. 71).
10. Presidente en funciones no puede plantear la cuestión de confianza (art. 21.4 Ley 50/1997) — style guide: excepción.

Also covered in the prose for asked questions: Secretariado del Gobierno functions (art. 9 Ley 50/1997, conv2024_X P1 6); art. 103.1 CE principles (conv2024_X P1 20, conv2022 P1 10); art. 107 CE Consejo de Estado (conv2025_A reserva 5).

#### Ambiguities (not resolved)

- Art. 98.1 CE admits «los demás miembros que establezca la ley»; art. 1.2 Ley 50/1997 lists only Presidente, Vicepresidentes and Ministros. The lesson states both and adds «Los Secretarios de Estado no son miembros del Gobierno», which is an inference from art. 1.2 (art. 7.1 calls them órganos superiores de la AGE). Reviewer: confirm the inference is acceptable or cut the sentence.
- Art. 2.2.j Ley 50/1997 has a typo in the consolidated text: «Secretarías de Estado, Asimismo,» (comma before a capital). Wording otherwise clear.
- Art. 8.1 Ley 50/1997: «Asistirá igualmente el Abogado General del Estado» — the lesson says «Asiste también», keeping that he attends rather than integrates the Comisión.
- The Ley 50/1997 file is consolidated 2025-01-03 and includes the art. 26.2 change by LO 1/2025 (not cited in the lesson).

#### Normativa

- CE: arts. 97–104 y 106–107 (título IV) y 108–116 (título V). R1 had arts. 97–107 y 108–116; art. 105 is not cited, so the range is split.
- Ley 50/1997 (Gobierno): arts. 1–15, 18, 20–21, 24 y 29. R1 listed the norm without a range; ranges checked against the títulos I–IV and VI of the consolidated text.

#### Verification

- Sentences checked: 129 (blind reviewer, SP/out/I.5/verification.md). PASS 128, FAIL 1, unverifiable 0.
- FAIL #7, line 11: «Los Secretarios de Estado no son miembros del Gobierno» was an inference; no article says it. Fix: sentence deleted. Art. 1.2 Ley 50/1997 (the composition) stays in that paragraph, and art. 7.1 (órganos superiores de la AGE) is already stated in the Secretarios de Estado section. The matching ambiguity above is resolved by this deletion.

## I.6 — `m01-l06`

El Gobierno Abierto: concepto y principios informadores. La Agenda 2030 y los Objetivos de Desarrollo Sostenible.

- **Final figures:** 2,177 words (`wc -w`), 12 parenthesised citations.
- **Verification:** 99 sentences checked, 93 PASS, 6 FAIL (all fixed before closing the tema), 0 unverifiable.
- **Glossary entries with origin here (2):** consulta pública, Agenda 2030.
- **Lo que más cae, as in the lesson:**

- La Agenda 2030 tiene 17 Objetivos de Desarrollo Sostenible y 169 metas (Resolución 70/1 de la Asamblea General de la ONU, de 25 de septiembre de 2015).
- La Agenda 2030 la aprobó la Asamblea General de las Naciones Unidas el 25 de septiembre de 2015 (Resolución 70/1).
- La meta 15.6, sobre los recursos genéticos, pertenece al Objetivo 15 (Resolución 70/1), «Vida de ecosistemas terrestres» en la web de las Naciones Unidas.
- El IV Plan de Gobierno Abierto 2020-2024 se aprobó el 29 de octubre de 2020 y se articula en cinco ejes (IV Plan de Gobierno Abierto).
- El V Plan de Gobierno Abierto 2025-2029 lo aprobó el pleno del Foro de Gobierno Abierto el 6 de octubre de 2025 (Portal de la Transparencia).
- El V Plan tiene 10 compromisos y 218 iniciativas, y suprime los ejes del IV Plan (V Plan de Gobierno Abierto).
- España se unió a la Alianza para el Gobierno Abierto en 2011, el año de su fundación (Portal de la Transparencia).
- La OCDE nombra cuatro principios: transparencia, integridad, rendición de cuentas y participación de las partes interesadas (Recomendación de la OCDE, de 14 de diciembre de 2017).
- Se puede prescindir de la consulta, la audiencia y la información públicas en las normas presupuestarias u organizativas (art. 133.4 LPAC).

### Writer's notes and verification detail

- Words (wc -w): 2,099. Target was about 1,600; the extra ~500 words are the two lists the exams ask from (17 ODS, 10 compromisos del V Plan) and the three LPAC art. 133 trámites. Within the 1,500–4,000 range.
- Citations: 11 parenthesised article citations («(art. …)»: Ley 19/2013, LRJSP, LPAC); the rest of the facts are cited to outside documents by name (about 20 citations to Resolución 70/1, the OCDE Recommendation, the Planes and the Portal de la Transparencia).

#### Lo que más cae (with motivation)

1. 17 ODS y 169 metas — conv2025_A P1 6 (17 objetivos); style guide «cantidad».
2. Agenda 2030 aprobada por la Asamblea General de la ONU el 25-09-2015 — conv2025_X P1 6 (17 ODS «de las Naciones Unidas»); «fecha».
3. Meta 15.6 (recursos genéticos) → ODS 15 — conv2024_X P1 7.
4. IV Plan aprobado el 29-10-2020, cinco ejes — conv2024_A P1 8 (cinco ejes) and conv2024_X reserva 1 (fecha).
5. V Plan aprobado por el pleno del Foro el 6-10-2025 — conv2022 P1 29 (plan vigente, now «norma modificada»; the current plan is the V); «fecha/órgano».
6. V Plan: 10 compromisos, 218 iniciativas, ejes suprimidos — style guide «cantidad»; distractor bait from the IV Plan's ejes.
7. España en la OGP desde 2011, año de su fundación — conv2022_X P1 22 (OGP; dudosa) family.
8. Cuatro principios OCDE — programme «concepto y principios informadores»; «enunciado».
9. Art. 133.4 LPAC: prescindir de los trámites en normas presupuestarias u organizativas — «excepción».

#### Ambiguities and sources outside sources/normativa (not resolved; listed)

Fuera de sources/normativa. Each fact below was checked read-only against the primary document; none is in the BOE consolidated collection:
- Resolución 70/1 de la Asamblea General (A/RES/70/1), Spanish PDF: https://documents.un.org/api/symbol/access?s=A/RES/70/1&l=es&t=pdf — date 25-09-2015, title, 17 ODS / 169 metas (preámbulo, párr. 18), five esferas, párr. 55, 82, 84, 87, ODS 15 meta 15.6, ODS 16 title and metas 16.6, 16.7, 16.10. Copy saved in SP/dl-un/.
- ODS short names: https://www.un.org/sustainabledevelopment/es/objetivos-de-desarrollo-sostenible/ (web names, not the resolution's titles; the resolution gives long titles).
- OCDE definition and four principles, OGP founded September 2011, Spain joined 2011, MRI, organisation in Spain (DG Gobernanza Pública, grupo interministerial, Comisión Sectorial, Foro), competence statement, «política palanca»: https://transparencia.gob.es/gobierno-abierto/que-es_organizacion
- Plan periods: https://transparencia.gob.es/gobierno-abierto/planes-accion/planes-accion-anteriores ; plans' definition: https://transparencia.gob.es/gobierno-abierto/planes-accion
- IV Plan approval 29-10-2020 (pleno del Foro), 10 compromisos, EJE 1–5: https://transparencia.gob.es/gobierno-abierto/planes-accion/documentos_ivplan and the PDF /content/dam/transparencia_home/gobierno-abierto/ivpga/documentos/IVPlanGobiernoAbierto_ES_vdef.pdf
- V Plan approval 6-10-2025 (pleno del Foro): https://transparencia.gob.es/gobierno-abierto/planes-accion/vplan ; 10 compromisos, 218 iniciativas (123/82/13), ejes suprimidos, two ejes transversales, OGP copresidency 2024-2025: PDF /content/dam/transparencia_home/gobierno-abierto/vpga/V%20PLAN_1.pdf
Other points:
- The IV Plan text says its ten compromisos are structured «en torno a cuatro grandes objetivos» plus «un quinto bloque»; its section headings label them «EJE 1» to «EJE 5». The lesson says nine compromisos in four ejes and a fifth eje with compromiso 10, following the headings. The official key «cinco ejes» (conv2024_A P1 8) matches the headings, not the «cuatro objetivos» sentence.
- The Foro de Gobierno Abierto was re-founded: the portal reports a «Proyecto de Real Decreto por el que se crea y regula el Foro de Gobierno Abierto» and the constitutive meeting of the new Foro (news of 10-08-2026). I could not identify the approved norm (number, BOE date). The lesson describes the Foro without citing its regulating norm and does not cite Orden HFP/134/2018, which created the previous Foro. Check before R3.
- The Estrategia de Desarrollo Sostenible 2030 (asked in conv2025_X P1 6) is not described: its official PDF (mdsocialesa2030.gob.es) did not download (certificate / HTML response), so its approval date is unverified and omitted.
- LPAC art. 133 carries the STC 55/2018 note (contrary to the constitutional order of competences except the first inciso of 133.1 and the first paragraph of 133.4). It binds the AGE in full; the lesson does not go into the STC. Worth one line in III.1, not here.
- conv2022_X P1 22 (Spain on the OGP Steering Committee) stays out: the mandate status is unknown (as the exams ledger says).

#### Normativa

- Ley 19/2013: art. 1 y preámbulo (R1 had no range; the tema rests on the plans, as R1 said).
- Ley 40/2015 (LRJSP): art. 3.1 — new for this tema.
- Ley 39/2015 (LPAC): art. 133 — new for this tema.
- Line «Fuera del BOE» lists the outside documents.

#### Verification

Separate pass (SP/out/I.6/verification.md): 99 sentences checked, 93 PASS, 6 FAIL, 0 unverifiable. Fixes (inferences deleted, not defended):
1. L3 «Ninguna ley española define el Gobierno Abierto» — absolute claim with no source. Deleted; the paragraph now says only that the definition, plans and Agenda come from outside the BOE, and that transparency and participation rest on laws. Same clause deleted from the g-gobierno-abierto definition.
2. L31 «Cada uno tiene reflejo en una ley española» — false for integridad. Deleted. The summary now says the laws back «la transparencia y la participación», not «esos principios».
3. L76–77 integridad = título II of Ley 19/2013 — inference; the law never uses «integridad». Replaced by the art. 1 wording on buen gobierno; heading renamed «Rendición de cuentas y buen gobierno».
4. L116/118 V Plan 2025-2029 cited to «Planes anteriores», which lists I–IV only. Caption now cites the I–IV periods to that page and the V Plan period to «Diseño del V Plan de Gobierno Abierto 2025-2029».
5. L203–204 «Tres de sus metas recogen los principios del Gobierno Abierto» — the resolution makes no such link. Now «Entre sus metas están estas»; heading «El Objetivo 16».
6. L220 «vida de ecosistemas terrestres» attributed to Resolución 70/1 — it is the website's short name. Line now cites the Objetivo 15 to the resolution and the name to the UN website.
Words after fixes: 2.098.

## I.7 — `m01-l07`

La Ley 19/2013, de 9 de diciembre, de transparencia, acceso a la información pública y buen gobierno.

- **Final figures:** 3,651 words (`wc -w`), 94 parenthesised citations.
- **Verification:** 107 sentences checked, 104 PASS, 3 FAIL (all fixed before closing the tema), 0 unverifiable.
- **Glossary entries with origin here (5):** información pública, publicidad activa, derecho de acceso a la información pública, autoridad administrativa independiente, silencio administrativo.
- **Lo que más cae, as in the lesson:**

- El derecho de acceso puede limitarse por perjuicio a la seguridad nacional, la defensa o la seguridad pública, entre otros límites (art. 14.1 Ley 19/2013).
- La publicidad activa de la Administración General del Estado la controla el Consejo de Transparencia y Buen Gobierno (art. 9.1 Ley 19/2013).
- La solicitud de acceso se resuelve y notifica en un mes, ampliable por otro mes, y el silencio es desestimatorio (art. 20.1 y 20.4 Ley 19/2013).
- La reclamación ante el Consejo es potestativa, se interpone en un mes y se resuelve en tres meses, con silencio desestimatorio (art. 24 Ley 19/2013).
- El solicitante no está obligado a motivar la solicitud de acceso (art. 17.3 Ley 19/2013).
- Se inadmite la solicitud sobre información en curso de elaboración, auxiliar o de apoyo, o que exija reelaboración (art. 18.1 Ley 19/2013).
- La Comisión de Transparencia y Buen Gobierno incluye un Diputado, un Senador y representantes del Tribunal de Cuentas, el Defensor del Pueblo, la Agencia Española de Protección de Datos y la Autoridad Independiente de Responsabilidad Fiscal, pero no del Consejo General del Poder Judicial (art. 36.2 Ley 19/2013).
- El Presidente del Consejo se nombra por cinco años no renovables mediante Real Decreto, con refrendo del Congreso por mayoría absoluta en un mes (art. 37.1 Ley 19/2013).
- Las entidades privadas que perciben en un año más de 100.000 euros en ayudas o subvenciones públicas, o cuyos ingresos anuales son al menos en un 40 % ayudas o subvenciones públicas con un mínimo de 5.000 euros, están sujetas a la publicidad activa (art. 3.b) Ley 19/2013).
- Las infracciones de buen gobierno prescriben a los cinco años las muy graves, a los tres las graves y al año las leves (art. 32.1 Ley 19/2013).

### Writer's notes and verification detail

- Word count (wc -w): 3,594. Citations: 95 parenthesised citations («(art…», «(arts…», «(disposición…»); 110 before the cuts.
- Structure: título preliminar (art. 1) → título I (ámbito arts. 2–3; publicidad activa arts. 5–10; acceso arts. 12–20 y 22; impugnaciones arts. 23–24 y DA 4) → título II (arts. 25–32) → título III (arts. 33–40, with RD 615/2024) → DA 6 and DF 9.
- First draft was 5,450 words; cut to the 4,000 cap at the coordinator's request. Dropped: art. 4, art. 5.5, art. 6 bis, art. 8.3, art. 11, art. 15.3 ponderación criteria, art. 19.1, 19.4, art. 21, art. 22.2–22.3, art. 30.6–30.8, art. 31.5, art. 36.4, DA 1, Estatuto art. 18.1 (vocal mandate). None of them is asked in bloque1_questions.md.

#### Lo que más cae (with source)

1. Límites del art. 14.1 (seguridad nacional, defensa, seguridad pública) — conv2025_A P1 7 (seguridad nacional), conv2024_X P1 8 (seguridad pública).
2. Control de la publicidad activa de la AGE por el CTBG, art. 9.1 — conv2025_X P1 7.
3. Plazo de resolución de un mes ampliable por otro; silencio desestimatorio, art. 20.1 y 20.4 — style guide: plazo.
4. Reclamación ante el CTBG: potestativa, un mes, tres meses, desestimada, art. 24 — conv2024_A P1 10.
5. No obligación de motivar, art. 17.3 — style guide: texto alterado.
6. Causas de inadmisión, art. 18.1 — style guide: otra figura del mismo tipo.
7. Composición de la Comisión, art. 36.2 (no CGPJ) — conv2022 P1 reserva 2.
8. Presidente: cinco años no renovables, Real Decreto, refrendo por mayoría absoluta en un mes, art. 37.1 — conv2024_A P1 reserva 1 (distractor «cuatro años»).
9. Entidades privadas del art. 3.b) (100.000 €, 40 %, 5.000 €) — style guide: cantidad.
10. Prescripción de infracciones, art. 32.1 — style guide: plazo.

#### Ambiguities and inconsistencies (not resolved)

- **Ministry names frozen in the consolidated text (2022-07-09).** Art. 10.1 makes the Portal de la Transparencia depend on the «Ministerio de la Presidencia»; arts. 31.2, 31.4, 33.1 and 37.1 name the «Ministro/Ministerio de Hacienda y Administraciones Públicas». The lesson quotes them and says «según el texto de la ley». Current ministry names are a question for RD 829/2023 / RD 1009/2023, not checked here.
- **Art. 33.1 vs Estatuto art. 1.1.** The Ley says the CTBG is an «organismo público» of DA 10 Ley 6/1997 «adscrito al Ministerio de Hacienda y Administraciones Públicas»; RD 615/2024 calls it an «autoridad administrativa independiente» (arts. 109–110 LRJSP) linked through the Ministerio para la Transformación Digital y de la Función Pública. The lesson cites art. 33.2 (personality, independence) from the Ley and the nature and link from the Estatuto; it does not quote art. 33.1.
- **Art. 36.2.g) vs Estatuto art. 17.1.f).** The Ley names a representative of the «Secretaría de Estado de Administraciones Públicas»; the Estatuto, of the «Secretaría de Estado de Función Pública». The lesson gives both, attributed.
- **Art. 23.1 and 24.3** still refer to the repealed Ley 30/1992 (arts. 107.2 and the recursos rules). The lesson states the rule without the cross-reference.
- **Art. 32.3** cites «Ley 30/1992, de 30 de noviembre» (the real date is 26 de noviembre); typo in the BOE text, not used.

#### Normativa

- Ley 19/2013 (transparencia): arts. 1–3, 5–10, 12–20 y 22–40, disposiciones adicionales cuarta y sexta, y disposición final novena.
- RD 615/2024 (Estatuto del CTBG): arts. 1, 12 y 17 del Estatuto.
- R1 left no range for either norm; both ranges come from the citations in the text.

#### Verification

Separate reviewer pass (SP/out/I.7/verification.md). Sentences checked: 107. PASS: 104. FAIL: 3. Unverifiable: 0. All three FAILs fixed with the reviewer's proposed wording:

1. L25–26, art. 2.1.g): «participación de esas entidades» narrowed the referent to the 2.1.f) institutions. Fixed to «la participación, directa o indirecta, de las entidades previstas en el artículo 2 sea superior al 50 por 100».
2. L239–241, art. 29.3: leves given as a closed list, missing the incumplimiento de los principios de actuación del art. 26.2.b) and the residual condition. Fixed to the full letter b) with «cuando no constituyan infracción grave o muy grave ni estén tipificados en otra norma».
3. L366, «Lo que más cae», art. 3.b): «un 40 % de ingresos públicos» misstated the test. Fixed to «cuyos ingresos anuales son al menos en un 40 % ayudas o subvenciones públicas con un mínimo de 5.000 euros».

Word count after fixes: 3.648 (wc -w).

## I.8 — `m01-l08`

La Administración General del Estado. Órganos centrales. Órganos superiores y directivos. Órganos territoriales. La Administración del Estado en el Exterior.

- **Final figures:** 3,577 words (`wc -w`), 113 parenthesised citations.
- **Verification:** 128 sentences checked, 123 PASS, 5 FAIL (all fixed before closing the tema), 0 unverifiable.
- **Glossary entries with origin here (10):** alto cargo, órganos superiores, órganos directivos, servicios comunes, unidades administrativas, Delegado del Gobierno, Subdelegado del Gobierno, Servicio Exterior del Estado, Oficinas Consulares, Representaciones Permanentes.
- **Lo que más cae, as in the lesson:**

- La jefatura superior de todo el personal del Departamento corresponde al Subsecretario (art. 63.1.f LRJSP).
- Órganos superiores: Ministros y Secretarios de Estado; los demás de la organización central son órganos directivos (art. 55.3 LRJSP).
- Los Delegados del Gobierno son órganos directivos con rango de Subsecretario (art. 72.3 LRJSP).
- Los Subsecretarios los nombra y separa un Real Decreto del Consejo de Ministros a propuesta del titular del Ministerio (art. 63.3 LRJSP).
- Los Subdirectores generales los nombra y cesa el Ministro, Secretario de Estado o Subsecretario del que dependan (art. 67.2 LRJSP).
- Los Directores generales se nombran entre funcionarios de carrera A1 o quienes perdieron esa condición por jubilación, salvo que el Real Decreto de estructura lo excepcione con memoria razonada (art. 66.2 LRJSP).
- La Administración General del Estado se organiza en Presidencia del Gobierno y en Ministerios (art. 57.1 LRJSP).
- Los órganos de nivel inferior a Subdirección General se crean por orden del Ministro respectivo, previa autorización del Ministro de Hacienda y Administraciones Públicas (art. 59.2 LRJSP).
- Las Oficinas Consulares de Carrera se crean y suprimen por real decreto del Consejo de Ministros, a iniciativa del Ministerio de Asuntos Exteriores (art. 47.2 Ley 2/2014).
- Las Representaciones Permanentes representan a España ante la Unión Europea o una Organización Internacional (art. 42.2 Ley 2/2014).

### Writer's notes and verification detail

- Words (wc -w): 3.572 after verification fixes (3,520 before) (title and the nombramientos table included). Target ~3,000; cap 4,000.
- Parenthesised citations: 112.
- Structure follows LRJSP título I: cap. I (arts. 54–56), cap. II Ministerios (arts. 57–68), cap. III órganos territoriales (arts. 69–79), cap. IV exterior (art. 80) → Ley 2/2014 título III (arts. 41–48).

#### Lo que más cae (source)

1. Jefatura superior de todo el personal del Departamento: Subsecretario (art. 63.1.f LRJSP) — conv2025_A P1 8; conv2022 P1 11; distractor in conv2024_X P1 9.
2. Órganos superiores: Ministros y Secretarios de Estado (art. 55.3 LRJSP) — style guide, órgano de otro nivel; conv2022 P1 35 (FALSA on Delegados as «órganos superiores»).
3. Delegados del Gobierno: órganos directivos con rango de Subsecretario (art. 72.3 LRJSP) — conv2022_X P1 31; conv2022 P1 35.
4. Subsecretarios: Real Decreto del Consejo de Ministros a propuesta del titular del Ministerio (art. 63.3 LRJSP) — conv2022_X P1 28.
5. Subdirectores generales: nombra y cesa Ministro, Secretario de Estado o Subsecretario del que dependan (art. 67.2 LRJSP) — conv2022_X P1 34 (FALSA b), conv2024_X sup. II 10, conv2022_X sup. II 19 (A1).
6. Directores generales funcionarios A1 salvo excepción con memoria razonada (art. 66.2 LRJSP) — conv2022_X P1 34; style guide, excepción.
7. AGE se organiza en Presidencia del Gobierno y en Ministerios (art. 57.1 LRJSP) — conv2022_X P1 37.
8. Órganos inferiores a Subdirección General: orden del Ministro, previa autorización del Ministro de Hacienda y AAPP (art. 59.2 LRJSP) — conv2024_A sup. I reserva 5 (merging two Subdirecciones; the art. 59.1 Real Decreto route).
9. Oficinas Consulares de Carrera: real decreto del Consejo de Ministros, a iniciativa de Asuntos Exteriores (art. 47.2 Ley 2/2014) — conv2025_X P1 8.
10. Representaciones Permanentes ante la UE o una Organización Internacional (art. 42.2 Ley 2/2014) — conv2024_A P1 9.

#### Normativa

- CE: art. 103. LRJSP: arts. 3 y 54–80 (R1 range 54–80 checked against the text: título I runs arts. 54–80; art. 81 opens título II). Ley 2/2014: arts. 1, 41, 42, 44, 47 y 48 (new range). Ley 50/1997: arts. 4, 7, 12 y 15. Ley 3/2015: art. 2. RD 829/2023: arts. 1 y 22. RD 1009/2023: cited without article (named only as the structure decree).
- The R1 stub listed RD 829/2023 and RD 1009/2023 without ranges; RD 829/2023 now has arts. 1 and 22.

#### Ambiguities / inconsistencies (not resolved)

1. **Stale ministry names in the consolidated texts.** LRJSP (consolidated 2024-08-02) still says «Ministerio de Hacienda y Administraciones Públicas» in arts. 54.2, 59.1, 59.2, 61.c, 63.1.c, 69.3, 73, 76, 78.1; Ley 2/2014 (consolidated 2018-06-12) says «Ministerio de Asuntos Exteriores y de Cooperación» and «Ministerio de Hacienda y Administraciones Públicas». The lesson quotes the law's names and gives the current departments only where a source says so: función pública → Ministerio para la Transformación Digital y de la Función Pública (art. 22.2 RD 829/2023); exterior → Ministerio de Asuntos Exteriores, Unión Europea y Cooperación (art. 1 RD 829/2023). conv2024_A sup. I reserva 5 reads art. 59 with «Ministro para la Transformación Digital y de la Función Pública».
2. **Adscription of the Delegaciones del Gobierno (art. 69.3 LRJSP).** No source in sources/normativa/ states which current ministry they are adscritas to (RD 829/2023 art. 12.1 gives «organización territorial del Estado» to Política Territorial; RD 1009/2023 art. 11 has a DG de la AGE en el Territorio). The lesson does not state the adscription; it was removed from the draft.
3. **Ley 2/2014 art. 44.4** refers to «apartado 10 del artículo 6 de la Ley 6/1997», a law repealed by the LRJSP. Not used in the lesson.
4. **LRJSP arts. 65.3 and 67.2** cite «artículo 76 de la Ley 7/2007» (EBEP, repealed) while arts. 63.3 and 66.2 cite the TREBEP. Same Subgrupo A1; lesson says «Subgrupo A1» only.
5. **Art. 61.f LRJSP** reads «cuando la competencia no esté atribuida al Consejo de Ministros a otro órgano» (missing comma/«,»); lesson reads it as a list of three.
6. **RD 829/2023 is consolidated to 2023-12-29** (normativa.yaml: no later amendments on boe.es at 2026-10-16). The 22-ministry list rests on that; RD 806/2026 dissolved the Cortes (elections 29-11-2026), so a new government after the elections may restructure ministries before the exam.

#### Verification

Blind pass (SP/out/I.8/verification.md): 128 sentences checked, 123 PASS, 5 FAIL, 0 unverifiable. All five fixed in the lesson:

1. L169, Secretarios generales (art. 64.1 LRJSP): «solo si su norma de estructura lo prevé» was an inference. Now: «Cuando las normas de estructura de un Ministerio prevén un Secretario general, determinan sus competencias sobre un sector de actividad administrativa».
2. L217, table row Subsecretario (art. 63.3 LRJSP): requirement left out the jubilados. Now «Funcionario de carrera A1, o jubilado que lo fue».
3. L220, table row Director general (art. 66.2 LRJSP): same omission. Now «Funcionario de carrera A1, o jubilado que lo fue, salvo excepción motivada».
4. L223–224, idoneidad under the table: the cited arts. 63.3–66.2 do not cover Ministros and Secretarios de Estado. Split into: Ministros and Secretarios de Estado are named also per Ley 3/2015 (art. 55.10 LRJSP); the four directive organs meet the idoneidad requirements «en todo caso» (arts. 63.3, 64.3, 65.3 y 66.2 LRJSP; art. 2.1 Ley 3/2015).
5. L368, Lo que más cae on Directores generales (art. 66.2 LRJSP): jubilados exception added («entre funcionarios de carrera A1 o quienes perdieron esa condición por jubilación, salvo…»).

After the fixes: wc -w 3.572; stray-marker regex clean.

## I.9 — `m01-l09`

La Organización territorial del Estado: las Comunidades Autónomas. Constitución y distribución de competencias entre el Estado y las Comunidades Autónomas. Estatutos de Autonomía.

- **Final figures:** 3,692 words (`wc -w`), 70 parenthesised citations.
- **Verification:** 82 sentences checked, 77 PASS, 5 FAIL (all fixed before closing the tema), 0 unverifiable.
- **Glossary entries with origin here (5):** Estatuto de Autonomía, ley marco, Tribunal Superior de Justicia, Fondo de Compensación, competencia exclusiva.
- **Lo que más cae, as in the lesson:**

- El Estado se organiza territorialmente en municipios, en provincias y en las Comunidades Autónomas que se constituyan (art. 137 CE).
- El equilibrio económico que vela el Estado es «adecuado y justo» y atiende en particular al hecho insular (art. 138.1 CE).
- Iniciativa del artículo 143: Diputaciones y dos terceras partes de los municipios, en seis meses; si no prospera, se reitera pasados cinco años (art. 143 CE).
- Las Cortes, por ley orgánica y por motivos de interés nacional, pueden acordar un Estatuto para territorios no integrados en la organización provincial (art. 144.b) CE).
- Los Estatutos son la norma institucional básica de cada Comunidad y el Estado los reconoce y ampara como parte de su ordenamiento (art. 147.1 CE).
- La reforma de un Estatuto requiere en todo caso aprobación de las Cortes Generales mediante ley orgánica (art. 147.3 CE).
- Los montes y aprovechamientos forestales están en la lista de competencias que pueden asumir las Comunidades (art. 148.1.8.ª CE).
- Tráfico y circulación de vehículos a motor es competencia exclusiva del Estado (art. 149.1.21.ª CE).
- En los Estatutos aprobados por la vía del artículo 151, la representación ordinaria del Estado en la Comunidad corresponde a su Presidente (art. 152.1 CE).
- Las medidas del artículo 155 exigen requerimiento previo al Presidente de la Comunidad y aprobación por mayoría absoluta del Senado (art. 155.1 CE).

### Writer's notes and verification detail

- Words: 3,645 (wc -w). Target was about 2,800; the overrun is the verbatim art. 148.1 list (22 materias, about 420 words), kept whole because the exams draw options from it (montes, puertos deportivos, sanidad e higiene). Art. 149.1 is given as 15 of its 32 materias, verbatim, including the four asked (9.ª, 20.ª, 21.ª, 26.ª). Within the 1,500–4,000 range.
- Citations: 70 parenthesised (68 «(art./arts. … CE)», 2 «(disp. trans. … CE)»).
- Structure: CE art. 2; título VIII cap. I (137–139); cap. III (143–158) in article order, grouped as constitución de las CCAA, Estatutos, organización, competencias, control, financiación; plus 81, 161 and DT 2.ª, 5.ª.

#### Lo que más cae

| Fact | Source |
|---|---|
| Municipios, provincias y CCAA que se constituyan (art. 137) | conv2022 P1 36 |
| Equilibrio «adecuado y justo», hecho insular (art. 138.1) | conv2025_X P1 9 (texto alterado: «apropiado», «autonomía») |
| Iniciativa art. 143: 2/3 municipios, seis meses, cinco años | option type plazo / cantidad |
| Art. 144.b): territorios no integrados en la organización provincial, interés nacional | conv2022_X P1 2 |
| Estatuto: norma institucional básica; el Estado lo reconoce y ampara (art. 147.1) | conv2024_A P1 11 |
| Reforma estatutaria: Cortes Generales mediante ley orgánica (art. 147.3) | conv2024_A P1 11 (distractor c) |
| Montes y aprovechamientos forestales en art. 148.1.8.ª | conv2025_X P1 10 |
| Tráfico y circulación de vehículos a motor, art. 149.1.21.ª | conv2024_X P1 10 |
| Representación ordinaria del Estado: Presidente de la CA (art. 152.1) | conv2025_A P1 9 |
| Art. 155: requerimiento al Presidente + mayoría absoluta del Senado | option type órgano / mayoría |

#### Ambiguities and notes (not resolved)

- Art. 152.1 lays down the institutional organization only for Statutes approved «por el procedimiento a que se refiere el artículo anterior» (art. 151). The lesson says so and does not extend it to the art. 143 Communities, although all Statutes adopted the same model. The exam (conv2025_A P1 9) asks the «representación ordinaria» citing art. 152 without that nuance.
- Art. 147.3 vs 152.2: the referéndum is required by the CE only for art. 151 Statutes; Statutes of the art. 143 route may require it in their own procedure. The lesson states only what the two articles say.
- The CE's DT 1.ª, 3.ª, 4.ª (Navarra), 6.ª, 7.ª and DA 1.ª (derechos históricos de los territorios forales) were left out for length; no bloque I official question asks them.
- Normativa: R1's range «arts. 137–158 (título VIII)» narrowed to the articles cited. Art. 161 (TC: impugnación with five-month suspension; conflictos de competencia) is cited here and belongs to I.1 too.

#### Normativa

- CE: arts. 2, 81, 137–139, 143–158 (título VIII, capítulos primero y tercero) y 161; disposiciones transitorias segunda y quinta.

#### Verification

Separate reviewer pass (SP/out/I.9/verification.md): 82 sentences checked; 77 PASS, 5 FAIL, 0 unverifiable. All five fixed in the lesson; words after fixes 3.692, citations 72.

| # | Line | FAIL | Fix |
|---|---|---|---|
| 26 | 109–112 | DT 2.ª «abrió esta vía» / «les bastaba»: inference; DT 2.ª refers to art. 148.2 and art. 151.2, not to the 151.1 iniciativa | Rewritten to the DT's own terms: proceder inmediatamente en la forma del art. 148.2 por acuerdo por mayoría absoluta de los órganos preautonómicos, comunicándolo al Gobierno; proyecto conforme al art. 151.2 a convocatoria del órgano preautonómico |
| 30 | 132–133 | «Los Estatutos fijan además el carácter…» turns art. 145.2's «podrán prever» into an obligation | «Pueden prever también el carácter y efectos de la comunicación…» |
| 33 | 144–145 | «norma de cada Comunidad, no del Estado» contradicts «parte integrante de su ordenamiento jurídico» | «El Estado reconoce el Estatuto como parte integrante de su ordenamiento jurídico (art. 147.1 CE).» |
| 55 | 292 | «El artículo 150 permite mover competencias fuera del reparto…»: no article says this; 150.3 moves nothing | «El artículo 150 regula las leyes marco, la transferencia o delegación de facultades y las leyes que armonizan las disposiciones normativas de las Comunidades (art. 150 CE).» (the reviewer's «leyes de armonización» not used: the CE does not use that phrase) |
| 80 | 389 | Lo que más cae dropped art. 152.1's limit to Estatutos of the art. 151 route | «En los Estatutos aprobados por la vía del artículo 151, la representación ordinaria del Estado en la Comunidad corresponde a su Presidente (art. 152.1 CE).» |

## I.10 — `m01-l10`

La Administración local: entidades que la integran. La provincia, el municipio y la isla.

- **Final figures:** 2,979 words (`wc -w`), 73 parenthesised citations.
- **Verification:** 101 sentences checked, 100 PASS, 1 FAIL (all fixed before closing the tema), 0 unverifiable.
- **Glossary entries with origin here (11):** entidades locales, municipio, provincia, término municipal, Padrón municipal, vecinos, Concejo Abierto, Junta de Gobierno Local, mancomunidades, áreas metropolitanas, municipios de gran población.
- **Lo que más cae, as in the lesson:**

- Cualquier alteración de los límites provinciales la aprueban las Cortes Generales mediante ley orgánica (art. 141.1 CE).
- Son elementos del Municipio el territorio, la población y la organización (art. 11.2 LBRL).
- El Alcalde es elegido por los Concejales o por los vecinos (art. 19.2 LBRL).
- El Alcalde, los Tenientes de Alcalde y el Pleno existen en todos los ayuntamientos (art. 20.1.a LBRL).
- La Junta de Gobierno Local existe en los municipios con población superior a 5.000 habitantes y en los de menos si lo dispone su reglamento orgánico o lo acuerda el Pleno (art. 20.1.b LBRL).
- La Junta de Gobierno Local la forman el Alcalde y Concejales en número no superior al tercio del número legal (art. 23.1 LBRL).
- El Presidente, los Vicepresidentes, la Junta de Gobierno y el Pleno existen en todas las Diputaciones (art. 32.1 LBRL).
- Parque público, biblioteca pública y tratamiento de residuos son obligatorios en los municipios de más de 5.000 habitantes (art. 26.1.b LBRL).
- Gran población: más de 250.000 habitantes o capital de provincia de más de 175.000; capitales y sedes autonómicas y municipios de más de 75.000 con circunstancias especiales, si lo decide la Asamblea Legislativa (art. 121.1 LBRL).
- Un municipio nuevo exige núcleos de población territorialmente diferenciados de al menos 4.000 habitantes (art. 13.2 LBRL).

### Writer's notes and verification detail

- Words (wc -w): 2,937. Parenthesised citations: 72 (10 of them in «Lo que más cae»).
- Sources read: CE arts. 137–142 (BOE-A-1978-31229, 2026-05-20); LBRL arts. 1–44 and 121 (BOE-A-1985-5392,
  2026-10-03); Ley 4/2026 DF 3 (BOE-A-2026-20528).

#### Lo que más cae

| Fact | Motivated by |
|---|---|
| Alteración de límites provinciales: Cortes Generales, ley orgánica (art. 141.1 CE) | conv2024_X P1 11 and reserva 4 |
| Elementos del Municipio: territorio, población y organización (art. 11.2 LBRL) | conv2022 P1 1 |
| Alcalde elegido por los Concejales o por los vecinos (art. 19.2 LBRL) | conv2022_X P1 39 |
| Alcalde, Tenientes de Alcalde y Pleno en todos los ayuntamientos (art. 20.1.a LBRL) | conv2024_A P1 12 |
| Junta de Gobierno Local en municipios de más de 5.000 habitantes (art. 20.1.b LBRL) | conv2024_A P1 12 (distractor); style guide: quantities |
| Junta de Gobierno Local: no más de un tercio del número legal de Concejales (art. 23.1 LBRL) | style guide: quantities |
| Presidente, Vicepresidentes, Junta de Gobierno y Pleno en todas las Diputaciones (art. 32.1 LBRL) | conv2025_X P1 11 |
| Servicios mínimos de más de 5.000 habitantes (art. 26.1.b LBRL) | style guide: quantities |
| Gran población: más de 250.000, o capital de provincia de más de 175.000 (art. 121.1 LBRL) | conv2025_A P1 10 |
| Nuevo municipio: núcleos de al menos 4.000 habitantes (art. 13.2 LBRL) | style guide: quantities |

#### Normativa

- CE: arts. 137 y 140–142.
- LBRL: arts. 3–4, 11–13, 15–16, 19–23, 25–27, 29, 31–36, 39–44 y 121, with the R1 «Cambio pendiente» sentence
  kept. R1's range «arts. 1–41 (títulos I a III)» is replaced by the articles actually cited; títulos IV (42–44)
  and X (121) are added.

#### Cambio pendiente

- Art. 25.2.q) LBRL (Ley 4/2026 DF 3.uno) is stated with «(desde 23-10-2026)». Art. 69.1 (DF 3.dos) is not
  used by the lesson.

#### Ambiguities and inconsistencies (not resolved)

- The consolidated LBRL PDF (2026-10-03) prints art. 25.2.q) and the new art. 69.1 as current text, with no
  «Téngase en cuenta… entra en vigor» notice and no «Redacción anterior» in the text extraction. R1's
  `version_vigente` note says the future-merged files carry both wordings; this one does not appear to. The
  wording matches Ley 4/2026 DF 3 exactly.
- Art. 26.2 LBRL carries the TC 111/2016 notice declaring «incisos destacados» unconstitutional; the
  highlighting is lost in text extraction, so it is unclear which words of the second paragraph are void. The
  lesson does not use art. 26.2.
- Art. 33.4 LBRL still speaks of the «Comisión de Gobierno» while arts. 32–35 call it «Junta de Gobierno».
  The lesson uses «Junta de Gobierno» and does not cite 33.4.
- Art. 28 LBRL in the consolidated text is a «gestión colaborativa» provision for municipios de menos de 20.000
  habitantes (the article was formerly repealed). Not used; flagged because older material calls art. 28 void.

#### Verification

- Blind pass (SP/out/I.10/verification.md): 101 sentences checked; 100 PASS, 1 FAIL, 0 unverifiable.
- FAIL row 87 (line ~296, citation): «La iniciativa puede partir de los propios Municipios» sat under art. 42.1,
  but the rule is in art. 42.2. Fixed: «La iniciativa para crear una comarca puede partir de los propios
  Municipios interesados (art. 42.2 LBRL).»
- PASS notes acted on: the «Lo que más cae» lines for the Junta de Gobierno Local (art. 20.1.b: also in
  municipios of 5,000 or fewer when the reglamento orgánico or the Pleno so provides) and for gran población
  (art. 121.1, adding cases c and d and the Asamblea Legislativa decision) now state the article in full.
- After fixes: 2.979 words; 73 parenthesised citations.

## I.11 — `m01-l11`

La organización de la Unión Europea. El Consejo Europeo, el Consejo, el Parlamento Europeo, la Comisión Europea y el Tribunal de Justicia de la Unión Europea. Efectos de la integración europea sobre la organización del Estado español.

- **Final figures:** 3,902 words (`wc -w`), 115 parenthesised citations.
- **Verification:** 134 sentences checked, 131 PASS, 3 FAIL (all fixed before closing the tema), 0 unverifiable.
- **Glossary entries with origin here (7):** competencia exclusiva, mayoría cualificada, minoría de bloqueo, competencia compartida, cuestión prejudicial, directiva, principio de atribución.
- **Lo que más cae, as in the lesson:**

- El Consejo ejerce conjuntamente con el Parlamento Europeo la función legislativa y la función presupuestaria (art. 16.1 TUE).
- El Consejo Europeo no ejerce función legislativa alguna y se pronuncia por consenso salvo que los Tratados dispongan otra cosa (arts. 15.1 y 15.4 TUE).
- El Presidente del Consejo Europeo se elige por mayoría cualificada para dos años y medio, renovable una sola vez (art. 15.5 TUE).
- El Consejo tiene su sede en Bruselas y celebra sus sesiones en Luxemburgo en abril, junio y octubre (art. 1.3 Reglamento interno del Consejo).
- La violación grave y persistente de los valores del artículo 2 la constata el Consejo Europeo por unanimidad (art. 7.2 TUE).
- La solicitud de ingreso la resuelve el Consejo por unanimidad, tras consultar a la Comisión y con la aprobación del Parlamento Europeo (art. 49 TUE).
- El Parlamento Europeo se reúne sin convocatoria el segundo martes de marzo (art. 229 TFUE).
- La moción de censura no se vota hasta pasados tres días y, si se aprueba, la Comisión dimite colectivamente (art. 234 TFUE).
- Son competencia exclusiva de la Unión la unión aduanera, las normas de competencia del mercado interior, la política monetaria del euro, la conservación de los recursos biológicos marinos y la política comercial común (art. 3.1 TFUE).
- La energía es competencia compartida y la industria es un ámbito de apoyo, coordinación o complemento (arts. 4.2 y 6 TFUE).

### Writer's notes and verification detail

- Words (wc -w): 3,681. Target about 3,000; under the 4,000 cap.
- Citations: 113 parenthesised «(art. …)» / «(arts. …)» citations, plus the Protocolo n.º 6 named in the text above the seats table.
- Sources: TUE and TFUE, consolidated versions DOUE C 202 of 7-6-2016 (CELEX-12016M-12016E); Reglamento interno del Consejo, Decisión 2009/937/UE (DOUE L 325, 11-12-2009), annex art. 1; CE (BOE-A-1978-31229, 2026-05-20).

#### Lo que más cae

| Line | Motivated by |
|---|---|
| Consejo: función legislativa y presupuestaria con el Parlamento (art. 16.1 TUE) | conv2025_A P1 11 |
| Consejo Europeo: no legisla; consenso salvo otra cosa (arts. 15.1 y 15.4 TUE) | conv2025_X P1 12 (option «por consenso»), conv2022_X P1 4 |
| Presidente del Consejo Europeo: mayoría cualificada, dos años y medio, una renovación (art. 15.5 TUE) | style guide: plazos / mayorías |
| Consejo: sede Bruselas; Luxemburgo en abril, junio y octubre (art. 1.3 Reglamento interno) | conv2022 P1 2 |
| Violación grave y persistente: Consejo Europeo por unanimidad (art. 7.2 TUE) | conv2024_A P1 13 |
| Ingreso: Consejo por unanimidad, consulta a la Comisión, aprobación del Parlamento (art. 49 TUE) | conv2025_X P1 12 |
| Parlamento: segundo martes de marzo sin convocatoria (art. 229 TFUE) | conv2022_X P1 7 |
| Moción de censura: tres días; dimisión colectiva (art. 234 TFUE) | conv2024_X P1 12, conv2022_X P1 7 |
| Competencias exclusivas, lista del art. 3.1 TFUE | conv2025_A reserva 3 |
| Energía compartida, industria de apoyo (arts. 4.2 y 6 TFUE) | conv2022 reserva 1 |

#### Normativa block

- TUE: arts. 1–2, 4–5, 7, 13–19, 49 y 50; Protocolo n.º 6 (sedes).
- TFUE: arts. 2–4, 6, 229, 231, 234–236, 238, 244, 247, 250, 252–254, 258–260, 263–264, 267 y 288.
- Reglamento interno del Consejo: arts. 1.3 y 1.4 del anexo.
- CE: arts. 93, 95, 96 y 135.

R1's ranges were TUE 13–19 and TFUE 223–281. Both were checked against the DOUE text: TUE título III is arts. 13–19, and TFUE sexta parte, título I, capítulo 1 (instituciones) runs from art. 223 to art. 287 (BCE and Tribunal de Cuentas are 282–287). The block now lists only the articles the lesson cites.

#### Ambiguities and limits (not resolved)

- **The treaty text is the 2016 consolidation.** TUE art. 52.1 still lists the Reino Unido among the Member States. The UK's withdrawal (art. 50 TUE) is not in the source file. The lesson gives no number of Member States, of Commissioners or of judges for that reason.
- **Members of the Parliament.** Art. 14.2 TUE gives only the ceiling (750 plus the President), the minimum of 6 and the maximum of 96. The actual seat allocation is a later European Council decision that is not in sources/normativa/. Not stated.
- **Abogados generales.** Art. 252 TFUE says eight, with the possibility of an increase by the Council. The lesson says «El TFUE fija ocho abogados generales». Any increase decided by the Council is not in the sources. Check before a question uses the number.
- **Tribunales especializados.** Art. 19.1 TUE and 257 TFUE still provide for them. Whether any exists today is not in the sources. The lesson names them only as part of the structure.
- **Reglamento interno del Consejo.** The file is the 2009 original. normativa.yaml records yearly changes to annex III (population figures). Art. 1.3 and 1.4 of the annex, which the lesson cites, were not checked against a consolidated version. The Protocolo n.º 6 (letra b) gives the same Luxembourg months, so the seat rule has two sources that agree.
- **«Efectos de la integración europea sobre la organización del Estado español».** No norm in sources/normativa/ treats this heading as such. The lesson uses CE arts. 93, 95, 96 and 135, TUE arts. 4.2, 4.3 and 19.1, and TFUE arts. 267 and 288, and states only what those texts say. Domestic organs created for EU affairs (for example a Comisión Mixta para la Unión Europea, or a ministry's secretaría de Estado) are not in any downloaded norm, so they are not mentioned.
- **The CE reform of art. 135 (2011) and of art. 13.2 (1992)** are commonly explained as effects of integration. The consolidated CE PDF does not print reform history, so the lesson does not mention it.

#### Verification

Blind pass (SP/out/I.11/verification.md): 134 sentences checked. 131 PASS, 3 FAIL, 0 unverifiable. All three FAILs are fixed in the lesson with the article's own wording. After the fixes the lesson has 3.780 words (wc -w).

| # | Article | FAIL | Fix |
|---|---|---|---|
| 94 | art. 260.2 TFUE | «Si el Estado no ejecuta la sentencia, el Tribunal puede imponerle…» left out the Comisión's referral, the observations step and the Court's finding. | Now: Comisión estima que no ha adoptado las medidas → somete el asunto tras ofrecer observaciones → indica el importe → si el Tribunal declara el incumplimiento, puede imponer suma a tanto alzado o multa coercitiva. |
| 95 | art. 263 TFUE | «actos de las instituciones destinados a producir efectos jurídicos frente a terceros» was broader than the article. | Now lists the article's scope: actos legislativos; actos del Consejo, de la Comisión y del BCE que no sean recomendaciones o dictámenes; actos del Parlamento Europeo y del Consejo Europeo destinados a producir efectos jurídicos frente a terceros. |
| 121 | art. 267 TFUE | «El órgano judicial que resuelve en última instancia está obligado…» dropped the condition and paraphrased the organ. | Now: a case pending before «un órgano jurisdiccional nacional cuyas decisiones no sean susceptibles de ulterior recurso judicial de Derecho interno», which «está obligado a someterla al Tribunal». |

Optional precision from row 123 (art. 135.3 CE, «en relación con el producto interior bruto del Estado») was not applied. The row is PASS.

## Checks and suites

Run on the final tree (lessons, glossary, course.yaml and goldens of this round):

- **Pipeline, course as draft:** loads and validates; `pytest -k "glossary or registry or content or pipeline"` green on
  the final tree (67 passed), including the never-coins checks for glossary and summaries. `figure steps per course`:
  `age-administrativo-c1: no figures`, `crypto-futures: 34 figures`, `fixture-oposiciones: no figures`.
- **Backend (`uv run pytest`):** 1,374 passed, 20 skipped. This run started before the 15 glossary definitions were
  rewritten; the glossary, registry and content tests were re-run after the rewrite and pass.
- **Frontend (`npx vitest run`):** 563 passed, 49 skipped; `tsc -b` clean. After the glossary rewrite, `src/lib/pdf`,
  `src/lib/glossary` and `src/lib/refs` were re-run: 302 passed, 49 skipped. The list-shape guard («no list marker in the
  middle of a sentence») passes for every lesson; the cross-reference report has 0 dangling references.
- **Goldens:** `glossary-links.es.txt` and `lesson-refs.es.txt` regenerated and reviewed (see Glossary). No diff under
  `content/crypto-futures/`.
- **Android bundle:** re-exported with the same fingerprint `9c95cf4a…` (98 files); `--verify-only` OK.
- **After the five decisions** (lessons I.1, I.3, I.5, I.6, I.8, I.11 edited; glossary untouched): content tests 68
  passed; `src/lib/pdf`, `src/lib/glossary`, `src/lib/refs` 302 passed, 49 skipped; `tsc -b` clean; goldens
  regenerated (still 50 marks, 4 references, 0 dangling); bundle fingerprint unchanged. The full backend and frontend
  suites were not re-run after this pass.

## Open items

- **After the 29-11-2026 elections:** a one-lesson round updates I.8's ministry list and its dated line «Estructura
    vigente a …» once the new government's restructuring decree is published, and re-checks every «(hoy: …)» note in
  bloque I against it. Since bloque II this includes the bloque II notes: Ministerio para la Transformación Digital y
  de la Función Pública (m02-l01, m02-l02, m02-l03), Ministerio de Hacienda (m02-l01), Ministerio de Industria y
  Turismo (m02-l03) and Ministerio de la Presidencia, Justicia y Relaciones con las Cortes (m02-l04).
- **Waiting glossary terms** (see Glossary) enter when a second lesson uses them or a defining article appears.
- **OEP 2026 convocatoria:** when it is published, R0b runs before anything else.
- **RGPD corrigenda (bloque II).** `sources/normativa/` holds the 2016 DOUE original of the RGPD, without corrections.
  Before R3 writes II.4 questions, save the consolidated RGPD text, or its corrección de errores, under `sources/` and
  re-check the verbatim-dependent sentences of m02-l04 (art. 9.1 «orientación sexual», art. 36.1 among them).
- **Norms named but not in `sources/` (bloque II), candidates for `normativa.yaml` before R3 asks about them:**
  RD 776/2011 (supresión of the Comisión Interministerial de Información Administrativa; now cited through the BOE note
  in RD 208/1996). RD 1401/2007 (composition of the Comisión Superior Calificadora de Documentos Administrativos).
  RD 1164/2002 (eliminación de documentos). Decreto 914/1969 (plazos de transferencia to the Archivo General de la
  Administración). The norm that renamed the Puntos de Atención al Emprendedor «al Emprendimiento» (presumably an
  amendment to Ley 14/2013 art. 13). The Acuerdo del Consejo de Ministros of 15-07-2005 (Red de Oficinas Integradas).
- **Orden HAP/1949/2014 status.** It rests on repealed norms and is not repealed expressly. The PAG page still lists
  it, but its address of the oficina 060 (María de Molina, 50) differs from the PAG's current office (Francisco
  Gervás, 7). Check whether a later orden replaced it before R3 asks about the PAG's channels.
- **RD 1112/2018 and STC 100/2019.** The plazos m02-l03 gives (arts. 12.3, 13.4, 13.6) are non-basic and bind the
  AGE. Questions on them must be set in the AGE, or carry the STC note.
- **Glossary candidate «oficinas integradas»** (m02-l01, m02-l03, no defining article) enters if a later lesson or
  norm in `sources/` defines it.

## Where to resume (after bloque I)

Bloque I is closed. The next session starts R2 bloque II (temas II.1–II.4, lessons `m02-l01`…`m02-l04`) with the same
spec plus the five decisions above.

# Bloque II — temas II.1–II.4

Round R2, bloque II, 2026-10-16. Nothing committed. Same procedure as bloque I: one writer per tema to a shared spec
(the bloque I spec plus the standing conventions above, and the rule that any outside source is saved under
`sources/otros/` with URL, date and sha256 before it is cited); then a separate blind reviewer that had not written
the lesson re-opened the cited article for every sentence carrying a number, plazo, majority, organ, date or exception,
checked every citation and the Normativa block, and checked the glossary candidates the same way. Every FAIL was fixed
against the article before the next tema started. The changed sentences then went through a second blind pass. Temas
ran in order. The per-sentence tables are working files, not kept in the repo; their counts and every FAIL are below.

Suites before writing (current tree at the start of the session): backend `uv run pytest` 1,374 passed, 20 skipped;
frontend `npx vitest run` 563 passed, 49 skipped.

## Summary

| Tema | Lesson | Words | Citations | Sentences checked | FAIL (fixed) | Unverifiable | Glossary checked / FAIL (fixed) | Glossary entries |
|---|---|---|---|---|---|---|---|---|
| II.1 | `m02-l01` | 3,482 | 75 | 121 | 7 | 0 | 8 / 0 | 8 |
| II.2 | `m02-l02` | 3,045 | 57 | 108 | 0 | 0 | 12 / 3 | 12 |
| II.3 | `m02-l03` | 3,387 | 68 | 124 | 1 | 0 | 9 / 1 | 9 |
| II.4 | `m02-l04` | 3,870 | 109 | 104 | 5 | 0 | 10 / 0 | 10 |
| **Total** | | **13,784** | **309** | **457** | **13** | **0** | **39 / 4** | **39** |

Words: `wc -w`, everything counted. Citations: parenthesised «(art» / «(arts» only. Citations to saved pages, the
Diccionario and «(disposición…» are counted in each tema's section. Second pass (sentences changed by the fixes and
by the coordinator): II.1 14 checked, 14 PASS; II.2–II.4: see «Second pass» below.

Lengths against the weights. Bloque II gets 14 of the 250 questions of 2025, but II.1 and II.4 recur in the
supuestos (style guide, per-tema table). All four lessons came out above their targets (II.1 3,000; II.2 2,300;
II.3 2,600; II.4 3,500) after cuts from first drafts of 5,500–7,900 words. Each writer cut first what no official
question of 2022–2025 asks; the cuts are listed per tema.

## Glossary

- 39 entries added, origin in bloque II; `glossary.yaml` now holds 118. 38 cite a defining article. «derecho de
  petición» has none in the sources: it enters because m01-l01 (art. 29 CE) and m02-l01 use it in the same sense.
- **The six waiting terms from bloque I** (mayoría absoluta, Gobierno Abierto, Objetivos de Desarrollo Sostenible,
  libre designación, recurso por incumplimiento, recurso de anulación): `grep -il` over all lessons finds none of them
  in a bloque II lesson, and no bloque II norm defines any of them. All six stay waiting. «libre designación» still
  enters with IV.5 (TREBEP / RD 364/1995).
- Not proposed, used once or with no defining article: oficinas integradas (m02-l01 and m02-l03, no defining article;
  candidate if a later lesson defines it), sede electrónica asociada, código seguro de verificación, delegado de
  protección de datos, derecho al olvido, elaboración de perfiles.
- **Glossary verification:** 39 checked, 35 PASS, 4 FAIL, all replaced with the reviewer's article-faithful wording:
  g-patrimonio-documental («parte del Patrimonio Histórico Español» is art. 48.1, not 49.2; both now cited),
  g-documento-administrativo-electronico (two conditions of art. 46.1 RD 203/2021 restored),
  g-archivo-electronico-unico («o actuaciones correspondientes», art. 55.1 RD 203/2021), g-carga-desproporcionada
  (third case of art. 7.2 RD 1112/2018). In the second pass g-carga-desproporcionada failed again: its «teniendo en
  cuenta al mismo tiempo el posible beneficio o perjuicio para los ciudadanos…» clause was missing. It was replaced with
  the reviewer's wording.
- **Goldens.** `glossary-links.es.txt` regenerated and read line by line: 50 → 70 web marks (28 also a PDF link), 90
  linkable terms the book never links. **Wrong-sense link excluded:** g-servicios-comunes in m02-l01 («Entidades
  Gestoras y Servicios Comunes de la Seguridad Social», the same false friend as m01-l07), now in `link_except`. Kept
  after reading: «Ley Orgánica» inside «Ley Orgánica 4/2001» and «Ley Orgánica 3/2018», and «Directiva» inside
  «Directiva 95/46/CE» and «Directiva de Servicios»: each names a real ley orgánica or directiva, so the sense holds.
  Also kept: «personas con discapacidad» in the RDL 1/2013 Normativa lines of the m03-l07 and m04-l02 stubs, same
  sense. `lesson-refs.es.txt`: 4 → 7 references, 0 dangling.

## Second pass

- II.1 (`verification-pass2.md`): 14 sentences, 14 PASS. Covered the seven FAIL fixes and two coordinator changes.
  First, a «(hoy: Ministerio de Hacienda)» note on «Ministerio de Economía y Hacienda» (art. 11.1 RD 951/2005), matched
  to art. 5.1 RD 829/2023 («presupuestos y gastos»). Second, the deletion of art. 6.2.d) RD 208/1996 from the Centro de
  Información Administrativa's list, since it is a function tied to the suppressed Comisión Interministerial.
- II.2–II.4 (`verification-pass2-II2-II4.md`): 9 lesson items, 9 PASS. They covered the art. 11 RD 1708/2011
  citation, the art. 2 RD 127/2015 fix, the new art. 12.3 RD 1112/2018 «Lo que más cae» line and the RD 1112/2018
  Normativa line, the four art. 7.1 / 89.2 / 96.1.a) LOPDGDD sentences and the RGPD Normativa line. Glossary: 4
  checked, 3 PASS, 1 FAIL (g-carga-desproporcionada, fixed as above).

## II.1 — `m02-l01`

Atención al público. Atención de personas con discapacidad. Los servicios de información administrativa. Información general y particular al ciudadano. Iniciativas. Reclamaciones. Quejas. Peticiones.

- **Final figures:** 3,482 words (`wc -w`), 75 parenthesised citations, plus «(disposición derogatoria única.b)
  RD 951/2005)» and «(nota al art. 6.2.d) RD 208/1996)». First draft 5,569 words.
- **Structure:** one `##` per item of the programme sentence, in its order. Atención al público (art. 4 RD 208/1996;
  cartas de servicios, arts. 3–4 and 8–11 RD 951/2005). Discapacidad (arts. 4 and 28 RDL 1/2013; arts. 1–2, 4, 7–8 and
  11–13 RD 366/2007; art. 10 of the Reglamento of RD 707/2026). Servicios de información (arts. 5–6 and 8–13
  RD 208/1996). Información general y particular (arts. 1–3). Iniciativas, Reclamaciones, Quejas (arts. 14–17 and 19
  RD 951/2005). Peticiones (LO 4/2001). No bold lead-ins: the four programme items are sections, not a list.
- **Cambio pendiente:** RD 366/2007 art. 13 in the RD 707/2026 wording, «(desde 02-01-2027)». RDL 1/2013 art. 4.2 in
  the Ley 4/2026 wording, «(desde 23-10-2026)».
- **Verification:** 121 sentences checked, 114 PASS, 7 FAIL (fixed), 0 unverifiable. Glossary 8/8 PASS. Fixed:
  1. Art. 11.1 RD 951/2005: the informe of the Ministerio de Economía y Hacienda when the carta has medidas de
     subsanación de contenido económico was dropped. Restored with «(hoy: Ministerio de Hacienda)».
  2. Art. 28.1 RDL 1/2013: the «No obstante» paragraph (plazos máximos of DA 3.ª.1) was dropped. Restored; DA 3.ª
     added to Normativa.
  3–5. Arts. 4.2.a), 7 and 8.2 RD 366/2007 are «recomendaciones» but read as rules. Each passage is now introduced as
     a recommendation.
  6. Art. 1.1 LO 4/2001: the delito o falta exception was dropped. Restored.
  7. Art. 8 LO 4/2001: the inadmission ground «título específico distinto» was dropped. Restored.
- **Glossary entries with origin here (8):** derecho de petición, cartas de servicios, información general, información
  particular, personas con discapacidad, Oficinas de Atención al Ciudadano, modelos normalizados, accesibilidad
  universal.
- **Lo que más cae, as in the lesson:**

- Las cartas de servicios se actualizan periódicamente en función de las circunstancias y, en cualquier caso, al menos cada tres años (art. 10.4 RD 951/2005).
- Las quejas y sugerencias presentadas por correo electrónico o a través de Internet deben estar suscritas con la firma electrónica del interesado (art. 15.2 RD 951/2005).
- Recibida la queja o sugerencia, la unidad responsable informa al interesado de las actuaciones realizadas en el plazo de 20 días hábiles (art. 16.1 RD 951/2005).
- El plazo de contestación se puede suspender si se requiere al interesado para que formule aclaraciones en un plazo de 10 días hábiles (art. 16.2 RD 951/2005).
- Sin respuesta en plazo, el ciudadano puede dirigirse a la Inspección General de Servicios del departamento para conocer los motivos de la falta de contestación (art. 16.3 RD 951/2005).
- La Inspección General de Servicios de cada departamento hace el seguimiento de las quejas y sugerencias de los órganos, unidades y organismos de su ámbito, tanto centrales como periféricos (art. 17.1 RD 951/2005).
- Las quejas no tienen, en ningún caso, la calificación de recurso administrativo ni su presentación interrumpe los plazos establecidos en la normativa vigente (art. 19 RD 951/2005).
- La jefatura de la unidad departamental de información administrativa la ostenta el titular de la Subdirección General que tenga encomendada la competencia sobre la información administrativa (art. 5.1 RD 208/1996).
- La información general se facilita obligatoriamente, sin exigir la acreditación de legitimación alguna (art. 2.2 RD 208/1996).
- La Administración asegura los derechos de los ciudadanos con discapacidad, entre otros medios, mediante la eliminación y corrección de cualquier norma, criterio, instrucción, actuación, práctica o decisión que suponga una vulneración de la igualdad de oportunidades de las personas con discapacidad (art. 2.d) RD 366/2007).

- **Sources of «Lo que más cae»:** 1 conv2025_A P1 12; 2 conv2025_A sup. I 6; 3 conv2025_A sup. I reserva 5; 4 style
  guide «otro plazo» (conv2020_X sup. I reserva 2, programa anterior); 5 style guide «órgano» (conv2020 sup. I 3); 6
  conv2025_X P1 13; 7 conv2024_X P1 13, conv2022_X P1 40; 8 conv2024_A P1 15; 9 style guide «texto alterado»
  (conv2020_X P1 19); 10 conv2024_X sup. I 5.
- **Normativa:** R1 gave the six norms without ranges. The ranges now come from the citations. LPAC is dropped: after
  the cuts the lesson cites no LPAC article. RD 707/2026 (Reglamento, art. 10) and RD 829/2023 (arts. 5.1 and 22.2) are
  added.
- **Ambiguous or inconsistent texts (listed, not resolved):**
  - «Iniciativas»: no norm defines them as a separate figure. RD 208/1996 art. 4.d) says «iniciativas o sugerencias»
    and RD 951/2005 art. 14 says «sugerencias». RD 208/1996 art. 6.2.d) and its derogatoria (Orden de 5-1-1959,
    «oficinas de iniciativas y reclamaciones») use the older term. The lesson uses the norms' terms; LPAC art. 133 is
    not used.
  - «Reclamaciones»: RD 208/1996 art. 4.e) pairs «quejas y reclamaciones» without telling them apart. RD 951/2005 uses
    «reclamaciones» only for incumplimiento of the cartas (arts. 9.c), 12.1).
  - RD 208/1996 art. 4.d)–e) and its DT única still refer to the capítulo III (Libro de Quejas y Sugerencias),
    derogated by RD 951/2005, whose DT única keeps it «hasta tanto se dicten las normas de aplicación y desarrollo».
  - Comisión Interministerial de Información Administrativa: arts. 11–13 RD 208/1996 «(Derogado)». Only the BOE
    consolidated-text note at art. 6.2.d) states its supresión by RD 776/2011; RD 776/2011 is not in sources/. Art.
    5.3.a) and f) still name a «Comisión Ministerial de Información Administrativa».
  - RD 208/1996 art. 6.1 places the Centro de Información Administrativa under a 1987 structure (RD 221/1987). No file
    in sources/ shows that it still exists with Subdirección General level. The lesson's present tense rests on the
    1996 text.
  - Frozen references in RD 208/1996 (arts. 3.1–3.2, 4.b), 14) to Ley 30/1992 and LO 5/1992. The lesson states the
    rules without them.
  - «Gobiernos Civiles» (art. 9.1 RD 208/1996) quoted as written. No source in sources/ names the successor for this
    article, so there is no «hoy».
  - «Ministerio de Administraciones Públicas» (art. 17.2 RD 951/2005, the IGS for the servicios periféricos of the
    Delegaciones) is quoted without «hoy». The competence match is unclear: the Delegaciones fall under Política
    Territorial, the IGS function under Función Pública. «Secretaría General para la Administración Pública» (arts.
    11.1 RD 951/2005, 11.2 RD 366/2007) is an old organ, not a ministry: quoted, no «hoy».
  - RDL 1/2013 art. 4.2 is rewritten whole by Ley 4/2026, and the file has only the new wording. The 33 % sentence
    carries «(desde 23-10-2026)» although that threshold is probably unchanged; the reviewer agrees the marker is
    harmless.
  - conv2020_X P1 17 (versiones simplificadas, old art. 13.1 RD 366/2007) stays excluded from 02-01-2027; the lesson
    gives only the new art. 13.1.

## II.2 — `m02-l02`

Concepto de documento, registro y archivo. Funciones del registro y del archivo. Clases de archivo y criterios de ordenación.

- **Final figures:** 3,045 words (`wc -w`), 57 parenthesised «(art» citations, plus 3 «(disposición…» and 3 citations
  of the saved Diccionario. First draft 5,563 words.
- **Structure:** concepto de documento (art. 49 Ley 16/1985; art. 2.2.b–d RD 1708/2011; art. 26.1 LPAC; art. 46.1
  RD 203/2021). Then registro (art. 16 LPAC; arts. 38, 40 and 53 RD 203/2021; DA 4 and DF 7 LPAC) and archivo (art. 59.1
  Ley 16/1985; art. 17.1 LPAC; art. 55.1 RD 203/2021). Then funciones (arts. 2.2.e–f, 13.6, 14.1 and DT 1 RD 1708/2011;
  arts. 55 and 58 Ley 16/1985), clases de archivo (arts. 8–12 RD 1708/2011) and criterios de ordenación (Diccionario
  de Terminología Archivística).
- **Outside source saved** (new rule): `sources/otros/cultura-dta-diccionario.html` and
  `cultura-dta-presentacion.html`, Ministerio de Cultura, Diccionario de Terminología Archivística (2.ª ed., 1995),
  in `fuentes.yaml` with sha256. No norm in sources/ lists criterios de ordenación. The Diccionario's «Ordenación»
  entry names cronológicas y/o alfabéticas only, so numérico, geográfico and temático are omitted.
- **Cambio pendiente:** Ley 4/2026 adds only DA 12 to Ley 16/1985 and touches none of the cited articles. The Normativa
  line says so.
- **Verification:** 108 sentences checked, 108 PASS, 0 FAIL, 0 unverifiable. Glossary 12 checked, 9 PASS, 3 FAIL
  (fixed; see Glossary above). After the pass, the citation «art. 11.1.º–3.º RD 1708/2011», which both writer and
  reviewer flagged as readable as an apartado 1, became «art. 11 RD 1708/2011, funciones 1.º a 3.º».
- **Glossary entries with origin here (12):** Patrimonio Documental, documento de archivo, documento electrónico,
  expediente electrónico, documentos públicos administrativos, documento administrativo electrónico, Registro
  Electrónico General, archivo electrónico único, ciclo vital de documentos, calendario de conservación, archivo
  intermedio, Comisión Superior Calificadora de Documentos Administrativos.
- **Lo que más cae, as in the lesson:**

- Los Organismos públicos vinculados o dependientes de cada Administración podrán disponer de su propio registro electrónico plenamente interoperable e interconectado con el Registro Electrónico General de la Administración de la que depende (art. 16.1 LPAC).
- Las disposiciones de creación de registros electrónicos especifican el órgano o unidad responsable de su gestión, así como la fecha y hora oficial y los días declarados como inhábiles (art. 16.1 LPAC).
- Los asientos se anotan respetando el orden temporal de recepción o salida de los documentos e indican la fecha del día en que se produzcan (art. 16.2 LPAC).
- El registro electrónico permite la presentación de documentos todos los días del año durante las veinticuatro horas (art. 31.2.a) LPAC).
- Los archivos del Sistema de Archivos de la Administración General del Estado se clasifican, atendiendo al ciclo vital de los documentos, en archivos de oficina o de gestión, archivos generales o centrales de los Ministerios y de los organismos públicos dependientes de los mismos, archivo intermedio y archivos históricos (art. 8 RD 1708/2011).
- Los archivos de oficina o de gestión eliminan los documentos de apoyo informativo antes de la transferencia al Archivo central (art. 9 RD 1708/2011).
- Llevar a cabo el proceso de identificación de series y elaborar el cuadro de clasificación es función del Archivo Central (art. 10.1 RD 1708/2011).
- El archivo intermedio custodia los documentos generados y reunidos por los Departamentos ministeriales y sus organismos públicos una vez finalizada su fase activa conforme a los calendarios de conservación; en la Administración General del Estado es el Archivo General de la Administración (art. 11 RD 1708/2011).
- Documento electrónico es la información de cualquier naturaleza en forma electrónica, archivada en un soporte electrónico, según un formato determinado y susceptible de identificación y tratamiento diferenciado (art. 2.2.c) RD 1708/2011).
- Documento de archivo es el ejemplar en cualquier tipo de soporte, testimonio de las actividades y funciones de las personas físicas y jurídicas, públicas o privadas (art. 2.2.b) RD 1708/2011).

- **Sources of «Lo que más cae»:** 1–2 conv2025_A P1 13; 3 conv2020 P1 11 (style); 4 conv2020 P1 40 (style); 5
  conv2024_X P1 14; 6 conv2025_X P1 14; 7 conv2022 P1 reserva 5; 8 conv2020_X P1 21 (style); 9 conv2025_X P1 15; 10
  conv2022_X P1 reserva 1.
- **Normativa:** R1 gave «LPAC: arts. 16–17» and the other three norms without ranges. Every range now comes from the
  citations. RD 829/2023 art. 22.1–22.2 is added for the «hoy» note on art. 38.1 RD 203/2021.
- **Ambiguous or inconsistent texts (listed, not resolved):**
  - Art. 12 RD 1708/2011 (consolidated 2024-03-27) has two apartados numbered «2». The lesson cites the second as «el
    segundo apartado numerado 2».
  - Arts. 2.2.c)–d) and 14.1.g) RD 1708/2011 still refer to Ley 11/2007 (repealed); arts. 20–22 and 24 to Ley 30/1992.
  - RD 1708/2011 gives no plazos de transferencia in years. It defers to the calendarios de conservación and,
    transitionally, to the Decreto 914/1969 (DT 1), which is not in sources/. Any year figure needs that decree or a
    departmental calendario saved first.
  - Not in sources/: RD 1401/2007 (composition of the Comisión Superior Calificadora; RD 1708/2011 DF 1 amends its
    art. 2.1.a) and RD 1164/2002 (eliminación de documentos). Both are candidates for normativa.yaml if the bank asks
    them.
  - Art. 58 Ley 16/1985 gives the Comisión Superior Calificadora more competences (integración en los Archivos, acceso,
    inutilidad administrativa) than the lesson and the glossary entry state.
  - «Ministerio de Presidencia» (art. 13.3–13.4 RD 1708/2011, Comisión de Archivos) matches no competence in
    RD 829/2023, so that passage was cut. Art. 40.2 RD 203/2021 (not cited) names the MPTFP and would need its own «hoy».
  - Art. 26.2 LPAC and art. 46.1 RD 203/2021 define the documento electrónico differently (the RD adds the ENI and the
    Derecho administrativo conditions). The lesson quotes both, attributed.

## II.3 — `m02-l03`

Administración electrónica y servicios al ciudadano. Análisis de principales páginas web de carácter público. Servicios telemáticos. Oficinas integradas de atención al ciudadano. Ventanilla única empresarial. El Punto de Acceso General de la Administración General del Estado.

- **Final figures:** 3,387 words (`wc -w`), 68 parenthesised «(art» citations, plus 1 anexo, 1 disposición and 2
  preámbulo citations, and 7 citations of saved pages, each «a fecha de 16-10-2026». First draft 5,783 words.
- **Structure:** administración electrónica (arts. 9.2, 10.1, 12.2 and 14 LPAC; arts. 3.2, 26.2.c) and 30.2
  RD 203/2021; art. 40 LRJSP). Then páginas web (arts. 38–39 LRJSP; arts. 6, 9.1 and 10.1 RD 203/2021; RD 1112/2018)
  and servicios telemáticos (art. 11.2 RD 203/2021; arts. 41.1 and 43 LPAC; arts. 40.3.f–g and 42.5 RD 203/2021). Then
  oficinas integradas (art. 10 RD 208/1996, cross-referenced to m02-l01), ventanilla única empresarial (RD 127/2015)
  and the PAG (arts. 13.a), 43.4 and 53.1.a) LPAC; arts. 7–8 RD 203/2021; Orden HAP/1949/2014). The registro is not
  restated: one cross-reference to m02-l02.
- **Outside sources saved** (`sources/otros/`, in `fuentes.yaml` with url, sha256 and lessons): pag-quienes-somos,
  pag-telefono-060, pag-oficina-informacion, sede-pag-portada, clave-que-es, pae-circe, pae-servicios (cited), and
  pae-subsede (`lessons: []`, it backs the Industria «hoy» note). The reviewer matched every sha256. Not saved:
  carpetaciudadana.gob.es (a JavaScript shell with no text), so Carpeta Ciudadana facts come from art. 8 RD 203/2021;
  one PAE URL returned 404.
- **«hoy» notes (convention 1):** art. 9.2.c) LPAC and art. 6.1 RD 203/2021 → Ministerio para la Transformación Digital
  y de la Función Pública (art. 22.1–22.2 RD 829/2023). Art. 5.1 Orden HAP/1949/2014 → same (art. 22.2). Art. 2
  RD 127/2015 «Ministerio de Industria, Energía y Turismo» → Ministerio de Industria y Turismo (art. 10.1 RD 829/2023).
  The reviewer passed all four. The Industria match is the weakest, because art. 10.1 does not name PYME; it holds
  through RD 1009/2023 art. 9 and pae-subsede.html.
- **Verification:** 124 sentences checked, 123 PASS, 1 FAIL (fixed), 0 unverifiable. Glossary 9 checked, 8 PASS, 1
  FAIL (fixed). Fixed: art. 2 RD 127/2015, the oficinas integradas «creadas según el Acuerdo de Consejo de Ministros de
  15 de julio de 2005» (condition restored). Coordinator change after the pass: the «Lo que más cae» line «El RD
  1112/2018 regula la accesibilidad…» (true but not a fact an option tests) was replaced by the plazo of art. 12.3
  RD 1112/2018. Art. 1 RD 1112/2018 then left the Normativa line because the text no longer cites it.
- **Glossary entries with origin here (9):** sede electrónica, portal de internet, Punto de Acceso General, Carpeta
  Ciudadana, Dirección Electrónica Habilitada única, certificado electrónico, sello electrónico, carga
  desproporcionada, declaración de accesibilidad.
- **Lo que más cae, as in the lesson:**

- La sede electrónica es la dirección electrónica disponible para los ciudadanos a través de redes de telecomunicaciones cuya titularidad corresponde a una Administración Pública, o bien a una o varios organismos públicos o entidades de Derecho Público en el ejercicio de sus competencias (art. 38.1 LRJSP).
- Las Administraciones Públicas podrán identificarse mediante un sello electrónico basado en un certificado electrónico reconocido o cualificado que reúna los requisitos exigidos por la legislación de firma electrónica (art. 40.1 LRJSP).
- En los organismos públicos estatales, la creación o supresión de portales se hace por resolución de la persona titular de la Presidencia o de la Dirección (art. 6.1 RD 203/2021).
- La Dirección Electrónica Habilitada única está alojada en la sede electrónica del PAGe de la Administración General del Estado (art. 7.4 RD 203/2021).
- Las personas físicas podrán elegir en todo momento si se comunican con las Administraciones por medios electrónicos o no, salvo que estén obligadas a relacionarse electrónicamente (art. 14.1 LPAC).
- La notificación electrónica obligatoria, o expresamente elegida por el interesado, se entiende rechazada a los diez días naturales desde su puesta a disposición sin acceso a su contenido (art. 43.2 LPAC).
- La oficina de asistencia en materia de registros puede hacer la identificación o firma electrónica del interesado no obligado a la relación electrónica, en los procedimientos para los que se haya previsto habilitación (art. 40.3.f) RD 203/2021).
- Recibidas las solicitudes de información accesible y las quejas, la entidad obligada debe responder en el plazo de veinte días hábiles (art. 12.3 RD 1112/2018).
- La sede electrónica del PAG se considera la sede central de la Administración General del Estado (art. 7.3 Orden HAP/1949/2014).
- Los PAE utilizan el sistema de tramitación telemática CIRCE e inician la tramitación a través del Documento Único Electrónico (art. 3.2 RD 127/2015).

- **Sources of «Lo que más cae»:** 1 conv2024_A P1 reserva 3; 2 conv2025_A P1 14; 3 conv2024_X P1 15; 4 conv2025_X P1
  16; 5 conv2020_X P1 22 (style); 6 style guide «plazo» (part 2); 7 conv2024_X sup. I 6; 8 style guide «plazo»
  (RD 1112/2018 was asked in conv2022 P1 39); 9 conv2022 P1 40; 10 conv2022 P1 41 (annulled; it tested RD 127/2015).
- **Normativa:** R1 gave the six norms without ranges. The ranges now come from the citations. RD 208/1996 (art. 10)
  and RD 829/2023 (arts. 10.1 and 22.1–22.2) are added. Domains are written without «www.»/«https://» so that
  remark-gfm does not turn them into links.
- **Ambiguous or inconsistent texts (listed, not resolved):**
  - Art. 9.2.c) LPAC requires «previa comunicación» to the SGAD with a two-month window; art. 26.2.c) RD 203/2021
    requires «previa autorización» of the SGAD. The lesson follows the LPAC.
  - «Lista de confianza de prestadores de servicios de certificación» (art. 9.2 LPAC) against «…prestadores
    cualificados de servicios de confianza» (art. 26.2 RD 203/2021). The lesson uses and cites the LPAC.
  - The Orden HAP/1949/2014 rests on repealed norms (Ley 11/2007, RD 1671/2009, Ley 30/1992, Ley 6/1997), names organs
    that no longer exist, and is not repealed expressly. The saved PAG page still lists it as its regulation and gives
    today's gestión (DG de Gobernanza Pública).
  - Arts. 4.2 and 8.5.b) of the Orden: «oficina 060 de calle María de Molina, 50». The saved PAG page gives calle
    Francisco Gervás, 7 and does not call it «060». The lesson gives both, each with its source.
  - Who runs the PAGe: art. 7.4 RD 203/2021 (MPTFP with the SGAD of MAETD) against art. 5 of the Orden (titularidad of
    MinHAP). Both resolve to the same ministry today.
  - RD 127/2015 says «Centro de Información y Red de Creación de Empresa» and «Puntos de Atención al Emprendedor». The
    PAE portal says «…de Empresas» and «Puntos de Atención al Emprendimiento». The renaming norm (presumably an
    amendment to art. 13 Ley 14/2013) is not in sources/ and was not identified.
  - RD 1112/2018: STC 100/2019 makes arts. 12.1, 12.3, 12.4, 12.6, 13 (part), 15.3 and 16.2 non-basic, and an inciso of
    15.3 null. The plazos the lesson gives (arts. 12.3, 13.4, 13.6) are non-basic. They bind the AGE; the lesson does
    not carry the STC note.
  - RD 1112/2018 has no «Observatorio de Accesibilidad Web»: that is a portal service, not saved, so it is omitted.
  - «Servicios telemáticos» and «oficinas integradas» have no defining norm. The Acuerdo del Consejo de Ministros of
    15-07-2005 is not in sources/.
  - The Cl@ve site menu still has «Cl@ve Pin». The saved «¿Qué es Cl@ve?» page names only Cl@ve Móvil and Cl@ve
    Permanente, and the lesson follows the page.

## II.4 — `m02-l04`

La protección de datos personales y su régimen Jurídico: principios, derechos, responsable y encargado del tratamiento, delegado y autoridades de protección de datos. Derechos digitales.

- **Final figures:** 3,870 words (`wc -w`), 109 parenthesised «(art» citations (99 in the body, 10 in «Lo que más
  cae»). First draft 7,914 words.
- **Structure:** programme order. Régimen jurídico (arts. 4.1–4.2 and 99.2 RGPD; art. 1 LOPDGDD). Principios (arts.
  5–7 and 9 RGPD; arts. 5, 6.1, 7.1, 9.1 and 22.3 LOPDGDD). Derechos (arts. 12, 15–17 and 20–22 RGPD; arts. 12.7, 13.3
  and 14 LOPDGDD). Responsable y encargado (arts. 4.7–4.8, 24, 28, 30 and 33–36 RGPD; art. 31.2 LOPDGDD). Delegado
  (arts. 37–39 RGPD; arts. 34, 36–37 and 70.2 LOPDGDD). Autoridades (arts. 51–52, 57–58 and 77 RGPD; arts. 44, 48, 57,
  65, 72–74 and 77–78 LOPDGDD). Derechos digitales (arts. 79–97 LOPDGDD, the título X list by the law's own names).
- **R1's unchecked range, checked now (LOPDGDD):** the writer read the 2025-12-27 consolidated text, títulos I–V and
  VII–X and the disposiciones adicionales primera to sexta. Every cited article exists with that number and heading in
  that text, and none is amended by Ley 10/2025 (which changed only art. 23, not cited). The RGPD stub range «arts.
  5–39 y 51–59» is replaced by the articles cited. The lesson cites arts. 4, 58, 77 and 99, which are outside the stub
  range, and does not cite 8, 10–11, 13–14, 18–19, 23, 25–27, 29, 31–32, 53–56 or 59.
- **«hoy» note:** «Ministerio de Justicia» (art. 44.1 LOPDGDD) → Ministerio de la Presidencia, Justicia y Relaciones con
  las Cortes. It cites art. 3.2 RD 829/2023 («las demás funciones atribuidas por las leyes») and its disposiciones
  finales primera and segunda. The reviewer passed it, noting that RD 829/2023 never names the AEPD, so the match is
  generic.
- **Verification:** 104 sentences checked, 99 PASS, 5 FAIL (fixed), 0 unverifiable. Glossary 10/10 PASS. Fixed with the
  reviewer's wording:
  1–2. Art. 7.1 LOPDGDD, body and «Lo que más cae»: the exception now carries «para la celebración del acto o negocio
     jurídico en cuyo contexto se recaba el consentimiento».
  3. Art. 89.2 LOPDGDD: «de los trabajadores o los empleados públicos» restored, so it is no longer a general ban.
  4. Art. 96.1.a) LOPDGDD: the herederos' access to the caudal relicto is restored.
  5. Normativa RGPD line: art. 57 RGPD, cited in the text, was missing; added.
- **Glossary entries with origin here (10):** datos personales, responsable del tratamiento, encargado del tratamiento,
  consentimiento del interesado, limitación del tratamiento, violación de la seguridad de los datos personales,
  categorías especiales de datos, responsabilidad proactiva, desconexión digital, Agencia Española de Protección de
  Datos.
- **Lo que más cae, as in the lesson:**

- Los responsables y encargados del tratamiento, así como todas las personas que intervengan en cualquier fase de este, están sujetos al deber de confidencialidad, que se mantiene aun finalizada su relación con el responsable o encargado (art. 5.1 y 5.3 LOPDGDD).
- El tratamiento de los datos de un menor solo puede fundarse en su consentimiento si es mayor de catorce años, salvo que la ley exija la asistencia de los titulares de la patria potestad o tutela para el acto o negocio jurídico en cuyo contexto se recaba el consentimiento (art. 7.1 LOPDGDD).
- El responsable informa de sus actuaciones sobre la solicitud de ejercicio de derechos en un mes desde su recepción, plazo prorrogable otros dos meses en caso necesario, teniendo en cuenta la complejidad y el número de solicitudes (art. 12.3 RGPD).
- En la solicitud de rectificación, el afectado indica a qué datos se refiere y la corrección que haya de realizarse, y acompaña la documentación justificativa cuando sea preciso (art. 14 LOPDGDD).
- Las imágenes de videovigilancia se suprimen en el plazo máximo de un mes desde su captación, salvo que deban conservarse para acreditar la comisión de actos que atenten contra la integridad de personas, bienes o instalaciones (art. 22.3 LOPDGDD).
- La violación de la seguridad se notifica a la autoridad de control sin dilación indebida y, de ser posible, a más tardar 72 horas después de tener constancia de ella, salvo que sea improbable que constituya un riesgo para los derechos y las libertades de las personas físicas (art. 33.1 RGPD).
- Las entidades aseguradoras y reaseguradoras deben designar delegado de protección de datos en todo caso; los profesionales de la salud que ejercen su actividad a título individual están exceptuados (art. 34.1.g) y l) LOPDGDD).
- El delegado tiene acceso a los datos personales y procesos de tratamiento, sin que el responsable o el encargado puedan oponerle la existencia de cualquier deber de confidencialidad o secreto (art. 36.3 LOPDGDD).
- La Presidencia de la Agencia y su Adjunto son nombrados por el Gobierno, a propuesta del Ministerio de Justicia (art. 48.3 LOPDGDD).
- Los actos y disposiciones de la Presidencia ponen fin a la vía administrativa y son recurribles directamente ante la Sala de lo Contencioso-administrativo de la Audiencia Nacional (art. 48.6 LOPDGDD).

- **Sources of «Lo que más cae»:** 1 conv2025_A P1 15; 2 style guide «cantidad» (age; distractors 13/16 from art. 8.1
  RGPD); 3 style guide «plazo»; 4 conv2025_X sup. I reserva 4; 5 conv2025_X P1 17; 6 conv2024_X P1 16; 7 conv2025_X P1
  reserva 1; 8 conv2024_A sup. I 4; 9 conv2024_A P1 14; 10 conv2022_X P1 reserva 2.
- **Ambiguous or inconsistent texts (listed, not resolved):**
  - The RGPD file is the 2016 DOUE original without corrigenda. Art. 9.1 reads «las orientación sexuales» (the lesson
    writes «la orientación sexual»). Art. 36.1 reads «para para mitigarlo» (paraphrased). Art. 9.2.b) is missing an «o»,
    and art. 30.2.d) refers to «artículo 30, apartado 1» where art. 32.1 is meant (neither is used). The lesson's
    verbatim-dependent sentences are listed in the working ledger; a corrigendum check is an open item.
  - Art. 77.2 LOPDGDD excludes «la prevista en el artículo 58.2.i» RGPD. The lesson writes «sin la multa
    administrativa», reading the two norms together.
  - Art. 65.4 LOPDGDD makes inadmisión depend on the remission («como consecuencia de dichas actuaciones de remisión»).
    The lesson conveys this only by sentence order.
  - Art. 5.1.e) RGPD allows longer retention for archive, research or statistics. The lesson gives the label-level rule.
    Exceptions in arts. 17.3 and 34.3 RGPD are not stated; those sentences cite only the first apartado.
  - Art. 34.1 LOPDGDD has sixteen letters. The lesson names six and gives no count.
  - Art. 18.4 CE is named inside the paraphrase of art. 1.a) LOPDGDD with no CE Normativa line, as m01-l07 does with
    art. 105.b) CE.

## course.yaml

- Lesson summaries for m02-l01…m02-l04, three sentences each, from the writers' drafts. In m02-l04 the delegado clause
  now reads «obligatorio, entre otros casos, cuando el tratamiento lo lleva a cabo una autoridad u organismo público».
  The draft said «en las autoridades y organismos públicos», which drops the art. 37.1.a) exception for the courts.
- Module summary for m02, two sentences, following the m01 shape.

## Checks and suites (bloque II)

Run on the final tree (lessons, glossary, course.yaml, goldens and saved sources of this round):

- **Pipeline, course as draft:** loads and validates. `pytest -k "glossary or registry or content or pipeline"`: 68
  passed, including the never-coins checks for glossary and summaries. `figure steps per course`:
  `age-administrativo-c1: no figures`, `crypto-futures: 34 figures`, `fixture-oposiciones: no figures`.
- **List-shape guard** («no list marker in the middle of a sentence») and **cross-reference report**: pass for every
  lesson; 7 references, 0 dangling. **i18n**: the label-catalog and locale tests pass in the full frontend run, and
  the bundle export's label-catalog check is OK.
- **Goldens:** `glossary-links.es.txt` (70 web marks) and `lesson-refs.es.txt` (7 references) regenerated and read
  line by line (see Glossary). One wrong-sense link was excluded. No diff under `content/crypto-futures/` or `dist/`.
- **Android bundle:** re-exported, fingerprint unchanged `9c95cf4a6bf2…` (98 files); `--verify-only` OK, leaked
  tokens OK.
- **Backend (`uv run pytest`), final tree:** 1,374 passed, 20 skipped, 4 warnings (slowapi deprecation). Same counts
  as before the round.
- **Frontend (`npx vitest run`), final tree:** 563 passed, 49 skipped; `tsc -b` clean. Same counts as before the
  round.
- `README.md` (course status line) now says the theory of bloques I and II is written.

## Where to resume (after bloque II)

Bloque II is closed. The next session starts R2 bloque III (temas III.1–III.7, lessons `m03-l01`…`m03-l07`) with the
same spec, the standing conventions, and the outside-sources rule of this round.
