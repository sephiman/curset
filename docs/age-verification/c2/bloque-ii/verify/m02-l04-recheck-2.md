# Verification — `m02-l04`, re-check 2

Verifier: blind verifier (opus), 2026-11-06. Did not write the lesson.

Files read: `docs/age-verification/c2/bloque-ii/pending/m02-l04.md`, `content/age-auxiliar-c2/es/lessons/m02-l04.md`,
`content/age-auxiliar-c2/sources/normativa.yaml` (Ley 34/2002 entry), `content/age-auxiliar-c2/sources/otros/fuentes.yaml`;
(pdftotext -layout) `sources/normativa/BOE-A-2002-13758_lssi_2025-12-18.pdf` (sha256 b959ff69…),
`sources/normativa/BOE-A-2018-12699_rd-1112-2018-accesibilidad-web_2019-08-12.pdf`,
`sources/otros/sgad-catalogo-servicios-admin-digital.pdf` (sha256 c4b8b11a… = fuentes.yaml).

Admissibility of `sgad-catalogo-servicios-admin-digital.pdf`: admissible. The PDF is the Ministerio de Hacienda y
Administraciones Públicas publication (Secretaría de Estado de Administraciones Públicas, Dirección de Tecnologías de la
Información y las Comunicaciones; «1ª edición electrónica: marzo de 2016»), hosted on rediris.es (RedIRIS, Red.es, a
public-sector entity). Caveat for the coordinator: the copy carries «NIPO: ……», an «¡ERROR! MARCADOR NO DEFINIDO» in the
index and «V0.21» in its URL, so it reads as a working copy of the edition; the facts checked are unaffected.

Result: 4 PASS, 2 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `f0751ccc9e` | FAIL | disp. adic. quinta Ley 34/2002 | DA 5.ª heading «Accesibilidad para las personas con discapacidad y de edad avanzada a la información proporcionada por medios electrónicos», «(Derogada)»: matches. The law's title is cut: it is «Ley 34/2002, de 11 de julio, de servicios de la sociedad de la información y de comercio electrónico» | La Ley 34/2002, de 11 de julio, de servicios de la sociedad de la información y de comercio electrónico, ya trataba en su disposición adicional quinta la accesibilidad para las personas con discapacidad y de edad avanzada a la información proporcionada por medios electrónicos; esa disposición está hoy derogada (disp. adic. quinta Ley 34/2002). |
| `fa9c634902` | PASS | preámbulo RD 1112/2018 | «También existen otras normas que hacen referencia a los requisitos de accesibilidad de los sitios web de las Administraciones Públicas … Algunas de ellas son la Ley 34/2002 …» | — |
| `79935a499d` | FAIL | sgad-catalogo-servicios-admin-digital.pdf, p. 18 | the nine services (SIR, REC, SICRES 3.0, Geiser y ORVE, REA, RFH, Representa, Notaría) are listed under «Registros y representación del ciudadano ante las AA.PP.»: matches. The title is not the document's: the cover reads «Catálogo de servicios – Administración digital», and the edition is «1ª edición electrónica: marzo de 2016» | En el «Catálogo de servicios – Administración digital» (1.ª edición electrónica, marzo de 2016), el apartado «Registros y representación del ciudadano ante las AA.PP.» incluye SIR, REC, SICRES 3.0, Geiser y ORVE, REA, RFH, Representa y Notaría. |
| `909469a62a` | PASS | sgad-catalogo-servicios-admin-digital.pdf, p. 18 | «Geiser y ORVE – soluciones para oficinas de registro, para digitalización de documentos conforme a NTI de Digitalización, e intercambio de asientos registrales por SIR» | — |
| `37a0f31357` | PASS | Normativa line | the prose cites disp. adic. quinta Ley 34/2002 and nothing else of that law. Outside the pending set: the prose now also cites «preámbulo RD 1112/2018» (line 189) and the RD 1112/2018 line («arts. 1.2, 2, 5, 7, 15–16 y 18») does not list «preámbulo» | — |
| `817304b3b4` | PASS | Otras fuentes line | the lesson cites exactly the nine files listed (pag-quienes-somos, pag-telefono-060, pag-oficina-informacion, sede-pag-portada, clave-que-es, pae-circe, pae-servicios, incibe-glosario-ciberseguridad, sgad-catalogo-servicios-admin-digital); sgad consulted 2026-11-06 as in fuentes.yaml | — |
