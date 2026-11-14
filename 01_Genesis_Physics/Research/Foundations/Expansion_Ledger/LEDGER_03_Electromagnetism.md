# Expansion Ledger — Domain 03: Electromagnetism

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> Per-domain trace of every displayed/named equation in
> `Research/Mathematical_Models/03_Electromagnetism/` back to the seed `1=1`,
> via the spine rungs S0–S9 (`SPINE.md`) and decrees D0–D6 (`DECREE_REGISTER.md`).
> Honesty rule: no equation is "derived from `1=1` alone" — each = spine path + named decrees.
> Reference docs cited by ID, never re-derived.

## Header

| Field | Value |
|-------|-------|
| Domain | Electromagnetism (03) |
| Files traced | `03-MAXWELL_DERIVATION.md`, `03-COMPLETIONS.md`, `03-APPLICATIONS.md`, `03-APPLIED_PHENOMENA.md`, `03-CONDENSED_MATTER_DERIVATION.md`, `03-PRECISION_COMPLETIONS.md`, `test_em_applications.py` |
| # equations traced | 67 (EQ-EM-01 … EQ-EM-67) |
| Decrees used across domain | D0 (ℝ continua), D1 (6D/4D manifold, KK), D2 (U(1) gauge field), D3 (winding ⇒ charge/flux/circulation quantization: EQ-EM-34/35/64 only), D4 (dimensionful scale anchor), D5 (fitted O(1) / data-matched constants), D6 (Firmament/membrane physical content) |
| # PARTIAL | 6 (EQ-EM-04, -05, -09, -25, -26, -60) |
| # UNTRACEABLE | 2 (UT-EM-01 cyclotron; UT-EM-02 spectroscopic/atomic formulas) — both cross-domain |

Notes on this domain:
- The `.py` test suite (`test_em_applications.py`) contains no equations distinct from the `.md`
  sources — its formulas (dispersion ω=ck, skin depth δ, photoelectric E=hf−W, Compton Δλ) are
  identical to those traced below; it is treated as scaffolding per Schema rule 5.
- Maxwell's equations here are obtained as the **U(1) sector of a KK reduction** of a 6D action.
  That makes them **S7 (gauge) + D1 (the manifold/extra dims) + D2 (the U(1) member) + D6 (the
  zone/membrane geometry supplying the warp profile)** — DERIVED-as-form given those decrees.
  The *form* (a free 1-form gauge field's Euler–Lagrange + Bianchi) is genuinely S6/S7 grammar.
- α⁻¹ = 1.44 ln(ξ_A/η_B): the **logarithm of a scale ratio is geometry (DERIVED ratio)**, but the
  **coefficient 1.44 = b_eff/2π is a Standard-Model beta-function input matched to data (FIT → D5)**,
  and the endpoints ξ_A, η_B are selected scales (D4). So α⁻¹ is PARTIAL, not fully derived.

---

### EQ-EM-01 — 6D metric ansatz with gauge fields (KK)
- **Equation:** ds² = e^{2A(ξ,η)}[ g^{(4)}_{μν} dx^μ dx^ν + 2A_μ^ξ dx^μ dξ + 2A_μ^η dx^μ dη ] + e^{2B(ξ,η)}(dξ²+dη²)
- **Source:** 03-MAXWELL_DERIVATION.md §1.1 (boxed)
- **Spine path:** S0→S3→S5→S9
- **Decrees:** D0, D1, D6 (D2 for the gauge-field interpretation of off-diagonal terms)
- **Trace:** 1=1 → S3/D0 gives the ℝ continuum the coordinates live on → S5 gives independent
  directions/dimension count → S9 builds the (pseudo-)Riemannian metric on a manifold. D1 fixes the
  dimension at 6; D6 supplies the zone/Firmament warp profile e^{2A}, e^{2B}; the off-diagonal
  g_{μξ}=A_μ is the KK gauge field (D2).
- **Constants:** warp factors A(ξ,η),B(ξ,η) [SELECTED scale → D4 / D6 profile]; zone edges ξ_A, η_B [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-EM-02 — 6D volume element
- **Equation:** √(−g₆) = e^{2A+2B} √(−g^{(4)})
- **Source:** 03-MAXWELL_DERIVATION.md §1.2 (boxed)
- **Spine path:** S0→S3→S5→S9
- **Decrees:** D0, D1, D6
- **Trace:** Pure determinant algebra of the EQ-EM-01 block metric to leading order in A_μ. The
  manifold/dimension is D1; the warp content is D6. No new physics input.
- **Constants:** warp factors [SELECTED scale → D4 / D6].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-EM-03 — Gauge coupling from KK volume
- **Equation:** g_EM² = (∫₀^{ξ_A}dξ e^{2A} ∫₀^{η_B}dη e^{2B})⁻¹ × κ₆²  ;  1/g_EM² = V_extra/κ₆²
- **Source:** 03-MAXWELL_DERIVATION.md §2.1 (boxed)
- **Spine path:** S0→S3→S5→S6→S9
- **Decrees:** D0, D1, D4, D6
- **Trace:** 1=1 → S6 supplies the integral over the extra coordinates → integrating the EQ-EM-01
  metric over (ξ,η) leaves a 4D coupling. D1 gives the extra dims to integrate out; D6 the warp
  profile; D4 sets κ₆ (the 6D gravitational scale) as a chosen unit.
- **Constants:** κ₆² [SELECTED scale → D4]; V_extra (∝ ξ_A, η_B) [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D4, D6).

### EQ-EM-04 — Warp profile (Waters Above)
- **Equation:** A(ξ,η₀) = A₀ + (λ/2) ln(ξ/ξ_ref)
- **Source:** 03-MAXWELL_DERIVATION.md §2.2
- **Spine path:** S0→S3→S9
- **Decrees:** D0, D1, D6
- **Trace:** This is a *posited* profile of the zone metric (D6 physical content), expressed on the
  ℝ continuum (S3) over the manifold (S9/D1). It is an input, not a derivation.
- **Constants:** λ≈0.05 [FIT → D5]; A₀, ξ_ref [SELECTED scale → D4].
- **Status:** PARTIAL (profile is a D6-input; λ is a fitted parameter).

### EQ-EM-05 — Warp profile (Waters Below)
- **Equation:** B(ξ₀,η) = B₀ − (γ/2) η
- **Source:** 03-MAXWELL_DERIVATION.md §2.2
- **Spine path:** S0→S3→S9
- **Decrees:** D0, D1, D6
- **Trace:** Same as EQ-EM-04 — a chosen suppression profile of the membrane (D6).
- **Constants:** γ≈10¹⁵ m⁻¹ [SELECTED scale → D4]; B₀ [SELECTED scale → D4].
- **Status:** PARTIAL (D6-input profile).

### EQ-EM-06 — Effective volume integrals V_A, V_B
- **Equation:** V_A ≈ (e^{2A₀}/λ) ξ_A ln(ξ_A/ξ_ref);  V_B = e^{2B₀}(1−e^{−γη_B})/γ
- **Source:** 03-MAXWELL_DERIVATION.md §2.3–2.4
- **Spine path:** S0→S3→S6
- **Decrees:** D0, D4, D6
- **Trace:** S6 integration of the EQ-EM-04/05 profiles over the ℝ continuum (S3). Arithmetic only.
- **Constants:** ξ_A, η_B, γ, λ [SELECTED scale → D4 / FIT → D5 for λ].
- **Status:** DERIVED-as-form (given the D6 profiles and D4 scales).

### EQ-EM-07 — Effective coupling in zone parameters
- **Equation:** g_EM² = κ₆² / (e^{2A₀+2B₀} · V_factor),  V_factor = (ξ_A/λ)ln(ξ_A/ξ_ref)·(1−e^{−γη_B})/γ
- **Source:** 03-MAXWELL_DERIVATION.md §2.5 (boxed)
- **Spine path:** S0→S3→S6→S9
- **Decrees:** D0, D1, D4, D6
- **Trace:** Substitute EQ-EM-06 into EQ-EM-03. Pure algebra on top of the integrated warp volume.
- **Constants:** κ₆², ξ_A, η_B [SELECTED scale → D4]; λ [FIT → D5].
- **Status:** DERIVED-as-form (given D1, D4, D6).

### EQ-EM-08 — Fine structure constant from coupling
- **Equation:** α = g_EM²/(4πℏc);  α = g_EM²/(4π) in natural units
- **Source:** 03-MAXWELL_DERIVATION.md §2.5
- **Spine path:** S0→S2→S4→S6→S7
- **Decrees:** D0, D2, D4
- **Trace:** S4 gives the phase/circle (the 4π is the solid angle of the gauge sphere via S4's π),
  S7 the U(1) coupling (D2); dividing the dimensionful coupling g_EM² (D4) by 4πℏc forms the
  dimensionless α. The *definition* is grammar; the *value* depends on g_EM².
- **Constants:** 4π [DERIVED ratio]; ℏ, c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (definition); value PARTIAL (inherits g_EM²).

### EQ-EM-09 — α⁻¹ from log scale ratio
- **Equation:** α⁻¹ = 4π/g_EM² = 1.44 ln(ξ_A/η_B) ≈ 1.44 × 95.2 ≈ 137.04
- **Source:** 03-MAXWELL_DERIVATION.md §2.5, §5.4, §10 (boxed); cross-ref DERIVE_FINE_STRUCTURE_COEFFICIENT.md
- **Spine path:** S0→S2→S3→S5→S7→S9
- **Decrees:** D0, D1, D2, D4, D5, D6
- **Trace:** 1=1 → S2 gives the ratio ξ_A/η_B → S3 the logarithm on ℝ → S9/D6 the warp geometry
  whose KK integral produces a *logarithmic* coupling. The endpoints ξ_A, η_B are selected scales
  (D4); the prefactor 1.44 = b_eff/2π is the SM beta-function coefficient matched to data (D5).
- **Constants:** ln(ξ_A/η_B)≈95.2 [DERIVED ratio]; 1.44 = b_eff/2π [FIT → D5]; ξ_A, η_B [SELECTED scale → D4].
- **Status:** PARTIAL (geometry gives the log; 1.44 is a fitted SM input).

### EQ-EM-10 — 4D electromagnetic action
- **Equation:** S_EM^{(4)} = −(1/4g_EM²) ∫ d⁴x √(−g) F_{μν}F^{μν}
- **Source:** 03-MAXWELL_DERIVATION.md §3.1 (boxed)
- **Spine path:** S0→S5→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** S7 gives the gauge-invariant quadratic-in-curvature action of a connection 1-form; S9/D1
  the manifold and √(−g); D2 selects U(1); D6/KK supplies the 1/g_EM² normalization (EQ-EM-07).
  Form `δS=0` borderline (S6 note).
- **Constants:** g_EM² [SELECTED scale → D4, value from EQ-EM-07].
- **Status:** DERIVED-as-form (δS=0 borderline; given D1, D2, D6).

### EQ-EM-11 — Field strength tensor
- **Equation:** F_{μν} = ∂_μ A_ν − ∂_ν A_μ
- **Source:** 03-MAXWELL_DERIVATION.md §3.1; test_em_applications.py header
- **Spine path:** S0→S6→S7
- **Decrees:** D2
- **Trace:** S7 gives the connection/gauge potential A_μ (U(1) ⇐ D2, free phase from S4); S6 the
  derivative ∂. The curvature of a U(1) connection is the antisymmetrized derivative — pure grammar.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D2).

### EQ-EM-12 — Gauge transformation from 6D reparameterization
- **Equation:** ξ → ξ + Λ(x)  induces  A_μ → A_μ − ∂_μ Λ  (and A → A+∇χ, φ → φ−∂_t χ)
- **Source:** 03-MAXWELL_DERIVATION.md §3.1, §8.1
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D1, D2
- **Trace:** S7 identity-preserving maps (diffeomorphism in the ξ-direction, D1) act on the
  off-diagonal metric as the U(1) gauge shift of A_μ. This is Noether/reparameterization grammar.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1, D2).

### EQ-EM-13 — EM equation of motion (covariant, vacuum + source)
- **Equation:** ∂_α F^{αμ} = 0 (vacuum);  ∂_α F^{αμ} = g_EM² J^μ (with current)
- **Source:** 03-MAXWELL_DERIVATION.md §3.2 (boxed)
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** δS_EM/δA_μ=0 (S6 variational, borderline) on EQ-EM-10 yields the Euler–Lagrange eq;
  the source term comes from adding S_int=∫A_μJ^μ. Two of Maxwell's four equations in one line.
- **Constants:** g_EM² [SELECTED scale → D4].
- **Status:** DERIVED-as-form (δS=0 borderline; given D1, D2, D6).

### EQ-EM-14 — Interaction action / minimal coupling
- **Equation:** S_interaction = ∫ d⁴x A_μ J^μ
- **Source:** 03-MAXWELL_DERIVATION.md §3.2
- **Spine path:** S0→S6→S7
- **Decrees:** D2
- **Trace:** S7 gauge invariance forces matter to couple to A_μ through the conserved current J^μ
  (minimal coupling). U(1) ⇐ D2.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D2).

### EQ-EM-15 — Bianchi identity (homogeneous Maxwell)
- **Equation:** ∂_μ ⋆F^{μν} = 0
- **Source:** 03-MAXWELL_DERIVATION.md §3.3 (boxed)
- **Spine path:** S0→S6→S7→S8
- **Decrees:** D1, D2
- **Trace:** F=dA ⇒ dF=0 identically (S6 exterior derivative, S8 topology of the closed form). This
  is a topological identity for any U(1) connection (D2) on the manifold (D1) — no equations of
  motion needed. Encodes Faraday + no-monopoles.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1, D2).

### EQ-EM-16 — E, B fields from F
- **Equation:** E^i = F^{0i};  B^k = ½ ε^{ijk} F_{ij}
- **Source:** 03-MAXWELL_DERIVATION.md §4.1
- **Spine path:** S0→S5→S6→S7
- **Decrees:** D1, D2
- **Trace:** A 3+1 split (S5 dimension/index structure on the D1 manifold) of the field tensor
  EQ-EM-11 into its electric (time-space) and magnetic (space-space) components. Definitional.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1, D2).

### EQ-EM-17 — Gauss's law
- **Equation:** ∇·E = ρ/ε₀
- **Source:** 03-MAXWELL_DERIVATION.md §4.2; 03-APPLICATIONS.md, 03-APPLIED_PHENOMENA.md §1.1
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** μ=0 component of EQ-EM-13 (∂_α F^{αμ}=g_EM²J^μ) in the 3+1 split EQ-EM-16, with the
  identification ε₀=1/(g_EM²c²) (EQ-EM-23).
- **Constants:** ε₀ [SELECTED scale → D4, value via g_EM²].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-18 — No magnetic monopoles
- **Equation:** ∇·B = 0
- **Source:** 03-MAXWELL_DERIVATION.md §4.2 (boxed); 03-APPLIED_PHENOMENA.md §1.1
- **Spine path:** S0→S6→S7→S8
- **Decrees:** D1, D2
- **Trace:** Spatial divergence of B from the Bianchi identity EQ-EM-15; topologically forced (S8)
  because B=∇×A. The doc ties it to the trivial winding of the ξ-circle (no monopole charge).
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1, D2).

### EQ-EM-19 — Faraday's law
- **Equation:** ∇×E = −∂B/∂t
- **Source:** 03-MAXWELL_DERIVATION.md §4.2 (boxed); 03-APPLIED_PHENOMENA.md §1.1
- **Spine path:** S0→S6→S7→S8
- **Decrees:** D1, D2
- **Trace:** Space-time component of the Bianchi identity EQ-EM-15. Grammar (dF=0), no source.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1, D2).

### EQ-EM-20 — Ampère–Maxwell law
- **Equation:** ∇×B = μ₀(J + ε₀ ∂E/∂t)
- **Source:** 03-MAXWELL_DERIVATION.md §4.2 (boxed); 03-APPLIED_PHENOMENA.md §1.1
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Spatial component of EQ-EM-13 with the identifications μ₀=g_EM², ε₀μ₀=1/c²
  (EQ-EM-23/24). The displacement current ε₀∂E/∂t is the time part of ∂_αF^{αi}.
- **Constants:** μ₀, ε₀ [SELECTED scale → D4]; c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-21 — ε₀μ₀ = 1/c²
- **Equation:** ε₀ μ₀ = 1/c²
- **Source:** 03-MAXWELL_DERIVATION.md §4.2, §5.1 (boxed)
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D4, D6
- **Trace:** Forced by matching the covariant EQ-EM-13/15 to the SI 3-vector form: the two
  couplings ε₀=1/(g_EM²c²), μ₀=g_EM² multiply to 1/c². Consistency relation, not independent.
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-EM-22 — Speed of light from metric signature
- **Equation:** ds²=0 ⇒ |dx|/dt = 1, i.e. c = 299792458 m/s
- **Source:** 03-MAXWELL_DERIVATION.md §5.2 (boxed); 03-APPLIED_PHENOMENA.md §1.2 (c=1/√(μ₀ε₀))
- **Spine path:** S0→S3→S9
- **Decrees:** D0, D1, D4, D6
- **Trace:** The null cone of the Lorentzian 4D metric (S9, signature from D6/D1) fixes the invariant
  speed; its numerical value is the chosen unit (D4 — "1 in chosen units" is the SI metre/second).
- **Constants:** c [SELECTED scale → D4]; signature (+−−−) [structural, D1/D6].
- **Status:** DERIVED-as-form for the invariant; the *number* is D4 (unit convention).

### EQ-EM-23 — ε₀ in terms of g_EM
- **Equation:** ε₀ = 1/(g_EM² c²)
- **Source:** 03-MAXWELL_DERIVATION.md §4.2, §5.3 (boxed)
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Coefficient-matching the 4D EM action EQ-EM-10 to the SI Lagrangian ½(ε₀E²−B²/μ₀).
- **Constants:** g_EM², c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-24 — μ₀ in terms of g_EM
- **Equation:** μ₀ = g_EM²
- **Source:** 03-MAXWELL_DERIVATION.md §4.2, §5.3 (boxed)
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Same coefficient match as EQ-EM-23; μ₀ is the KK coupling itself.
- **Constants:** g_EM² [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-25 — ε₀ numerical value
- **Equation:** ε₀ = e²/(4π α ℏ c) = 8.854×10⁻¹² F/m
- **Source:** 03-MAXWELL_DERIVATION.md §5.4 (boxed)
- **Spine path:** S0→S2→S4→S6→S7
- **Decrees:** D0, D2, D4, D5
- **Trace:** Invert the α definition (EQ-EM-37) for ε₀ and plug CODATA e, α, ℏ, c. The value is set
  by α (PARTIAL, EQ-EM-09) and chosen units (D4).
- **Constants:** e, ℏ, c [SELECTED scale → D4]; α [FIT/PARTIAL → D5 via EQ-EM-09]; 4π [DERIVED ratio].
- **Status:** PARTIAL (inherits α; otherwise unit-matched).

### EQ-EM-26 — μ₀ numerical value
- **Equation:** μ₀ = 1/(ε₀ c²) = 1.257×10⁻⁶ H/m
- **Source:** 03-MAXWELL_DERIVATION.md §5.4 (boxed)
- **Spine path:** S0→S2→S6
- **Decrees:** D0, D4
- **Trace:** Algebra from EQ-EM-21 given ε₀ (EQ-EM-25) and c (EQ-EM-22).
- **Constants:** ε₀, c [SELECTED scale → D4].
- **Status:** PARTIAL (inherits ε₀).

### EQ-EM-27 — Coulomb potential / law
- **Equation:** ∇²φ = −ρ/ε₀;  φ = q/(4πε₀ r);  E = q/(4πε₀ r²) r̂;  F = qq'/(4πε₀ r²) r̂
- **Source:** 03-MAXWELL_DERIVATION.md §6.1 (boxed F)
- **Spine path:** S0→S3→S4→S5→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Static limit of Gauss's law EQ-EM-17 (S6 Laplacian on ℝ³); the 1/r Green's function of
  ∇² in 3D (S5 dimension count = 3 ⇐ D1 reduction). 4π is the solid angle (S4). (S4/S5 are used by the
  trace and are now listed in the spine path.)
- **Constants:** ε₀ [SELECTED scale → D4]; 4π [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-28 — EM wave equation (E and B)
- **Equation:** ∇²E = μ₀ε₀ ∂²E/∂t² = (1/c²)∂²E/∂t²  (same for B)
- **Source:** 03-MAXWELL_DERIVATION.md §7.1 (boxed); 03-APPLICATIONS.md Test 1; 03-APPLIED_PHENOMENA.md §1.2
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Curl of Faraday (EQ-EM-19) + Ampère (EQ-EM-20) in vacuum, vector identity
  ∇×(∇×E)=∇(∇·E)−∇²E with ∇·E=0. S6 supplies the d'Alembertian □.
- **Constants:** c (via μ₀ε₀) [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-29 — Dispersion relation / plane wave
- **Equation:** k² = μ₀ε₀ ω² ⇒ k = ω/c, c = 1/√(μ₀ε₀), v_phase = v_group = c, ω = c|k|
- **Source:** 03-MAXWELL_DERIVATION.md §7.2 (boxed); 03-APPLICATIONS.md Test 1 (boxed); 03-APPLIED_PHENOMENA.md §1.3; 03-PRECISION_COMPLETIONS.md §1.2; test_em_applications.py Test 1
- **Spine path:** S0→S4→S6→S9
- **Decrees:** D0, D1, D4, D6
- **Trace:** Substitute the S4 plane wave e^{i(k·r−ωt)} into the wave equation EQ-EM-28. Phase from
  S4 (ℂ exponential); c is the metric-fixed speed.
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-EM-30 — EM energy density
- **Equation:** u = ½(ε₀E² + B²/μ₀)
- **Source:** 03-MAXWELL_DERIVATION.md §7.3
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Time-time component of the EM stress-energy tensor T^{μν} from the action EQ-EM-10
  (S7 Noether energy of the field).
- **Constants:** ε₀, μ₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-31 — Poynting vector
- **Equation:** S = (1/μ₀) E×B  ;  S = c u for a plane wave
- **Source:** 03-MAXWELL_DERIVATION.md §7.3 (boxed); 03-APPLIED_PHENOMENA.md §5.3
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Space-time (T^{0i}) component of the EM stress-energy tensor — the Noether energy
  flux. μ₀ from EQ-EM-24.
- **Constants:** μ₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-32 — Charge conservation / continuity
- **Equation:** ∂_μ J^μ = 0  ⇔  ∂ρ/∂t + ∇·J = 0
- **Source:** 03-MAXWELL_DERIVATION.md §8.2; 03-COMPLETIONS.md §2.1
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D2
- **Trace:** 1=1 → S1 gives the additive conservation form a+(−a)=0 → S7 (Noether) ties the U(1)
  gauge symmetry (D2) to a conserved current → divergence of EQ-EM-13 (∂_μ∂_νF^{νμ}=0 by
  antisymmetry) forces ∂_μJ^μ=0.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1, D2).

### EQ-EM-33 — Poynting's theorem (energy conservation)
- **Equation:** ∂u/∂t + ∇·S = −J·E
- **Source:** 03-MAXWELL_DERIVATION.md §8.3 (boxed)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** S1 conservation form + S7 (Noether, time translation) applied to the field T^{μν};
  substitute Maxwell's equations into ∂u/∂t. The −J·E is the source/sink (Joule heating).
- **Constants:** ε₀, μ₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-34 — Dirac / flux quantization
- **Equation:** ∮_C A·dl = Φ_B = 2πn/e, n∈ℤ;  Φ₀ = h/e
- **Source:** 03-MAXWELL_DERIVATION.md §9.1 (boxed)
- **Spine path:** S0→S4→S7→S8
- **Decrees:** D0, D2, D3
- **Trace:** 1=1 → S4 gives the ℂ phase of Ψ → S8 (π₁(S¹)=ℤ) forces the phase winding around a
  loop to be an integer multiple of 2π → single-valuedness quantizes the enclosed flux. Integer ⇐ D3.
- **Constants:** e, h [SELECTED scale → D4]; n [count → D3].
- **Status:** DERIVED-as-form (given D2, D3).

### EQ-EM-35 — Electric charge quantization
- **Equation:** q = n · q_unit, n∈ℤ
- **Source:** 03-MAXWELL_DERIVATION.md §9.2 (boxed)
- **Spine path:** S0→S4→S7→S8
- **Decrees:** D2, D3
- **Trace:** S8 winding number of the ξ-circle (D2/D3): charges are labelled by the integer winding,
  forcing q to come in integer units. The unit q_unit is set by the ξ-circle geometry (D6).
- **Constants:** q_unit [SELECTED scale → D4 / D6]; n [count → D3].
- **Status:** DERIVED-as-form (given D2, D3); unit magnitude PARTIAL.

### EQ-EM-36 — Photoelectric equation
- **Equation:** hf = W + E_kin  ⇔  E_kin = hf − W;  f₀ = W/h;  eV_s = hf − W
- **Source:** 03-APPLICATIONS.md Test 4 (boxed); test_em_applications.py Test 4
- **Spine path:** S0→S1→S4→S6→S7
- **Decrees:** D0, D4, D6
- **Trace:** 1=1 → S1 energy bookkeeping (in = out) → photon energy E=hf is the quantized field mode
  (S4 phase / S7 mode, membrane quantization ⇐ D6). Energy conservation gives the line equation.
- **Constants:** h [SELECTED scale → D4]; W [SELECTED scale → D4 / material datum, FIT → D5].
- **Status:** DERIVED-as-form (given D6); W is an empirical material constant.

### EQ-EM-37 — Photon energy & E = hf
- **Equation:** E_photon = hf = hc/λ;  fλ = c
- **Source:** 03-APPLIED_PHENOMENA.md §1.3 (boxed); 03-PRECISION_COMPLETIONS.md §1.1; Test files
- **Spine path:** S0→S4→S7
- **Decrees:** D0, D4, D6
- **Trace:** fλ=c is the dispersion EQ-EM-29 rewritten. E=hf is the quantization of the field
  oscillator (S4 phase quantum / S7 mode), supplied by membrane quantization (D6); h sets the unit.
- **Constants:** h [SELECTED scale → D4]; c [SELECTED scale → D4]; hc=1240 eV·nm [SELECTED scale → D4] (a *product of two dimensionful* constants ⇒ dimensionful [energy·length], NOT a dimensionless geometric ratio; tagged D4 per Decree rule 1).
- **Status:** DERIVED-as-form (given D6).

### EQ-EM-38 — Compton scattering shift
- **Equation:** Δλ = λ' − λ = (h/m_e c)(1 − cos θ) = λ_C(1 − cos θ);  λ_C = h/(m_e c) = 2.426 pm
- **Source:** 03-APPLICATIONS.md Test 5 (boxed); test_em_applications.py Test 5
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D0, D4
- **Trace:** 1=1 → S1 conservation (energy & 3-momentum books balance) applied to a relativistic
  photon (E=hf, p=h/λ via S4) + electron at rest; eliminate the electron variables algebraically.
- **Constants:** h, m_e, c [SELECTED scale → D4]; (1−cos θ) [DERIVED ratio].
- **Status:** DERIVED-as-form (given relativistic kinematics; D4 units).

### EQ-EM-39 — Ohm's law / Drude conductivity
- **Equation:** m dv/dt = −eE − mγv ⇒ v = −eE/(mγ);  J = σE,  σ = ne²/(mγ) = ne²τ/m;  ρ=1/σ
- **Source:** 03-COMPLETIONS.md §1.1–1.3 (boxed J=σE, σ)
- **Spine path:** S0→S1→S6
- **Decrees:** D0, D4, D6
- **Trace:** 1=1 → S1 (force balance, Newton's law from EQ in domain 01) + S6 ∂_t; steady-state drift
  gives σ. Material content (n, τ, the lattice) is condensed-matter physics on the membrane (D6).
- **Constants:** n, τ, m, e [SELECTED scale → D4]; γ=1/τ [material datum, FIT → D5].
- **Status:** DERIVED-as-form (given D6); σ value is empirical.

### EQ-EM-40 — Joule heating
- **Equation:** P = I²R;  P/V = J²ρ = σE²
- **Source:** 03-COMPLETIONS.md §1.3; 03-APPLIED_PHENOMENA.md §5.3
- **Spine path:** S0→S1→S6
- **Decrees:** D0, D4, D6
- **Trace:** Power = J·E (from Poynting source term EQ-EM-33) with J=σE (EQ-EM-39). Algebra.
- **Constants:** σ, ρ [SELECTED scale → D4 / FIT → D5].
- **Status:** DERIVED-as-form (given D6).

### EQ-EM-41 — Kirchhoff's current law
- **Equation:** ∇·J = 0 (steady) ⇒ Σ I = 0 at a node
- **Source:** 03-COMPLETIONS.md §2.1
- **Spine path:** S0→S1→S6
- **Decrees:** D0, D1
- **Trace:** Steady-state continuity EQ-EM-32 + divergence theorem (S6 integral over a node volume,
  D1 manifold). Charge conservation specialized to circuits.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-EM-42 — Kirchhoff's voltage law
- **Equation:** ∮ E·dl = 0 (electrostatic) ⇒ Σ ΔV = 0;  ε − IR − Q/C = 0 (RC loop)
- **Source:** 03-COMPLETIONS.md §2.2
- **Spine path:** S0→S1→S6
- **Decrees:** D0, D1
- **Trace:** E=−∇φ (conservative field, S1 potential) ⇒ closed-loop integral of a gradient is zero
  (S6 fundamental theorem). Energy conservation around the loop.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-EM-43 — Capacitance (parallel plate)
- **Equation:** C = Q/V = ε₀A/d;  with dielectric C = ε₀ε_r A/d;  D = ε₀ε_r E
- **Source:** 03-COMPLETIONS.md §3.3, §3.5 (boxed)
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Gauss's law EQ-EM-17 on a parallel-plate geometry (EA=Q/ε₀) with E=V/d. ε_r is a
  material polarization response (D6).
- **Constants:** ε₀ [SELECTED scale → D4]; ε_r [material datum, FIT → D5].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-44 — Capacitor energy
- **Equation:** U = ½ε₀E²·(Ad) = ½CV² = ½Q²/C
- **Source:** 03-COMPLETIONS.md §3.4
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Integrate the field energy density EQ-EM-30 over the capacitor volume; substitute
  EQ-EM-43.
- **Constants:** ε₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-45 — Inductance (solenoid) & induced EMF
- **Equation:** B = μ₀NI/ℓ;  L = Ψ/I = μ₀N²A/ℓ;  ε = −dΦ_B/dt = −L dI/dt;  V_L = L dI/dt
- **Source:** 03-COMPLETIONS.md §4.2–4.3 (boxed L, V_L)
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Ampère's law EQ-EM-20 gives the solenoid B; flux linkage Ψ=NΦ defines L; Faraday's law
  EQ-EM-19 gives the induced EMF. N is a turn count.
- **Constants:** μ₀ [SELECTED scale → D4]; N [plain integer — a design turn-count, NOT the topological n_w-winding decree, so it is *not* D3]; A, ℓ [geometry].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-46 — Inductor energy
- **Equation:** U_L = ½ L I²
- **Source:** 03-COMPLETIONS.md §4.4 (boxed)
- **Spine path:** S0→S6
- **Decrees:** D0, D4
- **Trace:** ∫ V_L I dt = ∫ L I dI (S6 integration) using EQ-EM-45.
- **Constants:** L [SELECTED scale → D4].
- **Status:** DERIVED-as-form.

### EQ-EM-47 — LC oscillation
- **Equation:** d²Q/dt² + Q/(LC) = 0  ⇒  ω₀ = 1/√(LC);  f = 1/(2π√(LC))
- **Source:** 03-COMPLETIONS.md §4.5 (boxed); §5.4 resonance ω_res=ω₀
- **Spine path:** S0→S4→S6
- **Decrees:** D0, D4
- **Trace:** KVL EQ-EM-42 on an LC loop with I=dQ/dt yields the SHO equation (S6 second derivative);
  its eigenfrequency (S4 circle/phase of the harmonic solution).
- **Constants:** L, C [SELECTED scale → D4].
- **Status:** DERIVED-as-form.

### EQ-EM-48 — RLC damped oscillator & resonance
- **Equation:** L Q̈ + R Q̇ + Q/C = 0 (and =V₀cosωt driven);  ω_d=√(ω₀²−Γ²), Γ=R/2L;  I₀(ω)=V₀/√(R²+(ωL−1/ωC)²);  tanδ=(ωL−1/ωC)/R;  Z=R+i(ωL−1/ωC)
- **Source:** 03-COMPLETIONS.md §5.1–5.4 (boxed I₀, ω_res)
- **Spine path:** S0→S4→S6
- **Decrees:** D0, D4
- **Trace:** KVL EQ-EM-42 with R, L, C terms gives a damped-driven SHO (S6); ℂ impedance and the
  three damping regimes follow from the characteristic roots (S4 complex exponentials).
- **Constants:** R, L, C [SELECTED scale → D4].
- **Status:** DERIVED-as-form.

### EQ-EM-49 — Skin depth & decay in a conductor
- **Equation:** ∇²E ≈ μ₀σ ∂E/∂t;  k²=−iωμ₀σ, k=(1−i)/δ;  δ = √(2/(ωμ₀σ)) = 1/√(πfμ₀σ) = √(2ρ/(ωμ₀));  E(z)=E₀e^{−z/δ}
- **Source:** 03-COMPLETIONS.md §7.1–7.3 (boxed δ); 03-APPLICATIONS.md Test 3 (boxed); 03-APPLIED_PHENOMENA.md §4.2 (boxed); 03-PRECISION_COMPLETIONS.md §3.3 (boxed); test_em_applications.py Test 3
- **Spine path:** S0→S4→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Maxwell in a conductor (Ohm's law EQ-EM-39 + Ampère EQ-EM-20) gives a diffusion equation;
  plug the S4 plane wave, solve the complex k. σ, ρ are material data (D6).
- **Constants:** μ₀ [SELECTED scale → D4]; σ, ρ [material datum, FIT → D5].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-50 — Shielding effectiveness
- **Equation:** SE = 20 log₁₀(E_in/E_out) = 8.686 (t/δ) dB
- **Source:** 03-COMPLETIONS.md §6.5; 03-APPLICATIONS.md Test 2; 03-PRECISION_COMPLETIONS.md §2.5 (boxed); 03-APPLIED_PHENOMENA.md §3.5
- **Spine path:** S0→S3→S6
- **Decrees:** D0, D4, D6
- **Trace:** Take 20 log₁₀ of the exponential decay EQ-EM-49 over thickness t. ln/log on ℝ (S3).
- **Constants:** 8.686 = 20/ln10 [DERIVED ratio]; t, δ [geometry / material].
- **Status:** DERIVED-as-form (given EQ-EM-49).

### EQ-EM-51 — AC resistance from skin effect
- **Equation:** R(f) = ρℓ/(2πaδ) ⇒ R ∝ √f;  R_AC/R_DC = 2r/δ (r≫δ)
- **Source:** 03-APPLIED_PHENOMENA.md §4.5; 03-PRECISION_COMPLETIONS.md §3.7
- **Spine path:** S0→S3→S6
- **Decrees:** D0, D4, D6
- **Trace:** R=ρℓ/A_eff with effective area = surface × skin depth (EQ-EM-49); δ∝f^{−1/2} gives the
  √f scaling.
- **Constants:** ρ [material datum, FIT → D5]; geometry r, ℓ.
- **Status:** DERIVED-as-form (given EQ-EM-49).

### EQ-EM-52 — EM boundary conditions
- **Equation:** E_{1∥}=E_{2∥};  D_{1⊥}=D_{2⊥} (ε₁E_{1⊥}=ε₂E_{2⊥});  H_{1∥}=H_{2∥} (B_{1∥}/μ₁=B_{2∥}/μ₂);  B_{1⊥}=B_{2⊥}
- **Source:** 03-COMPLETIONS.md §8.2–8.5 (boxed); 03-APPLIED_PHENOMENA.md §3.2
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Apply Maxwell's equations (Faraday EQ-EM-19, Gauss EQ-EM-17/18, Ampère EQ-EM-20) in
  integral form to a vanishing loop/pillbox straddling the interface (S6).
- **Constants:** ε₁,ε₂,μ₁,μ₂ [material data, FIT → D5].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-EM-53 — Snell's law
- **Equation:** k₁sinθ₁ = k₂sinθ₂ ⇒ n₁sinθ₁ = n₂sinθ₂
- **Source:** 03-COMPLETIONS.md §8.7 (boxed)
- **Spine path:** S0→S4→S6→S9
- **Decrees:** D0, D1, D6
- **Trace:** Continuity of the tangential wavevector at the interface (from EQ-EM-52 / phase matching
  of the S4 plane waves), with n=c/v.
- **Constants:** n₁, n₂ [material data, FIT → D5].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-EM-54 — Vacuum impedance
- **Equation:** Z₀ = √(μ₀/ε₀) = 377 Ω
- **Source:** 03-APPLIED_PHENOMENA.md "Physical Constants" table
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D4, D6
- **Trace:** Ratio of E/H amplitudes for a vacuum plane wave (EQ-EM-29), expressed via ε₀, μ₀.
- **Constants:** μ₀, ε₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6).

### EQ-EM-55 — Firmament wave speed c² = σ/μ
- **Equation:** c = √(σ/μ);  c² = σ/μ ≈ 9.0×10¹⁶ m²/s²
- **Source:** 03-APPLICATIONS.md Foundational table; 03-APPLIED_PHENOMENA.md; 03-CONDENSED_MATTER §Foundation; 03-PRECISION_COMPLETIONS.md §1.1; AXIOM_MEMBRANE_MECHANICS_v2.md
- **Spine path:** S0→S3→S9
- **Decrees:** D0, D1, D4, D6
- **Trace:** Membrane wave speed = √(tension/density) — the standard elastic-membrane result (S6 wave
  eq on the S9 manifold), with σ (Firmament tension) and μ (surface density) as D6 physical content;
  their magnitudes are chosen scales (D4) calibrated so c matches EQ-EM-22.
- **Constants:** σ, μ [SELECTED scale → D4 / D6]; c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6); σ, μ values are anchored to reproduce c.

---

## Condensed-matter block (03-CONDENSED_MATTER_DERIVATION.md + 03-PRECISION_COMPLETIONS.md Parts 4–5)

### EQ-EM-56 — Electron–phonon Hamiltonian
- **Equation:** H = H_e + H_ph + H_{e-ph} with H_e=Σε_k c†c, H_ph=Σℏω_q(b†b+½), H_{e-ph}=Σ g c†c(b†+b)
- **Source:** 03-CONDENSED_MATTER_DERIVATION.md §Foundation
- **Spine path:** S0→S4→S5→S6→S7
- **Decrees:** D0, D1, D4, D6
- **Trace:** Second-quantized field operators (S5 Hilbert space, S7 mode operators) for electrons and
  membrane lattice phonons (D6). The coupling g is membrane-deformation physics (D6).
- **Constants:** ε_k, ω_q, g [SELECTED scale → D4 / material, FIT → D5].
- **Status:** DERIVED-as-form (given D6); model Hamiltonian, parameters empirical.

### EQ-EM-57 — Cooper binding energy
- **Equation:** E_binding = −2ℏω_D e^{−1/λ},  λ=N(0)V
- **Source:** 03-CONDENSED_MATTER_DERIVATION.md §1
- **Spine path:** S0→S3→S5→S6
- **Decrees:** D0, D4, D6
- **Trace:** Two-electron bound-state problem above the Fermi sea with a contact attraction within
  ℏω_D (S5 Hilbert space, S6 integral over the shell); the exponential is the log-divergent DOS integral.
- **Constants:** ℏω_D [SELECTED scale → D4 / D6]; λ=N(0)V [material datum, FIT → D5].
- **Status:** DERIVED-as-form (given D6); coupling empirical.

### EQ-EM-58 — BCS gap equation & gap
- **Equation:** 1 = N(0)V ∫₀^{ℏω_D} dε/(2√(ε²+Δ²)) = (N(0)V/2) sinh⁻¹(ℏω_D/Δ);  Δ = 2ℏω_D e^{−1/N(0)V}
- **Source:** 03-CONDENSED_MATTER_DERIVATION.md §1 (boxed); 03-PRECISION_COMPLETIONS.md §4.3 (boxed)
- **Spine path:** S0→S3→S5→S6→S7
- **Decrees:** D0, D4, D6
- **Trace:** Mean-field (S7) diagonalization of the pairing Hamiltonian gives quasiparticle energies
  E_k=√(ε²+Δ²); the self-consistency integral (S6 over ℝ, S3) yields Δ. Membrane phonons supply ω_D (D6).
- **Constants:** ℏω_D [SELECTED scale → D4]; N(0)V [material datum, FIT → D5].
- **Status:** DERIVED-as-form (given D6); value empirical.

### EQ-EM-59 — Debye cutoff frequency
- **Equation:** ω_D = v_s (6π²N)^{1/3}/V;  ℏω_D ~ ℏc/a
- **Source:** 03-PRECISION_COMPLETIONS.md §4.2; 03-CONDENSED_MATTER §1
- **Spine path:** S0→S3→S5→S6
- **Decrees:** D0, D1, D4, D6
- **Trace:** Counting phonon modes up to the Brillouin-zone boundary (S5 dimension/mode count) at sound
  speed v_s (membrane, D6). The 3D mode count uses the dimension D1; the (6π²)^{1/3} is the S5 sphere-
  packing geometry. N is the (ordinary) atom/site count of the sample — a plain integer, NOT the
  topological n_w-winding decree, so D3 is *not* invoked here.
- **Constants:** v_s, a [SELECTED scale → D4 / D6]; N [plain integer site count — not D3]; (6π²)^{1/3} [DERIVED ratio].
- **Status:** DERIVED-as-form (given D6).

### EQ-EM-60 — Superconducting critical temperature
- **Equation:** T_c = (ω_D/πk_B) e^{−1/N(0)V} = Δ(0)/(πk_B);  strong-coupling: T_c=(ω_D/πk_B)e^{−(1+λ)/(λ−μ_c(1+λ))}
- **Source:** 03-PRECISION_COMPLETIONS.md §4.4, §4.5–4.6 (boxed)
- **Spine path:** S0→S3→S5→S6→S7
- **Decrees:** D0, D4, D5, D6
- **Trace:** Finite-T BCS gap equation; T_c is where Δ→0. Strong-coupling form (McMillan) adds the
  fitted Coulomb pseudopotential μ_c and coupling λ matched to each material.
- **Constants:** ω_D [SELECTED scale → D4]; λ, μ_c [FIT → D5]; k_B [SELECTED scale → D4].
- **Status:** PARTIAL (form derived; T_c values require fitted λ, μ_c — D5).

### EQ-EM-61 — London equations & penetration depth
- **Equation:** ∂J_s/∂t = (n_s e²/m_e)E;  ∇×J_s = −(n_e e²/m_e)B;  ∇²B = B/λ_L²;  λ_L = √(m_e/(μ₀ n_s e²));  B(z)=B₀e^{−z/λ_L}
- **Source:** 03-CONDENSED_MATTER_DERIVATION.md §2 (boxed); 03-PRECISION_COMPLETIONS.md §5.2–5.4 (boxed)
- **Spine path:** S0→S4→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Minimal coupling p→p−(e/c)A (S7/D2) of the macroscopic order parameter Ψ; the rigid
  phase response gives the London relation; curl + Ampère EQ-EM-20 yields the screening (∇²B=B/λ_L²).
  Coherent condensate is membrane physics (D6).
- **Constants:** m_e, e, μ₀ [SELECTED scale → D4]; n_s [material datum, FIT → D5].
- **Status:** DERIVED-as-form (given D2, D6).

### EQ-EM-62 — BEC critical temperature
- **Equation:** ⟨n_k⟩=1/(e^{β(ε−μ)}−1);  N=CVT_BEC^{3/2};  T_BEC = (2πℏ²/k_B m)(n/ζ(3/2))^{2/3}
- **Source:** 03-CONDENSED_MATTER_DERIVATION.md §3 (boxed)
- **Spine path:** S0→S3→S5→S6→S7
- **Decrees:** D0, D1, D4, D6
- **Trace:** Bose occupation (S7 statistics/mode operators of identical bosons) summed over modes with
  the 3D density of states g(ε)∝√ε (S5 dimension count ⇐ D1); condensation when the excited-state
  integral saturates. ζ(3/2) is the Riemann zeta value (S3/S6). (S7 is used by the trace and is now in
  the spine path.)
- **Constants:** ℏ, k_B, m [SELECTED scale → D4]; n [SELECTED scale → D4]; ζ(3/2)≈2.612 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-EM-63 — Condensate order parameter
- **Equation:** Ψ(r) = √n₀ e^{iφ(r)};  Ψ_total = Π_j Ψ(r_j)
- **Source:** 03-CONDENSED_MATTER_DERIVATION.md §3; §4
- **Spine path:** S0→S4→S5→S7
- **Decrees:** D0, D6
- **Trace:** Macroscopic occupation of a single ℂ mode (S4 phase, S5 Hilbert space) — spontaneously
  broken U(1) (S7). Membrane coherence (D6).
- **Constants:** n₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6).

### EQ-EM-64 — Superfluid velocity & circulation quantization
- **Equation:** v_s = (ℏ/m)∇φ;  ∮ v_s·dl = 2πnℏ/m = nκ, κ=h/m;  Γ = n h/m
- **Source:** 03-CONDENSED_MATTER_DERIVATION.md §4 (boxed iff)
- **Spine path:** S0→S4→S6→S8
- **Decrees:** D0, D3, D6
- **Trace:** v_s from the phase gradient of Ψ (EQ-EM-63); single-valuedness around a loop forces the
  phase winding to be an integer (S8, π₁(S¹)=ℤ; integer ⇐ D3), quantizing circulation in units h/m.
- **Constants:** ℏ, m [SELECTED scale → D4]; n [count → D3]; κ=h/m [SELECTED scale → D4] (the circulation quantum is *dimensionful* [m²/s] = ratio of two dimensionful constants ⇒ D4, not a dimensionless geometric ratio).
- **Status:** DERIVED-as-form (given D3, D6).

### EQ-EM-65 — Vortex energy per length
- **Equation:** E_v = (πℏ²n₀/m) ln(R/ξ)
- **Source:** 03-CONDENSED_MATTER_DERIVATION.md §4
- **Spine path:** S0→S3→S6→S8
- **Decrees:** D0, D4, D6
- **Trace:** Integrate the kinetic energy ½ρ_s v_s² of the 1/r circulating flow (EQ-EM-64) from core
  ξ to size R (S6); the log is the 2D integral of 1/r² (S3).
- **Constants:** ℏ, m, n₀ [SELECTED scale → D4]; ln(R/ξ) [DERIVED ratio].
- **Status:** DERIVED-as-form (given D6).

### EQ-EM-66 — Two-fluid momentum density
- **Equation:** ρ = ρ_s + ρ_n;  g = ρ_s v_s + ρ_n v_n
- **Source:** 03-CONDENSED_MATTER_DERIVATION.md §4
- **Spine path:** S0→S1→S5
- **Decrees:** D0, D6
- **Trace:** S1 additive split of one fluid into two components (superfluid + normal); momentum is the
  weighted sum (S5 vector). Two-fluid model is membrane-coherence physics (D6).
- **Constants:** ρ_s, ρ_n [SELECTED scale → D4 / material].
- **Status:** DERIVED-as-form (given D6).

### EQ-EM-67 — Dipole (Larmor) radiation field & power
- **Equation:** E_rad = (μ₀/4π)(p̈/rc) sinθ;  P_rad = (μ₀/6πc) ω² p̈²
- **Source:** 03-PRECISION_COMPLETIONS.md §1.4.1 (radio-wave generation)
- **Spine path:** S0→S5→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Solve the sourced EM equation of motion EQ-EM-13 (∂_α F^{αμ}=g_EM²J^μ) with a retarded
  Green's function on the Lorentzian manifold (S9/D1; S6 supplies the d'Alembertian and its retarded
  inverse); the far-field (radiation) part of the accelerating-dipole source J^μ gives E_rad ∝ p̈/r,
  and the Poynting flux EQ-EM-31 integrated over a sphere gives the Larmor power P_rad ∝ ω²p̈². U(1)
  gauge field ⇐ D2; μ₀=g_EM² ⇐ D6/KK (EQ-EM-24). This is genuine EM-domain physics (unlike the
  cross-domain generation mechanisms in UT-EM-01/02), so it is traced here rather than marked untraceable.
- **Constants:** μ₀ [SELECTED scale → D4]; c [SELECTED scale → D4]; 4π, 6π [DERIVED ratio] (solid-angle factors from S4).
- **Status:** DERIVED-as-form (given D1, D2, D6).

---

## UNTRACEABLE

### UT-EM-01 — Cyclotron / magnetron resonance frequency
- **Equation:** ω_c = eB/m  (used to "generate" microwaves; ν_c ≈ 1.76×10¹¹·B)
- **Source:** 03-PRECISION_COMPLETIONS.md §1.4.2
- **Reason:** This is the Lorentz-force cyclotron relation, which belongs to the Classical Mechanics /
  charged-particle-dynamics domain (Lorentz force F=qv×B), not derived anywhere in the EM domain files.
  It is *cited* as a source mechanism but no trace to the spine is given here; tracing it requires the
  Lorentz-force law from another domain's ledger. Marked UNTRACEABLE within this domain to avoid
  fabricating a chain.

### UT-EM-02 — Empirical spectroscopic/material formulas (Wien, Rydberg/Balmer, Bremsstrahlung, K-shell ionization)
- **Equation:** ν_peak=5.88×10¹⁰/T (Wien); ν=R_H c(1/2²−1/n²) (Balmer); E=13.6 eV·Z_eff²(1/n₁²−1/n₂²); E_max=eV (Bremsstrahlung)
- **Source:** 03-PRECISION_COMPLETIONS.md §1.4.3–1.4.7
- **Reason:** These belong to thermodynamics/blackbody (Wien) and atomic/quantum spectra (Rydberg,
  ionization) domains. They are quoted as *generation mechanisms* for EM spectral bands, not derived in
  the EM files. Their constants (5.88×10¹⁰, R_H, 13.6 eV) are empirical/atomic inputs with no
  EM-domain spine path; tracing them is the job of the Thermodynamics (02) and Quantum/Atomic (05)
  ledgers. Marked UNTRACEABLE here.

---

*End of LEDGER_03_Electromagnetism.md — UNRATIFIED exploratory trace.*
