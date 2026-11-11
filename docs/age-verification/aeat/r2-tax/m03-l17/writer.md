# Writer notes: m03-l17 (III.17, Impuesto sobre Sociedades)

## 1. Sources
- LIS `BOE-A-2014-12328_lis_2026-09-02.pdf` (pdftotext): arts. 1–11 (title I–IV, cap. I), 17.1, 20, 23–34 (arts. 30 bis, 35–39 read, not used), 40–41, 109–111, 124–127.
- RIS not used: no coverage question asks for it and no programme phrase needs it; no RIS citation in the lesson.
- RDL 22/2026 (arts. 33.1 and 3; `normativa.yaml` note: convalidado): the lesson states the text in force without a mark (60 %, 60.000 / 1.200.000 and 120.000 / 2.400.000 euros).

## 2. Pack questions (8 coverage of 8 stated; reference 2024-40 also stated)
| id | lesson section |
|---|---|
| 2025-11 | Doble imposición económica internacional (art. 32.1 LIS) |
| 2025-18 | Compensación de bases imponibles negativas (art. 26.1 LIS: 70 %, no time limit stated; the 10 years of art. 26.5 are the prescription of the Administration's right) |
| 2025-58 | Contribuyentes del impuesto (arts. 7.1.a), 2.1, 8.1, 6.1 LIS) |
| 2025-75 | Exenciones, last two paragraphs (arts. 9.3, 109, 110.1.a) LIS) |
| 2024-82 | Contribuyentes del impuesto (art. 7.2 LIS) |
| 2024-86 | Valoración de los elementos patrimoniales (art. 17.1 LIS) |
| 2024-94 | Efectos de la valoración contable diferente a la fiscal (art. 20 LIS) |
| 2022-45, 2024-40 (ref) | Pago fraccionado (art. 40.1 LIS; rest in m03-l06) |

## 3. Lo que más cae
1 art. 40.1: 2022-45, 2024-40. 2 art. 7.1.a): 2025-58. 3 art. 7.2: 2024-82. 4 art. 26.1: 2025-18. 5 art. 32.1: 2025-11. 6 art. 17.1: 2024-86. 7 art. 20: 2024-94. 8 arts. 9.3 and 110.1.a): 2025-75. 9 art. 9.3.c): 2025-75 (ledger: asked with 9.3). 10 art. 7.1 residencia: 2025-58 (distractor). Fewer than ten distinct coverage facts (8 questions); lines 9–10 repeat facts of those questions.

## 4. Worked examples
None (the plan lists none).

## 5. Course summary
El Impuesto sobre Sociedades es un tributo directo y personal que grava la renta de las sociedades y demás entidades jurídicas residentes en territorio español. Su base imponible parte del resultado contable corregido por la LIS, con reglas de imputación temporal y reducciones, y tributa al 25 por ciento salvo los tipos especiales del artículo 29. La declaración se presenta en los 25 días naturales siguientes a los 6 meses posteriores a la conclusión del período impositivo.

## 6. Glossary proposals
`g-hecho-imponible` and `g-devengo` exist (LGT definitions); not repeated.
```yaml
- id: g-cuota-integra-is
  es: cuota íntegra del Impuesto sobre Sociedades
  origin: m03-l17
  definition: {es: «La cantidad resultante de aplicar a la base imponible el tipo de gravamen» (art. 30.1 LIS).}
- id: g-actividad-economica-is
  es: actividad económica
  origin: m03-l17
  definition: {es: La ordenación por cuenta propia de los medios de producción y de recursos humanos o de uno de ambos con la finalidad de intervenir en la producción o distribución de bienes o servicios (art. 5.1 LIS).}
- id: g-entidad-patrimonial
  es: entidad patrimonial
  origin: m03-l17
  definition: {es: Aquella en la que más de la mitad de su activo está constituido por valores o no está afecto a una actividad económica; no realiza una actividad económica (art. 5.2 LIS).}
```

## 7. Unresolved, left out, ambiguities
- cites.py: 0 unresolved.
- Norms the prose names that `normativa.yaml` lacks, so they have no «Normativa» line: Ley 49/2002 (arts. 9.2 and 29.3 LIS), Ley 27/1984, the laws of the 9.1.f)–g), 9.4, 29.4, 29.6 and 29.7 LIS, the Ley de Partidos. The prose names them generically («la ley de régimen fiscal de las entidades sin fines lucrativos…», without number); decide whether platform section M adds them. The only numbered one left in the prose is Ley 7/1985 (LBRL, in `normativa.yaml`).
- Left out: arts. 11.8–11.10, 11.12–13 detail (one structure sentence only); 5.1 third paragraph and 5.2 second–fourth paragraphs (grupo, valores); 23.2, 23.4, 23.6–7; 24.3–4; 25.3; 26.4.c) 2.º–4.º detail; 29.4 sub-rules (SICAV accionistas, 3 and 7 years); 29.1 SICAV details; 30 bis (tributación mínima); 31.4, 32.2; 33.4–6 (pesca, navegación, rentas fuera de las ciudades); 40.2–5 and 41 (in m03-l06); 124.1 third paragraph kept; 128 onward. None asked and none named by the programme beyond their article's headline.
- RDL 22/2026 changed art. 33.1 and 3; convalidated per `normativa.yaml`, so no mark. The verifier should check 60 % and the euro limits against the snapshot text (they are as printed).
