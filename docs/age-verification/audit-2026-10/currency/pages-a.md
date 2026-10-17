# Currency check C1b, share «a» (fuentes.yaml, files not starting with «ms-»)

Date 2026-10-17. Live copies in `SP/currency/pages/` (SP = the session scratchpad); text extracts and diffs in `SP/currency/txt/`.
Every stored file's sha256 matches the `sha256` in `fuentes.yaml`.

Entries: 51. identical 32, text-identical 19, changed 0, gone 0.

| File | Status | HTTP / final URL | Note |
|---|---|---|---|
| `un-res-70-1-agenda-2030.pdf` | identical | 200 / https://documents.un.org/doc/undoc/gen/n15/291/93/pdf/n1529193.pdf | Redirect from the UN document API to the PDF file itself (same document). |
| `un-ods-objetivos.html` | text-identical | 200 / https://www.un.org/sustainabledevelopment/es/sustainable-development-goals/ | Markup only (Slider Revolution nonce); final URL is the site's canonical slug for the same page. |
| `transparencia-gobierno-abierto-que-es.html` | identical | 200 / same |  |
| `transparencia-planes-accion.html` | identical | 200 / same |  |
| `transparencia-planes-anteriores.html` | identical | 200 / same |  |
| `transparencia-iv-plan.html` | identical | 200 / same |  |
| `transparencia-iv-plan.pdf` | identical | 200 / same |  |
| `transparencia-v-plan.html` | identical | 200 / same |  |
| `transparencia-v-plan.pdf` | identical | 200 / same |  |
| `ue-paises.html` | text-identical | 200 / same | Markup only (menu/ECL attributes); readable text unchanged. |
| `ue-parlamento-europeo.html` | text-identical | 200 / same | Markup only; readable text unchanged. |
| `ue-consejo-europeo.html` | text-identical | 200 / same | Markup only; readable text unchanged. |
| `ue-consejo.html` | text-identical | 200 / same | Markup only; readable text unchanged. |
| `ue-comision-europea.html` | text-identical | 200 / same | Markup only; readable text unchanged. |
| `ue-tjue.html` | text-identical | 200 / same | Markup only; readable text unchanged. |
| `curia-tribunal-de-justicia.html` | text-identical | 200 / https://curia.europa.eu/site/jcms/d2_5093/es/ | Old Jo2_7024 URL redirects to the new CURIA site path; same page (stored copy already carries canonical d2_5093/es/el-tribunal-de-justicia). Text differs only in an anti-bot token blob at the end. |
| `curia-tribunal-general.html` | text-identical | 200 / https://curia.europa.eu/site/jcms/d2_5094/es/ | Old Jo2_7033 URL redirects to the new CURIA site path; same page (stored copy already carries canonical d2_5094/es/el-tribunal-general). Text differs only in an anti-bot token blob. |
| `comision-colegio.html` | text-identical | 200 / same | Markup only (JSON-LD datePublished metadata 2025-07-18 -> 2025-07-28); readable text unchanged. |
| `oecd-recomendacion-gobierno-abierto-2017.pdf` | identical | 200 / same |  |
| `boe-analisis-ce.xml` | identical | 200 / same | Script fetch without Accept header got 400; refetched with `Accept: application/xml`: 200, sha256 equal. |
| `cultura-dta-diccionario.html` | identical | 200 / same |  |
| `cultura-dta-presentacion.html` | identical | 200 / same |  |
| `pag-quienes-somos.html` | text-identical | 200 / same | Markup only (navigation link href); readable text unchanged. |
| `pag-telefono-060.html` | identical | 200 / same |  |
| `pag-oficina-informacion.html` | identical | 200 / same |  |
| `sede-pag-portada.html` | identical | 200 / same |  |
| `clave-que-es.html` | identical | 200 / same |  |
| `pae-circe.html` | text-identical | 200 / same | Markup only (SharePoint script revs); readable text unchanged. |
| `pae-servicios.html` | text-identical | 200 / same | Markup only (SharePoint script revs); readable text unchanged. |
| `pae-subsede.html` | text-identical | 200 / same | Markup only (SharePoint script revs); readable text unchanged. |
| `doue-rgpd-correccion-2018.pdf` | identical | 200 / same |  |
| `doue-rgpd-correccion-2021.pdf` | identical | 200 / same |  |
| `sepg-retribuciones-funcionarios-2026.pdf` | identical | 200 / same |  |
| `sepg-cuantias-retributivas-2026.pdf` | identical | 200 / same |  |
| `boe-api-leyes-pge_2026-10-17.json` | identical | 200 / API query (see note) | The `url` field is an API query description, not a URL (curl 000). Re-ran the described query (query_string `titulo:(presupuestos generales estado año)`, sort fecha_publicacion desc, limit 50, `Accept: application/json`): 200, sha256 equal. |
| `nist-prefijos-binarios.html` | text-identical | 200 / same | Markup only (Cloudflare beacon); readable text unchanged. |
| `incibe-glosario-ciberseguridad.pdf` | identical | 200 / same |  |
| `boe-rd-4-2010-eni.pdf` | identical | 200 / same |  |
| `azure-vdi.html` | text-identical | 200 / same | Only the per-request «Trace Id» line differs. |
| `azure-almacenamiento-nube.html` | text-identical | 200 / same | Only the per-request «Trace Id» line differs. |
| `apple-macos.html` | identical | 200 / same |  |
| `isoc-historia-internet.html` | text-identical | 200 / same | Only the footer social link («Stay connected»: Facebook -> Instagram) differs. |
| `whatwg-html-introduccion.html` | identical | 200 / same |  |
| `ue-com-2023-442-web-4-0.pdf` | identical | 200 / same |  |
| `rfc1122-capas-tcp-ip.txt` | identical | 200 / same |  |
| `rfc1918-direcciones-privadas.txt` | identical | 200 / same |  |
| `dominios-es-sobre-nosotros.html` | text-identical | 200 / same | Markup only (Incapsula script query); readable text unchanged. |
| `whatwg-html-scripting.html` | identical | 200 / same |  |
| `euskadi-diseno-adaptable.html` | identical | 200 / same |  |
| `aepd-guia-cookies.pdf` | identical | 200 / same |  |
| `rfc5322-formato-mensaje.txt` | identical | 200 / same |  |

Text-identical without any readable-text diff: the pagetext extract is byte-equal; only markup, scripts or metadata differ. Text-identical with a diff: the lines that differ are listed in the note and are all boilerplate (trace ids, anti-bot tokens, footer social link).

## Changed or gone pages

None. No lesson or glossary citation is affected.
