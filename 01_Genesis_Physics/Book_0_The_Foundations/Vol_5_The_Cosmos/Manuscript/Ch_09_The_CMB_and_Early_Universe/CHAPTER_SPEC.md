---
product: Foundations Vol 5
chapter: 9
title: The CMB and Early Universe
status: SPEC
author: Genesis Physics / Zone Framework
date: 2026-04-09
---

# Chapter 9 Specification: The CMB and Early Universe

## Mission

Take the sustaining-mode cosmological model of Vol 5 Ch 8 — the Firmament-projected Waters fluid, the Friedmann era structure, and the four density parameters — and use it to derive the observable structure of the cosmic microwave background: the recombination redshift, the photon decoupling surface, the acoustic peak positions, the relative peak heights, the Silk damping envelope, and the power-spectrum amplitude. Compare the resulting prediction to the Planck 2018 binned `TT` data quantitatively, with a chi-squared (or equivalent) figure of merit, and report it honestly. The chapter must answer the Skeptic's central question — *were any parameters tuned to match Planck?* — with a specific accounting of which numbers were inherited from non-CMB observations and which fall out of the chain.

## Requirements

Traced from Vol 5 WRITING_PROMPT.md and Vol 5 QUALITY_GATE.md.

| ID | Requirement | Source | Where Met |
|---|---|---|---|
| R5.9.1 | Recombination redshift $z_* \approx 1090$ derived from the Saha equation applied to the Firmament hydrogen-electron plasma at the temperature evolved from Ch 8 §8.8.3 ($T_0 = 2.725$ K, $T(z) = T_0(1+z)$) | Chapter prompt; CMB_POWER_SPECTRUM §VIII | §9.3 |
| R5.9.2 | Photon decoupling: visibility function $g(\eta)$ peak located at $z_\text{dec} \approx 1089$, width $\Delta z \approx 80$ | CMB_POWER_SPECTRUM §VIII; standard Boltzmann theory inherited from Vol 4 Ch 10 | §9.4 |
| R5.9.3 | Sound horizon at recombination $r_s(z_*) = c\!\int_0^{z_*} c_s(z')/[H(z')(1+z')]\,dz'$ derived from the Ch 8 era structure with $c_s = c/\sqrt{3(1+R_b)}$ and $R_b(z) = (3\rho_b/4\rho_\gamma)$, computed to give a number with stated uncertainty | CMB_POWER_SPECTRUM §IV; Ch 8 §8.9 (deferred from Ch 8 to Ch 9) | §9.5 |
| R5.9.4 | Angular-diameter distance to last scattering $d_A(z_*)$ computed from the Ch 8 distance integral (5.8.54) with the framework's $\Omega_i$ — value with uncertainty reported | CMB_POWER_SPECTRUM §I; Ch 8 §8.9 | §9.5 |
| R5.9.5 | First acoustic peak position $\ell_1 = \pi d_A(z_*)/r_s(z_*)$ corrected for the Rees–Sciama driving and pressure-anisotropy phase shifts; computed value with uncertainty reported alongside Planck 2018 ($\ell_1 = 220.6 \pm 0.6$) | CMB_TRANSFER_FUNCTION §§II–III | §9.6 |
| R5.9.6 | Higher peak positions $\ell_2, \ell_3, \ell_4, \ell_5$ derived as harmonics of $\ell_1$ with phase corrections and compared to Planck values | CMB_TRANSFER_FUNCTION §3.4 | §9.6 |
| R5.9.7 | Relative peak heights $C_2/C_1$ and $C_3/C_1$ derived from the baryon-loading factor $R_b$ and reported alongside observed values; the *negative* sign of the $C_2/C_1$ ratio is shown to follow from $R_b > 1/2$ | CMB_POWER_SPECTRUM §5.4; CMB_TRANSFER_FUNCTION §IV | §9.7 |
| R5.9.8 | Silk damping envelope $C_\ell^\text{damped} = C_\ell^\text{undamped}\exp[-(\ell/\ell_d)^2]$ derived with $\ell_d \sim 1300$ from photon diffusion in the prerecombination plasma, traced to membrane viscosity in §9.8.2 | CMB_POWER_SPECTRUM §VI; Vol 1 Ch 5 (Firmament membrane mechanics) | §9.8 |
| R5.9.9 | Power-spectrum amplitude $A_s \approx 2.1\times 10^{-9}$ identified as the *one* genuine inheritance from observation in this chapter (not derived in this volume; deferred to Vol 6); the spectral index $n_s = 0.965$ is shown to follow from the Vol 1 Ch 11 sustaining-mode expansion-rate parameter (qualitative; full derivation also Vol 6) | CMB_POWER_SPECTRUM §VII; Vol 1 Ch 11 | §9.9 |
| R5.9.10 | A *quantitative* fit to the Planck 2018 binned TT angular power spectrum: a $\chi^2/N_\text{dof}$ (or equivalent) is computed using the chapter's predicted $C_\ell$ against the public Planck 2018 binned TT data, and the result is reported with all stated assumptions and limitations. **The Skeptic's central question — "were parameters tuned post hoc?" — is answered specifically.** | Chapter prompt's KNOWN GAP (MEDIUM); Vol 5 QUALITY_GATE | §9.10 |
| R5.9.11 | Big-bang nucleosynthesis predictions ($Y_p \approx 0.245$, D/H, ⁷Li) inherited from Vol 4 Ch 10 (particle spectrum) and reported alongside observation; the unresolved ⁷Li problem is flagged honestly | CMB_POWER_SPECTRUM §IX; Vol 4 Ch 10 | §9.11 |
| R5.9.12 | The Sabbath Boundary's *observational signature* in the CMB is identified as the early-vs-late $H_0$ tension (Hubble tension), with the framework's specific quantitative prediction for the size of the discrepancy left as an open task to be derived in Ch 12 | Vol 5 WRITING_PROMPT (Sabbath Boundary scope); Ch 8 §8.8.1 | §9.12 |
| R5.9.13 | Test suite `Research/Mathematical_Models/08_Cosmology/test_cosmology.py` (CMB-relevant tests) is run, results reported, any failures explained | Chapter prompt | §9.13 |
| R5.9.14 | Forward links to Ch 10 (large-scale structure inherits the matter transfer function from this chapter), Ch 11 (DM/DE quantification uses the CMB constraints from this chapter), and Ch 12 (Hubble-tension/starlight chronology) explicit | Chapter prompt | §9.14 |
| R5.9.15 | Reviewer's Ledger (Vol 5 internal precedent) classifies every load-bearing claim as Derivation / Identity / Inheritance / Conjecture | Vol 5 internal precedent | §9.15 |

## Prerequisites (the reader must already know)

- **Vol 1 Ch 5** — Firmament as codimension-2 Firmament; tension $\sigma$; transverse-wave speed $c^2 = \sigma/\mu$ (Eq 1.5.37); membrane viscosity contribution to dissipation. *Used in §9.8.2 for Firmament interpretation of Silk damping.*
- **Vol 1 Ch 6** — Waters Above and Waters Below fields and the equilibrium profiles. *Used to inherit the four density parameters from Vol 5 Ch 8.*
- **Vol 1 Ch 11** — Zone thermodynamics, the four phases, and the Sabbath Boundary. *The chapter is restricted to sustaining mode after the Sabbath Boundary; the Boundary itself is the source of the Hubble-tension signature in §9.12.*
- **Vol 2 Ch 3** — Fine structure constant, Thomson cross section $\sigma_T = (8\pi/3)(e^2/m_e c^2)^2$, electron mass $m_e$. *Used in §9.4 for the visibility function and §9.8 for Silk damping.*
- **Vol 3 Ch 5** — Fluid dynamics, sound speed in compressible fluids, baryon-photon plasma equation of state. *Used in §9.5.*
- **Vol 3 Ch 8** — Phase transitions, the recombination crossover. *Used in §9.3.*
- **Vol 3 Ch 12** — Thermodynamics, Saha equation, ionization equilibrium. *Used in §9.3 for $z_*$ derivation.*
- **Vol 4 Ch 8** — Renormalization, precision treatment of constants. *Used to flag what is and is not free in this chapter.*
- **Vol 4 Ch 10** — Particle spectrum, weak-interaction freeze-out, neutron-proton ratio, BBN inputs. *Used in §9.11.*
- **Vol 5 Ch 1** — Einstein field equations on the Firmament (Eq 5.1.34), Bianchi identity. *Inherited from Ch 8.*
- **Vol 5 Ch 7** — Brane-nucleation surface as the past timelike boundary. *Inherited from Ch 8.*
- **Vol 5 Ch 8** — Friedmann constraint Eq (5.8.26), acceleration equation Eq (5.8.29), continuity Eq (5.8.30), era structure §8.7, density parameters Table 5.8.1, distance definitions §8.9, integrated $H_0, t_0, T_0$. **Direct foundation. The whole chapter is consequences of Ch 8.**

## "Why" Chain

1. **Why is there a CMB at all?** Because the Firmament plasma was hot enough early on for hydrogen to be ionized; photons were tightly coupled to free electrons through Thomson scattering; and as the Firmament expanded the temperature dropped below the hydrogen binding energy, electrons combined with protons, the universe became transparent, and the photon background — until then in equilibrium with the matter — streamed freely from the last-scattering surface to us. None of this is special to the framework; what is special is that the temperature evolution $T(z) = T_0(1+z)$ and the present-day temperature $T_0 = 2.725$ K were both *derived* in Vol 5 Ch 8 (§8.8.3), so the recombination redshift is also derived and not fit.
2. **Why does recombination happen at $T \sim 3000$ K instead of at $T \sim 13.6$ eV $\approx 158{,}000$ K?** Because the photon-to-baryon ratio $\eta_{\gamma b} \sim 10^9$ is enormous, so the high-energy tail of the Planck distribution keeps hydrogen ionized far below 13.6 eV; the Saha equation gives the correct crossover at $T \approx 0.3$ eV.
3. **Why is the CMB anisotropy small?** Because in sustaining mode the Waters fields and the Firmament matter are very nearly in their equilibrium configuration; the perturbations around equilibrium are small, of order $\delta T/T \sim 10^{-5}$. The smallness is set by the equilibrium energy scale; the framework does not put it in by hand any more than $\Lambda$CDM does, and §9.9 will defer the *amplitude* normalization to Vol 6.
4. **Why are there acoustic peaks at all?** Because before recombination the baryon-photon plasma supports pressure waves; the Firmament was filled with sound. Standing waves at integer multiples of the sound horizon set a comb of preferred wavelengths; these get projected onto the sky as a comb of preferred angular scales; the result is the famous peak structure.
5. **Why does the first peak land at $\ell \approx 220$ specifically?** Because $\ell_1 = \pi d_A(z_*)/r_s(z_*) \times (\text{phase corrections})$, and both $d_A$ and $r_s$ are determined by the era structure of Vol 5 Ch 8 from quantities that were derived (or inherited from non-cosmological sources) earlier. The peak position is a *prediction* of the framework — not a fit — modulo the load-bearing inheritances of Ch 8.
6. **Why is the second peak shorter than the first?** Because the baryon loading $R_b = 3\rho_b/(4\rho_\gamma)$ is large enough ($R_b \approx 0.6$ at recombination) that the inertial drag of the baryons on the photon-baryon fluid pulls the equilibrium of even-numbered (compression → rebound → rarefaction) oscillations down. The framework inherits this dynamics from Vol 3 Ch 5; what is novel is the *value* of $R_b$, which comes from $\Omega_b = 0.049$ and $\Omega_\gamma$ from Ch 8.
7. **Why is there a damping envelope cutting off power above $\ell \sim 1300$?** Because before recombination, photons random-walk through the electron-baryon plasma over a diffusion length $\lambda_d$ that, by recombination, is non-negligible compared to the smaller acoustic wavelengths. Sound waves shorter than $\lambda_d$ wash out — Silk damping. In the framework, Silk damping has an additional and consistent interpretation as *membrane viscosity* (Vol 1 Ch 5), but the standard photon-diffusion derivation is the load-bearing one.
8. **Why is the spectral index $n_s$ slightly less than 1?** Because the sustaining-mode expansion rate is not exactly de Sitter; the small departure from $n_s = 1$ is set by the running of the Hubble parameter through the Sabbath Boundary epoch. The full derivation belongs to Vol 6; this chapter takes $n_s = 0.965$ as an inheritance and shows that the sign of the deviation has the right sign in the framework.
9. **Why does the framework match Planck quantitatively, given that it does not have inflation?** Because *the equations of cosmological perturbation theory do not depend on whether the source of the initial conditions is inflation or the Sabbath-Boundary nucleation surface of Vol 5 Ch 7*. Once a near-scale-invariant primordial spectrum is supplied (from inflation in $\Lambda$CDM, from the Firmament-nucleation surface in this framework), the rest of the calculation is identical. The Skeptic should find this disturbing; §9.10 takes the discomfort seriously.
10. **Why is the Hubble tension the Sabbath Boundary's signature?** Because the CMB-inferred $H_0$ comes from the angular-diameter distance to recombination — i.e., from an integral over the *entire post-Boundary* expansion history — while the local distance ladder measures $H_0$ today. Any boundary discontinuity in the early-time evolution would shift the CMB-inferred value relative to the local one. The framework predicts a non-zero shift; the *size* of the shift is the discriminator that Vol 6 must compute.

## Key Deliverables (Foundations — derivation plan)

| # | Deliverable | Starts from | Ends at | Equation / Theorem |
|---|---|---|---|---|
| D1 | Recombination redshift $z_* = 1089$ from Saha + Boltzmann correction | Vol 3 Ch 12 (Saha); Ch 8 §8.8.3 ($T_0$) | $z_* \approx 1089$, last-scattering temperature $T_* \approx 2970$ K | §9.3, Eq (5.9.6) |
| D2 | Visibility function $g(\eta)$ and decoupling width $\Delta z \sim 80$ | Vol 4 Ch 10 (Boltzmann); D1 | $g(\eta)$ peaks at $z_\text{dec} = 1089$ | §9.4, Eq (5.9.11) |
| D3 | Sound horizon $r_s(z_*)$ from the Ch 8 era structure | Ch 8 §8.7 (era structure), Vol 3 Ch 5 (sound speed) | $r_s(z_*) = 144 \pm 1$ Mpc | §9.5, Eq (5.9.14) |
| D4 | Angular-diameter distance $d_A(z_*)$ | Ch 8 Eq (5.8.54); D1 | $d_A(z_*) = 13{,}900 \pm 50$ Mpc | §9.5, Eq (5.9.16) |
| D5 | First acoustic peak $\ell_1$ with phase corrections | D3, D4; Rees–Sciama analysis (CMB_TRANSFER_FUNCTION §III) | $\ell_1 = 220 \pm 5$ | §9.6, Eq (5.9.22) |
| D6 | Higher harmonics $\ell_2 \dots \ell_5$ | D5 | $\ell_2 = 540, \ell_3 = 810, \ell_4 = 1130, \ell_5 = 1430$ | §9.6, Table 5.9.1 |
| D7 | Peak height ratios $C_n/C_1$ from baryon loading $R_b$ | Vol 3 Ch 5; Ch 8 $\Omega_b, \Omega_\gamma$; D1 | $C_2/C_1 \approx 0.78$, $C_3/C_1 \approx 0.73$ | §9.7, Eq (5.9.30) |
| D8 | Silk damping scale $\ell_d$ from photon diffusion | Vol 2 Ch 3 (Thomson); Ch 8 era structure | $\ell_d \approx 1300$ | §9.8, Eq (5.9.34) |
| D9 | Quantitative fit to Planck 2018 binned TT spectrum | D5–D8 + inherited $A_s, n_s$ | $\chi^2/N_\text{dof}$ reported with full caveats | §9.10, Table 5.9.2 |
| D10 | BBN abundances inherited from Vol 4 Ch 10 | Vol 4 Ch 10 (n/p freeze-out, particle spectrum) | $Y_p = 0.245$, D/H $= 2.5\times 10^{-5}$, ⁷Li problem flagged | §9.11, Eqs (5.9.37–39) |
| D11 | Hubble-tension signature: framework predicts a non-zero CMB-vs-local $H_0$ offset | Ch 8 §8.8.1; Vol 1 Ch 11 (Sabbath Boundary) | Qualitative prediction; quantitative left to Vol 6 | §9.12 |
| D12 | Test-suite verification (relevant CMB tests) | D1–D9 | Pass/fail with residuals | §9.13 |

## Figures

Following the figure rules: every spatial relationship, transformation, multi-step derivation, and concept with a natural visual metaphor needs a figure. Foundations density target: 2–4 per chapter; this chapter has more because the CMB observables are inherently graphical and the comparison to Planck is meaningless without plots.

| ID | Title | Placement | Type | What it shows | Why needed |
|---|---|---|---|---|---|
| Fig 5.9.1 | Brane thermal history from radiation era to today | §9.2, after Eq (5.9.2) | Timeline | Temperature $T(z)$ on the vertical axis, redshift on the horizontal; key thresholds marked: BBN (1 MeV → 0.1 MeV), matter-radiation equality ($z\sim 3400$), recombination ($z=1089$), reionization ($z\sim 8$), today | Multi-event chronology — needs a single picture for the reader to keep the era structure straight |
| Fig 5.9.2 | Recombination as a Saha–Boltzmann transition | §9.3, after Eq (5.9.6) | Plot | Free-electron fraction $X_e(z)$ from $\sim 1$ at $z > 1500$ down to $\sim 10^{-4}$ at $z < 800$; the visibility function $g(\eta)(z)$ overlaid as a sharp peak at $z = 1089$, $\Delta z \sim 80$ | The crossover from opaque to transparent is the central physical event of the chapter |
| Fig 5.9.3 | Sound horizon and angular-diameter distance: the geometry | §9.5, after Eq (5.9.16) | Schematic | The Firmament FLRW spacetime drawn as a conformal diagram; the past light cone of "us today"; the last-scattering surface at $z_*$; the comoving sound horizon $r_s$ as a small circle on that surface; the projection onto the sky giving $\ell_1 \sim \pi d_A/r_s$ | Spatial relationship between $r_s$ (intrinsic ruler) and $d_A$ (projector) — must be visual |
| Fig 5.9.4 | The two clocks: $r_s$ as ruler, $d_A$ as projector | §9.6, after Eq (5.9.22) | Comparison panel | Left: $r_s(z_*) = 144$ Mpc derived from the era structure. Right: $d_A(z_*) = 13{,}900$ Mpc derived from the comoving-distance integral. Below: their ratio $\pi \times (d_A/r_s) \approx 304$, the naive first peak; the corrected (post Rees–Sciama, post pressure-anisotropy) value $\ell_1 = 220$ | The peak position has two ingredients with very different physical origins; the figure separates them |
| Fig 5.9.5 | The Planck 2018 TT spectrum and the framework's prediction | §9.10, after Table 5.9.2 | Plot | The Planck 2018 binned $\ell(\ell+1)C_\ell/2\pi$ in $\mu K^2$ vs $\ell$, with error bars; the framework's predicted curve overlaid; residuals $\Delta C_\ell/\sigma_\ell$ in a small panel below | This is the chapter's load-bearing comparison and must be visual |
| Fig 5.9.6 | Peak heights as a function of $R_b$ | §9.7, after Eq (5.9.30) | Plot | $C_n/C_1$ for $n = 2, 3, 4$ as functions of $R_b$ from $0$ to $1$; the framework's value $R_b = 0.6$ marked as a vertical line; the Planck-observed peak heights as horizontal bands at the framework $R_b$ | The baryon-loading dependence is the cleanest quantitative test of $\Omega_b$ |
| Fig 5.9.7 | Silk damping envelope | §9.8, after Eq (5.9.34) | Plot | The acoustic peak comb (idealized) multiplied by $\exp[-(\ell/\ell_d)^2]$ with $\ell_d = 1300$; the resulting damped envelope; horizontal axis in $\ell$, vertical in $\mu K^2$ | The damping envelope is the dominant feature of the spectrum at $\ell > 1500$ |
| Fig 5.9.8 | The Hubble-tension signature (qualitative) | §9.12 | Diagram | The CMB-inferred $H_0$ (gray box centered at 67.4 km/s/Mpc) and the local-distance-ladder $H_0$ (gray box centered at 73 km/s/Mpc), separated by an arrow labeled "Sabbath-Boundary discontinuity (Vol 1 Ch 11; Vol 5 Ch 12)"; explicit *no quantitative claim* note in the caption | Forward link; the figure prevents misreading the chapter's epistemic position |
| Fig 5.9.9 | Reviewer's Ledger | §9.15 | Table | Every load-bearing claim classified Derivation / Identity / Inheritance / Conjecture | Required for Vol 5 reviewer style |

## Problem Sets

Foundations chapters get problem sets graded computational → conceptual → challenge.

**Computational.**

1. Use the Saha equation $X_e^2/(1-X_e) = (2\pi m_e k_B T/h^2)^{3/2} (m_p/n_b) \exp(-B_H/k_B T)$ with $B_H = 13.6$ eV, $\Omega_b h^2 = 0.0223$, $T_0 = 2.725$ K, and the framework's $\Omega_i$ to find the redshift at which $X_e = 0.1$. Compare to the chapter's value $z_* \approx 1090$.

2. Compute the sound horizon $r_s(z_*)$ by numerical integration of $r_s = \int_0^{z_*} c_s(z')/[H(z')(1+z')]\,dz'$ with $c_s = c/\sqrt{3(1+R_b(z))}$ and $R_b(z) = 31500\,\Omega_b h^2/(1+z)$. Show that $r_s \approx 144$ Mpc.

3. Compute $d_A(z_*) = (c/H_0)/(1+z_*)\int_0^{z_*} dz'/E(z')$ with $E(z)$ from Ch 8 Eq (5.8.40). Verify $d_A(z_*) \approx 13{,}900$ Mpc.

**Conceptual.**

4. The framework derives the recombination redshift $z_*$, the angular-diameter distance $d_A(z_*)$, and the sound horizon $r_s(z_*)$. Yet it *inherits* the amplitude $A_s$ of the primordial power spectrum from observation. Why is $A_s$ in a different epistemic class from the others?

5. The Skeptic claims that any cosmological framework that has the same Friedmann era structure as $\Lambda$CDM and the same recombination physics will produce the same CMB spectrum, so the framework's match to Planck "doesn't count." State precisely what is and is not true about this objection.

6. Why is the second acoustic peak shorter than the first? Explain in your own words and identify the single cosmological parameter that controls the ratio.

**Challenge.**

7. Show that the integral $\ell_1 = \pi d_A(z_*)/r_s(z_*)$ is invariant (to leading order) under a uniform rescaling of $H_0$, holding the $\Omega_i$ fixed. Why does this make $\ell_1$ a *shape* observable rather than an *amplitude* observable?

8. The framework predicts a non-zero CMB-vs-local $H_0$ tension as a Sabbath-Boundary signature. Estimate, qualitatively, how large the tension would be if the Sabbath Boundary were a $\delta$-function discontinuity in the expansion rate at $z = 1$ vs. at $z = 100$. Which is more consistent with the observed $\sim 7\%$ tension? What would Vol 6 need to derive to nail this down?

9. Why is the ⁷Li problem unresolved by the framework as well as by $\Lambda$CDM? What new physics, if any, could close the gap?

## Verification Criteria

- All ten "Why?" questions answered from the geometry and the inherited dynamics, not by appeal to convention.
- The recombination redshift, the sound horizon, the angular-diameter distance, and the first peak position are derived step-by-step from Vol 5 Ch 8 plus standard inherited physics, with each step labeled.
- A *quantitative* fit to the Planck 2018 binned TT spectrum is reported with a $\chi^2/N_\text{dof}$ (or equivalent) and with full disclosure of which inputs were free and which were inherited.
- The Skeptic's central question is answered specifically in §9.10: which numbers were tuned, which were inherited from non-CMB observations, which fall out of the chain.
- The Hubble tension is identified as the Sabbath-Boundary signature without claiming a derivation; the Conjecture is flagged in §9.15.
- Forward links to Chs 10–12 are explicit.
- The chapter does not preach. The phrase "sustaining mode" appears with its zone-thermodynamic meaning (Vol 1 Ch 11), not as theology.
- The Physicist reviewer's central question — *"is the CMB power spectrum derived or smuggled in by using $\Lambda$CDM equations?"* — has a one-paragraph answer in §9.10 and a full answer in the Reviewer's Ledger.

## Research Gaps (flagged in advance)

| Gap | Severity | Mitigation |
|---|---|---|
| G1: The chapter prompt's KNOWN GAP — the quantitative CMB power spectrum fit to Planck — is the central technical task of §9.10. The CMB_POWER_SPECTRUM.md file gives the derivation chain but not a quantitative $\chi^2$. We will compute one in §9.10 using the simplest defensible approximation: take the framework's predicted peak positions and amplitudes, smooth with the Silk envelope, normalize against a single inherited $A_s$, and compare to the Planck 2018 binned TT spectrum. The result will be reported honestly. | MEDIUM | Treated head-on in §9.10. |
| G2: The full Boltzmann hierarchy is not solved in this chapter. We use the simplified analytical approximations of CMB_TRANSFER_FUNCTION.md (Rees–Sciama factor $\xi_\text{RS} \approx 0.79$, peak-position correction factor $\sim 1.52$) rather than running a CAMB-equivalent code. | MEDIUM | Stated openly in §9.6 and §9.10; the resulting peak positions are accurate to a few percent rather than per-mille; the chapter does not claim more. |
| G3: The amplitude normalization $A_s$ is inherited from observation, not derived. | HIGH (acknowledged) | Stated in §9.9 and §9.15; deferred explicitly to Vol 6. |
| G4: The spectral index $n_s = 0.965$ is inherited, with only a qualitative argument given for why it is less than 1. | MEDIUM (acknowledged) | Stated in §9.9 and §9.15; the qualitative argument is that the sustaining-mode expansion rate has a small running through the Sabbath Boundary epoch. |
| G5: The Hubble-tension prediction is qualitative; the chapter does not give a numerical value for the framework's expected size of the tension. | MEDIUM (acknowledged) | Stated in §9.12 and §9.15 as a Conjecture; deferred to Vol 6 (and Ch 12 of this volume for the chronology piece). |
| G6: The ⁷Li problem is unresolved. | LOW (universal) | Reported honestly in §9.11. |

## Word Count Target

10,000–13,000 words (30–40 pages). The single architectural claim is that *the entire CMB power spectrum follows from Vol 5 Ch 8 plus standard recombination physics*; everything else is consequences. The chapter must not become a survey of CMB physics — every section must advance the architectural claim.

## Notes on Voice

Feynman writing a textbook. Same register as Vol 5 Chs 1–8. The chapter has the mood of a careful confrontation: the CMB is the framework's most fearsome test, and the chapter knows it. There should be no triumphalism about the match to Planck — the match is presented with the qualifier that it is also the match $\Lambda$CDM achieves, and what makes it interesting in *this* framework is that the inputs were not fit at the cosmological scale. The Skeptic's reasonable objection — that the chapter is doing $\Lambda$CDM in zone-architecture clothing — must be taken seriously and answered specifically. The Theologian's interest is restricted to the Sabbath Boundary signature and the chronology forward link; the chapter does not preach.

---

*End of CHAPTER_SPEC.md. Proceed to Phase 2 (CHAPTER_OUTLINE.md).*
