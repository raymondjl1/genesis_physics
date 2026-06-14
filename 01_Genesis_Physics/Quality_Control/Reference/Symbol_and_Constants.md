# Symbol and Constants Reference

**One-page canonical reference for mathematical constants and parameters**

**Canonical reference maintained by the Analysis quality system**

Last updated: June 12, 2026 (added Topological Winding Numbers — n_w/n_q split, #849-race O5 resolution)
Location: `Quality_Control/Reference/Symbol_and_Constants.md`

---

## Firmament Properties

| Symbol | Value | Units | Dimension | Meaning |
|--------|-------|-------|-----------|---------|
| **σ** | 6.0×10⁹⁸ | kg/(m·s²) | [ML⁻¹T⁻²] | Firmament membrane 3-brane tension; fundamental creation parameter |
| **μ** | 6.7×10⁸¹ | kg/m³ | [ML⁻³] | Firmament membrane volume mass density |

---

## Derived Constants

| Symbol | Value | Units | Derivation | Meaning |
|--------|-------|-------|------------|---------|
| **c** | 2.998×10⁸ | m/s | √(σ/μ) | Speed of light; Firmament membrane wave speed |
| **G** | 6.674×10⁻¹¹ | m³/(kg·s²) | c⁴/(8πσ×L_eff²) | Gravitational constant; geometric coupling |
| **α⁻¹** | 137.036 | dimensionless | 1.44×ln(ξ_A/η_B) | Fine structure constant reciprocal; electromagnetic coupling |

---

## Scale Parameters

| Symbol | Value | Units | Meaning |
|--------|-------|-------|---------|
| **ξ_A** | 3×10²⁶ | m | Waters Above bulk extension (canonical, locked); numerically close to but distinct from Hubble radius (≈1.4×10²⁶ m) — see Vol 1 §10.2.1 |
| **η_B** | ~1.3×10⁻¹⁵ | m | Waters Below extent; nuclear-scale QCD cutoff |
| **L_eff** | 8.96×10⁻²⁹ | m | Effective coupling length from 6D reduction |

---

## Sustaining Field (κ States)

| Parameter | Regime | Value/State | Meaning | Thermodynamic Phase |
|-----------|--------|-----------|---------|---------------------|
| **κ** | General | [ML⁻¹T⁻³] | Power density; sustaining field strength | All phases |
| **κ_create** | Supercritical | >> κ_full | Rapid ordering; entropy decreasing | Creation (Days 1-6) |
| **κ_full** | Equilibrium | Edenic baseline | Perfect repair; zero net entropy production | Edenic (Post-Sabbath) |
| **κ_partial** | Subcritical | κ_full × (1 - ε) | Aging and decay; ε ~ 10⁻²⁷ to 10⁻⁶⁰ | Fall (Present epoch) |
| **κ_redeem** | Recovery | TBD | Entropy reversal; restoration | Redemption (Future) |

---

## Energy Budget (Friedmann)

| Density Parameter | Symbol | Fraction | Identification |
|------------------|--------|----------|-----------------|
| Dark Energy | Ω_Λ | 0.684 (68.4%) | Waters Above (Ψ_A); repulsive |
| Dark Matter | Ω_DM | 0.266 (26.6%) | Waters Below (Ψ_B); attractive |
| Baryonic Matter | Ω_b | 0.049 (4.9%) | Firmament condensed matter (Z₂.₂.₂) |
| **Total** | **Ω_total** | **0.999 ≈ 1** | Flat geometry (critical density) |

---

## Density Values

| Quantity | Symbol | Value | Units | Notes |
|----------|--------|-------|-------|-------|
| Waters Above density | ρ_A | 5.8×10⁻²⁷ | kg/m³ | Dark energy; constant with expansion |
| Waters Below density | ρ_B | 2.3×10⁻²⁷ | kg/m³ | Dark matter; dilutes as a⁻³ |
| Baryonic matter density | ρ_matter | 4.2×10⁻²⁸ | kg/m³ | Stars, atoms, earth; dilutes as a⁻³ |
| Critical density | ρ_critical | ~2.3×10¹⁷ | kg/m³ | QCD phase transition threshold |

---

## Cosmological Parameters

| Parameter | Symbol | Value | Meaning |
|-----------|--------|-------|---------|
| Hubble constant (present) | H₀ | 67.4 | km/s/Mpc |
| Hubble at creation | H_creation | ~3×10¹⁴ × H₀ | Exponential early expansion |
| Cosmological constant | Λ | 1.1×10⁻⁵² | m⁻² |
| Scale factor (now) | a(t_now) | ~10²⁶ | m (relative to Planck length) |

---

## Waters Fields

| Field | Symbol | Equation of State | Density Scaling | Role | Identification |
|-------|--------|-------------------|-----------------|------|-----------------|
| Waters Above | Ψ_A | w ≈ -1 | Constant (ρ ∝ a⁰) | Repulsive; cosmic acceleration | Dark energy |
| Waters Below | Ψ_B | w ≈ 0 | Matter-like (ρ ∝ a⁻³) | Attractive; gravitational scaffolding | Dark matter |

---

## "Waters Below" — Notation Convention (canonical disambiguation — 2026-06-13, #256 resolution)

The phrase **"Waters Below"** carries *four distinct senses* across Vol 2 (Ch 01 §1.0, Ch 04 §4.2, Ch 05, Ch 06). They share a name and a boundary parameter (η_B) but are different objects with different dimensions, and must not be conflated. Reserve a distinct symbol for each:

| Sense | Reserved symbol | Dimension | What it is | Canonical first use |
|-------|-----------------|-----------|------------|---------------------|
| **Field** | **Ψ_B** | (field on spacetime) | The dark-matter field/excitation; w ≈ 0, ρ ∝ a⁻³ (see Waters Fields table above) | Ch 05 §5.x; Glossary "Waters Below" |
| **Region (1D real slice)** | **W_B** | 1D | The η-interval region between the branes, 0 ≤ η ≤ η_B; the real transverse slice | Vol 2 Ch 04 §4.2 (Eq. before 2.4.1) |
| **Region (2D complex fiber)** | **W_B^ℂ** | 2D | The complexified transverse fiber w = η₁ + iη₂ = ρe^{iψ}, \|w\| ≤ η_B, on which the Z₃ orbifold acts | Vol 2 Ch 04 §4.2 (Eq. 2.4.1a) |
| **Scriptural referent** | **"Waters Below (Gen 1:7)"** | — | The mayim beneath the rāqîaʿ of Genesis 1:6–7; the scriptural object the geometry instantiates | Gen 1:6–7; Vol 1 Ch 3–5 |

**Rules:** (1) **Ψ_B** is *always* the field, never the region — do not write "Ψ_B" for the η-slice. (2) **W_B** is the 1D real region (the η-interval); **W_B^ℂ** is its 2D complexification (the fiber the Z₃ action requires). The same boundary scale η_B bounds both (η ∈ [0, η_B] for W_B; \|w\| ≤ η_B for W_B^ℂ). (3) When "Waters Below" denotes the **scriptural** object, tag it **(Gen 1:7)** so the referent is unambiguous. (4) The bare phrase "Waters Below" in prose defaults to the **region** sense (W_B / W_B^ℂ); use the reserved symbol whenever dimension or field-vs-region could be ambiguous. Mirrored in `Glossary.md`.

---

## Topological Winding Numbers (canonical notation — 2026-06-12, #849-race O5 resolution)

Two **distinct π₁ invariants** were historically both written "n_w" (or "n_ξ"). They must not be conflated — conflating them was the factor-3 double-count diagnosed in the #849 derivation race (`Research/Peer_Review/849_nw3_derivation_race/REFEREE_REPORT.md`, corpus correction #6; both race teams reached this disentanglement independently).

| Symbol | Name | What it winds | What it determines | Typical values |
|--------|------|----------------|--------------------|----------------|
| **n_w** | Charge winding (per-particle) | The U(1)_A phase of Ψ_A around a particle's defect line in Firmament 3-space | Electric charge quantization, Q = n·e | n_w = 1 for every charged lepton (all three generations) |
| **n_q** | Fiber/quotient winding (background) | The quotient (boundary) winding of the Waters-Above fiber **background** on the Z₃ orbifold; covering-space winding N = 3·n_q | Generation count via the Z₃-equivariant index (per-sector index = N/3 = n_q) | n_q = 3 ⟺ N = 9 ⟹ 3 color-singlet generations (+ colored partners, 9 = 3×3) |

**Rules:** (1) n_w is a property of an individual particle/defect; n_q is a property of the fiber background — they are independent invariants of different loops. (2) "n_ξ = 1 for every fermion" in defect tables is the CHARGE winding, **not** a generation index. (3) Postulate F's adopted "n_w = 3" is, in this canonical notation, the **background** invariant n_q = 3 (the generation-counting winding); it remains an adopted axiom, not derived (see `AXIOM_GODHEAD_ZONE_Z0.md` and registry §I). (4) The ξ-radial resonance spectrum is the **mass-hierarchy** mechanism, not the generation-counting mechanism.

---

## Key Dimensionless Ratios

| Ratio | Value | Significance |
|-------|-------|---------------|
| ξ_A / η_B | ~2.3×10⁴¹ | Determines α via ln function; cosmic scale hierarchy |
| κ_partial / κ_full | ε ~ 10⁻²⁷ to 10⁻⁶⁰ | Fall phase subcriticality; aging rate parameter |
| Ω_Λ / Ω_matter | ~27 | Energy hierarchy favoring dark expansion |

---

*Reference constants. For derivations, see `Research/Mathematical_Models/Firmament_Dynamics/`. For validation against observation, see `Research/Observational_Signatures/`.*
