# Re-check 1 — `m02-l10` (II.10 Access 365)

- Verifier: blind verifier (opus), did not write the lesson or the proposed fixes.
- Date: 2026-11-06.
- Files read: `docs/age-verification/c2/bloque-ii/pending/m02-l10.md`; `content/age-auxiliar-c2/es/lessons/m02-l10.md`;
  `content/age-auxiliar-c2/sources/otros/fuentes.yaml`; saved pages (text stripped from HTML)
  `ms-access-formato-numero.html`, `ms-access-glosario.html`, `ms-access-formularios.html`,
  `ms-access-subformulario.html`, `ms-access-consulta-seleccion.html`, `ms-access-no-coincidentes.html`,
  `ms-access-duplicados.html`.
- `ms-access-glosario.html`, which is newly cited in the input-mask item, matches its sha256 in `fuentes.yaml` and is
  listed in «Fuentes». «Fuentes» still lists exactly the files cited in the lesson body.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `fca05464b9` | PASS | ms-access-formato-numero.html; «Ejemplos de formatos predefinidos» | the page's table has exactly seven formats (Número general, Moneda, Euro, Corregido, Estándar, Porcentaje, Científico) and the item lists all seven, so no «entre otros» is needed. Each description is literal: «(Predeterminado) Muestra el número tal y como se ha introducido»; «Usa el separador de miles»; «Usa el símbolo del euro (€)»; «Muestra al menos un dígito»; «Multiplica el valor por 100 y anexa un signo de porcentaje (%)»; «Utiliza notación científica estándar». The Spanish UI label «Corregido» is still unconfirmed beyond the page (ledger) | — |
| `6e0efdaef8` | PASS | ms-access-glosario.html; «máscara de entrada» | «Un formato que consta de caracteres de visualización literales … y caracteres de máscara que especifican dónde se deben escribir los datos, así como qué tipo de datos y cuántos caracteres se permiten» | — |
| `c3256cad2f` | PASS | ms-access-formularios.html; ms-access-subformulario.html | the views Presentación and Diseño, and Formulario next to Hoja de datos in the split form, are in formularios; subformulario has «la vista Formulario, para que pueda ver o introducir información». «entre otras» marks the list as partial | — |
| `e2dc4350f2` | PASS | ms-access-consulta-seleccion.html; ms-access-no-coincidentes.html; ms-access-duplicados.html | «Nueva consulta»: «Asistente para consultas sencillas»; «Asistente para consultas de buscar no coincidentes»; «Asistente para buscar consultas duplicadas». «entre otros» marks the list as partial | — |

PASS 4, FAIL 0.
