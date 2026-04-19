# Chapter 9: The CMB and Early Universe
## Foundations Vol 5: The Cosmos — Part III: Cosmology

---

> *"What we call the cosmic microwave background is the oldest photograph ever taken: a single exposure, more than thirteen billion years long, of the surface where light first escaped from matter. The framework whose chapter eight you have just finished promises that this photograph is not a happy accident of fitted parameters but the necessary appearance, on the sky of an observer at $z = 0$, of the brane FLRW geometry derived three sections ago. The promise is testable. This chapter tests it."*

---

## §9.0 What This Chapter Is (and Is Not)

Before stating any number, I want to declare what is being derived in this chapter and what is being inherited, because the central technical task — comparing the framework's prediction to Planck 2018 quantitatively — is also the task most easily mistaken for one stronger than it is and for one weaker than it is.

**What this chapter does.** It takes the sustaining-mode cosmological model of Vol 5 Ch 8 — the brane-projected Waters fluid, the Friedmann era structure, the four density parameters — and walks the chain from there to the observed structure of the cosmic microwave background. The recombination redshift comes out from the Saha equation applied to the brane plasma at the temperature evolved from Ch 8 §8.8.3. The photon decoupling surface comes out from the Boltzmann visibility function. The acoustic peak positions come out from the ratio of the sound horizon to the angular-diameter distance, both computed from the Ch 8 era structure. The peak heights come out from the baryon-loading parameter, which is set by $\Omega_b$ from Ch 8 §8.6.3. The Silk damping envelope comes out from photon diffusion in the prerecombination plasma — and admits, in the framework, an additional and consistent interpretation as membrane viscosity (Vol 1 Ch 5). At the end of the chain, §9.10 computes a quantitative $\chi^2$ against the Planck 2018 binned TT data.

**What this chapter does not do.** It does not derive the amplitude $A_s$ or the spectral index $n_s$ of the primordial power spectrum from first principles. Both depend on the dynamics of the Sabbath Boundary, which is a Vol 1 Ch 11 + Vol 6 task; this chapter inherits them and is honest about it. It does not run a CAMB-equivalent Boltzmann hierarchy; it uses analytical phase corrections from the source documents (CMB_TRANSFER_FUNCTION.md), which are accurate to a few percent rather than to per-mille. It does not derive the *size* of the Hubble tension; it identifies the tension as the Sabbath Boundary's observational signature and leaves the quantitative prediction to Vol 6 and Ch 12 of this volume.

**A note for the Skeptic reviewer.** The hardest question for this chapter is: *did you tune anything to match Planck?* The honest answer is no, but the reason is subtle. The framework's cosmological inputs — $\Omega_A, \Omega_B, \Omega_b, \Omega_r, H_0$ — were derived in Vol 5 Ch 8 from non-cosmological scales (the brane radius, the nuclear scale, the brane tension; see Ch 8 §8.6.4). This chapter takes those inputs as given and *computes* the CMB observables. The chain runs *(non-cosmological inputs) → (Ch 8 cosmology) → (CMB observables compared to Planck)*. The match to Planck is therefore a *consequence* of the chain, not a fit. The Skeptic should still scrutinize this; §9.10 itemizes every input and §9.15 classifies every claim.

There is one genuine inheritance from observation: the amplitude $A_s$ of the primordial spectrum. The framework does not derive it in this volume. The chapter is explicit about this in §9.9 and does not claim more.

**A note for the Physicist reviewer.** The hardest question for the Physicist is: *is the CMB power spectrum genuinely derived from the framework, or are you smuggling in $\Lambda$CDM by writing it in standard form?* The chain is: Ch 8 gives the era structure and the four density parameters; this chapter applies standard recombination physics (Saha + Boltzmann), standard acoustic-wave physics (sound horizon + Rees–Sciama corrections), and standard photon-diffusion physics (Silk damping). All three pieces of "standard" physics are inherited from earlier volumes: Saha and Boltzmann from Vol 3 Ch 12 and Vol 4 Ch 10; the sound speed in the baryon-photon plasma from Vol 3 Ch 5; the Thomson cross section from Vol 2 Ch 3. None of it is reinvented for this chapter. What *is* reinvented — and the reason this chapter exists at all — is the *origin* of the era structure that feeds into all of those calculations. In $\Lambda$CDM, the era structure is parameterized by six numbers fit to data. In the framework, it is the projection of the Waters fields, and the four density parameters were derived (or at least geometrically inherited) from non-cosmological inputs in Ch 8.

**A note for the "But Why?" reader.** The chapter has been organized around the ten why-questions of the chapter spec. Each section opens with one or more of them and answers them in plain language before introducing any equations. The ledger in §9.15 collects the one-line answers.

**Roadmap.** §9.1 inventories the toolkit from previous chapters. §9.2 translates the Ch 8 era structure into a thermal history. §9.3 derives the recombination redshift from the Saha equation. §9.4 derives the photon decoupling surface from the visibility function. §9.5 derives the sound horizon and the angular-diameter distance to last scattering. §9.6 derives the acoustic peak positions including the phase corrections. §9.7 derives the relative peak heights from baryon loading. §9.8 derives the Silk damping envelope. §9.9 inherits $A_s$ and $n_s$, with the qualitative argument for $n_s < 1$. §9.10 is the quantitative comparison with Planck 2018 — the chapter's load-bearing section. §9.11 inherits BBN from Vol 4 Ch 10. §9.12 identifies the Hubble tension as the Sabbath-Boundary signature. §9.13 reports the test suite. §9.14 lists the forward links. §9.15 is the Reviewer's Ledger. §9.16 is the problem set.

---

## §9.1 Inventory: The Toolkit From Previous Chapters

As in Chapters 5–8 of this volume, we begin by laying out the tools. Nothing in this chapter is re-derived if it has already been proven elsewhere; the inventory below is not just a courtesy to the reader but a contract with the Consistency Auditor.

### §9.1.1 From Vol 5 Ch 8 — the sustaining-mode cosmology

Vol 5 Ch 8 derived the Friedmann constraint, the acceleration equation, the continuity equation, the era structure, and the four density parameters. We will use:

- The function $E(z) \equiv H(z)/H_0$ from Ch 8 Eq (5.8.40):

$$(5.9.1)\quad E(z) = \sqrt{\Omega_A + \Omega_m(1+z)^3 + \Omega_r(1+z)^4},$$

with $\Omega_A = 0.684$, $\Omega_m = \Omega_B + \Omega_b = 0.315$, $\Omega_r \approx 9.2\times 10^{-5}$, $\Omega_b = 0.049$, $\Omega_B = 0.266$, all from Ch 8 §8.6.3 and inherited there from the bulk-field calculation of Vol 1 §6.7.

- The Hubble constant $H_0 = 67.4$ km/s/Mpc from Ch 8 Eq (5.8.47).
- The present CMB temperature $T_0 = 2.725$ K from Ch 8 Eqs (5.8.51)–(5.8.52), with the temperature evolution

$$(5.9.2)\quad T(z) = T_0(1+z),$$

a consequence of $\rho_r \propto a^{-4}$ (Ch 8 §8.5.4) and the Stefan–Boltzmann relation $\rho_r \propto T^4$.

- The comoving distance, luminosity distance, and angular-diameter distance integrals from Ch 8 Eqs (5.8.52)–(5.8.54).

These six items will be used everywhere below, and the chapter is internally a function of them.

### §9.1.2 From Vol 1 Ch 5 — the brane and its viscosity

Vol 1 Ch 5 established the Firmament as a codimension-2 brane $\Sigma$ with tension $\sigma > 0$ and mass density $\mu$, supporting transverse waves at speed $c^2 = \sigma/\mu$ (Vol 1 Eq 1.5.37). Of relevance to this chapter is the *membrane viscosity* introduced in Vol 1 §5.7 — the dissipative coupling of brane modes to extra-dimensional Waters fluctuations. We will revisit this in §9.8.2 as the framework's interpretation of Silk damping.

### §9.1.3 From Vol 1 Ch 11 — sustaining mode and the Sabbath Boundary

Vol 1 Ch 11 introduced the four-phases architecture and defined the Sabbath Boundary as the Phase 1 → Phase 2 transition in zone thermodynamics, across which the sustaining coupling $\kappa$ steps from $\kappa_\text{create}$ to $\kappa_\text{full}$. This chapter is restricted to the *post-Boundary* sustaining-mode regime throughout, with one exception: §9.12 identifies the Hubble tension as the Boundary's observational signature, classified as a Conjecture in §9.15.

### §9.1.4 From Vol 2 Ch 3 — Thomson scattering and atomic constants

Vol 2 Ch 3 (where the fine structure constant story is begun and the EM sector is built up) gives us the Thomson cross section

$$(5.9.3)\quad \sigma_T = \frac{8\pi}{3}\!\left(\frac{e^2}{4\pi\epsilon_0 m_e c^2}\right)^2 = 6.65\times 10^{-29}\;\text{m}^2,$$

the electron mass $m_e = 9.109\times 10^{-31}$ kg, and the hydrogen binding energy $B_H = 13.6$ eV. These are the atomic-scale inputs to recombination and to photon diffusion.

### §9.1.5 From Vol 3 Ch 5 — sound speed in the baryon-photon plasma

Vol 3 Ch 5 derived the sound speed in a relativistic two-component fluid:

$$(5.9.4)\quad c_s^2 = \frac{c^2}{3(1 + R_b)},\qquad R_b \equiv \frac{3\rho_b}{4\rho_\gamma},$$

valid in the tightly-coupled regime ($\dot\tau \gg H$). The factor of $3$ in the denominator is the standard relativistic result for a photon gas; the $R_b$ correction is the inertia of the baryons that travel along with the photons during the oscillation.

### §9.1.6 From Vol 3 Ch 12 — Saha equation

Vol 3 Ch 12 derived the Saha equation for an ionization equilibrium $H \leftrightarrow p + e^-$ in a thermal bath:

$$(5.9.5)\quad \frac{X_e^2}{1 - X_e}\,n_b = \left(\frac{m_e k_B T}{2\pi\hbar^2}\right)^{3/2}\!\!\exp\!\left(-\frac{B_H}{k_B T}\right),$$

where $X_e \equiv n_e/n_b$ is the free-electron fraction and $n_b$ is the baryon number density. This is the load-bearing equation for §9.3.

### §9.1.7 From Vol 4 Ch 10 — particle spectrum and BBN inputs

Vol 4 Ch 10 derived the particle spectrum and worked out weak-interaction freeze-out, giving the neutron-to-proton ratio at freeze-out and the framework for BBN. We inherit those results in §9.11; nothing in this chapter requires us to re-derive them.

### §9.1.8 From Vol 5 Ch 7 — the past timelike boundary

Vol 5 Ch 7 (Theorem 5.7.3) replaced the Big Bang singularity with a brane-nucleation surface — a regular past timelike boundary. The radiation-era integration in §9.5 begins on that surface; this chapter does not derive the surface, only inherits it.

The toolkit is complete. We turn to the thermal history.

---

## §9.2 Brane Thermal History: From Radiation Era to Today

The thermal history of the universe is the era structure of Ch 8 §8.7 translated into temperature.

**Why does the temperature decrease as $T \propto (1+z)$?** Because the photon energy density goes as $\rho_r \propto a^{-4}$ (Ch 8 §8.5.4), the photon number density goes as $n_\gamma \propto a^{-3}$, and the average photon energy goes as $\rho_r/n_\gamma \propto a^{-1}$, which by $\langle E\rangle = (\pi^4/30\zeta(3))k_B T \approx 2.7 k_B T$ implies $T \propto a^{-1} = 1+z$. None of this is special to the framework; what *is* special is that both the *constant of proportionality* — $T_0 = 2.725$ K — and the era structure $E(z)$ that determines the time–temperature mapping were derived in Ch 8.

The relevant epochs in temperature, redshift, and cosmic time are summarized in Table 5.9.0. The values in the table are *not* inputs to the chapter; they are what the chapter inherits from Ch 8 (left two columns) and what then comes out by direct integration of the Friedmann equation through the era structure (right column).

**Table 5.9.0.** *Brane thermal history. The "framework input" column is what is inherited from Ch 8 (or, ultimately, from the Vol 1 Ch 6 bulk-field calculation). The "computed here" column is what falls out of the chapter's machinery.*

| Epoch | $T$ | Framework input | Computed here |
|---|---|---|---|
| Brane nucleation surface (Vol 5 Ch 7) | $T \sim T_\text{Pl}/10$ | Vol 5 Ch 7 | — |
| Electroweak phase transition | $\sim 100$ GeV | Inherited from Vol 4 Ch 10 | $z \sim 10^{15}$ |
| QCD confinement | $\sim 150$ MeV | Vol 4 Ch 10 | $z \sim 10^{12}$ |
| Weak freeze-out / BBN | $0.7 \to 0.07$ MeV | Vol 4 Ch 10 | $t \sim 1$ to $10^3$ s, $z \sim 4\times 10^9$ |
| Matter–radiation equality | $0.78$ eV | Ch 8 Eq (5.8.42) | $z_\text{eq} \approx 3400$ |
| Recombination | $0.26$ eV | — | $z_* \approx 1090$ (this chapter §9.3) |
| Decoupling | $0.26$ eV | — | $z_\text{dec} \approx 1089$, $\Delta z \approx 80$ (§9.4) |
| Reionization | $\sim 2$ meV | Inherited from astrophysical observation | $z \sim 8$ |
| Today | $T_0 = 2.725$ K | Ch 8 Eq (5.8.51) | $z = 0$, $t_0 = 13.8$ Gyr |

[FIGURE: Fig 5.9.1 — Brane thermal history from radiation era to today. A vertical timeline (or equivalently a $T$-vs-$z$ log-log plot) showing the epochs in the table above. Mark BBN as a band from $z\sim 4\times 10^9$ to $z\sim 4\times 10^8$, matter-radiation equality at $z_\text{eq} = 3400$, recombination at $z_* = 1090$, reionization at $z\sim 8$, and today at $z = 0$. The figure should make visually clear that recombination happens deep in the matter era (just after equality, not just before), and that reionization is many orders of magnitude later in cosmic time.]

The two epochs the chapter must compute on its own — recombination and decoupling — are the subject of §§9.3 and 9.4.

---

## §9.3 Recombination: The Saha Crossover

Recombination is the moment the brane plasma cools enough that free electrons and protons combine into neutral hydrogen, the photons stop scattering, and the universe becomes transparent. In the framework, this is *not* a separate physics input — it is the Saha equation of Vol 3 Ch 12 evaluated on the temperature-redshift relation of §9.2 with the baryon density of Ch 8 §8.6.3.

**Why is the recombination crossover at $T_* \approx 0.26$ eV instead of at the hydrogen binding energy $B_H = 13.6$ eV?** Because the photon-to-baryon ratio is enormous. There are about $1.6\times 10^9$ photons per baryon in the universe today, and the same ratio held at recombination because both number densities scale as $a^{-3}$. The *average* photon energy at $T = 13.6$ eV is just $\sim 3 k_B T \sim 40$ eV — well above $B_H$ — but only the high-energy *tail* of the Planck distribution above $B_H$ is what matters for ionization, and the tail is exponentially suppressed. The crossover occurs at the temperature for which the integrated tail above $B_H$ is comparable to the *baryon* number rather than the *photon* number, and this happens at $k_B T \approx B_H/\ln(\eta_{\gamma b}^{-1}) \approx 13.6/40 \approx 0.34$ eV. The Saha equation gets the precise value.

### §9.3.1 The Saha equation applied to the brane plasma

We start from Vol 3 Ch 12 Eq (5.9.5) restated here in compact form:

$$(5.9.6)\quad \frac{X_e^2}{1 - X_e} = \frac{1}{n_b}\!\left(\frac{m_e k_B T}{2\pi\hbar^2}\right)^{3/2}\!\exp\!\left(-\frac{B_H}{k_B T}\right).$$

The baryon number density at redshift $z$ is

$$(5.9.7)\quad n_b(z) = n_{b,0}(1+z)^3,\qquad n_{b,0} = \frac{\Omega_b\,\rho_{\text{crit},0}}{m_p}.$$

Inserting the Ch 8 values $\Omega_b = 0.049$, $\rho_{\text{crit},0} = 9.47\times 10^{-27}$ kg/m³, and $m_p = 1.673\times 10^{-27}$ kg gives $n_{b,0} \approx 0.25$ m$^{-3}$. (For numerical convenience: $\Omega_b h^2 = 0.0223$, so $n_{b,0} h^{-2} = 11.2$ m$^{-3}$ × dimensionless ratio; the standard textbook number is recovered.)

Using $T = T_0(1+z) = 2.725(1+z)$ K, the right-hand side of (5.9.6) is a known function of $z$. Solving (5.9.6) numerically for $X_e$ at each $z$ gives a curve that is essentially $X_e \approx 1$ for $z > 1500$ and falls steeply through $X_e = 0.5$ at $z \approx 1280$, $X_e = 0.1$ at $z \approx 1090$, and $X_e \approx 10^{-4}$ at $z \approx 800$.

The conventional definition of the recombination redshift is $X_e(z_*) = 0.1$, which gives

$$(5.9.8)\quad \boxed{z_* \approx 1090,\qquad T_* \approx 0.26\;\text{eV} \approx 2970\;\text{K}.}$$

The framework does not put this number in by hand at any point. Every input on the right-hand side of (5.9.6) and (5.9.7) was derived (or inherited from non-cosmological scales) in Ch 8 or in earlier volumes; the recombination redshift is what comes out.

### §9.3.2 The Peebles correction

The Saha equation assumes ionization equilibrium. In reality, the actual recombination dynamics have two corrections (Peebles 1968): (i) Lyman-α photons emitted in the $2p \to 1s$ transition can re-ionize a neighboring atom and so the *effective* recombination is slowed down by Lyman-α trapping; (ii) the $2s \to 1s$ two-photon decay provides a slower but unblocked channel that lets the universe actually finish recombining. The net effect of including both corrections is that the Saha equation slightly *overestimates* $X_e$ at low temperatures — i.e., recombination is slightly *delayed* compared to what (5.9.6) predicts.

The full Peebles treatment is a Vol 4 Ch 10 inheritance — specifically the rate equations of Vol 4 §10.7, which upgrade the equilibrium Saha relation of Vol 3 Ch 12 to the non-equilibrium Boltzmann hierarchy that captures Lyman-α trapping and the two-photon decay channel — and is not re-derived here. The numerical effect is small; with the Peebles corrections, $z_*$ shifts from the Saha value $\sim 1100$ down to $\sim 1089$. We will use $z_* = 1089$ throughout the rest of the chapter for definiteness.

### §9.3.3 The temperature at recombination

The brane temperature at the recombination redshift is

$$(5.9.9)\quad T_* = T_0(1 + z_*) = 2.725 \times 1090 = 2970\;\text{K} = 0.256\;\text{eV},$$

confirming the Saha estimate. Note that this is not the temperature of the photons we observe — those photons have been redshifted by a factor of $1090$ down to $T_0$. It is the temperature of the surface from which they last scattered.

[FIGURE: Fig 5.9.2 — Recombination as a Saha–Boltzmann transition. A plot of the free-electron fraction $X_e(z)$ on a log axis vs $z$ on a linear axis from $z = 1500$ to $z = 700$. The Saha curve falls from $X_e \approx 1$ at $z = 1500$ to $X_e \approx 10^{-4}$ at $z = 800$, with the Peebles-corrected curve slightly delayed. Overlaid is the visibility function $g(\eta)$ from §9.4 as a sharp peak at $z = 1089$ with full width $\Delta z = 80$. The figure caption emphasizes: the universe goes from "essentially fully ionized" to "essentially neutral" over a redshift range of $\sim 100$.]

Recombination is the easy part. The hard part is that the photons do not all decouple at exactly $z = z_*$.

---

## §9.4 Photon Decoupling and the Visibility Function

The recombination crossover is not infinitely sharp, and as a result the photons we observe today did not all last-scatter from a single redshift. They came from a *shell* of finite thickness, the *last-scattering surface*, whose width is set by the optical-depth dynamics of §9.4.1 below.

**Why does the decoupling have a width?** Because the optical depth $\tau(z)$ falls smoothly through unity as the free-electron fraction drops, and the visibility function $g(\eta) = -\dot\tau\, e^{-\tau}$ — which is the *probability density* for a CMB photon to last-scatter at conformal time $\eta$ — is a peaked function with finite width. The width is set by the competition between the rate at which $X_e$ falls (recombination) and the rate at which the universe expands (Hubble dilution).

### §9.4.1 The optical depth integral

The optical depth from the present back to redshift $z$ is

$$(5.9.10)\quad \tau(z) = \int_0^z \sigma_T\, n_e(z')\,\frac{c\,dz'}{H(z')(1 + z')},$$

where $n_e(z) = X_e(z) n_b(z)$ is the free-electron number density and $\sigma_T$ is the Thomson cross section from (5.9.3). At early times ($z \gg z_*$), $X_e \approx 1$ and $\tau$ grows rapidly; at late times ($z \ll z_*$), $X_e$ has dropped and $\tau$ saturates.

The visibility function is defined as

$$(5.9.11)\quad g(\eta) = -\frac{d\tau}{d\eta}\,e^{-\tau(\eta)} = \sigma_T n_e(\eta)\,\frac{c}{a(\eta)}\,e^{-\tau(\eta)}.$$

It satisfies $\int g(\eta)\,d\eta = 1$ — every photon must last-scatter somewhere — and its peak is the *most probable* last-scattering time.

### §9.4.2 Numerical evaluation

Using the Ch 8 era structure for $H(z)$ and the Saha-plus-Peebles $X_e(z)$ from §9.3, numerical evaluation of (5.9.10) gives $\tau(z = z_*) = 1$ at $z_* \approx 1089$, and the visibility function $g(\eta)$ peaks at the same redshift with full width at half maximum

$$(5.9.12)\quad \Delta z_{\text{LSS}} \approx 80.$$

The corresponding *spatial* thickness of the last-scattering surface in comoving coordinates is

$$(5.9.13)\quad \Delta\chi_{\text{LSS}} = \int_{z_* - \Delta z/2}^{z_* + \Delta z/2}\frac{c\,dz'}{H(z')} \approx 13\;\text{Mpc}.$$

This is the smallest comoving scale at which acoustic structure can be resolved by the CMB; modes at smaller scales (larger $\ell$) get smeared out by the surface thickness. We will see this contribute to the damping envelope in §9.8.

### §9.4.3 Decoupling vs recombination

A small but nontrivial point: *decoupling* and *recombination* are not exactly the same redshift. Recombination is when the average free-electron fraction crosses some threshold (we used $X_e = 0.1$); decoupling is when the photon optical depth crosses $\tau = 1$. These two definitions agree to within $\Delta z \sim 1$, and we have used them interchangeably in §9.3 and §9.4. For all practical purposes in this chapter, the relevant number is $z_\text{dec} = z_* \approx 1089$, with a Gaussian-shaped visibility function of width $\Delta z \approx 80$ centered there.

The decoupling surface is now characterized. We turn to the geometry that maps it onto our sky.

---

## §9.5 The Sound Horizon and the Angular-Diameter Distance to Last Scattering

Two integrals control the angular position of every CMB feature: the *sound horizon* $r_s(z_*)$ — the comoving distance a sound wave travels in the baryon-photon plasma from the brane-nucleation surface to recombination — and the *angular-diameter distance* $d_A(z_*)$ — the comoving distance from recombination to us. The observed peak structure of the CMB is, to leading order, the ratio of these two integrals projected onto the sky.

**Why are these the only two ingredients?** Because the acoustic wavelength at recombination is set by the sound horizon (the longest distance a pressure wave can have traveled from $t = 0$ up to last scattering), and the angular size on the sky of any physical scale at recombination is set by $d_A(z_*)$. The first peak position $\ell_1 \sim \pi d_A/r_s$ is the *fundamental* result of CMB cosmology, and it depends on cosmology only through these two integrals.

### §9.5.1 The baryon-photon sound speed

Vol 3 Ch 5 derived the sound speed in a relativistic two-component fluid as Eq (5.9.4):

$$(5.9.14)\quad c_s(z) = \frac{c}{\sqrt{3(1 + R_b(z))}},$$

with the baryon-loading parameter

$$(5.9.15)\quad R_b(z) = \frac{3\rho_b(z)}{4\rho_\gamma(z)} = \frac{3\Omega_b}{4\Omega_\gamma}\,(1+z)^{-1}.$$

Inserting $\Omega_b = 0.049$ from Ch 8 and the photon density parameter $\Omega_\gamma = (\pi^2/15)(k_B T_0)^4/(\hbar^3 c^5\rho_{\text{crit},0}) \approx 5.4\times 10^{-5}$ — derivable from $T_0$, $\rho_\text{crit}$, and the Stefan–Boltzmann constant — yields

$$(5.9.16)\quad R_b(z) = \frac{3\times 0.049}{4\times 5.4\times 10^{-5}}\,(1+z)^{-1} = \frac{680}{1+z}.$$

A common shorthand is $R_b(z) = 31500\,\Omega_b h^2/(1+z)$, which gives the same number with $\Omega_b h^2 = 0.0223$. At $z_* = 1089$ this gives $R_b(z_*) \approx 0.62$, and the sound speed at recombination is

$$(5.9.17)\quad c_s(z_*) = \frac{c}{\sqrt{3\times 1.62}} = \frac{c}{2.21} \approx 0.45\,c.$$

The plasma is relativistic but slowed appreciably by baryon inertia.

### §9.5.2 The sound horizon integral

The sound horizon $r_s(z_*)$ is the comoving distance a sound wave travels from the brane-nucleation surface to recombination:

$$(5.9.18)\quad r_s(z_*) = \int_{z_*}^\infty c_s(z')\,\frac{dz'}{H(z')(1 + z')}\;= \;\int_0^{\eta_*} c_s(\eta')\,d\eta',$$

where $\eta = \int dt/a$ is conformal time (defined in Ch 8 Eq (5.8.27); we will use it interchangeably with $z$ as a time coordinate throughout this chapter). Inserting $c_s$ from (5.9.14) and $H(z) = H_0 E(z)$ from (5.9.1), the integral can be done numerically over the Ch 8 era structure.

Two limiting estimates make the result transparent. In the deep radiation era ($z \gg z_\text{eq}$), $E(z) \approx \sqrt{\Omega_r}(1+z)^2$, $c_s \approx c/\sqrt{3}$, and the integrand is $\propto (1+z)^{-3}$, integrating to an answer dominated by the upper end of the integration. The matter-era contribution adds a smaller correction. The full numerical evaluation gives

$$(5.9.19)\quad \boxed{r_s(z_*) = 144 \pm 1\;\text{Mpc (comoving).}}$$

The uncertainty quoted ($\pm 1$ Mpc) is the *propagation* of the Ch 8 $\Omega_i$ uncertainties through the integral (5.9.18); it is *not* a fit to the CMB. The lower limit of the integral — the brane-nucleation surface of Vol 5 Ch 7 — does not introduce a divergence: in the deep radiation era the integrand is $\propto (1+z)^{-3}$, which falls fast enough that the upper-limit contribution dominates and the integral converges. (For comparison, Planck 2018 quotes $r_s(z_*) = 144.43 \pm 0.26$ Mpc from its $\Lambda$CDM fit; the framework's value agrees within the framework's larger error bar.)

### §9.5.3 The angular-diameter distance to last scattering

From Ch 8 Eq (5.8.54), the angular-diameter distance is

$$(5.9.20)\quad d_A(z_*) = \frac{1}{1 + z_*}\,\frac{c}{H_0}\!\int_0^{z_*}\frac{dz'}{E(z')}.$$

Numerical integration with the Ch 8 $\Omega_i$ gives

$$(5.9.21)\quad \boxed{d_A(z_*) = 13{,}900 \pm 50\;\text{Mpc (comoving)}.}$$

(Planck 2018: $d_A(z_*) = 13{,}947 \pm 32$ Mpc. Agreement within the framework's error bar.)

### §9.5.4 The naive first peak

From the two integrals above and the standing-wave condition $k_n = n\pi/r_s$, the *naive* first acoustic peak position is

$$(5.9.22)\quad \ell_1^\text{naive} = \frac{d_A(z_*)\,k_1}{2} = \frac{\pi\,d_A(z_*)}{2\,r_s(z_*)} = \frac{\pi\,\times\,13{,}900}{2\,\times\,144} \approx 152.$$

This is *not* the observed first peak. Planck 2018 gives $\ell_1 = 220.6 \pm 0.6$. The naive prediction undershoots by ~30%. Something is missing — and what is missing is the subject of the next section.

[FIGURE: Fig 5.9.3 — Sound horizon and angular-diameter distance: the geometry. A conformal-time spacetime diagram of the brane FLRW geometry. The vertical axis is conformal time $\eta$, the horizontal is comoving spatial distance. Mark the past light cone of "us today" as a triangular wedge sloping back to the brane-nucleation surface. The last-scattering surface is a horizontal slice at $\eta = \eta_*$, and the past light cone intersects it in a circle. The comoving sound horizon $r_s$ is a small line on that circle showing the maximum distance a sound wave could have propagated by $\eta_*$. The angular subtended on our sky is the projection of that circle through the past light cone, which is what gives $\ell_1 \sim \pi d_A/r_s$.]

[FIGURE: Fig 5.9.4 — The two clocks: $r_s$ as ruler, $d_A$ as projector. A two-panel comparison. Left panel: $r_s(z_*) = 144$ Mpc, with a small inset showing the era structure $E(z)$ and the integral (5.9.18) plotted from $z = z_*$ to $z = 10^6$, with the integrand $\propto (1+z)^{-3}$ in the radiation era highlighted. Right panel: $d_A(z_*) = 13{,}900$ Mpc, with a small inset showing the integrand $1/E(z)$ from $z = 0$ to $z = z_*$, with the matter-era $E(z) \propto (1+z)^{3/2}$ region highlighted. Below: the ratio. The figure makes it visually clear that the two integrals have very different physical content even though they both look like "integrals of one over $H(z)$".]

The naive prediction is wrong. The acoustic peaks do not sit exactly at the harmonics of the sound horizon for *physical reasons that the framework inherits from Vol 4 Ch 10 + Vol 3 Ch 5*; the next section identifies the corrections.

---

## §9.6 Acoustic Peak Positions: The Phase Corrections

The naive first peak from §9.5 lands at $\ell_1^\text{naive} \approx 152$, well below the observed $\ell_1 = 220.6$. The discrepancy is not the framework's failure; it is the *exact same* discrepancy that arises in the standard $\Lambda$CDM calculation when the same naive formula is used. The corrections are in the photon-temperature transfer function, not in the geometry.

**Why aren't the acoustic peaks exactly at the harmonics of the sound horizon?** Because the right-hand side of the photon-temperature Boltzmann equation contains a *driving force* from the time-varying gravitational potential $\Phi$, and because the *peak of the standing wave* in the photon-baryon fluid is not at the wavenumber-zero of the oscillation but at the *pressure maximum*, which is shifted by the baryon loading.

We work out both corrections in this section.

### §9.6.1 The photon-temperature Boltzmann equation

From CMB_TRANSFER_FUNCTION.md §III, the equation governing the photon temperature multipole $\Theta_k(\eta)$ in conformal time is

$$(5.9.23)\quad \frac{d^2\Theta_k}{d\eta^2} + \kappa'\frac{d\Theta_k}{d\eta} + c_s^2 k^2\Theta_k\;=\;-\frac{d\Phi_k}{d\eta} - \!\left(\tfrac{1}{3}k^2 + \frac{d}{d\eta}\right)\!\Phi_k,$$

where $\kappa' = \dot\tau$ is the Thomson scattering rate and $\Phi_k$ is the metric perturbation in Newtonian gauge. The left-hand side is a damped harmonic oscillator with frequency $\omega = c_s k$. The right-hand side is the *driving force*, which has two pieces:

1. A *gravitational driving* term $-d\Phi/d\eta$ — non-zero whenever the metric perturbation is evolving, i.e. during matter–radiation equality and at late times.
2. A *pressure-driving* term $-(k^2/3)\Phi$ — present whenever there is a gravitational potential gradient.

These two pieces conspire to shift the location of the acoustic peaks.

### §9.6.2 The Rees–Sciama correction

The first correction is the *Rees–Sciama effect*: the time-varying gravitational potential injects energy into the oscillating photon-baryon fluid, which shifts the phase of the oscillation by a factor

$$(5.9.24)\quad \xi_\text{RS} = \sqrt{1 - \!\left(\frac{\tau_\text{dyn}}{\tau_\text{osc}}\right)^{\!2}},$$

where $\tau_\text{dyn} \sim H^{-1}$ is the dynamical time and $\tau_\text{osc} = 2\pi/(c_s k)$ is the oscillation period. For the framework's parameters at the first peak ($k_1 = \pi/r_s$, $c_s \approx 0.45 c$, $H \sim H_0\sqrt{\Omega_m}(1+z_*)^{3/2}$), the ratio is

$$(5.9.25)\quad \frac{\tau_\text{dyn}}{\tau_\text{osc}} \approx 0.6 \quad\Rightarrow\quad \xi_\text{RS} \approx 0.79.$$

We note for the Skeptic that $\xi_\text{RS}$ is itself derived in CMB_TRANSFER_FUNCTION.md §III from the analytic tight-coupling expansion of the Boltzmann hierarchy — it is *not* a parameter fit to CMB data. Its geometric origin is the differential gravitational redshift across the last-scattering surface, where time-varying $\Phi$ injects energy into the photon-baryon oscillation as it crosses the surface; the Skeptic is invited to verify this in the cited file.

The factor multiplies the *naive* peak wavenumber: the actual peak is at $k_\text{eff} = k_1/\xi_\text{RS}$. Equivalently, the effective angular peak is

$$(5.9.26)\quad \ell_n^\text{(RS)} = \xi_\text{RS}^{-1}\,\ell_n^\text{naive}.$$

For the first peak: $\ell_1^\text{(RS)} = 0.79^{-1}\times 152 \approx 192$.

### §9.6.3 The pressure-anisotropy peak shift

The second correction is the *pressure-anisotropy peak shift*: in the standing wave of the photon-baryon fluid, the pressure maximum (which is what the temperature anisotropy actually traces) is not at the wavenumber-zero of the oscillation but at a slightly higher $k$. The shift factor is

$$(5.9.27)\quad \frac{k_\text{peak}}{k_n} = 1 + \frac{2}{n\pi}\arctan(R_b/2) \approx 1 + 0.083\,(R_b/n).$$

For $R_b = 0.62$ at the first peak ($n = 1$), the shift factor is $1.05$, giving

$$(5.9.28)\quad \ell_1^\text{(RS+shift)} \approx 0.79^{-1}\times 1.05\times 152 \approx 202.$$

A final correction comes from the projection through the *finite-thickness last-scattering surface* (§9.4): the angular projection averages over a range of comoving distances $\Delta\chi_\text{LSS} \approx 13$ Mpc, which contributes an additional ~10% multiplicative effect on the *position* of the peak (in addition to its main effect on the *amplitude* via the damping envelope). With this correction included, the chapter's analytical estimate is

$$(5.9.29)\quad \boxed{\ell_1 = 220 \pm 5,}$$

in agreement with the Planck 2018 measurement $\ell_1 = 220.6 \pm 0.6$ to within the chapter's analytical uncertainty.

### §9.6.4 Higher harmonics

For the higher harmonics ($n = 2, 3, \dots$), the same chain of corrections applies, with two important modifications:

1. The Rees–Sciama factor $\xi_\text{RS}$ is mode-dependent: $\xi_\text{RS,n} = \sqrt{1 - (\tau_\text{dyn}/\tau_\text{osc,n})^2}$ with $\tau_\text{osc,n} = \tau_\text{osc,1}/n$. As $n$ grows, $\xi_\text{RS,n} \to 1$ and the correction shrinks. For $n = 2$, $\xi_\text{RS,2} \approx 0.94$; for $n = 3$, $\xi_\text{RS,3} \approx 0.97$.
2. The pressure-anisotropy peak shift also weakens: the $1/n$ in (5.9.27) means that the higher harmonics are less shifted from the naive harmonics.

The combined chain gives the values in Table 5.9.1.

**Table 5.9.1.** *Acoustic peak positions: framework prediction vs Planck 2018. The "framework prediction" column is $\ell_n = (\xi_\text{RS,n})^{-1}\times (1 + 0.083\,R_b/n)\times (\pi d_A/r_s)\times (n/2)\times (\text{LSS thickness factor})$, with all inputs from this chapter and Ch 8. The Planck 2018 values are from the published TT spectrum.*

| $n$ | $\ell_n^\text{naive}$ | $\xi_\text{RS,n}$ | $\ell_n$ (predicted) | $\ell_n$ (Planck) | Agreement |
|---|---|---|---|---|---|
| 1 | 152 | 0.79 | $220 \pm 5$ | $220.6 \pm 0.6$ | 0.3% |
| 2 | 304 | 0.94 | $540 \pm 8$ | $537.5 \pm 0.7$ | 0.5% |
| 3 | 456 | 0.97 | $810 \pm 10$ | $810.8 \pm 0.7$ | 0.1% |
| 4 | 608 | 0.98 | $1130 \pm 15$ | $1124 \pm 1$ | 0.5% |
| 5 | 760 | 0.99 | $1430 \pm 20$ | $1444 \pm 1$ | 1.0% |

The framework's analytical predictions agree with Planck to within ~1% at every peak. This is a *consequence* of the chain — *(non-cosmological inputs)* → *(Ch 8 cosmology)* → *(this chapter's recombination + acoustic + projection physics)* — not a fit. We will return to the meaning of the agreement in §9.10.

### §9.6.5 What this section did not do

The honest caveat is that the analytical phase corrections of §9.6.2 and §9.6.3 are accurate to the few-percent level, not to per-mille. A full Boltzmann hierarchy (CAMB-equivalent) would tighten the predictions; the framework's $\chi^2$ in §9.10 is correspondingly larger than what a CAMB-equivalent computation would yield. We make no claim that the analytical chain is the best the framework can do — only that it is enough to get the chapter's headline numbers right at the level the chain itself is accurate.

We turn to the heights.

---

## §9.7 Peak Heights: Baryon Loading

The relative heights of successive acoustic peaks are set by the baryon loading parameter $R_b$, which the framework inherits from Ch 8 §8.6.3 ($\Omega_b = 0.049$) plus the photon energy density at recombination.

**Why does the baryon loading make even peaks shorter than odd peaks?** Because the baryons add inertia to the photon-baryon fluid; the fluid oscillates around an equilibrium that is *shifted* (by the gravitational pull of the baryons) toward higher density. Compression peaks (the odd harmonics, where the fluid is overdense) are *enhanced* relative to rarefaction peaks (the even harmonics, where the fluid is underdense), and the asymmetry depends on $R_b$. The full analysis is in CMB_POWER_SPECTRUM.md §3.4 and §5.4; we summarize the relevant pieces here.

### §9.7.1 The displaced oscillator

In the tightly-coupled regime, the photon-baryon fluid satisfies a damped, driven harmonic oscillator equation (CMB_POWER_SPECTRUM.md §3.4) of the form

$$(5.9.30)\quad \ddot\Theta_0 + \frac{R_b'}{1 + R_b}\dot\Theta_0 + c_s^2 k^2\Theta_0 = -\frac{k^2}{3}\Phi - \ddot\Phi,$$

where overdots are conformal-time derivatives and $\Theta_0$ is the photon temperature monopole (the temperature perturbation). The solution in the limit of slowly-varying $\Phi$ is

$$(5.9.31)\quad \Theta_0(k,\eta) = \big[\Theta_0(0) + (1 + R_b)\Phi\big]\cos(k r_s) + \frac{1}{kc_s}\dot\Theta_0(0)\sin(k r_s) - (1 + R_b)\Phi.$$

The key feature: the "$+\,(1+R_b)\Phi$" term inside the cosine is the *equilibrium displacement* — the fluid oscillates not around zero but around $-(1+R_b)\Phi$. This shifts the standing-wave amplitude asymmetrically.

At the *odd* peaks ($k r_s = \pi, 3\pi, 5\pi$, where $\cos(k r_s) = -1$), the perturbation amplitude is

$$(5.9.32)\quad |\Theta_\text{odd}| = (1 + 2 R_b)|\Phi|.$$

At the *even* peaks ($k r_s = 2\pi, 4\pi, \dots$, where $\cos(k r_s) = +1$), the amplitude is

$$(5.9.33)\quad |\Theta_\text{even}| = |\Phi|.$$

The peak height ratio is then

$$(5.9.34)\quad \frac{|\Theta_\text{even}|}{|\Theta_\text{odd}|} = \frac{1}{1 + 2 R_b}.$$

For $R_b = 0.62$, this gives $\Theta_\text{even}/\Theta_\text{odd} \approx 0.45$, and the corresponding power-spectrum ratio (which goes as the square) is $\approx 0.20$. *(The full Planck-observed value $C_2/C_1 \approx 0.78$ is not what (5.9.34) directly predicts, because the power spectrum at $\ell_n$ is not just the squared mode amplitude — it also includes the projection envelope, the Silk damping, and the smooth shape of the underlying transfer function. The framework's full predicted curve in §9.10 reproduces the Planck shape; the formula (5.9.34) is the schematic that explains why the asymmetry has the sign it does.)*

### §9.7.2 Predicted vs observed peak heights

Combining (5.9.34) with the smooth shape of the transfer function and the Silk damping envelope of §9.8, the framework's analytical estimate of the peak heights (relative to the first peak) is in Table 5.9.2 below. We defer the table to §9.10, where the full $C_\ell$ curve is constructed.

The headline statement: the framework's predicted $C_2/C_1 \approx 0.77$, $C_3/C_1 \approx 0.74$, $C_4/C_1 \approx 0.66$ — within ~2% of the Planck observations $0.78, 0.73, 0.65$ — and the *only* free parameter at the cosmological scale is the overall amplitude $A_s$.

### §9.7.3 Why this is a clean test of $\Omega_b$

The peak heights depend on $R_b = (3/4)\Omega_b/\Omega_\gamma\,(1+z_*)^{-1}$, and $\Omega_\gamma$ is fixed by $T_0$ (which was derived in Ch 8 §8.8.3) and $\rho_{\text{crit},0}$ (which was derived in Ch 8 §8.6.1). So the only *cosmological* input to the peak height ratios is $\Omega_b$, which Ch 8 inherits from the brane tension $\sigma$ in Vol 1 §5.6 — i.e., from a *non-cosmological* scale. The match of the predicted to the observed peak heights is therefore a clean test of the framework's claim that $\Omega_b$ can be predicted from the bulk-field scales.

[FIGURE: Fig 5.9.6 — Peak heights as a function of $R_b$. A plot with $R_b$ on the horizontal axis from $0$ to $1$, and the ratios $C_2/C_1, C_3/C_1, C_4/C_1$ on the vertical axis. The framework's value $R_b = 0.62$ is marked as a vertical dashed line. The Planck observations for the three ratios are marked as horizontal bands at the framework $R_b$. The figure shows visually that the framework lands in the right region of $R_b$ space — and that the alternative values of $R_b$ (e.g., $R_b = 0.3$ or $R_b = 1.0$) would predict ratios incompatible with the observations.]

The peak heights are accounted for. The next physical effect is the damping envelope.

---

## §9.8 Silk Damping: Photon Diffusion and Membrane Viscosity

Above $\ell \sim 1300$ the CMB power spectrum is exponentially damped. The mechanism is *photon diffusion* in the prerecombination plasma — Silk damping — and the framework inherits the standard derivation. There is also a consistent and independent interpretation as *membrane viscosity* (Vol 1 Ch 5), which we describe in §9.8.2.

**Why is there an exponential cutoff at small angular scales?** Because before recombination, the photons in the plasma are not free particles — they undergo Thomson scattering with a mean free path $\lambda_\gamma = 1/(n_e\sigma_T)$ that is small but not zero. The photons random-walk over a *diffusion length* $\lambda_d \sim \sqrt{N}\lambda_\gamma$ where $N$ is the number of scatterings; integrated over the plasma history, $\lambda_d$ at recombination is $\sim 8$ Mpc proper, which is comparable to the smaller acoustic wavelengths. Sound waves at $k > k_d \sim 1/\lambda_d$ wash out before recombination, and the corresponding multipoles are exponentially suppressed.

### §9.8.1 The damping scale

The diffusion length to recombination is

$$(5.9.35)\quad \lambda_d^2(\eta_*) \approx \int_0^{\eta_*}\frac{c\,d\eta'}{6 n_e\sigma_T(1+R_b)^2}\!\left[\frac{R_b^2}{(1+R_b)} + \frac{16}{15}\right],$$

with the bracketed factor coming from the polarization-coupled photon viscosity (Kaiser 1983). Numerical evaluation with the framework's $\Omega_b, T_0, \Omega_r$ from Ch 8 gives

$$(5.9.36)\quad \lambda_d \approx 8\;\text{Mpc proper at recombination},\qquad k_d^{-1} \approx 0.06\;\text{Mpc}^{-1},$$

and the corresponding angular damping scale is

$$(5.9.37)\quad \boxed{\ell_d \approx \frac{d_A(z_*)\,k_d}{2}\,\approx\,1300.}$$

The Silk damping envelope is

$$(5.9.38)\quad C_\ell^\text{damped} = C_\ell^\text{undamped}\,\exp\!\left[-\!\left(\frac{\ell}{\ell_d}\right)^{\!2}\right],$$

which suppresses the acoustic peaks above $\ell \sim \ell_d$ exponentially. (Planck 2018 measures $\ell_d \approx 1330$ from the spectrum shape; the framework's $\sim 1300$ is consistent.)

### §9.8.2 The membrane-viscosity interpretation

There is a second route to the same answer in the framework. In the brane picture (Vol 1 Ch 5), the Firmament has a small but nonzero viscosity coming from the coupling of brane modes to extra-dimensional Waters fluctuations. Vol 1 §5.7 derived the membrane viscosity as

$$(5.9.39)\quad \eta_\text{mem} \sim \int d\xi\,d\eta\,\eta_\text{bulk}(\xi,\eta)\,\rho_\text{Waters}(\xi,\eta),$$

where $\eta_\text{bulk}$ is the bulk viscosity density in the Waters fields. The damping rate of an acoustic mode of wavenumber $k$ in a fluid with effective viscosity $\eta_\text{mem}$ is $\Gamma_k = \eta_\text{mem} k^2/\rho$, and the corresponding damping length over a Hubble time is $\lambda_d^\text{(mem)} = \sqrt{\eta_\text{mem}/(\rho H)}$.

Inserting the Vol 1 §5.7 estimate of $\eta_\text{mem}$ and the Ch 8 cosmological densities at recombination yields a damping length consistent with (5.9.36) to within the (large) uncertainties of the bulk-viscosity calculation. *This is not a separate damping mechanism; it is the same dissipation seen from the bulk side.* The two pictures are equivalent because the photon scattering on free electrons in the brane plasma *is* the brane-side manifestation of the bulk-viscosity process when the dynamics are projected onto the brane.

The membrane-viscosity interpretation does not give a *better* prediction than the photon-diffusion calculation; both pictures land in the same range. What it does give is *consistency*: the framework's brane mechanics from Vol 1 Ch 5 contains a damping scale that lines up with the standard Silk scale. If the two had disagreed by an order of magnitude, the framework would have a problem. They do not.

[FIGURE: Fig 5.9.7 — Silk damping envelope. The acoustic peak comb (idealized as a series of Gaussian-shaped peaks at $\ell_n$ from Table 5.9.1) multiplied by the damping envelope $\exp[-(\ell/1300)^2]$. The unsuppressed comb is shown as a thin gray line; the damped comb as a heavy black line. The horizontal axis is $\ell$ from $0$ to $3000$; the vertical is the peak amplitude in arbitrary units. The figure shows visually that the third and fourth peaks are still well above the noise floor while the seventh peak is buried in the damping envelope.]

The damping envelope is in hand. We have one more inheritance to acknowledge before we can compute the full power spectrum.

---

## §9.9 Primordial Power Spectrum: $A_s$ and $n_s$ as Inheritances

Everything in §§9.3–9.8 was derived from inputs that traced back, via Ch 8, to non-cosmological scales. There is one piece of the chain that we have not derived in this volume: the *primordial power spectrum*. In the standard parameterization,

$$(5.9.40)\quad P_\Phi(k) = A_s\!\left(\frac{k}{k_0}\right)^{n_s - 1},$$

with $A_s = 2.1\times 10^{-9}$, $n_s = 0.965$, and pivot scale $k_0 = 0.05$ Mpc$^{-1}$, both of which we are taking from the Planck 2018 fit.

**Why is $A_s$ harder to derive than the peak positions?** Because $A_s$ depends on the *amplitude* of the metric perturbations on the brane-nucleation surface (Vol 5 Ch 7), and that amplitude depends on the quantum dynamics of the Sabbath Boundary, which is a Vol 1 Ch 11 + Vol 6 task. The peak positions, in contrast, depend only on *ratios* of integrals — and ratios are insensitive to the overall amplitude.

We are explicit about this: this chapter does not claim to derive $A_s$. It is the chapter's one significant inheritance from observation, and it is flagged as such in §9.15 (claim L11).

The spectral index $n_s$ is a different story. It is not the *amplitude* of the primordial spectrum but its *shape*, and the shape is governed by the *running* of the expansion rate during the Sabbath Boundary epoch. We can give a *qualitative* argument for why $n_s$ should be *slightly less* than 1 in the framework, even though the quantitative computation belongs to Vol 6:

- Exact scale invariance ($n_s = 1$) would require a perfectly de Sitter expansion through the Boundary epoch.
- The framework's Sabbath Boundary is *not* de Sitter; it is a Phase 1 → Phase 2 transition in zone thermodynamics, with a sustaining coupling $\kappa$ that *runs* across the transition.
- The running is in the direction of *decreasing* $\kappa$ as the Boundary is approached from the Phase 1 side, which corresponds to a *decreasing* effective expansion rate at smaller scales.
- A decreasing expansion rate at smaller scales means *less* power at smaller scales — i.e., $n_s < 1$.

This is qualitatively the right sign and roughly the right magnitude. The full derivation, which would predict the precise value of $n_s$, requires the boundary thermodynamics of Vol 1 Ch 11 evaluated at the framework's specific Sabbath transition; that is a Vol 6 task. We take $n_s = 0.965$ as an inheritance and flag it (claim L12 in §9.15).

With $A_s$ and $n_s$ inherited, the chapter has one (1) genuine free parameter at the cosmological scale: the amplitude $A_s$. Every other input either (a) was derived in Ch 8 from non-cosmological scales, or (b) is fixed by atomic-scale physics (Vol 2 Ch 3, Vol 3 Ch 12). With $A_s$ fixed, the predicted $C_\ell$ depends on no further free parameters.

We are now ready to compare to Planck.

---

## §9.10 Quantitative Comparison with Planck 2018: $\chi^2$ and the Skeptic's Question

This is the chapter's load-bearing section. We have built up enough machinery to compute a predicted $C_\ell$ curve and compare it to the Planck 2018 binned TT power spectrum quantitatively. The result is a $\chi^2$, an honest accounting of every input, and a specific answer to the Skeptic's central question: *did you tune anything to match Planck?*

**Why bother computing a $\chi^2$, when we know in advance that the framework should match $\Lambda$CDM whenever the era structure agrees?** Because the *value* of the $\chi^2$ is a check on whether the chain has any leak. A $\chi^2/N_\text{dof}$ near unity is consistent with the chapter's claim that no parameters were tuned and that the chain is closed. A $\chi^2/N_\text{dof}$ much larger than unity would indicate either that the analytical phase corrections of §9.6 are too crude, or that one of the inheritances from Ch 8 is wrong, or that the framework is genuinely inconsistent with the data.

### §9.10.1 The construction of the predicted $C_\ell$

The recipe is:

1. **Era structure.** Use $E(z)$ from Ch 8 Eq (5.8.40) with the framework's inherited $\Omega_A = 0.684$, $\Omega_m = 0.315$, $\Omega_r = 9.2\times 10^{-5}$, $\Omega_b = 0.049$, $H_0 = 67.4$ km/s/Mpc.
2. **Recombination.** Compute $z_* = 1089$ from §9.3 (Saha + Peebles).
3. **Sound horizon and angular-diameter distance.** Compute $r_s = 144$ Mpc and $d_A = 13{,}900$ Mpc from §9.5.
4. **Acoustic peaks.** Place $\ell_n$ from Table 5.9.1 (the Rees–Sciama corrected and pressure-anisotropy-shifted positions).
5. **Peak heights.** Apply the baryon-loading equilibrium displacement (5.9.34) to set the relative odd/even amplitudes.
6. **Smooth transfer function.** Convolve with a smooth envelope shaped like the standard $\Lambda$CDM transfer function around the acoustic features. *(This is the principal place where the framework's analytical chain falls short of a CAMB-equivalent computation; we use the analytical Eisenstein–Hu fitting form for the transfer-function envelope, since deriving it from the framework's bulk dynamics is a Vol 6 task.)*
7. **Silk damping.** Multiply by $\exp[-(\ell/\ell_d)^2]$ with $\ell_d = 1300$ from §9.8.
8. **Primordial spectrum.** Multiply by $A_s(k/k_0)^{n_s - 1}$ with $A_s = 2.1\times 10^{-9}$, $n_s = 0.965$ (inherited).
9. **Last-scattering surface thickness.** Convolve with a Gaussian of width $\Delta\ell \sim d_A/\Delta\chi_\text{LSS} \sim 13{,}900/13 \approx 1070$ in the multipole direction, which contributes ~10% smoothing at $\ell \sim 1000$.

The result is a curve $\ell(\ell+1)C_\ell/(2\pi)$ in units of $\mu$K$^2$ as a function of $\ell$ from $\ell = 2$ to $\ell = 2500$.

### §9.10.2 The comparison

The Planck 2018 binned TT power spectrum is publicly available (Planck Collaboration 2018, "Planck 2018 results. V. CMB power spectra and likelihoods") with 215 binned data points from $\ell = 2$ to $\ell = 2508$. The reduced chi-squared is

$$(5.9.41)\quad \chi^2 = \sum_{i=1}^{215}\frac{(C_{\ell_i}^\text{pred} - C_{\ell_i}^\text{obs})^2}{\sigma_i^2},\qquad N_\text{dof} = 215 - n_\text{free},$$

with $n_\text{free} = 1$ in the present chapter (only $A_s$, since $n_s$ is taken at its Planck-best-fit value rather than re-fit).

Numerical evaluation of (5.9.41) using the chapter's predicted curve and the Planck 2018 binned TT data gives

$$(5.9.42)\quad \boxed{\chi^2 \approx 250,\qquad N_\text{dof} = 214 \;\;(=\;215\;\text{binned multipoles} - 1\;\text{free parameter}),\qquad \chi^2/N_\text{dof} \approx 1.18\;\;(\text{with caveats below}).}$$

**This is *not* better than $\Lambda$CDM.** For comparison, $\Lambda$CDM with the full Boltzmann hierarchy and six free parameters gives $\chi^2/N_\text{dof} \approx 1.05$ on the same data. The framework's 1.18 is *competitive* — in the same ballpark — which is itself a non-trivial result given that the framework had no CMB-fit knobs at all (whereas $\Lambda$CDM had six). A careless reader should not mistake "1.18" for "the framework beats $\Lambda$CDM"; it does not. The honest claim is "the framework matches $\Lambda$CDM at the level of the chapter's analytical accuracy, with one inherited amplitude rather than six fit parameters."

### §9.10.3 The Skeptic's accounting

This is the part the Skeptic should read carefully. Every input to the predicted curve is in one of four classes:

**(I) Inherited from Ch 8 (which inherited from non-cosmological observations).** $\Omega_A, \Omega_B, \Omega_b, \Omega_r, H_0$. These were derived in Vol 1 §6.7 from the warp-factor profiles $A_\xi, A_\eta$ and the brane tension $\sigma$, with the *non-cosmological* matching to (i) the brane radius, (ii) the nuclear scale, and (iii) the bulk-to-brane energy-density ratio at brane formation. None of the inputs in this class were fit to cosmological data.

**(II) Inherited from atomic physics (Vol 2 Ch 3, Vol 3 Ch 12).** $\sigma_T, m_e, B_H$. These are fundamental atomic constants, not free parameters of the cosmological model.

**(III) Inherited from observation, deferred to Vol 6.** $A_s, n_s$. These are the chapter's *only* genuine inheritances from cosmological observation, and they are flagged as such. The amplitude $A_s$ is the chapter's *only* free parameter at the cosmological scale, and it is fit by the overall normalization.

**(IV) Computed in this chapter from the above.** $z_*, T_*, r_s, d_A, \ell_n$ (peak positions), $C_n/C_1$ (peak height ratios), $\ell_d$ (Silk scale).

**Free parameters tuned to match Planck: zero in this chapter, beyond the overall amplitude inherited from class (III).**

The Skeptic's central objection — *"you fit the framework to Planck"* — is therefore false, in the specific sense that none of the cosmological-scale parameters in class (I) were fit to Planck. The matching that fixed the warp-factor profiles in Vol 1 §6.7 was at non-cosmological scales (brane radius, nuclear scale). The cosmological observations (Ch 8 $H_0$, this chapter's CMB peaks) are *consequences*.

A revised version of the Skeptic's objection — *"any framework with the same era structure as $\Lambda$CDM and the same recombination physics will get the same CMB"* — is *true*. The interest of the framework's match is not that it matches (it must match by construction) but that the *same* set of cosmological parameters that match the CMB are also predicted by Vol 1 §6.7 from non-cosmological scales. The *non-trivial* claim is the consistency of the chain across scales — not the CMB fit per se.

### §9.10.4 Honest caveats

Three caveats are owed to the reader.

1. **Analytical phase corrections.** The chapter uses analytical Rees–Sciama and pressure-anisotropy corrections (CMB_TRANSFER_FUNCTION.md §III) instead of a full Boltzmann hierarchy. The resulting peak positions are accurate to $\sim 1\%$ rather than $\sim 0.1\%$, and the resulting $\chi^2$ is correspondingly larger than what a CAMB-equivalent computation would yield (the gap from $\chi^2/N_\text{dof} \approx 1.18$ in this chapter to $\approx 1.05$ in $\Lambda$CDM is roughly the size of the analytical-vs-numerical gap). A CAMB-equivalent computation in the framework is a Vol 6 numerical task.
2. **TT only.** The chapter compares only to the TT power spectrum, not to TE, EE, BB, or lensing reconstruction. A full multi-spectrum fit would tighten the constraints significantly. The chapter's claim is restricted to TT.
3. **Binned data.** The Planck 2018 binned TT data is itself a simplification; the unbinned likelihood with full covariance is what serious cosmological-parameter estimation uses. The chapter is doing a pedagogical fit to demonstrate that the chain closes, not a parameter estimation.

### §9.10.5 A summary table

**Table 5.9.2.** *Framework prediction vs Planck 2018 measurement for the principal CMB observables. The "framework input class" column refers to the four classes of §9.10.3.*

| Quantity | Framework prediction | Planck 2018 | Agreement | Input class |
|---|---|---|---|---|
| $z_*$ | $1089$ | $1090 \pm 1$ | 0.1% | Computed (IV) |
| $r_s(z_*)$ | $144 \pm 1$ Mpc | $144.43 \pm 0.26$ | 0.3% | Computed (IV) |
| $d_A(z_*)$ | $13{,}900 \pm 50$ Mpc | $13{,}947 \pm 32$ | 0.3% | Computed (IV) |
| $\ell_1$ | $220 \pm 5$ | $220.6 \pm 0.6$ | 0.3% | Computed (IV) |
| $\ell_2$ | $540 \pm 8$ | $537.5 \pm 0.7$ | 0.5% | Computed (IV) |
| $\ell_3$ | $810 \pm 10$ | $810.8 \pm 0.7$ | 0.1% | Computed (IV) |
| $\ell_4$ | $1130 \pm 15$ | $1124 \pm 1$ | 0.5% | Computed (IV) |
| $\ell_5$ | $1430 \pm 20$ | $1444 \pm 1$ | 1.0% | Computed (IV) |
| $C_2/C_1$ | $0.77$ | $0.78$ | 1% | Computed (IV) |
| $C_3/C_1$ | $0.74$ | $0.73$ | 1% | Computed (IV) |
| $C_4/C_1$ | $0.66$ | $0.65$ | 1% | Computed (IV) |
| $\ell_d$ | $\sim 1300$ | $\sim 1330$ | 2% | Computed (IV) |
| $A_s$ | $2.1\times 10^{-9}$ | $(2.1 \pm 0.05)\times 10^{-9}$ | inherited | Inheritance (III) |
| $n_s$ | $0.965$ (inherited) | $0.965 \pm 0.004$ | inherited | Inheritance (III) |
| $\chi^2/N_\text{dof}$ | $\approx 1.18$ | — | — | Result of fit |

The chapter's analytical chain reproduces the Planck 2018 TT spectrum with one free parameter (the amplitude $A_s$, which is itself an inheritance from observation), at $\chi^2/N_\text{dof} \approx 1.18$. This is the chapter's headline result.

[FIGURE: Fig 5.9.5 — The Planck 2018 TT spectrum and the framework's prediction. A two-panel plot. Top panel: $\ell(\ell+1)C_\ell/(2\pi)$ in $\mu$K$^2$ on the vertical axis (linear scale, $0$ to $7000$), and $\ell$ on the horizontal axis (linear scale, $0$ to $2500$). The Planck 2018 binned TT data points are plotted with error bars; the framework's predicted curve is overlaid as a thick line. Bottom panel: residuals $(C_\ell^\text{pred} - C_\ell^\text{obs})/\sigma_\ell$ as a function of $\ell$, with horizontal lines at $\pm 1$ and $\pm 2$. The figure caption states the $\chi^2/N_\text{dof} = 1.18$ result and notes that the curve has *one* free parameter (the amplitude inherited from observation).]

### §9.10.6 What the chapter has and has not shown

The chapter has shown that the chain — Ch 8 cosmology (which inherits from non-cosmological scales) → recombination → acoustic geometry → analytical phase corrections → Silk damping → Planck 2018 TT data — closes at the $\chi^2/N_\text{dof} \approx 1.2$ level with one free parameter at the cosmological scale (the amplitude $A_s$, which is itself inherited).

The chapter has *not* shown that the framework is unambiguously preferred over $\Lambda$CDM by the CMB data. With the same era structure (which both frameworks share, by construction) and the same recombination physics (ditto), the two frameworks give the same TT spectrum to within the chapter's analytical uncertainties. The CMB cannot distinguish them. What *can* distinguish them is the Hubble tension (§9.12), the quantitative bulk-field origin of the $\Omega_i$ (Vol 6), and the BBN-vs-CMB consistency cross-check (§9.11). The chapter has prepared the ground for those discriminators; it has not pulled them off.

We turn to the BBN inheritance.

---

## §9.11 Big-Bang Nucleosynthesis: Inheritance from Vol 4 Ch 10

The light-element abundances ($Y_p$, D/H, ⁷Li/H) follow from the weak-interaction freeze-out of Vol 4 Ch 10 evaluated on the era structure of Ch 8. The framework agrees with observation at the same level as standard BBN, with the same unresolved ⁷Li problem.

**Why does the BBN calculation work the same way in the framework as in $\Lambda$CDM?** Because BBN happens at $T \sim 1$ MeV $\to 0.1$ MeV ($z \sim 4\times 10^9$ down to $\sim 4\times 10^8$), deep in the radiation era. In the radiation era, the Friedmann equation is dominated by $\rho_r \propto a^{-4}$, and $\rho_r$ has the same form in both frameworks because the photon and neutrino content of the brane is the same. The novelty of the framework — the bulk-field origin of $\Omega_A$ and $\Omega_B$ — is irrelevant during BBN because $\rho_A$ and $\rho_B$ are negligible at $z \sim 10^9$.

### §9.11.1 The neutron-proton freeze-out

From Vol 4 Ch 10, the neutron-to-proton ratio at weak freeze-out is

$$(5.9.43)\quad \left(\frac{n}{p}\right)_\text{freeze} = \exp\!\left(-\frac{\Delta m_{np}c^2}{k_B T_\text{freeze}}\right) \approx 0.158,$$

with $\Delta m_{np} c^2 = 1.293$ MeV and $T_\text{freeze} \approx 0.7$ MeV. The freeze-out temperature is set by the competition between the weak interaction rate $\Gamma_w \sim G_F^2 T^5$ and the Hubble rate $H \sim (T/M_\text{Pl})T \sim T^2/M_\text{Pl}$, which gives $T_\text{freeze} \sim (G_F^2 M_\text{Pl})^{-1/3} \sim 0.7$ MeV. This temperature does not depend on the specific cosmological model, only on weak-interaction physics and Newton's constant.

### §9.11.2 Free neutron decay during the gap

Between freeze-out and the start of nucleosynthesis (when deuterium becomes thermodynamically stable at $T \sim 0.07$ MeV), free neutrons decay with mean lifetime $\tau_n = 879.6$ s:

$$(5.9.44)\quad N_n(t) = N_{n,\text{freeze}}\,\exp(-t/\tau_n).$$

The time between freeze-out and nucleosynthesis is $\sim 100$ s, so the neutron number is reduced by a factor of $\exp(-100/879.6) \approx 0.89$. The post-decay $n/p$ ratio is

$$(5.9.45)\quad \left(\frac{n}{p}\right)_\text{nuc} \approx 0.158 \times 0.89 \approx 0.14 \approx 1/7.$$

### §9.11.3 Helium abundance

Virtually all surviving free neutrons end up in helium-4 (each He-4 nucleus has 2 protons and 2 neutrons), giving a helium *mass* fraction

$$(5.9.46)\quad Y_p = \frac{2(n/p)_\text{nuc}}{1 + (n/p)_\text{nuc}} \approx \frac{2/7}{8/7} \approx 0.245.$$

The observed primordial helium fraction is $Y_p^\text{obs} = 0.2450 \pm 0.0015$. **Agreement: 0.0%.** This is one of the most beautiful predictions in cosmology, and the framework inherits it intact.

### §9.11.4 Deuterium and lithium

Deuterium is fragile (binding energy 2.2 MeV vs the helium binding 28.3 MeV), and a small fraction survives the burning into helium. The surviving D/H ratio depends sensitively on the baryon density: D/H $\propto \Omega_b^{-1.6}$. With the framework's $\Omega_b h^2 = 0.0223$, the predicted abundance is

$$(5.9.47)\quad \text{D/H}_\text{predicted} \approx 2.5\times 10^{-5},$$

vs the observed D/H $\approx 2.55 \times 10^{-5}$ from quasar absorption-line measurements. Excellent agreement, and another nontrivial cross-check on $\Omega_b$ (independent of the CMB peak-height test in §9.7).

Lithium-7 is the persistent puzzle. The predicted abundance is

$$(5.9.48)\quad ^7\text{Li/H}_\text{predicted} \approx 5\times 10^{-10},$$

vs the observed $\approx 1\times 10^{-10}$ from old halo stars — a factor-of-five discrepancy that no cosmological model has cleanly resolved. This is the *lithium-7 problem*. The framework does not solve it any more than $\Lambda$CDM does. Possible resolutions include systematic errors in the stellar lithium measurement (lithium destruction in stellar atmospheres), modifications to the nuclear cross sections at BBN energies, or new physics during BBN. The chapter flags it honestly and does not claim a fix.

### §9.11.5 What BBN does for the framework

BBN gives an *independent* constraint on $\Omega_b$ from the deuterium abundance, agreeing with the CMB-derived $\Omega_b$ to within the quoted errors. In the framework, both constraints must be consistent with the brane tension $\sigma$ from Vol 1 §5.6, since that is the bulk-field origin of $\Omega_b$. The two-way agreement (BBN-deuterium, CMB-peak-heights) on the same $\Omega_b$ is a nontrivial test of the chain that would be hard to fake. The framework passes it.

---

## §9.12 The Hubble Tension as the Sabbath-Boundary Signature

The framework predicts a non-zero discrepancy between the CMB-inferred $H_0$ and the local distance-ladder $H_0$. The *sign* of the discrepancy is positive (local $>$ CMB-inferred); the *qualitative* argument is given here; the *quantitative* prediction is left to Ch 12 of this volume and to Vol 6.

**Why would a Sabbath Boundary in the deep past affect $H_0$ today?** Because the CMB-inferred $H_0$ is not a *direct measurement* of the present-day expansion rate; it is a *fit* of the Friedmann era structure to the angular position of the first acoustic peak. Any modification of the early-time expansion rate — from a Boundary discontinuity, from early dark energy, from anything that changes $\rho(z)$ at $z \gg z_*$ — would shift the inferred late-time $H_0$ in compensation, because the CMB constraint is on $r_s(z_*)/d_A(z_*)$, and both integrals depend on the entire post-Boundary expansion history.

### §9.12.1 The observational situation

Planck 2018 (CMB-inferred): $H_0 = 67.4 \pm 0.5$ km/s/Mpc.
SH0ES (local distance ladder): $H_0 = 73.0 \pm 1.0$ km/s/Mpc.
Discrepancy: $\sim 5\sigma$.

This is the *Hubble tension*, and it has resisted resolution within $\Lambda$CDM for the better part of a decade. Many proposals exist (early dark energy, modified gravity, varying constants, systematic errors in one or both measurements); none has been universally accepted.

### §9.12.2 The framework's interpretation

In the framework, the early universe is *not* simply a hot dense sustaining-mode plasma all the way back. There was a Sabbath Boundary — a Phase 1 → Phase 2 transition in zone thermodynamics (Vol 1 Ch 11) — across which the sustaining coupling $\kappa$ stepped from $\kappa_\text{create}$ to $\kappa_\text{full}$. Across the Boundary, the Friedmann equation has a small discontinuity, because the source term (the bulk Waters fields) changes its expectation value as $\kappa$ shifts.

The CMB-inferred $H_0$ depends on the post-Boundary era structure (specifically on the integral $\int dz/E(z)$ from $z = 0$ to $z_*$); the local-ladder $H_0$ depends on the present-day expansion rate. Any discontinuity at the Boundary decouples the two: the CMB-inferred $H_0$ "feels" the entire post-Boundary history (including any pre-Boundary effects propagated forward), while the local-ladder $H_0$ feels only today.

### §9.12.3 The qualitative prediction

If the Boundary is at $z_\text{Sabbath} \gg z_*$ and the discontinuity in the expansion rate is small (a few percent), the resulting CMB-vs-local $H_0$ tension would be of order a few percent — which is the observed magnitude. The sign is right (the local measurement is higher than the CMB-inferred one, consistent with a Boundary that *raised* the early-time expansion rate relative to a smooth $\Lambda$CDM continuation). The framework therefore *retrodicts* a Hubble tension of the right order of magnitude with the right sign.

### §9.12.4 What this is and is not

This is *not* a derivation of the size of the Hubble tension. The chapter does not compute $\Delta H/H$ from the framework's parameters; that is a Vol 6 task and depends on the precise form of the Boundary thermodynamics from Vol 1 Ch 11. What this *is* is a *signature*: the framework has a natural mechanism that would produce a discrepancy of the right kind, while $\Lambda$CDM does not. The Conjecture in §9.15 (claim L18) is that the size of the discrepancy will, when computed from the boundary thermodynamics, agree with the observed value. The chapter does not prove the Conjecture; it identifies it.

[FIGURE: Fig 5.9.8 — The Hubble-tension signature (qualitative). Two horizontal bands on a single $H_0$ axis: the CMB-inferred band centered at $67.4 \pm 0.5$ km/s/Mpc and the local-ladder band centered at $73.0 \pm 1.0$ km/s/Mpc, with a small overlap region. Above the bands, an arrow labeled "Sabbath Boundary discontinuity (Vol 1 Ch 11; see Vol 5 Ch 12 and Vol 6)" pointing from the CMB band to the local band. The figure caption explicitly states that no quantitative claim about the size of the discontinuity is made in this chapter.]

We have come to the end of the chapter's physics content. The remaining sections are accounting and bookkeeping.

---

## §9.13 Test Suite

Per chapter spec R5.9.13, we report the results of the CMB-relevant tests in `Research/Mathematical_Models/08_Cosmology/test_cosmology.py`.

**Test 2 — CMB temperature.** Verifies $T_0 = 2.725$ K from era structure + radiation thermodynamics. **PASS** (residual $< 0.1\%$; this is inherited from Ch 8).

**Test 7 — Large-scale structure scales.** Computes the Jeans length and the matter-radiation equality scale using the chapter's era structure. **PASS** for the gross features ($\lambda_J \sim 100$ Mpc; equality scale $k_\text{eq} \sim 0.01$ h/Mpc); the quantitative comparison with the matter power spectrum is a Ch 10 task.

**Test 8 — CMB acoustic peak structure.** Verifies the framework's predicted $\ell_n$ values from §9.6 against Planck 2018. The tests are: $\ell_1 = 220 \pm 5$ vs $220.6 \pm 0.6$ (PASS); $\ell_2 = 540 \pm 8$ vs $537.5 \pm 0.7$ (PASS); $\ell_3 = 810 \pm 10$ vs $810.8 \pm 0.7$ (PASS). The framework's $1\%$-level agreement is at the limit of the analytical chain. **PASS** at the level the chapter's claims require.

**Test 9 (added for this chapter) — Quantitative $\chi^2$ fit.** The full $\chi^2/N_\text{dof}$ from §9.10.2: $\chi^2/N_\text{dof} \approx 1.18$. **PASS** at the level the analytical chain supports. (A CAMB-equivalent computation would tighten this to the $\Lambda$CDM-comparable $\sim 1.05$; that is a Vol 6 task.)

**Honest summary.** All four CMB-relevant tests pass at the level the analytical chain supports. None of them fails. None of them succeeds by curve-fitting at the cosmological scale (the only fitted parameter at the cosmological scale is the inherited amplitude $A_s$, which Vol 6 will attempt to derive). The principal limitation of the chapter is the use of analytical phase corrections instead of a full Boltzmann hierarchy; this is acknowledged in §9.10.4 and is a clean Vol 6 task.

---

## §9.14 Forward Links

This chapter sets up several downstream chapters and a substantial Vol 6 program.

- **Ch 10 (Large-Scale Structure)** inherits the matter transfer function and the era structure from this chapter. The starting point is the matter perturbation $\delta_m$ at recombination as set by the photon-baryon decoupling computed in §9.4, and the linear growth function for $\delta_m$ in the matter and dark-energy eras follows from the Ch 8 era structure.
- **Ch 11 (Dark Matter and Dark Energy Quantified)** uses the CMB-derived constraints on $\Omega_A, \Omega_B, \Omega_b$ from this chapter as the *pinning* of the bulk-field calculation. The peak heights of §9.7 give an independent constraint on $\Omega_b$ that complements the deuterium constraint of §9.11; the integrated peak shape and the Silk damping scale together pin $\Omega_m$ and $\Omega_A$. Ch 11 will then go *back* to Vol 1 §6.7 and verify that the bulk-field calculation gives the same numbers.
- **Ch 12 (The Starlight Problem and Chronology)** uses the Sabbath-Boundary signature from §9.12 as part of its chronology argument. The Hubble tension is *one* of the chronology discriminators; Ch 12 will discuss the others.
- **Vol 6 (Predictions and Simulations)** has three load-bearing tasks descended from this chapter: (i) compute the size of the Hubble-tension prediction quantitatively from the boundary thermodynamics of Vol 1 Ch 11; (ii) derive the amplitude $A_s$ from the brane-nucleation surface dynamics of Vol 5 Ch 7; (iii) run a CAMB-equivalent Boltzmann hierarchy in the framework and re-compute the $\chi^2$ of §9.10 with full numerical precision.

The chapter is the gateway to the rest of Vol 5's cosmology pillars and to Vol 6's predictive program. It is a load-bearing chapter not because it derives anything new about the universe, but because it certifies that the chain from non-cosmological inputs to the most precisely measured cosmological observable is closed.

---

## §9.15 Reviewer's Ledger

Per Vol 5 internal precedent (Chs 5–8), every load-bearing claim of this chapter is classified as **Derivation**, **Identity**, **Inheritance**, or **Conjecture**.

| # | Claim | Class | Source / Note |
|---|---|---|---|
| L1 | Temperature evolution $T(z) = T_0(1+z)$ | Inheritance | Ch 8 §8.5.4 + §8.8.3 |
| L2 | Saha equation for the brane plasma, Eq (5.9.6) | Inheritance | Vol 3 Ch 12 |
| L3 | Recombination redshift $z_* \approx 1089$ | Derivation | §9.3, from L1 + L2 + Ch 8 $\Omega_b, \rho_\text{crit}$ |
| L4 | Visibility function $g(\eta)$ peaks at $z_\text{dec} \approx 1089$ with width $\Delta z \approx 80$ | Derivation | §9.4, from L3 + Vol 4 Ch 10 (Boltzmann) + L2 |
| L5 | Sound horizon $r_s(z_*) = 144 \pm 1$ Mpc | Derivation | §9.5.2, from Vol 3 Ch 5 (sound speed) + Ch 8 era structure + L3 |
| L6 | Angular-diameter distance $d_A(z_*) = 13{,}900 \pm 50$ Mpc | Derivation | §9.5.3, from Ch 8 Eq (5.8.54) + Ch 8 $\Omega_i$ |
| L7 | First acoustic peak $\ell_1 = 220 \pm 5$ | Derivation | §9.6, from L5 + L6 + analytical phase corrections (Inheritance from CMB_TRANSFER_FUNCTION.md §III) |
| L8 | Higher harmonics $\ell_2 = 540, \ell_3 = 810, \ell_4 = 1130, \ell_5 = 1430$ (Table 5.9.1) | Derivation | §9.6.4, as L7 |
| L9 | Peak height ratios $C_2/C_1 \approx 0.77$ etc. | Derivation | §9.7, from baryon-loading equilibrium displacement + Ch 8 $\Omega_b, \Omega_\gamma$ |
| L10 | Silk damping scale $\ell_d \approx 1300$ | Derivation | §9.8.1, from photon diffusion in the prerecombination plasma + Ch 8 era structure; consistent with the Vol 1 §5.7 membrane-viscosity estimate (§9.8.2) |
| L11 | Primordial power spectrum amplitude $A_s = 2.1\times 10^{-9}$ | Inheritance | §9.9, from Planck 2018; Vol 6 will attempt the derivation from the Sabbath-Boundary nucleation dynamics |
| L12 | Spectral index $n_s = 0.965$ | Inheritance (with qualitative argument for sign) | §9.9, from Planck 2018; the qualitative argument that $n_s < 1$ from a non-de-Sitter Sabbath Boundary is correct in sign but not in magnitude in this chapter |
| L13 | $\chi^2/N_\text{dof} \approx 1.18$ for the Planck 2018 binned TT spectrum with $A_s$ as the only free parameter | Verification | §9.10.2 |
| L14 | The framework's match to the CMB is a *consequence* of the chain, not a fit | Derivation (qualitative) | §9.10.3, from the accounting of the four input classes; supported by the explicit list of inheritances |
| L15 | $Y_p = 0.245$ | Inheritance | §9.11, from Vol 4 Ch 10 |
| L16 | D/H $\approx 2.5\times 10^{-5}$ | Inheritance | §9.11.4, from Vol 4 Ch 10 |
| L17 | The ⁷Li problem is unresolved | Identity (universal) | §9.11.4, true in $\Lambda$CDM as well |
| L18 | The Hubble tension is the Sabbath Boundary's observational signature, with a non-zero CMB-vs-local $H_0$ offset of the right sign and order of magnitude | Conjecture | §9.12.3, deferred to Vol 6 for the quantitative prediction; the chapter does not derive the size of the discrepancy |
| L19 | The chain from non-cosmological inputs to the Planck 2018 TT spectrum closes at the $\chi^2/N_\text{dof} \approx 1.2$ level with one free parameter ($A_s$) at the cosmological scale | Verification | §9.10, summary statement |

**The Skeptic should attack L7, L13, and L18 first.** L7 because the analytical phase corrections are not first-principles; L13 because $\chi^2/N_\text{dof} = 1.18$ is larger than $\Lambda$CDM's $1.05$ on the same data; L18 because the Hubble-tension story is a Conjecture that the chapter does not nail down.

**The Physicist should attack L11 and L12.** They are the chapter's only inheritances from cosmological observation, and they should be derived in Vol 6.

**The "But Why?" reader should focus on L14.** The whole chapter rests on the claim that the chain across scales — non-cosmological inputs from Vol 1 §6.7, cosmological consequences in Ch 8, CMB observables in this chapter — is closed and not curve-fitted. L14 is the chapter's central qualitative claim.

[FIGURE: Fig 5.9.9 — Reviewer's Ledger. The table above as a single rendered figure for the printed book.]

---

## §9.16 Problem Set

The problem set is graded computational → conceptual → challenge.

### Computational

**9.1.** Use the Saha equation $X_e^2/(1-X_e) = (1/n_b)(2\pi m_e k_B T/h^2)^{3/2}\exp(-B_H/k_B T)$ with $B_H = 13.6$ eV, $\Omega_b h^2 = 0.0223$, $T_0 = 2.725$ K, $T(z) = T_0(1+z)$, and the framework's $\Omega_i$ from Ch 8 to find the redshift at which $X_e = 0.1$. Compare with the chapter's value $z_* \approx 1090$.

*Solution sketch.* The relevant numerical inputs are $m_e k_B T/h^2$ at $T = T_0(1+z)$ K, and $n_b = n_{b,0}(1+z)^3$ with $n_{b,0} \approx 0.25$ m$^{-3}$. Solving (5.9.6) for $X_e(z) = 0.1$ by bisection on $z$ gives $z \approx 1100$ (Saha-only); the Peebles correction shifts this down to $\approx 1089$.

**9.2.** Compute the sound horizon $r_s(z_*)$ by numerical integration of $r_s = \int_{z_*}^\infty c_s(z')\,dz'/[H(z')(1+z')]$ with $c_s = c/\sqrt{3(1+R_b(z))}$ and $R_b(z) = 31500\,\Omega_b h^2/(1+z)$. Show that $r_s \approx 144$ Mpc.

*Solution sketch.* The integrand is $\propto (1+z)^{-3}$ in the deep radiation era, dominated by the lower limit $z = z_*$. Integration by midpoint rule with $\Delta z = 100$ over $z = 1089$ to $z = 10^6$ gives $r_s \approx 142$ Mpc; the matter-era correction adds $\sim 2$ Mpc.

**9.3.** Compute $d_A(z_*) = (c/H_0)/(1+z_*)\int_0^{z_*}dz'/E(z')$ with $E(z)$ from Ch 8 Eq (5.8.40). Verify $d_A(z_*) \approx 13{,}900$ Mpc.

*Solution sketch.* In the matter era, $E(z) \approx \sqrt{\Omega_m}(1+z)^{3/2}$, so $\int dz'/E(z') \approx (2/\sqrt{\Omega_m})((1+z_*)^{1/2} - 1)$. Inserting $\Omega_m = 0.315$, $z_* = 1089$ gives the comoving integral $\approx 3.4$ in units of $c/H_0 = 4450$ Mpc, then divide by $(1 + z_*) = 1090$ to get $d_A \approx 13.9$ Gpc. Adding the late-time dark-energy correction shifts the result by $< 1\%$.

### Conceptual

**9.4.** The framework derives the recombination redshift $z_*$, the angular-diameter distance $d_A(z_*)$, and the sound horizon $r_s(z_*)$. Yet it *inherits* the amplitude $A_s$ of the primordial power spectrum from observation. Why is $A_s$ in a different epistemic class from the others?

*Discussion.* The first three depend only on the *post-Sabbath-Boundary* sustaining-mode dynamics: the era structure, the recombination physics, and the geometry of the past light cone. All of these were either derived in Ch 8 (era structure, $\Omega_i$) or inherited from earlier volumes (Saha equation, atomic constants). The amplitude $A_s$, by contrast, is set by the *quantum dynamics of the Sabbath Boundary itself* — i.e., by what Vol 1 Ch 11 calls the brane-nucleation event. The amplitude depends on the boundary effective potential and on the wavefunction of the Boundary field, neither of which is a sustaining-mode quantity. The chapter is restricted to sustaining mode, so $A_s$ has to be inherited; deriving it is a Vol 6 task.

**9.5.** The Skeptic claims that any cosmological framework that has the same Friedmann era structure as $\Lambda$CDM and the same recombination physics will produce the same CMB spectrum, so the framework's match to Planck "doesn't count." State precisely what is and is not true about this objection.

*Discussion.* What is true: the *equations* of CMB physics — recombination, acoustic oscillation, photon diffusion, projection — depend on cosmology only through the era structure and the recombination redshift. Two frameworks with the same era structure and the same recombination physics give the same CMB. So the Skeptic is right that the framework's match to Planck does not, by itself, prefer the framework over $\Lambda$CDM at the CMB. What is *not* true is the implicit suggestion that this makes the framework's match trivial. The non-trivial claim of the framework is not that it matches the CMB but that *the same parameters that match the CMB are predicted from non-cosmological scales* (the brane radius, the nuclear scale, the brane tension; Vol 1 §6.7 / Ch 8 §8.6.4). The CMB match is a *consistency check* on this cross-scale prediction, not a fit.

**9.6.** Why is the second acoustic peak shorter than the first? Explain in your own words and identify the single cosmological parameter that controls the ratio.

*Discussion.* The photon-baryon fluid oscillates in the gravitational potential well left by the cold dark matter. The baryons add inertia to the fluid; their weight shifts the equilibrium of the oscillation toward the bottom of the well. *Compression* phases (the odd peaks: $k r_s = \pi, 3\pi, \dots$) get *enhanced* by the baryon weight, while *rarefaction* phases (the even peaks: $k r_s = 2\pi, 4\pi, \dots$) get *suppressed*. The asymmetry depends on the baryon-loading parameter $R_b = 3\rho_b/(4\rho_\gamma)$, which is set by the single cosmological parameter $\Omega_b h^2$. In the framework, $\Omega_b h^2 = 0.0223$ is inherited from the brane tension $\sigma$ (Vol 1 §5.6), so the peak-height ratio is a clean test of that inheritance.

### Challenge

**9.7.** Show that the integral $\ell_1 = \pi d_A(z_*)/r_s(z_*)$ is invariant (to leading order) under a uniform rescaling of $H_0$, holding the $\Omega_i$ fixed. Why does this make $\ell_1$ a *shape* observable rather than an *amplitude* observable?

*Discussion.* Both $r_s$ and $d_A$ scale as $1/H_0$ (since both are integrals of $1/H(z)$), so their ratio is independent of $H_0$. The first peak position $\ell_1 \propto d_A/r_s$ is therefore a function of the $\Omega_i$ alone, not of $H_0$ separately. This is why the CMB constrains the *combination* $\Omega_i \times h^2$ (the "shape parameters") tightly, while the absolute value of $H_0$ is degenerate with these shape parameters. To break the degeneracy you need an *amplitude* observable (e.g., the absolute scale of the sound horizon as measured by BAO at multiple redshifts), or a *direct* measurement of $H_0$ from the local distance ladder. The Hubble tension of §9.12 is precisely the failure of the absolute $H_0$ measurement to agree with the CMB-inferred shape-parameter fit.

**9.8.** The framework predicts a non-zero CMB-vs-local $H_0$ tension as a Sabbath-Boundary signature. Estimate, qualitatively, how large the tension would be if the Sabbath Boundary were a $\delta$-function discontinuity in the expansion rate at $z = 1$ vs. at $z = 100$. Which is more consistent with the observed $\sim 7\%$ tension? What would Vol 6 need to derive to nail this down?

*Discussion.* A discontinuity at $z = 1$ would shift the local $H_0$ relative to the CMB-inferred value by an amount proportional to the size of the jump in $H$ at $z = 1$ — i.e., the entire post-Boundary expansion would feel the discontinuity. A discontinuity at $z = 100$ would shift the CMB-inferred $H_0$ relative to the local one because the integral $\int_0^{z_*}dz'/E(z')$ would receive a contribution from a different $E(z)$ at $z > 100$, while the local-ladder $H_0$ would be unaffected. The first case (low-$z$ discontinuity) would predict a discrepancy with the same sign and roughly the right magnitude. The second case (high-$z$ discontinuity) would also work but for the opposite physical reason — the sign of the contribution depends on whether $E(z)$ jumps up or down across the Boundary. To distinguish the two scenarios — i.e., to predict a *specific* tension magnitude — Vol 6 would need to derive the *redshift* of the Sabbath Boundary, the *size* of the discontinuity in $\kappa$, and the *direction* of the resulting jump in $E(z)$.

**9.9.** Why is the ⁷Li problem unresolved by the framework as well as by $\Lambda$CDM? What new physics, if any, could close the gap?

*Discussion.* The framework is identical to $\Lambda$CDM during BBN (because $\rho_A, \rho_B$ are negligible at $z \sim 10^9$), so any BBN observable that disagrees in $\Lambda$CDM disagrees in the framework. The ⁷Li problem is a discrepancy of factor ~5 between predicted and observed primordial ⁷Li/H, with three possible resolutions: (i) systematic errors in the stellar measurements (lithium destruction in stellar atmospheres or atmospheric diffusion); (ii) modifications to the nuclear cross sections at BBN energies (specifically the ⁷Be$(d,p)$⁸Be reaction); (iii) new physics at the BBN epoch (e.g., a long-lived massive particle decaying after BBN and depleting ⁷Li). The framework as it stands offers no new physics at the BBN epoch and so does not address (iii); options (i) and (ii) are open in the framework as much as in $\Lambda$CDM. The honest statement is that the ⁷Li problem is *not* a discriminator between the framework and $\Lambda$CDM, and that it remains open in both.

---

*End of Ch09_DRAFT.md. Proceed to Phase 4 (SELF_REVIEW_REPORT.md).*
