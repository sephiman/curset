# Verification — `m01-l10`, re-check 4 (blind)

- Verifier: blind verifier (opus), did not write the lesson.
- Date: 2026-11-06.
- Files read: `docs/age-verification/c2/bloque-i/spec.md` («Verifier (blind)»), `docs/prose-voice.md`,
  `docs/age-verification/c2/bloque-i/pending/m01-l10.md`, `content/age-auxiliar-c2/es/lessons/m01-l10.md` (section «La
  Presidencia», the «Normativa» list, every `fuente:` file name in the lesson),
  `content/age-auxiliar-c2/sources/otros/eurlex-decision-2016-1316.pdf` (`pdftotext -layout`, art. 1 and the annex),
  `content/age-auxiliar-c2/sources/otros/consilium-presidencia.html` (HTML stripped),
  `content/age-auxiliar-c2/sources/otros/fuentes.yaml` (entries for the eight files; sha256 of the two new files matches).
- Result: 4 PASS, 0 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `716c6b731e` | PASS | art. 1.1 and 1.3 Decisión (UE) 2016/1316 | Art. 1.1 rewrites art. 1 of Decisión 2009/908/UE: the order from 1-07-2017 to 31-12-2030 and its division into groups of three «se fijan en el anexo I». Art. 1.3 replaces the text of anexo I with the annex of the 2016 decision. Title and date «del Consejo, de 26 de julio de 2016» are exact | — |
| `ef47ef9623` | PASS | Anexo, Decisión (UE) 2016/1316 | The annex table reads «Polonia Enero-junio 2025», «Dinamarca Julio-diciembre 2025», «Chipre Enero-junio 2026», consecutive rows | — |
| `fbfac45c67` | PASS | fuente: consilium-presidencia.html | The page (heading «La Presidencia del Consejo de la UE») lists «Polonia: enero a junio de 2025 (en trío con Dinamarca y Chipre)», and the same trio for Dinamarca and Chipre. «A fecha de 06-11-2026» matches `consultado: "2026-11-06"` in fuentes.yaml. Voice clean | — |
| `ceab708c61` | PASS | fuentes.yaml | The eight files listed are exactly the eight `fuente:` files the lesson cites (consilium-presidencia, curia ×2, eurlex-decision-2016-1316, ue-comision-europea, ue-consejo, ue-paises, ue-parlamento-europeo); all have `lessons: [m01-l10]`. Six carry `consultado: "2026-10-16"`; eurlex-decision-2016-1316.pdf and consilium-presidencia.html carry `consultado: "2026-11-06"`, as the line says | — |
