# Chapter 4: Rigid Body Dynamics

## Rotation from Zone Conservation Laws

---

> *"He has inscribed a circle on the face of the waters at the boundary between light and darkness."*
> — Job 26:10

---

## §4.1 — Why Rigid Bodies Rotate

In Volume 1, Chapter 7, we derived angular momentum conservation from the zone manifold's rotational symmetry. The argument was clean: the spatial isotropy of the zone manifold (no direction is privileged — "God does not show favoritism," Acts 10:34) produces three rotational Killing vectors (Eq. 1.7.31), Noether's theorem yields three conserved angular momentum components (Eq. 1.7.33), and the total angular momentum of any isolated system is constant.

In Chapter 3, we wielded this conservation law to powerful effect: it confined central force orbits to planes, reduced the Kepler problem to a single radial ODE, and explained why planetary orbits close. But every application so far has treated angular momentum as a property of *point particles* — objects with mass but no spatial extent.

Real objects are not points. A spinning figure skater, a tumbling asteroid, a precessing gyroscope — these are extended bodies whose rotation involves the coordinated motion of every constituent particle. The question is: **what does angular momentum conservation look like for an extended object?**

The answer is the subject of this chapter, and here is the derivation chain:

$$\boxed{\text{Zone rotational symmetry (1.7.31)} \to \text{Angular momentum conservation (1.7.33)} \to \text{Inertia tensor} \to \text{Euler's equations} \to \text{Precession, gyroscopes}}$$

[FIGURE: Fig 3.4.1 — From Zone Symmetry to Rigid Body Rotation. Flowchart: Zone manifold SO(3) symmetry (Vol 1 Ch 7, Eq. 1.7.31) → Noether's theorem → Angular momentum conservation (Eq. 1.7.33) → Applied to extended body → Inertia tensor $I_{ij}$ → Euler's equations → Torque-free precession / Heavy top / Gyroscopic stability. Color code: blue = Vol 1 results, orange = Vol 3 Ch 1–3 results, green = this chapter's new derivations.]

No new physics enters this chapter. Everything follows from the rotational symmetry that Vol 1 established and the variational machinery that Ch 2 built. What *is* new is the geometry — the rich interplay between a body's mass distribution and its rotational dynamics. A sphere, a cylinder, and a rod all obey the same conservation law, but they rotate very differently. The inertia tensor is why.

### Degrees of Freedom

A rigid body in three-dimensional space has six degrees of freedom: three for the position of its center of mass, and three for its orientation. We already know how to handle the center-of-mass motion — it obeys F=ma (Ch 1), and for an isolated system, the center of mass moves in a straight line at constant velocity (momentum conservation, Vol 1 Eq. 1.7.30). That leaves the three rotational degrees of freedom, which are the subject of this chapter.

The **rigid body constraint** is the statement that the distance between any two points in the body is fixed:

$$|\mathbf{r}_\alpha - \mathbf{r}_\beta| = d_{\alpha\beta} = \text{constant} \tag{3.4.1}$$

for all particle pairs $(\alpha, \beta)$. This is a *holonomic* constraint — it depends only on positions, not velocities — and it dramatically reduces the degrees of freedom. A system of $N$ unconstrained particles has $3N$ degrees of freedom. The rigid constraint fixes all relative positions, leaving only 6 independent parameters (3 for center of mass + 3 for orientation). The Lagrangian formalism (Ch 2) handles constraints by choosing generalized coordinates that automatically satisfy them, making the constraint forces invisible.

For the translational degrees of freedom, the natural generalized coordinates are the center-of-mass position $(X, Y, Z)$. For the rotational degrees of freedom, we need coordinates that parameterize the body's orientation. These are the **Euler angles**, which we will introduce in §4.4.

---

## §4.2 — Kinematics of Rotation

Before we can write down the Lagrangian for a rotating body, we need the mathematical description of rotation itself. This is kinematics — the geometry of motion without reference to forces.

### §4.2.1 — The Angular Velocity Vector

Consider a rigid body rotating about a fixed point (for now, its center of mass). At any instant, the velocity of a point at position $\mathbf{r}$ relative to the center of mass is:

$$\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r} \tag{3.4.2}$$

where $\boldsymbol{\omega}$ is the **angular velocity vector**. This is a kinematic identity for rigid body rotation — it follows purely from the rigid constraint (3.4.1) and the fact that the only motion preserving all inter-particle distances is rotation.

*Why must $\boldsymbol{\omega}$ exist?* The argument is Euler's rotation theorem: any displacement of a rigid body with one fixed point is equivalent to a single rotation about some axis through that fixed point. At any instant, the body is undergoing an infinitesimal rotation by angle $d\theta$ about an axis $\hat{n}$. The angular velocity is:

$$\boldsymbol{\omega} = \dot{\theta}\,\hat{n} \tag{3.4.3}$$

The direction of $\boldsymbol{\omega}$ is the instantaneous rotation axis; its magnitude $|\boldsymbol{\omega}|$ is the angular speed.

### §4.2.2 — Two Frames: Space and Body

We need two reference frames:

**The space frame** $(X, Y, Z)$: fixed in the laboratory, inertial. This is the frame where we derived angular momentum conservation (Vol 1 Ch 7). The conservation law $d\mathbf{L}/dt = \boldsymbol{\tau}$ holds in this frame.

**The body frame** $(x, y, z)$: fixed in the rigid body, rotating with it. In this frame, the body's mass distribution is static — the inertia tensor is constant. This is the natural frame for describing the body's geometry.

The relationship between the two frames is encoded in a **rotation matrix** $R(t) \in SO(3)$:

$$\mathbf{r}_{\text{space}} = R(t) \, \mathbf{r}_{\text{body}} \tag{3.4.4}$$

The angular velocity in the body frame is related to the angular velocity in the space frame by:

$$\boldsymbol{\omega}_{\text{body}} = R^T \boldsymbol{\omega}_{\text{space}} \tag{3.4.5}$$

A critical point: **the angular velocity components in the two frames are generally different.** For the space frame, $\boldsymbol{\omega}$ is a vector whose components change as the body rotates. For the body frame, $\boldsymbol{\omega}$ has components that describe the rotation as seen by an observer riding on the body. The body-frame description turns out to be more useful for the equations of motion, because the inertia tensor is constant in that frame.

### §4.2.3 — The Transport Theorem

The single most important equation in this chapter's development is the **transport theorem**, which relates time derivatives in the space and body frames:

$$\left(\frac{d\mathbf{A}}{dt}\right)_{\text{space}} = \left(\frac{d\mathbf{A}}{dt}\right)_{\text{body}} + \boldsymbol{\omega} \times \mathbf{A} \tag{3.4.6}$$

for any vector $\mathbf{A}$. The proof is one line: express $\mathbf{A} = A_i(t)\hat{e}_i(t)$ in the rotating basis, differentiate using the product rule, and note that $d\hat{e}_i/dt = \boldsymbol{\omega} \times \hat{e}_i$ (the basis vectors rotate with the body). The first term $\dot{A}_i\hat{e}_i$ is the body-frame derivative; the second $A_i(\boldsymbol{\omega}\times\hat{e}_i) = \boldsymbol{\omega}\times\mathbf{A}$ is the frame rotation contribution.

*Why is this needed?* Because angular momentum conservation $d\mathbf{L}/dt = \boldsymbol{\tau}$ holds in the space (inertial) frame, but the inertia tensor $I_{ij}$ is constant in the body frame. We must use the transport theorem to translate between them. This translation is the origin of Euler's equations.

---

## §4.3 — The Moment of Inertia Tensor

### §4.3.1 — Why a Tensor?

Here is a question worth pausing on: *Why is the "moment of inertia" a tensor — a $3 \times 3$ matrix — rather than a simple number?*

The answer lies in the kinetic energy. Chapter 2 showed that, for any system described by generalized coordinates, the kinetic energy takes the form (Eq. 3.2.4):

$$T = \frac{1}{2} M_{ij}(q) \, \dot{q}^i \dot{q}^j$$

where $M_{ij}$ is the **mass matrix** in generalized coordinates. For rotation, the generalized velocities are the three components of $\boldsymbol{\omega}$. The mass matrix for rotational motion IS the inertia tensor. Because rotation about different axes produces different kinetic energies (spinning a pencil about its length is easy; spinning it end-over-end is hard), the single "mass" of translational mechanics becomes a matrix for rotational mechanics. The tensor encodes the body's geometry.

### §4.3.2 — Derivation

Consider a rigid body as a collection of mass elements $dm$ at positions $\mathbf{r}$ relative to the center of mass. The velocity of each element is $\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$ (Eq. 3.4.2). The total rotational kinetic energy is:

$$T_{\text{rot}} = \frac{1}{2}\int |\mathbf{v}|^2 \, dm = \frac{1}{2}\int |\boldsymbol{\omega} \times \mathbf{r}|^2 \, dm \tag{3.4.7}$$

Expanding the cross product using the vector identity $|\mathbf{A} \times \mathbf{B}|^2 = |\mathbf{A}|^2|\mathbf{B}|^2 - (\mathbf{A} \cdot \mathbf{B})^2$:

$$T_{\text{rot}} = \frac{1}{2}\int \left[\omega^2 r^2 - (\boldsymbol{\omega} \cdot \mathbf{r})^2\right] dm$$

Writing this in component form ($\omega_i$ are the components of $\boldsymbol{\omega}$, $r_i$ are the components of $\mathbf{r}$):

$$T_{\text{rot}} = \frac{1}{2}\int \left[\omega_i \omega_i \, r_j r_j - \omega_i r_i \, \omega_j r_j\right] dm = \frac{1}{2}\omega_i \omega_j \int \left[r^2 \delta_{ij} - r_i r_j\right] dm$$

This gives us:

$$\boxed{T_{\text{rot}} = \frac{1}{2} \omega_i \, I_{ij} \, \omega_j = \frac{1}{2}\boldsymbol{\omega} \cdot \mathbf{I} \cdot \boldsymbol{\omega}} \tag{3.4.8}$$

where the **moment of inertia tensor** is:

$$\boxed{I_{ij} = \int \left(r^2 \delta_{ij} - r_i r_j\right) dm} \tag{3.4.9}$$

In matrix form, with $\mathbf{r} = (x, y, z)$:

$$\mathbf{I} = \int \begin{pmatrix} y^2 + z^2 & -xy & -xz \\ -xy & x^2 + z^2 & -yz \\ -xz & -yz & x^2 + y^2 \end{pmatrix} dm \tag{3.4.10}$$

The diagonal elements $I_{xx} = \int(y^2 + z^2)\,dm$, etc., are the **moments of inertia** about the coordinate axes. The off-diagonal elements $I_{xy} = -\int xy\,dm$, etc., are the **products of inertia**. Both depend on the choice of body-fixed axes.

Notice the structure: this is precisely the mass matrix $M_{ij}(q)$ of Eq. 3.2.4, specialized to rotational coordinates. The derivation traces directly back to the zone manifold's metric structure, which determines the kinetic energy as the squared length of the velocity vector.

### §4.3.3 — Angular Momentum of a Rigid Body

The angular momentum of the rigid body is:

$$L_i = \int (\mathbf{r} \times \mathbf{v})_i \, dm = \int (\mathbf{r} \times (\boldsymbol{\omega} \times \mathbf{r}))_i \, dm$$

Using the BAC-CAB identity $\mathbf{r} \times (\boldsymbol{\omega} \times \mathbf{r}) = \boldsymbol{\omega}\,r^2 - \mathbf{r}(\mathbf{r} \cdot \boldsymbol{\omega})$:

$$\boxed{L_i = I_{ij}\,\omega_j} \tag{3.4.11}$$

This is the rigid body's angular momentum, expressed as a matrix equation: **angular momentum equals the inertia tensor acting on angular velocity.** Compare with the point particle case $L = \mu r^2 \dot{\phi}$ from Ch 3 (Eq. 3.3.4b) — there, a single moment of inertia $\mu r^2$ sufficed because the motion was planar. For a general rigid body rotating in three dimensions, the full tensor is needed.

A crucial observation: **$\mathbf{L}$ and $\boldsymbol{\omega}$ are generally NOT parallel.** They point in the same direction only when $\boldsymbol{\omega}$ is aligned with a principal axis of the inertia tensor. This misalignment between angular momentum and angular velocity is the source of precession and nutation — phenomena that have no analog in point-particle mechanics.

### §4.3.4 — Principal Axes and Principal Moments

The inertia tensor $I_{ij}$ is a real, symmetric matrix (the symmetry is manifest in Eq. 3.4.10). By the **spectral theorem** of linear algebra, any real symmetric matrix can be diagonalized by an orthogonal transformation:

$$R^T \mathbf{I} R = \begin{pmatrix} I_1 & 0 & 0 \\ 0 & I_2 & 0 \\ 0 & 0 & I_3 \end{pmatrix} \tag{3.4.12}$$

where $R$ is an orthogonal matrix (a rotation) and $I_1, I_2, I_3$ are the **principal moments of inertia** — the eigenvalues of $\mathbf{I}$. The columns of $R$ are the **principal axes** — the eigenvectors of $\mathbf{I}$.

*Why does this matter physically?* When the body-frame axes are aligned with the principal axes, the inertia tensor is diagonal, and:

$$L_1 = I_1\omega_1, \qquad L_2 = I_2\omega_2, \qquad L_3 = I_3\omega_3 \tag{3.4.13}$$

Angular momentum is parallel to angular velocity along each principal axis. If the body spins about a principal axis ($\omega_2 = \omega_3 = 0$, say), then $\mathbf{L} = I_1\omega_1\hat{e}_1$ is parallel to $\boldsymbol{\omega}$. The motion is pure rotation, with no tendency to precess.

For the remainder of this chapter, we choose the body frame to coincide with the principal axes. This is always possible and always simplifies the equations.

### §4.3.5 — The Parallel Axis Theorem

If we know the inertia tensor about the center of mass, we can find it about any other point using the **parallel axis theorem**:

$$I_{ij}^{(P)} = I_{ij}^{(\text{cm})} + M(d^2 \delta_{ij} - d_i d_j) \tag{3.4.14}$$

where $M$ is the total mass and $\mathbf{d}$ is the displacement from the center of mass to point $P$. For a single axis:

$$I_P = I_{\text{cm}} + Md^2 \tag{3.4.15}$$

The proof is a direct consequence of the definition (3.4.9) and the center-of-mass condition $\int \mathbf{r}\,dm = 0$ when measured from the center of mass.

### §4.3.6 — Worked Examples

**Uniform sphere** (mass $M$, radius $R$): By symmetry, all three principal moments are equal:

$$I_1 = I_2 = I_3 = \frac{2}{5}MR^2 \tag{3.4.16}$$

The inertia tensor is proportional to the identity matrix: $\mathbf{I} = \frac{2}{5}MR^2\,\mathbf{1}$. A sphere's angular momentum is always parallel to its angular velocity. This is the rotational analog of isotropy — and it traces to the zone manifold's spatial isotropy (Vol 1 Ch 3). A sphere inherits the full SO(3) symmetry of the underlying space.

**Uniform thin rod** (mass $M$, length $\ell$, about center): With the rod along the $z$-axis:

$$I_1 = I_2 = \frac{1}{12}M\ell^2, \qquad I_3 = 0 \tag{3.4.17}$$

(The $I_3 = 0$ is an idealization for a truly one-dimensional rod; a real rod has finite width and $I_3 \neq 0$ but small.)

**Uniform cylinder** (mass $M$, radius $R$, height $h$, about symmetry axis):

$$I_3 = \frac{1}{2}MR^2, \qquad I_1 = I_2 = \frac{1}{12}M(3R^2 + h^2) \tag{3.4.18}$$

A cylinder with $I_1 = I_2 \neq I_3$ is called a **symmetric top** — the most tractable nontrivial case of rigid body dynamics.

[FIGURE: Fig 3.4.2 — The Inertia Tensor as Geometric Object. Three panels: (a) uniform sphere with $I_1 = I_2 = I_3$ — ellipsoid of inertia is a sphere; (b) cylinder with $I_1 = I_2 \neq I_3$ — ellipsoid is oblate or prolate depending on aspect ratio; (c) general asymmetric body with $I_1 \neq I_2 \neq I_3$ — ellipsoid has three distinct axes. Principal axes labeled. Caption: "The ellipsoid of inertia $I_{ij}n_in_j = 1$ visualizes the tensor. Its shape determines the body's rotational character: sphere (equal moments), symmetric top (two equal), or asymmetric top (all different)."]

---

## §4.4 — Euler Angles and the Rotational Lagrangian

### §4.4.1 — Why Euler Angles?

The orientation of a rigid body in 3D space requires three parameters. There are many ways to parameterize SO(3) — rotation matrices (9 parameters with 6 constraints), quaternions (4 parameters with 1 constraint), axis-angle (3 parameters with a coordinate singularity). The classical choice is **Euler angles** $(\phi, \theta, \psi)$, which have a direct physical interpretation and connect naturally to the Lagrangian formalism.

The Euler angles define a sequence of three rotations that carry the space frame $(X, Y, Z)$ into the body frame $(x, y, z)$:

1. **Rotation by $\phi$** about the $Z$-axis (the space-frame vertical). This defines the "line of nodes" $N$ — the intersection of the $XY$-plane and the body's $xy$-plane.
2. **Rotation by $\theta$** about the line of nodes $N$. This tilts the body frame relative to the vertical by the "nutation angle" $\theta$.
3. **Rotation by $\psi$** about the body-frame $z$-axis. This is the "spin" of the body about its own symmetry axis.

[FIGURE: Fig 3.4.3 — Euler Angles. A 3D diagram showing the space frame $(X,Y,Z)$ and body frame $(x,y,z)$ with the three Euler rotations labeled. The line of nodes $N$ is the intersection of the $XY$-plane and the body's equatorial plane. Angles: $\phi$ (precession, around $Z$), $\theta$ (nutation, around $N$), $\psi$ (spin, around body $z$). Caption: "The three Euler angles decompose an arbitrary orientation into three sequential rotations. Each angle has a physical name: $\phi$ is precession, $\theta$ is nutation, $\psi$ is spin."]

### §4.4.2 — Angular Velocity in Terms of Euler Angles

The total angular velocity is the sum of the three rotation rates:

$$\boldsymbol{\omega} = \dot{\phi}\,\hat{Z} + \dot{\theta}\,\hat{N} + \dot{\psi}\,\hat{z} \tag{3.4.19}$$

where $\hat{Z}$ is the space-frame vertical, $\hat{N}$ is along the line of nodes, and $\hat{z}$ is the body-frame symmetry axis. To express this in body-frame components, we project each term:

$$\omega_1 = \dot{\phi}\sin\theta\sin\psi + \dot{\theta}\cos\psi \tag{3.4.20a}$$
$$\omega_2 = \dot{\phi}\sin\theta\cos\psi - \dot{\theta}\sin\psi \tag{3.4.20b}$$
$$\omega_3 = \dot{\phi}\cos\theta + \dot{\psi} \tag{3.4.20c}$$

These are the kinematic equations relating Euler angle rates to body-frame angular velocity components. They are purely geometric — no physics has entered yet.

### §4.4.3 — The Rotational Lagrangian

With the inertia tensor diagonal in the body frame (Eq. 3.4.12), the rotational kinetic energy (Eq. 3.4.8) becomes:

$$T_{\text{rot}} = \frac{1}{2}(I_1\omega_1^2 + I_2\omega_2^2 + I_3\omega_3^2) \tag{3.4.21}$$

For a **symmetric top** ($I_1 = I_2 \equiv I$), substituting the Euler angle expressions (3.4.20):

$$\omega_1^2 + \omega_2^2 = \dot{\theta}^2 + \dot{\phi}^2\sin^2\theta \tag{3.4.22}$$

(the $\psi$-dependent terms cancel due to $\sin^2\psi + \cos^2\psi = 1$). Therefore:

$$\boxed{T_{\text{rot}} = \frac{1}{2}I(\dot{\theta}^2 + \dot{\phi}^2\sin^2\theta) + \frac{1}{2}I_3(\dot{\phi}\cos\theta + \dot{\psi})^2} \tag{3.4.23}$$

This is the rotational Lagrangian for a symmetric top in Euler angles. Notice its structure: it is a quadratic form in the generalized velocities $(\dot{\phi}, \dot{\theta}, \dot{\psi})$, exactly as the general theory (Ch 2, Eq. 3.2.4) requires. The mass matrix is:

$$M_{ij} = \begin{pmatrix} I\sin^2\theta + I_3\cos^2\theta & 0 & I_3\cos\theta \\ 0 & I & 0 \\ I_3\cos\theta & 0 & I_3 \end{pmatrix} \tag{3.4.24}$$

### §4.4.4 — Canonical Momenta and Conserved Quantities

The canonical momenta (Ch 2, §2.4.2) are:

$$p_\phi = \frac{\partial T_{\text{rot}}}{\partial\dot{\phi}} = (I\sin^2\theta + I_3\cos^2\theta)\dot{\phi} + I_3\dot{\psi}\cos\theta \tag{3.4.25a}$$

$$p_\theta = \frac{\partial T_{\text{rot}}}{\partial\dot{\theta}} = I\dot{\theta} \tag{3.4.25b}$$

$$p_\psi = \frac{\partial T_{\text{rot}}}{\partial\dot{\psi}} = I_3(\dot{\phi}\cos\theta + \dot{\psi}) = I_3\omega_3 \tag{3.4.25c}$$

For a torque-free symmetric top, $T_\text{rot}$ is the entire Lagrangian ($V = 0$). Both $\phi$ and $\psi$ are **cyclic coordinates** — the Lagrangian does not depend on them explicitly. By Noether's theorem (Ch 2, Eq. 3.2.19):

$$p_\phi = \text{const.} = L_Z \qquad \text{(angular momentum about space } Z\text{-axis)} \tag{3.4.26}$$
$$p_\psi = \text{const.} = L_3 \equiv I_3\omega_3 \qquad \text{(spin angular momentum about body } z\text{-axis)} \tag{3.4.27}$$

These two conserved quantities, together with energy conservation ($T_{\text{rot}} = E = \text{const}$), completely determine the motion. Three constants of motion for three degrees of freedom — the system is integrable.

The physical meaning of these conserved momenta connects directly back to Vol 1 Ch 7. The momentum $p_\phi = L_Z$ is the component of angular momentum along the space-frame vertical — conserved because the torque-free Lagrangian is invariant under rotations about $Z$ (a manifestation of the zone manifold's rotational symmetry). The momentum $p_\psi = L_3 = I_3\omega_3$ is the spin angular momentum — conserved because the symmetric top's Lagrangian is invariant under rotations about its own symmetry axis.

---

## §4.5 — Euler's Equations of Motion

### §4.5.1 — Derivation from Angular Momentum Conservation

The master equation of rotational dynamics is the angular momentum equation in the space frame:

$$\left(\frac{d\mathbf{L}}{dt}\right)_{\text{space}} = \boldsymbol{\tau} \tag{3.4.28}$$

This is not a new axiom — it is $d\mathbf{L}/dt = \boldsymbol{\tau}$, which follows from the zone manifold's conservation law (Vol 1, Eq. 1.7.33) generalized to include external torques. For an isolated system, $\boldsymbol{\tau} = 0$ and angular momentum is exactly conserved. When external forces produce a torque, angular momentum changes at a rate equal to the applied torque — the rotational analog of $\mathbf{F} = m\mathbf{a}$ (Ch 1, Eq. 3.1.10).

Now we translate this to the body frame using the transport theorem (Eq. 3.4.6):

$$\left(\frac{d\mathbf{L}}{dt}\right)_{\text{space}} = \left(\frac{d\mathbf{L}}{dt}\right)_{\text{body}} + \boldsymbol{\omega} \times \mathbf{L} = \boldsymbol{\tau}$$

In the body frame, with principal axes as coordinates, $L_i = I_i\omega_i$ (no sum), so:

$$\left(\frac{dL_i}{dt}\right)_{\text{body}} = I_i\dot{\omega}_i$$

(Here we use the crucial fact that $I_i$ is constant in the body frame — the body's shape does not change as seen from within.)

Writing out the cross product $\boldsymbol{\omega} \times \mathbf{L}$ component by component:

$$(\boldsymbol{\omega} \times \mathbf{L})_1 = \omega_2 L_3 - \omega_3 L_2 = \omega_2 I_3\omega_3 - \omega_3 I_2\omega_2 = (I_3 - I_2)\omega_2\omega_3$$

Combining:

$$\boxed{\begin{aligned}
I_1\dot{\omega}_1 + (I_3 - I_2)\omega_2\omega_3 &= \tau_1 \\
I_2\dot{\omega}_2 + (I_1 - I_3)\omega_3\omega_1 &= \tau_2 \\
I_3\dot{\omega}_3 + (I_2 - I_1)\omega_1\omega_2 &= \tau_3
\end{aligned}} \tag{3.4.29}$$

These are **Euler's equations of rigid body motion**. They govern the time evolution of the angular velocity components in the body frame, subject to whatever external torque $\boldsymbol{\tau}$ is applied.

### §4.5.2 — Why the Nonlinear Terms?

Notice the nonlinear terms $(I_3 - I_2)\omega_2\omega_3$ and its cyclic permutations. These are NOT forces. They are purely geometric — they arise from the transport theorem's $\boldsymbol{\omega} \times \mathbf{L}$ term, which accounts for the fact that the body frame is rotating. If you measured angular momentum from within the rotating body, you would see it changing (precessing) even when no torque is applied, simply because your coordinate axes are spinning.

This is the rotational analog of the Coriolis and centrifugal "forces" that appear in rotating reference frames. They are not real forces — they are artifacts of the rotating frame. But they have real consequences: they cause the angular velocity vector to precess in the body frame, producing the tumbling motions we observe.

### §4.5.3 — Torque-Free Motion: The Symmetric Top

Set $\boldsymbol{\tau} = 0$ and $I_1 = I_2 \equiv I$ (symmetric top). Euler's equations become:

$$I\dot{\omega}_1 + (I_3 - I)\omega_2\omega_3 = 0 \tag{3.4.30a}$$
$$I\dot{\omega}_2 + (I - I_3)\omega_3\omega_1 = 0 \tag{3.4.30b}$$
$$I_3\dot{\omega}_3 = 0 \tag{3.4.30c}$$

From (3.4.30c): $\omega_3 = \text{const}$. The spin about the symmetry axis is constant — as it must be, since $p_\psi = I_3\omega_3$ is conserved (Eq. 3.4.27).

Define the **body-frame precession rate**:

$$\Omega_{\text{body}} = \frac{I_3 - I}{I}\omega_3 \tag{3.4.31}$$

Then equations (3.4.30a,b) become:

$$\dot{\omega}_1 = -\Omega_{\text{body}}\omega_2, \qquad \dot{\omega}_2 = \Omega_{\text{body}}\omega_1 \tag{3.4.32}$$

The solution is:

$$\omega_1(t) = \omega_\perp\cos(\Omega_{\text{body}} t + \alpha), \qquad \omega_2(t) = \omega_\perp\sin(\Omega_{\text{body}} t + \alpha) \tag{3.4.33}$$

where $\omega_\perp = \sqrt{\omega_1^2(0) + \omega_2^2(0)}$ is the magnitude of the angular velocity component perpendicular to the symmetry axis.

**Physical interpretation.** The angular velocity vector $\boldsymbol{\omega}$ traces a circle around the symmetry axis in the body frame. As seen from the space frame, $\boldsymbol{\omega}$ traces a cone around the fixed angular momentum vector $\mathbf{L}$. The body's symmetry axis also traces a cone around $\mathbf{L}$. These are the **body cone** and **space cone**, and their relationship is the key to visualizing torque-free precession.

[FIGURE: Fig 3.4.4 — Torque-Free Precession. Left panel: body frame view — $\boldsymbol{\omega}$ traces a circle around the body's symmetry axis $\hat{e}_3$. Right panel: space frame view — both $\boldsymbol{\omega}$ and $\hat{e}_3$ trace cones around the fixed $\mathbf{L}$ vector. The body cone rolls on the space cone (or inside it, depending on whether $I_3 > I$ or $I_3 < I$). Labels: $\mathbf{L}$ (fixed in space), $\boldsymbol{\omega}$ (instantaneous rotation axis), $\hat{e}_3$ (body symmetry axis), body cone, space cone.]

For an oblate body ($I_3 > I$, like Earth), $\Omega_\text{body}$ has the same sign as $\omega_3$: the body cone rolls *outside* the space cone, and the symmetry axis precesses in the same sense as the spin. For a prolate body ($I_3 < I$, like a football), $\Omega_\text{body}$ has the opposite sign: the body cone rolls *inside* the space cone, and precession is retrograde.

**Earth's Chandler wobble.** The Earth is an oblate symmetric top with $I_3/I \approx 1.00327$. A small misalignment between the rotation axis and the symmetry axis produces a predicted precession period of:

$$T_\text{Euler} = \frac{2\pi}{\Omega_\text{body}} = \frac{2\pi}{(I_3/I - 1)\omega_3} \approx \frac{1}{0.00327} \text{ day} \approx 306 \text{ days} \tag{3.4.34}$$

The observed "Chandler wobble" has a period of about 433 days — the difference is due to Earth's elasticity, which standard rigid body theory does not account for. This discrepancy is an honest limit of the rigid body approximation, and it points toward the continuum mechanics of Chapter 5.

---

## §4.6 — The Heavy Symmetric Top: Precession and Nutation

### §4.6.1 — Why Tops Don't Fall

Here is the question every child asks when watching a spinning top: **Why doesn't it fall over?**

It should fall. Gravity pulls its center of mass downward, creating a torque that should rotate the top toward the horizontal. And yet, as long as the top spins fast enough, it doesn't fall — it *precesses*, tracing a slow circle around the vertical.

The answer is a direct consequence of angular momentum's vector nature:

$$\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt} \tag{3.4.28}$$

Torque does not change the magnitude of $\mathbf{L}$; it changes its *direction*. The gravitational torque on a top with its center of mass at distance $l$ from the pivot is:

$$\boldsymbol{\tau} = Mgl\sin\theta\,\hat{\phi} \tag{3.4.35}$$

where $\theta$ is the angle between the symmetry axis and the vertical, and $\hat{\phi}$ is the azimuthal direction. This torque is perpendicular to both $\mathbf{L}$ (approximately along the symmetry axis for a fast-spinning top) and gravity (vertical). Therefore it pushes $\mathbf{L}$ sideways — producing a horizontal rotation of the angular momentum vector. This is precession.

### §4.6.2 — The Lagrangian Treatment

The complete Lagrangian for a heavy symmetric top with one point fixed is:

$$L = T_{\text{rot}} - V = \frac{1}{2}I(\dot{\theta}^2 + \dot{\phi}^2\sin^2\theta) + \frac{1}{2}I_3(\dot{\phi}\cos\theta + \dot{\psi})^2 - Mgl\cos\theta \tag{3.4.36}$$

where $l$ is the distance from the fixed point to the center of mass, and the potential energy is $V = Mgl\cos\theta$ (measuring from the horizontal).

Both $\phi$ and $\psi$ are cyclic coordinates. The conserved momenta are:

$$p_\phi = (I\sin^2\theta + I_3\cos^2\theta)\dot{\phi} + I_3\dot{\psi}\cos\theta = L_Z \tag{3.4.37}$$

$$p_\psi = I_3(\dot{\phi}\cos\theta + \dot{\psi}) = I_3\omega_3 = L_3 \tag{3.4.38}$$

Energy conservation gives:

$$E = \frac{1}{2}I\dot{\theta}^2 + V_{\text{eff}}(\theta) \tag{3.4.39}$$

where the **effective potential** is:

$$\boxed{V_{\text{eff}}(\theta) = \frac{(L_Z - L_3\cos\theta)^2}{2I\sin^2\theta} + \frac{L_3^2}{2I_3} + Mgl\cos\theta} \tag{3.4.40}$$

This is a one-dimensional problem in $\theta$ — exactly parallel to the effective potential method we used for central forces in Ch 3 (§3.2.3). The angular degrees of freedom $\phi$ and $\psi$ have been eliminated by their conservation laws, leaving only the nutation angle $\theta$ to be determined.

### §4.6.3 — Steady Precession

The simplest motion is **steady precession**: $\theta = \theta_0 = \text{const}$, so $\dot{\theta} = 0$ and the top precesses at a constant rate $\dot{\phi} = \Omega_p$. From $dV_\text{eff}/d\theta = 0$ and the constraint $\dot\theta = 0$, we find that $\Omega_p$ satisfies:

$$I\Omega_p^2\cos\theta_0 - L_3\Omega_p + Mgl = 0 \tag{3.4.41}$$

This is a quadratic in $\Omega_p$. For a fast-spinning top ($L_3 \gg \sqrt{4IMgl\cos\theta_0}$), the two solutions are:

**Slow precession:**

$$\boxed{\Omega_p^{(\text{slow})} \approx \frac{Mgl}{L_3} = \frac{Mgl}{I_3\omega_3}} \tag{3.4.42}$$

This is the familiar result: the precession rate is proportional to the torque ($Mgl$) and inversely proportional to the spin angular momentum ($I_3\omega_3$). The faster the top spins, the slower it precesses — exactly as angular momentum conservation demands. Torque changes $\mathbf{L}$'s direction at a rate proportional to $\tau/L$, and for large $L$ this rate is small.

**Fast precession:**

$$\Omega_p^{(\text{fast})} \approx \frac{L_3}{I\cos\theta_0} \tag{3.4.43}$$

This solution is rarely observed in everyday tops because it requires a very specific initial condition. It corresponds to a rapid precession where the centrifugal effects of the precessing motion itself dominate over gravity.

[FIGURE: Fig 3.4.5 — Heavy Symmetric Top Precession. A spinning top with its symmetry axis tilted at angle $\theta$ from the vertical. Gravity $Mg$ acts downward at the center of mass (distance $l$ from pivot). The gravitational torque $\boldsymbol{\tau} = \mathbf{r} \times M\mathbf{g}$ is horizontal, perpendicular to the tilt plane. The angular momentum vector $\mathbf{L}$ (approximately along the symmetry axis for fast spin) precesses around the vertical at rate $\Omega_p = Mgl/L_3$. Dashed circle shows the precession path of the symmetry axis tip. Caption: "A fast-spinning top precesses because gravity's torque is always perpendicular to $\mathbf{L}$, changing its direction but not its magnitude."]

### §4.6.4 — Nutation

When the initial conditions don't correspond to steady precession, the nutation angle $\theta$ oscillates between turning points $\theta_1$ and $\theta_2$ defined by $E = V_{\text{eff}}(\theta)$. This oscillation is **nutation** — a rapid nodding superimposed on the slow precession.

The motion of the symmetry axis, projected onto the horizontal plane, traces a characteristic pattern:

- If $\theta_1 = \theta_2$ (pure precession): a circle.
- If the top is released from rest ($\dot{\phi}_0 = 0$): cusps.
- If $\dot{\phi}_0 \neq 0$ but not the steady precession value: loops.

These patterns are direct consequences of the effective potential (3.4.40) and the conservation laws. The student who can sketch these patterns from the effective potential has mastered the heavy top.

### §4.6.5 — The Sleeping Top

A **sleeping top** is one that spins vertically ($\theta = 0$). This is an equilibrium — but is it stable?

Small perturbations about $\theta = 0$ grow or decay depending on the second derivative of $V_\text{eff}$. The stability condition is:

$$\boxed{L_3^2 > 4IMgl \qquad \text{(sleeping top stability)}} \tag{3.4.44}$$

or equivalently, $\omega_3 > \omega_{\text{crit}} = \sqrt{4IMgl/I_3^2}$. Above the critical spin rate, the top sleeps peacefully. Below it, the top tips over and begins to precess and nutate.

This is a bifurcation: the system transitions from a stable equilibrium (sleeping) to oscillatory motion (precession + nutation) as the spin drops below a critical value. The critical spin rate is determined entirely by the body's geometry ($I$, $I_3$, $M$, $l$) and the gravitational field ($g$) — both of which trace to zone architecture (inertia from metric structure, gravity from zone curvature).

---

## §4.7 — Gyroscopic Stability and Applications

### §4.7.1 — Stability of Rotation About Principal Axes

Return to the torque-free Euler equations (3.4.29 with $\boldsymbol{\tau} = 0$). Suppose the body rotates about one principal axis with a small perturbation about the other two. Let $\omega_3 = \Omega + \epsilon_3$ (dominant rotation about axis 3) with $\omega_1 = \epsilon_1$, $\omega_2 = \epsilon_2$ small. Linearizing Euler's equations:

$$I_1\dot{\epsilon}_1 \approx (I_2 - I_3)\Omega\epsilon_2 \tag{3.4.45a}$$
$$I_2\dot{\epsilon}_2 \approx (I_3 - I_1)\Omega\epsilon_1 \tag{3.4.45b}$$

Differentiating (3.4.45a) and substituting (3.4.45b):

$$\ddot{\epsilon}_1 = -\frac{(I_2 - I_3)(I_3 - I_1)}{I_1 I_2}\Omega^2\,\epsilon_1 \tag{3.4.46}$$

This is a harmonic oscillator if the coefficient of $\epsilon_1$ is negative — i.e., if $(I_2 - I_3)(I_3 - I_1) > 0$. Two cases:

- **$I_3 > I_1$ and $I_3 > I_2$** (rotation about the axis of LARGEST moment): stable.
- **$I_3 < I_1$ and $I_3 < I_2$** (rotation about the axis of SMALLEST moment): stable.
- **$I_1 < I_3 < I_2$ or $I_2 < I_3 < I_1$** (rotation about the INTERMEDIATE axis): **unstable.** In this case, $(I_2 - I_3) > 0$ while $(I_3 - I_1) > 0$, so $(I_2 - I_3)(I_3 - I_1) > 0$, making the coefficient of $\epsilon_1$ in Eq. (3.4.46) positive — an exponential growth rather than oscillation.

This is the **intermediate axis theorem** (also called the **tennis racket theorem** or **Dzhanibekov effect**): rotation about the intermediate principal axis is always unstable.

*Why?* The instability comes from the competing signs of the $(I_3 - I_2)$ and $(I_3 - I_1)$ terms in Euler's equations. When $I_3$ is intermediate, these terms have opposite signs, and their product drives exponential growth rather than oscillation. There is no physical force causing the instability — it is purely geometric, a consequence of the inertia tensor's structure.

### §4.7.2 — Gyroscopic Rigidity

A rapidly spinning body with angular momentum $L = I_3\omega_3 \gg 0$ resists changes in the direction of its spin axis. External torques produce precession rather than tilting. The precession rate (Eq. 3.4.42) scales as $\tau/L$ — the larger the angular momentum, the slower the response. In the limit $L \to \infty$, the gyroscope becomes infinitely rigid.

This is **gyroscopic rigidity**, and it has three important applications:

**The gyrocompass.** A spinning gyroscope mounted to rotate freely about one axis will align its spin axis with Earth's rotation axis. The Coriolis torque from Earth's rotation produces a precession that drives the gyro toward the north-south meridian. Once aligned, it stays aligned by gyroscopic rigidity. This works because angular momentum conservation (Vol 1 Eq. 1.7.33) applies in the rotating Earth frame with predictable Coriolis corrections.

**Spacecraft attitude control.** Reaction wheels — spinning disks mounted inside a spacecraft — use conservation of angular momentum to control the spacecraft's orientation without expelling propellant. Spin up a wheel in one direction, and the spacecraft rotates in the opposite direction. The International Space Station uses four reaction wheels (three primary + one backup) for attitude control. The physics is exactly Eq. (3.4.11): $\mathbf{L}_{\text{total}} = \mathbf{L}_{\text{wheels}} + \mathbf{L}_{\text{spacecraft}} = \text{const}$.

**Bicycle stability.** The gyroscopic effect of spinning wheels contributes to (though does not fully explain) bicycle stability. The front wheel's angular momentum produces a precession that steers the bicycle under the center of mass when it begins to lean. This is a dynamic application of $d\mathbf{L}/dt = \boldsymbol{\tau}$ — the gravitational torque on the leaning bicycle produces a steering precession.

### §4.7.3 — Vibration Modes of Rigid Bodies

A brief but important connection: a rigid body is an idealization. Real extended objects can deform, and when they do, they vibrate. These vibrations are standing waves in the material — precisely the kind of standing wave that the optics derivation chain (04-OPTICS_FROM_MAXWELL.md) analyzes for electromagnetic fields.

The connection is this: just as electromagnetic standing waves on the Firmament membrane create stable field configurations (the subject of Chapter 6), mechanical standing waves in an elastic body create normal modes of vibration. The mathematics is the same — eigenvalue problems for wave operators — and the physics traces to the same zone architecture: boundary conditions on the zone manifold select discrete frequencies.

We will not develop elastic vibrations in this chapter (that belongs to Ch 5, Continuum Mechanics), but the student should note the parallel: rigid body dynamics is the $\omega \to 0$ (zero-frequency) limit of continuum vibration theory, just as geometric optics is the $\lambda \to 0$ (zero-wavelength) limit of wave optics. Both limits emerge from the same zone architecture.

[FIGURE: Fig 3.4.6 — Gyroscopic Stability. A vector diagram showing a gyroscope with large angular momentum $\mathbf{L}$ along its spin axis. A small torque $\boldsymbol{\tau}$ produces a change $d\mathbf{L} = \boldsymbol{\tau}\,dt$ perpendicular to $\mathbf{L}$. The result is precession (change in direction) not tilting (change in magnitude). Inset: comparison with a non-spinning top that simply falls. Caption: "Gyroscopic stability in one picture. Torque changes $\mathbf{L}$'s direction, not its magnitude. The faster the spin, the smaller the angular change per unit torque — this is why gyroscopes resist reorientation."]

---

## §4.8 — Summary and Forward Look

This chapter derived the complete theory of rigid body rotation from two ingredients: **angular momentum conservation** (Vol 1 Ch 7, from the zone manifold's rotational symmetry) and the **Lagrangian/Hamiltonian formalism** (Ch 2, from the zone action's variational structure). No new physics was introduced. The derivation chain is:

$$\text{Zone SO(3) symmetry} \xrightarrow{\text{Noether}} \text{Angular momentum conservation} \xrightarrow{\text{extended body}} \text{Inertia tensor + Euler's equations}$$

The key results:

| Result | Equation | Derivation Source |
|--------|----------|-------------------|
| Inertia tensor | (3.4.9) | Kinetic energy (Ch 2 Eq. 3.2.4) + rigid constraint |
| $\mathbf{L} = \mathbf{I}\cdot\boldsymbol{\omega}$ | (3.4.11) | Noether charge for rotation |
| Euler's equations | (3.4.29) | Transport theorem + angular momentum conservation |
| Steady precession rate | (3.4.42) | Lagrangian with gravity + cyclic coordinates |
| Sleeping top stability | (3.4.44) | Effective potential analysis |
| Intermediate axis instability | (3.4.46) | Linearized Euler's equations |

**What comes next.** Chapter 5 relaxes the rigid body constraint and enters continuum mechanics, where deformable bodies and fluids are described by stress and strain tensors. The inertia tensor of this chapter generalizes to the stress-energy tensor of field theory — a connection that closes the circle back to the zone manifold's fundamental geometric object (Vol 1 Ch 7, Eq. 1.7.23).

The quantum analog of angular momentum — spin — will appear in Volume 4. There, the SO(3) rotational symmetry of the zone manifold will demand that angular momentum is quantized in integer and half-integer multiples of $\hbar$. The classical theory of this chapter provides the correspondence limit: quantum mechanics must reduce to Euler's equations when angular momenta are large compared to $\hbar$.

---

## Problem Sets

### Computational Problems

**Problem 4.1: Inertia Tensor of a Uniform Rectangular Plate.**
A uniform rectangular plate has mass $M$, dimensions $a \times b$, and negligible thickness. Place the plate in the $xy$-plane with its center at the origin.

(a) Compute the inertia tensor $I_{ij}$ about the center of mass.

(b) Verify that the coordinate axes are principal axes (explain why by symmetry).

(c) Use the parallel axis theorem to find the inertia tensor about one corner.

*Solution.* (a) By integration over $x \in [-a/2, a/2]$, $y \in [-b/2, b/2]$:
$I_{xx} = \frac{1}{12}Mb^2$, $I_{yy} = \frac{1}{12}Ma^2$, $I_{zz} = \frac{1}{12}M(a^2 + b^2)$. All products of inertia vanish by the symmetry of integration limits.

(b) The plate has two mirror symmetry planes ($xz$ and $yz$), which force the off-diagonal elements to zero. Principal axes coincide with symmetry axes.

(c) With $\mathbf{d} = (a/2, b/2, 0)$: $I_{xx}^{(\text{corner})} = \frac{1}{12}Mb^2 + M(b/2)^2 = \frac{1}{3}Mb^2$, etc. The off-diagonal product $I_{xy}^{(\text{corner})} = 0 + M(a/2)(b/2) = \frac{1}{4}Mab$.

---

**Problem 4.2: Precession Rate of a Gyroscope.**
A toy gyroscope has a disk of mass $M = 0.15$ kg and radius $R = 0.04$ m spinning at $\omega_3 = 150$ rad/s. The center of mass is $l = 0.03$ m from the pivot. Compute:

(a) The spin angular momentum $L_3 = I_3\omega_3$.

(b) The steady precession rate $\Omega_p$.

(c) The critical spin rate below which the gyroscope cannot sleep vertically.

*Solution.* (a) $I_3 = \frac{1}{2}MR^2 = \frac{1}{2}(0.15)(0.04)^2 = 1.2 \times 10^{-4}$ kg·m². Therefore $L_3 = 1.2 \times 10^{-4} \times 150 = 0.018$ kg·m²/s.

(b) $\Omega_p = Mgl/L_3 = (0.15)(9.81)(0.03)/(0.018) = 2.45$ rad/s, or about 0.39 rev/s. The top precesses roughly once every 2.6 seconds.

(c) The sleeping top condition (3.4.44) requires $L_3^2 > 4IMgl$. With $I \approx I_3/2 + Ml^2 \approx 1.95 \times 10^{-4}$ kg·m² (using the perpendicular axis theorem and parallel axis theorem): $\omega_{\text{crit}} = \sqrt{4IMgl}/I_3 = \sqrt{4(1.95\times10^{-4})(0.15)(9.81)(0.03)}/(1.2\times10^{-4}) \approx 49$ rad/s.

---

**Problem 4.3: Euler Angles for a Tilted Wheel.**
A uniform disk of mass $M$ and radius $R$ rolls without slipping on a horizontal surface while tilted at angle $\theta_0$ from the vertical (like a rolling coin). The contact point traces a circle of radius $r$ on the surface, and the disk's center traces a circle of radius $r + R\cos\theta_0$ at height $R\sin\theta_0$ above the surface.

(a) Express the angular velocity components $(\omega_1, \omega_2, \omega_3)$ in terms of $\dot{\phi}$, $\theta_0$, and the rolling condition.

(b) Show that steady precession requires $\dot{\phi}^2 = g\tan\theta_0/(r + R\cos\theta_0)$.

---

**Problem 4.4: Chandler Wobble Period.**
Using Earth's oblateness parameter $(I_3 - I)/I = 1/306$, compute:

(a) The rigid-body (Euler) prediction for the wobble period.

(b) The observed Chandler wobble period is approximately 433 days. What does the discrepancy tell us about Earth's interior?

*Solution.* (a) $T = 2\pi/\Omega_\text{body} = 2\pi/[(I_3/I - 1)\omega_3] = (1/0.00327)$ sidereal days $= 306$ days. (b) The longer observed period indicates Earth is not rigid — elastic deformation allows the body to adjust its shape slightly, reducing the effective oblateness and lengthening the period. This is a known result: the ratio $T_\text{observed}/T_\text{Euler} \approx 1.4$ constrains models of Earth's interior elasticity and viscosity.

### Conceptual Problems

**Problem 4.5: Why a Tensor?**
Explain physically, using the example of a dumbbell (two equal masses connected by a massless rod), why the moment of inertia must be a tensor rather than a scalar. Specifically: show that the angular momentum of a dumbbell spinning about an axis NOT aligned with the rod is not parallel to the angular velocity.

---

**Problem 4.6: Why Tops Precess, Not Fall.**
A friend who has not studied physics asks: "Why doesn't a spinning top fall over?" Give a clear physical explanation using only the concept of angular momentum as a conserved vector quantity. Then explain what changes when the top slows down below the critical spin rate.

---

**Problem 4.7: The Intermediate Axis.**
Hold a book (or phone) with the cover facing you. Toss it spinning about each of its three principal axes in turn (front-to-back, side-to-side, top-to-bottom). Describe what you observe. Explain the instability of rotation about the intermediate axis using the linearized Euler equations (3.4.45–3.4.46). Why does the book flip, and why does it flip back?

### Challenge Problems

**Problem 4.8: The Asymmetric Top — Qualitative Analysis.**
For a completely asymmetric top ($I_1 < I_2 < I_3$) with no external torques:

(a) Show that the angular momentum magnitude $L^2 = I_1^2\omega_1^2 + I_2^2\omega_2^2 + I_3^2\omega_3^2$ and the kinetic energy $2T = I_1\omega_1^2 + I_2\omega_2^2 + I_3\omega_3^2$ are both conserved.

(b) In $(\omega_1, \omega_2, \omega_3)$ space, the conservation of $L^2$ defines an ellipsoid and the conservation of $T$ defines another ellipsoid. Sketch both for the case $I_1 < I_2 < I_3$ and show that their intersection curves pass through the principal axis directions.

(c) Show that the intersection curves near the $\omega_1$ and $\omega_3$ axes are closed loops (stable rotation), while the intersection near $\omega_2$ consists of separatrices (unstable rotation). This provides a geometric proof of the intermediate axis theorem.

---

**Problem 4.9: The Tennis Racket in Space (Dzhanibekov Effect).**
In 1985, cosmonaut Vladimir Dzhanibekov observed a wingnut on the International Space Station spontaneously flip its rotation axis during torque-free motion.

(a) Model the wingnut as an asymmetric top with $I_1 : I_2 : I_3 = 1 : 2 : 3$. Set up the initial condition $\omega(0) = (0.01, \Omega, 0.01)$ with $\Omega = 10$ rad/s (spin about intermediate axis with small perturbations).

(b) Numerically integrate Euler's equations. Show that $\omega_2$ periodically reverses sign — the "flip." Estimate the flip period.

(c) Explain why the total angular momentum and energy remain constant despite the dramatic-looking flip. What conservation laws from Vol 1 Ch 7 guarantee this?

---

*With rigid body dynamics complete, the machinery of classical mechanics is fully assembled. The student who has worked through Chapters 1–4 can derive the motion of any mechanical system — from planets to gyroscopes — using the zone framework. Chapter 5 relaxes the rigid constraint and enters the continuum, where the Waters field equations of Volume 1 finally meet the fluid dynamics of everyday experience.*
