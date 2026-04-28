# Appendix E: Notation Reference — Complete Series

**Product:** Foundations Vol 6, Predictions, Simulations, and Open Problems
**Component:** Back Matter, Appendix E
**Scope:** The definitive, arbitrating symbol reference for the entire six-volume *Foundations of Genesis Physics* series. Extends the Vol 1 Appendix B notation scheme without superseding it; consolidates every symbol introduced anywhere in Vols 1–6; records deprecated and superseded notation.
**Convention:** Citation format `(V.Ch.Eq)` with `V ∈ {1,2,3,4,5,6}`. First-appearance locators are given as `V.Ch` (volume and chapter).

---

## E.1  How to Use This Appendix

Appendix E is the arbiter. If any chapter in any volume of the Foundations Series uses a symbol that is not documented here, one of two things must happen: either the symbol is added to this appendix (the usual resolution, when the chapter's usage is correct), or the chapter's notation is corrected to match (the resolution when the chapter has drifted). The Consistency Auditor runs the series-wide symbol audit against Appendix E on every validation cycle. Appendix E wins ties.

This is the complete-series reference. The canonical source for core membrane, zone, and cosmological parameters remains `Quality_Control/Reference/Symbol_and_Constants.md`, which this appendix consumes and expands. Vol 1 established the foundational notation in its own Appendix B (the zone manifold, Waters fields, Firmament, sustaining coupling). This appendix does not redefine those symbols — it preserves their Vol 1 definitions verbatim and appends every symbol that subsequent volumes introduced. Readers checking a symbol first encountered in Vol 1 will find its canonical entry here; readers checking a symbol from Vol 4 (the largest expansion) will find it here as well.

**What is in scope.** Every mathematical symbol that carries a technical meaning anywhere in Vols 1–6: Latin and Greek letters standing for fields, observables, operators, parameters, or indices; mathematical operators and relations (∇, ⊗, □, 〈·〉); index and tensor conventions; unit conventions (when they vary volume-to-volume); zone-architecture-specific notation (zone labels, Waters fields, boundary scales); all physical constants that appear in the series; the `P-XXX` prediction identifier scheme and the `T-XXX` technology identifier scheme; and any symbol that was used in an early draft and later superseded.

**What is out of scope.** Hebrew and Greek theological terms (covered in `Quality_Control/Reference/Glossary.md`). Axiom labels (covered in `Quality_Control/Reference/Axiom_Summary_Cards.md`). Scripture references (covered in `Quality_Control/Reference/Biblical_References.md`). One-off disposable variables internal to a single derivation (e.g., dummy indices, integration variables, temporary algebra) — these are local to the proof and not reused.

**Row format.** Every entry in the tables below uses one of two formats. The **long form**, used in the body sections (E.2 Latin letters through E.7 Zone-architecture notation), has six columns:

| Symbol | Name | Definition / Units | First Appears | Used In | Related |

The **compact form**, used in quick-reference blocks and the constants table (E.8), trims the locator columns where a symbol is series-wide. "First Appears" is the volume and chapter where the symbol is introduced with its current meaning (not necessarily its first informal mention). "Used In" lists every volume that references the symbol substantively. "Related" names the nearest neighbor symbols the reader should consult for context.

**Reading conventions.** Where a symbol has different conventional meanings in different sub-disciplines (e.g., `σ` is membrane tension in Vol 1 but Pauli-matrix index in Vol 4), both senses are listed and disambiguated by the volume tag in the "First Appears" column. Where a symbol appears with a subscript that changes its meaning (e.g., `κ_full` vs. `κ_partial`), each variant has its own row. Where the series uses a symbol in a way that conflicts with ordinary physics convention (rare, but it happens — see `κ` for sustaining-field power density, not second-law spring-constant), the nonstandard use is flagged with a ⚠ marker in the Definition column.

**How to extend Appendix E.** When a new chapter introduces a symbol, the chapter author is responsible for (a) checking whether the symbol already exists here, (b) if it does, using it exactly as defined, (c) if it does not, proposing an Appendix E row. The Consistency Auditor reviews the proposed row before the chapter is finalized.

---

## E.2  Latin Letters

Alphabetical, lowercase first, then uppercase. Entries for which the symbol is already in widespread physics use (e.g., `c` for speed of light, `e` for elementary charge) list the *derivation context* from zone architecture rather than the universal definition.

### E.2.1 Lowercase Latin

| Symbol | Name | Definition / Units | First Appears | Used In | Related |
|--------|------|---------------------|----------------|---------|---------|
| `a` | Cosmic scale factor | Dimensionless; FRW metric expansion factor, normalized to `a(t_now)=1` in most contexts | 5.Ch 8 | V5, V6 | `H`, `H₀`, `z` |
| `a_e` | Electron anomalous magnetic moment | Dimensionless; $(g_e-2)/2$, computed perturbatively from zone-derived QED | 4.Ch 7 | V4, V6 | `g_e`, `α` |
| `a_μ` | Muon anomalous magnetic moment | Dimensionless | 4.Ch 7 | V4, V6 | `a_e`, `α` |
| `b_eff`, `b_hi` | One- and two-loop coefficients in α derivation | Dimensionless | 5.Ch 13 | V5, V6 | `α`, `ξ_A`, `η_B` |
| `c` | Speed of light | 2.998 × 10⁸ m/s; derived as `c = √(σ/μ)` from membrane mechanics | 1.Ch 5 | All vols | `σ`, `μ`, `c_local` |
| `c_local` | Position-dependent local `c` | `c²_local = c₀²(1 + εR/(c₀²ρ_c))`; zone-architecture correction to classical GR constancy | 6.Ch 9 | V6 | `c`, `R` (Ricci), `ρ_c` |
| `d` | Gap width (Casimir, MRG) | m; boundary separation in dynamic-Casimir and MRG contexts | 4.Ch 9 | V4, V6 | `F/A`, `κ(f,f_n)` |
| `e` | Elementary charge | 1.602 × 10⁻¹⁹ C; emerges from brane U(1) topology | 2.Ch 6 | V2, V4, V6 | `α`, `Q` |
| `f` | Frequency | Hz; generic frequency variable | 1.Ch 5 | All vols | `ω`, `f_n`, `f_1` |
| `f_n` | nth resonant mode frequency | Hz; membrane vibration eigenfrequencies | 1.Ch 5 | V1, V6 | `f_1`, `ω_n` |
| `g` | Weak gauge coupling | Dimensionless; SU(2) coupling in electroweak sector | 4.Ch 11 | V4, V6 | `g'`, `M_W`, `v` |
| `g'` | Hypercharge gauge coupling | Dimensionless; U(1)_Y coupling | 4.Ch 11 | V4, V6 | `g`, `θ_W` |
| `g_e` | Electron g-factor | Dimensionless; `g_e ≈ 2.002319...` (zone-derived perturbatively) | 4.Ch 7 | V4, V6 | `a_e` |
| `g_μν` | Metric tensor | Dimensionless (coordinate-dependent); 4D-brane or 6D-bulk depending on context | 1.Ch 4 | All vols | `η_μν`, `R_μν` |
| `h` | Planck constant | 6.626 × 10⁻³⁴ J·s; derived from brane boundary quantization | 4.Ch 1 | V4, V5, V6 | `ℏ`, `m_P` |
| `h_+, h_×` | Tensor GW polarizations | Dimensionless strain amplitudes | 5.Ch 3 | V5, V6 | `h_S, h_L, h_V1, h_V2` |
| `h_S, h_L` | Scalar-breathing, longitudinal-scalar GW modes | Dimensionless strain; **novel in 6D zone theory** | 5.Ch 3 | V5, V6 | `h_+`, `h_V1,V2` |
| `h_V1, h_V2` | Vector GW polarization modes | Dimensionless strain; 6D-theory signatures | 5.Ch 3 | V5, V6 | `h_+`, `h_S` |
| `j^μ` | Conserved Noether current | Units per conserved quantity (e.g., C·m⁻²·s⁻¹ for charge current) | 1.Ch 7 | V1, V2, V4 | `∂_μ`, `Q` |
| `k` | Wave number | m⁻¹; $k = 2\pi/\lambda$ | 2.Ch 3 | All vols | `λ`, `ω` |
| `k_B` | Boltzmann constant | 1.381 × 10⁻²³ J/K | 1.Ch 11 | V1, V3, V5, V6 | `S`, `T` |
| `k_cut` | Waters-field power spectrum cutoff wavenumber | m⁻¹; `k_cut ~ 1/η_B` | 1.Ch 6 | V1, V5, V6 | `η_B` |
| `m` | Mass | kg or eV/c² (see E.6) | 1.Ch 5 | All vols | `m_P`, `m_e`, `m_H` |
| `m_e` | Electron mass | 0.511 MeV/c² | 4.Ch 10 | V4, V6 | `m_μ`, `y_e` |
| `m_μ` | Muon mass | 105.66 MeV/c² | 4.Ch 10 | V4, V6 | `m_e`, `m_τ` |
| `m_H` | Higgs boson mass | 125.10 GeV/c² | 4.Ch 11 | V4, V6 | `v`, `y_t` |
| `m_P` | Planck mass | 2.18 × 10⁻⁸ kg; $\sqrt{\hbar c/G}$ | 4.Ch 9 | V4, V5, V6 | `ℓ_P`, `t_P` |
| `m_Ψ` | Waters-field effective mass | eV/c²; `m_Ψc² ~ 10⁻³ eV` bound | 6.Ch 11 | V6 | `Ψ_A, Ψ_B`, `λ_W` |
| `n` | Integer mode index | Dimensionless; labels eigenstates of a boundary problem | 1.Ch 10 | V1, V4, V6 | `n_ξ`, `n_η` |
| `n_ξ, n_η` | Boundary quantum numbers (ξ and η directions) | Integer; mode indices in compact dimensions | 4.Ch 10 | V4, V6 | `ξ_A`, `η_B`, `m_e` |
| `p` | Momentum or pressure (context-dependent) | kg·m/s or Pa | 1.Ch 6 | All vols | `P^i`, `w` |
| `q` | Electric charge (generic) | C | 2.Ch 3 | V2, V4 | `e`, `Q` |
| `r` | Radial coordinate | m | 3.Ch 3 | V3, V5, V6 | `r_+`, `R_compact` |
| `r_+` | Event-horizon radius / outer horizon | m; warp-bubble context | 6.Ch 9 | V6 | `T_H` |
| `s` | Mandelstam variable or entropy density (context) | GeV² or J·K⁻¹·m⁻³ | 3.Ch 9 | V3, V4 | `S`, `t`-channel, `u`-channel |
| `t` | Time | s | 1.Ch 4 | All vols | `τ`, `t_0`, `t_P` |
| `t_0` | Present age of universe | 13.787 Gyr | 5.Ch 8 | V5, V6 | `H₀` |
| `t_P` | Planck time | 5.39 × 10⁻⁴⁴ s | 4.Ch 9 | V4, V5, V6 | `ℓ_P`, `m_P` |
| `u^μ` | Four-velocity | m/s (or dimensionless in natural units) | 5.Ch 2 | V5 | `g_μν` |
| `v` | Electroweak VEV | 246 GeV; Higgs vacuum expectation value | 4.Ch 11 | V4, V6 | `m_H`, `M_W` |
| `v_g` | Group velocity (Waters field) | m/s; `v_g = c√(1 − m_Ψ²c⁴/(ℏ²ω²))` | 6.Ch 11 | V6 | `m_Ψ`, `ω` |
| `w` | Equation-of-state parameter | Dimensionless; `w ≈ −1` for Ψ_A, `w ≈ 0` for Ψ_B | 5.Ch 11 | V5, V6 | `Ω_Λ`, `ρ_A` |
| `w_a` | Dark-energy equation-of-state evolution parameter | Dimensionless; CPL parameterization `w(a) = w₀ + (1−a)w_a` | 5.Ch 11 | V5, V6 | `w` |
| `x^μ` | Spacetime coordinate (Greek index implicit) | m (or dimensionless in natural units) | 1.Ch 4 | All vols | `g_μν`, `∂_μ` |
| `y_e, y_b, y_t, y_τ` | Yukawa couplings | Dimensionless | 4.Ch 11 | V4, V6 | `v`, `m_e`, `m_t` |
| `z` | Cosmological redshift | Dimensionless | 5.Ch 8 | V5, V6 | `a`, `H` |

### E.2.2 Uppercase Latin

| Symbol | Name | Definition / Units | First Appears | Used In | Related |
|--------|------|---------------------|----------------|---------|---------|
| `A` | Area, or gauge potential (context) | m², or V·s/m | 2.Ch 3 | V2, V4, V6 | `A_μ`, `F_μν` |
| `A_μ` | Electromagnetic 4-potential | V·s/m | 2.Ch 3 | V2, V4 | `F_μν`, `j^μ` |
| `B` | Magnetic field, or bandwidth (context) | T, or Hz | 2.Ch 3 | V2, V4, V6 | `E`, `F_μν` |
| `B_total` | Total baryon number | Dimensionless; approximately conserved | 1.Ch 7 | V1, V4 | `L_total`, `Q_total` |
| `C` | Capacitance or central charge (context) | F or dimensionless | 2.Ch 5 | V2, V4 | `L`, `R` |
| `D` | Displacement field or covariant derivative (context) | C/m² or dimensionless | 2.Ch 3 | V2, V4 | `∇`, `E` |
| `D_μ` | Gauge-covariant derivative | Dimensionless | 4.Ch 5 | V4 | `∂_μ`, `A_μ` |
| `E` | Electric field or energy (context) | V/m or J | 2.Ch 3 | All vols | `B`, `F_μν`, `U` |
| `E_binding` | Brane binding energy | J; $E_{\rm binding} = \sigma|\Delta\eta|$ | 6.Ch 9 | V6 | `σ`, `η_B` |
| `E_GW` | Gravitational-wave radiated energy | J | 5.Ch 3 | V5, V6 | `h_+, h_×` |
| `E_η` | η-boundary energy scale | GeV; `E_η ~ 150 GeV` | 4.Ch 12 | V4, V6 | `η_B`, `α_s` |
| `F` | Force or free energy (context) | N or J | 3.Ch 1 | V3, V4 | `m`, `a`, `S` |
| `F_μν` | Electromagnetic field tensor | V·s/m² | 2.Ch 3 | V2, V4 | `A_μ`, `E`, `B` |
| `𝓕` (script F) | Firmament field (when expressed as a scalar) | Dimensionless or m² (context) | 1.Ch 5 | V1 | `Z₂.₂`, `K_ij` |
| `G` | Gravitational constant | 6.674 × 10⁻¹¹ m³·kg⁻¹·s⁻²; `G = c⁴/(8πσ·L_eff²)` from 6D reduction | 2.Ch 9 | V2, V5, V6 | `σ`, `L_eff` |
| `G(r, η*)` | Zone-tunneling channel Green's function | Dimensionless (as an amplitude) | 6.Ch 11 | V6 | `η_B`, `η*` |
| `G_μν` | Einstein tensor | m⁻² | 5.Ch 2 | V5 | `R_μν`, `T_μν` |
| `H` | Hubble parameter or Hamiltonian (context) | s⁻¹ or J | 5.Ch 8 | V5, V6 | `H₀`, `a` |
| `H₀` | Hubble constant (present) | 67.4 km/s/Mpc | 5.Ch 8 | V5, V6 | `H`, `t_0` |
| `I` | Action or moment of inertia (context) | J·s or kg·m² | 1.Ch 7 | V1, V3 | `S` (action), `L` |
| `K_ij` | Extrinsic curvature tensor of Firmament hypersurface | m⁻¹ | 1.Ch 5 | V1, V5 | `𝓕`, `g_μν` |
| `L` | Angular momentum or Lagrangian (context) | kg·m²/s or J | 1.Ch 7 | All vols | `L^k`, `S`, `I` |
| `L^k` | Angular momentum component | kg·m²/s | 1.Ch 7 | V1, V3 | `L` |
| `L_eff` | Effective 6D-reduction coupling length | 8.96 × 10⁻²⁹ m | 1.Ch 4 | V1, V2 | `G`, `σ` |
| `L_total` | Total lepton number | Dimensionless; approximately conserved | 1.Ch 7 | V1, V4 | `B_total`, `Q_total` |
| `M_W` | W boson mass | 80.377 GeV/c²; `M_W = gv/2` | 4.Ch 11 | V4, V6 | `g`, `v` |
| `M_Z` | Z boson mass | 91.1876 GeV/c² | 4.Ch 11 | V4, V6 | `M_W`, `θ_W` |
| `N` | Particle number, boundary count, or sample size (context) | Dimensionless | 1.Ch 11 | All vols | `N_ν` |
| `N_ν` | Number of light neutrino species | 3 (topologically distinct boundary modes) | 4.Ch 11 | V4, V6 | `ν`, `N` |
| `P` | Power or probability (context) | W or dimensionless | 6.Ch 10 | V6 | `P_net`, `P_ext` |
| `P^i` | Momentum 3-vector component | kg·m/s | 1.Ch 7 | V1, V3 | `p` |
| `P_net` | MRG net power output | W; `P_net ≥ 30 W` (target) | 6.Ch 10 | V6 | `η` (efficiency), `κ(f,f_n)` |
| `Q` | Quality factor or total charge (context) | Dimensionless or C | 1.Ch 7 | V1, V2, V4, V6 | `Q_total`, `q` |
| `Q_total` | Total electric charge | C; conserved by U(1) gauge symmetry | 1.Ch 7 | V1, V2 | `j^μ` |
| `R` | Ricci scalar curvature, or rate (context) | m⁻² or Hz | 5.Ch 2 | V5, V6 | `R_μν`, `G_μν` |
| `ℛ` (script R) | Hierarchy ratio in EM-to-gravitational derivation | Dimensionless | 2.Ch 9 | V2, V6 | `α_em/α_G` |
| `R_compact` | Compactification radius (extra dimension) | m; `R ~ η_B` | 5.Ch 3 | V5, V6 | `η_B`, `m_KK` |
| `R_eff` | Effective compactification radius | m | 5.Ch 3 | V5, V6 | `R_compact` |
| `R_μν` | Ricci tensor | m⁻² | 5.Ch 2 | V5 | `R`, `G_μν` |
| `S` | Entropy, or action (context) | J/K or J·s | 1.Ch 11 | All vols | `dS/dt`, `I` |
| `S_CHSH` | CHSH Bell parameter | Dimensionless; Tsirelson bound `S ≤ 2√2` | 4.Ch 4 | V4, V6 | `δS` |
| `T` | Temperature or kinetic energy (context) | K or J | 1.Ch 11 | All vols | `T_c`, `T_H`, `T_μν` |
| `T_c` | Critical temperature (superconductivity or BEC) | K | 4.Ch 13 | V4, V6 | `λ_L` |
| `T_eff` | Effective channel noise temperature | K; `~10⁻¹³ K` for zone-tunneling | 6.Ch 11 | V6 | `B`, `SNR` |
| `T_H` | Hawking temperature | K; `T_H = ℏc³/(8πGk_Br_+)` | 6.Ch 9 | V6 | `r_+` |
| `T_μν` | Stress-energy tensor | J/m³ | 5.Ch 2 | V5 | `G_μν`, `ρ`, `p` |
| `V` | Volume or potential (context) | m³ or V | 1.Ch 11 | All vols | `V_eff`, `V_0` |
| `V_0` | Barrier height (tunneling contexts) | J | 4.Ch 3 | V4, V6 | `P` (prob) |
| `V_extra` | Non-Newtonian gravitational potential correction | J; short-range deviation signature | 2.Ch 9 | V2, V6 | `G`, `r` |
| `W` | Work function (photoelectric), or W boson (context) | J (work function) | 4.Ch 1 | V4, V6 | `M_W`, `hf` |
| `Z` | Zone label (integer), or partition function (context) | Dimensionless | 1.Ch 1 | All vols | `Z₀, Z₁, Z₂, ...` |

---

## E.3  Greek Letters

Alphabetical by Greek-alphabet name: α (alpha), β (beta), γ (gamma), δ (delta), ε (epsilon), ζ (zeta), η (eta), θ (theta), ι (iota), κ (kappa), λ (lambda), μ (mu), ν (nu), ξ (xi), ο (omicron, not used), π (pi), ρ (rho), σ (sigma), τ (tau), υ (upsilon, not used), φ/ϕ (phi), χ (chi), ψ/Ψ (psi), ω/Ω (omega).

| Symbol | Name | Definition / Units | First Appears | Used In | Related |
|--------|------|---------------------|----------------|---------|---------|
| `α` | Fine-structure constant | Dimensionless; `α⁻¹ = 1.44 × ln(ξ_A/η_B) ≈ 137.036` (zone-derived) | 5.Ch 13 | V5, V6 | `α⁻¹`, `ξ_A`, `η_B` |
| `α_em` | Electromagnetic coupling (running) | Dimensionless | 4.Ch 8 | V4 | `α` |
| `α_G` | Gravitational coupling constant | Dimensionless; `α_em/α_G = 1.24 × 10³⁶` | 2.Ch 9 | V2, V6 | `α_em`, `G` |
| `α_s` | Strong coupling constant | Dimensionless; `α_s(M_Z) = 0.118` | 4.Ch 12 | V4, V6 | `M_Z`, `E_η` |
| `α_B` | Waters-Below coupling | Dimensionless or m³·kg⁻¹·s⁻²; `|log₁₀(α_B/G)| ≤ 1` | 6.Ch 10 | V6 | `G`, `Ψ_B` |
| `β` | Velocity fraction (`v/c`), or KK-dispersion coefficient (context) | Dimensionless | 5.Ch 1 | V5, V6 | `γ`, `v` |
| `γ` | Lorentz factor, or PPN parameter, or spectral-leakage coefficient (context) | Dimensionless | 5.Ch 1 | V5, V6 | `β`, `η` |
| `Γ_H, Γ_W, Γ_Z` | Boson total decay widths | GeV (or MeV for `Γ_H`) | 4.Ch 11 | V4, V6 | `M_H, M_W, M_Z` |
| `δ` | Small variation, or Dirac delta function (context) | Dimensionless or m⁻¹ | 1.Ch 6 | All vols | `Δ`, `δ(x)` |
| `Δ` | Finite difference, or superconducting gap (context) | Dimension of operand | 3.Ch 5 | V3, V4, V6 | `δ` |
| `Δα/α` | Fractional variation of `α` over cosmic time | Dimensionless; predicted `= 0 ± 10⁻⁹/Gyr` | 5.Ch 13 | V5, V6 | `α` |
| `Δm²₂₁, Δm²₃₂` | Neutrino mass-squared splittings | eV² | 4.Ch 11 | V4, V6 | `ν`, `m_ν` |
| `ε` | Small parameter (generic), Fall-phase subcriticality | Dimensionless; `ε ~ 10⁻²⁷ to 10⁻⁶⁰` | 1.Ch 11 | V1, V5, V6 | `κ_partial/κ_full` |
| `ε_κ` | Sustaining-coupling fluctuation amplitude | Dimensionless; `ε_κ ~ 10⁻²⁷` | 6.Ch 11 | V6 | `κ`, `δρ_Λ/ρ_Λ` |
| `ε_0` | Vacuum permittivity | 8.854 × 10⁻¹² F/m | 2.Ch 3 | V2 | `μ_0`, `c` |
| `ζ` | Riemann zeta argument (thermodynamic calculations), generic | Dimensionless | 3.Ch 10 | V3 | — |
| `η` | Efficiency, or compact-dimension coordinate, or Minkowski metric (context) | Dimensionless or m | 1.Ch 4 | All vols | `η_B`, `η_μν` |
| `η_B` | Waters Below extent (nuclear/QCD boundary) | 1.3 × 10⁻¹⁵ m | 1.Ch 6 | V1, V4, V5, V6 | `ξ_A`, `α`, `n_η` |
| `η_μν` | Minkowski metric (flat spacetime) | Dimensionless; signature `(+,−,−,−)` on brane | 1.Ch 4 | All vols | `g_μν` |
| `η_sail, η_harvest, η_osc` | Subscripted extraction-efficiency factors | Dimensionless | 6.Ch 10 | V6 | `η` |
| `θ_W` | Weinberg (weak mixing) angle | Radians; `sin²θ_W ≈ 0.23122` | 4.Ch 11 | V4, V6 | `g`, `g'`, `M_W, M_Z` |
| `Θ` | Heaviside step function, or general angle (context) | Dimensionless | 1.Ch 10 | V1, V3 | `δ`, `θ` |
| `ι` | (Not used in Foundations Series — reserved.) | — | — | — | — |
| `κ` | Sustaining-field power density | kg·m⁻¹·s⁻³ ⚠ nonstandard use (not spring-constant) | 1.Ch 8 | V1, V5, V6 | `κ_full, κ_partial, κ_create, κ_redeem` |
| `κ_create` | Supercritical sustaining (Creation Days 1–6) | `>> κ_full`; entropy-decreasing regime | 1.Ch 8 | V1 | `κ`, Four Epochs |
| `κ_full` | Edenic equilibrium sustaining | Pre-Fall baseline; zero net entropy production | 1.Ch 11 | V1, V5 | `κ`, `ε` |
| `κ_partial` | Fall-phase sustaining | `κ_full(1−ε)`; subcritical regime (present epoch) | 1.Ch 11 | V1, V5, V6 | `κ`, `ε` |
| `κ_redeem` | Redemption-phase sustaining | Entropy-reversal regime (future) | 1.Ch 11 | V1 | `κ`, Four Epochs |
| `κ(f,f_n)` | MRG membrane-resonance coupling function | Dimensionless; `∝ (η_B/λ_device)²δ(f−f_n)` | 6.Ch 10 | V6 | `P_ext`, `f_n` |
| `κ_bulk` | Bulk geodesic shortcut factor | Dimensionless; `1 + ε` with `ε ~ 10⁻⁴–10⁻²` | 6.Ch 9 | V6 | `c`, `η_B` |
| `λ` | Wavelength, or cosmological constant (Λ, uppercase), or London depth (context) | m | 2.Ch 3 | All vols | `k`, `Λ`, `λ_L` |
| `λ_L` | London penetration depth | m | 4.Ch 13 | V4, V6 | `T_c` |
| `λ_W` | Waters-field attenuation length | m; `> 10²⁷ m` | 6.Ch 11 | V6 | `m_Ψ`, `ε_κ` |
| `Λ` | Cosmological constant | 1.1 × 10⁻⁵² m⁻² | 5.Ch 11 | V5, V6 | `Ω_Λ`, `ρ_Λ` |
| `μ` | Membrane volume mass density, or magnetic moment, or chemical potential (context) | kg/m³, A·m², or J (context-dependent) | 1.Ch 5 | V1–V6 | `σ`, `c` |
| `μ_0` | Vacuum permeability | 1.2566 × 10⁻⁶ T·m/A | 2.Ch 3 | V2 | `ε_0`, `c` |
| `ν` | Neutrino, or frequency (context) | — (particle) or Hz | 4.Ch 11 | V4, V6 | `N_ν`, `Δm²` |
| `ξ` | Compact-dimension coordinate (Above direction) | m | 1.Ch 4 | V1, V4, V5 | `ξ_A`, `n_ξ` |
| `ξ_A` | Waters Above extent (Hubble-scale cosmological radius) | ~3 × 10²⁶ m | 1.Ch 6 | V1, V5, V6 | `η_B`, `α`, `n_ξ` |
| `ο` | (Not used — omicron reserved.) | — | — | — | — |
| `π` | Mathematical constant π, or pion (context) | Dimensionless or — (particle) | 1.Ch 5 | All vols | — |
| `ρ` | Mass-energy density | kg/m³ (or GeV⁴ in natural units) | 1.Ch 6 | All vols | `ρ_A, ρ_B, ρ_matter, ρ_critical` |
| `ρ_A` | Waters Above (dark energy) density | 5.8 × 10⁻²⁷ kg/m³ | 5.Ch 11 | V5, V6 | `Ψ_A`, `Ω_Λ`, `Λ` |
| `ρ_B` | Waters Below (dark matter) density | 2.3 × 10⁻²⁷ kg/m³ | 5.Ch 11 | V5, V6 | `Ψ_B`, `Ω_DM` |
| `ρ_matter` | Baryonic matter density | 4.2 × 10⁻²⁸ kg/m³ | 5.Ch 8 | V5, V6 | `Ω_b` |
| `ρ_critical` | QCD critical density | ~2.3 × 10¹⁷ kg/m³ | 4.Ch 12 | V4 | `η_B` |
| `ρ_Λ, ρ_vac` | Cosmological-constant / vacuum-energy density | GeV⁴ or kg/m³; `~10⁻⁴⁷ GeV⁴` | 5.Ch 11 | V5, V6 | `Λ`, `Ω_Λ` |
| `σ` | Membrane 3-brane tension | 6.0 × 10⁹⁸ kg·m⁻¹·s⁻² ⚠ nonstandard use (not cross-section) | 1.Ch 5 | V1, V2, V5, V6 | `μ`, `c`, `E_binding` |
| `σ_DM-SM` | Dark-matter / Standard-Model cross-section | cm²; zone-architecture predicts exactly 0 | 5.Ch 11 | V5, V6 | `Ψ_B` |
| `σ_redeem` | Redemption-phase brane tension (speculative) | kg·m⁻¹·s⁻² | 1.Ch 11 | V1 | `σ`, `κ_redeem` |
| `σ_SB` | Stefan-Boltzmann constant | 5.670 × 10⁻⁸ W·m⁻²·K⁻⁴ | 3.Ch 10 | V3, V6 | `T`, `j` |
| `τ` | Proper time or lifetime (context) | s | 5.Ch 2 | V5, V6 | `t`, `τ_DM`, `τ_p` |
| `τ_couple` | Waters–Firmament coupling oscillation timescale | s; `~ 2ξ_A/c ~ 60 Gyr` | 5.Ch 11 | V5, V6 | `ξ_A`, `c` |
| `τ_DM, τ_p` | DM decay lifetime, proton lifetime | yr; zone architecture: `τ_DM = τ_p = ∞` | 5.Ch 11 | V5, V6 | `σ_DM-SM` |
| `υ` | (Not used — upsilon reserved.) | — | — | — | — |
| `φ, ϕ` | Scalar field or angle (context) | Dimensionless or radians | 1.Ch 6 | V1–V4 | `Ψ_A, Ψ_B` |
| `Φ` | Gravitational potential or flux (context) | m²/s² or V·m | 3.Ch 3 | V3, V5 | `g` (grav), `E` |
| `χ` | Susceptibility or Holevo capacity (context) | Dimensionless | 4.Ch 14 | V4, V6 | `S/N` |
| `ψ` | Wave function (generic) | Per √m³ (nonrelativistic QM) | 4.Ch 1 | V4 | `Ψ_A, Ψ_B` |
| `Ψ_A` | Waters Above field (dark energy) | Field amplitude (dimension depends on normalization) | 1.Ch 6 | V1, V5, V6 | `ρ_A`, `Ω_Λ`, `w` |
| `Ψ_B` | Waters Below field (dark matter) | Field amplitude | 1.Ch 6 | V1, V5, V6 | `ρ_B`, `Ω_DM`, `w` |
| `ω` | Angular frequency | rad/s | 1.Ch 5 | All vols | `f`, `k` |
| `ω_cut` | Dimensional-bypass spectrum cutoff frequency | rad/s; `ω_cut = c/η_B` | 6.Ch 9 | V6 | `η_B` |
| `Ω_b` | Baryonic matter density parameter | 0.049 (4.9%) | 5.Ch 8 | V5, V6 | `ρ_matter`, `ρ_critical` (cosmological) |
| `Ω_DM` | Dark-matter density parameter | 0.266 (26.6%) | 5.Ch 8 | V5, V6 | `ρ_B`, `Ψ_B` |
| `Ω_Λ` | Dark-energy density parameter | 0.684 (68.4%) | 5.Ch 8 | V5, V6 | `ρ_A`, `Ψ_A`, `Λ` |
| `Ω_r` | Radiation density parameter | ~9.2 × 10⁻⁵ | 5.Ch 8 | V5, V6 | — |
| `Ω_total` | Total density parameter | `= 1` (spatial flatness) | 5.Ch 8 | V5, V6 | `Ω_Λ + Ω_DM + Ω_b + Ω_r` |

---

## E.4  Mathematical Operators and Relations

Operators are in order of frequency of appearance across the series. The table below includes only operators whose usage in Genesis Physics requires clarification beyond the ordinary mathematical-physics meaning; universally standard symbols (`=`, `+`, `−`, `×`, `/`, `∑`, `∫`) are omitted.

| Symbol | Name | Meaning in Genesis Physics | Used In |
|--------|------|-----------------------------|---------|
| `∂_μ` | Partial derivative with respect to coordinate `x^μ` | Standard; `μ ∈ {0,1,2,3}` on brane, `{0,1,2,3,4,5}` on 6D bulk | V1, V2, V4, V5 |
| `∇` | Spatial gradient (3-vector) or covariant derivative (context) | 3-vector gradient in classical contexts; full `∇_μ` (covariant) in GR contexts | V1–V6 |
| `∇_μ` | Covariant derivative | Uses Christoffel symbols of `g_μν` | V5 |
| `□` | D'Alembertian operator | `∂_μ∂^μ = (1/c²)∂²/∂t² − ∇²` on flat brane; `∇_μ∇^μ` on curved spacetime | V2, V4, V5 |
| `⊗` | Tensor product | Standard; used for state spaces in V4 and product manifolds in V1 | V1, V4 |
| `⊕` | Direct sum | Used for zone decompositions `Z = Z_Above ⊕ Z_Below ⊕ Firmament`-like splittings | V1, V4 |
| `≡` | Defined as / identically equal | Used for definitions (not equations that could fail) | All vols |
| `∝` | Proportional to | Hides a constant of proportionality; used for scaling laws | All vols |
| `~` | Approximately equal (order-of-magnitude) | Weaker than `≈`; used when the number is a scale estimate | All vols |
| `≈` | Approximately equal (numerical) | Used when the stated digits are the best available, not exact | All vols |
| `≲`, `≳` | Less than or of the order of / greater than or of the order of | Used for inequality bounds with order-of-magnitude uncertainty | V5, V6 |
| `|·|` | Absolute value or determinant (context) | Determinant when applied to a matrix (`|g|` for metric determinant) | V1, V5 |
| `〈·〉`, `〈A〉` | Expectation value | Standard QM expectation; also used for classical ensemble average in V3 | V3, V4 |
| `〈A|B〉` | Inner product (Dirac bra-ket) | QM inner product | V4 |
| `δ(x)` | Dirac delta distribution | Standard | V2, V4, V6 |
| `δ_ij` | Kronecker delta | Dimensionless; `= 1` if `i=j`, else `0` | V1, V4 |
| `ε_ijk, ε^{μνρσ}` | Levi-Civita symbol (3-index) or tensor (4-index) | Totally antisymmetric; `ε_{123} = +1`; in 6D, `ε^{μνρσξη}` is the fully antisymmetric 6-tensor | V1, V2, V5 |
| `Γ^λ_{μν}` | Christoffel symbol | Connection coefficients from `g_μν` | V5 |
| `[A, B]` | Commutator | `AB − BA` | V4 |
| `{A, B}` | Anticommutator, or Poisson bracket (context) | `AB + BA` or Hamiltonian mechanics bracket | V3, V4 |
| `d/dt` | Total time derivative | Used in dynamical equations | All vols |
| `D/Dτ` | Covariant derivative along worldline | Used in GR geodesic equation | V5 |
| `⟂, ∥` | Perpendicular, parallel | Mode decomposition (e.g., `h_⊥, h_∥`) | V5 |

---

## E.5  Tensor and Index Conventions

These conventions hold across the entire series. Any chapter deviating from them is in error.

**Index placement and summation.** Einstein summation is implicit: repeated indices, one up and one down, are summed over their range. Upper (contravariant) indices raise; lower (covariant) indices lower. For vectors: `V^μ` is contravariant, `V_μ` is covariant, `V_μ = g_μν V^ν`. Indices are raised and lowered *only* with the metric tensor `g_μν` (brane) or the 6D metric `g_MN` (bulk). In flat-space contexts, `η_μν` substitutes for `g_μν`.

**Index ranges.** Greek indices (`μ, ν, ρ, σ, ...`) range over spacetime on the 4D brane: `0, 1, 2, 3`, with `0 = ct` and `1, 2, 3 = x, y, z`. Capital-Latin indices (`M, N, P, Q, ...`) range over the full 6D bulk: `0, 1, 2, 3, 4, 5`, with `4 = ξ` and `5 = η`. Lower-Latin indices (`i, j, k, ...`) range over the spatial three-submanifold: `1, 2, 3`. Hatted indices (`μ̂, ν̂, ...`) denote tangent-frame (locally inertial) components rather than coordinate components.

**Metric signature.** The 4D brane uses signature `(+, −, −, −)`, so that proper time obeys `dτ² = g_μν dx^μ dx^ν` with the timelike coordinate carrying the positive sign. The 6D bulk extends this to `(+, −, −, −, −, −)` — one timelike and five spacelike directions. This is the convention fixed in Axiom 5 (equation 1.1.5) and the 6D embedding metric (equation 1.4.1). Any chapter using the opposite signature `(−, +, +, +)` is in error and must be corrected.

**Symmetry and antisymmetry.** Round brackets denote symmetrization: `T_(μν) = ½(T_μν + T_νμ)`. Square brackets denote antisymmetrization: `T_[μν] = ½(T_μν − T_νμ)`. Parentheses and brackets around indices obey the standard normalization factor of `1/n!` for `n` indices.

**Levi-Civita tensor.** In 4D, `ε^{μνρσ}` is the fully antisymmetric rank-4 tensor with `ε^{0123} = +1` in a right-handed coordinate system. In 6D, `ε^{MNPQRS}` is the rank-6 analog. The tensor densities differ from the symbols by factors of `√|g|`; the series uses *tensors* (normalized), and distinguishes them from the underlying Levi-Civita *symbols* only when ambiguity arises.

**Hodge duality.** Used extensively in V2 for electromagnetism (`★F = F̃` with `F̃_{μν} = ½ε_{μνρσ}F^{ρσ}`) and in V5 for brane-volume forms.

**Brane-bulk projections.** A quantity living in the 6D bulk is decomposed via the induced metric `h_μν = g_μν − n_μn_ν`, where `n^μ` is the unit normal to the brane. Projections onto the brane use `h^μ_ν`; projections into the bulk use `n^μ`.

---

## E.6  Unit and Prefix Conventions

The Foundations Series mixes three unit conventions, chosen per-volume for pedagogical clarity. Readers must watch volume headers for which convention is active.

| Volume | Convention | Values explicit? | When `ℏ = c = 1`? |
|--------|------------|-------------------|--------------------|
| V1 | SI with explicit `ℏ, c`, but many dimensionful results stated in natural units for brevity | Mostly explicit | No (some sidebar derivations switch) |
| V2 | SI throughout; no natural-units shortcuts | Always explicit | No |
| V3 | SI throughout; thermodynamics with `k_B` explicit | Always explicit | No |
| V4 | Natural units: `ℏ = c = 1`, sometimes `k_B = 1`; masses in GeV or MeV | Restored at chapter end | Yes |
| V5 | Mixed: GR uses geometric units `G = c = 1` in some sections; cosmology uses SI; Planck units explicit in derivations | Restored at major boundaries | Partial (section-dependent) |
| V6 | SI predominates because predictions are compared to observation in SI or experimental units; natural units only in V4-derived sections | Always explicit | No |

**Restoration rules.** When a natural-units expression is quoted back into SI, the restoration is done by matching dimensions: each factor of `ℏ` carries units of J·s, each factor of `c` carries m/s, each factor of `k_B` carries J/K. For particle-physics masses: `1 GeV = 1.783 × 10⁻²⁷ kg = 5.068 × 10¹⁵ m⁻¹` (via `ℏ/(Mc)`).

**Decimal prefixes.** SI prefixes are standard: k (10³), M (10⁶), G (10⁹), T (10¹²), P (10¹⁵), m (10⁻³), μ (10⁻⁶), n (10⁻⁹), p (10⁻¹²), f (10⁻¹⁵), a (10⁻¹⁸). When confusion between `M` (mega) and `M` (mass symbol) or between `T` (tera) and `T` (temperature) arises, the context is disambiguated by a spelled-out qualifier in a footnote (e.g., `M_W = 80 GeV`, where `M` is the mass symbol, not the mega prefix).

**Astronomical and particle-physics specialty units.** The series uses:
- **Light-year** (`ly`), **parsec** (`pc`), **megaparsec** (`Mpc`): cosmological distance
- **Solar mass** (`M_☉`), **solar luminosity** (`L_☉`): stellar and galactic scales
- **Electronvolt** (`eV`, `keV`, `MeV`, `GeV`, `TeV`): particle physics
- **Gauss** (`G`), **Tesla** (`T`): magnetic-field strength in E&M experimental contexts
- **Barn** (`b = 10⁻²⁸ m²`): scattering cross-section

**Planck units.** `ℓ_P = 1.616 × 10⁻³⁵ m`, `t_P = 5.39 × 10⁻⁴⁴ s`, `m_P = 2.18 × 10⁻⁸ kg`, `T_P = 1.417 × 10³² K`. All derive from `ℏ, c, G, k_B`.

---

## E.7  Zone-Architecture-Specific Notation

These symbols are unique to the Genesis Physics framework and do not have counterparts in standard physics. The Consistency Auditor watches this section most closely.

**Zone labels (nested system).** The authoritative technical notation for zones uses the nested hierarchy from `Quality_Control/Reference/Zone_Architecture.md`. The labels `Z_n` are integer-subscripted and composed with dots to indicate nested hierarchy.

| Label | Name | Dimensionality | First Appears |
|-------|------|-----------------|-----------------|
| `Z₀` | Godhead | Infinite | 1.Ch 1 |
| `Z₁` | Heaven Prime | Infinite (transcendent) | 1.Ch 1 |
| `Z₂` | Earth Prime | 4D manifold | 1.Ch 1 |
| `Z₂.₁` | Atemporal Domain | 4D+ | 1.Ch 1 |
| `Z₂.₂` | Firmament Domain | 3D + time | 1.Ch 5 |
| `Z₂.₂.₁` | Waters Below | 3D | 1.Ch 6 |
| `Z₂.₂.₂` | Condensed Matter (baryonic) | 3D | 1.Ch 6 |
| `Z₂.₂.₃` | Waters Above | 3D | 1.Ch 6 |

Simplified labels (`Zone 1` through `Zone 4`) are permitted only in Book 2 contexts with explicit parenthetical nested clarification; they do not appear in the Foundations Series except in cross-book pedagogical bridges.

**Membrane and fields.**

| Symbol | Meaning | Units | First Appears |
|--------|---------|-------|---------------|
| `𝓕` | Firmament (as scalar field) | Context-dependent | 1.Ch 5 |
| `K_ij` | Extrinsic curvature of Firmament hypersurface | m⁻¹ | 1.Ch 5 |
| `[K_ij]` | Israel junction-condition discontinuity | m⁻¹ | 1.Ch 5 |
| `Ψ_A` | Waters Above field | Field amplitude | 1.Ch 6 |
| `Ψ_B` | Waters Below field | Field amplitude | 1.Ch 6 |
| `σ, μ` | Membrane tension and density | See E.3 | 1.Ch 5 |

**Boundary scales.**

| Symbol | Meaning | Value | First Appears |
|--------|---------|-------|---------------|
| `ξ_A` | Waters Above extent | ~3 × 10²⁶ m | 1.Ch 6 |
| `η_B` | Waters Below extent | 1.3 × 10⁻¹⁵ m | 1.Ch 6 |
| `L_eff` | 6D-reduction coupling length | 8.96 × 10⁻²⁹ m | 1.Ch 4 |
| `η*` | Zone-tunneling excursion coordinate | Fraction of `η_B` | 6.Ch 11 |

**Sustaining-field notation.** The symbol `κ` with four subscripts denotes the four thermodynamic phases of the sustaining field:

- `κ_create` — Creation supercritical phase (Days 1–6; `κ >> κ_full`)
- `κ_full` — Edenic equilibrium (post-Sabbath baseline; zero net entropy production)
- `κ_partial` — Fall subcritical phase (present epoch; `κ = κ_full(1−ε)`)
- `κ_redeem` — Redemption recovery phase (future; entropy reversal)

The Four-Epochs notation cross-references `Quality_Control/Reference/Four_Epochs_Timeline.md` for timeline context. The numerical values of `ε` (the subcriticality parameter) span `~10⁻²⁷ to 10⁻⁶⁰` depending on the observable being measured.

**Genesis-day timeline locators.** The timeline notation `Day N` (1 ≤ N ≤ 7) refers to the Genesis creation-day sequence with the timings tabulated in `Zone_Architecture.md` Table 5. Physical timescales (Planck, GUT, QCD, BBN) are given in seconds alongside. These are pedagogical timeline markers, not ordinary time variables, and are set in roman type (not italic) to distinguish them from mathematical variables.

---

## E.8  Constants Reference

Complete table of physical constants used anywhere in the series, with the zone-architecture derivation context where available. Values are CODATA 2022 unless otherwise noted.

| Constant | Symbol | Value | Units | Zone-Architecture Source | First Appears |
|----------|--------|-------|-------|---------------------------|-----------------|
| Speed of light | `c` | 2.998 × 10⁸ | m/s | `√(σ/μ)` from membrane mechanics | 1.Ch 5 |
| Gravitational constant | `G` | 6.674 × 10⁻¹¹ | m³·kg⁻¹·s⁻² | `c⁴/(8πσ·L_eff²)` from 6D reduction | 2.Ch 9 |
| Planck constant | `h` | 6.626 × 10⁻³⁴ | J·s | Brane-boundary quantization | 4.Ch 1 |
| Reduced Planck constant | `ℏ` | 1.055 × 10⁻³⁴ | J·s | `h/(2π)` | 4.Ch 1 |
| Boltzmann constant | `k_B` | 1.381 × 10⁻²³ | J/K | Standard (not derived in series) | 1.Ch 11 |
| Elementary charge | `e` | 1.602 × 10⁻¹⁹ | C | Brane U(1) quantization | 2.Ch 6 |
| Fine-structure constant | `α` | 1/137.036 | — | `1/[1.44 × ln(ξ_A/η_B)]` | 5.Ch 13 |
| Strong coupling at `M_Z` | `α_s(M_Z)` | 0.118 | — | η-boundary confinement | 4.Ch 12 |
| EM/gravitational hierarchy | `α_em/α_G` | 1.24 × 10³⁶ | — | Log-vs-power derivation on `ℛ` | 2.Ch 9 |
| Vacuum permittivity | `ε_0` | 8.854 × 10⁻¹² | F/m | Membrane impedance factor | 2.Ch 3 |
| Vacuum permeability | `μ_0` | 1.257 × 10⁻⁶ | T·m/A | Paired with `ε_0`; `c² = 1/(ε_0 μ_0)` | 2.Ch 3 |
| Stefan-Boltzmann | `σ_SB` | 5.670 × 10⁻⁸ | W·m⁻²·K⁻⁴ | From Planck spectrum integration | 3.Ch 10 |
| Avogadro | `N_A` | 6.022 × 10²³ | mol⁻¹ | Chemistry-layer definition | 3.Ch 9 |
| Gas constant | `R_gas` | 8.314 | J·mol⁻¹·K⁻¹ | `N_A k_B` | 3.Ch 9 |
| Rydberg constant | `R_∞` | 1.097 × 10⁷ | m⁻¹ | `α²m_ec/(2h)` | 4.Ch 7 |
| Electron mass | `m_e` | 0.511 | MeV/c² | Currently open — see P-052, P-055 | 4.Ch 10 |
| Proton mass | `m_p` | 938.272 | MeV/c² | QCD confinement-scale derivation | 4.Ch 12 |
| Muon mass | `m_μ` | 105.658 | MeV/c² | See P-053 | 4.Ch 10 |
| Tau mass | `m_τ` | 1776.86 | MeV/c² | — | 4.Ch 10 |
| W mass | `M_W` | 80.377 | GeV/c² | `gv/2` from SU(2) × U(1) breaking | 4.Ch 11 |
| Z mass | `M_Z` | 91.188 | GeV/c² | From `M_W`, `θ_W` | 4.Ch 11 |
| Higgs mass | `m_H` | 125.10 | GeV/c² | Electroweak fit | 4.Ch 11 |
| Electroweak VEV | `v` | 246 | GeV | Higgs minimum | 4.Ch 11 |
| Weak mixing angle | `sin²θ_W` | 0.23122 | — | Running coupling geometry | 4.Ch 11 |
| Cosmological constant | `Λ` | 1.1 × 10⁻⁵² | m⁻² | Waters Above repulsive density | 5.Ch 11 |
| Dark-energy density | `ρ_A` | 5.8 × 10⁻²⁷ | kg/m³ | `Ψ_A` confinement | 5.Ch 11 |
| Dark-matter density | `ρ_B` | 2.3 × 10⁻²⁷ | kg/m³ | `Ψ_B` matter-like scaling | 5.Ch 11 |
| Baryonic density | `ρ_matter` | 4.2 × 10⁻²⁸ | kg/m³ | `Z₂.₂.₂` condensed matter | 5.Ch 8 |
| QCD critical density | `ρ_critical` | 2.3 × 10¹⁷ | kg/m³ | QCD phase transition | 4.Ch 12 |
| Hubble constant (present) | `H₀` | 67.4 | km/s/Mpc | FRW fit (Planck value) | 5.Ch 8 |
| Age of universe | `t_0` | 13.787 | Gyr | FRW integration | 5.Ch 8 |
| Planck length | `ℓ_P` | 1.616 × 10⁻³⁵ | m | `√(ℏG/c³)` | 4.Ch 9 |
| Planck time | `t_P` | 5.39 × 10⁻⁴⁴ | s | `ℓ_P/c` | 4.Ch 9 |
| Planck mass | `m_P` | 2.18 × 10⁻⁸ | kg | `√(ℏc/G)` | 4.Ch 9 |
| Planck temperature | `T_P` | 1.417 × 10³² | K | `m_Pc²/k_B` | 4.Ch 9 |
| Membrane tension | `σ` | 6.0 × 10⁹⁸ | kg·m⁻¹·s⁻² | Fundamental creation parameter | 1.Ch 5 |
| Membrane density | `μ` | 6.7 × 10⁸¹ | kg/m³ | Fundamental creation parameter | 1.Ch 5 |
| 6D coupling length | `L_eff` | 8.96 × 10⁻²⁹ | m | 6D → 4D reduction | 1.Ch 4 |
| Waters Above extent | `ξ_A` | ~3 × 10²⁶ | m | Hubble-scale boundary | 1.Ch 6 |
| Waters Below extent | `η_B` | ~1.3 × 10⁻¹⁵ | m | QCD-scale boundary | 1.Ch 6 |

Derivations of the constants marked "zone-architecture source" are given in full in Vol 5 Appendix C (Derivations of Fundamental Constants) and Vol 2's coupling-constant chapters. Constants with "Standard (not derived in series)" are taken as empirical inputs — they are known but not derived from deeper zone-architecture principles within the current framework. Their derivation is among the open problems of Chapter 14.

---

## E.9  Prediction Identifier Scheme

Every testable prediction in Vol 6 carries a permanent identifier of the form `P-XXX` (three-digit zero-padded). The scheme is:

**Assignment rule.** Once an identifier is assigned in a chapter draft, it is bound to that prediction for the life of the series. Identifiers never migrate; they never get reused. If a prediction is superseded, the superseding prediction receives a new identifier and the old row in Appendix A is annotated as "superseded by P-YYY" rather than deleted. This rule protects citation stability across editions.

**Categorical labels (master-table canonical).** The 153 predictions are partitioned across fourteen category labels, chosen to reflect the *physical subject* of each prediction rather than its source chapter. The labels are taken verbatim from the Category column of the Appendix A §A.13 master table; any accounting discrepancy between this section and §A.13 is resolved in favor of §A.13.

| Category label | Count | Representative IDs | Physical subject |
|-----------------|-------|---------------------|-------------------|
| Structural | 7 | P-031, P-032, P-033, P-034, P-050, P-051, P-081 | Conservation laws, zone topology, aufbau, bonding |
| Couplings | 7 | P-004, P-005, P-006, P-056, P-057, P-058, P-065 | α, α_s, α_em/α_G, sin²θ_W, α-constancy |
| Particle | 21 | P-014–P-023, P-052–P-055, P-066, P-067, P-071, P-072, P-074, P-075, P-080 | W/Z/Higgs, leptons, quarks, neutrinos, CKM, jets |
| GR | 14 | P-007–P-013, P-059, P-060, P-068–P-070, P-100, P-101 | Classical GR tests, GW, KK modes, brane c |
| Cosmology | 17 | P-024–P-030, P-061–P-064, P-073, P-076–P-079, P-082 | DE/DM, H₀, age, Ω's, Λ, rotation curves, Waters power spectrum |
| QM | 4 | P-046, P-047, P-048, P-049 | Photoelectric, Compton, BEC, Casimir |
| EM | 6 | P-040–P-045 | Maxwell, c-from-metric, charge quantization, EM spectrum, BCS T_c, Meissner |
| QED/EM | 3 | P-001, P-002, P-003 | a_e, Lamb shift, a_μ |
| Thermo | 3 | P-037, P-038, P-039 | Second law, Planck spectrum, Stefan-Boltzmann |
| Classical | 2 | P-035, P-036 | F=ma, Kepler |
| Tech-FTL | 14 | P-083, P-084, P-089–P-099, P-102 | Warp bubble, dimensional bypass, zone tunneling |
| Tech-NRG | 18 | P-085, P-086, P-103–P-118 | MRG, Casimir arrays, expansion sail, latent heat |
| Tech-COM | 19 | P-087, P-088, P-119–P-135 | Zone-tunneling / Waters-field / consciousness channels |
| Tech-SNS | 18 | P-136–P-153 | MVI, atom-interferometer Waters sensor, DM aperture, life detection, LIGO retrofits, PTA |
| **Total** | **153** | — | — |

The sum (7+7+21+14+17+4+6+3+3+2+14+18+19+18 = 153) matches the master-table row count exactly. The coarser ten-category grouping used in Appendix A §A.3 through §A.12 (which merges Classical + QM + EM + QED/EM + Thermo into "QED and Electromagnetism" and related coarse buckets) is pedagogical; for any indexing or statistical claim the fourteen-label master-table scheme above is authoritative.

**Technology identifier scheme.** The `T-XXX-NN` scheme is the parallel identifier family for technology concepts introduced in Ch 9–12 and Ch 16, with `XXX ∈ {FTL, NRG, COM, SNS}` and `NN` a two-digit sequential number within that sub-family. These are consumed by Appendix F; the full list is:

- **T-FTL-01** Temporal Shortcut
- **T-FTL-02** Dimensional Bypass
- **T-FTL-03** Zone Tunneling
- **T-FTL-04** Field Distortion / Warp Bubble
- **T-FTL-05** Consciousness Interface
- **T-NRG-01** Membrane Resonance Generator (MRG)
- **T-NRG-02** Waters Above Expansion Sail
- **T-NRG-03** Dynamic Casimir Array
- **T-NRG-04** Zone-Boundary Latent-Heat Extraction
- **T-COM-01** Entanglement-Based Signaling (null per P-132)
- **T-COM-02** Zone-Tunneling Channel
- **T-COM-03** Waters-Field Modulation Channel
- **T-COM-04** Consciousness-Interface Channel
- **T-SNS-01** Membrane Vibration Interferometer (MVI)
- **T-SNS-02** Atom-Interferometer Waters-Field Sensor
- **T-SNS-03** Dark-Matter Imaging Aperture
- **T-SNS-04** LIGO Retrofit for Extended GW Polarizations
- **T-SNS-05** Life-Detection-from-Space Gravimeter
- **T-SNS-06** Zone-Boundary Anomaly Cosmology Cross-Correlator

Like P-XXX, T-XXX identifiers are permanent; a retired technology gets an annotation, never a renumbering.

---

## E.10  Deprecated / Superseded Symbols

Early drafts of the series used a handful of symbols that were later replaced with clearer or more standard notation. These are recorded here so that archive readers can map a draft citation to the current notation. No symbol in this section is currently correct — each row is a historical pointer.

| Deprecated Symbol | Early Meaning | Replaced By | Reason |
|---------------------|-----------------|---------------|---------|
| `Φ_0` (early Vol 1 drafts) | Firmament field amplitude | `𝓕` | Conflict with magnetic-flux convention (`Φ_B`) in V2 |
| `M_mem` | Membrane mass parameter | `μ` (density) plus explicit volume | Ambiguity between mass and mass density |
| `τ_cr` | Creation-phase timescale | `κ_create` (as a phase label, not timescale) | Early drafts conflated a timescale with a phase regime |
| `ζ_A, ζ_B` | Waters Above/Below extents | `ξ_A, η_B` | Ambiguity with Riemann zeta; the current Latin letters preserve `ξ = Above`, `η = Below` |
| `ℳ` (calligraphic M) | Generic zone manifold | `M` (capital Latin) in V1 notation; `Z_n` labels for specific zones | Visually indistinguishable from `𝓜_P` (Planck mass) in some typefaces |
| `Ψ_WA, Ψ_WB` | Waters Above/Below fields (verbose subscript) | `Ψ_A, Ψ_B` | Brevity; `W` redundant because the Ψ letter already signals "Waters" |
| `α_ZA` | Zone-architecture derived α | `α` (the single symbol; zone-derivation implicit) | Simpler notation; the derivation context is clear from the volume |
| `P-0XX` (leading zero one-digit) | Early prediction IDs before three-digit standard | `P-0XX` → `P-0XX` (padded consistently to three digits throughout) | Unified three-digit format |
| `T-ENG-NN` | Technology identifiers (early drafts) | `T-NRG-NN` (energy sub-family) | "ENG" conflated "engineering" and "energy"; `NRG` is unambiguous |
| `Zone-2a, Zone-2b` | Pre-nested-notation Firmament sublabels | `Z₂.₂.₁, Z₂.₂.₂, Z₂.₂.₃` | Nested notation made the hierarchy explicit |
| `κ_0` (in some Vol 1 drafts) | Sustaining baseline | `κ_full` | Avoids ambiguity with index-zero components; `κ_full` is semantically explicit |
| `𝒦` (script K) | Collective sustaining field | `κ` (single symbol with subscripts) | Single-letter notation matches standard convention |

Readers encountering any symbol in this table in older drafts, internal working documents, or pre-2026 GitHub discussions should translate to the Replaced-By column. The Consistency Auditor flags these automatically on audit runs.

---

*Appendix E is the arbiter. Changes to the notation conventions here cascade through every volume; the Consistency Auditor runs on every Appendix E edit. If a chapter in any volume uses a symbol not documented here, the discrepancy is a bug — either the chapter is wrong, or Appendix E is incomplete. Raise it through the audit workflow, not by private edit.*

*Last audit against series chapters: 2026-04-20. Next audit is triggered by any Appendix E update, any new chapter draft-complete event in any volume, or the quarterly consistency review — whichever comes first.*
