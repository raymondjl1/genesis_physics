---
product: Foundations Vol 4 — The Quantum World
chapter: 2
title: The Schrödinger Equation Derived
status: SPEC → OUTLINE → DRAFT
citation_convention: (1.Ch.Eq), (2.Ch.Eq), (3.Ch.Eq), (4.Ch.Eq)
target_length: 15,000–18,000 words (≈ 40–50 printed pages)
voice: Feynman writing a textbook
---

# Chapter 2 Specification — The Schrödinger Equation Derived

## 1. Mission (one sentence)

Show — with no postulate, no hand-wave, and no sleight-of-hand — that the time-dependent Schrödinger equation is the *non-relativistic envelope limit* of the Firmament membrane wave equation established in Vol 1 Ch 5, and that the ℏ appearing in it is the same ℏ already derived in Vol 1 Ch 10 §10.3.

## 2. Requirements Traced to Vol 4 Requirements

| Requirement | Source | Met in Chapter by |
|---|---|---|
| QM derived from membrane dynamics (no postulation) | WP §Critical Deliverables; Special instructions | §2.3, §2.4, §2.5 — the full envelope derivation |
| Schrödinger equation not *assumed* | WP §Identity; Ch 1 thesis | §2.4.5 — the final boxed result, earned line by line |
| Every step traces to the membrane EoM | Special instructions | §2.3 chain of implications; §2.9 traceability table |
| ℏ is the derived constant, not an import | WP §Critical; Special instructions | §2.2 restates (1.10.*), §2.4 uses derived ℏ throughout |
| Vol 1 Ch 5 (Firmament) and Ch 6 (Waters) cited | Dependencies table | §2.2, §2.7 |
| QM must reduce to Vol 3 classical mechanics in the right limit | Continuity checklist | §2.7 — Ehrenfest + ℏ → 0 limit |
| Honest about open issues | WP "Golden Rule" | §2.8 — four admitted limitations |
| 40–50 pages (15k–18k words) | WP chapter table | Seven sections, proportioned in outline |

## 3. Prerequisites (what the reader must already know)

From Volumes 1–3 and from Vol 4 Ch 1:

1. **The Firmament membrane wave equation** (Vol 1 Ch 5): μ ψ_tt = σ ∇²ψ − V_ext ψ + ℱ, with c² = σ/μ. Citation: (1.5.1)–(1.5.12).
2. **The Waters environmental coupling** (Vol 1 Ch 6): stochastic forcing ℱ(x,t) from Ψ_A, Ψ_B fluctuations. Citation: (1.6.*).
3. **Boundary-condition quantization and ℏ derivation** (Vol 1 Ch 10 §10.3): ℏ = (σ η_B³/2c)(η_B/ξ_A)² β_geom = 1.0546 × 10⁻³⁴ J·s. Citation: (1.10.12)–(1.10.19).
4. **Topological defects as particles** (Vol 3 Ch 6–7): particles are vortex cores with core radius ∼ η_B; mass m emerges from defect energy. Citation: (3.6.*), (3.7.*).
5. **Classical limit machinery** (Vol 3 Ch 1–2): Hamilton–Jacobi equation S_t + H(∇S, x) = 0; action principle. Citation: (3.1.*), (3.2.*).
6. **Ch 1 of this volume:** the two architectural facts (bounded extra dimensions; finite membrane action quantum) and the four "but why?" answers.

The reader is explicitly *not* assumed to know:
- Hilbert space formalism (this volume will build it from membrane spaces in Ch 6).
- The Schrödinger equation in any conventional form (that is what we are deriving).
- Dirac bra-ket notation (introduced in a side-note, §2.6).

## 4. The "Why" Chain (but why? questions this chapter answers)

1. **But why does a relativistic membrane equation become the non-relativistic Schrödinger equation?** — Because the rest-energy oscillation e^{−iE₀t/ℏ} is fast compared to the envelope dynamics, and the second time-derivative of the envelope is suppressed by a factor (Δt·E₀/ℏ)⁻¹ relative to the first.
2. **But why is the Schrödinger equation *first*-order in time when the membrane equation is *second*-order?** — Because one of the two degrees of freedom of the second-order equation has been "frozen out" by choosing the positive-frequency branch (the envelope). The antiparticle branch survives but is outside the non-relativistic window.
3. **But why is the wave function complex?** — Because the envelope is the slow modulation of a carrier e^{−iE₀t/ℏ}, and the carrier forces an intrinsically two-component (real + imaginary) structure. Real membranes, complex envelopes.
4. **But why does the Schrödinger equation contain i?** — Because the factor of i is what survives when you divide out e^{−iE₀t/ℏ} and keep only leading order in E/E₀. It is a *consequence* of rotating-frame bookkeeping, not an independent postulate.
5. **But why does the Schrödinger equation conserve probability?** — Because it is derived from a *real* wave equation with a real Hamiltonian operator, and the envelope's L² norm is the conserved mass of the localized defect.
6. **But why is the potential V(x) identified with an external tension variation on the membrane?** — Because the membrane wave equation already contains V_ext, and dimensional analysis forces V_ext/σ and V(x)·(2m/ℏ²) to coincide in the NR limit. This is shown in §2.5.

## 5. Key Deliverables (Foundations)

The chapter must produce *one* central derivation (§2.3–§2.5), plus a supporting web of checks. The central derivation is a line-by-line, dimensionally checked, forward-only chain from

$$\mu \ddot\psi = \sigma \nabla^2 \psi - V_{\text{ext}}\psi \tag{1.5.1}$$

to

$$i\hbar\, \partial_t \Psi = -\frac{\hbar^2}{2m}\nabla^2 \Psi + V(x)\Psi. \tag{4.2.central}$$

Every intermediate line must cite either (i) a Vol 1–3 result, (ii) a dimensional identity, or (iii) the explicit non-relativistic assumption E − E₀ ≪ E₀.

**Derivation plan** — the chapter's logical backbone:

| Step | Starting Point | Result | Citation |
|---|---|---|---|
| 0 | Ch 1 setup: we want the envelope equation | Statement of target | Ch 1 thesis |
| 1 | Firmament wave equation | Relativistic dispersion ω² = c²k² + (mc²/ℏ)² | (1.5.1)–(1.5.6), (1.5.10) |
| 2 | Derived ℏ from Vol 1 Ch 10 | Numerical value of ℏ | (1.10.12)–(1.10.19) |
| 3 | Dispersion + defect mass identification | Klein–Gordon form on the membrane | (1.5.10), (3.6.*) |
| 4 | Envelope ansatz ψ = Ψ(x,t) e^{−imc²t/ℏ} | Expansion of ∂_t ψ and ∂_t² ψ | Algebraic |
| 5 | NR limit (∂_t Ψ ≪ mc²/ℏ · Ψ) | Drop ∂_t² Ψ term | Dimensional argument |
| 6 | Rearrangement and c² = σ/μ | Time-dependent Schrödinger equation | Algebraic |
| 7 | Identification of V_ext/σ with V(x)·2m/ℏ² | External potential acquires physical meaning | Dimensional consistency |
| 8 | Probability current from real EoM | |Ψ|² conservation; continuity equation | Noether on (1.5.1) |
| 9 | Ehrenfest / ℏ → 0 limit | Recover Vol 3 Hamiltonian mechanics | (3.1.*), (3.2.*) |
| 10 | Stationary-state separation | Time-independent Schrödinger equation | Algebraic |
| 11 | Particle-in-a-box sanity check | Quantized k_n, E_n | (1.10.*) |
| 12 | Free-particle sanity check | Gaussian spreading, v_g = p/m | Algebraic |
| 13 | Ehrenfest theorem | ⟨x⟩, ⟨p⟩ obey classical equations | Algebraic |
| 14 | Traceability table and honest limitations | Chapter closes with scoreboard | §2.9, §2.8 |

## 6. Figures and Diagrams (5 figures)

Per the Foundations figure rule (3–5 figures per chapter), five figures are justified here:

| ID | Title | Placement | Type | Complexity |
|---|---|---|---|---|
| Fig 4.2.1 | Rest-Energy Carrier and Slow Envelope | §2.3, after ansatz introduction | Two-panel time series | Medium |
| Fig 4.2.2 | The Non-Relativistic Window | §2.4, mid-section | Log–log regime plot | Medium |
| Fig 4.2.3 | Derivation Tree — From (1.5.1) to Schrödinger | §2.5, after boxed result | Flowchart (single tree) | Medium |
| Fig 4.2.4 | Probability Current on the Membrane | §2.6, the continuity equation | Schematic + vector field | Medium |
| Fig 4.2.5 | Particle in a Box — Standing Waves of the Envelope | §2.7, example subsection | Schematic + energy-level diagram | Medium |

All five satisfy the figure rule: (1) spatial relationship (the membrane + envelope), (2) multi-step derivation (the tree), (3) conceptual model (rotating frame), (4) hierarchy (regimes), (5) canonical example (box).

## 7. Problem Sets (Foundations requires 3 tiers)

**Computational**

1. Starting from (1.5.1) with V_ext = 0 and plane-wave ansatz ψ ∝ e^{i(k·x − ωt)}, derive the dispersion ω² = c²k² and verify c² = σ/μ numerically.
2. Using E₀ = mc² with m = m_e = 9.109 × 10⁻³¹ kg and the derived ℏ = 1.0546 × 10⁻³⁴ J·s, compute the Compton angular frequency ω₀ = E₀/ℏ of the electron carrier. How many Compton oscillations occur per atomic-transition period (τ_atomic ≈ 10⁻¹⁵ s)?
3. For a Gaussian envelope Ψ(x,0) = (2πσ_x²)^(−1/4) exp(−x²/(4σ_x²)) propagating freely, compute the spreading σ_x(t) and show it grows as √(σ_x⁴ + (ℏt/2m)²)/σ_x.
4. For the particle-in-a-box of width L, compute the first three energy levels with L = η_B and m = m_e. Compare to the order of magnitude of nuclear-scale kinetic energies.
5. Verify dimensionally that [σ ∇² ψ] and [V_ext ψ] and [μ ψ_tt] are all force per unit volume, and that the envelope equation (time-dependent Schrödinger) has consistent units when ℏ is taken from (1.10.19).

**Conceptual**

6. Explain in one paragraph why the second time-derivative of the *envelope* is negligible even though the second time-derivative of the full membrane displacement is *not*.
7. Why must the wave function be complex? Frame the answer in terms of the carrier e^{−iE₀t/ℏ}. Would a purely real wave function be compatible with the envelope factorization?
8. The Schrödinger equation is first-order in time. The membrane equation is second-order. How can a second-order PDE produce a first-order envelope equation without losing degrees of freedom?
9. State Ehrenfest's theorem as a theorem about envelope moments. Why does it recover Hamilton's equations in the ℏ → 0 limit?

**Challenge**

10. Repeat the envelope derivation with the *negative*-frequency branch ψ = Ψ(x,t) e^{+imc²t/ℏ}. What equation do you get? What does it describe? (Hint: anti-particles.)
11. Suppose the stochastic Waters forcing ℱ(x,t) in (1.5.1) is reinstated. Show that, after averaging over sub-Planck timescales, it contributes a fluctuation-dissipation term of order η_B/ξ_A to the envelope equation. Explain why this correction is below current experimental sensitivity.
12. Take V_ext(x) to be a periodic lattice potential with period a. Show that the envelope equation admits Bloch-wave solutions and re-derive the standard band-theory dispersion relation. Relate the lattice spacing a to the Firmament structure.

## 8. Verification Criteria

A reviewer (especially The Physicist) must be able to confirm:

- [ ] Every line in §2.4 has a justification — either a dimensional identity, an algebraic step, or a cited Vol 1–3 equation.
- [ ] Nothing is ever used before it is introduced. Forward dependencies = 0.
- [ ] The final Schrödinger equation (4.2.central) is *derived*, not stated and then "motivated."
- [ ] The ℏ in the final equation is the same numerical constant from (1.10.19), verified in §2.2.
- [ ] The NR limit assumption is stated *explicitly* before it is used, with an order-of-magnitude justification.
- [ ] The first-order-in-time question (why did we lose a DOF?) is answered, not ducked.
- [ ] The complexity-of-ψ question (why i appears) is answered, not ducked.
- [ ] Probability conservation is demonstrated from the *real* membrane equation, not postulated.
- [ ] The classical limit (Vol 3 Ch 1–2) is recovered explicitly via Ehrenfest + ℏ → 0.
- [ ] Three sanity checks are performed: plane wave, free Gaussian, particle-in-a-box.
- [ ] Honest limitations (§2.8) are stated: stochastic Waters term dropped, relativistic corrections ignored, spin not addressed.
- [ ] Figure density 3–5 per chapter — we have 5.
- [ ] Problem sets have all three tiers.
- [ ] Word count within 15,000–18,000.
- [ ] Notation consistent with Series Bible and Vols 1–3 (ψ = full membrane; Ψ = envelope; ℏ, σ, μ, c, η_B, ξ_A canonical).
- [ ] Voice is Feynman-textbook: declarative, reasons first, unafraid of equations, one-paragraph asides in his timbre.
- [ ] Christ-as-answer sits in the margin, never on the page.

## 9. Research Files Used

- Primary: `Research/Mathematical_Models/05_Quantum_Mechanics/05-QM_FROM_MEMBRANE_DYNAMICS.md` — Parts I §1.3, II, III, IV.3
- Supporting: `Research/Foundations/TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md` — vortex mass identification
- Ch 1 of this volume — thesis, inherited architecture
- Vol 1 Ch 5, 6, 10 drafts — the cited results
- Vol 3 Ch 1, 2 drafts — classical limit target

## 10. Known Gaps Acknowledged (§2.8)

- **Stochastic Waters forcing ℱ(x,t) dropped** — justified by the scale argument (η_B/ξ_A)², but the full treatment is deferred to Ch 5.
- **Spin-½ not addressed** — the envelope scalar ψ describes bosonic excitations. The spin-½ BLOCKER (#1) is acknowledged and postponed to Ch 10.
- **Relativistic corrections (order v²/c²)** dropped in the NR limit — their recovery through the Dirac equation is the work of Vol 5, not Vol 4.
- **The Coulomb potential V(x) = −e²/r is used as an example only**; its own derivation from KK U(1) reduction is in Ch 7 of this volume. No circular dependency here — Ch 2 uses V(x) as a *slot*, and Ch 7 fills it.

No new gap is introduced.
