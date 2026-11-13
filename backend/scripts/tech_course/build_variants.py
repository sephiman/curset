# SPDX-License-Identifier: AGPL-3.0-only
"""Build-time variant families (requirements 6.2): a template and a parameter grid become questions.

    uv run python -m scripts.tech_course.build_variants [--course C] [--family NAME] [--timeout SECONDS]

A family is `variants/<family>.yaml`. Placeholders are `@@name@@`. Every grid point is instantiated and run on
the pinned toolchain; its stdout is the key. Each distractor is the stdout of the same program with one
typical mistake applied (`replace: [from, to]`); a variant without three distinct distractors is left out.
The quiz goes to `exercises/<exercise>.yaml`; its evidence (source hash, command, output hashes) to
`variants/<family>.runs.json`.
"""

from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from scripts.tech_course.lessons import add_course_argument, course_dir
from scripts.tech_course.run_snippets import (
    DEFAULT_TIMEOUT,
    RunRecord,
    Toolchain,
    build_toolchain,
    require_isolation,
    run_source,
)
from scripts.tech_course.toolchain import pinned

OPTION_IDS = "abcd"
DISTRACTORS_NEEDED = len(OPTION_IDS) - 1
_PLACEHOLDER = re.compile(r"@@(\w+)@@")


@dataclass(frozen=True)
class Mistake:
    name: str
    old: str
    new: str


@dataclass(frozen=True)
class Family:
    name: str
    exercise: str
    lesson: str
    citation: str
    file: str
    prompt: str
    template: str
    explanation: str
    grid: dict[str, list[object]]
    mistakes: list[Mistake]
    difficulty: int
    tags: list[str]


@dataclass(frozen=True)
class Variant:
    id: str
    params: dict[str, object]
    source: str
    key: RunRecord
    distractors: list[tuple[Mistake, RunRecord]]


def load_family(path: Path) -> Family:
    raw: Mapping[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    return Family(
        name=path.stem,
        exercise=raw["exercise"],
        lesson=raw["lesson"],
        citation=raw["citation"],
        file=raw["file"],
        prompt=raw["prompt"],
        template=raw["template"],
        explanation=raw["explanation"],
        grid={name: list(values) for name, values in raw["parameters"].items()},
        mistakes=[Mistake(m["name"], m["replace"][0], m["replace"][1]) for m in raw["mistakes"]],
        difficulty=int(raw.get("difficulty", 2)),
        tags=list(raw.get("tags", [])),
    )


def fill(text: str, values: Mapping[str, object]) -> str:
    return _PLACEHOLDER.sub(lambda match: str(values[match[1]]), text)


def grid_points(grid: Mapping[str, list[object]]) -> list[dict[str, object]]:
    names = list(grid)
    return [dict(zip(names, combo, strict=True)) for combo in itertools.product(*grid.values())]


def mutant(source: str, mistake: Mistake, params: Mapping[str, object]) -> str | None:
    """The program with the mistake applied once; None when the mistake does not apply to it."""
    old, new = fill(mistake.old, params), fill(mistake.new, params)
    return source.replace(old, new, 1) if old in source else None


def pick_distractors(
    family: Family,
    params: Mapping[str, object],
    source: str,
    key: RunRecord,
    toolchain: Toolchain,
    timeout: int,
) -> list[tuple[Mistake, RunRecord]]:
    picked: list[tuple[Mistake, RunRecord]] = []
    seen = {key.stdout.strip()}
    for mistake in family.mistakes:
        changed = mutant(source, mistake, params)
        if changed is None:
            continue
        result = run_source(family.file, changed, toolchain, timeout)
        answer = result.stdout.strip()
        if result.exit_code != 0 or not answer or answer in seen:
            continue
        seen.add(answer)
        picked.append((mistake, result))
        if len(picked) == DISTRACTORS_NEEDED:
            break
    return picked


def build_family(
    family: Family, toolchain: Toolchain, timeout: int = DEFAULT_TIMEOUT
) -> tuple[list[Variant], list[str]]:
    variants: list[Variant] = []
    skipped: list[str] = []
    for params in grid_points(family.grid):
        source = fill(family.template, params)
        label = ", ".join(f"{k}={v}" for k, v in params.items())
        key = run_source(family.file, source, toolchain, timeout)
        if key.exit_code != 0 or not key.stdout.strip():
            skipped.append(f"{family.name} ({label}): the program does not print")
            continue
        distractors = pick_distractors(family, params, source, key, toolchain, timeout)
        if len(distractors) < DISTRACTORS_NEEDED:
            skipped.append(f"{family.name} ({label}): {len(distractors)} distinct distractors")
            continue
        variants.append(
            Variant(
                f"{family.lesson}-v-{family.name}-{len(variants) + 1:03d}", params, source, key, distractors
            )
        )
    return variants, skipped


# --- output --------------------------------------------------------------------------------------------


def as_code(stdout: str) -> str:
    return ", ".join(f"`{line.strip()}`" for line in stdout.strip().splitlines())


def quiz_variant(family: Family, variant: Variant, position: int) -> dict[str, object]:
    answers = [variant.key.stdout, *(record.stdout for _, record in variant.distractors)]
    answers.insert(position, answers.pop(0))
    language = "kotlin" if family.file.endswith(".kt") else "java"
    return {
        "id": variant.id,
        "prompt": {"en": f"{family.prompt}\n\n```{language}\n{variant.source.strip()}\n```"},
        "options": [
            {
                "id": OPTION_IDS[i],
                "text": {"en": as_code(text)},
                **({"correct": True} if i == position else {}),
            }
            for i, text in enumerate(answers)
        ],
        "explanation": {
            "en": fill(family.explanation, {**variant.params, "key": as_code(variant.key.stdout)})
        },
        "citation": family.citation,
        "difficulty": family.difficulty,
        "tags": family.tags,
    }


def evidence(variant: Variant) -> dict[str, object]:
    return {
        "id": variant.id,
        "params": variant.params,
        "source_sha256": variant.key.snippet_sha256,
        "commands": variant.key.commands,
        "stdout_sha256": variant.key.stdout_sha256,
        "java": variant.key.java,
        "distractors": [
            {"mistake": m.name, "stdout_sha256": r.stdout_sha256} for m, r in variant.distractors
        ],
    }


class _Dumper(yaml.SafeDumper):
    pass


def _literal(dumper: yaml.SafeDumper, text: str) -> yaml.ScalarNode:
    style = "|" if "\n" in text else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", text, style=style)


_Dumper.add_representer(str, _literal)


def write_outputs(course: str, family: Family, variants: list[Variant]) -> tuple[Path, Path]:
    quiz = [quiz_variant(family, variant, index % len(OPTION_IDS)) for index, variant in enumerate(variants)]
    header = (
        "# SPDX-License-Identifier: AGPL-3.0-only\n"
        f"# Generated by build_variants.py from variants/{family.name}.yaml; edit the family.\n"
    )
    root = course_dir(course)
    exercise = root / "exercises" / f"{family.exercise}.yaml"
    runs = root / "variants" / f"{family.name}.runs.json"
    exercise.parent.mkdir(parents=True, exist_ok=True)
    runs.parent.mkdir(parents=True, exist_ok=True)
    body = yaml.dump(
        {"type": "quiz", "variants": quiz}, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=120
    )
    exercise.write_text(header + body, encoding="utf-8")
    runs.write_text(json.dumps([evidence(v) for v in variants], indent=1) + "\n", encoding="utf-8")
    return exercise, runs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_course_argument(parser)
    parser.add_argument("--family")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    args = parser.parse_args(argv)
    paths = sorted((course_dir(args.course) / "variants").glob(f"{args.family or '*'}.yaml"))
    if not paths:
        print("build_variants: no families")
        return 0
    families = [load_family(path) for path in paths]
    require_isolation()
    toolchain = build_toolchain(pinned(args.course), any(f.file.endswith(".kt") for f in families))
    status = 0
    for family in families:
        variants, skipped = build_family(family, toolchain, args.timeout)
        for line in skipped:
            print(f"skipped {line}")
        exercise, _ = write_outputs(args.course, family, variants)
        print(f"build_variants: {family.name}: {len(variants)} variants -> {exercise}")
        status = status or int(not variants)
    return status


if __name__ == "__main__":
    sys.exit(main())
