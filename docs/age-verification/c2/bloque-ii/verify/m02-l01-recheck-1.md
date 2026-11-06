# Verification — `m02-l01`, re-check 1

Verifier: blind verifier (opus), 2026-11-06. Did not write the lesson.

Files read: `docs/age-verification/c2/bloque-ii/pending/m02-l01.md`, `content/age-auxiliar-c2/es/lessons/m02-l01.md`,
`content/age-auxiliar-c2/sources/otros/boe-analisis-ce.xml`, `content/age-auxiliar-c2/sources/otros/boe-ce-1978-original.pdf`
(pdftotext -layout; sha256 `9a0e042b…0644408` matches `fuentes.yaml`; BOE núm. 311 de 29-12-1978, an official source),
`content/age-auxiliar-c2/sources/otros/fuentes.yaml`.

Result: 2 PASS, 1 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `9d083f2977` | PASS | art. 49 CE (texto original, BOE 29-12-1978) | quote verbatim: «Los poderes públicos realizarán una política de previsión, tratamiento, rehabilitación e integración de los disminuidos físicos, sensoriales y psíquicos»; BOE page is admissible, sha256 matches | — |
| `bfdda25e99` | FAIL | art. 49.2 CE; boe-analisis-ce.xml | facts right (art. 49.2 CE; the análisis: «SE MODIFICA el art. 49, por Reforma de 15 de febrero de 2024»), but line 138 now reads «- - Se atenderán…»: the earlier replacement carried its own list marker, so the item renders as a nested list; the replacement drops the inner «- » | Se atenderán particularmente las necesidades específicas de las mujeres y los menores con discapacidad (art. 49.2 CE); el artículo 49 tiene la redacción de la reforma de 15 de febrero de 2024 (fuente: `boe-analisis-ce.xml`). |
| `9c30fa0448` | PASS | sources/otros/fuentes.yaml | the lesson cites exactly `boe-analisis-ce.xml` and `boe-ce-1978-original.pdf`; consultado dates 16-10-2026 and 06-11-2026 match `fuentes.yaml` | — |
