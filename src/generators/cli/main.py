"""Typer entrypoint for gear-generator CLI."""

from __future__ import annotations

import typer

app = typer.Typer(help="Gear Generator CAD foundation tooling")


@app.callback()
def main() -> None:
    """CLI root callback. Reserved for global options."""


def run() -> None:
    app()


if __name__ == "__main__":
    run()
