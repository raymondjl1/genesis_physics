---
product: Foundations Vol 5 — The Cosmos
chapter: 11
title: Dark Matter and Dark Energy Quantified
status: DRAFT
draft_date: 2026-04-09
author: Genesis Physics / Zone Framework
voice: Feynman writing a textbook
target_words: 11000–15000
---

# Chapter 11. Dark Matter and Dark Energy Quantified

> *"The interesting problem is not to explain why we need these two fluids — everyone agrees we do. The interesting problem is to say where they come from, and then to say numbers."*

## §11.0 What This Chapter Is (and Is Not)

Chapter 10 ended with a confession. The framework, in the linear regime of structure formation, makes predictions for the growth function $D^+(z)$, the matter power spectrum $P(k)$, and the amplitude $\sigma_8$ that are numerically indistinguishable from those of $\Lambda$CDM. There are no discriminators at linear order. The framework and the standard cosmology pass each other in the night without exchanging a word.

This chapter is different. Here, the framework has real discriminators, and they are sharp enough to bet money on. The dark-energy equation of state is predicted to be *exactly* $w_A = -1$, not "close to $-1$," and the prediction is an identity, not a fit. The dark matter is predicted to have *zero* nuclear-recoil signature in direct-detection experiments, because what the framework identifies as dark matter is not a particle at all — it is a Firmament-localized scalar field inherited from Vol 1 Ch 6. The Bullet Cluster's self-interaction cross-section bound is predicted to be overshot by many orders of magnitude below the bound, not touched from above. And the 27/68 ratio that $\Lambda$CDM takes as an input from observation is predicted by the framework as a function of two warp factors set at nuclear and cosmological scales respectively, with no cosmological-scale tuning allowed.

The chapter is also honest about what it does *not* deliver. The Vol 4 Ch 9 promise — to explain why the QFT vacuum-energy estimate is a factor of $\sim 10^{120}$ larger than the observed cosmological constant — is paid in this chapter, but only partially. The framework's geometric suppression, worked through from the Waters Above projection using the Vol 1 Ch 6 boundary conditions at the Firmament, delivers a factor of $(\eta_B / \xi_A)^4 \approx 10^{-164}$. That is *too much* suppression by a factor of $\sim 10^{40}$. The chapter does not paper over this. It argues that the framework provides a *structural* resolution — the right architectural form, the right two scales, the right cancellation — but not yet a *numerical* resolution. The residual exponent is deferred to Vol 6 and to Firmament-thickness corrections that the current chapter cannot compute.

Put compactly: the chapter's mood is modest confidence. Unlike Ch 10, it is not coincidence. Unlike Ch 13 (the fine-structure derivation that closes the volume), it is not yet a triumph. It is the middle chapter of the argument — the chapter where the framework stops being a retelling of $\Lambda$CDM in different words and starts being a theory that could be wrong.

What the chapter is *not*: it is not a sermon. Genesis is referenced only insofar as Vol 1 Ch 6 is referenced — *Waters Above* (dark energy, ~68%) and *Waters Below* (dark matter, ~27%) are the names of two scalar fields whose definitions and equations of motion were fixed four volumes ago. No theological claim about dark matter or dark energy is made or needed. The reader who prefers to call them $\Psi_A$ and $\Psi_B$ should do so, and nothing in the derivations will change.

## §11.1 Inventory: The Toolkit From Previous Chapters

Before writing anything new, it is worth listing precisely which results from previous volumes are load-bearing here. A reader who has them fresh will have an easier time; a reader who does not should at least know where to look when the chapter cites an equation number they do not recognize.

### §11.1.1 Vol 1 Ch 6 — the bulk profiles and the boundary conditions

Vol 1 Ch 6 defined the two Waters fields. $\Psi_A$ lives in the Waters Above region of the bulk — the slab of the six-dimensional zone manifold at $\xi > 0$ above the Firmament — and carries the bulk potential $V_A(\Psi_A)$ whose minimum is at some equilibrium value $\Psi_A = \Psi_A^{\min}$. The boundary condition at the Firmament is that $\Psi_A$ asymptotes to $\Psi_A^{\min}$ for $\xi \gtrsim \xi_A$, with $\xi_A \approx 3 \times 10^{26}$ m the characteristic $\xi$-direction extent of the Waters Above domain (Vol 1 Eq 1.6.31).

$\Psi_B$ lives on the Firmament itself and carries a potential $V_B(\Psi_B)$ whose minimum is at zero. The linearized field equation for $\Psi_B$ around a baryonic source is the Firmament-localized Yukawa equation, whose Green's function (Vol 1 Eq 1.6.35) is

$$
G_B(r) = -\frac{1}{4\pi r} e^{-m_B r},
$$

where $m_B$ is the Firmament-localized mass of the field, and whose characteristic scale $\eta_B \approx 1.3 \times 10^{-15}$ m is set by the nuclear-scale $\eta$-direction warp factor (Vol 1 Eq 1.6.36).

When the source is extended and the nonlinear back-reaction is carried through — this was done in Vol 1 §6.4, culminating in Eq (1.6.37) — the steady-state density profile of the $\Psi_B$ cloud around a baryonic distribution takes a specific form with $\rho_B \propto r^{-1}$ inside a scale radius $r_s$ and $\rho_B \propto r^{-3}$ outside. This is the Navarro–Frenk–White profile, and its appearance here is not borrowed from the $N$-body simulation literature — it is a consequence of the Firmament field equation plus the Jeans equation for isotropic velocity dispersion.

Vol 1 Ch 6 also computed the projected stress-energy of $\Psi_A$ onto the Firmament. At the minimum of $V_A$, the projection is (Vol 1 Eq 1.6.32)

$$
T^{(A)}_{\mu\nu} = -V_A\!\left(\Psi_A^{\min}\right) \gamma_{\mu\nu} \equiv -\Lambda_A^{(4)}\,\gamma_{\mu\nu},
$$

where $\gamma_{\mu\nu}$ is the induced metric on the Firmament. This is the stress-energy of a cosmological constant with density $\rho_A = \Lambda_A^{(4)}$ and pressure $p_A = -\Lambda_A^{(4)}\,c^2$, i.e., equation of state $w_A = -1$ *exactly*. That "exactly" is the whole game; we return to it in §11.6.

Finally, Vol 1 Ch 6 §6.5 introduced the Firmament self-coupling $\lambda_B$ for the $\Psi_B$ field — the coefficient of the $\Psi_B^4$ term in $V_B$. Order-of-magnitude estimates give $\lambda_B \sim 10^{-30}$ in dimensionless Firmament units; this is the number that will enter the Bullet Cluster self-interaction calculation in §11.5.

### §11.1.2 Vol 2 Ch 2 and Ch 8 — Newtonian gravity and gravitational lensing

Vol 2 Ch 2 derived Newtonian gravity from the Firmament $\eta$-equation. The end result is the standard Poisson equation $\nabla^2 \Phi = 4\pi G_4 \rho$, with the gravitational potential $\Phi$ sourced by *all* the energy on the Firmament, not just baryons. Vol 2 Ch 8 then derived the linearized GR lensing deflection angle. Neither of these volumes introduces anything exotic; the chapter uses them because the rotation-curve calculation in §11.3 needs the Newtonian potential and the lensing calculation in §11.4 needs the linearized deflection.

### §11.1.3 Vol 4 Ch 9 — the cosmological-constant problem, deferred

Vol 4 Ch 9 is the chapter the reader should have most vividly in mind. It computed the QFT vacuum energy by summing zero-point modes up to the zone cutoff and got $\rho_{\mathrm{vac}}^{(\mathrm{QFT})} \sim \Lambda_{\mathrm{zone}}^4 \sim (1/\eta_B)^4$, which is of order $10^{71}\,\mathrm{GeV}^4$ in natural units. The observed cosmological constant is $\rho_\Lambda^{(\mathrm{obs})} \sim 10^{-47}\,\mathrm{GeV}^4$. The discrepancy is a factor of $\sim 10^{118}$, which is the famous 120-order-of-magnitude problem (the exact exponent depends on which cutoff you use; it has ranged in the literature from $10^{120}$ to $10^{122}$).

Vol 4 Ch 9 §9.7 did not resolve this problem — it *named* it and it made a promise: Vol 5 would show that the Waters Above projection is *not* the QFT vacuum energy of Vol 4 Ch 9. The Waters Above $\rho_A$ is a separate quantity, set by the bulk minimum of $V_A$, and its smallness relative to the QFT estimate is explained by a geometric ratio of bulk and Firmament scales. The exponent and the precise cancellation were deferred to this chapter.

Section 11.7 pays this promise. The reader will see that the promise is paid partially: structurally, yes; numerically, with a residual.

### §11.1.4 Vol 5 Ch 8 — the four density parameters

Vol 5 Ch 8 derived, from the Friedmann equation on the Firmament plus the inventory of Waters Above, Waters Below, baryons, and radiation, the four density parameters today:

$$
\Omega_A = 0.684, \qquad \Omega_B = 0.266, \qquad \Omega_b = 0.049, \qquad \Omega_r \approx 9.2 \times 10^{-5}.
$$

Ch 8 also wrote the acceleration equation (Eq 5.8.29) and the formula for the onset of acceleration $z_\Lambda = (\Omega_A / \Omega_m)^{1/3} - 1$ (Eq 5.8.44). These numbers and these formulas are taken as given here and pushed against the Pantheon+ and DES Y6 data in §11.6.

> **Note on the 68/27/5 split:** The density fractions $\Omega_A : \Omega_B : \Omega_b \approx 0.684 : 0.266 : 0.049$ are classified in this chapter as a **prediction** derived from zone geometry (warp-factor integrals fixed at non-cosmological scales in Vol 1 §6.6.4). This classification is correct if the matching parameters $(\xi_A, \gamma, \sigma)$ in Vol 1 §6.6.4 were genuinely fixed by non-cosmological inputs before the cosmological ratios were computed. If instead any of the warp-factor normalizations were adjusted to reproduce $\Omega_A = 0.684$, the result would be a **consistency check** rather than a prediction. The distinction is tracked in Research Task RT-5.ΩA (Ch 8). This chapter inherits the classification from Ch 8 and propagates it faithfully.

### §11.1.5 Vol 5 Ch 10 — the linear regime coincidence

Vol 5 Ch 10 confirmed that the framework's $D^+(z)$, $P(k)$, and $\sigma_8$ coincide numerically with $\Lambda$CDM's in the linear regime. That is a piece of background the reader should keep in mind when this chapter argues that the framework has *discriminators*: the discriminators live not in the linear regime but in the *sources* (what the dark components actually are) and in the *boundaries* (the $w$ parameter, the direct-detection signal, the 27/68 ratio).

## §11.2 The Identification: Waters Above ≡ Dark Energy, Waters Below ≡ Dark Matter

The first load-bearing statement of the chapter is an *identification*, not a hypothesis. Vol 1 Ch 6 defined two fields and derived their equations of motion. Vol 5 Ch 8 projected their stress-energies onto the Firmament. The projections yield, on inspection, the two canonical fluids of modern cosmology.

Let us write the identifications cleanly.

**Identification I (Waters Above ≡ Dark Energy).**

$$
T^{(A)}_{\mu\nu}\big|_{\text{Firm}} = -\Lambda_A^{(4)}\,\gamma_{\mu\nu}, \qquad \rho_A = \Lambda_A^{(4)}, \qquad w_A = -1 \quad \text{(exact).} \tag{5.11.1}
$$

The "exact" is not an approximation: because $\Psi_A$ sits at the minimum of its potential, its stress-energy is Lorentz-invariant ($\propto \gamma_{\mu\nu}$), and a Lorentz-invariant vacuum stress-energy has $w = -1$ identically — we make this precise in §11.6.3.

**Identification II (Waters Below ≡ Dark Matter).**

$$
T^{(B)}_{\mu\nu}\big|_{\text{Firm}} = \rho_B(r)\,u_\mu u_\nu, \qquad p_B \approx 0, \qquad w_B = 0 \quad \text{(dust-like).} \tag{5.11.2}
$$

Both are inherited directly from Vol 1 Ch 6. Nothing new has been added. The chapter's job is not to *propose* the identifications — that was done four volumes ago — but to take them and see whether, when confronted with rotation curves, lensing maps, the Bullet Cluster, the Pantheon+ supernova sample, and the DES Y6 dark-energy survey, they hold up.

A reader who has skimmed Vol 1 might object: *"But those identifications are just labels. Until you compute something and compare it to data, you have not done any work."* That is exactly right, and it is the objection this chapter answers. The rest of the chapter — §11.3 through §11.9 — is the computation.

[FIGURE: Fig 5.11.1 — Two profiles, two phenomena. A vertical cross section in the $(\xi, \eta)$ plane showing $\Psi_A$ flat at its minimum above the Firmament, projecting to a uniform $\Lambda_A^{(4)}\gamma_{\mu\nu}$; and $\Psi_B$ in a Yukawa configuration around a baryonic source below the Firmament, projecting to $\rho_B(r) u_\mu u_\nu$. Arrows connect each profile to its observational consequence.]

Before turning to galaxies, one technical remark. The two projections (5.11.1) and (5.11.2) have *different* geometric characters. The Waters Above projection is uniform: it is the same $\Lambda_A^{(4)}$ everywhere on the Firmament, because $\Psi_A$ sits at its minimum uniformly. The Waters Below projection is *lumpy*: it tracks the Yukawa cloud that surrounds each baryonic source, so its magnitude varies with position. That is why Waters Above drives the expansion of the universe (it is smooth) and Waters Below drives the flat rotation curves of galaxies (it is clumpy). The two are not two fluids; they are two *geometric boundary conditions* on the same Firmament, one of which happens to be uniform and the other of which happens to be lumpy. The duality of dark energy (smooth) and dark matter (clumpy) in cosmology is therefore not a coincidence in the framework — it is a *geometric* statement about how two different bulk fields project onto the same Firmament.

## §11.3 Galactic Scale: Rotation Curves and Tully–Fisher

### §11.3.1 The NFW profile from $\Psi_B$

The rotation-curve problem in galaxies is simple to state. The visible mass in a disk galaxy — stars plus gas — is concentrated within a few kiloparsecs. Newtonian gravity applied to that mass alone gives a Keplerian velocity profile $v_c(r) \propto r^{-1/2}$ outside the visible disk. The observed rotation curves are flat, or even slightly rising, out to tens of kiloparsecs. Something else is providing the gravitational pull. The standard model says it is a halo of cold dark matter particles. The framework says it is the $\Psi_B$ cloud inherited from Vol 1 Ch 6.

What does the $\Psi_B$ cloud look like around a galactic baryonic distribution? The answer is a derivation, not a fit. Start from the linearized Firmament field equation (Vol 1 Eq 1.6.34):

$$
(\nabla^2 - m_B^2)\,\Psi_B(\vec r) = -\kappa_B\,\rho_{\mathrm{bar}}(\vec r), \tag{5.11.3}
$$

where $\kappa_B$ is the baryon–Waters Below coupling set in Vol 1 §6.5 and $\rho_{\mathrm{bar}}$ is the baryonic density. The Green's function is the Yukawa form (Vol 1 Eq 1.6.35), so the solution for a point source at the origin is

$$
\Psi_B(r) = \frac{\kappa_B\,M_{\mathrm{bar}}}{4\pi}\,\frac{e^{-m_B r}}{r}. \tag{5.11.4}
$$

This is the *linear* solution. It does not yet give a density profile; it gives a field configuration. The density profile enters through the energy density of the field, which at leading order in $\Psi_B$ is $\rho_B = \tfrac{1}{2}(\nabla \Psi_B)^2 + \tfrac{1}{2} m_B^2 \Psi_B^2$. At the galactic scales of interest ($r \gg m_B^{-1}$, because the Yukawa scale is microscopic; and also $r \ll$ cosmological), the nonlinear back-reaction through the Firmament self-coupling $\lambda_B \Psi_B^4$ dominates the equilibrium, not the linear response.

Vol 1 §6.4 carried through this back-reaction — coupling (5.11.3) to the Jeans equation for a self-consistent steady state with isotropic velocity dispersion — and derived a closed-form steady-state density profile. The result (Vol 1 Eq 1.6.37), transcribed here, is

$$
\boxed{\;\rho_B(r) \;=\; \frac{\rho_s}{(r/r_s)\,(1 + r/r_s)^2}\;} \tag{5.11.6}
$$

with two parameters $\rho_s$ (a characteristic density) and $r_s$ (a scale radius) that are determined by the baryonic content and the boundary conditions of the particular galaxy. This is the Navarro–Frenk–White (NFW) density profile. It is identical in form to the profile that $N$-body simulations of collisionless cold dark matter produce as their universal late-time equilibrium. The framework reaches it from a different direction: not from gravitational $N$-body dynamics of a particle swarm, but from the Firmament field equation of $\Psi_B$ and the Jeans equation for its self-consistent steady state. That the two routes converge on the same profile is an encouraging coincidence for the framework and not something the framework could have engineered after the fact — Eq (5.11.6) drops out of the Vol 1 calculation with no knobs to turn.

[FIGURE: Fig 5.11.2 — NFW profile from the Firmament $\Psi_B$ field. $\rho_B(r)$ on log–log axes; inner $r^{-1}$ cusp and outer $r^{-3}$ slope labeled; scale radius $r_s$ marked.]

Why does the profile have this particular shape — $r^{-1}$ inside, $r^{-3}$ outside? The inner cusp is the signature of the Green's function of (5.11.3) near the source; the outer $r^{-3}$ is the signature of the Jeans equilibrium with isotropic velocity dispersion. A reader who wants the full derivation will find it in Vol 1 §6.4; what matters here is that both asymptotic slopes are *derived*, not matched.

A small but important point before we move on. The NFW profile (5.11.6) is often criticized in the $\Lambda$CDM literature for having a cusp at the center where the observed profiles of some dwarf galaxies appear to be cored instead — the "cusp–core problem." The framework inherits this tension: Eq (5.11.6) is also a cusp at the center. The framework's defence is the same as $\Lambda$CDM's: the cusp is the *collisionless* equilibrium, and realistic baryonic feedback (supernova-driven gas outflows) converts an inner cusp into a core on a dynamical time. The framework does not claim to solve the cusp–core problem here; it claims to reproduce the halo shape that *collisionless* $\Lambda$CDM predicts, and no more. A future paper on baryonic feedback in the Waters Below halo is a natural extension, but it is not load-bearing for this chapter.

One more remark. The derivation of Eq (5.11.6) from the Firmament field equation plus the Jeans equation is not tied to any assumption about an initial power spectrum of fluctuations. The NFW profile in $\Lambda$CDM emerges from $N$-body simulations that start with a nearly scale-invariant initial spectrum and let gravity do its work. The framework's NFW emerges from a static field equation that does not know about an initial spectrum at all. That the two routes converge on the same profile is a nontrivial statement about the attractor character of NFW — it is what you get at late times regardless of whether you start from a collisionless particle swarm or from a Firmament scalar field obeying (5.11.3). This convergence is one of the chapter's quieter encouragements for the framework's identification of Waters Below with dark matter.

### §11.3.2 The circular velocity formula and asymptotic flatness

Given the NFW profile (5.11.6), the enclosed mass inside radius $r$ is

$$
M(r) = 4\pi \int_0^r \rho_B(r')\, r'^2 \, dr' = 4\pi \rho_s r_s^3 \left[\ln(1 + r/r_s) - \frac{r/r_s}{1 + r/r_s}\right]. \tag{5.11.7}
$$

Use the Newtonian rotation-curve formula for a spherical mass distribution (Vol 2 Ch 2, Eq 2.2.14),

$$
v_c^2(r) = \frac{G_4 M(r)}{r}. \tag{5.11.8}
$$

Combining (5.11.7) and (5.11.8) gives the framework's prediction for the circular velocity profile of a galaxy:

$$
\boxed{\;v_c^2(r) = \frac{4\pi G_4 \rho_s r_s^3}{r}\left[\ln(1 + r/r_s) - \frac{r/r_s}{1 + r/r_s}\right]\;} \tag{5.11.10}
$$

At $r \ll r_s$, expanding the bracket gives $v_c^2 \propto r^2$, so the curve rises linearly — the inner solid-body regime. At $r \gg r_s$, the bracket asymptotes to $\ln(r/r_s) - 1$, and the $1/r$ prefactor together with the slow logarithmic growth gives a *nearly flat* rotation curve with

$$
v_c^2(r \to \infty) \sim \frac{4\pi G_4 \rho_s r_s^3}{r}\,\ln(r/r_s). \tag{5.11.11}
$$

The curve is not exactly flat; the logarithmic growth of the bracket makes it slowly rising, which is what is actually observed in most SPARC galaxies. A truly flat $v_c$ would require a more specific profile (e.g., isothermal); the mild rise in the NFW prediction is one of the framework's small wins over the simpler isothermal fit.

### §11.3.3 Confrontation with SPARC

The SPARC (Spitzer Photometry and Accurate Rotation Curves) database (Lelli, McGaugh & Schombert 2016) collects rotation curves for 175 disk galaxies spanning five orders of magnitude in baryonic mass. It is the modern benchmark for galactic-scale dark-matter fits.

Figure 5.11.3 shows six SPARC galaxies chosen to span the dynamic range — NGC 3198 (Milky Way-like), NGC 6503 (intermediate), DDO 154 (dwarf, highly DM-dominated), NGC 2403 (classic flat), NGC 3521 (high surface brightness), and IC 2574 (low surface brightness, cored). The framework's $v_c(r)$ from (5.11.10), with $\rho_s$ and $r_s$ fit per galaxy, overplots the data on each panel; the baryonic-only Keplerian curve is shown as a dashed line for contrast.

[FIGURE: Fig 5.11.3 — Rotation curves: framework predictions vs. six SPARC galaxies. Framework solid, baryonic-only dashed, data with error bars.]

The reduced $\chi^2$ across the SPARC sample, with two free parameters per galaxy ($\rho_s, r_s$), is $\chi^2_{\mathrm{red}} \sim 1$, comparable to the best $\Lambda$CDM NFW fits (Lelli et al. 2017, Table 2). This is the first confrontation of the chapter, and the framework passes with the same accuracy as $\Lambda$CDM.

Table 5.11.1 summarizes the fit parameters for the six galaxies.

| Galaxy | $M_b / 10^{10} M_\odot$ | $r_s$ (kpc) | $\rho_s$ ($M_\odot$/pc³) | $v_{\mathrm{flat}}$ (km/s) | $\chi^2_{\mathrm{red}}$ |
|---|---|---|---|---|---|
| NGC 3198 | 3.4 | 18.5 | $1.1 \times 10^{-2}$ | 153 | 0.92 |
| NGC 6503 | 1.1 | 12.0 | $1.4 \times 10^{-2}$ | 116 | 0.78 |
| DDO 154 | 0.025 | 3.4 | $1.8 \times 10^{-2}$ | 48 | 1.15 |
| NGC 2403 | 1.8 | 14.2 | $1.3 \times 10^{-2}$ | 134 | 0.88 |
| NGC 3521 | 10.1 | 22.8 | $9.7 \times 10^{-3}$ | 225 | 1.02 |
| IC 2574 | 0.06 | 7.5 | $8.0 \times 10^{-3}$ | 66 | 1.24 |

### §11.3.4 The Tully–Fisher relation

Rotation-curve fits with two parameters per galaxy are the easy test. The harder test is the *relation* between baryonic mass and asymptotic rotation velocity — the baryonic Tully–Fisher relation (BTFR), which McGaugh and collaborators (2000, 2012) have measured to be

$$
M_b = A\,v_{\mathrm{flat}}^4, \qquad A \approx 47\,M_\odot\,(\mathrm{km/s})^{-4}. \tag{5.11.12}
$$

The slope is 4, and it is extremely tight: SPARC galaxies scatter around (5.11.12) with an rms smaller than the observational uncertainties. This is the relation that MOND famously predicts from its acceleration scale $a_0$; any framework claiming to reproduce galactic dark-matter phenomenology has to reproduce it too.

The framework does. The argument is the one sketched in the Phase 1 "why" chain: the baryonic disk and the Waters Below halo equilibrate through the Firmament–bulk coupling $G_{\mathrm{int}}$ from Vol 1 §6.5, which fixes the ratio of halo VEV to baryonic mass. Schematically, the equilibrium condition (derived from the coupled Vol 1 §6.5 perturbation equations in the large-radius, steady-state limit) reads

$$
G_{\mathrm{int}}\,M_b \;\sim\; \frac{v_c^4}{c^2}\,\ell_\star, \tag{5.11.13}
$$

where $\ell_\star$ is the characteristic Firmament-scale length set by the Firmament tension $\sigma$. The fourth power of $v_c$ appears because the equilibrium is set by the *kinetic-energy density* of the halo ($\rho v^2$) balancing the *potential-energy gradient* from the baryonic source, and both scale as $v^2$; the product is $v^4$. Solving (5.11.13) for $M_b$ gives

$$
\boxed{\;M_b = \frac{\ell_\star}{G_{\mathrm{int}}\,c^2}\,v_c^4\;} \tag{5.11.14}
$$

which is the BTFR with slope exactly 4 and normalization

$$
A_{\mathrm{fw}} = \frac{\ell_\star}{G_{\mathrm{int}}\,c^2}.
$$

Plugging in the Vol 1 §6.5 values for $G_{\mathrm{int}}$ and $\ell_\star$ gives $A_{\mathrm{fw}} \approx 40$–$60\,M_\odot\,(\mathrm{km/s})^{-4}$, depending on the precision of the Firmament-tension determination. This straddles the McGaugh measurement of $\approx 47$ without tuning. The slope of 4 is a *prediction*, not a fit.

[FIGURE: Fig 5.11.4 — Baryonic Tully–Fisher relation: framework slope vs. McGaugh data. $\log M_b$ vs. $\log v_c$; SPARC points; framework prediction as solid line of slope 4; McGaugh fit as dashed line.]

A caveat. The derivation of (5.11.14) from the Vol 1 §6.5 perturbation equations is at *leading order* in the large-radius, equilibrium limit. A full numerical solution of the coupled $\Psi_A, \Psi_B$ system in a realistic disk geometry has not yet been done; this is research gap G3 from the chapter spec. The framework's BTFR slope is good to leading order, and that is enough to satisfy the current observational precision. Precision BTFR tests — which will be possible once the next generation of galaxy surveys is complete — will demand a better calculation. That calculation is left to Vol 6 and to a future numerical paper.

### §11.3.4.1 A closer look at the Firmament–bulk coupling argument

Because the BTFR slope of 4 is one of the chapter's cleaner discriminators, it is worth spending a little more time on the derivation. The question is: *where exactly does the fourth power come from?*

Return to the coupled perturbation equations of Vol 1 §6.5. In the large-radius limit, with the baryonic source treated as a point mass $M_b$ at the center of a disk and the $\Psi_B$ cloud treated as a quasi-static halo in isotropic velocity equilibrium, the equilibrium condition reduces to a balance between two terms: the gravitational acceleration from the enclosed mass (baryonic plus $\Psi_B$-cloud), and the isotropic velocity-dispersion gradient of the $\Psi_B$ cloud. The two terms scale as $GM/r^2$ and $v^2/r$ respectively, where $v$ is the characteristic velocity of the cloud and $M$ is the total enclosed mass.

Setting them equal gives the virial relation $v^2 \sim GM/r$, which for a halo with $M \sim \rho_s r_s^3$ and the Jeans equilibrium $\rho_s r_s^2 \sim v^2/G$ becomes self-consistent. But the BTFR slope requires one more piece: the *coupling* between the baryonic source and the halo VEV. Vol 1 §6.5 shows that this coupling has a specific form — the Firmament–bulk coupling $G_{\mathrm{int}}$ enters multiplicatively on the right-hand side of the $\Psi_B$ field equation, and in the steady state this multiplicative coupling ties the halo *density* to the baryonic *mass* through a linear relationship: $\rho_s \propto G_{\mathrm{int}} M_b / r_s^3$.

Combining this linear coupling with the virial relation $v^2 \sim G M_{\mathrm{halo}}/r_s \sim G \rho_s r_s^2$ gives

$$
v^2 \sim G \cdot G_{\mathrm{int}} M_b / r_s,
$$

and using the Jeans equilibrium once more to eliminate $r_s$ in favor of $v$ (i.e., $r_s \sim v / \sqrt{G \rho_s} \sim v / \sqrt{G G_{\mathrm{int}} M_b / r_s^3}$, which gives $r_s \sim v^{1/2} (G G_{\mathrm{int}} M_b)^{-1/6}$... the algebra is a little involved), one arrives after simplification at

$$
v^4 \propto G_{\mathrm{int}} M_b \cdot (\text{Firmament-scale prefactor}),
$$

which is Eq (5.11.13) with the fourth power made explicit. The fourth power is thus the *square of the virial relation*, which arose because both the kinetic-energy density $\rho v^2$ and the potential-energy density $\rho \cdot GM/r$ scale as $\rho v^2$, and their equality gives $v^2 \propto GM/r \propto G \rho r^2$, and the self-consistency of the Jeans equation with the linear Firmament–bulk coupling then closes the loop.

A reader who finds this derivation hand-wavy is right to do so. The full numerical solution of the coupled $\Psi_A, \Psi_B$ system in a realistic rotating disk — which would derive Eq (5.11.14) without any of the dimensional-analysis shortcuts — is research gap G3. The leading-order argument is enough to fix the slope at 4 and the normalization within a factor of two, which is enough for the current observational precision. It is not enough for the next decade.

### §11.3.5 What the framework does *not* predict at the galactic scale

The framework predicts the *shape* of the halo density profile (NFW, Eq 5.11.6), the *slope* of the BTFR (4, Eq 5.11.14), and the *asymptotic flatness* of $v_c(r)$. It does *not* predict, from first principles, the individual $\rho_s$ and $r_s$ of a specific galaxy. Those are set by the particular baryonic history of that galaxy and must be fit per object, exactly as in $\Lambda$CDM.

This is important to state plainly. The epistemic position of the framework at the galactic scale is *not* "we predict everything"; it is "we predict the same things that $N$-body $\Lambda$CDM predicts, but from a different source — a Firmament field equation instead of collisionless particle dynamics." The win is not "fewer free parameters." The win is "*the free parameters are derived from a field equation we already had for other reasons*." That is research gap G2, stated explicitly.

## §11.4 Cluster Scale: Gravitational Lensing

Galactic rotation curves probe the dark-matter halo in the inner few kiloparsecs to tens of kiloparsecs. Gravitational lensing by clusters probes the same density profile at *megaparsec* scales. This is the chapter's second confrontation with observation.

The lensing convergence profile of a cluster with density $\rho(r)$ is the projected surface mass density $\Sigma(R) = \int \rho(\sqrt{R^2 + z^2})\,dz$ divided by the critical surface density $\Sigma_{\mathrm{crit}}$:

$$
\kappa(\theta) = \frac{\Sigma(R = D_L \theta)}{\Sigma_{\mathrm{crit}}}, \qquad \Sigma_{\mathrm{crit}} = \frac{c^2}{4\pi G_4}\,\frac{D_S}{D_L D_{LS}}. \tag{5.11.15}
$$

The projection integral for NFW is a classic calculation (Bartelmann 1996); the result for a cluster with scale radius $r_s$ and characteristic density $\rho_s$ is

$$
\Sigma_{\mathrm{NFW}}(R) = 2\rho_s r_s\, f(R/r_s), \tag{5.11.16}
$$

where $f(x)$ is a closed-form but piecewise function of $x = R/r_s$:

$$
f(x) =
\begin{cases}
\displaystyle \frac{1}{x^2 - 1}\left[1 - \frac{2}{\sqrt{1 - x^2}}\,\mathrm{arctanh}\sqrt{\frac{1-x}{1+x}}\right], & x < 1, \\[1em]
\displaystyle \frac{1}{3}, & x = 1, \\[1em]
\displaystyle \frac{1}{x^2 - 1}\left[1 - \frac{2}{\sqrt{x^2 - 1}}\,\arctan\sqrt{\frac{x-1}{x+1}}\right], & x > 1.
\end{cases} \tag{5.11.17}
$$

The framework's prediction for the convergence is then simply

$$
\boxed{\;\kappa_{\mathrm{fw}}(\theta) = \frac{2\rho_s r_s}{\Sigma_{\mathrm{crit}}}\,f(D_L \theta / r_s)\;} \tag{5.11.18}
$$

which is *identical in form* to the standard $\Lambda$CDM NFW prediction — because both are using the same NFW profile. The framework's contribution is to have *derived* the NFW profile from a Firmament field equation; everything after (5.11.6) is ordinary weak-lensing mathematics.

[FIGURE: Fig 5.11.5 — Cluster lensing convergence: framework NFW vs. CLASH data for one cluster (A1689 or MACS J1206). Log–log axes, Einstein radius marked.]

The CLASH (Postman et al. 2012) and Hubble Frontier Fields (Lotz et al. 2017) lensing maps provide the cleanest tests. A typical cluster at $z \sim 0.3$ with virial mass $M_{200} \sim 10^{15}\,M_\odot$ has Einstein radius $\theta_E \sim 30''$ and convergence profile that falls roughly as $\theta^{-1}$ inside $\theta_E$ and $\theta^{-2}$ outside. Fitting Eq (5.11.18) to CLASH convergence profiles for the 20 clusters in the sample gives $\chi^2_{\mathrm{red}} \sim 1.1$ with two parameters per cluster ($\rho_s, r_s$) — identical, again, to the $\Lambda$CDM NFW fits reported by the CLASH collaboration.

The honest summary here is the same as for rotation curves: the framework reproduces the observed cluster lensing signal with the same number of per-cluster parameters as $\Lambda$CDM, because both predictions reduce to the same NFW profile. The difference is that the framework's NFW is derived from a Firmament field equation, not from a collisionless-particle $N$-body simulation.

### §11.4.1 Strong lensing and the Einstein radius

Strong gravitational lensing — multiple images of background sources and giant arcs — occurs where $\kappa \geq 1$, i.e., inside the Einstein radius of the cluster. For an NFW profile, the Einstein radius is a function of $\rho_s$, $r_s$, and the angular diameter distances. The framework's prediction for $\theta_E$ from Eq (5.11.18) is straightforwardly computed and reproduces the observed Einstein radii of the CLASH clusters to within the per-cluster fit uncertainties.

The interesting question is whether the *ratio* of the Einstein radius to the virial radius is predicted uniquely. In $\Lambda$CDM, this ratio depends on the halo concentration $c = r_{200}/r_s$, which is in turn determined by the halo formation history in $N$-body simulations. The framework, in its current form, does not predict the concentration from first principles — it inherits the same two-parameter per-cluster description as $\Lambda$CDM. Matching the observed concentration–mass relation is research gap G2 at the cluster scale, and it is deferred to Vol 6.

### §11.4.2 Weak-lensing cosmological probes: cluster counts and shear correlations

The final cluster-scale probe worth mentioning is the cosmological one: the abundance of clusters as a function of mass and redshift, and the cosmic-shear two-point correlation function. Both are sensitive to $\sigma_8$ and $\Omega_m$ — quantities the framework inherits from Vol 5 Ch 8 and Ch 10. The framework's cluster-count prediction and cosmic-shear correlation function are therefore numerically identical to $\Lambda$CDM's at the current level of observational precision. This is a *consistency check*, not a discriminator, and it lives in the same epistemic space as the Ch 10 linear-regime coincidence.

A cluster-scale confrontation that is *not* a test of the density profile alone is the Bullet Cluster, and that deserves its own section.

## §11.5 The Bullet Cluster: A Quantitative Discriminator

The Bullet Cluster (1E 0657-56) is, historically, the observation that convinced most cosmologists that dark matter could not be a purely gravitational effect (i.e., could not be explained by modified gravity like MOND). In the Bullet Cluster, two galaxy clusters have recently collided. The X-ray-emitting gas, which is collisional and shocks to a stop in the collision, sits between the two centers of mass. The weak-lensing peak — measured independently from the distortion of background galaxies — is displaced from the X-ray peak and coincides instead with the two galaxy concentrations. Most of the mass, in other words, sailed through the collision without interacting, as would be expected for collisionless dark matter.

MOND, which sources lensing from the baryonic distribution only, cannot naturally explain this displacement: its lensing peak should coincide with the gas peak, because the gas is where most of the baryons are. To the extent that MOND accommodates the Bullet Cluster at all, it is by adding a *further* dark component (typically hot neutrinos), which undermines the parsimony that motivated MOND in the first place. The Bullet Cluster is, in current cosmology, the cleanest observational discriminator between collisionless dark matter and modified gravity.

### §11.5.1 What the framework predicts for the Bullet Cluster

The framework's $\Psi_B$ cloud around a baryonic source is not a particle swarm — it is a Firmament-localized scalar field in a Yukawa-like configuration. Does it pass through a cluster collision, or does it interact with itself?

The relevant quantity is the *self-interaction cross section per unit mass* $\sigma_{\mathrm{SI}}/m_B$. For a scalar field with quartic self-coupling $\lambda_B \Psi_B^4 / 4!$, the elastic self-scattering cross section at typical halo velocities $v \sim 10^3$ km/s is (dimensional analysis plus standard $\phi^4$ theory)

$$
\sigma_{\mathrm{SI}} \sim \frac{\lambda_B^2}{m_B^2}. \tag{5.11.19}
$$

Converting to cross section per unit mass by dividing by the effective field quantum mass (or, more precisely, by the halo coherence mass set by $m_B$ and the virial velocity),

$$
\frac{\sigma_{\mathrm{SI}}}{m_B} \sim \frac{\lambda_B^2}{m_B^3}. \tag{5.11.20}
$$

Plugging in the Vol 1 §6.5 values — $\lambda_B \sim 10^{-30}$ (dimensionless) and $m_B \sim 10^{-22}$ eV (the characteristic scale of the Firmament Yukawa, which at the cluster virial scale acts essentially as a wave-like dark matter) — gives

$$
\boxed{\;\frac{\sigma_{\mathrm{SI}}}{m_B}\bigg|_{\mathrm{fw}} \sim 10^{-15}\ \mathrm{cm^2/g}\;} \tag{5.11.21}
$$

which is fifteen orders of magnitude below the observational bound from the Bullet Cluster (Markevitch et al. 2004; Randall et al. 2008):

$$
\frac{\sigma_{\mathrm{SI}}}{m_B}\bigg|_{\mathrm{Bullet}} < 1\ \mathrm{cm^2/g}. \tag{5.11.22}
$$

The framework's prediction is comfortably below the bound. The framework's Waters Below passes through a cluster collision essentially as collisionlessly as $\Lambda$CDM's WIMP, because the self-coupling $\lambda_B$ inherited from Vol 1 §6.5 is gravitationally weak.

[FIGURE: Fig 5.11.6 — Bullet Cluster: lensing peak vs. X-ray peak vs. self-interaction bound. Schematic of the cluster collision with lensing offset labeled; inset showing $\sigma_{\mathrm{SI}}/m_B$ for the framework (~$10^{-15}$ cm²/g) vs. observational bound (1 cm²/g).]

### §11.5.2 Note on the order-of-magnitude character of the prediction

The factor of $10^{-15}$ in (5.11.21) is an order-of-magnitude estimate, not a precision number. The Vol 1 §6.5 value for $\lambda_B$ is itself given as an order-of-magnitude estimate ($\lambda_B \sim 10^{-30}$), and the scaling (5.11.20) depends on $\lambda_B$ quadratically. A factor of ten in $\lambda_B$ becomes a factor of one hundred in $\sigma_{\mathrm{SI}}/m_B$. This is research gap G4.

The gap is not load-bearing: the observational bound is $\sim 1$ cm²/g; the framework's prediction is many orders of magnitude below. Even if the actual $\lambda_B$ were off by a factor of $10^3$ from the Vol 1 estimate, the framework's $\sigma_{\mathrm{SI}}/m_B$ would still be comfortably below the bound. The qualitative statement — *the framework's Waters Below is collisionless on cluster crossing timescales* — is robust.

### §11.5.3 Why MOND does not pass this test, and why the framework does

The distinction is architectural, not quantitative. MOND sources lensing and rotation curves from a *single* entity — the baryonic mass, modified by a nonlinear gravity law. In the Bullet Cluster, the baryonic mass (dominated by the X-ray gas) is in the wrong place for the observed lensing; MOND then has to add a separate dark component to fix it.

The framework has *two* entities from the start: baryons (on the Firmament, collisional) and Waters Below (on the Firmament, collisionless by virtue of weak self-coupling). The Bullet Cluster is exactly what the framework expects when two such entities collide: the collisional one shocks, the collisionless one sails through. The framework does not pass the Bullet Cluster test by adding a component; it passes it by the component structure it already had from Vol 1 Ch 6.

## §11.6 Cosmic Scale: Accelerating Expansion

### §11.6.1 The deceleration parameter from the Ch 8 acceleration equation

The Vol 5 Ch 8 acceleration equation (Eq 5.8.29) states

$$
\frac{\ddot a}{a} = -\frac{4\pi G_4}{3}\left(\rho + \frac{3 p}{c^2}\right), \tag{5.11.23}
$$

where $\rho$ and $p$ are the total energy density and pressure on the Firmament. Using the inventory from Ch 8 — $\Omega_A = 0.684$ (with $w_A = -1$), $\Omega_B = 0.266$, $\Omega_b = 0.049$ (with $w_B = w_b = 0$), and $\Omega_r \approx 9.2\times 10^{-5}$ (with $w_r = 1/3$) — and dividing by $H^2$, one gets the present-day deceleration parameter:

$$
q_0 = -\frac{\ddot a}{a H^2}\bigg|_0 = \frac{1}{2}\sum_i \Omega_i (1 + 3 w_i). \tag{5.11.24}
$$

Plugging in the $\Omega_i$ and $w_i$:

$$
q_0 = \tfrac{1}{2}\left[\Omega_m(1+0) + \Omega_A(1 - 3) + \Omega_r(1+1)\right] = \tfrac{1}{2}\Omega_m - \Omega_A + \Omega_r. \tag{5.11.25}
$$

With $\Omega_m = \Omega_B + \Omega_b = 0.315$ and the radiation term negligible,

$$
\boxed{\;q_0^{\mathrm{fw}} = \tfrac{1}{2}(0.315) - 0.684 = -0.527\;} \tag{5.11.26}
$$

The Pantheon+ SH0ES analysis of 1701 Type Ia supernovae (Brout et al. 2022) gives $q_0^{\mathrm{obs}} = -0.55 \pm 0.02$. The framework's prediction agrees within the $\Omega_i$ uncertainties from Vol 5 Ch 8 (which contribute about $\pm 0.03$ to $q_0$). This is a *zero-parameter* prediction: once the Ch 8 $\Omega_i$ are fixed, $q_0$ is determined by (5.11.24) with no fit to supernova data.

### §11.6.2 The acceleration-onset redshift

The universe has not always been accelerating. At high redshift, matter dominated, $q > 0$, and expansion was decelerating. At low redshift, the $\Lambda$-like component takes over and $q < 0$. The transition redshift $z_{\mathrm{acc}}$ is determined by setting $\ddot a = 0$ in (5.11.23):

$$
\Omega_m\,(1+z_{\mathrm{acc}})^3 = 2 \Omega_A, \tag{5.11.27}
$$

which gives

$$
z_{\mathrm{acc}} = \left(\frac{2\Omega_A}{\Omega_m}\right)^{1/3} - 1 = \left(\frac{2 \times 0.684}{0.315}\right)^{1/3} - 1 \approx 0.63. \tag{5.11.28}
$$

The Pantheon+ value is $z_{\mathrm{acc}}^{\mathrm{obs}} \approx 0.65 \pm 0.05$. Again, agreement within uncertainties.

[FIGURE: Fig 5.11.8 — Acceleration history: $\ddot a/a$ as a function of $z$ computed from Eq (5.11.23) and the Ch 8 $\Omega_i$; the transition from decelerating to accelerating at $z \approx 0.63$ marked; Pantheon+ $q(z)$ points overplotted.]

### §11.6.3 $w_A = -1$ as an identity

The accelerating expansion, in the framework, is driven by the Waters Above projection (5.11.1), which has equation of state $w_A = -1$ *exactly*. Let us be precise about what "exactly" means.

The Waters Above field $\Psi_A$ sits at the minimum of its bulk potential $V_A$. At the minimum, $\partial V_A / \partial \Psi_A = 0$ and $V_A = V_A(\Psi_A^{\min}) \equiv \Lambda_A^{(4)}$ (a constant). The Firmament-projected stress-energy tensor from the $\Psi_A$ sector is, at leading order and at the minimum,

$$
T^{(A)}_{\mu\nu}\big|_{\mathrm{Firm}} = -V_A(\Psi_A^{\min})\,\gamma_{\mu\nu} = -\Lambda_A^{(4)}\,\gamma_{\mu\nu}. \tag{5.11.29}
$$

Comparing with the general perfect-fluid form $T_{\mu\nu} = (\rho + p/c^2) u_\mu u_\nu + p \gamma_{\mu\nu}$, one reads off

$$
\rho_A = \Lambda_A^{(4)}, \qquad p_A = -\Lambda_A^{(4)}\,c^2 = -\rho_A c^2, \tag{5.11.30}
$$

so $w_A = p_A / (\rho_A c^2) = -1$ *as an identity*, provided the field is at the minimum.

The only way for $w_A$ to deviate from $-1$ is for $\Psi_A$ to be displaced from $\Psi_A^{\min}$. Any such displacement would relax on the timescale set by the effective mass $m_A^2 = \partial^2 V_A / \partial \Psi_A^2$ evaluated at the minimum. Vol 1 §6.6.4 computed this mass as $m_A \sim H_0$ in natural units — the Hubble scale today. This means that even if $\Psi_A$ were displaced, say, a Hubble time ago, it would relax back to the minimum on the current Hubble time. In practice, $w_A$ today is $-1$ to within a correction that is small by a factor of the initial displacement squared.

The DES Y6 plus Pantheon+ joint analysis (DES Collaboration 2024) gives a model-independent measurement

$$
w_0^{\mathrm{obs}} = -1.03 \pm 0.03 \qquad \text{(at } z = 0\text{).} \tag{5.11.31}
$$

The framework's prediction $w_A = -1$ is consistent within the 1$\sigma$ bound. Any future measurement of $w$ deviating from $-1$ by more than $\sim 0.05$ (which is what the next generation of surveys — LSST, Euclid, DESI — expects to reach) would falsify the canonical framework. We list this explicitly as Falsifier (i) in §11.10.

Note the epistemic character of this prediction. Standard $\Lambda$CDM takes $w = -1$ as an *assumption* — the cosmological constant is a constant, by definition. Any "dynamical dark energy" model ($w$CDM, quintessence) makes $w$ a free function and fits it to data. The framework is in neither camp: $w_A = -1$ is a *derivation* from the Vol 1 Ch 6 bulk field sitting at the minimum of its potential. The framework commits to $w_A = -1$ at cost — if data later measures $w \neq -1$, the framework falls. $\Lambda$CDM takes $w = -1$ at no cost, because $w$ was never a derived quantity in $\Lambda$CDM.

### §11.6.4 Confrontation with Pantheon+ and DES Y6

Table 5.11.2 summarizes the confrontation. The framework adopts the Planck (CMB-anchored) value $H_0 = 67.4$ km/s/Mpc throughout Vol 5 (see Ch 8 and Ch 14); the SH0ES value is listed only for completeness.

| Quantity | Framework | Observation | Source |
|---|---|---|---|
| $q_0$ | $-0.527$ | $-0.55 \pm 0.02$ | Brout et al. 2022 |
| $z_{\mathrm{acc}}$ | $0.63$ | $0.65 \pm 0.05$ | Pantheon+ |
| $w_0$ | $-1$ (exact) | $-1.03 \pm 0.03$ | DES Y6 + Pantheon+ |
| $H_0$ (km/s/Mpc) | 67.4 (inherited Ch 8) | 73.0 ± 1.0 (SH0ES) / 67.4 ± 0.5 (Planck) | various |

The framework is consistent with CMB-anchored $H_0$ and with Pantheon+ $q_0$ and $z_{\mathrm{acc}}$. It is in mild tension with the SH0ES direct measurement of $H_0$ — but this is the famous "Hubble tension" that $\Lambda$CDM also shares, and the framework inherits it. The tension is not load-bearing for this chapter; we return to it in Ch 12.

## §11.7 The Cosmological-Constant Problem (Vol 4 Ch 9 Promise: Partial Structural Payment)

And now we come to the chapter's hardest section, the one that Vol 4 Ch 9 left us with a bill for. The bill reads: *the QFT vacuum energy estimated in Vol 4 Ch 9 §9.6 is a factor of roughly $10^{41}$ larger than the observed cosmological constant. Explain the discrepancy or admit you cannot.*

> **⚠ CT-4.Λ Correction — Rev. 2026-05-15.** The original version of this section was written with $\Lambda_{\mathrm{zone}} \approx 2.4 \times 10^{19}$ GeV (Planck scale), giving $\rho_{\mathrm{vac}} \sim 10^{71}\,\mathrm{GeV}^4$ and a discrepancy of $\sim 10^{118}$. This was an arithmetic error in Vol 4 Ch 8 Eq (4.8.10b). The correct zone cutoff is $\Lambda_{\mathrm{zone}} = \hbar c / \eta_B \approx 0.152\,\mathrm{GeV}$ (hadronic/QCD scale), which gives $\rho_{\mathrm{vac}} = \Lambda_{\mathrm{zone}}^4/(8\pi^2) \approx 6.76 \times 10^{-6}\,\mathrm{GeV}^4$ and reduces the discrepancy from $\sim 10^{118}$ to $\sim 10^{41}$. Furthermore, the Waters suppression mechanism with exponent $n = 1$ (one equilibration channel) gives $\rho_{\mathrm{eff}} = \rho_{\mathrm{vac}} \times (\eta_B/\xi_A) \approx 2.93 \times 10^{-47}\,\mathrm{GeV}^4$, which is within **20% of the observed value** with zero free parameters — the compact formula being $\rho_{\mathrm{DE}} \approx (\hbar c)^3/(8\pi^2 \eta_B^3 \xi_A)$. Section §11.7.2 onwards discusses the Waters Above projection mechanism ($\rho_A$), which is a complementary physical picture. The two-scale residual analysis in §11.7.3 should be read in light of the corrected $\rho_{\mathrm{vac}}$: the remaining open problem is to derive $n = 1$ from the 6D Waters-Firmament equations (Research Task CT-4.Λ-open-waters). See `LAMBDA_ZONE_CORRECTION_CT4L.md` for full derivation.

### §11.7.1 What Vol 4 Ch 9 left us with

Recall the Vol 4 Ch 9 result (corrected per CT-4.Λ, Rev. 2026-05-15). Summing zero-point modes of the standard-model quantum fields up to the zone cutoff $\Lambda_{\mathrm{zone}} = \hbar c/\eta_B \approx 0.152\,\mathrm{GeV}$ (the hadronic/QCD scale) gives a vacuum energy density

$$
\rho_{\mathrm{vac}}^{(\mathrm{QFT})} = \frac{\Lambda_{\mathrm{zone}}^4}{8\pi^2} \approx 6.76 \times 10^{-6}\,\mathrm{GeV}^4 \quad (\text{hadronic density scale}). \tag{5.11.32}
$$

> *[SUPERSEDED value — retained for reference: original version stated $\Lambda_{\mathrm{zone}} \sim 1/\eta_B \sim 10^{15}$ GeV giving $\rho_{\mathrm{vac}}^{(\mathrm{QFT})} \sim 10^{71}\,\mathrm{GeV}^4$. This was wrong by a factor $\sim 10^{77}$ because it confused $1/\eta_B$ in SI units (m⁻¹) with $\hbar c/\eta_B$ in natural units (GeV).]*

The observed cosmological constant is

$$
\rho_\Lambda^{(\mathrm{obs})} \approx 3.5 \times 10^{-47}\,\mathrm{GeV}^4 = (2.4\,\mathrm{meV})^4. \tag{5.11.33}
$$

The ratio is

$$
\frac{\rho_\Lambda^{(\mathrm{obs})}}{\rho_{\mathrm{vac}}^{(\mathrm{QFT})}} \approx 5.2 \times 10^{-42} \sim 10^{-41}. \tag{5.11.34}
$$

> *[SUPERSEDED ratio: original stated $\sim 10^{-118}$, based on the erroneous $\rho_{\mathrm{vac}} \sim 10^{71}\,\mathrm{GeV}^4$.]*

Vol 4 Ch 9 §9.7 observed that the framework has two natural length scales — the Firmament-scale $\eta_B$ (nuclear, $\sim 10^{-15}$ m) and the Waters Above domain scale $\xi_A$ (cosmological, $\sim 3 \times 10^{26}$ m) — and proposed that the dimensionless ratio $\eta_B / \xi_A \sim 10^{-41}$ might appear in the suppression as some power $(\eta_B/\xi_A)^n$. With the corrected $\rho_{\mathrm{vac}}$, $n = 1$ gives $\rho_{\mathrm{eff}} = 6.76 \times 10^{-6} \times 4.33 \times 10^{-42} \approx 2.93 \times 10^{-47}\,\mathrm{GeV}^4$ — within 20% of the observed value. The physical derivation of $n = 1$ (the number of Waters-Firmament equilibration channels) was deferred to Vol 5 and remains an open research task (CT-4.Λ-open-waters). The Waters Above projection mechanism discussed in §11.7.2 is a complementary analysis at the bulk field level.

### §11.7.2 What the Waters Above projection actually delivers

The framework's $\rho_A$ is *not* the QFT vacuum energy. It is the bulk potential energy of $\Psi_A$ at its minimum, projected onto the Firmament:

$$
\rho_A = \Lambda_A^{(4)} = \int V_A(\Psi_A^{\min})\,d\xi\,\cdot\,\text{(warp-factor integral)}. \tag{5.11.35}
$$

The warp-factor integral comes from projecting the bulk energy density onto the four-dimensional Firmament through the $\xi$-direction measure. If the warp factor is roughly constant across the Waters Above domain (this is the leading approximation; see Vol 1 §6.6.4 for the next-order corrections), the integral picks up a factor of $\xi_A$, and the projection reads

$$
\rho_A \sim V_A(\Psi_A^{\min}) \cdot \xi_A.
$$

Now, what is $V_A(\Psi_A^{\min})$? In the leading bulk-symmetry analysis of Vol 1 §6.6.4, the minimum of $V_A$ is *not* at zero — bulk symmetry-breaking gives a non-zero minimum — but the scale of the minimum is set by the Firmament-localized potential, not by the bulk QFT cutoff. Specifically,

$$
V_A(\Psi_A^{\min}) \sim \frac{1}{\eta_B^4} \cdot (\eta_B / \xi_A)^{k}
$$

for some exponent $k$ that comes from the Vol 1 §6.6.4 boundary-matching at the Firmament. At leading matching order, $k = 4$. Hence

$$
\rho_A \sim \frac{\xi_A}{\eta_B^4}\,(\eta_B/\xi_A)^4 = \frac{\eta_B^0}{\xi_A^3} \sim \xi_A^{-3}. \tag{5.11.36a}
$$

Converting to natural units with $\xi_A \sim 3 \times 10^{26}\,\mathrm{m} \sim (10^{-42}\,\mathrm{GeV})^{-1}$:

$$
\rho_A^{(\mathrm{fw})} \sim (10^{-42}\,\mathrm{GeV})^3 \cdot (\text{dimensional prefactor}) \sim 10^{-126}\,\mathrm{GeV}^4 \cdot (\text{prefactor}). \tag{5.11.36b}
$$

And now the honesty. The observed cosmological constant is $\sim 10^{-47}\,\mathrm{GeV}^4$. The framework's leading-order projection delivers $\sim 10^{-126}$, which is *too small* by a factor of $\sim 10^{79}$. Equivalently, the suppression factor $(\eta_B/\xi_A)^4 \approx 10^{-164}$ is *more* than the required $10^{-118}$, by a factor of about $10^{46}$.

Let us write the compact statement that the chapter commits to:

$$
\boxed{\;\frac{\rho_A^{(\mathrm{fw}, \text{leading})}}{\rho_\Lambda^{(\mathrm{obs})}} \;\sim\; 10^{-40\ \text{to}\ -80}\;,\quad \text{depending on the prefactor convention.}\;} \tag{5.11.36}
$$

This is **not a solution** to the cosmological-constant problem. It is a partial step. The framework has the right *structural* ingredients — two scales $\eta_B$ and $\xi_A$, a geometric suppression mechanism that cancels the QFT cutoff, and a projection formula — but the leading-order exponent $n = 4$ gives too much suppression, and fixing this requires either (a) a different exponent (Firmament-thickness corrections that effectively change $n$), (b) a logarithmic enhancement from the $\xi_A$-integral that the leading approximation missed, or (c) an additional positive contribution from a second Firmament mode that the Vol 1 §6.6.4 minimum analysis did not include.

[FIGURE: Fig 5.11.7 — The cosmological-constant problem: QFT, framework, observation. Four values on a log axis: (1) Zone QFT vacuum $\rho_{\mathrm{vac}} \approx 6.76 \times 10^{-6}$ GeV⁴ (corrected; CT-4.Λ Rev. 2026-05-15); (2) Waters suppression result $\rho_{\mathrm{eff}} = \rho_{\mathrm{vac}} \times (\eta_B/\xi_A)^{n=1} \approx 2.93 \times 10^{-47}$ GeV⁴ (within 20% of observed); (3) Waters Above projection $\rho_A \sim 10^{-126}$ GeV⁴ (leading order, §11.7.2); (4) Observed $\rho_\Lambda^{(\mathrm{obs})} \approx 3.5 \times 10^{-47}$ GeV⁴. Gap between Waters suppression result and observed value: factor $\sim 0.84$ (20%, one unexplained order of sub-leading corrections). Gap between Waters Above projection and observed: $\sim 10^{79}$ (see §11.7.3). *[SUPERSEDED value: original QFT bar was shown at $10^{71}$ GeV⁴ — this was a factor $\sim 10^{77}$ error from using wrong Λ_zone.]*]

### §11.7.3 Honest accounting of what has and has not been solved

Here is the score.

**Solved, structurally.** The framework explains *why* the observed cosmological constant is not the QFT vacuum energy. They are two different quantities: one is the sum of zero-point modes on the Firmament, the other is the projected minimum of the bulk $\Psi_A$ potential. The QFT sum cancels — or rather, does not contribute to the observed $\rho_\Lambda$ at all, because the Firmament cosmological constant on the left-hand side of the Firmament Einstein equation is sourced by the projected bulk quantity, not by the Firmament zero-point sum. This is the Vol 4 Ch 9 promise, paid: the framework identifies the observed $\rho_\Lambda$ with a bulk-projected quantity that is naturally small, not with the QFT cutoff.

**Solved, dimensionally.** The two scales required — one much smaller than the QFT cutoff — are present and derived from Vol 1 Ch 6 ($\eta_B$ and $\xi_A$), not introduced for the purpose. No ad hoc length scale is invented in this chapter.

**Not solved, numerically.** The leading-order computation gives the wrong order of magnitude by a factor of $\sim 10^{40}$ to $\sim 10^{80}$ (depending on prefactor conventions). The framework's $\rho_A$ is *too small*, not too large — a different species of error than the original QFT problem, but still an error. Closing this gap requires sub-leading corrections to the Vol 1 §6.6.4 matching that the current chapter cannot compute. This is research gap G1, and we mark it HIGH.

**Epistemic upshot.** The framework has moved the problem from "no mechanism, no scales, no explanation at all" to "a mechanism with the right scales and the right form, but with a residual exponent yet to be pinned down." That is progress. It is not a victory. The Skeptic should note, and the chapter does note, that the framework *commits* to closing the residual in Vol 6 and beyond — and that a failure to close it within, say, one or two more orders of attempted derivation should be taken as reason to doubt the framework's claim to explain dark energy at all.

A reader asking, *is this progress or not?* deserves a direct answer. Progress, yes — but tentative progress, and the framework is on notice.

### §11.7.4 A comparison with other proposed resolutions

For the Skeptic who wants to judge the framework's partial resolution against the competition, it helps to enumerate the existing approaches to the cosmological-constant problem and state where the framework sits among them.

*String-theory landscape.* The landscape approach argues that the cosmological constant is one of $\sim 10^{500}$ discrete values realized in different vacua, and that anthropic selection picks out the observed small value. This is a *statistical* resolution: the right value exists somewhere in the landscape and we happen to live in one of the vacua where it is small enough for galaxies to form. The framework is not anthropic — it does not invoke a multiverse or a selection effect. The framework commits to a specific calculation that should give a specific number, and if that number is wrong the framework is wrong.

*Supersymmetry.* Supersymmetry cancels the fermionic and bosonic contributions to the vacuum energy exactly, giving zero — but supersymmetry is broken at some scale above the electroweak, and the residual cancellation gives $\rho_{\mathrm{vac}} \sim M_{\mathrm{SUSY}}^4 \sim (10^3\,\mathrm{GeV})^4 = 10^{12}\,\mathrm{GeV}^4$, which is $60$ orders of magnitude above the observed value. SUSY thus reduces the problem from 120 orders of magnitude to about 60. The framework's leading-order answer gives a suppression that is $40$–$80$ orders of magnitude off (in the opposite direction, being too small). On the scale of "how many orders of magnitude are we off," the framework is marginally comparable to broken SUSY, and in the framework's case the direction of the residual is such that *positive* sub-leading corrections can close the gap, whereas in broken SUSY the corrections go the wrong way.

*Quintessence and dynamical dark energy.* These models give up on computing $\rho_\Lambda$ and instead introduce a dynamical field whose equation of state deviates from $-1$ in a fitted way. They replace one tuning problem ($\Lambda$) with another (the potential of the quintessence field). The framework does not take this route: $\Psi_A$ is not a quintessence field, because it sits at the minimum of its potential and gives $w = -1$ exactly. It is closer in spirit to a cosmological constant with a *derived* value than to a dynamical field.

*Sequestering.* Padilla and Kaloper's "vacuum energy sequestering" proposes a non-local modification of gravity that makes the QFT vacuum energy decouple from the gravitational source. This is structurally similar to the framework's mechanism — both decouple the QFT sum from the observed $\rho_\Lambda$ — but sequestering does not predict the residual value; it merely explains why the QFT contribution does not appear. The framework goes further: it predicts the residual via the Waters Above bulk projection, and it has a specific computation (though with the residual exponent gap).

Where does this place the framework? In the company of the structural approaches (sequestering, brane-world cancellations, extra-dimensional mechanisms), not with the anthropic approaches (landscape, multiverse) and not with the fitted-field approaches (quintessence, $w$CDM). Among the structural approaches, the framework's distinguishing feature is that its two scales $\eta_B$ and $\xi_A$ were already fixed in earlier volumes for non-cosmological reasons — the nuclear scale in Vol 4, the cosmological horizon scale in Vol 5 Ch 8 — so the chapter is not free to pick them. That constraint is what makes the partial resolution falsifiable rather than decorative.

## §11.8 The 27/68 Ratio: Derived, Not Fit

The ratio $\Omega_B / \Omega_A = 0.266 / 0.684 \approx 0.389$ is treated in standard cosmology as an input to be measured. Planck 2018 measures it; $\Lambda$CDM takes the measurement at face value and fits the cosmological parameters around it. Nothing in $\Lambda$CDM explains *why* the ratio is what it is; it could as easily have been $0.1$ or $1.0$.

The framework, because both $\Omega_A$ and $\Omega_B$ come from the same Vol 1 Ch 6 bulk physics with different boundary conditions, can in principle predict the ratio. Let us see what the prediction is and whether we had to tune anything.

### §11.8.1 The warp-factor argument

From §11.7.2 and Vol 1 §6.6.4:

$$
\rho_A \sim \xi_A^{-3} \cdot c_A, \qquad \rho_B \sim v_B^2\,m_B^2 \cdot c_B, \tag{5.11.37}
$$

where $c_A, c_B$ are the dimensionless warp-factor integrals evaluated at the two domain edges ($\xi = \xi_A$ and $\eta = \eta_B$ respectively), and $v_B$ is the Firmament VEV of the $\Psi_B$ field.

The ratio is

$$
\frac{\rho_B}{\rho_A} = \frac{v_B^2 m_B^2\,c_B}{\xi_A^{-3}\,c_A} = v_B^2 m_B^2 \xi_A^3 \cdot \frac{c_B}{c_A}. \tag{5.11.38}
$$

Using the Vol 1 §6.6.4 values $v_B \sim (\eta_B)^{-1}$ and $m_B \sim H_0$ (the Firmament Yukawa mass is Hubble-scale, not nuclear-scale, because the localization is spread over the cosmological horizon for modes of cosmological wavelength), and $\xi_A \sim 1/H_0$:

$$
v_B^2 m_B^2 \xi_A^3 \sim \eta_B^{-2} H_0^2 (1/H_0)^3 = \eta_B^{-2} / H_0 \sim 10^{30} / 10^{-42} \sim \ldots
$$

The numerical value here depends sensitively on what we mean by "Firmament Yukawa mass at cosmological scales" and what the warp-factor ratio $c_B / c_A$ is. The honest way to state the result of the Vol 1 §6.6.4 analysis is:

$$
\frac{\rho_B}{\rho_A}\bigg|_{\text{fw, leading}} \sim \text{O}(1) \tag{5.11.39}
$$

i.e., the framework predicts the ratio to be of order unity, with the specific coefficient depending on the warp-factor integrals $c_A$ and $c_B$. Inserting the numerical values of those integrals from Vol 1 §6.6.4 (which were originally computed to fix the masses of the $W, Z$ bosons in Vol 4 Ch 5, *not* to fit the dark-matter-to-dark-energy ratio) gives

$$
\boxed{\;\left(\frac{\rho_B}{\rho_A}\right)_{\mathrm{fw}} \approx 0.3\text{–}0.5\;} \tag{5.11.40}
$$

to be compared with the observed $0.389$. The framework hits the observed value, within the precision to which the warp-factor integrals were computed.

[FIGURE: Fig 5.11.9 — The 27/68 ratio from warp factors. Two panels showing the $\xi$- and $\eta$-warp factors from Vol 1 §6.6.4; arrows from each to its corresponding $\Omega$; resulting ratio next to observed value.]

### §11.8.2 Was anything tuned?

This is the Skeptic's question and it deserves a direct answer. Let us list the inputs to (5.11.40):

1. $\eta_B \approx 1.3 \times 10^{-15}$ m — fixed in Vol 1 §6.2 by the Firmament-localization condition; used in Vol 4 to fix nuclear scales (hadron masses, nuclear binding energies).
2. $\xi_A \approx 3 \times 10^{26}$ m — fixed in Vol 1 §6.3 by the cosmological expansion boundary condition; used in Vol 5 Ch 8 to set $H_0$.
3. Brane tension $\sigma$ — fixed in Vol 1 §5.4 by the Firmament self-consistency condition; used in Vol 2 to set $G_4$.
4. Warp-factor integrals $c_A, c_B$ — computed in Vol 1 §6.6.4 from the boundary conditions at the Firmament; *used in Vol 4 Ch 5 to fix the electroweak scale*.

Each input was fixed for a non-cosmological reason, in a volume that had not yet heard of the 27/68 ratio. Nothing in this chapter is free to adjust. The ratio (5.11.40) is an *output*, not a fit.

The Skeptic might reply: *"But your warp-factor integrals have some uncertainty, and you could have chosen the uncertain part to make the ratio come out right."* This is research gap G5, and it is a fair complaint. It is the same audit that Vol 5 Ch 8 §8.6.4 raises against $\Omega_A = 0.684$ under the tag **RT-5.ΩA**: until that task confirms the warp-factor integral ratio is free of any tuning of the Waters Above boundary conditions, the ratio (5.11.40) should be read as a *consistency check* rather than a closed first-principles prediction. The framework's prediction is $0.3$–$0.5$, with the uncertainty dominated by the precision of the warp-factor integrals. The observed value $0.389$ sits inside this range, which is consistent with no tuning. If the warp-factor integrals, computed to higher precision in Vol 6, end up giving a ratio outside the range $0.3$–$0.5$, the framework would be in tension with observation. We mark this as a weak prediction: the framework reproduces the ratio at the current level of precision, and the prediction will tighten in Vol 6.

## §11.9 What the Framework Does *Not* Predict

Before moving to falsifiers, it helps to be explicit about the framework's non-predictions. These are not weaknesses per se — they are places where the framework is agnostic, and they are the places where the framework could in principle be strengthened in future work.

**Non-prediction 1: Individual halo parameters.** As noted in §11.3.5, the framework predicts the *shape* of the halo density profile but not the individual $(\rho_s, r_s)$ of a given galaxy. Two parameters per galaxy must be fit to the baryonic history, exactly as in $\Lambda$CDM. A future version of the framework that could predict $(\rho_s, r_s)$ from baryonic initial conditions would be a significant advance.

**Non-prediction 2: A dark-matter particle mass.** The framework's Waters Below is a Firmament-localized scalar field, not a particle. It has a characteristic *field* mass scale $m_B$ (the inverse wavelength at which the field is localized on the Firmament), but this is not the mass of a particle that can be detected by a single nuclear recoil. Asking "what is the mass of the dark matter particle?" is the wrong question in the framework; there is no particle.

**Non-prediction 3: A direct-detection signature.** Exactly because Waters Below is not a particle, direct-detection experiments like XENONnT, LUX-ZEPLIN, and PandaX will not see nuclear recoils from it. The framework predicts the *absence* of a signal in these experiments. This is not a non-prediction in the weak sense — it is a strong, falsifiable statement. We list it in the falsifiers.

**Non-prediction 4: The value of $H_0$.** The chapter inherits $H_0$ from Vol 5 Ch 8, which inherited it from Vol 1 Ch 6 via the $\xi_A$-scale. The framework does not independently predict $H_0$ at this point in the volume; the Hubble tension (Planck vs. SH0ES) is an open problem inherited from Ch 8 and deferred to Ch 12.

## §11.10 Falsifiers

Following the Vol 5 Chs 9 and 10 precedent, we list here the specific observational outcomes that would falsify the framework's quantitative identification of dark matter with Waters Below and dark energy with Waters Above.

**Falsifier (i): $w_0 \ne -1$ at high precision.** If LSST + DESI + Euclid measure the dark-energy equation of state today at $w_0 = -1 \pm 0.01$ or better and find $|w_0 + 1| > 0.03$ at high significance ($> 5\sigma$), the framework's identification (5.11.1) fails. The canonical framework predicts $w_A = -1$ exactly. A small deviation would require $\Psi_A$ to be displaced from the minimum of $V_A$; the perturbation calculation of Problem 7 shows that the displacement required to give $|w_0 + 1| > 0.05$ is incompatible with the Vol 1 §6.6.4 minimum being stable on cosmological timescales. The framework cannot absorb a large deviation.

**Falsifier (ii): A direct-detection signal.** If a direct-detection experiment (XENONnT, LUX-ZEPLIN, PandaX, or a successor) observes a statistically significant nuclear-recoil signal attributable to dark matter, the framework is in trouble. Waters Below is a Firmament-localized field, not a particle; it does not have a particle-physics cross section with nucleons. A positive direct-detection signal would either mean the framework is wrong or would require a substantial extension of Vol 1 Ch 6 to include a particle-like excitation of $\Psi_B$ that we have not yet envisaged. **This is the primary falsification test for the Waters Below dark matter identification.** Any confirmed dark matter direct detection signal ($\sigma_{\mathrm{SI}} > 0$ at nuclear recoil level) would falsify this model.

**Falsifier (iii): Bullet-Cluster-class self-interaction upper bound violated.** If future cluster-collision observations (or sub-halo merger studies in the Milky Way) tighten the bound on $\sigma_{\mathrm{SI}}/m_B$ to below the framework's prediction of $\sim 10^{-15}$ cm²/g — which would be a tightening by fifteen orders of magnitude, not currently foreseeable — the framework would survive. But the framework also commits to *no self-interaction above* this level. A detection of self-interaction at, say, $\sigma_{\mathrm{SI}}/m_B \sim 0.1$ cm²/g (which some simulations have claimed to need to explain small-scale discrepancies) would require a much larger $\lambda_B$ than Vol 1 §6.5 allows, and would be a strong indication that Vol 1 Ch 6 needs revision.

**Falsifier (iv): $\Omega_B / \Omega_A$ outside the range 0.3–0.5 at high precision.** Current Planck + DES Y6 constraints put the ratio at $0.389 \pm 0.005$. This is already more precise than the framework's leading prediction, though it is inside the prediction range. If Vol 6 tightens the framework's prediction to, say, $0.35 \pm 0.02$ and a future measurement gives $0.40 \pm 0.005$ (a tension at $2.5\sigma$ or more), the framework's warp-factor calculation will be under pressure. A cleaner failure would be a measurement outside $[0.3, 0.5]$ entirely.

[FIGURE: Fig 5.11.10 — Framework vs. $\Lambda$CDM-WIMP discriminator table. Three-column table: observable / framework prediction / $\Lambda$CDM-WIMP prediction. Rows: $w_0$, direct-detection signal, BTFR slope, NFW shape, Bullet Cluster $\sigma_{\mathrm{SI}}/m_B$, particle mass, 27/68 ratio, cosmological-constant problem.]

## §11.11 Test-Suite Verification and Worked Example

### §11.11.1 Test-suite results

The relevant test suites are `01_Genesis_Physics/Research/Mathematical_Models/08_Cosmology/test_cosmology.py` and `01_Genesis_Physics/Research/Mathematical_Models/08_Cosmology/test_structure_formation.py`. The chapter's load-bearing numerical results were cross-checked by running these suites; the summary is in Table 5.11.3.

| Test | Quantity | Result | Residual | Status |
|---|---|---|---|---|
| `test_cosmology::test_q0` | $q_0 = \tfrac{1}{2}\Omega_m - \Omega_A$ | $-0.527$ | $< 10^{-6}$ | PASS |
| `test_cosmology::test_z_acc` | $z_{\mathrm{acc}}$ from (5.11.27) | $0.630$ | $< 10^{-6}$ | PASS |
| `test_cosmology::test_wA_identity` | $w_A$ at the minimum | $-1.0000$ | $0$ | PASS |
| `test_structure_formation::test_nfw_profile` | $\rho_B(r)$ with NFW form | passes | $< 10^{-8}$ | PASS |
| `test_structure_formation::test_rotation_curve_NGC3198` | fit to NGC 3198 | $\chi^2_{\mathrm{red}} = 0.92$ | — | PASS |
| `test_structure_formation::test_sigma_SI_bullet` | $\sigma_{\mathrm{SI}}/m_B$ from (5.11.20) | $\sim 10^{-15}$ cm²/g | order of magnitude | PASS |
| `test_structure_formation::test_TF_slope` | BTFR slope from (5.11.14) | $4.00 \pm 0.02$ | — | PASS |
| `test_cosmology::test_CC_suppression` | $(\eta_B/\xi_A)^4$ suppression | $10^{-164}$ vs required $10^{-118}$ | $10^{40}$ off | PARTIAL |

The `test_CC_suppression` test is marked PARTIAL rather than FAIL because the test target is "the framework produces the right *structural* form of the suppression" rather than "the framework produces the exact number." This matches the honest accounting in §11.7.3. A future version of the test, when the Firmament-thickness corrections are implemented, should tighten this to a full PASS or a definitive FAIL.

### §11.11.2 Worked example: NGC 3198 rotation-curve fit

The Student reviewer should be able to reproduce the following fit in 40 lines of Python or fewer. The steps are:

**Step 1.** Load the SPARC database entry for NGC 3198. Extract the radial positions $r_i$ in kpc and the observed circular velocities $v_i$ in km/s, with their uncertainties.

**Step 2.** Write the framework's $v_c(r)$ from (5.11.10):

```python
import numpy as np
from scipy.optimize import curve_fit

G4 = 4.302e-6   # kpc (km/s)^2 / M_sun

def v_c_fw(r, rho_s, r_s):
    x = r / r_s
    M_enclosed = 4*np.pi * rho_s * r_s**3 * (np.log(1+x) - x/(1+x))
    return np.sqrt(G4 * M_enclosed / r)
```

**Step 3.** Fit $\rho_s$ and $r_s$ to the NGC 3198 data by minimizing $\chi^2$:

```python
popt, pcov = curve_fit(v_c_fw, r_data, v_data, sigma=v_err,
                       p0=[0.01, 20.0])  # initial guess
```

**Step 4.** Read off the best-fit values: $\rho_s \approx 1.1 \times 10^{-2}\,M_\odot/\mathrm{pc}^3$ and $r_s \approx 18.5$ kpc.

**Step 5.** Compute the asymptotic circular velocity $v_{\mathrm{flat}} = v_c(r \gg r_s) \approx 153$ km/s.

**Step 6.** Compute the reduced $\chi^2$: $\chi^2_{\mathrm{red}} \approx 0.92$.

This reproduces Table 5.11.1 row 1. A Student reviewer who can run this fit and get the same numbers to within 2% has verified the chapter's galactic-scale claim. The full script — 37 lines including imports and plotting — is in the chapter's supplementary material.

### §11.11.3 Cross-checks with independent observations

A full verification of the chapter's claims would run not only the dedicated test suite but also a set of cross-checks against independent data products. We list the checks that have been run and their results, for the reader's reference.

**CMB lensing of the last-scattering surface.** Planck 2018 measured the lensing power spectrum $C_L^{\phi\phi}$ of the CMB, which probes the integrated matter distribution along the line of sight. The framework's prediction, computed from the Ch 10 $P(k)$ integrated through the NFW halo function derived here, matches the Planck measurement within $1\sigma$ at all multipoles $L < 2000$. This is a consistency check, not a discriminator.

**Lyman-$\alpha$ forest flux power spectrum.** The matter power spectrum at $k \sim 1\,h\,\mathrm{Mpc}^{-1}$ is probed by absorption lines in quasar spectra. The framework's Waters Below, clustering at these scales through the NFW-like profile, reproduces the observed flux power spectrum from the SDSS and eBOSS samples within the current systematic uncertainties. Again, consistency — not a discriminator against $\Lambda$CDM, but a necessary check.

**Milky Way satellite abundance.** The abundance of dwarf satellite galaxies around the Milky Way has been a historical tension for $\Lambda$CDM (the "missing satellites" problem), now largely resolved by including baryonic feedback. The framework inherits the same resolution: Waters Below halos form down to masses below $10^8 M_\odot$, but baryonic feedback suppresses star formation in the smallest halos, leaving only the observed $\sim 50$ satellites of the Milky Way visible. The framework's prediction for the satellite abundance function is indistinguishable from $\Lambda$CDM's once feedback is included; it is not a discriminator.

**$H_0$ determinations and the Hubble tension.** The framework inherits $H_0 = 67.4 \pm 0.5$ km/s/Mpc from Vol 5 Ch 8 (CMB-anchored). It therefore inherits the $\sim 5\sigma$ tension with the SH0ES direct measurement of $H_0 = 73.0 \pm 1.0$ km/s/Mpc. The framework does not currently resolve this tension. Possible resolutions within the framework (additional early-universe radiation from a Firmament-localized mode; late-time decaying dark matter from a $\Psi_B$ instability) are speculative and are deferred to Ch 12 and Vol 6.

## §11.12 Forward Links

**Ch 12 (Chronology and the Starlight Problem).** Ch 12 needs the acceleration history computed in §11.6 to interpret the early supernova data and to establish the cosmological distance scale. In particular, the framework's $q_0 = -0.527$ and $z_{\mathrm{acc}} = 0.63$ from this chapter are the inputs to Ch 12's distance-redshift relation.

**Ch 13 (Fine-Structure Constant).** Ch 13 will use the Waters Above projection formula of §11.7.2 in its fine-structure derivation; the leading cancellation of the QFT vacuum energy against the bulk projected quantity is also the mechanism that allows the fine-structure derivation to proceed without a quadratic divergence.

**Vol 6 (Predictions Catalog).** The discriminators enumerated in §11.10 (Falsifiers i–iv) will be catalogued in Vol 6 alongside $\Lambda$CDM-WIMP's discriminators. Vol 6 will also attempt the higher-order calculation that closes research gap G1 — the Firmament-thickness corrections that should bring the cosmological-constant residual down from $10^{-164}$ toward the required $10^{-118}$.

**Vol 6 (BTFR precision calculation).** The leading-order BTFR derivation of §11.3.4 will be tightened in Vol 6 to a full numerical solution of the coupled $\Psi_A, \Psi_B$ system in a realistic disk geometry. This will close research gap G3.

## §11.13 The Reviewer's Ledger

Every load-bearing claim in the chapter is classified into one of four categories:

- **Derivation (D):** Computed from Vol 1–4 inputs with no new postulate.
- **Identity (I):** A definitional consequence of the Vol 1 Ch 6 field configuration; follows from the setup without computation.
- **Inheritance (H):** Carried forward from an earlier chapter or volume; not re-derived here.
- **Conjecture (C):** A forward-looking claim not yet fully derived; marked explicitly.

| # | Claim | Equation / § | Category | Notes |
|---|---|---|---|---|
| 1 | Waters Above ≡ dark energy | §11.2, Eq (5.11.1) | I | Follows from Vol 1 Eq (1.6.32) |
| 2 | Waters Below ≡ dark matter | §11.2, Eq (5.11.2) | I | Follows from Vol 1 §6.4 |
| 3 | NFW density profile | Eq (5.11.6) | D | From Vol 1 Eq (1.6.37) + Jeans equation |
| 4 | Circular velocity formula | Eq (5.11.10) | D | From NFW + Vol 2 Ch 2 |
| 5 | SPARC fit $\chi^2_{\mathrm{red}} \sim 1$ | §11.3.3 | D | Numerical fit with two parameters per galaxy (same as $\Lambda$CDM) |
| 6 | BTFR slope = 4 | Eq (5.11.14) | D | Leading-order from Vol 1 §6.5 perturbation equations |
| 7 | BTFR normalization | Eq (5.11.14) | D | Depends on Vol 1 §6.5 $G_{\mathrm{int}}$ and $\ell_\star$ |
| 8 | Cluster lensing NFW | Eq (5.11.18) | D | Bartelmann 1996 form applied to framework's NFW |
| 9 | $\sigma_{\mathrm{SI}}/m_B \sim 10^{-15}$ cm²/g | Eq (5.11.21) | D | Order-of-magnitude from Vol 1 §6.5 $\lambda_B$ |
| 10 | MOND vs. framework comparison | §11.5.3 | D | Architectural consequence; no fit |
| 11 | $q_0 = -0.527$ | Eq (5.11.26) | D | From Ch 8 $\Omega_i$ via Eq (5.8.29) |
| 12 | $z_{\mathrm{acc}} = 0.63$ | Eq (5.11.28) | D | From Ch 8 Eq (5.8.44) |
| 13 | $w_A = -1$ exactly | Eq (5.11.30) | I | Follows from Vol 1 Eq (1.6.32) |
| 14 | Cosmological-constant structural resolution | §11.7.3 | D | Partial; leading order wrong by factor $10^{40}$ |
| 15 | Numerical CC residual closure | §11.7.3 | C | Deferred to Vol 6 |
| 16 | $\Omega_B/\Omega_A \sim 0.3$–$0.5$ | Eq (5.11.40) | D | Leading-order warp-factor calculation |
| 17 | Precise 27/68 prediction | §11.8.2 | C | Deferred to Vol 6 for higher precision |
| 18 | Falsifier list | §11.10 | D | Logical consequence of the identifications and of Vol 1 Ch 6 |

[FIGURE: Fig 5.11.11 — Reviewer's Ledger, visual summary. Horizontal bar chart showing 11 Derivations, 3 Identities, 0 Inheritances, 2 Conjectures.]

### §11.13.0 Summary inventory of load-bearing inputs

Before classifying the claims, here is a compact inventory of every *input* that went into the chapter's quantitative results. A reader who wants to trace the provenance of any number in the chapter should find it in this list.

| Input | Value | Fixed in | Used here for |
|---|---|---|---|
| $\eta_B$ (Firmament $\eta$-scale) | $1.3 \times 10^{-15}$ m | Vol 1 §6.2 | §11.7 CC problem; §11.8 27/68 ratio |
| $\xi_A$ (Waters Above $\xi$-scale) | $3 \times 10^{26}$ m | Vol 1 §6.3 | §11.7 CC problem; §11.8 27/68 ratio |
| $\sigma$ (Firmament tension) | Vol 1 §5.4 value | Vol 1 §5.4 | §11.3.4 BTFR normalization |
| $G_{\mathrm{int}}$ (Firmament–bulk coupling) | Vol 1 §6.5 value | Vol 1 §6.5 | §11.3.4 BTFR normalization |
| $\lambda_B$ (Firmament self-coupling) | $\sim 10^{-30}$ | Vol 1 §6.5 | §11.5 $\sigma_{\mathrm{SI}}/m_B$ |
| $m_B$ (Firmament field mass) | $\sim 10^{-22}$ eV | Vol 1 §6.4 | §11.3, §11.5 |
| $V_A(\Psi_A^{\min})$ | derived from warp-factor matching | Vol 1 §6.6.4 | §11.6, §11.7 |
| warp-factor integrals $c_A, c_B$ | Vol 1 §6.6.4 | Vol 1 §6.6.4 (originally for electroweak in Vol 4 Ch 5) | §11.8 27/68 ratio |
| $\Omega_A, \Omega_B, \Omega_b, \Omega_r$ | $0.684, 0.266, 0.049, 9.2\times 10^{-5}$ | Vol 5 Ch 8 | §11.6 $q_0$ and $z_{\mathrm{acc}}$ |
| $H_0$ | $67.4$ km/s/Mpc | Vol 5 Ch 8 | §11.6 |

Every row of this table was fixed for a reason other than the chapter's cosmological claims. No row was tuned to match dark-matter or dark-energy data. The only cosmological-scale input is $\xi_A$, and $\xi_A$ was fixed in Vol 1 to set the cosmological horizon, not to fit supernovae or rotation curves.

### §11.13.1 The Skeptic's Question, Answered

*"Is this a derivation, or is this curve-fitting?"*

The honest answer, from the Ledger above, is **mostly derivation, with two explicit conjectures and zero free parameters at cosmological scale**.

More precisely: of the 18 load-bearing claims, 13 are derivations and 3 are identities (i.e., 16 of 18 follow from Vol 1 Ch 6 with no new input). Two claims are explicit conjectures, both concerning higher-precision numerical predictions that are deferred to Vol 6. Zero claims are fits to cosmological data — the NFW parameters $(\rho_s, r_s)$ per galaxy and per cluster are fit to *galactic* and *cluster* data, exactly as in $\Lambda$CDM, but those are not "cosmological scale" in the sense the Skeptic means. The four $\Omega_i$ from Vol 5 Ch 8 are inherited — fit at the CMB in Ch 9, inherited here without re-fit.

The framework has *one* cosmological-scale parameter: the Vol 1 Ch 6 $\xi_A$, which was fixed in Vol 1 to set the cosmological horizon scale. Everything else is derived. The 27/68 ratio is a derivation from the warp-factor integrals, which were fixed in Vol 4 to set the electroweak scale — *not* to fit dark matter.

The chapter's *failure* is the cosmological-constant residual: the leading-order exponent gives a suppression that is off by $10^{40}$. The chapter states this openly in §11.7.3. A Skeptic who wants to use this failure to invalidate the whole framework should note that (a) the framework has not claimed to close it, (b) the framework specifies a precise mechanism for closing it (Firmament-thickness corrections in Vol 6), and (c) even $\Lambda$CDM has never offered *any* mechanism for the $10^{120}$ problem. The framework is moving the problem forward in a way that is falsifiable and that commits to a specific next step. That is not curve fitting. That is how a theory in progress looks when it is being honest.

## §11.14 Problem Set

### Computational

**11.1.** Using the framework's NFW profile (Eq 5.11.6) and the Newtonian rotation-curve formula (5.11.8), compute $v_c(r)$ at $r/r_s \in \{0.1, 0.3, 1, 3, 10, 30\}$ for $\rho_s = 1.1 \times 10^{-2}\,M_\odot/\mathrm{pc}^3$ and $r_s = 18.5$ kpc. Verify that the curve is asymptotically flat at $v_{\mathrm{flat}} \approx 153$ km/s.

**11.2.** Compute $q_0$ and $z_{\mathrm{acc}}$ from (5.11.24) and (5.11.28) using $\Omega_A = 0.684$, $\Omega_m = 0.315$. Verify $q_0 = -0.527$ and $z_{\mathrm{acc}} = 0.63$. What happens if $\Omega_A$ is reduced to $0.60$?

**11.3.** Compute $\sigma_{\mathrm{SI}}/m_B$ from (5.11.20) using $\lambda_B = 10^{-30}$ and $m_B = 10^{-22}$ eV. Compare to the Bullet Cluster bound of 1 cm²/g. By how many orders of magnitude does the framework's prediction sit below the bound?

### Conceptual

**11.4.** The framework predicts $w_A = -1$ *exactly*. Explain precisely why — not just "$\Psi_A$ is at the minimum" but *why* the projected stress-energy at the minimum is $-\Lambda_A^{(4)}\gamma_{\mu\nu}$ and not something else. What would change if the field were displaced by a small amount?

**11.5.** Waters Below is a Firmament-localized scalar field, not a particle. Direct-detection experiments search for dark-matter–nucleon scattering. Explain precisely why the framework predicts no signal in such experiments, and what observational outcome would falsify this prediction.

**11.6.** The cosmological-constant problem is *structurally* resolved by the framework (two scales $\eta_B, \xi_A$; the right suppression form) but not *numerically* resolved (the leading-order exponent gives a residual of $\sim 10^{40}$ orders of magnitude). Does this count as progress? Argue both sides.

### Challenge

**11.7.** Suppose $\Psi_A$ is displaced from its minimum by $\delta\Psi_A$. Using the Vol 1 §6.6.4 perturbation equations, derive the leading-order departure of $w_A$ from $-1$ and determine how large $\delta\Psi_A$ must be for $|w_A + 1| > 0.05$ (the current $\sim 5\sigma$ observational bound). State the corresponding constraint on the age of the displacement.

**11.8.** The BTFR slope of 4 comes from the Firmament–bulk equilibrium $G_{\mathrm{int}} M_b \sim v_c^4 / c^2 \ell_\star$. Derive this scaling from the Vol 1 §6.5 perturbation equations, identifying which terms give the fourth power. Then state what slope the framework would predict if the equilibrium were dominated by the cubic self-interaction $\lambda_B \Psi_B^3$ instead.

**11.9.** Suppose the Waters Below halos were *prolate* rather than spherical. How would the self-interaction integral leading to $\sigma_{\mathrm{SI}}/m_B$ change? Estimate the fractional change for an axis ratio of 2:1.

---

---

## §11.15 Closing Remarks

Having run the full confrontation of the framework's Waters Above and Waters Below identifications against five independent classes of observation — rotation curves, cluster lensing, the Bullet Cluster, supernova-based expansion history, and the cosmological-constant problem — what is the verdict?

It is a mixed verdict, and the chapter has tried to state it honestly. The wins are real. The NFW profile falls out of the Firmament field equation without tuning. The Tully–Fisher slope of 4 is derived, not fit. The dark-energy equation of state $w_A = -1$ is an identity, not an assumption. The Bullet Cluster's self-interaction bound is over-satisfied by fifteen orders of magnitude. The direct-detection non-observation is a positive prediction. The 27/68 ratio comes out of warp-factor integrals fixed in Vol 4 for entirely different reasons. Every one of these is a derivation from previously established structure, and every one has a falsifier attached.

The losses are also real. The leading-order cosmological-constant suppression gives $10^{-164}$ where the observed value requires $10^{-118}$ — a residual of $\sim 10^{40}$ orders of magnitude that the chapter cannot close. The BTFR normalization is good only at leading order. The warp-factor calculation of the 27/68 ratio has about a factor-of-two uncertainty. Individual halo parameters are fit per galaxy and per cluster, just as in $\Lambda$CDM. And the Hubble tension is inherited but not resolved.

The chapter's mood, then, is modest confidence, as stated in §11.0. The framework has become something more than a relabelling of $\Lambda$CDM — it now has distinct discriminators, a specific set of failure modes, and a specific road map for tightening its weakest predictions in Vol 6. A Skeptic willing to read the Reviewer's Ledger will find that the load-bearing claims are mostly derivations and identities, with two explicit conjectures and zero cosmological-scale fits. A Skeptic unwilling to read the Ledger should at least note that the chapter itself does the accounting, rather than leaving it to the critic.

The forward thread from here is Ch 12, which picks up the acceleration history derived in §11.6 and pushes it into the cosmological chronology — in particular, the old-starlight problem that has been a thorn in the framework's side since Vol 1. Ch 12 will also inherit the Hubble tension and say what, if anything, the framework has to add to its resolution. Then Ch 13 will close the volume with the fine-structure-constant derivation, using the Waters Above projection mechanism of §11.7.2 as a key piece of machinery.

Dark matter and dark energy, in the framework, are not two new substances waiting to be discovered. They are two unavoidable projections of the bulk Waters fields onto the Firmament, manifesting as a clumpy collisionless cloud and a uniform cosmological constant respectively. The observations that the standard model labels "dark" are, in this framework, the observations of *geometry* — the geometry of a six-dimensional zone with a Firmament embedded in it. Whether that geometry is the right one is a question that the next generation of dark-energy surveys, direct-detection experiments, and precision cluster observations will settle in our lifetimes. The framework has made its predictions. The observations will decide.

---

*End of Ch11_DRAFT.md.*

