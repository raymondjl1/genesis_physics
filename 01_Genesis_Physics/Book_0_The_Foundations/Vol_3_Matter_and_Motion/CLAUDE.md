# Volume 3: Matter and Motion — Claude Instructions

You are working on Volume 3 of the Foundations Series. The headline: **F=ma becomes a theorem, not an axiom.** Classical mechanics and thermodynamics are derived from zone architecture. The student understands WHY things move the way they do.

## Prerequisites

**Volumes 1-2 must be complete and verified.** Zone manifold, all forces, and field equations from Vols 1-2 are assumed.

**Courses equivalent:** Classical Mechanics + Thermodynamics/Statistical Mechanics (2 semesters)
**Target:** 350-450 pages (~100,000-130,000 words)

## Research Files — READ THESE FIRST

```
Research/Mathematical_Models/
├── 01_Classical_Mechanics/01-APPLIED_GRAVITY_CALCULATIONS.md ← Gravity applications
├── 01_Classical_Mechanics/01-MATERIAL_PROPERTIES.md          ← Material properties
├── 02_Thermodynamics/02-LAWS_DERIVATION.md     ← Thermo from zone arch
├── 02_Thermodynamics/02-PHASE_TRANSITIONS_MOLECULAR.md       ← Phase transitions
├── 02_Thermodynamics/02-PLANCK_DISTRIBUTION.md               ← Planck spectrum
├── 02_Thermodynamics/02-WATERS_REPLENISHMENT.md ← Waters field thermo
├── 04_Optics_and_Waves/04-OPTICS_FROM_MAXWELL.md             ← Optics derived
├── 09_Chemistry_and_Materials/09-CHEMISTRY_DERIVATION.md  ← Chemistry connections
└── 09_Chemistry_and_Materials/09-ELEMENT_PREDICTION.md
```

## Known Research Gaps

| Gap | Chapters Affected | Status |
|-----|------------------|--------|
| Material properties completeness | Elasticity, specific heat chapters | `01-MATERIAL_PROPERTIES.md` — check coverage |
| Phase transitions molecular detail | Phase transition chapters | GitHub #12 |
| Optics wave equation from zone arch | Optics chapters | Partial in `04-OPTICS_FROM_MAXWELL.md` |

## Critical Deliverables

1. **F=ma derived** from zone architecture — NOT postulated
2. **Newton's laws as theorems** — consequences of deeper principles
3. **Thermodynamic laws** derived from open system axiom
4. **Statistical mechanics** from zone architecture ensemble theory
5. **Optics and wave mechanics** from Maxwell (Vol 2) applied
6. **Classical limits** shown where quantum (Vol 4) reduces to classical

## Assigned Reviewers

Same 6 as Vols 1-2. The Student is especially important here — classical mechanics is the student's first real test of "can I use this framework to solve problems?"

## Test Suites

```bash
cd Research/Mathematical_Models
python -m pytest 01_Classical_Mechanics/test_gravity_kinematics.py -v
python -m pytest 01_Classical_Mechanics/test_material_properties.py -v
python -m pytest 02_Thermodynamics/test_thermodynamic_laws.py -v
python -m pytest 02_Thermodynamics/test_phase_transitions.py -v
python -m pytest 02_Thermodynamics/test_planck_spectrum.py -v
python -m pytest 04_Optics_and_Waves/test_optics.py -v
```

## GitHub Tasks

```bash
gh issue create --title "Vol 3: Create BOOK_SPEC.md" --label "book:foundations,vol:3,phase:planning"
gh issue create --title "Vol 3: Research gap audit" --label "book:foundations,vol:3,research-gap"
for ch in $(seq -w 1 14); do
  gh issue create --title "Vol 3 Ch ${ch}: Spec → Outline → Draft → Verify" --label "book:foundations,vol:3,phase:writing"
done
gh issue create --title "Vol 3: Integration + validation" --label "book:foundations,vol:3,phase:integration"
```
