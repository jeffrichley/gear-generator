from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from generators.cli.main import app

runner = CliRunner()


def test_examples_hello_gear_creates_artifacts(tmp_path: Path) -> None:
    result = runner.invoke(
        app,
        [
            "examples",
            "hello-gear",
            "--output",
            str(tmp_path),
            "--teeth",
            "18",
            "--module",
            "1.5",
            "--width",
            "6.0",
        ],
    )

    assert result.exit_code == 0, result.stdout
    stl_path = tmp_path / "hello_gear.stl"
    step_path = tmp_path / "hello_gear.step"
    metadata_path = tmp_path / "hello_gear.json"

    for file_path in (stl_path, step_path, metadata_path):
        assert file_path.exists(), f"Expected artifact {file_path}"
