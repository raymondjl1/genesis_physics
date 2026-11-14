# Expansion Ledger — Domain 02: Thermodynamics

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This ledger traces every displayed/numbered equation and named key result in
> `Research/Mathematical_Models/02_Thermodynamics/` back to the seed `1=1` via the
> derivation spine (`SPINE.md`, rungs S0–S9) plus named decrees (`DECREE_REGISTER.md`,
> D0–D6). Per the honesty rules in `README_SCHEMA.md`: **no equation is "derived from
> `1=1` alone"** — every physics equation = spine path + named decrees. Constants are
> tagged `[DERIVED ratio] / [SELECTED scale → D4] / [FIT → D5] / [count → D3]`.

## Header / coverage table

| Field | Value |
|-------|-------|
| **Domain** | Thermodynamics (folder `02_Thermodynamics`) |
| **Files traced** | `02-LAWS_DERIVATION.md`, `02-STATISTICAL_MECHANICS.md`, `02-COMPLETIONS.md`, `02-PLANCK_DISTRIBUTION.md`, `02-PLANCK_SPECTRUM_DERIVATION.md`, `02-PHASE_TRANSITIONS_MOLECULAR.md`, `02-WATERS_REPLENISHMENT.md`, `test_thermodynamic_laws.py`, `test_planck_spectrum.py`, `test_phase_transitions.py` |
| **# equations traced** | 63 (EQ-THERMO-01 … EQ-THERMO-63) |
| **Decrees used across domain** | D0 (completed infinity / ℝ), D1 (dimension / manifold), D2 (gauge group, for the EM/KK sector), D3 (integer counts: N, N_A, Ω, g₀, g_n, DOF/winding counts), D4 (scale anchor / all dimensionful constants), D5 (fitted O(1) constants: VdW a,b; β≈0.325; 68/27/5 split; T_CMB; g_s), D6 (architectural axioms: Ψ_A/Ψ_B, Firmament, κ sustaining, open system) |
| **# PARTIAL** | 4 (EQ-THERMO-48, 58, 59, 62) |
| **# UNTRACEABLE** | 4 (UNTRACEABLE-A … UNTRACEABLE-D) |

**Note on the test `.py` files:** they numerically *re-verify* equations already displayed in
the markdown (Boltzmann ratio, Carnot, C_p−C_v=R, Planck radiance, Stefan-Boltzmann σ, Wien b,
solar luminosity, Van der Waals critical point, Clausius-Clapeyron, restitution). They introduce
no *new* equations, so they are cited as secondary sources on the existing blocks rather than
given their own blocks — except the solar-luminosity relation (EQ-THERMO-44) and the CMB blackbody
temperature (EQ-THERMO-62), which are named in the `.py`/CMB sections and get their own blocks.

**Domain-wide standing dependencies (cited once here, not re-cited per term):**
- Every continuous/real-valued quantity silently uses **D0** (ℚ→ℝ, rung S3). Stated once per block via the spine path reaching S3+.
- Every dimensionful constant (ℏ, k_B, c, R, σ_SB, b, h, σ-tension, μ, λ, β, κ, m, g, G, T_CMB) is "1 in chosen units" ⇒ **[SELECTED scale → D4]**.
- ℏ, k_B, c are imported from companion membrane documents (`DERIVE_HBAR_FROM_MEMBRANE.md`, `DERIVE_KB_FROM_MEMBRANE.md`, `AXIOM_MEMBRANE_MECHANICS_v2.md`). Within this domain they are inputs anchored by **D4** + **D6** (membrane content); their *internal* derivation is out of scope for this ledger.

---

## Part A — The 6D action and the starting functional

### EQ-THERMO-01 — 6D total action (thermodynamics starting point)
- **Equation:** S_total = ∫ d⁶x √(−g₆) [ (M_Pl²/2)R₆ − ½g^{AB}∂_AΨ_A∂_BΨ_A − V(Ψ_A) − ½g^{AB}∂_AΨ_B∂_BΨ_B − ½M_B²Ψ_B² + S_κ ]
- **Source:** 02-LAWS_DERIVATION.md (Part 1.1, eq. for S_total, line 50)
- **Spine path:** S0→S1→S2→S3→S5→S6→S9
- **Decrees:** D0, D1 (6D manifold + metric), D6 (Ψ_A/Ψ_B field content, κ sustaining term)
- **Trace:** 1=1 → S1/S2 give the +,−,·,/ ring and ℚ → S3 (with D0) gives ℝ-valued fields → S5/S9 supply the 6D manifold, metric g_{AB}, curvature R₆ (D1 fixes dimension=6) → S6 gives the ∂_A operators and the ∫ (action functional). The specific field content Ψ_A, Ψ_B and the sustaining piece S_κ are **not** grammar — they are injected by **D6** (architectural axioms). δS=0 dynamics are S6-borderline.
- **Constants:** M_Pl [SELECTED scale → D4]; M_B (mass of Ψ_B) [SELECTED scale → D4]; metric/curvature carry D1.
- **Status:** DERIVED-as-form (given D1, D6); action principle is S6-borderline.

### EQ-THERMO-02 — 6D Einstein-Hilbert + gauge (Planck-sector) action
- **Equation:** S₆ = (1/16πG₆)∫ d⁶x √(−g₆) [ R₆ − ¼F^ξ_{μν}F^{μν}_ξ − ¼F^η_{μν}F^{μν}_η ] + S_matter^(6)
- **Source:** 02-PLANCK_DISTRIBUTION.md (Part 1.1, line 51); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 1.1, line 51)
- **Spine path:** S0→S1→S2→S3→S5→S7→S9
- **Decrees:** D0, D1 (6D manifold), D2 (gauge sector / U(1) KK fields), D6 (membrane content)
- **Trace:** Same grammar as EQ-THERMO-01 for R₆; S7 (identity-preserving maps) gives the gauge field strengths F = dA, with the *specific* U(1) KK gauge sectors selected by **D2**. The off-diagonal-metric origin of A^ξ, A^η is membrane content ⇒ **D6**.
- **Constants:** G₆ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

---

## Part B — Zeroth Law, equipartition, temperature

### EQ-THERMO-03 — Boltzmann entropy (microstate definition)
- **Equation:** S = k_B ln Ω
- **Source:** 02-LAWS_DERIVATION.md (Part 4.2, line 306); 02-COMPLETIONS.md (Part 6.1, line 456); 02-STATISTICAL_MECHANICS.md (Step 3, line 68)
- **Spine path:** S0→S1→S2→S3→S5
- **Decrees:** D0, D3 (Ω is an integer microstate count), D4 (k_B), D6 (Ω counts membrane-defect microstates)
- **Trace:** 1=1 → S1/S2 give counting (ℕ) and ratio → Ω is an integer count of microstates [count → D3]; the logarithm is an S3/ℝ map (with D0). k_B converts the dimensionless ln Ω into entropy units. That the microstates are *membrane defect configurations* is **D6** content; the magnitude scale of k_B is **D4**.
- **Constants:** k_B [SELECTED scale → D4]; Ω [count → D3] (integer microstate count, geometric/configurational).
- **Status:** DERIVED-given-decrees (D3, D4, D6).

### EQ-THERMO-04 — Temperature from entropy
- **Equation:** 1/T = (∂S/∂U)_{V,N} = k_B (∂ ln Ω/∂U)_{V,N}
- **Source:** 02-LAWS_DERIVATION.md (Part 2.2, line 128)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4 (k_B), D6 (U is membrane-defect energy)
- **Trace:** Definition built from EQ-THERMO-03 by the S6 derivative ∂/∂U. T emerges as the reciprocal slope of S(U). Dimensionful via k_B (D4).
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-05 — Zeroth Law / thermal-equilibrium condition
- **Equation:** ∂(Ω₁Ω₂)/∂U₁ = 0 ⇒ Ω₁'/Ω₁ = Ω₂'/Ω₂ ⇒ T₁ = T₂
- **Source:** 02-LAWS_DERIVATION.md (Part 2.2, lines 140–143)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4, D6
- **Trace:** Multiplicities multiply (S2, independent subsystems); S6 stationarity (∂/∂U₁ = 0) of the product Ω₁Ω₂ at fixed total energy forces equal logarithmic slopes, i.e. equal T (via EQ-THERMO-04). The Zeroth Law is the maximization of total multiplicity.
- **Constants:** none new (k_B cancels).
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-06 — Equipartition (½k_BT per quadratic DOF)
- **Equation:** ⟨E⟩ = ½k_BT per quadratic DOF; ⟨E_total⟩ = (d/2)k_BT
- **Source:** 02-LAWS_DERIVATION.md (Part 2.3, line 159); 02-COMPLETIONS.md (Part 4.2, line 338)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D3 (d is an integer DOF count), D4 (k_B)
- **Trace:** 1=1 → ℝ continuum (S3) → the Gaussian integral ∫e^{−aq²/2k_BT}dq (S6 integration over an ℝ coordinate) gives z ∝ √(k_BT/a); ⟨E⟩ = −∂ln z/∂β = ½k_BT. The count d of quadratic DOFs is an integer [count → D3] (geometric/structural — 3 trans, +2 rot, …), not a free fit.
- **Constants:** k_B [SELECTED scale → D4]; d [count → D3] (geometric DOF count).
- **Status:** DERIVED-given-decrees (D3, D4).

---

## Part C — First Law (Noether) and conservation

### EQ-THERMO-07 — Stress-energy / Noether conservation
- **Equation:** ∂_μ T^μ_ν = 0 (and ∇_μ T^μ_0 = 0)
- **Source:** 02-LAWS_DERIVATION.md (Part 3.2, lines 202, 208)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1 (a spacetime to translate in)
- **Trace:** Identical to the canonical worked example EQ-FND-01: S1 gives the additive "books-balance" conservation form a+(−a)=0; S6 supplies ∂_μ; S7 (Noether) ties time-translation symmetry of the action to a conserved current; for the energy-momentum tensor this is ∂_μT^μ_ν=0. Only non-grammar input is D1 (existence of the manifold).
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-THERMO-08 — First Law of thermodynamics
- **Equation:** dU = δQ − δW
- **Source:** 02-LAWS_DERIVATION.md (Part 3.1/3.2, lines 177, 220); 02-COMPLETIONS.md (Part 9.3, line 679)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D6 (U, Q, W defined on the membrane/zone system)
- **Trace:** Integrate the Noether conservation EQ-THERMO-07 over a volume V; the boundary energy flux splits into heat exchange (δQ) and mechanical work (δW), giving dU = δQ − δW. The split into "heat" vs "work" channels is physical-content bookkeeping (D6) on top of the grammar.
- **Constants:** none new dimensionful (U, Q, W carry D4 via their energy units).
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-THERMO-09 — Extended (open-system) First Law with sustaining input
- **Equation:** dU = δQ − δW + δE_κ,  δE_κ = ∫_{Zone2} d³x κ(t)J(x)dt
- **Source:** 02-LAWS_DERIVATION.md (Part 3.4, lines 274, 277); 02-WATERS_REPLENISHMENT.md (eq. 2.1, line 179)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D6 (κ sustaining field, Zone boundary, open-system axiom)
- **Trace:** EQ-THERMO-08 plus an explicit external source term δE_κ. The sustaining coupling κ, the source distribution J, and the open-system framing are **entirely D6 content** (AXIOM_OPEN_SYSTEM, AXIOM_SUSTAINING_COUPLING). Not forced by grammar.
- **Constants:** κ(t) [SELECTED scale → D4, magnitude]; J(x) geometric source [D6].
- **Status:** DERIVED-given-decrees (D1, D6).

### EQ-THERMO-10 — Fundamental thermodynamic relation
- **Equation:** dU = T dS − P dV + μ dN
- **Source:** 02-STATISTICAL_MECHANICS.md (Step 6, line 113); 02-COMPLETIONS.md (Part 3.2)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** Combine First Law (EQ-THERMO-08) with dS = δQ_rev/T (EQ-THERMO-16) and the work term P dV plus chemical-potential term μ dN; each conjugate pair (T,S),(P,V),(μ,N) is an S6 differential pairing on the ℝ state space.
- **Constants:** T, P, μ dimensionful [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

---

## Part D — Second Law, entropy, Liouville

### EQ-THERMO-11 — Liouville equation
- **Equation:** ∂ρ/∂t + {ρ, H} = 0
- **Source:** 02-STATISTICAL_MECHANICS.md (Step 1, line 45)
- **Spine path:** S0→S1→S2→S3→S6→S7
- **Decrees:** D0, D1 (6D phase space)
- **Trace:** Phase-space density ρ(X,P,t) on the ℝ continuum (S3); the Poisson bracket {·,·} and Hamiltonian flow are S6/S7 structure (symplectic/Hamiltonian maps preserve the identity of the measure). D1 supplies the 6D (X,P) coordinates.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-THERMO-12 — Liouville theorem (phase-space volume conservation)
- **Equation:** dΩ/dt = 0,  Ω = ∫ d⁶X d⁶P ρ
- **Source:** 02-STATISTICAL_MECHANICS.md (Step 2, lines 53–62)
- **Spine path:** S0→S1→S2→S3→S6→S7
- **Decrees:** D0, D1
- **Trace:** From EQ-THERMO-11; the cross partials ∂²H/∂X∂P − ∂²H/∂P∂X cancel (S6 mixed-derivative equality), giving incompressible Hamiltonian flow. Pure grammar + D1.
- **Constants:** none.
- **Status:** DERIVED-as-form (given D1).

### EQ-THERMO-13 — Accessible-phase-space entropy
- **Equation:** S = k_B ln Ω_accessible,  Ω_accessible = ∫_{H≤E} d⁶X d⁶P
- **Source:** 02-STATISTICAL_MECHANICS.md (Step 3, lines 68, 73)
- **Spine path:** S0→S1→S2→S3→S5→S6
- **Decrees:** D0, D1, D4 (k_B)
- **Trace:** Specialization of EQ-THERMO-03 to a continuous 6D phase space; the accessible volume is the S6 integral over the energy shell H≤E (D1 supplies dimension).
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-14 — Second Law (ΔS ≥ 0)
- **Equation:** ΔS = S_f − S_i ≥ 0
- **Source:** 02-STATISTICAL_MECHANICS.md (Step 4, line 87); 02-LAWS_DERIVATION.md (Part 4.1, line 293); 02-COMPLETIONS.md (Part 6.4, line 493)
- **Spine path:** S0→S1→S2→S3→S5→S6
- **Decrees:** D0, D1, D4, D6 (microstates = membrane-defect configs; phase-dependence via κ)
- **Trace:** When two subsystems are coupled, accessible phase space grows (Ω_final ≥ Ω_A·Ω_B), so k_B ln Ω increases (EQ-THERMO-13). The combinatorial growth is grammar (S2 counting + S6 measure); the *physical* claim that real systems explore the larger space is D6 content. **Honesty note:** in this framework dS/dt≥0 is *phase-dependent* (Phase 3 only) — see EQ-THERMO-22; the universality is conditioned on κ=κ_partial (D6).
- **Constants:** k_B [SELECTED scale → D4]; Ω-ratios [DERIVED ratio / count].
- **Status:** DERIVED-given-decrees (D1, D4, D6).

### EQ-THERMO-15 — Irreversibility probability bound
- **Equation:** P(ΔS<0) ∼ exp(−N|ΔS|/k_B) ∼ 10^{−10^{23}}
- **Source:** 02-STATISTICAL_MECHANICS.md (Step 5, line 98); 02-LAWS_DERIVATION.md (Part 4.2, line 339)
- **Spine path:** S0→S1→S2→S3→S5
- **Decrees:** D0, D4 (k_B), D3 (N as a particle count, e.g. N_A)
- **Trace:** Ratio of microstate counts (S2) exponentiated over N degrees of freedom; N≈N_A is an integer count [count → D3]. Pure combinatorics once Ω is defined.
- **Constants:** k_B [SELECTED scale → D4]; N [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-16 — Clausius equality/inequality (entropy–heat)
- **Equation:** dS = δQ/T (reversible); dS > δQ/T (irreversible); dS ≥ δQ/T
- **Source:** 02-STATISTICAL_MECHANICS.md (Step 6, lines 105–108); 02-LAWS_DERIVATION.md (Part 4.1, line 298); 02-COMPLETIONS.md (Part 6.5)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4 (T scale)
- **Trace:** From EQ-THERMO-04 (1/T = ∂S/∂U) applied to a heat exchange δQ at temperature T; reversibility gives equality, irreversible entropy generation gives the inequality (EQ-THERMO-14).
- **Constants:** T [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-17 — Gibbs free energy minimization
- **Equation:** dG = dU − d(TS) + d(PV) = μ dN ≤ 0
- **Source:** 02-STATISTICAL_MECHANICS.md (Step 6, line 118)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** Legendre transform (S6 algebra) of U into G = U − TS + PV; the Second Law (EQ-THERMO-14) at fixed T,P forces dG ≤ 0.
- **Constants:** T,P,μ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-18 — Clausius cyclic inequality
- **Equation:** ∮ δQ/T ≤ 0 (= 0 reversible)
- **Source:** 02-STATISTICAL_MECHANICS.md (Carnot, line 435)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** Integrate EQ-THERMO-16 around a closed cycle (S6 line integral); equality iff every step reversible.
- **Constants:** T [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

---

## Part E — Phase-dependent κ-mechanism (Genesis-specific Second Law)

### EQ-THERMO-19 — Phase-2 effective Hamiltonian (sustained)
- **Equation:** H_{Phase2} = H_kinetic + V_particle − κ_full · V_sustain(p₁,…,p_N)
- **Source:** 02-LAWS_DERIVATION.md (Part 4.3, line 356)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4, D6 (κ sustaining potential)
- **Trace:** Grammar supplies an additive Hamiltonian (S1 sum); the sustaining term −κ_full·V_sustain is **pure D6 content** (sustaining-coupling axiom). Not forced.
- **Constants:** κ_full [SELECTED scale → D4]; V_sustain [D6 form].
- **Status:** DERIVED-given-decrees (D6).

### EQ-THERMO-20 — Phase-2 entropy stasis
- **Equation:** dΩ/dt|_{Phase2} = 0 ⇒ dS/dt|_{Phase2} = 0
- **Source:** 02-LAWS_DERIVATION.md (Part 4.3, line 368)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4, D6
- **Trace:** Under EQ-THERMO-19 the accessible microstate set is constrained, so multiplicity is constant ⇒ entropy constant. The constraint mechanism is D6. **Honesty:** this is a *prediction of the axiom set*, not a grammar consequence.
- **Constants:** none new.
- **Status:** DERIVED-given-decrees (D6).

### EQ-THERMO-21 — Phase-3 effective Hamiltonian (Fall)
- **Equation:** H_{Phase3} = H_kinetic + V_particle − κ_partial · V_sustain,  Δκ = κ_full − κ_partial
- **Source:** 02-LAWS_DERIVATION.md (Part 4.3, line 376)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4, D6
- **Trace:** As EQ-THERMO-19 with the reduced coupling κ_partial. The drop κ_full→κ_partial at the Fall is a decreed phase transition (D6, AXIOM_PHASE_TRANSITION_FALL).
- **Constants:** κ_partial, Δκ [SELECTED scale → D4]; κ-ratio Δκ/κ_full is an O(1) **[FIT → D5]** (constrained ~10⁻²⁷ from decay data).
- **Status:** DERIVED-given-decrees (D6); ratio is D5.

### EQ-THERMO-22 — Entropy production rate ∝ coupling deficit
- **Equation:** dS/dt|_{Phase3} = ρ(κ_full − κ_partial) = ρ Δκ;  dS/dt = L Δκ (linear response)
- **Source:** 02-LAWS_DERIVATION.md (Part 4.3/7.3, lines 398, 425, 435, 773)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4, D6
- **Trace:** Linear-response expansion (S6 derivative) of EQ-THERMO-14 in the small parameter Δκ; the proportionality "entropy production ∝ sustaining deficit" is the central D6-driven claim. ρ / L are effective conductances.
- **Constants:** ρ, L [SELECTED scale → D4]; Δκ [SELECTED scale → D4]; the "const" prefactor [FIT → D5].
- **Status:** DERIVED-given-decrees (D6); UNRATIFIED phase-dependence.

### EQ-THERMO-23 — Entropy jump at the Fall
- **Equation:** ΔS_jump = k_B ln(Ω_{Phase3}/Ω_{Phase2})
- **Source:** 02-LAWS_DERIVATION.md (Part 7.4, line 805)
- **Spine path:** S0→S1→S2→S3→S5
- **Decrees:** D0, D4, D6
- **Trace:** Difference of two Boltzmann entropies (EQ-THERMO-03) across the decreed Phase-2→Phase-3 transition (D6). Ratio of microstate counts is geometric/combinatorial.
- **Constants:** k_B [SELECTED scale → D4]; Ω-ratio [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D6).

---

## Part F — Third Law

### EQ-THERMO-24 — Bose-Einstein / Fermi-Dirac occupation
- **Equation:** ⟨n⟩_B = 1/(e^{(E−μ)/k_BT} − 1);  ⟨n⟩_F = 1/(e^{(E−μ)/k_BT} + 1)
- **Source:** 02-LAWS_DERIVATION.md (Part 5.2, lines 490, 493; Part 6.4, lines 670, 673); 02-COMPLETIONS.md (Part 5.2, line 403)
- **Spine path:** S0→S1→S2→S3→S6→S7→S8
- **Decrees:** D0, D4, D6 (defect = particle), and topology/spin (S8) for ±1 sign
- **Trace:** Geometric-series sum of Boltzmann factors per mode (S2/S6, see EQ-THERMO-31); the ±1 (Bose vs Fermi) comes from exchange phase = +1 (even winding) or −1 (odd winding), an S8 winding/index invariant. The framework derives the sign from vortex-core topology (D6 membrane content + S8). μ, T carry D4.
- **Constants:** k_B [SELECTED scale → D4]; the ±1 sign [DERIVED ratio via S8 winding parity].
- **Status:** DERIVED-given-decrees (D4, D6).

### EQ-THERMO-25 — Single-mode binary entropy
- **Equation:** S_n = −k_B⟨n⟩ln⟨n⟩ − k_B(1−⟨n⟩)ln(1−⟨n⟩)
- **Source:** 02-LAWS_DERIVATION.md (Part 5.2, line 502)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** Shannon/Gibbs entropy (EQ-THERMO-30) specialized to a two-state (occupied/empty) mode; vanishes at ⟨n⟩∈{0,1}.
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-26 — Third Law (entropy → constant at T→0)
- **Equation:** lim_{T→0} S(T) = S₀;  S₀ = 0 (non-degenerate), S₀ = k_B ln g₀ (degenerate)
- **Source:** 02-LAWS_DERIVATION.md (Part 5.1/5.2, lines 472, 513, 517); 02-STATISTICAL_MECHANICS.md (Test 2.4, lines 140, 184); 02-COMPLETIONS.md (Part 7.2, line 526)
- **Spine path:** S0→S1→S2→S3→S5→S6
- **Decrees:** D0, D3 (g₀ is an integer degeneracy count), D4, D6 (modes = Firmament quantized oscillations)
- **Trace:** As T→0 all occupations freeze to 0 or 1 (EQ-THERMO-24); each mode's binary entropy (EQ-THERMO-25)→0; summing, S→0 unless the ground state is g₀-fold degenerate, giving S₀ = k_B ln g₀. Ground-state degeneracy g₀ is an integer [count → D3].
- **Constants:** k_B [SELECTED scale → D4]; g₀ [count → D3] (integer ground-state degeneracy).
- **Status:** DERIVED-given-decrees (D3, D4, D6).

### EQ-THERMO-27 — Debye low-T entropy / heat-capacity law
- **Equation:** S(T) ≈ (4π⁴/5)Nk_B (T/Θ_D)³;  C_V ≈ (12π⁴/5)Nk_B(T/Θ_D)³ ∝ T³
- **Source:** 02-LAWS_DERIVATION.md (Part 5.2, line 530); 02-STATISTICAL_MECHANICS.md (Test 2.5 Step 5, line 269); 02-COMPLETIONS.md (Part 7.3, line 550)
- **Spine path:** S0→S1→S2→S3→S5→S6
- **Decrees:** D0, D1 (d=3 mode-counting), D3 (N particle count), D4, D6
- **Trace:** Density of states g(ω) ∝ ω² for the 3D linear (acoustic) dispersion ω=c_s|k| (S5 mode-counting in d=3, requiring D1, see EQ-THERMO-39 family); integrating the Bose energy over modes and differentiating gives the T³ law. The π⁴/15-type factors are pure ℝ-integral constants [DERIVED ratio]. N [count → D3]; Θ_D [SELECTED scale → D4].
- **Constants:** k_B, Θ_D [SELECTED scale → D4]; N [count → D3]; numeric 12π⁴/5 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D1, D3, D4, D6).

### EQ-THERMO-28 — Heat capacity vanishes / unattainability of T=0
- **Equation:** C_V(T)→0 as T→0;  ∫₀^{T₀} dT/C_V = ∞ (absolute zero unattainable)
- **Source:** 02-STATISTICAL_MECHANICS.md (Test 2.4 Steps 2–3, lines 158, 168, 172); 02-COMPLETIONS.md (Part 7.5, line 575)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** From the partition-function heat capacity (EQ-THERMO-34) with a gapped spectrum, ∂ln Z/∂T→0 exponentially; the divergent cooling integral follows from C_V→0 (S6 integral).
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

---

## Part G — Boltzmann distribution & partition function

### EQ-THERMO-29 — Boltzmann distribution
- **Equation:** P_n = e^{−E_n/k_BT}/Z,  Z = Σ_n e^{−E_n/k_BT} (with degeneracy: P = g_n e^{−E_n/k_BT}/Z)
- **Source:** 02-LAWS_DERIVATION.md (Part 6.1, lines 544, 576, 608); 02-STATISTICAL_MECHANICS.md (Test 2.11, line 489); 02-COMPLETIONS.md (Part 8.2, line 614); test_thermodynamic_laws.py (BoltzmannDistributionTest)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D3 (g_n degeneracy count), D4 (k_B/T)
- **Trace:** Maximize Gibbs entropy S=−k_BΣp_n ln p_n (EQ-THERMO-30) subject to Σp_n=1 and ⟨E⟩=U using Lagrange multipliers (S6 variation δS/δp_n=0); the multiplier λ₂ is identified with 1/k_BT by EQ-THERMO-04. Equivalent bath-counting derivation gives the same form. The exponential e^{·} is S4 content (analytic function on ℝ). The level degeneracy g_n is an integer [count → D3].
- **Constants:** k_B [SELECTED scale → D4]; g_n [count → D3] (integer level degeneracy).
- **Status:** DERIVED-given-decrees (D3, D4).

### EQ-THERMO-30 — Gibbs/Shannon entropy
- **Equation:** S = −k_B Σ_n p_n ln p_n
- **Source:** 02-LAWS_DERIVATION.md (Part 6.1, line 558); 02-STATISTICAL_MECHANICS.md (line 475); 02-WATERS_REPLENISHMENT.md (line 1030)
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D0, D4 (k_B)
- **Trace:** The −Σp ln p functional is the unique (up to k_B scale) additive measure of a probability distribution consistent with S2 (multiplicativity of independent multiplicities ⇒ additivity of ln). Reduces to EQ-THERMO-03 for a uniform distribution.
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (D4).

### EQ-THERMO-31 — Single-mode (harmonic-oscillator) partition function
- **Equation:** Z₁ = e^{−βℏω/2}/(1 − e^{−βℏω}) = 1/[2 sinh(βℏω/2)],  β=1/k_BT
- **Source:** 02-LAWS_DERIVATION.md (Part 6.3, lines 645, 648); 02-PLANCK_DISTRIBUTION.md (Part 3.1, line 179); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 4.2, line 230)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4 (ℏ, k_B), D6 (mode = Firmament oscillator)
- **Trace:** Sum the geometric series Σ_n e^{−βℏω(n+½)} (S2 ratio + S1 sum); E_n = ℏω(n+½) is the quantized oscillator spectrum (D6 membrane mode, ℏ from companion doc).
- **Constants:** ℏ, k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (D4, D6).

### EQ-THERMO-32 — Mean oscillator energy (Planck form)
- **Equation:** ⟨E⟩ = ℏω/2 + ℏω/(e^{βℏω} − 1);  classical limit ⟨E⟩→k_BT; quantum limit →ℏω/2
- **Source:** 02-LAWS_DERIVATION.md (Part 6.3, lines 651, 656, 661); 02-COMPLETIONS.md (Part 4.4, line 362); test_thermodynamic_laws.py
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4, D6
- **Trace:** ⟨E⟩ = −∂ln Z₁/∂β applied to EQ-THERMO-31 (S6 derivative). Limits follow by expanding the exponential.
- **Constants:** ℏ, k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-33 — Internal energy from Z
- **Equation:** U = −∂ln Z/∂β = k_BT² ∂ln Z/∂T
- **Source:** 02-LAWS_DERIVATION.md (Part 6.2, line 624); 02-STATISTICAL_MECHANICS.md (Test 2.5 Step 2, line 212); 02-COMPLETIONS.md (Part 8.3, line 625)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** Differentiate ln Z (S6) with respect to β=1/k_BT; the weighted energy average emerges directly from EQ-THERMO-29.
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-34 — Heat capacity from Z
- **Equation:** C_V = k_B β² ∂²ln Z/∂β² = (⟨E²⟩−⟨E⟩²)/k_BT² = k_B(T ∂²ln Z/∂T² + 2∂ln Z/∂T)
- **Source:** 02-LAWS_DERIVATION.md (Part 6.2, line 627); 02-STATISTICAL_MECHANICS.md (Test 2.5, lines 217, 220)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** Second β-derivative of ln Z (S6); equals the energy variance — a fluctuation–response identity.
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-35 — Thermodynamic potentials from Z (S, F, P)
- **Equation:** S = k_B ln Z + U/T;  F = U − TS = −k_BT ln Z;  P = −(∂F/∂V)_T = k_BT ∂ln Z/∂V
- **Source:** 02-LAWS_DERIVATION.md (Part 6.2, lines 630, 633, 636); 02-COMPLETIONS.md (Part 8.3, lines 631, 634)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** Standard Legendre/derivative relations (S6) once Z is known (EQ-THERMO-29/31). All macroscopic thermodynamics reduces to derivatives of ln Z.
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

---

## Part H — Ideal gas, heat capacities, transport (COMPLETIONS)

### EQ-THERMO-36 — Single-particle partition function (thermal wavelength)
- **Equation:** z = (mk_BT/2πℏ²)^{3/2} V = V/λ_T³,  λ_T = h/√(2πmk_BT)
- **Source:** 02-COMPLETIONS.md (Part 1.1, lines 70, 74)
- **Spine path:** S0→S1→S2→S3→S5→S6
- **Decrees:** D0, D4 (ℏ,k_B), D1 (3D box)
- **Trace:** Classical limit of the box-mode sum → Gaussian integral over 3 momentum directions (S6, three factors from S5 independent directions). Quantum scale set by ℏ (D4).
- **Constants:** ℏ,k_B [SELECTED scale → D4]; exponent 3/2 [DERIVED ratio — from d=3].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-37 — N-particle free energy (Stirling)
- **Equation:** Z_N = z^N/N!;  F = −Nk_BT ln(Ve/Nλ_T³)
- **Source:** 02-COMPLETIONS.md (Part 1.2, lines 82, 95)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D3 (N particle count), D4
- **Trace:** Indistinguishability factor 1/N! (S2 counting, Gibbs paradox); F = −k_BT ln Z_N with Stirling ln N!≈N ln N − N (S6 asymptotics). N is an integer particle count [count → D3].
- **Constants:** k_B [SELECTED scale → D4]; N [count → D3].
- **Status:** DERIVED-given-decrees (D3, D4).

### EQ-THERMO-38 — Ideal gas law
- **Equation:** PV = Nk_BT  ⇒  PV = nRT
- **Source:** 02-COMPLETIONS.md (Part 1.3, lines 109, 113); 02-PHASE_TRANSITIONS_MOLECULAR.md (line 46); test_thermodynamic_laws.py (constants)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D3 (N, N_A counts), D4
- **Trace:** P = −(∂F/∂V)_T applied to EQ-THERMO-37 (S6); ∂ln V/∂V = 1/V gives PV = Nk_BT. R = k_B N_A repackages per-mole (N_A [count → D3]).
- **Constants:** k_B, R [SELECTED scale → D4]; N_A [count → D3].
- **Status:** DERIVED-given-decrees (D3, D4).

### EQ-THERMO-39 — Monatomic / polyatomic specific heats
- **Equation:** C_V = (3/2)nR (monatomic); (5/2)nR (diatomic); 3nR (Dulong–Petit / polyatomic high-T); U = (3/2)Nk_BT
- **Source:** 02-STATISTICAL_MECHANICS.md (Test 2.5 Steps 3–4, lines 229, 233, 247, 251); 02-COMPLETIONS.md (Part 4.3, lines 348, 354)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D3 (DOF/particle counts), D4
- **Trace:** Equipartition (EQ-THERMO-06) × number of active quadratic DOF (3,5,6…); C_V = ∂U/∂T. The DOF counts are geometric/structural integers [count → D3], not fits.
- **Constants:** R [SELECTED scale → D4]; DOF count [count → D3]; 3/2,5/2,3 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D3, D4).

### EQ-THERMO-40 — C_p − C_v = R
- **Equation:** C_P − C_V = T(∂P/∂T)_V(∂V/∂T)_P = −T(∂P/∂V)_T(∂V/∂T)_P²;  for ideal gas C_P − C_V = nR (=R per mole)
- **Source:** 02-STATISTICAL_MECHANICS.md (Test 2.12, lines 581, 591, 606, 609); 02-COMPLETIONS.md (Part 3.3, lines 261, 278); test_thermodynamic_laws.py (HeatCapacityTest)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** Maxwell relation (∂S/∂V)_T=(∂P/∂T)_V (S6 cross-derivative of a potential) + cyclic chain rule, then the ideal-gas EOS (EQ-THERMO-38) reduces the RHS to nR.
- **Constants:** R [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-41 — Carnot efficiency
- **Equation:** η_Carnot = 1 − Q_C/Q_H = 1 − T_C/T_H
- **Source:** 02-STATISTICAL_MECHANICS.md (Test 2.7, line 428); 02-COMPLETIONS.md (Part 2.4, line 198); test_thermodynamic_laws.py (CarnotEfficiencyTest)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4 (T scale)
- **Trace:** For a reversible cycle ΔS_cycle=0 (EQ-THERMO-18) forces Q_H/T_H = Q_C/T_C; the isothermal heats are nRT ln(V_ratio) (from EQ-THERMO-38) and the adiabatic volume relation T V^{γ−1}=const makes the log-ratios cancel, giving η = 1 − T_C/T_H. Dimensionless ratio.
- **Constants:** none dimensionless-final; T's [SELECTED scale → D4] cancel into a ratio [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-42 — Fourier's law / phonon thermal conductivity
- **Equation:** q = −κ∇T,  κ = (1/3)C_v v_s λ
- **Source:** 02-COMPLETIONS.md (Part 5.3, lines 422, 444)
- **Spine path:** S0→S1→S2→S3→S6→S8
- **Decrees:** D0, D4, D6 (phonon = quantized Firmament wave)
- **Trace:** Kinetic-theory closure: heat flux = (energy/mode)(group velocity)(occupation) summed over modes (EQ-THERMO-24), linearized in ∇T. The phonon spectrum is membrane content (D6); the 1/3 is the geometric directional average [DERIVED ratio].
- **Constants:** κ, v_s, λ, C_v [SELECTED scale → D4]; 1/3 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D4, D6).

### EQ-THERMO-43 — Calorimetry / specific heat
- **Equation:** δQ = mc dT  ⇒  Q = mcΔT;  Q_hot + Q_cold = 0;  T_final = (m_h T_h + m_c T_c)/(m_h+m_c)
- **Source:** 02-COMPLETIONS.md (Part 9, lines 674, 691, 716, 723)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** First Law (EQ-THERMO-08) at constant V/P with U(T) linear ⇒ dU = mc dT; integration (S6) gives Q = mcΔT; energy conservation in an isolated calorimeter gives the mixing temperature.
- **Constants:** c (specific heat) [SELECTED scale → D4]; m [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-44 — Solar luminosity (Stefan-Boltzmann application)
- **Equation:** L_sun = 4πR²σ_SB T⁴
- **Source:** 02-PLANCK_SPECTRUM_DERIVATION.md (Part 9.3, line 550); 02-PLANCK_DISTRIBUTION.md (Part 9 table); test_planck_spectrum.py (SolarLuminosityTest)
- **Spine path:** S0→S1→S2→S3→S5→S6
- **Decrees:** D0, D1 (3D space ⇒ 4πR² sphere geometry), D4 (σ_SB, R, T)
- **Trace:** Stefan-Boltzmann flux (EQ-THERMO-49) × spherical surface area 4πR² (S5 geometry; the 2-sphere area in flat 3-space requires the d=3 manifold ⇒ D1). R_sun, T_sun are measured inputs [SELECTED scale → D4]; agreement to 0.5% is a validation, not a fit.
- **Constants:** σ_SB, R_sun, T_sun [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (D1, D4).

---

## Part I — Phase transitions (Clausius-Clapeyron, Van der Waals, Landau)

### EQ-THERMO-45 — First-order transition (Gibbs derivative discontinuities)
- **Equation:** (∂G/∂P)_T = V; (∂G/∂T)_P = −S; ΔS = L/T
- **Source:** 02-STATISTICAL_MECHANICS.md (Test 2.6 Step 1, line 296); 02-PHASE_TRANSITIONS_MOLECULAR.md (Part 2, lines 107, 110); 02-LAWS_DERIVATION.md (Part 8.1)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** S6 first derivatives of G (EQ-THERMO-17); a first-order transition is a jump in these first derivatives (V, S). Latent heat L = TΔS.
- **Constants:** L, T [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-46 — Clausius-Clapeyron equation
- **Equation:** dP/dT = (s₂−s₁)/(v₂−v₁) = ΔH/(TΔV) = L/(TΔV)
- **Source:** 02-STATISTICAL_MECHANICS.md (Test 2.6 Step 2, lines 309, 319); 02-PHASE_TRANSITIONS_MOLECULAR.md (Part 2, line 124); test_phase_transitions.py
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** Equality of phase chemical potentials along coexistence, dμ₁=dμ₂ ⇒ −s₁dT+v₁dP = −s₂dT+v₂dP (S6 differentials), rearranged with ΔS=L/T.
- **Constants:** L, ΔV, T [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-THERMO-47 — Van der Waals EOS + critical point
- **Equation:** (P + an²/V²)(V − nb) = nRT;  T_c = 8a/27bR, P_c = a/27b², V_c = 3b;  Z_c = P_cV_c/RT_c = 3/8
- **Source:** 02-PHASE_TRANSITIONS_MOLECULAR.md (Part 1, lines 46, 50, 79, 82); test_phase_transitions.py
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4 (a, b, R), D6 (intermolecular forces from membrane gauge fluctuations)
- **Trace:** EOS = ideal-gas (EQ-THERMO-38) corrected by excluded volume b and attraction a; the critical point is the inflection (∂P/∂V)_T=(∂²P/∂V²)_T=0 (S6), solved algebraically. Z_c=3/8 is a pure [DERIVED ratio]. a, b are material parameters (here treated as inputs, D4 scale / D6 origin); their first-principles membrane origin is qualitative (see UNTRACEABLE-A).
- **Constants:** a, b [SELECTED scale → D4]; R [SELECTED scale → D4]; Z_c=3/8 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (a,b origin partial).

### EQ-THERMO-48 — Landau free energy / order parameter
- **Equation:** F = F₀ + a(T,κ)Ψ² + bΨ⁴ + …;  a = a₀(T − T_c);  ψ ∝ (T_c − T)^β, β≈0.325
- **Source:** 02-LAWS_DERIVATION.md (Part 8.2, lines 864, 869); 02-STATISTICAL_MECHANICS.md (Critical exponents, line 359)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4
- **Trace:** Symmetry expansion of F in the order parameter Ψ (S6/analytic, even powers from a Ψ→−Ψ symmetry); sign change of the quadratic coefficient drives the second-order transition. The critical exponent β≈0.325 is an empirical/universality-class value [FIT → D5].
- **Constants:** a₀, b, T_c [SELECTED scale → D4]; β=0.325 [FIT → D5].
- **Status:** PARTIAL (form derived; exponent is D5/empirical).

---

## Part J — Thermal radiation (Planck, Stefan-Boltzmann, Wien)

### EQ-THERMO-49 — EM mode density in a cavity
- **Equation:** g(ν) = 8πν²/c³ (per unit volume);  g(k)=L³k²/π² (2 polarizations); g(λ)=8π/λ⁴
- **Source:** 02-PLANCK_DISTRIBUTION.md (Part 2, lines 148, 158); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 3, lines 188, 202)
- **Spine path:** S0→S1→S2→S3→S5→S7
- **Decrees:** D0, D1 (3D cavity), D2 (EM field / 2 transverse polarizations)
- **Trace:** Standing-wave quantization k_i=n_iπ/L (S5 independent directions, D1 gives d=3); counting modes in the positive octant of k-space ⇒ k²/π² density; the factor 2 polarizations is the U(1) gauge/transversality content (S7 gauge structure, member fixed by D2). 8π and the powers of ν are pure [DERIVED ratio].
- **Constants:** c [SELECTED scale → D4]; 8π [DERIVED ratio]; 2 (transverse polarizations) — a D2-fixed count (gauge transversality), not an independently selected integer.
- **Status:** DERIVED-given-decrees (D1, D2).

### EQ-THERMO-50 — Photon mean energy / Planck distribution per mode
- **Equation:** ⟨E⟩_photon = hν/(e^{hν/k_BT} − 1);  ⟨n(ν,T)⟩ = 1/(e^{hν/k_BT} − 1)
- **Source:** 02-PLANCK_DISTRIBUTION.md (Part 3.2, lines 193, 215); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 4.3, lines 244, 248)
- **Spine path:** S0→S1→S2→S3→S6→S8
- **Decrees:** D0, D4 (h,k_B), D2 (EM field), D6 (even-winding ⇒ boson), S8 (winding parity)
- **Trace:** ⟨E⟩=−∂ln Z₁/∂β (EQ-THERMO-32) with the zero-point term dropped; Bose statistics (no −μ for photons, μ=0) follows from even winding n_η (S8 integer invariant; even⇒+1 exchange phase). This is EQ-THERMO-24 specialized to massless photons.
- **Constants:** h, k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (D2, D4, D6).

### EQ-THERMO-51 — Planck energy density / spectral radiance
- **Equation:** u(ν,T) = 8πhν³/[c³(e^{hν/k_BT}−1)];  B(ν,T) = 2hν³/[c²(e^{hν/k_BT}−1)];  B(λ,T) = 2hc²/[λ⁵(e^{hc/λk_BT}−1)]
- **Source:** 02-PLANCK_DISTRIBUTION.md (Part 4, lines 227, 231, 241, 252); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 5, lines 268, 274, 284); 02-STATISTICAL_MECHANICS.md (Test 2.13, line 650); test_planck_spectrum.py
- **Spine path:** S0→S1→S2→S3→S5→S6
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Product of mode density (EQ-THERMO-49) and mean energy per mode (EQ-THERMO-50); the 2 (vs 8π/c³) for radiance is the hemisphere/Lambert geometric projection (S5/S6). The Rayleigh-Jeans limit (hν≪k_BT) → 8πν²k_BT/c³ and the UV-catastrophe resolution are limits of this expression.
- **Constants:** h, k_B, c [SELECTED scale → D4]; numeric prefactors [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D1, D2, D4, D6).

### EQ-THERMO-52 — Bose integral ∫x³/(eˣ−1)dx = π⁴/15
- **Equation:** ∫₀^∞ x³/(eˣ−1) dx = Γ(4)ζ(4) = 6·(π⁴/90) = π⁴/15
- **Source:** 02-STATISTICAL_MECHANICS.md (line 661); 02-PLANCK_DISTRIBUTION.md (Part 5.2, line 287); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 6.3, line 314)
- **Spine path:** S0→S1→S2→S3→S4→S6
- **Decrees:** D0 only (pure analysis)
- **Trace:** Pure mathematics: ℝ/ℂ analysis (S3/S4) and S6 integration; Γ(4)=3!=6 (S1 factorial), ζ(4)=π⁴/90 (S4 — π from the circle). No physics decree. Cited by rung, not re-derived.
- **Constants:** π⁴/15 [DERIVED ratio — pure number].
- **Status:** DERIVED-as-form (math identity; no physics decree beyond D0).

### EQ-THERMO-53 — Stefan-Boltzmann law and constant
- **Equation:** j* = σ_SB T⁴;  σ_SB = 2π⁵k_B⁴/(15h³c²) ≈ 5.670×10⁻⁸ W/m²K⁴
- **Source:** 02-PLANCK_DISTRIBUTION.md (Part 5.3, lines 297, 308, 312); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 6.4, lines 328, 332, 343); 02-STATISTICAL_MECHANICS.md (lines 671, 673); test_planck_spectrum.py
- **Spine path:** S0→S1→S2→S3→S4→S5→S6
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Integrate the Planck radiance (EQ-THERMO-51) over ν and the hemisphere; substitution x=hν/k_BT pulls out (k_BT)⁴ and leaves the Bose integral π⁴/15 (EQ-THERMO-52). The T⁴ power is forced by dimensional counting of the integral; σ_SB is a fixed combination of the D4-anchored constants. Numerical agreement (<0.001%) is validation, not fit.
- **Constants:** k_B, h, c [SELECTED scale → D4]; 2π⁵/15 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D1, D2, D4, D6).

### EQ-THERMO-54 — Wien displacement law
- **Equation:** 5(eᵘ−1)=ueᵘ ⇒ u=4.965…;  λ_max T = b = hc/(4.965 k_B) ≈ 2.898×10⁻³ m·K
- **Source:** 02-PLANCK_DISTRIBUTION.md (Part 6, lines 332, 340, 352); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 7, lines 392, 416, 424, 431); 02-STATISTICAL_MECHANICS.md (lines 681, 688); test_planck_spectrum.py
- **Spine path:** S0→S1→S2→S3→S4→S6
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Set ∂B(λ,T)/∂λ=0 on EQ-THERMO-51 (S6) → the transcendental 5(eᵘ−1)=ueᵘ; its root u≈4.965 is a pure number [DERIVED ratio]; b=hc/(uk_B) packages the D4 constants. The λ⁵ spectral form is inherited from the 3D cavity mode density (D1) of EQ-THERMO-51.
- **Constants:** h, c, k_B [SELECTED scale → D4]; u=4.965… [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D1, D2, D4, D6).

### EQ-THERMO-55 — Speed of light from membrane parameters
- **Equation:** c = √(σ/μ)
- **Source:** 02-PLANCK_DISTRIBUTION.md (Part 1.3, line 82); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 1.3, line 89)
- **Spine path:** S0→S1→S2→S3→S6→S9
- **Decrees:** D0, D4 (σ, μ scales), D6 (Firmament membrane mechanics)
- **Trace:** Wave speed of a tensioned membrane (S6 wave equation on the S9 curved membrane); σ (tension) and μ (density) are membrane content (D6) anchored by D4. The functional form √(σ/μ) is the standard membrane-wave result.
- **Constants:** σ, μ [SELECTED scale → D4]; c [SELECTED scale → D4, here derived from σ,μ].
- **Status:** DERIVED-given-decrees (D4, D6).

---

## Part K — Waters replenishment / open-system cosmo-thermodynamics

### EQ-THERMO-56 — Energy-reservoir definitions and (non)conservation
- **Equation:** E_total = E_A + E_B + E_F (not conserved; open);  dS_total/dt = dS_internal/dt + dS_external/dt ≥ 0
- **Source:** 02-WATERS_REPLENISHMENT.md (eqs. 1.1–1.5, 1.10; lines 110–139, 163)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4, D6 (Waters Above/Below/Firmament reservoirs, Zone 1 source)
- **Trace:** S1 additive split of total energy into three reservoir integrals (S6); the open-system Clausius inequality is EQ-THERMO-16 generalized. The reservoir identification (E_A=Waters Above, etc.) and the external Zone-1 source are entirely **D6** content.
- **Constants:** reservoir energies/entropies [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (D6).

### EQ-THERMO-57 — Firmament equation of motion (pressure balance)
- **Equation:** μ ∂²η/∂t² − σ∇²η = P_A − P_F − P_B
- **Source:** 02-WATERS_REPLENISHMENT.md (eq. 2.3, line 212)
- **Spine path:** S0→S1→S2→S3→S6→S9
- **Decrees:** D0, D1, D4, D6
- **Trace:** Driven wave equation for the membrane displacement η (S6 operators on the S9 membrane); pressures from the two Waters reservoirs are D6 source content. Same membrane mechanics that gives c=√(σ/μ) (EQ-THERMO-55).
- **Constants:** μ, σ [SELECTED scale → D4]; P_A,P_F,P_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (D1, D4, D6).

### EQ-THERMO-58 — Reservoir rate-equation system
- **Equation:** dE_A/dt = Ė_S − 3HE_A;  dE_B/dt = −β[E_B − E_{B,eq}];  dE_F/dt = 3HE_A + β[E_B−E_{B,eq}] − λE_F;  (sum) = Ė_S
- **Source:** 02-WATERS_REPLENISHMENT.md (eqs. 2.6, 2.8, 2.9, 2.10–2.13; lines 233, 255, 263, 271–283)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4, D6 (sustaining input Ė_S, dissipation λ, relaxation β; expansion work 3HE_A)
- **Trace:** Coupled first-order ODEs (S6) for the three reservoir energies; each transfer term (3HE_A expansion work, β relaxation, λ dissipation, Ė_S sustaining) is a **modeled** D6 process, not grammar. The closure constraint (sum = Ė_S) is energy bookkeeping for the open system.
- **Constants:** H, β, λ, Ė_S [SELECTED scale → D4]; the *forms* of the transfer terms are D6 modeling choices [FIT → D5 for β, λ, Ė_S magnitudes].
- **Status:** PARTIAL (ODE form is S6; the specific coupling terms are D6/D5 modeling, not forced).

### EQ-THERMO-59 — Steady-state balance and energy split
- **Equation:** Ė_S = 3HE_A^{ss} = λE_F^{ss};  E_A:E_B:E_F = 0.68:0.27:0.05;  Ė_S = 0.05 λ E_total
- **Source:** 02-WATERS_REPLENISHMENT.md (eqs. 5.2–5.7; lines 562, 568, 574, 578, 591, 601)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4, D6
- **Trace:** Set the EQ-THERMO-58 rates to zero (S6 stationarity) → sustaining balances dissipation. The 68/27/5 numbers are **observational inputs matched to ΛCDM** [FIT → D5], not derived from grammar; the document explains *why* E_A dominates (constant comoving density) but the precise split is fitted.
- **Constants:** H, λ [SELECTED scale → D4]; 0.68/0.27/0.05 [FIT → D5].
- **Status:** PARTIAL (balance form derived; ratios are D5 fits to data).

### EQ-THERMO-60 — Friedmann equations / dark-energy EOS
- **Equation:** H² = (8πG/3)(ρ_A+ρ_B+ρ_F);  ä = −(4πG/3)(ρ_A+ρ_B+3p_A)a;  w_A = p_A/ρ_Ac² = −1
- **Source:** 02-WATERS_REPLENISHMENT.md (eqs. 6.1–6.3, 6.2 line 686, 6.3 line 688, w line 702)
- **Spine path:** S0→S1→S2→S3→S6→S9
- **Decrees:** D0, D1, D4, D6
- **Trace:** Standard FRW dynamics from the Einstein equations on the S9 cosmological manifold (D1); w=−1 follows from requiring adiabatic constant-density expansion of Waters Above (D6). **Honesty:** this is the cosmology domain's territory — traced here only as it appears in the thermodynamic open-system argument. w=−1 here is consistency-matched to observation [borderline FIT/structural].
- **Constants:** G [SELECTED scale → D4]; w=−1 [DERIVED-given-D6 / consistency with data].
- **Status:** DERIVED-given-decrees (D1, D6); cross-domain (cosmology).

---

## Part L — Missed equations recovered in audit (2026-06-24)

### EQ-THERMO-61 — Barometric / isothermal-atmosphere distribution
- **Equation:** n(h) = n₀ e^{−mgh/k_BT};  scale height H = k_BT/(mg)
- **Source:** 02-STATISTICAL_MECHANICS.md (Test 2.11 Step 5, "Barometric Formula", lines 531, 533)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D4 (k_B, and the dimensionful magnitudes m, g), D6 (the external gravitational potential U=mgh is physical field content)
- **Trace:** Specialization of the Boltzmann distribution (EQ-THERMO-29) to a single particle in the gravitational potential energy U(h)=mgh: P(h) ∝ e^{−U(h)/k_BT} ⇒ number density n(h)=n₀e^{−mgh/k_BT}. Inherits the Boltzmann-factor grammar of EQ-THERMO-29 (S6 max-entropy, exponential on ℝ); the gravitational potential mgh is not grammar (a dimensionful magnitude g and a field background) ⇒ D4/D6. Used here only as a verification of the Boltzmann factor (recovers Earth's ~8.5 km scale height).
- **Constants:** k_B [SELECTED scale → D4]; m, g [SELECTED scale → D4]; scale height H=k_BT/mg [DERIVED ratio of D4 magnitudes].
- **Status:** DERIVED-given-decrees (D4, D6).

### EQ-THERMO-62 — CMB blackbody temperature (cosmological validation)
- **Equation:** T_CMB = 2.725 K (perfect Planck blackbody);  scale-factor cooling T ∝ 1/a(t), a(t)=a₀(t/t₀)^{1/2} (radiation era)
- **Source:** 02-PLANCK_DISTRIBUTION.md (Part 7, lines 368, 372, 379); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 9.2, lines 538, 583, 603)
- **Spine path:** S0→S1→S2→S3→S5→S6
- **Decrees:** D0, D1 (FRW cosmological manifold / scale factor a(t)), D2 (photon = EM boson), D4 (the 2.725 K magnitude), D5 (value matched to Planck-satellite data), D6 (Firmament radiation field, expanding-zone framing)
- **Trace:** The CMB obeys the Planck radiance (EQ-THERMO-51) with a single parameter T; adiabatic expansion on the FRW manifold (D1, cross-domain cosmology) redshifts the spectrum keeping it Planckian with T ∝ 1/a(t). The specific present-day value **2.725 K is not derived** — it is the measured Planck/COBE/WMAP value [FIT → D5] (agreement quoted at 0.018%–0.5%), reported here as a validation of the blackbody form, not a first-principles output.
- **Constants:** T_CMB = 2.725 K [FIT → D5] (measured, dimensionful ⇒ also D4 anchored); exponent ½ in a(t) [DERIVED ratio — radiation-era Friedmann scaling, cross-domain].
- **Status:** PARTIAL (Planck *form* derived; the temperature value is a D5 data match — cross-domain cosmology).

### EQ-THERMO-63 — 4D Maxwell EM action (KK reduction of the 6D gauge sector)
- **Equation:** S₄^EM = −¼∫d⁴x √(−g₄) F^EM_{μν}F^{μν}_EM,  F^EM_{μν}=∂_μA_ν−∂_νA_μ (with A_μ^EM = A_μ^η);  source-free ∂_μF^{μν}=0
- **Source:** 02-PLANCK_DISTRIBUTION.md (Part 1.2, lines 70, 74); 02-PLANCK_SPECTRUM_DERIVATION.md (Part 2, line 84)
- **Spine path:** S0→S1→S2→S3→S5→S7→S9
- **Decrees:** D0, D1 (4D after KK reduction of the 6D manifold), D2 (the U(1)_EM gauge member; off-diagonal A^η identified as the photon), D6 (the Waters-Below η-fibre origin of A^η)
- **Trace:** Dimensional reduction of the 6D Einstein–Hilbert + gauge action (EQ-THERMO-02) on the η-direction (S9 warped manifold ⇒ S5/S7 gauge structure) yields the 4D Maxwell action; the field strength F=dA is S7 (identity-preserving maps), the specific U(1)_EM is **D2**, and the identification A_μ^EM=A_μ^η (which off-diagonal metric component is the photon) is **D6** membrane content. The source-free equation ∂_μF^{μν}=0 is the δS=0 variation (S6-borderline). **Cross-domain:** this is Electromagnetism (domain 03) content, traced here only because it is the displayed gauge action underpinning the photon mode-counting (EQ-THERMO-49/50).
- **Constants:** none new dimensionful (G₆/coupling carried by EQ-THERMO-02 [SELECTED scale → D4]).
- **Status:** DERIVED-as-form (given D1, D2, D6); action principle S6-borderline; cross-domain (electromagnetism).

---

## UNTRACEABLE / partial items (honesty audit)

### UNTRACEABLE-A — Van der Waals a, b "from 6D gauge fluctuations"
- **Equation context:** a ≈ (2πN_A²/3)∫|U(r)|r²dr, b ≈ (2πN_A/3)σ³ with U(r) = −C₆/r⁶ + C₁₂/r¹² (02-PHASE_TRANSITIONS_MOLECULAR.md Part 5, lines 305, 318–320)
- **Reason:** The Lennard-Jones form and the integrals are standard, but the claim that C₆, C₁₂ (hence a, b) emerge *quantitatively* "from the 6D gauge field coupling strength" is asserted, not derived. No spine path produces the numerical a=0.5536, b=3.049×10⁻⁵ for water; they are empirical molecular parameters. Trace stops at "Lennard-Jones + D6 hand-wave"; the dimensionful values are **[FIT → D5]** with no shown derivation. Marked UNTRACEABLE for the *first-principles membrane origin*.

### UNTRACEABLE-B — Coefficient of restitution / Hertzian contact
- **Equation context:** e = −(v₂'−v₁')/(v₂−v₁); 1/E_eff = (1−ν₁²)/E₁ + (1−ν₂²)/E₂; a=(3FR_eff/4E_eff)^{1/3}; P_max=3F/2πa² (02-PHASE_TRANSITIONS_MOLECULAR.md Part 4, lines 204, 227, 230, 234)
- **Reason:** These are classical continuum-elasticity / contact-mechanics results (Hertz, Goldsmith). They are imported from materials literature with material constants E, ν, ρ as **measured inputs [SELECTED scale → D4]**. There is no derivation from the spine to the elastic moduli, and the restitution values (e=0.56 steel, e=0.80 rubber) are matched to experiment. No `1=1` chain to the numbers ⇒ UNTRACEABLE as Genesis-derived; the *forms* are standard mechanics (would belong to Classical Mechanics domain, S6).

### UNTRACEABLE-C — Sustaining-source effective temperature T₁ ~ 10³ K and entropy/info estimates
- **Equation context:** dS_external/dt = −Ė_S/T₁; T₁ ~ 10³ K; İ_S ~ 10⁷² bits/s; I_universe ~ 10¹²⁰ k_B (02-WATERS_REPLENISHMENT.md §3.4, §9.2, lines 365, 445, 1044, 1052)
- **Reason:** Order-of-magnitude estimates built on the unobservable Zone-1 properties (D6) plus assumed dissipation rates. The document itself flags Zone-1 properties as "not falsifiable by physics." No spine path fixes T₁ or the bit counts; they are illustrative numbers, not derived results. UNTRACEABLE (and acknowledged as metaphysical framing by the source).

### UNTRACEABLE-D — Sustaining coupling control law Ė_S = g_s[O_target − O(t)]
- **Equation context:** Ė_S = g_s·[O_target − O(t)] (02-WATERS_REPLENISHMENT.md eq. 8.1, line 942); and boundary-condition closure Ė_S = 3HE_A + λE_F (eq. 8.2)
- **Reason:** This is a postulated negative-feedback boundary condition (control-theory analogy), with g_s and O_target free. It is explicitly stated to be a chosen boundary condition / "intentional tuning," i.e. pure D6 decree with a D5-level free coupling g_s. The functional form is not forced by any spine rung. PARTIAL→UNTRACEABLE: form is a modeling choice; constants undetermined.

---

## Decrees used in this domain (summary)

| Decree | Where it enters |
|--------|-----------------|
| **D0** (ℝ continuum) | every block — all continuous T, S, U, integrals |
| **D1** (dimension / manifold) | 6D action, Liouville phase space, cavity mode counting, Friedmann, membrane EOM |
| **D2** (gauge group SU(3)×SU(2)×U(1)) | EM/KK sector: 2 photon polarizations, Bose statistics of photons, 4D Maxwell action (EQ-THERMO-02, 49, 50, 51, 53, 54, 63) |
| **D3** (integer counts) | particle/mole counts N, N_A; microstate count Ω; ground-state degeneracy g₀; level degeneracy g_n; quadratic-DOF counts d (EQ-THERMO-03, 06, 15, 26, 27, 29, 37, 38, 39) |
| **D4** (scale anchor) | every dimensionful constant: ℏ, k_B, c, h, R, σ_SB, b, σ-tension, μ, λ, β, κ, G, m, g, masses, T_CMB |
| **D5** (fitted O(1) constants) | Van der Waals a,b values; β≈0.325 critical exponent; 68/27/5 split; β,λ,Ė_S magnitudes; g_s; T_CMB=2.725 K (EQ-THERMO-62) |
| **D6** (architectural axioms) | Ψ_A/Ψ_B Waters fields, Firmament membrane, κ sustaining coupling, open-system framing, zone reservoirs, phase-2/3 Fall transition |

*No equation in this domain is "derived from `1=1` alone." Every block lists its spine path and the decrees it invokes, per the honesty discipline. Cross-ref: `SPINE.md`, `DECREE_REGISTER.md`, `README_SCHEMA.md`.*
