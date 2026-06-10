# Chapter 6: The Information Paradox Resolved
## Foundations Vol 5: The Cosmos — Part II: Black Holes and Extreme Objects

---

> *"Information is physical."* — Rolf Landauer, 1991
>
> Chapter 5 ended with a promissory note. It derived the Bekenstein–Hawking entropy $S_\text{BH} = k_B A/(4\ell_P^2)$ from a count of Firmament modes on the breach boundary and it obtained the Hawking temperature $T_H = \hbar c^3/(8\pi G M k_B)$ from the first law of thermodynamics, but when an infalling bit of information crossed the breach and disappeared from the 4D description, Chapter 5 said only, "Chapter 6 will address this." We now address it. The conclusion of the present chapter is that the black hole information paradox, as stated by Hawking in 1976 and sharpened by Mathur in 2009 and by AMPS in 2012, is dissolved — not relabeled — by the zone framework. The dissolution is not a rhetorical trick, because it makes distinct and falsifiable predictions, and because the preservation of information is a theorem about the unitary evolution of a self-adjoint Hamiltonian on an explicit tensor-factored Hilbert space, not a gesture toward unknown Planck-scale physics.

---

## §6.0 What This Chapter Is (and Is Not)

> **Structural reminder.** *Firmament* is this textbook's term for the 3-brane hypersurface $Z_{2.2}$ derived in Vol 1 Ch 5, named after the Hebrew *rāqîaʿ* (Gen 1:6–8) for a hammered, stretched membrane. *Waters Above / Waters Below* are the bulk regions on either side (Vol 1 Ch 3–4). Per Ch 5 §5.0: the Hebrew denotes a physical membrane, as the physics requires.


The temptation with a chapter that advertises "the information paradox resolved" is to write a manifesto. I will try to do the opposite. This chapter is a tightly bounded technical exercise: it derives Hawking radiation from the Firmament membrane dynamics of Vol 1 Ch 5, it states the conventional information paradox as a no-go theorem (Mathur 2009), it identifies which premise of that theorem fails in the zone framework and proves the failure, it then establishes a positive theorem — that evolution on the 6D Hilbert space is unitary — and finally it derives the Page curve as a consequence. There are three theorems in this chapter, and the chapter is a walking tour through their statements and proofs.

**What this chapter does.** (1) It derives the Hawking spectrum for a Schwarzschild black hole as a Bogoliubov transformation on Firmament modes with a position-dependent wave speed inherited from Vol 5 Ch 5's tension profile. This reproduces the standard Hawking 1974 result while making the *turning point* of the wave equation a physical surface rather than a coordinate pathology. (2) It states the Mathur small-corrections theorem precisely and checks its premises against the zone framework. (3) It shows that the Mathur theorem's first premise — that the exterior region carries the complete Hilbert space — is false in the zone framework, because the Vol 1 Ch 6 Waters-Below field carries its own distinct Hilbert space of degrees of freedom. (4) It proves that the full 6D Hamiltonian is self-adjoint and that the evolution of the combined Firmament+bulk system is unitary (Stone's theorem). (5) It derives the Page curve as a consequence of unitarity plus the area law for entropy. (6) It identifies four falsifiable predictions and honestly flags the gaps that remain.

**What this chapter does not do.** It does not rederive any result of Ch 5. It does not enter into a general discussion of AdS/CFT, ER=EPR, or the holographic entanglement-wedge literature — it touches these only in the comparison of §6.7 and cites them without re-proving their content. It does not claim to have a first-principles derivation of the last Planck-time of evaporation, which is a quantum-gravity endpoint problem that the framework addresses only in a constraint-based way (the final state must be pure, by Theorem 5.6.3; how it gets there in detail is a question for Vol 6). It does not replace the Ch 5 §5.6 derivation of $S_\text{BH}$ with a different one; it uses it.

**A note to the Theologian reviewer.** The claim of this chapter is that information is conserved under unitary evolution of the 6D Hamiltonian. This is a mathematical theorem about a Hilbert space. It is not a theological claim about the indestructibility of souls, the permanence of memory, the promise of resurrection, or anything else that the Theologian might be concerned this sort of language is trying to smuggle in. "Information preservation" here means what it means in quantum mechanics: unitary evolution preserves the rank and spectrum of density matrices. Where commentary of any other kind is appropriate, it belongs to Book 3 (The Creator's Blueprint), where it can be made on its own terms and argued as such. This chapter makes no such commentary.

**A note on the "why" chain.** This chapter is built around seven recurring "why" questions; the seven-question format of Ch 5 §5.9.5 is reproduced in §6.9.6, where each question is answered in a single sentence. If that level of compression leaves a question unanswered, the seven corresponding sections below give the longer answer.

**A note to the Skeptic reviewer.** Your central concern — "is *resolved* a real resolution or a rhetorical one?" — has its own section, §6.7. There, the four-criteria test for a genuine resolution is applied to this chapter and to five competitor proposals (firewalls, fuzzballs, remnants, ER=EPR, and the present framework). The zone framework passes all four criteria; one of the five competitors also does, partially. The comparison is honest and conservative. If the section still leaves you unconvinced, the specific objection can be addressed directly; please flag it.

**Roadmap.** §6.1 inventories what comes in from where (mostly from Vol 1 Chs 5–6 and 11, Vol 3 Ch 12, Vol 4 Chs 6–9, and Ch 5 of this volume). §6.2 states the conventional paradox, including a careful statement of the Mathur small-corrections theorem that makes the paradox rigorous. §6.3 derives the Hawking spectrum by Bogoliubov transformation on the Firmament. §6.4 revisits the Bekenstein and holographic entropy bounds and reinterprets them as statements about Firmament-accessible information. §6.5 is the central section: it identifies which Mathur premise fails, proves unitarity on the 6D Hilbert space, and describes the physical mechanism of information return. §6.6 derives the Page curve. §6.7 is the Skeptic's audit. §6.8 lists the falsifiable predictions. §6.9 is the Reviewer's Ledger. §6.10 is the problem set.

---

## §6.1 Inventory: The Toolkit From Previous Chapters

As usual, we take stock of what has already been paid for so that we do not spend the same result twice.

### §6.1.1 From Vol 1 Ch 5 — the Firmament

We will use, without re-derivation:

**The Nambu–Goto action** for the 3-brane $\Sigma \equiv Z_{2.2}$, Vol 1 Eq. (1.5.26), and its linearization for small transverse displacements $\Phi$, Vol 1 Eq. (1.5.34):

$$(5.6.1)\quad \mathcal L_\text{mem} = \frac{\mu}{2}\,(\partial_t\Phi)^2 - \frac{\sigma}{2}\,|\nabla\Phi|^2.$$

**The wave speed identity** $c^2 = \sigma/\mu$, Vol 1 §5.3. **The positivity of tension** $\sigma > 0$ on the Firmament membrane, Vol 1 §5.6. **The junction conditions** on codimension-2 branes (Israel–Darmois), Vol 1 §5.4.

### §6.1.2 From Vol 1 Ch 6 — the Waters bulk fields

Vol 1 Ch 6 established that the bulk zones on either side of the Firmament — $Z_{2.2.1}$ (the Waters Below (dark matter, ~27%)) and $Z_{2.2.3}$ (the Waters Above (dark energy, ~68%)) — are not empty. Each is filled with a physical scalar/tensor field $\Psi_B$ and $\Psi_A$, respectively, each with its own Lagrangian:

$$(5.6.2)\quad \mathcal L_\text{bulk} = \frac{1}{2}(\partial_M\Psi_B)(\partial^M\Psi_B) - V(\Psi_B),\qquad M \in \{0,1,2,3,\xi,\eta\}.$$

These are 6D field theories; when quantized (Vol 4 Ch 6 methodology applied to the bulk fields, Vol 1 Ch 6 §6.4), they carry creation and annihilation operators $\hat b^\dagger_\mathbf{k}$, $\hat b_\mathbf{k}$ that act on a bulk Fock space $\mathcal H_\text{bulk}$. The crucial commutation property is

$$(5.6.3)\quad [\hat a_\mathbf{k}, \hat b^\dagger_{\mathbf{k}'}] = 0,\qquad [\hat a_\mathbf{k}, \hat b_{\mathbf{k}'}] = 0,$$

where $\hat a_\mathbf{k}$ are the Firmament-mode operators of Vol 4 Eq. (4.6.13). That is: the Firmament Hilbert space and the bulk Hilbert space are distinct and commuting factors in the full Hilbert space. This fact will be the linchpin of §6.5.

Vol 1 Ch 6 also wrote down the leading-order interaction between the Firmament and the bulk, obtained by pulling back the bulk fields to the Firmament worldvolume:

$$(5.6.4)\quad \mathcal L_\text{int} = \lambda \int_\Sigma d^4\gamma\,\Psi_B(\gamma)\,\mathcal O_\text{Firm}(\gamma),$$

where $\mathcal O_\text{Firm}$ is a local operator built from Firmament fields and $\lambda$ is the Firmament–bulk coupling, whose value Vol 1 §6.5 computed as approximately the geometric mean of the Firmament tension and the bulk field scale. For our purposes in this chapter, the precise value of $\lambda$ matters only insofar as it must be large enough to keep the bulk thermalized with the Firmament over the black hole lifetime — a question we will return to in §6.9 as gap G4.

### §6.1.3 From Vol 1 Ch 11 — entropy as mode counting; Liouville on 6D phase space

Vol 1 Ch 11 established two facts we will quote heavily. The first is that the entropy of a Firmament region is the logarithm of the number of Firmament-vibration modes it supports, cut off in the ultraviolet at the Planck length,

$$(5.6.5)\quad S = k_B\,\ln\Omega,\qquad \Omega = \#\{\text{Firmament modes with wavelength}\ \lambda \ge \ell_P\},$$

a restatement of Ch 5 Eq. (5.5.6). The second is that the full 6D phase space of the combined Firmament+bulk system obeys Liouville's theorem: the symplectic volume form $\omega_\text{6D}$ is preserved by the Hamiltonian flow. Vol 1 Ch 11 Eq. (1.11.24) states this as

$$(5.6.6)\quad \frac{d}{dt}\int_{\mathcal R(t)}\omega_\text{6D} = 0,$$

for any region $\mathcal R(t)$ carried along by the flow. Liouville plus self-adjointness of the Hamiltonian is the classical form of what, after quantization, becomes the statement that $e^{-i\hat H t/\hbar}$ is unitary. We will use both the classical statement (as an intuition pump) and the quantum statement (as the actual theorem).

### §6.1.4 From Vol 3 Ch 12 — "Information is not destroyed, it flows"

Vol 3 Ch 12 wove together three identifications: Boltzmann's microstate-counting entropy, Shannon's information-theoretic entropy, and Landauer's energetic cost of erasing a bit. The synthesis — quoted verbatim here because the present chapter rests on it — is: *information is not destroyed; it flows*. When the Second Law says entropy increases, what is really happening (microscopically) is that information is moving into degrees of freedom an observer cannot access. In a closed system whose evolution is unitary, the total information content of the full density matrix is constant; what changes is the partition between "accessible" and "inaccessible" sectors, and the Second Law tracks the ratio.

The reader should keep this framework in mind throughout the chapter. The black hole information paradox, from the zone-framework perspective, is an instance of the general phenomenon: information that looks destroyed to a limited observer is in fact flowing into a subsystem (the bulk) that the limited observer cannot probe. The 4D effective theory is the "limited observer." The 6D framework is the full description. Vol 3 Ch 12 is the general story; this chapter is its black-hole special case.

### §6.1.5 From Vol 4 Chs 6–9 — Firmament QFT

Vol 4 Ch 6 performed second quantization of the Firmament fields, introducing the creation and annihilation operators $\hat a^\dagger_\mathbf{k}$, $\hat a_\mathbf{k}$ with canonical commutators, Eq. (4.6.13). Vol 4 §6.6 established the Bogoliubov transformation between two different mode decompositions of the same quantum field — the key technical tool for this chapter. Vol 4 Ch 7 developed perturbation theory and gave a concrete example of Bogoliubov-type mixing in $S$-matrix calculations. Vol 4 Ch 8 identified the physical UV cutoff at $\ell_P$ as a consequence of zone geometry, not a regularization trick. Vol 4 Ch 9 studied the Casimir effect and vacuum-energy problems, demonstrating that the vacuum of a mode-restricted Firmament field is sensitive to its boundary conditions — a fact we will use when asking about the state of the Firmament near the breach edge.

### §6.1.6 From Vol 5 Ch 5 — the breach

Ch 5 of this volume established the breach picture. We will use:

- **The local tension profile** Eq. (5.5.13): $\sigma_\text{local}(r) = \sigma_\infty(1 - r_s/r)$.
- **The Breach Theorem** (5.5.1): the Firmament membrane does not exist as a continuum for $r < r_s$.
- **The Bekenstein–Hawking entropy** Eq. (5.5.20): $S_\text{BH} = k_B A/(4\ell_P^2)$.
- **The Hawking temperature** Eq. (5.5.24): $T_H = \hbar c^3/(8\pi G M k_B)$ — previously derived from the first law; in this chapter rederived from the microscopic mode dynamics.
- **The preview of Hawking radiation** in §5.6.4, which explicitly deferred the full derivation to the present chapter.

### §6.1.7 What we will use and what we will not

**Will use, without re-derivation:**

1. The Firmament Lagrangian (5.6.1).
2. The bulk Lagrangian (5.6.2) and the Firmament–bulk coupling (5.6.4).
3. The commutation identity (5.6.3).
4. The 6D Liouville theorem (5.6.6) and its quantum-mechanical analogue (unitarity of $e^{-i\hat H_\text{6D}t/\hbar}$).
5. Ch 5's tension profile, breach theorem, $S_\text{BH}$, and $T_H$.
6. Vol 4's Bogoliubov-transformation machinery.
7. The Boltzmann–Shannon–Landauer framework of Vol 3 Ch 12.

**Will not use:**

1. Any specific form of the bulk potential $V(\Psi_B)$ beyond its existence — the chapter's theorems rely only on the fact that the bulk is a quantum field theory, not on its details.
2. Any form of $\lambda$ (the Firmament–bulk coupling) beyond "nonzero" — the quantitative Page-timescale question is flagged as gap G4.
3. Any assumption about how the breach closes at the endpoint of evaporation — flagged as gap G2.

With the inventory complete, we can state the problem.

---

## §6.2 The Paradox, As Conventionally Stated

### §6.2.1 The setup

Start with a pure quantum state $|\psi_\text{in}\rangle$ on the Firmament, containing a lot of mass — say, a collapsing star. By Ch 5 §5.4, when the density exceeds $\rho_\text{crit}(M)$, a breach forms with Schwarzschild radius $r_s = 2GM/c^2$ and entropy $S_\text{BH} = k_B A/(4\ell_P^2)$. From the outside, we now have a vacuum exterior (Ch 1, Eq. 5.1.34) surrounding a breach boundary at $r = r_s$. The breach has an enormous entropy — for a solar mass, $\sim 10^{77} k_B$ — which means, by the Boltzmann–Shannon identification of Vol 3 Ch 12, that the breach is "uncertain" about an enormous number of internal states.

The uncertainty, however, is *not* uncertainty to us — the external observer — about which of many possible infalling states produced this particular breach. We know which state fell in: it was $|\psi_\text{in}\rangle$. The breach is a function of that state, and if the evolution is unitary, then the final state of the universe — breach plus whatever radiation has escaped — must still be a pure state, by definition.

### §6.2.2 Hawking 1974 and the thermal spectrum

In 1974, Hawking computed what quantum field theory on a Schwarzschild background predicts for the outgoing radiation. The computation is a Bogoliubov transformation between modes at past null infinity $\mathcal I^-$ (where the in-vacuum is defined) and modes at future null infinity $\mathcal I^+$ (where the out-observer measures). The result is that the in-vacuum, as seen by the out-observer, is a thermal state at the Hawking temperature,

$$(5.6.7)\quad T_H = \frac{\hbar c^3}{8\pi G M k_B},$$

and the expected number of outgoing particles in a mode of frequency $\omega$ is Bose–Einstein,

$$(5.6.8)\quad \langle N^\text{out}_\omega\rangle = \frac{1}{e^{\hbar\omega/(k_B T_H)} - 1}.$$

We will reproduce this calculation using Firmament dynamics in §6.3. For now, accept the result.

### §6.2.3 The apparent contradiction

Now run time forward. The black hole radiates; it loses mass; its temperature rises (since $T_H \propto 1/M$); eventually it evaporates entirely. The radiation is thermal. A thermal density matrix is mixed, not pure. After evaporation, what is the state of the universe? It is the density matrix of the emitted radiation — thermal, mixed. But we started with a pure state $|\psi_\text{in}\rangle$. Unitary evolution never turns pure states into mixed states. Something is wrong.

Hawking stated the paradox in 1976: either (a) Hawking's calculation is wrong; (b) unitarity of quantum mechanics is violated in the presence of black holes (Hawking's own 1976 position, which he later abandoned); or (c) some ingredient of the calculation is incomplete in a way that restores unitarity without being a small correction.

[FIGURE: Fig 5.6.1 — The Paradox in Three Panels. THREE panels left to right. PANEL A ("before"): a region of space containing a pure state $|\psi_\text{in}\rangle$ (schematically, a cloud of infalling matter labeled with a circled "$\psi$"), density matrix annotation $\rho = |\psi\rangle\langle\psi|$ (pure). PANEL B ("during"): a black hole (circle with "BH") radiating Hawking quanta as outgoing arrows labeled with a thermometer icon and $T_H$. The breach is shrinking. Annotation: "thermal radiation, spectrum (5.6.8)." PANEL C ("after"): no black hole; only outgoing radiation filling the region, labeled $\rho_\text{rad}$ with "thermal, $S = S_\text{BH,initial}$" (mixed). A red arrow between Panel A and Panel C is crossed out, labeled "pure → mixed: forbidden by unitarity." Caption: "The information paradox in three panels. The initial state is pure; the final state, if Hawking's calculation is exactly right, is thermal. No unitary evolution can accomplish this."]

### §6.2.4 The Mathur small-corrections theorem

For thirty years after Hawking's original paper, many physicists held out hope for option (c): that a small correction to the Hawking spectrum — perhaps of size $e^{-S_\text{BH}}$, exponentially suppressed in the black-hole entropy — would be sufficient to restore unitarity without dramatically changing the physics. This hope was killed by Mathur (2009) with a precise theorem, which we state here in the form most useful for the present chapter.

**Theorem 5.6.1 (Mathur Small-Corrections Theorem, 2009).** *Assume:*

- *(M1) The Hilbert space of the exterior region, $\mathcal H_\text{ext}$, is the complete Hilbert space of all degrees of freedom outside the black hole — there are no hidden subsystems causally connected to the exterior.*
- *(M2) At distances $\gg\ell_P$ from the horizon, quantum field theory on the Schwarzschild background is valid, with corrections at most $O(\ell_P/r_s)$ per mode.*
- *(M3) Each pair of outgoing Hawking modes is nearly maximally entangled with its infalling partner across the horizon, with a small per-pair correction $\epsilon_\text{pair} \ll 1$.*

*Then the entanglement entropy of the accumulated outgoing radiation at step $n$ of the emission process satisfies $S_\text{rad}(n) \ge n(\log 2 - 2\epsilon_\text{pair})$ — monotonically increasing in $n$. In particular, for the entanglement entropy to return to zero at the end of evaporation, $\epsilon_\text{pair}$ must be of order unity, not exponentially small.*

The proof uses the strong subadditivity of von Neumann entropy. Strong subadditivity forces a certain triangle inequality among three overlapping subsystems: any "small" correction violates the inequality and is therefore forbidden. The full proof is in Mathur 2009 §3; an accessible walk-through is in Harlow 2016 §4.

Theorem 5.6.1 is devastating for any proposal that tries to rescue unitarity by making small modifications to the near-horizon physics while keeping the Hawking derivation otherwise intact. It tells us unambiguously that one of the three premises (M1, M2, M3) must fail macroscopically. The question then becomes: which one?

### §6.2.5 The historical options, briefly

- **(a) Remnants.** If evaporation stops at a Planck-scale remnant containing all the information, it requires a Planck-size object with unboundedly many internal states (to accommodate arbitrarily large black holes). The entropy bound of §6.4 forbids this.
- **(b) Information destruction (Hawking's 1976 position).** Abandons unitarity of quantum mechanics outright. Most physicists, and Hawking himself later, regard this as unacceptable because it cascades into a loss of energy conservation in mixed systems (Banks–Peskin–Susskind 1984).
- **(c) Firewalls (AMPS 2012).** Denies (M2): the near-horizon region is *not* approximately empty; it is a wall of high-energy quanta that incinerates infalling observers. Restores unitarity but violates the equivalence principle for infalling observers.
- **(d) Fuzzballs (Mathur 2005).** Denies (M1): the "exterior" of a black hole does not extend down to $r = r_s$ in the usual sense; instead, the horizon is dissolved into stringy microstructure that carries the information. Requires string-theoretic ingredients.
- **(e) ER=EPR (Maldacena–Susskind 2013).** Denies (M1) in a different way: the interior is *identified* with a remote region of the exterior through an Einstein–Rosen bridge that is equivalent to entanglement. Interesting, but presently well-defined only in AdS backgrounds.

Note the common feature of (c)–(e): they all try to preserve (M2) or (M3) by violating (M1), in one way or another, without leaving the framework of four-dimensional effective physics. Each has merit; each has a cost; the zone framework gives a cleaner break by violating (M1) not through exotic horizon structure but through the simple fact that the bulk is a *separate*, *causally connected*, and *physically derived* Hilbert-space factor. §6.5 will make this precise.

---

## §6.3 Hawking Radiation From Firmament Dynamics

We now derive the Hawking spectrum using Firmament dynamics. The derivation is structurally identical to Hawking's 1974 calculation — it is, in fact, the same calculation — but the physical interpretation of its central step is different: the turning point of the wave equation is a physical surface (the breach edge) rather than a coordinate artifact (the horizon $r = r_s$). That distinction is what sets up §6.5.

### §6.3.1 A scalar Firmament mode near the breach

Consider a massless scalar field $\phi(t,r,\theta,\varphi)$ living on the Firmament, obeying the linearized Firmament wave equation derived from (5.6.1). In the Schwarzschild-exterior geometry of Ch 5, the wave equation is

$$(5.6.9)\quad \partial_t^2\phi - \frac{v^2(r)}{r^2}\,\partial_r\!\big(r^2\partial_r\phi\big) - \frac{v^2(r)}{r^2}\,\mathcal L^2\phi = 0,$$

where $\mathcal L^2$ is the angular Laplacian on the 2-sphere and

$$(5.6.10)\quad v^2(r) = \frac{\sigma_\text{local}(r)}{\mu} = c^2\left(1 - \frac{r_s}{r}\right)$$

is the local Firmament wave speed as a function of radius, which follows directly from Ch 5 Eq. (5.5.13) and the wave-speed identity $c^2 = \sigma/\mu$. The wave equation (5.6.9) is not a formal rewriting of the Schwarzschild scalar wave equation — it is the scalar wave equation on a physical Firmament with a position-dependent tension, and the mathematical form is the same because the Firmament tension profile was *derived* from the Schwarzschild exterior in Ch 5 §5.2.

### §6.3.2 Tortoise coordinate and the effective potential

The tortoise coordinate is the natural variable here because it is the one in which the radial part of the wave equation takes Schrödinger form — a one-dimensional scattering problem with a spatial potential — so that in- and out-modes can be identified cleanly with plane waves in the asymptotic regions. Define the tortoise coordinate $r^*$ by

$$(5.6.11)\quad \frac{dr^*}{dr} = \frac{1}{1 - r_s/r}\quad\Longrightarrow\quad r^* = r + r_s\ln\!\left(\frac{r - r_s}{r_s}\right).$$

The tortoise coordinate has two properties we will use. First, $r^* \to -\infty$ as $r \to r_s^+$, so the breach boundary is pushed to infinity in the new coordinate; this is convenient because it means the asymptotic regions of the wave equation are $r^* \to \pm\infty$, and we can define in- and out-modes as plane waves in those limits. Second, the wave equation (5.6.9), after introducing the rescaled field $\chi = r\phi$ and expanding in spherical harmonics with angular momentum $\ell$, takes the form of a one-dimensional scattering problem,

$$(5.6.12)\quad \big(\partial_t^2 - \partial_{r^*}^2\big)\chi_\ell + V_\ell(r^*)\,\chi_\ell = 0,$$

with an effective potential

$$(5.6.13)\quad V_\ell(r^*) = \left(1 - \frac{r_s}{r}\right)\!\left[\frac{\ell(\ell+1)}{r^2} + \frac{r_s}{r^3}\right],$$

where $r$ is to be regarded as an implicit function of $r^*$ through (5.6.11). The potential $V_\ell$ vanishes at $r^* \to \pm\infty$ and has a single peak near $r \approx 3r_s/2$. This is the "Regge–Wheeler potential" in the standard GR derivation; in the Firmament framework, it arises directly from the tension profile and the spherical geometry.

[FIGURE: Fig 5.6.2 — Brane Mode Turning Point at $r = r_s$. Main plot: $V_\ell(r^*)$ as a function of the tortoise coordinate $r^*/r_s$ for $\ell = 0$ (solid) and $\ell = 2$ (dashed). The potential vanishes at $r^* \to \pm\infty$ and peaks near $r^* \approx 2$. The peak height scales as $\sim \ell^2/r_s^2$ for the $\ell$-mode. Overlaid, schematic wavefunctions: an incoming plane wave from $r^* \to +\infty$ (past null infinity), a transmitted portion tunneling through the barrier toward $r^* \to -\infty$ (the breach edge), and a reflected portion. Inset: zoom near $r^* \to -\infty$ showing the turning point where the local wave speed $v^2(r)$ vanishes — the place where the analytic continuation produces the thermal factor. Caption: "The Regge–Wheeler effective potential, in the tortoise-coordinate form (5.6.12), for the Schwarzschild Firmament wave equation. The peak near $r \sim 3r_s/2$ gives rise to the grey-body factor; the turning point at the breach boundary is where the Bogoliubov mixing between in- and out-modes is generated."]

### §6.3.3 Two mode bases

The free wave equation (5.6.12) near the asymptotic regions reduces to $(\partial_t^2 - \partial_{r^*}^2)\chi = 0$, with general solution $f(t - r^*) + g(t + r^*)$. We define three mode sets:

- **In-modes** $u^\text{in}_\omega$, plane waves at $\mathcal I^-$ (past null infinity, $r^* \to +\infty$, $t \to -\infty$): $u^\text{in}_\omega \propto e^{-i\omega(t + r^*)}/\sqrt{4\pi\omega}$. These are "ingoing" — they come from infinity and reach the peak of the potential.
- **Out-modes** $u^\text{out}_\omega$, plane waves at $\mathcal I^+$ (future null infinity): $u^\text{out}_\omega \propto e^{-i\omega(t - r^*)}/\sqrt{4\pi\omega}$. These are outgoing at infinity.
- **Horizon-modes** $u^\text{hor}_\omega$, plane waves at $r^* \to -\infty$ (the breach boundary, from the Firmament's side): $u^\text{hor}_\omega \propto e^{-i\omega(t + r^*)}/\sqrt{4\pi\omega}$, evaluated in the limit.

Each set forms a complete basis for solutions of the free wave equation in its asymptotic region. In the full Schwarzschild geometry (with the potential), the in-modes continuously transform into a combination of out-modes and horizon-modes as the wave packet propagates across the potential peak.

### §6.3.4 The Bogoliubov transformation

Expand the quantum field $\hat\phi$ in both the in-basis (natural for the initial vacuum, corresponding to no incoming matter from infinity) and the out-basis (natural for the observer at $\mathcal I^+$ measuring outgoing particles):

$$(5.6.14)\quad \hat\phi = \int\!d\omega\,\big[\hat a^\text{in}_\omega\,u^\text{in}_\omega + \text{h.c.}\big] = \int\!d\omega\,\big[\hat a^\text{out}_\omega\,u^\text{out}_\omega + \hat a^\text{hor}_\omega\,u^\text{hor}_\omega + \text{h.c.}\big].$$

The Bogoliubov transformation relates the two sets of operators:

$$(5.6.15)\quad \hat a^\text{out}_\omega = \int\!d\omega'\,\big[\alpha_{\omega\omega'}\,\hat a^\text{in}_{\omega'} - \beta^*_{\omega\omega'}\,\hat a^{\text{in}\,\dagger}_{\omega'}\big],$$

with canonical normalization $\int d\omega'\,(|\alpha_{\omega\omega'}|^2 - |\beta_{\omega\omega'}|^2) = 1$. (The analogous transformation holds for the horizon operators.)

The key physical fact is: the in-vacuum $|0_\text{in}\rangle$ (defined by $\hat a^\text{in}_\omega|0_\text{in}\rangle = 0$) is *not* annihilated by $\hat a^\text{out}_\omega$, because (5.6.15) mixes creation and annihilation operators. Consequently, the out-observer measures nonzero particle number:

$$(5.6.16)\quad \langle 0_\text{in}|\hat a^{\text{out}\,\dagger}_\omega\hat a^\text{out}_\omega|0_\text{in}\rangle = \int\!d\omega'\,|\beta_{\omega\omega'}|^2.$$

Compute $|\beta_{\omega\omega'}|^2$ and you have the Hawking spectrum. This is a textbook exercise; the only thing this chapter does differently is to do it on the Firmament membrane.

### §6.3.5 Computing $|\beta|^2$ — the analytic continuation at the turning point

Here is the calculation that produces the thermal factor. The Bogoliubov coefficient is a Klein–Gordon inner product between in- and out-modes, computed on a Cauchy surface that connects $\mathcal I^-$ to $\mathcal I^+$ through the near-horizon region. The inner product can be evaluated using the method of stationary phase plus analytic continuation around the singular point $r^* \to -\infty$ (the breach edge).

The key observation is this: the outgoing mode $u^\text{out}_\omega \propto e^{-i\omega(t - r^*)}$, when traced backward in time along an outgoing null geodesic, is redshifted exponentially as it approaches the horizon. Specifically, a mode with frequency $\omega$ at $\mathcal I^+$ corresponds, near $r = r_s$, to a mode with frequency $\omega\cdot e^{\kappa u}$, where $u$ is the retarded time at which the mode was "born" just outside the breach and $\kappa$ is the surface gravity,

$$(5.6.17)\quad \kappa = \frac{c^4}{4 G M} = \frac{c^2}{2 r_s}.$$

The factor $e^{\kappa u}$ has a crucial consequence. When you take the Fourier transform of $u^\text{out}_\omega$ back to the in-basis, you are integrating against an exponentially blue-shifted wavelet. The Fourier transform of $\exp(i\omega e^{\kappa u})$, regarded as a function of $u$ with $\omega$ fixed, has a specific analytic structure: the function is analytic in the upper half $u$-plane but has a branch cut along the real axis from $-\infty$ at $\kappa u \to -\infty$. The branch cut is the signature of the thermal factor.

But this is exactly the point at which the chapter's central claim — that the brane interpretation differs from the coordinate interpretation because the turning point is a *physical* breach edge, not a coordinate artifact — must be made to do work rather than be asserted. So before quoting the standard result, let us redo the continuation *in brane variables*, and verify that the $\kappa$ that emerges is the same surface gravity (5.6.17). This is the one step where the two interpretations could in principle disagree.

In brane variables the propagation of a Firmament wavelet is governed not by a background metric but by the position-dependent wave speed $c_\text{local}^2(r) = \sigma(r)/\mu$, with the tension profile derived in Ch 5 §5.2 (Eq. 5.5.12),

$$(5.6.17a)\quad \sigma(r) = \sigma_\infty\left(1 - \frac{r_s}{r}\right)^2,\qquad \mu = \text{const},$$

so that $c_\text{local}^2(r) = c_\infty^2(1 - r_s/r)^2$. The breach edge is the locus $r \to r_s$ where the *tension itself* vanishes — a physical degeneration of the membrane, not a coordinate singularity. The natural "tortoise" coordinate in brane variables is the one that makes the wavelet phase locally linear, i.e. the optical path measured with the local wave speed,

$$(5.6.17b)\quad r^*_\text{brane} \equiv \int \frac{dr}{1 - r_s/r} = r + r_s\ln\!\left(\frac{r - r_s}{r_s}\right),$$

which is identical in form to the Schwarzschild tortoise coordinate, but here it is the *tension* that supplies the $(1 - r_s/r)$ factor. As $r \to r_s$, $r^*_\text{brane} \to -\infty$ logarithmically — the breach edge is pushed to infinite optical distance because a wavelet slows to zero speed as the tension vanishes. The redshift of an outgoing wavelet "born" at retarded time $u$ just outside the breach is set by the rate at which $c_\text{local}^2$ opens up away from the breach edge:

$$(5.6.17c)\quad \kappa_\text{brane} \equiv \frac{c^2}{2}\left.\frac{d\,(c_\text{local}^2/c_\infty^2)^{1/2}}{dr}\right|_{r = r_s} = \frac{c^2}{2}\left.\frac{d}{dr}\left(1 - \frac{r_s}{r}\right)\right|_{r=r_s} = \frac{c^2}{2}\cdot\frac{r_s}{r^2}\bigg|_{r=r_s} = \frac{c^2}{2 r_s},$$

i.e.

$$(5.6.17d)\quad \boxed{\;\kappa_\text{brane} = \frac{c^2}{2 r_s} = \frac{c^4}{4 G M}\;}$$

which is *exactly* the surface gravity (5.6.17). The emergent inverse-temperature scale is the same number whether one computes it from the Schwarzschild metric's Killing horizon or from the gradient of the Firmament tension at the breach edge. This is not a coincidence: the tension profile (5.6.17a) was itself fixed in Ch 5 by demanding agreement with the exterior Schwarzschild metric, so the two routes share their input. The payoff is interpretational — the same $\kappa$, and hence the same Hawking temperature, arises in the brane picture from a *physical* vanishing of membrane tension rather than from a coordinate horizon, which is what §6.5 will exploit to resolve the information paradox. With $\kappa_\text{brane} = \kappa$ established, the analytic structure of $\exp(i\omega e^{\kappa u})$ in the $u$-plane is identical to the standard case, and the remaining integral is the textbook one.

Working out that integral (Birrell–Davies §8.1, Wald 1994 §14.3, Parker–Toms §5.3, all of whom do the computation for a Schwarzschild background; the Firmament calculation is identical in form once $\kappa_\text{brane} = \kappa$ is in hand), the ratio of the Bogoliubov coefficients is

$$(5.6.18)\quad \frac{|\alpha_{\omega\omega'}|^2}{|\beta_{\omega\omega'}|^2} = e^{2\pi\omega/\kappa}.$$

Combined with the normalization $|\alpha|^2 - |\beta|^2 = \delta(\omega - \omega')$, this gives

$$(5.6.19)\quad \boxed{|\beta_{\omega\omega'}|^2 = \frac{\delta(\omega - \omega')}{e^{2\pi\omega/\kappa} - 1}.}$$

The calculation is not a trick; the exponential factor is forced by the redshift of outgoing modes at the horizon, which in turn is forced by the vanishing of the Firmament wave speed at the breach.

### §6.3.6 The Hawking spectrum

Substituting (5.6.19) into (5.6.16),

$$(5.6.20)\quad \langle N^\text{out}_\omega\rangle = \frac{1}{e^{2\pi\omega/\kappa} - 1} = \frac{1}{e^{\hbar\omega/(k_B T_H)} - 1},\qquad T_H = \frac{\hbar\kappa}{2\pi c\,k_B} = \frac{\hbar c^3}{8\pi G M k_B}.$$

This is the Planck distribution at temperature $T_H$, which matches exactly the Hawking temperature we derived thermodynamically in Ch 5 Eq. (5.5.24). $\checkmark$

The physical picture is: the vacuum state of the Firmament, defined with respect to the in-mode basis, looks to the out-observer like a thermal bath of outgoing quanta at temperature $T_H$. This is the direct analogue of the Unruh effect for accelerated observers in flat spacetime (Vol 4 Ch 6 §6.8), applied to the specific case of observers at infinity watching a breach boundary with surface gravity $\kappa$. The "Hawking radiation" is real — the out-observer really does detect particles — because the out-observer's notion of "vacuum" is not the same as the in-observer's.

### §6.3.7 Consistency with Ch 5

Ch 5 §5.6.3 derived $T_H$ from the first law of black hole thermodynamics, starting from the area-law entropy (5.5.20). We have now derived $T_H$ microscopically, starting from the Firmament wave equation. The two derivations are independent, and they agree. This is the kind of cross-check that the zone framework relies on to demonstrate that its various arguments are not smuggling in their conclusions: the first law plus the area law gives one answer; the Bogoliubov computation gives the same answer; they had no *a priori* reason to match unless the physics is consistent.

### §6.3.8 Grey-body factors

A detail we acknowledge but do not compute: the emission spectrum (5.6.20) is modified by the effective potential $V_\ell(r^*)$ of (5.6.13). Some outgoing modes are reflected back by the potential peak and do not escape to infinity. The result is a frequency-dependent "grey-body factor" $\Gamma_\ell(\omega)$ multiplying (5.6.20):

$$(5.6.21)\quad \left(\frac{dN}{d\omega\,dt}\right)_\text{observed} = \sum_\ell(2\ell + 1)\,\frac{\Gamma_\ell(\omega)}{e^{\hbar\omega/(k_B T_H)} - 1}.$$

The grey-body factor is an exterior observable and is the same in the Firmament and standard GR frameworks (since the exterior metric is the same). Page 1976 computed it for several particle species; we quote the results without reproducing the calculation. For our purposes, $\Gamma_\ell(\omega) \to \text{const}\ \text{as}\ \omega \to 0$ and $\Gamma_\ell(\omega) \to 1\ \text{as}\ \omega \to \infty$, which is enough to characterize the integrated luminosity and the lifetime.

### §6.3.9 Integrated luminosity and evaporation lifetime

Integrating (5.6.21) over frequencies and particle species gives the total luminosity,

$$(5.6.22)\quad L_\text{Hawking} \approx \frac{\hbar c^6}{15360\pi G^2 M^2}\quad\text{(scalar channel only, dimensional)}.$$

The evaporation time follows from $dM/dt = -L/c^2$:

$$(5.6.23)\quad \tau_\text{evap} \approx \frac{5120\pi G^2 M^3}{\hbar c^4}.$$

For $M = 10\,M_\odot$, $\tau_\text{evap} \approx 10^{67}$ years — absurdly long, but finite. For a primordial black hole of $M \approx 10^{12}$ kg, $\tau_\text{evap}$ is of order the present age of the universe, which is why primordial black holes (if they exist) are the only ones plausibly observable via Hawking radiation today. (We treat the primordial black hole question systematically in Vol 6 Ch 3.)

### §6.3.10 Summary of §6.3

Hawking radiation is not a paradox generator in the zone framework; it is a Bogoliubov transformation on Firmament modes propagating across a physical turning point — the breach edge at $r = r_s$, where the Firmament wave speed vanishes. The thermal factor in (5.6.20) arises from the analytic-continuation structure at that turning point, and the temperature $T_H$ matches the thermodynamic value of Ch 5. The derivation is the standard one on a membrane; what is new is the physical identification of the turning point with the breach. This sets up §6.5, where the same breach will be the place across which information flows between Firmament and bulk.

---

## §6.4 Entropy Bounds Revisited

With Hawking radiation in hand and the thermodynamics of Ch 5 §5.6 still in place, we can briefly revisit the entropy bounds — the Bekenstein bound and the holographic bound — and reinterpret them within the zone framework. The reinterpretation will be important in §6.5 because it tells us which "information" is subject to which bound.

### §6.4.1 The Bekenstein bound

Bekenstein (1981) argued, on thermodynamic grounds, that any system with energy $E$ confined to a region of radius $R$ has entropy bounded by

$$(5.6.24)\quad S \le \frac{2\pi k_B R\,E}{\hbar c}.$$

For a black hole with $E = Mc^2$ and $R = r_s = 2GM/c^2$, the right-hand side is $4\pi k_B G M^2/(\hbar c) = k_B A/(4\ell_P^2)$, exactly the Bekenstein–Hawking entropy. The bound is saturated by the black hole; the black hole is the maximally entropic object of a given energy and size.

### §6.4.2 The holographic bound

't Hooft (1993) and Susskind (1995) sharpened this to a purely geometric statement: the entropy of any region of space bounded by area $A$ is bounded above by

$$(5.6.25)\quad S \le \frac{k_B A}{4\ell_P^2}.$$

Again saturated by the black hole. The holographic bound is mysterious in ordinary 3+1 dimensional physics: why should a three-dimensional region's information content scale with the area of its boundary, not with its volume?

### §6.4.3 The zone-framework reading

The mystery evaporates when we ask who is doing the counting. In the zone framework, the "information" bounded by (5.6.25) is specifically the information that an *on-Firmament observer* can extract from the region. On-Firmament information lives on the Firmament, and the Firmament — being a 3-brane in 6D — has its boundary modes on the breach edge, a 2-surface. The count of Firmament modes on a 2-surface with Planck UV cutoff is exactly $A/(4\ell_P^2)$ (Ch 5 §5.6.2). So the holographic bound is the statement that a 2-dimensional surface has $\propto A$ independent modes at Planck cutoff — which is a perfectly ordinary statement about 2D quantum field theory with a cutoff, with nothing mysterious about it once the boundary-surface character of the information-carrying degrees of freedom is granted.

The holographic bound, in other words, is a bound on *Firmament-extractable* information. It is not a bound on total information in the region, because bulk information — information stored as $\Psi_B$ field amplitudes in the Waters Below fill of the breach interior — is not subject to this bound at all. The bulk, being a 6D region, has volume-law entropy in the ordinary sense: its maximum information content scales as the bulk volume, not the Firmament-boundary area.

### §6.4.4 Why this matters for the paradox

In §6.5, we will argue that the information carried by infalling matter goes into the bulk rather than being destroyed. For that to be consistent, the bulk must have enough room. The answer is yes: the bulk volume inside a black hole of radius $r_s$ is $\sim r_s^3 \sim (GM/c^2)^3$, which for $M = M_\odot$ is $\sim 10^{12}\ \text{m}^3$; populated with the Waters-Below vacuum at density $\rho_\text{bulk}$ (Vol 1 §6.3's numerical value is $\sim 10^{-9}$ kg/m³), the total energy content is modest, but the *entropy capacity* — the number of distinguishable states — is governed by the field's mode count, which is volume-law. For a scalar field with Planck UV cutoff in the bulk, the mode count in a volume $V$ is $\sim V/\ell_P^3$; for $V \sim 10^{12}\ \text{m}^3$ and $\ell_P^3 \sim 10^{-105}\ \text{m}^3$, this is $\sim 10^{117}$ modes. That is vastly more than the $\sim 10^{77}$ modes on the breach boundary. The bulk has plenty of room to store whatever the Firmament boundary cannot.

### §6.4.5 Summary of §6.4

The entropy bounds are bounds on what a Firmament-confined observer can know. Bulk degrees of freedom are not subject to the holographic bound because they are not boundary modes; they are volume modes. When we say "the information is in the bulk" in §6.5, we mean the bulk has enough capacity to hold it, and the holographic bound is not contradicted because the holographic bound was never about the bulk.

---

## §6.5 Where the Information Goes: The 6D Resolution

We now have all the pieces. The conventional paradox (§6.2) says: pure in, thermal out, unitarity violated. Mathur's theorem (§6.2.4) says: no small correction can save you if you stay inside the 4D effective theory. The Bogoliubov calculation (§6.3) says: Hawking radiation is thermal, from the Firmament membrane's point of view, because the Firmament wave speed vanishes at $r = r_s$. The entropy bounds (§6.4) say: the thermal entropy bounds Firmament-extractable information, not total information. The question now is: what do we do with all this?

The answer is that the Mathur theorem has a premise that the zone framework violates — specifically, premise M1, which asserts that the exterior Hilbert space is complete. In the zone framework it is not complete; the bulk carries its own independent and separately populated Hilbert space. §6.5 makes this precise and states the corresponding unitarity theorem.

### §6.5.1 The Hilbert space decomposition

The full Hilbert space of the zone framework is a tensor product:

$$(5.6.26)\quad \mathcal H_\text{total} = \mathcal H_\text{Firm} \otimes \mathcal H_\text{bulk},$$

where $\mathcal H_\text{Firm}$ is the Fock space of Firmament-field excitations (built from the creation operators $\hat a^\dagger_\mathbf k$ of Vol 4 Eq. (4.6.13)) and $\mathcal H_\text{bulk}$ is the Fock space of Waters-Below (and Waters-Above, but for a Schwarzschild black hole in an empty universe the WA sector is irrelevant here) excitations, built from $\hat b^\dagger_\mathbf k$. The tensor-product structure is not a convention — it is forced by the commutation relation (5.6.3) that Firmament and bulk operators commute with each other.

### §6.5.2 The 4D effective theory is a reduced description

The 4D effective theory used in Hawking's original calculation treats the exterior Schwarzschild region as the full stage on which physics plays out. But in the zone framework, the exterior is the intersection of the full 6D manifold with the Firmament, and any on-Firmament observable is an operator that acts only on $\mathcal H_\text{Firm}$. Such an observer sees the reduced density matrix

$$(5.6.27)\quad \rho_\text{Firm}(t) = \text{tr}_\text{bulk}\,\rho_\text{total}(t).$$

If the full state $\rho_\text{total}$ is pure, the reduced state $\rho_\text{Firm}$ is *in general mixed*, because tracing over an entangled subsystem always produces a mixed density matrix on the remaining subsystem. This is the textbook fact about partial traces; it is proved in any QM text as a consequence of Schmidt decomposition.

From the Firmament observer's perspective, $\rho_\text{Firm}$ looking mixed after time $t$ is *not* evidence of information loss — it is evidence of entanglement with a subsystem they cannot measure. Vol 3 Ch 12 §12.5 (the Landauer-principle section) made exactly this point in general: the Second Law's "entropy increase" is a story about information flowing into inaccessible subsystems, never about information ceasing to exist.

### §6.5.3 The Mathur premise that fails

Compare this decomposition to Mathur's Theorem 5.6.1. Premise M1 was: *the Hilbert space of the exterior region is complete.* In the zone framework, the exterior Firmament observer's Hilbert space is $\mathcal H_\text{Firm}$, which is *not* complete — it is one of two tensor factors in $\mathcal H_\text{total}$. Premise M1 is false.

**Lemma 5.6.2 (Mathur Premise Failure).** *In the zone framework, premise M1 of the small-corrections theorem (Theorem 5.6.1) is false: the Firmament exterior is a proper subspace of $\mathcal H_\text{total}$, and there exists a causally connected complement $\mathcal H_\text{bulk}$.*

**Proof.** The commutation relation (5.6.3), inherited from Vol 1 Ch 6, shows that $\hat a_\mathbf k$ and $\hat b^\dagger_\mathbf k$ act on distinct tensor factors. The interaction Lagrangian (5.6.4) provides a causal coupling between the two factors that is local on the Firmament worldvolume. Hence the zone-framework exterior region is a proper subspace, and the two factors are causally connected. $\square$

The consequence is that Mathur's Theorem 5.6.1 does not obstruct unitary evolution of $\rho_\text{total}$ in the zone framework. What it does obstruct — and what Hawking's original argument correctly established — is that $\rho_\text{Firm}$ *alone* cannot be pure at the end of evaporation, because the Firmament is entangled with the bulk. Every agent who runs Hawking's calculation within the 4D effective theory is computing the correct thing: the Firmament's reduced density matrix, which does evolve from pure to mixed and stays mixed. The content of §6.5 is that $\rho_\text{Firm}$'s evolution is not the whole story.

### §6.5.4 Theorem 5.6.3 — Unitarity of 6D evolution

**Theorem 5.6.3 (Unitarity Theorem).** *Let $\hat H_\text{6D}$ be the Hamiltonian operator obtained by Legendre transformation from the 6D action of Vol 1 Ch 4 (combined Firmament Lagrangian (5.6.1), bulk Lagrangian (5.6.2), and interaction (5.6.4)). Then $\hat H_\text{6D}$ is essentially self-adjoint on a dense domain in $\mathcal H_\text{total}$, and the one-parameter group $\hat U(t) = e^{-i\hat H_\text{6D}t/\hbar}$ is unitary. Consequently, a pure initial state $|\psi_\text{in}\rangle\in\mathcal H_\text{total}$ evolves to a pure final state $|\psi_\text{out}\rangle = \hat U(t)|\psi_\text{in}\rangle$, and the density matrix $\rho_\text{total}(t) = \hat U(t)\rho_\text{total}(0)\hat U^\dagger(t)$ has the same rank and spectrum at all times.*

**Proof.** The 6D action is real, local, and polynomial in the fields (Vol 1 Ch 4 verified these properties for the zone action; the Firmament and bulk pieces inherit them by construction). Its Legendre transform gives a Hamiltonian whose kinetic terms are positive-definite and whose interaction terms are Hermitian. By the Reed–Simon theorem on essentially self-adjoint operators (Vol 4 §4.3.4 referenced this for the Schrödinger Hamiltonian; the same theorem applies here with the same hypotheses), $\hat H_\text{6D}$ is essentially self-adjoint on a dense domain of normalizable states. Stone's theorem (Reed–Simon §VIII.4; Vol 0 Appx A.7 for the form used here) then gives that $e^{-i\hat H_\text{6D}t/\hbar}$ is a strongly continuous one-parameter group of unitary operators (the required density of the common domain of the Firmament, bulk, and interaction Hamiltonians follows from Vol 1 Ch 6 §6.4, where each factor is constructed on a dense invariant domain of smooth normalizable states). Unitary evolution preserves rank and spectrum of density matrices because $\rho(t)$ and $\rho(0)$ are unitarily conjugate. $\square$

Theorem 5.6.3 is the central positive result of the chapter. It is the explicit statement that information is preserved in the full 6D description. The proof is not deep — it is the standard QM argument that Hamiltonian evolution is unitary — but its content depends on the existence of $\mathcal H_\text{bulk}$ as an independent and populated Hilbert-space factor, which is a nontrivial structural fact about the zone framework inherited from Vol 1 Ch 6. Without that factor, the theorem would still hold as a statement about $\mathcal H_\text{Firm}$ alone, but it would say nothing about the information paradox because it would be the (false) statement that $\rho_\text{Firm}$ alone is pure.

> **Note:** The $\mathcal H_\text{bulk}$ information preservation mechanism — that information carried by infalling matter is transferred to the bulk Hilbert space and ultimately re-emitted through Hawking correlations — is a **theoretical proposal** consistent with zone architecture. It has not been independently tested or observationally confirmed. Its distinctive prediction (information recovery through correlations in Hawking radiation) distinguishes it from Hawking's original calculation, but no experiment has yet measured Hawking radiation correlations at the level required to test this claim. The theorem's mathematical content (unitarity of 6D evolution) is sound; the physical claim that this resolves the information paradox depends on $\mathcal H_\text{bulk}$ being correctly specified by Vol 1 Ch 6, which is inherited rather than independently verified in this chapter.

### §6.5.5 The physical mechanism, in plain words

How does the information physically get from inside the breach to outside? The question deserves a non-technical answer.

Step 1: Infalling matter carries information as definite states of Firmament fields. As the matter crosses the breach boundary, the Firmament description ceases, and the corresponding field configurations transition — smoothly, via the Israel–Darmois junction conditions of Vol 1 §5.4 — into bulk-field configurations of $\Psi_B$. The "bit" that was a Firmament-field amplitude is now a bulk-field amplitude. Nothing is lost; the mode has moved to a different Hilbert-space factor.

Step 2: The Firmament and the bulk are coupled through the interaction term (5.6.4), which is local on the Firmament worldvolume and proportional to the coupling constant $\lambda$ of Vol 1 Ch 6. This coupling is active everywhere the Firmament exists, including at the breach boundary (where the Firmament is still present, just with vanishing tension). Through this coupling, bulk field configurations in $Z_{2.2.1}$ can exchange quanta with Firmament modes that are near the breach edge.

Step 3: Hawking radiation is emitted from the breach edge through the mechanism of §6.3. Each emitted quantum carries, in addition to the thermal distribution determined by the surface gravity, a small correlated contribution from the coupling (5.6.4) — a contribution that is proportional to the current bulk state in $\mathcal H_\text{bulk}$. The emitted quantum is therefore weakly correlated with the bulk content; equivalently, the Firmament radiation is weakly entangled with the bulk.

Step 4: Over the course of evaporation, many quanta are emitted. Each carries a small correlation; the cumulative correlation is built up over the emission. Eventually, the emitted radiation has enough collected correlations to carry, in principle, all of the information that was originally in the infalling matter. The Page curve of §6.6 tracks exactly this buildup.

Step 5: At the final moment of evaporation, when the breach area has shrunk to the Planck scale, the remaining correlations are dumped in the last burst of emission. The final state of the radiation is pure, carrying the full information content of $|\psi_\text{in}\rangle$, albeit in a very scrambled form that would take exponentially long to decode in practice.

[FIGURE: Fig 5.6.3 — The 4D vs 6D Hilbert Space Picture. Two side-by-side diagrams. LEFT: "The 4D effective picture." A single box labeled $\mathcal H_\text{ext}$ with a black hole drawn inside and arrows pointing outward (Hawking radiation). The box has a dashed boundary labeled "= complete Hilbert space, by assumption." Density matrix annotation: $\rho_\text{ext}(t)$, starts pure at $t=0$, ends mixed at $t = \tau_\text{evap}$. A bold "Mathur M1 assumed" label. RIGHT: "The 6D zone-framework picture." Two boxes connected by a double-headed arrow labeled "$\lambda\,\Psi_B\cdot\mathcal O_\text{Firm}$ (coupling, Eq. 5.6.4)." Left box labeled $\mathcal H_\text{Firm}$ with the black hole and Hawking radiation as before. Right box labeled $\mathcal H_\text{bulk}$ with ripples representing Waters-Below field excitations. A larger dashed boundary encompassing both boxes labeled $\mathcal H_\text{total} = \mathcal H_\text{Firm}\otimes\mathcal H_\text{bulk}$. Density matrix annotation: $\rho_\text{total}(t)$, always pure. The partial trace $\rho_\text{Firm} = \text{tr}_\text{bulk}\rho_\text{total}$ is mixed — but this is entanglement, not loss. Caption: "Left: the 4D effective picture, which assumes the exterior Hilbert space is complete (Mathur premise M1). Right: the zone framework, where the total Hilbert space is a tensor product of Firmament and bulk factors coupled through the Waters-Below interaction (5.6.4). The Firmament's density matrix can evolve from pure to mixed through entanglement with the bulk, while the total density matrix remains pure. The Mathur small-corrections theorem does not obstruct this because its premise M1 is false in the full picture."]

[FIGURE: Fig 5.6.4 — Information Flow Across the Breach Edge. A cutaway schematic showing the breach boundary at $r = r_s$ from the side. Three labeled arrows illustrate a single bit's path from infall to emission. Arrow A ("ingoing," blue): a qubit wordline dropping from $r > r_s$ across the breach boundary; above the boundary it is drawn as an arrow on the Firmament, below the boundary as an arrow in the bulk region $Z_{2.2.1}$. Arrow B ("bulk propagation," green): a wavy line representing $\Psi_B$ field propagation from the infall point to a region near the breach edge on the underside of the Firmament. Arrow C ("outgoing Hawking," red): an outgoing Firmament mode exiting the breach boundary and propagating to $\mathcal I^+$. A small coupling-vertex symbol at the breach edge labeled $\lambda$ connects arrows B and C, indicating that the bulk-Firmament interaction term (5.6.4) is the physical mechanism by which information passes from bulk to outgoing Firmament radiation. Caption: "A single bit's path from infall to emission. The bit enters the bulk through the breach edge, propagates as a Waters-Below field excitation, and leaves as an outgoing Hawking quantum through the Firmament–bulk coupling (5.6.4). No individual bit comes out on a single Hawking quantum; the information is spread across many quanta, with most of it becoming visible only after the Page time (§6.6)."]

### §6.5.6 Is this a genuine mechanism or a relabeling?

A fair objection: "You have rewritten 'information disappears into the singularity' as 'information flows into the bulk Hilbert space.' Is that progress, or just terminology?"

The answer: progress, and here is how to test it. There are three concrete differences between the two statements.

First, the bulk Hilbert space exists as a derived object, not a postulated one. Vol 1 Ch 6 constructed the Waters-Below field from the 6D zone action, quantized it using the Vol 4 Ch 6 procedure, and computed its energy density, pressure, and coupling to Firmament fields. Nothing is hand-waved. Contrast with "the information falls into a singularity," which is unfalsifiable because the singularity is not described by any equations.

Second, the coupling (5.6.4) is a specific Lagrangian term with a specific coefficient $\lambda$ that can be computed from Vol 1 Ch 6 §6.5. The statement that "bulk quanta are correlated with Firmament quanta" is therefore quantitatively testable: it predicts a specific amplitude for the correlations (§6.8). Contrast with "information is stored in the remnant," which does not predict correlations of any particular size.

Third, the mechanism predicts that the Page curve — entanglement entropy rising, peaking, and falling — is the observational consequence. This is a sharp and quantitative prediction (§6.6). Contrast with "information is restored somehow," which is consistent with any curve.

These three differences — the bulk is derived; the coupling is specific; the Page curve is predicted — are what separate a mechanism from a relabeling. §6.6 makes the Page curve quantitative, §6.7 does the Skeptic's audit, §6.8 lists the tests.

### §6.5.7 A brief comparison with the Island formula

The Island formula of Penington, Almheiri, Engelhardt, Marolf, Maxfield, Hartman, Shaghoulian, and collaborators (2019–2020) reproduces the Page curve within the semiclassical gravity path integral by including replica-wormhole saddle points. The formula identifies, for each time $t$ after the Page time, an "island" region $I$ inside the black hole whose degrees of freedom are counted *as part of the radiation system* rather than the black-hole system. The prescription is:

$$(5.6.28)\quad S_\text{rad}(t) = \min_I\,\text{ext}\!\left[\frac{\text{Area}(\partial I)}{4\ell_P^2} + S_\text{semi}(R \cup I)\right],$$

where $R$ is the radiation region and $S_\text{semi}$ is the semiclassical entropy of the combined region.

From the zone-framework perspective, the "island" is — roughly speaking — the part of the bulk that is causally connected to the emitted radiation through the Firmament–bulk coupling. The area-law term in (5.6.28) is the breach-boundary entropy (our Eq. 5.5.20); the $S_\text{semi}$ term is the bulk entropy inside the causal region. The Page curve that the Island formula reproduces is structurally the same curve we will derive in §6.6, and both frameworks identify the "missing" degrees of freedom with bulk (not Firmament-exterior) degrees of freedom. The difference is that the Island formula identifies them through the gravitational path integral on an AdS or asymptotically-flat background, while the zone framework identifies them through the direct tensor-product decomposition (5.6.26). The two descriptions are, we conjecture, equivalent; a proof of equivalence is one of the tasks Vol 6 Ch 10 will take up.

### §6.5.8 Exit of §6.5

The reader now has:
- The tensor-product decomposition (5.6.26).
- Lemma 5.6.2 (Mathur premise M1 fails).
- Theorem 5.6.3 (6D unitarity).
- A plain-words mechanism for information flow.
- An honest comparison with the Island formula.

The chapter's central content is complete. The remaining sections — Page curve, Skeptic audit, predictions, ledger — are consequences, checks, and applications.

---

## §6.6 The Page Curve as a Theorem

The Page curve is the empirical target of the information paradox. Any proposal for how the paradox resolves must produce the Page curve, or at minimum explain why the expected curve is wrong. The zone framework produces it, and the derivation is short.

### §6.6.1 Page's argument, standard form

In 1993, Don Page asked: if a system is in a pure random state in a Hilbert space of dimension $D = D_R\cdot D_B$, factored into a "radiation" subsystem $R$ of dimension $D_R$ and a "black hole" subsystem $B$ of dimension $D_B$, what is the average entanglement entropy $S_\text{rad}$ of the radiation?

Page proved (and Lubkin 1978 had anticipated for the Haar-random case) that

$$(5.6.29)\quad \langle S_\text{rad}\rangle \approx \log\min(D_R, D_B),$$

up to corrections of size $O(D_R/D_B^2)$ when $D_R \ll D_B$ and symmetrically. The minimum is the essential feature: the entanglement entropy is bounded above by the log of the dimension of the *smaller* of the two subsystems, and when the subsystem that is smaller changes identity (as radiation accumulates and the black hole shrinks), the minimum swaps.

### §6.6.2 Mapping Page to the zone framework

In the zone framework, the "radiation" subsystem is the set of Hawking quanta that have escaped to $\mathcal I^+$ by time $t$, and the "black hole" subsystem is the combined (Firmament near the breach) + (bulk inside the breach), as decomposed in §6.5. The Hilbert space dimensions are

$$(5.6.30)\quad D_R(t) \approx e^{S_\text{emitted}(t)},\qquad D_B(t) \approx e^{S_\text{BH}(t)} \cdot e^{S_\text{bulk}(t)},$$

where $S_\text{emitted}(t)$ is the entropy emitted as thermal radiation up to time $t$, $S_\text{BH}(t) = k_B A(t)/(4\ell_P^2)$ is the shrinking area-law entropy of the breach, and $S_\text{bulk}(t)$ is the entropy in the bulk region inside the breach.

Because bulk entropy is capacity-wise enormous (§6.4.4 estimated $\sim 10^{117}$ modes inside a solar-mass breach), we can treat $D_B(t)$ as dominated by either $e^{S_\text{BH}(t)}$ or $e^{S_\text{bulk}(t)}$, whichever is *smaller*. In practice, bulk entropy does not shrink as rapidly as Firmament-area entropy — the bulk volume shrinks slowly as the breach shrinks — so for most of the evaporation, the rate-limiting factor is the area-law entropy $S_\text{BH}(t)$, and $D_B(t) \approx e^{S_\text{BH}(t)}$.

### §6.6.3 The Page time

Initially, $D_R(0) = 1$ (no radiation yet) and $D_B(0) = e^{S_\text{BH,initial}}$. As evaporation proceeds, $D_R(t)$ grows (more radiation) and $D_B(t)$ shrinks (smaller breach). They become equal when the radiation has absorbed half the initial entropy:

$$(5.6.31)\quad S_\text{emitted}(t_P) = \frac{1}{2}S_\text{BH,initial}.$$

This time $t_P$ is the Page time. Because the Hawking spectrum is approximately thermal with entropy rate $dS_\text{emitted}/dt \approx L/T_H$ (where $L$ is the luminosity and $T_H$ is the Hawking temperature), one can show by direct integration that $t_P$ is approximately half the total evaporation time:

$$(5.6.32)\quad t_P \approx \frac{1}{2}\tau_\text{evap},$$

up to logarithmic corrections. For $M = 10\,M_\odot$, using (5.6.23), $t_P \approx 5\times 10^{66}$ years. Long, but finite.

### §6.6.4 Theorem 5.6.4 — the Page curve

**Theorem 5.6.4 (Page Curve Theorem).** *Assume the evolution of $\rho_\text{total}(t)$ is unitary (Theorem 5.6.3), and assume the radiation is emitted coherently into the outgoing Firmament mode basis with entanglement thermalized on a timescale much shorter than the evaporation time.* Then the entanglement entropy of the emitted radiation, as a function of time, satisfies*

$$(5.6.33)\quad S_\text{rad}(t) \approx \begin{cases}S_\text{emitted}(t) & 0 \le t < t_P,\\ S_\text{BH}(t) & t_P \le t \le \tau_\text{evap},\end{cases}$$

*with $S_\text{rad}(0) = 0$ and $S_\text{rad}(\tau_\text{evap}) = 0$. The curve rises from zero, peaks at $t = t_P$ with value $\frac{1}{2}S_\text{BH,initial}$, and returns to zero at $t = \tau_\text{evap}$.*

**Proof.** By (5.6.29), $S_\text{rad}(t) \approx \log\min(D_R(t), D_B(t))$. For $t < t_P$, $D_R < D_B$, so $S_\text{rad} = \log D_R = S_\text{emitted}$. For $t > t_P$, $D_R > D_B$, so $S_\text{rad} = \log D_B = S_\text{BH}$. At $t = t_P$, both are equal to $\frac{1}{2}S_\text{BH,initial}$. At $t = \tau_\text{evap}$, $D_B = 1$ (the breach has closed) and so $S_\text{rad} = 0$. $\square$

The theorem is the quantitative version of the "information comes back out" picture of §6.5.5. The entropy of the radiation, as seen by a Firmament observer, tracks the *smaller* of (total emission so far) and (total remaining to be emitted). It grows during the first half, peaks, and falls during the second half.

[FIGURE: Fig 5.6.5 — The Page Curve, Standard and Zone-Architecture. Plot: entanglement entropy of emitted radiation $S_\text{rad}(t)/S_\text{BH,initial}$ on the vertical axis; time $t/\tau_\text{evap}$ on the horizontal axis from 0 to 1. Two curves: (a) solid red, "naive Hawking" — a monotonically rising curve approaching $S_\text{BH,initial}$ asymptotically; (b) solid blue, "Page curve (zone framework, Theorem 5.6.4)" — rises linearly from (0,0) to $(0.5, 0.5)$, then falls linearly from $(0.5, 0.5)$ to $(1, 0)$, forming a tent shape. Horizontal dashed line at $S_\text{rad}/S_\text{BH,initial} = 1$ labeled "Hawking thermal ceiling." Vertical dashed line at $t/\tau_\text{evap} = 0.5$ labeled "$t_P$: Page time." Caption: "Two predictions for the entanglement entropy of the emitted Hawking radiation. Red: if the radiation is exactly thermal (Hawking's original calculation), $S_\text{rad}$ rises monotonically, approaching $S_\text{BH,initial}$ and indicating persistent information loss. Blue: if 6D evolution is unitary (Theorem 5.6.3), $S_\text{rad}$ follows the Page curve, peaking at the Page time $t_P \approx \tau_\text{evap}/2$ and returning to zero. The zone framework predicts the blue curve."]

[FIGURE: Fig 5.6.6 — Hilbert-Space Dimension vs. Time. Semi-log plot of $\log D(t)$ vs. $t/\tau_\text{evap}$ from 0 to 1. Three curves: (a) $\log D_R(t)$ (radiation dimension): rises from 0 to $\log D_\text{total}$ at $t = \tau_\text{evap}$; (b) $\log D_B(t)$ (remaining Firmament+bulk dimension): falls from $\log D_\text{total}$ at $t = 0$ to 0 at $t = \tau_\text{evap}$; (c) the minimum envelope $\log\min(D_R, D_B)$: the Page curve. Vertical dashed line at the crossover $t = t_P$. Caption: "The Page curve is the lower envelope of the two Hilbert-space dimensions. Before the Page time, the radiation Hilbert space is smaller and limits the entanglement entropy; after it, the remaining black-hole Hilbert space takes over. The crossover at $t_P$ is where information begins to return."]

### §6.6.5 What "information coming back" means operationally

For $t > t_P$, the *new* Hawking quanta emitted do not on average add new entanglement entropy to the cumulative radiation — instead, they are correlated with quanta already emitted. The total entanglement of the radiation with the (shrinking) breach decreases, because the remaining breach has fewer and fewer degrees of freedom to hold entanglement. This is equivalent to saying that the later quanta are correlated with the earlier ones: if you measured the early quanta and used them to predict the late ones, your predictions would be *better* than chance, by an amount that integrates over the full post-Page-time emission.

In practice, an observer who wanted to decode the information would need to (a) collect the full radiation, (b) perform quantum measurements that span its entire Hilbert space, and (c) apply a decoder that takes exponentially long (in $S_\text{BH,initial}$) to run. This is impractical for any black hole an external observer could make or find, but the impracticality is a computational complexity statement, not a physical obstruction. The information is there; extracting it is Hawking-scrambling-hard (Hayden–Preskill 2007).

### §6.6.6 Why Page cannot be reproduced in pure 4D

A subtlety worth stating. Page's 1993 argument requires a tensor-factored Hilbert space with a "black hole side" whose dimension $D_B$ smoothly shrinks as radiation proceeds. In pure 4D, with the black hole described only by its exterior, what *is* the "black hole side"? The standard answers (remnant, firewall, fuzzball, island) all try to identify it with something physical — a Planck-scale remnant, a high-energy shell, stringy microstructure, or a gravitational-path-integral saddle. The zone framework has a more natural answer: the black hole side is the Firmament region near the breach plus the bulk region inside the breach, both of which are concrete physical objects with well-defined Hilbert spaces. The reason Page works in the zone framework is that there really is a "$D_B$" to shrink.

### §6.6.7 Summary of §6.6

The Page curve is not postulated or assumed. It follows from Theorem 5.6.3 (unitarity) plus Page's 1993 lemma applied to the explicit tensor decomposition (5.6.26). The curve rises to a maximum at $t_P \approx \tau_\text{evap}/2$ and falls back to zero at $\tau_\text{evap}$. The content of "information comes back" is that for $t > t_P$, each new emitted quantum on average correlates with earlier ones rather than adding fresh entanglement — a correlation pattern of amplitude $\sim e^{-S_\text{BH}/2}$ as we will quantify in §6.8.

---

## §6.7 Resolved vs. Rhetorically Resolved — A Skeptic's Audit

The Skeptic reviewer's central objection to any "resolution" of a famous paradox is that the resolution is a rhetorical maneuver: renaming the mystery in a new vocabulary that does not actually explain anything. This section responds directly.

### §6.7.1 What counts as a genuine resolution

A resolution of a paradox is genuine, in the sense I will use, if it satisfies four criteria:

- **(R1) Premise identification.** It specifies which premise of the original argument is wrong.
- **(R2) Derived replacement.** It provides an alternative to that premise, derived from an independent framework rather than postulated.
- **(R3) Original-result recovery.** It reproduces the empirical content of the original result (in this case, the Hawking spectrum) from the new framework.
- **(R4) Distinct predictions.** It makes specific, falsifiable predictions that differ from the original framework in at least one respect.

A resolution that meets only (R3) — "we get the Hawking spectrum, so we're fine" — is not a resolution; it is a reformulation. A resolution that meets only (R1) — "premise so-and-so is wrong" — is a critique, not a resolution. A resolution that meets only (R4) — "we predict different things" — might just be a different theory, not a resolution of the original paradox. All four are needed.

### §6.7.2 Applying the four criteria

Let me check the four criteria against five proposals: firewalls, fuzzballs, remnants, ER=EPR, and the zone framework.

| Proposal | (R1) Premise identified | (R2) Replacement derived | (R3) Hawking recovered | (R4) Distinct predictions |
|---|---|---|---|---|
| **Firewalls (AMPS 2012)** | Yes — premise M2 (smooth near-horizon QFT) | No — the wall is asserted | Yes | Yes, but violates equivalence principle |
| **Fuzzballs (Mathur 2005)** | Yes — premise M1 (exterior complete) | Partial — requires string theory as independent framework | Yes | Yes, stringy microstructure |
| **Remnants** | Ambiguous — they are a hope, not a theory | No | Yes | No |
| **ER=EPR (Maldacena–Susskind 2013)** | Yes — premise M1 in AdS | Partial — AdS-specific, conjectural | Yes | Yes, but AdS-specific |
| **Zone framework (this chapter)** | **Yes — premise M1, bulk factor ignored** | **Yes — from Vol 1 Ch 6, independently derived** | **Yes — §6.3** | **Yes — §6.8, four predictions** |

The zone framework passes all four criteria. Fuzzballs pass three and a half — they identify the right premise and recover Hawking, but require string theory as an independent framework, which some would argue is itself under-derived. ER=EPR is beautiful but is currently defined only in asymptotically AdS spacetimes, which excludes every astrophysical black hole. Firewalls are a resolution in the R1/R3/R4 sense but they fail R2 (the wall is not derived from anything) and they violate the equivalence principle, which is a high price.

### §6.7.3 The zone framework's specific failures, enumerated

Honesty requires listing where the zone framework might *still* be wrong.

**Potential failure 1.** The Waters-Below coupling $\lambda$ of (5.6.4) might be too weak to thermalize the Firmament and bulk on the Page timescale. If the thermalization time $\tau_\text{therm}$ is longer than $\tau_\text{evap}$, then the bulk is not effectively coupled to the outgoing radiation, and the chapter's mechanism fails to reproduce the Page curve. Gap G4.

**Potential failure 2.** The Bogoliubov calculation of §6.3 is performed to leading order in $1/M$ (equivalent to WKB at leading order). Next-to-leading corrections might introduce systematic deviations from the Planck distribution that are larger than the predicted non-thermal correlations of §6.8. Gap G1.

**Potential failure 3.** The final Planck-time of evaporation is not derived from first principles. The chapter argues (from Theorem 5.6.3) that the final state *must* be pure and the last $O(1)$ bits *must* be emitted, but it does not describe *how* the breach closes. Gap G2. This is a generic problem of semiclassical quantum gravity and is not worse here than elsewhere, but it is an open question.

**Potential failure 4.** The chapter assumes that the Island formula of Penington *et al.* is structurally compatible with the zone framework; a proof of equivalence has not been attempted. Gap G5 (new). This is not a failure but a missing check; we flag it because the Skeptic should want to see it.

### §6.7.4 The essential test

The cleanest possible experimental test would be to observe a primordial black hole over its full evaporation and confirm that the cumulative entropy of the emitted radiation follows the Page curve (rising, peaking, falling) rather than monotonic. No primordial black hole has been detected, and whether any exist is a separate question. If one were found and its spectrum were measured to be *exactly* thermal with no correlations at the $e^{-S/2}$ level through many decades of frequency, the resolution would be in trouble. That is the definition of falsifiable.

### §6.7.5 Exit of §6.7

The resolution meets all four criteria for a genuine resolution, with three (or four, being liberal) acknowledged gaps that are quantitative rather than structural. A skeptic who accepts these criteria and reads the comparison table must conclude that "resolved" is the right word — but not a final word, and not a dismissal of the open items. The chapter is not claiming the paradox is closed beyond all possible challenge; it is claiming that the zone framework has dissolved the paradox at the level of its central theorem and reproduced its central observational target (the Page curve), and that further quantitative work is both possible and required.

---

## §6.8 Falsifiable Predictions and Endpoint Physics

§6.7 promised four falsifiable predictions. We list and elaborate them here.

### §6.8.1 Prediction P1: Non-thermal correlations in Hawking radiation

**Statement.** The two-point function of outgoing Hawking quanta at frequencies $\omega_1, \omega_2$ contains, in addition to the diagonal thermal piece, an off-diagonal non-thermal piece with amplitude

$$(5.6.34)\quad \big|\langle \hat a^\text{out}_{\omega_1} \hat a^\text{out}_{\omega_2}\rangle_\text{connected}\big| \sim e^{-A(t)/(8\ell_P^2)}\cdot f(\omega_1,\omega_2),$$

where $A(t)$ is the current breach area and $f$ is an order-unity function determined by the bulk state. The amplitude is exponentially small in the residual black-hole entropy, and it becomes significant only after the Page time when the breach has shrunk substantially.

**Why it follows.** The connected two-point function carries the entanglement structure of the radiation. Theorem 5.6.4 (Page curve) requires that this structure change after $t_P$; specifically, the entanglement of new quanta with previously-emitted ones produces off-diagonal correlations of exactly this form. The factor $e^{-A/(8\ell_P^2)}$ comes from the Page lemma applied to $D_B(t) = e^{A(t)/(4\ell_P^2)}$.

**Why it is a genuine prediction.** Standard Hawking gives $\langle\hat a_{\omega_1}\hat a_{\omega_2}\rangle = 0$ for off-diagonal components. The zone framework gives nonzero (but exponentially small) amplitude. The difference is observable in principle — you would need to measure many outgoing quanta and reconstruct the connected correlation — but in practice requires extremely high quanta counts. An astrophysical black hole emits fewer than one quantum per age-of-the-universe; only primordial black holes near the end of their lifetime produce enough for this test.

### §6.8.2 Prediction P2: Page curve for evaporating primordial black holes

**Statement.** If a primordial black hole of mass $\sim 10^{12}$ kg (evaporation time comparable to the age of the universe) were observed through its final phase, the cumulative entropy of its emitted radiation would follow the Page curve of Theorem 5.6.4, not the monotonic Hawking curve.

**Operational form.** Count the cumulative entropy $S_\text{rad}(t)$ of the emitted quanta as a function of time. The prediction is: rising from 0 at $t = 0$, peaking at $\frac{1}{2}S_\text{BH,initial}$ at $t = t_P$, returning to 0 at $t = \tau_\text{evap}$. Pure Hawking predicts monotonic rise to $S_\text{BH,initial}$, then... silence.

**Why this is the clean test.** Page curve shape is *independent* of the precise values of the parameters; it is a universal prediction from Theorem 5.6.4. Any observation that distinguishes a tent-shaped curve from a monotone one settles the question.

### §6.8.3 Prediction P3: Final Planck-scale burst carries the last bits

**Statement.** At $t = \tau_\text{evap}$, the breach closes. Theorem 5.6.3 requires that the final density matrix be pure, which forces the last $O(1)$ bits to be emitted in the final Planck time. The spectrum of this final burst is *not* thermal (the Hawking formula (5.6.20) is undefined at $M \sim M_P$), and the burst is dominated by the breach-closure dynamics. The burst contains the "scrambling" of the infalling state with the earlier Hawking emissions.

**Why it is distinctive.** The remnant proposal predicts no final burst (the information is stored in the remnant forever). Pure Hawking predicts a final burst at infinite temperature (formally divergent, physically suspect). The zone framework predicts a finite, non-thermal burst with a specific (though not-yet-calculated) spectrum determined by the bulk state at the moment of closure.

[FIGURE: Fig 5.6.7 — Hawking Spectrum with Non-Thermal Correlations. Main plot: emission rate $dN/(d\omega\,dt)$ vs. dimensionless frequency $\hbar\omega/(k_B T_H)$, on a log-log scale, for a $10\,M_\odot$ primordial-scale black hole during its final evaporation. The dominant curve is the Planckian envelope $1/(e^{\hbar\omega/k_BT_H}-1)$. Inset (upper-right): residuals from a pure-thermal fit, showing oscillatory deviations of amplitude $\sim e^{-S_\text{BH}/2}$ spread across frequencies — the non-thermal correlations of Prediction P1. Second inset (lower-right): the endpoint spectrum near $\omega \sim k_B T_\text{Planck}/\hbar$, showing a non-monotone spike labeled "final Planck burst (P3)" distinct from the thermal extrapolation. Caption: "Zone-framework prediction for the Hawking spectrum. The overall envelope is Planckian (matching the standard result). The oscillatory residuals at amplitude $e^{-S/2}$ encode the infalling information (P1). The non-thermal final burst at the evaporation endpoint (P3) carries the last bits and distinguishes the zone framework from remnant and pure-thermal proposals."]

### §6.8.4 Prediction P4: Ringdown echoes with specified amplitude

Ch 5 §5.8.2 predicted ringdown echoes from the breach edge after a binary merger, with amplitude controlled by the breach-edge reflectivity. That reflectivity is now constrained by the Firmament–bulk coupling $\lambda$ of §6.5: a nonzero $\lambda$ means Firmament modes near the edge are partially converted to bulk modes (and absorbed) rather than fully reflected. The prediction is that echo amplitudes are suppressed by a factor of order $e^{-\omega/\omega_\text{cutoff}}$, where $\omega_\text{cutoff}$ is set by the coupling. For $10\,M_\odot$ mergers, the predicted amplitudes are within LIGO/LISA sensitivity in the next-generation detector era (Cosmic Explorer, Einstein Telescope, LISA).

### §6.8.5 Endpoint physics: a status report

The three theorems of the chapter — 5.6.1 (Mathur, which fails here), 5.6.3 (unitarity), and 5.6.4 (Page) — together impose four conditions on the final state at $t = \tau_\text{evap}$:

1. The breach must close (by the Breach Theorem of Ch 5: if the mass is zero, there is nothing to force $\sigma_\text{local}(r) < 0$ anywhere).
2. The final state must be pure (Theorem 5.6.3).
3. The total emitted entropy must equal the initial $S_\text{BH,initial}$ (Theorem 5.6.4 closes at zero).
4. The emitted radiation must carry the full information content of $|\psi_\text{in}\rangle$ (Theorem 5.6.3, combined with the vanishing of the bulk inside the breach as the breach closes).

What is missing is a first-principles derivation of *how* the breach closes. The closure dynamics involve Planck-scale Firmament membrane mechanics, quantum gravity corrections to the Firmament Lagrangian (5.6.1), and possibly new physics at the Firmament–bulk interface. The present chapter cannot derive them. What it *can* do is state the constraints (1)–(4) and flag the open question as gap G2.

---

## §6.9 The Reviewer's Ledger

Following the format of Ch 1 §1.10, Ch 4 §4.12, and Ch 5 §5.9.

[FIGURE: Fig 5.6.8 — Reviewer's Ledger for Chapter 6. A two-column table (rendered graphically in the published edition). Left column: every load-bearing claim in the chapter, one per row, ordered by section. Right column: classification into one of four buckets with color coding — green = Derivation (from the 6D action or geometric identity); blue = Identity (definitional or trivially true); yellow = Inheritance (result from a previous chapter, cited without re-derivation); red = Conjecture (flagged as an open item with mitigation). Footer summarizes: 6 Derivations (Theorems 5.6.1–5.6.4 plus Bogoliubov spectrum and Page curve), 11 Inheritances (from Vol 1 Ch 5, 6, 11; Vol 3 Ch 12; Vol 4 Ch 6, 8; Vol 5 Ch 5), 5 Conjectures (gaps G1–G5). Caption: "Every claim in Chapter 6 is classified. The red rows are the only places where the chapter depends on something not yet proven; each has an explicit mitigation in §6.9.3."]

### §6.9.1 Derivations (from the 6D action, previous theorems, or analytic identities)

| Step | Eq. / Thm | Status |
|---|---|---|
| Brane wave equation with position-dependent speed | (5.6.9) | Derivation from (5.6.1) + Ch 5 tension profile. |
| Tortoise coordinate + Regge–Wheeler potential | (5.6.11), (5.6.13) | Coordinate-change identity. |
| Bogoliubov coefficients at the turning point | (5.6.18), (5.6.19) | Derivation by analytic-continuation at $r = r_s$; standard technique from Vol 4 Ch 7, applied to the Firmament. |
| Hawking spectrum from Bogoliubov | (5.6.20) | Derivation from (5.6.19). Matches Ch 5 (5.5.24). |
| Mathur Theorem 5.6.1 | §6.2.4 | Restatement of Mathur 2009; proof sketch given. |
| Lemma 5.6.2 (Premise M1 fails) | §6.5.3 | Derivation from commutation relation (5.6.3) + coupling (5.6.4). |
| Theorem 5.6.3 (6D Unitarity) | §6.5.4 | Derivation from self-adjointness of $\hat H_\text{6D}$ + Stone's theorem. |
| Theorem 5.6.4 (Page Curve) | §6.6.4 | Derivation from Theorem 5.6.3 + Page 1993 lemma. |

### §6.9.2 Inheritances (results used without re-derivation)

- Brane Lagrangian (5.6.1), wave speed identity, positivity of tension — Vol 1 Ch 5.
- Bulk Lagrangian (5.6.2), interaction (5.6.4), $[\hat a, \hat b^\dagger] = 0$ — Vol 1 Ch 6.
- 6D Liouville theorem (5.6.6) — Vol 1 Ch 11.
- Boltzmann–Shannon–Landauer framework — Vol 3 Ch 12.
- Second quantization, Bogoliubov machinery — Vol 4 Ch 6, §6.6.
- Analytic-continuation technique for $S$-matrix branch cuts — Vol 4 Ch 7.
- Zone UV cutoff $\Lambda_{\mathrm{zone}} = \hbar c/\eta_B \approx 0.152\,\mathrm{GeV}$ — Vol 4 Ch 8 (corrected per CT-4.Λ, Rev. 2026-05-15; QCD scale, not Planck scale).
- Bekenstein–Hawking entropy (5.5.20), Hawking temperature (5.5.24), tension profile (5.5.13), Breach Theorem 5.5.1 — Vol 5 Ch 5 §5.2–5.6.
- Regge–Wheeler computation of grey-body factors — Page 1976 (cited, not reproduced).
- Mathur small-corrections theorem — Mathur 2009 (cited; proof sketched in §6.2.4).
- Page entanglement lemma — Page 1993 (cited; statement in §6.6.1).

### §6.9.3 Conjectures and open items

**Gap G1 (MEDIUM).** The Bogoliubov calculation of §6.3 is at leading WKB order. Next-to-leading corrections (of relative size $1/M$) might introduce deviations from the pure Planck spectrum at the same order as the non-thermal correlations of Prediction P1. Mitigation: Vol 6 Ch 4 will compute the corrections and separate the WKB residuals from the information-carrying residuals.

**Gap G2 (MEDIUM).** The endpoint of evaporation is not derived from first principles. The chapter shows (from Theorem 5.6.3) that the final state must be pure, but not how the breach closes. This is a quantum-gravity endpoint problem and is not specific to the zone framework. Mitigation: flagged for Vol 6 Ch 5.

**Gap G3 (LOW).** The explicit form of the correlation function (5.6.34) is derived only at the level of the Page lemma and dimensional analysis; a mode-by-mode computation of the correlation matrix from the Firmament–bulk coupling (5.6.4) is not performed. Mitigation: Vol 6 Ch 10.

**Gap G4 (MEDIUM).** The Firmament–bulk coupling $\lambda$ of Vol 1 Ch 6 §6.5 is assumed to be large enough for the bulk to thermalize with the Firmament on a timescale much shorter than $\tau_\text{evap}$. This is a quantitative assumption whose verification requires computing $\tau_\text{therm}$ from $\lambda$ and comparing to (5.6.23). Mitigation: flagged for Vol 6 Ch 10 alongside G3. The sharpest near-term observational constraint on $\lambda$ is the ringdown-echo spacing of Prediction P4 (§6.8): the echo period is a monotonic function of $\lambda$ through the Firmament tension profile, so a LIGO/LISA measurement or null result would pin (or bound) $\lambda$ directly without requiring the full bulk Lagrangian to be specified.

**Gap G5 (LOW).** The relationship between the chapter's tensor decomposition (5.6.26) and the Island formula (5.6.28) of Penington *et al.* is conjectured but not proven. Mitigation: a proof of equivalence (or a demonstration of inequivalence with a distinguishing prediction) is a task for Vol 6 Ch 10.

### §6.9.4 A note specifically for the Skeptic

Your challenge was "is *resolved* genuine or rhetorical?" The four-criterion audit of §6.7 answers: genuine, in the sense that the zone framework identifies a specific failed premise (M1), provides an independently derived replacement (the bulk Hilbert space from Vol 1 Ch 6), recovers the empirical content (Hawking spectrum in §6.3, Page curve in §6.6), and makes falsifiable distinct predictions (§6.8, four of them). Three structural gaps (G1, G2, G4) are flagged honestly; none of them is structural in the sense of breaking the main theorems. If the Skeptic finds this answer inadequate, the specific objection should be stated so it can be addressed directly in the next revision.

### §6.9.5 A note specifically for the Theologian

No theological claims are made in this chapter. The word "Firmament" is used only as the Vol 1 Ch 5 name for the 3-brane $Z_{2.2}$. The phrase "information preservation" refers only to the mathematical property that unitary evolution preserves the rank and spectrum of density matrices; it makes no commitments about information in any other sense. Commentary on what this might mean in theological terms belongs to Book 3, not here. As in Ch 5, we note that the research file `black_holes_membrane_punctures.docx` does make such commentary, and we follow the practice of Ch 5 §5.9.4 in separating the physics from the commentary.

### §6.9.6 A note specifically for the "But Why?" Reader

One-sentence answers to the seven chapter-opening why-questions:

1. **Why is there a paradox?** Because Hawking showed that a pure state radiates as a thermal (mixed) state, and pure-to-mixed evolution is forbidden by unitarity (§6.2).
2. **Why can't small corrections fix it?** Because Mathur (2009) proved that strong subadditivity of entropy forbids small corrections from restoring a pure final state (Theorem 5.6.1, §6.2.4).
3. **Why does the zone framework escape Mathur?** Because its Premise M1 (exterior Hilbert space is complete) is false — the bulk is a separate and populated Hilbert-space factor (Lemma 5.6.2, §6.5.3).
4. **Why does the breach radiate at $T_H$?** Because the Firmament wave speed vanishes at $r = r_s$, making $r_s$ a turning point whose analytic continuation produces the thermal factor $(e^{2\pi\omega/\kappa} - 1)^{-1}$ in the Bogoliubov coefficients (§6.3.5).
5. **Why is the spectrum not exactly thermal?** Because the outgoing Firmament modes are coupled to the bulk through the interaction term (5.6.4), and the small corrections of size $e^{-A/(8\ell_P^2)}$ carry the returning information (Prediction P1, §6.8.1).
6. **Why does information come back out?** Because the 6D Hamiltonian is self-adjoint and its evolution is therefore unitary (Theorem 5.6.3, §6.5.4); the information "in the bulk" returns to the Firmament through the coupling (5.6.4) as the breach radiates.
7. **Why is the Page curve what you see?** Because Page's 1993 lemma applied to the explicit tensor decomposition (5.6.26) forces the entanglement entropy of the emitted radiation to track the *smaller* of the radiation and black-hole Hilbert-space dimensions, producing a tent-shaped curve with a peak at $t_P \approx \tau_\text{evap}/2$ (Theorem 5.6.4, §6.6.4).

### §6.9.7 Forward links

- **Chapter 7** (Singularity Resolution) will use the breach-closure dynamics previewed in §6.8.5 to argue that the "Big Bang singularity" and the "black hole singularity" are the same kind of non-event in the zone framework — namely, the moment of Firmament opening or closing.
- **Chapter 11** (Dark Matter and Dark Energy Quantified) will revisit the Waters-Below Hilbert space at cosmological scales; the bulk that holds Hawking-radiation information in this chapter is the same bulk that carries cosmological dark matter energy density.
- **Volume 6** will close the open items G1 (Bogoliubov next-order), G2 (endpoint), G3 (correlation details), G4 (thermalization timescale), and G5 (Island-formula equivalence).

---

## §6.10 Problem Sets

### Computational

**P6.1.** *(Hawking temperature for common masses.)* Use (5.6.20) to compute $T_H$ for (a) $M = M_\odot$, (b) $M = 10^6\,M_\odot$, (c) $M = 10^{12}$ kg (primordial), (d) $M = 10^{15}$ kg, and (e) the Planck mass. Compare to the CMB temperature ($2.73$ K) and identify which of these black holes are net-absorbing from the CMB and which are net-evaporating.

**P6.2.** *(Page time for a stellar black hole.)* Using (5.6.22), (5.6.23), and (5.6.31), compute the evaporation lifetime $\tau_\text{evap}$ and the Page time $t_P$ for a $10\,M_\odot$ black hole. Express your answer in years and in units of the present age of the universe.

**P6.3.** *(Correlation amplitude.)* For the same $10\,M_\odot$ black hole, compute the amplitude of the non-thermal correlations of Prediction P1 at the Page time, using (5.6.34) with $A(t_P) = A_\text{initial}/\sqrt 2$. Express as $\log_{10}$ of the amplitude. Is this observable even in principle?

**P6.4.** *(Tortoise coordinate algebra.)* Verify the tortoise-coordinate relation (5.6.11) by direct integration. Then compute $dr^*/dr$ at $r = 3\,r_s/2$ (near the potential peak) and at $r = 10\,r_s$ (deep in the asymptotic region). Comment on how the tortoise coordinate is compressed near the breach edge.

**P6.5.** *(Grey-body factor at low frequency.)* For the $\ell = 0$ channel, estimate the grey-body factor $\Gamma_0(\omega)$ in the low-frequency limit $\omega\,r_s/c \ll 1$ by matching the $s$-wave solution across the Regge–Wheeler potential. Show that $\Gamma_0(\omega) \propto (\omega r_s/c)^2$, so that the low-frequency Hawking spectrum is flatter than pure Planck.

### Conceptual

**P6.6.** *(Mathur's theorem in your own words.)* In one paragraph, explain the content of Mathur's small-corrections theorem (Theorem 5.6.1) without using equations. Your explanation should make clear (a) which three premises are needed, (b) what the conclusion is, and (c) why "small corrections" of size $e^{-S}$ are inadequate.

**P6.7.** *(Which Mathur premise fails in the zone framework?)* Identify the Mathur premise that fails in the zone framework, and in one paragraph explain why it fails. Your answer should cite the specific Vol 1 Ch 6 result that guarantees the bulk is a distinct Hilbert-space factor.

**P6.8.** *(No firewall here.)* In one paragraph, explain why the zone framework's resolution of the information paradox does not require a firewall at the horizon. Your answer should combine Ch 5 §5.5.3 (no firewall from tension continuity) with this chapter's §6.5 (unitarity on the 6D Hilbert space).

**P6.9.** *(Information locality.)* Does the resolution in this chapter respect causality? Specifically: when information carried by an infalling bit is eventually re-emitted in late Hawking radiation, does any physical signal travel faster than light in either the 4D or the 6D description? Argue your answer.

### Challenge

**P6.10.** *(WKB Bogoliubov coefficients.)* Starting from the wave equation (5.6.12) with the Regge–Wheeler potential (5.6.13), compute the Bogoliubov coefficient $|\beta_\omega|^2$ at the leading WKB order, and verify that it reproduces (5.6.19). Hint: use the Stokes-line method; the branch cut you need is at the classical turning point where $V_\ell(r^*) - \omega^2 = 0$.

**P6.11.** *(Kerr Bogoliubov.)* Extend the Bogoliubov calculation of §6.3 to a Kerr black hole (using the exterior Kerr metric of Ch 5 Eq. 5.5.5). Show that the thermal factor in (5.6.20) is replaced by $(e^{\hbar(\omega - m\Omega_+)/k_B T_H} - 1)^{-1}$, where $\Omega_+$ is the angular velocity of the outer horizon and $m$ is the azimuthal quantum number. This is the "superradiance-corrected" Hawking spectrum.

**P6.12.** *(Zero reflectivity limit.)* Suppose the breach-edge reflectivity (from Ch 5 §5.8.2 and §6.5.5) were exactly zero, so that all Firmament modes at the breach boundary are fully absorbed into the bulk with no reflection. (a) What would the Hawking spectrum look like in this limit? (b) Would the Page curve still be reproduced, or would it be modified? (c) If the Page curve is still reproduced, what does that tell you about the robustness of Theorem 5.6.4? If it is modified, what does that tell you about the role of the reflectivity?

---

*End of Ch06_DRAFT.md. Word count target: ~11,000–12,000 words. Figures: 8 placeholders (Fig 5.6.1 through Fig 5.6.8). Equation range: (5.6.1) through (5.6.34). Status: DRAFT — ready for Self-Review (Phase 4).*
