"""Gear planning unit-test scaffolding."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import pytest
from yaml import safe_load

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIGS_DIR = PROJECT_ROOT / "configs"

pytestmark = pytest.mark.unit


def load_config_fixture(relative_name: str) -> Dict[str, Any]:
    """Load a YAML configuration fixture residing under ``configs/``."""
    candidate = CONFIGS_DIR / relative_name
    if not candidate.exists():
        raise FileNotFoundError(f"Missing gear config fixture: {candidate}")
    with candidate.open("r", encoding="utf-8") as stream:
        data = safe_load(stream) or {}
    if not isinstance(data, dict):
        raise TypeError(f"Expected mapping in {candidate}, received {type(data)!r}")
    return data


__all__ = ["CONFIGS_DIR", "PROJECT_ROOT", "load_config_fixture", "pytestmark"]
