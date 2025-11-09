from __future__ import annotations

from pathlib import Path

import yaml
from typer.testing import CliRunner

from generators.cli.main import app

runner = CliRunner()


def test_tolerances_coupon_and_record(tmp_path: Path) -> None:
    coupon_dir = tmp_path / "coupon"
    coupon_dir.mkdir()

    result_coupon = runner.invoke(
        app,
        [
            "tolerances",
            "coupon",
            "--output",
            str(coupon_dir),
            "--diameter",
            "5.0",
        ],
    )
    assert result_coupon.exit_code == 0, result_coupon.stdout
    assert (coupon_dir / "tolerance_coupon.stl").exists()
    assert (coupon_dir / "tolerance_coupon.step").exists()

    source_path = tmp_path / "measurements.yaml"
    yaml.safe_dump(
        {
            "measurements": [
                {"offset_mm": 0.0, "fit_quality": "snug"},
                {"offset_mm": 0.1, "fit_quality": "free"},
            ]
        },
        source_path.open("w"),
    )

    output_dir = tmp_path / "profiles"
    result_record = runner.invoke(
        app,
        [
            "tolerances",
            "record",
            "--printer",
            "test-printer",
            "--material",
            "PLA+",
            "--source",
            str(source_path),
            "--output",
            str(output_dir),
        ],
    )

    assert result_record.exit_code == 0, result_record.stdout
    profile_path = output_dir / "test-printer.yaml"
    assert profile_path.exists()
    written = yaml.safe_load(profile_path.read_text())
    assert written["material"] == "PLA+"
    assert len(written["measurements"]) == 2
