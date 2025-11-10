import pytest
from rich.console import Console

from generators.core.utils import log_utils


@pytest.fixture()
def recording_console(monkeypatch: pytest.MonkeyPatch) -> Console:
    console = Console(record=True)
    monkeypatch.setattr(log_utils, "_CONSOLE", console)
    return console


def test_log_info_without_details_emits_plain_message(recording_console: Console) -> None:
    log_utils.log_info("hello world")
    output = recording_console.export_text()
    assert "hello world" in output
    assert "[info]" not in output  # Rich strips markup tags


def test_log_error_with_details_renders_table(recording_console: Console) -> None:
    log_utils.log_error("failed", details={"gear": "spur", "teeth": 22})
    output = recording_console.export_text()
    assert "failed" in output
    assert "gear" in output
    assert "22" in output


def test_log_table_prints_rows(recording_console: Console) -> None:
    log_utils.log_table("stats", [("module", "2"), ("width", "5")])
    output = recording_console.export_text()
    assert "stats" in output
    assert "module" in output
    assert "5" in output
