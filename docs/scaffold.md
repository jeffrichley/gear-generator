# Repository Scaffold

Validate and (optionally) create the expected project structure:

```bash
uv run gear-generator repo scaffold --root . --dry-run
uv run gear-generator repo scaffold --root . --autofix --output data/scaffold/report.json
```

The command checks for:

- Core package directories under `src/generators/`
- `examples/` and `outputs/examples/` for generated artifacts
- Test suites in `tests/unit`, `tests/integration`, and shared fixtures
- Supporting directories such as `configs/`, `data/`, and `docs/`

When `--autofix` is provided, missing directories/files are created and the JSON report records the change. Any failure exits with a non-zero status so CI pipelines can halt before proceeding.
