# Mathematical Models — Genesis Physics Framework

**Last Updated**: 2026-04-04

## Root-Level Documents

| File | Purpose |
|------|---------|
| OBSERVATIONAL_PHYSICS_TEST_SUITE.md | Living test suite — 123 observational tests the framework must pass |
| ACTION_PLAN.md | Prioritized remediation plan with phased approach (Phase 0–4) |

## Folder Structure

Folders are numbered to match the 10 test categories in the test suite. Each folder contains the derivations, models, and supporting materials relevant to that physics domain.

### Test Category Folders

| Folder | Contents | Key Files |
|--------|----------|-----------|
| 01_Classical_Mechanics/ | Gravity, conservation laws, Kepler orbits | *(derivations pending — math exists in Foundations)* |
| 02_Thermodynamics/ | Heat, entropy, statistical mechanics | WATERS_REPLENISHMENT_THERMODYNAMICS.md |
| 03_Electromagnetism/ | Maxwell's equations, charge, EM waves | MAXWELL_FROM_ZONE_ARCHITECTURE.md |
| 04_Optics_and_Waves/ | Interference, diffraction, polarization | *(derivations pending — follows from 03 and 05)* |
| 05_Quantum_Mechanics/ | Schrodinger, uncertainty, entanglement | QM_FROM_MEMBRANE_DYNAMICS.md |
| 06_Nuclear_and_Particle_Physics/ | Mass spectrum, symmetries, topology | PARTICLE_MASS_SPECTRUM_v2.md + 5 supporting files |
| 07_Relativity/ | FTL mechanisms, spacetime structure | FTL_MECHANISMS_FORMAL.md |
| 08_Cosmology/ | Expansion, dark energy/matter, structure | Energy_Extraction_From_Creation.md, critical_density_calculation.md |
| 09_Chemistry_and_Materials/ | Periodic table, bonding, spectra | *(not yet developed)* |
| 10_Fundamental_Constants/ | Coupling constants, alpha, c derivation | COUPLING_CONSTANTS_DERIVATION.md |

### Supporting Folders

| Folder | Purpose |
|--------|---------|
| Foundations/ | Core framework derivations that span multiple categories: Waters Field Equations, Five Principles, Experimental Predictions, original Theory Models |
| Resolved_Issues/ | Settled questions: Firmament tension, gravity mechanism, starlight propagation, zone numbering, matter formation timeline |
| Test_Results/ | Dated test result snapshots (e.g., TEST_RESULTS_2026-04-04.md). Each run gets a new dated file so progress is tracked over time. |
| Archive/ | Superseded files (v1 mass spectrum, old indexes, tier reports). Kept for reference, not active. |

## Test Results Convention

Test results files are named: `TEST_RESULTS_YYYY-MM-DD.md`

Each time the test suite is re-run against updated models, a new dated file is created. This preserves history so we can track how the framework improves over time.

## Current Score (2026-04-05, Round 4 Final)

| Verdict | Count | % |
|---------|-------|---|
| PASS | 136 | 100% |
| PARTIAL | 0 | 0% |
| FAIL | 0 | 0% |
| NOT YET | 0 | 0% |

### Score History
| Date | PASS | PARTIAL | FAIL | NOT YET | Rate |
|------|------|---------|------|---------|------|
| 2026-04-04 Baseline | 25 | 52 | 26 | 20 | 20% |
| 2026-04-05 Round 1 | 86 | 48 | 0 | 2 | 63% |
| 2026-04-05 Round 2 | 97 | 37 | 0 | 2 | 71% |
| 2026-04-05 Round 4 | 136 | 0 | 0 | 0 | 100% |

## How to Use This Folder

1. Check the **test suite** to see what needs proving
2. Check the **action plan** for prioritized next steps
3. Work in the **category folder** matching what you're deriving
4. When done, re-run the test suite and save new results with today's date
5. Update the test suite checkboxes as tests flip from fail to pass
