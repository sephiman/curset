# Verify re-check 2 — `m03-l05` (R2d, blind, Opus)

2026-11-17. 39 pending rows checked against the texts in `content/aeat-agentes-hacienda/sources/normativa/` (LGT 2024-12-21,
RGAT 2026-10-07, Orden HAC/1398/2003 2025-01-31, RD 1363/2010 2014-05-14). LO 15/1999 has no file; its line was checked
against the text of art. 94.5 LGT that names it. «Normativa» lines checked in both directions against every citation in the lesson.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `1825f07362` | PASS | art. 86.3 LGT | «apartado 1» → «apartado 1 del artículo 86 LGT»: right | — |
| `ed26037d13` | PASS | art. 88.4 LGT | «apartado 2 de este artículo» → art. 88 LGT: right | — |
| `fb12055e81` | PASS | art. 88.6 LGT | governed by the 88.6 citation of the next sentence; plazo and condition kept | — |
| `fd1fd1e1eb` | PASS | art. 66.2 RGAT | «apartado 1 de este precepto» → art. 66 RGAT; the esquema that follows has all of a)–e) | — |
| `d9fe48b9e1` | PASS | arts. 66.5–68.2 RGAT | lead-in to items each cited to the RGAT; claims no completeness | — |
| `36c5972714` | PASS | art. 66.6 RGAT | — | — |
| `a19592f470` | PASS | art. 69.5 RGAT | — | — |
| `159e20adb5` | PASS | art. 74.3 RGAT | letters b), c), d), e) and i), 12 months, two months: right | — |
| `84e15e0676` | PASS | art. 74.4 RGAT | — | — |
| `ea83d69822` | PASS | art. 78.3 RGAT | «estos medios» → programas informáticos y medios telemáticos (arts. 78.1–78.2): right | — |
| `6d315633da` | PASS | art. 78.3 RGAT | — | — |
| `298a108c0a` | PASS | apartado primero.2 Orden HAC/1398/2003 | «apartado anterior» → primero.1; inside the list led by «La Orden HAC/1398/2003 establece…», so «de la orden» resolves | — |
| `564183e406` | PASS | apartado segundo.1 Orden HAC/1398/2003 | «número 1 del apartado anterior» → primero.1: right | — |
| `49c039a378` | PASS | apartado segundo.4 Orden HAC/1398/2003 | «número 5 del apartado anterior» → primero.5: right | — |
| `06b9cf370d` | PASS | apartado tercero.1 Orden HAC/1398/2003 | «números 1 y 2 del apartado segundo»: right | — |
| `f3e87cb03b` | PASS | apartado cuarto.1 Orden HAC/1398/2003 | «número 4 del apartado Segundo»: right | — |
| `c72bcc25e3` | PASS | art. 93.2 LGT | «apartado anterior» → art. 93.1 LGT: right | — |
| `440711f116` | PASS | art. 94.1 LGT | subject («autoridades y entidades obligadas a informar y colaborar») is the esquema of art. 94.1 just above | — |
| `2a74d74ea5` | PASS | art. 30.1 RGAT | «este capítulo» → capítulo V (Obligaciones de información) del título II RGAT: right | — |
| `2751c576ca` | PASS | art. 30.2 RGAT | same chapter; governed by the 30.2 citation of the next sentence | — |
| `5d89b344f0` | PASS | art. 95 bis.3 LGT | — | — |
| `b4e52df06f` | FAIL | art. 95 bis.4 LGT | the article limits the pagos to those «a que se refiere el párrafo anterior» (payment of the whole amount owed at the fecha de referencia before the alegaciones plazo ends); the sentence dropped that link and widens it to any payment | Las alegaciones se refieren exclusivamente a la existencia de errores materiales, de hecho o aritméticos en relación con los requisitos del apartado 1 del artículo 95 bis LGT o a los pagos de la totalidad de la cantidad adeudada a la fecha de referencia efectuados por el deudor antes de la finalización del plazo para formular alegaciones, y en este caso debe aportarse justificación fehaciente de dichos pagos (art. 95 bis.4 LGT). |
| `a344de93cd` | PASS | art. 95 bis.4 LGT | — | — |
| `1c877e040f` | PASS | art. 95 bis.4 LGT | the orden also sets «los correspondientes ficheros y registros»; the sentence does not claim the orden sets only the date | — |
| `bba1c1cd68` | PASS | art. 95 bis.6 LGT | «apartado 4» → art. 95 bis.4 LGT: right | — |
| `32251eab45` | PASS | art. 95 bis.6 LGT | — | — |
| `0b32727036` | PASS | art. 95 bis.6 LGT | — | — |
| `745c7bca66` | PASS | art. 88 RGAT | lead-in to 88.3 and 88.7 with «además»; claims no completeness | — |
| `9ffdabb289` | PASS | art. 99.1 LGT | the list that follows covers arts. 99.2–99.9, the whole remainder of the article | — |
| `8202189fcf` | PASS | art. 99.3 LGT | — | — |
| `b6f2e8bd90` | PASS | art. 91.4 RGAT | «inferior al previsto en el párrafo anterior» = la mitad del plazo inicialmente fijado: right | — |
| `92356fb7cb` | FAIL | art. 98.2 RGAT | the article says «podrán hacerse constar, entre otros, los siguientes contenidos»; without «entre otros» the lead-in presents the open legal list as closed (the esquema reproduces all of a)–e); «entre otros» is the article's own word, not a stand-in for omitted items) | En las diligencias pueden hacerse constar, entre otros, los siguientes contenidos (art. 98.2 RGAT): |
| `0a84fcfa16` | FAIL | art. 98.3 RGAT | same: the article reads «y, entre otros:»; the lead-in drops it and closes the list (esquema a)–g) is complete) | En las diligencias pueden hacerse constar los hechos y circunstancias determinantes de la iniciación de otro procedimiento o que deban ser incorporados en otro ya iniciado y, entre otros, los siguientes (art. 98.3 RGAT): |
| `81789433ab` | PASS | art. 101.6 RGAT | «este apartado» → art. 101.6 RGAT: right | — |
| `e3ac4f2596` | FAIL | art. 104 RGAT | the article says «se considerarán dilaciones … entre otras, las siguientes»; the lead-in drops «entre otras» and presents the open list as closed (list a)–i) is complete) | Se consideran dilaciones en el procedimiento por causa no imputable a la Administración tributaria, entre otras, las siguientes (art. 104 RGAT): |
| `f99d4bb909` | PASS | art. 106.2 LGT | «apartado anterior» → art. 106.1 LGT: right | — |
| `63064d29b4` | PASS | Normativa (RGAT) | every RGAT citation in the lesson (parentheticals and esquema «Cita» cells) is listed; extras 36, 59, 82–86 and 111 are mentioned in copied law text of the same law (allowed by the ruling) | — |
| `1a60487dd4` | PASS | Normativa (RD 1363/2010) | lesson cites DA tercera.1 and DA tercera.2 (line 781); DA tercera.3 not cited; matches | — |
| `3286eae125` | PASS | Normativa (LO 15/1999) | named in art. 94.5 LGT («apartado 1 del artículo 21»), copied at line 376; not in `normativa.yaml`, given its own «nombrada en …» line as the ruling allows | — |

PASS 35 · FAIL 4
