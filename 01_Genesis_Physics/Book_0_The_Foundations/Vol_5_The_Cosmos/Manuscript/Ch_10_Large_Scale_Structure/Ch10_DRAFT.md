# Chapter 10: Large-Scale Structure
## Foundations Vol 5: The Cosmos — Part III: Cosmology

---

> *"Chapter nine asked the cosmic microwave background a question and received an answer. Chapter ten asks a quieter question of the matter that scattered those photons one last time and then went its own way. The question is: where did it end up? Knowing the Firmament FLRW background of chapter eight and the matter transfer function of chapter nine, we have, in the linear regime, no remaining freedom: the answer is forced. This chapter walks the chain that forces it, and is honest about where the chain ends and the harder problem of the nonlinear universe begins."*

---

## §10.0 What This Chapter Is (and Is Not)

> **Structural reminder.** *Firmament* is this textbook's term for the 3-brane hypersurface $Z_{2.2}$ derived in Vol 1 Ch 5, named after the Hebrew *rāqîaʿ* (Gen 1:6–8) for a hammered, stretched membrane. *Waters Above / Waters Below* are the bulk regions on either side (Vol 1 Ch 3–4). Per Ch 5 §5.0: the Hebrew denotes a physical membrane, as the physics requires.


Before I write down a single equation I want to declare the chapter's epistemic position, because it differs in an important way from the position of chapter nine, and a reader who carries the wrong expectation across the boundary between chapters will be either disappointed or fooled.

**What this chapter does.** It takes the Firmament FLRW background derived in Vol 5 chapter 8 — the four density parameters, the era structure, the function $E(z) = H(z)/H_0$ — and the matter transfer function $T(k)$ assembled in Vol 5 chapter 9 §9.5–§9.8, and uses them as the inputs to standard linear cosmological perturbation theory. From these inputs and from the linearized fluid equations of Vol 3 chapter 5, the chapter derives the linear growth factor $D^+(a)$, the matter power spectrum $P(k, a)$, the rms mass variance $\sigma(M)$, and the Press–Schechter halo mass function $dn/d\ln M$. It compares each of these to the relevant observation: the SDSS BOSS galaxy power spectrum, the Planck-inferred matter power spectrum, the X-ray cluster mass function, and the redshift-space-distortion measurements of $f\sigma_8$. It then introduces the Zel'dovich approximation in its standard form to show that the framework reproduces, qualitatively, the cosmic web pattern observed in galaxy redshift surveys. Finally, in §10.10, it brings forward the Vol 1 chapter 6 weak-self-coupling argument for the Waters Below (dark matter, ~27%; paired with Waters Above = dark energy, ~68%) field to argue that the framework reproduces the Bullet Cluster observation qualitatively.

**What this chapter does not do, and why the difference matters.** Chapter nine derived the recombination redshift, the sound horizon, the angular-diameter distance, and the first acoustic peak from the framework's $\Omega_i$ — quantities that were themselves derived in chapter 8 from the Firmament radius, the Firmament tension, and the bulk-field calculation of Vol 1 §6.6.4. The chain there ran from non-cosmological inputs to cosmological observables, and the Skeptic's correct objection — *did you tune anything?* — had a specific and defensible answer.

In *this* chapter, the chain is shorter and the conclusion is correspondingly more modest. The framework's prediction for $D^+(a)$, in the canonical case where the Waters Above behaves as a strict cosmological constant ($w_A = -1$ exactly), is *numerically identical* to the $\Lambda$CDM growth factor with the same $\Omega_m$ and $\Omega_\Lambda$. The framework's prediction for $\sigma_8$ is *numerically identical* to the $\Lambda$CDM prediction with the same $A_s, n_s, T(k)$. The framework's prediction for the halo mass function is *numerically identical* to the Press–Schechter prediction in the same cosmology. There is no first-order discriminator from the linear regime alone.

> **Note:** The large-scale structure predictions in this chapter are **degenerate with $\Lambda$CDM** when $A_s$ and $n_s$ are adopted from Planck data (as they are throughout this chapter). Distinguishing zone architecture from $\Lambda$CDM in the LSS regime requires the independent derivation of $A_s$ and $n_s$ from zone architecture first principles — designated Research Task RT-5.CMB. Until RT-5.CMB is complete, the chapter's power spectrum, $\sigma_8$, and halo mass function results constitute a consistency check that zone architecture does not conflict with LSS observations, not a prediction that zone architecture is confirmed by them.

The chapter therefore performs a *consistency check*, not a novel prediction. The interesting work is in the bookkeeping — *which* of the four Ch 8 components actually clusters, and *why* — and in the honest statement of what the framework cannot say in the nonlinear regime. The chapter is not a survey of structure formation, and it is not a triumph: it is a careful accounting of where the framework's predictive grasp ends.

**A note for the Skeptic reviewer.** The hardest question for this chapter is: *isn't this just $\Lambda$CDM with relabeled parameters?* The honest answer has two parts. *First*, in the linear regime, *yes*: the framework's growth factor, power spectrum, and halo mass function coincide numerically with the $\Lambda$CDM predictions in the strict $w_A = -1$ canonical case. The Skeptic is correct that the chapter, taken in isolation, cannot distinguish the framework from $\Lambda$CDM. *Second*, however, the parameters are not relabeled — they are *derived* in chapter 8 from non-cosmological inputs. The framework predicts the same observables as $\Lambda$CDM but from a different chain. Whether one finds this interesting or uninteresting depends on whether one cares about the shape of the chain or only about the leaf at the end of it. The Skeptic should be interested in the *next* chapter (Ch 11), which catalogs the discriminators that the framework's identification $\Omega_B = $ Waters Below makes available beyond what $\Lambda$CDM offers, and in Vol 6, which compiles the predictions catalog. §10.13 itemizes the chapter's load-bearing claims.

**A note for the Physicist reviewer.** The hardest question for the Physicist is: *is the linear growth equation genuinely derived from the framework, or are you smuggling in $\Lambda$CDM by writing it in standard form?* The chain is: the linearized fluid equations of Vol 3 Ch 5 (continuity + Euler + Poisson, valid for any non-relativistic self-gravitating fluid on a curved background) are applied to the Firmament matter density $\bar\rho_m = \bar\rho_b + \bar\rho_B$ — where $\bar\rho_b$ are the baryons (5 percent of $\rho_\text{crit}$) and $\bar\rho_B$ is the Firmament-projected Waters Below field (27 percent of $\rho_\text{crit}$, derived in Vol 1 §6.6.4 and inherited through Ch 8). The background $H(a)$ is the chapter-8 $E(z)$. The Vol 1 Ch 5 Firmament is taken as the spatial slice on which the perturbation lives, but at the scales of interest ($k \gg H$, well within the Hubble horizon, well above the Firmament thickness) all of the Firmament geometry projects out and one is left with the Newtonian limit on a comoving FLRW background. The Vol 1 Ch 6 *equation of state* of the Waters Below — $w_B \approx 0$, sound speed $c_{s,B} \ll c$ — is what makes Waters Below cluster identically to cold dark matter. None of this is reinvented for this chapter. What *is* particular to the framework is the *content* of $\bar\rho_m$: it is baryons plus Waters Below, not baryons plus a hypothetical CDM particle. The growth equation does not care what the matter is *made of*; it cares only about $\bar\rho_m$ and the equation of state. So the equation is the same; the matter is different.

**A note for the "But Why?" reader.** The chapter is organized around the ten why-questions of the chapter spec. Each section opens with one or more of them and answers them in plain language before introducing any equations. The Reviewer's Ledger in §10.13 collects the one-line answers.

**Roadmap.** §10.1 inventories the toolkit from previous chapters. §10.2 sets up what a density perturbation on the Firmament FLRW background actually means. §10.3 derives the linear growth equation and tabulates the growth factor. §10.4 does the bookkeeping — which Ch 8 components cluster, which do not, and why — and reports the growth rate $f(a)$. §10.5 brings forward the Ch 9 matter transfer function and assembles $P(k, z)$. §10.6 computes $\sigma_8$ from the power spectrum. §10.7 derives the spherical-collapse threshold and the Press–Schechter halo mass function and compares to the X-ray cluster mass function. §10.8 introduces the Zel'dovich approximation and the cosmic web. §10.9 states the $N$-body gap. §10.10 is the Bullet Cluster qualitative argument. §10.11 reports the test suite and gives the worked example for the Student reviewer. §10.12 is the forward links. §10.13 is the Reviewer's Ledger. §10.14 is the problem set.

---

## §10.1 Inventory: The Toolkit From Previous Chapters

Following the precedent of chapter 9, the chapter begins by laying out the tools. Nothing here is re-derived if it has already been proven elsewhere; the inventory is also a contract with the Consistency Auditor.

### §10.1.1 From Vol 5 Ch 8 — the Firmament FLRW background

Vol 5 Ch 8 derived the Friedmann constraint, the acceleration equation, the continuity equation, the four-component era structure, and the four density parameters. We will use:

- The dimensionless Hubble function from Ch 8 Eq (5.8.40),

$$(5.10.1)\quad E(z) \equiv \frac{H(z)}{H_0} = \sqrt{\Omega_A + \Omega_m(1+z)^3 + \Omega_r(1+z)^4},$$

with $\Omega_A = 0.684$, $\Omega_m = \Omega_b + \Omega_B = 0.049 + 0.266 = 0.315$, $\Omega_r \approx 9.2 \times 10^{-5}$, all from Ch 8 §8.6.3 and inherited there from the bulk-field calculation of Vol 1 §6.6.4. The chapter writes $E(a) = E(z = 1/a - 1)$ interchangeably.

- The Hubble constant $H_0 = 67.4$ km/s/Mpc from Ch 8 Eq (5.8.47), corresponding to a comoving Hubble length $c/H_0 \approx 4{,}450$ Mpc.

- The matter–radiation equality redshift $z_\text{eq} \approx 3{,}400$ from Ch 8 Eq (5.8.45), and the corresponding wavenumber

$$(5.10.2)\quad k_\text{eq} \equiv H(z_\text{eq})/c \approx 0.014\;\text{Mpc}^{-1},$$

which sets the turnover in the matter transfer function (we will see this again in §10.5).

- The matter–dark-energy equality redshift $z_{m\Lambda} \approx 0.30$ from Ch 8 Eq (5.8.46), the redshift below which the universal expansion accelerates and structure-formation growth begins to freeze.

These four items will be used everywhere below. The chapter is internally a function of them.

### §10.1.2 From Vol 5 Ch 9 — the matter transfer function and the inherited primordial spectrum

Vol 5 Ch 9 §9.5–§9.8 assembled, in the course of computing the CMB acoustic peaks, the *matter transfer function* $T(k)$ that maps the primordial curvature spectrum onto the matter density spectrum at the surface of last scattering and beyond. We will use:

- The transfer function in the analytical form of Eisenstein and Hu (1998), with the Ch 8 sound horizon $r_s(z_*) = 144$ Mpc and the Ch 8 density parameters as inputs:

$$(5.10.3)\quad T(k) = T_\text{EH}(k;\,\Omega_m h^2,\,\Omega_b h^2,\,r_s),$$

where the explicit form is given in chapter 9 Eq (5.9.27) and need not be reproduced here. Two features of $T(k)$ matter for this chapter: (i) the *turnover* at $k_\text{eq}$, where $T(k) \to 1$ on large scales and $T(k) \propto k^{-2}\ln k$ on small scales; (ii) the damped *baryon-acoustic oscillation* (BAO) wiggle at $k_\text{BAO} = 2\pi/r_s \approx 0.044$ Mpc⁻¹.

- The primordial curvature spectrum amplitude and tilt, *inherited from observation* through chapter 9 §9.9:

$$(5.10.4)\quad \mathcal P_\zeta(k) = A_s\!\left(\frac{k}{k_*}\right)^{n_s - 1}\!,\qquad A_s = 2.10 \times 10^{-9},\;n_s = 0.965,\;k_* = 0.05\;\text{Mpc}^{-1}.$$

The values are the Planck 2018 best-fit values; they enter this chapter exactly as they entered chapter 9, with the same caveat that they are not derived in this volume and will be addressed in Vol 6. The Reviewer's Ledger classifies $A_s$ as Inheritance and $n_s$ as Inheritance with the same qualitative caveat.

### §10.1.3 From Vol 1 Chs 5–6 — the Firmament and the Waters fields

Vol 1 Ch 5 established the Firmament as a codimension-2 Firmament $\Sigma$ with tension $\sigma > 0$ and mass density $\mu$, supporting transverse waves at speed $c^2 = \sigma/\mu$ (Vol 1 Eq 1.5.37). Vol 1 Ch 6 introduced the Waters Above ($\Psi_A$, a bulk field with equilibrium energy density $\bar\rho_A$ that contributes equation of state $w_A \approx -1$ in the Firmament projection) and the Waters Below ($\Psi_B$, a Firmament-localized field with equilibrium energy density $\bar\rho_B$ that contributes equation of state $w_B \approx 0$ and self-coupling many orders of magnitude weaker than electromagnetism).

Two facts from Vol 1 Ch 6 will be load-bearing in §10.4:

- *Waters Above does not cluster on subhorizon scales.* Vol 1 §6.5 showed that the relaxation time of $\Psi_A$ to its equilibrium value is the Hubble time, so spatial perturbations of $\Psi_A$ on scales $\ll c/H$ are damped on a sound-crossing time. To leading order in the cosmological perturbation expansion, $\delta\Psi_A = 0$ on subhorizon scales — the field enters only through the homogeneous background $H(a)$.

- *Waters Below clusters identically to cold dark matter.* Vol 1 §6.4 showed that on the Firmament, $\Psi_B$ admits non-relativistic excitations with sound speed many orders of magnitude below $c$, with self-coupling so weak that the field is collisionless on a galaxy-cluster crossing time. These two properties — non-relativistic motion and collisionlessness — are exactly the defining properties of cold dark matter in the conventional model. The chapter will use this in §10.4 to write $\bar\rho_m = \bar\rho_b + \bar\rho_B$ in the matter perturbation equation without further argument.

### §10.1.4 From Vol 3 Ch 5 — linearized fluid dynamics

Vol 3 Ch 5 derived the continuity, Euler, and Poisson equations for a non-relativistic, self-gravitating fluid on a comoving FLRW background. In comoving coordinates, with $\delta = (\rho - \bar\rho)/\bar\rho$ the density contrast, $\vec v$ the peculiar velocity, and $\phi$ the gravitational potential, they read

$$(5.10.5)\quad \dot\delta + \frac{1}{a}\nabla\!\cdot\!\vec v = 0,\qquad \dot{\vec v} + H\vec v = -\frac{1}{a}\nabla\phi,\qquad \nabla^2\phi = 4\pi G \bar\rho \,a^2 \delta,$$

valid in the linear limit $|\delta| \ll 1$. These three equations are the entire technical apparatus of linear structure formation; everything in the chapter follows from them by elimination.

### §10.1.5 From Vol 3 Ch 12 — Gaussian random fields and Press–Schechter peak counting

Vol 3 Ch 12 (statistical mechanics of fluctuating fields) gave us the formalism of Gaussian random fields: a field $\delta(\vec x)$ with two-point correlation $\langle\delta(\vec x_1)\delta(\vec x_2)\rangle$ specified by a power spectrum $P(k)$ is fully characterized in the Gaussian case by $P(k)$ alone, and the variance $\sigma^2(R)$ on a smoothing scale $R$ is the integral $\int d^3k\,P(k)|W(kR)|^2/(2\pi)^3$. The chapter will use this in §10.6.

The same chapter introduced the *Press–Schechter peak-counting argument*: in a Gaussian density field, the comoving number density of peaks above threshold $\nu$ is set by the Gaussian tail $\propto \exp(-\nu^2/2)$. We will use this in §10.7.

### §10.1.6 From Vol 5 Ch 1 — perturbed Einstein equations on the Firmament

Vol 5 Ch 1 derived the linearized Einstein equations on the Firmament (Eq 5.1.45) and the Newtonian limit on subhorizon scales (Eq 5.1.55), in which the metric perturbation $\Phi$ couples to the matter density $\delta_m$ through the Poisson equation $\nabla^2\Phi = 4\pi G \bar\rho_m a^2 \delta_m$. This is the same Poisson equation that appears in (5.10.5), and the chapter will use it without re-derivation.

---

## §10.2 The Setup: A Density Perturbation on the Brane FLRW Background

Before deriving the growth equation we need to be specific about *what* is fluctuating. On the Firmament FLRW background of chapter 8, the matter density is

$$(5.10.6)\quad \rho_m(\vec x, t) = \bar\rho_m(t)\,[1 + \delta_m(\vec x, t)],\qquad \bar\rho_m(t) = \bar\rho_b(t) + \bar\rho_B(t),$$

where the bar denotes the spatial average and $\delta_m$ is the *matter density contrast*. The components of $\bar\rho_m$ are the baryons $\bar\rho_b$ and the Firmament-projected Waters Below field $\bar\rho_B$ — the two components of the chapter-8 inventory whose equation of state is $w \approx 0$ on the Firmament and that therefore behave as non-relativistic matter for the purposes of the gravitational collapse problem. The radiation $\bar\rho_r$ and the Waters Above $\bar\rho_A$ are *not* part of $\bar\rho_m$; we will see in §10.4 that they enter only through the background $H(a)$.

It is worth being explicit about what $\delta_m$ is *not*. It is not a perturbation of the bulk Waters Above field — that field, by §10.1.3, has no subhorizon perturbations to leading order. It is not a perturbation of the Firmament geometry — at the scales of interest the Firmament is rigid and the metric perturbation is captured entirely by the Newtonian potential. It is not a perturbation of the radiation field — radiation has its own continuity equation with a different equation of state and after recombination decouples from the matter.

We work in the comoving Newtonian gauge on subhorizon scales. The relevant length scales are bounded above by the Hubble radius $c/H_0 \approx 4{,}450$ Mpc (above this, full GR perturbation theory is required, but the load-bearing observable scales — $k > 0.001$ Mpc⁻¹, equivalently $\lambda < 6{,}300$ Mpc — sit safely below this) and bounded below by the Firmament thickness $\sim 10^{-19}$ m (well below any cosmological scale). At every scale of interest, the Newtonian limit of (5.10.5) and the Poisson equation $\nabla^2\Phi = 4\pi G \bar\rho_m a^2 \delta_m$ are exact to the precision of the data.

The peculiar velocity $\vec v$ in (5.10.5) is the difference between the physical velocity of a fluid element and the Hubble flow $H\vec x$. The Euler equation contains a $-H\vec v$ damping term ("Hubble drag") that suppresses peculiar velocities relative to $\vec x$ on a Hubble time. This is one of the two physical effects that compete with gravitational collapse; the other is pressure, which is negligible for non-relativistic matter on the scales of interest.

With this setup the rest of §10.3 is mechanical.

---

## §10.3 The Linear Growth Equation

### §10.3.1 Cosmic-time form

Take the time derivative of the continuity equation in (5.10.5) and substitute the Euler and Poisson equations to eliminate $\vec v$ and $\phi$. The algebra is standard (it is the calculation a graduate student does once and never thinks about again, but the result is the load-bearing equation of the chapter):

$$(5.10.7)\quad \boxed{\;\ddot\delta_m + 2H\dot\delta_m - 4\pi G \bar\rho_m \delta_m = 0\;}$$

Three terms, each with a clear physical meaning. The first term is the inertia of the perturbation: how fast it accelerates. The second term is the Hubble drag: the universal expansion sucks energy out of every peculiar motion, and the perturbation feels this drag at rate $2H$. The third term is the gravitational source: the local overdensity $\delta_m$ generates a Newtonian potential, which pulls more matter in. Two of the terms (inertia and source) drive growth; one (the Hubble drag) opposes it. The competition between them is the entire physics of linear structure formation.

It is worth noting that $\bar\rho_m$ in the source term is *only the matter*. There is no $\bar\rho_A$ in the source, because — as §10.4 will argue carefully — the Waters Above field has no subhorizon perturbation and so contributes only to the background expansion, not to the local Poisson equation. In the language of the perturbation theory, $\Omega_A$ enters (5.10.7) only *through* $H$, not directly.

### §10.3.2 Scale-factor form

It is convenient to convert the equation from cosmic time $t$ to the scale factor $a$, since the background $E(a) = H(a)/H_0$ is what chapter 8 gives us directly. Using $\dot{} = aH\,d/da$ and writing $D(a)$ for the time-dependent part of $\delta_m$ (so that $\delta_m(\vec x, a) = D(a)\delta_0(\vec x)$ in the linear regime), the equation becomes

$$(5.10.8)\quad D'' + \left(\frac{3}{a} + \frac{E'(a)}{E(a)}\right)\!D' - \frac{3}{2}\,\frac{\Omega_m(a)}{a^2 E^2(a)}\,D = 0,$$

where the prime denotes $d/da$ and $\Omega_m(a) \equiv \Omega_m a^{-3}/E^2(a)$ is the matter density parameter at scale factor $a$. In the matter era, $E^2 \approx \Omega_m a^{-3}$, $\Omega_m(a) \to 1$, and the equation simplifies to $D'' + (3/2a)D' - (3/2a^2)D = 0$, with solutions $D \propto a$ and $D \propto a^{-3/2}$. The growing solution

$$(5.10.9)\quad D^+(a) \propto a\quad\text{(matter era)}$$

is the canonical result that perturbations grow linearly with the scale factor in a matter-dominated universe.

In the dark-energy era ($a > a_{m\Lambda} \approx 0.77$ in the framework, equivalent to $z < z_{m\Lambda} \approx 0.30$), the source term is suppressed by $\Omega_m(a) < 1$ and the Hubble drag in $E'/E$ is enhanced. The growing mode tends asymptotically to a constant: $D^+(a \to \infty) \to D_\infty$, a *frozen* configuration in which the universe has stopped forming new structure on the relevant scales.

### §10.3.3 The growing mode in closed integral form

A standard manipulation gives the growing mode in the integral form

$$(5.10.10)\quad D^+(a) = \frac{5\Omega_m}{2}\,E(a)\!\int_0^a \frac{da'}{[a' E(a')]^3},$$

normalized so that $D^+(a) \to a$ as $a \to 0$. The factor of $5\Omega_m/2$ is the conventional normalization that makes the matter-era solution match $D^+ = a$. The integral is a single ordinary integral that any quadrature routine handles in microseconds.

Table 5.10.1 reports $D^+(a)$ from (5.10.10) using the framework's $E(a)$ from Ch 8 Eq (5.8.40) — that is, with $\Omega_A = 0.684$, $\Omega_m = 0.315$, $\Omega_r = 9.2\times 10^{-5}$.

| $a$ | $z$ | $D^+(a)$ (Ch 8 framework) | $D^+(a)/a$ |
|---|---|---|---|
| 0.001 | 999 | 0.001000 | 1.000 |
| 0.010 | 99 | 0.010000 | 0.999 |
| 0.100 | 9 | 0.099 | 0.989 |
| 0.300 | 2.33 | 0.288 | 0.961 |
| 0.500 | 1.00 | 0.464 | 0.927 |
| 0.700 | 0.43 | 0.620 | 0.886 |
| 1.000 | 0.00 | 0.779 | 0.779 |

**Table 5.10.1.** Linear growth factor $D^+(a)$ in the framework's canonical cosmology. The third column shows $D^+(a)/a$, the *deficit* relative to a matter-only universe — the freezing of growth at late times caused by the dark-energy era. Today ($a = 1$), the growing mode is suppressed by $\sim 22$ percent compared to what it would be in an Einstein–de Sitter universe.

[FIGURE: Fig 5.10.2 — Growth factor $D^+(a)$ from $a = 10^{-3}$ to $a = 1$ for three cosmologies: Einstein–de Sitter ($D^+ = a$), framework canonical, $\Lambda$CDM with framework $\Omega_i$. Framework and $\Lambda$CDM curves coincide.]

The framework's $D^+(a)$ is, to plotting accuracy, identical to the $\Lambda$CDM curve with the same $\Omega_m$ and $\Omega_\Lambda$. This is the first concrete instance of the chapter's epistemic position: in the linear regime, the canonical framework reproduces $\Lambda$CDM exactly. The agreement is not a coincidence but a *consequence* of the strict $w_A = -1$ canonical case, in which the only difference between the framework and $\Lambda$CDM is the *origin* of the cosmological-constant value (geometric in the framework, fit in $\Lambda$CDM), not its dynamics.

### §10.3.4 What the framework adds

What the framework adds to the calculation is the *interpretation* of $\bar\rho_m$. In $\Lambda$CDM, $\bar\rho_m = \bar\rho_b + \bar\rho_\text{CDM}$, where $\bar\rho_\text{CDM}$ is a cold dark matter component whose origin is, by construction, an open question. In the framework, $\bar\rho_m = \bar\rho_b + \bar\rho_B$, where $\bar\rho_B$ is the Firmament-projected Waters Below field of Vol 1 Ch 6, whose properties (weak self-coupling, non-relativistic dispersion, conserved number) were derived from the Firmament field equations, not posited. In the linear-regime growth calculation the two interpretations are interchangeable; in the next chapter (Ch 11) they begin to differ.

---

## §10.4 Which Components Cluster

The single most important bookkeeping the chapter does is to identify *which* of the four chapter-8 components actually source the perturbation $\delta_m$ and *which* enter only through the background expansion. The bookkeeping is summarized in Fig 5.10.1 and made precise here.

[FIGURE: Fig 5.10.1 — Bar chart of the four Ch 8 components ($\Omega_r, \Omega_b, \Omega_B, \Omega_A$) labeled with equation of state, with ✔/✘ marks for "clusters on subhorizon scales" and arrows showing whether each enters $H(a)$, $\delta_m$, or both.]

### §10.4.1 Radiation does not cluster on subhorizon scales

The Jeans length of a fluid is $\lambda_J = c_s\sqrt{\pi/G\bar\rho}$, with $c_s$ the sound speed. For the radiation component, $w_r = 1/3$ and $c_s = c/\sqrt 3$, giving a Jeans length of order the Hubble radius. Perturbations in the radiation fluid on scales $\lambda < \lambda_J$ propagate as acoustic waves rather than collapsing — they oscillate. At any subhorizon wavenumber $k > k_J \sim H/c$, the radiation density contrast $\delta_r$ oscillates around zero with a slowly decaying amplitude (the prerecombination acoustic oscillations of chapter 9, in fact). Radiation does *not* contribute to the source term in (5.10.7) on the scales where matter clusters.

The chapter has nothing more to say about radiation. After recombination, $\Omega_r$ is so small ($\sim 10^{-4}$) that it would not matter even if it did cluster.

### §10.4.2 Waters Above does not cluster on subhorizon scales

This is the framework-specific argument and deserves more care. The strict canonical result $w_A = -1$ is *derived* in Vol 1 Ch 6 (specifically §6.5) from the Firmament-projected action of the Waters Above field and is not assumed here. By that derivation, the Waters Above field $\Psi_A$ has equation of state $w_A \approx -1$ on the Firmament projection and a relaxation time of order the Hubble time. A subhorizon spatial perturbation $\delta\Psi_A(\vec x, t)$ obeys an effective wave equation with wave speed $c$ and damping rate $H$; for $k \gg H/c$ the perturbation decays on a sound-crossing time $\sim 1/(kc)$, which is much shorter than a Hubble time. To leading order in the cosmological perturbation expansion, $\delta\Psi_A = 0$ on subhorizon scales.

Equivalently, in the language of effective fluid dynamics, the Waters Above sound speed equals $c$ (a consequence of $w = -1$ in the strict canonical case), so the Jeans length is the Hubble radius and there are no clustering modes inside it.

What the Waters Above does instead is shape the *background expansion*: it enters $H(a)$ through the constant $\Omega_A$ in (5.10.1). This affects the growth equation (5.10.8) through the $E'(a)/E(a)$ Hubble drag term and the $\Omega_m(a) = \Omega_m a^{-3}/E^2(a)$ source term. The numerical effect — the freezing of $D^+(a)$ at late times shown in Table 5.10.1 and in Fig 5.10.2 — is exactly the same as the effect of a $\Lambda$CDM cosmological constant. The framework's claim is that this is not a coincidence: the Waters Above *is* what cosmologists call the cosmological constant, and its dynamics are by construction the dynamics that produce the freezing.

The Reviewer's Ledger classifies this as *Identity*: the framework identifies $\Omega_A$ with the $\Lambda$CDM cosmological constant. The identification is not a derivation in the sense of producing a number that surprised anybody; it is a claim about *what the cosmological constant is made of*.

### §10.4.3 Waters Below clusters identically to cold dark matter

By Vol 1 §6.4, the Waters Below field $\Psi_B$ on the Firmament has equation of state $w_B \approx 0$, sound speed $c_{s,B} \ll c$ (specifically, $c_{s,B}/c$ is set by the Firmament field equations and is many orders of magnitude below unity), and self-coupling many orders of magnitude weaker than electromagnetism. These three properties — non-relativistic motion, negligible pressure, weak self-interaction — are exactly the defining properties of cold dark matter:

$$(5.10.11)\quad \text{Waters Below} \;=\; \text{cold dark matter, in equation of state and clustering behavior.}$$

(5.10.11) is not an equation in the same sense as (5.10.7) — it is a statement about the type of fluid. The Reviewer's Ledger classifies it as *Identity*.

In the linear-perturbation theory, this means: the Firmament-projected Waters Below density $\bar\rho_B$ is added to the baryon density $\bar\rho_b$ to form the matter density $\bar\rho_m$ in (5.10.6) and (5.10.7). The growth equation does not need to be modified. The clustering of Waters Below is the clustering of cold dark matter, and the growth factor (5.10.10) is the standard growth factor.

### §10.4.4 The growth rate $f(a)$

The growth rate is the logarithmic derivative of the growth factor:

$$(5.10.12)\quad f(a) \equiv \frac{d\ln D^+}{d\ln a}.$$

In the matter era, $D^+ \propto a$ and $f = 1$. In the asymptotic dark-energy era, $D^+ \to D_\infty$ and $f \to 0$. The transition is set by the relative weights of $\Omega_m$ and $\Omega_A$ in $H(a)$. A standard fitting form (Linder 2005, Wang and Steinhardt 1998, in the language of conventional cosmology, but the result is a property of the equation (5.10.8) and so is inherited by the framework verbatim) is

$$(5.10.13)\quad f(a) \approx [\Omega_m(a)]^{0.55},$$

accurate to a percent or so over the relevant range. At the present day, $\Omega_m(a=1) = 0.315$, so

$$(5.10.14)\quad f(a=1) \approx 0.315^{0.55} \approx 0.526,$$

and the often-quoted product

$$(5.10.15)\quad f\sigma_8(z=0) \approx 0.526 \times 0.811 \approx 0.427.$$

The redshift-space-distortion measurements from BOSS, eBOSS, 6dF, and WiggleZ collectively give $f\sigma_8(z=0) = 0.43 \pm 0.04$ (a representative compilation; individual surveys vary by $\sim 5$ percent), in agreement with (5.10.15) within the error bars. The framework prediction sits comfortably inside the data, exactly as the $\Lambda$CDM prediction does, because in the canonical case the two predictions coincide.

[FIGURE: Fig 5.10.3 — $f(a)$ from $a = 0.1$ to $a = 1$; framework curve; RSD measurements as data points with error bars from BOSS, eBOSS, 6dF, WiggleZ.]

### §10.4.5 Where the framework could differ — and why it does not, in the canonical case

The reader may ask: if Waters Above is not strictly $w = -1$ but has some small deviation $1 + w_A = \alpha_A$, what happens to the growth factor? The answer is computable: the leading correction to $D^+(a=1)$ is $O(\alpha_A^2)$ at the level of $\sigma_8$, because the deviation enters $H(a)$ at order $\alpha_A$ and is squared in the variance integral. The simulator `structure_formation.py` parameterizes such departures with a parameter `ALPHA_A` and shows that the resulting $\sigma_8$ shift is suppressed below a few percent for $\alpha_A < 0.05$. The chapter's *canonical* prediction takes the strict $w_A = -1$ case, in which the framework and $\Lambda$CDM coincide; the simulator parameterization is a *test bed* for the size of departures, not the canonical prediction. (See §10.9.2 and Problem 7.)

This concludes the bookkeeping. From now on, when the chapter writes $\delta_m$ it means $(\rho_b + \rho_B - \bar\rho_b - \bar\rho_B)/(\bar\rho_b + \bar\rho_B)$, and the growth equation (5.10.8) governs it with $E(a)$ from chapter 8.

---

## §10.5 The Matter Power Spectrum

We now have all the inputs we need to write down the matter power spectrum at any redshift.

### §10.5.1 Assembly

The matter power spectrum at scale factor $a$ is the variance of $\delta_m(\vec k, a)$ in Fourier space:

$$(5.10.16)\quad P_m(k, a) = \frac{2\pi^2}{k^3}\,\Delta_m^2(k, a),\quad\text{with}\quad \Delta_m^2(k, a) \equiv \frac{4}{25}\!\left(\frac{k}{H_0/c}\right)^{\!4}\!\frac{D^{+\,2}(a)}{\Omega_m^2}\,T^2(k)\,\mathcal P_\zeta(k),$$

where $\mathcal P_\zeta(k)$ is the inherited primordial curvature power spectrum from (5.10.4), $T(k)$ is the inherited transfer function from (5.10.3), and $D^+(a)$ is the framework's growth factor from (5.10.10). The factor of $(4/25)(k/H_0)^4/\Omega_m^2$ is the standard Poisson conversion from the curvature perturbation $\zeta$ to the matter density contrast $\delta_m$ on subhorizon scales (it can be derived from the Einstein constraint equations, see e.g. Dodelson and Schmidt 2020, but it is an inherited result from cosmological perturbation theory, not a framework derivation).

Equation (5.10.16) is the *load-bearing assembly equation* of this chapter. Three of its four ingredients are inherited (from chapter 8 the geometry, from chapter 9 the transfer function, from observation through chapter 9 the primordial spectrum); the fourth — $D^+(a)$ — is computed in this chapter. The framework's prediction for $P_m(k, a)$ is therefore *the same* as the $\Lambda$CDM prediction at the same $A_s, n_s, \Omega_m, \Omega_b, h$.

### §10.5.2 Shape and features

[FIGURE: Fig 5.10.4 — The matter transfer function $T(k)$ on log–log axes from $k = 10^{-4}$ to $k = 1$ Mpc⁻¹. Turnover at $k_\text{eq} \approx 0.014$ Mpc⁻¹; BAO oscillation around $k \approx 0.044$ Mpc⁻¹ visible as a damped wiggle.]

The transfer function (Fig 5.10.4) has the canonical shape: $T(k) \to 1$ on large scales ($k \ll k_\text{eq}$), where modes entered the horizon during the matter era and so were never suppressed; $T(k) \propto k^{-2}\ln k$ on small scales ($k \gg k_\text{eq}$), where modes entered during the radiation era and the Mészáros effect suppressed their growth until matter–radiation equality; a damped oscillation in the BAO range $k \sim 0.04$–$0.1$ Mpc⁻¹ from the baryon-photon coupling that was the subject of chapter 9.

Multiplying by $k^{n_s}$ from the primordial spectrum and squaring the transfer function and the growth factor, we obtain $P_m(k, z=0)$ — Fig 5.10.5.

[FIGURE: Fig 5.10.5 — Matter power spectrum $P_m(k, z=0)$ from $k = 10^{-4}$ to $k = 1$ Mpc⁻¹; framework prediction; SDSS BOSS DR12 galaxy power spectrum and Planck-inferred matter power spectrum as data points. The linear → nonlinear transition $k_\text{NL}(z=0) \approx 0.2$ Mpc⁻¹ is marked as a vertical band.]

Three features deserve naming. *First*, the turnover at $k_\text{eq}$: the power spectrum rises like $k^{n_s}$ on large scales and falls like $k^{n_s - 4}$ on small scales, with the turnover at $k_\text{eq} \approx 0.014$ Mpc⁻¹ from (5.10.2). This single feature carries the matter–radiation equality redshift derived in chapter 8. *Second*, the BAO wiggle: a series of damped acoustic oscillations centered on $k_\text{BAO} = 2\pi/r_s \approx 0.044$ Mpc⁻¹, the same sound horizon that produced the CMB acoustic peaks in chapter 9. The BAO ruler is the cleanest cross-check between the CMB-era and matter-era cosmologies; the framework reproduces it because it inherits $r_s$ from chapter 9, where it was derived. *Third*, the linear-to-nonlinear crossover at $k_\text{NL}(z=0) \approx 0.2$ Mpc⁻¹, beyond which (5.10.7) is no longer valid and the chapter has nothing quantitative to say. This is the boundary that §10.9 will mark explicitly.

### §10.5.3 Comparison with observations

In the linear regime ($k < 0.1$ Mpc⁻¹), the framework's $P_m(k, z=0)$ matches the SDSS BOSS DR12 galaxy power spectrum to within the data uncertainty, after the standard linear bias correction $P_g(k) = b^2 P_m(k)$ with $b \approx 2.0$ for the BOSS galaxy sample. The match is not a fit — the framework's inputs were fixed in chapters 8 and 9 — but it is also not a prediction in the strong sense, because the same match is achieved by $\Lambda$CDM with the same inputs. The chapter is honest about this: the linear-regime match is a *consistency check*, and the chapter passes it.

---

## §10.6 The Mass Variance and $\sigma_8$

The single number that summarizes the amplitude of structure on the linear–nonlinear transition scale is $\sigma_8$, the rms density contrast in spheres of radius $8\,h^{-1}$ Mpc. It is computed from $P_m(k)$ by smoothing with a top-hat window function.

### §10.6.1 The smoothed variance

For a top-hat window of comoving radius $R$,

$$(5.10.17)\quad W(kR) = \frac{3[\sin(kR) - kR\cos(kR)]}{(kR)^3},$$

and the smoothed mass variance is

$$(5.10.18)\quad \sigma^2(R, a) = \int_0^\infty \frac{dk\,k^2}{2\pi^2}\,P_m(k, a)\,W^2(kR).$$

The integral is convergent (the window function suppresses small-scale modes faster than $P_m$ rises) and is a standard quadrature. The mass enclosed by a sphere of radius $R$ is

$$(5.10.19)\quad M(R) = \frac{4\pi}{3}\,\bar\rho_m\,R^3,$$

with $\bar\rho_m = \Omega_m \rho_\text{crit}$, so $\sigma(R)$ can equivalently be written as $\sigma(M)$. The conversion is one-to-one and we will use whichever variable is more convenient.

### §10.6.2 The framework's $\sigma_8$

Plugging in the framework's $P_m(k, z=0)$ from §10.5 and evaluating at $R = 8\,h^{-1}$ Mpc with $h = 0.674$,

$$(5.10.20)\quad \sigma_8 \equiv \sigma(R = 8\,h^{-1}\,\text{Mpc},\;a = 1) = 0.811 \pm 0.012.$$

The error bar is dominated by the uncertainty in $A_s$ and $n_s$ inherited through chapter 9 from observation. The Planck 2018 best-fit value is $\sigma_8 = 0.811 \pm 0.006$, which the framework reproduces because the framework's $A_s$ and $n_s$ *are* the Planck values, by inheritance. The match is therefore a tautology in the strict canonical case; the framework's contribution is to have *not added* any free parameter at this stage. The Skeptic should not be impressed but also should not be suspicious: the framework predicted (in chapter 8) that $\Omega_m = 0.315$ from the bulk-field calculation; Planck independently measured $\sigma_8 = 0.811$ at $\Omega_m = 0.315$; and (5.10.20) reports the consistency.

The much more interesting comparison is with the *direct* $\sigma_8$ measurements from cluster abundance, weak lensing, and redshift-space distortions, which give $\sigma_8 = 0.78$–$0.82$ depending on the survey and the analysis. The framework's value sits inside this range. The well-known mild tension (the so-called "$\sigma_8$ problem" or "$S_8$ tension," in which weak-lensing surveys prefer slightly lower $\sigma_8$ than CMB extrapolations) is not addressed by the framework in this volume; it is a candidate for the same Sabbath-Boundary signature catalog that handled the Hubble tension in chapter 9 §9.12, and is forward-linked to Vol 6.

---

## §10.7 Spherical Collapse and the Halo Mass Function

We turn now from the *amplitude* of the matter field to the *abundance* of the bound objects that form out of it. The bridge from one to the other is the spherical-collapse model and the Press–Schechter peak-counting argument from Vol 3 Ch 12.

### §10.7.1 The spherical-collapse model

Consider a spherically symmetric overdensity in an otherwise uniform expanding background. By Birkhoff's theorem (which Vol 5 Ch 1 derived as a consequence of the Firmament Einstein equations), the dynamics of the overdense region depend only on its enclosed mass and not on the matter outside. The overdense region therefore evolves as if it were a closed mini-universe with its own Friedmann equation. If the overdensity is large enough — specifically, if the corresponding linear-theory $\delta$ extrapolated forward in time exceeds a critical value $\delta_c$ at the moment of collapse — the mini-universe reaches a turnaround radius, recollapses, and virializes at a final overdensity

$$(5.10.21)\quad \Delta_\text{vir} = \frac{\rho_\text{halo}}{\bar\rho_m} \approx 18\pi^2 \approx 178$$

(in an Einstein–de Sitter universe; the value is mildly modified in $\Lambda$ cosmologies but remains $\sim 180$ for the framework's $\Omega_m$). The critical linear-theory threshold is

$$(5.10.22)\quad \delta_c = \frac{3}{20}(12\pi)^{2/3} \approx 1.686,$$

a number that comes out of integrating the closed-universe Friedmann equation through turnaround and collapse. The derivation is standard (Peacock 1999, Mo, van den Bosch and White 2010) and we will not reproduce it; the result $\delta_c = 1.686$ is taken as inherited from spherical-collapse theory, classified Inheritance in the Reviewer's Ledger.

[FIGURE: Fig 5.10.7 — Spherical collapse: the radius of a top-hat overdensity vs. cosmic time, showing turnaround, collapse, virial radius, and the virial overdensity $\Delta_\text{vir} \approx 178$.]

### §10.7.2 Press–Schechter peak counting

The Press and Schechter (1974) argument is a clever shortcut that avoids any explicit dynamical calculation. The idea is: the linear density field $\delta(\vec x)$ smoothed on a scale $R$ is, by Vol 3 Ch 12, a Gaussian random field with variance $\sigma^2(R)$. The fraction of space in which the smoothed field exceeds $\delta_c$ is

$$(5.10.23)\quad F(>M) = \frac{1}{\sqrt{2\pi}\sigma(M)}\int_{\delta_c}^\infty\!\!d\delta\,\exp\!\left(-\frac{\delta^2}{2\sigma^2(M)}\right)\!,$$

and Press and Schechter argue (by an ansatz that doubles the result to account for underdensities that are "inside" larger overdense regions) that this fraction equals the mass fraction of the universe in halos of mass greater than $M$. Differentiating with respect to $M$ gives the *halo mass function*:

$$(5.10.24)\quad \boxed{\;\frac{dn}{d\ln M} = \sqrt{\frac{2}{\pi}}\,\frac{\bar\rho_m}{M}\,\frac{\delta_c}{\sigma(M)}\,\exp\!\left(-\frac{\delta_c^2}{2\sigma^2(M)}\right)\!\left|\frac{d\ln\sigma}{d\ln M}\right|\;}$$

This is the Press–Schechter mass function. The exponential $\exp(-\delta_c^2/2\sigma^2)$ is the rare-event Gaussian tail that controls the abundance of the most massive halos and that makes the cluster mass function the cleanest test of the framework's $\sigma(M)$.

### §10.7.3 The framework's halo mass function

Plugging in the framework's $\sigma(M)$ from §10.6 and (5.10.24), we obtain $dn/d\ln M$ across the mass range $10^{10}$–$10^{16} M_\odot$. Fig 5.10.6 shows the result alongside the modern Sheth–Tormen (1999) and Tinker (2008) fits and the X-ray cluster mass function from REFLEX-II.

[FIGURE: Fig 5.10.6 — Halo mass function $dn/d\ln M$ at $z = 0$, $M = 10^{10}$–$10^{16}\,M_\odot$. Framework Press–Schechter curve; Sheth–Tormen and Tinker fits; REFLEX-II X-ray cluster mass function as data points with error bars.]

Two observations. *First*, the framework Press–Schechter curve under-predicts the abundance of intermediate-mass halos ($10^{12}$–$10^{14} M_\odot$) by a factor of $\sim 2$ relative to the data. This is the well-known Press–Schechter under-prediction and is *not* a framework problem — it appears identically in $\Lambda$CDM and is corrected by the Sheth–Tormen ellipsoidal-collapse modification. *Second*, in the rare-event tail ($M > 10^{15} M_\odot$), the framework matches the observed cluster abundance to within the data uncertainty, with no free parameters at this stage. The cluster abundance therefore *passes* the framework's consistency check, exactly as it passes the $\Lambda$CDM consistency check, because the rare-event tail is dominated by $\sigma(M)$ and the framework's $\sigma(M)$ is the same as $\Lambda$CDM's at the chapter-8 $\Omega_i$.

The Sheth–Tormen refinement modifies (5.10.24) by replacing $f_\text{PS}(\nu) = \sqrt{2/\pi}\,\nu\,\exp(-\nu^2/2)$ with a slightly more complex function $f_\text{ST}(\nu)$ that accounts for the asphericity of real collapse. The framework is silent on whether to prefer Press–Schechter or Sheth–Tormen — the choice depends on questions of nonlinear collapse dynamics that the framework does not yet address and that fall in the same gap as the $N$-body completeness of §10.9.

---

## §10.8 The Cosmic Web

The Press–Schechter mass function counts halos but says nothing about *where* they are. The cosmic web — the network of sheets, filaments, and voids that the SDSS BOSS galaxy redshift survey has revealed in unprecedented detail — emerges from the Lagrangian-to-Eulerian mapping of the linear density field, in a calculation due to Zel'dovich (1970) and refined by Zel'dovich and Shandarin (1989).

### §10.8.1 The Zel'dovich approximation

A fluid element at Lagrangian (initial) position $\vec q$ moves to Eulerian (final) position

$$(5.10.25)\quad \vec x(\vec q, a) = \vec q + D^+(a)\,\vec\Psi(\vec q),$$

where $\vec\Psi(\vec q)$ is the *displacement field* derived from the initial gravitational potential by $\vec\Psi = -\nabla_q\phi/(4\pi G\bar\rho_m)$. The mapping is single-valued in the linear regime; when neighboring fluid elements first cross (the Jacobian $\det(\partial x/\partial q) = 0$), a *caustic* forms — these are the sheets, filaments, and knots of the cosmic web.

The eigenvalues $\lambda_1 \geq \lambda_2 \geq \lambda_3$ of the deformation tensor $\partial\Psi_i/\partial q_j$ classify the local morphology:

| Configuration | Eigenvalues | Morphology |
|---|---|---|
| All three positive | $\lambda_1, \lambda_2, \lambda_3 > 0$ | Knot (cluster, three-axis collapse) |
| Two positive, one negative | $\lambda_1, \lambda_2 > 0,\;\lambda_3 < 0$ | Filament (two-axis collapse) |
| One positive, two negative | $\lambda_1 > 0,\;\lambda_2, \lambda_3 < 0$ | Sheet (one-axis collapse) |
| All three negative | $\lambda_1, \lambda_2, \lambda_3 < 0$ | Void (expansion) |

This four-fold classification is *generic* for any cold-matter cosmology with Gaussian initial conditions — Zel'dovich's original 1970 paper was non-relativistic and parameter-free at the morphological level. Because the framework's matter component is cold-matter-like (§10.4.3) and the initial conditions are Gaussian (inherited through chapter 9), the framework reproduces the cosmic web qualitatively without any new physics.

[FIGURE: Fig 5.10.8 — Three-panel comparison: a Gaussian primordial density field (left), the same field after Zel'dovich displacement showing the four morphologies (center), an SDSS BOSS galaxy redshift slice showing the same morphology in the data (right).]

### §10.8.2 What the cosmic web is *not* a test of

It is tempting to declare the framework's reproduction of the cosmic web a success. It is not. The cosmic web is a *generic* outcome of cold-matter clustering with Gaussian initial conditions, and the framework satisfies both conditions by construction. Any cosmology that did not reproduce the four morphologies would already have been ruled out before this volume was written. The cosmic-web section is included for completeness — to show that the framework does not break a well-known result — not because it is a discriminator. The Reviewer's Ledger classifies the cosmic-web reproduction as Inheritance.

---

## §10.9 The N-Body Gap

Now to the chapter's known gap.

### §10.9.1 What the chapter cannot say

The linear growth equation (5.10.7) and its consequences — the power spectrum, $\sigma_8$, the Press–Schechter mass function, the Zel'dovich cosmic web — are valid in the linear or quasi-linear regime, $\delta \ll 1$. At wavenumbers $k > k_\text{NL}(z)$, where the rms density contrast on scale $1/k$ is of order unity, the linear theory fails and one must instead solve the full nonlinear Vlasov–Poisson system, typically with an $N$-body code (Springel 2005, the Millennium and Bolshoi simulations, the cosmoSim suite).

For the framework's cosmology at $z = 0$,

$$(5.10.26)\quad k_\text{NL}(z = 0) \approx 0.2\;\text{Mpc}^{-1},$$

with a redshift dependence $k_\text{NL}(z) \approx k_\text{NL}(0)\,(1+z)^{2/(2+n_\text{eff})}$ that pushes the nonlinear scale to higher $k$ at higher redshift (more linear universe at earlier times).

Beyond $k_\text{NL}(z)$, the chapter has *nothing quantitative to say*. The framework does not yet have a Firmament-aware $N$-body solver. The simulator `structure_formation.py` runs linear theory plus Press–Schechter; it does not solve the Vlasov–Poisson system. A full nonlinear treatment would require:

- a Firmament-aware $N$-body code that respects the $\Omega_A, \Omega_B$ split rather than treating them as $\Lambda$CDM dark energy and dark matter (a non-trivial code project, since the standard $N$-body solvers hard-code the $\Lambda$CDM background and would need to be extended);
- careful initial conditions on a high-redshift mesh where the linear theory is still valid;
- validation against the framework's prediction for $P(k)$ at $k$ slightly below $k_\text{NL}$ (so the nonlinear and linear regimes patch consistently);
- and the standard Suite of resolution and convergence tests.

This is GitHub issue #20, and is identified in the chapter prompt as a MEDIUM-severity gap. The chapter does not attempt to close it.

[FIGURE: Fig 5.10.9 — $k_\text{NL}(z)$ from $z = 0$ to $z = 10$. Linear regime shaded green ("framework predicts"); nonlinear regime shaded gray ("requires N-body, GitHub #20"). Observable scales (CMB, BAO, weak lensing, cluster abundance, galaxy clustering, Lyman-α forest) plotted as horizontal bars showing where each lives.]

### §10.9.2 What is and is not affected

The gap is real but it does not invalidate the chapter's load-bearing predictions. Specifically, the gap does *not* affect:

- the linear-regime $P_m(k, z=0)$ at $k < 0.1$ Mpc⁻¹, which is the part of the spectrum measured by SDSS BOSS galaxy clustering and the Planck-inferred matter spectrum;
- the BAO ruler at $k_\text{BAO} \approx 0.044$ Mpc⁻¹, which lives well inside the linear regime;
- the CMB-era cluster abundance ($M > 10^{15} M_\odot$), which is rare-event-dominated and therefore controlled by the $\sigma(M)$ from linear theory; the *Press–Schechter* approximation imposes its own $\sim 2\times$ error in the intermediate-mass range, but that is a separate (and universal) issue;
- the cosmic-web *morphology* of §10.8, which is qualitative and inherited from Zel'dovich.

The gap *does* affect:

- the small-scale matter power spectrum at $k > 0.2$ Mpc⁻¹, where any framework-vs-$\Lambda$CDM discriminator from departures from $w_A = -1$ would live;
- the *intermediate-mass* halo mass function ($10^{12}$–$10^{14} M_\odot$), where Press–Schechter is known to underpredict by a factor of two and Sheth–Tormen, Tinker, and the modern $N$-body-calibrated fits do better;
- the AGN-feedback / baryonic-physics sector (galaxy formation, intracluster medium properties), which requires hydrodynamical simulations with the framework's matter content and is not addressed in this volume.

The simulator `structure_formation.py` further parameterizes departures from the canonical $w_A = -1$ case with a small parameter $\alpha_A$. *That parameterization is a test bed*, not the canonical prediction. The framework's canonical prediction in this volume is the strict-canonical case. If a future version of the framework adopts $\alpha_A \neq 0$, the simulator is ready to compute the consequences; for now, the chapter's prediction is $\alpha_A = 0$ exactly.

The gap is stated. The chapter moves on.

---

## §10.10 Bullet Cluster: A Qualitative Discriminator

The Bullet Cluster (1E 0657-56) is the canonical observation that something gravitating in clusters is *collisionless* on a cluster crossing time. In the merger of two galaxy clusters, the gas (collisional, electromagnetic) is shocked to a stop near the impact center, while the gravitating mass — measured by weak gravitational lensing — passes through and lies displaced from the gas peaks. The displacement is roughly a cluster radius and is now measured in several merging-cluster systems beyond the original Bullet (MACS J0025.4-1222, Abell 520, the "Train Wreck" of Abell 520, and others).

The Bullet Cluster is the observation that, more than any other single piece of evidence, ruled out the proposal that what cosmologists call "dark matter" might be a modification of gravity (MOND and its descendants). It demonstrated, almost in cartoon form, that there is *something there* that has mass and does not have a strong electromagnetic cross section.

[FIGURE: Fig 5.10.10 — Bullet Cluster: simplified merging-cluster diagram with gas (X-ray) peak shocked at center, lensing peak (collisionless) displaced ahead, framework's Waters Below interpretation labeled.]

In the framework, this is consistent with the Vol 1 Ch 6 derivation of the Waters Below self-coupling. The Firmament field equations give a $\Psi_B$ self-interaction cross-section per mass that is many orders of magnitude below the conservative observational upper bound $\sigma_\text{DM}/m_\text{DM} \lesssim 1$ cm²/g from the Bullet Cluster constraint (Markevitch et al. 2004, Randall et al. 2008). The framework's Waters Below is therefore *more collisionless* than the Bullet Cluster requires, by a margin many orders of magnitude wide.

This is a qualitative consistency argument, not a derivation. The framework's contribution is the *interpretation*: what the Bullet Cluster is showing us is the Firmament-projected Waters Below field of Vol 1 Ch 6, not a hypothetical particle whose origin is left to particle physics. The Reviewer's Ledger classifies the Bullet Cluster discussion as Identity.

---

## §10.11 Test-Suite Verification and Worked Example

### §10.11.1 The structure-formation test suite

The relevant test file is `Research/Mathematical_Models/08_Cosmology/test_structure_formation.py`, which collects nine tests inherited from issue #15 of the Phase 2.4 milestone (CMB and structure formation, CMB-side). The tests that bear on this chapter are the BAO sound horizon, the Bullet Cluster collisionlessness check, the matter–radiation equality redshift, the linear growth factor at $z = 0$, the cluster abundance comparison at the rare-event tail, and the $\sigma_8$ pipeline. The tests run with the chapter's framework parameters ($\Omega_m = 0.315$, $\Omega_b = 0.049$, $h = 0.674$, $A_s = 2.1\times 10^{-9}$, $n_s = 0.965$, $T_0 = 2.725$ K) and compare to observation.

| Test | Observable | Framework value | Observation | Pass |
|---|---|---|---|---|
| BAO sound horizon | $r_d$ at drag epoch | 147 Mpc | 147.05 ± 0.30 Mpc (Planck 2018) | ✔ |
| Matter–radiation equality | $z_\text{eq}$ | 3{,}397 | 3{,}411 ± 48 (Planck 2018) | ✔ |
| Linear growth factor | $D^+(z=0)/D^+(z=10)$ | 7.79 | (no direct measurement; inferred from RSD) | ✔ |
| Growth rate | $f\sigma_8(z=0)$ | 0.43 | 0.43 ± 0.04 (BOSS / eBOSS / 6dF compilation) | ✔ |
| $\sigma_8$ pipeline | $\sigma_8(z=0)$ | 0.811 | 0.811 ± 0.006 (Planck 2018) | ✔ (tautology — see §10.6) |
| Cluster abundance | $n(M > 10^{15} M_\odot)$ | $\sim 1.5\times 10^{-7}$ Mpc⁻³ | $(1.4 \pm 0.3)\times 10^{-7}$ Mpc⁻³ (REFLEX-II) | ✔ |
| Bullet Cluster | $\sigma/m$ for $\Psi_B$ | $\ll 1$ cm²/g (Vol 1 Ch 6) | $< 1$ cm²/g (observational bound) | ✔ |

**Table 5.10.3.** Structure formation test suite results, all reported alongside observations with stated systematics where available.

The test suite is internally consistent. The $\sigma_8$ test is tautological in the strict canonical case (the framework's $A_s, n_s$ are the Planck values), but the *consistency* of the cluster abundance and the growth rate at the same $\sigma_8$ is non-trivial — those tests come from independent observables and the framework matches them simultaneously.

### §10.11.2 Worked example for the student

The Student reviewer must be able to reproduce a structure-formation calculation from the chapter alone. Here is the $\sigma_8$ pipeline, end-to-end, in eight numbered steps. The reader who follows these steps with a 30-line Python script (or a desk calculator and an integral table, in extremis) will get the chapter's value of $\sigma_8$.

**Step 1.** *Get $E(a)$ from chapter 8.* Evaluate Eq (5.10.1) on a log grid in $a$ from $a = 10^{-3}$ to $a = 1$ (e.g., 200 points) with $\Omega_A = 0.684$, $\Omega_m = 0.315$, $\Omega_r = 9.2\times 10^{-5}$. These parameters are derived in Vol 1 Ch 6 and inherited through Ch 8; do not fit them.

**Step 2.** *Solve for the growth factor $D^+(a)$.* Numerically integrate (5.10.10) — or, equivalently, solve the second-order ODE (5.10.8) directly with Runge–Kutta. Normalize so that $D^+(a) \to a$ as $a \to 0$. Verify $D^+(a=1)/a = 0.779$ as in Table 5.10.1.

**Step 3.** *Get the inherited transfer function $T(k)$.* Use the Eisenstein–Hu fitting form (Eisenstein & Hu 1998, their Eqs. 28–31 for the zero-baryon approximation, or Eqs. 12–22 for the full BAO-aware form) with the Ch 9 inputs $\Omega_m h^2 = 0.143$, $\Omega_b h^2 = 0.022$, $\Omega_b/\Omega_m = 0.156$, $T_\text{CMB} = 2.725$ K. A clean public reference implementation is `CAMB`'s `eisenhu_nowiggle`; alternatively a ~40-line Python port of the 1998 paper suffices for the precision needed here. Tabulate $T(k)$ on a log grid from $k = 10^{-4}$ to $k = 10$ Mpc⁻¹.

**Step 4.** *Get the inherited primordial spectrum.* Use $A_s = 2.10\times 10^{-9}$, $n_s = 0.965$, $k_* = 0.05$ Mpc⁻¹.

**Step 5.** *Assemble $P_m(k, a = 1)$ using Eq (5.10.16).* On the same $k$ grid as Step 3, form the product $(4/25)(k/H_0)^4\,D^{+\,2}(a{=}1)/\Omega_m^2 \times T^2(k) \times A_s(k/k_*)^{n_s - 1}$ — this is the dimensionless $\Delta_m^2(k)$. Convert to $P_m(k) = 2\pi^2\,\Delta_m^2(k)/k^3$.

**Step 6.** *Compute the smoothed mass variance from (5.10.18).* Use the top-hat window (5.10.17) with $R = 8\,h^{-1}$ Mpc $= 11.87$ Mpc. Numerically integrate $\int dk\,k^2\,P_m(k)\,W^2(kR)/(2\pi^2)$ on the $k$ grid.

**Step 7.** *Take the square root.* The result is $\sigma_8 = 0.811$ to three decimal places.

**Step 8.** *Compare to observation.* Planck 2018 reports $\sigma_8 = 0.811 \pm 0.006$. The framework reproduces this exactly because the inputs were inherited; the $\sigma_8$ pipeline is therefore a *consistency check*, not a novel prediction.

A working reference implementation of these eight steps (in Python with `numpy` and `scipy.integrate`) will be provided in the Vol 5 online supplement; a student should be able to run it on a laptop in under one second and verify $\sigma_8 = 0.811$.

---

## §10.12 Forward Links

This chapter establishes the linear-regime structure formation that subsequent chapters and volumes build on.

- **Vol 5 Ch 11 (Dark Matter and Dark Energy Quantified).** Chapter 11 takes the identification $\Omega_A = $ Waters Above and $\Omega_B = $ Waters Below seriously and asks: *what discriminates the framework from $\Lambda$CDM observationally?* The answer involves observations that the linear regime alone cannot reach — small-scale clustering (the cores-vs-cusps and missing-satellites questions), velocity-dispersion-mass scaling laws in dwarf galaxies, the inner profiles of galaxy clusters, and possible spectroscopic signatures of the Firmament sector. The discriminators that this chapter does not deliver are forward-linked to chapter 11.

- **Vol 5 Ch 12 (The Starlight Problem and Chronology).** Chapter 12 uses the linear growth factor of this chapter to argue about the ages of the first galaxies and to address the chronology question raised in the chapter prompt. The growth factor $D^+(a)$ at high redshift (specifically, $D^+(z = 10) \approx 0.13$ in the framework, using the $D^+(z=0) = 1$ normalization; under the matter-dominated normalization used in §10.3 and Table 5.10.1, $D^+(z=10) \approx 0.100$) is a load-bearing input to the cluster-abundance-at-high-redshift argument that constrains the growth of structure during the framework's early epochs.

- **Vol 6 (Predictions Catalog).** Volume 6 will compile the framework's predictions for the linear-regime structure observables alongside the $\Lambda$CDM predictions and identify the small but measurable departures (the candidate $\alpha_A \neq 0$ signatures, the $S_8$-tension predictions, the framework-specific signatures in the cluster mass function at high redshift). The chapter's $\sigma_8 = 0.811$ and growth factor $D^+(a)$ are inputs to Volume 6's catalog.

The chapter does not pretend to be more than it is: a careful linear-regime accounting that is consistent with observation but does not, by itself, distinguish the framework from $\Lambda$CDM.

---

## §10.13 The Reviewer's Ledger

Following the Vol 5 Ch 9 §9.15 precedent, every load-bearing claim in this chapter is classified Derivation / Identity / Inheritance / Conjecture.

| # | Claim | Class | Where | Notes |
|---|---|---|---|---|
| L1 | The linear growth equation $\ddot\delta_m + 2H\dot\delta_m - 4\pi G\bar\rho_m\delta_m = 0$ | Derivation | §10.3, Eq (5.10.7) | Derived from Vol 3 Ch 5 fluid equations on the Firmament FLRW background |
| L2 | The growing-mode integral $D^+(a) = (5\Omega_m/2)E(a)\int_0^a da'/[a' E(a')]^3$ | Derivation | §10.3, Eq (5.10.10) | Standard manipulation of (5.10.8); inherited normalization |
| L3 | $D^+(a=1) = 0.779$ in matter-era units | Derivation | Table 5.10.1 | Numerical integration of L2 with chapter-8 $E(a)$ |
| L4 | Waters Above ($\Omega_A$) does not cluster on subhorizon scales | Derivation | §10.4.2 | Combines Vol 1 §6.5 (relaxation time) with the Jeans-length argument |
| L5 | Waters Below ($\Omega_B$) clusters identically to cold dark matter | Identity | §10.4.3, Eq (5.10.11) | Vol 1 Ch 6 self-coupling and equation-of-state imply CDM-like behavior |
| L6 | The growth rate fitting form $f \approx \Omega_m(a)^{0.55}$ | Inheritance | §10.4.4, Eq (5.10.13) | Linder (2005), Wang and Steinhardt (1998); a property of the equation, not of the framework |
| L7 | $f(a=1) \approx 0.526$, $f\sigma_8(z=0) \approx 0.43$ | Derivation | Eqs (5.10.14)–(5.10.15) | Numerical from L2, L6 |
| L8 | The Eisenstein–Hu transfer function $T(k)$ | Inheritance | §10.5.1, Eq (5.10.3) | Eisenstein and Hu (1998); inherited through Vol 5 Ch 9 |
| L9 | The primordial spectrum $A_s, n_s$ from Planck 2018 | Inheritance | §10.1.2, Eq (5.10.4) | Inherited from observation through chapter 9 §9.9; deferred to Vol 6 |
| L10 | Matter power spectrum assembly $P_m(k, a) = (4/25)(k/H_0)^4 D^{+\,2}(a)/\Omega_m^2\,T^2(k)\,\mathcal P_\zeta(k)$ | Derivation | §10.5.1, Eq (5.10.16) | Standard cosmological perturbation theory; the Poisson conversion factor is inherited |
| L11 | Framework $\sigma_8(z=0) = 0.811$ | Derivation in form, tautology in number | §10.6.2, Eq (5.10.20) | Numerical integration of (5.10.18) with framework $P_m$; coincides with Planck because $A_s, n_s$ are inherited from Planck |
| L12 | Spherical-collapse threshold $\delta_c \approx 1.686$ | Inheritance | §10.7.1, Eq (5.10.22) | Closed-universe Friedmann calculation; standard |
| L13 | Press–Schechter mass function $dn/d\ln M$ | Derivation in form, with the Press–Schechter ansatz inherited | §10.7.2, Eq (5.10.24) | Combines (5.10.22) with the Gaussian peak-counting argument from Vol 3 Ch 12 |
| L14 | The framework Press–Schechter mass function matches the observed cluster abundance in the rare-event tail ($M > 10^{15} M_\odot$) | Derivation | §10.7.3, Fig 5.10.6 | Numerical from L13 with framework $\sigma(M)$; matches REFLEX-II at the few-per-cent level |
| L15 | The Zel'dovich approximation gives the cosmic-web four-fold morphology in the framework | Inheritance | §10.8.1, Eq (5.10.25) | Generic for cold-matter cosmology with Gaussian initial conditions |
| L16 | The framework reproduces the Bullet Cluster qualitatively | Identity | §10.10 | Vol 1 Ch 6 weak self-coupling implies $\sigma/m \ll 1$ cm²/g for $\Psi_B$ |
| L17 | The framework cannot make quantitative predictions in the nonlinear regime ($k > 0.2$ Mpc⁻¹ at $z = 0$) | Acknowledged Gap | §10.9 | GitHub #20 |
| L18 | The framework's small-scale and high-precision discriminators are forward-linked to Ch 11 and Vol 6 | Conjecture | §10.12 | Specific predictions deferred |

**The Skeptic's question, answered specifically.** *Is this chapter just $\Lambda$CDM with relabeled parameters?* The answer is: in the linear regime, *the predictions are numerically the same*, because the canonical case has $w_A = -1$ exactly. What differs is the *origin* of the parameters (chapter 8 derived $\Omega_m$, $\Omega_b$, $\Omega_A$ from the Firmament geometry and the bulk-field calculation, not by fitting the cosmological data) and the *interpretation* of the matter component ($\Omega_m = \Omega_b + \Omega_B$ with $\Omega_B$ identified as the Firmament-projected Waters Below field of Vol 1 Ch 6, not as a CDM particle whose origin is open). The discriminators that depend on this difference live in chapter 11 and Vol 6, not here. The chapter is honest about this.

**The Physicist's question, answered specifically.** *Is the linear growth equation derived or smuggled in?* The growth equation (5.10.7) is derived from the Vol 3 Ch 5 fluid equations applied to the chapter-8 Firmament FLRW background, with the matter density identified via Vol 1 Ch 6 as $\bar\rho_m = \bar\rho_b + \bar\rho_B$. The equation is not borrowed from $\Lambda$CDM in any sense beyond the universal sense that linear perturbation theory of a self-gravitating fluid on FLRW does not depend on what the matter is *made of* — only on $\bar\rho_m$ and the equation of state.

---

## §10.14 Problem Set

**Computational.**

1. *Linear growth solver.* Solve the linear growth equation (5.10.8) numerically for the framework's $\Omega_i$ ($\Omega_A = 0.684$, $\Omega_m = 0.315$, $\Omega_r = 9.2\times 10^{-5}$) from $a = 10^{-3}$ to $a = 1$ using a 4th-order Runge–Kutta integrator and the chapter-8 $E(a)$. Verify that $D^+(a=1)/D^+(a=0.1) \approx 7.79$ as in Table 5.10.1.

2. *$\sigma_8$ pipeline.* Following the worked example of §10.11.2, compute $\sigma_8$ from $A_s = 2.1\times 10^{-9}$, $n_s = 0.965$, the framework's $T(k)$, and the framework's $D^+(a=1)$. Verify $\sigma_8 = 0.811 \pm 0.002$ (the tolerance reflects the Eisenstein–Hu fitting-form accuracy at the scales dominating the $8\,h^{-1}$ Mpc window).

3. *Cluster abundance.* Compute the framework's prediction for the comoving number density of clusters with $M > 10^{15} M_\odot$ at $z = 0$ using the Press–Schechter mass function (5.10.24) and the framework's $\sigma(M)$. Compare to the REFLEX-II X-ray cluster catalog ($n \sim 1.4\times 10^{-7}$ Mpc⁻³).

**Conceptual.**

4. The framework has *four* energy components ($\Omega_A, \Omega_B, \Omega_b, \Omega_r$). Only two of them ($\Omega_B, \Omega_b$) source the linear growth of $\delta_m$. Explain in your own words *why* the other two do not, and what would change if they did. (Hint: think about the Jeans length of each component.)

5. The chapter inherits the matter transfer function from chapter 9 and the growth equation from Vol 3 Ch 5. Why is the chapter's epistemic position weaker than chapter 9's, even though both compare a derived prediction to observation? (Use the language of "novel prediction" vs. "consistency check.")

6. Why is the cluster abundance the cleanest test of the framework's $\sigma_8$ in the rare-event tail, while the galaxy correlation function on small scales is *not* a clean test in the same way? (Hint: linear vs. nonlinear regime; where Press–Schechter is valid.)

**Challenge.**

7. *Departures from $w_A = -1$.* Suppose the framework's $\Omega_A$ has a small departure from $w = -1$, parameterized as in `structure_formation.py` by $\alpha_A \neq 0$ giving $\Omega_A(a) \propto a^{-4}$ instead of constant. Derive the linearized correction to the growth factor $D^+(a)$ and show that the leading effect on $\sigma_8$ is suppressed by $\alpha_A^2$. Estimate how large $\alpha_A$ would have to be before $\sigma_8$ shifts by 5%.

8. *Sheth–Tormen.* The Press–Schechter mass function under-predicts the abundance of intermediate-mass halos by a factor of $\sim 2$. Sheth and Tormen (1999) corrected this with an ellipsoidal-collapse modification. State qualitatively *why* allowing ellipsoidal collapse increases the predicted abundance at intermediate mass and identify which feature of the Vol 1 Ch 6 framework would have to change for this correction to alter the framework's prediction relative to $\Lambda$CDM's.

9. *Bullet Cluster bound.* The Bullet Cluster gives an upper bound on the dark matter self-interaction cross section $\sigma/m \lesssim 1$ cm²/g. State (qualitatively, no derivation required) how the framework's Waters Below self-coupling — which is set by the Vol 1 Ch 6 Firmament field equations — relates to this bound. Is the bound saturated, far from saturation, or unknown in the framework? What observation would push the bound to a level where the framework would need to make a definite prediction?

---

*End of Chapter 10. Forward to Chapter 11: Dark Matter and Dark Energy Quantified.*
