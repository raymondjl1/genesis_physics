# FIX LOG — Volume 2: Forces and Fields
**Revision date:** 2026-05-14  
**Reviewer:** Subagent (Claude Sonnet 4.6)  
**Based on:** REVIEW_REPORT_Vol2.md — 7 critical blockers (BLOCKER-01 through BLOCKER-07)

All edits are surgical: no chapter was rewritten. Each fix is documented below with: chapter, location, change, reason.

---

## Phase 1 — Error Corrections

### FIX-01: Ch02 — Route 1 labeled as failing
- **File:** `Ch_02_Gravity_from_Zone_Curvature/Ch02_DRAFT.md`
- **Location:** §2.4.1, opening of "Route 1: G₄ from Volume Dilution"
- **Change:** Added italic note: *"This route fails to give the correct numerical value of G₄ without self-consistency fitting — presented to motivate Route 2."*
- **Reason:** Route 1 produces G₄ ≈ 5×10⁻⁴⁷ m³kg⁻¹s⁻², 36 orders of magnitude from the correct value. Presenting it without a status label misleads the reader. The chapter already had an honest note at the end of §2.4.1; this adds a visible upfront marker.

### FIX-02: Ch02 — G₄ dimensional inconsistency flagged (BLOCKER-02)
- **File:** `Ch_02_Gravity_from_Zone_Curvature/Ch02_DRAFT.md`
- **Location:** §2.4.2, equation 2.2.29 ($G_N = c^4/(8\pi\sigma L^2_\text{eff})$)
- **Change:** Added `⚠ DIMENSIONAL NOTE (Rev. 2026-05-14)` blockquote explaining that with σ in kg s⁻² and L_eff in m, the formula gives m²s⁻²kg⁻¹ not m³kg⁻¹s⁻². Points to Research Task RT-2.G. All G_N predictions marked provisional until RT-2.G is resolved.
- **Reason:** BLOCKER-02 from review — the formula has wrong units. This is a critical mathematical error that cannot be silently accepted.

### FIX-03: Ch02 — L_eff marked as phenomenological parameter
- **File:** `Ch_02_Gravity_from_Zone_Curvature/Ch02_DRAFT.md`
- **Location:** §2.4.2, parameter list item for L_eff
- **Change:** Appended "(L_eff is a phenomenological parameter in this derivation, determined by matching to the observed G_N. It is not yet derived from first principles — see Research Task RT-2.G.)"
- **Reason:** BLOCKER-07 — L_eff = 8.96×10⁻²⁹ m is matched to observation, not derived. Honest disclosure required.

### FIX-04: Ch04 — Z₃ orbifold correction on real coordinate (BLOCKER-01)
- **File:** `Ch_04_Strong_and_Weak_Forces_from_Zone_Boundary_Effects/Ch04_DRAFT.md`
- **Location:** §4.2, after equation 2.4.1 (Gaussian warp factor)
- **Change:** Added `⚠ Mathematical Correction (Rev. 2026-05-14) — Z₃ Orbifold on Real Coordinate` blockquote explaining that η → e^{2πi/3}η is undefined for real η. The correct construction requires a two-dimensional complex fiber w = η₁ + iη₂, with Z₃ acting as w → e^{2πi/3}w. Full derivation deferred to Vol 4 as Research Task RT-2.SU3. Updated orbifold condition equation to use complex coordinate w.
- **Reason:** BLOCKER-01 — applying a complex phase rotation to a real coordinate is mathematically undefined. This is the most critical mathematical error in the volume.

### FIX-05: Ch04 — Rigor Level for §4.2 updated
- **File:** `Ch_04_Strong_and_Weak_Forces_from_Zone_Boundary_Effects/Ch04_DRAFT.md`
- **Location:** §4.2, "Rigor Level" statement at end of section
- **Change:** Changed from "RIGOROUS" to "PROVISIONALLY RIGOROUS — PENDING RT-2.SU3" with explanation.
- **Reason:** The rigor claim was incorrect given the Z₃ fix required above.

### FIX-06: Ch09 — Hierarchy circularity flagged (BLOCKER-03)
- **File:** `Ch_09_The_Hierarchy_Problem_Solved/Ch09_DRAFT.md`
- **Location:** §9.3, after equation 2.9.21 (G₆ back-calculated from measured G₄)
- **Change:** Added `⚠ Derivation Status (Rev. 2026-05-14)` blockquote explaining the two directions of the identity G_N = G₆/V_extra: (a) independent derivation (predicts G₄) vs. (b) consistency check (back-calculates G₆). The current chapter uses direction (b). Points to Research Task RT-2.G6. Updated Assumption flag [A2] to cross-reference the note.
- **Reason:** BLOCKER-03 — the chapter presents a consistency check as if it were a derivation. This is circular reasoning.

---

## Phase 2 — Honest Labeling

### FIX-07: Ch01 — Warp function provisional labels added
- **File:** `Ch_01_Why_Forces_Exist/Ch01_DRAFT.md`
- **Location:** After metric equation reference (§1.4.2) and after coupling integrals discussion
- **Change (applied in prior session):** Added two provisional labels: "[Provisional — warp functions A(ξ,η), B(ξ,η) not yet derived from 6D Einstein equations. See Open Problem 1.WF.]"
- **Reason:** BLOCKER-06 (partial) — warp functions used before derivation.

### FIX-08: Ch01 — K≈1.44 Vol 4 dependency disclosed
- **File:** `Ch_01_Why_Forces_Exist/Ch01_DRAFT.md`
- **Location:** Fine structure coefficient description
- **Change (applied in prior session):** Added: "The geometric factor K ≈ 1.44 depends on the effective particle content of the Standard Model (derived in Vol 4); see the parameter disclosure in Ch 3, §3.7.4."
- **Reason:** BLOCKER-04 — anticipatory use of SM particle content not disclosed.

### FIX-09: Ch02 — Warp function provisional label added
- **File:** `Ch_02_Gravity_from_Zone_Curvature/Ch02_DRAFT.md`
- **Location:** After metric equation 2.2.2 reference
- **Change (applied in prior session):** Added: "[Provisional — warp functions A(ξ,η), B(ξ,η) not yet derived from 6D Einstein equations. See Open Problem 1.WF.]"
- **Reason:** Open Problem 1.WF — warp functions are assumed, not derived.

### FIX-10: Ch02 — Warp profile inconsistency note added
- **File:** `Ch_02_Gravity_from_Zone_Curvature/Ch02_DRAFT.md`
- **Location:** After equation 2.2.5
- **Change (applied in prior session):** Added note explaining that Ch02 uses exponential profile B_η = B₀ − γη/2 while Ch04 uses Gaussian B(η) = −γ²η²/2. These are distinct. Canonical profile must be established — see Open Problem 2.WP.
- **Reason:** BLOCKER-06 — two chapters use incompatible warp profiles for the same dimension.

### FIX-11: Ch03 — Fine structure coefficient b_eff disclosure (BLOCKER-04)
- **File:** `Ch_03_Electromagnetism_from_Membrane_Wave_Propagation/Ch03_DRAFT.md`
- **Location:** §3.7.3, after equation 2.3.80 (C = b_eff/(2π) ≈ 1.44)
- **Change:** Added `Parameter Disclosure (Rev. 2026-05-14)` blockquote explaining that b_eff ≈ 9.05 is computed from SM particle content derived in Vol 4, not in this volume. The derivation chain runs Vol 4 → Vol 2. The definitive version is Vol 5, Ch 13. The value α⁻¹ ≈ 137.04 is a consistency check, not a parameter-free prediction, until Vol 4 closes the loop.
- **Reason:** BLOCKER-04 — the fine structure derivation silently uses Vol 4 results as input.

### FIX-12: Ch04 — Warp profile cross-reference note added
- **File:** `Ch_04_Strong_and_Weak_Forces_from_Zone_Boundary_Effects/Ch04_DRAFT.md`
- **Location:** §4.2, after equation 2.4.1
- **Change:** Added warp profile note blockquote: Ch04 uses Gaussian B(η) = −γ²η²/2; Ch02 uses exponential. These are distinct. See Open Problem 2.WP.
- **Reason:** BLOCKER-06 — cross-volume inconsistency disclosure.

### FIX-13: Ch04 — sin²θ_W deferral note added (BLOCKER-05)
- **File:** `Ch_04_Strong_and_Weak_Forces_from_Zone_Boundary_Effects/Ch04_DRAFT.md`
- **Location:** After equation 2.4.43 (sin²θ_W = 0.2312)
- **Change:** Added `⚠ Derivation Status (Rev. 2026-05-14)` blockquote explaining that the value 0.2312 is not derived in this volume. The tree-level zone formula gives ≈0.13; the measured value requires radiative corrections. Marked as PENDING — Research Task RT-2.SW.
- **Reason:** BLOCKER-05 — sin²θ_W appears as a prediction without derivation.

### FIX-14: Ch05 — Warp function provisional label added
- **File:** `Ch_05_The_Zone_Lagrangian/Ch05_DRAFT.md`
- **Location:** §5.2.2, after the statement about warp factors A(ξ,η), B(ξ,η) being determined by the 6D Einstein equations
- **Change:** Added provisional label: "[Provisional — warp functions not yet derived from 6D Einstein equations in closed form. See Open Problem 1.WF. All coupling integrals and numerical predictions depending on A(ξ,η) or B(ξ,η) are provisional.]"
- **Reason:** Open Problem 1.WF — warp functions used throughout but not yet self-consistently derived.

### FIX-15: Ch06 — Warp function provisional label added
- **File:** `Ch_06_Gauge_Theory_from_Zone_Symmetries/Ch06_DRAFT.md`
- **Location:** After metric equation 2.6.1
- **Change:** Added: "[Provisional — warp functions A(ξ,η), B(ξ,η) not yet derived from 6D Einstein equations in closed form. See Open Problem 1.WF.]"
- **Reason:** Open Problem 1.WF consistency across chapters.

### FIX-16: Ch06 — Z₃ orbifold consistency note added
- **File:** `Ch_06_Gauge_Theory_from_Zone_Symmetries/Ch06_DRAFT.md`
- **Location:** §6.4.2, after equation 2.6.18 (polar coordinate definition)
- **Change:** Added note explaining that the polar coordinate formulation ψ ~ ψ + 2π/3 is the correct implementation of the Ch04 Z₃ correction: it corresponds to w → e^{2πi/3}w on the complex plane w = ξ + iη. Declared that this section's approach supersedes Ch04 §4.2 for rigorous analysis.
- **Reason:** BLOCKER-01 follow-through — the fix in Ch04 must be consistent with Ch06's treatment.

### FIX-17: Ch08 — G_N provisional cross-reference added
- **File:** `Ch_08_Gravitational_Field_Theory/Ch08_DRAFT.md`
- **Location:** §8.1.1, G₄ bullet point in parameter list
- **Change:** Added inline note pointing to Ch02 §2.4.2 dimensional issue and Research Task RT-2.G. Noted that the numerical value used is the measured value; zone derivation is provisional.
- **Reason:** BLOCKER-02 consistency — Ch08 uses the G_N value from Ch02 without acknowledging the dimensional issue.

### FIX-18: Ch10 — Beta function coefficients disclosed as SM values (BLOCKER-04)
- **File:** `Ch_10_Running_Couplings_and_Zone_Energy_Scales/Ch10_DRAFT.md`
- **Location:** §10.3, before equations 2.10.12–2.10.18 (beta coefficient derivations)
- **Change:** Added `Parameter Disclosure (Rev. 2026-05-14)` blockquote stating that b₁ = −41/10, b₂ = 19/6, b₃ = 7 are Standard Model values computed from SM particle content. That content is not derived in this volume — it is empirical input here, to be derived from zone topology in Vol 4. Cross-referenced RT-2.SU3 for SU(3).
- **Reason:** BLOCKER-04 — beta coefficients depend on SM particle content not yet derived from zone architecture.

### FIX-19: Ch11 — sin²θ_W pending note added (BLOCKER-05)
- **File:** `Ch_11_The_Force_Landscape/Ch11_DRAFT.md`
- **Location:** §11.3.1, predictions table and following text for Weinberg angle
- **Change:** (1) Marked table entry as "0.231 *(PENDING — see note below table)*". (2) Added `⚠ Prediction Status — PENDING (Rev. 2026-05-14)` blockquote after the Weinberg angle paragraph, explaining tree-level value ≈0.13 vs measured 0.231, deferring to Vol 4 + Research Task RT-2.SW.
- **Reason:** BLOCKER-05 — sin²θ_W is presented as a zone prediction without a derivation. The F1–F13 falsification tests were preserved exactly unchanged.

---

## Research Tasks Generated by This Review

| Task ID | Description | Status |
|---------|-------------|--------|
| RT-2.G | Correct dimensional derivation of G_N = c⁴/(8πσL²_eff) | OPEN |
| RT-2.G6 | Independent derivation of G₆ from 6D action without using measured G_N | OPEN |
| RT-2.SU3 | Rigorous Z₃ orbifold on 2D complex Waters Below fiber | OPEN |
| RT-2.SW | Full derivation of sin²θ_W including radiative corrections | OPEN |

## Open Problems Referenced

| Problem ID | Description |
|------------|-------------|
| OP 1.WF | Self-consistent derivation of warp functions A(ξ,η), B(ξ,η) from 6D Einstein equations |
| OP 2.WP | Canonical Waters Below warp profile — resolve exponential (Ch02) vs. Gaussian (Ch04) inconsistency |

---

*End of Fix Log*
