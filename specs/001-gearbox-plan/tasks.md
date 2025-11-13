---

description: "Task list template for feature implementation"
---

# Tasks: Spur & Helical Gear Planning

**Input**: Design documents from `/specs/001-gearbox-plan/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Test tasks are included because the specification and constitution emphasize validation and measurable outcomes.

**Organization**: Tasks are grouped by user story so each slice can be implemented and validated independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare baseline package and test scaffolding for gear planning work.

- [X] T001 Create gear planning package skeleton in `src/generators/gearboxes/__init__.py`                                                                      
- [X] T002 Establish test scaffolding modules for gear planning in `tests/unit/__init__.py` and `tests/integration/__init__.py`                                 

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core utilities and CLI structure required before any user story work.

**⚠️ CRITICAL**: Complete this phase before starting user stories.

- [ ] T003 [P] Reintroduce tolerance helpers (`fit_clearance`, `press_fit`, `angular_backlash_adjust`) in `src/generators/core/utils/tolerances.py`
- [ ] T004 [P] Extend `src/generators/cli/main.py` with `gear plan` command group (validate/export stubs)
- [ ] T005 Implement shared config loader utilities in `src/generators/gearboxes/schema.py`
- [ ] T006 [P] Create baseline validation test cases in `tests/unit/test_gear_configs.py`
- [ ] T007 [P] Create baseline CLI integration test harness in `tests/integration/test_cli_gear_plan.py`

---

## Phase 3: User Story 1 - Document Spur Gear Blueprint (Priority: P1) 🎯 MVP

**Goal**: Provide a complete spur gear planning workflow, including schema, builder, CLI validation, and documentation hooks.

**Independent Test**: Run `uv run python -m generators.cli.main gear plan validate --config configs/gear_core.spur_28.yaml --format json` and confirm status `valid` with spur-specific metrics logged.

### Implementation & Tests for User Story 1

- [ ] T008 [P] [US1] Populate spur schema sections in `configs/gear_core.yaml` (geometry, tolerances, validation metadata)
- [ ] T009 [P] [US1] Implement spur gear builder adhering to schema in `src/generators/gearboxes/spur.py`
- [ ] T010 [P] [US1] Add spur-specific validation rules (module/tooth/backlash checks) to `src/generators/gearboxes/schema.py`
- [ ] T011 [US1] Wire CLI `gear plan validate` handler to schema logic in `src/generators/cli/main.py`
- [ ] T012 [P] [US1] Add unit coverage for spur config acceptance/rejection in `tests/unit/test_gear_configs.py`
- [ ] T013 [US1] Add CLI integration scenario for spur validation in `tests/integration/test_cli_gear_plan.py`

**Checkpoint**: Spur gear planning pipelines (validate) function end-to-end.

---

## Phase 4: User Story 2 - Extend Plan for Helical Gear Variant (Priority: P2)

**Goal**: Layer helical-specific parameters, builders, and validation behaviors onto the shared spur foundation.

**Independent Test**: Run `uv run python -m generators.cli.main gear plan export --config configs/gear_core.helical_30.yaml --formats stl json` and confirm helix angle and handedness constraints are enforced.

### Implementation & Tests for User Story 2

- [ ] T014 [P] [US2] Extend `configs/gear_core.yaml` with helical geometry, helix angle, and handedness fields
- [ ] T015 [P] [US2] Implement helical gear builder in `src/generators/gearboxes/helical.py`
- [ ] T016 [US2] Enhance schema validation for helix angle limits and axial load notes in `src/generators/gearboxes/schema.py`
- [ ] T017 [US2] Update CLI export flow to handle helical builder selection in `src/generators/cli/main.py`
- [ ] T018 [P] [US2] Add unit coverage for helical config validation in `tests/unit/test_gear_configs.py`
- [ ] T019 [US2] Add integration scenario for helical export in `tests/integration/test_cli_gear_plan.py`

**Checkpoint**: Helical configurations validate and export independently of spur story code.

---

## Phase 5: User Story 3 - Validate Printability with Direct Gear Tests (Priority: P3)

**Goal**: Generate and verify direct gear test pairs, logging measurements back to configuration adjustments.

**Independent Test**: Run `uv run python -m generators.cli.main gear plan export --config configs/gear_core.spur_test.yaml --generate-test-pair --formats stl` and confirm test-pair assets and measurement guidance outputs.

### Implementation & Tests for User Story 3

- [ ] T020 [P] [US3] Implement gear test pair generator in `src/generators/gearboxes/test_pair.py`
- [ ] T021 [US3] Extend export workflow to emit test pair geometry and guidance in `src/generators/cli/main.py`
- [ ] T022 [P] [US3] Support `validation.test_pair` fields in `src/generators/gearboxes/schema.py`
- [ ] T023 [P] [US3] Add unit coverage for test pair configuration mapping in `tests/unit/test_gear_configs.py`
- [ ] T024 [US3] Add integration scenario for `--generate-test-pair` in `tests/integration/test_cli_gear_plan.py`

**Checkpoint**: Direct gear validation prints are generated and traceable to configuration adjustments.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, logging, and quality improvements spanning all stories.

- [ ] T025 [P] Update gear planning documentation in `docs/index.md` and `docs/utilities.md`
- [ ] T026 [P] Refresh quickstart workflow and examples in `specs/001-gearbox-plan/quickstart.md`
- [ ] T027 Validate CLI commands and document outputs in `docs/scaffold.md`
- [ ] T028 [US1] Add review checklist template updates and sign-off guidance in `specs/001-gearbox-plan/spec.md` and `specs/001-gearbox-plan/research.md`
- [ ] T029 [US1] Implement CLI support for logging review sign-offs in `src/generators/cli/main.py`
- [ ] T030 [US1] Add unit coverage for review logging behavior in `tests/unit/test_gear_configs.py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)** → Unblocked; start immediately.
- **Foundational (Phase 2)** → Depends on Phase 1 completion; BLOCKS all user stories.
- **User Stories (Phases 3–5)** → Each depends on foundational tasks; once Phase 2 completes, stories may proceed in priority order or in parallel if resourced.
- **Polish (Phase 6)** → Depends on completion of user stories targeted for release.

### User Story Dependencies

- **US1 (Spur)** → No dependency on other stories; only requires Phase 2.
- **US2 (Helical)** → Builds on shared schema/CLI; can start after Phase 2 but benefits from US1 completion for reuse.
- **US3 (Direct Gear Tests)** → Requires schema and CLI extensions from earlier stories; should start after US1 schema utilities are stable.

### Within Each User Story

1. Update configuration/data structures before building geometry.
2. Implement builders/services before wiring CLI commands.
3. Add unit coverage before integration scenarios.
4. Verify independent CLI command specified in each story checkpoint before advancing.

### Parallel Opportunities

- Setup tasks T001–T002 may proceed sequentially but are quick.
- Foundational tasks T003, T004, T006, and T007 marked [P] can be split by module/file.
- Within each user story, tasks marked [P] touch distinct files (config, builder, schema, tests) and can run concurrently once story begins.
- Different user stories can be staffed in parallel after Phase 2, provided shared schema changes are coordinated.

---

## Parallel Example: User Story 1

```bash
# Run in parallel after Phase 2 completion:
Task T008: Populate spur schema sections in configs/gear_core.yaml
Task T009: Implement spur builder in src/generators/gearboxes/spur.py
Task T010: Add spur validation rules in src/generators/gearboxes/schema.py
Task T012: Add unit coverage in tests/unit/test_gear_configs.py
```

---

## Implementation Strategy

### MVP First (Deliver User Story 1)

1. Complete Phases 1–2 to prepare utilities and CLI skeleton.
2. Execute Phase 3 tasks to deliver spur gear validation.
3. Run the independent CLI validation test and confirm documentation alignment.
4. Optionally ship MVP or gather feedback before extending to helical/test-pair work.

### Incremental Delivery

- After MVP, implement Phase 4 (helical) to expand capability while keeping spur workflow intact.
- Follow with Phase 5 to add direct gear test generation.
- Close with Phase 6 polish tasks to align docs and operational guidance.

### Parallel Team Strategy

- Team completes Phases 1–2 collaboratively.
- Assign developers by story:
  - Dev A: US1 spur workflow
  - Dev B: US2 helical upgrades
  - Dev C: US3 direct gear validation
- Synchronize on shared schema/CLI touchpoints before merging.

---

## Notes

- [P] tasks touch distinct files or are independent by design.
- Story labels map directly to spec user stories for traceability.
- Ensure each story’s independent CLI command passes before moving forward.
- Follow Test-First principle: write/adjust tests before implementing corresponding logic.
- Commit after each task or cohesive story milestone.
