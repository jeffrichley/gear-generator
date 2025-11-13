"""Integration tests for the gear plan CLI."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Dict

import pytest
from yaml import safe_dump

from tests.integration import CONFIGS_DIR, gear_cli_args


@pytest.fixture(autouse=True)
def ensure_configs_dir() -> None:
    CONFIGS_DIR.mkdir(parents=True, exist_ok=True)


def write_config(filename: str, payload: Dict[str, object]) -> Path:
    path = CONFIGS_DIR / filename
    path.write_text(safe_dump(payload), encoding="utf-8")
    return path


@pytest.fixture()
def valid_payload() -> Dict[str, object]:
    return {
        "gear_family": "spur",
        "variant_id": "spur_it_01",
        "geometry": {
            "module": 2.0,
            "tooth_count": 28,
            "pressure_angle": 20.0,
            "face_width": 10.0,
            "clearance": 0.15,
        },
        "tolerances": {
            "backlash_target": 0.7,
            "bore_offset": 0.1,
            "tooth_profile_scale": 0.985,
        },
        "materials": {"default": "PLA_PLUS"},
    }


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=False, capture_output=True, text=True)


def test_validate_command_emits_json_on_success(valid_payload: Dict[str, object]) -> None:
    config_path = write_config("spur_valid.yaml", valid_payload)
    result = run_cli(*gear_cli_args("gear", "plan", "validate", config=config_path.name, extra=["--format", "json"]))
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["status"] == "valid"


def test_validate_command_returns_errors_on_failure(valid_payload: Dict[str, object]) -> None:
    valid_payload["tolerances"] = {"backlash_target": 1.4}
    config_path = write_config("spur_invalid.yaml", valid_payload)
    result = run_cli(*gear_cli_args("gear", "plan", "validate", config=config_path.name))
    assert result.returncode == 1
    assert "backlash" in result.stderr.lower()


def test_export_command_accepts_minimal_arguments(valid_payload: Dict[str, object]) -> None:
    config_path = write_config("spur_export.yaml", valid_payload)
    result = run_cli(*gear_cli_args("gear", "plan", "export", config=config_path.name, extra=["--formats", "stl", "json"]))
    assert result.returncode == 0
    assert "queued export" in result.stdout.lower()
