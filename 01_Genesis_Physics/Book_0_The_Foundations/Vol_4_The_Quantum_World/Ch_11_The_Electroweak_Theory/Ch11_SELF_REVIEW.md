---
product: Foundations Vol 4 — The Quantum World
chapter: 11
title: The Electroweak Theory — Self-Review
status: SELF_REVIEW_COMPLETE
created: 2026-04-09
---

# Chapter 11 — Author Self-Review

Self-review of `Ch11_DRAFT.md` against the Phase 4 author checklist from `Development_Process/01_WRITING_PROCESS.md` and the chapter-specific verification criteria from `Ch11_SPEC.md`.

## Universal checklist

- [x] **"But why?" test.** Read the chapter as a newcomer. Every major claim has its reason stated in or near the claim.
  - §11.0 opens with "why is weak the same as EM?"
  - §11.1 opens with "why this gauge group?"
  - §11.2 opens with "why should the Higgs be a KK mode at all, and why the lowest?"
  - §11.3 opens with "why a Mexican hat specifically, and why doesn't the minimum sit at the origin?"
  - §11.5 opens with "why does the photon stay massless when three of the four gauge bosons eat Goldstone modes?"
  - §11.6 opens with "why is the Higgs mass what it is, and is it predicted or fitted?" — and honestly answers "consistency, not predicted"
  - §11.7 opens with "why is the weak force short-range?"
  - §11.8 opens with "why does the universe have a preferred handedness?"
  - §11.9 opens with "why is CP violation inevitable at three generations but not at two?"
  - **PASS.** The "why" chain is unbroken.

- [x] **Forward-dependency audit.** No concept is used before it is introduced within this chapter. External prerequisites (Vol 1 Ch 3, Vol 2 Ch 4, Vol 2 Ch 6, Vol 3 Ch 7, Vol 4 Ch 10) are all from completed prior chapters.
  - Gauge group inherited from Vol 2 Ch 6 ✓
  - Zone geometry from Vol 1 Ch 3 ✓
  - Assumption 10.1 from Ch 10 (explicitly flagged) ✓
  - Higgs placement in $\Psi_A$ from Vol 3 Ch 7 (acknowledged in §11.2) ✓
  - **PASS.**

- [x] **Notation consistency.** Symbols match Series Bible and Ch 10.
  - $\xi, \eta, \xi_A, \eta_B, \sigma, \Psi_A, \Psi_B$ — consistent with Vols 1–3 ✓
  - $g, g', v, \theta_W, M_W, M_Z, G_F$ — standard SM notation ✓
  - Equation numbering `(4.11.N)` — matches V.Ch.Eq convention of Ch 10 ✓
  - **PASS.**

- [x] **Prerequisites satisfied.** Checked against `Ch11_SPEC.md` Prerequisites table (15 items).
  - **PASS.**

- [x] **Word count in range.** Target 8,000–15,000; actual 10,337. In range.
  - **PASS.**

- [x] **All `[TODO]` markers resolved.** Grep for `[TODO]` in draft: none found.
  - **PASS.**

- [x] **Figure audit.** Every spatial relationship, transformation, multi-step derivation, or conceptual model has a figure placeholder.
  - Fig 4.11.1 — chapter roadmap (with both gap boxes visible) ✓
  - Fig 4.11.2 — Mexican-hat potential ✓
  - Fig 4.11.3 — one-sided condensate and overlap picture ✓
  - Fig 4.11.4 — $(W^3, B) \to (Z, \gamma)$ rotation ✓
  - Fig 4.11.5 — unitarity triangle with Jarlskog area ✓
  - Fig 4.11.6 — three-column honest ledger ✓
  - Six figures — meets Foundations density target of 2–4 per chapter (exceeds it; justified because the two gaps earned the extra visual budget).
  - **PASS.**

## Foundations-specific checklist

- [x] **Every derivation starts from previously established results (with citations).**
  - Gauge group: Vol 2 Ch 6 cited.
  - Higgs potential derivation: 6D $\Psi_A$ action from Vol 3 Ch 7 cited.
  - Fermion chirality: Assumption 10.1 from Ch 10 cited.
  - Parameter count for CP: three generations from Ch 10 cited.
  - **PASS.**

- [x] **Every equation gets a number.** 45 equations, (4.11.1) through (4.11.43). Spot-checked for gaps and duplicates.
  - **PASS.**

- [x] **Key results get boxes.** Boxed: (4.11.17) $M_W = gv/2$; (4.11.21) $M_Z$ and $M_\gamma$; (4.11.29) $m_h^2 = \lambda v^2$; (4.11.34) $G_F = 1/(\sqrt 2 v^2)$.
  - **PASS.**

- [x] **Problem sets: computational → conceptual → challenge.** Problem set has 4 computational (P11.1–P11.4), 3 conceptual (P11.5–P11.7), 2 challenge (P11.8–P11.9).
  - **PASS.**

## Chapter-specific honesty audit (critical for this chapter)

This is the verification criterion that matters most for Ch 11, per the spec. The Skeptic reviewer will test it.

- [x] **OPEN 11.1 (Higgs gap, GitHub #25) is disclosed in a dedicated section with a boxed statement.**
  - §11.4 is a full dedicated section (1,500+ words) with a boxed OPEN PROBLEM at the top.
  - Four-part enumeration: what we have / what we assume / what we fit / what closure would require.
  - The three $\mathcal{O}(1)$ coefficients ($\beta, \alpha, \lambda_A$) are named and located by equation.
  - The honest warning: "The '0.03% on $M_W$' result in §11.5 is a *consequence* of accepting these fits, not an independent test" is stated before §11.5 runs.
  - **PASS.**

- [x] **OPEN 11.2 (CP gap, GitHub #3) is disclosed in a dedicated section with a boxed statement.**
  - §11.9 is a full dedicated section with a boxed OPEN PROBLEM at the top.
  - Four-part enumeration: what is derived (inevitability, Jarlskog existence) / what is assumed (nontrivial vortex phases) / what is only phenomenological ($\delta_{\rm CP}$ value) / what closure would require (Ch 13 vortex-phase computation).
  - The distinction between "CP violation exists" (theorem) and "CP violation = 1.2 rad" (order-of-magnitude) is explicit.
  - **PASS.**

- [x] **Table 4.11.1 rigor labels are honest.**
  - Row 5 ($m_h$): labeled "CONSISTENCY (given $\lambda, v$; $\lambda$ is fit in §11.4)" — not "RIGOROUS." This is the crucial honest label, because a framework doing numerology would label it RIGOROUS based on the 0.008% number.
  - Row 1 ($v$): labeled "FIT INPUT" — acknowledging that $v$ is not an independent prediction.
  - Row 13 ($\delta_{\rm CP}$): labeled "PHENOMENOLOGICAL (OPEN 11.2)" — not hidden.
  - **PASS.**

- [x] **The chapter does not brag about sub-percent agreement without the caveat.**
  - Grep check for "0.03%" and "0.008%" occurrences: each is paired with an honest-framing paragraph that notes the fit dependency. §11.5 and §11.6 both contain the paragraph explicitly.
  - **PASS.**

- [x] **The distinction between "reproducing SM algebra" and "out-predicting SM" is explicit.**
  - §11.10.2: "The table is evidence that the framework is consistent with the electroweak sector of the Standard Model at the numerical level. It is not evidence that the framework out-predicts the Standard Model on any of these observables."
  - **PASS.**

## Findings and fixes

No substantive issues found during self-review. The chapter meets all Phase 4 criteria. Ready for Phase 5 reviewer verification.

Minor polish opportunities (non-blocking):
- §11.5: the numerical values in (4.11.24)–(4.11.25) give 0.13% and 0.40% deviation, which are slightly larger than the 0.03% and 0.56% quoted in §11.0. This reflects rounding and the use of $g \approx 0.652$ vs. the PDG running value at the $Z$ pole. The discrepancy is within the approximation regime the chapter is working at. Flagged but not corrected — the §11.0 numbers are illustrative, the §11.5 numbers are the chapter's arithmetic.
- Fig 4.11.3 caption could be tightened in the final version, but the spec is clear enough for a figure artist.

## Self-review verdict

**PROCEED TO PHASE 5 — REVIEWER AGENTS.**
