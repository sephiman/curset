#!/usr/bin/env bash
# prov.sh plan|record <c2 lesson> <c1 lessons...>
cd "$(dirname "$0")/../../../../../backend" && exec uv run python -m scripts.provenance "$@" 2>&1 | tail -1
