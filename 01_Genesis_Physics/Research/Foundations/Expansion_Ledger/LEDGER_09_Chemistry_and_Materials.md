# Expansion Ledger — Domain 09: Chemistry and Materials

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This ledger traces every displayed/numbered equation and named key result in
> `Research/Mathematical_Models/09_Chemistry_and_Materials/` back to the seed `1=1`
> via the spine rungs S0–S9 (`SPINE.md`) and the decree register D0–D6 (`DECREE_REGISTER.md`).
> No equation is "derived from `1=1` alone"; every physics equation = spine path + named decrees.
> Constants are tagged: [DERIVED ratio] / [SELECTED scale → D4] / [FIT → D5] / [count → D3].

## Header

| Field | Value |
|-------|-------|
| Domain | 09 — Chemistry and Materials |
| Files traced | `09-ATOMIC_STRUCTURE_DERIVATION.md`, `09-CHEMISTRY_DERIVATION.md`, `09-COMPLETIONS.md`, `09-ELEMENT_PREDICTION.md`, `test_atomic_structure.py` |
| # equations traced | 97 |
| Decrees used across domain | D0, D1, D2, D3, D4, D5, D6 |
| # PARTIAL | 8 |
| # UNTRACEABLE | 3 |

**Domain-level note.** Nearly all of chemistry in these files is *applied membrane QM*: the
Schrödinger equation (parent: `QM_FROM_MEMBRANE_DYNAMICS.md`) plus the Coulomb potential
(parent: `FINE_STRUCTURE_DERIVATION.md` / KK reduction) plus Pauli/fermion statistics (D3-tied
topology) plus the variational principle. The deep spine work is done in domains 03/05/06; this
domain mostly *consumes* those results and applies algebra. Where a result simply re-states a
parent-domain equation, the trace cites the parent and the rung it stands on rather than
re-deriving it. Every dimensionful chemical constant carries the unit scale **D4**; the membrane/
Firmament physical content (Ψ_A/Ψ_B, σ, η_B, ξ_A) is **D6**; the gauge/charge content is **D2**;
the spacetime manifold/dimension is **D1**.

---

## FILE: 09-ATOMIC_STRUCTURE_DERIVATION.md

### EQ-CHEM-01 — 6D total action (atomic-structure entry point)
- **Equation:** S_total = S_grav + S_Firm + S_gauge + S_matter + S_interaction
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, eq after "the total action is")
- **Spine path:** S0→S1→S2→S3→S5→S6→S7→S9
- **Decrees:** D0, D1, D6 (and D2 via the gauge sector)
- **Trace:** 1=1 → S1/S2 build the additive+multiplicative algebra of an action sum → S3/D0 give the real-valued continuum to integrate over → S6 supplies the integral/variational operators → S9 supplies the (warped) 6D manifold whose existence is **D1**, with the zone/Firmament field content **D6**; the individual sectors are themselves parent-document results. This is a structural template, not a closed-form law.
- **Constants:** none dimensionful here (each sector's couplings are tagged in their own domains).
- **Status:** DERIVED-as-form (given D0, D1, D6; gauge sector given D2).

### EQ-CHEM-02 — 6D Einstein–Hilbert gravitational sector
- **Equation:** S_grav = (1/2κ₆²) ∫_{M⁶} d⁶x √(−g₆) R₆
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, "Gravitational sector")
- **Spine path:** S0→S3→S6→S9
- **Decrees:** D0, D1 (a curved manifold + its dimension), D4 (κ₆ sets the scale)
- **Trace:** 1=1 → S3/D0 real continuum → S9 supplies curvature R on a Riemannian/Lorentzian manifold (its existence and dimension = **D1**) → S6 integrates it. Curvature-action form is generic; the 6D dimension is the decree.
- **Constants:** κ₆² = 8πG₆ [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D0, D1, D4).

### EQ-CHEM-03 — Brane (Firmament) action
- **Equation:** S_Firm = −σ ∫_Σ d⁴x √(−g₄) + (extrinsic curvature terms)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, "Brane action")
- **Spine path:** S0→S3→S6→S9
- **Decrees:** D1, D6 (the Firmament Σ is a physical-content axiom), D4 (tension σ)
- **Trace:** 1=1 → S9 gives a submanifold Σ embedded in the 6D manifold; that Σ *is* the Firmament — a **D6** architectural object → S6 integrates the tension over it. Form generic; existence of Σ is decreed.
- **Constants:** σ (Firmament tension) [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D4, D6).

### EQ-CHEM-04 — Gauge sector (KK)
- **Equation:** S_gauge = ∫_Σ d⁴x √(−g₄) [ −¼ F_{μν}F^{μν} + KK terms ]
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, "Gauge fields")
- **Spine path:** S0→S4→S6→S7→S9
- **Decrees:** D1, D2 (which gauge group; U(1) here), D4
- **Trace:** 1=1 → S4 gives the phase of ℂ → S7 promotes it to a gauge symmetry; the Yang–Mills form −¼F² is the canonical S7 invariant → which group/charge content is **D2** (U(1) from KK reduction) → S6 integrates over Σ (S9/D1).
- **Constants:** gauge coupling implicit [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D4).

### EQ-CHEM-05 — Matter (Dirac) sector
- **Equation:** S_matter = ∫_Σ d⁴x √(−g₄) [ ψ̄(iγ^μ D_μ − m)ψ ]
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, "Matter fields")
- **Spine path:** S0→S4→S5→S6→S7
- **Decrees:** D1, D2 (D_μ carries the gauge charge), D4 (mass m), D6 (fermion as membrane defect)
- **Trace:** 1=1 → S4/S5 build ℂ-spinor structure (Clifford algebra of the manifold) → S7 supplies the gauge-covariant derivative D_μ (charge = **D2**) → S6 integrates. The Dirac form is parent-domain (05/06); here it is the entry term for electrons on Σ.
- **Constants:** m_e [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D4, D6).

### EQ-CHEM-06 — Interaction (current–potential) sector
- **Equation:** S_interaction = ∫_Σ d⁴x √(−g₄) J^μ A_μ
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, "Interaction")
- **Spine path:** S0→S6→S7
- **Decrees:** D1, D2 (J^μ is the charged fermionic current)
- **Trace:** 1=1 → S7 minimal coupling J·A is the gauge-invariant first-order interaction (charge = **D2**) → S6 integrates over Σ.
- **Constants:** none new (charge folded into J^μ via D2).
- **Status:** DERIVED-as-form (given D1, D2).

### EQ-CHEM-07 — 6D warped metric ansatz
- **Equation:** ds² = e^{2Φ(x)} [ g^{(4)}_{μν} dx^μ dx^ν − dξ² − dη² ]
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 1)
- **Spine path:** S0→S3→S9
- **Decrees:** D0, D1, D6 (ξ,η are the Waters Above/Below dimensions), D4 (warp via Φ)
- **Trace:** 1=1 → S9 gives a metric with a warp factor; choosing exactly two extra dims (ξ,η) with the Waters interpretation is the **D1**+**D6** content. Profile/warp is **D9-profile** under D1.
- **Constants:** warp e^{2Φ} [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D0, D1, D4, D6).

### EQ-CHEM-08 — KK-reduced 4D effective action
- **Equation:** S_4D,eff = ∫_Σ d⁴x √(−g₄) [ R₄/(2κ₄²) − ¼ F_{μν}F^{μν} + ψ̄(iγ^μ D_μ − m_e)ψ ]
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 1, displayed result)
- **Spine path:** S0→S4→S5→S6→S7→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** 1=1 → integrate EQ-CHEM-01..07 over (ξ,η) (parent: KK reduction). The product of gravity+EM+Dirac on 4D Σ is forced once D1 fixes the reduction; this is the standard KK output cited here, not re-derived.
- **Constants:** κ₄²=8πG₄, m_e, gauge coupling [each SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (D0,D1,D2,D4,D6).

### EQ-CHEM-09 — Dirac equation (electron in EM field)
- **Equation:** [iγ^μ(∂_μ − ieA_μ) − m_e c²] ψ = 0
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 2)
- **Spine path:** S0→S4→S5→S6→S7
- **Decrees:** D1, D2 (charge e), D4 (m_e)
- **Trace:** 1=1 → S4/S5 spinor+ℂ → S7 minimal coupling to A_μ (charge = **D2**) → S6 differential operators → Euler–Lagrange of EQ-CHEM-05 gives the Dirac equation. Parent-domain result, applied to atomic electrons.
- **Constants:** e [SELECTED scale → D4 via D2], m_e [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D4).

### EQ-CHEM-10 — Pauli equation (non-relativistic reduction)
- **Equation:** iℏ ∂ψ/∂t = [ (p − eA)²/(2m_e) + V(r) + (eℏ/2m_e c) σ·B ] ψ
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 2)
- **Spine path:** S0→S4→S5→S6→S7
- **Decrees:** D1, D2 (charge, spin coupling), D4 (ℏ, m_e), D6
- **Trace:** 1=1 → take the v≪c limit of EQ-CHEM-09 (algebraic reduction). Spinor σ structure is S5; the magnetic-moment term is forced by the spinor content. ℏ enters from membrane quantization (**D6**, parent QM doc).
- **Constants:** ℏ [SELECTED scale → D4], e, m_e [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D4, D6).

### EQ-CHEM-11 — Schrödinger equation (time-independent, atomic)
- **Equation:** −(ℏ²/2m_e) ∇²ψ + V(r)ψ = Eψ
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 2 boxed; repeated §1.1)
- **Spine path:** S0→S4→S5→S6
- **Decrees:** D1, D4 (ℏ, m_e), D6 (membrane wave medium gives ℏ)
- **Trace:** 1=1 → S6 supplies ∇² and the eigenvalue form; set B=A=0 in EQ-CHEM-10. This is the central chemistry equation; its membrane derivation lives in `QM_FROM_MEMBRANE_DYNAMICS.md` (cited, not re-derived).
- **Constants:** ℏ, m_e [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D4, D6).

### EQ-CHEM-12 — Nuclear source current (point charge on Σ)
- **Equation:** J^μ = Ze δ³(r)(c,0,0,0)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 3)
- **Spine path:** S0→S3→S7
- **Decrees:** D1, D2 (charge Ze), D3 (Z is an integer count of protons)
- **Trace:** 1=1 → S3 delta distribution → charge content **D2**; the nuclear charge integer Z is a **count** (D3-type, here the proton number).
- **Constants:** Z [count → D3]; e [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D3).

### EQ-CHEM-13 — 6D Poisson equation / Green's function
- **Equation:** ∇²_{6D} Φ = −ρ ; ∇²_{6D} G₆ = −δ⁶(...)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 3)
- **Spine path:** S0→S3→S6→S9
- **Decrees:** D0, D1, D2 (EM field), D6
- **Trace:** 1=1 → S6 Laplacian on the 6D manifold (S9/D1) → Green's-function inversion is standard analysis (D0). EM field content is **D2**.
- **Constants:** none dimensionful new.
- **Status:** DERIVED-as-form (given D0, D1, D2).

### EQ-CHEM-14 — 2D extra-dimensional Green's function
- **Equation:** G₂(ξ,η; ξ₀,η₀) = (1/4π) ln(L²/L₀²)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 3)
- **Spine path:** S0→S3→S6→S9
- **Decrees:** D0, D1, D6 (ξ,η geometry; L₀ cutoff at extra-dim scale)
- **Trace:** 1=1 → 2D Laplace Green's function is logarithmic (standard analysis, D0/S6) on the (ξ,η) plane (**D1**/**D6**).
- **Constants:** L≈√(ξ_A·η_B), L₀ (Planck-scale cutoff) [both SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D0, D1, D4, D6).

### EQ-CHEM-15 — Coulomb potential from extra-dim integration
- **Equation:** V_eff(r) = Ze ∫dξdη G₆ = −Ze²/(4πε₀) · 1/r + QED corr.
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 3; boxed §"Result")
- **Spine path:** S0→S3→S6→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** 1=1 → integrate EQ-CHEM-13/14 over (ξ,η); the 1/r 4D form drops out of the dimensional reduction (parent: KK doc). This is a **DERIVED-as-form** Coulomb law, not imported.
- **Constants:** e²/(4πε₀) [SELECTED scale → D4]; Z [count → D3].
- **Status:** DERIVED-given-decrees (D0,D1,D2,D3,D4,D6).

### EQ-CHEM-16 — Fine structure constant from zone-scale ratio
- **Equation:** α = (1.4383/1) ln(ξ_A/η_B) ≈ 1/137.036 ; e²/(4πε₀)=ℏcα
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 3; §8.4; §10)
- **Spine path:** S0→S2→S3→S4→S9
- **Decrees:** D0, D1, D4 (the scales ξ_A, η_B are D4 anchors), D5 (the prefactor 1.4383 is fitted), D6
- **Trace:** 1=1 → S2 gives the ratio ξ_A/η_B (a *Logos* proportion) → S3 log → α is a dimensionless ratio of zone scales. The numeric coefficient 1.4383 is matched to reproduce 137.036, so it is **[FIT → D5]**, not a pure DERIVED ratio. (Parent: `FINE_STRUCTURE_DERIVATION.md`, flagged incomplete.)
- **Constants:** 1.4383 [FIT → D5]; ξ_A, η_B [SELECTED scale → D4]; α⁻¹=137.036 [FIT → D5] (it is the data-matched target, not a clean geometric ratio — tagged per audit-B honesty).
- **Status:** PARTIAL (DERIVED-as-form given D4; numeric prefactor is D5/open).

### EQ-CHEM-17 — Coulomb potential (final atomic form)
- **Equation:** V(r) = −Ze²/(4πε₀ r) = −Z ℏc α / r
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 3 boxed; §1.1)
- **Spine path:** S0→S2→S3→S6
- **Decrees:** D1, D2, D3 (Z), D4
- **Trace:** 1=1 → substitute EQ-CHEM-16 into EQ-CHEM-15. Pure algebra over the derived Coulomb law.
- **Constants:** α [see EQ-CHEM-16 tags]; e²/(4πε₀)=ℏcα [SELECTED scale → D4]; Z [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-18 — Fermion exchange phase (spin-statistics)
- **Equation:** ψ(r₁,r₂) → e^{iπ}ψ(r₂,r₁) = −ψ(r₂,r₁)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 4; §8.2)
- **Spine path:** S0→S4→S8
- **Decrees:** D3 (winding/topology of the defect → fermion class), D6 (defect on Firmament)
- **Trace:** 1=1 → S4 gives phase e^{iθ} → S8 gives the winding/topology that classifies a defect exchange; the half-winding (π) that makes the electron a fermion is the **D3**-type topological count, realized on the Firmament (**D6**).
- **Constants:** π [DERIVED ratio, from S4].
- **Status:** DERIVED-as-form (given D3, D6).

### EQ-CHEM-19 — Electron spin projection
- **Equation:** S_z = ±ℏ/2
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (Part 0, Step 4)
- **Spine path:** S0→S4→S5→S8
- **Decrees:** D3 (Jackiw–Rossi zero-mode count), D4 (ℏ), D6
- **Trace:** 1=1 → S5 spinor rep + S8 index/zero-mode theorem fix the spin-½ doublet; the ±½ count is topological (**D3**). ℏ sets the scale (**D4**).
- **Constants:** ℏ [SELECTED scale → D4]; ½ [count → D3].
- **Status:** DERIVED-as-form (given D3, D4, D6).

### EQ-CHEM-20 — Radial Schrödinger equation
- **Equation:** −(ℏ²/2m_e) u'' + [V(r) + ℏ²l(l+1)/(2m_e r²)] u = E u, u=rR
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.2)
- **Spine path:** S0→S4→S5→S6
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → separate EQ-CHEM-11 in spherical coords (S6 calculus); the centrifugal term comes from the angular Laplacian. Algebra over EQ-CHEM-11.
- **Constants:** ℏ, m_e [SELECTED scale → D4]; l [count → D3, see EQ-CHEM-21].
- **Status:** DERIVED-as-form (given D1, D4, D6).

### EQ-CHEM-21 — Angular momentum quantization
- **Equation:** L² = ℏ² l(l+1), l = 0,1,2,…
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.2; §3.1)
- **Spine path:** S0→S4→S5→S7→S8
- **Decrees:** D4 (ℏ), integer l [count → D3-type]
- **Trace:** 1=1 → S7 rotation group SO(3)/SU(2) → S8 integer winding gives integer l; eigenvalue l(l+1) is the Casimir. The integer-ness is topological (S8); ℏ is scale. Per DECREE_REGISTER rule 4, using the integer winding/index l invokes **D3**.
- **Constants:** ℏ [SELECTED scale → D4]; l [count → D3].
- **Status:** DERIVED-as-form (given D3, D4).

### EQ-CHEM-22 — Hydrogen energy eigenvalues
- **Equation:** E_n = −m_e e⁴ / [2(4πε₀)² ℏ² n²]
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.3)
- **Spine path:** S0→S4→S5→S6
- **Decrees:** D1, D4, D6
- **Trace:** 1=1 → solve EQ-CHEM-20 with the Coulomb V (EQ-CHEM-17); the discrete spectrum follows from the u(0)=u(∞)=0 boundary conditions (S6 + analysis). Standard closed-form result.
- **Constants:** m_e, e, ε₀, ℏ [all SELECTED scale → D4]; n [count → D3-type radial node count].
- **Status:** DERIVED-given-decrees (D1,D4,D6).

### EQ-CHEM-23 — Bohr radius
- **Equation:** a₀ = 4πε₀ℏ²/(m_e e²) = ℏ/(m_e c α)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.3; §1.4 boxed = 0.529177 Å)
- **Spine path:** S0→S2→S4→S6
- **Decrees:** D4, (D5 via α)
- **Trace:** 1=1 → algebraic regrouping of EQ-CHEM-22 constants; a₀ is the length where kinetic ℏ-term balances the Coulomb term.
- **Constants:** ε₀, ℏ, m_e, e [SELECTED scale → D4]; α [see EQ-CHEM-16].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-24 — Rydberg energy
- **Equation:** E_Ryd = ½ m_e c² α² = 13.6057 eV
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.3; Appendix A)
- **Spine path:** S0→S2→S4
- **Decrees:** D4, (D5 via α)
- **Trace:** 1=1 → rewrite EQ-CHEM-22 ground-state magnitude using α (EQ-CHEM-16). Pure algebra.
- **Constants:** m_e, c [SELECTED scale → D4]; α² [DERIVED ratio anchored by D5].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-25 — Hydrogen levels in Rydberg form
- **Equation:** E_n = −E_Ryd/n² = −13.6057 eV / n²
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.3 boxed; §10.1)
- **Spine path:** S0→S4→S6
- **Decrees:** D4
- **Trace:** 1=1 → EQ-CHEM-22 = EQ-CHEM-24 / n². Algebra; n from radial node count.
- **Constants:** E_Ryd [SELECTED scale → D4]; n [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-26 — Ground-state hydrogen wavefunction
- **Equation:** ψ_{100}(r) = (1/√π) a₀^{−3/2} exp(−r/a₀); |ψ|² = (1/π a₀³)e^{−2r/a₀}
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.4)
- **Spine path:** S0→S3→S4→S6
- **Decrees:** D0, D4
- **Trace:** 1=1 → normalized n=1,l=0 solution of EQ-CHEM-20; normalization uses real integrals (D0).
- **Constants:** a₀ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-27 — Most-probable radius
- **Equation:** r_prob = a₀ = 4πε₀ℏ²/(m_e e²) = 0.529177 Å
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.4 boxed)
- **Spine path:** S0→S4→S6
- **Decrees:** D4
- **Trace:** 1=1 → maximize r²|ψ|² (S6 derivative=0). Pure calculus over EQ-CHEM-26.
- **Constants:** a₀ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-28 — Rydberg constant
- **Equation:** R_∞ = m_e e⁴/(8 ε₀² h³ c) = m_e c α²/(2hc) = E_Ryd/(hc) = 1.097373×10⁷ m⁻¹
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.5 boxed)
- **Spine path:** S0→S2→S4
- **Decrees:** D4, (D5 via α)
- **Trace:** 1=1 → divide EQ-CHEM-24 by hc. Algebra.
- **Constants:** m_e, e, ε₀, h, c [SELECTED scale → D4]; α² [DERIVED ratio anchored by D5].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-29 — Spectral transition frequency
- **Equation:** ν = R_∞ c Z² (1/n_i² − 1/n_f²)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.5); test file Test 1
- **Spine path:** S0→S4→S6
- **Decrees:** D3 (Z, n_i, n_f integers), D4
- **Trace:** 1=1 → energy differences of EQ-CHEM-25 scaled by Z²; ΔE=hν. Algebra over integer levels.
- **Constants:** R_∞, c [SELECTED scale → D4]; Z, n_i, n_f [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-30 — Spin–orbit energy
- **Equation:** E_SO = (α² m_e c²/2)(Z⁴/n³)/[l(l+½)(l+1)]
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.6)
- **Spine path:** S0→S4→S5→S6→S7
- **Decrees:** D4, D5 (via α), D3 (Z,n,l)
- **Trace:** 1=1 → relativistic correction to EQ-CHEM-09 (Dirac); spin (S5) couples to orbital (S7) motion. Parent-domain perturbation result, applied.
- **Constants:** α² [DERIVED ratio anchored by D5]; m_e,c [SELECTED scale → D4]; Z,n,l [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-31 — Darwin term
- **Equation:** E_Darwin = (α² m_e c²/2)(Z⁴/n³)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.6)
- **Spine path:** S0→S4→S5→S6
- **Decrees:** D4, D5 (via α), D3
- **Trace:** 1=1 → contact-term relativistic correction from the non-relativistic reduction of EQ-CHEM-09. Applied parent result.
- **Constants:** α² [DERIVED ratio anchored by D5]; m_e,c [SELECTED scale → D4]; Z,n [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-32 — Fine-structure energy levels
- **Equation:** E_{n,j} = −E_Ryd Z²/n² [1 + (α²Z²/n²)(n/(j+½) − ¾)]
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§1.6)
- **Spine path:** S0→S4→S5→S6→S7
- **Decrees:** D4, D5 (via α), D3 (Z,n,j)
- **Trace:** 1=1 → Dirac-equation expansion (EQ-CHEM-09) to O(α²); combine EQ-CHEM-25/30/31. Standard relativistic spectrum.
- **Constants:** α² [DERIVED ratio anchored by D5]; E_Ryd, m_e [SELECTED scale → D4]; Z,n,j [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-33 — N-electron Hamiltonian
- **Equation:** H = Σ_i[−(ℏ²/2m_e)∇_i² − Ze²/(4πε₀ r_i)] + Σ_{i<j} e²/(4πε₀ r_{ij})
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§2.1)
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D1, D2, D3 (Z, electron count N), D4
- **Trace:** 1=1 → S1 additive sum of single-electron EQ-CHEM-11 terms plus pairwise Coulomb (EQ-CHEM-17). The counts (N electrons, Z) are D3-type.
- **Constants:** ℏ,m_e,e,ε₀ [SELECTED scale → D4]; Z,N [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-34 — Fermionic antisymmetry (Pauli)
- **Equation:** Ψ(…,r_i,σ_i,…,r_j,σ_j,…) = −Ψ(…,r_j,σ_j,…,r_i,σ_i,…)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§2.2); also CHEM eq 1.4, COMPLETIONS §1.1
- **Spine path:** S0→S4→S8
- **Decrees:** D3 (fermion topology/half-winding), D6 (defect on Firmament)
- **Trace:** 1=1 → EQ-CHEM-18 generalized to N particles; antisymmetry under exchange follows from the fermion class fixed at S8/**D3**.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D3, D6).

### EQ-CHEM-35 — Slater determinant
- **Equation:** Ψ = (1/√N!) det[ φ_a(r_i,σ_i) ]
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§2.3 boxed)
- **Spine path:** S0→S1→S5→S8
- **Decrees:** D3 (N count, fermion class), D6
- **Trace:** 1=1 → the determinant is the unique totally-antisymmetric (EQ-CHEM-34) combination of N orbitals; antisymmetry is the S8/D3 fermion property, determinant algebra is S5.
- **Constants:** N! normalization [count → D3].
- **Status:** DERIVED-as-form (given D3, D6).

### EQ-CHEM-36 — Helium singlet spin state
- **Equation:** Ψ_He = φ_{1s}(r₁)φ_{1s}(r₂)·(1/√2)[↑₁↓₂ − ↓₁↑₂]; S_total = 0
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§2.4)
- **Spine path:** S0→S5→S8
- **Decrees:** D3 (fermion class), D6
- **Trace:** 1=1 → impose EQ-CHEM-34 on two 1s electrons; symmetric space ⇒ antisymmetric spin singlet. Algebra over spinors (S5).
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D3, D6).

### EQ-CHEM-37 — Helium variational energy functional
- **Equation:** E(Z_eff) = 13.6[2Z_eff² − (27/8)Z_eff] eV
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§2.5–2.6); test file Test 2
- **Spine path:** S0→S4→S6
- **Decrees:** D4, D5 (the 5/8 Coulomb-integral coefficient is an analytic O(1) factor; ⟨T⟩,⟨V⟩ pieces are exact)
- **Trace:** 1=1 → ⟨H⟩ over the trial product wavefunction: kinetic 2Z_eff²·13.6, nuclear −4Z_eff·13.6, ee-repulsion (5/8)Z_eff·13.6 (the 5/8 is the analytic 1s–1s Coulomb integral). Variational principle = S6 stationarity (δS=0 borderline).
- **Constants:** 13.6 eV = E_Ryd [SELECTED scale → D4]; 5/8, 27/8 [DERIVED ratio, analytic].
- **Status:** DERIVED-given-decrees (variational form; δS=0 borderline).

### EQ-CHEM-38 — Optimal effective charge (helium)
- **Equation:** dE/dZ_eff = 0 ⇒ Z_eff* = 27/32 = 0.84375 (text) / Z−5/16=27/16 (test file)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§2.6); test file Test 2
- **Spine path:** S0→S6
- **Decrees:** none beyond D4 (in the underlying energy)
- **Trace:** 1=1 → minimize EQ-CHEM-37 (S6 derivative). **Note discrepancy:** the .md sets 4Z_eff−27/8=0 ⇒ 0.84375, but the standard/test-file result is Z_eff=Z−5/16=1.6875; the .md's algebra dropped the nuclear-attraction Z_eff-linear term. Flagged as an internal arithmetic inconsistency, not re-derived here.
- **Constants:** 27/32 or 27/16 [DERIVED ratio].
- **Status:** PARTIAL (DERIVED-as-form; internal numeric inconsistency between .md and test file).

### EQ-CHEM-39 — Helium ground-state energy (variational)
- **Equation:** E_He^var = 13.6[2(0.84375)² − (27/8)(0.84375)] = −19.365 eV (.md); ≈ −77.5 eV (test file, Z_eff=1.6875)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§2.6); test file Test 2
- **Spine path:** S0→S4→S6
- **Decrees:** D4, D5
- **Trace:** 1=1 → substitute EQ-CHEM-38 into EQ-CHEM-37. The −19.365 eV in the .md is wrong (propagates the EQ-CHEM-38 error); test-file −77.5 eV vs experimental −78.975 eV is the intended ~1.9% result.
- **Constants:** 13.6 eV [SELECTED scale → D4].
- **Status:** PARTIAL (numeric inconsistency; correct value is the test-file −77.5 eV).

### EQ-CHEM-40 — Helium ionization energies
- **Equation:** I₁ = E_{He+} − E_He = 24.575 eV; I₂ = −E_{He+} = 54.4 eV; E_{He+} = −Z²·13.6 = −54.4 eV
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§2.7); test file Test 2
- **Spine path:** S0→S4→S6
- **Decrees:** D3 (Z), D4
- **Trace:** 1=1 → He⁺ is hydrogen-like (EQ-CHEM-25 with Z=2, exact); differences give the ionization energies. Algebra.
- **Constants:** 13.6 eV [SELECTED scale → D4]; Z [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-41 — Quantum-defect orbital energy
- **Equation:** ε_{n,l} = −Z_eff²·13.6 eV / (n − δ_l)²
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§3.2, §6.1); CHEM eq 1.2 form
- **Spine path:** S0→S4→S6
- **Decrees:** D4, D5 (δ_l is fitted to spectra)
- **Trace:** 1=1 → EQ-CHEM-25 with screened charge and an l-dependent defect; δ_l is empirically matched (penetration), hence **D5**.
- **Constants:** 13.6 eV, Z_eff [SELECTED scale → D4]; δ_l [FIT → D5]; n [count → D3].
- **Status:** DERIVED-given-decrees (δ_l is a fit).

### EQ-CHEM-42 — Aufbau n+l rule / orbital capacity / shell capacity
- **Equation:** fill if (n₁+l₁)<(n₂+l₂); max e⁻ per subshell = 2(2l+1); per shell = 2n²
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§3.2–3.3); CHEM eq 1.1; COMPLETIONS eq 1.2; test Test 4
- **Spine path:** S0→S1→S5→S8
- **Decrees:** D3 (counts n,l,m,spin), D6
- **Trace:** 1=1 → count distinct (n,l,m_l,m_s) states (S5 dimension count + S8 integer m), then S1-sum 2Σ(2l+1)=2n². Pauli (EQ-CHEM-34) caps each at 2. Pure counting.
- **Constants:** 2, (2l+1), 2n² [count → D3].
- **Status:** DERIVED-as-form (given D3, D6).

### EQ-CHEM-43 — Slater screening / effective nuclear charge
- **Equation:** Z_eff = Z − S; ε_{n,l} ≈ −Z_eff²·13.6/(n−δ_l)²; I_E = (Z_eff/n)²·13.6 eV
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§3.2, §4.2); CHEM eq 1.2; test Tests 3,5
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D3 (Z, electron counts), D4, D5 (screening constants 0.30/0.35/0.85/1.00 are fitted)
- **Trace:** 1=1 → reduce nuclear Z by an additive screening sum (S1) of empirical per-electron constants; apply EQ-CHEM-25. Screening constants are **[FIT → D5]**.
- **Constants:** 13.6 eV [SELECTED scale → D4]; Z [count → D3]; S-constants 0.30/0.35/0.85/1.00 [FIT → D5].
- **Status:** DERIVED-given-decrees (screening is a fit; ~20–300% residuals noted).

### EQ-CHEM-44 — Hund's rules (qualitative ordering)
- **Equation:** maximize S, then L, then J-rule (set as energy ordering)
- **Source:** 09-ATOMIC_STRUCTURE_DERIVATION.md (§3.5); CHEM eq 3.5 (exchange integral J)
- **Spine path:** S0→S5→S6→S8
- **Decrees:** D3 (fermion exchange), D4
- **Trace:** 1=1 → exchange integral J (Coulomb matrix element over antisymmetrized states, EQ-CHEM-34) lowers energy for parallel spins; S6 ⟨H⟩ over Slater determinant. Form derived; the rule is the sign of J.
- **Constants:** J [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D3, D4).

---

## FILE: 09-CHEMISTRY_DERIVATION.md

### EQ-CHEM-45 — Membrane wave equation → Schrödinger
- **Equation:** ∂²ψ/∂t² = c²∇₄²ψ, c²=σ/μ ⇒ −(ℏ²/2m)∇₄²ψ + Vψ = Eψ
- **Source:** 09-CHEMISTRY_DERIVATION.md (Part 0, Stage 3, boxed)
- **Spine path:** S0→S4→S6→S9
- **Decrees:** D1, D4, D6 (σ,μ are Firmament membrane content)
- **Trace:** 1=1 → S6/S9 wave operator on the Firmament; non-relativistic limit yields EQ-CHEM-11. c²=σ/μ ties the wave speed to membrane tension/density (**D6**). Parent QM doc.
- **Constants:** σ, μ, ℏ, m [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D4, D6).

### EQ-CHEM-46 — Effective nuclear charge / orbital energy (chem form)
- **Equation:** Z_eff = Z − S; E_{n,l} = −Z_eff²·13.6 eV/n² + corrections
- **Source:** 09-CHEMISTRY_DERIVATION.md (eqs 1.2; 1.5 IE form)
- **Spine path:** S0→S4→S6
- **Decrees:** D3, D4, D5 (S)
- **Trace:** Same content as EQ-CHEM-43; restated here for the periodic-table discussion.
- **Constants:** 13.6 eV [SELECTED scale → D4]; Z [count → D3]; S [FIT → D5].
- **Status:** DERIVED-given-decrees (duplicate of EQ-CHEM-43).

### EQ-CHEM-47 — LCAO bonding/antibonding orbitals
- **Equation:** ψ_b = (1/√(2(1+S)))[φ_A+φ_B]; ψ_ab = (1/√(2(1−S)))[φ_A−φ_B]; S=∫φ_A*φ_B d³r
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 2.1; eqs 2.3–2.5 in COMPLETIONS)
- **Spine path:** S0→S1→S4→S6
- **Decrees:** D0, D4
- **Trace:** 1=1 → S1 linear combination of two atomic orbitals (solutions of EQ-CHEM-11); normalization uses the overlap integral S (real integral, D0). Superposition is grammar (S1/S4).
- **Constants:** S (overlap, dimensionless) [DERIVED ratio].
- **Status:** DERIVED-as-form (given D0, D4).

### EQ-CHEM-48 — Molecular orbital energies (variational)
- **Equation:** E = ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩; E_b=(α+β)/(1+S), E_ab=(α−β)/(1−S); α=⟨φ_A|H|φ_A⟩, β=⟨φ_A|H|φ_B⟩
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 2.2; COMPLETIONS eqs 2.6–2.8)
- **Spine path:** S0→S5→S6
- **Decrees:** D4
- **Trace:** 1=1 → Rayleigh quotient (S6 variational) over EQ-CHEM-47 in the 2-orbital basis; diagonalizing the 2×2 secular problem (S5 eigenvalue) gives E_b, E_ab. Form derived; α,β,S are integrals over the membrane orbitals.
- **Constants:** α, β [SELECTED scale → D4]; S [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4; variational δS=0 borderline).

### EQ-CHEM-49 — Bond energy splitting and lowering
- **Equation:** ΔE = 4|β|/(1−S²); ΔE_lower = −2|β|S/(1+S) ≈ −2|β|S
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 2.3); COMPLETIONS (eq 2.7)
- **Spine path:** S0→S6
- **Decrees:** D4
- **Trace:** 1=1 → subtract E_b,E_ab from EQ-CHEM-48. Pure algebra.
- **Constants:** β [SELECTED scale → D4]; S [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-CHEM-50 — H₂ 1s orbital and bonding MO
- **Equation:** φ_{1s}(r)=(1/√(π a₀³))e^{−r/a₀}; ψ_+=(1/√(2(1+S)))[φ_{1s}(r_A)+φ_{1s}(r_B)]
- **Source:** 09-CHEMISTRY_DERIVATION.md (§2.3); COMPLETIONS eqs 2.1–2.3
- **Spine path:** S0→S4→S6
- **Decrees:** D4
- **Trace:** 1=1 → EQ-CHEM-26 for each H, combined per EQ-CHEM-47. Algebra.
- **Constants:** a₀ [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-51 — H₂ two-electron singlet wavefunction
- **Equation:** Ψ_{H₂}=ψ_+(r₁)ψ_+(r₂)χ_singlet(s₁,s₂), χ_singlet=(1/√2)(|↑↓⟩−|↓↑⟩)
- **Source:** 09-CHEMISTRY_DERIVATION.md (§2.3)
- **Spine path:** S0→S5→S8
- **Decrees:** D3 (fermion antisymmetry), D6
- **Trace:** 1=1 → impose EQ-CHEM-34 on two electrons in ψ_+; symmetric space ⇒ singlet spin. Same logic as EQ-CHEM-36.
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D3, D6).

### EQ-CHEM-52 — Ionic bond formation energy
- **Equation:** E = I_A − E_aff,B + U_Coulomb(R), U_Coulomb=−e²/(4πε₀R); bond if I_A−E_aff,B < |e²/(4πε₀R)|
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 2.4); COMPLETIONS §3.1, eqs 3.3–3.7
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D2, D4
- **Trace:** 1=1 → S1 energy bookkeeping sum: ionization cost + affinity gain + Coulomb attraction (EQ-CHEM-17 with Z=1). I_A,E_aff are atomic results.
- **Constants:** e²/(4πε₀) [SELECTED scale → D4]; I_A,E_aff [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-53 — Ionic potential from 6D Green's function (chem form)
- **Equation:** φ(r)=−e/(4πε₀ r); G_{6D}=1/r² + 1/[(ξ−ξ')²+(η−η')²]; φ_4D ∝ 1/r
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 2.5)
- **Spine path:** S0→S3→S6→S9
- **Decrees:** D0, D1, D2, D4, D6
- **Trace:** Same KK-reduction content as EQ-CHEM-15, restated for ionic bonding.
- **Constants:** e/(4πε₀) [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (duplicate mechanism of EQ-CHEM-15).

### EQ-CHEM-54 — Bloch states / 1D tight-binding band
- **Equation:** ψ_k(r)=u_k(r)e^{ik·r}; E(k)=E₀ − 2t cos(ka); E_metal=N(E₀−2t) < N E₀
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 2.6; eq 4.1–4.2 + 4.5); COMPLETIONS eqs 4.1, 4.3
- **Spine path:** S0→S4→S6→S7→S9
- **Decrees:** D1, D4, D6 (periodic Firmament potential)
- **Trace:** 1=1 → S7 discrete translation symmetry of a periodic potential (S9 lattice) ⇒ Bloch theorem (S4 phase e^{ik·r}); the cosine band is the nearest-neighbor tight-binding solution of EQ-CHEM-11 in a periodic V. Standard solid-state result.
- **Constants:** E₀, t (hopping) [SELECTED scale → D4]; a (lattice constant) [SELECTED scale → D4]; N [count → D3].
- **Status:** DERIVED-as-form (given D1, D4, D6).

### EQ-CHEM-55 — Hydrogen-bond partial charge / energy
- **Equation:** δ ≈ e×0.2–0.4; E_{H-bond} ≈ −δ q/(4πε₀ r²)
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 2.7); COMPLETIONS eqs 5.2–5.4
- **Spine path:** S0→S2→S6
- **Decrees:** D4, D5 (the 0.2–0.4 charge fraction is fitted to electronegativity data)
- **Trace:** 1=1 → partial charge from asymmetric electron density (EQ-CHEM-11 solutions); dipole–charge Coulomb energy (EQ-CHEM-17 form). The 0.2–0.4 fraction is empirical (**D5**).
- **Constants:** e, ε₀ [SELECTED scale → D4]; 0.2–0.4 fraction [FIT → D5].
- **Status:** PARTIAL (charge fraction is a fit).

### EQ-CHEM-56 — VSEPR repulsion energy
- **Equation:** E_rep = Σ_{i<j} ∫∫ e²/(4πε₀|r_i−r_j|) |ψ_i|²|ψ_j|² d³r_i d³r_j
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 3.1)
- **Spine path:** S0→S1→S6
- **Decrees:** D2, D4
- **Trace:** 1=1 → S1-sum of pairwise Coulomb repulsions (EQ-CHEM-17) weighted by electron-pair densities; geometry minimizes it (S6). Standard form.
- **Constants:** e²/(4πε₀) [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D2, D4; δS=0 borderline).

### EQ-CHEM-57 — Hybrid orbital construction (sp, sp², sp³)
- **Equation:** φ_hyb,i = Σ_j c_{ij} φ_j; e.g. sp³: φ₁=½(φ_s+φ_{px}+φ_{py}+φ_{pz}), etc.
- **Source:** 09-CHEMISTRY_DERIVATION.md (eqs 3.3; §3.3 sp/sp²/sp³ sets)
- **Spine path:** S0→S1→S5→S6
- **Decrees:** D4
- **Trace:** 1=1 → S1/S5 orthonormal linear combinations of the s,p atomic orbitals (EQ-CHEM-11 solutions); the coefficients are fixed by orthonormality + pointing-toward-bond geometry (S6 minimization, EQ-CHEM-58). The ½, 1/√2, 1/√3, √(2/3), 1/√6 coefficients are DERIVED ratios from orthonormality.
- **Constants:** hybrid coefficients [DERIVED ratio].
- **Status:** DERIVED-as-form (given D4).

### EQ-CHEM-58 — Variational optimization of hybridization
- **Equation:** E=⟨Ψ|H|Ψ⟩=E_kin+E_Coul+E_exch; ∂E/∂c_i = 0
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 3.4)
- **Spine path:** S0→S6
- **Decrees:** D4
- **Trace:** 1=1 → stationarity of ⟨H⟩ w.r.t. the hybrid coefficients of EQ-CHEM-57 (S6). δS=0 borderline.
- **Constants:** none new.
- **Status:** DERIVED-as-form (given D4; δS=0 borderline).

### EQ-CHEM-59 — Exchange integral (Hund)
- **Equation:** J = ∫∫ φ_i*(r₁)φ_j(r₁) [e²/(4πε₀ r₁₂)] φ_i(r₂)φ_j*(r₂) d³r₁ d³r₂
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 3.5)
- **Spine path:** S0→S6→S8
- **Decrees:** D2, D3 (antisymmetry), D4
- **Trace:** 1=1 → Coulomb matrix element over antisymmetrized (EQ-CHEM-34) two-electron states; J>0 favors parallel spins. Same content as EQ-CHEM-44.
- **Constants:** e²/(4πε₀) [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D2, D3, D4).

### EQ-CHEM-60 — Multiple-bond energies (σ+π)
- **Equation:** E(C=C)=E_σ+E_π≈6.2 eV; E(C≡C)=E_σ+2E_π≈8.8 eV
- **Source:** 09-CHEMISTRY_DERIVATION.md (§3.5)
- **Spine path:** S0→S1→S6
- **Decrees:** D4, D5 (the per-bond σ/π energies are fitted/empirical)
- **Trace:** 1=1 → S1-sum of σ and π bond energies, each from EQ-CHEM-49-type overlap splitting. The ~3.6/2.6 eV components are empirical bond strengths (**D5**).
- **Constants:** E_σ≈3.6 eV, E_π≈2.6 eV [FIT → D5].
- **Status:** PARTIAL (component energies are fits).

### EQ-CHEM-61 — Bloch's theorem (crystal Schrödinger)
- **Equation:** V(r+a)=V(r); −(ℏ²/2m)∇²ψ+Vψ=Eψ ⇒ ψ_k(r)=u_k(r)e^{ik·r}, k∈[−π/a,π/a]
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 4.1); COMPLETIONS eq 4.1; eq 8 band theory
- **Spine path:** S0→S4→S6→S7→S9
- **Decrees:** D1, D4, D6
- **Trace:** Same as EQ-CHEM-54 (Bloch); restated for crystal band structure.
- **Constants:** a [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D4, D6).

### EQ-CHEM-62 — Crystallographic restriction theorem
- **Equation:** only n = 1,2,3,4,6 rotational symmetry allowed; nθ=2πm; 7 crystal systems; 230 space groups
- **Source:** 09-CHEMISTRY_DERIVATION.md (eqs 4.3, 4.4)
- **Spine path:** S0→S1→S5→S7
- **Decrees:** D1 (3D Euclidean space)
- **Trace:** 1=1 → S7 the discrete symmetry groups compatible with a 3D lattice (S5 dimension=3, **D1**); the integer constraint nθ=2πm is a counting theorem (S1/S8). This is a pure mathematical theorem given 3D space — no physical decree beyond D1.
- **Constants:** {1,2,3,4,6}, 7, 230 [count → D3-type, pure math].
- **Status:** DERIVED-as-form (given D1).

### EQ-CHEM-63 — Madelung crystal energy and equilibrium constant
- **Equation:** E_elec=−A e²/(4πε₀ a); E_total=N[−A e²/(4πε₀ a)+Bρ^{−n}−ε_zp]; a_eq=[A e²(n−1)/(4πε₀ B n)]^{1/(n−1)}; E_coh=A e²/(4πε₀ a)(1−1/n)
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 4.5); COMPLETIONS eq 3.1, §3 NaCl calc
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D0, D2, D4, D5 (Born exponent n, repulsion B fitted)
- **Trace:** 1=1 → S1/S3 infinite lattice sum of Coulomb terms (EQ-CHEM-17) → A is the convergent geometric sum (DERIVED ratio); add Born repulsion Bρ^{−n}; minimize (S6). n≈8–9 and B are empirical (**D5**).
- **Constants:** A (Madelung, e.g. NaCl 1.7476) [DERIVED ratio]; e²/(4πε₀) [SELECTED scale → D4]; n, B [FIT → D5].
- **Status:** DERIVED-given-decrees (A derived; Born terms fitted).

### EQ-CHEM-64 — Close-packing fraction
- **Equation:** f = π/(3√2) ≈ 0.7405 (FCC and HCP)
- **Source:** 09-CHEMISTRY_DERIVATION.md (eq 4.7)
- **Spine path:** S0→S3→S5
- **Decrees:** D1 (3D geometry)
- **Trace:** 1=1 → pure 3D Euclidean sphere-packing geometry (S3/S5, **D1**); π from S4. A geometric theorem, no physical decree.
- **Constants:** π/(3√2) [DERIVED ratio].
- **Status:** DERIVED-as-form (given D1).

### EQ-CHEM-65 — Metallic bonding energy (coordination)
- **Equation:** E_metal = −2t N (1D) / −z-dependent t; close packing maximizes z=12
- **Source:** 09-CHEMISTRY_DERIVATION.md (§4.7); COMPLETIONS eq 4.3
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D1, D4
- **Trace:** 1=1 → ground-state band energy from EQ-CHEM-54; larger coordination z ⇒ larger hopping ⇒ lower energy. Algebra over the band.
- **Constants:** t [SELECTED scale → D4]; z=12, N [count → D3].
- **Status:** DERIVED-as-form (given D1, D4).

---

## FILE: 09-COMPLETIONS.md (equations not duplicated above)

### EQ-CHEM-66 — Fermi energy (free electron gas)
- **Equation:** E_F = (ℏ²/2m)(3π²n)^{2/3}; N=∫₀^{E_F} ρ(E)dE
- **Source:** 09-COMPLETIONS.md (eq 4.2; eqs 8.1–8.2)
- **Spine path:** S0→S3→S5→S6
- **Decrees:** D3 (electron count/density n), D4
- **Trace:** 1=1 → count plane-wave states (S5 momentum space) up to a filling level (S8 integer states, S3 continuum limit); the (3π²n)^{2/3} is the 3D state-counting result. ℏ scale (**D4**).
- **Constants:** ℏ, m [SELECTED scale → D4]; n [count → D3]; 3π² [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-67 — Madelung energy with α prefactor (COMPLETIONS variant)
- **Equation:** U_Madelung = −N_A M α e²/(4πε₀ R)
- **Source:** 09-COMPLETIONS.md (eq 3.1)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D2, D4, D5 (M via fit/structure), D0
- **Trace:** Same as EQ-CHEM-63 electrostatic term. **Honesty flag:** the explicit insertion of the fine-structure constant α (1/137) into the Madelung energy (eqs 3.1, 3.5: "−1.748×(1/137)×1440 eV·Å/R") is dimensionally/physically incorrect — the Coulomb energy is e²/(4πε₀)=1.44 eV·nm already; multiplying by α double-counts. Traced as written but flagged.
- **Constants:** M [DERIVED ratio]; α [erroneously inserted]; e²/(4πε₀) [SELECTED scale → D4].
- **Status:** PARTIAL (algebra as written is internally inconsistent — spurious α factor).

### EQ-CHEM-68 — Rotational energy levels
- **Equation:** E_J = B J(J+1), B = ℏ²/(2I), ΔE = 2B(J+1) for J→J+1, I = μr²
- **Source:** 09-COMPLETIONS.md (eqs 6.1–6.2)
- **Spine path:** S0→S4→S5→S6→S7
- **Decrees:** D4, D3 (J integer)
- **Trace:** 1=1 → rigid-rotor eigenvalues: S7 rotation group ⇒ Casimir J(J+1) (same structure as EQ-CHEM-21); selection rule ΔJ=±1 from dipole matrix elements (S6). ℏ scale.
- **Constants:** ℏ [SELECTED scale → D4]; I=μr² [SELECTED scale → D4]; J [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-69 — Vibrational energy levels
- **Equation:** E_v = ℏω(v+½), ω = √(k/m), ΔE = ℏω
- **Source:** 09-COMPLETIONS.md (eqs 6.3–6.4)
- **Spine path:** S0→S4→S6
- **Decrees:** D4, D3 (v integer)
- **Trace:** 1=1 → quantum harmonic oscillator: quadratic potential (Taylor expansion of the bond potential, S6) gives equally-spaced levels; the +½ zero-point is forced by the ladder algebra (S4/S5). Standard QM result.
- **Constants:** ℏ, k, m [SELECTED scale → D4]; v [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-70 — Electronic transition energy and selection rules
- **Equation:** ΔE = E_bonding − E_bonding'; ΔS=0, ΔL=0,±1
- **Source:** 09-COMPLETIONS.md (eq 6.5; §6.3)
- **Spine path:** S0→S6→S7
- **Decrees:** D4
- **Trace:** 1=1 → energy difference of MO levels (EQ-CHEM-48); selection rules from angular-momentum conservation in the dipole operator (S7).
- **Constants:** none new.
- **Status:** DERIVED-as-form (given D4).

### EQ-CHEM-71 — Franck–Condon factor
- **Equation:** F_{v,v'} = |∫ ψ_v(r) ψ_{v'}(r) dr|²
- **Source:** 09-COMPLETIONS.md (eq 6.6)
- **Spine path:** S0→S3→S6
- **Decrees:** D0, D4
- **Trace:** 1=1 → overlap integral of vibrational wavefunctions (EQ-CHEM-69) between electronic states; squared modulus = transition probability (S6, real integral D0).
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D0, D4).

### EQ-CHEM-72 — Bragg's law and structure/form factors
- **Equation:** nλ = 2d sinθ; f_j=∫ρ_j e^{2πi q·r}d³r; F_h=Σ_j f_j e^{2πi h·r_j}; I_h=|F_h|²
- **Source:** 09-COMPLETIONS.md (eqs 7.1–7.4)
- **Spine path:** S0→S4→S6→S9
- **Decrees:** D1, D3 (integers n, Miller indices h,k,l)
- **Trace:** 1=1 → S4 wave phase + S6 interference over a periodic lattice (S9/D1); constructive interference at path difference = nλ. Miller indices and order n are integer counts (D3-type).
- **Constants:** λ, d [SELECTED scale → D4]; n, (h,k,l) [count → D3].
- **Status:** DERIVED-as-form (given D1).

### EQ-CHEM-73 — Crystal energy minimization (lattice constant)
- **Equation:** E_total = E_elec + E_rep + vibrational; ∂E_total/∂a = 0 ⇒ a_eq
- **Source:** 09-COMPLETIONS.md (eqs 7.5–7.6)
- **Spine path:** S0→S1→S6
- **Decrees:** D4, D5 (repulsion parameters)
- **Trace:** Same minimization content as EQ-CHEM-63; restated generically.
- **Constants:** repulsion params [FIT → D5].
- **Status:** DERIVED-given-decrees (duplicate of EQ-CHEM-63 minimization).

### EQ-CHEM-74 — Intrinsic semiconductor conductivity
- **Equation:** σ_intrinsic ∝ exp(−E_g/2k_B T)
- **Source:** 09-COMPLETIONS.md (eq 8.3)
- **Spine path:** S0→S3→S6
- **Decrees:** D4
- **Trace:** 1=1 → Fermi–Dirac/Boltzmann thermal excitation across the band gap E_g (EQ-CHEM-61 band structure); carrier density ∝ exp(−E_g/2k_BT). Statistical-mechanics result (parent: domain 02).
- **Constants:** E_g [SELECTED scale → D4]; k_B [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D4).

### EQ-CHEM-75 — BCS pairing gap and transition temperature
- **Equation:** ΔE_pair ~ ℏω_D exp(−1/λ); T_c = 1.13 ℏω_D exp(−1/λ); λ = V(0)N(E_F); ρ(E)=0 for |E−E_F|<Δ
- **Source:** 09-COMPLETIONS.md (eqs 9.1–9.4)
- **Spine path:** S0→S4→S6→S7
- **Decrees:** D4, D6 (Firmament phonons mediate pairing), D5 (λ, V(0) fitted to materials)
- **Trace:** 1=1 → Cooper instability: an attractive electron–phonon interaction (phonons = Firmament membrane vibrations, **D6**) at the Fermi surface (EQ-CHEM-66) always binds a pair; the BCS gap equation gives the exp(−1/λ) form. The 1.13 prefactor is the BCS integral constant (DERIVED ratio); λ, V(0) are material-fitted (**D5**).
- **Constants:** ℏω_D [SELECTED scale → D4]; 1.13 [DERIVED ratio]; λ, V(0), N(E_F) [FIT → D5].
- **Status:** DERIVED-given-decrees (form derived; couplings fitted).

---

## FILE: 09-ELEMENT_PREDICTION.md

### EQ-CHEM-76 — Strong coupling running
- **Equation:** α_s(M_Z) = g_s²/(4π) = [33⁻¹ ln(M_6²/m_q²)]⁻¹ ≈ 0.118; S_gluon = −(1/4g_s²)∫d⁶x√(−g₆)F^a_{μν}F^{μνa}
- **Source:** 09-ELEMENT_PREDICTION.md (§0.2)
- **Spine path:** S0→S4→S6→S7→S9
- **Decrees:** D1, D2 (SU(3) color), D4 (M_6, scales), D5 (matching α_s=0.118)
- **Trace:** 1=1 → S7 selects SU(3) (**D2**) from the SU(N) family; Yang–Mills action (S7) + RG running (S6) gives the logarithmic α_s. Parent domain 06; the value 0.118 is matched to experiment (**D5**).
- **Constants:** α_s≈0.118 [FIT → D5]; M_6, m_q [SELECTED scale → D4]; 33=11N_c−2n_f [count → D3].
- **Status:** DERIVED-given-decrees (parent-domain result; value fitted).

### EQ-CHEM-77 — String tension / linear confinement
- **Equation:** V(r)=σ_s r + const; σ_s = ∫dη √(g_{ηη}) B_η²; σ_s≈0.18 GeV²
- **Source:** 09-ELEMENT_PREDICTION.md (§0.3)
- **Spine path:** S0→S6→S7→S9
- **Decrees:** D1, D2, D4, D6 (flux tube in η-dimension)
- **Trace:** 1=1 → SU(3) flux-tube energy in the η (Waters Below) dimension (**D6**); the linear potential is the confinement result of domain 06. σ_s sets the scale (**D4**).
- **Constants:** σ_s≈0.18 GeV² [SELECTED scale → D4].
- **Status:** DERIVED-given-decrees (parent-domain result).

### EQ-CHEM-78 — Woods–Saxon nuclear potential
- **Equation:** V(r) = −V₀/[1 + exp((r−R)/a)]; V_C(r)=(Ze²/8πε₀)(3−r²/R²) inside
- **Source:** 09-ELEMENT_PREDICTION.md (§1.1)
- **Spine path:** S0→S3→S6
- **Decrees:** D1, D2, D4, D6
- **Trace:** 1=1 → mean-field of the strong potential (EQ-CHEM-77) over A nucleons gives a saturating well; the uniform-sphere Coulomb (EQ-CHEM-15 form) adds the proton repulsion. V₀, R, a are nuclear scales (**D4**).
- **Constants:** V₀≈50 MeV, R≈1.2A^{1/3} fm, a [SELECTED scale → D4]; Z [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-79 — Shell-model single-particle Hamiltonian with spin–orbit
- **Equation:** H = p²/2M + V_eff(r) + V_SO(l·s); E_{nlj}=E_osc(N) − V_ls[j(j+1)−l(l+1)−¾]; V_SO = −α_s(σ_s/ℏc)(1/r)(dV/dr) l·s
- **Source:** 09-ELEMENT_PREDICTION.md (§1.2–1.3)
- **Spine path:** S0→S4→S5→S6→S7
- **Decrees:** D1, D2, D4, D5 (V_ls≈7 MeV·fm fitted), D6
- **Trace:** 1=1 → single-nucleon Schrödinger (EQ-CHEM-11 analog) in the Woods–Saxon well (EQ-CHEM-78) with an l·s coupling whose strength traces to σ_s (**D6**); spin (S5) couples to orbit (S7). V_ls is fit to magic numbers (**D5**).
- **Constants:** M≈939 MeV [SELECTED scale → D4]; V_ls≈7 MeV·fm [FIT → D5].
- **Status:** DERIVED-given-decrees (spin–orbit strength fitted).

### EQ-CHEM-80 — Harmonic-oscillator shell degeneracy and energy
- **Equation:** E_N = ℏω(N+3/2); g(N) = ½(N+1)(N+2); ℏω ≈ ℏ²/(2MR²) ~ 5 MeV
- **Source:** 09-ELEMENT_PREDICTION.md (§1.3–1.4)
- **Spine path:** S0→S4→S5→S6
- **Decrees:** D4, D3 (N, degeneracy counts)
- **Trace:** 1=1 → 3D isotropic harmonic oscillator (EQ-CHEM-69 in 3D); the ½(N+1)(N+2) degeneracy is pure state-counting (S5/S8). ℏω from the well scale (**D4**).
- **Constants:** ℏω≈5 MeV [SELECTED scale → D4]; degeneracies [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-81 — Nuclear magic numbers
- **Equation:** magic numbers 2, 8, 20, 28, 50, 82, 126 (from spin–orbit reordering of 2,8,20,40,70,…)
- **Source:** 09-ELEMENT_PREDICTION.md (§1.3, §6.3, §9.1)
- **Spine path:** S0→S5→S6→S8
- **Decrees:** D3 (cumulative integer counts), D4, D5 (spin–orbit strength), D6
- **Trace:** 1=1 → cumulative sums of EQ-CHEM-80 degeneracies, reordered by the spin–orbit splitting of EQ-CHEM-79; the closed-shell gaps land at these integers. The reordering depends on the fitted V_ls (**D5**); the resulting numbers are counts (**D3**).
- **Constants:** {2,8,20,28,50,82,126} [count → D3].
- **Status:** DERIVED-given-decrees (given fitted spin–orbit strength).

### EQ-CHEM-82 — Binding energy definition
- **Equation:** B(A,Z) = [Z m_p + N m_n − M(A,Z)] c²
- **Source:** 09-ELEMENT_PREDICTION.md (§2.1)
- **Spine path:** S0→S1→S2
- **Decrees:** D3 (Z, N, A counts), D4 (masses)
- **Trace:** 1=1 → S1 mass-difference bookkeeping; E=mc² (parent: relativity domain) converts to energy.
- **Constants:** m_p, m_n, c [SELECTED scale → D4]; Z, N, A [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-83 — Semi-empirical mass formula (SEMF)
- **Equation:** B(A,Z) = a_V A − a_S A^{2/3} − a_C Z(Z−1)/A^{1/3} − a_A (A−2Z)²/A + δ(A,Z)
- **Source:** 09-ELEMENT_PREDICTION.md (§2.2–2.7 boxed)
- **Spine path:** S0→S1→S2→S3→S6
- **Decrees:** D1, D2, D3 (Z,N,A), D4, D5 (all five coefficients fitted), D6
- **Trace:** 1=1 → S1-sum of five physical contributions, each derived in §2: volume (strong saturation, EQ-CHEM-77), surface (membrane boundary, **D6**), Coulomb (EQ-CHEM-15/6D Green's function), asymmetry (Pauli/fermion statistics, EQ-CHEM-34), pairing (Cooper-like, EQ-CHEM-75 analog). Each coefficient is matched to data (**D5**), though the doc argues each is *also* estimable from 6D scales.
- **Constants:** a_V=15.68, a_S=18.56, a_C=0.717, a_A=28.1, Δ=11.0 MeV [each FIT → D5, dimensionful → D4].
- **Status:** DERIVED-given-decrees (coefficients are fits; honest residuals noted).

### EQ-CHEM-84 — Coulomb coefficient from 6D Green's function
- **Equation:** a_C = (3/20πε₀ r₀) e² = [3/(20π)]·(1.44 MeV·fm)/(1.2 fm) ≈ 0.717 MeV
- **Source:** 09-ELEMENT_PREDICTION.md (§2.4, §7.3)
- **Spine path:** S0→S2→S3→S6
- **Decrees:** D2, D4
- **Trace:** 1=1 → integrate the Coulomb energy (EQ-CHEM-15) over a uniform charged sphere; the 3/20 factor is the analytic self-energy integral. r₀ sets the scale (**D4**).
- **Constants:** e²/(4πε₀)=1.44 MeV·fm [SELECTED scale → D4]; r₀=1.2 fm [SELECTED scale → D4]; 3/20 [DERIVED ratio].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-85 — Pairing term
- **Equation:** δ(A,Z) = +Δ/A^{1/2} (even-even), 0 (odd-A), −Δ/A^{1/2} (odd-odd); Δ≈11 MeV
- **Source:** 09-ELEMENT_PREDICTION.md (§2.6)
- **Spine path:** S0→S6→S8
- **Decrees:** D3 (parity counts), D4, D5 (Δ fitted), D6
- **Trace:** 1=1 → Cooper-like nucleon pairing (EQ-CHEM-75 analog) on the Firmament (**D6**); the A^{−1/2} scaling and parity sign pattern from like-nucleon pairing. Δ is fit (**D5**).
- **Constants:** Δ≈11 MeV [FIT → D5].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-86 — Binding energy per nucleon
- **Equation:** B/A = a_V − a_S A^{−1/3} − a_C Z(Z−1)/A^{4/3} − a_A(A−2Z)²/A² + δ/A; peak at A≈56–62
- **Source:** 09-ELEMENT_PREDICTION.md (§2.8)
- **Spine path:** S0→S1→S6
- **Decrees:** D3, D4, D5
- **Trace:** 1=1 → divide EQ-CHEM-83 by A; the iron-peak maximum follows from the competing A-powers. Algebra.
- **Constants:** as in EQ-CHEM-83 [FIT → D5 / SELECTED → D4].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-87 — Alpha-decay Q-value and proton drip line
- **Equation:** Q_α = B(A,Z) − B(A−4,Z−2) − B(4,2); drip when B(A,Z+1) < B(A,Z); ΔB ≈ −a_C 2Z/A^{1/3}
- **Source:** 09-ELEMENT_PREDICTION.md (§3.1)
- **Spine path:** S0→S1→S6
- **Decrees:** D3, D4, D5
- **Trace:** 1=1 → finite differences of EQ-CHEM-83 in Z; sign change marks the drip line. Algebra over the SEMF.
- **Constants:** a_C etc. [FIT → D5].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-88 — Nuclear saturation density
- **Equation:** ρ = 3A/[4π(1.2 A^{1/3})³] ≈ 0.16 nucleons/fm³ (A-independent)
- **Source:** 09-ELEMENT_PREDICTION.md (§3.1)
- **Spine path:** S0→S2→S3
- **Decrees:** D4 (r₀=1.2 fm)
- **Trace:** 1=1 → geometric ratio A/volume with R∝A^{1/3}; the A-dependence cancels, leaving a constant set by r₀ (**D4**).
- **Constants:** r₀=1.2 fm [SELECTED scale → D4]; 0.16 fm⁻³ [DERIVED from r₀].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-89 — Fissility parameter
- **Equation:** x = E_Coul/(2E_surf) = (a_C/2a_S)(Z²/A) = 0.01932 Z²/A; fission when x≥1 ⇒ Z²/A ≥ 51.8
- **Source:** 09-ELEMENT_PREDICTION.md (§3.2)
- **Spine path:** S0→S2→S6
- **Decrees:** D3, D5 (via a_C, a_S)
- **Trace:** 1=1 → ratio of the Coulomb to surface terms of EQ-CHEM-83; the 0.01932 = a_C/(2a_S) is a ratio of fitted coefficients. Algebra.
- **Constants:** a_C/2a_S = 0.01932 [DERIVED ratio of FIT→D5 constants]; 51.8 [DERIVED ratio]; Z,A [count → D3].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-90 — Shell-corrected binding and alpha half-life
- **Equation:** B_total = B_SEMF + B_shell; log₁₀(t_{1/2}/s) = 0.315 Z_d/√Q_α − 0.415
- **Source:** 09-ELEMENT_PREDICTION.md (§3.2, §5.2)
- **Spine path:** S0→S1→S6
- **Decrees:** D3, D4, D5 (Geiger–Nuttall coefficients 0.315, 0.415 fitted; B_shell≈1–3 MeV)
- **Trace:** 1=1 → add a shell correction to EQ-CHEM-83; the Geiger–Nuttall half-life law is an empirical fit of tunneling through the Coulomb barrier (parent: nuclear domain). Coefficients are **D5**.
- **Constants:** 0.315, 0.415 [FIT → D5]; B_shell≈1–3 MeV [FIT → D5]; Z_d [count → D3].
- **Status:** PARTIAL (Geiger–Nuttall law is an empirical fit, not derived here).

### EQ-CHEM-91 — Neutron drip line (separation energy)
- **Equation:** S_n = B(A,Z) − B(A−1,Z) ≈ a_V − a_S A^{−1/3} − a_A 4(A−2Z)/A; drip at S_n=0 ⇒ N ≈ 0.14 A (naive)
- **Source:** 09-ELEMENT_PREDICTION.md (§3.3)
- **Spine path:** S0→S1→S6
- **Decrees:** D3, D5
- **Trace:** 1=1 → finite difference of EQ-CHEM-83 in N; S_n=0 marks the neutron drip. The naive N≈0.14A is corrected by magic-number shell gaps (the doc honestly flags the naive estimate as wrong).
- **Constants:** a_V, a_S, a_A [FIT → D5].
- **Status:** DERIVED-given-decrees (naive form; shell-corrected honestly noted).

### EQ-CHEM-92 — Relativistic 1s energy and critical Z
- **Equation:** E_{1s} = m_e c² √(1−(Zα)²); Z_crit ≈ 1/α ≈ 137 (point), ≈ 170–173 (finite size); Z_crit^ext = α⁻¹√(1−α²R/a₀)
- **Source:** 09-ELEMENT_PREDICTION.md (§4.2, §4.4 boxed)
- **Spine path:** S0→S4→S5→S6
- **Decrees:** D2 (charge), D3 (Z), D4, D5 (via α prefactor)
- **Trace:** 1=1 → exact Dirac 1s eigenvalue (EQ-CHEM-09) for a point Coulomb source; the energy goes imaginary at Zα=1, giving Z_crit=α⁻¹. Finite nuclear size shifts it to ~170. α from EQ-CHEM-16.
- **Constants:** α [see EQ-CHEM-16]; m_e,c [SELECTED scale → D4]; Z_crit≈137/170 [DERIVED ratio anchored by D5].
- **Status:** DERIVED-given-decrees.

### EQ-CHEM-93 — Period-8 Aufbau order (predicted)
- **Equation:** filling 8s → 5g → 6f → 7d → 8p; 50 elements Z=119–168
- **Source:** 09-ELEMENT_PREDICTION.md (§4.3, §8.2)
- **Spine path:** S0→S5→S8
- **Decrees:** D3 (orbital/element counts)
- **Trace:** 1=1 → extend the n+l Aufbau rule (EQ-CHEM-42) to n=8; first appearance of l=4 (g-block). Pure counting + the n+l ordering.
- **Constants:** capacities 2,18,14,10,6 [count → D3].
- **Status:** DERIVED-as-form (given D3).

### EQ-CHEM-94 — Z_max from zone-scale α
- **Equation:** Z_max ≈ α⁻¹ ≈ 137 (point) / 170–173 (finite); α⁻¹ ~ 1.44 ln(ξ_A/η_B) ~ 1.44×94 ≈ 137
- **Source:** 09-ELEMENT_PREDICTION.md (§4.4 boxed)
- **Spine path:** S0→S2→S3→S4
- **Decrees:** D4 (ξ_A,η_B scales), D5 (1.44 prefactor), D6
- **Trace:** 1=1 → combine EQ-CHEM-92 (Z_max=α⁻¹) with EQ-CHEM-16 (α from zone-scale ratio); the maximum element is encoded in the ξ_A/η_B architecture (**D6**). Prefactor 1.44 is fitted (**D5**).
- **Constants:** 1.44 [FIT → D5]; ξ_A,η_B [SELECTED scale → D4]; 137 [DERIVED ratio anchored by D5].
- **Status:** PARTIAL (rests on EQ-CHEM-16; numeric prefactor is D5/open).

### EQ-CHEM-95 — SEMF prediction for superheavy elements (Z=119, 120)
- **Equation:** B(305,119) ≈ 4782−2130−45−45 = 2562 MeV; Q_α ≈ 2562−2534−28.3 = −0.3 MeV; log₁₀ t_{1/2} ≈ 0.315×118/√6 − 0.415
- **Source:** 09-ELEMENT_PREDICTION.md (§5.1–5.2)
- **Spine path:** S0→S1→S6
- **Decrees:** D3 (Z,N,A), D4, D5
- **Trace:** 1=1 → evaluate EQ-CHEM-83 and EQ-CHEM-90 at specific (A,Z). Pure substitution; predictions for elements 119–130.
- **Constants:** SEMF coefficients [FIT → D5]; Z,N,A [count → D3].
- **Status:** DERIVED-given-decrees (numerical application).

---

## MISSED EQUATIONS RECOVERED IN AUDIT (appended)

### EQ-CHEM-96 — H₂ molecular binding curve / Morse potential
- **Equation:** E_mol(R)=2E_+ + V_nuclear(R); V_nuclear(R)=e²/(4πε₀R); ∂E_mol/∂R=0 ⇒ R_eq; E_mol(R)=D_e[1−e^{−a(R−R_eq)}]²+E₀ (R_eq≈0.7414 Å, D_e≈4.747 eV exper.)
- **Source:** 09-COMPLETIONS.md (§2.4, eqs 2.9–2.14)
- **Spine path:** S0→S1→S2→S6
- **Decrees:** D2 (nuclear/electron charge in the Coulomb repulsion), D4
- **Trace:** 1=1 → S1 energy bookkeeping: twice the bonding-MO energy E_+ (EQ-CHEM-48/50) plus the inter-nuclear Coulomb repulsion (EQ-CHEM-17 form, charge = **D2**); minimize over R (S6 stationarity, ∂E_mol/∂R=0) to fix R_eq. The Morse form D_e[1−e^{−a(R−R_eq)}]² is the standard analytic fit to the resulting binding curve; D_e, a, R_eq are dimensionful scales (**D4**). R_eq=0.7414 Å and D_e=4.747 eV are quoted **experimental** values (data, not derived).
- **Constants:** e²/(4πε₀) [SELECTED scale → D4]; D_e, a, R_eq, E₀ [SELECTED scale → D4]; experimental R_eq=0.7414 Å, D_e=4.747 eV [FIT → D5 (experimental targets)].
- **Status:** DERIVED-given-decrees (binding-curve form; Morse parameters and quoted numbers are experimental).

### EQ-CHEM-97 — Total energy of an electron on the membrane
- **Equation:** E_total = E_kinetic + E_potential + m_e c²; E_kinetic = −(ℏ²/2m_e)∇²ψ; E_potential = Coulomb + membrane-curvature term
- **Source:** 09-CHEMISTRY_DERIVATION.md (§5.1, eq 5.1)
- **Spine path:** S0→S1→S6→S9
- **Decrees:** D1, D2 (Coulomb/charge content), D4 (m_e, ℏ), D6 (electron as fermionic defect on the Firmament; curvature term is membrane geometry)
- **Trace:** 1=1 → S1 additive decomposition of the single-electron energy into kinetic (S6 ∇² operator), potential (Coulomb = EQ-CHEM-17 + the 6D membrane-curvature contribution from S9, **D6**), and rest energy m_e c² (parent: relativity). The electron's status as a topological defect on the Firmament and the curvature-as-potential reading are **D6** physical content; the charge coupling is **D2**.
- **Constants:** ℏ, m_e, c [SELECTED scale → D4].
- **Status:** DERIVED-as-form (given D1, D2, D4, D6).

---

## UNTRACEABLE / FLAGGED ITEMS

### UT-01 — Electron mass from extra-dimensional confinement
- **Equation (claimed):** m_e = ℏc/ξ_A (≈ 0.511 MeV) [ELEMENT_PREDICTION §7.1 table]; "electron mass is related to confinement in (ξ,η)" [CHEMISTRY §6.3]
- **Reason UNTRACEABLE:** The relation m_e = ℏc/ξ_A is asserted in a scale table with no derivation, and the prose explicitly admits the electron mass origin is "speculative but promising" and "requires solving the full 6D Firmament equation for topological solitons" (Phase 4.0). Dimensionally m_e c² = ℏc/ξ_A would put ξ_A at the electron Compton scale (~10⁻¹³ m), which contradicts the ξ_A ~ 10²⁶ m used elsewhere for α. This is an internally inconsistent placeholder, not a derivation. Marked UNTRACEABLE per honesty rules — chain not fabricated.

### UT-02 — Numeric value of the fine-structure prefactor 1.4383 / 1.44
- **Equation (claimed):** α⁻¹ = 1.4383 ln(ξ_A/η_B); α⁻¹ ≈ 1.44 ln(ξ_A/η_B)
- **Reason UNTRACEABLE:** The functional form (α as a log of a zone-scale ratio) traces to S2/S3 + D4 (EQ-CHEM-16), but the specific prefactor 1.4383 (and its rounding 1.44) has no spine derivation in this domain — the parent `FINE_STRUCTURE_DERIVATION.md` is itself flagged "Phase 1 result, incomplete." It is a number matched to reproduce 137.036, i.e. an open **[FIT → D5]** item, not a derived ratio. Recorded here as the genuinely open numerical input behind EQ-CHEM-16/94.

### UT-03 — Spurious α factor in the Madelung energy (COMPLETIONS §3.2)
- **Equation (as written):** U_Madelung = −N_A M α e²/(4πε₀ R), with the worked NaCl line "−1.748×(1/137)×1440/2.81 = −6.54 eV"
- **Reason UNTRACEABLE (as written):** Inserting the fine-structure constant α into the ionic Madelung energy is dimensionally/physically wrong: the Coulomb energy e²/(4πε₀) already equals 14.40 eV·Å, so multiplying by α≈1/137 under-counts by ~137× (the correct Madelung energy for NaCl is ≈ −8 eV, not −6.54 eV reached by an offsetting arithmetic slip). The CHEMISTRY/ATOMIC files give the correct α-free Madelung form (EQ-CHEM-63). This COMPLETIONS variant cannot be traced as written; flagged as an internal error, not fabricated into a chain. (The correct version is traced as EQ-CHEM-63.)

---

## COVERAGE NOTES

- **Duplications:** The four prose files heavily overlap (periodic table, bonding, Madelung, Bloch
  bands appear in 3–4 files). Where an equation is the same result restated, it is traced once in
  full and the duplicate cites the canonical entry (e.g. EQ-CHEM-46→43, 53→15, 61/54, 73→63).
- **Parent-domain results:** The Schrödinger equation (EQ-CHEM-11/45), Dirac equation (EQ-CHEM-09),
  Coulomb potential (EQ-CHEM-15/17), α (EQ-CHEM-16), spin-statistics (EQ-CHEM-18), SU(3)/confinement
  (EQ-CHEM-76/77) are genuinely *derived in domains 03/05/06 and the Foundations*; this ledger cites
  them by their rung path and decrees rather than re-deriving, per the schema's "cite rungs; never
  re-derive" rule.
- **Honesty residuals carried from the source files:** Slater-rule ionization energies (20–300% error),
  helium variational energy (~1.9% with the *correct* Z_eff, but the .md's own −19.365 eV is an
  internal arithmetic error, EQ-CHEM-38/39), SEMF coefficients as fits (D5), and the two open
  α-related numbers (UT-02) are all flagged rather than presented as clean derivations.
- **Pure-math theorems** (crystallographic restriction → 7 systems / 230 space groups, EQ-CHEM-62;
  close-packing fraction, EQ-CHEM-64) need only D1 (3D space); they are the cleanest "given one
  decree" entries in the domain.
