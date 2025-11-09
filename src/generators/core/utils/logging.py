"""Structured logging utilities for CLI commands."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from rich.console import Console
from rich.table import Table

_CONSOLE = Console()


@dataclass(slots=True)
class LogEvent:
    """Represents a structured log message."""

    level: str
    message: str
    details: dict[str, object] | None = None


def log(event: LogEvent) -> None:
    """Emit a structured message using Rich."""
    if event.details:
        table = Table(title=event.message)
        table.add_column("Key")
        table.add_column("Value")
        for key, value in event.details.items():
            table.add_row(str(key), repr(value))
        _CONSOLE.print(table)
    else:
        _CONSOLE.print(f"[{event.level}] {event.message}")


def log_error(message: str, *, details: dict[str, object] | None = None) -> None:
    log(LogEvent(level="error", message=message, details=details))


def log_info(message: str, *, details: dict[str, object] | None = None) -> None:
    log(LogEvent(level="info", message=message, details=details))


def log_table(title: str, rows: Iterable[tuple[str, str]]) -> None:
    table = Table(title=title)
    table.add_column("Key")
    table.add_column("Value")
    for key, value in rows:
        table.add_row(key, value)
    _CONSOLE.print(table)
