# SPDX-License-Identifier: AGPL-3.0-only
"""`property-source-winner`: the value a Spring Boot property resolves to when several sources define it."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.cited_source import source_line
from tradeschool.psicotecnico.item import OPTION_COUNT

#: From the lowest to the highest precedence, as the lesson lists them.
PRECEDENCE: tuple[tuple[str, str], ...] = (
    ("default", "the default properties"),
    ("yaml-jar", f"{code('application.yaml')} inside the jar"),
    ("props-jar", f"{code('application.properties')} inside the jar"),
    ("profile-jar", f"{code('application-prod.properties')} inside the jar"),
    ("props-outside", f"{code('application.properties')} outside the jar"),
    ("profile-outside", f"{code('application-prod.properties')} outside the jar"),
    ("env", f"environment variable {code('ACME_TIMEOUT')}"),
    ("sysprop", f"system property {code('-Dacme.timeout')}"),
    ("cli", f"argument {code('--acme.timeout')}"),
)
KEYS = tuple(key for key, _ in PRECEDENCE)
LABEL = dict(PRECEDENCE)
EASY = ("default", "props-jar", "env", "sysprop", "cli")
FILES = KEYS[1:6]
VALUES = (5, 10, 15, 25, 40, 60, 100, 150)
SOURCE_COUNT = 4

#: Each named misreading is the order a reader wrongly assumes, lowest to highest.
MISREADINGS: dict[str, tuple[str, ...]] = {
    "the first source read wins": tuple(reversed(KEYS)),
    "files outrank the environment and arguments": (
        "default",
        "env",
        "sysprop",
        "cli",
        "yaml-jar",
        "props-jar",
        "profile-jar",
        "props-outside",
        "profile-outside",
    ),
    "a file inside the jar outranks one outside": (
        "default",
        "props-outside",
        "profile-outside",
        "yaml-jar",
        "props-jar",
        "profile-jar",
        "env",
        "sysprop",
        "cli",
    ),
    "YAML outranks properties in one location": (
        "default",
        "props-jar",
        "yaml-jar",
        "profile-jar",
        "props-outside",
        "profile-outside",
        "env",
        "sysprop",
        "cli",
    ),
    "the environment outranks system properties": (
        "default",
        "yaml-jar",
        "props-jar",
        "profile-jar",
        "props-outside",
        "profile-outside",
        "sysprop",
        "env",
        "cli",
    ),
    "the plain file outranks its profile file": (
        "default",
        "yaml-jar",
        "profile-jar",
        "props-jar",
        "profile-outside",
        "props-outside",
        "env",
        "sysprop",
        "cli",
    ),
}


@dataclass(frozen=True)
class Definitions:
    #: (source key, value), in the order the stem lists them.
    defined: tuple[tuple[str, int], ...]


def winner(s: Definitions, order: tuple[str, ...] = KEYS) -> int:
    return max(s.defined, key=lambda entry: order.index(entry[0]))[1]


class PropertySourceGenerator(BackendGenerator[Definitions]):
    id: ClassVar[str] = "property-source-winner"
    citation: ClassVar[Citation] = Citation(
        "m05-l02",
        "spring-boot-features-external-config#page-title",
        confirmed="spring-boot-features-external-config#page-title",
    )

    def scenario(self, rng: random.Random, level: int) -> Definitions | None:
        if level == 1:
            sources = rng.sample(EASY, SOURCE_COUNT)
        else:
            sources = rng.sample(KEYS, SOURCE_COUNT)
            if sum(key in FILES for key in sources) < 2:
                return None
        drawn = Definitions(tuple(zip(sources, rng.sample(VALUES, SOURCE_COUNT), strict=True)))
        named = {winner(drawn, order) for order in MISREADINGS.values()} - {winner(drawn)}
        return drawn if len(named) >= OPTION_COUNT - 1 else None

    def stem(self, s: Definitions) -> str:
        listed = [f"{value} in {LABEL[key]}" for key, value in s.defined]
        has_profile = any("profile" in key for key, _ in s.defined)
        opening = "Spring Boot 4, profile `prod` active:" if has_profile else "Spring Boot 4:"
        return (
            f"{opening} {code('acme.timeout')} is {', '.join(listed[:-1])} and {listed[-1]}. "
            f"Which value wins?"
        )

    def correct(self, s: Definitions) -> str:
        return code(winner(s))

    def mistakes(self, s: Definitions) -> list[str]:
        return [code(winner(s, order)) for order in MISREADINGS.values()]

    def explanation(self, s: Definitions) -> str:
        ranked = sorted(s.defined, key=lambda entry: KEYS.index(entry[0]))
        chain = ", then ".join(f"{LABEL[key]} ({value})" for key, value in ranked)
        top_key, top_value = ranked[-1]
        beliefs: dict[int, list[str]] = {}
        for belief, order in MISREADINGS.items():
            if winner(s, order) != top_value:
                beliefs.setdefault(winner(s, order), []).append(belief)
        wrong = "; ".join(
            f"{code(value)} from believing that {' or that '.join(reasons)}"
            for value, reasons in beliefs.items()
        )
        return (
            f"Inputs: {', '.join(f'{LABEL[key]} = {value}' for key, value in s.defined)}. "
            f"Rule: Spring Boot reads its sources in a fixed order and a later source overrides an earlier "
            f"one; from lowest to highest the sources here rank default properties, application files "
            f"(YAML before properties, inside the jar before outside, the plain file before its profile "
            f"file), environment variables, system properties, command-line arguments. "
            f"Step 1: order the defined sources from the lowest rank: {chain}. "
            f"Step 2: the last one in that order, {LABEL[top_key]}, overrides all the others. "
            f"Result: {code(top_value)}. The other values come from misreadings: {wrong}. "
            f"{source_line(self.citation)}"
        )
