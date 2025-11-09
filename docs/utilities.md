# Shared Utilities

## Tolerance Helpers

- Generate calibration coupons:

  ```bash
  uv run gear-generator tolerances coupon --diameter 5.0 --output outputs/examples
  ```

  The command exports STL and STEP files plus JSON metadata describing each offset. Printed coupons can be measured and recorded using the `tolerances record` command.

- Record measured offsets:

  ```bash
  uv run gear-generator tolerances record \
    --printer prusa-mk4 \
    --material PLA+ \
    --source data/measurements/prusa-mk4.yaml
  ```

  Profiles are saved under `data/tolerances/{printer}.yaml` and adhere to the data model defined in the specification.

## Exporter Utilities

- Export Build123d geometry to STL/STEP using `generators.core.utils.exporters.export_part`.
- Metadata is written alongside geometry as `{name}.json`, enabling automation to consume pitch diameter, module, and other measurements.

## Measurement Helpers

- `generators.core.utils.measurements.compute_gear_metadata` calculates pitch diameter and associated gear properties for documentation and validation.
