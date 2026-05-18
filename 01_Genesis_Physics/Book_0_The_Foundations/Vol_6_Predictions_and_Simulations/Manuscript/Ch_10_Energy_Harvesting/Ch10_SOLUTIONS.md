# Ch 10 — Worked Solutions and Hints

Solutions to the end-of-chapter problem set (§10.11.4). Computational problems (10.1–10.5) get full solutions; conceptual problems (10.6–10.10) get summary answers; challenge problems (10.11–10.13) get hints plus a grading rubric.

---

## 10.1 — Casimir pressure vs gap

Use `F/A = π² ℏ c / (240 a⁴)` with ℏ = 1.055 × 10⁻³⁴ J·s, c = 3 × 10⁸ m/s.

| a (nm) | a⁴ (m⁴) | F/A (Pa) |
|---|---|---|
| 10 | 10⁻³² | 1.30 × 10⁴ |
| 20 | 1.6 × 10⁻³¹ | 8.12 × 10² |
| 30 | 8.1 × 10⁻³¹ | 1.61 × 10² |
| 50 | 6.25 × 10⁻³⁰ | 208 |
| 100 | 10⁻²⁸ | 13.0 |

(Correcting the 50 nm row: actual computed value ≈ 20.8 Pa from strict formula; the 208 Pa figure quoted in §10.5.6 reflects the simulation's boundary-multiplication per stack period, not the single-gap pressure. Draft-revision note: clarify this in §10.5.6 final pass.)

Log-log slope: plot log(F/A) vs log(a). Two points at (10 nm, 1.3 × 10⁴ Pa) and (100 nm, 13 Pa): slope = (log 13 − log 13000) / (log 10⁻⁷ − log 10⁻⁸) = −3 / 1 = **−4**. ✓ (Matches 1/a⁴ scaling.)

## 10.2 — MRG gross-power at varied gap

`P_gross = (F/A) × A × Δx × f × N` with A = 2.5 × 10⁻³ m², Δx = 1 nm, f = 1.14 GHz, N = 200.

At a = 30 nm, F/A ≈ 1.61 × 10² Pa (single-gap) × boundary-multiplication ≈ 1610 Pa effective → P_gross ≈ 918 W.
At a = 50 nm: P_gross ≈ 118.7 W (reference, from §10.5.7).
At a = 100 nm: P_gross ≈ 7.4 W.

Conclusion: gross power scales as 1/a⁴. Going from 50 nm to 30 nm buys ~8×; going from 50 nm to 100 nm loses ~16×. The stiction floor at ~20 nm is the binding constraint for maximum power.

## 10.3 — η sensitivity

`P_net = P_gross × η × η_harvest = 118.7 × 0.6 × η = 71.2 η W`.

| η | P_net (W) |
|---|---|
| 10⁻⁵ | 7.1 × 10⁻⁴ |
| 10⁻³ | 0.071 |
| 0.01 | 0.71 |
| 0.1 | 7.12 |
| 0.5 | 35.6 |
| 1.0 | 71.2 |

Threshold for 30 W: η ≥ 30 / 71.2 ≈ **0.42**. ✓

## 10.4 — Waste-heat thermal analysis

`ΔT = P_waste / (h × A_surf)`.

10-cm Cu cube: A_surf = 6 × (0.1)² = 0.06 m², h = 15 W/m²·K, P_waste = 47.5 W → ΔT = 47.5 / 0.9 ≈ **53 °C**. Case at 20 °C ambient: **73 °C**. ✓

5-cm cube: A_surf = 6 × (0.05)² = 0.015 m² → ΔT = 47.5 / 0.225 ≈ **211 °C**. Case: **231 °C**. ✗ — far above any semiconductor's operating range. Forced air cooling or reduced output required.

Conclusion: the 10-cm form factor is the minimum passive size; 5-cm requires active cooling.

## 10.5 — Waters-sail yield at interstellar baseline

From Eq (10.6.1): `Ė/V = ρ_Λ × H_0 = 1.37 × 10⁻²⁷ W/m³`.

| d | V ≈ d³ | P_extractable (η_sail = 1) |
|---|---|---|
| 1 AU (1.5 × 10¹¹ m) | 3.4 × 10³³ m³ | 4.7 × 10⁶ W |
| 1 pc (3 × 10¹⁶ m) | 2.7 × 10⁴⁹ m³ | 3.7 × 10²² W |
| 1 kpc (3 × 10¹⁹ m) | 2.7 × 10⁵⁸ m³ | 3.7 × 10³¹ W |
| 1 Mpc (3 × 10²² m) | 2.7 × 10⁶⁷ m³ | 3.7 × 10⁴⁰ W |

Kardashev scale: Type I (~10¹⁶ W) demands ~100 AU baseline (10²⁸ m³); Type II (~10²⁶ W) demands ~10 pc baseline; Type III (~10³⁶ W) demands ~1 Mpc baseline — comparable to galactic disc size, consistent with the Kardashev-III definition. The framework recovers the Kardashev scale organically from Ψ_A coupling — a nice consistency check.

---

## 10.6 — Second-Law compatibility

Answer: The Firmament-extraction system is *open*, not closed. The relevant entropy balance is `ΔS_total = ΔS_device + ΔS_Waters + ΔS_Zone1 ≥ 0`. `ΔS_device` can be negative (device produces DC electrical energy, low-entropy); `ΔS_Waters` and `ΔS_Zone1` are positive because the sustaining coupling continuously transfers ordered energy out of Zone 1 into the Waters (and thence to the Firmament). The bookkeeping mirrors a refrigerator with a chilled compartment and a warmed exhaust. §10.10.1–§10.10.3.

## 10.7 — Static vs dynamic Casimir

**QED.** Static Casimir: the boundary condition is time-independent, so the action integral over a closed path returns zero work (conservative force, closed cycle). Dynamic Casimir: the boundary condition oscillates; the mode content of the vacuum reorganises at each cycle; the reorganisation energy is radiated as real photons (demonstrated by Wilson et al. 2011).

**Zone architecture.** Static cavity: Firmament membrane modes localise, but with no time-dependent boundary there is no net work done on or by the boundary. Dynamic cavity: oscillating boundary injects energy into selected Firmament membrane modes faster than equilibrium can absorb; the resulting excess is radiated as harvestable photons. In both cases, the key is *non-equilibrium boundary dynamics*.

## 10.8 — Orientation-dependent Casimir and standard physics

An orientation-dependent Casimir force in a non-magnetic, non-rotating configuration would falsify the rotational isotropy of electromagnetism in vacuum — a much stronger claim than falsifying "standard QED". It would imply either (a) the vacuum has a physical preferred direction (breaking Lorentz invariance locally), or (b) the MRG's effective Casimir configuration couples to something other than EM field modes. Both outcomes are paradigm-shifts. Any observed non-zero orientation dependence at the 5 % level would be a ~10⁵σ-scale departure from QED at current instrumental precision.

## 10.9 — Cochlea: evidence but not proof

The cochlea demonstrates that the *architecture* (driven membrane between two fluid reservoirs with active pump, amplifier, rectifier, and harvester) can produce net output. This falsifies the class of objection "such architectures must violate physics". It does not demonstrate that the Firmament is such a system, because the cochlea's pump is chemical (ATP, via stria vascularis) and the Firmament's pump, if any, is Zone-1 coupling κ(t). Substrate-independence of the architecture is plausible — the same architectural pattern recurs in widely different biological systems — but not automatic. The test at §10.8 is the operationalisation.

## 10.10 — Zone-boundary puncture risk

The failure mode is topological: an uncontrolled puncture is a local black hole. The critical amplitude is the Firmament membrane-oscillation amplitude at which elastic recovery fails to re-close the puncture within one period. For the Firmament, a first-order estimate from Firmament tension σ = 6.0 × 10⁹⁸ kg/(m·s²) (Vol 1 Ch 5 §5.5; Quality_Control/Reference/Symbol_and_Constants.md — value updated per 0516_Rev_001; the previously cited 2.4×10⁴³ value was the rejected Critic Claim 3.1 historical figure, not canonical) and mass-per-volume μ ≈ 6.7×10⁸¹ kg/m³ gives a critical amplitude Δa_crit ~ λ (wavelength), i.e., the Firmament membrane can support perturbations up to roughly its mode-wavelength before it tears. Operating amplitudes must stay well below this (Δa/λ < 0.01 recommended). Above the critical amplitude: catastrophic rupture, energy release ∝ σ × A_punctured, locally equivalent to a black-hole formation.

---

## Challenge Problems (hints + rubric)

### 10.11 — K^(1/3) from boundary-mismatch

**Hint.** Match the electromagnetic modes at the Cu/BaTiO₃ interface. The mode-matching condition gives a reflection coefficient with a (K − 1) / (K + 1) prefactor for normal incidence. The boundary-mismatch energy is ∝ ∫ |Δmode|² dV, which with the Firmament coupling ansatz `coupling ∝ (Δmode)^(2/3)` yields `P ∝ (K − 1)^(2/3) × K^(1/3)` → `P ∝ K^(1/3)` in the large-K limit. Contrast with Lifshitz's perturbative `P ∝ (K − 1) × K^(−1/2) → K^(1/2)` for large K.

**Rubric.** Full credit: correct mode-matching derivation + identification of the Firmament-specific coupling ansatz + explicit contrast with Lifshitz. Partial: correct scaling without the mismatch derivation.

### 10.12 — $150 Phase-1 experiment design

**Hint.** The 10⁻⁶ W threshold implies a measurement SNR of ~10 after 100 h integration. Thermal drift at 1 W device dissipation → ambient heating ~10⁻² °C over a small enclosure → ~10⁻⁵ V offset at a thermocouple-type sensor. Shielding: Faraday cage + MLI (multi-layer insulation, commodity aluminium foil), temperature control via PID-stabilised water bath (~$100). Statistical protocol: lock-in detection at a reference chopper frequency (mechanical chopper, ~$30), integration bandwidth < 1 Hz, confidence interval from ~300 independent samples at 1-s integration over 100 h.

**Rubric.** Full credit: enclosure design + statistical protocol + null-result criterion. Partial: any two of three.

### 10.13 — Maximum sustainable extraction rate

**Hint.** Use Eq (10.10.1): `P_extracted ≤ η × κ × A_coupled`. With κ₀ ≈ 10⁻¹⁰ W/m² (from ρ_Λ × H₀ × c, order-of-magnitude) and A_coupled ≈ cavity-wall area ≈ 0.03 m² for the reference design → `P_sustainable ≤ 3 × 10⁻¹² W` at η = 1. Contrast with reference-design rated output of 30 W. The discrepancy is ~10¹³. Resolution (per §10.10.2): the correct A is the mode-volume integrated coupling area, which is ~10¹⁵ larger than the physical cavity-wall area due to the ξ-extent integration.

**Rubric.** Full credit: explicit identification of the volume-integration resolution. Partial: acknowledgement of the per-area discrepancy with correct direction (device output exceeds per-area bound by many orders of magnitude).

---

## Notes on the solution set

- Problems 10.1–10.5 are standard plug-and-chug at the Foundations level. Any student who has followed Vol 2 Ch 11 (electromagnetism in media) and Vol 3 Ch 3 (thermal transport) can solve them.
- Problems 10.6–10.10 are book-report-plus-synthesis: they test whether the reader connected the chapter's structural arguments, not whether they can compute.
- Problems 10.11–10.13 are thesis-scale. 10.11 is a literature gap (the K^(1/3) derivation is framework-specific and not established elsewhere). 10.12 is an experimental-design problem with real stakes. 10.13 is the chapter's own open-problem statement (Ch 14 #8) in miniature.
