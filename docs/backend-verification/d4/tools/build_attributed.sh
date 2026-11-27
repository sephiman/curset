#!/usr/bin/env bash
# build_attributed.sh — round D4 Part D: one exercise file per lesson from its blind-checked attributed questions.
# A question is left out when its verdict or the length-cue file (decision D4-D-6) has a fail line.
set -euo pipefail
repo="$(cd "$(dirname "$0")/../../../.." && pwd)"
work="$repo/docs/_work/backend-in-depth/d4/attr"
for q in "$work"/m*.questions.json; do
  lesson="$(basename "$q" .questions.json)"
  verdicts="$work/$lesson.combined.tsv"
  cat "$work/$lesson.verdicts.tsv" <(grep "^$lesson-" "$work/length-cue.tsv" || true) >"$verdicts"
  kept="$(python3 - "$q" "$verdicts" <<'PY'
import json, sys
fails = {l.split("\t")[0] for l in open(sys.argv[2]) if "\tfail" in l}
print(sum(q["id"] not in fails for q in json.load(open(sys.argv[1]))))
PY
)"
  out="$repo/content/backend-in-depth/exercises/$lesson-ex-attributed.yaml"
  if [ "$kept" = 0 ]; then rm -f "$out"; echo "$lesson: none kept"; continue; fi
  python3 "$repo/docs/backend-verification/s2/tools/build_quiz.py" "$q" "$out" --verdicts "$verdicts" >/dev/null
  echo "$lesson: $kept kept"
done
