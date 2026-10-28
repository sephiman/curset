# Excerpt verification — report, part 4 (items 127–176, pass 2, bloque VI)

Blind opus verifier, `sample-4.jsonl`: 50 at random (seed 20261029) from bloque VI. Saved by the coordinator from the
verifier's returned text. `excerpt_full` is null on all 50.

Counts: **yes 46, full-only 0, no 4** (128, 145, 148, 152). Flags: 145, 160, 169; minor: 162.

| n | key | verdict | note |
|---|---|---|---|
| 127 | m06-l05-ex-9/m06-l05-q350 | yes | "No puede cambiar la ubicación de la pestaña Archivo." |
| 128 | m06-l04-ex-10/m06-l04-q398 | no | Right section, wrong rows: the last two rows (Texto oculto, Guiones opcionales); the key is the first row, "Caracteres de tabulación … como flechas". |
| 129 | m06-l03-ex-1/m06-l03-q007 | yes | Ctrl + rueda del ratón row |
| 130 | m06-l06-ex-9/m06-l06-q343 | yes | Ends on a colon that introduces a list; harmless |
| 131 | m06-l04-ex-1/m06-l04-q024 | yes | TAB row for forward, plus the Mayús+TAB row |
| 132 | m06-l05-ex-2/m06-l05-q037 | yes | The Usar Autofiltro note |
| 133 | m06-l03-ex-6/m06-l03-q163 | yes | COP_VALUE_ENDSWITH ~> row |
| 134 | m06-l02-ex-6/m06-l02-q223 | yes | |
| 135 | m06-l07-ex-5/m06-l07-q132 | yes | |
| 136 | m06-l07-ex-1/m06-l07-q021 | yes | |
| 137 | m06-l05-ex-2/m06-l05-q033 | yes | "Revisar ," spacing is in the source HTML |
| 138 | m06-l07-ex-2/m06-l07-q038 | yes | |
| 139 | m06-l04-ex-8/m06-l04-q350 | yes | |
| 140 | m06-l08-ex-9/m06-l08-q261 | yes | "Alt (en inglés)" is in the source |
| 141 | m06-l01-ex-9/m06-l01-q259 | yes | |
| 142 | m06-l07-ex-10/m06-l07-q337 | yes | |
| 143 | m06-l03-ex-5/m06-l03-q137 | yes | |
| 144 | m06-l07-ex-2/m06-l07-q045 | yes | |
| 145 | m06-l03-ex-4/m06-l03-q112 | no | Flag: not from the unit its heading names. The Bóveda personal sentence is the last of the section before; the key sentence opens the named section ("Si elimina archivos … contenedor de reciclaje de Windows…"). |
| 146 | m06-l02-ex-3/m06-l02-q108 | yes | |
| 147 | m06-l04-ex-8/m06-l04-q349 | yes | |
| 148 | m06-l08-ex-8/m06-l08-q235 | no | Half the fact: "permite que las extensiones … se ejecuten" plus the Bing sentence; missing "Microsoft Edge no podrá impedir que las extensiones guarden el historial…", later in the same section. |
| 149 | m06-l06-ex-12/m06-l06-q426 | yes | |
| 150 | m06-l03-ex-1/m06-l03-q019 | yes | |
| 151 | m06-l08-ex-8/m06-l08-q244 | yes | |
| 152 | m06-l05-ex-6/m06-l05-q206 | no | Wrong row of the argument list: the `valor` row; the key is the next row, "value_if_error Obligatorio. El valor que se devuelve si la fórmula se evalúa como un error." |
| 153 | m06-l02-ex-2/m06-l02-q041 | yes | |
| 154 | m06-l03-ex-3/m06-l03-q069 | yes | "ZIP, RAR. Formatos de archivo 7z y TAR." is word for word from the source |
| 155 | m06-l04-ex-3/m06-l04-q054 | yes | |
| 156 | m06-l06-ex-4/m06-l06-q134 | yes | |
| 157 | m06-l01-ex-10/m06-l01-q342 | yes | [op.acc.6.6] |
| 158 | m06-l07-ex-10/m06-l07-q318 | yes | |
| 159 | m06-l03-ex-2/m06-l03-q047 | yes | |
| 160 | m06-l01-ex-9/m06-l01-q254 | yes | Flag: a pull-quote about another entry of the PDF page is appended. |
| 161 | m06-l03-ex-8/m06-l03-q275 | yes | |
| 162 | m06-l03-ex-5/m06-l03-q156 | yes | Minor: ends on a stray "Nota:" with nothing after it |
| 163 | m06-l02-ex-7/m06-l02-q253 | yes | |
| 164 | m06-l04-ex-10/m06-l04-q392 | yes | |
| 165 | m06-l04-ex-5/m06-l04-q212 | yes | "Delimitador de objeto de objeto" is in the source |
| 166 | m06-l02-ex-8/m06-l02-q311 | yes | |
| 167 | m06-l02-ex-8/m06-l02-q305 | yes | |
| 168 | m06-l05-ex-8/m06-l05-q307 | yes | |
| 169 | m06-l05-ex-6/m06-l05-q219 | yes | Flag: opens with banner text of an inline Copilot banner ("¿Qué necesito saber sobre corregir un error #N/A en Excel?"). |
| 170 | m06-l02-ex-1/m06-l02-q015 | yes | Sentence plus the "winver": list item |
| 171 | m06-l08-ex-5/m06-l08-q143 | yes | |
| 172 | m06-l01-ex-10/m06-l01-q330 | yes | |
| 173 | m06-l02-ex-7/m06-l02-q234 | yes | |
| 174 | m06-l03-ex-8/m06-l03-q263 | yes | |
| 175 | m06-l01-ex-10/m06-l01-q332 | yes | |
| 176 | m06-l02-ex-9/m06-l02-q340 | yes | |

## Misses and flags, grouped by cause (verifier's grouping)

1. Wrong rows picked from a list or table in the right section: 128, 152.
2. Sentence choice leaves out half of a two-part key: 148.
3. Section boundary off by one, a sentence from the previous section: 145.
4. Text that is not content leaks in: 160 (PDF pull-quote), 169 (Copilot banner).
5. Minor: label left dangling at the end: 162.

Not extractor bugs (in the source itself): spaces before punctuation, "de valor Obligatorio", "Delimitador de objeto de
objeto", "Alt (en inglés)", "ZIP, RAR. Formatos de archivo 7z y TAR.".
