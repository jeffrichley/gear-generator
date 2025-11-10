# Implementation Plan: Phase 0 CAD Foundations

**Branch**: `001-cad-foundations` | **Date**: 2025-11-08 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-cad-foundations/spec.md`

## Summary

Phase 0 delivers the Build123d-focused CAD foundation for the project: a reproducible Python 3.12+ toolchain, repository scaffolding aligned with the constitution’s library-first doctrine, and shared utility modules for exporters, materials, and measurements. The plan keeps a lightweight CLI entrypoint reserved for future commands while focusing on shared utilities and documentation housed under a unified `generators` package that future gear and motor modules will extend.

## Technical Context

**Language/Version**: Python 3.12 (per constitution)  
**Primary Dependencies**: Build123d, CadQuery, numpy, pyyaml, rich, typer (CLI), uv (env manager)  
**Storage**: N/A (documentation and geometry generation utilities only)  
**Testing**: pytest with `just test` wrapper; unit suite seeded in this phase
**Target Platform**: Developer workstations on macOS 14+ and Ubuntu 22.04 LTS  
**Project Type**: Python library + CLI entry point  
**Performance Goals**: Utility helpers execute quickly (seconds) to keep iteration tight on reference hardware
**Constraints**: Must operate fully within uv-managed virtual environment; commands must emit structured logging via rich  
**Scale/Scope**: Supports initial internal team (<10 engineers) with consistent CAD outputs  
**Visualization Workflow**: Jupyter-CadQuery notebooks as default preview; CQ-Editor documented as optional GUI

## Constitution Check

- ✅ Library-First: Deliverables packaged under `src/generators/` with modular subpackages for core utilities, gears, and motors.  
- ✅ CLI Interface: Provide a `gear-generator` CLI entrypoint for future commands (currently a placeholder hook).
- ✅ Test-First: Planning includes pytest suites (unit tests) authored before implementations.
- ✅ Observability: Helper modules emit structured logs via rich where applicable; configuration for log levels documented.
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
    │   └── utils/
    │       ├── __init__.py
    │       ├── log_utils.py
    │       ├── exporters.py
    │       ├── materials.py
    │       └── measurements.py
    ├── gears/
    │   └── __init__.py
    └── motors/
        └── __init__.py

tests/
├── unit/
│   └── test_exporters.py
└── integration/
    └── __init__.py
```

**Structure Decision**: Unified `generators` package exposes CLI and shared utilities under `core`, while reserving `gears` and `motors` subpackages for downstream phases; tests live at repository root per constitution.

## Complexity Tracking

_No constitution violations anticipated; table not required._
