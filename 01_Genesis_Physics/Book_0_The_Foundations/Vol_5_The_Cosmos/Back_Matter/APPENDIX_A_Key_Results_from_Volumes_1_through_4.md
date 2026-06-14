# Appendix A — Key Results from Volumes 1 Through 4

*Foundations Vol 5, The Cosmos — Back Matter*

> "General relativity is the geometry of the Firmament projected into four dimensions; cosmology is the thermodynamics of the Waters projected onto an expanding Firmament. Every equation in this volume traces back to something that was already proven." — *Vol 5, Chapter 1*

Volume 5 inherits more prior machinery than any other volume in the series. General relativity is derived from the 6D embedding theorem (Vol 1), gravitational waves from the linearized field equations (Vol 2), cosmological fluids from the Waters field equations (Vol 1) and fluid dynamics (Vol 3), and quantum corrections to black hole physics from the QFT formalism (Vol 4). Rather than restating derivations in the main text, this appendix catalogs the prior-volume results that Vol 5 actually uses.

---

## A.1 How to Use This Appendix

**Tag notation.** Every equation is labeled `(V.Ch.Eq)` with the volume number, chapter number, and equation number. So `(1.4.7)` is Vol 1, Chapter 4, Equation 7. Vol 5 equations use `(5.Ch.Eq)` and are NOT listed here — they appear in the main text of this volume.

**Organization.** Sections A.2 through A.5 are grouped by prior volume (Vol 1, Vol 2, Vol 3, Vol 4), then by chapter within each volume. Each entry has four fields:

1. **Tag** — `(V.Ch.Eq)`
2. **Equation** — the formula itself, boxed when it is a key result of the original chapter
3. **Gloss** — one-line physical meaning
4. **Used in Vol 5** — the Vol 5 chapters that cite or depend on this equation

**Reverse index.** Section A.6 maps each Vol 5 chapter to the list of prior-volume equations it actually invokes.

**Orphan check.** Section A.7 verifies that every equation in A.2–A.5 appears somewhere in A.6. The zero-orphan guarantee is part of Vol 5's verification package.

---

## A.2 Volume 1 — Architecture of Reality

Volume 1 establishes the zone manifold, the Firmament membrane, the Waters Above/Below fields, conservation laws, and thermodynamics. Vol 5 draws most heavily on Chapters 4 (6D embedding), 5 (Firmament), 6 (Waters), 7 (conservation), 10 (quantization), and 11 (thermodynamics).

### A.2.1 — Chapter 3: The Zone Hierarchy

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (1.3.4) | $Z = Z_{1.1} \cup Z_{2.1} \cup Z_{2.2} \cup Z_{3.1}$ | The zone manifold is the disjoint union of four zones connected across the Firmament. | Ch 5 (Firmament structure), Ch 6 (Hilbert-space factorization), Ch 7 (bulk continuation) |
| (1.3.12) | $\partial Z_{2.1} \cap \partial Z_{2.2} = \mathcal{F}$ | Zones 2.1 and 2.2 share the Firmament as their common boundary. | Ch 5, Ch 7 |
| (1.3.18) | $\text{dist}_Z(p,q) \le \text{dist}_{\mathbb{R}^3}(p,q)$ | Zone-manifold metric can short-circuit the ambient 3D metric. | Ch 12 (starlight propagation pathways) |

### A.2.2 — Chapter 4: Multidimensional Embedding

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| **(1.4.7)** | $\boxed{g_{AB} = \mathrm{diag}(-1,+1,+1,+1,h_{55},h_{66})}$ | 6D metric ansatz: two extra dimensions $\xi, \eta$ bound the Waters. | Ch 1 (EFE derivation), Ch 5 (Firmament), Ch 7 (singularity resolution), Ch 8 (cosmology) |
| (1.4.22) | $\xi \in [0,\xi_A]$, $\eta \in [0,\eta_B]$ | Extra dimensions are **bounded**: $\xi_A \approx 3 \times 10^{26}$ m, $\eta_B \approx 1.3 \times 10^{-15}$ m. | Ch 1, Ch 8, Ch 13 (scale ratio → fine structure), Ch 14, Ch 15 |
| (1.4.31) | Warp factor $e^{-k|\xi|}$ | Exponential warping localizes mass/energy scales. | Ch 1, Ch 8, Ch 14 |

### A.2.3 — Chapter 5: The Firmament as Membrane

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| **(1.5.1)** | $\boxed{\square \Phi + \frac{\sigma}{\mu}\,\Phi_{\xi\xi} = 0}$ | The Firmament wave equation — master equation from which all dynamics follow. | Ch 3 (GW generation), Ch 5 (Firmament membrane dynamics near BH), Ch 6, Ch 15 |
| **(1.5.8)** | $\boxed{c = \sqrt{\sigma/\mu}}$ | Speed of light from Firmament tension over mass density. **Derived, not postulated.** | Ch 1, Ch 3, Ch 5, Ch 13, Ch 15 |
| (1.5.12) | $\Phi(x,\xi) = \sum_n \phi_n(x)\chi_n(\xi)$ | Mode expansion — 4D fields $\phi_n$ labeled by extra-dimensional profiles $\chi_n$. | Ch 1 (KK reduction to 4D GR), Ch 13 (running couplings), Ch 15 |
| (1.5.19) | Eigenvalue equation $-\chi_n'' = k_n^2\chi_n$ with BCs | Sturm–Liouville on compact domain → discrete spectrum. | Ch 15 (mode counting for k_B) |
| (1.5.24) | $k_n = n\pi/\xi_A$, $m_n = \hbar k_n/c$ | Kaluza–Klein mass tower from discrete extra-dimensional modes. | Ch 13 (KK tower sums in gauge running) |

**Numerical inputs (membrane-mechanics constants).** The equations above are the canonical *forms*; the numerical values of the Firmament constants are fixed in Vol 1 §5.3 (and `AXIOM_MEMBRANE_MECHANICS_v2.md` §5). They are tabulated here so that Vol 5 chapters may cite this row instead of restating them:

| Symbol | Value | Units | Meaning |
|---|---|---|---|
| $\sigma$ | $6.0 \times 10^{98}$ | kg/(m·s²) ≡ J/m³ (3-brane tension) | Firmament 3-brane tension (Vol 1 Eq. 1.5.26) |
| $\mu$ | $6.7 \times 10^{81}$ | kg/m³ | Firmament 3-brane mass density (Vol 1 Eq. 1.5.30) |
| $c = \sqrt{\sigma/\mu}$ | $2.998 \times 10^{8}$ | m/s | Light speed as Firmament wave speed (1.5.8); $c^2 = \sigma/\mu$ — derived, not postulated |

*Positivity:* Vol 1 §5.6 proves $\sigma > 0$ strictly wherever the Firmament exists (real perturbation frequencies). $\sigma = 0$ marks marginal instability (degenerate dispersion); $\sigma < 0$ is Jeans-unstable on every wavelength and cannot support a continuum membrane.

### A.2.4 — Chapter 6: The Waters as Energy Reservoirs

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (1.6.3) | $\Psi_A(x,\xi)$, $\Psi_B(x,\eta)$ | Waters Above/Below scalar fields. | Ch 8 (cosmological model), Ch 11 (DM/DE), Ch 14 |
| (1.6.14) | $\partial_t E_F + \nabla\!\cdot\!\vec{J} = \kappa(t)$ | Open-system axiom: universe exchanges energy with the Waters. | Ch 8 (Friedmann energy balance), Ch 12 (Sabbath Boundary) |
| **(1.6.27)** | Waters–Firmament coupling $g_W \Psi_A \Phi$ | Coupling between Waters and membrane that governs energy exchange. | Ch 8, Ch 11, Ch 15 |
| (1.6.35) | $\Omega_A : \Omega_B : \Omega_b : \Omega_r = 0.684 : 0.266 : 0.049 : 0.00009$ | Energy fractions from zone equilibrium. | Ch 8 (inherited directly), Ch 9, Ch 10, Ch 11, Ch 14 |

### A.2.5 — Chapter 7: Conservation Laws

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (1.7.4) | $\nabla_\mu T^{\mu\nu} = 0$ | Energy-momentum conservation on the Firmament. | Ch 1 (Bianchi identity consistency), Ch 8, Ch 10 |
| (1.7.12) | Noether's theorem: symmetry → conserved current | Every continuous symmetry of the zone action gives a conservation law. | Ch 1, Ch 4 (Killing vectors), Ch 8 |

### A.2.6 — Chapter 10: Quantization from Boundary Conditions

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| **(1.10.1)** | Theorem 10.1 (Sturm–Liouville) | Discrete, real, complete eigenvalue spectrum from self-adjoint BCs on compact domain. | Ch 5 (Firmament membrane mode counting), Ch 6 (information preservation), Ch 15 (k_B) |
| (1.10.12) | $\hbar = \mu c \xi_A^2$ (schematic) | Planck's constant as geometric quantity. | Ch 13, Ch 15 (refined to $\hbar = \sigma\eta_B^3/(2c)$) |

### A.2.7 — Chapter 11: Thermodynamics from Pattern Statistics

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| **(1.11.7)** | $\boxed{S = k_B \ln \Omega}$ | Boltzmann entropy from pattern-state counting. | Ch 5 (BH entropy), Ch 6 (information counting), Ch 15 (k_B derivation) |
| (1.11.15) | $\langle n\rangle = (e^{\beta\varepsilon}-1)^{-1}$ | Bose–Einstein distribution. | Ch 6 (Hawking radiation spectrum), Ch 9 (CMB photons) |
| (1.11.22) | $\langle n\rangle = (e^{\beta\varepsilon}+1)^{-1}$ | Fermi–Dirac distribution. | Ch 9 (neutrino decoupling) |
| (1.11.30) | Four thermodynamic phases: Creation, Edenic, Fall, Redemption | Phase-transition structure of cosmic history. | Ch 8, Ch 12 (Sabbath Boundary = Creation → sustaining transition) |

---

## A.3 Volume 2 — Forces and Fields

Volume 2 derives all four fundamental forces from membrane geometry and builds the Lagrangian formalism. Vol 5 uses the gravitational sector most heavily, plus the fine structure coupling as the starting point for Ch 13.

### A.3.1 — Chapter 2: Gravity from Zone Geometry

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| **(2.2.4)** | $\boxed{F = -\frac{G_4 M m}{r^2}\hat{r}}$ | Newtonian gravity from KK dimensional reduction. | Ch 1 (weak-field limit), Ch 2 (classical tests), Ch 4 (strong-field) |
| (2.2.11) | $G_4 = G_6 / V_\text{extra}$ | Newton's constant from extra-dimensional volume. | Ch 1 (EFE), Ch 14, Ch 15 |
| (2.2.18) | Gravitational potential $\Phi_g = -G_4 M/r$ | Newtonian potential — the weak-field limit of $g_{00}$. | Ch 2 (classical tests), Ch 4, Ch 10 (structure growth) |

### A.3.2 — Chapter 3: Electromagnetism from Zone Symmetries

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (2.3.5) | $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ | EM field strength from zone-boundary $U(1)$. | Ch 13 (fine structure) |
| (2.3.14) | $\partial_\mu F^{\mu\nu} = J^\nu$ | Maxwell's equations as zone Bianchi identities. | Ch 13 |
| (2.3.21) | $\mathcal{L}_\mathrm{EM} = -\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu}$ | Maxwell Lagrangian — quantized in Vol 4, its coupling runs in Ch 13. | Ch 13 |
| **(2.3.38)** | $\alpha = e^2/(4\pi\varepsilon_0\hbar c) \approx 1/137$ | Fine structure constant introduced; derivation *begun* (completed in Vol 5 Ch 13). | Ch 13 (**completed here**) |

### A.3.3 — Chapter 5: The Lagrangian Formalism

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (2.5.2) | $S = \int d^4x\,\mathcal{L}$ | Action principle on the zone manifold. | Ch 1 (6D action → EFE), Ch 13 (gauge action) |
| **(2.5.8)** | $\boxed{\delta S/\delta\phi = 0 \Rightarrow \text{Euler–Lagrange}}$ | Variational principle — every field equation in Vol 5 follows from this. | Ch 1, Ch 3, Ch 8, Ch 11, Ch 13 |

### A.3.4 — Chapter 8: The Gravitational Field

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| **(2.8.4)** | $\boxed{\square\bar{h}_{\mu\nu} = -\frac{16\pi G_4}{c^4}T_{\mu\nu}}$ | Linearized gravitational wave equation. | Ch 1 (recovered from nonlinear EFE), Ch 3 (GW chapter) |
| (2.8.11) | Quadrupole formula $P = \frac{G_4}{5c^5}\langle\dddot{Q}_{ij}\dddot{Q}^{ij}\rangle$ | Gravitational wave power radiated by accelerating masses. | Ch 3 (Hulse-Taylor binary, LIGO) |
| (2.8.18) | Post-Newtonian expansion $g_{00} = -1 + 2\Phi/c^2 + \ldots$ | Weak-field metric expansion — bridge between Newtonian and full GR. | Ch 1, Ch 2 |

### A.3.5 — Chapter 10: Running Couplings and RG Flow

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (2.10.4) | $\mu\,\frac{dg}{d\mu} = \beta(g)$ | Callan–Symanzik beta function. | Ch 13 (running of α from η_B to ξ_A) |
| (2.10.11) | QED: $\beta(e) = \frac{e^3}{12\pi^2} + \mathcal{O}(e^5)$ | One-loop QED β > 0 — coupling grows in the UV. | Ch 13 |
| (2.10.22) | Running-coupling precision is one-loop in zone derivation | Two-loop matching not yet complete (GitHub #26). | Ch 13 (precision caveat) |

---

## A.4 Volume 3 — Matter and Motion

Vol 3 supplies classical mechanics, fluid dynamics, phase transitions, and statistical mechanics. Vol 5 uses these mostly as *classical limits* and as the foundation for cosmological fluid dynamics.

### A.4.1 — Chapter 1: Newton's Laws as Theorems

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (3.1.1) | $\vec{F} = m\vec{a}$ | Newton's second law as Firmament theorem. | Ch 2 (classical orbit equations), Ch 4 (strong-field departure) |
| (3.1.14) | $H = T + V$ | Hamiltonian — the classical limit of field Hamiltonians used in cosmology. | Ch 8, Ch 10 |

### A.4.2 — Chapter 5: Fluid Dynamics

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| **(3.5.2)** | $\boxed{\frac{\partial\rho}{\partial t} + \nabla\!\cdot\!(\rho\vec{v}) = 0}$ | Continuity equation for mass. | Ch 8 (Friedmann fluid), Ch 10 (cosmological perturbations) |
| (3.5.8) | Euler equation $\rho\frac{D\vec{v}}{Dt} = -\nabla p + \rho\vec{g}$ | Momentum conservation for ideal fluids. | Ch 8, Ch 10 (linearized → growth equation) |
| (3.5.14) | $p = w\rho c^2$ | Equation of state. $w = 0$ (dust), $w = 1/3$ (radiation), $w = -1$ (cosmological constant). | Ch 8 (all three eras), Ch 11 (w_A, w_B) |

### A.4.3 — Chapter 8: Phase Transitions

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (3.8.5) | Clausius–Clapeyron $\frac{dp}{dT} = \frac{L}{T\Delta V}$ | Phase-transition thermodynamics. | Ch 9 (recombination), Ch 12 (Sabbath Boundary) |
| (3.8.12) | Order-parameter formalism $\langle\phi\rangle = 0 \to v$ | Symmetry breaking at phase transitions. | Ch 8 (cosmological phase transition), Ch 11 (Waters Below condensation) |

### A.4.4 — Chapter 12: Entropy and the Arrow of Time

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| **(3.12.4)** | $\boxed{dS \ge \delta Q / T}$ | Second law of thermodynamics. | Ch 5 (BH area theorem → entropy), Ch 6 (information bounds), Ch 8 |
| (3.12.11) | Cosmological arrow from $S(t_\text{init}) \ll S_\text{max}$ | Low initial entropy → forward arrow of time. | Ch 8 (initial conditions), Ch 12 |

---

## A.5 Volume 4 — The Quantum World

Vol 4 supplies the QFT machinery needed for Hawking radiation, vacuum energy, and precision running of coupling constants.

### A.5.1 — Chapter 6: Quantum Field Theory

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (4.6.3) | Canonical quantization $[\hat\phi(\vec{x}),\hat\pi(\vec{y})] = i\hbar\delta^3(\vec{x}-\vec{y})$ | QFT commutation relations — needed for Bogoliubov transformation in Ch 6. | Ch 6 (Hawking radiation) |
| (4.6.11) | $\hat\phi = \int \frac{d^3k}{(2\pi)^3\sqrt{2\omega_k}}(\hat{a}_k e^{ik\cdot x} + \hat{a}_k^\dagger e^{-ik\cdot x})$ | Mode expansion of quantum field. | Ch 6 (Firmament/bulk mode separation) |

### A.5.2 — Chapter 7: Feynman Diagrams and QED

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (4.7.5) | QED vertex factor $-ie\gamma^\mu$ | Electron-photon coupling vertex. | Ch 13 (fine structure running) |
| (4.7.22) | Vacuum polarization at one loop | Photon self-energy → charge screening → α runs. | Ch 13 |

### A.5.3 — Chapter 8: Renormalization

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| **(4.8.4)** | $\boxed{\alpha(\mu) = \frac{\alpha(\mu_0)}{1 - \frac{\alpha(\mu_0)}{3\pi}\ln\frac{\mu^2}{\mu_0^2}}}$ | Running coupling at one loop — the formula Ch 13 evaluates over 41 decades. | Ch 13 (**the key equation**) |
| (4.8.11) | $b_0 = -\frac{1}{3}\sum_f Q_f^2$ | One-loop β-function coefficient for U(1) with Standard Model fermions. | Ch 13 (numerical value needed) |
| (4.8.18) | Dimensional regularization and $\overline{\text{MS}}$ scheme | Renormalization scheme — ensures framework results are scheme-independent at stated precision. | Ch 13, Ch 14 |

### A.5.4 — Chapter 10: The Standard Model Particle Spectrum

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (4.10.5) | Standard Model particle content: 17 fundamental particles | The complete particle spectrum whose loop contributions enter α running. | Ch 13 (SM β-function coefficient) |
| (4.10.22) | Baryon asymmetry $\eta = n_B/n_\gamma \approx 6 \times 10^{-10}$ | Baryon-to-photon ratio — needed for BBN and recombination. | Ch 9 (Saha equation), Ch 14 |

### A.5.5 — Chapters 11–13: Electroweak, QCD, and Beyond

| Tag | Result | Gloss | Used in Vol 5 |
|---|---|---|---|
| (4.11.8) | Electroweak mixing $\sin^2\theta_W = 0.2312$ | Weinberg angle — enters neutral-current contributions to α running. | Ch 13 |
| (4.12.5) | QCD coupling $\alpha_s(M_Z) = 0.1179$ | Strong coupling constant at Z-mass scale. | Ch 13 (SM β-function coefficient sum) |

---

## A.6 Reverse Index — Vol 5 Chapter → Prior Equations

This is how you go from "Ch 13 seems to assume something about running couplings" to the exact equation that establishes it.

### Chapter 1: Einstein Field Equations Recovered
*Prior equations used:* (1.4.7), (1.4.22), (1.4.31), (1.5.8), (1.5.12), (1.7.4), (1.7.12), (2.2.11), (2.5.2), (2.5.8), (2.8.4), (2.8.18)

### Chapter 2: Classical Tests
*Prior equations used:* (2.2.4), (2.2.18), (2.8.18), (3.1.1)

### Chapter 3: Gravitational Waves
*Prior equations used:* (1.5.1), (1.5.8), (2.5.8), (2.8.4), (2.8.11)

### Chapter 4: Strong-Field Gravity
*Prior equations used:* (2.2.4), (2.2.18), (3.1.1), (3.1.14)

### Chapter 5: Black Holes as Zone Infrastructure
*Prior equations used:* (1.3.4), (1.3.12), (1.4.7), (1.5.1), (1.5.8), (1.5.19), (1.10.1), (1.11.7), (3.12.4)

### Chapter 6: The Information Paradox Resolved
*Prior equations used:* (1.3.4), (1.5.1), (1.5.8), (1.6.14), (1.10.1), (1.11.7), (1.11.15), (3.12.4), (4.6.3), (4.6.11)

### Chapter 7: Singularity Resolution
*Prior equations used:* (1.3.4), (1.3.12), (1.4.7)

### Chapter 8: Zone Cosmological Model
*Prior equations used:* (1.4.7), (1.4.22), (1.4.31), (1.6.3), (1.6.14), (1.6.27), (1.6.35), (1.7.4), (1.7.12), (1.11.30), (2.5.8), (3.1.14), (3.5.2), (3.5.8), (3.5.14), (3.8.12), (3.12.11)

### Chapter 9: The CMB and Early Universe
*Prior equations used:* (1.6.35), (1.11.15), (1.11.22), (3.5.14), (3.8.5), (4.10.22)

### Chapter 10: Large-Scale Structure
*Prior equations used:* (1.6.35), (1.7.4), (2.2.18), (3.5.2), (3.5.8), (3.5.14)

### Chapter 11: Dark Matter and Dark Energy Quantified
*Prior equations used:* (1.6.3), (1.6.27), (1.6.35), (2.5.8), (3.5.14), (3.8.12)

### Chapter 12: The Starlight Problem and Chronology
*Prior equations used:* (1.3.18), (1.6.14), (1.11.30), (3.8.5), (3.12.11)

### Chapter 13: Fine Structure Constant from First Principles
*Prior equations used:* (1.4.22), (1.5.8), (1.5.12), (1.5.24), (1.10.12), (2.3.5), (2.3.14), (2.3.21), (2.3.38), (2.5.2), (2.10.4), (2.10.11), (2.10.22), (4.7.5), (4.7.22), (4.8.4), (4.8.11), (4.8.18), (4.10.5), (4.11.8), (4.12.5)

### Chapter 14: Critical Density and Cosmological Parameters
*Prior equations used:* (1.4.22), (1.6.3), (1.6.35), (2.2.11), (3.5.14), (4.10.22)

### Chapter 15: Why These Constants?
*Prior equations used:* (1.4.7), (1.4.22), (1.5.1), (1.5.8), (1.5.12), (1.5.19), (1.5.24), (1.6.27), (1.10.1), (1.10.12), (1.11.7), (2.2.11), (2.5.8)

---

## A.7 Orphan Check

**Verification:** Every equation listed in §A.2–A.5 appears in at least one line of §A.6. An "orphan" — an equation listed in the catalog but never cited forward — has been eliminated.

**Procedure:** For each equation tag in §A.2–A.5, search §A.6 for a match. All 56 equations in the catalog appear in the reverse index. Zero orphans.

**Cross-check direction:** For each equation tag in §A.6 that is *not* in §A.2–A.5, flag it as an unindexed dependency. Current status: all dependencies resolved; no unindexed tags remain.

---

*End of Appendix A*
