# Brief shared by every classifier of round R0a, course aeat-agentes-hacienda

Repo: /home/juanjo/PycharmProjects/curset (read-only for you). Scratchpad:
/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/be03eee0-d9a4-46b0-be16-0da5009fb4b2/scratchpad (call it $S).

You classify official first-exercise questions of the Cuerpo General Administrativo, especialidad de Agentes de la
Hacienda Pública (AEAT), acceso libre, convocatorias OEP 2020–2025. You write ONE output file in $S/work/ (named in your
task) and, if you need norm texts that are not local, downloads into $S/work/norms_extra/. Nothing else, anywhere.
Never write in the repo. Run any Python with `python3 -I`. Today is 2026-11-11.

## Inputs
- Your questions: a JSON list in $S/work/ (named in your task). Each item: id («2025-12» = exam, number in tipo A;
  «2022X-5» = the 2022 extraordinario), exam, date (exam date), n, tipoB (number(s) in tipo B), stem, opts {a..d}, key
  (definitive official key, or «ANULADA»), tribunal (what the Tribunal decided on this question: annulled, key changed).
- The parse can mangle a question. If one looks truncated or garbled, read the layout text: `pdftotext -layout` of
  content/aeat-agentes-hacienda/sources/examenes-oficiales/<date>_conv<OEP>_tipoA_cuestionario.pdf (2022X:
  2023-07-18_conv2022_extraordinario_tipoA_cuestionario.pdf).
- Programme: content/aeat-agentes-hacienda/sources/programa.md. Classify against the **2025 programme** (Anexo I), coded
  by the course as I.1–I.7 (Organización del Estado y funcionamiento de la AGE), II.1–II.5 (Derecho Administrativo
  General), III.1–III.20 (Organización de la Hacienda Pública y Derecho Tributario). The section «Cambios entre
  convocatorias» lists what the 2025 programme dropped (IRNR, Impuestos Especiales, contrabando, impuestos
  medioambientales, IVA «Tipos impositivos», retenciones, declaraciones informativas, obtención de información, consulta
  tributaria, recaudación en período voluntario, motivos de impugnación de la providencia, «Reducciones» of IRPF, IS
  exenciones subjetivas…). Earlier exams were sat on older programmes (34–37 temas); that does not matter for the tema
  you give, only for `fuera de temario`.
- Norm texts (consolidated, boe.es, downloaded 2026-11-11): $S/norms/<BOE-ID>.txt; the list is $S/work/norms_index.txt
  (LGT, RGAT 1065/2007, RGR 939/2005, RGRST 2063/2004, RGRVA 520/2005, LIRPF, RIRPF, LIVA, RIVA, LIS, RIS, RD 1619/2012,
  Ley 31/1990 art. 103, Orden PRE/3581/2007, the three AEAT Resoluciones of 13-01-2021, LOFCA, Ley 22/2009, TRLRHL,
  Ley 7/2012, Orden HAP/2178/2015, Orden EHA/1274/2007, LEC, Ley 28/1990). Common-part norms (CE, LOTC, LOPJ, Ley 50/1997,
  LRJSP, LPAC, LJCA, LBRL, TREBEP, Ley 30/1984, RD 364/1995, RD 365/1995, Ley 53/1984, RD 33/1986, LO 3/2007, LO 1/2004,
  RDL 1/2013, Ley 39/2006, Ley 19/2013, LOPDGDD, RGPD, TUE, TFUE, RDL 4/2000, LGSS…): the PDFs in
  content/age-auxiliar-c2/sources/normativa/ and content/age-administrativo-c1/sources/normativa/ (C2 is the more recent
  snapshot, 2026-11-05; `pdftotext -layout` them into $S/work/norms_extra/ if you need text). Their normativa.yaml files
  tell you which file is which and list cambios_pendientes. Anything else: download the consolidated PDF from
  `https://www.boe.es/buscar/pdf/<year>/<BOE-ID>-consolidado.pdf` (EU law: eur-lex.europa.eu) into $S/work/norms_extra/.
- Errata in stems that do not change the key are common in these exams: «Ley 58/2023» (= 58/2003), «Ley 27/2004» (= Ley
  27/2014 LIS), «Ley 29/1988» (= Ley 29/1998 LJCA), «Ley Orgánica 3/2017» (= LO 3/2007). Record each as «Errata: …».

## Status rules (one per question)
- `anulada`: the definitive sheet says ANULADA. Still classify tema and the style fields.
- `vigente`: official key correct today (2026-11-11), no note.
- `vigente-con-nota`: key stays, visible note of one kind: «Clave oficial discutida: <why>» (key not supported by the text
  in force, or not unique) in `nota_clave`; «Denominación actual: <current name>» (organ renamed since). An official key
  the Tribunal changed and that is right is plain `vigente` (the `tribunal` field already records it).
- `norma modificada: <norma> art. X`: the correct answer changed because the law changed (version in force today, or a
  change already published with a later effective date: then add «(cambio-pendiente, desde DD-MM-YYYY)»).
- `fuera de temario`: the topic is in no tema of the 2025 programme (e.g. IRNR, Impuestos Especiales, contrabando, ITF,
  gravámenes temporales, IVA tipos impositivos if no 2025 phrase covers the question). Give in `nota` the old tema it
  belonged to («programa 2024, tema 22: Impuestos Especiales de fabricación») and still give the nearest 2025 tema in
  `tema_alt` if one exists. If a 2025 phrase arguably covers it, use the tema and write «cobertura discutible: …» in nota.
- `dudosa`: you cannot settle it. Say why.
Official keys are never a source of facts. Check each key against the norm text in force (quote the decisive words,
≤ 25 words, in `evidence`, with the article). Never change an official key: record a disagreement in nota_clave.
When the answer depends on a figure a yearly norm sets (interés de demora, interés legal, IPREM, SMI, modules, amounts in a
Ley de Presupuestos or an annual order), fill `cifra_anual` with «<figure> — fijada por <norm>, <year>».

## Category vocabularies (use exactly these strings)
stem_form: «según el artículo X … (completar)», «según el artículo X … ¿?», «según la norma (sin artículo) … (completar)»,
«según la norma (sin artículo) … ¿?», «¿cuál de las siguientes…?», «señale/marque la (respuesta|afirmación) correcta»,
«pregunta directa ¿…?», «enunciado a completar», «supuesto breve con datos».
option_type: enunciado, órgano, plazo, cantidad, porcentaje, cálculo, procedimiento, fecha, artículo, sujeto, otro.
distractor: «texto alterado», «otra figura del mismo tipo», «invención», «otro plazo», «cifra cercana», «cálculo
erróneo», «órgano de otro nivel», «norma derogada o anterior», «mixto».
negative: true when the stem asks for the false/incorrect/excluded option (NO, FALSA, INCORRECTA, EXCEPTO, «no es»).
cites_article: true when the stem names an article number.

## Output
One JSON list, one object per question, in this shape:
{"id": "2025-12", "tema": "III.20", "tema_alt": null, "norma": "Reglamento (UE) 952/2013 (CAU)", "articulo": "art. 18",
 "stem_form": "…", "option_type": "…", "distractor": "…", "negative": false, "cites_article": true,
 "status": "vigente", "nota_clave": "", "nota": "", "evidence": "«…» (art. 18.1 CAU)", "key_check": "ok",
 "cifra_anual": null}
key_check: «ok» (checked against the text), «discutida», «no comprobable» (say why in nota), «anulada».

Work exam by exam, and save your output file after each exam (rewrite the whole JSON list), so a cut loses little.
At the end reply with: counts per status, the ids you marked dudosa / norma modificada / fuera de temario / clave
discutida with one line each, the norms you needed that were not local (with BOE id), and anything in the inputs that
looked wrong.
