#!/usr/bin/env bash
# close_round.sh <scratch dir> — the closing checks of a C2 content round, in the ledger's order; read every diff it prints.
set -uo pipefail
repo="$(cd "$(dirname "$0")/../../../.." && pwd)"
scratch="${1:?usage: close_round.sh <scratch dir outside the repo>}"
mkdir -p "$scratch"
status=0
step() { printf '\n=== %s\n' "$1"; }
fail() { echo "FAIL: $1"; status=1; }

step "goldens regenerated (read the diff)"
(cd "$repo/backend" && UPDATE_CITATIONS=1 uv run pytest tests/test_citations.py -q >/dev/null 2>&1)
(cd "$repo/frontend" && UPDATE_LESSON_REFS=1 npx vitest run src/lib/refs/report.test.ts >/dev/null 2>&1 \
  && UPDATE_GLOSSARY_LINKS=1 npx vitest run src/lib/glossary/report.test.ts >/dev/null 2>&1)
git -C "$repo" diff --stat -- 'content/*/citations.*.txt' 'content/*/lesson-refs.*.txt' 'content/*/glossary-links.*.txt'

step "crypto-futures and C1 (any path listed changed in this round)"
git -C "$repo" status --porcelain -- content/crypto-futures content/age-administrativo-c1 | awk '{print $2}' \
  | sed -E 's#(sources/otros)/[^/]+$#\1/…#' | sort | uniq -c

step "Android bundle re-exported to $scratch/bundle and compared with dist/bundle"
rm -rf "$scratch/bundle"
(cd "$repo/backend" && uv run python scripts/export_bundle.py --out "$scratch/bundle" >"$scratch/bundle.log" 2>&1) \
  || fail "export_bundle.py (see $scratch/bundle.log)"
if diff -rq "$repo/dist/bundle" "$scratch/bundle" >"$scratch/bundle.diff"; then
  echo "byte-identical"
else
  echo "differs: $(wc -l <"$scratch/bundle.diff") files (list in $scratch/bundle.diff)"
fi

step "backend: uv run pytest"
(cd "$repo/backend" && uv run pytest -q -p no:warnings 2>&1 | tail -3) | tee "$scratch/backend.log"
grep -q ' failed' "$scratch/backend.log" && fail "backend suite"

step "frontend: npx vitest run; tsc -b"
(cd "$repo/frontend" && npx vitest run 2>&1 | grep -E '^ +Tests ' ) | tee "$scratch/frontend.log"
grep -q 'failed' "$scratch/frontend.log" && fail "frontend suite"
(cd "$repo/frontend" && npx tsc -b) && echo "tsc -b clean" || fail "tsc -b"

exit $status
