"""fast_tags.py [lesson…]: tag_origins with an indexed row-twin lookup (same result, no quadratic scan)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "docs/age-verification/aeat/r2d/tools"))
sys.path.insert(0, str(ROOT / "backend"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_check  # noqa: E402
import tag_origins  # noqa: E402

_cache: dict[int, tuple[dict[str, tuple[str, str]], str]] = {}


def _index(pool: dict[str, tuple[str, str]]) -> tuple[dict[str, tuple[str, str]], str]:
    if id(pool) not in _cache:
        exact: dict[str, tuple[str, str]] = {}
        for text, twin in pool.items():
            exact.setdefault(text, twin)
            exact.setdefault(build_check.MARKER.sub("", text, count=1), twin)
        _cache[id(pool)] = (exact, "\n".join(pool))
    return _cache[id(pool)]


def row_twin(row: str, pool: dict[str, tuple[str, str]]) -> tuple[str, str] | None:
    exact, blob = _index(pool)
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    for cell in sorted(cells, key=len, reverse=True):
        for candidate in (cell, build_check.MARKER.sub("", cell, count=1)):
            if candidate in exact:
                return exact[candidate]
    candidate = build_check.MARKER.sub("", max(cells, key=len), count=1)
    if len(candidate) >= 15 and candidate in blob:
        return ("", "substring")
    return None


from lesson_model import references  # noqa: E402


def keys(text: str) -> set[str]:
    out: set[str] = set()
    for body, norm in references(text):
        body = re.sub(r"(\d+)[.\w)(ºª]*", r"\1", body)
        for a, b in re.findall(r"(\d+)\s*(?:\N{EN DASH}|-|to|a)\s*(\d+)", body):
            if int(b) - int(a) < 300:
                out.update(f"{n} {norm}" for n in range(int(a), int(b) + 1))
        out.update(f"{n} {norm}" for n in re.findall(r"\d+", body))
    return out


tag_origins._keys = keys
build_check._row_twin = row_twin
if __name__ == "__main__":
    raise SystemExit(tag_origins.main(sys.argv[1:]))
