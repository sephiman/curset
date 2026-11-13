# Excerpt check — batch 01

| n | key | verdict | note |
|---|---|---|---|
| 1 | m01-l01-q0048 | no | right unit (art. 38 shown), but the key rests on art. 38 closing sección 2.ª (arts. 30–38); no article text shows section bounds — needs the section heading |
| 2 | m01-l01-q0049 | no | right unit (art. 37.1 shown), but the key rests on section membership (sección 2.ª, arts. 30–38), which no article text shows |
| 3 | m01-l05-q0242 | yes |  |
| 4 | m01-l05-q0262 | yes |  |
| 5 | m01-l05-q0269 | yes |  |
| 6 | m01-l06-q0090 | full-only | text cut at «artículo 83. […]» before «medidas alternativas que se determinen reglamentariamente» (same par. 1, second subparagraph) |
| 7 | m01-l06-q0091 | full-only | cut at «artículo 83. […]» before «debidamente comunicada a la autoridad laboral»; the cut falls on the «83. 2 y 3» number dot |
| 8 | m01-l06-q0098 | yes |  |
| 9 | m01-l06-q0100 | yes |  |
| 10 | m01-l06-q0102 | yes |  |
| 11 | m01-l06-q0103 | yes |  |
| 12 | m01-l06-q0104 | yes |  |
| 13 | m01-l06-q0106 | yes |  |
| 14 | m01-l06-q0108 | yes |  |
| 15 | m01-l06-q0109 | yes |  |
| 16 | m01-l06-q0111 | yes |  |
| 17 | m01-l06-q0112 | yes |  |
| 18 | m01-l06-q0113 | yes |  |
| 19 | m01-l06-q0114 | full-only | cite «art. 42»: excerpt shows ap. 1 cut at «artículo 83. […]»; ap. 2 (the cupo) only in full |
| 20 | m01-l06-q0115 | full-only | cite «art. 95»: excerpt shows ap. 1–3.a; 95.4.h (three graves in a year) only in full |
| 21 | m01-l06-q0116 | full-only | cite «art. 95»: excerpt shows ap. 1–3.a; 95.4.a (vejaciones) only in full |
| 22 | m01-l06-q0119 | yes |  |
| 23 | m01-l06-q0121 | yes |  |
| 24 | m01-l06-q0122 | yes |  |
| 25 | m01-l06-q0123 | yes |  |
| 26 | m01-l06-q0125 | yes |  |
| 27 | m01-l06-q0126 | yes |  |
| 28 | m01-l06-q0127 | yes |  |
| 29 | m01-l07-q0423 | yes |  |
| 30 | m01-l07-q0426 | full-only | cite «art. 89» (prompt names 89.4): excerpt shows ap. 1–2; the two-year reserve of 89.4 only in full |
| 31 | m01-l07-q0427 | yes |  |
| 32 | m01-l07-q0428 | full-only | cite «art. 89» (prompt names 89.5): excerpt shows ap. 1–2; 89.5 only in full |
| 33 | m01-l07-q0430 | yes |  |
| 34 | m01-l07-q0431 | yes |  |
| 35 | m01-l07-q0432 | full-only | cite «art. 48» (prompt names 48.l): excerpt shows letters a–b; the fifteen days of letter l) only in full |
| 36 | m01-l07-q0434 | yes |  |
| 37 | m02-l01-q0061 | yes |  |
| 38 | m02-l01-q0062 | yes |  |
| 39 | m02-l01-q0064 | yes |  |
| 40 | m02-l01-q0066 | yes |  |
| 41 | m02-l01-q0068 | yes |  |
| 42 | m02-l01-q0069 | yes |  |
| 43 | m02-l01-q0070 | yes |  |
| 44 | m02-l01-q0071 | yes |  |
| 45 | m02-l01-q0072 | yes |  |
| 46 | m02-l01-q0073 | yes |  |
| 47 | m02-l01-q0074 | yes |  |
| 48 | m02-l01-q0076 | yes |  |
| 49 | m02-l01-q0080 | yes |  |
| 50 | m02-l01-q0081 | yes |  |
| 51 | m02-l01-q0082 | yes |  |
| 52 | m02-l01-q0083 | yes |  |
| 53 | m02-l01-q0085 | yes |  |
| 54 | m02-l01-q0086 | yes |  |
| 55 | m02-l01-q0087 | yes |  |
| 56 | m02-l01-q0089 | yes |  |
| 57 | m02-l01-q0090 | yes |  |
| 58 | m02-l01-q0092 | yes |  |
| 59 | m02-l01-q0093 | yes | 1.6 «complementará» is shown; the second clause (not in the 1.1 list) needs ap. 1, which is only in full |
| 60 | m02-l01-q0095 | yes |  |

Counts: yes 50, full-only 8, no 2, none-ok 0, none-miss 0

## Misses and flags by cause

- **Whole-article citation, fact in a later apartado or letter** (full-only): 19, 20, 21, 30, 32, 35. The citation names the article only (`art. 42`, `art. 95`, `art. 89`, `art. 48`), while the prompt names the apartado or letter (42.2, 95.4.a/h, 89.4, 89.5, 48.l). The excerpt shows the article's opening apartados up to the 200-word cut. Item 31, with the same `art. 89` citation, did get ap. 4, so the extractor can land on the right apartado when it has a hint.
- **Cut inside the paragraph that holds the fact** (full-only): 6, 7. Art. 42.1 RDL 1/2013 is cut at «artículo 83. […]». The cut takes the dot of «83. 2 y 3» as a sentence end and drops the closing clause (autoridad laboral, medidas reglamentarias).
- **Fact is structural and not in any article text** (no): 1, 2. Both questions ask about what sección 2.ª of chapter II of title I contains (arts. 30–38). The cited article is shown correctly, but no article text shows where the section begins or ends.
- Flags: none. There was no garbled text, and every excerpt was the unit its heading names.
