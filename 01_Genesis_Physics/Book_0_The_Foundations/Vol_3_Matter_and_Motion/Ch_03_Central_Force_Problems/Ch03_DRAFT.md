# Chapter 3: Central Force Problems

---

*In which the machinery of Chapters 1–2 meets the gravity of Volume 2 — and Kepler's laws emerge not as empirical rules but as geometric theorems of the zone manifold.*

---

## §3.1 — Why Central Forces Are Special

In Volume 2, we derived the gravitational force from the curvature of the zone manifold's extra dimensions. That derivation gave us a specific force law — an inverse-square attraction with a coupling constant $G_4$ determined by membrane tension and the effective coupling length (Vol 2, Eq. 2.2.29):

$$G_4 = \frac{c^4}{8\pi\sigma L_{\text{eff}}^2} = 6.674 \times 10^{-11} \; \text{m}^3/(\text{kg} \cdot \text{s}^2) \tag{2.2.29}$$

In Chapter 1, we derived the force equation $m\mathbf{a} = \mathbf{F}$ (Eq. 3.1.10) from the geodesic structure of the zone manifold. In Chapter 2, we built the Lagrangian and Hamiltonian formalisms that transform this force equation into a systematic machinery for solving mechanics problems.

Now we bring them together. This chapter asks: **what happens when you put a particle in the gravitational field that the zone manifold creates?**

The answer is everything that Kepler observed, everything that Newton explained, and more — but none of it postulated. Every orbit, every period, every scattering angle will trace back through an unbroken chain:

$$\boxed{\text{Zone manifold} \xrightarrow{\text{Vol 2 Ch 2}} \text{gravity} \xrightarrow{\text{Ch 1}} F = ma \xrightarrow{\text{Ch 2}} \text{Lagrangian} \xrightarrow{\text{this chapter}} \text{Kepler's laws}}$$

[FIGURE: Fig 3.3.1 — Derivation roadmap from zone curvature to Kepler's laws]

Why are central forces the right place to begin applying the machinery? Because the fundamental forces derived in Volume 2 — gravity (Ch 2) and the Coulomb interaction (Ch 3) — are both central forces: they point along the line connecting two bodies and depend only on the distance between them. This is not accidental. The zone manifold's 4D subspace has spherical symmetry in the spatial dimensions, and the forces that emerge from it inherit that symmetry. A central force is not a special case — it is the *generic* case for forces derived from zone geometry.

We will develop the theory in logical order: reduction to the radial problem (§3.2), the orbit equation (§3.3), Kepler's laws derived (§3.4), orbital energetics (§3.5), scattering theory (§3.6), and Bertrand's theorem (§3.7). Each section builds on the previous, and every result traces backward through the chain above.

A word about what makes this chapter different from a standard classical mechanics textbook. In Goldstein, Marion, or Landau & Lifshitz, the central force chapter begins with Newton's law of gravitation as a given — an empirical fact. The derivations that follow are mathematically identical to ours, but they rest on an axiom: "there exists an inverse-square gravitational force with coupling constant $G = 6.674 \times 10^{-11}$." The derivation of Kepler's laws is beautiful, but it carries an unexplained premise.

We have no such axiom. Our starting point is the zone manifold's geometry. The 6D Einstein-Hilbert action (Vol 2, Ch 2, Eq. 2.2.1) is dimensionally reduced via Kaluza-Klein to 4D (§2.3), projected onto the Firmament via the Gauss-Codazzi relations (§2.4), and taken to the weak-field limit (§2.5). The result is the Poisson equation $\nabla^2\Phi = 4\pi G_4\rho$ with $G_4$ determined by membrane parameters (Eq. 2.2.29). The $1/r$ potential is the unique spherically symmetric solution, and the $1/r^2$ force follows by differentiation.

The mathematics of orbits is the same as in any textbook — it has to be, since the force law is the same — but the *epistemic status* is entirely different. When we write $F = -G_4 Mm/r^2$, every symbol in that equation has been earned, not assumed. The student who follows this chain has something that Goldstein's student does not: an answer to "but why $1/r^2$?"

---

## §3.2 — Reduction to the Radial Problem

### §3.2.1 — The Two-Body Problem and Center-of-Mass Separation

Before writing down the Lagrangian for a central force, we need to address a subtlety that standard treatments often gloss over: we are dealing with TWO bodies, not one. The Sun does not sit at a fixed point while Earth orbits around it. Both bodies move, attracted to each other.

Consider two bodies of masses $M$ and $m$ at positions $\mathbf{r}_1$ and $\mathbf{r}_2$. Their total Lagrangian (from Eq. 3.2.3, specialized to two particles interacting through a central potential) is:

$$L_{\text{total}} = \frac{1}{2}M|\dot{\mathbf{r}}_1|^2 + \frac{1}{2}m|\dot{\mathbf{r}}_2|^2 - V(|\mathbf{r}_1 - \mathbf{r}_2|) \tag{3.3.0a}$$

We define the center-of-mass coordinate $\mathbf{R} = (M\mathbf{r}_1 + m\mathbf{r}_2)/(M+m)$ and the relative coordinate $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$. By direct substitution, the Lagrangian separates cleanly:

$$L_{\text{total}} = \underbrace{\frac{1}{2}(M+m)|\dot{\mathbf{R}}|^2}_{L_{\text{cm}}} + \underbrace{\frac{1}{2}\mu|\dot{\mathbf{r}}|^2 - V(r)}_{L_{\text{rel}}} \tag{3.3.0b}$$

where $\mu = Mm/(M+m)$ is the **reduced mass**. The center-of-mass Lagrangian $L_{\text{cm}}$ describes free motion (no forces act on the center of mass, by momentum conservation from Vol 1, Ch 7, Eq. 1.7.17). The relative Lagrangian $L_{\text{rel}}$ is mathematically identical to a single particle of mass $\mu$ moving in a fixed central potential $V(r)$. This separation is exact for any central force — it is a consequence of translational symmetry (Noether's theorem).

Why does this matter? Because it means the two-body central force problem is *equivalent* to a one-body problem. We need only solve the relative motion, and both bodies' trajectories follow from it. For the remainder of this chapter, "the particle" means the fictitious particle of mass $\mu$ at relative position $\mathbf{r}$, and the relative Lagrangian is:

$$L = \frac{1}{2}\mu|\dot{\mathbf{r}}|^2 - V(r) \tag{3.3.1}$$

where $\mu = Mm/(M + m)$ is the reduced mass. This is a direct specialization of the particle Lagrangian (Eq. 3.2.3) derived from the zone action in Chapter 2. For the zone-derived gravitational potential (Vol 2, Eq. 2.2.40):

$$V(r) = -\frac{G_4 Mm}{r} \tag{3.3.2}$$

Note what is happening: the potential $V(r)$ is **not postulated**. It is the weak-field solution of the 4D Einstein equations projected from the 6D zone manifold (Vol 2, §2.4). The $1/r$ form follows from Poisson's equation $\nabla^2\Phi = 4\pi G_4\rho$ applied to a point source.

In spherical coordinates $(r, \theta, \phi)$, the kinetic energy becomes:

$$T = \frac{1}{2}\mu\left(\dot{r}^2 + r^2\dot{\theta}^2 + r^2\sin^2\theta\,\dot{\phi}^2\right) \tag{3.3.3}$$

### §3.2.2 — Angular Momentum Conservation and Planar Motion

The Lagrangian (3.3.1) depends on $r$ alone — not on the angular coordinates $\theta$ or $\phi$. Rotational symmetry is exact for the zone-derived central potential because the Poisson equation inherits the spherical symmetry of 3D space (itself inherited from the zone manifold's spatial isotropy, Vol 1 Ch 3).

By Noether's theorem (Vol 1, Ch 7; Ch 2, §2.3), every continuous symmetry yields a conserved quantity. Rotational invariance gives conservation of the angular momentum vector:

$$\mathbf{L} = \mu\mathbf{r} \times \dot{\mathbf{r}} = \text{const.} \tag{3.3.4}$$

This has two immediate consequences:

**First,** $\mathbf{L}$ is constant in both magnitude and direction. The direction of $\mathbf{L}$ defines a fixed axis, and the motion is confined to the plane perpendicular to this axis. We choose coordinates so that this is the $\theta = \pi/2$ plane. From this point on, the problem is two-dimensional: $(r, \phi)$.

**Second,** the magnitude $L = |\mathbf{L}| = \mu r^2\dot{\phi}$ is a constant of the motion. This eliminates one degree of freedom.

Why does this matter? A 3D problem with three degrees of freedom has just become a 1D problem — one radial coordinate $r(t)$. The Lagrangian formalism does in two lines what would require considerable effort in the Newtonian approach. This is exactly the payoff that Chapter 2 promised.

It is worth noting that for a general three-dimensional force (not central), angular momentum is NOT conserved, and the motion is NOT confined to a plane. The constraint to planar motion is a *theorem* about central forces, not an assumption we make for simplicity. The zone-derived forces (gravity and Coulomb) are central because the zone manifold's spatial dimensions have spherical symmetry, and therefore all zone-derived orbits lie in planes. This is why the Solar System is approximately flat — each planet's orbit is a plane, and while these planes don't all coincide exactly (due to mutual perturbations), the underlying two-body orbits are exactly planar.

The reduced planar Lagrangian is:

$$L = \frac{1}{2}\mu(\dot{r}^2 + r^2\dot{\phi}^2) - V(r) \tag{3.3.4a}$$

The Euler-Lagrange equation for $\phi$ (Eq. 3.2.12) gives:

$$\frac{d}{dt}(\mu r^2\dot{\phi}) = 0 \quad \Rightarrow \quad L = \mu r^2\dot{\phi} = \text{const.} \tag{3.3.4b}$$

confirming angular momentum conservation directly from the Lagrangian machinery.

### §3.2.3 — The Effective Potential

With $\theta = \pi/2$ and $L = \mu r^2\dot{\phi}$, the Lagrangian reduces to:

$$L = \frac{1}{2}\mu\dot{r}^2 + \frac{L^2}{2\mu r^2} - V(r) \tag{3.3.5}$$

The total energy (conserved, since $L$ has no explicit time dependence — a consequence of the Symmetry Principle, Vol 1 Ch 8) is:

$$E = \frac{1}{2}\mu\dot{r}^2 + V_{\text{eff}}(r) \tag{3.3.6}$$

where the **effective potential** is:

$$\boxed{V_{\text{eff}}(r) = V(r) + \frac{L^2}{2\mu r^2}} \tag{3.3.7}$$

For zone-derived gravity, $V(r) = -G_4 Mm/r$, so:

$$V_{\text{eff}}(r) = -\frac{G_4 Mm}{r} + \frac{L^2}{2\mu r^2} \tag{3.3.8}$$

[FIGURE: Fig 3.3.2 — Effective potential for gravitational central force]

The effective potential encodes the entire qualitative behavior of the orbit. The first term ($-G_4 Mm/r$) is attractive and dominates at large $r$. The second term ($L^2/(2\mu r^2)$, the "centrifugal barrier") is repulsive and dominates at small $r$. Their competition creates a potential well with a minimum at:

$$r_{\text{circ}} = \frac{L^2}{G_4 Mm\mu} \tag{3.3.9}$$

This is the radius of the unique circular orbit for given $L$. Its energy is:

$$E_{\text{circ}} = V_{\text{eff}}(r_{\text{circ}}) = -\frac{(G_4 Mm)^2\mu}{2L^2} \tag{3.3.10}$$

**Stability of the circular orbit.** Is this minimum stable? The second derivative of $V_\text{eff}$ at $r_\text{circ}$ determines whether small perturbations oscillate (stable) or grow (unstable):

$$\frac{d^2 V_\text{eff}}{dr^2}\bigg|_{r_\text{circ}} = -\frac{2G_4 Mm}{r_\text{circ}^3} + \frac{3L^2}{\mu r_\text{circ}^4}$$

Substituting $r_\text{circ} = L^2/(G_4 Mm\mu)$, we get $d^2V_\text{eff}/dr^2 = G_4 Mm \mu^3 (G_4 Mm)^2/L^6 > 0$. The second derivative is positive — the minimum is a genuine minimum, and the circular orbit is stable. A slightly perturbed orbit oscillates radially about $r_\text{circ}$, producing a nearly-circular ellipse.

This stability is not guaranteed for all central forces. For $F \propto 1/r^n$ with $n \geq 3$, the effective potential has no minimum — all circular orbits are unstable. The inverse-square law's stability is another consequence of its mathematical specialness, closely related to Bertrand's theorem (§3.7).

Why is the centrifugal term $L^2/(2\mu r^2)$? It is not a real force — it is a consequence of expressing radial dynamics in polar coordinates with a conserved angular momentum. The particle is "trying" to fly away tangentially (angular momentum demands $v_\perp = L/(\mu r)$, which grows as $r$ shrinks), and this manifests as an effective repulsion in the radial equation. The Lagrangian formalism makes this automatic and exact.

**Orbit classification from $V_\text{eff}$:**

| Energy $E$ | Orbit Type | Eccentricity $e$ | Condition |
|-----------|-----------|-----------------|-----------|
| $E = E_{\text{circ}} < 0$ | Circular | $e = 0$ | $\dot{r} = 0$ always; $r = r_{\text{circ}}$ |
| $E_{\text{circ}} < E < 0$ | Elliptical | $0 < e < 1$ | $r$ oscillates between turning points |
| $E = 0$ | Parabolic | $e = 1$ | Marginally unbound; $r \to \infty$ as $v \to 0$ |
| $E > 0$ | Hyperbolic | $e > 1$ | Unbound; $r \to \infty$ with finite $v$ |

Each orbit type is completely determined by two conserved quantities — $E$ and $L$ — both of which trace to symmetries of the zone manifold (time translation and rotational invariance, respectively).

### §3.2.4 — Worked Example: Circular Orbit Speed

Before proceeding to the orbit equation, let us extract a concrete result from the effective potential. A circular orbit sits at the minimum of $V_\text{eff}$, where $dV_\text{eff}/dr = 0$. For zone-derived gravity:

$$\frac{dV_{\text{eff}}}{dr} = \frac{G_4 Mm}{r^2} - \frac{L^2}{\mu r^3} = 0$$

Solving: $L^2 = G_4 Mm\mu r_{\text{circ}}$ (Eq. 3.3.9). Using $L = \mu r_{\text{circ}} v_\perp$ where $v_\perp$ is the tangential speed:

$$\mu^2 r_{\text{circ}}^2 v_\perp^2 = G_4 Mm\mu r_{\text{circ}}$$

For the planetary case $m \ll M$, so $\mu \approx m$:

$$v_{\text{circ}} = \sqrt{\frac{G_4 M}{r_{\text{circ}}}} \tag{3.3.10a}$$

For the International Space Station at altitude 408 km above Earth ($r = R_E + 408\,\text{km} = 6.779 \times 10^6$ m):

$$v_{\text{ISS}} = \sqrt{\frac{6.674 \times 10^{-11} \times 5.972 \times 10^{24}}{6.779 \times 10^6}} = 7.667 \;\text{km/s}$$

The observed value is 7.66 km/s. This is not a coincidence — it is the circular orbit condition applied to zone-derived gravity, with no adjustable parameters.

### §3.2.5 — The Radial Equation of Motion

For completeness, the Euler-Lagrange equation (Eq. 3.2.12) for the radial coordinate gives:

$$\mu\ddot{r} = -\frac{dV_{\text{eff}}}{dr} = -\frac{dV}{dr} + \frac{L^2}{\mu r^3} \tag{3.3.10b}$$

The right-hand side has two terms: the actual force $-dV/dr$ and the centrifugal "force" $L^2/(\mu r^3)$. The latter is not a real force — it is a coordinate artifact that arises because we are describing radial motion in a rotating frame. The Lagrangian formalism handles it automatically; no fictitious forces need to be added by hand.

---

## §3.3 — The Orbit Equation

### §3.3.1 — Binet's Equation

The energy equation (3.3.6) gives us $r(t)$ — the radial distance as a function of time. But for many purposes, what we want is the orbit *shape* $r(\phi)$ — the trajectory in space, irrespective of when the particle reaches each point.

The key insight is that angular momentum conservation lets us trade $t$ for $\phi$ as the independent variable. Since $\dot{\phi} = L/(\mu r^2)$ is always positive (for counterclockwise orbits), $\phi$ increases monotonically and can serve as a "clock."

**Step 1: Express $\dot{r}$ in terms of $d/d\phi$.** Using the chain rule and $L = \mu r^2 \dot{\phi}$:

$$\dot{r} = \frac{dr}{dt} = \frac{dr}{d\phi}\cdot\dot{\phi} = \frac{dr}{d\phi}\cdot\frac{L}{\mu r^2} \tag{3.3.11}$$

**Step 2: Change variables to $u = 1/r$.** Then $r = 1/u$, $dr = -du/u^2$, and:

$$\dot{r} = -\frac{1}{u^2}\frac{du}{d\phi}\cdot\frac{Lu^2}{\mu} = -\frac{L}{\mu}\frac{du}{d\phi} \tag{3.3.12}$$

**Step 3: Compute $\ddot{r}$.** Differentiating again:

$$\ddot{r} = \frac{d}{dt}\left(-\frac{L}{\mu}\frac{du}{d\phi}\right) = -\frac{L}{\mu}\frac{d^2u}{d\phi^2}\cdot\dot{\phi} = -\frac{L^2 u^2}{\mu^2}\frac{d^2u}{d\phi^2}$$

**Step 4: Substitute into the radial equation of motion** (Eq. 3.3.10b). For a central force $F(r) = -dV/dr$, the equation $\mu\ddot{r} - L^2/(\mu r^3) = F(r)$ becomes:

$$-\frac{L^2 u^2}{\mu}\frac{d^2u}{d\phi^2} - \frac{L^2 u^3}{\mu} = F(1/u)$$

Dividing by $-L^2 u^2/\mu$:

$$\boxed{\frac{d^2u}{d\phi^2} + u = -\frac{\mu}{L^2}\frac{1}{u^2}F(1/u)} \tag{3.3.13}$$

This is **Binet's equation** — a second-order ODE for the orbit shape $u(\phi)$. It is a direct consequence of the Euler-Lagrange machinery from Chapter 2, with every step traceable. The force $F$ appears on the right-hand side; the left-hand side is pure kinematics (angular momentum conservation). For any given force law, solving Binet's equation gives the orbit shape.

Why is this equation so useful? Because for many force laws (including the zone-derived $1/r^2$), it is a *linear* ODE with constant coefficients — far simpler than the original nonlinear equation of motion in time.

### §3.3.2 — Solution for Zone-Derived Gravity

For the zone-derived gravitational force (Vol 2, Eq. 2.2.43):

$$F(r) = -\frac{G_4 Mm}{r^2} \tag{3.3.14}$$

Binet's equation becomes:

$$\frac{d^2u}{d\phi^2} + u = \frac{G_4 Mm\mu}{L^2} \equiv \frac{1}{p} \tag{3.3.15}$$

where we define the **semi-latus rectum** $p \equiv L^2/(G_4 Mm\mu)$. This is a simple harmonic oscillator equation with a constant offset. Its general solution is:

$$u(\phi) = \frac{1}{p}\left[1 + e\cos(\phi - \phi_0)\right] \tag{3.3.16}$$

or equivalently:

$$\boxed{r(\phi) = \frac{p}{1 + e\cos(\phi - \phi_0)}} \tag{3.3.17}$$

This is the equation of a conic section with one focus at the origin, semi-latus rectum $p$, and eccentricity $e$. The angle $\phi_0$ is the direction of periapsis (closest approach).

[FIGURE: Fig 3.3.3 — Orbit classification: conic sections from energy]

Pause to appreciate what has happened. We started with the zone manifold (Vol 1). From it, we derived gravity (Vol 2, Ch 2). We derived the force equation (Ch 1) and the Lagrangian formalism (Ch 2). Applying the Lagrangian to the gravitational potential gave us Binet's equation, and solving it gave us — conic sections. Ellipses, parabolas, hyperbolas. The same curves that Kepler inferred from Tycho Brahe's observations in the early 1600s, the same curves that Newton proved must follow from an inverse-square law in 1687. But here, the inverse-square law was not assumed. It was derived from the geometry of the extra dimensions.

The solution (3.3.17) is worth examining in detail. The semi-latus rectum $p = L^2/(G_4 Mm\mu)$ is entirely determined by the angular momentum and the strength of the gravitational coupling — both of which trace to the zone manifold. The eccentricity $e$ is set by the energy (a second conserved quantity from time-translation symmetry). Two symmetries of the zone manifold — rotational and temporal — are sufficient to determine the complete shape of every gravitational orbit in the universe.

**Worked example: Earth's orbital eccentricity.** Earth orbits the Sun with $a = 1.496 \times 10^{11}$ m and $e = 0.0167$. This means the Earth-Sun distance varies between $r_\text{min} = a(1-e) = 1.471 \times 10^{11}$ m (perihelion, early January) and $r_\text{max} = a(1+e) = 1.521 \times 10^{11}$ m (aphelion, early July). The difference is about 5 million km — roughly 3.3% of the mean distance.

From Eq. (3.3.18), we can compute Earth's orbital energy:

$$E = -\frac{G_4 M_\odot m_E}{2a} = -\frac{6.674\times 10^{-11} \times 1.989\times 10^{30} \times 5.972\times 10^{24}}{2 \times 1.496\times 10^{11}} = -2.65 \times 10^{33} \;\text{J}$$

This enormous binding energy (equivalent to about $2.9 \times 10^{16}$ kg of mass via $E = mc^2$) is what keeps Earth in its orbit. To escape the Solar System, Earth would need to gain exactly this much kinetic energy — a fact encoded in the vis-viva equation (§3.5).

### §3.3.3 — Orbit Parameters from Conserved Quantities

The eccentricity $e$ and semi-major axis $a$ are not free parameters — they are determined by the two conserved quantities $E$ and $L$. Let us derive the relationships explicitly.

**Energy from the orbit equation.** At the turning points (periapsis and apoapsis), the radial velocity vanishes: $\dot{r} = 0$. At periapsis ($\phi = \phi_0$), $r_{\min} = p/(1 + e)$. The total energy equals the effective potential at any turning point (since $\dot{r} = 0$ means $E = V_{\text{eff}}(r_{\text{turn}})$):

$$E = -\frac{G_4 Mm}{r_{\min}} + \frac{L^2}{2\mu r_{\min}^2}$$

Substituting $r_{\min} = p/(1+e)$ and $p = L^2/(G_4 Mm\mu)$:

$$E = -\frac{G_4 Mm(1+e)}{p} + \frac{L^2(1+e)^2}{2\mu p^2}$$

Using $G_4 Mm = L^2/(\mu p)$:

$$E = -\frac{L^2(1+e)}{\mu p^2} + \frac{L^2(1+e)^2}{2\mu p^2} = \frac{L^2}{2\mu p^2}\left[(1+e)^2 - 2(1+e)\right] = \frac{L^2}{2\mu p^2}(e^2 - 1)$$

Since $p = a(1-e^2)$ for an ellipse, this simplifies to $E = -L^2/(2\mu a p)$. Using $p = L^2/(G_4 Mm\mu)$ again:

$$\boxed{e = \sqrt{1 + \frac{2EL^2}{(G_4 Mm\mu)^2}}} \tag{3.3.18}$$

and for the semi-major axis $a = p/(1 - e^2)$ (valid for ellipses, $e < 1$):

$$\boxed{E = -\frac{G_4 Mm}{2a}} \tag{3.3.19}$$

This remarkable result says that the energy of a bound orbit depends only on the semi-major axis — not on the eccentricity, not on the angular momentum. A highly eccentric comet with semi-major axis $a$ has exactly the same energy as a circular orbit with radius $a$. Why? Because the $1/r$ potential has a hidden symmetry (the Laplace-Runge-Lenz vector, §3.5.3) that makes energy depend on a single orbital parameter.

---

## §3.4 — Kepler's Laws — Derived, Not Postulated

We now have everything needed to state Kepler's three laws as theorems of the zone framework.

### §3.4.1 — First Law: Orbits Are Conic Sections

**Theorem (Kepler's First Law).** *A body moving under the zone-derived gravitational force $\mathbf{F} = -(G_4 Mm/r^2)\hat{\mathbf{r}}$ follows a conic section with the central body at one focus.*

*Proof.* This is Eq. (3.3.17), the general solution of Binet's equation (3.3.13) for the force law (3.3.14). The semi-latus rectum $p = L^2/(G_4 Mm\mu)$ and eccentricity $e$ are determined by the conserved quantities $L$ and $E$ (Eq. 3.3.18). For bound orbits ($E < 0$), $e < 1$, and the conic is an ellipse. $\square$

The force law $F \propto 1/r^2$ that makes this work was not assumed — it was derived from the 6D Einstein-Hilbert action via dimensional reduction, Gauss-Codazzi projection, and the weak-field limit (Vol 2, Ch 2, §§2.2–2.4).

### §3.4.2 — Second Law: Equal Areas in Equal Times

**Theorem (Kepler's Second Law).** *The radius vector from the central body to the orbiting body sweeps out equal areas in equal times.*

*Proof.* The areal velocity is:

$$\frac{dA}{dt} = \frac{1}{2}r^2\dot{\phi} = \frac{L}{2\mu} = \text{const.} \tag{3.3.20}$$

This follows directly from the conservation of angular momentum $L = \mu r^2\dot{\phi}$ (Eq. 3.3.4), which is itself a consequence of Noether's theorem applied to the rotational symmetry of the zone-derived potential. $\square$

[FIGURE: Fig 3.3.4 — Kepler's Second Law: equal areas in equal times]

This is the most physically transparent of the three laws. Near periapsis, $r$ is small, so $\dot{\phi}$ must be large to keep $r^2\dot{\phi}$ constant — the planet moves faster. Near apoapsis, $r$ is large, so $\dot{\phi}$ is small — the planet moves slower. The "equal areas" rule is not about areas at all; it is about angular momentum conservation. And angular momentum is conserved because the zone manifold is rotationally symmetric.

Note that the Second Law is **force-law-independent**: it holds for ANY central force, not just $1/r^2$. This is because angular momentum conservation follows from rotational symmetry alone, regardless of the radial dependence of $V(r)$. Even if the zone manifold produced a completely different force law — say $F \propto 1/r^5$ — the Second Law would still hold, because rotational symmetry would still guarantee angular momentum conservation. This is why it was the easiest of the three laws for Newton to prove (Principia, Book I, Proposition I) — it required only the assumption that the force is central, not any specific force law.

The practical consequences are significant. For Earth's orbit ($e = 0.0167$), the speed variation between perihelion and aphelion is:

$$\frac{v_\text{peri}}{v_\text{aph}} = \frac{1+e}{1-e} = \frac{1.0167}{0.9833} = 1.034$$

Earth moves 3.4% faster in January (perihelion) than in July (aphelion). This is why Northern Hemisphere winter is slightly shorter than summer — Earth sweeps through the winter portion of its orbit faster. The difference is small for Earth ($e = 0.017$) but dramatic for comets ($e \approx 0.99$), which crawl at aphelion and whip past the Sun at perihelion at hundreds of km/s.

### §3.4.3 — Third Law: The Period–Distance Relation

**Theorem (Kepler's Third Law).** *The square of the orbital period is proportional to the cube of the semi-major axis:*

$$\boxed{T^2 = \frac{4\pi^2}{G_4(M + m)}a^3} \tag{3.3.21}$$

*For $m \ll M$ (the usual planetary case), $T^2 \approx 4\pi^2 a^3/(G_4 M)$.*

*Proof.* The strategy is elegant: combine the Second Law (areal velocity) with the geometry of the ellipse.

The total area of an ellipse with semi-major axis $a$ and semi-minor axis $b$ is $A_{\text{ellipse}} = \pi a b$. The orbit traces this area in one period $T$. By the Second Law, the areal velocity is constant at $dA/dt = L/(2\mu)$. Therefore:

$$T = \frac{A_{\text{ellipse}}}{dA/dt} = \frac{\pi a b}{L/(2\mu)} = \frac{2\pi\mu a b}{L}$$

Now we need to express $b$ and $L$ in terms of $a$. The semi-minor axis is $b = a\sqrt{1-e^2}$, and from the semi-latus rectum:

$$p = a(1-e^2) = \frac{L^2}{G_4 Mm\mu} \quad \Rightarrow \quad L^2 = G_4 Mm\mu \cdot a(1-e^2)$$

For the two-body problem, $G_4 Mm/\mu = G_4(M+m)$, so $L^2 = G_4(M+m)\mu^2 \cdot a(1-e^2)$ and $L = \mu\sqrt{G_4(M+m) \cdot a(1-e^2)}$.

Substituting into the period:

$$T = \frac{2\pi\mu a \cdot a\sqrt{1-e^2}}{\mu\sqrt{G_4(M+m) \cdot a(1-e^2)}} = 2\pi a^{3/2}\frac{\sqrt{1-e^2}}{\sqrt{G_4(M+m) \cdot a(1-e^2)}}$$

$$= 2\pi\sqrt{\frac{a^3}{G_4(M+m)}}$$

The eccentricity cancels completely. This is a deep result: the period depends only on the semi-major axis, not on how elongated the orbit is. A nearly circular orbit and a highly eccentric comet with the same $a$ have the same period. $\square$

### §3.4.4 — Numerical Validation: Zone Gravity vs. the Solar System

The derivation chain is complete: zone manifold → gravity → Kepler's Third Law. But does it actually work? We can check using the zone-derived value of $G_4$ (Vol 2, Eq. 2.2.29).

The test suite (`test_gravity_kinematics.py`) computes $T = 2\pi\sqrt{a^3/(G_4 M)}$ for three systems and compares with observed periods:

| System | Theory (days) | Observed (days) | Error |
|--------|-------------|----------------|-------|
| Mercury–Sun | 87.958 | 87.969 | 0.012% |
| Earth–Sun | 365.21 | 365.25 | 0.011% |
| Moon–Earth | 27.452 | 27.322 | 0.477% |

$$T_{\text{Mercury}} = 2\pi\sqrt{\frac{(5.791 \times 10^{10})^3}{6.674 \times 10^{-11} \times 1.989 \times 10^{30}}} = 7.600 \times 10^6 \;\text{s} = 87.96 \;\text{days} \tag{3.3.22}$$

All errors are below 0.5%. The Moon's slightly larger error (0.477%) reflects the simplification of treating the Earth-Moon system as an isolated two-body problem. In reality, the Sun's gravitational perturbation on the Moon is significant — the Sun-Moon gravitational force is actually larger than the Earth-Moon force (about 2.2 times larger), though the *tidal* (differential) force that matters for the Moon's orbit around Earth is dominated by Earth. Accounting for Solar perturbations through the three-body problem would reduce this error further.

These numbers were not tuned. The gravitational constant $G_4$ was derived from membrane parameters in Volume 2 (Eq. 2.2.29): $G_4 = c^4/(8\pi\sigma L_\text{eff}^2)$. The semi-major axes and masses are measured quantities. The agreement between prediction and observation validates the entire derivation chain from zone manifold to planetary orbits.

**Worked example: The mass of Jupiter from its moons.** Kepler's Third Law can be inverted to determine the mass of a central body from the orbit of a satellite. For Io (Jupiter's innermost Galilean moon, $a = 4.217 \times 10^8$ m, $T = 1.528 \times 10^5$ s):

$$M_J = \frac{4\pi^2 a^3}{G_4 T^2} = \frac{4\pi^2 (4.217\times 10^8)^3}{6.674\times 10^{-11} \times (1.528\times 10^5)^2} = 1.90 \times 10^{27} \;\text{kg}$$

The accepted value is $1.898 \times 10^{27}$ kg — an agreement within 0.1%. This technique (applied to different moons and different planets) is how the masses of all outer Solar System bodies are determined. It works because Kepler's Third Law is exact for two-body systems, and the zone-derived $G_4$ is precise.

The derivation chain is now complete for all three laws. Let us summarize the logical structure:

| Law | Statement | Derived From | Key Equation |
|-----|-----------|-------------|--------------|
| 1st | Orbits are conic sections | Binet's equation + $1/r^2$ force (Vol 2) | (3.3.17) |
| 2nd | Equal areas in equal times | Angular momentum conservation (Noether, Vol 1) | (3.3.20) |
| 3rd | $T^2 \propto a^3$ | 2nd Law + ellipse geometry + orbit parameters | (3.3.21) |

None of these laws was postulated. Each was proved as a theorem of the zone framework.

---

## §3.5 — Orbital Energy and the Vis-Viva Equation

### §3.5.1 — Energy of a Kepler Orbit

The energy–semi-major-axis relation (Eq. 3.3.19) tells us that $E = -G_4 Mm/(2a)$ for any bound orbit. This means:

- **More tightly bound orbits** (smaller $a$) have more negative energy.
- **Circular and eccentric orbits with the same $a$** have the same energy.
- **The energy determines the size, not the shape.** Shape (eccentricity) requires knowing $L$ as well.

### §3.5.2 — The Vis-Viva Equation

Combining $E = \frac{1}{2}\mu v^2 + V(r)$ with $E = -G_4 Mm/(2a)$ and $V(r) = -G_4 Mm/r$:

$$\frac{1}{2}\mu v^2 - \frac{G_4 Mm}{r} = -\frac{G_4 Mm}{2a}$$

Solving for $v^2$, and using $\mu = Mm/(M+m) \approx m$ for $m \ll M$:

$$\boxed{v^2 = G_4 M\left(\frac{2}{r} - \frac{1}{a}\right)} \tag{3.3.23}$$

This is the **vis-viva equation** (Latin: "living force") — it gives the speed at any point on any Keplerian orbit. Special cases:

- **Circular orbit** ($r = a$): $v_{\text{circ}} = \sqrt{G_4 M/a}$
- **Escape speed** ($a \to \infty$, i.e., $E = 0$): $v_{\text{esc}} = \sqrt{2G_4 M/r}$
- **Periapsis** ($r = a(1-e)$): $v_{\text{peri}} = \sqrt{G_4 M(1+e)/(a(1-e))}$

The escape speed is exactly $\sqrt{2}$ times the circular orbital speed at the same radius. This is a consequence of the $1/r$ potential structure — and therefore traces to the zone manifold's geometry.

**Worked example: Geostationary orbit.** A geostationary satellite has period $T = 86{,}164$ s (one sidereal day). By Kepler's Third Law:

$$a = \left(\frac{G_4 M_E T^2}{4\pi^2}\right)^{1/3} = \left(\frac{6.674\times 10^{-11} \times 5.972\times 10^{24} \times (86{,}164)^2}{4\pi^2}\right)^{1/3} = 4.216 \times 10^7 \;\text{m}$$

This is 42,160 km from Earth's center, or about 35,790 km altitude — exactly where communications satellites park. The vis-viva equation gives the orbital speed:

$$v = \sqrt{\frac{G_4 M_E}{a}} = \sqrt{\frac{6.674\times 10^{-11} \times 5.972\times 10^{24}}{4.216\times 10^7}} = 3.075 \;\text{km/s}$$

Every number here traces to zone-derived $G_4$. The agreement with the observed geostationary radius (42,164 km) is within 0.01%.

**Escape velocity from physical bodies.** The escape speed from a body of mass $M$ and radius $R$ is:

$$v_\text{esc} = \sqrt{\frac{2G_4 M}{R}}$$

For Earth: $v_\text{esc} = \sqrt{2 \times 6.674\times 10^{-11} \times 5.972\times 10^{24} / 6.371\times 10^6} = 11.18$ km/s (observed: 11.19 km/s). For the Moon: $v_\text{esc} = 2.38$ km/s. For the Sun (from its surface): $v_\text{esc} = 618$ km/s.

Notice that $v_\text{esc} = \sqrt{2}\, v_\text{circ}$: to escape, you need only $\sqrt{2} \approx 1.41$ times the circular orbital speed at the same radius. This factor of $\sqrt{2}$ is universal for $1/r$ potentials — it is the ratio of the virial coefficients for bound ($E = -T$) and marginally unbound ($E = 0$) orbits. In the zone framework, it traces to the $1/r$ form of the gravitational potential, which itself traces to the Poisson equation for a point source on the zone manifold.

**Hohmann transfer orbit — practical orbital mechanics.** The vis-viva equation makes orbit transfers calculable. To move from a circular orbit at $r_1$ to a circular orbit at $r_2 > r_1$, the minimum-energy approach is the Hohmann transfer: an elliptical orbit tangent to both circles, with $a_\text{transfer} = (r_1 + r_2)/2$. The two required velocity changes (computed from vis-viva at the tangent points) are:

$$\Delta v_1 = \sqrt{\frac{G_4 M}{r_1}}\left(\sqrt{\frac{2r_2}{r_1 + r_2}} - 1\right), \quad \Delta v_2 = \sqrt{\frac{G_4 M}{r_2}}\left(1 - \sqrt{\frac{2r_1}{r_1 + r_2}}\right)$$

These formulas underpin all orbital maneuvers in spaceflight — from low Earth orbit to geostationary, from Earth orbit to Mars. Every $\Delta v$ calculation in astrodynamics rests on the vis-viva equation, which rests on the zone-derived gravitational potential.

### §3.5.3 — The Laplace-Runge-Lenz Vector

The Kepler problem has a hidden conserved quantity beyond energy and angular momentum. The **Laplace-Runge-Lenz (LRL) vector** is:

$$\boxed{\mathbf{A} = \mathbf{p} \times \mathbf{L} - G_4 Mm\mu^2\hat{\mathbf{r}}} \tag{3.3.24}$$

where $\mathbf{p} = \mu\dot{\mathbf{r}}$ is the linear momentum and $\mathbf{L} = \mu\mathbf{r} \times \dot{\mathbf{r}}$ is the angular momentum.

To verify conservation, we compute $\dot{\mathbf{A}}$ explicitly. Using the equation of motion $\mu\ddot{\mathbf{r}} = -(G_4 Mm/r^3)\mathbf{r}$, i.e. $\dot{\mathbf{p}} = -(G_4 Mm\mu/r^3)\mathbf{r}$:

$$\dot{\mathbf{A}} = \dot{\mathbf{p}} \times \mathbf{L} + \mathbf{p} \times \dot{\mathbf{L}} - G_4 Mm\mu^2\frac{d\hat{\mathbf{r}}}{dt}$$

The second term vanishes since $\dot{\mathbf{L}} = 0$ (angular momentum is conserved for central forces). For the first term:

$$\dot{\mathbf{p}} \times \mathbf{L} = -\frac{G_4 Mm\mu}{r^3}(\mathbf{r} \times \mathbf{L}) = -\frac{G_4 Mm\mu}{r^3}\mathbf{r} \times (\mu\mathbf{r} \times \dot{\mathbf{r}})$$

Using the vector identity $\mathbf{a} \times (\mathbf{a} \times \mathbf{b}) = \mathbf{a}(\mathbf{a} \cdot \mathbf{b}) - \mathbf{b}|\mathbf{a}|^2$:

$$= -\frac{G_4 Mm\mu^2}{r^3}\left[\mathbf{r}(\mathbf{r}\cdot\dot{\mathbf{r}}) - \dot{\mathbf{r}}r^2\right]$$

For the third term, $d\hat{\mathbf{r}}/dt = [\dot{\mathbf{r}}r - \mathbf{r}\dot{r}]/r^2 = [\dot{\mathbf{r}} - \hat{\mathbf{r}}(\hat{\mathbf{r}}\cdot\dot{\mathbf{r}})]/r$, and using $\mathbf{r}\cdot\dot{\mathbf{r}} = r\dot{r}$:

$$-G_4 Mm\mu^2\frac{d\hat{\mathbf{r}}}{dt} = -\frac{G_4 Mm\mu^2}{r}\left[\dot{\mathbf{r}} - \hat{\mathbf{r}}\dot{r}\right] = -\frac{G_4 Mm\mu^2}{r^3}\left[\dot{\mathbf{r}}r^2 - \mathbf{r}(\mathbf{r}\cdot\dot{\mathbf{r}})\right]$$

Comparing: $\dot{\mathbf{p}} \times \mathbf{L}$ and the third term are exactly equal and opposite. Therefore $\dot{\mathbf{A}} = 0$. The Runge-Lenz vector is conserved — but ONLY for the exact $1/r$ potential. Any deviation from $1/r$ (such as GR corrections, or a different power law) would break this conservation.

We can also verify conservation using the Poisson bracket formalism from Chapter 2 (§2.6). The Hamiltonian is:

$$H = \frac{p^2}{2\mu} - \frac{G_4 Mm}{r}$$

and the Poisson bracket $\{A_i, H\} = 0$ for each component $i$, confirming conservation.

**Physical meaning:** $\mathbf{A}$ points from the focus to the periapsis and has magnitude $|\mathbf{A}| = G_4 Mm\mu^2 e$. Its conservation is the reason the orbit is a *fixed* ellipse — the periapsis does not precess. (When GR corrections are included, $\mathbf{A}$ is no longer exactly conserved, and the periapsis precesses. This is the origin of Mercury's famous 43 arcseconds per century.)

**Why is this important?** The Runge-Lenz vector explains a mystery about the Kepler orbit that conservation of energy and angular momentum alone do NOT explain. Energy determines the size ($a$) and angular momentum determines the shape ($e$) — but neither determines the *orientation* of the ellipse (the direction of periapsis). In a general central force problem, the periapsis would precess, and the orientation would not be a constant of the motion. In the Kepler problem, $\mathbf{A}$ is conserved, which means the periapsis stays fixed. The orbit is a *closed* ellipse, not a precessing one, precisely because this additional symmetry exists.

This is the deeper reason why Kepler orbits close (beyond the apsidal angle argument of §3.7): the Kepler problem has *more symmetry* than a generic central force problem. Three conserved quantities ($E$, $\mathbf{L}$, $\mathbf{A}$) for three degrees of freedom makes the system "maximally superintegrable" — every bounded orbit is periodic.

**Algebraic significance.** The three components of $\mathbf{L}$ and the three components of $\mathbf{A}$ generate an $SO(4)$ symmetry algebra via Poisson brackets (for $E < 0$). The fundamental brackets are:

$$\{L_i, L_j\} = \epsilon_{ijk}L_k, \quad \{L_i, A_j\} = \epsilon_{ijk}A_k, \quad \{A_i, A_j\} = -2\mu E\,\epsilon_{ijk}L_k \tag{3.3.25}$$

This $SO(4)$ symmetry is specific to the $1/r$ potential and is responsible for the "accidental" degeneracy of the hydrogen atom's energy levels — a connection that will become clear in Volume 4. For now, it is enough to note that the zone-derived gravity, by being exactly $1/r^2$, gives the Kepler problem a richer symmetry structure than a generic central force.

---

## §3.6 — Scattering Theory

### §3.6.1 — Hyperbolic Orbits

Why do we study unbound orbits? Because not every encounter between two bodies results in capture. A meteoroid passing through the Solar System, an alpha particle fired at a gold nucleus, a spacecraft performing a gravitational slingshot — all are scattering problems. The physics is the same Binet equation and the same zone-derived force law; only the energy has changed sign.

When $E > 0$, the eccentricity $e > 1$ (from Eq. 3.3.18), and the orbit is a hyperbola. The incoming body approaches from infinity with speed $v_\infty = \sqrt{2E/\mu}$, reaches a distance of closest approach $r_{\min} = p/(1 + e)$, and recedes to infinity along a different asymptotic direction. The question is: by how much is the trajectory deflected?

The orbit equation (3.3.17) still applies. At $r \to \infty$, $u \to 0$, so:

$$0 = \frac{1}{p}[1 + e\cos(\phi_\infty - \phi_0)]$$

which gives $\cos(\phi_\infty - \phi_0) = -1/e$. The asymptotic angles are:

$$\phi_\infty - \phi_0 = \pm\arccos(-1/e) = \pm(\pi - \alpha) \tag{3.3.26}$$

where $\cos\alpha = 1/e$. The total **deflection angle** (the angle between incoming and outgoing asymptotes) is:

$$\chi = \pi - 2\alpha \tag{3.3.27}$$

Using $\cos\alpha = 1/e$ and the identity $\cot(\chi/2) = \cot(\pi/2 - \alpha) = \tan\alpha$, together with $\tan\alpha = \sqrt{e^2 - 1}$ and $e^2 - 1 = 2EL^2/(G_4 Mm\mu)^2$ (from Eq. 3.3.18):

$$\boxed{\cot\frac{\chi}{2} = \frac{b \cdot \mu v_\infty^2}{G_4 Mm}} \tag{3.3.28}$$

where $b = L/(\mu v_\infty)$ is the **impact parameter** (the perpendicular distance between the incoming asymptote and the scattering center) and $v_\infty = \sqrt{2E/\mu}$ is the initial speed at infinity.

### §3.6.2 — The Differential Cross-Section

[FIGURE: Fig 3.3.5 — Scattering geometry: impact parameter to deflection angle]

### §3.6.2 — The Differential Cross-Section

The concept of a cross-section quantifies "how effective is the scattering center at deflecting incoming particles?" Imagine a beam of particles approaching the scattering center (a massive body for gravity, a nucleus for Coulomb). Each particle has a specific impact parameter $b$ — the perpendicular distance between its incoming trajectory and the center. Different impact parameters produce different deflection angles $\chi(b)$, as given by Eq. (3.3.28).

[FIGURE: Fig 3.3.5 — Scattering geometry: impact parameter to deflection angle]

A thin annular ring of particles with impact parameters between $b$ and $b + db$ has cross-sectional area $d\sigma = 2\pi b\,db$ (the area of the ring). These particles are scattered into a cone of solid angle $d\Omega = 2\pi\sin\chi\,|d\chi|$. The **differential cross-section** relates these:

$$\frac{d\sigma}{d\Omega} = \frac{b}{\sin\chi}\left|\frac{db}{d\chi}\right| \tag{3.3.29}$$

This definition is purely geometric — it applies to any central force. The physics enters through the relationship $b(\chi)$.

From Eq. (3.3.28), we can solve for $b$:

$$b = \frac{G_4 Mm}{\mu v_\infty^2}\cot\frac{\chi}{2} = \frac{G_4 Mm}{2E_\text{cm}}\cot\frac{\chi}{2}$$

Differentiating:

$$\left|\frac{db}{d\chi}\right| = \frac{G_4 Mm}{2E_\text{cm}} \cdot \frac{1}{2\sin^2(\chi/2)}$$

Now we need $b/\sin\chi$. Using $\sin\chi = 2\sin(\chi/2)\cos(\chi/2)$ and $b = (G_4 Mm/2E_\text{cm})\cos(\chi/2)/\sin(\chi/2)$:

$$\frac{b}{\sin\chi} = \frac{(G_4 Mm/2E_\text{cm})\cos(\chi/2)/\sin(\chi/2)}{2\sin(\chi/2)\cos(\chi/2)} = \frac{G_4 Mm}{4E_\text{cm}\sin^2(\chi/2)}$$

Multiplying:

$$\boxed{\frac{d\sigma}{d\Omega} = \left(\frac{G_4 Mm}{4E_{\text{cm}}}\right)^2 \frac{1}{\sin^4(\chi/2)}} \tag{3.3.30}$$

where $E_{\text{cm}} = \frac{1}{2}\mu v_\infty^2$ is the center-of-mass kinetic energy.

This is the **Rutherford scattering formula** — derived here for gravity, but equally applicable to the Coulomb force (replace $G_4 Mm$ with $kq_1q_2$). Both forces were derived from zone architecture (gravity in Vol 2 Ch 2, Coulomb in Vol 2 Ch 3), so both scattering cross-sections trace to zone geometry.

**Notable features:**

The cross-section diverges as $\chi \to 0$ (forward scattering). This is because large impact parameters produce small deflections, and the $1/r$ potential has infinite range — particles at arbitrarily large $b$ still feel a (tiny) force. The total cross-section is formally infinite:

$$\sigma_{\text{tot}} = \int\frac{d\sigma}{d\Omega}\,d\Omega \to \infty$$

This is not a pathology — it reflects the fact that gravity (and Coulomb) never truly vanish. In practice, scattering experiments have a finite angular resolution, and the total cross-section is replaced by a cross-section for scattering through angles greater than some minimum $\chi_{\min}$.

The Rutherford formula was historically verified by Geiger and Marsden's alpha particle scattering experiments (1909–1913), which revealed the nuclear structure of atoms. That same formula follows here from zone-derived forces without additional assumptions.

**Worked example: Gravitational scattering — the slingshot maneuver.** When a spacecraft encounters a planet, it follows a hyperbolic orbit around the planet and gains (or loses) speed relative to the Sun. This is the gravitational slingshot effect, used by Voyager 1 and 2 to reach the outer Solar System.

Consider a spacecraft approaching Jupiter ($M_J = 1.898 \times 10^{27}$ kg) with $v_\infty = 10$ km/s and impact parameter $b = 10^9$ m. The deflection angle is:

$$\cot\frac{\chi}{2} = \frac{b v_\infty^2}{G_4 M_J} = \frac{10^9 \times (10^4)^2}{6.674\times 10^{-11} \times 1.898\times 10^{27}} = \frac{10^{17}}{1.266\times 10^{17}} = 0.790$$

So $\chi/2 = 51.7°$ and $\chi = 103°$. The spacecraft's trajectory bends by more than a right angle — a significant deflection that can dramatically alter the spacecraft's heliocentric velocity. In Jupiter's reference frame, the speed is unchanged ($v_\infty$ is the same before and after); but in the Sun's frame, the change in direction translates to a change in speed. This is pure Keplerian physics, derived from zone gravity.

### §3.6.3 — Tidal Forces as a Scattering Application

A related prediction is the tidal acceleration — the differential gravitational acceleration across an extended body. From the zone-derived potential $\Phi = -G_4 M/r$:

$$a_{\text{tidal}} = \frac{2G_4 M}{r^3}\Delta r \tag{3.3.31}$$

where $\Delta r$ is the size of the extended body. For the Moon's tidal effect on Earth:

$$a_{\text{tidal}} = \frac{2G_4 M_{\text{Moon}}}{d^3}R_{\text{Earth}} \tag{3.3.32}$$

Using zone-derived $G_4 = 6.674 \times 10^{-11}$ m³/(kg·s²):

$$a_{\text{tidal}} = \frac{2 \times 6.674\times 10^{-11} \times 7.342\times 10^{22}}{(3.844\times 10^8)^3} \times 6.371\times 10^6 = 1.099 \times 10^{-6} \;\text{m/s}^2$$

Compared to the measured value $1.1 \times 10^{-6}$ m/s², the error is 0.066%.

Why do tidal forces go as $1/r^3$ when gravity goes as $1/r^2$? Because tidal forces are the *gradient* of the gravitational acceleration — the difference in gravitational pull across the finite size of the body. Differentiating $g = G_4 M/r^2$ with respect to $r$ gives $dg/dr = -2G_4 M/r^3$, and the tidal acceleration over a distance $\Delta r$ is $\Delta g = |dg/dr| \Delta r = 2G_4 M \Delta r/r^3$. The extra power of $1/r$ means tidal forces fall off faster than gravity itself — which is why the Moon's tidal effect on Earth is dominated by the Moon (closer) rather than the Sun (more massive but much farther), even though the Sun's gravitational pull on Earth is about 178 times stronger than the Moon's.

Tidal forces have profound astrophysical consequences: ocean tides on Earth (twice daily, from the Moon and Sun), tidal locking (the Moon always shows the same face to Earth because tidal dissipation has synchronized its rotation with its orbit), tidal disruption (a star passing too close to a black hole is torn apart when tidal forces exceed the star's self-gravity, at the Roche limit $r_\text{Roche} \approx R_\star (M_\text{BH}/M_\star)^{1/3}$), and the gradual evolution of the Earth-Moon system (tidal friction transfers angular momentum from Earth's rotation to the Moon's orbit, causing the Moon to recede at 3.8 cm/year and Earth's day to lengthen by about 2.3 milliseconds per century).

All of these phenomena are direct consequences of the $1/r$ gravitational potential derived from zone curvature. The physics of ocean tides, tidal disruption events, and the Moon's recession all trace back to the 6D Einstein-Hilbert action through the same chain we have followed throughout this chapter.

---

## §3.7 — Bertrand's Theorem: Why These Force Laws Are Special

### §3.7.1 — The Question

We have shown that the zone-derived $1/r^2$ force produces orbits that are conic sections — and in particular, that bound orbits are *closed*: the trajectory retraces itself exactly after one revolution. The ellipse does not precess; perihelion stays put. But is this typical? Most students, having seen only gravity and the harmonic oscillator, assume all central forces produce closed orbits. They are wrong — dramatically so.

If the force law were $F \propto 1/r^3$ or $F \propto 1/r^{3/2}$ or any other power law, the orbit would typically *precess*: each revolution, the periapsis would shift by some angle, and the orbit would trace a rosette pattern, never closing. This is not an exotic effect — it is the generic behavior. Closed orbits are the exception, not the rule.

The answer to "which force laws produce closed orbits?" was proved by Joseph Bertrand in 1873, and it is one of the most beautiful results in classical mechanics. Among all central force laws $F(r) = -kr^n$ (with $k > 0$ for attractive forces), only two produce closed orbits for ALL bound initial conditions:

1. $n = -2$: the inverse-square law ($F \propto 1/r^2$) — i.e., zone-derived gravity and Coulomb
2. $n = +1$: the linear restoring force ($F \propto r$) — i.e., the harmonic oscillator

### §3.7.2 — Apsidal Angle Analysis

Consider a nearly-circular orbit under a general central force $F(r)$. At the circular radius $r_0$, the centripetal acceleration equals the force:

$$\frac{L^2}{\mu^2 r_0^3} = |F(r_0)| \tag{3.3.33}$$

Now perturb slightly: let $r = r_0(1 + \epsilon)$ with $|\epsilon| \ll 1$. The effective potential near $r_0$ is approximately quadratic in $\epsilon$:

$$V_{\text{eff}}(r) \approx V_{\text{eff}}(r_0) + \frac{1}{2}\mu\omega_r^2 (r - r_0)^2$$

where the radial oscillation frequency is:

$$\omega_r^2 = \frac{1}{\mu}\frac{d^2 V_{\text{eff}}}{dr^2}\bigg|_{r_0} = -\frac{1}{\mu r_0}\left[3F(r_0) + r_0 F'(r_0)\right] \tag{3.3.34}$$

The orbital frequency (azimuthal) is:

$$\omega_\phi = \frac{L}{\mu r_0^2} = \sqrt{\frac{|F(r_0)|}{\mu r_0}} \tag{3.3.35}$$

The orbit closes if and only if the ratio $\omega_r/\omega_\phi$ is a rational number — so that the radial oscillation returns to its starting point after a whole number of azimuthal revolutions.

For a power-law force $F(r) = -kr^n$:

$$\frac{\omega_r^2}{\omega_\phi^2} = 3 + n \tag{3.3.36}$$

The **apsidal angle** (the angle between successive periapsis and apoapsis) is:

$$\Psi = \frac{\pi}{\omega_r/\omega_\phi} = \frac{\pi}{\sqrt{3 + n}} \tag{3.3.37}$$

For the orbit to close, $\Psi$ must be a rational multiple of $\pi$, which requires $\sqrt{3 + n}$ to be rational. For this to hold for **all** bound orbits (not just nearly-circular ones), Bertrand showed that $\sqrt{3+n}$ must be a positive integer. The only solutions with $n > -3$ (required for stable circular orbits) are:

- $\sqrt{3 + n} = 1 \Rightarrow n = -2$: **inverse-square law** → apsidal angle $= \pi$ (orbit closes in one revolution)
- $\sqrt{3 + n} = 2 \Rightarrow n = 1$: **linear force** → apsidal angle $= \pi/2$ (orbit closes in half a revolution, i.e., an ellipse centered at the force center)

[FIGURE: Fig 3.3.6 — Bertrand's theorem: why only two force laws close orbits]

### §3.7.3 — Proof Sketch

So far we have shown that for *nearly-circular* orbits, the ratio $\omega_r/\omega_\phi = \sqrt{3+n}$ must be rational for the orbit to close. For power-law forces, this ratio is independent of $r_0$ and $L$ — it depends only on $n$. This is already a strong constraint: most values of $n$ give irrational $\sqrt{3+n}$.

But Bertrand's theorem claims something stronger: closed orbits for ALL bound initial conditions, not just nearly-circular ones. The extension to arbitrary eccentricity proceeds in three steps:

**Step 1: The apsidal angle is continuous in eccentricity.** As we deform the orbit from circular ($e = 0$) to eccentric ($e > 0$), the apsidal angle $\Psi(e)$ varies continuously. For $e = 0$, $\Psi(0) = \pi/\sqrt{3+n}$.

**Step 2: A continuous function taking only rational values must be constant.** This is a topological fact: the rationals are nowhere dense in the reals. If $\Psi(e)/\pi$ is always a rational number (required for closed orbits at every eccentricity), and $\Psi(e)$ is continuous, then $\Psi(e)$ must be constant for all $e$ in any connected interval.

**Step 3: The constant must be $\pi/\sqrt{3+n}$.** Since $\Psi(0) = \pi/\sqrt{3+n}$, we need $\Psi(e) = \pi/\sqrt{3+n}$ for all $e$. For this to be rational, $\sqrt{3+n}$ must be a positive integer. The requirement $n > -3$ (for stable circular orbits) restricts us to $\sqrt{3+n} = 1$ ($n = -2$) and $\sqrt{3+n} = 2$ ($n = 1$). Higher integers ($\sqrt{3+n} = 3 \Rightarrow n = 6$, etc.) correspond to repulsive forces that do not produce bound orbits.

The key insight of the proof is the interplay between *analysis* (continuity of $\Psi(e)$) and *number theory* (rational values are sparse). This is why Bertrand's theorem is so powerful: it rules out infinitely many force laws in a single stroke. The detailed proof, including the explicit computation of higher-order corrections to $\Psi(e)$ that confirm the constancy, is developed in Problem 3.11 (Challenge).

**Worked example: Apsidal angle for specific force laws.** Let us verify the formula (3.3.37) for the two special cases:

- **Inverse-square ($n = -2$):** $\Psi = \pi/\sqrt{3+(-2)} = \pi/\sqrt{1} = \pi$. The orbit closes after the particle moves from periapsis to apoapsis and back — one complete revolution of $2\Psi = 2\pi$. This is exactly what we found for Kepler orbits.

- **Harmonic oscillator ($n = +1$):** $\Psi = \pi/\sqrt{3+1} = \pi/2$. The orbit closes after two apsidal passages — half a revolution. The total closure angle is $2\Psi = \pi$. The orbit is an ellipse, but now with the center (not the focus) at the origin. The apsidal angle is half that of the Kepler case, meaning the particle oscillates radially twice per orbit.

- **Cubic ($n = -3$):** $\sqrt{3+(-3)} = 0$. The apsidal angle is infinite — the orbit spirals in or out without bound. Circular orbits exist but are unstable. This illustrates why $n \geq -3$ is required for stable circular orbits.

- **Quartic ($n = -4$):** $\sqrt{3+(-4)} = \sqrt{-1}$ is imaginary. No stable circular orbits exist at all.

### §3.7.4 — Significance for the Zone Framework

Why does Bertrand's theorem matter here? Because it tells us that the zone-derived gravitational force is **mathematically special**. The zone manifold's geometry, through the chain of derivations in Volume 2, produces a force law that sits in a very exclusive club — one of only two force laws in the universe of possibilities that produce closed orbits.

This is not something we demanded. We did not build the zone manifold to produce closed orbits. We derived the gravitational potential from the 6D Einstein-Hilbert action, and closedness came for free. It is, in the language of the framework, a **derived prediction**: the zone architecture gives $1/r^2$ gravity, and Bertrand's theorem guarantees that the resulting orbits close. If the zone architecture had given a slightly different power law — say $1/r^{2.01}$ — planetary orbits would precess, and the Solar System would look qualitatively different.

---

## §3.8 — What Is Derived, What Remains, and What Comes Next

### §3.8.1 — Derivation Inventory

| Result | Derived From | Status |
|--------|-------------|--------|
| Binet's orbit equation (3.3.13) | Euler-Lagrange (Ch 2 Eq. 3.2.12) + angular momentum conservation (Vol 1 Ch 7) | DERIVED |
| Kepler orbit (3.3.17) | Binet's equation + zone-derived $1/r^2$ force (Vol 2 Eq. 2.2.43) | DERIVED |
| Kepler's three laws (3.3.20–3.3.21) | Orbit equation + angular momentum + energy conservation | DERIVED |
| Vis-viva equation (3.3.23) | Energy conservation + orbit parameters | DERIVED |
| Rutherford cross-section (3.3.30) | Orbit equation for $E > 0$ + cross-section definition | DERIVED |
| Bertrand's theorem (3.3.36–3.3.37) | Perturbation of circular orbits + continuity argument | PROVED |
| Runge-Lenz conservation (3.3.24) | Equation of motion for $1/r^2$ force | DERIVED |
| Numerical predictions (3.3.22, 3.3.32) | Zone-derived $G_4$ (Vol 2 Eq. 2.2.29) | VALIDATED (<0.5% error) |

Every result in this chapter traces backward through an unbroken chain to the zone manifold. The force law was derived, not postulated. The mechanics was derived, not assumed. The agreement with observation was predicted, not fitted.

### §3.8.2 — The Epistemic Achievement

It is worth pausing to appreciate what the derivation chain accomplishes. Standard physics begins with Newton's law of gravitation as an empirical fact: "there exists a force $F = GMm/r^2$, where $G$ is measured to be $6.674 \times 10^{-11}$." The Kepler problem is then solved as an application of that empirical law. The result is correct, but the student is left with the question: *why* $1/r^2$? Why not $1/r^3$? Why that particular value of $G$?

In the zone framework, these questions have answers. The $1/r^2$ force law follows from the 6D Einstein-Hilbert action via Kaluza-Klein reduction — it is the unique spherically symmetric solution of the 4D Poisson equation projected from the zone manifold (Vol 2, §2.4). The value of $G_4$ is determined by the membrane tension $\sigma$ and effective coupling length $L_\text{eff}$ (Vol 2, Eq. 2.2.29). And Bertrand's theorem (§3.7) tells us that this particular force law is one of only two that produce closed orbits — a mathematical fact that the zone framework inherits rather than demands.

The Kepler problem is not merely *solvable* in the zone framework. It is *derivable*. The student who finishes this chapter knows not just how to compute orbits, but *why* orbits have the shapes they do, all the way down to the geometry of the extra dimensions.

### §3.8.3 — Honest Limits

Every honest physics textbook tells you what it has NOT proven. Here is our inventory:

**1. General relativistic corrections.** The Newtonian treatment is the weak-field, low-velocity limit of full GR (which itself is the 4D limit of the 6D zone manifold Einstein equations). Effects like perihelion precession require the full Schwarzschild metric from Vol 2, Ch 2.

Mercury's perihelion advances by 43 arcseconds per century beyond what Newtonian mechanics predicts. This excess is explained by the GR correction term $-G_4 ML^2/(\mu c^2 r^3)$ added to the effective potential (Problem 3.13). The correction is small — it changes $V_\text{eff}$ by less than one part in $10^7$ at Mercury's orbit — but its effect accumulates over centuries and is precisely measured. This correction does NOT invalidate the Newtonian results of this chapter; it *refines* them. The Newtonian results hold when $v \ll c$ and $r \gg r_s = 2G_4 M/c^2$.

Other GR effects beyond Newtonian mechanics: gravitational radiation (binary pulsars lose orbital energy by emitting gravitational waves, as predicted by the quadrupole formula from Vol 2's field equations), Lense-Thirring precession from rotating masses (verified by Gravity Probe B at 0.43% accuracy, as computed in the test suite), and strong-field phenomena (black holes, neutron stars) where the Newtonian limit breaks down entirely.

**2. The N-body problem.** The two-body central force problem is exactly solvable. The three-body problem is not (Poincaré, 1890). This is not a limitation of the zone framework — it is a mathematical fact about nonlinear differential equations. Planetary perturbations, orbital resonances (Jupiter's moons, the Kirkwood gaps in the asteroid belt), and chaotic dynamics (Pluto's orbit, long-term Solar System stability) require perturbation theory or numerical methods. The zone framework provides the *exact* force law; solving the many-body equations of motion is a separate mathematical challenge.

**3. Non-gravitational perturbations.** Atmospheric drag (ISS loses ~2 km altitude per month without reboosts), solar radiation pressure (significant for interplanetary dust and solar sails), tidal dissipation (the Moon recedes from Earth by 3.8 cm/year), and the Yarkovsky effect (thermal radiation modifies asteroid orbits) all modify real orbits. These are secondary effects that rest on the gravitational foundation derived here and involve other zone-derived interactions (electromagnetic, thermal).

### §3.8.4 — What Comes Next

Chapter 4 (Rigid Body Dynamics) extends the machinery to extended objects — rotation, angular momentum of composite systems, and precession. Where this chapter treated the orbiting body as a point mass, Chapter 4 will account for its finite size, shape, and internal rotation. The tidal forces derived in §3.6.3 will return as the driver of tidal locking and tidal deformation. The moment of inertia tensor will extend the scalar $\mu$ of this chapter to a matrix that depends on the body's mass distribution.

Chapter 5 (Continuum Mechanics and Fluid Dynamics) takes the final step from particles to fields, connecting back to the Waters field equations of Vol 1 Ch 6. Where this chapter followed individual trajectories, Chapter 5 will follow entire flows — the continuous limit of infinitely many particles.

The central force problem will return in Volume 4 (Quantum Mechanics), where the Kepler problem becomes the hydrogen atom. The $SO(4)$ symmetry discovered here (§3.5.3) will explain the "accidental" degeneracy of hydrogen's energy levels — the fact that the energy depends only on the principal quantum number $n$ and not on the angular momentum quantum number $\ell$. In standard quantum mechanics, this degeneracy is called "accidental" because it is not explained by the obvious $SO(3)$ rotational symmetry. But it is not accidental at all — it is the quantum manifestation of the classical Runge-Lenz conservation, which itself traces to the exact $1/r$ form of the zone-derived Coulomb potential.

The deep connection between classical orbits and quantum energy levels, first recognized by Pauli (1926) and Fock (1935), is another prediction that emerges naturally from the zone framework. The $SO(4)$ symmetry we derived from Poisson brackets (Eq. 3.3.25) will become the $SO(4)$ symmetry of the hydrogen atom's Hilbert space — the same algebra, promoted from classical to quantum via the canonical quantization procedure $\{,\} \to (i\hbar)^{-1}[,]$ that Volume 4 will develop.

---

## Problems

### Computational

**Problem 3.1.** A satellite orbits Earth in an elliptical orbit with perigee altitude 200 km and apogee altitude 36,000 km above Earth's surface. Using the zone-derived $G_4 = 6.674 \times 10^{-11}$ m³/(kg·s²):
(a) Calculate the semi-major axis, eccentricity, and orbital period.
(b) Calculate the speed at perigee and apogee using the vis-viva equation.
(c) Calculate the specific orbital energy and angular momentum.

**Problem 3.2.** Plot the effective potential $V_{\text{eff}}(r)$ for the gravitational central force with $\mu = 1$ kg, $G_4 M = 1$ m³/s², and $L/(m) = 1, 2, 3$ m²/s. On each plot, mark the circular orbit radius and energy.

**Problem 3.3.** A Hohmann transfer orbit moves a spacecraft from a circular orbit of radius $r_1$ to a circular orbit of radius $r_2 > r_1$. Using the vis-viva equation, derive the two required velocity changes $\Delta v_1$ and $\Delta v_2$, and show that the total $\Delta v$ is minimized by this two-impulse transfer among all coplanar two-impulse transfers.

**Problem 3.4.** Alpha particles ($Z = 2$, $E_{\text{cm}} = 7.7$ MeV) scatter off a gold nucleus ($Z = 79$). Calculate the Rutherford differential cross-section at $\chi = 45°$, $90°$, and $135°$. (Use $kq_1 q_2 = Z_1 Z_2 e^2/(4\pi\epsilon_0)$ in place of $G_4 Mm$ — the formula is identical because the Coulomb force is also $1/r^2$.)

**Problem 3.5.** Compute the Kepler periods for Mars ($a = 1.524$ AU), Jupiter ($a = 5.203$ AU), and Saturn ($a = 9.537$ AU) using zone-derived $G_4$ and $M_\odot = 1.989 \times 10^{30}$ kg. Compare with observed periods (687, 4333, and 10759 days respectively). Do the errors remain below 0.5%? [Note: This problem extends the test suite validation from three bodies (Mercury, Earth, Moon) to six. The zone-derived $G_4$ makes a single prediction; every planet tests it independently.]

### Conceptual

**Problem 3.6.** Why doesn't the Moon spiral into Earth? Explain using the effective potential. What would have to change for the Moon to spiral inward?

**Problem 3.7.** Kepler's Second Law holds for ANY central force, but the First and Third Laws do not. Explain why, tracing the distinction to which properties of the force law are used in each derivation.

**Problem 3.8.** If the zone manifold produced a gravitational constant $G_4$ twice as large as observed, how would the following change: (a) Earth's orbital period, (b) escape speed from Earth's surface, (c) the Rutherford scattering cross-section for gravity?

**Problem 3.9.** Cometary orbits often have eccentricities very close to 1 (nearly parabolic). Explain why this is expected from the energy distribution of objects captured from the Oort Cloud. What does $e \approx 1$ tell you about the comet's energy relative to $E = 0$?

**Problem 3.10.** The Laplace-Runge-Lenz vector is conserved only for the exact $1/r$ potential. If the force law were $F = -G_4 Mm/r^{2+\epsilon}$ with $\epsilon \ll 1$, how would the orbit change? Connect this to Mercury's perihelion precession as a GR effect.

### Challenge

**Problem 3.11.** (Bertrand's theorem — full proof) Starting from the apsidal angle for nearly-circular orbits (Eq. 3.3.37), extend the proof to all bound orbits. Show that the requirement of closed orbits for *arbitrary* eccentricities, combined with the power-law assumption, restricts $n$ to exactly $\{-2, +1\}$. [Hint: Expand the apsidal angle in powers of the orbit eccentricity and demand rationality at each order.]

**Problem 3.12.** Show that the six quantities $(L_1, L_2, L_3, A_1, A_2, A_3)$ — where $\mathbf{L}$ is angular momentum and $\mathbf{A}$ is the Runge-Lenz vector — satisfy an $SO(4)$ Poisson bracket algebra (Eq. 3.3.25) for bound orbits ($E < 0$). [Hint: Define $\mathbf{M} = \mathbf{A}/\sqrt{-2\mu E}$ and compute $\{L_i, M_j\}$ and $\{M_i, M_j\}$.]

**Problem 3.13.** (Mercury's perihelion precession — the classical test of General Relativity)

The leading GR correction to the Newtonian effective potential is:

$$V_{\text{eff}}^{\text{GR}}(r) = -\frac{G_4 Mm}{r} + \frac{L^2}{2\mu r^2} - \frac{G_4 M L^2}{\mu c^2 r^3}$$

The last term comes from the Schwarzschild metric (Vol 2, Ch 2). Show that this produces a perihelion advance per orbit of:

$$\Delta\phi = \frac{6\pi G_4 M}{c^2 a(1-e^2)}$$

Evaluate for Mercury ($a = 5.791 \times 10^{10}$ m, $e = 0.2056$) and verify the famous result $\Delta\phi \approx 43''$ per century. This 43 arcseconds per century — unexplained from 1859 (Le Verrier's discovery of the anomaly) to 1915 (Einstein's General Relativity) — is one of the most celebrated predictions in physics. In the zone framework, it arises from the Schwarzschild solution of Vol 2, Ch 2: the extra $-G_4 ML^2/(\mu c^2 r^3)$ term modifies the effective potential just enough to make the orbit precess, breaking the exact Runge-Lenz conservation and Bertrand closure that the Newtonian limit preserves.

---

## Chapter Summary

This chapter is the first place in the Foundations series where the zone framework produces *quantitative predictions that can be checked against the sky*. Volumes 1 and 2 built the architecture and derived the forces. Chapters 1 and 2 of this volume derived the mechanics. Now, for the first time, all of that machinery has been pointed at nature — and nature said yes.

Central force problems are where the zone framework proves its worth as a *practical* physics tool. Starting from the gravitational potential derived in Volume 2 and the mechanics formalism of Chapters 1–2, we derived:

**Binet's equation** (3.3.13) — the general orbit equation for any central force, a direct consequence of the Euler-Lagrange formalism.

**Kepler's three laws** — not empirical rules, but theorems of the zone framework. Elliptical orbits (3.3.17) follow from the $1/r$ potential; equal areas in equal times (3.3.20) from angular momentum conservation; the period relation (3.3.21) from the interplay of both.

**Orbital energetics** — the vis-viva equation (3.3.23) and the Laplace-Runge-Lenz vector (3.3.24), revealing the hidden $SO(4)$ symmetry of the Kepler problem.

**Scattering theory** — the Rutherford cross-section (3.3.30), derived from the same orbit equation applied to unbound trajectories.

**Bertrand's theorem** (3.3.37) — the zone-derived $1/r^2$ force is one of only two force laws that produce closed orbits. This is not a coincidence but a derived consequence of zone geometry.

**Numerical validation** — Kepler periods for Mercury (0.012% error), Earth (0.011%), and Moon (0.477%); tidal forces (0.066% error); geodetic precession (0.43% error); all using the zone-derived $G_4$ with no free parameters.

The complete validation suite (run by `test_gravity_kinematics.py`) confirms five independent predictions at better than 5% accuracy, with most well below 1%. These are not fitting parameters — they are predictions from the zone manifold's geometry, checked against centuries of astronomical observation.

Every result traces backward through an unbroken chain: zone manifold → gravity → mechanics → orbits → predictions → agreement with nature.

---

*Next: Chapter 4 — Rigid Body Dynamics, where the machinery extends from point particles to extended objects.*
