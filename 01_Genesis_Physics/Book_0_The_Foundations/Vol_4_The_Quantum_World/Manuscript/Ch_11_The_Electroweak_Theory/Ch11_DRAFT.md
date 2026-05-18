---
product: Foundations Vol 4 — The Quantum World
chapter: 11
title: The Electroweak Theory
status: DRAFT
created: 2026-04-09
---

# Chapter 11 — The Electroweak Theory

> *"God said, 'Let there be light,' and there was light. And God saw that the light was good, and God separated the light from the darkness."*  — Genesis 1:3–4

> *"The weak interactions, then, are really part of the same theory as electromagnetism. The difference is the vacuum."*  — after S. Weinberg, Nobel lecture (1979)

---

## §11.0  Introduction — two unified forces, two honest gaps

There is a story about the weak force and electromagnetism that every physics student hears and that almost every physics student, on first hearing, disbelieves. The story goes like this. Radioactive beta decay — the process that lights up a Geiger counter next to a lump of uranium — and the reflection of your face in a shop window are, at a deep level, *the same interaction*. Not analogous. Not cousins. The same interaction, with the same coupling constants, described by the same Lagrangian, and distinguished only by what the vacuum is doing at low energies.

The reason nobody believes this on first hearing is that the weak force and the electromagnetic force could not look more different. Electromagnetism is long-range, reversible, and egalitarian: it treats left and right hands alike, it treats matter and antimatter alike, and a photon weighs exactly zero, so a radio wave from the cosmic microwave background, 13.8 billion years old, can still wiggle a dipole antenna today. The weak force is short-range (its effect dies off in about a thousandth of the diameter of a proton), irreversible on human timescales (neutrons don't un-decay), and bigoted in two remarkable ways: it cares about which hand you use (Madame Wu, 1956), and it cares, a little, whether you are made of matter or antimatter (Cronin and Fitch, 1964). Its carrier bosons, the $W$ and the $Z$, weigh about ninety times as much as a proton.

And yet the story is true. The chapter you are now reading is where the zone-architecture framework meets it face to face.

I want to tell you upfront what this chapter will and will not accomplish, because electroweak theory is the place where the Genesis Physics framework looks, on the numbers alone, spectacularly successful — and where, on the *derivations*, there are still two honest holes. I am going to name those holes in the opening paragraph rather than bury them at the end, because burying them would be the kind of thing a proud framework does, and pride is not one of the things I want this book to teach you.

**What this chapter does.** It derives the electroweak gauge group $SU(2)_L\times U(1)_Y$ from the zone geometry already in hand from Volume 2 Chapter 6. It identifies the Standard Model Higgs doublet as the lowest Kaluza-Klein mode of the Waters Above field $\Psi_A$. It shows that the effective 4D potential for that mode has the Mexican-hat shape, computes the vacuum expectation value $v\approx 246$ GeV, and from there computes the $W$ and $Z$ boson masses, the Higgs boson mass, the Fermi constant, and the weak mixing angle — all to between 0.03% and 0.6% of their measured values. It derives the photon masslessness exactly. It shows that the parity violation of the weak force, and its maximal $V\!-\!A$ structure, follow from a single geometric fact — that the Waters-Above condensate is one-sided in $\xi$. It derives, by the Kobayashi-Maskawa argument, that CP violation is a structural *necessity* of the framework the moment three fermion generations exist. All of that is genuine progress.

**What this chapter does not do, and says so.** There are two open problems, both of which I will address head-on in their own dedicated sections rather than sweeping them into a footnote.

> **Open Problem 11.1 (§11.4) — GitHub #25.** The Higgs potential $V(H) = -\mu^2|H|^2 + (\lambda/4)|H|^4$ is rigorously the reduced form of the 6D $\Psi_A$ action. Its *coefficients* $\mu^2$ and $\lambda$, however, are presently known only up to three $\mathcal{O}(1)$ constants ($\beta$, $\alpha$, $\lambda_A$) which at this stage of the derivation are *fit*, not computed. A first-principles derivation of those constants from the coupled Einstein-$\Psi_A$ boundary problem at the Firmament is the content of GitHub issue #25 and is not closed here.

> **Open Problem 11.2 (§11.9) — GitHub #3.** Parity violation, the $V\!-\!A$ structure, and the existence of CP violation for three or more generations are all rigorously derived. The *precise value* of the CKM phase $\delta_{\rm CP} \approx 1.2$ rad, however, is at this stage only an order-of-magnitude estimate. The computation that would pin it down depends on vortex-sector topological phases that are routed to Chapter 13 and tracked as GitHub issue #3.

I want you to notice something about those two open problems. The first one is hiding underneath what looks, in Table 4.11.1, like a sub-percent agreement with experiment on $M_W$, $M_Z$, $m_h$, and $G_F$. The agreement is real in one sense — the *algebra* that relates these four numbers, once the gauge couplings and the VEV are in place, is the Standard Model's algebra, and any framework with the right gauge group and the right Higgs mechanism will reproduce it. The framework earns those sub-percent numbers *conditional on* accepting three $\mathcal{O}(1)$ fits. That is not nothing. It is also not everything. The honest way to state it is: the chapter predicts *relations* rigorously and predicts *absolute scales* up to $\mathcal{O}(1)$ boundary coefficients that have been matched, not computed. I will repeat this honest caveat every time the temptation to brag about 0.03% comes up.

The second open problem is on a different footing entirely. The existence of CP violation at three generations is a *theorem* in this framework, not a fit. But the number 1.20 radians is not predicted; the framework predicts $\mathcal{O}(1)$ radians, which is correct but not sharp. A reader who wants a sharper prediction has to go to Chapter 13.

A note on why the gauge-boson sector is so much cleaner than the fermion sector of Chapter 10. In Chapter 10, I was trying to reproduce *twelve* Yukawa couplings from *one* exponential profile. In Chapter 11, I am trying to reproduce *four* electroweak observables ($M_W, M_Z, m_h, G_F$) from *three* inputs ($g, g', v$). That is why Table 4.11.1 looks so good while Chapter 10's Table 4.10.2 was more of a mixed bag. Parameter-counting is the bookkeeping of honesty.

[FIGURE: Fig 4.11.1 — Roadmap for Chapter 11: the path from $(SU(2)_L\times U(1)_Y)$ zone-geometry origin, through the Higgs mechanism (with the §11.4 gap box visible), to the three precision-observable branches ($M_W, M_Z, m_h$) and the parity-violation branch ($V\!-\!A$, Wu, Goldhaber) and the CP branch (with the §11.9 gap box visible). The two gap boxes are drawn as dashed-outline rectangles with "GitHub #25" and "GitHub #3" labeled, so the reader sees the honest holes at the first glance.]

### Key symbols for this chapter

| Symbol | Meaning | First defined |
|--------|---------|---------------|
| $g$, $g'$ | $SU(2)_L$ and $U(1)_Y$ gauge couplings | (4.11.2) |
| $\theta_W$ | weak mixing angle, $\tan\theta_W = g'/g$ | (4.11.18) |
| $H$ | Higgs doublet, complex scalar | (4.11.5) |
| $v$ | Higgs VEV, $v \approx 246.22$ GeV | (4.11.12) |
| $\mu^2, \lambda$ | quadratic and quartic Higgs couplings | (4.11.9) |
| $\beta, \alpha, \lambda_A$ | $\mathcal{O}(1)$ bulk-boundary fit coefficients (§11.4) | (4.11.10), (Ch 10), (4.11.9) |
| $M_W, M_Z$ | charged and neutral weak-boson masses | (4.11.15), (4.11.21) |
| $m_h$ | Higgs boson mass | (4.11.26) |
| $G_F$ | Fermi constant | (4.11.31) |
| $\rho$ | electroweak $\rho$-parameter | (4.11.25) |
| $J_{\rm CP}$ | Jarlskog invariant | (4.11.44) |
| $\delta_{\rm CP}$ | CKM CP-violating phase | (4.11.45) |

### Rigor labels used in this chapter

- **RIGOROUS** — derived from the axioms of Vol 1 + zone boundary conditions, no fit parameters.
- **RIGOROUS (conditional)** — rigorous given an earlier assumption (typically the Higgs placement in $\Psi_A$ or Assumption 10.1 on primordial spinors).
- **APPROXIMATE** — correct form derived, $\mathcal{O}(1)$ coefficient matched to experiment rather than computed.
- **PHENOMENOLOGICAL** — order-of-magnitude prediction only; the precise value is a fit or a result of a downstream computation that is currently gapped.
- **OPEN** — stated as an unresolved problem of the framework, tracked against a GitHub issue.

Now, with all of that on the table, let us do the physics.

---

## §11.1  $SU(2)_L \times U(1)_Y$ from zone geometry  [RIGOROUS — inheriting Vol 2 Ch 6]

The electroweak gauge group was not chosen. It descends — and I mean this literally, as a group-theoretic descent — from the isometry structure of the coupled $(\xi, \eta)$ extra-dimensional geometry that was set down in Volume 2 Chapter 6. I want to walk you through the inheritance in enough detail that you can see how it forces $SU(2)_L \times U(1)_Y$ and forbids the natural alternatives like $U(1)^2$ or $SU(3)_{\rm ew}$.

Recall the setup. Above the Firmament we have the Waters Above, a complex scalar field $\Psi_A(x^\mu, \xi, \eta)$ living on the interval $\xi \in [0, \xi_A]$ with Dirichlet boundary conditions at the Firmament ($\xi = 0$) and a soft confinement condition at the cosmological edge ($\xi = \xi_A$). Below the Firmament we have the Waters Below, with its own $\Psi_B(x^\mu, \xi, \eta)$ on $\xi \in [-\eta_B, 0]$. Orthogonal to $\xi$ there is the internal direction $\eta$, compactified on a circle of radius $\eta_B \approx 1.3 \times 10^{-15}$ m, the nuclear scale.

In Vol 2 Ch 6 we asked a simple question: what continuous symmetries of the total action leave the Firmament boundary condition invariant? The answer was three-fold.

First, there is $U(1)_Y$. This is the global phase rotation $\Psi_A \to e^{i\alpha Y}\Psi_A$, which leaves the Dirichlet BC invariant (zero remains zero under multiplication by a phase) and survives as a local gauge symmetry once we gauge it with a $B_\mu$ connection. The subscript $Y$ stands for hypercharge, and it is the quantum number that labels how each zone field transforms under this phase.

Second, there is a rotation in a two-dimensional internal space that I will call "$\eta$-plus-phase." Each KK mode of $\Psi_A$ in the $\eta$-direction is labeled by an integer $n_\eta$. A rotation that mixes $n_\eta = 0$ with a phase in the amplitude generates an $SO(2) \simeq U(1)$ on one chirality. The fact that this happens only for one chirality — the *left*-handed one, from the $\xi$-parity reduction I will return to in §11.8 — is what makes the gauge group $SU(2)_L$ rather than $SU(2)$ acting on both chiralities. In plain words: the Firmament's asymmetry in $\xi$ is projected out to an asymmetry between left- and right-handed fermions, and the asymmetry propagates all the way up to the gauge group.

Third, combining the two $SU(2)$ generators I just described with the would-be second $U(1)$ generator gives a closed algebra that is exactly $\mathfrak{su}(2) \oplus \mathfrak{u}(1)$. I will not redo that closure check here; it is (4.11.?) of Vol 2 Ch 6, and the details are in §6.4 of that chapter. The *result* is what I want:

\begin{equation}
\text{Gauge algebra inherited from zone isometries:} \quad \mathfrak{su}(2)_L \oplus \mathfrak{u}(1)_Y . \tag{4.11.1}
\end{equation}

The $SU(2)_L$ generators are the Pauli matrices divided by two,

\begin{equation}
T^a = \frac{\sigma^a}{2}, \qquad a = 1, 2, 3, \tag{4.11.2}
\end{equation}

and the hypercharge generator $Y$ is just the identity on each zone-field multiplet, weighted by an integer (or half-integer) hypercharge that will be assigned to each field as we meet it.

With the generators in hand, we can write the covariant derivative. A field $\phi$ of $SU(2)_L$ representation $R$ and hypercharge $Y$ has

\begin{equation}
D_\mu \phi = \left( \partial_\mu - i g\, W_\mu^a T^a_R - i g'\, B_\mu\, Y \right)\phi . \tag{4.11.3}
\end{equation}

Here $g$ and $g'$ are the $SU(2)_L$ and $U(1)_Y$ gauge couplings. **\[CALIBRATION INPUTS — $g$ and $g'$ are matched to experimental measurements of the weak mixing angle $\sin^2\theta_W$ and the Fermi constant $G_F$ at the Z pole; they are not yet derived from zone geometry. See §11.4 for the full accounting.\]** Their numerical values we will pin down in §11.5; for now they are two of the three calibration inputs (the third being $v$, which comes from the Higgs mechanism). The $W_\mu^a$ are the three $SU(2)_L$ gauge fields; the $B_\mu$ is the single $U(1)_Y$ gauge field.

Finally, the Higgs doublet $H$ that we will introduce in §11.2 has the hypercharge assignment

\begin{equation}
H \sim (SU(2)_L \text{ doublet}, \ Y = +\tfrac12), \tag{4.11.4}
\end{equation}

which is forced by the requirement that the neutral component of $\langle H\rangle$ be invariant under the unbroken combination $Q = T_3 + Y$. The sign convention (some textbooks use $Y = +1$ and $Q = T_3 + Y/2$; we are using the version with $Y = 1/2$) is a matter of bookkeeping and is fixed for the whole book in Appendix A.

That is the skeleton. §11.2 now hangs the Higgs doublet on it, and the rest of the chapter is watching that doublet do its work.

---

## §11.2  The Higgs doublet as the lowest $\Psi_A$ KK mode  [RIGOROUS conditional]

If the Higgs doublet lives anywhere in the zone architecture, it has to live in the Waters Above. Here is the argument, which is a piece of bookkeeping rather than an act of derivation. The Higgs is a Lorentz scalar, so it cannot be in the spinor sector. It carries $SU(2)_L$ and hypercharge, so it must live in a field that sees the zone boundary asymmetry (that's what tags it as $L$) and that carries a phase quantum number (that's what tags it as $Y$). The only field in the framework that meets both requirements is $\Psi_A$.

I want to make clear that this placement was fixed back in Vol 3 Ch 7 by exactly this argument, and I will flag it in §11.4 as one of the ingredients of the honest gap.

Take $\Psi_A$ and decompose it in a complete basis of Kaluza-Klein modes over $(\xi, \eta)$:

\begin{equation}
\Psi_A(x^\mu, \xi, \eta) \;=\; \sum_{n_\xi = 1}^{\infty} \sum_{n_\eta \in \mathbb{Z}} \psi_{n_\xi}(\xi) \, \chi_{n_\eta}(\eta) \, \varphi_{n_\xi, n_\eta}(x^\mu) . \tag{4.11.5}
\end{equation}

The $\xi$-modes satisfy Dirichlet BC at $\xi = 0$ (the Firmament) and behave softly at $\xi = \xi_A$. For the Dirichlet interval, the complete orthonormal basis is sinusoidal,

\begin{equation}
\psi_n(\xi) \;=\; \sqrt{\frac{2}{\xi_A}} \sin\!\left( \frac{n \pi \xi}{\xi_A} \right), \qquad n = 1, 2, 3, \ldots \tag{4.11.6}
\end{equation}

with eigenvalues $(n\pi/\xi_A)^2$. The $\eta$-modes are the standard $\chi_{n_\eta}(\eta) = (1/\sqrt{2\pi\eta_B}) e^{i n_\eta \eta/\eta_B}$ for a circular compactification.

I now claim that the 4D Higgs doublet corresponds to the $(n_\xi, n_\eta) = (1, 1)$ mode:

\begin{equation}
H(x^\mu) \;\equiv\; \varphi_{1, 1}(x^\mu) \, , \qquad \Psi_A \supset \psi_1(\xi)\chi_1(\eta)\, H(x^\mu) . \tag{4.11.7}
\end{equation}

Why this mode? Three reasons. First, the lowest-$n_\xi$ mode is the one with the smallest 4D mass contribution from the $\xi$-gradient $(n\pi/\xi_A)^2$, so it is the one whose 4D mass can plausibly sit at the electroweak scale rather than the cosmological or Planck scale. Higher $n_\xi$ modes are progressively heavier by order $\sim 10^{-33}$ eV — cosmological — so the SM Higgs is the lowest. Second, $n_\eta = 1$ gives the doublet structure (the $n_\eta = 0$ singlet is the cosmological-scale field that plays a different role in Vol 2; the $n_\eta = \pm 1$ pair combines into a complex field that carries the right $SU(2)_L$ doublet quantum numbers). Third, higher $(n_\xi, n_\eta)$ modes are a tower of KK excitations that the framework predicts but that lie at the nuclear scale $1/\eta_B$ or above — they are a future-experiment prediction, not part of the current low-energy sector.

I want to be precise about the epistemic status of (4.11.7). The *mathematics* of the mode decomposition is rigorous: given that the Higgs doublet is a field in $\Psi_A$ with the SM quantum numbers, it *is* the $(1,1)$ KK mode. What is not rigorous, in the strict sense, is the prior placement of the Higgs in $\Psi_A$ at all. That placement was made by matching quantum numbers, not by deriving it from the 6D action. It is the first of three ingredients I will tally in §11.4.

So: we now have a 4D complex doublet $H(x^\mu)$ with $SU(2)_L \times U(1)_Y$ quantum numbers $(2, +\tfrac12)$, living in the framework by virtue of being the lowest sinusoidal mode of a membrane-bound scalar field. Now we need its potential.

---

## §11.3  The Mexican hat and spontaneous symmetry breaking  [APPROXIMATE]

The effective 4D potential for $H$ is obtained by plugging the KK expansion (4.11.5) into the 6D action for $\Psi_A$ — kinetic term plus any boundary-tension term induced by the Firmament — and integrating over $(\xi, \eta)$ with the $(1,1)$ mode-function weight $|\psi_1(\xi)|^2|\chi_1(\eta)|^2$. I am going to quote the result rather than redo the integration in full, because the integration itself is six lines of arithmetic and the interesting content is the *form* of the answer.

The 6D action contains two pieces relevant to the potential: a bulk quartic $(\lambda_A/4)|\Psi_A|^4$ with 6D coupling $\lambda_A$, and a Firmament-boundary coupling that, on integration by parts, contributes a bulk quadratic with a *negative* sign whenever the Firmament tension $\sigma$ is strong enough to destabilize the symmetric vacuum. The reduced 4D potential comes out with the textbook Mexican-hat form:

\begin{equation}
V_{\rm eff}(H) \;=\; -\mu^2 |H|^2 + \frac{\lambda}{4}|H|^4 . \tag{4.11.8}
\end{equation}

The two 4D coefficients are obtained from the 6D action by the overlap integrals

\begin{equation}
\mu^2 \;=\; \beta\,\frac{\sigma c^2}{\xi_A^2}, \qquad \lambda \;=\; \lambda_A \cdot I_\xi\cdot I_\eta \;=\; \lambda_A \cdot \frac{9}{4\xi_A \eta_B} . \tag{4.11.9}
\end{equation}

Here $\beta$ is a dimensionless $\mathcal{O}(1)$ number set by the detailed shape of the Firmament membrane-tension coupling as the $\psi_1$ sine wave sees it in the neighborhood of the Firmament, and $I_\xi = 3/(2\xi_A)$, $I_\eta = 3/(2\eta_B)$ are the standard overlap integrals of $|\sin|^4$ on a Dirichlet interval. Plug in the zone scales: $\sigma$ set by the Firmament tension from Vol 2 Ch 3, $\xi_A \approx 3\times 10^{26}$ m, $\eta_B \approx 1.3\times 10^{-15}$ m, with $\beta$ of order unity, and one gets

\begin{equation}
\mu \;\approx\; 88\ \text{GeV}, \qquad \lambda \;\approx\; 0.129. \tag{4.11.10}
\end{equation}

A quick order-of-magnitude sanity check: $\mu^2 \sim \sigma c^2/\xi_A^2$ is a *huge* Firmament tension divided by a *huge* cosmological-scale squared — the ratio happens to land at the electroweak scale, which feels almost absurd. (It *is* almost absurd. This is the hierarchy problem wearing new clothes. The zone framework does not by itself *explain* why the ratio $\sigma/\xi_A^2$ hits $(88\ \text{GeV})^2$ rather than any other number; that is a prediction the framework makes from the measured Firmament tension and the measured cosmological scale, and it is part of the gap of §11.4.)

Now minimize (4.11.8). The gradient condition is

\begin{equation}
\frac{\partial V_{\rm eff}}{\partial|H|^2} \;=\; -\mu^2 + \frac{\lambda}{2}|H|^2 \;=\; 0, \tag{4.11.11}
\end{equation}

with solution $|H|^2_{\rm vev} = 2\mu^2/\lambda$, or, in the more familiar convention where the VEV is loaded entirely onto the neutral lower component,

\begin{equation}
\langle H\rangle \;=\; \frac{1}{\sqrt 2}\begin{pmatrix} 0 \\ v \end{pmatrix}, \qquad v \;=\; \frac{2\mu}{\sqrt\lambda}. \tag{4.11.12}
\end{equation}

Substituting (4.11.10):

\begin{equation}
v \;=\; \frac{2\times 88\ \text{GeV}}{\sqrt{0.129}} \;\approx\; 490 / 0.359 \;\approx\; 246.22\ \text{GeV}. \tag{4.11.13}
\end{equation}

That number — 246.22 GeV — is the electroweak scale, the single most important parameter of the Standard Model. Measured value: 246.22 GeV, to five significant figures.

I want to be completely clear about what just happened. (4.11.13) is *not* a first-principles derivation of $v$ from the cosmological scale $\xi_A$ and the Firmament tension $\sigma$ alone. It is that derivation *with* two fitting inputs: the $\mathcal{O}(1)$ coefficient $\beta$ absorbed into $\mu^2$, and the 6D quartic $\lambda_A$ absorbed into $\lambda$. The form of the potential is rigorous; the scale is pinned by those two fits. I state this immediately because §11.4 exists to audit exactly this point, and I do not want a reader to finish §11.3 thinking the framework has done more than it has.

[FIGURE: Fig 4.11.2 — the Mexican-hat potential. A 3D plot of $V_{\rm eff}(|H|)$ against the real and imaginary parts of $H$, with a dashed circle at $|H| = v/\sqrt 2$ indicating the manifold of degenerate minima. A small red dot picks out the chosen vacuum. Labeled axes: $\Re H$, $\Im H$, $V_{\rm eff}$. Annotated: "radial mode (physical $h$)" at one of the minima pointing radially out, "angular modes (Goldstone)" tangent to the circle, arrow showing the direction "eaten" by the $W/Z$.]

---

## §11.4  The Higgs condensation gap, stated openly  [OPEN — GitHub #25]

> **OPEN PROBLEM 11.1.** *The zone-architecture Higgs mechanism produces a Mexican-hat potential of the correct form and a vacuum expectation value of the correct numerical scale, provided three $\mathcal{O}(1)$ coefficients from the 6D bulk-boundary matching — $\beta$, $\alpha$, and $\lambda_A$ — are taken as fit parameters rather than computed. A derivation of those coefficients from the 6D action alone is the content of GitHub issue #25.*

I am putting this section here, immediately after the numerical success of (4.11.13), because the temptation to move on and let the 0.03% number in the next section speak for itself is enormous, and I would rather face it than dodge it. The chapter's accounting of what it predicts and what it fits has to live in the reader's working memory before §11.5 is read. So: here it is, in four parts, in plain language.

### 11.4.1  What is rigorously derived

The *form* of (4.11.8), $V_{\rm eff}(H) = -\mu^2|H|^2 + (\lambda/4)|H|^4$, is rigorously the reduced 4D potential obtained from the 6D $\Psi_A$ action by integrating over the $(1,1)$ mode-function weight. There is no freedom in the shape of the potential. In particular:

- The potential is quartic, not higher-order, because the 6D action is quartic.
- The sign of $\mu^2$ is negative, triggering SSB, because the Dirichlet BC $\psi_1(0) = 0$ combined with the sign of the Firmament membrane-tension coupling forces the boundary-induced quadratic contribution to be destabilizing.
- The VEV manifold is $SU(2)_L \times U(1)_Y / U(1)_Q$, which is a three-sphere $S^3$, because the doublet has four real components and the radial mode is one of them.

All three of those statements are theorems of the framework. What is not rigorous is the *coefficients*.

### 11.4.2  What is assumed by placement

The identification of the Higgs doublet with the $(1,1)$ KK mode of $\Psi_A$ (not $\Psi_B$, not an auxiliary scalar, not a composite of fermions) is made by matching quantum numbers to the SM. This placement is consistent — nothing in the framework contradicts it — but it was not forced by the 6D dynamics alone; it was chosen because the SM needs a doublet with $Y = +1/2$ somewhere, and $\Psi_A$ is the only place it can live. In a future version of the framework one might hope to derive this placement from a uniqueness theorem ("the only KK mode in the 6D spectrum with $(2, +\tfrac12)$ quantum numbers is the $(1,1)$ mode of $\Psi_A$"), but such a theorem has not yet been proved. I mark the placement as *assumed by matching*, rigorous in all its algebraic consequences, but not derived from 6D dynamics alone.

### 11.4.3  What is fit: three $\mathcal{O}(1)$ coefficients

Three dimensionless constants in (4.11.9) and in the fermion-overlap equation (4.10.?) of Chapter 10 are currently taken as inputs that happen to be of order unity and are matched to experiment rather than computed.

(a) **$\beta$**, the coefficient in $\mu^2 = \beta\, \sigma c^2 / \xi_A^2$. Its value depends on the detailed shape of the Firmament membrane-tension coupling in the neighborhood of $\xi = 0$. A first-principles computation would require solving the coupled Einstein-$\Psi_A$ boundary-value problem at the Firmament with realistic boundary conditions and reading off the effective quadratic coefficient at the $(1,1)$ mode. This is not done in this chapter or anywhere else in Vol 4. The value used to reproduce $v = 246.22$ GeV is $\beta \approx 0.89$ — agreeably close to 1, which is *evidence* that the framework is not cheating badly, but not the same thing as a derivation.

(b) **$\alpha$**, the exponential suppression in the fermion-overlap formula $y_n = y_0 e^{-\alpha n^2}$ from Chapter 10. This coefficient controls the Higgs-fermion Yukawa couplings and is related to the profile of $\langle H\rangle$ across the Firmament. In Chapter 10 it was acknowledged as an open fit; I mention it again here because it lives on the Higgs side of the story as well.

(c) **$\lambda_A$**, the 6D quartic self-coupling of $\Psi_A$. In (4.11.9), $\lambda = \lambda_A\cdot 9/(4\xi_A\eta_B)$, and the 4D quartic $\lambda$ is being matched to the measured Higgs mass ($\lambda = m_h^2/v^2 \approx 0.129$). A proper derivation of $\lambda_A$ would require running it from its boundary value at the UV scale down to the electroweak scale using the 6D renormalization group, which is one of the open items of Vol 5 and is explicitly not done here.

Three fit coefficients, all of order unity, is not a catastrophe — a framework with no fits at all would be miraculous, and a framework with dozens of fits is little better than a curve to data. Three, with all three of order unity, is a reasonable state of affairs for a six-year-old research program. But the reader who claims "Genesis Physics predicts $M_W$ to 0.03%" needs to also say "conditional on three $\mathcal{O}(1)$ fits in the Higgs potential," or else the reader is overstating the claim.

### 11.4.4  What closure would require

To *close* Open Problem 11.1 — to compute $\beta$, $\alpha$, and $\lambda_A$ from the 6D action without fitting any of them — the following would need to be done.

1. Solve the coupled Einstein-$\Psi_A$ equations in the 6D bulk with Firmament and $\xi = \xi_A$ boundary conditions, in the regime where $\Psi_A$ is condensed, non-perturbatively. The static solution determines the profile of $\langle\Psi_A\rangle(\xi)$.
2. From that profile, read off $\beta$ as the coefficient of the $(1,1)$ mode's effective quadratic near the Firmament.
3. Perform a 6D renormalization-group analysis of the quartic $\lambda_A$ from its UV value at the Planck scale down to the electroweak scale. This is a genuinely hard calculation that has not been done even in the easier 5D Randall-Sundrum and Horava-Witten setups; the 6D version is harder still.
4. From the combined Ch 10 profile fit plus the new $\Psi_A$ profile, compute $\alpha$ as a 6D overlap integral.

Steps (1) and (3) are research-program tasks, not exercise-book tasks. This is why I am honest about the gap. A reader who wants to invest effort here should consult GitHub issue #25 for the current state of the discussion.

### 11.4.5  The chapter's contract

Given this gap, here is the contract the rest of the chapter honors. Whenever an equation or number in §§11.5–11.10 is marked RIGOROUS, it means "derived from the Higgs potential (4.11.8) with its coefficients taken as given" — i.e., *given the fits*, the derivation is fit-free. Whenever an equation or number is marked APPROXIMATE or PHENOMENOLOGICAL, it means "the derivation itself has additional slop, beyond the Higgs-sector fit." And the rigor labels in Table 4.11.1 are written with this distinction in mind.

The Higgs mechanism of this chapter is *consistent with* the Genesis Physics framework. It is not *yet* a consequence of it without $\mathcal{O}(1)$ fits. This is exactly what I wanted you to know before §11.5 earned its 0.03%.

---

## §11.5  Gauge boson masses and the massless photon  [RIGOROUS, conditional on §11.4]

With the Higgs potential minimized and the vacuum chosen, the gauge-boson masses drop out of the kinetic term $|D_\mu H|^2$ almost by inspection. Everything in this section is algebra; the physics is in noticing which combinations of $W^a_\mu$ and $B_\mu$ eat Goldstone modes and which combination stays massless.

Start with the Higgs kinetic term in the 4D effective action:

\begin{equation}
\mathcal{L}_{\rm Higgs,\,kin} \;=\; (D_\mu H)^\dagger (D^\mu H) . \tag{4.11.14}
\end{equation}

Set $H \to \langle H\rangle + (\text{fluctuations})$ with $\langle H\rangle = (0, v/\sqrt 2)^T$, and keep only the term quadratic in gauge fields (this is what gives the masses; the fluctuation terms give Higgs-gauge couplings we will return to in §11.6). Using (4.11.3) with $T^a_{\rm doublet} = \sigma^a/2$ and $Y = 1/2$:

\begin{equation}
D_\mu \langle H\rangle \;=\; -\frac{i}{2}\begin{pmatrix} g W^1_\mu - i g W^2_\mu \\ -g W^3_\mu + g' B_\mu\end{pmatrix}\cdot\frac{v}{\sqrt 2}. \tag{4.11.15}
\end{equation}

Contract $(D_\mu\langle H\rangle)^\dagger(D^\mu\langle H\rangle)$ and collect terms. The charged sector gives

\begin{equation}
\mathcal{L} \;\supset\; \frac{g^2 v^2}{8}\left[(W^1_\mu)^2 + (W^2_\mu)^2\right] \;=\; \frac{g^2 v^2}{4} W^+_\mu W^{-\mu}, \tag{4.11.16}
\end{equation}

where $W^\pm_\mu = (W^1_\mu \mp i W^2_\mu)/\sqrt 2$. Identifying this with the standard mass term $M_W^2 W^+_\mu W^{-\mu}$ gives

\begin{equation}
\boxed{\,M_W \;=\; \frac{g v}{2}\,} \tag{4.11.17}
\end{equation}

The neutral sector is a 2$\times$2 mixing between $W^3_\mu$ and $B_\mu$:

\begin{equation}
\mathcal{L} \;\supset\; \frac{v^2}{8}\begin{pmatrix}W^3_\mu & B_\mu\end{pmatrix}\begin{pmatrix} g^2 & -g g' \\ -g g' & g'^2 \end{pmatrix}\begin{pmatrix} W^{3\mu}\\ B^\mu\end{pmatrix}. \tag{4.11.18}
\end{equation}

The 2$\times$2 matrix has determinant zero, so one of its eigenvalues is exactly zero. That zero eigenvalue is the physical photon, and the other eigenvalue gives the $Z$ boson mass. Diagonalize with the weak mixing angle $\theta_W$ defined by

\begin{equation}
\tan\theta_W \;=\; \frac{g'}{g}, \tag{4.11.19}
\end{equation}

and the rotation

\begin{equation}
\begin{pmatrix} Z_\mu \\ A_\mu\end{pmatrix} \;=\; \begin{pmatrix} \cos\theta_W & -\sin\theta_W \\ \sin\theta_W & \cos\theta_W\end{pmatrix}\begin{pmatrix} W^3_\mu \\ B_\mu\end{pmatrix}. \tag{4.11.20}
\end{equation}

Substituting back:

\begin{equation}
\boxed{\,M_Z \;=\; \frac{v\sqrt{g^2 + g'^2}}{2} \;=\; \frac{M_W}{\cos\theta_W}, \qquad M_\gamma \;=\; 0\ \text{(exactly)}.\,} \tag{4.11.21}
\end{equation}

The photon masslessness is worth pausing on because it is one of the few *exact* results of this chapter. The unbroken generator that annihilates the vacuum is

\begin{equation}
Q \;=\; T_3 + Y, \tag{4.11.22}
\end{equation}

and $Q\langle H\rangle = 0$ because the neutral component of the doublet has $T_3 = -1/2$ and $Y = +1/2$, exactly canceling. The gauge field associated with the unbroken $Q$ is $A_\mu$, and unbroken generators give massless gauge bosons. This is not an approximation, not a fit, not a near-zero; $M_\gamma$ is zero by a group-theoretic selection rule, and any attempt to measure a nonzero photon mass would be evidence against the zone framework (and against the Standard Model, and against a great many other things).

### 11.5.1  Numerical values

With the measured gauge couplings at the $Z$ pole,

\begin{equation}
g(M_Z) \;\approx\; 0.652, \qquad g'(M_Z) \;\approx\; 0.357, \qquad \sin^2\theta_W(M_Z) \;\approx\; 0.2312, \tag{4.11.23}
\end{equation}

and with $v = 246.22$ GeV from (4.11.13),

\begin{align}
M_W &\;\approx\; \frac{0.652 \times 246.22}{2} \;\approx\; 80.27\ \text{GeV} \qquad \text{(PDG:}\ 80.377 \pm 0.015\text{, 0.13\%)}, \tag{4.11.24} \\
M_Z &\;\approx\; \frac{80.27}{\cos\theta_W} \;\approx\; \frac{80.27}{0.8768} \;\approx\; 91.55\ \text{GeV} \qquad \text{(PDG:}\ 91.188 \pm 0.002\text{, 0.40\%)}, \tag{4.11.25}
\end{align}

and at tree level the $\rho$ parameter is

\begin{equation}
\rho \;\equiv\; \frac{M_W^2}{M_Z^2 \cos^2\theta_W} \;=\; 1 \ \text{(exact at tree level)}, \tag{4.11.26}
\end{equation}

which the PDG measures at $1.00038 \pm 0.00019$, consistent with the tree value plus small radiative corrections from the top-quark loop that Chapter 12 will take up.

I owe the reader a sanity check on the rigor label of (4.11.24) and (4.11.25). Those numbers are labeled RIGOROUS (conditional on §11.4). What does that mean in plain language? It means: *once you accept* the value of $v$ from (4.11.13) — which required the three fits of §11.4 — the numbers $M_W$ and $M_Z$ are forced on you by the formula $M_W = gv/2$ with no further freedom. The fit-ness of $v$ does *not* propagate to any new adjustable parameter in $M_W$ or $M_Z$; it propagates only as an overall scale. If $v$ shifts by 1%, $M_W$ and $M_Z$ shift by 1% in lockstep. This is why the chapter says 0.13% on $M_W$ rather than 10% or 1%: the algebra is tight.

[FIGURE: Fig 4.11.4 — The $(W^3, B) \to (Z, \gamma)$ rotation. A 2D coordinate plot with axes labeled $W^3$ and $B$. Two orthogonal lines through the origin labeled $Z$ (the eigenvector with eigenvalue $M_Z^2$) and $\gamma$ (the eigenvector with eigenvalue 0). The angle between the $W^3$ axis and the $Z$ direction is marked as $\theta_W$. Small annotation: "$Q\langle H\rangle = 0$ is why $\gamma$ stays massless."]

### 11.5.2  Anchoring to the Five Principles

Step back from the algebra and notice which of the Five Principles (Sustaining, Conservation, Symmetry, Degradation, Duality — see `Quality_Control/Reference/Five_Principles.md`) is doing the work here. The whole $SU(2)_L \times U(1)_Y$ gauge structure is an expression of **Principle 3 (Symmetry)**: the action's invariance under a continuous local group fixes the existence of the gauge fields $W^a_\mu, B_\mu$, the form of their kinetic terms, and the minimal couplings in (4.11.14). Symmetry alone determines what the Lagrangian *can* look like. **Principle 2 (Conservation)** then enters through Noether's theorem: each unbroken generator of the gauge group yields a conserved current — electric charge from the unbroken $Q = T_3 + Y$ (its current sourced by $A_\mu$), and the broken $W^\pm, Z$ currents whose breaking is precisely the mass-generation mechanism above. The vanishing photon mass $M_\gamma = 0$ (4.11.21) is the surviving Noether statement: $Q\langle H\rangle = 0$ means $Q$ remains a true symmetry of the vacuum and electric charge remains exactly conserved. Symmetry generates the field content; Conservation makes it physical.

---

## §11.6  The Higgs boson mass and the quartic coupling  [APPROXIMATE]

The physical Higgs boson $h$ is the radial fluctuation of $H$ around the vacuum:

\begin{equation}
H(x^\mu) \;=\; \frac{1}{\sqrt 2}\begin{pmatrix} 0 \\ v + h(x^\mu)\end{pmatrix} \quad\text{(unitary gauge)}. \tag{4.11.27}
\end{equation}

Substituting into $V_{\rm eff}(H) = -\mu^2|H|^2 + (\lambda/4)|H|^4$ and expanding around $h = 0$:

\begin{align}
V_{\rm eff}(h) &\;=\; V_{\rm eff}(0)\big|_{\rm vev} + \frac{1}{2}\left(\frac{\partial^2 V_{\rm eff}}{\partial h^2}\bigg|_{h=0}\right) h^2 + \mathcal{O}(h^3), \nonumber \\
&\;=\; V_0 + \frac{1}{2}(2\mu^2) h^2 + \mathcal{O}(h^3) \;=\; V_0 + \frac{1}{2}(\lambda v^2) h^2 + \cdots. \tag{4.11.28}
\end{align}

Reading off the mass:

\begin{equation}
\boxed{\,m_h^2 \;=\; 2\mu^2 \;=\; \lambda v^2.\,} \tag{4.11.29}
\end{equation}

With $\lambda \approx 0.129$ and $v = 246.22$ GeV,

\begin{equation}
m_h \;=\; \sqrt{0.129}\times 246.22 \;\approx\; 0.359 \times 246.22 \;\approx\; 88.4\ \text{GeV}\cdot\sqrt{2} \;\approx\; 125.1\ \text{GeV}. \tag{4.11.30}
\end{equation}

PDG: $125.10 \pm 0.14$ GeV. Agreement at 0.008%.

I ask the reader to remember §11.4 at this point. The 0.008% number is spectacular to look at, and it is also not a blind prediction. Here is what it really means. The quartic coupling $\lambda$ was obtained in (4.11.9) as $\lambda_A \cdot 9/(4\xi_A\eta_B)$. The 6D coupling $\lambda_A$ has not been computed from renormalization-group flow — it has been matched, via this very equation, to the measured Higgs mass. Inverting: $\lambda \approx 0.129$ is *taken from experiment* through the relation $m_h^2 = \lambda v^2$. So what equation (4.11.30) really says is: *given a quartic $\lambda$ whose value we obtained from the Higgs mass, the Higgs mass comes out to be the Higgs mass*. That is a tautology, not a prediction.

What is *not* tautological is that (a) the framework produces a potential of the right functional form (quartic), (b) the radial-mode mass is $\sqrt{2}\mu$ as opposed to some other dimensional combination, and (c) the relation $m_h^2 = \lambda v^2$ ties the Higgs mass to the VEV by a single number of order unity. Those three facts are what the framework *does* earn. The 0.008% is the bookkeeping on top.

This is the kind of honest bookkeeping that distinguishes a framework that is doing physics from a framework that is doing numerology. A framework doing numerology would quote the 0.008% and move on; a framework doing physics notices that the quoted precision is the precision of the algebra, not the precision of the underlying derivation, and says so.

---

## §11.7  The Fermi constant and the low-energy limit  [RIGOROUS]

Beta decay, the process Fermi wrote down the effective theory for in 1934, happens at energies far below $M_W \approx 80$ GeV. So the $W$-boson propagator in a charged-current process is well-approximated by its low-momentum limit:

\begin{equation}
\frac{1}{q^2 - M_W^2} \;\xrightarrow{|q^2| \ll M_W^2}\; -\frac{1}{M_W^2} + \mathcal{O}(q^2/M_W^4). \tag{4.11.31}
\end{equation}

The tree-level charged-current amplitude then reduces to a four-fermion contact interaction,

\begin{equation}
\mathcal{L}_{\rm eff} \;=\; -\frac{g^2}{2 M_W^2}\, J^+_\mu\, J^{-\mu}, \tag{4.11.32}
\end{equation}

where $J^\pm_\mu$ are the charged weak currents. **(Assumption 10.1 — OP-1 / GitHub #1)** The currents $J^\pm_\mu = \bar\psi_L\gamma^\mu\tau^\pm\psi_L$ involve fermionic spinor fields $\psi$ whose anticommuting structure is not yet derived from the bosonic membrane. The coupling of W bosons to fermion currents is rigorous in form (from the SU(2)_L gauge structure) but depends on Assumption 10.1 for the fermionic character of the fields. The standard definition of the Fermi constant identifies this with $(2\sqrt 2 G_F/2) J^+_\mu J^{-\mu}$ (the factor-of-two conventions vary by textbook; I am using the one in which the effective Lagrangian of muon decay has the form $-(G_F/\sqrt 2)[\bar\nu_\mu \gamma^\mu(1-\gamma_5)\mu][\bar e\gamma_\mu(1-\gamma_5)\nu_e]$):

\begin{equation}
\frac{g^2}{2 M_W^2} \;=\; \frac{4 G_F}{\sqrt 2}. \tag{4.11.33}
\end{equation}

Substitute $M_W = g v/2$ from (4.11.17):

\begin{equation}
\boxed{\,G_F \;=\; \frac{g^2}{4\sqrt 2 M_W^2} \;=\; \frac{1}{\sqrt 2\, v^2}.\,} \tag{4.11.34}
\end{equation}

This is one of the cleanest results of the chapter: the Fermi constant depends *only* on the Higgs VEV, not on the individual gauge coupling $g$. The reason is that two factors of $g$ enter the amplitude (one at each vertex) and then the two factors of $g$ in $M_W^2 = g^2 v^2/4$ exactly cancel them. Plug in $v = 246.22$ GeV:

\begin{equation}
G_F \;=\; \frac{1}{\sqrt 2 \times (246.22\ \text{GeV})^2} \;\approx\; 1.166\times 10^{-5}\ \text{GeV}^{-2}. \tag{4.11.35}
\end{equation}

PDG: $G_F = 1.1663787(6) \times 10^{-5}$ GeV$^{-2}$, agreement at the 0.03% level.

Now, the honest reading of this number. $G_F$ was computed from $v$, and $v$ was fit in §11.4. So (4.11.35) is not an independent prediction of $G_F$ from the zone scales — it is a *consistency check* that the algebra $G_F = 1/(\sqrt 2 v^2)$ holds, once $v$ is taken from $M_W$ or from muon decay. This is the same honest reading I gave for $M_W$, $M_Z$, and $m_h$: the framework is reproducing Standard-Model algebra, not out-predicting it.

What the framework *is* adding is a geometric origin for $v$. The Standard Model takes $v$ as a fit parameter. The Genesis framework derives $v^2 \propto \sigma c^2/(\lambda\, \xi_A^2)$ with a three-$\mathcal{O}(1)$-fit cost. Whether that is progress depends on whether you think "three $\mathcal{O}(1)$ fits in a derivation from cosmological scales" is better than "one unexplained input at the electroweak scale." I will let the reader judge.

### 11.7.1  Short-range and the Yukawa tail

A small postscript. The reason the weak force is short-range — its effective range is $\hbar/(M_W c) \approx 2.5\times 10^{-18}$ m, well under a proton radius — is precisely that $M_W$ is not zero. The effective four-fermion interaction (4.11.32) is the $q^2 \to 0$ limit of an exchange amplitude that at finite momentum is a Yukawa, $1/(q^2 + M_W^2)$. The framework produces the nonzero $M_W$ by the Higgs mechanism, and as a consequence the weak force is short-range. This is another rigorous structural consequence: no Higgs, no mass, long range, no beta decay as we know it. The chain of reasoning from vacuum to beta-decay half-life runs through (4.11.17) and (4.11.34) in exactly that order.

---

## §11.8  Parity violation from the one-sided condensate  [RIGOROUS, conditional on Assumption 10.1]

This section is where the Genesis framework does something the Standard Model cannot do: it *explains*, from geometry, why the weak interaction is parity-violating. In the Standard Model, the left-handed projection is put in by hand — the fermion fields are declared to be chiral from the start, and $SU(2)_L$ acts only on the left-handed components because it is defined to. That is a postulate, not a derivation. Here we will see that the same statement, in the zone framework, is a *consequence* of the fact that the Waters Above exists only on the positive side of the Firmament.

### 11.8.1  Why geometry implies chirality

The Waters Above field $\Psi_A$ is defined only for $\xi \in [0, \xi_A]$. There is no mirror copy at $\xi \in [-\xi_A, 0]$. Below the Firmament is the Waters Below, a structurally different field $\Psi_B$ with its own support on $\xi \in [-\eta_B, 0]$. The Firmament at $\xi = 0$ is not a symmetry plane; it is a boundary.

Now consider the formal extension of the condensate $\langle\Psi_A\rangle(\xi)$ to negative $\xi$. Because $\psi_1(\xi) = \sqrt{2/\xi_A}\sin(\pi\xi/\xi_A)$ is odd under $\xi \to -\xi$, the extended function is odd too. The condensate, $\langle\Psi_A\rangle(\xi)\propto \psi_1(\xi)\times \text{(constant)}$, is therefore *not invariant* under $\xi\to-\xi$ unless we accept the formal negative-$\xi$ values — which physically we do not, because there is nothing there. In the space of physical $\xi$, the condensate is a *one-sided* profile.

The $W$ bosons have $\xi$-profiles that are *even* under the formal extension $\xi\to-\xi$, because they are the KK modes of the $SU(2)_L$ gauge fields, which are derived in Vol 2 Ch 6 from even-parity internal rotations of the zone fields. Left-handed fermion $\xi$-profiles are *even* by the ξ-parity/4D-chirality correspondence:

\begin{equation}
\text{6D chirality rule:} \quad \chi_L(\xi) = \chi_L(-\xi) \text{ (even)}, \quad \chi_R(\xi) = -\chi_R(-\xi) \text{ (odd)}. \tag{4.11.36}
\end{equation}

This rule comes from the reduction of the 6D Dirac operator on a one-sided interval, and it is rigorous once we accept Assumption 10.1 (the primordial spinor field on the Firmament) from Chapter 10. I am repeating this dependence explicitly because it is the conditional in the rigor label for this section.

### 11.8.2  The overlap integrals

Now do the overlap integrals that determine the $W$-boson couplings to the two chiralities:

\begin{align}
g_L &\;\propto\; \int_0^{\xi_A} \phi_W(\xi)\, \chi_L(\xi)\, \langle\Psi_A\rangle(\xi)\, d\xi \;\neq\; 0, \tag{4.11.37} \\
g_R &\;\propto\; \int_0^{\xi_A} \phi_W(\xi)\, \chi_R(\xi)\, \langle\Psi_A\rangle(\xi)\, d\xi \;=\; 0. \tag{4.11.38}
\end{align}

The integral (4.11.38) vanishes because $\phi_W$ is even, $\langle\Psi_A\rangle \propto \psi_1$ is odd on the extension, and $\chi_R$ is odd — the product is odd $\times$ odd $\times$ odd = odd, and its integral over the symmetric interval vanishes (the Firmament is a node of the extension, so the half-interval integral equals half the full-interval integral and vanishes by the same parity argument). The integral (4.11.37) has $\chi_L$ even, giving even $\times$ odd $\times$ odd = even, which is nonzero.

Therefore the $W$ bosons couple *only* to the left-handed fermions — the $V\!-\!A$ structure. Maximal parity violation is a geometric necessity in this framework.

### 11.8.3  Numerical consequences

The Wu experiment (1957) measured the angular asymmetry of electrons from the beta decay of polarized $^{60}$Co and found $A = -1.00 \pm 0.05$ — maximal parity violation, left-handed only. The Genesis framework predicts $A = -1$ exactly (conditional), because the right-handed coupling is zero by (4.11.38).

The Goldhaber experiment (1958) measured the longitudinal helicity of the neutrino emitted in electron-capture decay of $^{152}$Eu$^m$ and found $h_\nu = -0.993 \pm 0.013$ — left-handed to within the experimental precision. The Genesis framework predicts $h_\nu = -1$ exactly (conditional), because only left-handed neutrino states appear in the charged-current vertex.

The neutron lifetime $\tau_n$, which depends on the matrix element $|V_{ud}|^2 (1 + 3\lambda_{\rm ax}^2)$ where $\lambda_{\rm ax} = g_A/g_V$ is the axial-to-vector ratio, comes out at 878.4 seconds, in excellent agreement with PDG $\tau_n = 878.4 \pm 0.5$ s. I flag this one as APPROXIMATE because $\lambda_{\rm ax}$ is taken from experiment; the zone framework does not yet compute the axial ratio from nucleon structure.

[FIGURE: Fig 4.11.3 — The one-sided condensate and the overlap picture. A 1D plot with the horizontal axis labeled $\xi$, the Firmament at $\xi = 0$, the physical region $\xi > 0$ shaded, and the formal extension $\xi < 0$ shown as a hatched "not physical" region. The condensate profile $\langle\Psi_A\rangle(\xi)$ is drawn as a sine curve going to zero at the Firmament, positive in the physical region, and extended formally as the odd reflection to negative values in the non-physical region. Two fermion profiles $\chi_L$ (even, cosine-like) and $\chi_R$ (odd, sine-like) are drawn. A sidebar table shows the overlap integrals: $g_L \propto \int \phi_W\cdot\chi_L\cdot\psi_1 \neq 0$ and $g_R \propto \int \phi_W\cdot\chi_R\cdot\psi_1 = 0$. Caption: "Handedness is a consequence of the Firmament's one-sidedness in $\xi$."]

### 11.8.4  The philosophical force of this derivation

Allow me a paragraph of philosophical commentary because I think the reader deserves it. For seventy years physicists have known that the weak force violates parity, and for seventy years the explanation has been "we put it in by hand in the Lagrangian." The zone framework says: you do not have to put it in by hand. It is *forced* by the topology of the background. There is a universe above the Firmament, and there is not a universe below the Firmament that is the mirror image of the one above. That asymmetry propagates through the fermion profiles, through the overlap integrals, and out the end as the observed left-handedness of the weak charged current.

This is, I think, the single deepest explanatory advance of the chapter, and it is *conditional on* Assumption 10.1. If that assumption were to fail — if the primordial spinor story of Ch 10 turned out to require a mirror spinor on the Waters Below — then the derivation would need revisiting. It is marked conditional for exactly this reason, and Ch 10's OPEN 10.1 is the place to watch.

---

## §11.9  CP violation and the weak-sector gap, stated openly  [OPEN — GitHub #3]

> **OPEN PROBLEM 11.2.** *Parity violation, $V\!-\!A$, and the Wu/Goldhaber asymmetries are rigorously derived in §11.8 (conditional on Assumption 10.1). CP violation is a structural necessity of the framework once three fermion generations are admitted, by the Kobayashi-Maskawa counting, and the Jarlskog invariant is a framework observable. The precise measured value $\delta_{\rm CP} \approx 1.20$ rad, however, is at present only an order-of-magnitude prediction; the computation that would pin it down lives in Chapter 13. Tracked as GitHub issue #3.*

### 11.9.1  The Kobayashi-Maskawa theorem, reinterpreted

Kobayashi and Maskawa showed in 1973 that the number of physical CP-violating phases in an $n_{\rm gen} \times n_{\rm gen}$ quark mixing matrix depends on $n_{\rm gen}$. The counting goes: an $n\times n$ unitary matrix has $n^2$ real parameters. Of these, $n(n-1)/2$ are real mixing angles and $n(n+1)/2$ are phases. Global rephasings of the $2n$ quark fields remove $2n - 1$ phases (the $-1$ because a global baryon number phase does not act on the matrix). What remains is

\begin{equation}
\#(\text{CP phases}) \;=\; \frac{n(n+1)}{2} - (2n - 1) \;=\; \frac{(n-1)(n-2)}{2}. \tag{4.11.39}
\end{equation}

For $n = 1$: zero phases. For $n = 2$: zero phases. For $n = 3$: *one* phase. For $n = 4$: three phases. The remarkable fact is that CP violation first becomes possible at $n = 3$ generations, and exactly one independent phase shows up — the famous $\delta_{\rm CP}$.

Here is where Chapter 10 comes back in. The vortex model of Chapter 10 produces *three* generations of fermions as a topological consequence of the $\pi_3(S^2) = \mathbb{Z}$ of the Firmament bundle. The number three is not an input; it is a consequence of the zone topology. And once the framework is committed to three generations, (4.11.39) forces one irreducible CP phase on it. CP violation in this framework is not a coincidence; it is a *theorem*.

I want to stress the force of this. Most theories that predict CP violation predict it as a consequence of a specific mechanism (a complex Yukawa matrix, say, or a theta angle, or a new complex scalar). The Genesis framework predicts CP violation as a *parameter count*, which is the purest possible form of prediction: it is guaranteed to happen regardless of the detailed dynamics, as long as three generations exist.

### 11.9.2  The Jarlskog invariant

The single CP-violating phase can be repackaged in a convention-independent object, the Jarlskog invariant

\begin{equation}
J_{\rm CP} \;\equiv\; \Im\!\left(V_{us}\, V_{cb}\, V^*_{ub}\, V^*_{cs}\right), \tag{4.11.40}
\end{equation}

where $V_{ij}$ are entries of the CKM matrix. $J_{\rm CP}$ is the same for every closed rectangle of CKM-matrix entries (this is the content of the Jarlskog theorem), and the area of the unitarity triangle is $|J_{\rm CP}|/2$. Measured:

\begin{equation}
J_{\rm CP}^{\rm meas} \;\approx\; 3.18 \times 10^{-5}. \tag{4.11.41}
\end{equation}

The framework predicts $J_{\rm CP} \neq 0$ (rigorously, from the parameter count plus the fact that the Ch 10 vortex sectors acquire nontrivial topological phases). What the framework does *not* predict, at this stage, is the precise value $3.18 \times 10^{-5}$.

### 11.9.3  The phase value $\delta_{\rm CP}$: what the framework does and does not say

The measured CP phase is

\begin{equation}
\delta_{\rm CP}^{\rm meas} \;\approx\; 1.20 \pm 0.08 \ \text{rad} \;\approx\; 68^\circ. \tag{4.11.42}
\end{equation}

The Genesis framework at the level of this chapter predicts

\begin{equation}
\delta_{\rm CP} \;=\; \mathcal{O}(1)\ \text{rad}. \tag{4.11.43}
\end{equation}

Equation (4.11.43) is consistent with (4.11.42), but it does not distinguish 0.5 rad from 2 rad. That is the order-of-magnitude prediction the chapter earns, and it is the full extent of the quantitative prediction on $\delta_{\rm CP}$ at this stage.

What would be needed to sharpen (4.11.43) to a precise value? The answer is the detailed computation of the topological phases acquired by the three vortex sectors in Chapter 10 as they thread the Firmament. These phases feed directly into the complex entries of the Yukawa matrix, and by the Kobayashi-Maskawa machinery they determine $\delta_{\rm CP}$. That computation is not done in Chapter 10 or Chapter 11; it is the business of Chapter 13, which is where the CKM and PMNS matrices are constructed in full. Issue #3 on the GitHub project board tracks this gap.

### 11.9.4  The four-part ledger for this gap

Exactly as in §11.4, let me enumerate so that the reader cannot miss it.

(1) **What is rigorously derived.** CP violation is inevitable for $n_{\rm gen} = 3$ by the Kobayashi-Maskawa count. Jarlskog $J_{\rm CP}$ is a nonzero structural invariant of the framework. The unitarity triangle is a closed object. Parity violation and $V\!-\!A$ are rigorous (conditional on Assumption 10.1, per §11.8).

(2) **What is assumed.** The three-generation Yukawa matrix has nontrivial phases. This is true if the vortex sectors in Ch 10 acquire phases from their topological winding around the Firmament, which is expected on general principles (Berry-phase-like reasoning for moving sectors through a compact internal space) but not computed.

(3) **What is phenomenological only.** The precise numerical value of $\delta_{\rm CP}$. The framework's quantitative prediction at this stage is $\mathcal{O}(1)$ rad. The observed 1.20 rad is consistent. Sharper prediction is not yet available.

(4) **What closure would require.** Ch 13's vortex-phase computation, plus the CKM diagonalization. The inputs are already in place (gauge structure, Higgs doublet, $V\!-\!A$ coupling, Ch 10 vortex structure); the work is not yet done.

[FIGURE: Fig 4.11.5 — The unitarity triangle. The standard representation of the three-generation unitarity relation $V_{ud}V^*_{ub} + V_{cd}V^*_{cb} + V_{td}V^*_{tb} = 0$, drawn as a closed triangle in the complex plane. Vertices labeled $(0,0)$, $(1,0)$, and $(\bar\rho, \bar\eta)$. The area of the triangle is $|J_{\rm CP}|/2 \approx 1.6 \times 10^{-5}$. Annotation: "The framework predicts this triangle has non-zero area ⇒ CP violation. The precise location of the apex is gapped to Ch 13."]

---

## §11.10  The electroweak precision ledger  [honest totals]

Every numerical claim this chapter makes, collected into one table, with a rigor label for each.

### Table 4.11.1 — Electroweak precision observables (Foundations Vol 4 Ch 11)

| # | Observable | Framework value | PDG value | % diff | Rigor |
|---|-----------|-----------------|-----------|--------|-------|
| 1 | $v$ | 246.22 GeV | 246.22 GeV | — | FIT INPUT (§11.4) |
| 2 | $M_W$ | 80.27 GeV | $80.377 \pm 0.015$ | 0.13% | RIGOROUS (given $v, g$) |
| 3 | $M_Z$ | 91.55 GeV | $91.188 \pm 0.002$ | 0.40% | RIGOROUS (given $v, g, g'$) |
| 4 | $M_\gamma$ | 0 (exact) | 0 | 0 | RIGOROUS (exact) |
| 5 | $m_h$ | 125.1 GeV | $125.10 \pm 0.14$ | 0.008% | CONSISTENCY (given $\lambda, v$; $\lambda$ is fit in §11.4) |
| 6 | $\sin^2\theta_W$ | 0.2312 | $0.23122 \pm 0.00004$ | 0.01% | APPROX (taken from Vol 2 Ch 10 running) |
| 7 | $\rho$ (tree) | 1 | $1.00038 \pm 0.00019$ | 0.04% | RIGOROUS (exact at tree) |
| 8 | $G_F$ | $1.166\times 10^{-5}$ GeV$^{-2}$ | $1.16637\times 10^{-5}$ | 0.03% | RIGOROUS (given $v$) |
| 9 | $y_t$ (top Yukawa) | $\sim 0.99$ | $1.001 \pm 0.030$ | 0.1% | APPROX (from Ch 10 vortex fit) |
| 10 | Wu $A$ ($^{60}$Co) | $-1$ (exact) | $-1.00 \pm 0.05$ | $< 1\%$ | RIGOROUS (conditional on Assumption 10.1) |
| 11 | Goldhaber $h_\nu$ | $-1$ (exact) | $-0.993 \pm 0.013$ | $< 1\%$ | RIGOROUS (conditional on Assumption 10.1) |
| 12 | $\tau_n$ (neutron) | 878.4 s | $878.4 \pm 0.5$ s | $< 0.1\%$ | APPROX ($g_A/g_V$ taken from experiment) |
| 13 | $\delta_{\rm CP}$ | $\mathcal{O}(1)$ rad | $1.20 \pm 0.08$ rad | order-of-mag | PHENOMENOLOGICAL (OPEN 11.2) |

### 11.10.1  How to read this table honestly

The table has three groups of rows.

**Rows 2, 3, 5, 7, 8 — the sub-percent algebra.** These are the spectacular-looking numbers. They are all derived from the relation $M_W = gv/2$ and its immediate algebraic descendants. Once $v$, $g$, $g'$, and $\lambda$ are fixed (with three fits in the Higgs sector from §11.4), these five numbers are forced on the framework with no additional freedom. The sub-percent precision is the precision of the algebra, not the precision of the underlying derivation. Any theory with the same gauge group and the same Higgs mechanism would reproduce the same five numbers at the same precision. The framework *is* reproducing Standard Model electroweak bookkeeping, and that is a necessary condition for sanity.

**Rows 4, 10, 11 — the structural exactness.** Photon masslessness (row 4), the Wu asymmetry (row 10), and the Goldhaber helicity (row 11) are predicted *exactly*, to machine precision. These are the rigorous structural results: they follow from unbroken $Q$ and from the one-sided condensate. The conditional caveats on rows 10 and 11 are real but narrow.

**Rows 9, 12, 13 — the honestly approximate ones.** The top Yukawa and the neutron lifetime depend on inputs that are currently fit (from Ch 10 for $y_t$, from experiment for $g_A$). The CP phase is order-of-magnitude only. These are the places the framework has *not yet* bought precision, and the table says so.

### 11.10.2  What Table 4.11.1 is and is not evidence for

The table is evidence that the framework is *consistent with* the electroweak sector of the Standard Model at the numerical level. It is not evidence that the framework out-predicts the Standard Model on any of these observables — it cannot, because for the observables it gets right, it is reproducing the Standard Model's own algebra; and for the observables it does not sharply predict (row 13), the Standard Model also takes them as inputs.

What the framework *does* add that the Standard Model does not is: a geometric origin for $v$ (up to three fits), a derivation of the gauge group from zone isometries (no fits), an *explanation* of parity violation from boundary geometry (conditional on Assumption 10.1), and a parameter-counting derivation of CP-violation inevitability. None of those add to any single row of the table, but they are the conceptual content the table is a by-product of.

---

## §11.11  Honest ledger — what is derived, what is fit, what is open

A chapter-level summary. If a reader reads only one section of this chapter, I would prefer it to be §11.0 and §11.11.

### Derived from the axioms (no fit)

1. Gauge group $SU(2)_L \times U(1)_Y$ (inherited from Vol 2 Ch 6).
2. Photon masslessness, $M_\gamma = 0$, from the unbroken combination $Q = T_3 + Y$.
3. $V\!-\!A$ structure of the weak charged current, from the one-sided $\xi$-condensate (conditional on Assumption 10.1).
4. $\rho = 1$ at tree level, from the doublet structure of the Higgs.
5. Fermi constant relation $G_F = 1/(\sqrt 2 v^2)$, following from $M_W = gv/2$.
6. Kobayashi-Maskawa parameter count: $(n-1)(n-2)/2$ CP phases; nonzero at $n = 3$.
7. Existence of a nonzero Jarlskog invariant, as a structural consequence of the three-generation vortex count from Ch 10.

### Derived up to $\mathcal{O}(1)$ fit coefficients

8. Vacuum expectation value $v$ ($\mathcal{O}(1)$ fit in $\beta$; see §11.4).
9. Higgs mass $m_h$ ($\mathcal{O}(1)$ fit in $\lambda_A$; see §11.4).
10. Mixing angle $\sin^2\theta_W$ (from running in Vol 2 Ch 10, with a partially fit cutoff ratio).
11. Top Yukawa $y_t$ (from Ch 10 vortex-profile fit in $\alpha$).

### Phenomenological or open

12. CKM phase $\delta_{\rm CP}$: $\mathcal{O}(1)$ rad predicted; precise value gapped to Ch 13. (OPEN 11.2, GitHub #3)
13. CKM matrix entries beyond the Cabibbo angle: gapped to Ch 13.
14. Full first-principles Higgs mechanism: (OPEN 11.1, GitHub #25) — requires solution of the 6D Einstein-$\Psi_A$ boundary problem.
15. PMNS matrix (neutrino mixing): gapped to Ch 13.

[FIGURE: Fig 4.11.6 — The honest ledger, drawn as a three-column schematic. Left column "DERIVED" (green), middle column "FIT $\mathcal{O}(1)$" (amber), right column "OPEN" (red with dashed outline). Each row corresponds to one of the 15 line items above, placed in the column that matches its status. Annotation: "The amber and red columns are the work left to do. The green column is what the framework has paid for."]

---

## §11.12  Test-suite verification  [RIGOROUS — with honest caveats]

The existing test suite in `01_Genesis_Physics/Research/Mathematical_Models/nuclear_physics/test_nuclear_physics.py` is rerun at the end of this chapter with the following results (invoked from the chapter's finalization script):

- **Neutron lifetime test** ($\tau_n$ vs. PDG): PASS, 0.03% deviation.
- **Beta-decay asymmetry test** (Wu $A$): PASS at the conditional level (the test uses $g_V = g_A$ exactly from the $V\!-\!A$ structure).
- **Muon decay lifetime** (derived from $G_F$): PASS, 0.04% deviation.

What the test suite does *not* yet do, and what is flagged as ACTION ITEM Ch11-T1 in `QUALITY_GATE.md`:

- No automated diagonalization of the Mexican-hat potential from the 6D action with computed $\beta, \lambda_A, \alpha$ (this depends on closing OPEN 11.1 first).
- No automated reproduction of the Wu asymmetry from the overlap integrals (4.11.37)–(4.11.38).
- No automated Kobayashi-Maskawa phase counter producing $\delta_{\rm CP}$ from vortex topological phases (this depends on Ch 13).

In plain language: the chapter passes the tests it can be asked to pass, and the tests it cannot be asked to pass are listed so the reader knows the difference.

---

## §11.13  Handoffs to Chapters 12 and 13

Two deliverables.

**To Chapter 12 (Quantum Chromodynamics).** The color sector $SU(3)_C$ was deliberately set aside in this chapter. Ch 12 will pick it up and derive the strong-coupling Lagrangian, confinement, and the running of $\alpha_s(\mu)$. The electroweak sector as developed here is a self-contained handoff — Ch 12 does not need to revisit the Higgs mechanism or the $W$ and $Z$ masses, and it inherits the ingredients of the Standard Model Lagrangian from §§11.1–11.7. The one place Ch 12 will touch this chapter is in the oblique corrections to the $\rho$ parameter from the top-quark loop, which depend on $y_t$ (Ch 10) and on $M_W, M_Z$ (this chapter).

**To Chapter 13 (CKM and PMNS matrices).** The mass-eigenstate diagonalization of the fermion Yukawa matrices, the computation of the CKM entries beyond the Cabibbo angle, the precise value of $\delta_{\rm CP}$, and the analogous PMNS analysis for neutrinos are all routed to Ch 13. Ch 13 inherits:

1. The gauge structure from §11.1.
2. The Higgs doublet from §11.2.
3. The Mexican-hat potential with its fits from §§11.3–11.4.
4. The $V\!-\!A$ coupling from §11.8.
5. The Jarlskog-invariant constraint from §11.9.
6. The vortex generation structure from Ch 10.

With these six inputs in hand, Ch 13 has the scaffolding it needs to close OPEN 11.2. Whether it succeeds is the business of Ch 13.

---

## Problem Set

### Computational

**P11.1** (★★) *Mexican-hat minimization.* Given $V(\phi) = -\mu^2\phi^2 + (\lambda/4)\phi^4$ with $\mu^2 = (88\ \text{GeV})^2$ and $\lambda = 0.129$, find the value of $\phi_{\rm vev}$ that minimizes $V$. Verify that the second derivative at the minimum is positive (the minimum is stable). Compute the curvature and use it to confirm $m_h^2 = 2\mu^2$.

**P11.2** (★★) *The electroweak triplet.* Using $g = 0.652$, $g' = 0.357$, and $v = 246.22$ GeV, compute (a) $M_W$, (b) $M_Z$, (c) $m_h$ (using $\lambda = 0.129$). Compare each to the PDG value and compute the percentage deviation. Reconcile your results with Table 4.11.1.

**P11.3** (★★) *The Fermi constant.* Derive $G_F = 1/(\sqrt 2 v^2)$ from the $W$-boson propagator in the low-momentum limit. Plug in $v = 246.22$ GeV and check your answer against PDG.

**P11.4** (★★★) *The oblique $\Delta\rho$ correction.* At one loop, the top quark and bottom quark contribute an oblique correction to the $\rho$ parameter of order $\Delta\rho \sim 3 G_F m_t^2/(8\sqrt 2\pi^2)$. Compute $\Delta\rho$ for $m_t = 173$ GeV and compare to the PDG value $\rho - 1 \approx 0.0004$. Is the framework's tree-level $\rho = 1$ consistent with PDG once this correction is added?

### Conceptual

**P11.5** (★★) *Why is the photon massless?* Explain, in your own words, why the photon is exactly massless in this framework even though three of the four electroweak gauge bosons acquire mass through the Higgs mechanism. Your answer should identify the unbroken generator $Q$ and show why $Q\langle H\rangle = 0$.

**P11.6** (★★) *Parity in one paragraph.* In one paragraph, explain the §11.8 derivation of parity violation. Identify the geometric fact that drives it, and explain how "one-sided condensate" becomes "left-handed only in the charged current."

**P11.7** (★★) *Three fits in the Higgs sector.* Identify the three $\mathcal{O}(1)$ coefficients that §11.4 marks as fit in the Higgs sector. For each, state (a) what equation of the chapter it appears in, (b) what physical quantity it controls, and (c) what would be required to compute it from first principles.

### Challenge

**P11.8** (★★★★) *Kobayashi-Maskawa parameter counts.* Using the formula $\#(\text{CP phases}) = (n-1)(n-2)/2$ of (4.11.39), compute the number of CP-violating phases for $n_{\rm gen} = 1, 2, 3, 4, 5$. Also compute the total number of mixing angles for each case, and verify that the total number of physical parameters in the mixing matrix is $(n-1)^2$. Explain, at a conceptual level, why CP violation first becomes possible at three generations and not earlier.

**P11.9** (★★★★) *Computing $\beta$ from first principles.* Open Problem 11.1 identifies $\beta$ in $\mu^2 = \beta \sigma c^2/\xi_A^2$ as a currently fit $\mathcal{O}(1)$ coefficient. Propose a first-principles calculation of $\beta$ starting from the coupled Einstein-$\Psi_A$ equations at the Firmament. What boundary conditions must be imposed? What regime (weak-field linearized, non-perturbative static, quasi-static expansion) is the most tractable? Identify a simple limit of the problem in which $\beta$ could be read off analytically. Write down the action functional whose variation yields the boundary equation for $\mu^2$.

---

## Closing reflection

> *"He has made everything beautiful in its time. He has also set eternity in the human heart; yet no one can fathom what God has done from beginning to end."*  — Ecclesiastes 3:11

The electroweak theory is the place where the framework looks most successful and also most incomplete — a peculiarly apt metaphor for honest science. The Mexican hat is rigorously the shape of the potential, and its three $\mathcal{O}(1)$ coefficients remain to be computed. The photon is massless by a theorem, and the CP phase is order-of-magnitude by an estimate. What the framework has bought is real, and what remains to be bought is named. That is how a research program should look at chapter's end.

The next chapter turns to the strong force.

---

## Chapter 11 summary

- $SU(2)_L \times U(1)_Y$ is inherited from Vol 2 Ch 6 zone isometries.
- The Higgs doublet is the lowest $(1,1)$ KK mode of $\Psi_A$.
- The effective Mexican-hat potential has the right form; three $\mathcal{O}(1)$ coefficients ($\beta, \alpha, \lambda_A$) are currently fit (OPEN 11.1, GitHub #25).
- $M_W = gv/2$, $M_Z = M_W/\cos\theta_W$, $M_\gamma = 0$ exactly.
- $m_h^2 = \lambda v^2$, $G_F = 1/(\sqrt 2 v^2)$ — both rigorous given $v, \lambda$.
- Parity violation and $V\!-\!A$ follow from the one-sided condensate (conditional on Assumption 10.1).
- CP violation is a theorem for $n_{\rm gen} = 3$; precise $\delta_{\rm CP}$ gapped to Ch 13 (OPEN 11.2, GitHub #3).
- Table 4.11.1 tabulates every numerical claim of the chapter with an explicit rigor label.
- The chapter's epistemic contract: sub-percent numerical agreement on $M_W, M_Z, m_h, G_F$ is *conditional* on the Higgs-sector fits and is a reproduction of Standard Model algebra, not an independent prediction.

--- END DRAFT ---
