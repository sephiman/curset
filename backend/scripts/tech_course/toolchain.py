# SPDX-License-Identifier: AGPL-3.0-only
"""The pinned JDK and Kotlin compiler of `sources/versions.yaml`; nothing else may run a snippet.

    uv run python -m scripts.tech_course.toolchain provision [--course backend-in-depth]

Java is matched on dotted components: the pin `25.0.5` accepts `25.0.5` and `25.0.5.0.3`, not `25.0.50`.
Kotlin is provisioned from the official JetBrains release into `~/.cache/curset/toolchains/`, after its
published sha256 matches; any version but the pinned one is refused.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path

import yaml

from scripts.tech_course.lessons import DEFAULT_COURSE, add_course_argument, course_dir

CACHE = Path.home() / ".cache" / "curset" / "toolchains"
RELEASE = "https://github.com/JetBrains/kotlin/releases/download/v{v}/kotlin-compiler-{v}.zip"
_JAVA_VERSION = re.compile(r'version "(?P<v>[^"]+)"')
_KOTLIN_VERSION = re.compile(r"kotlinc-jvm (?P<v>\S+)")


class ToolchainError(RuntimeError):
    pass


@dataclass(frozen=True)
class Pins:
    java: str
    kotlin: str


def pinned(course: str = DEFAULT_COURSE) -> Pins:
    loaded = yaml.safe_load((course_dir(course) / "sources" / "versions.yaml").read_text(encoding="utf-8"))
    products = {str(p["product"]): str(p["version"]) for p in loaded["products"]}
    java = max((v for name, v in products.items() if name.startswith("Java")), key=len)
    return Pins(java=java, kotlin=products["Kotlin"])


def java_matches(reported: str, pin: str) -> bool:
    return reported == pin or reported.startswith(f"{pin}.")


def java_version() -> str:
    result = subprocess.run(["java", "-version"], capture_output=True, text=True, check=False)
    found = _JAVA_VERSION.search(result.stderr)
    if found is None:
        raise ToolchainError("java -version printed no version")
    return found["v"]


def checked_java(pins: Pins) -> str:
    reported = java_version()
    if not java_matches(reported, pins.java):
        raise ToolchainError(f"java reports {reported}, the course pins {pins.java}")
    return reported


def kotlin_home(version: str) -> Path:
    return CACHE / f"kotlinc-{version}" / "kotlinc"


def kotlinc_version(home: Path) -> str:
    result = subprocess.run(
        [str(home / "bin" / "kotlinc"), "-version"], capture_output=True, text=True, check=False
    )
    found = _KOTLIN_VERSION.search(result.stderr + result.stdout)
    if found is None:
        raise ToolchainError(f"{home}: kotlinc printed no version")
    return found["v"]


def checked_kotlin(pins: Pins, home: Path | None = None) -> tuple[Path, str]:
    home = home or kotlin_home(pins.kotlin)
    if not (home / "bin" / "kotlinc").exists():
        raise ToolchainError(f"Kotlin {pins.kotlin} is not provisioned: run the toolchain provision command")
    reported = kotlinc_version(home)
    if reported != pins.kotlin:
        raise ToolchainError(f"kotlinc reports {reported}, the course pins {pins.kotlin}")
    return home, reported


def provision_kotlin(pins: Pins, version: str | None = None) -> Path:
    if version not in (None, pins.kotlin):
        raise ToolchainError(f"refusing Kotlin {version}: the course pins {pins.kotlin}")
    url = RELEASE.format(v=pins.kotlin)
    archive = CACHE / f"kotlin-compiler-{pins.kotlin}.zip"
    CACHE.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, archive)
    with urllib.request.urlopen(f"{url}.sha256") as response:
        published = response.read().decode().split()[0]
    actual = hashlib.sha256(archive.read_bytes()).hexdigest()
    if actual != published:
        archive.unlink()
        raise ToolchainError(f"sha256 of {archive.name} is {actual}, the release publishes {published}")
    _extract(archive, kotlin_home(pins.kotlin).parent)
    return kotlin_home(pins.kotlin)


def _extract(archive: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as bundle:
        for member in bundle.infolist():
            if not (destination / member.filename).resolve().is_relative_to(destination.resolve()):
                raise ToolchainError(f"{archive.name}: member {member.filename} escapes the folder")
        bundle.extractall(destination)
    for binary in (destination / "kotlinc" / "bin").iterdir():
        binary.chmod(0o755)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["provision", "show"])
    add_course_argument(parser)
    args = parser.parse_args(argv)
    pins = pinned(args.course)
    if args.command == "provision":
        provision_kotlin(pins)
    home, kotlin = checked_kotlin(pins)
    print(f"java {checked_java(pins)}; kotlin {kotlin} at {home}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ToolchainError as exc:
        print(f"toolchain: {exc}", file=sys.stderr)
        sys.exit(2)
