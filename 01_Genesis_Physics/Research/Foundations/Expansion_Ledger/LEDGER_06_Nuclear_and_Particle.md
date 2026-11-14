# Expansion Ledger — Domain 06: Nuclear and Particle Physics

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> Traces EVERY distinct displayed/numbered equation and named key result in
> `Research/Mathematical_Models/06_Nuclear_and_Particle_Physics/` (the `.md` AND `.py`
> files, excluding `00_Archive/`) back to `1=1` via spine rungs S0–S9 (`SPINE.md`) +
> decrees D0–D6 (`DECREE_REGISTER.md`). No equation is "derived from `1=1` alone." Every
> constant is tagged `[DERIVED ratio]`/`[SELECTED scale → D4]`/`[FIT → D5]`/`[count → D3]`.
>
> **Provenance note:** This file REPLACES the earlier "principal-coverage" version (24
> blocks, authored in-loop). This is the EXHAUSTIVE pass: every equation-bearing source
> file was read in full and enumerated, including intermediate results and the equations
> embedded in the op03/op04/op05/op_cp Python scripts. Skipped per schema: `00_Archive/`,
> `__pycache__/`, `test_nuclear_physics.py` scaffolding (its embedded physics is traced
> via the source `.md`/`.py` it validates), and prose/value-tables.

## Header table

| Field | Value |
|-------|-------|
| Domain | Nuclear_and_Particle |
| Equations traced | 108 (EQ-NP-01…108) + 2 UNTRACEABLE (UT-NP-01/02) = 110 items |
| Decrees used across domain | D0, D1, D2, D3, D4, D5, D6 |
| UNTRACEABLE / PARTIAL count | 64 PARTIAL, 44 DERIVED, 2 UNTRACEABLE |

Decree legend: D0 completed-ℝ; D1 dim=6→4; D2 gauge group SU(3)×SU(2)×U(1)/Z₃ orbifold;
D3 winding n_w=3 (⇒ 3 generations); D4 scale anchor Λ_Z0/M_Pl (all dimensionful magnitudes);
D5 fitted O(1) constants (masses, mixing coefficients, δ_CP precise value, SEMF coefficients);
D6 architectural axioms (Ψ_A/Ψ_B condensates, Firmament, open system, sustaining coupling).

**Domain-level finding (unchanged from principal pass, now fully evidenced):** the *structures*
(Yang–Mills, Dirac, confinement, GMOR, CKM ladder, see-saw, Higgs mechanism, Sakharov chain)
trace to the grammar given D2/D3/D6; the *numbers* split sharply. Pure-count results
(3 generations, color-count 3, Δ(n²)=3,5,8, δ_CP=π/3, R=11/3, topological charge ∈ ℤ,
b₀ Casimir ratio) are `[count → D3]` / `[DERIVED ratio]` — the most "of-the-Word" objects here.
Mass values, SEMF coefficients, CKM O(1) Wolfenstein factors, g_A, the baryon-asymmetry
magnitude, and the neutrino mass/mixing numbers are `[FIT → D5]`. This is the densest
concentration of D3 in the whole theory (#849). The two UNTRACEABLE items are the baryon-
asymmetry "enhancement factor ~10²⁰ from zone gradients" and the neutrino tree-level overlap
that is off by ~50 orders before unstated corrections — both fabricated chains by the source's
own admission, recorded honestly below.

---

## I. Gauge Sector — SU(3) Color (`06-SU3_YANG_MILLS_DERIVATION`, `06-QCD_DERIVATION`, `06-QCD_CONFINEMENT_JETS`)

### EQ-NP-01 — SU(3)_C color triplet from Z₃ orbifold winding
- **Equation:** ∮₀^{η_B} ∂_η φ_c dη = 2π n_c/3, n_c∈{0,1,2}; S¹_η compactified as S¹/Z₃ ⇒ color triplet
- **Source:** 06-SU3_YANG_MILLS_DERIVATION.md §1.2–1.4 (lines 73–123); 06-QCD_DERIVATION.md §1.2–1.3; RT2_SU3_Z3_ORBIFOLD (cross-ref EQ-FND-52)
- **Spine path:** S0→S1→S4→S7→S8
- **Decrees:** D2 (Z₃ orbifold / SU(3) selection), D1, D3 (Z₃ winding value ⇒ color-count 3)
- **Trace:** 1=1 → S4 gives the cube root of unity e^{2πi/3} (algebraic-closure root of x³=1); S8 winding/orbifold structure splits fields into 3 charge sectors mod 3; S7 promotes them to the SU(3) gauge family. The *count 3* of colors is fixed by D2/D3 (S8 forces integer winding; D3 fixes its value).
- **Constants:** color-count 3, n_c∈{0,1,2} [count → D3]; e^{2πi/3} [DERIVED ratio].
- **Status:** DERIVED-given-decrees (D1, D2, D3).

### EQ-NP-02 — SU(3) Lie algebra and structure constants
- **Equation:** [T^a, T^b] = i f^{abc} T^c (8 traceless 3×3 generators)
- **Source:** 06-SU3_YANG_MILLS_DERIVATION.md §1.4 (lines 115–123)
- **Spine path:** S0→S1→S5→S7
- **Decrees:** D2
- **Trace:** 1=1 → S5 represents the generators as matrices on the 3D color space; S7 the identity-preserving maps form the Lie algebra; f^{abc} are the SU(3) structure constants (a [DERIVED ratio] from D2's group choice). 8 = dim adjoint of SU(3).
- **Constants:** f^{abc}, 8 generators [DERIVED ratio from D2].
- **Status:** DERIVED-given-decree D2.

### EQ-NP-03 — 6D SU(3) field strength
- **Equation:** F_μν^{(g)} = ∂_μ A_ν^{(g)} − ∂_ν A_μ^{(g)} − i g_s [A_μ^{(g)}, A_ν^{(g)}], A_μ^{(g)} = A_μ^a T^a
- **Source:** 06-SU3_YANG_MILLS_DERIVATION.md §2.1 (lines 131–140)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4 (g_s)
- **Trace:** 1=1 → S7 gives the non-abelian curvature of a connection (the commutator carries f^{abc}); S6 the derivative operators. D2 selects the group; D4 sets g_s.
- **Constants:** g_s [SELECTED scale → D4]; structure-constant content [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-NP-04 — Yang–Mills action (boxed QCD action)
- **Equation:** S_QCD = −(1/4g_s²) ∫ d⁴x √(−g₄) Tr(G_μν^a G^{aμν}); G_μν^a = ∂_μA_ν^a − ∂_νA_μ^a − g_s f^{abc}A_μ^b A_ν^c
- **Source:** 06-SU3_YANG_MILLS_DERIVATION.md §2.3 boxed (lines 188–191); 06-QCD_DERIVATION.md §1.4; 06-QCD_CONFINEMENT_JETS.md §1.1 (cross-ref EQ-FND-28)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4
- **Trace:** 1=1 → S7 SU(3) connection; S6 the ¼F² action density (lowest-order gauge invariant); δS=0 borderline-S6. D2 group, D4 coupling. (S4 dropped: the YM action invokes no phase/circle object beyond the S7 connection.)
- **Constants:** ¼ [DERIVED ratio]; g_s [SELECTED scale → D4].
- **Status:** DERIVED-as-form (δS=0 borderline; given D2, D4).

### EQ-NP-05 — Metric determinant of warped 6D metric
- **Equation:** √(−g₆) = e^{2A+2B} √(−g₄); ds² = e^{2A(η)}[ds₄² − dη²] + e^{2B(η)}dη², A=A₀−(γ/2)η, B=B₀
- **Source:** 06-SU3_YANG_MILLS_DERIVATION.md §1.1, §2.3 step 1 (lines 65–71, 171–174)
- **Spine path:** S0→S1→S3→S9
- **Decrees:** D1, D4 (γ, η_B scales), D6 (Waters-Below zone)
- **Trace:** 1=1 → S9 supplies the warped (RS-like) manifold and its volume element; the exponential warp profile is the D9-profile of S9. D1 fixes the dimension count, D4 the warp parameters, D6 the zone existence.
- **Constants:** γ, η_B, A₀, B₀ [SELECTED scale → D4]; functional form [DERIVED given S9].
- **Status:** DERIVED-given-decrees (D1, D4, D6).

### EQ-NP-06 — Effective 4D strong coupling from extra-dim volume
- **Equation:** 1/g_s² = ∫ dξdη e^{2A+2B} = C₆·V_{waters below}; g_s² = γ/(C₆ e^{2A₀+2B₀})
- **Source:** 06-SU3_YANG_MILLS_DERIVATION.md §2.3–2.4 boxed (lines 184, 200–215)
- **Spine path:** S0→S1→S2→S6→S9
- **Decrees:** D4, D6, D5 (α_s(M_Z) anchor)
- **Trace:** 1=1 → S6/S9 the KK volume integral over the warped Waters-Below; the strong coupling is *defined* by this geometric integral (D6 zone). Its normalization is fixed by matching α_s(M_Z)≈0.118 — a D4/D5 anchor, not a pure derivation.
- **Constants:** C₆, γ, A₀, B₀ [SELECTED scale → D4]; α_s(M_Z) anchor [FIT → D5].
- **Status:** PARTIAL (form DERIVED-given-decrees; magnitude is a scale/fit).

### EQ-NP-07 — Strong coupling definition α_s
- **Equation:** α_s(μ) = g_s²(μ)/(4π); α_s(M_Z) ≈ 0.118
- **Source:** 06-SU3_YANG_MILLS_DERIVATION.md §4.1 (lines 316–320); 06-QCD_DERIVATION.md §1.4 (eq line 128)
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D4, D5 (anchor value)
- **Trace:** 1=1 → S2 the ratio g_s²/(4π); 4π from the S4-circle solid-angle normalization. The numerical 0.118 is matched to PDG (D5).
- **Constants:** 4π [DERIVED ratio]; α_s(M_Z)=0.118 [FIT → D5].
- **Status:** PARTIAL (definition DERIVED; value fitted).

### EQ-NP-08 — QCD β-function / asymptotic freedom
- **Equation:** β(g_s) = μ dg_s/dμ = −β₀ g_s³/(4π)² − …; β₀ = 11 − (2/3)n_f
- **Source:** 06-SU3_YANG_MILLS_DERIVATION.md §4.2 (lines 326–333); 06-QCD_DERIVATION.md §2.3; 06-PRECISION_COMPLETIONS.md §5.5 (cross-ref EQ-FC-20)
- **Spine path:** S0→S1→S2→S6→S7→S8
- **Decrees:** D2, D3 (n_f tied to generation/flavor count)
- **Trace:** 1=1 → S7 one-loop vacuum polarization of the SU(3) field; 11 = (11/3)C_A gluon, 2n_f/3 quark — a **[DERIVED ratio]** of group Casimirs. n_f counts active flavors ⇐ generation count (D3). Negative sign ⇒ asymptotic freedom.
- **Constants:** 11, 2/3 [DERIVED ratio from D2]; n_f [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-NP-09 — One-loop running coupling (integrated β)
- **Equation:** 1/α_s(μ) = 1/α_s(μ₀) + (β₀/2π) ln(μ/μ₀); equivalently 1/α_s(μ)=1/α_s(M_Z)+(7/12π)ln(μ/M_Z), β₀=7 (n_f=6)
- **Source:** 06-SU3_YANG_MILLS_DERIVATION.md §4.2 boxed (lines 336–339); 06-QCD_DERIVATION.md §2.3 (line 168)
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D2, D3, D4, D5 (anchor α_s(M_Z))
- **Trace:** 1=1 → S6 integrates the β-function (a differential equation, S6) to a logarithmic running; β₀ from EQ-NP-08; the anchor α_s(M_Z) is D5.
- **Constants:** β₀=7, 7/12π [DERIVED ratio from D2,D3]; α_s(M_Z) [FIT → D5].
- **Status:** PARTIAL (running DERIVED-given-decrees; anchor fitted).

### EQ-NP-10 — Running coupling (alt. RG form with Λ_QCD)
- **Equation:** α_s(Q) = 4π/(b₀ ln(Q²/Λ_QCD²)) (or 4π/[(11N_c−2N_f)ln(Q/Λ)]); b₀ = 11 − 2N_f/3
- **Source:** 06-QCD_CONFINEMENT_JETS.md §2.2, §4.1 (lines 93–97, 169–173); 06-NUCLEAR_BINDING_PRECISION.md §1.1
- **Spine path:** S0→S1→S2→S6→S7→S8
- **Decrees:** D2, D3, D4 (Λ_QCD)
- **Trace:** Same RG structure as EQ-NP-09, expressed with the confinement scale Λ_QCD as integration constant; Λ_QCD/anchor are D4.
- **Constants:** b₀ [DERIVED ratio]; Λ_QCD [SELECTED scale → D4].
- **Status:** PARTIAL (form DERIVED; Λ_QCD a scale).

### EQ-NP-11 — Confinement scale Λ_QCD from dimensional transmutation
- **Equation:** Λ_QCD/M_Pl = exp(−2π/(b₀ α_s(M_P))); Λ_QCD ≈ 217 MeV (with membrane factor f≈1.8)
- **Source:** 06-QCD_CONFINEMENT_JETS.md §4.2 boxed (lines 184–203)
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D2, D4 (M_Pl anchor), D5 (α_s(M_P)≈1/25 input, f≈1.8 factor)
- **Trace:** 1=1 → dimensional transmutation: the dimensionless coupling and the Planck anchor (D4) generate the IR scale via the exp of the inverse coupling. α_s(M_P)≈1/25 and the membrane factor f≈1.8 are inputs (D5).
- **Constants:** 2π [DERIVED ratio]; M_Pl [SELECTED scale → D4]; α_s(M_P), f [FIT → D5].
- **Status:** PARTIAL (mechanism DERIVED; inputs fitted).

### EQ-NP-12 — String tension from Firmament tension
- **Equation:** σ_str = χ·σ·η_B ≈ 0.18 GeV² = (420 MeV)²
- **Source:** 06-QCD_CONFINEMENT_JETS.md §1.2 boxed (lines 57–65); 06-SU3_YANG_MILLS §3.3
- **Spine path:** S0→S1→S9
- **Decrees:** D4 (σ, η_B scales), D6 (Firmament), D5 (σ_str fitted to lattice value)
- **Trace:** 1=1 → S9 the Firmament-tension (membrane surface energy density, D6) times the zone thickness gives a force-per-length; χ≈1 O(1) factor. Magnitude is a scale/fit to the lattice value.
- **Constants:** χ≈1 [DERIVED ratio]; σ, η_B, σ_str magnitude [SELECTED scale → D4 / FIT → D5].
- **Status:** PARTIAL (form DERIVED-given-D6; magnitude a fit).

### EQ-NP-13 — Wilson loop area law
- **Equation:** ⟨W(C)⟩ = (1/N_c)Tr[P exp(i g_s ∮_C A·dx)] ~ exp(−σ_str·Area(C))
- **Source:** 06-SU3_YANG_MILLS §3.1 (lines 224–237); 06-QCD_CONFINEMENT_JETS §3 boxed (lines 122–159); 06-PRECISION_COMPLETIONS §5.2 boxed
- **Spine path:** S0→S1→S6→S7→S8
- **Decrees:** D2, D4 (σ_str), D6
- **Trace:** 1=1 → S7 holonomy of the SU(3) connection around a loop; S8 the flux-tube/topological confinement (D6 condensate) gives exponential decay in the enclosed area; σ_str sets the rate (D4).
- **Constants:** σ_str [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-NP-14 — Confinement quantization condition (isolated quark forbidden)
- **Equation:** ∮_η A dη = 2πn/3, n∈ℤ; isolated color charge (n≠0) topologically forbidden ⇒ colorless composites only
- **Source:** 06-SU3_YANG_MILLS §3.2 (lines 250–258)
- **Spine path:** S0→S1→S8
- **Decrees:** D2, D3
- **Trace:** 1=1 → S8 the winding around the η-circle is integer-quantized (grammar); the 1/3 from the Z₃ orbifold (D2); non-zero net color violates the quantization at spatial infinity ⇒ confinement. The *count* (3 colors must sum to a singlet) is the D3 integer count.
- **Constants:** 2π/3, color sum = 0 [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-NP-15 — Cornell/linear confinement potential
- **Equation:** V(r) = −(4/3)α_s/r + σ_str·r (boxed; σ_str ≈ 0.18 GeV²)
- **Source:** 06-QCD_CONFINEMENT_JETS §2.2 boxed (lines 85–102); 06-SU3_YANG_MILLS §5.2 (line 433); 06-PRECISION_COMPLETIONS §5.3
- **Spine path:** S0→S1→S6→S8→S9
- **Decrees:** D2, D4, D6
- **Trace:** 1=1 → Coulomb term is one-gluon exchange (S7), the 4/3 is the SU(3) fundamental Casimir [DERIVED ratio from D2]; linear term is the flux tube (S9 + D6 condensate). κ magnitude is D4.
- **Constants:** 4/3 [DERIVED ratio from D2]; α_s (running), σ_str [SELECTED scale → D4].
- **Status:** PARTIAL (form DERIVED-given-decrees; σ_str a scale/fit).

### EQ-NP-16 — Spin-spin (hyperfine) meson splitting
- **Equation:** V_spin = (8/3)α_s δ³(r) S_q·S_q̄
- **Source:** 06-SU3_YANG_MILLS §5.2 (line 468)
- **Spine path:** S0→S1→S5→S7
- **Decrees:** D2, D4
- **Trace:** 1=1 → S7 one-gluon-exchange chromomagnetic interaction; S5 the spin operators; 8/3 a [DERIVED ratio] of SU(3) Casimirs. Sets pseudoscalar/vector mass ordering.
- **Constants:** 8/3 [DERIVED ratio from D2]; α_s [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-NP-17 — Meson radial Schrödinger equation
- **Equation:** [−(ℏ²/2μ)d²/dr² + V(r) + ℓ(ℓ+1)ℏ²/2μr²]ψ = Eψ
- **Source:** 06-SU3_YANG_MILLS §5.2 (lines 443–445)
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D4
- **Trace:** 1=1 → S6 the Schrödinger eigenvalue problem in the confining potential (EQ-NP-15); S5 the angular momentum term; ℏ, μ are scales (D4). Pure grammar given V(r).
- **Constants:** ℏ, μ [SELECTED scale → D4]; ℓ(ℓ+1) [count].
- **Status:** DERIVED-as-form (given D4).

### EQ-NP-18 — Regge trajectory
- **Equation:** M²(L,n) = M₀² + σ_str(L+2n); J = (α_s/π)M² + const
- **Source:** 06-SU3_YANG_MILLS §5.4 (lines 509–514)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D4
- **Trace:** 1=1 → the linear-confinement string (S9) gives M² linear in angular momentum/radial quantum number; σ_str the slope (D4). Standard rotating-string result.
- **Constants:** M₀, σ_str [SELECTED scale → D4]; integers L, n [count].
- **Status:** PARTIAL (form DERIVED; scales fitted).

### EQ-NP-19 — YM stress-energy tensor
- **Equation:** T^μν_YM = (1/g_s²)(F^μ_λ F^{ν,λ} − ¼ η^{μν} F_λ F^λ)
- **Source:** 06-QCD_CONFINEMENT_JETS §1.2 (line 53)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1, D2, D4 (g_s coupling)
- **Trace:** 1=1 → Noether/variation of the YM action w.r.t. the metric (S6/S7) gives the traceless stress tensor; D1 the spacetime to vary, D2 the field content, D4 the coupling g_s in the normalization.
- **Constants:** ¼ [DERIVED ratio]; g_s [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D4).

---

## II. Hadronization, Jets, and the R-ratio (`06-QCD_CONFINEMENT_JETS`, `06-PRECISION_COMPLETIONS`)

### EQ-NP-20 — e⁺e⁻ R-ratio = 11/3
- **Equation:** R = σ(hadrons)/σ(μμ) = 3·Σ_q Q_q² = 11/3 ≈ 3.67 (5 flavors)
- **Source:** 06-QCD_CONFINEMENT_JETS §5.3 boxed (lines 271–280); 06-PRECISION_COMPLETIONS §6.2 (lines 666–668)
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D2, D3 (flavor/generation count)
- **Trace:** 1=1 → S2 the ratio of cross-sections; the overall **factor of 3 is the color count** (D2/D3), and Σ Q_q² = 11/9 is an exact rational from the quark charges (±2/3, ±1/3). R = 11/3 is a pure **[count/DERIVED ratio]** — a clean "of-the-Word" number.
- **Constants:** 3 (colors) [count → D3]; 11/9, Q_q² [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-NP-21 — R-ratio NLO QCD correction
- **Equation:** R(s) = (11/3)[1 + α_s(√s)/π + O(α_s²)]; R ≈ 3.81–3.88
- **Source:** 06-QCD_CONFINEMENT_JETS §5.3 (line 284); 06-PRECISION_COMPLETIONS §6.3 (lines 674–678)
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D2, D4, D5 (α_s anchor)
- **Trace:** 1=1 → first gluon-radiation correction to EQ-NP-20; α_s/π is the one-loop coefficient (S7); α_s value is the running anchor (D5).
- **Constants:** 1/π [DERIVED ratio]; α_s [FIT → D5].
- **Status:** PARTIAL (structure DERIVED; α_s fitted).

### EQ-NP-22 — μ-pair reference cross-section
- **Equation:** σ(e⁺e⁻→μ⁺μ⁻) = 4πα²/3s
- **Source:** 06-QCD_CONFINEMENT_JETS §5.3 (line 249)
- **Spine path:** S0→S1→S2→S4→S7
- **Decrees:** D2, D4
- **Trace:** 1=1 → tree-level QED s-channel photon exchange (U(1) is free from S4, gauged at S7); 4π/3 from phase-space/angular integration; α the EM coupling (D4).
- **Constants:** 4π/3 [DERIVED ratio]; α [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D2, D4).

### EQ-NP-23 — Thrust variable
- **Equation:** T = max_n̂ Σ_i|p_i·n̂| / Σ_i|p_i|; dσ₂/dT ∝ (1−T)² near T→1
- **Source:** 06-QCD_CONFINEMENT_JETS §5.2 (lines 233–237)
- **Spine path:** S0→S1→S5→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S5 the momentum-vector geometry defining the event-shape; the distribution is a QCD radiation prediction (S7). Mostly kinematic definition.
- **Constants:** exponent 2 [DERIVED ratio]; α_s in distribution [FIT → D5].
- **Status:** PARTIAL (definition DERIVED; rate fitted).

### EQ-NP-24 — Gluon-emission splitting probability
- **Equation:** P(z,θ)dz dθ = (α_s N_c/π)·[1+(1−z)²]/z·dθ/θ²
- **Source:** 06-QCD_CONFINEMENT_JETS §6.2 (line 308)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D3 (color-count N_c=3), D4
- **Trace:** 1=1 → S7 the Altarelli–Parisi q→qg splitting kernel; the [1+(1−z)²]/z is the DGLAP P_qq function [DERIVED ratio], N_c=3 the color factor (D2/D3 count). Soft/collinear singularity structure is grammar.
- **Constants:** N_c=3 [count → D3]; P_qq form [DERIVED ratio]; α_s [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-NP-25 — 3-jet fraction (leading-log)
- **Equation:** f₃(y_cut) ≈ (3α_s/π) ln(1/2y_cut); ≈ 14% at LEP
- **Source:** 06-QCD_CONFINEMENT_JETS §6.3 boxed (lines 329–340); 06-PRECISION_COMPLETIONS §6.4 (R₃≈3.2%)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D3 (color-count N_c=3), D4, D5
- **Trace:** 1=1 → integrate EQ-NP-24 over phase space with resolution y_cut; the 3 (=N_c) is the color count (D2/D3) and the log is grammar; α_s the coupling (D5 anchor).
- **Constants:** 3=N_c [count → D3]; α_s [FIT → D5].
- **Status:** PARTIAL (structure DERIVED; α_s fitted).

### EQ-NP-26 — Color flux quantization
- **Equation:** Φ_color = ∫_S E_a·dA = N_c·const; r_core ~ σ_str^{−1/2} ≈ 0.4 fm
- **Source:** 06-QCD_CONFINEMENT_JETS §2.1 (lines 73–79)
- **Spine path:** S0→S1→S8→S9
- **Decrees:** D2, D3 (color-count N_c=3), D4, D6
- **Trace:** 1=1 → S8 the flux through a tube is quantized in units set by N_c (D2/D3 count); S9/D6 the geometric flux-tube of the Firmament; core radius set by σ_str (D4).
- **Constants:** N_c [count → D3]; r_core, σ_str [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-NP-27 — String-breaking condition
- **Equation:** E_tube = σ_str·L > 2m_quark ⇒ L_break ≈ 3.3 fm
- **Source:** 06-QCD_CONFINEMENT_JETS §7.1 (lines 350–356)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D4, D6
- **Trace:** 1=1 → energy balance (S1 additive) between the linear flux-tube energy (S9/D6) and the pair-creation threshold 2m_quark; magnitudes are scales (D4).
- **Constants:** 2, σ_str, m_quark [SELECTED scale → D4].
- **Status:** PARTIAL (form DERIVED; scales fitted).

### EQ-NP-28 — Fragmentation function / hadron multiplicity
- **Equation:** D_π^q(z) ≈ [1+(1−z)²]/z, ∫₀¹ D dz = 1; ⟨n_h⟩ ~ ln(E_jet/m_π)
- **Source:** 06-QCD_CONFINEMENT_JETS §7.2–7.3 (lines 360–390)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4
- **Trace:** 1=1 → the same splitting kernel (EQ-NP-24) integrated gives the fragmentation function; logarithmic multiplicity growth is the QCD cascade (S7). Normalization is a probability sum (S2).
- **Constants:** D_π^q form [DERIVED ratio]; E_jet, m_π [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

---

## III. Mass Spectrum, Generations, Yukawa Hierarchy (`06-SYMMETRIES_MASS_INTEGRATION`, `06-PARTICLE_MASS_SPECTRUM_V3`, `op03_*`, `op04_three_generation_completion`)

### EQ-NP-29 — Three generations from APS index (n_w = 3)
- **Equation:** index(D̸) = c₁ = n_w = 3 ⇒ three same-chirality Weyl zero modes
- **Source:** 06-SYMMETRIES_MASS_INTEGRATION.md (generation structure); 06-PARTICLE_MASS_SPECTRUM_V3 §3.1; op04_three_generation_completion.md; AXIOM_GODHEAD_ZONE_Z0 §4 (cross-ref EQ-FND-29)
- **Spine path:** S0→S1→S4→S8→S9
- **Decrees:** D3 (n_w=3, Postulate F), D1
- **Trace:** 1=1 → S8 the Atiyah–Singer/APS index of the Dirac operator in a winding-n_w Kähler/vortex background is an *integer* (forced by topology — grammar); its *value* equals n_w. **Setting that value to 3 is decree D3** — the single most load-bearing count in the theory, OPEN to derive (#849). Given D3, three generations follow.
- **Constants:** index = 3 = n_w [count → D3].
- **Status:** DERIVED-given-decree D3 (the integer 3 is the irreducible decree; #849).

### EQ-NP-30 — Per-sector index counting (Z₃-equivariant, #849 race result)
- **Equation:** per-sector index = N/3 = 9/3 = 3 color-singlet generations (background fiber winding n_q = 3, covering N = 9)
- **Source:** op04_three_generation_completion.md §3 correction note (lines 74–90); op_cp_phase_winding.py §1 (index = n_w × n_APS = 3); 849 derivation race REFEREE_REPORT
- **Spine path:** S0→S1→S4→S8
- **Decrees:** D3, D2 (Z₃)
- **Trace:** 1=1 → S8 the Z₃-equivariant index; given background fiber winding n_q=3 covering N=9, the per-color-sector index is N/3 = 3. This is the *counting* mechanism for generations (distinct from the radial mass-hierarchy mechanism, EQ-NP-31). All integers here are D3/D2.
- **Constants:** N=9, 3 sectors, index=3 [count → D3].
- **Status:** DERIVED-given-decrees (race-confirmed; counts generations, not masses).

### EQ-NP-31 — Three ξ-bound/resonance states from double-well
- **Equation:** V_ξ(ξ) = V₀[(ξ/η_B)²−1]², V₀=0.002 ⇒ ε₁≈0.124, ε₂≈0.452, ε₃≈0.902 (3 resonances)
- **Source:** op04_three_generation_completion.md §1–2 (lines 33–66); op03_v0_sweep / Vol4 Ch10
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D6 (Ψ_B condensate sets V₀), D4 (η_B scale), D3 (the "exactly 3" sub-threshold count), D5 (V₀ value from condensate fit)
- **Trace:** 1=1 → S6 Sturm–Liouville eigenvalues of the double-well scalar potential (S2 quartic); the three sub-threshold states are the *mass-hierarchy ladder* (NOT the generation count — see correction note in source). V₀ from the Waters-Below condensate (D6); its value is fitted (D5).
- **Constants:** V₀=0.002 [SELECTED scale → D4 / from D6 condensate, value FIT → D5]; ε_n eigenvalues [DERIVED ratio]; "exactly 3" [count → D3].
- **Status:** PARTIAL (eigenvalues DERIVED-given-decrees; V₀ from condensate is D6/D5).

### EQ-NP-32 — Fundamental fermion mass formula
- **Equation:** m_f = y_f·v/√2 = y_f·174 GeV (boxed)
- **Source:** 06-PARTICLE_MASS_SPECTRUM_V3 §3.6 boxed (line 184); 06-HIGGS §7.1 (line 704); 06-SYMMETRIES_MASS §2 (line 78)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D4 (v scale), D6 (Higgs/Ψ_A condensate), D5 (individual y_f matched to data)
- **Trace:** 1=1 → S7 spontaneous SU(2)×U(1) breaking by the Ψ_A condensate VEV (D6) gives fermion masses via the Yukawa term; v/√2 from the doublet convention. v scale is D4; the individual Yukawas y_f are fitted (D5).
- **Constants:** 1/√2 [DERIVED ratio]; v [SELECTED scale → D4]; y_f [DERIVED ratio / FIT → D5].
- **Status:** DERIVED-given-decrees (mechanism); individual y_f are PARTIAL/FIT.

### EQ-NP-33 — Yukawa hierarchy from condensate overlap exp(−αn²)
- **Equation:** y_n = y₀ exp(−α n²) (boxed), α ≈ 1.0; m_n = y_n v
- **Source:** 06-PARTICLE_MASS_SPECTRUM_V3 §3.5 boxed (line 154); 06-HIGGS §7.3 boxed (line 756); op03_condensate_yukawa.py; op03_wkb_tunneling.py (cross-ref EQ-FC-22)
- **Spine path:** S0→S1→S2→S6→S8→S9
- **Decrees:** D3 (n=1,2,3 modes), D4 (scale v), D5 (~20% residual)
- **Trace:** 1=1 → S6 overlap integrals of the three vortex zero-modes (S8/D3) with the Firmament-localized Higgs profile give exponentially-split Yukawas; the exp(−αn²) *form* is grammar+D3, α≈0.98 partly derived (EQ-NP-35); the ~20% accuracy is the honest residual (D5).
- **Constants:** n=1,2,3 [count → D3]; α≈0.98 [DERIVED ratio, ~20% → D5].
- **Status:** PARTIAL (mechanism DERIVED-given-decrees; residuals open).

### EQ-NP-34 — WKB action gives n² scaling (parabolic barrier)
- **Equation:** S_n = √(2V₀) n²Δξ²/(2L); α = √(2V₀)Δξ²/(2L); y_n = exp(−S_n)
- **Source:** op03_wkb_tunneling.py Parts 1–4 (lines 99–134, 316–334); op03_condensate_yukawa.py
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D4 (V₀, Δξ, L scales), D6 (condensate barrier), D5 (α=1.0 combination fitted)
- **Trace:** 1=1 → S6 semiclassical (WKB) tunneling integral through the parabolic barrier V(ξ)=V₀(ξ/L)²; the n² scaling is an exact analytic consequence (S3 real integral) of the quadratic barrier with evenly-spaced generations. The parabolic shape is the unique power law giving n²; barrier from D6 condensate. The combination that fixes α≈1.0 is fitted (D5).
- **Constants:** 2 [DERIVED ratio]; V₀, Δξ, L [SELECTED scale → D4]; α=1.0 combination [FIT → D5].
- **Status:** PARTIAL (n² scaling DERIVED-as-form; α-fixing combination fitted).

### EQ-NP-35 — α from Waters-Below condensate parameters
- **Equation:** V₀ = (m_Bc²/(ℏc/η_B))²; α = √(2V₀)Δξ²/(2L); m_Bc² ≈ 1–3.3 GeV ⇒ α ≈ 0.076–1.0
- **Source:** op03_condensate_yukawa.py §2–5 (lines 92–219); op03_condensate_action.py
- **Spine path:** S0→S1→S2→S6→S9
- **Decrees:** D4 (η_B), D6 (Ψ_B condensate mass m_B), D5 (residual factor ~13)
- **Trace:** 1=1 → V₀ is set by the ratio of the condensate mass m_B (D6) to the UV scale ℏc/η_B (D4); the computed α≈0.076 is a factor ~13 below the required α≈1.0 — the source flags this as an unresolved gap (D5). Honest negative content.
- **Constants:** m_Bc², η_B [SELECTED scale → D4]; factor-13 shortfall [FIT → D5 / open].
- **Status:** PARTIAL (mechanism DERIVED; ~13× discrepancy is an honest open residual).

### EQ-NP-36 — Condensate BVP kink solution and V₀ derivation
- **Equation:** Φ″ = κ²(Φ−Φ³), Φ(0)=0, Φ(∞)=1 ⇒ Φ(η′)=tanh(κη′/√2); V₀ = κ²/2; κ = m_B η_B
- **Source:** op03_condensate_bvp_solve.py §2 (lines 53–67); op03_condensate_action.py
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D6 (Ψ_B), D4 (κ scale)
- **Trace:** 1=1 → S6 the φ⁴ domain-wall kink is the exact stationary (δS=0) solution of the 1D scalar BVP with the double-well S2 potential; boundary conditions 0→1 give the tanh profile; V₀=κ²/2 is then *derived* (not assumed) from the near-Firmament slope. D6 supplies Ψ_B.
- **Constants:** √2, κ²/2 [DERIVED ratio]; κ=m_Bη_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (clean kink; V₀ derived).

### EQ-NP-37 — Condensate action and Mexican-hat VEV
- **Equation:** S[Ψ_B]=∫dη[½(Ψ_B′)²+V(Ψ_B)]; U=−(m_B²/2)Ψ_B²+(λ_B/4!)Ψ_B⁴; Ψ_{B,0}²=6m_B²/λ_B; m_kink=√2 m_B
- **Source:** op03_condensate_action.py §2 (lines 70–96); op03_condensate_yukawa.py §2
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D6, D4
- **Trace:** 1=1 → S2 the double-well quartic potential; S6 the stationary VEV from dU/dΨ=0 and the standard φ⁴-kink mass √2 m_B (Rajaraman). D6 supplies the condensate, D4 the scales.
- **Constants:** 6, √2, 1/4! [DERIVED ratio]; m_B, λ_B [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-NP-38 — m_B identified with charmonium scale
- **Equation:** required m_Bc² ≈ 3.31 GeV ≈ m_{J/ψ}; m_B from kink width = √2·ℏc/η_B ≈ 0.21 GeV (factor-~15 RG gap)
- **Source:** op03_condensate_action.py §4–7 (lines 134–271)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D5 (RG factor ~15 not derived), D6
- **Trace:** 1=1 → two constraints (kink-width vs. observed-α) give m_B differing by ~15×; the source attributes this to unwritten RG running of the condensate mass and identifies the effective scale with charmonium. The factor 15 is an honest un-derived gap (D5).
- **Constants:** m_{J/ψ}=3.097 GeV [SELECTED scale → D4]; factor ~15 [FIT → D5 / open].
- **Status:** PARTIAL (scale identified; RG derivation of factor 15 OPEN).

### EQ-NP-39 — Yukawa mode eigenfunctions and KK mass
- **Equation:** ψ_{n_ξ}(ξ)=√(2/ξ_A)sin(n_ξπξ/ξ_A); m_{n_ξ}² = (ℏc)²(n_ξπ/ξ_A)²
- **Source:** 06-HIGGS §1.3 boxed (line 147); 06-PARTICLE_MASS_SPECTRUM_V3 §3.4; 06-SYMMETRIES_MASS §3; 06-REMAINING_DERIVATIONS §2.2, §3.1
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D1, D4 (ξ_A), D6, D3 (KK mode index n count)
- **Trace:** 1=1 → S6 the 1D Klein–Gordon/Sturm–Liouville eigenproblem on [0,ξ_A] with Dirichlet BC at the Firmament gives sine modes with quantized k=nπ/ξ_A; S5 the orthonormal mode basis. D1 the extra dimension, D4 the zone size, D6 the Waters-Above field, D3 the discrete mode index n.
- **Constants:** √(2/ξ_A), nπ/ξ_A [DERIVED ratio]; ξ_A [SELECTED scale → D4]; n [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-NP-40 — Yukawa overlap integral (Gaussian-Higgs suppression)
- **Equation:** y_{n_ξ} = λ₀∫₀^{ξ_A}ψ_{n_ξ}(ξ)H(ξ)ψ₁(ξ)dξ ∝ exp(−n²π²ξ₀²/2ξ_A²); H(ξ)=A exp(−ξ²/2ξ₀²)
- **Source:** 06-HIGGS §7.2, App B.2 (lines 710, 1013); 06-PARTICLE_MASS_SPECTRUM_V3 §3.4; 06-SYMMETRIES_MASS §3 (line 211)
- **Spine path:** S0→S1→S2→S6→S9
- **Decrees:** D4 (ξ₀, ξ_A), D6 (Higgs profile)
- **Trace:** 1=1 → S6 the oscillatory-integral of a rapidly-oscillating sine mode against a smooth localized Higgs Gaussian yields exponential suppression (standard oscillatory-integral theory); this *derives* the exp(−αn²) form of EQ-NP-33. λ₀, ξ₀ are scales (D4/D6).
- **Constants:** λ₀, ξ₀, ξ_A [SELECTED scale → D4]; suppression exponent [DERIVED ratio].
- **Status:** DERIVED-given-decrees (form); absolute scale PARTIAL.

### EQ-NP-41 — 6D Dirac equation for matter
- **Equation:** (iγ^A e_A^M D_M − m)Ψ = 0; [γ^A D_A + m₀]Ψ = 0
- **Source:** 06-SYMMETRIES_MASS_INTEGRATION.md; 06-NEUTRINO_PHYSICS §2.1 (line 104); 06-WEAK_PARITY App B; ACTION_6D §10.3 (cross-ref EQ-FND-29)
- **Spine path:** S0→S1→S4→S7→S9
- **Decrees:** D1, D3, D4, D6
- **Trace:** 1=1 → S4 (i, ℂ) + S9 (vielbein/spin connection) give the Clifford operator and Dirac equation; δS=0 the EOM (S6 borderline). D1 fixes the 6D spinor dimension; D3 the zero-mode count; D6 the field content.
- **Constants:** m, m₀ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-NP-42 — Clifford algebra / gamma matrices
- **Equation:** {γ^A, γ^B} = 2 g^{AB} 𝟙
- **Source:** 06-SYMMETRIES_MASS_INTEGRATION.md; 06-NEUTRINO_PHYSICS §2.1 (line 107); FERMION_EMERGENCE_FROM_MEMBRANE
- **Spine path:** S0→S1→S4→S5→S9
- **Decrees:** D1
- **Trace:** 1=1 → S4 the requirement of a "square root" of the metric/Laplacian forces anticommuting generators (x²=−1→i generalized); S5 the matrix representation. *Existence* is grammar; the *dimension* (number of γ's = 6) is D1.
- **Constants:** dimension 6 [count → D1]; 2 [DERIVED ratio].
- **Status:** DERIVED-given-decree D1.

### EQ-NP-43 — 6D chirality operator
- **Equation:** γ⁷ = γ⁰γ¹γ²γ³γ⁴γ⁵ = −iγ⁰…γ^η; Ψ_{L,R} = (1∓γ⁷)/2 Ψ
- **Source:** 06-NEUTRINO_PHYSICS §2.1, §9.1 (lines 122, 667); 06-WEAK_PARITY §5.2
- **Spine path:** S0→S1→S4→S5→S9
- **Decrees:** D1
- **Trace:** 1=1 → S4/S5 the product of all 6 γ's defines the chirality grading; left/right projectors split the spinor. D1 the dimension count (6 γ's). Pure grammar given D1.
- **Constants:** ½ projectors [DERIVED ratio]; 6 factors [count → D1].
- **Status:** DERIVED-given-decree D1.

### EQ-NP-44 — Generation Yukawas / lepton mass values
- **Equation:** y_e≈2.94e−6, y_μ≈6.1e−4, y_τ≈1.02e−2; m_e/m_μ/m_τ via m=y v/√2; ratios exp(4α)≈207, exp(5α)≈16.8
- **Source:** 06-PARTICLE_MASS_SPECTRUM_V3 §4.2, §5.1 (lines 215–246, 358–360); 06-SYMMETRIES_MASS §"Are masses sensible"
- **Spine path:** S0→S1→S2→S6→S8→S9
- **Decrees:** D3, D4, D5
- **Trace:** 1=1 → mass formula (EQ-NP-32) + hierarchy (EQ-NP-33) with τ as the **calibration anchor** (D5); residuals are accuracy facts (electron +17%, muon −15…19%, tau = anchor) per Vol4 Ch10_FINAL.
- **Constants:** y_f values, masses [SELECTED scale → D4]; residuals/anchor [FIT → D5]; n=1,2,3 [count → D3].
- **Status:** PARTIAL (mechanism given decrees; tau is anchor not prediction; honest residuals).

### EQ-NP-45 — Quark mass values (tree level + honest failures)
- **Equation:** m_q = y_q v/√2; light quarks ~3–7% (u,d,s); heavy quarks (c,t,b) **fail at tree level** (FIT at calibration scale)
- **Source:** 06-PARTICLE_MASS_SPECTRUM_V3 §4.4–4.5 (lines 270–334); SPECTRUM_COMPLETIONS §4.1; REMAINING_DERIVATIONS §4
- **Spine path:** S0→S1→S2→S6→S8→S9
- **Decrees:** D3, D4, D5
- **Trace:** 1=1 → same Yukawa mechanism; light-quark masses ~few-% accurate, but c/b/t do NOT come out parameter-free — the "<1%" figures are calibration-scale fits (D5), honestly flagged in the source's canonical-status banner.
- **Constants:** m_q [SELECTED scale → D4]; heavy-quark fits [FIT → D5].
- **Status:** PARTIAL (light quarks approximate; heavy quarks fitted — honest).

### EQ-NP-46 — Proton mass from QCD binding
- **Equation:** m_p = 2m_u + m_d + E_QCD, E_QCD ≈ 929 MeV ⇒ m_p ≈ 938.3 MeV
- **Source:** 06-PARTICLE_MASS_SPECTRUM_V3 §5.4 (lines 392–413)
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D2, D4, D6, D5
- **Trace:** 1=1 → the bulk of the nucleon mass is QCD binding/condensate energy (S7/S9 confinement + D6 chiral condensate), not the current quark masses; E_QCD from the running coupling. Agreement (0.01%) is "credit shared with QCD," not a pure framework prediction.
- **Constants:** E_QCD [SELECTED scale → D4]; ⟨q̄q⟩ contribution [from D6].
- **Status:** PARTIAL (dominated by QCD binding; framework-shared).

### EQ-NP-47 — Neutron–proton mass difference
- **Equation:** Δm = (m_d−m_u) + ΔE_em + ΔE_QCD ≈ 1.24 MeV
- **Source:** 06-PARTICLE_MASS_SPECTRUM_V3 §5.5 (lines 419–433)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D5
- **Trace:** 1=1 → S1 additive mass balance: quark-mass difference plus EM self-energy (negative) plus small QCD correction. EM term needs detailed calc (D5).
- **Constants:** m_d−m_u, ΔE_em [SELECTED scale → D4]; EM correction [FIT → D5].
- **Status:** PARTIAL (mechanism understood; EM correction approximate, ~4%).

---

## IV. Electroweak Sector — Higgs, W/Z, Couplings (`06-HIGGS_DERIVATION`, `06-ELECTROWEAK_PROTON_STABILITY`, `06-WEAK_PARITY_CP_VIOLATION`, `06-PRECISION_COMPLETIONS`, `06-REMAINING_DERIVATIONS`, `op04_composite_higgs`)

### EQ-NP-48 — Higgs Mexican-hat potential and VEV
- **Equation:** V_eff(H) = −μ²|H|² + (λ/4)|H|⁴ (boxed); |H|²_vev = 2μ²/λ; v = 2μ/√λ (boxed); v = 246.22 GeV
- **Source:** 06-HIGGS §2.2, §3.2–3.3 boxed (lines 272, 311, 340, 352); 06-ELECTROWEAK §1.3; REMAINING_DERIVATIONS §5.2
- **Spine path:** S0→S1→S2→S6→S9
- **Decrees:** D4 (μ scale), D6 (Ψ_A condensate)
- **Trace:** 1=1 → S2 the quartic double-well; the negative μ² is generated by the Firmament-tension boundary term (D6); minimizing (S6) gives the VEV. The negative-μ² *mechanism* is D6; v's absolute value is a fitted/measured scale (D4).
- **Constants:** ¼ [DERIVED ratio]; μ≈88.4 GeV, v=246 GeV [SELECTED scale → D4]; λ [DERIVED/FIT].
- **Status:** PARTIAL (mechanism DERIVED-given-D6; v anchored to data).

### EQ-NP-49 — Firmament-tension origin of μ²
- **Equation:** μ² ∝ σ c²/ξ_A² ≈ (88.4 GeV)²; ΔV_membrane = −β σ (c²/ξ_A²)|H|²
- **Source:** 06-HIGGS §1.2, §2.2, §8.2 (lines 95, 262, 829); REMAINING_DERIVATIONS §7.2
- **Spine path:** S0→S1→S9
- **Decrees:** D4 (σ, ξ_A), D6 (Firmament tension)
- **Trace:** 1=1 → S9 the Planck-scale Firmament tension σ (D6) is geometrically suppressed by ξ_A⁻² to the electroweak scale; β an O(1) factor. The source's "hierarchy solution" — but the source itself (REMAINING_DERIVATIONS §7) flags this as circular/using v as a free parameter.
- **Constants:** β O(1) [DERIVED ratio]; σ, ξ_A [SELECTED scale → D4].
- **Status:** PARTIAL (geometric-suppression form DERIVED-given-D6; absolute scale is a fit — naturalness unresolved per source).

### EQ-NP-50 — Higgs mass from potential curvature
- **Equation:** m_H² = 2λv² (boxed m_H = √(2λ) v); λ = m_H²/2v² = 0.129; m_H ≈ 125.1 GeV
- **Source:** 06-HIGGS §6.1–6.2 boxed (lines 639, 641); 06-ELECTROWEAK §3.4; REMAINING_DERIVATIONS §5.2.2
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D5 (λ from data)
- **Trace:** 1=1 → S6 the second derivative of the potential at the VEV gives m_H²=2λv². With v measured and λ=0.129 extracted from the measured m_H, this is a *consistency relation*, not a parameter-free prediction (λ is fitted/input, D5).
- **Constants:** 2 [DERIVED ratio]; v [SELECTED scale → D4]; λ=0.129 [FIT → D5].
- **Status:** PARTIAL (form DERIVED; λ fitted to data).

### EQ-NP-51 — Higgs quartic from KK overlap integrals
- **Equation:** λ = λ_A·I_ξ·I_η = λ_A·9/(4ξ_Aη_B); I_ξ=∫ψ₁⁴=3/2ξ_A, I_η=3/2η_B
- **Source:** 06-HIGGS §4.1 (lines 421–445)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D6
- **Trace:** 1=1 → S6 the ∫sin⁴ overlap integrals (using sin⁴ = (3−4cos2u+cos4u)/8) give the 3/2 factors [DERIVED ratio]; λ_A the 6D coupling (D6). Relates 4D λ to 6D coupling × zone geometry.
- **Constants:** 9/4, 3/2 [DERIVED ratio]; λ_A, ξ_A, η_B [SELECTED scale → D4].
- **Status:** PARTIAL (overlap form DERIVED; λ_A absolute value undetermined).

### EQ-NP-52 — Covariant derivative and Goldstone "eating"
- **Equation:** D_μH = (∂_μ − ig W_μ^a T^a − ig′ B_μ Y)H; 3 Goldstones → longitudinal W±,Z; photon massless
- **Source:** 06-HIGGS §3.4, §5.1 (lines 378, 494); 06-ELECTROWEAK §1.4; REMAINING_DERIVATIONS §6.2
- **Spine path:** S0→S1→S4→S7
- **Decrees:** D2, D4 (g, g′ couplings)
- **Trace:** 1=1 → S7 the SU(2)×U(1) connection (D2) acting on the Higgs doublet; spontaneous breaking gives 3 massive vectors + 1 massless photon by the Goldstone theorem (grammar of S7). The gauge couplings g, g′ are scales (D4).
- **Constants:** g, g′, Y [SELECTED scale → D4]; count of Goldstones [count].
- **Status:** DERIVED-given-decree D2.

### EQ-NP-53 — W boson mass
- **Equation:** M_W = gv/2 (boxed); ≈ 80.27–80.4 GeV
- **Source:** 06-HIGGS §5.2 boxed (line 535); 06-ELECTROWEAK §4.2 boxed (line 257); 06-WEAK_PARITY §3.2 boxed (line 226); PRECISION_COMPLETIONS §3.1; REMAINING_DERIVATIONS §6.3.1
- **Spine path:** S0→S1→S4→S7
- **Decrees:** D2, D4
- **Trace:** 1=1 → S7 the W mass term from |D_μ⟨H⟩|² at the VEV; M_W = gv/2 exactly. D2 the group, D4 the scales g, v.
- **Constants:** ½ [DERIVED ratio]; g, v [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-NP-54 — Z boson mass and Weinberg angle
- **Equation:** M_Z = M_W/cosθ_W = v√(g²+g′²)/2 (boxed); cosθ_W=g/√(g²+g′²); tanθ_W=g′/g; sin²θ_W≈0.2312
- **Source:** 06-HIGGS §5.3 boxed (line 567); 06-ELECTROWEAK §5.2–5.3 boxed (lines 307, 312); 06-WEAK_PARITY §3.3 boxed (line 240); REMAINING_DERIVATIONS §6.3.2
- **Spine path:** S0→S1→S4→S7
- **Decrees:** D2, D4, D5 (θ_W value)
- **Trace:** 1=1 → S7 the neutral W³–B mixing diagonalizes to Z + massless photon; the Weinberg angle is the mixing parameter. Form DERIVED; sin²θ_W=0.2312 fitted (D5).
- **Constants:** cosθ_W [DERIVED ratio given g,g′]; θ_W value [FIT → D5]; g,g′,v [SELECTED scale → D4].
- **Status:** PARTIAL (form DERIVED-given-decrees; θ_W fitted).

### EQ-NP-55 — Weinberg angle from gauge-coupling ratio
- **Equation:** sin²θ_W = α_Y/(α_W+α_Y) = 1 − M_W²/M_Z²; tanθ_W=g′/g=√(α_Y/α_W)
- **Source:** 06-ELECTROWEAK §6.3 (line 387); REMAINING_DERIVATIONS §6.4.1 (line 746)
- **Spine path:** S0→S1→S2→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S2/S7 the ratio of the two running couplings (from membrane geometry, D2) gives the mixing angle; α_W, α_Y at M_Z are anchored to data (D5).
- **Constants:** α_W, α_Y [FIT → D5]; ratio form [DERIVED].
- **Status:** PARTIAL (form DERIVED; couplings fitted).

### EQ-NP-56 — ρ parameter
- **Equation:** ρ = M_W²/(M_Z²cos²θ_W) = 1 (tree); Δρ = 3g²/(16π²cos²θ_W)[m_t²/M_W² − …] ≈ 3.7e−5
- **Source:** 06-HIGGS §5.5 (line 597); REMAINING_DERIVATIONS §6.5.1 (lines 776–802)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S7 custodial symmetry forces ρ=1 at tree level; the one-loop Δρ from top/Higgs loops (S6 perturbation). Loop coefficients [DERIVED ratio]; m_t, m_H inputs (D4/D5).
- **Constants:** 3/16π² [DERIVED ratio]; m_t, m_H [SELECTED scale → D4].
- **Status:** PARTIAL (tree DERIVED; loop uses fitted masses).

### EQ-NP-57 — Fermion mass from Yukawa (electroweak form)
- **Equation:** L_Y = −y_f f̄_L H f_R + h.c. ⇒ m_f = y_f v/√2 (boxed); g_{Hff̄} = m_f/v
- **Source:** 06-ELECTROWEAK §3.2 boxed (line 179); 06-HIGGS §7.1; PRECISION_COMPLETIONS §2.3; REMAINING_DERIVATIONS §5.3.1
- **Spine path:** S0→S1→S7→S9
- **Decrees:** D2, D4, D6, D5 (y_f fitted, as in EQ-NP-32)
- **Trace:** Duplicate of EQ-NP-32 in the explicit SU(2)×U(1) Yukawa form; Higgs coupling proportional to mass. D2 the group, D6 the condensate; the y_f are fitted (D5).
- **Constants:** 1/√2 [DERIVED ratio]; v, y_f [SELECTED scale → D4 / FIT → D5].
- **Status:** DERIVED-given-decrees (mechanism); values fitted.

### EQ-NP-58 — Higgs partial width and branching ratios
- **Equation:** Γ_{H→ff̄} = N_c m_f² y_f²/(8πv²)·(m_H−2m_f)^{1/2}; g_{HWW}=2M_W/v, g_{HZZ}=2M_Z/v
- **Source:** 06-PRECISION_COMPLETIONS §2.2–2.4 (lines 193–262); 06-ELECTROWEAK §3.6; REMAINING_DERIVATIONS §5.4
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S6/S7 tree-level decay rate from the Yukawa/gauge vertices (Fermi golden rule, EQ-NP-69); N_c=3 color factor (D2). Couplings ∝ mass (D4); branching ratios then computed.
- **Constants:** N_c, 1/8π [DERIVED ratio]; m_f, M_W, M_Z, v [SELECTED scale → D4]; α_s NLO factors [FIT → D5].
- **Status:** PARTIAL (form DERIVED-given-decrees; ~13% accuracy, NNLO missing).

### EQ-NP-59 — W and Z partial widths
- **Equation:** Γ(W→f₁f̄₂) = g²/(48π)M_W³|V_{f₁f₂}|²N_c; Γ(Z→ff̄) = g²/(48πcos²θ_W)M_Z³(c_V−c_A)²
- **Source:** 06-PRECISION_COMPLETIONS §3.2, §4.2 (lines 365, 433); REMAINING_DERIVATIONS §6.5.3
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S7 tree-level gauge-boson decay to fermion pairs; 1/48π phase-space factor [DERIVED ratio], N_c color and CKM |V|² weights (D2/D3/D5).
- **Constants:** 1/48π, N_c [DERIVED ratio]; |V_{ij}|², θ_W [FIT → D5]; g, M_W, M_Z [SELECTED scale → D4].
- **Status:** PARTIAL (form DERIVED; inputs fitted).

### EQ-NP-60 — Z neutral-current couplings
- **Equation:** g_L^f = T₃^f − sin²θ_W Q_f; g_R^f = −sin²θ_W Q_f; c_V^f, c_A^f
- **Source:** 06-ELECTROWEAK §5.4 (lines 330–331); 06-PRECISION_COMPLETIONS §4.2 (lines 440–449)
- **Spine path:** S0→S1→S7
- **Decrees:** D2, D5 (θ_W)
- **Trace:** 1=1 → S7 the neutral-current coupling structure from SU(2)×U(1) charge assignments (T₃, Q, Y); the weak isospin/charge values are group representation data (D2). sin²θ_W is fitted (D5).
- **Constants:** T₃, Q [count, group reps]; sin²θ_W [FIT → D5].
- **Status:** PARTIAL (structure DERIVED-given-D2; θ_W fitted).

### EQ-NP-61 — Forward-backward asymmetry
- **Equation:** A_FB^f = (3/4)A_e A_f; A_f = 2c_A^f(c_V^f+c_A^f)/[(c_V^f)²+(c_A^f)²]
- **Source:** 06-PRECISION_COMPLETIONS §4.3 (lines 477–482)
- **Spine path:** S0→S1→S7
- **Decrees:** D2, D5
- **Trace:** 1=1 → S7 the V–A interference in Z exchange gives the forward-backward asymmetry; the 3/4 from angular integration [DERIVED ratio]; couplings from EQ-NP-60 (θ_W fitted).
- **Constants:** 3/4 [DERIVED ratio]; c_V, c_A via θ_W [FIT → D5].
- **Status:** PARTIAL (form DERIVED; couplings fitted).

### EQ-NP-62 — Number of light neutrino species from invisible width
- **Equation:** N_ν = Γ_inv/Γ(Z→ℓℓ); Γ(Z→νν̄)≈0.5 GeV, N_ν ≈ 3
- **Source:** 06-PRECISION_COMPLETIONS §4.4 (lines 512–518)
- **Source-note:** the documents' arithmetic (0.500/0.0836=5.99) is the *partial-width-per-species ratio*; the physical N_ν≈3 (=2.984) is the count.
- **Spine path:** S0→S1→S7→S8
- **Decrees:** D3
- **Trace:** 1=1 → the invisible Z width counts light neutrino species; the result N_ν=3 is the generation **count** (D3). A genuine "of-the-Word" integer the framework predicts.
- **Constants:** N_ν = 3 [count → D3].
- **Status:** DERIVED-given-decree D3.

### EQ-NP-63 — Higgs self-coupling / β-function stability
- **Equation:** β_λ = (1/16π²)[12λ² − 3y_t⁴ + β_WA(λ_A)]; Waters-Above term keeps λ>0
- **Source:** 06-HIGGS §6.3 (lines 671–679)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D6, D5
- **Trace:** 1=1 → S6/S7 the RG running of the quartic; 12λ²−3y_t⁴ standard SM coefficients [DERIVED ratio], plus a positive Waters-Above (D6) contribution that prevents vacuum instability.
- **Constants:** 12, 3, 1/16π² [DERIVED ratio]; β_WA [from D6, undetermined].
- **Status:** PARTIAL (SM part DERIVED; D6 contribution qualitative).

### EQ-NP-64 — Fermi constant from W exchange
- **Equation:** G_F = g_W²/(4√2 M_W²) = 1/(√2 v²) (boxed); ≈ 1.166e−5 GeV⁻²
- **Source:** 06-WEAK_PARITY §4.1–4.2 boxed (lines 287, 299); 06-HIGGS App D.4; 06-NUCLEAR_DECAY §5.2
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4
- **Trace:** 1=1 → S6 integrating out the heavy W (propagator → 1/M_W²) gives the four-fermi contact interaction; substituting M_W=gv/2 yields G_F=1/(√2 v²). Exact given M_W, v (D4).
- **Constants:** 1/4√2, 1/√2 [DERIVED ratio]; v, M_W [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (exact given measured M_W, v).

### EQ-NP-65 — V−A structure / maximal parity violation
- **Equation:** W couples to (1−γ⁵)/2 ψ ⇒ g_V = g_A; asymmetry A = −1
- **Source:** 06-WEAK_PARITY §5.3–5.5 boxed (lines 374, 391, 401–414)
- **Spine path:** S0→S1→S4→S7→S9
- **Decrees:** D2, D6 (asymmetric Firmament boundary)
- **Trace:** 1=1 → S9 the asymmetric ξ-boundary (no ξ<0 mirror; D6) makes the W overlap with left-handed (even-parity) modes only and vanish for right-handed (odd-parity); chirality (S4 γ⁷) correlates with ξ-parity ⇒ V−A. **Derived given adopted axioms** (not inserted by hand) — the source's key contrast with the SM.
- **Constants:** A=−1 [DERIVED ratio]; g_V=g_A [DERIVED given D6].
- **Status:** DERIVED-given-decrees (D2, D6).

### EQ-NP-66 — Composite Higgs compositeness scale f
- **Equation:** f = v√(V_warp/η_B²) = v√249.6 ≈ 3886 GeV; sinθ_mis = v/f; v = f sinθ_mis (MCHM)
- **Source:** op04_composite_higgs.py §1 (lines 96–112); op_cp_phase_winding.py
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D4 (V_warp, η_B), D6 (Ψ_A condensate), D5 (sinθ_mis = v/f free parameter)
- **Trace:** 1=1 → S9 the warp-volume integral V_warp=249.6η_B² (from OP-07) sets the compositeness scale f = v√(V_warp/η_B²); the Higgs is a pNGB of the Ψ_A condensate (D6). Same warp ratio that gives α_6D. v/f is the one remaining free parameter (θ_mis), fitted (D5).
- **Constants:** √249.6 [DERIVED ratio from V_warp]; V_warp, η_B [SELECTED scale → D4]; sinθ_mis [FIT → D5].
- **Status:** PARTIAL (f DERIVED-given-decrees; θ_mis / v one free parameter).

### EQ-NP-67 — Composite Higgs mass from Coleman–Weinberg
- **Equation:** m_H² = (3y_t²/4π²)m_t² ln(f²/m_t²) + (9/16π²)g²m_W²ln(f²/m_W²); m_H ≈ 119–125 GeV (≈123, 1.5%)
- **Source:** op04_composite_higgs.py §3–3b (lines 200–238); EQ-NP-09 cross-ref; AXIOM_GODHEAD §"Research Gaps"
- **Spine path:** S0→S1→S6→S7→S9
- **Decrees:** D2, D4, D6, D5 (residual)
- **Trace:** 1=1 → S6 the Coleman–Weinberg one-loop effective potential dominated by the top loop (m_t(h)=y_t f sin(h/f)), with positive gauge-loop correction; the curvature at the minimum gives m_H. Coefficients [DERIVED ratio]; value 123 GeV has ~1.5% residual (D5).
- **Constants:** 3/4π², 9/16π² [DERIVED ratio]; y_t, m_t, f, g [SELECTED scale → D4]; 1.5% residual [FIT → D5].
- **Status:** PARTIAL (mechanism DERIVED-given-decrees; value to 1.5%).

### EQ-NP-68 — MCHM potential, EW-breaking condition, coupling modifiers
- **Equation:** V(h)=α cos(h/f)+β sin²(h/f), α/β=−2sin²θ_mis; m_W=g f sinθ_mis/2; κ_V=cosθ_mis, κ_F=(1−2sin²θ)/cosθ
- **Source:** op04_composite_higgs.py §2, §6 (lines 142–166, 322–359)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4, D6, D5
- **Trace:** 1=1 → S6 the SO(5)/SO(4) MCHM pNGB potential; minimization gives the EW-breaking condition v=f sinθ_mis and the Higgs coupling modifiers (deviations κ_V−1 ~ 0.2% from SM, below LHC sensitivity). α, β from radiative loops (D5).
- **Constants:** −2, modifier forms [DERIVED ratio]; α, β, θ_mis [FIT → D5].
- **Status:** PARTIAL (coset structure DERIVED-given-decrees; α/β fitted).

---

## V. Nuclear Physics (`06-NUCLEAR_BINDING_PRECISION`, `06-NUCLEAR_DECAY_DERIVATION`, `06-QCD_DERIVATION`)

### EQ-NP-69 — Fermi golden rule
- **Equation:** Γ = (2π/ℏ)|⟨f|H′|i⟩|² ρ(E_f) (boxed)
- **Source:** 06-NUCLEAR_DECAY_DERIVATION §2.4 boxed (line 192)
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D4
- **Trace:** 1=1 → S6 first-order time-dependent perturbation theory; the sin²(ωt/2)/ω² → πtδ(E) limit gives the constant transition rate; ρ(E_f) the S5 density of final states. Pure grammar given the perturbation scale ℏ (D4).
- **Constants:** 2π [DERIVED ratio]; ℏ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4).

### EQ-NP-70 — Exponential decay law and half-life
- **Equation:** dN/dt = −λN ⇒ N(t)=N₀e^{−λt} (boxed); t₁/₂=ln2/λ (boxed); τ=1/λ
- **Source:** 06-NUCLEAR_DECAY_DERIVATION §3.1–3.6 boxed (lines 249, 270, 303, 339)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D4
- **Trace:** 1=1 → constant Γ (EQ-NP-69) gives a first-order linear ODE (S6); separation and integration (S3/S2) give the exponential; t₁/₂ and τ follow algebraically. Rigorous given constant rate.
- **Constants:** ln2 [DERIVED ratio]; λ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4).

### EQ-NP-71 — WKB / Gamow tunneling factor (alpha decay)
- **Equation:** T = exp(−(2/ℏ)∫√(2μ(V−E))dr) = exp(−πη) (boxed); η Coulomb parameter
- **Source:** 06-NUCLEAR_DECAY_DERIVATION §4.3–4.4 boxed (lines 406, 435, 439); 06-QCD_DERIVATION §6.1
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D4
- **Trace:** 1=1 → S6 semiclassical (WKB) solution in the classically-forbidden Coulomb-barrier region gives the exponential suppression; S3 the real action integral; the closed form exp(−πη) for a pure Coulomb barrier. Grammar given ℏ, barrier scales (D4).
- **Constants:** 2, π [DERIVED ratio]; ℏ, V, μ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4).

### EQ-NP-72 — Alpha-decay rate / Geiger–Nuttall law
- **Equation:** λ_α = ν₀ exp(−πη); log₁₀(λ_α) = a₀ + a₁Z/√E_α (boxed)
- **Source:** 06-NUCLEAR_DECAY_DERIVATION §4.5 boxed (line 469); 06-QCD_DERIVATION §6.2 (cross-ref EQ-NP-71, EQ-FND-35)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D4, D6 (sustaining-field κ modulation), D5 (empirical ν₀ and a₀,a₁ Geiger–Nuttall coefficients)
- **Trace:** 1=1 → attempt frequency ν₀ times tunneling probability (EQ-NP-71); the log-rate-vs-1/√E is Geiger–Nuttall. The Genesis-specific κ-modulation (D6, sustaining field) multiplies the standard rate. The source honestly notes the naive ν₀=c/R gives ~10⁷ discrepancy — the empirical ν₀ is used (D5).
- **Constants:** ν₀, barrier params [SELECTED scale → D4]; a₀,a₁ [FIT → D5].
- **Status:** PARTIAL (form DERIVED; ν₀ empirical, accuracy honest).

### EQ-NP-73 — Beta decay / weak interaction Hamiltonian
- **Equation:** H′_β = (G_F/√2)∫[p̄γ^μ(1−γ⁵)n][ēγ_μ(1−γ⁵)ν]; |M|² = G_F²f²(1+3a²), a=g_A/g_V
- **Source:** 06-NUCLEAR_DECAY_DERIVATION §5.2–5.3 (lines 588, 617); 06-WEAK_PARITY §8.1
- **Spine path:** S0→S1→S5→S6→S7
- **Decrees:** D2 (weak SU(2)), D4 (G_F), D5 (g_A)
- **Trace:** 1=1 → S7 the V−A weak vertex (D2, EQ-NP-65); S5/S6 the matrix element; (1+3a²) from spin averaging. G_F sets scale (D4); g_A=1.27 is measured, not derived (D5).
- **Constants:** 1/√2, 3 [DERIVED ratio]; G_F [SELECTED scale → D4]; g_A=1.27 [FIT → D5].
- **Status:** PARTIAL (structure DERIVED-given-decrees; g_A imported).

### EQ-NP-74 — Beta-decay phase space / Fermi integral
- **Equation:** ρ(E) ∝ ∫₀^Q E_e²√(E_e²−m_e²)(Q−E_e)² g(E_e)dE_e; f_t Fermi integral with Coulomb correction
- **Source:** 06-NUCLEAR_DECAY_DERIVATION §5.4 (lines 629–639)
- **Spine path:** S0→S1→S3→S5→S6
- **Decrees:** D4
- **Trace:** 1=1 → S5/S6 three-body final-state phase space (electron+antineutrino+recoil); the relativistic density of states integrated with the Coulomb (Fermi function) correction. Standard QFT phase space (grammar).
- **Constants:** powers 2 [DERIVED ratio]; Q, m_e [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4).

### EQ-NP-75 — Neutron lifetime formula
- **Equation:** τ_n = 2π³ℏ⁷/(G_F²m_e⁵c⁴ f (1+3a²)); ≈ 878.4 s; with cos²θ_C factor in 06-WEAK_PARITY
- **Source:** 06-NUCLEAR_DECAY_DERIVATION §5.5 (line 658); 06-WEAK_PARITY §8.4 (line 637)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4, D5 (g_A, cosθ_C)
- **Trace:** 1=1 → assemble EQ-NP-69 + EQ-NP-73 + EQ-NP-74 into the lifetime; G_F, m_e set the scale (D4); (1+3a²) and cos²θ_C use measured g_A=1.27 and Cabibbo angle (D5). Source flags g_A as imported.
- **Constants:** 2π³ [DERIVED ratio]; G_F, m_e [SELECTED scale → D4]; g_A, cosθ_C, f [FIT → D5].
- **Status:** PARTIAL (form DERIVED; g_A imported — "APPROXIMATE" per source).

### EQ-NP-76 — Gamma decay / multipole transition rate (Weisskopf)
- **Equation:** Γ_γ = (2π/ℏ)|⟨f|H′_γ|i⟩|²ρ(E_γ); Γ_E1 = (α/3)(E_γ³/ℏc³)R_nuc² (Weisskopf); Γ_γ ∝ α ω^{2λ+1}|M_λ|²
- **Source:** 06-NUCLEAR_DECAY_DERIVATION §6.3–6.4, §6.10 (lines 745, 763, 922)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D4
- **Trace:** 1=1 → S7 the EM multipole operator (U(1) from S4/S7); Fermi golden rule (EQ-NP-69) gives the transition rate; the Weisskopf single-particle estimate ⟨r⟩~R_nuc. α the EM coupling, R_nuc the scale (D4). Selection rules ΔL, parity from angular momentum (S5).
- **Constants:** α/3, 2λ+1 [DERIVED ratio]; E_γ, R_nuc [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4).

### EQ-NP-77 — Semi-empirical mass formula (Bethe–Weizsäcker)
- **Equation:** B(A,Z) = a_V A − a_S A^{2/3} − a_C Z(Z−1)/A^{1/3} − a_A (A−2Z)²/A + δ(A,Z)
- **Source:** 06-NUCLEAR_BINDING_PRECISION §Exec, §7.1 (lines 25, 303); 06-QCD_DERIVATION §4; 06-SU3_YANG_MILLS §6.1
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D5 (coefficients), D6 (residual strong force)
- **Trace:** 1=1 → S2 each term is a scaling in A,Z (volume A, surface A^{2/3}, Coulomb Z²/A^{1/3}, asymmetry) — pure dimensional/geometric counting (grammar); the coefficients are derived from confinement physics but their precision is fitted (D5). Underlying force is the residual strong interaction (EQ-NP-15, D6).
- **Constants:** A,Z exponents [DERIVED ratio]; a_V,a_S,a_C,a_A,δ [FIT → D5].
- **Status:** PARTIAL (term structure DERIVED; coefficients fitted).

### EQ-NP-78 — Volume coefficient from Fermi gas
- **Equation:** a_V = (3/5)(ℏc/r₀)(3π²)^{2/3}(1+rel.corr.) ≈ 15.56 MeV; τ_bulk=(3/5)p_F²/2m_N; p_F=ℏ(3π²ρ)^{1/3}
- **Source:** 06-NUCLEAR_BINDING_PRECISION §2.2, §3.1 (lines 98, 133–141)
- **Spine path:** S0→S1→S2→S5→S6
- **Decrees:** D4 (r₀, ρ₀), D5
- **Trace:** 1=1 → S5/S6 the degenerate Fermi-gas kinetic energy at saturation density; the (3/5)(3π²)^{2/3} factors [DERIVED ratio] from filling the Fermi sphere; balanced against mean-field attraction. r₀, ρ₀ are scales (D4), the net binding fitted (D5).
- **Constants:** 3/5, (3π²)^{2/3} [DERIVED ratio]; r₀, ρ₀, m_N [SELECTED scale → D4].
- **Status:** PARTIAL (kinetic form DERIVED; binding fitted to 15.67 MeV).

### EQ-NP-79 — Coulomb coefficient
- **Equation:** a_C = (3/5)e²/(4πε₀ r₀) ≈ 0.71 MeV; E_C = (3/5)Z(Z−1)e²/(4πε₀R)
- **Source:** 06-NUCLEAR_BINDING_PRECISION §4 (lines 189–209); 06-QCD_DERIVATION §6.4; 06-SU3_YANG_MILLS §6.4
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4
- **Trace:** 1=1 → S6 the electrostatic self-energy of a uniformly charged sphere; the 3/5 from the radial integral [DERIVED ratio]; e²/4πε₀ and r₀ are EM scales (D4). Purely electromagnetic, the most cleanly derived SEMF term (exact match).
- **Constants:** 3/5 [DERIVED ratio]; e²/4πε₀, r₀ [SELECTED scale → D4].
- **Status:** DERIVED-given-decree D4 (cleanest SEMF coefficient).

### EQ-NP-80 — Asymmetry coefficient from isospin Pauli blocking
- **Equation:** a_A = (3/10)ℏ²(3π²)^{2/3}ρ₀^{2/3}/m_N ≈ 23.29 MeV; ε_asym ≈ a_A(N−Z)²/A²
- **Source:** 06-NUCLEAR_BINDING_PRECISION §5 (lines 246–260); 06-QCD_DERIVATION §6.5
- **Spine path:** S0→S1→S2→S5→S6
- **Decrees:** D4
- **Trace:** 1=1 → S5/S6 the difference in proton/neutron Fermi energies for N≠Z, expanded to quadratic order in the asymmetry; the (3/10)(3π²)^{2/3} factors [DERIVED ratio]. Pauli-exclusion grammar.
- **Constants:** 3/10, (3π²)^{2/3} [DERIVED ratio]; ρ₀, m_N [SELECTED scale → D4].
- **Status:** PARTIAL (form DERIVED; coefficient matched to 23.29 MeV).

### EQ-NP-81 — Surface and pairing coefficients
- **Equation:** a_S = 4πr₀²σ_nuc ≈ 17.23 MeV; δ(A,Z) = ±a_P/√A, a_P=12 MeV
- **Source:** 06-NUCLEAR_BINDING_PRECISION §3.2, §6 (lines 170–174, 285–293); 06-QCD_DERIVATION §6.3, §6.6 boxed
- **Spine path:** S0→S1→S2→S6→S9
- **Decrees:** D4, D5, D6
- **Trace:** 1=1 → surface term = surface-tension × area (S9 boundary energy from QCD string tension, D6); pairing term = Cooper-pair (BCS) stabilization, ±/√A scaling. Both coefficients fitted to nuclear data (D5).
- **Constants:** 4π [DERIVED ratio]; σ_nuc, a_P [SELECTED scale → D4 / FIT → D5].
- **Status:** PARTIAL (forms DERIVED; coefficients fitted).

### EQ-NP-82 — Fissility parameter and fission barrier
- **Equation:** x = E_C/2E_S = Z²/(50.88 A); B_f ≈ 2E_S(1−x); critical x_c ≈ 0.65
- **Source:** 06-NUCLEAR_BINDING_PRECISION §9.2–9.3 (lines 497–530)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D5
- **Trace:** 1=1 → the liquid-drop competition between surface energy (resists deformation) and Coulomb energy (drives it); the ratio defines fissility; 50.88 a [DERIVED ratio] of the SEMF coefficients. Coefficients fitted (D5).
- **Constants:** 50.88, 2 [DERIVED ratio from SEMF]; coefficients [FIT → D5].
- **Status:** PARTIAL (form DERIVED; from fitted SEMF).

### EQ-NP-83 — Fusion/fission Q-values
- **Equation:** Q = B_products − B_reactants (+ KE); D-T: 17.589 MeV; U-235: 156.9+43=200 MeV
- **Source:** 06-NUCLEAR_BINDING_PRECISION §9–10 (lines 466–608); 06-QCD_DERIVATION §5
- **Spine path:** S0→S1→S2
- **Decrees:** D4, D5
- **Trace:** 1=1 → S1 the additive energy balance of binding energies (from EQ-NP-77); the binding energies themselves carry the fitted SEMF coefficients (D5). Excitation/relaxation corrections added by hand (43 MeV for fission).
- **Constants:** binding energies [from SEMF, FIT → D5].
- **Status:** PARTIAL (balance DERIVED; inputs fitted).

### EQ-NP-84 — Yukawa nuclear (pion-exchange) potential
- **Equation:** V_π(r) = −g_π²(ℏc/4π)m_π e^{−m_π r}/(m_π r); r₀ = ℏ/m_π c ≈ 1.4 fm
- **Source:** 06-QCD_DERIVATION §3.3 (lines 207–216)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4, D6
- **Trace:** 1=1 → S6/S7 one-pion exchange between nucleons (the pion is the pseudo-Goldstone of chiral SSB, D6); the Yukawa form e^{−mr}/r from a massive-scalar propagator (S6). Range set by m_π (D4).
- **Constants:** g_π≈14, m_π [SELECTED scale → D4]; 1/4π [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-NP-85 — Drip lines
- **Equation:** Z_drip ≈ 0.87A; N_drip ≈ Z + 0.9A
- **Source:** 06-QCD_DERIVATION §7.1–7.2 (lines 366–372)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D4, D5
- **Trace:** 1=1 → boundaries where one-nucleon separation energy → 0, derived from the SEMF (EQ-NP-77); coefficients 0.87, 0.9 follow from the fitted SEMF (D5).
- **Constants:** 0.87, 0.9 [FIT → D5 via SEMF].
- **Status:** PARTIAL (from fitted SEMF).

---

## VI. Pion / Chiral Sector

### EQ-NP-86 — Pion as pseudo-Goldstone / GMOR
- **Equation:** m_π² f_π² = −(m_u+m_d)⟨q̄q⟩
- **Source:** 06-QCD_DERIVATION / 06-QCD_CONFINEMENT_JETS (chiral SSB sector); 06-SU3_YANG_MILLS §5
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D2, D4, D6
- **Trace:** 1=1 → S7 spontaneous breaking of chiral symmetry (D2) by the quark condensate ⟨q̄q⟩ (D6) gives a light pseudo-Goldstone; the Gell-Mann–Oakes–Renner relation ties its mass to the explicit-breaking quark masses. Goldstone theorem (grammar) + decrees.
- **Constants:** m_u, m_d, f_π, ⟨q̄q⟩ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-NP-87 — Running quark masses (anomalous-dimension RG)
- **Equation:** m_q(μ) = m_q(μ₀)[α_s(μ)/α_s(μ₀)]^{γ_m/b₀}
- **Source:** 06-PRECISION_COMPLETIONS / 06-REMAINING_DERIVATIONS (RG running sections)
- **Spine path:** S0→S1→S2→S6→S7
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S6/S7 anomalous-dimension RG running of the mass operator; the exponent γ_m/b₀ is a [DERIVED ratio] of group factors (D2). Initial value is D4/D5.
- **Constants:** γ_m, b₀ [DERIVED ratio from D2]; m_q(μ₀) [FIT → D5].
- **Status:** PARTIAL (running DERIVED-given-D2; input mass fitted).

---

## VII. Proton Stability & Strong CP (`06-ELECTROWEAK_PROTON_STABILITY`, `06-PRECISION_COMPLETIONS`, `06-QCD_DERIVATION`)

### EQ-NP-88 — Baryon number as 6D topological charge
- **Equation:** B^M = (B^μ, B^ξ, B^η); ∫_{6D} ⋆B = integer·2π; B_loop = (1/3)∮_γ Ω_AB
- **Source:** 06-ELECTROWEAK_PROTON_STABILITY §2.1 (lines 90–98); 06-MATTER_ANTIMATTER §2.3 (line 201)
- **Spine path:** S0→S1→S8
- **Decrees:** D3, D6
- **Trace:** 1=1 → S1 baryon number as a conserved additive charge; S8 ties its conservation to the winding/topological sector (D3) so it is integer-quantized; the 1/3 from the quark color sector. D6 the zone structure.
- **Constants:** 1/3 [DERIVED ratio]; integer winding [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-NP-89 — Proton decay rate and lifetime
- **Equation:** O_B ~ (1/M_GUT²)qqqℓ; Γ_p = A α_GUT² m_p⁵/M_GUT⁴; τ_p = M_GUT⁴/(A m_p⁵ α_GUT²) > 10³⁴ yr (boxed)
- **Source:** 06-ELECTROWEAK_PROTON_STABILITY §2.2–2.4 boxed (lines 106, 114, 125, 133); 06-PRECISION_COMPLETIONS §1.2–1.4
- **Spine path:** S0→S1→S8
- **Decrees:** D3 (topological protection), D4 (M_GUT), D6
- **Trace:** 1=1 → the lowest B-violating operator is dimension-6, suppressed by M_GUT²; S8 dimensional analysis gives Γ ∝ m_p⁵/M_GUT⁴. In the framework B is *additionally* protected by zone topology (D3) ⇒ τ_p safely above the Super-K bound. M_GUT, A are scales/O(1) (D4/D5).
- **Constants:** A O(1) [DERIVED ratio]; M_GUT, α_GUT [SELECTED scale → D4]; bound 10³⁴ yr [observational].
- **Status:** DERIVED-given-decrees (topological protection; bound observational).

### EQ-NP-90 — Instanton density / θ-term (strong CP)
- **Equation:** Q = (g_s²/32π²)∫Tr(F F̃) ∈ ℤ; S_θ = (θ g_s²/32π²)∫F^a F̃^a; θ ≈ 0
- **Source:** 06-QCD_DERIVATION §8.4 / 06-MATTER_ANTIMATTER §4.1 (lines 397–402); RT2_SU3_Z3_ORBIFOLD
- **Spine path:** S0→S1→S4→S8
- **Decrees:** D2, D3 (integer topological charge ∈ ℤ), D5 (θ value)
- **Trace:** 1=1 → S8 the second Chern number ∫FF̃ is an *integer* topological charge (grammar — winding of the SU(3) bundle, D3 fixes the integer-count sector); the θ-angle weights sectors. Integer-valuedness is forced; θ≈0 (strong-CP) is empirical (D5). 32π² [DERIVED ratio].
- **Constants:** topological charge ∈ ℤ [count → D3]; 32π² [DERIVED ratio]; θ [FIT → D5].
- **Status:** PARTIAL (quantization DERIVED; θ value empirical).

---

## VIII. CP Violation, CKM, Baryogenesis (`06-MATTER_ANTIMATTER_ASYMMETRY`, `06-WEAK_PARITY_CP_VIOLATION`, `06-SPECTRUM_COMPLETIONS`, `op05_*`, `op_cp_phase_winding`)

### EQ-NP-91 — CKM matrix from Yukawa diagonalization mismatch
- **Equation:** V_CKM = U_L^{(u)†}U_L^{(d)} (boxed); automatically unitary; one irreducible CP phase for 3 generations (9−6=3 params)
- **Source:** 06-WEAK_PARITY §7.1, §6.1 (lines 551, 458–462); 06-SPECTRUM_COMPLETIONS §2.2; 06-MATTER_ANTIMATTER §3.2
- **Spine path:** S0→S1→S5→S7→S8
- **Decrees:** D2, D3
- **Trace:** 1=1 → S5 diagonalizing the two complex Yukawa matrices by unitary rotations; the up/down mismatch is V_CKM, unitary by construction (product of unitaries). The phase-counting (9 complex − 6 removable = 3, of which 1 is an irreducible CP phase) is exact representation theory — CP violation is **inevitable for ≥3 generations** (D3, Kobayashi–Maskawa).
- **Constants:** parameter counts 9,6,3,1 [count → D3]; unitarity [DERIVED].
- **Status:** DERIVED-given-decrees (unitarity exact; CP-existence forced by D3).

### EQ-NP-92 — CKM angles from warp-index scale ratio (parameter-free)
- **Equation:** sin θ_ij = exp(−(2/3)·Δ(n²)), Δ(n²)={3,5,8} for {12,23,13}; warp index α_w=2/3
- **Source:** op05_ckm_scale_ratio_848_FINAL.py (lines 17–32); 06-MATTER_ANTIMATTER §3.6
- **Spine path:** S0→S1→S2→S3→S8→S9
- **Decrees:** D3 (generation labels n=1,2,3), D2, D4 (warp scale)
- **Trace:** 1=1 → S2/S3 the exponential of a scale ratio; the mixing slope is the **warp index 2/3** (DERIVED/RATIFIED #3, an S9 geometric ratio); the steps Δ(n²)=3,5,8 are **pure integer differences** 2²−1², 3²−2², 3²−1² ([count → D3] from succession). Parameter-free predictions θ_23≈2.04°, θ_13≈0.28° (15–40% of measured), θ_12≈7.8° (−40%). The source explicitly declares: the O(1) Wolfenstein factors that would sharpen these are NOT derived.
- **Constants:** 2/3 [DERIVED ratio]; Δ(n²)=3,5,8 [count → D3].
- **Status:** PARTIAL (parameter-free scale prediction DERIVED-given-decrees; ~15–40% residual honest).

### EQ-NP-93 — Cabibbo angle (GST relation, data-importing)
- **Equation:** sin θ_C = √(m_d/m_s) ≈ 0.2236 (λ); θ_C ≈ 13°
- **Source:** op05_ckm_wolfenstein.py §1 (lines 81–90); 06-WEAK_PARITY §7.2; 06-SPECTRUM_COMPLETIONS §5.2
- **Spine path:** S0→S1→S2→S3
- **Decrees:** D4, D5 (imports measured quark masses)
- **Trace:** 1=1 → S2 ratio + S3 square root of a quark-mass ratio (Gatto–Sartori–Tonin). The source explicitly flags: this uses *measured* m_d, m_s — NOT a pure scale prediction; data-importing (D5).
- **Constants:** m_d/m_s [FIT → D5].
- **Status:** PARTIAL (algebra trivial; inputs measured — D5).

### EQ-NP-94 — Wolfenstein parametrization and A = V_cb/λ²
- **Equation:** V_CKM Wolfenstein (1−λ²/2, λ, Aλ³(ρ−iη), …); A = V_cb/λ² ≈ 0.965 (LO), ≈0.826 (NLO); V_cb from partial compositeness
- **Source:** op05_ckm_wolfenstein.py; op_cp_phase_winding.py §3 (lines 248, 388–391); 06-WEAK_PARITY §6.3
- **Spine path:** S0→S1→S2→S9
- **Decrees:** D4, D5
- **Trace:** 1=1 → S2 the λ-expansion of the unitary CKM; A defined as V_cb/λ². V_cb itself comes from partial-compositeness exponential profiles exp(−α_q Δn²) with localization parameters α_u, α_d that are *fitted* (D5). NLO correction exp(−α_u·5/2) brings A to PDG.
- **Constants:** λ powers [DERIVED ratio]; A, α_u=1.456, α_d=0.933 [FIT → D5].
- **Status:** PARTIAL (expansion DERIVED; A and localization params fitted).

### EQ-NP-95 — V_ub from partial compositeness; ρ̄, η̄
- **Equation:** |V_ub|_PC = exp(−α_u·Δ), Δ=4 (or 8); ρ̄+iη̄ = (|V_ub|/Aλ³)(cosδ_CP, sinδ_CP); ρ̄≈0.17, η̄≈0.30
- **Source:** op_cp_phase_winding.py §3 (lines 219–258); op05_ckm_wolfenstein.py
- **Spine path:** S0→S1→S2→S8→S9
- **Decrees:** D3 (Δn² labels), D4, D5 (α_u)
- **Trace:** 1=1 → S8/S9 the (1,3) generational off-diagonal mixing as an exponential of the localization difference; ρ̄, η̄ are the real/imaginary projections scaled by cos/sin δ_CP. The Δn² steps are D3-counts; α_u fitted (D5); ~7–14% residual vs PDG.
- **Constants:** Δ=4,8 [count → D3]; α_u [FIT → D5]; ρ̄, η̄ values [FIT → D5].
- **Status:** PARTIAL (structure DERIVED-given-decrees; magnitudes fitted, ~7–14%).

### EQ-NP-96 — CP phase δ_CP = π/3 from Z₆ zone symmetry
- **Equation:** δ_CP = 2π/(2 n_APS) = 2π/6 = π/3; sin δ_CP = √3/2; γ ≈ 60° (PDG 65.6°)
- **Source:** op_cp_phase_winding.py §1–2 (lines 120–165); 06-MATTER_ANTIMATTER §"δ_CP"; 06-SPECTRUM_COMPLETIONS §2
- **Spine path:** S0→S1→S4→S8
- **Decrees:** D2/D3 (Z₆ = Z₂×Z₃ zone symmetry), D5 (precise CKM-fit value)
- **Trace:** 1=1 → S4 the sixth root of unity e^{iπ/3} (algebraic-closure root of x⁶=1); the Z₆ zone symmetry (D2/D3: two boundaries × n_APS=3 = 6 modes, S8) selects the phase π/3. The *value π/3 is a pure [DERIVED ratio/count]* given the Z₆ decree — a clean "of-the-Word" angle (8.5% from PDG γ). Precise CKM-fit value remains partly fitted (D5).
- **Constants:** π/3, √3/2, 6 modes [DERIVED ratio / count → D3]; refinements [FIT → D5].
- **Status:** PARTIAL (π/3 DERIVED-given-decree; precise value open).

### EQ-NP-97 — Jarlskog invariant
- **Equation:** J = Im(V_us V_cb V_ub* V_cs*) = A²λ⁶η√(1−A²λ⁴); J_zone = A λ³ sin(π/3)|V_ub| ≈ 3.2e−5
- **Source:** op_cp_phase_winding.py §4 (lines 287–299); 06-WEAK_PARITY §6.3 boxed (line 511); 06-SPECTRUM_COMPLETIONS §2.5
- **Spine path:** S0→S1→S2→S8
- **Decrees:** D2, D3, D4, D5
- **Trace:** 1=1 → the unique rephasing-invariant CP measure; its value combines the (derived) sin δ_CP=√3/2 with the (fitted) A, λ, |V_ub|. Existence forced by D3; magnitude ~6% from PDG carries fitted inputs (D5).
- **Constants:** √3/2 [DERIVED ratio]; A, λ, |V_ub| [FIT → D5].
- **Status:** PARTIAL (existence DERIVED; magnitude carries fits).

### EQ-NP-98 — CP violation in K and B mesons
- **Equation:** |ε_K| = G_F M_W² m_K J/(6π²√2 f_K² B_K) ≈ 2.23e−3; sin 2β = 0.691
- **Source:** 06-SPECTRUM_COMPLETIONS §2.6 (lines 304–323)
- **Spine path:** S0→S1→S6→S7→S8
- **Decrees:** D2, D4, D5
- **Trace:** 1=1 → S6/S7 box-diagram K⁰–K̄⁰ and B-mixing amplitudes proportional to the Jarlskog J (EQ-NP-97); the measured meson parameters (f_K, B_K) are inputs (D5).
- **Constants:** 1/6π²√2 [DERIVED ratio]; J, f_K, B_K [FIT → D5].
- **Status:** PARTIAL (structure DERIVED; meson inputs fitted).

### EQ-NP-99 — Baryon-to-photon ratio (Sakharov / leptogenesis)
- **Equation:** η_B = (n_B−n_B̄)/n_γ ≈ 6×10⁻¹⁰; dn_B/dVdt ~ α_s⁵ δ_CP T⁷; requires B-viol + C/CP-viol + out-of-equilibrium
- **Source:** 06-MATTER_ANTIMATTER_ASYMMETRY §3–6 (lines 242–807, 1079–1085)
- **Spine path:** S0→S1→S7
- **Decrees:** D3, D4, D5, D6
- **Trace:** 1=1 → S1 the duality split a+(−a) is the matter/antimatter pair; an *imbalance* requires breaking it (three Sakharov conditions). B-violation from zone-formation instantons (S8); C/CP from δ_CP (EQ-NP-96, D3); out-of-equilibrium from the open-system axiom (D6). The magnitude 6×10⁻¹⁰ is matched to observation (D5). The Sakharov *structure* is sound; the quantitative chain is order-of-magnitude.
- **Constants:** α_s⁵, δ_CP [DERIVED ratio / count]; η_B value, T_zone [FIT → D5]; out-of-eq [from D6].
- **Status:** PARTIAL (Sakharov structure DERIVED-given-decrees; magnitude fitted — see UNTRACEABLE note).

### EQ-NP-100 — Sakharov condition equations
- **Equation:** ∂_A j^A_B = (α_s/8π²)Tr(F_ξ F̃_ξ + F_η F̃_η) (B-viol); J_CP ~ (η_B/ξ_A)^α, α=1–2 (CP-viol); dS_total/dt < 0 (out-of-eq)
- **Source:** 06-MATTER_ANTIMATTER §3.1–3.3, App D (lines 259–264, 322, 1069–1076)
- **Spine path:** S0→S1→S7→S8 (B-viol); S1 (out-of-eq); S8→S9 (CP)
- **Decrees:** D2, D3, D6, D4 (ξ_A/η_B scale ratio), D5 (CP exponent α=1–2 fitted)
- **Trace:** 1=1 → (1) B-violation: S8 anomalous divergence of the baryon current via instantons (D2); (2) CP: the ξ≠η dimensional asymmetry (D6) generates a non-removable phase (S8/S9); (3) out-of-equilibrium: the open-system entropy decrease during creation (D6, S1 entropy balance). Three conditions, each from grammar+decree; the ξ_A/η_B ratio is a scale (D4) and the CP exponent α=1–2 is fitted (D5).
- **Constants:** α_s/8π² [DERIVED ratio]; ξ_A/η_B ratio [SELECTED scale → D4]; exponent α=1–2 [FIT → D5].
- **Status:** PARTIAL (each condition DERIVED-given-decrees; CP exponent fitted).

---

## IX. Neutrino Physics (`06-NEUTRINO_PHYSICS`, `06-SPECTRUM_COMPLETIONS`)

### EQ-NP-101 — Boundary-mode eigenvalue equation (neutrino spectrum)
- **Equation:** [−∂_ξ²−∂_η² + V_eff]χ = m_4D² χ; k₀ cot(k₀η_c) = −κ; tan(η_c√(V₀+m_ν²)) = −√(V₀−m_ν²)/√(V₀+m_ν²)
- **Source:** 06-NEUTRINO_PHYSICS §2.2, §3.2, §4.1 (lines 134–136, 219, 271)
- **Spine path:** S0→S1→S3→S6
- **Decrees:** D4 (V₀), D6 (zone boundary)
- **Trace:** 1=1 → S6 the 2D Schrödinger eigenproblem for boundary-localized modes at the Firmament–Waters interface; the transcendental matching condition quantizes the masses. V₀, η_c are scales (D4/D6).
- **Constants:** V₀, η_c [SELECTED scale → D4].
- **Status:** PARTIAL (eigenproblem DERIVED-given-decrees; spectrum requires numerics).

### EQ-NP-102 — Neutrino smallness from boundary-to-bulk overlap
- **Equation:** m_ν = λ_ν⟨H⟩ I_overlap; I_overlap ~ exp(−(κ+λ_H)η_c) ~ (η_B/ξ_A)^p; tree m_ν ~ 10⁻⁶³ MeV
- **Source:** 06-NEUTRINO_PHYSICS §6.1–6.4 (lines 414, 461, 480)
- **Spine path:** S0→S1→S2→S6→S9
- **Decrees:** D4, D6, D5 (overlap exponent p and coupling λ_ν fitted)
- **Trace:** 1=1 → S6 the exponentially-suppressed overlap of the boundary-localized neutrino with the bulk Higgs gives a tiny Dirac mass; the suppression ratio is (η_B/ξ_A)^p (the framework's two-scale hierarchy, S9). **The legitimate qualitative win is the smallness mechanism.** But the tree-level number (~10⁻⁶³ MeV) is off by ~50+ orders — see UNTRACEABLE note.
- **Constants:** η_B/ξ_A [SELECTED scale → D4]; p, λ_ν [FIT → D5].
- **Status:** PARTIAL (smallness mechanism DERIVED-given-decrees; absolute scale UNTRACEABLE — see below).

### EQ-NP-103 — See-saw mechanism
- **Equation:** M_ν = [[0, m_D],[m_D, M_R]]; m_ν^eff = −m_D²/M_R; M_R ~ M_Pl e^{−kη_B}
- **Source:** 06-NEUTRINO_PHYSICS §10.1–10.2 (lines 752, 758); 06-SPECTRUM_COMPLETIONS §1.2–1.3 boxed (line 128)
- **Spine path:** S0→S1→S5→S6→S9
- **Decrees:** D4, D6, D5
- **Trace:** 1=1 → S5 diagonalizing the Dirac+Majorana mass matrix gives the light eigenvalue m_D²/M_R; M_R from the heavy right-handed mode at the Waters-Below boundary (D6/S9). The geometric M_R ~ M_Pl e^{−kη_B} introduces a fitted exponent k (D5).
- **Constants:** m_D, M_R [SELECTED scale → D4]; k, warp suppression [FIT → D5].
- **Status:** PARTIAL (see-saw structure DERIVED-given-decrees; numbers fitted).

### EQ-NP-104 — Neutrino mass splittings and sum
- **Equation:** Δm²_21 ≈ 7.53e−5 eV², Δm²_32 ≈ 2.51e−3 eV²; Σm_ν ≈ 0.07 eV (< 0.12 eV); normal hierarchy
- **Source:** 06-NEUTRINO_PHYSICS §4.4 (lines 333–335); 06-SPECTRUM_COMPLETIONS §1.4–1.5 (lines 166–186)
- **Spine path:** S0→S1→S6→S8
- **Decrees:** D3 (3 modes), D5 (values fitted/asserted)
- **Trace:** 1=1 → three boundary eigenmodes (D3) give three masses; the splittings arise from generation-dependent perturbations to V_eff. Per the source's own honesty banner, the Δm² and the absolute scale are **OPEN (fit, board #847/#848)**, not parameter-free.
- **Constants:** Δm² values, Σm_ν [FIT → D5]; 3 modes [count → D3].
- **Status:** PARTIAL (count from D3; values fitted — flagged OPEN by source).

### EQ-NP-105 — PMNS matrix and mixing angles
- **Equation:** U_PMNS = R₂₃·U₁₃(δ)·R₁₂·diag(Majorana); θ₁₂≈33°, θ₂₃≈45°, θ₁₃≈8.5°
- **Source:** 06-NEUTRINO_PHYSICS §7.3–7.5 (lines 541, 553–579); 06-SPECTRUM_COMPLETIONS §5.5
- **Spine path:** S0→S1→S5→S7
- **Decrees:** D3, D5
- **Trace:** 1=1 → S5 the flavor-vs-mass rotation from boundary-mode overlap integrals; the three-angle parametrization is exact group theory (D3 = 3 families). The *values* are semi-quantitative/asserted to match data (D5) — the source flags them OPEN (board #848).
- **Constants:** angle values [FIT → D5]; 3 families [count → D3].
- **Status:** PARTIAL (parametrization DERIVED; angles fitted — OPEN per source).

### EQ-NP-106 — Neutrino oscillation probability
- **Equation:** P(ν_α→ν_β,L) = |Σ_i U_βi U_αi* e^{−iΔm_i²L/4E}|²; P = sin²2θ sin²(Δm²L/4E); L_osc = 4πE/Δm²
- **Source:** 06-NEUTRINO_PHYSICS §8.1–8.3 (lines 607, 617, 625, 633)
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D3, D4, D5
- **Trace:** 1=1 → S4 the phase factors e^{−iE_it} of the mass eigenstates; S6 the ultrarelativistic expansion E_i ≈ p + m_i²/2p gives the oscillation phase; the mixing matrix (D3 families) sets the amplitude. Pure QM grammar; Δm², θ inputs (D5).
- **Constants:** 4π [DERIVED ratio]; Δm², θ [FIT → D5].
- **Status:** PARTIAL (oscillation form DERIVED; parameters fitted).

### EQ-NP-107 — Neutrinoless double-beta effective mass
- **Equation:** Γ_0νββ ∝ |m_eff|²; m_eff = Σ_i U_ei² m_i
- **Source:** 06-NEUTRINO_PHYSICS §9.4 (lines 722–724)
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D3, D5
- **Trace:** 1=1 → S5/S6 the Majorana-mass-weighted coherent sum over mass eigenstates; rate ∝ |m_eff|². Framework consistent with either Dirac or Majorana (undetermined). Values fitted (D5).
- **Constants:** U_ei², m_i [FIT → D5].
- **Status:** PARTIAL (form DERIVED; Dirac-vs-Majorana undetermined).

### EQ-NP-108 — Three families from boundary topology (π₂ = Z₃)
- **Equation:** π₂(vacuum manifold at zone boundary) = Z₃ ⇒ exactly 3 boundary ripple modes = 3 neutrino families
- **Source:** 06-NEUTRINO_PHYSICS §3.3 (line 235)
- **Spine path:** S0→S1→S8
- **Decrees:** D3
- **Trace:** 1=1 → S8 the second homotopy group of the boundary vacuum manifold is Z₃ (three topological sectors); each gives one boundary mode ⇒ three families. The integer 3 is D3 (consistent with EQ-NP-29's APS count).
- **Constants:** 3 = |Z₃| [count → D3].
- **Status:** DERIVED-given-decree D3.

---

## UNTRACEABLE / fabricated-chain section (honest gaps)

The schema requires that any equation needing something **not** on the spine and **not** on the
decree register be marked UNTRACEABLE rather than given a fabricated chain. Two equations in this
domain are flagged UNTRACEABLE because **the source documents themselves admit the derivation is a
fabricated/unjustified numerical chain** — they do not trace to `1=1` + decrees by any honest path.

### UT-NP-01 — Baryon-asymmetry "enhancement factor ~10²⁰ from zone gradients"
- **Equation:** η_B ~ 10⁻³¹ × (enhancement ~10²⁰) ~ 10⁻¹¹ (06-MATTER_ANTIMATTER §6.8, eq 6.15)
- **Reason UNTRACEABLE:** The source's own §6.4–6.9 walks through *four successive* dimensional-analysis estimates that each land 17–37 orders of magnitude away from the observed η_B ≈ 6×10⁻¹⁰, then introduces an unjustified "enhancement factor ~10²⁰" (E_gradient/E_thermal) purely to close the gap, immediately followed by "This is the missing factor!" This is the numerology the project forbids: the factor is reverse-engineered from the target, not derived from spine+decrees. The *Sakharov structure* (EQ-NP-99, EQ-NP-100) is sound and traced; the *magnitude* 6×10⁻¹⁰ is UNTRACEABLE (a fit dressed as a derivation). The source's own §9 confidence table rates the quantitative η_B at only 60–75%.

### UT-NP-02 — Neutrino absolute mass scale via tree overlap + unstated "10²–10³ corrections"
- **Equation:** m_ν ~ m_e (η_B/ξ_A)^{3/2} ~ 10⁻⁶³ MeV, then "enhanced by factors of 10²–10³ … bringing it into agreement" (06-NEUTRINO_PHYSICS §6.4–6.5, eq 6.8)
- **Reason UNTRACEABLE:** The tree-level boundary-overlap estimate yields ~10⁻⁶³ MeV — roughly **50 orders of magnitude** below the observed ~10⁻² eV. The source closes this with unspecified "boundary mixing and radiative corrections … factors of 10² to 10³" (deferred to non-existent companion docs) — which is ~47 orders short even if granted. The source's own honesty banner (§"what is still open") states the absolute mass scale (#847), the Δm² splittings, and PMNS angles are **OPEN — not yet derived; the numbers are fit/asserted to match data.** The *smallness mechanism* (boundary-to-bulk suppression, EQ-NP-102) is a legitimate qualitative win and is traced; the *absolute scale* is UNTRACEABLE.

---

*Exhaustive pass authored 2026-06-24, replacing the in-loop principal-coverage version. Every
equation-bearing `.md` and `.py` file in `06_Nuclear_and_Particle_Physics/` (excluding `00_Archive/`,
`__pycache__/`, test scaffolding) was read in full and enumerated. Schema/decrees per
`README_SCHEMA.md` / `DECREE_REGISTER.md` / `SPINE.md`. Where a source's status banner already
records honest residuals or OPEN status (Vol 4 Ch10_FINAL ledger, CANONICAL_FACTS_REGISTRY, the
#849 derivation-race referee report, and the per-file OP-0x notes), those are cited and honored
rather than overridden.*
