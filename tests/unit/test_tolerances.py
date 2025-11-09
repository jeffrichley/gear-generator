from __future__ import annotations

from pathlib import Path

import pytest

from generators.core.utils import tolerances


@pytest.mark.unit
def test_generate_coupon_creates_solids_for_each_offset(tmp_path: Path) -> None:
    part, metadata = tolerances.generate_coupon(diameter=6.0, height=8.0)

    assert len(metadata.offsets) == len(tolerances.DEFAULT_OFFSETS)
    assert len(part.solids()) == len(tolerances.DEFAULT_OFFSETS)

    export_path = tmp_path / "coupon.stl"
    tolerances.export_coupon(part, export_path)
    assert export_path.exists()


@pytest.mark.unit
def test_build_profile_round_trips_through_dict() -> None:
    measurements = [
        tolerances.ToleranceMeasurement(offset_mm=-0.1, fit_quality="press"),
        tolerances.ToleranceMeasurement(offset_mm=0.0, fit_quality="snug"),
    ]

    profile = tolerances.ToleranceProfile(
        printer_id="test-printer",
        material="PLA+",
        measurements=measurements,
    )

    data = profile.to_dict()
    restored = tolerances.ToleranceProfile.from_dict(data)
    assert restored == profile


@pytest.mark.unit
def test_save_profile_writes_yaml(tmp_path: Path) -> None:
    profile = tolerances.ToleranceProfile(
        printer_id="test-printer",
        material="PLA+",
        measurements=[
            tolerances.ToleranceMeasurement(offset_mm=0.0, fit_quality="snug"),
        ],
    )

    destination = tmp_path / "profiles"
    path = tolerances.save_profile(profile, destination)

    assert path.exists()
    contents = path.read_text()
    assert "printer_id: test-printer" in contents
