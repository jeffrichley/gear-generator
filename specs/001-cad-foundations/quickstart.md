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

```bash
uv run gear-generator env verify --format table
uv run gear-generator env verify --format json --output data/environment/profile.json
```

- Confirms Python version, uv activation, and dependency availability.
- Outputs structured logs via rich.

## 4. Scaffold Required Paths

```bash
uv run gear-generator repo scaffold --root . --autofix
```

- Ensures directories (`src/generators`, `examples`, `tests`, `docs`, `data`) exist.  
- Reports missing items and optionally creates them when `--autofix` flag provided.

## 5. Run the `hello_gear` Example

```bash
uv run gear-generator examples hello-gear --teeth 20 --module 2.0 --width 8.0 --output outputs/examples
ls outputs/examples/hello_gear.stl
```

Generates STL and STEP files plus metadata for verification.

## 6. Calibrate Printer Tolerances

```bash
uv run gear-generator tolerances coupon --diameter 5.0 --output outputs/examples
# Print coupon, measure fits
uv run gear-generator tolerances record --printer "prusa-mk4" --material PLA+ --source data/measurements/prusa-mk4.yaml --output data/tolerances
```

Stores clearance offsets for future parametric models.

## 7. Run Tests

```bash
just test
```

- Executes pytest with unit and integration markers.  
- Fails fast if CLI or utilities regress.

## 8. Publish Documentation (Optional in Phase 0)

```bash
uv run mkdocs serve
```

Hosts the MkDocs Material site for local review of developer guides.
