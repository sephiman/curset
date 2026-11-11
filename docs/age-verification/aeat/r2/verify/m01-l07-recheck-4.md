# m01-l07 — re-check 4 (blind): pending «Normativa» lines

Lesson: `content/aeat-agentes-hacienda/es/lessons/m01-l07.md`. Sources read with `pdftotext -layout` from
`content/aeat-agentes-hacienda/sources/normativa/`: LGSS `BOE-A-2015-11724_lgss_2026-11-11.pdf` (the course's
LGSS entry, `normativa.yaml`), RD 33/1986 `BOE-A-1986-1216_rd-33-1986-regimen-disciplinario_1991-12-31.pdf`,
TREBEP `BOE-A-2015-11719_trebep_2026-10-03.pdf`. Código Penal and Estatuto de los Trabajadores have no file; their
lines record norms the prose names inside another norm's text, as expected.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `9bd4ae1c89` | PASS | LGSS arts. 10.2, 10.3, 250.2; disposición adicional tercera.1 y 3 | Each precept is cited in the prose and nothing else of the LGSS is: art. 10.2 (lines 1149; regímenes especiales a)–e)), art. 10.3 (line 1151; trabajadores del mar y funcionarios por leyes específicas), art. 250.2 (lines 1151–1153; Empleados de Hogar por el título II), d.a. tercera.1 (line 1286; inclusión desde 1-1-2011 a los exclusivos efectos del TRLCPE) and .3 (line 1289; continuidad en Clases Pasivas). All four match the course LGSS file in content and numbering. | — |
| `3618669523` | PASS | RD 33/1986, art. 23, párrafo segundo | The prose names the Código Penal, libro segundo, títulos II y VII (lines 1048–1053). Art. 23 RD 33/1986 reads «tipificados en los títulos II y VII del Libro segundo del Código Penal»; the parenthetical is true. | — |
| `4e3c615d42` | PASS | TREBEP, art. 7, párrafo segundo | The prose names the Estatuto de los Trabajadores and its previsiones on suspensión del contrato (lines 48–50). Art. 7 TREBEP excludes «las previsiones del texto refundido de la Ley del Estatuto de los Trabajadores sobre las suspensiones de los contratos de trabajo»; «texto refundido» and the parenthetical are true. | — |

Voice: the three lines follow the list format of the other «Normativa» lines; no finding.
