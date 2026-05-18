---
product: Foundations Vol 4 — The Quantum World
chapter: 7
title: Perturbation Theory and Feynman Diagrams — Detailed Outline
status: OUTLINE
created: 2026-04-08
---

# Chapter 7 — Detailed Outline

This outline implements the SPEC. Each section carries a topic sentence, a "why" entry point, a content sketch, and an exit condition stating what the reader knows by the end. The twelve figures from the SPEC are placed at their sections.

---

## §7.0 Introduction — From Free Modes to Interacting Processes
**Topic sentence.** Chapter 6 built the machinery of a free Firmament; Chapter 7 turns the interaction on, and with it the entire catalog of processes that make the quantum world quantum.
**Why entry point.** The free theory of Ch 6 is exact but inert. Pair production, radiative decay, scattering, and the precision observables that made QED the most tested theory in physics all live in the *interacting* sector. This chapter is where the theory meets experiment.
**Content sketch.** Restate the Ch 6 result ($\hat H_0 = \sum_k \hbar\omega_k(\hat N_k + 1/2)$). Name the interactions we want to turn on: cubic and quartic terms in the Firmament Lagrangian that generate the QED vertex and, in later chapters, the Standard Model. Preview the four tools (interaction picture, Dyson series, Wick's theorem, Feynman diagrams). Announce the two acceptance tests (the electron g-2 and the Lamb shift). Acknowledge the spin-1/2 placeholder up front: the Dirac structure will be used without derivation, with Ch 10 flagged as the resolution.
**Exit condition.** The reader knows the goal, the tools, the two numerical targets, and the one honest caveat.

---

## §7.1 The Interacting Firmament
**Topic sentence.** An interaction on the Firmament is any term in the Firmament Lagrangian that is more than quadratic in the fields; such terms break the mode decoupling of Chapter 6 and require a new method.
**Why entry point.** Why do we call anything "interacting"? Because quadratic Lagrangians are sums of independent oscillators and can be solved exactly; anything beyond quadratic couples modes together, and coupled oscillators do not decouple.
**Content sketch.** Write the Firmament Lagrangian schematically $\mathcal{L} = \mathcal{L}_0 + \mathcal{L}_{\rm int}$. Identify the QED interaction from Vol 2 Ch 5–6 as $\mathcal{L}_{\rm int} = -e\bar\psi\gamma^\mu\psi A_\mu$. Split the Hamiltonian $\hat H = \hat H_0 + \hat H_{\rm int}$. Give an order-of-magnitude argument for why a perturbative treatment is legitimate when $\alpha \approx 1/137$ is small.

Figure: **Fig 4.7.1 — The Interacting Firmament: Free Modes with Vertices** — two panels contrasting the decoupled-mode Ch 6 picture with the coupled-mode interacting picture, with the interaction vertex ringed.

**Exit condition.** The reader has Ĥ = Ĥ₀ + Ĥ_int written down explicitly from the Firmament Lagrangian and knows that $\alpha$ is the small parameter.

---

## §7.2 The Interaction Picture
**Topic sentence.** The interaction picture puts the free evolution on the operators and the interaction on the states, which is the only arrangement in which perturbation theory in $\hat H_{\rm int}$ becomes tractable.
**Why entry point.** Why not stay in the Schrödinger picture? Because the Schrödinger picture leaves the state carrying *all* the dynamics, including the vastly complicated free evolution over the Fock space of Ch 6 — and we already solved that part exactly. Wasting computation to re-do it in each order of perturbation theory is unwise.
**Content sketch.** Define $|\psi_I(t)\rangle = e^{i\hat H_0 t/\hbar}|\psi_S(t)\rangle$ and $\hat A_I(t) = e^{i\hat H_0 t/\hbar}\hat A_S e^{-i\hat H_0 t/\hbar}$. Derive the interaction-picture Schrödinger equation $i\hbar\partial_t|\psi_I\rangle = \hat H_I(t)|\psi_I\rangle$ where $\hat H_I(t) = e^{i\hat H_0 t/\hbar}\hat H_{\rm int} e^{-i\hat H_0 t/\hbar}$. Note that the Ch 6 free field operators $\hat\psi(x,t)$ naturally live in the interaction picture.

Figure: **Fig 4.7.2 — Schrödinger vs Heisenberg vs Interaction Picture** — three-column comparison of where the time dependence sits.

**Exit condition.** The reader knows the three pictures, why we use the interaction picture, and has the equation $i\hbar\partial_t|\psi_I\rangle = \hat H_I(t)|\psi_I\rangle$ in hand.

---

## §7.3 The Dyson Series
**Topic sentence.** Integrating the interaction-picture Schrödinger equation iteratively produces the Dyson series, a time-ordered power series in $\hat H_I$ that is the starting point for every perturbative calculation in this volume.
**Why entry point.** Why time-ordered? Because $\hat H_I(t)$ and $\hat H_I(t')$ do not commute, and $\exp(\int \hat H_I)$ is only the right solution if the operators at earlier times stand to the right of those at later times. The time-ordering symbol $T$ enforces exactly that.
**Content sketch.** Iterate $|\psi_I(t)\rangle = |\psi_I(t_0)\rangle - (i/\hbar)\int_{t_0}^t \hat H_I(t_1) |\psi_I(t_1)\rangle dt_1$. Resum to the time-ordered exponential $\hat U_I(t, t_0) = T\exp[-i/\hbar \int \hat H_I]$. Define the S-matrix $\hat S = \hat U_I(+\infty, -\infty)$ as the object whose matrix elements give scattering amplitudes.

Figure: **Fig 4.7.3 — The Dyson Series as a Stack of Time-Ordered Integrals** — nested rectangles showing successive orders.

**Exit condition.** The reader has the Dyson series written down and knows that each order is a time-ordered product of interaction Hamiltonians.

---

## §7.4 Wick's Theorem
**Topic sentence.** Wick's theorem converts the time-ordered products inside the Dyson series into sums of normal-ordered products times contractions, and it is the bookkeeping device that lets us extract physical matrix elements.
**Why entry point.** Why do we need normal ordering at all? Because physical matrix elements pick out the pieces of an operator that act in a specific way on |0⟩ and |0⟩†, and normal ordering sorts operators into exactly that form. Without it, the Dyson series is a fog of commutators.
**Content sketch.** Define the contraction $\langle 0| T\hat\phi_i\hat\phi_j|0\rangle$. State Wick's theorem for a string of n free fields:
$T[\hat\phi_1 \cdots \hat\phi_n] = \sum_{\rm pairings} :\hat\phi\cdots\hat\phi: \prod_{\rm pairs} \langle 0|T\hat\phi_i\hat\phi_j|0\rangle$.
Prove by induction on n using the Ch 6 commutation relations. Show that matrix elements between initial and final states with definite particle content pick out the pairings in which exactly the right number of creation/annihilation operators remain.

Figure: **Fig 4.7.4 — Wick's Theorem in Pictures** — the four-field contraction patterns drawn as arcs between field labels.

**Exit condition.** The reader can apply Wick's theorem to a four- or six-field product by hand.

---

## §7.5 The Firmament Propagator
**Topic sentence.** The contractions in Wick's theorem are vacuum expectation values of time-ordered pairs of free-field operators, and for the Firmament those vacuum expectation values are the Feynman propagator of a scalar field with dispersion $\omega_k$, which we derive here and call $D_F$.
**Why entry point.** Why does the propagator depend only on the free theory? Because the vacuum and the free-field operators are all we have used; the interaction plays no role in defining $D_F$. The interaction decides *which* propagators appear in which diagrams, not what they are.
**Content sketch.** Use the Ch 6 mode expansion of $\hat\psi(x,t)$ to compute $\langle 0|T\hat\psi(x)\hat\psi(y)|0\rangle$. Carry out the sum over modes in infinite volume, take the Fourier transform, and arrive at $D_F(k) = i/(k^2 - m^2 + i\epsilon)$. Explain the $i\epsilon$ prescription as the enforcement of forward causality on the Firmament. Give the fermion and photon versions by analogy (a full derivation of the fermion version requires Ch 10 and is flagged here).

Figure: **Fig 4.7.5 — The Firmament Propagator in Real Space and Momentum Space** — real-space causal structure and momentum-space pole with $i\epsilon$ deformation.

**Exit condition.** The reader has $D_F(k)$ in hand with an understanding of where the $i\epsilon$ comes from and why the object is universal.

---

## §7.6 Feynman Diagrams and Feynman Rules for Zone Architecture
**Topic sentence.** Collecting the output of Wick's theorem by topology gives Feynman diagrams, and the translation dictionary from diagram to amplitude is the set of Feynman rules for zone architecture — the normative reference for the rest of the volume.
**Why entry point.** Why turn equations into pictures? Because at two loops the number of distinct contraction patterns reaches the dozens, and the human mind is better at tracking topology than at tracking integrals; the diagram is a compressed notation for an unambiguous mathematical expression.
**Content sketch.** Introduce Feynman diagrams as graphs whose vertices are factors of $\hat H_{\rm int}$ and whose edges are contractions. Give the full rulebook for zone architecture:

- External lines: scalar — $u(p)$ or $u^*(p)$; fermion — $u(p,s), \bar u(p,s), v(p,s), \bar v(p,s)$ (placeholder, with Ch 10 note); photon — $\epsilon^\mu(p,\lambda)$ or its conjugate.
- Internal lines (propagators): scalar $i/(k^2-m^2+i\epsilon)$; photon $-ig_{\mu\nu}/k^2$; fermion $i(\slashed k + m)/(k^2-m^2+i\epsilon)$ [Ch 10 placeholder].
- Vertices: QED vertex $-ie\gamma^\mu$ (from $-e\bar\psi\gamma^\mu\psi A_\mu$ in the Firmament Lagrangian).
- Loop integration: $\int d^4k/(2\pi)^4$ for each independent loop momentum.
- Symmetry factors: 1/N! for each permutation that leaves the diagram invariant.
- Overall sign: one factor of $(-1)$ for each closed fermion loop, one factor of $(-1)^{n-1}$ from the $n$-th order Dyson expansion (absorbed into the conventions).

Trace each rule to its Lagrangian origin in a small margin note. State explicitly that this rulebook is the source for Appendix C of this volume.

Figure: **Fig 4.7.6 — Feynman Rules for Zone Architecture — Reference Box** — the complete shaded-box rulebook.

**Exit condition.** The reader has the complete rulebook in a self-contained figure and can use it without consulting another chapter.

---

## §7.7 First Application — Tree-Level Coulomb Scattering
**Topic sentence.** Before tackling loops, apply the rules to the simplest nontrivial diagram — tree-level Coulomb scattering — and verify that the amplitude reproduces the classical Rutherford result in the non-relativistic limit.
**Why entry point.** Why start here? Because Coulomb scattering is the single place in QED where the answer is already known from 19th-century physics, so we have a sanity check: if the rules are right, the cross section must reduce to $d\sigma/d\Omega = (\alpha^2/4 m_e^2 v^4 \sin^4(\theta/2))$.
**Content sketch.** Draw the tree diagram: electron line exchanging a single photon with a proton line. Apply the rules to write the amplitude $\mathcal{M} = -ie^2 \bar u(p')\gamma^\mu u(p) \cdot (-g_{\mu\nu}/q^2) \cdot \bar u(P')\gamma^\nu u(P)$. Square, average over spins, take the non-relativistic limit, obtain Rutherford. Note that all quantities are finite at tree level — no cutoff needed.

Figure: **Fig 4.7.7 — Tree-Level Coulomb Scattering Diagram** — labeled electron–proton exchange diagram.

**Exit condition.** The reader has now *used* the rules of §7.6 in anger and has verified them against a known answer.

---

## §7.8 The One-Loop Vertex Correction
**Topic sentence.** The one-loop vertex correction is the diagram in which a virtual photon is exchanged between the two fermion legs of the electron–photon vertex, and its evaluation produces the form factors $F_1(q^2)$ and $F_2(q^2)$ from which the anomalous magnetic moment is extracted.
**Why entry point.** Why does *this* diagram give the anomalous magnetic moment? Because the vertex function, by Lorentz covariance and gauge invariance, can be decomposed into exactly two form factors, and $F_2(0)$ is the definition of $a_e$.
**Content sketch.** Draw the diagram. Apply the rules. Write the loop integral. Execute the Feynman parameterization. Perform the loop-momentum integral. Extract $F_1(0) = 1$ (charge normalization) and $F_2(0) = \alpha/(2\pi)$ (Schwinger). Do this carefully enough that a reader holding only this chapter can reproduce it. Acknowledge that the full step-by-step algebra occupies several pages in any QFT textbook and provide the essential milestones.

Figure: **Fig 4.7.8 — The One-Loop Vertex Correction Diagram** — the canonical g-2 diagram with momentum labels.

**Exit condition.** The reader has computed a one-loop diagram end to end and obtained the Schwinger term.

---

## §7.9 Electron g-2: The Precision Test
**Topic sentence.** Summing the perturbative series for the electron anomalous magnetic moment through the first five orders and adding the small hadronic contribution produces $a_e^{\rm th} = 0.00115965218089$, which matches the CODATA 2018 experimental value $a_e^{\rm exp} = 0.00115965218081(11)$ at a level of one part in $10^{10}$.
**Why entry point.** Why does the precision agreement matter? Because it says, with essentially no ambiguity, that the theoretical machinery of perturbation theory on the Firmament is a faithful description of physical reality to at least one part in a billion. No other prediction in physics is that precise.
**Content sketch.** Tabulate the coefficients $A_2 \approx 1.8951$ (Petermann–Sommerfield), $A_3 \approx 0.321$ (Laporta–Remiddi), $A_4$ and $A_5$ (Kinoshita and collaborators). Give the numerical contribution of each order. Present the final sum and the comparison with experiment. Interpret the agreement in the Genesis Physics framework: the virtual electron–positron pair in every loop is a literal oscillation of the Firmament in a hybrid $e^+e^-$ mode, and $\alpha$ is derived from the 6D geometry via $\alpha^{-1} = 1.44 \ln(\xi_A/\eta_B) \approx 137$.

Figure: **Fig 4.7.9 — Higher-Order QED Diagrams for the Electron g-2** — representative diagrams at each order with their multiplicities.

**Exit condition.** The reader has seen the framework produce a 12-digit prediction and knows how to read the calculation.

---

## §7.10 The Lamb Shift
**Topic sentence.** The 1057.845 MHz splitting between the 2S₁/₂ and 2P₁/₂ states of hydrogen is the algebraic sum of two QED diagrams — the electron self-energy (dominant, ~1052 MHz) and the vacuum polarization (small, ~27 MHz) — plus minor kinematic corrections.
**Why entry point.** Why 2S vs 2P specifically? Because the s-state wavefunction is nonzero at the nucleus and the p-state is not, and every term in the Lamb shift depends on $|\psi(0)|^2$ one way or another; the splitting is a direct probe of vacuum fluctuations at the origin.
**Content sketch.** Draw the two diagrams. Sketch the self-energy calculation $\Delta E_{\rm self} = \text{Re}\,\Sigma(E)$, identifying the ln-divergence, the mass renormalization subtraction, and the finite 1052 MHz contribution to the 2S level. Sketch the vacuum polarization calculation, write the Uehling contact term $-(\alpha^2 m_e c^2 / 12\pi)\delta^3(\vec r)$, compute its expectation value in the 2S state, obtain 27 MHz. Add the small kinematic and recoil corrections. Report the theoretical total 1057.845 MHz and compare with experiment $1057.845(9)$ MHz.

Figures: **Fig 4.7.10 — The Lamb Shift Diagrams** and **Fig 4.7.11 — Energy Level Splitting in Hydrogen**.

**Exit condition.** The reader has the complete breakdown of the Lamb shift and sees how each piece arises from a specific diagram in the rulebook of §7.6.

---

## §7.11 Divergences and the Membrane Cutoff
**Topic sentence.** Every loop integral in the preceding sections diverges logarithmically at large momentum, and in Genesis Physics that divergence is cut off physically at $\Lambda = \hbar c/\eta_B \approx 2.4 \times 10^{19}$ GeV by the finite thickness of the Firmament.
**Why entry point.** Why is this cutoff not a regularization trick? Because $\eta_B$ is a real length in the zone architecture — the extent of the Firmament into the Waters Below — and modes with wavelength shorter than $\eta_B$ do not fit on the Firmament. They are not excluded by convention; they do not exist.
**Content sketch.** Identify the log divergence in the vertex loop. Impose the cutoff at $\Lambda$. Show that the finite part of the integral — the part that gives $F_2(0) = \alpha/(2\pi)$ — is cutoff-independent, and that only the pieces absorbed into charge and mass renormalization depend on $\Lambda$. Explain why the same statement holds order by order (this is the content of renormalizability, which Ch 8 will treat systematically). Forward-reference Ch 8 for the complete story.

Figure: **Fig 4.7.12 — UV Divergence and the Membrane Cutoff** — loop-integrand plot with the cutoff marked.

**Exit condition.** The reader knows *why* the divergences do not threaten the precision predictions and that Ch 8 will prove the statement at every order.

---

## §7.12 Summary and What Comes Next
**Topic sentence.** Chapter 7 has built the perturbative toolkit, compiled the Feynman rules for zone architecture, and used the rules to recover QED's two precision triumphs; Chapter 8 will systematize the renormalization program, Ch 9 will address vacuum energy and the Casimir effect, and Chapters 10–14 will use the rulebook to derive the Standard Model.
**Content sketch.** Restate the four tools (interaction picture, Dyson series, Wick's theorem, Feynman diagrams). Restate the rulebook. Restate the two numerical agreements. Point forward. Point back honestly at the spin-1/2 placeholder and the cutoff details that Ch 8 will finish.

**Exit condition.** The reader can proceed to Ch 8 without looking back.

---

## Outline Review Checklist

- [x] Every chapter requirement maps to at least one section (Ch7-001 → §7.1; Ch7-002 → §7.2; Ch7-003 → §7.3; Ch7-004 → §7.4; Ch7-005 → §7.5; Ch7-006 → §7.6; Ch7-007 → §7.6; Ch7-008 → §7.6, §7.12; Ch7-009 → §7.7; Ch7-010 → §7.8; Ch7-011 → §7.9; Ch7-012 → §7.10; Ch7-013 → §7.11; Ch7-014 → §7.0, §7.5, §7.6, §7.8, §7.12; Ch7-015 → problem sets).
- [x] No section uses concepts not yet established (the fermion structure is the one placeholder, flagged every time it appears).
- [x] "Why" chain is unbroken across sections (§7.1 → §7.2 → §7.3 → §7.4 → §7.5 → §7.6 → §7.7 → §7.8 → §7.9 → §7.10 → §7.11).
- [x] Prerequisites are satisfied by prior chapters (Ch 2, Ch 6, Vol 2 Ch 5, Vol 2 Ch 6).
- [x] Figure plan complete — every spatial structure, diagrammatic object, and conceptual model has a figure spec in the SPEC (twelve figures).
