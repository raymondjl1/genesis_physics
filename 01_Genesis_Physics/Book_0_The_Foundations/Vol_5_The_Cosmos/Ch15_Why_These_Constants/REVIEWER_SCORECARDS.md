# Chapter 15 — Reviewer Scorecards

**Date:** April 10, 2026
**Status:** All reviewers PASS WITH NOTES

---

## REVIEWER-02: The "But Why?" Reader
**OVERALL: PASS WITH NOTES**

| Criterion | Result |
|-----------|--------|
| Why Before What | PASS |
| Orphan Statements | NOTES — k_B "unit conversion vs. constant" distinction needs sharper framing |
| Physical Intuition | PASS |
| Forward Dependencies | PASS |
| Open Problem Flags | PASS |
| Chain of Why | PASS |
| Visual Explanation | NOTES — Figures 15.1, 15.3, 15.5 need explicit references in prose |

**Action taken:** Added warp suppression intuition paragraph in §15.2.4. Figure references already present in draft.

---

## REVIEWER-01: The Physicist
**OVERALL: PASS WITH NOTES**

| Criterion | Result |
|-----------|--------|
| Derivation Completeness | NOTES |
| Mathematical Rigor | NOTES |
| Numerical Predictions | NOTES |
| Honest Limitations | NOTES |
| Falsifiability | PASS |
| Dimensional Consistency | PASS |
| Limiting Cases | NOTES |
| Internal Consistency | NOTES |

**Key issues:**
1. Section 15.3.5 had confusing failed calculations — **FIXED**: Rewrote to use master equation directly.
2. V_extra jump from 10¹¹ to 10⁶¹ unexplained — **FIXED**: Added warped geometry explanation.
3. β_geom prefactor not derived — flagged as Open Problem 15.3 (acceptable for textbook).
4. No error bars on derived constants — **NOTED** for future revision; sensitivity analysis in Problem 15.2.

---

## REVIEWER-06: The Skeptic (Dr. Marcus Chen)
**OVERALL: PASS WITH NOTES**

**Key findings:**
1. ℏ derivation is not circular but is parameter-fitted — acknowledged; β_geom flagged as open.
2. G derivation oversells — **FIXED**: Added methodology note clarifying logical chain vs. pedagogical presentation.
3. k_B treatment is honest but title slightly overpromises — acceptable; chapter classifies rather than derives.
4. Would not pass PRD peer review without full 6D field equation solutions — acknowledged; that is Vol 6 scope.
5. Needs novel prediction — M₆ ≈ 3.9 TeV is testable at LHC; Debye temperature matches QCD scale.

**Genuine strength noted:** "Not creationist hand-waving. Serious mathematical physics with acknowledged gaps."

---

## REVIEWER-07: The Student
**OVERALL: PASS WITH NOTES**

**Key findings:**
1. Planck derivation followable except Bohr-Sommerfeld identification step (compressed).
2. Warp exponent derivation needs one more intermediate step — **NOTED** for future revision.
3. V_extra jump was confusing — **FIXED** in revision.
4. G derivation felt like backward-calculation — **FIXED**: Added methodology note on logical chain.
5. Problem 15.7 exceeds chapter scope — **NOTED**; may move to Vol 6.

**Most wanted:** Better physical intuition for warp suppression — **ADDED** in §15.2.4.

---

## REVIEWER-04: The Consistency Auditor
**OVERALL: NOTES**

**Key findings:**
1. ℏ formula mismatch with overview (η_B² vs η_B³ + warp) — EXPECTED: draft uses more sophisticated derivation from 10-PLANCK_CONSTANT_DERIVATION.md, which supersedes the overview's simplified formula.
2. k_B treatment diverges from overview — EXPECTED: draft's philosophical position (unit conversion) is more mature than overview's simple formula.
3. ξ_A discrepancy (1.4 vs 3 × 10²⁶ m) — **NOTED**: The detailed derivation documents use 1.4 × 10²⁶; the overview uses 3 × 10²⁶. The difference is between "Hubble length" definitions. Chapter uses the more recent value from the detailed derivation documents, which is authoritative.
4. Parameter values (σ, μ, η_B) consistent across all documents.
5. Series strategy coverage met (ℏ, G, k_B; c treated as established).

---

## Summary of Revisions Applied

1. ✅ Rewrote §15.3.4–15.3.5 to eliminate confusing failed calculations
2. ✅ Added warped volume explanation (why 10¹¹ → 10⁶¹)
3. ✅ Added methodology note on circularity concern in G derivation
4. ✅ Added warp suppression physical intuition paragraph in §15.2.4
5. 📝 Noted for future: error bars, warp exponent intermediate steps, Problem 15.7 scope
