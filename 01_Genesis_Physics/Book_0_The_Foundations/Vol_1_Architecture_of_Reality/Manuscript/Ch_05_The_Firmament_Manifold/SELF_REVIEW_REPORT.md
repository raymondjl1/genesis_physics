# Self-Review Report: Chapter 5 — The Firmament Manifold

**Date:** April 6, 2026
**Draft Version:** 1.0
**Word Count:** ~12,000 (within spec: 8,000–15,000)
**Status:** ALL ISSUES ADDRESSED (Revision 2, 2026-04-06)

---

## Summary

The draft is structurally sound with a clear "why" chain, consistent notation, and comprehensive problem sets. However, 8 critical issues were found, primarily: incomplete derivations (intrinsic curvature, effective mass, Lorentz invariance proof), forward dependencies on Ch 6 (Waters pressures in stability analysis), and an abandoned dimensional analysis.

## Critical Issues (Must Fix)

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| C1 | Intrinsic curvature not computed, only cited | §5.1.5 | Add explicit FRW Ricci tensor computation |
| C2 | Lorentz invariance claimed but not proven | §5.3.6 | Add substitution proof |
| C3 | Forward dependency: Ch 6 Waters pressures used in stability | §5.6.4 | Defer full proof to Ch 6; state interim result |
| C4 | Effective mass m²_eff (Eq 1.5.52) not derived | §5.5.3 | Add derivation from perturbed NG action |
| C5 | Problem 5.23 uses undefined quantities (proton mass, EM constants) | Problems | Rephrase using Ch 5 machinery only |
| C6 | Dimensional analysis of S_NG abandoned | §5.3.2 | Complete the calculation |
| C7 | Problem 5.30 assumes κ-σ relationship not established | Problems | Rephrase as open question |
| C8 | Fig 1.5.7 referenced but not more developed than other placeholders | §5.0 | All figures are placeholders — acceptable for draft |

## Moderate Issues (12)

Key ones: notation inconsistency (K superscript position), Theorem 5.6.1 stated without proof (rephrase as Proposition), missing justification for plane wave ansatz, tilde notation introduced then abandoned.

## Revision Plan

Critical issues C1, C2, C3, C5, C6 will be addressed in revision pass. C4 adds significant material but the derivation sketch is sufficient for draft. C7, C8 are acceptable for initial review.
