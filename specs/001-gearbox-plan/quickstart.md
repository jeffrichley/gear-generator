# Quickstart: Spur & Helical Gear Planning

Follow these steps to author, validate, and export printable spur/helical gears using the shared planning assets.

## 1. Prepare Environment
- Ensure Python 3.12+, `uv`, and the project dependencies (`build123d`, `cadquery`, `pyyaml`, `numpy`) are installed.
- From repo root, run `just install` (or equivalent) to set up the virtual environment.

## 2. Create a Gear Configuration
- Copy `configs/gear_core.example.yaml` to a new file (e.g., `configs/gear_core.spur_28.yaml`).
- Update required fields:
  - `gear_family`: `spur` or `helical`
  - `variant_id`: unique identifier
  - `geometry`: module, tooth count, pressure angle, face width, optional helix angle
  - `tolerances`: backlash target (0.5–1.0), bore offset, tooth profile scale
  - `materials`: default filament and any overrides
  - `validation`: test pair reference, print overrides, measurement guidance

## 3. Validate Configuration via CLI
- Run `uv run python -m generators.cli.main gear plan validate --config configs/gear_core.spur_28.yaml --format json`.
- Confirm output status is `valid`; address any reported schema or planning rule violations.

## 4. Generate Geometry & Validation Pair
- Execute `uv run python -m generators.cli.main gear plan export --config configs/gear_core.spur_28.yaml --formats stl step json --generate-test-pair`.
- Locate generated assets under `dist/gear-plan/<variant_id>/` (STL, STEP, optional test-pair files).

## 5. Print & Measure Direct Gear Pair
- Slice and print the designated test pair (spur-spur, spur-rack, or helical match).
- Record backlash, contact pattern, and bore fit measurements per the plan.
- If deviations exceed targets, adjust offsets in the YAML and repeat validation.

## 6. Complete Review Checklist
- Fill out the cross-functional checklist (design, fabrication, QA) referencing exported documentation.
- Submit review metadata via CLI or API (per contracts) to log sign-off.

## 7. Promote Configuration
- Once validated, tag the `gear_core.yaml` entry and push updates for integration with downstream motor/gearbox assemblies.
