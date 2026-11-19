#!/usr/bin/env bash
# prep.sh <lesson…>: lint, apply overview/notes + layer + terms to the lesson, build the verifier and reader inputs.
set -u
cd "$(git rev-parse --show-toplevel)"
T="uv run --project backend python docs/age-verification/aeat/edition/tools"
for l in "$@"; do
  echo "== $l"
  $T/explanation.py lint "$l"
  $T/layer.py lint "$l"
  $T/explanation.py apply "$l" >/dev/null
  $T/layer.py strip "$l" >/dev/null
  $T/layer.py apply "$l" >/dev/null
  $T/layer.py apply-terms "$l" >/dev/null
  $T/verify_input.py "$l" >/dev/null
  $T/layer_verify.py "$l" >/dev/null
  $T/layer_reader.py "$l" >/dev/null
done
