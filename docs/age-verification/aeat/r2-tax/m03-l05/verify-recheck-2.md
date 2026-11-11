# Verification re-check 2 — `m03-l05` (blind)

Verifier: opus, 2026-11-11. Sources: `normativa.yaml` entries of the LPAC, LEC, LOFCA, Concierto (Ley 12/2002) and Convenio con Navarra (Ley 28/1990); snapshot PDFs of the LGT (2024-12-21, art. 106.1), RGAT (2026-10-07, art. 103.f)) and LPAC (2024-11-06). LPAC precepts cited in the prose: art. 30.4 (l.275), art. 14.2.a) (l.279), art. 43.2 (l.306); no other. The Ley 25/2003 has no entry in `normativa.yaml`, so its full title stands in for a `short`.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `8700e08cee` | PASS | LPAC citations in the prose | starts with the `short` «Ley 39/2015 (LPAC)»; lists exactly 14.2, 30.4 and 43.2, the three cited; no cambio pendiente (`cambios_pendientes: []`) | — |
| `d36c8f2df5` | PASS | art. 106.1 LGT; LEC entry | `short` «LEC (Ley 1/2000)»; l.289 names the LEC only through art. 106.1 LGT, with no article; no cambio pendiente on any cited precept | — |
| `3a8769cdb6` | PASS | art. 103.f) RGAT | full title matches the one the RGAT gives («Ley 25/2003, de 15 de julio, por la que se aprueba la modificación del Convenio Económico entre el Estado y la Comunidad Foral de Navarra»); art. 51 is the precept named in letter f) (l.244) | — |

Every norm named in the prose now has its «Normativa» line.

PASS 3 · FAIL 0
