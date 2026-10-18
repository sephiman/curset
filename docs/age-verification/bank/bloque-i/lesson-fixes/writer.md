# Bloque I lesson fixes — writer record (2026-10-18)

Bank ledger open items 1, 2, 8 and 10. Files touched: `content/age-administrativo-c1/es/lessons/m01-l01.md`,
`m01-l02.md`. Norm text: `pdftotext -layout sources/normativa/BOE-A-1978-31229_ce_2026-05-20.pdf`. Every new
citation was run through `scan_lesson` with the course `NormIndex`: each resolves to a CE anchor. Tests and goldens
not run (pause). Line numbers are after the edit.

## 1. m01-l01 «Lo que más cae», lmc-6 (open item 8) — l. 473

Old:

> - La Constitución tiene un título preliminar y diez títulos (CE).

New:

> - Solo los españoles son titulares de los derechos del artículo 23, salvo lo que, atendiendo a criterios de
>   reciprocidad, pueda establecerse por tratado o ley para el sufragio activo y pasivo en las elecciones municipales
>   (art. 13.2 CE).

Why this fact: asked by conv2020_X P1 1 (filed under I.1 only, `official/I.1.md`), stated and cited in the lesson
(l. 96–98, «(art. 13.2 CE)»), not among the other nine lines. Art. 13.2 CE:

> 2. Solamente los españoles serán titulares de los derechos reconocidos en el artículo 23, salvo lo que, atendiendo a
> criterios de reciprocidad, pueda establecerse por tratado o ley para el derecho de sufragio activo y pasivo en las
> elecciones municipales.

The structure sentence stays in the «Estructura» section (l. 13); only the «Lo que más cae» line changes.

## 2. m01-l02 table «Nombramientos en otros poderes» (open item 1) — l. 128–135

The «Artículo» column held bare `art. … CE`, which the scanner does not read (it reads parentheticals only). The
citation now closes the «Propuesta o elección» cell in parentheses, as the plain tables of m01-l01 (l. 324–328, «Tres
meses desde que sean firmes (art. 42 LOTC)») and m01-l07 (l. 277–279) do; the third column goes. No fact changed.

Old (header and one row; the other five alike):

> | Nombramiento | Propuesta o elección | Artículo |
> | El Fiscal General del Estado | El Gobierno, oído el Consejo General del Poder Judicial | art. 124.4 CE |

New:

> | Nombramiento | Propuesta o elección |
> | El Fiscal General del Estado | El Gobierno, oído el Consejo General del Poder Judicial (art. 124.4 CE) |

Scanned: arts. 122.3, 123.2, 124.4, 159.1, 160 and 152.1 CE each resolve (anchors `…-art-122`, `-123`, `-124`,
`-159`, `-160`, `-152`).

## 3a. m01-l02 tutela (open item 2) — l. 234–235

Old:

> Para la tutela la Constitución pide ser español de nacimiento. Para la Regencia basta ser español
> (arts. 59.4 y 60.1 CE).

New:

> Al tutor nombrado en el testamento del Rey difunto la Constitución le pide ser español de nacimiento.
> Para la Regencia basta ser español (arts. 59.4 y 60.1 CE).

Art. 60.1 CE (whole):

> 1. Será tutor del Rey menor la persona que en su testamento hubiese nombrado el Rey difunto, siempre que sea mayor de
> edad y español de nacimiento; si no lo hubiese nombrado, será tutor el padre o la madre mientras permanezcan viudos.
> En su defecto, lo nombrarán las Cortes Generales, pero no podrán acumularse los cargos de Regente y de tutor sino en
> el padre, madre o ascendientes directos del Rey.

## 3b. m01-l02 art. 151.2 (open item 2) — l. 140–145

Old:

> En los Estatutos de autonomía del artículo 151, una vez ratificados por las Cortes Generales, el Rey
> los sanciona y los promulga como ley (art. 151.2 CE).

New:

> En el procedimiento del artículo 151, el proyecto de Estatuto aprobado en referéndum en cada provincia
> se eleva a las Cortes Generales. Si los plenos de ambas Cámaras lo ratifican, el Rey lo sanciona y lo
> promulga como ley (art. 151.2.4.º CE). Si la Comisión Constitucional del Congreso y la delegación de
> la Asamblea proponente no llegan a un acuerdo, el proyecto se tramita como proyecto de ley ante las
> Cortes Generales. El texto que aprueban se somete a referéndum en las provincias, y su promulgación
> sigue a la aprobación en cada una (art. 151.2.5.º CE).

Art. 151.2 CE:

> 2.º Aprobado el proyecto de Estatuto por la Asamblea de Parlamentarios, se remitirá a la Comisión Constitucional del
> Congreso, la cual, dentro del plazo de dos meses, lo examinará con el concurso y asistencia de una delegación de la
> Asamblea proponente para determinar de común acuerdo su formulación definitiva.
> 3.º Si se alcanzare dicho acuerdo, el texto resultante será sometido a referéndum del cuerpo electoral de las
> provincias comprendidas en el ámbito territorial del proyectado Estatuto.
> 4.º Si el proyecto de Estatuto es aprobado en cada provincia por la mayoría de los votos válidamente emitidos, será
> elevado a las Cortes Generales. Los plenos de ambas Cámaras decidirán sobre el texto mediante un voto de
> ratificación. Aprobado el Estatuto, el Rey lo sancionará y lo promulgará como ley.
> 5.º De no alcanzarse el acuerdo a que se refiere el apartado 2 de este número, el proyecto de Estatuto será tramitado
> como proyecto de ley ante las Cortes Generales. El texto aprobado por éstas será sometido a referéndum del cuerpo
> electoral de las provincias comprendidas en el ámbito territorial del proyectado Estatuto. En caso de ser aprobado
> por la mayoría de los votos válidamente emitidos en cada provincia, procederá su promulgación en los términos del
> párrafo anterior.

Citation form `art. 151.2.4.º CE` parses (unit art. 151, norm CE); the course already uses the ordinal form
(m02-l02 l. 277, «art. 10.1.2.º RD …»).

## 3c. m01-l01 «Las reformas» (open item 10) — l. 69–72

Old:

> - 27 de agosto de 1992: artículo 13.2, sufragio pasivo de los extranjeros en las elecciones
>   municipales.
> - 27 de septiembre de 2011: artículo 135, estabilidad presupuestaria.
> - 15 de febrero de 2024: artículo 49, personas con discapacidad.
> - 19 de mayo de 2026: artículo 69.3, Formentera elige un senador propio.

New:

> - 27 de agosto de 1992: artículo 13.2.
> - 27 de septiembre de 2011: artículo 135.
> - 15 de febrero de 2024: artículo 49.
> - 19 de mayo de 2026: artículo 69.3.

`sources/otros/boe-analisis-ce.xml`, `<posteriores>`:

> el art. 69.3, por Reforma de 19 de mayo de 2026
> el art. 49, por Reforma de 15 de febrero de 2024
> el art. 135, por Reforma de 27 de septiembre de 2011
> el art. 13.2, por Reforma de 27 de agosto de 1992

No 1992, 2011 or 2024 reform text is in `sources/normativa/`. The 2026 one is
(`BOE-A-2026-10881_reforma-ce-art-69-3_2026-05-20.pdf`, title «… a los efectos de que la isla de Formentera elija un
senador propio …»), but its title is not a citable unit (`artículo único de la Reforma de 19 de mayo de 2026` does not
parse), and m01-l03 l. 79–82 already states the Formentera senator with its citation. So the materia goes for all
four. The intro sentences (four reforms, one article each, cited to the page) stay: the page lists four `SE MODIFICA`
entries, one article each.
