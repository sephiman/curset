## Writing rule (always)

The voice is defined in `docs/prose-voice.md`. This applies to every session, whatever the session
prompt says, unless the prompt explicitly overrides it.

- The course invents no vocabulary: only terms that exist outside the course with the same meaning.
- Every sentence of new or rewritten prose, lesson summaries and glossary definitions follows the voice
  page.
- The voice page's "never does" list is a hard constraint, not style advice.
- Spanish is Peninsular and addresses the reader as "tú".
- EN mirrors the ES structure.

## Subagent models and concurrency

- Writers (question drafting, lesson sentences, esquema rows): sonnet.
- Verifiers (blind checks of keys, citations, style, copies) and any
  re-check: opus. Never haiku for anything that decides a key.
- Coordinator: the session model.
- At most 8 subagents running at once (4 writers, 4 verifiers).
- A writer takes several parts in sequence in one run, reusing its
  loaded context; a verifier takes consecutive batches of 60 the same
  way. Spec, style guide and ofimática index are loaded once per agent
  run, not once per part.
- Progress is written to the ledger after every part, so a window cut
  loses at most one part.
- When the usage window is near its end, no new agents are launched;
  running ones finish their current part, the ledger is written, and
  work waits for the reset.

## Round working material

- Round working material (verifier inputs, drafts, reports, records, pools) lives under `docs/_work/` and `docs/age-verification/`; both are git-ignored and not part of the repo.
- Nothing in tests or build steps may read them, except the AEAT official-exam inputs `docs/age-verification/aeat/r0a` and `aeat/official`, which stay tracked.
