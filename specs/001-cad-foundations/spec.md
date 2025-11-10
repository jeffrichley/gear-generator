# Feature Specification: Phase 0 CAD Foundations

**Feature Branch**: `001-cad-foundations`  
**Created**: 2025-11-08  
**Status**: Draft  
**Input**: User description: "look at @iris.md and we are doing Phase 0 — CAD Foundations (Build123d utilities)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Deliver Shared Utility Modules (Priority: P1)

The CAD technologist needs starter utility modules (exporters, materials library, measurement helpers) that can be reused across future gear models.

**Why this priority**: Utilities reduce duplicated logic and keep generated parts consistent across gear and motor teams; they provide immediate value even without higher-level automation.

**Independent Test**: Execute the exporter and measurement unit tests to confirm metadata serialization and derived properties behave as expected.

**Acceptance Scenarios**:

1. **Given** the shared utility modules, **When** a part is exported via the helpers, **Then** STL/STEP files and metadata are produced without errors.
2. **Given** the measurement helper library, **When** it is invoked with representative gear parameters, **Then** it returns pitch diameter and related values consistent with documented formulas.

---

### Edge Cases

- Workstation lacks administrative rights for system-wide installs—spec must outline how to complete setup using user-space environments.
- Primary visualization tool (CQ-Editor or Jupyter-CadQuery) is unavailable—provide fallback approach so verification still passes.

## Assumptions

- Target operating systems are macOS 14+ and Ubuntu 22.04 LTS; Windows support can follow later phases.
- Team members have Python 3.12+ available or can install via pyenv/uv as part of the documented steps.
- Network access is available during setup to obtain packages and dependencies.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The specification MUST document a reproducible installation process for Build123d, CadQuery, NumPy, PyYAML, and visualization tooling, including command sequences and version targets.
- **FR-002**: The plan MUST require creation of an isolated Python environment (via uv, Poetry, or virtualenv) and define verification steps confirming the environment activates correctly.
- **FR-003**: The specification MUST define the repository directory structure, naming conventions, and required placeholder files so contributors can manually audit the scaffold before committing changes.
- **FR-004**: The specification MUST describe baseline utility modules for exporters, materials, and measurement calculations, including their intended inputs/outputs and acceptance checks.
- **FR-005**: The plan MUST define documentation deliverables (README outline, CHANGELOG initiation, documentation site stub) and the governance process for keeping them current.
- **FR-006**: The specification MUST outline manual validation checkpoints (e.g., checklists) to confirm toolchain readiness and directory compliance before closing Phase 0.                                            

### Key Entities *(include if feature involves data)*

- **Repository Skeleton**: Defines the directory tree, placeholder files, and documentation artifacts required for subsequent phases.                           
- **Utility Module Set**: Specifies shared helper libraries (exporters, materials, measurement) and their contracts.                                             

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A new workstation completes the Phase 0 setup checklist in under 60 minutes with zero unresolved dependency errors.
- **SC-002**: The repository structure validation passes with 100% compliance (all required directories/files present, no unexpected omissions).
- **SC-003**: At least 90% of team members report the documentation sufficient to reproduce the setup without requesting additional help during pilot onboarding.
