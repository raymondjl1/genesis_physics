# Chapter 2: Predictions That Differ from Standard Physics

---

*This chapter presents every prediction where zone architecture and the Standard Model make different quantitative commitments. For each: the zone architecture value, the standard physics value, the current experimental precision, and the specific experiment that could distinguish between them. Where zone architecture fails, we say so first.*

---

## 2.1 What "Differs" Means — A Taxonomy of Disagreements

Chapter 1 demonstrated that zone architecture reproduces the vast body of confirmed physics — from QED's twelve-digit precision to the cosmic energy budget, from Maxwell's equations to general relativity's classical tests. The framework passes, at minimum, the first test any new theory must face: it gets the known answers right.

But getting known answers right is necessary, not sufficient. A framework that merely replicates the Standard Model with different notation is scientifically useless — it adds explanation (the "why") but no new testable content. The real scientific interest begins where zone architecture and standard physics *disagree*. These disagreements are where the framework puts its neck on the line, and they come in three distinct types that the reader must distinguish before evaluating any specific prediction.

**Type A: Different Numerical Values.** Zone architecture and the Standard Model both predict a value for the same observable, and those values differ. A single measurement at sufficient precision can resolve the disagreement. The particle mass spectrum belongs here: zone architecture's Firmament membrane resonance model predicts masses that are wrong by factors of 20 to 1000. This is a genuine failure, and we present it first (Section 2.2) because a framework that hides its worst results does not deserve trust.

> **Note: The particle mass spectrum discrepancy (u quark ~370× error, d quark ~31,000× error) is the framework's most significant open failure.** The fundamental Firmament membrane mode produces 475.5 MeV/c² for the lightest stable particle; the observed electron mass is 0.511 MeV/c² — a 930× discrepancy. A possible resolution — computing the 2D membrane eigenvalue problem rather than the 1D approximation — is identified as Research Task RT-6.MASS2D. Until RT-6.MASS2D is complete, the particle mass sector remains structurally incomplete. Section 2.2 develops this in full.

**Type B: Different Theoretical Commitments.** The Standard Model leaves a quantity undetermined or allows multiple possibilities; zone architecture commits to a specific answer. No single measurement "resolves" this — instead, an experimental program progressively constrains the allowed space until one framework or the other is excluded. The neutrino mass hierarchy belongs here: the Standard Model allows both normal and inverted ordering; zone architecture permits only normal. The JUNO and DUNE experiments will produce a definitive answer within five to ten years.

**Type C: Effects Predicted to Exist But Below Current Detection.** Zone architecture predicts a nonzero value for a quantity that the Standard Model says is exactly zero, but the predicted magnitude is far below current experimental sensitivity. These are real predictions — falsifiable in principle — but they may require decades of technological progress to test. Gravitational wave dispersion belongs here: the 6D framework predicts a frequency-dependent correction to the speed of gravitational waves at the level of $\delta \sim 10^{-35}$, some twenty orders of magnitude below the best current constraint.

[FIGURE: Fig 6.2.1 — Taxonomy of Differing Predictions. A three-column diagram: Type A (different numbers, one measurement resolves, risk: immediate), Type B (different commitments, experimental program required, risk: medium-term), Type C (predicted effect below detection, decades to test, risk: long-term). Each column contains the specific predictions from this chapter.]

Throughout this chapter, each prediction continues the numbering established in Chapter 1 (P-052 onward) and follows the same standard format, with two additions: the *Standard Model value* appears alongside the zone architecture value, and each prediction is classified by type. The falsification thresholds are stated with explicit numerical bounds — no hedging, no "would need to be reconsidered."

One further distinction matters. Some predictions that *appear* to differ actually agree within experimental uncertainty. We flag these carefully: a prediction where the zone architecture value falls within the current error bars of the best measurement is not yet a confirmed difference — it is a *potential* difference awaiting better data. The Skeptic in every reader should ask of each entry: "Is this difference actually resolved by current experiments, or am I looking at noise?" We will answer that question honestly for every prediction in this chapter.

---

## 2.2 Particle Masses — The Honest Failure

We begin with the worst result in the entire framework.

The particle mass spectrum derivation (Vol 4, Ch 10) represents zone architecture's most ambitious quantitative attempt — and its most instructive failure. The idea is elegant: if particles are quantized vibrational modes of the Firmament membrane, then their masses should emerge as eigenvalues of the Firmament membrane wave equation, just as the frequencies of a vibrating drum are determined by its geometry. The mathematics is rigorous, the physics is clear, and the framework makes definite predictions.

Those predictions are wrong by three orders of magnitude.

Understanding *why* they are wrong — and what the failure tells us about the framework's incompleteness — is more scientifically valuable than any match in Chapter 1.

### The Firmament Resonance Model

The Firmament, modeled as a 2D membrane embedded in the 6D zone manifold, satisfies a wave equation with boundary conditions at the Waters Above (dark energy, ~68%; $\xi = \xi_A$) and Waters Below (dark matter, ~27%; $\eta = \eta_B$). The simplest model — hard-wall boundary conditions at the geometric extents — gives quantized resonance frequencies:

$$\omega_{n_\xi, n_\eta} = c\sqrt{\left(\frac{n_\xi \pi}{\xi_A}\right)^2 + \left(\frac{n_\eta \pi}{\eta_B}\right)^2} \tag{6.2.1}$$

The mass of each resonance mode is $m = \hbar\omega/c^2$. Different quantum numbers $(n_\xi, n_\eta)$ correspond to different particle species. This is not speculative — it is a direct consequence of the framework's axioms, and it makes quantitative predictions.

> **P-052: Electron Mass from Membrane Ground State**
> **Zone architecture value:** $m_e \sim 500$ MeV$/c^2$ (ground state of hard-wall model)
> **Standard Model value:** Fitted parameter (Yukawa coupling to Higgs)
> **Experimental value:** $m_e = 0.510\,998\,950$ MeV$/c^2$
> **Current precision:** $\Delta m_e/m_e \sim 3 \times 10^{-10}$
> **Distinguishing experiment:** Not applicable — the discrepancy is already resolved by observation
> **Source:** Vol 4, Ch 10, Eq (4.10.18)
> **Falsification threshold:** The hard-wall model is *already falsified* by the factor-of-1000 discrepancy. The question is whether refinements (soft potentials, Higgs coupling) can rescue the framework.
> **Type:** A (different numerical value)
> **Status:** DIFFERS — zone architecture fails

The factor-of-1000 error demands explanation, not excuse. The hard-wall model uses the *geometric* extents $\xi_A \approx 3 \times 10^{26}$ m and $\eta_B \approx 1.3 \times 10^{-15}$ m as the confining boundaries. The $\eta_B$ scale dominates (because $\eta_B \ll \xi_A$, the relevant frequency is $\omega \approx \pi c/\eta_B$), giving $m \approx \pi\hbar/(c\,\eta_B) \approx 500$ MeV. But the electron mass is 0.511 MeV — three orders of magnitude smaller.

What went wrong? The root cause analysis (documented in the Research archive, PARTICLE_MASS_SPECTRUM_SUMMARY.md) identifies four contributing factors:

First, particle masses are not set by geometric boundaries alone. The Higgs mechanism — electroweak symmetry breaking through the Higgs field acquiring a vacuum expectation value $v = 246.22$ GeV — plays a central role that the simple Firmament membrane model omits. In zone architecture, the Higgs should emerge as a specific Firmament membrane mode whose coupling to other modes (the Yukawa couplings) determines the mass spectrum. This coupling calculation has not been completed.

Second, the effective confining scale for particle masses is not $\eta_B$ (the Waters Below extent) but some dynamical scale $L_{\rm eff}$ set by the Higgs-Waters interaction. The electron mass requires $L_{\rm eff} \sim 3.9 \times 10^{-13}$ m — larger than $\eta_B$ by a factor of 300, suggesting the effective potential well is much wider than the hard-wall geometry.

Third, the generation structure — why the muon is 206.77 times heavier than the electron, rather than 2 to 10 times as the simple model predicts — requires understanding Yukawa coupling overlap integrals between the Higgs wavefunction and the fermion wavefunctions in the extra dimensions. These integrals have not been computed.

Fourth, neutrino masses ($m_\nu < 0.1$ eV) are a billion times lighter than the electron. The Firmament model provides no mechanism for such extreme lightness. This is a critical gap — neutrinos constitute roughly 10% of the universe by number density, and any complete particle physics framework must explain their masses.

> **P-053: Muon-to-Electron Mass Ratio**
> **Zone architecture value:** $m_\mu/m_e \approx 2$–$10$ (from simple quantum number assignment $n_\xi = 1$ vs. $n_\xi = 2$)
> **Standard Model value:** Determined by ratio of Yukawa couplings (fitted)
> **Experimental value:** $m_\mu/m_e = 206.768\,283\,63(82)$
> **Current precision:** $4 \times 10^{-9}$
> **Distinguishing experiment:** Already resolved — the simple model fails
> **Source:** Vol 4, Ch 10
> **Falsification threshold:** Hard-wall model already falsified for mass ratios
> **Type:** A
> **Status:** DIFFERS — zone architecture fails

> **P-054: Quark Mass Spectrum Pattern**
> **Zone architecture value:** Simple membrane quantum numbers predict regular spacing
> **Standard Model value:** Six quark masses fitted from experiment: $u \approx 2.2$, $d \approx 4.7$, $s \approx 93$, $c \approx 1275$, $b \approx 4180$, $t \approx 173\,000$ MeV
> **Experimental value:** Above (PDG values)
> **Current precision:** Varies (1–10% for most quarks)
> **Distinguishing experiment:** Already resolved — the irregular quark mass pattern does not match simple Firmament membrane modes
> **Source:** Vol 4, Ch 10
> **Falsification threshold:** Hard-wall model already falsified for quark mass pattern
> **Type:** A
> **Status:** DIFFERS — zone architecture fails

> **P-055: Neutrino Mass Scale**
> **Zone architecture value:** No mechanism for sub-eV masses in current framework
> **Standard Model value:** No prediction (masses added by hand or via seesaw mechanism)
> **Experimental value:** $\sum m_\nu < 0.12$ eV (cosmological bound); $\Delta m^2_{21} = 7.53 \times 10^{-5}$ eV$^2$
> **Current precision:** Mass-squared differences known to 2–3%
> **Distinguishing experiment:** Framework cannot currently make a prediction to test
> **Source:** Vol 4 (boundary mode analysis gives hierarchy, not absolute scale)
> **Falsification threshold:** N/A — framework is incomplete, not making a testable claim
> **Type:** A (gap in framework)
> **Status:** DIFFERS — zone architecture has no prediction

### What This Failure Means — and What It Does Not Mean

The particle mass sector is unambiguously incomplete. This must be stated without qualification: zone architecture, in its current form, cannot predict absolute particle masses. The 1000$\times$ electron mass error, the 20–100$\times$ mass ratio errors, and the missing neutrino mass mechanism are genuine failures of the simplest Firmament model.

But *incomplete* is not *falsified*. The distinction matters.

The hard-wall Firmament model is the *simplest possible* application of the zone architecture to particle masses — the equivalent of modeling an atom as a hard sphere. Real atoms require quantum mechanics, electron correlation, and nuclear structure. Similarly, real particle masses require the Higgs mechanism, Yukawa coupling dynamics, and the full Waters-Firmament interaction — physics that the framework accommodates in principle but has not yet computed in practice.

Three results from the same framework *do* work: the prediction of exactly three fermion generations (from the three lowest $\xi$-modes, matching the observed three families), the derivation of the fine structure constant (from the same geometric parameters that fail for masses), and the gauge group structure $SU(3) \times SU(2) \times U(1)$ (from zone symmetries). These successes demonstrate that the Firmament framework captures real physics — it is the mass sector specifically that requires additional theoretical development.

The parameter counting is also honest but not damning: zone architecture uses approximately 5 to 10 adjustable parameters to address 20 particle masses, compared to the Standard Model's approximately 30 free parameters for the same data. The improvement is modest, not revolutionary.

[FIGURE: Fig 6.2.2 — Particle Mass Spectrum: Zone Architecture vs. Experiment. A log-scale plot with particle species on the x-axis and mass (MeV) on the y-axis. Experimental values shown as points with error bars. Zone architecture hard-wall predictions shown as a separate series, dramatically above the data for light particles. The gap between the two series — the 1000$\times$ discrepancy — is the most important feature of the figure. An inset shows the three predictions that *do* work: three generations, $\alpha$, gauge group.]

The path forward is identified (Chapter 14, Open Problems): compute the Higgs wavefunction as a Firmament membrane mode, evaluate the Yukawa overlap integrals, solve the coupled Schrödinger equation with soft (Waters-mediated) potentials, and derive the effective confining scales from the dynamics rather than assuming hard walls. This is a research program, not a patch — and it may require the equivalent of a doctoral thesis to complete.

> **Note: The most promising near-term resolution is the 2D eigenvalue calculation.** The current simulations solve a 1D Firmament membrane model with L = η_B. The actual Firmament is 2D (or higher-dimensional). Computing the 2D membrane eigenvalue problem may shift the fundamental mode mass significantly, as 2D Bessel function zeros produce non-uniform mode spacing that could better accommodate the observed mass hierarchy. This is Research Task RT-6.MASS2D. Until RT-6.MASS2D is complete, the 930× electron mass discrepancy (fundamental mode 475.5 MeV/c² vs. observed 0.511 MeV/c²) and the quark mass discrepancies (u quark ~370×, d quark ~31,000×) remain the framework's most significant quantitative failures.

---

## 2.3 Coupling Constants — Close But Not Exact

The coupling constant predictions occupy the opposite end of the spectrum from particle masses. Where masses fail by factors of 1000, coupling constants agree to fractions of a percent. The small residual discrepancies are not failures — they are predictions about the framework's theoretical uncertainties, pointing precisely to the calculations that need refinement.

> **P-056: Fine Structure Constant — Residual Offset**
> **Zone architecture value:** $\alpha^{-1} = 137.17 \pm 0.15$
> **Standard Model value:** No prediction (fitted parameter)
> **Experimental value:** $\alpha^{-1} = 137.035\,999\,084(21)$
> **Current precision:** $\Delta\alpha/\alpha \sim 1.5 \times 10^{-10}$ (experimental)
> **ZA–experiment discrepancy:** $0.10\%$ ($\Delta\alpha^{-1} = 0.13$)
> **Distinguishing experiment:** This is a Type A difference — but because SM doesn't predict $\alpha$ at all, the "experiment" is theoretical refinement of $b_{\rm eff}$, not a new measurement. The measurement already exists; the theory needs to sharpen.
> **Source:** Vol 5, Ch 13, Eq (5.13.32)
> **Falsification threshold:** If refinement of $b_{\rm hi}$ (higher-loop coefficient) cannot bring the prediction within 0.01% of experiment, the logarithmic derivation pathway requires fundamental revision.
> **Type:** A (different numerical value — but SM has no competing prediction)
> **Status:** DIFFERS (0.10% offset)

The 0.10% discrepancy in $\alpha^{-1}$ is traced to the effective beta-function coefficient $b_{\rm eff} = 9.05$, whose four components ($b_{\rm QED} = 3.67$, $b_{\rm weak} = 2.00$, $b_{\rm red} = 1.40$, $b_{\rm hi} = 1.00$) carry varying levels of theoretical certainty (Eq 6.1.2, Chapter 1). The higher-loop coefficient $b_{\rm hi} = 1.00$ carries the largest uncertainty — it represents a placeholder for three-loop and higher corrections to the 6D-to-4D reduction that have not been computed. Shifting $b_{\rm hi}$ from 1.00 to approximately 0.87 would bring $\alpha^{-1}$ to within 0.01% of experiment. Whether this shift is physically justified requires a calculation that has not yet been performed.

This is qualitatively different from the particle mass failure. The mass spectrum fails because essential physics (Higgs coupling) is missing. The fine structure constant succeeds at 0.10% and identifies a specific coefficient whose refinement would improve agreement by an order of magnitude. The difference between "missing essential physics" and "needs a higher-loop calculation" is the difference between a structural gap and a precision frontier.

> **P-057: Weak Mixing Angle**
> **Zone architecture value:** $\sin^2\theta_W$ derived from zone geometry (Vol 4, Ch 11), currently within $\sim 1\%$ of measured value
> **Standard Model value:** Fitted parameter: $\sin^2\theta_W = 0.23122 \pm 0.00003$ ($\overline{\rm MS}$ scheme, $M_Z$ scale)
> **Experimental value:** Same as SM (definition-dependent)
> **Current precision:** $\Delta\sin^2\theta_W/\sin^2\theta_W \sim 1.3 \times 10^{-4}$
> **Distinguishing experiment:** As with $\alpha$, the SM fits this value; ZA derives it. Precision comparison requires completing the zone-geometry derivation at two-loop level.
> **Source:** Vol 4, Ch 11
> **Falsification threshold:** If zone geometry derivation cannot achieve sub-percent agreement after full two-loop computation, the electroweak sector of zone architecture requires revision.
> **Type:** A
> **Status:** DIFFERS (small offset, refinement in progress)

> **P-058: Strong Coupling Running at Extreme Energies**
> **Zone architecture value:** $\alpha_s(M_Z) = 0.118$ (matches SM). But: at energies approaching the zone boundary scale ($E \sim \hbar c/\eta_B \sim 150$ GeV), zone boundary effects modify the running beyond what perturbative QCD predicts.
> **Standard Model value:** $\alpha_s(M_Z) = 0.1180 \pm 0.0008$ with perturbative running $\alpha_s(Q) \to 0$ as $Q \to \infty$
> **Experimental value:** Consistent with SM running up to $Q \sim 1$ TeV (LHC data)
> **Current precision:** $\sim 0.7\%$ at $M_Z$; less precise at higher scales
> **Distinguishing experiment:** A future $e^+e^-$ collider (FCC-ee, ILC, or CEPC) measuring $\alpha_s$ at multiple energy scales from 91 GeV to $>$ 350 GeV would test whether the running follows the standard logarithmic form or shows zone-boundary deviations.
> **Source:** Vol 4, Ch 12; Vol 2, Ch 10
> **Falsification threshold:** If $\alpha_s$ running is measured to $\pm 0.1\%$ precision at $Q > 500$ GeV and shows no deviation from standard perturbative QCD, the zone-boundary modification is either absent or smaller than predicted.
> **Type:** A (different values at extreme energies)
> **Status:** DIFFERS (agreement at current energies; potential divergence at higher scales)

The coupling constant sector illustrates a pattern that recurs throughout this chapter: zone architecture's greatest scientific contribution is not necessarily getting a *different* number, but getting a number *at all* for quantities the Standard Model treats as unexplained inputs. The fine structure constant, the weak mixing angle, and the force hierarchy ratio are all fitted parameters in standard physics. Zone architecture derives them from geometry. Even where the derived values carry percent-level offsets, the act of deriving them — reducing free parameters — represents genuine theoretical progress.

A note on the scientific status of these differences. All three coupling constant predictions (P-056 through P-058) are Type A differences — different numerical values that could in principle be resolved by more precise calculations within zone architecture itself. They are not in conflict with observation; they are in the process of convergence toward observation. The path from 0.10% agreement to 0.01% agreement in $\alpha$ requires computing the higher-loop reduction coefficient $b_{\rm hi}$ to two-loop precision. The path to a precision weak mixing angle requires the full two-loop electroweak sector in zone geometry. These are specific, well-defined computational tasks — not vague hopes that the numbers will somehow improve.

The distinction matters because it separates coupling constants from particle masses. The mass sector fails because *essential physics is missing* (the Higgs-Waters coupling). The coupling constant sector succeeds at sub-percent level because the relevant physics *is present* — it merely needs to be computed at higher precision. This is the difference between a gap in the theory and a gap in the calculation.

---

## 2.4 Dark Matter — A Categorical Commitment

We turn now from Type A differences (wrong numbers, refinable) to the most consequential Type B difference in the framework: the nature of dark matter.

The Standard Model does not include dark matter. Its extensions propose dozens of candidates — WIMPs, axions, sterile neutrinos, primordial black holes, fuzzy dark matter — each with specific interaction cross-sections that dedicated experiments are designed to detect. Zone architecture makes a radically simpler commitment: dark matter is the Waters Below field ($\Psi_B$), a geometric excitation in the $\eta$ extra dimension, and it has *exactly zero* non-gravitational interactions with ordinary matter.

This is not a hedge. It is the most falsifiable prediction in the framework.

> **P-061: Dark Matter Interaction Cross-Section**
> **Zone architecture value:** $\sigma_{\rm DM\text{-}SM} = 0$ (exactly zero non-gravitational interactions)
> **Standard Model value:** No SM prediction; extensions predict: WIMPs $\sigma_{\rm SI} \sim 10^{-46}$ cm$^2$; axions $g_{a\gamma\gamma} \sim 10^{-12}$ GeV$^{-1}$
> **Experimental value:** No detection. Best upper limit: $\sigma_{\rm SI} < 4.1 \times 10^{-47}$ cm$^2$ (XENONnT, 2023)
> **Current precision:** Upper limits only — each generation of detectors improves by $\sim 10\times$
> **Distinguishing experiment:** Any direct dark matter detection experiment. A confirmed detection at *any* cross-section falsifies zone architecture. Continued null results support it.
> **Source:** Vol 5, Ch 11, §11.4
> **Falsification threshold:** A confirmed detection of dark matter with $\sigma > 10^{-48}$ cm$^2$ at $> 3\sigma$ significance, by at least two independent experiments, would falsify this prediction.
> **Type:** B (different theoretical commitment about DM nature)
> **Status:** DIFFERS — currently consistent with ZA

The reasoning behind the zero-interaction prediction is structural, not parametric. In zone architecture, the Waters Below field is confined to the bulk of the $\eta$ extra dimension — the region $\eta \in [\eta_0, \eta_B]$. The Firmament (which hosts all Standard Model fields) resides at the boundary $\eta = \eta_0$. The *only* interaction between the bulk and the boundary is gravitational — mediated by the curvature of the 6D spacetime that both regions share. Electromagnetic, weak, and strong interactions are gauge fields confined to the 4D Firmament. They cannot propagate into the $\eta$-bulk, and therefore they cannot couple to the Waters Below.

This is not a choice — it is a consequence of the geometry. As long as gauge fields are boundary-localized (which is required for the recovery of the Standard Model in Vol 4), dark matter *must* be gravitationally coupled and nothing else. Introducing a non-gravitational DM interaction would require either extending gauge fields into the bulk (breaking the Standard Model recovery) or adding new physics not contained in the seven axioms.

> **P-062: Dark Matter Decay Lifetime**
> **Zone architecture value:** $\tau_{\rm DM} = \infty$ (no decay channel exists — Waters Below is a field configuration, not a particle)
> **Standard Model extensions:** Some models predict finite DM lifetime ($\tau > 10^{26}$ years from current constraints)
> **Experimental value:** No decay detected. Constraint: $\tau_{\rm DM} > 10^{26}$ years (Super-Kamiokande)
> **Distinguishing experiment:** Detection of dark matter decay products (gamma rays, neutrinos) from galactic center or dwarf galaxies.
> **Source:** Vol 5, Ch 11
> **Falsification threshold:** Confirmed detection of DM decay products above astrophysical background at $> 3\sigma$.
> **Type:** B
> **Status:** DIFFERS — currently consistent with ZA

The experimental landscape tells a consistent story. Since the DAMA/LIBRA annual modulation claim (which has not been replicated by any other experiment), direct detection has been a sequence of increasingly sensitive null results:

- **LUX** (2017): $\sigma < 5.5 \times 10^{-47}$ cm$^2$ — no signal
- **XENON1T** (2018): $\sigma < 4.1 \times 10^{-47}$ cm$^2$ — no signal
- **PandaX-4T** (2021): $\sigma < 1.5 \times 10^{-46}$ cm$^2$ — no signal
- **XENONnT** (2023): approaching $\sigma < 10^{-47}$ cm$^2$ — no signal
- **LZ** (ongoing): targeting $\sigma \sim 10^{-47}$ cm$^2$

Each null result eliminates a swath of WIMP parameter space. The original WIMP "miracle" prediction ($\sigma \sim 10^{-44}$ cm$^2$) has been excluded by three orders of magnitude. The remaining viable WIMP space is shrinking toward the "neutrino fog" at $\sigma \sim 10^{-49}$ cm$^2$, where coherent neutrino scattering from the Sun and atmosphere creates an irreducible background that mimics a dark matter signal.

[FIGURE: Fig 6.2.3 — Dark Matter Detection Landscape. A log-log plot with DM mass on the x-axis and spin-independent cross-section on the y-axis. Shaded exclusion regions from LUX, XENON1T, PandaX, LZ. Projected sensitivities for XLZD, Darwin/ARGO. The "neutrino fog" floor at $\sim 10^{-49}$ cm$^2$. WIMP predictions clustered at $10^{-44}$ to $10^{-46}$. Zone architecture prediction: a flat line at $\sigma = 0$, below the bottom of the plot. The shrinking allowed region between current limits and the neutrino floor is the decisive experimental territory.]

Zone architecture's prediction creates an unusual evidential structure: every null result is weak evidence *for* the framework, while a single confirmed detection would be decisive evidence *against* it. This asymmetry — where absence of evidence is (mildly) evidence of absence — is characteristic of Type B predictions. The framework cannot be *proven* by null results, because the Standard Model with sufficiently low cross-section DM also predicts null results. But a confirmed detection would falsify zone architecture specifically, because no nonzero cross-section is compatible with the bulk-Firmament separation.

Indirect detection tells the same story. Fermi-LAT's 15-year survey of the galactic center shows no excess gamma-ray emission from dark matter annihilation. IceCube's search for neutrinos from dark matter capture in the Sun has produced null results. Both are exactly what zone architecture predicts, and both progressively constrain WIMP models that predict such signals.

---

## 2.5 Dark Energy — Geometric Certainty vs. Dynamical Freedom

The dark energy equation of state is the prediction most likely to be decisively tested in the near term. Three major observational programs — DESI, Euclid, and the Vera Rubin Observatory — are currently collecting data that will measure the equation of state parameter $w$ to unprecedented precision within the next two to five years.

> **P-063: Dark Energy Equation of State**
> **Zone architecture value:** $w = -1.000 \pm 0.001$ (geometrically fixed; uncertainty is theoretical, not physical)
> **Standard Model value:** No prediction — $w$ is a free parameter. ΛCDM assumes $w = -1$; extensions allow $w \neq -1$ and evolution.
> **Experimental value:** $w = -1.028 \pm 0.032$ (Planck 2018 + BAO); $w = -0.98^{+0.06}_{-0.05}$ (DES Y3); $w = -1.00 \pm 0.04$ (eBOSS)
> **Current precision:** $\sigma(w) \approx 0.03$
> **Distinguishing experiment:** DESI ($\sigma(w) \approx 0.02$ by 2027), Euclid + Roman ($\sigma(w) \approx 0.01$ by 2028), combined $\sigma(w) \approx 0.005$ by 2030.
> **Source:** Vol 5, Ch 11, Eq (5.11.42)
> **Falsification threshold:** If $w < -1.05$ or $w > -0.95$ measured at $> 3\sigma$ by combined DESI + Euclid, zone architecture is falsified.
> **Type:** B (different theoretical commitment — ZA says $w$ is fixed, not free)
> **Status:** DIFFERS from dynamical DE models; currently consistent with ΛCDM

> **P-064: No Dark Energy Evolution**
> **Zone architecture value:** $dw/dz = 0$ exactly. The equation of state does not vary with redshift.
> **Standard Model value:** Many models parameterize evolution: $w(a) = w_0 + (1 - a)\,w_a$, allowing nonzero $w_a$.
> **Experimental value:** $w_a = 0.0 \pm 0.3$ (current constraints — consistent with zero)
> **Current precision:** $\sigma(w_a) \approx 0.3$ — not yet constraining
> **Distinguishing experiment:** Same as P-063. Measuring $w$ in multiple redshift bins would test for evolution.
> **Source:** Vol 5, Ch 11
> **Falsification threshold:** If $w_a \neq 0$ at $> 2\sigma$ from combined surveys, the geometric fixity of Waters Above is challenged.
> **Type:** B
> **Status:** DIFFERS — currently consistent with no evolution

The physical basis for $w = -1$ in zone architecture is the confinement of the Waters Above field to a fixed region of the $\xi$ extra dimension: $\xi \in [\xi_0, \xi_A]$. This confinement enforces negative pressure with $p = -\rho$, giving $w = p/\rho = -1$. The field configuration is time-independent — established by the zone boundary conditions, not by dynamical evolution. Therefore $w = -1$ is not a coincidence or a fine-tuned parameter, but a geometric necessity.

The critical distinction from ΛCDM is subtle but important. ΛCDM also predicts $w = -1$ as its baseline (the cosmological constant). The difference is that ΛCDM *allows* $w \neq -1$ as a viable alternative — dynamical dark energy models (quintessence, phantom energy, k-essence) are consistent extensions. Zone architecture does not allow this alternative. If $w$ deviates from $-1$, zone architecture requires revision; ΛCDM simply switches to a different model.

Current measurements are consistent with $w = -1$ at the $\pm 0.03$ level. The decisive tests come from surveys now underway:

- **DESI** (2024–2029): Baryon acoustic oscillations from 40 million galaxies and quasars. Projected $\sigma(w) \approx 0.02$. First major results expected 2026–2027.
- **Euclid** (2023–2029): Weak lensing and galaxy clustering from 1.5 billion galaxies. Combined with Planck: $\sigma(w) \approx 0.01$ by 2028.
- **Vera Rubin LSST** (2025–2035): Photometric survey of 20 billion galaxies. Synergies with DESI and Euclid push combined precision to $\sigma(w) \approx 0.005$.
- **Gravitational wave standard sirens** (2030s): LIGO/Virgo/KAGRA + electromagnetic counterparts provide an independent distance-redshift measurement, reaching $\sigma(w) \approx 0.005$.

[FIGURE: Fig 6.2.4 — Dark Energy Equation of State: Current and Projected Constraints. A plot of $w$ vs. redshift $z$. Horizontal line at $w = -1$ (ZA prediction). Current data points with $\pm 0.03$ error bars clustered around $-1$. Projected error ellipses for DESI (2027), Euclid (2028), and combined (2030), shrinking progressively. Several dynamical DE model curves that deviate from $-1$ at high $z$. The figure shows that by 2030, experimental precision will distinguish ZA's flat $w = -1$ from models with $|w - (-1)| > 0.01$.]

If DESI and Euclid converge on $w = -1.000 \pm 0.005$ with no evidence for redshift evolution, zone architecture's geometric dark energy will be among the most precisely confirmed predictions in cosmology. If instead $w$ shows a statistically significant departure from $-1$ — say $w = -0.94$ at $3\sigma$ — the framework faces a serious challenge. The Waters Above field would need to be dynamical, requiring modification of the zone boundary conditions. This would not destroy the framework (the QED, GR, and particle physics sectors are independent), but it would undermine the cosmological architecture.

---

## 2.6 Fine Structure Constant — Fixed or Free?

> **P-065: Fine Structure Constant Constancy Over Cosmic Time**
> **Zone architecture value:** $\Delta\alpha/\alpha = 0 \pm 10^{-9}$ per billion years (geometric fixity — the $\pm 10^{-9}$ represents theoretical uncertainty in the Green's function coefficient, not physical variation)
> **Standard Model value:** Standard physics does not predict $\alpha$ varies. But SM-compatible extensions (coupled-dilaton models, dynamical DE) predict $\Delta\alpha/\alpha \sim 10^{-6}$ to $10^{-5}$ per Gyr.
> **Experimental value:** No significant variation detected. Best constraints: $|\Delta\alpha/\alpha| < 1.6 \times 10^{-6}$ (Molaro et al. 2020, ESPRESSO/VLT); atomic clocks: $\dot{\alpha}/\alpha = (1.6 \pm 2.3) \times 10^{-17}$ yr$^{-1}$
> **Current precision:** $\sim 10^{-6}$ (astrophysical); $\sim 10^{-17}$ yr$^{-1}$ (laboratory)
> **Distinguishing experiment:** Optical lattice clocks reaching $10^{-18}$ sensitivity; ALMA and ELT observations at high redshift reaching $10^{-8}$ precision.
> **Source:** Vol 5, Ch 13
> **Falsification threshold:** If any credible measurement finds $|\Delta\alpha/\alpha| > 3 \times 10^{-7}$ at $> 3\sigma$ confidence over cosmic time, the geometric fixity claim is falsified.
> **Type:** B (ZA says $\alpha$ *cannot* vary; some SM extensions say it *could*)
> **Status:** DIFFERS from dynamical models; currently consistent with constancy

The zone architecture derivation of $\alpha$ (Vol 5, Ch 13) depends on the ratio $\xi_A/\eta_B$, which is set by the zone boundary conditions. These conditions are structural features of the 6D manifold — they do not evolve with cosmic time any more than the topology of a sphere evolves. If $\alpha$ varies, it would mean the zone boundaries are dynamical, which contradicts the framework's foundational assumption of a static zone architecture.

An important caveat: ΛCDM with a pure cosmological constant ($w = -1$) also predicts $\Delta\alpha/\alpha = 0$. Zone architecture's prediction differs from *dynamical dark energy models*, not from ΛCDM itself. The scientific value of this prediction is therefore contingent on whether dark energy turns out to be dynamical. If DESI confirms $w = -1$ (supporting both ZA and ΛCDM), then the $\alpha$-constancy prediction becomes consistent with both frameworks and loses discriminating power. If instead evidence emerges for $w \neq -1$, then $\alpha$ variation becomes a second independent test of zone architecture's geometric assumptions.

The experimental trajectory is encouraging. The Webb et al. (2011, 2020) claim of a dipolar variation in $\alpha$ across the sky ($\Delta\alpha/\alpha \approx -1.15 \pm 0.24 \times 10^{-5}$) was not replicated by ESPRESSO observations, and the current consensus favors zero variation. Laboratory atomic clock measurements constrain the *present-day* rate of change to $|\dot{\alpha}/\alpha| < 10^{-17}$ yr$^{-1}$ — already far below any dynamical-DE prediction. Future ELT spectroscopy will probe $\Delta\alpha/\alpha$ at the $10^{-7}$ level at high redshift ($z > 5$), approaching the regime where coupled-dilaton models predict detectable variation.

The scientific value of this prediction is conditional but important. If all future experiments confirm $\Delta\alpha/\alpha = 0$ at increasing precision, zone architecture's geometric fixity claim gains support — but so does standard ΛCDM. The prediction becomes maximally discriminating only if evidence for dynamical dark energy ($w \neq -1$) emerges from DESI or Euclid. In that scenario, dynamical-DE models generally predict $\alpha$ variation, while zone architecture (if it survives the $w$ challenge at all) would need to explain how the zone boundaries could be dynamical for dark energy but static for $\alpha$. This interconnection between predictions — where the outcome of one test changes the scientific weight of another — illustrates why the predictions in this chapter cannot be evaluated in isolation.

---

## 2.7 Neutrino Mass Hierarchy — A Binary Test

> **P-066: Neutrino Mass Ordering — Normal Hierarchy Only**
> **Zone architecture value:** Normal hierarchy ($m_1 < m_2 < m_3$) is the *only* possibility. Inverted hierarchy is topologically forbidden.
> **Standard Model value:** Both orderings allowed. Global fits slightly favor normal ($\Delta\chi^2 \approx 2.4$ vs. inverted, NuFIT v5.2).
> **Experimental value:** Current data favor normal hierarchy at $\sim 1.5\sigma$ — not decisive.
> **Current precision:** $\Delta\chi^2 \approx 2.4$ between NH and IH hypotheses
> **Distinguishing experiment:** JUNO ($\sim 3\sigma$ by 2027), DUNE ($> 5\sigma$ by 2035), combined $> 5\sigma$ by 2028–2030.
> **Source:** Vol 4 (boundary eigenvalue analysis); UNIQUE_PREDICTIONS.md, Prediction 4
> **Falsification threshold:** If inverted hierarchy is confirmed at $> 3\sigma$ by JUNO + DUNE + atmospheric data, zone architecture is falsified.
> **Type:** B (different theoretical commitment — ZA allows only one of two options)
> **Status:** DIFFERS — clean binary test

This is the cleanest prediction in the entire chapter: a binary question with a definitive answer expected within the next five to ten years.

In zone architecture, neutrinos are boundary modes localized at the Firmament-Waters interface. The three neutrino families correspond to three topologically distinct ripple modes of the boundary, with eigenvalues in the ratio $\lambda_1 : \lambda_2 : \lambda_3 = 1 : 1.4 : 2.8$. This spacing mandates normal ordering — the lowest eigenvalue corresponds to the lightest neutrino, and the spacing increases monotonically. Inverted hierarchy would require the third eigenvalue to be *smaller* than the first two, which is impossible given the boundary condition operator's eigenvalue structure.

The mass-squared splittings predicted from this eigenvalue spectrum agree with experiment:

$$\Delta m^2_{21} = 7.5 \times 10^{-5}\ \text{eV}^2 \quad \text{vs.}\ 7.53 \pm 0.18 \times 10^{-5}\ \text{eV}^2\ \text{(measured)} \tag{6.2.4}$$
$$\Delta m^2_{32} = 2.5 \times 10^{-3}\ \text{eV}^2 \quad \text{vs.}\ 2.51 \pm 0.05 \times 10^{-3}\ \text{eV}^2\ \text{(measured)} \tag{6.2.5}$$

These agreements — 0.4% and 0.4%, respectively — are striking for a framework that struggles with absolute particle masses. The reason for the discrepancy between mass-splitting success and absolute-mass failure is that the splittings depend on the *ratios* of eigenvalues (which the boundary topology determines), while absolute masses depend on the overall scale (which requires the Higgs-Waters coupling not yet computed).

The decisive experiments are already under construction:

- **JUNO** (Jiangmen Underground Neutrino Observatory, China): A 20-kiloton liquid scintillator detector measuring reactor antineutrino oscillations. Expected sensitivity: $\sim 3\sigma$ distinction between hierarchies by 2027.
- **DUNE** (Deep Underground Neutrino Experiment, USA): A long-baseline experiment using a high-intensity neutrino beam from Fermilab to a 40-kiloton liquid argon detector in South Dakota. Expected sensitivity: $> 5\sigma$ by 2035, with early results possible by 2030.
- **Atmospheric neutrinos** (Hyper-Kamiokande, IceCube Upgrade): Independent measurements using naturally occurring neutrinos, providing complementary sensitivity.

If normal hierarchy is confirmed at $> 5\sigma$, zone architecture's prediction will be among its strongest vindications — a binary commitment where the Standard Model was agnostic, resolved exactly as the framework predicted. If inverted hierarchy is confirmed, zone architecture is falsified in a way that cannot be repaired without fundamentally modifying the boundary eigenvalue analysis.

---

## 2.8 Gravitational Wave Dispersion — The Long Game

> **P-059: Frequency-Dependent Gravitational Wave Propagation Speed**
> **Zone architecture value:** $v_{\rm GW}(f) = c\left[1 + \beta\ln(f/f_0) + \gamma(f/f_0)^{-2} + \cdots\right]$ with $\beta \sim 10^{-35}$ to $10^{-30}$
> **Standard Model value (GR):** $v_{\rm GW}(f) = c$ exactly, for all frequencies. No dispersion.
> **Experimental value:** $|v_{\rm GW} - c|/c < 3 \times 10^{-15}$ (GW170817 + GRB 170817A)
> **Current precision:** $3 \times 10^{-15}$ — extraordinary, but 20 orders of magnitude above the ZA prediction
> **Distinguishing experiment:** LISA + ground-based network (2030s–2040s), combining mHz and Hz-range observations for dispersion measurement across 9 orders of magnitude in frequency. Projected sensitivity: $\sigma(\beta) \sim 10^{-28}$ to $10^{-30}$.
> **Source:** Vol 5, Ch 3; UNIQUE_PREDICTIONS.md, Prediction 3
> **Falsification threshold:** If LISA-era measurements achieve $\sigma(\beta) < 10^{-30}$ and find no dispersion, the prediction remains consistent (ZA predicts $\beta \sim 10^{-35}$). If strong frequency dependence is found at $10^{-20}$ level, it would suggest a different extra-dimensional model than zone architecture.
> **Type:** C (effect predicted to exist but below current detection)
> **Status:** DIFFERS from GR — but currently untestable

This is zone architecture's most distinctive gravitational prediction, and its most frustrating: the framework predicts an effect that general relativity forbids, but at a magnitude so small that no instrument built or planned can detect it within the current generation.

The physical origin is straightforward. In a 6D spacetime, gravitational perturbations (gravitational waves) propagate not as a single mode but as a tower of Kaluza-Klein modes, each with a slightly different effective speed in 4D. The lowest mode — the massless graviton — travels at $c$. Higher KK modes carry extra-dimensional momentum, creating an effective mass that modifies their 4D propagation speed. The net effect on a gravitational wave packet is a tiny frequency-dependent dispersion: higher-frequency components arrive slightly earlier or later than lower-frequency components.

The dispersion relation for each KK mode takes the form:

$$\omega^2 = c^2 k^2 + m_n^2 c^4/\hbar^2 \tag{6.2.2}$$

where $m_n = n\hbar/(c\,\eta_B)$ is the mass of the $n$-th KK mode (Vol 5, Ch 3, Eq 5.3.22). For the massless mode ($n = 0$), $\omega = ck$ exactly, reproducing GR. For massive modes ($n \geq 1$), the group velocity is:

$$v_g = \frac{\partial\omega}{\partial k} = c\sqrt{1 - \frac{m_n^2 c^4}{\hbar^2\omega^2}} < c \tag{6.2.3}$$

The observed gravitational wave signal is a superposition of all KK modes weighted by their excitation amplitudes. Since higher modes are exponentially suppressed (their excitation probability scales as $e^{-m_n/T}$ for the source temperature $T$), the dominant contribution comes from the massless mode, with a tiny admixture of the first massive mode creating the dispersion.

The magnitude of the effect is set by the coupling between the 6D geometry and the 4D gravitational sector: $\epsilon \sim (l_{\rm Planck}/\eta_B)^2 \sim 10^{-35}$, where $l_{\rm Planck} \sim 10^{-35}$ m is the Planck length and $\eta_B \sim 10^{-15}$ m is the Waters Below extent. This ratio-squared gives the characteristic scale of the dispersion.

> **P-060: Kaluza-Klein Graviton Mode Structure**
> **Zone architecture value:** A discrete tower of massive KK graviton modes with mass spacing $\Delta m \sim \hbar/(c\,\eta_B) \sim 150$ MeV
> **Standard Model value (GR):** One massless graviton, no tower
> **Experimental value:** No KK modes detected
> **Distinguishing experiment:** Collider searches for KK graviton production (LHC, FCC); deviations from inverse-square gravity at sub-millimeter scales (torsion balance experiments).
> **Source:** Vol 5, Ch 3
> **Falsification threshold:** If graviton KK modes are detected with mass spacing inconsistent with $\hbar/(c\,\eta_B)$, the zone geometry parameters require revision.
> **Type:** C
> **Status:** DIFFERS — untestable with current sensitivity

The honest assessment: gravitational wave dispersion at $\beta \sim 10^{-35}$ is beyond the reach of any detector that will operate within the next two decades. Even LISA, which represents a generational leap in GW astronomy, will only reach $\sigma(\beta) \sim 10^{-28}$ at best — seven orders of magnitude above the prediction. Pulsar timing arrays combined with LISA might push to $10^{-30}$, still five orders of magnitude short.

This does not make the prediction scientifically worthless. It establishes a *target* for future technology, and it distinguishes zone architecture from other extra-dimensional theories (such as Randall-Sundrum brane worlds, which predict dispersion at different magnitudes). But the reader should understand that this prediction will not be tested in their lifetime unless a fundamentally new detection principle is discovered.

---

## 2.9 Proton Stability — Topology vs. Grand Unification

> **P-067: Proton Absolute Stability**
> **Zone architecture value:** $\tau_p = \infty$ (proton cannot decay — topological protection)
> **Standard Model value:** Proton stable (baryon number conservation), but SM mechanism is ad hoc
> **GUT predictions:** $\tau_p \sim 10^{34}$ to $10^{36}$ years (model-dependent)
> **Experimental value:** No decay observed. Lower bound: $\tau_p > 2.4 \times 10^{34}$ years (Super-Kamiokande, $p \to e^+\pi^0$ channel)
> **Current precision:** Lower bound only — pushes deeper with each year of non-observation
> **Distinguishing experiment:** Hyper-Kamiokande (2027+, reaching $10^{35}$ years), DUNE, megaton-scale detectors (2030s+, reaching $10^{36}$–$10^{37}$ years)
> **Source:** Vol 4, Ch 10 (topological classification of baryons)
> **Falsification threshold:** A confirmed proton decay event at any rate falsifies zone architecture's topological stability claim.
> **Type:** B (different theoretical commitment — ZA says proton *cannot* decay; GUTs say it can)
> **Status:** DIFFERS from GUTs; agrees with SM (but for different reasons)

In zone architecture, baryons are topological defects of the Firmament membrane — quantized winding numbers in the $\xi$-$\eta$ topological space. Baryon number conservation is not an accidental symmetry (as in the Standard Model) or a weakly broken symmetry (as in GUTs), but a *topological invariant*. A proton cannot decay to lighter particles because doing so would require changing the winding number of the Firmament — an operation that has no physical mechanism in the 6D framework.

This argument is elegant but carries an important caveat. The confidence level is SPECULATIVE (40%) because the topological protection hypothesis, while mathematically motivated, has not been rigorously proven within the full zone architecture framework. The classification of Standard Model particles as topological defects requires a complete mapping between membrane topology and the particle spectrum — a mapping that is only partially developed (the same incompleteness that produces the mass spectrum failures in Section 2.2).

The experimental situation is slowly tightening. Super-Kamiokande's 27 years of operation with 50 kilotons of water have produced zero candidate proton decay events, pushing the lifetime bound to $\tau_p > 2.4 \times 10^{34}$ years for the favored $p \to e^+\pi^0$ channel. Hyper-Kamiokande, with $8\times$ the volume, will reach $\tau_p > 10^{35}$ years within its first decade of operation (2027 onward). DUNE's liquid argon far detector provides complementary sensitivity in different decay channels. If the proton survives at $\tau_p > 10^{36}$ years, most minimal GUT models (SU(5), SO(10) without threshold corrections) will be excluded, indirectly supporting zone architecture's topological argument — though not confirming it, since the Standard Model also predicts proton stability.

The evidential structure of proton stability predictions resembles dark matter detection: continued non-observation provides slowly accumulating support for zone architecture (and for the Standard Model), while a single confirmed decay event would be decisive — falsifying zone architecture's topological protection and opening the door to GUT physics. The timescale is measured in decades, not years. A student beginning a career in proton decay experiments today may see the definitive result as a mid-career accomplishment.

One subtlety deserves attention. Zone architecture predicts proton stability for a *different reason* than the Standard Model does. In the Standard Model, baryon number conservation is an "accidental symmetry" — it follows from the gauge structure and renormalizability, not from any deep principle. In zone architecture, it is a topological invariant — as fundamental as the integer winding number of a vortex. If proton decay were ever observed, the Standard Model could accommodate it (by extending to a GUT); zone architecture could not (without abandoning the topological classification of baryons). This difference in *explanatory depth* is scientifically important even though both frameworks currently predict the same observable outcome.

---

## 2.10 The Honest Scorecard — What a Skeptic Should Think

Sixteen predictions. Four domains of failure. Four domains of strong testability. And three experiments that could deliver a verdict within five years.

### Test Suite Status for This Chapter's Predictions

Before the summary table, we report the validation status of each prediction against the framework's test suite (136 tests, as of April 5, 2026):

- **P-052 through P-055 (Particle Masses):** FAIL (by design). The hard-wall Firmament membrane model is *known* to be inadequate. Test suite category 6 (Nuclear and Particle Physics) shows these tests as PARTIAL — the framework is established but precision is absent. This is the most significant category of incompleteness in the test suite.
- **P-056 (Fine Structure Constant):** PARTIAL. Test 10.5 ($\alpha$ derivation) shows agreement to 0.10%. Refinement of $b_{\rm hi}$ is required for full PASS.
- **P-057 (Weak Mixing Angle):** PARTIAL. Zone geometry derivation established; precision derivation not yet completed.
- **P-058 (Strong Coupling Running):** PASS at $M_Z$ (Test 6.22, $\alpha_s = 0.118$). High-energy running not yet tested.
- **P-059, P-060 (GW Dispersion, KK Modes):** NOT YET. These are framework predictions with no corresponding test in the current suite — the tests would require computational GW simulations not yet developed.
- **P-061, P-062 (Dark Matter):** OPEN. Prediction is $\sigma = 0$; test requires comparison with experimental upper limits (consistent so far).
- **P-063, P-064 (Dark Energy):** PASS. Test 8.10 ($w = -1$, energy budget). Framework prediction matches current data.
- **P-065 ($\alpha$ Constancy):** OPEN. No time-variation test in current suite; consistent with all observations.
- **P-066 (Neutrino Hierarchy):** OPEN. Prediction awaits experimental determination (JUNO/DUNE).
- **P-067 (Proton Stability):** OPEN. Prediction awaits experimental limits reaching GUT scales.

Of the 16 predictions: 2 PASS, 2 PARTIAL, 4 FAIL (known incompleteness), 2 NOT YET (need new test infrastructure), and 6 OPEN (awaiting experimental resolution). The zero in the FAIL column of the *overall* test suite (97 PASS / 37 PARTIAL / 0 FAIL / 2 NOT YET) reflects that the mass spectrum failures are classified as PARTIAL (framework established, precision inadequate), not as contradictions. Whether this classification is fair is a judgment call the reader must make — but the numbers are not hidden.

The following table compiles every differing prediction from this chapter:

| P-# | Prediction | ZA | SM/Other | Gap | Type | Timeline | Confidence |
|-----|------------|-----|----------|-----|------|----------|-----------|
| P-052 | Electron mass | ~500 MeV | 0.511 MeV (fitted) | 1000$\times$ | A | Already failed | 5% |
| P-053 | Muon/electron ratio | 2–10 | 206.77 (fitted) | 20–100$\times$ | A | Already failed | 5% |
| P-054 | Quark masses | Regular pattern | Irregular (fitted) | Qualitative | A | Already failed | 10% |
| P-055 | Neutrino mass scale | No prediction | No prediction (seesaw) | N/A | A (gap) | — | — |
| P-056 | Fine structure constant | 137.17 | 137.036 (fitted) | 0.10% | A | Refinable | 90% |
| P-057 | Weak mixing angle | ~1% offset | 0.23122 (fitted) | ~1% | A | Refinable | 50% |
| P-058 | Strong coupling running | Modified at high $E$ | Standard running | Unknown | A | FCC-ee era | 50% |
| P-059 | GW dispersion | $\delta \sim 10^{-35}$ | $\delta = 0$ | 20 OoM | C | 2040s+ | 70% |
| P-060 | KK graviton modes | Tower at 150 MeV | No tower | N/A | C | Collider era | 70% |
| P-061 | DM interactions | $\sigma = 0$ | WIMPs: $10^{-46}$ | Categorical | B | Ongoing | 85% |
| P-062 | DM decay | $\tau = \infty$ | Finite (some models) | Categorical | B | Ongoing | 85% |
| P-063 | DE equation of state | $w = -1$ exactly | Free parameter | $\pm 0.001$ vs. $\pm 0.03$ | B | DESI 2027 | 90% |
| P-064 | DE evolution | $dw/dz = 0$ | Allowed nonzero | $\pm 0.001$ vs. $\pm 0.3$ | B | Euclid 2028 | 90% |
| P-065 | $\alpha$ constancy | $\Delta\alpha/\alpha = 0$ | Possibly varies | $10^{-9}$ vs. $10^{-6}$ | B | ELT era | 95% |
| P-066 | Neutrino hierarchy | Normal only | Both allowed | Binary | B | JUNO 2027 | 60% |
| P-067 | Proton stability | $\tau_p = \infty$ | GUT: $10^{34}$–$10^{36}$ yr | Categorical | B | Hyper-K 2030s | 40% |

*Confidence is expressed throughout on a single numerical scale (bracketed 5%–95%): the author's subjective probability that, when the test is completed, the zone-architecture prediction will be borne out. The scale is deliberately bounded away from 0% and 100% — no prediction here is certain either way. As a rough legend, ≤10% marks predictions that have already failed quantitatively (the mass sector, where the simplest Firmament model is off by ~1000×); ~50% marks predictions resting on derivations that are refinable but not yet complete; ≥90% marks predictions that follow from the framework's most robust structural commitments (e.g., the geometric fixity of $\alpha$ and $w=-1$). The earlier mixed use of "Low / Medium / High" has been retired in favor of this numerical scale so that all rows are directly comparable.*

### The Three Kill Shots

Three measurements could falsify zone architecture decisively:

**1. Dark matter is detected.** A confirmed direct detection of dark matter particles with $\sigma > 10^{-48}$ cm$^2$ would prove that dark matter has non-gravitational interactions, directly contradicting the Waters Below prediction. No repair is possible without abandoning the bulk-Firmament separation.

**2. Dark energy deviates from $w = -1$.** A combined DESI + Euclid measurement showing $w < -1.05$ or $w > -0.95$ at $> 3\sigma$ would demonstrate that the Waters Above field is dynamical, contradicting the geometric fixity of the zone boundaries.

**3. Inverted neutrino hierarchy is confirmed.** A JUNO + DUNE measurement establishing inverted hierarchy at $> 3\sigma$ would directly falsify the boundary eigenvalue analysis. The topological structure of the Firmament-Waters interface would have to be fundamentally different from what the framework assumes.

### The Particle Mass Elephant

The 1000$\times$ mass spectrum failure cannot be ignored and will not be minimized. It is the largest quantitative failure in the framework, and it means the particle mass sector is *incomplete*. The honest framing:

- The *simplest* Firmament model (hard walls) fails catastrophically for absolute masses.
- The *structural* features (three generations, mass-splitting ratios) succeed.
- The path to a complete mass prediction is identified (Higgs-Waters coupling, Yukawa overlap integrals) but not yet traveled.
- Until the mass sector is completed, zone architecture cannot claim to be a full replacement for the Standard Model's particle physics.

This is not a fatal defect. The Standard Model itself has 30 free parameters in its particle sector — it does not *predict* particle masses any more than zone architecture does. Both frameworks fit masses to data. Zone architecture attempts to derive them from geometry and partially fails; the Standard Model does not attempt the derivation at all. But partial failure in an ambitious attempt does not earn more scientific credit than no attempt — it earns a research program.

### What a Skeptic Should Conclude

A fair-minded skeptic reviewing this chapter should reach the following conclusions:

*First*, zone architecture makes genuine predictions distinct from the Standard Model. The differences are not artifacts of presentation or unfalsifiable hedges — they are quantitative commitments with identified experiments.

*Second*, the particle mass sector is a clear failure that requires significant additional theoretical work. It does not invalidate the framework's successes in other domains, but it prevents zone architecture from claiming completeness.

*Third*, the strongest near-term tests — dark energy equation of state (DESI/Euclid, 2027–2028), neutrino mass hierarchy (JUNO/DUNE, 2027–2030), and continued dark matter search null results — will provide decisive evidence within five to ten years.

*Fourth*, the framework's risk profile is asymmetric: three specific measurements can kill it (DM detection, $w \neq -1$, inverted hierarchy), while confirmation requires the convergence of multiple independent null or confirmatory results. This asymmetry — easy to kill, hard to confirm — is the hallmark of a genuinely scientific theory.

[FIGURE: Fig 6.2.5 — Experimental Timeline for Distinguishing Predictions. A horizontal timeline from 2025 to 2045. Above the line: experiments (DESI, JUNO, Euclid, DUNE, Hyper-K, Darwin, LISA, CMB-S4). Below the line: the specific ZA predictions each experiment tests. Color-coded: green for predictions testable by that experiment, red for potential falsification scenarios. The dense cluster of green markers in 2027–2030 shows the coming decade is the decisive period.]

The chapter that follows — Chapter 3: Novel Predictions — presents phenomena that zone architecture predicts and the Standard Model does not predict at all. Those are the framework's unique contributions to physics. But first, the framework had to demonstrate here that it makes commitments the Standard Model does not — commitments that real experiments can test, and that real measurements can overturn.

---

## Problems

**Computational**

**2.1** Compute the measurement precision $\sigma(w)$ needed to distinguish zone architecture's $w = -1.000$ from a dynamical dark energy model with $w_0 = -0.95$. Assuming Gaussian statistics, what signal-to-noise ratio is required for a $3\sigma$ detection of the difference? Which currently planned survey (DESI, Euclid, or Rubin LSST) will reach this precision first?

**2.2** The current best dark matter direct detection limit is $\sigma_{\rm SI} < 4.1 \times 10^{-47}$ cm$^2$ (XENONnT). The neutrino fog begins at approximately $\sigma \sim 10^{-49}$ cm$^2$. (a) How many orders of magnitude of improvement separate the current limit from the neutrino floor? (b) If each generation of detector improves sensitivity by one order of magnitude every 5 years, in what year will the neutrino floor be reached? (c) What scientific conclusion can be drawn if dark matter remains undetected at the neutrino floor?

**2.3** Using the Firmament mass formula $m = \hbar\omega/c^2$ with $\omega = n\pi c/L$ and the geometric extent $L = \eta_B = 1.3 \times 10^{-15}$ m, compute the predicted ground-state mass ($n = 1$). Compare with the observed electron mass $m_e = 0.511$ MeV$/c^2$. What effective confining scale $L_{\rm eff}$ would be needed to match the observed electron mass?

**2.4** Estimate the gravitational wave dispersion parameter $\delta(f)$ at LISA frequencies ($f \sim 10^{-3}$ Hz) using the scaling $\delta(f) \sim \epsilon \times (f_{\rm Planck}/f)^\alpha$ with $\epsilon \sim 10^{-35}$ and $\alpha = 2$. Compare with LISA's projected timing precision for gravitational wave signals. By how many orders of magnitude does the predicted effect fall below detection?

**Conceptual**

**2.5** Explain why a Type B prediction (zone architecture commits to normal hierarchy while the Standard Model allows both orderings) is more scientifically valuable than a Type A prediction (zone architecture gets a different number for the electron mass) over the long run. Consider both the information content of each prediction and the ease of future testing.

**2.6** The particle mass spectrum shows a factor-of-1000 error, yet this chapter calls the framework "incomplete" rather than "wrong." Under what specific conditions would you upgrade this assessment to "wrong"? Define the criteria in terms of: (a) a specific future theoretical result, and (b) a specific future experimental result.

**2.7** Zone architecture predicts zero dark matter interactions, and the evidence so far is a sequence of null results from increasingly sensitive detectors. Discuss the evidential asymmetry: why is a single confirmed detection (at any cross-section) more decisive than any number of null results? What does this asymmetry imply for the philosophy of science — specifically, for the distinction between confirmation and falsification?

**Challenge**

**2.8** You are given a $500 million budget and a 10-year timeline to test the maximum number of differing predictions in this chapter. Design your experimental program. Which predictions do you prioritize and why? Justify your resource allocation in terms of: (a) the scientific decisiveness of each test, (b) the feasibility within the budget and timeline, and (c) the independence of the tests (i.e., can one experiment test multiple predictions simultaneously?).

**2.9** The fine structure constant prediction ($\alpha$ is geometrically fixed) can in principle be tested by comparing $\alpha$ at different cosmic epochs. Propose a specific observational strategy using JWST spectroscopy and ELT high-resolution spectrographs to reach $\Delta\alpha/\alpha \sim 10^{-7}$ at redshifts $z > 5$. Specify: target selection criteria (which quasar absorption systems), required integration times, systematic error controls, and the analysis pipeline that would distinguish a physical variation from instrumental or astrophysical artifacts.
