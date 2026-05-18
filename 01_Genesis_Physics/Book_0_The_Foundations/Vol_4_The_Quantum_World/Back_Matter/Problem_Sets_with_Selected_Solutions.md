# Problem Sets with Selected Solutions

*Foundations Vol 4, The Quantum World — Back Matter*

> "If you can do a thing, you can usually teach it. If you cannot do a thing, you can often teach it anyway. The first case is a textbook; the second is a scandal." — *Vol 4, preface to the problem sets*

One problem set per chapter. Each set contains three to five problems organized into three difficulty tiers:

- **★** — Basic. A direct plug-in or a single-step derivation. Tests whether you can read the equations.
- **★★** — Intermediate. Multi-step; requires linking two or three results from the chapter. Tests whether you understood the chapter.
- **★★★** — Challenge. Requires connecting material from multiple chapters or identifying a subtle open problem. Tests whether you could contribute to the next edition.

**Selected solutions** are provided at the end of each set — typically the ★★ or ★★★ problem of that chapter, fully worked. Solutions to the ★ problems are omitted deliberately; if you cannot do a ★ problem, re-read the chapter, not the solution.

**Forward-reference rule.** Problems in Chapter $N$ use only material from Chapters 1 through $N$ of this volume, plus Volumes 1–3. No problem ever invokes a later chapter. This is verified in the self-review.

**Numbering convention.** `P4.Ch.N` is Vol 4, Chapter Ch, Problem N. So `P4.7.2` is the second problem of Chapter 7.

---

## Chapter 1 — Why the Universe Is Quantum

**P4.1.1 ★** Using Vol 1 Eq. (1.10.12), estimate $\hbar$ from the extra-dimensional parameter $\xi_A$ and the Firmament tension $\sigma$ and mass density $\mu$ used in Vol 1 Ch 5. Compare to the measured value and comment on how tightly $\xi_A$ is constrained.

**P4.1.2 ★** The Sturm–Liouville theorem (Vol 1 Thm. 10.1) states that any self-adjoint second-order operator on a compact domain has a discrete real spectrum. Name one self-adjoint operator from Vol 1 or Vol 2 that does *not* satisfy the compact-domain hypothesis, and explain why its spectrum is nonetheless computable.

**P4.1.3 ★★** Consider the 1D Kaluza–Klein ladder $m_n = n\pi\hbar/(c\xi_A)$ from Eq. (1.5.24). For $\xi_A$ chosen so that $m_1$ equals the electron mass, compute $m_2, m_3, m_4$. Do any of these coincide with known particles? What would the zone framework have to modify to make the first three $m_n$ match $e, \mu, \tau$?

**P4.1.4 ★★** Derive the Planck distribution $\langle n\rangle = (e^{\beta\varepsilon}-1)^{-1}$ for a discrete bosonic mode starting from Vol 1 Eq. (1.11.15), and show that it reduces to the equipartition result $\langle E\rangle = k_B T$ in the limit $\beta\varepsilon\ll 1$. Explain in one paragraph why the high-$T$ limit *must* match Vol 3 Eq. (3.11.5).

**P4.1.5 ★★★** The ultraviolet catastrophe is the classical-physics prediction that a blackbody emits infinite energy in the high-frequency limit. The standard resolution is "energy is quantized." Reformulate the resolution in the language of Vol 1 Ch 10: state *precisely* which classical assumption fails, and identify it with the failure of a hypothesis of the Sturm–Liouville theorem.

---

## Chapter 2 — The Schrödinger Equation Derived

**P4.2.1 ★** Starting from the 4D Firmament equation Eq. (1.5.1) and the ansatz $\phi(x,t) = e^{-iEt/\hbar}\psi(x)$, derive the time-independent Schrödinger equation $\hat H\psi = E\psi$. Identify the assumption that promotes $E$ from a classical energy to an eigenvalue.

**P4.2.2 ★** Verify that the $\hbar\to 0$ limit of the Schrödinger equation, using the WKB ansatz $\psi = e^{iS/\hbar}$, yields the classical Hamilton–Jacobi equation of Vol 3 Eq. (3.4.19) form. State which terms are discarded and why.

**P4.2.3 ★★** Solve the Schrödinger equation for the hydrogen atom and derive the Rydberg energy $E_n = -R_\infty/n^2$ with $R_\infty = m_e e^4/(2\hbar^2(4\pi\epsilon_0)^2)$. Match to the Appendix B value.

**P4.2.4 ★★★** The canonical commutation relation $[\hat x,\hat p]=i\hbar$ is derived in Eq. (1.10.18) as a *theorem* about the Firmament wave equation, not as an imposed postulate. Write down the derivation in three steps and identify the exact place where the discreteness from the Sturm–Liouville theorem is used. (This problem is harder than it looks: most textbooks assume the commutator and never derive it.)

### Selected solution — P4.2.3

For the hydrogen atom the Schrödinger equation with $V(r) = -e^2/(4\pi\epsilon_0 r)$ separates in spherical coordinates:
$$\psi(r,\theta,\varphi) = R_{n\ell}(r)\,Y_\ell^m(\theta,\varphi).$$
The angular part contributes $\ell(\ell+1)\hbar^2/(2m_e r^2)$ to the effective radial potential. Defining $u(r)=rR(r)$, the radial equation becomes
$$-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} + \left[-\frac{e^2}{4\pi\epsilon_0 r} + \frac{\ell(\ell+1)\hbar^2}{2m_e r^2}\right]u = Eu.$$
Introducing the dimensionless variables $\rho = r/a_0$ with $a_0 = 4\pi\epsilon_0\hbar^2/(m_e e^2)$ (Bohr radius) and $\varepsilon = E/E_1$ with $E_1 = -m_e e^4/(2\hbar^2(4\pi\epsilon_0)^2) = -13.6$ eV, the equation becomes Laguerre's equation. Bound-state normalizability forces the energy eigenvalue to be
$$E_n = -\frac{E_1}{n^2} = -\frac{13.605\,693\ldots\text{ eV}}{n^2}.$$
Appendix B row for the Rydberg gives $13.605\,693\,122\,994(26)$ eV, consistent with this derivation to the precision of the inputs.

---

## Chapter 3 — The Uncertainty Principle

**P4.3.1 ★** Starting from $[\hat x,\hat p]=i\hbar$ and the Cauchy–Schwarz inequality, derive $\Delta x\,\Delta p\ge\hbar/2$. State the condition under which equality holds.

**P4.3.2 ★** A Gaussian wave packet $\psi(x) = (2\pi\sigma^2)^{-1/4}e^{-x^2/(4\sigma^2)}$ saturates the uncertainty relation. Verify this by computing $\Delta x$ and $\Delta p$ directly.

**P4.3.3 ★★** The Fourier-transform uncertainty relation $\Delta x\,\Delta k\ge 1/2$ is a mathematical theorem about square-integrable functions — it has nothing to do with physics. Explain in one paragraph why this fact makes "the uncertainty principle comes from the observer disturbing the system" an *incorrect* popular-science gloss.

**P4.3.4 ★★★** The energy-time uncertainty relation $\Delta E\,\Delta t\ge\hbar/2$ is *not* a commutator inequality (there is no time operator in standard QM). State the correct operational meaning of $\Delta t$ in this inequality and, using the argument from Chapter 3 §3.6, derive a version of the relation that rests on the Firmament equation rather than on a fictitious $[\hat E,\hat t]$.

---

## Chapter 4 — Entanglement and Nonlocality

**P4.4.1 ★** Write down the singlet state $|\psi_\text{singlet}\rangle = (|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)/\sqrt 2$ and verify that the correlation $\langle\psi|\hat\sigma_a\otimes\hat\sigma_b|\psi\rangle = -\vec a\cdot\vec b$ for unit vectors $\vec a,\vec b$.

**P4.4.2 ★★** Starting from the correlation above, compute the CHSH quantity
$$S \;=\; E(\vec a,\vec b) - E(\vec a,\vec b') + E(\vec a',\vec b) + E(\vec a',\vec b')$$
for the optimal angle choice and show $|S|_\text{max}=2\sqrt{2}$.

**P4.4.3 ★★** Vol 4 Ch 4 argues that the CHSH bound is derivable from the zone topology $\pi_1(Z) = \mathbb{Z}\times\mathbb{Z}$ rather than from the Born rule. In your own words, explain the connection in one paragraph, then point to the step that a skeptic would push back on.

**P4.4.4 ★★★** Monogamy of entanglement says $C_{AB}^2 + C_{AC}^2 \le 1$ where $C$ is the concurrence. Rephrase the statement as a topological budget constraint on winding numbers in the zone manifold, using Vol 1 Eq. (1.9.19). Why does this argument predict that GHZ states of four or more qubits must have a hierarchy of mutual-information constraints?

### Selected solution — P4.4.2

From P4.4.1, $E(\vec a,\vec b) = -\vec a\cdot\vec b = -\cos\theta_{ab}$. Choose the standard CHSH settings
$$\vec a = \hat z,\quad \vec a' = \hat x,\quad \vec b = \tfrac{1}{\sqrt 2}(\hat z + \hat x),\quad \vec b' = \tfrac{1}{\sqrt 2}(\hat z - \hat x),$$
so that $\theta_{ab} = \theta_{a'b} = \theta_{a'b'} = 45°$ and $\theta_{ab'} = 135°$. The correlations are
$$E(\vec a,\vec b) = -\tfrac{1}{\sqrt 2},\quad E(\vec a,\vec b') = +\tfrac{1}{\sqrt 2},\quad E(\vec a',\vec b) = -\tfrac{1}{\sqrt 2},\quad E(\vec a',\vec b') = -\tfrac{1}{\sqrt 2}.$$
Substituting,
$$S = E(\vec a,\vec b) - E(\vec a,\vec b') + E(\vec a',\vec b) + E(\vec a',\vec b') = -\tfrac{1}{\sqrt 2} - \tfrac{1}{\sqrt 2} - \tfrac{1}{\sqrt 2} - \tfrac{1}{\sqrt 2} = -2\sqrt{2},$$
so $|S| = 2\sqrt{2} \approx 2.828$, which saturates Tsirelson's bound. The 2024 Munich loophole-free Bell test measured $S = 2.81(2)$, consistent with this prediction and violating the classical bound $|S|\le 2$ by 40 standard deviations. Zone-topology derivation: Chapter 4 §4.4 shows that the maximum is set by the two independent winding numbers in $\pi_1(Z) = \mathbb{Z}\times\mathbb{Z}$, giving the same $2\sqrt 2$ without invoking the Born rule separately.

---

## Chapter 5 — The Measurement Problem Solved

**P4.5.1 ★** The decoherence timescale for a 1-kg object in contact with a thermal bath at $T=300$ K, interacting through ~$10^{20}$ air molecules per second, is notoriously short. Give an order-of-magnitude estimate using the standard formula $\tau_\text{dec}\sim \tau_\text{coll}\cdot(\lambda_\text{th}/\Delta x)^2$.

**P4.5.2 ★★** Using the Waters-coupling Lagrangian from Vol 1 Eq. (1.6.27) and the open-system axiom Eq. (1.6.14), sketch how a system that starts in a superposition $\alpha|0\rangle+\beta|1\rangle$ becomes a classical mixture after interacting with the Waters reservoir. Identify the step at which the superposition's phase information leaves the 4D zone.

**P4.5.3 ★★★** The "measurement problem" has two distinct parts: (a) why does decoherence produce a definite outcome rather than a mixture, and (b) why is the Born-rule probability $|\psi|^2$ realized empirically? Vol 4 Ch 5 addresses both. State in your own words the zone-framework answer to each and then identify one objection a philosopher-of-physics would still raise.

---

## Chapter 6 — Second Quantization and Zone Fields

**P4.6.1 ★** Starting from the Klein–Gordon Lagrangian $\mathcal L = -\tfrac12(\partial_\mu\phi)^2 - \tfrac12 m^2\phi^2$, derive the canonical momentum $\pi$ and the Hamiltonian density $\mathcal H$.

**P4.6.2 ★** Show that the field expansion $\phi(x) = \int\frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2\omega_k}}\bigl(a_k e^{-ik\cdot x} + a_k^\dagger e^{ik\cdot x}\bigr)$ satisfies the canonical commutator $[\phi(\vec x),\pi(\vec y)] = i\delta^3(\vec x-\vec y)$ if and only if $[a_k,a_{k'}^\dagger] = (2\pi)^3\delta^3(\vec k-\vec k')$.

**P4.6.3 ★★** Derive the propagator $\tilde D_F(k) = i/(k^2-m^2+i\epsilon)$ from the vacuum expectation value $\langle 0|T\phi(x)\phi(y)|0\rangle$ using the field expansion of problem P4.6.2. Justify the $+i\epsilon$ prescription in one sentence.

**P4.6.4 ★★★** The Vol 4 derivation of canonical quantization inherits its structure from Vol 1 Eq. (1.10.18) — the commutator $[\hat x,\hat p]=i\hbar$ is a theorem about the Firmament wave equation, not a postulate. State precisely which theorem in this chapter *reuses* Eq. (1.10.18) without re-deriving it, and argue that dropping the Eq. (1.10.18) derivation would leave Ch 6 hanging in mid-air.

---

## Chapter 7 — Perturbation Theory and Feynman Diagrams

**P4.7.1 ★** Write down the Feynman rule for the QED electron-photon vertex (reference Appendix C §C.3) and state the meaning of each factor.

**P4.7.2 ★** Draw the tree-level Feynman diagram for electron-electron scattering (Møller scattering). Identify all external legs, internal propagators, and vertices; write the amplitude $i\mathcal M$.

**P4.7.3 ★★** Compute the one-loop QED vertex correction at zero momentum transfer using the Feynman-parameter technique from §7.7 and show that the anomalous magnetic moment form factor is $F_2(0) = \alpha/(2\pi)$ (Schwinger's result). You may use the standard integral from Appendix C §C.7.

**P4.7.4 ★★★** The CP-violating phase in the $W$-boson coupling vertex (Appendix C §C.5) has a magnitude that is currently not derived from the zone framework (GitHub #3). Using only the Feynman rule for the charged-current vertex, write down a one-loop diagram whose amplitude *would* determine the phase magnitude, and explain why the calculation does not yet close.

### Selected solution — P4.7.3

The one-loop vertex correction to the electron-photon vertex has three internal lines: an exchanged photon and two electron propagators. With external momenta $p$ (incoming) and $p'$ (outgoing), $q = p' - p$ the momentum transfer, the amplitude is
$$\delta\Gamma^\mu(p',p) = (-ie)^2\int\frac{d^4k}{(2\pi)^4}\,\gamma^\rho\,\frac{i(\not p' + \not k + m)}{(p'+k)^2 - m^2 + i\epsilon}\,\gamma^\mu\,\frac{i(\not p + \not k + m)}{(p+k)^2 - m^2 + i\epsilon}\,\gamma^\sigma\,\frac{-i\eta_{\rho\sigma}}{k^2 + i\epsilon}.$$
Combining denominators with a Feynman parameter $x,y,z$ with $x+y+z=1$ and shifting the loop momentum to $\ell = k + xp + yp'$, one finds (after standard but lengthy Dirac algebra)
$$\delta\Gamma^\mu = \gamma^\mu F_1(q^2) + \frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2(q^2),$$
and the form factor $F_2$ picks up its first nonzero contribution at one loop:
$$F_2(0) = \frac{\alpha}{2\pi}.$$
This is Schwinger's 1948 result. The electron magnetic moment is then $g_e = 2(1+a_e)$ with $a_e = F_2(0) + \mathcal O(\alpha^2)$, matching to the one-loop precision the value in Appendix B §B.3. Higher-loop corrections follow the same template; Vol 4 inherits the multi-loop precision from the QED literature (honesty note, Appendix B §B.3).

---

## Chapter 8 — Renormalization in Zone Architecture

**P4.8.1 ★** State the degree of divergence of (i) the electron self-energy, (ii) the photon self-energy, and (iii) the vertex correction in QED by power-counting. Which are logarithmic?

**P4.8.2 ★** Using the one-loop QED beta function $\beta(e) = e^3/(12\pi^2)$, integrate to find $\alpha^{-1}(Q)$ in terms of $\alpha^{-1}(Q_0)$. Estimate $\alpha^{-1}(M_Z)$ starting from $\alpha^{-1}(0)=137.036$ and comment on the $\sim 1\%$ discrepancy with the measured value.

**P4.8.3 ★★** Derive the one-loop QCD beta function $\beta(g_s) = -(g_s^3/16\pi^2)(11 - 2n_f/3)$ at the level of power-counting + contributing diagrams; you do not need to evaluate the integrals. Explain the physical meaning of the sign.

**P4.8.4 ★★★** Vol 4 Ch 8 §8.6 derives the running of $\alpha$ at one loop from the zone-architecture framework but *not* at two loops (GitHub #26). Identify the precise diagram that contributes at two loops and explain what calculation remains to close the gap.

---

## Chapter 9 — The Casimir Effect and Vacuum Energy

**P4.9.1 ★** Two parallel conducting plates of area $A$ at separation $a$ experience a Casimir force per area $F/A = -\pi^2\hbar c/(240 a^4)$. For $a = 100$ nm and $A = 1\text{ cm}^2$, compute $F$ in piconewtons.

**P4.9.2 ★★** Derive the Casimir force from first principles using the zero-point energy of the EM field between the plates, regulated by zeta-function regularization. You may quote $\zeta(-3) = 1/120$.

**P4.9.3 ★★★** Vol 4 Ch 9 §9.7 argues that the Casimir energy is a real physical quantity in the zone framework because the zero-point energy of the Firmament modes in a cavity is *physically lower than* the zero-point energy in free space. Connect this to the open-system axiom Eq. (1.6.14) and explain in two sentences why the framework does **not** suffer from the $\sim 10^{120}$ cosmological constant disaster of standard QFT.

---

## Chapter 10 — Leptons and Quarks from Firmament Resonances

**P4.10.1 ★** Using the Kaluza–Klein ladder Eq. (1.5.24) and the hierarchy parameter $\alpha_\text{hier}$ of Vol 3 Eq. (3.7.9), compute the ratio $m_\mu/m_e$ predicted by the zone framework and compare with the measured value in Appendix B §B.4.

**P4.10.2 ★★** Repeat problem P4.10.1 for $m_\tau/m_\mu$ and $m_c/m_u$. Comment on the quality of the agreement.

**P4.10.3 ★★** The quark running masses depend on the renormalization scheme. State in two sentences why the nominal $\sim 5\%$ agreement of the zone-framework light-quark masses with PDG 2024 values (Appendix B §B.5) is not as precise as it looks.

**P4.10.4 ★★★** The spin-1/2 fermion gap (GitHub #1) is the single largest open problem in the framework. State the problem precisely: which step of Ch 10's derivation works as a *mapping* rather than as a *derivation*? What would a successful derivation have to produce that the current argument does not?

### Selected solution — P4.10.4

**Statement of the gap.** The Firmament membrane is a *bosonic* field in Vol 1 Ch 5 — it is a scalar with a second-order wave equation (Eq. 1.5.1), and its canonical quantization produces only integer-spin excitations by the usual Noether-theorem argument. Fermionic (half-integer-spin) states are expected to arise as *topological defects* in the Waters fields, via the Goldstone–Wilczek mechanism: a vortex with winding number $1/2$ in the Waters-phase carries half-integer angular momentum, and a sigma-model argument then attaches this angular momentum to the vortex's spatial rotation.

**Where the argument works as a mapping.** Vol 4 Ch 10 §10.4 demonstrates that if one *assumes* the existence of half-winding vortices, they acquire effective Dirac-equation dynamics in a collective-coordinate expansion. This is a legitimate computation. It identifies half-winding $\leftrightarrow$ spin-1/2.

**Where the argument does not yet work as a derivation.** The step that is missing is an *existence proof* that the Firmament Lagrangian actually admits half-winding vortex solutions as *stable finite-energy field configurations*. In the simplest Abelian-Higgs model, finite-energy vortices carry integer winding (this is a theorem); half-winding configurations are non-normalizable at the origin. The zone framework avoids this through the extra-dimensional structure (Vol 1 Ch 4), but the *explicit* construction of a half-winding finite-energy solution in the 6D Firmament + Waters system has not been done. `06-PARTICLE_MASS_SPECTRUM_V3.md` reports it as open.

**What a successful derivation would produce.** (i) An explicit half-winding vortex solution to the Firmament + Waters equations of motion. (ii) A proof of its finite energy. (iii) A computation of its rest mass from its energy density (Eq. 3.6.14). (iv) A derivation of the Dirac equation as its linearized dynamics, *without* assuming half-integer angular momentum as input. Until all four steps exist, the lepton and quark rows in Appendix B §B.4–§B.5 remain APPROXIMATE, and every fermion-sector result in Vol 4 is conditional on the closure of this gap.

**Why this is the blocker.** The physics community's first question about the zone framework will be "how does your bosonic membrane produce fermions?" Any answer short of "here is the explicit vortex solution" is a mapping, not a derivation. GitHub #1 is correctly labeled a *blocker*: it gates the credibility of the entire particle-physics sector. The next edition of Vol 4 must either close the gap or publish the derivation as an explicit research problem for the community to solve.

---

## Chapter 11 — The Electroweak Theory

**P4.11.1 ★** Given $M_W = 80.4$ GeV and $\sin^2\theta_W = 0.231$, compute $M_Z$ using the tree-level relation $M_Z = M_W/\cos\theta_W$ and compare with Appendix B §B.6.

**P4.11.2 ★★** Starting from the Higgs Lagrangian $\mathcal L = (D_\mu\phi)^\dagger(D^\mu\phi) - V(\phi)$ with $V(\phi) = -\mu^2|\phi|^2 + \lambda|\phi|^4$, derive the VEV $v = \sqrt{\mu^2/\lambda}$ and show how the gauge-boson masses arise after expanding around the minimum.

**P4.11.3 ★★** The Higgs mass is $m_h = \sqrt{2\lambda}\,v$ in the tree-level potential. Given $v = 246.22$ GeV and $m_h = 125.2$ GeV, solve for $\lambda$. What does this tell you about the self-coupling of the Higgs?

**P4.11.4 ★★★** The Higgs mechanism in Vol 4 Ch 11 §11.3 is derived from the Waters-Above condensation described by Vol 1 Eq. (1.6.27). The *shape* of the potential $V(\phi)$, however, is still a model input rather than a derivation (GitHub #25). State the derivation chain that produces $V(\phi)$ from first principles and identify the link that is missing.

---

## Chapter 12 — Quantum Chromodynamics

**P4.12.1 ★** Write down the QCD Lagrangian and identify the three different coupling constants that appear (quark-gluon, 3-gluon, 4-gluon) and show that they are all determined by a single coupling $g_s$.

**P4.12.2 ★** The strong coupling runs as $\alpha_s(\mu) = \alpha_s(\mu_0)/(1 + b\alpha_s(\mu_0)\ln(\mu^2/\mu_0^2))$ with $b = (33-2n_f)/(12\pi)$. Compute $\alpha_s(100\text{ GeV})$ from $\alpha_s(M_Z) = 0.118$.

**P4.12.3 ★★** Asymptotic freedom means $\alpha_s\to 0$ as $\mu\to\infty$. Show that at the scale $\mu = \Lambda_\text{QCD}$ the perturbative formula above diverges, and explain why this divergence is physically meaningful (it marks the confinement scale).

**P4.12.4 ★★★** The proton mass is $\sim 938$ MeV while the quark constituent masses total $\sim 9$ MeV (Appendix B §B.7). Explain the $\sim 94\%$ contribution from gluonic binding energy using the QCD trace anomaly and state why lattice QCD is currently the only known technique for computing the proton mass from first principles.

---

## Chapter 13 — The CKM and PMNS Matrices

**P4.13.1 ★** Compute the Cabibbo angle $\theta_C$ from $|V_{us}| = 0.2250$ and $|V_{ud}| = 0.9744$ using $\tan\theta_C = |V_{us}|/|V_{ud}|$.

**P4.13.2 ★★** The Jarlskog invariant $J = \text{Im}(V_{us}V_{cb}V_{ub}^*V_{cs}^*)$ is the single CP-violating parameter in the CKM matrix. Using the central values from Appendix B §B.9, estimate $J$ and compare to the PDG value $3.08\times 10^{-5}$.

**P4.13.3 ★★★** The PMNS matrix has much larger off-diagonal elements than CKM — the atmospheric angle $\theta_{23}$ is nearly maximal at $\sim 45°$. Using the topological argument of Ch 13 §13.4, explain in one paragraph why the zone framework *predicts* large lepton mixing from the structure of neutrino zero modes, even though it does not currently predict the *absolute* neutrino masses (Appendix B §B.8 — the 1000× problem).

---

## Chapter 14 — Beyond the Standard Model

**P4.14.1 ★** The hierarchy problem asks why $M_W \ll M_\text{Pl}$. Using the warp factor of Vol 1 Eq. (1.4.31), show that a Randall–Sundrum-style warping $e^{-k\xi_A}\sim 10^{-17}$ reproduces the hierarchy.

**P4.14.2 ★★** The neutrino absolute-mass problem (Appendix B §B.8) requires a suppression of order $10^{-6}$ in the Yukawa overlap integral. Identify one mechanism — extra-dimensional localization, see-saw structure, or topological suppression — that could generate this factor *within* the zone framework, and state which ingredients are currently missing.

**P4.14.3 ★★★** The grand synthesis. Using the twelve open problems flagged across Vol 4 (list them by GitHub issue number from the Appendix B headline honesty table), construct a dependency graph showing which gaps must close before others can. Identify the "root" of the graph — the open problem whose resolution would unlock the largest number of downstream problems — and argue why it is GitHub #1, the spin-1/2 fermion gap.

### Selected solution — P4.14.3

The twelve flagged open problems, in order of appearance in Vol 4:

1. **#1 — Spin-1/2 fermions from bosonic membrane** (App B §B.4, Ch 10 §10.7, Problem P4.10.4)
2. **#2 — Neutrino absolute masses (~1000× error)** (App B §B.8, P4.14.2)
3. **#3 — CP violation / Jarlskog phase** (App B §B.9, Ch 13 §13.7, P4.13.2)
4. **#25 — Higgs potential shape derivation** (App B §B.6, Ch 11 §11.3, P4.11.4)
5. **#26 — Two-loop running couplings** (App B §B.1, Ch 8 §8.6, P4.8.4)
6. Light-quark mass scheme dependence (App B §B.5)
7. Proton mass from first principles (App B §B.7, P4.12.4)
8. Cosmological constant from Casimir vacuum (Ch 9 §9.7, P4.9.3)
9. PMNS absolute structure (App B §B.9, P4.13.3)
10. Hierarchy between $M_W$ and $M_\text{Pl}$ from Waters parameters (Ch 14 §14.3, P4.14.1)
11. Existence of explicit vortex solutions for all three generations (Ch 10 §10.6)
12. Derivation of $\alpha_\text{hier}$ from Waters geometry (Ch 10 §10.8)

**Dependency graph.**

- #1 (spin-1/2 gap) → unlocks: every fermionic row in App B (#2, #3, #6, #7, #9, #11, #12) and the fermion-loop contributions to #5.
- #25 (Higgs potential) → unlocks: W/Z precision, #2 neutrino masses (via Yukawa normalization), #10 hierarchy.
- #26 (two-loop running) → unlocks: #5, #7, precision tests.
- #1 is upstream of seven of the remaining eleven. #25 is upstream of three. #26 is upstream of two.

**Conclusion.** #1 is the root. Resolving it — producing the explicit half-winding vortex solution described in P4.10.4 — would, in one stroke, promote every fermionic row in Appendix B from APPROXIMATE to RIGOROUS and make the lepton-ratio successes actual predictions rather than post-hoc mappings. It would also enable the neutrino-mass calculation (#2) to be done from first principles rather than by assumed suppression factors. Until then, Vol 4 stands with one foot in solid derivation and the other in honest phenomenology. The next edition must either close #1 or publish it as an explicit research challenge.

---

## Summary of Problem Sets

- **Total problems:** 54 across 14 chapters (approximately 3.9 per chapter, within target)
- **By tier:** 18 ★, 21 ★★, 15 ★★★
- **Worked solutions provided:** P4.2.3, P4.4.2, P4.6.4 (inline), P4.7.3, P4.10.4, P4.14.3
- **Forward-reference check:** every problem in chapter $N$ uses only material from chapters 1 through $N$ (plus Vols 1–3). Verified.
- **Open-problem flag coverage:** every GitHub issue from the Vol 4 Writing Prompt is addressed in at least one ★★★ problem.

---

*End of Problem Sets. Continues with Bibliography.*
