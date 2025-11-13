# Data Model: Spur & Helical Gear Planning

## Overview

The feature formalizes configuration-driven gear generation. Core entities capture parametric inputs (`GearCoreConfig`), reusable tolerancing logic, direct gear validation tests, and review artifacts.

## Entities

### GearCoreConfig
- **Purpose**: Canonical YAML representation of spur/helical gear parameters.
- **Fields**:
  - `gear_family` *(enum)*: `spur` | `helical`
  - `variant_id` *(string)*: unique identifier per configuration
  - `geometry.module` *(float mm)*: gear module (0.5–3.0)
  - `geometry.tooth_count` *(int)*: total teeth for spur; base tooth count for helical (paired with handedness)
  - `geometry.pressure_angle` *(float degrees)*: default 20°; allow 14.5°–25°
  - `geometry.helix_angle` *(float degrees, optional)*: required for helical; ±15° cap for FDM prints
  - `geometry.face_width` *(float mm)*: printable width (5–20 mm typical window)
  - `geometry.clearance` *(float mm)*: radial clearance offset
  - `geometry.addendum_override` *(float mm, optional)*
  - `geometry.dedendum_override` *(float mm, optional)*
  - `tolerances.backlash_target` *(float degrees)*: default 0.5–1.0 window
  - `tolerances.bore_offset` *(float mm)*: printer/material specific offset
  - `tolerances.tooth_profile_scale` *(float percentage)*: compensation factor
  - `materials.default` *(enum)*: PLA_PLUS | PETG | ASA | NYLON | NYLON_CF
  - `materials.alternatives[]` *(list)*: override entries with material-specific offsets
  - `validation.test_pair.reference` *(string)*: identifier of mating gear/rack for validation
  - `validation.test_pair.print_settings` *(dict)*: overrides (layer height, infill) for quick validation prints
  - `validation.measurements.backlash_method` *(string)*: textual summary for QA procedure
  - `validation.measurements.contact_pattern_targets` *(string)*: expected tooth contact notes
  - `validation.measurements.bore_fit_targets` *(list mm)*
  - `metadata.authors[]` *(list)*: maintainers responsible
  - `metadata.revision` *(semver string)*
  - `metadata.notes` *(string)*
- **Relationships**:
  - References a single `GearTestPair` definition
  - Consumed by `GearDesignWorkflow`

### GearTestPair
- **Purpose**: Defines the direct gear validation geometry and measurement targets without relying on separate calibration prints.
- **Fields**:
  - `test_id` *(string)*
  - `gear_family` *(enum)*: `spur` | `helical`
  - `primary_gear` *(string)*: reference to variant under test
  - `reference_gear` *(string)*: mating gear/rack identifier
  - `print_parameters` *(dict)*: adjustments for validation print (face width reduction, infill, support)
  - `measurement.instructions` *(string)*
  - `measurement.targets` *(dict)*: backlash window, contact pattern expectations, bore fit notes
- **Relationships**:
  - Referenced by `GearCoreConfig.validation.test_pair`
  - Consumed by `GearDesignWorkflow`

### GearDesignWorkflow
- **Purpose**: Declarative steps linking configuration ingestion to CAD export and review.
- **Fields**:
  - `workflow_id` *(string)*
  - `steps[]` *(ordered list)*: structured entries containing `name`, `owner_role`, `inputs`, `outputs`
  - `checks.integrity` *(list)*: validation functions (e.g., undercut prevention, backlash check)
  - `checks.documentation` *(list)*: review artifacts required
  - `dependencies` *(list)*: required utilities (`tolerances.py`, `exporters.py`)
- **Relationships**:
  - Consumes `GearCoreConfig` and `GearTestPair` references.

### ReviewChecklist
- **Purpose**: Cross-functional sign-off covering design, fabrication, QA readiness.
- **Fields**:
  - `checklist_id` *(string)*
  - `category` *(enum)*: `design`, `fabrication`, `qa`
  - `items[]` *(list)*: each item has `description`, `acceptance_criteria`, `status`
  - `linked_config` *(string)*: `variant_id` for traceability
  - `signoff.owner` *(string)*
  - `signoff.date` *(date)*
- **Relationships**:
  - Linked to specific `GearCoreConfig` entries and `GearDesignWorkflow` stage completions.

### ToleranceHelper
- **Purpose**: Programmatic utilities reintroduced under `tolerances.py` to standardize offsets.
- **Functions**:
  - `fit_clearance(diameter, profile)`
  - `press_fit(diameter)`
  - `angular_backlash_adjust(module, backlash_target)`
- **Relationships**:
  - Invoked by Build123d part builders and CLI validation scripts.

## Data Flow Summary

1. Designers add/update a `GearCoreConfig` entry in `gear_core.yaml`.
2. CLI ingests YAML, validates schema, and instantiates Build123d builders using `ToleranceHelper`.
3. `GearTestPair` geometry is generated (when needed) alongside full gear outputs.
4. QA logs measurement results against direct test targets; adjustments feed back into `tolerances` fields.
5. `ReviewChecklist` captures sign-off before promoting the gear design to downstream assemblies.
