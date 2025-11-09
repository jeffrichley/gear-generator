# Changelog

All notable changes to this project will be documented in this file. The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-11-09

### Added
- Python 3.12 toolchain managed by uv with deterministic locking and just-based workflows.
- `gear-generator` CLI commands for environment verification, repository scaffolding, tolerance calibration, and the `hello-gear` example export.
- Shared utility modules covering logging, exporters, tolerances, materials, and measurements with persisted JSON/YAML reports.
- Documentation set including MkDocs navigation, quickstart onboarding, environment/scaffold guides, and captured sample outputs.

### Testing
- Unit and integration test suites exercising environment checks, scaffold validation, utility flows, and CLI usage via `just test`.
