# Verify — `m03-l19` (round R2d, blind)

2026-11-14. Verifier: Opus, blind (no writer.md, no earlier verify). Input: `pending.md` (582 rows). Norms: LIVA (BOE-A-1992-28740, 2026-10-07), RIVA (BOE-A-1992-28925, 2026-02-28), RD 1619/2012 (BOE-A-2012-14696, 2026-03-31), read with pdftotext and compared word for word.

Out-of-row finding (no pending row holds it): the «Normativa» block lists, besides LIVA, RIVA and RD 1619/2012, only «LGT (Ley 58/2003): arts. 124–127, nombrados en el art. 115.Tres LIVA». The copied law text in the prose also names LGT arts. 26 y 27 (art. 89.Cinco LIVA), 41.5 (art. 87.Cinco.4 LIVA), 120.3 (art. 89.Cinco.a) LIVA) and its título V (art. 31.10 RIVA), and names other norms with no «Normativa» line: Ley 22/2003 Concursal (arts. 80.Tres, 99.Tres LIVA), Ley 49/2002 (art. 79.Cinco.d) LIVA), RDLeg 4/2004 TRLIS art. 16 (art. 79.Cinco LIVA), RDLeg 3/2011 TRLCSP art. 235 (art. 75.Uno.2.º bis LIVA), Reglamento de Ejecución (UE) 282/2011 arts. 41 bis y 61 ter and Directiva 2006/112/CE (art. 23 bis RIVA; art. 97.Uno.4.º LIVA), Reglamento (UE) 2015/848 (arts. 80.Cinco.2.ª LIVA, 24.2 RIVA), Ley 1/2005 and RD 1031/2007 (art. 84.Uno.2.º.d) LIVA), RD 1065/2007 RGAT arts. 9, 74, 144.4 y 146.1 (arts. 27.2, 30.3 RIVA), RDLeg 339/1990 anexo (art. 95.Tres.2.ª LIVA), Código de Comercio (art. 27.2.c) RIVA). Under the R2b convention («nombrado en el art. …») each needs a line.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `5308a7eb0d` | PASS | art. 75.Uno LIVA | — | — |
| `3474ce4c7a` | PASS | art. 75.Uno.1.º LIVA | — | — |
| `d0e885fe38` | PASS | art. 75.Uno.2.º LIVA | — | — |
| `7310873a2c` | PASS | art. 75.Uno.2.º LIVA | — | — |
| `292622c2b1` | PASS | art. 75.Uno.2.º LIVA | — | — |
| `37dc924be5` | FAIL | art. 75.Uno.2.º bis LIVA | text verbatim, but the 2.º bis rule is cited as «art. 75.Uno.2.º»; it is its own number «2.º bis» | Cuando se trate de ejecuciones de obra, con o sin aportación de materiales, cuyas destinatarias sean las Administraciones públicas, en el momento de su recepción, conforme a lo dispuesto en el artículo 235 del Texto Refundido de la Ley de Contratos del Sector Público, aprobado por el Real Decreto Legislativo 3/2011, de 14 de noviembre (art. 75.Uno.2.º bis LIVA). |
| `9090303daa` | PASS | art. 75.Uno.3.º LIVA | — | — |
| `6798b75a89` | PASS | art. 75.Uno.4.º LIVA | — | — |
| `03a60906d6` | PASS | art. 75.Uno.5.º LIVA | — | — |
| `f6510ea667` | PASS | art. 75.Uno LIVA | — | — |
| `dd71cee8e3` | PASS | art. 75.Uno.7.º LIVA | — | — |
| `0a92b50a27` | PASS | art. 75.Uno.7.º LIVA | — | — |
| `1607d1b336` | PASS | art. 75.Uno.7.º LIVA | — | — |
| `59a13e77d9` | PASS | art. 75.Uno.8.º LIVA | — | — |
| `0324b3d8ef` | PASS | art. 75.Uno.8.º LIVA | — | — |
| `05617c467a` | PASS | art. 75.Dos LIVA | — | — |
| `7bd3a48cf1` | PASS | art. 75.Dos LIVA | — | — |
| `339d23b91a` | PASS | art. 75.Tres LIVA | — | — |
| `fa12163d8b` | PASS | art. 23 bis RIVA | — | — |
| `f8a98c42d5` | PASS | art. 77.Dos LIVA | — | — |
| `7c46fc58c6` | PASS | art. 78.Dos LIVA | — | — |
| `b00503f187` | PASS | art. 78.Dos.1.º LIVA | — | — |
| `0a7ff6c2c8` | PASS | art. 78.Dos.1.º LIVA | — | — |
| `90bff3fa55` | PASS | art. 78.Dos.1.º LIVA | — | — |
| `fba7312c9c` | PASS | art. 78.Dos LIVA | — | — |
| `f0566ab72c` | PASS | art. 78.Dos.3.º LIVA | — | — |
| `d355492e7a` | PASS | art. 78.Dos.3.º LIVA | — | — |
| `3f880b19d8` | PASS | art. 78.Dos.3.º LIVA | — | — |
| `806901b3db` | PASS | art. 78.Dos.4.º LIVA | — | — |
| `38f33673c3` | PASS | art. 78.Dos.4.º LIVA | — | — |
| `76e1b8789c` | PASS | art. 78.Dos.5.º LIVA | — | — |
| `b5e2168b53` | PASS | art. 78.Dos.6.º LIVA | — | — |
| `14062436af` | PASS | art. 78.Dos.7.º LIVA | — | — |
| `e18248f903` | PASS | art. 78.Tres LIVA | — | — |
| `9bdc156a66` | PASS | art. 78.Tres.1.º LIVA | — | — |
| `721f97530b` | PASS | art. 78.Tres.2.º LIVA | — | — |
| `fb6c61c957` | PASS | art. 78.Tres.3.º LIVA | — | — |
| `3c299018e0` | PASS | art. 79.Cinco LIVA | — | — |
| `4317e47625` | PASS | art. 79.Cinco LIVA | — | — |
| `c93b15bebe` | FAIL | art. 79.Cinco LIVA | the list this lead-in opens shows ten items (a–e, then a–c, then a–b) at one level: the requisitos a)–c) and the «valor de mercado» a)–b) of art. 79.Cinco are separate lists, not supuestos de vinculación; the article's list is a)–e) only | Se considerará que existe vinculación en los siguientes supuestos (art. 79.Cinco LIVA): [list a)–e) only; close the list after e)] |
| `e9c6ba06c3` | PASS | art. 79.Cinco LIVA | — | — |
| `6d5cd3c0c0` | PASS | art. 79.Cinco LIVA | — | — |
| `1c06bd2dab` | PASS | art. 79.Cinco LIVA | — | — |
| `a7886a0d2c` | PASS | art. 79.Cinco LIVA | — | — |
| `5dcea3c284` | PASS | art. 79.Cinco LIVA | — | — |
| `468481e4e7` | FAIL | art. 79.Cinco LIVA | verbatim, but placed inside item e) of the vinculación list; in the article it is a separate paragraph that opens its own list a)–c) | Esta regla de valoración únicamente será aplicable cuando se cumplan los siguientes requisitos (art. 79.Cinco LIVA): [own paragraph, followed by its own list a)–c)] |
| `8b8a650d30` | PASS | art. 79.Cinco LIVA | — | — |
| `77d0132ad2` | PASS | art. 79.Cinco LIVA | — | — |
| `a2f7586465` | PASS | art. 79.Cinco LIVA | — | — |
| `c931c8d114` | FAIL | art. 79.Cinco LIVA | verbatim, but placed inside item c) of the requisitos list; in the article it is a separate paragraph after that list | A los efectos de esta Ley, se entenderá por valor normal de mercado aquel que, para adquirir los bienes o servicios en cuestión en ese mismo momento, un destinatario, en la misma fase de comercialización en la que se efectúe la entrega de bienes o prestación de servicios, debería pagar en el territorio de aplicación del Impuesto en condiciones de libre competencia a un proveedor independiente (art. 79.Cinco LIVA). [own paragraph] |
| `234f4ffc74` | FAIL | art. 79.Cinco LIVA | verbatim lead-in placed inside item c) of the requisitos list, so its a)–b) read as more items of the same list | Cuando no exista entrega de bienes o prestación de servicios comparable, se entenderá por valor de mercado (art. 79.Cinco LIVA): [own paragraph, followed by its own list a)–b)] |
| `e6a244f6d6` | PASS | art. 79.Cinco LIVA | — | — |
| `823efdae89` | PASS | art. 79.Cinco LIVA | — | — |
| `767fee08a4` | FAIL | art. 79.Cinco LIVA | verbatim, but placed inside item b) of the «valor de mercado» list; in the article it is a separate paragraph referring to the two preceding paragraphs | A efectos de los dos párrafos anteriores, será de aplicación, en cuanto proceda, lo dispuesto en el artículo 16 del texto refundido de la Ley del Impuesto sobre Sociedades, aprobado por el Real Decreto Legislativo 4/2004, de 5 de marzo (art. 79.Cinco LIVA). [own paragraph after the list] |
| `70a627d458` | PASS | art. 79.Seis LIVA | — | — |
| `4130667267` | PASS | art. 79.Siete LIVA | — | — |
| `be252aa83f` | PASS | art. 79.Ocho LIVA | — | — |
| `1f75b5d845` | PASS | art. 79.Nueve LIVA | — | — |
| `6154df3a3d` | PASS | art. 79.Diez LIVA | — | — |
| `4c7f26fae2` | PASS | art. 79.Doce LIVA | — | — |
| `48a06836cc` | PASS | art. 24 bis RIVA | — | — |
| `64c672be76` | PASS | art. 80.Uno LIVA | — | — |
| `2b827b4513` | PASS | art. 80.Uno.1.º LIVA | — | — |
| `2fc9a26cb8` | PASS | art. 80.Uno.2.º LIVA | — | — |
| `a2fff5a716` | PASS | art. 80.Dos LIVA | — | — |
| `bfc1b29421` | PASS | art. 80.Tres LIVA | — | — |
| `f0a38f0bcf` | PASS | art. 80.Tres LIVA | — | — |
| `7a31a558b9` | PASS | art. 80.Tres LIVA | — | — |
| `144c239830` | PASS | art. 80.Cuatro LIVA | — | — |
| `2919ab6e06` | PASS | art. 80.Cuatro LIVA | — | — |
| `c8c7916d6d` | FAIL | art. 80.Cuatro LIVA | list nesting does not follow the article: A) is a bullet at the same level as its own conditions 1.ª–4.ª, and the letters B) and C) of the same apartado Cuatro are nested under condition 4.ª | A) Un crédito se considerará total o parcialmente incobrable cuando reúna las siguientes condiciones: [conditions 1.ª–4.ª nested under A); B) and C) at the level of A)] |
| `58f02bc71e` | PASS | art. 80.Cuatro.1.ª LIVA | — | — |
| `0b45025a21` | PASS | art. 80.Cuatro.1.ª LIVA | — | — |
| `0d5543d8c5` | PASS | art. 80.Cuatro.1.ª LIVA | — | — |
| `4d9928a0da` | PASS | art. 80.Cuatro.1.ª LIVA | — | — |
| `da641c1ff7` | PASS | art. 80.Cuatro.1.ª LIVA | — | — |
| `5eec18a6d1` | PASS | art. 80.Cuatro.1.ª LIVA | — | — |
| `872271b327` | PASS | art. 80.Cuatro.2.ª LIVA | — | — |
| `bb281570dd` | PASS | art. 80.Cuatro.3.ª LIVA | — | — |
| `9828036992` | PASS | art. 80.Cuatro.4.ª LIVA | — | — |
| `2a8dd03e3e` | FAIL | art. 80.Cuatro.B) LIVA | the sentence of condition 4.ª is right, but the item «B) La modificación deberá realizarse…» that follows it is nested under condition 4.ª and carries no citation of its own; B) is a letter of apartado Cuatro, not part of condition 4.ª | B) La modificación deberá realizarse en el plazo de los seis meses siguientes a la finalización del periodo de seis meses o un año a que se refiere la condición 1.ª anterior y comunicarse a la Agencia Estatal de Administración Tributaria en el plazo que se fije reglamentariamente. [item at the level of A), not under 4.ª] |
| `e473b8a10d` | FAIL | art. 80.Cuatro.B) and C) LIVA | verbatim, but governed by «art. 80.Cuatro.4.ª»: the sentence closes letter B) of apartado Cuatro (and the row opens C)), not condition 4.ª | En el caso de operaciones a las que sea de aplicación el régimen especial del criterio de caja, el plazo de seis meses para realizar la modificación se computará a partir de la fecha límite del 31 de diciembre a que se refiere el artículo 163 terdecies de esta ley (art. 80.Cuatro.B) LIVA). |
| `bd5ef22818` | PASS | art. 80.Cuatro.4.ª LIVA | — | — |
| `cf04eeb843` | FAIL | art. 80.Cuatro.C) LIVA | verbatim, but letter C) is nested under condition 4.ª and governed by «art. 80.Cuatro.4.ª»; it is letter C) of apartado Cuatro | No obstante lo dispuesto en el párrafo anterior, cuando el sujeto pasivo desista de la reclamación judicial al deudor o llegue a un acuerdo de cobro con el mismo con posterioridad al requerimiento notarial efectuado, como consecuencia de éste o por cualquier otra causa, deberá modificar nuevamente la base imponible al alza mediante la expedición, en el plazo de un mes a contar desde el desistimiento o desde el acuerdo de cobro, respectivamente, de una factura rectificativa en la que se repercuta la cuota procedente (art. 80.Cuatro.C) LIVA). |
| `751a7240a4` | PASS | art. 80.Cinco LIVA | — | — |
| `054eeeb924` | PASS | art. 80.Cinco.1.ª LIVA | — | — |
| `7b6b9f53d3` | PASS | art. 80.Cinco.1.ª LIVA | — | — |
| `b1fdb1af60` | PASS | art. 80.Cinco.2.ª LIVA | — | — |
| `b84c077c08` | PASS | art. 80.Cinco.2.ª LIVA | — | — |
| `ee5868594c` | PASS | art. 80.Cinco.3.ª LIVA | — | — |
| `2ed9cea839` | PASS | art. 80.Cinco.4.ª LIVA | — | — |
| `df06e2ccde` | PASS | art. 80.Cinco.5.ª LIVA | — | — |
| `d67f2e5125` | PASS | art. 80.Cinco.5.ª LIVA | — | — |
| `7f7a5136c5` | PASS | art. 80.Cinco.5.ª LIVA | — | — |
| `cc726877cb` | PASS | art. 80.Seis LIVA | — | — |
| `37c13b2548` | PASS | art. 80.Siete LIVA | — | — |
| `e7d486823a` | PASS | art. 24.1 RIVA | — | — |
| `5ce485e752` | PASS | art. 24.1 RIVA | — | — |
| `40baf7d98a` | PASS | art. 24.1 RIVA | — | — |
| `9c5cdd74ec` | PASS | art. 24.1 RIVA | — | — |
| `5fb8d7ee64` | PASS | art. 24.2 RIVA | — | — |
| `5375e078c4` | PASS | art. 24.2 RIVA | — | — |
| `1af32f9580` | FAIL | art. 24.2.a).1.º RIVA | art. 24.2 has two numbered series (under a) and under b)); «art. 24.2.1.º» does not say which; this is a).1.º. Also 1.º–2.º are bullets at the level of a) instead of nested under it | 1.º Las operaciones cuya base imponible se pretenda rectificar deberán haber sido facturadas y anotadas en el libro registro de facturas expedidas por el acreedor en tiempo y forma (art. 24.2.a).1.º RIVA). |
| `8b0a0254f5` | PASS | art. 24.2.2.º RIVA | — | — |
| `e66454e3c8` | FAIL | art. 24.2.a).2.º and 24.2.b) RIVA | text verbatim; citation «24.2.2.º» is ambiguous (a).2.º), and the letter «b) En caso de que el destinatario…» is nested under a).2.º as if it were a fourth document after c´); b) is a letter of art. 24.2 at the level of a) | A esta comunicación deberán acompañarse los siguientes documentos, que se remitirán a través del registro electrónico de la Agencia Estatal de Administración Tributaria (art. 24.2.a).2.º RIVA): [a´)–c´)]; then, at the level of a): b) En caso de que el destinatario de las operaciones tenga la condición de empresario o profesional (art. 24.2.b) RIVA): |
| `f92811d73b` | PASS | art. 24.2.1.º RIVA | — | — |
| `38c54d6981` | FAIL | art. 24.2.b).1.º RIVA | verbatim; cited «art. 24.2.1.º», the same citation the lesson gives to a).1.º; this is b).1.º | El incumplimiento de esta obligación no impedirá la modificación de la base imponible por parte del acreedor, siempre que se cumplan los requisitos señalados en el párrafo a) (art. 24.2.b).1.º RIVA). |
| `4efa5ab05d` | FAIL | art. 24.2.b).2.º RIVA | «declaración- liquidación» (stray space from the PDF line break; the article says «declaración-liquidación»); citation «24.2.2.º» is the one given to a).2.º; this is b).2.º | 2.º Además de la comunicación a que se refiere el número anterior, en la declaración-liquidación correspondiente al período en que se hayan recibido las facturas rectificativas de las operaciones, el citado destinatario deberá hacer constar el importe total de las cuotas rectificadas como minoración de las cuotas deducidas (art. 24.2.b).2.º RIVA). |
| `e05ac3147e` | FAIL | art. 24.2.b).3.º RIVA | verbatim; citation «24.2.3.º» omits the letter b) | 3.º Tratándose del supuesto previsto en el artículo 80.Tres de la Ley del Impuesto, las cuotas rectificadas deberán hacerse constar (art. 24.2.b).3.º RIVA): |
| `aa4bc6a762` | PASS | art. 24.2.4.º RIVA | — | — |
| `d0fd6b7e2c` | FAIL | art. 24.2.b).4.º, 24.2.c) and d) RIVA | verbatim; citation «24.2.4.º» omits the letter b), and letters c) and d) of art. 24.2 are nested under b).4.º with that citation; they are letters at the level of a) and b) | En el caso de que el destinatario de las operaciones se encuentre en concurso, las obligaciones previstas en los números anteriores recaerán en el mismo o en la administración concursal, en defecto de aquél, si se encontrara en régimen de intervención de facultades y, en todo caso, cuando se hubieren suspendido las facultades de administración y disposición (art. 24.2.b).4.º RIVA). [then, at the level of a): c) … d) … (art. 24.2.c) y d) RIVA)] |
| `bae739dc56` | PASS | art. 24.3 RIVA | — | — |
| `d82f07aa77` | PASS | art. 24.3 RIVA | — | — |
| `7f64c3743b` | FAIL | art. 24.3 RIVA | «declaración- liquidación»: stray space from the PDF line break; the article says «declaración-liquidación» | La variación en el importe de la cuota devengada se reflejará en la declaración-liquidación correspondiente al período en que se haya obtenido la devolución, salvo que ya hubiera sido totalmente deducida por el propio sujeto pasivo. |
| `b178a62762` | PASS | art. 24.3 RIVA | — | — |
| `30f481421b` | PASS | art. 81.Uno LIVA | — | — |
| `f39b216bcf` | PASS | art. 81.Uno LIVA | — | — |
| `ab9765d901` | PASS | art. 81.Dos LIVA | — | — |
| `96e47f1cab` | PASS | art. 81.Dos LIVA | — | — |
| `8d3df8b68d` | PASS | art. 81.Tres LIVA | — | — |
| `45421ac952` | PASS | art. 82.Uno LIVA | — | — |
| `139832a5ee` | PASS | art. 82.Uno LIVA | — | — |
| `7d465b0868` | PASS | art. 82.Uno LIVA | — | — |
| `f79d83ba76` | PASS | art. 82.Dos LIVA | — | — |
| `36a7e38be0` | PASS | art. 83.Uno LIVA | — | — |
| `0967634787` | PASS | art. 83.Uno LIVA | — | — |
| `3b10088c3e` | PASS | art. 83.Uno LIVA | — | — |
| `ed2a090e20` | PASS | art. 83.Uno LIVA | — | — |
| `f9d148bffb` | PASS | art. 83.Uno LIVA | — | — |
| `164bcf3884` | PASS | art. 83.Uno LIVA | — | — |
| `4b80050a12` | PASS | art. 83.Dos LIVA | — | — |
| `6f8f367df8` | PASS | art. 83.Dos.1.ª LIVA | — | — |
| `b35fdfbe8d` | PASS | art. 83.Dos.1.ª LIVA | — | — |
| `944d200763` | PASS | art. 83.Dos.2.ª LIVA | — | — |
| `9bc3096a96` | PASS | art. 83.Dos.3.ª LIVA | — | — |
| `50a9749240` | PASS | art. 83.Dos.3.ª LIVA | — | — |
| `796b5ebc9b` | PASS | art. 83.Dos.4.ª LIVA | — | — |
| `fb3cc77a75` | PASS | art. 83.Dos.5.ª LIVA | — | — |
| `c32f3d900e` | PASS | art. 83.Dos.6.ª LIVA | — | — |
| `be5c90c96f` | PASS | art. 83.Tres LIVA | — | — |
| `66b14698e5` | PASS | art. 83.Cuatro LIVA | — | — |
| `8cf572826d` | PASS | art. 84.Uno LIVA | — | — |
| `54fcedf729` | PASS | art. 84.Uno.1.º LIVA | — | — |
| `d607d5cf5d` | PASS | art. 84.Uno.2.º LIVA | — | — |
| `7e88abbfca` | PASS | art. 84.Uno.2.º LIVA | — | — |
| `7fd902cdb1` | PASS | art. 84.Uno.2.º LIVA | — | — |
| `5ad43039da` | FAIL | art. 84.Uno.2.º.c) LIVA | verbatim, but placed inside the last guion of c) (semielaborados); it refers to all the preceding párrafos of c), so inside one guion its scope reads narrower than the article's | En todo caso, se considerarán comprendidas en los párrafos anteriores las entregas de los materiales definidos en el anexo de esta ley (art. 84.Uno.2.º LIVA). [own paragraph at the level of the c) text, after the guiones] |
| `0ef6f31663` | PASS | art. 84.Uno.2.º LIVA | — | — |
| `9ac25b0552` | PASS | art. 84.Uno.2.º LIVA | — | — |
| `a637267b77` | FAIL | art. 84.Uno.2.º.g) LIVA | lead-in placed inside the third guion of g), and its a´)–b´) shown at the guion level, so g) appears to list five products; a´) and b´) are conditions on the last two guiones, not products | Lo previsto en estos dos últimos guiones solo se aplicará cuando el destinatario sea (art. 84.Uno.2.º LIVA): [own paragraph after the three guiones, with a´) and b´) nested under it] |
| `5601bd5cbe` | PASS | art. 84.Uno.2.º LIVA | — | — |
| `b5f71ea9f9` | FAIL | art. 84.Uno.2.º.g) LIVA | verbatim, but placed inside b´); it refers to «las dos letras anteriores» (a´ and b´), so it belongs after the a´)–b´) list | La acreditación de la condición del empresario o profesional a que se refieren las dos letras anteriores deberá realizarse con carácter previo o simultáneo a la adquisición, en las condiciones que se determinen reglamentariamente (art. 84.Uno.2.º LIVA). [own paragraph after a´)–b´)] |
| `d6efb3c9b6` | FAIL | art. 84.Uno.2.º LIVA | verbatim, but placed inside b´) of g); it governs the entregas of g) where the destinatario is sujeto pasivo under the whole número 2.º | Las entregas de dichos bienes, en los casos en que sean sujetos pasivos del Impuesto sus destinatarios conforme a lo establecido en este número 2.°, deberán documentarse en una factura mediante serie especial (art. 84.Uno.2.º LIVA). [own paragraph after a´)–b´)] |
| `07daada5a5` | FAIL | art. 84.Uno.3.º and 4.º LIVA | the 3.º lead-in and its a)–b) are verbatim, but número 4.º («4.° Sin perjuicio de lo dispuesto en los números anteriores…») is glued inside item b) of 3.º and governed by «art. 84.Uno.3.º»; 4.º is its own número of apartado Uno | 4.º Sin perjuicio de lo dispuesto en los números anteriores, los empresarios o profesionales, así como las personas jurídicas que no actúen como empresarios o profesionales, que sean destinatarios de entregas de gas y electricidad o las entregas de calor o de frío a través de las redes de calefacción o de refrigeración que se entiendan realizadas en el territorio de aplicación del impuesto conforme a lo dispuesto en el artículo 68.Seis de esta Ley, siempre que la entrega la efectúe un empresario o profesional no establecido en el citado territorio y le hayan comunicado el número de identificación que a efectos del impuesto sobre el valor añadido tengan asignado por la Administración española (art. 84.Uno.4.º LIVA). [own item at the level of 1.º–3.º] |
| `a85cc1ccab` | PASS | art. 84.Dos LIVA | — | — |
| `082dd6fb10` | PASS | art. 84.Dos LIVA | — | — |
| `dc231af52e` | PASS | art. 84.Tres LIVA | — | — |
| `45f020a211` | PASS | art. 24 ter RIVA | — | — |
| `1613214a42` | PASS | art. 85 LIVA | — | — |
| `ef307044c4` | PASS | art. 86.Uno LIVA | — | — |
| `96ff1aa5e0` | PASS | art. 86.Dos LIVA | — | — |
| `c2cf2593da` | PASS | art. 86.Dos.1.º LIVA | — | — |
| `177e88f83a` | PASS | art. 86.Dos.2.º LIVA | — | — |
| `dae1c2f132` | PASS | art. 86.Dos.3.º LIVA | — | — |
| `2687805150` | PASS | art. 86.Dos.4.º LIVA | — | — |
| `590a4fa1d8` | PASS | art. 86.Tres LIVA | — | — |
| `c35c641a1b` | PASS | art. 87.Uno LIVA | — | — |
| `90888f797a` | PASS | art. 87.Uno LIVA | — | — |
| `a9e92151cb` | PASS | art. 87.Dos LIVA | — | — |
| `aa39c6af9b` | PASS | art. 87.Dos.1.º LIVA | — | — |
| `959ea6f2ed` | PASS | art. 87.Dos.2.º LIVA | — | — |
| `b0c93a00bc` | PASS | art. 87.Dos.3.º LIVA | — | — |
| `d3e426a8f7` | PASS | art. 87.Tres LIVA | — | — |
| `43dcbfa445` | PASS | art. 87.Cuatro LIVA | — | — |
| `bcf888a366` | PASS | art. 87.Cinco LIVA | — | — |
| `38a0a4a2c8` | PASS | art. 87.Cinco LIVA | — | — |
| `9b6ffd9dcf` | PASS | art. 87.Cinco LIVA | — | — |
| `31d75093b9` | PASS | art. 87.Cinco LIVA | — | — |
| `4c7d79e1c7` | PASS | art. 87.Cinco LIVA | — | — |
| `76cbf8e49d` | FAIL | art. 87.Cinco.2 LIVA | verbatim, but placed inside item b) of the «precio notoriamente anómalo» list; it is a separate paragraph that applies to both a) and b) | Para la calificación del precio de la operación como notoriamente anómalo, la Administración tributaria estudiará la documentación de que disponga, así como la aportada por los destinatarios, y valorará, cuando sea posible, otras operaciones realizadas en el mismo sector económico que guarden un alto grado de similitud con la analizada, con objeto de cuantificar el valor normal de mercado de los bienes existente en el momento de realización de la operación (art. 87.Cinco.2 LIVA). [own paragraph after the list] |
| `91bd555a50` | FAIL | art. 87.Cinco.2 LIVA | the sentence ends with a stray «3.» (the number of the next apartado, glued on) and sits inside item b) of the list | No se considerará como precio notoriamente anómalo aquel que se justifique por la existencia de factores económicos distintos a la aplicación del Impuesto (art. 87.Cinco.2 LIVA). |
| `d352327ebd` | FAIL | art. 87.Cinco.3 LIVA | número 3 of art. 87.Cinco is glued inside item b) of the 87.Cinco.2 list, without its own citation, and ends with a stray «4.» | Para la exigencia de esta responsabilidad, la Administración tributaria deberá acreditar la existencia de un Impuesto repercutido o que hubiera debido repercutirse que no ha sido objeto de declaración e ingreso (art. 87.Cinco.3 LIVA). [own paragraph] |
| `5541f07120` | FAIL | art. 87.Cinco.4 LIVA | número 4 of art. 87.Cinco glued inside item b) of the 87.Cinco.2 list, without its own citation | Una vez que la Administración tributaria haya constatado la concurrencia de los requisitos establecidos en los apartados anteriores declarará la responsabilidad conforme a lo dispuesto en el artículo 41.5 de la Ley 58/2003, General Tributaria (art. 87.Cinco.4 LIVA). [own paragraph] |
| `77a53e81b0` | PASS | — | — | — |
| `e34a888a51` | PASS | art. 87.Uno LIVA | — | — |
| `ae090e3923` | PASS | art. 87.Cinco.1 LIVA | — | — |
| `cd9b6d93d3` | PASS | art. 88.Uno LIVA | — | — |
| `5b22e3539e` | PASS | art. 88.Uno LIVA | — | — |
| `e4a356c01e` | PASS | art. 88.Dos LIVA | — | — |
| `52198a1a73` | PASS | art. 88.Dos LIVA | — | — |
| `7ec45b29db` | PASS | art. 88.Dos LIVA | — | — |
| `3fbc9b2778` | PASS | art. 88.Tres LIVA | — | — |
| `c03aff2707` | PASS | art. 88.Cuatro LIVA | — | — |
| `f247ba44a6` | PASS | art. 88.Cinco LIVA | — | — |
| `82ce253c69` | PASS | art. 88.Seis LIVA | — | — |
| `23f0270df0` | PASS | art. 25.1 RIVA | — | — |
| `3dbe602c4d` | FAIL | art. 25.2 RIVA | a bare «(Derogado)» paragraph with no citation: the reader cannot tell what is repealed (it is art. 25.2 RIVA, which «Normativa» does not list) | drop |
| `555e0bb9f3` | PASS | art. 89.Uno LIVA | — | — |
| `1685223fb6` | PASS | art. 89.Uno LIVA | — | — |
| `41189fae0d` | PASS | art. 89.Dos LIVA | — | — |
| `85ab2fc43a` | PASS | art. 89.Tres LIVA | — | — |
| `fd43e23e04` | PASS | art. 89.Tres.1.º LIVA | — | — |
| `52d71543a9` | PASS | art. 89.Tres.2.º LIVA | — | — |
| `e8e4103b74` | PASS | art. 89.Cuatro LIVA | — | — |
| `8a58ac5c80` | PASS | art. 89.Cinco LIVA | — | — |
| `846f44d0ca` | PASS | art. 89.Cinco LIVA | — | — |
| `b76ed8c749` | PASS | art. 89.Cinco LIVA | — | — |
| `8045796078` | PASS | art. 89.Cinco LIVA | — | — |
| `707ba4c4e3` | PASS | art. 89.Cinco LIVA | — | — |
| `3dcb449f0e` | PASS | art. 89.Cinco LIVA | — | — |
| `a871433614` | PASS | art. 89.Cinco LIVA | — | — |
| `9904049c85` | PASS | art. 89.Uno LIVA | — | — |
| `09714cb90b` | PASS | art. 15.1 RD 1619/2012 | — | — |
| `3ec9f05902` | PASS | art. 15.2 RD 1619/2012 | — | — |
| `3771dd133a` | PASS | art. 15.2 RD 1619/2012 | — | — |
| `631988763b` | PASS | art. 15.2 RD 1619/2012 | — | — |
| `f58114e1d6` | PASS | art. 15.3 RD 1619/2012 | — | — |
| `7b995660c4` | PASS | art. 15.4 RD 1619/2012 | — | — |
| `67cc8341e2` | PASS | art. 15.4 RD 1619/2012 | — | — |
| `6f7acc2384` | PASS | art. 15.4 RD 1619/2012 | — | — |
| `0f88f9d226` | PASS | art. 15.4 RD 1619/2012 | — | — |
| `73bcf842dc` | PASS | art. 15.5 RD 1619/2012 | — | — |
| `fc17f2c877` | PASS | art. 15.5 RD 1619/2012 | — | — |
| `4fc6414109` | PASS | art. 15.5 RD 1619/2012 | — | — |
| `63141e1ef2` | PASS | art. 15.5 RD 1619/2012 | — | — |
| `8be8bec9bd` | PASS | art. 15.6 RD 1619/2012 | — | — |
| `dae5524b68` | PASS | art. 15.6 RD 1619/2012 | — | — |
| `2b6c0831ff` | PASS | art. 92.Uno LIVA | — | — |
| `bc53a20d4d` | PASS | art. 92.Uno.1.º LIVA | — | — |
| `63c07b5052` | FAIL | art. 92.Uno.2.º and 3.º LIVA | número 3.º is glued to item 2.º («2.º Las importaciones de bienes. 3°.»), so 92.Uno shows three items instead of four | 2.º Las importaciones de bienes (art. 92.Uno.2.º LIVA). |
| `c8ece549b9` | FAIL | art. 92.Uno.3.º LIVA | verbatim, but it is número 3.º of art. 92.Uno and is cited «art. 92.Uno.2.º», inside item 2.º | 3.º Las entregas de bienes y prestaciones de servicios comprendidas en los artículos 9.1.° c) y d); 84.uno.2.° y 4.º, y 140 quinque, todos ellos de la presente Ley (art. 92.Uno.3.º LIVA). [own item] |
| `4d49597102` | PASS | art. 92.Uno.4.º LIVA | — | — |
| `1c2ba337fc` | PASS | art. 92.Dos LIVA | — | — |
| `72e5a2ed15` | PASS | art. 93.Uno LIVA | — | — |
| `40c47c749f` | PASS | art. 93.Uno LIVA | — | — |
| `919a500a5d` | PASS | art. 93.Dos LIVA | — | — |
| `ea36454a40` | PASS | art. 93.Tres LIVA | — | — |
| `b371f88166` | PASS | art. 93.Cuatro LIVA | — | — |
| `9cba68e0d9` | PASS | art. 93.Cinco LIVA | — | — |
| `e930594ed0` | PASS | art. 93.Cinco LIVA | — | — |
| `0ed34301f3` | PASS | art. 93.Cinco LIVA | — | — |
| `aec14dc568` | PASS | art. 93.Cinco LIVA | — | — |
| `b7d9a8e30b` | PASS | art. 93.Cinco LIVA | — | — |
| `d18e078acd` | PASS | art. 93.Cinco LIVA | — | — |
| `5d0c94cd98` | PASS | art. 93.Cinco LIVA | — | — |
| `cc3e5f9171` | PASS | art. 94.Uno LIVA | — | — |
| `49a868c7ac` | PASS | art. 94.Uno.1.º LIVA | — | — |
| `9a9fa2324f` | PASS | art. 94.Uno.2.º LIVA | — | — |
| `eece08e252` | PASS | art. 94.Uno.3.º LIVA | — | — |
| `81fe3e3467` | PASS | art. 94.Uno.3.º LIVA | — | — |
| `54bacf499b` | PASS | art. 94.Dos LIVA | — | — |
| `8c2d0e69be` | PASS | art. 94.Tres LIVA | — | — |
| `74d3d9f0b0` | PASS | art. 95.Uno LIVA | — | — |
| `d5b9e4b087` | PASS | art. 95.Dos LIVA | — | — |
| `e67bc63da5` | PASS | art. 95.Dos.1.º LIVA | — | — |
| `c920faba30` | PASS | art. 95.Dos.2.º LIVA | — | — |
| `b65c46d39f` | PASS | art. 95.Dos.3.º LIVA | — | — |
| `0850b4bdff` | PASS | art. 95.Dos.4.º LIVA | — | — |
| `bd2563e25c` | PASS | art. 95.Dos.5.º LIVA | — | — |
| `6720fed181` | PASS | art. 95.Tres LIVA | — | — |
| `0a7caa8597` | PASS | art. 95.Tres.1.ª LIVA | — | — |
| `7f9d1b6ff8` | PASS | art. 95.Tres.2.ª LIVA | — | — |
| `28c18ee3b8` | PASS | art. 95.Tres.2.ª LIVA | — | — |
| `6bddea05b3` | PASS | art. 95.Tres.2.ª LIVA | — | — |
| `293d85f76b` | PASS | art. 95.Tres.3.ª LIVA | — | — |
| `303b2dd0e9` | PASS | art. 95.Tres.3.ª LIVA | — | — |
| `93afc97554` | PASS | art. 95.Tres.4.ª LIVA | — | — |
| `fbca1f1d6f` | PASS | art. 95.Tres.4.ª LIVA | — | — |
| `13a4d66a93` | PASS | art. 95.Tres.5.ª LIVA | — | — |
| `7a832880ac` | PASS | art. 95.Cuatro LIVA | — | — |
| `a1c5f65dec` | PASS | art. 95.Cuatro.1.º LIVA | — | — |
| `b36d081ac3` | PASS | art. 95.Cuatro.2.º LIVA | — | — |
| `77045b2331` | PASS | art. 95.Cuatro.3.º LIVA | — | — |
| `9a6acd9106` | PASS | art. 95.Cuatro.4.º LIVA | — | — |
| `2e1b2daeb5` | PASS | art. 96.Uno LIVA | — | — |
| `90e9945b15` | PASS | art. 96.Uno.1.º LIVA | — | — |
| `c37b1c4572` | PASS | art. 96.Uno LIVA | — | — |
| `b28f253337` | PASS | art. 96.Uno.3.º LIVA | — | — |
| `80e9981299` | PASS | art. 96.Uno.4.º LIVA | — | — |
| `fa2b10011b` | PASS | art. 96.Uno.5.º LIVA | — | — |
| `91dafa16dc` | PASS | art. 96.Uno.5.º LIVA | — | — |
| `18f263cd58` | PASS | art. 96.Uno.6.º LIVA | — | — |
| `b6a8089bc1` | PASS | art. 96.Dos LIVA | — | — |
| `b96eb7a6cf` | PASS | art. 96.Dos.1.º LIVA | — | — |
| `957ec53086` | PASS | art. 96.Dos.2.º LIVA | — | — |
| `a110b90eec` | PASS | art. 96.Dos.3.º LIVA | — | — |
| `da5bce25e0` | PASS | art. 96.Tres LIVA | — | — |
| `24dbd079d6` | PASS | art. 97.Uno LIVA | — | — |
| `4e6cec3b36` | PASS | art. 97.Uno LIVA | — | — |
| `ee1b7c70f5` | PASS | art. 97.Uno.1.º LIVA | — | — |
| `595561199f` | PASS | art. 97.Uno.2.º LIVA | — | — |
| `7b70a03e40` | PASS | art. 97.Uno.3.º LIVA | — | — |
| `b82359fb54` | PASS | art. 97.Uno.4.º LIVA | — | — |
| `bd98648fe7` | PASS | art. 97.Uno.4.º LIVA | — | — |
| `2cc9cdf37f` | PASS | art. 97.Uno.5.º LIVA | — | — |
| `9c12ac5b02` | PASS | art. 97.Dos LIVA | — | — |
| `a608fe923c` | PASS | art. 97.Dos LIVA | — | — |
| `c587a1359e` | PASS | art. 97.Tres LIVA | — | — |
| `57166a4d5e` | PASS | art. 97.Cuatro LIVA | — | — |
| `2f655adbd4` | PASS | art. 98.Uno LIVA | — | — |
| `39f71d78b5` | PASS | art. 98.Tres LIVA | — | — |
| `53498dd8ed` | PASS | art. 98.Cuatro LIVA | — | — |
| `1f71613775` | PASS | art. 98.Cinco LIVA | — | — |
| `0d7c860000` | PASS | art. 99.Uno LIVA | — | — |
| `3219b6fb2b` | PASS | art. 99.Dos LIVA | — | — |
| `529bc6d564` | PASS | art. 99.Dos LIVA | — | — |
| `cd1153bf94` | PASS | art. 99.Tres LIVA | — | — |
| `7eb510d760` | PASS | art. 99.Tres LIVA | — | — |
| `193d1f03d2` | FAIL | art. 99.Tres LIVA | «declaración- liquidación»: stray space from the PDF line break; the article says «declaración-liquidación» | Cuando no se hubieran incluido las cuotas soportadas deducibles a que se refiere el párrafo anterior en dichas declaraciones-liquidaciones, y siempre que no hubiera transcurrido el plazo de cuatro años, contados a partir del nacimiento del derecho a la deducción de tales cuotas, el concursado o, en los casos previstos por el artículo 86.3 de la Ley Concursal, la administración concursal, podrá deducirlas mediante la rectificación de la declaración-liquidación relativa al periodo en que fueron soportadas (art. 99.Tres LIVA). |
| `f409cbff55` | PASS | art. 99.Tres LIVA | — | — |
| `dcb180f8c9` | PASS | art. 99.Tres LIVA | — | — |
| `6809ed7622` | PASS | art. 99.Tres LIVA | — | — |
| `f2e13096c6` | PASS | art. 99.Cuatro LIVA | — | — |
| `869e888318` | PASS | art. 99.Cuatro LIVA | — | — |
| `4a32808860` | PASS | art. 99.Cuatro LIVA | — | — |
| `41f0fd952d` | PASS | art. 99.Cinco LIVA | — | — |
| `53ffcdc353` | PASS | art. 99.Cinco LIVA | — | — |
| `ab992b89ab` | PASS | art. 99.Cinco LIVA | — | — |
| `3c84ae081a` | PASS | art. 100 LIVA | — | — |
| `d2a68df849` | PASS | art. 100 LIVA | — | — |
| `daf1560a76` | PASS | art. 101.Uno LIVA | — | — |
| `3dd13a940e` | PASS | art. 101.Uno LIVA | — | — |
| `56d67ac4f8` | PASS | art. 101.Uno LIVA | — | — |
| `7af8724079` | PASS | art. 101.Uno LIVA | — | — |
| `8cc94bf683` | PASS | art. 101.Uno LIVA | — | — |
| `36a979b1e9` | PASS | art. 101.Uno LIVA | — | — |
| `782cb34de7` | PASS | art. 101.Dos LIVA | — | — |
| `a9883711ae` | PASS | art. 101.Dos LIVA | — | — |
| `2bdb03ec4d` | PASS | art. 101.Dos LIVA | — | — |
| `01b410b7ef` | PASS | art. 101.Dos LIVA | — | — |
| `4e2c3fc827` | PASS | — | — | — |
| `c34aef5a96` | PASS | art. 102.Uno LIVA | — | — |
| `a3e5d5c9e3` | PASS | art. 102.Dos LIVA | — | — |
| `b060008f86` | PASS | art. 103.Uno LIVA | — | — |
| `3fb8a969ce` | PASS | art. 103.Uno LIVA | — | — |
| `fb0b992d4e` | PASS | art. 103.Dos LIVA | — | — |
| `127542c0ef` | PASS | art. 103.Dos.1.º LIVA | — | — |
| `bd74868ca8` | PASS | art. 103.Dos.2.º LIVA | — | — |
| `26dabe8b45` | PASS | art. 104.Uno LIVA | — | — |
| `a9ebff401f` | PASS | art. 104.Uno LIVA | — | — |
| `0d557c2af4` | PASS | art. 104.Dos LIVA | — | — |
| `8b2f88a149` | PASS | art. 104.Dos.1.º LIVA | — | — |
| `f274851e25` | PASS | art. 104.Dos.2.º LIVA | — | — |
| `16dd365c40` | PASS | art. 104.Dos.2.º LIVA | — | — |
| `639dd47e38` | PASS | art. 104.Dos.2.º LIVA | — | — |
| `7386bdd903` | PASS | art. 104.Dos.2.º LIVA | — | — |
| `ab49104640` | PASS | art. 104.Tres LIVA | — | — |
| `6dec6b44b5` | PASS | art. 104.Tres.1.º LIVA | — | — |
| `3bb0fd9913` | PASS | art. 104.Tres.2.º LIVA | — | — |
| `17f982ef27` | PASS | art. 104.Tres.3.º LIVA | — | — |
| `2c58b3bfc7` | PASS | art. 104.Tres.4.º LIVA | — | — |
| `5e05ca9a27` | PASS | art. 104.Tres.4.º LIVA | — | — |
| `69513636b2` | PASS | art. 104.Tres.4.º LIVA | — | — |
| `21688ce8e0` | PASS | art. 104.Tres.5.º LIVA | — | — |
| `5092ac6151` | PASS | art. 104.Tres.6.º LIVA | — | — |
| `fd39b86f8f` | PASS | art. 104.Cuatro LIVA | — | — |
| `e0f0c5c637` | PASS | art. 104.Cuatro LIVA | — | — |
| `ffe457926a` | PASS | art. 104.Cuatro LIVA | — | — |
| `fcf2b659c2` | PASS | art. 104.Cinco LIVA | — | — |
| `5629934563` | PASS | art. 104.Cinco LIVA | — | — |
| `c664ab95f1` | PASS | art. 104.Seis LIVA | — | — |
| `3cc798748f` | PASS | art. 104.Seis LIVA | — | — |
| `85c7a63367` | PASS | art. 105.Uno LIVA | — | — |
| `e3bfe8ffe1` | PASS | art. 105.Dos LIVA | — | — |
| `d08e1b6cfd` | PASS | art. 105.Tres LIVA | — | — |
| `bcc43af114` | PASS | art. 105.Tres LIVA | — | — |
| `6ebeba3517` | PASS | art. 105.Cuatro LIVA | — | — |
| `fc64b1a197` | PASS | art. 105.Cinco LIVA | — | — |
| `0945a52ce7` | PASS | art. 105.Seis LIVA | — | — |
| `1a0a9f46f3` | PASS | art. 28.1 RIVA | — | — |
| `e3bd5da308` | PASS | art. 28.1.1.º RIVA | — | — |
| `7e486d8e41` | PASS | art. 28.1.1.º RIVA | — | — |
| `e76152486f` | FAIL | art. 28.1.1.º RIVA | verbatim, but placed inside item b) (inicio de actividades); in the article it is a separate paragraph of número 1.º that governs the option however it was exercised (a or b) | La opción por la aplicación de la regla de prorrata especial surtirá efectos en tanto no sea revocada por el sujeto pasivo, si bien, la opción por su aplicación tendrá una validez mínima de tres años naturales, incluido el año natural a que se refiere la opción ejercitada (art. 28.1.1.º RIVA). [own paragraph after a)–b)] |
| `ad759ff9e2` | FAIL | art. 28.1.1.º RIVA | verbatim, but placed inside item b); it is a paragraph of número 1.º after the a)–b) list | La revocación podrá efectuarse, una vez transcurrido el período mínimo mencionado, en la última declaración-liquidación correspondiente a cada año natural, procediéndose en tal caso, a la regularización de las deducciones practicadas durante el mismo (art. 28.1.1.º RIVA). [own paragraph after a)–b)] |
| `3f819067e5` | PASS | art. 28.1.2.º RIVA | — | — |
| `615ad8adf9` | PASS | art. 28.1.2.º RIVA | — | — |
| `d24216a4b8` | FAIL | art. 28.1.2.º RIVA | lead-in placed inside plazo b), and its own list of dates a)–b) is collapsed into one item shown as a third «a)» of the plazos list (with «b)» run inline); the article has two lists: plazos a)–b), then dates a)–b) under this paragraph | El régimen de deducción que se autorice únicamente podrá ser aplicable respecto de cuotas que sean soportadas o satisfechas a partir del momento en que se produzca el comienzo de la realización habitual de las entregas de bienes o prestaciones de servicios correspondientes a actividades empresariales o profesionales, y que lo sean a partir de las fechas que se indican a continuación, tanto en el supuesto de autorización del régimen notificada por la Administración al sujeto pasivo dentro del plazo de un mes a que se refiere el apartado dos de este artículo, como en el supuesto de autorizaciones que deban entenderse concedidas por haber transcurrido el referido plazo de un mes sin que se hubiese producido la notificación de la resolución de la Administración (art. 28.1.2.º RIVA): [own paragraph; dates a) and b) as two nested items; then «El régimen de deducción común autorizado surtirá efectos…» as a paragraph] |
| `528da42de7` | FAIL | art. 28.1.2.º RIVA | verbatim, but run inside the date item a) of the collapsed list; it is a paragraph of número 2.º on renouncing the regime | Dicha renuncia podrá efectuarse durante el mes de diciembre del año anterior a aquél a partir del cual se desea que la misma tenga efectos (art. 28.1.2.º RIVA). [own paragraph] |
| `3ed2346d4a` | FAIL | art. 28.1.2.º RIVA | verbatim, but run inside the date item a); it is a paragraph of número 2.º on the authorised regime | Por excepción a lo señalado en el párrafo anterior, el régimen de deducción común autorizado no surtirá efectos en cada uno de los años en los que el montante total de las cuotas deducibles por aplicación del mismo exceda en un 20 por 100 o más del que resultaría de aplicar con independencia el régimen de deducciones respecto de cada sector diferenciado (art. 28.1.2.º RIVA). [own paragraph] |
| `0e98144aaa` | PASS | art. 28.1.3.º RIVA | — | — |
| `f53ee11936` | PASS | art. 28.1.3.º RIVA | — | — |
| `de28252755` | FAIL | art. 28.1.3.º RIVA | verbatim, but this lead-in and its a´)–b´) are nested inside plazo b), so they read as applying only to the b) case; in the article it is a paragraph of número 3.º after plazos a)–b), for every authorised percentage | El porcentaje provisional autorizado surtirá efectos respecto de las cuotas soportadas a partir de las siguientes fechas (art. 28.1.3.º RIVA): [own paragraph after plazos a)–b), with a´)–b´) nested under it] |
| `687ee90128` | PASS | art. 28.1.4.º RIVA | — | — |
| `8ba9c01e88` | PASS | art. 28.1.4.º RIVA | — | — |
| `4854a1affb` | PASS | art. 28.1.4.º RIVA | — | — |
| `7213c2921c` | PASS | art. 28.1.4.º RIVA | — | — |
| `5d20137686` | PASS | art. 28.1.5.º RIVA | — | — |
| `e5c6a2b10b` | PASS | art. 28.1.5.º RIVA | — | — |
| `534f5c0056` | PASS | art. 28.1.5.º RIVA | — | — |
| `9b7d41d32c` | PASS | art. 28.1.5.º RIVA | — | — |
| `cc15e8294d` | PASS | art. 28.2 RIVA | — | — |
| `a5c52bfa3b` | PASS | art. 28.2 RIVA | — | — |
| `519418cfbb` | PASS | art. 107.Uno LIVA | — | — |
| `ab042a0611` | PASS | art. 107.Uno LIVA | — | — |
| `99db49e809` | PASS | art. 107.Uno LIVA | — | — |
| `b89e8b6b38` | PASS | art. 107.Dos LIVA | — | — |
| `abd08373a1` | PASS | art. 107.Tres LIVA | — | — |
| `e98f6e5d3c` | PASS | art. 107.Tres LIVA | — | — |
| `f2e3da7260` | PASS | art. 107.Cuatro LIVA | — | — |
| `ebc67b073d` | PASS | art. 107.Cinco LIVA | — | — |
| `d0da4dc75a` | PASS | art. 107.Cinco LIVA | — | — |
| `b1f78322c2` | PASS | art. 107.Seis LIVA | — | — |
| `d3a9b7deaf` | FAIL | art. 107.Siete LIVA | «declaración- liquidación»: stray space from the PDF line break; the article says «declaración-liquidación» | Los ingresos o, en su caso, deducciones complementarias resultantes de la regularización de deducciones por bienes de inversión deberán efectuarse en la declaración-liquidación correspondiente al último período de liquidación del año natural a que se refieran, salvo en el supuesto mencionado en el apartado cuatro, en el que deberá realizarse en el mismo año en que se soporten las cuotas repercutidas (art. 107.Siete LIVA). |
| `8c9a624580` | PASS | art. 108.Uno LIVA | — | — |
| `d175b637be` | PASS | art. 108.Dos LIVA | — | — |
| `fe1b93c9cd` | PASS | art. 108.Dos.1.º LIVA | — | — |
| `cde21e4c43` | PASS | art. 108.Dos.2.º LIVA | — | — |
| `a92652791e` | PASS | art. 108.Dos.3.º LIVA | — | — |
| `a7548b0d24` | PASS | art. 108.Dos.4.º LIVA | — | — |
| `66b012a184` | PASS | art. 108.Dos.5.º LIVA | — | — |
| `3dba6d1d92` | PASS | art. 109 LIVA | — | — |
| `c7beffbf7f` | PASS | art. 109 LIVA | — | — |
| `4ebf9f7835` | PASS | art. 109 LIVA | — | — |
| `3d6f4797d2` | PASS | art. 109 LIVA | — | — |
| `749bda9a7e` | PASS | art. 110.Uno LIVA | — | — |
| `901ee94fdc` | PASS | art. 110.Uno LIVA | — | — |
| `d9cd90a7ec` | PASS | art. 110.Uno.1.º LIVA | — | — |
| `e1e396d970` | PASS | art. 110.Uno.1.º LIVA | — | — |
| `9988e484b0` | PASS | art. 110.Uno.2.º LIVA | — | — |
| `494e0693cc` | PASS | art. 110.Uno.2.º LIVA | — | — |
| `8001e77007` | PASS | art. 110.Uno.2.º LIVA | — | — |
| `313d2f3882` | PASS | art. 110.Uno.2.º LIVA | — | — |
| `da07b56b5e` | PASS | art. 110.Dos LIVA | — | — |
| `f21f09ae32` | PASS | art. 110.Tres LIVA | — | — |
| `fb0ca6cf80` | PASS | art. 110.Cuatro LIVA | — | — |
| `3affe3d365` | PASS | art. 103.Dos.2.º LIVA | — | — |
| `6da50c3f83` | PASS | art. 107.Uno LIVA | — | — |
| `07e5e4e5ce` | PASS | art. 111.Uno LIVA | — | — |
| `41b10cdc94` | PASS | art. 111.Uno LIVA | — | — |
| `15809bfb6f` | PASS | art. 111.Dos LIVA | — | — |
| `19e070d559` | PASS | art. 111.Dos LIVA | — | — |
| `bbf8e9e93c` | PASS | art. 111.Tres LIVA | — | — |
| `eb22235b1c` | PASS | art. 111.Cuatro LIVA | — | — |
| `ffcf6f14bc` | PASS | art. 111.Cinco LIVA | — | — |
| `be3ba07039` | PASS | art. 111.Cinco LIVA | — | — |
| `b6b402704b` | PASS | art. 111.Seis LIVA | — | — |
| `02c28e5476` | PASS | art. 112.Uno LIVA | — | — |
| `5134f3a16c` | PASS | art. 112.Dos LIVA | — | — |
| `af1834c273` | PASS | art. 112.Tres LIVA | — | — |
| `c1bbb484b5` | PASS | art. 112.Tres.1.º LIVA | — | — |
| `99fad29c2a` | PASS | art. 112.Tres.2.º LIVA | — | — |
| `3d676770a9` | PASS | art. 112.Tres.3.º LIVA | — | — |
| `560e1d2811` | PASS | art. 113.Uno LIVA | — | — |
| `eaeb8a282f` | PASS | art. 113.Dos LIVA | — | — |
| `b7fc342afc` | PASS | art. 113.Tres LIVA | — | — |
| `1c3b9b1158` | PASS | art. 114.Uno LIVA | — | — |
| `ebf2b9a5c8` | PASS | art. 114.Uno LIVA | — | — |
| `bf9fcde2f7` | PASS | art. 114.Dos LIVA | — | — |
| `e7524dfc17` | PASS | art. 114.Dos.1.º LIVA | — | — |
| `9e14d4fece` | PASS | art. 114.Dos.1.º LIVA | — | — |
| `edaae95c4c` | PASS | art. 114.Dos.2.º LIVA | — | — |
| `f20745622b` | PASS | art. 114.Dos.2.º LIVA | — | — |
| `60c3149211` | PASS | art. 114.Dos.2.º LIVA | — | — |
| `eaab6d4855` | FAIL | art. 114.Dos.2.º LIVA | «declaración- liquidación»: stray space from the PDF line break; the article says «declaración-liquidación» | No obstante, cuando la rectificación tenga su origen en un error fundado de derecho o en las restantes causas del artículo 80 de esta Ley deberá efectuarse en la declaración-liquidación correspondiente al periodo impositivo en que el sujeto pasivo reciba el documento justificativo del derecho a deducir en el que se rectifiquen las cuotas inicialmente soportadas (art. 114.Dos.2.º LIVA). |
| `ba0a53fa40` | PASS | art. 27.1 RIVA | — | — |
| `fa40e9a8e4` | PASS | art. 27.2 RIVA | — | — |
| `324beee554` | PASS | art. 27.2 RIVA | — | — |
| `b7a6c36120` | PASS | art. 27.2 RIVA | — | — |
| `bd5ba5b2d3` | PASS | art. 27.2 RIVA | — | — |
| `348768fd1d` | PASS | art. 27.2 RIVA | — | — |
| `1b94320bbe` | PASS | art. 27.2 RIVA | — | — |
| `befb3aaf94` | PASS | art. 27.2 RIVA | — | — |
| `b2023c1236` | PASS | art. 27.2 RIVA | — | — |
| `d5e17303c6` | PASS | art. 27.3 RIVA | — | — |
| `126a8a0778` | PASS | art. 27.4 RIVA | — | — |
| `d4511645b5` | PASS | art. 115.Tres LIVA | — | — |
| `0de7927107` | PASS | art. 115.Tres LIVA | — | — |
| `595da2bf73` | PASS | art. 116.Dos LIVA | — | — |
| `6a71b7378f` | PASS | art. 117.Dos LIVA | — | — |
| `5911f89c74` | PASS | art. 117.Tres LIVA | — | — |
| `c021be6fde` | PASS | art. 117 bis LIVA | — | — |
| `a3343510ed` | PASS | art. 117 bis LIVA | — | — |
| `8c9b309511` | PASS | art. 119.Dos LIVA | — | — |
| `23e6f1dcdd` | FAIL | art. 119.Dos.1.º, 2.º and 3.º LIVA | text verbatim, but condition 2.º is glued inside item 1.º and cited «art. 119.Dos.1.º», and condition 3.º is glued inside letter b) of 2.º without a citation; the list shows four conditions (1.º, 4.º, 5.º, 6.º) where the article has six | 1.º Estar establecidos en la Comunidad o en las Islas Canarias, Ceuta o Melilla (art. 119.Dos.1.º LIVA). / 2.º No haber realizado en el territorio de aplicación del Impuesto entregas de bienes o prestaciones de servicios sujetas al mismo distintas de las que se relacionan a continuación (art. 119.Dos.2.º LIVA): [a)–b) nested] / 3.º No ser destinatarios de entregas de bienes ni de prestaciones de servicios respecto de las cuales tengan dichos solicitantes la condición de sujetos pasivos en virtud de lo dispuesto en los números 2.° y 4.° del apartado Uno del artículo 84 de esta Ley (art. 119.Dos.3.º LIVA). [three separate items] |
| `e03011aa1a` | PASS | art. 119.Dos.4.º LIVA | — | — |
| `297ea6865a` | PASS | art. 119.Dos.5.º LIVA | — | — |
| `1761d4af0d` | PASS | art. 119.Dos.5.º LIVA | — | — |
| `fdcec0e2e8` | PASS | art. 119.Dos.5.º LIVA | — | — |
| `68c09869df` | PASS | art. 119.Dos.5.º LIVA | — | — |
| `0af20c0eb7` | PASS | art. 119.Dos.6.º LIVA | — | — |
| `1d56aa9439` | PASS | art. 119.Tres LIVA | — | — |
| `3d957df46f` | PASS | art. 119.Cuatro LIVA | — | — |
| `ca7be0ea3d` | PASS | art. 119.Cinco LIVA | — | — |
| `a291747aef` | PASS | art. 119.Cinco LIVA | — | — |
| `48a4c68ebd` | PASS | art. 119.Seis LIVA | — | — |
| `2532d56bd6` | PASS | art. 119.Seis LIVA | — | — |
| `e2571a015c` | PASS | art. 119.Seis LIVA | — | — |
| `13d3e1d706` | PASS | art. 119.Siete LIVA | — | — |
| `2589d48b50` | PASS | art. 119.Siete LIVA | — | — |
| `593243e77a` | PASS | art. 119.Siete LIVA | — | — |
| `e64bf63f54` | PASS | art. 119.Siete LIVA | — | — |
| `8c326634ee` | PASS | art. 119 bis.Uno LIVA | — | — |
| `0b5eadb757` | PASS | art. 119 bis.Uno.1.º LIVA | — | — |
| `d81cf0d596` | PASS | art. 119 bis.Uno.1.º LIVA | — | — |
| `98510398ab` | PASS | art. 119 bis.Uno.2.º LIVA | — | — |
| `810f3c8483` | PASS | art. 119 bis.Uno.2.º LIVA | — | — |
| `d586cfcc3e` | PASS | art. 119 bis.Uno.3.º LIVA | — | — |
| `fb64f3fc3f` | PASS | art. 119 bis.Dos LIVA | — | — |
| `2a1b93e6b0` | PASS | art. 29 RIVA | — | — |
| `f03ed9c45e` | PASS | art. 29 RIVA | — | — |
| `50ed493596` | PASS | art. 30.1 RIVA | — | — |
| `b0914b7507` | PASS | art. 30.1 RIVA | — | — |
| `c4d718c3d2` | PASS | art. 30.2 RIVA | — | — |
| `248ee223f1` | PASS | art. 30.3 RIVA | — | — |
| `d4801f81c1` | PASS | art. 30.3 RIVA | — | — |
| `9ee90a3a5b` | PASS | art. 30.3 RIVA | — | — |
| `9e332949b0` | PASS | art. 30.3 RIVA | — | — |
| `978288e132` | PASS | art. 30.3 RIVA | — | — |
| `e7b0070850` | PASS | art. 30.3 RIVA | — | — |
| `83670c24bc` | PASS | art. 30.3 RIVA | — | — |
| `dc229a5831` | PASS | art. 30.3 RIVA | — | — |
| `e62471bf94` | PASS | art. 30.3 RIVA | — | — |
| `33a05f8397` | PASS | art. 30.4 RIVA | — | — |
| `cc1e770278` | PASS | art. 30.4 RIVA | — | — |
| `91b42a8734` | PASS | art. 30.4 RIVA | — | — |
| `01bc7b51d6` | PASS | art. 30.4 RIVA | — | — |
| `43be35ec6c` | PASS | art. 30.4 RIVA | — | — |
| `ad8f8c9f8b` | PASS | art. 30.4 RIVA | — | — |
| `d959dad905` | PASS | art. 30.4 RIVA | — | — |
| `c6a44d359d` | PASS | art. 30.5 RIVA | — | — |
| `ac2e1038e5` | PASS | art. 30.6 RIVA | — | — |
| `8ddecbd517` | PASS | art. 30.6 RIVA | — | — |
| `de08ec07f5` | PASS | art. 30.6 RIVA | — | — |
| `0474fa81a2` | PASS | art. 30.7 RIVA | — | — |
| `cd69561312` | PASS | art. 30.8 RIVA | — | — |
| `48745ee871` | PASS | art. 30.8 RIVA | — | — |
| `eb48dacdb0` | PASS | art. 30.8 RIVA | — | — |
| `ef827cdd03` | PASS | art. 30.8 RIVA | — | — |
| `57c0f14b3f` | PASS | art. 30.8 RIVA | — | — |
| `eee4a081e2` | PASS | art. 30.9 RIVA | — | — |
| `349758dff9` | PASS | art. 30.10 RIVA | — | — |
| `131d7ebe99` | PASS | art. 30.11 RIVA | — | — |
| `846ec1bf6a` | PASS | art. 30.11 RIVA | — | — |
| `8d475f9966` | PASS | art. 30.12 RIVA | — | — |
| `9efcbf7817` | PASS | art. 31.1 RIVA | — | — |
| `34ffab0349` | PASS | art. 31.1 RIVA | — | — |
| `17d36cd8df` | PASS | art. 31.1 RIVA | — | — |
| `65d3753ff5` | PASS | art. 31.1 RIVA | — | — |
| `043b43138f` | PASS | art. 31.1 RIVA | — | — |
| `9b8f3812d6` | PASS | art. 31.1 RIVA | — | — |
| `7386c638ca` | PASS | art. 31.1 RIVA | — | — |
| `b0ff62f303` | PASS | art. 31.1 RIVA | — | — |
| `76a99521be` | PASS | art. 31.1 RIVA | — | — |
| `341ba7743c` | PASS | art. 31.1.1.º RIVA | — | — |
| `c6d5117df0` | PASS | art. 31.1.2.º RIVA | — | — |
| `5dd96eae0a` | PASS | art. 31.1.3.º RIVA | — | — |
| `36168e9411` | PASS | art. 31.1.4.º RIVA | — | — |
| `20d5d1a8ec` | PASS | art. 31.1.4.º RIVA | — | — |
| `d04b30874a` | PASS | art. 31.1.5.º RIVA | — | — |
| `727ecc80e6` | PASS | art. 31.1.6.º RIVA | — | — |
| `c63c63b67b` | PASS | art. 31.1.6.º RIVA | — | — |
| `cb58f06537` | PASS | art. 31.1.6.º RIVA | — | — |
| `19e687ec7e` | PASS | art. 31.1.7.º RIVA | — | — |
| `240b6981a4` | PASS | art. 31.1.7.º RIVA | — | — |
| `3d7e4a40bd` | PASS | art. 31.1.8.º RIVA | — | — |
| `8ceff0f71e` | PASS | art. 31.2 RIVA | — | — |
| `a0328a81f2` | PASS | art. 31.3 RIVA | — | — |
| `b7b8451664` | PASS | art. 31.3 RIVA | — | — |
| `180480cf92` | PASS | art. 31.4 RIVA | — | — |
| `cdf98fff6a` | PASS | art. 31.5 RIVA | — | — |
| `1f1beeeea4` | PASS | art. 31.5 RIVA | — | — |
| `b06e95bdc6` | PASS | art. 31.6 RIVA | — | — |
| `fcc2f4d69e` | PASS | art. 31.6 RIVA | — | — |
| `c7e0f5969c` | PASS | art. 31.7 RIVA | — | — |
| `092dc67723` | PASS | art. 31.7 RIVA | — | — |
| `7a82b0fb7f` | PASS | art. 31.7 RIVA | — | — |
| `960a781ba9` | PASS | art. 31.7 RIVA | — | — |
| `c35d6a83e0` | PASS | art. 31.7 RIVA | — | — |
| `f4971fdcae` | PASS | art. 31.8 RIVA | — | — |
| `3c4f49b63c` | PASS | art. 31.8 RIVA | — | — |
| `9f99b3b49b` | PASS | art. 31.8 RIVA | — | — |
| `e91c7aeebc` | PASS | art. 31.8 RIVA | — | — |
| `4432903af6` | PASS | art. 31.9 RIVA | — | — |
| `64b13efebc` | PASS | art. 31.10 RIVA | — | — |
| `4951e8df5b` | PASS | art. 31.11 RIVA | — | — |
| `9a07e51342` | PASS | art. 32 RIVA | — | — |
| `65e7eb64c2` | PASS | art. 32 RIVA | — | — |
| `7a48098209` | PASS | art. 32.1 RIVA | — | — |
| `4d629e5812` | PASS | art. 32.2 RIVA | — | — |
| `ec4fdbb8a1` | FAIL | Normativa (LIVA) | the prose cites art. 119 LIVA (119.Uno at line 840, 119.Dos–Siete at lines 857–886), which the line does not list (it lists only 119 bis) | LIVA (Ley 37/1992): arts. 9.1, 20.Uno, 75.Uno–Tres, 76, 77.Uno–Dos, 78.Uno–Cuatro, 79.Uno–Doce, 80.Uno–Siete, 81.Uno–Tres, 82.Uno–Dos, 83.Uno–Cuatro, 84.Uno–Tres, 85, 86.Uno–Tres, 87.Uno–Cinco, 88.Uno–Seis, 89.Uno–Cinco, 92.Uno–Dos, 93.Uno–Cinco, 94.Uno–Tres, 95.Uno–Cuatro, 96.Uno–Tres, 97.Uno–Cuatro, 98.Uno, 98.Tres–Cinco, 99.Uno–Cinco, 100, 101.Uno–Dos, 102.Uno–Dos, 103.Uno–Dos, 104.Uno–Seis, 105.Uno–Seis, 106.Uno–Dos, 107.Uno–Siete, 108.Uno–Dos, 109, 110.Uno–Cuatro, 111.Uno–Seis, 112.Uno–Tres, 113.Uno–Tres, 114.Uno–Dos, 115.Uno–Tres, 116.Uno–Dos, 117.Uno–Tres, 117 bis, 118, 119.Uno–Siete y 119 bis.Uno–Dos. [if 84.Uno.4.º gets its own citation, «84.Uno–Tres» stays right: 4.º is inside apartado Uno] |
| `ef3c114293` | FAIL | Normativa (RIVA) | the prose cites art. 24 ter RIVA (line 258), which the line does not list | RIVA (RD 1624/1992): arts. 23 bis, 24.1–24.3, 24 bis, 24 ter, 25.1, 27.1–27.4, 28.1–28.2, 29, 30.1–30.12, 31.1–31.11 y 32.1–32.2. |
| `d8af7aaec6` | PASS | RD 1619/2012 (Reglamento de facturación) | — | — |

PASS 541 · FAIL 41
