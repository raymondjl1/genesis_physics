# Chapter 14 — Self-Review (Author Checklist)

**Date:** 2026-04-10
**Draft Version:** 1.0

---

## Universal Checks

- [x] **"But why?" test** — Every claim in the chapter has a "why" answer. Key why-chains verified:
  - Why ρ_crit has its value → because H₀ and G₄ are zone-derived (§14.2)
  - Why Ω_DE ≈ 0.68 → warp-factor integral over ξ-dimension (§14.4.1)
  - Why Ω_k = 0 → Firmament equilibrium, not coincidence (§14.4.5)
  - Why same scales produce all couplings → 6D KK reduction with logarithmic Green's function (§14.6.1)
  - Why 0-parameter prediction matters → epistemic argument in §14.8

- [x] **Forward dependency audit** — No concepts from Ch 15 or Vol 6 are used. Forward pointers ("In the next chapter...") are limited to the closing sentence and clearly flagged.

- [x] **Notation consistency** — Checked against prior chapters:
  - H₀, Ω_i, ρ_crit consistent with Ch 8 notation
  - α, α_s, sin²θ_W consistent with Ch 13 notation
  - ξ_A, η_B, A(ξ), B(η) consistent with Vol 1 notation
  - Equation numbering follows (5.14.N) convention

- [x] **Prerequisites satisfied** — All concepts used are established in prior chapters as listed in the spec. Key cross-references verified:
  - Friedmann equation: Eq 5.8.26 (Ch 8)
  - Density split: Eq 5.8.6 (Ch 8, from Vol 1 Ch 6)
  - Fine structure master formula: Eq 5.13.40 (Ch 13)
  - Deceleration parameter: Eq 5.11.24 (Ch 11)

- [x] **"Why" chain complete** — All 7 questions from spec §"Why Chain" are answered in the text.

- [x] **Word count** — Approximately 10,500 words. Within target range (8,000–12,000).

- [x] **TODOs resolved** — No `[TODO]` markers in the draft.

- [x] **Figure audit** — Four figure placeholders:
  - Fig 5.14.1: Derivation roadmap (§14.1) — spec complete
  - Fig 5.14.2: Cosmic energy budget (§14.4) — spec complete
  - Fig 5.14.3: Gauge coupling convergence (§14.6) — spec complete
  - Fig 5.14.4: Master comparison pull plot (§14.8) — spec complete

---

## Foundations-Specific Checks

- [x] **Every derivation starts from previously established results** — Equation citations verified:
  - ρ_crit from Eq 5.8.26 (Friedmann)
  - Ω_i from Vol 1 Ch 6 warp-factor integrals
  - α_s from Λ_QCD = ℏc/η_B + standard QCD running
  - sin²θ_W from warp-geometry calculation + 10-COUPLING_CONSTANTS_DERIVATION.md

- [x] **Problem sets cover full difficulty range** — 4 computational + 4 conceptual + 3 challenge = 11 problems

- [x] **Every numerical prediction includes** predicted value, uncertainty, experimental value, percent error:
  - Table 14.1 contains all 16 parameters with full comparison

---

## Issues Found and Fixed During Self-Review

1. **Critical density numerical error.** Initial calculation used H₀ in wrong units (km/s/Mpc vs. s⁻¹). Fixed: ρ_crit = 8.54 × 10⁻²⁷ kg/m³. Cross-checked against Planck value 8.53 × 10⁻²⁷ — consistent.

2. **Weinberg angle intermediate error.** The draft initially showed the exponential formula giving sin²θ_W = 0.00733, which is wrong. Caught and corrected: the text now honestly shows the error in the simplified formula, explains why it fails, and transitions to the correct full calculation yielding 0.231. This is actually pedagogically useful — it shows the student a common trap.

3. **Matter-formation vs. cosmological critical density confusion.** Added explicit disambiguation in §14.2 with a boxed warning. These differ by 43 orders of magnitude.

4. **Ω_DM discrepancy honestly stated.** Ensured the 2.7% disagreement is flagged as YELLOW, not swept under the rug. Three possible causes are listed.

5. **Parameter-count argument precision.** Clarified that zone framework reduces from 6 to ~2 free parameters (τ and A_s), not to zero. Honesty check passed.

---

## Consistency Audit Against Prior Chapters

| Value | This Chapter | Prior Chapter | Match? |
|-------|-------------|---------------|--------|
| H₀ | 67.4 km/s/Mpc | Ch 8 Eq 5.8.47: 67.4 | ✓ |
| Ω_A | 0.684 | Ch 8 Eq 5.8.6: 0.684 | ✓ |
| Ω_B | 0.266 | Ch 8 Eq 5.8.6: 0.266 | ✓ |
| Ω_b | 0.049 | Ch 8 Eq 5.8.6: 0.049 | ✓ |
| q₀ | −0.527 | Ch 11 Eq 5.11.24: −0.527 | ✓ |
| α⁻¹ | 137.17 | Ch 13 Eq 5.13.40: 137.17 | ✓ |
| T₀ | 2.725 K | Ch 8 Eq 5.8.51: 2.725 K | ✓ |
| ξ_A | 3.0 × 10²⁶ m | Ch 13: 3.0 × 10²⁶ m | ✓ |
| η_B | 1.3 × 10⁻¹⁵ m | Ch 13: 1.3 × 10⁻¹⁵ m | ✓ |
| σ | 6.0 × 10⁹⁸ kg/(m·s²) | Vol 1 Ch 5: 6.0 × 10⁹⁸ | ✓ |

All values consistent with prior chapters.

---

## Overall Assessment

**PASS for self-review.** Ready for reviewer agents.

Key strengths:
- Comprehensive derivation of ~15 parameters from zone inputs
- Honest comparison table with GREEN/YELLOW assessment
- No cherry-picking — Ω_DM discrepancy prominently flagged
- Pedagogically useful Weinberg angle "trap and correction"
- Problem set covers full difficulty range with conceptually rich problems

Key risk areas for reviewer agents:
- The Physicist will probe the Weinberg angle derivation more deeply
- The Skeptic will question whether H₀ = 67.4 is "derived" or just inherited from Ch 8
- The Student will want more explicit intermediate steps in several derivations
- The Consistency Auditor will check the ρ_crit calculation against different unit systems
