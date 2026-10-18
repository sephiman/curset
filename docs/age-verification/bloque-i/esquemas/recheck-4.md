# Bloque I esquemas — recheck 4, m01-l07 «Plazos de la resolución de acceso y de la reclamación», step 2 (2026-10-18)

Blind reviewer: no earlier verify, fixes or recheck file read. Rule: `spec.md` in this folder. Norm: Ley 19/2013
(BOE-A-2013-12887, consolidated 2022-07-09), arts. 2.1.f), 23, 24 and DA 4.ª, read in full. Prose: section
«Reclamación ante el Consejo de Transparencia y Buen Gobierno» of `content/age-administrativo-c1/es/lessons/m01-l07.md`
(ll. 199–224).

| # | row | citation | PASS/FAIL | passage / reason | replacement |
|---|-----|----------|-----------|------------------|-------------|
| 2 | Reclamación ante el Consejo de Transparencia y Buen Gobierno, potestativa y previa a la vía contencioso-administrativa, salvo en aquellos supuestos en que las Comunidades Autónomas atribuyan la competencia a un órgano específico, de acuerdo con la disposición adicional cuarta; contra las resoluciones de los órganos del artículo 2.1.f) solo cabe recurso contencioso-administrativo — un mes desde el día siguiente al de la notificación del acto o desde el día siguiente a aquel en que se produzcan los efectos del silencio administrativo | arts. 23.2, 24.1, 24.2 y 24.6 Ley 19/2013 | FAIL (clarity only) | Content passes. Art. 24.1 «con carácter potestativo y previo a su impugnación en vía contencioso-administrativa»; 24.2 «en el plazo de un mes a contar desde el día siguiente al de la notificación del acto impugnado o desde el día siguiente a aquel en que se produzcan los efectos del silencio administrativo»; 24.6 «salvo en aquellos supuestos en que las Comunidades Autónomas atribuyan dicha competencia a un órgano específico, de acuerdo con lo establecido en la disposición adicional cuarta»; 23.2 «contra las resoluciones dictadas por los órganos previstos en el artículo 2.1.f) sólo cabrá la interposición de recurso contencioso-administrativo». Every field is verbatim or a faithful shortening; the plazo, the potestativo/previo character, the 24.6 exception and the 23.2 exclusion are all kept; nothing is wider than the articles (DA 4.1 párr. 2.º, autonomous Asambleas and analogous institutions, is covered by «instituciones autonómicas análogas» in 2.1.f)). Every fact is in the prose (ll. 202–204, 206–210, 217–219, 221–224). Citation: one norm, every article named is cited in the prose; it parses as `art-23, art-24`, `Ley 19/2013`; load OK. Order after step 1 is supported (24.2 counts from the notification of the act or from the silence of 20.4). Reason for FAIL: the label ends on «solo cabe recurso contencioso-administrativo» and the plazo cell follows it (beside it on desktop, directly under it on a phone, `EsquemaBlock` `plazos` grid). The row reads «recurso contencioso-administrativo — un mes desde…», i.e. a one-month plazo for the contencioso (LJCA's is two months: an exam trap). Second, «salvo…» comes right after «previa a la vía contencioso-administrativa» and can read as an exception to the potestativo/previo character, not to the Consejo's competence (24.6). | Reclamación ante el Consejo de Transparencia y Buen Gobierno, salvo contra las resoluciones de los órganos del artículo 2.1.f), que solo admiten recurso contencioso-administrativo; potestativa y previa a la vía contencioso-administrativa; la competencia corresponde al Consejo, salvo en aquellos supuestos en que las Comunidades Autónomas atribuyan dicha competencia a un órgano específico, de acuerdo con la disposición adicional cuarta — (plazo field and citation unchanged). Needs no clause the prose lacks (prose ll. 202–204, 206–207, 217–219). Re-run `load_check.py` after the change: the label still writes «artículo 2.1.f)» and «disposición adicional cuarta». |

## Citation checks (read-only)

- `parse_segment('arts. 23.2, 24.1, 24.2 y 24.6 Ley 19/2013')` → `units=(art 23, art 24)`, `norm_text='Ley 19/2013'`.
- `load_check.py ../content/age-administrativo-c1` → `LOAD OK`.
- The course's live citation extraction for m01-l07 (in memory, nothing written) gives the step-2 row one esquema
  item, `arts. 23.2, 24.1, 24.2 y 24.6 Ley 19/2013` (anchors `art-23, art-24`). «disposición adicional cuarta» and
  «artículo 2.1.f)» inside the label produce no esquema citation; the only DA 4.ª and 2.1.f) items are the prose ones
  (`da-cuarta` l. 224, `art. 2.1.f)` elsewhere in the lesson).
- `content/age-administrativo-c1/citations.es.txt` l. 746 is stale: it still reads `arts. 23.2, 24.1 y 24.2 Ley 19/2013`.
  The golden test will fail until it is regenerated (`UPDATE_CITATIONS=1`); the regenerated row changes only that text.
  Anchors are unchanged.

## Verdict

FAIL (clarity only). The content, citation and grammar checks all pass. The label's clause order puts the
contencioso-administrativo right before the one-month plazo, so the row can read as a one-month plazo for the
recurso contencioso-administrativo. The fix is the reordering above, built only from the article's and the prose's
words. Separately, `citations.es.txt` l. 746 needs regenerating.
