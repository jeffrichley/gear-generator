# Environment Verification

Use the CLI to validate workstation readiness for the CAD foundations toolkit:

```bash
uv run gear-generator env verify --format table
uv run gear-generator env verify --format json --output data/environment/profile.json
```

The command reports:

- Operating system and Python version
- Whether the current shell is running inside the UV-managed virtual environment
- Status of required dependencies (`build123d`, `cadquery`, `numpy`, `pyyaml`, `rich`, `typer`)

If any dependencies are missing, the command exits with a non-zero status so that CI or local workflows can halt before proceeding.
