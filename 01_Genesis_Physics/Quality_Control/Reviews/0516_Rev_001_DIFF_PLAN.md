# 0516_Rev_001 — σ (membrane tension) units fix — DIFF PLAN

**Reviewers:** REVIEWER-01 (Physicist) + REVIEWER-04 (Consistency Auditor)
**Status:** PLAN ONLY — no edits performed.
**Canonical:** σ = **6.0×10⁹⁸ kg/(m·s²)** (≡ N/m² ≡ Pa ≡ J/m³, dim [ML⁻¹T⁻²]).
**Rule:** Replace `kg/s²` → `kg/(m·s²)` everywhere σ appears as a 3-brane tension. Keep `kg/(m·s²)` if already correct. Replace alternative spellings (`kg·m⁻¹·s⁻²`, `kg/m/s²`) if they appear correctly — flag only.

OOS = out of scope (under `00_Archive/`, `_pre-comprehensive`, `Quality_Control/Reviews/**`, `Quality_Control/Reviewers/**`). Those are NOT included below even when they contain hits.

---

## Volume 1 — Architecture of Reality

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_1_Architecture_of_Reality/Manuscript/Ch_05_The_Firmament_Manifold/Ch05_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 727 | `- The membrane tension $\sigma \approx 6.0 \times 10^{98}$ kg/s² and mass density $\mu \approx 6.7 \times 10^{81}$ kg/m³` | `- The membrane tension $\sigma \approx 6.0 \times 10^{98}$ kg/(m·s²) and mass density $\mu \approx 6.7 \times 10^{81}$ kg/m³` |
| 759 | `**Problem 5.4.** ... $\sigma = 6.0 \times 10^{98}$ kg/s² and $\mu = 6.7 \times 10^{81}$ kg/m³` | `**Problem 5.4.** ... $\sigma = 6.0 \times 10^{98}$ kg/(m·s²) and $\mu = 6.7 \times 10^{81}$ kg/m³` |
| 767 | `**Problem 5.8.** ... $\sigma = 6.0 \times 10^{98}$ kg/s² and $\ell_{\text{eff}} = 8.96 \times 10^{-29}$ m.` | `**Problem 5.8.** ... $\sigma = 6.0 \times 10^{98}$ kg/(m·s²) and $\ell_{\text{eff}} = 8.96 \times 10^{-29}$ m.` |

(Lines 366, 485 already use canonical units — no edit. Lines 487–495 derivation-status box uses the correct `kg/(m·s²)` form throughout — no edit.)

**Note Prob 5.4 / Prob 5.8:** task brief flagged Prob 5.4 as "off-value." Value is in fact already canonical (6.0×10⁹⁸); the defect is the unit. After the unit swap the worked answer (c² = σ/μ, % deviation < 1%) stands unchanged.

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_1_Architecture_of_Reality/Manuscript/ProblemSets_Ch07_11_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 626 | `If σ = 10⁻¹⁵ kg/m (membrane tension), η_B = 10⁻³⁵ m (boundary scale), ξ_A = 10⁻³⁷ m (amplitude scale), and β_geom ≈ 1, calculate ℏ numerically and compare to the known value.` | `If σ = 6.0×10⁹⁸ kg/(m·s²), η_B = 1.3×10⁻¹⁵ m, ξ_A = 3.0×10²⁶ m, and β_geom ≈ 1 (taking the canonical zone-architecture parameters; see Symbol_and_Constants.md), calculate ℏ numerically using Eq. (4.1.12) (or the simplified form ℏ ≈ σ η_B³/(2c) × (η_B/ξ_A)² × β_geom) and compare to the measured value 1.055×10⁻³⁴ J·s.` |

**RISK:** PS-10.3 originally used pedagogical "toy" numbers (10⁻¹⁵ kg/m with the wrong unit, 10⁻³⁵ m, 10⁻³⁷ m — note ξ_A < η_B in the original, which is *backwards*). Replacing with canonical parameters changes the numerical answer the student is expected to compute. Reviewer should also revise the solution key (if one exists downstream) and consider whether this problem should remain "compute ℏ from canonical parameters" (consistent with Vol 1 Ch 10) or be re-cast as a unit-checking exercise. **Recommend canonical-parameter recast as above.**

---

## Volume 2 — Forces and Fields

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/Manuscript/Ch_11_The_Force_Landscape/Ch11_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 78 | `\| Firmament tension \| σ ≈ 6.0×10⁹⁸ kg/s² \| Sets speed of light, Planck scale \|` | `\| Firmament tension \| σ ≈ 6.0×10⁹⁸ kg/(m·s²) \| Sets speed of light, Planck scale \|` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/Back_Matter/APPENDIX_B_Experimental_Data_Tables.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 30 | `\| Membrane surface tension (6D) \| σ \| 6.0 × 10⁹⁸ \| kg/s² \| ±10% \| ...` | `\| Membrane surface tension (6D) \| σ \| 6.0 × 10⁹⁸ \| kg/(m·s²) \| ±10% \| ...` |

---

## Volume 3 — Matter and Motion

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_3_Matter_and_Motion/Manuscript/Ch_07_The_Origin_of_Mass/Ch07_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 21 | `...where the membrane tension $\sigma \approx 6 \times 10^{98}$ kg/s² creates...` | `...where the membrane tension $\sigma \approx 6 \times 10^{98}$ kg/(m·s²) creates...` |
| 158 | `The Firmament is a domain wall with tension $\sigma = 6.0 \times 10^{98}$ kg/s² (Vol 1, Eq. 1.5.28).` | `The Firmament is a domain wall with tension $\sigma = 6.0 \times 10^{98}$ kg/(m·s²) (Vol 1, Eq. 1.5.28).` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_3_Matter_and_Motion/Back_Matter/Problem_Sets_with_Solutions.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 268 | `...the membrane tension $\sigma \approx 6\times 10^{98}$ kg/s²...` | `...the membrane tension $\sigma \approx 6\times 10^{98}$ kg/(m·s²)...` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_3_Matter_and_Motion/Back_Matter/APPENDIX_B_Experimental_Mechanics_Data.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 28 | `With $\sigma \approx 6\times 10^{98}$ kg/s² and $L_{\text{eff}}$ fixed by (2.9.11), the zone-derived value is $G_4 = 6.674\times 10^{-11}$ m³/(kg·s²)` | `With $\sigma \approx 6\times 10^{98}$ kg/(m·s²) and $L_{\text{eff}}$ fixed by (2.9.11), the zone-derived value is $G_4 = 6.674\times 10^{-11}$ m³/(kg·s²)` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_3_Matter_and_Motion/Back_Matter/APPENDIX_A_Key_Results_from_Volumes_1_and_2.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 71 | `$$\sigma \approx 6 \times 10^{98}\;\text{kg/s}^2 \tag{1.5.74}$$` | `$$\sigma \approx 6 \times 10^{98}\;\text{kg/(m·s}^2\text{)} \tag{1.5.74}$$` |

---

## Volume 4 — The Quantum World

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Manuscript/Ch_01_Why_the_Universe_is_Quantum/Ch01_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 97 | `...characterized by a tension $\sigma = 6.0 \times 10^{98}$ kg/s² and a surface mass density $\mu = 6.7 \times 10^{81}$ kg/m³.` | `...characterized by a tension $\sigma = 6.0 \times 10^{98}$ kg/(m·s²) and a surface mass density $\mu = 6.7 \times 10^{81}$ kg/m³.` |
| 226 | `...With the canonical parameters ($\sigma = 6.0\times 10^{98}$ kg/s², $\eta_B \approx 1.3\times 10^{-15}$ m...` | `...With the canonical parameters ($\sigma = 6.0\times 10^{98}$ kg/(m·s²), $\eta_B \approx 1.3\times 10^{-15}$ m...` |
| 383 | `**Problem 1.1.** The Firmament tension is $\sigma = 6.0 \times 10^{98}$ kg/s² and the surface mass density is $\mu = 6.7 \times 10^{81}$ kg/m³.` | `**Problem 1.1.** The Firmament tension is $\sigma = 6.0 \times 10^{98}$ kg/(m·s²) and the surface mass density is $\mu = 6.7 \times 10^{81}$ kg/m³.` |

(Line 282 sits inside the long Derivation Status quoteblock. Scan for any `kg/s²` inside it; current canonical text reads "$\sigma = 6.0 \times 10^{98}$" without units on line 282 — leave alone. If executor finds a `kg/s²` there, apply the same swap.)

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Manuscript/Ch_02_The_Schrodinger_Equation_Derived/Ch02_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 67 | `- $\sigma = 6.0 \times 10^{98}$ kg/s² — the Firmament's tension, from (1.5.3).` | `- $\sigma = 6.0 \times 10^{98}$ kg/(m·s²) — the Firmament's tension, from (1.5.3).` |
| 350 | `...(units of $[\sigma] = $ kg/s²) and "energy per defect" (units of J)...` | `...(units of $[\sigma] = $ kg/(m·s²)) and "energy per defect" (units of J)...` |
| 707 | `Verify that $c^{2} = \sigma/\mu$ with $\sigma = 6.0 \times 10^{98}$ kg/s² and $\mu = 6.7 \times 10^{81}$ kg/m³ gives the speed of light.` | `Verify that $c^{2} = \sigma/\mu$ with $\sigma = 6.0 \times 10^{98}$ kg/(m·s²) and $\mu = 6.7 \times 10^{81}$ kg/m³ gives the speed of light.` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Back_Matter/APPENDIX_B_Particle_Data_Tables.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 54 | `\| Newton's constant \| $G$ \| $6.674\,30(15)\times 10^{-11}$ m³/kg/s² \| CODATA 2022 \| Derived (3.2.8) \|` | `\| Newton's constant \| $G$ \| $6.674\,30(15)\times 10^{-11}$ m³/(kg·s²) \| CODATA 2022 \| Derived (3.2.8) \|` |

**RISK:** Line 54 is *Newton's G*, not σ. The string `m³/kg/s²` is ambiguous but conventionally read as `m³/(kg·s²)`. Optional cosmetic clean-up; not strictly in scope for the σ task. Flag and let the executor decide.

---

## Volume 5 — The Cosmos

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/Manuscript/Ch_14_Critical_Density_and_Cosmological_Parameters/Ch14_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 104 | `where σ = 6.0 × 10⁹⁸ kg/s² is the membrane tension (Vol 1 Ch 5)...` | `where σ = 6.0 × 10⁹⁸ kg/(m·s²) is the membrane tension (Vol 1 Ch 5)...` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/Manuscript/Ch15_Why_These_Constants/Ch15_Why_These_Constants_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 65 | `\| Brane tension \| σ \| 6.0 × 10⁹⁸ kg/s² \| Vol 1, Ch 5 \|` | `\| Brane tension \| σ \| 6.0 × 10⁹⁸ kg/(m·s²) \| Vol 1, Ch 5 \|` |
| 264 | `Its tension σ ≈ 6 × 10⁹⁸ kg/s² is an almost incomprehensibly large number.` | `Its tension σ ≈ 6 × 10⁹⁸ kg/(m·s²) is an almost incomprehensibly large number.` |
| 629 | `...is an elastic membrane with tension σ ≈ 6 × 10⁹⁸ kg/s² embedded in a 6D spacetime...` | `...is an elastic membrane with tension σ ≈ 6 × 10⁹⁸ kg/(m·s²) embedded in a 6D spacetime...` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/Manuscript/Ch_04_Strong_Field_Gravity/Ch04_DRAFT.md` — **PROSE-REWRITE RISK**

| Line | BEFORE | AFTER (proposed) |
|------|--------|-------|
| 448 | `where $\sigma$ is the membrane tension and $\Delta\eta$ is the perpendicular excursion. From Vol 1 Ch 5 §1.5.3, the membrane tension is $\sigma \sim 10^{98}$ J/m — an enormous value set by the bulk cosmological constant and the Planck mass.` | `where $\sigma$ is the membrane tension and $\Delta\eta$ is the perpendicular excursion. From Vol 1 Ch 5 §1.5.3, the membrane tension is $\sigma \approx 6.0 \times 10^{98}$ kg/(m·s²) (equivalently, energy per unit 3-volume; dim [ML⁻¹T⁻²]) — an enormous value set by the bulk cosmological constant and the Planck mass.` |
| 645 | `- The membrane tension $\sigma \sim 10^{98}$ J/m is Vol 1 Ch 5 §1.5.3.` | `- The membrane tension $\sigma \approx 6.0 \times 10^{98}$ kg/(m·s²) (energy per unit 3-volume) is Vol 1 Ch 5 §1.5.3.` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/Manuscript/Ch_05_Black_Holes_as_Zone_Infrastructure/Ch05_DRAFT.md` — **PROSE-REWRITE RISK**

| Line | BEFORE | AFTER (proposed) |
|------|--------|-------|
| 36 | `Numerically, $\sigma \approx 6.0 \times 10^{98}$ J/m (AXIOM_MEMBRANE_MECHANICS_v2.md §5, quoted in Vol 1 §5.3).` | `Numerically, $\sigma \approx 6.0 \times 10^{98}$ kg/(m·s²) (equivalently J/m³ = Pa for a 3-brane tension; see AXIOM_MEMBRANE_MECHANICS_v2.md §5, quoted in Vol 1 §5.3).` |
| 590 | `...$\sigma_\infty = 6.0 \times 10^{98}$ J/m and $\mu = 6.7 \times 10^{81}$ kg/m³ from Vol 1 §5.3...` | `...$\sigma_\infty = 6.0 \times 10^{98}$ kg/(m·s²) and $\mu = 6.7 \times 10^{81}$ kg/m³ from Vol 1 §5.3...` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/Back_Matter/Problem_Sets_with_Selected_Solutions.md` — **PROSE-REWRITE RISK**

| Line | BEFORE | AFTER |
|------|--------|-------|
| 152 | `...$\sigma \approx 6.0 \times 10^{98}$ J/m and $\mu \approx 6.7 \times 10^{81}$ kg/m³...` | `...$\sigma \approx 6.0 \times 10^{98}$ kg/(m·s²) and $\mu \approx 6.7 \times 10^{81}$ kg/m³...` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/Back_Matter/APPENDIX_B_Cosmological_Data_Tables.md` — **PROSE-REWRITE RISK**

| Line | BEFORE | AFTER |
|------|--------|-------|
| 174 | `\| Membrane tension \| $\sigma$ \| $\approx 6.0 \times 10^{98}$ J/m \| ...` | `\| Membrane tension \| $\sigma$ \| $\approx 6.0 \times 10^{98}$ kg/(m·s²) \| ...` |

---

## Volume 6 — Predictions and Simulations

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Manuscript/Ch_05_Simulation_Methodology/Ch05_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 79 | `The membrane tension is σ = 6.0 × 10⁹⁸ kg/s². IEEE 754...` | `The membrane tension is σ = 6.0 × 10⁹⁸ kg/(m·s²). IEEE 754...` |
| 121 | `\| σ (membrane tension) \| 6.0 × 10⁹⁸ \| kg/s² \| Sets wave speed...` | `\| σ (membrane tension) \| 6.0 × 10⁹⁸ \| kg/(m·s²) \| Sets wave speed...` |
| 130 | `Numerically, with σ = 6.0 × 10⁹⁸ kg/s² and μ = 6.7 × 10⁸¹ kg/m³, one obtains v ≈ 2.993 × 10⁸ m/s = 0.9975c...` | `Numerically, with σ = 6.0 × 10⁹⁸ kg/(m·s²) and μ = 6.7 × 10⁸¹ kg/m³, one obtains v ≈ 2.993 × 10⁸ m/s = 0.9975c...` |
| 187 | `The value v = √(σ/μ) computed from σ = 6.0×10⁹⁸ kg/s² and μ = 6.7×10⁸¹ kg/m³ gives v ≈ 2.993×10⁸ m/s = 0.9975c.` | `The value v = √(σ/μ) computed from σ = 6.0×10⁹⁸ kg/(m·s²) and μ = 6.7×10⁸¹ kg/m³ gives v ≈ 2.993×10⁸ m/s = 0.9975c.` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Manuscript/Ch_07_Membrane_Vibration_Spectra/Ch07_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 35 | `- **σ = 6.0 × 10⁹⁸ kg/s²** — the membrane tension. This extraordinary number reflects the Planck-scale rigidity of the firmament...` | `- **σ = 6.0 × 10⁹⁸ kg/(m·s²)** — the membrane tension. This extraordinary number reflects the Planck-scale rigidity of the firmament...` |
| 492 | `SIGMA = 6.0e98           # kg/s²` | `SIGMA = 6.0e98           # kg/(m·s²)` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Manuscript/Ch_09_FTL_Travel/Ch09_DRAFT.md` — **CRITICAL: 50-OOM ERROR**

This chapter prints σ in three incompatible ways. 1 J/m = 1 kg/s² (force per length), which is **fifty orders below** the canonical 6.0×10⁹⁸ kg/(m·s²) for a 3-brane. The downstream worked example V₀ = σ²/(2μ) ~ 10⁹⁸ J **does not follow** from σ ~ 10⁴⁸ J/m and μ ~ 10⁻¹⁷ kg/m; the arithmetic gives ~10¹¹³ J. The whole tunneling estimate must be rerun. **Do not just unit-swap — flag for derivation rebuild.**

| Line | BEFORE | AFTER (proposed unit/value fix; arithmetic still TODO) |
|------|--------|-------|
| 1950 | `> where σ ~ 10^48 J/m is membrane tension (Vol 1, Ch 5, equation (1.5.12)), and Δη is the extra-dimensional displacement.` | `> where σ ≈ 6.0×10⁹⁸ kg/(m·s²) is membrane tension (Vol 1, Ch 5, equation (1.5.12)), and Δη is the extra-dimensional displacement.` |
| 2086 | `> where σ ~ 10^48 J/m is membrane tension and μ ~ 10^-17 kg/m is membrane mass per unit area.` | `> where σ ≈ 6.0×10⁹⁸ kg/(m·s²) is membrane tension and μ ≈ 6.7×10⁸¹ kg/m³ is membrane volume mass density (Vol 1 Ch 5 / Symbol_and_Constants.md).` |
| ~2216 / ~2224 | Worked example V₀ = σ²/(2μ) ~ 10⁹⁸ J | **DO NOT EDIT YET — RERUN ARITHMETIC.** Cells: barrier-height expression, the V₀ numeric value, any downstream tunneling probability or temperature scale that consumes V₀. Reviewer must verify that the new σ + μ (and the corrected μ units kg/m³, not kg/m) give a *physically meaningful* barrier height before publishing. |
| 2422 | `(b) ... if c² = σ/μ? Use σ ~ 10^48 J/m and estimate μ from the metric.` | `(b) ... if c² = σ/μ? Use σ ≈ 6.0×10⁹⁸ kg/(m·s²) and μ ≈ 6.7×10⁸¹ kg/m³ (Symbol_and_Constants.md).` |

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Manuscript/Ch_09_FTL_Travel/Ch09_DRAFT_Part3.md`

Identical pattern at lines **434, 570, 700, 708, 906** — apply the same edits as the corresponding lines above (the file is a split-out copy of the same chapter).

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Manuscript/Ch_10_Energy_Harvesting/Ch10_SOLUTIONS.md` — **OFF-VALUE**

| Line | BEFORE | AFTER |
|------|--------|-------|
| 93 | `...a first-order estimate from membrane tension σ ≈ 2.4 × 10⁴³ kg/s² (Vol 1 Ch 5) and mass-per-area μ gives a critical amplitude...` | `...a first-order estimate from membrane tension σ ≈ 6.0 × 10⁹⁸ kg/(m·s²) (Vol 1 Ch 5; Symbol_and_Constants.md) and mass-per-volume μ ≈ 6.7×10⁸¹ kg/m³ gives a critical amplitude...` |

**RISK:** 2.4×10⁴³ is the "Critic Claim 3.1" historical-error value (see Ch14 §14.9.4). Ch10_SOLUTIONS is *currently citing the rejected value as if canonical.* The critical-amplitude estimate Δa_crit ~ λ that follows in the same paragraph is dimensional-analysis only and likely survives the value swap, but reviewer should re-run the energy-release estimate `E ∝ σ × A_punctured` if it's quantified anywhere downstream. Also: the prose says "mass-per-area μ" which is inconsistent with the canonical μ being kg/m³ (volume density). **Decide whether to keep the kg/m³ volume density (Symbol_and_Constants.md) or introduce a separate surface density variable in this section. Recommend the former for consistency.**

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Manuscript/Ch_14_Open_Problems/Ch14_DRAFT.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 562 | `### 14.9.4  Claim 3.1: "σ ≈ 2.4 × 10^43 kg/s²" — the 76-order-of-magnitude discrepancy` | **NO EDIT** — this is a historical quote of the critic's rejected number. Leave value as-is. Unit `kg/s²` is also being quoted from the critic; leave. |
| 564 | `...gave σ ≈ 2.16 × 10⁻³³ kg/s², while the framework claimed σ ≈ 2.4 × 10^43 kg/s².` | **NO EDIT** — same rationale; quoting historical erroneous values. |

(If editorial preference is to also normalize unit-presentation in quoted text, swap `kg/s²` → `kg/(m·s²)`. But the *values* must remain to preserve the historical narrative.)

### `01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Back_Matter/APPENDIX_E_Notation_Reference.md`

| Line | BEFORE | AFTER |
|------|--------|-------|
| 395 | `\| Membrane tension \| \`σ\` \| 6.0 × 10⁹⁸ \| kg·m⁻¹·s⁻² \| Fundamental creation parameter \| 1.Ch 5 \|` | **NO EDIT** — `kg·m⁻¹·s⁻²` is the dimensionally equivalent power-form of `kg/(m·s²)`. Already correct. |

---

## Audio book (`audio book/chapters/*_clean.txt`)

These files are TTS-preprocessed transcriptions of the manuscript. The fixes mirror the manuscript edits one-for-one. Spelled-out variants (e.g. "10 to the 98") must also have their unit phrase fixed (e.g. "kg/s²" → "kg/(m·s²)"); the digit-form variants take the same swap.

### Vol 1
- `Vol_1/audio book/chapters/Ch05_clean.txt` — lines **473, 697, 727, 735** (matches Ch05_DRAFT Prob 5.4/5.8 + body)
- `Vol_1/audio book/chapters/Ch10_clean.txt` — line **742** (Problem 10.3)
- `Vol_1/audio book/chapters/ProblemSets_Ch07_11_DRAFT_clean.txt` — PS-10.3 mirror of manuscript line 626 (executor: locate by string match `σ = 10⁻¹⁵ kg/m` or `sigma = 10 to the -15 kg/m`)

### Vol 2
- `Vol_2/audio book/chapters/Ch11_clean.txt` — line **66**
- `Vol_2/audio book/chapters/APPENDIX_B_clean.txt` — line **23**
- `Vol_2/audio book/chapters/APPENDIX_B_Experimental_Data_T_clean.txt` — line **23** (duplicate of the above)

### Vol 3
- `Vol_3/audio book/chapters/Ch07_clean.txt` — lines **19, 150**
- `Vol_3/audio book/chapters/APPENDIX_B_clean.txt` — line **22**
- `Vol_3/audio book/chapters/APPENDIX_B_Experimental_Mechan_clean.txt` — line **22**
- `Vol_3/audio book/chapters/Problem_Sets_with_Solutions_clean.txt` — line **228**
- `Vol_3/audio book/chapters/Problem_Se_clean.txt` — line **228**

### Vol 4
- `Vol_4/audio book/chapters/Ch01_clean.txt` — lines **85, 343**
- `Vol_4/audio book/chapters/Ch02_clean.txt` — lines **57, 321, 666**
- `Vol_4/audio book/chapters/APPENDIX_B_clean.txt` — line **44** (Newton's G; optional)
- `Vol_4/audio book/chapters/APPENDIX_B_Particle_Data_Table_clean.txt` — line **44** (Newton's G; optional)

### Vol 5
- `Vol_5/audio book/chapters/Ch14_clean.txt` — line **73**
- `Vol_5/audio book/chapters/Ch15_clean.txt` — lines **55, 250, 606**
- `Vol_5/audio book/chapters/Problem_Sets_with_Selected_Sol_clean.txt` — mirror of `P5.5.1` (J/m → kg/(m·s²))
- `Vol_5/audio book/chapters/Problem_Se_clean.txt` — same

### Vol 6
- `Vol_6/audio book/chapters/Ch05_clean.txt` — lines **69, 109** (and the line-187 explanatory note)
- `Vol_6/audio book/chapters/Ch07_clean.txt` — lines **29, 455**
- `Vol_6/audio book/chapters/Ch09_clean.txt` — lines **1824, 1925, 2225** (Ch 9 prose-rebuild mirror)
- `Vol_6/audio book/chapters/Ch14_clean.txt` — lines **536, 538** **NO EDIT** (historical quote)
- `Vol_6/audio book/chapters/APPENDIX_E_clean.txt` — line **359** NO EDIT
- `Vol_6/audio book/chapters/APPENDIX_E_Notation_Reference_clean.txt` — line **359** NO EDIT

---

## Reference docs (`Quality_Control/Reference/`)

### `01_Genesis_Physics/Quality_Control/Reference/Symbol_and_Constants.md`

**NO EDIT** — line 16 already canonical: `| **σ** | 6.0×10⁹⁸ | kg/(m·s²) | [ML⁻¹T⁻²] | Membrane 3-brane tension; fundamental creation parameter |`. This is the source of truth.

Other reference files (`Glossary.md`, `Equation_Registry.md`, `Axiom_Summary_Cards.md`, `Zone_Architecture.md`, `Biblical_References.md`, `Five_Principles.md`, `Four_Epochs_Timeline.md`) — grep returns no σ-with-units hits in scope. **NO EDIT.**

---

## Research/Foundations (in-scope, NOT 00_Archive)

| File | Line | BEFORE | AFTER |
|------|------|--------|-------|
| `Research/Foundations/AXIOM_MEMBRANE_MECHANICS.md` | 32 | `σ = membrane tension ≈ 6.0 × 10⁹⁸ kg/s²` | `σ = membrane tension ≈ 6.0 × 10⁹⁸ kg/(m·s²)` |
| `Research/Foundations/AXIOM_MEMBRANE_MECHANICS.md` | 62 | `σ = membrane tension [kg/s²] (force per unit length...)` | `σ = membrane tension [kg/(m·s²)] (energy per unit 3-volume; or equivalently force per unit area)` (also fix the "force per unit length" misdescription) |
| `Research/Foundations/AXIOM_MEMBRANE_MECHANICS.md` | 83, 86, 135 | `kg/s²` (3 hits) | `kg/(m·s²)` |
| `Research/Foundations/AXIOM_MEMBRANE_MECHANICS_CORRECTIONS_SUMMARY.md` | 14, 87, 101 | `kg/s²` | `kg/(m·s²)` |
| `Research/Foundations/AXIOM_MEMBRANE_MECHANICS_v2.md` | 33, 66, 235, 316, 319, 404, 424, 467 | `kg/s²` | `kg/(m·s²)` |
| `Research/Foundations/WATERS_FIELD_EQUATIONS.md` | 83, 1601 | `kg/s²` | `kg/(m·s²)` |
| `Research/Foundations/MEMBRANE_MASS_SCALE.md` | 237, 377, 414, 433, 520 | `kg/s²` | `kg/(m·s²)` |
| `Research/Foundations/L_EFF_DERIVATION.md` | 41, 172, 316, 455, 500 | `kg/s²` | `kg/(m·s²)` |
| `Research/Foundations/README_AXIOM3_CORRECTIONS.md` | 134, 208 | `kg/s²` | `kg/(m·s²)` |
| `Research/Foundations/VALIDATION_REPORT_2026-04-05.md` | 116, 133, 281 | `kg/s²` | `kg/(m·s²)` |

(All 00_Archive subpaths under Research/Foundations are OOS.)

## Research/Mathematical_Models (in-scope, NOT 00_Archive)

| File | Line | Notes |
|------|------|-------|
| `02_Thermodynamics/02-WATERS_REPLENISHMENT.md` | 1175, 1208 | `kg/s²` → `kg/(m·s²)` |
| `02_Thermodynamics/02-PLANCK_DISTRIBUTION.md` | 83 | same |
| `02_Thermodynamics/test_thermodynamic_laws.py` | 27 (comment), **70 (CODE: `SIGMA = 6.0e99`)** | **OFF-VALUE.** Line 70 sets σ to **6.0e99** not 6.0e98 — order-of-magnitude error in the simulation parameter. Fix value too. |
| `03_Electromagnetism/03-PRECISION_COMPLETIONS.md` | 43 | `kg/s²` → `kg/(m·s²)` |
| `03_Electromagnetism/03-APPLICATIONS.md` | 40 | same |
| `03_Electromagnetism/test_em_applications.py` | 26 (comment), **75 (CODE: `SIGMA = 6.0e99`)** | **OFF-VALUE.** Fix to `6.0e98` and `kg/(m·s²)` |
| `04_Optics_and_Waves/04-OPTICS_FROM_MAXWELL.md` | 280, 304 | `kg/s²` → `kg/(m·s²)` |
| `04_Optics_and_Waves/test_optics.py` | 24, **43 (CODE: `SIGMA = 6.0e99`)** | **OFF-VALUE.** Fix value + unit. |
| `05_Quantum_Mechanics/05-CONDENSED_MATTER_DERIVATION.md` | 71, 94 | unit swap |
| `05_Quantum_Mechanics/05-QM_FROM_MEMBRANE_DYNAMICS.md` | 92, 857 | unit swap |
| `05_Quantum_Mechanics/op09_decoherence_time.py` | 37 | unit swap (value correct: `6.0e98`) |
| `06_Nuclear_and_Particle_Physics/06-HIGGS_DERIVATION.md` | 36, 1215 | unit swap |
| `06_Nuclear_and_Particle_Physics/06-MASS_SPECTRUM_V2_EIGENVALUES.md` | 27, 621, 624, 695 | unit swap |
| `06_Nuclear_and_Particle_Physics/06-MASS_SPECTRUM_V2_HIERARCHY.md` | 55, 97, 721, 1068 | unit swap |
| `06_Nuclear_and_Particle_Physics/06-MASS_SPECTRUM_V2_TOPOLOGY.md` | 689 | unit swap |
| `06_Nuclear_and_Particle_Physics/06-MATTER_ANTIMATTER_ASYMMETRY.md` | 472, 673, 1015 | unit swap |
| `06_Nuclear_and_Particle_Physics/06-NUCLEAR_BINDING_PRECISION.md` | 4 | unit swap |
| `06_Nuclear_and_Particle_Physics/06-PARTICLE_MASS_SPECTRUM_V2.md` | 71 | unit swap |
| `06_Nuclear_and_Particle_Physics/06-PARTICLE_MASS_SPECTRUM_V3.md` | 64 | unit swap |
| `06_Nuclear_and_Particle_Physics/06-REMAINING_DERIVATIONS.md` | 129 | unit swap |
| `06_Nuclear_and_Particle_Physics/op03_condensate_yukawa.py` | 35 | unit swap (value correct) |
| `06_Nuclear_and_Particle_Physics/test_nuclear_physics.py` | 65 (G comment `m³/kg/s²`) | Newton's G; optional unit-presentation cleanup |
| `07_Relativity/07-COMPLETIONS_R4.md` | 812 | unit swap |
| `07_Relativity/test_gr_observables.py` | 24, **40 (CODE: `SIGMA = 6.0e99`)** | **OFF-VALUE.** Fix value + unit. |
| `08_Cosmology/test_cosmology.py` | **61 (CODE: `SIGMA = 6.0e99`)** | **OFF-VALUE.** Fix to `6.0e98`. |
| `08_Cosmology/op08_kappa_signatures.py` | 36 | unit swap (value correct) |
| `10_Fundamental_Constants/10-RESOLVED_MEMBRANE_TENSION.md` | 29, 30, 31, 32, 61, 95, 187, 189, 198, 250, 255, 303, 312, 333, 344, 354, 364, 370, 379, 391, 393, 409, 410, 447, 475, 483, 519 | This is the *resolution doc*. Lines stating canonical σ = 6.0×10⁹⁸ get unit swap; lines quoting *rejected* historical values (7.5×10²⁵, 7.5×10³⁴, 2.4×10⁴³, 2.16×10⁻³³) keep their values but unit can be normalized for consistency. |
| `10_Fundamental_Constants/10-RUNNING_COUPLINGS_RG_FLOW.md` | 133, 137, 779, 935, 1091 | unit swap |
| `10_Fundamental_Constants/10-PLANCK_CONSTANT_DERIVATION.md` | 61, 267, 365, 584, 625 | unit swap |
| `10_Fundamental_Constants/10-GRAVITATIONAL_CONSTANT_DERIVATION.md` | 600 | unit swap |
| `10_Fundamental_Constants/10-FUNDAMENTAL_CONSTANTS_OVERVIEW.md` | 495, 602 | unit swap |
| `10_Fundamental_Constants/10-COUPLING_CONSTANTS_DERIVATION.md` | 268 | unit swap |
| `10_Fundamental_Constants/10-COMPLETIONS.md` | 70 | unit swap |
| `10_Fundamental_Constants/10-COMPLETIONS_R4.md` | 61, 344, 813 | unit swap |
| `10_Fundamental_Constants/10-CONSTANTS_FROM_6D.md` | 383 | unit swap |
| `10_Fundamental_Constants/10-BOLTZMANN_CONSTANT_DERIVATION.md` | 106, 637 | unit swap |
| `10_Fundamental_Constants/op01_beta_geom_warp_integral.py` | 36 | unit swap (value correct) |
| `10_Derivation_Chain/INDEX.md` | 310 | unit swap |
| `10_Derivation_Chain/README.md` | 54 | unit swap |
| `10_Derivation_Chain/TEST_PARAMETERS.md` | 55 | unit swap (also flag: `Restoring force per length` description is misleading — σ for a 3-brane is energy per 3-volume, dim [ML⁻¹T⁻²]) |
| `10_Derivation_Chain/test_derivation_chains.py` | 901, 903, 908 | unit swap; line 903 dimensional check `[σ/μ] = (kg/s²) / (kg/m³) = m²/s²` is **DIMENSIONALLY WRONG**: kg/s² / kg/m³ = m³/s², not m²/s². With the correct σ = kg/(m·s²), the ratio σ/μ = m²/s² ✓. **The unit fix here also fixes a bug.** |
| `01_Classical_Mechanics/01-APPLIED_GRAVITY_CALCULATIONS.md` | 129 | **OFF-VALUE.** `\sigma = 6.0 \times 10^{99}` kg/s² — should be `6.0 \times 10^{98}` kg/(m·s²). Fix both. |
| `01_Classical_Mechanics/test_gravity_kinematics.py` | 17, **39 (CODE: `SIGMA = 6.0e99  # ... (corrected exponent)`)** | **OFF-VALUE.** Comment says "corrected exponent" but the value is wrong — fix to `6.0e98` and unit string. |
| `11_GP_Unique_Predictions/test_gp_unique_predictions.py` | 72, 711, 748 | unit swap (values correct) |

## Research/Simulations (in-scope)

| File | Line | BEFORE | AFTER |
|------|------|--------|-------|
| `Research/Simulations/waters_field_sim.py` | 36 | `SIGMA = 6.0e98          # kg/s²  (membrane tension)` | `SIGMA = 6.0e98          # kg/(m·s²)  (membrane tension)` |
| `Research/Simulations/membrane_vibrations.py` | 11, 41, 321 | `kg/s²` (3 hits) | `kg/(m·s²)` |
| `Research/Simulations/README.md` | 86, 150 | unit swap |
| `Research/Simulations/SIMULATION_RESULTS.md` | 55 | unit swap |

(Peer_Review/critic_report.md hits are historical-quote material; OOS by editorial judgment — leave alone. If executor wants to also fix, swap unit but keep the rejected values.)

---

## Grep guards

After fixes land, all of these must return **zero** matches (excluding OOS paths):

```bash
# 1) the literal bad unit (the load-bearing check)
grep -rn "kg/s²" 01_Genesis_Physics/Book_0_The_Foundations/ \
  --exclude-dir=00_Archive

grep -rn "kg/s²" 01_Genesis_Physics/Research/Foundations/ \
  --exclude-dir=00_Archive

grep -rn "kg/s²" 01_Genesis_Physics/Research/Mathematical_Models/ \
  --exclude-dir=00_Archive --exclude-dir=Test_Results

grep -rn "kg/s²" 01_Genesis_Physics/Research/Simulations/

# 2) common variants
grep -rnE "kg/s\^2|kg s\^-2|kg·s⁻²|\\\\text\{kg/s\}\\^2" \
  01_Genesis_Physics/Book_0_The_Foundations/ \
  --exclude-dir=00_Archive

# 3) the "energy per length" wrong-dimension prose for σ — Vol 6 Ch 9 trap
grep -rn "σ ~ 10\^48 J/m\|σ \\\\sim 10\^\{48\} J/m\|sigma ~ 10\^48 J/m" \
  01_Genesis_Physics/Book_0_The_Foundations/ \
  --exclude-dir=00_Archive

# 4) the rejected historical σ values that must not be cited as canonical
grep -rnE "2\\.4 ?[×\\\\*x] ?10\\^?\\{?43\\}? kg" \
  01_Genesis_Physics/Book_0_The_Foundations/ \
  --exclude-dir=00_Archive \
  --exclude=Ch14_DRAFT.md   # Ch 14 §14.9.4 quotes this as historical critic claim

# 5) off-value exponent in research code
grep -rnE "SIGMA *= *6\\.0e99" 01_Genesis_Physics/Research/

# 6) the wrong-value 10^99 narrative
grep -rn "10\^{99}\\|10⁹⁹\\|10\\*\\*99" 01_Genesis_Physics/Research/ \
  --exclude-dir=00_Archive | \
  grep -v "order-of-magnitude\\|order of magnitude"
```

Acceptable residual hits inside the OOS paths (`/00_Archive/`, `Quality_Control/Reviews/`, `Quality_Control/Reviewers/`, `_pre-comprehensive`) are expected and intentional — those files document the bug history.

---

## Dimensional sanity check

**Canonical:** σ = 6.0×10⁹⁸ kg/(m·s²) [dim ML⁻¹T⁻²]
**Canonical:** μ = 6.7×10⁸¹ kg/m³ [dim ML⁻³]
**Source for μ:** `01_Genesis_Physics/Quality_Control/Reference/Symbol_and_Constants.md` line 17 — `| **μ** | 6.7×10⁸¹ | kg/m³ | [ML⁻³] | Membrane volume mass density |`. (Cross-confirmed in Vol 1 Ch 5 §5.5 derivation status block, lines 493 and 696.)

**Ratio:**
σ/μ = [ML⁻¹T⁻²] / [ML⁻³] = L²T⁻² ✓ (units of velocity²)

Numerically:
σ/μ = (6.0×10⁹⁸ kg/(m·s²)) / (6.7×10⁸¹ kg/m³) = (6.0/6.7) × 10⁹⁸⁻⁸¹ × (m³)/(m·s²·1) = 0.8955 × 10¹⁷ m²/s² = **8.96×10¹⁶ m²/s²**

√(σ/μ) = 2.993×10⁸ m/s ≈ **0.9975 c** (CODATA c = 2.998×10⁸ m/s, 0.25% short — within the ±10% σ uncertainty noted in Vol 2 App B and consistent with rounded parameter values; the framework asserts c = √(σ/μ) *exactly* by Axiom 3 — the gap is a parameter-precision artifact, not a physics defect).

**This identity holds only with σ in kg/(m·s²) and μ in kg/m³.** If σ is misinterpreted as kg/s² (force-per-length, what a 2D drumhead has), the ratio gives m³/s² instead of m²/s² and the speed-of-light identity collapses. The unit fix is therefore not cosmetic — it is the difference between a dimensionally consistent framework and a 76-OOM Critic Claim 3.1.

---

## Top-level risk flags

1. **Vol 6 Ch 9 (FTL Travel) — full derivation rebuild required.** σ ~ 10⁴⁸ J/m is 50 orders below canonical AND the worked example V₀ = σ²/(2μ) ~ 10⁹⁸ J is internally inconsistent with the stated σ and μ (true value would be 10¹¹³ J). The "10⁹⁸ J barrier" the chapter publishes can only be recovered by yet a *fourth* σ value (~10⁴¹ J/m). Reviewer-04 already flagged this as Volume 6 finding C1. Unit-swap alone is insufficient — the worked example, the tunneling probability that consumes V₀, and any "δc/c at L1" prediction that depends on σ/μ must all be re-derived from canonical parameters. **Recommend: hold Ch 9 publication, route to author for arithmetic rebuild, then re-review.** Also: μ is stated as "kg/m" (per-length) in Ch 9, but the canonical μ is kg/m³ (per-volume). Two unit defects in the same paragraph.

2. **Vol 6 Ch 10 Energy Harvesting — citing rejected value as canonical.** Ch10_SOLUTIONS line 93 attributes σ ≈ 2.4×10⁴³ kg/s² to "Vol 1 Ch 5" — but Vol 1 Ch 5 says 6.0×10⁹⁸ kg/(m·s²), and Ch 14 §14.9.4 explicitly identifies 2.4×10⁴³ as the *rejected* Critic Claim 3.1 value. The cross-reference is not just wrong-valued, it is wrong-direction. Also: the surrounding prose uses "mass-per-area μ" while Symbol_and_Constants.md and the rest of the series uses volume density (kg/m³). Reviewer must decide whether to keep the kg/m³ convention (recommended) and rewrite the paragraph, or introduce a separate surface-density variable.

3. **Vol 5 Ch 4 §strong-field + Ch 5 §black-holes + App B + ProblemSets — "J/m" prose-rewrite class.** Six locations across Volume 5 describe σ as "J/m" (energy per length). J/m has dim [MT⁻²] (force, identical to kg/s²) — wrong for a 3-brane tension. Unit-swap to kg/(m·s²) is correct but the surrounding prose ("an enormous value set by the bulk cosmological constant and the Planck mass" / "energy per unit area" / etc.) should also be checked. Equivalent SI: kg/(m·s²) = N/m² = Pa = J/m³ (energy per 3-volume). Recommend standard parenthetical "(equivalently energy per unit 3-volume; Pa; dim [ML⁻¹T⁻²])" at first occurrence in each chapter.

4. **Research test code — `SIGMA = 6.0e99` in five test_*.py files** (`02/test_thermodynamic_laws.py:70`, `03/test_em_applications.py:75`, `04/test_optics.py:43`, `07/test_gr_observables.py:40`, `08/test_cosmology.py:61`, `01/test_gravity_kinematics.py:39`). Comment on line 39 even says "(corrected exponent)" — apparently a previous fix in the wrong direction. These off-by-ten-times values mean every numerical test result from these scripts in the past has used σ ten times the canonical value. The 11_GP_Unique_Predictions, 05_QM, 06_Nuclear, 08_Cosmology op_*.py, and 10_Fundamental_Constants op_*.py files use the correct 6.0e98 — so reviewer must audit which test results were generated with which value and whether any published numerical comparisons were skewed. **Treat as a separate finding from the unit fix; consider re-running `make test` once values are normalized.**

5. **Vol 1 PS-10.3 toy-numbers vs canonical-numbers.** ProblemSets_Ch07_11 line 626 uses pedagogical fake values (σ = 10⁻¹⁵ kg/m, η_B = 10⁻³⁵ m, ξ_A = 10⁻³⁷ m) with backwards ordering (ξ_A < η_B). Substituting canonical values changes the answer the student computes. Reviewer should confirm with author whether (a) replace the problem with the canonical-numbers version (recommended; consistent with Vol 1 Ch 10 worked derivation), or (b) keep it as a pure unit-checking exercise with fictitious numbers and just fix the unit so kg/m doesn't mislead the student into thinking σ has units of force-per-length. Either choice requires the solution key to match — flag for downstream cleanup.

6. **Additional secondary risks.**
   - Vol 4 App B line 54: `m³/kg/s²` for G is ambiguous parsing — Newton's G unit, separate physical quantity, optional cosmetic fix to `m³/(kg·s²)`.
   - `test_derivation_chains.py:903` contains a *dimensional-analysis bug* hiding behind the bad σ unit: `(kg/s²) / (kg/m³) = m²/s² ✓` is arithmetically wrong (kg/s² / kg/m³ = m³/s², which equals m²/s² only if you start from kg/(m·s²) — i.e. the canonical unit). The unit fix to `kg/(m·s²)` simultaneously fixes the dimensional check. **Good — but flag so executor doesn't miss that the algebra on that line is correct *only after* the unit swap.**

---

## Executor checklist

- [ ] Apply line-level edits in Volumes 1–6 manuscript files (sections above)
- [ ] Apply mirror edits to `audio book/chapters/*_clean.txt`
- [ ] Apply Research/Foundations + Research/Mathematical_Models + Research/Simulations edits
- [ ] Fix the six `SIGMA = 6.0e99` off-value bugs in test_*.py (separate concern from the unit fix; same PR OK)
- [ ] Rewrite PS-10.3 (Vol 1 ProblemSets_Ch07_11_DRAFT line 626) to canonical parameters
- [ ] Hold Vol 6 Ch 9 (DRAFT + DRAFT_Part3 + audio Ch09_clean.txt) — needs author rebuild of V₀ tunneling example, not just unit swap
- [ ] Rerun the six grep guards in CI / locally; all must report zero outside OOS paths
- [ ] Update task list `0516_Rev_Book_0_TASKS.md` row for σ-units fix to DONE
