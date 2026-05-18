# Chapter 2 — Detailed Outline with Figure Plan

Target length: 15,000–18,000 words. Seven sections + problem sets.

---

## §2.0 Where This Chapter Fits (≈ 500 words)

- **Topic sentence:** Chapter 1 told you *why* the universe is quantum. This chapter shows *how* the first of the quantum postulates — the Schrödinger equation — falls out of the architecture as a theorem.
- **Why entry point:** Why should the envelope of a relativistic Firmament membrane wave be the object every graduate quantum course begins with?
- **Key content:**
  - One-paragraph recap of Ch 1's two architectural facts.
  - Statement of the target: derive the time-dependent Schrödinger equation line by line from (1.5.1), with no imports.
  - A promise: every step will be either a citation, an algebraic manipulation, or a dimensionally-justified approximation.
  - The Feynman-voice confession: when you first learn QM you are told "the Schrödinger equation is a postulate — do not ask where it comes from." Here, we ask.
- **Exit condition:** Reader knows the chapter's contract.

(No figure.)

---

## §2.1 The Target We Are Aiming At (≈ 900 words)

- **Topic sentence:** Before we derive a thing, write the target on the board and stare at it.
- **Why entry point:** Why is the Schrödinger equation the "right" target for the first chapter of dynamics?
- **Key content:**
  - Write the conventional Schrödinger equation as every textbook writes it:
    iℏ ∂_t Ψ = −(ℏ²/2m)∇²Ψ + V(x)Ψ
  - Identify seven things a conventional textbook leaves unjustified:
    1. Why ℏ appears at all.
    2. Why there is a factor of i.
    3. Why it is first-order in time.
    4. Why Ψ is complex.
    5. Why the kinetic term is −ℏ²/(2m).
    6. Why V(x) appears additively.
    7. Why any of this should be believed.
  - Promise: by the end of §2.5 every one of these will be either derived or inherited.
  - Brief note on the reader's prerequisites (Ch 1 + Vol 1 Ch 5, 6, 10).
- **Exit condition:** The reader has an equation to aim at and a scorecard of seven promises.

(No figure.)

---

## §2.2 Inheritance: What We Take From Vols 1–3 (≈ 1,500 words)

- **Topic sentence:** Four facts from Volumes 1–3 carry the entire weight of the derivation. Name them once, cite them once, and never import anything else.
- **Why entry point:** Why do we insist on restating the inheritance *before* touching new equations?
- **Key content:**

  **Inheritance 1 — The Firmament wave equation.** Vol 1 Ch 5 gave us
  μ ψ_tt = σ ∇²ψ − V_ext(x) ψ + ℱ(x,t)   (1.5.1)
  with c² = σ/μ. Restate the physical meaning of each symbol. Note explicitly that ψ is real — the Firmament membrane's transverse displacement — not complex.

  **Inheritance 2 — The derived ℏ.** Vol 1 Ch 10 §10.3 gave us
  ℏ = (σ η_B³/2c)(η_B/ξ_A)² β_geom = 1.0546 × 10⁻³⁴ J·s   (1.10.19)
  Restate the derivation in one paragraph; do not re-derive. From this chapter onward the symbol ℏ *means* this value.

  **Inheritance 3 — Topological defect mass.** Vol 3 Ch 6–7 established that a localized defect on the Firmament carries an effective rest energy E₀ = m c² where m is set by the defect's homotopy class and core energy. We will need this *identification* in §2.4.

  **Inheritance 4 — The relativistic dispersion for a massive localized mode.** From the linearized Firmament equation around a defect, Vol 1 Ch 5 Eq. (1.5.10) gave
  ω²(k) = c² k² + (m c²/ℏ)²
  where m is the defect mass. This is the Klein–Gordon dispersion; we did not have to assume it, because the topological defect's extra confinement term *provides* the mass gap.

  - Dimensional table: verify each of the four inherited quantities has the dimensions claimed.
  - Point out what we are explicitly *not* importing: probability, Hilbert space, Hermitian operators, commutation relations, the Born rule, Planck's postulate.
- **Exit condition:** Reader has the four inheritances in a box and knows nothing else will be imported.

(No figure.)

---

## §2.3 The Envelope Ansatz (≈ 2,200 words)

- **Topic sentence:** The trick — the single move that takes us from a relativistic membrane to non-relativistic quantum mechanics — is to separate the rest-energy oscillation from the slow variation.
- **Why entry point:** Why factor the wave into a "carrier" and an "envelope"?
- **Key content:**
  - The rest-energy oscillation problem. Write out ψ ∼ e^{−iE₀ t/ℏ} for E₀ = mc². For an electron, ω₀ = mc²/ℏ ≈ 7.8 × 10²⁰ rad/s. A second of lab time contains 10²¹ rotations of the carrier. Any laboratory measurement averages over ∼ 10²¹ such cycles. What we *see* is not ψ; it is the slow envelope.
  - The ansatz:
    ψ(x, t) = Ψ(x, t) · exp(−i E₀ t/ℏ),   E₀ = mc².
  - Two warnings:
    1. The envelope Ψ is not what the Firmament membrane displacement is. The Firmament membrane displacement is the *real part* of ψ. The envelope is a bookkeeping device for the slow modulation.
    2. The complex phase is introduced *here*, by hand, as a notational choice. The real content is the real and imaginary parts of Ψ, which together encode the two degrees of freedom of a real second-order wave (displacement and velocity).
  - Dimensional check: [Ψ] = [ψ] = length (transverse displacement).
  - Physical pictures:
    - Carrier: oscillation at the Compton frequency ω₀.
    - Envelope: slow spatial/temporal variation on the scale of the de Broglie wavelength.
  - **Insert Fig 4.2.1** — two-panel time series: top panel shows full ψ(t) oscillating at ω₀; bottom panel shows Ψ(t) envelope, much slower.
  - Take derivatives:
    ∂_t ψ = e^{−iE₀t/ℏ}[∂_t Ψ − (iE₀/ℏ)Ψ]
    ∂_t² ψ = e^{−iE₀t/ℏ}[∂_t² Ψ − (2iE₀/ℏ) ∂_t Ψ − (E₀²/ℏ²) Ψ]
    ∇² ψ = e^{−iE₀t/ℏ} ∇² Ψ
  - Careful algebra. This is the longest algebraic stretch of the chapter; do it slowly.

### Fig 4.2.1 — Rest-Energy Carrier and Slow Envelope

| Field | Spec |
|---|---|
| ID | Fig 4.2.1 |
| Title | The Carrier-Envelope Factorization |
| Placement | §2.3, after the ansatz is stated |
| Type | Two-panel time series |
| What it shows | Top panel: full ψ(t) at a fixed spatial point, oscillating at ω₀ = mc²/ℏ ≈ 7.8 × 10²⁰ rad/s. Bottom panel: slow envelope Ψ(t), varying on the atomic-transition timescale ∼ 10⁻¹⁵ s. The ratio of the two timescales is shown explicitly: "1 envelope cycle contains ∼ 10⁶ carrier cycles for an electron at atomic energies." Vertical dashed lines mark one carrier period. |
| Why needed | The central conceptual move of the derivation. Seeing the carrier-envelope separation makes the subsequent dropping of ∂_t² Ψ obvious. |
| Key labels | ψ, Ψ, ω₀, carrier period, envelope period |
| Equations referenced | (1.5.1), the ansatz line |
| Complexity | Medium |

---

## §2.4 The Non-Relativistic Limit (≈ 3,200 words)

- **Topic sentence:** Substitute the ansatz into the Firmament membrane equation and watch the Schrödinger equation appear — provided you are willing to drop one term, and only one, and provided you can say *honestly* why.
- **Why entry point:** Why is this approximation justified, and in what regime does it fail?
- **Key content:**
  - Substitution. Substitute the derivatives from §2.3 into μ ψ_tt = σ ∇²ψ − V_ext ψ. Cancel the common factor e^{−iE₀ t/ℏ}. Result:

    μ [∂_t² Ψ − (2iE₀/ℏ) ∂_t Ψ − (E₀²/ℏ²) Ψ] = σ ∇² Ψ − V_ext(x) Ψ

  - Parse each term by dimensional magnitude.
    - μ ∂_t² Ψ: envelope acceleration (slow).
    - μ (2iE₀/ℏ) ∂_t Ψ: first derivative, the dominant time term.
    - μ (E₀²/ℏ²) Ψ: the rest-energy term, which we will cancel against a piece of V_ext below.
    - σ ∇² Ψ: the spatial Laplacian.
    - V_ext Ψ: the external potential.
  - **The non-relativistic window.** Define ε = E − E₀ ≪ E₀ where E is the total energy of the envelope. Then ∂_t Ψ ∼ −(iε/ℏ) Ψ and ∂_t² Ψ ∼ −(ε²/ℏ²) Ψ. The ratio of the second-derivative term to the first-derivative term is

    |μ ∂_t² Ψ| / |(2iμE₀/ℏ) ∂_t Ψ| ∼ (ε²/ℏ²) / (2E₀ε/ℏ²) = ε/(2E₀).

    For an electron in a hydrogen atom, ε ∼ 13.6 eV and E₀ = 511 keV, so ε/(2E₀) ≈ 1.3 × 10⁻⁵. Dropping ∂_t² Ψ introduces errors at the part-in-10⁵ level.
  - **Insert Fig 4.2.2** — the non-relativistic window. Log–log plot of ε vs E₀ with two shaded regions: NR limit OK (below the diagonal) and relativistic corrections required (above).

### Fig 4.2.2 — The Non-Relativistic Window

| Field | Spec |
|---|---|
| ID | Fig 4.2.2 |
| Title | Where the Schrödinger Equation Is Valid |
| Placement | §2.4, just after the order-of-magnitude estimate |
| Type | Log–log regime plot |
| What it shows | Horizontal axis: rest energy E₀ (electron, proton, pion, etc.). Vertical axis: kinetic energy ε. Diagonal line ε = E₀ marks the boundary. Below the line: "Schrödinger valid (error ≤ ε/2E₀)." Above: "Relativistic corrections needed (Dirac, Klein–Gordon)." Dots for hydrogen ground state (ε ≈ 13.6 eV, E₀ ≈ 511 keV), chemical bonds, nuclear transitions, MeV-scale scattering. |
| Why needed | Shows the reader exactly where the derivation applies and where it breaks. Honest about the approximation's reach. |
| Key labels | E₀, ε, hydrogen, chemistry, nuclear, ε/(2E₀) |
| Equations referenced | The ε/(2E₀) error estimate |
| Complexity | Medium |

  - **Dropping the second derivative.** Now set ∂_t² Ψ ≈ 0 with the understanding that the error is of order ε/(2E₀). What remains:

    −(2iμE₀/ℏ) ∂_t Ψ − (μ E₀²/ℏ²) Ψ = σ ∇² Ψ − V_ext Ψ

  - **Identifying the mass gap term.** The (μ E₀²/ℏ²) Ψ term is the rest-energy piece of the Klein–Gordon operator. Using E₀ = mc² and c² = σ/μ:

    μ E₀²/ℏ² = μ m² c⁴/ℏ² = (μ c²) · m² c²/ℏ² = σ · m² c²/ℏ²

    The right-hand side already contains a σ ∇² Ψ. If we rewrite the mass-gap term as −σ · m² c²/ℏ² Ψ and move it to the right, we get

    −(2iμE₀/ℏ) ∂_t Ψ = σ ∇² Ψ − σ (m²c²/ℏ²) Ψ − V_ext Ψ

  - **Dividing by the coefficient.** Use E₀ = mc² once more and μ = σ/c²:

    2iμE₀/ℏ = 2i (σ/c²)(mc²)/ℏ = 2iσm/ℏ

    So the equation becomes

    −(2iσm/ℏ) ∂_t Ψ = σ ∇² Ψ − σ (m²c²/ℏ²) Ψ − V_ext Ψ

    Divide both sides by −2iσm/ℏ:

    ∂_t Ψ = (ℏ/(2iσm)) [σ ∇² Ψ − σ (m²c²/ℏ²) Ψ − V_ext Ψ]
          = (ℏ/(2im)) ∇² Ψ − (ℏ m c²/(2i m² c² · ... )) Ψ − (ℏ/(2iσm)) V_ext Ψ
    (careful algebraic step; show all work)

  - **The cancellation that produces ℏ²/2m.** Multiply top and bottom of the prefactor (ℏ/(2im)) by i/i to get (−iℏ/(2m)) (−1) = iℏ/(2m). Move iℏ to the left:

    iℏ ∂_t Ψ = −(ℏ²/(2m)) ∇² Ψ + (rest-energy piece) + (potential piece)

  - **The rest-energy piece vanishes or becomes a constant.** Because the envelope ansatz already *removed* the rest-energy oscillation, the surviving rest-energy piece is a constant shift and can be absorbed into the definition of energy — i.e. into the zero-point of V(x). We are about to show this in §2.5.
- **Exit condition:** The reader has a near-final equation, missing only the identification of V_ext with the physical V(x) and the cancellation of the rest-energy constant.

(No additional figure in this section beyond Fig 4.2.2.)

---

## §2.5 Identifying V(x) and the Final Schrödinger Equation (≈ 1,800 words)

- **Topic sentence:** The last step is the one everyone skips: show that V_ext(x) in the Firmament membrane equation and V(x) in the Schrödinger equation are *the same physical object*, differing only by a dimensional rescaling and a constant offset.
- **Key content:**
  - The constant rest-energy offset. Absorb m²c²σ/ℏ² into V_ext:
    V_physical(x) := V_ext(x) − σ · (m²c²/ℏ²)  (plus suitable factors)
    This is a redefinition, not a new assumption — it's the freedom to choose the zero of potential energy. For any localized defect, the constant offset is the rest mass; measured energies are differences.
  - Dimensional bookkeeping. [V_ext] = force/length² = N/m², [V_physical(x)·Ψ] in the Schrödinger equation must match [ℏ² ∇² Ψ/(2m)] = J. Check the conversion factor: V(x) = V_ext(x) / (surface density μ) → gives the standard V in J. Derive the conversion explicitly.
  - Conventional relabeling: call V_physical simply V(x). Then

    iℏ ∂_t Ψ = −(ℏ²/2m) ∇² Ψ + V(x) Ψ

    This is the **time-dependent Schrödinger equation**. Boxed as (4.2.1), the central result of the chapter.
  - **Insert Fig 4.2.3** — derivation tree. Every node in the tree is an equation; every edge is an operation (substitution, expansion, approximation, cancellation, relabeling). The reader can audit the entire derivation at a glance.

### Fig 4.2.3 — Derivation Tree: From (1.5.1) to the Schrödinger Equation

| Field | Spec |
|---|---|
| ID | Fig 4.2.3 |
| Title | Derivation Tree: (1.5.1) → Schrödinger |
| Placement | §2.5, directly after the boxed result (4.2.1) |
| Type | Single-tree flowchart |
| What it shows | Root: μ ψ_tt = σ ∇²ψ − V_ext ψ   (1.5.1). Branches downward through named steps: "[1] Plane-wave dispersion ω² = c²k² + (mc²/ℏ)²," "[2] Envelope ansatz ψ = Ψ e^{−iE₀t/ℏ}," "[3] Take ∂_t, ∂_t², ∇² of both sides," "[4] Substitute and cancel carrier," "[5] NR limit: drop ∂_t² Ψ (error ε/2E₀)," "[6] Absorb rest-energy into V_physical," "[7] Divide by −2iσm/ℏ, use μ=σ/c²," "[8] Relabel V_physical → V(x)." Leaf: iℏ ∂_t Ψ = −(ℏ²/2m)∇² Ψ + V(x) Ψ   (4.2.1). Arrows annotated with the assumption or identity used at each step. |
| Why needed | Lets a reviewer — or a student — audit the entire derivation in a single pass. |
| Key labels | Step numbers 1–8; the ansatz symbols; the final boxed equation. |
| Equations referenced | (1.5.1), (1.5.10), (1.10.19), (4.2.1) |
| Complexity | Medium |

  - **The scorecard from §2.1 revisited.** Walk through the seven unjustified things and mark each one resolved.
- **Exit condition:** The Schrödinger equation is on the page and every symbol in it has a genealogy.

---

## §2.6 Probability, Complexity, and the First-Order Mystery (≈ 2,300 words)

- **Topic sentence:** Three things about the boxed equation still look like magic: the factor of i, the first-order time derivative, and the idea that |Ψ|² is a probability density. None of them are magic.
- **Why entry point:** Why should a real membrane produce a complex envelope whose modulus-squared is a probability?
- **Key content:**
  - **Why i appears.** Trace i back to the envelope ansatz. The carrier e^{−iE₀t/ℏ} was introduced to absorb the rest-energy oscillation; i is built into the carrier; when you differentiate once, i comes out; when you divide through, i stays. The i in the Schrödinger equation is the *fingerprint* of the rotating frame.
  - **Why the envelope equation is first-order in time.** The full Firmament membrane equation is second-order, so it has two independent solutions for each mode: positive-frequency (e^{−iωt}) and negative-frequency (e^{+iωt}). The envelope ansatz picks out the positive-frequency branch. The negative-frequency branch is also a solution, and it gives *another* first-order Schrödinger equation with i → −i — the equation for antiparticles (anticipating Dirac in Vol 5). Total DOF count: 2 first-order equations ↔ 1 second-order equation. Nothing has been lost.
  - **Why Ψ is complex.** Ψ encodes both the slow amplitude and the slow phase of the real Firmament membrane displacement. Re(Ψ) is proportional to the in-phase slow amplitude; Im(Ψ) is proportional to the quadrature slow amplitude. Two real numbers = one complex number. No new degrees of freedom introduced.
  - **Probability conservation from the real Firmament membrane equation.** Multiply the Schrödinger equation by Ψ*, its complex conjugate by Ψ, subtract, and watch the continuity equation fall out:

    ∂_t |Ψ|² + ∇·J = 0,
    J = (ℏ/2im)[Ψ* ∇Ψ − Ψ ∇Ψ*]

  - Physical interpretation. |Ψ|² is *not* initially a probability density — it is the envelope energy density of the Firmament defect, in units of rest energy. But: for a single defect of fixed rest mass, the integral ∫|Ψ|² d³x is conserved and set by the defect's mass. Normalize to 1 and it is a probability density. The Born rule (derived properly in Ch 5) is the statement that this geometrically meaningful density *is* the probability of finding the defect at x.
  - Stationary states. Separate Ψ(x,t) = ψ(x) e^{−iEt/ℏ} to obtain the time-independent Schrödinger equation

    Ĥ ψ(x) = E ψ(x),   Ĥ = −(ℏ²/2m)∇² + V(x)

    An eigenvalue problem on a bounded domain with the Sturm–Liouville structure of Vol 1 Ch 10 → discrete spectrum when the domain is bounded (particle in a box, Ch 1 revisited), continuous spectrum when the domain is free (plane waves).
  - **Insert Fig 4.2.4** — probability current on the Firmament membrane. Two panels: left shows a Gaussian envelope translating; right shows the arrow field J(x) and the conservation law in action.

### Fig 4.2.4 — Probability Current on the Membrane

| Field | Spec |
|---|---|
| ID | Fig 4.2.4 |
| Title | Probability Current: The Envelope Continuity Equation |
| Placement | §2.6, after the continuity equation is derived |
| Type | Two-panel schematic + vector field |
| What it shows | Left panel: snapshot of a translating Gaussian |Ψ(x,t)|² on the Firmament, with the envelope indicated at t and t+Δt. Right panel: vector field J(x) pointing in the direction of motion, with ∂_t|Ψ|² and ∇·J annotated such that their sum is zero. Marginal text: "|Ψ|² is the envelope energy density of the defect; it is conserved because the Firmament equation is real." |
| Why needed | The continuity equation is the single most important consistency check of the chapter — if it fails, the envelope interpretation fails. |
| Key labels | |Ψ|², J, ∂_t, ∇· |
| Equations referenced | The continuity equation |
| Complexity | Medium |

- **Exit condition:** Reader knows why i, why first-order, why complex, and why |Ψ|² is conserved — all from the Firmament, no new postulates.

---

## §2.7 Sanity Checks and the Classical Limit (≈ 2,500 words)

- **Topic sentence:** A derivation is only as good as its sanity checks. Here are three, plus the ℏ → 0 recovery of Vol 3 classical mechanics.
- **Key content:**
  - **Sanity check 1: plane-wave free particle.** Set V(x) = 0 and try Ψ = A e^{i(k·x − Et/ℏ)}. Substitute. Recover E = ℏ²k²/2m: the non-relativistic kinetic energy. Group velocity v_g = dE/d(ℏk) = ℏk/m = p/m. The envelope propagates at the classical particle velocity. ✓
  - **Sanity check 2: Gaussian wave packet free propagation.** Compute the spreading rate from the dispersion. σ_x(t) = σ_x(0)√(1 + (ℏt/(2m σ_x²(0)))²). Plug in electron numbers: an electron localized to 1 nm spreads to ∼ 1 cm in a microsecond. Classical particles don't spread — the ℏ is responsible.
  - **Sanity check 3: particle in a box of width L.** The time-independent Schrödinger equation in a box with ψ(0) = ψ(L) = 0 is a Sturm–Liouville problem (cite (1.10.*)). Eigenstates ψ_n(x) = √(2/L) sin(nπx/L); eigenvalues E_n = ℏ²(nπ/L)²/(2m). Plug in L = η_B and m = m_e to get order-of-magnitude check (yields nuclear-scale energies, ∼100 MeV, confirming that confining an electron to η_B is hyper-relativistic and explains why atomic electrons have L ∼ Bohr radius, not η_B).
  - **Insert Fig 4.2.5** — particle in a box standing waves and their energy levels.

### Fig 4.2.5 — Particle in a Box: Standing Waves of the Envelope

| Field | Spec |
|---|---|
| ID | Fig 4.2.5 |
| Title | Particle in a Box — Envelope Standing Waves |
| Placement | §2.7, at the sanity-check subsection |
| Type | Schematic + energy-level diagram |
| What it shows | Left: a 1D box of width L with the first four eigenfunctions ψ_n(x) = √(2/L) sin(nπx/L), each offset vertically by its energy E_n = n² π² ℏ²/(2mL²). Right: corresponding energy ladder, with n = 1, 2, 3, 4 marked. Annotation: "Discrete spectrum: inherited from Sturm–Liouville on a bounded domain (Vol 1 Ch 10)." |
| Why needed | The canonical QM example, now *explained* rather than asserted. Shows continuity with Vol 1 Ch 10. |
| Key labels | L, ψ_n, E_n, n = 1..4 |
| Equations referenced | ψ_n and E_n formulas |
| Complexity | Medium |

  - **Ehrenfest's theorem.** Compute d⟨x⟩/dt = ⟨p⟩/m and d⟨p⟩/dt = −⟨∇V⟩ from the Schrödinger equation by differentiating under the integral and integrating by parts. These are Hamilton's equations for the envelope's centroid. So the envelope's mean position and momentum obey classical mechanics. ✓
  - **The ℏ → 0 limit.** Write Ψ = A(x,t) exp(iS(x,t)/ℏ) with A, S real (the WKB/ Madelung substitution). Substitute into the Schrödinger equation and expand in powers of ℏ. At leading order (ℏ⁰): the Hamilton–Jacobi equation

    ∂_t S + (∇S)²/(2m) + V(x) = 0

    which is exactly Vol 3 Eq. (3.1.*). At the next order, a continuity equation for A². So the classical mechanics of Vol 3 is recovered in the ℏ → 0 limit of the envelope equation. ✓
  - Commentary: ℏ → 0 doesn't mean ℏ becomes zero; it means ℏ is small compared to the typical action in the problem. For a baseball the typical action is ∼ 10³⁴ ℏ; for an electron in an atom it is ∼ ℏ. Classical mechanics works where ℏ is negligible; quantum mechanics where it is not. Same equation, different regime.
- **Exit condition:** Reader has three confirmations that the Schrödinger equation works, and has seen it reduce to the classical limit of Vol 3 explicitly.

---

## §2.8 Honest Limitations (≈ 900 words)

- **Topic sentence:** Four things we did not do, and why.
- **Key content:**
  1. **We dropped the stochastic Waters forcing ℱ(x,t).** The term is order (η_B/ξ_A)² smaller than V_ext for any laboratory-accessible energy, but it is not exactly zero. It will return in Ch 5 where it drives decoherence.
  2. **We used a *scalar* envelope.** Real particles have spin. The spin-½ electron cannot be written as a scalar. The derivation in this chapter is therefore strictly the Schrödinger equation for *bosonic* excitations — integer-spin defects. The spin-½ extension is BLOCKER #1 (GitHub issue #1) and has not yet been resolved from the bosonic membrane. Chapter 10 addresses the status of that open problem honestly. Nothing in the present chapter is invalid; it just doesn't cover fermions.
  3. **We dropped relativistic corrections of order ε/(2E₀).** For atomic electrons this is ∼ 10⁻⁵. For muonic atoms it is larger; for nuclear transitions it can be of order 1. The relativistic extension is the Klein–Gordon equation (which we have all the way back in §2.2) or the Dirac equation (which requires spin and is outside this chapter).
  4. **V(x) is treated as a slot to be filled by other chapters.** In this chapter V(x) is a generic external tension variation; its explicit form for particular problems (Coulomb, harmonic oscillator) is supplied in later chapters of this volume and in Vol 5 applications. No circular dependency — Ch 2 hands V(x) to Ch 7, Ch 7 computes it from U(1) KK reduction, and the two chapters meet cleanly.
- **Exit condition:** Reader cannot be surprised later by any of these four limitations.

(No figure.)

---

## §2.9 Chapter Summary and Traceability Table (≈ 700 words)

- **Topic sentence:** Before moving on, check the receipts.
- **Key content:**
  - The boxed Schrödinger equation (4.2.1).
  - A traceability table with two columns: every line in §2.4–§2.5, and the Vol 1 / Vol 3 equation or the algebraic justification backing it.
  - One-paragraph forward pointer to Ch 3 (the uncertainty principle), Ch 5 (the measurement problem), and Ch 6 (second quantization).
  - Closing Feynman-voice paragraph: "When we started, there was a list of seven unjustified things on the board. There is none now. The list is a theorem."
- **Exit condition:** The chapter is closed.

(No figure.)

---

## §2.10 Problem Sets (see SPEC §7)

- Three tiers: computational (5), conceptual (4), challenge (3) — 12 problems total.

---

## Outline Review Checklist

- [x] Every chapter requirement maps to at least one section (see SPEC §2).
- [x] No section uses concepts not yet established.
- [x] "Why" chain unbroken — six "but why?" questions answered across §2.4–§2.6.
- [x] Inheritance stated once, cited thereafter.
- [x] Figure plan complete — five figures spec'd.
- [x] Open problems explicit in §2.8 (spin, stochastic forcing, relativistic, V slot).
- [x] Problem sets have all three tiers.
- [x] Word-count budget sums to ≈ 16,500 words (within 15–18k target).
