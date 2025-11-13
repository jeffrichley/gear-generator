"""Shared gear planning package scaffolding.

This package centralizes registration for gear builders and validation hooks so
spur, helical, and future gear families can plug in incrementally during the
feature rollout."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, Dict, Iterable, List, MutableMapping, Tuple, Union

GearConfig = Mapping[str, Any]
GearBuilder = Callable[[GearConfig], Any]
GearValidator = Callable[[GearConfig], Tuple[bool, List[str]]]


class GearRegistry:
    """In-memory registry for gear planning behaviors."""

    def __init__(self) -> None:
        self._builders: Dict[str, GearBuilder] = {}
        self._validators: Dict[str, GearValidator] = {}

    def register_builder(self, gear_family: str, builder: GearBuilder, *, overwrite: bool = False) -> None:
        """Register a builder callable for a gear family."""
        normalized = gear_family.lower()
        if not overwrite and normalized in self._builders:
            raise ValueError(f"Builder already registered for gear family '{normalized}'.")
        self._builders[normalized] = builder

    def register_validator(self, gear_family: str, validator: GearValidator, *, overwrite: bool = False) -> None:
        """Register a validation callable for a gear family."""
        normalized = gear_family.lower()
        if not overwrite and normalized in self._validators:
            raise ValueError(f"Validator already registered for gear family '{normalized}'.")
        self._validators[normalized] = validator

    def get_builder(self, gear_family: str) -> GearBuilder:
        """Return the builder for the requested gear family."""
        normalized = gear_family.lower()
        try:
            return self._builders[normalized]
        except KeyError as exc:
            raise KeyError(f"No builder registered for gear family '{normalized}'.") from exc

    def get_validator(self, gear_family: str) -> GearValidator:
        """Return the validator for the requested gear family."""
        normalized = gear_family.lower()
        try:
            return self._validators[normalized]
        except KeyError as exc:
            raise KeyError(f"No validator registered for gear family '{normalized}'.") from exc

    def remove_builder(self, gear_family: str) -> None:
        """Remove a registered builder if present."""
        self._builders.pop(gear_family.lower(), None)

    def remove_validator(self, gear_family: str) -> None:
        """Remove a registered validator if present."""
        self._validators.pop(gear_family.lower(), None)

    def registered_families(self) -> Tuple[str, ...]:
        """Return a sorted tuple of all registered gear families."""
        families = {*(self._builders.keys()), *(self._validators.keys())}
        return tuple(sorted(families))

    def builders(self) -> MutableMapping[str, GearBuilder]:
        """Expose the builder registry for inspection or bulk operations."""
        return self._builders

    def validators(self) -> MutableMapping[str, GearValidator]:
        """Expose the validator registry for inspection or bulk operations."""
        return self._validators

    def clear(self) -> None:
        """Remove all registered builders and validators."""
        self._builders.clear()
        self._validators.clear()

    def items(self) -> Iterable[Tuple[str, Union[GearBuilder, None], Union[GearValidator, None]]]:
        """Yield gear families with their builder and validator (if both registered)."""
        families = self.registered_families()
        for family in families:
            yield (
                family,
                self._builders.get(family),
                self._validators.get(family),
            )


registry = GearRegistry()

__all__ = [
    "GearBuilder",
    "GearConfig",
    "GearRegistry",
    "GearValidator",
    "registry",
]
