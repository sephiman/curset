# Excerpt check — batch 22

| n | key | verdict | note |
|---|---|---|---|
| 1261 | m03-l08-q0154 | yes |  |
| 1262 | m03-l08-q0155 | yes |  |
| 1263 | m03-l08-q0156 | yes |  |
| 1264 | m03-l08-q0157 | yes |  |
| 1265 | m03-l08-q0158 | yes |  |
| 1266 | m03-l08-q0159 | yes |  |
| 1267 | m03-l08-q0161 | yes |  |
| 1268 | m03-l08-q0162 | yes |  |
| 1269 | m03-l08-q0163 | yes |  |
| 1270 | m03-l08-q0164 | yes |  |
| 1271 | m03-l08-q0166 | yes |  |
| 1272 | m03-l08-q0169 | yes |  |
| 1273 | m03-l08-q0170 | yes |  |
| 1274 | m03-l08-q0171 | yes |  |
| 1275 | m03-l08-q0172 | yes |  |
| 1276 | m03-l08-q0174 | yes |  |
| 1277 | m03-l08-q0175 | yes |  |
| 1278 | m03-l08-q0176 | yes |  |
| 1279 | m03-l08-q0177 | yes |  |
| 1280 | m03-l08-q0178 | yes |  |
| 1281 | m03-l08-q0179 | yes |  |
| 1282 | m03-l08-q0180 | yes |  |
| 1283 | m03-l08-q0181 | yes |  |
| 1284 | m03-l08-q0182 | yes |  |
| 1285 | m03-l08-q0183 | yes |  |
| 1286 | m03-l08-q0184 | no | cite «art. 150.2»: excerpt cut by «[…]» after the «plazo único» paragraph; the last paragraph of 150.2 (no application of art. 104.2 to interrupciones justificadas or dilaciones) is dropped, and excerpt_full is null (unit too long) |
| 1287 | m03-l08-q0185 | yes |  |
| 1288 | m03-l08-q0188 | yes |  |
| 1289 | m03-l08-q0189 | no | cite «art. 150.3»: excerpt shows letras a)–d) then «[…]»; the fact is in letra e) (intento de notificación de la propuesta) and the paragraph after letra g) («Salvo que concurra la circunstancia prevista en la letra e)… la inspección no podrá realizar ninguna actuación»); excerpt_full null |
| 1290 | m03-l08-q0190 | no | cite «art. 150.3»: excerpt shows letras a)–d); fuerza mayor is letra g), cut; excerpt_full null |
| 1291 | m03-l08-q0192 | no | cite «art. 150.3»: excerpt shows letras a)–d); the continuation for unaffected periods/elements is in the first paragraph after letra g) («No obstante, si la Administración Tributaria aprecia…»), cut; excerpt_full null |
| 1292 | m03-l08-q0193 | no | cite «art. 150.3»: excerpt shows letras a)–d); «continuará por el plazo que reste» is the last paragraph of 150.3, cut; excerpt_full null |
| 1293 | m03-l08-q0195 | yes |  |
| 1294 | m03-l08-q0196 | yes |  |
| 1295 | m03-l08-q0197 | yes |  |
| 1296 | m03-l08-q0199 | yes |  |
| 1297 | m03-l08-q0200 | yes |  |
| 1298 | m03-l08-q0201 | yes |  |
| 1299 | m03-l08-q0202 | yes |  |
| 1300 | m03-l08-q0203 | yes |  |
| 1301 | m03-l08-q0204 | yes |  |
| 1302 | m03-l08-q0205 | yes |  |
| 1303 | m03-l08-q0206 | yes |  |
| 1304 | m03-l08-q0217 | yes |  |
| 1305 | m03-l08-q0219 | yes |  |
| 1306 | m03-l08-q0221 | yes |  |
| 1307 | m03-l08-q0222 | yes |  |
| 1308 | m03-l08-q0223 | yes |  |
| 1309 | m03-l08-q0224 | yes |  |
| 1310 | m03-l08-q0226 | yes |  |
| 1311 | m03-l08-q0228 | yes |  |
| 1312 | m03-l08-q0232 | yes |  |
| 1313 | m03-l08-q0233 | yes |  |
| 1314 | m03-l08-q0234 | yes |  |
| 1315 | m03-l08-q0235 | yes |  |
| 1316 | m03-l08-q0236 | yes |  |
| 1317 | m03-l08-q0237 | yes |  |
| 1318 | m03-l08-q0238 | yes |  |
| 1319 | m03-l08-q0239 | yes |  |
| 1320 | m03-l08-q0241 | yes |  |

## Misses and flags by cause

- **Long apartado cut at 200 words, no full text (5):** 1286 (art. 150.2 LGT, last paragraph), 1289, 1290, 1291, 1292 (art. 150.3 LGT, letras e)–g) and the closing paragraphs). Art. 150 LGT is too long for `excerpt_full`, so a cut apartado leaves the reader with nothing; the extractor should pick the paragraph or letra that holds the fact (150.3.e, 150.3.g, 150.3 párrafos finales) instead of the first 200 words.
- No garbled text, no heading/unit mismatch.
