# Live check, R3 close: six Microsoft pages (verifier 1)

Date: 2026-10-27 20:13. Method: `curl -sSL` with a Chrome user agent and `Accept-Language: es-ES`, es-es URL from `sources/otros/fuentes.yaml` (none of the six has `url_actual`); every fetch returned HTTP 200 with no redirect. Saved and live HTML were converted to text by the same stdlib `html.parser` script (script/style/svg/noscript/template dropped, block tags to newlines, whitespace collapsed), then diffed with `diff`. Saved-file sha256 equals the value in fuentes.yaml for all six.

| # | Saved file | Fetched | sha256 saved | sha256 live | Visible text |
|---|---|---|---|---|---|
| 1 | ms-word-indice.html | OK | a910f0c9497f37fba88ac98b2554bd846f7a68a1fadddfe00b21cc5ba2744168 | 683bf8706e65e44da41dca183a4237a3b9ba181d79aca9c36112389419b0aa02 | unchanged (226 lines, empty diff) |
| 2 | ms-excel-lista-desplegable.html | OK | c2fc3f63bd3fcec093de0fea34144b3159746127630d689b3b351a08b6cddc73 | e2c5d2461ae59e710efa3ccc2fe7b754105bd97923092ea465d3e2f18e2ec2ed | unchanged (323 lines, empty diff) |
| 3 | ms-win-update.html | OK | 2cad41ba356078a18ca2fbbf7dfdf572769ffa1bd7956e1687a51036a602b6dd | 4d798f810e955a4da4ff16d45436d3773556f4f5681516bf855644dd699b8de3 | unchanged (325 lines, empty diff) |
| 4 | ms-outlook-buscar.html | OK | d901250aa08e7f91d265707e4c08a50abfeebcdec9593e82073fc453b09ba4f4 | aadfba63f846f656197e7977a72705c00ad9df5e4345783182bb5de5b0c78b33 | unchanged (367 lines, empty diff) |
| 5 | ms-outlook-procedimientos.html | OK | bfec8685a1efdf19c1ef501a81226f01e18dc73ab9f4271051ee3d2b94984685 | 9c5127d87cd967390e8a0ab32c946452c199bcb6fbd6c5044e43733eefbad578 | unchanged (801 lines, empty diff) |
| 6 | ms-outlook-limpieza-buzon.html | OK | c42e2ff49e25fed723816195afcca631d46c7a62626144c003f54ba50e76d748 | 1faa24308b5b11b89b3d9c3819c7cf6631bc86ac4772fb2effe64a4f3aebcc3d | unchanged (213 lines, empty diff) |

Raw HTML hashes differ, as expected (scripts, ids); the visible text is identical on all six.

## Disputed sentences, as the live es-es page prints them today

1. Word index: «Si necesita un tercer nivel, siga el texto de subentrada con punto y coma.» The es-es page still says «punto y coma»; the en-us «colon» reading was not rechecked here (out of scope: es-es as saved).
2. Excel validation: «… escriba un título y un mensaje en los cuadros (hasta 225 caracteres).» (twice, Windows and Mac sections).
3. Windows Update: «Las actualizaciones de funciones se distribuyen una vez al año …» and «Las actualizaciones de funciones suelen ocurrir dos veces al año …» (both still on the page, for Windows 11 and Windows 10).
4. Outlook search: exact-phrase and search-key text unchanged, e.g. «Para buscar una cadena en concreto, debe usar comillas.»
5, 6. «Se aplica a: Outlook 2024 Outlook 2021» on both pages, unchanged.

## Changed sentences

None.

## Questions and lessons affected

None: no page changed, so no kept question's key, distractor or explanation and no lesson sentence rests on a changed sentence.

For reference, kept questions (not in drops.tsv) citing each page: ms-word-indice 7 (m06-l04-q158, q159, q161–q165); ms-excel-lista-desplegable 5 (m06-l05-q331, q333, q334, q336, q369); ms-win-update 5 (m06-l01-q339, q354–q356, q358); ms-outlook-buscar 18 (m06-l07-q124–q126, q128–q137, q140, q141, q147, q148, q174); ms-outlook-procedimientos 4 (m06-l07-q158–q161); ms-outlook-limpieza-buzon 3 (m06-l07-q162–q164). Lessons citing them: m06-l01, m06-l04, m06-l05, m06-l07.

Downloads: /tmp/claude-1000/-home-juanjo-PycharmProjects-curset/0c1e49ae-d2ba-46ff-9345-b19bf0f39e40/scratchpad/verifier-1-live/<name>/live.html.
