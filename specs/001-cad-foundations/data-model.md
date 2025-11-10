# Data Model — Phase 0 CAD Foundations

## Overview

Phase 0 does not persist application data; instead it documents reusable utility modules and the metadata they emit when exporting geometry. The data descriptions below serve as guidance for consistent JSON output and documentation tables.

## Entities

### ExportArtifact
- **Description**: Metadata written alongside STL/STEP exports produced by `exporters.export_part`.
- **Fields**:
  - `name` (string) – logical identifier for the artifact bundle.
  - `paths` (list of strings) – exported file paths relative to the output directory.
  - `metadata` (object) – free-form key/value pairs describing gear geometry (e.g., module, face width, pitch diameter).
- **Validation Notes**: `paths` must include at least one entry; metadata keys should be camelCase for downstream tooling consistency.

### UtilityModule
- **Description**: Documentation record capturing the purpose and inputs/outputs of a shared helper (exporters, materials, measurements).
- **Fields**:
  - `name` (string)
  - `purpose` (string)
  - `inputs` (list of strings)
  - `outputs` (list of strings)
- **Validation Notes**: Each module must declare at least one input and output to remain useful for downstream automation.

## State & Storage

- Export metadata is persisted as JSON adjacent to generated artifacts under `outputs/`.
- Utility documentation lives in Markdown (`docs/utilities.md`) and is regenerated manually when helpers change.

## Data Volume Assumptions

- Export metadata files are small (<5 KB) and generated on demand for demonstrations.
- No centralized database or long-lived records exist in Phase 0.
