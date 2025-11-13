"""Gear planning integration-test scaffolding."""

from __future__ import annotations

from pathlib import Path
from typing import Sequence, Tuple
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIGS_DIR = PROJECT_ROOT / "configs"
CLI_ENTRYPOINT = "generators.cli.main"

pytestmark = pytest.mark.integration


def gear_cli_args(*subcommands: str, config: str | None = None, extra: Sequence[str] | None = None) -> Tuple[str, ...]:
    """Compose CLI arguments for the gear planning Typer app."""
    base: list[str] = [sys.executable, "-m", CLI_ENTRYPOINT]
    base.extend(subcommands)
    if config:
        base.extend(["--config", str((CONFIGS_DIR / config).resolve())])
    if extra:
        base.extend(extra)
    return tuple(base)


def ensure_config_path(relative_name: str) -> Path:
    """Resolve and validate config path for integration scenarios."""
    candidate = CONFIGS_DIR / relative_name
    if not candidate.exists():
        raise FileNotFoundError(f"Missing integration config: {candidate}")
    return candidate.resolve()


def project_path(relative: str) -> Path:
    """Resolve a path relative to the project root for process helpers."""
    return (PROJECT_ROOT / relative).resolve()


__all__ = [
    "CLI_ENTRYPOINT",
    "CONFIGS_DIR",
    "PROJECT_ROOT",
    "ensure_config_path",
    "gear_cli_args",
    "project_path",
    "pytestmark",
]
