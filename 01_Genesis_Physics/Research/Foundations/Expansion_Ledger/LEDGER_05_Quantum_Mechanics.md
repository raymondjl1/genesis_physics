# Expansion Ledger — Domain 05: Quantum Mechanics

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This ledger traces every displayed/numbered equation and named key result in
> `Research/Mathematical_Models/05_Quantum_Mechanics/` back to the seed `1=1` via the
> Derivation Spine (rungs S0–S9, `SPINE.md`) plus named decrees (D0–D6, `DECREE_REGISTER.md`).
> Honesty rule applied throughout: no equation is "derived from `1=1` alone." Every physics
> equation = spine path + decrees. Dimensionful constants are tagged `[SELECTED scale → D4]`;
> data-matched values `[FIT → D5]`; topological integers `[count → D3]`; geometry/topology
> ratios `[DERIVED ratio]`.

## Header / coverage table

| Field | Value |
|-------|-------|
| Domain | Quantum_Mechanics (`05_Quantum_Mechanics/`) |
| Files traced | 13 (.md ×10, .py ×3) + 2 test-suite .py (equations already covered) |
| Equation blocks | 70 |
| Decrees used across domain | D0, D1, D2, D3, D4, D5, D6 |
| # PARTIAL | 7 |
| # UNTRACEABLE | 3 |

**Decree legend (as invoked here):**
- **D0** — completed infinity (ℝ, continua, integrals). Silently present in nearly every entry; cited once per block.
- **D1** — dimension = 6 (and 4D reduction); any manifold/metric/KK reduction/Laplacian.
- **D2** — gauge group SU(3)×SU(2)×U(1); any gauge field, charge, U(1)_A, Coulomb-from-KK.
- **D3** — winding n_w = 3 / topological integer counts (generations, vortex winding values).
- **D4** — scale anchor (Λ_Z0, M_Z0 = M_Pl): every dimensionful magnitude (σ, η_B, ξ_A, m_e, ℏ value, …).
- **D5** — residual fitted O(1) constants matched to data (work functions, N(0)V, ξ₀ consistency value, etc.).
- **D6** — architectural axioms: Firmament membrane, Ψ_A/Ψ_B Waters, zone boundaries, sustaining/open-system content.

**Note on the membrane substrate.** Almost every QM result in this domain is built on the
Firmament membrane wave equation (a physical-content object). That substrate invokes **D6**
(membrane/Waters exist), **D1** (a 6D manifold + Laplacian), and **D4** (σ, μ, η_B, ξ_A are
dimensionful). These are cited per block; the underlying grammar (∂, ∇², ℝ, ℂ) is cited by rung
ID and never re-derived.

---

### EQ-QM-01 — Firmament membrane wave equation
- **Equation:** μ ∂²ψ/∂t² = σ ∇²ψ − V_ext ψ + ℱ
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §1.3 (boxed)
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D6 (the Firmament membrane + Ψ-forcing exist), D1 (4D manifold + Laplacian ∇²), D4 (μ, σ dimensionful), D0 (ℝ continuum).
- **Trace:** 1=1 → S1 gives additive balance (force terms sum) → S3 grants the ℝ-valued field ψ(x,t) (needs D0) → S6 supplies ∂²/∂t² and ∇². The *content* (that there IS an elastic membrane with tension σ and density μ) is **D6**; the manifold it lives on is **D1**. Newton's-law form (mass×accel = restoring + external + forcing) is the S1 conservation structure applied to the membrane.
- **Constants:** μ [SELECTED scale → D4]; σ [SELECTED scale → D4]; V_ext, ℱ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6, D1, D4).

### EQ-QM-02 — Wave speed from tension and density
- **Equation:** c = √(σ/μ) = 3.0×10⁸ m/s
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §1.1
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D6 (membrane substrate), D4 (σ, μ are the chosen dimensionful inputs), D0.
- **Trace:** 1=1 → S2 gives the ratio/quotient σ/μ → S3 gives the square root (real). c emerges as the membrane's characteristic speed. That its numerical value equals the observed light speed is fixed by the **D4** choice of σ and μ.
- **Constants:** σ, μ [SELECTED scale → D4]; c [SELECTED scale → D4] (value is a consequence of D4 inputs).
- **Status:** DERIVED-given-decrees.

### EQ-QM-03 — Massless membrane dispersion
- **Equation:** ω(k) = c|k|
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §1.3; 05-CONDENSED_MATTER_DERIVATION.md §1.1
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D6, D1, D4 (c), D0.
- **Trace:** 1=1 → S6 supplies plane-wave solutions e^{i(kx−ωt)} of the homogeneous EQ-QM-01 → substituting gives ω² = c²k². The linear-in-|k| branch is the acoustic mode. D1 supplies k as a wavevector on the manifold.
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6, D1, D4).

### EQ-QM-04 — Relativistic (massive) dispersion
- **Equation:** ω(k) = √((mc²/ℏ)² + (ck)²)
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §1.3; 05-CONDENSED_MATTER_DERIVATION.md §1.1
- **Spine path:** S0→S1→S3→S4→S6
- **Decrees:** D6, D1, D4 (m, c, ℏ), D0.
- **Trace:** 1=1 → adding a mass (confinement) term to EQ-QM-01 gives a Klein–Gordon-type membrane equation → S4 (phase/ℂ) + S6 give the dispersion √(rest² + propagating²). m and ℏ enter as dimensionful magnitudes (D4); ℏ itself is derived in EQ-QM-06.
- **Constants:** m, c, ℏ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6, D1, D4).

### EQ-QM-05 — Topological vortex action quantum (bare)
- **Equation:** S_vortex = E_vortex · τ_min = πσ η_B²·(η_B/c) = πσ η_B³/c
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §2.1
- **Spine path:** S0→S1→S2→S3→S8
- **Decrees:** D6 (membrane + vortex), D3 (unit winding n=1 is a topological count), D4 (σ, η_B, c), D0.
- **Trace:** 1=1 → S8 classifies the vortex by an integer winding (π₁=ℤ); the unit-winding defect (n=1, a **D3** count) has core energy σ·(πr_core²) with r_core=η_B, and minimum timescale τ=η_B/c → product is the action. S2/S3 supply the arithmetic; S8 supplies the topological quantization label.
- **Constants:** σ, η_B, c [SELECTED scale → D4]; winding n=1 [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-QM-06 — Bare quantum ℏ₀ from Bohr–Sommerfeld
- **Equation:** ℏ₀ = σ η_B³ / (2c)  (= 2.197×10⁴⁵ J·s)
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §2.2 (boxed)
- **Spine path:** S0→S1→S2→S3→S8
- **Decrees:** D6, D3 (winding count + Bohr–Sommerfeld integer), D4 (σ, η_B, c), D0.
- **Trace:** 1=1 → S8 gives the integer loop-quantization ∮p·dq = 2πnℏ; setting the topological action (EQ-QM-05, with the 2π loop factor) equal to the quantum action for n=1 solves for ℏ₀ = σ η_B³/(2c). The *form* is forced by topology (S8) + arithmetic (S2); the numerical magnitude is set by D4.
- **Constants:** σ, η_B, c [SELECTED scale → D4]; n=1 [count → D3].
- **Status:** DERIVED-given-decrees. (Bare value is ~10⁷⁹ too large; warp suppression follows.)

### EQ-QM-07 — Warp-suppressed ℏ (corrected CT-4.β form)
- **Equation:** ℏ = (σ η_B³/2c)·(ξ₀/L_A)^{4/3}·β_geom^(residual)
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §2.4 (boxed, Rev. 2026-05-15); BETA_GEOM_DERIVATION_CT4B.md §3.4
- **Spine path:** S0→S1→S2→S3→S8→S9
- **Decrees:** D6, D1 (6D metric + warp), D3 (winding), D4 (σ, η_B, ξ₀, L_A, c), D5 (ξ₀≈60 l_Pl fixed by consistency with ℏ_obs, not independently derived), D0.
- **Trace:** 1=1 → EQ-QM-06 gives ℏ₀ → S9 (curved/warped manifold, **D1**) supplies the Waters-Above warp factor e^{−2A_ξ(ξ₀)} = (ξ₀/L_A)^{4/3} → product gives observed ℏ. The Firmament position ξ₀ is set by the Israel junction condition but its value (~60 l_Pl) is presently a **D5** consistency choice (blocked by RT-1.WF), so the match to ℏ_obs is "exact by construction," PARAMETRIC.
- **Constants:** σ, η_B, ξ₀, L_A, c [SELECTED scale → D4]; (ξ₀/L_A)^{4/3} [DERIVED ratio] in form but ξ₀ value [FIT → D5]; β_geom^(residual)≈1 [DERIVED ratio].
- **Status:** PARTIAL (PARAMETRIC; ξ₀ not independently derived — RT-1.WF / OP-G6).

### EQ-QM-08 — Israel junction condition for Firmament position
- **Equation:** ∂A/∂ξ|_{ξ₀} = −κ₆²σ/3  ⇒  ξ₀ = 2/(κ₆²σ)
- **Source:** BETA_GEOM_DERIVATION_CT4B.md §3.2 (boxed); 05-QM_FROM_MEMBRANE_DYNAMICS.md §2.4
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6 (Firmament as boundary brane), D1 (6D metric, κ₆²), D4 (σ, κ₆²), D0.
- **Trace:** 1=1 → S9 (curvature + connection on the 6D manifold) gives the junction/Israel matching of the warp derivative across the brane → S6 supplies ∂_ξ; solving the first-order condition gives ξ₀ in terms of κ₆² and σ. κ₆² itself is undetermined here (blocked by OP-G6).
- **Constants:** κ₆², σ [SELECTED scale → D4].
- **Status:** PARTIAL (κ₆² not derived; OP-G6 open).

### EQ-QM-09 — Waters-Above warp function
- **Equation:** A_ξ(ξ) = (2/3)·ln(L_A/ξ);  e^{−2A_ξ(ξ₀)} = (ξ₀/L_A)^{4/3}
- **Source:** BETA_GEOM_DERIVATION_CT4B.md §2.2 / §3.1 (citing METRIC_6D_SOLUTIONS.md §3.2)
- **Spine path:** S0→S1→S2→S3→S9
- **Decrees:** D6 (Waters-Above zone), D1 (6D warped metric), D4 (L_A, ξ₀), D0.
- **Trace:** 1=1 → S9 supplies the AdS-type warped manifold whose Einstein equations yield a power-law (logarithmic-A) warp profile → S2/S3 give the ln and the 4/3 power. The exponent 4/3 is a geometric [DERIVED ratio] from the AdS solution; the scales are D4.
- **Constants:** L_A, ξ₀ [SELECTED scale → D4]; exponents 2/3, 4/3 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D6, D1, D4); profile is an approximate analytic solution.

### EQ-QM-10 — η-direction subleading warp correction
- **Equation:** A_η(η) ≈ −α η²/(2η_B²);  e^{−2|A_η(η₀)|} ≈ 0.975
- **Source:** BETA_GEOM_DERIVATION_CT4B.md §3.3
- **Spine path:** S0→S1→S2→S3→S9
- **Decrees:** D6 (Waters-Below zone), D1 (metric), D4 (η_B, α<0.1), D0.
- **Trace:** 1=1 → S9 gives the Waters-Below warp profile (quadratic near the brane) → evaluated at η₀≈η_B/2 gives a ~2.5% correction. α<0.1 is presently bounded, not pinned.
- **Constants:** η_B [SELECTED scale → D4]; α [FIT → D5] (bound, not derived).
- **Status:** PARTIAL.

### EQ-QM-11 — Klein–Gordon membrane equation (potential form)
- **Equation:** [ (1/c²)∂²_t − ∇² + m²c²/ℏ² ] ψ = 0
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §3.3 (alt. derivation)
- **Spine path:** S0→S1→S3→S4→S6
- **Decrees:** D6, D1, D4 (m, c, ℏ), D0.
- **Trace:** 1=1 → EQ-QM-01 with the confinement term identified as V_ext/σ = m²c²/ℏ² gives the relativistic wave operator. S4 (ℂ phase) + S6 (□ d'Alembertian) supply the form.
- **Constants:** m, c, ℏ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6, D1, D4).

### EQ-QM-12 — Time-dependent Schrödinger equation
- **Equation:** iℏ ∂Ψ/∂t = ĤΨ = [ −ℏ²/(2m)∇² + V(x) ] Ψ
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §3.3 (boxed); reused across all 05 docs
- **Spine path:** S0→S1→S3→S4→S6
- **Decrees:** D6 (membrane), D1 (manifold + ∇²), D4 (ℏ, m), D0.
- **Trace:** 1=1 → write ψ = e^{−imc²t/ℏ}Ψ (slowly-varying envelope, S4 phase) in EQ-QM-11 → the m²c⁴ terms cancel and dropping the second-order time derivative (non-relativistic limit) leaves the first-order Schrödinger form. ℏ is the *derived* constant of EQ-QM-07; here it appears as a coefficient.
- **Constants:** ℏ, m [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6, D1, D4).

### EQ-QM-13 — Momentum operator eigenvalue (p = ℏk)
- **Equation:** p̂ e^{ikx} = −iℏ ∂_x e^{ikx} = ℏk·e^{ikx}
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §4.2
- **Spine path:** S0→S1→S3→S4→S6
- **Decrees:** D1 (∂_x on manifold), D4 (ℏ), D0.
- **Trace:** 1=1 → S4 supplies the complex phase e^{ikx}; S6 supplies ∂_x → the eigenvalue ℏk identifies momentum. Fourier completeness (S6 + D0) underlies the decomposition.
- **Constants:** ℏ [SELECTED scale → D4].
- **Status:** DERIVED-as-form.

### EQ-QM-14 — de Broglie relation
- **Equation:** λ = h/p = 2πℏ/p
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §4.2 (boxed); 05-CONDENSED_MATTER §7.1
- **Spine path:** S0→S1→S2→S4→S6
- **Decrees:** D4 (ℏ), D0.
- **Trace:** 1=1 → from EQ-QM-13 (p=ℏk) and λ=2π/k (S4 circle/period) → λ = 2πℏ/p. h=2πℏ.
- **Constants:** ℏ, h [SELECTED scale → D4].
- **Status:** DERIVED-as-form.

### EQ-QM-15 — Group velocity equals particle velocity
- **Equation:** v_g = dω/dk |_{k₀} = ℏk/m = p/m
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §4.3
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D4 (ℏ, m), D0.
- **Trace:** 1=1 → S6 differentiates the non-relativistic dispersion ω=ℏk²/2m → v_g = ℏk/m = p/m, recovering the classical velocity.
- **Constants:** ℏ, m [SELECTED scale → D4].
- **Status:** DERIVED-as-form.

### EQ-QM-16 — Fourier / Heisenberg uncertainty
- **Equation:** Δx·Δk ≥ 1/2  ⇒  Δx·Δp ≥ ℏ/2
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §5.1–§5.2 (boxed)
- **Spine path:** S0→S1→S3→S4→S6
- **Decrees:** D4 (ℏ), D0 (real continua, integrals).
- **Trace:** 1=1 → S4/S6 give the Fourier-transform pair (e^{−ikx}, integrals need D0) → Cauchy–Schwarz + Plancherel give the pure-math bound Δx·Δk ≥ 1/2 (a theorem of analysis, no physics decree). Multiplying by ℏ (p=ℏk, EQ-QM-13) gives ΔxΔp ≥ ℏ/2.
- **Constants:** ℏ [SELECTED scale → D4]; the 1/2 [DERIVED ratio] (Gaussian-saturated math bound).
- **Status:** DERIVED-as-form.

### EQ-QM-17 — Orbital angular momentum quantization
- **Equation:** L̂_z e^{imφ} = mℏ e^{imφ}  ⇒  L_z = mℏ (m ∈ ℤ)
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §6.1 (boxed)
- **Spine path:** S0→S1→S4→S6→S8
- **Decrees:** D1 (∂_φ on the angular manifold), D4 (ℏ), D3 (winding integer m), D0.
- **Trace:** 1=1 → S4 gives single-valued phase e^{imφ} on the circle; single-valuedness forces m ∈ ℤ (S8, π₁(S¹)=ℤ) → S6's L̂_z = −iℏ∂_φ acts to give eigenvalue mℏ. The integer m is the **D3**-type topological count (winding); half-integers arise for fermionic π-winding defects.
- **Constants:** ℏ [SELECTED scale → D4]; m [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-QM-18 — Total angular momentum eigenvalues
- **Equation:** L̂² Y_{ℓm} = ℓ(ℓ+1)ℏ² Y_{ℓm};  L̂_z Y_{ℓm} = mℏ Y_{ℓm}
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §6.2
- **Spine path:** S0→S1→S4→S5→S6→S8
- **Decrees:** D1 (Laplacian on S²), D4 (ℏ), D3 (integers ℓ, m), D0.
- **Trace:** 1=1 → S5/S6 give the Laplacian eigenproblem on the 2-sphere (spherical harmonics); S8 supplies the integer labels from the topology of S². ℏ² scales the eigenvalue.
- **Constants:** ℏ [SELECTED scale → D4]; ℓ, m [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-QM-19 — Coulomb potential from KK U(1)
- **Equation:** ∇²φ = −4πe²δ³(r)  ⇒  φ(r) = −e²/r
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §7.1
- **Spine path:** S0→S1→S5→S6→S7
- **Decrees:** D2 (U(1)_A gauge field from KK), D1 (KK reduction of ξ-dimension), D4 (e²), D0.
- **Trace:** 1=1 → S7 gives the U(1) gauge structure (free phase of ℂ, but *that* U(1)_A is the EM sector is **D2**); D1 KK-reduces the ξ-dimension to a 4D gauge field → solving 4D Gauss law (S6) for a point source gives the 1/r potential.
- **Constants:** e² [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-QM-20 — Bohr radius
- **Equation:** a₀ = ℏ²/(m_e e²) ≈ 0.53 Å  (a_n = n²a₀)
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §7.3
- **Spine path:** S0→S1→S2→S6→S8
- **Decrees:** D2 (Coulomb e²), D4 (ℏ, m_e, e²), D3 (Bohr integer n), D0.
- **Trace:** 1=1 → centripetal=Coulomb balance (S1) + Bohr topological quantization ∮p·dl=2πnℏ (S8) → solve for orbit radius a_n = n²ℏ²/(m_e e²). n is the **D3**-type integer.
- **Constants:** ℏ, m_e, e² [SELECTED scale → D4]; n [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-QM-21 — Hydrogen energy levels
- **Equation:** E_n = −m_e e⁴/(2n²ℏ²) = −13.6 eV/n²
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §7.4 (boxed)
- **Spine path:** S0→S1→S2→S6→S8
- **Decrees:** D2 (Coulomb), D4 (m_e, e², ℏ), D3 (n), D0.
- **Trace:** 1=1 → E_n = kinetic + potential = −e²/(2a_n); substituting a_n=n²a₀ (EQ-QM-20) gives the −13.6 eV/n² spectrum. Quantization n from the topological Bohr condition (S8).
- **Constants:** m_e, e², ℏ [SELECTED scale → D4]; n [count → D3]; 13.6 eV [SELECTED scale → D4] (consequence of D4 inputs).
- **Status:** DERIVED-given-decrees.

### EQ-QM-22 — Reduced density matrix / decoherence
- **Equation:** ρ_sys = Tr_env[|Ψ_full⟩⟨Ψ_full|] = |c₁|²|ψ₁⟩⟨ψ₁| + |c₂|²|ψ₂⟩⟨ψ₂|
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §8.3; 05-COMPLETIONS.md Test 5 (Eq. 17)
- **Spine path:** S0→S1→S5
- **Decrees:** D6 (Waters environment ℰ, Ψ_A/Ψ_B), D1 (Hilbert space dimension), D4, D0.
- **Trace:** 1=1 → S5 gives the tensor-product Hilbert space and the partial-trace operation; orthogonality of environment branches ⟨Env₂|Env₁⟩≈0 kills cross terms. The environment being the Waters fields is **D6**.
- **Constants:** none dimensionful (|c_i|² dimensionless amplitudes).
- **Status:** DERIVED-as-form (given D6).

### EQ-QM-23 — Born rule from energy-transfer statistics
- **Equation:** P(outcome i) = ⟨ΔE_i⟩/Σ⟨ΔE_j⟩ = |c_i|²
- **Source:** 05-QM_FROM_MEMBRANE_DYNAMICS.md §8.4
- **Spine path:** S0→S1→S5
- **Decrees:** D6 (Waters-mediated energy transfer + |Ψ|²∝energy density), D4, D0.
- **Trace:** 1=1 → branch energy transfer ΔE_i ∝ |c_i|² (membrane amplitude² = energy density, a **D6** physical-content statement) → normalizing gives P=|c_i|². NB: op09_collapse_resolution.md explicitly flags that the Born rule is *not* fully derived (see UNTRACEABLE-A).
- **Constants:** none dimensionful.
- **Status:** PARTIAL (heuristic; see UNTRACEABLE-A for the honest scope boundary).

### EQ-QM-24 — Spin from winding (Goldstone–Wilczek)
- **Equation:** S = n/2
- **Source:** 05-SPIN_STATISTICS_DERIVATION.md §1, §6
- **Spine path:** S0→S1→S8
- **Decrees:** D6 (defect on Firmament), D3 (winding integer n), D0.
- **Trace:** 1=1 → S8 gives the integer vortex winding n; the Goldstone–Wilczek relation ties the bound-zero-mode angular momentum to n/2. The integer n is **D3**-type.
- **Constants:** none dimensionful; n [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-QM-25 — Configuration-space fundamental group (d ≥ 3)
- **Equation:** π₁(C_N(ℝ^d)) ≅ 𝕊_N  (d ≥ 3)
- **Source:** 05-SPIN_STATISTICS_DERIVATION.md §2, §10
- **Spine path:** S0→S1→S5→S8
- **Decrees:** D1 (spatial dimension d = 3), D0.
- **Trace:** 1=1 → S5/S8 supply the topology of the N-particle configuration space; for d≥3 the braid collapses to the symmetric group. The "d=3" is the spatial-dimension content of **D1** (6D→4D).
- **Constants:** none; d is a dimension count [count → D3-type via D1].
- **Status:** DERIVED-as-form (pure topology, given D1).

### EQ-QM-26 — Exchange phase / Berry phase
- **Equation:** τ₁₂ Ψ = e^{inπ} Ψ = (−1)ⁿ Ψ
- **Source:** 05-SPIN_STATISTICS_DERIVATION.md §3, §4, §9
- **Spine path:** S0→S1→S4→S8
- **Decrees:** D6 (defects), D3 (winding n), D0.
- **Trace:** 1=1 → S4 gives the geometric/Berry phase from the complex order-parameter field e^{inθ}; a full exchange rotates by π, accumulating e^{inπ}=(−1)ⁿ. n is **D3**-type.
- **Constants:** none dimensionful; n [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-QM-27 — Spin–statistics connection
- **Equation:** (−1)^{2S} = exchange phase;  S=n/2 ⇒ statistics = (−1)ⁿ
- **Source:** 05-SPIN_STATISTICS_DERIVATION.md §6 (boxed)
- **Spine path:** S0→S1→S4→S8
- **Decrees:** D6, D3 (n), D0.
- **Trace:** 1=1 → combine EQ-QM-24 (S=n/2) and EQ-QM-26 ((−1)ⁿ): the same winding integer fixes both spin and exchange sign. Odd n → fermion, even n → boson.
- **Constants:** none; n [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-QM-28 — Pauli exclusion from antisymmetry
- **Equation:** Ψ(r,r) = −Ψ(r,r) ⇒ Ψ(r,r) = 0
- **Source:** 05-SPIN_STATISTICS_DERIVATION.md §5
- **Spine path:** S0→S1→S5
- **Decrees:** D0 (and the antisymmetry from EQ-QM-27).
- **Trace:** 1=1 → S1 additive structure: an object equal to its own negation must vanish (2x=0 ⇒ x=0 in a field, S2). Applied to the antisymmetric wavefunction.
- **Constants:** none.
- **Status:** DERIVED-as-form.

### EQ-QM-29 — Twisted Dirac index = winding (generation count)
- **Equation:** index(D_A) = ∫ Â(R)∧ch(F) − (h+η(0))/2 = c₁ = n_w  (= 3 given Postulate F)
- **Source:** op02_aps_index_computation.py §1–§6; op02_kahler_spinor_derivation.md §4
- **Spine path:** S0→S1→S4→S5→S8→S9
- **Decrees:** D6 (Firmament vortex + Kähler extra-dims), D1 (6D manifold, Dirac op), D2 (U(1)_A twisting gauge field), D3 (winding n_w = 3, Postulate F), D0.
- **Trace:** 1=1 → S9 gives the Kähler 2-manifold + Dirac operator; S8 supplies the integer index via APS/Atiyah–Singer; the gauge twist (D2) injects c₁ = (1/2π)∮A·dl = n_w. Jackiw–Rossi/Weinberg give index = n_w exactly (numerically verified 1→1, 2→2, 3→3). The value "3" is **D3** (Postulate F, adopted axiom — *not* derived).
- **Constants:** c₁ = n_w [count → D3].
- **Status:** DERIVED-given-decrees (index=n_w computed; n_w=3 is D3, open to derive).

### EQ-QM-30 — Kähler closedness / spinor bundle (Theorems 1–2)
- **Equation:** Ω closed (2D ⇒ every 2-form closed) ⇒ M_⊥ Kähler;  S = Λ^{0,*}(M_⊥), D = ∂̄ + ∂̄†
- **Source:** op02_kahler_spinor_derivation.md §1–§2
- **Spine path:** S0→S1→S4→S5→S9
- **Decrees:** D6 (extra-dim geometry exists), D1 (the 2D (ξ,η) manifold), D0.
- **Trace:** 1=1 → S4 (ℂ structure) makes any oriented 2-surface complex; S9 gives the Hermitian/Kähler metric and the Dolbeault spinor bundle. Pure geometry given the manifold (D1, D6).
- **Constants:** none.
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-QM-31 — Casimir vacuum energy & force
- **Equation:** E_vac/A = −π²ℏc/(720 d³);  F/A = −π²ℏc/(240 d⁴)
- **Source:** 05-QUANTUM_PHENOMENA_CALCULATIONS.md §6 (boxed); 05-APPLIED_CALCULATIONS.md Test 1; test_qm_applied.py
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D6 (membrane zero-point modes), D1 (mode boundary conditions, 3D), D4 (ℏ, c), D0 (zeta-regularized infinite sum).
- **Trace:** 1=1 → confined EM modes ω_n=πnc/d (S6 + boundary conditions, D1) → sum of ½ℏω_n zero-point energies, zeta-regularized (S3 + D0) gives ∝ℏc/d³ → F=−dE/dd gives the 1/d⁴ force. The π²/240 is a [DERIVED ratio] (ζ(−3) arithmetic).
- **Constants:** ℏ, c [SELECTED scale → D4]; π²/240, π²/720 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D6, D1, D4).

### EQ-QM-32 — Aharonov–Bohm phase
- **Equation:** Δφ = (e/ℏ)∮A·dl = eΦ_B/ℏ
- **Source:** 05-APPLIED_CALCULATIONS.md Test 2; 05-QUANTUM_PHENOMENA §7 (boxed); test_qm_applied.py
- **Spine path:** S0→S1→S4→S6→S7→S8
- **Decrees:** D2 (U(1) gauge potential A), D4 (e, ℏ), D0.
- **Trace:** 1=1 → S7 gives the U(1) gauge connection A (that it is EM is **D2**); S4 phase accumulates ∮A·dl; Stokes (S6) gives Φ_B → Δφ = eΦ_B/ℏ. Single-valuedness (S8) makes a flux quantum return 2π.
- **Constants:** e, ℏ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-QM-33 — Flux quantum
- **Equation:** Φ₀ = h/e ⇒ Δφ(Φ₀) = 2π
- **Source:** 05-APPLIED_CALCULATIONS.md Test 2
- **Spine path:** S0→S1→S2→S8
- **Decrees:** D2 (charge e), D4 (h, e), D0.
- **Trace:** 1=1 → from EQ-QM-32 with Φ_B=h/e the phase is exactly 2π (S8 single-valuedness). The ratio h/e is the natural flux unit.
- **Constants:** h, e [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-QM-34 — Singlet correlation function
- **Equation:** E(a,b) = ⟨σ·a ⊗ σ·b⟩ = −cos θ_ab (= −a·b)
- **Source:** 05-APPLIED_CALCULATIONS.md Test 3; 05-COMPLETIONS §7; 05-QUANTUM_PHENOMENA §4
- **Spine path:** S0→S1→S4→S5→S7
- **Decrees:** D6 (ξ-η entanglement channel — physical interpretation), D2 (SU(2) spin / Pauli σ), D0.
- **Trace:** 1=1 → S5 gives the two-qubit Hilbert space + Pauli operators (SU(2), from S7 family selected by **D2**); the rotationally-invariant singlet gives correlation −cosθ. The 6D ξ-η mechanism is **D6** interpretation, not needed for the math.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D2).

### EQ-QM-35 — CHSH bound and Tsirelson violation
- **Equation:** |S| ≤ 2 (classical);  |S| = 2√2 (quantum)
- **Source:** 05-APPLIED_CALCULATIONS.md Test 3; 05-COMPLETIONS §7 (boxed); 05-QUANTUM_PHENOMENA §4 (boxed)
- **Spine path:** S0→S1→S3→S4→S5
- **Decrees:** D2 (SU(2) spin), D0.
- **Trace:** 1=1 → plugging EQ-QM-34 at optimal angles into S = E(a,b)+E(a,b')+E(a',b)−E(a',b') gives 2√2 (S3 √2). The classical ≤2 bound is a counting fact; the quantum 2√2 is the Tsirelson optimum.
- **Constants:** 2, 2√2 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D2).

### EQ-QM-36 — Quantum teleportation fidelity
- **Equation:** Bell-basis rewrite (Eq. 19–21) ⇒ F = |⟨ψ₀|Bob⟩|² = 1 (ideal); F_classical = 2/3
- **Source:** 05-APPLIED_CALCULATIONS.md Test 4; 05-COMPLETIONS §6; 05-QUANTUM_PHENOMENA §5 (boxed)
- **Spine path:** S0→S1→S4→S5→S7
- **Decrees:** D6 (entanglement channel — interpretive), D2 (SU(2)/Pauli corrections), D0.
- **Trace:** 1=1 → S5 tensor structure + Bell basis; expanding the input state and applying the Pauli (S7/D2) correction for each measurement outcome recovers |ψ₀⟩ exactly → F=1. The 2/3 classical bound is the no-entanglement guessing limit.
- **Constants:** F=1, 2/3 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D2).

### EQ-QM-37 — London penetration depth
- **Equation:** λ_L = √(m/(μ₀ n_s e²));  B(x) = B₀ e^{−x/λ_L}
- **Source:** 05-APPLIED_CALCULATIONS.md Test 5; 05-CONDENSED_MATTER §4.1 (boxed); test files
- **Spine path:** S0→S1→S3→S6→S7
- **Decrees:** D6 (condensate order parameter), D2 (U(1) gauge → massive photon), D4 (m, μ₀, n_s, e), D0.
- **Trace:** 1=1 → London relation J=−(n_s e²/mc)A (S6) + Maxwell (S7, D2) → ∇²B = B/λ_L² → exponential decay with λ_L. Higgs-type U(1) breaking is **D2/D6**.
- **Constants:** m, μ₀, n_s, e [SELECTED scale → D4]; n_s [FIT → D5] (effective superfluid density matched to data).
- **Status:** DERIVED-given-decrees (≈42% error vs Nb — free-electron approx).

### EQ-QM-38 — BEC critical temperature
- **Equation:** T_c = (2πℏ²/m k_B)·(n/ζ(3/2))^{2/3}
- **Source:** 05-APPLIED_CALCULATIONS.md Test 6; 05-CONDENSED_MATTER §5.2 (boxed); test files
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D1 (3D density of states), D4 (ℏ, m, k_B, n), D0 (ζ-function sum / integral).
- **Trace:** 1=1 → Bose occupation 1/(e^{β(ε−μ)}−1) (S2/S3); setting N = ∫g(ε)/(e^{βε}−1)dε at μ→0 with the 3D density of states (S6, D1) and the integral ∝ ζ(3/2) (D0) → invert for T_c. ζ(3/2)≈2.612 is a [DERIVED ratio].
- **Constants:** ℏ, m, k_B [SELECTED scale → D4]; n [SELECTED scale → D4]; ζ(3/2) [DERIVED ratio].
- **Status:** DERIVED-given-decrees (≈45% error for ⁴He — strong interactions).

### EQ-QM-39 — Condensate fraction
- **Equation:** N₀/N = 1 − (T/T_c)^{3/2}
- **Source:** 05-CONDENSED_MATTER §5.3
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D1 (3D), D4, D0.
- **Trace:** 1=1 → from the same Bose integral (EQ-QM-38), the excited-state population scales as (T/T_c)^{3/2} in 3D; the remainder condenses. Exponent 3/2 is a [DERIVED ratio] from the 3D density of states.
- **Constants:** none new; 3/2 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-QM-40 — Superfluid velocity from phase
- **Equation:** v_s = (ℏ/m) ∇θ
- **Source:** 05-CONDENSED_MATTER §6.1
- **Spine path:** S0→S1→S4→S6→S7
- **Decrees:** D6 (order parameter Ψ=√n₀ e^{iθ}), D4 (ℏ, m), D0.
- **Trace:** 1=1 → S4 gives the phase θ of the complex order parameter; the gauge-covariant current (S6/S7) gives v_s ∝ ∇θ with coefficient ℏ/m.
- **Constants:** ℏ, m [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6).

### EQ-QM-41 — Circulation quantization
- **Equation:** κ_n = ∮v_s·dl = 2πℏn/m = hn/m
- **Source:** 05-CONDENSED_MATTER §6.2 (boxed); test files
- **Spine path:** S0→S1→S4→S6→S8
- **Decrees:** D6, D4 (ℏ, m), D3 (winding n), D0.
- **Trace:** 1=1 → ∮∇θ·dl must be 2πn for single-valued Ψ (S8, π₁(S¹)=ℤ) → κ = hn/m. Integer n is **D3**-type winding.
- **Constants:** ℏ, h, m [SELECTED scale → D4]; n [count → D3].
- **Status:** DERIVED-given-decrees (κ₀=h/m exact for ⁴He).

### EQ-QM-42 — Landau critical velocity
- **Equation:** v_L = min_q [ω(q)/q]
- **Source:** 05-CONDENSED_MATTER §6.4
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D6 (excitation spectrum), D4, D0.
- **Trace:** 1=1 → energy/momentum balance for creating an excitation (S1 conservation) gives the minimum velocity for dissipation as the infimum of ω(q)/q (S6 + D0).
- **Constants:** none dimensionful (spectrum-dependent).
- **Status:** DERIVED-as-form (given D6).

### EQ-QM-43 — Bloch's theorem
- **Equation:** ψ_{k,n}(x) = e^{ikx} u_{k,n}(x),  u(x+R)=u(x);  E_n(k+2π/R)=E_n(k)
- **Source:** 05-CONDENSED_MATTER §2.2
- **Spine path:** S0→S1→S4→S6→S7
- **Decrees:** D1 (lattice manifold + ∇²), D4 (lattice constant R), D0.
- **Trace:** 1=1 → discrete translation symmetry T_R commutes with H (S7 group structure); shared eigenstates carry a Bloch phase e^{ikx} times a periodic envelope (S4/S6). R is **D4**.
- **Constants:** R [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-QM-44 — Band gap from Bragg scattering
- **Equation:** ΔE_gap ≈ 2|V_G|,  V_G = (1/R)∫₀^R V(x)e^{−iGx}dx,  at k=π/R
- **Source:** 05-CONDENSED_MATTER §2.3
- **Spine path:** S0→S1→S4→S6→S7
- **Decrees:** D1 (lattice), D4 (V₀, R), D0.
- **Trace:** 1=1 → degenerate plane waves at the Bragg condition 2k=G (S7 reciprocal lattice) mix; perturbation lifts the degeneracy by 2|V_G| (S6 Fourier coefficient). V_G is **D4**.
- **Constants:** V_G, R [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-QM-45 — Cooper pair binding energy
- **Equation:** ε_pair = −ℏω_D exp(−1/(N(0)V))
- **Source:** 05-CONDENSED_MATTER §3.2
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D6 (phonon = membrane mode), D4 (ℏ, ω_D), D5 (N(0)V coupling matched to data), D0.
- **Trace:** 1=1 → integral equation for the bound state in the energy shell ℏω_D (S6) → exponential weak-coupling solution. The product N(0)V (~0.2–0.4) is **D5** (matched to the material).
- **Constants:** ℏω_D [SELECTED scale → D4]; N(0)V [FIT → D5].
- **Status:** DERIVED-given-decrees.

### EQ-QM-46 — BCS gap
- **Equation:** Δ(0) = 2ℏω_D exp(−1/(N(0)V))
- **Source:** 05-CONDENSED_MATTER §3.3 (boxed); test files
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D6, D4 (ℏ, ω_D), D5 (N(0)V), D0.
- **Trace:** 1=1 → mean-field gap equation 1 = N(0)V·sinh⁻¹(ℏω_D/Δ) (S6 integral, D0) → weak-coupling solution. Same structure as EQ-QM-45.
- **Constants:** ℏω_D [SELECTED scale → D4]; N(0)V [FIT → D5].
- **Status:** DERIVED-given-decrees (≈26% error Nb).

### EQ-QM-47 — Critical temperature & universal ratio
- **Equation:** k_B T_c = 1.134 ℏω_D exp(−1/(N(0)V));  2Δ(0)/(k_B T_c) = 2π/e^γ ≈ 3.528
- **Source:** 05-CONDENSED_MATTER §3.4 (boxed)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D6, D4 (ℏ, ω_D, k_B), D5 (N(0)V), D0.
- **Trace:** 1=1 → T_c is where Δ→0 in the gap equation; the gap-to-T_c ratio 2π/e^γ is coupling-independent (a [DERIVED ratio], with Euler γ). 1.134 = e^γ/π type factor.
- **Constants:** ℏω_D, k_B [SELECTED scale → D4]; N(0)V [FIT → D5]; 3.528, 1.134 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-QM-48 — Proca (massive photon) Lagrangian in SC
- **Equation:** ℒ_Proca = −¼F_{μν}F^{μν} + ½ m_γ² A_μ A^μ;  m_γ ~ e n_s ℏ/(mc²)
- **Source:** 05-CONDENSED_MATTER §4.2
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2 (U(1) gauge field), D6 (condensate breaking U(1)), D4 (e, n_s), D0.
- **Trace:** 1=1 → S7 gives the U(1) field strength F_{μν} (D2); spontaneous symmetry breaking by the condensate (D6) adds a mass term → photon acquires mass m_γ ~ 1/λ_L. (δS=0 borderline, S6.)
- **Constants:** e, n_s [SELECTED scale → D4]; n_s [FIT → D5].
- **Status:** DERIVED-as-form (δS=0 borderline; given D2, D6).

### EQ-QM-49 — Effective cosmological-constant-scale ℏω/2 (zero point)
- **Equation:** E₀,n = ½ℏω_n per mode
- **Source:** 05-APPLIED_CALCULATIONS.md Overview; 05-QED_PRECISION §1.4
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D6 (membrane oscillation), D4 (ℏ), D0.
- **Trace:** 1=1 → S6 quantizes each membrane oscillator mode; the ground-state energy is ½ℏω (the harmonic-oscillator zero point). Membrane never ceases oscillating (D6).
- **Constants:** ℏ [SELECTED scale → D4]; ½ [DERIVED ratio].
- **Status:** DERIVED-as-form (given D6).

### EQ-QM-50 — Photon energy
- **Equation:** E_photon = ℏω = hf
- **Source:** 05-COMPLETIONS §8 (Eq. 24, boxed); 05-QUANTUM_PHENOMENA §2
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D2 (EM field from KK), D4 (ℏ), D0.
- **Trace:** 1=1 → quantized field mode (S6) with phase e^{−iωt} (S4) carries energy quanta ℏω. The EM identification is **D2**.
- **Constants:** ℏ, h [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D2).

### EQ-QM-51 — Photoelectric equation
- **Equation:** E_k = hf − W (= hf − φ);  f_threshold = W/h
- **Source:** 05-COMPLETIONS §8 (Eq. 25, boxed); 05-QUANTUM_PHENOMENA §2 (boxed)
- **Spine path:** S0→S1→S6
- **Decrees:** D2 (photon), D4 (h, W), D5 (work function W matched per material), D0.
- **Trace:** 1=1 → energy conservation (S1) at the surface: photon ℏω = binding W + kinetic. W is material-specific **D5**.
- **Constants:** h [SELECTED scale → D4]; W (e.g. 2.36 eV Na) [FIT → D5].
- **Status:** DERIVED-given-decrees.

### EQ-QM-52 — Compton wavelength & shift
- **Equation:** λ_C = h/(m_e c);  Δλ = (h/m_e c)(1 − cos θ)
- **Source:** 05-COMPLETIONS §9 (Eq. 27, boxed); 05-QUANTUM_PHENOMENA §3 (boxed)
- **Spine path:** S0→S1→S2→S3→S4
- **Decrees:** D2 (photon EM), D4 (h, m_e, c), D0.
- **Trace:** 1=1 → relativistic 4-momentum conservation (S1 conservation, S3 √) for photon–electron collision → eliminate recoil angle → Δλ = λ_C(1−cosθ). λ_C = h/m_e c is set by D4.
- **Constants:** h, m_e, c [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-QM-53 — Electron recoil & Klein–Nishina
- **Equation:** E_e = ℏω_i − ℏω_f;  dσ/dΩ = (r₀²/2)(ω_f/ω_i)²(ω_i/ω_f + ω_f/ω_i − sin²θ)
- **Source:** 05-COMPLETIONS §9 (Eq. 28, 31, boxed)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2 (QED vertex, charge), D4 (ℏ, m_e, r₀), D0.
- **Trace:** 1=1 → conservation (S1) gives recoil energy; the QED differential cross section follows from the electron–photon vertex (S7, D2) with classical electron radius r₀ = αℏ/(m_e c).
- **Constants:** ℏ, m_e, r₀ [SELECTED scale → D4]; α [DERIVED ratio]/[FIT → D5] (see EQ-QM-62).
- **Status:** DERIVED-given-decrees.

### EQ-QM-54 — Non-degenerate perturbation theory
- **Equation:** E_n^{(1)} = ⟨n⁰|H'|n⁰⟩;  E_n^{(2)} = Σ_{k≠n} |⟨k⁰|H'|n⁰⟩|²/(E_n⁰−E_k⁰)
- **Source:** 05-COMPLETIONS §1 (Eq. 1–3, boxed)
- **Spine path:** S0→S1→S2→S5
- **Decrees:** D1 (Hilbert space), D0.
- **Trace:** 1=1 → expand the eigenvalue problem (H₀+λH')|n⟩=E_n|n⟩ in powers of λ (S2 power series, S5 eigenproblem) → order-by-order corrections. Pure linear algebra given the Hilbert space (D1).
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form.

### EQ-QM-55 — Degenerate perturbation (W matrix)
- **Equation:** W_{ij} = ⟨n_i⁰|H'|n_j⁰⟩;  diagonalize W
- **Source:** 05-COMPLETIONS §1 (Eq. 4, boxed)
- **Spine path:** S0→S1→S5
- **Decrees:** D1, D0.
- **Trace:** 1=1 → within a degenerate subspace, the correct zeroth-order basis diagonalizes the perturbation matrix (S5 eigenvalues). Linear algebra.
- **Constants:** none.
- **Status:** DERIVED-as-form.

### EQ-QM-56 — Variational principle
- **Equation:** E[ψ] = ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ ≥ E₀;  ∂E/∂α_i = 0
- **Source:** 05-COMPLETIONS §2 (Eq. 5–6, boxed)
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D1 (Hilbert space), D0.
- **Trace:** 1=1 → expand trial state in eigenbasis (S5); since all E_n ≥ E₀, the weighted average ≥ E₀. Minimizing over parameters (S6, δ=0) gives the best bound. Helium gives −24.4 eV (0.8%).
- **Constants:** none dimensionful (energies are consequences of D4 inputs).
- **Status:** DERIVED-as-form (δS=0 borderline at the minimization step).

### EQ-QM-57 — WKB ansatz & quantization
- **Equation:** ψ = A(x)e^{iS/ℏ}, (S')²=2m(E−V), A=C/⁴√p;  ∮p dx=2πnℏ, ∫√(2m(E−V))dx=(n+½)πℏ
- **Source:** 05-COMPLETIONS §3 (Eq. 7–11, boxed)
- **Spine path:** S0→S1→S3→S4→S6→S8
- **Decrees:** D4 (ℏ, m), D3 (quantization integer n), D0.
- **Trace:** 1=1 → S4 phase ansatz in the Schrödinger equation; leading ℏ→0 order gives the Hamilton–Jacobi (S')²=2m(E−V) (S6) → amplitude from the next order → Bohr–Sommerfeld loop quantization (S8) fixes the integer n. Exact for the harmonic oscillator.
- **Constants:** ℏ, m [SELECTED scale → D4]; n, ½ [count → D3]/[DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-QM-58 — Harmonic oscillator spectrum
- **Equation:** E_n = (n+½)ℏω
- **Source:** 05-COMPLETIONS §3 (boxed)
- **Spine path:** S0→S1→S3→S6→S8
- **Decrees:** D4 (ℏ, ω), D3 (n), D0.
- **Trace:** 1=1 → WKB (EQ-QM-57) on V=½mω²x² gives exactly (n+½)ℏω; reproduces the algebraic ladder result. The ½ is the zero point (S8 turning-point phase).
- **Constants:** ℏ, ω [SELECTED scale → D4]; n [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-QM-59 — Path integral / propagator
- **Equation:** K = ∫𝒟x exp(iS[x]/ℏ);  Z(β)=∫𝒟x exp(−S_E[x]);  𝒜_tunnel ~ exp(−S_B/ℏ)
- **Source:** 05-COMPLETIONS §4 (Eq. 12–15, boxed)
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D1 (configuration space), D4 (ℏ), D0 (functional measure).
- **Trace:** 1=1 → slice the time-evolution operator e^{−iHt/ℏ} (S6), insert position resolutions (S5), short-time propagator gives e^{iS_slice/ℏ} (S4) → continuum limit is the sum over paths weighted by e^{iS/ℏ}. δS=0 selects the classical path (S6 borderline).
- **Constants:** ℏ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (δS=0 borderline; functional measure needs D0).

### EQ-QM-60 — Density matrix, reduced state, von Neumann entropy
- **Equation:** ρ=|ψ⟩⟨ψ|;  ⟨O⟩=Tr(ρO);  ρ_A=Tr_B(ρ_AB);  S(ρ)=−Tr(ρ log₂ ρ)
- **Source:** 05-COMPLETIONS §5 (Eq. 16–18, boxed)
- **Spine path:** S0→S1→S5
- **Decrees:** D1 (Hilbert space), D0.
- **Trace:** 1=1 → S5 supplies the operator/Hilbert-space formalism, tensor products, partial trace, and the spectral entropy. Bell state gives S_A=1 bit. Pure linear algebra.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form.

### EQ-QM-61 — He first-order correction
- **Equation:** E^{(1)} = 5e²/(8πε₀a₀) = (5/8)·13.6 eV = 8.5 eV
- **Source:** 05-COMPLETIONS §1 (numerical)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D2 (Coulomb), D4 (e², a₀), D0.
- **Trace:** 1=1 → the electron–electron Coulomb integral over 1s orbitals (EQ-QM-54 applied to He) evaluates to 5/8 of the Rydberg. The 5/8 is a [DERIVED ratio] (orbital integral).
- **Constants:** e², a₀ [SELECTED scale → D4]; 5/8 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-QM-62 — Fine-structure constant from 6D geometry
- **Equation:** α⁻¹ = 1.44·ln(ξ_A/η_B) = 137.036;  α = e²/(4πε₀ℏc)
- **Source:** 05-COMPLETIONS §9 (Eq. 32, boxed); 05-QED_PRECISION §7.3; 05-QM_FROM_MEMBRANE §9.2
- **Spine path:** S0→S1→S2→S3→S9
- **Decrees:** D2 (U(1)_A coupling), D1 (6D→4D KK integral), D4 (ξ_A, η_B), D5 (the prefactor 1.44 and precise match to 137.036), D0.
- **Trace:** 1=1 → the 6D gauge coupling reduces to 4D via a logarithmic integral over the warped extra dimensions (S9, D1) → α⁻¹ ∝ ln(ξ_A/η_B). The coefficient 1.44 and the precise value 137.036 are not derived to 2-loop precision (the raw formula gives ~137.18), so the calibration is **D5**.
- **Constants:** ξ_A, η_B [SELECTED scale → D4]; 1.44, 137.036 [FIT → D5]; ln-ratio [DERIVED ratio].
- **Status:** PARTIAL (UV form derived given D1/D2; precision to 137.036 is D5 — an honest open item).

### EQ-QM-63 — Schwinger anomalous moment (one-loop)
- **Equation:** a_e^{(1)} = F₂(0)/… = α/(2π) ≈ 0.001161
- **Source:** 05-QED_LOOPS_DERIVATION.md §3.3 (boxed); 05-QED_PRECISION §2.2–§2.4
- **Spine path:** S0→S1→S2→S5→S6→S7
- **Decrees:** D2 (QED vertex / charge), D1 (6D KK propagator, loop integral), D4 (m_e), D5 (α value), D0.
- **Trace:** 1=1 → the one-loop vertex correction (S6/S7 gauge theory, D2) with Feynman-parameter + loop integrals (S6, D1, D0) gives F₂(0) → a_e=α/(2π). The KK tower (D1) provides natural UV regularization. α enters from EQ-QM-62.
- **Constants:** α [FIT → D5]; m_e [SELECTED scale → D4]; 1/(2π) [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-QM-64 — Higher-loop g−2 series & total
- **Equation:** a_e = α/2π + A₂(α/π)² + A₃(α/π)³ + … = 0.00115965218…
- **Source:** 05-QED_LOOPS_DERIVATION.md §4; 05-QED_PRECISION §2.5–§2.6, §7.1
- **Spine path:** S0→S1→S2→S5→S6→S7
- **Decrees:** D2, D1, D4 (m_e), D5 (α; loop coefficients A₂=−0.328…, A₃=1.181…), D0.
- **Trace:** 1=1 → enumerate two-/three-/four-loop diagram topologies and integrate (S6/S7, D1, D0); the rational/numerical coefficients A_n are [DERIVED ratio] (loop integrals) but their *use* with measured α is **D5**. Matches experiment to ~10⁻¹².
- **Constants:** α [FIT → D5]; A₂, A₃ [DERIVED ratio]; m_e [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-QM-65 — Lamb shift
- **Equation:** ΔE_{2S−2P} = ΔE_SE + ΔE_VP = 1057.845 MHz;  V_VP ∝ −(α²/15π)…δ³(r)
- **Source:** 05-QED_LOOPS_DERIVATION.md §5; 05-QED_PRECISION §3
- **Spine path:** S0→S1→S2→S5→S6→S7
- **Decrees:** D2 (QED), D1 (KK regularization), D4 (m_e, a₀), D5 (α), D0.
- **Trace:** 1=1 → self-energy (electron coupling to virtual photon modes) + vacuum polarization (Uehling potential from virtual pairs), both one-loop QED (S6/S7, D2), regularized by the KK cutoff (D1) → 1057.845 MHz. The S-state contact term uses |ψ_{2S}(0)|² from EQ-QM-20.
- **Constants:** m_e, a₀ [SELECTED scale → D4]; α [FIT → D5].
- **Status:** DERIVED-given-decrees.

### EQ-QM-66 — Natural UV cutoff from membrane thickness
- **Equation:** Λ_UV = ħc/η_B;  m_{n,m}² = m₀² + π²n²/ξ_A² + π²m²/η_B²;  Σ 1/N^{2p} converges
- **Source:** 05-QED_LOOPS_DERIVATION.md §7; 05-QED_PRECISION §5
- **Spine path:** S0→S1→S2→S3→S5→S6
- **Decrees:** D6 (membrane thickness η_B), D1 (KK mode tower), D4 (ħ, c, η_B, ξ_A), D0.
- **Trace:** 1=1 → KK mode masses grow as N/η_B (S5/S6, D1); the mode sum Σ1/N^{2p} converges (S3, D0), giving a finite cutoff Λ_UV = ħc/η_B. Cutoff set by the membrane thickness (D6/D4). NB: CT-4.Λ corrects the *numerical* value to ≈0.152 GeV (see EQ-QM-67).
- **Constants:** ħ, c, η_B, ξ_A [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-QM-67 — Corrected zone UV cutoff (CT-4.Λ)
- **Equation:** Λ_zone = ħc/η_B = 0.152 GeV ≈ Λ_QCD
- **Source:** LAMBDA_ZONE_CORRECTION_CT4L.md §1 (boxed)
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D6 (η_B = confinement scale), D4 (ħ, c, η_B), D0.
- **Trace:** 1=1 → S2 quotient ħc/η_B with η_B=1.3 fm gives 152 MeV (the QCD scale), correcting the earlier erroneous Planck-scale value. Pure arithmetic given the D4 scales.
- **Constants:** ħ, c, η_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (corrected).

### EQ-QM-68 — Vacuum energy density & Waters suppression (n=1)
- **Equation:** ρ_vac = Λ_zone⁴/(8π²);  ρ_eff = ρ_vac·(η_B/ξ_A) = (ħc)³/(8π² η_B³ ξ_A) ≈ 2.93×10⁻⁴⁷ GeV⁴
- **Source:** LAMBDA_ZONE_CORRECTION_CT4L.md §4.3; N1_DERIVATION_CT4L_OPEN_WATERS.md (Eq. N1.7, boxed)
- **Spine path:** S0→S1→S2→S3→S5→S9
- **Decrees:** D6 (Waters-Above vacuum + single equilibration channel), D1 (KK mode counting), D3 (exponent n=1 as a one-channel/zero-mode count), D4 (η_B, ξ_A), D0.
- **Trace:** 1=1 → ρ_vac counts zero-point modes to the cutoff (S6/S3, D0) → only the KK zero-mode survives, fraction 1/N_KK = η_B/ξ_A (S5 counting, D1) → ρ_eff suppressed by one power (n=1). The exponent n=1 has a structural (not yet rigorous) justification; it is a **D3**-type count (single channel / single zero-mode). 20% agreement with ρ_DE.
- **Constants:** η_B, ξ_A [SELECTED scale → D4]; n=1 [count → D3]; 1/(8π²) [DERIVED ratio].
- **Status:** PARTIAL (n=1 structurally argued, rigorous derivation pending OP-A_ξ).

### EQ-QM-69 — Decoherence time & g_int
- **Equation:** τ_D ~ ħ/(g_int² ρ_env k_B T)·(λ_th/Δx)²;  g_int = Ψ_{B,0}²/M_Pl
- **Source:** op09_decoherence_time.py; op09_collapse_resolution.md §1–§2
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D6 (Ψ_B Waters-Below coupling = environment), D4 (ħ, k_B, M_Pl, m_B), D5 (g_int anchored to condensate mass; order-of-magnitude), D0.
- **Trace:** 1=1 → Caldeira–Leggett-type decoherence formula (S6) with the environment coupling g_int derived from the Ψ_B condensate interaction L_int = (1/M_Pl)ψ̄ψ|Ψ_B|² (D6). g_int is now anchored to m_B (OP-03) rather than free, but remains order-of-magnitude (D5).
- **Constants:** ħ, k_B, M_Pl, m_B [SELECTED scale → D4]; g_int [FIT → D5].
- **Status:** PARTIAL (g_int derived to within an order of magnitude).

### EQ-QM-70 — Bohr magneton & electron magnetic moment
- **Equation:** μ⃗ = g₀·(e/2m_e)·S⃗;  μ_B = eℏ/(2m_e) = 9.285×10⁻²⁴ J/T;  μ_e = μ_B;  g_e = 2(1 + a_e)
- **Source:** 05-QED_PRECISION_CALCULATIONS.md §2.1 (boxed Eq. for μ_B; Eq. for μ⃗ and g_e); 05-QM_FROM_MEMBRANE_DYNAMICS.md §9.3 (consistency check #5–6)
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D2 (U(1)_A charge e + the spin/SU(2) coupling that defines the gyromagnetic g₀), D4 (e, ℏ, m_e dimensionful), D3 (spin/winding sets the half-integer S; see EQ-QM-17/24), D0.
- **Trace:** 1=1 → the minimal U(1) coupling of the charged defect (S7, D2) gives the magnetic moment μ⃗ ∝ (e/2m_e)S⃗ (S6 current ⇒ moment); the natural unit is μ_B = eℏ/(2m_e) (S2 quotient of the D4 scales), and the tree-level gyromagnetic ratio g₀ = 2 follows from the Dirac/relativistic structure with the anomalous part a_e from EQ-QM-63/64. The half-integer spin S that μ⃗ multiplies is the D3-type winding (EQ-QM-24).
- **Constants:** e, ℏ, m_e [SELECTED scale → D4]; μ_B = 9.285×10⁻²⁴ J/T [SELECTED scale → D4] (consequence of D4 inputs); g₀ = 2 [DERIVED ratio]; a_e [DERIVED ratio]/[FIT → D5] via EQ-QM-63/64.
- **Status:** DERIVED-given-decrees.

---

## UNTRACEABLE items (honest gaps — no chain fabricated)

### UNTRACEABLE-A — Why a single measurement outcome occurs ("collapse")
- **Statement:** The ontological selection of ONE outcome in a measurement (beyond decoherence-suppressed interference).
- **Reason:** op09_collapse_resolution.md explicitly states this is "NOT resolvable within the zone framework" and is open in *all* of physics. Decoherence (EQ-QM-22) explains suppression of interference and pointer-basis selection, but not which branch is realized. No spine rung or decree forces a single outcome — this is neither grammar (S0–S9) nor an enumerated decree (D0–D6). Marked UNTRACEABLE per the honesty rule rather than fabricating a chain.

### UNTRACEABLE-B — Born rule as a first-principles theorem
- **Statement:** P(outcome) = |ψ|² as a derived law (not a heuristic).
- **Reason:** EQ-QM-23 gives only a heuristic energy-transfer argument; op09 and op09_collapse_resolution.md both list "Born rule from zone" as NOT resolved (requires a separate derivation, Vol 4 Ch 1, not present in this domain). The |ψ|²-energy-density identification is a D6 *interpretation*, not a derivation of the probability postulate. No rung/decree supplies the measure-theoretic step.

### UNTRACEABLE-C — Value n_w = 3 (three generations) and the bare Λ_Z0 / ξ₀ magnitudes from first principles
- **Statement:** That the winding is *3* (EQ-QM-29), and the independent first-principles values of ξ₀ (EQ-QM-07/08) and κ₆².
- **Reason:** n_w = 3 is **Postulate F**, an explicitly *adopted* axiom (D3 selects the integer; the framework states board #849 tracks deriving it but it is not derived here). Likewise ξ₀ and κ₆² are blocked by RT-1.WF / OP-G6. These are honestly *selected* inputs, not derivations. (Listed here for completeness of the coverage audit; within the ledger they are correctly tagged D3/D5 rather than claimed as DERIVED. The genuinely untraceable residue is the *origin* of the integer 3 and of κ₆², which lies outside both spine and decree register as anything other than a selection.)

---

*Cross-ref: `SPINE.md` (S0–S9), `DECREE_REGISTER.md` (D0–D6), `README_SCHEMA.md`.*
*Domain agent: Quantum_Mechanics. UNRATIFIED exploratory ledger.*
