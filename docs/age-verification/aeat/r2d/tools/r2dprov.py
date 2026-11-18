"""r2dprov.py plan|record|apply <lesson…>: provenance for R2d; its reports win over R2, R2-tax and R2b/c."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "docs/age-verification/aeat/r2-tax/tools"))
sys.path.insert(0, str(ROOT / "backend"))

import taxprov  # noqa: E402
from scripts.provenance import report_verdicts  # noqa: E402

R2D = ROOT / "docs/age-verification/aeat/r2d"
COMMON_REPORTS = ROOT / "docs/age-verification/aeat/r2/verify"


def _reports(lesson_id: str) -> list[Path]:
    common = sorted(COMMON_REPORTS.glob("*.md"), key=taxprov._order) if lesson_id < "m03" else []
    tax = sorted((taxprov.TAX / lesson_id).glob("verify*.md"), key=taxprov._order)
    return common + tax + sorted((R2D / lesson_id).glob("verify*.md"), key=taxprov._order)


def verdicts(lesson_id: str) -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    for report in _reports(lesson_id):
        for sid, verdict in report_verdicts(report).items():
            out[sid] = (verdict, str(report.relative_to(ROOT)))
    return out


if __name__ == "__main__":
    if sys.argv[1] == "apply":
        taxprov.apply(sys.argv[2], Path(sys.argv[3]), pending_root=R2D)
        raise SystemExit(0)
    raise SystemExit(taxprov.main(sys.argv[1], sys.argv[2:], verdicts_of=verdicts, pending_root=R2D))
