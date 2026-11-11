# Verification — `m03-l04` (blind)

Verifier: opus, 2026-11-11. Sources: snapshot PDFs in `content/aeat-agentes-hacienda/sources/normativa/` (LGT arts. 29–48, 66–70, 104.5, 139 and DA 6.ª; RGAT arts. 2–3, 11, 17–20, 29, 59, 110–113; RD 1619/2012 arts. 2–4 and 15; RIVA arts. 40, 61, 62, 69 bis and 71.3; RIRPF art. 68; Código de Comercio art. 30; RD 1676/2009 art. 4); `normativa.yaml` (cambios_pendientes of the LIVA). Worked-example dates and weekdays recomputed with python3 `datetime`.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `d2e85b97db` | PASS | LGT (title, structure) | — | — |
| `4fd71c7fc9` | PASS | RGAT (title, structure) | — | — |
| `6fa8e3cafb` | PASS | RD 1619/2012 (title) | — | — |
| `f8f783e54f` | PASS | RIVA, RIRPF (titles) | titles end before the «y se modifica…» tails; core title exact | — |
| `884ac4ebb3` | PASS | Código de Comercio art. 30 (title) | — | — |
| `adc7f9f93b` | PASS | RD 1676/2009 art. 4 (title) | — | — |
| `e8ce6add14` | PASS | art. 29.1 LGT | — | — |
| `09985f88de` | PASS | art. 29.2 LGT | — | — |
| `1d63d7f094` | PASS | art. 29.2 LGT | — | — |
| `9c825a932f` | PASS | art. 29.2 LGT | — | — |
| `49a04a2854` | PASS | art. 29.2 LGT | — | — |
| `c74ec3f68f` | PASS | art. 29.2 LGT | — | — |
| `d8903034e3` | PASS | art. 29.2 LGT | — | — |
| `2db2a7174d` | PASS | art. 29.2 LGT | — | — |
| `8f20b0dd55` | PASS | art. 29.2 LGT | — | — |
| `69744d9037` | PASS | art. 29.2 LGT | — | — |
| `3e506238de` | PASS | art. 29.2 LGT | — | — |
| `77178b71a7` | PASS | art. 29.2 LGT | — | — |
| `2aeb7f91dd` | PASS | art. 29.3 LGT | — | — |
| `508913b3f7` | PASS | art. 70.1 LGT | — | — |
| `c6c1960ccc` | PASS | art. 70.2 LGT | — | — |
| `af7f5b3dfd` | PASS | art. 2.2 RGAT | — | — |
| `4f9e1111ab` | PASS | art. 2.2 RGAT | — | — |
| `f77256b30e` | PASS | art. 2.2 RGAT | — | — |
| `8d4c527806` | PASS | art. 2.2 RGAT | — | — |
| `b6bb96ae84` | PASS | art. 2.2 RGAT | — | — |
| `2c553cbdbc` | PASS | art. 3.1 RGAT | — | — |
| `f7d2e18db2` | PASS | art. 3.2 RGAT | — | — |
| `7b31961374` | PASS | art. 3.2 RGAT | — | — |
| `8cb4c2571b` | PASS | art. 3.2.a) RGAT | — | — |
| `ae722dbb04` | PASS | art. 3.2.a) RGAT | — | — |
| `8aa1cd4d45` | PASS | art. 3.2 RGAT | — | — |
| `e2b44df205` | PASS | art. 3.5 RGAT | — | — |
| `f496167a5a` | PASS | art. 3.5 RGAT | — | — |
| `bffef20fce` | PASS | art. 11.1 RGAT | — | — |
| `c7280977a7` | PASS | art. 11.2 RGAT | — | — |
| `61741d6ea4` | PASS | art. 11.3 RGAT | — | — |
| `0e5d3db218` | PASS | art. 11.4 RGAT | — | — |
| `b6aef783a5` | PASS | art. 11.4 RGAT | — | — |
| `aa7c538d7e` | PASS | disposición adicional sexta.1 LGT | — | — |
| `223c84e1ee` | PASS | disposición adicional sexta.1 LGT | — | — |
| `d2b30e0991` | PASS | disposición adicional sexta.1 LGT | — | — |
| `884f7e977a` | PASS | disposición adicional sexta.2 LGT | — | — |
| `32f7f6f51e` | PASS | disposición adicional sexta.3 LGT | — | — |
| `5f38f02be7` | PASS | disposición adicional sexta.3 LGT | — | — |
| `f659d3dcda` | PASS | disposición adicional sexta.4 LGT | — | — |
| `d7b9d6f72c` | PASS | disposición adicional sexta.4 LGT | — | — |
| `4894875841` | PASS | disposición adicional sexta.4 LGT | — | — |
| `80626dba06` | PASS | disposición adicional sexta.4 LGT | — | — |
| `dff239e052` | PASS | disposición adicional sexta.4 LGT | — | — |
| `495aa12a4a` | PASS | disposición adicional sexta.4 LGT | — | — |
| `37afcd2b0a` | PASS | art. 18.1 RGAT | — | — |
| `1da2c7d0e9` | PASS | art. 18.2 RGAT | — | — |
| `a596994fab` | PASS | art. 19.1 RGAT | — | — |
| `9305579cdc` | FAIL | art. 19.2 RGAT | drops the narrowing condition «que realicen o participen en operaciones de naturaleza o con trascendencia tributaria» | Los españoles que realicen o participen en operaciones de naturaleza o con trascendencia tributaria y no estén obligados a obtener el documento nacional de identidad por residir en el extranjero o por ser menores de 14 años deben obtener un número de identificación fiscal propio (art. 19.2 RGAT). |
| `298d4821bc` | PASS | art. 19.2 RGAT | — | — |
| `3c5b553175` | PASS | art. 20.1 RGAT | — | — |
| `d61fcf97bf` | FAIL | art. 20.2 RGAT | drops the narrowing condition «cuando vayan a realizar operaciones de naturaleza o con trascendencia tributaria» | Si no lo tienen, deben solicitar a la Administración tributaria, cuando vayan a realizar operaciones de naturaleza o con trascendencia tributaria, un número de nueve caracteres: una letra inicial, «que será la M», siete caracteres alfanuméricos y un carácter de verificación alfabético (art. 20.2 RGAT). |
| `25f0113c20` | PASS | art. 29.1 RGAT | — | — |
| `b7937f4e2c` | PASS | art. 29.1 RGAT | — | — |
| `b104aaecb7` | PASS | art. 29.2 RGAT | — | — |
| `b4b08d2eb0` | PASS | art. 30.1 Código de Comercio | — | — |
| `3845d8c193` | PASS | art. 62.1 RIVA | — | — |
| `ff7201f08b` | PASS | art. 62.2 RIVA | — | — |
| `2015b18d71` | PASS | art. 40.1 RIVA | — | — |
| `aff4b70126` | PASS | art. 40.1 RIVA | — | — |
| `03f02fa4c1` | PASS | art. 61.2 RIVA | — | — |
| `bf4b5062cf` | PASS | art. 62.6 RIVA | — | — |
| `99ce299610` | PASS | art. 71.3.1.º RIVA | — | — |
| `559c553ef7` | PASS | art. 69 bis.1.a) RIVA | — | — |
| `d0cdf43f5c` | PASS | art. 69 bis.1.b) RIVA | — | — |
| `ac18fae77e` | PASS | art. 69 bis.1 RIVA | — | — |
| `fcf5453faa` | PASS | art. 68.1 RIRPF | — | — |
| `8d08068520` | PASS | art. 68.2 RIRPF | — | — |
| `64bf0ebbe4` | PASS | art. 68.3 RIRPF | — | — |
| `040c8130b8` | PASS | art. 68.3 RIRPF | — | — |
| `cc256cbb74` | PASS | art. 68.3 RIRPF | — | — |
| `1c15e54fe1` | PASS | art. 68.3 RIRPF | — | — |
| `25f0a0f700` | PASS | art. 68.4 RIRPF | — | — |
| `b127b176f1` | PASS | art. 68.5 RIRPF | — | — |
| `81361677bc` | PASS | art. 68.5 RIRPF | — | — |
| `ec3f9240bf` | PASS | art. 68.5 RIRPF | — | — |
| `e570f880a2` | PASS | art. 68.5 RIRPF | — | — |
| `4d3d0d2edd` | PASS | art. 68.10 RIRPF | — | — |
| `30569df611` | PASS | art. 2.1 RD 1619/2012 | — | — |
| `f1ed3dffeb` | PASS | art. 2.1 RD 1619/2012 | — | — |
| `ee269f2ecc` | PASS | art. 3.1 RD 1619/2012 | — | — |
| `85c7b16abc` | PASS | art. 3.1 RD 1619/2012 | — | — |
| `a78e9c8fdd` | PASS | art. 3.1 RD 1619/2012 | — | — |
| `6d7c23a976` | PASS | art. 3.1 RD 1619/2012 | — | — |
| `7043d4f51b` | PASS | art. 3.1 RD 1619/2012 | — | — |
| `e13a5928af` | PASS | art. 3.3 RD 1619/2012 | — | — |
| `bf8094bb12` | PASS | art. 3.3 RD 1619/2012 | — | — |
| `f8cea8a34d` | PASS | art. 4.1 RD 1619/2012 | — | — |
| `32ab19ecb6` | PASS | art. 4.1 RD 1619/2012 | — | — |
| `97bb22ac20` | PASS | art. 4.1 RD 1619/2012 | — | — |
| `f3d24e4ba1` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `7147179a36` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `4a6b87dd24` | FAIL | art. 4.2.a) RD 1619/2012 | drops the narrowing sentence of the definition: «No se reputarán ventas al por menor las que tengan por objeto bienes que, por sus características objetivas, envasado, presentación o estado de conservación, sean principalmente de utilización empresarial o profesional» | Son ventas al por menor las entregas de bienes muebles corporales o semovientes en las que el destinatario no actúe como empresario o profesional, sino como consumidor final. No son ventas al por menor las que tienen por objeto bienes que, por sus características objetivas, envasado, presentación o estado de conservación, sean principalmente de utilización empresarial o profesional. |
| `53dc77e19e` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `781e0c6f79` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `44ff9c7900` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `3cc8fb345e` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `1547915be2` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `ff54e93011` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `c7e1645742` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `0197468541` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `bc0e8f60ac` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `7176ba807f` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `aacf85a661` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `5f70c8521d` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `238acdeead` | PASS | art. 4.2 RD 1619/2012 | — | — |
| `87a5233398` | PASS | art. 4.3 RD 1619/2012 | — | — |
| `e7d09f84bc` | PASS | art. 4.4 RD 1619/2012 | — | — |
| `12278f82a8` | PASS | art. 4.4 RD 1619/2012 | — | — |
| `dcc9672115` | PASS | art. 4.4 RD 1619/2012 | — | — |
| `6d6b4f046e` | PASS | art. 4.4 RD 1619/2012 | — | — |
| `ba05eeefcc` | PASS | art. 4.4 RD 1619/2012 | — | — |
| `7d6b2ef235` | PASS | art. 15.1–2 RD 1619/2012 | — | — |
| `90a6296a0f` | PASS | art. 15.3 RD 1619/2012 | — | — |
| `19c270eb08` | PASS | art. 30.1 LGT | — | — |
| `369b2e295c` | PASS | art. 30.2 LGT | — | — |
| `93035d25ff` | PASS | art. 31.1 LGT | — | — |
| `61037af27a` | PASS | art. 31.2 LGT | — | — |
| `7e809d9b8b` | PASS | art. 32.2 LGT | — | — |
| `0f45638753` | PASS | art. 33.2 LGT | — | — |
| `123b541f84` | PASS | art. 34.1 LGT | — | — |
| `709808efd7` | PASS | art. 34.1 LGT | — | — |
| `491450d4bb` | PASS | art. 34.1 LGT | — | — |
| `4aa05e43d3` | PASS | art. 34.1 LGT | — | — |
| `f4fc3f29a9` | PASS | art. 34.1 LGT | — | — |
| `1eccd5d265` | PASS | art. 34.1 LGT | — | — |
| `42ed3bbec5` | PASS | art. 34.1 LGT | — | — |
| `7f4dec2f9d` | PASS | art. 34.1 LGT | — | — |
| `df467d36e7` | PASS | art. 34.1 LGT | — | — |
| `e712d3609e` | PASS | art. 34.1 LGT | — | — |
| `d12972a055` | PASS | art. 34.1 LGT | — | — |
| `c3c7f93fb3` | PASS | art. 34.1 LGT | — | — |
| `c20b047f28` | PASS | art. 34.1 LGT | — | — |
| `f114333c6a` | PASS | art. 34.1 LGT | — | — |
| `7f08004058` | PASS | art. 34.1 LGT | — | — |
| `0597ec9ca3` | PASS | art. 34.1 LGT | — | — |
| `1b1cc6b362` | PASS | art. 34.1 LGT | — | — |
| `ed79cabfc3` | PASS | art. 34.1 LGT | — | — |
| `2a52487c41` | PASS | art. 34.1 LGT | — | — |
| `22ad049312` | PASS | art. 34.1 LGT | — | — |
| `bc86d785ac` | PASS | art. 34.1 LGT | — | — |
| `e1e3ec028d` | PASS | art. 34.2 LGT | — | — |
| `ed494ab630` | PASS | art. 4.1 RD 1676/2009 | — | — |
| `fdc38f9f86` | PASS | art. 4.1.a) y b) RD 1676/2009 | — | — |
| `7ad345476f` | PASS | art. 35.1 LGT | — | — |
| `7f7bd99aa9` | PASS | art. 35.2 LGT | — | — |
| `9ee35c1c8b` | PASS | art. 35.2 LGT | — | — |
| `7288b4124f` | PASS | art. 35.2 LGT | — | — |
| `608bf86d6d` | PASS | art. 35.2 LGT | — | — |
| `b9cb4354b0` | PASS | art. 35.2 LGT | — | — |
| `49a2857666` | PASS | art. 35.2 LGT | — | — |
| `edcd897dfa` | PASS | art. 35.2 LGT | — | — |
| `427ecaf7c5` | PASS | art. 35.2 LGT | — | — |
| `36d4797756` | PASS | art. 35.2 LGT | — | — |
| `0e137a56e0` | PASS | art. 35.2 LGT | — | — |
| `9638ba0f22` | PASS | art. 35.2 LGT | — | — |
| `90d09bfb87` | PASS | art. 35.2 LGT | — | — |
| `32065152e4` | PASS | art. 35.3 LGT | — | — |
| `f7c315ba4a` | PASS | art. 35.4 LGT | — | — |
| `3ee380ea68` | PASS | art. 35.5 LGT | — | — |
| `41f2acc965` | FAIL | art. 35.6 LGT | fact right; opener «También lo son» is the blacklisted «También es…» split (same ruling as m03-l02) | Aquellos a los que se pueda imponer obligaciones tributarias conforme a la normativa sobre asistencia mutua tienen igualmente la consideración de obligados tributarios (art. 35.6 LGT). |
| `1f661dc6a3` | PASS | art. 35.7 LGT | — | — |
| `ed65b8a4a4` | PASS | art. 35.7 LGT | — | — |
| `f9785de067` | PASS | art. 35.7 LGT | — | — |
| `babc42019a` | PASS | art. 36.1 LGT | — | — |
| `1b85ef4437` | PASS | art. 36.1 LGT | — | — |
| `67aeb06831` | PASS | art. 36.2 LGT | — | — |
| `dc0c8beba3` | PASS | art. 36.3 LGT | — | — |
| `791167285d` | PASS | art. 36.3 LGT | — | — |
| `b4131ec65e` | PASS | art. 37.1 LGT | — | — |
| `16e8d1eb8c` | PASS | art. 37.2 LGT | — | — |
| `afd19eca8f` | PASS | art. 37.3 LGT | — | — |
| `16bdc2c647` | PASS | art. 38.1 LGT | — | — |
| `b7b0c38e1c` | PASS | art. 38.2 LGT | — | — |
| `d07920d5ab` | PASS | art. 38.2 LGT | — | — |
| `f81cf10663` | PASS | art. 38.3 LGT | — | — |
| `2ddabf392f` | PASS | art. 38.4 LGT | — | — |
| `6771a2500d` | PASS | art. 39.1 LGT | — | — |
| `6a26f9d9da` | PASS | art. 39.1 LGT | — | — |
| `3ec21cd586` | PASS | art. 39.1 LGT | — | — |
| `55ca2ee307` | PASS | art. 39.1 LGT | — | — |
| `eb5490ab98` | PASS | art. 39.2 LGT | — | — |
| `083c390b31` | PASS | art. 39.3 LGT | — | — |
| `bbc7ae3c98` | PASS | art. 39.3 LGT | — | — |
| `f43025f203` | PASS | art. 40.1 LGT | — | — |
| `16ef7cef1d` | PASS | art. 40.1 LGT | — | — |
| `4fbfaca081` | PASS | art. 40.3 LGT | — | — |
| `ccb49e4614` | PASS | art. 40.4 LGT | — | — |
| `4d88bc8d1b` | PASS | art. 40.5 LGT | — | — |
| `3acbdb8813` | PASS | art. 41.1 LGT | — | — |
| `68d8bc514a` | PASS | art. 41.2 LGT | — | — |
| `1c202ec879` | PASS | art. 41.3 LGT | — | — |
| `c010970c1f` | PASS | art. 41.3 LGT | — | — |
| `4b0ff8af3b` | PASS | art. 41.4 LGT | — | — |
| `f9e68a7cf9` | PASS | art. 41.5 LGT | — | — |
| `2f2a5f4463` | PASS | art. 41.5 LGT | — | — |
| `ab0006e070` | PASS | art. 41.6 LGT | — | — |
| `f1761020a4` | PASS | art. 42.1 LGT | — | — |
| `c6edf7496a` | PASS | art. 42.1 LGT | — | — |
| `b614f8b82f` | PASS | art. 42.1 LGT | — | — |
| `ad98018e4c` | PASS | art. 42.1 LGT | — | — |
| `851126fe3b` | PASS | art. 42.1 LGT | — | — |
| `1490a864d1` | PASS | art. 42.1 LGT | — | — |
| `ddee8ab8ba` | PASS | art. 42.1 LGT | — | — |
| `05b9bde72b` | PASS | art. 42.1 LGT | — | — |
| `5b9b5c5e60` | PASS | art. 42.2 LGT | — | — |
| `3f2369f765` | PASS | art. 42.2 LGT | — | — |
| `8d4f9d5e57` | PASS | art. 42.2 LGT | — | — |
| `efc4c4ca3c` | PASS | art. 42.2 LGT | — | — |
| `3ba648deb0` | PASS | art. 42.2 LGT | — | — |
| `bd97c3fcf3` | PASS | art. 42.3 LGT | — | — |
| `7d8083efa2` | PASS | art. 42.4 LGT | — | — |
| `22108fd6ff` | PASS | art. 43.1 LGT | — | — |
| `1d33873811` | PASS | art. 43.1 LGT | — | — |
| `217228196d` | PASS | art. 43.1 LGT | — | — |
| `c2a267ed8d` | PASS | art. 43.1 LGT | — | — |
| `dd9db55ddb` | PASS | art. 43.1 LGT | — | — |
| `37e65e48a2` | PASS | art. 43.1 LGT | — | — |
| `a4c823f29c` | PASS | art. 43.1 LGT | — | — |
| `28bd7b4140` | PASS | art. 43.1 LGT | — | — |
| `28702839ea` | PASS | art. 43.1 LGT | — | — |
| `5d59a3fc54` | PASS | art. 43.1 LGT | — | — |
| `aac5123729` | PASS | art. 43.1 LGT | — | — |
| `a1bd8c6401` | PASS | art. 43.1 LGT | — | — |
| `f1a6d0a073` | PASS | art. 43.1 LGT | — | — |
| `7e7b67ee5c` | PASS | art. 43.1 LGT | — | — |
| `0e701bc976` | PASS | art. 43.1 LGT | — | — |
| `29323828b6` | PASS | art. 43.1 LGT | — | — |
| `0ab42ad671` | PASS | art. 43.2 LGT | — | — |
| `dab04ea54f` | PASS | art. 43.2 LGT | — | — |
| `eccc48d695` | PASS | art. 43.2 LGT | — | — |
| `20276d9bee` | PASS | art. 43.3 LGT | — | — |
| `2ce5c43af3` | PASS | art. 43.4 LGT | — | — |
| `725ab0d143` | PASS | art. 44 LGT | — | — |
| `d84c39c5b8` | PASS | art. 44 LGT | — | — |
| `df61b98de5` | PASS | art. 45.1 LGT | — | — |
| `dd6876b99e` | PASS | art. 45.2 LGT | — | — |
| `311cd5e006` | PASS | art. 45.3 LGT | — | — |
| `1c1152aa16` | PASS | art. 45.3 LGT | — | — |
| `ecf558d3e9` | PASS | art. 110.1 RGAT | — | — |
| `ed5744787f` | PASS | art. 110.3 RGAT | — | — |
| `d5ea4d008d` | PASS | art. 110.4 RGAT | — | — |
| `e8ebe6eda4` | PASS | art. 46.1 LGT | — | — |
| `45138891d7` | PASS | art. 46.2 LGT | — | — |
| `352841fc67` | PASS | art. 46.2 LGT | — | — |
| `baa3377e08` | PASS | art. 46.3 LGT | — | — |
| `964085ba87` | PASS | art. 46.6 LGT | — | — |
| `598bd2adb2` | PASS | art. 46.7 LGT | — | — |
| `f0d1336113` | PASS | art. 111.1 RGAT | — | — |
| `fdf7d2ce04` | PASS | art. 111.1 RGAT | — | — |
| `02ca1ff25f` | PASS | art. 111.1 RGAT | — | — |
| `5ffb7e0e75` | PASS | art. 111.2 RGAT | — | — |
| `ee896e425e` | PASS | art. 111.2 RGAT | — | — |
| `bfc3ef2cf1` | PASS | art. 111.2 RGAT | — | — |
| `18578f0a54` | PASS | art. 111.2 RGAT | — | — |
| `6c516fdbb6` | PASS | art. 111.2 RGAT | — | — |
| `cad40c4d7a` | PASS | art. 111.2 RGAT | — | — |
| `7d3915f43c` | PASS | art. 111.5 RGAT | — | — |
| `24f98067e6` | PASS | art. 111.5 RGAT | — | — |
| `69bef3fd28` | PASS | art. 111.6 RGAT | — | — |
| `303419bdb1` | PASS | art. 112.1 RGAT | — | — |
| `dccbc1428d` | PASS | art. 112.1 RGAT | — | — |
| `92625c2242` | PASS | art. 112.4 RGAT | — | — |
| `34d1126864` | PASS | art. 112.5 RGAT | — | — |
| `1b9f76a2b8` | PASS | art. 47 LGT | — | — |
| `392ee2babb` | PASS | art. 48.1 LGT | — | — |
| `7ab0e84604` | PASS | art. 48.2 LGT | — | — |
| `bb0a812fba` | PASS | art. 48.2 LGT | — | — |
| `85584b54d6` | PASS | art. 48.2 LGT | — | — |
| `8f67ac421d` | PASS | art. 48.2 LGT | — | — |
| `ec4fabbae9` | PASS | art. 48.2 LGT | — | — |
| `f8c54c70b4` | PASS | art. 48.2 LGT | — | — |
| `7b0e254351` | PASS | art. 48.2 LGT | — | — |
| `44fecf606e` | PASS | art. 48.2 LGT | — | — |
| `bc5c30c523` | PASS | art. 48.2 LGT | — | — |
| `ac4578e7f2` | PASS | art. 48.2 LGT | — | — |
| `85f24ac1ba` | PASS | art. 48.2 LGT | — | — |
| `1c9580710b` | PASS | art. 113 RGAT | — | — |
| `5eaafa89fe` | PASS | art. 113 RGAT | — | — |
| `ab8e81aaa6` | PASS | art. 48.3 LGT | — | — |
| `24e966c38c` | PASS | art. 48.3 LGT | — | — |
| `9b93fadda9` | PASS | art. 48.4 LGT | — | — |
| `de10e19719` | PASS | art. 17.1 RGAT | — | — |
| `bf4d05ec07` | PASS | art. 17.2 RGAT | — | — |
| `f59ad920f4` | PASS | art. 17.3 RGAT | — | — |
| `33a61dcb05` | PASS | art. 59.2 RGAT | — | — |
| `21a89d93e0` | PASS | art. 59.2 RGAT | — | — |
| `cfd6f959d4` | PASS | art. 66 LGT | — | — |
| `10e30263e3` | PASS | art. 66 LGT | — | — |
| `12a25a66ea` | PASS | art. 66 LGT | — | — |
| `5ca5673fa2` | PASS | art. 66 LGT | — | — |
| `586d62f55e` | PASS | art. 66 LGT | — | — |
| `79a7849097` | PASS | art. 66 bis.1 LGT | — | — |
| `0a06ecc92b` | PASS | art. 66 bis.2 LGT | — | — |
| `55769c56f9` | PASS | art. 66 bis.2 LGT | — | — |
| `1e155f1fb3` | PASS | art. 67.1 LGT | — | — |
| `ec06e35cd8` | PASS | art. 67.1 LGT | — | — |
| `680ec2f1bd` | PASS | art. 67.1 LGT | — | — |
| `485da72867` | PASS | art. 67.1 LGT | — | — |
| `74bc70a3f9` | PASS | art. 67.1 LGT | — | — |
| `05926a6e61` | PASS | art. 67.1 LGT | — | — |
| `4393c7bbbb` | PASS | art. 67.1 LGT | — | — |
| `ed95f8abbc` | PASS | art. 67.2 LGT | — | — |
| `0173736936` | PASS | art. 67.2 LGT | — | — |
| `7fc62197c3` | PASS | art. 67.2 LGT | — | — |
| `3986fe7650` | PASS | art. 68.1 LGT | — | — |
| `cbc83b4e47` | PASS | art. 68.1 LGT | — | — |
| `5b99597ac5` | PASS | art. 68.1 LGT | — | — |
| `d9e869cee7` | PASS | art. 68.1 LGT | — | — |
| `95df8b6393` | PASS | art. 68.2 LGT | — | — |
| `410c51f496` | PASS | art. 68.2 LGT | — | — |
| `4bca425406` | PASS | art. 68.2 LGT | — | — |
| `6366ca8495` | PASS | art. 68.2 LGT | — | — |
| `fcb06d2052` | PASS | art. 68.3 LGT | — | — |
| `4a07ffaaa8` | PASS | art. 68.4 LGT | — | — |
| `8869b193bb` | PASS | art. 68.5 LGT | — | — |
| `2524640dbf` | PASS | art. 68.6 LGT | — | — |
| `8fccdff005` | PASS | art. 68.7 LGT | — | — |
| `dbfb016abf` | PASS | art. 68.7 LGT | — | — |
| `a4b1ebb494` | PASS | art. 68.7 LGT | — | — |
| `8fd059389d` | FAIL | art. 68.7 LGT, último párrafo | the article excludes the whole apartado 7 («Lo dispuesto en este apartado no será aplicable…»), not only the contencioso-administrativo rule | Lo dispuesto en el apartado 7 no se aplica al plazo de prescripción del derecho de la Administración tributaria para exigir el pago cuando no se hubiera acordado la suspensión en vía contencioso-administrativa (art. 68.7 LGT). |
| `811716668b` | PASS | art. 68.8 LGT | — | — |
| `f7d938a40c` | PASS | art. 68.8 LGT | — | — |
| `bde19cba43` | PASS | art. 68.8 LGT | — | — |
| `8b7092556a` | PASS | art. 68.8 LGT | — | — |
| `8cb6456cc6` | PASS | art. 68.9 LGT | — | — |
| `b9a8f658e9` | PASS | art. 68.9 LGT | — | — |
| `4e2403fbdb` | PASS | art. 69.1 LGT | — | — |
| `b8cc4d1165` | PASS | art. 69.2 LGT | — | — |
| `a70eb8b8d4` | PASS | art. 69.3 LGT | — | — |
| `0c930c2da5` | PASS | art. 70.3 LGT | — | — |
| `4fe6b72ffa` | PASS | example data | — | — |
| `c1d127cae2` | PASS | example data | 2022-06-30 is a Thursday (python3) | — |
| `6484ff31e8` | FAIL | example data; art. 104.5 LGT | 2025-03-14 is a Friday (python3); the facts never say the comprobación limitada ended without caducidad, which the result depends on (art. 104.5 LGT: actuaciones of a caducado procedure do not interrupt) | El viernes 14 de marzo de 2025 la Administración tributaria le notifica el inicio de un procedimiento de comprobación limitada de esa autoliquidación, que termina sin caducidad. |
| `be5a9dd405` | PASS | example data | 2026-09-15 is a Tuesday (python3) | — |
| `1fb51945e3` | PASS | art. 66.a) LGT | — | — |
| `62ac826267` | PASS | art. 67.1 LGT | day after 30-06-2022 = 01-07-2022 (Friday) | — |
| `c93b36432b` | PASS | arts. 66.a) y 67.1 LGT | four years from 01-07-2022 end 30-06-2026; 15-09-2026 is later | — |
| `0859456029` | PASS | art. 68.1.a) LGT | — | — |
| `483c7c067c` | FAIL | arts. 68.1.a) and 104.5 LGT | true only if the procedure does not caducar: «las actuaciones realizadas en los procedimientos caducados no interrumpirán el plazo de prescripción» (art. 104.5 LGT); had it caducado, the right prescribed on 30-06-2026 and the result flips. Add 104.5 to the LGT «Normativa» line (see cd2480a1f5) | Interrumpe el plazo, porque el procedimiento no caduca: las actuaciones realizadas en los procedimientos caducados no interrumpen el plazo de prescripción (arts. 68.1.a) y 104.5 LGT). |
| `cc8ae5c9c9` | PASS | arts. 68.6 y 68.7 LGT | — | — |
| `edeefff7f1` | PASS | arts. 68.6 y 68.7 LGT | — | — |
| `910b43e676` | PASS | arts. 66.a) y 68.6 LGT | 14-03-2025 + 4 years = 14-03-2029 | — |
| `7dab4befd4` | PASS | arts. 66.a) y 68.6 LGT | 14-03-2025 → 14-09-2026 = 1 year 6 months | — |
| `9f9ce8e14b` | PASS | arts. 66.a), 67.1, 68.1.a) and 68.6 LGT | correct once the no-caducidad fact is stated (6484ff31e8, 483c7c067c) | — |
| `74401afff5` | PASS | art. 68.8 LGT | — | — |
| `a64d148f39` | PASS | art. 68.3 LGT, art. 68.7 LGT | — | — |
| `39a12aecd1` | PASS | arts. 66.c) y 67.1 LGT | — | — |
| `8d18510eef` | PASS | art. 67.2 LGT | — | — |
| `069a1d68c1` | PASS | art. 66 bis.2 LGT | — | — |
| `1a4e0b0eca` | PASS | art. 69.2–3 LGT | — | — |
| `d17e26772b` | PASS | art. 4.1–2 RD 1619/2012 | — | — |
| `9b6db9e0ef` | PASS | art. 112.1 RGAT, art. 46.7 LGT | — | — |
| `0b75391eaa` | PASS | art. 43.1.h) LGT | — | — |
| `ec6866af6c` | PASS | arts. 19.2 y 20.2 RGAT | — | — |
| `cd2480a1f5` | FAIL | LGT (Normativa line) | prose names art. 26 LGT (lines 130, 137) and art. 66 bis.3 (line 336, «artículo 66 bis, apartados 2 y 3»), neither listed; 104.5 added for the step-4 fix | LGT (Ley 58/2003): arts. 26, 29.1–3, 30.1–2, 31.1–2, 32.2, 33.2, 34.1–2, 35.1–7, 36.1–3, 37.1–3, 38.1–4, 39.1–3, 40.1, 40.3–5, 41.1–6, 42.1–4, 43.1–4, 44, 45.1–3, 46.1–3, 46.6–7, 47, 48.1–4, 66, 66 bis.1–3, 67.1–2, 68.1–9, 69.1–3, 70.1–3, 79, 104.5, 115, 175, 175.2, 176 y disposición adicional sexta.1–4. |
| `a82a866e7e` | PASS | RGAT (RD 1065/2007) | — | — |
| `26f51a82df` | FAIL | RD 1619/2012 (Normativa line) | prose names art. 2.2 (line 86, «salvo en los supuestos del artículo 2.2») and art. 2.3.b) b') (line 122); only 2.1 listed | RD 1619/2012 (Reglamento de facturación): arts. 2.1–3, 3.1, 3.3, 4.1–4, 5, 6, 7, 15.1–3 y 16.1. |
| `48f21372bd` | PASS | RIVA (RD 1624/1992) | — | — |
| `0213e127b8` | PASS | RIRPF (RD 439/2007) | — | — |
| `59a593b0c5` | PASS | Código de Comercio | — | — |
| `c4c3c74a55` | PASS | RD 1676/2009 (Consejo para la Defensa del Contribuyente) | — | — |
| `dfed5c1192` | FAIL | LIVA (Normativa line); normativa.yaml cambios_pendientes | cites art. 20.uno.23.º, whose letter e´) the RDL 29/2026 changes with effects from 01-12-2026 (cambios_pendientes); the cambio-pendiente note is missing (form as in m03-l18) | LIVA (Ley 37/1992): arts. 20, 20.uno.23.º, 25, 25.uno y dos, 26.tres, 68.Tres.a), 80, 121, 123.uno.B).3.º y 129.uno. Cambio pendiente por el Real Decreto-ley 29/2026, de 6 de octubre, sin convalidar, con efectos desde el 01-12-2026 (art. 20.Uno.23.º e´)). |

PASS 359 · FAIL 10
