# Expansion Ledger — Domain 08: Cosmology

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This ledger traces every displayed/numbered equation and named key result in
> `Research/Mathematical_Models/08_Cosmology/` back to the seed `1=1` using the
> Derivation Spine (rungs S0–S9, `SPINE.md`) plus the named decrees (D0–D6,
> `DECREE_REGISTER.md`). Per the honesty rules in `README_SCHEMA.md`, **no equation
> is claimed "derived from `1=1` alone"** — every physics equation = spine path +
> named decrees + equation-specific algebra. Constants are tagged
> `[DERIVED ratio]` / `[SELECTED scale → D4]` / `[FIT → D5]` / `[count → D3]`.

## Header

| Field | Value |
|-------|-------|
| Domain | Cosmology (08) |
| Equation blocks | 71 |
| Decrees used across domain | D0, D1, D2, D3, D4, D5, D6 |
| UNTRACEABLE items | 4 |
| PARTIAL items | 24 |

**Sources covered:** `08-FRIEDMANN_EVOLUTION.md`, `08-CRITICAL_DENSITY_CALCULATION.md`,
`08-BBN_EARLY_UNIVERSE.md`, `08-CMB_POWER_SPECTRUM.md`, `08-CMB_TRANSFER_FUNCTION.md`,
`08-COMPLETIONS.md`, `08-COMPLETIONS_R4.md`, `08-PRECISION_OBSERVABLES.md`,
`08-RESOLVED_MATTER_FORMATION_TIMELINE.md`, `08-ENERGY_EXTRACTION_CREATION.md`,
`op08_kappa_signatures.py`, `test_cosmology.py`, `test_structure_formation.py`.
**Excluded by skip rules / non-equation:** `08-README_R4.md` (meta-overview),
`08-VACUUM_ENERGY_..._NULL_REPLICATION_HISTORY.md` (external-literature note, no framework equations),
prose/value tables, and code scaffolding.

**Standing decree note (applies to every dimensionful cosmological quantity):** every
equation below that carries a length, time, mass, energy, temperature, or `H₀`/`G₄`-type
magnitude silently depends on **D4** (the scale anchor `M_{Z0}=M_Pl`, `Λ_Z0`) — "the unit
of 1." It is cited once per block, not per term. All continuum (ℝ-valued) usage depends on
**D0** and is likewise cited once per block.

---

### EQ-COS-01 — 6D gravitational action
- **Equation:** S_grav^(6D) = (1/2κ₆²) ∫_{M⁶} d⁶x √(−g₆) (R₆ − 2Λ₆) + S_matter
- **Source:** 08-FRIEDMANN_EVOLUTION.md §1.1
- **Spine path:** S0→S1→S2→S3→S6→S9
- **Decrees:** D0, D1 (6D manifold + dimension count), D4 (κ₆², Λ₆ scales), D6 (matter/zone content via S_matter)
- **Trace:** 1=1 → S1/S2 give the additive+ring grammar → S3+D0 supply the ℝ continuum → S6 supplies the volume integral and curvature operator → S9 supplies the (Lorentzian/Kähler) 6D manifold with metric and curvature scalar R₆; the **dimension 6** is injected by **D1**, the gravitational coupling κ₆ and bulk Λ₆ are dimensionful magnitudes fixed by **D4**, and S_matter packages the zone field content (**D6**). The action *form* is forced; its dimension and scale are decreed.
- **Constants:** κ₆² [SELECTED scale → D4]; Λ₆ [SELECTED scale → D4]; dimension 6 [count → D1].
- **Status:** DERIVED-as-form (δS=0 borderline; given D1, D4, D6).

### EQ-COS-02 — 6D FRW metric ansatz
- **Equation:** ds₆² = −c²dt² + a²(t) dΩ₃² + e^{2B(t,ξ,η)}(dξ² + dη²)
- **Source:** 08-FRIEDMANN_EVOLUTION.md §1.1 (boxed)
- **Spine path:** S0→S3→S5→S9
- **Decrees:** D0, D1 (6 dimensions, 3+1 split + 2 extra), D4 (c, a magnitudes), D6 (zone/warp structure B)
- **Trace:** 1=1 → S3/S5 give ℝ and independent directions of expansion (dimension as a count) → S9 furnishes the metric/curvature manifold. The **6 dimensions and the 3-flat spatial slice** are **D1**; the warp/breathing modulus B over the (ξ,η) extra dimensions is zone-architecture content (**D6**); c and the scale factor are dimensionful (**D4**). The FRW *symmetry form* is generic to S9; the specific zone profile is decreed.
- **Constants:** c [SELECTED scale → D4]; dimension split 4+2 [count → D1]; B-profile [SELECTED → D6].
- **Status:** DERIVED-given-decrees (D1, D6).

### EQ-COS-03 — Kaluza–Klein reduction of the coupling
- **Equation:** 1/κ₄² = (1/κ₆²) ∫ dξ dη e^{2B(t,ξ,η)} = V_extra(t)/κ₆²
- **Source:** 08-FRIEDMANN_EVOLUTION.md §1.2
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1 (extra dimensions to integrate out), D4 (κ scales), D6 (warp profile B)
- **Trace:** 1=1 → S6 supplies integration over the extra-dimensional measure → S9 supplies the warped metric whose volume element is e^{2B}. Integrating the 6D Einstein–Hilbert term over the **D1** extra dimensions with the **D6** warp profile collapses κ₆ into an effective 4D κ₄. The reduction *operation* is grammar; what is reduced (which dimensions, which profile) is decreed.
- **Constants:** κ₆, κ₄ [SELECTED scale → D4]; V_extra [DERIVED ratio from B-profile, given D6].
- **Status:** DERIVED-given-decrees (D1, D6).

### EQ-COS-04 — 4D gravitational constant from 6D
- **Equation:** G₄ = G₆ / V_extra(t)   (with G₆ = κ₆²/(8π))
- **Source:** 08-FRIEDMANN_EVOLUTION.md §1.2, §3.1, §E.3 (boxed)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4 (G₆ scale), D6 (warp profile setting V_extra)
- **Trace:** Direct consequence of EQ-COS-03: the 4D Newton constant is the 6D one divided by the warped extra-dimensional volume. G₆ is the dimensionful anchor (**D4**); V_extra is geometric (**D1**, **D6**). The numerical value G₄ ≈ 6.67×10⁻¹¹ is obtained by *choosing* warp parameters (λ≈41, γ≈10¹⁵ m⁻¹) for self-consistency — those parameters are matched, not derived.
- **Constants:** G₆ [SELECTED scale → D4]; V_extra [DERIVED ratio, given D6]; λ≈41, γ≈10¹⁵ m⁻¹ [FIT → D5].
- **Status:** PARTIAL (mechanism DERIVED-given-decrees; numerical value relies on fitted warp parameters → D5).

### EQ-COS-05 — First Friedmann equation (sustaining mode)
- **Equation:** H² = (8πG₄/3)(ρ_A + ρ_B + ρ_b)
- **Source:** 08-FRIEDMANN_EVOLUTION.md §2.1, §E.1 (boxed); 08-COMPLETIONS.md (1.1); 08-PRECISION_OBSERVABLES.md §1.1; test_cosmology.py (TEST 1)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1 (FRW manifold), D4 (G₄), D6 (Ψ_A/Ψ_B zone densities)
- **Trace:** 1=1 → S1 gives the conserved additive bookkeeping → S6 the time-derivative operator (H = ȧ/a) → S9 the FRW metric whose tt-Einstein component yields the Friedmann constraint. D1 supplies the spacetime to expand in; the three density sources ρ_A (Waters Above), ρ_B (Waters Below), ρ_b (baryons) are **D6** physical content. The Friedmann *form* is GR-on-FRW; the source decomposition is decreed.
- **Constants:** G₄ [SELECTED scale → D4]; 8π/3 [DERIVED ratio]; ρ_i [SELECTED → D6, magnitudes D4].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-COS-06 — Acceleration (second Friedmann) equation
- **Equation:** ä/a = −(4πG₄/3)(ρ_A + P_A + ρ_B + P_B + ρ_b + P_b)   [+ρ_r+P_r in §E.1]
- **Source:** 08-FRIEDMANN_EVOLUTION.md §2.1, §E.1; 08-COMPLETIONS_R4.md (8.9.9); test_cosmology.py (TEST 6)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4, D6
- **Trace:** Companion to EQ-COS-05; S6 second derivative + S9 spatial-curvature Einstein components give the acceleration relation. Same decree set: D1 (manifold), D6 (zone fluids), D4 (G₄). Sign of acceleration follows from the equations of state (EQ-COS-08/-11).
- **Constants:** G₄, 4π/3 [DERIVED ratio + D4]; ρ_i, P_i [SELECTED → D6].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-COS-07 — Fluid energy-conservation / continuity equation
- **Equation:** dρ/dt + 3H(ρ + p/c²) = 0   ⇒   ρ(a) = ρ₀ (a₀/a)^{3(1+w)}
- **Source:** 08-PRECISION_OBSERVABLES.md §1.2; test_cosmology.py (TEST 6 doc)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4 (c)
- **Trace:** 1=1 → S1 gives conservation form a+(−a)=0 → S6 the d/dt operator on the FRW volume (∝a³) → S9 the metric. This is Noether time-translation (∂_μT^{μν}=0) specialized to a perfect fluid on FRW; only D1 (a spacetime) is needed beyond grammar. The w-parametrization integrates the ODE; w-values are supplied per component below.
- **Constants:** c [SELECTED scale → D4]; factor 3, 3(1+w) [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1).

### EQ-COS-08 — Waters Above: dark-energy equation of state w_A = −1
- **Equation:** ρ_A = ½Ψ̇_A² + V_A, P_A = ½Ψ̇_A² − V_A → (attractor Ψ̇_A→0) → w_A = P_A/ρ_A = −1
- **Source:** 08-FRIEDMANN_EVOLUTION.md §2.2 (boxed); 08-COMPLETIONS_R4.md §8.9.2; test_cosmology.py (TEST 6)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4 (V_A=Λ_A scale), D6 (Ψ_A field existence)
- **Trace:** 1=1 → S6 supplies the scalar-field kinetic/potential Lagrangian and its stress tensor → S1 the energy/pressure bookkeeping. The *existence* of the Waters-Above scalar Ψ_A with a flat potential is **D6**; that a frozen scalar gives w=−1 is generic field theory. The constant potential value Λ_A is a dimensionful scale (**D4**).
- **Constants:** Λ_A = V_A [SELECTED scale → D4]; w_A = −1 [DERIVED ratio, given the D6 field].
- **Status:** DERIVED-given-decrees (D6).

### EQ-COS-09 — Waters Below potential (symmetry-breaking)
- **Equation:** V_B(Ψ_B) = −(μ_B²/2)Ψ_B² + (λ_B/4!)Ψ_B⁴
- **Source:** 08-FRIEDMANN_EVOLUTION.md §2.3
- **Spine path:** S0→S2→S6→S7
- **Decrees:** D0, D4 (μ_B, λ_B scales), D6 (Ψ_B field)
- **Trace:** 1=1 → S2 gives the polynomial ring (φ², φ⁴) → S6 the field-theory action context → S7 the symmetry whose spontaneous breaking the double-well encodes. The field Ψ_B and its self-interaction are **D6** content; μ_B (mass) and λ_B (coupling) are decreed magnitudes (**D4**). Same Mexican-hat form as Landau–Ginzburg (EQ-COS-19).
- **Constants:** μ_B [SELECTED scale → D4]; λ_B [SELECTED → D4/D5]; 1/2, 1/4! [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D6).

### EQ-COS-10 — Waters Below: dark-matter dilution
- **Equation:** ρ_B(t) = ρ_{B,0}(a₀/a)³, w_B ≈ 0
- **Source:** 08-FRIEDMANN_EVOLUTION.md §2.3 (boxed), §E.2
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4 (ρ_{B,0}), D6 (Ψ_B as pressureless dust)
- **Trace:** Special case of EQ-COS-07 with w=0: a pressureless field dilutes as a⁻³. That the Waters-Below KK zero mode behaves as cold dust is the **D6** claim; the a⁻³ scaling is then forced.
- **Constants:** ρ_{B,0} [SELECTED scale → D4]; exponent 3 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D6).

### EQ-COS-11 — Energy-density scalings (radiation, matter, Λ)
- **Equation:** ρ_r ∝ a⁻⁴ (w=1/3); ρ_m, ρ_b ∝ a⁻³ (w=0); ρ_Λ = const (w=−1)
- **Source:** 08-FRIEDMANN_EVOLUTION.md §5.1–5.3, §A.3, §E.2; 08-PRECISION_OBSERVABLES.md §1.3
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4
- **Trace:** Each is EQ-COS-07 evaluated at the relevant w (radiation w=1/3 from S4/S5 mode-counting of photon phase space; matter w=0; Λ w=−1 from EQ-COS-08). Only D1 beyond grammar; the equation-of-state values for radiation/matter are standard, not decreed.
- **Constants:** ρ_{i,0} [SELECTED scale → D4]; exponents 3,4 and w=1/3 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1).

### EQ-COS-12 — Critical density
- **Equation:** ρ_crit = 3H₀²/(8πG₄) ≈ 9.47×10⁻²⁷ kg/m³
- **Source:** 08-FRIEDMANN_EVOLUTION.md §2.4, §E.5; 08-COMPLETIONS.md (1.5); 08-PRECISION_OBSERVABLES.md §8.1; test_cosmology.py & test_structure_formation.py (RHO_CRITICAL)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4 (H₀, G₄)
- **Trace:** EQ-COS-05 set to flat (Ω_k=0) and solved for the density that closes the universe. The *form* is algebra on the Friedmann equation; the numerical value is fixed by the dimensionful H₀ and G₄ (**D4**).
- **Constants:** H₀, G₄ [SELECTED scale → D4]; 3/8π [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1).

### EQ-COS-13 — Density parameters / closure (energy budget)
- **Equation:** Ω_i = ρ_i/ρ_crit; Ω_A=0.684, Ω_B/Ω_DM=0.266, Ω_b=0.049, Ω_r≈10⁻⁴; Σ Ω_i = 1
- **Source:** 08-FRIEDMANN_EVOLUTION.md §2.4 (boxed); 08-COMPLETIONS.md §5.2 (5.8–5.11); 08-PRECISION_OBSERVABLES.md §8.1; test_cosmology.py (TEST 3)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4, D6 (zone extents fix the ratios), D5 (values matched to Planck)
- **Trace:** Ω_i is the dimensionless ratio ρ_i/ρ_crit. Closure Σ=1 follows from flatness (EQ-COS-21). The framework *claims* the ratios come from zone-extent geometry (**D6**), but the documents quote the Planck values (0.684/0.266/0.049) directly and acknowledge the precise warp-profile derivation is deferred — so as stated these specific fractions are **fitted** (**D5**).
- **Constants:** Ω_A, Ω_DM, Ω_b, Ω_r [FIT → D5] (claimed [DERIVED ratio] from D6 but not yet derived); ρ_crit magnitude [→ D4].
- **Status:** PARTIAL (closure DERIVED; individual fractions D5 pending D6 derivation).

### EQ-COS-14 — Hubble parameter today
- **Equation:** H₀² = (8πG₄/3)ρ_crit ⇒ H₀ = 67.4 km/s/Mpc = 2.19×10⁻¹⁸ s⁻¹
- **Source:** 08-FRIEDMANN_EVOLUTION.md §3.3 (boxed), §E.4; 08-COMPLETIONS.md (1.4)–(1.8); 08-PRECISION_OBSERVABLES.md §2.2; test_cosmology.py (TEST 1)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4 (G₄, ρ_crit), D5 (the value 67.4 is the Planck measurement)
- **Trace:** EQ-COS-05 at present epoch. The *form* is grammar+GR; the numerical 67.4 km/s/Mpc is adopted from Planck (the documents back-fill the energy budget to reproduce it), hence **D5**.
- **Constants:** G₄, ρ_crit [SELECTED scale → D4]; H₀ = 67.4 [FIT → D5].
- **Status:** PARTIAL (form DERIVED-as-form; value FIT → D5).

### EQ-COS-15 — Hubble's law
- **Equation:** v_rec = H₀ d   (with v_rec = d/dt[a(t₀)d] = ȧ(t₀)d)
- **Source:** 08-COMPLETIONS.md §1.1 (1.2)–(1.3); 08-PRECISION_OBSERVABLES.md §2.3; test_cosmology.py (TEST 1)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4 (H₀)
- **Trace:** 1=1 → S6/S9: proper distance = a(t)·(comoving d); its time derivative is ȧ·d = H₀·d on the FRW metric. Pure kinematic consequence of expansion; only D1 beyond grammar.
- **Constants:** H₀ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-COS-16 — Redshift–scale-factor relation
- **Equation:** 1 + z = a(t₀)/a(t_e) = λ_obs/λ_rest;  z ≈ H₀d/c (nearby)
- **Source:** 08-PRECISION_OBSERVABLES.md §2.3; 08-BBN_EARLY_UNIVERSE.md §7; test_cosmology.py (TEST 2)
- **Spine path:** S0→S4→S6→S9
- **Decrees:** D0, D1, D4 (c)
- **Trace:** 1=1 → S4 supplies the photon phase/wavelength → S9 the expanding metric that stretches null geodesics → ratio of scale factors = wavelength ratio. Standard FRW; D1 only.
- **Constants:** c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1).

### EQ-COS-17 — Hubble expansion function E(z)
- **Equation:** E(z) = H(z)/H₀ = √(Ω_Λ + Ω_m(1+z)³ + Ω_r(1+z)⁴ [+Ω_k(1+z)²])
- **Source:** 08-FRIEDMANN_EVOLUTION.md §7.1; 08-COMPLETIONS.md (3.2); 08-PRECISION_OBSERVABLES.md §2.1; 08-CMB_TRANSFER_FUNCTION.md §1.1; test_structure_formation.py (H_of_z)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4, D5 (Ω values)
- **Trace:** EQ-COS-05 rewritten in redshift using the EQ-COS-11 scalings; each Ω(1+z)^n term is one diluting component. The functional form is forced; the Ω inputs carry their EQ-COS-13 status (D5).
- **Constants:** Ω_Λ,Ω_m,Ω_r [FIT → D5]; exponents 2,3,4 [DERIVED ratio].
- **Status:** PARTIAL (form DERIVED; Ω inputs D5).

### EQ-COS-18 — Critical-density-for-matter (ρ_critical for Waters→matter)
- **Equation:** ρ_critical = 3 m_p⁴ c³ / (4πℏ³) ≈ 2.3×10¹⁷ kg/m³  (R = ℏ/m_p c)
- **Source:** 08-CRITICAL_DENSITY_CALCULATION.md §3.3, §8.1
- **Spine path:** S0→S2→S5→S6
- **Decrees:** D0, D4 (m_p, c, ℏ scales), D6 (Firmament/Waters condensation picture)
- **Trace:** 1=1 → S2 ratios/powers → packing a nucleon mass into a Compton-radius sphere R=ℏ/(m_p c) gives ρ = m/( (4/3)πR³ ) ∝ m⁴c³/ℏ³. The condensation-at-nuclear-density *claim* is **D6** zone content; the algebra is grammar. Value reproduces nuclear density because m_p, c, ℏ are decreed scales (**D4**).
- **Constants:** m_p, c, ℏ [SELECTED scale → D4]; 3/4π [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D6); numerical agreement contingent on D4 inputs.

### EQ-COS-19 — Landau–Ginzburg free-energy functional & order parameter
- **Equation:** F[φ] = ∫[a(T)φ² + bφ⁴ + c(∇φ)²]dV;  δF/δφ=0 ⇒ φ² = a₀(T_c−T)/(2b)
- **Source:** 08-CRITICAL_DENSITY_CALCULATION.md §4.1–4.2
- **Spine path:** S0→S2→S6→S7
- **Decrees:** D0, D4 (a₀,b,c, T_c scales), D6 (Waters↔matter phase transition)
- **Trace:** 1=1 → S2 polynomial ring → S6 variational derivative δF/δφ=0 (S6 δS=0 borderline) → S7 the broken symmetry (φ↔−φ). Generic mean-field theory; the *identification* of φ with Waters/matter order is **D6**.
- **Constants:** a₀,b,c,T_c [SELECTED scale → D4]; 1/(2b) [DERIVED ratio].
- **Status:** DERIVED-as-form (δS=0 borderline; given D6).

### EQ-COS-20 — Coleman–Weinberg radiative symmetry breaking
- **Equation:** V_eff(φ) = (λ/4!)φ⁴ + (λ²/256π²)φ⁴[ln(φ²/μ²) − 25/6];  φ_c² = μ² exp(33/2)
- **Source:** 08-CRITICAL_DENSITY_CALCULATION.md §5.1–5.2
- **Spine path:** S0→S2→S6→S7
- **Decrees:** D0, D4 (λ, μ scales)
- **Trace:** 1=1 → S2 ring + S6 (loop integral / log) + S7 (the gauged/scalar symmetry). One-loop effective potential is standard QFT; the renormalization scale μ and coupling λ are dimensionful inputs (**D4**). No zone-specific decree beyond the matter content.
- **Constants:** λ, μ [SELECTED scale → D4]; 33/2, 25/6, 256π² [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4 scales).

### EQ-COS-21 — Spatial flatness / curvature parameter
- **Equation:** Ω_k = −kc²/(H₀²a₀²); Σ Ω_i + Ω_k = 1; (k=0) ⇒ Ω_total = 1
- **Source:** 08-COMPLETIONS.md §4.3 (4.2)–(4.3); 08-PRECISION_OBSERVABLES.md §4.1; test_cosmology.py (TEST 4)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4, D6 (zone geometry asserted to set k=0)
- **Trace:** Curvature term in EQ-COS-05 rearranged. The vanishing of k is *claimed* to be structural from the flat Firmament slice (**D6**); the constraint Σ=1 is then forced. The "inflation flattens Ω_k" alternative (08-PRECISION_OBSERVABLES.md §4.2) is a separate mechanism.
- **Constants:** c, H₀, a₀ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (k=0 from D6).

### EQ-COS-22 — Inflationary e-fold flattening
- **Equation:** a∝e^{Ht}; Ω_k(t_f) = (e^{−60})² Ω_k(t_i) ≈ 10⁻⁵² Ω_k(t_i)
- **Source:** 08-PRECISION_OBSERVABLES.md §4.2
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4
- **Trace:** Exponential-expansion solution of EQ-COS-05 with Λ-domination drives Ω_k=|k|/(aH)²→0. The "60 e-folds" is an assumed inflation duration, not derived. (Note: this document invokes standard inflation, which the framework elsewhere replaces with the creation-epoch metric — a noted internal tension.)
- **Constants:** 60 e-folds [FIT → D5]; e^{−120} [DERIVED ratio given the input].
- **Status:** PARTIAL (form DERIVED; e-fold count assumed → D5).

### EQ-COS-23 — Creation-epoch Hubble rate
- **Equation:** H_creation ≈ 3×10¹⁴ × H₀ ≈ 2×10¹² s⁻¹
- **Source:** 08-FRIEDMANN_EVOLUTION.md §4.1 (boxed); 08-COMPLETIONS.md §3.3; 08-RESOLVED_MATTER_FORMATION_TIMELINE.md §2.2
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D6 (creation-epoch sustaining input κ_create)
- **Trace:** 1=1 → S6/S9 give H=ȧ/a on the creation metric. The magnitude 3×10¹⁴ H₀ is *fixed by requiring* observable-universe-scale stars to form/illuminate within 6 days — a back-solved constraint, not a derivation. The external energy source (κ) is **D6**.
- **Constants:** H_creation/H₀ ≈ 3×10¹⁴ [FIT → D5]; H₀ magnitude [→ D4].
- **Status:** PARTIAL (UNTRACEABLE numeric ratio; back-solved → D5; the document itself lists this as an open question, §D.1).

### EQ-COS-24 — Creation-epoch scale factor
- **Equation:** a_creation(τ) = a_i exp(H_creation τ), τ ∈ [0, 6 days]
- **Source:** 08-FRIEDMANN_EVOLUTION.md §4.1, §E.6; 08-RESOLVED_MATTER_FORMATION_TIMELINE.md §2.2, §3.1
- **Spine path:** S0→S4→S6→S9
- **Decrees:** D0, D1, D4, D6
- **Trace:** Exponential solution of EQ-COS-05 (S6) at constant H. The duration "6 days" is a scriptural/decree input (**D6** architectural boundary), H_creation per EQ-COS-23. Form forced; inputs decreed.
- **Constants:** a_i [SELECTED scale → D4]; H_creation [→ D5]; 6 days [SELECTED → D6].
- **Status:** PARTIAL (form DERIVED; H_creation and duration decreed/fitted).

### EQ-COS-25 — Sabbath-boundary junction (metric discontinuity)
- **Equation:** lim_{t→t_S⁻}H = H_creation ≈ 3×10¹⁴ s⁻¹; lim_{t→t_S⁺}H = H_sustaining ≈ 2×10⁻¹⁸ s⁻¹
- **Source:** 08-FRIEDMANN_EVOLUTION.md §4.2; 08-COMPLETIONS.md §3.3; 08-RESOLVED_MATTER_FORMATION_TIMELINE.md §2.4
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D6 (the Sabbath metric-discontinuity axiom)
- **Trace:** A first-order junction in ȧ across t_Sabbath. This is **axiomatic content** (AXIOM_METRIC_DISCONTINUITY): the discontinuity is *posited* (**D6**), not derived from the spine. The two limiting H-values come from EQ-COS-14 and EQ-COS-23.
- **Constants:** H_creation, H_sustaining [→ D5/D4]; discontinuity ratio 3×10¹⁴ [→ D5].
- **Status:** UNTRACEABLE-as-derivation (the discontinuity is a posited axiom, D6; recorded honestly, no spine derivation of the jump itself).

### EQ-COS-26 — Coordinate-time / age integral
- **Equation:** t₀ = ∫₀^∞ dz/[(1+z)H(z)] = (1/H₀)∫₀^∞ dz/[(1+z)E(z)] ≈ 13.8 Gyr
- **Source:** 08-FRIEDMANN_EVOLUTION.md §4.3, §7 (boxed); 08-COMPLETIONS.md §3.1–3.2; 08-PRECISION_OBSERVABLES.md §9; test_structure_formation.py (TEST 8)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D5 (Ω values, H₀)
- **Trace:** 1=1 → S6 integrates dt = dz/[(1+z)H] over EQ-COS-17. The *integral form* is forced by FRW kinematics; the 13.8 Gyr value follows from the D5 Ω-budget and H₀. Framework reads this as sustaining-mode coordinate time (mapped from 6 creation days via EQ-COS-25/-40).
- **Constants:** Ω_i, H₀ [FIT → D5 / scale D4]; 13.8 Gyr [DERIVED from those inputs].
- **Status:** PARTIAL (form DERIVED-as-form; value rests on D5 inputs).

### EQ-COS-27 — Scale-factor power laws per era
- **Equation:** radiation a∝t^{1/2}, H=1/(2t); matter a∝t^{2/3}, H=2/(3t); Λ a=a_*e^{H_∞(t−t_*)}, H_∞=√Ω_Λ H₀
- **Source:** 08-FRIEDMANN_EVOLUTION.md §5.1–5.3, §A.3, §E.6
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D5 (Ω_Λ)
- **Trace:** Single-component solutions of EQ-COS-05 with EQ-COS-11 scalings. Exponents 1/2, 2/3 are derived; H_∞=√Ω_Λ H₀ uses the D5 dark-energy fraction.
- **Constants:** exponents 1/2,2/3 [DERIVED ratio]; Ω_Λ [FIT → D5]; H₀ [→ D4].
- **Status:** DERIVED-as-form (given D1; Λ-era amplitude uses D5).

### EQ-COS-28 — CMB temperature redshift scaling
- **Equation:** T(a) = T₀(a₀/a) ⇒ T(z) = T₀(1+z); T₀ = 2.7255 K
- **Source:** 08-FRIEDMANN_EVOLUTION.md §6.1, §E.7; 08-CMB_POWER_SPECTRUM.md §8.2 (boxed); 08-COMPLETIONS_R4.md §8.2.1; 08-PRECISION_OBSERVABLES.md §3.2; test_cosmology.py (TEST 2)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4 (T₀ scale), D5 (the value 2.7255 K)
- **Trace:** Adiabatic cooling: dE=−PdV for a photon gas (E=aT⁴V, P=aT⁴/3) on the FRW volume V∝a³ gives dT/da=−T/a ⇒ T∝1/a (derived in 08-CMB_POWER_SPECTRUM.md §8.2). The *scaling* is forced; the absolute T₀=2.7255 K is the measured anchor (**D5**, magnitude D4).
- **Constants:** T₀ = 2.7255 K [FIT → D5]; exponent 1 [DERIVED ratio].
- **Status:** PARTIAL (scaling DERIVED-as-form; T₀ value FIT → D5).

### EQ-COS-29 — Recombination temperature
- **Equation:** T_rec = T₀(1+z_rec) = 2.7255 × 1090 ≈ 3000 K
- **Source:** 08-FRIEDMANN_EVOLUTION.md §6.1; 08-CMB_POWER_SPECTRUM.md §8.2; 08-COMPLETIONS.md §2.2; test_cosmology.py (TEST 2)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D2 (E_ion=13.6 eV is the EM binding of hydrogen, ½α²m_e c², carrying the U(1) charge), D4, D5 (T₀, z_rec from Saha/hydrogen ionization)
- **Trace:** EQ-COS-28 at z_rec≈1089. z_rec itself comes from the Saha ionization balance of hydrogen (E_ion=13.6 eV); that binding energy is set by the electromagnetic coupling (E_ion=½α²m_e c², the U(1) charge → **D2**) with m_e, c the **D4** scales; T₀ is the D5 anchor.
- **Constants:** T₀ [FIT → D5]; E_ion=13.6 eV [→ D2 (α) + D4 (m_e,c)]; z_rec ≈ 1089 [DERIVED from Saha + those scales]; product ≈ 3000 K.
- **Status:** DERIVED-given-decrees (D2 for the EM binding energy; D5 anchor).

### EQ-COS-30 — Planck blackbody law
- **Equation:** B_ν(T) = (2hν³/c²)/(e^{hν/k_BT}−1) [= (8πhν³/c³)·n_ν energy density form]
- **Source:** 08-COMPLETIONS_R4.md §8.2.2 (8.2.4)–(8.2.7); 08-PRECISION_OBSERVABLES.md §3.3; 08-BBN_EARLY_UNIVERSE.md §7
- **Spine path:** S0→S4→S5→S6
- **Decrees:** D0, D4 (h, c, k_B scales)
- **Trace:** 1=1 → S4 (phase/quantized modes hν) → S5 (mode counting in a cavity) → S6 (Bose–Einstein occupation n_ν=1/(e^{hν/kT}−1) from the statistical sum). Standard QM/stat-mech; only dimensionful constants are decreed (**D4**).
- **Constants:** h, c, k_B [SELECTED scale → D4]; 2,8π factors [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4 scales).

### EQ-COS-31 — Radiation energy density (Stefan–Boltzmann)
- **Equation:** ρ_r = (π²/30) g_eff k_B⁴ T⁴/(ℏc)³ [or (π²/30)(k_BT)⁴/(ℏc)³ for photons]
- **Source:** 08-COMPLETIONS_R4.md §8.2.1 (8.2.3); 08-PRECISION_OBSERVABLES.md §3.3; 08-BBN_EARLY_UNIVERSE.md §8 (a-constant)
- **Spine path:** S0→S4→S5→S6
- **Decrees:** D0, D4 (k_B, ℏ, c), D3-adjacent (g_eff degree-of-freedom count)
- **Trace:** Integral of EQ-COS-30 over frequency/momentum modes (S5 counting + S6 integration). g_eff counts relativistic species — an integer-ish count of degrees of freedom; the photon factor 2 and neutrino factors are S5/S8-type counts.
- **Constants:** k_B,ℏ,c [SELECTED scale → D4]; π²/30 [DERIVED ratio]; g_eff [count].
- **Status:** DERIVED-as-form (given D4 scales).

### EQ-COS-32 — Wien displacement law
- **Equation:** λ_max = b/T, b = 2.898×10⁻³ m·K ⇒ λ_max ≈ 1.06 mm at T₀
- **Source:** 08-PRECISION_OBSERVABLES.md §3.3; 08-COMPLETIONS_R4.md §8.2.2
- **Spine path:** S0→S4→S6
- **Decrees:** D0, D4 (b, T₀)
- **Trace:** Maximize EQ-COS-30 in ν/λ (S6 derivative set to zero). b is a combination of h, c, k_B (**D4**); T₀ is the D5 anchor.
- **Constants:** b [SELECTED scale → D4]; T₀ [FIT → D5].
- **Status:** DERIVED-as-form (given D4).

### EQ-COS-33 — Sound speed in the baryon–photon fluid
- **Equation:** c_s = c/√(3(1+R)), R = 3ρ_b/(4ρ_γ)
- **Source:** 08-BBN_EARLY_UNIVERSE.md §1; 08-CMB_POWER_SPECTRUM.md §4.1; 08-CMB_TRANSFER_FUNCTION.md §2.2; 08-COMPLETIONS.md §7.1; 08-COMPLETIONS_R4.md §8.5.1; 08-PRECISION_OBSERVABLES.md §5.4; test_structure_formation.py (sound_speed_baryon)
- **Spine path:** S0→S2→S6→S9
- **Decrees:** D0, D4 (c), D5 (R via Ω_b/Ω_γ)
- **Trace:** 1=1 → S2 ratios → adiabatic sound speed c_s²=∂p/∂ρ of a photon gas loaded by baryons gives c/√3 reduced by the baryon-loading factor R. The c/√3 limit is forced; R uses the D5 baryon fraction.
- **Constants:** c [SELECTED scale → D4]; R [FIT → D5]; 3,4 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4; R input D5).

### EQ-COS-34 — Sound horizon at recombination/drag
- **Equation:** r_s = ∫₀^{z_*} c_s(z)/[(1+z)H(z)] dz ≈ 144–147 Mpc
- **Source:** 08-BBN_EARLY_UNIVERSE.md §1 (boxed 147 Mpc); 08-CMB_POWER_SPECTRUM.md §4.2 (boxed 144); 08-CMB_TRANSFER_FUNCTION.md §2.2; 08-COMPLETIONS.md §7 (7.2)–(7.5); 08-COMPLETIONS_R4.md §8.5.2; 08-PRECISION_OBSERVABLES.md §5.4; test_structure_formation.py (sound_horizon_drag)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D5 (Ω, H₀ in the integrand)
- **Trace:** 1=1 → S6 integrates the comoving distance a sound wave travels (c_s/aH) to z_*. Form forced; the ≈147 Mpc value rests on the D5 cosmological parameters and z_*.
- **Constants:** integrand inputs Ω, H₀ [FIT → D5 / D4]; r_s ≈ 147 Mpc [DERIVED from those].
- **Status:** PARTIAL (form DERIVED-as-form; value rests on D5).

### EQ-COS-35 — BAO correlation-function peak
- **Equation:** ξ(r) = ξ₀[(r/r_s)^{−γ} + A e^{−(r/r_s)²}];  ξ(r)=(r₀/r)^γ at small r
- **Source:** 08-BBN_EARLY_UNIVERSE.md §1; 08-COMPLETIONS_R4.md §8.5.3, §8.6.4; 08-PRECISION_OBSERVABLES.md §5.5
- **Spine path:** S0→S4→S6→S9
- **Decrees:** D0, D1, D4, D5 (r_s scale)
- **Trace:** 1=1 → S4/S6 Fourier transform of the matter power spectrum (EQ-COS-37) whose acoustic feature sits at r_s imprints a bump in the two-point correlation. The power-law + Gaussian-bump *form* is a phenomenological fit (γ, A, r₀ are fitted shape parameters, **D5**); the location r_s is EQ-COS-34.
- **Constants:** γ, A, r₀ [FIT → D5]; r_s [→ D5 via EQ-COS-34].
- **Status:** PARTIAL (acoustic scale DERIVED; shape parameters FIT → D5).

### EQ-COS-36 — Acoustic-peak wavenumbers / multipole projection
- **Equation:** k_n = nπ/r_s; ℓ = d_A k/2; ℓ_n = nπ d_A(z_*)/(2 r_s); ℓ₁≈220 (with corrections)
- **Source:** 08-CMB_POWER_SPECTRUM.md §4.3–4.4 (boxed); 08-CMB_TRANSFER_FUNCTION.md §2.1–2.3; test_structure_formation.py (TEST 1)
- **Spine path:** S0→S4→S6→S9
- **Decrees:** D0, D1, D4, D5 (d_A, r_s from the Ω-budget)
- **Trace:** 1=1 → S4 standing-wave quantization k_n r_s=nπ → S6/S9 flat-sky projection ℓ≈k d_A/2 (Bessel-peak argument). The naive ℓ₁ and the corrected ℓ₁≈220 require transfer-function/Rees–Sciama factors (EQ-COS-43). The integers n are S8-type counts; d_A, r_s carry D5.
- **Constants:** n [count]; π/2 [DERIVED ratio]; d_A, r_s [FIT → D5].
- **Status:** PARTIAL (quantization + projection DERIVED-as-form; peak values need D5 inputs + corrections).

### EQ-COS-37 — Primordial / matter power spectrum
- **Equation:** P_Φ(k) = A_s (k/k₀)^{n_s−1}; P(k,z)=A_s k^{n_s} T²(k) D²(z)
- **Source:** 08-CMB_POWER_SPECTRUM.md §5.2, §7.1 (boxed); 08-FRIEDMANN_EVOLUTION.md §A.4; 08-COMPLETIONS_R4.md §8.6.2; 08-PRECISION_OBSERVABLES.md §5.3
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D0, D1, D4 (A_s, k₀ scales), D5 (A_s, n_s values)
- **Trace:** 1=1 → S5 (Fourier modes of the density field) → S6 (their variance) → near-scale-invariant power law from creation-epoch fluctuations. A_s = 2.1×10⁻⁹ and n_s = 0.965 are matched to Planck (**D5**); the framework notes A_s normalization is not yet derived from zone geometry.
- **Constants:** A_s, n_s [FIT → D5]; k₀ = 0.05 Mpc⁻¹ [SELECTED scale → D4].
- **Status:** PARTIAL (functional form DERIVED; amplitude/tilt FIT → D5).

### EQ-COS-38 — Spectral index from creation-epoch slow-roll
- **Equation:** n_s − 1 ≈ −2η_creation [or n_s = 1+2ε]; n_s ≈ 0.965
- **Source:** 08-FRIEDMANN_EVOLUTION.md §8.1 (boxed); 08-CMB_POWER_SPECTRUM.md §7.1
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D5 (slow-roll parameter / value)
- **Trace:** 1=1 → S6 expansion-rate variation parameter η/ε set the tilt away from scale invariance. The *relation* is standard slow-roll; the value 0.965 is matched (**D5**) and the slow-roll parameter itself is "moderate" by assumption.
- **Constants:** n_s ≈ 0.965 [FIT → D5]; η/ε [FIT → D5].
- **Status:** PARTIAL (form DERIVED; value FIT → D5).

### EQ-COS-39 — Scalar-perturbation amplitude (inflation-analogue)
- **Equation:** Δ_s²(k) = H_creation²/(4π² φ̇); A_s ∝ H_creation⁴
- **Source:** 08-FRIEDMANN_EVOLUTION.md §8.1; 08-CMB_POWER_SPECTRUM.md §7.2
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D6 (creation-epoch field φ), D5 (A_s value)
- **Trace:** 1=1 → S6/S9 give the standard inflationary fluctuation amplitude in terms of H and φ̇. Uses H_creation (EQ-COS-23, itself D5) and an unspecified φ̇; the document concedes a geometric suppression factor ~10⁶⁶ is needed to match A_s≈2×10⁻⁹ and is not derived.
- **Constants:** H_creation [→ D5]; suppression ~10⁶⁶ [FIT → D5].
- **Status:** PARTIAL (form DERIVED; normalization unexplained → D5).

### EQ-COS-40 — Tensor-to-scalar ratio
- **Equation:** r = Δ_t²/Δ_s² < 0.01 [= 16ε]
- **Source:** 08-FRIEDMANN_EVOLUTION.md §B.1; 08-PRECISION_OBSERVABLES.md §11.1
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D5 (ε)
- **Trace:** Ratio of tensor to scalar perturbation power (S6 on the FRW metric, tensor modes from S9). r=16ε is standard single-field slow-roll; ε is a model input. Prediction r<0.01 is a bound, not a derived number.
- **Constants:** 16 [DERIVED ratio]; ε [FIT → D5].
- **Status:** PARTIAL (form DERIVED; magnitude D5).

### EQ-COS-41 — Non-Gaussianity prediction
- **Equation:** f_NL ≈ 0.1–1
- **Source:** 08-FRIEDMANN_EVOLUTION.md §8.2 (boxed), §B.1
- **Spine path:** —
- **Decrees:** D6 (deterministic creation-epoch metric)
- **Trace:** Claimed to follow from a "deterministic creation-epoch metric" producing minimal non-Gaussianity; no derivation chain is given — it is an order-of-magnitude assertion. Not reducible to a spine path as stated.
- **Constants:** f_NL ~ O(1) [asserted, no derivation].
- **Status:** UNTRACEABLE (qualitative assertion; no spine-derivable chain provided).

### EQ-COS-42 — Density-perturbation growth equation
- **Equation:** δ̈ + 2Hδ̇ − 4πGρ_m δ = 0 (=(3Ω_mH₀²/2a³)δ); δ∝a (matter era)
- **Source:** 08-FRIEDMANN_EVOLUTION.md §A.4; 08-COMPLETIONS_R4.md §8.6.1 (8.6.1)–(8.6.2); 08-PRECISION_OBSERVABLES.md §5.2
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4, D6 (the gravitating dark-matter source)
- **Trace:** 1=1 → S6 (second-order ODE) on the FRW background; Jeans/Newtonian perturbation theory of the self-gravitating fluid. Growing mode δ∝a is derived. Source ρ_m includes the Waters-Below dark matter (**D6**).
- **Constants:** 4πG, 3/2 [DERIVED ratio + D4 via G].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-COS-43 — Growth function
- **Equation:** D(a) = (5/2)Ω_m(a)(E(a)/E₀)∫₀^a da'/(a'³E³(a')); D(a)≈a (matter era)
- **Source:** 08-PRECISION_OBSERVABLES.md §5.2; 08-COMPLETIONS_R4.md §8.6.2
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D5 (Ω_m via E)
- **Trace:** Integral solution of EQ-COS-42 over the EQ-COS-17 expansion history. Form forced; Ω_m input is D5.
- **Constants:** 5/2 [DERIVED ratio]; Ω_m [FIT → D5].
- **Status:** DERIVED-as-form (given D1; D5 input).

### EQ-COS-44 — Transfer function (Eisenstein–Hu)
- **Equation:** T(k) = ln(e+1.84βk)/[ln(e+1.84βk) + (0.3γ)²]
- **Source:** 08-COMPLETIONS_R4.md §8.6.3 (8.6.8)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D5 (β, γ, k_eq)
- **Trace:** Phenomenological fitting function for how perturbations evolve through matter–radiation equality; β, γ are fitted shape constants (Eisenstein–Hu), not derived. The turnover scale k_eq is set by equality, a D5-parameter epoch.
- **Constants:** 1.84, 0.3, β, γ [FIT → D5].
- **Status:** PARTIAL (UNTRACEABLE fit form; standard fitting function, D5 constants).

### EQ-COS-45 — CMB power spectrum (C_ℓ)
- **Equation:** C_ℓ = ⟨|a_ℓm|²⟩ = (2/π)∫₀^∞ dk k² P_Φ(k)|T_k^Θ(z_*)|²
- **Source:** 08-CMB_POWER_SPECTRUM.md §5.1 (boxed), §5.2; 08-CMB_TRANSFER_FUNCTION.md §7.1
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D0, D1, D4, D5 (P_Φ, transfer-function inputs)
- **Trace:** 1=1 → S5 (spherical-harmonic decomposition of ΔT/T) → S6 (variance, k-integral) → the line-of-sight integral of the primordial spectrum times the transfer function. Form is standard; inputs (EQ-COS-37, EQ-COS-44) carry D5.
- **Constants:** 2/π [DERIVED ratio]; P_Φ, T_k [→ D5].
- **Status:** DERIVED-as-form (given D1; D5 inputs).

### EQ-COS-46 — Radiation transfer / Boltzmann hierarchy
- **Equation:** dΘ₀/dη = −dΦ/dη − κ'(Θ₀−Θ₀^{(0)}) − (1/3)kΘ₁; dΘ₁/dη = (k/3)(Θ₀−2Θ₂) − κ'Θ₁ + (1/3)kΦ; dv_b/dη = −Hv_b − c_s²/(1+R_b) kδ_b + kΦ
- **Source:** 08-CMB_POWER_SPECTRUM.md §5.2; 08-CMB_TRANSFER_FUNCTION.md §3.1, §6.1
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D2 (Thomson coupling κ'=σ_T n_e carries the EM charge e, see EQ-COS-53), D4, D6 (baryon/photon/dark-matter content)
- **Trace:** 1=1 → S6 (the Boltzmann/transport ODEs) on the FRW background (S9), with Thomson coupling κ'=σ_T n_e — whose cross-section carries the U(1) electric charge e (**D2**, per EQ-COS-53). Standard CMB physics; the field content (baryons, photons, Waters Below) is D6.
- **Constants:** 1/3, 2 [DERIVED ratio]; κ' [→ D2 (charge) + D4]; c_s, R_b, H [→ D4/D5].
- **Status:** DERIVED-as-form (given D1, D2, D6).

### EQ-COS-47 — Linearized 6D Einstein perturbation equation
- **Equation:** g_AB = ḡ_AB + h_AB; δG_AB = 8πG₆ δT_AB; □φ + (3H+...)φ̇ + 4πG₆ e^{2A}δρ_total = 0
- **Source:** 08-CMB_POWER_SPECTRUM.md §1.2, §2.1–2.3 (boxed); 08-CMB_TRANSFER_FUNCTION.md §7.1
- **Spine path:** S0→S5→S6→S9
- **Decrees:** D0, D1, D4 (G₆), D6 (Ψ_A/Ψ_B perturbations)
- **Trace:** 1=1 → S5 (perturbation expansion into scalar/vector/tensor irreps) → S6 (d'Alembertian □, linearized differential operators) → S9 (background 6D metric). Linearized Einstein equation around the 6D background; dimension and zone fields are D1/D6.
- **Constants:** G₆ [SELECTED scale → D4]; 8π, 3, 4π [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-COS-48 — Coupled baryon–dark-matter oscillator system
- **Equation:** v̈_b + (2H+...)v̇_b + c_s²k²v_b + α_c k²δ_B = 0; δ̈_B + (2H+...)δ̇_B + (c_B²/a²)k²δ_B + β_c k²v_b = 0
- **Source:** 08-CMB_POWER_SPECTRUM.md §3.4 (boxed); 08-CMB_TRANSFER_FUNCTION.md §4.1
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D6 (coupling between Firmament baryons and Waters-Below modes)
- **Trace:** 1=1 → S6 (coupled damped-oscillator ODEs) from the linearized stress-energy. The cross-couplings α_c, β_c encode the Firmament↔Waters-Below interaction (**D6**); the dispersion (EQ-COS-49) follows.
- **Constants:** α_c, β_c [SELECTED → D6/D5]; c_s, c_B [→ D4].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-COS-49 — Acoustic dispersion relation
- **Equation:** ω_k = c_s k; T_k = 2π/(c_s k)
- **Source:** 08-CMB_POWER_SPECTRUM.md §4.1; 08-CMB_TRANSFER_FUNCTION.md §2.2
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D4 (c_s)
- **Trace:** 1=1 → S6 wave-equation eigenfrequency of EQ-COS-48 in the tight-coupling limit. Pure grammar once c_s (EQ-COS-33) is given.
- **Constants:** c_s [→ D4/D5 via R].
- **Status:** DERIVED-as-form.

### EQ-COS-50 — Angular-diameter & related distances
- **Equation:** d_C(z)=(c/H₀)∫₀^z dz'/E(z'); d_A=d_C/(1+z); d_L=(1+z)d_C
- **Source:** 08-FRIEDMANN_EVOLUTION.md §A.5, §E.8; 08-CMB_POWER_SPECTRUM.md §4.4; 08-CMB_TRANSFER_FUNCTION.md §1.1 (boxed); test_structure_formation.py (comoving/angular_diameter_distance)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D5 (Ω, H₀ in E)
- **Trace:** 1=1 → S6 integrates the null-geodesic comoving distance over EQ-COS-17; d_A and d_L are kinematic (1+z) rescalings on the FRW metric. Form forced; numerical d_A(z_*)≈13.2–13.9 Gpc uses D5 parameters.
- **Constants:** c, H₀ [→ D4]; Ω_i [FIT → D5]; (1+z) factors [DERIVED].
- **Status:** PARTIAL (form DERIVED-as-form; values rest on D5).

### EQ-COS-51 — Rees–Sciama / baryon-loading peak corrections
- **Equation:** ξ_RS = √(1−(τ_dyn/τ_osc)²) ≈ 0.79; C_{2n}/C_{2n−1} = ((1−0.5R_b)/(1+R_b))²; C₂/C₁≈−0.22
- **Source:** 08-CMB_TRANSFER_FUNCTION.md §3.2 (boxed), §4.1–4.2 (boxed); 08-CMB_POWER_SPECTRUM.md §5.4
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D5 (R_b)
- **Trace:** 1=1 → S6 (time-varying driving of the oscillator EQ-COS-48 by the decaying potential Φ) gives a phase/amplitude correction. ξ_RS and the odd/even peak-height ratio are derived as functions of R_b (D5). The documents openly note residual ~50% gaps requiring full Boltzmann integration — so these are partial/heuristic.
- **Constants:** R_b [FIT → D5]; 0.79, −0.22 [DERIVED from R_b + heuristics].
- **Status:** PARTIAL (heuristic corrections; full transfer function deferred to numerics).

### EQ-COS-52 — Silk damping envelope
- **Equation:** λ_D=√(cλ_γ/3 · cΔη); k_d=1/λ_D; |T_k|²∝exp(−(k/k_d)²); C_ℓ^{damped}=C_ℓ exp(−(ℓ/ℓ_d)²)
- **Source:** 08-CMB_POWER_SPECTRUM.md §6.1–6.2 (boxed); 08-CMB_TRANSFER_FUNCTION.md §5.1–5.3 (boxed)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D2 (Thomson rate via EM charge e in σ_T, see EQ-COS-53), D4 (m_e, c, n_e scales), D5 (k_d, ℓ_d values)
- **Trace:** 1=1 → S6 (diffusion/random-walk of photons, Thomson rate τ̇=σ_T n_e) gives a Gaussian damping in k. Form forced by diffusion physics; the Thomson cross-section σ_T carries the EM coupling e (the U(1) charge, **D2**, per EQ-COS-53); the damping scale k_d≈0.02 Mpc⁻¹ / ℓ_d≈1325 uses D5 ionization history.
- **Constants:** σ_T [→ D2 (charge e) + D4 (m_e,c), per EQ-COS-53]; n_e [SELECTED scale → D4]; k_d, ℓ_d [FIT → D5].
- **Status:** DERIVED-as-form (given D1, D2; damping scale D5).

### EQ-COS-53 — Thomson cross-section
- **Equation:** σ_T = (8π/3)(e²/(4πε₀ m_e c²))² = 6.65×10⁻²⁹ m²
- **Source:** 08-CMB_TRANSFER_FUNCTION.md §5.1; 08-COMPLETIONS_R4.md §8.8.2
- **Spine path:** S0→S2→S4→S6
- **Decrees:** D0, D2 (electromagnetic coupling e), D4 (m_e, c, ε₀)
- **Trace:** 1=1 → S2/S4 (classical radius from EM coupling) → S6 (scattering integral). The electric charge e invokes the U(1) gauge content (**D2**); the rest are dimensionful scales (**D4**). Standard QED result.
- **Constants:** e [→ D2]; m_e, c, ε₀ [SELECTED scale → D4]; 8π/3 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D2, D4).

### EQ-COS-54 — n/p equilibrium and freeze-out ratio
- **Equation:** n_n/n_p = e^{−Q/k_BT}, Q=m_n−m_p=1.293 MeV; (n/p)_freeze ≈ e^{−1.293/0.7} ≈ 0.15
- **Source:** 08-BBN_EARLY_UNIVERSE.md §3; 08-CMB_POWER_SPECTRUM.md §9.1 (boxed); 08-COMPLETIONS.md §6.3; 08-COMPLETIONS_R4.md §8.11.2–8.11.3; test_structure_formation.py (TEST 4)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D0, D2 (weak interaction), D4 (Q, T scales), D3-adjacent (3 ν species → freeze-out timing)
- **Trace:** 1=1 → S6 (Boltzmann/Saha equilibrium) → S7 (the weak interaction n↔p, an SU(2)×U(1) process, **D2**). The Boltzmann factor e^{−Q/kT} is grammar; Q=1.293 MeV (mass splitting) is a decreed/measured scale (**D4**, ultimately from the mass-spectrum sector). Freeze-out T_f≈0.7 MeV from Γ_weak~G_F²T⁵ = H (EQ-COS-55).
- **Constants:** Q [SELECTED scale → D4]; T_f [DERIVED via EQ-COS-55]; e^{...} [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D2; D4 mass-splitting input).

### EQ-COS-55 — Weak freeze-out condition
- **Equation:** Γ_weak ~ G_F²T⁵ ≈ H ~ T²/M_P ⇒ T_f ≈ 0.7–0.8 MeV (T_νdec≈2.3 MeV)
- **Source:** 08-BBN_EARLY_UNIVERSE.md §3, §6; 08-COMPLETIONS_R4.md §8.14.1 (8.14.1)–(8.14.6)
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D0, D1, D2 (weak coupling G_F), D4 (G_F, M_P scales)
- **Trace:** 1=1 → S7 (weak interaction rate, D2) vs S9/EQ-COS-11 (radiation-era Hubble rate). Setting rate=expansion gives the freeze-out/decoupling temperature. G_F is the weak scale (**D2**, magnitude **D4**); M_P is the **D4** Planck anchor.
- **Constants:** G_F, M_P [SELECTED scale → D4; coupling → D2]; T_f, T_νdec [DERIVED].
- **Status:** DERIVED-given-decrees (D2).

### EQ-COS-56 — Neutron decay between freeze-out and BBN
- **Equation:** N_n(t)=N_{n,0}e^{−t/τ_n}, τ_n≈879.4 s ⇒ (n/p)_nuc ≈ 1/7
- **Source:** 08-BBN_EARLY_UNIVERSE.md §3; 08-CMB_POWER_SPECTRUM.md §9.1; 08-COMPLETIONS_R4.md §8.11.3 (8.11.7)–(8.11.8); test_structure_formation.py (TEST 4)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D0, D2 (weak decay), D4 (τ_n scale)
- **Trace:** 1=1 → S6 exponential-decay ODE; the lifetime τ_n is a weak-interaction (**D2**) measured/decreed scale (**D4**). Reduces (n/p) from 0.15 to ~1/7 over ~200 s.
- **Constants:** τ_n [SELECTED scale → D4]; e^{−t/τ} [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D2).

### EQ-COS-57 — Helium-4 mass fraction
- **Equation:** Y_p = 2(n/p)_nuc/(1+(n/p)_nuc) ≈ 0.245–0.247
- **Source:** 08-BBN_EARLY_UNIVERSE.md §3 (boxed); 08-CMB_POWER_SPECTRUM.md §9.2 (boxed); 08-COMPLETIONS.md §6.4 (6.5)–(6.7); 08-COMPLETIONS_R4.md §8.11.4 (8.11.10)–(8.11.12); test_structure_formation.py (TEST 4)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D0, D2, D4 (mass-splitting/τ_n), D3-adjacent (counting nucleons into He-4)
- **Trace:** 1=1 → S2 (ratio bookkeeping): all neutrons captured into He-4 (2n+2p) gives the mass-fraction formula. Pure counting once (n/p)_nuc is fixed (EQ-COS-54/-56). The 0.245 value follows from the D2/D4 weak-physics inputs.
- **Constants:** (n/p)_nuc [DERIVED via EQ-COS-54/56]; factor 2 [count]; Y_p ≈ 0.245 [DERIVED-given-decrees].
- **Status:** DERIVED-given-decrees (D2).

### EQ-COS-58 — Deuterium abundance / baryon-density sensitivity
- **Equation:** D/H ∝ η^{−1.6}; D/H ≈ 2.5×10⁻⁵ (η=6.1×10⁻¹⁰); σv = A(T)T^{−2/3}e^{−44.027/(k_BT)^{1/2}}
- **Source:** 08-BBN_EARLY_UNIVERSE.md §4 (boxed); 08-COMPLETIONS.md §6; 08-COMPLETIONS_R4.md §8.12.2 (8.12.2), §8.12.4 (8.12.10); test_structure_formation.py (TEST 5)
- **Spine path:** S0→S2→S6→S7
- **Decrees:** D0, D2 (nuclear/strong reactions), D4 (η, Q_d scales), D5 (η value & power-law normalization)
- **Trace:** 1=1 → S6/S7 (nuclear reaction network, strong-force **D2**). The η^{−1.6} scaling and the Gaussian-tunneling rate are fits to the BBN reaction network (Cyburt/Steigman normalization), and η=6.1×10⁻¹⁰ is the measured baryon-to-photon ratio (**D5**). D/H≈2.5×10⁻⁵ then follows.
- **Constants:** η [FIT → D5]; exponent −1.6, 44.027 [FIT → D5]; Q_d=2.22 MeV [→ D4].
- **Status:** PARTIAL (network-fit relation; η and normalization FIT → D5).

### EQ-COS-59 — Lithium-7 abundance & membrane-catalysis resolution
- **Equation:** (⁷Li/H)_BBN ≈ 5×10⁻¹⁰; (⁷Li/H)_final = (1−b)×5×10⁻¹⁰ = 1.5×10⁻¹⁰ (b≈0.7)
- **Source:** 08-BBN_EARLY_UNIVERSE.md §5 (boxed); 08-COMPLETIONS.md §6.5; 08-COMPLETIONS_R4.md §8.13.3 (8.13.7); test_structure_formation.py (TEST 6)
- **Spine path:** S0→S2→S6→S7
- **Decrees:** D0, D2, D4, D6 (Firmament-catalysis hypothesis), D5 (branching b)
- **Trace:** The BBN production 5×10⁻¹⁰ traces like EQ-COS-58 (D2 network). The *resolution* — a membrane-catalyzed destruction with branching b≈0.7 — is an explicitly **speculative D6 hypothesis** the documents mark PARTIAL/OPEN; b is fitted to land on the observed 1.6×10⁻¹⁰ (**D5**).
- **Constants:** 5×10⁻¹⁰ [DERIVED-given-decrees via network]; b≈0.7 [FIT → D5]; mechanism [SELECTED → D6, unproven].
- **Status:** PARTIAL (production DERIVED-given-decrees; depletion mechanism UNTRACEABLE/speculative, flagged OPEN by source).

### EQ-COS-60 — Neutrino temperature & N_eff
- **Equation:** T_ν = (4/11)^{1/3}T_γ ≈ 1.95 K; ρ_rad = (1+(7/8)(4/11)^{4/3}N_eff)ρ_γ; N_eff = 3.044
- **Source:** 08-BBN_EARLY_UNIVERSE.md §6 (boxed); 08-COMPLETIONS.md §11 (11.1)–(11.6); 08-COMPLETIONS_R4.md §8.14.2 (8.14.7)–(8.14.22); test_structure_formation.py (TEST 7)
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D0, D2 (weak decoupling), D3 (three neutrino species), D4 (T_γ scale)
- **Trace:** 1=1 → S5/S6 (entropy conservation g_*s a³T³=const across e⁺e⁻ annihilation) gives the (4/11)^{1/3} reheat ratio. The factor 7/8 is fermion vs boson statistics (S5 counting). **Three** species is the generation count (**D3**); the +0.044 is a QED finite-temperature correction. T_γ=2.7255 K is the D5 anchor.
- **Constants:** (4/11)^{1/3}, 7/8 [DERIVED ratio]; N_eff=3 [count → D3]; +0.044 [DERIVED correction]; T_γ [FIT → D5].
- **Status:** DERIVED-given-decrees (D3 for the species count; ratio forced).

### EQ-COS-61 — Effective deceleration / transition redshift
- **Equation:** q = Ω_m/2 − Ω_Λ; q₀≈−0.53; (1+z_t)³ = 2Ω_Λ/Ω_m ⇒ z_t≈0.63
- **Source:** 08-COMPLETIONS_R4.md §8.9.1 (8.9.2)–(8.9.3), §8.9.4 (8.9.14)–(8.9.16); 08-PRECISION_OBSERVABLES.md §7.2; test_cosmology.py (TEST 6)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4, D5 (Ω_m, Ω_Λ)
- **Trace:** From EQ-COS-06: q=−aä/ȧ² evaluated with the EQ-COS-13 budget; z_t set by ä=0 (matter density = 2× dark energy). Algebra forced; the numbers use the D5 Ω-values.
- **Constants:** Ω_m, Ω_Λ [FIT → D5]; factor 2, 1/2 [DERIVED ratio].
- **Status:** PARTIAL (form DERIVED-as-form; values D5).

### EQ-COS-62 — Olbers'-paradox surface brightness / redshift dimming
- **Equation:** I_obs = I_emitted/(1+z)⁴; I_total = ∫I(z)n(z)(dV/dz)dz → finite; B_ν blackbody bound
- **Source:** 08-BBN_EARLY_UNIVERSE.md §7 (boxed); 08-COMPLETIONS.md §10; test_structure_formation.py (TEST 9)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4, D6 (finite zone/creation horizon)
- **Trace:** 1=1 → S6/S9: surface brightness dims as (1+z)⁴ (two powers energy redshift, two time-dilation/volume) on the FRW metric; integrating over a finite observable volume (finite age + recombination cutoff, D6) gives a finite, dim sky. Form forced; horizon finiteness is D6/creation content.
- **Constants:** exponent 4 [DERIVED ratio]; horizon scale [→ D4/D6].
- **Status:** DERIVED-as-form (given D1; finite-horizon claim D6).

### EQ-COS-63 — NFW & isothermal dark-matter halo / rotation curves
- **Equation:** ρ_NFW(r)=ρ_s/[(r/r_s)(1+r/r_s)²]; M(r)=4πρ_s r_s³[ln(1+r/r_s)−(r/r_s)/(1+r/r_s)]; v_c=√(GM/r); isothermal ρ∝r⁻²
- **Source:** 08-COMPLETIONS.md §8 (8.4)–(8.8); 08-COMPLETIONS_R4.md §8.7.2–8.7.4 (8.7.2)–(8.7.8); 08-PRECISION_OBSERVABLES.md §6.2; test_cosmology.py (TEST 5)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4 (G, ρ_s, r_s), D6 (Waters-Below as collisionless dark matter)
- **Trace:** 1=1 → S6 integrates Poisson/Newtonian enclosed-mass M(r)=∫4πr²ρ dr; demanding flat v_c forces ρ∝r⁻² (isothermal); the NFW profile is the standard collapse profile. The dark-matter field is Waters Below (**D6**); ρ_s, r_s are halo-specific fitted scales (**D5/D4**).
- **Constants:** G [→ D4]; ρ_s, r_s [FIT → D5]; concentration c [FIT → D5].
- **Status:** DERIVED-as-form (given D1, D6); halo parameters FIT → D5.

### EQ-COS-64 — Bullet-cluster momentum/mass ratio
- **Equation:** Δp_C/Δp_A = ρ_C/ρ_A ≈ 8; M_DM/M_b = Ω_DM/Ω_b ≈ 5.4 (observed ~9)
- **Source:** 08-BBN_EARLY_UNIVERSE.md §2; 08-COMPLETIONS.md §9; 08-COMPLETIONS_R4.md §8.8.4 (8.8.3); test_structure_formation.py (TEST 3)
- **Spine path:** S0→S1→S6
- **Decrees:** D0, D4, D5 (Ω_DM, Ω_b), D6 (collisionless Waters Below)
- **Trace:** 1=1 → S1 momentum bookkeeping; the DM/baryon ratio is just Ω_DM/Ω_b (EQ-COS-13). Collisionlessness of Waters Below (**D6**) explains the spatial separation. Ratio value carries the D5 budget; observed ~9 vs predicted 5.4 is acknowledged as only "consistent within uncertainties."
- **Constants:** Ω_DM/Ω_b ≈ 5.4 [FIT → D5]; separation kinematics [→ D4].
- **Status:** PARTIAL (ratio = Ω-budget, D5; mechanism D6).

### EQ-COS-65 — Jeans length and mass
- **Equation:** λ_J = π√(c_s²/(Gρ₀)); M_J = (4π/3)ρ₀(λ_J/2)³
- **Source:** test_cosmology.py (TEST 7); 08-RESOLVED_MATTER_FORMATION_TIMELINE.md §3.2 (instability)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4 (G, c_s scales), D6 (dark-matter background)
- **Trace:** 1=1 → S6 balances pressure support (c_s) against self-gravity (Gρ₀) in the perturbation ODE (EQ-COS-42); the scale where they cross is λ_J. Form forced; ρ₀ and σ_v are epoch/halo inputs.
- **Constants:** G [→ D4]; c_s=σ_v, ρ₀ [→ D4/D5]; π, 4π/3 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1, D6).

### EQ-COS-66 — Sackur–Tetrode entropy & Gibbs free energy (condensation thermodynamics)
- **Equation:** G = H − TS = U + PV − TS; S_Waters = Nk_B[ln(V/N)+(3/2)ln(2πmk_BT/h²)+5/2]; ρ_critical = exp[(−ε_b/k_BT) − f(T)]
- **Source:** 08-CRITICAL_DENSITY_CALCULATION.md §2.1–2.4
- **Spine path:** S0→S2→S5→S6
- **Decrees:** D0, D4 (m, ε_binding, h, k_B scales), D6 (Waters↔matter phase picture)
- **Trace:** 1=1 → S2 (ring/log) → S5 (phase-space mode counting → Sackur–Tetrode) → S6 (minimize G). Standard statistical thermodynamics of an ideal-gas-vs-condensate transition; the identification with Waters/matter is **D6**. ε_binding≈8 MeV is a nuclear scale (**D4**).
- **Constants:** ε_binding, m, h, k_B [SELECTED scale → D4]; 3/2, 5/2 [DERIVED ratio].
- **Status:** DERIVED-as-form (given D6).

### EQ-COS-67 — Membrane strain energy & gravitational dimple
- **Equation:** E_strain=(1/2)σ(∇η)²; η(r)=−Gm/r; E_strain,total = 2πσ(Gm)²/R
- **Source:** 08-CRITICAL_DENSITY_CALCULATION.md §3.1
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D4 (σ tension scale), D6 (Firmament membrane mechanics)
- **Trace:** 1=1 → S6 (gradient energy of a tense membrane) integrated over the Newtonian-potential dimple η=−Gm/r → finite strain energy ∝(Gm)²/R. The membrane-tension picture is **D6** (Firmament mechanics axiom); σ is its dimensionful scale (**D4**).
- **Constants:** σ [SELECTED scale → D4]; G [→ D4]; 2π, 1/2 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D6).

### EQ-COS-68 — Membrane-curvature density threshold & Planck density
- **Equation:** R~8πGρ; K_max~1/l_P²=c³/(ℏG); ρ_Planck=c⁵/(ℏG²)≈5.16×10⁹⁶ kg/m³; ρ_critical=K_c c²/(8πG)
- **Source:** 08-CRITICAL_DENSITY_CALCULATION.md §6.1–6.2
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D4 (G, ℏ, c → Planck scale), D6 (membrane breakdown curvature)
- **Trace:** 1=1 → S9 (Ricci curvature R~8πGρ from Einstein equations) → maximum curvature at the Planck scale l_P (a pure combination of G, ℏ, c, **D4**). The condensation-at-critical-curvature hypothesis is **D6**.
- **Constants:** G, ℏ, c [SELECTED scale → D4]; 8π [DERIVED ratio]; K_c [SELECTED → D6].
- **Status:** DERIVED-given-decrees (D6).

### EQ-COS-69 — κ-driven dark-energy equation of state w(z)
- **Equation:** κ(t)=κ_full(1−ε); ρ_Λ(z)=ρ_Λ0 κ(z)/κ_now; w(z) = −1 + nε_now/3 (ε∈[10⁻⁶⁰,10⁻²⁷])
- **Source:** op08_kappa_signatures.py §2 (Part 1)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D0, D1, D4, D6 (sustaining coupling κ / Axiom 5)
- **Trace:** 1=1 → S6 differentiates ln ρ_Λ w.r.t. ln a using EQ-COS-07; a slowly-decreasing κ(t) (the sustaining coupling, **D6**) gives w = −1 + (1/3)d ln κ/d ln a = −1 + nε/3. The deviation is set by ε, a parameter from the entropy-production argument (Vol 1 Ch 8) — a decreed/bounded magnitude. Result: |w+1|<10⁻²⁷, observationally invisible (the script flags κ as currently UNFALSIFIABLE).
- **Constants:** ε [SELECTED → D6, range bounded]; n [SELECTED]; 1/3 [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D6); deviation FIT/bounded, observationally null.

### EQ-COS-70 — κ entropy-production & decay-rate signatures
- **Equation:** dS/dt = ε E_{Z2}/(T_eff t_H); m_f_eff=m_f(1−ε) ⇒ ΔΓ/Γ = 5Δm_f/m_f = −5ε; m_γ_eff²=2α_A κ|Ψ_A|²
- **Source:** op08_kappa_signatures.py §3–§5 (Parts 2–4)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D0, D2 (weak β-decay m_f⁵ dependence), D4 (energy/temperature scales), D6 (κ coupling to matter/photons)
- **Trace:** 1=1 → S6/S7: the κ field couples to O_sustain terms (R⁶, K, |Ψ_A|², |Ψ_B|², ψ̄ψ). A fractional withdrawal ε scales fermion masses, and Γ∝G_F²m_f⁵ (weak decay, **D2**) gives ΔΓ/Γ=−5ε. The photon-mass term gives a CMB-monopole bound. All effects ∝ε (≤10⁻²⁷) are below detection — recorded as observationally null/honest disclosure.
- **Constants:** ε [SELECTED → D6, bounded]; factor 5 [DERIVED ratio]; α_A,|Ψ_A|² [SELECTED → D6].
- **Status:** DERIVED-given-decrees (D6); all signatures below current thresholds.

### EQ-COS-71 — Hubble-tension prediction (Sabbath-boundary H₀ shift)
- **Equation:** ΔH₀/H₀ = f·(ΔK_extrinsic/K_critical) ≈ 0.08 ⇒ ΔH₀ ≈ 5.4 km/s/Mpc (H₀ early=67.4, late≈72.8)
- **Source:** 08-FRIEDMANN_EVOLUTION.md §9.2–9.3 (boxed)
- **Spine path:** S0→S6→S9
- **Decrees:** D0, D1, D4 (H₀, curvature scales), D6 (Sabbath-boundary metric discontinuity, EQ-COS-25), D5 (the order-1 coefficient f / boundary-condition value)
- **Trace:** 1=1 → S6/S9 give H=ȧ/a on a metric with a derivative discontinuity across the Sabbath boundary (the **D6** axiom of EQ-COS-25). The CMB (z>1100) probes the metric near the boundary (H₀=67.4) while the local ladder (z<0.1) probes the relaxed metric (H₀≈73); their *difference* is parametrized as ΔH₀/H₀ = f·(ΔK_extrinsic/K_critical). The functional *form* is forced once the discontinuity is posited, but the coefficient f and the value ≈0.08 are tuned to reproduce the observed ΔH₀≈5.6 km/s/Mpc — a **fitted** match (**D5**), and the underlying discontinuity is itself the posited, un-derived D6 axiom (UNTRACEABLE per EQ-COS-25).
- **Constants:** f, ΔK/K_critical [FIT → D5]; ratio 0.08 [FIT → D5]; H₀ magnitudes [SELECTED scale → D4].
- **Status:** PARTIAL (form rests on the posited D6 Sabbath discontinuity of EQ-COS-25 — itself UNTRACEABLE; the 0.08 coefficient is fitted to the observed tension → D5).

---

## UNTRACEABLE / OPEN ITEMS (coverage audit)

| # | Item (eq id) | Reason it cannot be traced to the spine |
|---|--------------|------------------------------------------|
| 1 | Sabbath-boundary metric discontinuity (EQ-COS-25) | The ȧ jump (factor ~3×10¹⁴) is a **posited axiom** (AXIOM_METRIC_DISCONTINUITY, D6), not derived from S0–S9. The framework's own §D.1 lists "nature of the Sabbath Boundary" as an open question. |
| 2 | H_creation/H₀ ≈ 3×10¹⁴ (EQ-COS-23) | Back-solved from the requirement that stars form/illuminate in 6 days; a fitted ratio (D5). 08-FRIEDMANN_EVOLUTION §D.1 explicitly asks whether this is symmetry-determined or an independent constant — currently undetermined. |
| 3 | Non-Gaussianity f_NL ~ 0.1–1 (EQ-COS-41) | Stated as a qualitative consequence of a "deterministic creation-epoch metric" with no quantitative derivation chain; not reducible to a spine path as written. |
| 4 | Li-7 membrane-catalysis branching b≈0.7 (EQ-COS-59) | The Firmament-catalyzed ⁷Be/⁷Li destruction is an explicitly **speculative, unfinished D6 hypothesis** (sources mark it PARTIAL/OPEN); the branching ratio b is fitted to the observed abundance, not derived. |

**Additional honesty notes:**
- The **energy-budget fractions** Ω_A/Ω_DM/Ω_b (EQ-COS-13), **H₀=67.4** (EQ-COS-14), **A_s/n_s** (EQ-COS-37/38), and **G₄ warp parameters** (EQ-COS-04) are presented as "derived from zone geometry without fitting," but the documents quote Planck values and defer the geometric derivation to unfinished work — so they are tagged **[FIT → D5]** here per the honesty discipline.
- 08-PRECISION_OBSERVABLES.md §4.2 invokes **standard 60-e-fold inflation** (EQ-COS-22) for flatness, which is in tension with the framework's creation-epoch-metric replacement of inflation elsewhere; both are recorded, the tension noted.
- The "creation-epoch metric → 13.8 Gyr coordinate time" mapping (08-RESOLVED_MATTER_FORMATION_TIMELINE.md) rests entirely on EQ-COS-23/-24/-25; its time-dilation integrals are algebra on those decreed inputs, not independent derivations, and the document itself concedes observational indistinguishability from standard cosmology.
- `08-ENERGY_EXTRACTION_CREATION.md` (capacitor E=½CV², source table) and `08-VACUUM_ENERGY_..._NULL_REPLICATION_HISTORY.md` contain no new framework equations beyond textbook formulas applied speculatively; not assigned EQ-COS blocks.

*Cross-ref: `SPINE.md`, `DECREE_REGISTER.md`, `README_SCHEMA.md`.*
