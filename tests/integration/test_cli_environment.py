from typer.testing import CliRunner

from generators.cli.main import app

runner = CliRunner()


def test_env_verify_outputs_json_table(tmp_path):
    result = runner.invoke(
        app,
        [
            "env",
            "verify",
            "--format",
            "json",
            "--output",
            str(tmp_path / "profile.json"),
        ],
    )

    assert result.exit_code == 0, result.stdout
    assert "Environment verification" in result.stdout

    output_file = tmp_path / "profile.json"
    assert output_file.exists()
    data = output_file.read_text()
    assert "packages" in data
