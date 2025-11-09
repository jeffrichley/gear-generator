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
- [X] T005 [P] Update `.gitignore` to include `/.venv`, `/uv.lock`, `/outputs`, `/data/tolerances/*.yaml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Prepare shared package structure, CLI wiring, and test scaffolding (must precede user stories)

- [X] T006 Create package directories and placeholders per plan (`src/generators/__init__.py`, `src/generators/cli/__init__.py`, `src/generators/core/__init__.py`, `src/generators/core/environment/__init__.py`, `src/generators/core/utils/__init__.py`, `src/generators/gears/__init__.py`, `src/generators/motors/__init__.py`)
- [X] T007 Create `examples/` and `outputs/examples/.gitkeep` directories
- [X] T008 Create test layout (`tests/unit/__init__.py`, `tests/integration/__init__.py`, `tests/fixtures/__init__.py`)
- [X] T009 Implement pytest configuration (`pytest.ini`) enforcing `pytest.mark.unit` and `pytest.mark.integration`
- [X] T010 [P] Add Rich-based logging helper in `src/generators/core/utils/logging.py` with stub implementation
- [X] T011 [P] Scaffold CLI entrypoint `src/generators/cli/main.py` registering Typer app with placeholder commands (`env`, `repo`, `examples`, `tolerances`)
- [X] T012 Document developer guidelines in `docs/README.md` referencing Quickstart flow

---

## Phase 3: User Story 1 – Stand Up the CAD Toolchain (Priority: P1) 🎯 MVP

**Goal**: Provide reproducible environment verification CLI for Build123d toolchain

**Independent Test**: Running `uv run gear-generator env verify` on a clean workstation reports readiness (JSON + table) or actionable failures

### Tests (write first)

- [X] T013 [US1] Create failing unit tests for environment checks in `tests/unit/test_environment_checks.py` covering Python version, uv activation, dependency import
- [X] T014 [P] [US1] Create failing integration test invoking CLI `env verify` in `tests/integration/test_cli_environment.py`

### Implementation

- [X] T015 [US1] Implement dependency probing logic in `src/generators/core/environment/checks.py` returning `EnvironmentProfile`
- [X] T016 [US1] Implement CLI command `env verify` in `src/generators/cli/main.py` with JSON/table output and rich logging
- [X] T017 [US1] Serialize verification output to `data/environment/profile.json` using helpers in `src/generators/core/utils/exporters.py`
- [X] T018 [US1] Update Quickstart section for environment verification in `specs/001-cad-foundations/quickstart.md`
- [X] T019 [US1] Document command usage in `docs/environment.md`

**Checkpoint**: Env verification passes locally; tests green.

---

## Phase 4: User Story 2 – Establish the Repository Skeleton (Priority: P2)

**Goal**: Scaffold repository directories/files and validate against defined structure

**Independent Test**: Running `uv run gear-generator repo scaffold --root . --dry-run` reports compliance; `--autofix` creates missing nodes

### Tests (write first)

- [X] T020 [US2] Add failing unit tests for scaffold validation logic in `tests/unit/test_scaffold_validator.py`
- [X] T021 [P] [US2] Add integration test covering `repo scaffold` CLI flow in `tests/integration/test_cli_scaffold.py`

### Implementation

- [X] T022 [US2] Implement scaffold specification constants in `src/generators/core/environment/scaffold.py`
- [X] T023 [US2] Implement CLI command `repo scaffold` in `src/generators/cli/main.py` supporting `--autofix`
- [X] T024 [US2] Emit structured reports persisted to `data/scaffold/report.json`
- [X] T025 [US2] Update documentation tree description in `docs/scaffold.md`

**Checkpoint**: Scaffold command passes tests; directories auto-created when missing.

---

## Phase 5: User Story 3 – Deliver Shared Utility Modules (Priority: P3)

**Goal**: Provide reusable tolerance, exporter, materials, and measurement utilities plus hello gear example

**Independent Test**: Running `uv run gear-generator examples hello-gear` exports STL/STEP; tolerance coupon command generates artifact and records YAML measurements

### Tests (write first)

- [X] T026 [US3] Add unit tests for tolerance offsets and fit coupon generation in `tests/unit/test_tolerances.py`
- [X] T027 [P] [US3] Add unit tests for exporter metadata logging in `tests/unit/test_exporters.py`
- [X] T028 [P] [US3] Add integration test for `examples hello-gear` CLI in `tests/integration/test_cli_examples.py`
- [X] T029 [US3] Add integration test for `tolerances coupon/record` flow in `tests/integration/test_cli_tolerances.py`

### Implementation

- [X] T030 [US3] Implement tolerance helpers and coupon generator in `src/generators/core/utils/tolerances.py`
- [X] T031 [P] [US3] Implement exporter utilities (STL/STEP + metadata) in `src/generators/core/utils/exporters.py`
- [X] T032 [US3] Implement materials and measurement utilities in `src/generators/core/utils/materials.py` and `src/generators/core/utils/measurements.py`
- [X] T033 [US3] Implement hello gear Build123d script in `examples/hello_gear.py`
- [X] T034 [US3] Wire CLI commands `examples hello-gear` and `tolerances coupon/record` in `src/generators/cli/main.py`
- [X] T035 [US3] Persist tolerance profiles to `data/tolerances/{printer}.yaml` with schema from data model
- [X] T036 [US3] Document utilities in `docs/utilities.md` and extend Quickstart calibration steps

**Checkpoint**: Utilities export artifacts; tests green.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Clean up, documentation, and release readiness

- [X] T037 [P] Add MkDocs pages for environment, scaffold, utilities and enable navigation in `mkdocs.yml`
- [X] T038 [P] Run `just test` and ensure CI configuration (e.g., `.github/workflows/tests.yml`) exists or is updated
- [X] T039 Perform code linting/formatting pass (`uv run ruff format` / `ruff check`) and resolve issues
- [X] T040 Finalize CHANGELOG entry for Phase 0 foundations in `CHANGELOG.md`
- [X] T041 [P] Capture sample outputs (screenshots or JSON) and store under `docs/assets/`

---

## Dependencies & Execution Order

### Phase Dependencies

1. **Phase 1 Setup** → enables environment tooling
2. **Phase 2 Foundational** → depends on Phase 1; blocks user stories
3. **Phase 3 (US1)** → depends on Phase 2
4. **Phase 4 (US2)** → depends on Phase 2
5. **Phase 5 (US3)** → depends on Phase 2; can start after US1 but runs independently
6. **Phase 6 Polish** → depends on completion of targeted user stories

### User Story Dependencies

- **US1 (P1)**: No dependencies beyond foundational; forms MVP
- **US2 (P2)**: Independent once foundational complete; can run parallel to US1 if team split
- **US3 (P3)**: Independent once foundational complete; shares CLI file changes with other stories—coordinate merges

### Task-Level Notes

- Tests (T013–T014, T020–T021, T026–T029) must be written before corresponding implementation tasks in each phase
- CLI wiring tasks (T016, T023, T034) require baseline CLI scaffold (T011)
- Documentation updates (T019, T025, T036, T037) can run parallel after respective features implemented

---

## Parallel Opportunities

- Phase 1: T005 can run parallel after initial files exist
- Phase 2: T010 and T011 parallelizable while others set up directories
- US1: T014 integration test can run while T013 is authored; T017–T019 parallel after core implementation (T015–T016)
- US2: T021 integration test and T022 implementation can progress once validator contracts defined
- US3: T027 and T028 can run parallel; T031 parallel with T030 after tolerance API contract stable
- Polish phase contains multiple parallel documentation/ops tasks

---

## Implementation Strategy

### MVP (Deliver US1 only)

1. Complete Phases 1–2
2. Execute all US1 tasks (tests → implementation → docs)
3. Validate via `uv run gear-generator env verify` and test suite
4. Optionally release internal tooling guide

### Incremental Delivery

- After MVP, add US2 scaffold automation, validate independently, then proceed to US3 utilities. Each story maintains standalone value.

### Team Parallelization

- Developer A: Leads US1 (environment CLI)
- Developer B: Leads US2 (repo scaffold)
- Developer C: Leads US3 (utilities) once foundational ready
- Shared documentation tasks coordinated during polish phase

