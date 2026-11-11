"""prov.py plan|record [lesson…]: provenance.py for AEAT lessons, with the C1/C2 sources derivation.yaml maps."""

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
PLAN = yaml.safe_load((ROOT / "docs/age-verification/aeat/r2/derivation.yaml").read_text())
EXTRA = yaml.safe_load((ROOT / "docs/age-verification/aeat/r2/extra-sources.yaml").read_text() or "{}") if (
    ROOT / "docs/age-verification/aeat/r2/extra-sources.yaml").exists() else {}


def sources(lesson: str) -> list[str]:
    found = [str(i["take"]).split("#", 1)[0] for i in PLAN[lesson] if "take" in i]
    return list(dict.fromkeys(found + list(EXTRA.get(lesson, []))))


def main(command: str, lessons: list[str]) -> int:
    status = 0
    for lesson in lessons or list(PLAN):
        args = ["uv", "run", "python", "-m", "scripts.provenance", "--course", "aeat-agentes-hacienda", command,
                lesson, *sources(lesson)]
        done = subprocess.run(args, cwd=ROOT / "backend", capture_output=True, text=True)
        print((done.stderr.strip().splitlines() or ["?"])[-1])
        status |= done.returncode
    return status


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1], sys.argv[2:]))
