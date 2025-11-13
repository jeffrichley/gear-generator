# Research: Spur & Helical Gear Planning

## Decision 1: Canonical `gear_core.yaml` Schema Fields
- **Decision**: Define top-level sections for `gear_family`, `geometry`, `tolerances`, `materials`, `validation`, and `metadata`, with required fields (module, tooth counts, pressure angle, helix angle for helical, face width, backlash target, clearance offsets).
- **Rationale**: Aligns with parametric gear design practice where geometry inputs, manufacturing adjustments, and verification data must be separated for reuse and automation. Mirrors structure used in existing `motor_core` configs.
- **Alternatives Considered**:
  - Single flat YAML with all values — rejected due to poor readability and difficult schema validation.
  - Multiple YAML files per gear family — rejected to avoid fragmentation and duplicated metadata.

## Decision 2: Direct Gear Validation Strategy
- **Decision**: Use a representative gear pair (spur-spur or spur-rack for spur gears, and matched helical pair for helical gears) with reduced face width to minimize print time while preserving tooth engagement characteristics.
- **Rationale**: Validates true mesh behavior, backlash, and surface contact on production geometry without maintaining separate calibration artifacts.
- **Alternatives Considered**:
  - Dedicated calibration fixtures — rejected per stakeholder direction to avoid extra artifacts.
  - Full assembly prints — rejected due to material/time overhead for iterative validation.

## Decision 3: Backlash Measurement & Acceptance Window
- **Decision**: Target 0.5°–1.0° backlash for initial spur/helical prints, measured by coupling the test gear with a reference gear and recording angular displacement under light preload.
- **Rationale**: Balances robotics-level precision with realistic expectations for FDM. Supports future tightening once material-specific compensations mature.
- **Alternatives Considered**:
  - <0.5° backlash — rejected due to high reprint risk and inconsistent results across printers.
  - >1.0° backlash — rejected because it compromises joint rigidity and increases positional error.

## Decision 4: Tolerance Helper Reinforcement
- **Decision**: Reintroduce `tolerances.py` with standardized helper functions (`fit_clearance`, `press_fit`, `angular_backlash_adjust`) referenced throughout the plan.
- **Rationale**: Centralizes offset logic; supports data-driven adjustments tied to direct gear test findings and keeps Build123d builders lean.
- **Alternatives Considered**:
  - Embedding offsets directly in geometry builders — rejected for maintainability and cross-gear reuse concerns.
  - Managing offsets solely in YAML — rejected because code-side utility is still required for Build123d constructs.
