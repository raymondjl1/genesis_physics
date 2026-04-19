---
product: Foundations Vol 4 — The Quantum World
chapter: 8
title: Renormalization in Zone Architecture
status: SPEC
created: 2026-04-08
---

# Chapter 8: Renormalization in Zone Architecture — Specification

## Mission

Chapter 7 derived Feynman diagrams and computed QED processes, but every loop integral diverged at large momentum. This chapter explains why those divergences appear, why they do not threaten physical predictions, and why in zone architecture the ultraviolet cutoff is not arbitrary but physical — set by the finite thickness of the Firmament. The reader will understand that renormalization is not a mathematical trick but a consequence of a finite-sized medium.

---

## Requirements

| Req ID | Chapter Requirement | Traces To | Status |
|--------|-------------------|-----------|--------|
| Ch8-001 | Motivate renormalization from divergent loop integrals in Ch 7 | V4-RENORMALIZATION | NOT MET |
| Ch8-002 | Introduce the ultraviolet (UV) divergence problem: what happens when you integrate a loop to ∞ | V4-RENORMALIZATION | NOT MET |
| Ch8-003 | Explain regularization procedures: cutoff, dimensional regularization, Pauli-Villars (sketch all three) | V4-RENORMALIZATION | NOT MET |
| Ch8-004 | Explain why regularization is needed: makes divergences explicit so we can subtract them | V4-RENORMALIZATION | NOT MET |
| Ch8-005 | Introduce the renormalization group (RG): the flow of coupling constants with energy scale Q | V4-RENORMALIZATION | NOT MET |
| Ch8-006 | Derive or clearly state the beta function β_i = dα_i/d(ln Q) for at least one coupling (electromagnetic preferred) | V4-RENORMALIZATION | NOT MET |
| Ch8-007 | Explain running couplings: α(Q) changes with the energy scale probed in an experiment | V4-RENORMALIZATION | NOT MET |
| Ch8-008 | State the known gap (MEDIUM severity, GitHub #26): RG flow analysis is only partial — what is derived from zone axioms vs. what is estimated or conjectured | V4-GAP-HONESTY | NOT MET |
| Ch8-009 | Show explicitly: in zone architecture, the UV cutoff Λ_zone = ℏc/η_B is PHYSICAL, not arbitrary | V4-CUTOFF-PHYSICAL | NOT MET |
| Ch8-010 | Derive or state with clear precision flags: at least one loop integral that is divergent without cutoff but finite with Λ_zone | V4-CUTOFF-APPLICATION | NOT MET |
| Ch8-011 | Show what is calculated vs. what is estimated: a table distinguishing rigorous zone-architecture results, leading-order estimates, and open problems | V4-HONESTY | NOT MET |
| Ch8-012 | Compare predictions (running of α_EM, α_s, Weinberg angle) with experimental measurements where available; give honest error bars | V4-PRECISION | NOT MET |
| Ch8-013 | Philosophical punchline: because the cutoff is physical, the theory has NO ambiguity in "bare parameters" — the bare theory is well-defined | V4-CONCEPTUAL | NOT MET |
| Ch8-014 | Flag the GitHub #26 gap in the chapter body (not just the spec) as an explicit Open Problem 8.X; do not hand-wave around missing RG flow coefficients | V4-GAP-HONESTY | NOT MET |
| Ch8-015 | Provide problem sets spanning computational (evaluate a loop with cutoff), conceptual (why does the cutoff matter?), and challenge (dimensional regularization equivalence) | V4-PROBLEMS | NOT MET |

---

## Prerequisites

| Concept | Established In |
|---------|---------------|
| Feynman diagrams and Feynman rules for zone architecture | Vol 4 Ch 7 |
| Loop integrals and their ultraviolet behavior | Vol 4 Ch 7 §7.8–7.11 |
| Interaction picture and Dyson series | Vol 4 Ch 7 §7.2–7.3 |
| The membrane (Firmament) and its thickness η_B | Vol 1 Ch 5 |
| Dimensional analysis and scaling laws | Vol 3 Ch 1 |
| Fine structure constant α and its origin in 6D geometry | Vol 2 Ch 3, cited in Vol 4 Ch 1 |
| Running couplings at the heuristic level (reference Vol 2 Ch 10, or provide brief overview) | Vol 2 Ch 10 (foundation document) |

---

## "Why" Chain

1. **Why do loop integrals diverge in the first place?** — Because we integrate the loop momentum k to ∞, and the integrand falls off slowly (logarithmically or slower). In an infinite medium with no high-energy cutoff, this integral diverges. The answer is: they diverge because we've assumed an infinitely divisible spacetime. The Firmament is finite.

2. **Why can we trust finite predictions if the divergences are infinite?** — Because renormalization is not a trick: the divergent parts depend only on the cutoff (or the regularization scheme), while the finite parts are *cutoff-independent* and represent the observable physics. Once we separate them, predictions are unambiguous.

3. **Why is the cutoff physical in Genesis Physics and not just a mathematical artifact?** — Because η_B, the thickness of the membrane into the Waters Below, is a real physical length. Modes with wavelength shorter than η_B do not fit on the membrane. The cutoff Λ_zone = ℏc/η_B is not a choice; it is a property of the medium.

4. **How do coupling constants "run" with energy, and why?** — Because at different energy scales Q, we are resolving different subsets of the quantum modes available in the 6D zone architecture. Low-Q experiments see only the low-lying Kaluza-Klein modes and measure an "effective" low-energy coupling. High-Q experiments resolve more modes and measure a "bare" high-energy coupling. The running is the smooth interpolation between these regimes.

5. **What precision limits exist, and where?** — The RG flow analysis in zone architecture is only partial (GitHub #26). We have the one-loop beta function; higher-loop coefficients are either estimated or depend on detailed numerical integration of the 6D membrane spectrum. Honest error bars are necessary.

6. **Why does unification happen, and does zone architecture predict it?** — The three gauge couplings (electromagnetic, weak, strong) converge at high energy (E_GUT ≈ 10¹⁶ GeV) because they are all manifestations of the single zone-interaction strength at the membrane scale. The merging of couplings is a prediction of the geometric origin of gauge symmetries.

---

## Key Deliverables

### Derivations (Foundations Vol 4, Chapter 8)

| # | Derivation | Starting Point | Result | Equations |
|---|-----------|---------------|--------|-----------|
| 1 | Divergent loop integral (worked example) | Coulomb photon exchange loop from Ch 7 | Logarithmic divergence at large k; result → ∞ without cutoff | (4.8.1)–(4.8.10) |
| 2 | Regularization by sharp cutoff | Same loop integral with upper limit Λ | Integral becomes finite; logarithm of Λ appears | (4.8.11)–(4.8.18) |
| 3 | Relation of Λ to zone parameters | Membrane thickness η_B and membrane scale | Λ_zone = ℏc/η_B; numerical value ~2.4×10¹⁹ GeV | (4.8.19)–(4.8.22) |
| 4 | One-loop beta function for α_EM | Loop integral for vacuum polarization | β_α = (α²/3π); running: α(Q) = α(Q₀)/(1 - (α/3π) ln(Q/Q₀)) | (4.8.23)–(4.8.35) |
| 5 | Running coupling at arbitrary energy | Beta function integrated | α(Q) as a function of Q from μ to Planck scale | (4.8.36)–(4.8.42) |
| 6 | Counterterms and minimal subtraction | Divergent part separated from finite part | δm, δZ, δλ defined; separation is scheme-dependent but physics is universal | (4.8.43)–(4.8.52) |
| 7 | Renormalizability statement (outline) | Beta function structure | All observable quantities depend only on finite parts; theory is renormalizable at one loop; higher loops conjectured (OPEN PROBLEM 8.2) | (4.8.53)–(4.8.58) |

### Figures and Diagrams

| Fig ID | Title | Type | Placement | What It Shows | Why It's Needed | Key Labels | Equations Referenced | Complexity |
|--------|-------|------|-----------|---------------|----------------|------------|---------------------|-----------|
| Fig 4.8.1 | Loop Integral Divergence: k→∞ Behavior | Plot | §8.1 | Integrand d⁴k/(k²-m²+iε)² as function of k, showing log divergence at large k, no natural cutoff | Visualizes the problem: why does integrating to ∞ give ∞? | k (log scale), integrand, log divergence, no cutoff | (4.8.5)–(4.8.10) | Medium |
| Fig 4.8.2 | Three Regularization Schemes | Comparison | §8.2 | Three panels: (a) hard cutoff Λ; (b) dimensional regularization in d=4-2ε dimensions; (c) Pauli-Villars heavy propagators. All achieve the same end: make divergence explicit and finite. | Shows that divergences appear in all schemes but physics is independent of scheme choice. | Λ, ε, Pauli masses M, d, log divergence | (4.8.11)–(4.8.20) | Medium |
| Fig 4.8.3 | The Membrane Cutoff Λ_zone in 6D | Schematic | §8.3 | The Firmament (2D membrane) in 6D spacetime, with thickness η_B into ξ and η directions. Wavefunctions at scales shorter than η_B do not fit. Dashed line at ℏc/η_B marks Λ_zone. | Explains that the cutoff is *not* arbitrary: it comes from the physical size of the medium. | Firmament, Waters Above, Waters Below, η_B, λ < η_B shaded as forbidden, Λ_zone marked | (4.8.19)–(4.8.22) | Complex |
| Fig 4.8.4 | Divergent Integral with Hard Cutoff | Plot | §8.3 | Integrand of Ch 7 vertex loop: the logarithmic rise stops abruptly at Λ_zone. Compare integrated result with and without cutoff: ∞ vs. finite number. | Concrete visual: finite cutoff → finite integral. | Integrand, Λ_zone barrier, log curve, finite area below cutoff, ∞ tail if extended | (4.8.11)–(4.8.18) | Medium |
| Fig 4.8.5 | Running Coupling α(Q) from Low to High Energy | Plot | §8.5 | Curve of α_EM(Q) vs. log(Q), starting at α(m_e c) ≈ 1/137, rising smoothly as Q increases, diverging as Q → Λ_zone. Experimental points overlaid (photon-photon scattering at CERN, etc.). | Shows that coupling is not constant; it is a function of energy scale probed. | α (vertical), Q (log scale), m_e, Z mass, W mass, E_Planck, experimental points | (4.8.36)–(4.8.42) | Medium |
| Fig 4.8.6 | Coupling Unification in the GUT Limit | Plot | §8.7 | Three running-coupling curves: α₁ (EM), α₂ (weak), α₃ (strong), all starting at different low-energy values, converging near E_GUT ≈ 10¹⁶ GeV where they become the single zone-interaction strength. | Demonstrates that the three gauge symmetries are manifestations of one underlying interaction at the membrane scale. | α₁, α₂, α₃ (legend), Q (log), E_GUT marked, convergence point | (4.8.59)–(4.8.62) [discussion section] | Medium |
| Fig 4.8.7 | Renormalization: Divergent vs. Finite Parts | Diagram | §8.6 | A Feynman diagram loop integral written as: [divergent part ∝ log Λ] + [finite part ∝ physical quantity]. Visual separation showing divergence goes into counterterm, finite part is the observable. | Makes concrete: divergence is not physics, it is a book-keeping artifact that we absorb into the bare parameters. | Integrand, divergent region, finite region, counterterm δ, observable | (4.8.43)–(4.8.52) | Medium |
| Fig 4.8.8 | Precision Table: What is Calculated vs. Estimated | Table | §8.8 | Four-column table: (1) Result/quantity; (2) Level (derived from zone axioms / estimated / conjectured); (3) Precision / error bars; (4) Open problem link if applicable. Rows: one-loop β function, two-loop, Λ_zone, coupling convergence, renormalizability at all orders. | Explicitly addresses the Skeptic reviewer: this is what we know, what we think we know, what remains open. | Result name, Level (checkmarks or crosses), %error, Issue # | (4.8.53)–(4.8.58) | Complex |

### Problem Sets (Foundations)

| Difficulty | Count | Topics Covered |
|-----------|-------|---------------|
| Computational | 3 | (1) Evaluate the logarithmically divergent loop integral ∫d⁴k/(k²-m²+iε)² with hard cutoff Λ; report the result and compare with and without cutoff. (2) Use the one-loop running formula α(Q) = α(Q₀)/(1 - (α/3π) ln(Q/Q₀)) to compute α_EM at the Z boson mass scale (Q = 91.2 GeV) given α(m_e c) ≈ 1/137. (3) Plot the running coupling α_EM(Q) from Q = 1 MeV to Q = 10¹⁹ GeV and mark the experimental measurement points. |
| Conceptual | 3 | (1) Explain why the divergence of a loop integral depends on the regularization scheme, but the finite part — and hence any observable — does not. (2) Why is the cutoff Λ_zone = ℏc/η_B *not* a choice in Genesis Physics, unlike dimensional regularization which is a mathematical convenience? (3) The electromagnetic coupling α_EM increases with energy (inverse of fine structure constant decreases). The strong coupling α_s decreases. Why the opposite behavior, and what does it imply for unification? |
| Challenge | 2 | (1) Show that the one-loop beta function for α_EM, β_α = α²/(3π), leads to a running coupling that has a Landau pole (divergence) at some large energy Q_Landau. Compute Q_Landau numerically. Does this contradict the existence of Λ_zone? Explain. (2) In dimensional regularization (d=4-2ε), compute the divergent part of the Coulomb loop integral (Ch 7 §7.8) and verify that it gives the same log divergence in the limit ε→0 as the hard-cutoff calculation does in the limit Λ→∞. |

---

## Section Outline

### Section 1: Why Loop Integrals Diverge
- **Topic sentence:** When we compute multi-loop Feynman diagrams, we integrate over all possible momenta of internal particles, and if we integrate to ∞, we often get ∞.
- **"Why" entry point:** Chapter 7 computed loop integrals like the vertex correction and got divergences. Where do they come from?
- **Key content:** Concrete example from Ch 7 (vertex loop or self-energy). Show the integrand behavior at large k. Identify the divergence as logarithmic or worse. Explain that in Standard QFT, there is *no* high-k cutoff, so ∞ is unavoidable.
- **Exit condition:** Reader knows that divergences are a real problem unless we cut off the integral at some scale.

### Section 2: Regularization — Three Methods
- **Topic sentence:** To extract physics from divergent integrals, we introduce a cutoff (or regularization parameter) that makes the integral finite, allowing us to separate the divergence from the observable.
- **"Why" entry point:** How do we *define* a divergent integral? Mathematically, we need a cutoff.
- **Key content:** (1) Hard cutoff: Λ (simplest; relies on upper limit). (2) Dimensional regularization: d = 4 − 2ε (algebraic; standard in particle physics). (3) Pauli-Villars (historical; heavy propagators). Show that all three give the same divergent structure (e.g., ln Λ vs. 1/ε) and all produce the same finite parts.
- **Exit condition:** Reader understands that the choice of regularization is a *choice*, but the physics is independent of the choice.

### Section 3: The Physical Cutoff in Zone Architecture
- **Topic sentence:** In Genesis Physics, the cutoff is not arbitrary. The Firmament has a finite thickness η_B into the perpendicular (ξ, η) dimensions, so wavelengths shorter than η_B do not fit on the membrane.
- **"Why" entry point:** What sets the value of the cutoff Λ?
- **Key content:** Relation of wavelength to momentum: λ = ℏc/k. A mode with k > ℏc/η_B has λ < η_B and cannot exist. Therefore Λ_zone = ℏc/η_B is a *physical* cutoff, not a regularization choice. Numerical value: η_B ≈ 1.3×10⁻¹⁵ m → Λ_zone ≈ 2.4×10¹⁹ GeV. Compare with Planck scale (same order).
- **Exit condition:** Reader knows that in zone architecture the cutoff is *not arbitrary*; it is set by the membrane thickness.

### Section 4: A Worked Example — The Vertex Loop with Cutoff
- **Topic sentence:** Take the one-loop vertex correction from Ch 7 and compute it with the zone cutoff Λ_zone.
- **"Why" entry point:** How does the cutoff change the result of the Ch 7 calculation?
- **Key content:** Set up the vertex integral. Show the divergent behavior at large k. Apply the hard cutoff. Perform the k integration (details in appendix or outline the key steps). Extract the result: finite number plus log Λ term. Show that the log Λ term can be absorbed into a counterterm (charge renormalization). Show that the finite part (the anomalous magnetic moment) is unchanged.
- **Exit condition:** Reader has seen a concrete divergent integral become finite, and has seen how the divergence and the physics separate.

### Section 5: The Renormalization Group and Running Couplings
- **Topic sentence:** The coupling constant of a theory is not actually constant; it depends on the energy scale Q at which we probe it. This "running" is encoded in the renormalization group (RG).
- **"Why" entry point:** Chapter 7 computed α_EM as a number, but experiments at different energies measure different values. What's going on?
- **Key content:** Define the beta function β_i = dα_i / d(ln Q). Derive or state the one-loop beta function for α_EM: β_α = α²/(3π). Solve the differential equation to get the running coupling α(Q). Show that α increases (decreases in inverse) with energy: the fine structure constant is not ~1/137 everywhere, but only at low energy. At Z mass (91 GeV), it's closer to 1/128. The running comes from virtual loops (e.g., vacuum polarization for EM).
- **Exit condition:** Reader knows that coupling constants run, understands why (virtual loops screen or enhance the coupling), and can compute α at a different scale given α at a reference scale.

### Section 6: Counterterms and the Separation of Divergence from Physics
- **Topic sentence:** The divergent part of every loop integral can be absorbed into a "counterterm" — a redefinition of the bare coupling or mass — leaving a finite, observable result.
- **"Why" entry point:** We have divergences. Can we just subtract them and keep computing?
- **Key content:** Define the counterterms: δZ (wave function renormalization), δm (mass counterterm), δλ (coupling counterterm). Show that the divergence of each one-loop diagram depends only on the regularization (e.g., ln Λ). Show that once we subtract these divergences, all loop-corrected matrix elements are finite. Explain "minimal subtraction": we subtract exactly the divergent part, no more, no less.
- **Exit condition:** Reader understands that renormalization is a systematic procedure, not an ad-hoc trick, and that the observable physics is independent of the subtraction scheme.

### Section 7: Renormalizability and Higher Loops
- **Topic sentence:** The fact that one-loop divergences can be removed by finite counterterms is not an accident. In certain theories, including QED and the Standard Model, this pattern persists to all orders of perturbation theory.
- **"Why" entry point:** We showed one loop works. Does two loops? Three loops? All loops?
- **Key content:** State the renormalizability theorem (outline, not full proof): in a renormalizable theory, the counterterms determined at one loop suffice for all higher loops. Cite that QED is renormalizable at all orders (Dyson, Renard, etc.). **Flag the open problem:** in zone architecture, renormalizability at two loops and higher is not yet proven. The detailed 6D momentum structure of two-loop integrals in the zone architecture has not been fully computed. This is GitHub #26 (MEDIUM severity).
- **Exit condition:** Reader knows that renormalizability is a property of theories, that QED has it, and that zone architecture claims it but the proof is incomplete.

### Section 8: Honest Accounting — What is Calculated, Estimated, and Open
- **Topic sentence:** This section makes explicit: what results in this chapter come from rigorous zone-architecture derivations, what are leading-order estimates, and what are open problems.
- **"Why" entry point:** The Skeptic reviewer will want to know: how much of this is real physics, and how much is hand-waving?
- **Key content:** A table or list:
  - **Calculated from zone axioms**: (1) The existence of a physical cutoff Λ_zone = ℏc/η_B from the membrane thickness. (2) The form of the one-loop beta function β_α = α²/(3π) from vacuum polarization (virtual loop structure is universal). (3) The running coupling formula α(Q) = α(Q₀) / [1 - (α/3π) ln(Q/Q₀)].
  - **Estimated / Approximate**: (1) The numerical coefficient in the two-loop beta function (quoted from standard QED, not re-derived in zone architecture). (2) The coupling unification scale E_GUT ≈ 10¹⁶ GeV (depends on two-loop RG flow, which is partial).
  - **Conjectured / Open**: (1) Renormalizability at all orders in zone architecture (one-loop is proven, higher orders assumed but not verified). (2) Potential complications at the membrane scale Λ_zone: do new physics degrees of freedom emerge?
- **Exit condition:** Reader has a clear picture of the framework's precision and limitations.

### Section 9: Comparison with Experiment
- **Topic sentence:** The running couplings predicted by zone architecture must match the experimental measurements of coupling strengths at different energy scales.
- **"Why" entry point:** We have a theory. Does it work?
- **Key content:** Present experimental measurements:
  - α(m_e c) ≈ 1/137.036 (low-energy value from atomic physics)
  - α(M_Z ≈ 91.2 GeV) ≈ 1/127.9 (from Z production at LEP)
  - α_s(M_Z) ≈ 0.1184 (strong coupling at Z scale, from hadronic decays)
  - Compare with zone-architecture predictions using the running formulas. Show error bars: typically 1–2% for EM, ~3–5% for strong coupling.
  - Discuss sources of discrepancy: higher-loop terms, hadronic contributions (not yet fully derived in zone architecture), experimental uncertainties.
- **Exit condition:** Reader sees that the framework makes testable predictions and that they agree with experiment to within the limits of what has been computed.

### Section 10: Philosophical Punchline — Well-Defined Bare Parameters
- **Topic sentence:** Because the cutoff is physical, the "bare" (unrenormalized) parameters of the theory are well-defined, not arbitrary.
- **"Why" entry point:** In Standard QFT, the bare coupling and bare mass are mathematical infinities; renormalization is a sleight of hand. In zone architecture, it's different.
- **Key content:** In zone architecture, the "bare" values are the values at the membrane scale Q ~ Λ_zone. Above that scale, no more modes exist; there is no need for further renormalization. The finite-thickness membrane ensures that the theory has a natural high-energy completion. This is a feature, not a limitation: it explains why QFT works so well at accessible energies.
- **Exit condition:** Reader understands that zone architecture solves the "interpretation" problem of renormalization by making the cutoff physical.

### Section 11: Summary and Open Problems
- **Topic sentence:** Chapter 8 has explained the origin of loop divergences, shown how renormalization removes them, demonstrated that the cutoff is physical, and shown that couplings run with energy.
- **Content sketch:** Restate the four key tools (regularization, counterterms, beta functions, running couplings). Restate the physical cutoff Λ_zone. Restate the one-loop running formula. List the open problems: two-loop RG flow in zone architecture, renormalizability at all orders, emergence of physics at the membrane scale. Point forward to Ch 9 (Casimir effect, vacuum energy) and Ch 10–14 (Standard Model applications).
- **Exit condition:** Reader can proceed to Ch 9 understanding the renormalization framework.

---

## Verification Criteria

### Universal Criteria
- [ ] Every requirement in the table above is marked MET
- [ ] "But why?" chain — all 6 questions answered in the chapter text
- [ ] No forward dependencies except those explicitly flagged (Ch 9 for Casimir; Ch 10 for Standard Model applications)
- [ ] Notation consistent with Vol 1–4 Ch 1–7
- [ ] Word count within target range: 8,000–15,000 words
- [ ] All `[FIGURE: ...]` placeholders correspond to specs above
- [ ] All `[TODO]` markers resolved

### Product-Specific Criteria (Foundations Vol 4)
- [ ] Every derivation starts from a previously established equation with citation
- [ ] Every equation numbered (4.8.N), contiguous
- [ ] The worked example (loop integral with cutoff) is complete enough for a graduate student to reproduce
- [ ] The one-loop beta function is derived, not quoted (or if quoted, source cited explicitly)
- [ ] The running coupling formula is derived from the beta function
- [ ] The GitHub #26 gap is referenced in the chapter body as an explicit Open Problem 8.X (or 8.1, 8.2, etc.)
- [ ] The physical cutoff Λ_zone is explained as a property of η_B, not a regularization choice
- [ ] The "what is calculated vs. estimated vs. open" section is comprehensive and honest
- [ ] Experimental comparisons are made with error bars
- [ ] Voice is Feynman-textbook: pedagogical, honest about limits
- [ ] Problem sets span computational → conceptual → challenge

### Critical for Skeptic Reviewer
- [ ] No hand-waving around infinities: every divergence is explicitly shown and handled
- [ ] The cutoff derivation traces back to η_B (a real membrane thickness, not a math trick)
- [ ] Higher-loop RG flow is explicitly flagged as partial/open, not claimed as complete
- [ ] The section "what is calculated vs. estimated vs. open" is detailed and not glossed over
- [ ] Experimental agreement is presented with honest error bars and limitations

---

## Assigned Reviewers

| Reviewer | Assigned? | Status | Date |
|----------|-----------|--------|------|
| The Physicist | YES | — | — |
| But Why? Reader | YES | — | — |
| Writing Coach | YES | — | — |
| Consistency Auditor | YES | — | — |
| The Skeptic | YES | — | — |
| The Student | YES | — | — |
| The Style Editor | YES | — | — |
| The Theologian | YES | — | — |
| The Navigator | YES | — | — |

---

## Notes

- **Primary source**: `10-RUNNING_COUPLINGS_RG_FLOW.md` and `05-APPLIED_CALCULATIONS.md` for worked examples.
- **Direct foundation**: Vol 2 Ch 10 (running couplings — foundation document, not yet written). This chapter fills that gap for Vol 4 readers.
- **Load-bearing prior chapters**: Vol 4 Ch 7 (Feynman diagrams and divergences). Every derivation here starts from a Ch 7 result.
- **GitHub #26 criticality**: Running coupling constants precision is a MEDIUM-severity open problem. This chapter MUST disclose it and not hide it. The Skeptic will specifically check for hand-waving.
- **Skeptic hot button**: The UV cutoff. Explain explicitly and repeatedly that Λ_zone = ℏc/η_B is not a regularization trick but a physical property of the medium.
- **Student acceptance criterion**: The Student reviewer must be able to compute a running coupling at an arbitrary energy scale after reading this chapter.
- **Test suite**: `Research/Mathematical_Models/05_Quantum_Mechanics/test_qm_applied.py` should be run (may not directly test RG flow, but good for consistency check).

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-08 | Initial spec created | Beginning Phase 1 of Ch 8 chapter writing |

