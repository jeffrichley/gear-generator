from generators.core.utils.measurements import GearMetadata, compute_gear_metadata


def test_compute_gear_metadata_returns_expected_dataclass():
    result = compute_gear_metadata(module=2.5, teeth=20, width=7.5)
    assert result == GearMetadata(
        pitch_diameter=50.0,
        module=2.5,
        teeth=20,
        face_width=7.5,
    )
