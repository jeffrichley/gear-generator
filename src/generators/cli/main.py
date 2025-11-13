"""Typer entrypoint for gear-generator CLI."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List

import typer

from generators.gearboxes import schema

app = typer.Typer(help="Gear Generator CAD foundation tooling")
gear_app = typer.Typer(help="Gear-related commands")
plan_app = typer.Typer(help="Shared gear planning workflow commands")

app.add_typer(gear_app, name="gear")
gear_app.add_typer(plan_app, name="plan")


def _load_and_validate(config: Path) -> tuple[dict, list[str]]:
    try:
        data = schema.load_config(config)
    except schema.GearConfigError as exc:
        typer.echo(f"Configuration load error: {exc}", err=True)
        raise typer.Exit(code=1) from exc
    is_valid, errors = schema.validate_config(data)
    return data, errors if not is_valid else []


@plan_app.command("validate")
def validate(  # noqa: D401 - Typer CLI function
    config: Path = typer.Option(..., exists=True, readable=True, help="Path to gear configuration YAML."),
    output_format: str = typer.Option("text", "--format", "-f", help="Output format: text or json."),
) -> None:
    data, errors = _load_and_validate(config)
    if output_format.lower() == "json":
        payload = {"status": "valid" if not errors else "invalid"}
        if errors:
            payload["errors"] = errors
        typer.echo(json.dumps(payload))
    else:
        if errors:
            for message in errors:
                typer.echo(f"Validation error: {message}", err=True)
        else:
            typer.echo(f"Configuration '{data.get('variant_id', '<unknown>')}' passed validation.")
    if errors:
        raise typer.Exit(code=1)


@plan_app.command("export")
def export(  # noqa: D401 - Typer CLI function
    config: Path = typer.Option(..., exists=True, readable=True, help="Path to gear configuration YAML."),
    formats: List[str] = typer.Option(
        ["stl"],
        "--formats",
        help="One or more export formats (e.g. stl, step, json).",
        show_default=True,
    ),
    generate_test_pair: bool = typer.Option(True, help="Whether to queue direct gear test pair assets."),
) -> None:
    data, errors = _load_and_validate(config)
    if errors:
        for message in errors:
            typer.echo(f"Validation error: {message}", err=True)
        raise typer.Exit(code=1)

    if not formats:
        typer.echo("At least one export format is required.", err=True)
        raise typer.Exit(code=1)

    variant = data.get("variant_id", config.stem)
    typer.echo(
        f"Queued export for '{variant}' with formats {formats} (test pair={'on' if generate_test_pair else 'off'})."
    )


@app.callback()
def main() -> None:
    """CLI root callback. Reserved for global options."""


def run() -> None:
    app()


if __name__ == "__main__":
    run()
