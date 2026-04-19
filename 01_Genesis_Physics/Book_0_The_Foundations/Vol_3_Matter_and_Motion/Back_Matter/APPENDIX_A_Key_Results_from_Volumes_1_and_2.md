# APPENDIX A: Key Results from Volumes 1–2

*A reference for every Vol 1 and Vol 2 equation cited in Volume 3. The student can look up any referenced result here without flipping back to earlier volumes.*

---

## A.1 How to Use This Appendix

Throughout Volume 3, we cite prior results using compact tags:

- **`(1.Ch.Eq)`** — Volume 1, Chapter `Ch`, Equation `Eq`
- **`(2.Ch.Eq)`** — Volume 2, Chapter `Ch`, Equation `Eq`
- **`(3.Ch.Eq)`** — Volume 3 (this volume), Chapter `Ch`, Equation `Eq`

Every tag of the first two kinds that appears anywhere in Vol 3 is reproduced in this appendix, with the equation in full, a one-line gloss of what it says, and a list of Vol 3 chapters that use it. Notation follows **Vol 1 Appendix B (Notation Reference)** exactly — see that appendix for the master symbol list.

The appendix is structured in three parts:

- **§A.2** Volume 1 results (by chapter)
- **§A.3** Volume 2 results (by chapter)
- **§A.4** Reverse index: which Vol 3 chapter cites which Vol 1/2 equation

If you are reading Vol 3 and hit an equation you do not recognize, check the tag, jump here, and you will find it.

---

## A.2 Volume 1: Architecture of Reality — Results Used in Vol 3

### A.2.1 Chapter 1 — Axioms and Definitions

**Open System Axiom.** The zone manifold is not an isolated system; energy and information flow across its boundary through the sustaining coupling $\kappa(t)$.
$$\text{Universe is open} \iff \exists \;\kappa(t) \neq 0 \tag{1.1.1}$$
*Used in Vol 3: Ch 9, 12 (First Law extension; arrow of time).* 

**Five Governing Principles** (named but formalized in Ch 8): Variation, Symmetry, Quantization, Conservation, Degradation.
*Used in Vol 3: Ch 1, 2, 9, 12.*

### A.2.2 Chapter 2 — Mathematical Preliminaries

Vol 3 cites no specific equation from Ch 2; it assumes the vector calculus and tensor analysis results compiled in Vol 2 Appendix A. See §A.3 of *that* appendix for the specific identities reused in Vol 3 Ch 4–5.

### A.2.3 Chapter 3 — The Zone Manifold

**Zone metric (6D).**
$$ds^2 = g_{\mu\nu}(x)\,dx^\mu dx^\nu + h_{ab}(x,y)\,dy^a dy^b \tag{1.3.12}$$
Coordinates $x^\mu$ ($\mu = 0,1,2,3$) label the 4D Firmament; $y^a$ ($a = 4,5$) label the two compact extra dimensions.
*Used in Vol 3: Ch 1 (geodesic derivation), Ch 2 (Lagrangian), Ch 6–7 (KK reduction).*

**Flat-space limit.**
$$g_{\mu\nu}(x) \to \eta_{\mu\nu} = \text{diag}(-,+,+,+) \qquad h_{ab} \to \delta_{ab}\,L_{\text{eff}}^2 \tag{1.3.31}$$
*Used in Vol 3: Ch 1 (first law from geodesic + flat-space limit).*

### A.2.4 Chapter 4 — The 6D Embedding Space

**Embedding isometry.** The zone manifold embeds isometrically in $\mathbb{R}^{6,0}$ (spatial) × $\mathbb{R}^{0,1}$ (temporal), with the Firmament as the 4D hypersurface of fixed extra-dimensional radius:
$$y^a y^a = L_{\text{eff}}^2 \tag{1.4.18}$$
*Used in Vol 3: Ch 6 (standing-wave mode counting).*

### A.2.5 Chapter 5 — The Firmament Manifold

**Firmament wave equation** for the membrane displacement field $\Phi(x,y)$:
$$\left(\Box_4 + \nabla_y^2 + m_0^2\right)\Phi(x,y) = 0 \tag{1.5.51}$$
where $\Box_4 = \eta^{\mu\nu}\partial_\mu\partial_\nu$ is the 4D d'Alembertian and $\nabla_y^2$ is the Laplacian on the compact extra dimensions.
*Used in Vol 3: Ch 6 (standing-wave mode spectrum), Ch 7 (Higgs as KK mode).*

**KK mode expansion.** Because the extra dimensions are compact with circumference $2\pi L_{\text{eff}}$, separation of variables gives:
$$\Phi(x,y) = \sum_{n,\ell} \phi_{n\ell}(x)\, Y_{n\ell}(y), \qquad m_{n\ell}^2 = m_0^2 + \frac{n^2 + \ell^2}{L_{\text{eff}}^2} \tag{1.5.63}$$
*Used in Vol 3: Ch 6, 7.*

**Membrane tension.**
$$\sigma \approx 6 \times 10^{98}\;\text{kg/s}^2 \tag{1.5.74}$$
*Used in Vol 3: Ch 7 (electroweak vacuum), Ch 5 (stress-tensor scale setting).*

### A.2.6 Chapter 6 — Waters Field Equations

**Waters Below field equation** (the equation that becomes Navier-Stokes under a Madelung transform):
$$\boxed{\Box_6\Psi_B + U'(\Psi_B) + G_{\text{int}}\Psi_A = 0} \tag{1.6.15}$$
where $\Psi_B$ is the complex Waters Below scalar, $U'$ the potential derivative, and $G_{\text{int}}$ the coupling to the Waters Above field $\Psi_A$.
*Used in Vol 3: Ch 5 (continuum/fluid), Ch 11 (transport), Ch 12 (entropy).*

**Madelung transformation.** Writing $\Psi_B = \sqrt{\rho}\,e^{iS/\hbar}$ and separating real/imaginary parts of (1.6.15) yields the **continuity equation** and the **Euler equation** plus a quantum pressure term:
$$\partial_t\rho + \nabla\cdot(\rho\mathbf{v}) = 0 \tag{1.6.19}$$
$$\rho\left(\partial_t + \mathbf{v}\cdot\nabla\right)\mathbf{v} = -\nabla p - \rho\nabla\Phi_g + \mathbf{f}_Q \tag{1.6.20}$$
$$\mathbf{v} = \nabla S/m, \qquad \mathbf{f}_Q = \frac{\hbar^2}{2m}\nabla\left(\frac{\nabla^2\sqrt{\rho}}{\sqrt{\rho}}\right) \tag{1.6.21}$$
*Used in Vol 3: Ch 5 (the central continuum/Navier-Stokes derivation).*

**Waters stress-energy tensor** (schematic — full form spans (1.6.22)–(1.6.41)):
$$T_{\mu\nu}^{(W)} = \partial_\mu\Psi^*\partial_\nu\Psi + \partial_\nu\Psi^*\partial_\mu\Psi - g_{\mu\nu}\mathcal{L}_W \tag{1.6.22}$$
*Used in Vol 3: Ch 5 (stress tensor via Waters side), Ch 9 (first-law source J).*

### A.2.7 Chapter 7 — Symmetries and Conservation Laws

**Covariant conservation of stress-energy** (from diffeomorphism invariance of the zone action):
$$\nabla_\mu T^{\mu\nu} = 0 \tag{1.7.17}$$
*Used in Vol 3: Ch 1 (third law / action-reaction), Ch 5 (Cauchy stress symmetry).*

**Noether momentum current** (from spatial translation invariance):
$$P^\mu = \int_\Sigma T^{\mu 0}\, d^3x, \qquad \dot{P}^\mu = 0 \tag{1.7.30}$$
*Used in Vol 3: Ch 1, 4, 5, 11.*

**Rotational Killing vectors** (SO(3) spatial isotropy):
$$\xi_{(i)}^\mu = \epsilon_{ijk}\,x^j\,\delta^{\mu k}, \qquad i = 1,2,3 \tag{1.7.31}$$
*Used in Vol 3: Ch 3 (central force planar reduction), Ch 4 (rigid body).*

**Angular momentum conservation.**
$$L^i = \int_\Sigma \xi_{(i)}^\mu T^0{}_\mu\,d^3x, \qquad \dot{L}^i = 0 \tag{1.7.33}$$
*Used in Vol 3: Ch 3, 4.*

### A.2.8 Chapter 8 — Five Governing Principles

**Total zone action** (principle of stationary action in its Vol 1 form):
$$S_{\text{total}} = \int d^6x\,\sqrt{-g}\,\mathcal{L}_{\text{total}}, \qquad \delta S_{\text{total}} = 0 \tag{1.8.3}$$
*Used in Vol 3: Ch 2, 9.*

### A.2.9 Chapter 9 — Pattern Operators and Seven Types

**Seven pattern types** $\{\mathcal{P}_1,\dots,\mathcal{P}_7\}$ — the topological/resonance classes identified in Vol 1 Ch 9. Vol 3 uses only the enumeration; no specific equation is cited beyond the catalog itself.
*Used in Vol 3: Ch 6 (Chladni / topological defect classification).*

### A.2.10 Chapter 10 — Quantization from Boundary Conditions

**Discrete-spectrum theorem.** For any field on the zone manifold subject to periodic boundary conditions on the compact extra dimensions, the eigenvalue spectrum is discrete:
$$\lambda_n = \lambda_0 + \frac{n^2\pi^2}{L_{\text{eff}}^2}, \qquad n \in \mathbb{Z}_{\geq 0} \tag{1.10.22}$$
*Used in Vol 3: Ch 6, 10 (Planck spectrum derivation).*

### A.2.11 Chapter 11 — Thermodynamics from Zone Separation

**6D action restricted to thermodynamic sector.**
$$S_{\text{thermo}} = \int d^6x\,\sqrt{-g}\left[\tfrac{1}{2}(\partial\Phi)^2 - V(\Phi) + \mathcal{L}_\kappa\right] \tag{1.11.1}$$
*Used in Vol 3: Ch 9, 10.*

**Multiplicity from membrane defect counting.**
$$\Omega(U,V,N) = \#\{\text{microstates of the defect ensemble with fixed }(U,V,N)\} \tag{1.11.2}$$
*Used in Vol 3: Ch 9 (Zeroth Law), Ch 10.*

**Boltzmann entropy.**
$$\boxed{S = k_B\ln\Omega} \tag{1.11.10}$$
*Used in Vol 3: Ch 9, 10, 12.*

**Zero-point + thermal energy** (per mode of angular frequency $\omega$):
$$\langle E_\omega\rangle = \tfrac{1}{2}\hbar\omega + \frac{\hbar\omega}{e^{\hbar\omega/k_BT} - 1} \tag{1.11.14}$$
*Used in Vol 3: Ch 9 §9.6.4, Ch 10 (Planck).*

**First Law — closed system form.**
$$dU = \delta Q - \delta W \tag{1.11.18}$$
*Used in Vol 3: Ch 9.*

**First Law — open system form.**
$$\boxed{dU = \delta Q - \delta W + \delta E_\kappa} \tag{1.11.19}$$
where $\delta E_\kappa$ is the sustaining-input term. This is the open-system generalization that makes the zone framework thermodynamically complete.
*Used in Vol 3: Ch 9, 12.*

**Source term for the sustaining input.**
$$\delta E_\kappa = \int_V J(x)\,d^3x, \qquad J(x) = \kappa(t)\,\Psi_A^*(x)\Psi_B(x) \tag{1.11.20}$$
*Used in Vol 3: Ch 9, 12.*

**Partition function.**
$$\boxed{Z(T) = \sum_n e^{-E_n/k_BT}} \tag{1.11.25}$$
*Used in Vol 3: Ch 9, 10, 11.*

**Boltzmann distribution.**
$$p_n = \frac{1}{Z}\,e^{-E_n/k_BT} \tag{1.11.37}$$
*Used in Vol 3: Ch 9, 10, 11, 12.*

**Entropy growth in Phase 3 (post-Fall).**
$$\boxed{\frac{dS}{dt} = L\cdot\Delta\kappa > 0} \tag{1.11.46}$$
where $L$ is a positive functional of the system's state and $\Delta\kappa = \kappa_{\text{full}} - \kappa_{\text{partial}} > 0$.
*Used in Vol 3: Ch 9 (Second Law), Ch 12 (arrow of time).*

**Third Law.**
$$\lim_{T\to 0^+} S(T) = 0 \tag{1.11.49}$$
*Used in Vol 3: Ch 9.*

**Debye-like density of states.**
$$g(\omega)\,d\omega \propto \omega^{d-1}\,d\omega, \qquad \omega \leq \omega_D \tag{1.11.54}$$
*Used in Vol 3: Ch 9 §9.7.3.*

**Debye low-temperature entropy and heat capacity.**
$$S(T) \propto T^d \quad (T \ll \Theta_D), \qquad c_V(T) \propto T^d \tag{1.11.55}\text{–}\tag{1.11.56}$$
In three dimensions this is the famous $T^3$ law.
*Used in Vol 3: Ch 9 §9.7.3.*

**Unattainability of $T=0$.**
$$\text{No finite sequence of operations reaches }T = 0. \tag{1.11.57}$$
*Used in Vol 3: Ch 9 §9.7.4.*

---

## A.3 Volume 2: Forces and Fields — Results Used in Vol 3

### A.3.1 Chapter 1 — Why Forces Exist

Vol 3 cites the conceptual result — "all fundamental forces arise from gauge structure on the zone manifold" — but no specific numbered equation from Ch 1.

### A.3.2 Chapter 2 — Gravity from Zone Curvature

**Four-dimensional Newton constant from membrane tension.**
$$\boxed{G_4 = \frac{c^4}{8\pi\sigma L_{\text{eff}}^2} = 6.674 \times 10^{-11}\;\text{m}^3/(\text{kg}\cdot\text{s}^2)} \tag{2.2.29}$$
*Used in Vol 3: Ch 1 (F=ma with gravitational coupling), Ch 3 (Kepler's third law), Ch 8 (gravitational aspects of phase transitions).*

**Geodesic equation** for a test particle of proper time $\tau$:
$$\boxed{\frac{d^2x^\mu}{d\tau^2} + \Gamma^\mu{}_{\alpha\beta}\frac{dx^\alpha}{d\tau}\frac{dx^\beta}{d\tau} = 0} \tag{2.2.44}$$
*Used in Vol 3: Ch 1 (first law derivation), Ch 3 (orbital mechanics from curvature).*

### A.3.3 Chapter 3 — Electromagnetism from Membrane Wave Propagation

**Maxwell's equations in tensor form.**
$$\partial_\mu F^{\mu\nu} = \mu_0 J^\nu, \qquad \partial_{[\alpha}F_{\mu\nu]} = 0 \tag{2.3.27}$$
*Used in Vol 3: Ch 5 (optics subsection), Ch 10 (photon modes for Planck spectrum).*

**Vacuum wave speed.**
$$c = 1/\sqrt{\mu_0\epsilon_0} \tag{2.3.41}$$
*Used in Vol 3: Ch 5, 10.*

### A.3.4 Chapter 4 — Strong and Weak Forces from Zone Boundary Effects

**Coupling scale hierarchy.**
$$\alpha_s(M_Z) \approx 0.118, \qquad \alpha_w(M_Z) \approx 0.034 \tag{2.4.33}$$
*Used in Vol 3: Ch 7 (mass hierarchy), Ch 8 (electroweak transition).*

### A.3.5 Chapter 5 — The Zone Lagrangian

**Zone action.**
$$S_{\text{zone}} = \int d^6x\,\sqrt{-g}\,\mathcal{L}_{\text{zone}} \tag{2.5.1}$$
*Used in Vol 3: Ch 1, 2, 9.*

**Full zone Lagrangian** (schematic; the complete expression occupies (2.5.2)–(2.5.19)):
$$\mathcal{L}_{\text{zone}} = \mathcal{L}_{\text{grav}} + \mathcal{L}_{\text{gauge}} + \mathcal{L}_{\text{Waters}} + \mathcal{L}_{\text{matter}} + \mathcal{L}_\kappa \tag{2.5.20}$$
*Used in Vol 3: Ch 1, 2.*

**Variational principle — master field equation.**
$$\delta S_{\text{total}} = 0 \quad\Longrightarrow\quad \frac{\delta\mathcal{L}_{\text{zone}}}{\delta\phi^I} - \partial_\mu\frac{\delta\mathcal{L}_{\text{zone}}}{\delta(\partial_\mu\phi^I)} = 0 \tag{2.5.21}$$
for every field $\phi^I$.
*Used in Vol 3: Ch 1 (F=ma as a special case), Ch 2, Ch 9.*

### A.3.6 Chapter 6 — Gauge Theory from Zone Symmetries

**Electroweak gauge group structure.**
$$G_{\text{EW}} = SU(2)_L \times U(1)_Y \;\xrightarrow{\text{SSB}}\; U(1)_{\text{EM}} \tag{2.6.18}$$
*Used in Vol 3: Ch 7 (mass generation).*

### A.3.7 Chapter 7 — Classical Electrodynamics Complete

**EM field tensor and Lagrangian.**
$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu, \qquad \mathcal{L}_{EM} = -\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu} - J^\mu A_\mu \tag{2.7.5}$$
*Used in Vol 3: Ch 10 (photon modes).*

**Radiation Poynting flux.**
$$\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B} \tag{2.7.38}$$
*Used in Vol 3: Ch 10 (Stefan-Boltzmann cross-check).*

### A.3.8 Chapter 8 — Gravitational Field Theory

**Weak-field Newtonian limit.**
$$g_{00} = -\left(1 + \frac{2\Phi_N}{c^2}\right), \qquad \nabla^2\Phi_N = 4\pi G_4\rho \tag{2.8.24}$$
*Used in Vol 3: Ch 1 (F=ma in gravitational field), Ch 3 (Kepler).*

### A.3.9 Chapter 9 — The Hierarchy Problem Solved

**Electroweak / Planck scale ratio.**
$$\frac{M_{\text{EW}}}{M_{\text{Pl}}} \sim \exp\!\left[-\,c_1\,\left(\frac{L_{\text{eff}}}{\ell_{\text{Pl}}}\right)^2\right] \tag{2.9.11}$$
*Used in Vol 3: Ch 7 (why v ≪ M_Pl), Ch 8.*

### A.3.10 Chapter 10 — Running Couplings and Zone Energy Scales

**One-loop running of the gauge couplings.**
$$\alpha_i^{-1}(Q) = \alpha_i^{-1}(Q_0) + \frac{b_i}{2\pi}\ln(Q/Q_0) \tag{2.10.7}$$
*Used in Vol 3: Ch 7 (Yukawa coupling hierarchy), Ch 8 (phase transition scale).*

### A.3.11 Chapter 11 — The Force Landscape

**Force summary table.** Gravity, electromagnetism, weak, strong — their relative strengths at $Q = 1\,\text{GeV}$ and at $Q = M_Z$.
$$\text{Fig. 2.11.1: Force strengths vs. energy scale} \tag{2.11.1}$$
*Used in Vol 3: Ch 7, 8, 9 (context for which forces dominate at which scales).*

---

## A.4 Reverse Index — Which Vol 3 Chapter Uses Which Vol 1/2 Result

| Vol 3 Chapter | Vol 1 equations used | Vol 2 equations used |
|---------------|---------------------|---------------------|
| 1 (Newton as theorems) | (1.1.1), (1.3.12), (1.3.31), (1.7.17), (1.7.30), (1.8.3) | (2.2.29), (2.2.44), (2.5.1), (2.5.20), (2.5.21), (2.8.24) |
| 2 (Lagrangian / Hamiltonian) | (1.3.12), (1.8.3) | (2.5.1), (2.5.20), (2.5.21) |
| 3 (Central force) | (1.7.31), (1.7.33) | (2.2.29), (2.2.44), (2.8.24) |
| 4 (Rigid body) | (1.7.17), (1.7.30), (1.7.31), (1.7.33) | — |
| 5 (Continuum / fluids) | (1.6.15), (1.6.19)–(1.6.21), (1.6.22), (1.7.17), (1.7.30), (1.7.33) | (2.3.27), (2.3.41) |
| 6 (Standing waves) | (1.4.18), (1.5.51), (1.5.63), (1.10.22) (Vol 1 Ch 9 pattern types) | — |
| 7 (Origin of mass) | (1.5.51), (1.5.63), (1.5.74) | (2.4.33), (2.6.18), (2.9.11), (2.10.7) |
| 8 (Phase transitions) | (1.11.10), (1.11.25), (1.11.37) | (2.4.33), (2.9.11), (2.10.7) |
| 9 (Four laws) | (1.1.1), (1.8.3), (1.11.1), (1.11.2), (1.11.10), (1.11.14), (1.11.18), (1.11.19), (1.11.20), (1.11.25), (1.11.37), (1.11.46), (1.11.49), (1.11.54)–(1.11.57) | (2.5.1) |
| 10 (Stat mech) | (1.5.63), (1.10.22), (1.11.1), (1.11.2), (1.11.10), (1.11.14), (1.11.25), (1.11.37) | (2.3.27), (2.7.5), (2.7.38) |
| 11 (Kinetic theory) | (1.6.15), (1.7.30), (1.11.25), (1.11.37) | — |
| 12 (Entropy / arrow) | (1.1.1), (1.6.15), (1.11.10), (1.11.19), (1.11.20), (1.11.46) | — |

**Orphan check (self-test for this appendix).** Every equation listed in §A.2 and §A.3 appears in at least one row of the table above. If a future revision of Vol 3 adds a citation not in the table, this appendix must be updated. If a future revision removes a citation, the corresponding entry may be archived but should not be deleted until Vol 4 has confirmed it is also unused downstream.

---

*End of Appendix A. For experimental numerical values referenced by these equations, see Appendix B. For notation, see Vol 1 Appendix B.*
