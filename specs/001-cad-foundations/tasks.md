# Tasks: Phase 0 CAD Foundations

**Input**: Design documents from `/specs/001-cad-foundations/`
**Prerequisites**: plan.md (required), spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Constitution enforces test-first. Each user story phase begins with failing tests before implementation.

**Organization**: Tasks grouped by user story to ensure independent delivery and validation.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initialize repository tooling and dependency management

- [X] T001 Create `pyproject.toml` with Python 3.12 and pinned dependencies (Build123d 0.6.x, CadQuery 2.4.x, numpy, pyyaml, rich, typer) at repository root
- [X] T002 Generate `uv.lock` by running `uv sync` to capture deterministic environment
- [X] T003 Add `justfile` with `just test` invoking `uv run pytest -m "unit or integration"`
- [X] T004 Configure MkDocs Material skeleton under `docs/` with `mkdocs.yml`
- [X] T005 [P] Update `.gitignore` to include `/.venv`, `/uv.lock`, `/outputs`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Prepare shared package structure and test scaffolding (must precede user stories)

- [X] T006 Create package directories and placeholders per plan (`src/generators/__init__.py`, `src/generators/cli/__init__.py`, `src/generators/core/__init__.py`, `src/generators/core/utils/__init__.py`, `src/generators/gears/__init__.py`, `src/generators/motors/__init__.py`)
- [X] T007 Create `outputs/` directory scaffolding for generated artifacts
- [X] T008 Create test layout (`tests/unit/__init__.py`, `tests/integration/__init__.py`, `tests/fixtures/__init__.py`)
- [X] T009 Implement pytest configuration (`pytest.ini`) enforcing `pytest.mark.unit` and `pytest.mark.integration`
- [X] T010 [P] Add Rich-based logging helper in `src/generators/core/utils/log_utils.py` with stub implementation
- [X] T011 [P] Scaffold CLI entrypoint `src/generators/cli/main.py` with a Typer app placeholder for future commands
- [X] T012 Document developer guidelines in `docs/README.md` referencing Quickstart flow

---

## Phase 3: User Story 1 – Shared Utility Modules (Priority: P1) 🎯 MVP

**Goal**: Provide reusable exporter, materials, and measurement utilities.

**Independent Test**: Exporter and measurement unit tests validate metadata generation and calculations.

### Tests (write first)

- [X] T027 [US1] Add unit tests for exporter metadata logging in `tests/unit/test_exporters.py`

### Implementation

- [X] T031 [P] [US1] Implement exporter utilities (STL/STEP + metadata) in `src/generators/core/utils/exporters.py`
- [X] T032 [US1] Implement materials and measurement utilities in `src/generators/core/utils/materials.py` and `src/generators/core/utils/measurements.py`
- [X] T036 [US1] Document utilities in `docs/utilities.md`

**Checkpoint**: Utilities export artifacts; tests green.

---

## Phase 5: User Story 3 – Deliver Shared Utility Modules (Priority: P3)

**Goal**: Provide reusable exporter, materials, and measurement utilities

**Independent Test**: Exporter and measurement unit tests validate metadata generation and calculations

### Tests (write first)

- [X] T027 [P] [US3] Add unit tests for exporter metadata logging in `tests/unit/test_exporters.py`

### Implementation

- [X] T031 [P] [US3] Implement exporter utilities (STL/STEP + metadata) in `src/generators/core/utils/exporters.py`
- [X] T032 [US3] Implement materials and measurement utilities in `src/generators/core/utils/materials.py` and `src/generators/core/utils/measurements.py`
- [X] T036 [US3] Document utilities in `docs/utilities.md`

**Checkpoint**: Utilities export artifacts; tests green.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Clean up, documentation, and release readiness

- [X] T037 [P] Add MkDocs pages for scaffold and utilities and enable navigation in `mkdocs.yml`
- [X] T038 [P] Run `just test` and ensure CI configuration (e.g., `.github/workflows/tests.yml`) exists or is updated
- [X] T039 Perform code linting/formatting pass (`uv run ruff format` / `ruff check`) and resolve issues
- [X] T040 Finalize CHANGELOG entry for Phase 0 foundations in `CHANGELOG.md`
- [X] T041 [P] Capture sample outputs (screenshots or JSON) and store under `docs/assets/`

---

## Dependencies & Execution Order

### Phase Dependencies

1. **Phase 1 Setup** → establishes tooling baseline
2. **Phase 2 Foundational** → depends on Phase 1; blocks user stories
3. **Phase 3 (US1)** → depends on Phase 2
4. **Phase 6 Polish** → depends on completion of targeted user stories

### User Story Dependencies

- **US1 (P1)**: No dependencies beyond foundational; forms MVP

### Task-Level Notes

- Tests (T027) must be written before corresponding implementation tasks in each phase
- Documentation updates (T036, T037) can run parallel after respective features implemented

---

## Parallel Opportunities

- Phase 1: T005 can run parallel after initial files exist
- Phase 2: T010 and T011 parallelizable while others set up directories
- US1: T031 and T036 can run after the exporter tests (T027) are in place
- Polish phase contains multiple parallel documentation/ops tasks

---

## Implementation Strategy

### MVP (Deliver US1 only)

1. Complete Phases 1–2
2. Execute all US1 tasks (tests → implementation → docs)
3. Validate via the exporter/measurement unit tests (`uv run pytest -m unit`)
4. Optionally release internal tooling guide

### Incremental Delivery

- After MVP, consider layering additional tooling (e.g., scaffold automation) once utility workflows stabilize. Each increment should remain independently valuable.

### Team Parallelization

- Developer A: Leads US1 (shared utilities)
- Developer B: Focuses on documentation polish (T036, T037)
- Shared documentation tasks coordinated during polish phase

