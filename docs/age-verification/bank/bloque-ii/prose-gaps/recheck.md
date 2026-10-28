# Prose gaps of «Esquemas bloque II»: re-check of the five fixes, 2026-10-19

Re-check reviewer: wrote neither the change nor `verify.md`. Scope: the five items `verify.md` failed (#4, #54, #59,
#64, #65), each read again with the whole paragraph or esquema it sits in, against `pdftotext -layout` of the files
named in `sources/normativa.yaml`: LO 4/2001 `BOE-A-2001-21090_lo-derecho-peticion_2011-07-28.pdf`, RGPD
`CELEX-32016R0679_rgpd_2016-05-04.pdf`, LOPDGDD `BOE-A-2018-16673_lopdgdd_2025-12-27.pdf`. Citations were run through
the backend's own parser (`tradeschool.citations.lesson.scan_lesson` and `course._esquema_problems`) from a scratch
script over the current working-tree files. Line numbers are those of the lesson files now. `CLAUDE.md` and
`docs/prose-voice.md` read first. No lesson edited, pytest not run, goldens not touched.

Totals: **5 items, 5 PASS, 0 FAIL.**

| # | Lesson | Line | Item | Result | Reason (norm quoted) |
|---|---|---|---|---|---|
| 4 | m02-l01 | 338–343 | Prose: art. 9.1 párr. 1, 9.2 and 9.1 párr. 2 LO 4/2001, in that order | PASS | Norm: «1. La declaración de inadmisibilidad será siempre motivada y deberá acordarse y notificarse al peticionario en los cuarenta y cinco días hábiles siguientes al de presentación del escrito de petición. Cuando la inadmisión traiga causa de la existencia en el ordenamiento jurídico de otros procedimientos específicos para la satisfacción del objeto de la petición, la declaración de inadmisión deberá indicar expresamente las disposiciones a cuyo amparo deba sustanciarse, así como el órgano competente para ella. 2. En otro caso, se entenderá que la petición ha sido admitida a trámite.» «En otro caso» now follows the plazo sentence directly, so it answers the 45-day inadmission again, not the other-procedures case. The 9.1 párr. 2 sentence is verbatim («la declaración» for «la declaración de inadmisión», which the sentence before names). No condition dropped. Parser: `art. 9.1` (l. 339), `art. 9.2` (l. 340), `art. 9.1` (l. 343), all LO 4/2001 art. 9; nothing new. The rest of the paragraph block (arts. 8, 10.1, 10.2, 11.1) and the `plazos` esquema «Algunos plazos de las peticiones» are unchanged; row 1 (arts. 9.1, 9.2 y 10.1) still matches and its apartados are cited in prose; esquema check: no problem |
| 54 | m02-l04 | 181–183 | Prose: art. 22.4 RGPD scope | PASS | Norm: «4. Las decisiones a que se refiere el apartado 2 no se basarán en las categorías especiales de datos personales contempladas en el artículo 9, apartado 1, salvo que se aplique el artículo 9, apartado 2, letra a) o g), y se hayan tomado medidas adecuadas para salvaguardar los derechos y libertades y los intereses legítimos del interesado.» Prose: «Las decisiones de los tres casos del artículo 22.2 no se basarán …». Apartado 2 has exactly three letters (a) contrato, b) Derecho de la Unión o de los Estados miembros, c) consentimiento explícito), all stated in the sentence at l. 174–178, so the scope is now the article's: neither narrowed to a) and c) nor wider. Exception and safeguards verbatim. «artículo 22.2» and «artículo 9.1» sit in running text, so the parser reads only `(art. 22.4 RGPD)` (l. 183, art. 22). The paragraph's 22.1, 22.2 and 22.3 sentences were re-read against the article: 22.3 keeps «En los casos a que se refiere el apartado 2, letras a) y c)» as «En los casos del contrato y del consentimiento explícito» |
| 59 | m02-l04 | 197 | Row «Decisiones individuales automatizadas», arts. 22.1, 22.2, 22.3 y 22.4 RGPD | PASS | Same norm as #54. The cell's last sentence now reads «Las decisiones de los tres casos del artículo 22.2 no se basarán …», word for word the prose. The cell is the prose of l. 172–183; each apartado written out and each cited in prose (l. 174, 178, 181, 183). Title «Algunos derechos del interesado» keeps the selection marker (art. 18, 19 and 15.2 are not rows). Esquema check: no problem |
| 64 | m02-l04 | 353–355 | Prose: art. 65.5 párr. 2 LOPDGDD, «conforme al artículo 64.4» | PASS | Norm: «En el supuesto de que la Agencia Española de Protección de Datos actúe como consecuencia de la comunicación que le hubiera sido remitida por la autoridad de control de otro Estado miembro de la Unión Europea, conforme al artículo 64.4 de esta ley orgánica, el cómputo del plazo señalado en el párrafo anterior se iniciará una vez que se reciba en la Agencia toda la documentación necesaria para su tramitación.» Prose keeps «conforme al artículo 64.4 de la LOPDGDD», which restores art. 64.4's limit (a reclamación filed with that authority «cuando la Agencia Española de Protección de Datos tuviese la condición de autoridad de control principal»). «ese plazo» points to the three months of the sentence before, as «el plazo señalado en el párrafo anterior». No longer wider than the article. «artículo 64.4 de la LOPDGDD» is outside parentheses: the parser reads only `art. 65.4` (l. 349) and `art. 65.5` (l. 350, 353, 355), no 64.4 citation. See note 1 |
| 65 | m02-l04 | 363 | Row «La Agencia, sobre la admisión a trámite de la reclamación», art. 65.5 LOPDGDD | PASS | Same norm as #64. Third sentence: «Cuando la Agencia actúe por la comunicación de la autoridad de control de otro Estado miembro de la Unión Europea, conforme al artículo 64.4, el cómputo se inicia una vez que reciba toda la documentación necesaria para su tramitación». Condition restored, with the norm's own comma placement. Row citation `art. 65.5 LOPDGDD` is cited in prose; no 64.4 row or anchor needed. First two sentences unchanged and faithful to 65.5 párr. 1 (as #63 of `verify.md`). Esquema check: no problem. (`writer.md` gives l. 364; the row is at l. 363) |

Voice, all five: Peninsular Spanish, no filler, rhetorical question, triad, «no solo… sino», closer, stacked hedge or
blacklisted split opener. The added words are the norm's («Cuando la inadmisión traiga causa…», «conforme al artículo
64.4») or a plain pointer («Las decisiones de los tres casos del artículo 22.2»). No coined term.

## Notes outside the PASS/FAIL count (none blocks)

1. m02-l04 l. 353–355 and 363: art. 64.4 itself is not stated anywhere in the lesson, so the reader meets «conforme al
   artículo 64.4» as a bare cross-reference. That is the norm's own wording and keeps the scope exact; a gloss («la
   reclamación presentada ante esa autoridad cuando la Agencia sea autoridad de control principal») would be a separate
   prose gap, with its own `(art. 64.4 LOPDGDD)` citation.
2. m02-l04 l. 181: the fixed line is 147 columns, past the file's ~118-column wrap (the fix was not re-wrapped).
   Cosmetic; a re-wrap changes no citation.
3. m02-l04 l. 349–350 (outside the five items, unchanged this round): the prose says «La decisión sobre la admisión se
   notifica …»; art. 65.5 párr. 1 also covers «la que determine, en su caso, la remisión de la reclamación a la autoridad
   de control principal que se estime competente». The row (l. 363) says «admisión o inadmisión». Not wrong, only
   narrower; `verify.md` #63 passed it.
4. m02-l04 l. 357, esquema title «Plazos de respuesta a las solicitudes y reclamaciones» (unchanged this round) carries
   no «Algunos», though the LOPDGDD sets other plazos on reclamaciones (e.g. art. 64.1 párr. 2, six months to resolve).
   Candidate for the title rule in a later pass.
