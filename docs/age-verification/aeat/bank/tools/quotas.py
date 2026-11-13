"""Per-tema quotas of the AEAT bank: 5,000 split by the questions per tema of OEP 2022–2025, floor 50, largest remainders.

Usage: `python3 quotas.py` prints the table as markdown and the JSON on the last line.
"""

from __future__ import annotations

import json

TOTAL = 5000
FLOOR = 50
# Ledger «Questions per tema per exam», last column (OEP 2022–2025 with the 2022 extraordinario).
WEIGHT = {
    "I.1": 9, "I.2": 9, "I.3": 13, "I.4": 13, "I.5": 10, "I.6": 9, "I.7": 11,
    "II.1": 9, "II.2": 14, "II.3": 14, "II.4": 15, "II.5": 12,
    "III.1": 9, "III.2": 9, "III.3": 13, "III.4": 32, "III.5": 22, "III.6": 8, "III.7": 16, "III.8": 23,
    "III.9": 16, "III.10": 10, "III.11": 11, "III.12": 24, "III.13": 20, "III.14": 18, "III.15": 24,
    "III.16": 16, "III.17": 8, "III.18": 15, "III.19": 19, "III.20": 11,
}


def quotas() -> dict[str, int]:
    total_weight = sum(WEIGHT.values())
    raw = {t: TOTAL * w / total_weight for t, w in WEIGHT.items()}
    base = {t: max(FLOOR, int(r)) for t, r in raw.items()}
    # floors may overshoot: take the surplus back from the largest temas, then hand out the remainder by fraction
    while sum(base.values()) > TOTAL:
        t = max((t for t in base if base[t] > FLOOR), key=lambda t: base[t] - raw[t])
        base[t] -= 1
    order = sorted(raw, key=lambda t: raw[t] - int(raw[t]), reverse=True)
    i = 0
    while sum(base.values()) < TOTAL:
        base[order[i % len(order)]] += 1
        i += 1
    return base


if __name__ == "__main__":
    q = quotas()
    print("| Tema | Weight | Quota |\n|---|---|---|")
    for t in WEIGHT:
        print(f"| {t} | {WEIGHT[t]} | {q[t]} |")
    for part in ("I.", "II.", "III."):
        print(part, sum(v for t, v in q.items() if t.startswith(part) and (part != "I." or not t.startswith("II"))))
    print(sum(q.values()))
    print(json.dumps(q))
