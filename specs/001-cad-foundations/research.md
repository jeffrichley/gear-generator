# Research Summary — Phase 0 CAD Foundations

## Decision 1: Default Visualization Workflow
- **Decision**: Adopt Jupyter-CadQuery notebooks as the default preview tool; offer CQ-Editor as optional add-on.  
- **Rationale**: Jupyter-CadQuery works cross-platform with minimal GUI dependencies, aligns with Python-first workflow, and supports inline snapshots useful for documentation.  
- **Alternatives Considered**:  
  - *CQ-Editor as default*: Rejected because Qt dependencies complicate Linux headless setups.  
  - *FreeCAD workbench*: Overkill for scripted geometry, adds heavy install burden.  
  - *Text-only STL export*: Lacks interactive inspection, harder for early validation.

## Decision 2: Environment Verification Strategy
- **Decision**: Provide a `gear-generator env verify` CLI command that imports core dependencies, checks Python 3.12+, validates uv environment activation, and reports versions in JSON and human-readable formats.  
- **Rationale**: Matches constitution’s CLI mandate, enables automated CI checks, and gives immediate feedback to onboarding engineers.  
- **Alternatives Considered**:  
  - *Manual checklist only*: Error-prone and hard to automate.  
  - *Custom shell script*: Less portable across shells and misses Python import verification.

## Decision 3: Dependency Pinning Policy
- **Decision**: Pin Build123d to 0.6.x and CadQuery to 2.4.x with uv-managed `pyproject.toml`, locking minor versions while allowing patch updates.  
- **Rationale**: These releases are stable on Python 3.12 and widely used; uv lock files keep reproducibility without freezing patch fixes.  
- **Alternatives Considered**:  
  - *Latest floating versions*: Risk of breaking changes.  
  - *Fully frozen versions*: Increases maintenance overhead when security fixes release.

## Decision 4: Tolerance Calibration Assets
- **Decision**: Generate a printable fit-coupon STL via `gear-generator tolerances coupon` with embossed offsets (-0.2 mm to +0.2 mm) and record measured fits in YAML under `data/tolerances/{printer}.yaml`.  
- **Rationale**: Provides repeatable calibration workflow and structured data storage for future automation.  
- **Alternatives Considered**:  
  - *Ad-hoc measurements*: Inconsistent and not versionable.  
  - *External calibration tools*: Adds dependencies and cost, not necessary for PLA/PETG baseline.

## Decision 5: Documentation Tooling
- **Decision**: Use MkDocs Material to host environment guides and utility references generated from Markdown in `docs/`.  
- **Rationale**: Lightweight static site that integrates well with Markdown, easy to publish later; aligns with library-first documentation needs.  
- **Alternatives Considered**:  
  - *Sphinx*: Heavier config, more suitable for API docstrings.  
  - *GitHub Wiki*: Less version-controlled, harder to enforce reviews.

All identified clarifications are resolved; plan proceeds to design phase.
