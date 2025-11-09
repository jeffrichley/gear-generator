from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Material:
    name: str
    density_g_cm3: float
    tensile_strength_mpa: float | None = None


STANDARD_MATERIALS: dict[str, Material] = {
    "PLA+": Material(name="PLA+", density_g_cm3=1.24, tensile_strength_mpa=60),
    "PETG": Material(name="PETG", density_g_cm3=1.27, tensile_strength_mpa=50),
    "ASA": Material(name="ASA", density_g_cm3=1.07, tensile_strength_mpa=45),
    "Nylon": Material(name="Nylon", density_g_cm3=1.15, tensile_strength_mpa=75),
    "Nylon-CF": Material(name="Nylon-CF", density_g_cm3=1.20, tensile_strength_mpa=110),
}


def get_material(name: str) -> Material:
    try:
        return STANDARD_MATERIALS[name]
    except KeyError as exc:
        raise ValueError(f"Unknown material: {name}") from exc


__all__ = ["get_material", "Material", "STANDARD_MATERIALS"]
