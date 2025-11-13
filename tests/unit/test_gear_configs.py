"""Baseline gear planning unit tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import pytest
from yaml import safe_dump

from generators.core.utils.tolerances import angular_backlash_adjust, fit_clearance, press_fit
from generators.gearboxes import schema


@pytest.fixture()
def sample_config() -> Dict[str, Any]:
    return {
        "gear_family": "spur",
        "variant_id": "spur_28_proto",
        "geometry": {
            "module": 2.0,
            "tooth_count": 28,
            "pressure_angle": 20.0,
            "face_width": 12.0,
            "clearance": 0.15,
        },
        "tolerances": {
            "backlash_target": 0.7,
            "bore_offset": 0.12,
            "tooth_profile_scale": 0.985,
        },
        "materials": {"default": "PLA_PLUS"},
        "validation": {"test_pair": {"reference": "spur_ref_28"}},
        "metadata": {"authors": ["QA"], "revision": "0.1.0"},
    }


def write_yaml(path: Path, payload: Dict[str, Any]) -> Path:
    path.write_text(safe_dump(payload), encoding="utf-8")
    return path


class TestToleranceHelpers:
    def test_fit_clearance_scales_with_diameter(self) -> None:
        small = fit_clearance(6.0, profile="standard")
        large = fit_clearance(22.0, profile="standard")
        assert pytest.approx(large, rel=0.1) > small

    def test_press_fit_returns_negative_offset(self) -> None:
        offset = press_fit(10.0)
        assert offset < 0
        tighter = press_fit(18.0)
        assert offset < 0 and tighter <= offset

    def test_angular_backlash_adjust_converts_degrees_to_mm(self) -> None:
        clearance = angular_backlash_adjust(module=2.0, backlash_target=0.7)
        assert clearance > 0
        doubled = angular_backlash_adjust(module=2.0, backlash_target=1.4)
        assert pytest.approx(doubled, rel=0.05) == pytest.approx(clearance * 2, rel=0.05)


class TestConfigSchema:
    def test_load_config_reads_yaml_file(self, tmp_path: Path, sample_config: Dict[str, Any]) -> None:
        config_path = write_yaml(tmp_path / "gear.yaml", sample_config)
        loaded = schema.load_config(config_path)
        assert loaded["gear_family"] == "spur"
        assert loaded["geometry"]["module"] == pytest.approx(2.0)

    def test_load_config_rejects_missing_required_fields(self, tmp_path: Path, sample_config: Dict[str, Any]) -> None:
        sample_config.pop("geometry")
        config_path = write_yaml(tmp_path / "gear.yaml", sample_config)
        with pytest.raises(schema.GearConfigError):
            schema.load_config(config_path)

    def test_validate_config_identifies_backlash_violations(self, sample_config: Dict[str, Any]) -> None:
        sample_config["tolerances"]["backlash_target"] = 1.6
        is_valid, errors = schema.validate_config(sample_config)
        assert not is_valid
        assert any("backlash" in message.lower() for message in errors)

    def test_validate_config_success_path(self, sample_config: Dict[str, Any]) -> None:
        is_valid, errors = schema.validate_config(sample_config)
        assert is_valid
        assert errors == []

    def test_validate_config_requires_helix_angle_for_helical(self, sample_config: Dict[str, Any]) -> None:
        sample_config["gear_family"] = "helical"
        sample_config["geometry"].pop("clearance", None)
        sample_config["geometry"].setdefault("helix_angle", 20.0)
        is_valid, errors = schema.validate_config(sample_config)
        assert not is_valid
        assert any("helix" in message.lower() for message in errors)
