# Expansion Ledger — Domain 04: Optics and Waves

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This ledger traces every displayed/numbered equation and named key result in the
> `04_Optics_and_Waves` domain back to the seed `1=1` via the spine rungs (`SPINE.md`,
> S0–S9) plus named decrees (`DECREE_REGISTER.md`, D0–D6). No equation is "derived from
> `1=1` alone": every physics equation = spine path + decrees + equation-specific algebra.
> Constants are tagged `[DERIVED ratio]` / `[SELECTED scale → D4]` / `[FIT → D5]` /
> `[count → D3]`. Arithmetic, ℝ, ℂ are cited by rung ID, never re-derived.

## Header table

| Metric | Value |
|--------|-------|
| **# equations traced** | 43 |
| **Decrees used across domain** | D0 (completed-ℝ), D1 (dimension/manifold = 6→4D), D2 (gauge group / EM U(1)), D4 (scale anchor → c, σ, μ, all dimensionful constants), D5 (fitted optical material constants), D6 (Firmament/Waters/zone architecture content) |
| **# UNTRACEABLE** | 3 (Firmament σ, μ "numerical values"; starlight H_creation magnitude; starlight perpendicular-shortcut numerics) |
| **# PARTIAL** | 4 (starlight comoving-distance numerics, redshift z~10²⁶, geodesic EOM applied, perpendicular-route claim) |

**Source files covered:**
- `04-OPTICS_FROM_MAXWELL.md` (Tests 1–8, Parts I–IV)
- `04-COMPLETIONS.md` (Tests 1–7)
- `04-RESOLVED_STARLIGHT_PROPAGATION.md` (starlight propagation derivation)
- `test_optics.py` (no equations distinct from the .md files — all are the same Snell/TIR/diffraction/double-slit/Sellmeier/Cherenkov/Doppler results already traced below; the test hardcodes σ=6.0e98, μ=6.7e81 kg/m³, disagreeing with the .md file's μ=6.7×10⁸² kg/m² — see UNTRACEABLE-01)

**Audit addendum (2026-06-24 adversarial re-scan):** two displayed equations missed in the first pass are now traced as EQ-OPT-49 (acoustic reflection coefficient, 04-COMPLETIONS.md Test 6 §6.4) and EQ-OPT-50 (Poynting vector, 04-OPTICS_FROM_MAXWELL.md Test 2 energy argument). Several constant tags were corrected from `[DERIVED ratio]` to `[SELECTED scale → D4]` where the quantity is dimensionful (ℏ in EQ-OPT-22; the 12.27 Å combination in EQ-OPT-23; ω₀ in EQ-OPT-25), and S2/S3 rungs that the traces actually use were added to the spine paths of EQ-OPT-17, -19, -21, -28, -30, -33. No honest UNTRACEABLE/PARTIAL flag was weakened.

**Domain-wide trace prerequisites (cited per-entry, not re-derived):**
Maxwell's equations and the EM wave equation enter this domain from the *Electromagnetism*
domain (`03-MAXWELL_DERIVATION.md`) via **S0→S1→S6→S7** + **D1** (6D manifold, KK reduction
to 4D) + **D2** (U(1) gauge sector) + **D6** (Firmament as the membrane carrying the field).
Optics equations stand on top of this wave equation; most add only S6 (PDE/limits), S4
(phase `e^{iθ}`), and boundary-condition algebra. The spine never produces the *value* of c,
σ, μ, ε₀, μ₀, h — those are all dimensionful and trace to **D4** (the unit of "1").

---

## PART A — Foundations (`04-OPTICS_FROM_MAXWELL.md`, Part I)

### EQ-OPT-01 — 6D total action functional
- **Equation:** S_total = S_grav + S_Firm + S_waters + S_gauge + S_matter + S_interaction + S_sustaining
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.1 Step 1)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D1 (6D manifold), D2 (gauge sector), D6 (Firmament/Waters/sustaining content)
- **Trace:** 1=1 → S1 additive structure (sum of action pieces) → S6 gives the integral/action functional (δS=0 borderline) → S9 supplies the Kähler/curved manifold to integrate over; D1 fixes it as 6D, D2 injects S_gauge, D6 injects S_Firm/S_waters/S_sustaining as physical-content terms. This action is *imported* from `ACTION_6D_COMPLETE.md`; here it is the starting point only.
- **Constants:** none displayed; each sub-action carries dimensionful couplings [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-OPT-02 — 6D warped metric ansatz
- **Equation:** ds² = e^{2A(ξ,η)} g_μν dx^μ dx^ν + e^{2B(ξ,η)}(dξ²+dη²) + 2A_μ^ξ dx^μ dξ + 2A_μ^η dx^μ dη
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.1 Step 1)
- **Spine path:** S0→S1→S3→S5→S9
- **Decrees:** D1 (dimension = 6, warp profile), D6 (zone/warp content)
- **Trace:** 1=1 → S3 gives ℝ-valued continua (given D0) → S5 gives independent directions (the extra dims ξ,η) and the metric as inner-product structure → S9 gives the warped/Kähler manifold with curvature. D1 fixes the count at 6 and selects the warp profile A,B; the off-diagonal g_μξ, g_μη are the seeds of the KK gauge field (D2).
- **Constants:** warp factors A(ξ,η), B(ξ,η) are functions, dimensionful via the scale anchor [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D0, D1, D6).

### EQ-OPT-03 — 6D gauge action
- **Equation:** S_gauge^{(6D)} = −(1/4g₆²) ∫ d⁶x √(−g₆) F_MN F^MN
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.1 Step 2)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D1 (6D manifold), D2 (U(1)/gauge group)
- **Trace:** 1=1 → S7 (identity-preserving maps) gives the gauge group and field strength as the curvature of a connection → S6 supplies the action integral → S9 the manifold/measure. D2 selects the gauge group; D1 the 6 dimensions.
- **Constants:** g₆ (6D gauge coupling) dimensionful [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2).

### EQ-OPT-04 — Field strength definition
- **Equation:** F_MN = ∂_M A_N − ∂_N A_M
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.1 Step 2)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2 (gauge field exists), D1 (manifold to differentiate on)
- **Trace:** 1=1 → S7 gives the gauge connection A_M → S6 supplies ∂ → the antisymmetric derivative is the curvature 2-form. D2 makes A a gauge field; D1 gives indices M,N=0..5.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1, D2).

### EQ-OPT-05 — 4D reduced effective action (KK)
- **Equation:** S₄ = ∫ d⁴x √(−g₄) [R₄/(2κ₄²) − (1/4g₄²)F_μν F^μν + L_matter + …]
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.1 Step 3)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D1 (KK reduction 6D→4D), D2 (gauge sector), D6 (membrane content)
- **Trace:** 1=1 → (EQ-OPT-01..04) → integrate over (ξ,η) at zero mode. D1 selects the 6→4 reduction; the surviving F_μν is the 4D EM field. Imported from `KK_DIMENSIONAL_REDUCTION.md`.
- **Constants:** κ₄ (4D gravitational), g₄ (4D gauge coupling) [SELECTED scale → D4]; V_extra appears as g₄²=g₆²/V_extra [DERIVED ratio] given the warp geometry.
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-OPT-06 — Speed-of-light / vacuum constitutive relation
- **Equation:** c² = 1/(ε₀μ₀)  (equivalently ε₀μ₀ = 1/c²)
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.1 Step 3; Level 2/3 of chain diagram)
- **Spine path:** S0→S1→S5→S9
- **Decrees:** D1 (metric signature), D4 (scale anchor sets the magnitude)
- **Trace:** 1=1 → S5/S9 give the metric (inner product + signature) → the Lorentzian signature forces a single invariant speed; ε₀, μ₀ are the unit-dependent split of that one constant. The *value* 3×10⁸ m/s is not forced — it is "1" in chosen units (D4).
- **Constants:** c [SELECTED scale → D4]; ε₀ ≈ 8.854×10⁻¹² F/m [SELECTED scale → D4]; μ₀ ≈ 4π×10⁻⁷ H/m [SELECTED scale → D4]; their product 1/c² [DERIVED ratio] from signature.
- **Status:** DERIVED-as-form for the relation; the numerical values are DERIVED-given-decrees (D4).

### EQ-OPT-07 — Maxwell's equations (4D, from variation)
- **Equation:** ∂_ν F^νμ = j^μ  ⇔  ∇·E=ρ/ε₀, ∇·B=0, ∇×E=−∂_t B, ∇×B=μ₀(J+ε₀∂_t E)
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.1 Step 4); 04-COMPLETIONS.md Test 3 Eq.(7) context
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1 (4D manifold), D2 (U(1) gauge), D6 (Firmament carries the field)
- **Trace:** 1=1 → δS₄/δA_μ=0 (S6 variation, δS=0 borderline) gives the inhomogeneous pair; the Bianchi identity ∂_[λ F_μν]=0 (A_μ single-valued, S7) gives the homogeneous pair. Imported from `03-MAXWELL_DERIVATION.md`. This is the parent equation for ALL optics below.
- **Constants:** ε₀, μ₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6; δS=0 borderline).

### EQ-OPT-08 — EM field tensor components
- **Equation:** F_μν = [[0,−E_x/c,…],[E_x/c,0,−B_z,B_y],…]  (E, B as components of F_μν)
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.1 Step 4)
- **Spine path:** S0→S1→S5→S7
- **Decrees:** D1 (4D indices), D2 (gauge field)
- **Trace:** 1=1 → S5 (matrix/tensor structure) + S7 (gauge field) → the antisymmetric F_μν repackages the 3-vectors E, B. Definitional repackaging of EQ-OPT-04 in 4D.
- **Constants:** c [SELECTED scale → D4] (appears dividing E to make components commensurate).
- **Status:** DERIVED-as-form (given D1, D2).

### EQ-OPT-09 — EM wave equation (vacuum)
- **Equation:** ∇²E − (1/c²)∂²_t E = 0  and  ∇²B − (1/c²)∂²_t B = 0
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.1 Step 5); 04-COMPLETIONS.md Eq.(1)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D2, D6
- **Trace:** 1=1 → take ∇× of Faraday's law in EQ-OPT-07, use ∇×(∇×E)=∇(∇·E)−∇²E with ρ=0 (S6 vector calculus on the manifold). The d'Alembertian □ is the S6 operator. This single equation generates all eight optical phenomena.
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-OPT-10 — Membrane wave equation (Firmament form)
- **Equation:** ∂²ψ/∂t² = c² ∇²ψ
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.2; §3.1); 04-COMPLETIONS.md Eq.(14)
- **Spine path:** S0→S1→S6
- **Decrees:** D6 (Firmament membrane as physical substrate), D4 (c scale)
- **Trace:** 1=1 → S6 supplies the second-order hyperbolic PDE; D6 identifies ψ as the transverse displacement of the Firmament membrane. Same equation as EQ-OPT-09 in scalar form — the "single governing equation."
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6, D4).

### EQ-OPT-11 — Membrane force balance → wave speed
- **Equation:** μ ∂²ψ/∂t² dA = σ ∇²ψ dA  ⇒  ∂²ψ/∂t² = (σ/μ)∇²ψ  ⇒  c² = σ/μ
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.2)
- **Spine path:** S0→S1→S6
- **Decrees:** D6 (membrane with tension σ, density μ), D4 (σ, μ scales)
- **Trace:** 1=1 → S1 conservation (Newton's 2nd law as inertial = restoring, the a+(−a) balance) → S6 the curvature operator ∇² → identify c²=σ/μ by matching to EQ-OPT-10. D6 supplies the membrane; D4 sets the magnitudes of σ, μ.
- **Constants:** σ [SELECTED scale → D4]; μ [SELECTED scale → D4]; c²=σ/μ [DERIVED ratio] *as a relation*, but the specific σ, μ values are not forced (see UNTRACEABLE-01).
- **Status:** DERIVED-as-form for the relation c²=σ/μ; the numerical σ=6.0×10⁹⁸, μ=6.7×10⁸² (file disagrees with test's 6.7×10⁸¹) are UNTRACEABLE.

### EQ-OPT-12 — Plane-wave dispersion (vacuum, massless)
- **Equation:** E(x,t)=E₀ e^{i(k·x−ωt)};  ω = c|k|;  k = ω/c;  λ = 2π/k = c/f
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.1 Level 4, §1.3); 04-COMPLETIONS.md §1.2
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D4 (c scale)
- **Trace:** 1=1 → S4 gives the complex phase e^{iθ} and the circle → S6 says plane waves diagonalize the wave operator EQ-OPT-09 → substituting yields the linear, non-dispersive relation ω=c|k|. Phase velocity v_p=ω/k=fλ is then S2 (ratio).
- **Constants:** c [SELECTED scale → D4]; the relations λ=2π/k, f=ω/2π are pure S2/S4 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-OPT-13 — Refractive index / phase-velocity ratio
- **Equation:** n = c_vacuum/c_material;  v_p = c/n;  λ_material = λ_vacuum/n;  k_material = n k_vacuum
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Part I §1.3)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4 (c scale); D6 (medium = material response of the membrane)
- **Trace:** 1=1 → S2 gives the ratio (proportion / Logos) defining n as a dimensionless speed ratio → applied to EQ-OPT-12. n itself is set by material response (EQ-OPT-26/27).
- **Constants:** n [DERIVED ratio] (dimensionless speed ratio), but its numerical value per material is material data [FIT → D5].
- **Status:** DERIVED-as-form (given D4).

---

## PART B — Eight Optical Phenomena (`04-OPTICS_FROM_MAXWELL.md`, Part II)

### EQ-OPT-14 — Snell's law (refraction)
- **Equation:** n₁ sin θ₁ = n₂ sin θ₂
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 1); 04-COMPLETIONS.md Eq.(7); test_optics.py Test 1
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D4 (c), D6 (two media / interface)
- **Trace:** 1=1 → wave equation EQ-OPT-09 in each medium → S4 phase continuity at the interface forces tangential k continuity: k₁ sin θ₁ = k₂ sin θ₂ → substitute k_j=n_j ω/c, cancel ω/c. Only boundary-condition algebra is added.
- **Constants:** n₁, n₂ [FIT → D5] (material indices); angles dimensionless [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-15 — Critical angle (total internal reflection)
- **Equation:** θ_c = arcsin(n₂/n₁)
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 2); test_optics.py Test 2
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → Snell's law EQ-OPT-14 with θ_ref=90° (sin=1) → solve for incident angle. Pure trigonometric inversion.
- **Constants:** n₁, n₂ [FIT → D5]; θ_c dimensionless [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-16 — Evanescent decay constant / penetration depth
- **Equation:** κ = (n₂ω/c)√((n₁/n₂)²sin²θ − 1);  d_pen = 1/κ
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 2)
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → for θ>θ_c, Snell gives sin θ_ref>1 → cos θ_ref becomes imaginary (S4 analytic continuation into ℂ) → the wave EQ-OPT-12 becomes e^{−κz}, real exponential decay. ℂ from S4 is the load-bearing step.
- **Constants:** c [SELECTED scale → D4]; n₁,n₂ [FIT → D5]; ω, θ inputs.
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-17 — Single-slit diffraction intensity
- **Equation:** I(θ) = I₀ [sin β / β]²,  β = πa sin θ/λ
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 3); test_optics.py Test 3
- **Spine path:** S0→S1→S2→S4→S6
- **Decrees:** D4 (λ scale), D6 (aperture/membrane)
- **Trace:** 1=1 → Huygens-Fresnel superposition (S6 integral of S4 phases over the slit) → ∫_{−a/2}^{a/2} e^{iky sinθ}dy = (2/k sinθ)sin(ka sinθ/2) → square the amplitude (S2 product with conjugate). The sinc² is pure S2+S4+S6 algebra (S2 added to path for the modulus-squared).
- **Constants:** I₀ amplitude [SELECTED scale → D4]; a, λ inputs; β dimensionless [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-18 — Single-slit minima
- **Equation:** sin θ_n = nλ/a,  n=±1,±2,…
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 3); test_optics.py Test 3
- **Spine path:** S0→S1→S4→S6→S8
- **Decrees:** D4, D6
- **Trace:** 1=1 → set sin β=0 in EQ-OPT-17 → β=nπ (the integer n is an S8 winding/zero-count, not a chosen decree value — it enumerates zeros of sine). Solve for θ.
- **Constants:** λ, a inputs; n [count] (intrinsic integer from sine zeros, NOT D3 — it is a generic enumeration, not n_w).
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-19 — Photon double-slit Born-rule probability
- **Equation:** P(x) = |ψ₁+ψ₂|² = |ψ₁|²+|ψ₂|²+2Re[ψ₁*ψ₂]
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 4); 04-COMPLETIONS.md Test 1; test_optics.py Test 4
- **Spine path:** S0→S1→S2→S4→S5
- **Decrees:** D6 (membrane displacement = ψ)
- **Trace:** 1=1 → S5 Hilbert-space superposition ψ=ψ₁+ψ₂ → S4 complex amplitudes → Born rule = squared modulus (S2 product with conjugate). The interference cross-term is the 2Re part. (S2 added to path because the squared modulus is a ring product; D4 dropped because the probability form carries no dimensionful constant.)
- **Constants:** none dimensionful in the probability form.
- **Status:** DERIVED-as-form (given D6).

### EQ-OPT-20 — Double-slit fringe pattern and spacing
- **Equation:** P(x)=2|A₀|²{1+cos Δφ}, Δφ=k(r₂−r₁); bright x_m=mλL/d; Δx=λL/d
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 4); 04-COMPLETIONS.md Eq.(2,3,4); test_optics.py Test 4
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D4 (λ scale), D6
- **Trace:** 1=1 → EQ-OPT-19 with equal slits → cos Δφ (S4) → small-angle path difference r₂−r₁≈d x/L (S6 geometry) → constructive at Δφ=2πm. Fringe spacing is the S2 difference x_{m+1}−x_m.
- **Constants:** λ, L, d inputs [SELECTED scale → D4 for the length unit]; integer m [count] (generic).
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-21 — Intensity form 4A²cos²(πyd/Lλ)
- **Equation:** I(y) = 4A² cos²(πyd/Lλ)
- **Source:** 04-COMPLETIONS.md (Test 1 Eq.(3) context, Eq. boxed); domain summary
- **Spine path:** S0→S1→S2→S4→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → EQ-OPT-20: ψ=2A cos(Δφ/2) e^{i(kL−ωt)} (sum of two S4 phases) → I=|ψ|² (S2 modulus-squared, now in path) gives 4A²cos²(Δφ/2). Same physics as EQ-OPT-20, intensity form.
- **Constants:** A [SELECTED scale → D4]; y,d,L,λ inputs.
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-22 — de Broglie wavelength
- **Equation:** λ_dB = h/p = h/(m_e v) = h/√(2m E_kin)
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 5); 04-COMPLETIONS.md Eq.(5); test_optics.py Test 5
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D4 (h, m_e scales), D6 (matter = membrane oscillation)
- **Trace:** 1=1 → Planck-Einstein E=ℏω, p=ℏk (S4 phase ↔ energy/momentum identification) → k=p/ℏ with k=2π/λ → λ=2πℏ/p=h/p. The relations p=ℏk are imported quantum postulates (cross-domain to QM); within optics they are taken as given.
- **Constants:** h=6.626×10⁻³⁴ J·s [SELECTED scale → D4]; ℏ=h/2π [SELECTED scale → D4] (dimensionful action; the 1/2π factor alone is [DERIVED ratio], but ℏ itself inherits h's D4 scale); m_e [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-23 — Electron accelerating-voltage wavelength
- **Equation:** λ_dB(V) = h/√(2m_e eV) = 12.27 Å/√V
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 5)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4 (h, m_e, e scales)
- **Trace:** 1=1 → eV = ½m_e v² (energy conservation, S1) → p=√(2m_e eV) → substitute into EQ-OPT-22. The constant 12.27 Å = h/√(2m_e e) is a pure combination of dimensionful constants.
- **Constants:** h, m_e, e [SELECTED scale → D4]; the numeric 12.27×10⁻¹⁰ m·V^{1/2} [SELECTED scale → D4] (a *dimensionful* combination h/√(2m_e e), so it inherits the D4 anchors — not a pure [DERIVED ratio]).
- **Status:** DERIVED-given-decrees (D4).

### EQ-OPT-24 — Electron fringe spacing
- **Equation:** Δx = λ_dB L/d = hL/(d√(2mE))
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 5); 04-COMPLETIONS.md Eq.(6)
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → identical interference geometry as EQ-OPT-20 with λ→λ_dB (EQ-OPT-22).
- **Constants:** h, m [SELECTED scale → D4]; L, d, E inputs.
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-25 — Driven-oscillator equation of motion
- **Equation:** m_e ẍ + Γ ẋ + k x = −e E₀ cos(ωt)
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 6)
- **Spine path:** S0→S1→S6
- **Decrees:** D4 (m_e, e, k scales), D6 (medium oscillators)
- **Trace:** 1=1 → S1 (Newton balance: inertia + damping + restoring = drive) → S6 second-order ODE. D6 supplies the bound-electron model.
- **Constants:** m_e, e [SELECTED scale → D4]; Γ damping, k spring const [SELECTED scale → D4]; ω₀=√(k/m_e) [SELECTED scale → D4] (dimensionful resonance frequency [1/time] built from two D4 anchors — not a dimensionless [DERIVED ratio]).
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-26 — Refractive index from oscillator response
- **Equation:** n² = 1 + Σ_i N_i e²/[m_e ε₀(ω₀ᵢ²−ω²)]  (and n ≈ 1 + Ne²/[2m_e ε₀(ω₀²−ω²)])
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 6)
- **Spine path:** S0→S1→S6
- **Decrees:** D4 (e, m_e, ε₀, N scales), D6 (polarizable medium)
- **Trace:** 1=1 → steady-state solution of EQ-OPT-25 → dipole p=−ex → polarization P=Np → D=ε₀E+P → ε_r=1+Ne²/[m_e ε₀(ω₀²−ω²)] → n=√ε_r. Sum over resonances i (S1 additive).
- **Constants:** N (number density), e, m_e, ε₀ [SELECTED scale → D4]; resonance ω₀ᵢ material data [FIT → D5].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-27 — Sellmeier equation
- **Equation:** n²(λ) = 1 + Σ_i B_i λ²/(λ² − C_i),  C_i = λ₀ᵢ²
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 6); test_optics.py Test 6
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D5 (material coefficients), D6
- **Trace:** 1=1 → convert EQ-OPT-26 from ω to λ via ω=2πc/λ (S2 ratio) → algebra gives the λ²/(λ²−C_i) form. The coefficients B_i, C_i are matched to data.
- **Constants:** B_i ∝ oscillator strength [FIT → D5]; C_i = λ₀ᵢ² [FIT → D5]; specific crown-glass values (1.03961212, 0.231792344, 1.01046945, …) [FIT → D5].
- **Status:** DERIVED-as-form for the form; coefficient values are FIT (D5).

### EQ-OPT-28 — Cherenkov angle
- **Equation:** cos θ_C = 1/(nβ) = c/(nv),  β=v/c;  sin θ_C = (c/n)t/(vt)
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 7); test_optics.py Test 7
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D4 (c scale), D6 (medium with index n)
- **Trace:** 1=1 → wavefront (Mach-cone) geometry: particle covers vt, light covers (c/n)t in same time → S2 ratio gives sin θ_C=(c/n)/v → cos via Pythagoras (S3, now in path). Threshold nβ>1 from sin≤1.
- **Constants:** c [SELECTED scale → D4]; n [FIT → D5]; β input.
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-29 — Cherenkov energy-loss (heuristic)
- **Equation:** dE/dx ≈ (e²/c)(1 − 1/(nβ)) = (e²/c)(1 − cos θ_C)
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 7)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → energy carried by the shock front ∝ (1−cos θ_C) (S1 conservation) × Coulomb-scale prefactor e²/c. Stated as approximate ("≈") in source — heuristic, not full Frank-Tamm.
- **Constants:** e, c [SELECTED scale → D4].
- **Status:** PARTIAL (heuristic prefactor, not the rigorous Frank-Tamm spectral form).

### EQ-OPT-30 — Relativistic Doppler effect
- **Equation:** f_obs = f_source √((1±β)/(1∓β)) = f_source γ(1±β);  λ_obs = λ_source √((1∓β)/(1±β))
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 8); test_optics.py Test 8
- **Spine path:** S0→S1→S3→S4→S9
- **Decrees:** D1 (Lorentzian metric), D4 (c)
- **Trace:** 1=1 → phase invariant k'x'−ω't'=kx−ωt (S4) → Lorentz boost of (ω,k) from S9 Lorentzian structure → ω_obs=γω_source(1±β); with ω=ck (massless) → the √ ratio. γ=1/√(1−β²) is pure S3/S9 (S3 now in path for the √ / completed-ℝ step).
- **Constants:** c [SELECTED scale → D4]; β, γ dimensionless [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1, D4).

---

## PART C — Optics Completions (`04-COMPLETIONS.md`, Tests 3–7)

### EQ-OPT-31 — EM boundary conditions at dielectric interface
- **Equation:** E₁^∥ = E₂^∥ (tangential E continuous);  ε₁E₁^⊥ = ε₂E₂^⊥ (normal D continuous)
- **Source:** 04-COMPLETIONS.md (Test 3 §3.1)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2 (EM field), D4 (ε scales), D6 (interface)
- **Trace:** 1=1 → Maxwell EQ-OPT-07 integrated across a pillbox/loop at the interface (S6 Stokes/Gauss) → continuity of tangential E and normal D. Standard boundary algebra.
- **Constants:** ε₁, ε₂ [SELECTED scale → D4]; n_j=√(ε_j μ_j) [DERIVED ratio].
- **Status:** DERIVED-as-form (given D2, D4, D6).

### EQ-OPT-32 — Fresnel p-reflection amplitude & Brewster condition
- **Equation:** r_p ∝ (n₂cos θ_i − n₁cos θ_t)/(n₂cos θ_i + n₁cos θ_t);  vanishes when n₂cos θ_i = n₁cos θ_t
- **Source:** 04-COMPLETIONS.md (Test 3 §3.2, Eq.(8))
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4, D6
- **Trace:** 1=1 → impose EQ-OPT-31 on incident+reflected+transmitted plane waves (S4 phases) → solve the linear system for the reflected amplitude (S5 linear algebra). Numerator zero is the Brewster condition.
- **Constants:** n₁, n₂ [FIT → D5]; angles [DERIVED ratio].
- **Status:** DERIVED-as-form (given D2, D4, D6).

### EQ-OPT-33 — Brewster's angle
- **Equation:** tan θ_B = n₂/n₁;  with θ_B + θ_t = 90°
- **Source:** 04-COMPLETIONS.md (Test 3 Eq.(9))
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → combine Brewster numerator-zero (EQ-OPT-32) with Snell (EQ-OPT-14) → trig identity (S2 ratio + S3 Pythagoras, now in path) → tan θ_B=n₂/n₁.
- **Constants:** n₁, n₂ [FIT → D5]; θ_B [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-34 — Paraxial single-surface focal length
- **Equation:** n₁θ₁ ≈ n₂θ₂; Δθ=(n₁−n₂)θ₁/n₂; f₁ = n₂R/(n₂−n₁)
- **Source:** 04-COMPLETIONS.md (Test 4 §4.1–4.2, Eq.(10,11))
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → small-angle limit of Snell EQ-OPT-14 (sin θ≈θ, S6 Taylor) → geometry of a ray at height h hitting curvature R → f₁=n₂R/(n₂−n₁).
- **Constants:** n₁, n₂ [FIT → D5]; R input length [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-35 — Lensmaker's equation
- **Equation:** 1/f = (n−1)(1/R₁ − 1/R₂)
- **Source:** 04-COMPLETIONS.md (Test 4 Eq.(12))
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → add reciprocal focal powers of two surfaces (EQ-OPT-34) in the thin-lens limit (S1 additive, S2 reciprocals).
- **Constants:** n=n_lens/n_surround [DERIVED ratio / FIT → D5]; R₁,R₂ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-36 — Thin-lens imaging equation & magnification
- **Equation:** 1/f = 1/s_o + 1/s_i;  m = −s_i/s_o
- **Source:** 04-COMPLETIONS.md (Test 4 Eq.(13))
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → paraxial ray geometry (similar triangles, S2 ratios) for object/image conjugates. Pure geometric optics.
- **Constants:** f, s_o, s_i lengths [SELECTED scale → D4]; m [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-37 — Standing-wave quantization
- **Equation:** kL = nπ ⇒ k_n = nπ/L;  ω_n = nπv/L;  f_n = nv/(2L);  E_n = ℏω_n = nπℏv/L
- **Source:** 04-COMPLETIONS.md (Test 5 Eq.(14,15,16))
- **Spine path:** S0→S1→S5→S6→S8
- **Decrees:** D4 (v, ℏ scales), D6 (bounded membrane)
- **Trace:** 1=1 → wave EQ-OPT-10 with fixed-end BCs → separation of variables (S6) → X(x)=A sin kx, sin(kL)=0 → kL=nπ (S8 integer mode count from boundary). ω_n=vk_n; E_n=ℏω_n uses the S4/QM Planck relation.
- **Constants:** v, ℏ [SELECTED scale → D4]; L input length; mode integer n [count] (generic boundary count, not D3).
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-38 — Acoustic (sound) wave equation
- **Equation:** ρ₀ ∂²u/∂t² = −∇p; ∂ρ/∂t + ∇·(ρ₀u)=0; p=c_s²ρ'; ⇒ ∇²p − (1/c_s²)∂²_t p = 0
- **Source:** 04-COMPLETIONS.md (Test 6 Eq.(17,18,19))
- **Spine path:** S0→S1→S6
- **Decrees:** D4 (ρ₀, c_s scales), D6 (continuum medium)
- **Trace:** 1=1 → Newton's 2nd law (S1) + mass continuity (S1 conservation) + adiabatic state p=c_s²ρ' → combine via S6 (time/space derivatives) → wave equation for p. Same hyperbolic form as EQ-OPT-10.
- **Constants:** ρ₀, c_s [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-39 — Speed of sound
- **Equation:** c_s = √(B/ρ₀);  c_s = √(γ k_B T/m)  (ideal gas, B=γp₀);  Z = ρ₀c_s
- **Source:** 04-COMPLETIONS.md (Test 6 Eq.(20))
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4 (B, ρ₀, k_B scales), D6 (medium)
- **Trace:** 1=1 → identify c_s²=B/ρ₀ from EQ-OPT-38 (S2 ratio); for ideal gas B=γp₀ and p₀=ρ₀k_B T/m → c_s=√(γk_B T/m). Acoustic impedance Z=ρ₀c_s is a product (S2).
- **Constants:** B bulk modulus, ρ₀, k_B [SELECTED scale → D4]; γ=C_p/C_v [DERIVED ratio]; m molecular mass [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-40 — Eikonal equation (geometric optics)
- **Equation:** |∇S|² = n²k₀²,  k₀=ω/c;  ψ=A e^{iS/ℏ}
- **Source:** 04-COMPLETIONS.md (Test 7 §7.1, Eq.(21))
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D4 (c scale), D6 (index field n(r))
- **Trace:** 1=1 → high-frequency (ℏ→0 / short-λ) limit of the wave EQ-OPT-09 with ψ=A e^{iS/ℏ} (S4 phase) → leading order gives the eikonal |∇S|²=n²k₀² (S6 asymptotics).
- **Constants:** c [SELECTED scale → D4]; n(r) [FIT → D5]; k₀ input.
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-41 — Ray (Fermat) equation & ray-parameter conservation
- **Equation:** d/ds(n dr/ds) = ∇n;  n(z)sin θ(z) = n₀ sin θ₀ = const
- **Source:** 04-COMPLETIONS.md (Test 7 §7.2, §7.4, Eq.(22,23))
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D4, D6
- **Trace:** 1=1 → ray = gradient trajectory of S from EQ-OPT-40 (S6) → Fermat stationary optical path ∫n ds (δS=0 borderline, S6) → in a stratified medium n(z), translational symmetry in x (S7 Noether) conserves the transverse ray parameter n sin θ.
- **Constants:** n(z) [FIT → D5]; angles [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4, D6; δS=0 borderline).

---

## PART D — Starlight Propagation (`04-RESOLVED_STARLIGHT_PROPAGATION.md`)

### EQ-OPT-42 — Creation-epoch 6D metric
- **Equation:** ds² = −c₀²dt² + a²(t)[dx²+dy²+dz²] + b²(t)dξ² + c²(t)dη²
- **Source:** 04-RESOLVED_STARLIGHT_PROPAGATION.md (§3.1, §6 Book 0 §3.1)
- **Spine path:** S0→S1→S3→S5→S9
- **Decrees:** D0 (ℝ continua), D1 (6D dimension), D6 (Waters Above/Below directions ξ,η; creation/sustaining epochs)
- **Trace:** 1=1 → S5 independent directions (3 Firmament + 2 perpendicular + time) → S9 Lorentzian/curved manifold with time-dependent scale factors → D1 fixes 6 dims; D6 identifies ξ→Waters Above, η→Waters Below and the epoch structure.
- **Constants:** c₀ [SELECTED scale → D4]; scale factors a,b,c functions [SELECTED scale → D4]; their exponential rates H below.
- **Status:** DERIVED-as-form (given D0, D1, D6).

### EQ-OPT-43 — Null geodesic condition (6D light propagation)
- **Equation:** g_μν (dx^μ/dλ)(dx^ν/dλ) = 0  ⇒  c₀²(dt/dλ)² = a²(dr/dλ)² + b²(dξ/dλ)² + c²(dη/dλ)²
- **Source:** 04-RESOLVED_STARLIGHT_PROPAGATION.md (§3.2, §6 Book 0 §3.2)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D6
- **Trace:** 1=1 → ds²=0 for light on the EQ-OPT-42 metric (S9 + S6 affine parameter λ). This is the unified equation the document hangs the whole "distant starlight" resolution on. The null condition itself is standard.
- **Constants:** c₀ [SELECTED scale → D4]; scale factors [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-OPT-44 — Comoving distance / Friedmann light path
- **Equation:** dr = c dt/a(t);  r = ∫ c dt/a(t) = (c/H_c)[1 − exp(−H_c Δt)]  (exponential a)
- **Source:** 04-RESOLVED_STARLIGHT_PROPAGATION.md (§3.3, §3.6 misc, §4.1, §6 Book 0 §3.3)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1 (FRW manifold), D6 (creation-epoch expansion content)
- **Trace:** 1=1 → pure-Firmament limit (dξ=dη=0) of EQ-OPT-43 → c₀ dt = a dr → integrate with a(t)=a₀exp(H_c t) (S6). Standard FRW result.
- **Constants:** c [SELECTED scale → D4]; H_c expansion rate [SELECTED scale → D4]; the magnitude H_creation is asserted/constrained, not derived — see PARTIAL below.
- **Status:** PARTIAL — the equation is DERIVED-as-form, but the document's own numerics (lines 144–188, 296–360) repeatedly fail to reach cosmological distances and conclude H_creation is "constrained by the theological requirement," not computed. The required H_creation magnitude is UNTRACEABLE.

### EQ-OPT-45 — Coordinate-time dilation relation (Mechanism B)
- **Equation:** dt ≈ (a(t)/c₀) dℓ;  Δt ≈ (a₀ dℓ/c₀ H_c) exp(H_c t)
- **Source:** 04-RESOLVED_STARLIGHT_PROPAGATION.md (§3.4)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D6
- **Trace:** 1=1 → rearrange EQ-OPT-43 in the Firmament-dominant limit → dt∝a(t)dℓ → integrate exponential a (S6). Interpretation of the same null condition.
- **Constants:** c₀, a₀, H_c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D6) for the relation; physical magnitude inherits EQ-OPT-44's PARTIAL status.

### EQ-OPT-46 — Cosmological redshift / photon energy decay
- **Equation:** E_comoving(t) = E₀ exp(−H_c t);  E_comoving = E_lab/a(t);  z ~ 10²⁶
- **Source:** 04-RESOLVED_STARLIGHT_PROPAGATION.md (§3.6 Book 0 Energy-Momentum)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → photon four-momentum on EQ-OPT-42 metric → E∝1/a(t) (S9 + S6) → for exponential a, exponential redshift. The relation E∝1/a is standard FRW.
- **Constants:** E₀ [SELECTED scale → D4]; H_c [SELECTED scale → D4]; the quoted z~10²⁶ depends on the unconstrained H_creation.
- **Status:** PARTIAL — relation DERIVED-as-form (given D1, D6); the numerical z~10²⁶ is not independently derivable (inherits H_creation indeterminacy).

### EQ-OPT-47 — Perpendicular-shortcut (Mechanism A) effective shortening
- **Equation:** c₀(dt/dλ)=√2 a(dr/dλ) when a(dr)=b(dξ); shortening when (b/a)² ≪ 1
- **Source:** 04-RESOLVED_STARLIGHT_PROPAGATION.md (§3.3, §3.4, §6 Book 0 §3.4 Route 2)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D6
- **Trace:** 1=1 → allocate the null condition EQ-OPT-43 between radial and perpendicular components → if b≪a, perpendicular travel "costs less" coordinate time. The algebra is consistent, but the *claim* that a real photon takes this route, and that it yields the needed shortening, is asserted, not solved from the geodesic EOM.
- **Constants:** scale factors a,b [SELECTED scale → D4]; (b/a)² [DERIVED ratio] but unquantified.
- **Status:** PARTIAL — the inequality is a self-consistent observation; the physical conclusion ("light reaches Earth in days") is not derived (no completed geodesic integration; the document acknowledges this).

### EQ-OPT-48 — Geodesic equations of motion
- **Equation:** d²x^μ/dλ² + Γ^μ_αβ (dx^α/dλ)(dx^β/dλ) = 0
- **Source:** 04-RESOLVED_STARLIGHT_PROPAGATION.md (§6 Book 0 §3.5)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D6
- **Trace:** 1=1 → S9 curved manifold + S6 (δS=0 borderline, geodesic = extremal path) gives the geodesic equation with Christoffel symbols Γ from the EQ-OPT-42 metric. Standard GR; written but not solved in the document.
- **Constants:** none new; Γ built from a,b,c,c₀ [SELECTED scale → D4].
- **Status:** PARTIAL — DERIVED-as-form (given D1, D6; δS=0 borderline) but only stated, not integrated for the starlight problem.

---

## PART E — Equations recovered in the missed-equation re-scan (audit addendum)

### EQ-OPT-49 — Acoustic reflection coefficient (impedance mismatch)
- **Equation:** r = (Z₂ − Z₁)/(Z₂ + Z₁),  Z_j = ρ₀ⱼ c_{s,j}
- **Source:** 04-COMPLETIONS.md (Test 6 §6.4, displayed after Eq.(20))
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4 (ρ₀, c_s scales), D6 (two acoustic media / interface)
- **Trace:** 1=1 → impose continuity of pressure and normal particle velocity at the interface on the plane-wave solutions of the acoustic wave EQ-OPT-38 (S6 boundary algebra) → solve the linear 1D system for the reflected over incident pressure amplitude (S2 ratio) → r=(Z₂−Z₁)/(Z₂+Z₁). Same impedance-matching structure as the Fresnel amplitudes (EQ-OPT-32), acoustic version. (Missed in the original pass; it is a displayed result, not boxed.)
- **Constants:** Z₁, Z₂ = ρ₀c_s [SELECTED scale → D4]; r [DERIVED ratio] (dimensionless impedance ratio).
- **Status:** DERIVED-as-form (given D4, D6).

### EQ-OPT-50 — Poynting vector (energy-flux definition used in the TIR energy argument)
- **Equation:** S = (1/μ₀) E × B
- **Source:** 04-OPTICS_FROM_MAXWELL.md (Test 2, "Energy Argument," displayed at line 525)
- **Spine path:** S0→S1→S5→S7
- **Decrees:** D2 (EM field content), D4 (μ₀ scale), D6 (Firmament carries the field)
- **Trace:** 1=1 → S7 gives the gauge field strength (E, B as components of F_μν, cf. EQ-OPT-08) → S5 supplies the cross product / antisymmetric bilinear on the 3-space → the conserved EM energy-flux current (Noether/stress-tensor T^{0i}, S7) is S=(1/μ₀)E×B. Used in the document only to argue the evanescent wave (EQ-OPT-16) carries zero net normal energy at total internal reflection. (Missed in the original pass; a displayed definitional equation invoked for the TIR energy balance.)
- **Constants:** μ₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D2, D4, D6).

---

## UNTRACEABLE items (coverage audit)

### UNTRACEABLE-01 — Firmament tension and density numerical values
- **Equation/quantity:** σ = 6.0×10⁹⁸ kg/(m·s²),  μ = 6.7×10⁸² kg/m² (file) / 6.7×10⁸¹ kg/m³ (test_optics.py)
- **Reason:** The relation c²=σ/μ (EQ-OPT-11) is grammar, but the *individual* values of σ and μ are stated to come "from zone architecture and the fine structure constant" with no shown derivation. They are reverse-engineered so that √(σ/μ)=c. Only their ratio is constrained (= c², which is itself D4). The file and the test suite even disagree on μ's exponent (10⁸² vs 10⁸¹) and units (kg/m² vs kg/m³), so the numbers are not on any reproducible chain. Not on the spine; not a clean D4 scale anchor (two free numbers with one constraint). UNTRACEABLE.

### UNTRACEABLE-02 — Creation-epoch Hubble magnitude H_creation
- **Equation/quantity:** H_creation ≈ 2–7×10⁻⁴ s⁻¹; H_creation/H₀ ≈ 3×10¹⁴
- **Reason:** The document repeatedly attempts to compute the distance light travels and each time falls short of cosmological scales (lines 144–188, 296–360, 646–651), then explicitly states (line 354) "The proper time for light to reach Earth is not calculated from first principles—it's constrained by the theological requirement of functional integrity." The magnitude is a back-solved constraint, not a derivation from `1=1` + decrees. Not traceable.

### UNTRACEABLE-03 — Perpendicular-shortcut realization (Mechanism A physical claim)
- **Equation/quantity:** the claim that photons actually traverse ξ,η to shorten travel and that this resolves distant starlight
- **Reason:** EQ-OPT-47 shows the null condition *permits* perpendicular components, but the geodesic EOM (EQ-OPT-48) is never solved to demonstrate that real light paths take this route or that the shortening suffices. The document concedes "the calculation requires iteration" and does not complete it. The physical resolution rests on assertion, so the quantitative claim is UNTRACEABLE (the *form* of the equations, EQ-OPT-42..48, is traced; the *conclusion* is not).

---

## Notes on coverage

- **test_optics.py** contains the same equations as the .md files (Snell, TIR, single-slit,
  double-slit photon/electron, Sellmeier, Cherenkov, Doppler) plus the membrane constants. No
  equation in the test file is distinct from those already traced (EQ-OPT-11, 14–18, 19–24,
  27, 28, 30). Its σ/μ constants are flagged under UNTRACEABLE-01 (and it disagrees with the
  .md file on μ).
- **Recurring decree pattern:** essentially every optics equation rides on the EM wave equation
  (EQ-OPT-09/10), which carries D1+D2+D6; optics then adds only S4 (phase), S6 (PDE/limits/
  boundary algebra), and S2/S3 (ratios, Pythagoras). The dimensionful constants (c, h, ε₀, σ, μ,
  scale factors) are uniformly D4. Material indices and Sellmeier/Fresnel coefficients are D5.
- **δS=0 borderline** flagged on EQ-OPT-01, -07, -41, -48 per SPINE.md S6 note.
- **Integer counts** in diffraction/interference/standing-wave orders (n, m) are generic
  enumerations of zeros/periods, NOT the topological n_w=3 (D3); tagged [count] not [count → D3].
