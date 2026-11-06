# Verification — `m02-l06`, re-check 1

Verifier: blind verifier (opus), 2026-11-06. Did not write the lesson.

Files read: `docs/age-verification/c2/bloque-ii/pending/m02-l06.md`, `content/age-auxiliar-c2/es/lessons/m02-l06.md`,
`content/age-auxiliar-c2/sources/otros/fuentes.yaml`, and in `content/age-auxiliar-c2/sources/otros/` (HTML stripped to
text): `ms-win-wifi.html` (Windows 11 tab), `ms-win-iconos-escritorio.html` (one tab, «Se aplica a Windows 11 Windows 10»),
`ms-copilot-introduccion.html` (sha256 `0c23b4a1…69153f3`, matches `fuentes.yaml`; differs from C1's copy `c41e9c64…`).

Result: 3 PASS, 1 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `137dd795e2` | PASS | ms-win-wifi.html; Windows 11, «Encontrar la contraseña de la red Wi-Fi» | Windows 11 tab, note: «También puedes ver la contraseña de las redes guardadas en la página Administrar redes conocidas seleccionando cualquier red y, a continuación, Mostrar junto a la contraseña de la red Wi-Fi»; same tab gives the path «Red & Internet>Wi-Fi>Administrar redes conocidas» | — |
| `c88396a2f7` | PASS | ms-win-iconos-escritorio.html; «Personalizar los iconos del escritorio predeterminados» | page lists «Este equipo», «Papelera de reciclaje», «Red», «User's Files: acceso directo a sus carpetas personales» («Entre los iconos esenciales que puede personalizar se incluyen»; step 3 «Selecciona los iconos que desearías tener en el escritorio»); «entre» marks the list as selective | — |
| `0237e09cdb` | PASS | ms-win-iconos-escritorio.html; «Personalizar los iconos del escritorio predeterminados» | step 2 «Selecciona Configuración del icono de escritorio», step 3 «Selecciona los iconos…»; the four icons as listed on the page | — |
| `8da5a6a797` | FAIL | fuentes.yaml; ms-copilot-introduccion.html | title now matches the page heading (`<h1>` «Introducción a Microsoft Copilot») and host learn.microsoft.com is right, but the saved file is the fresh copy (sha256 `0c23b4a1…`, origen «descarga nueva», consultado «2026-11-05» in `fuentes.yaml`); «consultado el 17-10-2026» is C1's date for its older copy | `ms-copilot-introduccion.html`: Microsoft, «Introducción a Microsoft Copilot» (learn.microsoft.com, consultado el 05-11-2026). |
