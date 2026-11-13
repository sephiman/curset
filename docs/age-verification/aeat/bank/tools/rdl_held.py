"""Citations that rest on an article under RDL 29/2026 (pending convalidation): such a question is held, not built.

Source: docs/age-verification/aeat/r1/rdl-29-2026-revert-list.md. A citation is held when it names one of these
precepts. The match is by norm and article number (paragraph-aware for LIRPF arts. 23 and 85); a bare «art. 23 LIRPF»
is held too. Usage: imported by check_draft.py and the build; `python3 rdl_held.py <json> …` lists the held ids.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# norm label → article numbers; disposiciones as «adicional 55», «transitoria 15»
HELD: dict[str, set[str]] = {
    "LIRPF": {"24", "67", "68", "95 ter", "adicional 55", "adicional 5", "adicional 26", "adicional 50",
              "adicional 58", "adicional 62", "adicional 65", "adicional 66", "transitoria 15", "transitoria 38"},
    "RIRPF": {"41 bis", "69", "75", "76", "93", "94", "adicional 8"},
    "TRLRHL": {"72"},
    "LIVA": {"91"},
    "RGAT": {"39 quater"},
}
PARAGRAPH_HELD = {("LIRPF", "23"): {"2"}, ("LIRPF", "85"): {"1"}}
NUMBER = re.compile(r"(\d+(?:\s?(?:bis|ter|quater))?)(?:\.(\d+))?")
SEGMENT = re.compile(r"^(?P<kind>arts?\.|disposici[óo]n(?:es)? (?P<disp>adicional|transitoria)(?:es)?|DA|DT)\s*(?P<list>.+?)\s+(?P<norm>[A-Z]{3,6})$")


def held_reason(citation: str) -> str | None:
    for part in citation.split(";"):
        m = SEGMENT.match(part.strip())
        if not m or m.group("norm") not in HELD:
            continue
        norm = m.group("norm")
        disp = m.group("disp") or {"DA": "adicional", "DT": "transitoria"}.get(m.group("kind"), "")
        for art, para in NUMBER.findall(m.group("list")):
            key = f"{disp} {art}".strip()
            if (norm, art) in PARAGRAPH_HELD and not disp:
                if not para or para in PARAGRAPH_HELD[(norm, art)]:
                    return f"{norm} art. {art}{'.' + para if para else ''}"
            elif key in HELD[norm]:
                return f"{norm} {key}"
    return None


if __name__ == "__main__":
    for name in sys.argv[1:]:
        for q in json.loads(Path(name).read_text(encoding="utf-8")):
            reason = held_reason(str(q["citation"]))
            if reason:
                print(f"{q['id']}\t{reason}\t{q['citation']}")
