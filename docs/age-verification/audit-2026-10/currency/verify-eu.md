# Blind verification — EU sources after the R2b currency check

Date: 2026-10-17. Scope: every place in `content/age-administrativo-c1/es/lessons/` and `glossary.yaml` that states
who decides preliminary rulings, the composition or competences of the Tribunal General or the Tribunal de Justicia,
or an article of the Council Rules of Procedure. Checked against the new consolidations, extracted with
`pdftotext -layout`:

- TUE + Protocols: `sources/normativa/CELEX-02016M-20250315_tue_2025-03-15.pdf` (02016M, 15.03.2025, 007.001). The
  Statute of the CJEU (Protocol No 3) is in this file: art. 48, art. 49 bis, art. 50, art. 50 ter.
- TFUE: `sources/normativa/CELEX-02016E-20250315_tfue_2025-03-15.pdf` (02016E, 15.03.2025, 007.001).
- Council Rules: `sources/normativa/CELEX-02009D0937-20260101_reglamento-interno-consejo_2026-01-01.pdf` (02009D0937,
  01.01.2026, 020.001).

Line numbers are as of this check; another agent was editing `m01-l11.md`, so locate by quote. `exercises/` and
`course.yaml` contain no statement on these points (grep for «prejudicial», «Tribunal General», «Reglamento interno
del Consejo»: no hits).

| # | Place (file:line, quote) | Article (new file) | PASS/FAIL | Reason | Replacement (for FAIL, verbatim-faithful Spanish) |
|---|---|---|---|---|---|
| 1 | `m01-l11.md:120` «El Reglamento interno lo llama Coreper (art. 1.3 Reglamento interno del Consejo).» | Reglamento interno, anexo art. 1.3 (02009D0937) | PASS | Art. 1.3 párr. 2: «el Comité de Representantes Permanentes de los Gobiernos de los Estados miembros (Coreper)». | — |
| 2 | `m01-l11.md:128-129` «El Reglamento interno del Consejo, aprobado por la Decisión 2009/937/UE del Consejo, de 1 de diciembre de 2009» | Header of 02009D0937 | PASS | «DECISIÓN DEL CONSEJO de 1 de diciembre de 2009 por la que se aprueba su Reglamento interno (2009/937/UE)». | — |
| 3 | `m01-l11.md:129-131` «La Presidencia la ejercen grupos predeterminados de tres Estados miembros durante dieciocho meses. Cada miembro del grupo preside por rotación todas las formaciones, salvo la de Asuntos Exteriores, durante seis meses (art. 1.4 …).» | Reglamento interno, anexo art. 1.4 | PASS | Art. 1.4: «grupos predeterminados de tres Estados miembros durante un período de dieciocho meses […] Cada miembro del grupo ejercerá por rotación, durante un período de seis meses, la Presidencia de todas las formaciones del Consejo, con excepción de la formación de Asuntos Exteriores». Unchanged. | — |
| 4 | `m01-l11.md:135-136` «El Consejo tiene su sede en Bruselas. Durante los meses de abril, junio y octubre celebra sus sesiones en Luxemburgo (art. 1.3 …).» | Reglamento interno, anexo art. 1.3 párr. 1 | PASS | «El Consejo tendrá su sede en Bruselas. Durante los meses de abril, junio y octubre, el Consejo celebrará sus sesiones en Luxemburgo». | — |
| 5 | `m01-l11.md:136-138` «En circunstancias excepcionales, el Consejo o el Coreper pueden decidir por unanimidad que una sesión se celebre en otro lugar (art. 1.3 …).» | Reglamento interno, anexo art. 1.3 párr. 2 | PASS | «Cuando concurran circunstancias excepcionales y por causas debidamente justificadas, el Consejo o el […] (Coreper) podrán decidir, por unanimidad, que una sesión del Consejo se celebre en otro lugar.» | — |
| 6 | `m01-l11.md:438` «Lo que más cae»: «El Consejo tiene su sede en Bruselas y celebra sus sesiones en Luxemburgo en abril, junio y octubre (art. 1.3 Reglamento interno del Consejo).» | Reglamento interno, anexo art. 1.3 | PASS | Same text as #4. | — |
| 7 | `m01-l11.md:450` «Reglamento interno del Consejo: arts. 1.3 y 1.4 del anexo.» | Reglamento interno, anexo | PASS | Both still exist under those numbers in the annex («ANEXO — REGLAMENTO INTERNO DEL CONSEJO — Artículo 1»). | — |
| 8 | `m01-l11.md:267-269` «El Tribunal de Justicia de la Unión Europea comprende el Tribunal de Justicia, el Tribunal General y los tribunales especializados. Garantiza el respeto del Derecho […] (art. 19.1 TUE).» | TUE art. 19.1 (02016M) | PASS | Literal match. | — |
| 9 | `m01-l11.md:273` «Lo compone un juez por Estado miembro, asistido por abogados generales (art. 19.2 TUE).» | TUE art. 19.2 párr. 1 | PASS | «estará compuesto por un juez por Estado miembro. Estará asistido por abogados generales.» | — |
| 10 | `m01-l11.md:273-275` «El TFUE fija ocho abogados generales. El Consejo, por unanimidad, puede aumentar su número si el Tribunal lo pide (art. 252 TFUE).» | TFUE art. 252 (02016E) | PASS | «estará asistido por ocho abogados generales. Si el Tribunal de Justicia lo solicitare, el Consejo, por unanimidad, podrá aumentar el número». | — |
| 11 | `m01-l11.md:278-283` six-year term by common accord after the art. 255 committee, partial renewal every three years, reappointment, President for three years renewable (art. 253 TFUE) | TFUE art. 253 | PASS | All four elements literal in art. 253. | — |
| 12 | `m01-l11.md:287` «El Tribunal General dispone al menos de un juez por Estado miembro (art. 19.2 TUE).» | TUE art. 19.2 párr. 2 | PASS | «El Tribunal General dispondrá al menos de un juez por Estado miembro.» | — |
| 13 | `m01-l11.md:287-288` «El número exacto lo fija el Estatuto del Tribunal de Justicia de la Unión Europea (art. 254 TFUE).» | TFUE art. 254 párr. 1 | PASS | «El número de jueces del Tribunal General será fijado por el Estatuto». | — |
| 14 | `m01-l11.md:288-290` «Sus miembros se designan también por seis años, con renovación parcial cada tres, y eligen a su Presidente por tres años (art. 254 TFUE).» | TFUE art. 254 párr. 2-3 | PASS | «por un período de seis años […] Cada tres años tendrá lugar una renovación parcial […] Presidente del Tribunal General por un período de tres años». | — |
| 15 | `m01-l11.md:290-291` «el Tribunal General tiene 54 jueces, dos por cada Estado miembro» | Estatuto (Protocolo n.º 3) art. 48 c), in 02016M | PASS | «c) dos Jueces por Estado miembro a partir del 1 de septiembre de 2019»; 27 × 2 = 54. The sentence cites the curia page, not the Statute; the new Statute confirms it. | — |
| 16 | `m01-l11.md:295-297` «El Tribunal se pronuncia sobre los recursos de un Estado miembro, de una institución o de personas físicas o jurídicas, y con carácter prejudicial, a petición de los órganos jurisdiccionales nacionales (art. 19.3 TUE).» | TUE art. 19.3; TFUE art. 256.3; Estatuto art. 50 ter | FAIL | Art. 19.3 gives this to «El Tribunal de Justicia de la Unión Europea» (the institution). The lesson's subject is the bare «El Tribunal», right after the «El Tribunal de Justicia» and «El Tribunal General» subsections, and at line 274 the same lesson uses «el Tribunal» for the Tribunal de Justicia. Read that way, the sentence says the Tribunal de Justicia alone decides preliminary references. That is no longer true: art. 256.3 TFUE and Estatuto art. 50 ter (M10, Reg. 2024/2019) now give the Tribunal General the preliminary references that fall exclusively within IVA, impuestos especiales, código aduanero, clasificación arancelaria, compensación a pasajeros and comercio de derechos de emisión. The citation is right; the subject is ambiguous. | «El Tribunal de Justicia de la Unión Europea se pronuncia sobre los recursos de un Estado miembro, de una institución o de personas físicas o jurídicas, y con carácter prejudicial, a petición de los órganos jurisdiccionales nacionales (art. 19.3 TUE).» Optional second sentence (then add 256 to the TFUE line in «Normativa»): «El Tribunal General es competente para conocer de las cuestiones prejudiciales en materias específicas determinadas por el Estatuto (art. 256.3 TFUE).» |
| 17 | `m01-l11.md:423-425` «Cuando la cuestión prejudicial se plantea en un asunto pendiente ante un órgano jurisdiccional nacional cuyas decisiones no sean susceptibles de ulterior recurso judicial de Derecho interno, ese órgano está obligado a someterla al Tribunal (art. 267 TFUE).» | TFUE art. 267 párr. 3; Estatuto art. 50 ter párr. 3 | PASS | Matches art. 267 («dicho órgano estará obligado a someter la cuestión al Tribunal»), which uses the same bare «Tribunal» for the institution. It is true even if read as the Tribunal de Justicia, because art. 50 ter párr. 3 says that every preliminary reference «se presentará ante el Tribunal de Justicia», which then transfers it. | — |
| 18 | `m01-l11.md:449` «Normativa» TFUE list: «252–254, … 267» | TFUE | PASS | Every cited article exists and supports its sentence. If #16's optional sentence is adopted, add 256. | — |
| 19 | `glossary.yaml:614-620` g-cuestion-prejudicial: «Petición de un órgano jurisdiccional nacional al Tribunal de Justicia de la Unión Europea para que se pronuncie sobre la interpretación de los Tratados o sobre la validez e interpretación de los actos de la Unión. Es obligatoria para el órgano cuyas decisiones no admiten ulterior recurso (art. 267 TFUE).» | TFUE art. 267; Estatuto art. 50 ter | PASS | It names the institution, as art. 267 párr. 1 does («El Tribunal de Justicia de la Unión Europea será competente para pronunciarse, con carácter prejudicial: a) sobre la interpretación de los Tratados; b) sobre la validez e interpretación de los actos…»). Obligation per párr. 3. It does not say that the Tribunal de Justicia alone decides. | — |

## Counts

19 places checked: **18 PASS, 1 FAIL** (#16).

## Note on the R2b report

`normativa.md` («Citations of changed articles», item 2) quotes Estatuto art. 50 ter as listing materias a) to e).
The new text has a sixth: «f) el régimen de comercio de derechos de emisión de gases de efecto invernadero», plus a
second paragraph keeping for the Tribunal de Justicia the references that raise independent questions of primary law,
public international law, general principles or the Charter. Item 2's verdict «Fact changes: no» rests on reading «El
Tribunal» as the institution; this check finds the lesson's wording ambiguous, so it disagrees for line 295 only.
