# The Foundations of Genesis Physics — Claude Instructions

You are working on the **Foundations Series** — a 6-volume graduate textbook that derives ALL of physics from zone architecture axioms. This is the bedrock of the entire Genesis Physics project. **Everything depends on this being right.**

## Build Order: THIS IS FIRST

The Foundations Series is built before ANY other book. Vol 1 → Vol 2 → Vol 3 → Vol 4 → Vol 5 → Vol 6. Each volume depends on everything before it. No skipping.

## The Six Volumes

| Vol | Title | Folder | Physics Covered |
|-----|-------|--------|----------------|
| 1 | Architecture of Reality | `Vol_1_Architecture_of_Reality/` | Axioms, zone manifold, conservation laws, thermodynamics |
| 2 | Forces and Fields | `Vol_2_Forces_and_Fields/` | All 4 fundamental forces from membrane geometry |
| 3 | Matter and Motion | `Vol_3_Matter_and_Motion/` | Classical mechanics, F=ma as theorem, stat mech |
| 4 | The Quantum World | `Vol_4_The_Quantum_World/` | QM, QFT, Standard Model, particle masses |
| 5 | The Cosmos | `Vol_5_The_Cosmos/` | GR, cosmology, fine structure constant |
| 6 | Predictions & Simulations | `Vol_6_Predictions_and_Simulations/` | Testable predictions, computational validation |

## Before Writing Any Volume

1. **Read the volume's QUALITY_GATE.md** — volume-specific requirements and critical deliverables
2. **Read `Quality_Control/BOOK_SERIES_STRATEGY.md`** — chapter outlines for that volume
3. **Read `Development_Process/01_WRITING_PROCESS.md`** — the chapter-level workflow
4. **Read `Quality_Control/01_REQUIREMENTS.md`** — especially WHY-001 through WHY-007 and MATH-001 through MATH-014
5. **Check Research/** — find existing derivations before attempting new ones

## Research Mapping

Each volume maps to specific Research folders. **USE THESE — do not re-derive from scratch.**

### Vol 1: Architecture of Reality
```
Research/Foundations/
├── AXIOM_OPEN_SYSTEM.md              ← Core axiom: universe is open system
├── AXIOM_6D_SPACETIME.md             ← 6D spacetime structure
├── AXIOM_MEMBRANE_MECHANICS.md       ← Firmament as membrane (use v2)
├── AXIOM_METRIC_DISCONTINUITY.md     ← Zone boundaries
├── AXIOM_WATERS_DUALITY.md           ← Dark matter/dark energy
├── AXIOM_SUSTAINING_COUPLING.md      ← Sustaining force
├── AXIOM_PHASE_TRANSITION_FALL.md    ← Four thermodynamic phases
├── ACTION_6D_COMPLETE.md             ← Complete 6D action
├── METRIC_6D_SOLUTIONS.md            ← Metric solutions
└── KK_DIMENSIONAL_REDUCTION.md       ← Kaluza-Klein reduction

Research/Mathematical_Models/
├── 02_Thermodynamics/02-LAWS_DERIVATION.md
└── 10_Fundamental_Constants/10-FUNDAMENTAL_CONSTANTS_OVERVIEW.md
```

### Vol 2: Forces and Fields
```
Research/Mathematical_Models/
├── 03_Electromagnetism/03-MAXWELL_DERIVATION.md  ← Maxwell's equations
├── 03_Electromagnetism/03-APPLICATIONS.md
├── 10_Fundamental_Constants/10-COUPLING_CONSTANTS_DERIVATION.md
├── 10_Fundamental_Constants/10-GRAVITATIONAL_CONSTANT_DERIVATION.md    ← Gravity constant
└── 10_Fundamental_Constants/10-RUNNING_COUPLINGS_RG_FLOW.md
```

### Vol 3: Matter and Motion
```
Research/Mathematical_Models/
├── 01_Classical_Mechanics/01-APPLIED_GRAVITY_CALCULATIONS.md
├── 01_Classical_Mechanics/01-MATERIAL_PROPERTIES.md
├── 02_Thermodynamics/02-LAWS_DERIVATION.md
├── 02_Thermodynamics/02-PHASE_TRANSITIONS_MOLECULAR.md
├── 02_Thermodynamics/02-PLANCK_DISTRIBUTION.md
├── 04_Optics_and_Waves/04-OPTICS_FROM_MAXWELL.md
└── 09_Chemistry_and_Materials/09-CHEMISTRY_DERIVATION.md
```

### Vol 4: The Quantum World
```
Research/Mathematical_Models/
├── 05_Quantum_Mechanics/05-QM_FROM_MEMBRANE_DYNAMICS.md     ← QM foundations
├── 05_Quantum_Mechanics/05-QED_PRECISION_CALCULATIONS.md
├── 05_Quantum_Mechanics/05-CONDENSED_MATTER_DERIVATION.md
├── 06_Nuclear_and_Particle_Physics/06-PARTICLE_MASS_SPECTRUM_V3.md  ← Latest version
├── 06_Nuclear_and_Particle_Physics/06-HIGGS_DERIVATION.md
├── 06_Nuclear_and_Particle_Physics/06-NEUTRINO_PHYSICS.md
├── 06_Nuclear_and_Particle_Physics/06-QCD_DERIVATION.md
├── 06_Nuclear_and_Particle_Physics/06-WEAK_PARITY_CP_VIOLATION.md
├── 06_Nuclear_and_Particle_Physics/06-MATTER_ANTIMATTER_ASYMMETRY.md
└── Research/Foundations/TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md
```

### Vol 5: The Cosmos
```
Research/Mathematical_Models/
├── 07_Relativity/07-GR_OBSERVABLES.md
├── 07_Relativity/07-BH_MERGERS_DYNAMICS.md
├── 07_Relativity/07-FTL_MECHANISMS_FORMAL.md
├── 08_Cosmology/08-CMB_POWER_SPECTRUM.md
├── 08_Cosmology/08-FRIEDMANN_EVOLUTION.md
├── 10_Fundamental_Constants/10-FINE_STRUCTURE_DERIVATION.md  ← Crown jewel
└── 10_Fundamental_Constants/10-PLANCK_CONSTANT_DERIVATION.md
```

### Vol 6: Predictions and Simulations
```
Research/Simulations/
├── membrane_vibrations.py
├── structure_formation.py
├── waters_field_sim.py
├── SIMULATION_RESULTS.md
└── energy_harvesting_simulation.html

Research/Mathematical_Models/
├── OBSERVATIONAL_PHYSICS_TEST_SUITE.md     ← Master test list
├── DERIVATION_CHAIN_AUDIT.md              ← Derivation completeness
└── Test_Results/                          ← Dated test results
```

## Known Research Gaps (as of April 2026)

These are areas where Research/ is incomplete or has known issues. **Flag these when writing touches them:**

> **Author Ratification #1 (2026-06-11):** Λ_Z0 (Godhead-zone cosmological constant) and Postulate F (Hopf winding n_w = 3) are adopted as foundational axioms. Several rows below are now **RESOLVED *given* those adopted axioms, with the dependency stated transparently** (builder's honesty — not "proven from nothing"). See `Research/Foundations/AXIOM_GODHEAD_ZONE_Z0.md` and the GitHub project board (open-problems register; issues #1/#2/#3/#25/#26).

| Gap | Impact | Status | Research Files |
|-----|--------|--------|---------------|
| Spin-1/2 fermions from bosonic membrane | Vol 4 — particle classification | **RESOLVED given adopted Postulate F (n_w=3)** — Kähler spinors + APS index +3; dependency stated; no longer a blocker (GitHub #1) | `Foundations/AXIOM_GODHEAD_ZONE_Z0.md`, `Foundations/TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md` |
| Particle mass spectrum | Vol 4 — mass predictions | **RESOLVED given adopted Λ_Z0 / Postulate F** (GitHub #2) — mechanism resolved; honest residuals remain (electron +17%, heavier quarks fail at tree level; absolute scale a numerical item) | `Mathematical_Models/06_.../06-PARTICLE_MASS_SPECTRUM_V3.md` |
| Weak interaction / CP violation | Vol 4 — weak force | Partial — δ_CP = π/3 from Z₆ topology; precise CKM angles still open (GitHub #3) | `Mathematical_Models/06_.../06-WEAK_PARITY_CP_VIOLATION.md` |
| Fine structure constant precision | Vol 5 — crown jewel derivation | **RESOLVED given adopted Λ_Z0** (UV boundary, α_6D≈1.82); two-loop precision to 137.036 still an honest numerical item | `Mathematical_Models/10_.../10-FINE_STRUCTURE_DERIVATION.md` |
| Higgs mechanism from membrane | Vol 4 — mass generation | **RESOLVED given adopted Λ_Z0 / Postulate F** (GitHub #25) — composite Higgs; m_H ≈ 123 GeV (1.5%); θ_mis derived | `Mathematical_Models/06_.../06-HIGGS_DERIVATION.md` |

## Test Suites

Research has Python test suites for validating derivations. Run after completing any chapter that involves physics derivations:

```bash
cd Research/Mathematical_Models
python -m pytest [domain]/test_*.py -v
```

Domains: `01_Classical_Mechanics`, `02_Thermodynamics`, `03_Electromagnetism`, `04_Optics_and_Waves`, `05_Quantum_Mechanics`, `06_Nuclear_and_Particle_Physics`, `07_Relativity`, `08_Cosmology`, `09_Chemistry_and_Materials`

## Assigned Reviewer Agents

All 10 reviewers are active for the Foundations Series:
1. **The Physicist** — Mathematical rigor (CRITICAL for this series)
2. **But Why? Reader** — "Why" chain complete?
3. **Writing Coach** — Graduate textbook voice, not dry
4. **Consistency Auditor** — Cross-volume notation, equation numbering
5. **The Skeptic** — Would Dr. Marcus Chen (atheist physicist) take this seriously?
6. **The Student** — Can a grad student reproduce derivations?
7. **Style Editor** — Formatting, style consistency, polish
8. **Theologian** — Biblical accuracy and exegetical rigor
9. **Navigator** — Depth calibration, series coherence

(Homeschool Mom is NOT assigned to Foundations.)

## Voice

Feynman writing a textbook. Rigorous, precise, but human. Never dry. The reader should feel the excitement of discovery even while working through heavy math. Every equation gets physical intuition BEFORE the derivation.

## Critical Rules

- **Every derivation starts from previously established results.** Cite equation numbers.
- **Every equation gets a number.** Reference by number, not "the equation above."
- **Problem sets are required.** Computational → Conceptual → Challenge difficulty range.
- **No forward dependencies.** Never use a result from a later volume or chapter.
- **Mark uncertainty.** Open problems and incomplete derivations are labeled explicitly.
- **Use existing Research.** Read the relevant files BEFORE writing. Don't reinvent derivations.

## GitHub Tasks for Foundations Series

**The GitHub project board (Genesis Physics, project #5) is the CANONICAL open-problems and task register.** Do not create or maintain standalone register/status `.md` files for open problems — track open items as board issues and move them across Todo/In Progress/Done.

When `gh` CLI is available, create these issues with label `book:foundations`:

### Series-Level Tasks
1. Create BOOK_SPEC.md for Foundations Series from template
2. Audit Research/ completeness against all 6 volume chapter outlines
3. Build master notation standard (symbols, conventions, equation numbering scheme)
4. Establish LaTeX template and formatting standards

### Per-Volume Tasks (repeat for each volume)
1. Create BOOK_SPEC.md for Vol N from `Development_Process/04_BOOK_SPEC_TEMPLATE.md`
2. Map all chapter requirements to Research/ files — identify gaps
3. Create CHAPTER_SPEC.md for each chapter from template
4. Write detailed outline for each chapter
5. Draft each chapter following writing process
6. Run self-review checklist
7. Run all 6 assigned reviewer agents — iterate until PASS
8. Run relevant test suites — all must pass
9. Update QUALITY_GATE.md with verification results

```bash
# Example: Create Vol 1 issues
gh issue create --repo raymondjl1/genesis_physics \
  --title "Foundations Vol 1: Create BOOK_SPEC.md" \
  --label "book:foundations,vol:1,phase:planning" \
  --body "Create book specification from Development_Process/04_BOOK_SPEC_TEMPLATE.md for Vol 1: Architecture of Reality. Map all chapter requirements to Research/Foundations/ files."

gh issue create --repo raymondjl1/genesis_physics \
  --title "Foundations Vol 1: Research Gap Audit" \
  --label "book:foundations,vol:1,research-gap" \
  --body "Map every chapter's required derivations to existing Research/ files. Document gaps as separate issues."
```
