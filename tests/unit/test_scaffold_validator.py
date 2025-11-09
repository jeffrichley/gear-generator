from pathlib import Path

import pytest

from generators.core.environment import scaffold


@pytest.mark.unit
def test_validate_structure_reports_missing_directories(tmp_path: Path) -> None:
    report = scaffold.validate_structure(tmp_path)

    missing = {item.path for item in report.results if item.state == "missing"}
    assert "src/generators/core" in missing
    assert report.status == "fail"


@pytest.mark.unit
def test_validate_structure_with_autofix_creates_missing_nodes(tmp_path: Path) -> None:
    report = scaffold.validate_structure(tmp_path, autofix=True)

    assert report.status == "pass"
    for required in scaffold.REQUIRED_PATHS:
        assert (tmp_path / required.path).exists()
