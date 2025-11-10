# Repository Scaffold

Validate and (optionally) create the expected project structure:

Audit the repository tree manually (or with your own scripting) to ensure the following required directories are present:

- Core package directories under `src/generators/`
- Output directories under `outputs/` for generated artifacts
- Test suites in `tests/unit`, `tests/integration`, and shared fixtures
- Supporting directories such as `configs/`, `data`, and `docs`

Create any missing paths before committing new work so downstream modules have a predictable layout.
