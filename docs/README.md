# Developer Guidelines

1. Install dependencies with `uv sync` (or `just install-dev`).
2. Use `just test` to execute unit and integration suites (`uv run pytest -m "unit or integration"`).
3. All commands are available via the `gear-generator` Typer CLI (see `docs/environment.md`, `docs/scaffold.md`, and `docs/utilities.md`).
4. Follow the test-first workflow: write failing tests before implementing CLI and utility logic.
5. Record printer tolerance results under `data/tolerances/{printer}.yaml` using the provided CLI commands once implemented.
