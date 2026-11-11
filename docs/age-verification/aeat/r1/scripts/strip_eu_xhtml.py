"""Strip the Cellar XHTML of the two CAU regulations: drop embedded data: images and event handlers, keep the rest byte for byte."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
NORMATIVA = REPO / "content/aeat-agentes-hacienda/sources/normativa"
ORIGINALS = Path.home() / "PycharmProjects/curset-saved-originals/aeat-agentes-hacienda/normativa"
FILES = (
    "CELEX-02015R2446-20261101_cau-reglamento-delegado_2026-11-01.html",
    "CELEX-02015R2447-20260701_cau-reglamento-ejecucion_2026-07-01.html",
)
EMBEDDED_IMAGE = re.compile(rb"<img\s[^>]*?src=\"data:[^\"]*\"[^>]*>", re.S)
EVENT_HANDLER = re.compile(rb"\s+on[a-z]+=\"[^\"]*\"")


def strip(xhtml: bytes) -> bytes:
    return EVENT_HANDLER.sub(b"", EMBEDDED_IMAGE.sub(b"", xhtml))


def main() -> int:
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        path = NORMATIVA / name
        raw = path.read_bytes()
        backup = ORIGINALS / name
        if not backup.exists():  # a second run must not overwrite the bytes as fetched
            backup.write_bytes(raw)
        original = backup.read_bytes()
        stripped = strip(original)
        path.write_bytes(stripped)
        print(
            f"{name}\t{len(original)}\t{hashlib.sha256(original).hexdigest()}"
            f"\t{len(stripped)}\t{hashlib.sha256(stripped).hexdigest()}"
            f"\timages {len(EMBEDDED_IMAGE.findall(original))}\thandlers {len(EVENT_HANDLER.findall(original))}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
