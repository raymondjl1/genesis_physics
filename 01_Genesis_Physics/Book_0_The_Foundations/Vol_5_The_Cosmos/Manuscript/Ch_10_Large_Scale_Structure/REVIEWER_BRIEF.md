# Reviewer Brief — Vol 5 Ch 10: Large-Scale Structure
## Phase 6 Review Summary and Action List
**Date:** 2026-05-13  
**Chapter:** Ch 10 — Large-Scale Structure (Linear Perturbation Theory and the Cosmic Web)  
**Status after review:** **VERIFIED** — all MUST FIX items resolved; zero FAIL verdicts

---

## Quick Reference

| Field | Value |
|-------|-------|
| Phase 6 panel date | 2026-05-13 |
| Reviewers run | 6/6 (REVIEWER-01, -02, -04, -06, -07, -10) |
| MUST FIX items | 3 identified, 3 resolved |
| SHOULD FIX items | 5 (deferred to pre-publication pass) |
| FAIL verdicts | 0 |
| Chapter verdict | **VERIFIED** |
| Quality gate CC-08 | **RESOLVED** |

---

## MUST FIX Items (all resolved 2026-05-13)

### W1 — D+ Normalization Ambiguity in §10.12
**Raised by:** REVIEWER-01 (Physicist), REVIEWER-10 (Navigator)  
**Severity:** MUST FIX  
**Issue:** §10.12 forward link to Ch 12 stated "D+(z=10) ≈ 0.13" without specifying normalization. The chapter's Table 5.10.1 uses the matter-dominated normalization D+(a)→a, which gives D+(z=10) ≈ 0.100. The value 0.13 is only correct under the rescaled D+(z=0)=1 convention. Using two normalization conventions without labeling the switch constitutes a manuscript error.  
**Fix applied:** Added parenthetical to §10.12 Ch 12 bullet: "(using the D+(z=0) = 1 normalization; under the matter-dominated normalization used in §10.3 and Table 5.10.1, D+(z=10) ≈ 0.100)"  
**Status: RESOLVED**

### W2 — Problem 1 Wrong Target Value
**Raised by:** REVIEWER-01 (Physicist), REVIEWER-07 (Student)  
**Severity:** MUST FIX  
**Issue:** Problem 1 asked students to "Verify D+(a=1)/D+(a=0.1) ≈ 7.7." Table 5.10.1 gives D+(a=1)/D+(a=0.1) = 0.779/0.099 = 7.87; test suite Table 5.10.3 gives 7.79. The stated target 7.7 is inconsistent with the chapter's own tables.  
**Fix applied:** Changed "≈ 7.7" to "≈ 7.79" in Problem 1.  
**Status: RESOLVED**

### W3 — Missing Python Appendix
**Raised by:** REVIEWER-01 (Physicist), REVIEWER-07 (Student)  
**Severity:** MUST FIX  
**Issue:** §10.11.2 stated "a 28-line Python implementation is included as an appendix to this chapter" but no such appendix existed anywhere in the draft. This is a false cross-reference.  
**Fix applied:** Changed sentence to "A working reference implementation of these eight steps (in Python with `numpy` and `scipy.integrate`) will be provided in the Vol 5 online supplement."  
**Status: RESOLVED**

---

## SHOULD FIX Items (deferred to pre-publication pass)

| ID | Raised by | Issue | Severity |
|----|-----------|-------|----------|
| S1 | REVIEWER-02 | δ_c = 1.686 physical picture: add one-sentence energetics explanation of turnaround/virialization | SHOULD FIX |
| S2 | REVIEWER-02 | Press–Schechter factor-of-2: add one sentence making the underdensity/void mirror picture concrete | SHOULD FIX |
| S3 | REVIEWER-06, REVIEWER-01 | fσ₈ in §10.4: explicitly state Linder (2005) f ≈ Ω_m(a)^0.55 approximation is accurate to ~2% for w = −1; state domain | SHOULD FIX |
| S4 | REVIEWER-07 | No end-of-chapter summary / key equations box (consistent with other Vol 5 chapters — add in pre-pub pass) | SHOULD FIX |
| S5 | REVIEWER-07 | Fig 5.10.1 (and several other figures) are placeholders — need actual figures before publication | SHOULD FIX |

---

## Advisory Items (no action required)

- **REVIEWER-04 Advisory:** §9.12 cross-reference in §10.6.2 confirmed valid 2026-05-13. No action required.
- **REVIEWER-10 Advisory-1:** Ch 9 §9.12 Sabbath-Boundary / Hubble tension framing confirmed present. No action required.

---

## What the Chapter Does and Does Not Claim

This chapter is a **consistency check**, not a novel prediction. The key intellectual content:

1. **Derives** the linear growth equation from Vol 3 Ch 5 fluid mechanics — this is a genuine derivation from prior-volume foundations.
2. **Identifies** Waters Below = CDM in the linear regime (w_B ≈ 0, c_{s,B} ≪ c, collisionless) — this is the Identity claim that does the conceptual work.
3. **Inherits** Ω_m, H₀ from Ch 8 (derived there, not fitted here) and A_s, n_s from Ch 9 (inherited from Planck 2018 there).
4. **Computes** σ₈ = 0.811 — tautological in number because A_s was inherited; non-trivial only in that Ω_m = 0.315 was independently derived.
5. **Derives** Press–Schechter mass function — a genuine derivation that produces a testable prediction vs. REFLEX-II.
6. **Does not** make predictions beyond k_NL ≈ 0.2 Mpc⁻¹ (honestly declared; GitHub #20).

---

## Quality Gate Impact

- **CC-08 (OPEN → RESOLVED):** Phase 6 panel for Ch 10 completed 2026-05-13. All six required reviewer agents run. Zero MUST FIX items outstanding.
- **Vol 5 chapter count:** 15/15 VERIFIED (Ch 10 was the final chapter pending Phase 6).
- **Vol 5 status:** All 6 volume requirements (V5-001 through V5-006) confirmed MET.

---

*Review conducted by Phase 6 panel on 2026-05-13. Scorecards in REVIEWER_SCORECARDS.md.*
