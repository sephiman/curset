# Verification re-check 1 — `m03-l06` (blind)

Verifier: opus, 2026-11-11. Sources: snapshot PDFs of the LGT (2024-12-21: arts. 120.1, 120.3, 121), RIRPF (2026-10-07: arts. 75, 76) and RDL 29/2026 (`BOE-A-2026-20823_rdl-29-2026_2026-10-07.pdf`), disposición final tercera: Tres (75.3.h)), Cuatro (75.3.i)), Cinco (new 75.3.k) and last paragraph of 75.3), Seis (75.4), Siete (76.2.h)), all «con efectos desde la entrada en vigor de este real decreto-ley»; the RDL is unconvalidated (`normativa.yaml` header). Arts. 75.1 and 76.1 are untouched by the RDL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `3cf81ddf26` | PASS | arts. 120.1 and 121 LGT | art. 120.1 «Las autoliquidaciones son declaraciones…», art. 121 «la declaración presentada…»; blacklisted «Son…» opener gone | — |
| `4be64fc2a0` | PASS | art. 120.3 LGT | base «sobre el importe de la devolución que proceda», «sin necesidad de que el obligado lo solicite» and both starting points of the six months kept | — |
| `58b836e622` | PASS | art. 75.1 RIRPF | no RDL mark, right: apartado 1 is unchanged | — |
| `a0d35e99e9` | PASS | art. 75.3.h)–k) RIRPF; RDL 29/2026, DF 3.ª Tres–Cinco | h), i) and k) are in the RDL wording (k) added by it); j) exists and is unchanged; mark in the form of the spec | — |
| `671c558f0f` | PASS | art. 76.1 RIRPF | words of the article; no RDL mark, right: the RDL changes only 76.2.h), not cited | — |

PASS 5 · FAIL 0
