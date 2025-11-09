"""Repository scaffold validation and generation."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path

from generators.core.environment import checks


@dataclass(frozen=True)
class PathRequirement:
    path: str
    kind: str  # "directory" or "file"
    description: str
    placeholder_text: str | None = None


@dataclass(slots=True)
class ScaffoldResult:
    path: str
    state: str  # present | missing | unexpected
    notes: str | None = None


@dataclass(slots=True)
class ScaffoldReport:
    status: str
    checked_at: str
    results: list[ScaffoldResult]

    def to_dict(self) -> dict[str, object]:
        return {
            "status": self.status,
            "checkedAt": self.checked_at,
            "results": [asdict(result) for result in self.results],
        }


REQUIRED_PATHS: tuple[PathRequirement, ...] = (
    PathRequirement(
        "src/generators", "directory", "Root package for CLI and utilities"
    ),
    PathRequirement("src/generators/cli", "directory", "Typer CLI package"),
    PathRequirement("src/generators/core", "directory", "Core utilities package"),
    PathRequirement(
        "src/generators/core/environment", "directory", "Environment tooling"
    ),
    PathRequirement("src/generators/core/utils", "directory", "Shared utility helpers"),
    PathRequirement("src/generators/gears", "directory", "Gear generators staging"),
    PathRequirement("src/generators/motors", "directory", "Motor generators staging"),
    PathRequirement("examples", "directory", "Example scripts"),
    PathRequirement("outputs/examples", "directory", "Generated artifacts"),
    PathRequirement("tests/unit", "directory", "Unit tests"),
    PathRequirement("tests/integration", "directory", "Integration tests"),
    PathRequirement("tests/fixtures", "directory", "Shared fixtures"),
    PathRequirement("configs", "directory", "Configuration files"),
    PathRequirement("data", "directory", "Data assets and calibration"),
    PathRequirement("docs", "directory", "MkDocs documentation"),
    PathRequirement(
        "docs/README.md", "file", "Developer documentation index", "# Documentation\n"
    ),
)


def validate_structure(root: Path, autofix: bool = False) -> ScaffoldReport:
    results: list[ScaffoldResult] = []
    for requirement in REQUIRED_PATHS:
        target = root / requirement.path
        if requirement.kind == "directory":
            if target.exists() and target.is_dir():
                results.append(ScaffoldResult(path=requirement.path, state="present"))
            else:
                if autofix:
                    target.mkdir(parents=True, exist_ok=True)
                    results.append(
                        ScaffoldResult(
                            path=requirement.path, state="present", notes="created"
                        )
                    )
                else:
                    results.append(
                        ScaffoldResult(path=requirement.path, state="missing")
                    )
        else:
            if target.exists():
                results.append(ScaffoldResult(path=requirement.path, state="present"))
            else:
                if autofix:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    text = requirement.placeholder_text or ""
                    target.write_text(text)
                    results.append(
                        ScaffoldResult(
                            path=requirement.path, state="present", notes="created"
                        )
                    )
                else:
                    results.append(
                        ScaffoldResult(path=requirement.path, state="missing")
                    )

    missing = any(result.state == "missing" for result in results)
    status = "fail" if missing else "pass"
    return ScaffoldReport(
        status=status,
        checked_at=datetime.now(UTC).isoformat(timespec="seconds"),
        results=results,
    )


def ensure_structure(root: Path, autofix: bool = False) -> ScaffoldReport:
    return validate_structure(root, autofix=autofix)


def default_root() -> Path:
    return Path.cwd()


def required_package_names() -> tuple[str, ...]:
    return checks.REQUIRED_PACKAGES


__all__ = [
    "REQUIRED_PATHS",
    "PathRequirement",
    "ScaffoldReport",
    "ScaffoldResult",
    "default_root",
    "ensure_structure",
    "required_package_names",
    "validate_structure",
]
