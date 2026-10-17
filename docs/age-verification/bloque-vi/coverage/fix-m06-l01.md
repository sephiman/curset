# Coverage fix — m06-l01 (2026-10-17)

Lesson: `content/age-administrativo-c1/es/lessons/m06-l01.md`. Rows of `fixes.md`: 2025 A 41, 2024 A 43. Applied under
the rule change of `fix-spec.md` (requirements v1.5: no word ceiling; no cuts for length; earlier cuts an exam asked
are restored). Before: 1,498 words. After: 1,616 words (`wc -w`). Lines ≤ 120 (except the `#` title, kept exactly).
Fuentes in order of first citation (`fuentes_order.py`: in order, nothing missing, nothing uncited).

## Fixes

### 1. 2025 A 41 — the processor interprets and executes instructions (item «Procesador (CPU)»)

Old:
```
- **Procesador (CPU)**: la «unidad de procesamiento central» es el «cerebro» principal del equipo; los demás chips se
  conectan a una placa de circuito, la placa base (fuente: `ms-learn-equipos-procesador.html`).
```
New:
```
- **Procesador (CPU)**: la «unidad de procesamiento central» es el «cerebro» principal del equipo; los demás chips se
  conectan a una placa de circuito, la placa base (fuente: `ms-learn-equipos-procesador.html`). Puede interpretar una
  secuencia de instrucciones (fuente: `ms-win32-processor-cache.html`) y el sistema operativo lo usa para ejecutar
  instrucciones de programa (fuente: `ms-win-analisis-cpu.html`).
```
Source passages:
- `ms-win32-processor-cache.html` (already cited by the lesson): «La Win32_Processorclase WMI representa un dispositivo
  que puede interpretar una secuencia de instrucciones en un equipo que se ejecuta en un sistema operativo Windows.»
- `ms-win-analisis-cpu.html` (new): «En esta guía, tanto el procesador como la CPU hacen referencia a un procesador
  lógico, es decir, un dispositivo de hardware que el sistema operativo puede usar para ejecutar instrucciones de
  programa.»

«Lo que más cae», old → new (same two passages; the line now states the fact 2025 A 41 asked):
```
- La CPU es el cerebro principal del equipo (fuente: `ms-learn-equipos-procesador.html`).
```
```
- El procesador interpreta instrucciones y con él se ejecutan las de los programas (fuente:
  `ms-win32-processor-cache.html`, `ms-win-analisis-cpu.html`).
```

Sin fuente oficial: «obtiene» (fetch) as a step of the cycle. No Microsoft Spanish page found says the processor
«obtiene» or «busca» the instructions (searched `sources/otros/*` and the INCIBE glossary for «instrucci» near
«procesador/CPU», and learn/support.microsoft.com es-es). The microsoft.com page «Especificaciones y requisitos del
sistema de Windows 11» says only «Interpreta las instrucciones y le indica a cada componente qué hacer» (not saved: it
adds nothing the two cited pages lack).

### 2. 2024 A 43 — Excel is an Office application (new item, after «Aplicación de fuentes abiertas»)

New:
```
- **Aplicaciones de Office**: PowerPoint y Excel, entre otras (fuente: `ms-office-autoguardado.html`).
```
Source passage (`ms-office-autoguardado.html`, already saved for m06-l04): «Si desea deshabilitar Autoguardado de
manera predeterminada para todas sus aplicaciones de Office, como PowerPoint y Excel, tendrá que repetir estos pasos
para cada uno de esos programas.» This is also the restoration of the earlier cut «Aplicaciones de Office» (ledger,
«Cut for length»); its old page (`office-suites`) was not re-saved because a saved page states the fact.

## Restorations (earlier cuts an exam asked; writer notes `docs/age-verification/bloque-vi/m06-l01.md` «Cuts», ledger «Cut for length»)

### 3. MySQL (2020 ord. 41: MySQL is not an operating system) — appended to item «Sistema gestor de bases de datos»

Old: `… relacionales (RDBMS) (fuente: `ms-sql-server.html`).`
New:
```
  relacionales (RDBMS) (fuente: `ms-sql-server.html`). MySQL es un motor de base de datos (fuente:
  `ms-azure-mysql.html`).
```
Source passage (`ms-azure-mysql.html`, re-saved): «MySQL es un motor de base de datos popular para ejecutar aplicaciones
web y móviles a escala de Internet.»

### 4. Minería de datos (2020 extr. 43) — new item after «Sistema gestor de bases de datos»

New:
```
- **Minería de datos**: proceso de detectar información accionable de grandes conjuntos de datos; usa análisis
  matemáticos para derivar patrones y tendencias (fuente: `ms-mineria-datos.html`).
```
Source passage (`ms-mineria-datos.html`, re-saved): «La minería de datos es el proceso de detectar información
accionable de grandes conjuntos de datos. La minería de datos usa análisis matemáticos para derivar patrones y
tendencias que existen en los datos.» (The page notes the SQL Server Analysis Services feature is discontinued; the
definition is the concept, not that product.)

Not restored (no exam row in `docs/age-ofimatica-index.md`): Espacios de almacenamiento detail (RAID is listed as never
asked and keeps its item), GPU line, Software (INCIBE) line, prefijos binarios beyond GiB, NTFS 8 PB limit, Microsoft
Authenticator 30-second code, Defender scan types, router home-LAN clause. `recheck-queue.md` lists no fix-round cut for
m06-l01.

## Cuts

None. A first pass of this fix cut five clauses for length (placa base, gibi/GiB, 5 GB of OneDrive, firewall
profiles, gestor de contraseñas); all were undone under the rule change, and the lesson keeps them as before.

## New sources (fragment `SP/m06-l01/fuentes.yaml`, appended)

```yaml
- file: ms-win-analisis-cpu.html
  url: "https://learn.microsoft.com/es-es/windows-hardware/test/wpt/cpu-analysis"
  title: "Microsoft, «Análisis de CPU»"
  consultado: "2026-10-17"
  sha256: 96cbe80e4d19ea81f3d5467cc8f2bc10fdddb8872504bd0803d00dc68bf742c9
  lessons: [m06-l01]
- file: ms-azure-mysql.html
  url: "https://learn.microsoft.com/es-es/azure/mysql/flexible-server/overview"
  title: "Microsoft, «Azure Database para MySQL, servidor flexible»"
  consultado: "2026-10-17"
  sha256: 4c107f35e383a6b11882008026b108b0b09ecbde0163d6e9a8c490bba8814be3
  lessons: [m06-l01]
- file: ms-mineria-datos.html
  url: "https://learn.microsoft.com/es-es/analysis-services/data-mining/data-mining-concepts?view=asallproducts-allversions"
  title: "Microsoft, «Conceptos de minería de datos»"
  consultado: "2026-10-17"
  sha256: 68eed0604d2cd368f6a1fa9eaf48ef4377fa39b81a5a8e7935f1f0f747e9d8c2
  lessons: [m06-l01]
```
All three `lang="es-es"`; final URLs as recorded.

reused: [ms-office-autoguardado.html] (add m06-l01 to its `lessons`; it lists only m06-l04).

## Word count

1,616.
