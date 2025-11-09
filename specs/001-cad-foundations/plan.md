# Implementation Plan: Phase 0 CAD Foundations

**Branch**: `001-cad-foundations` | **Date**: 2025-11-08 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-cad-foundations/spec.md`

## Summary

Phase 0 delivers the Build123d-focused CAD foundation for the project: a reproducible Python 3.12+ toolchain, repository scaffolding aligned with the constitution’s library-first doctrine, and shared utility modules with a `hello_gear` proof. The plan emphasizes environment automation, CLI access, and verification assets housed under a unified `generators` package that future gear and motor modules will extend.

## Technical Context

**Language/Version**: Python 3.12 (per constitution)  
**Primary Dependencies**: Build123d, CadQuery, numpy, pyyaml, rich, typer (CLI), uv (env manager)  
**Storage**: N/A (documentation and geometry generation utilities only)  
**Testing**: pytest with `just test` wrapper; unit + integration suites seeded in this phase  
**Target Platform**: Developer workstations on macOS 14+ and Ubuntu 22.04 LTS  
**Project Type**: Python library + CLI entry point  
**Performance Goals**: Environment verification CLI completes in <2 minutes; `hello_gear` export completes in <5 minutes on reference hardware  
**Constraints**: Must operate fully within uv-managed virtual environment; commands must emit structured logging via rich  
**Scale/Scope**: Supports initial internal team (<10 engineers) with consistent CAD outputs  
**Visualization Workflow**: Jupyter-CadQuery notebooks as default preview; CQ-Editor documented as optional GUI

## Constitution Check

- ✅ Library-First: Deliverables packaged under `src/generators/` with modular subpackages for core utilities, gears, and motors.  
- ✅ CLI Interface: Provide `gear-generator` CLI with `environment check`, `scaffold`, and `hello-gear` commands.  
- ✅ Test-First: Planning includes pytest suites (unit + integration) authored before implementations.  
- ✅ Integration Testing: `tests/integration/test_cli_environment.py` planned to exercise CLI end-to-end.  
- ✅ Observability: Commands emit structured logs via rich; configuration for log levels documented.  
- ✅ Additional Constraints: Python 3.12 baseline, uv workflow, pytest markers, enums for categorical values.  
- ✅ Governance: Outputs (plan, research, data-model) conform to Specify flow.

## Project Structure

### Documentation (this feature)

```text
specs/001-cad-foundations/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── README.md
└── checklists/
    └── requirements.md
```

### Source Code (repository root)

```text
src/
└── generators/
    ├── __init__.py
    ├── cli/
    │   ├── __init__.py
    │   └── main.py
    ├── core/
    │   ├── __init__.py
    │   ├── environment/
    │   │   ├── __init__.py
    │   │   ├── checks.py
    │   │   └── scaffold.py
    │   └── utils/
    │       ├── __init__.py
    │       ├── logging.py
    │       ├── tolerances.py
    │       ├── exporters.py
    │       ├── materials.py
    │       └── measurements.py
    ├── gears/
    │   └── __init__.py
    └── motors/
        └── __init__.py

examples/
└── hello_gear.py

tests/
├── unit/
│   ├── test_environment_checks.py
│   ├── test_scaffold_validator.py
│   ├── test_tolerances.py
│   └── test_exporters.py
└── integration/
    ├── test_cli_environment.py
    ├── test_cli_scaffold.py
    ├── test_cli_examples.py
    └── test_cli_tolerances.py
```

**Structure Decision**: Unified `generators` package exposes CLI and shared utilities under `core`, while reserving `gears` and `motors` subpackages for downstream phases; examples and tests live at repository root per constitution.

## Complexity Tracking

_No constitution violations anticipated; table not required._
