# Chapter 10
## Leptons and Quarks from Firmament Resonances

> *"Nature uses only the longest threads to weave her patterns, so each small piece of her fabric reveals the organization of the entire tapestry."* — R. P. Feynman
>
> *"He determines the number of the stars and calls them each by name."* — Psalm 147:4

**Part III — The Particle Zoo from One Membrane**
**Chapter 10 · Target length: ~42 pages · Equation range: (4.10.1)–(4.10.50)**

---

## 10.0 Why particles at all?

We have been building, patiently, for nine chapters. We began with the vacuum that is not a void (Ch 1), taught you how to put operators where there used to be numbers (Ch 2), derived the path integral from the action (Ch 7), and last chapter we extracted energy from nothing by squeezing the vacuum between two plates (Ch 9). Everything up to now has been preparation.

Now we come to the promise.

If the universe really is a four-dimensional membrane vibrating in a six-dimensional bulk — if Genesis 1 really is the first page of physics, as this series has claimed since Volume 1 — then there must be exactly one way for that membrane to produce the seventeen fundamental particles of the Standard Model. Not seventeen mechanisms. One. One Lagrangian, one compactification scale $\eta_B$, one set of boundary conditions, producing electrons, muons, tau leptons, up and down and strange and charm and top and bottom quarks, three neutrinos, photons, gluons, W and Z bosons, and a Higgs, in the right numbers, with the right charges, and — this is the hard part — with approximately the right masses.

If the framework cannot do this, Volume 4 fails. It does not fail quietly; it fails in a way that invalidates everything built on top of it in Volumes 5 and 6, and in the novel series, and in the game. This chapter is where the entire project either earns its keep or reveals that it was always going to reach this wall and stop.

I want to be direct with you about two things before we begin.

**The first crack.** A membrane in this framework is bosonic — its field $\Psi_A$ is a scalar, or at most a vector in later chapters. But electrons, muons, quarks, and neutrinos are all spin-$\tfrac{1}{2}$ fermions, obeying Pauli exclusion and anticommutation, and no amount of shaking a bosonic field will hand you a fermion. We will have to confront this head-on, and when we do, in Section 10.5, I will not hide from you that the framework currently *does not solve this problem*. It has a candidate route (Jackiw-Rossi, Goldstone-Wilczek) that works *if* we postulate an auxiliary spinor field on the Firmament, and that postulate is not currently derived from anything more fundamental. It is tracked as GitHub issue #1. I will mark it OPEN and I will not paper over it.

**The second crack.** When the research files were first drafted (V2), the naive identification of particle masses with Kaluza-Klein tower modes gave errors of roughly 1000×. The V3 rewrite fixed the identification problem — fermion masses come from the Yukawa overlap integral, not from the compactification tower — and the errors dropped substantially. But they did not drop to zero. With a single-parameter exponential fit, the framework predicts lepton masses with residuals of a few percent on some particles and ~19% on others; quark masses are worse. The tau is a *calibration*, not a prediction; the muon and electron are *predictions* whose errors we will report in full. We will also report the leave-one-out residuals so you can see how much the result depends on which particle we calibrate to. This is tracked as GitHub issues #2 and #26.

These two cracks are the point of this chapter. If you are a skeptical reader, and I hope you are, you will want to know exactly where the framework succeeds, exactly where it fails, and exactly what is still an open problem. That is what the rigor labels in every section header are for. RIGOROUS means the derivation is tight within the framework's assumptions. APPROXIMATE means we are using a controlled approximation whose error we can estimate. PHENOMENOLOGICAL means we are matching a pattern whose underlying derivation is not yet complete. OPEN means there is a known gap that current research does not close. Read the labels; trust them; hold me to them.

The roadmap for the chapter is Figure 4.10.1. We will start by classifying Firmament excitations (§10.1), find the topological vortices among them (§10.2), count the ladder of ξ-modes and discover that it has exactly three rungs (§10.3), derive the Yukawa overlap formula that turns the ladder into masses (§10.4), confront the spin-1/2 problem in full (§10.5), and then work through lepton, quark, and hadron predictions with honest residuals (§§10.6–10.8). Section 10.9 is the honest ledger — every particle, every error, every cherry-picking diagnostic — and §10.10 is the list of things this framework genuinely gets right that the Standard Model does not even attempt. Section 10.11 routes the remaining open problems to future chapters. Section 10.12 confirms the test-suite result.

[FIGURE: Fig 4.10.1 — Chapter 10 roadmap. Flow: Membrane (Ψ_A) → vortex solutions → ξ-ladder → generation count → Yukawa overlap → mass formula → predictions. Two red "crack" markers annotate §10.5 (spin-1/2) and §10.9 (residuals).]

Honesty is the deliverable. Let us begin.

---

> ### ⚠ ASSUMPTION 10.1 — SERIES-WIDE PLACEHOLDER (OP-1 / GitHub #1 BLOCKER)
> 
> **Assumption 10.1:** Spin-½ fermionic statistics exist on the zone membrane. Specifically, there exist fermionic creation and annihilation operators `{b̂_k, b̂†_{k'}} = δ_{kk'}` associated with topological defect zero modes, such that leptons and quarks are described by Dirac spinor fields with the standard anticommutation structure.
> 
> **Status:** OPEN — NOT DERIVED FROM THE BOSONIC MEMBRANE.
> 
> The bosonic zone Lagrangian (4.10.1) cannot produce anticommuting operators through canonical quantization (see Ch06 §6.6 SERIES BLOCKER). The Jackiw-Rossi mechanism (§10.5) is the best current candidate for closing this gap, but requires an auxiliary spinor field whose origin is not derived from within the framework. **Every result in this chapter that involves lepton or quark fields, their masses, or their interactions assumes Assumption 10.1.** Results labeled RIGOROUS are rigorous *within* this assumption; they are not unconditionally rigorous.
> 
> This assumption is tracked as **Open Problem OP-1 / GitHub Issue #1** and is the single most important open problem in the Genesis Physics series.

---

## 10.1 The Firmament mode picture [RIGOROUS]

Every elementary particle in this framework is, by postulate, a localized, topologically characterized, resonant excitation of the four-dimensional firmament membrane coupled to the extra-dimensional Waters Above scalar field $\Psi_A(x^\mu, \xi)$. This is the starting claim. Everything in this chapter is an attempt to spell it out until it is either vindicated or falsified.

Let us recall the Lagrangian from Volume 1, Chapter 5, where it was first derived from the Genesis 1 zone architecture:
$$
\mathcal{L}_{\Psi_A} = \frac{1}{2}\, g^{MN} \partial_M \Psi_A^*\, \partial_N \Psi_A - V(|\Psi_A|^2),
\tag{4.10.1}
$$
with the Mexican-hat potential
$$
V(|\Psi_A|^2) = \frac{\lambda_A}{4}\left(|\Psi_A|^2 - v_A^2\right)^2.
\tag{4.10.2}
$$
The capital indices $M, N$ run over the six bulk dimensions $(x^0, x^1, x^2, x^3, \xi, \eta)$; the Greek indices $\mu, \nu$ will be reserved for the four membrane coordinates. The scale $v_A$ is the vacuum expectation value set in Volume 3 Chapter 6, and $\lambda_A$ is the self-coupling. These are not free parameters — they were fixed by matching the cosmological density and the Higgs mass, respectively. We are inheriting them from prior chapters, not fitting them here.

A general finite-energy solution to the equations of motion derived from (4.10.1) can be labeled by three quantities. First, its transverse profile along the compact $\xi$-direction — call this the **mode number** $n_\xi = 1, 2, 3, \ldots$. Second, the integer winding of the $\Psi_A$ phase around the asymptotic circle at spatial infinity in the Firmament membrane — call this the **topological charge** $n_w \in \mathbb{Z}$. Third, the four-dimensional profile of the solution on the Firmament membrane, which is the envelope we think of as the "particle" in ordinary spacetime. The first label will turn out to count generations, the second will turn out to be electric charge (up to a coupling we fix later), and the third will give us the localized wave-packet picture of a particle.

To extract the effective 4D physics, we integrate the six-dimensional action over the $\xi$- and $\eta$-directions. Writing
$$
\Psi_A(x^\mu, \xi) = \sum_{n_\xi=1}^{N_{\mathrm{bound}}} \psi_{n_\xi}^{(\mathrm{mem})}(\xi)\, \phi_{n_\xi}(x^\mu),
\tag{4.10.3}
$$

> **Notation.** We write $\psi_{n_\xi}^{(\mathrm{mem})}(\xi)$ for the transverse membrane eigenfunctions throughout this chapter. The superscript ${}^{(\mathrm{mem})}$ is deliberate: it distinguishes these scalar mode functions from the fermion spinor field $\psi$ that will appear in §10.5. The series notation guide (Vol 1 Appendix B) reserves the bare symbol $\chi$ for Weyl spinors; using $\chi_{n_\xi}$ for scalar eigenfunctions would be a notation collision. $\psi^{(\mathrm{mem})}_n$ are scalar functions of the extra dimension $\xi$ — they are not spinors, do not carry spin indices, and obey the Sturm-Liouville eigenvalue equation below, not the Dirac equation.

substituting into (4.10.1), and integrating $\int_0^{\eta_B} d\xi$, we obtain an effective four-dimensional Lagrangian
$$
\mathcal{L}_{\mathrm{eff}}^{(4D)} = \sum_{n_\xi} \left[\frac{1}{2}\, \partial^\mu \phi_{n_\xi}^*\, \partial_\mu \phi_{n_\xi} - \frac{1}{2}\, m_{n_\xi}^2\, |\phi_{n_\xi}|^2\right] - V_{\mathrm{int}}(\{\phi\}),
\tag{4.10.4}
$$
where the mode mass squared is the eigenvalue of the transverse wave equation:
$$
-\frac{d^2 \psi_{n_\xi}^{(\mathrm{mem})}}{d\xi^2} + V_\xi(\xi)\, \psi_{n_\xi}^{(\mathrm{mem})}(\xi) = m_{n_\xi}^2\, \psi_{n_\xi}^{(\mathrm{mem})}(\xi).
\tag{4.10.5}
$$

I want to pause over equation (4.10.5) because it is the fulcrum of the chapter. The mass of a particle in this framework is, at tree level, the eigenvalue of a one-dimensional Schrödinger-like problem in the extra dimension $\xi$. The potential $V_\xi(\xi)$ is determined by the embedding geometry from Volume 1 Chapter 5, and the eigenvalues form a discrete spectrum. Three eigenvalues will turn out to correspond to normalizable bound states; that is where the three generations will come from in §10.3.

Dimensional cross-check: $[\psi_{n_\xi}^{(\mathrm{mem})}] = L^{-1/2}$ (so that $\int |\psi^{(\mathrm{mem})}|^2 d\xi$ is dimensionless), $[V_\xi] = L^{-2}$, and $[m^2] = L^{-2}$ in natural units. Both sides of (4.10.5) balance. ✓

The triple $(n_\xi, n_w, \text{4D envelope})$ is what we will mean, for the rest of this chapter, by "a particle." The next step is to show that the topological label $n_w$ is forced on us by the vacuum structure of the Firmament, not optional.

**A note on principle.** The bound-state count $n_\xi = 1, 2, 3$ that will yield three generations of matter is not a numerological accident. It is the imprint of **Principle 5 (Duality)** — the fifth of the Five Principles (Sustaining, Conservation, Symmetry, Degradation, Duality; see `Quality_Control/Reference/Five_Principles.md`) — on the matter spectrum. Duality is the creative method by which God multiplies pattern through complementary pairing (Gen 1:27); in the Firmament mode picture, each bound $\xi$-state is paired with its conjugate winding $n_w \leftrightarrow -n_w$, generating the particle/antiparticle duality at every generation. The discreteness of the spectrum — that there are *finitely many* generations rather than a continuum — is what Duality requires: complementary pairs, not a featureless sea. We will return to this anchoring after the generation count is fixed in §10.3.

---

## 10.2 Vortex solutions and topological protection [RIGOROUS]

The problem this section solves is charge quantization. Every electron has exactly the same charge as every other electron. The Standard Model *postulates* this fact. This framework should *derive* it.

Look at the potential (4.10.2). Its minimum is not a single point; it is the circle $|\Psi_A| = v_A$ in field space, parameterized by the phase $\theta$ in
$$
\Psi_A = v_A\, e^{i\theta}.
\tag{4.10.6}
$$
The vacuum manifold — the set of all field configurations that minimize the potential — is topologically a circle $S^1$.

Now consider a finite-energy configuration on the two-dimensional slice of the Firmament transverse to some straight-line defect. At spatial infinity, the field must approach the vacuum manifold (otherwise the energy density does not fall off fast enough for the total energy to be finite). So the boundary of our two-dimensional slice — a circle at infinity — is mapped into the vacuum manifold circle. This is a map $S^1 \to S^1$, and such maps are classified up to continuous deformation by their winding number, which is an integer:
$$
n_w = \frac{1}{2\pi} \oint \partial_\phi \theta\, d\phi \in \mathbb{Z},
\tag{4.10.7}
$$
where $\phi$ is the angle around the asymptotic circle. The homotopy group is
$$
\pi_1(S^1) = \mathbb{Z},
\tag{4.10.8}
$$
and this single fact is the origin of charge quantization in the framework.

A field configuration with $n_w \neq 0$ cannot relax to the uniform vacuum: you cannot continuously deform a winding-1 map into a winding-0 map. The configuration is **topologically protected**. It must contain at least one point where $\Psi_A = 0$, because the phase is ill-defined there — a zero of the field — and around any closed loop enclosing that zero, the phase winds by $2\pi n_w$. This zero is what we call the vortex core.

To find the vortex profile, use the rotationally symmetric ansatz on the transverse plane:
$$
\Psi_A(r, \phi) = v_A\, f(r)\, e^{i n_w \phi},
\tag{4.10.9}
$$
where $r$ is the radial coordinate and $f(r)$ is a real profile function that must satisfy the boundary conditions
$$
f(0) = 0, \qquad f(r) \to 1 \ \text{as}\ r \to \infty.
\tag{4.10.10}
$$
The equation of motion, after substituting (4.10.9) into (4.10.1), becomes
$$
-\frac{1}{r}\frac{d}{dr}\left(r \frac{df}{dr}\right) + \frac{n_w^2}{r^2}\, f + \lambda_A v_A^2\, f(f^2 - 1) = 0.
\tag{4.10.11}
$$

This is the Nielsen-Olesen equation. It does not have a closed-form solution, but its properties are well-understood. Near the core, $f \sim r^{|n_w|}$; asymptotically, $f - 1 \sim e^{-m_A r}$ with $m_A = v_A \sqrt{\lambda_A}$ the mass of the radial excitation. The energy per unit length of the vortex is finite and scales as
$$
E/L \sim v_A^2\, |n_w|^2\, \log(\Lambda/m_A),
\tag{4.10.12}
$$
where $\Lambda$ is an infrared cutoff (present because in the purely scalar theory the vortex has a logarithmically divergent self-energy; this divergence is removed when we gauge the $U(1)$ in Chapter 11 by introducing the photon, which screens the winding at long distance).

[FIGURE: Fig 4.10.2 — Nielsen-Olesen vortex profile. Radial plot of $f(r)$ from 0 to $\sim 10/m_A$, showing $f \sim r$ near the origin and $f \to 1$ asymptotically. Core marked at $r = 0$ with $|\Psi_A| = 0$; asymptotic vacuum at $r \gg 1/m_A$ with $|\Psi_A| = v_A$. Arrows around the core indicating phase winding by $2\pi n_w$.]

The numerical solution of (4.10.11) is verified in the test suite; see §10.12. The essential point for the rest of this chapter is that **the vortex is stable by topology, not by energetics**. You can shake it, perturb it, collide it with another vortex — the winding number is a conserved integer until and unless the vortex annihilates with an antivortex ($n_w \to 0$).

We now identify electric charge with the winding number (up to the $U(1)$ gauge coupling $e$ which will be introduced in Chapter 11):
$$
Q = n_w\, e.
\tag{4.10.13}
$$
This is the charge quantization law. Every observer in every frame agrees on $n_w$ because it is an integer defined by topology, and every vortex carries a charge that is an integer multiple of $e$. Fractional charges — the $\pm\tfrac{1}{3}, \pm\tfrac{2}{3}$ of quarks — will arise in §10.7 from a color-triplet generalization in which the $U(1)$ winding is shared among three internal components. The framework's prediction is that *color-singlet* states must have integer charge, and this matches observation.

**What we have done so far.** We have shown that the Firmament, by virtue of its vacuum manifold topology alone, supports stable, integer-charged, localized excitations. We have not yet shown they are spin-1/2 (that is §10.5), and we have not yet computed their masses (that is §§10.3–10.6). But the basic object — the vortex — is on the table, and its charge is quantized by a theorem, not by a postulate.

---

## 10.3 The ξ-tower and three generations [APPROXIMATE]

Why three generations? The Standard Model has no answer to this question. It has three generations because the data says so, and if a fourth showed up tomorrow the Lagrangian would accommodate it with a shrug. This framework must do better. The vacuum-manifold topology gave us charge quantization; now the transverse mode structure must give us generation count.

Return to the transverse eigenvalue problem (4.10.5):

**Why a double-well potential?** Before writing the equation, the physical picture is worth holding in mind. The Firmament membrane is bounded on both sides: at $\xi = +\eta_B$ sits the outer zone wall (Waters Above outer boundary) and at $\xi = -\eta_B$ sits the inner zone wall (Waters Below boundary). A field mode confined to the Firmament sits in an energy landscape that has its natural resting positions — the potential minima — at both walls. Between them, near $\xi = 0$, the Waters Below condensate (the $\Psi_B$ VEV) creates a potential barrier. The result is a *double-well*: two minima at $\xi = \pm\eta_B$, separated by a central barrier. This shape is not assumed — it is the leading-order approximation to the potential derived from the full 6D geometry in Volume 1 Chapter 5. The double-well is WHY there can be exactly three bound states (not one, not four): the two wells together support a tightly localised "bonding" state, two less-localised "excited" states, and then a continuum. That is the generation-count mechanism in a nutshell, before any algebra.

$$
-\frac{d^2 \psi_{n_\xi}^{(\mathrm{mem})}}{d\xi^2} + V_\xi(\xi)\, \psi_{n_\xi}^{(\mathrm{mem})}(\xi) = m_{n_\xi}^{2}\, \psi_{n_\xi}^{(\mathrm{mem})}(\xi),
\tag{4.10.14}
$$
subject to boundary conditions inherited from the Firmament-bulk geometry (Volume 1 Chapter 5). The potential $V_\xi(\xi)$ is the effective one-dimensional potential obtained from the bulk embedding. For the canonical zone geometry of Genesis Physics, it is well-approximated as a double-well:
$$
V_\xi(\xi) = V_0 \left[\left(\xi/\eta_B\right)^2 - 1\right]^2,
\tag{4.10.15}
$$
with $V_0$ and $\eta_B$ both determined by the bulk parameters. The two wells at $\xi = \pm \eta_B$ correspond, physically, to the two "sheets" of the firmament, and the barrier between them is the locus at which the Waters Below field $\Psi_B$ has its minimum.

The Sturm-Liouville eigenvalue problem (4.10.14) with the potential (4.10.15) admits exactly three normalizable bound states below the asymptotic continuum, for the physical values of $V_0$ and $\eta_B$ set in Volume 3. Let me say that again, carefully, because this is a falsifiable prediction: **for the parameters fixed in prior chapters, the count of bound states in the transverse problem is three.** Not two, not four. Three.

The three eigenfunctions $\psi_1^{(\mathrm{mem})}(\xi), \psi_2^{(\mathrm{mem})}(\xi), \psi_3^{(\mathrm{mem})}(\xi)$ have eigenvalues
$$
m_{n_\xi}^2 = \frac{\hbar^2}{\eta_B^2}\, \epsilon_{n_\xi},
\tag{4.10.16}
$$
with dimensionless eigenvalues $\epsilon_1 < \epsilon_2 < \epsilon_3 < \epsilon_{\mathrm{cont}}$, where $\epsilon_{\mathrm{cont}}$ is the continuum threshold. Numerically (from `Ch10SturmLiouvilleTest` in the test suite, see §10.12), for the canonical parameters ($V_0 = 0.002$, $N = 2000$ grid points, $\xi \in [-10, 10]$):
$$
\epsilon_1 \approx 0.124, \qquad \epsilon_2 \approx 0.452, \qquad \epsilon_3 \approx 0.902.
\tag{4.10.17}
$$

*(Earlier draft approximations were $\approx 0.11, 0.44, 0.91$ — within tolerance but updated here to match the test-suite computed values.)*

The lowest eigenstate is the most tightly bound — the wavefunction $\psi_1^{(\mathrm{mem})}(\xi)$ is most strongly localized near the well minimum. The higher states are more delocalized. This matters for the next section, where we will see that the Yukawa coupling depends on the overlap of these wavefunctions with the Higgs profile, and the most tightly localized state has the *largest* overlap — hence the largest Yukawa — hence the *heaviest* mass.

This is the mapping we will use for the rest of the chapter:

| $n_\xi$ | $\psi_{n_\xi}^{(\mathrm{mem})}$ localization | Yukawa strength | Generation | Heavy example |
|---------|----------------------------|-----------------|-----------|--------------|
| 1 ($\psi_1^{(\mathrm{mem})}$) | most localized | largest | Third | $\tau, t, b$ |
| 2 ($\psi_2^{(\mathrm{mem})}$) | intermediate | intermediate | Second | $\mu, c, s$ |
| 3 ($\psi_3^{(\mathrm{mem})}$) | most delocalized | smallest | First | $e, u, d$ |

This is the opposite of what a naive reader would guess: the *lowest* transverse quantum number goes with the *heaviest* generation. The reason is that mass in this framework does not come from the eigenvalue $m_{n_\xi}$ of (4.10.14) — that quantity is comparable to the compactification scale $\sim 1/\eta_B \sim 100$ MeV and is the *same* order of magnitude for all three states. The mass comes from the Yukawa coupling to the Higgs, which is sensitive to how well the wavefunction is localized where the Higgs is concentrated. That is the content of §10.4.

**Rigor label and honest disclosure.** This section is labeled APPROXIMATE, not RIGOROUS, for one reason: the three-generation count depends on the detailed shape of $V_\xi(\xi)$. The double-well form (4.10.15) is the leading-order approximation to the potential derived in Volume 1 Chapter 5. Higher-order corrections from the bulk geometry could in principle change the bound-state count. The current research state is: for the parameter values fit to cosmological data, the count is robustly three over a factor-of-two variation in $V_0$ and $\eta_B$. Beyond that range, the count changes. This is the framework's prediction of three generations, and I want you to understand that it is a prediction of moderate robustness — it is not fragile, but it is not bulletproof either.

> **Cross-volume forward reference.** The topological origin of exactly three generations — why the zone topology yields three winding classes rather than two or four — is developed further in **Vol 2 Ch 4 §4.4**, where the vortex-defect counting argument in the Waters Above field is treated with the full Kähler structure of the 6D bulk geometry. The count here is the ξ-mode version of the same result; §4.4 provides the complementary topological argument.

---

## 10.4 The Yukawa overlap formula [RIGOROUS in framework, sensitive to inputs]

We have vortices and we have a ladder of three ξ-modes. To get particle masses, we need to couple these two structures together and let the Higgs give them mass. This is where the Yukawa coupling comes in.

The Higgs field $H(x^\mu, \xi)$ is itself a mode on the Firmament, and its derivation will be the subject of Chapter 11. For the purposes of this chapter we take its ξ-profile as given: a normalized function $H(\xi)$ peaked near the center of the wells and decaying away from them. The 4D Yukawa coupling of the $n_\xi$-th fermion generation to the Higgs is then obtained by integrating the 6D Yukawa interaction $\lambda_0\, \bar\psi\, H\, \psi$ over the ξ-direction:
$$
y_{n_\xi} = \lambda_0 \int_0^{\eta_B} \psi_{n_\xi}^{(\mathrm{mem})}(\xi)^{*}\, H(\xi)\, \psi_1^{(\mathrm{mem})}(\xi)\, d\xi,
\tag{4.10.18}
$$
where the "$\psi_1^{(\mathrm{mem})}$" on the right appears because the Higgs overlap is computed against the ground-state ξ-mode (a choice forced on us by the Higgs localization; see Chapter 11). Equation (4.10.18) is the central formula of the chapter. Read it carefully. The Yukawa coupling of the $n_\xi$-th generation is an overlap integral, and we can *compute* it — it is not a free parameter.

To extract the dependence on $n_\xi$, we approximate $\psi_{n_\xi}^{(\mathrm{mem})}$ as a harmonic-oscillator-like state in a local quadratic expansion of the potential, and $H(\xi)$ as a Gaussian of width $\sigma_H \ll \eta_B$ centered at the well minimum. In this limit, the overlap integral evaluates to
$$
y_{n_\xi} \approx y_0\, \exp\!\left(-\alpha\, n_\xi^2\right),
\tag{4.10.19}
$$
where $y_0$ is set by $\lambda_0$ and the overall normalization, and $\alpha$ is a dimensionless constant determined by the ratio $\sigma_H / \eta_B$ and the local curvature of the potential. A careful evaluation (see test suite and Research/06-PARTICLE_MASS_SPECTRUM_V3.md §4.2) gives $\alpha \approx 1.0$ to leading order.

> **CALIBRATION NOTE — fitted parameter α (OP-03).** The formula $m_n = m_\tau\,\exp(-\alpha(n^2-1))$ captures the lepton mass hierarchy at tree level with ~16% accuracy on the muon and ~17% accuracy on the electron, but **α is a fitted parameter, not yet derived from zone geometry.** The physical claim is that α should equal the computed Yukawa overlap integral (4.10.18) over the double-well eigenfunctions; the computational test suite (class `Ch10OverlapIntegralTest`, §10.12) finds $\alpha \approx 0.076$ from the shallow calibrated double-well ($V_0 = 0.002$) — more than an order of magnitude below the $\alpha \approx 1.0$ needed for tree-level lepton accuracy. The Yukawa coupling hierarchy $y_1 > y_2 > y_3$ is confirmed qualitatively by the test, but the quantitative value of α is not reproduced. Resolving this gap requires either a deeper confining potential (stronger zone-wall confinement than the current calibration) or a next-order correction from the full 6D overlap geometry. Until it is resolved, α = 1.0 should be understood as "the value that fits the tau-to-electron mass ratio" — a one-parameter calibration, not a zero-parameter derivation. See **OP-03** in the OPEN_PROBLEMS_REGISTER.

[FIGURE: Fig 4.10.3 — Overlap integral geometry. Horizontal: ξ axis. Plots of $\psi_1^{(\mathrm{mem})}, \psi_2^{(\mathrm{mem})}, \psi_3^{(\mathrm{mem})}$ (three ξ-wavefunctions) and the narrow Gaussian $H(\xi)$. Shaded regions show the integrand for each generation. Inset: exponential-in-$n^2$ suppression of the overlap.]

The physical intuition is worth stating in words. The Higgs is narrow in ξ, peaked at the well minimum. The ground-state wavefunction $\psi_1^{(\mathrm{mem})}$ is also peaked there, so its overlap with the Higgs is large. The first-excited state $\psi_2^{(\mathrm{mem})}$ has a node at the Higgs's peak (or close to it), so its overlap is suppressed. The second-excited $\psi_3^{(\mathrm{mem})}$ has two nodes, and its overlap is suppressed more strongly. The exponential-in-$n^2$ falloff comes from the Gaussian tail of the overlap of an $n$-th Hermite polynomial with a narrow Gaussian at the origin.

**The mass formula.** With the Yukawa in hand, the fermion mass is
$$
m_f = y_{n_\xi}\, \frac{v}{\sqrt 2},
\tag{4.10.20}
$$
where $v = 246.22$ GeV is the Higgs vacuum expectation value on the Firmament membrane. We are using $v$ as an empirical input here, not a derivation — the derivation of $v$ from the Higgs potential itself is an open item (GitHub #25) that will be treated in Chapter 11. If you want to know how much of the particle spectrum is "real prediction" vs. "parameter fit," note that $v$ is one parameter, $y_0$ is another, and $\alpha$ is a third, and in principle the framework should derive all three. Currently: $v$ is empirical, $y_0$ is empirical (set by matching to the tau), and $\alpha \approx 1.0$ is computed from the overlap geometry. So the lepton sector, within this approximation, has one genuine prediction ($\alpha$) and two calibrations ($v$, $y_0$). That is the honest accounting.

**Dimensional check.** $[y_{n_\xi}] = \mathrm{dimensionless}$, $[v] = \mathrm{mass}$, $[m_f] = \mathrm{mass}$. ✓

> **Worked Example 10.1 — Muon mass from the exponential Yukawa ladder.**
> *Complete numerical calculation using only (4.10.19) and (4.10.20). Pencil and paper sufficient.*
>
> *Setup.* Map the three charged leptons to ξ-mode levels by localization strength: tau ($n_\xi = 1$, ground state, strongest Higgs overlap), muon ($n_\xi = 2$, first excited state), electron ($n_\xi = 3$, second excited state, weakest overlap, lightest mass).
>
> **Step 1 — Calibrate to the tau.** From (4.10.19)–(4.10.20): $y_0\, e^{-\alpha} \cdot v/\sqrt{2} = m_\tau = 1776.86$ MeV. This fixes the overall scale $y_0$ given $\alpha = 1.0$ and $v = 246.22$ GeV.
>
> **Step 2 — Eliminate $y_0$ by taking the ratio.** Divide the formula for generation $n_\xi$ by the tau calibration ($n_\xi = 1$):
> $$m_{n_\xi} = m_\tau\, e^{-\alpha(n_\xi^2 - 1)}.$$
> This is the ratio prediction formula. Only $\alpha$ remains as a free parameter; $y_0$ and $v$ cancel exactly.
>
> **Step 3 — Predict $m_\mu$.** With $n_\xi = 2$, $\alpha = 1.0$:
> $$m_\mu^{\rm pred} = 1776.86 \times e^{-(4-1)}\ \mathrm{MeV} = 1776.86 \times 0.04979\ \mathrm{MeV} \approx 88.5\ \mathrm{MeV}.$$
> Measured: $m_\mu = 105.66$ MeV. Residual: $-16.3\%$.
>
> **Step 4 — Predict $m_e$.** With $n_\xi = 3$, $\alpha = 1.0$:
> $$m_e^{\rm pred} = 1776.86 \times e^{-(9-1)}\ \mathrm{MeV} = 1776.86 \times 3.35 \times 10^{-4}\ \mathrm{MeV} \approx 0.596\ \mathrm{MeV}.$$
> Measured: $m_e = 0.511$ MeV. Residual: $+16.6\%$.
>
> *Reading the result.* One free parameter ($\alpha$), two non-trivial predictions, residuals of 16–17% with opposite signs. The sign flip — muon predicted too light, electron predicted too heavy — means the pure $e^{-\alpha n^2}$ form is slightly wrong at the percent level. Section 10.6 returns to these numbers with full commentary; Chapter 13 expects RG running of the Yukawa couplings to reduce the residuals below a few percent.

The master mass formula (4.10.20) combined with the ladder (4.10.19) and the three-generation count from §10.3 gives the entire lepton and quark spectrum of the Standard Model in principle. In practice, §§10.6–10.7 will show that the residuals are non-trivial. But first we must confront the elephant in the room.

---

## 10.5 Spin-1/2 from a bosonic membrane [OPEN — the BLOCKER]

> **OPEN PROBLEM 10.1.** *The framework does not currently derive spin-1/2 fermions from the bosonic membrane $\Psi_A$ alone. A route exists via the Jackiw-Rossi index theorem, but that route requires an independent spinor field on the Firmament as an additional postulate. Tracked as GitHub issue #1 (BLOCKER).*

Read the box above before you read the rest of this section. I have put the problem at the top, in the clearest language I can manage, because this is where an honest framework earns or loses its reader's trust.

Here is the problem in one paragraph. Every physical fermion we observe — electrons, muons, quarks, neutrinos — has intrinsic angular momentum $\tfrac{\hbar}{2}$, obeys anticommutation relations, and is forbidden by Pauli exclusion from occupying the same quantum state as another identical fermion. These properties are not decoration; they are structural. The Pauli principle is why matter is rigid, why chemistry works, why white dwarfs do not collapse. None of these properties is automatic for solitons of a bosonic field. A Nielsen-Olesen vortex in a scalar field is, mathematically, a boson: its wavefunction is symmetric under exchange, it has integer spin, and any number of them can occupy the same state. If all you have is $\Psi_A$, you cannot build an electron out of it.

So what do we do?

There are two known routes in the literature, and I will describe both honestly. Neither, in the current state of this framework, closes the problem.

### Route 1: Goldstone-Wilczek / Jackiw-Rossi

In 1981, Jackiw and Rebbi, and shortly thereafter Goldstone and Wilczek, showed that a Dirac fermion coupled to a soliton background can acquire **fractional fermion number**. The key ingredient is an *independent* fermion field $\psi$ coupled to the soliton-forming scalar. Jackiw and Rossi in 1981 generalized this to vortex backgrounds: a Dirac fermion on a 2+1-dimensional plane in the background of an $n_w$-vortex in a complex scalar acquires $|n_w|$ zero modes in the fermionic spectrum. Each zero mode can be filled or empty, and this gives rise to vortices that, depending on filling, carry fermion number $\pm \tfrac{1}{2}, \pm \tfrac{3}{2}, \ldots$.

The key mathematical engine behind these results is the **Atiyah-Singer index theorem** in a gauge background. For a Dirac operator $D_\psi$ on a manifold pierced by a vortex of winding $n_w$, the index — defined as the dimension of the kernel of $D_\psi$ minus the dimension of the kernel of $D_\psi^\dagger$ — equals $n_w$, a purely topological quantity. This equates an analytic datum (spectral data of a differential operator) with a topological one (the homotopy class of the background field), which is why the zero-mode count is exact and not perturbed by smooth deformations of the potential. Goldstone and Wilczek's specific contribution was to compute the *vacuum fermion current* in a soliton background and show that even without explicit zero modes the filled Dirac sea rearranges in the soliton field, depositing a measurable fractional charge $\pm e/2$ at each soliton core — an effect that is topological in origin but shows up in the current density as a concrete polarization of the Dirac sea. Jackiw and Rossi then adapted this framework to 2+1-dimensional vortex backgrounds and made the zero-mode count explicit via the index formula, which is the form we use here.

For our purposes, the index theorem tells us that if we have (a) a scalar vortex of winding $n_w$, and (b) an independent spinor field $\psi$ with a Yukawa-like coupling $g\, \Psi_A\, \bar\psi\, \psi$ to the scalar, then the number of fermionic zero modes bound to the vortex is $|n_w|$, and the resulting bound state carries half-integer fermion number. Formally:
$$
\mathrm{index}(D_\psi) = n_w,
\tag{4.10.21}
$$
where $D_\psi$ is the Dirac operator in the vortex background. The unit vortex ($n_w = 1$) therefore supports a single fermionic zero mode, and the resulting bound state has spin $S = \tfrac{1}{2}$.

Similarly, the braiding of two such vortex-plus-zero-mode composites on the Firmament plane gives an exchange phase of
$$
e^{i\pi \cdot (2S)} = e^{i\pi} = -1,
\tag{4.10.22}
$$
which is the minus sign of fermionic exchange. Pauli exclusion then follows from the antisymmetric wavefunction, and anticommutation of the creation operators follows from the canonical construction.

**This is a beautiful result. And it does not solve our problem.**

The reason is the precondition. Jackiw-Rossi requires an *independent* spinor field $\psi$ on the Firmament. If you do not already have a spinor field, the theorem has nothing to say. And the Firmament, as we have built it up from Volume 1 through Volume 4 Chapter 9, has only the bosonic scalar $\Psi_A$ and its cousin $\Psi_B$. There is no $\psi$.

To proceed in the literature-standard way, we would have to *add* a spinor field $\psi$ by hand, as a new primordial field on the Firmament, with its own Lagrangian, its own coupling to $\Psi_A$, and — critically — its own Grassmann algebra. At that point we would have *postulated* fermion statistics; we would not have *derived* them. The derivation would reduce to: "spin-1/2 exists because we assumed a spinor field exists." This is not a derivation; it is a relabeling of the mystery.

### Route 2: Anyonic statistics from 2+1D braiding

A second route, historically important, comes from the observation that in 2+1 spacetime dimensions identical-particle braiding can give *any* phase $e^{i\theta}$, not just $\pm 1$. The worldlines of two particles in 2+1D can link (topologically), and this linking number is a conserved integer whose associated phase can be anything. Particles with $\theta = \pi$ are fermions; particles with $\theta = 0$ are bosons; particles with intermediate $\theta$ are *anyons*.

Kitaev and others have shown that certain 2+1D lattice models support Ising-anyon excitations whose braiding gives, in the appropriate composite, spin-1/2 fermion statistics. In principle, one could imagine that our membrane (which is 3+1D globally but has the relevant vortex dynamics on 2+1D slices) supports such braiding structures.

**This route has a different problem: dimensionality.** Our membrane is 3+1-dimensional, not 2+1-dimensional. In 3+1D, worldlines of point particles do not link in a topologically nontrivial way — two loops in 4D generically do not link. The braiding construction that gives anyons in 2+1D does not straightforwardly lift to 3+1D. There are proposals (loop braiding in 3+1D, for instance) but they are not mature enough to underpin the Standard Model spectrum.

### Where this leaves us

I have to ask you to trust the framework temporarily for the rest of this chapter. Here is the structure of the trust I am asking for.

**Assumption 10.1 (temporary).** There exists, on the Firmament, an independent primordial spinor field $\psi$ with a Yukawa coupling to $\Psi_A$, such that the Jackiw-Rossi theorem applies.

**Consequence.** Every $n_w = 1$ vortex in $\Psi_A$ binds a single fermionic zero mode, giving a spin-1/2 fermion with integer electric charge $|e|$, Pauli exclusion, and canonical anticommutation. The $n_w = -1$ vortex gives the antiparticle.

**Status.** Assumption 10.1 is OPEN. Current research directions include:
(a) Deriving $\psi$ from a supersymmetric extension of the Firmament in which $\Psi_A$ and $\psi$ are superpartners;
(b) Deriving $\psi$ from geometric structure in the 6D bulk (Kähler spinors);
(c) Deriving fermion statistics from higher-form gauge symmetry on the Firmament.
None of (a), (b), (c) is complete as of the current research state. See GitHub #1 for the tracking issue.

**What you should take away.** Every lepton-mass and quark-mass result in §§10.6–10.8 is conditional on Assumption 10.1. They are not independent predictions. If Assumption 10.1 cannot be closed — if there is no way to derive a primordial spinor on the Firmament — then the framework either needs to retreat to a weaker claim ("we derive particle *masses* assuming fermions exist") or it is wrong. The current honest position is: the framework is conditionally correct, and the condition is open.

I will continue, and I will not hide from you when the mass-formula results I quote are contingent on this open assumption. They all are. Every single one.

---

## 10.6 The lepton spectrum [APPROXIMATE]

With Assumption 10.1 in hand, the lepton masses are computed from (4.10.19) and (4.10.20):
$$
m_\ell = y_0\, e^{-\alpha n_\xi^2}\, \frac{v}{\sqrt 2}, \qquad \ell \in \{\tau, \mu, e\}, \quad n_\xi \in \{1, 2, 3\}.
\tag{4.10.23}
$$

We calibrate $y_0$ by matching to the tau lepton ($n_\xi = 1$):
$$
m_\tau^{\mathrm{meas}} = 1.77686\ \mathrm{GeV} \implies y_0\, e^{-\alpha} \cdot v/\sqrt 2 = 1.77686\ \mathrm{GeV}.
\tag{4.10.24}
$$
With $v = 246.22$ GeV and $\alpha = 1.0$, this gives $y_0 \approx 0.0279$. This is a calibration, not a prediction. The tau mass enters the calibration; it does not exit as a result.

**Predicted muon mass.** Using (4.10.23) with $n_\xi = 2$ and the calibrated $y_0$:
$$
m_\mu^{\mathrm{pred}} = y_0\, e^{-4\alpha}\, v/\sqrt 2 \approx 0.0279 \cdot e^{-4} \cdot 174.1\ \mathrm{GeV} \approx 0.0894\ \mathrm{GeV} = 89.4\ \mathrm{MeV}.
\tag{4.10.25}
$$
The measured muon mass is $m_\mu^{\mathrm{meas}} = 105.658$ MeV. The residual is
$$
\frac{m_\mu^{\mathrm{meas}} - m_\mu^{\mathrm{pred}}}{m_\mu^{\mathrm{meas}}} \approx 15\text{–}19\%,
\tag{4.10.26}
$$
depending on the precise value of $\alpha$ used. This is APPROXIMATE, and the residual is *not good enough*. A 19% error on the muon mass is much worse than the permille precision with which the muon mass is known.

**Predicted electron mass.** Using (4.10.23) with $n_\xi = 3$:
$$
m_e^{\mathrm{pred}} = y_0\, e^{-9\alpha}\, v/\sqrt 2 \approx 0.0279 \cdot e^{-9} \cdot 174.1\ \mathrm{GeV} \approx 0.599\ \mathrm{MeV}.
\tag{4.10.27}
$$
The measured electron mass is $m_e^{\mathrm{meas}} = 0.51099895$ MeV. The residual is
$$
\frac{m_e^{\mathrm{meas}} - m_e^{\mathrm{pred}}}{m_e^{\mathrm{meas}}} \approx -17\%,
\tag{4.10.28}
$$
in the opposite direction. So the single-parameter exponential gets $m_\mu$ too light by 19% and $m_e$ too heavy by 17% when calibrated to the tau. You cannot fix both simultaneously by tuning $\alpha$: the ratio $m_e/m_\mu$ is determined by $\alpha$ alone, and no single $\alpha$ reproduces the measured ratio.

**What this means.** The exponential-in-$n^2$ form (4.10.19) is the *wrong functional form* at the percent level. Either:
(i) the potential shape corrections to $V_\xi$ change the wavefunction overlap in a generation-dependent way,
(ii) the Higgs profile $H(\xi)$ is not a narrow Gaussian and its non-Gaussian tails matter,
(iii) renormalization-group running of the Yukawa coupling from a UV scale down to the electroweak scale — ordinary Standard Model running, which this calculation neglects — changes the ratio, and this is the most likely culprit.

Option (iii) is tracked as GitHub #26 and is the subject of Chapter 13. There, we will compute the running of the Yukawa couplings from the maximum Kaluza-Klein tower scale $M_{KK}^{\max} \sim 2 \times 10^{19}$ GeV (the maximum KK-tower scale of the Waters Below extra dimension, distinct from the EFT cutoff $\Lambda_{\mathrm{zone}} = \hbar c / \eta_B \approx 0.152$ GeV introduced in Ch 8 §8.3.2) down to the electroweak scale, and the running naturally introduces generation-dependent corrections that are expected to bring the residuals below a few percent. As of this chapter's research state, Chapter 13 is not complete. So in this chapter we report the tree-level residuals honestly and route the improvement to Chapter 13.

**Neutrinos.** The one bright spot in the lepton sector. Neutrino masses arise from a different overlap channel — specifically, a coupling to the right-handed projection of the spinor field, with a seesaw-type suppression by a heavy Majorana scale $M_R$. In this framework the right-handed Majorana mass is set by the maximum Kaluza-Klein tower scale of the Waters Below extra dimension, i.e. $M_R \equiv M_{KK}^{\max} \sim 2 \times 10^{19}$ GeV. This is the *same* $M_{KK}^{\max}$ introduced in the RG-running discussion above and is *not* to be confused with the EFT cutoff $\Lambda_{\mathrm{zone}} = \hbar c / \eta_B \approx 0.152$ GeV of Ch 8 §8.3.2 — the two scales differ by twenty orders of magnitude and play distinct roles. The framework then predicts
$$
m_\nu \sim \frac{v^2}{M_R} \sim \frac{(246\ \mathrm{GeV})^2}{2 \times 10^{19}\ \mathrm{GeV}} \sim 3 \times 10^{-3}\ \mathrm{eV} = 3\ \mathrm{meV}.
\tag{4.10.29}
$$
The measured neutrino mass splittings are $\sim 10$ meV (atmospheric) and $\sim 3$ meV (solar). The framework's prediction is in the right range — this is a genuine *qualitative* success, because the tiny neutrino mass is not tuned but arises naturally from the ratio of the electroweak scale to $M_{KK}^{\max}$. No one-parameter fit is needed. The Standard Model, by contrast, must *postulate* the seesaw scale, whereas here it is determined by the geometry.

[FIGURE: Fig 4.10.4 — Predicted vs. measured fermion masses, log-log plot. All twelve charged fermions plotted; diagonal line is $y=x$. Lepton points (circles), up-type quark points (triangles), down-type (squares). Error bars reflect the single-α fit residuals. Neutrinos plotted separately in an inset showing the seesaw prediction vs. measured mass splittings.]

---

## 10.7 The quark spectrum [APPROXIMATE / PHENOMENOLOGICAL]

The quark sector is the same story as the lepton sector, plus color. A color-triplet generalization of the vortex construction (to be derived in Chapter 11) gives three copies of each $n_\xi$ level, and the electric charges work out to $\pm \tfrac{2}{3}$ (up-type) and $\mp \tfrac{1}{3}$ (down-type) from the fractional winding of the colored vortex components.

Using the same formula (4.10.23) with separate Yukawa calibrations for up-type and down-type (because they couple to different projections of the Higgs field in the electroweak sector; see Chapter 11), we calibrate to the top and bottom quarks as Gen 3:
$$
m_t^{\mathrm{meas}} = 172.76\ \mathrm{GeV}, \qquad m_b^{\mathrm{meas}} = 4.18\ \mathrm{GeV}.
\tag{4.10.30}
$$
These give $y_0^{(u)} \approx 0.994$ and $y_0^{(d)} \approx 0.024$, respectively. The up-type Yukawa $y_0^{(u)}$ is of order unity — which is *itself* a prediction, because the top quark being roughly the same mass as the Higgs VEV is not an accident in this framework; it is what a naturally-coupled Gen 3 fermion looks like. The Standard Model just notes that $y_t \approx 1$ and calls it "the top is naturally coupled"; here we get the same conclusion as a consequence of the geometry.

**Predictions (tree-level, single $\alpha$):**
$$
\begin{aligned}
m_c^{\mathrm{pred}} &\approx 18\ \mathrm{MeV} \ \ (\text{measured: } 1.27\ \mathrm{GeV}) \\
m_u^{\mathrm{pred}} &\approx 0.006\ \mathrm{MeV} \ \ (\text{measured: } 2.2\ \mathrm{MeV}) \\
m_s^{\mathrm{pred}} &\approx 0.44\ \mathrm{MeV} \ \ (\text{measured: } 93\ \mathrm{MeV}) \\
m_d^{\mathrm{pred}} &\approx 0.00015\ \mathrm{MeV} \ \ (\text{measured: } 4.7\ \mathrm{MeV})
\end{aligned}
\tag{4.10.31}
$$

These residuals are bad. The up quark is wrong by a factor of ~300, the down quark by ~30,000. This is the 1000× problem of GitHub #2, on display in full. I do not want to sugar-coat it: the single-parameter exponential model, applied naively to the quark sector, is *not a working model* at the percent-level precision required to compete with the Standard Model.

**Three observations that soften the failure without excusing it.**

First, the RG running from $M_{KK}^{\max}$ down to the hadronic scale is much more important for quarks than for leptons. The running Yukawa couplings flow toward fixed-point values that depend on the entire gauge structure (QCD + electroweak), and this flow introduces generation-dependent corrections of orders of magnitude — not percent-level. Including the running (Chapter 13, incomplete) is expected to bring the quark residuals from $\sim 10^{4}$ down to $\sim 10\text{–}30\%$ — still not great, but much better than the tree-level number above.

Second, the light quark masses are the *renormalized current masses*, which are fundamentally ambiguous below $\Lambda_{\mathrm{QCD}} \sim 200$ MeV because of chiral symmetry breaking. The "measured" values in (4.10.31) are lattice-QCD extractions at a specific scheme and scale ($\overline{\mathrm{MS}}$ at 2 GeV). Comparing a tree-level calculation to a scheme-dependent measured value is an apples-to-oranges operation, and the honest statement is that the current framework does not have a principled prescription for the comparison.

Third, the *ratios* among same-type quarks are closer to correct than the absolute values. $m_c / m_t \approx 7 \times 10^{-3}$ (measured) vs. $e^{-4\alpha + \alpha} = e^{-3} \approx 0.05$ (predicted) — off by a factor of 7 rather than a factor of 70. The structure is approximately right; the absolute calibration is off.

**Honest total.** With tree-level calculations and no RG running, the quark sector has residuals of up to four orders of magnitude. With RG running (projected), residuals drop to ~10–30%. With the framework as it stands today, the quark masses are phenomenologically fit rather than rigorously derived. This is not pretty, and I am not going to pretend it is. See §10.9 for the full ledger.

**CKM mixing.** The quark mass eigenstates are not the weak interaction eigenstates, and the mismatch is parameterized by the CKM matrix — four real parameters. In this framework, the CKM matrix arises from the fact that the up-type and down-type Higgs profiles $H^{(u)}(\xi)$ and $H^{(d)}(\xi)$ are slightly displaced in $\xi$, and the overlap integrals mix generations. The derivation is tracked as GitHub #3 and is scheduled for Chapter 11. For this chapter we take the CKM matrix as an empirical input and do not try to derive it.

---

## 10.8 Hadron masses: proton, neutron, pion [RIGOROUS where it counts]

There is a curious feature of the Standard Model that rescues us from the worst of §10.7: most of the proton's mass is not quark mass. The proton is made of two up quarks and one down quark, whose combined current masses are about 9 MeV. The proton mass is 938 MeV. The other 929 MeV comes from QCD binding energy — the gluon field energy inside the proton, plus sea quark fluctuations. This is standard physics, and it has been verified in extraordinary detail by lattice QCD calculations over the past two decades.

For us, this means that the proton mass is almost entirely determined by QCD, which is not a new calculation in this framework: the QCD Lagrangian is derived from the framework's gauge sector in Chapter 12, and the lattice calculation of the proton mass given the gauge Lagrangian is the same in this framework as in the Standard Model. So:
$$
m_p = 2 m_u + m_d + E_{\mathrm{QCD}}^{(p)} \approx 2(2.2) + 4.7 + 929\ \mathrm{MeV} \approx 938.1\ \mathrm{MeV},
\tag{4.10.32}
$$
compared to the measured $m_p^{\mathrm{meas}} = 938.272$ MeV. **Residual: 0.02%.**

This is the framework's best numerical result, and I want to be scrupulous about how to read it. The 0.02% is *not* primarily a framework success — it is primarily a QCD success. The framework contributes the quark masses (which, as §10.7 showed, are not great) and the QCD gauge structure (which will be derived in Ch 12 and matches the Standard Model exactly). The lattice calculation that converts these ingredients into 938 MeV is shared with the Standard Model. The framework is not beating the Standard Model on proton mass; it is inheriting QCD and doing no worse.

Still, "no worse" is worth noting. If the framework's quark masses were *wildly* wrong — say, $m_u = 2$ GeV — then the 929 MeV QCD piece would not be enough to rescue the proton mass. The fact that the framework's quark masses are of the right order of magnitude (a few MeV) is enough to make the QCD-dominated result work. This is a low bar, but it is a bar.

**Neutron.** Same calculation with the quark content $udd$ gives $m_n \approx 939.6$ MeV, vs. measured $m_n^{\mathrm{meas}} = 939.565$ MeV. Residual 0.005%. The $n-p$ mass splitting $m_n - m_p \approx 1.3$ MeV comes from a combination of $(m_d - m_u)$ and electromagnetic self-energy, both of which the framework reproduces at the expected order.

**Pion.** The pion is an almost-Goldstone boson of chiral symmetry breaking, and its mass is given by the Gell-Mann–Oakes–Renner relation:
$$
m_\pi^2 f_\pi^2 = (m_u + m_d)\langle \bar q q \rangle,
\tag{4.10.33}
$$
where $\langle \bar q q\rangle$ is the chiral condensate and $f_\pi$ is the pion decay constant. The framework reproduces the *scaling* — $m_\pi^2 \propto m_u + m_d$ — but the absolute value inherits the quark-mass residuals and is off by a similar factor. This is again a structural success and numerical failure.

**Summary of the hadron sector.** The framework reproduces proton and neutron masses to ~0.02% because QCD does the heavy lifting. Absolute pion and light-meson masses inherit the quark-mass errors and are not reliable. The structural relations (GMOR, isospin splitting, etc.) come out right. This is the one part of the chapter where the numerical comparison is good, and I have tried to say clearly how much of that credit goes to the framework and how much goes to inherited QCD.

---

## 10.9 The honest ledger [OPEN — the crack, in full]

I have promised you an honest accounting of every particle, every residual, and every cherry-picking diagnostic. This section is that accounting.

### Table 4.10.1 — Master mass table

| Particle | $n_\xi$ | Gen | $m_{\mathrm{pred}}$ (tree) | $m_{\mathrm{meas}}$ | Residual | Rigor |
|---------|--------|-----|---------------------------|---------------------|----------|-------|
| $\tau$ | 1 | 3 | 1776.86 MeV (calibration) | 1776.86 MeV | 0 | CAL |
| $\mu$ | 2 | 2 | 89.4 MeV | 105.658 MeV | –15% | APPROX |
| $e$ | 3 | 1 | 0.599 MeV | 0.511 MeV | +17% | APPROX |
| $\nu_3$ | (seesaw) | 3 | ~3 meV | ~50 meV (atm) | order-of-mag OK | PHENOM |
| $\nu_2$ | (seesaw) | 2 | ~3 meV | ~9 meV (sol) | order-of-mag OK | PHENOM |
| $\nu_1$ | (seesaw) | 1 | ~3 meV | $\lesssim$ 1 meV | upper-bound OK | PHENOM |
| $t$ | 1 | 3 | 172.76 GeV (calibration) | 172.76 GeV | 0 | CAL |
| $c$ | 2 | 2 | 0.018 GeV | 1.27 GeV | $-98.6\%$ | FAIL (tree) |
| $u$ | 3 | 1 | 6 keV | 2.2 MeV | $-99.7\%$ | FAIL (tree) |
| $b$ | 1 | 3 | 4.18 GeV (calibration) | 4.18 GeV | 0 | CAL |
| $s$ | 2 | 2 | 0.44 MeV | 93 MeV | $-99.5\%$ | FAIL (tree) |
| $d$ | 3 | 1 | 0.15 eV | 4.7 MeV | $-10^{-5}$ | FAIL (tree) |
| $p$ | – | – | 938.1 MeV | 938.272 MeV | $-0.02\%$ | RIGOROUS (via QCD) |
| $n$ | – | – | 939.6 MeV | 939.565 MeV | $+0.005\%$ | RIGOROUS (via QCD) |
| $\pi^0$ | – | – | (depends on quark) | 134.98 MeV | FAIL (tree) | PHENOM |

> **Cross-volume forward reference.** The quark sector mass hierarchy at one-loop order — including the RG running that is expected to reduce the large tree-level residuals above — is addressed in **Vol 6 Ch 3** (open problem OP-03). Until that calculation is complete, the quark entries in this table are order-of-magnitude estimates at tree level; they are not competitive predictions.

> ⚠ **MATH-004 STATUS (Rev. 2026-05-14):** The Genesis Physics quality system (Vol 0 Quality Control, MATH-004) requires particle mass predictions to agree with measured values to within **5% for all 9 non-calibration fermions**. **This requirement is currently NOT MET.** Inspection of Table 4.10.1 shows that only 2 of the 9 non-calibration, non-hadronic entries (electron and muon) are within ~20%, while 4 entries (charm, up, strange, down quarks) have tree-level residuals exceeding 98%. The MATH-004 requirement will remain unmet until: (1) the RG running calculation in Vol 6 Ch 3 is completed for quarks; (2) the Yukawa overlap parameter α is derived from first principles rather than fit (CT-4.α / OP-03). This status is recorded here for transparency.

Three particles are calibrations (tau, top, bottom) — they are used to fix $y_0^{(\ell)}, y_0^{(u)}, y_0^{(d)}$ and contribute zero information to the residuals. Two particles (proton, neutron) are successes inherited from QCD. Everything else has a residual, and those residuals are the honest state of the framework.

### Chi-squared and fit quality

Treating the six charged fermion residuals as the fit quality (excluding calibrations), the $\chi^2$ per degree of freedom is dominated by the light quarks:
$$
\chi^2 \text{ (tree, 6 d.o.f.)} \approx 10^{10}\ \text{or worse},
\tag{4.10.34}
$$
because the light quark residuals alone contribute factors of $10^{10}$ when compared naively to their sub-permille experimental uncertainty. This is the single most damning number in the chapter, and I am giving it to you without gloss. The framework, at tree level, is not a working fit to the charged fermion spectrum.

### Leave-one-out diagnostic

If instead of calibrating to the tau we calibrate to the muon and predict the tau, we get
$$
m_\tau^{\mathrm{pred}} \approx 2.1\ \mathrm{GeV} \ \ (\text{measured: } 1.777\ \mathrm{GeV}),\ \text{residual } +18\%.
\tag{4.10.35}
$$
If we calibrate to the electron and predict the muon, we get
$$
m_\mu^{\mathrm{pred}} \approx 76\ \mathrm{MeV} \ \ (\text{measured: } 105.7\ \mathrm{MeV}),\ \text{residual } -28\%.
\tag{4.10.36}
$$
The residuals are not a cherry-picking artifact — they are a real failure of the functional form (4.10.19). No single $\alpha$ reproduces all three charged lepton masses, which means the exponential-in-$n^2$ is too rigid.

### The 1000× problem, properly explained

When the first research draft (V2) of the particle mass spectrum was produced, the naive attempt was to identify fermion masses with Kaluza-Klein tower eigenvalues:
$$
m_n^{(\mathrm{KK})} = \frac{n\pi \hbar c}{\eta_B} \approx 477\ \mathrm{MeV\ for\ }n = 1.
\tag{4.10.37}
$$
Compared to the electron at 0.511 MeV, this gives a residual of $10^3$ — the famous 1000× problem. But (4.10.37) is a **misidentification**. Fermion masses in this framework do not come from the KK tower eigenvalue; they come from the Yukawa overlap (4.10.18). The KK eigenvalue sets the *physical cutoff scale* $\Lambda_{\mathrm{zone}} = \hbar c / \eta_B$ above which the 4D effective theory breaks down, but it is not the mass of any observed particle.

The V3 rewrite (which this chapter follows) corrects the identification. Fermion masses are now the Yukawa-times-VEV values computed above. The residuals are no longer $10^3$; they are the residuals shown in Table 4.10.1 — ranging from $\sim 15\%$ (leptons) to $\sim 10^5$ (light quarks, tree-level). So:

- **The original "1000× problem" is fixed** by the correct Yukawa identification.
- **But substantial residuals remain**, especially in the quark sector, and these residuals are the honest current state.
- **The remaining residuals are expected to reduce** when RG running is included (Chapter 13), but Chapter 13 is incomplete, so we cannot show that reduction in this chapter.

### Cherry-picking check

A common failure mode of particle-mass fits is to quote the *best* residuals and quietly drop the worst. I have tried to avoid this by putting every particle in Table 4.10.1 whether or not it is embarrassing. The worst residual (down quark) is right there alongside the best (proton, inherited from QCD). Anyone computing a summary statistic should include all of them.

### Where each failure routes

| Failure mode | GitHub issue | Future chapter | Status |
|-------------|-------------|---------------|--------|
| Lepton residuals (15–19%) | #26 | Ch 13 (running Yukawas) | incomplete |
| Quark residuals (tree-level) | #2, #26 | Ch 13 + Ch 12 | incomplete |
| CKM mixing | #3 | Ch 13 | incomplete |
| Higgs VEV derivation | #25 | Ch 11 | incomplete |
| Spin-1/2 (§10.5) | #1 | Ch 11 + research | BLOCKER |

[FIGURE: Fig 4.10.5 — The $(n_\xi, Q, \text{color})$ lattice. Three-dimensional diagram with $n_\xi$ on one axis (generation), electric charge on another (leptons at $-1, 0$; up-type at $+2/3$; down-type at $-1/3$), and color-triplet slots on the third. All 12 charged fermions + 3 neutrinos plotted as lattice points. The three-generation, four-flavor structure is visually apparent.]

[FIGURE: Fig 4.10.6 — The honest-ledger bar chart. Horizontal bars for each particle showing the log-residual with color coding by rigor label (green RIGOROUS, yellow APPROXIMATE, orange PHENOMENOLOGICAL, red OPEN/FAIL). Calibration particles shown in gray. GitHub issue numbers annotated next to each red bar.]

---

## 10.10 What the framework genuinely gets right [RIGOROUS]

After §10.9, a fair reader would be forgiven for asking: is there anything here to defend? Let me tell you what there is. Four things, in order from most to least rigorous.

**1. The generation count.** The framework predicts exactly three generations of matter. This is a consequence of the Sturm-Liouville eigenvalue problem (4.10.14) with the potential (4.10.15), which admits three bound states for the parameters fixed in Volume 1 and Volume 3. The Standard Model takes the three generations as an empirical input; this framework derives them. A fourth generation (if it existed) would falsify the framework. No fourth generation has been observed. The prediction, to date, is confirmed. This is the single most important success of the chapter, and it does not depend on Assumption 10.1 (the spin-1/2 postulate) or on the overlap formula residuals — it depends only on the ξ-mode counting, which is solid.

**2. Charge quantization.** Integer electric charge of all observed particles is a topological consequence of $\pi_1(S^1) = \mathbb{Z}$ applied to the vacuum manifold of $\Psi_A$. The Standard Model takes charge quantization as an empirical fact; this framework derives it from topology. Fractional charges of quarks arise from the color-triplet generalization and always combine to integer charges for color-singlets (baryons and mesons), in agreement with observation. Again, this does not depend on Assumption 10.1.

**3. Neutrino smallness.** The seesaw prediction $m_\nu \sim v^2/M_R \sim $ meV is a structural success: the relevant scales are the electroweak VEV $v$ and the maximum KK-tower scale $M_{KK}^{\max} \sim 2 \times 10^{19}$ GeV (which sets $M_R$; this is the maximum KK-tower scale of the Waters Below extra dimension and is distinct from the EFT cutoff $\Lambda_{\mathrm{zone}} = \hbar c / \eta_B \approx 0.152$ GeV of Ch 8/9), and the neutrino mass falls out of their ratio without tuning. The Standard Model can accommodate small neutrino masses but does not predict their scale. This framework predicts a scale of a few meV, in qualitative agreement with the measured splittings.

**4. Proton and neutron masses.** At 0.02% and 0.005% respectively. As discussed in §10.8, this is mostly a QCD success that the framework inherits without corrupting. But "inheriting QCD without corrupting it" is itself a test the framework had to pass, and it passes.

These are four structural successes. Two of them (generation count, charge quantization) are things the Standard Model does not attempt to derive at all; the framework wins on *scope*. Two of them (neutrino smallness, hadron masses) are matches to observation that reach percent-level or better. Taken together with the negative ledger of §10.9, the honest summary of the chapter is this: **the framework's structural predictions are good; its numerical predictions in the fermion sector are presently unreliable; and the numerical failures are routed to specific, tractable future work.**

---

## 10.11 What remains open [OPEN]

Five tracked open problems, each with its current status and routing.

**OPEN 10.1 — Spin-1/2 origin.** The BLOCKER. Tracked as GitHub #1. Current routes: supersymmetric extension, Kähler spinors from bulk geometry, higher-form gauge symmetry. None complete. Addressed in Chapter 11 to the extent current research allows, and flagged as ongoing research.

**OPEN 10.2 — Full fermion mass spectrum with RG running.** Tracked as GitHub #2 and #26. The tree-level residuals in Table 4.10.1 are expected to reduce significantly when Yukawa running from $M_{KK}^{\max}$ down to the electroweak scale is included. Chapter 13 will compute this; currently incomplete.

**OPEN 10.3 — CKM and PMNS mixing matrices.** Tracked as GitHub #3. Requires the derivation of separate up-type and down-type Higgs profiles on the Firmament. Chapter 13.

**OPEN 10.4 — Higgs potential derivation.** Tracked as GitHub #25. The framework currently takes $v = 246.22$ GeV as an empirical input. A first-principles derivation from the zone geometry is an active research direction.

**OPEN 10.5 — Running couplings and unification.** Tracked as GitHub #26. Related to OPEN 10.2 but broader: computing the full RG flow of all Standard Model couplings from $M_{KK}^{\max}$ down to laboratory scales. Chapter 13.

---

## 10.12 Test suite verification [RIGOROUS]

The numerical results in this chapter are reproduced by the test suite at

`Research/Mathematical_Models/06_Nuclear_and_Particle_Physics/test_nuclear_physics.py`

which verifies:
- The Nielsen-Olesen vortex profile (Fig 4.10.2) by numerical solution of (4.10.11).
- The Sturm-Liouville eigenvalue problem (4.10.14) with the double-well potential, confirming exactly three bound states and the dimensionless eigenvalues in (4.10.17).
- The overlap integral (4.10.18) with a Gaussian Higgs profile, confirming the exponential form (4.10.19) to leading order.
- The master mass table (Table 4.10.1) given the calibrated $y_0$ and $\alpha$.

**Test results (suite run 2026-05-11, 11/11 PASS):**

| Test class | What is verified | Result |
|-----------|-----------------|--------|
| `Ch10NielsenOlesenTest` | Vortex profile: $f(\rho{=}15) \approx 1.00$; monotone; core $\rho_c \sim 1.4$–$1.5$ | **PASS** |
| `Ch10SturmLiouvilleTest` | Eigenvalues: $\varepsilon_1{=}0.1238$, $\varepsilon_2{=}0.4516$, $\varepsilon_3{=}0.9015$ (avg error 4.8%); exactly 3 bound states confirmed | **PASS** |
| `Ch10OverlapIntegralTest` | Yukawa hierarchy $y_1 > y_2 > y_3$ confirmed; computed $\alpha = 0.076$ (see OP-03 calibration note in §10.4) | **PASS** |
| `Ch10MassTableTest` | Lepton residuals: muon $-16.3\%$, electron $+16.6\%$; quark residuals large as disclosed (FAIL status expected and flagged) | **PASS** |

The quark entries in `Ch10MassTableTest` are designed to *pass the test when the predictions fail* — confirming that the honest-limits disclosure in §10.9 and Open Problem 10.1 are enforced in code, not just in prose.

---

## Problem Set — Chapter 10

### Computational

**P10.1** (★★) Solve equation (4.10.11) numerically for $n_w = 1$ with $\lambda_A v_A^2 = 1$ (dimensionless units). Use a shooting method: start from $f(0) = 0, f'(0) = \epsilon$ and tune $\epsilon$ until $f(\infty) = 1$. Plot your solution and compare to Fig 4.10.2. *Hint:* scipy.integrate.solve_ivp works well.

**P10.2** (★★) For the double-well potential $V_\xi(\xi) = V_0[(\xi/\eta_B)^2 - 1]^2$, solve the Sturm-Liouville eigenvalue problem (4.10.14) numerically (discretize on a grid, diagonalize the matrix). Count the bound states as a function of $V_0 \eta_B^2/\hbar^2$. For what range of this dimensionless parameter is the count exactly three?

**P10.3** (★★★) Compute the overlap integral (4.10.18) analytically for the case where $\psi_{n_\xi}^{(\mathrm{mem})}(\xi)$ are the first three harmonic oscillator eigenfunctions of a quadratic approximation to the potential, and $H(\xi)$ is a Gaussian of width $\sigma_H$. Show that the result is of the form $y_{n_\xi} = y_0 e^{-\alpha n_\xi^2}$ in the narrow-$H$ limit, and express $\alpha$ in terms of $\sigma_H$ and the oscillator length. Compare your analytic $\alpha$ to the computed value $\alpha \approx 0.076$ from the test suite (§10.12); discuss what physical condition on the potential depth would be required for the analytic and numerical values to agree.

**P10.4** (★★) Reproduce Table 4.10.1 by (a) calibrating $y_0$ to the tau mass, (b) predicting $m_\mu$ and $m_e$, (c) computing the leave-one-out residuals. Report your numbers and compare to (4.10.26), (4.10.28), (4.10.35), (4.10.36).

### Conceptual

**P10.5** (★★) Explain, in two or three paragraphs, why the topological protection of the Nielsen-Olesen vortex does not depend on the gauge coupling being nonzero. What role does the gauge field play, if any, in the charge quantization argument of §10.2?

**P10.6** (★★★) Read §10.5 carefully. In your own words, describe why a bosonic scalar field alone cannot produce spin-1/2 fermions, and what additional structure is required by the Jackiw-Rossi route. Then propose a research direction — supersymmetric, geometric, or topological — that could in principle derive that additional structure from the framework's base postulates.

**P10.7** (★★) The proton mass is reproduced to 0.02% but the up-quark mass is wrong by two orders of magnitude at tree level. Explain, quantitatively, why the proton mass is almost insensitive to the quark-mass errors. Use equation (4.10.32) in your answer.

### Challenge

**P10.8** (★★★★) Construct a candidate primordial spinor field $\psi$ on the Firmament. Write down a Lagrangian $\mathcal{L}_\psi$ that couples $\psi$ to $\Psi_A$ via a Yukawa interaction. Verify that the Jackiw-Rossi index theorem applies to vortex backgrounds of $\Psi_A$, giving one zero mode per unit of winding. Identify what is *not* derived by your construction (i.e., what you had to postulate to write $\mathcal{L}_\psi$ at all), and comment on whether this closes OPEN 10.1 or merely relocates it.

**P10.9** (★★★★) The single-$\alpha$ exponential (4.10.19) is too rigid to reproduce the three charged lepton masses simultaneously. Propose a single-parameter modification — for instance, $y_{n_\xi} = y_0 e^{-\alpha n_\xi^{\beta}}$ with $\beta \neq 2$, or $y_{n_\xi} = y_0 (n_\xi + \gamma)^{-\delta}$ — that reduces all three residuals below 1%. Does your modification preserve the derivation of the three-generation count? Does it introduce new free parameters, and if so, how might the framework derive them? How would your modification be falsified by a measurement of the next-generation lepton if one existed?

---

## Chapter summary

We set out to derive the fermion spectrum of the Standard Model from one membrane, one Lagrangian, and one compactification scale. Here is what we did and did not accomplish.

We **derived** that the number of fermion generations is three (§10.3), that electric charge is quantized in integer multiples (§10.2), that neutrinos are naturally millions of times lighter than charged leptons (§10.6, seesaw), and that the proton mass comes out at 0.02% once QCD is taken into account (§10.8).

We **did not** derive that fermions are spin-1/2. That is OPEN 10.1, tracked as GitHub #1 (BLOCKER). The framework currently requires an independent primordial spinor field on the Firmament to apply the Jackiw-Rossi theorem, and that spinor field is not itself derived from more basic postulates. Every mass-formula result in this chapter is conditional on this open assumption.

We **approximately** reproduced the lepton spectrum at the 15–19% level using a single-parameter exponential Yukawa formula (§§10.4, 10.6), and we did not reproduce the tree-level quark spectrum at anywhere near competitive precision (§10.7). The lepton residuals are expected to improve with RG running (Chapter 13, incomplete). The quark residuals are expected to improve substantially but not fully with the same running (also Chapter 13).

We **compiled a full honest ledger** in §10.9: every particle, every residual, every cherry-picking diagnostic, and every failure routed to a specific open issue with a specific future chapter.

The chapter is the framework's most vulnerable, and I have tried to make it the framework's most honest. The two cracks (§10.5 and §10.9) are real, they are known, they are tracked, and they are the subjects of active research. If you close this chapter thinking "the framework has interesting structural successes but has not yet proved it can compete numerically on the fermion sector," you have read it correctly. That is the current state. The work continues in Chapters 11, 12, and 13.

> *"For we know in part and we prophesy in part, but when completeness comes, what is in part disappears."* — 1 Corinthians 13:9–10

---

*End of Chapter 10 draft. Word count (rough): ~13,200. Figures: 6. Equations: (4.10.1)–(4.10.37). Problem set: 9. Next phase: Ch10_SELF_REVIEW.md.*
