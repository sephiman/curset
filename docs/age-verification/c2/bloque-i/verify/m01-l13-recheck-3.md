# Verification — `m01-l13`, re-check 3 (blind)

- Verifier: blind verifier (opus), did not write the lesson.
- Date: 2026-11-06.
- Files read: `docs/age-verification/c2/bloque-i/spec.md`, `docs/prose-voice.md`, `docs/age-verification/c2/bloque-i/pending/m01-l13.md`,
  `content/age-auxiliar-c2/es/lessons/m01-l13.md` (all of it; every TREBEP and Ley 30/1984 citation extracted from lines 1–950),
  `sources/normativa/BOE-A-1984-17387_ley-30-1984-funcion-publica_2015-10-31.pdf` (BOE notes, disposición adicional decimonovena),
  `sources/normativa/BOE-A-2015-11719_trebep_2026-10-03.pdf`. Precedent for BOE-note citations in a Normativa line:
  `content/age-auxiliar-c2/es/lessons/m01-l14.md` line 882 and `verify/m01-l14-recheck-2.md` (`7c75e1a57b`).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `19ecdab603` | PASS | disposición derogatoria única b) and disposición final cuarta.2 TREBEP; BOE notes to arts. 3, 6–8, 13, 20, 29 and 33 Ley 30/1984; disposición adicional decimonovena Ley 30/1984 | The lesson states Ley 30/1984 rules that still apply. Arts. 13.1 and 18.6 are outside the derogation list. Arts. 29 and 33 are in the list, but the BOE notes keep them in force «en tanto no se oponga… hasta que se dicten las Leyes de Función Pública», and those notes sit in the source after arts. 29 and 33. The disposición adicional decimonovena is not in letter b) and carries no BOE derogation note. The title of the law is exact. «Varias» makes no claim of completeness. Voice is clean | — |
| `eebb595e37` | PASS | Normativa line, TREBEP | The articles cited in the prose are 2.1, 2.5, 7, 8.1–2, 9.1–2, 10.1–5 (incl. 10.1.a)–d)), 11.1, 12.1, 12.3–5, 13.1, 55.1–2, 56.1, 57.1–3, 57.5, 59.1–2, 60.1–3, 61.6, 61.8, 62.1–2, 63, 64.1–2, 65, 66, 67.1–4, 69.1–3, 70.1–2, 71.3, 75.1–2, 76, 80.1, 80.4, 82.1 (table, l. 713), 85.1–2, 86.1, 87.1–3 (incl. 87.1.i)), 88.1–2, 89.2–6, 90.1–2, 90.4, 91 and 98.3. The dispositions cited are DA decimoséptima.4, the derogatoria única (párrafo primero, b) and f)) and DF cuarta.1–2. That is exactly the list. Nothing is listed that the prose does not cite | — |
| `24f0202bb4` | FAIL | Normativa line, Ley 30/1984 | The articles listed are all cited: 13.1, 18.6, 20.2, 29.3 (incl. 29.3.c)), 29.5, 29 bis.1–3, 33 and DA decimonovena. The prose also cites the Ley 30/1984 BOE notes: «notas del BOE a los arts. 3, 6–8, 13 y 20 Ley 30/1984» (l. 123), «nota del BOE al art. 29» and «nota del BOE al art. 33». Arts. 3 and 6–8 appear nowhere in the line. Under the m01-l14 precedent, where line 882 lists «nota del BOE al art. 21», those notes belong in the line. The notes exist in the source after arts. 3, 6, 7, 8, 13, 20, 29 and 33. The «artículo 1.1 de la Ley 30/1984» mention is cited to art. 1 RD 33/1986 and does not count | Ley 30/1984 (reforma de la Función Pública): notas del BOE a los arts. 3, 6–8, 13, 20, 29 y 33; arts. 13.1, 18.6, 20.2, 29.3, 29.5, 29 bis.1–3 y 33; disposición adicional decimonovena. |
