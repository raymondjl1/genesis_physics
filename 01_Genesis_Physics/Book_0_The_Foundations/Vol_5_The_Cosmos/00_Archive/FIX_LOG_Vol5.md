# Vol 5 Fix Log
## Rev. 2026-05-14 — Phase 1 (Error Corrections) and Phase 2 (Honest Labeling)

---

### Ch01: Einstein Field Equations Recovered

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 1 | §1.1.1, after metric Eq (5.1.1) | Added provisional label for warp functions A(ξ,η) and B(ξ,η): "Warp functions used without full 2D derivation from 6D Einstein equations. Designated Open Problem 1.WF." | Fix instruction: add warp function provisional label. Functions are used in factorized form; simultaneous derivation in both ξ,η not carried out in Vol 5. |
| 2 | §1.1.1 | No ξ_A correction needed: ξ_A does not appear as a numerical value in the accessible Ch01 text. | Verification: searched chapter; no 1.4×10²⁶ m reference found. |

---

### Ch02: Classical Tests

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 3 | (no edit) | No ξ_A correction needed; chapter does not use ξ_A numerically in the reviewed text. | Verification: searched chapter; ξ_A does not appear as a raw value. |
| 4 | (no edit) | LIGO O3 echo note not applicable here; chapter covers classical GR tests, not echoes. | Ringdown echoes are not predicted in Ch02; note belongs in Ch05. |

---

### Ch03: Gravitational Waves

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 5 | (no edit) | Ringdown echoes are not explicitly predicted in Ch03 (they are deferred to Ch05). No LIGO O3 note added here. | Fix instruction: "If ringdown echoes are predicted here, add..." — they are not; Ch03 deals with GW generation and waveforms, not echo predictions. |

---

### Ch04: Strong-Field Gravity

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 6 | (no edit) | Warp functions A(ξ,η) and B(ξ,η) are used in §4.8 (FTL mechanism) with explicit acknowledgment they come from Vol 1 Ch 4 and are not re-derived. No additional provisional label required beyond what is already in the text. Problem set confirmed present at §(Problem Sets). | Warp functions referenced as inherited from Vol 1; already labeled. Problem set confirmed. |

---

### Ch05: Black Holes as Zone Infrastructure

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 7 | §5.8.2 (Prediction 1: Ringdown echoes), after Eq (5.5.31) | Added LIGO O3 null result observational status note: "LIGO O3 did not detect post-merger echoes. Constraint on breach reflectivity from null result designated RT-5.ECHO." | Fix instruction: add LIGO O3 echo null result note. Review found this was missing; current text says "results as of 2024 are inconclusive" which understates the O3 null result. |
| 8 | §5.6.2, after entropy counting equation | Added Gauss-Bonnet note: "Formal proof that Firmament topology produces correct Gauss-Bonnet factor in mode count designated RT-5.GB." | Fix instruction: add RT-5.GB note. Gauss-Bonnet factor of 1/2 is asserted (inherited from Vol 1 §11.4) rather than proved within Vol 5. |

---

### Ch06: The Information Paradox Resolved

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 9 | After Theorem 5.6.3 discussion paragraph | Added note: "H_bulk information preservation mechanism is a theoretical proposal consistent with zone architecture, not experimentally confirmed. Its prediction (information recovery in Hawking correlations) is not yet observationally tested." | Fix instruction: if information preservation reads as proven fact, add note. Chapter intro calls it a "theorem," which is mathematically correct; note distinguishes mathematical theorem from observational confirmation. |

---

### Ch07: Singularity Resolution

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 10 | (no edit) | Problem set confirmed present at §7.10. No additional fixes required. | Problem set present; warp function provisional label not required in this chapter (singularity resolution does not use the factorized warp function approximation in the way Ch01/Ch04 do). |

---

### Ch08: Zone Cosmological Model

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 11 | §8.6.3, after energy-budget table | Added RT-5.ΩA note: "Whether Ω_A = 0.684 is a prediction or a consequence of normalization conventions in warp-factor integrals is not fully transparent. Research Task RT-5.ΩA: verify result does not depend on tuning of Waters Above boundary conditions." | Fix instruction: add Ω_A transparency note. |
| 12 | (no edit) | ξ_A in Ch08 appears as "ξ_A ≈ 3.0×10²⁶ m" (line 185), consistent with canonical value. No correction needed. | Verification: Ch08 already uses 3.0×10²⁶ m. |

---

### Ch09: The CMB and Early Universe

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 13 | §9.9 header | Added Parameter Disclosure box: "A_s = 2.1×10⁻⁹ and n_s = 0.965 adopted from Planck 2018, not derived from zone architecture. CMB comparison is consistency check, not prediction. True zone-architecture CMB predictions (A_s, n_s from first principles) designated RT-5.CMB." | Fix instruction: CMB amplitude and tilt disclosure. Chapter §9.9 already says A_s is inherited; the disclosure box makes this prominent. |
| 14 | §9.12.4 | Added RT-5.H₀ note: "Hubble tension prediction requires computing ΔH₀ from specific κ-transition parameters. Until completed (RT-5.H₀), Hubble tension cannot be claimed as zone architecture prediction. Structural argument compelling but unquantified." | Fix instruction: Hubble tension note. Ch09 §9.12 correctly classifies this as a Conjecture (L18); note makes the unquantified status explicit. |

---

### Ch10: Large-Scale Structure

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 15 | §10.0 intro (after the "numerically identical" paragraph) | Added prominent ΛCDM degeneracy note box: "Large-scale structure predictions degenerate with ΛCDM when A_s and n_s adopted from Planck. Distinguishing zone architecture from ΛCDM requires independent derivation of A_s and n_s (RT-5.CMB)." | Fix instruction: make ΛCDM degeneracy note prominent. Chapter already states this in its intro; added blockquote to make it stand out. |

---

### Ch11: Dark Matter and Dark Energy Quantified

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 16 | §11.10 Falsifier (ii) | Added sentence: "This is the primary falsification test for the Waters Below dark matter identification. Any confirmed dark matter direct detection signal (σ_SI > 0 at nuclear recoil level) would falsify this model." | Fix instruction: present σ_SI = 0 prediction as key experimental test with explicit falsifier statement. |
| 17 | §11.1.4, after density parameters table | Added note on 68/27/5 split: "Classified as prediction derived from zone geometry if matching parameters fixed at non-cosmological scales (Vol 1 §6.7). If warp-factor normalizations were adjusted to reproduce Ω_A = 0.684, result would be consistency check. Distinction tracked in RT-5.ΩA." | Fix instruction: label 68/27/5 split as prediction or consistency check. |

---

### Ch12: The Starlight Problem and Chronology

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 18 | Section 2.1 header | Added hermeneutics context note at start of Section 2.1: "The following section presents biblical-interpretive context for the two-phase expansion hypothesis. This material supplements the physical argument and may be of interest to theologically engaged readers, but the physical hypothesis stands independently." | Fix instruction: move hermeneutics note to start of Hebrew grammatical analysis section. |
| 19 | Line 140 (theorem heading) | Renamed "Theorem 5.12.1 (Two-Phase Expansion Structure)" to "Physical Interpretation 5.12.1 (Two-Phase Expansion Structure)". | Fix instruction CRITICAL: theology mislabeled as physics theorem. Hebrew grammar cannot prove a physical theorem. |
| 20 | After Physical Interpretation 5.12.1 heading | Added EPISTEMOLOGICAL NOTE (Rev. 2026-05-14): "This 'Physical Interpretation' is not a theorem in the mathematical sense. Two-phase expansion structure is a physical hypothesis motivated by zone architecture and biblical interpretation. Biblical grammatical analysis provides theological motivation but does not constitute a physical proof. Physical validation designated Research Task RT-5.2PH." | Fix instruction CRITICAL: add epistemological warning after theorem heading. |
| 21 | Renamed "Proof sketch" to "Interpretive argument" | Changed "*Proof sketch:*" to "*Interpretive argument:*" to reflect that the argument is hermeneutical, not mathematical. | Consistent with renaming theorem → Physical Interpretation. |
| 22 | Section 4.1 header | Added unfalsifiability note: "The mature creation principle is unfalsifiable by construction — any observation can be accommodated by positing appropriate initial conditions at creation. It is therefore a theological principle that cannot function as a physical mechanism in a falsifiable theory." | Fix instruction: mature creation unfalsifiability note. |

---

### Ch13: Fine Structure Constant from First Principles

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 23 | After b_eff Figure 5.13.5 description | Added b_eff derivation chain note: "b_eff = 9.05 computed from Standard Model particle content (Vol 4). Correct derivation chain Vol 4 → Vol 5 Ch 13. b_eff computed from zone-topology mode counting, not fitted to observed α. This is the series' cleanest result." | Fix instruction: add b_eff note. Chapter already states this; note makes the derivation chain and non-fitted status explicit. |
| 24 | ξ_A value | ξ_A = 3.0×10²⁶ m confirmed in Chapter 13 text (Eq 5.13.4). No correction needed. | Verification: Ch13 uses canonical 3.0×10²⁶ m value correctly. This is the crown jewel chapter; preserved exactly. |

---

### Ch14: Critical Density and Cosmological Parameters

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 25 | (no edit) | ξ_A confirmed as 3.0×10²⁶ m throughout (lines 185, 201, 409, etc.). No correction needed. | Verification: Ch14 uses 3.0×10²⁶ m correctly. |
| 26 | (no edit) | Problem set confirmed present at §14.10. No addition needed. | Problem set at §14.10 with 9+ problems. |

---

### Ch15: Why These Constants?

| # | Location | Change | Reason |
|---|----------|--------|--------|
| 27 | Table line 67 | ξ_A value changed from 1.4×10²⁶ m to 3.0×10²⁶ m. | Fix instruction CRITICAL: ξ_A inconsistency. Ch15 used Hubble radius; canonical value is particle horizon 3.0×10²⁶ m (consistent with Ch13). |
| 28 | After table, §15.1 | Added correction note: "[Corrected: ξ_A = 3.0×10²⁶ m (particle horizon), consistent with Ch 13 canonical value. Earlier draft used Hubble radius (1.4×10²⁶ m). — Rev. 2026-05-14]" | Fix instruction: add explicit correction note with date. |
| 29 | §15.2.4, warp exponent calculation (Eq 15.17–15.18) | Updated ratio η_B/ξ_A from 0.929×10⁻⁴¹ to 4.33×10⁻⁴² (corrected for ξ_A = 3.0×10²⁶ m). Updated λ calculation: λ ≈ 0.967 ≈ 1. | Propagated ξ_A correction through warp exponent derivation. |
| 30 | §15.2.5, Step 2 (Eq 15.20) | Updated (η_B/ξ_A)² from (1.4×10²⁶)⁻² to (3.0×10²⁶)⁻² giving 1.88×10⁻⁸³ (was 8.63×10⁻⁸³). Added correction note. | Propagated ξ_A correction through numerical result. |
| 31 | §15.2.5, Step 3 (Eq 15.21) | Updated ℏ_derived from 1.896×10⁻³⁷ to 4.13×10⁻³⁸ J·s. | Propagated corrected suppression factor. |
| 32 | §15.2.5, Eq 15.23 (ratio) | Updated ℏ_derived/ℏ_obs from 1.80×10⁻³ to 3.92×10⁻⁴. | Propagated corrected ℏ_derived. |
| 33 | §15.2.6 "Why is ℏ so small?" paragraph | Updated ratio description from "~10⁻⁴¹, square is 10⁻⁸²" to "~4.3×10⁻⁴², square is ~1.9×10⁻⁸³". Added correction note. | Propagated ξ_A correction to explanatory text. |
| 34 | ξ_A in §15.3 (G derivation) | Updated "ξ_A ≈ 1.4×10²⁶ m" to "ξ_A ≈ 3.0×10²⁶ m" in warp factor section. | Propagated ξ_A correction. |
| 35 | Eq 15.37 (naive V_extra) | Updated V_extra_naive from 1.4×10²⁶ × 1.3×10⁻¹⁵ ≈ 1.8×10¹¹ m² to 3.0×10²⁶ × 1.3×10⁻¹⁵ ≈ 3.9×10¹¹ m². | Propagated ξ_A correction. |
| 36 | §15.2.3, before Bohr-Sommerfeld step | Added DIMENSIONAL CORRECTION note (Rev. 2026-05-14): "Vortex action formula S = ση_B³/c dimensional check [kg s⁻²][m³][m s⁻¹]⁻¹ = [kg m² s⁻¹] = action (J·s) as shown in Eq 15.7. A careful dimensional analysis of vortex action geometry confirming the full coefficient is designated CT-5.ℏ. The ℏ derivation is provisional pending CT-5.ℏ." | Fix instruction: add dimensional correction note. Note: the chapter's own dimensional check (Eq 15.7) confirms [M L² T⁻¹] = action, not momentum. The note designates CT-5.ℏ for rigorous coefficient verification. |
| 37 | §15.2.4, after λ ≈ 1 paragraph | Added λ calibration note: "The warp exponent λ is fitted to reproduce the observed ℏ. It is not derived from the 6D field equations. This is a calibration, not a prediction, pending a derivation of λ from the 6D action." | Fix instruction: add λ calibration note. Chapter claims λ ≈ 1 is "geometrically natural" but the value is back-derived from requiring the correct ℏ suppression. |

---

## Summary of Research Tasks Designated

| Task ID | Chapter | Description |
|---------|---------|-------------|
| Open Problem 1.WF | Ch01 | Full 2D warp profile A(ξ,η), B(ξ,η) derivation from 6D Einstein equations |
| RT-5.ECHO | Ch05 | Quantitative upper bound on Firmament breach reflectivity from LIGO O3 null result |
| RT-5.GB | Ch05 | Formal proof that Firmament topology gives correct Gauss-Bonnet factor in entropy mode count |
| RT-5.ΩA | Ch08, Ch11 | Verify Ω_A = 0.684 result is fitting-free; display intermediate integral values |
| RT-5.CMB | Ch09, Ch10 | Derive A_s and n_s from zone architecture first principles |
| RT-5.H₀ | Ch09 | Compute ΔH₀ from specific κ-transition parameters of Sabbath Boundary |
| RT-5.2PH | Ch12 | Derive two-phase expansion transition time and rates from zone field equations |
| CT-5.ℏ | Ch15 | Rigorous dimensional analysis of vortex action geometry for ℏ derivation coefficient |

---

*Fix log generated Rev. 2026-05-14. All Phase 1 (error corrections) and Phase 2 (honest labeling) edits applied.*
