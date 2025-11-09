"""Typer entrypoint for gear-generator CLI."""

from __future__ import annotations

import json
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from generators.core.environment import checks
from generators.core.utils import exporters, materials, tolerances
from generators.core.utils import logging as log_utils
from generators.examples.hello_gear import HelloGearConfig, build_hello_gear

app = typer.Typer(help="Gear Generator CAD foundation tooling")
console = Console()

env_app = typer.Typer(help="Environment verification commands")
examples_app = typer.Typer(help="Example geometry commands")
tolerances_app = typer.Typer(help="Tolerance calibration commands")

app.add_typer(env_app, name="env")
app.add_typer(examples_app, name="examples")
app.add_typer(tolerances_app, name="tolerances")


@app.callback()
def main() -> None:
    """CLI root callback. Reserved for global options."""


def _render_profile_table(profile: checks.EnvironmentProfile) -> None:
    table = Table(title="Environment verification")
    table.add_column("Property")
    table.add_column("Value")

    table.add_row("OS", f"{profile.os_name} {profile.os_version}")
    table.add_row("Python", profile.python_version)
    table.add_row("UV Active", "yes" if profile.uv_active else "no")
    table.add_row("Status", profile.status)

    console.print(table)

    pkg_table = Table(title="Dependencies")
    pkg_table.add_column("Package")
    pkg_table.add_column("Version")
    pkg_table.add_column("Status")
    for record in profile.packages:
        pkg_table.add_row(record.name, record.version or "-", record.status)
    console.print(pkg_table)


@env_app.command("verify")
def env_verify(
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Optional path to persist verification results as JSON.",
    ),
    fmt: str = typer.Option(
        "table", "--format", "-f", help="Output format: table or json."
    ),
) -> None:
    """Check workstation readiness for Build123d/CadQuery workflows."""
    profile = checks.collect_environment_profile()

    console.print("Environment verification results", style="bold green")

    if fmt.lower() == "json":
        console.print_json(data=profile.to_dict())
    else:
        _render_profile_table(profile)

    if output is not None:
        save_json(profile.to_dict(), output)

    if profile.status != "ready":
        raise typer.Exit(code=1)


@examples_app.command("hello-gear")
def examples_hello_gear(
    teeth: int = typer.Option(20, help="Number of teeth for the demonstration gear."),
    module: float = typer.Option(2.0, help="Module used to size the gear."),
    width: float = typer.Option(8.0, help="Face width of the gear in millimetres."),
    output: Path = typer.Option(
        Path("outputs/examples"), "--output", help="Directory for generated artifacts."
    ),
) -> None:
    config = HelloGearConfig(teeth=teeth, module=module, width=width)
    part, metadata = build_hello_gear(config)

    console.print("Generating hello gear example", style="bold green")
    artifacts = exporters.export_part(
        part,
        output,
        name="hello_gear",
        metadata={
            "teeth": config.teeth,
            "module": config.module,
            "faceWidth": config.width,
            "pitchDiameter": metadata.pitch_diameter,
        },
    )
    exporters.write_metadata(artifacts, output)
    console.print(f"Artifacts written to {output}")


@tolerances_app.command("coupon")
def tolerances_coupon(
    diameter: float = typer.Option(5.0, help="Nominal diameter for coupon columns."),
    output: Path = typer.Option(
        Path("outputs/examples"), "--output", help="Directory for coupon geometry."
    ),
) -> None:
    console.print("Generating tolerance coupon", style="bold green")
    part, metadata = tolerances.generate_coupon(diameter=diameter)
    artifacts = exporters.export_part(
        part,
        output,
        name="tolerance_coupon",
        metadata={
            "baseDiameter": metadata.base_diameter,
            "offsets": list(metadata.offsets),
        },
    )
    exporters.write_metadata(artifacts, output)
    console.print(f"Coupon generated in {output}")


@tolerances_app.command("record")
def tolerances_record(
    printer: str = typer.Option(..., "--printer", help="Identifier for the printer."),
    material_name: str = typer.Option(
        ..., "--material", help="Material name (e.g. PLA+)."
    ),
    source: Path = typer.Option(
        ..., "--source", help="YAML file containing measurement entries."
    ),
    output: Path = typer.Option(
        Path("data/tolerances"),
        "--output",
        help="Directory to store tolerance profiles.",
    ),
) -> None:
    material = materials.get_material(material_name)
    measurements = list(tolerances.load_measurements(source))
    if not measurements:
        raise typer.BadParameter("Measurement file contained no entries.")

    profile = tolerances.ToleranceProfile(
        printer_id=printer,
        material=material.name,
        measurements=measurements,
    )
    path = tolerances.save_profile(profile, output)
    console.print(f"Profile saved to {path}")


def save_json(data: dict[str, object], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(data, indent=2))
    log_utils.log_info("Saved JSON file", details={"path": str(destination)})


def run() -> None:
    app()


if __name__ == "__main__":
    run()
