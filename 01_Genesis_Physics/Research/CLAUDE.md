# Research Folder — Claude Instructions

This folder contains the **physics research backbone** of the entire Genesis Physics Series. Every derivation, test suite, and validation here feeds into all four books. **Nothing is written in any book that isn't derived or proven here first.**

## Core Philosophy

Research is the engine room. If it's not proven here, it doesn't go in a book. Period.

## Folder Structure

```
Research/
├── Foundations/              ← Axioms and foundational derivations (7+ axiom files)
│   ├── AXIOM_*.md           ← One file per axiom (6D spacetime, membrane, open system, etc.)
│   ├── *_DERIVATION.md      ← Key foundational derivations
│   └── VALIDATION_REPORT_*.md ← Validation status
│
├── Mathematical_Models/      ← 10 physics domains with derivations + test suites
│   ├── 01_Classical_Mechanics/
│   ├── 02_Thermodynamics/
│   ├── 03_Electromagnetism/
│   ├── 04_Optics_and_Waves/
│   ├── 05_Quantum_Mechanics/
│   ├── 06_Nuclear_and_Particle_Physics/
│   ├── 07_Relativity/
│   ├── 08_Cosmology/
│   ├── 09_Chemistry_and_Materials/
│   ├── 10_Fundamental_Constants/
│   ├── Archive/              ← Older versions and superseded models
│   └── Test_Results/         ← Validation reports and test run outputs
│
├── Papers/                   ← Research papers (docx format)
│   ├── hebrew_word_analysis.docx
│   ├── cosmological_challenges_yec.docx
│   ├── flood_subterranean_reservoir_model.docx
│   └── [other specialized papers]
│
├── Peer_Review/              ← Skeptic and critic analysis
│
└── Simulations/              ← Python scripts for computational validation
    └── *.py
```

## How to Use This Folder

### When Writing a Book Chapter
1. **Check here FIRST** — find the derivation that supports the chapter's claims
2. **Reference by filename** — cite the specific Research file in the chapter spec
3. **If the derivation doesn't exist** — STOP. Create a Research Gap issue. Don't make it up.

### When Adding New Research
1. Place it in the correct domain folder under `Mathematical_Models/`
2. Follow the naming convention: `DOMAIN_TOPIC.md` (e.g., `GRAVITY_COMPLETIONS.md`)
3. Include: starting assumptions, every derivation step, final result with error analysis
4. Write or update a test suite (`test_*.py`) to validate numerically
5. Run the test suite and document results in `Test_Results/`

### When Validating Existing Research
1. Run the Python test suites: `python -m pytest [domain]/test_*.py -v`
2. Check results against `Test_Results/` — compare with prior runs
3. Flag any regressions or new failures

## Research Domain → Book Mapping

| Domain | Book 0 Volume(s) | Book 1 Chapters | Book 2 Chapters |
|--------|------------------|-----------------|-----------------|
| Foundations/Axioms | Vol 1 (all) | Ch 1–5 | Ch 1–4 |
| Classical Mechanics | Vol 3 | Ch 6–8 | Ch 7 |
| Thermodynamics | Vol 3 | Ch 8 | Ch 8 |
| Electromagnetism | Vol 2 | Ch 9–10 | Ch 9 |
| Optics & Waves | Vol 3 | Ch 10 | Ch 3 |
| Quantum Mechanics | Vol 4 | Ch 15–16 | Ch 13 |
| Nuclear & Particle | Vol 4 | Ch 14–15 | Ch 7, 13 |
| Relativity | Vol 5 | Ch 16, 18 | Ch 12 |
| Cosmology | Vol 5 | Ch 19–21 | Ch 6, 10, 12 |
| Chemistry & Materials | Vol 3 | Ch 22 | — |
| Fundamental Constants | Vol 5, Vol 6 | Ch 23–24 | Ch 9 |

## Known Research Gaps (Critical)

These are tracked in GitHub issues but summarized here for quick reference. **Author Ratification #1 (2026-06-11):** Λ_Z0 and Postulate F (n_w = 3) are adopted as foundational axioms; items 1, 2, and 4 below are now **RESOLVED *given* those adopted axioms, dependency stated transparently** (builder's honesty — not "proven from nothing"). The canonical open-problems & task register is the **GitHub project board (issues #1/#2/#3/#25/#26)**; the axiom itself is `Research/Foundations/AXIOM_GODHEAD_ZONE_Z0.md`. (The legacy file `Research/00_Archive/OPEN_PROBLEMS_REGISTER.md` is a frozen, deprecated snapshot — do not maintain it.)

1. **Spin-1/2 fermions** — **RESOLVED given adopted Postulate F (n_w=3)**: Kähler spinors + APS index +3 → three generations. **No longer a blocker.** Dependency stated.
2. **Particle mass spectrum** — **RESOLVED given adopted Λ_Z0 / Postulate F**: mechanism resolved; honest residuals remain (electron +17%, heavier quarks fail at tree level; absolute scale a numerical item).
3. **Weak interaction / CP violation** — partial (δ_CP = π/3 from Z₆ topology; precise CKM angles still open).
4. **Higgs mechanism** — **RESOLVED given adopted Λ_Z0 / Postulate F**: composite Higgs, m_H ≈ 123 GeV (1.5%), θ_mis derived.
5. **Fine structure constant precision** — UV boundary resolved given Λ_Z0 (α_6D ≈ 1.82); two-loop precision to 137.036 still an honest open numerical item.

## What NOT to Do

- **Never fabricate derivations.** If it's not here, it's not proven.
- **Never modify archived files.** `Archive/` and `00_Archive/` are read-only history.
- **Never skip test suites.** Every derivation should have numerical validation.
- **Never claim a derivation is complete if the test suite fails.** Honesty is the foundation.
