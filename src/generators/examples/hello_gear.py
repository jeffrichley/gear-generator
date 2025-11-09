from __future__ import annotations

from dataclasses import dataclass

from build123d import BuildPart, Cylinder, Part

from generators.core.utils import measurements


@dataclass(frozen=True)
class HelloGearConfig:
    teeth: int = 20
    module: float = 2.0
    width: float = 8.0


def build_hello_gear(config: HelloGearConfig) -> tuple[Part, measurements.GearMetadata]:
    pitch_diameter = config.module * config.teeth
    radius = pitch_diameter / 2.0

    with BuildPart() as bp:
        Cylinder(radius=radius / 2.0, height=config.width)

    metadata = measurements.compute_gear_metadata(
        module=config.module,
        teeth=config.teeth,
        width=config.width,
    )
    return bp.part, metadata
