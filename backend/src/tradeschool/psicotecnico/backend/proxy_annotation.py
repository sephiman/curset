# SPDX-License-Identifier: AGPL-3.0-only
"""`proxy-annotation-applies`: whether the advice of a proxy-based annotation runs for a given call shape."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar, Literal

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.cited_source import source_line

Shape = Literal[
    "external", "self-injection", "self-invocation", "final", "private", "package-private", "aspectj"
]

APPLIES: dict[Shape, bool] = {
    "external": True,
    "self-injection": True,
    "package-private": True,
    "aspectj": True,
    "self-invocation": False,
    "final": False,
    "private": False,
}
#: The shapes whose rule is stated for `@Transactional` only.
TRANSACTIONAL_ONLY: tuple[Shape, ...] = ("package-private", "aspectj")
ANNOTATIONS = ("@Transactional", "@Cacheable", "@Async")
LEVEL_SHAPES: dict[int, tuple[Shape, ...]] = {
    1: ("external", "self-invocation", "self-injection"),
    2: ("final", "private", "package-private", "aspectj", "self-invocation", "external"),
}

CALL: dict[Shape, str] = {
    "external": "In proxy mode, another bean calls the public method through its injected reference.",
    "self-injection": "In proxy mode, another public method of the bean calls it through a self reference.",
    "self-invocation": "In proxy mode, another public method of the same bean calls it as `this.method()`.",
    "final": "In proxy mode, the class has no interface and another bean calls its public `final` method.",
    "private": "In proxy mode, another public method of the same bean calls its `private` method.",
    "package-private": (
        "In Spring Framework 7, with a class-based proxy, another bean calls a package-visible method."
    ),
    "aspectj": "In AspectJ mode, another public method of the same bean calls it as `this.method()`.",
}
REASON: dict[Shape, str] = {
    "external": "the call comes in through the proxy, which then runs its interceptors for it",
    "self-injection": "the call goes through the injected proxy, not through `this`, so advice runs",
    "package-private": "a class-based proxy advises package-visible methods since Spring Framework 6",
    "aspectj": "AspectJ weaving puts the advice in the bytecode, so no proxy is left to skip",
    "self-invocation": "a call on `this` bypasses the proxy, so the interceptor chain does not run it",
    "final": "a class-based proxy extends the class and so cannot override a `final` method",
    "private": "a `private` method cannot be overridden by a subclass, so no proxy advises it",
}
PRESENT = "the annotation is on that method, and its presence alone triggers the advice"
EVERYTHING = "Spring Boot proxies all of its beans, so every call to any method is advised"
CALLER_ANNOTATED = "the proxy advises a method only if the caller bean carries the annotation too"
#: Misreadings that apply to each shape, as (applies, reason); all options are 81 characters long.
MISREADINGS: dict[Shape, tuple[tuple[bool, str], ...]] = {
    "external": (
        (False, "the injected reference is the raw target object, and the call skips the proxy"),
        (False, "the proxy advises a method only when the calling bean also has the annotation"),
        (False, "advice runs only for calls made from inside the same bean, never from another"),
    ),
    "self-injection": (
        (False, "a call from inside the bean always runs on `this` and never reaches the proxy"),
        (False, "a bean cannot hold a reference to its own proxy, so the advice is always lost"),
        (False, CALLER_ANNOTATED),
    ),
    "package-private": (
        (False, "advice applies only to `public` methods, whatever the type of proxy is in use"),
        (False, "a class-based proxy can never override a package-visible method of its target"),
        (False, "only methods declared on an interface are advised, whatever the visibility is"),
    ),
    "aspectj": (
        (False, REASON["self-invocation"]),
        (False, "AspectJ mode needs a proxy too, and a call on `this` always misses that proxy"),
        (False, "AspectJ mode advises only calls arriving from another bean, never from `this`"),
    ),
    "self-invocation": (
        (True, PRESENT),
        (True, EVERYTHING),
        (True, "`this` is the proxy inside the bean, so the call is intercepted all the same"),
    ),
    "final": (
        (True, PRESENT),
        (True, EVERYTHING),
        (True, "the call comes in through the proxy, hence the interceptor chain runs for it"),
    ),
    "private": (
        (True, PRESENT),
        (True, EVERYTHING),
        (True, "a class-based proxy can advise `private` methods, so the call is intercepted"),
    ),
}
CALL_PATH: dict[Shape, str] = {
    "external": "the call arrives through the proxy",
    "self-injection": "the call arrives through the proxy held in the self reference",
    "package-private": "the call arrives through the proxy",
    "final": "the call arrives through the proxy",
    "self-invocation": "the call runs on `this`, inside the target object, and never reaches the proxy",
    "private": "the call runs on `this`, inside the target object, and never reaches the proxy",
    "aspectj": "there is no proxy: the advice is woven into the bytecode, so every call is advised",
}
METHOD_ABILITY: dict[Shape, str] = {
    "external": "the method is public, so the proxy can advise it",
    "self-injection": "the method is public, so the proxy can advise it",
    "package-private": "the method is package-visible, which a class-based proxy can advise since 6.0",
    "final": "the method is `final`, so a class-based proxy cannot override or advise it",
    "self-invocation": "the call bypassed the proxy, so the method's visibility does not matter",
    "private": "the method is `private`, so even a proxy could not advise it",
    "aspectj": "woven advice does not depend on overriding the method",
}


@dataclass(frozen=True)
class CallShape:
    shape: Shape
    annotation: str


def _verdict(applies: bool, reason: str) -> str:
    return f"{'Yes' if applies else 'No'}: {reason}"


class ProxyAnnotationGenerator(BackendGenerator[CallShape]):
    id: ClassVar[str] = "proxy-annotation-applies"
    citation: ClassVar[Citation] = Citation(
        "m05-l03",
        "spring-fw-tx-declarative-annotations#using-transactional",
        confirmed=(
            "spring-fw-tx-declarative-annotations#using-transactional; "
            "spring-fw-aop-proxying#aop-understanding-aop-proxies; "
            "spring-fw-aop-proxying#proxying-mechanisms"
        ),
    )

    def scenario(self, rng: random.Random, level: int) -> CallShape:
        shape = rng.choice(LEVEL_SHAPES[level])
        annotation = "@Transactional" if shape in TRANSACTIONAL_ONLY else rng.choice(ANNOTATIONS)
        return CallShape(shape, annotation)

    def stem(self, s: CallShape) -> str:
        return (
            f"A method is annotated {code(s.annotation)}. {CALL[s.shape]} "
            f"Does the advice of the annotation run for this call?"
        )

    def correct(self, s: CallShape) -> str:
        return _verdict(APPLIES[s.shape], REASON[s.shape])

    def mistakes(self, s: CallShape) -> list[str]:
        return [_verdict(applies, reason) for applies, reason in MISREADINGS[s.shape]]

    def explanation(self, s: CallShape) -> str:
        misread = "; ".join(
            f"{_verdict(applies, reason).lower()}" for applies, reason in MISREADINGS[s.shape]
        )
        return (
            f"Inputs: {code(s.annotation)}, call shape: {s.shape}. "
            f"Rule: in proxy mode only calls that come in through the proxy are intercepted, and a proxy "
            f"can advise only the methods it is able to override; the mere presence of the annotation "
            f"is not enough. "
            f"Step 1: {CALL_PATH[s.shape]}. "
            f"Step 2: {METHOD_ABILITY[s.shape]}. "
            f"Result: {_verdict(APPLIES[s.shape], REASON[s.shape])}. "
            f"The other options are misreadings: {misread}. {source_line(self.citation)}"
        )
