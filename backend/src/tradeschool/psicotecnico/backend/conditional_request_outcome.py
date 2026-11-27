# SPDX-License-Identifier: AGPL-3.0-only
"""`conditional-request-outcome`: the answer to a request whose `If-None-Match` condition is false."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.cited_source import source_line

Method = Literal["GET", "HEAD", "PUT", "DELETE"]
Match = Literal["list", "star"]

NOT_MODIFIED = "304 Not Modified"
PRECONDITION_FAILED = "412 Precondition Failed"
REVALIDATING: tuple[Method, ...] = ("GET", "HEAD")
LEVEL_METHODS: dict[int, tuple[Method, ...]] = {1: ("GET", "PUT"), 2: ("GET", "HEAD", "PUT", "DELETE")}
LEVEL_MATCHES: dict[int, tuple[Match, ...]] = {1: ("list",), 2: ("list", "star")}
PATHS = ("/items/7", "/books/41", "/orders/9", "/users/12", "/files/3")
TAGS = ("a1", "b2", "c3", "d4", "e5")


@dataclass(frozen=True)
class Request:
    method: Method
    path: str
    match: Match
    listed: tuple[str, ...]
    current: str


@dataclass(frozen=True)
class Answer:
    performed: bool
    status: str


def status_for(method: Method) -> str:
    return NOT_MODIFIED if method in REVALIDATING else PRECONDITION_FAILED


def answer_label(answer: Answer) -> str:
    if not answer.performed:
        return f"Answering {code(answer.status)} without performing the method"
    if answer.status == "2xx":
        return f"Performing the method and then answering with a {code('2xx')} status code"
    return f"Performing the method first and then answering {code(answer.status)}"


def answer_text(answer: Answer) -> str:
    if not answer.performed:
        return f"answers {code(answer.status)} and does not perform the method"
    if answer.status == "2xx":
        return f"performs the method and then answers with a {code('2xx')} status code"
    return f"performs the method first, then answers {code(answer.status)}"


@dataclass(frozen=True)
class Misreading:
    name: str
    answer: Answer
    why: str


def misreadings(method: Method) -> list[Misreading]:
    other_rule = (
        Misreading(
            f"applying the rule for the other methods, {code('412')}, to a {code(method)}",
            Answer(False, PRECONDITION_FAILED),
            f"a false {code('If-None-Match')} condition gets {code(NOT_MODIFIED)} "
            f"for {code('GET')} and {code('HEAD')}",
        )
        if method in REVALIDATING
        else Misreading(
            f"applying the rule for {code('GET')} and {code('HEAD')}, {code('304')}, to a {code(method)}",
            Answer(False, NOT_MODIFIED),
            f"a false {code('If-None-Match')} condition gets {code(PRECONDITION_FAILED)} "
            f"for every method but {code('GET')} and {code('HEAD')}",
        )
    )
    return [
        other_rule,
        Misreading(
            "ignoring the condition and performing the method",
            Answer(True, "2xx"),
            "the server must not perform the method when the condition evaluates to false",
        ),
        Misreading(
            "believing the condition is checked after the method has run",
            Answer(True, status_for(method)),
            "the condition is a precondition, tested before the method is applied to the target resource",
        ),
    ]


def header(request: Request) -> str:
    if request.match == "star":
        return "If-None-Match: *"
    return "If-None-Match: " + ",".join(f'"{tag}"' for tag in request.listed)


class ConditionalRequestOutcomeGenerator(BackendGenerator[Request]):
    id: ClassVar[str] = "conditional-request-outcome"
    # The subject is padding only: key and distractors share one template, so length says nothing.
    forms: ClassVar[tuple[str, ...]] = ("It {}", "The server {}", "The origin server {}")
    citation: ClassVar[Citation] = Citation(
        "m07-l04", "rfc9110#section-13.1.2", confirmed="rfc9110#section-13.1.2"
    )

    def scenario(self, rng: random.Random, level: int) -> Request:
        match = rng.choice(LEVEL_MATCHES[level])
        tags = rng.sample(TAGS, 3)
        listed = tuple(tags[:2]) if match == "list" else ()
        current = rng.choice(listed) if match == "list" else tags[2]
        return Request(rng.choice(LEVEL_METHODS[level]), rng.choice(PATHS), match, listed, current)

    def stem(self, s: Request) -> str:
        state = (
            f"The current entity tag of the resource is {code(chr(34) + s.current + chr(34))}."
            if s.match == "list"
            else "The resource has a current representation."
        )
        return (
            f"A client sends {code(f'{s.method} {s.path}')} with {code(header(s))}. {state} "
            f"What does the origin server do?"
        )

    def correct(self, s: Request) -> str:
        return answer_text(Answer(False, status_for(s.method)))

    def mistakes(self, s: Request) -> list[str]:
        return [answer_text(m.answer) for m in misreadings(s.method)]

    def explanation(self, s: Request) -> str:
        condition = (
            f"the resource has a current representation, so the condition {code('*')} is false"
            if s.match == "star"
            else f"the listed tag {code(chr(34) + s.current + chr(34))} matches the current entity tag, "
            f"so the condition is false"
        )
        wrong = " ".join(
            f"{answer_label(m.answer)} comes from {m.name}, but {m.why}." for m in misreadings(s.method)
        )
        return (
            f"Inputs: {code(f'{s.method} {s.path}')}, {code(header(s))}. "
            f"Rule: the {code('If-None-Match')} condition is false when {code('*')} meets a current "
            f"representation or a listed tag matches the current one; then the server must not perform the "
            f"method and answers {code(NOT_MODIFIED)} for {code('GET')} or {code('HEAD')} and "
            f"{code(PRECONDITION_FAILED)} for all other methods. "
            f"Step 1: {condition}. "
            f"Step 2: the method is {code(s.method)}, so the answer is {code(status_for(s.method))}. "
            f"Result: {answer_label(Answer(False, status_for(s.method)))}. "
            f"{wrong} {source_line(self.citation)}"
        )
