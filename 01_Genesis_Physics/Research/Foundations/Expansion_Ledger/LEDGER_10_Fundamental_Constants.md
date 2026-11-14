# Expansion Ledger — Domain 10: Fundamental Constants

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> Traces **every** distinct displayed/numbered equation and named key result in
> `Research/Mathematical_Models/10_Fundamental_Constants/` back to `1=1` via spine rungs S0–S9
> (`SPINE.md`) + decrees D0–D6 (`DECREE_REGISTER.md`). No equation is "derived from `1=1` alone."
> Constants tagged `[DERIVED ratio]` / `[SELECTED scale → D4]` / `[FIT → D5]` / `[count → D3]`.
>
> **Provenance note:** This is the EXHAUSTIVE re-trace replacing the earlier "principal-coverage"
> ledger (authored in-loop, 28 headline equations). It enumerates intermediate equations, failed
> attempts kept on record, definitional identities, and the op-file computations. Files traced (18):
> `10-FUNDAMENTAL_CONSTANTS_OVERVIEW.md`, `10-CONSTANTS_FROM_6D.md`, `10-PLANCK_CONSTANT_DERIVATION.md`,
> `10-GRAVITATIONAL_CONSTANT_DERIVATION.md`, `10-BOLTZMANN_CONSTANT_DERIVATION.md`,
> `10-FINE_STRUCTURE_DERIVATION.md`, `10-COUPLING_CONSTANTS_DERIVATION.md`,
> `10-RUNNING_COUPLINGS_RG_FLOW.md`, `10-RESOLVED_MEMBRANE_TENSION.md`,
> `10-MASS_HIERARCHY_RESOLUTION.md`, `10-COMPLETIONS.md`, `10-COMPLETIONS_R4.md`,
> `op01_z0_axiom_statement.md`, `op00_z0_action.py`, `op01_beta_geom_warp_integral.py`,
> `op07_two_loop_rg.py`, `op07_uv_bc_firstprinciples.py`. (Archive/__pycache__ none present.)

## Header table

| Field | Value |
|-------|-------|
| Domain | Fundamental_Constants |
| Equations traced | 97 |
| Decrees used across domain | D1, D2, D3, D4, D5, D6 (D0 implicit per SPINE.md S3 note — ℝ-continuum used domain-wide, cited once here, not per row) |
| Status breakdown | 36 DERIVED-as-form, 12 DERIVED-given-decrees, 48 PARTIAL, 1 UNTRACEABLE (per-row primary Status tag) |
| UNTRACEABLE / PARTIAL count | 48 PARTIAL, 1 UNTRACEABLE by per-row tag. NOTE: 5 of the 48 PARTIAL rows are flagged "PARTIAL → UNTRACEABLE / leans UNTRACEABLE" (EQ-FC-57, 64, 74, 86, 91) — their load-bearing coefficients are fitted/asserted, not derived. Together with EQ-FC-11 (the lone hard UNTRACEABLE) these are the **4 honest-gap findings** enumerated in the UNTRACEABLE § below (one finding can span two equations). So: 1 equation tagged UNTRACEABLE outright, 6 equations implicated across 4 documented honest-gap findings. |

Decree legend: D0 completed-ℝ; D1 dimension=6→4; D2 gauge group/U(1)/SU(2)/SU(3); D3 winding n_w=3;
D4 scale anchor Λ_Z0, M_{Z0}=M_Pl (every dimensionful magnitude); D5 fitted O(1) constants;
D6 architectural axioms (Firmament σ/μ, Waters Ψ_A/Ψ_B, zones, sustaining coupling).

**Domain-level finding:** This domain is the sharpest illustration of the grammar/decree split.
*Every* dimensionful constant here (ℏ, G, k_B, σ, μ, c, k₁, Λ_Z0, N_A) is `[SELECTED scale → D4]` —
a unit, not a derived number. The genuine *content* lives in the **dimensionless ratios** (α⁻¹≈137,
L_A/η_B=83.2, β_geom=813, b_eff≈9.05, the warp suppressions). The framework's own files repeatedly
rediscover this (k_B "is a unit conversion factor"; G's absolute value "not derivable"; ℏ coefficient
"taken from experiment"). The four ℏ derivations and three G derivations are **mutually inconsistent
dimensional ansätze** (σηB²/c vs σηB³/2c vs σηBξA/4π vs the Λ_Z0 β_geom chain); the ledger records
each on its own terms and flags the contradictions. The op-files (2026-05) are the most honest layer:
they invert the formulas, expose the required β_geom=813 / L_A=83.2ηB / α_6D≈1.82 as constrained-but-
not-derived, and reduce the whole tower to the single axiom Λ_Z0 (D4).

---

## I. The Λ_Z0 Axiom and the ℏ/α Chain (`op01_z0_axiom_statement.md`, `op00_z0_action.py`, `op01_beta_geom_warp_integral.py`)

### EQ-FC-01 — The Z₀ action (single foundational free parameter)
- **Equation:** S_Z0 = ∫d⁶x√(−g)[M_{Z0}⁴R⁽⁶⁾ − 2Λ_Z0] + Firmament term
- **Source:** op01_z0_axiom_statement.md §"The Axiom"; op00_z0_action.py §2
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1 (6D manifold), D4 (Λ_Z0 — the scale anchor), D6 (Z₀/Firmament architecture)
- **Trace:** 1=1 → S9 supplies the 6D Einstein–Hilbert + cosmological-constant action density; S6 the variational structure. The *form* is grammar; the single number Λ_Z0 is the irreducible scale decree D4 ("what 1 measures"). Whole framework reduces to this one parameter.
- **Constants:** Λ_Z0, M_{Z0} [SELECTED scale → D4]; the coefficients 1, 2 [DERIVED ratio].
- **Status:** DERIVED-as-form (the one scale is D4, by design).

### EQ-FC-02 — RS fine-tuning condition (k₁ from Λ_Z0)
- **Equation:** k₁² = |Λ_Z0|/(5 M_{Z0}⁴)
- **Source:** op01_z0_axiom_statement.md §"The Axiom"; op00_z0_action.py §3
- **Spine path:** S0→S1→S2→S3→S9
- **Decrees:** D4, D6, D1
- **Trace:** 1=1 → S2/S3 give the ratio and square root; the Randall–Sundrum fine-tuning relation (S9 AdS geometry) ties the curvature k₁ to the bulk Λ_Z0. The 5 is a [DERIVED ratio] from the 6D RS junction algebra. k₁'s magnitude is D4; the relation form is grammar+geometry.
- **Constants:** k₁, Λ_Z0, M_{Z0} [SELECTED scale → D4]; 5 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FC-03 — Z₀ brane tension (6D RS2)
- **Equation:** σ = 5 k₁ M_{Z0}⁴  (with σ² = 24 M_{Z0}⁴|Λ_Z0|/5 the exact RS2 junction)
- **Source:** op01_z0_axiom_statement.md §"Brane tension"; op00_z0_action.py §3–§4
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D1 (6D RS manifold), D4, D6
- **Trace:** 1=1 → S9 RS2 junction condition on the Z₀/Z₁ boundary fixes σ in terms of k₁ and M_{Z0} (the 6D manifold the junction lives on is D1, per DECREE rule 2). Both the prefactor 5 and the 24/5 are [DERIVED ratio] RS algebra; σ's magnitude is D4. This σ is the same Firmament tension used throughout the domain.
- **Constants:** σ, k₁, M_{Z0} [SELECTED scale → D4]; 5, 24/5 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FC-04 — Z₁ AdS warp profile
- **Equation:** A_Z1(ξ) = (2/3) ln(L_A/ξ)
- **Source:** op00_z0_action.py §1 (header); op01_beta_geom_warp_integral.py §4
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D1, D6, D4
- **Trace:** 1=1 → S9 solving the Z₁ Einstein eq. in the AdS bulk gives the logarithmic warp factor; the 2/3 index is the [DERIVED ratio] dimensional-reduction exponent (matches the canonical λ=−4/3 warp index reconciliation in the G-doc). L_A is a scale (D4).
- **Constants:** L_A [SELECTED scale → D4]; 2/3 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FC-05 — AdS length / curvature relation
- **Equation:** L_A = 3/(2k₁);  k₁ = 2/(3L_A) = 6.16×10¹² m⁻¹;  k₁c² = 1.22 MeV
- **Source:** op01_z0_axiom_statement.md §"Numerical Values"; op00_z0_action.py §1
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D1 (6D AdS manifold), D4, D6
- **Trace:** 1=1 → S2 reciprocal/ratio; the 3/2 from the AdS warp integral (S9; the warped 6D manifold is D1, per DECREE rule 2). L_A/η_B=83.2 is the load-bearing [DERIVED ratio]; k₁'s MeV magnitude is D4.
- **Constants:** L_A, k₁ [SELECTED scale → D4]; 3/2, 83.2 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FC-06 — Z₁ cosmological constant induced
- **Equation:** Λ_Z1 = −5 k₁²  (= −5k₁²M_{Z0}⁴ in mass⁶ units)
- **Source:** op00_z0_action.py §3 ("Lambda_Z1 = -5*k1^2")
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D1 (6D RS manifold), D4, D6
- **Trace:** 1=1 → S9 RS relation between bulk Λ and curvature on the 6D manifold (D1, per DECREE rule 2); 5 is [DERIVED ratio] RS algebra; sign negative = AdS. Magnitude scales with D4.
- **Constants:** Λ_Z1, k₁ [SELECTED scale → D4]; 5 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FC-07 — |Λ_Z0| numerical value under canonical M_{Z0}=M_Pl
- **Equation:** |Λ_Z0| = 5 k₁² M_Planck⁴ ≈ 1.65×10⁷¹ GeV⁶
- **Source:** op01_z0_axiom_statement.md §"Numerical Values"; op00_z0_action.py §6
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4 (both k₁ and the M_{Z0}=M_Pl choice)
- **Trace:** 1=1 → S2/S3 arithmetic substituting EQ-FC-02 with M_{Z0}=M_Pl. The number is pure unit choice (D4) twice over: k₁ scale + Planck-mass identification. Honestly: not a prediction.
- **Constants:** Λ_Z0, M_Planck, k₁ [SELECTED scale → D4]; 5 [DERIVED ratio].
- **Status:** PARTIAL (a number fixed entirely by the D4 unit/anchor choices; not derived content).

### EQ-FC-08 — β_geom warp integral (ℏ geometric factor)
- **Equation:** β_geom = I_ξ(L_A)·I_η/η_B² = 813.2;  I_ξ = 3 L_A^{4/3} η_B^{−1/3};  I_η = η_B·(√π/2)·erf(1) ≈ 0.7468 η_B
- **Source:** op01_beta_geom_warp_integral.py §4–§5; op01_z0_axiom_statement.md §"Hierarchy"
- **Spine path:** S0→S1→S6→S8→S9
- **Decrees:** D1, D3 (winding sector), D4 (scales in integrand), D6
- **Trace:** 1=1 → S6 integral of e^{2A} over the (ξ,η) fiber (S9 warp), η-piece an erf from a Gaussian boundary layer, ξ-piece the AdS power law (EQ-FC-04). β_geom=813 is a pure [DERIVED ratio] *given* L_A=83.2η_B. Honestly: the script shows L_A is required-not-derived, so β_geom is constrained, not first-principles.
- **Constants:** 813.2, 0.7468, 3, 4/3 [DERIVED ratio]; L_A, η_B [SELECTED scale → D4].
- **Status:** PARTIAL (geometry yields β_geom *iff* L_A=83.2η_B is fixed by Z₁ BC — still open per op01).

### EQ-FC-09 — Bare quantum ħ₀ (vortex base)
- **Equation:** ħ₀ = π σ η_B³/(2c)
- **Source:** op01_beta_geom_warp_integral.py §1; 10-PLANCK eq.(2.6)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D4, D6, D1
- **Trace:** 1=1 → S6/S9 vortex-core action on the membrane (tension × core area × light-crossing time, S6). Dimensionally [action]; magnitude pure D4 (σ,η_B,c all units). ~10⁴⁵ J·s, off by 10⁷⁹ before suppression.
- **Constants:** σ, η_B, c [SELECTED scale → D4]; π, ½ [DERIVED ratio].
- **Status:** PARTIAL (correct dimension; numerically meaningless until warp-suppressed).

### EQ-FC-10 — Planck constant from the Λ_Z0 chain (canonical ℏ formula)
- **Equation:** ℏ = ħ₀·(η_B/ξ_A)²·β_geom ≈ 1.05×10⁻³⁴ J·s
- **Source:** op01_beta_geom_warp_integral.py §3,§6; op01_z0_axiom_statement.md §"Hierarchy"
- **Spine path:** S0→S1→S2→S6→S8→S9
- **Decrees:** D1, D3, D4, D6
- **Trace:** 1=1 → chain EQ-FC-01..09 assembles ℏ as bare prefactor × warp suppression (η_B/ξ_A)² × dimensionless β_geom. The *dimensionful* ℏ is D4; the *content* is β_geom (D1,D3 geometry given L_A). This is the canonical reconciled ℏ; supersedes the OVERVIEW/CONSTANTS_FROM_6D ansätze.
- **Constants:** σ, η_B, ξ_A, c [SELECTED scale → D4]; β_geom, (η_B/ξ_A)², ½, π [DERIVED ratio].
- **Status:** PARTIAL (DERIVED-given-decrees in form; β_geom value depends on open L_A).

### EQ-FC-11 — k₁ at the nuclear/QED boundary (interpretive identity)
- **Equation:** k₁c² = 1.22 MeV; k₁/E_deuteron ≈ 0.55; k₁ between m_e (0.511) and E_d (2.22 MeV)
- **Source:** op00_z0_action.py §6
- **Spine path:** S0→S1→S2
- **Decrees:** D4
- **Trace:** 1=1 → S2 ratios of energy scales. The *coincidence* that k₁ sits between m_e and the deuteron binding is flagged by the source itself as "numerology or genuine connection — requires investigation." No spine path forces this proximity.
- **Constants:** k₁, m_e, E_d [SELECTED scale → D4]; the ratios [DERIVED ratio, but physically unexplained].
- **Status:** UNTRACEABLE (the claimed "naturalness" of k₁≈nuclear scale is asserted, not derived; see UNTRACEABLE §).

### EQ-FC-12 — ℏ sensitivity to L_A (constraint precision)
- **Equation:** Δℏ/ℏ = Δβ_geom/β_geom = (4/3)·ΔL_A/L_A
- **Source:** op01_beta_geom_warp_integral.py §7
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4
- **Trace:** 1=1 → S2/S6 differentiate β_geom ∝ L_A^{4/3}; the 4/3 is the [DERIVED ratio] AdS exponent. A consistency statement, not a new physical equation: L_A must be fixed to ~1% for ℏ at 1%.
- **Constants:** 4/3 [DERIVED ratio].
- **Status:** DERIVED-as-form (sensitivity identity).

---

## II. ℏ, c, G, k_B from Membrane Geometry (`10-CONSTANTS_FROM_6D`, `10-FUNDAMENTAL_CONSTANTS_OVERVIEW`, `10-PLANCK/GRAVITATIONAL/BOLTZMANN_DERIVATION`)

### EQ-FC-13 — 6D membrane action (kinetic form)
- **Equation:** S_total = ∫d⁶x[½μ(∂_t φ)² − ½σ(∂_i φ)²]
- **Source:** 10-CONSTANTS_FROM_6D §intro; 10-PLANCK §framework
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S6 supplies ∂; S9 the membrane field φ on the 6D manifold; S1 the +/− (kinetic vs gradient) split. Form is grammar; σ,μ are D4 and D6 (membrane content).
- **Constants:** σ, μ [SELECTED scale → D4]; ½ [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1,D6).

### EQ-FC-14 — Firmament wave equation (□φ=0)
- **Equation:** □φ = ∂²φ/∂t² − c²∇²φ = 0;  (1/c²)∂²φ/∂t² − ∇²φ = 0
- **Source:** 10-OVERVIEW eq.(16); 10-CONSTANTS_FROM_6D eq.(48); 10-BOLTZMANN eq.(2.1)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1 (6D membrane manifold), D4, D6
- **Trace:** 1=1 → S6 the d'Alembertian □; varying EQ-FC-13 (which itself carries D1) on the 6D membrane manifold (D1, per DECREE rule 2) gives the wave equation. c is the wave speed (D4 via σ/μ). Pure grammar given the membrane.
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1,D6).

### EQ-FC-15 — Speed of light from membrane (c²=σ/μ)
- **Equation:** c² = σ/μ ⇒ c = 2.998×10⁸ m/s
- **Source:** 10-OVERVIEW eq.(8); 10-CONSTANTS_FROM_6D §1.2; 10-RESOLVED_MEMBRANE_TENSION; 10-RUNNING eq.(6.1)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1 (6D membrane manifold), D6, D4
- **Trace:** 1=1 → S6 transverse-wave speed v²=tension/density on the elastic membrane medium (the 6D manifold is D1, per DECREE rule 2); identifying Firmament σ,μ gives c. D6 posits the membrane; D4 the magnitudes. Cross-ref EQ-FND-39.
- **Constants:** σ, μ, c [SELECTED scale → D4]. (c is dimensionful — m/s — so it is a D4 unit, not a [DERIVED ratio], even though it equals √(σ/μ): honesty rule 2. Only the *dimensionless* relation c²μ/σ=1 is grammar.)
- **Status:** DERIVED-given-decrees.

### EQ-FC-16 — Oscillator mode energy quantization
- **Equation:** E_n = (n+½)ℏω, n=0,1,2,…
- **Source:** 10-OVERVIEW eq.(17); 10-BOLTZMANN eq.(2.3); 10-CONSTANTS_FROM_6D eq.(53)
- **Spine path:** S0→S1→S4→S5→S6
- **Decrees:** D4
- **Trace:** 1=1 → S5/S6 harmonic-oscillator spectrum from the canonical structure; ½ zero-point is grammar; ℏ the action quantum (D4); n the mode count (S1/S8 integer).
- **Constants:** ℏ [SELECTED scale → D4]; ½ [DERIVED ratio]; n [count → D3-style integer, here just ℕ].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-17 — Transverse standing-wave quantization in η
- **Equation:** ψ ∝ sin(n_η π η/η_B); k_η = n_η π/η_B; k_η^min = π/η_B
- **Source:** 10-OVERVIEW eqs.(18–20)
- **Spine path:** S0→S1→S3→S5
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S5 standing-wave modes in a box of width η_B (Dirichlet); n_η integers from S8/ℕ. η_B is D4/D6. Pure grammar.
- **Constants:** η_B [SELECTED scale → D4]; π, n_η [DERIVED ratio / count].
- **Status:** DERIVED-as-form (given D1,D6).

### EQ-FC-18 — Confinement momentum / uncertainty seed
- **Equation:** Δp_η·Δη ≳ const; p_η ~ ℏ/η_B; ℏ ~ p_η·η_B
- **Source:** 10-OVERVIEW eqs.(21–24)
- **Spine path:** S0→S1→S4→S5
- **Decrees:** D4, D6
- **Trace:** 1=1 → S5 confinement to width η_B forces momentum spread ~ℏ/η_B (uncertainty). ℏ scale is D4. A heuristic that motivates the ℏ ansatz.
- **Constants:** ℏ, η_B [SELECTED scale → D4].
- **Status:** DERIVED-as-form (heuristic, given D4,D6).

### EQ-FC-19 — Relativistic mode dispersion
- **Equation:** E = ℏω = ℏck_η; for ground mode E ~ ℏcπ/η_B
- **Source:** 10-OVERVIEW eqs.(25–26)
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D4
- **Trace:** 1=1 → S6 ω=ck dispersion (massless modes); E=ℏω couples action quantum to frequency. Scales D4.
- **Constants:** ℏ, c, η_B [SELECTED scale → D4]; π [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-20 — ℏ dimensional ansatz (σηB²/c, OVERVIEW form)
- **Equation:** ℏ = σ η_B²/c (with C_ℏ ~ O(0.1) coefficient: ℏ = C_ℏ σηB²/c)
- **Source:** 10-OVERVIEW eqs.(29,64), §2.12 boxed
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6, D4, D1
- **Trace:** 1=1 → S6 mode quantization gives the *dimensional form* ℏ ∝ σηB²/c; the source is explicit the coefficient C_ℏ is NOT first-principles (taken from experiment; naive value off by 10⁹⁴). One of FOUR competing ℏ ansätze in the domain.
- **Constants:** σ, η_B, c [SELECTED scale → D4]; C_ℏ [FIT → D5].
- **Status:** PARTIAL (dimensional form only; coefficient a fit; numerically fails raw).

### EQ-FC-21 — Effective-mass oscillator frequency
- **Equation:** m_eff ~ μ η_B³; ω = √(k_spring/m_eff) = √(σ/(μη_B)) = c/η_B
- **Source:** 10-OVERVIEW eqs.(40–42)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1 (6D membrane manifold), D4, D6
- **Trace:** 1=1 → S6 SHM frequency from spring constant / effective mass on the membrane (S9; 6D manifold is D1, per DECREE rule 2); using σ/μ=c² gives ω=c/η_B. Intermediate result establishing EQ-FC-20.
- **Constants:** σ, μ, η_B, c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6).

### EQ-FC-22 — Zero-point energy of confined mode
- **Equation:** E₀ = ½ℏω = ½ℏc/η_B = πℏc/(2η_B) (with k=π/η_B)
- **Source:** 10-OVERVIEW eqs.(43,62)
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D4
- **Trace:** 1=1 → S4/S6 ½ℏω vacuum energy of the lowest mode. Grammar; scales D4.
- **Constants:** ℏ, c, η_B [SELECTED scale → D4]; ½, π [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-23 — Canonical field commutator
- **Equation:** [φ(r),Π(r′)] = iℏ δ³(r−r′); [a_n,a_m†]=δ_nm; Π=(1/c²)∂φ/∂t
- **Source:** 10-CONSTANTS_FROM_6D §4.1 eq.(51,52,50); 10-OVERVIEW eqs.(50–52)
- **Spine path:** S0→S1→S4→S5→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → S4 (i from ℂ) + S5/S6 (conjugate momentum from the Lagrangian) give the canonical bracket; promoting Poisson→commutator inserts ℏ (D4). Cross-ref LEDGER_05.
- **Constants:** ℏ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-24 — Many-body mode energy
- **Equation:** E = Σ_i ℏω_i(n_i+½)
- **Source:** 10-CONSTANTS_FROM_6D eq.(53)
- **Spine path:** S0→S1→S4→S5→S6
- **Decrees:** D4
- **Trace:** 1=1 → sum of EQ-FC-16 over modes; grammar.
- **Constants:** ℏ [SELECTED scale → D4]; ½ [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-25 — Box momentum quantization
- **Equation:** p_n = nπℏ/V (or k_n=nπ/L, Δk=π/L); Δp=πℏ/L
- **Source:** 10-OVERVIEW eqs.(55–60)
- **Spine path:** S0→S1→S3→S5
- **Decrees:** D4
- **Trace:** 1=1 → S5 discrete spectrum in a finite domain; integers from ℕ. Establishes the confinement scaling for ℏ. Scale D4.
- **Constants:** ℏ, L/V [SELECTED scale → D4]; π, n [DERIVED ratio/count].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-26 — Phase-space ℏ ansatz (CONSTANTS_FROM_6D form)
- **Equation:** Δx·Δp = σ η_B ξ_A/(4π) ⇒ ℏ = σ η_B ξ_A/(4π)
- **Source:** 10-CONSTANTS_FROM_6D §1.4 boxed, eqs.(in §1.3–1.4)
- **Spine path:** S0→S1→S4→S5→S9
- **Decrees:** D1, D6, D4
- **Trace:** 1=1 → S5 phase-space cell set by membrane tension × compact volume η_B ξ_A; S4 supplies i in [φ,π]=iℏ. 4π is geometric [DERIVED ratio]. A SECOND, distinct dimensional ansatz (uses ξ_A, not η_B²/c) — competes with EQ-FC-20.
- **Constants:** σ, η_B, ξ_A [SELECTED scale → D4]; 4π [DERIVED ratio].
- **Status:** PARTIAL (dimensional ansatz; conflicts with EQ-FC-20/EQ-FC-10 — coefficient unsettled).

### EQ-FC-27 — Self-consistent ℏ collapse (Planck-scale parameter substitution)
- **Equation:** with σ~M_Pl²c, η_B~ξ_A~1/M_Pl ⇒ ℏ = c/(4π)
- **Source:** 10-CONSTANTS_FROM_6D §1.5
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4
- **Trace:** 1=1 → S2/S3 substitute Planck-scale forms into EQ-FC-26; a self-consistency identity (defines a relation among ℏ,c,M_Pl), not a derivation of ℏ. Honest "self-consistent definition."
- **Constants:** c, M_Pl [SELECTED scale → D4]; 4π [DERIVED ratio].
- **Status:** PARTIAL (tautological self-consistency, not a value prediction).

### EQ-FC-28 — Uncertainty principle
- **Equation:** Δx·Δp ≥ ℏ/2 = |⟨[x,p]⟩|/2
- **Source:** 10-CONSTANTS_FROM_6D §4.2 eq.(273-region); 10-OVERVIEW eq.(21)
- **Spine path:** S0→S1→S4→S5
- **Decrees:** D4
- **Trace:** 1=1 → S5 Cauchy–Schwarz on the S4 commutator EQ-FC-23 gives ΔxΔp≥½|⟨[x,p]⟩|=ℏ/2. Theorem of grammar; only scale ℏ is D4.
- **Constants:** ℏ [SELECTED scale → D4]; ½ [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-29 — Schrödinger equation
- **Equation:** iℏ ∂Ψ/∂t = ĤΨ, Ĥ=p̂²/2m+V(x̂)
- **Source:** 10-CONSTANTS_FROM_6D §4.3 eqs.(283,288)
- **Spine path:** S0→S1→S4→S5→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → quantizing the membrane wave equation EQ-FC-14 with S4/S5 canonical structure gives time-evolution by Ĥ. Cross-ref LEDGER_05. Grammar + scale.
- **Constants:** ℏ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4,D6).

### EQ-FC-30 — Naive ℏ failure (recorded negative result)
- **Equation:** σ η_B²/c = 3.38×10⁶⁰ J·s (off by ~10⁹⁴)
- **Source:** 10-OVERVIEW eqs.(30–35); 10-PLANCK eqs.(1.1)
- **Spine path:** S0→S1→S2
- **Decrees:** D4
- **Trace:** 1=1 → S2 substitute canonical σ,η_B,c into EQ-FC-20. Honest negative result kept on record: the dimensional form has correct dimension but wrong magnitude by 94 orders, motivating warp suppression.
- **Constants:** σ, η_B, c [SELECTED scale → D4].
- **Status:** PARTIAL (negative result; see UNTRACEABLE/COVERAGE note on coefficient mystery).

### EQ-FC-31 — Planck-unit definitions (M_Pl, ℓ_Pl, t_Pl, E_Pl)
- **Equation:** M_Pl=√(ℏc/G), ℓ_Pl=√(ℏG/c³), t_Pl=√(ℏG/c⁵), E_Pl=1.221×10¹⁹ GeV
- **Source:** 10-CONSTANTS_FROM_6D §2.4; 10-OVERVIEW eqs.(13–15,146–149)
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4
- **Trace:** 1=1 → S2/S3 unique monomials in ℏ,c,G with mass/length/time dimensions. Pure dimensional grammar once the three scales (all D4) given.
- **Constants:** ℏ,c,G [SELECTED scale → D4]; ½ powers [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-32 — Planck consistency M_Pl·ℓ_Pl
- **Equation:** M_Pl ℓ_Pl = √(ℏ²/c) ~ ℏ/c
- **Source:** 10-CONSTANTS_FROM_6D §2.4
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4
- **Trace:** 1=1 → S2 product of EQ-FC-31 entries; dimensional identity.
- **Constants:** ℏ,c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-33 — Linearized Einstein equation / Newtonian limit
- **Equation:** G_μν = (8πG/c⁴)T_μν; ∇²φ = 4πGMδ³(x); φ = −GM/r; h₀₀≈2φ/c²
- **Source:** 10-OVERVIEW eqs.(70,72,73,74); 10-CONSTANTS_FROM_6D §5.1
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S9 Einstein tensor + S6 variation of EH action; weak-field limit gives Poisson/Newton. G is the coupling (D4); 8π,4π [DERIVED ratio]. Cross-ref relativity ledger.
- **Constants:** G,c [SELECTED scale → D4]; 8π,4π,2 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1).

### EQ-FC-34 — G from membrane stiffness (scaling)
- **Equation:** G ~ c⁴/σ; (with C_G: G = (c⁴/σ)·C_G, C_G~η_B²/ξ_A²)
- **Source:** 10-OVERVIEW eqs.(78,81,89), §3.4 boxed
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6, D4, D1
- **Trace:** 1=1 → S9 weak-field membrane bending vs linearized Einstein gives G∝1/σ. Source is explicit and honest: scaling (gravity weak ⇐ σ huge) is derived; absolute value NOT first-principles. Note the doc itself catches the dimensional error in c⁴/σ and corrects to c²/(μη_B).
- **Constants:** c, σ [SELECTED scale → D4]; η_B²/ξ_A² [DERIVED ratio]; C_G [FIT → D5].
- **Status:** PARTIAL (scaling DERIVED; absolute value open per source).

### EQ-FC-35 — G dimensional correction (c²/μη_B form)
- **Equation:** G = c²/(μη_B)·C_G ⇒ 1.03×10⁻⁵¹ (off by ~10⁴⁰)
- **Source:** 10-OVERVIEW eqs.(86–93), §3.5–3.6
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D4, D6, D1
- **Trace:** 1=1 → S2 dimensional-analysis solution G=[L³M⁻¹T⁻²] from σ,μ,c,η_B,ξ_A (one free exponent solved as c²/μη_B). Honest negative: numerically off by 40 orders. A SECOND G ansatz.
- **Constants:** c, μ, η_B [SELECTED scale → D4]; C_G [FIT → D5].
- **Status:** PARTIAL (dimensional form; numerically fails by 10⁴⁰).

### EQ-FC-36 — G from critical density (Friedmann inversion)
- **Equation:** ρ_crit = 3H²/(8πG) ⇒ G = 3H²/(8πρ_crit)
- **Source:** 10-OVERVIEW eqs.(97,98)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S9 Friedmann equation rearranged; G expressed via cosmic H and density. Definitional inversion, not a membrane derivation; scales D4.
- **Constants:** H, ρ_crit [SELECTED scale → D4]; 3, 8π [DERIVED ratio].
- **Status:** DERIVED-as-form (Friedmann identity; given D1).

### EQ-FC-37 — G from α-analog hierarchy (failed estimate)
- **Equation:** G ~ ℏc/(α (ξ_A/η_B)² m_ref²) ⇒ 1.56×10⁻⁵⁷ (off)
- **Source:** 10-OVERVIEW eqs.(101–108)
- **Spine path:** S0→S1→S2
- **Decrees:** D4, D5
- **Trace:** 1=1 → S2 ratio combining α, scale ratio, nucleon mass. Recorded as a failed numerical attempt (off by ~46 orders). A THIRD G route.
- **Constants:** ℏ,c,m_ref [SELECTED scale → D4]; α, (ξ_A/η_B)² [DERIVED ratio]; coefficient [FIT → D5].
- **Status:** PARTIAL (failed estimate, kept on record).

### EQ-FC-38 — Gravitational fine-structure analog
- **Equation:** α_G = G m_P²/(ℏc) = 1 (Planck mass); G m_e²/(e²/4πε₀) ≈ 10⁻³⁸
- **Source:** 10-OVERVIEW eqs.(99,67); 10-PLANCK eq.(5.1)
- **Spine path:** S0→S1→S2
- **Decrees:** D4
- **Trace:** 1=1 → S2 ratio of gravitational to EM coupling; tautological at m_P (defines it); 10⁻³⁸ hierarchy = (m_e/m_P)² [DERIVED ratio] given masses (D4/D5).
- **Constants:** masses, e, ε₀ [SELECTED scale → D4 / FIT → D5]; 10⁻³⁸ [DERIVED ratio].
- **Status:** DERIVED-as-form (given mass scales).

### EQ-FC-39 — Planck-length non-emergence (honest negative)
- **Equation:** ℓ_Pl = √(ℏG/c³) ~ η_B/√σ = 5.3×10⁻⁶⁵ m (≠ 1.6×10⁻³⁵)
- **Source:** 10-OVERVIEW §5.2 eqs.(150,151)
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4, D6
- **Trace:** 1=1 → S2/S3 substitute membrane forms of ℏ,G into ℓ_Pl; result misses true Planck length by ~30 orders. The structure traces; the value fails (because membrane-G EQ-FC-34/35 are not numerically correct).
- **Constants:** ℏ,G,c,σ,η_B [SELECTED scale → D4].
- **Status:** PARTIAL (negative result; flagged in coverage).

### EQ-FC-40 — G from 6D KK volume reduction (CONSTANTS_FROM_6D form)
- **Equation:** G₄ = G₆ V_compact = G₆ ξ_A η_B; G₆ = ℏc/(M_Pl² ξ_A η_B); G₄ = ℏc/M_Pl²
- **Source:** 10-CONSTANTS_FROM_6D §2 boxed; KK_DIMENSIONAL_REDUCTION
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4
- **Trace:** 1=1 → integrating 6D EH over the two extra dims (S9+S6) relates G₄,G₆ by V_compact. Note CONSTANTS_FROM_6D writes G₄=G₆·V (multiply) while GRAVITATIONAL/COMPLETIONS write G₄=G₆/V (divide) — an internal sign-of-exponent inconsistency. Cross-ref EQ-FND-46.
- **Constants:** G₆, M_Pl, ξ_A, η_B [SELECTED scale → D4]; V_compact [DERIVED ratio].
- **Status:** PARTIAL (form DERIVED-given-decrees; multiply/divide inconsistency across files).

### EQ-FC-41 — Equipartition / Boltzmann definition
- **Equation:** ⟨E⟩ = ½k_B T per quadratic DOF; E_kin = (3/2)Nk_B T; ⟨p²/2m⟩=½k_BT
- **Source:** 10-OVERVIEW eqs.(110,111,116,118); 10-BOLTZMANN eqs.(2.9,3.6,3.7)
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4
- **Trace:** 1=1 → S2/S3 statistical-counting theorem; equipartition is grammar. Used to *define* k_B. k_B sets the energy↔temperature unit (D4).
- **Constants:** k_B [SELECTED scale → D4]; ½, 3/2 [DERIVED ratio].
- **Status:** DERIVED-as-form (k_B is a D4 unit).

### EQ-FC-42 — Bose–Einstein / Fermi–Dirac occupation
- **Equation:** ⟨n⟩ = 1/(e^{(ε−μ)/k_BT} ∓ 1)
- **Source:** 10-BOLTZMANN eqs.(2.4,7.1,7.2,7.3); 10-OVERVIEW eq.(113); 10-CONSTANTS_FROM_6D-region
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4, D3 (winding parity ⇒ statistics)
- **Trace:** 1=1 → S2 geometric series of Boltzmann weights over the mode ladder; ∓1 from boson/fermion counting. The framework ties parity to defect winding (S8/D3) — boson=integer, fermion=half-integer winding.
- **Constants:** k_B [SELECTED scale → D4]; statistics sign [count → D3].
- **Status:** DERIVED-as-form (given D4; statistics-from-winding is D3-flavored, partly asserted).

### EQ-FC-43 — Single-oscillator partition function & mean energy
- **Equation:** Z = e^{−βℏω/2}/(1−e^{−βℏω}); ⟨E⟩ = ℏω/2 + ℏω/(e^{βℏω}−1); classical → k_BT
- **Source:** 10-OVERVIEW eqs.(130–132); 10-BOLTZMANN eqs.(in §7.2)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D4
- **Trace:** 1=1 → S2 geometric series Σxⁿ=1/(1−x) over Eₙ=ℏω(n+½); ⟨E⟩=−∂lnZ/∂β (S6). Pure grammar; only ℏ,k_B scales (D4). Classical limit recovers equipartition.
- **Constants:** ℏ,k_B [SELECTED scale → D4]; ½ [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-44 — Boltzmann entropy / temperature definition
- **Equation:** S = k_B ln Ω; 1/(k_BT) = ∂S/∂E; ΔE = k_BTΔS
- **Source:** 10-OVERVIEW eqs.(121,126,127); 10-BOLTZMANN eqs.(9.1,9.4)
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4
- **Trace:** 1=1 → S2 logarithm of microstate count; thermodynamic temperature is the conjugate of entropy. Grammar; k_B is the D4 unit.
- **Constants:** k_B [SELECTED scale → D4]; Ω [count].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-45 — Density of states (3D Debye)
- **Equation:** ρ(ω) = Vω²/(2π²c³); g(ω)=ω²/(π²c³); N(ω)=Vω³/(π²c³)
- **Source:** 10-OVERVIEW eq.(114); 10-BOLTZMANN eqs.(2.2,3.3); 10-COMPLETIONS eq.(3.3)
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D1, D4
- **Trace:** 1=1 → S5 counting independent k-modes in a 3D box (k-space shell) with ω=ck (S6) gives ω² DOS. D1 fixes 3 spatial dims; D4 the scale c. (Note OVERVIEW uses 2π², COMPLETIONS uses π² — factor-of-2 internal discrepancy.)
- **Constants:** c [SELECTED scale → D4]; 2π²/π² [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FC-46 — Debye frequency / temperature
- **Equation:** ω_D = c/η_B ≈ 2.3×10²³ rad/s; T_D = ℏω_D/k_B = ℏc/(k_Bη_B)
- **Source:** 10-BOLTZMANN eqs.(2.6,2.7,2.8)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → S6 cutoff at the shortest membrane wavelength η_B; T_D ratio of Debye energy to k_B. Scales D4; cutoff η_B is D6.
- **Constants:** c, η_B, ℏ, k_B [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D6).

### EQ-FC-47 — k_B as unit conversion (honest theorem)
- **Equation:** k_B = 1.380649×10⁻²³ J/K (SI-defined); k_B T = ⟨E per DOF⟩
- **Source:** 10-OVERVIEW §4.11,§4.13; 10-BOLTZMANN §4,§10; 10-COMPLETIONS §3.5
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4
- **Trace:** 1=1 → existence/form from statistical mechanics (grammar); the source's own honest conclusion: k_B is a **unit-conversion factor**, absolute value not derivable — temperature is an independent unit (pure D4). This is the §11 dimensionful theorem restated by the framework itself, three times across the domain.
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** PARTIAL (existence/form DERIVED; absolute value is a unit (D4), per source).

### EQ-FC-48 — k_B ~ ℏc/η_B candidate (failed)
- **Equation:** k_B ~ ℏc/η_B = 2.43×10⁻¹¹ J/K (off by ~10¹²)
- **Source:** 10-BOLTZMANN eqs.(3.10–3.13)
- **Spine path:** S0→S1→S2
- **Decrees:** D4
- **Trace:** 1=1 → S2 dimensional candidate from membrane energy/length; honest negative: off by 10¹². Then "rescued" by an ad-hoc warp factor e^{2A}≈5.7×10⁻¹³ (A≈−14.4) chosen to match — i.e. a fit, not a derivation.
- **Constants:** ℏ,c,η_B [SELECTED scale → D4]; warp factor [FIT → D5].
- **Status:** PARTIAL (failed candidate + reverse-engineered warp factor).

### EQ-FC-49 — k_B ~ ℏc/ξ_A and Compton-scale candidate (failed)
- **Equation:** k_B ~ ℏc/ξ_A; k_B ~ λ_C m_e c²/ξ_A = 1.05×10⁻⁵² J/K (off by ~10²⁹)
- **Source:** 10-OVERVIEW eqs.(141–145)
- **Spine path:** S0→S1→S2
- **Decrees:** D4
- **Trace:** 1=1 → S2 alternative dimensional candidates; both fail numerically by huge factors. Recorded honestly.
- **Constants:** ℏ,c,ξ_A,m_e [SELECTED scale → D4].
- **Status:** PARTIAL (failed candidates).

### EQ-FC-50 — Quantum-to-thermal ratio
- **Equation:** ℏω/(k_BT) (sets quantum vs classical regime); ~5.9×10⁹ at η_B scale, 300 K
- **Source:** 10-OVERVIEW eqs.(136–139); 10-BOLTZMANN §3
- **Spine path:** S0→S1→S2
- **Decrees:** D4
- **Trace:** 1=1 → S2 dimensionless ratio of two energy scales; physical and [DERIVED ratio] given ℏ,k_B,ω,T. Source notes this ratio is physical even though k_B's absolute value is a unit — clean statement of the §11 principle.
- **Constants:** scales [SELECTED scale → D4]; the ratio [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-51 — Planck temperature
- **Equation:** T_P = √(ℏc⁵/(Gk_B²)) = 1.417×10³² K
- **Source:** 10-OVERVIEW eq.(133); 10-BOLTZMANN table
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4
- **Trace:** 1=1 → S2/S3 unique monomial in ℏ,c,G,k_B with temperature dimension. Source flags the circularity (defining k_B via T_P uses k_B). Pure dimensional grammar; scales D4.
- **Constants:** ℏ,c,G,k_B [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-52 — Compton wavelength consistency
- **Equation:** λ_C = h/(m_e c) = 2πℏ/(m_e c) = 2.43×10⁻¹² m
- **Source:** 10-OVERVIEW §2.11 eqs.(65,66)
- **Spine path:** S0→S1→S2→S4
- **Decrees:** D4
- **Trace:** 1=1 → S2/S4 definitional ratio of action-scale to momentum; grammar given ℏ,m_e,c (D4). Consistency check on ℏ.
- **Constants:** ℏ, m_e, c [SELECTED scale → D4]; 2π [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-53 — Planck spectral / Stefan–Boltzmann
- **Equation:** u(ω,T) = (ℏω³/π²c³)/(e^{ℏω/k_BT}−1); σ_SB = π²k_B⁴/(60ℏ³c²)
- **Source:** 10-OVERVIEW §4; 10-BOLTZMANN eq.(5.3)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D4
- **Trace:** 1=1 → S6 integrate mode energy EQ-FC-43 against DOS EQ-FC-45; σ_SB is a pure combination of ℏ,c,k_B with [DERIVED ratio] π²/60 (from ∫x³/(eˣ−1)=π⁴/15). Scales D4. Cross-ref LEDGER_02.
- **Constants:** ℏ,c,k_B [SELECTED scale → D4]; π²/60 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

---

## III. Couplings, Tension, and Hierarchies (`10-COUPLING_CONSTANTS`, `10-FINE_STRUCTURE`, `10-RESOLVED_MEMBRANE_TENSION`, `10-MASS_HIERARCHY`, `10-RUNNING_COUPLINGS`)

### EQ-FC-54 — Membrane tension resolution (canonical σ)
- **Equation:** σ = μ c² = ρ_Planck·η_B·c² ≈ 6.0×10⁹⁸ kg/(m·s²); μ = ρ_Pl η_B ≈ 6.7×10⁸² kg/m²
- **Source:** 10-RESOLVED_MEMBRANE_TENSION §3; 10-OVERVIEW eqs.(6,7)
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D1 (6D membrane manifold), D4, D6
- **Trace:** 1=1 → S2 σ=μc² from EQ-FC-15 (which carries D1); μ built from Planck density × η_B thickness on the 6D membrane (D1, per DECREE rule 2). σ,μ are Firmament elastic constants (D6); their magnitudes fixed by matching c and the η_B thickness choice (D4). Resolves a prior 73-order spread by *selecting* δ=η_B.
- **Constants:** σ, μ, ρ_Planck, η_B [SELECTED scale → D4].
- **Status:** PARTIAL (ratio σ/μ=c² derived; individual magnitudes are D4 unit anchors via a chosen thickness).

### EQ-FC-55 — Planck density
- **Equation:** ρ_Planck = m_P/ℓ_P³ = 5.15×10⁹⁷ kg/m³
- **Source:** 10-RESOLVED_MEMBRANE_TENSION §3 Step 2
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4
- **Trace:** 1=1 → S2/S3 ratio of Planck mass to Planck-length cubed (EQ-FC-31). Dimensional grammar; scales D4.
- **Constants:** m_P, ℓ_P [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4).

### EQ-FC-56 — α master formula (log-ratio)
- **Equation:** α⁻¹ = C·ln(ξ_A/η_B); C = b_eff/(2π); ln(ξ_A/η_B) ≈ 95.26
- **Source:** 10-FINE_STRUCTURE eqs.(33,441,669); 10-COUPLING eq.(107); 10-OVERVIEW eq.(153)
- **Spine path:** S0→S1→S2→S3→S4→S7→S8
- **Decrees:** D1, D2 (U(1) coupling), D4 (scales in ratio), D5 (C/b_eff calibration)
- **Trace:** 1=1 → S4 U(1) phase; S2/S3 the ratio ξ_A/η_B and its log; warp-weighted gauge coupling runs logarithmically (S7/S8). α⁻¹ is dimensionless [DERIVED ratio]; ln-structure is grammar+geometry; coefficient C is the open item.
- **Constants:** ξ_A/η_B [DERIVED ratio]; C [FIT/DERIVED → see EQ-FC-57]; α⁻¹ [DERIVED ratio given C].
- **Status:** PARTIAL (log/ratio structure DERIVED-given-decrees; coefficient open).

### EQ-FC-57 — b_eff from SM particle content
- **Equation:** C = b_eff/(2π) = 9.05/(2π) ≈ 1.44; b_eff built from SM loop content
- **Source:** 10-FINE_STRUCTURE §5–§6 eqs.(40,313,373,418,447)
- **Spine path:** S0→S1→S2→S7→S8
- **Decrees:** D1, D2, D3 (3 generations), D5
- **Trace:** 1=1 → S7 β-function coefficient from the gauge/matter content; D2 fixes the group, D3 the 3 generations. The doc's *own arithmetic wanders* (b=48, then 5.33, then "8.97≈9.05" assembled from listed sub-contributions 3.67+2+1.4+0.7+0.6). The clean charge-weighted count gives 16/3≈5.33, NOT 9.05; the extra ~3.7 is admitted to come from un-derived "topological/warp/higher-loop" terms. So 9.05 is a partly-assembled, partly-fitted number.
- **Constants:** 2π [DERIVED ratio]; b_eff=9.05 [FIT → D5 (the residual ~3.7 above the derivable 5.33)]; 3 generations [count → D3].
- **Status:** PARTIAL → leans UNTRACEABLE (the headline 9.05 is not reproduced by the document's own clean count; see UNTRACEABLE §).

### EQ-FC-58 — α numerical prediction
- **Equation:** α⁻¹ = 1.44×95.26 = 137.17 (vs 137.036, 0.095% error); C_obs = 1.4381
- **Source:** 10-FINE_STRUCTURE §7; 10-COUPLING §2.6; 10-RESOLVED_MEMBRANE_TENSION §4
- **Spine path:** S0→S1→S2
- **Decrees:** D4, D5
- **Trace:** 1=1 → S2 arithmetic product of C and the log. The 0.1% agreement is the domain's headline; but C is reverse-checked against data (C_obs=137.036/95.26=1.4381), so this is calibration-confirmed, not parameter-free.
- **Constants:** ξ_A/η_B [DERIVED ratio]; C=1.44 [FIT → D5]; α⁻¹ [DERIVED ratio given C].
- **Status:** PARTIAL (precision agreement; coefficient is D5-calibrated).

### EQ-FC-59 — 6D gauge action & KK reduction formula
- **Equation:** S_gauge⁶ = −(1/4κ₆²)∫d⁶x√(−g)F_MN F^MN; 1/g_EM² = (1/κ₆²)∫dξdη e^{2A+2B}|f₀|²
- **Source:** 10-FINE_STRUCTURE §1–§2 eqs.(57,96,109); op07_uv_bc_firstprinciples.py §1
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D1, D2, D4, D6
- **Trace:** 1=1 → S7 gauge field on the 6D manifold (S9); S6 integrate out extra dims → 4D coupling = warp-weighted volume. The op07 script notes the e^{4A} factors cancel for gauge zero modes (only e^{2B} survives) — a genuine [DERIVED] structural result.
- **Constants:** κ₆, g₆ [SELECTED scale → D4]; warp integral [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form).

### EQ-FC-60 — 6D metric with warp factors
- **Equation:** ds² = e^{2A(ξ)}η_μν dx^μdx^ν − dξ² − e^{2B(η)}dη²; A=A₀+(λ/2)ln(ξ/ξ₀), B=B₀−(γ/2)η
- **Source:** 10-FINE_STRUCTURE §1.2 eqs.(68,71,73); 10-COUPLING §1.2; 10-MASS_HIERARCHY §3.2
- **Spine path:** S0→S1→S9
- **Decrees:** D1, D6, D4
- **Trace:** 1=1 → S9 metric ansatz on the 6D zone manifold preserving 4D Poincaré; warp profiles are the D6 architecture. λ,γ are profile parameters (D4/D5).
- **Constants:** A₀,B₀,λ,γ [SELECTED scale → D4 / FIT → D5].
- **Status:** DERIVED-as-form (given D1,D6).

### EQ-FC-61 — Zero-mode wavefunction & normalization
- **Equation:** f₀(ξ) ∝ ξ^{−α}; ∫e^{2A}|f₀|²dξ = 1; V_ξ ∝ ∫ξ^{λ−2α}dξ → ln(ξ_A/η_B) when λ−2α=−1
- **Source:** 10-FINE_STRUCTURE §3–§4 eqs.(138,150,183,187)
- **Spine path:** S0→S1→S3→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S6 solving the zero-mode equation in the warped geometry; the log emerges precisely when the integrand ~1/ξ. This is the mechanism behind EQ-FC-56's logarithm. Localization exponent α≈1–2 asserted from "topology."
- **Constants:** α (localization) [FIT → D5]; ln(ξ_A/η_B) [DERIVED ratio].
- **Status:** PARTIAL (log mechanism DERIVED; α-exponent asserted).

### EQ-FC-62 — Running coupling / β-function (general)
- **Equation:** μ dα⁻¹/dμ = b₀/(2π); α⁻¹(μ) = α⁻¹(μ₀) + (b₀/2π)ln(μ/μ₀)
- **Source:** 10-FINE_STRUCTURE §5.1 eqs.(234,239); 10-RUNNING eqs.(2.1,1.13,3.1)
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S7 β-function as scale-derivative of the gauge coupling (Noether/RG structure); S6 the integral. D2 fixes the group + matter; b₀ a [DERIVED ratio] integer combo. Standard RG grammar.
- **Constants:** b₀ [DERIVED ratio from D2]; 2π [DERIVED ratio]; boundary value [FIT → D5].
- **Status:** DERIVED-as-form (given D2).

### EQ-FC-63 — 2D Green's function (logarithmic)
- **Equation:** ∇²₂ G₂ = δ²(r); G₂ = −(1/2π)ln r; G_extra ≈ C₀ + (1/2π)ln(ξ_A/η_B)
- **Source:** 10-COUPLING §2.2–§2.3 eqs.(123,132,136)
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D1, D4
- **Trace:** 1=1 → S6 the 2D Laplacian Green's function is logarithmic (a math identity, not approximation, in 2D). Provides an alternate route to the ln(ξ_A/η_B) of EQ-FC-56. D1 supplies the 2-extra-dim structure.
- **Constants:** 1/2π [DERIVED ratio]; ξ_A/η_B [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form; the 1.4383 residue derivation §2.5/AppA is heuristic — see EQ-FC-64).

### EQ-FC-64 — Pole-residue 1.4383 coefficient (heuristic)
- **Equation:** 1.4383 = (4π/3π)·(geometric factor); m²_eff = Σ_{nm≠0}(n²π²/ξ_A²+m²π²/η_B²)
- **Source:** 10-COUPLING §2.5, AppA eqs.(166,768,772)
- **Spine path:** S0→S1→S3→S7→S8
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → claims the EM coupling coefficient comes from a pole-residue of the KK-summed Green's function, "4π/3π × geometric factor." The derivation is admitted hand-wavy ("detailed calculation… yields Res ∝ ln"); the 4π/3π split is asserted. This is the COUPLING-doc's version of the 1.44; competes with FINE_STRUCTURE's b_eff/2π.
- **Constants:** 1.4383 [FIT → D5]; 4π,3π [DERIVED ratio].
- **Status:** PARTIAL → UNTRACEABLE (the 1.4383 residue is asserted, not derived; see UNTRACEABLE §).

### EQ-FC-65 — QED one-loop running of α
- **Equation:** α(Q) = α₀/(1−(α₀/3π)ln(Q/Q₀)); β₀^QED = 1/3π ≈ 0.106; b_em = 41/10
- **Source:** 10-COUPLING §2.7 eq.(197); 10-RUNNING §2.1 eqs.(2.4),§3.1; op07_two_loop_rg.py §2
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S7 QED β-function from virtual e⁺e⁻ screening; 1/3π and 41/10 are [DERIVED ratio] from the charge-weighted SM content (D2). Running form grammar; anchor value D5. (op07 computes ΣQ²=14/3 and b₀=8/(3π) — note the domain mixes 41/10, 4.1, and 8/(3π) conventions.)
- **Constants:** 1/3π, 41/10 [DERIVED ratio from D2]; α(M_Z) anchor [FIT → D5].
- **Status:** PARTIAL (running+coefficient DERIVED-given-D2; anchor a fit).

### EQ-FC-66 — Two-loop RG and UV boundary condition
- **Equation:** dα⁻¹/dlnμ = −(b₀/2π) − (b₁/8π²)α + …; α(Λ_zone) ≈ 1/146; Δb_eff ~ 0.8%
- **Source:** op07_two_loop_rg.py §3–§5; op07_uv_bc §4; 10-RUNNING §5
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D1, D2, D4, D5
- **Trace:** 1=1 → S6/S7 two-loop β-function; integrating from the UV boundary Λ_zone=ℏc/η_B runs α⁻¹. b₁ from ΣQ⁴ (D2). The two-loop shift is quantified at ~0.8% (within the stated 0.15 precision budget). UV boundary is the open D5 item.
- **Constants:** b₁ [DERIVED ratio from D2]; 8π² [DERIVED ratio]; UV boundary [FIT → D5].
- **Status:** PARTIAL (running DERIVED; UV BC computed-not-derived; two-loop within budget).

### EQ-FC-67 — UV BC from 6D action (α_6D ≈ 1.82)
- **Equation:** α_4D = α_6D·(η_B²/V_warp); V_warp = 3L_A η_B; α_4D = α_6D/(3·83.2) ⇒ α_6D ≈ 1.82
- **Source:** op07_uv_bc_firstprinciples.py §1–§3,§6
- **Spine path:** S0→S1→S2→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S6 KK reduction (EQ-FC-59) gives α_4D = α_6D·η_B²/V_warp; with V_warp≈3L_Aη_B (using ξ_min=L_A cutoff), α_4D ≈ α_6D/(3·83.2). For α_4D=1/137, α_6D≈1.82 — an O(1) "natural" coupling. KEY: the SAME L_A=83.2η_B that fixes ℏ also gives α~1/137 to ~20%. Genuine cross-link, but α_6D=1.82 (not 1.0) and ξ_min=L_A are admitted unresolved.
- **Constants:** α_6D≈1.82 [FIT → D5]; 3, 83.2 [DERIVED ratio]; L_A, η_B [SELECTED scale → D4].
- **Status:** PARTIAL (structure + cross-link DERIVED; α_6D=1.82 and the ξ_min=L_A cutoff asserted).

### EQ-FC-68 — Strong coupling SU(3) origin & gluon count
- **Equation:** SU(3) from 3 transverse polarizations; #gluons = 3²−1 = 8
- **Source:** 10-COUPLING §3.2 eq.(249)
- **Spine path:** S0→S1→S5→S7
- **Decrees:** D2, D1
- **Trace:** 1=1 → S7 SU(N) family; D2 selects SU(3); 3²−1=8 is a [count → D3-style] from the adjoint dimension. The "3 transverse directions ⇒ 3 colors" picture is an interpretive overlay (geometry→color), asserted.
- **Constants:** 8 = 3²−1 [count, DERIVED from D2]; 3 colors [count].
- **Status:** PARTIAL (8 gluons DERIVED-given-D2; the color=polarization geometry is asserted).

### EQ-FC-69 — α_s RG running & b₀
- **Equation:** α_s(μ) = α_s(μ₀)/[1+(b₀/2π)α_s ln(μ/μ₀)]; b₀ = 11−2n_f/3 = (33−2n_f)/3; β₀=(33−2n_f)/12π
- **Source:** 10-COUPLING §3.4,§3.8 eqs.(282,355); 10-RUNNING §2.1 eqs.(2.5,2.6); 10-OVERVIEW
- **Spine path:** S0→S1→S2→S6→S7→S8
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S7 Yang–Mills β-function from SU(3) Casimirs (11 gluons, 2n_f/3 quarks); S8 instanton sector. b₀ is a [DERIVED ratio] integer combo from D2. Running grammar; Λ_QCD/anchor are D4/D5.
- **Constants:** b₀ [DERIVED ratio from D2]; 2π,12π [DERIVED ratio]; α_s(M_Z), Λ_QCD [FIT → D5 / D4].
- **Status:** PARTIAL (running+b₀ DERIVED-given-D2; anchor a fit; doc's arithmetic for b₂ wanders, see EQ-FC-77).

### EQ-FC-70 — α_s(M_Z) numerical
- **Equation:** α_s(M_Z) = 4π/(β₀ ln(M_Z²/Λ²_QCD)) ≈ 0.117–0.118 (vs 0.1179)
- **Source:** 10-COUPLING §3.4 eqs.(287–293); 10-RUNNING §3.2
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S2 arithmetic from EQ-FC-69 with Λ_QCD≈200 MeV and n_f=5. Matches data ~1%, but Λ_QCD is fitted (D5) and α_s(M_Z) is used as input elsewhere.
- **Constants:** Λ_QCD, α_s(M_Z) [FIT → D5]; 4π [DERIVED ratio].
- **Status:** PARTIAL (agreement; anchor fitted).

### EQ-FC-71 — Λ_QCD from zone scale
- **Equation:** Λ_QCD ≈ ℏc/η_B ≈ 150 MeV (vs 200–220 MeV, within 30%)
- **Source:** 10-COUPLING §3.5 eqs.(300–306)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → S2 the confinement scale = inverse Firmament thickness ℏc/η_B. η_B is D4/D6. A genuine zone→QCD link, but 30% off and Λ_QCD's exact value still fitted.
- **Constants:** ℏ,c,η_B [SELECTED scale → D4].
- **Status:** PARTIAL (order-of-magnitude link; 30% off).

### EQ-FC-72 — Strong coupling from membrane tension (warp form)
- **Equation:** α_s = (T_color/σ)·e^{−2A₀}; A₀ ≈ ln(M_Firm/M_Planck)
- **Source:** 10-COUPLING §3.3,§3.7 eqs.(265,335,341)
- **Spine path:** S0→S1→S7→S9
- **Decrees:** D1 (6D warp manifold), D2, D4, D6, D5
- **Trace:** 1=1 → S9 warp-suppressed coupling = (color tension/Firmament tension)×warp; the warp factor e^{−2A₀} lives on the 6D manifold (D1, per DECREE rule 2). The e^{−2A₀} is invoked to fix a prior "~20× error" — i.e. a tuning. T_color and A₀ are not derived.
- **Constants:** T_color, σ [SELECTED scale → D4]; e^{−2A₀} [FIT → D5].
- **Status:** PARTIAL (warp-tuned to match; T_color/A₀ undetermined).

### EQ-FC-73 — Confinement barrier potential
- **Equation:** V_boundary(η) = V₀[1+tanh(η/δ_η)], V₀≈1 GeV, δ_η≈1 fm
- **Source:** 10-COUPLING §3.6 eqs.(321)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1 (6D zone manifold), D4, D6
- **Trace:** 1=1 → S6/S9 a phenomenological confining wall at the zone boundary on the 6D manifold (D1, per DECREE rule 2); V₀,δ_η are chosen scales (D4/D6). Model ansatz, not derived.
- **Constants:** V₀, δ_η [SELECTED scale → D4].
- **Status:** PARTIAL (ansatz with chosen parameters).

### EQ-FC-74 — Weak coupling & Weinberg angle (zone asymmetry)
- **Equation:** α_w = g_w²/4π ≈ 0.034; tan(θ_W) ≈ exp(−λ ln(ξ_A/η_B)); sin²θ_W = tan²/(1+tan²) ≈ 0.231
- **Source:** 10-COUPLING §4.1,§4.5 eqs.(390,460,467)
- **Spine path:** S0→S1→S2→S3→S7→S8
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S7 SU(2)×U(1); the mixing angle is *posited* to come from an exponential of the log-scale ratio with a tuned λ≈0.0258 chosen to land on 0.231. The 0.09% "agreement" is a fit: λ is solved backwards from sin²θ_W.
- **Constants:** ξ_A/η_B [DERIVED ratio]; λ≈0.0258 [FIT → D5]; sin²θ_W [DERIVED ratio given λ].
- **Status:** PARTIAL → leans UNTRACEABLE (λ reverse-engineered to fit; see UNTRACEABLE §).

### EQ-FC-75 — Weak coupling from barrier tunneling (failed estimate)
- **Equation:** A ~ exp[−√(2m_e V_B/ℏ²)] ≈ 0.73; α_w ~ |A|² ~ 0.53 (vs 0.033)
- **Source:** 10-COUPLING §4.4 eqs.(438,442,445)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → S6 WKB tunneling amplitude across the zone barrier; gives O(1), "consistent after normalization" — i.e. off by ~16× and hand-waved. Recorded.
- **Constants:** m_e, V_B [SELECTED scale → D4]; α_w [DERIVED ratio, fails by ~16×].
- **Status:** PARTIAL (failed estimate, off by ~16×).

### EQ-FC-76 — Electroweak mixing & Higgs potential
- **Equation:** W³ = sinθ_W A + cosθ_W Z; tanθ_W = g'/g_w; V(H) = −μ²H†H+λ(H†H)²; ⟨H⟩=v≈246 GeV
- **Source:** 10-COUPLING §4.2,§4.6 eqs.(404,410,481); 10-MASS_HIERARCHY §8
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D1 (6D manifold for the S9 warp embedding), D2, D4, D6
- **Trace:** 1=1 → S7 the electroweak mixing rotation (grammar of the gauge basis); the Higgs potential is the standard Mexican hat. The S9 step embeds the Higgs on the 6D manifold (D1, per DECREE rule 2). v is the EW scale (D4). The Genesis claim that v emerges from warp geometry (EQ-FC-86) is separate and weaker.
- **Constants:** v, μ, λ_H [SELECTED scale → D4 / FIT → D5].
- **Status:** DERIVED-as-form (EW mixing); v-origin is PARTIAL (see EQ-FC-86).

### EQ-FC-77 — One-loop β coefficients (SM, with self-corrected arithmetic)
- **Equation:** b_em=41/10, b_w=−19/6, b_s=7 (=11−2n_f/3); b₂=11−n_f/3 attempts corrected to −19/6
- **Source:** 10-RUNNING §2.1,§6, AppB eqs.(2.4,2.10,2.6); 10-COUPLING §5,§6
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D2
- **Trace:** 1=1 → S7 the SM one-loop β coefficients are [DERIVED ratio] integers/rationals from group Casimirs + matter content (D2). The RUNNING doc visibly mis-derives b₂ several times (gets 5/3, then 9, then corrects to −19/6) — the *correct* values are standard, the document's path to them is unreliable.
- **Constants:** 41/10, −19/6, 7 [DERIVED ratio from D2].
- **Status:** DERIVED-given-decrees (values standard; doc's arithmetic shaky).

### EQ-FC-78 — α_em(M_Z) running prediction
- **Equation:** α⁻¹(M_Z) ≈ 134.4 (Genesis 1-loop) vs 127.94 (exp), ~5% off
- **Source:** 10-RUNNING §3.1 eqs.(3.6,3.7); §5.3
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S2 run EQ-FC-65 from membrane scale to M_Z; 5% miss attributed to missing two-loop + thresholds. Honest discrepancy noted.
- **Constants:** b_em [DERIVED ratio]; scales [SELECTED scale → D4].
- **Status:** PARTIAL (5% off; two-loop/threshold gap acknowledged).

### EQ-FC-79 — GUT unification condition & scale
- **Equation:** α₁=α₂=α₃ at E_GUT; ln(E_GUT/M_Z)=2π(α₁⁻¹−α₂⁻¹)/(b₁−b₂); E_GUT ~ 10¹⁰–10¹⁶ GeV
- **Source:** 10-RUNNING §4, AppC eqs.(4.7,4.8,C.3,C.4); 10-COUPLING §5
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S2 equate the three running couplings (EQ-FC-62). The one-loop result gives ~10¹⁰ GeV (admitted "much lower than standard 10¹⁶"); the doc then *asserts* corrections push it to 10¹⁶–10¹⁹. The unification is geometry-motivated but numerically not delivered at one loop.
- **Constants:** b_i [DERIVED ratio]; α_i(M_Z) [FIT → D5]; E_GUT [DERIVED ratio, but 1-loop value wrong].
- **Status:** PARTIAL (condition DERIVED-as-form; predicted scale off by ~6 orders at one loop).

### EQ-FC-80 — α₁ GUT normalization
- **Equation:** g₁ = √(5/3)g'; α₁ = (5/3)α_Y; α₁⁻¹(M_Z) ≈ 59.2
- **Source:** 10-RUNNING §4.1 eqs.(4.5,4.6)
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D2, D4
- **Trace:** 1=1 → S7 the SU(5) hypercharge normalization factor 5/3 is a [DERIVED ratio] from the GUT embedding (D2). Standard.
- **Constants:** 5/3 [DERIVED ratio]; α₁(M_Z) [FIT → D5].
- **Status:** DERIVED-given-decrees.

### EQ-FC-81 — Proton lifetime estimate
- **Equation:** τ_p ~ 1/Γ ~ 10³⁵ yr (at 10¹⁶ GeV) to 10⁴⁵⁻⁵⁰ yr (at 10¹⁹ GeV)
- **Source:** 10-RUNNING §4.3 eqs.(4.12,4.13)
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D2, D4
- **Trace:** 1=1 → S2 dimensional GUT decay-rate estimate Γ~α_GUT²(M_GUT/m_p)²/m_p. Standard GUT order-of-magnitude; depends on the (uncertain) E_GUT.
- **Constants:** α_GUT, M_GUT, m_p [SELECTED scale → D4 / FIT → D5].
- **Status:** PARTIAL (order-of-magnitude; depends on open E_GUT).

### EQ-FC-82 — Membrane Planck scale from tension
- **Equation:** E_Planck = √(σ/(ℏμ)) ≈ 1.22×10¹⁹ GeV (≈1.9×10¹⁹ in one calc)
- **Source:** 10-RUNNING §1.2 eqs.(1.5,1.11,1.12,4.15); 10-COUPLING
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D1 (6D membrane manifold), D4, D6
- **Trace:** 1=1 → S2 dimensional combination of σ,ℏ,μ (membrane elastic constants on the 6D manifold, S9; D1 per DECREE rule 2) giving an energy; matches the GR Planck scale within ~50%. Confirms σ encodes Planck-scale physics, but the agreement is a consistency check on D4 anchors, not a prediction.
- **Constants:** σ, ℏ, μ [SELECTED scale → D4].
- **Status:** PARTIAL (consistency check; ~50% in one variant).

---

## IV. Mass Hierarchy (`10-MASS_HIERARCHY_RESOLUTION.md`)

### EQ-FC-83 — Naive confinement mass (the 1000× problem)
- **Equation:** m₀c² = n_η πℏc/η_B; ground mode ≈ 477 MeV
- **Source:** 10-MASS_HIERARCHY §1 eqs.(in §1.1–1.2)
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S5 confinement KK mass in the η-box (EQ-FC-17 dispersion). 477 MeV ≈ hadronic scale, NOT electron — the recorded "1000× problem" motivating warping. Scale D4.
- **Constants:** ℏ,c,η_B [SELECTED scale → D4]; π, n_η [DERIVED ratio/count].
- **Status:** PARTIAL (negative result; sets up the warp mechanism).

### EQ-FC-84 — Warped Sturm–Liouville eigenvalue problem
- **Equation:** ψ″−γψ′=−λψ; μ_n²=λ_n−γ²/16; m_n c²=ℏc√((nπ/η_B)²+γ²/16) ≈ ℏcγ/4
- **Source:** 10-MASS_HIERARCHY §6 eqs.(6.1–6.3)
- **Spine path:** S0→S1→S3→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S6 the fermion mode equation in the warped η-metric (EQ-FC-60); substitution ψ=e^{γη/4}u reduces to SHM. Eigenvalues spaced at ℏcγ/4. γ²/16, etc. are [DERIVED ratio]; γ is a scale.
- **Constants:** γ, η_B [SELECTED scale → D4]; 1/16, 1/4 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form).

### EQ-FC-85 — Warp suppression / mass hierarchy (Yukawa scaling)
- **Equation:** m_f = m_base·e^{−γη_peak/2}; m_n ∝ exp(−αn²), α≈0.98; γ ≈ 8.2×10¹⁵ m⁻¹
- **Source:** 10-MASS_HIERARCHY §3–§5,§7,§9 eqs.(3.x,5.x,7.x); AXIOM_GODHEAD §3 (OP-03)
- **Spine path:** S0→S1→S2→S6→S8→S9
- **Decrees:** D1, D3 (generation count), D4 (mass scale), D5 (residuals)
- **Trace:** 1=1 → S6 overlap integrals of the three vortex zero-modes (S8, n_w=3⇒n=1,2,3) with the warp measure (S9) give exponentially-split masses. The *form* and count n=1,2,3 are grammar+D3; γ≈8.2×10¹⁵ is *reverse-solved* from m_e (the doc admits η_e>η_B, electron "at/beyond IR boundary"). So mechanism is DERIVED-given-decrees; the parameter γ is fitted.
- **Constants:** n=1,2,3 [count → D3]; α≈0.98, γ [FIT → D5]; mass scale [SELECTED scale → D4].
- **Status:** PARTIAL (mechanism DERIVED-given-decrees; γ fitted, electron mass not cleanly reproduced).

### EQ-FC-86 — Higgs VEV from warp geometry
- **Equation:** v = v₆·e^{A(ξ₀)}; v ≈ 246 GeV requires e^{A(ξ₀)} ~ 0.025–0.25 with chosen v₆
- **Source:** 10-MASS_HIERARCHY §8 eqs.(8.x)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1 (6D warp manifold), D2, D4, D6, D5
- **Trace:** 1=1 → S9 warp-suppressed bulk VEV at the Firmament (the warp e^{A(ξ₀)} lives on the 6D manifold, D1, per DECREE rule 2). The doc offers two scenarios (v₆=1 TeV vs 10 TeV) each with a tuned warp factor chosen to hit 246 GeV — i.e. v is fitted, not predicted. γ_ξ solved backwards.
- **Constants:** v, v₆ [SELECTED scale → D4]; e^{A(ξ₀)}, γ_ξ [FIT → D5].
- **Status:** PARTIAL → leans UNTRACEABLE (v reverse-engineered from a tuned warp; see UNTRACEABLE §).

### EQ-FC-87 — Yukawa coupling & fermion mass
- **Equation:** m_f = y_f v; y_e = m_e/v ≈ 2.1×10⁻⁶
- **Source:** 10-MASS_HIERARCHY §8.6,§9 eqs.(8.x)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S2 standard mass=Yukawa×VEV; y_f from overlap integrals (D5, localization-dependent). y_e is just m_e/v (definitional given both).
- **Constants:** v [SELECTED scale → D4]; y_f [FIT → D5].
- **Status:** PARTIAL (definitional; y_f fitted via localization).

### EQ-FC-88 — Top quark mass estimate
- **Equation:** m_t ≈ y_t v e^{−γη_t/2} ≈ 84 GeV (vs 173; "corrections close the gap")
- **Source:** 10-MASS_HIERARCHY §9.4 eqs.(in §9.4)
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D1 (6D warp manifold), D2, D4, D5
- **Trace:** 1=1 → EQ-FC-85 (which carries D1,D3) with top localization η_t≈0.2η_B on the warped 6D manifold (D1, per DECREE rule 2); gives 84 GeV, off by ~2×, with the shortfall hand-waved to "QCD/radiative/mixing corrections." Recorded.
- **Constants:** y_t, v, γ, η_t [SELECTED scale → D4 / FIT → D5].
- **Status:** PARTIAL (off by ~2×; corrections asserted).

### EQ-FC-89 — Neutrino mass suppression (bulk delocalization + seesaw)
- **Equation:** m_ν ~ m₀ e^{−γη_B/4} ~ 10⁻³ m₀ ~ meV; ½m_ν^bulk ν̄^c ν Majorana term
- **Source:** 10-MASS_HIERARCHY §9.5,§10 eqs.(10.x)
- **Spine path:** S0→S1→S6→S8→S9
- **Decrees:** D1, D3, D4, D5
- **Trace:** 1=1 → S6 overlap of a *delocalized* bulk neutrino (no localizer coupling) with the warp measure gives extra suppression → meV. Order-of-magnitude matches oscillation data; the specific eigenvalues (8.7/9.6/51 meV) are quoted, not derived.
- **Constants:** m₀, γ, η_B [SELECTED scale → D4 / FIT → D5]; e^{−γη_B/4} [DERIVED ratio given γ].
- **Status:** PARTIAL (order-of-magnitude; eigenvalues quoted).

### EQ-FC-90 — γ from 6D cosmological constant
- **Equation:** γ = 2k = 2√(Λ₆/(6M₆⁴))
- **Source:** 10-MASS_HIERARCHY §5.4 eqs.(in §5.4)
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S9 AdS curvature from the bulk Λ₆ (parallels EQ-FC-02). Relates the warp rate to bulk vacuum energy; Λ₆,M₆ are D4. Provides the in-principle origin of γ, but γ's value is still fixed by data (EQ-FC-85).
- **Constants:** Λ₆, M₆ [SELECTED scale → D4]; 2, 1/6 [DERIVED ratio].
- **Status:** PARTIAL (relates γ to Λ₆; both undetermined except by fit).

---

## V. Cosmological Constant, N_A, and Other "Completions" (`10-COMPLETIONS.md`, `10-COMPLETIONS_R4.md`)

### EQ-FC-91 — ℏ from vortex action × warp (COMPLETIONS form)
- **Equation:** ℏ = (πσηB³/c)·(ηB/ξA)^λ, λ≈2; numerically off by ~3× then "refined to 1.055e-34"
- **Source:** 10-COMPLETIONS §1 eqs.(1.3,1.6,1.7); 10-COMPLETIONS_R4 §1 eqs.(1.1,1.3); 10-PLANCK eqs.(2.6,4.12)
- **Spine path:** S0→S1→S6→S8→S9
- **Decrees:** D1, D3, D4, D6
- **Trace:** 1=1 → vortex action (EQ-FC-9) × power-law warp (ηB/ξA)^λ. This is the THIRD/FOURTH ℏ ansatz; the R4 doc visibly flails (tries λ=2,2.5,3,5, base σηB²/c vs σηB³/c) and finally *asserts* "ℏ=1.0546e-34" after the arithmetic fails to converge. Not a clean derivation — the exponent is tuned to the answer.
- **Constants:** σ,ηB,ξA,c [SELECTED scale → D4]; λ,α_warp,β_geom [FIT → D5].
- **Status:** PARTIAL → UNTRACEABLE (the COMPLETIONS/R4 ℏ exponent is fitted by trial; superseded by EQ-FC-10; see UNTRACEABLE §).

### EQ-FC-92 — G from KK reduction (COMPLETIONS form, G₄=G₆/V_extra)
- **Equation:** G₄ = G₆/V_extra; V_extra ~ 10⁶⁰ m² ⇒ G₄ ≈ 6.67×10⁻¹¹; M₄,Pl²=V_extra M₆,Pl⁴
- **Source:** 10-COMPLETIONS §2 eqs.(2.6,2.20); 10-COMPLETIONS_R4 §2; 10-GRAVITATIONAL §3.4
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S6 integrate 6D EH over extra dims → G₄=G₆/V_extra. The value is obtained by *back-solving* V_extra (or M₆) from the observed G₄ — both COMPLETIONS and R4 and the GRAVITATIONAL doc explicitly invert rather than predict (GRAVITATIONAL §6.6 gets 10⁻¹²⁴, off by 10¹¹³; §6.8 inverts to find M₆≈7.8×10⁷ kg). So G is calibration, not derivation.
- **Constants:** G₆, M₆, V_extra [SELECTED scale → D4]; ξ_A,η_B [SELECTED scale → D4].
- **Status:** PARTIAL (form DERIVED; absolute value back-solved, not predicted; raw attempts off by 10⁴⁰–10¹¹³).

### EQ-FC-93 — Avogadro's number as scale ratio
- **Equation:** N_A = R/k_B = 6.022×10²³; N_A = (1 g)/m_u = 10⁻³/(1.66×10⁻²⁷); (L/a₀)³ ~ 10²⁴
- **Source:** 10-COMPLETIONS §4 eqs.(4.1,4.4,4.5); 10-COMPLETIONS_R4 §3 eqs.(3.4,3.8)
- **Spine path:** S0→S1→S2
- **Decrees:** D4
- **Trace:** 1=1 → S2 ratio of macroscopic gram to atomic mass unit; N_A=R/k_B is definitional. The order 10²³–10²⁴ follows from the atomic/macroscopic scale ratio (a₀ from ℏ,m_e,e — D4). Honestly flagged as definitional/conventional, order-of-magnitude only.
- **Constants:** m_u, R, k_B, a₀ [SELECTED scale → D4]; (L/a₀)³ [DERIVED ratio].
- **Status:** PARTIAL (definitional/unit; order-of-magnitude derived).

### EQ-FC-94 — Bohr radius
- **Equation:** a₀ = 4πε₀ℏ²/(m_e e²) ≈ 0.53×10⁻¹⁰ m
- **Source:** 10-COMPLETIONS_R4 §3 eq.(3.6); 10-COMPLETIONS §4.3
- **Spine path:** S0→S1→S2→S4→S5
- **Decrees:** D2, D4
- **Trace:** 1=1 → S5 bound-state radius from balancing Coulomb (S4/D2 EM) and kinetic energy; standard QM. Scales D4; cross-ref chemistry/QM ledgers. Used only to estimate N_A's order.
- **Constants:** ℏ,m_e,e,ε₀ [SELECTED scale → D4]; 4π [DERIVED ratio].
- **Status:** DERIVED-as-form (given D2,D4).

### EQ-FC-95 — Cosmological constant from Waters Above / sustaining coupling
- **Equation:** Λ = 8πG₄ρ_Λ/(3c²) ≈ 1.1×10⁻⁵² m⁻²; Λ ~ 1/ξ_A² ~ 1/(10²⁶)² ~ 10⁻⁵²; V_A = Λ_A const
- **Source:** 10-COMPLETIONS §5 eqs.(5.6,5.11,5.13); cross-ref KK §7.3
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1 (4D/6D manifold for Einstein's eq.), D4, D6
- **Trace:** 1=1 → S6 minimize the Waters-Above potential V_A; its value enters Einstein's eq. (on a manifold, S9 ⇒ D1 per DECREE rule 2) as Λ. The "explanation" Λ~1/ξ_A² is a dimensional coincidence (ξ_A is the Hubble scale by construction, so 1/ξ_A² is the observed Λ by definition — circular). The 10¹²² "resolution" recasts the cc problem as a sustaining-coupling (D6) choice rather than deriving Λ.
- **Constants:** ⟨Ψ_A⟩, ξ_A, G₄ [SELECTED scale → D4]; 8π/3 [DERIVED ratio]; sustaining κ [D6].
- **Status:** PARTIAL (form DERIVED-given-decrees; value tied to D4 via a near-circular identity).

### EQ-FC-96 — Dark-energy equation of state
- **Equation:** w = P_Λ/ρ_Λ = −1 (exact, no evolution); vs observed w = −1.009±0.089
- **Source:** 10-COMPLETIONS §5.8 eqs.(5.12,5.14,5.15)
- **Spine path:** S0→S1→S6
- **Decrees:** D6
- **Trace:** 1=1 → S6 a constant potential V_A (held by the sustaining coupling, D6) gives w=−1 by definition of a cosmological constant. This is a structural claim of the open-system axiom (D6), consistent with data. Not a numerical prediction beyond w=−1.
- **Constants:** none dimensionful; w=−1 [DERIVED-as-form given D6].
- **Status:** DERIVED-as-form (given D6).

### EQ-FC-97 — 6D Planck mass ↔ Newton constant (definitional identity)
- **Equation:** M₆⁴ = 1/(8πG₆); M₆ = 1/√G₆ (in 6D, [G₆]=[M⁻²]); M₆² = ℏc/G₆
- **Source:** 10-GRAVITATIONAL_CONSTANT_DERIVATION §"6D Planck scale" eqs.(boxed, lines 102/116/126/130)
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D1 (6D EH action ⇒ the 6D manifold), D4 (the magnitude of G₆/M₆)
- **Trace:** 1=1 → S9 the 6D Einstein–Hilbert action S=(1/16πG₆)∫√(−g)R fixes the dimension [G₆]=[M⁻²] (D1 supplies the 6-dim manifold, per DECREE rule 2); S2 dimensional algebra then reads off M₆=(8πG₆)^{−1/4} (and M₆²=ℏc/G₆ in ℏ=c≠1 units). Pure definitional rewrite of the 6D coupling as a mass scale; both G₆ and M₆ are dimensionful (D4). Feeds EQ-FC-40/EQ-FC-90/EQ-FC-92 (which use M₆ without first stating this identity).
- **Constants:** G₆, M₆ [SELECTED scale → D4]; 8π, ¼ powers [DERIVED ratio].
- **Status:** DERIVED-as-form (definitional identity; given D1,D4).

---

## UNTRACEABLE / honest gaps

These items cannot be traced to spine + decrees as *derivations*; they are asserted, reverse-engineered, or self-contradictory. Recorded per honesty rule 4.

1. **EQ-FC-11 — k₁ ≈ nuclear/QED boundary "naturalness."** The claim that k₁=1.22 MeV sitting between m_e and the deuteron binding is meaningful is, by the source's own words, "numerology or a genuine connection [that] requires further investigation." No spine path forces k₁ to this scale; it is a downstream consequence of the fitted L_A=83.2η_B. **Reason:** asserted coincidence, no derivation.

2. **EQ-FC-57 / EQ-FC-64 — the α coefficient (b_eff=9.05 / C=1.4383 / 1.44).** Two different files derive the *same* coefficient by *different, mutually inconsistent* routes, and neither is reproducible from its own clean accounting: FINE_STRUCTURE's honest charge-weighted count gives b_eff=16/3≈5.33 (⇒C≈0.85), and the jump to 9.05 is assembled from un-derived "topological/warp/higher-loop" terms (3.67+2+1.4+0.7+0.6); COUPLING's "4π/3π × geometric factor"=1.4383 is an asserted pole residue with the key integral "diverges logarithmically… after proper regularization." The number that makes α=137 work is calibrated to data (C_obs=137.036/95.26=1.438), not derived. **Reason:** the load-bearing dimensionless coefficient is fitted/assembled, not derived; the two derivations disagree on its origin.

3. **EQ-FC-74 / EQ-FC-86 — sin²θ_W and the Higgs VEV from "warp geometry."** Both are reverse-engineered: λ≈0.0258 is solved backwards from sin²θ_W=0.231, and e^{A(ξ₀)} is chosen (with a free v₆) to hit v=246 GeV. The quoted sub-percent "agreements" are tautological fits. **Reason:** free warp parameters tuned to the target; no independent determination.

4. **EQ-FC-91 / EQ-FC-30 — the ℏ numerical coefficient (membrane-ansatz family).** Across OVERVIEW, CONSTANTS_FROM_6D, PLANCK, COMPLETIONS, and COMPLETIONS_R4 there are *four mutually inconsistent* dimensional ansätze for ℏ (σηB²/c, σηB³/2c, σηBξA/4π, and the warp-power family) and the R4 document openly fails to converge, trying λ=2,2.5,3,5 before *asserting* the answer. The honest, reconciled form is the Λ_Z0/β_geom chain (EQ-FC-10), and even that depends on the still-open L_A. **Reason:** the membrane-ansatz ℏ coefficient is fitted by trial and the ansätze contradict each other; only EQ-FC-10 is principled, and it is itself PARTIAL.

**Cross-cutting internal inconsistencies recorded (not separate UNTRACEABLE items, but flagged):**
- G₄ = G₆·V_compact (CONSTANTS_FROM_6D) vs G₄ = G₆/V_extra (GRAVITATIONAL, COMPLETIONS) — opposite exponent sign.
- DOS prefactor 2π² (OVERVIEW) vs π² (COMPLETIONS).
- α coefficient written as 41/10, 4.1, and 8/(3π) in different files for the "same" b_em.
- The GRAVITATIONAL doc's own §4.2 reconciliation note flags its λ=41 volume exponent as a *superseded fitting knob*, NOT the canonical warp index λ=−4/3 — i.e. the G derivation there is self-disavowed.

---

*Exhaustive re-trace, 2026-06-24, replacing the principal-coverage ledger. Schema/decrees per
`README_SCHEMA.md` / `DECREE_REGISTER.md`. 97 equations; per-row Status: 1 UNTRACEABLE, 48 PARTIAL,
12 DERIVED-given-decrees, 36 DERIVED-as-form. (4 documented honest-gap findings span 6 equations — see UNTRACEABLE §.)
Adversarial audit 2026-06-24: added missing D1 to 14 S9-manifold rows (EQ-FC-03,05,06,14,15,21,54,72,73,76,82,86,88,95)
per DECREE rule 2; corrected EQ-FC-15 mislabel (dimensionful c is [SELECTED scale → D4], not [DERIVED ratio]);
added EQ-FC-97 (6D Planck-mass↔G₆ identity, missing from prior coverage); counts above reconciled to reality.*
