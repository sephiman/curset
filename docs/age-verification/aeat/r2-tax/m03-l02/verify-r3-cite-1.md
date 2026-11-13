# Blind check — R3 citation fix, m03-l02, 2026-11-12

Source: `BOE-A-2021-590_res-13-01-2021-gestion-tributaria_2025-12-26.pdf` (`pdftotext -layout`, 21 pages, PDF page
index = printed «Página N»). «Segundo. El Departamento de Gestión Tributaria.» opens on page 4 (points 1 and 2.a–b);
point 3 («De acuerdo con lo establecido en la Orden de 2 de junio de 1994 … el Departamento …») with the list a)–e)
of Subdirecciones Generales is on page 5; points 5–9 of the same apartado develop each Subdirección. «Tercero» (Oficina
Nacional de Gestión Tributaria, page 11), «Cuarto» (Unidad Central de Información y Asistencia Digital) and «Quinto»
(Dependencias Regionales) carry no such list.

| item | verdict | reason | replacement |
|---|---|---|---|
| `72768f27ea` | PASS | The list the sentence introduces (a) Planificación y Coordinación, b) Técnica Tributaria, c) Información y Asistencia Tributaria, d) Verificación y Control Tributario, e) Asistencia Jurídica y Coordinación Normativa) is apartado segundo.3 of the Resolución, word for word with lesson lines 76–80, and is not in apartado tercero or elsewhere. «apartado segundo.3» matches the lesson's form for the other apartados (`apartado segundo Orden de 2 de junio de 1994`, `apartado primero.3 Orden …`, `apartado quinto.1 Orden …`, `apartado cuarto.3 Resolución de 13-01-2021 (estructura …)`). The golden line (citations.es.txt l. 2181) now reads anchor `boe-a-2021-590-apartado-segundo`, `…pdf#page=4`, text «apartado segundo.3 Resolución de 13-01-2021 (Departamento de Gestión Tributaria)»: page 4 is where apartado segundo opens, which is the anchor-level page the golden uses everywhere (e.g. `apartado cuarto.3` of BOE-A-2021-519 opens at the page of apartado cuarto). Note: point 3 itself sits on page 5, one page further. | |
| `5de41ea2b9` | PASS | Normativa line «Resolución de 13-01-2021 (Departamento de Gestión Tributaria): apartado segundo.3.» matches the only prose citation of this norm in the lesson, and the form matches the neighbouring Normativa lines («apartados primero.1 y cuarto.2», «apartados primero, tercero.1–2, …»). The golden normativa line (l. 2274) points at the same file. | |

Checked 2: PASS 2, FAIL 0.
