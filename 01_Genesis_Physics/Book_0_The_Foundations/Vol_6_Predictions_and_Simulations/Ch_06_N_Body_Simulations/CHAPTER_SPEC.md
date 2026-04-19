# Chapter Specification: Vol 6, Chapter 6 — N-Body Simulations with Zone Corrections

**Product:** Foundations (Book 0), Volume 6: Predictions, Simulations, and Open Problems
**Chapter:** 6
**Working Title:** N-Body Simulations with Zone Corrections
**Status:** SPEC COMPLETE
**Date:** 2026-04-11

---

## Mission

Present the complete N-body simulation results for cosmic structure formation under zone-architecture corrections — growth factors, power spectra, halo mass functions, and density contrast evolution — compared head-to-head with standard ΛCDM, so that a graduate student can reproduce every result on a laptop and a skeptical physicist can evaluate whether the differences are physically meaningful and observationally testable.

---

## Requirements Traceability

| Req ID | Chapter Requirement | Traces To | Status |
|--------|-------------------|-----------|--------|
| Ch06-001 | Present all structure_formation.py simulation results with actual numerical output | V6-002 | NOT MET |
| Ch06-002 | Side-by-side comparison of Genesis Physics vs ΛCDM: growth factor, power spectrum, halo mass function | V6-006 | NOT MET |
| Ch06-003 | Convergence tests demonstrating numerical reliability | V6-002 | NOT MET |
| Ch06-004 | Resolution studies (N_a convergence) with quantified numerical error | V6-002 | NOT MET |
| Ch06-005 | Comparison with survey data (SDSS, DES) — what's validated, what's projected | V6-006 | NOT MET |
| Ch06-006 | Exact commands to reproduce every result | V6-002 | NOT MET |
| Ch06-007 | Honest assessment of what's validated vs. what needs more resolution (GitHub #20) | V6-003 | NOT MET |
| Ch06-008 | Scale-dependent signatures identifiable by current/next-gen surveys | V6-001 | NOT MET |

---

## Prerequisites

| Concept | Established In |
|---------|---------------|
| Waters Field Equations (dimensionless form) | Vol 1, Ch 6; Vol 2, Ch 3 |
| Cosmological perturbation theory with zone corrections | Vol 5, Ch 6 |
| Modified Friedmann equation with Waters contributions | Vol 5, Ch 4 |
| Simulation methodology (finite differences, convergence, validation) | Vol 6, Ch 5 |
| Dimensionless formulation and CFL condition | Vol 6, Ch 5, §5.3–5.4 |
| Prediction catalog: cosmological predictions P-046 through P-067 | Vol 6, Ch 1–3 |
| Falsification criteria for structure formation predictions | Vol 6, Ch 4 |

---

## "Why" Chain

1. **Why simulate structure formation at all?** — Because the linear perturbation theory of Vol 5 breaks down at late times and small scales. Simulations bridge the gap between analytical predictions and observable galaxy surveys.
2. **Why N-body (particle-mesh) rather than solving PDEs directly?** — The structure_formation.py code uses a semi-analytical approach (growth factor integration + Press-Schechter) rather than full N-body. This is honest: it's the current state of the code. Full particle-mesh N-body is an open problem (Section 6.7).
3. **Why does zone architecture differ from ΛCDM?** — Waters Below (Ψ_B ∝ a⁻³) enhances growth at large scales; Waters Above (Ψ_A ∝ a⁻⁴) suppresses growth at small scales. The combined effect is a scale-dependent modification to the matter power spectrum.
4. **Why should we trust these results?** — Convergence tests show the growth factor ratio D_GP/D_LCDM converges as temporal resolution increases (N_a: 25→200), and the code reproduces known ΛCDM behavior when zone corrections are turned off.
5. **Why compare with SDSS and DES specifically?** — These surveys provide the most precise measurements of the galaxy power spectrum and halo mass function at the scales where zone corrections produce measurable (~2–13%) deviations.
6. **Why is this chapter honest about limitations?** — GitHub #20 flags N-body dynamics completeness as a MEDIUM gap. The current code uses linear perturbation theory, not full nonlinear N-body. This must be stated clearly so readers know what's validated (linear regime, k < 0.1 Mpc⁻¹) and what's projected (nonlinear regime, k > 1 Mpc⁻¹).

---

## Key Deliverables

### Simulation Results (from actual runs)

| # | Result | Source | Actual Value |
|---|--------|--------|-------------|
| 1 | Growth factor ratio D_GP/D_LCDM at z=0 | structure_formation.py | 0.9881 (N_a=50) |
| 2 | Power spectrum ratio at k=0.01 (large scales) | structure_formation.py | ~0.878 at z=0 |
| 3 | Power spectrum ratio at k=10 (small scales) | structure_formation.py | ~0.867 at z=0 |
| 4 | Convergence of D_GP/D_LCDM with N_a | Convergence test | 0.978→0.988→0.994→0.997 |
| 5 | Halo mass function comparison | structure_formation.py | GP suppressed relative to ΛCDM |

### Figures (6 planned)

| Fig ID | Title | Type | Placement | What It Shows | Why It's Needed | Key Labels | Complexity |
|--------|-------|------|-----------|---------------|----------------|------------|-----------|
| Fig 6.6.1 | Growth Factor Comparison | Plot | §6.2 | D(z)/D(0) for ΛCDM vs Genesis Physics | The primary observable difference — must be visualized | D(z), z, model labels | Medium |
| Fig 6.6.2 | Power Spectrum Evolution | Plot | §6.3 | P(k) at z=0, 1, 10 for both models | Shows scale-dependent and redshift-dependent differences | k, P(k), z labels | Medium |
| Fig 6.6.3 | Power Spectrum Ratio | Plot | §6.3 | P_GP(k)/P_LCDM(k) at multiple redshifts | The key diagnostic — where do models diverge? | k, ratio, unity line | Medium |
| Fig 6.6.4 | Halo Mass Function | Plot | §6.4 | dn/dM for both models at z=0 | Tests halo abundance predictions | M_sun, dn/dM | Medium |
| Fig 6.6.5 | Convergence Study | Plot | §6.5 | D_GP/D_LCDM vs N_a (temporal resolution) | Demonstrates numerical trustworthiness | N_a, ratio, converged value | Simple |
| Fig 6.6.6 | Survey Comparison Schematic | Diagram | §6.6 | SDSS/DES measurement precision overlaid on predicted differences | Shows which scales are currently testable | k ranges, σ_P/P, survey labels | Complex |

### Problem Sets

| Difficulty | Count | Topics Covered |
|-----------|-------|---------------|
| Computational | 2 | Run the simulation and reproduce growth factor table; vary α_A, α_B |
| Conceptual | 2 | Why scale-dependent? Why do models converge at high z? |
| Challenge | 2 | Implement RK4 time integrator; add baryonic acoustic oscillation feature |

---

## Verification Criteria

### Universal
- [ ] "But why?" test — every result has physical motivation
- [ ] No forward dependencies — nothing from Ch 7–12 used here
- [ ] Notation consistent with Vol 1 Appendix B and Ch 5
- [ ] All code references match actual filenames in Research/Simulations/
- [ ] Word count: 8,000–15,000
- [ ] All simulation results are ACTUAL outputs, not claimed

### Product-Specific (Foundations)
- [ ] Every equation numbered
- [ ] Key results boxed
- [ ] Problem sets: computational → conceptual → challenge
- [ ] Exact reproduction commands provided for every result
- [ ] Known gap (GitHub #20) honestly disclosed

---

## Assigned Reviewers

| Reviewer | Assigned? | Status | Date |
|----------|-----------|--------|------|
| The Physicist | YES | — | — |
| But Why? Reader | YES | — | — |
| Writing Coach | YES | — | — |
| Consistency Auditor | YES | — | — |
| Homeschool Mom | NO | — | — |
| The Skeptic | YES | — | — |
| The Student | YES | — | — |
| Style Editor | YES | — | — |
| The Theologian | NO | — | — |
| The Navigator | YES | — | — |

---

## Notes

- **CRITICAL HONESTY NOTE:** The simulation is semi-analytical (linear perturbation theory + Press-Schechter), NOT a full particle-mesh N-body code. The chapter title "N-Body Simulations" must be contextualized: this is the *framework* for N-body with zone corrections, validated in the linear regime. Full nonlinear N-body is an open problem.
- **GitHub #20:** N-body dynamics completeness flagged as MEDIUM gap. Chapter must explicitly state what additional resolution/methods are needed.
- **Power spectrum ratio shows ~12-13% suppression** across all scales at z=0, not the ~2-8% range reported in SIMULATION_RESULTS.md. The actual simulation output is the ground truth; the chapter reports actual results.
- **Convergence with N_a** shows the growth factor ratio approaches 1.0 as resolution increases, suggesting the ~1.2% difference at N_a=50 is partly a numerical artifact of the Euler integrator's step size.

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-11 | Initial spec created | Ch 6 writing sprint |
