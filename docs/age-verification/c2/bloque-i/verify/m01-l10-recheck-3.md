# Verification — `m01-l10`, re-check 3 (blind)

- Verifier: blind verifier (opus), did not write the lesson.
- Date: 2026-11-06.
- Files read: `docs/age-verification/c2/bloque-i/spec.md`, `docs/prose-voice.md`, `docs/age-verification/c2/bloque-i/pending/m01-l10.md`,
  `content/age-auxiliar-c2/es/lessons/m01-l10.md` (section «El Tribunal de Justicia de la Unión Europea»),
  `content/age-auxiliar-c2/sources/otros/fuentes.yaml` (entries for both curia pages, consultado 2026-10-16),
  `content/age-auxiliar-c2/sources/otros/curia-tribunal-general.html`, `content/age-auxiliar-c2/sources/otros/curia-tribunal-de-justicia.html`.
- Result: 2 PASS, 0 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `cf268c22d8` | PASS | fuente: curia-tribunal-de-justicia.html; curia-tribunal-general.html | both pages: «uno de los dos órganos jurisdiccionales que forman conjuntamente la institución» / «los dos órganos jurisdiccionales que conforman el Tribunal de Justicia de la Unión Europea»; «a fecha de 16-10-2026» matches `consultado` in fuentes.yaml; it does not contradict art. 19.1 TUE in the paragraph before it, which says what the Treaty provides for | — |
| `0a44e8bd6f` | PASS | fuente: curia-tribunal-general.html; curia-tribunal-de-justicia.html | the quote matches the Tribunal General page verbatim; the Tribunal de Justicia page says it is «uno de los dos órganos jurisdiccionales»; citation form as in the rest of the lesson; voice clean | — |
