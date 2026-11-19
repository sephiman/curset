# Fix brief — `m01-l03`

## caso:### Órganos superiores y órganos directivos#1

Current: Marta es Delegada del Gobierno en una Comunidad Autónoma y Pedro es Subdelegado en una provincia de esa Comunidad. Ambos son órganos directivos de la organización territorial (art. 55.4 LRJSP). Marta tiene rango de Subsecretario y Pedro, nivel de Subdirector general (art. 55.4 LRJSP). Marta, como órgano directivo, tiene condición de alto cargo (art. 55.6 LRJSP).

Blind verifier: FAIL — «Ambos son órganos directivos… Marta, como órgano directivo, tiene condición de alto cargo (art. 55.6 LRJSP)»: el art. 55.6 da la condición de alto cargo a los órganos superiores y directivos «excepto los Subdirectores generales y asimilados»; justificarla «como órgano directivo» justo después de decir que Pedro (nivel de Subdirector general) también lo es deja la regla errónea de que todo órgano directivo, incluido Pedro, es alto cargo. Debe decir que lo es por no ser Subdirector general ni asimilado, y que la excepción alcanza a Pedro como asimilado (o no pronunciarse sobre él).
Student reader: REWRITE — It shows Marta as alto cargo but never shows Pedro (Subdirector general level) is not, which is the exception worth applying.

## caso:### Las entidades públicas empresariales#1

Current: Una entidad pública empresarial se financia con ingresos de mercado (art. 103.1 LRJSP) y contrata a Lucía como personal laboral. El personal se rige por el Derecho laboral, con las especificaciones del artículo 106 (art. 106.1 LRJSP). La contratación de la entidad se rige por la legislación de contratos del sector público (art. 106.6 LRJSP). En su denominación figura «entidad pública empresarial» o «E.P.E.» (art. 103.3 LRJSP).

Blind verifier: PASS — Financiación con ingresos de mercado (art. 103.1), personal laboral con las especificaciones del art. 106 (art. 106.1), contratación por la LCSP (art. 106.6) y la mención «E.P.E.» (art. 103.3).
Student reader: REWRITE — The "No confundir" point is EPE versus organismo autónomo, yet the case never contrasts them; show Lucía's regime in each.

