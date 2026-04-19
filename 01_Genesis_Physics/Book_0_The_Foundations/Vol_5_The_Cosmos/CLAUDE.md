# Volume 5: The Cosmos — Claude Instructions

You are working on Volume 5 of the Foundations Series. This volume derives general relativity, builds a complete cosmology, and derives fundamental constants — including the **fine structure constant**, the crown jewel of the entire framework.

## Prerequisites

**Volumes 1-4 must be complete and verified.**

**Courses equivalent:** General Relativity + Cosmology + Astrophysics (2-3 semesters)
**Target:** 400-500 pages (~120,000-150,000 words)

## Research Files — READ THESE FIRST

```
Research/Mathematical_Models/
├── 07_Relativity/07-GR_OBSERVABLES.md                ← GR predictions and tests
├── 07_Relativity/07-BH_MERGERS_DYNAMICS.md     ← Black hole dynamics
├── 07_Relativity/07-FTL_MECHANISMS_FORMAL.md          ← FTL from zone architecture
├── 07_Relativity/07-FTL_MECHANISMS_SUMMARY.md
├── 08_Cosmology/08-CMB_POWER_SPECTRUM.md              ← CMB predictions
├── 08_Cosmology/08-FRIEDMANN_EVOLUTION.md             ← Cosmological evolution
├── 08_Cosmology/08-ENERGY_EXTRACTION_CREATION.md
├── 08_Cosmology/08-CRITICAL_DENSITY_CALCULATION.md
├── 10_Fundamental_Constants/10-FINE_STRUCTURE_DERIVATION.md ← CROWN JEWEL
├── 10_Fundamental_Constants/10-PLANCK_CONSTANT_DERIVATION.md
├── 10_Fundamental_Constants/10-GRAVITATIONAL_CONSTANT_DERIVATION.md
└── 10_Fundamental_Constants/10-BOLTZMANN_CONSTANT_DERIVATION.md

Research/Papers/
├── black_holes_membrane_punctures.docx    ← BH as membrane punctures
├── cosmological_challenges_yec.docx       ← Cosmological timeline
└── starlight_rapid_expansion.docx         ← Starlight problem
```

## Known Research Gaps

| Gap | Severity | Status |
|-----|----------|--------|
| Fine structure constant derivation precision | HIGH | Partial in `10-FINE_STRUCTURE_DERIVATION.md` |
| CMB power spectrum fit to observations | MEDIUM | `CMB_POWER_SPECTRUM.md` — check quantitative agreement |
| N-body dynamics completeness | MEDIUM | GitHub #20 |
| GR observables quantitative precision | MEDIUM | GitHub #8 — 9 tests, check pass rate |

## Critical Deliverables

1. **General relativity derived** from 6D embedding — Einstein field equations as consequence
2. **Black holes explained** as zone infrastructure (membrane punctures)
3. **Complete cosmology** — expansion, structure formation, CMB
4. **Fine structure constant derived** from first principles — THE make-or-break calculation
5. **Fundamental constants (ℏ, G, k_B) derived** — not measured, derived
6. **Cosmological timeline** — honest treatment of age/timeline questions

## Test Suites

```bash
cd Research/Mathematical_Models
python -m pytest 07_Relativity/test_gr_observables.py -v
python -m pytest 08_Cosmology/test_cosmology.py -v
python -m pytest 08_Cosmology/test_structure_formation.py -v
```

## GitHub Tasks

```bash
gh issue create --title "Vol 5: Create BOOK_SPEC.md" --label "book:foundations,vol:5,phase:planning"
gh issue create --title "Vol 5: Research gap audit — fine structure constant, GR precision" --label "book:foundations,vol:5,research-gap"
for ch in $(seq -w 1 15); do
  gh issue create --title "Vol 5 Ch ${ch}: Spec → Outline → Draft → Verify" --label "book:foundations,vol:5,phase:writing"
done
gh issue create --title "Vol 5: Integration + validation" --label "book:foundations,vol:5,phase:integration"
```
