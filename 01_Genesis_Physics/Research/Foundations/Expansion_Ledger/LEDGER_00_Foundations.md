# Expansion Ledger — Domain 00: Foundations

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This ledger traces every distinct displayed/numbered equation and named key result in
> `Research/Foundations/` (axiom files, the 6D action, the Waters field equations, the Five
> Principles, KK reduction, warp/metric/coupling derivations) back to the seed `1=1` via the
> spine rungs S0–S9 (`SPINE.md`) plus named decrees D0–D6 (`DECREE_REGISTER.md`). No equation is
> "derived from `1=1` alone": every physics equation = spine path + decrees. Constants are tagged
> `[DERIVED ratio]` / `[SELECTED scale → D4]` / `[FIT → D5]` / `[count → D3]`. Untraceable items
> are recorded with a reason, never fabricated.
>
> Scope note: the root-folder `WATERS_FIELD_EQUATIONS.md` and `FIVE_PRINCIPLES_FORMALIZED.md`
> carry an "ARCHIVED — OBE" banner but are the canonical copies the task note and `README_SCHEMA.md`
> cite (the `00_Archive/` duplicates are skipped). They are traced here. Files in `00_Archive/`,
> `Expansion_Ledger/`, and `EXPANSION_HYPOTHESIS_ANALYSIS.md` are skipped per the honesty rules.

## Header table

| Field | Value |
|-------|-------|
| Domain | Foundations |
| Equations traced | 61 |
| Decrees used across domain | D0, D1, D2, D3, D4, D5, D6 |
| UNTRACEABLE / PARTIAL count | 13 PARTIAL, 3 UNTRACEABLE |

Decree legend (see `DECREE_REGISTER.md`): D0 completed infinity (ℝ); D1 dimension = 6 (and 4D
after reduction); D2 gauge group SU(3)×SU(2)×U(1) / Z₃ orbifold; D3 winding n_w = 3; D4 scale
anchor Λ_Z0, M_{Z0}=M_Pl (every dimensionful magnitude); D5 residual fitted O(1) constants;
D6 architectural axioms (Ψ_A/Ψ_B, Firmament, sustaining source).

---

## I. The Five Governing Principles (`FIVE_PRINCIPLES_FORMALIZED.md`)

### EQ-FND-01 — Energy–momentum conservation (Noether)
- **Equation:** ∂_μ T^μν = 0   (eq. 2.6, 2.11)
- **Source:** FIVE_PRINCIPLES_FORMALIZED.md (eqs. 2.6, 2.11; also WATERS eq. 2.17/(F))
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1 (a manifold to translate along)
- **Trace:** 1=1 → S1 gives the additive "books-balance" form a+(−a)=0 (Conservation) → S6 supplies ∂_μ → S7 (Noether) ties time-translation symmetry of the action to a conserved current; applied to T^μν this is ∂_μ T^μν = 0. Only non-grammar input is D1 (that there is a spacetime to translate in).
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-FND-02 — Canonical energy–momentum tensor
- **Equation:** T^μν = π^μ (∂_ν ψ) − L_total δ^μ_ν   (eq. 2.6)
- **Source:** FIVE_PRINCIPLES_FORMALIZED.md eq. 2.6
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D6 (it is built from the field content L_total of the Waters axioms)
- **Trace:** 1=1 → S6 gives ∂, the Lagrangian and π^μ = ∂L/∂(∂_μψ) → S7 Noether current for translations defines T^μν as the response of L_total to a coordinate shift. D6 fixes which fields enter L_total; D1 supplies the index range.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-FND-03 — Conserved energy / momentum / angular momentum
- **Equation:** E=∫d³x T^00, dE/dt=0; P^i=∫d³x T^0i, dP^i/dt=0; L^i=∫d³x (x×p)^i, dL^i/dt=0   (eqs. 2.7–2.9)
- **Source:** FIVE_PRINCIPLES_FORMALIZED.md eqs. 2.7, 2.8, 2.9
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1
- **Trace:** 1=1 → S7 Noether on EQ-FND-01 for time-, space-translation, and rotation symmetries (S5 gives the rotation group as a member of the derived symmetry family) yields the three conserved integrals. Closed-system boundary condition (Conservation Principle = S1 split + D6 zone closure) makes them global.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-FND-04 — Lorentz transformation
- **Equation:** x′ = γ(x − vt), t′ = γ(t − vx/c²)   (eq. 2.17)
- **Source:** FIVE_PRINCIPLES_FORMALIZED.md eq. 2.17
- **Spine path:** S0→S1→S3→S4→S6→S9
- **Decrees:** D1, D4 (c sets the unit relating x and t), D6 (the Firmament wave operator whose invariance is required)
- **Trace:** 1=1 → S3/S4 build ℝ and the invariant quadratic form; S6 supplies the d'Alembertian wave operator □ (the Firmament oscillation equation, EQ-FND-40); requiring that operator to be form-invariant selects the linear maps preserving x²−c²t². D1 gives the 3+1 split; D4 fixes c; D6 supplies the membrane whose wave operator is the symmetry's origin (the "smuggled" physical input made explicit).
- **Constants:** c [SELECTED scale → D4]; γ=(1−v²/c²)^{−1/2} [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FND-05 — Shannon/Boltzmann entropy
- **Equation:** S = −k_B Σ_i p_i ln p_i   (eq. 5.2)
- **Source:** FIVE_PRINCIPLES_FORMALIZED.md eq. 5.2
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D0 (real-valued log), D4 (k_B sets the entropy unit)
- **Trace:** 1=1 → S2 gives ratios/probabilities p_i and the log via S3 limits; counting microstates and weighting by −ln gives S. k_B is the unit conversion (D4). The Second-Law inequality dS/dt≥0 (eq. 5.1) is the Degradation Principle, a dynamical statement tied to D6 (open-system/curse), not forced by grammar.
- **Constants:** k_B [SELECTED scale → D4].
- **Status:** PARTIAL (functional form DERIVED-given-decrees; dS/dt≥0 rests on D6, see EQ-FND-30..32).

### EQ-FND-06 — Bekenstein–Hawking entropy
- **Equation:** S_BH = (k_B c³/4Għ) A   (eq. 5.17)
- **Source:** FIVE_PRINCIPLES_FORMALIZED.md eq. 5.17
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4
- **Trace:** 1=1 → S9 supplies the horizon (a curvature/manifold structure, D1) → the area A and the combination c³/(Għ) are read off the Einstein equation (EQ-FND-18). Cited as an imported standard result; the 1/4 coefficient is from semiclassical gravity, not re-derived here.
- **Constants:** k_B, c, G, ħ [each SELECTED scale → D4]; 1/4 [DERIVED ratio, imported].
- **Status:** PARTIAL (form cited; coefficient not derived in-framework).

### EQ-FND-07 — Total Lagrangian density (Five-Principles form)
- **Equation:** L_total = L_membrane + L_A + L_B + L_matter + L_int, with L_int = −G_int Ψ_A Ψ_B and V_A,V_B quartic   (eqs. 10.1–10.2)
- **Source:** FIVE_PRINCIPLES_FORMALIZED.md eqs. 10.1, 10.2
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D6 (Ψ_A/Ψ_B/Firmament field content), D4 (m_A,m_B,σ,G_int), D2 (U(1)/CPT symmetry constraint on allowed terms)
- **Trace:** 1=1 → S6 gives kinetic (∂ψ)² and S2 gives polynomial self-interaction; S7 symmetry (CPT/U(1)) forbids odd cross-terms and forces the paired Ψ_A↔Ψ_B coupling. D6 injects the existence of the two Waters fields and the membrane; D4 sets all dimensionful couplings.
- **Constants:** σ, m_A, m_B, λ_A, λ_B, G_int [each SELECTED scale → D4]. (Note: superseded by complex-Ψ_A form — see EQ-FND-12.)
- **Status:** DERIVED-given-decrees (legacy real-Ψ_A convention).

---

## II. The Waters Field Equations (`WATERS_FIELD_EQUATIONS.md`)

### EQ-FND-08 — Unperturbed 6D line element
- **Equation:** ds₀² = −c²dt² + a²(t)[dx²+dy²+dz²] + b²(t)dξ² + d²(t)dη²   (eq. 1.1)
- **Source:** WATERS_FIELD_EQUATIONS.md eq. 1.1 (also AXIOM_6D_SPACETIME.md metric)
- **Spine path:** S0→S1→S3→S5→S9
- **Decrees:** D1 (six dimensions), D4 (c and the scale factors)
- **Trace:** 1=1 → S5 grants independent directions of expansion (dimension as a count) → D1 fixes that count at 6 → S9 equips ℝ⁶ with a Lorentzian metric. The split into (4D) + (ξ,η) is the zone architecture (D6).
- **Constants:** c [SELECTED scale → D4]; a,b,d(t) profiles [SELECTED scale → D4]; dimension = 6 [count → D1] (the dimension count is the D1 decree per DECREE_REGISTER rule 2 — NOT D3, which selects the winding n_w=3).
- **Status:** DERIVED-given-decrees (D1, D4, D6).

### EQ-FND-09 — Firmament (Nambu–Goto) action, weak-field
- **Equation:** S_membrane = (σ/2)∫d⁴x√(−g⁽⁰⁾)(∂_μη ∂^μη + ∂_μξ ∂^μξ) + const   (eqs. 1.4→1.7)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 1.4, 1.6, 1.7
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6 (the Firmament exists), D4 (σ)
- **Trace:** 1=1 → S9 gives the induced metric √(−g_ind) of an embedded surface → S6 expands the area functional to quadratic order, the leading term constant, the next the kinetic term. D6 posits the membrane; D4 sets its tension σ.
- **Constants:** σ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-FND-10 — Total action functional (Waters form)
- **Equation:** S_total = S_membrane + S_A + S_B + S_interaction + S_matter   (eq. 1.3 / 1.29)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 1.3, 1.29
- **Spine path:** S0→S1→S2→S6→S7→S9
- **Decrees:** D6, D4, D1
- **Trace:** Same construction as EQ-FND-07 but with the matter and membrane sectors written explicitly on the 6D manifold (D1). The action principle δS=0 is the borderline-DERIVED S6 step.
- **Constants:** all couplings [SELECTED scale → D4].
- **Status:** DERIVED-as-form (δS=0 borderline) given D1, D4, D6.

### EQ-FND-11 — Gravity / Firmament-curvature equation (Poisson & wave form)
- **Equation:** □η = −4πG ρ_matter   (eq. 2.2→2.4 / (A) / 3.1)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 2.2–2.4, 3.1
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6 (η is the Firmament displacement field), D4 (G)
- **Trace:** 1=1 → S6 gives the d'Alembertian □ → varying the membrane action (EQ-FND-09) plus the matter source gives σ∇²η = ρ_matter; identifying G ≡ σ/(4πμc²) recasts it as □η = −4πGρ. D6 supplies η; D4 supplies G via membrane constants.
- **Constants:** G [SELECTED scale → D4]; 4π [DERIVED ratio]; the identification G=σ/(4πμc²) is structural.
- **Status:** DERIVED-given-decrees.

### EQ-FND-12 — Waters Above EOM (dark energy)
- **Equation:** □Ψ_A + m_A²Ψ_A + (λ_A/3!)Ψ_A³ + G_int Ψ_B = 0   (eq. 2.5 / (B) / 3.2). Canonical complex form: □₆Ψ_A − ∂V_A/∂Ψ_A* − G_int Ψ_A Ψ_B = 0 (ACTION_6D §10.2).
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 2.5, 3.2; ACTION_6D_COMPLETE.md §10.2
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D6 (Ψ_A exists), D4 (m_A, λ_A, G_int), D2 (U(1)_A phase symmetry fixing the |Ψ_A|²Ψ_B coupling)
- **Trace:** 1=1 → S6 gives □; S2 gives the polynomial potential terms; varying L_A+L_int (EQ-FND-07/10) by Euler–Lagrange yields the EOM. S7/D2 U(1)_A invariance selects the corrected multiplicative coupling. D6 posits Ψ_A; D4 fixes the masses/couplings.
- **Constants:** m_A, λ_A, G_int [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-FND-13 — Waters Below EOM (dark matter)
- **Equation:** □Ψ_B − m_B²Ψ_B − (λ_B/3!)Ψ_B³ − G_int Ψ_A = −ρ_matter   (eq. 2.7 / (C) / 3.3)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 2.7, 3.3
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D6, D4
- **Trace:** Same Euler–Lagrange construction as EQ-FND-12 for the L_B sector, with sign-flipped (confining) mass term and ρ_matter as the condensation sink. D6 supplies Ψ_B and the matter-as-condensate picture; D4 the couplings.
- **Constants:** m_B, λ_B, G_int [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-FND-14 — 4D Einstein field equation (effective)
- **Equation:** G_μν + Λ_eff g_μν = (8πG/c⁴)[T_μν^matter + T_μν^A + T_μν^B]   (eq. 2.11 / (D) / 3.4)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 2.10, 2.11, 3.4
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S9 gives curvature R, the Einstein tensor G_μν, and the metric g_μν → varying the Einstein–Hilbert + matter action (S6 δS=0) by g_μν yields the field equation. D1 fixes 4D after reduction; D4 fixes G and c⁴; D6 supplies the Waters stress-energy sources.
- **Constants:** G, c [SELECTED scale → D4]; 8π [DERIVED ratio].
- **Status:** DERIVED-as-form (δS=0 borderline) given D1, D4, D6.

### EQ-FND-15 — Waters stress-energy tensors
- **Equation:** T_μν^{A,B} = ∂_μΨ ∂_νΨ − ½g_μν[g^{ρσ}∂_ρΨ∂_σΨ + V(Ψ)]   (eqs. 2.14, 2.15)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 2.14, 2.15; ACTION_6D §10.1 (complex Ψ_A form)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6, D4
- **Trace:** 1=1 → S6/S9 give T_μν = −(2/√−g)δ(√−g L)/δg^μν; applied to the scalar Lagrangian this is the standard scalar stress tensor. D6 supplies the fields; D4 their potentials.
- **Constants:** masses in V [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-FND-16 — Matter continuity equation
- **Equation:** ∂ρ_matter/∂t + ∇·(ρ_matter u) = 0   (eq. 2.18 / (E) / 3.5)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 2.18, 3.5
- **Spine path:** S0→S1→S6
- **Decrees:** D1, D6
- **Trace:** 1=1 → S1 conservation form a+(−a)=0 applied to a density → S6 local form ∂ρ + ∇·(ρu) = 0 is the divergence of the matter current, a corollary of ∇_μT^μν=0 (EQ-FND-01). D6 identifies ρ_matter as condensed Waters Below.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-FND-17 — de Sitter / Hubble equilibrium of Waters Above
- **Equation:** Λ_eff = (8πG/3)ρ_A^vac ≈ (2πGλ_A/3)v_A⁴; a(t)=a₀e^{Ht}, H²=Λ_eff/3   (eqs. 4.7, 4.8 / 6.11–6.12)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 4.6–4.8, 6.8–6.12
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D4, D6
- **Trace:** 1=1 → setting δΨ_A=0 in EQ-FND-12 gives the VEV v_A → its potential energy V(v_A) enters EQ-FND-14 as a constant Λ_eff → the FLRW Friedmann equation H²=Λ_eff/3 (S9 + S6) integrates to exponential expansion. D6 supplies the VEV mechanism; D4 the couplings.
- **Constants:** G, λ_A [SELECTED scale → D4]; v_A [SELECTED scale → D4]; factors 8π/3, 2π/3 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FND-18 — Schwarzschild metric
- **Equation:** ds² = −c²(1−2GM/c²r)dt² + (1−2GM/c²r)⁻¹dr² + r²dΩ²   (eq. 6.7)
- **Source:** WATERS_FIELD_EQUATIONS.md eq. 6.7
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4
- **Trace:** 1=1 → S9 vacuum Einstein equation R_μν=0 (from EQ-FND-14 with T=0) → the unique static spherically-symmetric solution. Cited as a standard GR result, not re-derived. r_s=2GM/c².
- **Constants:** G, c [SELECTED scale → D4]; 2 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1, D4), solution imported.

### EQ-FND-19 — Yukawa screening of Waters Below
- **Equation:** Ψ_B(r) ∝ e^{−m_B r}/r   (eqs. 2.9, 4.13)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 2.9, 4.12, 4.13
- **Spine path:** S0→S1→S6
- **Decrees:** D6, D4
- **Trace:** 1=1 → S6 static limit of EQ-FND-13, (∇²−m_B²)Ψ_B = −source → the spherically-symmetric Green's function of the massive Helmholtz operator is the Yukawa form. D6 gives Ψ_B; D4 gives m_B (the screening length 1/m_B).
- **Constants:** m_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-FND-20 — NFW dark matter profile
- **Equation:** ρ_B(r) ∝ 1/[r(1+r/r_s)²]   (eqs. 6.20, 10.x)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 6.18–6.20
- **Spine path:** S0→S1→S6
- **Decrees:** D6, D4, D5 (r_s matched to halo data)
- **Trace:** 1=1 → S6 back-reaction of EQ-FND-13 in a halo with the 1/r outer Ψ_B solution gives the NFW form. The scale radius r_s is fit to observation.
- **Constants:** r_s [FIT → D5].
- **Status:** PARTIAL (functional form DERIVED-given-decrees; r_s is a fit).

### EQ-FND-21 — Gravitational-wave (membrane perturbation) equation
- **Equation:** □δη = 0; □h^TT_μν = −(16πG/c⁴)T^TT_μν; h^TT_ij = (4G/c⁴)(1/r)Q̈_ij(t−r/c)   (eqs. 5.2, 5.13, 5.14)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 5.1–5.4, 5.11–5.15
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4
- **Trace:** 1=1 → S6 linearizing EQ-FND-11/14 about flat space gives the source-free wave equation □δη=0 and the TT quadrupole formula. D1 supplies the 4D index structure; D4 supplies G,c. Propagation speed = c (from EQ-FND-40).
- **Constants:** G, c [SELECTED scale → D4]; 4, 16π [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FND-22 — Jeans growth / structure-formation rate
- **Equation:** d²δρ/dt² + 2H(dδρ/dt) = 4πGρ₀δρ; λ_J = π√(c_s²/Gρ₀)   (eqs. 5.7, 5.8, 6.13–6.14)
- **Source:** WATERS_FIELD_EQUATIONS.md eqs. 5.7, 5.8, 6.13–6.16
- **Spine path:** S0→S1→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → S6 linearized continuity + Poisson (EQ-FND-11,16) in an expanding background gives the perturbation growth equation; the Jeans length follows from balancing pressure against gravity. D4 supplies G; D6 the matter content.
- **Constants:** G [SELECTED scale → D4]; c_s [SELECTED scale → D4]; 2,4π,π [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

---

## III. The 6D Master Action (`ACTION_6D_COMPLETE.md`)

### EQ-FND-23 — Master 6D action functional
- **Equation:** S_total = S_grav + S_Firm + S_waters + S_gauge + S_matter + S_interaction + S_sustaining
- **Source:** ACTION_6D_COMPLETE.md §2 (boxed)
- **Spine path:** S0→S1→S2→S6→S7→S9
- **Decrees:** D1, D2, D3, D6, D4
- **Trace:** 1=1 → the full ladder: S6 (action/variation), S7 (gauge symmetry), S9 (curvature/manifold) assemble the standard sector list; each sector injects a decree — gravity/manifold D1, gauge D2, fermion-winding D3, Waters/Firmament/sustaining D6, all scales D4. This is the union of EQ-FND-24..29.
- **Constants:** all couplings [SELECTED scale → D4].
- **Status:** DERIVED-as-form (δS=0 borderline) given D1, D2, D3, D4, D6.

### EQ-FND-24 — 6D Einstein–Hilbert action
- **Equation:** S_grav = (1/2κ₆²)∫_{M⁶}d⁶x√(−g₆)R₆ + S_boundary, κ₆²=8πG₆   (§3.1)
- **Source:** ACTION_6D_COMPLETE.md §3.1; OP_G6_KAPPA6 (G6.1)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4
- **Trace:** 1=1 → S9 supplies R₆ on a 6D manifold (D1) → the Einstein–Hilbert scalar is the unique lowest-order diffeomorphism-invariant action density. S_boundary is the Gibbons–Hawking–York term. D4 sets G₆.
- **Constants:** G₆ (κ₆²) [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D4).

### EQ-FND-25 — Firmament localized-source action
- **Equation:** S_Firm = ∫d⁶x√(−g₆)[σ_Firm δ(ξ−ξ₀)δ(η−η₀) + κ_B H² δ(...)]   (§4.4)
- **Source:** ACTION_6D_COMPLETE.md §4.1–4.4
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6, D4, D1
- **Trace:** 1=1 → S9 induced-metric/extrinsic-curvature structure of an embedded brane → after the dimensional-consistency correction the brane is a localized δ-source with tension σ_Firm and Helfrich bending κ_B H². D6 posits the membrane; D4 the tensions.
- **Constants:** σ_Firm, κ_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (dimensional caveats noted in source).

### EQ-FND-26 — Waters Lagrangian (canonical complex-Ψ_A form)
- **Equation:** L_waters = −g^{AB}∂_AΨ_A*∂_BΨ_A − V_A(|Ψ_A|) − ½g^{AB}∂_AΨ_B∂_BΨ_B − V_B(Ψ_B) − G_int|Ψ_A|²Ψ_B   (§5.1 eq. 5.x)
- **Source:** ACTION_6D_COMPLETE.md §5.1
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D6, D4, D2 (U(1)_A invariance)
- **Trace:** 1=1 → S4 phase of ℂ gives the U(1)_A symmetry → S6 kinetic + S2 polynomial potentials, restricted by S7/D2 to U(1)_A-invariant terms → the lowest-order invariant cross-coupling is |Ψ_A|²Ψ_B. D6 supplies the fields; D4 the scales.
- **Constants:** G_int, V_A/V_B parameters [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-FND-27 — Waters Below VEV and equation of state
- **Equation:** ⟨Ψ_B⟩ = √(6μ_B²/λ_B) = v_B; ρ_B = μ_B⁴/(12λ_B); w_B ≈ 0   (§5.3)
- **Source:** ACTION_6D_COMPLETE.md §5.3
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D6, D4
- **Trace:** 1=1 → S2 quartic potential −½μ_B²Ψ²+ (λ_B/4!)Ψ⁴ has a minimum at v_B=√(6μ_B²/λ_B) (algebra of the stationarity condition) → its depth gives ρ_B. D6 supplies Ψ_B; D4 the parameters.
- **Constants:** μ_B, λ_B [SELECTED scale → D4]; 6,12 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FND-28 — Gauge sector field strengths (U(1), SU(2), SU(3))
- **Equation:** S_gauge = −¼∫√(−g₆)F²; F_μν^{(W)} = ∂_μA_ν^{(W)} − ∂_νA_μ^{(W)} − ig_W[A_μ,A_ν]   (§6)
- **Source:** ACTION_6D_COMPLETE.md §6.1–6.2
- **Spine path:** S0→S1→S4→S7
- **Decrees:** D2 (which gauge group), D1, D4
- **Trace:** 1=1 → S4 gives U(1) phase for free; S7 gives the derived SU(N) family; D2 selects SU(3)×SU(2)×U(1) and the non-abelian commutator term. The fields arise as off-diagonal metric/KK modes (D1). D4 sets g_W.
- **Constants:** g_W, g_s [SELECTED scale → D4 / running, see EQ-FND-58]; ¼ [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D1, D2, D4).

### EQ-FND-29 — 6D Dirac matter action and equation
- **Equation:** S_matter = ∫√(−g₆)Ψ̄(iγ^A e_A^M D_M − m)Ψ; EOM (iγ^A e_A^M D_M − m)Ψ = 0   (§7.1, §10.3)
- **Source:** ACTION_6D_COMPLETE.md §7.1, §10.3
- **Spine path:** S0→S1→S4→S7→S9
- **Decrees:** D1, D3 (winding ⇒ generation count), D4, D6
- **Trace:** 1=1 → S4 (ℂ, square root of −1) and S9 (vielbein/spin connection) give the Clifford algebra {γ^A,γ^B}=2g^{AB} and the Dirac operator → varying Ψ̄ gives the Dirac equation. D1 fixes 6D spinor dimension; D3 (n_w=3) sets how many 4D generations the zero modes give (see EQ-FND-52); D4 the mass.
- **Constants:** m [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-FND-30 — Yukawa mass generation
- **Equation:** S_Yukawa = ∫√(−g₆) y Ψ̄ Ψ_A Ψ; m_eff = y v_A   (§7.3)
- **Source:** ACTION_6D_COMPLETE.md §7.3
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D6, D4, D5 (y matched to data)
- **Trace:** 1=1 → S7 gauge/Lorentz-invariant cubic coupling ȲΨ_AΨ → when Ψ_A acquires VEV v_A (D6), the term becomes a mass m_eff=yv_A. The dimensionless Yukawa y is calibrated to the observed mass (D5).
- **Constants:** v_A [SELECTED scale → D4]; y [FIT → D5].
- **Status:** PARTIAL (mechanism DERIVED-given-decrees; y is a fit).

### EQ-FND-31 — 6D Einstein equations and Waters EOMs (from variation)
- **Equation:** G_AB = κ₆²T_AB^total; □₆Ψ_A − ∂V_A/∂Ψ_A* − G_intΨ_AΨ_B = 0; □₆Ψ_B + μ_B²Ψ_B − (λ_B/6)Ψ_B³ − G_int|Ψ_A|² = 0   (§10.1–10.2)
- **Source:** ACTION_6D_COMPLETE.md §10.1, §10.2
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → δS_total=0 (S6) by g_AB gives the 6D Einstein equation; by Ψ_A*,Ψ_B gives the bulk wave equations. These are the 6D parents of EQ-FND-12/13/14. D1,D4,D6 as above.
- **Constants:** κ₆², μ_B, λ_B, G_int [SELECTED scale → D4].
- **Status:** DERIVED-as-form (δS=0 borderline) given D1, D4, D6.

---

## IV. Axioms — Open System, Sustaining, Metric Discontinuity, Fall

### EQ-FND-32 — Open-system entropy balance
- **Equation:** dS_total = dS_irreversible + dS_exchange, with dS_exchange = δQ/T + δS_external; phase values dS_total/dt {<0, =0, >0, ≤0}   (AXIOM_OPEN_SYSTEM §"Mathematical Formalism")
- **Source:** AXIOM_OPEN_SYSTEM.md (entropy balance); FIVE_PRINCIPLES eqs. 5.1, 6.16
- **Spine path:** S0→S1→S6
- **Decrees:** D6 (the open-system/external source axiom)
- **Trace:** 1=1 → S1 split a+(−a) lets total entropy separate into internal + exchange terms; the Clausius inequality dS_irr≥0 is the S6 dynamical form. The decisive content — that δS_external≠0 (an external Creator term) — is NOT grammar; it is the D6 architectural axiom. Phase signs are decreed boundary conditions.
- **Constants:** none dimensionful (rates phase-dependent).
- **Status:** PARTIAL — the balance form is S1/S6; the external-source term and its sign per phase are D6 axioms, not derived.

### EQ-FND-33 — Sustaining-coupling field equation
- **Equation:** □₆κ + m_κ²κ = 0 (bulk); κ|_{ξ₀}=κ_source(t)   (AXIOM_SUSTAINING_COUPLING §2.1)
- **Source:** AXIOM_SUSTAINING_COUPLING.md §2.1–2.2
- **Spine path:** S0→S1→S6
- **Decrees:** D6 (κ exists as boundary-sourced field), D4 (m_κ)
- **Trace:** 1=1 → S6 massive Klein–Gordon operator □+m² is the generic free-field equation; D6 posits κ as a scalar carrying the Creator's sustaining input with a Dirichlet boundary source. D4 sets m_κ (Compton range ≥ Hubble).
- **Constants:** m_κ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (the field's existence is the D6 axiom).

### EQ-FND-34 — κ-coupled Waters source equations
- **Equation:** □₆Ψ_A + V′(Ψ_A) = κ(x^A)J_A(ξ); □₆Ψ_B + M_B²Ψ_B = κ(x^A)J_B(η); □₆κ + m_κ²κ = J_AΨ_A + J_BΨ_B   (AXIOM_SUSTAINING_COUPLING §6.2; SUSTAINING_COUPLING.md)
- **Source:** AXIOM_SUSTAINING_COUPLING.md §6.2 (and §2.3)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D6, D4
- **Trace:** 1=1 → S6 variation of the extended action S_grav+S_waters+S_κ (S_κ = ½(∂κ)²−½m_κ²κ²+κ(J_AΨ_A+J_BΨ_B)) gives the three coupled EOMs. D6 supplies κ, J_A, J_B; D4 the masses.
- **Constants:** m_κ, M_B, J normalizations A₀,B₀ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-FND-35 — Phase-dependent decay-rate law
- **Equation:** λ_Phase3 ≈ λ₀(1 − κ_partial/κ_full) = λ₀ Δκ/κ_full; ε ≡ Δκ/κ_full ~ 10⁻²⁷–10⁻⁶⁰   (§3.3, §4.1, §5.4)
- **Source:** AXIOM_SUSTAINING_COUPLING.md §3.3, §4.1, §5.1–5.4
- **Spine path:** S0→S1→S2
- **Decrees:** D6 (κ phases), D5 (ε fixed by matching observed decay rates)
- **Trace:** 1=1 → S2 ratio Δκ/κ_full → expanding the κ-modulated tunneling integral (Gamow form, imported) to leading order gives λ ∝ ε. The numerical ε is not derived; it is back-solved from the measured ¹⁴C half-life (D5).
- **Constants:** λ₀ [SELECTED scale → D4]; ε [FIT → D5]; κ_full/κ_partial values [SELECTED → D4].
- **Status:** PARTIAL (linear-in-ε form derived; ε and κ-phase magnitudes are fits/decrees).

### EQ-FND-36 — Sabbath-boundary metric junction conditions
- **Equation:** [g_μν]₊₋ = 0, [K_μν]₊₋ ≠ 0; H_creation ≈ 3×10¹⁴ H₀   (AXIOM_METRIC_DISCONTINUITY)
- **Source:** AXIOM_METRIC_DISCONTINUITY.md §"Mathematical Formalism"
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6 (the metric phase transition / Sabbath boundary), D4 (H₀, the ratio)
- **Trace:** 1=1 → S9 Israel junction conditions for a hypersurface (continuous metric, discontinuous extrinsic curvature) are standard GR (S6/S9). The existence of the Sabbath boundary and the factor ≈3×10¹⁴ are D6/D4 decreed inputs, not derived.
- **Constants:** H₀ [SELECTED scale → D4]; 3×10¹⁴ [FIT/decreed → D5/D6].
- **Status:** PARTIAL (junction form DERIVED; the transition and its magnitude are decreed).

### EQ-FND-37 — Friedmann coordinate-time integral
- **Equation:** t_coord = ∫₀^∞ dz/[(1+z)H(z)] ≈ 13.8 Gyr   (AXIOM_METRIC_DISCONTINUITY)
- **Source:** AXIOM_METRIC_DISCONTINUITY.md §"The Time Mapping"
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S9 FLRW metric + S6 integral of 1/(aH) is standard cosmology; the value follows from the measured H(z). The reinterpretation as "sustaining-mode coordinate time" is a D6 framing, not a new equation.
- **Constants:** H(z) parameters [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (standard integral; framing is D6).

### EQ-FND-38 — Fall phase-transition order parameter
- **Equation:** η_curse = dS_curse/dt; Phase2: η_curse=0, Phase3: η_curse>0; dS_total/dt = dS_diss/dt + dS_sust/dt + dS_curse/dt   (AXIOM_PHASE_TRANSITION_FALL)
- **Source:** AXIOM_PHASE_TRANSITION_FALL.md §"Order Parameter"
- **Spine path:** S0→S1→S6
- **Decrees:** D6
- **Trace:** 1=1 → S1/S6 give the additive entropy-rate decomposition; the curse term dS_curse and its first-order (discontinuous) onset are the D6 axiom (the Fall). No grammar forces a third entropy channel — it is decreed.
- **Constants:** none dimensionful.
- **Status:** PARTIAL — decomposition is S1/S6; the curse term is a D6 axiom.

---

## V. Membrane Mechanics & Constants (`AXIOM_MEMBRANE_MECHANICS_v2.md`)

### EQ-FND-39 — Speed of light from membrane (c² = σ/μ)
- **Equation:** c² = σ/μ
- **Source:** AXIOM_MEMBRANE_MECHANICS_v2.md §"Statement"/§5; also WATERS eq. 6.6, KK eq. 6.10
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6 (the Firmament is an elastic membrane), D4 (σ, μ set the unit of c)
- **Trace:** 1=1 → S6 wave equation on an elastic medium has transverse-wave speed v²=tension/density (classical result) → identifying the Firmament tension σ and density μ gives c²=σ/μ. D6 supplies the membrane; D4 supplies σ,μ (hence the magnitude of c).
- **Constants:** σ, μ [SELECTED scale → D4]; c [DERIVED ratio from σ,μ].
- **Status:** DERIVED-given-decrees.

### EQ-FND-40 — Firmament wave operator / Lorentz symmetry origin
- **Equation:** □φ = (1/c²)∂²φ/∂t² − ∇²φ = 0
- **Source:** AXIOM_MEMBRANE_MECHANICS_v2.md §"Why c Is Invariant"
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6, D4
- **Trace:** 1=1 → S6 the membrane oscillation equation is the d'Alembertian wave equation; the coordinate transformations preserving it are exactly the Lorentz group (EQ-FND-04). D6 supplies the membrane; D4 the speed c.
- **Constants:** c [SELECTED scale → D4 (via σ,μ)].
- **Status:** DERIVED-given-decrees.

### EQ-FND-41 — Gravitational constant from membrane stiffness
- **Equation:** G = c⁴/(8πσℓ_eff²)
- **Source:** AXIOM_MEMBRANE_MECHANICS_v2.md §3; L_EFF_DERIVATION.md
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D6, D4
- **Trace:** 1=1 → S6 weak-field membrane bending □δh ~ ρ/σ compared with the linearized Einstein equation □h ~ 8πG T identifies G ∝ 1/σ, with a geometric factor ℓ_eff² restoring dimensions. D6 supplies the membrane; D4 supplies σ; ℓ_eff is then fixed by G,σ,c.
- **Constants:** σ, c [SELECTED scale → D4]; ℓ_eff [DERIVED ratio = √(c⁴/8πσG)]; 8π [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FND-42 — Effective coupling length L_eff
- **Equation:** L_eff² = c⁴/(8πσG) = V_extra,eff = ∫∫ e^{2A+2B}dξdη ≈ 8.0×10⁻⁵⁷ m²
- **Source:** L_EFF_DERIVATION.md §2.3, §3 (and AXIOM_MEMBRANE_MECHANICS_v2 §3)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → invert EQ-FND-41 for ℓ_eff; independently it equals the warp-weighted extra-dimensional volume from KK reduction (EQ-FND-49). D1 supplies the extra dimensions; D4 the constants. Note source flags the geometric volume integral does NOT yet reproduce the numerical value from first principles (Phase 0 gap).
- **Constants:** c,σ,G [SELECTED scale → D4]; L_eff [DERIVED ratio].
- **Status:** PARTIAL (algebraic identity exact; geometric derivation of the value open).

### EQ-FND-43 — 6D dispersion / rest-mass relation
- **Equation:** m₀²c⁴ = (p_ξ c)² + (p_η c)² + (E_bind)², p_ξ = 2πħn_ξ/ξ_A   (§4)
- **Source:** AXIOM_MEMBRANE_MECHANICS_v2.md §4
- **Spine path:** S0→S1→S4→S5→S9
- **Decrees:** D1, D4
- **Trace:** 1=1 → S9 6D energy-momentum invariant E²=Σ(p_ic)²+(mc²)² → for a 3-space rest state the mass comes from confined ξ,η momenta (S5 modes quantized 2πħn/L). D1 supplies the extra dimensions; D4 the scales ξ_A,η_B.
- **Constants:** ħ,c,ξ_A,η_B [SELECTED scale → D4]; n_ξ,n_η [count] (generic KK mode quantum numbers from S5 — these are *free* integer labels, NOT the decreed winding n_w=3, so they do NOT invoke D3; D3 selects only the single fixed generation winding); 2π [DERIVED ratio].
- **Status:** DERIVED-given-decrees (mode framework); specific masses remain open (see EQ-FND-30).

---

## VI. KK Dimensional Reduction (`KK_DIMENSIONAL_REDUCTION.md`)

### EQ-FND-44 — 6D KK metric ansatz
- **Equation:** ds² = e^{2A}g̃_μν dx^μdx^ν + e^{2B}(dξ²+dη²) + 2A_μ^ξ dx^μdξ + 2A_μ^η dx^μdη   (eq. 1.1)
- **Source:** KK_DIMENSIONAL_REDUCTION.md eq. 1.1
- **Spine path:** S0→S1→S5→S9
- **Decrees:** D1, D2 (off-diagonal modes → gauge fields), D4
- **Trace:** 1=1 → S5/S9 build the 6D metric with the most general 4D-Poincaré-invariant warped form; the off-diagonal g_μa become KK gauge potentials. D1 fixes 6 dimensions; D2 their interpretation as SM gauge fields; D4 the warp scales.
- **Constants:** warp parameters A₀,B₀,λ,γ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-FND-45 — 6D Ricci scalar (reduced)
- **Equation:** R₆ = e^{−2A}R̃₄ − 2e^{−2A}□̃A − 3e^{−2A}(∂A)² − … + e^{−2A}[¼F²] + …   (eq. 2.6, boxed)
- **Source:** KK_DIMENSIONAL_REDUCTION.md eq. 2.6
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1
- **Trace:** 1=1 → S9 the Ricci scalar of the ansatz EQ-FND-44 is a fixed differential-geometric computation (Christoffel→Riemann→Ricci, eqs. 2.1–2.5). No new decree beyond D1 (the manifold).
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).

### EQ-FND-46 — 4D Newton constant from extra-dim volume
- **Equation:** κ₄² = κ₆²/V_extra ⇒ G₄ = G₆/V_extra   (eq. 3.4, boxed)
- **Source:** KK_DIMENSIONAL_REDUCTION.md eq. 3.4; AXIOM_MEMBRANE_MECHANICS_v2 §2; OP_G6 (G6.12)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4
- **Trace:** 1=1 → integrating EQ-FND-24 over ξ,η factors √−g₆ = e^{2A+2B}√−g̃; the prefactor V_extra rescales 1/κ₆² to 1/κ₄². D1 supplies the two extra dims; D4 supplies G₆.
- **Constants:** G₆ [SELECTED scale → D4]; V_extra [DERIVED ratio from warp integral].
- **Status:** DERIVED-given-decrees.

### EQ-FND-47 — Maxwell equations from KK vectors
- **Equation:** S_Maxwell = −(1/4e²)∫√−g̃ F_μνF^μν; ∂_νF^νμ = e²J^μ; ∂_μ⋆F^μν = 0   (eqs. 3.5, 6.2, 6.6, 6.7)
- **Source:** KK_DIMENSIONAL_REDUCTION.md §3.4, §6.2–6.3
- **Spine path:** S0→S1→S4→S6→S7
- **Decrees:** D2 (U(1)), D1, D4
- **Trace:** 1=1 → S4 gives U(1) phase; the KK off-diagonal mode F_μξ becomes the EM field strength (eq. 6.3); S6 variation of the F² action gives Ampère–Maxwell, the Bianchi identity gives Faraday/no-monopoles. D2 selects U(1); D4 sets e.
- **Constants:** e (=√4πα) [SELECTED scale → D4 / see EQ-FND-48]; ¼ [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-FND-48 — Fine structure constant from geometry
- **Equation:** α⁻¹ = 1.44 ln(ξ_A/η_B) ≈ 137; α = e²/4π
- **Source:** KK_DIMENSIONAL_REDUCTION.md §4 (eqs. 4.4–4.6); WATERS eq. 6.21; AXIOM_MEMBRANE_MECHANICS_v2 §"EM coupling"; AXIOM_6D_SPACETIME
- **Spine path:** S0→S1→S2→S4→S7→S8
- **Decrees:** D1, D2, D4, D5 (the 1.44 coefficient)
- **Trace:** 1=1 → S2 gives the ratio ξ_A/η_B and S3 its log; the gauge coupling from the warp-weighted KK radius runs logarithmically (S7/S8 + QED β-function) so α⁻¹ ∝ ln(ξ_A/η_B). The scales ξ_A,η_B are D4; the prefactor C≈1.44 is presented partly as geometry, partly as a fit to reproduce 137 (the source itself shows the pure one-loop estimate gives ~56, so 1.44 absorbs SM particle content / calibration).
- **Constants:** ξ_A, η_B [SELECTED scale → D4]; 1.44 [FIT → D5]; ln-ratio [DERIVED ratio]; α [DERIVED ratio given those].
- **Status:** PARTIAL — log structure DERIVED-given-decrees; the coefficient 1.44 is a fit (D5), 0.1% agreement.

### EQ-FND-49 — Effective extra-dimensional volume (warp integral)
- **Equation:** V_extra = e^{2A₀+2B₀}(ξ_A/λ + 1/γ); A₀+B₀ ≈ −70   (eqs. 5.2, 5.4)
- **Source:** KK_DIMENSIONAL_REDUCTION.md §5
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D5 (A₀,B₀ tuned to match G₄)
- **Trace:** 1=1 → integrate the warp factors (EQ-FND-50) over ξ,η; the normalization e^{2A₀+2B₀} is then solved so that G₄=G₆/V_extra reproduces the observed G₄ — i.e. it is calibrated, not predicted (source says "calibration, not prediction").
- **Constants:** ξ_A,η_B,λ,γ [SELECTED scale → D4]; A₀,B₀ [FIT → D5].
- **Status:** PARTIAL (form DERIVED; normalization is a fit).

### EQ-FND-50 — Cosmological constant from moduli stabilization
- **Equation:** Λ_eff = (8πG₄/c⁴)ρ_Λ = V(⟨Ψ_A⟩)/M_Pl⁴; V ≈ (2.4×10⁻³ eV)⁴   (eq. 7.3)
- **Source:** KK_DIMENSIONAL_REDUCTION.md §7.3
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D4, D6
- **Trace:** 1=1 → S6 minimizing V(Ψ_A) (dV/dΨ_A=0) fixes ⟨Ψ_A⟩; its value enters EQ-FND-14 as Λ_eff. D6 supplies the Waters Above potential; D4 (and Λ_Z0 anchoring) sets the scale. The match to (2.4 meV)⁴ is observational.
- **Constants:** ⟨Ψ_A⟩, M_Pl [SELECTED scale → D4]; 8π [DERIVED ratio].
- **Status:** DERIVED-given-decrees (absolute value tied to D4 scale anchor).

### EQ-FND-51 — Newtonian limit of reduced Einstein equations
- **Equation:** ∇²Φ = 4πG₄ρ_m; Φ = −G₄M/r; F = G₄Mm/r²   (eqs. 8.2–8.5)
- **Source:** KK_DIMENSIONAL_REDUCTION.md §8
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4
- **Trace:** 1=1 → S6 weak-field expansion g̃_μν=η_μν+h_μν of EQ-FND-14 gives the Poisson equation; its point-mass Green's function gives Newton's potential and inverse-square force. D1 fixes 4D; D4 fixes G₄.
- **Constants:** G₄ [SELECTED scale → D4]; 4π [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

---

## VII. Gauge/Topology, Fermions, and Λ_Z0 Chain

### EQ-FND-52 — SU(3)_C from Z₃ orbifold
- **Equation:** Φ(e^{2πi/3}w) = e^{2πi n_c/3}Φ(w), n_c ∈ {0,1,2}; w ~ e^{2πi/3}w   (RT2 SU3.6–SU3.10)
- **Source:** RT2_SU3_Z3_ORBIFOLD.md §1–2; KK §3.5
- **Spine path:** S0→S1→S4→S7→S8
- **Decrees:** D2 (the Z₃ orbifold / SU(3) selection)
- **Trace:** 1=1 → S4 the complex fiber w=ξ+iη and its phase; S8 the discrete winding sectors; the Z₃ identification ψ~ψ+2π/3 yields three irreducible reps = three colors, closing the SU(3) adjoint. The choice of Z₃ (vs another quotient) is D2.
- **Constants:** 3 [count → D3-style structural via D2].
- **Status:** DERIVED-given-decrees (the group is selected by D2).

### EQ-FND-53 — Spin-½ from Kähler spinor (Postulate F)
- **Equation:** (ξ,η) manifold Kähler ⇒ Dolbeault spinor bundle ⇒ 4D spin-½ zero modes   (AXIOM_GODHEAD_ZONE_Z0 §4)
- **Source:** AXIOM_GODHEAD_ZONE_Z0.md §4; op02 (cited)
- **Spine path:** S0→S1→S4→S5→S9
- **Decrees:** D1, D3 (n_w=3 / Postulate F)
- **Trace:** 1=1 → S4/S9 give the complex 2D fiber and its Kähler structure; the Dolbeault complex provides a natural spinor bundle whose KK reduction yields 4D spin-½ modes. The winding input n_w=3 (D3) is the adopted topological axiom enabling this.
- **Constants:** none dimensionful; n_w=3 [count → D3].
- **Status:** DERIVED-given-decrees (D1, D3) — D3 is an adopted axiom, stated transparently.

### EQ-FND-54 — Three generations from APS index
- **Equation:** index(D) = +3 for the n_w=3 vortex background ⇒ 3 generations; c₁ = n_w
- **Source:** AXIOM_GODHEAD_ZONE_Z0.md §4; op02_aps_index_computation.py (cited)
- **Spine path:** S0→S1→S8
- **Decrees:** D3 (n_w=3)
- **Trace:** 1=1 → S8 supplies integer index invariants (APS / Atiyah–Singer) as forced; *which* integer is the decreed winding. With n_w=3 (D3) the gauge-twisted Dirac index computes to +3 = generation count. The source is explicit that n_w=3 is adopted, not derived (the #849 race refuted all derivation attempts).
- **Constants:** 3 [count → D3].
- **Status:** DERIVED-given-decrees (entirely contingent on the D3 axiom).

### EQ-FND-55 — Z₀ Randall–Sundrum action and Λ_Z0 anchor
- **Equation:** S_Z0 = ∫d⁶x√(−g)[M_{Z0}⁴R⁽⁶⁾ − 2Λ_Z0] − σ; k₁² = |Λ_Z0|/(5M_{Z0}⁴); M_{Z0}=M_Pl
- **Source:** AXIOM_GODHEAD_ZONE_Z0.md §1; op01 (cited)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D4 (Λ_Z0 is THE scale anchor), D1
- **Trace:** 1=1 → S9 RS action with bulk cosmological constant Λ_Z0; the RS fine-tuning condition fixes k₁²=|Λ_Z0|/(5M_{Z0}⁴). The single free magnitude Λ_Z0 is the irreducible D4 scale anchor (identified theologically with Z₀/Godhead); M_{Z0}=M_Pl is the minimal assignment.
- **Constants:** Λ_Z0, M_{Z0}=M_Pl [SELECTED scale → D4 — this is the root scale decree]; 5 [DERIVED ratio]; σ [SELECTED → D4].
- **Status:** DERIVED-as-form (given D4); Λ_Z0 itself is the undecreed-from-within ground input (the thesis, not a defect).

### EQ-FND-56 — Λ_Z0 → ℏ derivation chain
- **Equation:** k₁ = √(|Λ_Z0|/5M_{Z0}⁴) = 1.22 MeV; L_A = 3/(2k₁) = 83.2η_B; β_geom = I_ξ(L_A)·I_η/η_B² = 813; ℏ = (ση_B³/2c)(η_B/ξ_A)²β_geom
- **Source:** AXIOM_GODHEAD_ZONE_Z0.md §2; op01/op07/op10 (cited)
- **Spine path:** S0→S1→S2→S3→S6→S9
- **Decrees:** D4 (Λ_Z0 anchor), D1, D6
- **Trace:** 1=1 → each link is algebra/geometry (S2 ratios, S6 warp integrals) starting from the single D4 input Λ_Z0: k₁ from the RS condition (EQ-FND-55), L_A from the AdS relation, β_geom from the warp-integral/winding factor, ℏ from the membrane suppression formula. The ONE undetermined number is Λ_Z0; everything else is derivation/measurement/zone-axiom.
- **Constants:** Λ_Z0 [SELECTED scale → D4]; k₁,L_A,η_B,ξ_A,σ [SELECTED scale → D4]; β_geom=813, 83.2, 5, 3/2 [DERIVED ratio]; ℏ [DERIVED given D4].
- **Status:** DERIVED-given-decrees (β_geom numerical refinement beyond L_A=83.2η_B flagged open in source).

### EQ-FND-57 — α from the same Z₁ ratio
- **Equation:** α_4D = α_6D/(3·83.2), α_6D ≈ 1.82, α⁻¹(one-loop) ≈ 137.17
- **Source:** AXIOM_GODHEAD_ZONE_Z0.md §2–3; op07 (cited)
- **Spine path:** S0→S1→S2→S7→S8
- **Decrees:** D4, D2, D5 (two-loop precision residual)
- **Trace:** 1=1 → the same L_A/η_B=83.2 ratio (from Λ_Z0, EQ-FND-56) feeds the 6D→4D gauge-coupling reduction; α_6D≈1.82 → α⁻¹≈137.17 at one loop. The two-loop step to 137.036 is an honest open numerical item (the residual is D5-like).
- **Constants:** 83.2, 3 [DERIVED ratio]; α_6D [DERIVED given D4]; two-loop residual [FIT/open → D5].
- **Status:** PARTIAL (one-loop DERIVED-given-decrees; precision to 137.036 open).

### EQ-FND-58 — Warp factor A_ξ (Waters Above) and B_ξ
- **Equation:** A_ξ(ξ) = (2/3)ln(ξ₀/ξ) (canonical, λ=−4/3); B_ξ(ξ) = B₀ − ln(ξ/L_A); L_A = ξ₀; e^{2A_ξ} = (ξ₀/ξ)^{4/3}
- **Source:** WARP_FUNCTION_DERIVATION_RT1WF.md §2.1, eqs. 2.4, 2.7, 2.22, 2.23; KK §1.3 reconciliation note; OP_G6 (G6.14)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S9 solving the bulk 6D Einstein equation (E1) with Waters-Above stress-energy (V_A≈Λ_A) gives an AdS₅-type warp; the ansatz A_ξ=(2/3)ln(L_A/ξ) satisfies it, with L_A=ξ₀ fixed by the Firmament normalization A(ξ₀,η₀)=0. D1 supplies the geometry; D6 the Waters Above field; D4 the scales. (Source is honest that the A_ξ/B_ξ pair is only simultaneously consistent to leading order.)
- **Constants:** ξ₀,L_A [SELECTED scale → D4]; 2/3, 4/3 [DERIVED ratio].
- **Status:** PARTIAL — leading-order DERIVED; exact simultaneous solution needs numerics (source).

### EQ-FND-59 — Warp factor A_η (Waters Below) and junction tensions
- **Equation:** A_η(η) = −κ_B(η−η₀), κ_B = 1/η_B; junctions σ_ξ = 4/(κ₆²ξ₀), σ_η = 6/(κ₆²η_B); σ_η/σ_ξ = 3ξ₀/2η_B ~ 10⁴⁰
- **Source:** WARP_FUNCTION_DERIVATION_RT1WF.md §2.2, eqs. 2.9, 2.12; §2.4 eqs. 2.26–2.28; OP_G6 (G6.3, G6.4, G6.8)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → S9 RS single-brane geometry in η gives exponential warp A_η=−κ_B|η−η₀|; the codimension-2 Israel junction conditions [∂_ξA]=−κ₆²σ_ξ/3, [∂_ηA]=−κ₆²σ_η/3 fix the anisotropic tensions in terms of the zone scales ξ₀,η_B. D1/D6/D4 supply manifold, membrane, scales. The 10⁴⁰ tension hierarchy = the zone scale hierarchy (D4).
- **Constants:** κ_B=1/η_B, ξ₀, η_B, κ₆² [SELECTED scale → D4]; 4, 6, 3/2 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (OP-2.21 closed via anisotropic tension; A_η RS-ansatz noted as not fully self-consistent from Ψ_B EOM).

### EQ-FND-60 — κ₆² self-consistency and B₀
- **Equation:** κ₆² = κ₄²·(3/2)e^{2B₀}ξ₀η_B; e^{2B₀} ≈ 1.77×10²⁵ ⇒ B₀ ≈ 29
- **Source:** OP_G6_KAPPA6_DERIVATION.md eqs. G6.19, G6.25–G6.27; OP_AETA_PSI_B_SELF_CONSISTENT (cited)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D4
- **Trace:** 1=1 → S6/S9 KK reduction gives κ₆²=κ₄²V₂^eff with V₂^eff=(3/2)e^{2B₀}ξ₀η_B (warp integral, EQ-FND-46/49); equating to the Israel-junction κ₆² target fixes e^{2B₀}, hence B₀≈29. D1 supplies the extra dims; D4 the κ₄²,ξ₀,η_B inputs. B₀ derived (not normalized away) by the self-consistency requirement.
- **Constants:** κ₄², ξ₀, η_B [SELECTED scale → D4]; 3/2, B₀=29, e^{2B₀} [DERIVED ratio]; G₄ check closes at 0.5%.
- **Status:** DERIVED-given-decrees.

### EQ-FND-61 — CP-violating phase from Z₆ zone symmetry
- **Equation:** δ_CP = π/3   (from the Z₆ symmetry of the zone fiber; the same n_w that fixes the generation count)
- **Source:** AXIOM_GODHEAD_ZONE_Z0.md §4 (line "the same n_w fixes the CP phase δ_CP = π/3 from the Z₆ zone symmetry (OP-05)"); op05_ckm_* (cited)
- **Spine path:** S0→S1→S4→S8
- **Decrees:** D3 (n_w=3 / the winding), D2 (the Z₆ discrete zone symmetry of the gauge/charge fiber)
- **Trace:** 1=1 → S4 supplies the complex phase of the fiber w=ξ+iη; S8 supplies the discrete winding/index structure on that circle. The Z₆ identification on the zone fiber (a discrete subgroup selected by the same orbifold/winding data as SU(3), D2) pins the CP phase to a rational multiple of π: δ_CP = 2π/6 = π/3. This is a topological angle (S4/S8), not a fitted CKM parameter — but *which* discrete symmetry (Z₆) and *which* winding (n_w=3) are the decreed inputs D2/D3, so the value is DERIVED-given-decrees, not derived from grammar alone. Note: the *value* π/3 is a topology-forced rational angle [DERIVED ratio]; the precise CKM mixing *angles* remain a separate open/fit item (D5, see Nuclear/Particle ledger), so this row covers only the phase δ_CP.
- **Constants:** δ_CP = π/3 [DERIVED ratio] (topological angle 2π/6 given the Z₆ decree); 6, 3 [count → D3] (the Z₆ order and n_w both trace to the decreed winding).
- **Status:** DERIVED-given-decrees (D2, D3) — the phase is topology-forced *given* the decreed Z₆/n_w; the broader CKM angle spectrum is out of scope here (see D5 fits in the Nuclear/Particle ledger).

---

## VIII. UNTRACEABLE / honesty audit

The following named results in the domain cannot be honestly traced to `1=1` + decrees as
*derivations*; they are recorded here rather than given a fabricated chain.

### UT-FND-01 — Numerical magnitudes σ ≈ 6.0×10⁹⁸, μ ≈ 6.7×10⁸¹
- **Equation:** σ ≈ 6.0×10⁹⁸ kg·m⁻¹·s⁻², μ ≈ 6.7×10⁸¹ kg·m⁻³ (Firmament tension/density absolute values)
- **Reason:** Source (AXIOM_MEMBRANE_MECHANICS_v2 §2, §"Remaining Open Issues") states these absolute magnitudes "cannot yet be derived without solving the full 6D field equations with zone boundary conditions" — they are back-solved from c² = σ/μ and the chosen c. Their ratio is fixed (D4-consistent), but the individual values are an open Phase-0 numerical item, not a spine+decree derivation.

### UT-FND-02 — The 1.44 coefficient in α⁻¹ = 1.44 ln(ξ_A/η_B)
- **Equation:** C = 1.44 (fine-structure prefactor)
- **Reason:** KK §4.3–4.5 shows the pure one-loop geometric estimate gives C≈0.58 (α⁻¹≈56), far from 137; the value 1.44 is obtained by requiring the formula to reproduce the measured 137 and absorbing "the combined effect of warp geometry and Standard Model particle content." This is a fit (recorded as D5 in EQ-FND-48), not a first-principles constant. Honest status: PARTIAL/fit, flagged UNTRACEABLE as a pure derivation.

### UT-FND-03 — n_w = 3 (Postulate F) itself
- **Equation:** n_w = 3 (Hopf/π₁ winding of the Waters-Above vortex sector)
- **Reason:** AXIOM_GODHEAD_ZONE_Z0 §0,§4 documents that the integer 3 is an **adopted axiom** (D3), not derived: six independent physics derivation attempts (#849 race, junction-monodromy, zone-address) plus a scriptural-derivation attempt all returned FAIL/NUMEROLOGY/CONSONANT-BUT-NOT-FORCED. It is the "located freedom" of the framework. Everything downstream (EQ-FND-53/54) is "resolved *given* n_w=3," but n_w=3 is itself untraceable below the decree level by the framework's own honest verdict.

---

*Cross-ref: `SPINE.md` (S0–S9), `DECREE_REGISTER.md` (D0–D6), `README_SCHEMA.md` (row format & honesty rules).*
