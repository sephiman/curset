# SPDX-License-Identifier: AGPL-3.0-only
"""`http-method-properties`: which HTTP methods are safe or idempotent under RFC 9110."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.cited_source import source_line

Kind = Literal["safe", "not-safe", "idempotent-unsafe", "not-idempotent"]

SAFE = ("GET", "HEAD", "OPTIONS", "TRACE")
IDEMPOTENT_UNSAFE = ("PUT", "DELETE")
NEITHER = ("POST",)
#: Resource paths by length, so that every request line has the same length and length says nothing.
PATHS_BY_LENGTH: dict[int, tuple[str, str]] = {
    7: ("/jobs/3", "/tags/8"),
    8: ("/carts/4", "/files/7"),
    9: ("/orders/9", "/items/12"),
    10: ("/users/124", "/books/405"),
    11: ("/invoices/2", "/reports/17"),
}
LINE_LENGTH = 15
CLASS_OF = {
    **dict.fromkeys(SAFE, "safe"),
    **dict.fromkeys(IDEMPOTENT_UNSAFE, "idempotent but not safe"),
    **dict.fromkeys(NEITHER, "neither safe nor idempotent"),
}


ASKED: dict[Kind, str] = {
    "safe": "a safe request",
    "not-safe": "a request that is not safe",
    "idempotent-unsafe": "an idempotent request that is not safe",
    "not-idempotent": "a request that is not idempotent",
}


@dataclass(frozen=True)
class Methods:
    kind: Kind
    variant: int
    answer: str


def is_safe(method: str) -> bool:
    return method in SAFE


def is_idempotent(method: str) -> bool:
    return method in SAFE or method in IDEMPOTENT_UNSAFE


def fits(kind: Kind, method: str) -> bool:
    if kind == "safe":
        return is_safe(method)
    if kind == "not-safe":
        return not is_safe(method)
    if kind == "idempotent-unsafe":
        return is_idempotent(method) and not is_safe(method)
    return not is_idempotent(method)


class HttpMethodPropertiesGenerator(BackendGenerator[Methods]):
    id: ClassVar[str] = "http-method-properties"
    citation: ClassVar[Citation] = Citation(
        "m07-l04", "rfc9110#section-9.2.1", confirmed="rfc9110#section-9.2.1; rfc9110#section-9.2.2"
    )

    def scenario(self, rng: random.Random, level: int) -> Methods:
        kind: Kind = (
            "safe" if level == 1 else rng.choice(("idempotent-unsafe", "not-idempotent", "safe", "not-safe"))
        )
        pool = [m for m in CLASS_OF if fits(kind, m)]
        return Methods(kind, rng.randrange(2), rng.choice(pool))

    def stem(self, s: Methods) -> str:
        if s.kind == "safe":
            return (
                "A client may send any of the following requests. Which one is safe in "
                "the sense of RFC 9110, meaning its defined semantics are essentially read-only?"
            )
        if s.kind == "not-safe":
            return (
                "A client may send any of the following requests. Which one is not safe in the sense of "
                "RFC 9110, because its defined semantics are not essentially read-only?"
            )
        if s.kind == "idempotent-unsafe":
            return (
                "A client may send any of the following requests. Which one is idempotent "
                "but not safe, as RFC 9110 defines both properties for its methods?"
            )
        return (
            "A proxy sits between a client and an origin server, and a connection fails before the "
            "response arrives. Which of these requests must the proxy not retry automatically?"
        )

    def _line(self, s: Methods, method: str) -> str:
        return code(f"{method} {PATHS_BY_LENGTH[LINE_LENGTH - len(method) - 1][s.variant]}")

    def correct(self, s: Methods) -> str:
        return self._line(s, s.answer)

    def mistakes(self, s: Methods) -> list[str]:
        return [self._line(s, m) for m in CLASS_OF if not fits(s.kind, m)]

    def explanation(self, s: Methods) -> str:
        rule = (
            f"RFC 9110 defines {_codes(SAFE)} as safe; {_codes(IDEMPOTENT_UNSAFE)} and the safe methods "
            f"are idempotent; no other method it defines is idempotent"
        )
        goal, misreading = {
            "safe": (
                "find the method among the safe ones",
                "taking a method that changes state for a read-only one",
            ),
            "not-safe": (
                "find the method among the ones that are not safe",
                "taking a read-only method for one that changes state",
            ),
            "idempotent-unsafe": (
                "keep the idempotent methods and drop the safe ones",
                "forgetting that safe methods are idempotent too, or taking `POST` for idempotent",
            ),
            "not-idempotent": (
                "keep the methods that are not idempotent, which a proxy must not retry",
                "taking an idempotent method for one that must not be retried",
            ),
        }[s.kind]
        wrong = ", ".join(f"{code(m)} is {CLASS_OF[m]}" for m in CLASS_OF if not fits(s.kind, m))
        return (
            f"Inputs: the question asks for {ASKED[s.kind]}. "
            f"Rule: {rule}. "
            f"Step 1: classify {code(s.answer)} as {CLASS_OF[s.answer]}. "
            f"Step 2: {goal}. "
            f"Result: {self._line(s, s.answer)}. The other options come from {misreading}: {wrong}. "
            f"{source_line(self.citation)}"
        )


def _codes(methods: tuple[str, ...]) -> str:
    return ", ".join(code(m) for m in methods)
