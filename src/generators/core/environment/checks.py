"""Environment verification utilities."""

from __future__ import annotations

import os
import platform
from dataclasses import dataclass, field
from datetime import UTC, datetime
from importlib import metadata
from typing import Sequence, cast

REQUIRED_PACKAGES: tuple[str, ...] = (
    "build123d",
    "cadquery",
    "numpy",
    "pyyaml",
    "rich",
    "typer",
)


@dataclass(slots=True)
class PackageRecord:
    name: str
    version: str | None
    status: str

    def to_dict(self) -> dict[str, str | None]:
        return {"name": self.name, "version": self.version, "status": self.status}

    @classmethod
    def from_dict(cls, data: dict[str, str | None]) -> PackageRecord:
        return cls(
            name=str(data["name"]),
            version=data.get("version"),
            status=str(data["status"]),
        )


@dataclass(slots=True)
class EnvironmentProfile:
    os_name: str
    os_version: str
    python_version: str
    uv_active: bool
    packages: list[PackageRecord] = field(default_factory=list)
    verification_timestamp: str = field(
        default_factory=lambda: datetime.now(UTC).isoformat(timespec="seconds")
    )
    status: str = "pending"

    def to_dict(self) -> dict[str, object]:
        return {
            "osName": self.os_name,
            "osVersion": self.os_version,
            "pythonVersion": self.python_version,
            "uvActive": self.uv_active,
            "packages": [record.to_dict() for record in self.packages],
            "verificationTimestamp": self.verification_timestamp,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> EnvironmentProfile:
        raw_packages = cast("Sequence[dict[str, str | None]]", data.get("packages", []))
        packages = [PackageRecord.from_dict(item) for item in raw_packages]
        return cls(
            os_name=str(data["osName"]),
            os_version=str(data["osVersion"]),
            python_version=str(data["pythonVersion"]),
            uv_active=bool(data["uvActive"]),
            packages=packages,
            verification_timestamp=str(
                data.get("verificationTimestamp", datetime.now(UTC).isoformat())
            ),
            status=str(data["status"]),
        )


def collect_environment_profile() -> EnvironmentProfile:
    python_version = platform.python_version()
    os_name = platform.system()
    os_version = platform.release()
    uv_active = bool(os.environ.get("VIRTUAL_ENV"))

    packages = list(_gather_package_records(REQUIRED_PACKAGES))

    status = (
        "ready"
        if all(pkg.status == "installed" for pkg in packages)
        else "missing-deps"
    )

    return EnvironmentProfile(
        os_name=os_name,
        os_version=os_version,
        python_version=python_version,
        uv_active=uv_active,
        packages=packages,
        status=status,
    )


def _gather_package_records(packages: tuple[str, ...]) -> list[PackageRecord]:
    records: list[PackageRecord] = []
    for name in packages:
        try:
            version = metadata.version(name)
            records.append(
                PackageRecord(name=name, version=version, status="installed")
            )
        except metadata.PackageNotFoundError:
            records.append(PackageRecord(name=name, version=None, status="missing"))
    return records


__all__ = [
    "EnvironmentProfile",
    "PackageRecord",
    "REQUIRED_PACKAGES",
    "collect_environment_profile",
]
