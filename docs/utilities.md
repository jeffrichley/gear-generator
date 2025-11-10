# Shared Utilities

## Exporter Utilities

- Export Build123d geometry to STL/STEP using `generators.core.utils.exporters.export_part`.
- Metadata is written alongside geometry as `{name}.json`, enabling automation to consume pitch diameter, module, and other measurements.

## Measurement Helpers

- `generators.core.utils.measurements.compute_gear_metadata` calculates pitch diameter and associated gear properties for documentation and validation.
