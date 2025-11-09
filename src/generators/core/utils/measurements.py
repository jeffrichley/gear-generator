from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GearMetadata:
    pitch_diameter: float
    module: float
    teeth: int
    face_width: float


def compute_gear_metadata(module: float, teeth: int, width: float) -> GearMetadata:
    pitch_diameter = module * teeth
    return GearMetadata(
        pitch_diameter=pitch_diameter,
        module=module,
        teeth=teeth,
        face_width=width,
    )


__all__ = ["GearMetadata", "compute_gear_metadata"]
