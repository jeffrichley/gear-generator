# Feature Specification: Phase 0 CAD Foundations

**Feature Branch**: `001-cad-foundations`  
**Created**: 2025-11-08  
**Status**: Draft  
**Input**: User description: "look at @iris.md and we are doing Phase 0 — CAD Foundations (Build123d utilities)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Stand Up the CAD Toolchain (Priority: P1)

The lead mechanical engineer needs a reliable checklist to install Build123d, CadQuery, supporting Python packages, and visualization tools so that the design team can begin creating parametric parts without manual guesswork.

**Why this priority**: Without a predictable environment, none of the later gear or motor work can start; this is the critical path for the entire program.

**Independent Test**: Execute the documented setup steps on a clean workstation and confirm the verification script reports all dependencies ready.

**Acceptance Scenarios**:

1. **Given** a clean workstation with network access, **When** the engineer follows the installation procedure, **Then** all required packages install without unresolved dependency errors.
2. **Given** a configured workstation, **When** the verification script is run, **Then** it confirms Build123d, CadQuery, and visualization tooling are available at the specified versions.

---

### User Story 2 - Establish the Repository Skeleton (Priority: P2)

The repository maintainer wants to scaffold the agreed directory layout, baseline documentation, and automation hooks so contributors can add models and utilities in consistent locations.

**Why this priority**: A predictable structure avoids rework and speeds onboarding; it directly supports future Phases 1–3.

**Independent Test**: Start from the spec, generate the folder tree, placeholder files, and configuration stubs; verify an automated check compares the result to the defined structure and passes.

**Acceptance Scenarios**:

1. **Given** the Phase 0 spec, **When** the maintainer runs the scaffold script or manual steps, **Then** all directories (`src/generators/cli`, `src/generators/core/environment`, `src/generators/core/utils`, `src/generators/gears`, `src/generators/motors`, `examples`, `tests`, `configs`, `data`) exist with placeholder READMEs where required.
2. **Given** the repository skeleton, **When** the validation checklist is executed, **Then** it confirms that documentation anchors (README, CHANGELOG, doc site stub) and configuration examples are present.

---

### User Story 3 - Deliver Shared Utility Modules (Priority: P3)

The CAD technologist needs starter utility modules (tolerance helpers, exporters, materials library, measurement helpers) and proof-of-life scripts to ensure geometry reuse is possible before teams add complex designs.

**Why this priority**: Utilities reduce duplicated logic and keep printed parts consistent across gear and motor teams; however, they build on the environment and repo structure, hence P3.

**Independent Test**: Generate the example modules, run the `hello_gear` sample, and confirm exported geometry matches defined tolerances and metadata outputs.

**Acceptance Scenarios**:

1. **Given** the shared utility modules, **When** the `hello_gear` example is executed, **Then** it exports an STL and STEP file, logs metadata, and opens a preview without errors.
2. **Given** the tolerance helper library, **When** the fit-coupon generator runs with default offsets, **Then** it produces a model annotated with the defined clearance values for physical validation.

### Edge Cases

- Workstation lacks administrative rights for system-wide installs—spec must outline how to complete setup using user-space environments.
- Primary visualization tool (CQ-Editor or Jupyter-CadQuery) is unavailable—provide fallback approach so verification still passes.
- Printer-dependent tolerance offsets differ from defaults—define how to capture calibration data without blocking the phase deliverable.

## Assumptions

- Target operating systems are macOS 14+ and Ubuntu 22.04 LTS; Windows support can follow later phases.
- Team members have Python 3.12+ available or can install via pyenv/uv as part of the documented steps.
- Network access is available during setup to obtain packages and dependencies.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The specification MUST document a reproducible installation process for Build123d, CadQuery, NumPy, PyYAML, and visualization tooling, including command sequences and version targets.
- **FR-002**: The plan MUST require creation of an isolated Python environment (via uv, Poetry, or virtualenv) and define verification steps confirming the environment activates correctly.
- **FR-003**: The specification MUST define the repository directory structure, naming conventions, and required placeholder files so scaffolding can be audited automatically.
- **FR-004**: The specification MUST describe baseline utility modules for tolerances, exporters, materials, and measurement calculations, including their intended inputs/outputs and acceptance checks.
- **FR-005**: The plan MUST include a `hello_gear` reference example that demonstrates geometry generation, metadata logging, and export to STL/STEP formats using the shared utilities.
- **FR-006**: The specification MUST provide guidance for capturing printer-specific tolerance offsets through printable fit-test artifacts and documentation of resulting compensation values.
- **FR-007**: The plan MUST define documentation deliverables (README outline, CHANGELOG initiation, documentation site stub) and the governance process for keeping them current.
- **FR-008**: The specification MUST outline automated or manual validation checkpoints (e.g., scripts, checklists) to confirm environment readiness, directory compliance, and example execution before closing Phase 0.

### Key Entities *(include if feature involves data)*

- **Environment Profile**: Captures OS assumptions, dependency versions, package sources, and validation script outputs.
- **Repository Skeleton**: Defines the directory tree, placeholder files, and documentation artifacts required for subsequent phases.
- **Utility Module Set**: Specifies shared helper libraries (tolerances, exporters, materials, measurement) and their contracts.
- **Example Artifacts**: Includes reference scripts (`hello_gear`), sample configuration files, and generated outputs used to verify readiness.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A new workstation completes the Phase 0 setup checklist in under 60 minutes with zero unresolved dependency errors.
- **SC-002**: The repository structure validation passes with 100% compliance (all required directories/files present, no unexpected omissions).
- **SC-003**: The `hello_gear` example exports STL and STEP outputs and records metadata in under 5 minutes on a configured workstation.
- **SC-004**: At least 90% of team members report the documentation sufficient to reproduce the setup without requesting additional help during pilot onboarding.
