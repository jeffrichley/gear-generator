"""Tolerance helper utilities for gear planning workflows."""

from __future__ import annotations

import math
from typing import Final

__all__ = ["fit_clearance", "press_fit", "angular_backlash_adjust"]

_PROFILE_CLEARANCE_FACTORS: Final[dict[str, float]] = {
    "fine": 0.08,
    "standard": 0.12,
    "coarse": 0.18,
}

_PRESS_FIT_BASE: Final[float] = 0.05
_PRESS_FIT_MULTIPLIER: Final[float] = 0.0015
_BACKLASH_MIN_DEGREES: Final[float] = 0.1


def fit_clearance(diameter: float, *, profile: str = "standard") -> float:
    """Return the positive clearance (mm) for a slip-fit bore."""
    if diameter <= 0:
        raise ValueError("Diameter must be greater than zero for fit clearance calculations.")
    baseline = _PROFILE_CLEARANCE_FACTORS.get(profile.lower(), _PROFILE_CLEARANCE_FACTORS["standard"])
    clearance = baseline + (diameter * 0.002)
    return round(clearance, 4)


def press_fit(diameter: float) -> float:
    """Return the negative offset (mm) required for a press-fit bore."""
    if diameter <= 0:
        raise ValueError("Diameter must be greater than zero for press-fit calculations.")
    offset = -(_PRESS_FIT_BASE + (diameter * _PRESS_FIT_MULTIPLIER))
    return round(offset, 4)


def angular_backlash_adjust(*, module: float, backlash_target: float) -> float:
    """Convert an angular backlash target (degrees) into linear clearance (mm)."""
    if module <= 0:
        raise ValueError("Module must be positive for backlash adjustment calculations.")
    if backlash_target <= 0:
        raise ValueError("Backlash target must be positive.")
    target = max(backlash_target, _BACKLASH_MIN_DEGREES)
    clearance = (math.pi * module) * (target / 360.0)
    return round(clearance, 5)
