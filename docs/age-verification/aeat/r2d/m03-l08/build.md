# Build — III.8 (`m03-l08`), R2d, 2026-11-17

Words (`wc -w`): HEAD 9,018 (esquema rows 707; 8,311 without) → built 22,850 (esquema rows 4,953; 17,897 without).
Ratio excluding esquema rows: 2.15 to HEAD without rows; 1.35 of the 1.6 target (13,298). Above the target: the range
holds about 100 articles (HEAD treated a third in full); every article states its rule, conditions and exceptions, every
legal enumeration is an esquema (or, for the Resolución, a bullet list), and only the sentences below were left out.

Method: the pool (`expansion/m03-l08.md`) is HEAD's lesson with every verified addition and correction in the norm's
order, so the build is the pool with the sentences below left out and the legal lists turned into esquemas. «Lo que más
cae» is HEAD's ten lines (the pool's are identical). A script (`scratchpad/b08/build.py`) wrote the file from the pool
lines so the bytes stay identical.

## Sentences added (not in HEAD): 284 prose + 132 esquema rows (109 from list items)

- (a) R2b removals: none (the map lists none).
- (b) Review items (about 41 sentences with citations to the articles of the four items): denuncia pública (art. 114.1–3 LGT);
  órganos de inspección (166.2–3, 167–170 RGAT; Resolución de 24-03-1992 Uno.1–2, Cinco.1, Cinco.2.c, Siete; the Inspector
  Jefe who dicta las liquidaciones); retroacción (art. 150.7 LGT, art. 197.8 RGAT); reducción de la sanción (art. 156.4,
  188.1 LGT, with the pointer to III.13 for 188.2–4).
- (c) Every other article not or partly treated at HEAD: 115.1–3, 116 LGT; 166.2–3, 167–170, 171.2–3, 172.2, 173.1, 173.4,
  174, 176.1–2, 178.1, 178.4–5, 179, 184.2–3, 185.1–3, 186–188, 189.2–3, 190, 191.3–4, 192–197 RGAT; 97–100 RGAT; 150.3
  (closing paragraphs), 150.6.a, 155.5 (second paragraph), 158.3–5, 159 LGT; 193–194 RGAT; 87.2 second paragraph and
  87.5 RGAT; 101.4.b LGT. The remaining new sentences are the esquema rows of the lists below.
- (d) The three «No confundir» blocks (estimación indirecta/disconformidad; plazos de las actas; medidas cautelares).
- (e) HEAD sentences replaced by their pool form (36): art. 117.1 sentence (the `m03-l07` id becomes «tema III.7»), the
  «entre otros» lead-ins of art. 171.1 and 176.1, 172.3, 87.3 lead-in, «locales del obligado tributario» (152.1–2),
  87.1, 87.2, 87.5 (two paragraphs), 178.5, 179.1–3, 150.3 c), e), f) and the closing paragraphs, 150.5, 185.1–2,
  186.1, 187.3, 188.1–2, 189.1, 190.1, 190.3 (the «entre otras causas» sentence), 181.4, and the Normativa lines.
- Normativa: the pool's lines rebuilt from what the built lesson cites. New text versus the pool: the RGAT line (the left-out
  sentences below remove 168.2, 170.4, 170.6, 99.3, 193.5–6, 194.4 and 194.6 from the cited set: `168.1, 168.3–4`,
  `170.1–2, 170.5, 170.7–8`, `99.1–2, 99.4`, `193.1–4`, `194.1–3, 194.5`). Versus HEAD: new lines for the Resolución
  de 24-03-1992, LPAC art. 14, RGRVA (art. 66.4), art. 47 ter of the Concierto, and the final «no figuran en `normativa.yaml`» line;
  LGT and RGAT lines extended.

## Enumerations as esquemas (109 rows from items; header «Elemento | Contenido | Cita», the only header the pool verified for these)

166.2 a)–b); 166.3 a)–c); 97.1 a)–e); 98.1 a)–g); 98.2 a)–e); 98.3 a)–g); 100.2 a)–b); 176.1 a)–e); 174.2 a)–d); 178.5 a)–b);
88.2 a)–d); 184.2 a)–c); 158.3 a)–d); 193.4 a)–e); 190.2 a)–d); 190.3 a)–d); 190.4 a)–e); 191.4 a)–b); 186.8 a)–c); and,
repeating nested bullets of the prose as verbatim sub-items: 186.7 a)–c); 187.2 a)–b); 187.3 a)–c); 188.4 a)–b). Items of
two or more sentences are split in one row per sentence (the checker verifies sentences). Lists HEAD already had whole stay as
bullets (141, 171.1, 173.5, 87.3, 153, 151.1, 182.2, 178.3, 150.1, 150.3, 150.6, 155.2, 155.3, 156.3, 158.1) and the
three existing HEAD esquemas stay. Exception: Resolución de 24-03-1992, apartado Uno.1 (a–b) and Cinco.1 (a–c) stay as
verified bullet lists: the citation grammar cannot write «apartado Uno.1 de la Resolución» in an esquema Cita cell, so
an esquema fails `cites.py`.

## Checks

- build_check: `m03-l08: HEAD 271 · added byte-identical 306 · esquema rows from items 109 · not in pool 1`.
- cites.py: 432 citations, 0 unresolved.
- split_paragraphs: 0 paragraphs split.
- index_sources (`--course aeat-agentes-hacienda`): no error names m03-l08 (run fails on m03-l02, another builder's lesson: «apartado undécimo quater.2/3 Orden de 2 de junio de 1994» cited by esquema rows with no prose citation).

## Pool sentences left out (each states no rule, condition or exception of its article: development or procedure)

- art. 167.1 RGAT, «Los resultados de esas actuaciones inspectoras se documentan en diligencia …»: how the result is recorded, no duty beyond 99 RGAT.
- art. 168.2 RGAT, escrito motivado and the month to answer: procedure between Administrations.
- art. 170.4 RGAT (annual drafting of the plan, apoyo informático) and 170.6 (revision of the plan): organisation.
- art. 170.8 RGAT second sentence (propuestas de otros órganos): repeats the planning source of 170.5.
- art. 99.3 RGAT («Las diligencias se incorporan al respectivo expediente»): repeats art. 97.3 for comunicaciones and 98.
- art. 193.5 RGAT (lead-in, items a)–b) and the «Entre otros…» sentence; disociación of third-party data) and 193.6 (single informe): procedure; the rules of art. 193.1–4 are in.
- art. 194.4 RGAT (both bullets: composition of the Comisión, repeats art. 159.1 LGT) and 194.6 (quarterly publication): organisation.

## Pool gaps

None: every article of the ranges has pool sentences.

## Sentences that do not stand on their own where they now sit

- «Esa comprobación e investigación puede realizarse …» (art. 115.1, first bullet follows the sentence it refers to).
- «Ese acuerdo no puede ser objeto de recurso …» (art. 181.5 RGAT, after the esquema of the medidas cautelares plazos and the
  «No confundir» block: «ese acuerdo» points back to the acuerdo motivado of the previous paragraph, now separated by them).
- «En ese caso se procede de la siguiente forma:» (art. 187.3 RGAT, nested bullet; fused with its lead-in).
- «Dicho acuerdo se notifica al obligado tributario …» (art. 188.4 RGAT, nested bullet; fused with its lead-in).
- «Asimismo, de acuerdo con el artículo 101.4.a) …» (art. 190.3 RGAT, follows the 190.2 esquema).
- Bullet sentences of art. 169 RGAT and the Siete bullets (Resolución) sit without a lead-in; each cites its own article.
- «En caso de no cumplirse esos requisitos …» (art. 184.2 RGAT, follows the esquema of the requisitos).
- «El contenido de la comunicación de inicio está en la sección de documentación.» (a pointer inside «Iniciación»).
- «Los apartados 2 a 4 del artículo 188 de la LGT se tratan en el tema III.13.» (a pointer, not a rule).

## Not in pool (1: the Normativa RGAT line)

- l.902: `RGAT (RD 1065/2007): arts. 60.4, 61, 61.2, 87.1–5, 88.2, 97.1–3, 98.1–3, 99.1–2, 99.4, 100.1–2, … y 197.1–8.` (the pool's line with the cited set reduced for the left-out sentences).
