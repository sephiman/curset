# Verify re-check 1 — `m03-l16`

Blind re-check, 2026-11-14 (Opus). Sources: LIRPF `BOE-A-2006-20764_lirpf_2026-11-11.pdf`, RIRPF `BOE-A-2007-6820_rirpf_2026-10-07.pdf`, RDL 29/2026 marks per `normativa.yaml` and `docs/age-verification/aeat/r1/rdl-29-2026-revert-list.md`. Esquema «Deducciones en la cuota del artículo 68 LIRPF» (lines 282–294): renders as a table (directive, header, separator, nine 4-cell rows, closing `:::`); every row checked against arts. 68.1–68.6 and 69.1–2 LIRPF and passes. Worked examples (lines 33–39, 212–220, 422–428) recomputed with python3: correct.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `ae6510b765` | PASS | DA 39.ª.1 LIRPF | — | — |
| `56a37141cd` | PASS | art. 51.2.a) LIRPF | 1.º–3.º complete | — |
| `b86aaed495` | PASS | art. 51.3 LIRPF | a)–e) complete | — |
| `ce4772ab4d` | PASS | art. 51.5 LIRPF | — | — |
| `767f77d466` | PASS | DA 16.ª LIRPF | — | — |
| `cf1d7bcc83` | PASS | art. 53.2 LIRPF | — | — |
| `d011244982` | PASS | art. 54.5 LIRPF | a)–c) complete | — |
| `45ef1ad01c` | PASS | art. 54.5 LIRPF, último párrafo | — | — |
| `c4bdec91a1` | PASS | art. 64 LIRPF | — | — |
| `351b396710` | PASS | art. 65 LIRPF | second scale matches (60.000 → 8.950,75; 22,50 % en adelante) | — |
| `acedf62636` | PASS | art. 68.1.2.º LIRPF | a)–c) complete | — |
| `63cc311e29` | PASS | art. 68.1.5.º LIRPF | — | — |
| `9f1f5f74d1` | PASS | art. 68.2.b) LIRPF | — | — |
| `76c74477d6` | PASS | art. 58.1 RIRPF | a)–d) complete | — |
| `f38944edcc` | PASS | art. 68.5 LIRPF | a)–c) complete | — |
| `9d702d7164` | PASS | art. 59.1 RIRPF | — | — |
| `b1f99ef54a` | PASS | art. 59.2 RIRPF | a)–c) complete | — |
| `b298dd0636` | PASS | esquema header | header row of a well-formed table | — |
| `e41cd7a825` | PASS | arts. 68.2.a) y 69.2 LIRPF | — | — |
| `7b82c9be84` | PASS | arts. 68.3.a) y 69.1 LIRPF | — | — |
| `a7f9372459` | PASS | art. 68.6 LIRPF (RDL 29/2026) | figures match; convalidación mark right | — |
| `a25a1b2d12` | PASS | DA 50.ª.1–3 LIRPF | 20/40/60 %, 7/30 %, 5.000/7.500/5.000 y 15.000 euros match | — |
| `27c16981f5` | PASS | DA 58.ª.1–3 LIRPF | — | — |
| `90b9944c4d` | PASS | DA 62.ª.1–3 LIRPF | — | — |
| `0d95208fba` | PASS | DA 62.ª.6 LIRPF (RDL 29/2026) | DA 62.ª.6 is on the revert list; mark right | — |
| `f9aadc698f` | PASS | DT 15.ª.1–2 LIRPF | — | — |
| `23af1f86d0` | PASS | DT 18.ª.1–2 LIRPF | — | — |
| `906ccd6f8c` | PASS | art. 81.3 LIRPF | — | — |
| `f16977872a` | PASS | art. 60 bis.1 RIRPF | — | — |
| `f4c38500c8` | PASS | DA 61.ª.1 LIRPF | — | — |
| `67e7d5f62e` | PASS | art. 96.3.a) LIRPF | «No confundir» line, faithful cut with both 1.º and 2.º | — |
| `2b43d910d8` | PASS | art. 97.5 LIRPF | — | — |
| `71e9033743` | PASS | art. 63.2 RIRPF | — | — |
| `0d2294167b` | PASS | art. 104.2 LIRPF | — | — |
| `1fe0ab59f3` | PASS | art. 104.3 LIRPF | — | — |
| `2971ad5170` | FAIL | Normativa, LIRPF | the prose names the disposición adicional novena LIRPF (line 100, DA 16.ª sentence); not listed | LIRPF (Ley 35/2006): arts. 7, 8.2, 10.1, 14.4, 15.2–4, 17.1.c), 17.2.a), 18.2, 20, 25.1–3, 30.2, 32.3, 38.2, 44–49, 50.1–3, 51.1–9, 52.1–2, 53.1–2, 54.1–5, 55, 56.1–3, 57–61, 62, 63.1–2, 64, 65, 66.1–2, 67.1–2, 68.1–6, 69.1–2, 70.1–2, 75, 79, 80.1–3, 81.1–5, 81 bis.1–3, 82.1–3, 83.1–2, 84.1–6, 85, 91.10, 92.4, 95, 96.1–9, 97.1–6, 98.1–6, 99.8, 99.11, 102, 103.1–5, 104.1–3, 104.5, disposiciones adicionales 9.ª, 10.ª, 11.ª, 16.ª, 39.ª, 48.ª, 50.ª, 57.ª, 58.ª, 61.ª y 62.ª y disposiciones transitorias 15.ª y 18.ª. |
| `4063faeb81` | FAIL | Normativa, LIRPF cambio pendiente | the lesson cites art. 85 LIRPF (lines 11, 396, 488), and `normativa.yaml` `cambios_pendientes` has art. 85.1 changed by the RDL 29/2026 with effects from 01-01-2027; the note omits it (m03-l15 carries it) | Cambio pendiente por el Real Decreto-ley 29/2026, de 6 de octubre, sin convalidar, con efectos desde el 08-10-2026 (arts. 67.1 y 68.6, disposición adicional 62.ª.6 y disposición transitoria 15.ª.3). Cambio pendiente por el Real Decreto-ley 29/2026, de 6 de octubre, sin convalidar, con efectos desde el 01-01-2027 (art. 85.1). |
| `c1c624651c` | PASS | Normativa, LIS | — | — |
| `902b5ce605` | PASS | Normativa, Ley 20/1991 | — | — |
| `eaee1e7063` | FAIL | Normativa, TRLPFP | the prose also names the disposición adicional primera of the texto refundido (art. 51.2.a) 3.º and 51.4 LIRPF), and art. 67 is named in the DA 16.ª LIRPF sentence too | Texto refundido de la Ley de Regulación de los Planes y Fondos de Pensiones (Real Decreto Legislativo 1/2002): arts. 5, 8 y 67 y disposición adicional primera, nombrados en los arts. 51 y 52 y en la disposición adicional decimosexta LIRPF. |
| `c307822ac5` | FAIL | Normativa, Código de Comercio | the prose also names the Código de Comercio in art. 104.2 LIRPF (line 475) | Código de Comercio: art. 42, nombrado en el art. 68.1.2.º LIRPF; nombrado también en el art. 104.2 LIRPF. |
| `47896e5f2c` | FAIL | Normativa, normas nombradas | named in the prose and missing from the block: Ley del Impuesto sobre el Patrimonio, art. 4.8.dos.a) (art. 68.1.2.º LIRPF, line 241; in `normativa.yaml` as Ley 19/1991); texto refundido de la Ley del Impuesto sobre Sociedades, Capítulo II del Título VII and art. 43.2 (arts. 45 and 54.5 LIRPF, lines 11 and 120); Directiva 2003/41/CE (art. 51.1.2.º LIRPF, line 94); Real Decreto-ley 19/2021 (DA 50.ª, line 298); Real Decreto-ley 5/2023 (DA 58.ª, line 299); none of the last four is in `normativa.yaml` | Ley 19/1991 (Impuesto sobre el Patrimonio): art. 4.8.dos.a), nombrado en el art. 68.1.2.º LIRPF. Nombradas por su materia o por su número y no incluidas en `normativa.yaml`: texto refundido de la Ley del Impuesto sobre Sociedades (Real Decreto Legislativo 4/2004), Capítulo II del Título VII y art. 43.2, nombrados en los arts. 45 y 54.5 LIRPF; Directiva 2003/41/CE, nombrada en el art. 51.1.2.º LIRPF; Real Decreto-ley 19/2021, nombrado en la disposición adicional quincuagésima LIRPF; Real Decreto-ley 5/2023, nombrado en la disposición adicional quincuagésima octava LIRPF; Ley 28/2022 (empresas emergentes), Ley 19/2021 (ingreso mínimo vital), Ley 13/1985 (coeficientes de inversión), Real Decreto 1006/1985 y Real Decreto 1467/1997. |

PASS 37 · FAIL 5
