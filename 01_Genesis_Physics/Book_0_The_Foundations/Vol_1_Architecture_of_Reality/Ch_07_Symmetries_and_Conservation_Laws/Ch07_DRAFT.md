# Chapter 7: Symmetries and Conservation Laws

---

## Part II: The Firmament and the Waters (continued)

---

> *"Every good and perfect gift is from above, coming down from the Father of the heavenly lights, who does not change like shifting shadows."*
> — James 1:17

---

## 7.1 Why Conservation Laws Exist

Here is a question that most physics textbooks never bother to ask: *Why is energy conserved?*

They will tell you *that* energy is conserved. They will show you beautiful experiments confirming it to fifteen decimal places. They will even invoke Noether's theorem as the "reason." But press further — *why* does the action have time-translation symmetry in the first place? — and you get silence, or a shrug, or "it just does."

We can do better. In fact, after six chapters of careful construction, we *must* do better. We have built the zone manifold (Chapter 3), embedded it in six dimensions (Chapter 4), stretched the Firmament across it as a dynamical membrane (Chapter 5), and written the field equations governing the Waters (Chapter 6). Every one of those constructions came with a specific *why*. The conservation laws that flow from them deserve the same treatment.

The program of this chapter is straightforward and ambitious: **derive every conservation law of physics from the symmetries of the zone manifold, using Noether's theorem as the bridge.**

The logical chain runs like this:

1. **Divine attribute** (e.g., God is eternal and unchanging — Malachi 3:6)
2. **Manifold symmetry** (e.g., the action is invariant under time translations)
3. **Noether's theorem** (continuous symmetry → conserved current)
4. **Conservation law** (e.g., energy is conserved: dE/dt = 0)

This is not metaphor. It is mathematics. Emmy Noether proved in 1918 that every continuous symmetry of an action functional yields exactly one conserved current. We established in Chapter 1 (Axiom 3) that the symmetries of our zone manifold reflect divine attributes. In Chapters 4–6, we wrote down the complete action. Now we harvest the consequences.

By the end of this chapter, the reader will possess:

- A rigorous proof of Noether's theorem adapted to the 6D zone manifold
- Explicit derivations of energy, momentum, angular momentum, and charge conservation
- An understanding of WHY each law holds — traced to a specific divine attribute
- A clear taxonomy of exact versus approximate symmetries
- An explanation of anomalies: classical symmetries that quantum mechanics destroys
- Precise, boxed conservation law statements ready for Volume 2 to use as constraints

Let us begin with the theorem itself.

---

## 7.2 Noether's Theorem on the Zone Manifold

### 7.2.1 The Total Action

Across Chapters 4, 5, and 6, we assembled the complete action for the zone manifold system. Let us collect it here. The total action is:

$$\boxed{S_{\text{total}} = S_{\text{grav}} + S_{\text{membrane}} + S_{\text{Waters}} + S_{\text{matter}}} \tag{1.7.1}$$

where:

- $S_{\text{grav}}$ is the Einstein-Hilbert action on the 6D manifold, governing the metric $g_{AB}$ (Chapter 4, Eq. (1.4.66)):

$$S_{\text{grav}} = \frac{c^4}{16\pi G_6} \int d^6x \, \sqrt{-g} \, R^{(6)} \tag{1.7.2}$$

- $S_{\text{membrane}}$ is the Firmament action (Chapter 5, Eq. (1.5.31)):

$$S_{\text{membrane}} = -\sigma \int d^4\xi \, \sqrt{-\gamma} + \frac{\mu}{2} \int d^4\xi \, \sqrt{-\gamma} \, \gamma^{\mu\nu} \partial_\mu \Phi \, \partial_\nu \Phi + \cdots \tag{1.7.3}$$

- $S_{\text{Waters}}$ is the Waters field action (Chapter 6, Eq. (1.6.9)):

$$S_{\text{Waters}} = \int d^6x \, \sqrt{-g} \left[ \frac{1}{2} g^{AB} \partial_A \Psi_A \, \partial_B \Psi_A - V(\Psi_A) + \frac{1}{2} g^{AB} \partial_A \Psi_B \, \partial_B \Psi_B - U(\Psi_B) - G_{\text{int}} \Psi_A \Psi_B \right] \tag{1.7.4}$$

- $S_{\text{matter}}$ encompasses all baryonic matter fields coupled to the metric and Waters fields.

The notation follows our conventions: capital Latin indices $A, B = 0, 1, 2, 3, 5, 6$ run over all six dimensions; Greek indices $\mu, \nu = 0, 1, 2, 3$ run over the four Firmament dimensions; $\gamma_{\mu\nu}$ is the induced metric on the Firmament hypersurface; $g_{AB}$ is the full 6D metric from Eq. (1.4.2).

### 7.2.2 Statement of the First Noether Theorem

**Why does Noether's theorem work?** The physical intuition is disarmingly simple. If the action does not change when you perform some transformation — slide time forward, shift space sideways, rotate your coordinates — then the equations of motion must contain a quantity that does not change either. Invariance of the *law* implies constancy of a *thing*.

More precisely:

> **Theorem 7.1 (Noether, 1918).** Let $S[\phi^a] = \int d^n x \, \mathcal{L}(\phi^a, \partial_\mu \phi^a, x)$ be an action functional for fields $\phi^a(x)$. Suppose a continuous family of transformations parameterized by $\epsilon$,
>
> $$x^\mu \to x^\mu + \epsilon \, \delta x^\mu, \qquad \phi^a \to \phi^a + \epsilon \, \delta \phi^a \tag{1.7.5}$$
>
> leaves the action invariant: $\delta S = 0$ to first order in $\epsilon$. Then there exists a current
>
> $$j^\mu = \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi^a)} \delta \phi^a + \left( \mathcal{L} \, \delta^\mu{}_\nu - \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi^a)} \partial_\nu \phi^a \right) \delta x^\nu \tag{1.7.6}$$
>
> that is conserved on shell (i.e., when the fields satisfy the Euler-Lagrange equations):
>
> $$\partial_\mu j^\mu = 0 \tag{1.7.7}$$

The conserved *charge* associated with this current is:

$$Q = \int d^{n-1}x \, j^0(x) \tag{1.7.8}$$

and satisfies $dQ/dt = 0$.

### 7.2.3 Proof

The proof is short enough to include in full, and important enough to demand it. A student who cannot reproduce this proof has not understood the chapter.

To find the conserved current, we watch how the Lagrangian changes under the symmetry transformation. The key insight is that the Lagrangian can change in two independent ways: (1) the fields themselves shift ($\phi^a \to \phi^a + \epsilon\,\delta\phi^a$), and (2) the spacetime coordinates move ($x^\mu \to x^\mu + \epsilon\,\delta x^\mu$), warping the domain of integration. These two effects must be separated and tracked independently. Their interplay — when combined and forced to vanish by the invariance condition $\delta S = 0$ — reveals the hidden conserved quantity.

Consider the variation of the action under the transformation (1.7.5). The total variation of $\mathcal{L}$ has two pieces — one from the field transformation, one from the coordinate transformation:

$$\delta \mathcal{L} = \frac{\partial \mathcal{L}}{\partial \phi^a} \delta\phi^a + \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi^a)} \delta(\partial_\mu \phi^a) + \partial_\mu \mathcal{L} \, \delta x^\mu \tag{1.7.9}$$

We use the identity $\delta(\partial_\mu \phi^a) = \partial_\mu(\delta \phi^a)$ (variations commute with derivatives) and integrate by parts:

$$\frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi^a)} \partial_\mu(\delta\phi^a) = \partial_\mu \left[ \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi^a)} \delta\phi^a \right] - \left[ \partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi^a)} \right] \delta\phi^a \tag{1.7.10}$$

Substituting back and grouping terms:

$$\delta \mathcal{L} = \underbrace{\left[ \frac{\partial \mathcal{L}}{\partial \phi^a} - \partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi^a)} \right]}_{\text{= 0 on shell (Euler-Lagrange)}} \delta\phi^a + \partial_\mu \left[ \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi^a)} \delta\phi^a \right] + \partial_\mu (\mathcal{L} \, \delta x^\mu) \tag{1.7.11}$$

The first term vanishes when the fields satisfy the Euler-Lagrange equations. The invariance condition $\delta S = 0$ then requires:

$$\partial_\mu \left[ \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi^a)} \delta\phi^a + \mathcal{L} \, \delta x^\mu \right] = 0 \tag{1.7.12}$$

The quantity in brackets is precisely the Noether current $j^\mu$ from Eq. (1.7.6). Therefore $\partial_\mu j^\mu = 0$. $\square$

**Two remarks.** First, notice where the Euler-Lagrange equations entered: the conservation law holds *on shell*, meaning for fields that actually satisfy the equations of motion. This is not a limitation — it is a feature. The conserved quantities are properties of physical solutions, not arbitrary field configurations.

Second, observe that the proof works for *any* action and *any* continuous symmetry. We did not need to specify the field content. This universality is why Noether's theorem is arguably the most powerful single result in theoretical physics.

### 7.2.4 Covariant Generalization for the Zone Manifold

On a curved manifold, ordinary derivatives $\partial_\mu$ become covariant derivatives $\nabla_\mu$, and the conservation equation becomes:

$$\nabla_\mu j^\mu = \frac{1}{\sqrt{-g}} \partial_\mu \left( \sqrt{-g} \, j^\mu \right) = 0 \tag{1.7.13}$$

For the 6D zone manifold with metric $g_{AB}$, the covariant divergence uses the full 6D determinant:

$$\nabla_A j^A = \frac{1}{\sqrt{-g_6}} \partial_A \left( \sqrt{-g_6} \, j^A \right) = 0 \tag{1.7.14}$$

The conserved charge becomes an integral over a 5D spacelike hypersurface $\Sigma$:

$$Q = \int_\Sigma d^5x \, \sqrt{h} \, n_A j^A \tag{1.7.15}$$

where $n_A$ is the unit normal to $\Sigma$ and $h$ is the determinant of the induced metric on $\Sigma$.

### 7.2.5 The Second Noether Theorem: Gauge Symmetries

For completeness, we state the second theorem, which applies to *local* (gauge) symmetries:

> **Theorem 7.2 (Noether's Second Theorem).** If the action is invariant under a transformation with an arbitrary function $\epsilon(x)$ (not just a constant $\epsilon$), then the equations of motion are not all independent — they satisfy identities.

The most important application: the invariance of $S_{\text{grav}}$ under arbitrary diffeomorphisms produces the *contracted Bianchi identity*:

$$\nabla_\mu G^{\mu\nu} = 0 \tag{1.7.16}$$

which, via the Einstein equations $G^{\mu\nu} = (8\pi G/c^4) T^{\mu\nu}$, implies:

$$\nabla_\mu T^{\mu\nu} = 0 \tag{1.7.17}$$

This is **covariant energy-momentum conservation** — the master equation from which individual conservation laws follow. We derived it abstractly in Chapter 2 (Eq. (1.2.31)) from the Bianchi identity; now we see it is a *consequence of diffeomorphism invariance* via Noether's second theorem.

[FIGURE: Fig 1.7.1 — Noether's Theorem: From Symmetry to Conservation. Flowchart showing the logical chain: Divine Attribute → Manifold Symmetry → Invariance of Action → Noether Current → Conserved Charge, with the two Noether theorems as parallel paths for global and local symmetries.]

---

## 7.3 Energy Conservation from Time-Translation Symmetry

### 7.3.1 The Why

*Why is energy conserved?*

Because God is eternal. "I the LORD do not change" (Malachi 3:6). If the nature of God does not depend on *when* you examine it, then the laws of physics — which reflect that nature through the zone manifold — cannot depend on time either. In Chapter 4, we identified the Killing vector $K^\mu_{(t)} = \partial_t$ (Eq. (1.4.32)) as the generator of time translations on the zone manifold. The 6D metric (1.4.2), the membrane action (1.7.3), and the Waters action (1.7.4) are all constructed to be time-translation invariant. Noether's theorem then guarantees a conserved charge. That charge is energy.

This is not a metaphor dressed in equations. It is a derivation. Let us make it explicit.

### 7.3.2 The Derivation

Consider the time-translation Killing vector from Chapter 4:

$$K^A_{(t)} = (1, 0, 0, 0, 0, 0) = \delta^A_0 \tag{1.7.18}$$

This generates the transformation $t \to t + \epsilon$, $x^i \to x^i$, $\xi \to \xi$, $\eta \to \eta$. The total action $S_{\text{total}}$ is invariant because:

- The 6D metric (1.4.2) has $\partial_t g_{AB} = 0$ in the cosmological rest frame (the warp factors $A(\xi,\eta)$ and $B(\xi,\eta)$ depend only on the extra coordinates)
- The potentials $V(\Psi_A)$ and $U(\Psi_B)$ are time-independent functions of the fields
- The coupling $G_{\text{int}}$ is a constant
- The membrane tension $\sigma$ and mass density $\mu$ are constants

The Noether current associated with $K^A_{(t)}$ is the energy-momentum density contracted with the Killing vector:

$$j^A_{(E)} = T^A{}_B \, K^B_{(t)} = T^A{}_0 \tag{1.7.19}$$

The conservation equation $\nabla_A j^A_{(E)} = 0$ gives:

$$\nabla_A T^{A0} = 0 \tag{1.7.20}$$

Expanding this in the 6D coordinates:

$$\frac{1}{\sqrt{-g_6}} \partial_A \left( \sqrt{-g_6} \, T^{A0} \right) = 0 \tag{1.7.21}$$

The conserved charge — the total energy — is obtained by integrating the time component over a spacelike hypersurface:

$$\boxed{E = \int d^3x \, d\xi \, d\eta \, \sqrt{-g_6} \, T^{00} = \text{constant}} \tag{1.7.22}$$

### 7.3.3 Sector Decomposition

The total stress-energy tensor decomposes into contributions from each sector:

$$T^{AB}_{\text{total}} = T^{AB}_{\text{grav}} + T^{AB}_{\text{membrane}} + T^{AB}_{\text{A}} + T^{AB}_{\text{B}} + T^{AB}_{\text{matter}} \tag{1.7.23}$$

The individual sectors are *not* separately conserved — energy flows between them. The membrane absorbs energy from the Waters; matter radiates energy into the Waters Below; the Waters Above drive expansion. But the *total* is exactly conserved:

$$\frac{dE_{\text{total}}}{dt} = \frac{d}{dt}\left( E_{\text{membrane}} + E_A + E_B + E_{\text{matter}} \right) = 0 \tag{1.7.24}$$

This is precisely what we would expect from the Conservation Principle (Principle 2, Chapter 1): after Day 7, nothing is created or destroyed within Zone 2.2. Noether's theorem provides the *mathematical proof* of what theology asserts.

### 7.3.4 Energy in the Effective 4D Theory

An observer on the Firmament does not measure 6D integrals. They measure 4D quantities. By integrating over the extra dimensions (a process we will formalize as Kaluza-Klein reduction in Volume 2), the 6D conservation law projects to:

$$\nabla_\mu T^{\mu 0}_{\text{eff}} = 0 \tag{1.7.25}$$

where $T^{\mu\nu}_{\text{eff}}$ is the effective 4D stress-energy tensor, incorporating all the extra-dimensional physics as effective masses, couplings, and cosmological constants. The 4D energy:

$$\boxed{E_{\text{4D}} = \int d^3x \, \sqrt{-\gamma} \, T^{00}_{\text{eff}} = \text{constant}} \tag{1.7.26}$$

This is the energy conservation law as measured in laboratory physics.

---

## 7.4 Momentum and Angular Momentum Conservation

### 7.4.1 Linear Momentum: God's Omnipresence

*Why is momentum conserved?*

Because God is equally present everywhere. "Where can I go from your Spirit? Where can I flee from your presence?" (Psalm 139:7). If no location in space is privileged over any other, then the laws of physics must be the same at all spatial points. This is spatial translation invariance. From Chapter 4, the three spatial Killing vectors are:

$$K^A_{(i)} = \delta^A_i, \quad i = 1, 2, 3 \tag{1.7.27}$$

generating the transformations $x^i \to x^i + \epsilon^i$ while leaving $t$, $\xi$, and $\eta$ unchanged. By the same argument as Section 7.3, the action is invariant under these translations because neither the metric warp factors, the potentials, nor the couplings depend on the spatial coordinates $x^i$ (in the cosmological rest frame, the FLRW metric has spatial homogeneity).

The Noether currents are:

$$j^A_{(P_i)} = T^A{}_i \tag{1.7.28}$$

and their conservation $\nabla_A T^{Ai} = 0$ yields three conserved charges:

$$\boxed{P^i = \int d^3x \, d\xi \, d\eta \, \sqrt{-g_6} \, T^{0i} = \text{constant}, \quad i = 1, 2, 3} \tag{1.7.29}$$

In the effective 4D theory:

$$\boxed{P^i_{\text{4D}} = \int d^3x \, \sqrt{-\gamma} \, T^{0i}_{\text{eff}} = \text{constant}} \tag{1.7.30}$$

This is linear momentum conservation: the total momentum of an isolated system does not change. Every collision, every explosion, every gravitational interaction conserves total momentum — because space itself has no preferred location.

### 7.4.2 Angular Momentum: God's Impartiality

*Why is angular momentum conserved?*

Because God shows no favoritism in direction. "God does not show favoritism" (Acts 10:34). If no direction in space is privileged, then the laws must be invariant under rotations. The three rotation Killing vectors from Chapter 4 (Eq. (1.4.36)) generate the SO(3) rotation group:

$$K^A_{(R_k)} = \epsilon_{kij} x^i \delta^A_j \tag{1.7.31}$$

where $\epsilon_{kij}$ is the Levi-Civita symbol and $k = 1, 2, 3$ labels the three independent rotation generators (about $x$, $y$, $z$ axes respectively).

The associated Noether currents define the angular momentum tensor:

$$M^{A,ij} = x^i T^{Aj} - x^j T^{Ai} \tag{1.7.32}$$

Its conservation $\nabla_A M^{A,ij} = 0$ (which follows from $\nabla_A T^{Ai} = 0$ and the symmetry $T^{ij} = T^{ji}$) yields three conserved angular momenta:

$$\boxed{L^k = \frac{1}{2} \epsilon_{kij} \int d^3x \, \sqrt{-\gamma} \, M^{0,ij}_{\text{eff}} = \text{constant}, \quad k = 1, 2, 3} \tag{1.7.33}$$

### 7.4.3 The Poincaré Algebra

Together, the 4 translations (1 time + 3 space) and the 6 independent Lorentz transformations (3 rotations + 3 boosts) generate the **Poincaré group** — the full symmetry group of flat spacetime. The 10 conserved charges are:

| Symmetry | Generator | Conserved Quantity | Charge |
|----------|-----------|-------------------|--------|
| Time translation | $\partial_t$ | Energy | $E$ |
| Spatial translations | $\partial_i$ | Linear momentum | $P^i$ (3) |
| Rotations | $\epsilon_{kij} x^i \partial_j$ | Angular momentum | $L^k$ (3) |
| Boosts | $t \partial_i + x^i \partial_t$ | Center-of-mass motion | $K^i$ (3) |

$$\text{Total: } 1 + 3 + 3 + 3 = 10 \text{ conserved charges} \tag{1.7.34}$$

These 10 charges close under the Poincaré algebra, exactly as identified in Chapter 4 (Eq. (1.4.37)). Every prediction of special relativity — time dilation, length contraction, the invariant speed $c$ — follows from this symmetry structure.

[FIGURE: Fig 1.7.2 — Killing Vectors on the Zone Manifold. The 6D zone manifold shown schematically with the four Killing vectors (∂_t, ∂_x, ∂_y, ∂_z) as arrows along the 4D Firmament, the six rotation/boost generators as curved arrows, and X marks on the ξ and η directions where warp factors break translational symmetry.]

---

## 7.5 Charge Conservation from Gauge Symmetry

### 7.5.1 From Duality to Gauge Invariance

*Why is electric charge conserved?*

Because God creates through complementary pairs — the Duality Principle (Principle 5). "God created mankind in his own image... male and female he created them" (Genesis 1:27). This pairing permeates all creation: Waters Above and Below, matter and antimatter, positive and negative charge.

In the mathematical framework, duality manifests as a *gauge symmetry* of the Waters fields. Consider the global phase transformation:

$$\Psi_A \to e^{i\alpha} \Psi_A, \qquad \Psi_B \to e^{-i\alpha} \Psi_B \tag{1.7.35}$$

where $\alpha$ is a constant. This is a U(1) transformation — the same symmetry group that governs electromagnetism. The Waters action (1.7.4) is invariant under this transformation because:

- The kinetic terms $|\partial_A \Psi|^2$ involve $|\Psi|^2$ and are phase-invariant
- The potentials $V(|\Psi_A|^2)$ and $U(|\Psi_B|^2)$ depend only on magnitudes
- The interaction term $G_{\text{int}} \Psi_A \Psi_B$ transforms as $G_{\text{int}} e^{i\alpha} \Psi_A e^{-i\alpha} \Psi_B = G_{\text{int}} \Psi_A \Psi_B$ — invariant

(A technical note on fields: Chapter 6 developed the Waters field equations using real scalar fields $\Psi_A$ and $\Psi_B$, which is sufficient for the gravitational and thermodynamic properties of the Waters. However, to accommodate *charge* — the ability of matter to carry positive or negative electric quantum numbers — the fields must be promoted to complex scalars. This is a standard procedure in field theory: any real field can be extended to a complex field by combining two real degrees of freedom into one complex field, $\Psi = \Psi_1 + i\Psi_2$. The real-field equations of Chapter 6 describe the physical vacuum state; the complex extension reveals the full symmetry structure, including the U(1) gauge symmetry responsible for electromagnetism. We will develop the complex Waters formalism systematically in Volume 2; here we use it to derive the charge conservation law.)

### 7.5.2 The Electromagnetic Current

Applying Noether's theorem to the U(1) transformation (1.7.35) with infinitesimal parameter $\alpha$:

$$\delta \Psi_A = i\alpha \Psi_A, \qquad \delta \Psi_B = -i\alpha \Psi_B \tag{1.7.36}$$

The Noether current is:

$$j^\mu_{\text{em}} = i \left[ \Psi_A^* (\partial^\mu \Psi_A) - (\partial^\mu \Psi_A^*) \Psi_A \right] - i \left[ \Psi_B^* (\partial^\mu \Psi_B) - (\partial^\mu \Psi_B^*) \Psi_B \right] \tag{1.7.37}$$

Its conservation follows from Noether's theorem:

$$\boxed{\partial_\mu j^\mu_{\text{em}} = 0} \tag{1.7.38}$$

The conserved charge is the total electric charge:

$$\boxed{Q = \int d^3x \, j^0_{\text{em}} = \text{constant}} \tag{1.7.39}$$

### 7.5.3 Promoting to Local Gauge Invariance

The global symmetry (1.7.35) with constant $\alpha$ produces charge conservation. But physics demands more: we want *local* gauge invariance with $\alpha = \alpha(x)$, because the Duality Principle operates at every point independently.

Local invariance requires introducing a gauge field $A_\mu$ — the electromagnetic potential — with the covariant derivative:

$$D_\mu \Psi = (\partial_\mu - ieA_\mu) \Psi \tag{1.7.40}$$

and the gauge transformation:

$$A_\mu \to A_\mu + \frac{1}{e} \partial_\mu \alpha(x) \tag{1.7.41}$$

The full locally gauge-invariant action includes the Maxwell kinetic term:

$$S_{\text{EM}} = -\frac{1}{4} \int d^4x \, \sqrt{-\gamma} \, F_{\mu\nu} F^{\mu\nu} \tag{1.7.42}$$

where $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is the electromagnetic field strength.

This is how electromagnetism *emerges* from the Duality Principle. The requirement that Waters Above and Waters Below maintain their complementary pairing at every spacetime point — local gauge invariance — forces the existence of the photon. We will develop this fully in Volume 2. For now, the key result is:

**Local U(1) gauge invariance of the Waters action guarantees charge conservation absolutely.** It is not an approximate law. It is exact, because gauge invariance is an exact symmetry — the photon is massless, which means U(1) is unbroken.

### 7.5.4 Baryon and Lepton Number

Beyond electric charge, particle physics recognizes two other approximately conserved quantum numbers:

**Baryon number** $B$: the number of baryons (protons, neutrons) minus antibaryons. Since each baryon is composed of three quarks, baryon number is equivalently:

$$B = \frac{1}{3}(n_q - n_{\bar{q}}) \tag{1.7.43}$$

where $n_q$ counts quarks and $n_{\bar{q}}$ counts antiquarks. The factor of $1/3$ reflects the three-quark composition of each baryon.

**Lepton number** $L$: the number of leptons (electrons, neutrinos) minus antileptons.

$$L = n_\ell - n_{\bar{\ell}} \tag{1.7.44}$$

These arise from approximate global symmetries of the strong and electroweak interactions. Here $\psi_q$ denotes the quark field and $\psi_\ell$ the lepton field; the Lagrangians for strong and electroweak interactions are invariant under global phase rotations of these fields:

$$\psi_q \to e^{i\beta/3} \psi_q \quad \text{(baryon rotation)} \tag{1.7.45}$$
$$\psi_\ell \to e^{i\gamma} \psi_\ell \quad \text{(lepton rotation)} \tag{1.7.46}$$

The associated Noether currents give:

$$\frac{dB}{dt} \approx 0, \qquad \frac{dL}{dt} \approx 0 \tag{1.7.47}$$

We write "$\approx 0$" rather than "$= 0$" deliberately. These are *approximate* conservation laws — and the reason they are only approximate is one of the most profound facts in physics. We address this in Section 7.6.

### 7.5.5 CPT as a Discrete Noether Analog

The continuous symmetries we have discussed produce conservation laws via Noether's first theorem. But the Duality Principle also implies discrete symmetries:

- **C** (Charge conjugation): particle ↔ antiparticle, $q \to -q$
- **P** (Parity): spatial reflection, $\vec{x} \to -\vec{x}$
- **T** (Time reversal): $t \to -t$

The combined operation **CPT** is an exact symmetry of any Lorentz-invariant quantum field theory (the CPT theorem of Lüders and Pauli). While individual C, P, or T may be violated, their product never is:

$$\boxed{\text{CPT symmetry is exact: } \mathcal{L}(\phi, x) = \mathcal{L}(\phi^{\text{CPT}}, x^{\text{CPT}})} \tag{1.7.48}$$

Why must CPT hold? Because any quantum field theory that is both Lorentz-invariant and causal — meaning that spacelike-separated measurements commute — automatically respects CPT. This is not a symmetry we impose; it is built into the fabric of relativistic quantum mechanics. Violating CPT would require abandoning either Lorentz invariance or quantum causality itself — a revolution far beyond any observed anomaly.

CPT invariance guarantees:

- Every particle has an antiparticle with identical mass
- Particle and antiparticle lifetimes are equal
- Total charge of the universe is zero (if created from nothing)

This is the discrete counterpart of continuous charge conservation. The Duality Principle, expressed through CPT, ensures that creation's fundamental pairing is never broken.

---

## 7.6 Approximate Symmetries, Anomalies, and Broken Conservation

### 7.6.1 Why Some Symmetries Are Only Approximate

Not every classical symmetry survives into the quantum theory. This is not a failure of our framework — it is a prediction of it. The zone structure introduces specific symmetry-breaking mechanisms that we must catalogue honestly.

There are three categories:

1. **Symmetries broken by zone structure** (classical breaking)
2. **Symmetries broken by quantum effects** (anomalies)
3. **Symmetries broken by phase transitions** (spontaneous breaking)

### 7.6.2 Extra-Dimensional Symmetry Breaking: Why No Kaluza-Klein Charges

A question the reader should have been asking since Chapter 4: *The 6D manifold has six coordinates. We found Killing vectors for only four directions (plus rotations and boosts). Why don't the extra dimensions $\xi$ and $\eta$ produce their own conservation laws?*

The answer is in the warp factors. Recall from Chapter 4 (Eq. (1.4.2)) that the 6D metric has the form:

$$ds^2 = e^{2A(\xi,\eta)} \left[ -c^2 dt^2 + a^2(t)(dx^2 + dy^2 + dz^2) \right] + e^{2B(\xi,\eta)} (d\xi^2 + d\eta^2) \tag{1.7.49}$$

The warp factors $A(\xi,\eta)$ and $B(\xi,\eta)$ depend on the extra coordinates. This means $\partial_\xi$ and $\partial_\eta$ are **not** Killing vectors:

$$\mathcal{L}_{\partial_\xi} g_{AB} \neq 0, \qquad \mathcal{L}_{\partial_\eta} g_{AB} \neq 0 \tag{1.7.50}$$

where $\mathcal{L}$ denotes the Lie derivative. Since the metric is not invariant under extra-dimensional translations, Noether's theorem produces *no* conserved charges for these directions.

**Why is this necessary?** Because the extra dimensions carry the zone structure. The Waters Above occupy the $\xi > \xi_0$ region; the Waters Below occupy $\eta < \eta_0$. The Firmament sits at fixed $(\xi_0, \eta_0)$. This architecture — which we motivated physically and theologically in Chapters 3–5 — *requires* the extra dimensions to be inhomogeneous. Homogeneity would mean no zones, no boundaries, no Firmament, no Waters separation. The very structure that makes the universe what it is necessarily breaks extra-dimensional translation symmetry.

This is a *feature*, not a bug. It explains why we observe exactly 10 Poincaré conservation laws (energy, 3 momenta, 3 angular momenta, 3 boost charges) and no exotic "fifth forces" or extra-dimensional charges in laboratory physics.

### 7.6.3 Quantum Anomalies: The Chiral Anomaly

A classical symmetry can be destroyed by quantum effects. The most important example is the **chiral anomaly** (Adler-Bell-Jackiw, 1969).

Consider a massless fermion $\psi$ with a classical chiral symmetry:

$$\psi \to e^{i\alpha \gamma_5} \psi \tag{1.7.51}$$

where $\gamma_5$ is the chirality matrix. Classically, this symmetry gives a conserved axial current:

$$\partial_\mu j^\mu_5 \overset{\text{classical}}{=} 0 \tag{1.7.52}$$

But when you compute the quantum corrections (the triangle diagram with two vector vertices and one axial vertex), you find:

$$\boxed{\partial_\mu j^\mu_5 = \frac{e^2}{16\pi^2} F_{\mu\nu} \tilde{F}^{\mu\nu}} \tag{1.7.53}$$

where $\tilde{F}^{\mu\nu} = \frac{1}{2} \epsilon^{\mu\nu\rho\sigma} F_{\rho\sigma}$ is the dual field strength. The right-hand side is nonzero in the presence of electromagnetic fields. The classical conservation law is *anomalous* — broken by quantum mechanics.

**Why does this matter for our framework?** Because the anomaly has profound physical consequences:

1. **Neutral pion decay**: $\pi^0 \to \gamma\gamma$ proceeds via the chiral anomaly. Without it, this decay would be forbidden. The observed rate matches the anomaly prediction to within 2%.

2. **Baryon number violation**: Through the electroweak anomaly ('t Hooft process), baryon number $B$ is violated:

$$\partial_\mu j^\mu_B = \frac{N_f g^2}{32\pi^2} W^a_{\mu\nu} \tilde{W}^{a\mu\nu} \tag{1.7.54}$$

where $N_f$ is the number of fermion families. This means $B$ is conserved only approximately — violated by quantum tunneling processes (sphalerons) that are exponentially suppressed at low temperatures but active in the early universe.

3. **Matter-antimatter asymmetry**: The baryon asymmetry of the universe ($n_B / n_\gamma \approx 6 \times 10^{-10}$) requires B violation, as Sakharov showed in 1967. The anomaly provides it.

### 7.6.4 Anomaly Cancellation

Not all anomalies are physical. In a consistent quantum theory, certain anomalies must *cancel* between different particle species. The **gauge anomaly** — an anomaly in a local (gauge) symmetry — would render the theory mathematically inconsistent (non-unitary, non-renormalizable).

In the Standard Model, the gauge anomaly cancels precisely when the number of quark colors equals the number of lepton families:

$$\sum_{\text{fermions}} Q_f^3 = 3 \times \left(\frac{2}{3}\right)^3 + 3 \times \left(-\frac{1}{3}\right)^3 + (-1)^3 + 0^3 = 0 \tag{1.7.55}$$

This cancellation is not accidental. In our framework, it is a consequence of the zone manifold's topological consistency — the same consistency that requires the Firmament to be a well-defined hypersurface (Chapter 5). A universe with anomalous gauge symmetries would be mathematically sick; the zone architecture forbids it.

### 7.6.5 CP Violation and the Fall

The combined operation CP (charge conjugation × parity) is *almost* a symmetry — but not quite. CP violation was discovered in 1964 in kaon decays and has since been observed in B meson and charm meson systems.

In our framework, CP violation has a specific theological interpretation. CP symmetry is a manifestation of perfect Duality — matter and antimatter behaving identically under mirror reflection. Its violation signals the *asymmetry* introduced by the Fall (Phase 3). During the Edenic phase (Phase 2), when $\kappa = \kappa_{\text{full}}$, CP would be exact. The weakening of the sustaining field ($\kappa_{\text{partial}} < \kappa_{\text{full}}$) allows small CP-violating effects:

$$\delta_{\text{CP}} \propto \epsilon \sim \frac{\kappa_{\text{full}} - \kappa_{\text{partial}}}{\kappa_{\text{full}}} \tag{1.7.56}$$

Here is the conjecture: the parameter $\epsilon$ — defined in Chapter 1 (Eq. (1.6.1)) as the measure of the sustaining field's diminishment after the Fall — should couple to CP-violating interactions in the Standard Model. During the Edenic phase ($\epsilon = 0$, full sustenance), CP would be exact. As $\epsilon > 0$ increases after the Fall, CP violation becomes possible. The *magnitude* of CP violation, measured in kaon and B meson experiments, should therefore scale with $\epsilon$. This is testable in principle: measure $\epsilon$ independently (through aging rates, cosmological parameters) and check whether the CP violation strength matches.

This connection resonates with Paul's assertion that "the creation was subjected to frustration" (Romans 8:20–21). The precise magnitude of CP violation may be a physical signature of that cosmic rupture.

We flag this as speculative and mark it as an open question for Volume 6 (Predictions and Simulations).

[FIGURE: Fig 1.7.4 — Exact vs. Approximate Symmetries. Left column: exact symmetries (CPT, U(1) gauge, Poincaré) shown as perfect circles with unbroken conservation law statements. Right column: approximate symmetries (B, L, CP, chiral) shown as cracked circles with anomaly equations and breaking mechanisms labeled.]

---

## 7.7 The Conservation Law Taxonomy

### 7.7.1 Master Summary

We have now derived every major conservation law from first principles. Let us collect them in a single reference table:

**Table 7.1: Conservation Laws of the Zone Manifold**

| Conservation Law | Symmetry | Type | Status | Equation | Divine Attribute |
|-----------------|----------|------|--------|----------|-----------------|
| Energy | Time translation | Continuous, global | **Exact** | (1.7.22), (1.7.26) | Eternality |
| Linear momentum (×3) | Spatial translation | Continuous, global | **Exact** | (1.7.29), (1.7.30) | Omnipresence |
| Angular momentum (×3) | Rotation | Continuous, global | **Exact** | (1.7.33) | Impartiality |
| Boost charge (×3) | Lorentz boost | Continuous, global | **Exact** | (1.7.34) | Spacetime unity |
| Electric charge | U(1) gauge | Continuous, local | **Exact** | (1.7.38), (1.7.39) | Duality |
| CPT | Lorentz + QFT | Discrete | **Exact** | (1.7.48) | Duality |
| Baryon number | Approx. global U(1)_B | Continuous, global | **Approximate** | (1.7.47) | Duality (broken by anomaly) |
| Lepton number | Approx. global U(1)_L | Continuous, global | **Approximate** | (1.7.47) | Duality (broken by anomaly) |
| Chiral charge | Axial U(1)_A | Continuous, global | **Anomalous** | (1.7.53) | — (broken by quantum effects) |

### 7.7.2 What Entropy Is Not

A common confusion: *Is entropy conservation a Noether result?*

No. Entropy is *not* a conserved Noether charge. Entropy increases (Second Law), which means there is no symmetry of the action that produces it as a conserved current. The Second Law arises from the *Degradation Principle* (Principle 4), not from the *Symmetry Principle* (Principle 3).

More precisely:

- **Conservation laws** (energy, momentum, charge): arise from *symmetries* via Noether's theorem. These are *exact* statements about what does not change.
- **The Second Law** (entropy increase): arises from *initial conditions* combined with *statistics*. It is a statement about the *direction* of change, not the absence of change.

The distinction matters because it prevents a false paradox. Energy is conserved *and* entropy increases — there is no contradiction. Energy conservation says the total stays the same; entropy increase says the total gets redistributed in an increasingly disordered way. Conservation governs the *amount*; the Second Law governs the *arrangement*.

We will formalize this fully in Chapter 11 (Thermodynamics from Zone Separation), where the Second Law is derived from the statistics of zone mixing.

### 7.7.3 Boxed Key Results for Volume 2

Volume 2 (Forces and Fields) will derive force laws under the constraint that they conserve every exact quantity in Table 7.1. The following boxed results are the precise statements that Volume 2 will cite:

$$\boxed{\text{Energy: } \nabla_\mu T^{\mu 0}_{\text{eff}} = 0 \quad \Rightarrow \quad E_{\text{total}} = \text{const}} \tag{1.7.57}$$

$$\boxed{\text{Momentum: } \nabla_\mu T^{\mu i}_{\text{eff}} = 0 \quad \Rightarrow \quad P^i_{\text{total}} = \text{const}} \tag{1.7.58}$$

$$\boxed{\text{Angular Momentum: } \nabla_A M^{A,ij} = 0 \quad \Rightarrow \quad L^k_{\text{total}} = \text{const}} \tag{1.7.59}$$

$$\boxed{\text{Charge: } \nabla_\mu j^\mu_{\text{em}} = 0 \quad \Rightarrow \quad Q_{\text{total}} = \text{const}} \tag{1.7.60}$$

$$\boxed{\text{CPT: } \mathcal{L} = \mathcal{L}^{\text{CPT}} \quad \Rightarrow \quad m_{\text{particle}} = m_{\text{antiparticle}}} \tag{1.7.61}$$

Any force law that violates these constraints is *wrong* — regardless of how elegant it appears. These are the non-negotiable boundary conditions that God's character imposes on physics.

### 7.7.4 Experimental Verification of Exact Conservation Laws

Our framework predicts that the conservation laws in Table 7.1 marked "exact" are mathematically exact — not merely very good approximations. Experiment cannot prove exact conservation, but it can set bounds on how precisely conservation holds. The current experimental limits are extraordinary:

**Table 7.2: Experimental Bounds on Conservation Law Violations**

| Conservation Law | Observable | Current Bound | Source |
|-----------------|-----------|---------------|--------|
| Energy | Energy non-conservation per interaction | $|\Delta E / E| < 10^{-15}$ | Particle collider precision |
| Momentum | Momentum non-conservation per collision | $|\Delta p / p| < 10^{-11}$ | LEP/LHC beam experiments |
| Angular momentum | Anomalous spin precession | $|\Delta L / L| < 10^{-12}$ | Penning trap measurements |
| Electric charge | Charge non-conservation (electron decay) | $|\Delta Q| < 10^{-21} e$ | Electron lifetime > $6.6 \times 10^{28}$ years |
| CPT | Particle-antiparticle mass difference | $|m_K - m_{\bar{K}}| / m_K < 6 \times 10^{-19}$ | Neutral kaon system |
| Baryon number | Proton decay | $\tau_p > 10^{34}$ years | Super-Kamiokande |

Every one of these bounds is consistent with exact conservation. No violation has ever been observed for the laws we mark as "exact" in Table 7.1. The approximate laws (baryon number, lepton number) are observed to hold to extraordinary precision at low energies, but our framework predicts they are violated by quantum anomalies at rates consistent with the bounds above.

These experimental results are not inputs to our theory. They are *predictions*. The zone manifold's symmetries mathematically guarantee exact conservation of energy, momentum, angular momentum, and charge. If any future experiment detected a violation of these laws, it would falsify the framework — specifically, it would mean the zone manifold lacks the corresponding symmetry, which would require revising the axioms of Chapter 1.

### 7.7.5 Forward Look: Chapter 8

This chapter established WHAT is conserved and WHY. Chapter 8 will take the complementary step: expressing the Five Governing Principles themselves as mathematical constraints on the action. Where Chapter 7 derived conservation laws *from* the action's symmetries, Chapter 8 will show how the Five Principles *restrict* which actions are physically allowed. The two chapters together form a complete system: Chapter 7 tells you what any valid theory must conserve; Chapter 8 tells you what any valid theory must satisfy.

[FIGURE: Fig 1.7.3 — Conservation Law Family Tree. Root: Symmetry Principle (Axiom 3). First branch: Continuous Symmetries → Noether's First Theorem → Energy (Eternality), Momentum (Omnipresence), Angular Momentum (Impartiality), Charge (Duality). Second branch: Local Gauge Symmetries → Noether's Second Theorem → Bianchi Identities → Covariant Conservation. Third branch: Discrete Symmetries → CPT Theorem → Particle-Antiparticle Equality. Fourth branch (dashed): Approximate Symmetries → B, L conservation (with anomaly corrections noted).]

---

## 7.8 Problems

### Computational Problems

**Problem 7.1.** *Noether current for a real scalar field.*
Consider a real scalar field $\phi$ with Lagrangian $\mathcal{L} = \frac{1}{2} \partial_\mu \phi \, \partial^\mu \phi - \frac{1}{2} m^2 \phi^2$. Under time translation $t \to t + \epsilon$, compute the Noether current $j^\mu$ explicitly. Verify that $\partial_\mu j^\mu = 0$ on shell using the Klein-Gordon equation.

**Problem 7.2.** *Stress-energy tensor verification.*
Starting from the Waters Above Lagrangian density $\mathcal{L}_A = \frac{1}{2} \partial_\mu \Psi_A \, \partial^\mu \Psi_A - V(\Psi_A)$, derive the stress-energy tensor $T^{\mu\nu}_A$ using the Noether procedure (not the Hilbert definition). Show that $T^{00}_A = \frac{1}{2}(\dot{\Psi}_A)^2 + \frac{1}{2}(\nabla\Psi_A)^2 + V(\Psi_A)$ is positive-definite for $V \geq 0$.

**Problem 7.3.** *Killing vector verification.*
Verify that $K^\mu = (1, 0, 0, 0)$ is a Killing vector of the FLRW metric $ds^2 = -c^2 dt^2 + a^2(t)(dx^2 + dy^2 + dz^2)$ by computing the Lie derivative $\mathcal{L}_K g_{\mu\nu}$. Where does this computation break down if $a = a(t)$? Reconcile with the fact that energy is still conserved in cosmology. (Hint: the Killing equation fails for the full time-dependent metric, but the action for the matter fields can still be time-translation invariant.)

**Problem 7.4.** *Angular momentum of a rotating Waters configuration.*
Consider a Waters Below field with angular dependence $\Psi_B(r, \theta) = f(r) e^{im\theta}$ in polar coordinates. Compute the angular momentum $L_z$ using Eq. (1.7.33). Show that $L_z = m \int r \, dr \, |\partial_r f|^2$ (up to constants).

**Problem 7.5.** *Charge from U(1) symmetry.*
For the complex Waters field $\Psi = \Psi_A + i\Psi_B$ with Lagrangian $\mathcal{L} = \partial_\mu \Psi^* \partial^\mu \Psi - m^2 |\Psi|^2$, apply Noether's theorem to the transformation $\Psi \to e^{i\alpha}\Psi$ and derive the conserved current. Verify that the charge $Q = i\int d^3x \, (\Psi^* \dot{\Psi} - \dot{\Psi}^* \Psi)$.

**Problem 7.6.** *Non-Killing extra dimensions.*
For the warped metric $ds^2 = e^{2A(\xi)}(-c^2 dt^2 + dx^2) + d\xi^2$ in 3D (one spatial dimension plus one extra), compute $\mathcal{L}_{\partial_\xi} g_{AB}$ explicitly. Show it is proportional to $A'(\xi)$ and therefore vanishes only for $A = \text{const}$ (flat extra dimension).

**Problem 7.7.** *Total energy in the two-Waters system.*
Consider the combined Lagrangian $\mathcal{L} = \mathcal{L}_A + \mathcal{L}_B + G_{\text{int}}\Psi_A \Psi_B$. Derive the total stress-energy tensor $T^{00}_{\text{total}}$ and show that $dE_{\text{total}}/dt = 0$ even though $dE_A/dt \neq 0$ and $dE_B/dt \neq 0$ individually.

**Problem 7.8.** *Conserved charges of the Poincaré group.*
Starting from the 10 Killing vectors of Minkowski spacetime (4 translations, 3 rotations, 3 boosts), construct all 10 conserved charges for a free scalar field. Verify that they satisfy the Poincaré algebra: $[P^\mu, P^\nu] = 0$, $[M^{\mu\nu}, P^\rho] = \eta^{\mu\rho} P^\nu - \eta^{\nu\rho} P^\mu$.

### Conceptual Problems

**Problem 7.9.** *Why no extra-dimensional charges?*
Explain in your own words (citing specific equations) why the warp factors $A(\xi,\eta)$ and $B(\xi,\eta)$ prevent the extra dimensions from contributing conserved charges. What would happen physically if these factors were constant (flat extra dimensions)?

**Problem 7.10.** *Why CPT but not CP?*
Using the CPT theorem and the observed CP violation in kaon decays, explain why T violation must also exist. What does this imply about time-reversal symmetry in particle physics versus the macroscopic arrow of time?

**Problem 7.11.** *Entropy is not a Noether charge.*
A colleague claims "the Second Law is just another conservation law, like energy conservation." Write a careful refutation. Identify the specific mathematical property that energy has (and entropy lacks) that makes energy a Noether charge.

**Problem 7.12.** *Theological grounding.*
For each of the four exact conservation laws (energy, momentum, angular momentum, charge), identify the divine attribute that generates the corresponding symmetry. Explain in one paragraph each why the conservation law would fail if the divine attribute were absent.

**Problem 7.13.** *Conservation in an expanding universe.*
In an FLRW cosmology with scale factor $a(t)$, the naive energy $E = \int d^3x \, T^{00}$ is NOT conserved (photons redshift, losing energy). How is this consistent with our derivation? (Hint: distinguish the Killing vector of the full metric from the Killing vector of the background plus perturbations.)

**Problem 7.14.** *Anomaly and pion decay.*
The neutral pion $\pi^0$ decays to two photons ($\pi^0 \to \gamma\gamma$) with a measured lifetime of $8.5 \times 10^{-17}$ s. Explain why this decay would be forbidden by chiral symmetry alone, and how the anomaly equation (1.7.53) permits it. What would the universe look like if the chiral anomaly did not exist?

### Challenge Problems

**Problem 7.15.** *Ward-Takahashi identity.*
Starting from the path integral formulation $Z = \int \mathcal{D}\phi \, e^{iS[\phi]}$, derive the Ward-Takahashi identity for U(1) symmetry: $\partial_\mu \langle j^\mu(x) \phi(y) \rangle = -i\delta^4(x-y) \langle \phi(y) \rangle$. Explain why this identity is the quantum version of Noether's theorem.

**Problem 7.16.** *Anomaly computation.*
Compute the triangle diagram contributing to the chiral anomaly. Show that the result is $\partial_\mu j^\mu_5 = \frac{e^2}{16\pi^2} F_{\mu\nu} \tilde{F}^{\mu\nu}$ by evaluating the linearly divergent integral with Pauli-Villars regularization.

**Problem 7.17.** *Precision bounds on conservation laws.*
Current experimental bounds on energy conservation violation are $|\Delta E / E| < 10^{-15}$ per interaction (from particle physics). On charge conservation, $|\Delta Q| < 10^{-21} e$ per electron lifetime. Convert these into bounds on the symmetry-breaking parameters in our framework: what minimum precision must the warp factors maintain to be consistent with observation?

**Problem 7.18.** *Conservation laws as constraints on Volume 2.*
Suppose you are constructing a force law $F = F(\Psi_A, \Psi_B, g_{\mu\nu})$ to describe the interaction between Waters Above and baryonic matter. Using only the conservation laws derived in this chapter, write down the most general set of constraints that $F$ must satisfy. How many independent components of $F$ are constrained by energy, momentum, and charge conservation together?

---

## Chapter Summary

This chapter has accomplished a single, powerful task: **deriving every conservation law of physics from the symmetries of the zone manifold.**

The results, in order:

1. **Noether's theorem** (Section 7.2): Every continuous symmetry of the action produces a conserved current. Proved in full for the zone manifold action $S_{\text{total}}$.

2. **Energy conservation** (Section 7.3): From time-translation symmetry, reflecting God's eternality. Exact.

3. **Momentum conservation** (Section 7.4): From spatial-translation symmetry, reflecting God's omnipresence. Exact.

4. **Angular momentum conservation** (Section 7.4): From rotational symmetry, reflecting God's impartiality. Exact.

5. **Charge conservation** (Section 7.5): From U(1) gauge symmetry, reflecting the Duality Principle. Exact.

6. **CPT invariance** (Section 7.5): From Lorentz invariance plus quantum field theory. Exact.

7. **Baryon and lepton number** (Section 7.5): From approximate global symmetries. Approximate — violated by quantum anomalies.

8. **No extra-dimensional charges** (Section 7.6): Because warp factors break extra-dimensional translation symmetry. This is a feature of the zone structure, not a deficiency.

9. **Anomalies** (Section 7.6): Some classical symmetries (chiral, baryon number) are broken by quantum corrections. This is physical and observable (pion decay, matter-antimatter asymmetry).

Every conservation law traces to a specific symmetry, which traces to a specific divine attribute. Standard physics catalogs these laws empirically. We have *derived* them. The reader now possesses not merely the *what* of conservation — but the *why*.

These conservation laws are the constraints that Volume 2 must respect when deriving force laws. Any candidate force law that violates energy, momentum, or charge conservation is automatically excluded — not by fiat, but by the geometry of the zone manifold itself.

---

*Next: Chapter 8 — The Five Governing Principles as Constraints, where we express the full theological-physical framework as variational constraints on the action.*
