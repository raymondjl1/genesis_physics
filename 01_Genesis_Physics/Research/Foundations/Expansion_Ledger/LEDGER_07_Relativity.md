# Expansion Ledger — Domain 07: Relativity

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This ledger traces every distinct displayed/numbered equation and named key result in
> `Research/Mathematical_Models/07_Relativity/` back to the seed `1=1` via the spine rungs
> S0–S9 (`SPINE.md`) plus the named decrees D0–D6 (`DECREE_REGISTER.md`). No equation is
> "derived from `1=1` alone": every physics result = spine path + named decrees + algebra.
> Constants are tagged `[DERIVED ratio]` / `[SELECTED scale → D4]` / `[FIT → D5]` / `[count → D3]`.

## Header

| Field | Value |
|-------|-------|
| Domain | 07 — Relativity (Special + General Relativity, GW, black holes, FTL, Z₁ field eqs) |
| Files traced | `07-SPECIAL_RELATIVITY_DERIVATION.md`, `07-RESOLVED_GRAVITY_MECHANISM.md`, `07-GR_OBSERVABLES.md`, `07-GR_PRECISION_OBSERVABLES.md`, `07-GW_ADVANCED_GR.md`, `07-COMPLETIONS.md`, `07-COMPLETIONS_R4.md`, `07-BH_MERGERS_DYNAMICS.md`, `07-FTL_MECHANISMS_FORMAL.md`, `07-FTL_MECHANISMS_SUMMARY.md`, `op10_z1_field_equations.md`, `test_gr_observables.py` |
| # equation blocks | 56 |
| Decrees used across domain | D0 (ℝ continua), D1 (manifold/dimension = 6→4), D4 (dimensionful scale anchor), D5 (fitted data values), D6 (zone/Firmament/Waters/membrane content) |
| # UNTRACEABLE | 6 |
| # PARTIAL | 12 (EQ-REL-35, -36, -39, -40, -44, -45, -48, -49, -50, -52, -54, -56; plus EQ-REL-27's validated-number caveat) |

**Recurring deduplication note.** Several formulas appear in many files with identical content:
the Schwarzschild metric/radius, Kerr metric, Einstein field equations, Lorentz factor,
quadrupole power, chirp mass, frequency-evolution (chirp), Lense-Thirring Ω_LT, and the
GW150914 chirp-mass check. Each is traced **once** at its primary locator; duplicate locators
are listed inside that block. The `.py` file re-encodes the same SR/GR formulas numerically and
is cited only where it adds a formula not in the `.md` files (none new — all map to existing blocks).

**Cross-domain note.** Every GR file in this folder bottoms out on the *6D action* and its
*KK reduction* (`ACTION_6D_COMPLETE.md`, `KK_DIMENSIONAL_REDUCTION.md`), and on `G_4 = G_6/V_extra`
(`10-GRAVITATIONAL_CONSTANT_DERIVATION.md`). Those parent derivations live in Foundations /
Domain 10 and are cited by name, not re-derived here. The relativity ledger picks up at the
4D Einstein equations and their solutions/observables.

---

### EQ-REL-01 — 6D background line element (Minkowski 6D)
- **Equation:** ds² = −c²dt² + dx² + dy² + dz² + dξ² + dη²
- **Source:** 07-SPECIAL_RELATIVITY_DERIVATION.md §1.1 (also 07-RESOLVED_GRAVITY_MECHANISM.md §3.2; 07-GR_PRECISION §2.1)
- **Spine path:** S0→S1→S3→S5→S9
- **Decrees:** D0 (real continua), D1 (6 dimensions), D6 (the ξ,η = Waters/Firmament directions)
- **Trace:** 1=1 → S1/S3 build ℝ → S5 supplies independent directions and an inner product → S9 supplies a (pseudo-)Riemannian metric. D1 fixes the count of directions to **six**; D6 names two of them (ξ,η) as the Waters-Above / Waters-Below perpendicular directions and one as time. The flat diagonal form is the unperturbed (vacuum) metric.
- **Constants:** c [SELECTED scale → D4] (set by σ/μ, see EQ-REL-44); signature (−,+,+,+,+,+) is a structural choice under D1/D6, not a number.
- **Status:** DERIVED-given-decrees (D0,D1,D6).

### EQ-REL-02 — 4D Minkowski metric from dimensional reduction
- **Equation:** ds²|_membrane = −c²dt² + dx² + dy² + dz²
- **Source:** 07-SPECIAL_RELATIVITY_DERIVATION.md §1.2 (eq. for ξ=η=0 zero modes)
- **Spine path:** S0→S1→S3→S5→S9
- **Decrees:** D0, D1 (reduction 6→4), D6 (confinement to the Firmament ξ=η=0)
- **Trace:** 1=1 → EQ-REL-01 → set the perpendicular zero modes ξ=η=0 (particle confined to the Firmament, a D6 content statement) → the induced metric on the 4D hypersurface is Minkowski. D1 supplies "4 after reduction."
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (D0,D1,D6).

### EQ-REL-03 — Lorentz-invariant interval
- **Equation:** Δs² = −c²Δt² + Δx² + Δy² + Δz²
- **Source:** 07-SPECIAL_RELATIVITY_DERIVATION.md §1.2 / §2.2
- **Spine path:** S0→S1→S3→S5→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-02 → the bilinear form of the Minkowski metric integrated along a worldline is the invariant interval; its invariance is the S7 (identity-preserving-map / isometry) statement applied to the metric of EQ-REL-02.
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-REL-04 — Proper time / Lorentz factor γ
- **Equation:** dτ = dt√(1 − v²/c²) = dt/γ,  γ = 1/√(1 − v²/c²)
- **Source:** 07-SPECIAL_RELATIVITY_DERIVATION.md §2.2 (boxed); also test_gr_observables.py Test 1
- **Spine path:** S0→S1→S3→S5→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-03 → set Δs² = −c²Δτ² for a particle at rest and Δs² = −(c²−v²)Δt² in a boosted frame → equate (S7 invariance) → solve the resulting algebra for dτ/dt. The square-root/continuum is S3+D0.
- **Constants:** c [SELECTED scale → D4]; v²/c², γ are dimensionless ratios [DERIVED ratio] (kinematic, no fit).
- **Status:** DERIVED-given-decrees.

### EQ-REL-05 — Time dilation
- **Equation:** Δt = γ Δt₀ = Δt₀/√(1 − v²/c²)
- **Source:** 07-SPECIAL_RELATIVITY_DERIVATION.md §3.1 (boxed); test_gr_observables.py Test 1
- **Spine path:** S0→S1→S3→S5→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-04 → identify Δt₀ = proper period in clock frame, apply interval invariance (S7) between frames → algebra gives Δt = γΔt₀.
- **Constants:** c [SELECTED scale → D4]; γ [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-06 — Length contraction
- **Equation:** L = L₀√(1 − v²/c²) = L₀/γ
- **Source:** 07-SPECIAL_RELATIVITY_DERIVATION.md §4.1 (corrected line 165); test_gr_observables.py Test 2
- **Spine path:** S0→S1→S3→S5→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-04 + the Lorentz transformation x=γ(x'+vt'), t=γ(t'+vx'/c²) (an S7 isometry of EQ-REL-02) → impose simultaneity in the lab frame → algebra yields L = L₀/γ.
- **Constants:** c [SELECTED scale → D4]; 1/γ [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-07 — Relativistic Doppler (general angle)
- **Equation:** f_obs = γ f_src (1 − β cosθ),  β = v/c
- **Source:** 07-SPECIAL_RELATIVITY_DERIVATION.md §5.1
- **Spine path:** S0→S1→S3→S4→S5→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → form the wave 4-vector k^μ=(ω/c, k⃗) (phase of a wave is S4) → Lorentz-boost it (S7 isometry of EQ-REL-02) → ω_obs = γ(ω_src − v k_x) with k_x=(ω/c)cosθ → divide by 2π.
- **Constants:** c [SELECTED scale → D4]; β, γ, (1−βcosθ) [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-08 — Doppler: head-on approach / recession / transverse
- **Equation:** f_obs = f_src√((1±β)/(1∓β))  (approach/recession);  f_obs = γ f_src  (transverse, θ=90°)
- **Source:** 07-SPECIAL_RELATIVITY_DERIVATION.md §5.2–5.4 (three boxed results)
- **Spine path:** S0→S1→S3→S4→S5→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-07 → substitute θ=0, π, π/2 and simplify γ(1∓β) = √((1±β)/(1∓β)). Pure algebra on the general formula.
- **Constants:** c [SELECTED scale → D4]; the √-ratios [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-09 — 4D Einstein field equations
- **Equation:** R_μν − ½ g_μν R + Λ_eff g_μν = 8πG₄/c⁴ · T_μν   (equivalently G_μν = (8πG/c⁴)T_μν)
- **Source:** 07-GR_OBSERVABLES.md §0 eq.(0.6); 07-RESOLVED_GRAVITY_MECHANISM.md §3.5 / VI; 07-GR_PRECISION (framework eq.); 07-COMPLETIONS_R4.md §"Variation"; 07-BH_MERGERS_DYNAMICS.md §1.3
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1 (a manifold to curve), D6 (T_μν content from Waters/matter), and **δS=0 borderline** (S6 note)
- **Trace:** 1=1 → S9 supplies curvature R on a manifold (D1) → the 6D Einstein-Hilbert action S=(1/16πG₆)∫R₆√−g₆ + S_matter (parent file ACTION_6D) → KK-reduce to 4D (Domain-10 input) → vary g_μν (S6, δS=0 borderline; S7 ties symmetry to the conserved Einstein/stress tensor) → field equations. T_μν content (matter + Waters) is D6.
- **Constants:** G₄ [SELECTED scale → D4, itself = G₆/V_extra, see EQ-REL-10]; Λ_eff [SELECTED scale → D4]; 8π, ½ are [DERIVED ratio] (geometric).
- **Status:** DERIVED-as-form (δS=0 borderline; given D1,D6).

### EQ-REL-10 — 4D Newton constant from extra-dimensional volume
- **Equation:** G₄ = G₆ / V_extra   (with V_extra ≈ 10⁶¹ m²)
- **Source:** 07-GR_OBSERVABLES.md §0 eq.(0.5), §1.2 eq.(1.2)–(1.3) boxed; 07-COMPLETIONS.md; 07-BH_MERGERS_DYNAMICS.md §1.2/§2.2; 07-GR_PRECISION (G=G₆/V_compact)
- **Spine path:** S0→S1→S5→S9
- **Decrees:** D0, D1 (the 2 extra dims and their volume), D6 (ξ_A, η_B = Waters/Firmament scales)
- **Trace:** 1=1 → KK-reduction of the 6D action (parent: KK_DIMENSIONAL_REDUCTION.md, Domain 10) integrates R₆ over the compact (ξ,η) volume → the 4D coupling is the 6D coupling divided by that volume. The chain is structural; the *value* of V_extra depends on selected scales ξ_A≈3×10²⁶ m, η_B≈1.3×10⁻¹⁵ m.
- **Constants:** G₄, G₆ [SELECTED scale → D4]; V_extra [SELECTED scale → D4] (built from ξ_A, η_B which are D4/D6 boundary scales).
- **Status:** DERIVED-given-decrees (the *form* G₄=G₆/V is derived; the numerical G₄=6.674×10⁻¹¹ is anchored by D4, with V_extra adjusted to match — see honesty note in EQ-REL-45).

### EQ-REL-11 — Schwarzschild metric
- **Equation:** ds² = −(1 − r_s/r)c²dt² + dr²/(1 − r_s/r) + r²(dθ² + sin²θ dφ²)
- **Source:** 07-GR_OBSERVABLES.md §0 eq.(0.7); 07-GR_PRECISION §2.2 (boxed); 07-COMPLETIONS.md §3.2; 07-BH_MERGERS_DYNAMICS.md §2.1; test_gr_observables.py header
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6, (δS=0 borderline upstream in EQ-REL-09)
- **Trace:** 1=1 → EQ-REL-09 → impose spherical symmetry + staticity + vacuum (R_μν=0) → solve the resulting ODEs (S6) to get A(r)=1−r_s/r, B(r)=1/(1−r_s/r). The identification of r_s with mass is EQ-REL-12.
- **Constants:** c [SELECTED scale → D4]; r_s [SELECTED scale → D4, via EQ-REL-12].
- **Status:** DERIVED-given-decrees.

### EQ-REL-12 — Schwarzschild radius
- **Equation:** r_s = 2GM/c²
- **Source:** 07-GR_OBSERVABLES.md §1.4 eq.(1.6) boxed; 07-GR_PRECISION §9.1; 07-COMPLETIONS.md; 07-BH_MERGERS_DYNAMICS.md §2.1; test_gr_observables.py Tests 3,11
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11 → match the weak-field limit g₀₀≈−(1+2Φ/c²) to Newtonian Φ=−GM/r → identify the integration constant as r_s=2GM/c². The factor 2 is geometric [DERIVED ratio].
- **Constants:** G, M, c all [SELECTED scale → D4] (dimensionful); 2 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-13 — Kerr metric (rotating black hole)
- **Equation:** ds² = −(Δ − a²sin²θ)/ρ² c²dt² − [2a sin²θ(r_s − r)/ρ²] c dt dφ + ρ²/Δ dr² + ρ² dθ² + [sin²θ((r²+a²)² − a²Δsin²θ)/ρ²] dφ²;  ρ²=r²+a²cos²θ, Δ=r²−r_s r+a², a=J/(Mc)
- **Source:** 07-COMPLETIONS.md §1.3 (boxed); 07-COMPLETIONS_R4.md §1.2 (boxed); 07-GW_ADVANCED_GR.md §5.1; 07-GR_OBSERVABLES.md §0 eq.(0.9)–(0.10)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6, (δS=0 borderline upstream)
- **Trace:** 1=1 → EQ-REL-09 → impose stationarity + axisymmetry + vacuum → the unique such solution of the 4D Einstein equations is the Kerr metric. Spin parameter a=J/(Mc) is a kinematic ratio.
- **Constants:** G,M,c,J [SELECTED scale → D4]; a, Δ, ρ² combinations [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-14 — Kerr horizons and ergosphere
- **Equation:** r₊ = M + √(M²−a²);  r₋ = M − √(M²−a²);  r_ergo = M + √(M²−a²cos²θ)   (geometric units)
- **Source:** 07-COMPLETIONS.md §1.4 (three boxed)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-13 → set Δ=0 (horizons, where g_rr diverges) and g_tt=0 (ergosphere) → solve quadratics in r. Pure algebra on the Kerr functions.
- **Constants:** M, a [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-REL-15 — Frame-dragging angular velocity / Lense-Thirring precession
- **Equation:** ω_drag = g_tφ/g_φφ;  weak-field Ω_LT = 2GJ/(c²r³)
- **Source:** 07-COMPLETIONS_R4.md §1.3 eq.(1.3.1) boxed; 07-GW_ADVANCED_GR.md §5.3 (boxed); 07-COMPLETIONS.md §1.5 eq.(2); 07-GR_OBSERVABLES.md §6 eq.(6.2) boxed; test_gr_observables.py Test 10
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-13 → read off the off-diagonal g_tφ, form ω_drag=g_tφ/g_φφ, expand in the slow-rotation/large-r limit → Ω_LT=2GJ/(c²r³).
- **Constants:** G,J,c [SELECTED scale → D4]; factor 2 [DERIVED ratio]. (Note: the test_gr_observables.py Test 10 uses a variant 2G/(3c²)·L/r³ with a 1/3; the .md files use 2GJ/(c²r³). Discrepant numeric coefficient — see UNTRACEABLE-U6.)
- **Status:** DERIVED-given-decrees.

### EQ-REL-16 — Mercury perihelion precession
- **Equation:** δφ = 6πGM/(c²a(1−e²)) = 3π r_s/(2a)
- **Source:** 07-GR_OBSERVABLES.md §1 eq.(1.10) boxed; 07-GR_PRECISION §8.1 (boxed); 07-BH_MERGERS_DYNAMICS.md §3.3; test_gr_observables.py Test 8
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11 → write the orbit equation d²u/dφ²+u = r_s/(2L²)+3(r_s/2)u² for a timelike geodesic (S6 geodesic eq.) → perturb a near-circular orbit → the relativistic 3u² term shifts the angular frequency, giving advance 6πGM/(c²a(1−e²)) per orbit. Factors 6π and 3 are [DERIVED ratio].
- **Constants:** G,M,c,a [SELECTED scale → D4]; e, 6π [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-17 — Light deflection by gravity
- **Equation:** δθ = 4GM/(c²b)   (GR); cf. Newtonian 2GM/(c²b)
- **Source:** 07-GR_OBSERVABLES.md §2 eq.(2.2); 07-GR_PRECISION §5.1 (boxed Δφ=2GM/bc²… see note); test_gr_observables.py Test 5
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11 → integrate the null-geodesic (ds²=0) equation in the weak-field limit r_s≪b → deflection 4GM/(c²b). The "2+2" (time-dilation + space-curvature) gives the factor 4. (07-GR_PRECISION §5.1 writes Δφ=2GM/(bc²) for the radial-only piece, then quotes 1.75″ which requires the full factor-4 result — an internal inconsistency in that file, see UNTRACEABLE-U5.)
- **Constants:** G,M,c,b [SELECTED scale → D4]; factor 4 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-18 — Gravitational redshift
- **Equation:** ν_obs/ν_emit = √((1−r_s/r_obs)/(1−r_s/r_emit));  weak field z ≈ (GM/c²)(1/r_emit − 1/r_obs) = ΔΦ/c²
- **Source:** 07-GR_OBSERVABLES.md §3 eq.(3.2)/(3.4) boxed; 07-GR_PRECISION §4.1 (boxed); test_gr_observables.py Test 4
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11 → photon frequency scales with √g₀₀ at emission/observation radii (S7 invariance of the wave phase) → ratio of √(1−r_s/r); Taylor-expand for weak field.
- **Constants:** G,M,c [SELECTED scale → D4]; z [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-19 — Gravitational time dilation
- **Equation:** dτ = √(1 − r_s/r) dt;  dτ₁/dτ₂ = √((1−r_s/r₁)/(1−r_s/r₂))
- **Source:** 07-GR_PRECISION §3.1 (boxed); test_gr_observables.py Test 3
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11 → for a static clock (dr=dθ=dφ=0), ds²=−(1−r_s/r)c²dt² gives dτ=√(1−r_s/r)dt. Ratio between two radii is algebra.
- **Constants:** G,M,c (in r_s) [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-REL-20 — Shapiro time delay
- **Equation:** Δt = (4GM/c³) ln(4r₁r₂/b²)   (grazing; radial form Δt=(2GM/c³)ln(r₂/r₁))
- **Source:** 07-GR_OBSERVABLES.md §4 eq.(4.3)/(4.4) boxed; 07-GR_PRECISION §7.1; test_gr_observables.py Test 7
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11 → integrate coordinate travel time t=∫dr/(c√(1−r_s/r)) and expand for r_s≪r → excess delay (r_s/2c)ln(r₂/r₁); grazing geometry replaces the log argument and the factor with 4GM/c³.
- **Constants:** G,M,c,b [SELECTED scale → D4]; factor 4 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-21 — Einstein ring radius (gravitational lensing)
- **Equation:** θ_E = √(4GM_lens D_LS/(c² D_OS))  (07-GR_OBS form);  θ_E = √(4GM/c² · D_LS/(D_L D_S))  (07-GR_PRECISION / py form)
- **Source:** 07-GR_OBSERVABLES.md §5 eq.(5.3) boxed; 07-GR_PRECISION §6.1; test_gr_observables.py Test 6
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-17 (deflection) → plug δθ into the lens equation β=θ−(D_LS/D_OS)δθ → set β=0 (perfect alignment) → solve θ² for the Einstein radius.
- **Constants:** G,M,c, D's [SELECTED scale → D4]; factor 4 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-22 — Geodetic precession
- **Equation:** Ω_geo = GM/(c²r³)   (circular orbit; = ½ Lense-Thirring magnitude)
- **Source:** 07-GR_OBSERVABLES.md §9 eq.(9.1)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11 → parallel-transport a spin vector around a circular geodesic (S7 holonomy/connection) → the de Sitter precession Ω_geo=GM/(c²r³).
- **Constants:** G,M,c [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-REL-23 — Linearized Einstein wave equation (GW)
- **Equation:** □ h̄_μν = −16πG₄ T_μν,  with harmonic gauge ∂^μ h̄_μν = 0, h̄_μν = h_μν − ½η_μν h
- **Source:** 07-GR_OBSERVABLES.md §7 eq.(7.2); 07-GW_ADVANCED_GR.md §1.3; 07-COMPLETIONS_R4.md §2.2; 07-BH_MERGERS_DYNAMICS.md §4.1
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-09 → write g_μν=η_μν+h_μν with |h|≪1 → linearize the Einstein tensor → in harmonic gauge the d'Alembertian □ (S6) acts on the trace-reversed perturbation = source. □ and the trace-reversal are grammar (S6/S5).
- **Constants:** G₄ [SELECTED scale → D4]; 16π [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-24 — GW far-field quadrupole strain
- **Equation:** h_μν = (4G₄/c⁴)(1/r) d²I_μν/dt²|_ret;  I_ij = ∫ T₀₀ x_i x_j d³x;  TT form h_ij=(2G₄/c⁴r)Ï_ij^TT
- **Source:** 07-GR_OBSERVABLES.md §7 eq.(7.3)/(7.4)/(7.7) boxed; 07-GW_ADVANCED_GR.md §2.1; 07-BH_MERGERS_DYNAMICS.md §4.1; 07-COMPLETIONS.md §5 eq.(20)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-23 → solve with the retarded Green's function of □ → multipole-expand a localized source → leading term is the quadrupole, h∝(G/c⁴r)Ï.
- **Constants:** G₄,c [SELECTED scale → D4]; 4 (or 2 in TT) [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-25 — Quadrupole radiated power (Peters–Mathews)
- **Equation:** P = (32/5)(G₄⁴/c⁵)(m₁m₂)²(m₁+m₂)/a⁵;  general P = (G/5c⁵)Σ(d³I_ij/dt³)²
- **Source:** 07-GW_ADVANCED_GR.md §2.3 (boxed); 07-COMPLETIONS_R4.md §2.2 eq.(2.2.1) boxed; 07-GR_OBSERVABLES.md §7.2 eq.(7.8); 07-BH_MERGERS_DYNAMICS.md §4.2 eq.; test_gr_observables.py Test 9
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-24 → compute the energy flux of h (stress-energy of the GW field) integrated over a sphere → P=(G/5c⁵)⟨(d³I/dt³)²⟩ → insert a circular-binary quadrupole with ω²=G(m₁+m₂)/a³ (Kepler, EQ-REL-30) → algebra gives the 32/5 form.
- **Constants:** G,c,masses [SELECTED scale → D4]; 32/5 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-26 — Orbital decay rate (da/dt)
- **Equation:** da/dt = −(64/5)(G₄³/c⁵) m₁m₂(m₁+m₂)/a³
- **Source:** 07-COMPLETIONS_R4.md §2.3 eq.(2.3.1) boxed; 07-BH_MERGERS_DYNAMICS.md §3.4 boxed; 07-GR_OBSERVABLES.md §8.1 eq.(8.1)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-25 + orbital energy E=−Gm₁m₂/2a → set dE/dt=−P → solve for da/dt. Pure calculus.
- **Constants:** G,c,masses [SELECTED scale → D4]; 64/5 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-27 — Period decay (Hulse–Taylor)
- **Equation:** Ṗ = −(192π/5)(G₄³/c⁵) m₁m₂(m₁+m₂) P^(−2/3)  (×kinematic factors)
- **Source:** 07-COMPLETIONS_R4.md §2.5; 07-GR_OBSERVABLES.md §8 eq.(8.3) (merger-time form t₀)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6, D5 (the predicted −2.40×10⁻¹² matched to data)
- **Trace:** 1=1 → EQ-REL-26 → convert da/dt to Ṗ using Kepler's third law (P∝a^(3/2)) → the 192π/5 form. The reported numeric −2.40×10⁻¹² s/s uses fitted neutron-star masses 1.44/1.39 M_☉ → D5.
- **Constants:** G,c [SELECTED scale → D4]; m₁,m₂ values [FIT → D5]; 192π/5 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form); the validated number is PARTIAL (depends on D5 masses).

### EQ-REL-28 — Chirp mass
- **Equation:** M_c = (m₁m₂)^(3/5)/(m₁+m₂)^(1/5)
- **Source:** 07-GW_ADVANCED_GR.md §3.1; 07-COMPLETIONS_R4.md §2.3; 07-COMPLETIONS.md §4.3 eq.(12) boxed; 07-GR_OBSERVABLES.md §7.3/§11.2
- **Spine path:** S0→S1→S2
- **Decrees:** D0, D4 (the constituent masses m₁,m₂ are dimensionful scales)
- **Trace:** 1=1 → S2 supplies products/ratios and rational powers → M_c is *defined* as the particular mass combination that factors out of the frequency-evolution equation (EQ-REL-29). It is an algebraic definition, not a separate physical law; its content is fixed once EQ-REL-29 is derived. Because M_c is built from the dimensionful masses m₁,m₂, the definition carries D4 (it is "1 in chosen mass units"); the S2 rung supplies the rational-power algebra and that is the only differential/operator content — no S6 step is actually used.
- **Constants:** masses m₁,m₂ [SELECTED scale → D4]; exponents 3/5, 1/5 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (definition).

### EQ-REL-29 — Chirp frequency evolution
- **Equation:** df/dt = (96/5)π^(8/3)(G₄M_c/c³)^(5/3) f^(11/3)
- **Source:** 07-GW_ADVANCED_GR.md §3.2 eq. (boxed); 07-COMPLETIONS_R4.md §2.4 eq.(2.4.1) boxed; 07-COMPLETIONS.md §4.3 eq.; 07-BH_MERGERS_DYNAMICS.md §4.3
- **Spine path:** S0→S1→S2→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-26 (da/dt) + Kepler f=(1/π)√(G M/a³) → differentiate f w.r.t. a, substitute da/dt → the masses collapse into M_c^(5/3); the 96/5 and π^(8/3) are geometric.
- **Constants:** G,c [SELECTED scale → D4]; M_c via EQ-REL-28; 96/5, π^(8/3), 11/3 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-30 — Kepler's third law (relativistic binary)
- **Equation:** ω² = G(m₁+m₂)/a³;  T = 2π√(a³/(G M))
- **Source:** 07-GW_ADVANCED_GR.md §2.3; 07-COMPLETIONS_R4.md §2.2; 07-BH_MERGERS_DYNAMICS.md §3.1
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → Newtonian limit of EQ-REL-09 (Poisson, EQ-REL-34) → two-body reduction with centripetal balance μω²a = Gm₁m₂/a² → ω²=GM/a³. (Used as an input to EQ-REL-25/26/29.)
- **Constants:** G, masses [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-REL-31 — GW strain amplitude (in terms of chirp mass)
- **Equation:** h(t) = (2/r)(G₄M_c/c²)^(5/3)(πf)^(2/3) × [polarization]
- **Source:** 07-GW_ADVANCED_GR.md §4.1 eq. (boxed); 07-GR_OBSERVABLES.md §7.3 eq.(7.10); 07-COMPLETIONS.md §4.2 eq.(11); 07-BH_MERGERS_DYNAMICS.md §4.3
- **Spine path:** S0→S1→S2→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-24 (h∝Ï/r) → insert circular-binary quadrupole and Kepler relation → amplitude ∝(GM_c/c²)^(5/3)(πf)^(2/3)/r.
- **Constants:** G,c [SELECTED scale → D4]; M_c (EQ-REL-28); exponents [DERIVED ratio]; polarization factor ~O(1) [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-32 — Regge–Wheeler equation + QNM frequencies
- **Equation:** d²ψ/dr*² + (ω² − V_RW)ψ = 0, V_RW = (1−r_s/r)[ℓ(ℓ+1)/r² + r_s/r³];  ℓ=2,n=0: ω = (0.3737 − 0.0890 i) c³/(GM)
- **Source:** 07-COMPLETIONS_R4.md §3.2–3.3 (boxed ω₂); 07-COMPLETIONS.md §4.5 eq.(15) ringdown; 07-BH_MERGERS_DYNAMICS.md §6.2 (f₂₂₀≈0.1494 c³/GM)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11 → perturb the Schwarzschild metric, decompose in spherical harmonics (S5/S7), odd-parity sector → Regge-Wheeler ODE (S6) with the stated potential → solving the eigenvalue/boundary problem yields the complex QNM ω. The dimensionless numbers 0.3737, 0.0890 are computed eigenvalues [DERIVED ratio].
- **Constants:** G,M,c [SELECTED scale → D4]; mode coefficients [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-33 — Price's theorem (power-law tail)
- **Equation:** h_μν(t,r) ~ C/t^(2ℓ+3)  (e.g. ℓ=2 → t^(−7))
- **Source:** 07-COMPLETIONS_R4.md §3.5 eq.(3.5.1) boxed
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6, D3? — no; the exponent is set by ℓ (a harmonic index, S5/S8), not by a winding decree
- **Trace:** 1=1 → EQ-REL-32 framework → late-time perturbation decay is governed by coupling to zero-frequency modes; the multipole index ℓ (an S5/S8 integer, generic — not the n_w=3 of D3) fixes the power 2ℓ+3.
- **Constants:** exponent 2ℓ+3 [count] (harmonic index, S5/S8 — *not* D3).
- **Status:** DERIVED-given-decrees.

### EQ-REL-34 — Poisson equation / Newton's law (weak-field limit)
- **Equation:** ∇²Φ = 4πGρ;  F = −m∇Φ = GMm/r²;  (from ∇²η = −4πGρ/c², Φ=−½c²η)
- **Source:** 07-RESOLVED_GRAVITY_MECHANISM.md §3.6/§6.5; 07-BH_MERGERS_DYNAMICS.md §1.3; 07-GR_PRECISION §11
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-23 (linearized Einstein) → synchronous/static gauge, slow matter → ∇²h₀₀=−(8πG/c⁴)ρ collapses to Poisson with Φ=−c²h₀₀/4 → gradient gives the inverse-square force.
- **Constants:** G [SELECTED scale → D4]; 4π [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-35 — Gravity as η-curvature (induced 4D metric)
- **Equation:** g_μν = δ_μν + ½ (∂η/∂x_μ)(∂η/∂x_ν) + …;  weak field g₀₀≈−c²(1+2Φ/c²), g_ij≈δ_ij(1+2Φ/c²); R_μν ≈ −∂²η/∂x_μ∂x_ν + …;  ∂²η/∂t² + ∇²η = κ T⁰⁰
- **Source:** 07-RESOLVED_GRAVITY_MECHANISM.md §3.3–3.5
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6 (η = Waters-Below direction; matter = condensed Waters), δS=0 borderline
- **Trace:** 1=1 → EQ-REL-01 (6D metric) → let matter perturb the η-coordinate (D6 content: matter is a Waters-Below intrusion) → the induced (Gauss-Codazzi) metric on the 4D Firmament inherits curvature ∝∂²η → identify with the Ricci tensor and hence EQ-REL-09. The η-source equation (□η=κT⁰⁰) is a structural ansatz of the framework, not a forced step.
- **Constants:** κ [SELECTED scale → D4] (= function of ρ_critical and ℏ); ½, 2 [DERIVED ratio].
- **Status:** PARTIAL (the η-mechanism is a D6 modeling ansatz; the *form* matches GR but the κ-coupling map is asserted, not derived).

### EQ-REL-36 — Gravitational constant from membrane tension
- **Equation:** G = σ_membrane/(ρ_critical · c²)
- **Source:** 07-RESOLVED_GRAVITY_MECHANISM.md §6.4/§10.1 (boxed dimensional form)
- **Spine path:** S0→S1→S5→S9
- **Decrees:** D0, D1, D4, D6 (σ, ρ_critical are Firmament/Waters content scales)
- **Trace:** 1=1 → dimensional analysis matches [G]=L³M⁻¹T⁻² to [σ]/([ρ][c²]) → G=σ/(ρ_crit c²). The file itself flags this as "circular, determines G self-consistently" (§6.4) — i.e. it is a *consistency relation*, not an independent prediction.
- **Constants:** σ, ρ_critical, c, G all [SELECTED scale → D4].
- **Status:** PARTIAL (dimensional/self-consistent only; the file admits circularity — the numerical G is anchored, not derived).

### EQ-REL-37 — 6D Einstein-Hilbert action & 6D field equations
- **Equation:** S=(1/16πG₆)∫d⁶x√−g₆ R₆ (+matter, +Λ₆);  G_MN + Λ₆ g_MN = (8πG₆/c⁴)T_MN
- **Source:** 07-RESOLVED_GRAVITY_MECHANISM.md §6.1; 07-COMPLETIONS.md §1.1; 07-GW_ADVANCED_GR.md §1.1; 07-COMPLETIONS_R4.md §1.1; 07-FTL_MECHANISMS_FORMAL.md §0.3; 07-BH_MERGERS_DYNAMICS.md §1.1
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1 (6 dims), D6 (T_MN = Waters + matter), δS=0 borderline
- **Trace:** 1=1 → S9 supplies curvature R₆ on a 6-manifold (D1) → the Einstein-Hilbert action is the simplest diffeomorphism-invariant scalar (S7) integrated over the manifold (S6) → δS=0 yields the 6D field equations. This is the *parent* of all GR results here; the canonical derivation lives in ACTION_6D_COMPLETE.md (Foundations).
- **Constants:** G₆, Λ₆, c [SELECTED scale → D4]; 16π, 8π [DERIVED ratio].
- **Status:** DERIVED-as-form (δS=0 borderline; given D1,D6).

### EQ-REL-38 — 6D KK metric ansatz (warped)
- **Equation:** ds² = e^{2A(ξ,η)} g̃_μν dx^μ dx^ν + e^{2B(ξ,η)}(dξ²+dη²)
- **Source:** 07-GR_OBSERVABLES.md §0 eq.(0.3); 07-FTL_MECHANISMS_FORMAL.md §0.1 (boxed, with a²(t) factor); 07-BH_MERGERS_DYNAMICS.md §1.2; op10_z1_field_equations.md §1
- **Spine path:** S0→S1→S5→S9
- **Decrees:** D0, D1, D6 (the warp profiles A,B = Waters geometry)
- **Trace:** 1=1 → S9 metric on M⁴×K² (D1) → require 4D Poincaré invariance → metric factorizes into a warped 4D block times the (ξ,η) block. The warp factors A,B are D6/D9-profile content.
- **Constants:** warp factors e^{2A}, e^{2B} [SELECTED scale → D4]; a(t) scale factor [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (the *form* is forced by Poincaré invariance; the profiles are D6).

### EQ-REL-39 — Hawking temperature
- **Equation:** T_H = ℏc³/(4πk_B GM) = ℏc/(4πk_B r_s)   (factor 8π in test_gr_observables.py & some texts)
- **Source:** 07-COMPLETIONS.md §2.1 eq.(3) boxed; test_gr_observables.py Test 11 (uses 8π)
- **Spine path:** S0→S1→S4→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11 (Schwarzschild) + quantum field phase (S4) → surface gravity κ_grav=c⁴/(4GM) sets the periodicity of Euclidean time → T_H=ℏκ_grav/(2πck_B). The framework also re-derives it from "Firmament mode counting" (D6), reaching the same form. (Note: 07-COMPLETIONS.md writes 4π; the .py file writes 8π — a coefficient discrepancy, see UNTRACEABLE-U4.)
- **Constants:** ℏ,c,G,M,k_B [SELECTED scale → D4]; 4π/8π [DERIVED ratio, but inconsistent across files].
- **Status:** PARTIAL (form derived; coefficient inconsistent between files).

### EQ-REL-40 — Bekenstein–Hawking entropy
- **Equation:** S = k_B A/(4ℓ_P²) = π k_B r_s²/ℓ_P² = 4πG k_B M²/(ℏc);  A₀ = 4πℓ_P²
- **Source:** 07-COMPLETIONS.md §2.2 eq.(4)/(5)/(6) boxed
- **Spine path:** S0→S1→S5→S8→S9
- **Decrees:** D0, D1, D6 (Firmament mode-counting content)
- **Trace:** 1=1 → horizon area A=4πr_s² (geometry) → count Planck-area cells N=A/ℓ_P² (S8 integer invariants / mode counting) → S=k_B ln(states)≈k_B N/4. The framework attributes the cell counting to Firmament oscillation modes (D6). The 1/4 is asserted to match Bekenstein, not independently derived.
- **Constants:** ℓ_P, M [SELECTED scale → D4]; the 1/4 factor [DERIVED ratio, matched to Bekenstein].
- **Status:** PARTIAL (mode-counting gives A/ℓ_P²; the exact 1/4 is matched, not forced).

### EQ-REL-41 — Black-hole evaporation (mass loss & lifetime)
- **Equation:** dM/dt = −ℏc⁶/(15360πG²M²);  t_evap = 5120πG²M³/(ℏc⁴)
- **Source:** 07-COMPLETIONS.md §2 (numerical-verification block)
- **Spine path:** S0→S1→S4→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-39 (T_H) + Stefan-Boltzmann-type horizon luminosity L∝A T_H⁴ → dM/dt=−L/c² → integrate for t_evap∝M³. The numerical prefactors 15360π, 5120π are standard greybody-free results [DERIVED ratio].
- **Constants:** ℏ,c,G,M [SELECTED scale → D4]; prefactors [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-42 — Conformal rescaling / Penrose compactification
- **Equation:** g̃_μν = Ω²(x) g_μν;  Kruskal T,X = (r_s/2c)e^{cr/2r_s}{sinh,cosh}(ct/r_s);  Penrose (ũ,ṽ)=(arctan u_K, arctan v_K)
- **Source:** 07-COMPLETIONS.md §3.1–3.4 eq.(7)/(8)/(9) (diagrams) and the boxed conformal map
- **Spine path:** S0→S1→S4→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → a conformal map Ω² rescales the metric (S9) preserving light cones (S4 phase/causal structure) → Kruskal coordinates regularize the horizon → arctan compactifies infinity to a finite diagram. These are coordinate constructions, not new physical law.
- **Constants:** r_s, c [SELECTED scale → D4]; Ω(x) dimensionless [DERIVED ratio].
- **Status:** DERIVED-given-decrees (coordinate/geometric).

### EQ-REL-43 — Causal disconnection of BH interior
- **Equation:** J⁻(ℐ⁺) ∩ I⁺(r=r_s) = ∅
- **Source:** 07-COMPLETIONS.md §3 eq.(10) boxed
- **Spine path:** S0→S1→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-42 (causal structure of the Penrose diagram) → the horizon is a null one-way surface → the causal past of future infinity excludes the interior. This is a topological/causal statement read off the diagram, not a numeric equation.
- **Constants:** none dimensionful.
- **Status:** DERIVED-given-decrees (causal-structure statement).

### EQ-REL-44 — Wave speed from membrane properties
- **Equation:** c = √(σ/μ)   (σ = Firmament tension, μ = mass density)
- **Source:** 07-SPECIAL_RELATIVITY_DERIVATION.md §1.1; 07-COMPLETIONS_R4.md §"Genesis Physics Context"; test_gr_observables.py header
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D4 (σ, μ are dimensionful Firmament scales), D6 (membrane content)
- **Trace:** 1=1 → the Firmament is modeled as an elastic membrane (D6) → the standard wave equation on a tensioned membrane (S6) has phase speed √(tension/density) → identify with c. σ and μ are selected scales whose ratio is set to c²; this is an anchoring, not an independent prediction of c.
- **Constants:** σ, μ [SELECTED scale → D4]; c [SELECTED scale → D4].
- **Status:** PARTIAL (form is the membrane wave-speed; the *value* c is anchored by choosing σ/μ — D4).

### EQ-REL-45 — Lense-Thirring / GP-B numerical prediction (39 mas/yr)
- **Equation:** Ω_LT ≈ 39 mas/yr (Earth, GP-B orbit), from Ω_LT=2GJ/(c²r³)
- **Source:** 07-COMPLETIONS_R4.md §1.5–1.6 (verification box); 07-GW_ADVANCED_GR.md §5.4
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6, D5 (Earth model / geometric factor reconciled to the 37.2 mas/yr datum)
- **Trace:** 1=1 → EQ-REL-15 → insert Earth's J, GP-B orbit r → the bare formula gives ~0.26 mas/yr (file's own first computation), then a "geometric factor" is invoked to reach 39 mas/yr to match GP-B's 37.2±7.2. The reconciling geometric factor is data-driven → D5.
- **Constants:** G,J,c,r [SELECTED scale → D4]; geometric-factor reconciliation [FIT → D5].
- **Status:** PARTIAL (the formula is derived; the matched number requires an undisclosed geometric factor → D5; see UNTRACEABLE-U6 for the coefficient mismatch).

### EQ-REL-46 — Black hole shadow angular size
- **Equation:** θ_shadow ≈ 5.2 GM/(c²D);  photon sphere r_ph = (3/2)r_s; b = 2√27 GM/c²;  r_shadow = 3√3 GM/c²
- **Source:** 07-GR_OBSERVABLES.md §10 eq.(10.1)–(10.4) boxed; 07-BH_MERGERS_DYNAMICS.md §8.3
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11/EQ-REL-13 → photon circular-orbit condition (ds²=0 geodesic, S6) gives r_ph=3GM/c² and critical impact parameter b=3√3 GM/c²=2√27·GM/c² → divide by distance D for the angular size. The 5.2≈3√3 is geometric [DERIVED ratio].
- **Constants:** G,M,c,D [SELECTED scale → D4]; 3√3≈5.2 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-47 — ISCO radius and frequency
- **Equation:** r_ISCO = 6GM/c² = 3r_s;  f_ISCO = c³/(6^{3/2}πG M)
- **Source:** 07-COMPLETIONS_R4.md §4.2; 07-BH_MERGERS_DYNAMICS.md §2.1/§5.1
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-11 → effective-potential analysis of timelike geodesics (S6) → the innermost stable circular orbit is where the effective potential's stable minimum disappears, at r=6GM/c²; the orbital frequency there follows from Kepler.
- **Constants:** G,M,c [SELECTED scale → D4]; 6, 6^{3/2} [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-REL-48 — Final-mass / radiated-energy relation (BH merger)
- **Equation:** M_f = (m₁+m₂)(1 − E_rad/Mc²);  E_rad/Mc² ≈ 0.048 (equal-mass);  E_rad=(1−M_f/M_i)c²
- **Source:** 07-COMPLETIONS_R4.md §4.4 / §4.7; 07-COMPLETIONS.md §4.5 eq.(16) boxed; 07-GR_OBSERVABLES.md §11.4
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6, D5 (the 0.048 / 3 M_☉ radiated comes from numerical relativity fitted to GW150914)
- **Trace:** 1=1 → mass-energy conservation (S1 conservation form) applied to the merger: final mass = initial − radiated. The *fraction* radiated (≈4.8%, spin a_f≈0.67) is a numerical-relativity result calibrated to data → D5.
- **Constants:** masses [SELECTED scale → D4]; 0.048, a_f≈0.67 [FIT → D5 / numerical-relativity].
- **Status:** PARTIAL (conservation form is exact; the radiated fraction & final spin are NR/fit numbers → D5).

### EQ-REL-49 — FTL temporal-shortcut proper time
- **Equation:** τ_shortcut ≈ ∫ e^{A(ξ(s))}√(−c²(dt/ds)² + a²‖∇_⊥r‖²) ds + ∫ e^{B(ξ)}dξ;  v_eff = d/τ_shortcut > c
- **Source:** 07-FTL_MECHANISMS_FORMAL.md §1.3–1.4
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D6 (warp factors A,B = Waters geometry)
- **Trace:** 1=1 → EQ-REL-38 (warped 6D metric) → proper time along a worldline that excursions into larger ξ (Waters Above) is compressed by the e^{A} warp factor → effective 4D speed exceeds c. The geodesic structure is rigorous; the *engineerability* of the required A-perturbation is speculative (file rates it ~70% rigorous).
- **Constants:** warp factors, c [SELECTED scale → D4]; e^{−λ_AΔξ} reduction [DERIVED ratio given a chosen Δξ].
- **Status:** PARTIAL (geodesic form derived from D6 metric; engineering claim is speculative, not an equation that predicts data).

### EQ-REL-50 — FTL warp-bubble (Alcubierre-like) metric & energy
- **Equation:** ds₄² = −(c²−v_b²)dt² + 2v_b c dt dx + dx²+dy²+dz²;  E ~ (c⁴/16πG) h R
- **Source:** 07-FTL_MECHANISMS_FORMAL.md §4.3 (boxed) / §4.4
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6 (Waters field Ψ_A configuration sources the bubble)
- **Trace:** 1=1 → EQ-REL-09 → engineer a stress-energy from a localized Waters-Above field configuration (D6) → the induced 4D metric takes the Alcubierre form with bubble velocity v_b. The energy estimate uses the linearized T_μν~(c⁴/16πG)h/L².
- **Constants:** c,G [SELECTED scale → D4]; v_b, h, R [SELECTED scale → D4]; 16π [DERIVED ratio].
- **Status:** PARTIAL (the metric form is GR-standard; the Waters-field sourcing and causality "Sabbath boundary" arguments are D6 modeling, not derived predictions).

### EQ-REL-51 — FTL zone-tunneling (WKB) probability
- **Equation:** P = exp(−(2/ℏ)∫₀^a √(2m(V(η)−E)) dη) = exp(−2√(2mV₀)L/ℏ)
- **Source:** 07-FTL_MECHANISMS_FORMAL.md §3.2; 07-FTL_MECHANISMS_SUMMARY.md (Mechanism 3 key eq.)
- **Spine path:** S0→S1→S4→S6→S9
- **Decrees:** D0, D6 (zone-boundary potential V₀~σ is Firmament content)
- **Trace:** 1=1 → the zone boundary at η=0 is modeled as a quantum potential step V(η) (D6) → standard WKB tunneling through a barrier (S4 phase + S6 integral) gives the exponential suppression. The barrier height V₀~σ (membrane tension) is D6/D4.
- **Constants:** ℏ, m, V₀~σ, L [SELECTED scale → D4]; the exponent [DERIVED ratio given those scales].
- **Status:** DERIVED-given-decrees (the WKB form is standard QM; the zone-barrier identification is D6).

### EQ-REL-52 — Z₁ field equations (atemporal zone)
- **Equation:** ³R_Z1 = 16πG₅ ρ_Z1 (Hamiltonian constraint);  d²A_Z1/dξ² + (dA_Z1/dξ)² = −(4/3)k₁²,  A_Z1(ξ)=(2/3)ln(L_A/ξ)+C₁;  □_Z1 κ + V'(κ)=J_κ;  □_Z1 Ψ_A − m_A² e^{2B} Ψ_A = 0;  L_A = 3/(2k₁), k₁²=−Λ_Z1/5
- **Source:** op10_z1_field_equations.md §2.1–2.4, §3
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6 (Z₁ atemporal zone, κ sustaining field, Ψ_A Waters-Above field), δS=0 borderline
- **Trace:** 1=1 → EQ-REL-37/EQ-REL-38 specialized to Zone Z₁ with lapse N=0 (atemporality, a D6 zone-architecture condition) → the Einstein equations reduce to constraint-only (no evolution); the warp factor obeys a Randall-Sundrum-type ODE whose solution A_Z1=(2/3)ln(L_A/ξ) reproduces the assumed Waters-Above profile; κ and Ψ_A obey their reduced wave equations. L_A↔Λ_Z1 link is left **OPEN** in the source.
- **Constants:** G₅, L_A, k₁, Λ_Z1, m_A [SELECTED scale → D4]; 2/3, 4/3, 5 [DERIVED ratio]; ε, n_A profile params unfixed.
- **Status:** PARTIAL (field-equation forms written and self-consistent; L_A/Λ_Z1 determination explicitly OPEN in the source — depends on unspecified Z₀ physics).

### EQ-REL-53 — Geodesic equation / equivalence principle
- **Equation:** d²x^A/dτ² + Γ^A_BC (dx^B/dτ)(dx^C/dτ) = 0  (6D; reduces to d²x^μ/dτ² + Γ^μ_ρσ ẋ^ρ ẋ^σ = 0 on the Firmament ξ̇=η̇=0) ⇒ Equivalence Principle (motion independent of m₀)
- **Source:** 07-GR_PRECISION_OBSERVABLES.md §1.1 (boxed "Geodesic motion ⇒ Equivalence Principle"); 07-FTL_MECHANISMS_FORMAL.md §1.2; 07-RESOLVED_GRAVITY_MECHANISM.md §3.7
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1 (a manifold with a connection to move on), D6 (Firmament confinement ξ=η=0 for the 4D reduction)
- **Trace:** 1=1 → S9 supplies a metric/connection on a manifold (D1) → extremizing the particle action S=−∫m₀√(g_AB ẋ^A ẋ^B)dτ (S6 variation; S7 ties reparametrization invariance to the affine-geodesic form) → the Euler-Lagrange equation is the geodesic equation, whose Christoffel symbols depend only on g_AB, not on m₀. Mass-independence is the equivalence principle. Restricting to the Firmament zero modes (D6) gives the 4D geodesic equation used by EQ-REL-16/17/22.
- **Constants:** none dimensionful (Γ^A_BC are geometric [DERIVED ratio]); m₀ cancels.
- **Status:** DERIVED-as-form (δS=0 borderline; given D1,D6).

### EQ-REL-54 — 6D static spherical (Schwarzschild–Reissner–Nordström) analog metric
- **Equation:** ds² = −(1 − r_s/r − r_q²/r²)c²dt² + (1 − r_s/r − r_q²/r²)⁻¹dr² + r²(dθ² + sin²θ dφ²) + (1 − ρ_B(η)/ρ_crit)dη² + (1 − ρ_A(ξ)/ρ_crit,above)dξ²
- **Source:** 07-RESOLVED_GRAVITY_MECHANISM.md §6.2
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1 (6 dims), D6 (ρ_A(ξ), ρ_B(η) = Waters-Above/Below density profiles fill the ξ,η blocks), δS=0 borderline (upstream in EQ-REL-37)
- **Trace:** 1=1 → EQ-REL-37 (6D Einstein eqs) → impose staticity + spherical symmetry in the 4D block and product structure in the extra dimensions → the 4D block is the Reissner–Nordström form (Schwarzschild + charge term r_q²/r²) and the (ξ,η) blocks carry the Waters density profiles. The r_q² (charge) term is a structural option; ρ_A,ρ_B profiles are D6 content. This is the 6D parent of the purely-4D EQ-REL-11.
- **Constants:** r_s, r_q [SELECTED scale → D4]; ρ_A,ρ_B,ρ_crit [SELECTED scale → D4, D6 profiles]; the metric-coefficient combinations [DERIVED ratio].
- **Status:** PARTIAL (the 4D RN block is GR-standard; the ξ,η Waters-density blocks are an asserted D6 ansatz, not derived — the profiles ρ_A(ξ),ρ_B(η) are not fixed in-source).

### EQ-REL-55 — GW polarization tensor (plus/cross) and detector strain
- **Equation:** h_ij^TT = [[h₊cos(ωt−kz), h_×sin(ωt−kz), 0],[h_×sin(ωt−kz), −h₊cos(ωt−kz),0],[0,0,0]];  ΔL_x = (L/2)h₊, ΔL_y = −(L/2)h₊;  h(t) = (ΔL_x − ΔL_y)/L = h₊
- **Source:** 07-COMPLETIONS.md §5.1 eq.(17)/(18)/(19) (boxed); 07-GR_OBSERVABLES.md §7 (TT perturbation); 07-BH_MERGERS_DYNAMICS.md §7.2 (h_+ , h_×)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6
- **Trace:** 1=1 → EQ-REL-23 (□h̄_μν=0 in vacuum) → impose the transverse-traceless gauge for a wave along ẑ (S7 residual-gauge fixing) → only two independent components survive, the plus/cross polarizations. A detector arm of length L stretched by the wave records ΔL/L = h, and the differential of two orthogonal arms isolates h₊. The "two polarizations" count is the spin-2 / TT structure [count] (geometric, S5/S7 — not a D3 generation count).
- **Constants:** h₊, h_× dimensionless strains [DERIVED ratio]; L, ω, k [SELECTED scale → D4]; the 2 polarization count [count] (TT structure, not D3).
- **Status:** DERIVED-given-decrees (gauge/geometry of the linearized wave).

### EQ-REL-56 — First law of black-hole thermodynamics
- **Equation:** dM = T_H dS + Ω_H dJ + Φ_H dQ;  (Schwarzschild, J=Q=0): dM = T_H dS;  T_H = (∂M/∂S)|_J = ℏc³/(4πGk_B M)
- **Source:** 07-COMPLETIONS.md §2.4 (boxed dM=T_H dS)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D0, D1, D6 (horizon = Firmament mode-counting surface)
- **Trace:** 1=1 → EQ-REL-39 (T_H) + EQ-REL-40 (S∝A) → differentiate the mass-area relation A=16πG²M²/c⁴ and substitute T_H, recovering dM=T_H dS for Schwarzschild; the rotating/charged terms Ω_H dJ + Φ_H dQ follow by the same area-variation argument on the Kerr-Newman horizon (S1 conservation/exactness form, S6 differential). This is a thermodynamic identity built on EQ-REL-39/40, not an independent law.
- **Constants:** ℏ,c,G,M,k_B [SELECTED scale → D4]; Ω_H,Φ_H [DERIVED ratio of horizon quantities]; 4π [DERIVED ratio].
- **Status:** PARTIAL (the identity follows algebraically from T_H and S=A/4, which are themselves PARTIAL — see EQ-REL-39 coefficient issue U4 and EQ-REL-40's matched 1/4).

---

## UNTRACEABLE / honesty audit

- **UNTRACEABLE-U1 — Λ_Z1 from Z₀ physics.** op10_z1_field_equations.md §5 states the closing
  link (compute Λ_Z1, hence L_A and β_geom, from the Z₀ action) is OPEN. No spine path reaches a
  numerical Λ_Z1; the Z₀ sector is unspecified. Cannot be traced beyond "set by Z₀."
- **UNTRACEABLE-U2 — κ coupling constant in the η-gravity mechanism (EQ-REL-35).**
  07-RESOLVED_GRAVITY_MECHANISM.md §3.3 introduces ∂²η+∇²η=κT⁰⁰ with κ "determined by ρ_critical
  and ℏ" but never derives κ; the map from η-curvature to the actual Einstein tensor is asserted.
- **UNTRACEABLE-U3 — G = σ/(ρ_crit c²) numerical value (EQ-REL-36).** The file itself flags the
  membrane-tension derivation of G as "circular, determines G self-consistently" and the §10.2
  numerical attempt is abandoned mid-calculation ("Wait, need to be careful with units…"). The
  value of G is anchored (D4), not predicted.
- **UNTRACEABLE-U4 — Hawking-temperature coefficient (EQ-REL-39).** 07-COMPLETIONS.md uses
  T_H=ℏc³/(4πk_B GM); test_gr_observables.py Test 11 uses 8π. The two differ by a factor 2 with no
  reconciliation. The *form* is standard but the framework does not fix the coefficient internally.
- **UNTRACEABLE-U5 — Light-deflection coefficient inconsistency (EQ-REL-17).**
  07-GR_PRECISION_OBSERVABLES.md §5.1 boxes Δφ=2GM/(bc²) (Newtonian/half value) yet then reports
  1.75″, which requires the factor-4 GR result. The displayed equation and the quoted number are
  mutually inconsistent within that file (07-GR_OBSERVABLES.md has the correct factor 4).
- **UNTRACEABLE-U6 — Frame-dragging coefficient & GP-B reconciliation (EQ-REL-15/45).** The .md
  files use Ω_LT=2GJ/(c²r³); test_gr_observables.py Test 10 uses 2G/(3c²)·L/r³ (extra 1/3) and a
  hand-set "expected" 54.5 mas/yr, while 07-COMPLETIONS_R4.md's bare formula yields 0.26 mas/yr and
  is then rescaled to 39 mas/yr by an undisclosed "geometric factor" to match GP-B (37.2±7.2). The
  reconciling factor is not derived — it is fitted to the datum (→ D5).

*Cross-ref: SPINE.md (S0–S9), DECREE_REGISTER.md (D0–D6), README_SCHEMA.md.*
