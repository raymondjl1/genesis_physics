# Chapter Specification: Vol 6, Chapter 5 — Simulation Methodology

**Product:** Foundations (Book 0), Volume 6: Predictions, Simulations, and Open Problems
**Chapter:** 5
**Working Title:** Simulation Methodology
**Status:** SPEC COMPLETE
**Date:** 2026-04-11

---

## Mission

Establish the complete computational framework — numerical methods, convergence criteria, error estimation, parallelization strategy, and validation methodology — that underpins every simulation result in Chapters 6–8, so that a graduate student can set up the environment, run every simulation, and trust the results.

---

## Requirements Traceability

| Req ID | Requirement | How This Chapter Addresses It | Status |
|--------|------------|-------------------------------|--------|
| V6-002 | All simulations reproducible | Full environment setup, dependency list, exact commands, verification cases | ADDRESSED |
| V6-006 | Comparison with standard physics is scrupulously fair | Validation against known analytical solutions; honest error reporting | ADDRESSED |
| WHY-* | Every concept explains WHY | Each numerical method choice explained with physical/mathematical motivation | ADDRESSED |
| MATH-* | Mathematical rigor | Convergence proofs, order-of-accuracy demonstrations, error bounds | ADDRESSED |

---

## Prerequisites

The reader must already know:

| Concept | Source |
|---------|--------|
| Waters Field Equations (dimensionless form) | Vol 1, Ch 6; Vol 2, Ch 3 |
| Membrane wave equation and boundary conditions | Vol 1, Ch 5, Eqs (1.5.12)–(1.5.18) |
| Zone manifold structure | Vol 1, Ch 3 |
| Prediction catalog (P-001 through P-088) | Vol 6, Ch 1–4 |
| Linear perturbation theory basics | Vol 5, Ch 6 |
| Basic numerical methods (finite differences, eigenvalue problems) | Standard graduate coursework |

---

## "Why" Chain

This chapter answers the following "but why?" questions:

1. **Why these numerical methods?** — The Waters Field Equations are coupled nonlinear PDEs spanning 41 orders of magnitude in length scale. Finite differences with dimensionless formulation are the simplest scheme that handles this range while maintaining O(Δx²) accuracy.
2. **Why dimensionless variables?** — Physical scales range from η_B ≈ 10⁻¹⁵ m to ξ_A ≈ 10²⁶ m. Without normalization, floating-point arithmetic fails catastrophically.
3. **Why explicit Euler (and when not)?** — Simplicity and transparency for weak-coupling regime. Semi-implicit methods are needed for strong coupling or long integrations.
4. **Why these convergence criteria?** — The grid convergence study (64→128→256) demonstrates O(Δx²) convergence — the expected order for second-order centered differences. This is the minimum standard for publishable computational physics.
5. **Why trust the code?** — Validation against analytical solutions (1D string eigenfrequencies, Bessel function zeros), energy conservation tracking, and convergence studies. The method of manufactured solutions provides additional confidence.
6. **Why Python?** — Reproducibility, accessibility, and the NumPy/SciPy ecosystem. GPU acceleration (CuPy/JAX) available for production runs.

---

## Key Deliverables

### Derivation Plan

| Starting Point | Result | Equation Numbers |
|---------------|--------|-----------------|
| Waters Field Equations (dimensional) | Dimensionless formulation | Eq (6.5.1)–(6.5.4) |
| Dimensionless PDEs | Finite difference discretization | Eq (6.5.5)–(6.5.8) |
| Discrete equations | Stability analysis (CFL condition) | Eq (6.5.9) |
| Eigenvalue problem K φ = λ M φ | Membrane spectrum numerical method | Eq (6.5.10)–(6.5.12) |
| Grid refinement study | Convergence order demonstration | Eq (6.5.13) |
| Error propagation analysis | Uncertainty quantification | Eq (6.5.14)–(6.5.15) |

### Figures (4 planned)

| Figure ID | Title | Type | Placement | What It Shows | Why Needed |
|-----------|-------|------|-----------|--------------|------------|
| Fig 6.5.1 | Simulation Architecture Overview | Flowchart | §5.2 | Three simulation modules, their inputs, outputs, and interdependencies | Reader needs the big picture before details |
| Fig 6.5.2 | Dimensionless Variable Scaling | Schematic | §5.3 | Physical scales mapped to O(1) computational domain | The 41-order-of-magnitude span is the core challenge — must be visualized |
| Fig 6.5.3 | Grid Convergence Study | Plot | §5.6 | Final energy vs. grid resolution (64, 128, 256) with O(Δx²) reference line | Demonstrates numerical trustworthiness — the "proof the code works" |
| Fig 6.5.4 | Validation Methodology Flowchart | Flowchart | §5.7 | Four-layer validation: analytical benchmarks → convergence → conservation → cross-code comparison | Shows the reader how trust is established systematically |

### Problem Sets

1. (Computational) Set up the simulation environment and reproduce the 1D equilibrium test. Compare your energy to Table 6.5.1.
2. (Computational) Run the grid convergence study with nx = 32, 64, 128, 256, 512. Plot the convergence rate and verify O(Δx²).
3. (Conceptual) Why does the CFL condition for the Waters field solver differ from a standard wave equation? What physical quantity sets the wave speed?
4. (Conceptual) Explain why periodic boundary conditions are more numerically stable than Dirichlet for the coupled field evolution. Under what physical conditions would Dirichlet be more appropriate?
5. (Challenge) Implement the Crank-Nicolson time integrator for the 1D Waters field solver. Compare energy conservation with explicit Euler over 1000 time steps. What improvement do you observe?
6. (Challenge) Derive the modified CFL condition when the coupling constant G_int is not small. At what value of G_int does explicit Euler become unconditionally unstable?

---

## Verification Criteria

### Universal
- [ ] "But why?" test — every numerical choice has its reason
- [ ] No forward dependencies — nothing from Ch 6–8 used here
- [ ] Notation consistent with Vol 1 Appendix B and Symbol_and_Constants.md
- [ ] All code references match actual filenames in Research/Simulations/
- [ ] Word count: 8,000–15,000

### Product-Specific (Foundations)
- [ ] Every equation numbered
- [ ] Key results boxed
- [ ] Problem sets: computational → conceptual → challenge
- [ ] A Student can set up the environment and run simulations after reading this chapter

---

## Assigned Reviewers

| Reviewer | Critical Check for This Chapter |
|----------|-------------------------------|
| The Physicist | Are numerical methods mathematically justified? Convergence proofs real? |
| The "But Why?" Reader | Does every method choice explain WHY this approach? |
| The Writing Coach | Technical chapters risk being dry — keep it alive and motivated |
| The Consistency Auditor | Code references match actual files; notation matches series |
| The Skeptic | Would a skeptic trust these simulations? Is validation methodology rigorous? |
| The Student | Can they actually set up the environment and run the code? |
| The Style Editor | Formatting, equation numbering, code block style |
| The Theologian | N/A for this chapter (no theological content) |
| The Navigator | Does this chapter properly serve Ch 6–8? Series coherence? |
