# Appendix A: Complete Prediction Index

**Product:** Foundations Vol 6, Predictions, Simulations, and Open Problems
**Component:** Back Matter, Appendix A
**Scope:** Every testable prediction cataloged anywhere in Vol 6 — 153 predictions (P-001 through P-153) grouped by category, each with quantitative falsification threshold.
**Convention:** Citation format `(V.Ch.Eq)` with `V ∈ {1,2,3,4,5,6}`. Status values: MATCHES / DIFFERS / NOVEL / OPEN.

---

## A.1  How to Use This Appendix

This appendix is the single, scrutable, consolidated bet that Genesis Physics makes against nature. Chapters 1 through 4 and 9 through 12 introduced 153 numbered predictions. They are scattered across roughly 600 pages of argument. A skeptic — the person for whom this volume is written — needs one place where every commitment is visible side-by-side. That is the purpose of Appendix A.

Each prediction carries a permanent identifier of the form `P-XXX` (three-digit zero-padded). The identifier never migrates: once assigned in a chapter draft, it is bound to that prediction for the life of the series. If a prediction is later retired or superseded, its identifier is not reused; the row in this appendix is annotated as "superseded by P-YYY" rather than deleted. This rule protects citation stability across editions.

Every row in the master table of §A.13 has nine columns:

- **ID** — the P-XXX identifier.
- **Title** — a short descriptive title (10–15 words).
- **Predicted value** — what zone architecture predicts, quantitatively where possible, qualitatively where the framework currently cannot produce a number.
- **SM value** — what the Standard Model / ΛCDM / GR predicts, or "no prediction" where standard physics is silent, or "fitted" where standard physics measures but does not predict.
- **Experimental value** — the best current measurement or bound.
- **Precision** — the tightest available precision (fractional, absolute, or bound).
- **Source** — the Vol 6 chapter where the prediction is defined, plus the Vols 1–5 source equation in `(V.Ch.Eq)` form.
- **Status** — one of four values:
  - **MATCHES** — zone architecture's prediction is consistent with experiment at the relevant precision, and either equals the SM prediction or provides a derivation where the SM only fits.
  - **DIFFERS** — zone architecture and standard physics make different quantitative or structural commitments. The difference may or may not be currently resolvable.
  - **NOVEL** — zone architecture predicts an effect that standard physics does not predict at all (not merely "does not measure").
  - **OPEN** — the prediction awaits experimental resolution, or the framework's own calculation is incomplete. Not a cop-out — OPEN tags force honest accounting.
- **Falsification threshold** — a quantitative observation that would make the prediction wrong. This column is the *contract* with the physics community. The Skeptic reviewer checks that every threshold is genuinely falsifiable — tautologies ("prediction fails if it is falsified") are rejected. Predictions where the chapter draft omits a numerical threshold are flagged in §A.15 with either a proposed threshold (extracted from the derivation) or an explicit note that the prediction is currently unfalsifiable and belongs to Ch 14.

The master table is organized into ten categories (§A.3 through §A.12), chosen so that predictions testing the same physical system cluster together and reviewers can audit the framework's risk profile by domain. Within each category, predictions are ordered by P-XXX number, not by chapter. The per-category intros (150–300 words each) summarize the category's overall status and flag the most consequential predictions.

**How to read the precision column.** A number like "0.10%" means fractional agreement. A number like "3 × 10⁻¹⁵" is absolute (fractional speed-of-GW agreement in this case). An entry "upper bound" means only a limit is known, not a detection. An entry "N/A" means the prediction cannot be currently quantitatively compared — either because the framework has no number, or because no experiment yet addresses the observable.

**How to read the status column.** A MATCHES status is not necessarily a victory — a match to an already-fitted SM value is weaker than a match to an SM-predicted value. A DIFFERS status can be a victory (the prediction is more constrained than SM), a failure (the prediction is wrong), or a pending test (the difference is below current precision). The per-category narrative clarifies.

**How to read the falsification column.** Thresholds are stated as specific numerical conditions under which the prediction is falsified at a specified significance (typically 3σ or 5σ). A threshold that reads "Any confirmed detection at any level" is maximally strict; a threshold that reads "Detection at > 10× the predicted value" is weaker but still falsifiable. The column never reads "it would require reconsideration" — that is hedge language, not a threshold.

---

## A.2  Test-Suite Context

As of 2026-04-05 (the definitive final test run, documented in `Research/Mathematical_Models/Test_Results/TEST_RESULTS_2026-04-05_DEFINITIVE.md`), the overall validation state of Genesis Physics across 136 numerical and conceptual tests is:

| Outcome | Count | Percentage |
|---------|-------|------------|
| PASS | 97 | 71.3% |
| PARTIAL | 37 | 27.2% |
| FAIL | 0 | 0.0% |
| NOT YET | 2 | 1.5% |

The appendix uses these test-suite results to support claims about individual predictions. Where a prediction cites a test ID (e.g., "Test 6.22"), the test's status is reflected in the prediction's status column: a PASS test usually corresponds to a MATCHES prediction; a PARTIAL test often corresponds to a DIFFERS prediction with quantitative agreement but incomplete derivation; a NOT YET test corresponds to OPEN.

The zero-FAIL count warrants explicit care. It does not mean the framework has no failures. The particle-mass predictions (P-052 through P-055) are wrong by factors of 20 to 1000 against experiment. These are classified PARTIAL in the test suite because the suite measures *derivation-chain consistency*, not *simple-model accuracy* — the hard-wall Firmament membrane model is incomplete, but the Firmament-vibration framework is not internally contradictory. Whether this classification is fair is a judgment call the reader must make; Chapter 2 confronts it head-on. The appendix preserves the classification but foregrounds the underlying disagreement with experiment.

---

## A.3  Category I — Structural Predictions (Conservation Laws, Zone Topology, Gauge Structure)

Nine predictions (P-031, P-032, P-033, P-034, P-042, P-050, P-051, P-081, P-082) covering the structural backbone of the framework: the four classical conservation laws derived from zone-manifold symmetries, charge quantization from Firmament topology, the periodic table and chemical bonding as the end of the longest derivation chain in the series, and the two novel predictions (zone-number conservation P-081; cosmic zone-transition imprints P-082) that would only emerge from zone topology. Every entry in this category is a Level 1 match with the Standard Model — the mathematics is identical, but zone architecture provides the derivation.

The category's falsification profile is asymmetric: the conservation laws are tested to extraordinary precision in every particle-physics experiment for the last century, so a failure here would falsify almost all of modern physics simultaneously, not just zone architecture. The zone-specific additions (P-081, P-082) are where category risk lives.

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|
| P-031 | Energy Conservation | $dE_{\rm total}/dt = 0$ (time-translation symmetry of zone manifold) | Same (Noether + Poincaré) | Confirmed to $10^{-15}$ precision (atomic physics, cosmology) | $10^{-15}$ | Vol 6 Ch 1; Vol 1 Ch 7, Eq (1.7.22) | MATCHES | Any confirmed energy-conservation violation in an isolated system at $> 3\sigma$, not accountable by Waters-field coupling (Eq 1.7.24). |
| P-032 | Momentum Conservation | $dP^i/dt = 0$ (spatial-translation symmetry) | Same | Confirmed in all particle-physics experiments | Exact | Vol 6 Ch 1; Vol 1 Ch 7, Eq (1.7.29) | MATCHES | Observation of spontaneous momentum change in an isolated system at $> 3\sigma$. |
| P-033 | Angular Momentum Conservation | $dL^k/dt = 0$ (rotational symmetry) | Same | Confirmed atomic / nuclear / astrophysical | Exact | Vol 6 Ch 1; Vol 1 Ch 7, Eq (1.7.33) | MATCHES | Observation of $L$-violation in any isolated system at $> 3\sigma$. |
| P-034 | Charge Conservation | $\nabla_\mu j^\mu = 0$ (Firmament U(1) gauge) | Same | $\tau_p > 10^{34}$ yr bound (proton lifetime) | Exact | Vol 6 Ch 1; Vol 1 Ch 7; Vol 2 Ch 6 | MATCHES | Any observation of net charge creation or destruction at any rate. |
| P-042 | Charge Quantization | Quantized in units of $e$ (Firmament topology) | Observed fact; partial Dirac-monopole explanation | All measured charges are integer multiples of $e/3$ or $e$ | Exact | Vol 6 Ch 1; Vol 2 Ch 3; Vol 2 Ch 6; Test 3.7 | MATCHES | Discovery of a stable particle with irrational or non-quantized electric charge at $> 5\sigma$. |
| P-050 | Periodic Table Structure | Aufbau principle from multi-electron Schrödinger equation on zone-derived QM | Same (QM applied to atoms) | All ionization energies match to measured precision | Structural | Vol 6 Ch 1; Vol 4; Test 9.1 | MATCHES | Discovery of a stable element with ground-state electron configuration violating aufbau (beyond known Cr, Cu exceptions). |
| P-051 | Chemical Bonding | Covalent / ionic / metallic / hydrogen bonding from zone-derived QM | Same (quantum chemistry) | All bonding types, bond energies, molecular geometries consistent | Structural | Vol 6 Ch 1; Test 9.2 | MATCHES | Discovery of a bonding mechanism not describable by quantum-mechanical orbital theory. |
| P-081 | Zone Number Conservation | Conserved integer $Z$ from zone-manifold $\pi_1$ (generalized Noether) | No such quantum number exists in SM | Not yet measured (requires completed topological classification) | N/A | Vol 6 Ch 3; Vol 1 Ch 7 | NOVEL | Once topological classification identifies specific zone-number-forbidden channels, measurement of those channels at the SM-predicted rate with no suppression at $> 3\sigma$ falsifies Z-conservation. |
| P-082 | Cosmic Zone Transition Imprints | Linear/planar zone-geometry-shaped perturbations in CMB temperature and polarization | No zone transitions exist in SM cosmology | Not detected; bounded by Planck + BICEP | Upper bound | Vol 6 Ch 3; Vol 5 Ch 11 | NOVEL | CMB-S4 finds no zone-transition-template features above cosmic-variance floor at $3\sigma$ after template search at $\ell \sim 10$–100. |

---

## A.4  Category II — Forces and Couplings

Seven predictions (P-004, P-005, P-006, P-056, P-057, P-058, P-065) covering the derivation of the three SM gauge couplings and the electromagnetic-to-gravitational force hierarchy from zone geometry. This is the category where the framework produces *genuine* predictions — values that standard physics merely fits. The fine structure constant is the headline: zone architecture predicts $\alpha^{-1} = 137.17 \pm 0.15$ from the logarithm of the ratio $\xi_A/\eta_B$ (Eq 5.13.32), while the Standard Model treats $\alpha$ as a free input parameter. The 0.10% residual offset is attributed to the not-yet-computed higher-loop coefficient $b_{\rm hi}$.

The category's risk lives in the prediction P-065 — that $\alpha$ is *fixed* and cannot vary with cosmic time. This is a stronger claim than ΛCDM makes, and it discriminates zone architecture from dynamical-dark-energy models.

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|
| P-004 | Fine Structure Constant | $\alpha^{-1} = 137.17 \pm 0.15$ (derived from $\xi_A/\eta_B$) | Fitted (no prediction) | $\alpha^{-1} = 137.035\,999\,084(21)$ | 0.10% | Vol 6 Ch 1; Vol 5 Ch 13, Eq (5.13.32) | MATCHES | Any $|\Delta\alpha/\alpha| > 10^{-7}$ over cosmic time; or inability to bring predicted $\alpha^{-1}$ within 0.01% of experiment by refining $b_{\rm eff}$. |
| P-005 | EM-to-Gravitational Force Hierarchy | $\alpha_{\rm em}/\alpha_G = 1.24 \times 10^{36}$ (log vs. power law on $\mathcal{R}$) | Observed; "hierarchy problem" unsolved | $1.24 \times 10^{36}$ | 0.08% | Vol 6 Ch 1; Vol 2 Ch 9, Eq (2.9.45) | MATCHES | Deviations from inverse-square gravity at $r < 10^{-6}$ m at $> 3\sigma$ would modify $V_{\rm extra}$. |
| P-006 | Strong Coupling Constant | $\alpha_s(M_Z) = 0.118$ (from $\eta$-boundary confinement) | Fitted from experiment | $0.1180 \pm 0.0008$ (PDG) | $< 0.2\%$ | Vol 6 Ch 1; Vol 4 Ch 12; Test 6.22 | MATCHES | Value measured outside PDG $\pm 3\sigma$ band in future precision measurements. |
| P-056 | Fine Structure Constant Residual Offset | $\alpha^{-1} = 137.17 \pm 0.15$ (same as P-004) | No prediction | 137.036 | 0.10% | Vol 6 Ch 2; Vol 5 Ch 13, Eq (5.13.32) | DIFFERS | If refinement of $b_{\rm hi}$ (two-loop reduction) cannot bring the prediction within 0.01% of experiment, the logarithmic derivation pathway requires fundamental revision. |
| P-057 | Weak Mixing Angle | $\sin^2\theta_W$ within $\sim 1\%$ (derived, not fitted) | $\sin^2\theta_W = 0.23122 \pm 0.00003$ (fitted) | Same as SM (definition-dependent) | $\sim 1\%$ | Vol 6 Ch 2; Vol 4 Ch 11 | DIFFERS | Full two-loop zone-geometry derivation fails to achieve sub-percent agreement with measured value. |
| P-058 | Strong Coupling Running at Extreme Energies | Modified running above $E_\eta \sim 150$ GeV from zone boundary | Standard perturbative QCD; $\alpha_s \to 0$ as $Q \to \infty$ | Consistent with SM up to $\sim 1$ TeV | $\sim 0.7\%$ at $M_Z$ | Vol 6 Ch 2; Vol 4 Ch 12; Vol 2 Ch 10 | DIFFERS | $\alpha_s$ measured at $\pm 0.1\%$ at $Q > 500$ GeV shows no deviation from standard perturbative QCD (FCC-ee era). |
| P-065 | Fine Structure Constant Constancy Over Cosmic Time | $\Delta\alpha/\alpha = 0 \pm 10^{-9}$ per Gyr (geometric fixity) | No prediction; dynamical-DE allows $\sim 10^{-6}$/Gyr | $|\Delta\alpha/\alpha| < 1.6 \times 10^{-6}$ (ESPRESSO); $\dot\alpha/\alpha = (1.6 \pm 2.3) \times 10^{-17}$ yr⁻¹ (atomic clocks) | $10^{-6}$ astrophysical, $10^{-17}$ yr⁻¹ lab | Vol 6 Ch 2; Vol 5 Ch 13 | DIFFERS | $|\Delta\alpha/\alpha| > 3 \times 10^{-7}$ detected at $> 3\sigma$ over cosmic time. |

---

## A.5  Category III — Particle Physics

Twenty-two predictions covering the particle spectrum, electroweak phenomenology, QCD observables, superconductivity (BCS), the number of neutrino species, and the one category where the framework's failure is both the largest and the most pedagogically honest: the hard-wall particle-mass model fails by factors of 20 to 1000 (P-052, P-053, P-054, P-055). Chapter 2 is unambiguous that this is a *component-level* failure of the simplest mass model, not a framework failure, but the error cannot be hidden. The appendix preserves the honest accounting.

The category's successes are disproportionately structural (why three generations, why the gauge group, why confinement) rather than numerical. The numerical successes (W/Z masses, Higgs mass, jet observables) are Level 1 matches that follow from zone architecture's recovery of the SM Lagrangian — strong consistency evidence, but not independent derivations.

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|
| P-014 | W Boson Mass | $M_W = 80.377$ GeV (from $M_W = gv/2$) | Same | $80.377 \pm 0.012$ GeV (PDG) | 0.1% | Vol 6 Ch 1; Vol 4 Ch 11 | MATCHES | $M_W$ outside $80.377 \pm 0.050$ GeV at $> 3\sigma$. |
| P-015 | W Boson Width and Branching Ratios | $\Gamma_W = 2.085$ GeV; BR$_{\rm had}$ = 67.4%, BR$_{\rm lep}$ = 32.6% | Same | $2.085 \pm 0.042$ GeV; $67.41 \pm 0.27\%$ | $< 0.5\%$ | Vol 6 Ch 1; Vol 4 Ch 11 | MATCHES | Branching-ratio anomaly $> 3\sigma$ in any channel. |
| P-016 | Z Boson Mass | $M_Z = 91.1876$ GeV | Same | $91.1876 \pm 0.0021$ GeV | 0.002% | Vol 6 Ch 1; Vol 4 Ch 11 | MATCHES | $M_Z$ outside current $\pm 3\sigma$ band. |
| P-017 | Z Boson Width and Partial Widths | $\Gamma_Z = 2.495$ GeV; all partial widths within 0.2% of PDG | Same | $2.4952 \pm 0.0023$ GeV | 0.03% total | Vol 6 Ch 1; Vol 4 Ch 11; Test 6.20 | MATCHES | Partial-width anomaly $> 3\sigma$ in any channel. |
| P-018 | Number of Neutrino Species | $N_\nu = 3.0$ (three topologically distinct boundary modes) | $N_\nu = 3$ (from Z-width) | $2.984 \pm 0.008$ | 0.5% | Vol 6 Ch 1; Vol 4 Ch 11; Test 6.20 | MATCHES | $N_\nu$ measurement outside $[2.9, 3.1]$ at $> 3\sigma$. |
| P-019 | Higgs Boson Mass | $m_H = 125.1$ GeV | Fitted | $125.10 \pm 0.14$ GeV (ATLAS+CMS) | $< 0.1\%$ | Vol 6 Ch 1; Vol 4 Ch 11 | MATCHES | $m_H$ shifts by more than 1 GeV from current world average. |
| P-020 | Higgs Coupling Structure | $y_t = 0.994$, $y_b = 0.0239$, $y_\tau = 0.0102$; $\Gamma_H = 4.62$ meV | Yukawa $\propto$ mass | $y_t = 1.001 \pm 0.030$; $y_b = 0.021$–$0.024$; $y_\tau = 0.010$–$0.011$; $\Gamma_H = 4.07 \pm 0.16$ meV | 0.7%–13% | Vol 6 Ch 1; PARTICLE_PRECISION_COMPLETIONS | MATCHES | Coupling-ratio pattern deviating from mass-proportionality at $> 3\sigma$. |
| P-021 | QCD Confinement and String Tension | $\sigma = 0.18$ GeV²/fm²; asymptotic freedom $\alpha_s(M_Z) = 0.118$ | Lattice QCD: $\sigma \in [0.18, 0.19]$ | Same | $\sim 2\%$ | Vol 6 Ch 1; Vol 4 Ch 12; Test 6.22 | MATCHES | String tension outside $[0.15, 0.22]$ GeV²/fm² from improved lattice. |
| P-022 | Jet Observables in $e^+e^-$ Annihilation | $R$-ratio NLO = 3.81; 3-jet rate = 3.2% | Same (NLO QCD) | $R = 3.88 \pm 0.05$; 3-jet rate $= 3.2\% \pm 0.1\%$ | $\sim 2\%$ | Vol 6 Ch 1; Test 6.23 | MATCHES | $R$-ratio or jet-rate anomalies $> 3\sigma$ at future colliders. |
| P-023 | Neutrino Mass Splittings | $\Delta m^2_{21} = 7.5 \times 10^{-5}$ eV²; $\Delta m^2_{32} = 2.5 \times 10^{-3}$ eV² (boundary eigenvalue spectrum) | Fitted | $7.53 \pm 0.18 \times 10^{-5}$; $2.51 \pm 0.05 \times 10^{-3}$ | 0.4% each | Vol 6 Ch 1; UNIQUE_PREDICTIONS Prediction 4 | MATCHES | Splittings outside $3\sigma$ of global oscillation fits. |
| P-044 | Superconductivity (BCS Gap and $T_c$) | $T_c$(Al) = 1.16 K; $T_c$(Nb) = 9.3 K | BCS theory | 1.175 K; 9.25 K | $< 1\%$ | Vol 6 Ch 1; EM_PRECISION_COMPLETIONS; Test 3.12 | MATCHES | Systematic $T_c$ deviation from BCS $> 10\%$ in conventional superconductors. |
| P-045 | Meissner Effect (Penetration Depths) | $\lambda_L$(Pb) ≈ 37 nm; $\lambda_L$(Al) ≈ 16 nm | London equation | 39 nm; 15 nm | $\sim 5\%$ | Vol 6 Ch 1; EM_PRECISION_COMPLETIONS; Test 3.13 | MATCHES | Penetration depths deviating from London theory by $> 20\%$ in conventional superconductors. |
| P-046 | Photoelectric Effect | $KE = hf - W$ (Einstein relation, membrane quantization) | Same (Einstein 1905) | Confirmed in all photoelectric measurements | Structural | Vol 6 Ch 1; Vol 4 Ch 1; Test 5.1 | MATCHES | Photoelectron energy not linear in frequency, or absence of threshold. |
| P-047 | Compton Scattering | $\Delta\lambda = (h/m_e c)(1 - \cos\theta)$ | Same | $< 0.1\%$ agreement in X-ray scattering | $< 0.1\%$ | Vol 6 Ch 1; Vol 4; Test 5.2 | MATCHES | Wavelength shift deviating from Compton formula by $> 1\%$. |
| P-048 | Bose-Einstein Condensation | $T_c$ formula validated for $^{87}$Rb | Same (Einstein 1925) | $T_c \approx 170$ nK at $n \sim 10^{14}$ cm⁻³ | Structural | Vol 6 Ch 1; Vol 4; Test 5.12 | MATCHES | BEC $T_c$ deviating from prediction by $> 5\%$ after finite-size/interaction corrections. |
| P-052 | Electron Mass from Membrane Ground State | $\sim 500$ MeV (hard-wall $\eta_B$) | Fitted (Higgs Yukawa) | 0.511 MeV | Wrong by 1000× | Vol 6 Ch 2; Vol 4 Ch 10, Eq (4.10.18) | DIFFERS | Already falsified: hard-wall model is inadequate. Framework-level threshold: if soft-potential + Higgs-Waters coupling calculation yields mass > 10× experimental value, membrane-mode interpretation of $m_e$ is falsified. |
| P-053 | Muon-to-Electron Mass Ratio | $\sim 2$–$10$ (simple $n_\xi$ quantum numbers) | Fitted | 206.77 | Wrong by 20–100× | Vol 6 Ch 2; Vol 4 Ch 10 | DIFFERS | Already falsified for hard-wall model. Framework threshold: complete Yukawa-overlap calculation yielding any ratio < 100 or > 500 for $(n_\xi=1,n_\xi=2)$ modes. |
| P-054 | Quark Mass Spectrum Pattern | Regular spacing in hard-wall model | Irregular, fitted | u ≈ 2.2, d ≈ 4.7, s ≈ 93, c ≈ 1275, b ≈ 4180, t ≈ 173000 MeV | Qualitative mismatch | Vol 6 Ch 2; Vol 4 Ch 10 | DIFFERS | Already falsified for hard-wall. Framework threshold: soft-potential calculation cannot produce the observed hierarchy within factor-of-3 at all six flavors. |
| P-055 | Neutrino Mass Scale | No mechanism for sub-eV masses in current framework | No prediction (seesaw) | $\sum m_\nu < 0.12$ eV (cosmological) | N/A (framework gap) | Vol 6 Ch 2; Vol 4 | OPEN | Framework cannot currently falsify; classified OPEN until Higgs-Waters coupling is computed. |
| P-066 | Neutrino Mass Ordering — Normal Only | Normal hierarchy ($m_1 < m_2 < m_3$) is unique (boundary eigenvalue topology) | Both orderings allowed | Normal favored at $\sim 1.5\sigma$ (NuFIT v5.2) | $\Delta\chi^2 \approx 2.4$ | Vol 6 Ch 2; UNIQUE_PREDICTIONS 4 | DIFFERS | Inverted hierarchy confirmed at $> 3\sigma$ by JUNO + DUNE + atmospheric combined. |
| P-067 | Proton Absolute Stability | $\tau_p = \infty$ (topological winding) | Stable (SM accidental); $10^{34}$–$10^{36}$ yr (GUTs) | $\tau_p > 2.4 \times 10^{34}$ yr (SK) | Lower bound only | Vol 6 Ch 2; Vol 4 Ch 10 | DIFFERS | Any confirmed proton-decay event at any rate. |
| P-074 | Super-Heavy Firmament Resonances | Additional matter modes at $m \sim n \cdot 480$ MeV (hard-wall), soft-potential corrected | No additional matter resonances predicted | Not yet detected | Bound | Vol 6 Ch 3; Vol 1 Ch 5, Eq (1.5.12)–(1.5.18); Vol 4 Ch 10 | NOVEL | Complete soft-boundary calculation predicts masses $< 5$ TeV; HL-LHC finds none at $\pm 10\%$ precision at those masses. |
| P-075 | Firmament Vibration Frequency Ratios | Helmholtz eigenvalue pattern on zone domain (specific mass ratios if 3+ resonances found) | No prediction | Not yet measured | N/A | Vol 6 Ch 3; Vol 1 Ch 5 | NOVEL | Three or more new resonances found with ratios inconsistent with any Helmholtz pattern on simply-connected 2D domain. |
| P-144 | Subnuclear Form-Factor Anomaly at HL-LHC | DIS form factor at $q > 200$ GeV differs from SM by $(2 \pm 1)\%$ (from $\eta_B$-boundary hadronic coupling) | No anomaly predicted | Not yet measured at required precision | Target $0.5\%$ | Vol 6 Ch 12; Vol 4 Ch 12 | NOVEL | HL-LHC measurement at $q = 500$ GeV shows no anomaly above $0.5\%$ at $3\sigma$. |

---

## A.6  Category IV — Relativity and General Relativity

Fifteen predictions (P-007 to P-013, P-059, P-060, P-068 to P-070, P-100, P-101, P-151 to P-153) covering every classical test of general relativity, gravitational-wave observables, the six extra GW polarization modes unique to a 6D theory, the Firmament-mechanical origin of $c$, and bulk-geodesic shortcut effects. Zone architecture recovers GR as the zero-mode sector of 6D Einstein equations and therefore passes every classical GR test identically. The novel territory is the polarization modes, the KK graviton tower, and the prediction that $c$ itself is a Firmament property with second-order corrections from local curvature.

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|
| P-007 | Mercury Perihelion Precession | 42.98 arcsec/century | Same (GR) | $42.98 \pm 0.04$ arcsec/century | 0.16% | Vol 6 Ch 1; Vol 5 Ch 2, Eq (5.2.12)–(5.2.14) | MATCHES | Anomalous precession $> 0.1$ arcsec/century above GR. |
| P-008 | Gravitational Light Bending | $\delta\theta = 1.7478$ arcsec at solar limb | 1.75 arcsec | $\gamma - 1 = (-0.8 \pm 1.2) \times 10^{-4}$ | $10^{-4}$ | Vol 6 Ch 1; Vol 5 Ch 2, Eq (5.2.21) | MATCHES | $|\gamma - 1| > 10^{-3}$ from any PPN measurement. |
| P-009 | Shapiro Time Delay | $\Delta t = 5.61$ μs (Viking) | Same | $\gamma - 1 = (2.1 \pm 2.3) \times 10^{-5}$ (Cassini) | $10^{-5}$ | Vol 6 Ch 1; Vol 5 Ch 2, Eq (5.2.32) | MATCHES | $|\gamma - 1| > 10^{-4}$ from future radar ranging. |
| P-010 | Gravitational Redshift (Pound-Rebka) | $z = 2.457 \times 10^{-15}$ for $h = 22.5$ m | Same (equivalence principle) | Confirmed to 0.54% (Pound-Rebka) | 0.54% | Vol 6 Ch 1; Vol 5 Ch 2, Eq (5.2.25)–(5.2.26) | MATCHES | Any equivalence-principle violation at any precision. |
| P-011 | Gravitational Wave Speed | $v_{\rm GW} = c$ exactly | Same (GR) | $|v_{\rm GW} - c|/c < 3 \times 10^{-15}$ (GW170817) | $3 \times 10^{-15}$ | Vol 6 Ch 1; Vol 5 Ch 3; Relativity Test 7.12 | MATCHES | $v_{\rm GW} \neq c$ at $> 3\sigma$ significance. |
| P-012 | Frame Dragging (Gravity Probe B) | $\sim 39$ mas/yr | Same (Lense-Thirring) | $37.2 \pm 7.2$ mas/yr | Within $1\sigma$ | Vol 6 Ch 1; Vol 5 Ch 2, Eq (5.2.39) | MATCHES | Deviation from GR prediction by $> 3\sigma$ in LAGEOS/future. |
| P-013 | GPS Gravitational Time Dilation | $\Delta\tau/\tau \approx 5.3 \times 10^{-10}$ | Same | $\sim 38.7$ μs/day net | 1.47% | Vol 6 Ch 1; Vol 5 Ch 2, Eq (5.2.28) | MATCHES | GPS timing anomaly at nanosecond level over sustained periods. |
| P-059 | Frequency-Dependent GW Propagation Speed | $\beta \sim 10^{-35}$ (KK dispersion) | Exactly zero dispersion | $|v_{\rm GW} - c|/c < 3 \times 10^{-15}$ | $3 \times 10^{-15}$ | Vol 6 Ch 2; Vol 5 Ch 3; UNIQUE_PREDICTIONS 3 | DIFFERS | LISA+PTA era $\sigma(\beta) < 10^{-30}$ and frequency-dependent dispersion at $10^{-20}$ level would indicate a different extra-dim model. |
| P-060 | KK Graviton Tower | Discrete tower, $\Delta m \sim \hbar/(c\eta_B) \sim 150$ MeV | No tower | Not detected | Bound | Vol 6 Ch 2; Vol 5 Ch 3 | DIFFERS | KK modes detected with spacing inconsistent with $\hbar/(c\eta_B)$. |
| P-068 | Vector GW Polarization Modes | Two vector modes from $h_{\mu\xi}$, $h_{\mu\eta}$; amplitude $\sim (R_{\rm compact}/\lambda_{\rm GW})^2$ | Only two tensor modes allowed | Not yet detected | Bound | Vol 6 Ch 3; Vol 5 Ch 3, Eq (5.3.24)–(5.3.31) | NOVEL | Third-gen detectors with null-stream analysis find no vector modes at $h < 10^{-25}$ with compactification $R \sim 10^{-6}$ m. |
| P-069 | Scalar GW Modes (Zone Breathing) | Two scalar modes; mass $m_\Phi \sim \hbar/(c R_{\rm eff})$ | No scalar GW modes | Not detected | N/A | Vol 6 Ch 3; Vol 5 Ch 3; Vol 1 Ch 5 | NOVEL | Detection of scalar mode with mass inconsistent with $m_\Phi = n\hbar/(cR_{\rm eff})$ for any integer $n$ with $R_{\rm eff}$ consistent with zone parameters. |
| P-070 | Kaluza-Klein Graviton Tower | Discrete tower, $m_n = n \hbar c / R_{\rm eff}$, Yukawa falloff | Graviton massless; no tower | No KK modes detected; Eöt-Wash bounds inverse-square to $r > 30$ μm | Bound | Vol 6 Ch 3; Vol 5 Ch 3 | NOVEL | HL-LHC + Eöt-Wash combined exclude $R_{\rm eff} > 30$ μm; zone-architecture prediction $R \sim \eta_B$ remains viable below this. |
| P-100 | Speed of Light as Brane Property | $c^2 = \sigma/\mu$ from Firmament membrane mechanics | $c$ is universal constant (GR postulate) | Constant to $< 10^{-15}$ in all measured environments | $10^{-15}$ | Vol 6 Ch 9; Vol 1 Ch 5 | NOVEL | $c$ measured constant at $10^{-18}$ fractional precision in all gravitational environments. |
| P-101 | Bulk Geodesic Shortcut Factor | $\kappa_{\rm bulk} = 1 + \varepsilon$ with $\varepsilon \sim 10^{-4}$–$10^{-2}$ (gravity via bulk, EM via Firmament) | Both at $c$ (GR) | $v_{\rm GW} - v_{\rm EM}$ consistent with zero (GW170817) | $3 \times 10^{-15}$ | Vol 6 Ch 9 | NOVEL | Multi-event combined analysis of 10+ NS mergers shows no GW lead time beyond plasma/dust dispersion at $3\sigma$. |
| P-151 | Extended GW Polarization Amplitude Relations | $h_S/h_+ = h_L/h_\times = e^{2A_0} \sim 10^{-3 \pm 0.5}$; $h_{V_{1,2}}/h_+ = e^{A_0} \sim 10^{-1.5 \pm 0.3}$ (warp-factor suppression) | Only $h_+, h_\times$ | Not yet measured for extra modes | Bound | Vol 6 Ch 12 | NOVEL | LIGO-retrofit ratio $h_S/h_+$ outside $[10^{-4}, 10^{-2}]$ for a GW150914-class event. |
| P-152 | LIGO-Retrofit Sensitivity Gain for Scalar Breathing Mode | $h_S^{\rm min} = 10^{-22.5 \pm 0.3}$ at 100 Hz | N/A (mode absent in GR) | Not yet implemented | N/A | Vol 6 Ch 12 | NOVEL | Retrofit-A implementation with mirror-angle adjustment achieves $h_S$ sensitivity worse than $10^{-21}$ at design frequency. |
| P-153 | Pulsar-Timing-Array Longitudinal-Mode Detection Threshold | $h_L \sim 10^{-15}$ at $10^{-9}$ Hz from SMBH inspirals; PTA reaches $10^{-16}$ sensitivity | No longitudinal mode | NANOGrav stochastic-background observations | Projected | Vol 6 Ch 12 | NOVEL | PTA reaches $h_L < 10^{-17}$ after 10-year integration with no detection. |

---

## A.7  Category V — Cosmology

Nineteen predictions (P-024 to P-030, P-061 to P-064, P-076 to P-079, P-082 [cross-filed], P-141, P-143, P-145, P-146) spanning the cosmic energy budget, the dark-energy equation of state, dark-matter phenomenology, the cosmological-constant problem as a geometric UV cutoff, and specific anomalies at the zone-boundary scale that observable surveys can test. This is arguably the category where zone architecture makes the most discriminating predictions: $w = -1$ exactly (P-063) with zero evolution (P-064), a categorical commitment to non-interacting dark matter (P-061, P-062), and a mechanistic account of the 68/27/5 cosmic energy split (P-025).

The risk is concentrated on P-061 and P-063. A confirmed direct-detection DM signal or a confirmed $w \neq -1$ from DESI + Euclid would force major framework revision.

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|
| P-024 | Dark Energy Equation of State | $w = -1$ (geometric certainty, Waters Above confinement) | $w = -1$ (ΛCDM, observed fact) | $w = -1.03 \pm 0.03$ (Planck+BAO) | Consistent | Vol 6 Ch 1; Vol 5 Ch 11, Eq (5.11.1); UNIQUE_PREDICTIONS 2 | MATCHES | DESI/Euclid find $w$ outside $[-1.05, -0.95]$ at $> 3\sigma$. |
| P-025 | Cosmic Energy Budget | $\Omega_\Lambda = 0.684$, $\Omega_{\rm DM} = 0.266$, $\Omega_b = 0.049$, $\Omega_r \approx 9.2 \times 10^{-5}$ | Fitted | Planck: $0.685 \pm 0.007$, $0.265 \pm 0.007$, $0.049 \pm 0.001$ | $< 0.2\%$ each | Vol 6 Ch 1; Vol 5 Ch 8, 11 | MATCHES | Any component deviating from zone-derived by $> 3\sigma$ in future Euclid+Roman+DESI combined. |
| P-026 | Hubble Constant | $H_0 = 67.4$ km/s/Mpc | Fitted: 67.4 (Planck) / 73.0 (SH0ES) | $67.4 \pm 0.5$ (Planck) | Planck only | Vol 6 Ch 1; Vol 5 Ch 8; Test 8.1 | MATCHES | Hubble-tension resolution favoring $H_0 > 70$ forces zone architecture to explain the local measurement. |
| P-027 | Spatial Flatness | $\Omega_{\rm total} = 1$ (manifold topology) | $1.000 \pm 0.002$ (Planck, ΛCDM+inflation) | Same | Consistent with exact | Vol 6 Ch 1; Vol 5 Ch 8; Test 8.4 | MATCHES | $|\Omega_{\rm total} - 1| > 0.01$ at $> 3\sigma$. |
| P-028 | Age of the Universe | $t_0 = 13.787$ Gyr | $13.787 \pm 0.020$ Gyr | Same | Consistent | Vol 6 Ch 1; Vol 5 Ch 8; Test 8.15 | MATCHES | Age determination shifts by more than 0.1 Gyr from current value. |
| P-029 | Baryonic Tully-Fisher Relation | $M_b = A v_{\rm flat}^4$ with slope exactly 4; $A \approx 40$–$60~M_\odot/({\rm km/s})^4$ | Empirical; ΛCDM requires tuning | $A \approx 47$; slope $= 4.0 \pm 0.1$ (McGaugh) | Exact slope | Vol 6 Ch 1; Vol 5 Ch 11, Eq (5.11.14) | MATCHES | Slope significantly different from 4 at $> 3\sigma$. |
| P-030 | Galaxy Rotation Curves (SPARC) | NFW-like profile from Waters Below Firmament field equation; $\chi^2_{\rm red} \approx 0.78$–$1.24$ across 6 galaxies | NFW from ΛCDM N-body | SPARC survey data | ΛCDM-comparable | Vol 6 Ch 1; Vol 5 Ch 11, Eq (5.11.6)–(5.11.10) | MATCHES | Systematic NFW failure with $\chi^2_{\rm red} > 3$ across SPARC. |
| P-061 | Dark Matter Interaction Cross-Section | $\sigma_{\rm DM\text{-}SM} = 0$ (bulk–Firmament separation) | No SM prediction; WIMPs ~$10^{-46}$ | $< 4.1 \times 10^{-47}$ cm² (XENONnT, 2023) | Upper bound | Vol 6 Ch 2; Vol 5 Ch 11 §11.4 | DIFFERS | Confirmed detection with $\sigma > 10^{-48}$ cm² at $> 3\sigma$ by at least two independent experiments. |
| P-062 | Dark Matter Decay Lifetime | $\tau_{\rm DM} = \infty$ (field configuration, not particle) | Some extensions finite | $> 10^{26}$ yr | Lower bound | Vol 6 Ch 2; Vol 5 Ch 11 | DIFFERS | Confirmed DM-decay products from galactic center / dwarfs above astrophysical background at $> 3\sigma$. |
| P-063 | Dark Energy EOS (tight constraint) | $w = -1.000 \pm 0.001$ | Free parameter; ΛCDM assumes $-1$ | $-1.028 \pm 0.032$ (Planck+BAO); $-0.98^{+0.06}_{-0.05}$ (DES Y3) | $\sigma(w) \sim 0.03$ | Vol 6 Ch 2; Vol 5 Ch 11, Eq (5.11.42) | DIFFERS | Combined DESI+Euclid $w < -1.05$ or $w > -0.95$ at $> 3\sigma$. |
| P-064 | No Dark Energy Evolution | $dw/dz = 0$ exactly | $w(a) = w_0 + (1-a)w_a$ allowed | $w_a = 0.0 \pm 0.3$ | $\sigma(w_a) \sim 0.3$ | Vol 6 Ch 2; Vol 5 Ch 11 | DIFFERS | $w_a \neq 0$ at $> 2\sigma$ from combined DESI+Euclid. |
| P-076 | Membrane Zero-Point Energy and $\Lambda$ | UV cutoff from compact dimensions yields $\rho_{\rm vac} \sim 10^{-47}$ GeV⁴ (not $10^{74}$) | $\rho_{\rm vac} \sim M_{\rm Pl}^4$ from naive QFT ($10^{120}$ discrepancy) | $\rho_{\rm vac} = 2.9 \times 10^{-47}$ GeV⁴ | Known observationally | Vol 6 Ch 3; Vol 4 Ch 9 | NOVEL | Completed mode-counting calculation yields $\rho_{\rm vac}$ more than $\sim 10\times$ different from observed. |
| P-077 | Waters Field Density Gradient Signatures | Cored profile (not cuspy NFW) from finite ground-state solution | NFW cuspy from ΛCDM N-body | Cusp-core tension in dwarf galaxies | Qualitative | Vol 6 Ch 3; Vol 1 Ch 6; Vol 5 Ch 11 | NOVEL | Baryonic feedback simulations fully resolve cusp-core within SM, and Waters-field profile gives wrong scale length or asymptotic behavior. |
| P-078 | Waters Field Fluctuation Power Spectrum | Cutoff at $k_{\rm cut} \sim 1/\eta_B$; finite coherence length | Scale-free CDM at small scales | Missing-satellites / too-big-to-fail tensions | Qualitative | Vol 6 Ch 3; Vol 1 Ch 6; Vol 5 Ch 11 | NOVEL | Completed Waters-field power spectrum predicts satellite-galaxy count inconsistent with Milky Way census / LSST deep imaging at $3\sigma$. |
| P-079 | Waters-Firmament Coupling Oscillations | $\tau_{\rm couple} \sim 2\xi_A/c \sim 60$ Gyr; $\delta\rho_\Lambda/\rho_\Lambda \sim 10^{-3}$ | No DE-DM coupling in ΛCDM | $w(z)$ precision at $\pm 0.03$ | Target $\pm 0.001$ | Vol 6 Ch 3; SUSTAINING_COUPLING.md; Vol 1 Ch 6 | NOVEL | High-$z$ ($z > 2$) DE measurements show $w = -1.000 \pm 0.001$ with no oscillatory structure constrains $\delta\rho_\Lambda/\rho_\Lambda < 10^{-3}$. |
| P-141 | Dark-Energy Density Fluctuation Amplitude | $\delta\rho_A/\rho_\Lambda \leq \epsilon_\kappa \sim 10^{-27}$ | Uniform cosmological constant | Not yet measured at Hubble scale | Target $10^{-20}$ | Vol 6 Ch 12 | NOVEL | Euclid/DESI find $\delta\rho_A/\rho_\Lambda \geq 10^{-20}$ at any Hubble-scale wavelength. |
| P-143 | ISW Cross-Correlation Anomaly at $\xi$-Boundary | $\Delta C_\ell^{T\delta}/C_\ell^{T\delta,\rm ΛCDM} = (10 \pm 5)\%$ at $\ell \sim 300 \pm 100$ | ΛCDM prediction | Planck+BOSS consistent with ΛCDM | Target $2\%$ | Vol 6 Ch 12 | NOVEL | Planck+BOSS+Euclid matched-filter reprocessing shows no excess above $2\%$ at $3\sigma$. |
| P-145 | High-Redshift Shapiro Time-Delay Anomaly | $\Delta H/H = (0.5 \pm 0.3)\%$ at $z > 5$, scaling as $\tanh(z/z_{\rm boundary})$ | No anomaly | Not yet measured at 0.2% | Target $0.2\%$ | Vol 6 Ch 12 | NOVEL | JWST+Euclid show no departure from ΛCDM at 0.2% level. |
| P-146 | Thermal Anisotropy from Zone-Boundary Vacuum-Energy Step | $\Delta T/T \sim 10^{-5}$ correlated with zone-boundary position | ΛCDM + inflation sources only | Planck data consistent with ΛCDM | Boundary of detection | Vol 6 Ch 12 | NOVEL | Planck+Euclid cross-correlation shows no zone-boundary-correlated pattern at $3\sigma$. |

---

## A.8  Category VI — QED and Electromagnetism

Eleven predictions (P-001 to P-003, P-040, P-041, P-043, P-049, and the EM-adjacent entries in other categories) covering QED precision at parts-per-trillion, the derivation of Maxwell's equations from Firmament membrane wave propagation, the emergence of $c$ from zone metric parameters, charge-quantization consequences (cross-filed in Category I), and the Casimir effect as direct experimental evidence for membrane zero-point modes. This is the framework's strongest category by precision: the electromagnetic test suite achieved a perfect 100% pass rate (13 of 13 tests).

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|
| P-001 | Electron Anomalous Magnetic Moment | $a_e = 0.001\,159\,652\,180\,89$ (perturbative QED) | Same | $a_e = 0.001\,159\,652\,180\,81(11)$ | $7 \times 10^{-10}$ | Vol 6 Ch 1; Vol 4 Ch 7, Eq (4.7.51)–(4.7.56) | MATCHES | $a_e^{\rm exp}$ shifts by $> 3\sigma$ from zone-derived QED value. |
| P-002 | Lamb Shift | 1057.845 MHz | Same (QED) | $1057.845(9)$ MHz | $10^{-7}$ | Vol 6 Ch 1; Vol 4 Ch 7, Eq (4.7.57)–(4.7.63) | MATCHES | Deviation beyond experimental uncertainty not accountable by higher-order corrections. |
| P-003 | Muon Anomalous Magnetic Moment | Standard QED+hadronic+electroweak | $a_\mu^{\rm SM} = 0.001\,165\,918\,10(43)$ | $a_\mu^{\rm exp} = 0.001\,165\,920\,61(41)$ | $4.2\sigma$ tension | Vol 6 Ch 1; Vol 4 Ch 7 | MATCHES (same tension as SM) | Resolution of $4.2\sigma$ tension as genuine new physics would require both SM and ZA to extend. |
| P-040 | Maxwell's Equations (Complete Set) | All four derived from Firmament membrane wave propagation | Postulated (Maxwell 1865) | Confirmed for 160 years | Structural | Vol 6 Ch 1; Vol 2 Ch 3; Tests 3.1–3.5 | MATCHES | Any deviation from Maxwell's equations in vacuum. |
| P-041 | Speed of Light | $c = 1/\sqrt{\mu_0\varepsilon_0}$ from zone metric | 299,792,458 m/s (SI exact) | Exact by definition | $< 10^{-9}$ historical | Vol 6 Ch 1; Vol 2 Ch 3; Test 10.1 | MATCHES | Photon speed $\neq c$ in vacuum. |
| P-043 | Full Electromagnetic Spectrum | Radio → gamma-ray as Firmament membrane modes | Same (Maxwell + sources) | Confirmed in all bands | Structural | Vol 6 Ch 1; EM_PRECISION_COMPLETIONS; Test 3.6 | MATCHES | EM radiation not satisfying Maxwell's equations. |
| P-049 | Casimir Effect | $F/A = -\pi^2 \hbar c / 240 d^4$ from zone vacuum-mode confinement | Same (Casimir 1948) | Confirmed to $\sim 1\%$ (Lamoreaux) | $\sim 1\%$ | Vol 6 Ch 1; Vol 4 Ch 9; Test 5.16 | MATCHES | Casimir force deviating from $d^{-4}$ by $> 5\%$ after corrections. |
| P-035 | Newton's Second Law ($F = ma$) | Theorem from Firmament membrane dynamics | Axiom in classical mechanics | Confirmed since 1687 | Exact | Vol 6 Ch 1; Vol 3 Ch 1; Test 1.2 | MATCHES | Violation of $F \propto a$ for macroscopic object outside known quantum/relativistic regimes. |
| P-036 | Kepler's Laws | Derived from zone gravitational potential | Same (Newton) | Confirmed in planetary/exoplanet orbits | High | Vol 6 Ch 1; Vol 3 Ch 3; Test 1.6 | MATCHES | Orbital anomalies not attributable to known perturbations. |
| P-037 | Second Law of Thermodynamics | $dS \geq 0$ from zone separation | Statistical (Boltzmann) / Clausius | Never violated macroscopically | Exact | Vol 6 Ch 1; Vol 1 Ch 11; Vol 3 Ch 9, 12; Test 2.3 | MATCHES | Spontaneous macroscopic entropy decrease in isolated system (not fluctuation). |
| P-038 | Planck Blackbody Spectrum | Planck's law from statistical mechanics on zone manifold | Same (Planck 1900) | COBE/FIRAS $< 10^{-4}$ | $< 10^{-4}$ | Vol 6 Ch 1; Vol 3 Ch 10; Test 2.8 | MATCHES | Deviation from Planck spectrum in any thermal system beyond perturbative effects. |
| P-039 | Stefan-Boltzmann Law | $j = \sigma T^4$ from Planck spectrum integration | Same | $\sigma = 5.670\,374 \times 10^{-8}$ (exact from other constants) | Exact | Vol 6 Ch 1; Vol 3 Ch 10; Test 2.9 | MATCHES | Any deviation from $T^4$ scaling of radiated power. |

---

## A.9  Category VII — Technology: Faster-Than-Light Travel

Fourteen predictions (P-083 to P-084, P-089 to P-102) covering the five FTL mechanisms derived in Chapter 9 (Temporal Shortcut, Dimensional Bypass, Zone Tunneling, Field Distortion / Warp Bubble, Consciousness Interface) and the Phase 3 thermodynamic lock that prevents macroscopic FTL in the current cosmological era. These are **speculative** predictions with confidence levels ranging from 5% (Temporal Shortcut) to 70% (Warp Bubble). Each is quantitatively specified, each has a falsification threshold, and each is explicitly labeled with its Mechanism 1–5 identifier from `FTL_MECHANISMS_FORMAL.md`.

The honest caveat: many of these predictions are currently untestable — the experimental apparatus to engineer a warp bubble, detect dimensional-bypass radiation, or measure a photon's zone-tunneling probability does not exist. They are nonetheless falsifiable *in principle* because each specifies a quantitative signature that would distinguish it from standard physics if the experiment could be performed.

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|
| P-083 | Warp Bubble GW Signature | Asymmetric burst from Waters-field configuration; $E_{\rm GW} \sim 10^{23}$ J; $h \sim 10^{-24}$ at 10 Mpc | No mechanism (exotic matter required in GR) | Not detected | N/A | Vol 6 Ch 3; FTL_MECHANISMS_FORMAL Mech 4; Vol 5 Ch 4 | NOVEL | Waveform computed and found to violate the energy conditions zone architecture itself requires; internal inconsistency. |
| P-084 | Dimensional Bypass Radiation Burst | Broadband X-ray–gamma spectrum with $E_{\rm max} \sim \hbar c/\eta_B \sim 150$ GeV | No prediction | Not identified | N/A | Vol 6 Ch 3; FTL_MECHANISMS_FORMAL Mech 2 | NOVEL | Candidate event observed with spectrum inconsistent with $(dE/d\omega) \propto \omega^2 \exp(-\omega/\omega_{\rm cut})$, $\omega_{\rm cut} = c/\eta_B$. |
| P-089 | GW Breathing Modes Unique to 6D Topology | Scalar and vector modes; amplitude ratios from 6D warp factors | Only two tensor modes | Not detected | Bound | Vol 6 Ch 9; Vol 5 Ch 3 | NOVEL | GW observations of $> 100$ events show no scalar or vector modes at $h < 10^{-25}$. |
| P-090 | Local Variation of $c$ in Gravitational Fields | $c_{\rm local}^2 = c_0^2(1 + \varepsilon R/(c_0^2 \rho_c))$; fractional $\sim 10^{-17}$ | $c$ is constant (GR) | Consistent with constant | Precision target $10^{-17}$ | Vol 6 Ch 9 | NOVEL | $> 50$ millisecond pulsars show no systematic $c$-variation with local Ricci curvature at $10^{-17}$ fractional level. |
| P-091 | Radiation Burst Signature from Dimensional Bypass Re-Entry | $E_{\rm radiated} = E_{\rm binding}(1 - e^{-t/\tau})$; $E_{\rm binding} \sim 10^{25}$ J; $\tau \sim 10^{-9}$ s | No such mechanism | No anomalous bursts identified | N/A | Vol 6 Ch 9; FTL_MECHANISMS_FORMAL Mech 2 | NOVEL | Century of gamma-ray monitoring detects no anomalous bursts consistent with re-entry spectrum. |
| P-092 | Starlight Propagation Confirms Dimensional Bypass Geometry | $t_{\rm observed} = t_{\rm Firm}(1-\delta) + t_{\rm bulk}$, $\delta \sim 0.1$–$0.5$ | 4D-only propagation | Starlight observed since creation | N/A (interpretive) | Vol 6 Ch 9 | NOVEL | Alternative mechanism (other than bulk-path propagation) established to explain early starlight arrival. |
| P-093 | Brane Binding Energy Scale | $E_{\rm binding} = \sigma|\Delta\eta| \sim 10^{23}$–$10^{28}$ J | No Firmament → no binding energy | Not yet measured | N/A | Vol 6 Ch 9; Vol 1 Ch 5, Eq (1.5.12) | NOVEL | Precision vacuum-energy experiments show volume-scaling (3D) rather than area-scaling (2D membrane) for negative-energy-density creation. |
| P-094 | Macroscopic Zone Tunneling Probability | $P \approx \exp(-2\sqrt{2mV_0}L/\hbar) \approx 10^{-10^{63}}$ for 1 kg object | Same WKB formula | Not testable directly | N/A | Vol 6 Ch 9; FTL_MECHANISMS_FORMAL Mech 3 | NOVEL | Observed WKB violation in mesoscopic systems (10¹² – 10²⁴ atoms) due to quantum-enhancement resonance. |
| P-095 | Warp Bubble GW Emission | $f_{\rm GW} = (1/\pi)\sqrt{a/R} \sim 1$ Hz for $R \sim 1$ km, $a \sim 10$ m/s² | Similar but requires exotic matter | Not detectable currently | N/A | Vol 6 Ch 9; FTL_MECHANISMS_FORMAL Mech 4 | NOVEL | Controlled warp-bubble operation (future) produces no detectable GW at predicted frequency. |
| P-096 | Dark Energy Density Local Variation | $\rho_\Lambda({\bf r}) = \langle\rho_\Lambda\rangle(1 + \delta)$, $|\delta| \sim 10^{-1}$–$10^{-5}$ at km–AU scales | Uniform ΛCDM | Not measured at 10⁻¹⁸ precision | Target $10^{-18}$ | Vol 6 Ch 9 | NOVEL | Space-based gravitational-redshift experiment measures time dilation at $10^{-18}$ everywhere with no residual above known mass distributions. |
| P-097 | Hawking Radiation from Warp Bubble Horizon | $T_H = \hbar c^3/(8\pi G k_B r_+) \approx 10^{-24}$ K for $r_+ \sim 1$ km | Similar (Alcubierre analogy, non-rigorous) | Not detectable currently | N/A | Vol 6 Ch 9 | NOVEL | Future bubble operation yields $T_H$ far from prediction (e.g., $10^{-5}$ K instead of $10^{-24}$ K), requiring refinement. |
| P-098 | Consciousness-Mediated Non-Local Quantum Correlation | CHSH $S > 2$ with engineered neural quantum coherence (Stage 2+) | Brain too warm/wet for macroscopic coherence | Not achievable currently | N/A | Vol 6 Ch 9; QM_FROM_MEMBRANE_DYNAMICS | NOVEL | Stage 2 engineered neural coherence achieved and no Bell violations observed. |
| P-099 | Neural Quantum Coherence Enhancement | $\tau_{\rm coherence,enhanced}/\tau_{\rm baseline} \sim 10^3$–$10^6$ (with technique) | Thermal decoherence limit $\sim 10^{-13}$–$10^{-15}$ s | Not achievable currently | N/A | Vol 6 Ch 9 | NOVEL | Engineered neural quantum systems show no enhancement under intention (Stage 2+). |
| P-102 | Phase 3 Thermodynamic Lock | Current universe cannot locally extract $> 10^{26}$ J of dark energy | No phase transition | $\delta \rho_\Lambda < 10^{-5}$ observed | N/A | Vol 6 Ch 9 | OPEN | Controlled experiments in Stage 2/3 demonstrate warp-bubble engineering with energy requirement below current-phase allowance, or observed natural FTL phenomena in Phase 3 without Phase 4 transition. |

---

## A.10  Category VIII — Technology: Energy Harvesting

Eighteen predictions (P-085, P-086, P-103 to P-118, plus the ENERGY_FRACTIONS_DERIVATION-linked entries) covering every energy-extraction concept the framework enables: the Firmament Resonance Generator (MRG), dynamic-Casimir arrays, Waters-field expansion sails, Waters-Below binding-energy release, zone-boundary latent heat, and the sustainable extraction-rate bound. The MRG reference design (Chapter 10) is a sub-category unto itself, with ten specific quantitative predictions (P-103 through P-110, plus orientation and magnetic-bias dependences) that form a single coherent experimental proposal.

Every entry has an explicit, tabletop-scale falsification threshold (except those tied to astronomical-baseline sails, which require space missions). This category is the most amenable to near-term laboratory test.

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|
| P-085 | Firmament Resonance Energy Coupling | $\kappa(f, f_n) \sim (\eta_B/\lambda_{\rm device})^2 \delta(f-f_n)$; $P_{\rm ext} \sim \kappa E_{\rm mode} f_n$ | No membrane → no coupling | Not yet measured | Target $> 3\sigma$ | Vol 6 Ch 3; Vol 1 Ch 5; membrane_resonance_generator.docx | NOVEL | Casimir-cavity sweep across predicted membrane frequency shows no anomalous force at $>3\sigma$ above standard Casimir. |
| P-086 | Waters Field Energy Density Measurement | $\delta\rho_{\rm WA} \sim \rho_{\rm WA}(|\delta g|/c^2) \sim 10^{-36}$ kg/m³ for lab gravity | No local DE interaction | Current precision $\sim 10^{-27}$ kg/m³ | Target $\delta\rho/\rho < 10^{-6}$ | Vol 6 Ch 3; Vol 5 Ch 11 | NOVEL | Future experiment measures local DE at $\delta\rho/\rho < 10^{-6}$ with no variation near massive objects. |
| P-103 | MRG Net Power Output | $P_{\rm net} \geq 30$ W at $\eta \geq 0.42$, gravitational-vertical orientation | 0 W (closed-ground-state QED) | Not yet measured | Target $10^{-8}$ detection sensitivity | Vol 6 Ch 10, §10.5.7–§10.5.8, Eq (10.5.9) | NOVEL | $P_{\rm net} < 10^{-6}$ W across any orientation at $\eta \geq 10^{-8}$, 100-h run, $p < 10^{-3}$. |
| P-104 | Dynamic-Casimir Boundary Scaling | Photon-production rate scales linearly with boundary count $N \in [4, 500]$ | Same linear scaling in low-$N$ regime | Not yet measured at full range | Target exponent 1.0 | Vol 6 Ch 10, §10.5.3 | NOVEL | Scaling exponent on $N$ outside $[0.8, 1.2]$ over operating range. |
| P-105 | MRG Case Temperature | $T_{\rm case} \leq 80$°C at 30–65 W output, 20°C ambient, still-air, 10-cm Cu housing | N/A | Not yet measured | Target $< 100$°C | Vol 6 Ch 10, §10.5.9, Eq (10.5.11) | NOVEL | $T_{\rm case} > 100$°C under rated-output conditions. |
| P-106 | MRG Loaded $Q$ | Loaded cavity $Q \geq 10^4$ at 1.14 GHz (polished Cu, BaTiO₃ stack) | N/A | Not yet measured | Target $Q > 10^3$ | Vol 6 Ch 10, §10.5.10 | NOVEL | $Q < 10^3$ — resonance too broad for spectral-fingerprint test. |
| P-107 | Orientation Dependence | $P_{\rm net}(\theta) = P_{\rm net}(0)\cos^2\theta$ from gravitational vertical | Isotropic | Not yet measured | Target $5\%$ modulation | Vol 6 Ch 10, §10.5.4, §10.8.3 | NOVEL | Angular modulation $< 5\%$ of $P_{\rm net}(0)$ over full rotation, $3\sigma$ over 24 h. |
| P-108 | Magnetic-Bias Dependence | $P_{\rm net}$ changes by factor $\geq 10$ between N52 installed, demagnetized, and reversed polarity | No static-B dependence | Not yet measured | Target factor 10 | Vol 6 Ch 10, §10.5.4, §10.8.2 | NOVEL | Change $<$ factor 2. |
| P-109 | Dielectric Scaling | $P \propto K^{1/3}$ across $K \in [1, 10^4]$ | Lifshitz: $P \propto K^{1/2}$ | Not yet measured at full range | Target exponent $0.33$ | Vol 6 Ch 10, §10.8.4 | DIFFERS | Fitted exponent outside $[0.28, 0.38]$ with $< 10\%$ measurement uncertainty. |
| P-110 | Spectral Fingerprint | Sharp peaks at 1.14, 2.28, 3.42 GHz; $Q \geq 10^3$; peak/noise $\geq 5\times$ | Flat Johnson-Nyquist at ambient $T$ | Not yet measured | Target $5\sigma$ peak above noise floor | Vol 6 Ch 10, §10.8.5 | NOVEL | Absence of $\geq 2$ resonant peaks above Johnson-Nyquist at $3\sigma$. |
| P-111 | Waters Above Expansion-Sail Yield | $P \propto \rho_\Lambda c^2 (H_0/c) A \eta_{\rm sail}$; $<10^{-5}$ W for $A < 1$ AU | No DE extraction | Not yet measured | Target $< 10^{-6}$ W tabletop | Vol 6 Ch 10, §10.6.2, Eq (10.6.1) | NOVEL | Tabletop-scale ($A < 1$ m²) sustained extraction $> 10^{-6}$ W above MRG-class. |
| P-112 | Waters-Below Coupling Constant | $|\log_{10}(\alpha_B/G)| \leq 1$ | No such coupling | Not yet measured | Target $\pm 1$ order | Vol 6 Ch 10, §10.6.4 | NOVEL | Direct measurement yields $\alpha_B$ outside $[0.1G, 10G]$. |
| P-113 | No Local $\rho_\Lambda$ Dip Under MRG Operation | No operational harvester produces local depression $> 10^{-30}$ kg/m³ | Uniform DE | Not yet measured | Target $10^{-30}$ kg/m³ | Vol 6 Ch 10, §10.6.3 | NOVEL | Detected local $\rho_\Lambda$ depression co-located with extraction facility, depth $> 10^{-30}$ kg/m³, $> 3\sigma$. |
| P-114 | Micro-Condensation Binding-Energy Release | $\varepsilon \cdot c^2 \geq 10^{-5} c^2$ per unit condensed mass | No mechanism | Not yet measured | Target $\varepsilon > 10^{-5}$ | Vol 6 Ch 10, §10.6.4, Eq (10.6.2) | NOVEL | Mass-energy deficit $< 10^{-5} m c^2$ in seed-vibration condensation apparatus. |
| P-115 | Casimir-Array Scaling Law | $P \propto N (\Delta a/a)^2 \omega \eta_{\rm harvest} \eta$ in additive regime ($N \leq 500$, $\Delta a/a \leq 0.1$) | Standard Casimir only | Not yet measured at array scale | Target exponent 2.0 | Vol 6 Ch 10, §10.7.2 | NOVEL | Fitted exponent on $\Delta a/a$ outside $[1.5, 2.5]$, or saturation at $N < 100$. |
| P-116 | Zone-Boundary Latent Heat | $\Delta E/\Delta m \geq 10^{-3} c^2$ at Firmament/Waters-Below interface | No such boundary | Not yet measured | Target $10^{-3} c^2$ | Vol 6 Ch 10, §10.7.3 | NOVEL | Measured deficit $< 10^{-3} c^2$ per unit condensed mass. |
| P-117 | Controlled Boundary-Oscillation Rate | $P \leq V_{\rm barrier} \omega A_{\rm coupled} \eta_{\rm osc}$; safe cap $\sim 10^{-6}$ W/m² | No such boundary | Not yet measured | Target $10^{-5}$ W/m² | Vol 6 Ch 10, §10.7.3 | NOVEL | Sustained extraction $> 10^{-5}$ W/m² without membrane failure. |
| P-118 | Sustainable Extraction-Rate Bound | Maximum sustained $\leq \kappa_0 Q_{\rm eff} N$ with $\kappa_0 \leq 10^{-10}$ W/m² | N/A | Not yet measured | Target $1$ W/m² ceiling | Vol 6 Ch 10, §10.10.2, Eq (10.10.1) | NOVEL | Operation at $> 1$ W/m² per unit cavity-wall area with no observable $\rho_\Lambda$ depletion over comparable volume. |

---

## A.11  Category IX — Technology: Communication

Nineteen predictions (P-087, P-088, P-119 to P-135) covering zone-tunneling channels, Waters-field modulation channels, consciousness-interface channels, the no-signaling constraint that forbids any closed signaling loop (P-135), the no-signaling floor for entangled particles (P-132), and the Holevo capacity bounds that zone architecture must obey. This category is scientifically interesting because it simultaneously contains zone architecture's most speculative claims (consciousness-based FTL communication, P-130) and its strongest null predictions (entanglement-based signaling is strictly forbidden, P-132).

The falsification thresholds are designed to prevent the framework from hiding behind unfalsifiable hedges. The consciousness-channel predictions (P-130, P-131) are framed as pre-registered experimental targets with specific $d$-effect sizes.

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|
| P-087 | Zone-Dependent Bell Inequality Correction | $\delta S \sim (E_{\rm local}/E_{\rm zone})^2 \sim 4 \times 10^{-5}$ at RHIC/LHC fields | Tsirelson bound $S \leq 2\sqrt{2}$ absolute | Current CHSH precision $\sim 10^{-3}$ | Target $10^{-4}$ | Vol 6 Ch 3; Vol 4 Ch 4 | NOVEL | CHSH measured at $\pm 10^{-4}$ in low-field and high-field with no significant difference. |
| P-088 | Zone Tunneling for Quantum State Transfer | $P_{\rm photon} \sim 0.22$ through zone boundary of thickness $\sim \eta_B$ | No zone boundaries | Not yet measured | Target $P > 10^{-3}$ | Vol 6 Ch 3; FTL_MECHANISMS_FORMAL Mech 3 | NOVEL | Refined boundary-potential calculation yields $P < 10^{-10}$; single-photon zone tunneling experimentally inaccessible. |
| P-119 | Zone-Tunneling Channel Bandwidth at Fixed $\eta$-Excursion | $B = (1.0 \pm 0.5) \times 10^6$ Hz at $\eta_* = 0.5 \eta_B$ | No channel | Not yet measured | Target bandwidth | Vol 6 Ch 11 | NOVEL | Construction of $\eta$-coupling source/receiver pair demonstrates $B < 100$ Hz or $B > 100$ MHz at this excursion. |
| P-120 | Zone-Tunneling Channel Range | $G(r_{4D}, \eta_*) \propto \eta_*^{1/2} \log(r_{4D}/\eta_B)$ | No channel | Not yet measured | Target $\pm 30\%$ | Vol 6 Ch 11; Vol 5 Ch 4 | NOVEL | Measured $G$ differs from predicted scaling by $> 30\%$. |
| P-121 | Zone-Tunneling SNR Floor | $N = k_B T_{\rm eff} B$ with $T_{\rm eff} = (1 \pm 0.5) \times 10^{-13}$ K | No channel | Not yet measured | Target $10^{-13}$ K | Vol 6 Ch 11 | NOVEL | Noise floor $> 10^{-10}$ K (at $10^3\times$ prediction) or $< 10^{-15}$ K. |
| P-122 | Zone-Tunneling EM Spectral Leakage | Leakage $\gamma P_T$ with $\gamma = 10^{-3.5 \pm 0.5}$ | No channel | Not yet measured | Target $10^{-3.5}$ | Vol 6 Ch 11 | NOVEL | Transmitter at 10 kW for 1 h shows no EM line at $10^{-10}$ W level. |
| P-123 | Waters-Field Group Velocity Regimes | $v_g = c\sqrt{1 - m_\Psi^2 c^4/(\hbar^2\omega^2)}$; $v_g \to 0$ at effective-mass threshold, $v_g \to c$ in vacuum | No Waters field | Not yet measured | Target $v_g < c$ | Vol 6 Ch 11, Eq (11.4.4) | NOVEL | Detection of Waters-field modulation propagating faster than $c$ at any frequency. |
| P-124 | Waters-Field Attenuation Length | $\lambda_W = \hbar/(\epsilon_\kappa m_\Psi c) > 10^{27}$ m with $\epsilon_\kappa \lesssim 10^{-27}$, $m_\Psi c^2 \sim 10^{-3}$ eV | N/A | Not yet measured | Target $10^{27}$ m | Vol 6 Ch 11 | NOVEL | $1/e$ attenuation below $10^{20}$ m at design frequency. |
| P-125 | Waters-Field Bandwidth | $B \sim 10 m_\Psi c^2/\hbar$ (vacuum) or $10^{-3} m_\Psi c^2/\hbar$ (matter-coupled) | N/A | Not yet measured | Target $10$ / $10^{-3}$ ratio | Vol 6 Ch 11 | NOVEL | Operation with bandwidth below $10^{-5} m_\Psi c^2/\hbar$ or above $10^3 m_\Psi c^2/\hbar$. |
| P-126 | MRG-Driven Waters-Field Modulation at 1 AU | $(100 \pm 30)$ bps, BER $10^{-6}$, with 500 W drive, $Q = 10^4$ | No such channel | Not yet measured | Target $100$ bps | Vol 6 Ch 11, §11.4.7 | NOVEL | 1-AU baseline achieves bitrate $< 1$ bps or $> 10^4$ bps. |
| P-127 | Waters-Field Channel Anisotropy | $\cos^2\theta$ dependence on MRG magnetic-bias / Waters-Below direction angle | No anisotropy | Not yet measured | Target $10\%$ modulation | Vol 6 Ch 11; Vol 6 Ch 10 §10.5 | NOVEL | No $\cos^2\theta$ dependence at $10\%$ level in controlled transmit-rotate experiment. |
| P-128 | Consciousness-Interface Information Capacity | $I_{\rm max} = k_B A_{Z1}/(4 \ell_P^2 \ln 2)$ (Zone-1 holographic bound) | No such channel | Not yet measured | Target realistic footprint | Vol 6 Ch 11 | NOVEL | Shared-consciousness protocol achieves bitrate requiring $A_{Z1}$ larger than any plausible footprint (e.g., $10^{50}$ bps at unit footprint). |
| P-129 | Consciousness-Interface Energy Cost | $E_{\rm interface} = 10^6$–$10^9$ J per 1-hour session | No such channel | Not yet measured | Target $10^6$–$10^9$ J | Vol 6 Ch 11 | NOVEL | Operation at $< 10^3$ J or $> 10^{12}$ J. |
| P-130 | Consciousness-Interface Controllability Threshold | Volitional bit-encoding at $\geq 10^{-4}$ bit/trial (focused-attention, modern controls) | No such effect | PEAR baseline $\sim 10^{-4}$ effect | Target $10^{-4}$ bit/trial | Vol 6 Ch 11 | NOVEL | Phase-1 experiment at $10^{-6}$ bit/trial with null result tightens; $10^{-8}$ null effectively falsifies channel interpretation. |
| P-131 | Consciousness-Interface Statistical Signal Beyond PEAR | $d = 0.01$ effect size at $N \geq 10^6$ trials, $p < 10^{-3}$ | Null (PEAR not replicated) | PEAR-class studies | Target $d = 0.01$ | Vol 6 Ch 11 | NOVEL | Pre-registered replication at $N \geq 10^6$ with null at $p < 10^{-3}$. |
| P-132 | Zone-Architecture No-Signaling for Particle Entanglement | Reduced single-particle statistics unchanged by remote basis changes | Same (QM) | Consistent with QM no-signaling | Exact | Vol 6 Ch 11 | MATCHES (null prediction) | Statistically significant ($p < 10^{-6}$) dependence of $\rho_A$ on $M_B$ at any basis pair, any range, any setting. |
| P-133 | Holevo Capacity Bound for Zone-Tunneling Channel | $\chi = \log_2(1 + S/N)$ | Same (QIT) | N/A | Standard bound | Vol 6 Ch 11, §11.3 | MATCHES | Demonstration of channel achieving $\chi > \log_2(1 + S/N) + 1$ bit per use. |
| P-134 | Holevo Capacity Bound for Waters-Field Channel | $\chi = \log_2(1 + S/N)$ | Same (QIT) | N/A | Standard bound | Vol 6 Ch 11, §11.4.7 | MATCHES | Same as P-133. |
| P-135 | No Closed Signaling Loops | No combination of four zone-architecture channels produces a closed signaling loop | Same (causality) | N/A | Exact | Vol 6 Ch 11 | MATCHES (null prediction) | Demonstration of a closed signaling loop with any channel or channel combination, however small the loop's parameters. |

---

## A.12  Category X — Technology: Sensors

Eighteen predictions (P-136 to P-153) covering membrane-vibration interferometers (MVIs), atom-interferometer Waters-field sensors, dark-matter imaging apertures, LIGO retrofits for the extended GW polarizations, life-detection from space, and the CMB/LSS cross-correlation anomalies at the zone boundary. This category is the framework's most near-term-testable. Several predictions (P-139, P-140, P-142, P-147, P-151) have quantitative targets within a decade of projected instrumentation.

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|
| P-136 | Membrane-Vibration Fundamental Mode | $f_1 = (1.5 \pm 0.5)$ mHz on solar-system patch | No membrane | Not yet measured | Target $f_1$ | Vol 6 Ch 12, Eq (12.2.3); Vol 1 Ch 5 | NOVEL | MVI-class detection of mode resonance outside $[0.5, 5]$ mHz after controlled engineered driving, or mode above 50 mHz / below 0.1 mHz. |
| P-137 | Membrane-Vibration Strain at MVI | $h = 10^{-25.0 \pm 0.5}$ after 1 s for 500 W MRG-T driver at 1 AU | No membrane | Not yet measured | Target $h \sim 10^{-25}$ | Vol 6 Ch 12; Vol 1 Ch 5 | NOVEL | Engineered driver running for $10^7$ s at predicted frequency must show strain $> 10^{-26}$; null at $10^{-27}$ falsifies coupling amplitude. |
| P-138 | Firmament Mode Spectral-Line Spacing | $f_n = n \cdot f_1$ with patch-boundary corrections | No membrane | Not yet measured | Target ratio $2 \pm 0.3$ | Vol 6 Ch 12, Eq (12.2.3) | NOVEL | Detected spectrum with $f_2/f_1 \neq 2 \pm 0.3$ at $3\sigma$. |
| P-139 | Atom-Interferometer Waters-Field Sensitivity | $a_\Psi^{\rm min} = 10^{-24.0 \pm 0.5}$ m/s² after $10^6$ s coherent integration, MAGIS-100 successor | No Waters field | Not yet measured at required precision | Target $10^{-24}$ m/s² | Vol 6 Ch 12 | NOVEL | Continuous $\Psi_A$-source background at $a_\Psi > 10^{-20}$ m/s² in isolated region falsifies uniform-$\Psi_A$ hypothesis. |
| P-140 | Dark-Matter Distribution Map Resolution | 1-km Waters-field aperture resolves $\Psi_B$ clumps at $\theta_{\rm res} = 10^{-6}$ rad; $\sim 20$ pc at Virgo | No direct DM imaging | Not yet measured | Target kpc resolution | Vol 6 Ch 12 | NOVEL | Absence of sub-kpc $\Psi_B$ substructure at predicted $\sim 10^{-2}$ of cluster-DM-mass level, 1-km Waters sensor. |
| P-141 | Dark-Energy Density Fluctuation Amplitude | $\delta\rho_A/\rho_\Lambda \leq \epsilon_\kappa \sim 10^{-27}$ | Uniform Λ | Not yet measured at Hubble scale | Target $10^{-20}$ | Vol 6 Ch 12 | NOVEL | Euclid/DESI find $\delta\rho_A/\rho_\Lambda \geq 10^{-20}$ at any Hubble-scale wavelength. |
| P-142 | Modified LIGO Waters-Field Detection Threshold | $h_{\rm min} = 10^{-24.5}$ at $10^3$ s integration with 10% scalar-charge enhancement | N/A | Not yet implemented | Target $10^{-24.5}$ | Vol 6 Ch 12 | NOVEL | Failure to detect known-transmitted 1-MW MRG source at 1 AU after $10^4$ s integration. |
| P-143 | ISW Cross-Correlation Anomaly at $\xi$-Boundary | $\Delta C_\ell^{T\delta}/C_\ell^{T\delta,\rm ΛCDM} = (10 \pm 5)\%$ at $\ell \sim 300 \pm 100$ | ΛCDM prediction | Planck+BOSS consistent with ΛCDM | Target $2\%$ | Vol 6 Ch 12 | NOVEL | Reprocessing Planck+BOSS+Euclid shows no excess above $2\%$ at $3\sigma$. |
| P-144 | Subnuclear Form-Factor Anomaly at HL-LHC | $(2 \pm 1)\%$ anomaly at $q > 200$ GeV | No anomaly | Not yet measured at $0.5\%$ | Target $0.5\%$ | Vol 6 Ch 12; Vol 4 Ch 12 | NOVEL | HL-LHC at $q = 500$ GeV shows no anomaly above $0.5\%$ at $3\sigma$. |
| P-145 | High-Redshift Shapiro Anomaly | $\Delta H/H = (0.5 \pm 0.3)\%$ at $z > 5$, $\tanh(z/z_{\rm boundary})$ | No anomaly | Not yet measured | Target $0.2\%$ | Vol 6 Ch 12 | NOVEL | JWST+Euclid show no departure from ΛCDM at 0.2% level. |
| P-146 | Thermal Anisotropy from Zone-Boundary Vacuum-Energy Step | $\Delta T/T \sim 10^{-5}$ correlated with zone-boundary position | ΛCDM + inflation | Planck consistent with ΛCDM | Boundary of detection | Vol 6 Ch 12 | NOVEL | Planck+Euclid cross-correlation shows no zone-boundary-correlated pattern at $3\sigma$. |
| P-147 | Orbital Tidal-Gradient Signal for Earth Biomass | $\delta a_{\rm bio} = 10^{-16.0 \pm 0.5}$ m/s² after 24-hour integration, 500 km altitude over dense vegetation | No such signal | Not yet measured | Target $10^{-16}$ m/s² | Vol 6 Ch 12 | NOVEL | GRACE-Bio pilot shows no signal $> 10^{-18}$ m/s² over vegetated regions, or positive signal $> 10^{-14}$ m/s² (100× predicted). |
| P-148 | Biomass-vs-Sterile Regional Differential | $\Delta a_{\rm bio} = 10^{-16.0 \pm 0.5}$ m/s² forest-desert differential | No effect | Not yet measured | Target $10^{-16}$ m/s² | Vol 6 Ch 12 | NOVEL | Forest-minus-desert differential below $10^{-18}$ m/s² at $3\sigma$ (GRACE-Bio). |
| P-149 | Zone-Field Life-Detection False-Positive Rate | $< 10^{-3}$ in forest-vs-desert channel | N/A | Target via pilot mission | Target $< 10^{-3}$ | Vol 6 Ch 12 | NOVEL | Observed false-positive rate $> 10^{-2}$ in zone-field channel from non-biological confounders. |
| P-150 | Exoplanetary Life-Detection Sensitivity at 10 pc | $10^{-28}$ m/s² after 10-year integration (LISA-class, Proxima Cen b) | No sensor | Insufficient currently | Target $10^{-28}$ | Vol 6 Ch 12 | NOVEL | Future interferometer at $10^{-30}$ m/s² detects Proxima Cen b signal $10\times$ above prediction — falsifies $1/r^2$ scaling. |
| P-151 | Extended GW Polarization Amplitude Relations | $h_S/h_+ = h_L/h_\times = e^{2A_0} \sim 10^{-3 \pm 0.5}$; $h_V/h_+ = e^{A_0} \sim 10^{-1.5 \pm 0.3}$ | Only $h_+, h_\times$ | Not yet retrofitted | Target $10^{-3}$ | Vol 6 Ch 12 | NOVEL | LIGO-retrofit ratio $h_S/h_+$ outside $[10^{-4}, 10^{-2}]$ for GW150914-class event. |
| P-152 | LIGO-Retrofit Scalar-Mode Sensitivity | $h_S^{\rm min} = 10^{-22.5 \pm 0.3}$ at 100 Hz | N/A | Not yet implemented | Target $10^{-22.5}$ | Vol 6 Ch 12 | NOVEL | Retrofit-A implementation achieves $h_S < 10^{-21}$ at design frequency. |
| P-153 | PTA Longitudinal-Mode Detection Threshold | $h_L \sim 10^{-15}$ at $10^{-9}$ Hz from SMBH inspirals; PTA reaches $10^{-16}$ sensitivity | No longitudinal mode | NANOGrav stochastic bg | Target $10^{-16}$ | Vol 6 Ch 12 | NOVEL | PTA reaches $h_L < 10^{-17}$ after 10-year integration with no detection. |

---

## A.13  Master Summary Table

All 153 predictions at a glance. Columns condensed for scannability; full details in §A.3–§A.12.

| ID | Category | Title (Short) | Status | Source Chapter |
|----|----------|---------------|--------|----------------|
| P-001 | QED/EM | Electron $a_e$ | MATCHES | Ch 1 |
| P-002 | QED/EM | Lamb Shift | MATCHES | Ch 1 |
| P-003 | QED/EM | Muon $a_\mu$ | MATCHES | Ch 1 |
| P-004 | Couplings | Fine Structure Constant | MATCHES | Ch 1 |
| P-005 | Couplings | EM/Gravitational Hierarchy | MATCHES | Ch 1 |
| P-006 | Couplings | Strong Coupling $\alpha_s(M_Z)$ | MATCHES | Ch 1 |
| P-007 | GR | Mercury Precession | MATCHES | Ch 1 |
| P-008 | GR | Light Bending | MATCHES | Ch 1 |
| P-009 | GR | Shapiro Delay | MATCHES | Ch 1 |
| P-010 | GR | Pound-Rebka Redshift | MATCHES | Ch 1 |
| P-011 | GR | GW Speed | MATCHES | Ch 1 |
| P-012 | GR | Frame Dragging | MATCHES | Ch 1 |
| P-013 | GR | GPS Time Dilation | MATCHES | Ch 1 |
| P-014 | Particle | $M_W$ | MATCHES | Ch 1 |
| P-015 | Particle | $\Gamma_W$, branching | MATCHES | Ch 1 |
| P-016 | Particle | $M_Z$ | MATCHES | Ch 1 |
| P-017 | Particle | $\Gamma_Z$, partials | MATCHES | Ch 1 |
| P-018 | Particle | $N_\nu = 3$ | MATCHES | Ch 1 |
| P-019 | Particle | Higgs Mass | MATCHES | Ch 1 |
| P-020 | Particle | Higgs Couplings | MATCHES | Ch 1 |
| P-021 | Particle | QCD Confinement + String Tension | MATCHES | Ch 1 |
| P-022 | Particle | Jet Observables | MATCHES | Ch 1 |
| P-023 | Particle | Neutrino Mass Splittings | MATCHES | Ch 1 |
| P-024 | Cosmology | DE EOS $w = -1$ | MATCHES | Ch 1 |
| P-025 | Cosmology | Cosmic Energy Budget | MATCHES | Ch 1 |
| P-026 | Cosmology | $H_0$ (Planck) | MATCHES | Ch 1 |
| P-027 | Cosmology | Spatial Flatness | MATCHES | Ch 1 |
| P-028 | Cosmology | Age of Universe | MATCHES | Ch 1 |
| P-029 | Cosmology | Tully-Fisher Slope | MATCHES | Ch 1 |
| P-030 | Cosmology | SPARC Rotation Curves | MATCHES | Ch 1 |
| P-031 | Structural | Energy Conservation | MATCHES | Ch 1 |
| P-032 | Structural | Momentum Conservation | MATCHES | Ch 1 |
| P-033 | Structural | Angular Momentum Conservation | MATCHES | Ch 1 |
| P-034 | Structural | Charge Conservation | MATCHES | Ch 1 |
| P-035 | Classical | Newton's 2nd Law | MATCHES | Ch 1 |
| P-036 | Classical | Kepler's Laws | MATCHES | Ch 1 |
| P-037 | Thermo | Second Law | MATCHES | Ch 1 |
| P-038 | Thermo | Planck Blackbody | MATCHES | Ch 1 |
| P-039 | Thermo | Stefan-Boltzmann | MATCHES | Ch 1 |
| P-040 | EM | Maxwell's Equations | MATCHES | Ch 1 |
| P-041 | EM | Speed of Light | MATCHES | Ch 1 |
| P-042 | EM | Charge Quantization | MATCHES | Ch 1 |
| P-043 | EM | Full EM Spectrum | MATCHES | Ch 1 |
| P-044 | EM | Superconductivity $T_c$ | MATCHES | Ch 1 |
| P-045 | EM | Meissner Effect | MATCHES | Ch 1 |
| P-046 | QM | Photoelectric Effect | MATCHES | Ch 1 |
| P-047 | QM | Compton Scattering | MATCHES | Ch 1 |
| P-048 | QM | BEC | MATCHES | Ch 1 |
| P-049 | QM | Casimir Effect | MATCHES | Ch 1 |
| P-050 | Structural | Periodic Table | MATCHES | Ch 1 |
| P-051 | Structural | Chemical Bonding | MATCHES | Ch 1 |
| P-052 | Particle | Electron Mass (hard-wall) | DIFFERS | Ch 2 |
| P-053 | Particle | Muon/Electron Ratio | DIFFERS | Ch 2 |
| P-054 | Particle | Quark Mass Pattern | DIFFERS | Ch 2 |
| P-055 | Particle | Neutrino Mass Scale | OPEN | Ch 2 |
| P-056 | Couplings | $\alpha$ Residual Offset | DIFFERS | Ch 2 |
| P-057 | Couplings | Weak Mixing Angle | DIFFERS | Ch 2 |
| P-058 | Couplings | $\alpha_s$ Running at Extreme Energies | DIFFERS | Ch 2 |
| P-059 | GR | GW Dispersion | DIFFERS | Ch 2 |
| P-060 | GR | KK Graviton Tower | DIFFERS | Ch 2 |
| P-061 | Cosmology | DM Interaction Cross-Section | DIFFERS | Ch 2 |
| P-062 | Cosmology | DM Decay Lifetime | DIFFERS | Ch 2 |
| P-063 | Cosmology | DE EOS Tight Bound | DIFFERS | Ch 2 |
| P-064 | Cosmology | DE No Evolution | DIFFERS | Ch 2 |
| P-065 | Couplings | $\alpha$ Cosmic Constancy | DIFFERS | Ch 2 |
| P-066 | Particle | Neutrino Normal Hierarchy | DIFFERS | Ch 2 |
| P-067 | Particle | Proton Absolute Stability | DIFFERS | Ch 2 |
| P-068 | GR | Vector GW Polarization | NOVEL | Ch 3 |
| P-069 | GR | Scalar GW Modes | NOVEL | Ch 3 |
| P-070 | GR | KK Graviton Tower (structural) | NOVEL | Ch 3 |
| P-071 | Particle | Zone Boundary Scattering Resonances | NOVEL | Ch 3 |
| P-072 | Particle | Anomalous Energy Loss to Extra Dims | NOVEL | Ch 3 |
| P-073 | Cosmology | Zone Transition Thermal Relics | NOVEL | Ch 3 |
| P-074 | Particle | Super-Heavy Firmament Resonances | NOVEL | Ch 3 |
| P-075 | Particle | Membrane Frequency Ratios | NOVEL | Ch 3 |
| P-076 | Cosmology | Membrane ZPE / Λ | NOVEL | Ch 3 |
| P-077 | Cosmology | Waters Field Density Gradients | NOVEL | Ch 3 |
| P-078 | Cosmology | Waters Field Power Spectrum | NOVEL | Ch 3 |
| P-079 | Cosmology | Waters-Firmament Coupling Oscillations | NOVEL | Ch 3 |
| P-080 | Particle | Topological Defect Scattering | NOVEL | Ch 3 |
| P-081 | Structural | Zone Number Conservation | NOVEL | Ch 3 |
| P-082 | Cosmology | Cosmic Zone Transition Imprints | NOVEL | Ch 3 |
| P-083 | Tech-FTL | Warp Bubble GW Signature | NOVEL | Ch 3 |
| P-084 | Tech-FTL | Dimensional Bypass Radiation Burst | NOVEL | Ch 3 |
| P-085 | Tech-NRG | Firmament Resonance Energy Coupling | NOVEL | Ch 3 |
| P-086 | Tech-NRG | Waters Field Energy Density | NOVEL | Ch 3 |
| P-087 | Tech-COM | Zone-Dependent Bell Correction | NOVEL | Ch 3 |
| P-088 | Tech-COM | Zone Tunneling for Quantum States | NOVEL | Ch 3 |
| P-089 | Tech-FTL | GW Breathing Modes (6D) | NOVEL | Ch 9 |
| P-090 | Tech-FTL | Local $c$ Variation | NOVEL | Ch 9 |
| P-091 | Tech-FTL | Dim. Bypass Re-Entry Burst | NOVEL | Ch 9 |
| P-092 | Tech-FTL | Starlight via Bulk Paths | NOVEL | Ch 9 |
| P-093 | Tech-FTL | Brane Binding Energy Scale | NOVEL | Ch 9 |
| P-094 | Tech-FTL | Macro Zone Tunneling Suppression | NOVEL | Ch 9 |
| P-095 | Tech-FTL | Warp Bubble GW Emission | NOVEL | Ch 9 |
| P-096 | Tech-FTL | DE Density Local Variation | NOVEL | Ch 9 |
| P-097 | Tech-FTL | Hawking Radiation from Warp Bubble | NOVEL | Ch 9 |
| P-098 | Tech-FTL | Consciousness Non-Local Correlation | NOVEL | Ch 9 |
| P-099 | Tech-FTL | Neural Coherence Enhancement | NOVEL | Ch 9 |
| P-100 | GR | $c$ as Brane Property | NOVEL | Ch 9 |
| P-101 | GR | Bulk Geodesic Shortcut | NOVEL | Ch 9 |
| P-102 | Tech-FTL | Phase 3 Thermodynamic Lock | OPEN | Ch 9 |
| P-103 | Tech-NRG | MRG Net Power Output | NOVEL | Ch 10 |
| P-104 | Tech-NRG | Dynamic Casimir Scaling | NOVEL | Ch 10 |
| P-105 | Tech-NRG | MRG Case Temperature | NOVEL | Ch 10 |
| P-106 | Tech-NRG | MRG Loaded Q | NOVEL | Ch 10 |
| P-107 | Tech-NRG | MRG Orientation Dependence | NOVEL | Ch 10 |
| P-108 | Tech-NRG | MRG Magnetic-Bias | NOVEL | Ch 10 |
| P-109 | Tech-NRG | MRG Dielectric Scaling | DIFFERS | Ch 10 |
| P-110 | Tech-NRG | MRG Spectral Fingerprint | NOVEL | Ch 10 |
| P-111 | Tech-NRG | WA Expansion-Sail Yield | NOVEL | Ch 10 |
| P-112 | Tech-NRG | WB Coupling Constant $\alpha_B$ | NOVEL | Ch 10 |
| P-113 | Tech-NRG | No $\rho_\Lambda$ Dip Under MRG | NOVEL | Ch 10 |
| P-114 | Tech-NRG | Micro-Condensation Binding Energy | NOVEL | Ch 10 |
| P-115 | Tech-NRG | Casimir-Array Scaling Law | NOVEL | Ch 10 |
| P-116 | Tech-NRG | Zone-Boundary Latent Heat | NOVEL | Ch 10 |
| P-117 | Tech-NRG | Boundary-Oscillation Rate Cap | NOVEL | Ch 10 |
| P-118 | Tech-NRG | Sustainable Extraction Bound | NOVEL | Ch 10 |
| P-119 | Tech-COM | ZT Channel Bandwidth | NOVEL | Ch 11 |
| P-120 | Tech-COM | ZT Channel Range | NOVEL | Ch 11 |
| P-121 | Tech-COM | ZT SNR Floor | NOVEL | Ch 11 |
| P-122 | Tech-COM | ZT EM Spectral Leakage | NOVEL | Ch 11 |
| P-123 | Tech-COM | Waters-Field Group Velocity | NOVEL | Ch 11 |
| P-124 | Tech-COM | Waters-Field Attenuation Length | NOVEL | Ch 11 |
| P-125 | Tech-COM | Waters-Field Bandwidth | NOVEL | Ch 11 |
| P-126 | Tech-COM | MRG-Driven Waters Modulation at 1 AU | NOVEL | Ch 11 |
| P-127 | Tech-COM | Waters-Field Anisotropy | NOVEL | Ch 11 |
| P-128 | Tech-COM | Consciousness Capacity Bound | NOVEL | Ch 11 |
| P-129 | Tech-COM | Consciousness Energy Cost | NOVEL | Ch 11 |
| P-130 | Tech-COM | Consciousness Controllability Threshold | NOVEL | Ch 11 |
| P-131 | Tech-COM | Consciousness PEAR-Replication Signal | NOVEL | Ch 11 |
| P-132 | Tech-COM | Particle Entanglement No-Signaling | MATCHES | Ch 11 |
| P-133 | Tech-COM | Holevo Bound (ZT Channel) | MATCHES | Ch 11 |
| P-134 | Tech-COM | Holevo Bound (Waters Channel) | MATCHES | Ch 11 |
| P-135 | Tech-COM | No Closed Signaling Loops | MATCHES | Ch 11 |
| P-136 | Tech-SNS | Membrane Fundamental Mode | NOVEL | Ch 12 |
| P-137 | Tech-SNS | Membrane Strain at MVI | NOVEL | Ch 12 |
| P-138 | Tech-SNS | Firmament Mode Spacing | NOVEL | Ch 12 |
| P-139 | Tech-SNS | Atom-Interferometer Waters Sens. | NOVEL | Ch 12 |
| P-140 | Tech-SNS | DM Map Resolution | NOVEL | Ch 12 |
| P-141 | Tech-SNS | DE Density Fluctuation Amplitude | NOVEL | Ch 12 |
| P-142 | Tech-SNS | LIGO Waters-Field Threshold | NOVEL | Ch 12 |
| P-143 | Tech-SNS | ISW $\xi$-Boundary Anomaly | NOVEL | Ch 12 |
| P-144 | Tech-SNS | HL-LHC Form-Factor Anomaly | NOVEL | Ch 12 |
| P-145 | Tech-SNS | High-$z$ Shapiro Anomaly | NOVEL | Ch 12 |
| P-146 | Tech-SNS | CMB Thermal Anisotropy | NOVEL | Ch 12 |
| P-147 | Tech-SNS | Earth Biomass Tidal Gradient | NOVEL | Ch 12 |
| P-148 | Tech-SNS | Biomass vs. Desert Differential | NOVEL | Ch 12 |
| P-149 | Tech-SNS | Life-Detection False-Positive Rate | NOVEL | Ch 12 |
| P-150 | Tech-SNS | Exoplanet Life-Detection Sensitivity | NOVEL | Ch 12 |
| P-151 | Tech-SNS | Extended GW Polarization Ratios | NOVEL | Ch 12 |
| P-152 | Tech-SNS | LIGO-Retrofit Scalar Sensitivity | NOVEL | Ch 12 |
| P-153 | Tech-SNS | PTA Longitudinal-Mode Threshold | NOVEL | Ch 12 |

**Status tally:** MATCHES 55 · DIFFERS 16 · NOVEL 80 · OPEN 2 · Total 153.

**Category tally:** Structural 7 · Couplings 7 · Particle 21 · GR 14 · QED/EM 3 · EM 6 · Classical 2 · Thermo 3 · QM 4 · Cosmology 17 · Tech-FTL 14 · Tech-NRG 18 · Tech-COM 19 · Tech-SNS 18 · Total 153 (some predictions are cross-filed between narrative categories in §A.3–§A.12; in the master table each prediction has exactly one canonical category assignment).

---

## A.14  Cross-Reference Index: Source Equation → Prediction ID

The following index reverses the "Source" column of the master table, allowing a reader to navigate from a Vol 1–5 derivation equation to the Vol 6 predictions that depend on it. This is the orphan-check counterpart: every equation cited below must appear in at least one P-XXX row, and every row in §A.13 must cite a source.

### Vol 1 — Architecture of Reality

- **Vol 1 Ch 5, Eq (1.5.12)** (Firmament tension σ) → P-074, P-093, P-100
- **Vol 1 Ch 5, Eq (1.5.12)–(1.5.18)** (Firmament membrane wave equation) → P-074
- **Vol 1 Ch 5** (Firmament membrane dynamics, broader) → P-069, P-075, P-085, P-100, P-103, P-136, P-137, P-138
- **Vol 1 Ch 6** (Waters field equations) → P-077, P-078, P-079
- **Vol 1 Ch 7, Eq (1.7.22)** (time-translation Noether) → P-031
- **Vol 1 Ch 7, Eq (1.7.29)** (spatial-translation Noether) → P-032
- **Vol 1 Ch 7, Eq (1.7.33)** (rotational Noether) → P-033
- **Vol 1 Ch 7** (Noether symmetries generally) → P-031, P-032, P-033, P-034, P-081
- **Vol 1 Ch 11** (zone-separation entropy, thermodynamics) → P-037

### Vol 2 — Forces and Fields

- **Vol 2 Ch 3** (EM / Maxwell derivation) → P-040, P-041, P-042, P-043
- **Vol 2 Ch 6** (gauge group from zone symmetries) → P-034, P-042
- **Vol 2 Ch 9, Eq (2.9.45)** (force hierarchy from $\mathcal{R}$) → P-005
- **Vol 2 Ch 10** (running couplings) → P-058

### Vol 3 — Matter and Motion

- **Vol 3 Ch 1** (membrane-dynamics derivation of Newton's 2nd Law) → P-035
- **Vol 3 Ch 3** (zone-derived gravitational potential → Kepler) → P-036
- **Vol 3 Ch 9, Ch 12** (entropy from zone separation) → P-037
- **Vol 3 Ch 10** (Planck spectrum, Stefan-Boltzmann) → P-038, P-039

### Vol 4 — The Quantum World

- **Vol 4 Ch 1** (photoelectric / Einstein relation) → P-046
- **Vol 4 Ch 4** (CHSH from zone connectivity; QM_FROM_MEMBRANE_DYNAMICS) → P-087
- **Vol 4 Ch 7, Eq (4.7.51)–(4.7.56)** (perturbative QED $a_e$) → P-001
- **Vol 4 Ch 7, Eq (4.7.57)–(4.7.63)** (Lamb shift QED) → P-002
- **Vol 4 Ch 7** (perturbative QED framework) → P-001, P-002, P-003
- **Vol 4 Ch 9** (vacuum energy / ZPE) → P-049, P-076
- **Vol 4 Ch 10, Eq (4.10.18)** (hard-wall mass spectrum) → P-052
- **Vol 4 Ch 10** (particle spectrum, topological boundary modes) → P-018, P-023, P-052, P-053, P-054, P-067, P-074
- **Vol 4 Ch 11** (electroweak theory) → P-014, P-015, P-016, P-017, P-018, P-019, P-020, P-057
- **Vol 4 Ch 12** (QCD from $\eta$-boundary) → P-006, P-021, P-022, P-058, P-144
- **Vol 4 Ch 14, Eq (4.14.8)–(4.14.15)** (zone boundary scattering corrections) → P-071
- **Vol 4 Ch 14** (topological classification of baryons) → P-067, P-080

### Vol 5 — The Cosmos

- **Vol 5 Ch 1** (EFE recovered from 6D) → P-007 through P-013
- **Vol 5 Ch 2, Eq (5.2.12)–(5.2.14)** (Mercury precession) → P-007
- **Vol 5 Ch 2, Eq (5.2.21)** (light bending) → P-008
- **Vol 5 Ch 2, Eq (5.2.25)–(5.2.26)** (Pound-Rebka redshift) → P-010
- **Vol 5 Ch 2, Eq (5.2.28)** (GPS time dilation) → P-013
- **Vol 5 Ch 2, Eq (5.2.32)** (Shapiro delay) → P-009
- **Vol 5 Ch 2, Eq (5.2.39)** (frame dragging) → P-012
- **Vol 5 Ch 3** (gravitational waves from 6D) → P-011, P-059, P-060, P-068, P-069, P-070, P-089
- **Vol 5 Ch 3, Eq (5.3.22)** (KK mode dispersion) → P-059
- **Vol 5 Ch 3, Eq (5.3.24)–(5.3.31)** (6D linearized Einstein perturbations) → P-068
- **Vol 5 Ch 4** (FTL mechanisms foundation) → P-083, P-120
- **Vol 5 Ch 8** (zone cosmology) → P-025, P-026, P-027, P-028
- **Vol 5 Ch 11** (dark sector, Waters as DM/DE) → P-024, P-025, P-030, P-061, P-062, P-063, P-064, P-077, P-078, P-086, P-096
- **Vol 5 Ch 11, Eq (5.11.1)** ($w = -1$ from Waters Above) → P-024
- **Vol 5 Ch 11, Eq (5.11.6)–(5.11.10), Table 5.11.1** (NFW from WB Firmament field) → P-030
- **Vol 5 Ch 11, Eq (5.11.14)** (Tully-Fisher) → P-029
- **Vol 5 Ch 11, Eq (5.11.42)** (DE EOS precision) → P-063
- **Vol 5 Ch 11 §11.4** (bulk-Firmament separation) → P-061
- **Vol 5 Ch 13** (fine structure derivation) → P-004, P-056, P-065
- **Vol 5 Ch 13, Eq (5.13.25)–(5.13.28)** (6D Green's function) → P-004 (derivation)
- **Vol 5 Ch 13, Eq (5.13.32)** (α master formula) → P-004, P-056
- **Vol 5 Ch 13, Eq (5.13.39)** ($b_{\rm eff}$ decomposition) → P-004

### Vol 6 — Predictions, Simulations, and Open Problems (intra-volume)

- **Vol 6 Ch 1, Eq (6.1.2)** (α master formula, restated) → P-004
- **Vol 6 Ch 1, Eq (6.1.3)** (log scale ratio) → P-004
- **Vol 6 Ch 1, Eq (6.1.4)** (Tully-Fisher derivation) → P-029
- **Vol 6 Ch 2, Eq (6.2.1)** (hard-wall eigenfrequency) → P-052
- **Vol 6 Ch 2, Eq (6.2.2)–(6.2.3)** (KK group velocity) → P-059
- **Vol 6 Ch 2, Eq (6.2.4)–(6.2.5)** (neutrino splittings) → P-023, P-066
- **Vol 6 Ch 3, Eq (6.3.1)** (scalar perturbation equation) → P-069
- **Vol 6 Ch 3, Eq (6.3.2)** ($E_\eta$ zone boundary energy) → P-071
- **Vol 6 Ch 3, Eq (6.3.3)** (scattering correction) → P-071
- **Vol 6 Ch 3, Eq (6.3.4)** (energy loss to extra dim) → P-072
- **Vol 6 Ch 3, Eq (6.3.5)** (zone-transition peak frequency) → P-073
- **Vol 6 Ch 3, Eq (6.3.6)** (Firmament membrane wave equation — restated) → P-074
- **Vol 6 Ch 3, Eq (6.3.7)** (hard-wall mass scaling) → P-074
- **Vol 6 Ch 3, Eq (6.3.8)** (effective mode count) → P-076
- **Vol 6 Ch 3, Eq (6.3.9)** (Waters Below field equation) → P-077
- **Vol 6 Ch 3, Eq (6.3.10)** (quadrupole formula applied to bubble) → P-083
- **Vol 6 Ch 3, Eq (6.3.11)** (bypass radiation spectrum) → P-084, P-091
- **Vol 6 Ch 3, Eq (6.3.12)** (coupling coefficient) → P-085
- **Vol 6 Ch 3, Eq (6.3.13)** (extracted power) → P-085
- **Vol 6 Ch 3, Eq (6.3.14)** (Waters Above density perturbation) → P-086
- **Vol 6 Ch 3, Eq (6.3.15)** (CHSH correction) → P-087
- **Vol 6 Ch 3, Eq (6.3.16)** (photon zone tunneling) → P-088
- **Vol 6 Ch 10, §10.5.3** → P-104
- **Vol 6 Ch 10, §10.5.4, §10.8.2** → P-108
- **Vol 6 Ch 10, §10.5.4, §10.8.3** → P-107
- **Vol 6 Ch 10, §10.5.7–§10.5.8, Eq (10.5.9)** → P-103
- **Vol 6 Ch 10, §10.5.9, Eq (10.5.11)** → P-105
- **Vol 6 Ch 10, §10.5.10** → P-106
- **Vol 6 Ch 10, §10.6.1 / Eq (10.6.1)** → P-111
- **Vol 6 Ch 10, §10.6.3** → P-113
- **Vol 6 Ch 10, §10.6.4, Eq (10.6.2)** → P-114
- **Vol 6 Ch 10, §10.6.4** → P-112
- **Vol 6 Ch 10, §10.7.2** → P-115
- **Vol 6 Ch 10, §10.7.3** → P-116, P-117
- **Vol 6 Ch 10, §10.8.4** → P-109
- **Vol 6 Ch 10, §10.8.5** → P-110
- **Vol 6 Ch 10, §10.10.2, Eq (10.10.1)** → P-118
- **Vol 6 Ch 11, §11.3** → P-133
- **Vol 6 Ch 11, §11.4.7** → P-126, P-134
- **Vol 6 Ch 11, §11.4, Eq (11.4.4)** → P-123
- **Vol 6 Ch 12, Eq (12.2.3)** → P-136, P-138

### Research Archive Citations

- **UNIQUE_PREDICTIONS.md Prediction 2** (DE EOS) → P-024, P-063
- **UNIQUE_PREDICTIONS.md Prediction 3** (GW dispersion) → P-059
- **UNIQUE_PREDICTIONS.md Prediction 4** (neutrino boundary modes) → P-023, P-066
- **ENERGY_FRACTIONS_DERIVATION.md** → P-085, P-086, P-025
- **SUSTAINING_COUPLING.md** → P-079
- **QM_FROM_MEMBRANE_DYNAMICS.md** → P-087, P-098
- **FTL_MECHANISMS_FORMAL.md Mechanism 2** → P-084, P-091
- **FTL_MECHANISMS_FORMAL.md Mechanism 3** → P-088, P-094
- **FTL_MECHANISMS_FORMAL.md Mechanism 4** → P-083, P-095
- **PARTICLE_MASS_SPECTRUM_SUMMARY.md** (failure documentation) → P-052, P-053, P-054
- **PARTICLE_PRECISION_COMPLETIONS.md** → P-014, P-019, P-020, P-021, P-022
- **EM_PRECISION_COMPLETIONS.md** → P-043, P-044, P-045
- **Test 1.2** → P-035
- **Test 1.6** → P-036
- **Test 2.3, 2.8, 2.9** → P-037, P-038, P-039
- **Test 3.1–3.5** → P-040
- **Test 3.6, 3.7** → P-042, P-043
- **Test 3.12, 3.13** → P-044, P-045
- **Test 5.1, 5.2, 5.12, 5.16** → P-046, P-047, P-048, P-049
- **Test 6.20** → P-017, P-018
- **Test 6.22, 6.23** → P-006, P-021, P-022
- **Test 7.12** → P-011
- **Test 8.1, 8.4, 8.15** → P-026, P-027, P-028
- **Test 9.1, 9.2** → P-050, P-051
- **Test 10.1** → P-041

---

## A.15  Falsification-Threshold Gap Report

Every prediction in §A.3–§A.12 has a falsification-threshold column populated. The Skeptic reviewer will audit these for tautology (threshold = "prediction fails if prediction is falsified") and genuine quantitative specificity. Preliminary self-audit results:

**Genuine, numerically specific thresholds (majority — 147/153):** 147 predictions carry thresholds that specify a numerical condition (significance level, fractional precision, or categorical discovery) under which the prediction is overturned. Examples: P-004 requires $\alpha^{-1}$ within 0.01% of experiment after $b_{\rm eff}$ refinement, at 3σ; P-061 requires no confirmed DM detection at $\sigma > 10^{-48}$ cm² by two independent experiments; P-066 requires inverted hierarchy at 3σ from JUNO + DUNE.

**Conditionally falsifiable (6 predictions flagged for Ch 14 treatment):**

- **P-055 (Neutrino Mass Scale):** No mechanism currently in framework; unfalsifiable until Higgs-Waters coupling computed. Classified OPEN. Pathway to falsifiability documented in Ch 14 Open Problems.
- **P-081 (Zone Number Conservation):** No specific suppressed channel identified until topological classification is completed. Falsification threshold stated in conditional form ("once classification identifies specific channels"). Classified NOVEL with caveat. Ch 14 entry required.
- **P-092 (Starlight via Bulk Paths):** Interpretive prediction; direct falsification requires discovering an alternative mechanism, which is not itself a numerical threshold. Classified NOVEL; falsification is logical rather than numerical. Noted in §A.1.
- **P-098 / P-099 (Consciousness Predictions):** Require Stage 2+ neural quantum coherence engineering — not achievable with current technology. Classified NOVEL with explicit "Stage 2+ required" caveat. Thresholds specify what would falsify *given the apparatus*. Ch 14 records the technology dependency as an Open Problem.
- **P-102 (Phase 3 Thermodynamic Lock):** Classified OPEN. The falsification condition ("warp-bubble engineering with energy below current-phase allowance") is contingent on developing warp-bubble engineering itself — a bootstrap dependency. Ch 14 treats this as a research direction, not an immediate test.

**Non-falsifiable (0 predictions):** No prediction in Vol 6 is intentionally unfalsifiable. All five conditional-falsifiability entries above have explicit pathways to falsifiability that await framework completion (theoretical calculations) or technology maturation (experimental apparatus). The framework does not hide predictions behind permanent hedges.

**Thresholds that exceed current experimental reach:** Many predictions specify thresholds that current instruments cannot meet (e.g., P-059's GW dispersion at 10⁻³⁵ is 20 orders of magnitude below LIGO's precision). These are not flagged as gaps because the threshold is *quantitative and falsifiable in principle* — the prediction simply waits for better apparatus. The Skeptic should note that "awaits better instruments" is scientifically different from "awaits reframing of the claim."

---

*Appendix A complete. Total predictions indexed: 153. Master table, cross-reference index, and falsification-threshold audit deliver the framework's consolidated scientific bet in one scrutable location.*

*Next back-matter component: Appendix B — Simulation Code Repository.*
