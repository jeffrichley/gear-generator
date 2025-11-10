from unittest.mock import Mock

from generators.cli import main


def test_main_callback_returns_none() -> None:
    assert main.main() is None


def test_run_invokes_typer_application(monkeypatch):
    mock_app = Mock()
    monkeypatch.setattr(main, "app", mock_app)
    main.run()
    mock_app.assert_called_once_with()
