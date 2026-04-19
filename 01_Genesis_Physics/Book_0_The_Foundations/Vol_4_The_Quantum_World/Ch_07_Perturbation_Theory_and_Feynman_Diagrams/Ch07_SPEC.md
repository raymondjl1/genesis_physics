---
product: Foundations Vol 4 — The Quantum World
chapter: 7
title: Perturbation Theory and Feynman Diagrams
status: SPEC
created: 2026-04-08
---

# Chapter 7: Perturbation Theory and Feynman Diagrams — Specification

## Mission

Chapter 6 built the free-field machinery: a Firmament whose displacement ψ̂(x,t) is an operator on a Fock space of non-interacting modes. Everything in that chapter is exact, because the free theory is exactly solvable. Nature, however, is not free. The Firmament carries vertices at which modes ring *into each other*, and those vertices are what give us the processes that motivated second quantization in the first place — pair production, radiative decay, scattering. This chapter is the systematic treatment of those interactions.

We develop time-dependent perturbation theory for the interacting Firmament: the interaction picture, the Dyson series, Wick's theorem, and the graphical bookkeeping of Feynman diagrams. From the Vol 2 Ch 5 brane Lagrangian and the Vol 2 Ch 6 gauge structure we extract a specific set of vertex rules for the zone architecture — rules that will be compiled into Appendix C of this volume. We then put those rules to work on the two precision tests that made QED credible: the electron anomalous magnetic moment $a_e$ and the Lamb shift in hydrogen. By the end of the chapter the reader should be able to draw a diagram, translate it into a complex number, and get numerical agreement with experiment to one part in $10^{10}$ — and should understand at every step *why* each of those moves is forced by the zone architecture.

---

## Requirements

| Req ID | Chapter Requirement | Traces To | Status |
|--------|-------------------|-----------|--------|
| Ch7-001 | Motivate perturbation theory from the impossibility of exactly solving the interacting Firmament | V4-QFT-FOUNDATIONS | NOT MET |
| Ch7-002 | Derive the interaction picture: split Ĥ = Ĥ₀ + Ĥ_int, evolve states with Ĥ_int and operators with Ĥ₀ | V4-QFT-DERIVATIONS | NOT MET |
| Ch7-003 | Derive the Dyson series for the time-evolution operator Û_I(t, t₀) and the time-ordered exponential expression | V4-QFT-DERIVATIONS | NOT MET |
| Ch7-004 | State and prove Wick's theorem: T-products as sums of normal-ordered products plus contractions | V4-QFT-DERIVATIONS | NOT MET |
| Ch7-005 | Identify contractions with the Firmament propagator and give it the explicit momentum-space form D_F(k) from Vol 2 Ch 5 | V4-QFT-DERIVATIONS | NOT MET |
| Ch7-006 | Introduce Feynman diagrams as the graphical bookkeeping of Wick contractions in the S-matrix expansion | V4-QFT-DERIVATIONS | NOT MET |
| Ch7-007 | Derive the Feynman rules for zone architecture: external lines, internal lines (propagators), vertices (from the brane Lagrangian), loop integration, and symmetry factors | V4-QFT-RULES | NOT MET |
| Ch7-008 | Organize the rules in a self-contained box and mark them as the source for Appendix C | V4-QFT-RULES | NOT MET |
| Ch7-009 | Apply the rules to compute the tree-level electron–photon vertex and recover Coulomb scattering | V4-QFT-APPLIED | NOT MET |
| Ch7-010 | Compute the one-loop vertex correction and extract the Schwinger term $a_e^{(1)} = \alpha/(2\pi)$ | V4-QED-PRECISION | NOT MET |
| Ch7-011 | Cite the higher-order corrections (α², α³, α⁴, α⁵, hadronic) and show the full numerical comparison $a_e^{\rm th} = 0.00115965218...$ vs $a_e^{\rm exp} = 0.00115965218081(11)$ | V4-QED-PRECISION | NOT MET |
| Ch7-012 | Compute the Lamb shift: identify the self-energy and vacuum-polarization contributions, recover $\Delta\nu = 1057.845$ MHz | V4-QED-PRECISION | NOT MET |
| Ch7-013 | Address UV divergences honestly: show how they arise, explain why the membrane thickness $\eta_B$ provides a *physical* cutoff, and flag Ch 8 as the chapter that treats renormalization systematically | V4-QFT-HONESTY | NOT MET |
| Ch7-014 | Respect the spin-1/2 BLOCKER: use the Dirac fermion structure as a *placeholder* for the eventual topological-defect derivation (Ch 10), and mark the dependency explicitly | V4-GAP-HONESTY | NOT MET |
| Ch7-015 | Provide problem sets spanning computational (diagram → amplitude), conceptual (why contractions?), and challenge (two-loop Schwinger coefficient, Uehling potential) | V4-PROBLEMS | NOT MET |

---

## Prerequisites

| Concept | Established In |
|---------|---------------|
| Zone manifold, Firmament, Waters | Vol 1 Ch 3, Ch 5, Ch 6 |
| Boundary-condition quantization and normal modes | Vol 1 Ch 10 |
| Fine structure constant α from 6D geometry | Vol 2 Ch 3 (and reference to FINE_STRUCTURE_DERIVATION.md) |
| Zone Lagrangian and canonical momentum | Vol 2 Ch 5 (eqs. 2.5.1–2.5.5) |
| Gauge symmetries and U(1)×SU(2)×SU(3) | Vol 2 Ch 6 |
| Running couplings at the heuristic level | Vol 2 Ch 10 |
| Schrödinger equation from membrane dynamics | Vol 4 Ch 2 |
| Second quantization, Fock space, creation/annihilation operators | Vol 4 Ch 6 |
| Free-field Hamiltonian Ĥ = Σ_k ℏω_k (N̂_k + 1/2) | Vol 4 Ch 6 (eq. 4.6.55) |
| One-excitation sector = single-particle QM | Vol 4 Ch 6 §6.7 |

---

## "Why" Chain

1. **Why do we need perturbation theory at all? Why not solve the interacting Firmament exactly?** — Because the interacting wave equation is nonlinear, and no closed-form solution exists for any physically realistic interaction term (the cubic and quartic couplings of the brane Lagrangian are specifically the terms we could not absorb into the free quadratic form in Ch 6). Whenever the interaction is small compared to the free dynamics — and on the Firmament, the dimensionless coupling α ≈ 1/137 is small — we can expand in powers of the interaction and compute observable quantities order by order. Perturbation theory is not a trick; it is the statement that *a small correction to a solvable problem can itself be solved by iteration*.

2. **Why the interaction picture and not the Schrödinger picture we used in Ch 2?** — Because the Schrödinger picture puts *all* of the time evolution on the state, and in an interacting theory with a vast Hilbert space that is numerically intractable. The interaction picture splits the labor: the operators carry the free evolution (which we already solved exactly in Ch 6), and the states carry only the extra wiggle induced by the interaction. The Dyson series then becomes a power series in the interaction Hamiltonian — and each term has a graphical interpretation.

3. **Why a *time-ordered* exponential? Why can't we just exponentiate ∫Ĥ_I dt?** — Because Ĥ_I(t) at different times in general does not commute with itself, and for noncommuting operators $e^{\int A(t) dt}$ is not the solution to $\dot{U} = -i A U$. Dyson's prescription — time order the product — is the correct generalization. It is exactly the same "one moment after another" logic that gave us the path integral in Ch 2, now written in operator form.

4. **Why Wick's theorem?** — Because the Dyson series is an integral over products of field operators at many different times, and to extract physical matrix elements we need to rearrange each product into a form where all annihilation operators sit to the right of all creation operators (so that acting on |0⟩ picks out the right part). Wick's theorem is the bookkeeping identity that turns a time-ordered product into a sum of normal-ordered products and contractions. Every contraction is a Firmament propagator. Every normal-ordered remainder matches external particles in the initial and final state. There are no other possibilities.

5. **Why is each contraction a propagator, and why is the propagator the same object no matter what interaction we put in?** — Because the propagator is a property of the *free* field — the vacuum expectation value of a time-ordered pair of field operators — and the free field is determined entirely by the Vol 2 Ch 5 quadratic Lagrangian. The interaction can be anything; the propagator is fixed by the kinetic term. This is why the same Firmament propagator D_F(k) will appear in every QED diagram, every electroweak diagram, every Standard Model diagram in Chapters 10–12.

6. **Why draw diagrams at all? Couldn't we just write the integrals?** — We could, and for a one-line calculation there is no advantage. But at two loops the number of distinct terms in the Wick expansion reaches the dozens, at three loops the thousands, and the bookkeeping becomes impossible without a graphical shortcut. Feynman's genius was to notice that the terms come in topologically distinct patterns and that each pattern — each *diagram* — carries all the information needed to reconstruct the integral. The diagram is a compressed notation for an unambiguous mathematical expression. Every element of the diagram translates into a specific factor by a dictionary we call the Feynman rules.

7. **Why do the Feynman rules take the form they do — why this particular set of factors?** — Because each factor descends directly from a specific piece of the brane Lagrangian. External lines are the wavefunctions of the Ch 6 one-excitation states. Internal lines are the free-field two-point function, which is the Green's function of the Vol 2 Ch 5 kinetic operator. Vertices are the Fourier transforms of the cubic and quartic coupling terms that we *omitted* from the free Hamiltonian. Loop integrals enumerate the mode sums that close off virtual exchanges. Symmetry factors account for the overcounting when identical lines produce the same contraction. Nothing in the rulebook is ad hoc; every rule traces to an equation in the Lagrangian.

8. **Why does the one-loop vertex correction specifically produce $a_e^{(1)} = \alpha/(2\pi)$?** — Because the integrand, after the standard Feynman-parameter and loop-momentum gymnastics, collapses to a pure number times $\alpha$, and the number, computed from the zone architecture, is $1/(2\pi)$. The same calculation done in standard QED gives the same answer, because the free propagator and the vertex are the same object in both formalisms — in Genesis Physics, the free propagator is derived from the membrane kinetic term rather than postulated from a relativistic field theory, but the answer is identical. The virtue of the Genesis Physics derivation is not a different numerical answer but a different *interpretation*: the virtual electron-positron pair in the loop is a literal oscillation of the Firmament in a hybrid $e^+e^-$ mode, not an abstract mathematical particle.

9. **Why does the Lamb shift distinguish 2S and 2P states specifically?** — Because the s-state wavefunction is nonzero at the origin and the p-state is not, and the dominant part of the Lamb shift — the self-energy contribution — depends on $|\psi(0)|^2$. The p-states do not feel the short-distance vacuum fluctuations the way s-states do. The contact term, the vacuum-polarization contribution, and the kinetic-energy correction all respect this $\ell = 0$ vs $\ell > 0$ distinction. The 1057.845 MHz splitting is the algebraic sum of all of them.

10. **Why are the divergences a feature and not a bug?** — Because the loop integrals, before any cutoff, diverge at large momentum, and in a theory with no physical high-momentum cutoff one is reduced to the "renormalization" procedure of subtracting infinity from infinity. In Genesis Physics the divergence is cut off at $\Lambda \sim \hbar c/\eta_B$ — the physical membrane thickness — and the cutoff is *not* a regularization scheme; it is a property of the medium. Below this cutoff the loop integrals are finite. The divergence of standard QED is an artifact of pretending that space is infinitely divisible. The Firmament is not. Ch 8 will make this statement quantitative; this chapter shows the mechanism.

---

## Key Deliverables

### Derivations (Foundations Vol 4, Chapter 7)

| # | Derivation | Starting Point | Result | Equations |
|---|-----------|---------------|--------|-----------|
| 1 | Splitting Ĥ into free and interacting parts | Brane Lagrangian (2.5.4) with cubic/quartic terms retained | Ĥ = Ĥ₀ + Ĥ_int, with Ĥ_int from the non-quadratic sector | (4.7.1)–(4.7.5) |
| 2 | Interaction picture operators and states | Time evolution split: $\hat{A}_I(t) = e^{iĤ_0 t/\hbar} \hat{A}_S e^{-iĤ_0 t/\hbar}$ | $i\hbar \partial_t |\psi_I\rangle = \hat{H}_I(t) |\psi_I\rangle$ | (4.7.6)–(4.7.12) |
| 3 | Dyson series | Iterative integration of the interaction-picture Schrödinger equation | $\hat{U}_I(t,t_0) = T \exp\left[-\frac{i}{\hbar}\int_{t_0}^t \hat{H}_I(t') dt'\right]$ | (4.7.13)–(4.7.22) |
| 4 | Wick's theorem | Recursive rewriting of T-products using the free-field commutators from Ch 6 | $T[\phi_1\cdots\phi_n] = \sum_{\rm pairings} :\phi\cdots\phi: \prod \langle 0|T\phi_i\phi_j|0\rangle$ | (4.7.23)–(4.7.33) |
| 5 | Firmament propagator | Vacuum expectation value of the free field product using the Ch 6 mode expansion | $D_F(k) = i/(k^2 - m^2 + i\epsilon)$ (scalar form); photon form $-ig_{\mu\nu}/k^2$ | (4.7.34)–(4.7.45) |
| 6 | Feynman rules for zone architecture | Systematic reading of the Dyson series after Wick contraction | Complete dictionary: external lines, propagators (scalar, fermion, photon), QED vertex $-ie\gamma^\mu$, loop measure $\int d^4k/(2\pi)^4$, symmetry factors | (4.7.46)–(4.7.60) [RULES BOX] |
| 7 | Tree-level Coulomb scattering | Apply the rules to $e^- + p \to e^- + p$ at leading order | $\mathcal{M} = -i e^2 \bar{u}\gamma^\mu u \cdot (-g_{\mu\nu}/q^2) \cdot \bar{u}\gamma^\nu u$; recovers Rutherford in non-relativistic limit | (4.7.61)–(4.7.70) |
| 8 | One-loop vertex correction | Apply the rules to the vertex diagram with one virtual photon | Form factors $F_1(q^2), F_2(q^2)$; $F_2(0) = \alpha/(2\pi)$ | (4.7.71)–(4.7.90) |
| 9 | Electron g-2: Schwinger term | Identify $a_e^{(1)} = F_2(0)$ | $a_e^{(1)} = \alpha/(2\pi) = 0.0011614070...$ | (4.7.91)–(4.7.94) |
| 10 | Full numerical $a_e$ | Summation of α through α⁵ + hadronic | $a_e^{\rm th} = 0.00115965218...$ | (4.7.95)–(4.7.99) |
| 11 | Lamb shift: self-energy contribution | One-loop electron self-energy Σ(p²) in the bound-state formalism | $\Delta E_{\rm self}^{2S} - \Delta E_{\rm self}^{2P} \approx 1051.8$ MHz $\cdot h$ | (4.7.100)–(4.7.115) |
| 12 | Lamb shift: vacuum polarization contribution | Contact term from Uehling potential $-(\alpha^2 m_e c^2/12\pi)\delta^3(\vec{r})$ | $\Delta E_{\rm vac}^{2S} - \Delta E_{\rm vac}^{2P} \approx 6$ MHz $\cdot h$ | (4.7.116)–(4.7.123) |
| 13 | Lamb shift total | Sum of self-energy + vacuum polarization + small corrections | $\Delta\nu_{\rm Lamb} = 1057.845$ MHz (theory) vs 1057.845(9) MHz (experiment) | (4.7.124)–(4.7.127) |
| 14 | UV divergence and membrane cutoff | Identify the logarithmic divergence in the vertex loop and apply $\Lambda = \hbar c/\eta_B$ | Finite loop integral; $\Lambda \approx 2.4 \times 10^{19}$ GeV; forward reference to Ch 8 | (4.7.128)–(4.7.135) |

### Figures and Diagrams

**The rule: if a reader would grab a napkin to draw it, the chapter needs a figure there.**

| Fig ID | Title | Type | Placement | What It Shows | Why It's Needed | Key Labels | Equations Referenced | Complexity |
|--------|-------|------|-----------|---------------|----------------|------------|---------------------|-----------|
| Fig 4.7.1 | The Interacting Firmament — Free Modes with Vertices | Schematic | §7.1 | Two ringed panels. Left: three Firmament normal modes vibrating independently (the Ch 6 picture). Right: the same three modes with a vertex coupling where two modes "feed" into a third — ringed by a dashed red box labeled Ĥ_int. | Converts the abstract splitting Ĥ = Ĥ₀ + Ĥ_int into a picture of modes that either stay in their own lane (free theory) or mix at a point (interacting theory). | Mode k₁, k₂, k₃, Ĥ₀, Ĥ_int, Vertex | (4.7.1)–(4.7.5) | Medium |
| Fig 4.7.2 | Schrödinger vs Heisenberg vs Interaction Picture | Comparison | §7.2 | A three-column diagram showing where the time dependence sits in each picture: (S) all on the state; (H) all on the operator; (I) free part on the operator, interaction on the state. An arrow labeled "we use" points at column (I). | Anchors the verbal description of the interaction picture in a structural comparison the reader can remember. | ψ(t), Â(t), Ĥ₀, Ĥ_int | (4.7.6)–(4.7.12) | Simple |
| Fig 4.7.3 | The Dyson Series as a Stack of Time-Ordered Integrals | Diagram | §7.3 | A nested series of rectangles representing successive orders: Û = 1 + (1st order) + (2nd order) + ..., with the n-th rectangle containing n time-integration variables $t_1 > t_2 > ... > t_n$ and the operator product T[Ĥ_I(t₁)...Ĥ_I(t_n)]. | Makes the recursive structure of the Dyson series visually obvious. | T, Ĥ_I, Order 1, Order 2, Order n | (4.7.13)–(4.7.22) | Medium |
| Fig 4.7.4 | Wick's Theorem in Pictures | Diagram | §7.4 | For a four-field product $T[\phi_1\phi_2\phi_3\phi_4]$, show the three distinct contraction patterns as arcs connecting pairs of field labels, each labeled with a propagator symbol D_F. Above: the normal-ordered form :φ₁φ₂φ₃φ₄:. | The whole theorem becomes a single picture of arcs, which is how practitioners actually remember it. | φ₁..φ₄, D_F, :: (normal ordering), Contraction | (4.7.23)–(4.7.33) | Medium |
| Fig 4.7.5 | The Firmament Propagator in Real Space and Momentum Space | Plot + Diagram | §7.5 | Two panels. Left: a plot of the real-space propagator D_F(x-y) showing a light-cone-like structure peaked on the forward and backward cones. Right: the momentum-space form $i/(k^2-m^2+i\epsilon)$ with a pole annotated on the k⁰ axis and the Feynman $i\epsilon$ prescription shown as a small contour deformation. | Makes the propagator feel like an object the reader could recognize in either representation, and visually connects the $i\epsilon$ prescription to causality on the Firmament. | D_F(x-y), light cone, k², m², $i\epsilon$, pole | (4.7.34)–(4.7.45) | Complex |
| Fig 4.7.6 | Feynman Rules for Zone Architecture — Reference Box | Rules Box | §7.6 (boxed result) | A single large shaded box containing: (a) external-line factors (incoming/outgoing scalar, fermion, photon) with their wavefunctions; (b) three propagator diagrams (scalar, fermion, photon) with their algebraic expressions; (c) the QED vertex $-ie\gamma^\mu$ pictured as a point with three lines; (d) loop measure $\int d^4k/(2\pi)^4$; (e) symmetry factor rule. Each row labeled with the Lagrangian term it comes from. | This is the reference object the reader will consult for every calculation in the rest of the volume. It is also the source for Appendix C. | External, Propagator, Vertex, Loop, Symmetry | (4.7.46)–(4.7.60) | Complex |
| Fig 4.7.7 | Tree-Level Coulomb Scattering Diagram | Feynman Diagram | §7.7 | An electron line (incoming p, outgoing p') exchanging a single photon with a proton line (incoming P, outgoing P'). Momentum labels, vertex dots, photon propagator labeled $-ig_{\mu\nu}/q^2$. | The first concrete Feynman diagram the reader meets, used to anchor the rules. | e⁻, p, p', γ, q, p^+, P, P' | (4.7.61)–(4.7.70) | Medium |
| Fig 4.7.8 | The One-Loop Vertex Correction Diagram | Feynman Diagram | §7.8 | The electron vertex with a virtual photon looping between the two external fermion lines. Momentum labels on each internal segment: p, p', k, p-k, p'-k. External photon attaches at the vertex; loop photon is a dashed curve connecting the two fermion legs. | This is *the* diagram for $a_e^{(1)}$. Every reader of the g-2 story recognizes it; the chapter is not complete without it. | p, p', k, p-k, p'-k, γ external, γ loop, vertex | (4.7.71)–(4.7.90) | Complex |
| Fig 4.7.9 | Higher-Order QED Diagrams for the Electron g-2 | Schematic | §7.9 | A small multi-panel showing representative two-loop, three-loop, and four-loop diagrams, with annotations of the number of diagrams at each order (∼7 at two-loop, ∼72 at three-loop, ∼891 at four-loop, ∼12672 at five-loop) and their coefficients $A_2 = 1.895$, $A_3 = 0.321$, etc. | Shows the reader why higher-order QED is a monumental calculation and puts the coefficients in perspective; gives credibility to the 12-digit agreement with experiment. | 1-loop, 2-loop, 3-loop, 4-loop, A₂, A₃, A₄, A₅ | (4.7.95)–(4.7.99) | Complex |
| Fig 4.7.10 | The Lamb Shift Diagrams: Self-Energy and Vacuum Polarization | Feynman Diagrams | §7.10 | Two labeled panels. Left: the electron self-energy — an electron line with a photon loop attached. Right: vacuum polarization — a photon propagator with an electron loop inside. Beside each, the energy shift contribution for the 2S₁/₂ state. | Shows *which* diagrams are responsible for the Lamb shift and what fraction of the total each contributes, so that the numerical answer is not magic. | Σ(p), Π(q²), 2S₁/₂, 2P₁/₂, ~1052 MHz, ~27 MHz | (4.7.100)–(4.7.127) | Medium |
| Fig 4.7.11 | Energy Level Splitting in Hydrogen: 2S₁/₂ and 2P₁/₂ | Energy Level Diagram | §7.10 | The hydrogen n=2 level split under the Lamb shift. Flat levels without Lamb shift (Dirac prediction, degeneracy), split levels with Lamb shift, labeled with the 1057.845 MHz frequency. Experimental value cited below. | Gives physical grounding to an otherwise abstract quantity. The reader sees, on an energy-level diagram, what the calculation has produced. | 2S₁/₂, 2P₁/₂, Dirac, Lamb shift, 1057.845 MHz | (4.7.124)–(4.7.127) | Simple |
| Fig 4.7.12 | UV Divergence and the Membrane Cutoff | Plot | §7.11 | A plot of the vertex-loop integrand as a function of loop momentum k, showing the logarithmic growth at large k, with a vertical dashed line at $\Lambda = \hbar c/\eta_B \approx 2.4 \times 10^{19}$ GeV. Shaded region above $\Lambda$ labeled "modes with $\lambda < \eta_B$ cannot exist on the Firmament". | Visually distinguishes the standard-QED divergence (integrate to infinity) from the Genesis Physics behavior (integrate to a physical cutoff), showing that the cutoff is not a regularization trick but a property of the medium. | k, log, $\Lambda$, $\eta_B$, $\lambda$, divergence, cutoff | (4.7.128)–(4.7.135) | Medium |

### Problem Sets (Foundations)

| Difficulty | Count | Topics Covered |
|-----------|-------|---------------|
| Computational | 4 | (1) Given a two-field T-product and explicit creation/annihilation operators, apply Wick's theorem and identify the contraction pattern. (2) Compute the tree-level $e^-e^- \to e^-e^-$ (Møller) amplitude from the rules of Fig 4.7.6 and verify that it has the correct crossing symmetry. (3) Evaluate the one-loop Feynman parameter integral for $F_2(q^2=0)$ and recover the Schwinger term $\alpha/(2\pi)$. (4) Use the Uehling potential to compute the vacuum-polarization contribution to the 2S Lamb shift, and report the answer in MHz. |
| Conceptual | 3 | (1) Explain why the propagator D_F(k) depends only on the *free* Lagrangian and not on the interaction. (2) Why are disconnected diagrams absent from S-matrix elements? Give the Goldstone–Wick argument. (3) Explain, in one paragraph, why the one-loop vertex correction gives the *same* numerical $a_e^{(1)}$ in standard QED and in Genesis Physics, despite the very different interpretations. |
| Challenge | 3 | (1) Compute the two-loop coefficient $A_2 = 0.5 - \pi^2/6 + (3/4)\zeta(3) + (\pi^2/2)\ln 2 \approx -0.3285$ *starting from the three two-loop diagrams* (this result is the Petermann–Sommerfield coefficient, and it is a standard graduate-level calculation). (2) Derive the Uehling potential $\Phi_{\rm vac}(r) = -(\alpha/3\pi)\int_{2m_e c}^\infty (dk/k) e^{-kr}\sqrt{1-(2m_e c/k)^2}$ starting from the photon self-energy and the Ward identity. (3) Show that the vertex loop integral, cut off at $\Lambda = \hbar c/\eta_B$, produces the same $F_2(0)$ as dimensional regularization does in the standard treatment, and explain why the cutoff-dependence cancels in this particular observable. |

---

## Verification Criteria

### Universal Criteria
- [ ] Every requirement above is marked MET
- [ ] "But why?" chain — all 10 questions answered in the chapter text
- [ ] No forward dependencies except those explicitly flagged (Ch 8 for systematic renormalization; Ch 10 for the spin-1/2 blocker; Appendix C for the compiled Feynman rules)
- [ ] Notation consistent with Vols 1–3 and Vol 4 Ch 1–6
- [ ] Word count within target: 10,000–14,000 words
- [ ] All `[FIGURE: ...]` placeholders correspond to specs above
- [ ] All `[TODO]` markers resolved

### Product-Specific Criteria (Foundations Vol 4)
- [ ] Every derivation starts from a previously established equation (Vol 2 Ch 5, Vol 4 Ch 6) with citation
- [ ] Every equation numbered (4.7.N)
- [ ] The Feynman rules box is self-contained and labeled as the source for Appendix C
- [ ] The spin-1/2 placeholder is acknowledged openly with forward reference to Ch 10 (SKEPTIC-CRITICAL)
- [ ] The $a_e$ calculation reaches the Schwinger term explicitly, and the full numerical comparison with experiment is shown
- [ ] The Lamb shift is derived, not quoted — both the self-energy and vacuum-polarization contributions are identified
- [ ] The UV cutoff is presented as a physical property of the membrane, not a regularization scheme
- [ ] Voice is Feynman-textbook: reasons-first, declarative, engaging
- [ ] Problem sets span computational → conceptual → challenge
- [ ] A Student reviewer can pick up the chapter and *do* a Feynman diagram calculation

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

- **Primary source:** `05-QED_PRECISION_CALCULATIONS.md`. The chapter's numerical targets for $a_e$ and the Lamb shift are taken directly from this document.
- **Load-bearing prior chapters:** Vol 2 Ch 5 (Lagrangian — source of the propagator) and Vol 2 Ch 6 (gauge theory — source of the vertex $-ie\gamma^\mu$) must be cited at the moment each of those objects appears.
- **Student reviewer is the acceptance criterion.** The Student reviewer must be able to work through a tree-level diagram and at least sketch the one-loop vertex correction after reading. If the reviewer cannot do this, the chapter is not done.
- **Spin-1/2 placeholder alert:** the electron is treated as a Dirac spinor without derivation. The chapter must flag this as a placeholder for the Ch 10 topological-defect derivation. Use of $\bar{u}\gamma^\mu u$ is permitted because the one-excitation matrix element is universal; derivation of the fermionic structure is not.
- **Appendix C dependency:** the Feynman rules box in §7.6 is the normative form. Appendix C will reproduce it verbatim, with expanded derivations in the margins. The rules box in this chapter must be complete enough to stand alone.
- **Skeptic alert:** two hot buttons. (1) The propagator derivation — show explicitly that it comes from the Ch 6 free-field VEV, do not import it from a QFT textbook. (2) The UV cutoff — show that $\Lambda = \hbar c/\eta_B$ is a physical property, not a regularization parameter. The Skeptic will check for hand-waving at both points.
- **Theologian note:** no doctrinal commentary this chapter. Save it for Ch 14 and the Creator's Blueprint companion.
- **Test suite:** `Research/Mathematical_Models/05_Quantum_Mechanics/test_qm_applied.py` must be run at the end of Phase 6 and its pass/fail recorded here.

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-08 | Initial spec created | Beginning Phase 1 of Ch 7 chapter writing |
