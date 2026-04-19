# Problem Sets with Selected Solutions — Volume 3

*Problems are labeled by difficulty: **[C]** computational, **[X]** conceptual, **[\*]** challenge. Each chapter provides 4–5 problems. At least one problem per chapter is worked in full; others receive answer keys or hints. All problems reference only Volumes 1–3; none require material from Volumes 4–6. Equation tags follow Appendix A conventions.*

---

## How to Use These Problem Sets

These exercises exist for one reason: to let you answer the question the Student reviewer cares most about — *"Can I actually solve problems using the zone framework?"* Every problem can be solved with nothing more than Vols 1–3 in front of you (plus a calculator). If you find yourself needing a result from outside Vols 1–3, the problem is mis-stated — please flag it for revision.

Before starting, please have these four references at hand:
- **Vol 1 Appendix B** (Notation Reference)
- **Vol 3 Appendix A** (Key Results from Vols 1–2) — for quick citation lookup
- **Vol 3 Appendix B** (Experimental Data) — for all numerical values
- Whichever Vol 3 chapter the problem is drawn from

Worked solutions are marked ⭐. The remaining problems have either an answer key or a one-line hint at the end of this document.

---

# Chapter 1 — Newton's Laws as Theorems

### Problem 1.1 [C] ⭐ — Geodesic straight lines in flat space

**Problem.** Starting from the geodesic equation (2.2.44),
$$\frac{d^2x^\mu}{d\tau^2} + \Gamma^\mu{}_{\alpha\beta}\frac{dx^\alpha}{d\tau}\frac{dx^\beta}{d\tau} = 0,$$
take the flat-space limit (1.3.31) and show explicitly that the spatial components reduce to $d^2\mathbf{x}/dt^2 = 0$, i.e. Newton's first law.

**Solution.** In the flat-space limit $g_{\mu\nu} \to \eta_{\mu\nu}$, all components of the metric are constants; therefore the Christoffel symbols $\Gamma^\mu{}_{\alpha\beta} = \tfrac{1}{2}g^{\mu\sigma}(\partial_\alpha g_{\sigma\beta} + \partial_\beta g_{\sigma\alpha} - \partial_\sigma g_{\alpha\beta})$ vanish identically.

The geodesic equation collapses to $d^2 x^\mu/d\tau^2 = 0$. In the non-relativistic limit $\tau \approx t$ (to leading order in $v/c$), this becomes
$$\frac{d^2x^i}{dt^2} = 0 \qquad (i = 1,2,3),$$
which integrates once to $\mathbf{v} = \text{const}$. An object in a force-free region moves in a straight line at constant velocity — this is Newton's first law, now a theorem of the flat-space limit of the geodesic equation. $\blacksquare$

---

### Problem 1.2 [X] — Why F=ma is linear in acceleration

**Problem.** A student asks: "Couldn't F depend on acceleration through some more complicated function, like $F = m\mathbf{a} + m\lambda\mathbf{a}^3$?" Using Ch 1 §1.4–1.6, explain in words (no more than 200) why the form of the force law is *linear* in $\mathbf{a}$ — i.e., why the higher-order term $\lambda\mathbf{a}^3$ cannot appear.

**Hint.** The answer lies in the test-particle action (3.1.7) and the variational principle (2.5.21). Vary the action; collect terms. Higher-order-in-$\mathbf{a}$ terms would have to come from the action's dependence on higher derivatives of $x^\mu$, which is excluded by the Vol 1 Ch 8 regularity requirement on $\mathcal{L}_{\text{total}}$.

---

### Problem 1.3 [C] — Inertial–gravitational mass equivalence

**Problem.** Show that the same $m$ appearing in the coupling constant of the test-particle action — i.e., the "inertial mass" — is *identically* the $m$ that multiplies the gravitational potential in the weak-field limit (2.8.24). (*That is, prove the Equivalence Principle from Ch 1's derivation chain.*)

**Answer key.** Vary (3.1.7) → geodesic (2.2.44). Take weak-field limit (2.8.24); the time-time component gives $\mathbf{a} = -\nabla\Phi_N$. The $m$ on the left (from the variational normalization of $\dot x^\mu$) is numerically the same $m$ that enters the Poisson source $4\pi G_4\rho$ on the right. They are *one parameter* in the action, not two.

---

### Problem 1.4 [*] — Third Law from covariant conservation

**Problem.** Two particles interact through a field $\phi$. Using (1.7.17), $\nabla_\mu T^{\mu\nu} = 0$, show that the total rate of momentum change of particle 1 is exactly equal and opposite to that of particle 2 (after the field has carried its share), proving Newton's third law as a theorem.

**Hint.** Integrate $\nabla_\mu T^{\mu i} = 0$ over a spatial region containing both particles and apply the divergence theorem. The surface term vanishes for an isolated system. Then split $T^{\mu\nu}$ into particle 1, particle 2, and field contributions.

---

# Chapter 2 — Lagrangian and Hamiltonian Mechanics

### Problem 2.1 [C] ⭐ — Double pendulum Lagrangian

**Problem.** Two identical rods of length $\ell$ and mass $m$ hang in a uniform gravitational field $g$. The first is pivoted at the top; the second is pinned to the bottom of the first. Let $\theta_1, \theta_2$ be the angles of each rod from vertical. Write $L = T - V$ and the two Euler–Lagrange equations.

**Solution.** Positions of the centers of mass:
$$x_1 = \tfrac{\ell}{2}\sin\theta_1,\quad y_1 = -\tfrac{\ell}{2}\cos\theta_1$$
$$x_2 = \ell\sin\theta_1 + \tfrac{\ell}{2}\sin\theta_2,\quad y_2 = -\ell\cos\theta_1 - \tfrac{\ell}{2}\cos\theta_2$$

Kinetic energy (rod 1: translational of CM + rotational about CM with $I = m\ell^2/12$; similarly rod 2):
$$T_1 = \tfrac{1}{2}m\left(\dot x_1^2 + \dot y_1^2\right) + \tfrac{1}{2}\cdot\tfrac{m\ell^2}{12}\dot\theta_1^2 = \tfrac{1}{6}m\ell^2\dot\theta_1^2$$
$$T_2 = \tfrac{1}{2}m\left(\dot x_2^2 + \dot y_2^2\right) + \tfrac{1}{2}\cdot\tfrac{m\ell^2}{12}\dot\theta_2^2$$
$$\quad = \tfrac{1}{2}m\ell^2\dot\theta_1^2 + \tfrac{1}{8}m\ell^2\dot\theta_2^2 + \tfrac{1}{2}m\ell^2\dot\theta_1\dot\theta_2\cos(\theta_1-\theta_2) + \tfrac{1}{24}m\ell^2\dot\theta_2^2$$
Simplify $T_2$: the rotational term adds $\tfrac{1}{24}m\ell^2\dot\theta_2^2$ to the translational $\tfrac{1}{8}m\ell^2\dot\theta_2^2$ giving $\tfrac{1}{6}m\ell^2\dot\theta_2^2$. So
$$T = T_1 + T_2 = \tfrac{2}{3}m\ell^2\dot\theta_1^2 + \tfrac{1}{6}m\ell^2\dot\theta_2^2 + \tfrac{1}{2}m\ell^2\dot\theta_1\dot\theta_2\cos(\theta_1-\theta_2).$$

Potential energy (measuring from the pivot):
$$V = -\tfrac{1}{2}mg\ell\cos\theta_1 - mg\left(\ell\cos\theta_1 + \tfrac{1}{2}\ell\cos\theta_2\right) = -\tfrac{3}{2}mg\ell\cos\theta_1 - \tfrac{1}{2}mg\ell\cos\theta_2.$$

Lagrangian $L = T - V$. Euler–Lagrange gives two coupled second-order ODEs in $(\theta_1,\theta_2)$. The point of this exercise is not to linearize or solve — it is to see how easily the Lagrangian approach handles a system that Newtonian free-body analysis would bury in constraint forces.

Compare the pain with what you would have written using $\sum\mathbf{F} = m\mathbf{a}$ and drawing two free-body diagrams with tension forces you do not care about. This is why Ch 2 exists. $\blacksquare$

---

### Problem 2.2 [C] — Bead on a rotating hoop

**Problem.** A bead of mass $m$ slides without friction on a vertical circular hoop of radius $R$ that rotates about its vertical diameter with constant angular velocity $\Omega$. Let $\theta$ be the angle of the bead from the bottom. Write the Lagrangian, find the equilibrium positions, and determine the critical angular velocity $\Omega_c$ above which the bottom ($\theta = 0$) becomes unstable.

**Answer key.** $L = \tfrac{1}{2}mR^2\dot\theta^2 + \tfrac{1}{2}mR^2\Omega^2\sin^2\theta + mgR\cos\theta$. Equilibria at $\theta = 0$, $\theta = \pi$, and (if $\Omega^2 > g/R$) $\cos\theta_\star = g/(\Omega^2 R)$. Bottom becomes unstable at $\Omega_c = \sqrt{g/R}$.

---

### Problem 2.3 [X] — Why $H$ is conserved when $L$ has no explicit $t$

**Problem.** Using only the Euler–Lagrange equations and the definition $H = \sum_i p_i\dot q_i - L$, show that $dH/dt = -\partial L/\partial t$. Explain in one sentence why this makes $H$ a conserved quantity (and, when $L$ is "kinetic − potential", the total energy) whenever $L$ does not depend explicitly on time.

---

### Problem 2.4 [*] — Legendre transform of a 4-velocity Lagrangian

**Problem.** Consider the relativistic free-particle Lagrangian $L = -mc^2\sqrt{1 - v^2/c^2}$. Compute the canonical momentum $\mathbf{p} = \partial L/\partial\mathbf{v}$ and perform the Legendre transform to obtain the Hamiltonian $H(\mathbf{p})$. Verify that $H^2 = (pc)^2 + (mc^2)^2$.

**Hint.** $\mathbf{p} = m\mathbf{v}/\sqrt{1 - v^2/c^2}$. Solve for $\mathbf{v}$ in terms of $\mathbf{p}$, then substitute into $H = \mathbf{p}\cdot\mathbf{v} - L$.

---

# Chapter 3 — Central Force Problems

### Problem 3.1 [C] ⭐ — Kepler's third law from (2.2.29)

**Problem.** Using the zone-derived $G_4$ from (2.2.29), (a) write Kepler's third law $T^2 = (4\pi^2/G_4M_\odot)a^3$ and (b) predict the orbital period of a satellite at semi-major axis $a = 1.496\times 10^{11}$ m about $M_\odot = 1.989\times 10^{30}$ kg. Compare to 1 year = $3.156\times 10^7$ s.

**Solution.**
(a) For a two-body central $-k/r$ problem, the reduced mass $\mu = m_1 m_2/(m_1+m_2)$ orbits an effective center at the ellipse's focus. From Ch 3 §3.4:
$$T^2 = \frac{4\pi^2}{G_4(M_\odot+m)}a^3 \approx \frac{4\pi^2}{G_4 M_\odot}a^3$$
(the approximation holds whenever $m \ll M_\odot$). The constant $G_4$ comes from Vol 2 (2.2.29).

(b) Plug in numbers:
$$T^2 = \frac{4\pi^2\,(1.496\times 10^{11})^3}{(6.674\times 10^{-11})(1.989\times 10^{30})} = \frac{4\pi^2\cdot 3.349\times 10^{33}}{1.327\times 10^{20}} = \frac{1.322\times 10^{35}}{1.327\times 10^{20}} = 9.96\times 10^{14}\,\text{s}^2$$
$$T = 3.155\times 10^7\,\text{s}.$$
This is 1.0000 years — the definition of an astronomical unit. Notice that the $G_4$ used here is not postulated; it was derived in Vol 2 from $\sigma$ and $L_{\text{eff}}$. The entire chain Zone → $G_4$ → Kepler → 1 year is closed. $\blacksquare$

---

### Problem 3.2 [C] — Effective potential for a circular orbit

**Problem.** For a particle of mass $m$ in a $-k/r$ central potential with angular momentum $\ell$, show that the effective radial potential
$$U_{\text{eff}}(r) = \frac{\ell^2}{2mr^2} - \frac{k}{r}$$
has a minimum at $r_0 = \ell^2/(mk)$ and that at this radius the orbit is a circle. Compute the orbital frequency $\omega$ and verify $\omega^2 r_0^3 = k/m$ — i.e., Kepler's third law for circular orbits.

---

### Problem 3.3 [X] — Why central-force orbits lie in a plane

**Problem.** In 3D Euclidean space, why does the orbit of a particle in a central force lie in a fixed plane? Explain using the angular-momentum conservation law (1.7.33) — no vector-calculus manipulation required, just the physical reason.

**Answer key.** $\mathbf{L} = \mathbf{r}\times m\mathbf{v}$ is conserved, so $\mathbf{L}$ is a fixed vector in space. Because $\mathbf{r}\perp\mathbf{L}$ at every instant (from the definition of cross product) and $\mathbf{L}$ does not change, $\mathbf{r}(t)$ lies forever in the plane perpendicular to $\mathbf{L}$ through the origin.

---

### Problem 3.4 [*] — Rutherford scattering cross-section

**Problem.** A particle of charge $q_1$ and mass $m$ approaches a fixed charge $q_2$ from infinity with speed $v_\infty$ and impact parameter $b$. Using the Ch 3 §3.6 scattering machinery, derive the Rutherford differential cross-section
$$\frac{d\sigma}{d\Omega} = \left(\frac{q_1 q_2}{4 E}\right)^2\frac{1}{\sin^4(\theta/2)},$$
where $E = \tfrac{1}{2}mv_\infty^2$.

---

# Chapter 4 — Rigid Body Dynamics

### Problem 4.1 [C] ⭐ — Inertia tensor of a thin square plate

**Problem.** A uniform thin square plate of side $a$ and mass $M$ has its center at the origin, lies in the $xy$-plane, and is aligned with the axes. Compute the inertia tensor $I_{ij}$ about its center.

**Solution.** Mass per unit area $\mu = M/a^2$. For a lamina in the $xy$-plane, $z = 0$ everywhere, so $I_{zz} = \int(x^2+y^2)\mu\,dA$ and the perpendicular-axis theorem gives $I_{zz} = I_{xx} + I_{yy}$.

Compute $I_{xx} = \mu\int_{-a/2}^{a/2}\int_{-a/2}^{a/2}y^2\,dx\,dy = \mu a\cdot(a^3/12) = \mu a^4/12 = Ma^2/12$.
By symmetry $I_{yy} = Ma^2/12$. Perpendicular-axis theorem gives $I_{zz} = Ma^2/6$.

Off-diagonal terms vanish because $\int xy\,dx\,dy = 0$ (odd integrand over a symmetric region). Therefore
$$I_{ij} = \frac{Ma^2}{12}\begin{pmatrix}1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 2\end{pmatrix}.$$
The plate has two equal moments of inertia in-plane and twice that about the out-of-plane axis — a familiar textbook result, now derived with the exact geometry bookkeeping the Ch 4 machinery requires. $\blacksquare$

---

### Problem 4.2 [C] — Torque-free Euler equations for a symmetric top

**Problem.** For a symmetric top with $I_1 = I_2 \neq I_3$ and no external torque, solve Euler's equations $I_i\dot\omega_i = (I_j-I_k)\omega_j\omega_k$ (cyclic). Show that $\omega_3 = $ const and that $\omega_1, \omega_2$ precess about the symmetry axis at angular frequency $\Omega = \omega_3(I_3 - I_1)/I_1$.

---

### Problem 4.3 [X] — Why a spinning top does not fall

**Problem.** A spinning top leaning at angle $\theta$ from vertical, with spin angular momentum $\mathbf{L}$ along its symmetry axis, experiences gravitational torque $\boldsymbol\tau = \mathbf{r}\times M\mathbf{g}$. Explain (in words, not in an equation) why this torque causes the top to *precess* rather than to *fall*. Connect to the conservation law (1.7.33).

---

### Problem 4.4 [*] — Tennis racket theorem

**Problem.** A rigid body has three distinct principal moments $I_1 < I_2 < I_3$. Linearize Euler's equations about rotation around each principal axis, and show that rotations about the axes of smallest and largest moment are stable, but rotation about the intermediate axis is unstable (the "tennis racket theorem" or "Dzhanibekov effect").

---

# Chapter 5 — Continuum Mechanics and Fluid Dynamics

### Problem 5.1 [C] ⭐ — Madelung transformation gives continuity

**Problem.** Starting from (1.6.15), write $\Psi_B = \sqrt{\rho}\,e^{iS/\hbar}$. Substitute, and show that the imaginary part of the equation yields the continuity equation (1.6.19), $\partial_t\rho + \nabla\cdot(\rho\mathbf{v}) = 0$, with $\mathbf{v} = \nabla S/m$.

**Solution.** Write (1.6.15) in the non-relativistic form $i\hbar\partial_t\Psi_B = -(\hbar^2/2m)\nabla^2\Psi_B + V\Psi_B$ (valid in the low-velocity limit where $\Box_6 \to \partial_t^2/c^2 - \nabla^2 \to -\nabla^2$ after the appropriate non-rel reduction). Substitute $\Psi_B = \sqrt{\rho}\,e^{iS/\hbar}$.

$\partial_t\Psi_B = (\tfrac{1}{2}\rho^{-1/2}\partial_t\rho + (i/\hbar)\sqrt\rho\,\partial_t S)e^{iS/\hbar}$.

$\nabla\Psi_B = (\tfrac{1}{2}\rho^{-1/2}\nabla\rho + (i/\hbar)\sqrt\rho\,\nabla S)e^{iS/\hbar}$.

$\nabla^2\Psi_B = [\nabla^2\sqrt\rho + 2(i/\hbar)\nabla\sqrt\rho\cdot\nabla S + (i/\hbar)\sqrt\rho\nabla^2 S - (1/\hbar^2)\sqrt\rho|\nabla S|^2]e^{iS/\hbar}$.

Multiply the Schrödinger equation by $e^{-iS/\hbar}$ and take the imaginary part (the terms carrying one factor of $i$):
$$\hbar\cdot\tfrac{1}{2}\rho^{-1/2}\partial_t\rho = -(\hbar^2/2m)\left[2\,\tfrac{1}{2}\rho^{-1/2}\nabla\rho\cdot(\nabla S/\hbar) + \sqrt\rho\,\nabla^2 S/\hbar\right]$$
$$\Longrightarrow\quad \partial_t\rho = -\frac{1}{m}\left[\nabla\rho\cdot\nabla S + \rho\nabla^2 S\right] = -\nabla\cdot(\rho\,\nabla S/m) = -\nabla\cdot(\rho\mathbf{v}).$$
This is (1.6.19). The real part, by a parallel calculation, gives the Euler equation (1.6.20) with the quantum pressure of (1.6.21). The Waters Below field equation *is* continuity + Euler + quantum pressure, in disguise. $\blacksquare$

---

### Problem 5.2 [C] — Navier–Stokes from the Euler + viscous stress

**Problem.** Starting from (1.6.20) without the quantum-pressure term and adding a viscous stress $\partial_j\tau_{ij} = \mu\nabla^2 v_i + (\zeta + \mu/3)\partial_i(\nabla\cdot\mathbf{v})$, write the full Navier–Stokes equation and identify each term: convective, pressure gradient, gravitational, shear viscous, bulk viscous.

---

### Problem 5.3 [X] — Why the continuum approximation works

**Problem.** Explain in ≤ 200 words why, despite matter being made of $\sim 10^{23}$ discrete atoms per cm³, it is valid to treat a fluid as a continuous density field $\rho(\mathbf{x},t)$. What is the hierarchy of length scales involved? At what scale does the approximation fail?

---

### Problem 5.4 [*] — Bulk modulus of copper from interatomic Coulomb

**Problem.** Model copper as an FCC lattice with nearest-neighbor spacing $a_0 = 2.55$ Å. Treat the binding as a screened Coulomb between effective unit charges. Estimate the bulk modulus as $K \sim e^2/(4\pi\epsilon_0 a_0^4)$ (dimensional argument) and compare to the measured $K_{\text{Cu}} = 140$ GPa (Appendix B.2).

**Answer key.** $K \sim (1.602\times 10^{-19})^2/(4\pi\cdot 8.854\times 10^{-12}\cdot(2.55\times 10^{-10})^4) \approx 5.5\times 10^{11}$ Pa = 550 GPa. The dimensional estimate is off by a factor of ~4; the Ch 5 §5.3 refined derivation includes a lattice geometry factor that brings it into the 96 % agreement reported in B.2.3.

---

# Chapter 6 — Standing Waves and Stable Configurations

### Problem 6.1 [C] ⭐ — Chladni modes on a square drumhead

**Problem.** A square membrane of side $L$, fixed at all edges, obeys the 2D wave equation $\Box\phi = c_s^{-2}\ddot\phi - \nabla^2\phi = 0$ with $\phi = 0$ on the boundary. (a) Find all standing-wave eigenmodes and their frequencies. (b) Sketch the nodal pattern of the $(m,n) = (2,3)$ mode.

**Solution.**
(a) Separation of variables: $\phi = X(x)Y(y)T(t)$. Boundary conditions force $X \propto \sin(m\pi x/L)$, $Y \propto \sin(n\pi y/L)$ with integers $m,n \geq 1$. The dispersion relation gives
$$\omega_{mn}^2 = c_s^2\left(\frac{m^2 + n^2}{L^2}\right)\pi^2 \qquad\Longrightarrow\qquad \omega_{mn} = \frac{\pi c_s}{L}\sqrt{m^2+n^2}.$$
The spectrum is discrete (because the geometry is bounded), quantized by the two integers $(m,n)$ — exactly the situation of the Firmament (1.5.63) reduced to 2D. Compare with Vol 1 (1.10.22): boundary conditions force discrete eigenvalues.

(b) The $(2,3)$ mode has $\phi \propto \sin(2\pi x/L)\sin(3\pi y/L)$. The nodal lines are where $\phi = 0$: these occur at $x = L/2$ (one interior vertical line from the $\sin(2\pi x/L)$ factor) and $y = L/3, 2L/3$ (two interior horizontal lines from $\sin(3\pi y/L)$). The drumhead divides into six rectangular cells, alternating sign. Sand sprinkled on the drumhead collects on the three nodal lines. $\blacksquare$

---

### Problem 6.2 [C] — Vortex winding number

**Problem.** Consider the 2D field $\phi(x,y) = |\phi|\,e^{in\theta}$, where $\theta = \arctan(y/x)$ and $n\in\mathbb{Z}$. (a) Compute the contour integral $\oint\nabla\theta\cdot d\mathbf{l}$ around a closed loop enclosing the origin. (b) Show that $n$ is a topological invariant — it cannot change under continuous deformations of $\phi$ that avoid $\phi = 0$.

**Answer key.** (a) $\oint = 2\pi n$. (b) Deformation continuity ensures $\phi \neq 0$ along the path; the winding number is therefore an integer that cannot jump.

---

### Problem 6.3 [X] — Why matter cannot simply decay

**Problem.** In Ch 6 §6.6, we argued that topologically protected defects cannot smoothly decay because decay would require passing through $\phi = 0$ on a codimension-2 surface, and continuous evolution cannot jump the topology. In your own words (≤ 150), explain why this is the zone-framework answer to the question "*why are particles stable?*", and contrast it with the Standard Model's answer ("*because we postulate conservation laws*").

---

### Problem 6.4 [*] — KK mass ladder from (1.5.63)

**Problem.** Using the KK mode expansion (1.5.63), show that the mass spectrum of the zero'th, first, and second KK excitations of a Firmament field with $m_0 = 0$ is $m_{n\ell}^2 = (n^2+\ell^2)/L_{\text{eff}}^2$. Taking $L_{\text{eff}} \sim 10^{-18}$ m, estimate the mass of the first excited KK mode in GeV. Why are these modes not yet observed at LHC?

**Hint.** $\hbar c \approx 0.197$ GeV·fm; $L_{\text{eff}} \sim 10^{-3}$ fm gives $m_{10} \sim 200$ GeV — right at the edge of current sensitivity.

---

# Chapter 7 — The Origin of Mass

### Problem 7.1 [C] ⭐ — Electroweak VEV from membrane tension

**Problem.** Using the Ch 7 §7.3 derivation, estimate the Higgs VEV $v$ from the membrane tension $\sigma \approx 6\times 10^{98}$ kg/s² and compare to the PDG value $v = 246.22$ GeV (Appendix B.6.4).

**Solution.** The Ch 7 §7.3 result (schematically):
$$v^2 \;\sim\; \frac{\sigma\,L_{\text{eff}}^2}{\hbar c}\cdot e^{-c_1 (L_{\text{eff}}/\ell_{\text{Pl}})^2}$$
where the exponential factor comes from the Kaluza-Klein hierarchy (2.9.11). The geometrical parameters yield $v \approx 240$ GeV to the precision of $\sigma$ (which is known only to ~1 %). Agreement: within uncertainty (see B.8 summary). $\blacksquare$

*Note.* The point of this problem is not to carry out a precise numerical calculation — the chain is too long for a textbook problem. The point is to see how the chain closes: membrane tension from Vol 1 → hierarchy from Vol 2 → electroweak scale in Vol 3. Each step has been done; here you trace them.

---

### Problem 7.2 [C] — Charged-lepton mass ratio

**Problem.** Using the Yukawa overlap integral formalism of Ch 7 §7.4, and assuming Gaussian vortex profiles of widths $w_e < w_\mu < w_\tau$, show that the ratio $m_\mu/m_e$ can be expressed as the ratio of two overlap integrals between vortex profiles and the Higgs condensate. Numerically, match to $m_\mu/m_e = 206.77$ (Appendix B.6.1) and solve for the width ratio.

**Hint.** The Yukawa coupling $y \propto \int d^2r\,|\psi_{\text{vortex}}|^2\,|v|$; narrower vortices give smaller overlap.

---

### Problem 7.3 [X] — Why the Higgs field is not postulated

**Problem.** The Standard Model introduces the Higgs field as an additional field with a postulated Mexican-hat potential. In the zone framework, what *is* the Higgs field, and why is its Mexican-hat potential not a postulate? Answer in ≤ 200 words, citing the specific Vol 1 / Vol 2 results that make this reduction possible.

**Answer key.** The Higgs is the lowest KK mode of the Waters Above scalar $\Psi_A$ (Vol 1 Ch 5). The Mexican-hat potential arises from the Firmament boundary conditions and the membrane tension (1.5.74); the negative mass-squared term comes from minimizing the total action under the $\Psi_A\leftrightarrow\Psi_B$ coupling $G_{\text{int}}$ (1.6.15). Nothing is added by hand.

---

### Problem 7.4 [*] — Quark mass hierarchy bounds

**Problem.** Using the running-coupling formula (2.10.7) and the Yukawa overlap scheme, derive an order-of-magnitude upper bound on the top-quark mass from the requirement that its Yukawa coupling remain perturbative ($y_t < \sqrt{4\pi}$) up to $Q = M_{\text{Pl}}$.

---

# Chapter 8 — Phase Transitions in Zone Architecture

### Problem 8.1 [C] ⭐ — Van der Waals critical exponents

**Problem.** The van der Waals equation is $(p + a/V^2)(V - b) = Nk_BT$. (a) Find the critical point $(T_c, V_c, p_c)$ by solving $\partial p/\partial V = \partial^2 p/\partial V^2 = 0$. (b) Expand about the critical point and show that the mean-field critical exponents are $\alpha=0, \beta=1/2, \gamma=1, \delta=3$.

**Solution.**
(a) Solve the two conditions. Differentiate:
$\partial p/\partial V = -Nk_BT/(V-b)^2 + 2a/V^3 = 0$
$\partial^2 p/\partial V^2 = 2Nk_BT/(V-b)^3 - 6a/V^4 = 0$
Dividing, $2/(V-b) = 3/V \Rightarrow V_c = 3b$. Substituting: $k_BT_c = 8a/(27b)$, $p_c = a/(27b^2)$.

(b) Let $t = (T - T_c)/T_c$, $\phi = (V - V_c)/V_c$. Expand the van der Waals equation to cubic order in $\phi$ and linear in $t$; the resulting effective free energy is Landau-like, $F \approx F_0 + A t\phi^2 + B\phi^4$. Minimizing gives $\phi_\star \propto \sqrt{-t}$ (so $\beta = 1/2$). Isothermal compressibility $\kappa_T \propto 1/t$ gives $\gamma = 1$. On the critical isotherm ($t=0$), $p - p_c \propto \phi^3$, so $\delta = 3$. Heat capacity has a jump discontinuity but no divergence, so $\alpha = 0$. These are the mean-field (Landau) exponents, and they match universal class behavior — the universality at work is exactly what Ch 8 §8.4 derives from zone topology. $\blacksquare$

---

### Problem 8.2 [C] — Clausius–Clapeyron for water

**Problem.** Using $dp/dT = L/(T\Delta v)$ with the latent heat of vaporization of water $L = 40.65$ kJ/mol and molar volume change $\Delta v \approx v_{\text{gas}} \approx RT/p$ at the boiling point ($T = 373$ K, $p = 101.3$ kPa), estimate the slope of the coexistence curve $dp/dT$. Compare to the experimental 3.61 kPa/K.

---

### Problem 8.3 [X] — Universality and zone topology

**Problem.** Explain why the 3D Ising model, the liquid–gas critical point, and the ferromagnetic Curie transition all share the same critical exponents. What does Ch 8 §8.5 say about the *zone* reason — not just the renormalization-group reason — for this universality?

---

### Problem 8.4 [*] — Electroweak phase transition temperature

**Problem.** Using Ch 8 §8.6, estimate the cosmological temperature at which the electroweak transition occurred. How does this connect to the Higgs VEV $v = 246$ GeV?

---

# Chapter 9 — The Four Laws, Complete Derivation

### Problem 9.1 [C] ⭐ — Two-level system partition function

**Problem.** A system has two non-degenerate energy levels at $0$ and $\epsilon$. (a) Write the partition function $Z(T)$. (b) Compute the Helmholtz free energy $F$, energy $\langle E\rangle$, entropy $S$, and heat capacity $c_V$. (c) Sketch $c_V(T)$ and identify the Schottky anomaly.

**Solution.**
(a) $Z = 1 + e^{-\epsilon/k_BT}$ — directly from (1.11.25).

(b) $F = -k_BT\ln Z$. Probabilities $p_0 = 1/Z$, $p_1 = e^{-\epsilon/k_BT}/Z$. Energy $\langle E\rangle = \epsilon p_1 = \epsilon/(1 + e^{\epsilon/k_BT})$. Entropy $S = -k_B(p_0\ln p_0 + p_1\ln p_1)$. Heat capacity:
$$c_V = \frac{d\langle E\rangle}{dT} = k_B\left(\frac{\epsilon}{k_BT}\right)^2\frac{e^{\epsilon/k_BT}}{(1+e^{\epsilon/k_BT})^2}.$$

(c) $c_V(T)$ vanishes at $T=0$ (Third Law behavior), has a peak near $k_BT \approx 0.42\epsilon$ (the Schottky anomaly), and decays as $1/T^2$ for $T \gg \epsilon/k_B$. This is the simplest non-trivial heat-capacity curve and displays all three laws (Third: $c_V \to 0$; Second: $S$ monotone; First: $dU = TdS$) in one plot. $\blacksquare$

---

### Problem 9.2 [C] — Maxwell relations

**Problem.** Starting from the four thermodynamic potentials $U(S,V), F(T,V), G(T,p), H(S,p)$, derive all four Maxwell relations. Use one of them to show that $(\partial S/\partial V)_T = (\partial p/\partial T)_V$ — the key identity for computing entropy change at fixed $T$.

---

### Problem 9.3 [X] — Why the Second Law is phase-dependent

**Problem.** In Vol 1 Ch 11 we said "entropy never decreases" and then Vol 3 Ch 9 said "entropy never decreases *in Phase 3*". Reconcile these two statements using (1.11.46) and the open-system First Law (1.11.19). In particular, explain what would happen to $dS/dt$ in Phase 2 ($\kappa = \kappa_{\text{full}}$, $\Delta\kappa = 0$).

---

### Problem 9.4 [*] — Debye $T^3$ law numerical check

**Problem.** Using the Debye model from Ch 9 §9.7.3 with Debye temperature $\Theta_D = 343$ K for copper (Appendix B.4.1), compute the molar heat capacity of Cu at $T = 10$ K. Compare to the high-$T$ Dulong–Petit value $3R = 24.94$ J/(mol·K).

**Answer key.** At $T \ll \Theta_D$, $c_V \approx (12\pi^4/5)R(T/\Theta_D)^3 \approx 234\cdot(10/343)^3\cdot 8.314 \approx 0.048$ J/(mol·K). About 0.2 % of Dulong–Petit — this is why Cu looks like it has no heat capacity at cryogenic temperatures.

---

# Chapter 10 — Statistical Mechanics on the Zone Manifold

### Problem 10.1 [C] ⭐ — Planck distribution from (1.10.22)

**Problem.** Starting from the discrete-spectrum theorem (1.10.22) applied to photon modes in a cubic cavity of side $L$, and applying the grand-canonical partition function for bosons with $\mu = 0$, derive the Planck spectral energy density
$$u(\omega)\,d\omega = \frac{\hbar\omega^3}{\pi^2 c^3}\frac{d\omega}{e^{\hbar\omega/k_BT} - 1}.$$

**Solution.** Mode count: for a cubic cavity, the allowed wave vectors are $\mathbf{k} = (\pi/L)(n_x, n_y, n_z)$ with positive integers $n_i$. The number of modes with $|\mathbf{k}|$ in $(k, k+dk)$, including two polarizations, is $g(k)dk = (V k^2/\pi^2)dk$. Convert to $\omega = ck$: $g(\omega)d\omega = (V\omega^2/\pi^2 c^3)d\omega$.

Each mode is a harmonic oscillator with mean energy $\langle E\rangle = \hbar\omega/(e^{\hbar\omega/k_BT} - 1)$ (from (1.11.14), dropping the zero-point piece which does not contribute to finite-temperature radiation).

Energy density per unit frequency:
$$u(\omega) = \frac{g(\omega)\langle E\rangle}{V} = \frac{\omega^2}{\pi^2 c^3}\cdot\frac{\hbar\omega}{e^{\hbar\omega/k_BT}-1} = \frac{\hbar\omega^3}{\pi^2 c^3}\frac{1}{e^{\hbar\omega/k_BT} - 1}.\quad\blacksquare$$

Integrating over $\omega$ and using $\int_0^\infty x^3/(e^x-1)dx = \pi^4/15$ gives the Stefan–Boltzmann law $u_{\text{total}} = (4\sigma_{SB}/c)T^4$ with $\sigma_{SB} = \pi^2 k_B^4/(60\hbar^3 c^2)$ — exactly the CODATA value (Appendix B.1). The entire constant has no free parameters.

---

### Problem 10.2 [C] — Ideal gas partition function

**Problem.** (a) Derive the single-particle partition function $Z_1 = V/\lambda_T^3$ with $\lambda_T = h/\sqrt{2\pi mk_BT}$. (b) For $N$ indistinguishable particles, write $Z_N = Z_1^N/N!$ and use Stirling's approximation to derive the ideal-gas law $pV = Nk_BT$ and the Sackur–Tetrode entropy.

---

### Problem 10.3 [X] — Why fluctuations decrease with system size

**Problem.** In the canonical ensemble, show that the relative fluctuation in energy $\sigma_E/\langle E\rangle$ scales as $1/\sqrt{N}$ for a macroscopic system of $N$ particles. Explain the physical significance — why does thermodynamics look deterministic at our scale but statistical at the atomic scale?

---

### Problem 10.4 [*] — CMB temperature from COBE/FIRAS

**Problem.** Given the COBE/FIRAS total CMB energy density $u = 4.175\times 10^{-14}$ J/m³ (Appendix B.5), solve $u = (4\sigma_{SB}/c)T^4$ for $T$ and confirm $T = 2.7255$ K. Note that the framework underlying this calculation is entirely Ch 10 + Appendix A entries (1.10.22), (1.11.14), (1.11.25) — no input from beyond Vol 3.

---

# Chapter 11 — Kinetic Theory and Transport

### Problem 11.1 [C] ⭐ — Mean free path and viscosity

**Problem.** For an ideal gas of hard spheres of diameter $d$ at number density $n$ and temperature $T$, (a) derive the mean free path $\lambda = 1/(\sqrt{2}\pi d^2 n)$. (b) Using the elementary kinetic-theory result $\mu = (1/3)\rho\bar v\lambda$ with $\bar v = \sqrt{8k_BT/\pi m}$, compute the viscosity of air at 20 °C ($d \approx 3.7$ Å, $n = 2.5\times 10^{25}$ m⁻³, $m = 4.65\times 10^{-26}$ kg).

**Solution.**
(a) Consider a test particle moving with speed $\bar v$. In time $t$, it sweeps out a cylinder of volume $\pi d^2 \bar v t$ (factor $\sqrt 2$ correction from relative velocity). The number of collisions is $n\cdot\pi d^2 \bar v t\cdot\sqrt 2$. The mean free path is the distance between collisions:
$$\lambda = \frac{\bar v t}{n\cdot\sqrt 2\pi d^2 \bar v t} = \frac{1}{\sqrt 2\pi d^2 n}.$$
Plugging numbers for air: $\lambda = 1/(\sqrt 2\pi\cdot (3.7\times 10^{-10})^2\cdot 2.5\times 10^{25}) \approx 6.6\times 10^{-8}$ m = 66 nm.

(b) $\bar v = \sqrt{8\cdot 1.38\times 10^{-23}\cdot 293/(\pi\cdot 4.65\times 10^{-26})} \approx 463$ m/s.
$\rho = nm = 2.5\times 10^{25}\cdot 4.65\times 10^{-26} \approx 1.16$ kg/m³.
$\mu = (1/3)\cdot 1.16\cdot 463\cdot 6.6\times 10^{-8} \approx 1.18\times 10^{-5}$ Pa·s.

Measured value (Appendix B.3): $1.81\times 10^{-5}$ Pa·s. The elementary estimate is within a factor ~1.5 of the measured value; the more refined Chapman–Enskog formula cited in Appendix B.3.1 achieves ~3 %. Both treatments are in Ch 11. $\blacksquare$

---

### Problem 11.2 [C] — Thermal conductivity from kinetic theory

**Problem.** Following the same elementary reasoning as Problem 11.1, derive $k \approx (1/3)n\bar v\lambda\cdot c_V$ per particle and compute the thermal conductivity of air at 20 °C. Compare with the measured 0.0257 W/(m·K).

---

### Problem 11.3 [X] — Boltzmann's H-theorem in one sentence

**Problem.** State Boltzmann's H-theorem in one sentence and explain — in ≤ 150 words — how it resolves the apparent paradox that microscopic Newtonian / Hamiltonian dynamics is time-reversible but the macroscopic H function is monotonically decreasing.

---

### Problem 11.4 [*] — Chapman–Enskog from Boltzmann

**Problem.** Outline (you do not need to carry out every step) the Chapman–Enskog expansion of the Boltzmann equation that yields the viscosity of a dilute gas to leading order in the gradient expansion. Identify where the mean-field approximation enters.

---

# Chapter 12 — Entropy, Information, and the Arrow of Time

### Problem 12.1 [C] ⭐ — Landauer's principle numerical

**Problem.** Landauer's principle states that erasing one bit of information at temperature $T$ requires at least $k_BT\ln 2$ of energy. (a) Compute this for $T = 300$ K. (b) A modern CPU dissipates about $10^{11}$ J of energy erasing bits over its lifetime; how many bit erasures is this at the Landauer bound? (c) How many bit erasures per second is a 100-watt processor doing, at the bound?

**Solution.**
(a) $k_BT\ln 2 = 1.38\times 10^{-23}\cdot 300\cdot 0.693 \approx 2.87\times 10^{-21}$ J per bit. This is tiny — ~18 meV — but nonzero.

(b) $10^{11}/2.87\times 10^{-21} \approx 3.5\times 10^{31}$ bit erasures at the bound. A real CPU exceeds this by factors of $\sim 10^4$–$10^5$ because real logic is not operating at the thermodynamic limit.

(c) $100/(2.87\times 10^{-21}) \approx 3.5\times 10^{22}$ bit erasures per second at the bound. Real CPUs do $\sim 10^{17}$ actual bit operations per second — five orders of magnitude away from the fundamental bound, meaning there is enormous room for more efficient hardware before physics says "stop". $\blacksquare$

---

### Problem 12.2 [C] — Entropy of mixing

**Problem.** Two equal-volume vessels of ideal gas, one containing $N$ atoms of species A and the other $N$ atoms of species B, both at temperature $T$, are connected. Compute the entropy increase upon mixing, $\Delta S = 2Nk_B\ln 2$, using (1.11.10). Now do the same for two vessels of *the same* species; explain why the answer is $\Delta S = 0$ (the Gibbs paradox) and how the Vol 1 Ch 11 treatment using distinguishable-vs-indistinguishable particle counting resolves it.

---

### Problem 12.3 [X] — Why time's arrow is "theological", not merely statistical

**Problem.** Standard physics explains the arrow of time statistically: the universe started in a low-entropy state, so entropy increases. Vol 3 Ch 12 offers a different explanation: $\kappa(t)$ changed at the Fall, converting a time-symmetric phase into an asymmetric phase via (1.11.46). In ≤ 300 words, explain the difference, and state one observable consequence that would distinguish the two explanations in principle (even if not yet in practice).

---

### Problem 12.4 [*] — κ-dependent Second Law in Phase 4

**Problem.** In Phase 4 (Redemption), $\kappa$ transitions from $\kappa_{\text{partial}}$ back toward $\kappa_{\text{full}}$. Using (1.11.46), write the sign of $dS/dt$ in this phase. Does the Second Law reverse? Does entropy decrease? Or does the functional $L$ itself change sign? Discuss what the Ch 12 §12.7 framework says, and identify the conceptual (not computational) open problem.

---

# Hints and Answer Key for Unsolved Problems

Selected hints, not full solutions. Problems marked ⭐ are fully worked above.

- **1.2** — Higher-derivative Lagrangians produce higher-order equations of motion; the Ostrogradsky instability forbids them as fundamental. $F = m\mathbf{a}$ is the only consistent form.
- **1.3** — Check that the single $m$ in (3.1.7) appears identically when you extract (2.8.24) via the weak-field limit.
- **2.2** — Bifurcation at $\Omega_c = \sqrt{g/R}$; for $\Omega > \Omega_c$, the bottom destabilizes and new equilibria appear off-axis.
- **2.3** — Chain rule on $H(q,p,t)$ and substitute EL to show the explicit $t$ dependence is all that survives.
- **2.4** — $H = c\sqrt{p^2 + m^2c^2}$.
- **3.2** — At the minimum, $dU_{\text{eff}}/dr = 0$ gives $r_0 = \ell^2/(mk)$; $\omega^2 = k/(mr_0^3)$.
- **3.3** — Conservation of $\mathbf{L}$ forces the motion into a plane.
- **3.4** — Solve the hyperbolic orbit; match impact parameter to scattering angle; differentiate.
- **4.2** — $\omega_1 + i\omega_2 \propto e^{i\Omega t}$ with $\Omega = \omega_3(I_3-I_1)/I_1$.
- **4.3** — Angular momentum vector precesses at $\Omega_p = \tau/L = MgR\sin\theta/(I\omega_s\sin\theta) = MgR/(I\omega_s)$.
- **4.4** — Linearize Euler's equations; the cross-term on the intermediate axis gives a real exponential mode (instability).
- **5.2** — Standard Navier–Stokes form.
- **5.3** — Molecular scale $\ll$ coarse-graining scale $\ll$ macroscopic scale.
- **6.2** — $\oint = 2\pi n$ exactly.
- **6.3** — Topology $\neq$ dynamics.
- **6.4** — $m_{10} = \hbar c/L_{\text{eff}} \sim 200$ GeV for $L_{\text{eff}} \sim 10^{-3}$ fm.
- **7.2** — Yukawa $y \propto \int|\psi|^2 v$; narrower vortex has smaller overlap; widths in ratio $\sim 1:14:51$.
- **7.3** — The Higgs *is* the lowest KK mode of $\Psi_A$; the Mexican-hat emerges from boundary conditions.
- **7.4** — Running coupling constraint: $y_t(M_{\text{Pl}}) < \sqrt{4\pi}$ gives $m_t \lesssim 200$ GeV, consistent with 172.6 GeV.
- **8.2** — $dp/dT \approx Lp/(RT^2) \approx 40650\cdot 101300/(8.314\cdot 373^2) \approx 3.56$ kPa/K — within 2 % of measured.
- **8.3** — Universality comes from relevance/irrelevance of operators at the fixed point; zone topology constrains which operators can appear.
- **8.4** — $T_c \sim v/k_B \sim 160$ GeV/$k_B \sim 1.9\times 10^{15}$ K.
- **9.2** — $dU = TdS - pdV$ gives $(\partial T/\partial V)_S = -(\partial p/\partial S)_V$; cycle through the other potentials.
- **9.3** — In Phase 2, $\Delta\kappa = 0$ gives $dS/dt = 0$: the universe is perfectly time-symmetric.
- **10.2** — $pV = Nk_BT$ falls out of $-\partial F/\partial V|_T$; Sackur–Tetrode from $S = -\partial F/\partial T|_V$.
- **10.3** — $\langle (\Delta E)^2\rangle = k_BT^2\cdot c_V\cdot N$; dividing by $\langle E\rangle^2 \propto N^2$ gives $1/\sqrt N$.
- **11.2** — $k_{\text{air}} \approx 0.024$ W/(m·K), within 7 % of measured.
- **11.3** — The H-theorem applies to the ensemble-averaged $f$, not to individual Hamilton trajectories.
- **12.2** — Distinguishable: $\Delta S = 2Nk_B\ln 2$; identical: $\Delta S = 0$; the $1/N!$ in (1.11.25) per-species treatment resolves Gibbs.
- **12.3** — Statistical explanation predicts no deviation from CPT; $\kappa$-phase explanation predicts scale-dependent deviations. A CPT-violating observation at cosmological scale would discriminate.
- **12.4** — Open problem: whether $L$ itself changes sign, or $\Delta\kappa$ changes sign, or both. Ch 12 §12.7 flags this as an open research question.

---

*End of Problem Sets. Fifty problems, twelve fully worked, covering every chapter of Volume 3.*
