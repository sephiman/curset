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
- **RGPD corrigenda (bloque II).** *Closed in bloque III (fix b): the corrigenda are saved and m02-l04 re-checked.* `sources/normativa/` holds the 2016 DOUE original of the RGPD, without corrections.
  Before R3 writes II.4 questions, save the consolidated RGPD text, or its corrección de errores, under `sources/` and
  re-check the verbatim-dependent sentences of m02-l04 (art. 9.1 «orientación sexual», art. 36.1 among them).
- **Norms named but not in `sources/` (bloque II), candidates for `normativa.yaml` before R3 asks about them:** *Closed in bloque III (fix a): five saved and indexed; the PAE renaming norm does not exist, and m02-l03 now cites art. 13.1 Ley 14/2013.*
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

# Bloque III — temas III.1–III.7

Round R2, bloque III, 2026-10-16. Nothing committed. Same procedure as bloque II: one writer per tema to a shared spec
(the bloque II spec, the standing conventions and the outside-sources rule), then a separate blind reviewer that had
not written the lesson. The reviewer re-opened the cited article for every sentence carrying a number, plazo,
majority, organ, date, exception, condition or list, and checked the Normativa block and the glossary candidates.
Every FAIL was fixed against the article; the changed sentences then went through a second blind pass (III.1–III.3
together, III.4 alone) and a third pass (III.4–III.7 and the course.yaml summaries). Temas were written in order.
III.6 was drafted while III.5 was in review; no file overlapped. The per-sentence tables are working files, not kept
in the repo; their counts and every FAIL class are below.

Two additions for this bloque, from the round prompt: III.3 and III.4 use the 4,000-word limit and cover plazos,
recursos, silencio, cómputo de plazos (art. 30 LPAC) and the LCSP thresholds, procedures and contract types, because
part 2 is built on them; the other temas hold word targets proportional to exam weight. Before drafting III.3 and
III.4 the writer tallied every official question of 2022–2025 for the tema by article and allocated words by it.

## Fixes before III.1 (open items of bloque II)

### a. The six norms named in bloque II but missing from sources/

All six were downloaded from boe.es into `sources/normativa/` and indexed in `normativa.yaml` (placed after
RD 1112/2018, under a comment line):

| Norm | File | What it settles |
|---|---|---|
| RD 776/2011 | `BOE-A-2011-9736_rd-776-2011-organos-colegiados_2011-06-04.pdf` | Art. 1 and anexo suppress the Comisión Interministerial de Información Administrativa (arts. 11–12 RD 208/1996); DD única c) derogates art. 13. m02-l01 now cites «(art. 1 y anexo RD 776/2011)» instead of the BOE note, and Normativa lists it. |
| Decreto 914/1969 | `BOE-A-1969-643_decreto-914-1969-archivo-general_1969-05-26.pdf` | Confirms the m02-l02 sentence (number, date, transfers to the Archivo General). No lesson change. |
| RD 1401/2007 | `BOE-A-2007-19248_rd-1401-2007-comision-calificadora_2017-05-23.pdf` | Cited by no sentence. Contradicts neither m02-l02 sentence on the Comisión Superior Calificadora. Its art. 1.2 still adscribes it to the Ministerio de Cultura; art. 13.6 RD 1708/2011 adds the adscription to the Comisión de Archivos. Listed, not resolved. |
| RD 1164/2002 | `BOE-A-2002-22192_rd-1164-2002-eliminacion-documentos_2007-11-07.pdf` | Cited by no sentence; indexed for R3 (eliminación de documentos). |
| Acuerdo del Consejo de Ministros de 15-07-2005 | `BOE-A-2005-13337_acuerdo-cm-oficinas-integradas_2005-08-03.pdf` | Published as the anexo of the Resolución de 19-07-2005 (BOE núm. 184, 03-08-2005). Not in the consolidated collection; the file is the diario PDF of pp. 27269–27271, which carry other dispositions too. m02-l03 now cites the anexo beside the RD 127/2015 preámbulo. |
| Renaming of the PAE «al Emprendimiento» | **not found** | Ley 14/2013 art. 13 (Ley 18/2022 wording), Ley 18/2022 and Ley 28/2022 all say «Puntos de Atención al Emprendedor»; «Emprendimiento» is only the portal's label. Per the prompt, the citation now rests on the norm in force: m02-l03 adds «La ley los sigue llamando Puntos de Atención al Emprendedor (art. 13.1 Ley 14/2013…)». Ley 14/2013 is saved (`BOE-A-2013-10074_ley-14-2013-emprendedores_2025-04-09.pdf`) and indexed with this note. Its art. 13.3 also says «Centro de Información y Red de Creación de Empresas», the portal's form, against RD 127/2015's «Empresa». |

A blind check of the changed and affected sentences (9 items) passed.

### b. RGPD corrigenda

EUR-Lex refused automated download (HTTP 202 challenge), so the consolidated text could not be saved. The
Publications Office SPARQL lists three corrigenda; two have a Spanish version. Their official PDFs (cellar) are saved
in `sources/otros/` and indexed in `fuentes.yaml` with sha256: `doue-rgpd-correccion-2018.pdf` (DO L 127 de 23-05-2018,
CELEX 32016R0679R(02)) and `doue-rgpd-correccion-2021.pdf` (DO L 74 de 04-03-2021, R(03)). R(01) (DO L 314 de 2016)
has no Spanish version. The RGPD entry of `normativa.yaml` now points to both.

Re-check of m02-l04 against the corrected text: two FAILs, fixed. Art. 12.3 now reads «sin dilación indebida y, en
cualquier caso, en el plazo de un mes» (body and «Lo que más cae»); art. 37.1.c) now reads «categorías especiales de
datos **o** de datos personales relativos a condenas». Art. 9.1 («la orientación sexual») and art. 36.1 («para
mitigarlo») already matched the corrected text. The RGPD Normativa line names both corrigenda. A blind sweep of every
RGPD citation in m02-l04 and the glossary against the corrigenda passed (the only affected entry,
g-categorias-especiales-de-datos, matches).

## Summary

| Tema | Lesson | Target / ceiling | First draft | Words | Citations | Checked (pass 1) | FAIL (fixed) | Later passes | Glossary entries |
|---|---|---|---|---|---|---|---|---|---|
| III.1 | `m03-l01` | 2,000 / 2,400 | 3,162 | 2,285 | 49 | 74 | 4 | 5/5 PASS | 5 |
| III.2 | `m03-l02` | 2,500 / 2,900 | 3,467 | 2,676 | 60 | 100 | 5 | 6/6 PASS | 4 |
| III.3 | `m03-l03` | 4,000 cap | 8,210 | 3,979 | 107 | 164 | 31 | 28/28 PASS | 8 |
| III.4 | `m03-l04` | 4,000 cap | 6,945 | 3,991 | 104 | 147 | 24 | 55: 5 FAIL (fixed), then PASS | 11 |
| III.5 | `m03-l05` | 1,500 / 1,800 | 2,397 | 1,669 | 30 | 61 | 10 | 21/21 PASS | 2 |
| III.6 | `m03-l06` | 2,200 / 2,600 | 3,518 | 2,315 | 51 | 65 | 5 | 10/10 PASS | 1 |
| III.7 | `m03-l07` | 2,400 / 2,800 | 5,261 | 2,689 | 53 | 65 | 4 | 5/5 PASS | 8 |
| **Total** | | | | **19,604** | **454** | **676** | **83** | | **39** |

Words: `wc -w`, everything counted. Citations: «(art» / «(arts» only. III.1, III.2, III.5 and III.6 came out above
target but under the ceiling; III.5 stops at 1,669 because the next cuts were asked items. Most FAILs, in every tema,
are the same class: a condition, exception or «salvo / en su caso / siempre que» clause of the article dropped so the
sentence reads as a wider rule. The second class is a selective list that reads as complete.

## Glossary

- 39 entries added, origin in bloque III; `glossary.yaml` holds 157. Each cites its defining article. Pass 1 checked
  every candidate (III.1 5, III.2 4, III.3 8, III.4 12, III.5 3, III.6 2, III.7 9); 11 FAILs were replaced with the
  reviewer's article-faithful wording (circular definitions of declaración de lesividad and recusación, dropped
  conditions in potestad reglamentaria, órgano colegiado and recurso potestativo de reposición, wrong citations in
  decreto legislativo and costumbre, «vicio» in anulabilidad). Pass 3 re-checked the III.5–III.7 entries: 11/11 PASS.
- Not added: Plan Anual Normativo, convalidación (two senses), nulidad de pleno derecho and responsabilidad
  patrimonial (no defining article), actuaciones complementarias, medio propio personificado (cut from the lesson),
  comunicación (the bare word carries other senses in about a dozen lessons), acciones positivas (RDL 1/2013 art. 2.g)
  defines «medidas de acción positiva» differently, and m02-l01 uses it).
- **Never-coins:** «contrato menor», «contrato sujeto a regulación armonizada», «contrato de obras» and «contrato de
  suministro» appeared only in the plural, which the substring check does not accept. Two headings and two
  definition sentences of m03-l04 were put in the singular; no fact changed.
- **Goldens.** `glossary-links.es.txt` regenerated and read line by line: 70 → 121 web marks (40 also a PDF link).
  **Wrong-sense links excluded** (`link_except`): g-interesado in m01-l01 (audiencia del interesado, Defensor),
  m01-l08 (Ministro interesado), m01-l10 (Municipios interesados) and m02-l04 (the RGPD «interesado»); g-convenio in
  m01-l03 and m02-l04 (international convenios), m03-l04 (concursal convenio), m04-l08 and m05-l04 (IV Convenio
  único); g-organo-colegiado in m01-l03, m01-l05, m01-l09 and m03-l01 (colegiados outside the AGE, which art. 20.1
  LRJSP does not cover); g-servicios-comunes in m03-l04 (the Seguridad Social false friend). Kept after reading:
  «Real Decreto Legislativo 1/2013 / 3/2011» and «Ley Orgánica n/aaaa» (each names a real decreto legislativo or ley
  orgánica), g-interesado in the procedural sense (m02-l01–l03, m03-l02, m03-l05, m03-l06), g-convenio in m01-l07,
  m01-l08, m01-l09, m02-l01 and m02-l03 (administrative convenios).
- `lesson-refs.es.txt`: 7 → 21 references, 0 dangling. The writers had wrapped lesson ids in «» (the spec's example
  did); the renderer adds them, so the golden showed ««m03-l03»». The guillemets were removed from the m03 lessons.

## III.1 — `m03-l01`

- **Structure:** fuentes (art. 1 Código Civil; arts. 9.3, 103.1 CE), jerarquía (arts. 1.2 CC, 128.3 LPAC, 24.2 Ley
  50/1997, 149.3 CE), ley (arts. 81.2 CE, 131 LPAC, 2 CC), decreto legislativo and decreto-ley (arts. 82–83, 85–86
  CE), reglamento: concepto (art. 97 CE, 128.1 and 129.4 LPAC), clases (only the forms of art. 24.1 Ley 50/1997 and
  art. 22.3 LO 3/1980), límites (arts. 128.2, 47.2, 37.1 LPAC), elaboración (arts. 129.1 LPAC, 25–26 Ley 50/1997),
  otras fuentes (art. 1.3–1.6 CC). Cross-references to m01-l03 and m01-l06.
- **FAILs fixed (4):** art. 128.1 LPAC conditions (Estatutos; Constitución, Estatutos and LBRL); the STC 55/2018
  sentence (now general, pointing to the notes, which carry the exceptions of arts. 129.4 and 133); art. 26.6 Ley
  50/1997 (tramitación urgente as a second ground); «Lo que más cae» art. 128.2 (truncated list and dropped «sin
  perjuicio» clause).
- **«hoy» note:** Ministro de la Presidencia (art. 24.1.e) Ley 50/1997) → Ministro de la Presidencia, Justicia y
  Relaciones con las Cortes (art. 3.1 RD 829/2023, asistencia a las Comisiones Delegadas).
- **normativa.yaml:** the LPAC entry now records STC 55/2018 (arts. 129, 130, 132, 133 and the void incisos of art.
  129.4); LO 3/1980 temas + III.1.
- **Glossary (5):** decreto-ley, decreto legislativo, potestad reglamentaria, costumbre, jurisprudencia.
- **Lo que más cae sources:** 1 conv2025_A P1 16; 2 conv2022 P1 19; 3 conv2024_X P1 17, conv2022_X P1 8; 4
  conv2022_X P1 8; 5 conv2022 P1 37; 6 conv2025_X P1 reserva 4; 7 style «plazo»; 8 conv2024_A P1 17 (ledger III.2),
  style «texto alterado»; 9 and 10 style «texto alterado».
- **Not in the sources, left out:** a classification of reglamentos; the rank of ley orgánica against ley ordinaria
  (conv2022 P1 37 option b); primacy of EU law. Ley 50/1997 art. 26 is quoted as the file prints it (LO 1/2025
  wording).

## III.2 — `m03-l02`

- **Structure:** concepto (the LPAC defines no acto administrativo; título III, arts. 34–52), clases (only categories
  an LPAC article names, each with it: arts. 47.1.f, 24.4, 112.1, 113–114, 39.3, 109.1), elementos (heading over arts.
  34–36; the expression is not in the LPAC), eficacia (37–39, 98.1), validez (47–52), motivación (35), notificación
  (40–46). Cross-references to m03-l01, m03-l03 and m02-l03.
- **FAILs fixed (5):** art. 109.1 conditions on revocación; art. 98.1 uncited; art. 35.2 mandatory clause; art. 40.2
  «en su caso» and «sin perjuicio»; «Lo que más cae» art. 42 (who may take a paper notification). Voice: repeated
  «La LPAC no / habla de» openers and «Uno de ellos es» rewritten.
- **normativa.yaml:** LJCA temas + III.2 (art. 70.2).
- **Glossary (4):** anulabilidad, desviación de poder (art. 70.2 LJCA), inderogabilidad singular, comparecencia en
  la sede electrónica.
- **Lo que más cae sources:** 1 conv2025_A P1 17, conv2022_X P1 14; 2 conv2024_A P1 17; 3 conv2022 P1 4, conv2025_A P1
  reserva 4, conv2020_X sup. I 4; 4 conv2024_A P1 reserva 2, conv2025_X sup. I reserva 2; 5 conv2022 sup. I 2; 6
  conv2022 P1 20; 7 conv2020 P1 16; 8 conv2025_X P1 20; 9 conv2024_A sup. II 6; 10 conv2022_X P1 5, conv2020_X sup.
  II reserva 4.
- **Left out:** «actos consentidos» (only art. 28 LJCA uses it).

## III.3 — `m03-l03`

- **Tally** (70 rows of 2022–2025, 2 anuladas; modelo B not counted twice): alzada (121–122) 7; art. 114 5; reposición
  (123–124) 5; abstención y recusación (23–24 LRJSP) 5; convenios (47–53 LRJSP) 5; art. 21 4; art. 30 4; silencio (24,
  91.3) 3; art. 68 3; art. 82 3; art. 87 / 22.2.b) 3; lesividad (107) 3; delegación (9 LRJSP) 3; órganos colegiados (17,
  20 LRJSP) 3. No question asks the LJCA beyond art. 46.
- **Structure:** the two laws (interesados and representación, arts. 4.1, 5.6 LPAC; competencia, delegación,
  órganos colegiados, abstención y recusación, convenios, arts. 8–9, 17, 20.1, 23–24, 47.1, 49.h) LRJSP); cómputo de
  plazos in full (arts. 30–33 LPAC, three worked date examples, each recomputed with `cal`); plazo máximo (21–23);
  silencio (24–25); iniciación, ordenación, instrucción, terminación (56.2, 58, 68, 74, 76.1, 77.2, 80, 82–84, 87,
  94–96); revisión de oficio (106–111) and recursos (112, 114–115, 118, 121–126); recurso contencioso-administrativo,
  actividad impugnable and partes (arts. 6, 18, 19.1, 23.1–2, 25, 29.1, 30, 46.1 LJCA; DA 1.ª LO 1/2025).
- **FAILs fixed (31):** dropped conditions or exceptions in arts. 4.1, 5.6, 21.1, 21.3, 24.1 (twice, including the
  condition at the end of its third paragraph on alzada against desestimación presunta), 30.1, 30.2, 31.2.b), 32.1,
  68.1, 68.2, 84.1, 94.4, 95.1, 106.1, 114.2, 121.1, 122.2 LPAC; 23.2.a)–b), 24.1, 47.1, 53.1 LRJSP; 19.1, 29.1, 30, 46.4
  LJCA; DA 1.ª LO 1/2025; «Lo que más cae» reposición («si el acto es expreso»). Three sentences were removed rather
  than fixed (5.3 LPAC, 53.1 LRJSP, 46.4 LJCA). To stay under 4,000, whole low-yield items were cut (4.1 a/c, 5.3,
  63.1, 66.1, 73.1, 85, 88.1 LPAC; 14.2, 53.1 LRJSP; 19.2, 23.3, 28, 46.4 LJCA; one worked example); the cómputo,
  silencio, recursos and revisión material was not cut.
- **Glossary (8):** interesado, convenio, órgano colegiado, recurso de alzada, recurso potestativo de reposición,
  recurso extraordinario de revisión, declaración de lesividad, recusación.
- **Lo que más cae sources:** 1 conv2022_X sup. I 3, conv2024_X sup. II 15, conv2024_A sup. I reserva 4; 2 conv2025_A
  sup. II 19, conv2024_A sup. II reserva 2, conv2022 sup. II 13–14; 3 conv2025_A P1 18, conv2024_A sup. II reserva 2; 4
  conv2024_X sup. II 15; 5 conv2025_A sup. I 1–2, conv2022_X sup. I 1; 6 conv2025_A sup. I 4, conv2022_X sup. I 2; 7
  conv2022 sup. I 3; 8 conv2025_A P1 19, conv2022 sup. I 15; 9 conv2025_X sup. I 17, conv2022_X sup. I reserva 3; 10
  conv2024_X P1 18, conv2025_A sup. I 3.
- **Listed, not resolved:** conv2025_X sup. I reserva 3 keys «el máximo órgano rector del INE»; art. 111.c) LPAC
  makes the answer depend on the INE statute, which is not in sources/. LO 1/2025 DA 1.ª redirects the Juzgados de lo
  Contencioso-Administrativo to Secciones of the Tribunales de Instancia «una vez constituidos e implantados de forma
  efectiva»; the lesson gives no implantation dates.

## III.4 — `m03-l04`

- **Tally** (65 questions 2022–2025): art. 159 10; 106–108 6; 118 5; 12–18 4; 44–50 4; 19–22 3; 101 3; 29 3; 204–206
  and 242.4 3; 219/221/223 3; 235/238/244 3; 145, 153, 193, 198 2 each.
- **Thresholds.** The consolidated LCSP file prints 5.404.000 / 216.000 / 140.000 euros with no note. They were set by
  the Orden HAC/1517/2025, de 18 de diciembre (BOE-A-2025-26605, BOE 26-12-2025), artículo único, from 01-01-2026,
  applying Reglamentos Delegados (UE) 2025/2150–2152 and 2025/2487 under DA undécima LCSP; 750.000 (art. 22.1.c) is
  unchanged. Saved as `BOE-A-2025-26605_orden-hac-1517-2025-umbrales_2025-12-26.pdf` (diario PDF; boe.es has no
  consolidated PDF) and indexed after the LCSP; the reviewer matched title, date, pages and sha256. No source in the
  repo states an end date; the lesson says «desde el 1 de enero de 2026».
- **Structure:** concepto y clases (arts. 2, 12–18, 25–26), regulación armonizada (19–22 with the Orden), preparación
  (órgano, duración 29, pliegos, presupuesto base de licitación and valor estimado 100–102, contrato menor 118,
  urgencia y emergencia 119–120, garantías 106–108), adjudicación (abierto 156–158, simplificado and 159.6,
  restringido 160–162 and 164, licitación con negociación 167 and 169, negociado sin publicidad 168, diálogo
  competitivo 172, mesa 326, adjudicación y formalización 150 and 153, acuerdos marco 219 and 221), efectos y
  extinción (193, 198, 210–211, 213, 235, 238, 243–244), revisión de precios and modificación (103, 204–206), cesión y
  subcontratación (214–215), invalidez and recurso especial (39–40, 44–45, 50, 53).
- **Procedures restored at the owner's request.** The first draft had cut the restringido plazos and the
  negotiated procedures for length. The fix round put back arts. 161, 162, 164, 167, 168 (compact) and 169, and cut
  instead aptitud (65–66), prerrogativas (190–191), 131.2, 146.1, cesión letters a), c), d), 223.2, 229.5, 323.2, 62,
  116.1, 99.1, 326.3, 326.6, 159.4.b), 150.2 (retirada), 196, 210.3, 203.1–2, most of 211.1, 49.1, 177.1 and the DA
  undécima sentence. Several of these were each asked once (62, 66, 65.1, 99.1, 196, 223.2, 229.5).
- **FAILs fixed:** pass 1, 24 (16.3 syntax, 18.1.a), 19.1/19.2 exclusions, 107.1 «Administraciones Públicas», 108.2,
  156.3, 158.3, 159.6 selective list, 168 conditions, 326.1 mesa potestativa, 193.3, 244.1, 205.2.a), 214.2.b), 44.1,
  50.2, and seven «Lo que más cae» lines, two of them deleted, leaving 8). Pass 2 found 5 new defects in the
  rewrites (108.2 contract types, 167.f arraigo, 169.2 «puede», 168.a scope and wording, 50.2 start of the plazo);
  fixed with the reviewer's wording, then PASS in pass 3.
- **Ministry name:** «Ministerio de Hacienda y Función Pública» (arts. 45.1, 323.3…) is omitted, not given a «hoy»:
  art. 5 RD 829/2023 does not name contratación and the TACRC's present adscription is in no source file.
- **Glossary (11):** contrato menor, presupuesto base de licitación, valor estimado (101.1.a and b), contrato sujeto a
  regulación armonizada, contrato de obras, de suministro, de servicios, concesión de servicios, contrato mixto,
  acuerdo marco, mesa de contratación.
- **Lo que más cae sources:** 1 conv2022_X P1 23, conv2025_X sup. I 2 and sup. II 13; 2 conv2024_A sup. II 14,
  conv2025_A sup. II 1, conv2022_X sup. II 17; 3 conv2025_A sup. I 10, conv2024_X sup. II 6; 4 conv2025_A sup. II 2,
  conv2024_A sup. II 19, conv2022_X P1 32; 5 conv2024_X sup. II 3, conv2025_A sup. I 7; 6 conv2024_A sup. II 9,
  conv2022_X sup. I reserva 5; 7 conv2025_A sup. II 5 and 9, conv2022 sup. I 13; 8 conv2024_A sup. II 16, conv2022_X
  sup. II reserva 3.
- **For the exams ledger (R3):** conv2024_A sup. II 14 and every official question resting on the 2024–2025
  thresholds (5.538.000 / 221.000 / 143.000) now has a different figure in force; they need «norma modificada»
  review. conv2024_X sup. II 4: the official key is 22 March, and twenty days from 2 March 2024 give 21 March.

## III.5 — `m03-l05`

- **Structure:** the four «actividad de …» labels are the programme's headings only (no cited text uses them; the
  lesson says so). Limitación: art. 4.1 LRJSP, art. 69 LPAC, potestad sancionadora (arts. 25.1, 27.1, 29.3 LRJSP; 63.1,
  85 LPAC). Arbitral: art. 112.2 LPAC, art. 2.1 Ley 60/2003. Servicio público and formas de gestión: arts. 85–86.2
  LBRL, art. 284.1 LCSP. Fomento: art. 2 LGS. Cross-references to m03-l03 and m03-l04.
- **FAILs fixed (10):** arts. 25.1 (procedure; título XI LBRL) and 27.1 LRJSP; 85.2, 85.3 and 112.2 LPAC; 86.2 LBRL;
  2.1.b) LGS; three «Lo que más cae» lines. The fix round cut 29.1, 30.1, 31.1 LRJSP, 1.4 Ley 60/2003, 7.3 LGP, 15.2,
  32.1 and 284.2 LCSP, the art. 2.4.j) LGS sentence and two «Lo que más cae» lines (8 remain).
- **normativa.yaml:** LBRL temas + III.5. The Normativa LBRL line says «(sin cambios por la Ley 4/2026)»: Ley 4/2026
  touches only arts. 25.2 and 69.1.
- **Glossary (2):** declaración responsable, subvención.
- **Lo que más cae sources:** 1 conv2024_A P1 23 (anulada; the only III.5 question); 2 conv2024_A P1 24 («III.3 (o
  III.5)»); 3 conv2025_A P1 21 («V.6 (o III.5)»); 4–8 style categories «texto alterado», «otra figura del mismo tipo»
  and «cantidad».
- **Listed:** art. 85.2.B LBRL still refers to the contrato de gestión de servicios públicos of RDL 3/2011, repealed
  by the LCSP; quoted as written, with the repeal cited to the LCSP derogatoria.

## III.6 — `m03-l06`

- **Tally** (27 questions, 2020–2025): art. 67 LPAC 6; 81 6; 91.3 4; 114.1.e) 4; 32.8, 32.1–2 and 34.3 LRJSP 2 each.
  Words: about 45 % procedure, 25 % requisitos, 25 % supuestos.
- **FAILs fixed (5):** the «hoy» note on «Ministerio de Justicia» (art. 32.8 LRJSP) removed, because art. 3 RD 829/2023
  does not clearly cover the TC indemnizaciones; the clases list now says «algunos de los supuestos»; art. 67.1 LPAC
  gains its two other starting dates; art. 82.1 condition placed on the dictamen; «Lo que más cae» 67.1 with its start.
- **normativa.yaml:** the LO 3/1980 note wrongly put the 50.000 euros in the LO; it is in art. 81.2 LPAC (art. 22.13
  LO 3/1980 says «en los supuestos establecidos por las leyes»). Corrected.
- **Glossary (1):** Consejo de Estado (art. 107 CE; art. 1.1 LO 3/1980). Responsabilidad patrimonial not added (no
  defining article).
- **Lo que más cae sources:** 1 conv2022 sup. II 12, conv2020 sup. I 4, conv2020_X sup. I reserva 3; 2 conv2022_X sup.
  I 12; 3 conv2025_X sup. II reserva 1, conv2022 P1 38; 4 conv2025_X sup. II reserva 2, conv2024_X sup. I 12; 5 conv2022
  sup. II 13, conv2022_X sup. I 13; 6 conv2024_X sup. I 9; 7 conv2025_X sup. II reserva 3, conv2024_X sup. I 10; 8
  conv2025_A P1 22, conv2025_X P1 24; 9 conv2024_X P1 21; 10 conv2020_X P1 25 and style «otra figura del mismo tipo».
- **Listed:** art. 32.9 LRJSP still refers to the 2011 texto refundido de contratos; quoted as written.

## III.7 — `m03-l07`

- **Tally** (2020–2025): LO 3/2007 5 (arts. 64, 49, DA 1.ª, 76, 7.2); Ley 4/2023 2 (5.2, 1.3); Ley 15/2022 1 (9.4); RDL
  1/2013 1 (2.i); LO 1/2004 and Ley 39/2006 none. Rows «II.1 (o III.7)» are RD 366/2007 and stay in m02-l01.
- **Cambio pendiente:** every sentence on an article Ley 4/2026 amends carries «(desde 23-10-2026)» (art. 2.m) RDL
  1/2013; arts. 2.2, 26.1, 28.1–2 Ley 39/2006); arts. 2.i), 42 RDL 1/2013 and 1.1, DA 17.ª Ley 39/2006 are not amended
  and carry none. The reviewer checked each against the text of Ley 4/2026.
- **FAILs fixed (4):** the Observatorio sentence cited only RD 829/2023 (now art. 30.1 LO 1/2004, with the «hoy» inside
  the parenthesis); art. 42.1 RDL 1/2013 (negociación colectiva sectorial); the Grado III+ of DA 17.ª Ley 39/2006 (from
  RDL 11/2025) added after the three grados of art. 26.1; «Lo que más cae» art. 24 LO 1/2004 («en los términos que se
  determinen en su legislación específica»).
- **«hoy» note:** Ministerio de Trabajo y Asuntos Sociales → Ministerio de Igualdad (art. 20 RD 829/2023), at art.
  30.1 LO 1/2004. Not given (no clear match): arts. 63 and 46.4 LO 3/2007.
- **Glossary (8):** discriminación directa / indirecta por razón de sexo, acoso sexual, acoso por razón de sexo,
  composición equilibrada, situación de dependencia (desde 23-10-2026), persona trans, normalización.
- **Lo que más cae sources:** 1 conv2025_X P1 25; 2 conv2022 P1 5; 3 conv2025_A sup. II 17; 4 conv2020 P1 23; 5 conv2020
  P1 22; 6 style «otra figura del mismo tipo»; 7 conv2025_A P1 23; 8 conv2024_A P1 25; 9 conv2024_X P1 22; 10 conv2024_X
  P1 reserva 2.
- **Listed:** DF 1.ª Ley 39/2006 still describes «niveles» inside the grados; art. 26 has none.

## course.yaml

- Lesson summaries m03-l01…m03-l07, three sentences each, from the writers' drafts. Pass 3 checked all 21 sentences:
  6 FAIL, all fixed with the reviewer's wording (subject-matter limits of arts. 82.1 and 86.1 CE; the art. 106.1
  condition and the lesividad four-year limit; the poder-adjudicador condition and the Orden as source of the
  thresholds; art. 2.1.b) LGS; the start of the six months of art. 91.3; «de nacionalidad española», art. 43.1 Ley
  4/2023).
- Module summary for m03, two sentences, in the m01/m02 shape.

## Checks and suites (bloque III)

Run on the final tree (lessons, glossary, course.yaml, goldens, normativa.yaml, fuentes.yaml and saved sources of this
round):

- **Pipeline, course as draft:** loads and validates. `pytest -k "glossary or registry or content or pipeline"`: 68
  passed, including the never-coins checks for glossary and summaries (it first failed on four plural-only contract
  terms; see Glossary). `figure steps per course`: `age-administrativo-c1: no figures`, `crypto-futures: 34
  figures`, `fixture-oposiciones: no figures`.
- **Backend (`uv run pytest`), final tree:** 1,374 passed, 20 skipped, 4 warnings. Same counts as before the round.
- **Frontend (`npx vitest run`), final tree:** 563 passed, 49 skipped; `tsc -b` clean. Same counts as before the round.
- **Goldens:** `glossary-links.es.txt` (121 web marks) and `lesson-refs.es.txt` (21 references, 0 dangling)
  regenerated and read line by line (see Glossary). No diff under `content/crypto-futures/` or `dist/`.
- **Android bundle:** re-exported, fingerprint unchanged `9c95cf4a6bf2…` (98 files); `--verify-only` OK, leaked tokens
  OK.
- `README.md` (course status line) now says the theory of bloques I, II and III is written.

## Open items (after bloque III)

- **After the 29-11-2026 elections:** the «hoy» re-check round now also covers m03-l01 (Ministerio de la Presidencia,
  Justicia y Relaciones con las Cortes) and m03-l07 (Ministerio de Igualdad).
- **Exams ledger, thresholds:** official questions resting on the 2024–2025 LCSP thresholds (5.538.000 / 221.000 /
  143.000; e.g. conv2024_A sup. II 14) need «norma modificada» review against the Orden HAC/1517/2025 before they enter
  the «Exámenes oficiales» set. conv2024_X sup. II 4: official key 22 March, computed 21 March; check before R3.
- **LCSP thresholds after 2027:** no source in the repo gives an end date for the Orden HAC/1517/2025 figures. If a
  new orden is published before the exam, m03-l04, its glossary entry and the course.yaml summary change.
- **INE statute** (conv2025_X sup. I reserva 3, art. 111.c) LPAC) is not in sources/; needed before R3 asks it. *Closed
  in bloque IV (fix before IV.1): RD 803/2022 saved and indexed; the official key is d), not «el máximo órgano rector».*
- **Glossary candidates waiting:** Plan Anual Normativo, actuaciones complementarias, medio propio personificado,
  nulidad de pleno derecho, responsabilidad patrimonial, comunicación (with a `link_except` plan), acciones positivas
  (scoped to LO 3/2007). Plus the six bloque I terms and «oficinas integradas», still waiting.
- **Formatting:** a few lines of m03-l01, m03-l02 and m03-l04 run past the usual wrap width; cosmetic only.

## Where to resume (after bloque III)

Bloque III is closed. The next session starts R2 bloque IV (temas IV.1–IV.9, lessons `m04-l01`…`m04-l09`) with the
same spec, the standing conventions and the outside-sources rule. The writer spec of this round adds one rule: lesson
ids in cross-references are written bare (m03-l03), never in «».

# Bloque IV — temas IV.1–IV.9

Round R2, bloque IV, 2026-10-16. Nothing committed. Same procedure as bloque III: one writer per tema to a shared spec
(the bloque III spec, the standing conventions, the outside-sources rule, and two additions from the round prompt:
where the TREBEP and the pre-TREBEP rules still in force differ, the lesson says which applies to AGE funcionarios and
cites both; IV.4, IV.5 and IV.6 use the 4,000-word limit and state every situación, permiso, plazo de reingreso, falta,
sanción and prescription period). A separate blind reviewer re-opened the cited article for every sentence and table
cell carrying a number, plazo, majority, organ, date, exception, condition or list, recomputed every worked date, and
checked Normativa, the glossary candidates and the course.yaml summary. Every FAIL was fixed against the article; the
changed sentences went through a second blind pass, and a third where the second found FAILs. Temas ran in order; the
writer of tema N+1 drafted while tema N was in review, against a scope table that assigned each article to one lesson.
The per-sentence tables are working files, not kept in the repo.

Suites before writing (tree at the start of the session): frontend `npx vitest run` 561 passed, 2 failed, 49 skipped —
the two failures are the glossary-link and lesson-reference goldens, which moved because m04-l01 was being written
while the run went on; the backend run was cut by the `timeout` before its summary line.

## Fix before IV.1 (open item of bloque III): the INE statute

- The statute in force is the **Real Decreto 803/2022, de 4 de octubre**, por el que se aprueba el Estatuto del
  Organismo Autónomo Instituto Nacional de Estadística (BOE-A-2022-16198, consolidated 31-10-2025, amended by RD 965/2025).
  It repealed the RD 508/2001 (BOE-A-2001-9097) on 05-10-2022. Saved as
  `sources/normativa/BOE-A-2022-16198_rd-803-2022-estatuto-ine_2025-10-31.pdf` (sha256 `dd372063…de4584`) and indexed in
  `normativa.yaml` (temas III.3) under a comment line before bloque IV.
- What it settles: the INE is an organismo autónomo adscrito al Ministerio de Economía, Comercio y Empresa a través de la
  Secretaría de Estado de Economía y Apoyo a la Empresa (art. 1.1); its órganos de gobierno are the Presidencia and the
  Consejo de Dirección (art. 3); art. 16 governs recursos against acts of the Presidencia. With art. 111.c).1.º LPAC, the
  revisión de oficio of the Presidencia's acts belongs to the órgano de adscripción.
- **Correction to the bloque III ledger.** conv2025_X sup. I reserva 3 keys **d)** (the Secretaría de Estado through
  which the INE is adscrito) on the definitive answer sheet, not «el máximo órgano rector del INE» (option c), as the
  III.3 entry said. Key d) is consistent with the statute and art. 111.c).1.º. The statute does not use the expression
  «máximo órgano rector». m03-l03 cites no INE fact, so no lesson changes.

## Summary

| Tema | Lesson | Target / ceiling | First draft | Words | Citations | Checked (pass 1) | FAIL (fixed) | Later passes | Glossary |
|---|---|---|---|---|---|---|---|---|---|
| IV.1 | `m04-l01` | 2,200 / 2,600 | 4,728 | 2,584 | 42 | 86 + LQMC + summary | 6 + 1 + 1 | p2 14: 1 FAIL; p3 5/5 | 5 |
| IV.2 | `m04-l02` | 2,200 / 2,600 | 4,354 | 2,588 | 49 | 72 | 2 (glossary 1) | p2 6/6 | 3 |
| IV.3 | `m04-l03` | 2,200 / 2,600 | 3,863 | 2,595 | 37 | 76 | 4 + summary 1 | p2 21: 3 FAIL; p3 6/6 | 5 |
| IV.4 | `m04-l04` | 4,000 cap | 6,794 | 3,995 | 89 | 148 | 4 + summary 1 | p2 20: 4 FAIL; p3 coordinator | 4 |
| IV.5 | `m04-l05` | 4,000 cap | 6,614 | 3,998 | 55 | 131 | 12 (glossary 2, summary 1) | p2 82: 13 FAIL; p3 34: 5 FAIL, applied | 8 |
| IV.6 | `m04-l06` | 4,000 cap | ≈5,000 | 3,990 | 63 | 152 | 11 (glossary 1, summary 1) | p2 23 rows + 8 cuts: 1 FAIL, applied | 6 |
| IV.7 | `m04-l07` | 2,000 / 2,400 | 3,860 | 2,382 | 52 | 92 | 6 | p2 18/18; 1 FAIL in an untouched sentence + glossary 2, applied | 3 |
| IV.8 | `m04-l08` | 2,800 / 3,200 | 4,563 | 3,171 | 69 | 115 | 4 + Normativa 1 + summary 1 | coordinator against the text | 3 |
| IV.9 | `m04-l09` | 1,800 / 2,400 | ≈3,900 | 2,398 | 48 | 74 | 11 (glossary 1, summary 2) | p2 24: 2 FAIL + glossary 1, applied | 2 |
| **Total** | | | | **27,701** | **504** | **946** | **60 lesson** | | **39** |

Words: `wc -w`, everything counted. Citations: «(art» / «(arts» only; table cells that cite «art. N norma» without a
parenthesis (IV.4, IV.5, IV.6) are not counted. «p2/p3»: second and third blind passes on the changed sentences.
«applied» / «coordinator»: the last replacements were the reviewer's own article wording, applied by the coordinator
and checked by diff against the article text; no further blind pass ran on them (IV.4 p3, IV.5 p3, IV.6, IV.7, IV.8,
IV.9). IV.8 had no separate second pass: the coordinator checked the six fixes against the Convenio and TREBEP text
and corrected one word («del Convenio» → «de este Convenio», art. 3.1).

**IV.9 ceiling.** Raised by the coordinator from 2,200 to 2,400 (IV.7's) so the 11 first-pass fixes needed no cuts of
asked items. IV.7 and IV.9 have about the same exam weight.

**FAIL classes.** As in bloques I–III, most FAILs were a dropped condition, exception or «salvo / sin perjuicio» clause
of the article, and the second class a selective list that read as complete. Bloque IV adds two:
1. **Quoting the TREBEP disposición derogatoria única without its opening paragraph** («con el alcance establecido en el
   apartado 2 de la disposición final cuarta»), so that a letter b) or f) reads as an unqualified repeal (IV.1, IV.2,
   IV.3, IV.4, IV.6).
2. **Cut-induced FAILs.** Cutting to the ceiling removed a clause of a kept sentence (IV.5 arts. 48.2, 54.1, 70.2; IV.7
   art. 21.1.c). From IV.5 on, the rule was «cut whole facts only, never a clause of a kept sentence».

**Coordinator restorations.** Three times a writer's cuts removed required content, and the coordinator had it put
back: IV.5 (the permisos of art. 48 d), f), i), j) and art. 49 b), g), cut to fit; then arts. 14 and 52 TREBEP, the
whole «derechos» and the general deber), IV.6 (arts. 41–43 RD 33/1986, the vista, propuesta and alegaciones plazos),
IV.7 (asistencia sanitaria, arts. 15.1 and 17.1 RDL 4/2000). In IV.5 the art. 14 list was then shortened to the letters
any 2020–2025 question asks or uses as a distractor plus those with a condition clause, introduced as «Entre los
derechos individuales del artículo 14 están estos».

## Which rule applies (TREBEP and the pre-TREBEP texts)

No text in `sources/` says, article by article, whether a provision of Ley 30/1984, RD 364/1995, RD 365/1995 or
RD 33/1986 «se opone» to the TREBEP. The lessons therefore quote the texts that govern the question and state both
rules where they differ, each cited; no lesson picks a winner the texts do not name. The texts quoted are: the
disposición derogatoria única TREBEP (opening paragraph, b) and f)), its disposición final cuarta (apartado 1, with the
párrafo on compatibilidades, and apartado 2), the BOE notes on each Ley 30/1984 article kept «en tanto no se oponga…
hasta que se dicten las Leyes de Función Pública», the scope of the RDL 6/2023 (art. 105.5 and DF 7.ª.2: libro segundo
applies to the Administración del Estado «como norma de desarrollo» of the TREBEP) and its disposición derogatoria. The
one case a text settles is the personal eventual in servicios especiales (art. 87.1.i) TREBEP against arts. 3.d) and
4.i) RD 365/1995); the lesson states both rules side by side after the second pass removed an inferred «rige el
TREBEP».

Differences recorded in the lessons, both rules cited:

- **IV.1:** who sets the number of eventual posts and appoints (art. 12.2 TREBEP / art. 20.2 Ley 30/1984).
- **IV.2:** the discapacidad reserve: 7 % (art. 59.1 TREBEP), 10 % in the Administración del Estado (art. 108.4
  RDL 6/2023), 5 % (art. 2.1 RD 2271/2004 and DA 19.ª Ley 30/1984, which is not in the DD única b) list); plazos of the
  convocatoria (art. 70.1 TREBEP / art. 108.2 RDL 6/2023); exclusions from órganos de selección (art. 60.2 TREBEP /
  art. 115.2 RDL 6/2023).
- **IV.3:** concurso as sistema selectivo (art. 4.1 RD 364/1995, no ley required / arts. 61.6 TREBEP and 114.6
  RDL 6/2023, «sólo en virtud de ley»); aprobados above plazas (art. 25.1 RD 364/1995 / arts. 61.8 TREBEP and 114.10
  RDL 6/2023).
- **IV.4:** minimum stay in excedencia voluntaria por interés particular (none in art. 89.2 TREBEP; two years in
  art. 29.3.c) Ley 30/1984; art. 16.3 RD 365/1995); the loss of the condition for not asking reingreso (art. 16.4
  RD 365/1995, a cause absent from art. 63 TREBEP); agrupación familiar (requisites of art. 89.3 TREBEP, duration of
  art. 17 RD 365/1995); cuidado de familiares (reserva «al menos dos años», art. 89.4 TREBEP, against the whole period and
  the one-parent rule, art. 14 RD 365/1995); prolongation of service to seventy (art. 67.3 TREBEP / art. 33 Ley
  30/1984); cómputo in servicios especiales (art. 87.2 TREBEP / art. 8.2 RD 365/1995).
- **IV.5:** DF 4.ª.1 TREBEP defers carrera, promoción interna and provisión (arts. 16–20, 78–84) to the leyes de Función
  Pública; no text says whether RDL 6/2023 libro segundo is that law for the AGE. Promoción interna, two years «de
  servicio activo en el inferior Subgrupo» (art. 18.2 TREBEP) / «en el Cuerpo o Escala» (art. 76 RD 364/1995);
  intervalos de niveles (DT 6.ª RDL 6/2023 / art. 71.1 RD 364/1995); movilidad por violencia de género (art. 82.1 TREBEP,
  also sexual, no vacancy needed / art. 66 ter RD 364/1995).
- **IV.6:** prescription of faltas (3 años / 2 años / 6 meses, art. 97 TREBEP / 6 años / 2 años / 1 mes, art. 20
  RD 33/1986) and of sanciones (3 / 2 / 1 año / 6 años / 2 años / 1 mes, art. 21 RD 33/1986), start dates and
  interruption (only art. 20.2 RD 33/1986 regulates it); faltas graves and leves reserved to ley (arts. 95.3–4 TREBEP)
  while the only lists in force are arts. 7–8 RD 33/1986; pay of the suspenso provisional (art. 98.3 TREBEP / art. 21.4
  RD 365/1995); compatibilidades «continuará rigiéndose por la actual normativa» (DF 4.ª.1 párr. 2 TREBEP).

## Saved sources (bloque IV)

All indexed in `normativa.yaml`; each was verified independently by the tema's reviewer (fresh download from boe.es,
same sha256, same text, metadata and /analisis read):

| Norm | File | Why |
|---|---|---|
| RD 803/2022 (Estatuto del INE) | `BOE-A-2022-16198_rd-803-2022-estatuto-ine_2025-10-31.pdf` | Fix before IV.1 (above) |
| RD 2073/1999 (Registro Central de Personal) | `BOE-A-2000-1007_rd-2073-1999-registro-central-personal_2000-01-18.pdf` | Its DD única repeals capítulo I of the RD 1405/1986 Reglamento except arts. 2, 3 and 4.1; the RCP plazos, asientos and anotaciones the exams ask are in it. The RD 1405/1986 entry now says so. |
| Resolución de 14-04-2026, SEFP, jornada y horarios en la AGE | `BOE-A-2026-8287_res-14-04-2026-jornada-horarios-age_2026-04-15.pdf` | Applies from 16-04-2026 and repeals the Resolución de 28-02-2019 (BOE-A-2019-2861), the one in force at the 2022–2025 exams, not saved. Apartado 14.3 (permisos in days are naturales unless the norm says hábiles), 9.7 and 9.10. |
| RD 577/1997 (Estatuto de MUFACE) | `BOE-A-1997-9874_rd-577-1997-estatuto-muface_2026-06-12.pdf` | Órganos de gobierno and the Consejo General's composition; adscription through the SEFP. RD 466/2026 (BOE-A-2026-12711, verified on boe.es, not saved) renamed it «Mutualidad General de Funcionarias y Funcionarios Civiles del Estado, O.A.»; the lesson rests on the saved consolidated text. |

`normativa.yaml` also: IV.1 added to the temas of RDL 6/2023, RD 829/2023 and RD 1009/2023; IV.3 to RDL 6/2023; IV.5 to
LO 3/2007.

## Glossary

- 39 entries added, origin in bloque IV; `glossary.yaml` holds 196. Each cites its defining article, which its origin
  lesson cites. «libre designación», waiting since bloque I, entered with IV.5.
- Withdrawn by writers after cuts left the singular absent from prose, or the defining article uncited: carrera
  profesional (IV.5), haber regulador (IV.7), incapacidad permanente (IV.9). Dropped by the coordinator: especialidad
  (IV.8; the bare word carries other senses in many lessons).
- Not proposed: personal directivo (art. 13.1 TREBEP defines it by reference), concurso (provisión and selection
  senses), incapacidad temporal in the RDL 4/2000 sense (the entry is defined by art. 169.1 LGSS and opens «En el
  Régimen General»).
- **Never-coins:** «órgano de selección» appeared only in the plural; the m04-l02 heading «Órganos de selección» became
  «El órgano de selección». Plural `match` forms added to seven multi-word terms.
- **Glossary verification:** every candidate checked in pass 1 (8 FAIL across temas, all replaced with the reviewer's
  wording: g-organo-de-seleccion, g-comision-de-servicios, g-carrera-horizontal, g-pliego-de-cargos,
  g-mutualismo-administrativo, g-mutualista, g-incapacidad-temporal, g-promocion-interna) and the replacements in pass 2.
- **Goldens.** `glossary-links.es.txt` regenerated and read line by line: 121 → 235 → 225 web marks (62 also a PDF link).
  **Wrong-sense links excluded** (`link_except`): g-oposicion in m01-l07 (oposición de un tercero, Ley 19/2013) and
  m02-l04 (derecho de oposición, RGPD); g-directiva in m04-l01 and m04-l08 («funciones / facultades directivas»);
  g-convenio in m04-l06 (convenios colectivos); g-servicio-activo and g-separacion-del-servicio in m01-l04 (judges,
  LOPJ); g-incapacidad-temporal in m04-l05 and m04-l07 (the funcionarios' RDL 4/2000 sense); g-alto-cargo in m04-l04
  (alto cargo of an international organisation). Kept after reading: «Empleado Público» inside the TREBEP's title,
  «Real Decreto Legislativo / Decreto-ley n/aaaa» (each names a real one), g-convenio in m04-l01 (convenio de
  Conferencia Sectorial), g-interesado in m04-l04–l06, g-regimen-general-de-la-seguridad-social in m04-l04 and m04-l07.
  `lesson-refs.es.txt`: 21 → 57 references, 0 dangling.

## IV.1 — `m04-l01`

- **Tally** (2022–2025): Registro Central de Personal 4 (one anulada); art. 12 TREBEP (eventual) 2; arts. 8–9 1; art. 7
  1; art. 2 1; competencias 2 shared with other temas.
- **Structure:** clases de personal (arts. 8–13 TREBEP; eventual in full; interinos → m04-l03, laborales → m04-l08),
  demás normativa (DD única and DF 4.ª.2 TREBEP quoted; the BOE notes on Ley 30/1984; ámbito of RD 364/1995, RD 365/1995,
  RD 33/1986 and Ley 53/1984), competencias (Ley 30/1984 arts. 2–3 as in force; arts. 22.2–3 RD 829/2023 and 21.C)
  RD 1009/2023), Registro Central de Personal (art. 13 Ley 30/1984, art. 71 TREBEP, RD 2073/1999, arts. 15–16 RD 1405/1986).
- **«hoy»:** Ministerio de la Presidencia (art. 2 Ley 30/1984) → Ministerio para la Transformación Digital y de la Función
  Pública (art. 22.2 RD 829/2023). Not given: Dirección General de la Función Pública (art. 13.1 Ley 30/1984), Secretario
  de Estado para la Administración Pública (art. 25.1 RD 364/1995).
- **Glossary (5):** empleado público, funcionario de carrera, personal laboral, personal eventual, Registro Central de
  Personal.
- **Listed:** the anotación lists of art. 4.1 RD 1405/1986 and art. 13.1 RD 2073/1999 differ («reingresos», laboral
  «bajas definitivas»), which may be why conv2025_A P1 24 was annulled; art. 7 TREBEP now adds «y parental» (RDL 9/2025):
  conv2022_X P1 35 may need a «norma modificada» check; art. 11.2 RD 2073/1999 does not say hábiles or naturales.

## IV.2 — `m04-l02`

- **Tally:** 8 questions; 6 in scope (art. 103.3 CE; art. 70.1 TREBEP; art. 108.3 RDL 6/2023; art. 59.1 TREBEP; art. 10
  RD 364/1995; the OEP by Real Decreto); arts. 56 and 61.7 → m04-l03.
- **Worked date:** convocatoria published jueves 15-04-2027, veinte días naturales «a partir del siguiente al de
  publicación» (art. 18.1 RD 364/1995): viernes 16-04 to miércoles 05-05-2027.
- **Cambio pendiente:** art. 4.2 RDL 1/2013 «(desde 23-10-2026)»; no cited TREBEP article changes.
- **Glossary (3):** Oferta de Empleo Público, órgano de selección, Comisión Permanente de Selección.
- **Listed:** the approval form of the OEP rests only on art. 5.1 RD 2271/2004 («Real Decreto»); conv2020_X sup. II 15
  keys the Subsecretario as convoking organ, no source names it; RD 2271/2004 art. 1.1 defines discapacidad through the
  repealed Ley 51/2003.

## IV.3 — `m04-l03`

- **Tally:** 10 in scope; interinos (art. 10 TREBEP) 6 of them.
- **Cut for length:** DT 3.ª.2 TREBEP (the old Grupos A–E onto A1–C2). m04-l06 now quotes the fragment it needs.
- **Glossary (5):** funcionario interino, funcionario en prácticas, curso selectivo, oposición, concurso-oposición.
- **Listed:** the nombramiento organ (art. 25.1 RD 364/1995, Secretario de Estado para la Administración Pública)
  against the official keys' Secretaría de Estado de (Hacienda y) Función Pública; no source in the repo maps them.
  Ley 20/2021 (the art. 10 wording) is not in `sources/` and is not named.

## IV.4 — `m04-l04`

- **Tally** (29 questions): servicios especiales 8; servicio activo 4; interés particular, cuidado de familiares,
  adquisición 3 each; excedencia por servicios en el sector público, violencia de género, pérdida 2 each; one each for
  agrupación familiar, otras Administraciones, toma de posesión (art. 114.12 RDL 6/2023), suspensión firme.
- **Structure:** adquisición (art. 62; toma de posesión, quince días naturales from the publicación del nombramiento, one
  month with cambio de localidad, art. 114.12 RDL 6/2023) and pérdida (arts. 63–68; jubilación 2027: 67, or 65 with
  38 años y 6 meses, art. 205.1.a) and DT 7.ª LGSS); situaciones in tables (requisitos / duración / efectos), every
  plazo of reingreso (arts. 9.1, 14.3, 15.3, 16.4, 17.2, 18.4, 22.3–5 RD 365/1995); reingreso and adscripción provisional.
- **Worked dates:** nombramiento published lunes 01-03-2027 → martes 16-03-2027, or jueves 01-04-2027 with cambio de
  localidad; cese of an alto cargo published viernes 14-05-2027 → lunes 14-06-2027 (art. 9.1 RD 365/1995 with art. 30.4
  LPAC; the lesson says art. 9.1 gives no start date).
- **Glossary (4):** servicio activo, servicio en otras Administraciones Públicas, suspensión firme, expectativa de destino.
- **For the exams ledger:** art. 114.12 RDL 6/2023 supports the official key of conv2025_A sup. I 16, which the exams
  ledger marks «Clave oficial discutida»; art. 48.1 RD 364/1995 (three días hábiles / one month) is provisión, not
  nuevo ingreso. The IV.3 writer reached the same reading.
- **Listed:** whether «a partir de la publicación» (art. 114.12) counts the publication day; start of the month in
  art. 9.1 and counting of «con un mes de antelación» in art. 22.3 RD 365/1995; whether DF 4.ª.2 keeps the excedencia por
  servicios en el sector público and the other situaciones outside art. 85.1 TREBEP (art. 85.2 allows future laws to
  create them; the exams treat them as in force); art. 19 RD 365/1995 (no trienios) against the last paragraph of
  art. 29.3 Ley 30/1984.

## IV.5 — `m04-l05`

- **Tally** (46 rows, 39 in part 2): provisión 16 (concurso 7, libre designación 3, toma de posesión y cese 3, comisión
  de servicios and adscripción provisional 3); permisos 10; vacaciones 2; grado personal 5; promoción interna 3; código
  de conducta 2; derechos 2; carrera horizontal 1; owned elsewhere 5 (art. 30 TREBEP → m05-l04).
- **Structure:** «Qué norma se aplica» (DF 4.ª.1 TREBEP, DF 7.ª.2 RDL 6/2023 quoted); concurso, libre designación,
  toma de posesión y cese (art. 48 RD 364/1995 with the prórrogas of 48.2 and 48.3), other forms in a table (comisión
  de servicios voluntaria and forzosa, «duración máxima de un año», adscripción provisional, redistribución,
  reasignación, movilidad por salud and por violencia de género); derechos (art. 14, shortened list; art. 15); permisos
  (every letter of arts. 48 and 49 TREBEP in tables; «desde 23-10-2026» on the two paragraphs Ley 4/2026 adds to
  art. 49.e)); vacaciones (art. 50); who grants permisos (apartados 9.7 and 9.10 of the Resolución de 14-04-2026: no norm
  names the organ); deberes (arts. 52, 53.7, 54.3, 54.8); carrera horizontal (art. 122 RDL 6/2023); grado personal
  (art. 70 RD 364/1995); promoción interna (art. 18.2 TREBEP; arts. 73, 76 RD 364/1995).
- **Worked date:** cese lunes 03-03-2025 with cambio de residencia → jueves 03-04-2025 (the 2025 ordinario key; art. 48.1
  RD 364/1995 with art. 30.4 LPAC; the lesson says art. 48 does not say how the month is computed).
- **Glossary (8):** libre designación, grado personal, comisión de servicios, adscripción provisional, redistribución de
  efectivos, reasignación de efectivos, promoción interna, carrera horizontal.
- **Cuts of note:** méritos and concurso específico, remoción, art. 47 and 47 bis TREBEP (jornada), arts. 50.5, 58.2, 74.1,
  78–79 RD 364/1995, art. 51.2 list, art. 54 bullets other than 54.3 and 54.8, art. 14 letters not asked, the vacaciones
  worked example. None asked in 2022–2025.
- **For the exams ledger:** the matrimonio «quince días naturales» key (conv2025_A sup. II reserva 2) rests on the 2019
  Resolución, not saved; the 2026 one (apartado 14.3) gives the same reading. conv2024_A sup. II reserva 1: the key holds
  under art. 67 RD 364/1995, not only 54.1.

## IV.6 — `m04-l06`

- **Tally** (21 valid): faltas muy graves 5; incompatibilidades 5; faltas graves and leves 3; sanciones 3; procedimiento
  3; prescripción 2.
- **Structure:** incompatibilidades (Ley 53/1984: arts. 3, 7, 9, 12, 14, 16, 19; RD 598/1985 arts. 5, 14; DF 4.ª.1 párr. 2
  TREBEP); régimen disciplinario (arts. 93–98 TREBEP; art. 95.2 in full; arts. 7.1 and 8 RD 33/1986 in full; sanciones
  table with arts. 14–17 RD 33/1986; prescription table, both regimes); procedimiento (arts. 29–37 and 41–45 RD 33/1986;
  suspensión provisional, art. 98.3 TREBEP, arts. 33 RD 33/1986 and 21.4 RD 365/1995).
- **Worked date:** pliego de cargos notified martes 04-05-2027, diez días (art. 36 RD 33/1986), with art. 30.2 LPAC →
  martes 18-05-2027; the lesson says RD 33/1986 does not say hábiles or naturales.
- **Glossary (6):** separación del servicio, suspensión provisional, pliego de cargos, autorización de compatibilidad,
  reconocimiento de compatibilidad, demérito.
- **Listed:** whether the AGE has the ley de Función Pública that would bring in the new art. 16.1 Ley 53/1984; art. 33.2
  RD 33/1986 refers to the Ley de Funcionarios Civiles del Estado, repealed by DD única a) TREBEP; art. 32.1 to the old
  Ley de Procedimiento Administrativo; RD 33/1986 fixes no overall plazo máximo; old organ names (Comisión Superior de
  Personal, Gobernadores civiles) quoted without «hoy»; RD 1777/1994 not in `sources/`. For the exams ledger: conv2022_X
  sup. II 2 (key against art. 96.1.a) TREBEP, already flagged); conv2020_X sup. II 19 keys the Oficina de Conflictos de
  Intereses, no source supports it.

## IV.7 — `m04-l07`

- **Tally:** 6 + 1 shared with IV.9 (art. 21 RDL 4/2000 ×2; arts. 5, 3.1, 22.2; Ley 29/1975); conv2022_X P1 9 (art. 264
  LGSS) → IV.9.
- **Structure:** régimen especial (arts. 1–4 RDL 4/2000; the 2011 integration, art. 2.2 RDL 4/2000 and DA 3.ª.1 and 3.ª.3
  LGSS); MUFACE (naturaleza, art. 5.1; RD 577/1997 arts. 1, 4–5; adscription through the SEFP, art. 22.3.c)
  RD 829/2023); campo de aplicación (art. 3 in full); asistencia sanitaria (arts. 15.1, 17.1); incapacidad temporal
  (arts. 19–21; RD 375/2003 arts. 90.4, 95.1–2; donación de órganos, art. 21.1.c)); riesgo durante el embarazo
  (art. 22); clases pasivas (RDL 670/1987, arts. 28–45 as cited, pensiones table).
- **Cut:** cotización, financiación, the nine-item prestaciones list, incapacidad permanente in MUFACE (art. 23), gran
  invalidez, the art. 28.2.a) prórroga (twelve / fifteen years). None asked in 2022–2025.
- **Glossary (3):** mutualismo administrativo, Régimen de Clases Pasivas, mutualista.
- **Listed:** RD 466/2026 renamed MUFACE while RDL 4/2000 and RD 375/2003 keep the old name; RD 577/1997 has two
  articles numbered 6; art. 5.1 RD 577/1997 still names the «Ministro de Hacienda y Función Pública», quoted without
  «hoy»; art. 4.1 RDL 4/2000 («dependiente del Ministerio de Administraciones Públicas») gets today's adscription in the
  next sentence rather than as «(hoy: …)»; conv2022 P1 32 (MUFACE «created» in 1975) has no source; conv2022 sup. II
  reserva 2 keys «día 91» against «desde el cuarto mes».

## IV.8 — `m04-l08`

- **Tally** (23 rows): Convenio clasificación 6 (art. 8.1 ×5, art. 11); ámbito 2 (the exterior exclusion); TREBEP 61.7
  ×2, 11.3, 7; Convenio arts. 27.2, 31.3, 72.2, 70 and DA 11.ª one each; 7 owned elsewhere (complementos and
  indemnizaciones → m05-l04).
- **Structure:** régimen jurídico (arts. 7, 11 TREBEP; ET), selection (arts. 11.3, 55.2, 61.7 TREBEP; Convenio arts. 27,
  31), derechos y deberes (arts. 14–15, 51–52 TREBEP; ET), jornada (Convenio arts. 64, 72 against the Resolución de
  14-04-2026: both stated, no rule), incompatibilidades and régimen disciplinario (arts. 93–96 TREBEP; → m04-l06),
  Convenio: ámbito (arts. 1–2 in full), vigencia (art. 3), sistema de clasificación (arts. 7–11, grupos M3–E0 with
  their titulaciones).
- **Glossary (3):** grupo profesional, familia profesional, despido disciplinario.
- **Listed:** jornada 37,5 h (Convenio) against 35 h (Resolución de 14-04-2026, apartado 3.1); Convenio art. 33.1 (six
  months in twelve, under RD 2720/1998, not in `sources/`) against art. 15.2 ET as now worded; whether the DT 3.ª
  encuadramiento has become effective; whether the Convenio has been denounced (art. 3). For the exams ledger:
  conv2025_A sup. II 15 is an INAEM case, and art. 8.4 / anexo IV exclude INAEM from the art. 8 classification;
  conv2025_X sup. I 20 prints identical text in options b) and d) (key d); conv2020_X P1 35, options a)–c) all in anexo II.

## IV.9 — `m04-l09`

- **Tally:** 7 distinct (art. 44.1 ×2; 42.1.a); 46.1; 194.1; 215.2.a); 264.1.d)).
- **Structure:** campo de aplicación (arts. 7, 136 LGSS; funcionarios of DA 3.ª → m04-l07); acción protectora (art. 42.1
  in full; arts. 44, 46); incapacidad temporal (arts. 169–174, the observation periods, donación de órganos);
  nacimiento y cuidado (arts. 177–179), riesgo durante el embarazo y la lactancia (arts. 186–189), cuidado de menores
  con cáncer (arts. 190–192, art. 190.5 «desde 23-10-2026»), incapacidad permanente (arts. 194, 196), jubilación
  (art. 205 and DT 7.ª; parcial, art. 215.2), muerte y supervivencia (art. 216, with 216.3), desempleo (arts. 264, 268,
  270), prestaciones familiares (art. 237.1).
- **Worked date:** baja por enfermedad común lunes 01-03-2027: subsidio from jueves 04-03, paid by the empresario up to
  lunes 15-03 (art. 173.1); the lesson says the article does not say whether the baja day is day 1 or whether days are
  naturales.
- **Cut:** art. 155.1, corresponsabilidad en el cuidado del lactante (arts. 183–184), art. 195.1, the desempleo duration
  scale (art. 269.1), the pointer to the Convenio complement in m04-l08. None asked in 2022–2025. art. 363.1.d) (the
  scope table gave it to IV.9) is a non-contributory pension outside the Régimen General (art. 155.1); it is not cited.
- **Glossary (2):** incapacidad temporal (Régimen General sense), Régimen General de la Seguridad Social.
- **Listed:** STC 140/2024 on art. 177 (unconstitutional without nullity), not in `sources/`; the IT percentages are not
  in the LGSS (art. 171 leaves them to implementing rules); arts. 237.1, 165.3 and 187.2 still say «maternidad /
  paternidad».

## course.yaml

- Lesson summaries m04-l01…m04-l09, three sentences each, from the writers' notes as fixed after review. Each tema's
  reviewer checked its three sentences (pass 1: 8 FAIL in all, fixed with the reviewer's wording), and the second pass
  checked the changed ones.
- Module summary for m04, two sentences, in the m01–m03 shape; it names topics only.

## Checks and suites (bloque IV)

Run on the final tree (lessons, glossary, course.yaml, goldens, normativa.yaml and saved sources of this round):

- **Pipeline, course as draft:** loads and validates. `pytest -k "glossary or registry or content or pipeline"`: 68
  passed, including the never-coins checks for glossary and summaries (it first failed on «órgano de selección», plural
  only; see Glossary). `figure steps per course`: `age-administrativo-c1: no figures`, `crypto-futures: 34 figures`,
  `fixture-oposiciones: no figures`.
- **Backend (`uv run pytest`):** 1,374 passed, 20 skipped, 4 warnings.
- **Frontend (`npx vitest run`):** 562 passed, 1 failed, 49 skipped on the first full run; `tsc -b` clean. The failure
  was the list-shape guard: nine Normativa lines ended in a bare article number («art. 30.»), which renders as an
  ordered-list marker. Each now carries the article's heading or scope in parentheses, as m01-l06 does («art. 30
  (cómputo de plazos).»). After the fix `src/lib/refs`, `src/lib/glossary` and `src/lib/pdf`: 302 passed, 49 skipped.
- **Goldens:** `glossary-links.es.txt` (225 web marks) and `lesson-refs.es.txt` (57 references, 0 dangling) regenerated
  and read line by line (see Glossary). No diff under `content/crypto-futures/` or `dist/`.
- **Android bundle:** re-exported, fingerprint unchanged `9c95cf4a6bf2…` (98 files); `--verify-only` OK, leaked tokens OK.
- `README.md` (course status line) now says the theory of bloques I–IV is written.

## Open items (after bloque IV)

- **After the 29-11-2026 elections:** the «hoy» re-check round also covers m04-l01, m04-l03 (Ministerio para la
  Transformación Digital y de la Función Pública, art. 22.2 RD 829/2023) and m04-l07 (MUFACE's adscription through the
  Secretaría de Estado de Función Pública, art. 22.3.c) RD 829/2023).
- **Exams ledger (R3), from this bloque:** conv2025_A sup. I 16 (art. 114.12 RDL 6/2023 supports the official key; the
  «Clave oficial discutida» note can go); conv2022_X P1 35 (art. 7 TREBEP now adds «y parental», RDL 9/2025: «norma
  modificada» check); conv2025_X sup. I reserva 3 (key d), see the INE fix); conv2024_A sup. II reserva 1 (key holds under
  art. 67 RD 364/1995); conv2025_A sup. II 15 (INAEM is outside the art. 8 classification of the Convenio único);
  conv2025_X sup. I 20 (options b) and d) identical); conv2020_X sup. II 19 (Oficina de Conflictos de Intereses, no
  source); conv2022 P1 32 (MUFACE «created» in 1975, no source).
- **Which rule applies:** the differences listed above stay open until a text settles them; questions authored on them
  must rest on the rule the stem names, or use the point both texts share.
- **DF 4.ª.1 TREBEP and RDL 6/2023:** no source says whether RDL 6/2023 libro segundo makes arts. 16–20 and 78–84 TREBEP
  effective in the AGE. If one appears, m04-l03, m04-l05 and the «Qué norma se aplica» section change.
- **Not saved, cited by no sentence:** the Resolución de 28-02-2019 (jornada; in force at the 2022–2025 exams),
  RD 466/2026 (MUFACE renaming; verified on boe.es), Ley 20/2021 (art. 10 TREBEP wording), RD 2720/1998 (Convenio
  art. 33.1), RD 1777/1994 (incompatibilidades procedure), STC 140/2024 (art. 177 LGSS). Save one before a question
  rests on it.
- **Cut for length, candidates if a later round has room:** DT 3.ª.2 TREBEP in full (m04-l03; m04-l06 quotes a
  fragment), MUFACE incapacidad permanente (m04-l07), the desempleo duration scale and corresponsabilidad en el cuidado
  del lactante (m04-l09), concurso específico and remoción (m04-l05).
- **Waiting glossary terms:** the bloque I–III lists (minus «libre designación», which entered) plus «personal
  directivo» and «incapacidad permanente».

## Second blind pass on the unreviewed changes (start of bloque V, 2026-10-17)

The fixes in IV.8 and the final replacements applied by diff in IV.4, IV.5, IV.6, IV.7 and IV.9 (the «applied» /
«coordinator» rows of the Summary) had not been re-read by a reviewer. The working tables of bloque IV were gone, so
the items were recovered from the previous session's transcripts: the last review report of each lesson (its FAIL rows,
lesson, glossary, summary and Normativa) and the coordinator's replacement scripts. A reviewer that had written none of
them located each item by its excerpt in the current files and re-checked it against the article.

| Lesson | Checked | PASS | FAIL | Not located |
|---|---|---|---|---|
| IV.4 `m04-l04` | 5 | 5 | 0 | 0 |
| IV.5 `m04-l05` | 9 | 8 | 1 | 0 |
| IV.6 `m04-l06` | 6 | 6 | 0 | 0 |
| IV.7 `m04-l07` | 6 | 5 | 1 | 0 |
| IV.8 `m04-l08` | 6 | 6 | 0 | 0 |
| IV.9 `m04-l09` | 10 | 10 | 0 | 0 |
| **Total** | **42** | **40** | **2** | **0** |

Both FAILs were dropped exceptions, both fixed against the article:

1. **IV.5, art. 48.1 RD 364/1995 with art. 30.4 LPAC** (cese → toma de posesión in one month). The sentence lacked the
   art. 30.4 rule for a month with no equivalent day. It now ends «…en el mes de vencimiento o, si en el mes de
   vencimiento no hubiera día equivalente, el último día del mes (m03-l03).» To stay at 4,000 words, the full LPAC title
   in that sentence became «artículo 30.4 LPAC» (the Normativa line names Ley 39/2015). The Normativa line now reads
   «art. 30.4 (plazos en meses).» `wc -w` 4,000.
2. **IV.7, art. 28.2.a) TRLCPE.** Cutting the prórroga sentence to make room for fix #19 had removed the «No obstante»
   exception, so jubilación forzosa read as having none. Restored in item a): twelve years of servicios efectivos, the
   fifteen of art. 29 not completed, prórroga for the time missing, granted if apto. `wc -w` 2,439, 39 over the 2,400
   ceiling. The reviewer's candidate cut was the art. 22.3.c) RD 829/2023 sentence, which carries MUFACE's present
   adscription and sits in the «hoy» re-check open item. It was kept, and the overrun is accepted.

A third blind check of both replacements passed. The reviewer added one note: no article sends the toma-de-posesión
month to the LPAC, so applying art. 30.4 to a cese is the lesson's reading. The sentence says so («El artículo 48 no
dice cómo se computa el mes. Con el artículo 30.4 LPAC…»). Not counted as FAILs, still open: m04-l09 is at 2,401 words
(the scope table gave IV.9 2,200, raised to 2,400 by the coordinator); m04-l08 line 208 runs to 120 columns. The
broken wrap inside «(art. 5.1 RDL 4/2000)» in m04-l07 was fixed. Outside this pass's scope and not re-read: the IV.4
summary wording «el Reglamento de Situaciones Administrativas», the Normativa labels of m04-l01 and m04-l03, and the
`link_except` edits.

## Where to resume (after bloque IV)

Bloque IV is closed. The next session starts R2 bloque V (temas V.1–V.6, lessons `m05-l01`…`m05-l06`) with the same
spec, the standing conventions and the outside-sources rule. Two rules from this bloque carry over: quote the TREBEP
disposición derogatoria única with its opening paragraph, and cut whole facts only, never a clause of a kept sentence.
m04-l05 points to m05-l04 for the derechos retributivos.

# Bloque V — temas V.1–V.6

Round R2, bloque V, 2026-10-17. Nothing committed. Same procedure as bloque IV: one writer per tema to a shared spec
(the bloque IV spec adapted to bloque V: budget in force, amounts verbatim, the cambio-pendiente norms of this bloque,
a scope table), then a separate blind reviewer that had not written the lesson. The reviewer re-opened the cited
article for every sentence, table row and cell carrying a number, plazo, amount, percentage, organ, date, exception,
condition or list, recomputed every worked example, verified every newly saved source on boe.es (fresh download, same
sha256), and checked Normativa, «Lo que más cae», the glossary candidates and the course.yaml summary. Every FAIL was
fixed against the article; the changed sentences went through a second blind pass, and a third where the second found
FAILs. The writer of tema N+1 drafted while tema N was in review (V.4 drafted alongside V.3). The per-sentence tables are
working files, not kept in the repo.

**No unreviewed last edits.** Bloque IV left replacements applied after the last pass (see «Second blind pass on the
unreviewed changes» above). This bloque closed that gap: every replacement the coordinator applied after a lesson's last
blind pass (V.2 Normativa and summary, V.3 «Lo que más cae» and summary, V.4 «Lo que más cae» and summary, V.5 summary,
and the two bloque IV fixes) went through one more blind check: 6 PASS, 1 FAIL. The FAIL was the V.4 summary, where the
1,5 % read as the only 2026 increase; it was fixed with the reviewer's wording. Two edits came after that check: the V.6
art. 42.4 LGS sentence and two clarity changes in the V.2 summary. Each is the reviewer's wording, checked by the
coordinator against the article (art. 42.4 LGS; art. 56.3–4 LGP; art. 2.1–2 RDL 14/2025), with no further blind pass.

Suites before writing (tree at the start of the session): backend `uv run pytest` 1,374 passed, 20 skipped; frontend
`npx vitest run` 561 passed, 2 failed, 49 skipped. The two failures were the glossary-link and lesson-reference goldens,
which moved because m05-l01 and the bloque IV fixes were edited during the run.

## Prompt decisions for this bloque

- **Budget in force.** On 17-10-2026 no Ley de Presupuestos Generales del Estado has been published after the Ley
  31/2022 (PGE 2023). A title search in the boe.es API is saved as `sources/otros/boe-api-leyes-pge_2026-10-17.json` and
  indexed. m05-l01 states that the PGE 2023 are in force prorrogados (art. 134.4 CE, art. 38 LGP) and that figures tied to
  the annual budget law change every year. m05-l02 and m05-l04 repeat the second point where they give a figure. The
  Ley 31/2022 entry of `normativa.yaml` now lists V.1.
- **Pagos a justificar and anticipos de caja fija.** The round prompt asks for them with V.2/V.3 at the 4,000 ceiling; the
  programme lists them in V.5. Their full regime (límites, plazos, justificación, reposición, cuentas) is in m05-l03; m05-l05
  gives what each is, its norm and the cross-reference. The art. 79.3 LGP rule on the carta de pago for the unspent amount
  stays in m05-l05 under «Justificación de libramientos».
- **V.4 ceiling.** The prompt holds word targets for V.1, V.5 and V.6 only, and requires the indemnización tables in V.4.
  The coordinator raised V.4 from 2,800 / 3,400 to the course maximum of 4,000 (R4.3). m05-l04 is at 3,984.
- **Amounts in V.4.** RD 462/2002: anexo II as revised by the Acuerdo del Consejo de Ministros of 02-12-2005, published by
  Resolución de 2 de diciembre de 2005 (BOE-A-2005-19988). It is the last revision of anexo II on boe.es on 17-10-2026, and
  the consolidated text already prints its amounts. Kilometraje: Orden HFP/793/2023 (0,26 / 0,106 euros por kilómetro).
  The lesson quotes DF 4.ª RD 462/2002 (Consejo de Ministros for anexos II and IV, the Ministro de Hacienda for the
  kilometraje) and art. 11.2 (anexo III). Sueldo, trienios, pagas extraordinarias and complemento de destino for 2026: the
  two SEPG tables, saved under `sources/otros/` and indexed. They are not norms: they apply art. 2.1 RDL 14/2025 to the
  art. 19.Cinco and art. 23 amounts of the Ley 31/2022. The lesson says they change every year.

## Saved sources (bloque V)

Indexed in `normativa.yaml` (under a comment line before bloque VI) or `fuentes.yaml`. The tema reviewer verified each
writer-saved file independently on boe.es (fresh download, same sha256, metadata and /analisis).

| Source | File | Why |
|---|---|---|
| Resolución de 2-12-2005 (dietas, anexo II RD 462/2002) | `BOE-A-2005-19988_res-02-12-2005-dietas-anexo-ii_2005-12-03.pdf` | The amounts of anexo II in force; boe.es «SE ACTUALIZA el anexo II». Diario PDF. |
| Orden HFP/793/2023 | `BOE-A-2023-16462_orden-hfp-793-2023-kilometraje_2023-07-17.pdf` | Kilometraje of art. 18.1 RD 462/2002; repeals the Orden EHA/3770/2005. |
| Orden HAC/557/2026 | `BOE-A-2026-12037_orden-hac-557-2026-elaboracion-pge-2027_2026-06-05.pdf` | Elaboración of the PGE 2027 (V.1); programas (anexo I) and clasificación económica (anexo II). |
| Orden de 1-2-1996, Instrucción de operatoria contable | `BOE-A-1996-2627_orden-1996-instruccion-operatoria-contable_2024-09-17.pdf` | A different Orden from the documentos contables one of the same date. Ten official questions rest on it (reglas 6.1, 20, 24, 31, 36, 42, 77, 86). Saved by the V.3 writer. |
| Ley 33/1987 (PGE 1988) | `BOE-A-1987-28404_ley-33-1987-pge-1988_2013-12-26.pdf` | Arts. 33–34 (devengo of pagas extraordinarias; liquidación por días), to which art. 23.Uno.B) Ley 31/2022 refers; in force per /analisis. Saved by the V.4 writer. |
| Resolución de 20-01-2014, DG de Presupuestos (clasificación económica) | `BOE-A-2014-879_res-20-01-2014-clasificacion-economica_2014-01-29.pdf` | The only source that defines each capítulo with its inclusions and exclusions; three official questions name it. Saved by the V.5 writer. |
| SEPG, retribuciones del personal funcionario 2026 | `sources/otros/sepg-retribuciones-funcionarios-2026.pdf` | 2026 amounts (V.4). |
| SEPG, cuantías retributivas 2026 | `sources/otros/sepg-cuantias-retributivas-2026.pdf` | Same, by article of the Ley 31/2022. |
| boe.es API title search | `sources/otros/boe-api-leyes-pge_2026-10-17.json` | No Ley de PGE after the Ley 31/2022. |

`normativa.yaml` also: V.3 added to the temas of RD 640/1987 and RD 725/1989; V.2 and V.5 to the Orden HAC/557/2026.
The saved texts of the LGP, RD 462/2002, the Orden de 30-7-1992 and the other bloque V norms were checked against the
«Última actualización» on boe.es (17-10-2026). All are current.

## Summary

| Tema | Lesson | Target / ceiling | First draft | Words | Citations | Checked (pass 1) | FAIL (fixed) | Later passes | Glossary |
|---|---|---|---|---|---|---|---|---|---|
| V.1 | `m05-l01` | 1,800 / 2,200 | 4,056 | 2,169 | 44 | 65 | 3 + glossary 2 + summary 1 | p2 7/7 | 6 |
| V.2 | `m05-l02` | 4,000 cap | 5,625 | 4,000 | 72 | 120 (1 unverifiable) | 12 + LQMC 1 + glossary 5 + summary 3 | p2 27: 4 FAIL + summary 3; p3 8: 2 FAIL (Normativa) + summary 1, applied | 7 |
| V.3 | `m05-l03` | 4,000 cap | 7,545 | 3,999 | 60 | 136 | 7 (LQMC 2) + glossary 1 + summary 1 | p2 19/19; 1 LQMC outside the diff + summary 2, applied | 10 |
| V.4 | `m05-l04` | 2,800 / 3,400 → 4,000 | 6,137 | 3,984 | 54 | 123 | 8 + glossary 3 + summary 2 | p2 23: 1 FAIL + summary 2 + match 4; p3 7/7, 1 LQMC outside the diff, applied | 8 |
| V.5 | `m05-l05` | 2,000 / 2,400 | 3,707 | 2,367 | 13 | 58 | 4 (LQMC 2) + glossary 3 + summary 1 | p2 12/12; summary 1, applied | 5 |
| V.6 | `m05-l06` | 1,800 / 2,200 | 4,576 | 2,198 | 30 | 71 | 6 (LQMC 2) + glossary 1 + summary 1 | p2 20: 1 FAIL, applied | 2 |
| **Total** | | | | **18,717** | **273** | **573** | **41 lesson** | | **38** |

Words: `wc -w`, everything counted. Citations: «(art» / «(arts» only. V.5 cites mostly anexo IV of the Resolución de
20-01-2014, IOC reglas and Orden apartados, which are not counted. «applied»: the reviewer's replacement, applied by the
coordinator and covered by the closing check above.

**FAIL classes.** The same two as in bloques I–IV: a dropped «salvo / excepto / previo informe» clause (V.2 arts.
47.3, 54.3 with 59, 62.1.d); V.3 art. 152.2; V.4 arts. 7.1, 9.1, 11.2; V.6 arts. 34.4, 42.4 LGS), and a selective list
that reads as complete (V.2 the transferencias table and its órganos; V.3 the documentos contables table; V.4 anexo I
compacted). Bloque V adds two:
1. **Code grammar and labels no text states.** V.2 read «Sección 33, organismo 101» into an aplicación; V.4 labelled the
   SEPG annual columns ambiguously (12 mensualidades against the «TOTAL ANUAL» with pagas).
2. **Cut-induced FAILs again**, despite the rule. V.2 cut art. 53.5 (the exception to «en el propio ejercicio») and
   art. 10.Dos Ley 31/2022; V.4 cut art. 12.4 RD 462/2002 (the exception to «solo el 50 por 100» on return). Each was
   restored and paid for with another whole fact.

## Glossary

- 38 entries added, origin in bloque V; `glossary.yaml` holds 234. Each cites its defining article, which its origin
  lesson cites. g-clasificacion-economica has origin m05-l02 (art. 40.1.c) LGP), proposed by the V.5 writer.
- Dropped after review: g-credito-ampliable and g-incorporacion-de-credito (plural only in prose), g-acreedor-directo
  (plural only in its proposed origin m05-l03). Not proposed: prórroga presupuestaria, ciclo presupuestario, pago en firme
  (no text defines them).
- **Plural `match` forms.** The derived plural puts the ending on the last word. Head-noun plurals were added to 12
  bloque V terms (crédito(s) presupuestario(s), suplemento(s) de crédito, pago(s) a justificar…). The V.4 writer added
  them to complemento(s) de destino / específico(s) / de productividad, residencia(s) oficial(es) and the other V.4
  multi-word terms.
- **Goldens.** `glossary-links.es.txt` regenerated and read line by line: 225 → 292 web marks (79 also a PDF link).
  **Wrong-sense links excluded** (`link_except`): g-servicios-comunes in m05-l03 («entidades gestoras y servicios comunes
  de la Seguridad Social», the same false friend as m01-l07 and m02-l01) and g-convenio in m05-l06 (the concursal
  convenio of art. 34.4 LGS). Kept after reading: g-tribunal-de-cuentas and g-presupuestos-generales-del-estado in bloque
  I and IV lessons, g-estabilidad-presupuestaria in m01-l01 (art. 135 CE), g-alto-cargo in anexo I RD 462/2002 (m05-l04)
  and in the clasificación económica (m05-l05), g-unidades-administrativas in m05-l03 (RD 725/1989), g-convenio in
  m05-l02 (convenios between departments), g-directiva in m05-l06 (EU directives in the LCSP title), g-dieta in m05-l03.
  `lesson-refs.es.txt`: 57 → 86 references, 0 dangling.

## V.1 — `m05-l01`

- **Tally** (9 questions, 2022–2025): elaboración and remisión 5 (arts. 36.2, 36.5, 37.1 LGP; art. 134.3 CE), art. 28 LGP 2,
  art. 3.2 LO 2/2012 1, programas finalistas 1. 2020 (programa anterior): arts. 26.1, 27, 28.1 LGP.
- **Structure:** concepto (arts. 32, 34 LGP; art. 134 CE), principios as the texts name them (art. 26.1 LGP; arts. 3–8 LO
  2/2012; art. 134.2 CE), ciclo (elaboración arts. 36–37 LGP with the Orden HAC/557/2026 as the current example; aprobación;
  prórroga art. 38 LGP with the dated statement of the budget in force), presupuesto por programas (art. 35 LGP; the Orden),
  terminología. Worked examples: remisión of the 2027 proyecto before jueves 01-10-2026; 456C finalista / 423N instrumental
  by the anexo I letter rule.
- **Glossary (6):** Presupuestos Generales del Estado, estabilidad presupuestaria, escenarios presupuestarios plurianuales,
  ejercicio presupuestario, programa de gasto, crédito presupuestario.
- **Lo que más cae sources:** 1 conv2025_A P1 34, conv2022_X P1 12; 2 conv2022_X sup. II reserva 4; 3 conv2022 sup. I reserva
  5; 4 conv2024_A P1 35; 5 conv2024_X P1 34, conv2022_X P1 26; 6 conv2024_X P1 35; 7 conv2022_X P1 17; 8 style «texto
  alterado».
- **Listed:** no text in `sources/` names «fases» of the presupuesto por programas: the lesson says so and gives what the LGP
  regulates instead. «Ciclo presupuestario» is defined nowhere. Art. 134.3 CE (Congreso, three months) and art. 37.1 LGP
  (Cortes, before 1 October) are both stated. Art. 134.4 CE and art. 38.1 LGP word the prórroga differently; both are quoted.
  No text says each successive prórroga carries the 2023 initial budget. Orden HAC/557/2026 anexo I refers to a
  non-existent «artículo 6 apartado 1.1.1». Art. 35.1 LGP prints «33.1.ª)».

## V.2 — `m05-l02`

- **Tally** (38 questions, 34 in part 2): clasificación económica 11 (shared with V.5), transferencias 9 (arts. 52.1.a),
  61.a), 62.1.a), 62.2, 63.1.a) LGP; art. 9.Dos.1 Ley 31/2022), gastos plurianuales 5 (art. 47.2–3), generaciones 4,
  extraordinarios and suplementos 4, retención previa a una transferencia 2, incorporaciones, anticipos, vinculación 1 each.
- **Structure:** PGE: contenido y estructura (arts. 33, 35, 40 LGP; Ley 31/2022); the reading of an aplicación as far as a
  text states (art. 8.Dos.5 Ley 31/2022); créditos: especialidad, vinculación (arts. 27.2, 42–44, 46); gastos plurianuales
  (arts. 47, 47 bis); every modificación (arts. 51–60 LGP; Ley 31/2022 arts. 9–11) with a summary table modificación /
  órgano / financiación; anticipos de tesorería (art. 60). Worked examples: a plurianual of 810.000 euros on a crédito
  inicial of 800.000 (second year above the 60 % ceiling: only the Gobierno, art. 47.3); a suplemento of 15.000 euros in an
  organismo autónomo with a capítulo of 85.000 (Ministro de Hacienda, art. 56.3.b).
- **«hoy» notes:** «Ministro de Hacienda y Administraciones Públicas» (art. 55.2 LGP) and «Ministerio de Hacienda y Función
  Pública» (art. 9 Ley 31/2022) → Ministerio de Hacienda (art. 5.1 RD 829/2023). «Ministro de Economía» (art. 60.1, anticipos
  de tesorería) is quoted without «hoy»: no RD 829/2023 article clearly covers it.
- **Glossary (7):** crédito extraordinario, suplemento de crédito (one shared wording, faithful to art. 55.1), generación de
  crédito, transferencia de crédito, anticipo de Tesorería, Fondo de Contingencia, compromiso de gasto plurianual.
- **Lo que más cae sources:** 1 conv2022 sup. II 17, conv2025_X sup. II 18, conv2024_X sup. I 2, conv2022_X sup. II 13; 2
  conv2022 sup. II reserva 3, conv2024_X sup. I 2, conv2022_X sup. II 13; 3 conv2022 P1 16, conv2024_X sup. I 1; 4 conv2022_X
  sup. I reserva 2, conv2025_A sup. II 10, conv2025_X sup. I 13, conv2022_X sup. II 15; 5 conv2025_A sup. I 11, conv2022 sup. I
  9; 6 conv2025_A sup. II 11–12, conv2022 sup. I 10.
- **Cuts of note:** arts. 7 (regla segunda) and 10.Cinco Ley 31/2022 (arrendamientos plurianuales: diez anualidades,
  100 %), arts. 39, 41, 47.4–6, 49.2, 50.2, 53.4, 54.4, 56.5–6, 57, 60.2 LGP, and the RC/MC sentences (the retención
  previa is now in m05-l03, regla 6.1 IOC).
- **Listed:** art. 47.2 says «no superior a cuatro» ejercicios and gives four percentages for later years, and it does not
  say at which level the «crédito inicial» is taken. Art. 56 does not restate the art. 55.1 conditions. Whether «excluidos
  incentivos al rendimiento y gastos sociales» (art. 9.Siete Ley 31/2022) also limits the capítulo 1 ampliaciones is open.
  Art. 10 Ley 31/2022 is renumbered by RDL 7/2026; the lesson cites the current numbering. No text states how an aplicación
  code is built.
- **For the exams ledger:** conv2024_X sup. I 4 keys the titular del ministerio for a transfer 220 → 202; arts. 63.1.a) with
  43.2.b), 62.1.a) LGP and art. 9.Dos.1 Ley 31/2022 give it to the Ministro de Hacienda, and the parallel conv2022_X sup. II
  15 and conv2025_X sup. I 13 key Hacienda: candidate «Clave oficial discutida». conv2025_X sup. I 12 and conv2022 sup. II 11
  (retención previa) are supported by regla 6.1 IOC.

## V.3 — `m05-l03`

- **Tally** (50 questions, 1 anulada; includes the PAJ/ACF rows the exams ledger files under V.5 and the two retención
  rows from V.2): documentos contables 15, anticipos de caja fija 10, pagos a justificar 7, fases 6, órganos (art. 74 LGP) 5,
  Tribunal de Cuentas and rendición 3, función interventora 2, ordenación del pago 1, realización del pago 1. No 2022–2025
  question asks reparos, discrepancias, omisión, control financiero permanente, auditoría or the Tribunal's composition.
- **Structure:** órganos (art. 74 LGP); fases (art. 73 LGP; regla 20 IOC) and documentos contables (apartados sexto–séptimo
  Orden de documentos contables; IOC) with a fase / documento / órgano table; compromisos para ejercicios posteriores
  (cross-reference m05-l02; IOC reglas 42 and 77); ordenación del pago (art. 75.1 LGP) and realización (apartados sexto–noveno
  Orden PRE/1576/2002 as amended in 2026); pagos a justificar (art. 79 LGP; RD 640/1987, art. 6 «desde 28-10-2026») and
  anticipos de caja fija (art. 78 LGP; RD 725/1989, art. 6.3 «desde 28-10-2026») in full; control interno (arts. 142 and
  following LGP: función interventora, fiscalización limitada previa, reparos, discrepancias, omisión; RD 2188/1995 art. 16
  for the fifteen-day plazos); Tribunal de Cuentas (art. 136 CE; LO 2/1982; Ley 7/1988). Worked example: fondos a justificar
  received martes 02-03-2027, invested lunes 15-03-2027 → jueves 15-04-2027 and miércoles 02-06-2027 (the RD is silent on the
  cómputo; art. 30.4 LPAC applied, the lesson says so).
- **«hoy» note:** «Ministro de Economía» (art. 75.1 LGP) → Ministerio de Economía, Comercio y Empresa (art. 15.A).1.º RD
  1009/2023).
- **Glossary (10):** aprobación del gasto, compromiso de gasto, reconocimiento de la obligación, anticipo de caja fija, pago a
  justificar, función interventora, control financiero permanente, auditoría pública, reparo, Tribunal de Cuentas.
- **Lo que más cae sources:** 1 conv2024_X P1 39, conv2022 sup. II 9; 2 conv2025_X P1 39, conv2025_X sup. I 7, conv2024_A sup.
  II 20, conv2024_X sup. I 19; 3 conv2025_A P1 38, conv2024_A P1 40; 4 conv2025_X sup. II 12; 5 conv2025_A sup. I reserva 4,
  conv2022_X sup. I 19, conv2024_A sup. II 12; 6 conv2025_X P1 36, conv2024_X sup. I 3; 7 conv2025_X sup. I 4, conv2022_X sup.
  I 7; 8 conv2024_A P1 38; 9 conv2024_X P1 37.
- **Cuts of note:** art. 74.4 LGP (delegación and desconcentración) and regla 55.1 IOC, both named in the scope table; regla
  77.7 (resolución del contrato) and anexo I fecha-de-gasto rules went to m05-l06.
- **Listed:** two plazo regimes for pagos a justificar (art. 79.4 LGP: three months, six for expropiaciones and pagos en el
  extranjero; art. 10 RD 640/1987: the month after the inversión and in any case three months, FSE and expropiaciones six),
  both stated and attributed. Two dates for the Cuenta General (art. 131.1 LGP before 31 October; art. 33.1 Ley 7/1988), both
  stated. RD 2188/1995 lags the LGP (500.000 pesetas in art. 18 against 5.000 euros in art. 151.c) LGP; four reparo cases
  against five in art. 154.2): the lesson cites the LGP. Art. 77 LGP is pagos indebidos, not modos de pago; the current LGP
  has no plan de disposición de fondos; «propuesta de pago» is part of the reconocimiento (art. 73.4 LGP). The IOC cites the
  1988 TRLGP. Art. 136.1 CE prints «de Estado» (sic).
- **For the exams ledger:** conv2022 sup. II 9 (ACF in Parques Nacionales: the supuesto gives no capítulo 2 figure to check the
  7 %); conv2024_X sup. II reserva 5 (RC «más el IVA» rests on the LCSP, not on the V.3 orders); conv2025_A sup. II reserva 4
  (organ name).

## V.4 — `m05-l04`

- **Tally** (20 questions: 15 classified V.4 plus conv2025_X S2 8–9 (art. 30 TREBEP), conv2025_X S2 3 and conv2022_X P1 15
  (Convenio), conv2024_A P1 36): RD 462/2002 6, Ley 30/1984 4, Ley 33/1987 3, art. 30 TREBEP 2, Convenio 2, clasificación
  económica 3, Orden de 30-7-1992 0. The bloque IV ledger said IV.5 sent five art. 30 rows here; the V.4 writer found two in
  2022–2025 plus conv2020 P1 reserva 2.
- **Structure:** retribuciones de los funcionarios (arts. 21–24, 30 TREBEP with DD única and DF 4.ª quoted; arts. 23–24 Ley
  30/1984; art. 23 Ley 31/2022) with the 2026 tables (sueldo and trienio by subgrupo, pagas extraordinarias, complemento de
  destino niveles 16 a 22 from the SEPG documents; RDL 14/2025 art. 2.1–2, including the conditional 0,5 % payable in the first
  quarter of 2027); personal laboral (art. 56.1 IV Convenio único); nóminas, altas y bajas (Orden de 30-7-1992); devengo y
  liquidación (arts. 33–34 Ley 33/1987); pago (Orden PRE/1576/2002); indemnizaciones (RD 462/2002: supuestos, anexo I in full,
  anexo II table, kilometraje, anexo III named, anexo IV table, art. 12 hours, art. 7.1 courses, art. 32.Tres and DA 32.ª Ley
  31/2022 as far as the text goes; DF 4.ª and art. 11.2 on who revises each amount). Worked example: a C1 funcionario in
  comisión de servicio con derecho a indemnización, martes to miércoles, 28 h: 48,92 + 28,21 + 110,24 = 187,37 euros.
- **Glossary (8):** trienio, complemento de destino, complemento específico, complemento de productividad, gratificación por
  servicios extraordinarios, residencia oficial, comisión de servicio con derecho a indemnización, dieta. No wrong-sense
  overlap with g-comision-de-servicios (provisión sense).
- **Lo que más cae sources:** 1 conv2025_A P1 37, conv2024_A sup. II reserva 4; 2 conv2024_A P1 39; 3 conv2024_X P1 38; 4
  conv2025_X sup. II 8–9; 5 conv2025_X P1 38, conv2022 P1 reserva 4; 6 conv2022 sup. I reserva 3, conv2024_A sup. I reserva 2;
  7 conv2024_A sup. II 5; 8 conv2022 P1 25; 9 conv2024_X sup. II reserva 2.
- **Cuts of note:** art. 27 TREBEP, the RDL 6/2023 complemento de desempeño and de carrera paragraph, apartados 4.2.2.1, 5.5,
  6 and 8 of the Orden de 30-7-1992, noveno.2.1.a) Orden PRE/1576/2002. None asked in 2022–2025.
- **Listed:** anexo IV (asistencias) keeps its 2002 amounts; boe.es records no revision. Art. 32.Tres Ley 31/2022 keeps
  indemnizaciones at their 2022 amounts, while the Orden HFP/793/2023 raised the kilometraje in 2023 and RDL 14/2025 does not
  name art. 32.Tres. DA 32.ª says only that the art. 26.3 suspension «se mantiene»; the year rests on the boe.es analysis, so
  the lesson gives none. The two SEPG documents give different annual complemento de destino figures (14 payments against
  12 mensualidades); the lesson uses the 12-mensualidad column and labels it. DF 4.ª.1 TREBEP defers arts. 21–30 (except
  25.2): both rules are stated, as in bloque IV. Anexo I keeps «los Ministerios de Hacienda y de Administraciones Públicas»
  without «hoy». No text in `sources/` gives a euro rounding rule. For funcionarios, no text in `sources/` states the 1
  December start of the paga period.
- **For the exams ledger:** conv2022 P1 25 cites the Resolución de 4-1-2010 (nóminas), not saved; conv2022 sup. II 8 (which
  habilitación pays after a change of post) has no text in `sources/`.

## V.5 — `m05-l05`

- **Tally** (18 questions classified V.5, all on ACF or PAJ, owned by m05-l03; plus 11 classified V.2 that test the
  clasificación económica of V.5's first three items, where this lesson spends its words).
- **Structure:** clasificación económica (Resolución de 20-01-2014, anexo IV; the same codes in anexo II of the Orden
  HAC/557/2026): capítulo 2, capítulo 6, capítulos 4 and 7 with inclusions and exclusions; pagos: concepto y tipos, pagos por
  obligaciones presupuestarias (cross-reference m05-l03 for propuesta, ordenación and realización), the other kinds named
  (anticipos de caja fija, pagos a justificar, extrapresupuestarios, en formalización); justificación de libramientos (arts.
  73.4, 79.3–4 LGP; regla 61.1 IOC).
- **Glossary (5):** clasificación económica (origin m05-l02), gastos corrientes en bienes y servicios, inversiones reales,
  transferencias corrientes, transferencias de capital.
- **Lo que más cae sources:** 1 conv2025_X sup. I 7, conv2022_X P1 21; 2 conv2022_X P1 24, conv2022_X sup. II 11 (anulada); 3
  conv2025_X sup. II 10, conv2022_X sup. I reserva 1, conv2022_X sup. II 14; 4 conv2025_X sup. I 6, conv2025_A sup. I 8; 5
  conv2024_X sup. II 8; 6 conv2022_X sup. I 5; 7 conv2024_A P1 36; 8 conv2024_A sup. II 18; 9 conv2025_A sup. II reserva 3.
- **Listed:** articles 43 and 73 have different names in the 2014 Resolución and the 2027 Orden; the lesson names neither.
  No text in `sources/` defines «pago en firme»; the lesson says so and quotes the two uses (regla 59 bis IOC; RD 640/1987
  disposición derogatoria). Regla 88 IOC calls transferencias «no condicionadas», and capítulos 4 and 7 say «condicionados o
  no»: both are stated. Apartado primero.2 Orden PRE/1576/2002 still cites art. 65 TRLGP.
- **ACF/PAJ points m05-l03 does not cover** (candidates for a later round): art. 79.6 LGP (cuenta approved or reparada in two
  months; conv2020 P1 38), the rest of art. 79.3 LGP, art. 78.5 LGP, apartado noveno.2.5 Orden PRE/1576/2002, apartado
  décimo.1 Orden de documentos contables, regla 64.2 IOC.

## V.6 — `m05-l06`

- **Tally** (22 questions): art. 198.4 LCSP 3, art. 34.1 LGS 2, regla 77.1 IOC 2 (m05-l03), regla 77.7, 42.2.b), 86.3 IOC 1
  each, anexo I nota 34 1, arts. 10, 8.1, 5.1 LGS 1 each, art. 151.e) LGP 1 (m05-l03), art. 2.4 LGS 1 (m03-l05), LCSP arts. 106,
  107, 108, 29.2, 193.3, 101 6 (m03-l04). No 2022–2025 question asks justificación, pagos anticipados, garantías or reintegro;
  those sections are short.
- **Structure:** contratos: expediente de gasto and tramitación anticipada (art. 117.2 LCSP; regla 42 IOC), documentos
  (cross-reference m05-l03; regla 77.7 IOC on resolución), pago del precio (art. 198.4 LCSP, with a worked date: acta lunes
  03-05-2027 → miércoles 02-06-2027; factura martes 18-05 → jueves 17-06-2027); subvenciones: plan estratégico (art. 8.1 LGS),
  requisitos (art. 9), competencia (art. 10, the 12 millones de euros threshold), gasto and pago (art. 34.1–4, the pago
  anticipado and its «en ningún caso» exclusions), justificación (art. 30), reintegro (arts. 37.1 «entre otros», 39.1, 42.4),
  documentos (regla 86 IOC; anexo I nota 34). LGS cambio pendiente: Ley 4/2026 only adds art. 2.4.j), which the lesson does not
  cite; the Normativa line keeps the note.
- **Glossary (2):** plan estratégico de subvenciones, pago anticipado.
- **Lo que más cae sources:** 1 conv2024_A P1 37, conv2025_X sup. II 15; 2 conv2025_X sup. II 16; 3 conv2025_A P1 39; 4
  conv2022_X sup. I 20; 5 conv2024_A sup. I 18, conv2024_X P1 40; 6 conv2022_X P1 27; 7 conv2025_A P1 40; 8 conv2024_A sup. I 17;
  9 conv2025_A P1 reserva 1.
- **Cuts of note:** arts. 105, 117.1, 118.3, 198.3, 198.8, 199, 210.4, 240, 243 LCSP; arts. 34.5, 37.1.d)–i), 38.2, 39.2–3, 40,
  41.1, 42.5, 44.3 LGS; arts. 56, 70.1, 71.2 RLGS; reglas 42.3–4, 77.4–6, 78, 83–85, 87 IOC. Arts. 56 RLGS and 44.3 LGS were
  asked only in 2020.
- **Listed:** art. 42.4 LGS lets the reintegro plazo be suspended and extended under art. 42.5–6 of the repealed Ley 30/1992
  (quoted as written). Art. 36.1.b) LGS refers to «artículo 60» LGP, today the anticipos de tesorería. The interés de demora of
  subvenciones in force on 17-10-2026 is in no source (DA 42.ª Ley 31/2022 set 4,0625 % until 31-12-2023); the art. 38.2
  sentence was cut. Reglas 42.1, 77.1, 85–87 IOC cite repealed texts. Art. 198.4 LCSP counts the factura plazo «desde» and the
  others as «siguientes».
- **Overlaps left for a later pass (convention 3):** m03-l04 restates art. 198.4 LCSP, which the scope gives to m05-l06; m05-l03
  repeats the RC de «tramitación anticipada» (regla 42.2.b) IOC) and the art. 151.e) LGP exemption that m05-l06 also states.

## course.yaml

- Lesson summaries m05-l01…m05-l06, three sentences each, from the writers' notes as fixed after review. Every sentence was
  checked by its tema's reviewers (pass 1: 9 FAIL in all, fixed with the reviewer's wording); the later passes and the
  closing check covered the changed ones.
- Module summary for m05, two sentences, in the m01–m04 shape; it names topics only.

## Checks and suites (bloque V)

Run on the final tree (lessons, glossary, course.yaml, goldens, normativa.yaml, fuentes.yaml and saved sources of this
round, and the two bloque IV fixes):

- **Pipeline, course as draft:** loads and validates. `pytest -k "glossary or registry or content or pipeline"`: 68
  passed, including the never-coins checks for glossary and summaries. `figure steps per course`:
  `age-administrativo-c1: no figures`, `crypto-futures: 34 figures`, `fixture-oposiciones: no figures`.
- **Backend (`uv run pytest`):** 1,374 passed, 20 skipped, 4 warnings.
- **Frontend (`npx vitest run`):** 563 passed, 49 skipped, including the list-shape guard and the regenerated goldens;
  `tsc -b` clean.
- **Goldens:** `glossary-links.es.txt` (292 web marks) and `lesson-refs.es.txt` (86 references, 0 dangling) regenerated
  and read line by line (see Glossary). No diff under `content/crypto-futures/` or `dist/`.
- **Android bundle:** re-exported, fingerprint unchanged `9c95cf4a6bf2…` (98 files); `--verify-only` OK, leaked tokens OK.
- `README.md` (course status line) now says the theory of bloques I to V is written.

## Open items (after bloque V)

- **After the 29-11-2026 elections:** the «hoy» re-check round also covers m05-l02 (Ministerio de Hacienda, art. 5.1 RD
  829/2023) and m05-l03 (Ministerio de Economía, Comercio y Empresa, art. 15.A).1.º RD 1009/2023).
- **Budget law.** If a Ley de PGE for 2027 is published before the exam, m05-l01 (the dated budget-in-force statement),
  m05-l02 (every Ley 31/2022 article cited), m05-l04 (the 2026 amounts and art. 32.Tres) and the course.yaml summaries of
  m05-l01, m05-l02 and m05-l04 change. The 2027 retribution amounts (SEPG tables for 2027) and the conditional 0,5 % of
  art. 2.2 RDL 14/2025 (payable in the first quarter of 2027) need a check before R3 asks them.
- **Indemnizaciones.** The Government announced a revision of the RD 462/2002 amounts (press, September 2026; not a source).
  If a Resolución or Orden is published, m05-l04's anexo II, kilometraje and anexo IV tables change, and so do their glossary
  entries.
- **Exams ledger (R3), from this bloque:** conv2024_X sup. I 4 (transfer 220 → 202: official key titular del ministerio,
  the articles give it to the Ministro de Hacienda; candidate «Clave oficial discutida»); conv2025_X sup. I 12 and conv2022
  sup. II 11 (retención previa, supported by regla 6.1 IOC); conv2022 sup. II 9 (no capítulo 2 figure to check the 7 %);
  conv2024_X sup. II reserva 5 (RC «más el IVA» rests on the LCSP); conv2022 P1 25 (Resolución de 4-1-2010 on nóminas, not
  saved); conv2022 sup. II 8 (no text on which habilitación pays).
- **Overlaps (convention 3):** m03-l04 restates art. 198.4 LCSP (owner m05-l06); m05-l03 and m05-l06 both state regla 42.2.b)
  IOC and art. 151.e) LGP. A later cleanup pass keeps each in one lesson.
- **Not saved, cited by no sentence:** the Resolución de 4-1-2010 (nóminas), the Orden HFP/535/2022 (elaboración of the
  PGE 2023), the interés de demora of subvenciones in force (no source after DA 42.ª Ley 31/2022). Save one before a question
  rests on it.
- **Cut for length, candidates if a later round has room:** art. 74.4 LGP and regla 55.1 IOC (m05-l03); art. 10.Cinco Ley
  31/2022 and art. 47.4–6 LGP (m05-l02); the RDL 6/2023 complementos de desempeño y de carrera (m05-l04); art. 79.6 LGP and
  the other ACF/PAJ points listed under V.5; art. 38.2 and 39.2 LGS (m05-l06).
- **Bloque IV leftovers:** m04-l07 is 39 words over its 2,400 ceiling, and m04-l09 is at 2,401. m04-l08 line 208 runs past
  the wrap width. The IV.4 summary wording «el Reglamento de Situaciones Administrativas» was not re-read.
- **Waiting glossary terms:** the bloque I–IV lists, plus crédito ampliable, incorporación de crédito, acreedor directo and
  prórroga presupuestaria.

## Where to resume (after bloque V)

Bloque V is closed. The next session starts R2 bloque VI (temas VI.1–VI.8, lessons `m06-l01`…`m06-l08`), the short
list-shaped ofimática lessons of R4.3 (600–1,500 words), built on the ofimática index (`docs/age-ofimatica-index.md`).
The spec carries over with two additions from this bloque: every replacement applied after a lesson's last blind pass
gets one more blind check before the bloque closes, and multi-word glossary terms get head-noun plural `match` forms when
they are added.

# Bloque VI — temas VI.1–VI.8

Round R2, bloque VI, 2026-10-17. Nothing committed. One writer per tema to a shared spec (`spec-bloque-vi.md`): sources
are saved official pages only (Microsoft's Spanish documentation for Windows 11 and Microsoft 365 desktop; for VI.1 and
the internet, mail and security items an official or standards-body page), each saved under `sources/otros/` before it
is cited and indexed in `fuentes.yaml`; every list item ends with «(fuente: `file`)»; a «Fuentes» block replaces
«Normativa» as the last section; lessons are list-shaped, 600–1,500 words. Then a blind verifier per tema, who had not
written the lesson, checked every item field by field (label, path, shortcut, behaviour, default) against the saved
page, the sha256 of every file, a re-download of one page in five (article text compared, not bytes), and coverage
against the ofimática index, the exams ledger and the programme. The writer of tema N+1 drafted while tema N was in
review. Every edit applied after a tema's pass was re-checked blind by the next tema's verifier (VI.1 edits in the VI.2
pass, and so on). A closing blind check covered the last edits (VI.8), all course.yaml summaries of m06, the 43 m06
glossary entries and the 11 m06 lines of `glossary-links.es.txt`: 73/73 PASS. The per-item tables, the writer spec and the
writers' notes are kept in `docs/age-verification/bloque-vi/` (decision 1 below).

Notation in this section: «2025 A 44 / B 41» = 2025 ordinaria, modelo A question 44, modelo B question 41; «2025 X» =
extraordinaria; «2022» and «2020» alone = ordinaria; P1R = reserve question of part 1.

## Prompt decisions for this bloque

- **incibe.es** rejects a bare `-A "Mozilla/5.0"`: pages were downloaded with a full Firefox user agent plus `Accept`
  and `Accept-Language: es-ES` headers.
- **Accepted as official:** NIST (government standards body) for the IEC binary prefixes, because iec.ch blocks
  automated access (AWS WAF challenge); a vendor's own support page for its own product (Apple for macOS; the
  www.microsoft.com Paint product page); the Basque Government web-service page for «Diseño adaptable»; the Council
  register copy (doc. 12092/23) of COM(2023) 442 final, because EUR-Lex answers with a WAF challenge; the Internet
  Society history page, ISOC being the IETF's organisational home (authors Leiner, Cerf, Kahn et al.). The W3C HTML 4.01
  chapters 2 and 18 were first cited for HTML and client-side JavaScript; after the close they were replaced by the
  WHATWG HTML Standard (see «Decisions after bloque VI»).
- **Not used:** RAE dictionary, Microsoft Q&A and Community forums, academies, blogs, Wikipedia, the FSF page, MDN and
  WHATWG.
- **«&» labels** (Microsoft's Spanish pages print «Privacidad & seguridad», «Importar & vínculo»): written as printed,
  never silently as «y»; the «y» form is listed below as not confirmed.
- **Singular or plural the page does not print = not confirmed** (exam «Gráficos modernos» against the page's «Gráfico
  moderno»).
- **«Lo que más cae»** lines state facts the exams asked, not neighbouring facts from the same page; most repeated index
  families first.
- **«Fuentes» replaces «Normativa»** in m06. The ENS stays cited by its file in `sources/normativa/`
  (`BOE-A-2022-7191_ens_2024-11-06.pdf`, m06-l01), not copied to `sources/otros/`.
- **Outlook:** Microsoft 365 desktop has two clients; items that differ name theirs («Outlook clásico», «nuevo
  Outlook»).
- **Garbled paths.** Microsoft's machine-translated Spanish prints «X del sistema>», «Información de>archivo>». A path
  is written in reading order only when every label is on the page and the order is printed plainly on that page or
  another saved page; otherwise the item gives the labels without the path.

## Saved sources (bloque VI)

173 new files in `sources/otros/`, all indexed in `fuentes.yaml` with URL, title, consultado 2026-10-17, sha256 and the
lessons citing them (167 HTML, 4 PDF, 2 TXT). sha256 re-run on all 173 when this section was drafted: all match; no file
in the folder is unindexed and no entry lacks its file. No file saved before bloque VI is cited by m06.

| Domain | Files |
|---|---|
| support.microsoft.com | 135 |
| learn.microsoft.com | 22 |
| azure.microsoft.com | 2 |
| www.microsoft.com | 1 |
| www.w3.org | 2 |
| www.rfc-editor.org | 2 |
| physics.nist.gov | 1 |
| www.incibe.es | 1 |
| www.boe.es | 1 |
| support.apple.com | 1 |
| www.internetsociety.org | 1 |
| data.consilium.europa.eu | 1 |
| www.dominios.es | 1 |
| www.euskadi.eus | 1 |
| www.aepd.es | 1 |
| **Total** | **173** (160 Microsoft) |

New files by tema: VI.1 25, VI.2 20, VI.3 19, VI.4 26, VI.5 31, VI.6 18, VI.7 20, VI.8 14.

**Reused within the bloque** (one file, two lessons in its `lessons` list): `incibe-glosario-ciberseguridad.pdf` (l01,
l08), `ms-win-atajos.html` (l02, l03), `ms-onedrive-restaurar.html` (l02, l03), `ms-win-menu-inicio.html` (l02, l08),
`ms-office-pdf.html` (l04, l06), `ms-office-barra-acceso-rapido.html` (l04, l05). Plus the ENS from
`sources/normativa/`. Fuentes lines in the eight lessons: 180 = 173 new + 6 reuses + the ENS.

**Re-downloads** (one in five, per tema): 5, 4, 5, 6, 7, 5, 4 and 4 files, 40 in all. Each returned HTTP 200 at the
fragment URL with the same article text (the INCIBE PDF and RFC 1122 byte-identical).

Pages downloaded, cited in a draft and then removed from `sources/otros/` when the item was cut stay out of the index
(VI.1: Office suites, Azure MySQL, data mining, Espacios de almacenamiento; VI.7: Outlook charts, Limpieza de
conversación, Correo no deseado, carpetas de búsqueda, grupos de envío y recepción).

## Summary

| Tema | Lesson | Words | Items | Fuentes | Pass 1 checks | FAIL (fixed) | Re-check of post-pass edits | Glossary |
|---|---|---|---|---|---|---|---|---|
| VI.1 | `m06-l01` | 1,498 | 33 | 26 (25 + ENS) | 62 | 1 (glossary) | 2/2 PASS (in VI.2) | 7 |
| VI.2 | `m06-l02` | 1,497 | 35 | 20 | 53 | 3 (2 items, LQMC 1) | 4/4 PASS (in VI.3) | 6 |
| VI.3 | `m06-l03` | 1,494 | 35 | 21 (19 + 2 reused) | 75 | 5 (2 items, LQMC 1, LQMC order, glossary 1) | 4/4 PASS (in VI.4) | 5 |
| VI.4 | `m06-l04` | 1,480 | 33 | 26 | 53 | 3 (2 items, summary) | 4/4 PASS (in VI.5) | 6 |
| VI.5 | `m06-l05` | 1,498 | 35 | 32 (31 + 1 reused) | 55 | 3 (1 item, LQMC order, summary) | 5/5 PASS (in VI.6) | 3 |
| VI.6 | `m06-l06` | 1,477 | 33 | 19 (18 + 1 reused) | 52 | 5 (4 items, LQMC 1) | 5/5 PASS (in VI.7) | 5 |
| VI.7 | `m06-l07` | 1,489 | 26 | 20 | 63 | 4 (3 items, Fuentes 1) | 4/4 PASS (in VI.8) | 5 |
| VI.8 | `m06-l08` | 1,471 | 32 | 16 (14 + 2 reused) | 66 | 2 (1 item, LQMC order) | 2/2 PASS (closing check) | 6 |
| **Total** | | **11,879** | **262** | **180** | **479** | **26** | **30/30** | **43** |

Words: `wc -w` on the final file, everything counted. Items: `- ` lines in the programme sections; each lesson also has
exactly ten «Lo que más cae» lines. Pass 1 checks: the rows of each `verify-pass1.md` (items, LQMC, Fuentes and
fragment, summary, glossary, form). The closing check adds 73 rows (10 queue items, 9 summaries, 43 glossary entries, 11
link lines), all PASS.

**FAIL classes** (26 in the pass-1 files):
1. **Label not confirmed / «&» written as «y»** (7): VI.3 «Privacidad y seguridad»; VI.4 «Vista › Macros › Grabar
   macro»; VI.6 «Archivo › Información» (Compactar), «Gráficos modernos», «Agrupar y ordenar», «Importar y vincular»;
   VI.7 Fuentes title «requisitos, limitaciones y pasos».
2. **Claim broader than the page** (7): VI.2 Acoplar («a un borde»; the page says left or right edge); VI.4 Historial de
   versiones (skipped «Abrir versión»); VI.5 Fechas (dropped «de manera predeterminada»); VI.7 Acceso delegado (dropped
   «o con Exchange Online»), Búsqueda (Ctrl+Mayús+P without its client), Responder y Reenviar («los incluye» lost the
   attachments); VI.8 JavaScript (only «al cargar la página»).
3. **Citation on the wrong page** (3): VI.2 Varios escritorios («Nuevo escritorio» is on `ms-win-escritorios.html`),
   VI.2 LQMC 1 («de forma predeterminada» is on `ms-win-barra-tareas.html`), VI.3 LQMC 1 («Ver» is on
   `ms-win-explorador.html`; also dropped «listas»).
4. **LQMC order or LQMC not the asked fact** (4): order not by family size in VI.3, VI.5, VI.8; VI.6 «la regla de
   registro compara campos» was not what 2020 X 58, 2022 42 or 2020 X 60 asked.
5. **Contradiction between two official pages** (1): VI.3 Recortes stated Impr Pant per `ms-win-recortes.html` (whole
   screen to the clipboard) against m06-l02's `ms-win-atajos.html` (select an area). Clause dropped in m06-l03.
6. **Summary term absent from the lesson** (2): VI.4 «la barra de acceso rápido»; VI.5 «los valores de error» and
   «impresión».
7. **Glossary match or term** (2): VI.1 g-doble-factor-de-autenticacion matched «autenticación multifactor» (match
   removed); VI.3 g-registro-de-windows, a term no page or lesson prints (replaced by g-editor-del-registro).

## Glossary

- 49 candidates proposed (VI.1 7, VI.2 6, VI.3 7, VI.4 6, VI.5 5, VI.6 6, VI.7 6, VI.8 6), all PASS in review after the
  two replacements below.
- **Dropped, to the waiting list** (6): only the plural appears in prose, so the singular entry would not link —
  g-extension-de-nombre-de-archivo (m06-l03), g-ruta-unc (m06-l03), g-referencia-estructurada (m06-l05),
  g-consulta-de-accion (m06-l06), g-grupo-de-microsoft-365 (m06-l07); g-referencia-absoluta (m06-l05): the term is not
  in the prose at all.
- **43 added**, origin m06; `glossary.yaml` holds 277. Each definition follows its saved page and ends «(fuente: file)».
  Multi-word terms carry head-noun plural `match` forms.
- **Replacements in review:** the `match` «autenticación multifactor» was removed from g-doble-factor-de-autenticacion
  (Microsoft's MFA is two or more factors; the entry is INCIBE's two-factor sense); g-registro-de-windows →
  g-editor-del-registro (`ms-win-herramientas-sistema.html`).
- **`link_except` added:** g-plantilla in m01-l10 («plantilla de personal»); g-informacion-general in m06-l05 (a Fuentes
  title, «Información general sobre fórmulas en Excel»); g-acceso-directo in m06-l04 (keyboard access keys of the
  ribbon); g-acceso-rapido in m06-l02 (a definition sentence), m06-l04 and m06-l05 (inside «Barra de herramientas de
  acceso rápido»).
- **Goldens.** `glossary-links.es.txt` regenerated and read line by line: 292 → 303 web marks (79 → 80 also a PDF link);
  «linkable terms the book never links» 155 → 197. The 11 new marks (m06-l02 1, m06-l03 5, m06-l06 1, m06-l08 4) all use
  the entry's sense (closing check part 3b). `lesson-refs.es.txt` unchanged.

## VI.1 — `m06-l01`

- **Tally** (33 rows filed VI.1 first, 7 of them 2020): index families Hardware, memoria y almacenamiento (13 q),
  Seguridad (6), Software, nube y otros conceptos (6), Sistemas operativos (4), Bases de datos (conceptos) (2). Rows
  where VI.1 is only the bracketed alternative belong to VI.2, VI.3, VI.6, VI.8 or II.3.
- **Structure:** four `##` with the programme's words. Hardware y software: CPU, RAM, caché, bit y byte, múltiplos del
  byte (NIST), requisitos de Windows 11, BIOS y UEFI, Plug and Play, dispositivos de entrada, router, aplicación de
  fuentes abiertas (ENI), SaaS, VDI, SGBD. Almacenamiento: HDD/SSD, NTFS, sistemas de archivos de Windows, RAID, nube,
  Copias de seguridad de Windows. Sistemas operativos: ejemplos, funciones del kernel. Seguridad: malware, virus, gusano
  y troyano, antivirus, cortafuegos, phishing, CAPTCHA, certificado digital, contraseña robusta, autenticación
  multifactor, actualizaciones, ENS (arts. 2.1, 26; op.acc.6). No shortcuts, so no key-notation line.
- **Glossary (7):** malware, cortafuegos, phishing, copia de seguridad, doble factor de autenticación, SaaS, NTFS.
- **Lo que más cae sources:** 1 2025 A 44 / B 41, 2020 43; 2 2025 A 43 / B 42; 3 2025 A 41 / B 44; 4 2024 X 41, 2024 A
  41 / B 45; 5 2022 X 51 (and 46); 6 2022 70; 7 2025 A 42 / B 43; 8 2024 X 42, 2020 P1R 5; 9 2024 X 43, 2020 X 42; 10
  2024 X 44.
- **Pass 1:** G5 g-doble-factor-de-autenticacion `match` «autenticación multifactor» → removed. Applied as well (a
  verifier note, not a FAIL): RAID now says «en Espacios de almacenamiento directo (Windows Server)».
- **Labels not confirmed:** none. `ms-win-firewall.html` and `ms-win-antivirus.html` print «Firewall & protección de
  red» and «Protección contra amenazas & virus» in their steps; the lesson uses the forms of the same pages' titles
  («Firewall y protección de red», «Protección contra virus y amenazas»).
- **Not documented:** disipador (2025 X 41); escáner as input and impresora as output device (2024 A 41 / B 45);
  «software libre» by that name (2025 X 42: the lesson uses the ENI's «aplicación de fuentes abiertas»); chat de IA /
  ChatGPT (2024 A 65 / B 61, filed «VI.1 (o VI.8)»: no official Spanish page; Copilot is in VI.2); Linux and Android as
  operating systems (2020 41); a hardware definition of the caché beyond the L2/L3 property of `Win32_Processor`.
- **Retired:** none described. BIOS is answered with UEFI, which «reemplaza a la antigua interfaz de firmware del BIOS»
  (`ms-win-uefi.html`).
- **Cuts:** Office desktop applications (2024 A 43), MySQL as a database engine (2020 41), minería de datos (2020 X 43),
  Espacios de almacenamiento levels; GPU line, INCIBE «software» definition, binary prefixes beyond GiB, NTFS 8 PB
  limit, Authenticator 30-second code, Defender scan types, router home-LAN clause.
- **For the exams ledger:** 2024 A 65 (chat de IA) has no owner lesson; decide VI.1, VI.2 or VI.8.

## VI.2 — `m06-l02`

- **Tally** (29 rows, 8 of them 2020, 5 on retired features): Atajos de teclado de Windows, Funciones del sistema,
  Accesos directos, Notificaciones/concentración/escritorios, Configuración y cuentas, Información del sistema, Menú
  Inicio y anclaje, Varias pantallas, IA y Copilot, Accesibilidad, Papelera de reciclaje, Búsqueda en Windows.
- **Structure:** El entorno Windows. Fundamentos (Configuración, Opciones de inicio de sesión / Windows Hello, Versión,
  Narrador, Lupa, Acceso por voz); Ventanas, iconos, menús contextuales, cuadros de diálogo (maximizar y cerrar,
  Alt+Tab, Acoplar, Diseños de ajuste, menú contextual, cuadros de diálogo); El escritorio y sus elementos (iconos,
  acceso directo, Papelera, barra de tareas, widgets y Configuración rápida, centro de notificaciones, No molestar,
  varios escritorios, varias pantallas, captura de pantalla); El menú Inicio (abrir, posición, estructura, anclar,
  búsqueda); Copilot (abrir, qué es, frente a un buscador, Copilot en Word, Excel y Outlook). Intro states the key
  notation.
- **Glossary (6):** barra de tareas, menú Inicio, acceso directo, Papelera de reciclaje, Windows Hello, Microsoft
  Copilot.
- **Lo que más cae sources:** 1 2025 X 44, 2024 X 70, 2025 A 67 / B 67; 2 2025 A 45 / B 45; 3 2025 A 46 / B 46, 2025 X
  45; 4 2024 A 50 / B 50, 2024 A 66 / B 66, 2020 47; 5 2022 47, 2022 X 47; 6 2025 X 47; 7 2022 X 48, 2020 50; 8 2022 X
  45; 9 2022 45; 10 2022 X 50, 2020 X 44 (also 2025 X 48, filed VI.3).
- **Pass 1:** Acoplar «a un borde» → «al borde izquierdo o derecho… o a una esquina para que ocupe un cuarto»; Varios
  escritorios «Vista de tareas › Nuevo escritorio» re-cited to `ms-win-escritorios.html`, Windows+Ctrl+D to
  `ms-win-atajos.html`; LQMC 1 second source `ms-win-barra-tareas.html` for «de forma predeterminada». Cambiar de
  ventana lost a parenthesis for words.
- **Labels not confirmed:** no label is missing from its page; seven paths are decoded from garbled strings (see Open
  items). Windows+A: `ms-win-atajos.html` says it opens «el Centro de actividades de Windows 11»,
  `ms-win-barra-tareas.html` the Configuración rápida; the lesson follows the taskbar page («Centro de actividades» is
  the Windows 10 name).
- **Not documented:** Modo Dios (2022 46): only Q&A threads and Windows 7 archive pages.
- **Retired:** Cortana (one line: retired spring 2023, `ms-cortana-fin-soporte.html`); Reconocimiento de voz → Acceso
  por voz (item kept, replacement line cut); Asistente de concentración, Centro de actividades and live tiles appear
  only in Windows 10 parts of the pages and are not described; Correo y Contactos (2024 X 49) not mentioned.
- **Cuts:** idiomas para mostrar, voz y teclado (2024 X 48); Registro (2024 X 51, now in m06-l03); Otros usuarios (2024
  X 49); Foco, Windows+L / Ctrl+Alt+Supr, Copilot Chat, Copilot data permissions, escala/resolución detail, Windows+X,
  Alt+arrastrar, «Resumir un archivo».
- **For the exams ledger:** 2020 44 and 2020 51: every saved Spanish page says «Configuración › Sistema › Acerca de»
  (`ms-win-version.html`, `ms-win-atajos.html`), not «Información». 2022 X 45: «Escritorios» is now confirmed
  (`ms-win-escritorios.html`, «Expanda Escritorios»). Impr Pant: m06-l02 now states both official descriptions (see
  «Decisions after bloque VI»).

## VI.3 — `m06-l03`

- **Tally** (37 rows filed VI.3 first or bracketed, 9 of them 2020; 1 annulled, 4 on retired features; rows owned by
  VI.1 and VI.2 are listed, not repeated): Explorador de archivos (10 q), Atajos de teclado (8), Herramientas del
  sistema (6), Accesorios: WordPad y Bloc de notas (4), Búsqueda en Windows (3), Papelera (2), Información del sistema,
  Accesos directos.
- **Structure:** El Explorador de archivos (abrir, diseños, extensiones y elementos ocultos, extensión, teclas, menú
  contextual, rutas UNC); Gestión de carpetas y archivos (crear/renombrar/eliminar, arrastrar, Enviar a y comprimir,
  compartir en red local, Papelera); Operaciones de búsqueda (cuadro, indexación, Buscar en Windows, AQS); «Este equipo»
  y «Acceso rápido» (Inicio, Acceso rápido, Este equipo, Asignar unidad de red, Acerca de); Accesorios (Bloc de notas,
  encabezado y pie, Recortes, Grabadora de pasos, Paint, Calculadora, Reloj, Asistencia rápida); Herramientas del
  sistema (Herramientas de Windows, Administrador de tareas, Visor de eventos, Editor del Registro, Unidad de
  recuperación, Historial de archivos).
- **Glossary (5):** Explorador de archivos, Acceso rápido, indexación, Editor del Registro, Historial de archivos.
- **Lo que más cae sources:** 1 2025 A 48 / B 50, 2020 46; 2 2022 X 49; 3 2020 49; 4 2024 A 47 / B 47, 2020 X 48, 49,
  50, 2024 X 54; 5 2025 X 46, 2024 A 49 / B 49; 6 2024 X 58; 7 2020 X 51; 8 2024 A 51 / B 55; 9 2024 X 57; 10 2025 X 50.
- **Pass 1:** Buscar en Windows path → «Configuración › Privacidad & seguridad › Buscar en Windows» (as printed);
  Recortes Impr Pant clause dropped (contradiction with m06-l02); LQMC 1 re-cited to both Explorer pages, with «listas»;
  LQMC reordered by family size; g-registro-de-windows → g-editor-del-registro.
- **Labels not confirmed:** «Iconos muy grandes», «Mosaicos», «Lista» (singular), «Ordenar» and «Más», «Estándar»
  (Calculadora), «Privacidad y seguridad» (see Open items).
- **Not documented:** Ctrl+Mayús+arrastrar creates a shortcut (2025 X 48: the official page gives Alt+arrastrar); «Este
  equipo › Propiedades» opens Configuración › Sistema (2025 A 49); the contents of Herramientas de Windows (2022 48:
  screenshot only); Detalles shows the most information (2020 46); sorting by fields not shown (2024 X 55); the «Enviar
  a» destinations (2024 X 56: only Carpeta comprimida here and Escritorio in m06-l02).
- **Retired:** WordPad (removed from 24H2), Grabadora de pasos (no longer updated, Recortes recommended), Herramientas
  administrativas → Herramientas de Windows: one line each, sourced. Explorer ribbon (2024 X 53) not described.
- **Cuts:** window parts, Ctrl+Mayús+1…9, tabs, Alt+Flecha arriba, Mayús+F10, selection keys; 24H2 archive formats;
  \\localhost and «Volver a conectar»; cloud search; index timing and size; Acerca de contents; Recortes autosave, OCR
  and Retraso; Paint layers; Calculadora converters and «Mantener en la parte superior»; Reloj presets; msinfo32,
  MSConfig, compmgmt.msc, eventvwr.msc, regedit run commands; OneDrive cloud deletes; LQMC Restaurar and Unidad de
  recuperación.
- **For the exams ledger:** 2024 X 52: «Herramientas de Windows» confirmed (`ms-win-herramientas-windows.html`), which
  closes «Sin confirmar en la interfaz española». 2024 X 57: the setting prints «Privacidad & seguridad». 2025 A 48: the
  Spanish page does not print «Iconos muy grandes» or «Mosaicos». Impr Pant: `ms-win-recortes.html` says it captures the
  whole screen to the clipboard, `ms-win-atajos.html` that it lets you select an area; m06-l03 states neither.

## VI.4 — `m06-l04`

- **Tally** (30 rows, 7 of them 2020; 2 annulled, 1 on a retired feature): Interfaz (7 q), Formato de texto, imágenes y
  objetos (4), Pestaña Revisar (4), Leer en voz alta / Transcribir (3), Estilos, índices, notas (3), Colaboración en
  línea, Impresión, Plantillas, Atajos de Word (2 each), Combinar correspondencia (1).
- **Structure:** Principales funciones y utilidades (Sugerencias de teclas, barra de estado, Contar palabras, Mostrar u
  ocultar ¶, panel de navegación, ortografía, sinónimos y mayúsculas, Traducir, Lectura en voz alta, Transcribir,
  coautoría, combinar correspondencia, macros); Creación y estructuración (tabla de contenido, índice, notas, espaciado,
  delimitador, recorte de pantalla, saltos de sección, encabezado/pie/números, tablas); Gestión, grabación, recuperación
  e impresión (Archivo, formatos, Autoguardado, Historial de versiones, Autorrecuperación, PDF, Imprimir);
  Personalización (barra de herramientas de acceso rápido, cinta, ubicación predeterminada, marcas). Only function keys,
  Alt sequences and locale-independent combinations, plus Ctrl+B for the panel de navegación.
- **Glossary (6):** plantilla, macro, combinación de correspondencia, Autoguardado, Autorrecuperación, coautoría.
- **Lo que más cae sources:** 1 2024 A 52 / B 54; 2 2024 A 53 / B 53; 3 2024 X 61, 2024 X 60; 4 2025 A 51 / B 51; 5 2025
  X 51; 6 2022 X 53, 2020 54, 2025 A 53 / B 53; 7 2024 A 54 / B 52, 2024 A 55 / B 51; 8 2022 51, 2022 X 55; 9 2022 52,
  2025 X 55; 10 2025 A 54 / B 54 (2020 53, annulled, same family).
- **Pass 1:** Macros: tab and «Grabar macro» dropped → «el menú Macros tiene «Ver macros» y «Detener grabación»»;
  Historial de versiones → «… › Historial de versiones › Abrir versión › Restaurar»; summary «la barra de acceso rápido»
  → «la barra de herramientas de acceso rápido». Applied as well (a note): Delimitador «ancla» → «anclaje», the page's
  noun.
- **Labels not confirmed:** the Macros tab and button; the Layout tab for Saltos; «Mostrar todo»; «Leer en voz alta»;
  «número de página»; «Visualización» against «Mostrar» (see Open items).
- **Not documented:** the Formato de imagen pane tabs (2020 52); a note's text shown on hover (2025 A 52); cursiva (2025
  A 51: the shortcuts page mixes Ctrl+I and Ctrl+K letter sets); Navegación's Títulos / Páginas / Resultados (2020 X 55,
  only «Ctrl+B opens the panel» is covered).
- **Retired:** Presentar en línea (2020 X 54): not named by the programme, no line; page read, not saved.
- **Cuts:** Inicio › Edición › Seleccionar (2020 X 52); Opciones de impresión in Opciones de Word (2020 53, annulled);
  Alt sequences per tab, Ctrl+F1, Alt+Z, Ctrl+Mayús+E, note and index shortcuts, Ctrl+P, Ctrl+F2, Alt+5; manual table of
  contents; Interletraje; Bloquear anclaje; Autorrecuperación panel; PDF/A; QAT below the ribbon; ribbon export;
  Transcribir formats.
- **For the exams ledger:** 2024 X 60: the button prints «Mostrar u ocultar ¶», not «Mostrar todo». 2020 54 / 2022 X 53:
  current pages say «Lectura en voz alta». 2025 A 53: `ms-word-transcribir.html` gives 300 minutes a month (an option
  said 600) and says Transcribir is in Word desktop only for commercial tenants. 2020 X 53: no saved page ties Macros to
  the «Vista» tab (`ms-word-macros.html` prints «Ver»). LQMC 6 keeps «Transcribir separa oradores»; the verifier's
  alternative («graba en Word o carga un audio», the keyed fact of 2025 A 53) was not applied.

## VI.5 — `m06-l05`

- **Tally** (28 rows, 8 of them 2020; 2 annulled): Otras funciones (7 q), Funciones lógicas y de error (6), Referencias
  (4), Fechas (3), Gestión de datos (3), Celdas y rangos (2), Impresión (2), Validación de datos (1).
- **Structure:** Principales funciones (teclas de acceso, tablas dinámicas); Libros, hojas y celdas (hojas, ocultar,
  proteger hoja y libro, Inmovilizar paneles, rangos no adyacentes, Combinar y centrar, separadores); Introducción y
  edición (edición, fechas, formato personalizado); Fórmulas y funciones (referencias, otras hojas, estructuradas,
  SI/NO/O, SI.ERROR, #N/A, búsqueda e información, contar, texto y fecha); Gráficos (Gráficos recomendados, Alt+F1,
  F11); Gestión de datos (ordenar, Autofiltro, filtro avanzado/duplicados/formato condicional, Subtotales, segmentación,
  Power Query, lista desplegable, Imprimir, Escalar); Personalización (cinta, barra de herramientas de acceso rápido).
  No letter shortcuts.
- **Glossary (3):** referencia relativa, tabla dinámica, segmentación de datos.
- **Lo que más cae sources:** 1 2025 X 58; 2 2020 56, 2025 A 58 / B 55; 3 2022 54; 4 2025 X 57; 5 2022 X 58, 2020 55; 6
  2025 X 56; 7 2025 A 55 / B 58; 8 2025 A 56 / B 57, 2020 X 57; 9 2024 A 58 / B 58; 10 2020 59.
- **Pass 1:** Fechas → «por defecto, el 1-1-1900 es el 1»; CONTARA/CONTAR line moved to the top (largest family);
  summary «los valores de error» and «impresión» → «y el error #N/A» and «…Validación de datos, Imprimir y la cinta».
  Coverage gap closed after the pass: «el punto y coma (;) es el operador de unión: C2:C7;E2:E7»
  (`ms-excel-referencias-estructuradas.html`, 2025 A 57), paid for by cutting «Ctrl+Av Pág y Ctrl+Re Pág cambian de
  hoja» and «con contraseña o sin ella».
- **Labels not confirmed:** «Imprimir selección», «Ajustar todas las columnas en una página», «Vista» against «Ver» for
  Inmovilizar paneles (see Open items). Printed but inconsistent across pages: SI.ERROR / SIERROR, BUSCARV / CONSULTAV,
  #N/A / #N/D, «Segmentación» / «Segmentador»; the category pages print NOT, OR, AND, DAY, XLOOKUP in English.
- **Not documented:** «;» as the argument separator (2022 X 60, MAX); «20-2» read as 20-feb (2024 A 60: the page gives
  «2/2» only); PRUEBA.F.N (2022 53).
- **Retired:** none.
- **Cuts:** PRUEBA.F.N; the function pages for SI, Y, ES, CONTAR, MAX, EXTRAE, DIVIDIRTEXTO, FORMULATEXTO, BUSCARV,
  BUSCARX, FILAS, F4, the #¡DIV/0!, #¿NOMBRE?, #¡VALOR!, #REF! pages, sistemas de fechas 1900/1904, Autorrellenar,
  Relleno rápido, barra de estado, tablas, mover hojas, filtro avanzado, formato condicional, operadores (all read, not
  saved); referencia 3D, sheet names with spaces, Tabla1, Agregar nivel, text/number filters, Alerta de error styles,
  áreas de impresión, scale percentage, F9, .xlsx/.xlsm/.xltx.
- **For the exams ledger:** 2022 54 (SI.ERROR, key disputed): the LQMC line states only the page's behaviour. 2024 A 59
  and 2024 X 62: neither label is printed on a Spanish Microsoft page. 2025 A 57: the «;» union operator is documented
  (`ms-excel-referencias-estructuradas.html`).

## VI.6 — `m06-l06`

- **Tally** (35 rows, 8 of them 2020; 2 annulled, 1 retired): Consultas (7 q), Reglas de validación (6), Otras (5),
  Tablas (4), Claves, índices y relaciones (3), Informes (3), Expresiones (3, 2020 only), Dividir (2), Formularios (1).
- **Structure:** Principales funciones (objetos, límites, Compactar y reparar, módulos, dividir, Gráfico moderno);
  Tablas (tipos de datos, Moneda, Autonumeración y Calculado, formato de Número, propiedades de campo, clave principal;
  `###` Reglas de validación: campo y registro); Consultas (crear y ejecutar, de acción, criterios, parámetros, campo
  calculado, WHERE); Formularios (crear, vistas, subformularios, orden de tabulación); Informes (origen, secciones,
  Agrupación, orden y total); Relaciones (ventana, tipos, integridad referencial); Importación, vinculación y
  exportación (importar o vincular, exportar a Excel, a PDF).
- **Glossary (5):** clave principal, clave externa, integridad referencial, regla de validación, tabla vinculada.
- **Lo que más cae sources:** 1 2024 X 64, 2025 X 61, 2022 61; 2 2025 A 60 / B 60; 3 2025 A P1R 2 / B P1R 2; 4 2025 X
  60; 5 2022 58, 2020 63 (and 2024 X 68); 6 2022 42, 2020 X 60; 7 2025 A 62 / B 62; 8 2025 X 59; 9 2024 A 57 / B 57; 10
  2020 X 59, 2022 X 63.
- **Pass 1:** Compactar: «Archivo › Información» dropped → «con la base abierta o sin abrirla; sin abrirla, desde
  «Herramientas de base de datos»»; «Gráficos modernos» → «Gráfico moderno»; «Agrupar y ordenar» → «Agrupación, orden y
  total»: panel opened from «Diseño de informe › Agrupación y totales»; «Importar y vincular» → «Importar & vínculo»;
  LQMC 6 «la regla de registro compara campos» → «La regla de validación limita los valores que se pueden escribir en un
  campo».
- **Labels not confirmed:** «Indizado», «Requerido», «Divisor de bases de datos», «Introduzca el valor del parámetro»,
  «Origen del control», the Diseño tab for Orden de tabulación, «Gráficos modernos», «Archivo › Información», «Agrupar y
  ordenar», «Importar y vincular» (see Open items).
- **Not documented:** none among the programme phrases. 2024 X 45 (PostgreSQL for a contacts database) has no Access
  feature and no Microsoft page naming it; 2025 A 59 (2.345,68 → Estándar) only as «datos numéricos con decimales».
- **Retired:** «Información» (Tell Me), 2022 56: not named by the programme, not described.
- **Cuts:** Expresiones (2020 61 SiInm, 62 Año, 64 Conmutador; pages read, not saved); parámetros page, índice page,
  grouped reports, origen de registros, Access shortcuts, function list; Número sizes, Sí/No, Texto largo 65.535, 32
  tables per query, 10 fields per key, Autonumeración start, types without rules, Crear tabla overwrite, report tools,
  Detalle, export of macros and modules.
- **For the exams ledger:** 2025 X P1R 2: `ms-access-graficos.html` lists «nubes de palabras» among the chart types and
  has a «Nube de Word» section, so the note «no consta que exista "Nube de palabras"» (and the index note on the five
  chart types) is contradicted and the key (c) is supported. 2022 X 62: the route «Archivo › Información» stays
  unconfirmed; «Herramientas de base de datos» (key a) is printed.

## VI.7 — `m06-l07`

- **Tally** (34 rows filed VI.7 or «VI.7 (o VI.8)», 9 of them 2020; 4 annulled): Búsqueda (8 q), Creación, envío y
  respuesta (7), Organización y configuración (5), Permisos y delegación (4), Limpieza y archivo (3), Grupos (2), Reglas
  (2). 2020 69 (SMTP) is left to VI.8.
- **Structure:** Conceptos elementales y funcionamiento (Outlook, IMAP y POP, S/MIME, grupos de Microsoft 365, permisos
  de carpeta, acceso delegado); El entorno de trabajo (qué cliente usas, vistas, categorías, búsqueda, Buzón actual,
  Limpieza de buzón, Archivar); Enviar, recibir, responder y reenviar (enviar y recibir, Responder y Reenviar, atajos,
  recuperar, programar envío); Creación (mensaje nuevo, importancia alta, firmas); Reglas (regla, crear, mensajes
  existentes); Libreta de direcciones (libreta, grupo de contactos). Items name their client where the two differ.
- **Glossary (5):** IMAP, POP, S/MIME, acceso delegado, lista de contactos.
- **Lo que más cae sources:** 1 2025 A 65 / B 64; 2 2022 X 65; 3 2024 A 61 / B 65; 4 2024 X 69; 5 2025 X 64; 6 2022 65;
  7 2024 A 68 / B 68; 8 2024 X 66 (2025 A 64 / B 65 annulled); 9 2024 A 63 / B 63, 2020 X 67; 10 2024 A 64 / B 62.
- **Pass 1:** Acceso delegado → «exige cuenta profesional o educativa en Microsoft 365 o con Exchange Online»; Búsqueda
  → «en Outlook clásico, Ctrl+E o F3 busca y Ctrl+Mayús+P crea una carpeta de búsqueda»; Responder y Reenviar →
  «Reenviar admite destinatarios nuevos e incluye los datos adjuntos»; Fuentes title of `ms-outlook-recuperar.html` →
  «requisitos, limitaciones & pasos» (also in the fragment).
- **Labels not confirmed:** «Retrasar entrega», «Incluir», «Delegar acceso», «Correo no deseado › Opciones», «Formato de
  texto › Edición › Buscar», público / privado (see Open items). Two paths rest on the reverse-order decode only:
  «Archivo › Herramientas › Limpieza de buzón» and «Configuración › Cuentas › Firmas».
- **Not documented:** «Dirigir respuestas a» (2020 X 65): no Spanish Microsoft page.
- **Retired:** none named by the programme (Correo y Calendario belongs to VI.2).
- **Cuts:** Insertar › Ilustraciones › Gráfico (2020 X 64); Limpiar conversación / carpeta (2020 X 66); Correo no
  deseado levels (2020 X 61); carpetas de búsqueda; send/receive group options (2020 X P1R 1, only Ctrl+Alt+S kept); F4
  in an open item (2020 X 68); vistas path, S/MIME option labels, recall in the new Outlook and the 24-hour retry, the
  120-minute delay rule, Autoarchivar, default importance, rule limits for Gmail/Yahoo/iCloud, «Ejecutar esta nueva
  regla ahora», keytips, new-Outlook list steps, Ctrl+Mayús+L, Alt+S, «Todos los elementos de Outlook».
- **For the exams ledger:** 2024 X 65 («proyecto», key c, «Clave oficial discutida») and 2025 X 66 ("9876", key a,
  `vigente`) are contradicted by `ms-outlook-buscar.html`: prefix matching returns proyecto, proyectos, proyector… «con
  o sin comillas» (option a of 2024 X 65; the same page's table says quotes give the exact phrase, so the page is
  internally inconsistent), and «Las cadenas de números de menos de cinco dígitos se omiten» (a four-digit search
  returns nothing; candidate «Clave oficial discutida» for 2025 X 66). The new Outlook has folder permission levels
  (`ms-outlook-compartir-carpeta.html`, «Uso compartido y permisos»). Delegation in the new Outlook is «solo
  parcialmente disponible» and is assigned from classic Outlook, not from «Configuración › Cuentas»
  (`ms-outlook-delegados.html`). The index notes marked «posible» on both points change.

## VI.8 — `m06-l08`

- **Tally** (32 rows filed VI.8 first or bracketed, 8 of them 2020; 2 annulled): Navegación y servicios web (6 q),
  Lenguajes web (5), Red: IP, DNS, TCP/IP, FTP (5), Correo: protocolos (4, only SMTP filed VI.8 first), Diseño web
  adaptable (2), HTTP y HTTPS (2). Bracketed rows already covered in VI.1, VI.2 and VI.7 (router, SaaS, escritorio
  virtual, Copilot, chat de IA, S/MIME, IMAP/POP) are not repeated.
- **Structure:** Origen, evolución y estado actual (ARPANET, NCP → TCP/IP on 1-1-1983, World Wide Web y HTML, Web 3.0,
  Web 4.0); Conceptos elementales sobre protocolos y servicios (`###` Red: protocolo, TCP/IP, capas, dirección IP,
  direcciones privadas, DNS, ping, HTTP, HTTPS, FTP, SMTP; `###` Servicios: dominio .es, HTML, JavaScript, diseño
  adaptable, alojamiento, spam, CAPTCHA); Funcionalidades básicas de los navegadores (cookie, cookies de sesión y
  persistentes, historial, favoritos, descargas, pestañas, InPrivate, extensiones, anclar un sitio a Inicio; Microsoft
  Edge).
- **Glossary (6):** TCP/IP, dirección IP, DNS, HTTPS, cookie, spam.
- **Lo que más cae sources:** 1 2025 A 68 / B 68; 2 2025 A 69 / B 70; 3 2025 X 69; 4 2024 A 69 / B 69, 2022 X 70, 2020
  70; 5 2020 65, 2020 X 69; 6 2025 X 67, 2024 X 47; 7 2022 X 69, 2022 66; 8 2022 X 64; 9 2025 X 68, 2020 67; 10 2025 X
  70, 2020 68.
- **Pass 1:** JavaScript → «se ejecuta en el equipo del cliente al cargar el documento o con un evento, como activar un
  enlace»; LQMC reordered by family size (Navegación, Lenguajes, Red, HTTP/HTTPS, Diseño adaptable; the last two tie).
  Summary: «En Microsoft Edge» → «En el navegador (Microsoft Edge)» (a verifier note).
- **Labels not confirmed:** «Configuración y más › Más herramientas › Anclar a Inicio», «hosting», «IPv4» / «IPv6»,
  «secuestro de sesión» (see Open items). The layer names, «inicio de sesión remoto», «lenguaje de marcado de
  hipertexto» and «lenguaje de script del lado del cliente» are standard Spanish renderings of English standards text
  (RFC 1122, WHATWG HTML Standard), not UI labels.
- **Not documented:** none. No support.microsoft.com es-es page was found for finding downloads, adding favourites,
  deleting cookies or pinning sites; `ms-edge-atajos.html` covers the shortcuts.
- **Retired:** none.
- **Cuts:** none forced (1,438 words before review). Left out: NSFNET and the 1985 TCP/IP mandate, HTML versions
  2.0–4.01, RFC 1918 block names, DNSSEC, Ctrl+L / Ctrl+Entrar, «Bloquear cookies de terceros», InPrivate search.
- **For the exams ledger:** 2025 A 67: the keyed path «Configuración y más › Más herramientas › Anclar a Inicio» is
  printed on no single page («Configuración y más» is printed as the menu's name on `ms-edge-atajos.html` and
  `ms-edge-inprivate.html`). 2020 66: «hosting» is not printed; INCIBE's entry is «Servidor».

## course.yaml

- Eight lesson summaries m06-l01…m06-l08, three sentences at most (m06-l01 two), in topic-list form, from the writers'
  proposals with the reviewers' corrections: VI.4 «la barra de herramientas de acceso rápido»; VI.5 «…BUSCARV y el error
  #N/A» and «…Power Query, Validación de datos, Imprimir y la cinta»; VI.8 «En el navegador (Microsoft Edge)». Checked
  in each tema's pass 1 and again, sentence by sentence, in the closing check (9 PASS with the module summary).
- Module summary for m06 (new, coordinator's wording), two sentences in the m01–m05 shape; it names topics only.
- **Left as they are** (closing-check notes, non-blocking): the m06-l04 summary's «Estilos» rests only on «Los estilos
  de título forman la tabla de contenido» and «aplica Título 1, Título 2…»; the m06-l06 summary has «Compactar y reparar
  y dividir» (two «y» in a row); g-menu-inicio is marked inside a Fuentes title of m06-l08 («Personalizar el menú Inicio
  de Windows»; right sense, no `link_except`).

## Checks and suites (bloque VI)

Run on the final tree (lessons, glossary, course.yaml, goldens, fuentes.yaml and saved sources of this round):

- **Pipeline, course as draft:** loads and validates. `pytest -k "glossary or registry or content or pipeline"`: 68
  passed, including the never-coins checks for glossary and summaries (the first run failed on six plural-only glossary
  terms, which were dropped; see Glossary). `figure steps per course`: `age-administrativo-c1: no figures`,
  `crypto-futures: 34 figures`, `fixture-oposiciones: no figures`.
- **Backend (`uv run pytest`):** 1,374 passed, 20 skipped, 4 warnings. Same as the baseline at the start of the session.
- **Frontend (`npx vitest run`):** 563 passed, 49 skipped, including the list-shape guard on the eight list-shaped
  lessons and the regenerated goldens; `tsc -b` clean. The baseline run at the start had 1 failure (562 passed): it
  ran while m06-l01 was being written, and the run on the final tree has none.
- **Goldens:** `glossary-links.es.txt` regenerated and read line by line (292 → 303 web marks; wrong senses excluded,
  see Glossary). `lesson-refs.es.txt` regenerated, unchanged (0 dangling). No diff under `content/crypto-futures/` or
  `dist/`.
- **Cross-reference of sources:** every file cited in an m06 lesson is in `sources/otros/` (or the ENS in
  `sources/normativa/`) and indexed in `fuentes.yaml` with a matching sha256; no saved file is unindexed; every Fuentes
  block lists exactly the files its lesson cites, in order of first citation.
- **Android bundle:** re-exported, fingerprint unchanged `9c95cf4a6bf2…` (98 files); `--verify-only` OK, leaked tokens
  OK.
- `README.md` (course status line) now says the theory of all six bloques is written.

## Decisions after bloque VI (2026-10-17)

Taken by Juanjo after reading the close; applied in the same session. Where an earlier paragraph of this section says
otherwise, this one rules.

1. **Audit trail.** The writer spec, the writers' notes, every per-item verification report, the re-check queue and the
   closing checks of this bloque are copied into `docs/age-verification/bloque-vi/` (one file per tema plus the shared
   files; see its README). Bloque IV's and V's working tables were lost with `/tmp`. **From now on every round writes its
   reports directly under `docs/age-verification/<bloque>/`, not in a scratch folder.**
2. **Unconfirmed labels.** The lessons keep the label the official page prints. The table «Etiqueta del examen /
   Etiqueta oficial» under Open items lists all 41, so R3 writes authored questions with the official label and the
   «Exámenes oficiales» set keeps the exam's wording.
3. **Facts with no official source** (Modo Dios, Ctrl+Mayús+arrastrar, PRUEBA.F.N, disipador…): out of the lessons and
   out of the authored bank; the «Exámenes oficiales» set keeps them as asked. Listed under «Sin fuente oficial».
4. **Impr Pant.** m06-l02 states both official descriptions, each with its source, and does not choose (as the TREBEP
   and earlier-rule cases are handled): `ms-win-atajos.html` (select an area, to the clipboard) and
   `ms-win-recortes.html` (the whole screen, to the clipboard). To stay at 1,500 words, m06-l02 lost three clauses: who
   the Narrador is for, two dialog-box keys (Barra espaciadora, Esc) and the desktop right-click › Ver sizes.
5. **Sources outside the list.** NIST, Apple, the Council copy of COM(2023) 442, the Basque Government page and the
   Internet Society are accepted. The W3C HTML 4.01 files are replaced by the current HTML Standard:
   `whatwg-html-introduccion.html` (§1, introduction and history) and `whatwg-html-scripting.html` (§4.12), saved and
   indexed; the two `w3c-html401-*` files are deleted and unindexed. m06-l08's World Wide Web, HTML and JavaScript items
   and two «Lo que más cae» lines were rewritten to the WHATWG text; «lenguaje de marcado de hipertexto» now cites
   `ms-win-extensiones.html`. m06-l08 is at 1,471 words.
6. **Exams ledger.** Applied: conv2025_X P1 66 → «Clave oficial discutida»; conv2024_X P1 65's note now cites the
   Microsoft page; conv2025_X P1 reserva 2 → `vigente` with a note confirming the key; conv2020 P1 44 → `vigente`, and
   the index's «Información» notes now say «Acerca de». Counts updated in its summary table.
7. **Small points.** m06-l04 summary «Estilos de título»; m06-l06 summary «Compactar y reparar base de datos y Dividir
   la base de datos»; m06-l04 «Lo que más cae» «Transcribir graba en Word o carga un audio» (the fact 2025 A 53 asked).

**Blind check of these edits** (`docs/age-verification/bloque-vi/postclose-check.md`): 19 checked, 18 PASS, 1 FAIL. The
FAIL was the m06-l02 Narrador cut: it dropped the accessibility purpose that 2024 A 46 and 2020 50 ask. The item now
reads «lee la pantalla si eres invidente o tienes visión reducida» (the checker's wording), paid for by cutting
«(aplicaciones, configuración y archivos)» from the Búsqueda item; both re-checked blind, 11/11 PASS
(`postclose-recheck.md`). m06-l02 is at 1,500 words. After these edits: content tests (`pytest -k "glossary or registry
or content or pipeline"`) 68 passed, never-coins included; frontend `src/lib/refs`, `src/lib/glossary`, `src/lib/pdf`
302 passed, 49 skipped; goldens regenerated, unchanged since the close (303 web marks, 0 dangling references). The full
backend and frontend suites were not re-run after these edits.

## Coverage check 2022–2025 (2026-10-17)

Audit and fixes asked after the close; reports in `docs/age-verification/bloque-vi/coverage/` (auditor spec `spec.md`,
per-lesson reports `m06-lNN.md`, fix list `fixes.md`, fix spec `fix-spec.md`, writer files `fix-m06-lNN.md`, blind
verifications `verify-fix-m06-lNN.md`, the re-check queue `recheck-queue.md` and its check `recheck.md`).

**Audit.** For every index row of 2022–2025, four read-only auditors took the fact the keyed option states (questionnaire
and definitive key) and looked for it in the owner lesson (the exams ledger's first tema). Retired features and the
«Sin fuente oficial» list were left out of the denominator.

| Lesson | Asked | Covered | Partial | Miss | Share missed (partial = ½) |
|---|---|---|---|---|---|
| m06-l01 | 22 | 20 | 1 | 1 | 6.8 % |
| m06-l02 | 19 | 16 | 1 | 2 | 13.2 % |
| m06-l03 | 14 | 12 | 2 | 0 | 7.1 % |
| m06-l04 | 21 | 17 | 4 | 0 | 9.5 % |
| m06-l05 | 17 | 15 | 2 | 0 | 5.9 % |
| m06-l06 | 24 | 24 | 0 | 0 | 0 % |
| m06-l07 | 25 | 20 | 4 | 1 | 12 % |
| m06-l08 | 15 | 15 | 0 | 0 | 0 % |

No lesson missed more than a third, so all were patched. One m06-l02 miss (2025 A 47, Windows Search «aplicaciones,
configuración y archivos») was caused by a cut made earlier the same day to fit the Narrador fix. Two m06-l07 gaps
(2025 X 66, 2024 X 65) are the disputed Outlook search keys: the lesson follows Microsoft's page on purpose.

**Fixes.** 18 facts to add (`fixes.md`) plus two partials the auditor had passed on a functional reading (Asistencia
rápida, the quick access toolbar's «frequently used»). Mid-round, requirements v1.5 removed the word ceiling: writers
undid their own cuts, added every fix without cutting, and restored the earlier space cuts an exam asked (2020 and
annulled rows included): MySQL and minería de datos (m06-l01); idiomas, Registro, screen settings, and, by coordinator
decision although the index lists them as never asked, the two dialog-box keys and the desktop icon sizes (m06-l02);
Acerca de contents, the OneDrive Papelera and cloud-search clauses (m06-l03); Seleccionar, Opciones de impresión
(m06-l04); EXTRAE syntax (m06-l05); SiInm, Año(), calculated fields and controls, Conmutador, Texto largo 65.535
(m06-l06); Gráficos, Limpiar, Correo no deseado levels, carpetas de búsqueda, grupos de envío y recepción, F4 (m06-l07).
m06-l08 had no restorable cut an exam asked.

Where two official pages disagree, the lesson states both with their sources, as for Impr Pant: the quick access
toolbar's default position (m06-l04, «encima de la cinta» against «oculta debajo»). New sources: 25 pages (24 Microsoft
Spanish pages and RFC 5322 for the address form), saved and indexed in `fuentes.yaml` with sha256;
`ms-office-autoguardado.html` now also lists m06-l01 and `ms-win-busqueda-privacidad.html` m06-l03.

**Verification.** Blind per lesson: m06-l01 22/22, m06-l02 24/24, m06-l03 23/25, m06-l04 28/29, m06-l05 8/8, m06-l06
22/24 (with the m06-l08 check), m06-l07 16/20. The 10 FAILs (claims wider than the page, missing client labels in
Outlook, a person switch in one sentence, a rule about the colon in calculated fields inferred from examples, a position
stated against a cited page) were fixed with the verifiers' wording or a newly saved page, and re-checked blind: 16/17,
the one FAIL a line wrap, fixed. Every row the audit had marked covered was re-checked against the lessons after the
fixes: none lost. Glossary: `link_except` for g-directiva in m06-l03 (a Windows policy, not an EU directive);
`glossary-links.es.txt` 303 → 304 web marks (g-autoguardado now linked from a Fuentes title in m06-l01, same sense).

**Checks.** On the final tree: content tests (`pytest -k "glossary or registry or content or pipeline"`) 68 passed,
never-coins included; frontend `src/lib/refs`, `src/lib/glossary`, `src/lib/pdf` 302 passed, 49 skipped; goldens
regenerated (304 web marks, `lesson-refs.es.txt` unchanged, 0 dangling); every file in `sources/otros/` indexed, sha256
matching. The full backend and frontend suites were not re-run.

## Open items (after bloque VI)

**Exam labels and official labels** (decision of 2026-10-17: the lessons keep the label the official page prints;
R3 writes authored questions with the official label; the «Exámenes oficiales» set keeps the exam's original wording).
«—» means no official page prints a label for it.

| Etiqueta del examen | Etiqueta oficial |
|---|---|
| «Iconos muy grandes» (2025 A 48) | «iconos extra grandes» (m06-l03; `ms-win-explorador-lector.html`) |
| «Mosaicos» (2025 A 48) | — not printed: the Spanish page writes «iconos» where the English one has «Tiles» (m06-l03 leaves it out) |
| «Lista» (2025 A 48) | «listas» (m06-l03; `ms-win-explorador.html`) |
| «Ordenar», «Más» (Explorer command bar, 2024 X 55) | — not printed (m06-l03 says only that the column buttons in Detalles sort) |
| «Estándar» (Calculadora) | «Standard» (m06-l03; `ms-win-calculadora.html`) |
| «Privacidad y seguridad» (2024 X 57) | «Privacidad & seguridad» (m06-l03; `ms-win-indexacion.html`) |
| «Grabación de acciones de usuario» (2024 A 45) | «Grabadora de pasos» (m06-l03; `ms-win-desuso.html`) |
| «Vista › Macros» (2020 X 53) | «Ver» on the Macros page, «Vista» on the shortcut page without Macros (m06-l04 names no tab; `ms-word-macros.html`) |
| «Grabar macro» | «grabar macros», inside a garbled path (m06-l04 leaves it out; `ms-word-macros.html`) |
| Tab of «Saltos» («Disposición») | «Saltos de diseño>» on the page, «Disposición» on the shortcut page without Saltos (m06-l04 names only Saltos; `ms-word-salto-seccion.html`) |
| «Mostrar todo» (2024 X 60) | «Mostrar u ocultar ¶» (m06-l04; `ms-word-opciones-mostrar.html`) |
| «Leer en voz alta» (2022 X 53, 2020 54) | «Lectura en voz alta» (m06-l04; `ms-word-lectura-voz-alta.html`) |
| «Número de página» | «numeración de páginas» (m06-l04; `ms-word-numeros-pagina.html`) |
| «Mostrar» (Opciones de Word, 2020 53) | «Opciones de Word (Mostrar)» in the title, «Visualización» in the path (`ms-word-opciones-mostrar.html`) |
| «Imprimir selección» (2024 A 59) | «Imprimir hojas activas» › «Imprimir tabla seleccionada» (m06-l05; `ms-excel-imprimir.html`) |
| «Ajustar todas las columnas en una página» (2024 X 62) | the behaviour only: Ancho 1 página, Alto Automático; neighbouring label «Ajustar hoja en una página» (m06-l05; `ms-excel-escalar.html`) |
| «Vista › Inmovilizar paneles» | «pestaña Vista» and «Ver>Inmovilizar paneles» on the same page (m06-l05 writes «Vista»; `ms-excel-inmovilizar-paneles.html`) |
| «SIERROR» (2022 54) | «SI.ERROR» (m06-l05; `ms-excel-funcion-sierror.html`) |
| «BUSCARV» | «BUSCARV» in the body, «CONSULTAV» in one page title (m06-l05 writes BUSCARV) |
| «#N/A» (2025 X 57) | «#N/A» (m06-l05; `ms-excel-error-na.html`); the DIVIDIRTEXTO page prints «#N/D» |
| «Combinar y centrar» (2020 59) | «Combinar y centrar» and «Combinar & centro» (m06-l05; `ms-excel-combinar-celdas.html`) |
| «Indizado» (2025 X 59) | «Indexado» (m06-l06; `ms-access-tipos-datos.html`) |
| «Requerido» (2025 X 59) | «Obligatorio» (m06-l06; `ms-access-tipos-datos.html`) |
| «Divisor de bases de datos» (2020 X 59) | «Asistente para el separador de base de datos» (m06-l06; `ms-access-dividir.html`) |
| «Introduzca el valor del parámetro» (2025 A 60) | — not printed (m06-l06 gives the behaviour only) |
| «Origen del control» (2020 64) | «ControlSource» (`ms-access-expresiones.html`) and «origen de control» of a text box (`ms-access-formularios.html`); m06-l06 prints both as the pages do, without equating them |
| Tab of «Orden de tabulación» | «Diseño» on the cited page, «Diseño de formulario» on `ms-access-formularios.html` (m06-l06 follows its cited page) |
| «Gráficos modernos» (2025 X P1R 2) | «Gráfico moderno» (m06-l06; `ms-access-graficos.html`) |
| «Archivo › Información» (Compactar y reparar, 2022 X 62) | garbled «Información de>archivo>» (m06-l06 gives the closed-database path only; `ms-access-compactar.html`) |
| «Agrupar y ordenar» | «Agrupar &ordenar»; m06-l06 names the panel «Agrupación, orden y total» (`ms-access-informes.html`) |
| «Importar y vincular» | «Importar & vínculo» / «Importar & vincular» (m06-l06 as printed; `ms-access-importar-excel.html`) |
| «Retrasar entrega» (2025 X 64) | «Opciones de mensaje», «Opciones de entrega», «No entregar antes» (m06-l07; `ms-outlook-programar-envio.html`) |
| «Incluir» (group of Firma, 2020 X 62) | «Mensaje › Firma › Firmas» (m06-l07; `ms-outlook-firma.html`) |
| «Delegar acceso» (2024 A 63) | «Delegar el acceso» (m06-l07; `ms-outlook-delegados.html`) |
| «Correo no deseado › Opciones» (2020 X 61) | «Inicio › Eliminar › Bloquear › Opciones de correo electrónico no deseado» (junk-mail page read, not saved; item cut) |
| «Formato de texto › Edición › Buscar» (2020 X 68) | — not printed on any page read (item cut) |
| «Mail» (new Outlook, Ctrl+1) | «Vaya a Mail» (m06-l07 writes «va al correo»; `ms-outlook-atajos.html`) |
| «Configuración y más › Más herramientas › Anclar a Inicio» (2025 A 67) | «menú de más opciones › Más herramientas › Anclar a Inicio», garbled (m06-l02, m06-l08; `ms-win-menu-inicio.html`) |
| «hosting» (2020 66) | — not printed; m06-l08 uses «alojamiento de sitios web» (`incibe-glosario-ciberseguridad.pdf`, «Servidor») |
| «IPv4» / «IPv6» | «en su versión v4» / «en su versión v6» (m06-l08; `incibe-glosario-ciberseguridad.pdf`) |
| «secuestro de sesión» | «Session Hijacking», «también llamado secuestro de cookies» (m06-l08; `incibe-glosario-ciberseguridad.pdf`) |

**Paths decoded from garbled strings** (every label printed; order read back, confirmed by the plainly printed pattern
on another saved page unless noted):
- m06-l01: «Configuración › Cuentas › Copias de seguridad de Windows» — printed «Configuración>cuentas>de Copias de
  seguridad de Windows».
- m06-l02: «Configuración › Sistema › Multitarea» — «Multitarea del sistema>» (`ms-win-acoplar.html`,
  `ms-win-escritorios.html`).
- m06-l02: «Configuración › Sistema › Notificaciones» — «Notificaciones del sistema>».
- m06-l02: «Configuración › Cuentas › Opciones de inicio de sesión» — «Opcionesde inicio de sesión decuentas>».
- m06-l02: «Configuración › Personalización › Temas › Configuración del icono de escritorio» — «Temas de
  personalización>».
- m06-l02: «Enviar a › Escritorio (crear acceso directo)» — steps print «Enviar al>escritorio», the note «solo Enviar
  a».
- m06-l02: «Anclados» — the structure list prints «Chinchetas», the layout section «Anclados».
- m06-l02: «Asistente para el ajuste» — the same page also prints «Asistente de acoplamiento» and «Asistente de ajuste».
- m06-l02: «Windows+Impr Pant» — the row prints «Tecla Windows + PrtScn»; the key is «Impr Scn o Impr Pant».
- m06-l03: «Ver › Mostrar › Extensiones de nombre de archivo» — `ms-win-explorador.html` «Ver>presentación»;
  `ms-win-extensiones.html` «Ver>mostrar>extensiones de nombre de archivo».
- m06-l03: «Ver más › Opciones», list «Abrir Explorador de archivos para:» — the list label is printed only in the
  Windows 10 part of the page.
- m06-l03: «Ctrl+Windows+Q» — `ms-win-asistencia-rapida.html` «Presione Ctrl, + tecla + del logotipo de Windows,Q»;
  `ms-win-atajos.html` prints it plainly.
- m06-l04: «Revisar › Traducir › Traducir documento», «Revisar › Lectura en voz alta», «Referencias › Tabla de
  contenido», «Archivo › Imprimir», «Archivo › Opciones › Personalizar cinta de opciones», «Insertar › Numeración de
  páginas › Posición actual» — garbled on their pages; listed in the VI.4 notes.
- m06-l04: «Inicio › Seleccionar» (coverage fixes) — «Seleccionar inicio >»; tab-first order printed plainly on other
  saved Word pages («Inicio>Dictar>Transcripción») and on the English page («Home > Select»).
- m06-l05: «Revisar › Proteger libro», «Datos › Filtro», «Archivo › Imprimir» — garbled on their pages, order printed in
  prose on the same page.
- m06-l06: «Herramientas de base de datos» (Compactar, closed database) — «Herramientas >de base de datos»; the tab is
  printed plainly on `ms-access-dividir.html`, `ms-access-clave-principal.html`, `ms-access-relaciones.html`.
- m06-l06: «Nuevo origen de datos › Desde archivo › Excel» — «Nuevo origen>de datos desde archivo>Excel», reassembled
  across a «>»; no saved page prints it plainly.
- m06-l07: «Archivo › Agregar cuenta», «Archivo › Configuración de la cuenta › Delegar el acceso», «Mensaje › Firma ›
  Firmas», «Archivo › Administrar reglas y alertas › Nueva regla», «Configuración › Correo › Reglas» — garbled, order
  confirmed by plain prints.
- m06-l07: «Archivo › Herramientas › Limpieza de buzón» and «Configuración › Cuentas › Firmas» — reverse-order decode
  only; no saved page prints them in order.
- m06-l08: Edge «menú de más opciones › Más herramientas › Anclar a Inicio» — labels in the page's own garbled order.

**Sin fuente oficial** (decision of 2026-10-17: these stay out of the lessons and out of the authored bank; the
«Exámenes oficiales» set keeps the questions as asked). No official page found:
- m06-l01: disipador (2025 X 41) — searched support.microsoft.com and learn.microsoft.com es-es (disipador, heat sink):
  a Surface fan page and Q&A threads only.
- m06-l01: escáner as input and impresora as output device (2024 A 41 / B 45) — no Microsoft or standards page
  classifies them; HID driver pages checked.
- m06-l01: «software libre» against «software gratuito» (2025 X 42) — no official page defines it by that name; the ENI
  term «aplicación de fuentes abiertas» is used.
- m06-l01: chat de IA / ChatGPT (2024 A 65 / B 61) — no official Spanish page; no owner lesson.
- m06-l01: Linux and Android as operating systems (2020 41) — no Spanish official page saved.
- m06-l01: hardware definition of the caché beyond L2/L3 — only the `Win32_Processor` reference; the archived Microsoft
  blog was not used.
- m06-l02: Modo Dios (2022 46) — support and learn (es-es, en-us): Q&A threads and Windows 7 archive pages only.
- m06-l03: Ctrl+Mayús+arrastrar creates a shortcut (2025 X 48) — support and learn (es-es, en-us): Q&A threads and a
  2010 MSDN blog only; `ms-win-atajos.html` gives Alt+arrastrar.
- m06-l03: «Este equipo › Propiedades» opens Configuración › Sistema (2025 A 49) — support and learn: Q&A threads only.
- m06-l03: contents of Herramientas de Windows (2022 48) — screenshot only on `ms-win-herramientas-windows.html`.
- m06-l03: Detalles shows the most information (2020 46); sorting by fields not shown (2024 X 55); the «Enviar a»
  destinations (2024 X 56) — no page states them.
- m06-l04: Formato de imagen pane tabs (2020 52) — support es-es and en-us: no Word page lists the pane's tabs.
- m06-l04: a note's text on hover (2025 A 52) — closest is `ms-word-opciones-mostrar.html` (tooltips over hyperlinks and
  comment marks «o contenido similar»).
- m06-l04: cursiva shortcut (2025 A 51) — `ms-word-atajos.html` mixes the Spanish and English letter sets.
- m06-l05: «;» as the argument separator (2022 X 60) — no Spanish Microsoft page states it; «Operadores de cálculo y
  prioridad» (read, not saved) prints the union operator garbled.
- m06-l05: «20-2» read as a date (2024 A 60) — the page documents «2/2» only.
- m06-l05: PRUEBA.F.N (2022 53) — the Spanish category page prints «PRUEBA.F» and a garbled «F.PRUEBA».
- m06-l06: PostgreSQL (2024 X 45) — no Microsoft page names it; not an Access feature.
- m06-l06: 2.345,68 → Estándar (2025 A 59) — the page gives only «datos numéricos con decimales».
- m06-l07: «Dirigir respuestas a» / «Enviar las respuestas a» (2020 X 65) — support es-es and en-us («Direct Replies
  To», «Have replies sent to»): Q&A threads and third-party guides only.
- m06-l07: send/receive group options (2020 X P1R 1) — only a learn.microsoft.com page for Outlook 2016; restored in
  the coverage fixes from that page (see «Coverage check 2022–2025»).
- m06-l01: the processor «obtiene» (fetches) instructions (2025 A 41) — no official Spanish page; the lesson states
  «interpreta» and «ejecuta».
- m06-l02: the speech language can differ from the display language (2024 X 48) — `ms-win-idioma.html` says speech uses
  the display language; not written.
- m06-l03: the per-drive Papelera setting (2025 X 50) — forum threads and blogs only; the lesson gives the documented
  «No mover archivos eliminados a la papelera de reciclaje» policy.
- m06-l04: characters with and without spaces in Contar palabras (2022 X 56) — not on any page found.
- m06-l04: «palabra que no está en el diccionario» for Word desktop (2025 X 51) — only the Word para la Web tab says it.
- m06-l07: adding the account is the *first* step in Outlook (2022 62) — no page says «primer paso»; the lesson gives
  the first-run screen (type the address, Conectar).

**Impr Pant: two official descriptions** (decision of 2026-10-17: state both with their sources, as the TREBEP
and earlier-rule cases are stated; the lesson does not choose). `ms-win-atajos.html` (Windows 11 table): «Seleccione una
zona de la pantalla para hacer una captura de pantalla en el portapapeles»; `ms-win-recortes.html`: Imprimir pantalla
(PrtSc) takes «toda la pantalla» to the clipboard. m06-l02 now states both, each with its source; m06-l03 states
neither. R2b re-checks both live pages.

**Exams-ledger and index updates** (applied 2026-10-17, see the R2 bloque VI paragraph of
`docs/age-official-exams-ledger.md`): conv2025_X P1 66 → «Clave oficial discutida» and conv2024_X P1 65 keeps it, both
citing `ms-outlook-buscar.html`; conv2025_X P1 reserva 2 → `vigente` with a note confirming the key
(`ms-access-graficos.html`); conv2020 P1 44 → `vigente` and the index notes on 2020 44 and 51 now say «Acerca de», not
«Información». Not applied, for R3: 2022 X 45 «Escritorios» and 2024 X 52 «Herramientas de Windows» confirmed; new
Outlook has folder permission levels and its delegation is assigned from classic Outlook (index «posible» notes); 2025
A 67 Edge path not printed as keyed; 2024 A 65 (chat de IA) needs an owner tema; 2025 A 53 (Transcribir: 300 minutes on
the page, an option said 600).

**Waiting glossary terms:** the bloque I–V lists, plus g-extension-de-nombre-de-archivo, g-ruta-unc,
g-referencia-absoluta, g-referencia-estructurada, g-consulta-de-accion, g-grupo-de-microsoft-365 (each needs its
singular, or a plural `match`-only entry, in prose).

**Cut for length:** superseded. Requirements v1.5 removed the word ceiling; every cut an exam asked was restored in
the coverage fixes (see «Coverage check 2022–2025»). Not restored: Otros usuarios (2024 X 49, `función retirada`), the
«Enviar a» destinations and cursiva (sin fuente oficial), and cuts no exam asked.

**Files resting on non-UI sources:** `ms-win-tolerancia-errores.html` (Windows Server / Azure Local, not Windows 11; the RAID item says
so); `ms-win32-processor-cache.html`, `ms-sql-bits.html`, `ms-win-componentes-kernel.html`, `ms-win-aqs.html` (developer
references); `ms-office-formatos-archivo.html` (Word 2007–2021 table); `ms-win-paint.html` (product page);
`nist-prefijos-binarios.html`, `rfc1122-capas-tcp-ip.txt`, `rfc1918-direcciones-privadas.txt`,
`isoc-historia-internet.html`, `whatwg-html-introduccion.html`, `whatwg-html-scripting.html`, `rfc5322-formato-mensaje.txt`
(English; facts only, no labels); `ms-win-registro.html` (Windows Server troubleshooting page quoting an old definition);
`ms-win-directivas-explorador.html` (Policy CSP, admin documentation); `ms-outlook-grupos-envio-recepcion.html` (Office
Customization Tool 2016).

**Length.** No ceiling since requirements v1.5. After the coverage fixes the lessons run 1,471–1,879 words.

## Where to resume (after bloque VI)

R2 is complete for all six bloques. The next session starts R2b, the scope and currency audit (section 4b of the
requirements). For bloque VI it compares each saved page in `sources/otros/` with its live URL (labels, paths,
shortcuts, «Se aplica a»), starting with the open items above: the Impr Pant pair, the unconfirmed labels and the two
Outlook search keys. Every round writes its verification reports under `docs/age-verification/<bloque>/`
(decision 1 of «Decisions after bloque VI»).
