# Chapter 2: Lagrangian and Hamiltonian Mechanics

## The Variational Foundations of Classical Dynamics

---

> *"The action is the hero of the story."*
> — attributed to Richard Feynman

---

## §2.1 Why Formalism Matters — From F=ma to the Action Principle

Chapter 1 accomplished something that standard physics textbooks skip: it derived F=ma from the geometry of the zone manifold. The student now holds Newton's three laws not as axioms but as theorems, traced back to the zone action, the geodesic equation, and covariant conservation of stress-energy. Per Ch 1 §1.1, the test-particle action used in that derivation descends from the Firmament metric established in Vol 1 Ch 5 — the induced metric on the *rāqîaʿ* of Gen 1:6–8. Everything in this chapter inherits that pedigree.

But there's a problem.

F=ma, as Newton formulated it, is a *vector equation.* It works beautifully when you can identify all the forces and decompose them into Cartesian components. For a ball rolling down a smooth incline, you draw the free-body diagram, resolve forces, and apply $m\mathbf{a} = \sum\mathbf{F}$. The calculation takes half a page.

Now consider a double pendulum — a pendulum hanging from the end of another pendulum. Two masses, two rigid rods, four forces (two tensions, two weights). The constraint forces (tensions) do no work, but they couple the motion of both masses. In Cartesian coordinates, you have four equations of motion, four constraint equations, and six unknowns (four positions plus two tensions). The problem is solvable, but brutally complicated. The constraint forces — which you don't care about — dominate the algebra.

Or consider a bead sliding on a rotating wire hoop. Or the three-body gravitational problem. Or $10^{23}$ molecules in a gas. In each case, the Newtonian approach buries the physics under constraint forces that you must track but don't want.

There must be a better way. And there is — and it isn't new. It's the *same* variational principle that the zone framework is built upon.

Recall what Volume 1, Chapter 8 established: the Five Principles constrain the zone action $S_\text{total}$ (Eq. 1.8.3). The physical field configurations are stationary points of that action. Volume 2, Chapter 5 constructed the complete zone Lagrangian $\mathcal{L}_\text{zone}$ (Eq. 2.5.20) and derived every field equation from $\delta S_\text{total} = 0$ (Eq. 2.5.21). Chapter 1 of this volume extracted F=ma by varying the test particle action (Eq. 3.1.7) with respect to the worldline.

In every case, the method was the same: **write the action, vary it, set the variation to zero.** This is the variational principle — the engine beneath everything.

This chapter does not introduce a new principle. It *systematizes* the principle you already know. The Lagrangian formulation is the systematic application of $\delta S = 0$ to particle mechanics. The Hamiltonian formulation is a mathematical reshaping of the same content that reveals deeper structure. Both are already implicit in the zone framework. We're making them explicit.

Here is the program:

- **§2.2** derives the particle Lagrangian from the zone Lagrangian — showing that $L = T - V$ is not a postulate but a consequence of dimensional reduction.
- **§2.3** derives the Euler-Lagrange equations and shows they reproduce F=ma (consistency with Chapter 1).
- **§2.4** introduces the Legendre transform and constructs the Hamiltonian.
- **§2.5** derives Hamilton's equations and explores phase space.
- **§2.6** develops Poisson brackets — the algebraic structure of classical mechanics.
- **§2.7** treats canonical transformations — the symmetries of phase space.
- **§2.8** presents the Hamilton-Jacobi equation — the bridge to quantum mechanics.
- **§2.9** takes stock of what was derived and what comes next.

[FIGURE: Fig 3.2.1 — From Zone Lagrangian to Particle Mechanics. Flowchart: Zone Action (Vol 2 Ch 5, Eq. 2.5.1) → KK reduction to 4D → 4D effective action → test particle limit → particle Lagrangian $L(q, \dot{q}, t)$ → Euler-Lagrange equations → F=ma (Ch 1, Eq. 3.1.10). Also: Particle Lagrangian → Legendre transform → Hamiltonian $H(q, p, t)$ → Hamilton's equations → Poisson brackets → canonical transformations → Hamilton-Jacobi. Color code: orange = Vol 2 results, blue = Ch 1 results, green = this chapter's new derivations.]

---

## §2.2 The Particle Lagrangian from the Zone Action

> **Notation convention.** This chapter works at two scales: the *field* level (zone Lagrangian density $\mathcal{L}$, field Hamiltonian density $\mathcal{H}$) and the *particle* level (particle Lagrangian $L$, particle Hamiltonian $H$). Calligraphic letters ($\mathcal{L}$, $\mathcal{H}$) always denote field-level densities on the zone manifold; italic letters ($L$, $H$) always denote particle-level functions of generalized coordinates and momenta. The Einstein summation convention (repeated indices summed) is used throughout; all summation indices run over the 4D spacetime or $n$-dimensional configuration space unless explicitly stated otherwise. Summation over 6D zone-manifold indices is always written with explicit limits.

### §2.2.1 The Chain of Reduction

The zone Lagrangian (Vol 2, Ch 5, Eq. 2.5.20) is a density on the 6D zone manifold:

$$\mathcal{L}_\text{zone} = \frac{1}{2\kappa_6^2} R_6 + \mathcal{L}_\text{Firm}\,\delta_\Sigma + \mathcal{L}_\text{waters} + \mathcal{L}_\text{gauge} + \mathcal{L}_\text{matter} + \mathcal{L}_\text{Yukawa} + \kappa(t)\,\mathcal{O}_\text{sustain} \tag{2.5.20}$$

This describes everything: geometry, fields, forces, matter, and sustaining. But a single particle — an electron moving through space, say — doesn't need the full 6D field theory. It needs the *effective* description: what does the zone framework predict for the trajectory of a localized object?

The reduction proceeds in three steps:

**Step 1: From 6D to 4D (Kaluza-Klein Reduction).** Volume 2, Chapter 5, §5.5 showed that integrating the zone Lagrangian over the two extra dimensions $(\xi, \eta)$ yields an effective 4D Lagrangian. The gravitational sector produces the 4D Einstein-Hilbert action. The gauge sectors produce the Standard Model gauge Lagrangian. The matter sector produces 4D Dirac fields. All coupling constants become integrals of warp factors over the extra dimensions.

**Step 2: From 4D Fields to Test Particle.** When we focus on a single localized particle (a "test particle" — one whose own gravitational and electromagnetic fields are negligible), the full 4D field theory reduces to the test particle action. Chapter 1 already wrote this down (Eq. 3.1.7):

$$S_\text{particle} = -m \int d\tau + \int f_\mu \, dx^\mu \tag{3.1.7}$$

where $m$ is the rest mass and $f_\mu$ encodes external forces. This is the particle's worldline action — the action for a 0-dimensional object (a point) moving through 4D spacetime.

**Step 3: From Relativistic to Non-Relativistic.** In the non-relativistic limit ($v \ll c$, weak fields), the proper time $d\tau \approx dt$, and the test particle action becomes:

$$S = \int_{t_1}^{t_2} L(q^i, \dot{q}^i, t) \, dt \tag{3.2.1}$$

where $L$ is the **Lagrangian** — a function of generalized coordinates $q^i$, their time derivatives $\dot{q}^i$, and possibly time $t$.

### §2.2.2 Deriving $L = T - V$

Let's perform Step 3 explicitly. Start with the test particle action (Eq. 3.1.7) in the non-relativistic limit. For a particle of mass $m$ in a gravitational potential $\Phi(\mathbf{x})$ and an electromagnetic potential $(V_{\text{EM}}, \mathbf{A})$:

Why proper time? A relativistic particle's worldline is a curve through spacetime, and we need a parameter to measure "how much time the particle experiences" along that curve — independent of any observer's clock. Proper time $\tau$ is that parameter: it is the elapsed time measured by a clock traveling with the particle. It is the natural choice because it is a Lorentz scalar — all observers agree on its value — which means an action built from $d\tau$ is automatically coordinate-invariant, inheriting the diffeomorphism invariance of the zone manifold. The proper time element is:

$$d\tau = \sqrt{1 - v^2/c^2} \, dt \approx \left(1 - \frac{v^2}{2c^2}\right) dt$$

So the free-particle action becomes:

$$-mc^2 \int d\tau \approx -mc^2 \int \left(1 - \frac{v^2}{2c^2}\right) dt = \int \left(-mc^2 + \frac{1}{2}mv^2\right) dt$$

The constant $-mc^2$ doesn't affect the equations of motion (it vanishes under variation), so we can drop it. The gravitational coupling adds $-m\Phi$, and the electromagnetic coupling adds $q(\mathbf{A} \cdot \mathbf{v} - V_{\text{EM}})$. Collecting terms:

$$L = \frac{1}{2}m|\dot{\mathbf{x}}|^2 - m\Phi(\mathbf{x}) - qV_{\text{EM}}(\mathbf{x}) + q\mathbf{A}(\mathbf{x}) \cdot \dot{\mathbf{x}} \tag{3.2.2}$$

For a purely mechanical system (no electromagnetic fields), this simplifies to:

$$\boxed{L = T - V = \frac{1}{2}m|\dot{\mathbf{x}}|^2 - V(\mathbf{x}) \quad \text{(Eq. 3.2.3)}}$$

where $T = \frac{1}{2}mv^2$ is the kinetic energy and $V = m\Phi$ is the potential energy.

**This is not a postulate.** It is the non-relativistic limit of the test particle action on the zone manifold. The student has now seen $L = T - V$ derived, not assumed. Every textbook that starts with "the Lagrangian is $T - V$" is starting in the middle of the story. The beginning of the story is the zone action.

### §2.2.3 Generalized Coordinates

The power of the Lagrangian formulation lies in its indifference to coordinates. The action (Eq. 3.2.1) is a scalar — it doesn't care whether you describe the particle's position in Cartesian, polar, spherical, or any other coordinate system. Why? Because the action is an integral of $L\,dt$, and $L$ was derived from the test particle action $-m\int d\tau + \int f_\mu dx^\mu$, which is built from geometric objects (proper time, the force one-form) that have no preferred coordinate system. The coordinate-freedom of the particle action is a direct inheritance from the zone manifold's diffeomorphism invariance (Vol 1, Ch 7): physics is independent of how you label points.

Let $q^1, q^2, \ldots, q^n$ be any set of $n$ independent coordinates that describe the system's configuration. These are **generalized coordinates**. They need not be lengths or angles; they need only specify the system's state uniquely. The number $n$ is the number of **degrees of freedom**.

For a single particle in 3D space without constraints: $n = 3$, and $(q^1, q^2, q^3)$ could be $(x, y, z)$ or $(r, \theta, \phi)$ or any other set.

For a double pendulum confined to a plane: $n = 2$, and $(q^1, q^2) = (\theta_1, \theta_2)$ — the two angles. The constraint forces (tensions) disappear from the problem entirely.

**This is the practical payoff.** In the Newtonian approach, constraints introduce forces you must track. In the Lagrangian approach, constraints reduce the number of coordinates. You never see the tension in a pendulum rod; you work directly with the angle.

The kinetic energy in generalized coordinates takes the form:

$$T = \frac{1}{2} \sum_{i,j} M_{ij}(q) \, \dot{q}^i \dot{q}^j \tag{3.2.4}$$

where $M_{ij}(q)$ is the **mass matrix** (or inertia tensor in generalized coordinates), which depends on the coordinates but not on velocities. This quadratic form in velocities is a direct consequence of the metric structure of the zone manifold: the kinetic energy is the squared length of the velocity vector, measured with the metric.

The Lagrangian becomes:

$$L(q, \dot{q}, t) = \frac{1}{2} M_{ij}(q) \dot{q}^i \dot{q}^j - V(q, t) \tag{3.2.5}$$

### §2.2.4 Constraints and Degrees of Freedom

A system of $N$ particles in 3D has $3N$ Cartesian coordinates. If $k$ constraint equations relate these coordinates:

$$f_\alpha(x_1, y_1, z_1, \ldots, x_N, y_N, z_N, t) = 0, \quad \alpha = 1, \ldots, k \tag{3.2.6}$$

then the system has $n = 3N - k$ degrees of freedom. By choosing generalized coordinates $(q^1, \ldots, q^n)$ that automatically satisfy the constraints, the constraint forces vanish from the Lagrangian.

There is a deep connection here to the zone framework. In Volume 1, Chapter 8, the Five Principles were expressed as constraint functionals $\mathcal{C}_i[S]$ (Eq. 1.8.2), and the constrained action was formed using Lagrange multipliers (Eq. 1.8.3). The method we're using here for mechanical constraints — reducing coordinates to eliminate constraint forces — is the same mathematical technique applied at a different scale. The zone action has constraints that narrow the space of valid field configurations; a mechanical system has constraints that narrow the space of valid particle configurations. In both cases, the right choice of variables makes the constraints invisible.

---

## §2.3 The Euler-Lagrange Equations

### §2.3.1 The Variational Principle

The action for a mechanical system is:

$$S[q] = \int_{t_1}^{t_2} L(q^i, \dot{q}^i, t) \, dt \tag{3.2.7}$$

The principle of stationary action states: the physical trajectory $q^i(t)$ is the one that makes $S$ stationary with respect to small variations $\delta q^i(t)$ that vanish at the endpoints:

$$\delta S = 0 \quad \text{for all } \delta q^i \text{ with } \delta q^i(t_1) = \delta q^i(t_2) = 0 \tag{3.2.8}$$

This is not a new principle. It is the *same* principle that governs the zone action (Vol 2 Ch 5, Eq. 2.5.21): $\delta S_\text{total} = 0$. The zone action is a functional of fields $\phi^a(x^A)$ over 6D spacetime. The particle action is a functional of trajectories $q^i(t)$ over 1D time. The mathematics is identical; the domain is different.

### §2.3.2 Derivation

We compute $\delta S$ by substituting $q^i(t) + \delta q^i(t)$ into the action and expanding to first order:

$$\delta S = \int_{t_1}^{t_2} \left[ \frac{\partial L}{\partial q^i} \delta q^i + \frac{\partial L}{\partial \dot{q}^i} \delta \dot{q}^i \right] dt \tag{3.2.9}$$

where we sum over repeated indices $i$. Since $\delta \dot{q}^i = d(\delta q^i)/dt$, integrate the second term by parts:

$$\int_{t_1}^{t_2} \frac{\partial L}{\partial \dot{q}^i} \frac{d(\delta q^i)}{dt} dt = \left[ \frac{\partial L}{\partial \dot{q}^i} \delta q^i \right]_{t_1}^{t_2} - \int_{t_1}^{t_2} \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}^i}\right) \delta q^i \, dt \tag{3.2.10}$$

The boundary term vanishes because $\delta q^i(t_1) = \delta q^i(t_2) = 0$. Combining:

$$\delta S = \int_{t_1}^{t_2} \left[ \frac{\partial L}{\partial q^i} - \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}^i}\right) \right] \delta q^i \, dt = 0 \tag{3.2.11}$$

Since $\delta q^i(t)$ is arbitrary (subject to endpoint conditions), the integrand must vanish for each $i$:

$$\boxed{\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}^i}\right) - \frac{\partial L}{\partial q^i} = 0, \quad i = 1, \ldots, n \quad \text{(Eq. 3.2.12)}}$$

These are the **Euler-Lagrange equations** — $n$ second-order ordinary differential equations for the $n$ generalized coordinates. They are the necessary and sufficient conditions for a trajectory to be a stationary point of the action.

### §2.3.3 Consistency Check: Recovering F=ma

For a single particle in Cartesian coordinates with $L = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - V(x, y, z)$:

$$\frac{\partial L}{\partial \dot{x}} = m\dot{x}, \quad \frac{d}{dt}(m\dot{x}) = m\ddot{x}$$

$$\frac{\partial L}{\partial x} = -\frac{\partial V}{\partial x}$$

The Euler-Lagrange equation for $x$ gives:

$$m\ddot{x} = -\frac{\partial V}{\partial x} = F_x$$

This is precisely Newton's Second Law (Eq. 3.1.10 from Chapter 1). The Euler-Lagrange equations and the direct variational derivation of Chapter 1 agree exactly. $\checkmark$

### §2.3.4 The Power of Generalized Coordinates: Worked Examples

**Example 1: The Simple Pendulum**

A mass $m$ hangs from a rigid, massless rod of length $\ell$, swinging in a vertical plane. The Newtonian approach requires resolving gravity and tension into tangential and radial components. The Lagrangian approach uses one coordinate: the angle $\theta$.

Kinetic energy: $T = \frac{1}{2}m\ell^2\dot{\theta}^2$

Potential energy (with zero at the pivot): $V = -mg\ell\cos\theta$

Lagrangian:
$$L = \frac{1}{2}m\ell^2\dot{\theta}^2 + mg\ell\cos\theta \tag{3.2.13}$$

Euler-Lagrange:
$$\frac{d}{dt}(m\ell^2\dot{\theta}) + mg\ell\sin\theta = 0$$

$$\boxed{\ddot{\theta} + \frac{g}{\ell}\sin\theta = 0 \quad \text{(Eq. 3.2.14)}}$$

One equation, one unknown. The tension never appears. The constraint (fixed rod length) was absorbed into the choice of coordinate $\theta$.

For small angles ($\sin\theta \approx \theta$), this reduces to simple harmonic motion with period $T = 2\pi\sqrt{\ell/g}$. The constraint force — the tension — does no work and carries no physical information about the pendulum's oscillation. The Lagrangian approach discards it automatically.

**Example 2: The Double Pendulum**

Two masses $m_1$ and $m_2$ connected by rigid rods of lengths $\ell_1$ and $\ell_2$. Generalized coordinates: $(\theta_1, \theta_2)$.

The positions are:

$$x_1 = \ell_1\sin\theta_1, \quad y_1 = -\ell_1\cos\theta_1$$
$$x_2 = \ell_1\sin\theta_1 + \ell_2\sin\theta_2, \quad y_2 = -\ell_1\cos\theta_1 - \ell_2\cos\theta_2$$

Kinetic energy:

$$T = \frac{1}{2}m_1\ell_1^2\dot{\theta}_1^2 + \frac{1}{2}m_2\left[\ell_1^2\dot{\theta}_1^2 + \ell_2^2\dot{\theta}_2^2 + 2\ell_1\ell_2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1 - \theta_2)\right] \tag{3.2.15}$$

Potential energy:

$$V = -(m_1 + m_2)g\ell_1\cos\theta_1 - m_2 g\ell_2\cos\theta_2 \tag{3.2.16}$$

The Lagrangian $L = T - V$ gives two coupled Euler-Lagrange equations — complex, but systematically derivable. The four constraint forces (two tensions, each with two components) never appear. A problem that would be nightmarish in Newtonian mechanics becomes merely algebraically tedious in the Lagrangian approach.

This is not a mathematical trick. It is a consequence of the zone framework's variational foundation: because physics is governed by the action, and the action is a scalar, the equations of motion can be expressed in *any* coordinates without introducing fictitious forces.

### §2.3.5 Constrained Systems and Lagrange Multipliers

Sometimes constraints are useful — you *want* to know the constraint force (e.g., when does a bead fly off a wire?). The Lagrangian approach handles this via Lagrange multipliers, exactly as the zone framework handles the Five Principles (Vol 1, Ch 8, §8.3.3).

For a constraint $f(q^1, \ldots, q^n, t) = 0$, augment the Lagrangian:

$$L' = L + \lambda f(q, t) \tag{3.2.17}$$

The Euler-Lagrange equations for $L'$ with respect to $q^i$ give:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}^i}\right) - \frac{\partial L}{\partial q^i} = \lambda \frac{\partial f}{\partial q^i} \tag{3.2.18}$$

The right-hand side is the constraint force. The Euler-Lagrange equation for $\lambda$ recovers the constraint $f = 0$.

Compare this directly with the constrained zone action (Vol 1, Ch 8, Eq. 1.8.3):

$$S_\text{constrained}[\phi^a, \lambda_i] = S_\text{total}[\phi^a] + \sum_i \lambda_i \mathcal{C}_i[\phi^a] \tag{1.8.3}$$

The structure is identical. Lagrange multipliers are Lagrange multipliers, whether they constrain a bead on a wire or the zone action under the Five Principles. The zone framework uses the same mathematics at every scale.

### §2.3.6 Noether's Theorem for Particle Mechanics

Volume 1, Chapter 7 derived Noether's theorem for the zone action: every continuous symmetry produces a conserved current. The same theorem applies to the particle Lagrangian, and the proof is simpler because we're in one dimension (time) instead of six.

**Theorem (Noether).** If the Lagrangian $L(q, \dot{q}, t)$ is invariant under a continuous transformation $q^i \to q^i + \epsilon\,\delta q^i$ (to first order in $\epsilon$), then the quantity:

$$\boxed{Q = \frac{\partial L}{\partial \dot{q}^i}\delta q^i \quad \text{(Eq. 3.2.19)}}$$

is conserved: $dQ/dt = 0$ along solutions of the Euler-Lagrange equations.

**Proof.** The invariance condition is $\delta L = 0$ under $q^i \to q^i + \epsilon\,\delta q^i$:

$$\delta L = \frac{\partial L}{\partial q^i}\delta q^i + \frac{\partial L}{\partial \dot{q}^i}\delta\dot{q}^i = 0$$

Using the Euler-Lagrange equations (3.2.12) to replace $\partial L/\partial q^i$:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}^i}\right)\delta q^i + \frac{\partial L}{\partial \dot{q}^i}\frac{d(\delta q^i)}{dt} = \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}^i}\delta q^i\right) = 0$$

Therefore $Q = \frac{\partial L}{\partial \dot{q}^i}\delta q^i$ is constant in time. $\square$

**Applications:**

| Symmetry | Transformation | Conserved Quantity |
|----------|---------------|--------------------|
| Spatial translation in $x$ | $\delta x = 1$ | Linear momentum $p_x = m\dot{x}$ |
| Rotation about $z$-axis | $\delta\phi = 1$ | Angular momentum $L_z = mr^2\dot{\phi}$ |
| Time translation ($\partial L/\partial t = 0$) | $\delta t = 1$ | Energy $H = \sum_i p_i\dot{q}^i - L$ |

The last line deserves emphasis: **when the Lagrangian has no explicit time dependence, the energy is conserved.** This follows from the Symmetry Principle (Vol 1, Ch 8, §8.6): God's unchanging nature implies time-translation invariance, which implies energy conservation. We proved this at the zone level in Vol 1, Ch 7. Now we see it again at the particle level. Same principle, same consequence, different scale.

---

## §2.4 The Legendre Transform — From Velocities to Momenta

### §2.4.1 Why Transform?

The Lagrangian $L(q, \dot{q}, t)$ is a function of coordinates and velocities. The equations of motion (3.2.12) are $n$ second-order ODEs. This is natural for the configuration-space picture: you specify positions and velocities at one time, and the equations predict positions and velocities at all other times.

But there's another picture — and it will prove more fundamental.

Instead of positions and velocities, consider positions and *momenta*. The reason is threefold:

1. **Thermodynamics and statistical mechanics** (Chapters 9–12 of this volume) operate in phase space $(q, p)$, not configuration space $(q, \dot{q})$. The entropy, partition function, and Boltzmann distribution are all defined on phase space. The Degradation Principle (Vol 1, Ch 8, §8.7.5) is naturally expressed as a constraint on Hamiltonian flow in phase space (Eq. 1.8.29).

2. **Quantum mechanics** (Volume 4) replaces classical phase-space variables with operators satisfying $[\hat{q}, \hat{p}] = i\hbar$. This commutator is the quantum version of a structure we'll discover shortly: the Poisson bracket. The Hamiltonian formulation is the direct classical antecedent of quantum theory.

3. **The mathematics is more symmetric.** The Lagrangian treats $q$ and $\dot{q}$ asymmetrically (one is the derivative of the other). The Hamiltonian treats $q$ and $p$ on equal footing — they are independent variables in phase space. This symmetry has deep geometric meaning.

### §2.4.2 Canonical Momentum

Define the **canonical momentum** conjugate to $q^i$:

$$\boxed{p_i = \frac{\partial L}{\partial \dot{q}^i} \quad \text{(Eq. 3.2.20)}}$$

For a particle with $L = \frac{1}{2}M_{ij}\dot{q}^i\dot{q}^j - V(q)$ (Eq. 3.2.5), this gives:

$$p_i = M_{ij}(q)\dot{q}^j \tag{3.2.21}$$

In Cartesian coordinates, $p_i = m\dot{x}_i$ — the ordinary momentum. In polar coordinates, $p_\theta = mr^2\dot{\theta}$ — the angular momentum. The canonical momentum generalizes the concept of momentum to any coordinate system.

Notice the connection to Noether's theorem (Eq. 3.2.19): the conserved quantity associated with a coordinate translation $\delta q^i = 1$ is precisely the canonical momentum $p_i$. Momentum is the Noether charge of translational symmetry — at both the zone level (Vol 1, Ch 7) and the particle level.

For a charged particle in an electromagnetic field, the Lagrangian (Eq. 3.2.2) gives:

$$p_i = m\dot{x}_i + qA_i \tag{3.2.22}$$

The canonical momentum includes a contribution from the vector potential. This is not the "mechanical momentum" $m\dot{x}_i$; it is the *total* momentum including the field. This distinction, which often confuses students in standard courses, is natural in the zone framework: the canonical momentum is the derivative of the *total* action (particle plus field coupling) with respect to velocity. The field contributes.

### §2.4.3 The Legendre Transform

The **Legendre transform** replaces the velocity variables $\dot{q}^i$ with the momentum variables $p_i$. It is defined by:

$$\boxed{H(q, p, t) = \sum_i p_i \dot{q}^i - L(q, \dot{q}, t) \quad \text{(Eq. 3.2.23)}}$$

where, on the right-hand side, $\dot{q}^i$ is expressed as a function of $(q, p)$ by inverting the relation $p_i = \partial L/\partial\dot{q}^i$.

The function $H$ is the **Hamiltonian**.

**Geometric interpretation.** The Legendre transform maps from the tangent bundle $TQ$ (the space of positions and velocities) to the cotangent bundle $T^*Q$ (the space of positions and momenta). This is not just a change of variables — it is a change of *arena*. The tangent bundle is where Lagrangian mechanics lives. The cotangent bundle — **phase space** — is where Hamiltonian mechanics lives. Phase space has a natural geometric structure (the symplectic form) that the tangent bundle lacks. We'll meet it shortly.

[FIGURE: Fig 3.2.2 — Configuration Space vs. Phase Space. Left panel: configuration space with axes $(q, \dot{q})$. A trajectory traces a curve. Right panel: phase space with axes $(q, p)$. The SAME physical trajectory traces a different curve. The Legendre transform (arrow between panels) is the map. In the left panel, the trajectory is parameterized by velocity; in the right, by momentum. The curve shapes differ, but the physics is identical.]

**Invertibility.** The Legendre transform is invertible if and only if the mass matrix $M_{ij}$ (Eq. 3.2.4) is non-degenerate: $\det(M_{ij}) \neq 0$. This is guaranteed for all mechanical systems we consider: a degenerate mass matrix would mean that some velocity component doesn't contribute to kinetic energy, which would indicate a gauge degree of freedom (a subject for field theory, not particle mechanics).

### §2.4.4 When Does $H = E$?

A crucial question: **Is the Hamiltonian the same as the total energy?**

Not always. But under two conditions — both of which have zone-architectural origins — the answer is yes.

**Condition 1:** The Lagrangian has no explicit time dependence ($\partial L/\partial t = 0$).

**Condition 2:** The kinetic energy is a homogeneous quadratic function of velocities: $T = \frac{1}{2}M_{ij}(q)\dot{q}^i\dot{q}^j$.

When both hold, Euler's theorem on homogeneous functions gives:

$$\sum_i \dot{q}^i \frac{\partial T}{\partial \dot{q}^i} = 2T$$

Therefore:

$$H = \sum_i p_i\dot{q}^i - L = \sum_i \frac{\partial L}{\partial\dot{q}^i}\dot{q}^i - L = 2T - (T - V) = T + V = E \tag{3.2.24}$$

**The Hamiltonian equals the total energy.**

Why do these conditions hold? Condition 1 follows from the Symmetry Principle: when the laws of physics are time-independent (which they are in Phase 3, to the precision set by $\epsilon \lesssim 10^{-27}$), the Lagrangian has no explicit time dependence. Condition 2 follows from the metric structure of the zone manifold: the kinetic energy is the squared length of the velocity vector, which is necessarily quadratic in the velocity components.

When these conditions fail — for example, in a rotating reference frame, where the metric effectively acquires time-dependent cross terms — the Hamiltonian and energy differ. The rotating-frame Hamiltonian includes a centrifugal potential and Coriolis terms that make $H \neq T + V$. This is not a defect; it is the correct description of mechanics in a non-inertial frame.

### §2.4.5 Worked Example: Simple Harmonic Oscillator

The simple harmonic oscillator (SHO) is the simplest non-trivial system and the prototype for everything from molecular vibrations to quantum field theory. Let's work through it in both formalisms.

**Lagrangian:**

$$L = \frac{1}{2}m\dot{x}^2 - \frac{1}{2}kx^2 \tag{3.2.25}$$

Canonical momentum: $p = m\dot{x}$, so $\dot{x} = p/m$.

**Hamiltonian:**

$$H = p\dot{x} - L = p\frac{p}{m} - \left(\frac{1}{2}m\frac{p^2}{m^2} - \frac{1}{2}kx^2\right) = \frac{p^2}{2m} + \frac{1}{2}kx^2 \tag{3.2.26}$$

This equals $T + V$ — confirming Eq. (3.2.24) for this case.

---

## §2.5 Hamilton's Equations of Motion

### §2.5.1 Derivation from the Modified Hamilton's Principle

The Hamiltonian formulation has its own variational principle. Express the action in terms of $(q, p)$ rather than $(q, \dot{q})$:

$$S[q, p] = \int_{t_1}^{t_2} \left[\sum_i p_i\dot{q}^i - H(q, p, t)\right] dt \tag{3.2.27}$$

This is the **modified Hamilton's principle** (sometimes called the phase-space action). The integrand $p_i\dot{q}^i - H$ is called the **Poincaré-Cartan form**.

Requiring $\delta S = 0$ with respect to *independent* variations $\delta q^i$ and $\delta p_i$ (with $\delta q^i$ vanishing at the endpoints, but $\delta p_i$ unconstrained):

**Variation with respect to $q^i$:**

$$\delta_q S = \int_{t_1}^{t_2} \left[-\dot{p}_i - \frac{\partial H}{\partial q^i}\right] \delta q^i \, dt = 0$$

(after integrating $p_i\delta\dot{q}^i$ by parts, dropping the boundary term).

**Variation with respect to $p_i$:**

$$\delta_p S = \int_{t_1}^{t_2} \left[\dot{q}^i - \frac{\partial H}{\partial p_i}\right] \delta p_i \, dt = 0$$

Since $\delta q^i$ and $\delta p_i$ are arbitrary, both integrands must vanish:

$$\boxed{\dot{q}^i = \frac{\partial H}{\partial p_i}, \qquad \dot{p}_i = -\frac{\partial H}{\partial q^i} \quad \text{(Eq. 3.2.28)}}$$

These are **Hamilton's equations** — a system of $2n$ first-order ODEs, mathematically equivalent to the $n$ second-order Euler-Lagrange equations (3.2.12).

### §2.5.2 Verification: Equivalence with Euler-Lagrange

Let's verify that Hamilton's equations reproduce the Euler-Lagrange equations.

From $H = p_i\dot{q}^i - L$, compute:

$$\frac{\partial H}{\partial p_i} = \dot{q}^i + p_j\frac{\partial\dot{q}^j}{\partial p_i} - \frac{\partial L}{\partial\dot{q}^j}\frac{\partial\dot{q}^j}{\partial p_i}$$

But $p_j = \partial L/\partial\dot{q}^j$, so the last two terms cancel:

$$\frac{\partial H}{\partial p_i} = \dot{q}^i \quad \checkmark$$

Similarly:

$$\frac{\partial H}{\partial q^i} = p_j\frac{\partial\dot{q}^j}{\partial q^i} - \frac{\partial L}{\partial q^i} - \frac{\partial L}{\partial\dot{q}^j}\frac{\partial\dot{q}^j}{\partial q^i} = -\frac{\partial L}{\partial q^i}$$

Hamilton's second equation gives:

$$\dot{p}_i = -\frac{\partial H}{\partial q^i} = \frac{\partial L}{\partial q^i}$$

Combined with $p_i = \partial L/\partial\dot{q}^i$:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial\dot{q}^i}\right) = \frac{\partial L}{\partial q^i}$$

This is the Euler-Lagrange equation (3.2.12). The two formulations are fully equivalent. $\checkmark$

### §2.5.3 Worked Example: Simple Harmonic Oscillator in Hamilton's Equations

Using the Hamiltonian (Eq. 3.2.26):

$$\dot{x} = \frac{\partial H}{\partial p} = \frac{p}{m}$$

$$\dot{p} = -\frac{\partial H}{\partial x} = -kx$$

Combining: $m\ddot{x} = \dot{p} = -kx$, which gives $\ddot{x} + \omega^2 x = 0$ with $\omega = \sqrt{k/m}$.

The solution is:

$$x(t) = A\cos(\omega t + \phi), \qquad p(t) = -mA\omega\sin(\omega t + \phi) \tag{3.2.29}$$

[FIGURE: Fig 3.2.6 — Simple Harmonic Oscillator in Both Formalisms. Left panel: $x(t)$ vs. $t$ — the familiar sinusoidal oscillation. Middle panel: $(x, p)$ phase portrait — an ellipse. Right panel: energy contours in phase space — nested ellipses $H = \text{const}$. The trajectory sits on one contour. Caption: "The phase portrait reveals the SHO's complete dynamics at a glance. Every initial condition determines an ellipse. The Hamiltonian is constant on each ellipse — energy is conserved."]

The phase portrait — the trajectory in the $(x, p)$ plane — is an ellipse:

$$\frac{x^2}{2E/k} + \frac{p^2}{2mE} = 1$$

Every point on the ellipse has the same energy. The trajectory circulates clockwise (for our sign conventions). This is the Hamiltonian's natural language: not a function of time, but a flow in phase space.

### §2.5.4 Phase Space and Liouville's Theorem

The **phase space** of a system with $n$ degrees of freedom is the $2n$-dimensional space with coordinates $(q^1, \ldots, q^n, p_1, \ldots, p_n)$. Hamilton's equations define a **flow** on phase space: they tell you how the state $(q, p)$ evolves in time.

A fundamental property of Hamiltonian flow is **Liouville's theorem**: the phase-space volume is preserved.

**Theorem (Liouville).** The volume element $d^nq \, d^np$ is invariant under the time evolution generated by Hamilton's equations.

**Proof.** Consider a small volume element $\Delta\Gamma$ at time $t$. Under Hamilton's equations, each point in $\Delta\Gamma$ evolves to a new point at time $t + dt$. The Jacobian of the time-evolution map is:

$$\frac{\partial(\dot{q}^i, \dot{p}_i)}{\partial(q^j, p_j)} = \begin{pmatrix} \partial\dot{q}^i/\partial q^j & \partial\dot{q}^i/\partial p_j \\ \partial\dot{p}_i/\partial q^j & \partial\dot{p}_i/\partial p_j \end{pmatrix}$$

Using Hamilton's equations:

$$\frac{\partial\dot{q}^i}{\partial q^j} = \frac{\partial^2 H}{\partial q^j\partial p_i}, \qquad \frac{\partial\dot{p}_i}{\partial p_j} = -\frac{\partial^2 H}{\partial p_j\partial q^i}$$

The trace of the Jacobian (which determines the rate of volume change) is:

$$\sum_i \left(\frac{\partial\dot{q}^i}{\partial q^i} + \frac{\partial\dot{p}_i}{\partial p_i}\right) = \sum_i \left(\frac{\partial^2 H}{\partial q^i\partial p_i} - \frac{\partial^2 H}{\partial p_i\partial q^i}\right) = 0 \tag{3.2.30}$$

The trace vanishes by the symmetry of mixed partial derivatives. Therefore the Jacobian determinant equals 1 (to first order in $dt$), and the volume is preserved. $\square$

**Why does Liouville's theorem matter?** Because it is the classical foundation of statistical mechanics. When we treat $10^{23}$ particles as a statistical ensemble (Chapters 9–12), the distribution function $\rho(q, p, t)$ evolves on phase space. Liouville's theorem says the phase-space density is conserved along trajectories — the fundamental starting point for the Boltzmann equation and for equilibrium statistical mechanics.

[FIGURE: Fig 3.2.3 — Symplectic Structure of Phase Space. A blob of initial conditions in $(q, p)$ space evolves under Hamiltonian flow. At time $t_1$: a circle. At time $t_2$: a distorted shape (stretched and sheared). Key point: the AREA (in 2D) or VOLUME (in higher dimensions) is the same in both. Labels: "Volume preserved (Liouville)," "Shape changes, volume doesn't." The symplectic 2-form $\omega = dp \wedge dq$ measures the preserved area.]

### §2.5.5 Connection to the Degradation Principle

Volume 1, Chapter 8, §8.7.5 expressed the Degradation Principle in Hamiltonian language. The canonical momenta $\Pi_a = \partial\mathcal{L}/\partial\dot{\phi}^a$ and the Hamiltonian $\mathcal{H} = \Pi_a\dot{\phi}^a - \mathcal{L}$ define phase-space dynamics for the zone fields (Eqs. 1.8.27–1.8.28). The Degradation constraint requires:

$$\frac{\partial\mathscr{S}[\rho]}{\partial t} \geq 0 \quad \text{(Phase 3)} \tag{1.8.29}$$

Now we can unpack this. Liouville's theorem says the phase-space density $\rho$ is conserved along individual trajectories. But the *coarse-grained* entropy — the entropy computed from a smoothed version of $\rho$ — can increase, because fine-grained structure below the coarse-graining scale is lost. This is the mechanism of the Second Law: Hamiltonian dynamics preserves information perfectly at the fine-grained level, but the information becomes *inaccessible* at the macroscopic level.

The Degradation Principle (Phase 3) says this inaccessibility is a one-way process: coarse-grained entropy increases monotonically during the Fall phase. In the Edenic Phase (Phase 2), the sustaining field $\kappa_\text{full}$ was strong enough to maintain the coarse-grained structure — entropy production was zero. The weakening of $\kappa$ in Phase 3 allows the natural tendency of Hamiltonian dynamics (spreading in phase space, loss of macroscopic coherence) to proceed unchecked.

We will develop this connection fully in Chapters 9–12. For now, the key point is: **the Hamiltonian formulation is not just a mathematical convenience. It is the natural arena for the Degradation Principle and for thermodynamics.**

---

## §2.6 Poisson Brackets and the Algebra of Observables

### §2.6.1 Definition and Motivation

Hamilton's equations (3.2.28) describe how $q$ and $p$ evolve. But what about an *arbitrary* function $f(q, p, t)$ on phase space? How does it evolve?

$$\frac{df}{dt} = \sum_i \left(\frac{\partial f}{\partial q^i}\dot{q}^i + \frac{\partial f}{\partial p_i}\dot{p}_i\right) + \frac{\partial f}{\partial t}$$

Substituting Hamilton's equations:

$$\frac{df}{dt} = \sum_i \left(\frac{\partial f}{\partial q^i}\frac{\partial H}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial H}{\partial q^i}\right) + \frac{\partial f}{\partial t}$$

The sum defines a bilinear operation on phase-space functions:

$$\boxed{\{f, g\} = \sum_i \left(\frac{\partial f}{\partial q^i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q^i}\right) \quad \text{(Eq. 3.2.31)}}$$

This is the **Poisson bracket** of $f$ and $g$. The time evolution of any observable is:

$$\boxed{\frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t} \quad \text{(Eq. 3.2.32)}}$$

If $f$ has no explicit time dependence, then $f$ is conserved if and only if $\{f, H\} = 0$.

### §2.6.2 Fundamental Brackets

What happens when we compute the Poisson bracket of the canonical variables themselves — the building blocks of phase space? Since $q$ and $p$ are the independent coordinates and momenta from which all other observables are constructed, their mutual brackets must encode the fundamental structure of phase space. And indeed they do — the results follow directly from the definition (Eq. 3.2.31) by straightforward computation:

$$\{q^i, q^j\} = 0, \qquad \{p_i, p_j\} = 0, \qquad \{q^i, p_j\} = \delta^i_j \tag{3.2.33}$$

These are the **fundamental Poisson brackets**. They encode the canonical structure of phase space. Any two coordinates commute (positions don't "interfere" with each other). Any two momenta commute (momenta don't interfere with each other either). But a coordinate and its conjugate momentum have bracket equal to the Kronecker delta — they are maximally "entangled" in the Poisson-bracket sense. This asymmetry between same-type and conjugate-pair brackets is the algebraic fingerprint of the symplectic structure.

The student should note these carefully, because in Volume 4, the transition to quantum mechanics will be made by the replacement:

$$\{f, g\}_\text{classical} \to \frac{1}{i\hbar}[\hat{f}, \hat{g}]_\text{quantum}$$

The fundamental brackets (3.2.33) become the canonical commutation relations $[\hat{q}^i, \hat{p}_j] = i\hbar\delta^i_j$ — the foundation of quantum mechanics. The Poisson bracket is the classical shadow of the quantum commutator. We will not develop this further here (that is Vol 4's business), but the student should know that the algebraic structure being built in this section is not transient — it is the permanent mathematical language of physics.

### §2.6.3 Properties of Poisson Brackets

The Poisson bracket satisfies three algebraic properties:

1. **Antisymmetry:** $\{f, g\} = -\{g, f\}$

2. **Leibniz rule (derivation):** $\{fg, h\} = f\{g, h\} + g\{f, h\}$

3. **Jacobi identity:** $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$

These three properties define a **Lie algebra** structure on the space of phase-space functions. The fact that classical observables form a Lie algebra is not an accident — it reflects the symplectic geometry of phase space. The Poisson bracket is the Lie bracket induced by the symplectic form $\omega = \sum_i dp_i \wedge dq^i$.

The Jacobi identity deserves special attention. It ensures consistency of time evolution: the bracket $\{f, \{g, h\}\}$ can be computed in any order without contradiction. Physically, it means that the conservation laws themselves are consistent — if $A$ and $B$ are both conserved, then $\{A, B\}$ is also conserved (this is sometimes called the "Poisson theorem").

### §2.6.4 Conservation Laws via Poisson Brackets

A quantity $Q(q, p)$ is conserved if and only if:

$$\{Q, H\} = 0 \tag{3.2.34}$$

This provides a systematic test for conservation. Given any candidate conserved quantity, compute its bracket with the Hamiltonian. If it vanishes, $Q$ is conserved.

**Example: Angular Momentum.** For a particle in a central potential $V(r)$ in 2D polar coordinates, the Hamiltonian is:

$$H = \frac{p_r^2}{2m} + \frac{p_\theta^2}{2mr^2} + V(r) \tag{3.2.35}$$

Test whether $L_z = p_\theta$ is conserved:

$$\{p_\theta, H\} = -\frac{\partial H}{\partial\theta} = 0$$

since $H$ does not depend on $\theta$. Therefore $p_\theta = L_z$ is conserved. $\checkmark$

This connects directly to Noether's theorem: the coordinate $\theta$ is cyclic (absent from $H$), so its conjugate momentum is conserved. Noether via the Lagrangian and Poisson brackets via the Hamiltonian give the same result. The zone framework's symmetry structure (Vol 1, Ch 7) manifests identically in both formalisms.

### §2.6.5 The Angular Momentum Algebra

The components of angular momentum in 3D are:

$$L_x = yp_z - zp_y, \quad L_y = zp_x - xp_z, \quad L_z = xp_y - yp_x$$

Their Poisson brackets are:

$$\{L_x, L_y\} = L_z, \qquad \{L_y, L_z\} = L_x, \qquad \{L_z, L_x\} = L_y \tag{3.2.36}$$

This is the Lie algebra $\mathfrak{so}(3)$ — the algebra of rotations in 3D. The Poisson bracket reproduces the rotation group's algebraic structure. This is another instance of Noether's theorem at work: rotational symmetry (a continuous group) produces angular momentum (a set of conserved quantities), and the Poisson brackets of those quantities reproduce the symmetry group's algebra.

In Volume 4, this algebra becomes $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$, and the quantization of angular momentum — the fact that its measured values are discrete multiples of $\hbar$ — follows directly.

---

## §2.7 Canonical Transformations

### §2.7.1 Motivation: Phase-Space Coordinate Freedom

On the zone manifold, physics is independent of coordinates — this is diffeomorphism invariance (Vol 1, Ch 7). The equations of motion have the same form in any coordinate system because the action is a scalar.

Phase space has an analogous property. The Hamiltonian equations (3.2.28) have a specific form:

$$\dot{q}^i = \frac{\partial H}{\partial p_i}, \qquad \dot{p}_i = -\frac{\partial H}{\partial q^i}$$

A **canonical transformation** is a change of phase-space coordinates:

$$(q^i, p_i) \to (Q^i, P_i)$$

that preserves this form — Hamilton's equations in the new coordinates have the *same* structure, possibly with a different Hamiltonian $K(Q, P, t)$:

$$\dot{Q}^i = \frac{\partial K}{\partial P_i}, \qquad \dot{P}_i = -\frac{\partial K}{\partial Q^i} \tag{3.2.37}$$

Not every change of variables is canonical. Canonical transformations are the special ones that preserve the symplectic structure of phase space — the Poisson bracket relations.

[FIGURE: Fig 3.2.4 — Canonical Transformation as Phase-Space Coordinate Change. Two overlapping coordinate grids on a phase-space plane. Old coordinates $(q, p)$ with blue grid lines. New coordinates $(Q, P)$ with red grid lines. A single trajectory passes through both grids. In both coordinate systems, Hamilton's equations hold. Caption: "Canonical transformations change the description but not the physics — the phase-space analog of diffeomorphism invariance on the zone manifold."]

### §2.7.2 The Symplectic Condition

A transformation $(q, p) \to (Q, P)$ is canonical if and only if the fundamental Poisson brackets are preserved:

$$\{Q^i, Q^j\} = 0, \qquad \{P_i, P_j\} = 0, \qquad \{Q^i, P_j\} = \delta^i_j \tag{3.2.38}$$

where the brackets on the left are computed using the OLD variables $(q, p)$.

There is a compact way to state this condition using matrices. Think of it by analogy: a rotation in ordinary space preserves the length of vectors, which means it preserves the metric ($\mathbf{R}^T\mathbf{I}\mathbf{R} = \mathbf{I}$). A canonical transformation preserves not *lengths* but *oriented areas* in phase space — the symplectic form — so it satisfies an analogous matrix equation, but with the metric replaced by the symplectic matrix.

Defining the Jacobian matrix $\mathbf{M}$ of the transformation:

$$M_{ab} = \frac{\partial(Q^1, \ldots, Q^n, P_1, \ldots, P_n)_a}{\partial(q^1, \ldots, q^n, p_1, \ldots, p_n)_b}$$

the symplectic condition is:

$$\mathbf{M}^T \mathbf{J} \mathbf{M} = \mathbf{J} \tag{3.2.39}$$

where $\mathbf{J}$ is the standard symplectic matrix:

$$\mathbf{J} = \begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix} \tag{3.2.40}$$

A matrix satisfying Eq. (3.2.39) is called **symplectic**. Canonical transformations are symplectomorphisms — the symmetry group of the symplectic form $\omega = \sum_i dp_i \wedge dq^i$.

### §2.7.3 Generating Functions

Canonical transformations can be systematically constructed using **generating functions**. Why are there exactly four types? A canonical transformation maps old variables $(q, p)$ to new variables $(Q, P)$. To specify the transformation, you need a function that bridges old and new — but you have a choice: which pair of variables (one old, one new) do you use as the independent arguments? There are four possible pairings: $(q, Q)$, $(q, P)$, $(p, Q)$, and $(p, P)$. Each choice produces a different type of generating function. They are related to each other by Legendre transforms — the same operation that connects $L$ and $H$.

**Type 1: $F_1(q, Q, t)$**

$$p_i = \frac{\partial F_1}{\partial q^i}, \qquad P_i = -\frac{\partial F_1}{\partial Q^i}, \qquad K = H + \frac{\partial F_1}{\partial t} \tag{3.2.41}$$

**Type 2: $F_2(q, P, t)$**

$$p_i = \frac{\partial F_2}{\partial q^i}, \qquad Q^i = \frac{\partial F_2}{\partial P_i}, \qquad K = H + \frac{\partial F_2}{\partial t} \tag{3.2.42}$$

**Type 3: $F_3(p, Q, t)$**

$$q^i = -\frac{\partial F_3}{\partial p_i}, \qquad P_i = -\frac{\partial F_3}{\partial Q^i}, \qquad K = H + \frac{\partial F_3}{\partial t} \tag{3.2.43}$$

**Type 4: $F_4(p, P, t)$**

$$q^i = -\frac{\partial F_4}{\partial p_i}, \qquad Q^i = \frac{\partial F_4}{\partial P_i}, \qquad K = H + \frac{\partial F_4}{\partial t} \tag{3.2.44}$$

The different types are related by Legendre transforms (the same tool we used to go from $L$ to $H$). The student should master Type 2, which is the most commonly used.

**Example: The Identity Transformation.** The generating function $F_2 = q^i P_i$ gives $p_i = P_i$ and $Q^i = q^i$ — the identity. This verifies that the identity is canonical (as it should be).

**Example: The Exchange Transformation.** The generating function $F_1 = q^i Q_i$ gives $p_i = Q_i$ and $P_i = -q^i$. This swaps coordinates and momenta (with a sign). This transformation underscores the democratic treatment of $q$ and $p$ in Hamiltonian mechanics — they can be interchanged without affecting the form of the equations.

### §2.7.4 Worked Example: Simplifying the Harmonic Oscillator

To see canonical transformations earn their keep, let's apply one to the harmonic oscillator — a system we already solved (§2.5.3), but whose phase-space trajectory (an ellipse) suggests a natural simplification: transform to coordinates in which the trajectory is a circle traversed at constant speed.

The Hamiltonian is $H = p^2/(2m) + \frac{1}{2}m\omega^2 x^2$ (Eq. 3.2.26). We seek new variables $(Q, P)$ in which $H$ depends only on $P$ (so that $Q$ evolves linearly in time). This is exactly the action-angle transformation previewed in §2.8.6.

Use a Type-2 generating function of the form:

$$F_2(x, P) = \frac{m\omega x^2}{2}\cot Q$$

Wait — this mixes old and new variables in a way that requires care. Instead, work from the known action-angle result. Define:

$$x = \sqrt{\frac{2P}{m\omega}}\sin Q, \qquad p = \sqrt{2m\omega P}\cos Q$$

**Step 1: Verify this is canonical.** Compute the Poisson bracket:

$$\{Q, P\}_{x,p} = \frac{\partial Q}{\partial x}\frac{\partial P}{\partial p} - \frac{\partial Q}{\partial p}\frac{\partial P}{\partial x}$$

From the transformation: $x^2 = (2P/m\omega)\sin^2 Q$ and $p^2 = 2m\omega P\cos^2 Q$, so $H = P\omega(\sin^2 Q + \cos^2 Q) = \omega P$.

One can verify (by computing the partial derivatives explicitly) that $\{Q, P\}_{x,p} = 1$. $\checkmark$

**Step 2: The new Hamiltonian.** In the new variables:

$$K(Q, P) = \omega P$$

This depends only on $P$ — the problem is solved.

**Step 3: Hamilton's equations in the new variables.**

$$\dot{Q} = \frac{\partial K}{\partial P} = \omega, \qquad \dot{P} = -\frac{\partial K}{\partial Q} = 0$$

So $P = \text{const}$ (the action variable — proportional to the energy) and $Q = \omega t + Q_0$ (the angle variable — increases uniformly). The elliptical phase-space trajectory in $(x, p)$ has become uniform circular motion in $(Q, P)$.

This is the payoff of canonical transformations: a problem with non-trivial dynamics becomes trivial in the right coordinates. The physics hasn't changed — the oscillator still oscillates — but the mathematical description has been reduced to its simplest possible form. For the harmonic oscillator this is merely elegant; for more complex systems (the Kepler problem in Chapter 3, or multi-body dynamics), canonical transformations can be the difference between solvable and intractable.

### §2.7.5 Infinitesimal Canonical Transformations

Why study infinitesimal transformations when we already have the full generating-function machinery? Because every continuous symmetry is built from infinitesimal ones — a finite rotation is a sequence of tiny rotations, a finite time step is a sequence of tiny time steps. The infinitesimal version reveals *which phase-space function generates which transformation*, connecting symmetries, conservation laws, and dynamics in a single unified picture.

For an infinitesimal transformation $(q, p) \to (q + \delta q, p + \delta p)$ generated by a function $G(q, p)$:

$$\delta q^i = \epsilon\{q^i, G\} = \epsilon\frac{\partial G}{\partial p_i}, \qquad \delta p_i = \epsilon\{p_i, G\} = -\epsilon\frac{\partial G}{\partial q^i} \tag{3.2.45}$$

where $\epsilon$ is an infinitesimal parameter.

This is profound: **every phase-space function $G$ generates a canonical transformation, and every canonical transformation is generated by a phase-space function.** The Poisson bracket is the infinitesimal generator.

Special cases:

- $G = H$ generates time evolution (Hamilton's equations).
- $G = p_i$ generates translations in $q^i$.
- $G = L_z$ generates rotations about the $z$-axis.

Symmetries, conservation laws, and canonical transformations are three faces of the same coin. This is Noether's theorem, viewed from the Hamiltonian side.

---

## §2.8 The Hamilton-Jacobi Equation and the Classical-Quantum Bridge

### §2.8.1 The Idea

Is there a canonical transformation that makes the problem *trivial*? That is, a transformation to new variables $(Q, P)$ in which the new Hamiltonian $K = 0$, so that $\dot{Q}^i = \dot{P}_i = 0$ — all the new coordinates and momenta are constants of the motion?

If such a transformation exists, then finding it is equivalent to solving the problem completely. The answer to "is there such a transformation?" is yes — always. Finding it requires solving a partial differential equation called the **Hamilton-Jacobi equation**.

### §2.8.2 Derivation

We seek a Type-2 generating function $S(q, P, t)$ such that the new Hamiltonian vanishes:

$$K = H + \frac{\partial S}{\partial t} = 0$$

From the Type-2 relations (Eq. 3.2.42):

$$p_i = \frac{\partial S}{\partial q^i}$$

Substituting into $K = 0$:

$$\boxed{H\left(q^i, \frac{\partial S}{\partial q^i}, t\right) + \frac{\partial S}{\partial t} = 0 \quad \text{(Eq. 3.2.46)}}$$

This is the **Hamilton-Jacobi (H-J) equation** — a first-order partial differential equation for the function $S(q, P, t)$, called **Hamilton's principal function**.

For a system with $n$ degrees of freedom, the H-J equation is one PDE in $n + 1$ variables $(q^1, \ldots, q^n, t)$. A complete solution contains $n$ constants of integration $\alpha_1, \ldots, \alpha_n$ (which become the new momenta $P_i = \alpha_i$). The new coordinates are:

$$Q^i = \frac{\partial S}{\partial\alpha_i} = \beta_i = \text{const} \tag{3.2.47}$$

Together, the $2n$ constants $(\alpha_i, \beta_i)$ determine the trajectory completely.

### §2.8.3 Connection to the Action

Hamilton's principal function $S$ has a physical interpretation: it is the *action* evaluated along the classical trajectory:

$$S(q, \alpha, t) = \int_{t_0}^{t} L \, dt' \bigg|_\text{classical} \tag{3.2.48}$$

where the integral is taken along the path that satisfies the Euler-Lagrange equations with the given boundary conditions. This closes the circle: the action, which was our starting point (the zone action, the variational principle), turns out to be the generating function that solves the equations of motion.

### §2.8.4 Separation of Variables and Conservation Laws

When the Hamiltonian has a separable structure — typically because of symmetries — the H-J equation admits a separated solution:

$$S(q^1, \ldots, q^n, t) = W_1(q^1) + W_2(q^2) + \cdots + W_n(q^n) - Et \tag{3.2.49}$$

Each function $W_i(q^i)$ satisfies an ODE. The separation constants are the conserved quantities (energy, angular momentum, etc.).

**Example: Central Force Problem (Preview of Chapter 3).**

For a particle in a central potential $V(r)$, in spherical coordinates $(r, \theta, \phi)$:

$$H = \frac{p_r^2}{2m} + \frac{p_\theta^2}{2mr^2} + \frac{p_\phi^2}{2mr^2\sin^2\theta} + V(r) \tag{3.2.50}$$

The H-J equation separates: $S = W_r(r) + W_\theta(\theta) + L_z\phi - Et$, where $L_z = p_\phi$ is the $z$-component of angular momentum (a constant because $\phi$ is cyclic). The $\theta$-equation yields the total angular momentum $L$ as a separation constant. The $r$-equation yields the orbit equation. Chapter 3 will develop this in full.

### §2.8.5 The Eikonal Limit and the Bridge to Quantum Mechanics

The Hamilton-Jacobi equation contains within it the seeds of quantum mechanics. To see this, consider a free particle with Hamiltonian $H = p^2/2m$. The H-J equation is:

$$\frac{1}{2m}\left(\frac{\partial S}{\partial x}\right)^2 + \frac{\partial S}{\partial t} = 0 \tag{3.2.51}$$

Now consider the substitution $S = -i\hbar\ln\psi$, where $\psi$ is some complex function. Then $\partial S/\partial x = -i\hbar(\partial\psi/\partial x)/\psi$, and the H-J equation becomes:

$$-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} + \frac{\hbar^2}{2m}\frac{(\partial\psi/\partial x)^2}{\psi^2}\frac{1}{\psi}\frac{\partial\psi}{\partial x} + i\hbar\frac{\partial\psi}{\partial t} = 0$$

In the limit $\hbar \to 0$, the second term dominates, and we recover the classical H-J equation. But if we *keep* $\hbar$ finite and add the second-derivative term, we get something very close to the **Schrödinger equation**:

$$i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}$$

This is not a derivation of quantum mechanics — that must wait for Volume 4, where the zone architecture's boundary conditions (Vol 1, Ch 10) provide the physical reason for quantization. But it shows that the Hamilton-Jacobi equation is the *classical limit* of the Schrödinger equation. Lagrangian/Hamiltonian mechanics is not replaced by quantum mechanics; it is contained within it as the $\hbar \to 0$ limit.

The hierarchy is:

$$\text{Zone Action (Vols 1–2)} \to \text{Lagrangian (§2.2–2.3)} \to \text{Hamiltonian (§2.4–2.5)} \to \text{Hamilton-Jacobi (§2.8)} \xrightarrow{\hbar \neq 0} \text{Quantum Mechanics (Vol 4)}$$

[FIGURE: Fig 3.2.5 — The Hierarchy: Zone Action → Lagrangian → Hamiltonian → Quantum. Vertical hierarchy with four levels. Top: Zone Action $S_\text{total}$ (Vol 1–2), complete 6D description. Second: Lagrangian mechanics $L(q, \dot{q}, t)$ (this chapter), particle-level, $n$ second-order equations. Third: Hamiltonian mechanics $H(q, p, t)$ (this chapter), phase-space formulation, $2n$ first-order equations. Bottom: Quantum mechanics $\hat{H}\psi = i\hbar\partial\psi/\partial t$ (Vol 4), operator formulation, wave equation. Arrow from H-J equation bridges third and fourth levels. Caption: "Each level inherits from the one above. The zone action is the root; quantum mechanics is the most refined branch."]

### §2.8.6 Action-Angle Variables

For periodic systems (like the harmonic oscillator or planetary orbits), there exists a particularly useful canonical transformation to **action-angle variables** $(w, J)$.

The **action variable** is:

$$J = \oint p \, dq \tag{3.2.52}$$

where the integral is over one complete period of the motion. The **angle variable** $w$ increases uniformly in time:

$$w = \nu t + w_0, \qquad \nu = \frac{\partial H}{\partial J} \tag{3.2.53}$$

where $\nu$ is the frequency of the motion.

In action-angle variables, the Hamiltonian depends only on $J$: $H = H(J)$. The equations of motion are:

$$\dot{w} = \nu(J) = \text{const}, \qquad \dot{J} = 0 \tag{3.2.54}$$

The motion is uniform on a torus in phase space. This is the simplest possible form of Hamiltonian dynamics.

**Connection to quantization (preview).** In the old quantum theory (Bohr-Sommerfeld), the quantization condition was $J = n\hbar$ — the action variable takes integer multiples of Planck's constant. Volume 4 will derive this from the zone architecture's boundary conditions (Vol 1, Ch 10), but the fact that it's the *action variable* that gets quantized is no coincidence. The action variable is the invariant of the classical orbit — the quantity that survives the transition to quantum mechanics.

---

## §2.9 What Is Derived, What Is Formalism, and What Comes Next

### What We DERIVED in This Chapter (From Zone Principles)

1. **The particle Lagrangian $L = T - V$** (Eq. 3.2.3): Derived as the non-relativistic limit of the test particle action on the zone manifold (Eq. 3.1.7), which itself is extracted from the zone Lagrangian (Eq. 2.5.20) via KK reduction and the test particle limit.

2. **The Euler-Lagrange equations** (Eq. 3.2.12): Derived from the variational principle $\delta S = 0$ (the same principle that governs the zone action, Vol 2 Ch 5 Eq. 2.5.21). Verified to reproduce F=ma (Eq. 3.1.10).

3. **Noether's theorem for particles** (Eq. 3.2.19): The particle-level version of the zone-level Noether theorem (Vol 1, Ch 7). Symmetries produce conservation laws at every scale.

4. **The Hamiltonian $H$ and Hamilton's equations** (Eqs. 3.2.23, 3.2.28): Derived from the Lagrangian via the Legendre transform. The Hamiltonian equals the total energy under conditions that trace to the Symmetry Principle and the metric structure of the zone manifold.

5. **Liouville's theorem** (Eq. 3.2.30): A consequence of the Hamiltonian structure. Phase-space volume is conserved — the classical foundation for the Degradation Principle and statistical mechanics.

6. **The connection between Hamiltonian flow and the Degradation Principle** (§2.5.5): The zone framework's entropy constraint (Vol 1, Ch 8 §8.7.5) is naturally expressed in the Hamiltonian language developed here.

### What Is Mathematical Formalism (Not Physical Claims)

1. **The Legendre transform** is a mathematical operation, not a physical derivation. It reorganizes the same information into a different form.

2. **Poisson brackets** are a mathematical structure on phase space. They encode Hamiltonian mechanics algebraically but add no new physical content beyond Hamilton's equations.

3. **Canonical transformations and generating functions** are coordinate-change machinery. They simplify problems but do not change the physics.

4. **The Hamilton-Jacobi equation** is a reformulation of Hamilton's equations as a PDE. It is mathematically equivalent to the Euler-Lagrange equations.

### Comparison with Standard Textbooks

In standard classical mechanics (Goldstein, Landau & Lifshitz, Taylor), the Lagrangian $L = T - V$ is typically *postulated* as a starting point. The student is told "define the Lagrangian as kinetic minus potential energy" and then derives the Euler-Lagrange equations from the action principle.

This is pedagogically efficient but conceptually backwards. It treats the action principle as a mathematical trick rather than a fundamental statement about the structure of reality. The zone framework inverts this: the action principle is the foundation (Vol 1, Ch 8), the zone Lagrangian is constructed from axioms (Vol 2, Ch 5), and the particle Lagrangian is extracted from it. The student who follows this path understands *why* $L = T - V$ — not just *that* it works.

### What Comes Next

This chapter built the formal machinery. The next three chapters apply it:

- **Chapter 3 (Central Force Problems):** The Lagrangian and Hamiltonian methods, applied to the gravitational and Coulomb potentials. Kepler's problem solved via Hamilton-Jacobi separation. Orbital mechanics derived from zone gravity (Vol 2, Ch 2).

- **Chapter 4 (Rigid Body Dynamics):** The Lagrangian approach to rotating systems. Euler angles, Euler's equations, the spinning top — all derived from the zone conservation laws (Vol 1, Ch 7).

- **Chapter 5 (Continuum Mechanics and Fluid Dynamics):** The Lagrangian and Hamiltonian formulations extended from particles to continuous media. Connection back to the Waters field equations (Vol 1, Ch 6).

Beyond Part I, the Hamiltonian formulation will be essential for:

- **Part III (Chapters 9–12):** Thermodynamics and statistical mechanics. Phase space, Liouville's theorem, and the Boltzmann distribution are all Hamiltonian constructs.

- **Volume 4 (Quantum Mechanics):** The canonical commutation relations, the Schrödinger equation, and the path integral all emerge from the Hamiltonian/Lagrangian structure built here.

The student now holds the complete toolkit of classical mechanics. Every tool traces back to the zone action.

---

## Problem Sets

### Set 1: Computational Problems

**Problem 2.1: The Pendulum via Lagrangian Mechanics**

A simple pendulum of mass $m$ and length $\ell$ swings in a vertical plane.

(a) Write the Lagrangian using $\theta$ as the generalized coordinate.
(b) Derive the equation of motion using the Euler-Lagrange equations.
(c) Find the period of small oscillations.
(d) Compute the canonical momentum $p_\theta$ and the Hamiltonian $H(\theta, p_\theta)$.
(e) Verify that Hamilton's equations reproduce the same equation of motion.

**Solution:**

(a) $L = \frac{1}{2}m\ell^2\dot{\theta}^2 + mg\ell\cos\theta$ (Eq. 3.2.13).

(b) Euler-Lagrange: $m\ell^2\ddot{\theta} + mg\ell\sin\theta = 0$, i.e., $\ddot{\theta} + (g/\ell)\sin\theta = 0$ (Eq. 3.2.14).

(c) For small $\theta$: $\ddot{\theta} + (g/\ell)\theta = 0$. Period: $T = 2\pi\sqrt{\ell/g}$.

(d) $p_\theta = \partial L/\partial\dot{\theta} = m\ell^2\dot{\theta}$, so $\dot{\theta} = p_\theta/(m\ell^2)$.

$H = p_\theta\dot{\theta} - L = \frac{p_\theta^2}{m\ell^2} - \frac{p_\theta^2}{2m\ell^2} - mg\ell\cos\theta = \frac{p_\theta^2}{2m\ell^2} - mg\ell\cos\theta$

(e) $\dot{\theta} = \partial H/\partial p_\theta = p_\theta/(m\ell^2)$ ✓
$\dot{p}_\theta = -\partial H/\partial\theta = -mg\ell\sin\theta$
Combined: $m\ell^2\ddot{\theta} = -mg\ell\sin\theta$ ✓

---

**Problem 2.2: Bead on a Rotating Hoop**

A bead of mass $m$ slides without friction on a circular hoop of radius $R$ that rotates about a vertical diameter with angular velocity $\omega$.

(a) Using the angle $\theta$ from the bottom of the hoop as the generalized coordinate, show that the Lagrangian is:
$$L = \frac{1}{2}mR^2\dot{\theta}^2 + \frac{1}{2}mR^2\omega^2\sin^2\theta - mgR(1-\cos\theta)$$

(b) Find the equilibrium positions (where $\ddot{\theta} = 0$ and $\dot{\theta} = 0$).
(c) Show that for $\omega^2 > g/R$, a new stable equilibrium appears at $\cos\theta_0 = g/(R\omega^2)$.

**Solution:**

(a) The bead's position in the lab frame: $x = R\sin\theta\cos\omega t$, $y = R\sin\theta\sin\omega t$, $z = R(1-\cos\theta)$. Computing $v^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2$:

$v^2 = R^2\dot{\theta}^2 + R^2\omega^2\sin^2\theta$

So $T = \frac{1}{2}m(R^2\dot{\theta}^2 + R^2\omega^2\sin^2\theta)$ and $V = mgR(1-\cos\theta)$.

$L = T - V = \frac{1}{2}mR^2\dot{\theta}^2 + \frac{1}{2}mR^2\omega^2\sin^2\theta - mgR(1-\cos\theta)$ ✓

(b) Euler-Lagrange: $mR^2\ddot{\theta} = mR^2\omega^2\sin\theta\cos\theta - mgR\sin\theta$

At equilibrium: $\sin\theta(\omega^2 R\cos\theta - g) = 0$

Solutions: $\theta = 0$ (bottom), $\theta = \pi$ (top), and $\cos\theta_0 = g/(R\omega^2)$ (if $\omega^2 > g/R$).

(c) When $\omega^2 > g/R$, the ratio $g/(R\omega^2) < 1$, so $\cos\theta_0 = g/(R\omega^2)$ has a solution with $0 < \theta_0 < \pi/2$. Stability analysis (computing $\partial^2V_\text{eff}/\partial\theta^2$) shows this is stable while $\theta = 0$ becomes unstable — a pitchfork bifurcation.

---

**Problem 2.3: Two-Body Gravitational Problem**

Two masses $m_1$ and $m_2$ interact gravitationally with no external forces.

(a) Write the Lagrangian in center-of-mass and relative coordinates.
(b) Show that the center-of-mass moves uniformly and the relative coordinate satisfies a one-body problem with reduced mass $\mu = m_1 m_2/(m_1 + m_2)$.
(c) Compute the Hamiltonian and verify that $H = E$ (total energy).

**Solution:**

(a) Let $\mathbf{R} = (m_1\mathbf{r}_1 + m_2\mathbf{r}_2)/(m_1 + m_2)$ and $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$.

$L = \frac{1}{2}(m_1 + m_2)\dot{\mathbf{R}}^2 + \frac{1}{2}\mu\dot{\mathbf{r}}^2 + \frac{G_4 m_1 m_2}{|\mathbf{r}|}$

(b) The CM Euler-Lagrange equation: $(m_1+m_2)\ddot{\mathbf{R}} = 0$ → uniform motion. The relative coordinate equation: $\mu\ddot{\mathbf{r}} = -G_4 m_1 m_2 \hat{\mathbf{r}}/r^2$.

(c) $p_R = (m_1+m_2)\dot{\mathbf{R}}$, $p_r = \mu\dot{\mathbf{r}}$.

$H = \frac{p_R^2}{2(m_1+m_2)} + \frac{p_r^2}{2\mu} - \frac{G_4 m_1 m_2}{r} = T + V = E$ ✓

---

**Problem 2.4: Hamilton's Equations for a Central Force**

For a particle of mass $m$ in a central potential $V(r)$ in 2D polar coordinates:

(a) Write the Lagrangian $L(r, \theta, \dot{r}, \dot{\theta})$.
(b) Find the canonical momenta $p_r$ and $p_\theta$.
(c) Construct the Hamiltonian $H(r, \theta, p_r, p_\theta)$.
(d) Write Hamilton's equations. Show that $p_\theta$ (angular momentum) is conserved.
(e) Reduce to a one-dimensional problem in $r$ using the conservation of $p_\theta$.

**Solution:**

(a) $L = \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2) - V(r)$

(b) $p_r = m\dot{r}$, $p_\theta = mr^2\dot{\theta}$

(c) $H = \frac{p_r^2}{2m} + \frac{p_\theta^2}{2mr^2} + V(r)$ (Eq. 3.2.35)

(d) $\dot{r} = p_r/m$, $\dot{\theta} = p_\theta/(mr^2)$, $\dot{p}_r = p_\theta^2/(mr^3) - V'(r)$, $\dot{p}_\theta = -\partial H/\partial\theta = 0$ → $p_\theta$ is conserved.

(e) With $p_\theta = L$ (constant): $H = \frac{p_r^2}{2m} + V_\text{eff}(r)$ where $V_\text{eff}(r) = V(r) + L^2/(2mr^2)$.

---

**Problem 2.5: Generating Function for the Oscillator**

For the simple harmonic oscillator with $H = p^2/(2m) + \frac{1}{2}kx^2$:

(a) Find the Type-2 generating function $F_2(x, P)$ that transforms to action-angle variables $(w, J)$.
(b) Express $H$ in terms of $J$ alone.
(c) Verify that $w$ increases linearly in time with frequency $\nu = \omega/(2\pi)$.

**Solution:**

(a) The H-J equation: $\frac{1}{2m}\left(\frac{\partial S}{\partial x}\right)^2 + \frac{1}{2}kx^2 = E$

$\frac{\partial S}{\partial x} = \sqrt{2m(E - \frac{1}{2}kx^2)}$

$S = \int \sqrt{2m(E - \frac{1}{2}kx^2)} \, dx$

The action variable: $J = \oint p\,dx = \oint \sqrt{2m(E - \frac{1}{2}kx^2)} \, dx = \frac{2\pi E}{\omega}$ where $\omega = \sqrt{k/m}$.

Therefore $E = J\omega/(2\pi) = J\nu$ and the generating function is $F_2 = S(x, J)$ with $E = E(J)$.

(b) $H = J\omega/(2\pi)$ — linear in $J$.

(c) $\dot{w} = \partial H/\partial J = \omega/(2\pi) = \nu$ → $w = \nu t + w_0$. ✓

---

### Set 2: Conceptual Problems

**Problem 2.6: Why Least Action, Not Least Energy?**

A ball rolling down a hill minimizes potential energy at the bottom. Why isn't the fundamental principle "least energy" instead of "least action"?

**Solution:**

"Least energy" describes *equilibrium* — a static state. "Least action" (more precisely, stationary action) describes *motion* — a trajectory through time. The action integrates $L = T - V$ over the entire path, balancing kinetic and potential energy. A ball rolling down a hill *increases* kinetic energy while decreasing potential; neither is minimized along the trajectory. What is stationary is the *action* — the time integral of their difference.

The zone framework explains why: the Five Principles constrain the *action* (Vol 1, Ch 8), not the energy. Energy conservation is a *consequence* of the action's time-translation symmetry (Noether's theorem), but the action is more fundamental.

---

**Problem 2.7: When Is $H \neq E$?**

Give a physical example where the Hamiltonian is NOT equal to the total energy, and explain why.

**Solution:**

Consider a bead on a rotating hoop (Problem 2.2). In the rotating frame, the effective Lagrangian includes a $\frac{1}{2}mR^2\omega^2\sin^2\theta$ term that looks like negative potential energy. The Hamiltonian (computed from this Lagrangian) is:

$H = \frac{p_\theta^2}{2mR^2} - \frac{1}{2}mR^2\omega^2\sin^2\theta + mgR(1-\cos\theta)$

This differs from the total kinetic-plus-potential energy because the constraint (forced rotation at $\omega$) does work on the bead. Condition 2 of §2.4.4 fails: the kinetic energy in the lab frame includes cross terms between $\dot{\theta}$ and $\omega$ that make $T$ not purely quadratic in $\dot{\theta}$.

The Hamiltonian is the conserved quantity associated with time-translation symmetry in the rotating frame — which is not the total energy in the lab frame.

---

**Problem 2.8: What Do Poisson Brackets Mean Physically?**

Explain the physical meaning of $\{L_x, L_y\} = L_z$ (Eq. 3.2.36) without using any formulas.

**Solution:**

$\{L_x, L_y\} = L_z$ says: if you perform an infinitesimal rotation about the $x$-axis (generated by $L_x$) followed by an infinitesimal rotation about the $y$-axis (generated by $L_y$), and then undo both in reverse order, the net effect is an infinitesimal rotation about the $z$-axis. The Poisson bracket measures the "failure to commute" of two transformations — and for rotations, rotating about $x$ then $y$ is not the same as rotating about $y$ then $x$. The difference is a rotation about $z$.

---

**Problem 2.9: Why Do Canonical Transformations Preserve Physics?**

Explain, in terms of the zone framework, why canonical transformations preserve the form of Hamilton's equations.

**Solution:**

Hamilton's equations arise from the variational principle $\delta S = 0$ applied to the phase-space action (Eq. 3.2.27). Canonical transformations preserve the symplectic form $\omega = dp \wedge dq$, which is the geometric structure that makes the variational principle well-defined in phase space.

This is the phase-space analog of diffeomorphism invariance on the zone manifold (Vol 1, Ch 7): just as the zone action is a scalar under coordinate transformations on $\mathcal{M}_Z$, the phase-space action is invariant (up to boundary terms) under canonical transformations. Physics doesn't depend on how you label the states.

---

**Problem 2.10: From Zone Action to Poisson Brackets**

Trace the logical chain from the zone action (Vol 2, Ch 5) to the fundamental Poisson bracket $\{q, p\} = 1$. List each step and the equation where it occurs.

**Solution:**

1. Zone action $S_\text{total}$ constructed from axioms (Vol 2, Ch 5, Eq. 2.5.1)
2. Variational principle $\delta S_\text{total} = 0$ gives field equations (Vol 2, Ch 5, Eq. 2.5.21)
3. Test particle action extracted via KK reduction (Vol 3, Ch 1, Eq. 3.1.7)
4. Non-relativistic limit gives particle Lagrangian $L = T - V$ (Vol 3, Ch 2, Eq. 3.2.3)
5. Variational principle gives Euler-Lagrange equations (Eq. 3.2.12)
6. Legendre transform gives Hamiltonian (Eq. 3.2.23)
7. Modified Hamilton's principle gives Hamilton's equations (Eq. 3.2.28)
8. Hamilton's equations imply $\{q, p\} = 1$ (Eq. 3.2.33)

Every step traces back to the zone action. The fundamental Poisson bracket is not a postulate — it is a consequence of the zone framework's variational structure.

---

### Set 3: Challenge Problems

**Problem 2.11: Lagrangian for a Charged Particle from Zone Gauge Coupling**

Starting from the zone gauge sector (Vol 2, Ch 5, Eq. 2.5.10) and the matter-gauge coupling in the zone Lagrangian, derive the Lagrangian for a classical charged particle in an electromagnetic field:

$$L = \frac{1}{2}m\dot{\mathbf{x}}^2 - q\phi + q\mathbf{A}\cdot\dot{\mathbf{x}}$$

Show that the Euler-Lagrange equations give the Lorentz force law.

**Solution Sketch:**

Start from the matter sector (Eq. 2.5.13) with the covariant derivative $D_\mu = \partial_\mu + iqA_\mu$ for U(1). In the test-particle limit, the gauge coupling adds $q\int A_\mu dx^\mu$ to the worldline action. In the non-relativistic limit:

$\int A_\mu dx^\mu = \int (-\phi + \mathbf{A}\cdot\mathbf{v})dt$

Adding to the free-particle Lagrangian: $L = \frac{1}{2}mv^2 - q\phi + q\mathbf{A}\cdot\dot{\mathbf{x}}$

Canonical momentum: $\mathbf{p} = m\dot{\mathbf{x}} + q\mathbf{A}$ (Eq. 3.2.22).

Euler-Lagrange for $x_i$:

$\frac{d}{dt}(m\dot{x}_i + qA_i) = -q\frac{\partial\phi}{\partial x_i} + q\frac{\partial A_j}{\partial x_i}\dot{x}_j$

Expanding the time derivative of $A_i$ using the chain rule:

$m\ddot{x}_i = -q\frac{\partial\phi}{\partial x_i} - q\frac{\partial A_i}{\partial t} + q\dot{x}_j\left(\frac{\partial A_j}{\partial x_i} - \frac{\partial A_i}{\partial x_j}\right)$

Identifying $E_i = -\partial\phi/\partial x_i - \partial A_i/\partial t$ and $(\mathbf{v}\times\mathbf{B})_i = \dot{x}_j(\partial A_j/\partial x_i - \partial A_i/\partial x_j)$:

$m\ddot{\mathbf{x}} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$

This is the Lorentz force law — derived from the zone gauge sector.

---

**Problem 2.12: Liouville's Theorem from Hamilton's Equations**

Prove Liouville's theorem directly: show that the divergence of the Hamiltonian vector field in phase space vanishes.

**Solution:**

The Hamiltonian vector field is $\mathbf{X}_H = (\dot{q}^1, \ldots, \dot{q}^n, \dot{p}_1, \ldots, \dot{p}_n) = (\partial H/\partial p_1, \ldots, -\partial H/\partial q^1, \ldots)$.

The divergence is:

$\nabla\cdot\mathbf{X}_H = \sum_i\left(\frac{\partial\dot{q}^i}{\partial q^i} + \frac{\partial\dot{p}_i}{\partial p_i}\right) = \sum_i\left(\frac{\partial^2 H}{\partial q^i\partial p_i} - \frac{\partial^2 H}{\partial p_i\partial q^i}\right) = 0$

by the equality of mixed partials (assuming $H$ is $C^2$).

Since the divergence vanishes, the flow is incompressible, and by the divergence theorem, the volume of any region of phase space is preserved under time evolution. $\square$

---

**Problem 2.13: Hamilton-Jacobi and the Eikonal Equation**

Show that the Hamilton-Jacobi equation for a free particle in 3D:

$$\frac{1}{2m}|\nabla S|^2 + \frac{\partial S}{\partial t} = 0$$

is equivalent to the eikonal equation of geometric optics:

$$|\nabla\phi|^2 = n^2/c^2$$

when $S = S_0(\mathbf{x}) - Et$ and the appropriate identifications are made. Explain why this means light rays are "particle trajectories" and vice versa.

**Solution:**

For $S = S_0(\mathbf{x}) - Et$: $|\nabla S_0|^2 = 2mE = p^2$, i.e., $|\nabla S_0| = p$. The gradient $\nabla S_0$ points along the momentum — along the trajectory.

For the eikonal equation: consider a monochromatic wave $\psi = A\,e^{ik_0\phi(\mathbf{x})}$ in a medium with index $n(\mathbf{x})$. The eikonal approximation (short wavelength limit) gives $|\nabla\phi|^2 = n^2$. The gradient $\nabla\phi$ points along the ray direction.

Identifying $S_0/\hbar \leftrightarrow k_0\phi$ and $p/\hbar \leftrightarrow k_0 n$, the equations are identical. Light rays and particle trajectories are both described by Hamilton-Jacobi theory — the ray is the classical limit of the wave, and the particle trajectory is the classical limit of the quantum wavefunction.

This is the deep reason why optics and mechanics share the same mathematical structure: both are limits of wave theories (electromagnetic theory and quantum mechanics, respectively), and both are governed by variational principles (Fermat's principle for optics, Hamilton's principle for mechanics).

---

**Problem 2.14: Noether's Theorem for Time-Dependent Symmetries**

Generalize Noether's theorem to the case where the Lagrangian is invariant under a transformation that also shifts time: $t \to t + \epsilon\tau(q)$, $q^i \to q^i + \epsilon\xi^i(q)$.

Show that the conserved quantity is:

$$Q = \frac{\partial L}{\partial\dot{q}^i}\xi^i - (p_i\dot{q}^i - L)\tau = \frac{\partial L}{\partial\dot{q}^i}\xi^i - H\tau$$

and verify that for $\tau = 1, \xi = 0$ (time translation), $Q = -H$ (energy conservation).

**Solution:**

Under the transformation $t \to t + \epsilon\tau$, $q^i \to q^i + \epsilon\xi^i$, the Lagrangian transforms as:

$\delta L = \frac{\partial L}{\partial q^i}\xi^i\epsilon + \frac{\partial L}{\partial\dot{q}^i}\delta\dot{q}^i\epsilon + \frac{\partial L}{\partial t}\tau\epsilon$

where $\delta\dot{q}^i = \dot{\xi}^i - \dot{q}^i\dot{\tau}$ (the change in velocity accounting for the time reparametrization).

Invariance requires $\delta(L\,dt) = 0$, which gives $\delta L + L\dot{\tau} = 0$.

Using the Euler-Lagrange equations to simplify, and collecting total time derivatives:

$\frac{d}{dt}\left(\frac{\partial L}{\partial\dot{q}^i}\xi^i + L\tau - \frac{\partial L}{\partial\dot{q}^i}\dot{q}^i\tau\right) = 0$

$Q = \frac{\partial L}{\partial\dot{q}^i}\xi^i - (p_i\dot{q}^i - L)\tau = \frac{\partial L}{\partial\dot{q}^i}\xi^i - H\tau$

For $\tau = 1, \xi = 0$: $Q = -H$, so $dH/dt = 0$ — energy is conserved. $\checkmark$

---

*This chapter has built the complete formal apparatus of classical mechanics — Lagrangian and Hamiltonian — from the variational structure of the zone framework. Every equation traces back to the zone action. The student now has the tools to solve any classical mechanics problem; the next chapters apply them.*
