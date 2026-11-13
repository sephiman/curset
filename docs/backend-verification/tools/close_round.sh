#!/usr/bin/env bash
# close_round.sh <scratch dir> — the closing checks of a backend-in-depth round; read every diff it prints.
set -uo pipefail
repo="$(cd "$(dirname "$0")/../../.." && pwd)"
scratch="${1:?usage: close_round.sh <scratch dir outside the repo>}"
mkdir -p "$scratch"
status=0
step() { printf '\n=== %s\n' "$1"; }
fail() { echo "FAIL: $1"; status=1; }

step "other courses (any path listed changed in this round; must be empty)"
changed="$(git -C "$repo" status --porcelain -- content/crypto-futures content/age-administrativo-c1 \
  content/age-auxiliar-c2 content/aeat-agentes-hacienda | awk '{print $2}' | sort)"
if [ -n "$changed" ]; then echo "$changed"; fail "another course changed"; else echo "byte-identical"; fi

step "Android bundle re-exported to $scratch/bundle and compared with dist/bundle"
rm -rf "$scratch/bundle"
(cd "$repo/backend" && uv run python scripts/export_bundle.py --out "$scratch/bundle" >"$scratch/bundle.log" 2>&1) \
  || fail "export_bundle.py (see $scratch/bundle.log)"
if diff -rq "$repo/dist/bundle" "$scratch/bundle" >"$scratch/bundle.diff"; then
  echo "byte-identical"
else
  echo "differs: $(wc -l <"$scratch/bundle.diff") files (list in $scratch/bundle.diff)"
  fail "Android bundle"
fi

step "backend: uv run pytest"
(cd "$repo/backend" && uv run pytest -q -p no:warnings 2>&1 | tail -3) | tee "$scratch/backend.log"
grep -qE ' (failed|error)' "$scratch/backend.log" && fail "backend suite"

step "frontend: npx vitest run; tsc -b"
(cd "$repo/frontend" && npx vitest run 2>&1 | grep -E '^ +Tests ') | tee "$scratch/frontend.log"
grep -q 'failed' "$scratch/frontend.log" && fail "frontend suite"
(cd "$repo/frontend" && npx tsc -b) && echo "tsc -b clean" || fail "tsc -b"

step "backend-in-depth audits (coverage pending is reported, never a failure)"
tech() { (cd "$repo/backend" && uv run python -m "scripts.tech_course.$1" "${@:2}"); }
tech run_snippets --check || fail "run_snippets --check"
tech check_citations || fail "check_citations"
tech check_extracts || fail "check_extracts"
tech check_scope || fail "check_scope"
tech check_coverage || fail "check_coverage"
tech lint_questions --exclude-failed || fail "lint_questions"

step "lesson quota report"
tech lesson_quota | tee "$scratch/lesson_quota.tsv" | awk -F'\t' 'NR==1 || $2=="written"'

exit $status
