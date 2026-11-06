# Formats restore — blind verification (2026-11-06)

Source: `content/age-administrativo-c1/sources/otros/ms-office-open-xml.html`, h1 «Formatos Open XML y extensiones de
nombres de archivo» (canonical support.microsoft.com/es-es/office/vba/open-xml-formats-and-file-name-extensions).
«Se aplica a» lists «Word para Microsoft 365» (no «para Mac» suffix, so the Windows desktop app), plus Word
2016–2021: **the page applies.** Text extracted by my own HTML-to-text pass; every saved page in `sources/otros/` was
extracted and grepped for the distractors (JavaScript, Python, .odt, OpenDocument, 97-2003, .dot*, .doc*).
Anchors: `_anchor('m06-l04', citation)` resolves all three to `fuente-ms-office-open-xml-html`. Each citation label
is one sentence inside a single block of the page (q243 and q247: the `<p>` «De forma predeterminada, los documentos…»;
q246: the `<li>` «Detección más fácil de documentos que contienen macros»); none spans two paragraphs.

| id/place | 1 | 2 | 3 | 4 | 5 | verdict | reason |
|---|---|---|---|---|---|---|---|
| m06-l04-q243 | PASS | PASS | PASS | PASS | PASS | PASS | Key: «La "x" indica un archivo XML que no tiene macros, mientras que la "m" indica que sí contiene macros». Reversed option: same sentence. «Word 97-2003»: «La extensión de plantilla usada en versiones anteriores sigue existiendo, pero ahora incluye una "x" o una "m" al final» (and `ms-office-formatos-archivo.html`: «.dot Plantilla de Word 97-2003»). «Documentos / solo estilos»: Word table «Plantilla .dotx», «Plantilla habilitada para macros .dotm», «Documento .docx». |
| m06-l04-q246 | PASS | FAIL | PASS | FAIL | PASS | FAIL | No saved page has a sentence that rules out the «JavaScript» and «Python» options: the page says only «no puede contener macros de Visual Basic para Aplicaciones (VBA) ni macros XLM» for "x" files, and the explanation rejects the two as «el lenguaje que la página nombra», which rests on the page's silence. |
| m06-l04-q247 | PASS | PASS | PASS | PASS | PASS | PASS | Key and .doc: «el archivo usa ahora la extensión de nombre de archivo .docx de forma predeterminada, en lugar de la extensión de nombre de archivo .doc». .docm: «Files que se guardan con el sufijo "x" predeterminado…» and the row «Documento habilitado para macros .docm». .odt: the default is .docx (same sentence), and the tables list «todas las extensiones de nombres de archivo predeterminadas de Word». |
| m06-l04.md, «Formatos» row (l. 71–73) | — | — | — | — | — | PASS | Every fact is printed on the page: the Word table (Documento .docx, Documento habilitado para macros .docm, Plantilla .dotx, Plantilla habilitada para macros .dotm), «.docx de forma predeterminada, en lugar de … .doc», and «Solo los archivos cuya extensión de nombre termina con una "m" … pueden contener macros». The voice is fine and nothing is coined. |
| m06-l04.md, «Lo que más cae» .dotm/.dotx (l. 118) | — | — | — | — | — | PASS | «Plantilla habilitada para macros .dotm»; .dotx «Plantilla» + «La "x" indica un archivo XML que no tiene macros». |
| m06-l04.md, Fuentes entry (l. 163–164) | — | — | — | — | — | PASS | The title matches the page's h1 exactly; support.microsoft.com and 06-11-2026 match the save date (`fuentes.yaml` consultado 2026-11-06). |

## Notes (no verdict change)

- q243 check 5: conv2022 P1 52 asks what .dotm «indica», with options for a template with macros, a template without
  macros and a Word 97-2003 file. q243 contrasts .dotx with .dotm in paired statements. The stem form and the options
  are new and the angle differs, so it passes. The «Word 97-2003» idea does recur in the option about .dotx.
- q243 explanation: «las dos son plantillas, así que ninguna se limita a guardar estilos» is an inference. The page
  supports it only through the table labels and the "m" = macros sentence.
- The labels are quoted sentences, not the section heading that `bloque-vi/spec.md` describes. Each lies in one paragraph, as
  the prompt asks.
- Another saved page, `ms-office-formatos-archivo.html` (Microsoft Learn, Word 2007–2021), agrees with every fact
  above, and its .docm row says «Almacena código de macros Visual Basic para Aplicaciones (VBA)». It still does not
  rule out JavaScript or Python, so q246 stays FAIL.

Counts: 3 questions, 2 PASS, 1 FAIL (q246, check 2/4). Lesson: 3 places, 3 PASS.
