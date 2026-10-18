# SPDX-License-Identifier: AGPL-3.0-only
"""Content YAML read through libyaml's C parser, ten times faster than PyYAML's pure-Python one."""

from __future__ import annotations

from pathlib import Path

import yaml


def read_yaml(path: Path) -> object:
    with path.open(encoding="utf-8") as fh:
        return yaml.load(fh, Loader=yaml.CSafeLoader)
