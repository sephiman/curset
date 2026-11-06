# Verification — `m02-l06`, re-check 2 (blind)

Verifier: blind, 2026-11-06. Did not write the lesson. Files read: `docs/age-verification/c2/bloque-ii/pending/m02-l06.md`,
`content/age-auxiliar-c2/es/lessons/m02-l06.md` (line 158 and the citation at line 92),
`content/age-auxiliar-c2/sources/otros/fuentes.yaml` (entry `ms-copilot-introduccion.html`), and the saved page
`content/age-auxiliar-c2/sources/otros/ms-copilot-introduccion.html` (sha256 `0c23b4a1…69153f3`, equal to `fuentes.yaml`;
`lang="es-es"`; `<h1>` «Introducción a Microsoft Copilot»; `<title>` «¿Qué es Microsoft Copilot? | Microsoft Learn»).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `db2d4d5f80` | PASS | fuentes.yaml; ms-copilot-introduccion.html | title is the page's `<h1>` heading, which `fuentes.yaml` records as «(encabezado: «Introducción a Microsoft Copilot»)»; host learn.microsoft.com right; «consultado el 05-11-2026» equals `consultado: "2026-11-05"`; the file is cited in the prose (line 92). For the coordinator, not the line: the `fuentes.yaml` entry has `lessons: []` (m02-l06 missing), its `url` differs from the page's canonical (`…/es-es/copilot/plan/copilot-overview`), and line 158 is 128 characters, past the file's wrap width | — |

PASS 1, FAIL 0.
