# Implementation Plan: Spur & Helical Gear Planning

**Branch**: `001-gearbox-plan` | **Date**: November 10, 2025 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-gearbox-plan/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Document the reusable planning assets needed to deliver printable spur and helical gears. This includes defining the canonical `gear_core.yaml` schema, validation heuristics (e.g., 0.5°–1.0° backlash targets), direct gear test guidance, and cross-functional review checkpoints so engineers, designers, and fabrication technicians can execute Phase 1 gearbox work with minimal rework.

## Technical Context

**Language/Version**: Python 3.12+
**Primary Dependencies**: Build123d, CadQuery, PyYAML, NumPy
**Storage**: Local file system (YAML configs, generated STLs/STEPs)
**Testing**: pytest (unit + integration), `just test`
**Target Platform**: Cross-platform CLI (macOS/Linux CI)
**Project Type**: Library-first Python package with CLI entrypoints
**Performance Goals**: Generate spur/helical geometry + validation test meshes in < 10 seconds per configuration on developer hardware
**Constraints**: Maintain 0.5°–1.0° backlash target, enforce structured logging, ensure CLI supports both human-readable and JSON reporting
**Scale/Scope**: Initial library supports up to 10 gear variants per run with extensible YAML schema for future gearbox families

## Constitution Check

- **Library-First**: PASS — planning outputs expand reusable configuration and documentation assets for existing library structure.
- **CLI Interface**: PASS — plan reinforces CLI workflows by documenting required commands and outputs.
- **Test-First**: PASS — plan mandates direct gear verification and YAML validation tests before geometry implementation.
- **Integration Testing**: PASS — outlines cross-functional review and tooling validation which will translate into integration tests.
- **Observability**: PASS — constraints call for structured logging and measurement traceability.
- **Technology Stack (Python 3.12+, uv, pytest)**: PASS — conforms to mandated tooling.

All gates satisfied; Phase 0 may proceed.

### Post-Design Check (after Phase 1)

Re-evaluated after generating research, data model, contracts, and quickstart:
- **Library-First**: PASS — design artifacts reinforce reusable modules without adding throwaway scaffolding.
- **CLI Interface**: PASS — quickstart and contracts maintain CLI plus JSON pathways.
- **Test-First**: PASS — plan mandates schema/unit tests prior to geometry generation.
- **Integration Testing**: PASS — API contract and CLI integration test placeholders ensure end-to-end validation.
- **Observability**: PASS — plan calls for structured logging and measurement traceability in workflows.
- **Technology Stack**: PASS — design sticks with Python 3.12+, uv, pytest, Build123d ecosystem.

## Project Structure

### Documentation (this feature)

```text
specs/001-gearbox-plan/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
src/
├── generators/
│   ├── cli/
│   │   └── main.py
│   ├── core/
│   │   ├── utils/
│   │   │   ├── exporters.py
│   │   │   ├── materials.py
│   │   │   ├── measurements.py
│   │   │   └── tolerances.py  # to (re)introduce per plan guidance
│   │   └── __init__.py
│   └── gearboxes/
│       ├── spur.py            # new parametric spur planning/build rules
│       └── helical.py         # new parametric helical planning/build rules
│       ├── schema.py         # shared config parsing and validation logic
│       └── test_pair.py      # production-geometry validation pair generation

configs/
└── gear_core.yaml             # canonical schema + exemplars

tests/
├── unit/
│   └── test_gear_configs.py   # schema + validation coverage
└── integration/
    └── test_cli_gear_plan.py  # CLI + direct gear workflow validation
```

**Structure Decision**: Extend existing `src/generators` package with dedicated `gearboxes` modules and restore shared tolerance utilities; back the plan with configuration-driven tests under `tests/unit` and CLI coverage under `tests/integration`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|--------------------------------------|
