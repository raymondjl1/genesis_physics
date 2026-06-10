# Volume 4: The Quantum World — Claude Instructions

You are working on Volume 4 of the Foundations Series. This is the **make-or-break volume** for the framework's credibility. If zone architecture can derive the Standard Model and predict particle masses, the physics community will take notice. If it can't, they won't.

## Prerequisites

**Volumes 1-3 must be complete and verified.** All classical mechanics, forces, and thermodynamics assumed.

**Courses equivalent:** Quantum Mechanics + QFT + Particle Physics (3 semesters)
**Target:** 500-600 pages (~150,000-180,000 words) — the largest volume

## Research Files — READ THESE FIRST

```
Research/Mathematical_Models/
├── 05_Quantum_Mechanics/05-QM_FROM_MEMBRANE_DYNAMICS.md     ← QM foundations (CRITICAL)
├── 05_Quantum_Mechanics/05-QED_PRECISION_CALCULATIONS.md     ← g-2, Lamb shift
├── 05_Quantum_Mechanics/05-APPLIED_CALCULATIONS.md        ← Applied QM
├── 05_Quantum_Mechanics/05-CONDENSED_MATTER_DERIVATION.md    ← Condensed matter
├── 06_Nuclear_and_Particle_Physics/06-PARTICLE_MASS_SPECTRUM_V3.md ← USE v3 (latest)
├── 06_Nuclear_and_Particle_Physics/00_Archive/06-MASS_SPECTRUM_V2_*.md  ← Supporting analysis (5 files; ARCHIVED — superseded by V3 per CANONICAL_FACTS_REGISTRY §H)
├── 06_Nuclear_and_Particle_Physics/06-HIGGS_DERIVATION.md ← Higgs
├── 06_Nuclear_and_Particle_Physics/06-NEUTRINO_PHYSICS.md
├── 06_Nuclear_and_Particle_Physics/06-QCD_DERIVATION.md
├── 06_Nuclear_and_Particle_Physics/06-WEAK_PARITY_CP_VIOLATION.md
├── 06_Nuclear_and_Particle_Physics/06-MATTER_ANTIMATTER_ASYMMETRY.md
├── 06_Nuclear_and_Particle_Physics/06-REMAINING_DERIVATIONS.md
└── 06_Nuclear_and_Particle_Physics/06-SYMMETRIES_MASS_INTEGRATION.md

Research/Foundations/
└── TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md  ← Particles as topological defects
```

## KNOWN RESEARCH GAPS — CRITICAL

These are the biggest open problems in the entire project. **Several are GitHub blockers.**

| Gap | Severity | GitHub Issue | Status |
|-----|----------|-------------|--------|
| **Spin-1/2 fermions from bosonic membrane** | BLOCKER | #1 | The membrane is bosonic — deriving fermionic excitations is THE decisive challenge |
| **Particle mass spectrum 1000× errors** | HIGH | #2 | Current predictions off by ~1000× for some particles. See `06-PARTICLE_MASS_SPECTRUM_V3.md` |
| **Weak interaction / CP violation** | HIGH | #3 | Derivation incomplete |
| **Higgs mechanism from membrane** | HIGH | #25 | Partial — condensation model needs completion |
| **Running coupling constants** | MEDIUM | #26 | RG flow analysis partial |

**WARNING:** Do not write chapters covering these topics as if the derivations are complete. If a derivation has known issues, the chapter must say so explicitly. "Open problem" is better than hand-waving. The Skeptic reviewer (Dr. Marcus Chen) will catch it.

## Critical Deliverables

1. **QM derived from membrane dynamics** — uncertainty, superposition, measurement problem EXPLAINED
2. **QFT developed** from zone architecture
3. **Entire Standard Model derived** — all particles, all interactions
4. **Particle masses calculated** from membrane resonance modes (with honest error reporting)
5. **QED precision calculations** — g-2, Lamb shift
6. **Nuclear physics and QCD** from zone topology

## Assigned Reviewers

All 6 (no Homeschool Mom). The Physicist is CRITICAL for this volume — every QM/QFT derivation will be scrutinized.

## Test Suites

```bash
cd Research/Mathematical_Models
python -m pytest 05_Quantum_Mechanics/test_qm_applied.py -v
python -m pytest 05_Quantum_Mechanics/test_condensed_matter.py -v
python -m pytest 06_Nuclear_and_Particle_Physics/test_nuclear_physics.py -v
python -m pytest 09_Chemistry_and_Materials/test_atomic_structure.py -v
```

## GitHub Tasks

```bash
gh issue create --title "Vol 4: Create BOOK_SPEC.md" --label "book:foundations,vol:4,phase:planning"
gh issue create --title "Vol 4: CRITICAL research gap audit — spin-1/2, mass spectrum, Higgs" --label "book:foundations,vol:4,research-gap,blocker"
gh issue create --title "Vol 4: Map QM/QFT chapters to Research/ — identify all gaps" --label "book:foundations,vol:4,research-gap"
for ch in $(seq -w 1 18); do
  gh issue create --title "Vol 4 Ch ${ch}: Spec → Outline → Draft → Verify" --label "book:foundations,vol:4,phase:writing"
done
gh issue create --title "Vol 4: Integration + validation — particle physics stress test" --label "book:foundations,vol:4,phase:integration"
```
