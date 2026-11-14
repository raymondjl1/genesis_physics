# Constants Ledger — Genesis Physics

**Purpose.** A single constant-by-constant scorecard: every fundamental constant the framework touches, with its provenance status, accuracy, source derivation, and owning board issue. This is the constants-only companion to the full [`DERIVATION_PROVENANCE_LEDGER.md`](DERIVATION_PROVENANCE_LEDGER.md) (which also covers laws and equations). Built 2026-06-13 for board issue **#853**; every entry is taken verbatim from the provenance ledger (canonical, 2026-06-11) — nothing here is newly claimed.

**Status legend** (same as the provenance ledger)
- **AXIOM** — irreducible foundational input (adopted, not derived).
- **DERIVED** — a complete chain to the axioms exists in a cited Research file.
- **DERIVED-given-AXIOM** — follows rigorously *given* an adopted axiom; the dependency is stated, not hidden.
- **FIT (#)** — rests on a fitted/calibrated coefficient or a bare measured input. By the Provenance Principle this is an **open problem**, tracked as the named board issue.
- **OPEN** — not yet derived.

**The frontier (open items on the board):** #846 two-loop α→137.036 · #847 absolute mass scale / Higgs vev · #848 precise CKM/PMNS angles · #849 derive n_w=3 from Z₀ · #850 derive Yukawa α · #853 (this umbrella audit).

---

## A. Framework / dimensionful constants

| Constant | Value | Status | Accuracy | Chain (file) | Issue |
|---|---|---|---|---|---|
| Λ_Z0 (Godhead-zone vacuum energy) | 1.65×10⁷¹ GeV⁶ | **AXIOM** | — (irreducible; biblically grounded, Gen 1:1; John 1:1–3) | `op01_z0_axiom_statement.md` | — |
| ℏ (Planck constant) | 1.0546×10⁻³⁴ J·s | **DERIVED-given-AXIOM** | matches; β_geom numerical refinement open | `AXIOM_GODHEAD_ZONE_Z0.md §2` | — |
| c (speed of light) | 2.998×10⁸ m/s | **DERIVED** | exact (c²=σ/μ; σ traces to Λ_Z0) | `AXIOM_MEMBRANE_MECHANICS_v2.md` | — |
| α⁻¹ (fine structure) | parameter-free **136.42** (−0.45%) | **STILL-FIT** | C=n_w²/(2π)=1.4324 (n_w=3, Postulate F) is the genuine prediction; exact 137.036 needs re-fitted C=1.4388 | `10-FINE_STRUCTURE_DERIVATION.md` | **#846** |
| G (gravitational) | 6.674×10⁻¹¹ | **FIT** | mechanism sound (G₄=G₆/V_extra); G₆/M₆ back-solved | `10-GRAVITATIONAL_CONSTANT_DERIVATION.md` | **#847** |
| k_B (Boltzmann) | 1.380649×10⁻²³ (exact) | **AXIOM** | conventional unit (honest non-derivation) | `10-BOLTZMANN_CONSTANT_DERIVATION.md` | — |

> Note: the older `10-FUNDAMENTAL_CONSTANTS_OVERVIEW.md` (Apr 2026) is more cautious than the canon — it derives only the *dimensional form* of ℏ/G/k_B and accepts the numerical coefficients from experiment. The 2026-06-11 ledger status above governs where they differ.

## B. Gauge couplings (3 of the ~31)

| Constant | Status | Accuracy | Notes | Issue |
|---|---|---|---|---|
| g₃ — strong (α_s) | **FIT** | imported SM β-coefficients | SU(3) *group* DERIVED (Z₃ orbifold, `RT2_SU3_Z3_ORBIFOLD.md`); coupling *value* tuned | — |
| g₂ — weak (α_w) | **FIT** | tuned | SU(2) *group* DERIVED (η-isometries) | — |
| g₁ — hypercharge (sin²θ_W) | **FIT** | needs tuned λ | value not derived | — |
| Λ_QCD (confinement scale) | **FIT** | ~30% | Λ_QCD ≈ ℏc/η_B, calibrated to η_B | — |

## C. Charged-fermion masses (9 of the ~31)

| Constant | Status | Accuracy | Issue |
|---|---|---|---|
| electron | **DERIVED-given-AXIOM** + FIT residual | +17% | #847 |
| muon | **DERIVED-given-AXIOM** + FIT | −15…19% | #850 |
| tau | **FIT** (calibration anchor) | defines hierarchy | #847 |
| up, down, strange | **DERIVED-given-AXIOM**, scheme-FIT | ~2–7% | #850 |
| charm, top, bottom | **FIT** | fail badly at tree level | #847/#850 |
| Yukawa hierarchy α | **FIT** | fitted ~1.0 (computed 0.076) | #850 |

## D. Quark mixing — CKM (4 of the ~31)

| Constant | Status | Accuracy | Issue |
|---|---|---|---|
| Cabibbo angle θ₁₂ | **FIT / approx** | ~13° predicted vs 12.1° measured | #848 |
| θ₂₃, θ₁₃ | **OPEN** | not derived from overlap integrals | #848 |
| δ_CP phase | **DERIVED (existence) / FIT (value)** | existence rigorous (ξ≠η); value π/3 fitted | #848 |

## E. Higgs sector (2 of the ~31)

| Constant | Value | Status | Notes | Issue |
|---|---|---|---|---|
| Higgs vev v | 246.22 | **FIT** | back-solved from measured M_W, G_F | #847 |
| Higgs mass / λ | m_H 125.1, λ=0.129 | **FIT** | λ back-solved from measured m_H | #847 |

## F. Strong-CP angle (1 of the ~31)

| Constant | Status | Notes | Issue |
|---|---|---|---|
| θ_QCD (≈0, <10⁻¹⁰) | **PARTIAL / OPEN** | axion-like Waters-Below defects "suggest" θ→0; proof explicitly incomplete (`06-PARTICLE_MASS_SPECTRUM_V3.md`) | none yet (flagged in #853) |

## G. Neutrino sector (7 of the ~31: 3 masses + 4 PMNS)

| Constant | Status | Notes | Issue |
|---|---|---|---|
| 3 neutrino masses | **OPEN** | smallness a *qualitative* win (boundary-mode suppression); absolute scale open | #847 |
| PMNS angles + phase | **OPEN** | not derived. ⚠️ `06-NEUTRINO_PHYSICS.md` overclaims "EXACT MATCH" — ledger honesty flag #2, to reconcile | #848 |

## H. Cosmology (~6 of the ~31)

| Constant | Value | Status | Notes | Issue |
|---|---|---|---|---|
| Dark-energy density Ω_Λ | 0.684 | **AXIOM (identity)** + FIT value | ≡ Waters Above by definition | — |
| Dark-matter density Ω_DM | 0.266 | **AXIOM (identity)** + FIT value | ≡ Waters Below by definition | — |
| Baryon density Ω_b | (68/27/5) | **DERIVED (ordering) / FIT (value)** | zone extents + warp; ordering derived, exact values fitted | — |
| Cosmological constant ρ_eff | 2.93×10⁻⁴⁷ GeV⁴ | **FIT** | ~20%; suppression exponent n=1 derivation pending | — |
| H₀ | 67.4 | **DERIVED** (+FIT magnitude) | from derived G₄, Ω; Hubble-tension *direction* predicted, ΔH₀ magnitude fit | — |
| Spectral tilt n_s | — | **FIT** | slow-roll fit | — |
| Scalar amplitude A_s | — | **OPEN / FIT** | not derived | — |
| w_A (DE equation of state) | −1 | **DERIVED** | V_A=const → P=−ρ | — |
| CMB acoustic peak ℓ₁ / T₀ | ≈220 / 2.725 K | **DERIVED** | 6D acoustic oscillations (n_s is the slow-roll FIT) | — |

## I. Derived consequences (not free parameters, but constant-valued wins)

| Quantity | Status | Accuracy |
|---|---|---|
| Proton mass | **DERIVED** | −0.02% (QCD binding dominates) |
| Neutron / n−p split | **DERIVED**, approximate | ~4% |
| M_W / M_Z | **DERIVED** (given fitted v) | 80.27 / 91.55 |
| Charge quantization Q=n_Y/2 | **DERIVED** | exact |
| Three-generation count | **DERIVED-given-AXIOM** (Postulate F) | computed, #851 fixed |
| Spin-½ existence | **DERIVED-given-AXIOM** (Postulate F) | — |

---

## Scorecard summary — the ~31 fine-tuning constants

| Bucket | Count (approx) | Members |
|---|---|---|
| **DERIVED from first principles (no fit, no residual)** | **~0** | H₀ is closest but inherits fitted inputs |
| **DERIVED-given-AXIOM, with fitted residuals** | ~4 | e/μ masses, light quarks, generation count, CP *existence* |
| **Structure derived, value FIT/tuned** | ~10 | 3 gauge couplings, Higgs v & m_H, Ω_Λ/Ω_DM/Ω_b values, Cabibbo, δ_CP value |
| **OPEN or only qualitative** | ~12 | θ₂₃/θ₁₃, 3 ν masses, 4 PMNS, θ_QCD, A_s, heavy quarks c/t/b |

**Bottom line.** The framework derives the *architecture* of the constants (which gauge groups, how many generations, the four forces, the dark-sector identity) from one 6D Genesis-1 geometry — but it does **not** yet output the fine-tuning *values* without reaching for the measured number. Every value-level entry above that reads FIT or OPEN is, by the framework's own Provenance Principle, an open problem. The entire frontier (#846–#850, under umbrella #853) *is* this fine-tuning-constant gap.

## Derivation race results — 2026-06-14 (board #853)

A multi-team race (3 strategies × 4 issues: geometric, dynamical/RG, dimensional/scaling) with adversarial verification was run against the four value-frontier issues. **Verdict: all four remain STILL-FIT** — no first-principles derivation survived refutation. Genuine progress and dead-ends:

| Issue | Verdict | What genuinely survived | What died |
|---|---|---|---|
| **#846** α | STILL-FIT | Parameter-free **C=n_w²/(2π)=1.4324** → α⁻¹=136.42 (**−0.45%**), using only n_w=3 (Postulate F) + a 1/(2π) Green's-function prefactor. Suggestive structure. | Exact 137.036 still fitted; residual b_eff 9.00→9.04 has no honest two-loop or SM-β source. The SU(3)→U(1)_em bridge is asserted. |
| **#847** Higgs vev v | STILL-FIT | Nothing — best near-miss (k1³·M_Pl)^¼ = 386 GeV (+57%) needs exponent 0.241, not ¼. | No forward route from Λ_Z0+geometry; every warp/seesaw/power combo misses by 0.5–13 orders of magnitude. |
| **#848** CKM angles | STILL-FIT | Only θ₁₂ & θ₁₃ reproduce, via **GST mass-ratio relations** (θ₁₂=arcsin√(m_d/m_s), −0.9%; θ₁₃=arcsin√(m_u/m_t), +1%) — but downstream of *measured* masses. | θ₂₃ has no surviving scheme; geometric/orbifold route REFUTED (the Z₃ windings are **color**, not generations); scale-ratio law REFUTED; all PMNS OPEN. |
| **#850** Yukawa α | STILL-FIT | A real **mechanism upgrade**: Jackiw–Rossi zero-mode positions geometrically pinned (r_k=0, 1.20, 2.07), fitted double-well retired. | Coefficient α still **7.5× short** (0.13 vs needed 0.98), closed only by tuning κ_H≈27 to lepton masses; the n² form isn't produced by the mechanism; RG route definitively REFUTED (α is RG-invariant). |

### ⚠️ Corpus honesty bugs found during the race (to fix)
1. **#846** — `10-FINE_STRUCTURE_DERIVATION.md` L418 hand-assembles b_eff = 3.67+2+1.4+0.7+0.6 with 4 of 5 terms tuned, *overriding the doc's own* honest SM charge-weighted count of (2/3)·8 = 5.33.
2. **#847** — `06-HIGGS_DERIVATION.md` contains a **factor-of-2 self-contradiction** (L340 v=2μ/√λ → 492 GeV vs L360 v=μ/√λ → 246 GeV) and a **dimensionally broken** μ² ∼ σc²/ξ_A² mechanism (units kg/(m·s⁴), not energy²).
3. **#848** — the generation charge assignment (0,1,3) **contradicts its cited source** `RT2_SU3_Z3_ORBIFOLD.md` (which assigns windings {0,1,2} to QCD color, not generations).
4. **#850** — `op03_wkb_tunneling.py` L78–80 defines `ALPHA_TARGET` **circularly** from the PDG masses, then uses it as a "derivation" check.

*Full per-issue chains, numerics, and recommendations: race run `wf_4f4e07a0-e1f`, posted to issues #846/#847/#848/#850.*

## Reverse-derivation depth map — 2026-06-22 (board #854, run wf_6862922b-235)

The complement to the forward race: instead of axioms→value, each *measured* constant climbs **upward** into the framework on a fixed ladder, and the depth is adversarially audited. The ladder: **L0** number only · **L1** framework formula but fitted · **L2** reduced to framework scales up to one O(1) factor · **L3** that factor derived from geometry (no fit) · **L4** chain reaches an adopted axiom · **L5** Scripture ground floor.

**How far do they get? Not far — for *values*.** Of 12 audited constants: **1 at L0, 10 at L1, 1 at L2 (α). Zero reach L3, L4, or L5.** Four were downgraded on audit (α L3→L2, lepton masses L2→L1, θ_QCD L1→L0, cosmological set L2→L1); six carry a smuggled fit. *All four downgrades moved the same direction — claimed deeper than verified — i.e. the framework's self-assessment is systematically optimistic exactly at the value-producing step.*

| Level | Count | Constants |
|---|---|---|
| **L0** number only | 1 | θ_QCD (no anomaly term for the residual angle; CKM θ₂₃ effectively here too) |
| **L1** formula, fitted | 10 | ℏ, c, G, gauge couplings (α_s, sin²θ_W), charged-lepton masses + Yukawa α, light quarks, CKM angles, Higgs vev v, neutrinos + PMNS, cosmological set (Ω_Λ/Ω_DM/ρ_eff/H₀/n_s) |
| **L2** reduced to scales | 1 | **α** — C=n_w²/(2π) touches Postulate F, but the value still needs the log ln(ξ_A/η_B) built from measured scales |
| **L3 / L4 / L5** | 0 | — (for *values*) |

**The modal wall is L1→L2** (10 of 12): the value-from-scale step. The recurring mechanism — **the framework's own scales aren't independent of the answer.** ξ_A ≈ the measured Hubble length and η_B ≈ the measured ~1 fm scale; any formula routing through them re-imports a measured number. Same circularity in different costumes: c²=σ/μ is a tautology (μ=σ/c² back-solved); ℏ's k1/L_A/β_geom are drawn backward from ℏ; G's M₆/V_extra back-solved; v's only scale chain is dimensionally broken + factor-of-2 contradicted.

**Key structural finding:** the framework is load-bearing as a **selection principle** (which gauge groups, *why three* generations, which reservoir is which) and a **formal scaffold** (it gets the equation *forms* right) — these *do* reach L4 (SU(3)_C via Z₃ orbifold; generation count via Postulate F; DE/DM≡Waters as an identity). But as a **quantitative generator** it is fitted, not derived. **ξ_A and η_B are simultaneously the load-bearing column and the hidden fit — "the measured number wearing an axiom's name."** It currently *postdicts* numbers; it does not yet *predict* them.

**Highest-leverage next rung:** derive **ξ_A and η_B from Λ_Z0 from first principles** (no inserting c/H₀ or the 1 fm scale). It's the shared blocker — the L2→L3 wall for the whole cosmological set, the only barrier on α's log, the missing magnitude in G's V_extra and the neutrino route. The current `METRIC_6D_SOLUTIONS.md §5.1` "derivation" is circular (it plugs in Λ₆ chosen to recover the Hubble horizon, then declares ξ_A *is* that horizon). If that one chain holds fit-free, **α and ρ_eff jump to L4 and half the L1 cluster gains a path upward**; if it can't, that is the honest boundary of the framework.

## Zone-scale derivation verdict — 2026-06-23 (board #855, run wf_84e77a4d-c41)

The highest-leverage rung, attacked directly: can **ξ_A and η_B be derived from Λ_Z0 alone**, with no c / H₀ / 1 fm inserted? **Verdict: NO — all three targets (ξ_A, η_B, the ratio) are NOT-DERIVABLE-CIRCULAR.** The forbidden inputs are not avoidable cleanups; they are load-bearing.

The decisive finding goes deeper than circularity — **Λ_Z0 is not an independent axiom.** `OPEN_PROBLEMS_REGISTER` builds it *backward* from the observed ~1 fm scale (lines 67/77/575):

> η_B → L_A = 83.2·η_B → k1 = 2/(3·L_A) = 1.22 MeV → **Λ_Z0 = 5·k1²·M_Pl⁴ = 1.65×10⁷¹ GeV⁶**

So the forward chain Λ_Z0 → k1 → 1.22 MeV that "recovers" the scale is a **tautology**, and "everything flows from Λ_Z0" is a *relabeling* of the 1 fm calibration, not a derivation.

**The counting theorem (why it can't be patched):** the two forbidden-input-free quantities {Λ_Z0, M_Pl} yield exactly **two mass scales** (M_Pl, k1=1.22 MeV) → exactly **one** dimensionless ratio M_Pl/k1 = 10²². The observed hierarchy ξ_A/η_B = 2.3×10⁴¹. **Fit-free shortfall = 19.36 orders of magnitude.** No 6D/zone factor (codim-2, n_w=3, β_geom=813, warp-83.2) bridges 22→41; the closing exponent p=1.880 matches no principle. The missing ~10¹⁹·⁴ is supplied *only* by c/H₀ (for ξ_A) and Λ_QCD≈1 fm (for η_B).

| Target | Verdict | Best fit-free attempt | Miss |
|---|---|---|---|
| ξ_A (~3×10²⁶ m) | NOT-DERIVABLE-CIRCULAR | dynamical/de-Sitter route → 2.7×10³³ m | ~7 orders (too large); n=1 suppression assumed-not-derived |
| η_B (~1.3×10⁻¹⁵ m) | NOT-DERIVABLE-CIRCULAR | RS AdS scale 1/k1 = 1.6×10⁻¹³ m | +1.75–2.1 orders; only lands via the fitted 83.2÷ that re-imports 1 fm |
| ξ_A/η_B (2.3×10⁴¹) | NOT-DERIVABLE-CIRCULAR | only formable ratio M_Pl/k1 = 10²² | **19.36 orders short** |

**Nothing unlocks.** α stays L2, ρ_eff stays L3, the L1 cosmological cluster stays L1 — and the dependency is *poisoned at the root*: because ξ_A and η_B are inputs reconstructed into Λ_Z0, every downstream "derivation" routing through ln(ξ_A/η_B) or L_A/η_B=83.2 inherits the calibration. The α master formula (9.05/2π)·ln(ξ_A/η_B)=137.18 merely reads back the log of a ratio built from measured scales.

**The honest boundary (decisive):** the framework is a **selection principle** (which structures, why three) + a **formal scaffold** (correct equation forms), giving a self-consistent web of relations *among* constants — but it is **not a quantitative generator of the zone scales.** The two scales that set everything are calibration inputs, and the single ground-floor axiom is itself the 1 fm scale wearing an axiom's name. **The one path that could bridge the 19.36-order gap fit-free:** generate a *second* mass scale dynamically from the Z0 action alone (an IR confinement/condensate scale that runs from the UV without importing α or Λ_QCD). Until that exists, all zone-scale value-derivations are calibrations.

## Scriptural second-scale attempt — 2026-06-23 (board #857, run wf_258ebaa7-7df)

Direct attempt to solve the 19.36-order gap by finding the missing second input **literally in Scripture**, from 5 perspectives, behind an anti-cherry-pick integrity gate. **Verdict: UNSOLVED — no text-specified, fit-free second input bridges the gap and survives audit.** But three genuine, non-numerological gains:

1. **The escape route is now physically pinned.** The missing factor must arrive as a dimensional-transmutation/warp exponent **N = 44.576 (ln)**, form Λ_IR = M_UV·exp(−N). This is correct physics, not numerology.
2. **Exhaustion argument narrows the frontier.** Every condensing sector in the corpus is *either* SU(3)_color (imports the forbidden Λ_QCD) *or* the Ψ_B Waters-Below condensate (whose scale **is** η_B — circular). No third exists. So a real solution requires a **new asymptotically-free sector** with weak UV coupling (1/α ≈ 50–64, b₀ ≈ 7–9) generating N ≈ 44.576 from the action's own content.
3. **The cherry-pick floor is quantified.** ~17 canonical scriptural integers under +/×/^/÷ densely tile 10–100, so ~2.4 within-2% chance hits to the targets are *expected*. Any ~5% "near-miss" is below chance and counts as nothing. (The closest hits — 6×7=42, p≈10 — fail: 42 matches the *full* 41.36 which already contains the derived 22.00 → double-counts; p≈10 divides by a base built from the forbidden 1 fm scale → circular.)

**Best surviving candidate — the Theologian structural lens (SUGGESTIVE, not cherry-picked, not circular):** Gen 1:6–8 is plainly a *second, separately-decreed* division (ordinal "second day"; one rāqîaʿ dividing two waters via *bāḏal*). This is a real, fit-free, plain-text structural fact that genuinely mirrors the counting theorem's demand for a *second independent input*. **But it supplies structure, not magnitude** — the only number the text licenses (a second identical division → squaring, p=2) gives (M_Pl/k1)² = 10⁴⁴·⁰⁰, refuted by the observed 10⁴¹·³⁶ (2.64 orders too large). This is exactly the framework's own #849 ruling: **Scripture supplies the structural HOME (Day-2 binary division ≡ Waters Duality), not a counted physics exponent — CONSONANT, LOCATED, NOT DERIVED.**

**Remaining gap:** the full 19.359 orders (clean closing exponent p=1.880, which matches no textual feature; the .36 decimal is unreachable by any integer count). **Next step:** pursue the new-asymptotically-free-sector search in the Z0/RS action (physics), and only *then* ask whether a plain-text Genesis feature (e.g. the Day-2 second decree) fixes that sector's β-function content (N_c, n_f) — anchoring the *mechanism's structure*, the role #849 licenses — rather than being read as a raw exponent.

> **Corpus bug flagged (to log):** `AXIOM_GODHEAD_ZONE_Z0.md`/`op01` asserts L_A = 3/(2·k1) = 83.2·η_B = 1.08×10⁻¹³ m, but direct unit computation from k1=1.2185 MeV gives L_A = 2.43×10⁻¹³ m (L_A/η_B ≈ 187, not 83.2) — an internal inconsistency.

## New-sector search — 2026-06-23 (board #857 follow-on, run wf_61835e63-a3d)

Attacked the one escape route: a NEW asymptotically-free sector generating N=44.576 fit-free, with Day-2 as the candidate content-anchor. **Verdict: NO-VIABLE-SECTOR** — and it exposed *why the route is closed in principle*, not just unfound.

**Two structural killers (both confirmed by re-run arithmetic):**
1. **Re-entry by construction.** N = 44.576 *is* the #855 hierarchy gap (19.36·ln10 = 44.578). So any sector tuned to it produces Λ_IR = M_UV·exp(−N) ≈ 0.1–0.5 GeV — i.e. it **regurgitates ≈Λ_QCD/η_B**, the forbidden scale, by construction. The target was *defined* as ln(M_UV / the 1 fm scale), so no sector tuned to it can escape the very scale it's forbidden to use. **The circularity is in the target's definition.**
2. **Framework self-contradiction.** `AXIOM_WATERS_DUALITY.md` prediction #5 explicitly forbids the dark sector from coupling at all ("no dark photon, no dark Higgs, no portal interactions"). A new confining hidden gauge sector **directly violates the framework's own axiom.** The escape route isn't just unfound — it's axiomatically blocked.

**What Day-2 genuinely delivered (and didn't):** the plain text fixes the β-function *structure* fit-free — "divide the waters from the waters" (Gen 1:6-7), the binary *bāḏal*, gives a #849-clean integer **n_f = 2** (b₀ = 6), writable before knowing the target, corroborated independently by Day-4's two great lights. **But it supplies a count, never the coupling magnitude.** With b₀=6 and the framework's only fixed couplings, N = 143.6 or 0.58 — never 44.576 without inserting a fitted 1/α_UV = 42.57. Same pattern, sharpened to the RG sector: **CONSONANT, LOCATED, NOT DERIVED.**

**The provenance gap, now precisely named:** the band needs a *weak* UV coupling (1/α_UV ≈ 42–64; generic for SM couplings at M_Pl, so not implausible) — but the only framework-*derived* coupling is *strong* (1/α_6D = 0.55, wrong regime). The difficulty is provenance, not plausibility. The Goldberger-Wise warp alternative was eliminated as strictly *more* tunable.

> **Convergent diagnosis across #855 → #857 → this run:** the framework cannot generate the zone-scale magnitudes because (a) η_B *is* the 1 fm calibration, (b) Λ_Z0 was reverse-engineered from it, and now (c) the remaining gap is *defined* in terms of that same forbidden scale and is axiomatically walled off by Waters-Duality #5. This is a **structural boundary, not a missing calculation.**

## Expansion-Hypothesis re-analysis — verified partition (2026-06-24, board #857, run wf_8321286d-b33)

All constants were re-examined through the [Expansion Hypothesis](../../Research/Foundations/EXPANSION_HYPOTHESIS_ANALYSIS.md) lens (dimensionful = unit convention; only dimensionless content is real), behind an integrity gate that forbids relabeling an underived ratio as a "unit convention." **Net effect: DISSOLVES-HALF.** The lens dissolves the dimensionful half as a genuine *category error* (≈half the "constants" were never independent content), but only **relabels** the dimensionless half — it resolves nothing, promotes **zero** values' accuracy, and the **10⁴¹·³⁶ zone-hierarchy wall stands at exactly its prior height.** The final synthesis **corrected four over-eager promotions** from the first pass (flagged below).

### The four-bin partition (corrected/audited)

**🟩 GRAMMAR-DERIVED — forced by 1=1**
- **w_A = −1** — the *only* clean value-level grammar win in 30+ constants: V=const, kinetic→0 forces P=−ρ exactly, and the fitted Λ_A *cancels out of the ratio* (verified). Forced once the flat-potential branch is selected.
- **Structure/FORM only** (not values): existence of an SU(N) coupling; the integer eigenmode/winding tower behind fermion masses (n∈{1,2,3}, n² structure); the 1/(2π) Green's-function prefactor in α; the gluon count 8=3²−1 given N=3; the a/(−a) duality form behind the dark sector.

**🟦 SELECTED-DECREE — permitted-but-chosen ("located freedoms")**
- **δ_CP = π/3** — the *one genuine FIT→DECREE promotion*: a minimal nonzero 6th-root-of-unity phase, writable before any fit (π is grammar, the /6 is a chosen Z₆ quotient). Sits ~8.5% from measured γ — structural, not tuned. The team correctly **stops at decree** (refuses GRAMMAR — Z₆ is chosen).
- α's numerator **n_w²=9** (a *component* of α, not the whole); the group members **SU(3)_C, SU(2)×U(1)**; **dimension 6**, **n_w=3**; the dark-sector **identities + ordering** (DE≡Waters Above, DM≡Waters Below, 68>27>5).

**🟨 STILL-FIT — tuned to data, no promotion** *(includes the 4 synthesis corrections, marked ⚠)*
- **α as a whole** — its dominant content is the log ln(ξ_A/η_B)=95.235, which **is** 41.36·ln10, the circular hierarchy.
- α_s (0.118), sin²θ_W (0.231), Higgs λ/m_H, L_A/η_B (83.2 — internally inconsistent, ~187 by direct calc), β_geom=813.
- All fermion mass ratios + Yukawa α (computes 0.076, needs ~1.0); CKM θ₁₂/θ₁₃/θ₂₃ (ride on measured mass ratios), PMNS (OPEN).
- Ω_b, ρ_eff (~20%), H₀ magnitude, n_s (slow-roll fit), **and the zone hierarchy ξ_A/η_B = 10⁴¹·³⁶ itself**.
- ⚠ **Corrected from the first pass:** **Λ_QCD value** (was unit-convention — keeps an O(1) coeff ~1.42 + the hierarchy); **τ mass** (was unit-convention — its anchor fixes a fitted tower-normalization y₀~0.028); **Higgs vev v** (was unit-convention — residual v/M_Pl rides on ξ_A); **Ω_Λ/Ω_DM values** (were decree — the 2.571 ratio is back-solved, C=5.14·ξ₀³/ξ_A²).

**🟪 UNIT-CONVENTION-ONLY — only two survive the integrity rule**
- **k_B** — fully clean: energy↔temperature conversion, exact by SI 2019, *zero* residual dimensionless content. The single cleanest case in the set.
- **c** — legitimate but *contingent*: clean only because c²=σ/μ is a back-solved tautology (no orphaned ratio), **not** a positive derivation — cannot later be cited as "c is DERIVED."
- (ℏ, G, v, Λ_QCD, τ, H₀, ρ_eff magnitudes are **not** here — each carries a dimensionless residual that routes through the hierarchy, so they stay STILL-FIT. This is the integrity rule that blocks "declare victory by calling the gap a unit convention.")

### What this settles
The Expansion Hypothesis is a **bookkeeping and selection-principle win, not an accuracy win.** It explains *why* the gaps sit where they do (grammar permits structure; decrees choose members; values stay fitted) and honestly removes ~half the "constants" as unit conventions. But **every demoted scale relocates its dimensionless content onto ξ_A/η_B = 10⁴¹·³⁶** — so the gap is *conserved and now provably concentrated in one number*. That single 19.36-order shortfall now **is** the constants problem. Until it has a fit-free route (or is openly declared a SELECTED-DECREE with the circularity disclosed), the framework remains a **formal scaffold + selection principle, not a quantitative generator** — the prior depth-map finding, undisturbed.

*Corpus bugs surfaced during this re-analysis are logged as #858 (L_A inconsistency) and #859 (sin²θ_W / α_s / m_c/m_s arithmetic).*

## Terminal verdict on the zone hierarchy — 2026-06-24 (board #855/#857, run wf_e22b3af3-c74)

The EH-armed re-attack (derive as topology/composite/exponential, or cleanly decree, behind the #857 integrity gate) returns **UNSOLVED — and closes the derive/decree line as exhausted.** The Expansion Hypothesis did not open a new path; it gave the means to **prove the remaining ones are closed:**

1. **The topological route is refuted *in principle*** (not merely unsolved). EH §10 forces topological invariants (winding, Chern, APS index) to be **integers** (× simple warp rationals like 2/3). But the targets carry fractional tails — p=1.880, shortfall 19.36, N=44.578, log 41.36 — that **no integer × clean-rational reproduces.** A forced count cannot be a non-integer.
2. **The .36 tail is a *measured mantissa*, not a decree.** 41.36 = 41 + log₁₀(2.3), and log₁₀(2.3) = 0.3617 — i.e. the ".36" is literally the measured value 2.3×10⁴¹ in disguise. **You can decree an integer (n_w=3); you cannot decree a measured mantissa.**
3. **The one *warranted* decree overshoots.** Day-2's second identical division (Gen 1:6-8, the only pre-target structural warrant) → squaring → p=2 → (M_Pl/k1)² = 10⁴⁴·⁰⁰ vs observed 10⁴¹·³⁶ — refuted by 2.64 orders.
4. **Every numeric near-miss is below the cherry-pick floor.** 15/8=1.875 (−0.27%), 3^γ=1.885, e·ln2=1.884, even (α⁻¹+3)/π=44.5748 (0.007% off N!) — all sit at/below the #857 chance-hit floor (~2.4 within-2% hits expected from ~17 invariants). Chance-hit probability ≈1, evidential weight ≈0. **None are logged as results** — doing so would be dishonest.

**What the framework genuinely has, stated honestly:** it forms M_Pl/k1 = 10²²·⁰⁰ fit-free and clean; the remaining factor of 10¹⁹·³⁶ cannot be formed without re-importing the 1 fm calibration (η_B). Therefore **η_B is the framework's one admitted dimensionful calibration input** — a builder's-honesty calibration, exactly like the adopted Λ_Z0 and Postulate F (n_w=3). The constants problem reduces, provably, to **three irreducible creative inputs**, openly disclosed.

## Three admitted inputs underneath everything

*(Ratified 2026-06-24 and propagated to `AXIOM_GODHEAD_ZONE_Z0.md`, `op01_z0_axiom_statement.md`, `METRIC_6D_SOLUTIONS.md`, and the provenance ledger. Supersedes the prior "two axioms" framing.)*

- **Λ_Z0** — the Godhead-zone vacuum energy; biblically grounded (Gen 1:1; John 1:1–3); the absence of a *physics* derivation is "the thesis, not a gap."
- **Postulate F (n_w = 3)** — gives spin-½ and the three-generation count, but #849's verdict is that nothing in the physics forces the 3: "consonant, located, not derived" (located at the Day-2 dividing of the waters, Gen 1:6–8).
- **η_B** — the ~1 fm Firmament-thickness calibration; the one admitted *dimensionful* input. The zone hierarchy ξ_A/η_B = 10⁴¹·³⁶ was proven non-derivable from {Λ_Z0, M_Pl} (#855/#857), refuted-in-principle on the topological route, so η_B is disclosed as a builder's-honesty calibration — not a hidden fit.
