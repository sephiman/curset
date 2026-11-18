# Build — III.2 (`m03-l02`), R2d, 2026-11-17

Base HEAD plus whole pool sentences, byte-identical (`tools/build_check.py`). The lesson was assembled in scratch (pool order, every pool list that follows a lead-in ending in «:» turned into an esquema `| Elemento | Contenido | Cita |` whose Cita cell is the lead-in's citation; multi-sentence items split into «x)» and «x) (cont.)» rows) and written once its esquemas were complete.

## Size
- Words (`wc -w`, esquema rows excluded): HEAD 4,070 → built 12,630. Ratio 3.10 × HEAD; 1.94 × the 1.6 target (target 6,512). Over target on purpose: every article of the range keeps its rule/conditions/exceptions sentences and every enumeration is complete.
- Esquema-row words (table lines): HEAD 75 → built 22,396 (37 `tabla` esquemas with 494 rows from items, plus the two `arbol`).

## Sentences added by category (build_check: 249 byte-identical + 494 esquema rows)
- (a) R2b removals: none (map: no section removed).
- (b) Confirmed review items: Consejo Superior and Consejos Territoriales (arts. 65–66 Ley 22/2009: 16 sentences, 37 rows); Comisión de Seguridad y Control (Orden 1994 primero.6 and Res. 26-01-1998: 8 sentences); Servicios centrales with their Subdirecciones (Orden 1994 décimo–undécimo quater, duodécimo, decimocuarto: 52 sentences, 31 rows); Comité Permanente opening clause (primero.4); Comisión/Consejo wording.
- (c) Article sentences: the rest — art. 103 Ley 31/1990 Dos.2–6, Cuatro, Cinco, Seis, Siete, Ocho, Nueve, Diez, Once.1/Once.5, Tres.2 last párrafo, Uno.3 párr. 4–5 (about 45 sentences, Cinco as esquema); art. 5.2–3 LGT and DA 17.ª LRJSP; arts. 4–9 Orden PRE/3581/2007 (327 rows); Res. territorial segundo, cuarto.3–6, quinto.1 a)–o), sexto, noveno, décimo–decimosexto (about 40 sentences, 80 rows); Orden 1994 decimotercero.2, decimoquinto; area organs of Gestión Tributaria, Aduanas, Informática, Recaudación, Inspección, DCGC (Res. 2021/2023/1992).
- (d) «No confundir»: 3 blocks (Comité Permanente / Comité de Coordinación; Consejo Superior / Comisión de Seguridad y Control; Delegados Especiales / Director General), 6 sentences.
- (e) Pool versions replacing HEAD: the opening norm list (split in three paragraphs and a list with Resolución 26-01-1998, Ley 22/2009 and the area resolutions), art. 103.Dos.2 and Dos.5 sentences (completed), art. 6.1 Orden PRE esquema in place of «entre otras funciones» (l. 96; l) is its row), Comité Permanente sentence (primero.4, with the opening clause), Delegados Especiales quinto.1.a)/c) (now rows of the quinto.1 esquema), the central `arbol` (extended with Servicios, DCGC, Intervención, Comités, Comisión). HEAD's «Órganos rectores» esquema removed (repeated one paragraph; the map asks for it).

## Enumerations as esquemas (37 tabla)
Arts. 4.1–4.2, 5.1–5.2, 6.1–6.2, 7.1–7.2, 8.1–8.2, 9 Orden PRE/3581/2007; art. 103.Cinco, Tres.2, Tres.3 Ley 31/1990; art. 1.1 Orden PRE; Subdirecciones of Gestión Tributaria, Inspección, Recaudación, Aduanas (Orden 1994 segundo–quinto); Servicios centrales (primero.2); Servicio Jurídico competencias (décimo.1); Auditoría Interna funciones and órganos (undécimo.2–3); DCGC tercero.2 a)–k); art. 65.3 and 66.2 Ley 22/2009; Res. territorial primero, cuarto.3, quinto.1, sexto.1, noveno.1, duodécimo.1, decimocuarto.1, decimoquinto.2, decimosexto.1; Aduanas primero.2; Recaudación primero.
Two lists stay as bullets, not esquemas: the funciones a)–f) and competencias a)–b) of the Servicio de Planificación y Relaciones Institucionales (Orden 1994 undécimo quater.2–3). The pool cites them as «según el apartado undécimo quater, número N, de la Orden…», which the citation parser does not read, so no row citation can be one the prose also cites (the course would not validate). Their sentences are in the pool form, complete.

## build_check line
`m03-l02: HEAD 78 · added byte-identical 249 · esquema rows from items 494 · not in pool 0`

## «not in pool» (0)
None. The header `| Elemento | Contenido | Cita |` is held by the pool of other lessons. The Normativa section is the pool's (every line is a pool sentence; it names exactly what the built lesson cites, since no pool sentence was dropped). Nothing outside HEAD and the pool is in the lesson, so there are no new Normativa lines of my own.

## Pool sentences left out and why
- None dropped from the pool. Sentences left out of the HEAD text: the «Órganos rectores» esquema (3 rows + header; repeats the paragraph before it), the HEAD `arbol` (replaced by the pool's extended one), l. 96 and the two Delegados Especiales sentences (replaced, see (e)).

## Pool gaps (no pool sentence; no prose written)
- Art. 103.Cuatro.7 Ley 31/1990 (régimen de personal, párrafo 7).
- Orden 1994 disposición adicional primera (colaboración del Servicio de Vigilancia Aduanera con Inspección y Recaudación).

## Sentences that do not stand on their own where they now sit
- «Todo ello sin perjuicio de la delegación de facultades…» (art. 103.Tres.2): «Todo ello» refers to the esquema of facultades before it.
- «El porcentaje será fijado en cada año en la Ley anual de Presupuestos» (art. 103.Cinco): refers to row b) of the financiación esquema.
- «Dependen directamente de la Dirección Adjunta de Vigilancia Aduanera las Subdirecciones Generales de las letras g) y h)»: refers to the letters of the esquema before it.
- «Las funciones de la Unidad…», «Los funcionarios de la Unidad…» (art. 103.Nueve): «la Unidad» is named in the bullet before.
- «Se integran también en él…», «Depende del Presidente…», «Desarrolla en particular…», «Está integrado por…», «Con rango de dirección adjunta, está integrado…», «Está integrada por…», «Ejerce, dentro de su ámbito…», «Puede ejercerlas también…», «Su Presidente es el Presidente…», «Su funcionamiento puede ser…», «Cuenta con una Secretaría Técnica…», «Podrán incorporarse como miembros…»: the subject is the organ of the sentence or heading just before.
- Rows `x) (cont.)`: second sentence of a multi-sentence pool item, kept under its own row with the item's citation.

## Checks
`build_check` (above); `cites.py m03-l02`: 792 citations, 0 unresolved; `split_paragraphs.py`: 7 paragraphs split; `index_sources.py --course aeat-agentes-hacienda`: see the final message.
