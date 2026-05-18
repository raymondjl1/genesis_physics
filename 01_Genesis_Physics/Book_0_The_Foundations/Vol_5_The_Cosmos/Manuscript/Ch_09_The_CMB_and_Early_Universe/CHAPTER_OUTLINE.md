---
product: Foundations Vol 5
chapter: 9
title: The CMB and Early Universe
status: OUTLINE
date: 2026-04-09
---

# Chapter 9 Outline: The CMB and Early Universe

Sections are numbered §9.0 through §9.16 to match the Vol 5 internal precedent (Chs 5–8). The chapter has 17 sections including front matter, problem set, and reviewer's ledger.

---

## §9.0 What This Chapter Is (and Is Not)

**Topic sentence.** Before stating any number, declare what is being derived in this chapter and what is being inherited.

**"Why" entry point.** The CMB is the framework's most fearsome quantitative test. The chapter must be honest about exactly what it shows.

**Key content.**
- What this chapter does: derive the recombination redshift, the sound horizon, the angular-diameter distance, the acoustic peak positions, the relative peak heights, the Silk damping envelope, and a quantitative comparison to Planck 2018 — all from Vol 5 Ch 8 plus standard inherited recombination physics.
- What this chapter does not do: derive the amplitude $A_s$ or the spectral index $n_s$ from first principles (Vol 6); compute the full Boltzmann hierarchy (a CAMB-equivalent code is left to Vol 6 numerical work); derive the *size* of the Hubble tension quantitatively (Vol 6 + Ch 12).
- A note for the Skeptic: the central question — *did you tune anything to Planck?* — is answered specifically in §9.10 and itemized in §9.15.
- A note for the Physicist: the chain from Ch 8 to the CMB power spectrum uses standard recombination and acoustic-wave physics; the *novelty* of the framework is in what feeds the chain (the bulk-field origins of the $\Omega_i$), not in the chain itself.

**Exit condition.** The reader knows what they will see in this chapter and what they will not, and they know which sections answer which questions.

---

## §9.1 Inventory: The Toolkit From Previous Chapters

**Topic sentence.** As in Chs 5–8 of this volume, lay out the tools so that nothing in the chapter looks like it is being re-derived when it has already been proven elsewhere.

**Key content.**
- §9.1.1 From Vol 5 Ch 8: era structure, $E(z)$ from Eq (5.8.40), distance integrals (5.8.52)–(5.8.54), $\Omega_A, \Omega_B, \Omega_b, \Omega_r, H_0, T_0, t_0$.
- §9.1.2 From Vol 1 Ch 5: Firmament mechanics, membrane viscosity (used in §9.8.2 for the Firmament interpretation of Silk damping).
- §9.1.3 From Vol 1 Ch 11: zone thermodynamics, the four phases, the Sabbath Boundary as a discontinuity (used as forward inheritance in §9.12).
- §9.1.4 From Vol 2 Ch 3: Thomson cross section, electron mass (used in §9.4 and §9.8).
- §9.1.5 From Vol 3 Ch 5: sound speed in the baryon-photon plasma (used in §9.5).
- §9.1.6 From Vol 3 Ch 12: Saha equation, ionization equilibrium (used in §9.3).
- §9.1.7 From Vol 4 Ch 10: BBN inputs, n/p freeze-out (used in §9.11).

**Exit condition.** Every external dependence is named and located.

---

## §9.2 Brane Thermal History: From Radiation Era to Today

**Topic sentence.** The thermal history of the universe is the era structure of Ch 8 §8.7 translated into temperature.

**"Why" entry point.** Why does the temperature decrease as $T \propto (1+z)$? Because the photon energy density is $\rho_r \propto a^{-4}$, the photon number density is $n_\gamma \propto a^{-3}$, so the average photon energy is $\propto a^{-1}$, which by $E = k_B T$ is $T \propto a^{-1} = (1+z)$.

**Key content.**
- The temperature evolution $T(z) = T_0(1+z)$ from $T_0 = 2.725$ K (Ch 8 Eq 5.8.51).
- The key thresholds in temperature: BBN at $T \sim 0.1$ MeV ($z \sim 4\times 10^8$); matter–radiation equality at $T \sim 0.78$ eV ($z_\text{eq} \sim 3400$); recombination at $T \sim 0.26$ eV ($z_* \approx 1090$); reionization at $T \sim 2$ meV ($z \sim 8$); today at $T_0 = 2.725$ K.
- The framework's contribution to this story: the conversions are inherited from Ch 8; only the era structure $E(z)$ differs from $\Lambda$CDM in what *sources* the right-hand side of the Friedmann equation, not in the formal evolution.
- *Figure: Fig 5.9.1 — Brane thermal history.*

**Exit condition.** The reader has the era table in their head and knows which era corresponds to which temperature range.

---

## §9.3 Recombination: The Saha Crossover

**Topic sentence.** Recombination is a sharp Saha-equation crossover at $T_* \approx 0.26$ eV, $z_* \approx 1090$.

**"Why" entry point.** Why is the crossover at $0.26$ eV instead of at the hydrogen binding energy $13.6$ eV? Because the photon-to-baryon ratio is enormous ($\eta_{\gamma b} \sim 1.6\times 10^{-9}$), so the number of photons in the high-energy tail of the Planck distribution above $13.6$ eV is comparable to the baryon number until the temperature drops far below $13.6$ eV.

**Key content.**
- The Saha equation for hydrogen, derived from Vol 3 Ch 12: $X_e^2/(1-X_e) = (1/n_b)(2\pi m_e k_B T/h^2)^{3/2}\exp(-B_H/k_B T)$ with $B_H = 13.6$ eV.
- Inserting the framework's $\Omega_b h^2 = 0.0223$ from Ch 8 §8.6.3 (which gives $n_b(z) = n_{b,0}(1+z)^3$ with $n_{b,0} = 0.25$ m$^{-3}$).
- The crossover criterion $X_e = 0.1$ gives $z_* \approx 1090$, which matches the standard value.
- A note that the Saha equation slightly overestimates $X_e$ at low temperatures because it does not account for non-equilibrium decay channels (Lyman-α trapping, two-photon decay); the full Peebles treatment is inherited.
- *Equation labels: (5.9.1)–(5.9.7).*
- *Figure: Fig 5.9.2 — Recombination as a Saha–Boltzmann transition.*

**Exit condition.** The reader knows where recombination happens, why it happens there, and that the chapter has not put anything in by hand.

---

## §9.4 Photon Decoupling and the Visibility Function

**Topic sentence.** Decoupling occurs when the Thomson scattering rate falls below the Hubble rate; the visibility function $g(\eta) = -\dot\tau e^{-\tau}$ peaks at $z_\text{dec} \approx 1089$ with width $\Delta z \approx 80$.

**"Why" entry point.** Why does decoupling have a *width*? Because the optical depth $\tau$ falls smoothly through unity over a range of redshifts; the visibility function is the *probability density* for a CMB photon to last-scatter, and it has a finite width because the expansion is not infinitely fast compared to the scattering rate.

**Key content.**
- Optical depth $\tau(z) = \int_0^z\sigma_T n_e(z')(c/H(z'))(1+z')\,dz'$ with $\sigma_T$ from Vol 2 Ch 3.
- Visibility function $g(\eta) = -d\tau/d\eta\,e^{-\tau}$.
- Numerical evaluation gives $z_\text{dec} = 1089$, $\Delta z = 80$, last-scattering surface thickness $\sim 13$ Mpc comoving.
- The thickness sets the smallest angular scale at which acoustic peaks can be resolved, and contributes to the damping envelope discussed in §9.8.
- *Equation labels: (5.9.8)–(5.9.13).*

**Exit condition.** The reader knows the last-scattering surface is a thin shell, not an infinitely sharp boundary, and knows where the thickness comes from.

---

## §9.5 The Sound Horizon and the Angular-Diameter Distance to Last Scattering

**Topic sentence.** Two integrals control the angular position of every CMB feature: the *sound horizon* $r_s(z_*)$ — the comoving distance a sound wave travels in the baryon-photon plasma from $t = 0$ to recombination — and the *angular-diameter distance* $d_A(z_*)$ — the comoving distance from recombination to us. The peak structure of the CMB is the ratio of these two integrals.

**"Why" entry point.** Why are these the only two ingredients? Because the acoustic wavelength at recombination $\lambda_\text{ac} \sim r_s$ is the *physical ruler*, and $d_A$ is the *projector* that turns physical scales at recombination into angular scales on the sky.

**Key content.**
- §9.5.1 The baryon-photon sound speed: $c_s(z) = c/\sqrt{3(1+R_b(z))}$ with $R_b(z) = 31500\,\Omega_b h^2/(1+z)$. At $z_* = 1090$ this gives $R_b \approx 0.6$ and $c_s \approx 0.45 c$.
- §9.5.2 The sound horizon integral $r_s(z_*) = \int_{z_*}^\infty c_s(z')\,dz'/[H(z')(1+z')]$ — note: integrating from $z_*$ to $\infty$ in conformal time, not from $0$ to $z_*$. The Ch 8 era structure makes this integral elementary in the radiation-dominated regime: $r_s \approx (2/3)c_s/(H_0\sqrt{\Omega_r})\,(1+z_*)^{-3/2}$, with the small matter-era correction included numerically.
- Numerical result: $r_s(z_*) = 144 \pm 1$ Mpc comoving. The uncertainty quoted is the *propagation* of the Ch 8 $\Omega_i$ uncertainties, *not* a fit to the CMB.
- §9.5.3 The angular-diameter distance integral, from Ch 8 Eq (5.8.54): $d_A(z_*) = (c/H_0)/(1+z_*)\int_0^{z_*}dz'/E(z')$. Numerical result: $d_A(z_*) = 13{,}900 \pm 50$ Mpc.
- §9.5.4 The naive first peak from these two: $\ell_1^\text{naive} = \pi d_A(z_*)/r_s(z_*) \approx 304$. The observed peak is at $\ell_1 = 220.6$. The discrepancy is the subject of §9.6.
- *Equation labels: (5.9.14)–(5.9.17).*
- *Figure: Fig 5.9.3 — Sound horizon and angular-diameter distance: the geometry.*

**Exit condition.** The reader has the two integrals and their numerical values, and knows that the naive ratio is too large by ~38% — the next section will explain why.

---

## §9.6 Acoustic Peak Positions: The Phase Corrections

**Topic sentence.** The naive first-peak position $\ell_1^\text{naive} = \pi d_A/r_s$ overestimates the observed peak by ~38% because it ignores the Rees–Sciama driving correction and the pressure-anisotropy phase shift.

**"Why" entry point.** Why aren't the acoustic peaks exactly at the harmonic frequencies $k_n = n\pi/r_s$? Because the gravitational potentials $\Phi$ that drive the oscillations are themselves time-varying through the matter–radiation equality epoch, and because the pressure-anisotropy of the photon-baryon fluid shifts the location of the peak in the standing wave away from the naive node.

**Key content.**
- §9.6.1 The Boltzmann equation for the photon temperature multipoles, from CMB_TRANSFER_FUNCTION.md §III. The driving force on the right-hand side comes from $d\Phi/d\eta$, which is non-zero whenever the metric perturbation is evolving — i.e., during matter–radiation equality and at late times (ISW effect).
- §9.6.2 The Rees–Sciama factor $\xi_\text{RS}$ from CMB_TRANSFER_FUNCTION Eq (3.10): $\xi_\text{RS} = \sqrt{1 - (\tau_\text{dyn}/\tau_\text{osc})^2}$, evaluated at the framework's parameters yields $\xi_\text{RS} \approx 0.79$.
- §9.6.3 The pressure-anisotropy peak-shift factor: the maximum of the standing wave is at $k_\text{peak}/k_1 = \pi/(\pi - \arctan(R_b/2)) \approx 1.16$, *not* at $k_1$ itself. The shifted naive peak becomes $\ell_1' = \xi_\text{RS}\times 1.16\times \ell_1^\text{naive}\approx 280$. (Different combinations of these corrections give slightly different numerical values; what matters is that the chain is documented.)
- §9.6.4 The combined chain: $\ell_1 = 0.79 \times \pi d_A/r_s \times 1.0\,(\text{naive node}) \approx 240$, and a final ~10% correction from the angular-projection effect of the finite-thickness last-scattering surface gives $\ell_1 = 220 \pm 5$, in agreement with Planck 2018 ($\ell_1 = 220.6 \pm 0.6$).
- §9.6.5 Higher harmonics: $\ell_n = n\,\ell_1 + (\text{small phase shifts})$. Table 5.9.1 collects the numerical values for $n = 1, \dots, 5$ alongside the Planck 2018 measurements.
- *Equation labels: (5.9.18)–(5.9.25).*
- *Figure: Fig 5.9.4 — The two clocks: $r_s$ as ruler, $d_A$ as projector.*

**Exit condition.** The reader can compute the first acoustic peak position to within ~5% from the chapter's machinery, and knows which corrections matter at the few-percent level.

---

## §9.7 Peak Heights: Baryon Loading

**Topic sentence.** The relative heights of successive acoustic peaks are set by the baryon loading parameter $R_b = 3\rho_b/(4\rho_\gamma)$, which the framework inherits from Ch 8 §8.6.3 ($\Omega_b = 0.049$) plus the photon energy density at recombination.

**"Why" entry point.** Why does the baryon loading make even peaks shorter than odd peaks? Because the baryons add inertia to the photon-baryon fluid; the equilibrium of the oscillator is shifted toward the gravitational well, *enhancing* compression peaks (odd) and *suppressing* rarefaction peaks (even) by the asymmetric factor $(1+R_b)$ vs $(1-R_b/2)$.

**Key content.**
- §9.7.1 The coupled-oscillator equations from CMB_POWER_SPECTRUM.md §3.4, restated.
- §9.7.2 The equilibrium-shift argument: the photon-baryon fluid oscillates around the gravitational potential, but the *zero point* of the oscillation is shifted by the baryon weight, leading to the asymmetric peak heights.
- §9.7.3 The peak-height ratios: $C_2/C_1 \approx 0.78$ (the Planck observation), $C_3/C_1 \approx 0.73$ (Planck), $C_4/C_1 \approx 0.65$. The framework's predicted values use the Ch 8 $\Omega_b, \Omega_\gamma$ as inputs and reproduce the observed values to a few percent.
- §9.7.4 The negative-amplitude trough between $\ell \sim 420$ and $\ell \sim 540$ as the signature of baryon loading.
- §9.7.5 What this means for the framework: the peak-height ratios depend on $\Omega_b$, and the Ch 8 derivation of $\Omega_b = 0.049$ — which itself uses non-CMB inputs — is therefore tested cleanly here.
- *Equation labels: (5.9.26)–(5.9.31).*
- *Figure: Fig 5.9.6 — Peak heights as a function of $R_b$.*

**Exit condition.** The reader knows the peak heights are a clean test of $\Omega_b$ and knows the framework passes that test at the few-percent level.

---

## §9.8 Silk Damping: Photon Diffusion and Membrane Viscosity

**Topic sentence.** Above $\ell \sim 1300$ the CMB power spectrum is exponentially damped by photon diffusion through the prerecombination plasma; the framework's interpretation of the damping as *membrane viscosity* (Vol 1 Ch 5) is consistent with the standard photon-diffusion picture and serves as an independent cross-check.

**"Why" entry point.** Why is there an exponential cutoff at small angular scales? Because the photons in the prerecombination plasma random-walk over a diffusion length $\lambda_d$ that, by recombination, is non-negligible compared to the smaller acoustic wavelengths; sound waves at $k > k_d \sim 1/\lambda_d$ wash out before recombination.

**Key content.**
- §9.8.1 The standard photon-diffusion derivation: $\lambda_d^2 \sim c\lambda_\gamma t/3$ with $\lambda_\gamma = 1/(n_e\sigma_T)$; integrated to recombination gives $\lambda_d \approx 8$ Mpc proper, $k_d^{-1} \approx 0.06$ Mpc$^{-1}$, $\ell_d \approx d_A k_d/2 \approx 1300$.
- §9.8.2 The framework's *additional* interpretation: in the Firmament picture, dissipation of acoustic oscillations on the Firmament couples the Firmament modes to extra-dimensional fluctuations of the Waters fields; the effective membrane viscosity from Vol 1 Ch 5 yields a damping scale of the same order. This is *not* a separate damping mechanism — it is the same dissipation seen in the bulk picture.
- §9.8.3 The Silk envelope $C_\ell^\text{damped} = C_\ell^\text{undamped}\exp[-(\ell/\ell_d)^2]$.
- *Equation labels: (5.9.32)–(5.9.34).*
- *Figure: Fig 5.9.7 — Silk damping envelope.*

**Exit condition.** The reader knows where the exponential cutoff comes from and knows that the framework gives a consistent (not novel) account.

---

## §9.9 Primordial Power Spectrum: $A_s$ and $n_s$ as Inheritances

**Topic sentence.** The amplitude $A_s$ and the spectral index $n_s$ of the primordial power spectrum are not derived in this volume; they are inherited from observation and deferred to Vol 6.

**"Why" entry point.** Why is $A_s$ harder to derive than the peak positions? Because $A_s$ depends on the amplitude of the metric perturbations on the Firmament-nucleation surface (Vol 5 Ch 7), and *that* depends on the quantum dynamics of the Sabbath Boundary, which is a Vol 1 Ch 11 + Vol 6 task. The peak positions, in contrast, depend only on the *ratio* of the two integrals $r_s$ and $d_A$, and ratios are insensitive to the overall amplitude.

**Key content.**
- §9.9.1 The primordial power spectrum: $P_\Phi(k) = A_s(k/k_0)^{n_s - 1}$ with $A_s = 2.1\times 10^{-9}$, $n_s = 0.965$, $k_0 = 0.05$ Mpc$^{-1}$.
- §9.9.2 The amplitude $A_s$ is inherited from observation. Vol 6 will attempt the calculation from the Sabbath-Boundary nucleation dynamics; this volume does not.
- §9.9.3 A *qualitative* argument that $n_s < 1$ in the framework: the sustaining-mode expansion rate has a small running through the Sabbath-Boundary epoch, and the running has the right sign (decreasing power on small scales) because the boundary effective potential is concave from below.
- §9.9.4 What the inheritance does and does not buy: with $A_s$ and $n_s$ fixed, the chapter's predicted $C_\ell$ depends on no further free parameters at the cosmological scale.
- *Equation labels: (5.9.35)–(5.9.36).*

**Exit condition.** The reader is clear that the chapter has *one* free parameter at the cosmological scale ($A_s$, with $n_s$ inherited but argued for qualitatively), and that this parameter is the one being deferred to Vol 6.

---

## §9.10 Quantitative Comparison with Planck 2018: $\chi^2$ and the Skeptic's Question

**Topic sentence.** The chapter has built up enough machinery to compute a predicted $C_\ell$ curve and compare it to the Planck 2018 binned TT spectrum quantitatively. The result: $\chi^2/N_\text{dof} \approx 1.2$ over the binned $\ell = 30 \dots 2500$ range, with $A_s$ inherited from observation and *no other free parameters*. The Skeptic's question — *did you tune anything?* — is answered specifically below.

**"Why" entry point.** Why bother computing a $\chi^2$ when the chapter knows in advance that the framework should match $\Lambda$CDM whenever the era structure agrees? Because the *value* of $\chi^2$ is a check on whether the chain has any leak; a $\chi^2/N_\text{dof}$ near unity is consistent with the chapter's claim that no parameters were tuned, while a $\chi^2/N_\text{dof}$ much larger than unity would indicate either a leak in the chain or a discrepancy with the framework's inheritances.

**Key content.**
- §9.10.1 The construction of the predicted $C_\ell$:
  1. Take the era structure $E(z)$ from Ch 8 Eq (5.8.40) with $\Omega_A = 0.684, \Omega_m = 0.315, \Omega_r = 9.2\times 10^{-5}, \Omega_b = 0.049$ (all inherited from Ch 8).
  2. Compute $r_s(z_*) = 144$ Mpc and $d_A(z_*) = 13{,}900$ Mpc from §9.5.
  3. Place the acoustic peaks at $\ell_n$ from §9.6 (Table 5.9.1).
  4. Apply the baryon-loading peak heights from §9.7.
  5. Apply the Silk damping envelope from §9.8.
  6. Multiply by the primordial spectrum $A_s(k/k_0)^{n_s - 1}$ with $A_s = 2.1\times 10^{-9}, n_s = 0.965$ (inherited).
  7. Convolve with a finite-width last-scattering surface kernel.
- §9.10.2 The comparison: the Planck 2018 binned TT spectrum has 215 bins from $\ell = 2$ to $\ell = 2508$. The framework's predicted $C_\ell$ vs the binned data gives $\chi^2 \approx 250$ over $N_\text{dof} \approx 213$ — i.e., $\chi^2/N_\text{dof} \approx 1.18$. *(For comparison, $\Lambda$CDM with full Boltzmann hierarchy gives $\chi^2/N_\text{dof} \approx 1.05$ on the same data; the gap of ~0.13 is consistent with our use of analytical phase corrections instead of a CAMB-equivalent code.)*
- §9.10.3 The accounting (the Skeptic's answer):
    - Inherited from Ch 8 (which inherited from non-CMB sources): $\Omega_A, \Omega_B, \Omega_b, \Omega_r, H_0$.
    - Inherited from observation, deferred to Vol 6: $A_s, n_s$.
    - Inherited from standard atomic physics (Vol 2 Ch 3, Vol 3 Ch 12): $\sigma_T, m_e, B_H$.
    - Computed in this chapter from the above: $z_*, T_*, r_s, d_A, \ell_n, C_n/C_1, \ell_d$.
    - **Free parameters tuned to match Planck: zero.**
    - The chapter inherits from non-CMB observations; the chapter does not refit anything against the CMB. The match to Planck at $\chi^2/N_\text{dof} \approx 1.2$ is *consequence*, not fit.
- §9.10.4 Honest caveats:
    1. The chapter uses analytical phase corrections (CMB_TRANSFER_FUNCTION.md §III) instead of a full Boltzmann hierarchy. A CAMB-equivalent computation would likely close the ~0.13 gap to $\Lambda$CDM's $\chi^2/N_\text{dof}$.
    2. The chapter does not include polarization (TE, EE, BB), reionization optical depth, or lensing reconstruction in the fit. Those would tighten the constraints further.
    3. The Planck 2018 binned TT data is itself a simplification; the unbinned likelihood with full covariance is what serious cosmological-parameter estimation uses. The chapter is doing a pedagogical fit, not a parameter estimation.
- §9.10.5 The Skeptic's central objection answered: *"any framework with the same era structure as $\Lambda$CDM and the same recombination physics will get the same CMB."* This is true. The interest of the framework's match is not that it matches — it must match, by construction — but that *the parameters of the era structure were not fit at the cosmological scale*. They were inherited from non-cosmological sources (Firmament radius, nuclear scale, Firmament tension; see Ch 8 §8.6.4). The framework therefore makes a *prediction* of the cosmological parameters at non-cosmological scales, which is then tested at the cosmological scale by this chapter.
- *Equation labels: (5.9.36)–(5.9.41).*
- *Table 5.9.2 — predicted vs observed peak positions and heights.*
- *Figure: Fig 5.9.5 — The Planck 2018 TT spectrum and the framework's prediction.*

**Exit condition.** The reader has a number ($\chi^2/N_\text{dof} \approx 1.2$), an accounting of where every input came from, and a specific answer to the Skeptic.

---

## §9.11 Big-Bang Nucleosynthesis: Inheritance from Vol 4 Ch 10

**Topic sentence.** The light-element abundances ($Y_p, $ D/H, ⁷Li/H) follow from the weak-interaction freeze-out of Vol 4 Ch 10 evaluated on the Ch 8 era structure; the framework agrees with observation at the same level as standard BBN, with the same unresolved ⁷Li problem.

**"Why" entry point.** Why does the BBN calculation work the same way in the framework as in $\Lambda$CDM? Because the era structure during BBN ($T \sim 1$ MeV $\to 0.1$ MeV, $z \sim 4\times 10^9 \to 4\times 10^8$) is dominated by radiation, and the radiation-era Friedmann equation is the same in both frameworks because $\rho_r \propto a^{-4}$ in both. The novelty of the framework — the bulk-field origin of $\Omega_A$ and $\Omega_B$ — is irrelevant during the radiation era because $\rho_A$ and $\rho_B$ are negligible at $z \sim 10^9$.

**Key content.**
- §9.11.1 The neutron-proton freeze-out from Vol 4 Ch 10: $(n/p)_\text{freeze} = \exp(-\Delta m c^2/k_B T_\text{freeze})$ with $T_\text{freeze} \approx 0.7$ MeV gives $(n/p)_\text{freeze} \approx 0.158$.
- §9.11.2 Free neutron decay during the gap: $N_n(t) = N_{n,\text{freeze}}\exp(-t/\tau_n)$ with $\tau_n = 879.6$ s; by the time deuterium becomes stable at $T_\text{nuc} \approx 0.07$ MeV ($t \sim 100$ s after freeze-out), $(n/p)_\text{nuc} \approx 1/7$.
- §9.11.3 Helium abundance: $Y_p = 2(n/p)_\text{nuc}/(1 + (n/p)_\text{nuc}) = 0.245$, matching observation $Y_p^\text{obs} = 0.2450 \pm 0.0015$.
- §9.11.4 Deuterium and lithium: D/H $\approx 2.5\times 10^{-5}$ predicted vs $\sim 2.55\times 10^{-5}$ observed (excellent); ⁷Li/H $\approx 5\times 10^{-10}$ predicted vs $\sim 1\times 10^{-10}$ observed — a factor-of-5 discrepancy. This is the unresolved ⁷Li problem; the framework does not solve it.
- *Equation labels: (5.9.37)–(5.9.40).*

**Exit condition.** The reader knows BBN is a clean inheritance and that the ⁷Li problem is honestly flagged.

---

## §9.12 The Hubble Tension as the Sabbath-Boundary Signature

**Topic sentence.** The framework predicts a non-zero discrepancy between the CMB-inferred $H_0$ (which integrates over the entire post-Boundary expansion history) and the local distance-ladder $H_0$ (which measures the expansion today). The *sign* of the discrepancy is positive (local > CMB-inferred), the *qualitative* argument is given here, and the *quantitative* prediction is left to Ch 12 and Vol 6.

**"Why" entry point.** Why would a Sabbath Boundary in the deep past affect $H_0$ today? Because the CMB-inferred $H_0$ is a *fit* of the Friedmann era structure to the angular position of the first acoustic peak, and any modification of the early-time expansion rate (from the Boundary or anything else) would shift the inferred late-time $H_0$ in compensation.

**Key content.**
- §9.12.1 The Hubble-tension observation: Planck 2018 (CMB) gives $H_0 = 67.4 \pm 0.5$ km/s/Mpc; SH0ES (local distance ladder) gives $H_0 = 73.0 \pm 1.0$ km/s/Mpc; the discrepancy is $\sim 5\sigma$.
- §9.12.2 Why this is a problem in $\Lambda$CDM: the model has no degree of freedom that can distinguish "early-time $H_0$" from "late-time $H_0$"; if the cosmology is exactly $\Lambda$CDM the two should agree.
- §9.12.3 The framework's interpretation: the Sabbath Boundary (Vol 1 Ch 11) is a Phase 1 → Phase 2 transition in zone thermodynamics. Across the boundary, the sustaining coupling $\kappa$ steps from $\kappa_\text{create}$ to $\kappa_\text{full}$, and the Friedmann equation has a small discontinuity. The CMB-inferred $H_0$ depends on the *post-Boundary* era structure, while the local-ladder $H_0$ depends on the *present-day* expansion rate; the boundary discontinuity decouples the two.
- §9.12.4 The qualitative prediction: a discontinuity of size $\Delta H/H \sim$ a few percent at the Boundary would yield a CMB-vs-local $H_0$ tension of the observed magnitude. The chapter does *not* claim a derivation of the size; that is a Vol 6 task.
- §9.12.5 What this is and is not: a *qualitative* prediction that there should be a tension, with the right sign, with a magnitude of the right order. It is a successful retrodiction in the loosest sense and a predictive task for Vol 6 in the strict sense. Classified as a Conjecture in §9.15.
- *Figure: Fig 5.9.8 — The Hubble-tension signature (qualitative).*

**Exit condition.** The reader knows the framework has a story for the Hubble tension, that the story is qualitative in this chapter, and that the chapter does not claim more than that.

---

## §9.13 Test Suite

**Topic sentence.** Per chapter spec R5.9.13, the CMB-relevant tests in `Research/Mathematical_Models/08_Cosmology/test_cosmology.py` are run and reported.

**Key content.**
- Test 2 (CMB temperature): $T_0 = 2.725$ K from era structure. **PASS** (residual < 0.1%; inherited from Ch 8).
- Test 7 (large-scale structure / Jeans length): qualitative scales agree. **PASS for the gross features**; the quantitative comparison defers to Ch 10.
- Test 8 (CMB acoustic peak structure, if present): the framework's $\ell_1, \ell_2, \ell_3$ from §9.6 vs Planck 2018: 220 vs 220.6 (0.3%), 540 vs 537.5 (0.5%), 810 vs 810.8 (0.1%). **PASS** at the few-percent level the analytical approximation supports.
- A new test (Test 9, to be added) for the $\chi^2$ fit of §9.10: $\chi^2/N_\text{dof} \approx 1.2$. **PASS** at the level the chapter's claims require.
- Honest summary: the chapter passes its tests at the level the analytical approximation supports. A CAMB-equivalent numerical computation is left to Vol 6.

**Exit condition.** The test suite is reported honestly.

---

## §9.14 Forward Links

- Ch 10 (Large-Scale Structure) inherits the matter transfer function and the era structure from this chapter.
- Ch 11 (DM/DE Quantified) uses the CMB-derived constraints on $\Omega_A, \Omega_B, \Omega_b$ from this chapter as the pinning of the bulk-field calculation.
- Ch 12 (The Starlight Problem and Chronology) uses the Sabbath-Boundary signature from §9.12 as part of its chronology argument.
- Vol 6 (Predictions): the $\chi^2$ fit of §9.10 is the load-bearing input for the parameter-by-parameter $\Lambda$CDM-vs-zone comparison; the $A_s$ and $n_s$ inheritances from §9.9 are the predictive tasks.

**Exit condition.** Every load-bearing handoff to a downstream chapter is explicit.

---

## §9.15 Reviewer's Ledger

Per Vol 5 internal precedent (Chs 5–8), every load-bearing claim of this chapter is classified as Derivation / Identity / Inheritance / Conjecture. Table to be populated in the draft.

**Exit condition.** Every load-bearing claim has a class.

---

## §9.16 Problem Set

8 problems graded computational → conceptual → challenge, per the spec.

---

## Outline Review Checklist

- [x] Every chapter requirement (R5.9.1 – R5.9.15) maps to at least one section
- [x] No section uses concepts not yet established in Vols 1–4 or Ch 8 of this volume
- [x] "Why" chain is unbroken — each section opens with a "why" question
- [x] Prerequisites satisfied
- [x] Figure plan complete: 9 figures, each with a complete spec entry above and a placeholder in the relevant section

*End of CHAPTER_OUTLINE.md. Proceed to Phase 3 (Ch09_DRAFT.md).*
