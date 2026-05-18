# Chapter 7: Classical Electrodynamics Complete

*Foundations of Genesis Physics — Volume 2: Forces and Fields*

---

> *"The field is the seat of all energy and all force."*
> — Adapted from Maxwell's conception of the electromagnetic field

---

## 7.1 The Road from Zone Geometry to Classical E&M

In Chapter 3 we accomplished something that standard physics never does: we *derived* Maxwell's equations. We showed that the off-diagonal metric components of the 6D zone manifold, upon Kaluza-Klein reduction, yield the electromagnetic four-potential $A_\mu$. The gauge invariance that every textbook postulates emerged as coordinate freedom in the $\xi$-direction (Eq. 2.3.9). The four Maxwell equations followed — two from the Euler-Lagrange equations of the gauge sector, two from the Bianchi identity — with not a single free parameter (Eqs. 2.3.27–2.3.42). The constants $\varepsilon_0$, $\mu_0$, and $c$ were not inputs; they were *outputs*, computed from warp-factor integrals over the extra dimensions (Eqs. 2.3.29–2.3.33). Even the fine structure constant $\alpha^{-1} \approx 137$ found its geometric origin in the ratio of zone extents (Eqs. 2.3.69–2.3.82).

In Chapters 5 and 6 we assembled the complete zone Lagrangian (Eq. 2.5.1) and showed that the gauge group $U(1) \times SU(2) \times SU(3)$ is uniquely forced by zone manifold topology (Theorem 2.6.1). The electromagnetic $U(1)$ sector is the isometry group of the $\xi$-direction circle (Eqs. 2.6.2–2.6.5).

The present chapter asks: *given that we have Maxwell's equations from first principles, what follows?*

The answer is: *all of classical electrodynamics.* Every result in Jackson's monumental textbook — radiation, waveguides, optics, circuits, shielding — follows from the four equations we derived in Chapter 3 and the Lagrangian formalism of Chapter 5. No new postulates are needed. No new constants must be introduced. The Firmament membrane gave us Maxwell's equations; those equations give us the rest.

[FIGURE: Fig 2.7.1 — Derivation Roadmap: From Zone Geometry to Classical E&M]

The roadmap (Fig. 2.7.1) illustrates the logical flow. From the 6D zone metric (Vol 1), Chapter 3 derived the four Maxwell equations. From those four equations, the present chapter branches into six domains: wave propagation (§7.2), radiation (§7.3), boundary phenomena (§7.4), waveguides (§7.5), circuits (§7.6), and optics (§7.7), with conducting media (§7.8) as a cross-cutting application. Each domain traces back to Chapter 3. No detours are needed.

Let us begin with the most fundamental consequence of Maxwell's equations: electromagnetic waves.

---

## 7.2 Electromagnetic Waves — Propagation, Polarization, and Energy

### 7.2.1 The wave equation from Maxwell's equations

Why do disturbances in the electromagnetic field propagate? Because the two curl equations — Faraday's law and the Ampère-Maxwell law — couple changes in **E** to changes in **B** and vice versa. A time-varying electric field generates a magnetic field; that changing magnetic field regenerates an electric field. The coupled dance propagates through space as a wave.

Let us make this precise. We begin with the two source-free curl equations derived in Chapter 3:

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \tag{2.7.1}$$

$$\nabla \times \mathbf{B} = \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} \tag{2.7.2}$$

These are Faraday's law (Eq. 2.3.42) and the vacuum Ampère-Maxwell law (Eq. 2.3.27 with $\mathbf{J} = 0$), restated here for reference.

Take the curl of (2.7.1):

$$\nabla \times (\nabla \times \mathbf{E}) = -\frac{\partial}{\partial t}(\nabla \times \mathbf{B}) \tag{2.7.3}$$

Substituting (2.7.2) into the right side:

$$\nabla \times (\nabla \times \mathbf{E}) = -\mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} \tag{2.7.4}$$

Using the vector identity $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$ and noting that Gauss's law in vacuum (Eq. 2.3.27) gives $\nabla \cdot \mathbf{E} = 0$:

$$\boxed{\nabla^2 \mathbf{E} = \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} = \frac{1}{c^2}\frac{\partial^2 \mathbf{E}}{\partial t^2}} \tag{2.7.5}$$

An identical derivation starting from (2.7.2) yields the same equation for **B**:

$$\nabla^2 \mathbf{B} = \frac{1}{c^2}\frac{\partial^2 \mathbf{B}}{\partial t^2} \tag{2.7.6}$$

Here we have used the relation $\varepsilon_0 \mu_0 = 1/c^2$ (Eq. 2.3.33), which is not a separate fact but a consequence of the warp-factor integrals.

Equations (2.7.5) and (2.7.6) are the electromagnetic wave equations. They tell us that the electromagnetic field propagates at speed $c$ — the Firmament membrane wave speed derived in Vol 1 (Eq. 1.5.36) as $c^2 = \sigma/\mu$, where $\sigma$ is the Firmament tension and $\mu$ its mass density. The wave speed is a *material property of the Firmament membrane*, not an arbitrary constant of nature.

### 7.2.2 Plane wave solutions and dispersion

The wave equation (2.7.5) admits plane wave solutions of the form:

$$\mathbf{E}(\mathbf{r}, t) = \mathbf{E}_0 \, e^{i(\mathbf{k} \cdot \mathbf{r} - \omega t)} \tag{2.7.7}$$

Substituting into (2.7.5) yields the dispersion relation:

$$\boxed{\omega = c|\mathbf{k}|} \tag{2.7.8}$$

This is the dispersion relation of a non-dispersive medium. Both the phase velocity $v_\text{ph} = \omega/|\mathbf{k}| = c$ and the group velocity $v_g = \partial\omega/\partial|\mathbf{k}| = c$ equal the speed of light. Electromagnetic waves in vacuum carry information at exactly $c$, with no frequency dependence — from radio waves at $\sim 10^3$ Hz to gamma rays at $\sim 10^{20}$ Hz, a span of 17 orders of magnitude.

Why is vacuum non-dispersive? Because the zone Lagrangian's gauge sector (Eq. 2.5.1, $\mathcal{L}_\text{gauge}$) contains only the standard kinetic term $-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}$. Higher-derivative corrections (e.g., $F^4$ terms) are suppressed by the zone energy scale — the characteristic energy set by the compactification radius of the extra dimensions, which is far above any classical electromagnetic frequency. These corrections would introduce dispersion, but in the classical limit they are negligible: the ratio of photon energy to the zone scale is vanishingly small for all frequencies we consider here.

### 7.2.3 Transversality and polarization

Gauss's law in vacuum ($\nabla \cdot \mathbf{E} = 0$) constrains the wave. For the plane wave (2.7.7):

$$\nabla \cdot \mathbf{E} = i\mathbf{k} \cdot \mathbf{E}_0 \, e^{i(\mathbf{k} \cdot \mathbf{r} - \omega t)} = 0 \tag{2.7.9}$$

Therefore $\mathbf{k} \cdot \mathbf{E}_0 = 0$: the electric field is *transverse* — perpendicular to the direction of propagation. Similarly, $\nabla \cdot \mathbf{B} = 0$ yields $\mathbf{k} \cdot \mathbf{B}_0 = 0$.

Faraday's law (2.7.1) relates the two amplitudes:

$$\mathbf{B}_0 = \frac{1}{\omega}\mathbf{k} \times \mathbf{E}_0 = \frac{1}{c}\hat{\mathbf{k}} \times \mathbf{E}_0 \tag{2.7.10}$$

The triad $(\hat{\mathbf{k}}, \mathbf{E}_0, \mathbf{B}_0)$ is mutually orthogonal, with $|\mathbf{B}_0| = |\mathbf{E}_0|/c$.

[FIGURE: Fig 2.7.2 — Electromagnetic Wave Propagation on the Firmament]

Why exactly two polarization states? The propagation direction $\hat{\mathbf{k}}$ is fixed. In the plane perpendicular to $\hat{\mathbf{k}}$, there are exactly two independent directions — call them $\hat{\mathbf{e}}_1$ and $\hat{\mathbf{e}}_2$. Any polarization is a superposition:

$$\mathbf{E}_0 = E_1 \hat{\mathbf{e}}_1 + E_2 \hat{\mathbf{e}}_2 \tag{2.7.11}$$

where $E_1$ and $E_2$ are complex amplitudes. The relative magnitude and phase determine the polarization state:

- **Linear polarization:** $E_2/E_1$ is real. The electric field oscillates in a fixed plane.
- **Circular polarization:** $|E_1| = |E_2|$ and $E_2/E_1 = \pm i$. The electric field traces a circle. The $+i$ case gives left-circular; the $-i$ case gives right-circular.
- **Elliptical polarization:** The general case. The field traces an ellipse.

[FIGURE: Fig 2.7.3 — Polarization States]

This two-fold polarization degeneracy is a direct consequence of the Firmament's codimension. The Firmament is a 4D membrane in 6D; electromagnetic waves propagate along it with their fields confined to the transverse directions within the Firmament membrane. On a 4D membrane, a wave propagating in one spatial direction leaves 2 transverse spatial dimensions — hence exactly 2 polarization states. If the Firmament had different codimension, or if we lived in a different-dimensional space, the number of polarizations would differ.

### 7.2.4 Energy transport: Poynting's theorem

Electromagnetic waves carry energy. To derive the energy transport, we appeal to the zone Lagrangian's gauge sector. In Chapter 3 we stated Poynting's theorem (Eqs. 2.3.94–2.3.98). Here we derive it from the full Lagrangian formalism of Chapter 5.

The electromagnetic energy density is:

$$u = \frac{1}{2}\left(\varepsilon_0 E^2 + \frac{B^2}{\mu_0}\right) \tag{2.7.12}$$

The energy flux (Poynting vector) is:

$$\mathbf{S} = \frac{1}{\mu_0}\mathbf{E} \times \mathbf{B} \tag{2.7.13}$$

Taking the time derivative of $u$ and using Maxwell's equations (2.7.1)–(2.7.2):

$$\frac{\partial u}{\partial t} = \varepsilon_0 \mathbf{E} \cdot \frac{\partial \mathbf{E}}{\partial t} + \frac{1}{\mu_0}\mathbf{B} \cdot \frac{\partial \mathbf{B}}{\partial t} \tag{2.7.14}$$

Substituting $\partial \mathbf{B}/\partial t = -\nabla \times \mathbf{E}$ from (2.7.1) and $\varepsilon_0 \partial \mathbf{E}/\partial t = \frac{1}{\mu_0}\nabla \times \mathbf{B} - \mathbf{J}$ from the full Ampère-Maxwell law:

$$\frac{\partial u}{\partial t} = \frac{1}{\mu_0}\mathbf{E} \cdot (\nabla \times \mathbf{B}) - \mathbf{E} \cdot \mathbf{J} - \frac{1}{\mu_0}\mathbf{B} \cdot (\nabla \times \mathbf{E}) \tag{2.7.15}$$

Using the vector identity $\nabla \cdot (\mathbf{E} \times \mathbf{B}) = \mathbf{B} \cdot (\nabla \times \mathbf{E}) - \mathbf{E} \cdot (\nabla \times \mathbf{B})$:

$$\boxed{\frac{\partial u}{\partial t} + \nabla \cdot \mathbf{S} = -\mathbf{J} \cdot \mathbf{E}} \tag{2.7.16}$$

This is **Poynting's theorem** — the local energy conservation law for the electromagnetic field. The left side is the rate of change of field energy density plus the divergence of energy flux. The right side, $-\mathbf{J} \cdot \mathbf{E}$, is the rate at which the field does work on charges (or receives energy from them). In vacuum ($\mathbf{J} = 0$), energy is exactly conserved: $\partial u/\partial t + \nabla \cdot \mathbf{S} = 0$.

This result is the Noether current for time-translation invariance of the electromagnetic Lagrangian. The zone Lagrangian (Eq. 2.5.1) is invariant under $t \to t + \text{const}$ (a Poincaré symmetry, Vol 1 Ch 7); Noether's theorem guarantees a conserved energy current, and Poynting's vector is precisely that current.

For a plane wave, the time-averaged Poynting vector is:

$$\langle \mathbf{S} \rangle = \frac{1}{2\mu_0}|\mathbf{E}_0|^2 \hat{\mathbf{k}} = \frac{c}{2}\varepsilon_0|\mathbf{E}_0|^2 \hat{\mathbf{k}} \tag{2.7.17}$$

The intensity $I = |\langle \mathbf{S} \rangle|$ has dimensions of power per unit area (W/m²) and is proportional to $E_0^2$ — a result that will matter for optics (§7.7) and for the photoelectric effect (which Vol 4 will treat quantum-mechanically).

**Radiation pressure.** A plane wave impinging on a perfectly absorbing surface transfers momentum at the rate $p_\text{rad} = I/c$ per unit area. For a perfectly reflecting surface, the pressure doubles: $p_\text{rad} = 2I/c$. This follows from the electromagnetic momentum density $\mathbf{g} = \mathbf{S}/c^2 = \varepsilon_0 \mathbf{E} \times \mathbf{B}$.

---

## 7.3 Electromagnetic Potentials and Radiation

### 7.3.1 Potentials as fundamental geometric objects

In Chapter 3 we showed that the electromagnetic four-potential $A_\mu$ is not an auxiliary construct but the off-diagonal component of the 6D metric (Eq. 2.3.1). The physical fields $\mathbf{E}$ and $\mathbf{B}$ are derived quantities:

$$\mathbf{E} = -\nabla\phi - \frac{\partial \mathbf{A}}{\partial t}, \qquad \mathbf{B} = \nabla \times \mathbf{A} \tag{2.7.18}$$

where $\phi = A_0$ (the time component) and $\mathbf{A} = (A_1, A_2, A_3)$ (the spatial components).

The field strength tensor is:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu \tag{2.7.19}$$

This is gauge-invariant: the transformation $A_\mu \to A_\mu + \partial_\mu \Lambda$ (Eq. 2.3.9, arising from reparameterization $\xi \to \xi + \Lambda(x)$ in the extra dimension) leaves $F_{\mu\nu}$ unchanged.

### 7.3.2 Gauge choices

The gauge freedom allows us to impose one additional condition on $A_\mu$, simplifying calculations without changing the physics.

**Lorenz gauge:** $\partial_\mu A^\mu = 0$, or equivalently:

$$\nabla \cdot \mathbf{A} + \frac{1}{c^2}\frac{\partial \phi}{\partial t} = 0 \tag{2.7.20}$$

In this gauge, Maxwell's equations decouple into wave equations for each component:

$$\Box^2 \phi = -\frac{\rho}{\varepsilon_0}, \qquad \Box^2 \mathbf{A} = -\mu_0 \mathbf{J} \tag{2.7.21}$$

where $\Box^2 = \nabla^2 - (1/c^2)\partial^2/\partial t^2$ is the d'Alembertian. These are manifestly Lorentz-covariant — as they must be, since the wave speed $c$ is the Firmament's intrinsic speed.

**Coulomb gauge:** $\nabla \cdot \mathbf{A} = 0$. This gauge is not Lorentz-covariant but separates the instantaneous Coulomb field from the radiative transverse field. It is useful for near-field problems and connects naturally to the electrostatic limit.

Why two gauges? Because different problems benefit from different simplifications. The Lorenz gauge respects Lorentz invariance and is natural for radiation; the Coulomb gauge separates longitudinal (non-radiative) from transverse (radiative) degrees of freedom. The physics is identical in both — only the book-keeping differs.

### 7.3.3 Retarded potentials

The wave equations (2.7.21) in the Lorenz gauge have a unique causal solution given by the retarded Green's function:

$$\phi(\mathbf{r}, t) = \frac{1}{4\pi\varepsilon_0} \int \frac{\rho(\mathbf{r}', t_\text{ret})}{|\mathbf{r} - \mathbf{r}'|} \, d^3r' \tag{2.7.22}$$

$$\mathbf{A}(\mathbf{r}, t) = \frac{\mu_0}{4\pi} \int \frac{\mathbf{J}(\mathbf{r}', t_\text{ret})}{|\mathbf{r} - \mathbf{r}'|} \, d^3r' \tag{2.7.23}$$

where the retarded time is:

$$t_\text{ret} = t - \frac{|\mathbf{r} - \mathbf{r}'|}{c} \tag{2.7.24}$$

[FIGURE: Fig 2.7.4 — Retarded Potential and Light Cone]

Why retarded and not advanced? Because the Green's function of the wave equation admits both retarded and advanced solutions. The retarded solution respects causality: the field at $(\mathbf{r}, t)$ depends on the source at earlier times, not later ones. This is not a boundary condition we impose by hand — it follows from the arrow of time established by the Degradation Principle (Vol 1, Ch 8, Eq. 1.8.12), which ensures entropy increases and effects follow causes.

### 7.3.4 Radiation from accelerating charges

Now we derive the central result: accelerating charges radiate. A charge $q$ moving with velocity $\mathbf{v}(t)$ and acceleration $\mathbf{a}(t)$ produces, at large distances, radiation fields that fall off as $1/r$ (unlike the $1/r^2$ Coulomb field).

To extract the radiation field, we evaluate the retarded potentials (2.7.22–2.7.23) for a point charge $q$ at position $\mathbf{r}_0(t)$ with velocity $\mathbf{v}(t)$ and acceleration $\mathbf{a}(t)$.

The vector potential is:

$$\mathbf{A}(\mathbf{r}, t) = \frac{\mu_0 q}{4\pi}\frac{\mathbf{v}(t_\text{ret})}{R(1 - \hat{\mathbf{R}} \cdot \mathbf{v}/c)} \tag{2.7.25a}$$

where $\mathbf{R} = \mathbf{r} - \mathbf{r}_0(t_\text{ret})$ and the denominator accounts for the retardation effect (the source moves during signal transit). The electric field obtained from $\mathbf{E} = -\nabla\phi - \partial\mathbf{A}/\partial t$ separates into two terms:

$$\mathbf{E} = \underbrace{\frac{q}{4\pi\varepsilon_0}\frac{(\hat{\mathbf{R}} - \mathbf{v}/c)(1 - v^2/c^2)}{R^2(1 - \hat{\mathbf{R}} \cdot \mathbf{v}/c)^3}}_{\text{velocity field} \sim 1/R^2} + \underbrace{\frac{q}{4\pi\varepsilon_0 c}\frac{\hat{\mathbf{R}} \times [(\hat{\mathbf{R}} - \mathbf{v}/c) \times \mathbf{a}]}{R(1 - \hat{\mathbf{R}} \cdot \mathbf{v}/c)^3}}_{\text{acceleration field} \sim 1/R} \tag{2.7.25b}$$

The first term is the generalized Coulomb field (it falls as $1/R^2$ and carries no net energy to infinity). The second term — the *radiation field* — falls as $1/R$ and carries energy away from the source. Only accelerating charges contribute to this term. The separation arises because the time derivative $\partial\mathbf{A}/\partial t$ applied to the $1/R$ potential generates both a $1/R^2$ piece (from differentiating $1/R$ itself) and a $1/R$ piece (from differentiating the velocity-dependent numerator, which introduces the acceleration $\mathbf{a}$). It is this second contribution that survives at large $R$ and constitutes radiation.

In the non-relativistic limit ($v \ll c$), the radiation field simplifies to:

$$\mathbf{E}_\text{rad} = \frac{q}{4\pi\varepsilon_0 c^2 r}\left[\hat{\mathbf{r}} \times (\hat{\mathbf{r}} \times \mathbf{a})\right]_{t_\text{ret}} \tag{2.7.25}$$

where $\hat{\mathbf{r}}$ points from source to field point, and all quantities are evaluated at the retarded time. The corresponding magnetic field is $\mathbf{B}_\text{rad} = \hat{\mathbf{r}} \times \mathbf{E}_\text{rad}/c$.

The double cross product gives the angular pattern: $|\hat{\mathbf{r}} \times (\hat{\mathbf{r}} \times \mathbf{a})| = a\sin\theta$, where $\theta$ is the angle between $\hat{\mathbf{r}}$ and $\mathbf{a}$. The radiation intensity is therefore proportional to $\sin^2\theta$: maximum perpendicular to the acceleration, zero along the acceleration axis. This is the **dipole radiation pattern**.

[FIGURE: Fig 2.7.5 — Radiation Pattern from Accelerating Charge]

The total power radiated is obtained by integrating the Poynting vector over a sphere:

$$\boxed{P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}} \tag{2.7.26}$$

This is the **Larmor formula**, derived here from the retarded-potential solution of the zone-architecture Maxwell equations. Every quantity in this expression has been derived from zone geometry: $q$ is quantized by $\xi$-topology (Eq. 2.3.83), $\varepsilon_0$ from warp-factor integrals (Eq. 2.3.29), and $c$ from Firmament mechanics (Eq. 1.5.36).

The Larmor formula answers a deep question: *why do accelerating charges radiate?* Because the retarded-potential solution of the wave equation couples field propagation to source dynamics. An accelerating source creates a kink in the field lines — that kink propagates outward at $c$ as radiation. The mechanism is purely geometric: the wave equation on the Firmament membrane forces field disturbances to propagate, and acceleration creates those disturbances.

**Oscillating dipole.** For a harmonically oscillating dipole $\mathbf{p}(t) = \mathbf{p}_0 e^{-i\omega t}$, the time-averaged radiated power is:

$$\langle P \rangle = \frac{\omega^4 |\mathbf{p}_0|^2}{12\pi\varepsilon_0 c^3} \tag{2.7.27}$$

The $\omega^4$ dependence explains why the sky is blue: Rayleigh scattering involves atmospheric molecules acting as oscillating dipoles driven by sunlight, and the shorter-wavelength (higher-frequency) blue light is scattered far more strongly than red.

> **Worked Example 7.2: Synchrotron Radiation Power.**
> An electron ($q = 1.60 \times 10^{-19}$ C) in a synchrotron has centripetal acceleration $a = v^2/R$ where $v \approx c$ and $R = 100$ m. Using the Larmor formula (2.7.26):
>
> $a = c^2/R = (3.00 \times 10^8)^2/100 = 9.0 \times 10^{14}$ m/s²
>
> $P = \frac{(1.60 \times 10^{-19})^2 (9.0 \times 10^{14})^2}{6\pi(8.854 \times 10^{-12})(3.00 \times 10^8)^3}$
>
> $= \frac{2.56 \times 10^{-38} \times 8.1 \times 10^{29}}{6\pi \times 8.854 \times 10^{-12} \times 2.7 \times 10^{25}} = \frac{2.07 \times 10^{-8}}{4.50 \times 10^{15}} = 4.6 \times 10^{-24}$ W
>
> This is tiny per electron, but a synchrotron beam with $N \sim 10^{12}$ electrons radiates $\sim 4.6$ μW — visible as synchrotron radiation, a direct confirmation of the Larmor formula. (The full relativistic treatment, using the Liénard formula $P = q^2\gamma^6 a^2/(6\pi\varepsilon_0 c^3)$ with $\gamma \gg 1$, gives enormously larger power at GeV energies. The non-relativistic Larmor formula here gives only the conceptual mechanism.)

**Radiation reaction.** The radiated energy must come from somewhere — it comes from the kinetic energy of the charge, implying a radiation-reaction force. The Abraham-Lorentz force is $\mathbf{F}_\text{rad} = \frac{q^2}{6\pi\varepsilon_0 c^3}\dot{\mathbf{a}}$. This expression involves the time derivative of acceleration and leads to well-known pathologies (runaway solutions, pre-acceleration). These are artifacts of treating point charges classically and are resolved in the quantum treatment (Vol 4). We note the issue honestly and move on.

---

## 7.4 Boundary Conditions, Reflection, and Refraction

### 7.4.1 The four boundary conditions

When electromagnetic waves encounter an interface between two media, continuity conditions on the fields determine the reflected and transmitted waves. These conditions are not additional postulates — they follow directly from Maxwell's equations applied to the boundary.

[FIGURE: Fig 2.7.6 — EM Boundary Conditions at Interface]

Consider a planar interface between medium 1 (permittivity $\varepsilon_1$, permeability $\mu_1$) and medium 2 ($\varepsilon_2$, $\mu_2$). Applying Maxwell's equations in integral form to a thin pillbox straddling the interface, and to a thin rectangular loop, we obtain four conditions:

**From Gauss's law** ($\nabla \cdot \mathbf{D} = \rho_f$), using a pillbox of vanishing height:

$$D_{1\perp} - D_{2\perp} = \sigma_f \tag{2.7.28}$$

where $\sigma_f$ is the free surface charge density. In the absence of free surface charge: $\varepsilon_1 E_{1\perp} = \varepsilon_2 E_{2\perp}$.

**From $\nabla \cdot \mathbf{B} = 0$** (no magnetic monopoles), same pillbox:

$$B_{1\perp} = B_{2\perp} \tag{2.7.29}$$

This is always true — there are no magnetic surface charges.

**From Faraday's law** ($\nabla \times \mathbf{E} = -\partial\mathbf{B}/\partial t$), using a thin loop:

$$E_{1\parallel} = E_{2\parallel} \tag{2.7.30}$$

Tangential **E** is always continuous.

**From Ampère-Maxwell law** ($\nabla \times \mathbf{H} = \mathbf{J}_f + \partial\mathbf{D}/\partial t$), thin loop:

$$H_{1\parallel} - H_{2\parallel} = K_f \tag{2.7.31}$$

where $K_f$ is the free surface current density. In the absence of free surface currents: $H_{1\parallel} = H_{2\parallel}$, or equivalently $B_{1\parallel}/\mu_1 = B_{2\parallel}/\mu_2$.

These four conditions — two on normal components, two on tangential — are the complete set needed to solve any boundary-value problem in electromagnetism.

### 7.4.2 Snell's law of refraction

Consider a plane wave incident on a planar interface. The tangential **E**-field must be continuous everywhere on the boundary at all times. This forces the tangential components of all three wavevectors (incident, reflected, transmitted) to match:

$$k_1 \sin\theta_i = k_1 \sin\theta_r = k_2 \sin\theta_t \tag{2.7.32}$$

From the first equality: $\theta_r = \theta_i$ (angle of reflection equals angle of incidence).

From the second, using $k = n\omega/c$ where $n$ is the refractive index:

$$\boxed{n_1 \sin\theta_i = n_2 \sin\theta_t} \tag{2.7.33}$$

This is **Snell's law**. It was not postulated — it followed from the continuity of tangential **E** at the interface, which itself followed from Faraday's law, which was derived from the zone manifold in Chapter 3.

The refractive index $n = c/v_\text{phase} = \sqrt{\varepsilon_r \mu_r}$ is the ratio of the vacuum wave speed (set by the Firmament membrane) to the wave speed in the medium. In standard treatments, $n$ is measured; in zone architecture, it can in principle be computed from the material's electromagnetic response to the zone-derived fields.

### 7.4.3 Fresnel equations

The boundary conditions not only determine the *direction* of reflected and transmitted waves but also their *amplitudes*. The results depend on the polarization state.

Consider **s-polarization** (E perpendicular to the plane of incidence, i.e., parallel to the interface). The electric field has only a tangential component. Applying the boundary conditions (2.7.30) and (2.7.31):

From tangential E continuity (2.7.30):

$$E_i + E_r = E_t \tag{2.7.34a}$$

From tangential H continuity (2.7.31), using $H = B/\mu \approx nE/(\mu_0 c)$ for non-magnetic media:

$$n_1(E_i - E_r)\cos\theta_i = n_2 E_t \cos\theta_t \tag{2.7.34b}$$

The minus sign on $E_r$ arises because the reflected wave's wavevector has the opposite normal component. Solving this $2 \times 2$ system for $r_s = E_r/E_i$ and $t_s = E_t/E_i$:

$$r_s = \frac{n_1\cos\theta_i - n_2\cos\theta_t}{n_1\cos\theta_i + n_2\cos\theta_t}, \qquad t_s = \frac{2n_1\cos\theta_i}{n_1\cos\theta_i + n_2\cos\theta_t} \tag{2.7.34}$$

For **p-polarization** (E in the plane of incidence), the analysis is analogous but the field components that are tangential and normal swap roles. Applying the same boundary conditions yields:

$$r_p = \frac{n_2\cos\theta_i - n_1\cos\theta_t}{n_2\cos\theta_i + n_1\cos\theta_t}, \qquad t_p = \frac{2n_1\cos\theta_i}{n_2\cos\theta_i + n_1\cos\theta_t} \tag{2.7.35}$$

Note the asymmetry: for s-polarization, the numerator is $n_1\cos\theta_i - n_2\cos\theta_t$; for p-polarization, it is $n_2\cos\theta_i - n_1\cos\theta_t$. This asymmetry is why Brewster's angle exists for p-polarization but not for s-polarization (in non-magnetic media).

Energy conservation provides a consistency check. The reflectance and transmittance must satisfy $R + T = 1$, where $R = |r|^2$ and $T = |t|^2 (n_2\cos\theta_t)/(n_1\cos\theta_i)$. The factor of $n_2\cos\theta_t/(n_1\cos\theta_i)$ accounts for the change in beam cross-section and wave impedance at the interface. The reader should verify this as an exercise (Problem 7.2).

[FIGURE: Fig 2.7.7 — Reflection, Refraction, and Total Internal Reflection]

[FIGURE: Fig 2.7.8 — Fresnel Coefficients vs. Angle]

**Brewster's angle.** Setting $r_p = 0$ gives $n_2\cos\theta_i = n_1\cos\theta_t$. Combined with Snell's law, this yields:

$$\tan\theta_B = \frac{n_2}{n_1} \tag{2.7.36}$$

At Brewster's angle, the reflected light is purely s-polarized. This is the principle behind polarizing sunglasses and Brewster windows in laser cavities.

### 7.4.4 Total internal reflection

When $n_1 > n_2$ (light going from a denser to a rarer medium), Snell's law gives $\sin\theta_t = (n_1/n_2)\sin\theta_i > 1$ for angles above the critical angle:

$$\boxed{\theta_c = \arcsin\left(\frac{n_2}{n_1}\right)} \tag{2.7.37}$$

For $\theta_i > \theta_c$, $\cos\theta_t$ becomes imaginary. Physically, this means the transmitted wavenumber component normal to the interface, $k_z = (n_2\omega/c)\cos\theta_t$, is purely imaginary — so the plane-wave factor $e^{ik_z z}$ becomes a real exponential decay $e^{-\kappa z}$ rather than an oscillation. No transmitted propagating wave exists and the wave is totally reflected. However, an evanescent field penetrates into medium 2, decaying exponentially with depth:

$$E_2 \propto e^{-\kappa z}, \qquad \kappa = \frac{\omega}{c}\sqrt{n_1^2\sin^2\theta_i - n_2^2} \tag{2.7.38}$$

The evanescent wave carries no net energy into medium 2 (the time-averaged Poynting vector normal to the interface vanishes). This phenomenon is the basis of optical fibers, which confine light by total internal reflection, and of frustrated total internal reflection used in optical beam splitters.

---

## 7.5 Waveguides and Confined Electromagnetic Fields

### 7.5.1 Why confinement quantizes modes

In Vol 1, Chapter 10, we showed that boundary conditions on the zone manifold quantize allowed states. The same mechanism operates here in a more familiar setting. When electromagnetic waves propagate inside a hollow conductor of finite cross-section, the boundary conditions at the walls ($E_\parallel = 0$ and $B_\perp = 0$ on a perfect conductor) restrict the allowed transverse field patterns to discrete modes — just as standing waves on a string can only have wavelengths that fit the string length.

### 7.5.2 Rectangular waveguide

Consider a rectangular waveguide with cross-section $a \times b$ ($a > b$), aligned along the $z$-axis. We seek solutions propagating as $e^{i(k_z z - \omega t)}$ with fields confined to the interior.

We begin from the full wave equation (2.7.5) and assume a field of the form $\psi(x,y,z,t) = \psi_\perp(x,y) \, e^{i(k_z z - \omega t)}$, where $\psi$ stands for any field component. Substituting into the wave equation and separating the longitudinal propagation from the transverse structure:

$$\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right)\psi_\perp + k_\perp^2 \psi_\perp = 0 \tag{2.7.39}$$

where the transverse wavenumber is:

$$k_\perp^2 = \frac{\omega^2}{c^2} - k_z^2 \tag{2.7.39a}$$

This is a 2D Helmholtz equation — the same mathematical structure that appears in quantum mechanics for a particle in a box (and for the same reason: boundary conditions on a finite domain).

For a rectangular waveguide, we further separate variables: $\psi_\perp(x,y) = X(x)Y(y)$. Each factor satisfies $X'' + k_x^2 X = 0$ and $Y'' + k_y^2 Y = 0$ with $k_x^2 + k_y^2 = k_\perp^2$. The boundary conditions determine the allowed solutions.

**TM modes** ($B_z = 0$ everywhere; the longitudinal component is $E_z$). The tangential electric field must vanish at a perfect conductor, so $E_z = 0$ at all four walls: $x = 0$, $x = a$, $y = 0$, $y = b$. The vanishing at $x = 0$ and $y = 0$ selects sine functions; the vanishing at $x = a$ and $y = b$ quantizes the wavenumbers: $k_x = m\pi/a$, $k_y = n\pi/b$ with $m, n = 1, 2, 3, \ldots$ Therefore:

$$E_z = E_0 \sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{n\pi y}{b}\right)e^{i(k_z z - \omega t)} \tag{2.7.40}$$

with $m, n \geq 1$ (both must be at least 1 for TM modes; $m = 0$ or $n = 0$ gives $E_z = 0$ identically). The transverse wavenumber is:

$$k_\perp^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 \tag{2.7.41}$$

The transverse E and B components are derived from $E_z$ using the relation between longitudinal and transverse fields that follows from Maxwell's equations:

$$\mathbf{E}_\perp = \frac{ik_z}{k_\perp^2}\nabla_\perp E_z, \qquad \mathbf{B}_\perp = \frac{i\omega}{c^2 k_\perp^2}\hat{\mathbf{z}} \times \nabla_\perp E_z \tag{2.7.41a}$$

These relations show that once $E_z$ is known, all other field components follow. The transverse fields inherit the sine/cosine structure of $E_z$.

**TE modes** ($E_z = 0$ everywhere; the longitudinal component is $B_z$). The boundary condition for $B_z$ at a perfect conductor is $\partial B_z/\partial n = 0$ (the normal derivative vanishes), which follows from $E_\parallel = 0$ at the wall via Maxwell's equations. This selects cosine functions with the same quantized wavenumbers:

$$B_z = B_0 \cos\left(\frac{m\pi x}{a}\right)\cos\left(\frac{n\pi y}{b}\right)e^{i(k_z z - \omega t)} \tag{2.7.42}$$

with $m, n \geq 0$ (but not both zero — that would give a uniform field with no transverse structure, hence no guided mode). The same $k_\perp$ relation (2.7.41) holds, and the transverse fields follow from analogous relations to (2.7.41a).

### 7.5.3 Cutoff frequencies and dispersion

For propagation, $k_z$ must be real, which requires $\omega > ck_\perp$. The cutoff frequency for the $(m,n)$ mode is:

$$\boxed{\omega_{mn} = c\pi\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}} \tag{2.7.43}$$

Below this frequency, $k_z$ is imaginary and the wave decays exponentially (evanescent). The mode with the lowest cutoff is TE$_{10}$ (with $m=1, n=0$):

$$\omega_{10} = \frac{c\pi}{a} \tag{2.7.44}$$

This is the fundamental mode. For $\omega_{10} < \omega < \omega_{01}$, only the TE$_{10}$ mode propagates — single-mode operation.

[FIGURE: Fig 2.7.9 — Waveguide Cross-Section and Mode Patterns]

The dispersion relation for a propagating mode is:

$$\omega^2 = \omega_{mn}^2 + c^2 k_z^2 \tag{2.7.45}$$

[FIGURE: Fig 2.7.10 — Dispersion Relation in Waveguide]

Notice the structure: because boundary conditions force a nonzero transverse wavenumber $k_\perp$, the wave must devote part of its total $\omega/c$ budget to the transverse directions. Only the remainder goes into longitudinal propagation. This is why the waveguide mode behaves as though it has mass — the confined transverse degrees of freedom act as an energy threshold that must be exceeded before longitudinal propagation can occur. Formally, this is a *massive* dispersion relation, identical in form to the relativistic energy-momentum relation $E^2 = (m_\text{eff}c^2)^2 + (pc)^2$ with an effective mass $m_\text{eff}c^2 = \hbar\omega_{mn}$. The phase and group velocities are:

$$v_\text{ph} = \frac{\omega}{k_z} = \frac{c}{\sqrt{1 - (\omega_{mn}/\omega)^2}} > c \tag{2.7.46}$$

$$v_g = \frac{\partial\omega}{\partial k_z} = c\sqrt{1 - (\omega_{mn}/\omega)^2} < c \tag{2.7.47}$$

The phase velocity exceeds $c$, but the group velocity (which carries energy and information) is always less than $c$. Their product is $v_\text{ph} \cdot v_g = c^2$, a universal relation.

Why do waveguides have cutoff frequencies? The transverse boundary conditions quantize the allowed transverse wavenumbers (just as boundary conditions quantize energy levels in Vol 1, Ch 10). A minimum transverse wavenumber implies a minimum frequency for propagation. Below cutoff, the wave cannot "fit" inside the guide and decays exponentially. This is the same boundary-condition quantization mechanism that operates throughout zone architecture — here applied to a macroscopic electromagnetic system.

### 7.5.4 Cylindrical waveguides and optical fibers

In cylindrical geometry (radius $a$), the transverse equation separates in polar coordinates and involves Bessel functions $J_m(\kappa r)$ inside the core and modified Bessel functions $K_m(\gamma r)$ in the cladding. The matching conditions at $r = a$ yield the characteristic equation for guided modes.

The key parameter is the **V-number**:

$$V = \frac{2\pi a}{\lambda}\sqrt{n_\text{core}^2 - n_\text{clad}^2} \tag{2.7.48}$$

For $V < 2.405$ (the first zero of $J_0$), only the fundamental LP$_{01}$ mode propagates — single-mode fiber. This is the design regime for long-distance telecommunications, where single-mode operation minimizes pulse dispersion.

In cylindrical coordinates, the transverse wave equation (2.7.39) becomes a Bessel equation. Inside the core ($r < a$), the radial dependence is $J_m(\kappa r)$ where $\kappa^2 = n_\text{core}^2 k_0^2 - \beta^2$, $\beta = k_z$ is the propagation constant, and $k_0 = \omega/c$. In the cladding ($r > a$), the field must decay: the radial dependence is $K_m(\gamma r)$ where $\gamma^2 = \beta^2 - n_\text{clad}^2 k_0^2$. Matching $E_z$, $H_z$, $E_\phi$, and $H_\phi$ at $r = a$ yields the characteristic equation:

$$\left[\frac{J_m'(\kappa a)}{\kappa a J_m(\kappa a)} + \frac{K_m'(\gamma a)}{\gamma a K_m(\gamma a)}\right]\left[\frac{n_\text{core}^2 J_m'(\kappa a)}{\kappa a J_m(\kappa a)} + \frac{n_\text{clad}^2 K_m'(\gamma a)}{\gamma a K_m(\gamma a)}\right] = m^2\left(\frac{1}{(\kappa a)^2} + \frac{1}{(\gamma a)^2}\right)^2\frac{\beta^2}{k_0^2} \tag{2.7.49}$$

This is a transcendental equation in $\beta$ that must be solved numerically for each azimuthal order $m$. The V-number (2.7.48) determines how many solutions exist: for $V < 2.405$, only the fundamental LP$_{01}$ mode propagates.

The physics is identical to the rectangular case: boundary conditions at the core-cladding interface quantize the allowed transverse modes. The difference is geometry (cylindrical vs. rectangular) and the confining mechanism (total internal reflection at the core-cladding interface rather than conducting walls).

> **Worked Example 7.1: Standard Single-Mode Fiber.**
> An SMF-28 optical fiber has $n_\text{core} = 1.4681$, $n_\text{clad} = 1.4629$, and core radius $a = 4.1$ μm. At $\lambda = 1550$ nm:
>
> $V = \frac{2\pi(4.1 \times 10^{-6})}{1550 \times 10^{-9}}\sqrt{1.4681^2 - 1.4629^2} = \frac{2\pi(4.1)}{1.55}\sqrt{0.01527} = 16.61 \times 0.1236 = 2.05$
>
> Since $V = 2.05 < 2.405$, only the fundamental LP$_{01}$ mode propagates — single-mode operation, as designed. At $\lambda = 1260$ nm, $V = 2.52 > 2.405$, and the fiber becomes multi-mode. The cutoff wavelength is $\lambda_c = 1260$ nm for this fiber design.

---

## 7.6 Circuit Theory as a Limit of Field Theory

### 7.6.1 From fields to circuits

[FIGURE: Fig 2.7.11 — Circuit Elements from Maxwell Equations]

Circuit theory is not a separate subject. It is the quasi-static, lumped-element limit of Maxwell's equations. When the dimensions of a circuit are much smaller than the electromagnetic wavelength ($\ell \ll \lambda = c/f$), the fields are well-approximated by their static or slowly-varying forms, and the distributed Maxwell equations reduce to ordinary differential equations relating voltage and current at discrete nodes.

Let us make this reduction explicit.

### 7.6.2 Ohm's law

In a conductor, free electrons experience the zone-derived Coulomb force from the electric field and collisional drag from the lattice. The Drude model gives the equation of motion for an electron:

$$m_e \frac{d\mathbf{v}}{dt} = -e\mathbf{E} - \frac{m_e}{\tau}\mathbf{v} \tag{2.7.49}$$

where $\tau$ is the mean free time between collisions. In steady state ($d\mathbf{v}/dt = 0$):

$$\mathbf{v}_d = -\frac{e\tau}{m_e}\mathbf{E} \tag{2.7.50}$$

The current density is $\mathbf{J} = -ne\mathbf{v}_d$ (where $n$ is the electron number density):

$$\boxed{\mathbf{J} = \sigma\mathbf{E}, \qquad \sigma = \frac{ne^2\tau}{m_e}} \tag{2.7.51}$$

This is **Ohm's law** in its local form. For a uniform wire of length $L$ and cross-section $A$, integrating gives $V = IR$ with $R = L/(\sigma A) = \rho L/A$.

Every quantity traces to zone architecture: $e$ from $\xi$-topology (Eq. 2.3.83), $m_e$ from the Yukawa coupling to the Higgs sector (treated in Vol 4), and $\varepsilon_0$ (which determines the Coulomb force) from warp-factor integrals.

### 7.6.3 Kirchhoff's current law (KCL)

Kirchhoff's current law states that the total current entering a node equals the total current leaving it:

$$\sum_k I_k = 0 \tag{2.7.52}$$

This is not a separate law. It is the integral form of charge conservation:

$$\frac{\partial\rho}{\partial t} + \nabla \cdot \mathbf{J} = 0 \tag{2.7.53}$$

In steady state ($\partial\rho/\partial t = 0$), integrating over a small volume containing the node and applying the divergence theorem gives $\oint \mathbf{J} \cdot d\mathbf{A} = 0$, which is exactly (2.7.52).

Charge conservation itself is a Noether current: it follows from the $U(1)$ gauge symmetry of the zone Lagrangian (Vol 1, Ch 7, Eqs. 1.7.35–1.7.36; Vol 2, Ch 6, Eqs. 2.6.2–2.6.5). KCL is gauge symmetry in disguise.

### 7.6.4 Kirchhoff's voltage law (KVL)

For a closed loop in a circuit:

$$\sum_k V_k = 0 \tag{2.7.54}$$

This follows from the conservative nature of the electrostatic field. In the static limit, $\nabla \times \mathbf{E} = 0$ (Faraday's law with $\partial\mathbf{B}/\partial t = 0$), so **E** is the gradient of a potential: $\mathbf{E} = -\nabla\phi$. The line integral around a closed loop vanishes:

$$\oint \mathbf{E} \cdot d\mathbf{l} = -\oint d\phi = 0 \tag{2.7.55}$$

which is (2.7.54). When time-varying magnetic flux is present, KVL generalizes to include EMFs from Faraday's law, but the origin remains the same: Maxwell's equations on the zone manifold.

### 7.6.5 Capacitance

A capacitor stores energy in the electric field between its plates. For parallel plates of area $A$ separated by distance $d$:

Gauss's law (derived in Ch 3) gives the field between the plates:

$$E = \frac{\sigma_\text{charge}}{\varepsilon_0} = \frac{Q}{\varepsilon_0 A} \tag{2.7.56}$$

The voltage is $V = Ed = Q d/(\varepsilon_0 A)$, giving:

$$\boxed{C = \frac{Q}{V} = \frac{\varepsilon_0 A}{d}} \tag{2.7.57}$$

The energy stored is:

$$U_C = \frac{1}{2}CV^2 = \frac{1}{2}\frac{Q^2}{C} = \frac{\varepsilon_0}{2}\int E^2 \, dV \tag{2.7.58}$$

The last form makes explicit that the energy resides in the electric field — this is the EM energy density $u_E = \varepsilon_0 E^2/2$ from Eq. (2.7.12), integrated over the volume between the plates.

With a dielectric of relative permittivity $\varepsilon_r$: $C = \varepsilon_0 \varepsilon_r A/d$.

### 7.6.6 Inductance and Faraday's law

An inductor stores energy in the magnetic field. For a solenoid of $N$ turns, length $\ell$, and cross-sectional area $A$:

Ampère's law (from Ch 3) gives the field inside:

$$B = \mu_0 \frac{NI}{\ell} \tag{2.7.59}$$

The total magnetic flux linkage is $\Psi = NBA = \mu_0 N^2 IA/\ell$, giving:

$$\boxed{L = \frac{\Psi}{I} = \frac{\mu_0 N^2 A}{\ell}} \tag{2.7.60}$$

Faraday's law (Eq. 2.7.1) gives the induced EMF:

$$\mathcal{E} = -\frac{d\Psi}{dt} = -L\frac{dI}{dt} \tag{2.7.61}$$

The energy stored is:

$$U_L = \frac{1}{2}LI^2 = \frac{1}{2\mu_0}\int B^2 \, dV \tag{2.7.62}$$

Again, the energy resides in the magnetic field — this is $u_B = B^2/(2\mu_0)$ from Eq. (2.7.12).

### 7.6.7 LC and RLC oscillations

Combining a capacitor and inductor in series:

$$L\frac{d^2Q}{dt^2} + \frac{Q}{C} = 0 \tag{2.7.63}$$

This is a simple harmonic oscillator with natural frequency:

$$\boxed{\omega_0 = \frac{1}{\sqrt{LC}}} \tag{2.7.64}$$

Energy oscillates between the electric field (capacitor) and the magnetic field (inductor) at frequency $\omega_0$.

Adding resistance $R$ gives the damped oscillator:

$$L\frac{d^2Q}{dt^2} + R\frac{dQ}{dt} + \frac{Q}{C} = 0 \tag{2.7.65}$$

The solution depends on the damping ratio $\Gamma = R/(2L)$ relative to $\omega_0$:

- **Underdamped** ($\Gamma < \omega_0$): $Q(t) = Q_0 e^{-\Gamma t}\cos(\omega_d t + \varphi)$ with $\omega_d = \sqrt{\omega_0^2 - \Gamma^2}$
- **Critically damped** ($\Gamma = \omega_0$): $Q(t) = (A + Bt)e^{-\omega_0 t}$
- **Overdamped** ($\Gamma > \omega_0$): two real exponential decays

For a driven RLC circuit with $V(t) = V_0\cos\omega t$, the current amplitude is:

$$I_0(\omega) = \frac{V_0}{\sqrt{R^2 + (\omega L - 1/\omega C)^2}} \tag{2.7.66}$$

Maximum current occurs at resonance: $\omega = \omega_0 = 1/\sqrt{LC}$, where $I_0 = V_0/R$. The quality factor $Q = \omega_0 L/R$ measures the resonance sharpness.

[FIGURE: Fig 2.7.12 — RLC Resonance Curve]

The connection to waveguides is not accidental. Both waveguide cutoff (§7.5) and circuit resonance are manifestations of boundary-condition quantization interacting with the wave equation. The waveguide is a distributed system; the RLC circuit is the lumped-element limit of the same physics.

> **Worked Example 7.3: AM Radio Tuner.**
> An AM radio station broadcasts at $f_0 = 1000$ kHz. Design a tuning circuit with $C = 200$ pF.
>
> Required inductance: $L = 1/(\omega_0^2 C) = 1/[(2\pi \times 10^6)^2 \times 200 \times 10^{-12}] = 1/(3.95 \times 10^{13} \times 2.0 \times 10^{-10}) = 126.7$ μH.
>
> For $Q = 50$ (reasonable for a practical coil): $R = \omega_0 L/Q = (2\pi \times 10^6)(126.7 \times 10^{-6})/50 = 15.9$ Ω.
>
> The bandwidth is $\Delta f = f_0/Q = 1000/50 = 20$ kHz. This is exactly wide enough to pass the 10 kHz audio bandwidth of an AM signal while rejecting adjacent stations at $\pm 10$ kHz spacing.
>
> Every parameter in this design traces to zone-derived physics: the resonance frequency to $1/\sqrt{LC}$ (which combines Gauss's law through $C$ and Faraday's law through $L$), the Q-factor to the ratio of stored to dissipated energy (from Poynting's theorem, Eq. 2.7.16).

---

## 7.7 Optics from Electromagnetic Waves

### 7.7.1 Optics as applied electrodynamics

Optics is not a separate discipline. It is electrodynamics at wavelengths near $\lambda \sim 400$–$700$ nm, where the human visual system operates. Every optical phenomenon follows from the wave solutions of §7.2 and the boundary conditions of §7.4. This section derives the essential results, establishing the foundation that Vol 3 will extend to wave mechanics.

### 7.7.2 Geometric optics: the short-wavelength limit

When the wavelength is much smaller than the scale of obstacles and apertures, the wave nature of light can be approximated by *rays* — lines perpendicular to the wavefronts. This is the **eikonal approximation**.

Write the electric field as $\mathbf{E}(\mathbf{r}) = \mathbf{E}_0(\mathbf{r})e^{ik_0 S(\mathbf{r})}$, where $S(\mathbf{r})$ is the eikonal (phase function) and $k_0 = 2\pi/\lambda$ is the vacuum wavenumber. Substituting into the wave equation and keeping leading order in $k_0 \to \infty$ yields the **eikonal equation**:

$$|\nabla S|^2 = n^2(\mathbf{r}) \tag{2.7.67}$$

The rays are the curves $\mathbf{r}(s)$ satisfying $d\mathbf{r}/ds = \nabla S/n$, which obey:

$$\frac{d}{ds}\left(n\frac{d\mathbf{r}}{ds}\right) = \nabla n \tag{2.7.68}$$

This is the **ray equation** — the "equation of motion" for light rays in a medium with spatially varying index $n(\mathbf{r})$. In uniform media ($\nabla n = 0$), rays travel in straight lines. At interfaces where $n$ changes discontinuously, Snell's law (2.7.33) governs the ray direction.

### 7.7.3 Thin lens equation

For a thin lens with spherical surfaces of radii $R_1$ and $R_2$, applying Snell's law at each interface in the paraxial (small angle) approximation yields the **lensmaker's equation**:

$$\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right) \tag{2.7.69}$$

where $f$ is the focal length and $n$ is the lens index relative to the surrounding medium. The thin lens equation relating object distance $s$, image distance $s'$, and focal length is:

$$\boxed{\frac{1}{s} + \frac{1}{s'} = \frac{1}{f}} \tag{2.7.70}$$

This is entirely a consequence of Snell's law applied in the paraxial limit — and Snell's law was derived from Maxwell's equations (§7.4.2), which were derived from zone geometry (Ch 3).

### 7.7.4 Interference

When two coherent waves overlap, their fields add vectorially. The intensity (proportional to $|\mathbf{E}|^2$) shows interference fringes.

**Double-slit interference.** Two slits separated by distance $d$, illuminated by a plane wave of wavelength $\lambda$, produce an intensity pattern on a distant screen:

$$I(\theta) = I_0 \cos^2\left(\frac{\pi d \sin\theta}{\lambda}\right) \tag{2.7.71}$$

Bright fringes occur at $d\sin\theta = m\lambda$ ($m = 0, \pm 1, \pm 2, \ldots$).

### 7.7.5 Diffraction

When a wave passes through an aperture of width $a$, it spreads. The intensity pattern for a single slit is:

$$I(\theta) = I_0 \left[\frac{\sin(\pi a\sin\theta/\lambda)}{\pi a\sin\theta/\lambda}\right]^2 \tag{2.7.72}$$

The central maximum has angular half-width $\Delta\theta \approx \lambda/a$. This sets the fundamental **diffraction limit**: no optical system can resolve features smaller than about $\lambda/(2\text{NA})$, where NA is the numerical aperture. This limit is intrinsic to the wave nature of electromagnetic radiation — it is not a technological limitation but a consequence of the wave equation (2.7.5).

[FIGURE: Fig 2.7.13 — Interference and Diffraction Patterns]

### 7.7.6 Dispersion in media

In a material medium, the refractive index depends on frequency: $n(\omega)$. This *dispersion* causes different wavelengths to travel at different speeds, producing rainbow-like spectral separation and pulse broadening.

The origin of dispersion is the resonant response of bound electrons (or ions) in the medium. Near a resonance frequency $\omega_0$, the Lorentz oscillator model gives:

$$n^2(\omega) = 1 + \frac{Ne^2}{\varepsilon_0 m_e}\sum_j \frac{f_j}{\omega_j^2 - \omega^2 - i\gamma_j\omega} \tag{2.7.73}$$

where $f_j$ are oscillator strengths, $\omega_j$ are resonance frequencies, and $\gamma_j$ are damping constants.

In transparent regions (far from resonances), the Cauchy formula provides a practical approximation:

$$n(\lambda) \approx A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4} \tag{2.7.74}$$

with constants $A$, $B$, $C$ determined by the material.

The group velocity in a dispersive medium is:

$$v_g = \frac{c}{n + \omega \, dn/d\omega} \tag{2.7.75}$$

When $dn/d\omega > 0$ (normal dispersion), $v_g < c/n < c$. Near resonances, anomalous dispersion can occur where $v_g$ appears to exceed $c$ — but the signal velocity (which carries information) never does.

This establishes the optics and wave-propagation foundation that Vol 3 inherits for its treatment of wave mechanics. The wave equation (2.7.5), dispersion relation (2.7.8), boundary conditions (§7.4), and dispersion in media (2.7.73) are all passed forward as established results.

---

## 7.8 Electromagnetic Waves in Conducting Media

### 7.8.1 Maxwell's equations in a conductor

In a conducting medium with conductivity $\sigma$ (derived in §7.6.2), the current density $\mathbf{J} = \sigma\mathbf{E}$ modifies the wave equation. Starting from the full Ampère-Maxwell law:

$$\nabla \times \mathbf{B} = \mu_0\sigma\mathbf{E} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t} \tag{2.7.76}$$

For good conductors at frequencies below optical ($\sigma \gg \varepsilon_0\omega$), the conduction current dominates the displacement current. Taking the curl and following the same procedure as §7.2.1:

$$\nabla^2\mathbf{E} = \mu_0\sigma\frac{\partial\mathbf{E}}{\partial t} \tag{2.7.77}$$

This is a **diffusion equation**, not a wave equation. Electromagnetic fields in a good conductor do not propagate — they diffuse.

### 7.8.2 Skin depth

For a plane wave $\mathbf{E} = E_0 e^{i(kz - \omega t)}\hat{\mathbf{x}}$ entering a conductor, substituting into (2.7.77) gives a complex wavenumber:

$$k^2 = i\omega\mu_0\sigma \quad \Longrightarrow \quad k = (1+i)\sqrt{\frac{\omega\mu_0\sigma}{2}} = \frac{1+i}{\delta} \tag{2.7.78}$$

where the **skin depth** is:

$$\boxed{\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}}} \tag{2.7.79}$$

The field decays exponentially:

$$E(z) = E_0 \, e^{-z/\delta} \, e^{i(z/\delta - \omega t)} \tag{2.7.80}$$

[FIGURE: Fig 2.7.14 — Skin Depth and Faraday Cage]

The skin depth scales as $\delta \propto 1/\sqrt{f}$: higher frequencies penetrate less. For copper ($\sigma = 5.96 \times 10^7$ S/m):

| Frequency | Skin Depth | Regime |
|-----------|-----------|--------|
| 60 Hz | 8.5 mm | Power transmission — current uses full cross-section |
| 1 kHz | 2.1 mm | Audio frequencies |
| 1 MHz | 66 μm | Radio — surface current only |
| 1 GHz | 2.1 μm | Microwave — extreme surface confinement |

### 7.8.3 Faraday cage shielding

A conducting enclosure shields its interior from external electromagnetic fields. For static fields, the shielding is perfect: charges redistribute on the surface to cancel the interior field exactly.

For dynamic fields at frequency $\omega$, the shielding effectiveness depends on the ratio of wall thickness $t$ to skin depth $\delta$:

$$\text{SE} = 20\log_{10}\left(e^{t/\delta}\right) \approx 8.68\frac{t}{\delta} \text{ dB} \tag{2.7.81}$$

A 1 mm copper wall provides:
- At 60 Hz: 1.0 dB (poor — skin depth exceeds thickness)
- At 1 MHz: 132 dB (excellent — thousands of skin depths)
- At 1 GHz: 4200+ dB (impenetrable)

The attenuation is exponential in $t/\delta$ — the same exponential mechanism that makes confinement absolute in the strong force (Ch 4). In both cases, geometry (here the conducting boundary; there the $\mathbb{Z}_3$ orbifold) creates a barrier that fields cannot cross.

### 7.8.4 Practical applications

The skin effect and Faraday cage shielding have immediate engineering consequences derived entirely from Maxwell's equations:

**Power transmission:** At 50/60 Hz, the skin depth in copper is $\sim$9 mm. Solid conductors are effective. For large currents, hollow conductors or bundled cables save material without losing conductivity.

**Radio-frequency design:** At MHz frequencies, skin depth drops to tens of micrometers. Only the surface carries current, so thin plating (silver or gold over copper) is as effective as solid metal. Coaxial cables need only a thin outer conductor for shielding.

**Microwave shielding:** Mesh with aperture spacing $\ll \delta$ blocks microwave fields. This is why the window of a microwave oven has a metal mesh with $\sim$1 mm holes — the holes are far smaller than the $\sim$12 cm microwave wavelength and much smaller than the skin depth at 2.45 GHz.

---

## 7.9 Summary and the Classical Electrodynamics Landscape

### 7.9.1 What we have derived

This chapter, combined with Chapter 3, constitutes a complete derivation of classical electrodynamics from zone architecture. Let us survey what has been established:

| Domain | Key Results | Zone Architecture Origin |
|--------|-----------|------------------------|
| **Wave propagation** | Wave equation (2.7.5), dispersion $\omega = c|\mathbf{k}|$ (2.7.8), polarization, energy transport (2.7.16) | Maxwell Eqs (Ch 3) → curl coupling → wave equation; $c^2 = \sigma/\mu$ from Firmament (1.5.36) |
| **Radiation** | Retarded potentials (2.7.22–23), Larmor formula (2.7.26), dipole pattern | Lorenz gauge wave eq → Green's function → retarded solution; causality from Degradation Principle |
| **Boundary phenomena** | 4 boundary conditions (2.7.28–31), Snell's law (2.7.33), Fresnel equations (2.7.34–35), total internal reflection (2.7.37) | Maxwell Eqs integrated across interface; tangential continuity from Faraday, normal from Gauss |
| **Waveguides** | TE/TM modes (2.7.40–42), cutoff frequencies (2.7.43), massive dispersion (2.7.45) | Wave eq + conducting BCs → transverse quantization; same mechanism as Vol 1 Ch 10 |
| **Circuits** | Ohm (2.7.51), Kirchhoff (2.7.52, 54), C (2.7.57), L (2.7.60), LC/RLC (2.7.63–66) | Quasi-static limit of Maxwell; KCL = charge conservation (Noether/U(1)); KVL = conservative E-field |
| **Optics** | Geometric optics (2.7.67–68), thin lens (2.7.70), interference (2.7.71), diffraction (2.7.72), dispersion (2.7.73) | Short-wavelength limit of wave eq; wave superposition; material response to zone-derived fields |
| **Conducting media** | Skin depth (2.7.79), Faraday cage (2.7.81) | Maxwell + J = σE → diffusion eq; exponential decay from complex k |

Every entry in the right column traces back to Chapter 3's derivation of Maxwell's equations from 6D zone geometry, supplemented by the Lagrangian formalism of Chapter 5 and the gauge theory of Chapter 6. No additional postulates were introduced.

### 7.9.2 Comparison with standard treatment

A standard electrodynamics course (at the level of Jackson or Griffiths) covers the same material — but *postulates* Maxwell's equations and treats $\varepsilon_0$, $\mu_0$, $c$, and gauge invariance as empirical inputs. In zone architecture:

- Maxwell's equations are *derived* from 6D geometry (Ch 3)
- $\varepsilon_0$ and $\mu_0$ are *calculated* from warp-factor integrals (Ch 3)
- $c$ is the Firmament's wave speed (Vol 1, Ch 5)
- Gauge invariance is coordinate freedom (Ch 3, Eq. 2.3.9)
- The fine structure constant has geometric origin (Ch 3, Eqs. 2.3.69–82)

The *applications* derived in this chapter are identical to those in standard electrodynamics — they must be, since they follow from the same Maxwell equations. The difference is foundational: the student knows *why* these equations hold, rather than accepting them on empirical authority.

### 7.9.3 What Vol 3 inherits

Volume 3 (Matter and Motion) will use the following results from this chapter:

1. **Wave equation and dispersion** (§7.2): Foundation for wave mechanics and quantum wave equations
2. **Optics** (§7.7): Geometric optics as the classical limit of quantum mechanics (Hamilton-Jacobi ↔ eikonal)
3. **Dispersion in media** (§7.7.6): Material response framework extended to quantum oscillators
4. **Poynting's theorem** (§7.2.4): Energy conservation framework for matter-field interactions
5. **Boundary conditions** (§7.4): Quantum boundary-value problems follow the same mathematical structure

### 7.9.4 Open questions

Two areas remain incomplete at the classical level:

**Radiation reaction.** The Abraham-Lorentz force (§7.3.4) involves third-order time derivatives and admits pathological solutions. This is a well-known difficulty in classical electrodynamics that is resolved only in quantum electrodynamics (Vol 4). We note this honestly as an intrinsic limitation of classical field theory, not a gap in zone architecture.

**Nonlinear electrodynamics.** At very high field strengths (approaching the Schwinger limit $E_c = m_e^2 c^3/(e\hbar) \approx 1.3 \times 10^{18}$ V/m), quantum pair-production effects modify Maxwell's equations. These are quantum corrections to the classical theory and will be treated in Vol 4.

Both open questions are resolved by the same mechanism: quantization of the electromagnetic field on the zone manifold. The classical treatment given here is the complete and correct low-energy limit.

---

## Problems

### Computational

**Problem 7.1.** A plane electromagnetic wave in vacuum has electric field amplitude $E_0 = 100$ V/m. Calculate: (a) the magnetic field amplitude, (b) the time-averaged Poynting vector magnitude, and (c) the radiation pressure on a perfectly reflecting surface. Express all intermediate steps using zone-derived constants.

**Problem 7.2.** Calculate the Fresnel reflection coefficients $r_s$ and $r_p$ for light passing from air ($n_1 = 1.00$) to glass ($n_2 = 1.52$) at angles of incidence $\theta = 0°, 30°, 56.3°$ (Brewster), and $80°$. Verify that $|r_s|^2 + |t_s|^2(n_2\cos\theta_t)/(n_1\cos\theta_i) = 1$ (energy conservation) at each angle.

**Problem 7.3.** A rectangular waveguide has dimensions $a = 2.286$ cm and $b = 1.016$ cm (standard WR-90). (a) Calculate the cutoff frequencies for the first five modes. (b) Determine the frequency range for single-mode (TE$_{10}$) operation. (c) At $f = 10$ GHz, calculate the phase velocity, group velocity, and guide wavelength.

**Problem 7.4.** Calculate the skin depth in copper ($\sigma = 5.96 \times 10^7$ S/m) at frequencies of 60 Hz, 1 kHz, 1 MHz, and 1 GHz. For each, determine the shielding effectiveness of a 0.5 mm copper sheet.

**Problem 7.5.** An oscillating electric dipole with $|\mathbf{p}_0| = 10^{-29}$ C·m radiates at $f = 5 \times 10^{14}$ Hz (visible light). Calculate: (a) the total radiated power using Eq. (2.7.27), (b) the radiation resistance $R_\text{rad} = P/I_0^2$, and (c) the electric field amplitude at distance $r = 1$ m along the equatorial plane.

**Problem 7.6.** Design an RLC circuit to resonate at $f_0 = 1$ MHz with quality factor $Q = 100$. Given $C = 100$ pF, determine $L$ and $R$. Calculate the bandwidth and the current amplitude at resonance for a driving voltage of 1 V.

**Problem 7.7.** Calculate the critical angle for total internal reflection at a glass-air interface ($n_\text{glass} = 1.50$). For an optical fiber with core index $n_\text{core} = 1.48$ and cladding index $n_\text{clad} = 1.46$, calculate the V-number at $\lambda = 1550$ nm for a core radius of $a = 4.1$ μm. Is this single-mode?

**Problem 7.8.** A radio transmitter operates at 100 MHz with antenna current amplitude $I_0 = 5$ A. Model the antenna as a short dipole of length $\ell = 1$ m. Calculate the radiated power, the radiation resistance, and the electric field strength at distance $r = 10$ km along the equatorial plane.

### Conceptual

**Problem 7.9.** Explain why electromagnetic waves in vacuum have exactly two polarization states. Connect your answer to (a) the dimensionality of the Firmament membrane and (b) the transversality condition from Gauss's law.

**Problem 7.10.** A waveguide has a cutoff frequency — below it, waves cannot propagate. But vacuum has no cutoff frequency. What is fundamentally different about the two situations? Connect your answer to boundary-condition quantization (Vol 1, Ch 10).

**Problem 7.11.** Kirchhoff's current law says $\sum I = 0$ at a node. Derive this from (a) the continuity equation and (b) the Noether current for $U(1)$ gauge symmetry. Show that KCL is gauge symmetry in a practical disguise.

**Problem 7.12.** Why is the retarded potential the physical solution rather than the advanced potential? Your answer should reference (a) the Degradation Principle from Vol 1, Ch 8, and (b) the thermodynamic arrow of time.

**Problem 7.13.** At Brewster's angle, reflected light is perfectly polarized. Explain why this occurs from the boundary conditions (§7.4), and discuss why the phenomenon depends on polarization direction relative to the plane of incidence.

**Problem 7.14.** Explain why the Poynting vector $\mathbf{S} = (1/\mu_0)\mathbf{E} \times \mathbf{B}$ points in the direction of energy flow. Connect this to (a) the direction of wave propagation and (b) the Noether current for time-translation symmetry.

### Challenge

**Problem 7.15.** Derive the guided modes of a cylindrical waveguide of radius $a$ with perfectly conducting walls. Show that the transverse wave equation in cylindrical coordinates yields Bessel functions, write the characteristic equation for TE and TM modes, and calculate the first three cutoff frequencies in terms of Bessel zeros.

**Problem 7.16.** Derive the complete angular distribution of radiation from an oscillating electric dipole: electric field, magnetic field, Poynting vector, and differential power $dP/d\Omega$ as functions of angle $\theta$. Integrate to recover the Larmor formula (2.7.26). Show that the radiation pattern has $\sin^2\theta$ dependence and explain the physical reason.

**Problem 7.17.** Design a Faraday cage to attenuate a 900 MHz cellular signal by at least 60 dB using copper sheet. (a) Calculate the required thickness. (b) The cage has ventilation holes of diameter 5 mm; explain why these do not compromise shielding at 900 MHz. (c) At what frequency would 5 mm holes begin to leak significantly?

**Problem 7.18.** Starting from the wave equation (2.7.5) and the eikonal ansatz, derive the thin-film interference condition for a film of thickness $d$ and index $n$ in air. Show that constructive interference occurs at $2nd = (m + 1/2)\lambda$ for light reflected from the film. Explain the factor of $1/2$ in terms of the phase shift at reflection (connecting to the Fresnel equations of §7.4.3).

---

*This chapter has shown that the four Maxwell equations derived in Chapter 3 from the zone manifold are sufficient to produce all of classical electrodynamics. From radiation to circuits, from waveguides to optics, every result traces back to the Firmament membrane. In Chapter 8, we turn to the other geometric force — gravity — and develop the full gravitational field theory that seeds Volume 5's treatment of general relativity and cosmology.*

---

## Selected Solutions

**Solution 7.1.** (a) $B_0 = E_0/c = 100/(3.00 \times 10^8) = 3.33 \times 10^{-7}$ T. (b) $\langle S \rangle = E_0^2/(2\mu_0 c) = (100)^2/(2 \times 1.257 \times 10^{-6} \times 3.00 \times 10^8) = 13.3$ W/m². (c) For perfect reflection: $p = 2\langle S \rangle/c = 2(13.3)/(3.00 \times 10^8) = 8.85 \times 10^{-8}$ Pa.

**Solution 7.2.** At normal incidence ($\theta = 0°$): $r_s = r_p = (1.00 - 1.52)/(1.00 + 1.52) = -0.206$. Reflectance $R = 0.0426 = 4.3\%$. At Brewster's angle ($\theta_B = 56.3°$): $r_p = 0$ exactly; $r_s = -0.385$, giving $R_s = 14.8\%$. Energy conservation check at $30°$: $\theta_t = \arcsin(1.00 \times \sin 30°/1.52) = 19.2°$; $r_s = (1.00 \times 0.866 - 1.52 \times 0.944)/(1.00 \times 0.866 + 1.52 \times 0.944) = -0.240$; $t_s = 0.760$; $R_s = 0.0576$; $T_s = (0.760)^2 \times (1.52 \times 0.944)/(1.00 \times 0.866) = 0.578 \times 1.657 = 0.9424$; $R_s + T_s = 1.000$ ✓.

**Solution 7.3.** (a) Cutoff frequencies $f_{mn} = (c/2)\sqrt{(m/a)^2 + (n/b)^2}$. TE$_{10}$: $f_{10} = c/(2a) = 3.00 \times 10^8/(2 \times 0.02286) = 6.56$ GHz. TE$_{20}$: $13.12$ GHz. TE$_{01}$: $f_{01} = c/(2b) = 14.76$ GHz. TE$_{11}$ = TM$_{11}$: $\sqrt{f_{10}^2 + f_{01}^2} = 16.15$ GHz. TE$_{30}$: $19.68$ GHz. (b) Single-mode range: $6.56$ GHz $< f < 13.12$ GHz (TE$_{10}$ only). (c) At $f = 10$ GHz: $k_z = (2\pi f/c)\sqrt{1 - (f_{10}/f)^2} = (2\pi \times 10^{10}/3 \times 10^8)\sqrt{1 - 0.431} = 209.4 \times 0.754 = 157.9$ m$^{-1}$; $v_\text{ph} = 2\pi f/k_z = 3.98 \times 10^8$ m/s; $v_g = c^2/v_\text{ph} = 2.26 \times 10^8$ m/s; $\lambda_g = 2\pi/k_z = 3.98$ cm.

**Solution 7.4.** $\delta = \sqrt{2/(\omega\mu_0\sigma)}$. At 60 Hz: $\delta = \sqrt{2/(2\pi \times 60 \times 4\pi \times 10^{-7} \times 5.96 \times 10^7)} = 8.5$ mm. SE for 0.5 mm: $8.68 \times 0.5/8.5 = 0.51$ dB (poor). At 1 kHz: $\delta = 2.1$ mm; SE $= 2.1$ dB. At 1 MHz: $\delta = 66$ μm; SE $= 65.8$ dB (excellent). At 1 GHz: $\delta = 2.1$ μm; SE $= 2071$ dB (impenetrable).

**Solution 7.7.** Critical angle: $\theta_c = \arcsin(1/1.50) = 41.8°$. V-number: $V = (2\pi \times 4.1 \times 10^{-6}/1550 \times 10^{-9})\sqrt{1.48^2 - 1.46^2} = 16.61 \times \sqrt{0.0588} = 16.61 \times 0.2425 = 4.03$. Since $V = 4.03 > 2.405$, this fiber is *not* single-mode at 1550 nm — it supports approximately $V^2/2 \approx 8$ modes. For single-mode operation at 1550 nm, the core radius would need to be $a < 4.1 \times 2.405/4.03 = 2.45$ μm, or the index difference would need to be reduced.

**Solution 7.9.** (Conceptual) EM waves propagate on the 4D Firmament membrane embedded in 6D. A wave propagating in the $\hat{\mathbf{z}}$ direction on this membrane has its fields in the transverse plane. On the 4D Firmament, the spatial transverse plane perpendicular to $\hat{\mathbf{z}}$ is 2-dimensional (spanned by $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}}$). Gauss's law $\nabla \cdot \mathbf{E} = 0$ (Eq. 2.3.27, derived from 6D geometry) enforces transversality: $\mathbf{k} \cdot \mathbf{E}_0 = 0$ (Eq. 2.7.9). With $\mathbf{k}$ fixing one direction, two orthogonal directions remain — hence exactly two polarization states. In a hypothetical 5D membrane, there would be 3 polarization states; in 3D, only 1. The number 2 is a direct consequence of the Firmament's dimensionality.

**Solution 7.11.** (Conceptual) (a) From continuity: In steady state, $\partial\rho/\partial t = 0$, so $\nabla \cdot \mathbf{J} = 0$. Integrating over a volume enclosing the node and applying the divergence theorem: $\oint \mathbf{J} \cdot d\mathbf{A} = 0$, which is $\sum I_k = 0$. (b) From Noether: The zone Lagrangian (Eq. 2.5.1) has U(1) gauge symmetry (the $\xi$-direction isometry, Eqs. 2.6.2–2.6.5). By Noether's first theorem (Vol 1, Ch 7, Eq. 1.7.6), this symmetry generates a conserved current $j^\mu$ with $\partial_\mu j^\mu = 0$. The spatial integral of $j^0$ is the total charge, and $\partial_\mu j^\mu = 0$ in the steady state is the continuity equation. KCL is the practical manifestation of gauge symmetry: every time an engineer applies KCL to a circuit node, they are (unknowingly) invoking the $\xi$-direction isometry of the 6D zone manifold.

**Solution 7.12.** (Conceptual) The wave equation $\Box^2 \phi = -\rho/\varepsilon_0$ admits two Green's function solutions: the retarded one ($t_\text{ret} = t - r/c$, field depends on past sources) and the advanced one ($t_\text{adv} = t + r/c$, field depends on future sources). Both are mathematically valid. The physical solution is the retarded one because: (a) The Degradation Principle (Vol 1, Ch 8) establishes a thermodynamic arrow of time. Entropy increases; effects follow causes. The advanced solution would require effects to precede causes, violating the entropy gradient. (b) The retarded boundary condition corresponds to outgoing radiation — energy flows away from the source. The advanced boundary condition would require incoming radiation converging on the source from spatial infinity — a state of absurdly low entropy that the Degradation Principle forbids. The selection of retarded over advanced potentials is not an arbitrary choice but a consequence of the thermodynamic structure established in Vol 1.
