# Derivation Provenance Ledger — Genesis Physics

**Purpose.** Operationalizes the Governing Provenance Principle (`00_SERIES_VISION.md`): *everything must derive from the framework's axioms and the Bible.* Every canonical result is traced **Scripture → axiom → derivation chain → result**, with each result's status marked. Built 2026-06-11 from a full read-only audit of `Research/` against `CANONICAL_FACTS_REGISTRY.md` and `Biblical_References.md`. Status of any disputed item is governed by the registry (★ Author Ratification #1).

**Status legend**
- **AXIOM** — an irreducible foundational input (adopted, not derived). The permitted ground floor.
- **DERIVED** — a complete chain to the axioms exists in a cited Research file.
- **DERIVED-given-AXIOM** — follows rigorously *given* an adopted axiom (e.g. Postulate F); the axiom dependency is stated, not hidden.
- **FIT (#)** — rests on a fitted/calibrated coefficient or a bare measured input **not** derived from an axiom. By the Provenance Principle this is an **open problem**, tracked as the named board issue.

**The frontier (open FIT items, on the board):** #846 two-loop α→137.036 · #847 absolute mass scale / Higgs vev · #848 precise CKM/PMNS angles · #849 derive n_w=3 from Z₀ · #850 derive Yukawa α.

---

## 0. The top of every chain — axioms ↔ Scripture

| Axiom | One-line statement | Biblical anchor (as cited in the axiom file) | Status |
|---|---|---|---|
| **Λ_Z0 — Godhead-zone constant** | Vacuum energy of the deepest zone Z₀; the single ground-floor parameter from which ℏ, α, … flow. | **Gen 1:1; John 1:1–3** — Z₀ = the Godhead / the uncaused ground; John 1:3 = the provenance principle in Scripture (`AXIOM_GODHEAD_ZONE_Z0.md` §0) | **AXIOM** (irreducible; **biblically grounded**) |
| **Postulate F — winding n_q=3** | Waters-Above vortex sector carries quotient winding 3 → Kähler spinors (spin-½) + twisted index +3 (three generations; **computed**, #851 fixed). | **CONSONANT, LOCATED, NOT DERIVED** (2026-06-13 scriptural derivation + Theologian referee, `Peer_Review/849_scriptural_derivation/`): the (ξ,η) fiber = the Waters of Gen 1:6-7, which the text divides **binarily** (two waters, one firmament — not three); the integer 3 is **not** read off the page. But it has a genuine scriptural **home** — the Day-2 dividing of the waters (Gen 1:6-8) — where it is adopted as a freely-decreed creation parameter, conserved by superselection. Six physics derivations (incl. the Z₃+energetics race + coordinate/spectral race, `Peer_Review/`) prove physics cannot force it either. | **AXIOM** (adopted creation parameter; consonant+located, not derived) → deeper derivation open **#849** |
| **Open System** | Universe is thermodynamically open — created, sustained, acted upon (δE_ext ≠ 0). | **Col 1:17; Heb 1:3** (also John 1:3) | **AXIOM** (adopted, biblically motivated) |
| **6D Spacetime** | Universe is a 6D manifold (t,x,y,z,ξ,η); the 4D world is the Firmament membrane. | **Gen 1:1** | **AXIOM** (adopted) |
| **Waters Duality** | Dark energy = Waters Above (Ψ_A, ξ); dark matter = Waters Below (Ψ_B, η). | **Gen 1:6-7** | **AXIOM** (adopted) |
| **Membrane / Firmament Mechanics** | c² = σ/μ; constants derive from membrane geometry. | **Gen 1:6** (rāqîaʿ) | DERIVED-from 6D Spacetime |
| **Sustaining Coupling κ** | Scalar power-density field encoding active maintenance; drives the four epochs. | **Heb 1:3; Neh 9:6** | DERIVED-from Open System |
| **Metric Discontinuity / Sabbath Boundary** | First-order metric transition; locks constants; 6 days ↔ 13.8 Gyr coordinate time. | **Gen 2:1-3; Exod 20:11** | DERIVED-from 6D Spacetime |
| **Phase Transition / The Fall** | Thermodynamic transition κ_full→κ_partial; arrow of time turns on. | **Gen 3; Rom 8:20-22** | DERIVED-from Sustaining Coupling |

> **Ground-floor status (updated 2026-06-11).** **Λ_Z0 is now biblically grounded** — Z₀ = the Godhead, the uncaused ground (Gen 1:1; John 1:1–3, with John 1:3 = the provenance principle in Scripture; `AXIOM_GODHEAD_ZONE_Z0.md` §0). That Λ_Z0 has no *physics* derivation is the thesis, not a gap: the chain bottoms out at the Creator. **The one remaining ground-floor open item is n_w=3** (Postulate F): a hypothesis test (#849) found **no mechanism** linking the triune God (or any three-fold Z₀ structure) to the winding number — verdict **OPEN**, the Trinity↔3 link is a **resonance, not a derivation** (the framework's color-Z₃ and generation-n_w are independent 3's). Deriving n_w=3 — or formally accepting it as the framework's single topological axiom — is the deepest frontier (#849).

---

## 1. Fundamental constants

| Result | Value | Verse | Axiom(s) | Chain (file) | Provenance |
|---|---|---|---|---|---|
| Λ_Z0 | 1.65×10⁷¹ GeV⁶ (at M_Z0=M_Pl) | Gen 1:1 (thematic) | Λ_Z0 | irreducible (`op01_z0_axiom_statement.md`) | **AXIOM** |
| ℏ | 1.0546×10⁻³⁴ J·s | Gen 1:1 | Λ_Z0, 6D, Membrane | Λ_Z0→k₁=1.22 MeV→L_A=83.2η_B→β_geom=813→ℏ (`AXIOM_GODHEAD_ZONE_Z0.md` §2) | **DERIVED-given-AXIOM** (β_geom numerical refinement open) |
| c | 2.998×10⁸ m/s | Gen 1:6-8 | Membrane | c²=σ/μ; σ traces to Λ_Z0 (`AXIOM_MEMBRANE_MECHANICS_v2.md`) | **DERIVED** |
| α⁻¹ (fine structure) | one-loop 137.17 (0.095%) | Gen 1:1 | Λ_Z0, 6D, Sustaining | α⁻¹=C·ln(ξ_A/η_B); UV boundary from Λ_Z0 (`10-FINE_STRUCTURE_DERIVATION.md`) | **FIT (#846)** — C=1.4383 fitted to hit 137.036 |
| G / G₄ | 6.674×10⁻¹¹ | Gen 1:1; Col 1:17 | 6D, Sustaining | G₄=G₆/V_extra via KK reduction (`10-GRAVITATIONAL_CONSTANT_DERIVATION.md`) | **FIT (#847)** — G₆/M₆ back-solved; mechanism sound |
| k_B | 1.380649×10⁻²³ (exact) | — | (unit definition) | conversion factor K↔J (`10-BOLTZMANN_CONSTANT_DERIVATION.md`) | **AXIOM** (conventional unit, honest non-derivation) |

## 2. Particles / Standard Model

| Result | Status | Verse | Axiom(s) | Chain (file) | Provenance |
|---|---|---|---|---|---|
| Spin-½ existence | resolved given Postulate F | Gen 1:1 | Λ_Z0 + Postulate F | n_w=3→Kähler→4D spin-½ (`AXIOM_GODHEAD_ZONE_Z0.md` §4) | **DERIVED-given-AXIOM** (#849) |
| Three-generation count | **computed** given Postulate F (#851 fixed 2026-06-11) | Gen 1:1 | Postulate F | twisted index: c₁=n_w + Jackiw–Rossi modes, numerically verified + adversarially checked (`op02_aps_index_computation.py` v2) | **DERIVED-given-AXIOM** (#849) |
| Charge quantization | win | Gen 1:1 | 6D, Postulate F | Q=n_Y/2 from U(1)_Y winding | **DERIVED** |
| Electron mass | +17% residual | — | Λ_Z0 + Postulate F | y_e overlap integral (`06-PARTICLE_MASS_SPECTRUM_V3.md` §4.2) | **DERIVED-given-AXIOM**, FIT residual (#847) |
| Muon mass | −15…19% | — | Λ_Z0 + Postulate F | y_μ=y_0e^(−4α) | **DERIVED-given-AXIOM**, FIT (α #850) |
| Tau mass | calibration anchor | — | Λ_Z0 + Postulate F | tau fixes the hierarchy (definitional) | **FIT** (calibration input #847) |
| Light quarks (u,d,s) | ~2–7% | — | Λ_Z0 + Postulate F | overlap + QCD running | **DERIVED-given-AXIOM**, scheme-FIT |
| Heavy quarks (c,t,b) | fail badly at tree level | — | Λ_Z0 + Postulate F | exp-hierarchy (registry §F supersedes V3 "<1%") | **FIT (#847/#850)** |
| Proton mass | −0.02% | Gen 1:1 | 6D | m_p=2m_u+m_d+E_QCD (`06-QCD_DERIVATION.md`) | **DERIVED** (QCD binding dominates) |
| Neutron / n−p split | ~4% | — | 6D | Δm=m_d−m_u+ΔE (`V3` §5.5) | **DERIVED**, approximate |
| Higgs vev v / m_H | v=246.22; m_H 125.1 | Gen 1:6-7 | Waters Duality | λ=0.129 back-solved from measured m_H (`06-HIGGS_DERIVATION.md`) | **FIT** — v, λ from measured M_W, G_F, m_H |
| M_W / M_Z | 80.27 / 91.55 | Gen 1:6-7 | Waters Duality | M_W=gv/2; M_Z=M_W/cosθ_W | **DERIVED** (given fitted v) |
| Yukawa hierarchy α | fitted ~1.0 (computed 0.076) | — | Λ_Z0 + Postulate F | y_n=y_0e^(−αn²) (`V3` §3.5, OP-03) | **FIT (#850)** |
| CKM mixing angles | Cabibbo approx; rest OPEN | Gen 1:6 | Firmament Mech. | unitarity derived; angles not (`06-WEAK_PARITY_CP_VIOLATION.md`) | **FIT/OPEN (#848)** |
| CP violation | existence rigorous; δ_CP=π/3 fitted | Gen 1:6 | Firmament + Postulate F | ξ≠η asymmetry → complex phases | **DERIVED (existence) / FIT (value)** |
| Neutrino masses/mixing | smallness qualitative win; abs scale OPEN | Gen 1:1 | 6D | boundary-mode suppression (`06-NEUTRINO_PHYSICS.md`) | **FIT/OPEN (#847/#848)** |
| Electroweak V−A / parity | A=−1 derived from boundary asymmetry | Gen 1:6 | Firmament Mech. | no ξ<0 mirror → W couples LH only | **DERIVED-given-AXIOM** (see flag) |

## 3. The four forces

| Result | Status | Verse | Axiom(s) | Chain (file) | Provenance |
|---|---|---|---|---|---|
| Maxwell's equations | from membrane geometry | Gen 1:6 | 6D, Firmament | off-diag metric → KK → 4D EM action (`03-MAXWELL_DERIVATION.md`) | **DERIVED** |
| Einstein field equations | from 6D metric | Gen 1:1; Col 1:17 | 6D, Sustaining | 6D Einstein-Hilbert → KK → 4D EFE (`KK_DIMENSIONAL_REDUCTION.md`) | **DERIVED** |
| SU(3)_C + 8 gluons | from Z₃ orbifold | Gen 1:6 | 6D | Z₃ winding → 3 colors (`RT2_SU3_Z3_ORBIFOLD.md`) | **DERIVED** |
| QCD confinement | mechanism derived; Λ_QCD ~30% | Gen 1:6 | 6D, Firmament | boundary impenetrability; Λ_QCD≈ℏc/η_B | **FIT** (Λ_QCD calibrated to η_B) |
| SU(2)_L + W/Z | from η-isometries | Gen 1:6 | 6D, Firmament | isometry → gauge group (`06-WEAK_PARITY_CP_VIOLATION.md`) | **DERIVED** (masses use fitted v) |
| Four forces from four sectors | one 6D metric → SU(3)×SU(2)×U(1)+gravity | Gen 1:6-7; Col 1:17 | 6D | metric component split (`10-COUPLING_CONSTANTS_DERIVATION.md`) | **DERIVED** (picture; values fitted) |
| Gauge coupling values (α_s, α_w, sin²θ_W) | measured/tuned inputs | Gen 1:6 | 6D, Firmament | SM β-coefficients imported; sin²θ_W needs tuned λ | **FIT** |
| Hierarchy (gravity weakness) | G₄=G₆/V_extra | Col 1:17; Gen 1:6 | 6D, Firmament | flux dilution in large extra dims | **FIT (#847-adjacent)** — number calibrated |
| Warp index | A_ξ=(2/3)ln(ξ₀/ξ) | Gen 1:6 | 6D | solves 6D Einstein eq (`WARP_FUNCTION_DERIVATION_RT1WF.md`) | **DERIVED** (RATIFIED ★#3; KK λ≈0.05 & gravity λ=41 superseded) |

## 4. Cosmology / dark sector

| Result | Status | Verse | Axiom(s) | Chain (file) | Provenance |
|---|---|---|---|---|---|
| Dark energy ≡ Waters Above | Ω_Λ=0.684 | Gen 1:6-7 | Waters Duality | Ψ_A excitation of ξ (`AXIOM_WATERS_DUALITY.md`) | **AXIOM** (identity) |
| Dark matter ≡ Waters Below | Ω_DM=0.266 | Gen 1:6-7 | Waters Duality | Ψ_B excitation of η, w≈0 | **AXIOM** (identity) |
| w_A = −1 | DE equation of state | Gen 1:6-7 | Waters Duality | V_A=const → P=−ρ (`08-FRIEDMANN_EVOLUTION.md`) | **DERIVED** |
| 68/27/5 budget | Planck 2018 | Gen 1:6-7 | Waters Duality, 6D | zone extents + warp (`ENERGY_FRACTIONS_DERIVATION.md`) | **DERIVED** ordering; **FIT** exact values |
| Cosmological constant ρ_eff | 2.93×10⁻⁴⁷ GeV⁴ (~20%) | Gen 1:6-7 | Waters Duality | Λ_zone⁴ suppressed by (η_B/ξ_A)^n, n=1 (`N1_DERIVATION_CT4L_OPEN_WATERS.md`) | **FIT** — n=1 exponent derivation pending |
| Sabbath Boundary | metric transition; constants lock | Gen 2:1-3; Exod 20:11 | Metric Discontinuity | junction conditions (`AXIOM_METRIC_DISCONTINUITY.md`) | **AXIOM** |
| The Fall | arrow of time turns on | Gen 3; Rom 8:20-22 | Phase Transition | κ_full→κ_partial (`AXIOM_PHASE_TRANSITION_FALL.md`) | **AXIOM** |
| Starlight / age | 6 days ↔ 13.8 Gyr coord. time | Gen 1 + Gen 2:1-3 | Metric Discontinuity | Sabbath-boundary time mapping | **DERIVED-given-AXIOM** |
| CMB peaks / T₀ | ℓ₁≈220; T₀=2.725 K | Gen 1:6-7 | Waters Duality | 6D acoustic oscillations (`08-CMB_POWER_SPECTRUM.md`) | **DERIVED** (n_s slow-roll FIT) |
| H₀ = 67.4 | + Hubble-tension prediction | — | 6D, Metric Disc. | Friedmann with derived G₄, Ω (`08-FRIEDMANN_EVOLUTION.md`) | **DERIVED** (ΔH₀ magnitude FIT) |

## 5. Classical mechanics / thermodynamics / quantum mechanics

| Result | Status | Verse | Axiom(s) | Chain (file) | Provenance |
|---|---|---|---|---|---|
| F=ma, Newton 1/2/3 | from 6D action | — | 6D, Firmament | worldline action → Euler-Lagrange (`01-COMPLETIONS.md`) | **DERIVED** |
| Lagrangian/Hamiltonian mech. | — | — | 6D, Firmament | non-rel limit + Legendre | **DERIVED** |
| Conservation laws (E, p, L) | Noether on zone symmetries | Mal 3:6 (immutability) | Open System, 6D | Noether (`01-EXPLICIT_DERIVATIONS.md`) | **DERIVED** |
| Kepler's laws / tides / collisions | — | — | 6D, Firmament | KK Newtonian limit | **DERIVED** |
| Open-system axiom | universe open to Creator | Col 1:17; Heb 1:3 | Open System | foundational (`AXIOM_OPEN_SYSTEM.md`) | **AXIOM** |
| Sustaining field κ | active maintenance | Heb 1:3; Neh 9:6 | Sustaining Coupling | foundational (`AXIOM_SUSTAINING_COUPLING.md`) | **AXIOM** |
| Laws 0–3 of thermo | from microstate counting | (2nd law: Rom 8:20-22) | 6D, Fall | S=k_B lnΩ; arrow of time from the Fall (`02-LAWS_DERIVATION.md`) | **DERIVED** |
| Entropy-production rate | dS/dt ∝ Δκ | Rom 8:22 | Sustaining, Fall | linear response | **FIT** (conductance/ε estimated) |
| Planck / Stefan-Boltzmann / Wien | exact matches | Gen 1:14-19 | 6D, Firmament | mode quantization + Bose stats (`02-PLANCK_SPECTRUM_DERIVATION.md`) | **DERIVED** |
| Schrödinger eq. | from membrane dynamics | John 1:1 | 6D, Firmament | carrier/envelope non-rel limit (`05-QM_FROM_MEMBRANE_DYNAMICS.md`) | **DERIVED** (modulo ℏ) |
| Uncertainty / de Broglie / L quant. | — | John 1:1 | 6D, Firmament | Fourier theorem; winding | **DERIVED** |
| Hydrogen levels | E_n=−13.6/n² eV | John 1:1 | 6D, Firmament | KK Coulomb + Bohr-Sommerfeld | **DERIVED** |
| Measurement / decoherence | pointer basis, τ_D | John 1:1 | 6D, Firmament | environment trace-out (`op09_collapse_resolution.md`) | **DERIVED** (scope-limited) |
| Born rule \|c\|² | — | John 1:1 | 6D, Firmament | energy-transfer argument heuristic | **FIT/OPEN** (explicitly unresolved) |
| g−2 / Lamb shift | <10⁻¹¹ / 0.005% | Ps 148:1 | 6D, Firmament, Open | QED loops as membrane-mode sums | **FIT (#846)** — conditional on measured α |
| ℏ (membrane derivation) | parametric | John 1:1 | 6D, Firmament | matches only if ξ₀≈60 ℓ_Pl (pending κ₆²) | **FIT** (parametric, OP-G6) |

---

## Summary — provenance at a glance
- **AXIOM (irreducible / adopted):** Λ_Z0, Postulate F (the two ground-floor inputs); Open System, 6D Spacetime, Waters Duality, Sabbath Boundary, the Fall (biblically anchored); dark-sector identities; k_B (unit convention).
- **DERIVED / DERIVED-given-AXIOM (chain to axioms exists):** ℏ, c, Maxwell, GR/EFE, SU(3)/SU(2) gauge groups, the four-forces picture, F=ma + all of classical mechanics, the conservation laws, the thermo laws + arrow of time, Planck/Stefan-Boltzmann/Wien, Schrödinger + uncertainty + hydrogen + decoherence, spin-½, three generations, charge quantization, M_W/M_Z, proton mass, w=−1, the energy-budget ordering, starlight/age, CMB peaks, H₀.
- **FIT — open by the Provenance Principle (board issues):** fine-structure precision **#846**; absolute mass scale / heavy quarks / Higgs vev **#847**; CKM/PMNS angles **#848**; derive n_w=3 from Z₀ **#849**; Yukawa α **#850**. Plus honest sub-fits: Λ_QCD scale, gauge-coupling values, n=1 CC exponent, entropy-rate coefficient, ΔH₀ magnitude, Born rule, ℏ-parametric (ξ₀).

## Honesty flags surfaced during the audit (for cleanup, not yet edited)
1. **Two irreducible axioms have no verse** — Λ_Z0 and Postulate F are structurally, not scripturally, anchored. This is the framework's thinnest point against its own "Genesis → physics" thesis. (#849 addresses n_w=3.)
2. **`06-NEUTRINO_PHYSICS.md` overclaims** — reports PMNS angles / Δm² as "EXACT MATCH," contradicting registry §F/§G ("qualitative win" / "OPEN"). Should be reconciled to the honest canon.
3. **V−A tension** — `06-WEAK_PARITY_CP_VIOLATION.md` derives V−A from boundary asymmetry but its own limitations summary still says "parity violation inserted by hand." The two statements should be reconciled.
4. **Heavy-quark "<1%"** — V3 body still shows c/t/b "<1% ✓" while its own footnote + registry say they fail at tree level. Body should match the footnote.
5. **Axiom-numbering inconsistency** — RESOLVED 2026-06-11. The `AXIOM_*.md` files previously disagreed with their own traceability matrices and with `Axiom_Summary_Cards.md` on index numbers (Open System was "Axiom 1" and "Axiom 4"; Sustaining was "Axiom 3" and "Axiom 5"). One canonical dependency-ordered numbering (0: Λ_Z0/Postulate F; 1: 6D Spacetime; 2: Waters Duality; 3: Membrane/Firmament; 4: Open System; 5: Sustaining Coupling; 6: Metric Discontinuity/Sabbath; 7: Phase Transition/Fall) is now recorded at the top of `Axiom_Summary_Cards.md` and applied to every `AXIOM_*.md` header, traceability matrix, and cross-reference (verses/statements unchanged).

*Verses are taken only from the axiom files and `Biblical_References.md`; no scriptural link or derivation was invented. Where a chain bottoms out in a fit or an adopted axiom, it is marked as such.*
