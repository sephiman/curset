# Verify re-check 1 — `m01-l03`

Blind re-check (R2d spec-verify.md, incl. «Added 2026-11-14» and the «Normativa» ruling). Norm texts: pdftotext of `content/aeat-agentes-hacienda/sources/normativa/`.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `13aa24e272` | PASS | art. 2.2.n) Ley 50/1997 | sits after the art. 13.1 paragraph instead of closing the art. 2.2 list; moving it under the list is a structural fix | — |
| `379ee11ff9` | PASS | art. 10.3 Ley 50/1997 | — | — |
| `21b9c4ef7a` | PASS | art. 3.1.j) LRJSP | — | — |
| `f5eb854133` | PASS | art. 19.2 LRJSP | — | — |
| `49c52dca53` | PASS | art. 69.3 LRJSP | — | — |
| `32bbc332a4` | FAIL | art. 103.1 LRJSP | «No confundir» line: the cut drops the defining clause «y que junto con el ejercicio de potestades administrativas desarrollan actividades prestacionales, de gestión de servicios o de producción de bienes de interés público, susceptibles de contraprestación» | Las entidades públicas empresariales son entidades de Derecho público, con personalidad jurídica propia, patrimonio propio y autonomía en su gestión, que se financian con ingresos de mercado, a excepción de aquellas que tengan la condición o reúnan los requisitos para ser declaradas medio propio personificado de conformidad con la Ley de Contratos del Sector Público, y que junto con el ejercicio de potestades administrativas desarrollan actividades prestacionales, de gestión de servicios o de producción de bienes de interés público, susceptibles de contraprestación (art. 103.1 LRJSP). |
| `379f0ad166` | PASS | art. 108 sexies.5 LRJSP | — | — |
| `5c5f299208` | PASS | Ley 40/2015 (LRJSP) | matches every LRJSP citation of the lesson | — |
| `636dd08f41` | PASS | arts. 55.11.b) y 61.e), 61.n) LRJSP | — | — |
| `4c63d234d7` | FAIL | arts. 73.1.e).4.º, 104 y 113 LRJSP | the lesson also names the Ley del Patrimonio de las Administraciones Públicas in the art. 113 LRJSP sentence (line 902) | Ley 33/2003 (Patrimonio de las Administraciones Públicas): nombrada en los arts. 73.1, 104 y 113 LRJSP; no figura en `normativa.yaml`. |
| `5fad9672c4` | PASS | art. 73.1.d).2.º LRJSP | — | — |
| `0ac19c35b4` | FAIL | art. 1 RD 829/2023 | art. 1 RD 829/2023 does not name RD 1009/2023 (published later); the lesson names it in its own sentence (line 495), without a precept | RD 1009/2023 (estructura orgánica básica): sin precepto citado. |
| `403c8bc4e6` | FAIL | arts. 55.10, 62.2.e), 72.4, 80, 103.1, 104 y 130 LRJSP; art. 11 Ley 50/1997 | RDLeg 3/2011 is also named in the art. 62.2.e) LRJSP item (line 574); the «Ley de Contratos del Sector Público» named in the art. 103.1 LRJSP sentence (line 859) is on no «Normativa» line | Ley 3/2015, RDLeg 3/2011, Ley de Contratos del Sector Público, Ley 2/2014 y Ley de Fundaciones: nombradas en los arts. 55.10, 62.2.e), 72.4, 80, 103.1, 104 y 130 LRJSP y en el art. 11 Ley 50/1997; no figuran en `normativa.yaml`. |
| `9b1bb0326c` | PASS | art. 84.2 LRJSP | — | — |
| `ccb73d9f42` | PASS | art. 111.1 LRJSP | — | — |

PASS 11 · FAIL 4
