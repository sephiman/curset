# S1 Part A — source recovery (2026-11-13)

**Tier B** (`s0/tier-b.yaml`, coordinator-supplied data, chapter numbers only): `ddia-kleppmann` (1st ed., O'Reilly 2017, ISBN 978-1-449-37332-0, ch. 3, 5–9; bullets 6.2.a, 9.1.b, 8.2.b, 8.5.e, 9.2.b, 9.2.c) replaces the S0 entry; `clrs-4` (4th ed., MIT Press 2022, ISBN 978-0-262-04630-5; module 02 bullets). Orientation only.

**Tier A stored** (`tech_sources.py fetch`, all `storage: local`, `extract_allowed: false`):
- `paper-berenson-critique-ansi-isolation` (MSR-TR-95-51, June 1995) sha256 `daa8ed45e311`; evidence `paper-critique-ansi-isolation-page` (MSR publication page: six authors, MSR-TR-95-51, June 1995) `7e355ecfc7b2`. Write skew = A5B: `#p9`, `#p10`.
- `paper-ports-grittner-ssi` (PVLDB 5(12), pp. 1850–1861) `29ea89b404b6`; evidence `paper-ports-grittner-ssi-page` (vldb.org vol5 page) `a83e34fb3d3a`. Write skew: `#p2` (Figure 1), `#p3` (sec. 2.1.1).
- `paper-basiri-chaos-engineering` (IEEE Software 33(3) 2016, arXiv 1702.05843 author preprint) `64a9380e5a5d`; evidence `paper-basiri-chaos-engineering-page` `3ff72fe68640`.

**Tier C stored:** `azure-waf-design-diagrams` (Azure Well-Architected, Architecture design diagrams) `8585d8d5bbb0`. `principles-of-chaos` retiered A → C: Basiri et al. p2 say the authors posted it online.

**Licence rules added** (`sources/licences.yaml`, from each paper's own notice): Critique PDF (ACM notice), `vldb.org/pvldb` (VLDB notice), arXiv 1702.05843 (© 2016 IEEE); all no extracts. `pg-transaction-iso` confirmed (sha256 `3bf98c4886dd`, unchanged), reused; it does not use the name "write skew".

**Bullets** (`coverage/m*.final.tsv`, `default-rules.tsv` annotated, nothing deleted):
- 6.2.a F: four paper anchors added, R2 cleared, "write skew" restored.
- 9.1.b drop → X (amendment 1), DDIA orientation.
- 9.1.d drop → J (R1) via `azure-waf-design-diagrams` (high-level system diagram, data-flow diagram).
- 11.6.g drop → F (R1): hypothesis, failure injection and experiment steps from Basiri et al.; "blast radius" is J from principles-of-chaos; SRE ch. 17 statistical tests as J.
- 1.4.a stays dropped: Google eng-practices and the Microsoft Engineering Playbook checklists do not cover unnecessary dependencies, encapsulation, leaky abstractions or hidden debt. 1.4.c and 12.4.a were not touched.

**Totals:** F 158, F+X 33, X 10, J 45, drop 3; 1,351 refs, 0 unresolved. `coverage_report.py` already handled X, so it was not changed. Ledger rows 09 and 11 and the Coverage bullet were updated. The ledger's Sources line (619; 595 A / 24 C) is now out of date: the real counts are 623 (597 A / 26 C), and it was left for the coordinator. `pytest -k "source or tech or coverage"`: 32 passed.
