# RDL 29/2026 — revert list (aeat-agentes-hacienda)

Round R1, 2026-11-11. Real Decreto-ley 29/2026, de 6 de octubre (BOE-A-2026-20823). Not convalidated or derogated on
2026-11-11: the BOE open-data analysis of the RDL lists no later act, and the BOE sumarios of 28-09 to 11-11-2026 carry
no acuerdo.

**Convalidation deadline: 19-11-2026** (publication + 30 working days). Sources and count:

- Dates, from the BOE XML of the RDL (`diario_boe/xml.php?id=BOE-A-2026-20823`): `fecha_disposicion` 20261006,
  `fecha_publicacion` 20261007.
- Art. 86.2 CE (course snapshot `BOE-A-1978-31229_ce_2026-05-20.pdf`): «en el plazo de los treinta días siguientes a su
  promulgación». Art. 151.1 of the Reglamento del Congreso (`BOE-A-1982-5196_reglamento-congreso_2026-07-28.pdf`)
  repeats it; art. 90.1: «los plazos señalados por días en este Reglamento se computarán en días hábiles».
- Holidays: Resolución de 17-10-2025 de la Dirección General de Trabajo, fiestas laborales 2026 (BOE-A-2025-21667,
  https://www.boe.es/boe/dias/2025/10/28/pdfs/BOE-A-2025-21667.pdf, sha256
  `31057b03d927672352b3a5163b30e03d75bddacc3a489626f28f14535ce0facf`): 12-10 is the only national holiday in the
  window; 02-11 («Día siguiente a Todos los Santos») is a holiday in the Comunidad de Madrid, where the Congreso sits.
- Count: 30 days excluding Saturdays, Sundays and 12-10, from the day after publication → **19-11-2026**.
  Variants: also excluding 02-11 (Madrid) → 20-11-2026; counted from promulgation, as art. 86.2 CE words it →
  18-11-2026 (19-11 without 02-11). Thirty calendar days would have ended on 05-11 or 06-11-2026; the Congreso does not
  count that way (art. 90.1) and the BOE shows no derogation. The Mesa fixes the exact count (arts. 90.2 and 91), and
  with the Cortes dissolved (elections of 29-11-2026, RD 806/2026) the vote falls to the Diputación Permanente
  (arts. 78.2 CE and 151.1 of the Reglamento). Re-check the BOE from 18-11-2026.
- The RDL 26/2026, with the same content, was derogated on 02-10-2026 (BOE-A-2026-20526).

**If the Congreso convalidates it:** nothing reverts. Move the entries below from «pendiente de convalidación» to
«convalidado (Resolución de …)» in `normativa.yaml`, and drop the override note of ledger item 2025-53.

**If the Congreso derogates it (or the window lapses):** every precept below returns to its wording before
08-10-2026, and the changes with later effects (01-12-2026, 01-01-2027) never apply. The course files are boe.es
consolidations that already print the RDL wording; the column «Earlier wording» says where the text to restore is.

| Norm (file) | Precepts that revert | RDL 29/2026 provision | Effect | Tema | Earlier wording |
|---|---|---|---|---|---|
| LIRPF (`BOE-A-2006-20764_lirpf_2026-11-11.pdf`) | DA 55.ª (imputación at 1,1 % for 2026) | art. 6, primero | 01-01-2026 | III.15 | not in the file: boe.es consolidation before 08-10-2026 |
| LIRPF | arts. 7.ñ), 23.2, 67.1, 68.6; sección 8.ª of título X (art. 95 ter); DA 5.ª.4, 26.ª, 50.ª.6, 58.ª.5, 62.ª.6; new DA 65.ª and 66.ª (delete); DT 15.ª.3 (delete), DT 38.ª | art. 6, segundo, Uno–Catorce | 08-10-2026 | III.15, III.16 | not in the file: boe.es consolidation before 08-10-2026 |
| LIRPF | art. 24; art. 85.1 (scale 1,1–3 %) — `cambios_pendientes` entry is dropped | art. 6, tercero, Uno–Dos | 01-01-2027 | III.15 | in the file, «Redacción anterior» under each article |
| LIVA (`BOE-A-1992-28740_liva_2026-10-07.pdf`) | art. 20.Uno.23.º e´); art. 91.Uno.2.2.º, 91.Uno.2.10.º, 91.Dos.1.6.º — `cambios_pendientes` entry is dropped | art. 7, Uno–Cuatro | 01-12-2026 | III.18 | **not in the file** (boe.es prints the new wording with no notice): the wording in force until 30-11-2026 must come from the consolidation before 07-10-2026 |
| TRLRHL (`BOE-A-2004-4214_trlrhl_2026-10-07.pdf`) | art. 72 (title, 4; new 4 bis and 4 ter deleted) | art. 8 | 08-10-2026 | III.1 | not in the file |
| TRLRHL | art. 107.4 coefficients — `cambios_pendientes` entry and the `cifras_anuales` row change: the table of the «Redacción anterior» stays for 2026 and after | art. 10 | 01-12-2026 | III.1 | in the file, «Redacción anterior» |
| RIRPF (`BOE-A-2007-6820_rirpf_2026-10-07.pdf`) | arts. 41 bis, 69, 75, 76, 93, 94; DA 8.ª | DF 3.ª | 08-10-2026 | III.15, III.16 | not in the file |
| RGAT (`BOE-A-2007-15984_rgat_2026-10-07.pdf`) | art. 39 quater (deleted) | DF 4.ª | 08-10-2026 | III.4 | not needed: the article did not exist |
| LEC (`BOE-A-2000-323_lec_2026-10-07.pdf`) | arts. 22.6, 685.2 | art. 5 | 08-10-2026 | — (the course uses only arts. 605–607) | not needed |

Course items that depend on it:

- `normativa.yaml`: the `note`, `amended_2025_2026` line, `cambios_pendientes` and `cifras_anuales` rows of the five
  entries above that name BOE-A-2026-20823; the header paragraph on unconvalidated RDLs.
- `docs/aeat-official-exams-ledger.md`, item 2025-53 (LIRPF art. 85.1): `norma modificada` only through this RDL; if it
  is derogated, key B is vigente again and the item moves to `vigente`.
- Lessons: none yet (R1 stubs carry only the «Cambio pendiente» line in the Normativa blocks of III.1, III.15 and
  III.18). From R2 on, every sentence that cites a precept in the table carries the «(…, desde DD-MM-YYYY)» or
  «pendiente de convalidación» mark, so the flip stays mechanical.
- Files to download on a derogation: the boe.es consolidations of LIRPF, LIVA, TRLRHL and RIRPF dated after the
  derogation (boe.es republishes the earlier wording); the stubs' Normativa lines and these entries then point at them.
