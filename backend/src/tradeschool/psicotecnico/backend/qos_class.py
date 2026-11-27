# SPDX-License-Identifier: AGPL-3.0-only
"""`qos-class-pod`: which Pod gets a given Kubernetes QoS class from its containers' requests and limits."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from tradeschool.psicotecnico.backend.base import BackendGenerator, Citation, code
from tradeschool.psicotecnico.backend.source_line import source_line
from tradeschool.psicotecnico.item import Params

ANCHORS = "k8s-qos#criteria; k8s-qos#criteria-1; k8s-qos#criteria-2"
RULE = (
    "Rule: a Pod is `Guaranteed` when every container has a CPU and a memory limit and request, "
    "all greater than zero and each limit equal to its request; `BestEffort` when no container sets any "
    "CPU or memory request or limit; `Burstable` otherwise."
)
KEY_REASON = "every container has equal non-zero CPU and memory requests and limits"
CPUS = ("50m", "250m", "500m", "1000m")
MEMORIES = ("128Mi", "256Mi", "512Mi", "1Gi")

#: One container's (cpu request, cpu limit, memory request, memory limit); None is unset.
Container = tuple[str | None, str | None, str | None, str | None]
Pod = tuple[Container, ...]


@dataclass(frozen=True)
class QosScenario:
    asked: str
    key: Pod
    #: The three shown wrong Pods, each with the fact that rules it out.
    wrong: tuple[tuple[str, Pod], ...]


def qos_class(pod: Pod) -> str:
    if all(_guaranteed(container) for container in pod):
        return "Guaranteed"
    return (
        "Burstable"
        if any(any(value is not None for value in container) for container in pod)
        else "BestEffort"
    )


def _guaranteed(container: Container) -> bool:
    cpu_request, cpu_limit, memory_request, memory_limit = container
    return None not in container and cpu_request == cpu_limit and memory_request == memory_limit


def _equal(cpu: str, memory: str) -> Container:
    return (cpu, cpu, memory, memory)


def _render_container(container: Container) -> str:
    cpu_request, cpu_limit, memory_request, memory_limit = (value or "none" for value in container)
    return f"cpu {cpu_request}/{cpu_limit}, memory {memory_request}/{memory_limit}"


def _render(pod: Pod) -> str:
    return code(" + ".join(_render_container(container) for container in pod))


class QosClassGenerator(BackendGenerator[QosScenario]):
    id: ClassVar[str] = "qos-class-pod"
    levels: ClassVar[tuple[int, ...]] = (1,)
    citation: ClassVar[Citation] = Citation("m10-l03", ANCHORS, confirmed=ANCHORS)

    def scenario_for(self, seed: int, level: int) -> QosScenario:
        scenario = self.build(seed, Params(level)).facts["scenario"]
        assert isinstance(scenario, QosScenario)
        return scenario

    def scenario(self, rng: random.Random, level: int) -> QosScenario | None:
        def settled() -> Pod:
            return tuple(_equal(rng.choice(CPUS), rng.choice(MEMORIES)) for _ in range(level))

        def below_limit() -> Pod:
            cpu, memory = rng.choice(CPUS[:3]), rng.choice(MEMORIES[:3])
            return (
                (cpu, CPUS[CPUS.index(cpu) + 1], memory, MEMORIES[MEMORIES.index(memory) + 1]),
                *settled()[1:],
            )

        def memory_only() -> Pod:
            return ((None, None, *_equal_memory(rng.choice(MEMORIES))), *settled()[1:])

        def requests_only() -> Pod:
            return ((rng.choice(CPUS), None, rng.choice(MEMORIES), None), *settled()[1:])

        key = settled()
        slips = [
            ("its requests are below the limits, but each limit must equal its request", below_limit()),
            ("it has no CPU request or limit, but CPU and memory must both be set", memory_only()),
            ("it has no limits, but a CPU and a memory limit must be set", requests_only()),
            ("no container sets any request or limit", ((None, None, None, None),) * level),
        ]
        wrong = tuple(rng.sample(slips, 3))
        pods = [key, *(pod for _, pod in wrong)]
        if len(set(pods)) != 4:
            return None
        return QosScenario("Guaranteed", key, wrong)

    def stem(self, s: QosScenario) -> str:
        return (
            "Kubernetes gives every Pod a QoS class. Each option lists the containers of one Pod as "
            "request/limit, with `none` for unset. "
            f"Which Pod gets the {code(s.asked)} class?"
        )

    def correct(self, s: QosScenario) -> str:
        return _render(s.key)

    def mistakes(self, s: QosScenario) -> list[str]:
        return [_render(pod) for _, pod in s.wrong]

    def explanation(self, s: QosScenario) -> str:
        key = f"Step 1: {_render(s.key)} is {code(s.asked)}, because {KEY_REASON}."
        refuted = " ".join(
            f"Step {n}: {_render(pod)} is {code(qos_class(pod))}, because {reason}."
            for n, (reason, pod) in enumerate(s.wrong, start=2)
        )
        return f"{RULE} {key} {refuted} Result: {_render(s.key)}. {source_line(self.citation)}"


def _equal_memory(memory: str) -> tuple[str, str]:
    return (memory, memory)
