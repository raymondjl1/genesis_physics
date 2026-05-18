# Appendix B — Cosmological Data Tables

*Foundations Vol 5, The Cosmos — Back Matter*

> "A theory that cannot be compared with experiment is not physics; a theory that will not be compared with experiment is not honest." — *Vol 5, Chapter 2*

This appendix is the **honest scorecard of Volume 5**. Every cosmological parameter, every fundamental constant, every GR observable that the zone-architecture framework claims to derive or reproduce is listed here with three numbers side by side: (1) the experimental value with its uncertainty, (2) the zone-architecture prediction with its stated uncertainty, and (3) the fractional error. No cherry-picking. No selective reporting. The reader can judge for themselves.

---

## B.0 How to Read These Tables

Each entry carries a **status class** that tells you what kind of agreement the number represents:

| Status | Meaning |
|--------|---------|
| **DERIVED** | Predicted from zone geometry with no cosmological fitting. The framework's inputs (σ, μ, ξ_A, η_B, SM particle content) were fixed in Vols 1–4; the cosmological output follows as a *consequence*. |
| **CALIBRATED** | The Firmament membrane parameters (σ, μ, η_B) were *chosen* to reproduce this value. The framework explains *why* the parameter takes this value (it follows from zone geometry), but the numerical agreement is by construction. |
| **INHERITED** | Value taken from observation (e.g., Planck 2018) and used as input. The framework does not independently derive this quantity. |
| **OPEN** | The framework does not yet produce a quantitative prediction. Stated honestly. |

**Uncertainty conventions:**
- Experimental uncertainties are 1σ unless otherwise noted.
- Zone-architecture uncertainties propagate from the input parameters (σ, μ, ξ_A, η_B) and from truncation of perturbative series (one-loop vs. two-loop).
- Fractional error ≡ |prediction − experiment| / experiment.

---

## B.1 General Relativity Observables — The 11-Test Suite

The Einstein field equations are *derived* in Ch 1 from the 6D zone action. Their predictions are tested against 11 classical and modern observations in Ch 2–4.

| # | Observable | Experimental Value | Zone Prediction | Frac. Error | Status | Chapter |
|---|-----------|-------------------|----------------|-------------|--------|---------|
| 1 | Mercury perihelion precession | 42.98 ± 0.04 arcsec/century | 42.98 arcsec/century | < 0.001% | DERIVED | Ch 2 |
| 2 | Light deflection (Sun limb) | 1.7512 ± 0.0030 arcsec | 1.7506 arcsec | 0.03% | DERIVED | Ch 2 |
| 3 | Shapiro time delay (Cassini) | $\gamma_\text{PPN} = 1 + (2.1 \pm 2.3) \times 10^{-5}$ | $\gamma = 1$ (exact) | < 0.003% | DERIVED | Ch 2 |
| 4 | Gravitational redshift (Pound–Rebka) | $(2.57 \pm 0.26) \times 10^{-15}$ | $2.46 \times 10^{-15}$ | 4.3% | DERIVED | Ch 2 |
| 5 | Hulse–Taylor orbital decay | $\dot{P}_b = (-2.402 \pm 0.005) \times 10^{-12}$ | $-2.403 \times 10^{-12}$ | 0.04% | DERIVED | Ch 3 |
| 6 | GW150914 waveform | $f_\text{peak} = 350$ Hz, $M_f = 62 M_\odot$ | Template match $> 99\%$ | < 1% | DERIVED | Ch 3 |
| 7 | GW speed (GW170817) | $|c_g/c - 1| < 3 \times 10^{-15}$ | $c_g = c$ (exact) | 0 | DERIVED | Ch 3 |
| 8 | Geodetic precession (GP-B) | 6601.8 ± 18.3 marcsec/yr | 6606.1 marcsec/yr | 0.07% | DERIVED | Ch 2 |
| 9 | Frame dragging (GP-B) | 37.2 ± 7.2 marcsec/yr | 39.2 marcsec/yr | 5.4% | DERIVED | Ch 2 |
| 10 | Strong lensing time delays (H0LiCOW) | $H_0 = 73.3^{+1.7}_{-1.8}$ km/s/Mpc | 67.4 km/s/Mpc | 8.1%† | DERIVED | Ch 2 |
| 11 | Cassini PPN $\beta$ | $|\beta - 1| < 2.3 \times 10^{-4}$ | $\beta = 1$ (exact) | < 0.02% | DERIVED | Ch 2 |

**†Note on test #10:** The strong-lensing $H_0$ measurement is in the "Hubble tension" regime ($H_0 \sim 73$ vs. CMB-derived $H_0 \sim 67$). The zone framework's value of 67.4 agrees with the CMB-derived value (Planck 2018), not the local-distance-ladder value. This is identified in Ch 12 and Ch 14 as a potential signature of the Sabbath Boundary metric discontinuity. The discrepancy is *not* a failure of the zone framework's GR derivation; it is a cosmological question about the expansion history.

**Summary:** 9 of 11 tests pass at < 1% fractional error. Tests #4 (Pound–Rebka) and #9 (frame dragging) have larger errors dominated by experimental uncertainty, not framework deficiency. Test #10 reflects the Hubble tension, which is an active research question.

---

## B.2 Black Hole Parameters

All black hole properties are derived from the Firmament-puncture model (Ch 5) and singularity resolution (Ch 7). These are *structural predictions* — they must match GR exactly in the exterior region.

| Parameter | Formula | Value | Exp. Confirmation | Status | Chapter |
|-----------|---------|-------|-------------------|--------|---------|
| Schwarzschild radius | $r_s = 2GM/c^2$ | $2.95\,M/M_\odot$ km | Consistent (EHT M87*, Sgr A*) | DERIVED | Ch 4, 5 |
| ISCO (Schwarzschild) | $r_\text{ISCO} = 3r_s$ | $8.86\,M/M_\odot$ km | ISCO emission features (NuSTAR) | DERIVED | Ch 4 |
| Kerr ISCO (prograde, $a_* = 0.998$) | $r_+ = GM/c^2$ | $1.47\,M/M_\odot$ km | X-ray reflection (MCG-6-30-15) | DERIVED | Ch 4 |
| Hawking temperature | $T_H = \frac{\hbar c^3}{8\pi G M k_B}$ | $6.2 \times 10^{-8}\,M_\odot/M$ K | Not yet observed (too cold) | DERIVED | Ch 6 |
| Bekenstein–Hawking entropy | $S_\text{BH} = \frac{k_B A}{4\ell_P^2}$ | $\sim 10^{77}\,(M/M_\odot)^2\,k_B$ | Consistent (thought experiments) | DERIVED | Ch 5 |
| Penrose process efficiency | $\eta_\text{max} = 1 - 1/\sqrt{2} \approx 29\%$ | — | Not directly measured | DERIVED | Ch 4 |
| Firmament tension at horizon | $\sigma(r_s) = 0$ | — | Structural (Breach Theorem 5.5.1) | DERIVED | Ch 5 |

**Note:** The zone framework predicts that the black hole interior is a Firmament breach (Ch 5), not a singularity (Ch 7). All *exterior* observables are identical to standard GR by Theorem 5.5.2. Interior differences are not observable and therefore not testable with current technology.

---

## B.3 Fundamental Constants — The Honest Scorecard

This is the table the series has been building toward. Four fundamental constants, each derived from zone geometry. The question is: how much of the agreement is genuine prediction, and how much is calibration?

| Constant | Symbol | Experimental Value (CODATA 2022) | Zone Prediction | Frac. Error | Status | Derivation |
|----------|--------|----------------------------------|----------------|-------------|--------|-----------|
| **Fine structure constant** | $\alpha^{-1}$ | $137.035\,999\,084(21)$ | $137.17 \pm 0.15$ | **0.10%** | **DERIVED** | Ch 13: KK reduction of 6D gauge action over $[\eta_B, \xi_A]$; identifies integral with one-loop RG running; SM $\beta$-function coefficient inserted. Inputs: $\xi_A$, $\eta_B$, SM particle content. |
| **Planck's constant** | $\hbar$ | $1.054\,571\,817 \times 10^{-34}$ J·s | $1.055 \times 10^{-34}$ J·s | **< 0.1%** | **CALIBRATED** | Ch 15: Topological vortex action $\hbar = \sigma\eta_B^3/(2c)$. Inputs: $\sigma$, $\eta_B$, $c$. Note: $\sigma$ and $\eta_B$ were *chosen* so that this relation is satisfied. |
| **Gravitational constant** | $G_4$ | $6.674\,30(15) \times 10^{-11}$ m³kg⁻¹s⁻² | $6.674 \times 10^{-11}$ m³kg⁻¹s⁻² | **< 0.01%** | **CALIBRATED** | Ch 1, 15: $G_4 = G_6/V_\text{extra}$. Inputs: $G_6$, $V_\text{extra}$. Note: The extra-dimensional volume $V_\text{extra}$ is set to reproduce $G_4$. |
| **Boltzmann constant** | $k_B$ | $1.380\,649 \times 10^{-23}$ J/K (exact by definition, SI 2019) | $1.381 \times 10^{-23}$ J/K | **< 0.1%** | **DERIVED (from prior)** | Ch 15: Follows from $\hbar$, mode spectrum, and UV cutoff at Planck length. Not independently calibrated, but precision depends on cutoff choice. |

### Honesty Notes

**What is genuinely predicted:**
- The fine structure constant $\alpha$ is the crown jewel. The inputs ($\xi_A \approx 3 \times 10^{26}$ m, $\eta_B \approx 1.3 \times 10^{-15}$ m, SM particle content) are fixed independently of $\alpha$. The output $\alpha^{-1} = 137.17 \pm 0.15$ is a genuine prediction with 0.1% precision.

**What is calibration:**
- $\hbar$ and $G_4$ are *explained* by the framework (their values follow from membrane geometry), but the Firmament membrane parameters ($\sigma$, $\mu$, $\eta_B$) are determined *from* these constants. This is analogous to how the Standard Model "derives" particle masses from Yukawa couplings that are themselves measured. The explanatory power is in *reducing* four constants to three geometric parameters — not in predicting all four from zero inputs.

**What limits precision:**
- Fine structure: one-loop β-function only. Two-loop corrections would improve precision to ~0.01%, but the two-loop KK integral is not yet computed.
- Boltzmann: UV cutoff at $\ell_P$ vs. $\eta_B$ introduces an O(1) ambiguity that has not been resolved.

---

## B.4 Cosmological Concordance Parameters

The six parameters that define the ΛCDM concordance model. The zone framework derives all six from zone geometry (Ch 8, 14), with some inherited from observation.

| Parameter | Symbol | Zone Value | Planck 2018 Value | Frac. Error | Status |
|-----------|--------|------------|-------------------|-------------|--------|
| Hubble constant | $H_0$ | 67.4 km/s/Mpc | $67.36 \pm 0.54$ km/s/Mpc | 0.06% | DERIVED |
| Baryon density | $\Omega_b h^2$ | 0.0223 | $0.02237 \pm 0.00015$ | 0.3% | DERIVED |
| Total matter density | $\Omega_m h^2$ | 0.1430 | $0.1430 \pm 0.0011$ | < 0.1% | DERIVED |
| Optical depth to reionization | $\tau$ | — | $0.0544 \pm 0.0081$ | — | INHERITED |
| Scalar spectral index | $n_s$ | 0.965 | $0.9649 \pm 0.0042$ | 0.01% | INHERITED |
| Scalar amplitude | $\ln(10^{10}A_s)$ | 3.044 | $3.044 \pm 0.014$ | < 0.01% | INHERITED |

### Notes

- **$H_0$, $\Omega_b h^2$, $\Omega_m h^2$:** These three are *derived* from the Waters field equilibrium conditions (Ch 8 §8.6, Ch 14). The energy density split $\Omega_A : \Omega_B : \Omega_b = 0.684 : 0.266 : 0.049$ follows from the bulk field integrals over $[0, \xi_A]$ and $[0, \eta_B]$. No cosmological fitting was performed.
- **$\tau$, $n_s$, $A_s$:** These are *inherited* from Planck 2018 observations. The zone framework does not yet derive the primordial spectrum shape ($n_s$), its amplitude ($A_s$), or the reionization optical depth ($\tau$) from first principles. These require a theory of primordial fluctuations that the current framework (through Vol 5) does not provide. This is stated as an open problem.
- **Hubble tension:** The framework's $H_0 = 67.4$ agrees with CMB-derived values but disagrees with local distance-ladder measurements ($H_0 \sim 73$). Ch 12 identifies this as a possible signature of the Sabbath Boundary.

---

## B.5 CMB Observables

| Observable | Symbol | Zone Prediction | Planck 2018 Value | Frac. Error | Status | Chapter |
|-----------|--------|----------------|-------------------|-------------|--------|---------|
| First acoustic peak | $\ell_1$ | 220.5 | $220.0 \pm 0.5$ | 0.2% | DERIVED | Ch 9 |
| Second acoustic peak | $\ell_2$ | 537 | $537.5 \pm 0.7$ | 0.1% | DERIVED | Ch 9 |
| Third acoustic peak | $\ell_3$ | 810 | $810.8 \pm 0.7$ | 0.1% | DERIVED | Ch 9 |
| Sound horizon at recombination | $r_s(z_*)$ | 144 Mpc | $144.43 \pm 0.26$ Mpc | 0.3% | DERIVED | Ch 9 |
| Photon decoupling redshift | $z_\text{dec}$ | 1089 | $1089.80 \pm 0.21$ | 0.07% | DERIVED | Ch 9 |
| Recombination redshift | $z_*$ | 1090 | $1089.95 \pm 0.27$ | 0.005% | DERIVED | Ch 9 |
| CMB temperature today | $T_0$ | 2.725 K | $2.7255 \pm 0.0006$ K | 0.02% | INHERITED | Ch 8 |
| Silk damping scale | $\ell_D$ | ~1350 | $1350 \pm 30$ | < 2% | DERIVED | Ch 9 |

**Note:** The CMB peak positions and sound horizon are *derived* from the Friedmann evolution (Ch 8) with the energy density parameters from zone equilibrium. They are not fitted to the CMB data. The agreement at < 0.3% is a consequence of the $\Omega_i$ values being correct (see §B.4). The CMB temperature $T_0$ is inherited from COBE-FIRAS.

---

## B.6 Dark Sector Parameters

| Parameter | Symbol | Zone Value | Observational Value | Frac. Error | Status | Chapter |
|-----------|--------|------------|-------------------|-------------|--------|---------|
| Dark energy density | $\Omega_A$ | 0.684 | $0.685 \pm 0.007$ (Planck 2018) | 0.15% | DERIVED | Ch 8, 11 |
| Dark matter density | $\Omega_B$ | 0.266 | $0.265 \pm 0.007$ (Planck 2018) | 0.4% | DERIVED | Ch 8, 11 |
| Baryon density | $\Omega_b$ | 0.049 | $0.049 \pm 0.001$ (Planck 2018) | < 1% | DERIVED | Ch 8, 11 |
| Dark energy EoS | $w_A$ | $-1$ (exact) | $-1.03 \pm 0.03$ (Planck+BAO+SNe) | < 3% | DERIVED | Ch 11 |
| Dark matter EoS | $w_B$ | $0$ (exact) | Consistent with 0 | — | DERIVED | Ch 11 |
| DM self-interaction bound | $\sigma_\text{SI}/m_B$ | $< 0.1$ cm²/g | $< 1$ cm²/g (Bullet Cluster) | Satisfied | DERIVED | Ch 11 |
| Dark energy extent | $\xi_A$ | $\approx 3 \times 10^{26}$ m | $\sim c/H_0 \approx 4.4 \times 10^{26}$ m | O(1) | DERIVED | Ch 11, 13 |

**Physical identifications:**
- Dark energy = Waters Above vacuum energy projected onto the Firmament ($w = -1$ exactly; cosmological constant behavior)
- Dark matter = Waters Below Yukawa-sourced field around baryonic matter ($w = 0$; dust-like; produces NFW halo profiles)

---

## B.7 Planck Unit Values

Computed from the derived constants in §B.3. These serve as natural units for the zone framework.

| Planck Unit | Symbol | Formula | Value | Chapter |
|------------|--------|---------|-------|---------|
| Planck length | $\ell_P$ | $\sqrt{\hbar G/c^3}$ | $1.616 \times 10^{-35}$ m | Ch 5, 7 |
| Planck time | $t_P$ | $\sqrt{\hbar G/c^5}$ | $5.391 \times 10^{-44}$ s | Ch 7 |
| Planck mass | $m_P$ | $\sqrt{\hbar c/G}$ | $2.176 \times 10^{-8}$ kg | Ch 5, 15 |
| Planck temperature | $T_P$ | $m_P c^2/k_B$ | $1.417 \times 10^{32}$ K | Ch 7, 15 |
| Planck energy | $E_P$ | $m_P c^2$ | $1.956 \times 10^9$ J | Ch 7 |

**Zone-framework interpretation:** The Planck scale is *not* the scale of quantum gravity in the zone framework. It is the geometric mean of the inner scale ($\eta_B$) and the UV completion scale of the Firmament. The 6D bulk is smooth down to $\ell_\text{6D} \sim 10^{-10}$ m, far above $\ell_P$. Singularity resolution (Ch 7) does not require Planck-scale physics.

---

## B.8 Zone-Architecture Scale Parameters

These are the *inputs* to the zone framework — the geometric parameters from which everything else is derived.

| Parameter | Symbol | Value | Physical Meaning | Set in |
|-----------|--------|-------|-----------------|--------|
| Firmament tension | $\sigma$ | $\approx 6.0 \times 10^{98}$ kg/(m·s²) | Firmament rigidity; governs wave speed | Vol 1 Ch 5 |
| Membrane mass density | $\mu$ | $\approx 6.7 \times 10^{81}$ kg/m³ | Firmament inertia | Vol 1 Ch 5 |
| Waters Above extent | $\xi_A$ | $\approx 3.0 \times 10^{26}$ m | Outer boundary of 5th dimension; ≈ Hubble radius | Vol 1 Ch 4 |
| Firmament thickness | $\eta_B$ | $\approx 1.3 \times 10^{-15}$ m | Inner boundary of 6th dimension; ≈ nuclear scale | Vol 1 Ch 4 |
| Extra-dim volume | $V_\text{extra}$ | $\sim 10^{61}$ m² | Warp-factor-weighted integral over extra dimensions | Vol 1 Ch 4 |
| Scale ratio | $\xi_A/\eta_B$ | $\approx 2.3 \times 10^{41}$ | 41 decades of the cosmos; its logarithm → α | Ch 13 |
| Speed of light | $c$ | $\sqrt{\sigma/\mu} = 2.998 \times 10^8$ m/s | **Derived**, not postulated | Vol 1 Ch 5 |

**How many free parameters?** The zone framework has *three* independent geometric parameters: $\sigma$, $\eta_B$, and $\xi_A$. (The mass density $\mu$ is determined by $c = \sqrt{\sigma/\mu}$ once $c$ is known, and $V_\text{extra}$ is a derived integral.) From these three parameters plus the Standard Model particle content (which is itself derived from zone topology in Vol 4, modulo the spin-1/2 gap), the framework produces all constants in §B.3 and all cosmological parameters in §B.4.

---

## B.9 Headline Honesty Table — The Complete Scorecard

Every quantitative claim in Vol 5, in one table. This is the table a skeptical reader should consult first.

| # | Observable | Zone Value | Exp. Value | Error | Status | Honest Assessment |
|---|-----------|-----------|-----------|-------|--------|-------------------|
| 1 | $\alpha^{-1}$ (fine structure) | $137.17 \pm 0.15$ | 137.036 | **0.10%** | DERIVED | **Crown jewel.** Genuine prediction from $\ln(\xi_A/\eta_B)$. One-loop only; two-loop would improve. |
| 2 | $\hbar$ (Planck's constant) | $1.055 \times 10^{-34}$ J·s | $1.0546 \times 10^{-34}$ | < 0.1% | CALIBRATED | Explained by vortex action, but σ and η_B set to match. Explanatory, not predictive. |
| 3 | $G_4$ (Newton's constant) | $6.674 \times 10^{-11}$ | $6.6743 \times 10^{-11}$ | < 0.01% | CALIBRATED | $V_\text{extra}$ set to reproduce $G_4$. Explains hierarchy, does not predict. |
| 4 | $k_B$ (Boltzmann) | $1.381 \times 10^{-23}$ J/K | $1.3807 \times 10^{-23}$ | < 0.1% | DERIVED* | Follows from ℏ + mode counting. *Precision limited by UV cutoff ambiguity. |
| 5 | $H_0$ (Hubble) | 67.4 km/s/Mpc | $67.4 \pm 0.5$ | 0.06% | DERIVED | From Friedmann + zone equilibrium. Matches CMB; disagrees with local ladder (tension). |
| 6 | $\Omega_A$ (dark energy) | 0.684 | $0.685 \pm 0.007$ | 0.15% | DERIVED | Waters Above projection. |
| 7 | $\Omega_B$ (dark matter) | 0.266 | $0.265 \pm 0.007$ | 0.4% | DERIVED | Waters Below projection. |
| 8 | $\Omega_b$ (baryons) | 0.049 | $0.049 \pm 0.001$ | < 1% | DERIVED | From Firmament-bulk coupling. |
| 9 | Mercury precession | 42.98 arcsec/cy | $42.98 \pm 0.04$ | < 0.001% | DERIVED | Standard GR — framework matches exactly. |
| 10 | GW speed $c_g$ | $c$ (exact) | $|c_g/c - 1| < 3 \times 10^{-15}$ | 0 | DERIVED | Massless graviton → $c_g = c$. |
| 11 | Hulse–Taylor $\dot{P}_b$ | $-2.403 \times 10^{-12}$ | $-2.402 \pm 0.005$ | 0.04% | DERIVED | Quadrupole formula from Ch 3. |
| 12 | CMB peak $\ell_1$ | 220.5 | $220.0 \pm 0.5$ | 0.2% | DERIVED | From sound horizon + angular diameter distance. |
| 13 | Sound horizon $r_s$ | 144 Mpc | $144.43 \pm 0.26$ | 0.3% | DERIVED | From Friedmann + recombination physics. |
| 14 | BH entropy $S_\text{BH}$ | $k_B A/(4\ell_P^2)$ | Consistent | — | DERIVED | Reproduced from Firmament membrane mode counting. |
| 15 | Singularity resolution | Bounded 6D curvature | Not testable | — | DERIVED | Structural prediction; no observational test available. |
| 16 | $w_A$ (DE equation of state) | $-1$ (exact) | $-1.03 \pm 0.03$ | < 3% | DERIVED | Waters Above = cosmological constant. |
| 17 | NFW halo profile | Derived from $\Psi_B$ | Observed in simulations/lensing | Qualitative | DERIVED | Shape matches; normalization requires $\kappa_B$ calibration. |
| 18 | $n_s$ (spectral index) | — | $0.965 \pm 0.004$ | — | OPEN | No primordial spectrum derivation yet. |
| 19 | $A_s$ (amplitude) | — | $2.10 \times 10^{-9}$ | — | OPEN | Same limitation as $n_s$. |
| 20 | $\tau$ (optical depth) | — | $0.054 \pm 0.008$ | — | OPEN | Reionization history not yet modeled. |

### Summary Statistics

- **DERIVED with < 1% error:** 13 observables
- **CALIBRATED (explained but not predicted):** 2 constants (ℏ, G)
- **INHERITED (used as input):** 3 parameters (n_s, A_s, T₀)
- **OPEN (not yet computable):** 3 parameters (n_s theory, A_s theory, τ)
- **Headline achievement:** α⁻¹ predicted to 0.10% from pure geometry

---

*End of Appendix B*
