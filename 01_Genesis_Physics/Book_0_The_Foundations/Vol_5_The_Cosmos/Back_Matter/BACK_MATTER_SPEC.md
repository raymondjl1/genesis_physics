# Vol 5 Back Matter — Specification & Outline

**Product:** Foundations Vol 5, The Cosmos
**Scope:** Appendices A, B, C; Problem Sets (Ch 1–15); Bibliography
**Lifecycle phase:** Phase 1 (Spec) + Phase 2 (Outline) — this document
**Voice:** Feynman writing a textbook (match Vols 1–4 back matter register)
**Citation convention:** `(V.Ch.Eq)` with `V ∈ {1,2,3,4,5}`

---

## Mission

Give the Vol 5 reader — a graduate student or working physicist — a single, compact, self-contained reference for everything the volume uses or produces, with honest accounting of what the zone-architecture framework gets right, what it gets wrong, and by how much.

This is the culminating back matter of the series so far (target: ~30,000 words). It must:

1. Let any reader navigate from a Vol 5 derivation back to the Vol 1–4 equation it inherits (Appendix A + reverse index).
2. Show every cosmological parameter and fundamental constant with the zone-architecture prediction next to the experimental value and fractional error — the honest scorecard of Volume 5 (Appendix B).
3. Compile all four fundamental-constant derivations (α, ℏ, G, k_B) in a single summary table with derivation chains (Appendix C).
4. Give worked problem sets for every chapter with selected solutions (Ch 1–15).
5. Provide a 150+ entry bibliography covering GR, cosmology, precision measurements, and zone-architecture internal sources.

---

## Requirements Traced to QUALITY_GATE.md and WRITING_PROMPT.md (Vol 5)

| Req | Source | Covered by |
|-----|--------|-----------|
| Fine structure constant α⁻¹ = 137.17 ± 0.15 (0.1%) honest reporting | WRITING_PROMPT.md §Gaps, Ch 13 | App B §B.3, App C §C.1 |
| CMB power spectrum fit precision stated | WRITING_PROMPT.md §Gaps | App B §B.5 |
| GR observables pass rate (11 tests) | WRITING_PROMPT.md §Gaps | App B §B.1 |
| Cosmological parameters: all six ΛCDM concordance values | Ch 14 | App B §B.4 |
| Dark matter/dark energy 68/27/5 split derived | Ch 11, Vol 1 Ch 6 | App B §B.4 |
| All derived constants (ℏ, G, k_B) from Ch 15 | Ch 15 | App C §C.2–C.4 |
| Problem sets reference only Vols 1–5 | WRITING_PROMPT.md Continuity Checklist | Problem sets |
| 150+ bibliography entries | User instruction | Bibliography |
| No forward references to Vol 6 | User instruction | All components |
| Consistency with Vol 4 App A format | Vol 4 back matter | App A |

---

## Prerequisites (What the Reader Already Has)

- Full working knowledge of Vols 1–4 (axioms, forces, classical mechanics, QM/QFT, Standard Model)
- Vol 5 Chapters 1–15 read in sequence (problem sets never forward-reference)
- Vol 1 Appendix B (Notation Reference) — we reuse its symbol tables, do not redefine

---

## "Why" Chain the Back Matter Answers

- **Why Appendix A?** Vol 5 cites hundreds of Vol 1–4 equations; the reader must be able to find the antecedent without scrolling across five books.
- **Why Appendix B with comparison tables?** This is the *honest scorecard* — every cosmological observable, every derived constant, experimental value vs. framework prediction with fractional error. No cherry-picking.
- **Why Appendix C?** The crown jewel of the entire Foundations series is that fundamental constants are *derived*, not measured. Scattering these derivations across Ch 13 and Ch 15 buries the achievement. One compiled reference table lets any reader see the full program at a glance.
- **Why 15 problem sets?** Foundations rule: every chapter gets computational / conceptual / challenge problems. GR and cosmology problems are notoriously hard to set at the right level; these must be genuinely solvable from the text.
- **Why 150+ references?** GR, cosmology, and precision measurements each have vast literatures. The Planck collaboration alone has dozens of key papers.

---

## Figure & Table Plan

This is a back-matter deliverable; figures are sparse but tables are dense.

| ID | Placement | Type | What it shows |
|----|-----------|------|---------------|
| Tbl 5.A.1 | App A §A.2 | Table | Vol 1 results used in Vol 5, by chapter |
| Tbl 5.A.2 | App A §A.3 | Table | Vol 2 results used in Vol 5, by chapter |
| Tbl 5.A.3 | App A §A.4 | Table | Vol 3 results used in Vol 5, by chapter |
| Tbl 5.A.4 | App A §A.5 | Table | Vol 4 results used in Vol 5, by chapter |
| Tbl 5.A.5 | App A §A.6 | Table | Reverse index: Vol 5 chapter → prior-volume equations cited |
| Tbl 5.B.1 | App B §B.1 | Table | GR observables: 11-test suite with predicted vs. measured |
| Tbl 5.B.2 | App B §B.2 | Table | Black hole parameters (Schwarzschild, Kerr, thermodynamics) |
| Tbl 5.B.3 | App B §B.3 | Table | **Fundamental constants: α, ℏ, G, k_B — predicted vs. measured, fractional error** |
| Tbl 5.B.4 | App B §B.4 | Table | **Cosmological parameters: all six ΛCDM concordance values** |
| Tbl 5.B.5 | App B §B.5 | Table | CMB observables (peak positions, damping scale, optical depth) |
| Tbl 5.B.6 | App B §B.6 | Table | Dark sector parameters (Ω_A, Ω_B, Ω_b, w_A, w_B) |
| Tbl 5.B.7 | App B §B.7 | Table | Planck unit values (ℓ_P, t_P, m_P, T_P, E_P) |
| Tbl 5.B.8 | App B §B.8 | Table | Zone-architecture scale parameters (σ, μ, ξ_A, η_B, V_extra) |
| Tbl 5.B.9 | App B §B.9 | Table | **Headline honesty table: every Vol 5 observable, error class, status** |
| Tbl 5.C.1 | App C §C.1 | Table | Fine structure constant derivation chain |
| Tbl 5.C.2 | App C §C.2 | Table | Planck constant derivation chain |
| Tbl 5.C.3 | App C §C.3 | Table | Gravitational constant derivation chain |
| Tbl 5.C.4 | App C §C.4 | Table | Boltzmann constant derivation chain |
| Tbl 5.C.5 | App C §C.5 | Table | **Master constants summary: all four constants in one table** |

No pictorial figures in the back matter; every visual is a table.

---

## Appendix A: Key Results from Volumes 1–4

**Structure (mirrors Vol 4 App A, extended to four prior volumes):**

- §A.1 How to use this appendix — tag notation, orphan-check principle
- §A.2 Volume 1 results used in Vol 5 — grouped by Vol 1 chapter (Ch 4 6D embedding, Ch 5 Firmament, Ch 6 Waters, Ch 7 Conservation, Ch 10 Quantization, Ch 11 Thermodynamics)
- §A.3 Volume 2 results used in Vol 5 — Ch 2 Gravity, Ch 3 EM → fine structure, Ch 5 Lagrangian, Ch 8 Gravitational field, Ch 10 Running couplings
- §A.4 Volume 3 results used in Vol 5 — Ch 5 Fluid dynamics → cosmological fluids, Ch 8 Phase transitions, Ch 12 Entropy
- §A.5 Volume 4 results used in Vol 5 — Part II QFT → Hawking radiation, Ch 10 Particles → nucleosynthesis, Ch 8 Renormalization → constants precision
- §A.6 Reverse index — Vol 5 chapter → list of prior equations cited
- §A.7 Orphan check — every listed equation appears in the reverse index

Each equation row: equation number (boxed), full formula, one-line gloss, list of Vol 5 chapters that cite it.

---

## Appendix B: Cosmological Data Tables

**Structure:**

- §B.0 How to read these tables (status classes: DERIVED / CALIBRATED / INHERITED / OPEN)
- §B.1 General relativity observables — 11-test suite (Mercury precession, light bending, Shapiro delay, gravitational redshift, LIGO waveforms, Cassini, Hulse-Taylor, frame dragging, geodetic precession, gravitational wave speed, strong-lensing time delays)
- §B.2 Black hole parameters — Schwarzschild radius, ISCO, Kerr ergosphere, Hawking temperature, Bekenstein-Hawking entropy, Penrose process efficiency
- §B.3 **Fundamental constants — α⁻¹, ℏ, G₄, k_B: experimental value, zone prediction, fractional error, derivation chapter**
- §B.4 **Cosmological concordance parameters — H₀, Ω_bh², Ω_mh², τ, n_s, A_s: zone value vs. Planck 2018**
- §B.5 CMB observables — first three acoustic peak positions (ℓ₁, ℓ₂, ℓ₃), damping scale, photon decoupling redshift z_dec, sound horizon r_s
- §B.6 Dark sector — Ω_A (dark energy), Ω_B (dark matter), Ω_b (baryons), equation-of-state parameters w_A, w_B, dark matter self-interaction bound
- §B.7 Planck units — ℓ_P, t_P, m_P, T_P, E_P computed from derived constants
- §B.8 Zone-architecture scale parameters — σ, μ, ξ_A, η_B, V_extra, ξ_A/η_B ratio
- §B.9 **Headline honesty table — every parameter this volume claims to derive or match, its status (DERIVED/CALIBRATED/INHERITED/OPEN), fractional error, and honest assessment**

**Critical requirement:** §B.3 must present every constant with the same formatting: (1) experimental value with CODATA/PDG uncertainty, (2) zone-architecture prediction with stated uncertainty, (3) fractional error = |pred − exp|/exp. The fine structure constant at 0.1% is the headline; ℏ and G are near-exact because the membrane parameters (σ, μ, η_B) were *calibrated* to reproduce them — this must be stated explicitly. k_B is derived from mode-counting but its precision depends on the UV cutoff choice. No hiding behind precision that was put in by hand.

---

## Appendix C: Derivations of Fundamental Constants Summary Table

**Structure:**

- §C.0 Purpose — why compile these derivations separately
- §C.1 Fine structure constant α — from 6D gauge action → KK reduction → RG running → α⁻¹ = 137.17 ± 0.15. Full derivation chain: Vol 2 Ch 3 (gauge coupling started) → Vol 4 Ch 8 (renormalization) → Vol 5 Ch 13 (completed). Inputs: ξ_A, η_B, SM β-function coefficient.
- §C.2 Planck's constant ℏ — from membrane vortex action → Bohr-Sommerfeld quantization → ℏ = ση_B³/(2c). Full chain: Vol 1 Ch 5 (membrane) → Vol 1 Ch 10 (quantization) → Vol 5 Ch 15. Inputs: σ, η_B, c.
- §C.3 Gravitational constant G — from 6D → 4D dimensional reduction → G₄ = G₆/V_extra. Full chain: Vol 1 Ch 4 (6D embedding) → Vol 2 Ch 2 (gravity) → Vol 5 Ch 1 (EFE) → Vol 5 Ch 15. Inputs: G₆, V_extra.
- §C.4 Boltzmann constant k_B — from membrane mode counting → entropy → k_B = S/ln Ω. Full chain: Vol 1 Ch 11 (thermodynamics) → Vol 5 Ch 5 (BH entropy) → Vol 5 Ch 15. Inputs: mode spectrum, UV cutoff.
- §C.5 **Master summary table — all four constants, derivation status, precision achieved, what is genuine prediction vs. calibration**

**Critical requirement:** §C.5 must distinguish sharply between:
- **GENUINE PREDICTIONS** (α — the framework predicts α⁻¹ = 137.17 from ξ_A/η_B ratio; no fitting)
- **CALIBRATION-DEPENDENT** (ℏ, G — membrane parameters σ, μ, η_B are *chosen* to reproduce these; the framework explains *why* they take these values but does not predict them from fewer inputs)
- **DERIVED FROM PRIOR** (k_B — follows from ℏ and the mode spectrum; precision limited by UV cutoff)

---

## Problem Sets — Structure

One section per chapter (15 sections). Each chapter:

- 3–5 problems
- Difficulty tiers: ★ basic / ★★ intermediate / ★★★ challenge
- Mix: ≥1 computational, ≥1 conceptual, ≥1 that forces the reader to retrace a derivation or check a limit
- Selected solutions: one problem per chapter fully worked, typically the ★★ or ★★★ problem
- Number format: `P5.Ch.N` (e.g., P5.7.3 = Vol 5, Ch 7, problem 3)

Estimated: ~60 problems total. Forward-references forbidden — Ch N problems may only use Ch 1..N material plus Vols 1–4. No references to Vol 6.

---

## Bibliography — Plan

Target: **≥150 entries**, organized in sections:

- R.1 General relativity: foundational and historical papers (Einstein 1915/1916, Hilbert, Schwarzschild, Kerr, Penrose, Hawking, etc.) — ~20 entries
- R.2 GR textbooks (MTW, Wald, Carroll, Hartle, Schutz, Poisson-Will, etc.) — ~15 entries
- R.3 Gravitational wave observations (LIGO/Virgo collaboration papers, GW150914, GW170817, O3/O4 catalog) — ~15 entries
- R.4 Black hole physics (Bekenstein, Hawking 1974/1975, Penrose 1965, Page curve, Mathur, Almheiri-Marolf-Polchinski-Sully) — ~15 entries
- R.5 Cosmology textbooks and reviews (Weinberg Cosmology, Dodelson-Schmidt, Mukhanov, Kolb-Turner, Peebles, Ryden) — ~15 entries
- R.6 CMB and Planck collaboration (Planck 2018 I–XIII, WMAP, COBE-FIRAS, ACT, SPT) — ~15 entries
- R.7 Large-scale structure (Eisenstein et al. BAO, SDSS, DESI, Press-Schechter, Zel'dovich) — ~10 entries
- R.8 Precision measurements of fundamental constants (CODATA 2022, α measurements by Gabrielse/Parker/Morel, Planck constant NIST, G measurements) — ~15 entries
- R.9 Dark matter and dark energy observations (Rubin-Ford 1970, Zwicky 1933, Perlmutter/Riess 1998/1999, DES, Pantheon+, Bullet Cluster) — ~15 entries
- R.10 Zone-architecture internal sources (Vols 1–4, research files, simulations) — ~15 entries

Total target: ~150 entries. Citation format: Chicago author-year with sequential numbering within each section, symbol marking class (📜 foundational, 📘 textbook, ⚛ experiment, ⚙ data compilation, ☷ zone-architecture internal).

---

## Verification Criteria

- [ ] Every equation in App A §A.2–A.5 appears in §A.6 reverse index (orphan check)
- [ ] Every GR test in Ch 2's 11-test suite appears in App B §B.1
- [ ] Every derived constant in Ch 13 and Ch 15 appears in App B §B.3 and App C
- [ ] Every cosmological parameter from Ch 14 appears in App B §B.4
- [ ] Every Vol 5 chapter (1–15) has ≥3 problems
- [ ] Bibliography ≥ 150 entries, sections balanced per plan
- [ ] No forward references in problem sets (to Ch N+1 or Vol 6)
- [ ] Headline honesty table (§B.9) lists every prediction with honest error classification
- [ ] App C §C.5 distinguishes GENUINE PREDICTION from CALIBRATION-DEPENDENT
- [ ] Fine structure constant appears as α⁻¹ = 137.17 ± 0.15 (0.1%) consistently throughout
- [ ] All notation matches Vol 1 Appendix B

---

*Phase 1 + Phase 2 complete. Phase 3 (draft) begins in the five component files in this folder.*
