"""Shared configuration schema utilities for gear planning."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, Tuple

from yaml import safe_load

ALLOWED_GEAR_FAMILIES = {"spur", "helical"}
BACKLASH_RANGE = (0.5, 1.0)
HELIX_RANGE = (-15.0, 15.0)
PRESSURE_ANGLE_RANGE = (14.5, 25.0)
MODULE_RANGE = (0.2, 10.0)
FACE_WIDTH_RANGE = (1.0, 50.0)


class GearConfigError(ValueError):
    """Raised when a configuration cannot be parsed or fails basic validation."""


def load_config(path: str | Path) -> Dict[str, Any]:
    """Load a gear configuration from YAML and enforce required structure."""
    config_path = Path(path)
    if not config_path.exists():
        raise GearConfigError(f"Configuration file does not exist: {config_path}")
    data = safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise GearConfigError("Configuration must be a mapping at the top level.")
    errors = list(_validate_required_keys(data))
    if errors:
        raise GearConfigError("; ".join(errors))
    return data


def validate_config(config: Dict[str, Any]) -> Tuple[bool, list[str]]:
    """Validate a loaded configuration and return status plus error messages."""
    errors: list[str] = []

    gear_family = str(config.get("gear_family", "")).lower()
    if gear_family not in ALLOWED_GEAR_FAMILIES:
        errors.append("gear_family must be one of: spur, helical")

    geometry = _as_mapping(config.get("geometry"))
    tolerances = _as_mapping(config.get("tolerances"))
    materials = _as_mapping(config.get("materials"))

    module = _coerce_float(geometry.get("module"))
    if module is None or not MODULE_RANGE[0] <= module <= MODULE_RANGE[1]:
        errors.append("geometry.module must be between 0.2 and 10.0")

    tooth_count = geometry.get("tooth_count")
    if not isinstance(tooth_count, int) or tooth_count <= 0:
        errors.append("geometry.tooth_count must be a positive integer")

    pressure_angle = _coerce_float(geometry.get("pressure_angle"))
    if (
        pressure_angle is None
        or not PRESSURE_ANGLE_RANGE[0] <= pressure_angle <= PRESSURE_ANGLE_RANGE[1]
    ):
        errors.append("geometry.pressure_angle must be 14.5°–25°")

    face_width = _coerce_float(geometry.get("face_width"))
    if face_width is None or not FACE_WIDTH_RANGE[0] <= face_width <= FACE_WIDTH_RANGE[1]:
        errors.append("geometry.face_width must be between 1 and 50 mm")

    backlash = _coerce_float(tolerances.get("backlash_target"))
    if backlash is None or not BACKLASH_RANGE[0] <= backlash <= BACKLASH_RANGE[1]:
        errors.append("tolerances.backlash_target must be 0.5°–1.0°")

    if "default" not in materials:
        errors.append("materials.default is required")

    if gear_family == "helical":
        helix_angle = _coerce_float(geometry.get("helix_angle"))
        if helix_angle is None:
            errors.append("geometry.helix_angle is required for helical gears")
        elif not HELIX_RANGE[0] <= helix_angle <= HELIX_RANGE[1]:
            errors.append(
                "geometry.helix_angle must be between -15° and 15° for helical gears"
            )

    return (len(errors) == 0, errors)


def _validate_required_keys(config: Dict[str, Any]) -> Iterable[str]:
    if "gear_family" not in config:
        yield "gear_family is required"
    if "geometry" not in config or not isinstance(config["geometry"], dict):
        yield "geometry mapping is required"
    if "tolerances" not in config or not isinstance(config["tolerances"], dict):
        yield "tolerances mapping is required"
    if "materials" not in config or not isinstance(config["materials"], dict):
        yield "materials mapping is required"


def _as_mapping(value: Any) -> Dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _coerce_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


__all__ = [
    "ALLOWED_GEAR_FAMILIES",
    "BACKLASH_RANGE",
    "GearConfigError",
    "HELIX_RANGE",
    "load_config",
    "validate_config",
]
