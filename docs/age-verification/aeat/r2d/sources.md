# R2d: fuentes descargadas (2026-11-14)

Todas desde boe.es con curl (User-Agent genérico); no hizo falta Playwright. Cada fichero se descargó primero en una carpeta nueva del scratchpad (`fetch/<id>/`), se comprobó título, id y fecha con `pdftotext` y luego se copió a `content/aeat-agentes-hacienda/sources/normativa/`.
Ids: ninguno tomado de memoria sin verificar. Los ids se localizaron con la API de búsqueda de legislación consolidada del BOE y cada uno se verificó con el título en `diario_boe/xml.php` y en el PDF; el de la Comisión de Seguridad y Control (BOE-A-1998-2494) viene de la nota «Véase» de la Orden de 1994.

| BOE id | Norma | Fecha (consolidación o publicación) | sha256 | Cómo |
|---|---|---|---|---|
| BOE-A-2024-26915 | RDL 9/2024 (medidas urgentes; derogado) | 2025-01-23 | `2d018bcbfae335572c8692359d0910b3871502b25a6edbfd00fa38b3ff80c159` | PDF consolidado https://www.boe.es/buscar/pdf/2024/BOE-A-2024-26915-consolidado.pdf (curl) |
| BOE-A-2025-1136 | Resolución de 22-01-2025 (derogación del RDL 9/2024) | 2025-01-23 | `9fd57c95c80455eb111ed9b71f9963747c81d50ea261156f021fa174e1a27c58` | PDF del diario (curl) |
| BOE-A-2025-26458 | RDL 16/2025 (prórroga de medidas; derogado) | 2026-01-28 | `a4f82a8cb3df7e9ed88802b7a5fc46f69c934bb619652f59d4b6669374ce0111` | PDF consolidado https://www.boe.es/buscar/pdf/2025/BOE-A-2025-26458-consolidado.pdf (curl) |
| BOE-A-2026-2024 | Resolución de 27-01-2026 (derogación del RDL 16/2025) | 2026-01-28 | `d9f03317c6cb9296c9547b96fe0cbaee484b02734d40220f2a4ef33f04868582` | PDF del diario (curl) |
| BOE-A-2026-2547 | RDL 2/2026 (medidas urgentes; derogado) | 2026-02-28 | `3bcc7dec8ee105019535a017734ef46e95b620480fc3299a5d8607dcafb9bda0` | PDF consolidado https://www.boe.es/buscar/pdf/2026/BOE-A-2026-2547-consolidado.pdf (curl) |
| BOE-A-2026-4667 | Resolución de 26-02-2026 (derogación del RDL 2/2026) | 2026-02-28 | `35b53169fcb92a6ddf3b36a94faf57865229e174945fced5d2601f60991f7f16` | PDF del diario (curl) |
| BOE-A-2023-16461 | Orden HFP/792/2023 (dietas y gastos de locomoción en el IRPF) | 2023-07-17 | `35a0e51fee696ad8951cd78efa0c256f079348965db6356c1ebd8151044d476b` | PDF del diario (curl) |
| BOE-A-2010-17575 | RD 1363/2010 (notificaciones electrónicas obligatorias en la AEAT) | 2014-05-14 | `59f1e4ed26f4bf581ba3e1a9c5407657658e8e4a8ab94d85b3ef8b8495d452f8` | PDF consolidado https://www.boe.es/buscar/pdf/2010/BOE-A-2010-17575-consolidado.pdf (curl) |
| BOE-A-2008-20953 | Orden EHA/3786/2008 (modelo 303 de IVA) | 2026-01-26 | `2f3eb8c3569ea5fc00dc3ba96471249086b463e828ac88c6ddc5136b1d7c9780` | PDF consolidado https://www.boe.es/buscar/pdf/2008/BOE-A-2008-20953-consolidado.pdf (curl) |
| BOE-A-2026-1761 | Orden HAC/27/2026 (modifica modelos 303, 322, 353 y otros de IVA) | 2026-01-26 | `0552f1b8b0e30b22a63e0cc4be29f5ba8ab050609dcb04ed16549b8eb5030694` | PDF del diario (curl) |
| BOE-A-2009-18472 | Orden EHA/3111/2009 (modelo 390 de IVA) | 2026-01-26 | `df2ae8090c8f706a7e7443e311e5a3b4ac916e3176451c93b6d8a64ce95f5e00` | PDF consolidado https://www.boe.es/buscar/pdf/2009/BOE-A-2009-18472-consolidado.pdf (curl) |
| BOE-A-2009-18567 | Orden EHA/3127/2009 (modelo 190) | 2025-12-12 | `486c23bcea2fd3a869a719f2def8d6dcca47f622908adfe66483323bc1833630` | PDF consolidado https://www.boe.es/buscar/pdf/2009/BOE-A-2009-18567-consolidado.pdf (curl) |
| BOE-A-2007-6032 | Orden EHA/672/2007 (modelos 130 y 131) | 2015-02-19 | `9f9810e7908a11795573319b24fd71d398ecf91b0142946bf9ec62f2b1f9399b` | PDF consolidado https://www.boe.es/buscar/pdf/2007/BOE-A-2007-6032-consolidado.pdf (curl) |
| BOE-A-2017-2778 | Orden HFP/227/2017 (modelos 202 y 222) | 2025-03-19 | `c62ba7dc4c49de3e558e720ce05ea2a9dd091e02bc92ed88de2607660dae04e1` | PDF consolidado https://www.boe.es/buscar/pdf/2017/BOE-A-2017-2778-consolidado.pdf (curl) |
| BOE-A-2026-11583 | Orden HAC/529/2026 (modelo 200, períodos iniciados en 2025) | 2026-05-29 | `63a56f49b548c6e5f1b464f3230c53a6c623bfed0ec0733c0e121a81cdc3c301` | PDF del diario (curl) |
| BOE-A-1996-29117 | Ley 13/1996 (medidas fiscales, administrativas y del orden social) | 2025-09-30 | `090a6c0c8ee277ae6d6fa14c1a6779ecc3eba62c23c49380434718c82d7dfd5d` | PDF consolidado https://www.boe.es/buscar/pdf/1996/BOE-A-1996-29117-consolidado.pdf (curl) |
| BOE-A-2012-15650 | Ley 16/2012 (medidas tributarias; impuesto sobre depósitos) | 2014-10-17 | `0fcd69133cd73f4ba44298f89ada6bcb4ed7d89738ad81b212df9b4c4a1c886a` | PDF consolidado https://www.boe.es/buscar/pdf/2012/BOE-A-2012-15650-consolidado.pdf (curl) |
| BOE-A-2012-15649 | Ley 15/2012 (sostenibilidad energética) | 2026-09-30 | `06df93bb51f515984b1b7f4f1a6279849cdb62fe50e933ac3ccd068f38040f6c` | PDF consolidado https://www.boe.es/buscar/pdf/2012/BOE-A-2012-15649-consolidado.pdf (curl) |
| BOE-A-2013-11331 | Ley 16/2013 (fiscalidad medioambiental; gases fluorados) | 2022-07-09 | `b70b94156c9c8d3fcc93374721cff839d344a108de17f30364e22899c22bc9e1` | PDF consolidado https://www.boe.es/buscar/pdf/2013/BOE-A-2013-11331-consolidado.pdf (curl) |
| BOE-A-2015-5633 | Ley 8/2015 (hidrocarburos; extracción de gas, petróleo y condensados) | 2015-05-22 | `a1985587e90700adfcb45e6fface0996fd53f03b6e5058a8925c1e8787fef59a` | PDF consolidado https://www.boe.es/buscar/pdf/2015/BOE-A-2015-5633-consolidado.pdf (curl) |
| BOE-A-2011-9280 | Ley 13/2011 (regulación del juego) | 2022-12-31 | `c16d1cdc5835bbbc2e7319070a71e8c5105643c3234d7e3de73a76d8a5952d18` | PDF consolidado https://www.boe.es/buscar/pdf/2011/BOE-A-2011-9280-consolidado.pdf (curl) |
| BOE-A-2020-12355 | Ley 4/2020 (Impuesto sobre Determinados Servicios Digitales) | 2020-10-16 | `26e60ae323b2fb9fb44109b240cede705ee28bc63ff5b3621f473d8df4538047` | PDF consolidado https://www.boe.es/buscar/pdf/2020/BOE-A-2020-12355-consolidado.pdf (curl) |
| BOE-A-2020-12356 | Ley 5/2020 (Impuesto sobre las Transacciones Financieras) | 2022-07-01 | `dfcce3897aea8a69f7db44057c1d45e6dd7738e6ddd1f02f3536cb6ef492810a` | PDF consolidado https://www.boe.es/buscar/pdf/2020/BOE-A-2020-12356-consolidado.pdf (curl) |
| BOE-A-2022-5809 | Ley 7/2022 (residuos; envases de plástico y depósito de residuos) | 2025-04-02 | `0cb40737c77c3724816ddfcdb470e739dd0cd85e9a3ac73e56cbf5cdfe42b9a9` | PDF consolidado https://www.boe.es/buscar/pdf/2022/BOE-A-2022-5809-consolidado.pdf (curl) |
| BOE-A-2024-26694 | Ley 7/2024 (Impuesto Complementario; margen de intereses y comisiones) | 2026-10-03 | `254a2591269fa9d77c5093eb009ba89f803ba86820a017c05e9947f3f485feb5` | PDF consolidado https://www.boe.es/buscar/pdf/2024/BOE-A-2024-26694-consolidado.pdf (curl) |
| BOE-A-1991-14463 | Ley 20/1991 (aspectos fiscales del REF de Canarias) | 2022-12-24 | `a95a22c2d9dd77665350a4c6ffea40fb3f23071504e6eb4b00a5cf6259f6e431` | PDF consolidado https://www.boe.es/buscar/pdf/1991/BOE-A-1991-14463-consolidado.pdf (curl) |
| BOE-A-1991-7645 | Ley 8/1991 (IPSI de Ceuta y Melilla) | 2013-07-27 | `e355abd6b43102ce10121c2bbe1132e0e77b1a1846cd55e810f5d5c1bf8a4c07` | PDF consolidado https://www.boe.es/buscar/pdf/1991/BOE-A-1991-7645-consolidado.pdf (curl) |
| BOE-A-2023-26452 | RDL 8/2023 (medidas económicas y sociales; prórroga de gravámenes temporales) | 2026-10-07 | `02ad9516bdfd4a0aa4696dfd6e5b11cd9fd15f483748869aa7e6f4b230440376` | PDF consolidado https://www.boe.es/buscar/pdf/2023/BOE-A-2023-26452-consolidado.pdf (curl) |
| BOE-A-1998-2494 | Resolución de 26-01-1998 (Comisión de Seguridad y Control de la AEAT) | 1998-02-05 | `9452250b2d728a201fce762856549011c1fd100e0b67cb9561b0ad8867c0802b` | PDF del diario (curl) |
| BOE-A-2007-9508 | Orden EHA/1274/2007 (modelos 036 y 037) | 2025-01-09 | `e9a250f7d8e6d46904002e9d5c27942cf84a25e824aa20952d2f5dbb41f66879` | PDF consolidado https://www.boe.es/buscar/pdf/2007/BOE-A-2007-9508-consolidado.pdf (curl) |
| BOE-A-2023-24840 | RD 1007/2023 (sistemas informáticos de facturación; VERI*FACTU) | 2025-12-03 | `34418589f3c5684cbb5aa55cf208d08de96e81bb216623c14db51f3da5b9731f` | PDF consolidado https://www.boe.es/buscar/pdf/2023/BOE-A-2023-24840-consolidado.pdf (curl) |
| BOE-A-2006-20764 (art. 23) | XML versiones | 2026-11-14 | `02acd2e6f63dccae2af195920832ebeb352828d82f8214abb8508bada9da991f` | API datos abiertos, Accept: application/xml (curl) |

## Observaciones

- BOE-A-2026-4667 es la Resolución de 26-02-2026 (derogación del RDL 2/2026); la de 27-01-2026 (BOE-A-2026-2024) es la del RDL 16/2025.
- Orden HFP/792/2023 = BOE-A-2023-16461 (dietas y locomoción en el IRPF). La HFP/793/2023 (BOE-A-2023-16462, uso de vehículo particular, RD 462/2002) no se descargó.
- Art. 104 h) RGAT remite a la disposición adicional tercera del RD 1363/2010 (BOE-A-2010-17575).
- Modelo 200: la orden de los períodos de 2025 es la HAC/529/2026; la HAC/565/2020 (períodos de 2019) no se descargó. Modelo 303: la orden base EHA/3786/2008 consolidada y la HAC/27/2026 que la modifica.
- Modelos 036/037: Orden EHA/1274/2007, consolidada a 09-01-2025.
- Ley 8/2015: el impuesto sobre el valor de la extracción de gas, petróleo y condensados está en el capítulo II (art. 9 ss.), verificado en el PDF.
- No obtenido: nada.

## Lote 3

Ids verificados con la API de búsqueda del BOE y el título del PDF.

| BOE id | Norma | Fecha | sha256 | Cómo |
|---|---|---|---|---|
| BOE-A-1985-11672 | LOREG (LO 5/1985) | 2026-07-02 | `861ea98cd5bf21c4b6d2349cebfe244f0a525cf3c812e546bff05ec15f57d1c7` | PDF consolidado https://www.boe.es/buscar/pdf/1985/BOE-A-1985-11672-consolidado.pdf (curl) |
| BOE-A-1982-837 | Ley 50/1981 (Estatuto Orgánico del Ministerio Fiscal) | 2025-01-03 | `e43539cd5eb942b30001cf53005939d152090a06da306bc0b968159e3e093374` | PDF consolidado https://www.boe.es/buscar/pdf/1982/BOE-A-1982-837-consolidado.pdf (curl) |
| BOE-A-1984-7249 | LO 3/1984 (iniciativa legislativa popular) | 2015-03-31 | `3a3790230df681ce09be7ab306c93d4df0d24f2dce960f4e4a857f6ce17c8eab` | PDF consolidado https://www.boe.es/buscar/pdf/1984/BOE-A-1984-7249-consolidado.pdf (curl) |
| BOE-A-1980-1564 | LO 2/1980 (modalidades de referéndum) | 1980-12-24 | `3a6a6ef13f6ae61a17327b882f63cee935dc44b65545e78cb83a6287e3011f44` | PDF consolidado https://www.boe.es/buscar/pdf/1980/BOE-A-1980-1564-consolidado.pdf (curl) |

## Lote 4

Ids verificados con la API de búsqueda del BOE y el título del PDF.

| BOE id | Norma | Fecha | sha256 | Cómo |
|---|---|---|---|---|
| BOE-A-2022-14580 | Ley 16/2022 (reforma del TR de la Ley Concursal) | 2022-12-28 | `09f9df3cfa8a8345c57961bcecf483878fd515141d6689c5fff7faec38429dd7` | PDF consolidado (curl) |
| BOE-A-2020-4859 | TRLC (RDLeg 1/2020) | 2025-01-03 | `444e25fea9b78b269bdbf86d9f9797220e64c7a253c4276569e413224a4b8cf9` | PDF consolidado (curl) |
| BOE-A-1946-2453 | Ley Hipotecaria (Decreto de 8-02-1946) | 2025-01-03 | `a24234f737b698e47f7f8c1d1f740b1ca01b392d493dc10bd9c1556813e40885` | PDF consolidado (curl) |
| BOE-A-1947-3843 | Reglamento Hipotecario (Decreto de 14-02-1947) | 2020-11-26 | `53b7401ad6cd14f21a25aaf6dd96ae16098a8f6964923384a3407a3dc73f6e11` | PDF consolidado (curl) |
| BOE-A-1994-26003 | LAU (Ley 29/1994) | 2026-11-13 | `fe895bd297942e6a95fb56603c84a037912e53b8362989a3c9b47b7a002e351f` | PDF consolidado (curl) |
| BOE-A-1996-8930 | TRLPI (RDLeg 1/1996) | 2022-03-30 | `42458597f9ea311636f3a757e6636b24c68876433af599fd77a08f0894b675c0` | PDF consolidado (curl) |
| BOE-A-2002-24252 | TRLPFP (RDLeg 1/2002) | 2022-12-24 | `4bf03ce6fae79a0dded6daffc0c6f483cc35ab673bf9e5e4c3148b8c4c1e62cd` | PDF consolidado (curl) |
| BOE-A-2009-10326 | Orden EHA/1658/2009 (domiciliación del pago de deudas) | 2026-06-23 | `1ec682eeb157f36bf91720be539f9d5b7e1bfdc2466ab0184d140666bb386b43` | PDF consolidado (curl) |
| BOE-A-2007-13223 | Orden EHA/2027/2007 (entidades de crédito colaboradoras en la recaudación) | 2025-12-22 | `a5012ed57542f8ef7c7d8235806edbe0aaa5ddaa927fe9e03cbacea91db41bc4` | PDF consolidado (curl) |
| BOE-A-1998-13072 | Orden de 4-06-1998 (gestión recaudatoria de las tasas) | 2025-03-14 | `c0a2008680e23a2533c1f8943b0e6da05e1993efd576b937af3f37de4be90bad` | PDF consolidado (curl) |

No obtenido: la orden ministerial que fija el límite de pago con tarjeta (art. 36.2 RGR). El RGR no la nombra («la orden del Ministro de Economía y Hacienda correspondiente»); ni la Orden EHA/1658/2009 (domiciliación), ni la EHA/2027/2007, ni la Orden de 4-06-1998 contienen un límite. Búsqueda en la API de legislación consolidada sin resultado.
| Ley 10/2014 (entidades de crédito) | BOE-A-2014-6726 | sources/normativa/BOE-A-2014-6726_ley-10-2014-entidades-credito_2023-06-29.pdf | 333bd6236629dc86b15092cf6411c6a2afd4dea94db5e83b9696a6c3face617c | 2026-11-18, for art. 9.1.º.c) c´) LIVA (III.19) |
