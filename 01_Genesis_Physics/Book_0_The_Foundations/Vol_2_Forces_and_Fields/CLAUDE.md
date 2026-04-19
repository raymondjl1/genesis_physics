# Volume 2: Forces and Fields — Claude Instructions

You are working on Volume 2 of the Foundations Series. This volume answers the question every physics student asks and never gets answered: **Why are there four forces, why do they have the strengths they do, and why do they work the way they work?**

## Prerequisites

**Volume 1 must be complete and verified.** All axioms, zone manifold, conservation laws, and notation from Vol 1 are assumed. Cite Vol 1 equation numbers directly.

**Courses equivalent:** Electrodynamics + Classical Field Theory (2 semesters)
**Target:** 400-500 pages (~120,000-150,000 words)

## Research Files — READ THESE FIRST

```
Research/Mathematical_Models/
├── 03_Electromagnetism/03-MAXWELL_DERIVATION.md  ← CRITICAL: Maxwell derived
├── 03_Electromagnetism/03-APPLICATIONS.md                 ← Applied EM calculations
├── 10_Fundamental_Constants/10-COUPLING_CONSTANTS_DERIVATION.md ← Force strengths
├── 10_Fundamental_Constants/10-GRAVITATIONAL_CONSTANT_DERIVATION.md    ← Gravitational constant
├── 10_Fundamental_Constants/10-RUNNING_COUPLINGS_RG_FLOW.md ← RG flow

Research/Foundations/
├── AXIOM_MEMBRANE_MECHANICS_v2.md    ← Membrane geometry → forces
├── ACTION_6D_COMPLETE.md             ← Action principle → field equations
└── KK_DIMENSIONAL_REDUCTION.md       ← Dimensional reduction → gauge fields
```

## Known Research Gaps

| Gap | Chapters Affected | Status |
|-----|------------------|--------|
| Running coupling constants precision | Force unification chapters | GitHub #26 — partial |
| Gravity derivation from 6D action completeness | Gravity chapters | `10-GRAVITATIONAL_CONSTANT_DERIVATION.md` — check status |

## Critical Deliverables

1. **Maxwell's equations derived** from membrane geometry — not postulated
2. **Gravity derived** from 6D metric — not assumed as given
3. **Strong force derived** from zone topology
4. **Weak force derived** from membrane-boundary interactions
5. **Hierarchy problem solved** — why forces have different strengths
6. **Fine structure constant derivation begun** (completed in Vol 5)

## Assigned Reviewers

Same 6 as Vol 1 (all except Homeschool Mom). The Physicist is especially critical here — every force derivation must be airtight.

## Test Suites

```bash
cd Research/Mathematical_Models
python -m pytest 03_Electromagnetism/test_em_applications.py -v
python -m pytest 01_Classical_Mechanics/test_gravity_kinematics.py -v
```

## GitHub Tasks

```bash
gh issue create --title "Vol 2: Create BOOK_SPEC.md" --label "book:foundations,vol:2,phase:planning"
gh issue create --title "Vol 2: Research gap audit — are all 4 forces derivable?" --label "book:foundations,vol:2,research-gap"
for ch in $(seq -w 1 15); do
  gh issue create --title "Vol 2 Ch ${ch}: Spec → Outline → Draft → Verify" --label "book:foundations,vol:2,phase:writing"
done
gh issue create --title "Vol 2: Integration + validation" --label "book:foundations,vol:2,phase:integration"
```
