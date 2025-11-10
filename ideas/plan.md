# Parametric Powertrain Plan

## Phase 0 — Foundations & Environment

- [x] ### Subphase 0.1 — Environment & Toolchain
  - [x] Install `build123d`, `cadquery`, `numpy`, `pyyaml`, and supporting visualization tools (CQ-Editor or Jupyter-CadQuery).
  - [x] Stand up a dedicated virtual environment and package manager workflow (`uv` or `poetry`).
  - [x] Verify STL/STEP export and preview pipeline for rapid iteration.

- [x] ### Subphase 0.2 — Repository & Documentation Scaffolding
  - [x] Establish project layout: `src/motors`, `src/gearboxes`, `src/utils`, `src/examples`, `src/tests`, plus `configs/` and `data/`.
  - [x] Seed `README.md`, `CHANGELOG.md`, and initialize MkDocs or Sphinx for rendered documentation.
  - [x] Configure semantic versioning and Git conventions for design iterations.

- [ ] ### Subphase 0.3 — Parametric CAD Scaffolding
  - [ ] Create reusable YAML schemas: `gear_core.yaml` (module, tooth count, backlash, pressure angle, helix angle, face width, clearance) and `motor_core.yaml` (stator slots, poles, airgap, magnet dimensions, coil spec, stack height).
  - [ ] Implement foundational Build123d templates: gear hub, carrier, ring, sun, output plates, stator/rotor plates, spacers, bearing blocks.
  
- [ ] ### Subphase 0.4 — Utilities & Tolerance Helpers
  - [x] Implement `utils/tolerances.py` for press fits, clearance classes, and printable fit test coupons.
  - [ ] Add component data utilities
    - [x] `utils/materials.py`
    - [ ] `utils/bearings.py`
    - [ ] `utils/magnets.py`
    - [ ] `utils/fasteners.py`
  - [x] Provide `utils/exporters.py` and `utils/measurements.py` for STL/STEP export, mass properties, torque, and inertia calculations.

- [ ] ### Subphase 0.5 — Test & Metrology Rig Designs
  - [ ] Model torque dyno (reaction arm + load cell), optical tachometer mounts, and current/voltage logging harnesses.
  - [ ] Design backlash gauge fixtures, rotor balancing jigs, and efficiency measurement scripts.
  - [ ] Document target measurement workflows for repeatable validation.

## Phase 1 — Parametric Core Development

- [ ] ### Subphase 1.1 — Base Geometry Engine
  - [ ] Create a `GearBase` class encapsulating shared parameters (module, width, backlash, helix angle).
  - [ ] Implement a reusable involute profile generator with error compensation for printed teeth.
  - [ ] Integrate tolerance offsets directly into feature creation logic.

- [ ] ### Subphase 1.2 — Gear Part Library MVP
  - [ ] Deliver parametric `SpurGear`, `HelicalGear`, `PlanetarySet`, `CycloidalDisc`, and `FlexSpline` classes.
  - [ ] Capture key attributes: tooth counts, module, pressure angle, helix angle, reduction ratios, pin counts, wall thickness, and material adjustments.
  - [ ] Validate with quick prints to confirm backlash targets and tooth integrity.

- [ ] ### Subphase 1.3 — Motor Geometry Primitives
  - [ ] Implement `RotorCan`, `StatorCore`, `AxialRotor`, and `AxialStator` parametric classes covering poles, slot counts, coil thickness, magnet arc angles, and airgap spacing.
  - [ ] Include balancing, magnet retention, and coil former features in each design.

- [ ] ### Subphase 1.4 — Test Rig Parametrics
  - [ ] Generate parametric reaction-arm torque testers, rotor balancing fixtures, and gear backlash gauges within Build123d.
  - [ ] Ensure fixtures share the tolerance helper utilities for consistent printer compensation.

## Phase 2 — Configuration & Automation Layer

- [ ] ### Subphase 2.1 — Config Schema & Validation
  - [ ] Define YAML configuration schemas for gears, motors, and assemblies; load via dataclasses with validation (`pydantic` or `voluptuous`).
  - [ ] Maintain config versions for material/printer variations and design families.

- [ ] ### Subphase 2.2 — Batch Generation & Metadata
  - [ ] Script automated sweeps that iterate configs, build geometry, and export STL/STEP assets.
  - [ ] Log metadata (mass, inertia, reduction ratio, torque capacity estimates) to CSV for analysis.

- [ ] ### Subphase 2.3 — Hello-World Examples
  - [ ] Create `examples/hello_gear.py`, `examples/hello_motor.py`, and `examples/hello_joint.py` showcasing end-to-end parametric workflows.
  - [ ] Demonstrate tolerance helpers and exporter utilities within each example.

## Phase 3 — Gearbox Family Development

- [ ] ### Subphase 3.1 — Spur & Helical Foundations
  - [ ] Refine involute profiles with tip relief, crowning options, and helix angle sweeps.
  - [ ] Provide printable test coupons to calibrate backlash, pitch error, and contact patterns.

- [ ] ### Subphase 3.2 — Planetary Gearsets
  - [ ] Deliver 1-stage, 2-stage, and high-ratio planetary modules with swappable sun/planet/ring components.
  - [ ] Integrate auto-ratio calculators, bearing seat generators, and carrier templates.
  - [ ] Validate backlash (<0.5–1°) and torque capacity with printed prototypes.

- [ ] ### Subphase 3.3 — Cycloidal Drives
  - [ ] Generate eccentric cam discs, pin-plate arrays, and eccentric carriers with pin diameter compensation.
  - [ ] Include options for needle versus printed pins and shock-load analysis.

- [ ] ### Subphase 3.4 — Strain-Wave / Harmonic Drives
  - [ ] Model TPU/compliant flexsplines, aluminum or printed wave generators, and circular spline rings.
  - [ ] Start ratios at 30–50:1 before scaling to 100+:1; verify zero-backlash potential and flex durability.

- [ ] ### Subphase 3.5 — Differential Epicyclic Modules
  - [ ] Design Ravigneaux/Simpson-style differential gearsets for compound reductions and steering use cases.
  - [ ] Parameterize power split ratios and carrier interconnects.

- [ ] ### Subphase 3.6 — Worm & Worm-Helical Hybrids
  - [ ] Implement self-locking worm stages with efficiency modeling and heat buildup validation.
  - [ ] Explore worm-helical combos for vertical load applications.

- [ ] ### Subphase 3.7 — Bevel & Spiral Bevel Options
  - [ ] Add right-angle gearing with adjustable pressure angles and printable tolerancing strategies.
  - [ ] Reserve for later stages once printer accuracy is proven.

- [ ] ### Subphase 3.8 — Build Order Milestone
  - [ ] Confirm spur → helical → planetary → cycloidal → strain-wave → differential → worm → bevel progression.
  - [ ] Document “done” criteria: backlash targets, tooth strength, efficiency curves, BOM with standard bearings/shafts, auto-generated drawings.

## Phase 4 — Motor Family Development

- [ ] ### Subphase 4.1 — Radial Flux BLDC Outrunner
  - [ ] Develop 12N14P and 24N28P variants with printed stator holders, magnet retention, and balancing jigs.
  - [ ] Measure torque versus current and validate coil winding workflows.

- [ ] ### Subphase 4.2 — Radial Flux BLDC Inrunner
  - [ ] Create compact inrunner designs optimized for high RPM and gearbox integration; include encoder mounts.

- [ ] ### Subphase 4.3 — Axial Flux Single Rotor
  - [ ] Produce flattened rotor/stator assemblies with steel backing rotors, N52 magnet arcs, and printed airgap shims.

- [ ] ### Subphase 4.4 — Axial Flux Dual Rotor (Yokeless)
  - [ ] Implement symmetric flux paths, alignment strategies, and airgap tuning mechanisms.

- [ ] ### Subphase 4.5 — Coreless & PCB Stator Motors
  - [ ] Model air-core coil carriers, PCB winding layouts, and visualize winding paths.

- [ ] ### Subphase 4.6 — Switched Reluctance Prototype
  - [ ] Prototype magnet-free SRM with laminated printed steel cores and control experimentation.

- [ ] ### Subphase 4.7 — Motor Milestone
  - [ ] Achieve measured Kv/Ke, torque constants, no-load current, efficiency >70%, and safe rotor retention at maximum RPM.

## Phase 5 — Integrated Drive Modules

- [ ] ### Subphase 5.1 — Standard Actuator Builds
  - [ ] Combine outrunner motors with spur/helical and planetary gearboxes for baseline joints.
  - [ ] Create outrunner + cycloidal modules for impact-resistant applications.
  - [ ] Integrate axial flux motors with strain-wave gearboxes for slim, zero-backlash joints.

- [ ] ### Subphase 5.2 — Advanced Combinations
  - [ ] Explore dual-stage reductions (planetary → harmonic) for ultra-high ratios.
  - [ ] Design differential dual-motor units for experimental power split control.

- [ ] ### Subphase 5.3 — Packaging & Instrumentation
  - [ ] Add encoder housings, cable routing, mounting flanges, and M3/M4 heat-set insert patterns.
  - [ ] Standardize shafting (5 mm, 8 mm, 10 mm keyed/D-flat) and bearing selections (608, 6805, 6810, 5×16×5, 8×22×7).

- [ ] ### Subphase 5.4 — Integration Milestone
  - [ ] Define actuator module specs: output torque, peak/continuous ratings, backlash, audible noise, assembly time.

## Phase 6 — Testing, Optimization & Materials

- [ ] ### Subphase 6.1 — Validation Playbook
  - [ ] Execute static torque tests (reaction arm + load cell) for stall and breakaway torque.
  - [ ] Capture dynamic torque vs RPM vs current data, efficiency maps, and temperature rise at 5/15/30 minutes.
  - [ ] Measure backlash and stiffness under ±τ cycles and document noise (dBA @ 0.5 m).

- [ ] ### Subphase 6.2 — Material & Durability Passes
  - [ ] Progress through material ladder: PLA+ → PETG → ASA → Nylon → Nylon-CF; apply TPU for flexsplines/bushings.
  - [ ] Conduct 100-hour endurance runs, dust ingress tests, relube interval studies, and printed pin wear analysis.

- [ ] ### Subphase 6.3 — Optimization Campaigns
  - [ ] Add tooth profile refinements (tip relief, crowning, lubricant pockets) and helix angle sweeps for noise reduction.
  - [ ] Pursue weight reduction with lattice infill regions and perform simplified thermal simulations.

## Phase 7 — Showcase & Extensions

- [ ] ### Subphase 7.1 — Documentation & Guides
  - [ ] Auto-generate build guides, exploded views, section diagrams, and print setting tables from configuration metadata.
  - [ ] Publish comprehensive joint spec sheets aligned with ISO-style reporting.

- [ ] ### Subphase 7.2 — Interactive & Web Experiences
  - [ ] Develop interactive param configurator notebooks for live geometry previews.
  - [ ] Optional FastAPI + Three.js viewer to share parametric designs online.

- [ ] ### Subphase 7.3 — Community & Release
  - [ ] Release the library ("build123d-motorgearbox") on GitHub with example configs and STL bundles.
  - [ ] Launch a community challenge (“Print your ratio!”) to encourage feedback and refinements.

- [ ] ### Subphase 7.4 — Roadmap Wrap-Up
  - [ ] Summarize TL;DR build order and highlight future research tracks beyond rotary systems (e.g., planar/tubular linear motors).
  - [ ] Catalogue residual risks, testing gaps, and prioritized backlog items for the next development cycle.
