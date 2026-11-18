# Writer notes — III.2 (m03-l02)
1. Work list: 1 done (arts. 4–9 Orden PRE/3581/2007 whole, apartados 1 and 2; «(Sin contenido)» letters dropped, so letters skip); 2 done (Servicios, Intervención Delegada, Gabinete; Subdirecciones of undécimo bis/ter/quater as prose); 3 done (primero.4 clause, primero.6, Resolución 26-01-1998, arts. 65–66 Ley 22/2009); 4 done (art. 103 Dos–Diez, Once.1, Once.5, Uno.3, Tres.2); 5 done; 6 done (RT segundo, cuarto.4–6, quinto.1 all, sexto, noveno, undécimo–decimosexto, Orden 1994 decimotercero.2, decimoquinto); 7 done (organs per area; DCGC tercero.1–2); 8 done (esquema removed, arbol extended, DCGC paragraph split); 9 three «No confundir»; 10 not done (glossary marks are not in the lesson file); 11 done.
2. Words 4,145 -> 29,146.
3. Articles added: those of work items 1–7 plus Orden 1994 DA 1.ª.
4. Enumerations: Orden PRE 4–9 (about 200 letters), art. 103.Cinco a)–f), 65.3 a)–n), 66.2 a)–m), Orden 1994 décimo.1, undécimo.2–3, quater.2–3, RT quinto.1, sexto.1, noveno.1, duodécimo.1, decimocuarto.1, decimoquinto.2, decimosexto.1, DCGC tercero.2 a)–k).
5. «No confundir»: Comité Permanente / Comité de Coordinación; Delegados Especiales / Director General; Consejo Superior / Comisión de Seguridad y Control.
6. Deleted: esquema «Los órganos rectores» (repeated one paragraph); the «entre otras funciones» sentence (named). quinto.1.a)/c) sentences subsumed in the full list.
7. Facts with no pack question: about 250.
8. Glossary: none. 9. course.yaml: add Servicios, Consejo Superior, Comisión de Seguridad y Control, personal and financiación.
10. Citation grammar cannot read «apartado undécimo bis/ter/quater» or «primero.Uno»; the first three are cited as «(según el apartado undécimo quater, número N, de la Orden…)» (prose, not a citation), Resolución 26-01-1998 as «apartado primero». Not covered: Res. Aduanas 2021 segundo, Resolución 11-05-1999 (not stored). Esquema rows now cite apartado primero.2.c)–e).

## Fix pass (verifier notes)

- Closing paragraphs of apartado tercero.2 Resolución DCGC (`c7c87339c1`, `77da9fe564`, `6b4d851bd5`, `93771f0601`): moved out of item k) into a paragraph after the list.
- Rows 98 and 195 (ordinal references): already joined in the lesson; nothing to do.
- Normativa: «nombrado en» lines added for the norms with an entry (LGT arts. 111, 154, 155–156, 160–162; Ley 53/1984 art. 9; RGAT art. 59.4; RD 1619/2012 art. 10.1.a)–b); RD 1007/2023; Código Civil art. 1.227; CAU, Reglamento Delegado 2015/2446, Reglamento de Ejecución 2015/2447; Ley 7/2022) and three final lines for norms without an entry. Apartados undécimo bis/ter/quater stay in the prose form (coordinator decision). primero.1 and decimosexto.2 are not in the lines; segundo.8 and art. 93.1.a) LGT already present.
- cites.py: 0 unresolved.

## Reduction pass

- Protected units: art. 103.Tres.1-3 Ley 31/1990 (whole, kept as list), art. 6.1.l) Orden PRE/3581/2007 (row full text), apartados quinto.3 Resolución 13-01-2021 (territorial), cuarto.d), primero.2, primero.3 y decimotercero.3 Orden 1994, segundo.3 Resolución DGT; lines citing them untouched.
- Method (scripted, not per-article rewriting): lettered lists with a parseable lead-in citation became esquemas (rows: letter + first clause, about 8 words, sub-items 4); other added paragraphs/bullets kept the first sentence plus up to one sentence with plazos, numbers, «salvo»/«siempre que»/«sin perjuicio»/rango, long sentences cut at a clause with their citation; a sentence is restored only if it carries the last mention of an article/apartado (two-component unit).
- Enumerations moved to esquemas: 28 (arts. 4.1, 4.2, 5.1, 5.2, 6.1, 6.2, 7.1, 7.2, 8.1, 8.2, 9 Orden PRE/3581/2007; 103.Cinco y 103.Tres.2 Ley 31/1990; 65.3 y 66.2 Ley 22/2009; apartados of the 2021 Resoluciones and the Orden 1994). Apartados «undécimo bis/ter/quater» stay lists (citation grammar).
- Words 29,861 -> 17585. Above the ~15,000 target: esquema rows repeat the Cita (about 8 words each over ~330 rows) and the protected units; reduction by script, so a human pass on the cut sentences («…» fragments) is advisable.

## Reduction pass — DISCARDED (2026-11-17)

Juanjo stopped the reduction pass and discarded its output. The lesson was restored to the verified expansion
(`r2d/expansion/m03-l02.md`) and is rebuilt from HEAD by the build pass (`r2d/spec-build.md`). The notes above about
the reduction describe no text now in the lesson.
