# Verify re-check 1 — `m03-l08` (R2d, blind, 2026-11-14)

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `bcf89a085b` | PASS | art. 117.1.c), e), k) LGT | letters c), e), k) verbatim (k) cut before «en los términos establecidos en la normativa específica», no condition lost) | — |
| `0875ee4ede` | PASS | art. 169.1 RGAT | verbatim, first paragraph | — |
| `498c2652a4` | PASS | art. 172.3 RGAT | verbatim; «autoridades del artículo 172.2» = delegado or director de departamento | — |
| `f581e4a9a4` | PASS | art. 185.1 RGAT | first paragraph verbatim | — |
| `832d12d984` | PASS | art. 186.1 RGAT | verbatim | — |
| `4fb29f2e56` | PASS | art. 186.7, second paragraph and a)–c) RGAT | lead-in and a)–c) complete, nested under the lead-in | — |
| `5889338ae2` | PASS | art. 187.2 and 187.2.a) RGAT | a) with 1.º and 2.º, nested | — |
| `5e85f2d158` | PASS | art. 187.2.a).2.º and b) RGAT | minoración sentence and letter b) verbatim | — |
| `d384468f5c` | PASS | art. 187.3.b) RGAT | verbatim (rendering of its list is the lead-in's row below) | — |
| `6a2d2dbc13` | PASS | art. 188.4 RGAT | lead-in and a)–b) complete, nested | — |
| `7041fc7537` | PASS | art. 186.7 RGAT | «No confundir»: first sentence of 186.7 verbatim with its own citation, beside 155.5 LGT verbatim | — |
| `6742a52183` | PASS | LGT cited in prose | every LGT article cited in the prose (7.2, 13, 15, 16, 26.2, 27, 31, 32.2, 34.1.h, 41/41.4, 53/53.1, 62/62.2, 66/66.a, 66 bis.2, 68.1.a, 93, 94, 99.7, 101.3–4, 104.2, 108.2, 111, 113–117.1, 134–159, 179.3, 188.1, 191–197, 203.1, 251) is listed and vice versa | — |
| `e86bae2619` | PASS | art. 150.3.f) and closing paragraph LGT | names art. 47 ter (apartado tres) of the Concierto; prose lines 390, 399 | — |
| `e27ca7f0df` | PASS | art. 166.2.b) and 166.3.b) RGAT | name RDLeg 1/2004 and art. 46.3 Ley 21/2001; no normativa.yaml entries | — |
| `a56dab8213` | FAIL | art. 187.3 RGAT | lead-in «En ese caso se procede de la siguiente forma:» (line 665): the a)–c) items of art. 187.3 (lines 666–668) render as sibling top-level items, not nested under it. Fix: indent lines 666–668 as sub-items of line 665 | En ese caso se procede de la siguiente forma: |

PASS 14 · FAIL 1
