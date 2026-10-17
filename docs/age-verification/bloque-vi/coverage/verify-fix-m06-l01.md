# Blind verification of the coverage fix — m06-l01 (2026-10-17)

Spec: `fix-spec.md` («Verifier» and «Rule change»: no word ceiling; restorations allowed). Inputs: `fix-m06-l01.md`
(writer's claims), `m06-l01.md` (coverage report), `fixes.md` rows 2025 A 41 and 2024 A 43. Lesson as it now stands:
`content/age-administrativo-c1/es/lessons/m06-l01.md` (compared with `git diff HEAD`). Pages read with `pagetext.py`.
Exam texts read from `sources/examenes-oficiales/` (`pdftotext -layout`).

## Changes

| # | Change | Check | PASS/FAIL | Reason | Replacement |
|---|---|---|---|---|---|
| 1 | Procesador (CPU): «Puede interpretar una secuencia de instrucciones» | literal on page | PASS | `ms-win32-processor-cache.html`: «representa un dispositivo que puede interpretar una secuencia de instrucciones» | — |
| 1 | Procesador (CPU): «el sistema operativo lo usa para ejecutar instrucciones de programa» | literal on page | PASS | `ms-win-analisis-cpu.html`: «un dispositivo de hardware que el sistema operativo puede usar para ejecutar instrucciones de programa» | — |
| 1 | 2025 A 41 now stated | fact asked | PASS | Key a: «búsqueda, interpretación y ejecución de instrucciones»; the item now gives interpretation and execution, which no other option has. «Búsqueda/obtiene» is recorded as sin fuente oficial (no Spanish Microsoft page found by the writer; not re-searched) | — |
| 1b | LQMC «El procesador interpreta instrucciones y con él se ejecutan las de los programas» | literal; replaces «La CPU es el cerebro principal» | PASS | Same two passages; the old line's fact stays in the item; not a copy of the option text; LQMC still ten lines | — |
| 2 | New item «Aplicaciones de Office: PowerPoint y Excel, entre otras» | literal on page | PASS | `ms-office-autoguardado.html`: «todas sus aplicaciones de Office, como PowerPoint y Excel» | — |
| 2 | 2024 A 43 now stated | fact asked | PASS | Options Windows / Excel / MySQL / Chrome: Excel is now named as an Office application; MySQL is now a database engine (change 3), Windows an OS | — |
| 3 | Restoration: «MySQL es un motor de base de datos» | literal; exam row | PASS | `ms-azure-mysql.html`: «MySQL es un motor de base de datos popular…». Exam row: 2020 ord. 41 (index line 320, `vigente`; option c MySQL as «NO corresponde a un sistema operativo») | — |
| 4 | Restoration: item «Minería de datos» | literal; exam row | PASS | `ms-mineria-datos.html`: «La minería de datos es el proceso de detectar información accionable de grandes conjuntos de datos. La minería de datos usa análisis matemáticos para derivar patrones y tendencias…». Exam row: 2020 extr. 43 (index line 327, `vigente`, key c «Descubrir patrones…») | — |
| 5 | Restorations not made (Espacios de almacenamiento, GPU line, Software INCIBE, prefijos beyond GiB, NTFS 8 PB, Authenticator, Defender scan types, router home-LAN) | rule change | PASS | No index row asks any of them as cut (RAID listed as never asked; tarjeta gráfica 2024 X 50, router 2025 X 43 and the TB/PB/EB comparison stay covered by existing items). `recheck-queue.md` has no fix-round cut for m06-l01 | — |
| 6 | First-pass cuts undone | no cut remains | PASS | `git diff HEAD` shows only additions and the moved Fuentes line; placa base, GiB, 5 GB OneDrive, firewall profiles and gestor de contraseñas are in place | — |

## New sources

| File | sha256 vs fix notes | Official, Spanish | Final URL | PASS/FAIL |
|---|---|---|---|---|
| `ms-win-analisis-cpu.html` | match (`96cbe80e…`) | learn.microsoft.com, `lang="es-es"` | canonical = recorded URL | PASS |
| `ms-azure-mysql.html` | match (`4c107f35…`) | learn.microsoft.com, `lang="es-es"` | canonical = recorded URL | PASS |
| `ms-mineria-datos.html` | match (`68eed060…`) | learn.microsoft.com, `lang="es-es"` | canonical = recorded URL | PASS |
| `ms-office-autoguardado.html` (reused) | matches its `fuentes.yaml` entry (`becfaa16…`) | support.microsoft.com | as indexed | PASS |

None of the three new files is in `fuentes.yaml` yet (expected; coordinator merges). The coordinator also adds m06-l01
to the `lessons` of `ms-office-autoguardado.html`. Re-download check: done on `ms-win-registro.html` (byte-identical) and
`ms-win-idioma.html` (same extracted text), both m06-l02 pages; see `verify-fix-m06-l02.md`.

## Covered rows re-checked against the lesson as it stands

All 20 rows marked `covered` in `m06-l01.md` still have their quoted text in the lesson (antivirus, RAM, múltiplos,
escritorio virtual, router, Mac OS, certificado digital, lápiz óptico, gusano y troyano, memoria física, SaaS, tarjeta
gráfica, CAPTCHA, phishing, caché, Plug and Play, BIOS/UEFI, bit, NTFS/exFAT/UDF/FAT32, NTFS predeterminado). The
partial row (2025 A 41) and the miss (2024 A 43) are now covered. Nothing asked 2022–2025 was cut.

## Form

| Check | PASS/FAIL | Note |
|---|---|---|
| Words | PASS | `wc -w` 1,616, as claimed; no ceiling under the rule change |
| Lines ≤ 120 | PASS | only line 1 (`#` title, unchanged from HEAD) is longer |
| Fuentes | PASS | `fuentes_order.py`: nothing missing, nothing uncited, in order; `ms-win32-processor-cache.html` moved up to its new first citation; titles match the pages' `<title>` |
| List-shape hygiene | PASS | no `-`, `*` or `1.` after sentence punctuation mid-line |
| Item shape | PASS | Procesador item is now four lines; m06-l02 already has four-line items accepted in earlier passes |
| Voice | PASS | no fillers, triads, rhetorical questions or closers; no invented terms |
| LQMC | PASS | exactly ten lines |

## Counts

- Checks: 10 change rows, 4 source rows, 1 coverage re-check, 7 form rows = 22.
- PASS: 22. FAIL: 0.
