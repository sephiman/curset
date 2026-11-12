#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
# The CI `e2e` job on this machine: the backend image built from the working tree and a throwaway
# Postgres, as two containers with the job's service settings, then the same `npm run test:e2e`.
# Keep in step with `.github/workflows/ci.yml` (jobs.e2e). Needs :8000 free; reuses a Vite on :5173.
set -euo pipefail

repo="$(cd "$(dirname "$0")/../.." && pwd)"
network=curset-e2e
image=curset-backend:e2e

if curl -fsS -o /dev/null http://localhost:8000/api/health 2>/dev/null; then
  echo "Something already answers on :8000; stop the dev backend first." >&2
  exit 1
fi

cleanup() {
  docker rm -f curset-e2e-backend curset-e2e-postgres >/dev/null 2>&1 || true
  docker network rm "$network" >/dev/null 2>&1 || true
}
trap cleanup EXIT
cleanup

docker build --file "$repo/backend/Dockerfile" --tag "$image" "$repo"
docker network create "$network" >/dev/null

docker run --detach --name curset-e2e-postgres --network "$network" --network-alias postgres \
  --env POSTGRES_USER=curset --env POSTGRES_PASSWORD=curset-e2e --env POSTGRES_DB=curset \
  --health-cmd "pg_isready -U curset -d curset" --health-interval 2s --health-timeout 5s --health-retries 30 \
  postgres:17 >/dev/null

docker run --detach --name curset-e2e-backend --network "$network" --publish 127.0.0.1:8000:8000 \
  --env DB_HOST=postgres --env DB_USERNAME=curset --env DB_PASSWORD=curset-e2e --env DB_NAME=curset \
  --env AUTH_SECRET=e2e-only-not-a-secret --env COOKIE_SECURE=false \
  --env RUN_MIGRATIONS_ON_STARTUP=true --env SYNC_CONTENT_ON_STARTUP=true --env DEV_MODE=true --env EXTRA_CONTENT_DIR=/app/e2e-content \
  --restart on-failure:20 \
  --health-cmd "curl -fsS http://localhost:8000/api/health" \
  --health-interval 3s --health-timeout 5s --health-start-period 5s --health-retries 40 \
  "$image" >/dev/null

for _ in $(seq 1 60); do
  [ "$(docker inspect --format '{{.State.Health.Status}}' curset-e2e-backend)" = healthy ] && break
  sleep 2
done
if [ "$(docker inspect --format '{{.State.Health.Status}}' curset-e2e-backend)" != healthy ]; then
  docker logs curset-e2e-backend >&2
  exit 1
fi

# A fresh database: the session file from a run against another stack would name an account it lacks.
rm -rf "$repo/frontend/e2e/.auth"
cd "$repo/frontend"
npm run test:e2e
