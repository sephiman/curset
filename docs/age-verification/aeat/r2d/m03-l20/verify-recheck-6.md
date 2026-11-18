# m03-l20 — blind verify (re-check 6), 2026-11-17

Sources: `CELEX-02013R0952-20221212_cau_2022-12-12.pdf` (arts. 4.1, 18.1, 79.4, 86.6, 163.1 CAU); `CELEX-02015R2447-20260701_cau-reglamento-ejecucion_2026-07-01.html` (art. 221.2); `CELEX-02015R2446-20261101_cau-reglamento-delegado_2026-11-01.html` (for the Normativa line, via the lesson's «Cita» cells).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `1ec9ddc3c5` | PASS | art. 18.1 CAU, párr. 1 | verbatim | — |
| `f810e8b0c4` | FAIL | art. 18.1 CAU, párr. 2 | text verbatim, but line 169 ends «(art. 18.1 CAU). (art. 18.1 CAU).»: a duplicate citation after the full stop. Structural fix: keep one citation | «Esta representación podrá ser directa, en cuyo caso el representante aduanero actuará en nombre y por cuenta de otra persona, o indirecta, en cuyo caso actuará en su propio nombre pero por cuenta de otra persona.» (art. 18.1 CAU). |
| `8697f15b7d` | PASS | art. 79.4 CAU, párr. 1 | «apartado 1, letra c)» given its article | — |
| `b97f57888e` | PASS | art. 79.4 CAU, párr. 2 | every condition kept | — |
| `321f2e049a` | PASS | art. 86.6 CAU | «del presente Reglamento» given as the Código Aduanero de la Unión; «siempre que … tentativa de fraude» kept | — |
| `42653d17f4` | PASS | art. 221.2 RE, párr. 2 | 3 000 EUR, por envío y por declarante, prohibiciones o restricciones kept | — |
| `cc5758b72e` | PASS | art. 221.2 RE, párr. 3 | — | — |
| `55a41f964e` | PASS | art. 221.2 RE, párr. 4 | — | — |
| `22981ebda6` | FAIL | Normativa, norms not in `normativa.yaml` | Decisión n.º 1/2023 entry is right (anexo IV; arts. 7.1.a).ii)–iii), 7.1.b).ii), 7.3 incl. 7.3.a), 9 a 14; named in arts. 138, 141.1 and 142 RD); 1186/2009, 2658/87, 2017/2455, 2019/883, 2006/112 and the treaties/convenios also right. Missing: the «Acta de adhesión de 2003» named in the art. 4.1 CAU row (line 24), and art. 10.1, letras a) y c), of Reglamento (UE) 2022/2399, named at line 710 (art. 163.1 CAU) | - Convenio relativo a un régimen común de tránsito, Convenio aduanero firmado en París el 18 de mayo de 1963, Tratado de 23 de noviembre de 1964 entre la República Federal de Alemania y la Confederación Suiza, Acta de adhesión de 2003, Tratado relativo al Establecimiento de la República de Chipre, Convenio TIR, Convenio ATA y Convenio de Estambul: nombrados en los arts. 4.1 y 4.2 CAU y 5.1.a).iii), 5.3, 78 y 79 Reglamento Delegado (UE) 2015/2446, sin precepto citado; Reglamento (CE) n.º 1186/2009 (arts. 25.1, 35 a 41 y 115 a 121), nombrado en el art. 86.6 CAU y en los arts. 135.1, 137.1, 138 y 142 Reglamento Delegado (UE) 2015/2446; Reglamento (CEE) n.º 2658/87 (anexo I), nombrado en los arts. 136.1, 138 y 140.1 Reglamento Delegado (UE) 2015/2446; Directiva (UE) 2017/2455 (art. 4.1) y Directiva (UE) 2019/883 (art. 6), nombradas en los arts. 138, 141.5 y 141.8 Reglamento Delegado (UE) 2015/2446; Decisión n.º 1/2023 (anexo IV, arts. 7.1.a).ii)–iii), 7.1.b).ii), 7.3 y 9 a 14), nombrada en los arts. 138, 141.1 y 142 Reglamento Delegado (UE) 2015/2446; Directiva 2006/112/CE (título XII, capítulo 6, sección 4), nombrada en el art. 221.4 Reglamento de Ejecución (UE) 2015/2447; y Reglamento (UE) 2022/2399 (anexo y art. 10.1.a) y c)), nombrado en el art. 163.1 CAU; no figuran en `normativa.yaml`. |

PASS 7 · FAIL 2
