<!--
Sync Impact Report:
Version: template → 1.0.0
Initial creation for gear-generator project
Principles: Library-First, CLI Interface, Test-First, Integration Testing, Observability
Added sections: Additional Constraints (Python 3.12+), Development Workflow (Specify toolkit)
Templates: ✅ validated - all templates are generic and align with these principles
TODO: RATIFICATION_DATE - project is new, marking as initial ratification
-->

# Gear Generator Constitution

## Core Principles

### I. Library-First
Every feature starts as a standalone library with a clear, focused purpose.
Libraries MUST be self-contained, independently testable, and well-documented.
No organizational-only or scaffolding libraries—every library must deliver
measurable value. This principle ensures modularity, reusability, and clear
separation of concerns.

### II. CLI Interface
Every library MUST expose its functionality via a command-line interface.
Use text in/out protocol: stdin/args → stdout, errors → stderr. Support
both JSON (for programmatic use) and human-readable formats. This ensures
libraries are accessible, testable, and composable in scripts and pipelines.

### III. Test-First (NON-NEGOTIABLE)
TDD is mandatory for all feature development. The workflow is strict:
1. Tests written
2. User approval
3. Tests fail (verification)
4. Then implement

The Red-Green-Refactor cycle is strictly enforced. This prevents defects
and ensures test coverage from the start.

### IV. Integration Testing
Integration tests MUST be written for: new library contract tests,
contract changes, inter-library communication, and shared schemas. Unit
tests cover internal logic; integration tests verify real-world scenarios
and library interactions work correctly.

### V. Observability
All code MUST use structured logging for debugging and monitoring. The
rich library is preferred for colored output and callouts. Text I/O
protocols ensure debuggability. Logging levels MUST be appropriate:
DEBUG for development, INFO for normal operation, WARNING for issues,
ERROR for failures.

## Additional Constraints

### Technology Stack
- Python 3.12+ required
- Use `uv` for virtual environment and dependency management
- Prefer enums over magic strings for static values
- Avoid `Any` type—use concrete types
- Use pytest for testing with `just test` command
- Explicit pytest.mark.unit decorations required

### Code Quality
- All code MUST pass linting checks
- No disabling warnings in test commands
- Configuration models centralized in their own package
- Test plugins placed under tests system directory

## Development Workflow

### Specify Toolkit
This project uses the Specify toolkit for feature development:

1. **Specification**: Use `/speckit.specify` command to generate feature
   specs from user requirements
2. **Planning**: Use `/speckit.plan` command to create implementation
   plans with technical design
3. **Tasks**: Use `/speckit.tasks` command to generate actionable task
   lists from design documents
4. **Checklist**: Use `/speckit.checklist` command to create validation
   checklists

Each feature follows: spec.md → plan.md → tasks.md → implementation.
Feature specifications include user stories prioritized as P1, P2, P3.
Each user story MUST be independently testable and deliverable.

### Versioning
Dynamic versioning from `__init__.py`—versions MUST NOT be hardcoded
in pyproject.toml. Follow semantic versioning (MAJOR.MINOR.PATCH) for
releases.

## Governance

This constitution supersedes all other practices and must be respected
in all development work. All PRs and code reviews MUST verify compliance
with these principles.

Amendments require:
1. Documentation of the proposed change
2. Justification for the amendment
3. Update to this file with version bump
4. Synchronization with affected templates and documentation

Complexity MUST be justified—simpler alternatives rejected must be
documented. Use this constitution as the primary guidance for all
development decisions.

**Version**: 1.0.0 | **Ratified**: 2025-01-27 | **Last Amended**: 2025-01-27
