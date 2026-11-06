# Verification — `m01-l04`, re-check 1

Verifier: blind verifier (opus), 2026-11-06. Did not write the lesson.

Files read: `docs/age-verification/c2/bloque-i/pending/m01-l04.md` (now 0 pending: the fixed sentence is byte-identical to
the already-PASS `d1900d4aa7`), `docs/age-verification/c2/bloque-i/verify/m01-l04.md` (the FAIL on `a9bcad53b7`),
`content/age-auxiliar-c2/es/lessons/m01-l04.md` (lines 223 and 290),
`content/age-auxiliar-c2/sources/normativa/BOE-A-1985-12666_lopj_2025-02-17.pdf` (pdftotext -layout, art. 65).

Result: 1 PASS, 0 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `d1900d4aa7` | PASS | art. 65.1.º.e LOPJ | the fixed «Lo que más cae» line (290, formerly `a9bcad53b7`) now carries the exception on the whole 1.º, «salvo que corresponda en primera instancia a la Sección de lo Penal del Tribunal Central de Instancia», and letter e) word for word. It is identical to line 223, so it has that sentence's id (sha1 checked) | — |
