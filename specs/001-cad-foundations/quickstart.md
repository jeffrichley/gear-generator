# Quickstart — CAD Foundations

## 1. Prerequisites

1. Install Python 3.12.2 or newer.  
2. Install `uv` (https://github.com/astral-sh/uv).  
3. Ensure Git and a compatible slicer (e.g., PrusaSlicer) are available.

## 2. Bootstrap the Repository

```bash
uv init gear-generator
uv sync
```

This creates and installs the pinned environment defined in `pyproject.toml` (Phase 0 deliverable).

## 3. Verify the Environment

Confirm manually that Python 3.12 is active and core dependencies install cleanly via `uv sync`. Run `python -c "import build123d, cadquery"` if you need a quick smoke test.

## 4. Scaffold Required Paths

Ensure directories (`src/generators`, `tests`, `docs`, `data`, `outputs`) exist before committing changes. Create any missing paths so contributors land in a predictable layout.

## 5. Run Tests

```bash
just test
```

- Executes pytest with the available unit suite.  
- Fails fast if utilities regress.

## 6. Publish Documentation (Optional in Phase 0)

```bash
uv run mkdocs serve
```

Hosts the MkDocs Material site for local review of developer guides.
