from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from build123d import Part, export_step, export_stl


@dataclass(slots=True)
class ExportedFile:
    path: Path
    format: str


@dataclass(slots=True)
class ExportArtifacts:
    base_name: str
    files: list[ExportedFile]
    metadata: dict[str, object]


def export_part(
    part: Part,
    output_dir: Path,
    name: str,
    formats: Sequence[str] = ("stl", "step"),
    metadata: dict[str, object] | None = None,
) -> ExportArtifacts:
    output_dir.mkdir(parents=True, exist_ok=True)
    exported: list[ExportedFile] = []
    normalized_formats = formats if isinstance(formats, Sequence) else tuple(formats)
    for fmt in normalized_formats:
        fmt_lower = fmt.lower()
        path = output_dir / f"{name}.{fmt_lower}"
        if fmt_lower == "stl":
            export_stl(part, str(path))
        elif fmt_lower == "step":
            export_step(part, str(path))
        else:
            raise ValueError(f"Unsupported export format: {fmt}")
        exported.append(ExportedFile(path=path, format=fmt_lower))

    return ExportArtifacts(base_name=name, files=exported, metadata=metadata or {})


def write_metadata(artifacts: ExportArtifacts, destination: Path) -> Path:
    destination.mkdir(parents=True, exist_ok=True)
    path = destination / f"{artifacts.base_name}.json"
    data = {
        "files": [
            {
                "path": str(file.path),
                "format": file.format,
            }
            for file in artifacts.files
        ],
        **artifacts.metadata,
    }
    path.write_text(_to_json(data))
    return path


def _to_json(data: dict[str, object]) -> str:
    import json

    return json.dumps(data, indent=2)


__all__ = [
    "ExportArtifacts",
    "ExportedFile",
    "export_part",
    "write_metadata",
]
