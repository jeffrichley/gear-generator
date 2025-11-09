from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable, Sequence

import yaml
from build123d import BuildPart, Cylinder, Locations, Part

DEFAULT_OFFSETS: tuple[float, ...] = (-0.2, -0.1, 0.0, 0.1, 0.2)
COUPON_HEIGHT_MM = 10.0
COUPON_SPACING_MM = 2.0


@dataclass(slots=True)
class CouponMetadata:
    base_diameter: float
    offsets: tuple[float, ...]


@dataclass(slots=True)
class ToleranceMeasurement:
    offset_mm: float
    fit_quality: str
    notes: str | None = None

    def to_dict(self) -> dict[str, object]:
        data: dict[str, object] = {
            "offset_mm": self.offset_mm,
            "fit_quality": self.fit_quality,
        }
        if self.notes:
            data["notes"] = self.notes
        return data

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> ToleranceMeasurement:
        offset_raw = data.get("offset_mm", 0.0)
        fit_quality_raw = data.get("fit_quality", "")
        notes_raw = data.get("notes")
        notes_value = str(notes_raw) if isinstance(notes_raw, str) else None
        if isinstance(offset_raw, (int, float, str)):
            try:
                offset_value = float(offset_raw)
            except ValueError:
                offset_value = 0.0
        else:
            offset_value = 0.0
        return cls(
            offset_mm=offset_value,
            fit_quality=str(fit_quality_raw),
            notes=notes_value,
        )


@dataclass(slots=True)
class ToleranceProfile:
    printer_id: str
    material: str
    measurements: list[ToleranceMeasurement]
    updated_at: str = field(
        default_factory=lambda: datetime.now(UTC).isoformat(timespec="seconds")
    )

    def to_dict(self) -> dict[str, object]:
        return {
            "printer_id": self.printer_id,
            "material": self.material,
            "updated_at": self.updated_at,
            "measurements": [m.to_dict() for m in self.measurements],
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> ToleranceProfile:
        measurements = [
            ToleranceMeasurement.from_dict(entry)
            for entry in data.get("measurements", [])
        ]
        return cls(
            printer_id=str(data["printer_id"]),
            material=str(data["material"]),
            measurements=measurements,
            updated_at=str(data.get("updated_at", datetime.now(UTC).isoformat())),
        )


def generate_coupon(
    diameter: float = 5.0,
    offsets: Sequence[float] = DEFAULT_OFFSETS,
    height: float = COUPON_HEIGHT_MM,
) -> tuple[Part, CouponMetadata]:
    """Create a Build123d model containing columns for each offset."""
    with BuildPart() as bp:
        for index, offset in enumerate(offsets):
            radius = max((diameter + offset) / 2.0, 0.1)
            with Locations((index * (diameter + COUPON_SPACING_MM), 0, 0)):
                Cylinder(radius=radius, height=height)
    metadata = CouponMetadata(base_diameter=diameter, offsets=tuple(offsets))
    return bp.part, metadata


def export_coupon(part: Part, destination: Path) -> None:
    from build123d import export_stl

    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    export_stl(part, str(path))


def save_profile(profile: ToleranceProfile, output_dir: Path) -> Path:
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{profile.printer_id}.yaml"
    path.write_text(yaml.safe_dump(profile.to_dict(), sort_keys=False))
    return path


def load_measurements(path: Path) -> Iterable[ToleranceMeasurement]:
    data = yaml.safe_load(Path(path).read_text())
    entries = data.get("measurements", []) if isinstance(data, dict) else []
    for entry in entries:
        yield ToleranceMeasurement.from_dict(entry)


__all__ = [
    "CouponMetadata",
    "DEFAULT_OFFSETS",
    "export_coupon",
    "generate_coupon",
    "load_measurements",
    "save_profile",
    "ToleranceMeasurement",
    "ToleranceProfile",
]
