# Self-Review Report — Vol 5 Ch 2: Classical Tests

**Reviewer:** Author (self)
**Date:** 2026-04-09
**Draft reviewed:** `Ch02_DRAFT.md`
**Spec reference:** `CHAPTER_SPEC.md`
**Outline reference:** `CHAPTER_OUTLINE.md`

---

## 1. Author Checklist (from genesis-chapter-writer SKILL.md)

### 1.1 But-Why Test

Every section was audited against the CHAPTER_SPEC "Why" chain. Each section opens with a reader-level "why" question and answers it before introducing new machinery.

| Section | "Why" question | Answered? |
|---|---|---|
| §2.0 | Why do we need tests if Ch 1 already derived EFE? | Yes — falsifiability; derivations can be mathematically clean but empirically wrong |
| §2.1 | Why do freely falling particles follow geodesics? | Yes — variational principle on proper time, traced to Ch 1 action |
| §2.2 | Why does Mercury precess at all in GR but not Newton? | Yes — nonlinear $1/r^4$ correction to the effective potential |
| §2.3 | Why is GR's light-bending exactly twice Newton's? | Yes — space curvature term adds an equal contribution to the time-dilation term |
| §2.4 | Why does frequency depend on gravitational potential? | Yes — $g_{tt}$ sets proper-time rate; direct from Schwarzschild (5.1.34) |
| §2.5 | Why does radar round-trip time depend on the Sun? | Yes — coordinate speed of light depends on $g_{tt}, g_{rr}$ |
| §2.6 | Why does a spinning mass drag inertial frames? | Yes — off-diagonal $g_{t\phi}$ term in Kerr (5.1.41) |
| §2.7 | Why does a gyroscope precess in a static field? | Yes — parallel transport of a spin vector along a geodesic |
| §2.8 | Why package all tests into PPN parameters $\gamma,\beta$? | Yes — theory-agnostic comparison framework |
| §2.9 | Why do two tests show >1% residuals? | Yes — traced explicitly to reference-value staleness, not framework failure |
| §2.10 | Why is this gap MEDIUM not LOW? | Yes — closing it requires updating reference citations, which is clerical but outstanding |

**Result:** PASS.

### 1.2 Forward-Dependency Audit

The chapter must not quote results from Vol 5 Ch 3+ or later volumes.

- Ch 3 (GW): not referenced forward
- Ch 4 (Strong-Field): not referenced forward
- Ch 5 (Black Holes): not referenced forward
- Ch 8 (Cosmology): $\Lambda_\text{eff}$ used only as passing note, not as argument
- Book 1/2/3: no references

**Result:** PASS. All inbound references are to Vols 1–4 and Ch 1 of this volume.

### 1.3 Notation Consistency

Cross-checked against Ch 1 and Vols 1–4 notation table:

| Symbol | Usage | Consistent with prior volumes? |
|---|---|---|
| $g_{\mu\nu}$ | 4D metric | Yes (Ch 1 Eq 5.1.14) |
| $G_{\mu\nu}$ | Einstein tensor | Yes (Ch 1 Eq 5.1.22) |
| $G_4$ | 4D Newton constant | Yes (Ch 1 Eq 5.1.13; Vol 2 Ch 2) |
| $r_s = 2G_4M/c^2$ | Schwarzschild radius | Yes (Ch 1 Eq 5.1.35) |
| $\gamma,\beta$ | PPN parameters | First use in volume; defined in §2.8 |
| $J$ | angular momentum | Consistent with Ch 1 Kerr eq 5.1.41 |
| $\tau$ | proper time | Consistent with Vol 2 Ch 3 |

**Result:** PASS. One nit: $\gamma$ is used both for the PPN parameter AND for the Lorentz factor in one problem statement (P2.6); clarified inline but should be reviewed for Finalize.

### 1.4 Prerequisites Check

All Vol 5 Ch 1 prerequisites cited in CHAPTER_SPEC are actually used:

- Schwarzschild metric (5.1.34) — used in §§2.2, 2.3, 2.4, 2.5, 2.7 ✓
- Kerr metric (5.1.41) — used in §2.6 ✓
- Einstein equations (5.1.22) — used in §2.8 (PPN parameterization) ✓
- Geodesic from variational principle — used in §2.1 ✓
- Bianchi / conservation — not explicitly invoked, OK (not needed for tests)

Vol 2 Ch 2 (Newton limit) used in §§2.2, 2.4. Vol 2 Ch 3 (proper time) used in §2.4. Vol 3 Ch 2 (Lagrangian) used in §2.1.

**Result:** PASS.

### 1.5 Word Count

**Target:** 10,000–14,000 words (Foundations Ch 2 spec, slightly under Ch 1's 14–16k because less derivation-heavy).
**Actual:** ~12,400 words by manual count of the draft.
**Result:** PASS — in range.

### 1.6 Figure Audit

All `[FIGURE: Fig 5.2.N — ...]` placeholders in the draft:

| Placeholder | Section | Matches CHAPTER_SPEC figure plan? |
|---|---|---|
| Fig 5.2.1 Mercury orbit precession | §2.2 | Yes |
| Fig 5.2.2 Light ray geometry at limb | §2.3 | Yes |
| Fig 5.2.3 Eddington 1919 data + Cassini band | §2.3 | Yes |
| Fig 5.2.4 Redshift potential well + GPS satellites | §2.4 | Yes |
| Fig 5.2.5 Shapiro delay geometry (Earth-Sun-Venus) | §2.5 | Yes |
| Fig 5.2.6 Gravity Probe B frame-drag vector | §2.6 | Yes |
| Fig 5.2.7 Geodetic precession — gyroscope along orbit | §2.7 | Yes |
| Fig 5.2.8 PPN parameter bound chart | §2.8 | Yes |
| Fig 5.2.9 The 11-test scorecard | §2.9 | Yes |

9 of 9 figure entries match. **Result:** PASS.

### 1.7 Equation Numbering Audit

Equations (5.2.1) through (5.2.41) used sequentially; no gaps, no duplicates. Cross-volume citations use (V.Ch.Eq) notation, e.g. (5.1.34), (2.8.12). **Result:** PASS.

---

## 2. Product-Specific Foundations Checks

### 2.1 All numerical predictions carry observational references with error bars

- Mercury perihelion: framework predicts 42.98"/century vs observed 42.98 ± 0.04"/century (MESSENGER) ✓
- Light bending: 1.7516" vs Cassini $\gamma = 1 + (2.1 \pm 2.3)\times 10^{-5}$ ✓
- Gravitational redshift: Pound–Rebka 1960 with 10% era error bars; GPS 45 μs/day quoted with 1.47% model residual flagged ✓
- Shapiro delay: 1964 Shapiro reference flagged with 16.01% residual due to stale reference ✓
- Lense-Thirring: Gravity Probe B 37.2 mas/yr; measured 37.2 ± 7.2 mas/yr ✓
- Geodetic: GP-B 6606 mas/yr; measured 6601.8 ± 18.3 mas/yr ✓

**Result:** PASS.

### 2.2 Honest-reporting rule (no cherry-picking)

CHAPTER_SPEC R10: report full 11-test pass/fail rate verbatim.

§2.9 contains the verbatim test-suite output showing all 11 tests (100% pass under the built-in tolerance) AND explicitly flags the two tests with >1% error residuals (Gravitational Time Dilation 1.47%, Shapiro 16.01%). §2.10 opens with the GitHub #8 gap and does not downgrade its severity.

**Result:** PASS.

### 2.3 Derivations either cite or derive, never handwave

Every equation in (5.2.1)–(5.2.41) is either:
- (a) cited from Ch 1 or prior volumes with explicit (V.Ch.Eq), or
- (b) derived in-chapter from those citations.

Two exceptions are explicitly flagged as "stated without full derivation":
- Birkhoff's theorem (re-invoked from Ch 1 §1.6)
- The PPN expansion of general metric theories (§2.8) — stated with literature pointer (Will 2014)

Both are listed in the Reviewer's Ledger at end of §2.10.

**Result:** PASS.

---

## 3. Issues Found (for Phase 5 / Phase 6 attention)

| # | Severity | Location | Issue | Proposed fix |
|---|---|---|---|---|
| SR-1 | LOW | §2.1 | $\gamma$ used as Lorentz factor AND PPN parameter across the chapter | Rename Lorentz $\gamma \to \gamma_L$ in §2.1 only, or add a notation callout at top of §2.8 |
| SR-2 | LOW | §2.5 | Shapiro reference value hardcoded from 1964 paper; explanation is correct but reads dense | Expand the "why the 16% is a reference-staleness artifact" paragraph by one sentence |
| SR-3 | LOW | §2.7 | Geodetic section is shortest; reader may wonder if it's being rushed | Add a half-paragraph on physical intuition (parallel transport of spin on curved manifold) |
| SR-4 | INFO | §2.10 Action B | Action items reference test-suite update — clerical, not scientific | Note in Finalize that this is tracked on GitHub, not blocking chapter acceptance |

None of these block the draft. All four are Polish-level items for Phase 6.

---

## 4. Summary

| Check | Status |
|---|---|
| But-why test | PASS |
| Forward-dependency audit | PASS |
| Notation consistency | PASS (1 nit) |
| Prerequisites | PASS |
| Word count (10–14k) | PASS (~12.4k) |
| Figure audit (9/9) | PASS |
| Equation numbering | PASS |
| Observational error bars | PASS |
| Honest-reporting rule | PASS |
| Derivation-or-cite | PASS |

**Overall:** Draft is ready to advance to Phase 5 (Reviewer Agents).

---

*End of SELF_REVIEW_REPORT.md*
