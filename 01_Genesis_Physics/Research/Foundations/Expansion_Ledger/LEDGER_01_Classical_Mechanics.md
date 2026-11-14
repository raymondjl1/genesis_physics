# Expansion Ledger — Domain 01: Classical Mechanics

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This ledger traces every displayed/numbered equation and named key result in the
> Classical Mechanics domain back to the seed `1=1` via the spine rungs (`SPINE.md`, S0–S9)
> and the decree register (`DECREE_REGISTER.md`, D0–D6). No equation is "derived from `1=1`
> alone": each = spine path + named decrees + equation-specific algebra. Constants are tagged
> `[DERIVED ratio]` / `[SELECTED scale → D4]` / `[FIT → D5]` / `[count → D3]`.
> Reference docs: `SPINE.md`, `DECREE_REGISTER.md`, `README_SCHEMA.md`.

## Header table

| Metric | Value |
|--------|-------|
| **# equations traced** | 105 (EQ-CM-01 … EQ-CM-105) |
| **Decrees used across domain** | D0 (completed infinity / ℝ), D1 (dimension / manifold; also the spatial-dimension count 3 in DOF/DOS results), D2 (charge / EM coupling — imported into EQ-CM-102/103 from the Electromagnetism domain), D4 (scale anchor / units), D5 (residual fitted O(1) constants — LJ params, Born-Mayer, restitution, latent-heat prefactors, critical exponents), D6 (architectural axioms: Firmament, Waters, sustaining coupling) |
| **# UNTRACEABLE** | 1 full (EQ-CM-52, the membrane-derived form/value of γ damping, `01-COMPLETIONS.md` §6.1). EQ-CM-95 additionally carries a *within-row* UNTRACEABLE note: real-fluid critical exponents are not captured by the mean-field treatment. |
| **# PARTIAL** | 5 (EQ-CM-85 LJ 12-repulsion, EQ-CM-86 real restitution, EQ-CM-92 latent-heat prefactors, EQ-CM-102 Born-Mayer B,ρ, EQ-CM-103 Young's-modulus scaling) |

**Domain note.** Almost everything in this domain is *standard classical mechanics recovered as a
weak-field / non-relativistic / continuum limit* of the 6D action. The honest pattern repeats:
the equation's **form** is forced by the spine (S1 conservation, S5 vector/tensor structure, S6
calculus, S7 Noether), while the **6D-membrane provenance** (the action, warp factors, zone fields)
injects **D1** (a manifold of some dimension) and **D6** (the architectural field content). The
*dimensionful constants* (G, σ, c, k_B, ε, etc.) are all `[SELECTED scale → D4]` — they are "1 in
chosen units." Genuinely matched-to-data O(1) numbers are flagged `[FIT → D5]`. Dimensionless
ratios forced by geometry (e.g. 2/5 for a sphere, the 3/2 de Sitter factor) are `[DERIVED ratio]`.

**Two decrees beyond the headline four appear in this domain and must be cited honestly:**
(i) **D2** — the electric charge / Coulomb coupling `e²/4πε₀` in the ionic-crystal elasticity
results (EQ-CM-102, EQ-CM-103) is a gauge-charge object; per the DECREE_REGISTER rule "using a
charge invokes D2," those rows cite **D2** even though the charge is *imported* from the
Electromagnetism domain rather than re-derived here. (ii) **D5** — the residual fitted O(1)
constants (LJ ε,σ and the 12-exponent, Born-Mayer B,ρ, real-material restitution e, latent-heat
bond-count prefactors, real-fluid critical exponents) are matched to data. **Honesty caveat on the
spatial "3":** several heat-capacity / density-of-states results (EQ-CM-89, EQ-CM-98, EQ-CM-100,
EQ-CM-104) use the integer 3 = number of spatial dimensions. That count is **D1** (a dimension
count), NOT **D3** (which is reserved for the topological winding n_w=3 → generations). These rows
now cite D1 explicitly.

---

## SECTION A — `01-EXPLICIT_DERIVATIONS.md`

### EQ-CM-01 — 6D effective gravitational potential with extra-dim corrections
- **Equation:** V_eff(r) = −(GMm/r)(1 + α₁/r² + α₂/r⁴ + …)
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.6, Step 1)
- **Spine path:** S0→S1→S3→S5→S6→S9
- **Decrees:** D1 (6D manifold + dimensional reduction), D6 (Firmament/zone field content), D0 (ℝ continuum).
- **Trace:** 1=1 → S5 supplies the manifold/tensor structure and S9 the curvature `R` of the 6D Kähler/Riemannian manifold → integrating the interaction action over the compact ξ,η dimensions (D1 fixes there are extra dims; D6 supplies the zone architecture) leaves a 4D Newtonian `1/r` potential plus a power series of curvature corrections that vanish for r ≫ η_B.
- **Constants:** G [SELECTED scale → D4]; α₁ ∼ η_B²/c², α₂ ∼ η_B⁴ [SELECTED scale → D4] (set by the extra-dimension size η_B, a chosen length).
- **Status:** DERIVED-given-decrees (form; corrections schematic).

### EQ-CM-02 — Orbital Lagrangian (polar coordinates)
- **Equation:** L = ½μ_r ṙ² + ½μ_r r²θ̇² + GMm/r
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.6, Step 2)
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D1, D0; D6 (gravity sourced by membrane).
- **Trace:** 1=1 → S6 supplies the action/Lagrangian object (δS=0, borderline) → S5 gives the vector kinematics (ṙ, r²θ̇²) → the potential term GMm/r is EQ-CM-01 to leading order.
- **Constants:** G, M, m, μ_r [SELECTED scale → D4].
- **Status:** DERIVED-as-form (δS=0 borderline), given D1/D6.

### EQ-CM-03 — Angular momentum conservation (central force)
- **Equation:** L_z = μ_r r²θ̇ = const = mℓ
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.6, Step 2)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1 (a plane to rotate in).
- **Trace:** 1=1 → S1 gives the conserved-quantity (books-balance) form → S7 (Noether) ties the rotational symmetry of L to a conserved current; for the central potential that current is L_z.
- **Constants:** none dimensionless beyond the chosen mass/length units [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-04 — Energy conservation (central force)
- **Equation:** E = ½μ_r ṙ² + L_z²/(2μ_r r²) − GMm/r = const
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.6, Step 2)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D0; D6 (gravitational potential content).
- **Trace:** 1=1 → S1 conservation form → S7 (Noether) ties time-translation symmetry to conserved energy; the centrifugal term L_z²/(2μ_r r²) is EQ-CM-03 substituted in.
- **Constants:** G, M, m [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-05 — Binet orbit equation
- **Equation:** d²u/dθ² + u = GM/ℓ²,  u = 1/r
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.6, Step 3); identical in 01-APPLIED_GRAVITY_CALCULATIONS.md §4.2 and 01-NBODY_DYNAMICS.md §1
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → S6 supplies the 2nd-order ODE operator → substituting the conserved L_z (EQ-CM-03) into the energy/EOM (EQ-CM-04) and changing variable to u=1/r yields a linear harmonic-type ODE with constant forcing GM/ℓ².
- **Constants:** G, M, ℓ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-06 — Conic-section orbit (Kepler's First Law)
- **Equation:** r(θ) = a(1−e²)/(1 + e cosθ);  equivalently u(θ) = (GM/ℓ²)(1 + e cos(θ−θ₀))
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.6, Step 3 & Law I)
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → general solution of the linear ODE EQ-CM-05 is a constant plus a cosine (S4 gives the circle/phase, S6 the solution); rewritten in r it is a conic section. Bounded orbits (0≤e<1) are ellipses.
- **Constants:** a, e [DERIVED ratio] for e (set by E, ℓ; dimensionless), with a [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-07 — Eccentricity / semi-major axis from constants of motion
- **Equation:** a = ℓ²/[GM(1−e²)];  e = √(1 + 2Eℓ²/(GMm)²)
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.6, Step 3); e also in 01-NBODY_DYNAMICS.md §1
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → match the conic solution EQ-CM-06 to the conserved E and ℓ; algebra (S2/S3) yields a and e in terms of them.
- **Constants:** G, M, m [SELECTED scale → D4]; e [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-08 — Kepler's Second Law (equal areas)
- **Equation:** dA/dt = ½r²θ̇ = ℓ/2 = const;  A(t) = (ℓ/2)t
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.6, Law II)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1.
- **Trace:** 1=1 → areal velocity ½r²θ̇ equals L_z/(2μ_r), constant by EQ-CM-03; S7/Noether (angular-momentum conservation) is the only physics, so equal areas in equal times.
- **Constants:** ℓ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-09 — Kepler's Third Law (harmonic law)
- **Equation:** T² = (4π²/GM)a³;  T = 2π√(a³/GM)
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.6, Law III); also 01-APPLIED §4.2/§5.3; test_gravity_kinematics.py (KeplerOrbitsTest)
- **Spine path:** S0→S1→S3→S4→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → period = (orbit area πab)/(areal velocity ℓ/2) from EQ-CM-08; substitute b=a√(1−e²) and ℓ=√(GMa(1−e²)) (from EQ-CM-07); π enters via S4 (the circle). Algebra (S2/S3) gives T²∝a³.
- **Constants:** G, M [SELECTED scale → D4]; 4π² [DERIVED ratio] (geometry, via S4).
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-10 — Circular-orbit speed
- **Equation:** v_circ = √(GM/a)  (also v=√(GM/r) in 01-APPLIED §5.3)
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.6, e=0 case)
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D1; D6.
- **Trace:** 1=1 → set e=0 in EQ-CM-09 and use v=2πa/T; algebra gives v=√(GM/a).
- **Constants:** G, M [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-11 — Geodesic deviation (tidal) equation
- **Equation:** D²η^i/Dt² = −R^i_{0j0} η^j
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.7, Step 1)
- **Spine path:** S0→S1→S5→S6→S9
- **Decrees:** D1 (manifold/curvature), D0.
- **Trace:** 1=1 → S9 supplies the Riemann curvature R of the manifold; S6 the covariant 2nd derivative; the relative acceleration of nearby geodesics is the contraction of curvature with separation η.
- **Constants:** none dimensionful (curvature in chosen units, [SELECTED scale → D4]).
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-12 — Weak-field metric (Newtonian gauge)
- **Equation:** ds² = −(1 + 2Φ/c²)c²dt² + (1 − 2Φ/c²)δ_ij dx^i dx^j
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.7, Step 1); also Test 1.8 Step 2
- **Spine path:** S0→S1→S5→S9
- **Decrees:** D1, D0, D6.
- **Trace:** 1=1 → S9 gives the Lorentzian metric; the weak-field perturbation 2Φ/c² is the linearization of the warp-factor structure (D6/D1) about flat space.
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-13 — Riemann–potential relation (weak field)
- **Equation:** R^i_{0j0} = −∂²Φ/∂x^i∂x^j + …
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.7, Step 1)
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D0.
- **Trace:** 1=1 → compute Riemann curvature (S9) of the weak-field metric EQ-CM-12 (S6 derivatives); to leading order it is the Hessian of Φ.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-14 — Tidal tensor definition
- **Equation:** 𝒯_ij = −∂²Φ/∂x^i∂x^j;  for point mass: 𝒯_ij = (GM/r³)(3 x_i x_j/r² − δ_ij)
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.7, Step 2); component form in 01-APPLIED §4.3 (T_ij = 3GM x_i x_j/r⁵ − GM δ_ij/r³)
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → take second derivatives (S6) of Φ=−GM/r; the 3x_ix_j/r² − δ_ij angular structure is pure geometry.
- **Constants:** G, M [SELECTED scale → D4]; the factor 3 [DERIVED ratio] (from ∂²(1/r)).
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-15 — Tidal acceleration
- **Equation:** a⃗_tidal = −𝒯·η⃗;  radial: a_tidal ≈ 2(GM/d³)R (= 2GM/d³ × Δr)
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.7, Steps 3–4); 01-APPLIED §4.3; test_gravity_kinematics.py (TidalForcesTest)
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → contract the tidal tensor EQ-CM-14 with separation η; the radial component (z=R) gives 𝒯_zz=2GM/d³, hence factor-2 differential acceleration across the body.
- **Constants:** G, M, d, R [SELECTED scale → D4]; factor 2 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-16 — Parallel transport of spin (gyroscope)
- **Equation:** DL/Dt = 0,  i.e. dL^i/dt + Γ^i_{jk}(dx^j/dt)L^k = 0
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.8, Step 1); spin form dS^μ/dτ=Γ^μ_{νλ}u^ν S^λ in 01-APPLIED §4.4
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1.
- **Trace:** 1=1 → S9 supplies the connection Γ; parallel transport (zero covariant derivative, S6) of the angular-momentum vector along the worldline is the defining equation.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-17 — Geodetic precession rate
- **Equation:** ω_prec = −(GM)^{3/2}/(c²r^{5/2});  ⃗ω_prec = −(GM/c²r³)⃗v
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.8, Step 3)
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → solve the parallel-transport equation EQ-CM-16 in the weak-field Schwarzschild metric; for a circular orbit v=√(GM/r) the precession rate scales as (GM)^{3/2}/(c²r^{5/2}).
- **Constants:** G, M, c [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-18 — Geodetic precession angle per orbit
- **Equation:** ΔΘ_geodetic = 2πGM/(c²r v_circ)
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.8, Step 3)
- **Spine path:** S0→S4→S5→S6→S9
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → integrate EQ-CM-17 over one orbital period (2π/(v/r)); π from S4 (the circle).
- **Constants:** G, M, c [SELECTED scale → D4]; 2π [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-19 — 6D Noether → energy-momentum conservation
- **Equation:** ∂_μ T^{μν} = 0  (under X^μ → X^μ + ε^μ)
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.10, Step 1); also 01-COMPLETIONS.md §3, §9; this is the domain analog of the schema's worked EQ-FND-01
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1 (a spacetime to translate in).
- **Trace:** 1=1 → S1 gives the additive conservation form a+(−a)=0 → S6 the operator ∂_μ → S7 (Noether) ties translation invariance of the action to the conserved T^{μν}.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-20 — Conservation of total energy and momentum (integrated)
- **Equation:** d/dt ∫ T^{00} d³x = 0 ⇒ E_total const;  d/dt ∫ T^{0i} d³x = 0 ⇒ p⃗_total const
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.10, Step 1)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D6 (Zone A integration region).
- **Trace:** 1=1 → integrate EQ-CM-19 over the Firmament (Zone A, D6) and apply the divergence theorem (S6); the surface term vanishes, giving constant integrated E and p.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-21 — Momentum conservation (collisions)
- **Equation:** m₁v⃗₁ + m₂v⃗₂ = m₁v⃗₁′ + m₂v⃗₂′
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.10, Step 2); 01-INTERMOLECULAR §3.1; 01-MATERIAL §3.1.1; .py collision functions
- **Spine path:** S0→S1→S7
- **Decrees:** D1.
- **Trace:** 1=1 → S1 conservation form; S7 ties translation invariance to momentum, the integrated EQ-CM-20 specialized to two point masses.
- **Constants:** masses [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-22 — Kinetic-energy conservation (elastic collisions)
- **Equation:** ½m₁v₁² + ½m₂v₂² = ½m₁v₁′² + ½m₂v₂′²
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.10, Step 2); 01-INTERMOLECULAR §3.1; 01-MATERIAL §3.1.1
- **Spine path:** S0→S1→S7
- **Decrees:** D1.
- **Trace:** 1=1 → energy conservation (S7, time-translation) restricted to the elastic case where no energy leaks to internal modes.
- **Constants:** masses [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-23 — Head-on elastic collision (stationary target)
- **Equation:** v₁′ = (m₁−m₂)/(m₁+m₂) v₁;  v₂′ = 2m₁/(m₁+m₂) v₁
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.10, Step 3)
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D1.
- **Trace:** 1=1 → solve the linear (EQ-CM-21) + quadratic (EQ-CM-22) system; ratios are pure S2 algebra.
- **Constants:** mass ratios [DERIVED ratio]; masses [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-24 — General 1D elastic collision
- **Equation:** v₁′ = [(m₁−m₂)v₁ + 2m₂v₂]/(m₁+m₂);  v₂′ = [(m₂−m₁)v₂ + 2m₁v₁]/(m₁+m₂)
- **Source:** 01-MATERIAL §3.1.2; test_material_properties.py (elastic_collision_1d)
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D1.
- **Trace:** 1=1 → same linear+quadratic system as EQ-CM-23 but with both targets moving; S2 algebra.
- **Constants:** mass ratios [DERIVED ratio]; masses [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-25 — Perfectly inelastic final velocity
- **Equation:** v⃗_f = (m₁v⃗₁ + m₂v⃗₂)/(m₁+m₂)
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.10, Step 5)
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D1.
- **Trace:** 1=1 → momentum conservation EQ-CM-21 with v₁′=v₂′=v_f; solve (S2).
- **Constants:** masses [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-26 — Inelastic energy loss / reduced mass
- **Equation:** ΔE = ½ [m₁m₂/(m₁+m₂)] v₁² = ½μ_r v₁²;  ΔE/E_i = m₂/(m₁+m₂)
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.10, Step 5)
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D1.
- **Trace:** 1=1 → E_i − E_f using EQ-CM-25; algebra (S2) collapses to the reduced mass μ_r.
- **Constants:** μ_r [SELECTED scale → D4]; fractional loss [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-27 — Rotational kinetic energy / moment of inertia
- **Equation:** T_rot = ½ω²∫ρ r_⊥² d³r = ½Iω²,  with I = ∫ρ(r⃗) r_⊥² d³r
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.11, Step 1); 01-APPLIED §4.5
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D1, D0; D6 (mass distribution on Firmament).
- **Trace:** 1=1 → v=ω×r (S5 vector product) → square and integrate the kinetic energy (S6); the geometric factor r_⊥² defines I.
- **Constants:** none dimensionless; M, R [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-28 — Inertia tensor
- **Equation:** I_ij = ∫ρ(r⃗)(r²δ_ij − r_i r_j) d³r;  T_rot = ½ω_i I_ij ω_j
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.11, Step 2); 01-APPLIED §4.5
- **Spine path:** S0→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → |ω×r|² expanded (S5) gives the r²δ_ij − r_i r_j tensor structure; integrate (S6).
- **Constants:** none dimensionless.
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-29 — Moment of inertia of uniform sphere
- **Equation:** I_sphere = (2/5)MR²
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.11, Step 3); 01-APPLIED §4.5; test_gravity_kinematics.py (RotationalDynamicsTest)
- **Spine path:** S0→S3→S5→S6
- **Decrees:** D1, D0.
- **Trace:** 1=1 → evaluate EQ-CM-27's integral over a uniform ball with the spherical volume element (S6 integration, S4 angular integrals); the 2/5 is pure geometry.
- **Constants:** 2/5 [DERIVED ratio]; M, R [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-30 — Moment of inertia of uniform cylinder
- **Equation:** I_cylinder = ½MR²
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.11, Step 4)
- **Spine path:** S0→S3→S5→S6
- **Decrees:** D1, D0.
- **Trace:** 1=1 → evaluate EQ-CM-27's integral over a uniform cylinder (S6); 1/2 is geometry.
- **Constants:** 1/2 [DERIVED ratio]; M, R [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-31 — Parallel axis theorem
- **Equation:** I = I_cm + Md²
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.11, Step 5)
- **Spine path:** S0→S5→S6
- **Decrees:** D1.
- **Trace:** 1=1 → shift the integration variable in EQ-CM-27 by the center-of-mass offset d; the cross term vanishes (cm definition), leaving I_cm + Md² (S6 algebra).
- **Constants:** M, d [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-32 — Rotational EOM (angular momentum / torque)
- **Equation:** L⃗ = Iω⃗;  dL⃗/dt = τ⃗;  α⃗ = τ⃗/I
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.11, Step 6); 01-COMPLETIONS.md §7.2
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1.
- **Trace:** 1=1 → S7/Noether (rotation symmetry) gives angular-momentum conservation; its rate of change equals the applied torque (S6 derivative).
- **Constants:** I [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-33 — Physical pendulum energy & angular speed
- **Equation:** E = ½Iω² − Mgd cosθ = const;  ω = √[(2gd/I)(cosθ − cosθ₀)]
- **Source:** 01-EXPLICIT_DERIVATIONS.md (Test 1.11, Step 7)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → energy conservation (S7) with rotational KE (EQ-CM-27) and gravitational potential −Mgd cosθ; solve for ω (S2/S3).
- **Constants:** g, d, I [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

---

## SECTION B — `01-COMPLETIONS.md`

### EQ-CM-34 — 6D geodesic equation
- **Equation:** d²X^A/dτ² + Γ^A_{BC}(dX^B/dτ)(dX^C/dτ) = 0
- **Source:** 01-COMPLETIONS.md §1.2; 4D form in 01-APPLIED §4.1
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1 (6D manifold + metric), D0.
- **Trace:** 1=1 → S9 supplies the metric/connection Γ; the geodesic (straightest path, δ∫ds=0) is the S6 variational EOM. Restricting to the Firmament reduces A→μ.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (δS=0 borderline), given D1.

### EQ-CM-35 — Equivalence principle (m_inertial = m_grav)
- **Equation:** m_inertial = m_grav;  a^i = −∂Φ/∂x^i (mass-independent)
- **Source:** 01-COMPLETIONS.md §1.2; 01-APPLIED §4.1/§3.3
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1; D6 (matter confined to Firmament).
- **Trace:** 1=1 → the geodesic EQ-CM-34 depends only on the metric, not the test mass; therefore the same a for all bodies forces m_inertial = m_grav. The only non-grammar input is D1/D6 (a curved Firmament).
- **Constants:** none dimensionful.
- **Status:** DERIVED-given-decrees.

### EQ-CM-36 — Static stress tensor (isotropic pressure)
- **Equation:** σ_ij = P(x)δ_ij
- **Source:** 01-COMPLETIONS.md §2.2
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D6 (Firmament continuum).
- **Trace:** 1=1 → S5 supplies the rank-2 tensor; isotropy of a static fluid forces the diagonal form P δ_ij. Membrane-continuum content is D6.
- **Constants:** P [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-37 — Hydrostatic equilibrium
- **Equation:** ∇P = ρg⃗;  dP/dz = −ρg;  P(z) = P₀ − ρgz
- **Source:** 01-COMPLETIONS.md §2.3
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → force balance (S1) on a fluid element, divide by volume and take the limit (S6); pressure gradient balances gravity. Constant-ρ integration gives the linear profile.
- **Constants:** ρ, g, P₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-38 — Archimedes' buoyant force
- **Equation:** F_buoy = ρ_fluid V_obj g = m_displaced g
- **Source:** 01-COMPLETIONS.md §2.4
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → integrate the hydrostatic pressure EQ-CM-37 over the object surface (S6); the net upward force equals the displaced fluid weight.
- **Constants:** ρ_fluid, V_obj, g [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-39 — Floating fraction
- **Equation:** V_submerged/V_obj = ρ_obj/ρ_fluid
- **Source:** 01-COMPLETIONS.md §2.4
- **Spine path:** S0→S1→S2
- **Decrees:** D1; D6.
- **Trace:** 1=1 → equate buoyant force (EQ-CM-38) to weight; ratio of densities (S2 division).
- **Constants:** density ratio [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-40 — Pascal's law / hydraulic press
- **Equation:** P_new = P_old + ΔP (everywhere);  F₂ = F₁(A₂/A₁)
- **Source:** 01-COMPLETIONS.md §2.5
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D1; D6.
- **Trace:** 1=1 → uniform ΔP preserves the hydrostatic balance EQ-CM-37; force is pressure×area, so the area ratio multiplies the force (S2).
- **Constants:** area ratio A₂/A₁ [DERIVED ratio]; forces [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-41 — Perfect-fluid stress-energy tensor
- **Equation:** T^{μν} = (ρ + P/c²)u^μ u^ν + P g^{μν}
- **Source:** 01-COMPLETIONS.md §3.1
- **Spine path:** S0→S1→S5→S9
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → S5/S9 supply the tensor and metric; a perfect fluid is the most general isotropic T^{μν} built from u^μ and g^{μν}. Membrane-fluid content is D6.
- **Constants:** ρ, P, c [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-42 — Euler equation (inviscid flow)
- **Equation:** ∂v⃗/∂t + (v⃗·∇)v⃗ = −(1/ρ)∇P + g⃗
- **Source:** 01-COMPLETIONS.md §3.1
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → ∂_μ T^{μi}=0 (EQ-CM-19/Noether) for the perfect fluid EQ-CM-41, take the non-relativistic limit (S6 expansion); the convective derivative form drops out.
- **Constants:** ρ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-43 — Continuity equation
- **Equation:** ∂ρ/∂t + ∇·(ρv⃗) = 0;  incompressible: ∇·v⃗ = 0
- **Source:** 01-COMPLETIONS.md §3.2
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1; D6.
- **Trace:** 1=1 → the time component ∂_μ T^{μ0}=0 (EQ-CM-19) is mass conservation; S1 conservation form, S6 divergence.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-44 — Bernoulli's equation
- **Equation:** v²/2 + P/ρ + Φ = const (along streamline);  v²/2 + P/ρ + gz = const
- **Source:** 01-COMPLETIONS.md §3.3
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → for steady irrotational flow, the Euler equation EQ-CM-42 with the vector identity (v·∇)v = ∇(v²/2) − v×(∇×v) (S5) becomes a gradient of a scalar; integrate (S6) ⇒ constant along streamline.
- **Constants:** ρ, g [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-45 — Point-particle Lagrangian (L = T − V)
- **Equation:** L(x,ẋ) = ½mẋ² − V(x);  charged: L = ½mẋ² − qφ + qA·ẋ
- **Source:** 01-COMPLETIONS.md §4.1, §5.3; same as the non-relativistic limit in §5.2
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → non-relativistic limit of the worldline action −∫m dτ (S6, expanding dτ≈dt(1−v²/2c²)) gives ½mv²; minimal coupling to a potential adds −V. The worldline/field content is D6.
- **Constants:** m, q [SELECTED scale → D4].
- **Status:** DERIVED-as-form (δS=0 borderline), given D1/D6.

### EQ-CM-46 — Generalized momentum
- **Equation:** p_i = ∂L/∂ẋ^i = mẋ^i
- **Source:** 01-COMPLETIONS.md §4.2
- **Spine path:** S0→S5→S6
- **Decrees:** D1.
- **Trace:** 1=1 → differentiate the Lagrangian EQ-CM-45 w.r.t. velocity (S6).
- **Constants:** m [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-47 — Hamiltonian via Legendre transform
- **Equation:** H(x,p) = p·ẋ − L = p²/(2m) + V(x)
- **Source:** 01-COMPLETIONS.md §4.3
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → Legendre transform (S6) of EQ-CM-45 using p=mẋ (EQ-CM-46); algebra (S2) gives T+V.
- **Constants:** m [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-48 — Hamilton's equations
- **Equation:** ẋ = ∂H/∂p = p/m;  ṗ = −∂H/∂x = −∇V = F
- **Source:** 01-COMPLETIONS.md §4.4
- **Spine path:** S0→S1→S6
- **Decrees:** D1; D6.
- **Trace:** 1=1 → vary the phase-space action / differentiate H (EQ-CM-47, S6); the two equations recover velocity-momentum and Newton's law.
- **Constants:** m [SELECTED scale → D4].
- **Status:** DERIVED-as-form (δS=0 borderline), given D1.

### EQ-CM-49 — Liouville's theorem
- **Equation:** d/dt[dV/(dp dx)] = 0
- **Source:** 01-COMPLETIONS.md §4.5
- **Spine path:** S0→S5→S6→S7
- **Decrees:** D1.
- **Trace:** 1=1 → Hamiltonian flow (EQ-CM-48) is divergence-free in phase space (∂ẋ/∂x + ∂ṗ/∂p = 0), so the phase-space volume measure is conserved (S6/S7).
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-50 — Euler–Lagrange equation ⇒ Newton's second law
- **Equation:** (d/dt)(∂L/∂ẋ^i) − ∂L/∂x^i = 0 ⇒ mẍ^i = −∂V/∂x^i = F^i
- **Source:** 01-COMPLETIONS.md §5.4
- **Spine path:** S0→S1→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → stationary action δS=0 (S6) for EQ-CM-45 gives the Euler–Lagrange equation; substituting L=T−V yields F=ma.
- **Constants:** m [SELECTED scale → D4].
- **Status:** DERIVED-as-form (δS=0 borderline), given D1/D6.

### EQ-CM-51 — Damped/driven oscillator EOM
- **Equation:** mẍ + γẋ + kx = F_ext(t)
- **Source:** 01-COMPLETIONS.md §6.1
- **Spine path:** S0→S1→S6
- **Decrees:** D1, D0; D6 (damping γ from coupling deficit to Waters).
- **Trace:** 1=1 → Newton's law (EQ-CM-50) for a restoring force −kx plus a dissipative term γẋ; the dissipative term's *existence* is the membrane sustaining-coupling content (D6). S6 supplies the ODE.
- **Constants:** m, k, γ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-52 — Damping coefficient from coupling deficit
- **Equation:** γ = (2ρ_defect V₀/μ₀) × Δκ
- **Source:** 01-COMPLETIONS.md §6.1
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D6 (Ψ-fields, sustaining coupling κ); D0.
- **Trace:** 1=1 → the spine + D6 supply the sustaining-coupling field κ and membrane defect density, but the specific algebraic form γ = 2ρ_defect V₀ Δκ/μ₀ is *asserted* from membrane mechanics, not derived step-by-step in the source.
- **Constants:** ρ_defect, V₀, μ₀, Δκ [SELECTED scale → D4]; the numerical prefactor 2 and the functional form are **not traced**.
- **Status:** UNTRACEABLE (the *value/form* of γ relies on an unstated membrane-mechanics result; only its existence is decree-justified by D6).

### EQ-CM-53 — Damped-oscillator characteristic roots & regimes
- **Equation:** λ = [−γ ± √(γ²−4mk)]/(2m);  ω_d = √(ω₀² − γ²/4m²) = ω₀√(1−ζ²), ω₀=√(k/m), ζ=γ/(2√(mk))
- **Source:** 01-COMPLETIONS.md §6.2
- **Spine path:** S0→S1→S3→S4→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → substitute x=e^{λt} into EQ-CM-51 (F=0); the quadratic (S3) and its complex roots (S4) give the under/critically/over-damped regimes and ω_d.
- **Constants:** ζ [DERIVED ratio]; m, k, γ, ω₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-54 — Driven oscillator steady-state amplitude & phase
- **Equation:** A(ω) = (F₀/m)/√[(ω₀²−ω²)² + (γω/m)²];  tanδ = (γω/m)/(ω₀²−ω²); Q = ω₀/Δω = mω₀/γ
- **Source:** 01-COMPLETIONS.md §6.3
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → particular solution of EQ-CM-51 with F₀cos(ωt); complex-exponential method (S4) gives the resonant amplitude/phase and the Q-factor.
- **Constants:** Q [DERIVED ratio]; F₀, m, k, γ, ω₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-55 — Euler's rigid-body equations
- **Equation:** I₁ω̇₁ − (I₂−I₃)ω₂ω₃ = τ₁ (and cyclic);  L_i = I_ii ω_i
- **Source:** 01-COMPLETIONS.md §7.1–7.3
- **Spine path:** S0→S1→S5→S6→S7
- **Decrees:** D1.
- **Trace:** 1=1 → dL/dt=τ (EQ-CM-32) transformed into the body frame; the rotating-frame term ω×L (S5 cross product) produces the gyroscopic (I₂−I₃)ω₂ω₃ couplings.
- **Constants:** I_i [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-56 — Torque-free angular momentum conservation
- **Equation:** L⃗ = Iω⃗ = const;  I₁ω₁, I₂ω₂, I₃ω₃ each const (when τ=0)
- **Source:** 01-COMPLETIONS.md §7.4
- **Spine path:** S0→S1→S7
- **Decrees:** D1.
- **Trace:** 1=1 → set τ=0 in EQ-CM-55/EQ-CM-32; S7/Noether rotation symmetry gives conserved L.
- **Constants:** I_i [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-57 — N-body Lagrangian and equations of motion
- **Equation:** L = Σᵢ ½mᵢṙᵢ² + Σ_{i<j} Gmᵢmⱼ/|rᵢ−rⱼ|;  mᵢr̈ᵢ = −Σ_{j≠i} (Gmᵢmⱼ/|rᵢ−rⱼ|³)(rᵢ−rⱼ)
- **Source:** 01-COMPLETIONS.md §8.1–8.2; H form in 01-NBODY_DYNAMICS.md (intro)
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D1, D0; D6 (membrane gravity).
- **Trace:** 1=1 → sum of point-particle Lagrangians (EQ-CM-45) with pairwise Newtonian potentials (EQ-CM-01 leading term); Euler–Lagrange (EQ-CM-50) per coordinate gives the inverse-square force sum.
- **Constants:** G, mᵢ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-58 — N-body conservation laws & center of mass
- **Equation:** P_total = Σmᵢṙᵢ = const;  L_total = Σrᵢ×mᵢṙᵢ = const;  E_total = ΣT + ΣV = const;  R_CM = Σmᵢrᵢ/Σmᵢ, Ṙ_CM = P_total/M_total
- **Source:** 01-COMPLETIONS.md §8.3–8.4
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1.
- **Trace:** 1=1 → S7/Noether applied to the N-body action (EQ-CM-57): translation→P, rotation→L, time-translation→E. The CM moves uniformly because P is conserved.
- **Constants:** masses [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-59 — Two-body reduction to one-body
- **Equation:** μr̈ = −(Gm₁m₂/r²)r̂,  μ = m₁m₂/(m₁+m₂),  V(r) = −Gm₁m₂/r
- **Source:** 01-COMPLETIONS.md §8.5; 01-NBODY_DYNAMICS.md §1
- **Spine path:** S0→S1→S2→S5→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → change to CM + relative coordinates in EQ-CM-57 (N=2); the relative motion is a single particle of reduced mass μ in a central potential (S2 algebra).
- **Constants:** G, μ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

### EQ-CM-60 — Work–energy theorem
- **Equation:** W = ∫F·dr = ΔKE;  rotational: W = ∫τ dθ = ½Iω_f² − ½Iω_i²
- **Source:** 01-COMPLETIONS.md §9.1–9.4
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → energy conservation (S7) E=T+V const; differentiate, use F=−∇V (EQ-CM-50), integrate F·dr (S6) to get ΔKE.
- **Constants:** none dimensionless; m, I [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1/D6).

---

## SECTION C — `01-APPLIED_GRAVITY_CALCULATIONS.md` (gravity-specific equations)

### EQ-CM-61 — 6D Einstein–Hilbert action
- **Equation:** S_grav^(6) = (1/16πG₆)∫_{M⁶} d⁶x √(−g₆) R₆ + S_boundary + S_matter
- **Source:** 01-APPLIED §1.1; Appendix A.1; same master action cited across the domain
- **Spine path:** S0→S1→S2→S5→S6→S9
- **Decrees:** D1 (6 dimensions), D0, D6 (zone boundary/field content).
- **Trace:** 1=1 → S9 supplies the curvature scalar R and metric of a 6D manifold; the Einstein–Hilbert action is the simplest diffeomorphism-invariant scalar built from R (S6 integral). D1 fixes "6"; D6 supplies the boundary/matter sectors.
- **Constants:** G₆ [SELECTED scale → D4]; 1/16π [DERIVED ratio] (normalization via S4).
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-62 — 6D metric with warp factors
- **Equation:** ds₆² = e^{2A(ξ,η)}[−c²dt² + a²(t)(dx²+dy²+dz²)] + e^{2B(ξ,η)}(dξ²+dη²)
- **Source:** 01-APPLIED §1.2; Appendix A.2
- **Spine path:** S0→S5→S9
- **Decrees:** D1, D6 (warp/zone profile; "D9-profile"), D0.
- **Trace:** 1=1 → S9 (Kähler/warped manifold) admits a warped-product metric; the specific warp profiles A,B are the architectural choice D6/D1 (a selected profile).
- **Constants:** c [SELECTED scale → D4]; warp profiles [SELECTED → D6].
- **Status:** DERIVED-given-decrees (form; profile selected).

### EQ-CM-63 — 6D Einstein field equations
- **Equation:** G₆^{AB} = R₆^{AB} − ½g₆^{AB}R₆ = 8πG₆ T₆^{AB}
- **Source:** 01-APPLIED §1.3
- **Spine path:** S0→S1→S5→S6→S9
- **Decrees:** D1, D0, D6.
- **Trace:** 1=1 → vary the 6D Einstein–Hilbert action EQ-CM-61 (δS=0, S6) w.r.t. the metric; the Einstein tensor equals the stress-energy source.
- **Constants:** G₆ [SELECTED scale → D4]; 8π [DERIVED ratio].
- **Status:** DERIVED-as-form (δS=0 borderline), given D1/D6.

### EQ-CM-64 — Effective volume / coupling length
- **Equation:** V_eff = ∫₀^{ξ_A}∫₀^{η_B} e^{2A+2B} dξ dη = L_eff²;  L_eff = √(∫ e^{2A+2B} dξ dη)
- **Source:** 01-APPLIED §1.4
- **Spine path:** S0→S3→S6→S9
- **Decrees:** D1, D6 (warp profile), D0.
- **Trace:** 1=1 → integrate the warp factor (EQ-CM-62) over the compact dimensions (S6); defines an effective area L_eff².
- **Constants:** L_eff [SELECTED scale → D4]; warp profile [SELECTED → D6].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-65 — 4D Newton's constant from reduction
- **Equation:** G₄ = G₆/V_eff = G₆/L_eff²;  G = c⁴/(8π σ L_eff)
- **Source:** 01-APPLIED §1.5; §5.1; Appendix A.6
- **Spine path:** S0→S2→S3→S6→S9
- **Decrees:** D1, D6 (Firmament tension σ), D0; D4 (the value of G is anchored to chosen units).
- **Trace:** 1=1 → dimensional reduction divides G₆ by the compact volume (EQ-CM-64); rewriting via membrane tension σ (D6) gives G = c⁴/(8πσL_eff). The numerical value 6.674×10⁻¹¹ depends on the chosen σ and L_eff.
- **Constants:** G, G₆, σ, L_eff, c [SELECTED scale → D4]; 8π [DERIVED ratio]. (σ=6.0×10⁹⁸, L_eff=8.03×10⁻⁵⁸ m are chosen scales → D4.)
- **Status:** DERIVED-given-decrees (value tied to D4).

### EQ-CM-66 — Induced metric on Firmament
- **Equation:** γ_μν = (∂X^A/∂x^μ)(∂X^B/∂x^ν) g_AB = e^{2A(ξ₀,η₀)} g_μν^(4)
- **Source:** 01-APPLIED §2.1
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D6.
- **Trace:** 1=1 → pull back the 6D metric EQ-CM-62 to the 4D embedded hypersurface (S6 chain rule); the warp factor at (ξ₀,η₀) rescales the 4D metric.
- **Constants:** warp factor [SELECTED → D6].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-67 — Extrinsic curvature & Gauss–Codazzi
- **Equation:** K_μν^(i) = −½ ∂g_μν^(4)/∂x^{i,⊥};  R_μν^(4) = K^{(1)}·K^{(1)} + K^{(2)}·K^{(2)} − K^{(1)}_μν K^{(1)} − K^{(2)}_μν K^{(2)} + R_μν^bulk
- **Source:** 01-APPLIED §2.2
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D6 (codimension-2 brane), D0.
- **Trace:** 1=1 → S9 differential geometry of an embedded surface; the Gauss–Codazzi identity relates intrinsic curvature to extrinsic curvatures of the two normal directions (D6: two Waters zones).
- **Constants:** none dimensionful.
- **Status:** DERIVED-given-decrees (standard geometry; brane content D6).

### EQ-CM-68 — Projected 4D Einstein equations (with Λ_eff)
- **Equation:** R_μν − ½g_μν R + Λ_eff g_μν = 8πG T_μν;  G_μν + Λ_eff g_μν = 8πG T_μν
- **Source:** 01-APPLIED §2.4; Appendix A.4
- **Spine path:** S0→S1→S5→S6→S9
- **Decrees:** D1, D0, D6 (Λ_eff from Waters Above).
- **Trace:** 1=1 → project the 6D field equations EQ-CM-63 onto the Firmament via Gauss–Codazzi (EQ-CM-67); the bulk/extrinsic contributions appear as an effective cosmological term Λ_eff (D6 dark-energy content).
- **Constants:** G, Λ_eff [SELECTED scale → D4]; 8π [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-69 — Linearized Ricci tensor (weak field)
- **Equation:** g_μν = η_μν + h_μν, |h_μν|≪1;  R_μν ≈ −½□h_μν + …
- **Source:** 01-APPLIED §3.1
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D0.
- **Trace:** 1=1 → expand the metric about flat space (S5) and linearize the curvature (S6); □ is the S6 d'Alembertian.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-70 — Poisson equation for gravity
- **Equation:** ∇²h₀₀ = 16πGρ;  ∇²Φ = 4πGρ,  Φ = −GM/r, h₀₀ = 2Φ/c²
- **Source:** 01-APPLIED §3.2; Appendix A.7
- **Spine path:** S0→S1→S5→S6→S9
- **Decrees:** D1, D0, D6.
- **Trace:** 1=1 → non-relativistic limit of the linearized field equations EQ-CM-68/EQ-CM-69 (slow sources); the 00-component reduces to Poisson's equation for the potential.
- **Constants:** G [SELECTED scale → D4]; 4π [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-71 — Newtonian gravitational acceleration
- **Equation:** g⃗ = −∇Φ = −(GM/r²)r̂;  a = GM/r² (mass-independent)
- **Source:** 01-APPLIED §3.3; §4.1; test_gravity_kinematics.py (EquivalencePrincipleTest, a=GM/R²)
- **Spine path:** S0→S5→S6
- **Decrees:** D1; D6.
- **Trace:** 1=1 → gradient (S6) of Φ=−GM/r from EQ-CM-70; the inverse-square field follows. Mass independence is the equivalence principle (EQ-CM-35).
- **Constants:** G, M [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-CM-72 — Schwarzschild metric & radius
- **Equation:** ds² = −(1−r_s/r)c²dt² + dr²/(1−r_s/r) + r²(dθ² + sin²θ dφ²);  r_s = 2GM/c²
- **Source:** 01-APPLIED §4.2; §5.4; Appendix A.5
- **Spine path:** S0→S4→S5→S6→S9
- **Decrees:** D1, D0, D6.
- **Trace:** 1=1 → solve the vacuum projected Einstein equations EQ-CM-68 for a static spherically symmetric mass (S9 + S6); the integration constant is r_s=2GM/c². sin²θ from S4.
- **Constants:** G, M, c [SELECTED scale → D4]; factor 2 in r_s [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-73 — de Sitter (geodetic) precession (GR form)
- **Equation:** ω_geo = (3/2)(GM/c²r) ω_orbital,  ω_orbital = √(GM/r³)
- **Source:** 01-APPLIED §4.4; test_gravity_kinematics.py (GyroscopePrecessionTest)
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D0, D6.
- **Trace:** 1=1 → parallel-transport the spin (EQ-CM-16) around a circular Schwarzschild orbit (EQ-CM-72); the curvature contraction yields the 3/2 factor times GM/c²r times orbital frequency.
- **Constants:** G, M, c [SELECTED scale → D4]; 3/2 [DERIVED ratio] (geometry of the Schwarzschild metric).
- **Status:** DERIVED-given-decrees.

### EQ-CM-74 — Orbital / escape velocity, Schwarzschild radius (dimensional summary)
- **Equation:** v = √(GM/r);  v_esc = √(2GM/r);  Φ = GM/r;  r_s = 2GM/c²
- **Source:** 01-APPLIED §5.2–5.4
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D1; D6.
- **Trace:** 1=1 → energy balance (½v²=GM/r for circular; ½v_esc²=GM/r for escape) from the Newtonian potential EQ-CM-70/71; algebra (S3).
- **Constants:** G, M, c [SELECTED scale → D4]; factors 2 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-CM-75 — Lense–Thirring frame dragging
- **Equation:** g_{tφ} ∝ J/r²;  ω_drag = 2GJ/(c²r³)
- **Source:** 01-APPLIED §6.1; .py docstring
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D1, D0, D6.
- **Trace:** 1=1 → a rotating source gives an off-diagonal metric component (S9); the induced precession of a local inertial frame is ω_drag ∝ J/r³.
- **Constants:** G, J, c [SELECTED scale → D4]; factor 2 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-76 — Gravitational time dilation
- **Equation:** g_tt = −e^{2A}c² ≈ −(1−2Φ/c²)c²;  dt_proper/dt_coord = √(1−2Φ/c²) ≈ 1 − Φ/c²
- **Source:** 01-APPLIED §6.2
- **Spine path:** S0→S3→S5→S9
- **Decrees:** D1, D0, D6.
- **Trace:** 1=1 → the time-time warp factor (EQ-CM-62/72) sets the proper-time rate; expand √ to first order (S3) ⇒ fractional slowdown Φ/c².
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

---

## SECTION D — `01-NBODY_DYNAMICS.md` (chaos, integrators, definitional constants)

### EQ-CM-77 — Lyapunov divergence (chaos)
- **Equation:** δ(t) ≈ δ₀ e^{λt};  t_L = 1/λ
- **Source:** 01-NBODY_DYNAMICS.md §1 (Three-body); Appendix
- **Spine path:** S0→S5→S6
- **Decrees:** D1; D6.
- **Trace:** 1=1 → linearize the N-body flow (EQ-CM-57) about a trajectory (S6); the tangent-space growth rate λ (S5 eigenvalue) gives exponential separation. λ>0 ⇒ chaos. λ is a property of the system, measured numerically.
- **Constants:** λ [SELECTED scale → D4] (inverse time; the value ~0.086–0.1 Myr⁻¹ is numerically estimated, effectively [FIT → D5] to simulation).
- **Status:** DERIVED-as-form (given D1).

### EQ-CM-78 — Verlet / leapfrog symplectic integrator
- **Equation:** r(t+Δt) = 2r(t) − r(t−Δt) + a(t)Δt²;  velocity form: v(t+Δt/2)=v(t−Δt/2)+a(t)Δt, r(t+Δt)=r(t)+v(t+Δt/2)Δt;  composition e^{Δt(A+B)} ≈ Π e^{c_iΔtA}e^{d_iΔtB}
- **Source:** 01-NBODY_DYNAMICS.md §2
- **Spine path:** S0→S3→S6
- **Decrees:** none beyond D0 (discretization of the ℝ-time ODE).
- **Trace:** 1=1 → Taylor-expand the trajectory (S6) and cancel odd terms to second order; the scheme is symplectic because it composes exact Hamiltonian sub-flows (EQ-CM-48). This is numerical method, not new physics.
- **Constants:** c_i, d_i [DERIVED ratio] (chosen to cancel error orders).
- **Status:** DERIVED-as-form (given D0).

### EQ-CM-79 — Boltzmann constant (SI 2019 definition)
- **Equation:** k_B = 1.380649×10⁻²³ J/K (exact)
- **Source:** 01-NBODY_DYNAMICS.md §3; consistency table
- **Spine path:** S0 (unit convention only)
- **Decrees:** D4 (scale/unit anchor).
- **Trace:** 1=1 → k_B is not derived; it is a *defined* unit conversion between energy and temperature. Pure D4 (choice of the "1" for thermal energy scale).
- **Constants:** k_B [SELECTED scale → D4] (exact by SI definition).
- **Status:** DERIVED-given-decrees (definitional, D4).

### EQ-CM-80 — Equipartition & Planck-mode average energy
- **Equation:** ⟨E_mode⟩ = k_B T (one quadratic DOF);  ⟨E(ω,T)⟩ = ℏω(½ + 1/(e^{ℏω/k_BT}−1));  T_cross = ℏω/k_B
- **Source:** 01-NBODY_DYNAMICS.md §3; "Extended Discussion"
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D4 (k_B, ℏ scales); D0.
- **Trace:** 1=1 → average energy of a thermal oscillator from the Bose/partition sum (S6); high-T limit gives k_B T (classical), low-T gives ℏω/2. The crossover temperature is the ratio of the two scales.
- **Constants:** k_B, ℏ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (form; scales D4).

### EQ-CM-81 — Avogadro constant (SI 2019 definition)
- **Equation:** N_A = 6.02214076×10²³ mol⁻¹ (exact)
- **Source:** 01-NBODY_DYNAMICS.md §4; consistency table
- **Spine path:** S0→S1 (counting → ℕ)
- **Decrees:** D4 (unit anchor for "mole").
- **Trace:** 1=1 → N_A is a *defined* counting unit (entities per mole). S1 supplies counting (ℕ); D4 fixes the convention. Not a physical derivation.
- **Constants:** N_A [count] but as a *unit definition* it is [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (definitional, D4).

### EQ-CM-82 — Gas constant and ideal gas law
- **Equation:** R = k_B N_A = 8.314462618 J/(mol·K);  M_molar = m_atomic N_A;  PV = nRT = N k_B T
- **Source:** 01-NBODY_DYNAMICS.md §3–§4; consistency table
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4 (k_B, N_A scales); D0.
- **Trace:** 1=1 → R is the product of the two defined constants (S2); the ideal gas law PV=Nk_BT follows from the equipartition/partition function of N free particles (S6). Macroscopic↔microscopic bridge via N_A.
- **Constants:** R, k_B, N_A [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (definitional relation, D4).

### EQ-CM-83 — Other SI-2019 defining constants (c, h, e)
- **Equation:** c = 299792458 m/s; h = 6.62607015×10⁻³⁴ J·s; e = 1.602176634×10⁻¹⁹ C; α = e²/(4πε₀ℏc); Δx Δp ≥ ℏ/2
- **Source:** 01-NBODY_DYNAMICS.md consistency table
- **Spine path:** S0 (units); α uses S2/S4
- **Decrees:** D4 (all dimensionful values); for α additionally D2/D6 noted elsewhere (charge/gauge — out of this domain's scope).
- **Trace:** 1=1 → c, h, e are *defined* SI scales (pure D4). The fine-structure ratio α is dimensionless (S2 ratio) but its *value* (≈1/137.036) is an electromagnetic/constants-domain result; it is NOT geometry-forced here, so it must not be tagged [DERIVED ratio] in this domain.
- **Constants:** c, h, e [SELECTED scale → D4]; α — dimensionless (S2 ratio) but its value is out-of-domain and in-framework still partly fitted; tag deferred to the EM/Fundamental-Constants ledger (there it is closer to [FIT → D5] pending the two-loop precision item). NOT claimed [DERIVED ratio] here.
- **Status:** DERIVED-given-decrees (definitional, D4; α value out-of-domain — see EM/Constants ledger).

---

## SECTION E — `01-INTERMOLECULAR_PHASE_TRANSITIONS.md`

### EQ-CM-84 — Van der Waals attraction & C₆ coefficient
- **Equation:** V_vdW(r) = −C₆/r⁶;  C₆ = (3/4)α₁α₂ I₁I₂/(I₁+I₂)
- **Source:** 01-INTERMOLECULAR §1.2; KK form V_vdW^KK ∼ Σ g²e^{−2Δm·r}/r⁶ in §1.4
- **Spine path:** S0→S2→S3→S5→S6
- **Decrees:** D1, D0; D6 (KK/Firmament mode exchange).
- **Trace:** 1=1 → second-order perturbation of two coupled fluctuating dipoles (S6) gives the −1/r⁶ tail; the 3/4 is a geometric average of two oscillators. The Firmament/KK provenance is D6.
- **Constants:** C₆, α, I [SELECTED scale → D4]; 3/4 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form).

### EQ-CM-85 — Lennard-Jones potential & force
- **Equation:** V_LJ(r) = 4ε[(σ/r)¹² − (σ/r)⁶];  r_min = 2^{1/6}σ;  F = −4ε[−12σ¹²/r¹³ + 6σ⁶/r⁷]
- **Source:** 01-INTERMOLECULAR §2.1, §2.3, §3.3
- **Spine path:** S0→S2→S3→S6
- **Decrees:** D1, D0; D6.
- **Trace:** 1=1 → combine the derived −1/r⁶ attraction (EQ-CM-84) with an empirical 1/r¹² repulsion (Pauli overlap); differentiate (S6) for the force; r_min from setting F=0 (S3).
- **Constants:** ε, σ [SELECTED scale → D4] / [FIT → D5] (ε, σ fitted to vapor-pressure data, e.g. Ar ε/k_B=119.8 K); the 12 exponent is an empirical approximation [FIT → D5].
- **Status:** PARTIAL (6-tail derived; 12-repulsion and parameters fitted → D5).

### EQ-CM-86 — Coefficient of restitution & hard-sphere limit
- **Equation:** e = |v₂′−v₁′|/|v₁−v₂|;  hard-sphere V_HS = ∞ (r<σ), 0 (r≥σ) ⇒ e=1;  KE_final = e² KE_initial
- **Source:** 01-INTERMOLECULAR §3.2–§3.4; 01-MATERIAL §3.2.1
- **Spine path:** S0→S1→S2
- **Decrees:** D1; D6 (phonon/KK dissipation channels for e<1).
- **Trace:** 1=1 → e is a defined velocity ratio; the elastic limit (e=1) follows from EQ-CM-22/24; energy loss to internal modes (D6) gives e<1.
- **Constants:** e [DERIVED ratio] (e=1 limit) / [FIT → D5] (real-material e values).
- **Status:** PARTIAL (definition + elastic limit derived; real e values fitted).

### EQ-CM-87 — Equipartition average energy
- **Equation:** Z = Σ_n e^{−E_n/k_BT};  ⟨E⟩ = −∂lnZ/∂β = ½k_B T per quadratic DOF
- **Source:** 01-INTERMOLECULAR §4.1; 01-MATERIAL §1.1 (and §4 partition function in INTERMOLECULAR)
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D4 (k_B scale); D0.
- **Trace:** 1=1 → the canonical partition function (S6 integral over a quadratic Hamiltonian) gives a Gaussian; ⟨E⟩=½k_B T per quadratic term by the standard ∂lnZ/∂β.
- **Constants:** k_B [SELECTED scale → D4]; ½ [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form; scale D4).

### EQ-CM-88 — Heat capacities by degrees of freedom
- **Equation:** U = (3/2)Nk_BT, C_V=(3/2)Nk_B (monatomic);  C_V=(5/2)R (diatomic, rot);  (7/2)R (diatomic, vib);  vibrational threshold Θ_vib = ℏω/k_B
- **Source:** 01-INTERMOLECULAR §4.2–§4.4; 01-MATERIAL §1.1
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D4 (k_B); D0.
- **Trace:** 1=1 → count quadratic DOF (S1 counting) and apply equipartition EQ-CM-87; differentiate U w.r.t. T (S6) for C_V. The integer DOF counts (3, 5, 7 halves) are geometric/combinatorial.
- **Constants:** k_B, R [SELECTED scale → D4]; the DOF factors 3/2, 5/2, 7/2 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form; scale D4).

### EQ-CM-89 — Dulong–Petit law
- **Equation:** ⟨E_atom⟩ = 3k_B T;  C_V,molar = 3R = 24.9 J/(mol·K)
- **Source:** 01-INTERMOLECULAR §4.5; 01-MATERIAL §1.1; test_material_properties.py (DULONG_PETIT=3R)
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D1 (the factor 3 is the spatial-dimension count), D4 (k_B); D0.
- **Trace:** 1=1 → 3N atoms × 2 quadratic terms each × ½k_B T = 3Nk_B T (EQ-CM-87/88); C_V=3R. The 3 is the spatial dimension count, which is **D1** (a dimension count), NOT D3 (D3 is the winding n_w=3 → generations).
- **Constants:** R [SELECTED scale → D4]; 3 [DERIVED ratio] (spatial-dimension count from D1, not a D3 winding count).
- **Status:** DERIVED-given-decrees (form; scale D4).

### EQ-CM-90 — Helmholtz/Gibbs thermodynamic functions
- **Equation:** F = −k_BT lnZ;  U = −∂lnZ/∂β;  S = k_B lnZ + U/T;  P = −(∂F/∂V)_T;  G = F + PV
- **Source:** 01-INTERMOLECULAR §5.2
- **Spine path:** S0→S1→S6
- **Decrees:** D4 (k_B); D0.
- **Trace:** 1=1 → standard thermodynamic potentials as derivatives of lnZ (S6) from the partition function EQ-CM-87.
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (form; scale D4).

### EQ-CM-91 — Phase-equilibrium condition & Clausius–Clapeyron
- **Equation:** μ_α(T,P) = μ_β(T,P), G_α=G_β;  dP/dT = ΔS/ΔV = L/(TΔV);  L = TΔS
- **Source:** 01-INTERMOLECULAR §5.3, §6.1; §9.2
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4; D0.
- **Trace:** 1=1 → equal chemical potentials at coexistence; take the total differential along the boundary (S6), solve for dP/dT (S2); use L=TΔS.
- **Constants:** L, ΔV [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D0/D4).

### EQ-CM-92 — Latent-heat / binding estimates
- **Equation:** L_fusion ∼ ε × (broken bonds);  L_vaporization ∼ 10ε
- **Source:** 01-INTERMOLECULAR §6.2–§6.3
- **Spine path:** S0→S1→S2
- **Decrees:** D4 (ε scale); D6 (intermolecular binding content).
- **Trace:** 1=1 → latent heat estimated as bond energy ε times a bond-count factor; the numeric prefactors (0.1, 10) are heuristic fits to data (water L_fus=334 kJ/kg, L_vap=2260 kJ/kg).
- **Constants:** ε [SELECTED scale → D4]; bond-count prefactors [FIT → D5].
- **Status:** PARTIAL (scaling form only; prefactors fitted → D5).

### EQ-CM-93 — Van der Waals equation of state
- **Equation:** (P + aN²/V²)(V − Nb) = NkT;  a ≈ 4εσ³, b ≈ 2πσ³/3
- **Source:** 01-INTERMOLECULAR §7.1
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4 (a, b scales); D6; D0.
- **Trace:** 1=1 → modify the ideal gas law (EQ-CM-82) with finite-volume (b) and attraction (a) corrections; a,b mapped to the LJ parameters (EQ-CM-85).
- **Constants:** a, b [SELECTED scale → D4] / [FIT → D5] (a,b from data).
- **Status:** DERIVED-given-decrees (form; parameters fitted).

### EQ-CM-94 — Van der Waals critical point
- **Equation:** (∂P/∂V)_Tc=0, (∂²P/∂V²)_Tc=0 ⇒ V_c=3Nb, T_c=8a/(27kb), P_c=a/(27b²)
- **Source:** 01-INTERMOLECULAR §7.2–§7.3
- **Spine path:** S0→S2→S3→S6
- **Decrees:** D4; D0.
- **Trace:** 1=1 → set the first and second V-derivatives of the vdW pressure (EQ-CM-93) to zero (S6) and solve the simultaneous equations (S3); the 3, 8/27, 1/27 are pure algebra.
- **Constants:** a, b [SELECTED scale → D4]; 3, 8/27, 1/27 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D0/D4).

### EQ-CM-95 — Mean-field critical exponents & scaling
- **Equation:** ρ_l−ρ_g ∼ (−τ)^β, β=½;  C_P ∼ |τ|^{−α}, α=0;  χ_T ∼ |τ|^{−γ}, γ=1;  δ∼ρ^δ, δ=3;  f = |T−T_c|^{2−α}F(…)
- **Source:** 01-INTERMOLECULAR §8.1–§8.2
- **Spine path:** S0→S2→S3→S6
- **Decrees:** D4; D0.
- **Trace:** 1=1 → expand the vdW EOS (EQ-CM-93/94) near the critical point (S6 Taylor); mean-field exponents (½,0,1,3) drop out of the leading singular powers.
- **Constants:** β,α,γ,δ [DERIVED ratio] (mean-field; real-fluid values differ — fit/RG correction noted).
- **Status:** DERIVED-as-form (mean-field; real exponents UNTRACEABLE at this level, acknowledged in source).

### EQ-CM-96 — Gibbs phase rule
- **Equation:** F = C − P + 2;  single component: F = 3 − P
- **Source:** 01-INTERMOLECULAR §9.1
- **Spine path:** S0→S1
- **Decrees:** none beyond D0.
- **Trace:** 1=1 → counting argument (S1): variables minus constraints from equal chemical potentials; +2 for T,P.
- **Constants:** integers C, P, 2 [DERIVED ratio] — these are pure S1 counting integers (variables/constraints/the two intensive fields), NOT D3 winding counts; D3 is reserved for the topological n_w=3 generation count.
- **Status:** DERIVED-as-form.

### EQ-CM-97 — Phase-boundary curves (Antoine / solid-liquid)
- **Equation:** P(T) = P_ref exp[−(L_vap/R)(1/T − 1/T_ref)];  P(T) ≈ P₀ + L_fusion/(T_m ΔV_sl)(T−T_m)
- **Source:** 01-INTERMOLECULAR §9.2
- **Spine path:** S0→S2→S6
- **Decrees:** D4; D0.
- **Trace:** 1=1 → integrate Clausius–Clapeyron EQ-CM-91 with ΔV≈V_gas=RT/P for the boiling curve (S6); linearize for the steep solid-liquid curve.
- **Constants:** L, R, T_ref [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D0/D4).

---

## SECTION F — `01-MATERIAL_PROPERTIES.md` (distinct equations)

### EQ-CM-98 — Debye internal energy & specific heat
- **Equation:** ⟨E(ω)⟩ = ℏω/(e^{ℏω/k_BT}−1);  g(ω)=9N_A ω²/ω_D³;  U = 9N_Ak_BT ∫₀^{Θ_D/T} x³/(e^x−1) dx;  C_V = 9R·D(Θ_D/T);  ω_D = k_BΘ_D/ℏ
- **Source:** 01-MATERIAL §1.2.1–1.2.2; test_material_properties.py (specific_heat_debye_per_mole)
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D1 (the g(ω)∝ω² Debye DOS and the prefactor 9=3×3 use the 3 spatial dimensions), D4 (k_B, ℏ, Θ_D scales); D0.
- **Trace:** 1=1 → Bose-Einstein mode energy (S6) integrated over the Debye density of states g(ω)∝ω² (the ω² power and the prefactor 9N_A/ω_D³ are specific to **3** spatial dimensions, **D1**; linear dispersion ω=v_s|k|, S5); the dimensionless variable x=ℏω/k_BT recasts U as the Debye integral.
- **Constants:** k_B, ℏ, Θ_D [SELECTED scale → D4]; 9 and the density-of-states normalization [DERIVED ratio] (3D geometry, from D1).
- **Status:** DERIVED-given-decrees (form; scales D4).

### EQ-CM-99 — Debye function & limits
- **Equation:** D(y) = (1/y³)∫₀^y x⁴e^x/(e^x−1)² dx;  D→⅓·(norm) ⇒ C_V→3R (T→∞);  C_V → (12π⁴/5)R(T/Θ_D)³ (T→0)
- **Source:** 01-MATERIAL §1.2.2–1.2.3; test_material_properties.py (debye_integral)
- **Spine path:** S0→S3→S4→S6
- **Decrees:** D4; D0.
- **Trace:** 1=1 → differentiate U (EQ-CM-98) w.r.t. T (S6) to define D(y); the high-T limit recovers Dulong-Petit (EQ-CM-89), the low-T limit gives the T³ law (the π⁴/15 from the S4-related ∫x³/(e^x−1)dx=π⁴/15).
- **Constants:** 12π⁴/5, π⁴/15 [DERIVED ratio]; R, Θ_D [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (form; scales D4).

### EQ-CM-100 — Einstein model specific heat
- **Equation:** ⟨E⟩ = ℏω_E/(e^{ℏω_E/k_BT}−1) + ℏω_E/2;  C_V = 3R(Θ_E/T)² e^{Θ_E/T}/(e^{Θ_E/T}−1)²,  Θ_E=ℏω_E/k_B
- **Source:** 01-MATERIAL §1.3.1; test_material_properties.py (specific_heat_einstein_per_mole)
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D1 (the 3N DOF uses the spatial-dimension count 3), D4 (k_B, ℏ, Θ_E); D0.
- **Trace:** 1=1 → single-frequency oscillator average energy (S6) times 3N DOF (the 3 is the spatial-dimension count, **D1**); differentiate w.r.t. T for C_V. High-T → 3R, low-T → exponential suppression.
- **Constants:** k_B, ℏ, Θ_E [SELECTED scale → D4]; 3 [DERIVED ratio] (spatial-dimension count from D1).
- **Status:** DERIVED-given-decrees (form; scales D4).

### EQ-CM-101 — Harmonic interatomic spring constant
- **Equation:** U(r) = U(r₀) + ½k_s(r−r₀)² + …;  k_s = ∂²U/∂r²|_{r₀}
- **Source:** 01-MATERIAL §2.1.1
- **Spine path:** S0→S3→S6
- **Decrees:** D4; D0; D6 (interatomic potential content).
- **Trace:** 1=1 → Taylor-expand any interatomic potential about equilibrium (S6); the second derivative is the effective spring constant.
- **Constants:** k_s [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D0).

### EQ-CM-102 — Coulomb + Born-Mayer potential & spring constant
- **Equation:** U_C = −Z₁Z₂e²/(4πε₀r);  U_R = B e^{−r/ρ};  k_s = 2Z₁Z₂e²/(4πε₀r₀³) + (B/ρ²)e^{−r₀/ρ}
- **Source:** 01-MATERIAL §2.1.2; test_material_properties.py (youngs_modulus_ionic_crystal)
- **Spine path:** S0→S2→S3→S6
- **Decrees:** D2 (the electric charge e / Coulomb coupling e²/4πε₀ is a gauge-charge object — per the DECREE_REGISTER rule "using a charge invokes D2"; here it is imported from the Electromagnetism domain, not re-derived), D4 (e, ε₀, B, ρ scales), D5 (B, ρ fitted); D6 (lattice/Firmament content); D0.
- **Trace:** 1=1 → Coulomb attraction (EM domain; its very form rests on **D2**, the charge/gauge content, cited not re-derived here) plus empirical Born-Mayer repulsion; second derivative at equilibrium (S6) gives k_s.
- **Constants:** e, ε₀ [SELECTED scale → D4] (and the charge content is D2); B, ρ [FIT → D5] (empirical).
- **Status:** PARTIAL (Coulomb input from EM domain; B,ρ fitted → D5).

### EQ-CM-103 — Young's modulus from Coulomb scaling
- **Equation:** σ = Eε;  E ∼ (1/V)∂²U_lattice/∂ε²;  E = (e²/4πε₀)·(1/a⁴),  a = n^{−1/3};  E ≈ k_s/a
- **Source:** 01-MATERIAL §2.2; test_material_properties.py (youngs_modulus_from_interatomic_force)
- **Spine path:** S0→S2→S3→S6
- **Decrees:** D2 (built on the Coulomb/charge coupling e²/4πε₀ via EQ-CM-102 — charge invokes D2), D4, D5 (scaling calibrated/limited by data); D6 (lattice content); D0.
- **Trace:** 1=1 → stress=modulus×strain (definition); E from the curvature of the lattice energy density (EQ-CM-101/102) ∼ Coulomb energy / a³, whose charge content is **D2**. Order-of-magnitude scaling only.
- **Constants:** e, ε₀, a [SELECTED scale → D4] (charge content D2); numeric agreement (Cu 0.2%, Fe 57%) shows it is a [FIT → D5]-level estimate, not exact.
- **Status:** PARTIAL (scaling form; quantitative accuracy limited, band-structure not captured).

### EQ-CM-104 — Debye temperature ↔ elastic modulus
- **Equation:** Θ_D = (ℏ/k_B)v_s(3π²n)^{1/3};  v_s = √(E/ρ);  E ∼ ρ(k_BΘ_D/(ℏn^{1/3}))²
- **Source:** 01-MATERIAL §2.3
- **Spine path:** S0→S3→S4→S5→S6
- **Decrees:** D1 (the (3π²n)^{1/3} cutoff is the 3D k-space mode count — uses the spatial-dimension count 3), D4; D0.
- **Trace:** 1=1 → Debye cutoff from the phonon density of states in 3D (S5, with 3π²n from the spherical k-space count, S4; the "3D" mode-counting is the spatial-dimension input **D1**); sound speed v_s=√(E/ρ) links Θ_D and E.
- **Constants:** ℏ, k_B [SELECTED scale → D4]; 3π² [DERIVED ratio] (3D k-space geometry, from D1).
- **Status:** DERIVED-given-decrees (form; scales D4).

### EQ-CM-105 — General inelastic collision with restitution
- **Equation:** v₁′ = [(m₁−em₂)v₁ + m₂(1+e)v₂]/(m₁+m₂);  v₂′ = [m₁(1+e)v₁ + (m₂−em₁)v₂]/(m₁+m₂);  ΔKE = ½[m₁m₂/(m₁+m₂)](1−e²)(v₁−v₂)²
- **Source:** 01-MATERIAL §3.2.2–§3.2.3; test_material_properties.py (inelastic_collision_1d)
- **Spine path:** S0→S1→S2
- **Decrees:** D1; D6 (dissipation gives e<1).
- **Trace:** 1=1 → momentum conservation (EQ-CM-21) + restitution relation v₁′−v₂′=−e(v₁−v₂); solve the 2×2 linear system (S2); energy loss ∝(1−e²).
- **Constants:** e [DERIVED ratio for e=1, otherwise FIT → D5]; masses [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1; e value fitted for real materials).

---

## Coverage audit / honesty notes

- **Recurring backbone.** EQ-CM-19 (∂_μT^{μν}=0) is the domain's master conservation law and the
  parent of the Euler equation, continuity, work-energy, and all collision/N-body conservation laws.
  It is the direct analog of the schema's worked example EQ-FND-01 (S0→S1→S6→S7, D1).
- **Where D6 carries real weight.** The fluid, oscillator-damping, intermolecular, and gravity-source
  equations cite **D6** because their *physical content* (Firmament continuum, sustaining coupling κ,
  Waters zones, membrane tension σ) is architectural, not grammatical.
- **Where D4 dominates.** Every dimensionful constant (G, σ, c, k_B, ℏ, N_A, e, ε, ε₀, Θ_D…) is
  "1 in chosen units" → **D4**. The SI-2019 *defining* constants (k_B, N_A, c, h, e) are pure D4
  unit conventions, not physical derivations.
- **Where D2 sneaks in (now cited).** The only place this nominally-mechanical domain touches a
  gauge charge is the ionic-crystal elasticity chain (EQ-CM-102 Coulomb+Born-Mayer spring constant,
  EQ-CM-103 Young's modulus). The Coulomb coupling e²/4πε₀ carries the electric charge, so per the
  DECREE_REGISTER rule "using a charge invokes D2," both rows now cite **D2** (imported from the EM
  domain, not re-derived here). Earlier these rows hid the charge behind D6 alone — corrected.
- **The spatial "3" is D1, never D3.** EQ-CM-89, EQ-CM-98, EQ-CM-100, EQ-CM-104 use 3 = spatial
  dimensions in their DOF / density-of-states factors. Those rows now cite **D1** and tag the 3 as
  a [DERIVED ratio] from the dimension count — explicitly NOT a D3 winding count. The old
  "[count → D3-like]" hedges on EQ-CM-89 and EQ-CM-96 are removed.
- **Genuine fits (D5).** The LJ 12-repulsion exponent and ε,σ; Born-Mayer B,ρ; real-material
  restitution e; latent-heat bond-count prefactors; and real-fluid critical exponents are
  **matched to data**, flagged [FIT → D5].
- **The one UNTRACEABLE item.** EQ-CM-52 — the *form/value* of the membrane damping coefficient
  γ = 2ρ_defect V₀ Δκ/μ₀ — is asserted from membrane mechanics without a step-by-step derivation in
  the source; only the *existence* of damping is decree-justified (D6). Recorded as UNTRACEABLE.
- **Borderline δS=0.** All action-principle equations (Lagrangian, Hamilton's equations,
  Euler–Lagrange, geodesic, Einstein equations) are tagged "DERIVED-as-form (δS=0 borderline)" per
  the SPINE.md S6 note: that the realized expansion is the *stationary* one may itself be a
  dynamical decree.

*Cross-ref: `SPINE.md`, `DECREE_REGISTER.md`, `README_SCHEMA.md`, `EXPANSION_HYPOTHESIS_ANALYSIS.md`.*
