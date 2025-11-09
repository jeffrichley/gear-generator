from __future__ import annotations

from pathlib import Path

import pytest
from build123d import BuildPart, Cylinder

from generators.core.utils import exporters


@pytest.mark.unit
def test_export_part_writes_requested_formats(tmp_path: Path) -> None:
    with BuildPart() as bp:
        Cylinder(radius=5, height=2)

    artifacts = exporters.export_part(
        part=bp.part,
        output_dir=tmp_path,
        name="test_part",
        formats=("stl", "step"),
        metadata={"pitchDiameter": 10.0},
    )

    paths = {artifact.path for artifact in artifacts.files}
    assert tmp_path / "test_part.stl" in paths
    assert tmp_path / "test_part.step" in paths


@pytest.mark.unit
def test_write_metadata_creates_json(tmp_path: Path) -> None:
    artifacts = exporters.ExportArtifacts(
        base_name="test", files=[], metadata={"ratio": 3.0}
    )

    path = exporters.write_metadata(artifacts, tmp_path)
    assert path.exists()
    content = path.read_text()
    assert '"ratio": 3.0' in content
