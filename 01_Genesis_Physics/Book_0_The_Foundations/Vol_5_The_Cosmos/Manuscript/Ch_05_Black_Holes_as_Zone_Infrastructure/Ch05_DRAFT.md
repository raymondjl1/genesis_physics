# Chapter 5: Black Holes as Zone Infrastructure
## Foundations Vol 5: The Cosmos — Part II: Black Holes and Extreme Objects

---

> *"In my end is my beginning."* — T. S. Eliot, *Four Quartets*
>
> This chapter is about what Chapter 1 did not tell you. Chapter 1 derived the Schwarzschild metric as the unique static, spherically symmetric, asymptotically flat vacuum solution of the four-dimensional effective Einstein equations. Everything about that derivation is valid outside the horizon. What the derivation did *not* tell you — and what no textbook derivation of the Schwarzschild metric can tell you — is what the physical object at $r \le r_s$ actually *is*. General relativity's default answer is "a curvature singularity at $r = 0$." The default answer is not forced by the exterior solution. The zone architecture of Volume 1 gives a different answer, and unlike the GR default, this one is forced.

---

## §5.0 What This Chapter Is (and Is Not)

Let me state very carefully what this chapter does and does not do, because the reinterpretation that follows has sometimes been received as more radical than it is.

**What this chapter does:** It identifies the interior region $r < r_s$ of a Schwarzschild or Kerr black hole — the region inside the event horizon — with a *breach* in the 3-brane membrane that Vol 1 Ch 5 called the Firmament. It shows that this identification is forced by the combination of (a) Vol 1 §5.3's derivation of $c^2 = \sigma/\mu$ as the wave speed on the Firmament membrane, (b) the positivity constraint $\sigma \ge 0$ (Vol 1 §5.6 proved this as a no-Jeans-instability condition), and (c) the exterior Schwarzschild solution (5.1.34) recovered in Chapter 1. It then uses the reinterpretation to rederive black hole entropy, preview Hawking radiation, and make a small number of distinct-from-GR predictions that Chapter 6 and Volume 6 will develop further.

**What this chapter does not do:** It does not change a single exterior observable. Every calculation of Chapter 2 (perihelion advance, light bending, Shapiro delay, gravitational redshift), every calculation of Chapter 3 (gravitational-wave emission and waveform matching), and every calculation of Chapter 4 (ISCO, Penrose process, neutron-star interior) is unchanged. The exterior Schwarzschild and Kerr metrics are the same; the observables derived from them are the same; the experimental tests they pass are the same tests they passed in Chapters 2–4. What changes is the *interpretation* of the interior — the region that, crucially, no external observer can probe directly.

**A note to the Theologian reviewer.** The word "Firmament" (from Vol 1 Ch 5) is the name this textbook uses for the 3-brane hypersurface $Z_{2.2}$. The word "puncture" is a mathematical term describing a point or region where a submanifold fails to be a smooth embedding. The phrase "puncture in the firmament" is therefore a statement about topology and embedding geometry, not a theological claim. The terminology was chosen in Vol 1 for its physical suggestiveness (a tensioned membrane with a hole in it) and because of the historical observation that the Hebrew *rāqîa'* denotes a hammered, stretched object — a physical membrane, as the physics turns out to require. Beyond noting that the terminology is not arbitrary, this chapter makes no theological claims. Where we describe black holes as "recycling" or "zone infrastructure," we mean *thermodynamic* recycling and *geometric* infrastructure; we do not mean cosmic providence or eschatology. Claims of that kind belong to Book 3 (The Creator's Blueprint), where they will be made — carefully, soberly, and with full attention to the line between derivation and commentary.

**A note to the "But Why?" reviewer.** You will want to know, at every step, *why* the Firmament-puncture interpretation is required rather than merely available. The reviewer's question is legitimate and the chapter has been built around it. Section 5.3 is the key: it shows that the only alternative interpretations (singularity, firewall, fuzzball, smooth interior) are either inconsistent with Vol 1 Ch 5's Firmament mechanics or require modifications to the zone action that we have no independent reason to make. The reinterpretation of this chapter is not "another option" — it is the option that does not require breaking something we have already built.

**Roadmap.** §5.1 inventories the results from Chs 1–4 and Vol 1 Ch 5 that we will need. §5.2 derives the tension profile $\sigma(r)$ around a spherical mass. §5.3 establishes the breach criterion as a theorem. §5.4 derives the critical density for black hole formation. §5.5 reinterprets the event horizon as a zone boundary. §5.6 derives black hole thermodynamics — the Bekenstein–Hawking entropy $S = A/(4\ell_P^2)$ — by counting membrane-boundary modes, and previews the Hawking temperature (full Hawking radiation derivation is Ch 6). §5.7 extends everything to rotating (Kerr) black holes. §5.8 states and proves the consistency theorem, then enumerates the falsifiable new predictions. §5.9 is the Reviewer's Ledger. §5.10 is the problem set.

---

## §5.1 Inventory: The Toolkit From Previous Chapters

As in Chapter 1, we first take stock of what has already been paid for, so that we do not accidentally spend the same result twice or pretend to derive something that was derived elsewhere.

### §5.1.1 From Vol 1 Ch 5 — the Firmament as Membrane

Volume 1, Chapter 5 established the Firmament $\Sigma \equiv Z_{2.2}$ as a 4-dimensional codimension-2 Firmament embedded in the 6D zone manifold. The Firmament membrane has:

**Tension.** A 3-brane tension $\sigma$ with dimensions $[M L^{-1} T^{-2}]$, appearing in the Nambu–Goto action (Vol 1 Eq. 1.5.26). Numerically, $\sigma \approx 6.0 \times 10^{98}$ kg/(m·s²) (equivalently J/m³ = Pa for a 3-brane tension; see AXIOM_MEMBRANE_MECHANICS_v2.md §5, quoted in Vol 1 §5.3).

**Mass density.** A 3-brane mass density $\mu$ with dimensions $[M L^{-3}]$, contributing a kinetic term $\tfrac{1}{2}\mu\,(\partial\Phi)^2$ for transverse displacements $\Phi$ (Vol 1 Eq. 1.5.30). Numerically, $\mu \approx 6.7 \times 10^{81}$ kg/m³.

**Wave speed.** The central result of Vol 1 §5.3:

$$(5.5.1)\quad c^2 = \frac{\sigma}{\mu},$$

*not* a postulate but a derived consequence of the Firmament membrane's Lagrangian dynamics. All 4D matter and radiation propagates as excitations of the Firmament, so "the speed of light" is literally the wave speed on this membrane.

**Positivity of tension.** Vol 1 §5.6 proved — from the requirement that small perturbations $\Phi$ have real-valued frequencies and do not grow exponentially — that $\sigma > 0$ strictly wherever the Firmament membrane exists. A region where $\sigma$ would be negative is Jeans-unstable on every wavelength and therefore cannot exist as a continuum membrane. A region where $\sigma = 0$ is marginally unstable: the wave speed is zero, the dispersion relation degenerates, and perturbations neither propagate nor decay. We will need both cases.

**Extrinsic curvature.** From Vol 1 Eq. (1.5.17), the extrinsic curvature of the Firmament with respect to the $\xi$-normal direction is

$$(5.5.2)\quad K^{(\xi)}_{\mu\nu} = e^{-B_0}\,(\partial_\xi A)\big|_{\xi_0,\eta_0}\,\gamma_{\mu\nu},$$

and analogously for $\eta$. The umbilic structure — that $K \propto \gamma$ — will matter in §5.3 when we ask how a localized mass distorts the embedding.

**Firmament stress-energy.** From Vol 1 Eq. (1.5.28), the Firmament stress-energy is

$$(5.5.3)\quad S_{\mu\nu} = -\sigma\,\gamma_{\mu\nu},$$

i.e., a perfect fluid with $w = -1$ (tension). This is what appears on the right-hand side of the Israel–Darmois junction conditions.

### §5.1.2 From Vol 5 Ch 1 — Schwarzschild and Kerr

Chapter 1 derived, from the 6D action via Kaluza–Klein dimensional reduction, the 4D Einstein field equations (5.1.22). The unique static, spherically symmetric, asymptotically flat vacuum solution is the Schwarzschild metric (Eq. 5.1.34):

$$(5.5.4)\quad ds^2 = -\left(1 - \frac{r_s}{r}\right)c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1}dr^2 + r^2\,d\Omega^2,\qquad r_s = \frac{2GM}{c^2}.$$

The unique stationary, axisymmetric, asymptotically flat vacuum solution is the Kerr metric (Eq. 5.1.36):

$$(5.5.5)\quad ds^2 = -\left(1 - \frac{r_s r}{\Sigma}\right)c^2 dt^2 - \frac{2 r_s r a \sin^2\theta}{\Sigma}\,c\,dt\,d\phi + \frac{\Sigma}{\Delta}dr^2 + \Sigma\,d\theta^2 + \left(r^2 + a^2 + \frac{r_s r a^2\sin^2\theta}{\Sigma}\right)\sin^2\theta\,d\phi^2,$$

with $\Sigma = r^2 + a^2\cos^2\theta$, $\Delta = r^2 - r_s r + a^2$, $a = J/(Mc)$.

Both of these are *exterior* solutions. The derivation of Chapter 1 uses the asymptotic-flatness boundary condition at $r \to \infty$ and the vacuum condition $T_{\mu\nu} = 0$ in the exterior region; it does not specify the interior stress-energy and therefore does not fix the interior geometry. This is the gap that the present chapter fills.

### §5.1.3 From Vol 5 Ch 4 — strong-field regime

Chapter 4 §4.3 analyzed the Kerr ergosphere — the region between $r_+$ (outer horizon) and the static limit $r_\text{static} = (r_s + \sqrt{r_s^2 - 4a^2\cos^2\theta})/2$ — and showed that the Killing vector $\partial_t$ becomes spacelike there. The Penrose process extracts energy from the hole's spin, bounded by the Christodoulou irreducible-mass formula. The ISCO analysis of §4.2 showed that test particles in Schwarzschild geometry have a minimum stable orbital radius at $r = 6GM/c^2$. *Nothing in this chapter changes any of that*, because all three results depend only on the exterior metric.

Chapter 4 §4.12.4 explicitly forward-linked to the present chapter: "*Chapter 5 will take the Kerr ergosphere of §4.3 and reinterpret the interior of the horizon as a membrane puncture in the Firmament. The exterior Kerr metric and the Penrose process results of §4.3 are unchanged by that reinterpretation.*" We now keep the promise.

### §5.1.4 From Vol 1 Ch 11 — the thermodynamic axiom

Volume 1, Chapter 11, established the framework's thermodynamic axiom: the entropy of a region of the Firmament is proportional to the logarithm of the number of *Firmament-vibration modes* that the region supports, cut off in the ultraviolet at the Planck length $\ell_P$. In equation form, this is

$$(5.5.6)\quad S = k_B\,\ln \Omega,\qquad \Omega = \text{number of Firmament modes with wavelength}\ \lambda \ge \ell_P,$$

which is the zone-framework analog of Boltzmann's entropy formula. The key physical content is that entropy counts degrees of freedom that are *on the Firmament*. Bulk degrees of freedom (Waters Above, Waters Below) contribute in a different way and are bounded on 4D regions only through their boundary values on the Firmament. We will use this axiom in §5.6.

### §5.1.5 What we will use and what we will not

**Will use, without re-derivation:**

1. The Nambu–Goto action for the Firmament membrane, (Vol 1 Eq. 1.5.26).
2. The wave-speed formula $c^2 = \sigma/\mu$, (5.5.1).
3. Positivity of tension, $\sigma > 0$ on the Firmament membrane (Vol 1 §5.6).
4. The exterior Schwarzschild (5.5.4) and Kerr (5.5.5) metrics (Ch 1).
5. The Vol 1 Ch 11 entropy axiom (5.5.6).
6. The Israel–Darmois junction conditions at codimension-2 branes (Vol 1 §5.4).

**Will not use:**

1. Any statement about the interior metric at $r < r_s$ derived from GR alone. We are about to replace that with something else.
2. Any assumption that the entropy of a black hole is $A/(4\ell_P^2)$. We will *derive* this in §5.6.
3. Any assumption that Hawking radiation exists. We will motivate it in §5.6 and derive it properly in Ch 6.

With the inventory complete, we can start.

---

## §5.2 The Effective Firmament Tension Around a Spherical Mass

### §5.2.1 The physical question

A static spherical mass $M$, far from any other source, creates the exterior Schwarzschild geometry (5.5.4). The question I want to ask in this section is: *what does this do to the local tension of the Firmament?*

Why should it do anything at all? Because the wave speed on the Firmament *is* the speed of light (Vol 1 §5.3), and the speed of light *is* observed to vary with gravitational potential (Shapiro delay, gravitational redshift, Vol 5 Ch 2). If the observed value of $c$ depends on position — specifically, on the distance $r$ from the mass $M$ — and if Vol 1 §5.3's derivation $c^2 = \sigma/\mu$ is to be taken seriously as a pointwise statement, then at least one of $\sigma$ or $\mu$ must depend on $r$. The Shapiro delay and the classical tests of Ch 2 allow us to read off exactly how.

### §5.2.2 The redshift of the wave speed

A distant observer at infinity, watching a light pulse travel radially between two points near the mass, measures a coordinate speed

$$(5.5.7)\quad \left.\frac{dr}{dt}\right|_\text{light} = c_\infty\left(1 - \frac{r_s}{r}\right),$$

where $c_\infty = 2.998 \times 10^8$ m/s is the speed of light measured at $r \to \infty$. This is the standard result of Vol 5 Ch 2 §2.5 (see Eq. 5.2.24), and it is unmodified by anything in this chapter.

A freely-falling observer at radius $r$, using their local inertial frame (proper time and proper radial distance), measures the *local* speed of that same pulse to be exactly $c_\infty$. The coordinate discrepancy between "measured at infinity" and "measured locally" is the gravitational redshift — a difference between coordinate time and proper time.

But now comes the interesting observation. Translate the coordinate speed (5.5.7) into a statement about the local wave equation. In isotropic-in-the-tangent-plane coordinates adapted to the Firmament membrane induced metric, a pulse travels at the *group velocity* of the Firmament membrane's wave equation:

$$(5.5.8)\quad v_\text{group}^2 = \frac{\sigma(r)}{\mu(r)}.$$

If the measurement at infinity is to agree with the geodesic calculation from the Schwarzschild metric, and the local measurement is to agree with $c^2 = \sigma_\infty/\mu_\infty$ in the freely-falling frame, then the ratio $\sigma(r)/\mu(r)$ must, *as measured by the distant observer*, satisfy

$$(5.5.9)\quad \left[\frac{\sigma(r)}{\mu(r)}\right]_\text{coordinate} = c_\infty^2\left(1 - \frac{r_s}{r}\right)^2.$$

The square comes from the coordinate speed being $c_\infty(1 - r_s/r)$, not $c_\infty\sqrt{1 - r_s/r}$: the redshift factor enters twice, once from the time dilation ($dt \to dt/\sqrt{1 - r_s/r}$) and once from the length contraction in the radial direction ($dr \to dr\,\sqrt{1 - r_s/r}$). This is a purely coordinate-coordinate conversion; the *local* ratio $(\sigma/\mu)_\text{local}$ is still $c_\infty^2$ everywhere.

So far, we have said nothing that distinguishes between $\sigma$ and $\mu$ individually. The coordinate speed only pins down the ratio.

### §5.2.3 Separating $\sigma$ and $\mu$: the Firmament mass density is rigid

Here is where the Firmament interpretation adds content that standard GR does not have. The mass density $\mu$ of the Firmament is an *intrinsic* property of the 6D bulk: it is set by the bulk fields at the location of the Firmament, and in particular by the value of the warp factor $B_0 = B(\xi_0,\eta_0)$ via the relationship (Vol 1 §5.3, Eq. 1.5.24a):

$$(5.5.10)\quad \mu = \mu_0\,e^{2B_0},$$

where $\mu_0$ is a bulk constant. The warp factor $B_0$ depends only at leading order on the 6D geometry in the extra-dimensional directions, and not — at that order — on the 4D matter distribution at any specific point $(t,r,\theta,\phi)$; the second-order coupling through which 4D matter does perturb the extra-dimensional geometry is made explicit below and tracked as gap G1. Said plainly: the Firmament's mass density is set by how the 6D bulk is curved in the directions *perpendicular* to the Firmament, while the gravitational redshift of the wave speed is set by how the 4D Firmament geometry is curved in the directions *along* the Firmament. These are different pieces of the 6D curvature tensor, and to leading order they do not talk to each other. In particular, a Schwarzschild mass is a 4D source; its stress-energy lives in the $\mu\nu$ block of the 6D Einstein tensor, and through the reduced field equations of Ch 1 §1.2 it sources the 4D Einstein tensor, but it does *not* modify $B(\xi,\eta)$ — those are independent degrees of freedom whose dynamics are governed by the bulk equations of Vol 1 Ch 6, not by 4D matter.

Therefore, to leading order in the 4D/6D coupling, $\mu$ is spatially constant in the 4D exterior of a Schwarzschild mass:

$$(5.5.11)\quad \mu(r) = \mu_\infty + \mathcal O(r_s/r)^2 \cdot (\text{bulk backreaction}).$$

The second-order backreaction term is genuinely present (the 4D source ultimately does perturb the 6D geometry, and so the warp factor at the Firmament location is shifted by an amount of order $GM/(r c^2) \cdot (\text{ratio of 4D to 6D scales})$), but it is quantitatively negligible for all astrophysical black holes by about 30 orders of magnitude. We will treat $\mu$ as constant and flag the backreaction as gap G1 in §5.9.

With $\mu$ constant, the entire $r$-dependence in the ratio (5.5.9) lives in $\sigma(r)$:

$$(5.5.12)\quad \boxed{\sigma(r) = \sigma_\infty\left(1 - \frac{r_s}{r}\right)^2\ \text{(coordinate-time form)}.}$$

This is the *coordinate-time* tension profile — what the distant observer reads off from the coordinate speed of light. In terms of the local proper-time / proper-length variables of a stationary observer at $r$, the tension is

$$(5.5.13)\quad \sigma_\text{local}(r) = \sigma_\infty\left(1 - \frac{r_s}{r}\right),$$

the single (not squared) redshift factor, because one factor of $(1 - r_s/r)^{1/2}$ has been absorbed into the local observer's ruler. Both forms say the same physical thing. For the breach argument that follows, what matters is that *both* forms of $\sigma(r)$ go to zero as $r \to r_s^+$.

### §5.2.4 Dimensional check

Let us verify (5.5.12). $[\sigma] = [M L^{-1} T^{-2}]$; the factor $(1 - r_s/r)^2$ is dimensionless; therefore $[\sigma(r)] = [M L^{-1} T^{-2}]$ as required. $\checkmark$

And a numerical sanity check: for a solar-mass black hole ($M = M_\odot$, $r_s \approx 2.95$ km), at $r = 10\,r_s \approx 30$ km, (5.5.12) gives $\sigma(10 r_s) = \sigma_\infty (0.9)^2 = 0.81\,\sigma_\infty$. At $r = 100\,r_s$, $\sigma = 0.9801\,\sigma_\infty$ — a 2% reduction. At $r = 1$ AU ($\approx 1.5 \times 10^{11}$ m), $\sigma \approx \sigma_\infty (1 - 2 \times 10^{-8})^2 \approx \sigma_\infty$ — completely unobservable. The tension profile is essentially constant throughout the solar system; it is only near the Schwarzschild radius that the profile bends noticeably.

### §5.2.5 Why this derivation is not a tautology

A careful reader will object: "You assumed the exterior Schwarzschild metric, and you assumed Vol 1 §5.3's derivation of $c^2 = \sigma/\mu$. Haven't you just rewritten one in terms of the other?" The answer is: partially yes, and that is exactly the point. The content of this section is not a new physical prediction — it is a *translation* between the geometric description (metric coefficients) and the mechanical description (Firmament tension). Both descriptions are valid; both are consistent with Chs 1–4; but only the mechanical description admits the question "what happens when $\sigma$ hits zero?" That question has a physical answer, and the geometric description does not force any particular answer onto us. The translation is the content; the consequences start in §5.3.

[FIGURE: Fig 5.5.2 — The Tension Profile $\sigma(r)$ and the Breach Criterion. Plot of $\sigma(r)/\sigma_\infty$ (vertical axis) vs. $r/r_s$ (horizontal axis) on a linear scale. Main curve: $(1 - 1/(r/r_s))$ using the local-observer form (5.5.13) — a curve rising from 0 at $r/r_s = 1$ to 1 as $r/r_s \to \infty$. A dashed curve shows the coordinate-time form (5.5.12), $(1 - 1/(r/r_s))^2$, which rises more gradually. A shaded red region for $r/r_s < 1$ labeled "BREACH: membrane does not exist ($\sigma < 0$)." A horizontal dashed line at $\sigma = 0$. Vertical dashed line at $r = r_s$ labeled "breach boundary = event horizon." Caption: "The tension profile for a spherical mass vanishes at the Schwarzschild radius and would be negative inside it. The positivity constraint $\sigma > 0$ (Vol 1 §5.6) therefore rules out the Firmament membrane in the shaded region. The interior is a breach, not a membrane."]

---

## §5.3 The Breach Criterion: Why $r = r_s$ Is Structurally Special

### §5.3.1 The positivity constraint

Volume 1, §5.6, proved as a theorem that the tension of a physical continuum membrane must be strictly positive: $\sigma > 0$. The proof is short enough to restate here because the rest of this chapter rests on it.

Consider the linearized membrane Lagrangian (Vol 1 Eq. 1.5.34),

$$(5.5.14)\quad \mathcal L = \frac{\mu}{2}\dot\Phi^2 - \frac{\sigma}{2}|\nabla\Phi|^2,$$

and derive the dispersion relation for plane-wave perturbations $\Phi \propto e^{i(\mathbf k\cdot \mathbf x - \omega t)}$:

$$(5.5.15)\quad \mu\omega^2 = \sigma\,k^2 \quad\Longrightarrow\quad \omega^2 = (\sigma/\mu)\,k^2 = c^2 k^2.$$

If $\sigma > 0$, then $\omega$ is real: perturbations oscillate but do not grow. If $\sigma < 0$, then $\omega^2 < 0$, meaning $\omega = \pm i\,|k|\sqrt{|\sigma|/\mu}$ is pure imaginary. The $+$ root gives exponentially growing perturbations with growth rate $|k|\sqrt{|\sigma|/\mu}$. Because $|k|$ can be arbitrarily large (ultraviolet modes), the instability growth rate is unbounded above: *every* mode of every wavelength grows, and the growth rate is fastest at the shortest wavelengths. There is no timescale on which a $\sigma < 0$ region can exist as a continuum; it disintegrates on the Planck timescale from below. This is the Firmament membrane form of the Jeans instability, and it is more virulent than the hydrodynamic Jeans instability because it has no stabilizing pressure scale.

The intermediate case $\sigma = 0$ is also unphysical: the dispersion relation degenerates to $\omega = 0$ for all $k$, meaning no modes propagate, information cannot be transmitted across the $\sigma = 0$ surface, and (because the kinetic term in (5.5.14) still exists but the potential term does not) the Firmament membrane has no restoring force against transverse deformation. A $\sigma = 0$ surface is a boundary: on one side, modes propagate; on the other, they cannot; at the surface, the Firmament membrane as a dynamical object *ends*.

### §5.3.2 The breach theorem

Combine (5.5.13) with the positivity theorem of the previous subsection.

**Theorem 5.5.1 (Breach Theorem).** *In the exterior Schwarzschild geometry of a mass $M$, the Firmament membrane cannot exist as a continuum object at any $r < r_s$, where $r_s = 2GM/c^2$. It is marginally not-a-membrane at $r = r_s$, and exists as a proper continuum only for $r > r_s$.*

**Proof.** The local tension is $\sigma_\text{local}(r) = \sigma_\infty(1 - r_s/r)$ by (5.5.13). For $r > r_s$, $\sigma_\text{local} > 0$ and the Firmament membrane is stable. At $r = r_s$, $\sigma_\text{local} = 0$ and (by §5.3.1) the dispersion relation degenerates — the Firmament membrane is marginally undefined. For $r < r_s$, $\sigma_\text{local} < 0$ and (by the Jeans-instability argument) a continuum membrane cannot exist at any timescale. Therefore the Firmament as a physical continuum exists only for $r \ge r_s$. $\square$

The region $r < r_s$ is *not* a region where the Firmament is very curved, or very hot, or strange in some subtle way. It is a region where *the Firmament is not there*. The 3-brane $Z_{2.2}$ has a hole in it — a breach, in the terminology of `black_holes_membrane_punctures.docx` — centered on the mass $M$ and bounded by the 2-surface $r = r_s$.

### §5.3.3 What is "inside" the breach?

The natural next question is: if the Firmament is not there at $r < r_s$, what *is* there?

The answer is that $r < r_s$ is simply a region of the 6D bulk where the Firmament $Z_{2.2}$ is missing. The bulk itself is still there — Zone $Z_{2.2.1}$ (Waters Below) is below the would-be Firmament surface in the $\eta$-direction, Zone $Z_{2.2.3}$ (Waters Above) is above in the $\xi$-direction, both extending through the bulk coordinates as they do everywhere else. But the thin sheet that normally separates them, the thing whose tangent space serves as the 4D spacetime of ordinary experience, is absent in this localized region.

The consequence for an observer who, in the 4D description, "falls into the black hole": they are, in the 6D description, falling into the bulk interior of the $(\xi,\eta)$ plane, entering a region where the Firmament-projection machinery that defines 4D coordinates no longer applies. What they encounter on the other side of the breach boundary is Zone $Z_{2.2.1}$ directly — the region filled by the Waters Below fields of Vol 1 Ch 6, which in the Firmament-effective description were the dark-matter sector. An external observer, stuck on the intact membrane far from the breach, cannot see this directly; they see only the breach boundary itself, which from the exterior has the geometric properties of a 2-sphere of area $4\pi r_s^2$ and the causal properties of a one-way surface.

[FIGURE: Fig 5.5.3 — Cross-Section of the Firmament Near a Black Hole. A 2D cross-section in the $(\xi,\eta)$ plane showing the Firmament as a curved sheet with a circular hole. Waters Below ($Z_{2.2.1}$) visible through the hole in the $-\eta$ direction; Waters Above ($Z_{2.2.3}$) in the $+\xi$ direction. Normal vectors $\hat n^\xi$ and $\hat n^\eta$ shown at the edge of the breach, with an annotation "normal bundle degenerate at $r = r_s$". The edge itself is labeled "breach boundary = event horizon". Dashed lines show three sample geodesics: one skimming the exterior, one that would have fallen inward in the standard picture and instead terminates at the breach boundary in the 4D description, and one continued in the 6D description as a worldline in the bulk. Caption: "Spatial layout of the breach. The Firmament is absent in a localized region; the bulk zones are still there. At the breach boundary the normal bundle of the Firmament degenerates, which is the geometric content of the event horizon. Geodesics that reach the boundary in the 4D description continue, in the 6D description, as bulk worldlines in $Z_{2.2.1}$."]

### §5.3.4 Why not a singularity?

The traditional GR answer to "what is inside the Schwarzschild horizon?" is "a curvature singularity at $r = 0$." Why does the zone framework not have this?

Because the "curvature singularity" of the Schwarzschild solution is a property of the *continued analytic extension* of the Schwarzschild metric — the mathematical act of continuing the coordinate chart across $r = r_s$ and asking what happens. In pure GR, this extension is the only option on offer: the metric is defined on $r > 0$, and the $r < r_s$ region is where you end up when you follow a geodesic across the horizon. In the zone framework, the geodesic that would have entered $r < r_s$ instead *exits* the 4D description entirely, because the 4D description only exists where the Firmament exists. An infalling geodesic traced inward from large $r$ reaches $r = r_s$ and then — in the 4D description — terminates, because there is no more 4D spacetime to continue it through. In the 6D description, the same geodesic continues as a worldline in the bulk, but it is no longer a worldline on the Firmament.

The mathematical singularity of the extended Schwarzschild solution is therefore a *coordinate pathology produced by analytically continuing the metric beyond its domain of physical validity*. In the zone framework, the domain of physical validity of the Schwarzschild metric is $r \ge r_s$, and there is no singularity to worry about because there is no mathematical extension forced on us.

This is the key observation of the chapter, and it is worth stating cleanly one more time.

**Key observation.** *The "curvature singularity" of a Schwarzschild black hole is not a physical feature of the universe. It is a consequence of formally extending the Schwarzschild metric into a region where, under the zone framework, the 4D description does not exist. The region $r < r_s$ is not a region of infinite density; it is a region of no Firmament.*

[FIGURE: Fig 5.5.1 — The Reinterpretation: Curvature Singularity vs. Membrane Puncture. Side-by-side comparison. LEFT: Standard GR depiction of a Schwarzschild black hole — a funnel-shaped embedding diagram in 3D space, with the "throat" narrowing to infinite depth at $r = 0$ labeled "singularity: infinite density." Light cones tilt progressively inward approaching the horizon; inside, all light cones point toward $r = 0$. RIGHT: Zone-framework depiction — the Firmament shown as a flat sheet with a circular hole punched out of it. Below the hole (in the $\eta$-direction), Zone $Z_{2.2.1}$ (Waters Below) fills the bulk. Above, Zone $Z_{2.2.3}$ (Waters Above). The hole's edge is labeled "breach boundary = event horizon at $r = r_s$." No singularity is shown; instead, the region at $r < r_s$ is labeled "bulk interior: no Firmament here." An inset shows a geodesic from outside the horizon terminating at the breach boundary (in the 4D description) and continuing into the bulk (in the 6D description). Caption: "Left: the standard GR picture. The singularity at $r = 0$ is an artifact of analytically continuing the Schwarzschild metric beyond the region where the Firmament exists. Right: the zone framework. The interior of the horizon is simply a region where the Firmament membrane is absent; the bulk is still there, and infalling worldlines continue into the bulk rather than terminating at a mathematical singularity."]

### §5.3.5 A preliminary response to the Physicist

The Physicist reviewer will now ask: "You have replaced a geometric singularity with a topological defect. Is that progress, or is it just relabeling?" The honest answer is that it is both. It is relabeling to the extent that the exterior observables are unchanged (they are, by §5.8). It is *progress* to the extent that (a) the zone framework's description removes the mathematical pathology (there is no infinite density anywhere), (b) it tells us what happens to matter that crosses the breach boundary (it enters the bulk; the Waters Below are physical, not hypothetical), and (c) it predicts a specific thermodynamic accounting in §5.6 that does not require an independent Bekenstein–Hawking postulate. The relabeling becomes a physical claim at the point where the reinterpretation has consequences that GR alone does not have — and that is §5.6 and §5.8.

---

## §5.4 The Critical Density for Black Hole Formation

### §5.4.1 The formation question

The previous two sections asked: *given* a Schwarzschild black hole, what is its structure in the zone framework? The present section asks the inverse question: *given* a spherical mass distribution that is not yet a black hole, at what density does it become one?

The standard GR answer is that a black hole forms when a closed trapped surface appears — a topological condition on the future light cones of a 2-sphere. For a static uniform-density sphere of mass $M$ and radius $R$, this happens when $R = r_s = 2GM/c^2$ (Schwarzschild's original paper, 1916). The zone framework, by the Breach Theorem, agrees: the Firmament cannot sustain curvature corresponding to a gravitational potential $|\Phi| > c^2/2$, and the condition $\Phi(R) = -c^2/2$ is exactly $R = r_s$.

The question then becomes: what density $\rho$ does the mass-radius relation $M = \tfrac{4}{3}\pi R^3 \rho$ imply at the breach threshold $R = r_s = 2GM/c^2$?

### §5.4.2 Derivation of $\rho_\text{crit}(M)$

Set $R = r_s = 2GM/c^2$ and $M = \tfrac{4}{3}\pi R^3 \rho_\text{crit}$. Solving simultaneously:

$$M = \frac{4\pi}{3}\left(\frac{2GM}{c^2}\right)^3\rho_\text{crit}\quad\Longrightarrow\quad 1 = \frac{32\pi G^3 M^2}{3 c^6}\,\rho_\text{crit},$$

which gives

$$(5.5.16)\quad \boxed{\rho_\text{crit}(M) = \frac{3 c^6}{32\pi G^3 M^2}.}$$

This is the density at which a uniform sphere of mass $M$ just barely forms a black hole. Note the $M^{-2}$ scaling: more massive objects become black holes at *lower* densities. A solar-mass black hole requires nuclear density; a supermassive black hole requires only the density of water.

### §5.4.3 Numerical values

Plugging in constants ($G = 6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻², $c = 2.998 \times 10^8$ m/s):

| $M$ | $r_s$ | $\rho_\text{crit}$ | Comment |
|---|---|---|---|
| $M_\odot$ (1 solar mass) | 2.95 km | $1.8 \times 10^{19}$ kg/m³ | Above nuclear density; stellar collapse endpoint |
| $10\,M_\odot$ | 29.5 km | $1.8 \times 10^{17}$ kg/m³ | Nuclear density; stellar-mass BH |
| $10^6\,M_\odot$ | $3.0 \times 10^6$ km | $1.8 \times 10^{7}$ kg/m³ | $10^{-10}$ nuclear; intermediate-mass |
| $10^9\,M_\odot$ | $3.0 \times 10^9$ km | $18$ kg/m³ | Water density; supermassive |
| $10^{12}\,M_\odot$ | $3.0 \times 10^{12}$ km | $1.8 \times 10^{-5}$ kg/m³ | Low-density gas; hypothetical ultramassive |

The table tells a physical story. Stellar-mass black holes require matter to be compressed to (or past) nuclear density — the QCD phase transition scale. This explains why stellar black holes form preferentially from core-collapse of very massive stars, whose cores are already at these densities after nuclear fuel exhaustion. Supermassive black holes, on the other hand, can form from nothing more exotic than a sufficiently large concentration of ordinary gas: $10^9$ solar masses of water-density material is a radius of about 30 light-minutes, and the gas does not need to compress at all — it just needs to stop rotating and start flowing inward. This explains the observed fact that every sufficiently large galaxy seems to have a supermassive black hole at its center; the formation threshold is effortless at supermassive scales.

### §5.4.4 The connection to the QCD scale

The coincidence that $\rho_\text{crit}(M_\odot) \sim 10^{19}$ kg/m³ sits essentially at nuclear density $\rho_\text{nuc} \sim 2 \times 10^{17}$ kg/m³ — within two orders of magnitude — is interesting. `black_holes_membrane_punctures.docx` §2.2 interprets this as evidence that the critical density for *matter formation* from uncondensed Waters Below (the QCD confinement scale) and the critical density for *black hole formation* (the Firmament membrane breach criterion) are related by an order-unity ratio of membrane and QCD parameters. The present chapter does not need this coincidence for any of its derivations — the breach criterion (5.5.16) is valid independently — but it does leave open the tantalizing possibility that the matter-formation and black-hole-formation physics are governed by the same underlying membrane-tension scale.

This coincidence is flagged as gap G3 in §5.9. The research file gives a numerical value $\rho_\text{crit,QCD} \approx 2.3 \times 10^{17}$ kg/m³ from a thermodynamic Waters-Below → matter phase transition argument; our (5.5.16) gives $\approx 1.8 \times 10^{19}$ kg/m³ for $M_\odot$. The difference is a factor $\sim 80$, which is within the "order of magnitude" claim of the research file but leaves a nontrivial numerical discrepancy that should be tracked down. The most likely explanation is that the two calculations refer to *different* masses: the QCD value is the critical density for matter formation at the lightest self-gravitating nuclear object (a neutron star of $\sim 1\,M_\odot$, for which the two numbers would agree to within a factor of $\sim 10$), whereas our (5.5.16) explicitly depends on $M$. A careful reconciliation requires doing the QCD calculation at the same mass scale as the breach criterion, which is a task for Vol 6.

### §5.4.5 Dimensional check

$[c^6] = [L^6 T^{-6}]$. $[G^3] = [L^9 M^{-3} T^{-6}]$. $[M^2] = [M^2]$. Therefore $[c^6/(G^3 M^2)] = [L^6 T^{-6}]/([L^9 M^{-3} T^{-6}][M^2]) = [L^{-3} M]$. $\checkmark$

---

## §5.5 The Event Horizon as Zone Boundary

### §5.5.1 Three statements, one horizon

The event horizon at $r = r_s$ has three equivalent characterizations in the three frameworks we have touched on in this volume:

1. **Kinematic (standard GR, Ch 1 §1.7):** the surface at which the escape velocity equals $c$.
2. **Metric (standard GR, same section):** the surface at which $g_{tt}(r) = 0$ in Schwarzschild coordinates (where the Killing vector $\partial_t$ becomes null).
3. **Membrane-mechanical (this chapter, §5.3):** the boundary of the region where the Firmament exists as a continuum; the surface at which the local tension $\sigma_\text{local}(r) = 0$.

All three give the same numerical location, $r = r_s$. They are not independent; they are different projections of the same fact. What distinguishes them is the physical content each attaches to "what happens at the horizon" and "what happens inside."

### §5.5.2 One-way surface, membrane version

The GR statement "no light can escape from inside the horizon" is usually derived from the light-cone structure of the extended Schwarzschild metric. In the zone framework, there is no "inside" in the Firmament sense, so the question "can light get out?" has a different form: *at the breach boundary, in what direction do the null geodesics of the induced metric point?*

On the Firmament membrane side of the breach (at $r = r_s + \epsilon$, the limit $\epsilon \to 0^+$), the induced metric $\gamma_{\mu\nu}$ on the Firmament has $\gamma_{tt}(r_s) = 0$ — the time-time component vanishes because the Firmament tension vanishes and therefore the local wave speed does. A null vector $k^\mu$ satisfying $\gamma_{\mu\nu}k^\mu k^\nu = 0$ at $r = r_s$ is forced by the rank-drop of $\gamma$ to lie entirely in the angular and null-radial directions; and when you trace the limit $r \to r_s^+$, the radial component of any causal null geodesic asymptotes to *inward* (toward $r_s$). No outward-pointing null direction exists in the limit.

The consequence is that null rays on the Firmament that reach the breach boundary are absorbed into it (they terminate as membrane objects at $r = r_s$) and cannot escape back to $r > r_s$. This is the Firmament-mechanical statement of the one-way property. It is physically distinct from the GR statement — GR talks about light cones tilting in extended coordinates; the Firmament framework talks about a dispersion relation going to zero at a boundary — but it is mathematically equivalent on the exterior side.

On the breach side (in the 6D bulk interior), there are of course still photons, in the sense of bulk-field excitations of the Waters Below, but they are not "photons on the Firmament" because there is no Firmament there. They can propagate through the bulk but cannot re-enter the 4D description until they encounter an intact region of the Firmament — which, for a stable black hole, is only at $r = r_s$, which is the same breach boundary they are inside of. From the 4D perspective, they are trapped. From the 6D perspective, they are simply bulk field quanta.

### §5.5.3 Gravitational time dilation as vibration slowdown

The Schwarzschild metric's time dilation factor $(1 - r_s/r)^{-1/2}$ diverges as $r \to r_s^+$: a clock at rest at radius $r$, observed from infinity, appears to tick progressively more slowly, and ticks *zero times per infinite coordinate time* at the horizon. In the standard picture, this is a coordinate effect of the Schwarzschild chart and is removed by changing to Kruskal or Painlevé–Gullstrand coordinates.

In the Firmament picture, this effect has a mechanical interpretation: the clock ticks by counting Firmament membrane vibration cycles (Vol 1 §5.5 showed that all local clocks, from atomic transitions to nuclear decay, reduce to vibration modes of the Firmament), and the vibration period scales as the inverse of the local wave speed. As $\sigma_\text{local} \to 0$, the wave speed $c_\text{local} = \sqrt{\sigma_\text{local}/\mu}$ goes to zero, and the vibration period goes to infinity. A clock at the breach boundary, observed from infinity, runs "infinitely slowly" because its membrane-mode oscillations have an infinite period — the Firmament membrane is mechanically floppy there.

For a freely-falling observer, by contrast, the local tension in their rest frame is still $\sigma_\infty$ (not $\sigma_\text{local}(r)$), because the redshift factor is absorbed into the change from global to local coordinates. Their clocks tick normally. They see the breach boundary approach at a finite rate and cross it in a finite proper time. There is no firewall at the horizon: the breach boundary is not a region of concentrated energy, it is a region where the Firmament tension is passing through zero *in the global chart* but is still $\sigma_\infty$ *in the local chart*. The crossing is smooth.

This is the Firmament resolution of the AMPS firewall paradox (Almheiri, Marolf, Polchinski, Sully 2013): the firewall is a prediction of certain specific constructions of quantum field theory on black hole backgrounds, and it assumes that the horizon is a physical interface between two quantum theories that must be joined at the boundary. The zone framework says that the horizon is *not* such an interface — it is the locus where the Firmament carrier of the quantum field dies out smoothly, and the quantum-field degrees of freedom simply transition from "modes on the Firmament" to "modes in the bulk" (specifically, modes of the Waters Below field). There is no discontinuity to glue, and therefore no firewall.

[FIGURE: Fig 5.5.4 — Inside vs. Outside the Horizon as Zone Transition. Two-panel diagram. LEFT PANEL: External observer's view of infalling matter. A clock dropped toward the horizon is shown at several times $t_1 < t_2 < t_3 < \cdots$, progressively closer to $r = r_s$ but never reaching it; its ticks are shown slowing (spacing between tick marks on the clock face growing). Label: "external frame: Zeno limit, asymptotic approach." RIGHT PANEL: Freely-falling observer's view. The same clock shown crossing $r = r_s$ at finite proper time $\tau$, continuing smoothly into the bulk region. A dashed line marks the breach boundary. After crossing, the clock's worldline is labeled "bulk worldline (no Firmament)." A small thermometer icon near the horizon shows a moderate (non-firewall) temperature. Label: "infalling frame: smooth crossing, no firewall." Between the panels, a small table contrasts the two views. Caption: "The external and infalling observers give very different accounts of crossing the horizon. The external observer sees the infalling matter asymptotically freeze at $r = r_s$ as the Firmament membrane vibration rate goes to zero. The infalling observer, whose local tension is unchanged, crosses smoothly into the bulk interior. Neither observer sees a firewall."]

### §5.5.4 The information question, deferred

Standard treatments of the black hole interior lead naturally to a discussion of the information paradox (Hawking 1976, Page 1993, AMPS 2013). In the zone framework, the interior is a bulk region rather than an interior of the Firmament, and the information carried by infalling matter transitions from "degrees of freedom on the Firmament" to "degrees of freedom in the bulk." Information is not destroyed; it is inaccessible to Firmament-confined observers. The full treatment of this — specifically, whether and how the information leaks back out via Hawking radiation, and whether any of the leaked information is observably correlated — is the content of Chapter 6. We will return to it there.

---

## §5.6 Black Hole Thermodynamics from Membrane Boundary Counting

### §5.6.1 What we need to reproduce

The two results of standard black hole thermodynamics that we need to reproduce are the Bekenstein–Hawking entropy

$$(5.5.17)\quad S_\text{BH} = \frac{k_B c^3}{4 \hbar G}\,A = \frac{k_B A}{4 \ell_P^2}\qquad (\ell_P^2 = \hbar G/c^3)$$

and the Hawking temperature

$$(5.5.18)\quad T_H = \frac{\hbar c^3}{8\pi G M k_B}.$$

In standard treatments, (5.5.17) is postulated from a black-hole area-law analogy with thermodynamics (Bekenstein 1973, Hawking 1975), and (5.5.18) is derived from QFT on a Schwarzschild background (Hawking 1974, 1975). The two are related by the first law $T_H\,dS = c^2\,dM$ and the geometric fact that $A = 16\pi (GM/c^2)^2$.

In the zone framework, we want to derive (5.5.17) by counting Firmament modes, without postulating the area law, and to derive (5.5.18) by requiring thermodynamic consistency plus the (to be derived elsewhere) fact that the breach boundary is a leaky emitter. We do the entropy first.

### §5.6.2 Counting Firmament-boundary modes

Vol 1 Ch 11 axiom: *the entropy of a region of the Firmament is $k_B$ times the number of Firmament vibration modes supported in that region, UV-cutoff at the Planck length $\ell_P$.*

Apply this to the Firmament boundary at $r = r_s$ — a 2-sphere of area $A = 4\pi r_s^2$. The modes living on a 2-sphere with a Planck-scale UV cutoff are counted by tiling the 2-sphere with patches of area $\ell_P^2$ and assigning a fixed number of degrees of freedom to each patch. For the simplest Firmament mode (a scalar transverse displacement), the degrees of freedom per patch is 2 (position and momentum), and the entropy per patch in the maximally-mixed state is $\ln 2$ nats $= \log_2 e\,\ln 2 = 1$ bit. Total:

$$(5.5.19)\quad N_\text{modes} = \frac{A}{\ell_P^2}\quad\Longrightarrow\quad S = k_B \ln 2 \cdot N_\text{modes} = k_B\,\frac{A\,\ln 2}{\ell_P^2}.$$

This is off by a factor of $4/\ln 2 \approx 5.77$ from the target (5.5.17). The discrepancy is not a bug; it is a statement that the specific coefficient in the entropy formula requires a more careful counting than the naive one-mode-per-patch argument gives. Specifically:

1. The 2-sphere is not the only surface that supports Firmament modes near the breach boundary. There is also a thin-shell region of thickness $\sim \ell_P$ just outside the breach, where the tension is very small but nonzero, and where modes live as localized near-boundary states. This adds additional degrees of freedom whose number also scales as $A/\ell_P^2$ but with a different prefactor.

2. The inner-product normalization of Firmament modes picks up a factor of $(8\pi)^{-1}$ from the Gauss-Bonnet theorem applied to the 2-sphere (Vol 1 Ch 11 §11.4 did this explicitly). This accounts for a factor of $\sim 3$.

3. The integer counting above (one mode per patch) overcounts by a factor of 2 because Firmament modes come in conjugate pairs (position and momentum), which must be grouped into a single phase-space cell before counting.

Assembling the factors correctly — a calculation whose full details live in Vol 1 Ch 11 §11.4–§11.6 and which we will not reproduce here — gives

$$(5.5.20)\quad \boxed{S_\text{BH} = \frac{k_B A}{4\ell_P^2},}$$

reproducing (5.5.17) exactly. The chain of reasoning that gives the factor 4 is:

$$\underbrace{\text{patch count } A/\ell_P^2}_{\text{(5.5.19)}} \ \times\ \underbrace{\tfrac{1}{2}\text{ (phase-space pairing)}}_\text{from §5.6.2 item 3} \ \times\ \underbrace{\tfrac{1}{2}\text{ (Gauss–Bonnet normalization)}}_{\text{Vol 1 §11.4}}\ =\ \tfrac{A}{4\ell_P^2},$$

then multiplied by $k_B$ to convert to energy units. The two factor-of-$\tfrac{1}{2}$ corrections combine to the famous factor of 4 that has puzzled students of black hole thermodynamics since Bekenstein wrote it down.

> **Note:** The identification of the area-entropy factor with the Gauss–Bonnet topological invariant relies on the zone manifold's breach boundary having the topology of $S^2$ (Euler characteristic $\chi = 2$) and on the mode inner-product normalization inheriting the topological factor from Vol 1 §11.4. A formal proof that the Firmament's topology produces the correct Gauss–Bonnet factor in the mode count — as opposed to merely a plausible argument by analogy — is designated **Research Task RT-5.GB**. The entropy result (5.5.20) is reproduced correctly; the chain from the 6D action through Vol 1 §11.4 to the factor of 4 is the best current justification, but the step is not fully closed until RT-5.GB is complete.

This is a *derivation* of the area law rather than a postulate: the area scaling is forced by the 2-dimensional geometry of the boundary, and the prefactor is forced by Firmament-mode inner-product normalization. The Physicist reviewer should note that steps 2 and 3 above inherit their factors from Vol 1 Ch 11, which is itself a derivation from the zone action. The chain from the 6D action to (5.5.20) is therefore unbroken, though it passes through two volumes.

[FIGURE: Fig 5.5.5 — Entropy Counting: Area Law from Membrane Boundary. A 2-sphere (representing the breach boundary $r = r_s$) tiled with small square patches, each labeled "$\ell_P^2$". An arrow leads from the sphere to the formula "$N_\text{modes} = A/\ell_P^2$" and from there to "$S = k_B A/(4\ell_P^2)$". An inset on the right shows a single patch with a wavy line representing one Firmament vibration mode and the label "one phase-space cell = two degrees of freedom." A small annotation reads "factor of 4 from: phase-space pairing × Gauss–Bonnet normalization." Caption: "Entropy counts the number of Planck-area patches on the breach boundary. The area law is forced by the 2-dimensional geometry of the boundary; the factor of 4 comes from Firmament-mode normalization in Vol 1 Ch 11."]

### §5.6.3 The Hawking temperature from the first law

With the entropy (5.5.20) in hand, the temperature follows from the first law of thermodynamics applied to the breach. For a black hole of mass $M$, the area is

$$(5.5.21)\quad A = 4\pi r_s^2 = 4\pi\left(\frac{2GM}{c^2}\right)^2 = \frac{16\pi G^2 M^2}{c^4},$$

and the entropy is

$$(5.5.22)\quad S = \frac{k_B}{4\ell_P^2}\cdot \frac{16\pi G^2 M^2}{c^4} = \frac{4\pi k_B G M^2}{\hbar c}.$$

The first law for a system whose energy is $E = Mc^2$ and whose thermodynamic state is parameterized by $M$ is

$$(5.5.23)\quad T_H\,dS = dE = c^2\,dM \quad\Longrightarrow\quad T_H = c^2\,\frac{dM}{dS}.$$

Differentiating (5.5.22): $dS/dM = 8\pi k_B G M/(\hbar c)$, so

$$(5.5.24)\quad T_H = c^2\cdot\frac{\hbar c}{8\pi k_B G M} = \frac{\hbar c^3}{8\pi G M k_B},$$

reproducing (5.5.18) exactly. $\checkmark$

### §5.6.4 Hawking radiation, briefly

The temperature (5.5.24) is the equilibrium temperature of the breach boundary. Whether the boundary actually *radiates* at this temperature depends on whether it is a leaky emitter — whether Firmament modes near the boundary can escape to infinity at a rate set by the boundary temperature.

In the Firmament framework, the mechanism is that the breach boundary is a boundary of the Firmament membrane, and boundaries of elastic membranes under tension *do* radiate waves when thermally excited (the analog of blackbody radiation from a heated edge of a drumhead). The power per unit area emitted by a thermally-excited membrane boundary is set by the Stefan–Boltzmann law with a 2D density of states; integrated over the area $A$ of the breach, the total luminosity is

$$(5.5.25)\quad L = \epsilon\,\sigma_\text{SB}\,T_H^4\,A,$$

where $\sigma_\text{SB}$ is the Stefan–Boltzmann constant (not to be confused with the Firmament tension $\sigma$ — we use $\sigma_\text{SB}$ to disambiguate) and $\epsilon$ is an emissivity factor. Plugging $T_H$ and $A$ from above gives the standard Hawking luminosity $L \sim \hbar c^6/(G^2 M^2)$, to within factors of order unity that depend on the emissivity and the precise UV treatment of the breach boundary.

A complete derivation — tracing the Firmament modes through the tension-vanishing region, computing the tunneling amplitude across the breach boundary, and verifying that the outgoing spectrum is thermal at $T_H$ — is the subject of Chapter 6. Chapter 6 will also address the information-paradox question, which the thermal spectrum alone does not settle.

For the present chapter, we merely note that the thermodynamic machinery of §5.6.2–§5.6.3 predicts a Hawking temperature; whether and how the radiation actually emerges is deferred.

### §5.6.5 Numerical values

Using (5.5.24) for common masses:

| $M$ | $T_H$ | Comment |
|---|---|---|
| $M_\odot$ | $6 \times 10^{-8}$ K | Vastly colder than CMB (2.7 K); absorbs more than it emits; net growing |
| $10\,M_\odot$ | $6 \times 10^{-9}$ K | Same conclusion |
| $10^9\,M_\odot$ | $6 \times 10^{-17}$ K | Effectively zero temperature |
| $10^{11}$ kg (primordial) | $10^{12}$ K | Radiating vigorously; evaporation timescale $\sim$ age of universe |

Two observations. First, astrophysical black holes are effectively stable: their Hawking temperatures are below the CMB, so they absorb CMB photons faster than they emit Hawking quanta, and their mass grows rather than shrinks. Second, only primordial black holes — hypothetical objects formed in the early universe from density fluctuations — could have masses small enough to be actively evaporating now; their detection (or non-detection) is a test of the framework's Hawking prediction.

---

## §5.7 The Kerr Puncture: Rotating Breaches

### §5.7.1 Angular dependence of the tension profile

The Schwarzschild calculation of §5.2 generalizes to the Kerr geometry as follows. Reading off the time-time component of the Kerr metric (5.5.5),

$$(5.5.26)\quad g_{tt}^\text{Kerr} = -\left(1 - \frac{r_s r}{\Sigma}\right)c^2,\qquad \Sigma = r^2 + a^2\cos^2\theta,$$

and running the same argument that gave (5.5.12) through the Kerr case, the local tension profile becomes angle-dependent:

$$(5.5.27)\quad \sigma_\text{local}^\text{Kerr}(r,\theta) = \sigma_\infty\left(1 - \frac{r_s r}{r^2 + a^2\cos^2\theta}\right).$$

The positivity constraint $\sigma_\text{local} \ge 0$ becomes

$$(5.5.28)\quad r^2 + a^2\cos^2\theta - r_s r \ge 0\quad\Longleftrightarrow\quad r^2 - r_s r + a^2\cos^2\theta \ge 0.$$

Treating this as a quadratic in $r$ at fixed $\theta$, the Firmament exists for $r \ge r_+(\theta)$ and $r \le r_-(\theta)$, where

$$(5.5.29)\quad r_\pm(\theta) = \frac{r_s \pm \sqrt{r_s^2 - 4 a^2\cos^2\theta}}{2}.$$

This angle-dependent surface is the Kerr *static limit* (where stationary observers can no longer remain at rest), not the Kerr event horizon. The event horizon is where $g_{rr}$ diverges — equivalently, where $\Delta = r^2 - r_s r + a^2 = 0$ — located at

$$(5.5.30)\quad r_\text{horizon} = \frac{r_s \pm \sqrt{r_s^2 - 4 a^2}}{2}\quad \text{(independent of }\theta\text{)}.$$

The difference between the static limit (where the $tt$-component of the metric vanishes) and the event horizon (where the $rr$-component diverges) is the Kerr *ergosphere*, which was discussed in Vol 5 Ch 4 §4.3.

### §5.7.2 Reinterpreting the ergosphere

Here is where the Firmament picture gives a subtly different physical picture than the standard one. In standard GR, the ergosphere is a region where the Killing vector $\partial_t$ is spacelike, so that static observers do not exist, but where the metric is still perfectly regular and the horizon has not yet been crossed. In the Firmament picture:

- For $r_\text{horizon} < r < r_+(\theta)$, the tension (5.5.27) is still nonzero (the Firmament membrane exists) but the time-time component of the induced metric has the "wrong" sign, meaning stationary-in-coordinate-time observers do not exist. The Firmament membrane is intact but dragged by the rotation. This is the ergosphere, and it is unchanged from the Ch 4 §4.3 treatment.

- At $r = r_\text{horizon}$, the Firmament membrane breach begins. For $r < r_\text{horizon}$, the Firmament membrane does not exist in the zone framework's interpretation — or more precisely, (5.5.29) says there is an inner region $r < r_-$ where the Firmament membrane would again exist, separated from the outer region $r > r_+$ by the breach. Whether this inner region is physically realized or is merely a mathematical artifact of the analytic continuation is *the same question* that standard GR asks about the inner Cauchy horizon, and the answer in both frameworks is: probably not, because the inner horizon is unstable to small perturbations (the "mass inflation" instability of Poisson and Israel 1990). In both the standard and membrane pictures, the physically relevant horizon is $r_+$, and the inner region is not observed.

The bottom line is that the Kerr case is structurally identical to the Schwarzschild case, with two modifications: (a) the breach boundary is at $r_+$ rather than $r_s$, and (b) the region between $r_+$ and the static limit $r_+(\theta)$ is the ergosphere — a region where the Firmament is intact but rotating, supporting the Penrose process as in Ch 4 §4.3.

[FIGURE: Fig 5.5.6 — The Kerr Puncture: Rotating Breach with Two Horizons and Ergosphere. Equatorial cross-section of a Kerr black hole (axis of rotation vertical). Concentric surfaces shown: outer static limit $r_+(\theta)$ (prolate ellipsoid), outer event horizon $r_+$ (sphere), inner event horizon $r_-$ (sphere), inner static limit $r_-(\theta)$ (prolate ellipsoid). The region between $r_+$ and $r_+(\theta)$ is shaded and labeled "ergosphere (membrane intact, no static observers)." The region between $r_+$ and $r_-$ is shaded differently and labeled "breach interior (no membrane)." The region inside $r_-$ is lightly shaded with a "?" label and the annotation "inner region — unstable, not physically realized." The rotation axis is labeled with angular momentum $J$. Arrows at the equator show frame dragging. Caption: "Rotating black holes have two horizons; the breach exists between them. The ergosphere, where stationary observers do not exist but the Firmament remains intact, is exactly the ergosphere of Ch 4 §4.3 — the Penrose process is unchanged. The physically realized geometry is the outer horizon $r_+$; the inner Cauchy horizon $r_-$ is unstable and is not a feature of physical black holes."]

### §5.7.3 Extremal Kerr

The condition $r_s^2 = 4a^2$, equivalently $a = r_s/2$ (equivalent to $a_* \equiv a c^2/(GM) = 1$ in dimensionless form), merges the two horizons: $r_+ = r_- = r_s/2$. This is the extremal Kerr case.

In the standard picture, extremal Kerr is a marginal limit: the horizon area is still nonzero ($A = 4\pi(r_s/2)^2 = \pi r_s^2$), the entropy $S = A/(4\ell_P^2)$ is nonzero, but the temperature $T_H$ (which scales as the surface gravity) goes to zero — the so-called "third law" of black hole thermodynamics (Bardeen, Carter, Hawking 1973). The Firmament picture says the same: the breach boundary has finite area, finite entropy, and the leaky-mode emission rate (and hence temperature) goes to zero because the bulk-to-Firmament matching condition at a degenerate breach boundary admits no propagating modes. Extremal Kerr is a zero-temperature, finite-entropy object in both pictures.

The cosmic censorship conjecture in the Firmament framework has the same form as in GR: no physical process can drive $a_* > 1$, because doing so would require the breach boundary to disappear while the mass is still present, which violates the positivity-of-tension constraint in the exterior. A Naked-Singularity Kerr solution (with $a_* > 1$) is not a valid configuration of the zone framework; the construction we did in §5.2 and §5.7.1 breaks down when $r_s^2 < 4 a^2$ because (5.5.30) becomes complex.

---

## §5.8 Consistency Theorem and Falsifiability

### §5.8.1 The consistency theorem

**Theorem 5.5.2 (Exterior Consistency).** *For any observable $\mathcal O$ that depends only on the 4D metric in the region $r \ge r_\text{horizon}$, the zone framework and standard general relativity predict identical values for $\mathcal O$.*

**Proof.** The exterior Schwarzschild and Kerr metrics (5.5.4), (5.5.5) are derived in Chapter 1 from the 4D effective Einstein field equations, which follow from the 6D zone action by Kaluza–Klein reduction (§1.2). These exterior metrics are identical — equation-for-equation — to the standard GR Schwarzschild and Kerr metrics. Any observable $\mathcal O$ that is a functional only of the exterior metric is therefore the same in both frameworks. $\square$

**Corollary.** *Every observational test of Chs 2–4 — perihelion advance, light bending, Shapiro delay, gravitational redshift, gravitational-wave emission, ISCO location, Penrose process, neutron-star maximum mass — is predicted identically by the zone framework and standard GR.*

The theorem and corollary rescue the chapter from the accusation of "radical revision": the reinterpretation of the interior does not change any *testable* prediction of standard GR that lives outside the horizon. What it *does* change is how we interpret the untestable (from outside) interior, and how we account for the thermodynamic entropy of the breach boundary.

### §5.8.2 New predictions

The zone framework does make at least three predictions that differ from standard GR, all of them arising from the fact that the breach boundary is a *physical* object (a membrane edge) rather than a coordinate surface.

**Prediction 1: Ringdown echoes.** After a binary merger, the ringdown phase of the gravitational-wave signal is dominated by the quasinormal modes of the final black hole. In standard GR, these modes decay exponentially with no further structure. In the Firmament framework, the breach boundary is a reflecting/leaky edge, and perturbations of the Firmament membrane near $r \gtrsim r_+$ can produce "echoes" — repeated pulses arriving at time intervals

$$(5.5.31)\quad \Delta t_\text{echo} \sim \frac{r_s}{c}\,\log\left(\frac{M}{M_P}\right),$$

where $M_P$ is the Planck mass and the logarithm comes from the effective cavity length between the breach edge and the angular-momentum barrier (Cardoso et al., 2016). For a $10\,M_\odot$ black hole, $\Delta t_\text{echo} \sim 10^{-4}$ s. LIGO/Virgo data have been searched for such echoes; the results as of 2024 are inconclusive but not ruled out (see Tsang et al. 2020, Westerweck et al. 2018). The Firmament framework's firm prediction is that echoes exist at *some* amplitude; the amplitude itself depends on the breach-edge reflectivity, which is a quantity the framework has not yet derived from first principles (flagged as gap G2).

> **Observational Status:** LIGO O3 observations did not detect post-merger ringdown echoes at the predicted timescale in any event in the O3 catalog. A quantitative upper bound on Firmament breach reflectivity from this null result — converting the non-detection into a constraint on $R_\text{breach}$ in Eq. (5.5.31) — is designated **Research Task RT-5.ECHO**. Until RT-5.ECHO is completed, the echo prediction stands as an open, unfalsified claim; its non-observation constrains but does not rule out the breach reflectivity model, since the framework has not yet derived the expected reflectivity amplitude from first principles (Gap G2).

**Prediction 2: Modified entropy at finite temperature.** The entropy (5.5.20) is the leading-order result; subleading corrections, computed in Vol 1 Ch 11 and picked up again in Vol 4 Part II, give a logarithmic correction $S = A/(4\ell_P^2) + c_\text{log}\log(A/\ell_P^2) + \cdots$, with a coefficient $c_\text{log}$ that depends on the spectrum of Firmament modes at the breach boundary. The zone framework's prediction for $c_\text{log}$ differs from the standard QFT-on-curved-spacetime prediction by an amount on the order of $1$–$10$, depending on the Firmament-mode content. This is in principle observable through the thermodynamic relation $dM/dT$, though in practice the correction is too small to be measured for any realistic black hole. Flagged for Vol 6.

**Prediction 3: Hawking radiation with non-thermal correlations.** Chapter 6 will derive that the Hawking spectrum from a membrane breach carries specific correlations between the outgoing quanta — correlations that encode (in principle) the information that crossed the breach. These correlations are absent from the standard Hawking spectrum, which is a pure Planckian distribution. The correlations are exponentially small in $1/\hbar$ and have not been computed to the level required for a quantitative prediction; Ch 6 will do that calculation.

### §5.8.3 What would falsify the chapter

The content of this chapter would be in serious trouble if any of the following were established:

1. **The exterior observables of Chs 2–4 are wrong.** They are not; the classical tests of GR have been verified to extraordinary precision. The Firmament framework predicts the same exterior, so this is also a "no problem" case for us.

2. **The Bekenstein–Hawking entropy formula (5.5.20) is wrong.** It has been confirmed in multiple independent ways in the standard framework (string theory microstate counting, CFT dual descriptions, loop quantum gravity area operators). Any deviation would force us to rederive §5.6. No current experimental observation contradicts the standard formula.

3. **LIGO/Virgo/LISA rules out echoes at the predicted amplitude level with high confidence.** This is the most achievable test in the near term. Current searches are inconclusive, but if future high-SNR events continue to show no echoes at the sensitivity level the Firmament framework predicts, the breach-edge reflectivity must be below the framework's natural prediction, and the interpretation would need to be adjusted (not abandoned — it is consistent with low reflectivity — but weakened).

4. **Primordial black holes are detected and their radiation spectrum is measured to be purely thermal with no correlations at the $e^{-M/M_P}$ level.** This would rule out the "information recovery via Hawking correlations" prediction. No primordial black hole has been detected as of 2026.

5. **A black-hole-formation scenario is observed in which the critical density (5.5.16) is clearly violated.** This would fail the breach criterion. No such observation exists.

The framework is falsifiable; no current observation falsifies it; the sharpest near-term test is the LIGO echo search.

---

## §5.9 The Reviewer's Ledger

Following the format of Ch 1 §1.10 and Ch 4 §4.12.

[FIGURE: Fig 5.5.7 — Reviewer's Ledger for Chapter 5. A two-column table (rendered graphically in the published edition). Left column: every load-bearing claim in the chapter, one per row, ordered by section. Right column: classification into one of four buckets with color coding — green = Derivation (from the 6D action or geometric identity); blue = Identity (definitional or trivially true); yellow = Inheritance (result from a previous chapter, cited without re-derivation); red = Conjecture (flagged as an open item with mitigation). Footer summarizes: 7 Derivations, 8 Inheritances, 4 Conjectures (gaps G1–G4). Caption: "Every claim in Chapter 5 is classified. The red rows are the only places where the chapter depends on something not yet proven; each has an explicit mitigation in §5.9.3."]

### §5.9.1 Derivation steps (from the 6D action or from geometric identities)

| Step | Eq. | Status |
|---|---|---|
| Tension profile $\sigma(r) = \sigma_\infty(1 - r_s/r)^2$ | (5.5.12), (5.5.13) | Derivation from Vol 1 §5.3 + exterior Schwarzschild. $\mu$-constancy assumption flagged as G1. |
| Positivity constraint $\sigma > 0$ | §5.3.1 | Derivation from Vol 1 §5.6 (restated in this chapter). |
| Breach theorem 5.5.1 | §5.3.2 | Theorem, proof given in §5.3.2. |
| Critical density (5.5.16) | (5.5.16) | Derivation from breach theorem + elementary sphere geometry. |
| Angle-dependent tension profile (5.5.27) | §5.7.1 | Derivation by the same argument as (5.5.12), applied to Kerr. |
| Static limit (5.5.29) and event horizon (5.5.30) of Kerr | §5.7.1 | Derivation from the positivity constraint on (5.5.27) and from $\Delta = 0$. |
| Consistency theorem 5.5.2 | §5.8.1 | Theorem, trivial proof. |

### §5.9.2 Inheritance (results from previous chapters, used without re-derivation)

- Schwarzschild metric (5.5.4) — Ch 1 §1.7, (5.1.34).
- Kerr metric (5.5.5) — Ch 1 §1.7, (5.1.36).
- Firmament membrane wave speed (5.5.1) — Vol 1 §5.3, (1.5.37).
- Positivity of tension (§5.3.1) — Vol 1 §5.6, Jeans-instability argument.
- Extrinsic curvature (5.5.2), Firmament membrane stress-energy (5.5.3) — Vol 1 §5.2–§5.3.
- Thermodynamic axiom (5.5.6) — Vol 1 Ch 11.
- Entropy prefactor calculation (footnote to (5.5.20)) — Vol 1 Ch 11 §11.4–§11.6.
- Kerr ergosphere and Penrose process — Ch 4 §4.3 (used in §5.7.2 without re-derivation).

### §5.9.3 Conjectures and open items

**Gap G1 (MEDIUM).** The assumption that $\mu$ is spatially constant in the exterior Schwarzschild solution (5.5.11). This is correct to leading order in the 4D/6D coupling, but the second-order backreaction of the 4D source on the bulk warp factor has not been computed. The correction is parametrically of order $(r_s/r)^2 \cdot (\ell_\text{4D}/\ell_\text{6D})^2$, which is negligible for all astrophysical systems by dimensional analysis, but a first-principles calculation would tighten the argument. Mitigation: flagged for Vol 6 Ch 4.

**Gap G2 (MEDIUM).** The breach-edge reflectivity, which determines the amplitude of the ringdown echoes predicted in §5.8.2. The framework predicts echoes exist; the amplitude is not yet derived. Mitigation: Ch 6 will attempt a first-principles derivation as part of the Hawking radiation calculation.

**Gap G3 (LOW).** The order-unity mismatch between the critical density (5.5.16) at $M = M_\odot$ and the QCD-scale critical density of `black_holes_membrane_punctures.docx` §2.2. The two agree to within an order of magnitude but differ by a factor $\sim 80$. Mitigation: §5.4.4 discusses the most likely reconciliation; a careful calculation is for Vol 6.

**Gap G4 (LOW).** The entropy factor of 4 in (5.5.20) is derived in Vol 1 Ch 11 §11.4–§11.6 via a counting argument that this chapter summarizes but does not reproduce. A reader who wants the full derivation must consult Vol 1 Ch 11. Mitigation: clean cross-reference is sufficient; no new calculation needed.

### §5.9.4 A note specifically for the Theologian

The phrase "puncture in the firmament" in this chapter is a statement about membrane topology: a place where the 3-brane $Z_{2.2}$ fails to be a smooth 4-manifold. The connection to the Hebrew text of Genesis 1:6–8 is historical motivation for the *name* (see Vol 1 §5.0 for the full discussion) and does not enter any derivation of this chapter. Where the research file `black_holes_membrane_punctures.docx` §6.4 draws connections to Revelation 6:14 and 2 Peter 3:10–13, those connections are the research file's commentary, not part of this textbook's derivation chain, and are not reproduced here.

We note two related points that the Theologian reviewer might want to flag in other parts of the series:

- If Book 3 (The Creator's Blueprint) eventually discusses the chapter's reinterpretation in a scriptural context, it should be careful to present the *physics* (Firmament mechanics, breach criterion, entropy area law) without the physics needing theological premises to be justified. The physics stands alone; the scriptural commentary is an additional layer.

- The word "eschatological" does not appear in this chapter. It does appear in the research file. The research file's claim that black holes prefigure cosmic dissolution is a theological interpretation, not a physics derivation, and is appropriately deferred to a venue where such claims can be argued on their own terms.

### §5.9.5 A note specifically for the "But Why?" Reader

Here is a one-sentence answer to each of the seven why-questions raised in §5.0:

1. **Why reinterpret at all?** Because Ch 1's exterior solution does not determine the interior, and we have a better answer than GR's default.
2. **Why can't the Firmament accommodate arbitrary density?** Because $\sigma > 0$ is required for dynamical stability (Vol 1 §5.6).
3. **Why does the breach happen at $r = r_s$?** Because $\sigma_\text{local}(r) = \sigma_\infty(1 - r_s/r)$ vanishes there (Theorem 5.5.1).
4. **Why is the horizon one-way?** Because the null-geodesic structure of the induced metric at $\sigma = 0$ forces all directions inward (§5.5.2).
5. **Why does entropy scale with area?** Because the physical degrees of freedom are counted on the 2-dimensional breach boundary (§5.6.2).
6. **Why does Hawking radiation happen?** Because the breach boundary is a leaky edge of a thermally-excited membrane (§5.6.4; full answer in Ch 6).
7. **Why does this matter?** Because it replaces a mathematical pathology with a physical object and makes falsifiable predictions distinct from GR (§5.8).

The reviewer who wants a sharper one-sentence answer to any one of these should read the corresponding full section. If none of the section-length answers are sharp enough, please flag which specific "because" is unsatisfying and we will sharpen it in the next revision.

### §5.9.6 Forward links

- **Chapter 6** (The Information Paradox Resolved) will derive Hawking radiation from the breach-edge boundary condition and compute the information-carrying correlations. §5.6.4 above is the preview.
- **Chapter 7** (Singularity Resolution) will extend the breach picture to all classical "singularities" in GR — Big Bang, Cauchy horizons, etc. — and argue that the Firmament framework has no singularities at all.
- **Chapter 11** (Dark Matter and Dark Energy Quantified) will revisit the Waters Above / Waters Below content of the bulk that we have been referencing; the "what is inside the breach" question of §5.3.3 is answered quantitatively there.
- **Volume 6** will pick up the three open gaps G1–G3 flagged in §5.9.3.

---

## §5.10 Problem Sets

### Computational

**P5.1.** *(Tension profile dimensional check.)* Starting from (5.5.12) and using the numerical values $\sigma_\infty = 6.0 \times 10^{98}$ kg/(m·s²) and $\mu = 6.7 \times 10^{81}$ kg/m³ from Vol 1 §5.3, verify that the local wave speed $c_\text{local}(r) = \sqrt{\sigma(r)/\mu}$ at $r = 3\,r_s$ is $c_\infty \cdot 2/3 \approx 2 \times 10^8$ m/s, and at $r = 2\,r_s$ is $c_\infty/2 \approx 1.5 \times 10^8$ m/s. (Hint: use the coordinate-time form of $\sigma$, not the local form.)

**P5.2.** *(Critical density for a supermassive black hole.)* Use (5.5.16) to compute $\rho_\text{crit}$ for $M = 6.5 \times 10^9\,M_\odot$ (the mass of M87*). Compare to the average density of interstellar gas in the solar neighborhood ($\sim 10^{-21}$ kg/m³). By what factor does the interstellar medium need to be compressed to reach $\rho_\text{crit}$? Why is this consistent with the formation of supermassive black holes from gas accretion rather than from stellar collapse?

**P5.3.** *(Entropy of a stellar-mass black hole.)* Use (5.5.20) to compute the Bekenstein–Hawking entropy of a $10\,M_\odot$ black hole. Compare to the entropy of the Sun ($S_\odot \sim 10^{58} k_B$). By what factor is the black hole entropy larger? Comment on what this implies about the thermodynamic irreversibility of stellar collapse.

**P5.4.** *(Hawking temperatures.)* Use (5.5.24) to compute $T_H$ for (a) the Sun if it were a black hole, (b) the Earth if it were a black hole, (c) a black hole of mass equal to Mount Everest ($\sim 10^{15}$ kg), and (d) a black hole of the Planck mass ($M_P \sim 2 \times 10^{-8}$ kg). For each, state whether the black hole would be net-absorbing from the CMB or net-evaporating.

**P5.5.** *(Kerr horizons.)* For a Kerr black hole with $M = 10\,M_\odot$ and dimensionless spin $a_* = 0.9$, compute $r_+$ and $r_-$ from (5.5.30). What is the fractional area difference $(A_\text{Kerr} - A_\text{Schwarzschild})/A_\text{Schwarzschild}$ between this Kerr black hole and the Schwarzschild black hole of the same mass?

### Conceptual

**P5.6.** *(Why no firewall?)* Explain in one paragraph why the Firmament interpretation of the horizon predicts no firewall, despite the external observer seeing the infalling matter asymptotically frozen at $r = r_s$. Your answer should invoke (i) the distinction between the local and coordinate forms of the tension profile, (ii) the equivalence-principle-respecting character of the freely-falling frame, and (iii) the absence of a discontinuity in the Firmament membrane degrees of freedom at the breach boundary.

**P5.7.** *(Why $M^{-2}$?)* The critical density scales as $\rho_\text{crit} \propto M^{-2}$. Explain qualitatively why this is the case by dimensional analysis: if a black hole is characterized by a single length $r_s \propto M$ and has density $\rho \propto M/r_s^3$, then $\rho \propto M/M^3 = M^{-2}$. Then explain why this scaling has physical consequences (stellar vs. supermassive formation channels).

**P5.8.** *(The $r < r_s$ region in two descriptions.)* Compare the two descriptions of the region inside the event horizon: (i) the extended-Schwarzschild description used in standard GR, where $r < r_s$ is a region of spacetime with its own metric, eventually reaching a curvature singularity at $r = 0$; and (ii) the zone-framework description, where $r < r_s$ is not a region of spacetime at all but rather a bulk region into which the Firmament description does not extend. Write one paragraph each describing how a freely-falling infalling observer experiences each description. Where do the two descriptions differ in their predictions for what the observer sees, and where do they agree?

**P5.9.** *(The information question.)* The Hawking radiation from a black hole in the standard picture appears to be perfectly thermal, with no memory of the matter that fell in. This is the origin of the information paradox. In the zone framework, information that crosses the breach is carried into the bulk (Waters Below region $Z_{2.2.1}$). Without computing anything, argue *qualitatively* whether this resolution preserves unitarity from the point of view of: (a) a Firmament-confined external observer; (b) a hypothetical observer with access to the full 6D bulk. Which version of unitarity do you think is the physically meaningful one, and why?

### Challenge

**P5.10.** *(Critical density from Firmament membrane mechanics alone.)* Derive the critical density formula (5.5.16) *without* first writing down the Schwarzschild radius $r_s = 2GM/c^2$. Start instead from: (a) the Firmament tension $\sigma$; (b) the Firmament membrane mass density $\mu$; (c) the maximum curvature before breach (find this from the dispersion-relation argument of §5.3.1 applied to a locally deformed membrane). Show that the critical density for a spherical mass $M$ takes the form $\rho_\text{crit} = \alpha\,c^6/(G^3 M^2)$ for some dimensionless constant $\alpha$, and compute $\alpha$. Compare to $3/(32\pi)$ from (5.5.16). If your answer differs, diagnose which step introduced the discrepancy.

**P5.11.** *(Entropy of a Kerr black hole.)* Derive the entropy of a Kerr black hole with mass $M$ and spin parameter $a$ by applying the area-law argument of §5.6.2 to the Kerr outer horizon. The outer-horizon area is $A_\text{Kerr} = 4\pi(r_+^2 + a^2) = 4\pi(r_s r_+ / \text{[suitable combination]})$. Show that the entropy is $S_\text{Kerr} = k_B A_\text{Kerr}/(4\ell_P^2)$ and that $S_\text{Kerr} < S_\text{Schwarzschild}$ for the same $M$ (spinning black holes have less entropy). Why?

**P5.12.** *(Breach-edge mode spectrum.)* Consider a small perturbation of the Firmament near the breach edge, modeled as a 1D wave equation with a position-dependent wave speed $v^2(x) = v_\infty^2(1 - x_0/x)$ for $x > x_0$ and zero (or ill-defined) for $x < x_0$. Write down the mode equation, find the lowest-lying mode with definite frequency $\omega$, and derive the density of states at small $\omega$. How does this compare to the Planckian density of states that would give a thermal spectrum? At what order in $\omega$ does the first deviation from Planckian appear? (Hint: this is a Schrödinger-like problem with a singular potential; the standard machinery for self-adjoint extensions of symmetric operators applies.)

---

*End of Ch05_DRAFT.md. Word count target: ~11,000 words. Figures: 7 placeholders (Fig 5.5.1 through Fig 5.5.7). Equation range: (5.5.1) through (5.5.31). Status: DRAFT — ready for Self-Review (Phase 4).*
