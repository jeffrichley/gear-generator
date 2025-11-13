# Feature Specification: Spur & Helical Gear Planning

**Feature Branch**: `001-gearbox-plan`  
**Created**: November 10, 2025  
**Status**: Draft  
**Input**: User description: "look at @iris.md and read about what we would need to do to make a spur gear and helical gear. things like gear_core.yaml perhaps?  basically like the Phase 1 — Gearboxes"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Document Spur Gear Blueprint (Priority: P1)

A CAD-focused engineer needs a reference plan that spells out every parameter, dependency, and validation step required to create a printable spur gear using the shared parametric tooling.

**Why this priority**: The spur gear is the baseline artifact that informs all other gear families. Without this, downstream motor-gearbox work cannot start.

**Independent Test**: Confirm that a reader can author a new spur-gear configuration file and associated checklist without consulting any other resources.

**Acceptance Scenarios**:

1. **Given** the plan, **When** an engineer drafts a `gear_core.yaml` spur entry, **Then** all mandatory parameters, ranges, and validation rules are enumerated with rationales.
2. **Given** the plan, **When** QA reviews it, **Then** they can derive physical verification steps (fit, backlash, strength checkpoints) solely from the documented process.

---

### User Story 2 - Extend Plan for Helical Gear Variant (Priority: P2)

A designer wants to reuse the spur guidance to generate helical options, including helix angle considerations, handedness, and load impacts, without rewriting the core plan.

**Why this priority**: Helical gears are the next planned deliverable and depend on the spur framework with additional requirements around axial load and meshing.

**Independent Test**: Validate that the plan lists all additional inputs, tolerances, and test deltas required for helical gears relative to spur gears.

**Acceptance Scenarios**:

1. **Given** the completed plan, **When** the designer prepares a helical gear spec, **Then** helix angle limits, handedness choices, and compensations for printer-induced skew are documented.
2. **Given** the plan, **When** manufacturing reviews it, **Then** they identify any additional fixturing or support needs unique to helical prints.

---

### User Story 3 - Validate Printability with Direct Gear Tests (Priority: P3)

A fabrication technician must print a representative spur/helical gear pair (or gear plus rack) to confirm fit, backlash, and tooth fidelity before green-lighting production runs.

**Why this priority**: Direct gear tests validate tolerances and tooth contact without relying on separate calibration prints, keeping verification aligned with production parts.

**Independent Test**: Ensure the plan defines which gear pair to print, measurement checkpoints, and pass/fail criteria that can be executed independently of broader assemblies.

**Acceptance Scenarios**:

1. **Given** the plan, **When** the technician prints the designated gear test pair, **Then** they understand what dimensions to measure and how to adjust offsets if results fall outside target ranges.
2. **Given** the plan, **When** design reviews test outcomes, **Then** they can map results back to configuration parameters without additional clarification.

### Edge Cases

- Parameter combinations produce tooth undercut or non-integer module relationships; the plan must flag and gate these prior to fabrication.
- Printer capability varies (e.g., nozzle diameter, filament swelling), requiring documented fallback offsets and reprint triggers.
- Helical gear handedness conflicts with intended rotation direction; the plan must highlight verification checkpoints before committing to assembly.
- Direct gear tests reveal inconsistent tooth contact across the width, prompting guidance on recalibrating Z-compensation and face-width adjustments.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The plan MUST define a canonical `gear_core.yaml` schema covering spur and helical parameters (module, tooth counts, pressure angle, helix angle, face width, backlash, clearance, material presets) along with acceptable ranges or defaults.
- **FR-002**: The plan MUST outline parameter validation rules for spur and helical gears, covering module/tooth relationships, minimum addendum to avoid undercut, helix angle limits based on printer capability, and a standardized initial backlash target range of 0.5°–1.0°.
- **FR-003**: The plan MUST describe the workflow for generating Build123d geometry from configuration data, highlighting shared steps and deltas between spur and helical gears.
- **FR-004**: The plan MUST specify the configuration and evaluation method for direct gear fit tests (e.g., mating spur pair, gear-and-rack combo), including measurement instructions and acceptance thresholds.
- **FR-005**: The plan MUST provide guidance for documenting test outcomes, linking measurement deltas from direct gear tests back to configuration adjustments (e.g., clearance offsets, backlash targets, helix compensation).
- **FR-006**: The plan MUST enumerate dependencies on shared utilities (tolerance helpers, exporters, materials data) so cross-functional teams know prerequisites before attempting fabrication.
- **FR-007**: The plan MUST capture review and sign-off checkpoints for engineering, manufacturing, and QA to ensure consistent interpretation before moving to the next gear family.

### Key Entities *(include if feature involves data)*

- **GearCoreConfig**: Logical representation of spur/helical parameters stored in `gear_core.yaml`, including required fields, optional overrides, and validation notes.
- **GearDesignWorkflow**: Ordered set of steps transforming configuration data into validated CAD output, including tolerance application and documentation hand-offs.
- **GearTestPair**: Production-geometry spur/helical gear pairs (printed with reduced face width or paired with a rack) used to validate backlash, contact pattern, and bore fit before full-thickness prints.
- **ReviewChecklist**: Cross-functional sign-off items tying design intent, fabrication readiness, and QA validation into a shared approval artifact.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Team members can create a complete spur or helical `gear_core.yaml` entry, including validation notes, in under 30 minutes using only the plan.
- **SC-002**: At least 90% of initial spur/helical gear validation prints based on the plan pass direct gear fit tests without rework.
- **SC-003**: Cross-functional reviewers (design, fabrication, QA) report fewer than two clarification questions during the first review cycle of the plan.
- **SC-004**: Direct test measurements can be traced back to specific configuration parameters within five minutes during QA audits.

## Assumptions

- Build123d and associated utilities (tolerance helpers, exporters) are already installed and documented separately.
- Teams have access to standard FDM printers with 0.4 mm nozzles and commonly used engineering polymers (PLA+, PETG) for baseline validation.
- Material-specific offset tables will be refined later; this plan captures the structure and placeholders for those datasets.

## Clarifications

### Session 2025-11-10

- Q: What backlash target range should the plan standardize for initial spur and helical prints? → A: Standardize 0.5°–1.0° backlash range.
