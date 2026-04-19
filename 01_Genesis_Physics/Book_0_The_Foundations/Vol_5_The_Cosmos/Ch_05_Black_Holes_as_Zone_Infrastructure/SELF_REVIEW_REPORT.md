---
product: Foundations Vol 5
chapter: 5
title: Black Holes as Zone Infrastructure
phase: 4 (Self-Review)
date: 2026-04-09
status: PASS
---

# Chapter 5 Self-Review Report

## Word Count

Measured: ~11,900 words (target 9,000–13,000). **PASS.**

## Universal Author Checklist

### 1. "But why?" test

Every load-bearing claim in the chapter has an explicit reason:

- Why reinterpret? §5.0 — because Ch 1 leaves the interior underdetermined.
- Why does the Firmament redshift σ? §5.2.2 — because c² = σ/μ and c redshifts.
- Why is μ rigid? §5.2.3 — because bulk warp factor varies on a much longer scale than 4D gradients (Vol 1 §5.4).
- Why σ ≥ 0? §5.3.1 — Jeans instability from Vol 1 §5.6.
- Why r = r_s specifically? §5.3.2 — theorem from redshift formula plus positivity.
- Why not a singularity? §5.3.4 — the singularity is an artifact of analytic continuation past the brane's domain.
- Why S ∝ A? §5.6.2 — codimension of the boundary (2D surface in 3D brane).
- Why the factor 1/4? Footnote to (5.5.20) — brane-mode pairing + Gauss–Bonnet normalization.
- Why is Hawking radiation finite temperature? §5.6.3 — first law applied to the derived entropy.
- Why Kerr has two horizons? §5.7.1 — angle-dependent tension has two roots.
- Why doesn't the exterior change? §5.8.1 — the exterior metric is the same; exterior observables depend only on the exterior metric.

Every "why" has a local answer. **PASS.**

### 2. Forward dependency audit

Audited every concept introduced in Ch 5 against the prerequisite list in CHAPTER_SPEC.md:

- Membrane, σ, μ, c²=σ/μ: Vol 1 Ch 5 ✓
- Positivity and Jeans instability: Vol 1 §5.6 ✓
- Waters Above/Below, Z₂.₂.₁, Z₂.₂.₃: Vol 1 Ch 6 ✓
- Thermodynamic axiom, brane-mode counting: Vol 1 Ch 11 ✓
- Schwarzschild (5.1.34), Kerr (5.1.36), Bianchi identities: Vol 5 Ch 1 ✓
- Classical tests (used only as consistency check): Vol 5 Ch 2 ✓
- Ergosphere, ISCO, Penrose process: Vol 5 Ch 4 ✓
- QFT-on-curved-spacetime (Hawking preview only, full derivation deferred): Vol 4 ✓
- QCD scale reference: Vol 3 Ch 8 ✓

No concept is used before it is introduced. The Hawking radiation section is kept to a *preview* and explicitly forward-links Ch 6 for the full derivation. **PASS.**

### 3. Notation consistency

Checked against Vol 5 Symbol_and_Constants.md and against Ch 1 / Ch 4:

- r_s = 2GM/c² ✓ (matches (5.1.34))
- Kerr parameters a, Σ, Δ ✓ (matches (5.1.36))
- Entropy prefactor k_B A/(4 ℓ_P²) ✓
- T_H = ℏc³/(8π G M k_B) ✓
- Zone labels Z₂.₂, Z₂.₂.₁, Z₂.₂.₃ ✓
- Equation numbering (5.5.N) ✓ — 31 equations, contiguous, no gaps.

**PASS.**

### 4. Prerequisites satisfied

Every prerequisite in CHAPTER_SPEC.md maps to an existing or concurrently-drafted chapter. No circular dependencies. **PASS.**

### 5. "Why" chain complete

Seven questions in the spec; seven answers in §5.0–§5.8. §5.9.5 restates the chain as an explicit check for the But-Why reviewer. **PASS.**

### 6. Word count in range

11,900 words / target 9,000–13,000. **PASS.**

### 7. TODO markers

grep for `[TODO]`: 0 hits. **PASS.**

### 8. Figure audit

Seven figure placeholders in the draft after the Fig 5.5.3 and Fig 5.5.7 additions. Each has a complete spec in CHAPTER_OUTLINE.md. Inventory:

| ID | Location | Type | Status |
|---|---|---|---|
| Fig 5.5.1 | §5.3.4 (after the key observation) | Comparison | PLACEHOLDER |
| Fig 5.5.2 | §5.2 (after the tension profile derivation) | Plot | PLACEHOLDER |
| Fig 5.5.3 | §5.3.3 (after spatial description of bulk) | Schematic | PLACEHOLDER |
| Fig 5.5.4 | §5.5 (inside vs. outside) | Schematic | PLACEHOLDER |
| Fig 5.5.5 | §5.6.2 (area law) | Diagram | PLACEHOLDER |
| Fig 5.5.6 | §5.7 (Kerr puncture) | Cross-section | PLACEHOLDER |
| Fig 5.5.7 | §5.9 (reviewer's ledger) | Table | PLACEHOLDER |

Every spatial relationship, transformation, multi-step derivation, and conceptual model in the chapter has a figure. **PASS.**

## Foundations-Specific Checks

- Every derivation starts from a previously established result, with equation number citations. ✓
- Every equation is numbered. ✓
- Key results (tension profile (5.5.12), breach theorem §5.3.2, critical density (5.5.16), entropy (5.5.20), Hawking T (5.5.24), Kerr horizons (5.5.30), consistency theorem 5.5.2) are boxed or set off as theorems. ✓
- Problem sets in three buckets — computational, conceptual, challenge. §5.10 has 5 computational + 5 conceptual + 2 challenge = 12 problems. ✓

## Requirement Traceability (R5.5.1–R5.5.8)

| Req | Where addressed | Status |
|---|---|---|
| R5.5.1 Schwarzschild/Kerr as limits of zone framework | §5.1.2, §5.2, §5.7 | MET |
| R5.5.2 Event horizons from breach criterion | §5.3.2 (theorem), §5.5 | MET |
| R5.5.3 BH thermodynamics from Vol 1 Ch 11 | §5.6.2 | MET |
| R5.5.4 Hawking radiation previewed, Ch 6 deferred | §5.6.4 | MET |
| R5.5.5 ρ_crit derived from membrane mechanics | §5.4.2 | MET |
| R5.5.6 Consistency with Chs 1–4 | §5.8.1 theorem | MET |
| R5.5.7 Theologian: terminology as naming convention | §5.0, §5.9.4 | MET |
| R5.5.8 "But Why?" answered from geometry | §5.9.5 chain | MET |

All eight requirements met.

## Product-Specific Check: Theologian

§5.0 and §5.9.4 explicitly disclaim any theological weight on the word "breach," "Firmament," "Waters Above/Below." These are zone-architecture labels inherited from Vol 1's naming convention, not doctrinal claims. No preaching; no verses cited. **PASS.**

## Product-Specific Check: But Why?

§5.9.5 walks the full seven-step chain with a one-line geometric answer for each step. No appeal to authority; no "because that's how it works." **PASS.**

## Research Gaps (carried forward from spec)

- G1 (nonlinear σ in r < r_s): not needed — interior is not membrane.
- G2 (breach-mode boundary condition): deferred to Ch 6 with explicit pointer in §5.6.4.
- G3 (ρ_crit QCD prefactor): flagged in §5.4.4 with both values reported.
- G4 (full BH entropy via QFT-on-curved-spacetime): Vol 4 cited in §5.6.2 footnote.

## Overall Verdict

**PASS.** Chapter 5 is ready for Phase 5 (Reviewer Agent Verification).

---

*End of SELF_REVIEW_REPORT.md.*
