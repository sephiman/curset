# Re-check queue (R2b, 2026-10-17)

Every edit applied after a lesson's blind verification, in order. Each gets one more blind check before the round closes
(`recheck.md`).

| # | Lesson | Origin | Edit applied | Source |
|---|---|---|---|---|
| 1 | m02-l03 | verify-m02 FAIL l03-2 | Art. 53.1.a) LPAC sentence now keeps «en caso de que la Administración no dicte ni notifique resolución expresa en plazo» (verifier's wording) | `BOE-A-2015-10565` LPAC, art. 53.1.a) |
| 2 | m02-l03 | verify-m02 FAIL l03-3 | Added after the certificado sentence: «La Autoridad de Certificación se abrevia AC, o CA por sus siglas en inglés (Certification Authority) (INCIBE, …, 2.1.30; sources/otros/incibe-glosario-ciberseguridad.pdf).» Normativa «Otras fuentes» line names the file; `fuentes.yaml` lists m02-l03 for it | `incibe-glosario-ciberseguridad.pdf`, 2.1.30 |
| 3 | m06-l03 | bloque VI `recheck.md` F1 | Line-wrap fix at `(fuente: \`ms-win-directivas-explorador.html\`).` was applied but never re-checked | — |
| 4 | m01-l11 | verify-m01 FAIL E1 | «Los recursos», first paragraph replaced with the verifier's wording: present tense, «una o varias de estas materias», the art. 50 ter second-paragraph exception (Derecho primario, Derecho internacional público, principios generales, Carta), «tras verificar» | `CELEX-02016E-20250315_tfue_2025-03-15.pdf` art. 256.3; `CELEX-02016M-20250315_tue_2025-03-15.pdf` art. 19.3 TUE, Protocolo n.º 3 art. 50 ter |
| 5 | glossary | verify-m01 note | `g-competencia-exclusiva`: stale `link_except: [m01-l06]` removed (the sentence it covered went with «El Gobierno Abierto en España»; «competencia exclusiva» no longer appears in m01-l06) | — |
| 6 | m03-l03 | verify-m03-l03 FAIL #8 | Art. 93.2 LRJSP paragraph moved unchanged out of «Convenios» into a new «### Organismos públicos» after the consorcios paragraph | LRJSP art. 93.2 |
| 7 | normativa.yaml | verify-m03-l03 FAIL #15a | Código Civil entry: `temas: ["III.1", "III.3"]`, note adds art. 918 for III.3 | — |
| 8 | m05-l04 | verify-m05-b FAIL 1 | Deleted «Esas asistencias son las del artículo 1.1.d) RD 462/2002.» (no text joins concepto 233 and art. 1.1.d)); the concepto 233 sentence stays | Resolución de 20-01-2014, anexo IV, art. 23 |
| 9 | m05-l06 | verify-m05-b FAIL 2 | Art. 56.1–3 RLGS blocks moved unchanged from after art. 34.3 LGS to after the art. 34.4 LGS paragraph, before «### Documentos contables de las subvenciones» | RD 887/2006 art. 56 |
| 10 | m03-l03 | frontend list-shape guard | Normativa line «- Código Civil: art. 918.» → «- Código Civil: art. 918 (cómputo de grados de parentesco).» («918.» read as a stray list marker) | Código Civil art. 918 |
| 11 | m04-l05 | verify-m04-a FAIL 7 | Remoción paragraph (arts. 50.1, 50.5 RD 364/1995) rewrapped to 120, text unchanged | — |
| 12 | m04-l05 | verify-m04-a FAIL 12 | «Lo que más cae»: art. 47.1 line restored (asked by conv2020_X sup. I reserva 1 and conv2025_A sup. II 18); art. 64.3 line removed (asked once; stays in the text); art. 30.1–2 line replaced with the verifier's wording (deducción proporcional, sin perjuicio de la sanción disciplinaria, no devenga ni percibe) | TREBEP art. 30; RD 364/1995 arts. 47.1, 64.3 |
| 13 | m04-l08 | verify-m04-a FAIL 18 | Crédito horario block (art. 68.e) ET table and art. 86.1.d) Convenio único) moved unchanged to the end of «### Derechos y deberes», after art. 5 ET's list | ET art. 68.e); Convenio único art. 86.1.d) |
| 14 | m04-l03 | verify-m04-b FAIL 3b | Second «(hoy: …)» note at art. 25.1 RD 364/1995 removed; paragraph back to its HEAD text (the note stays once, at art. 27.1) | RD 364/1995 art. 25.1 |
| 15 | m04-l03 | verify-m04-b FAIL 3c | Secretaría de Estado paragraph now also names the Oficina de Conflictos de Intereses, con rango de Dirección General | RD 1009/2023 art. 21.C); RD 829/2023 art. 22.3.c) |
| 16 | m04-l03 | verify-m04-b FAIL 1 | TREBEP Normativa line rewrapped after the removal of art. 75.2 | — |
| 17 | m04-l04 | verify-m04-b FAIL 4 | Agrupación familiar paragraph (art. 89.3 TREBEP, art. 17 RD 365/1995) reflowed, text unchanged | — |
| 18 | glossary | golden review | `link_except` added: g-convenio for m01-l01 (art. 94.1 CE «tratados o convenios», international sense, as m01-l03 already is) and g-servicios-comunes for m04-l05 («Servicios Comunes de la Seguridad Social», as m01-l07 already is) | — |
| 19 | m06-l02 | C.4 (2024 X 48 now «Clave oficial discutida») | «Idiomas» item adds «Para instalar la voz de un idioma, ese idioma debe estar establecido como idioma para mostrar» — the page's fact, which the lesson states instead of the disputed key | `ms-win-idioma.html` («Asegúrese de que el idioma en el que se va a usar la voz está establecido como idioma para mostrar») |
| 20 | m04-l05 | ledger open item («hoy» re-check) | First mention of the «Secretario de Estado para la Administración Pública» (art. 54.1 RD 364/1995) gets «(hoy: titular de la Secretaría de Estado de Función Pública)» with art. 22.3.c) RD 829/2023; later mention at art. 48.2 left as written (convention: once); Normativa RD 829/2023 now «arts. 22.2 y 22.3.c)» | RD 364/1995 art. 54.1; RD 829/2023 art. 22.3.c) |
