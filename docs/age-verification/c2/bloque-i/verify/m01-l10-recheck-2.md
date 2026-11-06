# Verification — `m01-l10`, re-check 2 (blind)

- Verifier: blind verifier (opus), did not write the lesson.
- Date: 2026-11-06.
- Files read: `docs/age-verification/c2/bloque-i/spec.md`, `docs/prose-voice.md`, `content/age-auxiliar-c2/sources/normativa.yaml`,
  `content/age-auxiliar-c2/sources/otros/fuentes.yaml`, `docs/age-verification/c2/bloque-i/pending/m01-l10.md`,
  `content/age-auxiliar-c2/es/lessons/m01-l10.md`, `sources/otros/ue-paises.html` (visible text; the saved copy is page 1 of 2,
  results 1–20 of 27, Alemania to Lituania).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `6e118d1e43` | PASS | ue-paises.html (España) | «Estado miembro de la UE desde 1986» | — |
| `e2a6d18082` | PASS | ue-paises.html (Austria, Finlandia; Chequia … Lituania) | Austria and Finlandia: desde 1995. Chequia, Chipre, Eslovaquia, Eslovenia, Estonia, Hungría, Letonia, Lituania: desde 2004. Both lists are marked «entre otros», which is right: the saved page stops at Lituania, so the other 1995 and 2004 entrants are not in the file and the sentence does not claim them | — |
| `8fed7fbf9b` | PASS | Normativa line, otras fuentes | The prose cites exactly six `sources/otros` files (ue-consejo, ue-paises, ue-parlamento-europeo, ue-comision-europea, curia-tribunal-de-justicia, curia-tribunal-general); all six are listed and nothing else is. fuentes.yaml gives «consultado: 2026-10-16» for all six, matching «a fecha de 16-10-2026» | — |
