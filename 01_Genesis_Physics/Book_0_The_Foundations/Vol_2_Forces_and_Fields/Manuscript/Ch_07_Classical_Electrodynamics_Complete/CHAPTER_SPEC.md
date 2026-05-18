# Chapter Spec — Classical Electrodynamics Complete

**Book/Volume:** Foundations Vol 2: Forces and Fields
**Chapter Number:** Chapter 7
**Working Title:** Classical Electrodynamics Complete
**Status:** VERIFIED

---

## Mission

> This chapter delivers the full apparatus of classical electrodynamics — radiation, waveguides, optics, circuits, and boundary-value problems — derived entirely from the zone architecture Maxwell equations established in Chapter 3 and the formal Lagrangian/gauge machinery of Chapters 5–6, so the student sees that every result in Jackson traces back to the Firmament membrane.

---

## Requirements

| Req ID | Chapter Requirement | Traces To | Status |
|--------|-------------------|-----------|--------|
| Ch07-001 | Derive the electromagnetic wave equation in vacuum and in media from zone-architecture Maxwell equations (2.3.27–2.3.42) | V2-EM-COMPLETE | MET |
| Ch07-002 | Derive electromagnetic radiation from accelerating charges (Larmor formula, radiation fields, retarded potentials) | V2-EM-COMPLETE | MET |
| Ch07-003 | Derive EM boundary conditions at interfaces from zone Maxwell equations and solve reflection/refraction (Snell's law, Fresnel equations) | V2-EM-COMPLETE | MET |
| Ch07-004 | Derive guided-wave solutions: rectangular and cylindrical waveguides, TE/TM modes, cutoff frequencies | V2-EM-COMPLETE | MET |
| Ch07-005 | Derive circuit-element laws (Ohm, Kirchhoff, capacitance, inductance, RLC resonance) from Maxwell equations | V2-EM-COMPLETE | MET |
| Ch07-006 | Derive geometric and wave optics (Snell's law, total internal reflection, thin lens, diffraction, interference) from EM wave solutions | V2-EM-COMPLETE | MET |
| Ch07-007 | Derive Poynting's theorem and electromagnetic energy-momentum conservation from zone Lagrangian (2.5.1) | V2-LAGRANGIAN | MET |
| Ch07-008 | Derive electromagnetic potentials (scalar φ, vector A), gauge freedom, Coulomb and Lorenz gauges from zone-architecture gauge invariance (2.3.9) | V2-GAUGE | MET |
| Ch07-009 | Show every standard classical E&M result reduces from zone-architecture first principles — no postulated laws | V2-WHY | MET |
| Ch07-010 | Provide worked examples and problem sets spanning computational, conceptual, and challenge levels | V2-PROBLEMS | MET |
| Ch07-011 | Establish results that Vol 3 inherits: optics, wave mechanics, dispersion in media | V2→V3 | MET |

---

## Prerequisites

| Concept | Established In |
|---------|---------------|
| Zone manifold, 6D metric, embedding space | Vol 1, Ch 3–4 |
| Firmament as 4D membrane, induced metric γ_μν | Vol 1, Ch 5 |
| Speed of light c² = σ/μ (Firmament membrane wave speed) | Vol 1, Ch 5 (Eq. 1.5.36) |
| Waters field equations, scalar potentials | Vol 1, Ch 6 |
| Noether's theorem, conservation laws, U(1) charge conservation | Vol 1, Ch 7 |
| Five Principles as constraints | Vol 1, Ch 8 |
| All four Maxwell equations derived from 6D KK reduction | Vol 2, Ch 3 (Eqs. 2.3.27–2.3.42) |
| Gauge invariance as extra-dimensional coordinate freedom | Vol 2, Ch 3 (Eq. 2.3.9) |
| ε₀, μ₀, c, α derived from zone parameters | Vol 2, Ch 3 (Eqs. 2.3.29–2.3.82) |
| Field strength tensor F_μν, covariant Maxwell equations | Vol 2, Ch 3 (Eq. 2.3.10) |
| Poynting's theorem (initial form) | Vol 2, Ch 3 (Eqs. 2.3.94–2.3.98) |
| Complete zone Lagrangian with seven sectors | Vol 2, Ch 5 (Eq. 2.5.1) |
| U(1) gauge theory from ξ-direction isometry | Vol 2, Ch 6 (Eqs. 2.6.2–2.6.6) |
| Yang-Mills equations and gauge structure | Vol 2, Ch 6 (Eqs. 2.6.25–2.6.38) |

---

## "Why" Chain

1. **Why do electromagnetic waves radiate from accelerating charges?** — Because the Maxwell equations (derived from membrane geometry in Ch 3) couple field changes to source motion; acceleration creates propagating disturbances on the Firmament.
2. **Why does light bend at an interface?** — Because boundary conditions on E and B (forced by continuity of the Firmament membrane geometry across material discontinuities) require wavevector components to match, producing Snell's law.
3. **Why do waveguides have cutoff frequencies?** — Because the transverse boundary conditions on a finite cross-section quantize the allowed transverse wavenumbers, creating a minimum frequency for propagation — the same boundary-condition quantization mechanism from Vol 1, Ch 10.
4. **Why does Ohm's law work?** — Because the Drude model of electron transport in the zone-derived Coulomb field (from ε₀) yields a linear current-field relation under steady-state conditions.
5. **Why are there only two independent polarization states?** — Because the transversality condition (∇·E = 0 in vacuum, from Gauss's law derived in Ch 3) constrains the wave to 2 degrees of freedom on the 4D Firmament membrane.
6. **Why can we describe EM with potentials (φ, A) instead of fields?** — Because gauge invariance (which is extra-dimensional coordinate freedom, Ch 3 Eq. 2.3.9) means the physics lives in the gauge-invariant F_μν; the potentials are the more fundamental geometric objects.
7. **Why does EM energy flow as S = (1/μ₀) E × B?** — Because the Noether current for time-translation symmetry of the zone EM Lagrangian yields exactly Poynting's vector.
8. **Why do circuits obey Kirchhoff's laws?** — Because KCL is charge conservation (Noether current from U(1), Vol 1 Ch 7) and KVL is energy conservation (from the conservative nature of the electrostatic field derived in Ch 3).

---

## Key Deliverables

### Derivations (Foundations)

| # | Derivation | Starting Point | Result | Equations |
|---|-----------|---------------|--------|-----------|
| 1 | EM wave equation (vacuum) | Maxwell Eqs (2.3.27–2.3.42) | ∇²E = (1/c²)∂²E/∂t² | TBD |
| 2 | Plane wave solutions and dispersion | Wave equation | ω = c|k|, polarization, transversality | TBD |
| 3 | EM potentials and gauge choices | Gauge invariance (2.3.9) | φ, A; Coulomb and Lorenz gauges | TBD |
| 4 | Retarded potentials | Lorenz gauge + causality | Green's function solution for φ, A | TBD |
| 5 | Radiation from accelerating charge | Retarded potentials | Larmor formula P = q²a²/(6πε₀c³) | TBD |
| 6 | Poynting's theorem (full) | Zone Lagrangian (2.5.1) gauge sector | ∂u/∂t + ∇·S = −J·E | TBD |
| 7 | EM boundary conditions | Maxwell Eqs at interface | 4 conditions (E‖, D⊥, B⊥, H‖) | TBD |
| 8 | Reflection and refraction | Boundary conditions + plane waves | Snell's law, Fresnel equations | TBD |
| 9 | Total internal reflection | Snell's law + n₁ > n₂ | Critical angle θ_c = arcsin(n₂/n₁) | TBD |
| 10 | Rectangular waveguide modes | Maxwell Eqs + boundary conditions | TE_mn, TM_mn modes, cutoff ω_mn | TBD |
| 11 | Cylindrical waveguide (optical fiber) | Maxwell Eqs + cylindrical BCs | LP modes, V-number | TBD |
| 12 | Ohm's law from Drude model | Coulomb field (from ε₀) + electron transport | J = σE | TBD |
| 13 | Kirchhoff's laws | Charge conservation + energy conservation | KCL: ΣI = 0, KVL: ΣV = 0 | TBD |
| 14 | Capacitance | Gauss's law (from 2.3.27) | C = ε₀A/d | TBD |
| 15 | Inductance and Faraday's law | Faraday (from 2.3.42) + flux linkage | L = μ₀N²A/ℓ, EMF = −dΦ/dt | TBD |
| 16 | LC and RLC oscillations | Circuit Eqs from Maxwell | ω₀ = 1/√(LC), resonance, Q-factor | TBD |
| 17 | Thin lens equation | Snell's law + paraxial approximation | 1/f = (n−1)(1/R₁ − 1/R₂) | TBD |
| 18 | Interference and diffraction | EM wave superposition | Single-slit I(θ), double-slit fringes | TBD |
| 19 | EM waves in conducting media | Maxwell Eqs + J = σE | Skin depth δ = √(2/(ωμ₀σ)) | TBD |
| 20 | Faraday cage shielding | Boundary conditions + skin depth | SE ≈ 8.68 t/δ dB | TBD |

### Figures and Diagrams

| Fig ID | Title | Type | Placement | What It Shows | Why It's Needed | Key Labels | Complexity |
|--------|-------|------|-----------|---------------|----------------|------------|-----------|
| Fig 2.7.1 | Derivation Roadmap: From Zone Geometry to Classical E&M | Flowchart | §7.1, opening | Complete derivation chain from 6D metric → Maxwell → all classical E&M | Reader sees the logical architecture before diving into details | Axioms, Ch 3 results, Ch 5–6 machinery, this chapter's topics | Complex |
| Fig 2.7.2 | Electromagnetic Wave Propagation on the Firmament | Diagram | §7.2, after wave equation | Plane wave with E, B, k mutually perpendicular; membrane shown as propagation substrate | Spatial relationship of E, B, k fundamental to all that follows | E₀, B₀, k, c, λ, Firmament surface | Medium |
| Fig 2.7.3 | Polarization States | Diagram | §7.2, after polarization | Linear, circular, elliptical polarization; 2 DOF on membrane | Why exactly 2 polarizations — connects to Firmament geometry | ê₁, ê₂, k, Poincaré sphere | Medium |
| Fig 2.7.4 | Retarded Potential and Light Cone | Diagram | §7.3, after retarded potentials | Source at retarded time, field point, light cone connecting them | Causality in radiation — why retarded, not advanced | t_ret, r, J(t_ret), light cone | Medium |
| Fig 2.7.5 | Radiation Pattern from Accelerating Charge | Plot | §7.3, after Larmor formula | Dipole radiation pattern (sin²θ) with energy flow arrows | Power distribution in space — why radiation is anisotropic | P(θ), S, a, q | Medium |
| Fig 2.7.6 | EM Boundary Conditions at Interface | Cross-section | §7.4, opening | Two media with interface; pillbox and loop constructions | Visual proof method for 4 boundary conditions | E‖, D⊥, B⊥, H‖, n̂, ε₁, ε₂ | Medium |
| Fig 2.7.7 | Reflection, Refraction, and Total Internal Reflection | Diagram | §7.4, after Snell's law | Incident, reflected, refracted rays; critical angle case | Three regimes of interface behavior | θ_i, θ_r, θ_t, n₁, n₂, θ_c | Medium |
| Fig 2.7.8 | Fresnel Coefficients vs. Angle | Plot | §7.4, after Fresnel eqs | r_s, r_p, t_s, t_p as functions of angle; Brewster angle marked | Quantitative behavior at interfaces; Brewster's angle visual | r_s, r_p, θ_B, θ_c | Simple |
| Fig 2.7.9 | Waveguide Cross-Section and Mode Patterns | Diagram | §7.5, after mode derivation | Rectangular cross-section with TE₁₀, TE₂₀, TM₁₁ field patterns | Mode structure is spatial — must be seen to be understood | a, b, E-field lines, node planes | Complex |
| Fig 2.7.10 | Dispersion Relation in Waveguide | Plot | §7.5, after cutoff | ω vs. k with cutoff frequency marked; evanescent region shaded | Why waveguides have cutoff — visual makes it intuitive | ω_c, k_z, ω(k), evanescent region | Simple |
| Fig 2.7.11 | Circuit Elements from Maxwell Equations | Flowchart | §7.6, opening | Maxwell equations → Ohm → Kirchhoff → C, L → LC/RLC | Shows how circuit theory is a special case of field theory | Gauss → C, Faraday → L, continuity → KCL | Medium |
| Fig 2.7.12 | RLC Resonance Curve | Plot | §7.6, after RLC | Current amplitude vs. frequency; different Q values | Resonance is universal; connects to waveguide cutoff | ω₀, Δω, Q, I(ω) | Simple |
| Fig 2.7.13 | Interference and Diffraction Patterns | Plot/Diagram | §7.7, after diffraction | Double-slit geometry + intensity pattern | Fundamental wave behavior; connects to Vol 4 quantum | d, λ, θ, I(θ), fringes | Medium |
| Fig 2.7.14 | Skin Depth and Faraday Cage | Cross-section | §7.8, after skin depth | Field exponential decay into conductor; Faraday cage cross-section | Visualizes field penetration — abstract without picture | δ, E(z), conductor wall | Simple |

### Problem Sets (Foundations)

| Difficulty | Count | Topics Covered |
|-----------|-------|---------------|
| Computational | 8 | Wave equation solutions, Fresnel coefficients, waveguide modes, RLC circuits, skin depth calculations, Larmor radiation power |
| Conceptual | 6 | Why 2 polarizations, why waveguide cutoff, why Kirchhoff from Maxwell, why retarded not advanced, Brewster angle meaning, energy flow direction |
| Challenge | 4 | Derive cylindrical waveguide modes, radiation from oscillating dipole (full angular distribution), design Faraday cage for specific attenuation, derive thin-film interference from zone Maxwell |

---

## Section Outline

### Section 7.1: The Road from Zone Geometry to Classical E&M
- **Topic sentence:** This section maps the complete logical path from the zone manifold (Vol 1) through the Maxwell equations (Ch 3) and gauge theory (Ch 5–6) to every classical electromagnetic phenomenon.
- **"Why" entry point:** The reader has Maxwell's equations but hasn't seen their full power deployed; this section shows the territory ahead.
- **Key content:** Derivation roadmap figure; summary of what Ch 3 established; what the formal machinery of Ch 5–6 adds; what this chapter will derive. Statement: every result in classical electrodynamics follows from what we already have.
- **Exit condition:** Reader sees the complete architecture and knows no new postulates are needed.

### Section 7.2: Electromagnetic Waves — Propagation, Polarization, and Energy
- **Topic sentence:** Derive the wave equation from Maxwell's equations, solve it for plane waves, establish polarization states, and derive energy transport (Poynting vector) from the zone Lagrangian.
- **"Why" entry point:** Why do disturbances in the EM field propagate as waves? Because the curl equations couple E and B changes in a way that produces a wave equation.
- **Key content:** Wave equation derivation; plane wave solutions; dispersion relation ω = c|k|; transversality and 2 polarization states; Poynting vector from Noether/Lagrangian; energy density; radiation pressure.
- **Exit condition:** Reader can write general EM wave solutions, understands polarization, and knows how energy flows.

### Section 7.3: Electromagnetic Potentials and Radiation
- **Topic sentence:** Introduce scalar and vector potentials as the natural geometric objects (connecting to gauge invariance from Ch 3/6), derive retarded potentials, and obtain the complete radiation field from accelerating charges.
- **"Why" entry point:** Fields (E, B) are gauge-invariant observables, but the potentials (φ, A) are the fundamental objects in zone geometry — they ARE the off-diagonal metric components.
- **Key content:** Potentials from F_μν; gauge choices (Coulomb, Lorenz); Green's function and retarded potentials; radiation fields from oscillating dipole; Larmor formula; radiation reaction (brief, noting Abraham-Lorentz).
- **Exit condition:** Reader can calculate radiation from any charge distribution and understands the causal structure.

### Section 7.4: Boundary Conditions, Reflection, and Refraction
- **Topic sentence:** Derive the four electromagnetic boundary conditions from Maxwell's equations at material interfaces, then obtain Snell's law, the Fresnel equations, total internal reflection, and Brewster's angle.
- **"Why" entry point:** Real materials break translational symmetry — what happens at the boundary is set by the same Maxwell equations that govern the bulk.
- **Key content:** Pillbox and loop arguments; 4 boundary conditions; plane wave at interface; Snell's law; Fresnel equations for s- and p-polarization; Brewster's angle; total internal reflection; evanescent waves.
- **Exit condition:** Reader can solve any plane-wave–at-interface problem and understands reflection/refraction from first principles.

### Section 7.5: Waveguides and Confined Electromagnetic Fields
- **Topic sentence:** Solve Maxwell's equations in bounded geometries to derive waveguide modes, cutoff frequencies, and dispersion — showing that boundary-condition quantization (Vol 1, Ch 10) operates here too.
- **"Why" entry point:** What happens when EM waves are confined? The same boundary-condition mechanism that quantizes energy levels in Vol 1 now quantizes allowed propagation modes.
- **Key content:** Rectangular waveguide: TE and TM mode derivation; cutoff frequencies; dispersion relation ω²= ω_c² + c²k²; group and phase velocity; cylindrical waveguide overview; optical fiber basics.
- **Exit condition:** Reader can derive modes and cutoffs for rectangular waveguides and sees the pattern in cylindrical geometry.

### Section 7.6: Circuit Theory as a Limit of Field Theory
- **Topic sentence:** Derive Ohm's law, Kirchhoff's laws, capacitance, inductance, and RLC resonance as special cases of Maxwell's equations — showing that circuit theory is not a separate subject but a limiting regime of the zone field equations.
- **"Why" entry point:** Engineers use circuits daily without Maxwell's equations — but those circuit laws are consequences of the same Maxwell equations derived from zone geometry in Ch 3.
- **Key content:** Ohm's law from Drude + Coulomb; KCL from charge conservation; KVL from conservative E-field; capacitance from Gauss's law; inductance from Faraday's law; LC oscillations; RLC driven circuits; resonance and Q-factor.
- **Exit condition:** Reader sees circuit theory as a special case and can derive any circuit law from Maxwell.

### Section 7.7: Optics from Electromagnetic Waves
- **Topic sentence:** Derive geometric optics (lenses, mirrors) as the short-wavelength limit and wave optics (interference, diffraction) as the general case, establishing the foundation Vol 3 inherits.
- **"Why" entry point:** Optics is electrodynamics at visible wavelengths — every optical phenomenon follows from the wave solutions of §7.2 and the boundary conditions of §7.4.
- **Key content:** Geometric optics from eikonal approximation; thin lens equation from Snell's law; ray tracing; Huygens-Fresnel principle; single-slit diffraction; double-slit interference; diffraction limit; dispersion in media.
- **Exit condition:** Reader can derive basic optical results and sees optics as applied electrodynamics, with groundwork for Vol 3 wave mechanics.

### Section 7.8: Electromagnetic Waves in Conducting Media
- **Topic sentence:** Solve Maxwell's equations in conductors to derive skin depth, Faraday cage shielding, and wave attenuation — completing the classical treatment.
- **"Why" entry point:** The J = σE constitutive relation (from §7.6) modifies wave propagation in conductors; the result is exponential attenuation.
- **Key content:** Maxwell in conductors (displacement current vs. conduction current); complex wavenumber; skin depth formula; frequency dependence; Faraday cage shielding effectiveness; practical applications.
- **Exit condition:** Reader can calculate EM behavior in conductors and understands practical shielding.

### Section 7.9: Summary and the Classical Electrodynamics Landscape
- **Topic sentence:** Survey what has been derived, state explicitly what traces to zone architecture, and preview what Vol 3 inherits.
- **"Why" entry point:** The reader needs to see the complete picture — every classical E&M result, traced back to the Firmament membrane.
- **Key content:** Master table: phenomenon → zone-architecture origin; comparison with Jackson chapter-by-chapter; what this chapter establishes for Vol 3; open questions (radiation reaction, non-linear effects); problem set.
- **Exit condition:** Reader has a complete mental map of classical electrodynamics as a consequence of zone geometry.

---

## Verification Criteria

### Universal Criteria

- [x] Every requirement in the table above is marked MET
- [x] "But why?" chain — every question answered in the chapter text
- [x] No forward dependencies — no concept used that isn't established in prior chapters
- [x] Notation consistent with Vol 1 Appendix B and Vol 2 Chapters 1–6
- [x] Word count within target range: 12,000–15,000 words (~12,400)
- [x] All `[TODO]` markers resolved
- [x] All `[FIGURE]` placeholders have matching specs (14 of 14)

### Foundations-Specific Criteria

- [x] Every derivation starts from previously established results (equation numbers cited)
- [x] Maxwell's equations match exactly the form in 03-MAXWELL_DERIVATION.md
- [x] All numerical values match CODATA 2018 / Symbol_and_Constants.md
- [x] Problem sets cover full difficulty range (computational 8, conceptual 6, challenge 4)
- [x] Solutions written for selected problems (7 of 18; remainder deferred to appendix)
- [x] Results Vol 3 needs (optics, wave mechanics, dispersion) are clearly established and labeled (§7.9.3)

---

## Assigned Reviewers

| Reviewer | Assigned? | Status | Date |
|----------|-----------|--------|------|
| The Physicist | YES | PASS | 2026-04-07 |
| But Why? Reader | YES | PASS | 2026-04-07 |
| Writing Coach | YES | PASS | 2026-04-07 |
| Consistency Auditor | YES | PASS | 2026-04-07 |
| Homeschool Mom | NO | — | — |
| The Skeptic | YES | PASS | 2026-04-07 |
| The Student | YES | PASS | 2026-04-07 |
| Style Editor | YES | PASS | 2026-04-07 |
| Figure Auditor | YES | PASS | 2026-04-07 |
| Dependency Checker | YES | PASS | 2026-04-07 |

---

## Notes

- This chapter is the "applied E&M" complement to Ch 3's "foundational E&M." Ch 3 derived Maxwell's equations; Ch 7 deploys them across all classical phenomena.
- Source material: 03-MAXWELL_DERIVATION.md (equations to match exactly) and 03-APPLICATIONS.md (phenomena to cover).
- The key thesis: everything in Jackson's *Classical Electrodynamics* traces back to the Firmament membrane. No postulated laws — every result derived.
- Vol 3 inherits: optics (§7.7), wave mechanics groundwork (§7.2), dispersion in media (§7.7–7.8). These must be clearly established and labeled.
- Known open areas: radiation reaction (Abraham-Lorentz), non-linear E&M — acknowledge honestly, defer to Vol 4/5 as appropriate.

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-07 | Initial spec created | Phase 1 of chapter lifecycle |
| 2026-04-07 | Draft completed, self-review passed | Phases 2–4 |
| 2026-04-07 | All 9 reviewers PASS, status → VERIFIED | Phases 5–6 |
