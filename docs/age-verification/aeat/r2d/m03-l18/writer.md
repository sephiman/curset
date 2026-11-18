# Writer notes — m03-l18 (III.18, IVA I)

Method: the new text was generated from the snapshots by script (paragraphs copied from the LIVA / RIVA PDFs, ordinals and letters kept, one citation per item or lead-in) and the unchanged verified sentences were kept from the previous file.

1. Work list
- 1 art. 20.Uno whole (1.º–28.º, 21.º and 27.º «(Suprimido)») as a list, sub-letters nested: done (section «Exenciones en operaciones interiores»). No esquema (list with ordinals, spec-write allows it). 23.º e´) carries «(desde 01-12-2026, Real Decreto-ley 29/2026, convalidación pendiente)».
- 2 art. 20.Tres + RIVA 4, 6, 7: done («Entidades o establecimientos de carácter social»).
- 3 RIVA 8 (renuncia): done.
- 4 art. 21 whole + RIVA 9 whole (viajeros a)–e), tres meses, quince días): done.
- 5 art. 20 bis, 22 (Uno–Dieciséis as a list, definitions of navegación marítima/aérea), 23, 24, 25, RIVA 10–13: done. Art. 22 is a list, not an esquema: an esquema row must be cited in prose and would duplicate it.
- 6 art. 70.Uno whole and 70.Dos: done.
- 7 arts. 71, 72, 73 + RIVA 22, 23 (art. 74 derogado, no text): done.
- 8 art. 69.Dos a)–l), 69.Tres 1.º–5.º: done.
- 9 art. 68 whole (Uno–Seis): done.
- 10 art. 7 whole (1.º–12.º, 8.º A)–F) with a´)–m´): done.
- 11 art. 11.Dos 1.º–16.º: done.
- 12 art. 6.Dos a)–g), 6.Tres a)–d) as lists: done.
- 13 art. 9.1.º c) exclusions and «sin perjuicio» (3), 9.1.º d) a´)–d´), 9.3.º a)–h): done.
- 14 arts. 8.Tres, 8 bis, 9 bis, 10, 5.Cuatro, RIVA 1, 1 bis, art. 3.Dos.1.º a)–b): done (written whole, not one line).
- 15 three «No confundir» blocks: done (see 5).
- 16 split of the long paragraphs and removal of «(`m03-l19`)»: done.
- 17 Normativa re-derived from the parsed citations; cambio-pendiente line kept; «Lo que más cae» unchanged. course.yaml summary and glossary exception for `g-convenio` (l. 13): not done here (outside my files); see 8 and 9.

2. Words: 6276 → about 29,800 (wc -w).

3. Articles treated now: 5.Cuatro, 6.Dos–Tres whole, 7.1.º a)–c), 7.8.º B)–F), 7.10.º–11.º, 8.Tres, 8 bis, 9 bis, 9.3.º a)–h), 10, 11.Dos 4.º 5.º 9.º 10.º 13.º 14.º, 13.1.ª a)–g), 20.Uno all numbers, 20.Tres, 20 bis, 21 whole, 22 whole, 23, 24, 25, 68–73, RIVA 1, 1 bis, 4, 6–13, 22, 23.

4. Enumerations completed: 20.Uno 10 → 26 numbers in force; 6.Dos 4 → 7; 6.Tres 2 → 4; 7 10 → 12; 7.8.º B) 0 → 4; 7.8.º F) 3 → 13; 11.Dos 10 → 16; 9.1.º c) sin perjuicio 1 → 3; 9.1.º d) 1 → 4; 9.3.º 0 → 8; 13.1.ª exclusions 1 → 7; 21 2 → 7; 22 2 → 16 apartados; 68.Tres 0 → 4; 69.Dos 3 → 12; 69.Tres 2 → 5; 70.Uno 4 → 9; 3.Dos.1.º 3 territories → 13.
   The old sentence «La exención de la letra a) del número 18.º no se extiende…» (l. 177) is now inside 18.º a) and was removed as a duplicate.

5. «No confundir»: autoconsumo de bienes (art. 9.1.º a) LIVA) / de servicios (art. 12.2.º LIVA), after art. 12; comisionista en nombre propio (art. 8.Dos.6.º) / ajeno (art. 11.Dos.15.º), after art. 11; exportación (art. 21.1.º) / entrega a otro Estado miembro (art. 25.Uno), after RIVA 13.

6. Reworded without being named: the old paraphrase items of art. 7, 20.Uno, 21, 22, 68.Dos, 69.Dos, 70 were replaced by verbatim text (the arts. are in the work list). Verbs of lead-ins «Estarán/Se entenderán» put in present tense («Están exentas»).

7. Facts added with no pack question: about 60 article units (every unit above except those in the pack list in the map header).

8. Glossary proposals: none.

9. Course summary: «Naturaleza y ámbito del IVA, hecho imponible de entregas y servicios, las exenciones de los artículos 20 a 25 completas y las reglas de localización de los artículos 68 a 73.»

10. Sources missing: the wording of art. 20.Uno.23.º e´) in force until 30-11-2026 is not in any snapshot (the LIVA file and the RDL 29/2026 print only the wording from 01-12-2026), so the lesson gives that wording with the pending mark and no earlier text. Cross-reference fixes owed: `g-convenio` link at l. 13 (glossary, not mine). Unresolved citations: none (cites.py through a sandbox copy because another writer's m03-l13 breaks the live course load).

## Fix pass (verifier notes), R2d fixer 2

- Added Normativa line «LIVA, versiones del art. 20: art. 20.Uno.23.º e´), en la redacción vigente hasta el 30-11-2026.». cites.py: 0 unresolved.


## Reduction pass (2026-11-17)

- Protected articles (kept whole, pack «Norma» lines and «Lo que más cae»): LIVA 7, 8, 9, 12, 13, 20, 21, 22.
- Method: script over the R2d-added blocks only (HEAD text untouched). Every other article added in R2d keeps at most its first four sentences (about 170 words), each cut paragraph ending with its own citation; lead-ins of lists, «El artículo N del X regula:» lines, headings, «No confundir» blocks, worked examples, «Lo que más cae» and «Normativa» untouched.
- Enumerations moved to esquemas (flat table, one row per item with its letter or ordinal, nested items flattened with their path, «Cita» = the lead-in's citation, item-level citations dropped from the cells): 46.
- Words (wc -w): 29,461 -> 31,522. Esquema markup (pipes and the repeated «Cita» column) counts as words, so the net cut is smaller than the prose removed.
- Per reduced article, words before -> after (cut by more than 10 words):
  - ? 20: 447 -> 351
  - ? 7: 27 -> 0
  - LIVA 11: 415 -> 91
  - LIVA 20: 3894 -> 2736
  - LIVA 21: 1102 -> 314
  - LIVA 22: 3360 -> 2931
  - LIVA 23: 346 -> 164
  - LIVA 24: 712 -> 259
  - LIVA 25: 401 -> 205
  - LIVA 68: 1197 -> 337
  - LIVA 69: 631 -> 245
  - LIVA 7: 1508 -> 225
  - LIVA 70: 1284 -> 74
  - LIVA 73: 408 -> 207
  - LIVA 8: 583 -> 210
  - RIVA 10: 1000 -> 97
  - RIVA 12: 206 -> 79
  - RIVA 13: 230 -> 166
  - RIVA 9: 1977 -> 59
- cites.py: 0 unresolved; index_sources.py --course aeat-agentes-hacienda: no validation error.

## Reduction pass — DISCARDED (2026-11-17)

Juanjo stopped the reduction pass and discarded its output. The lesson was restored to the verified expansion
(`r2d/expansion/m03-l18.md`) and is rebuilt from HEAD by the build pass (`r2d/spec-build.md`). The notes above about
the reduction describe no text now in the lesson.
