---
product: Foundations Vol 5 — The Cosmos
chapter: 6
title: The Information Paradox Resolved
status: OUTLINE
---

# Chapter 6 — Detailed Outline

Target: ~11,000 words; 8 figures; equations (5.6.1)–(5.6.30); Feynman voice.

## §6.0 What This Chapter Is (and Is Not) — ~400 words

- **Topic sentence.** Chapter 5 deferred the question "where does the information go?" This chapter answers it.
- **Why entry point.** The standard Hawking paradox says a pure state becomes mixed — violating unitarity. Vol 3 Ch 12 told us information cannot be destroyed; Ch 5 showed the brane has a hole; we now show these are consistent.
- **What this chapter does:** derive Hawking radiation from membrane dynamics; state the conventional paradox as a no-go theorem; show the zone framework's premises break the theorem; prove 6D unitarity; prove the Page curve.
- **What it does not do:** rederive Vol 5 Ch 5 results; wade into AdS/CFT, ER=EPR, or holographic entanglement wedges in detail (though it engages with them in §6.7); claim the final Planck-scale burst is fully understood (G2).
- **A note to the Theologian and the Navigator.** Information preservation is a mathematical theorem about 6D Hamiltonian evolution, not a theological claim. The central result is stated once, explicitly, in §6.5.
- **Exit condition.** Reader knows what the chapter will prove, and knows the three theorems it will establish.

## §6.1 Inventory: The Toolkit From Previous Chapters — ~700 words

### §6.1.1 From Vol 1 Ch 5 — Membrane dynamics
- Nambu–Goto action (Vol 1 Eq. 1.5.26); linearized membrane Lagrangian (Vol 1 Eq. 1.5.34).
- Wave speed $c^2 = \sigma/\mu$; positivity of tension.
- Junction conditions on codimension-2 branes.

### §6.1.2 From Vol 1 Ch 6 — The Waters bulk fields
- Waters Below field $\Psi_\text{WB}$ with its own Lagrangian and its own Hilbert space $\mathcal H_\text{bulk}$.
- Coupling to the brane through a boundary term $\mathcal L_\text{int} = \lambda\,\Psi_\text{WB}(\gamma)\cdot\mathcal O_\text{brane}(\gamma)$.
- Key fact: the bulk has physical degrees of freedom that an on-brane observer cannot measure directly.

### §6.1.3 From Vol 1 Ch 11 — Entropy as brane-mode counting + Liouville on 6D phase space
- Eq. (5.6.6) restatement of $S = k_B\ln\Omega$ at Planck cutoff.
- Liouville theorem: the 6D phase-space measure is conserved by the full 6D Hamiltonian flow.

### §6.1.4 From Vol 3 Ch 12 — "Information is not destroyed, it flows."
- Boltzmann–Shannon identification of entropy with missing information.
- Landauer's principle: erasing a bit costs $k_B T \ln 2$.
- Liouville → microscopic reversibility → unitarity.

### §6.1.5 From Vol 4 Ch 6–9 — QFT on the brane
- Second quantization: $[\hat a_k, \hat a_{k'}^\dagger] = \delta_{kk'}$ (4.6.13).
- Bogoliubov transformations (Vol 4 §6.6, used here): two different mode expansions of the same quantum field are related by a linear transformation with coefficients $\alpha_{kk'}$, $\beta_{kk'}$.
- Planck-length UV cutoff from Vol 4 Ch 8.
- Vacuum-boundary-condition sensitivity (Casimir, Vol 4 Ch 9).

### §6.1.6 From Vol 5 Ch 5 — The breach picture
- Tension profile (5.5.13): $\sigma_\text{local}(r) = \sigma_\infty(1 - r_s/r)$.
- Breach Theorem 5.5.1.
- Bekenstein–Hawking entropy (5.5.20): $S_\text{BH} = k_B A/(4\ell_P^2)$.
- Hawking temperature (5.5.24): $T_H = \hbar c^3/(8\pi G M k_B)$ — derived from the first law; here we re-derive from the microscopic mode structure.

### §6.1.7 What we will use and not re-derive
Same format as Ch 5 §5.1.5. Explicit list.

- **Exit condition.** Reader has a one-page map of what comes in from where, including equation numbers.

## §6.2 The Paradox As Conventionally Stated — ~1300 words

### §6.2.1 The setup
A pure quantum state $|\psi\rangle$ containing a lot of mass collapses into a black hole. The Schwarzschild exterior is classical and the black hole has entropy $S_\text{BH} = A/(4\ell_P^2)$ — huge, but finite.

### §6.2.2 Hawking 1974: thermal radiation
Hawking's 1974 calculation computes the Bogoliubov mixing between the mode basis at past null infinity ($\mathcal I^-$) and the one at future null infinity ($\mathcal I^+$). The result: the in-vacuum is an out-thermal state at temperature $T_H = \hbar c^3/(8\pi G M k_B)$. This is (5.6.14), previewed here, derived in §6.3.

### §6.2.3 The contradiction
If the radiation is exactly thermal, the density matrix of the outgoing radiation after complete evaporation is $\rho_\text{rad} = Z^{-1} e^{-\hat H/k_B T_H}$ — a mixed state. But the initial state $|\psi\rangle$ was pure. Pure-to-mixed evolution violates unitarity, which is axiomatic in QM.

**[FIGURE 5.6.1 placed here.]** Three-panel schematic.

### §6.2.4 Why "small corrections" cannot fix this: Mathur's theorem
State the Mathur 2009 theorem in precise form. Its premises:
- **Premise M1:** The Hilbert space in the exterior region is complete (no "hidden" degrees of freedom).
- **Premise M2:** Modes at distances $\gg\ell_P$ from the horizon behave as standard QFT on Schwarzschild.
- **Premise M3:** Each Hawking mode-pair is approximately entangled in its native wavelength only.

Under these premises, the entanglement entropy of the radiation at step $n$ in the emission is $\approx n\cdot\ln 2$ — monotonically growing. For the entanglement entropy to return to zero (pure final state), the *per-step* correction to the entanglement of a pair must be at least $O(1)$, not $O(e^{-S})$. "Small corrections" (exponentially suppressed in the BH entropy) are provably inadequate.

**Theorem 5.6.1 (Mathur Small-Corrections, restated).** *Under premises M1–M3, no correction smaller than order unity to the per-pair entanglement can restore the final state to a pure state.*

Sketch of proof (in outline): strong subadditivity of entanglement entropy forces a triangle inequality that is violated if corrections are too small.

### §6.2.5 The historical options and why each fails
- **(a) Remnants.** Fails because the entropy bound at Planck scale is too small to hide an arbitrary amount of information.
- **(b) Non-local modification of QFT.** Fails because it violates causality at scales where causality is experimentally verified.
- **(c) Firewalls (AMPS 2012).** Fails equivalence principle for infalling observers; Ch 5 §5.5.3 already noted why the membrane picture gives no firewall.
- **(d) Fuzzballs.** Require exotic stringy microstructure; offloads rather than solves the problem; not derivable from a 4D Lagrangian.
- **(e) ER=EPR.** Interesting but conjectural and specific to AdS.

The common feature: all of these try to fix the paradox *within* the 4D effective theory by tweaking one of the premises of Hawking's derivation, while keeping the theory 4D. The zone framework does something different: it drops Premise M1 because the exterior is provably not the full Hilbert space.

- **Exit condition.** Reader understands the paradox is a real theorem, not a confusion, and understands exactly which assumption has to fail for a resolution to exist.

## §6.3 Hawking Radiation From Membrane Dynamics — ~1600 words

### §6.3.1 The setup: a scalar brane mode near the breach
Consider a massless scalar brane mode $\phi(t,r,\theta,\varphi)$ obeying the wave equation
$$(5.6.1)\quad \partial_t^2\phi - v^2(r)\,\frac{1}{r^2}\partial_r\!\left(r^2\partial_r\phi\right) - v^2(r)\,\frac{1}{r^2}\mathcal L^2\phi = 0,$$
where $v^2(r) = \sigma_\text{local}(r)/\mu = c^2(1 - r_s/r)$. The position-dependent wave speed is the whole point: it vanishes at the breach.

### §6.3.2 Tortoise coordinate
Define $r^* = \int dr/(1 - r_s/r) = r + r_s\ln(r/r_s - 1)$. In $r^*$, the wave equation reduces (for radial modes with $\ell = 0$) to
$$(5.6.2)\quad (\partial_t^2 - \partial_{r^*}^2)\,\chi + V_\text{eff}(r^*)\chi = 0,\qquad \chi = r\phi,$$
with an effective potential $V_\text{eff}$ that peaks near $r \approx 3r_s/2$ and vanishes exponentially as $r^* \to \pm\infty$.

**[FIGURE 5.6.2 placed here.]**

### §6.3.3 The two mode bases
- **In-modes:** plane waves at $\mathcal I^-$ (past null infinity, $r^* \to +\infty$, $t \to -\infty$): $\chi_\text{in} \propto e^{-i\omega(t + r^*)}$.
- **Out-modes:** plane waves at $\mathcal I^+$ (future null infinity): $\chi_\text{out} \propto e^{-i\omega(t - r^*)}$.
- **Horizon-modes:** waves on the brane surface at $r^* \to -\infty$ (the breach edge). These live only for $t < t_\text{breach}$.

### §6.3.4 The Bogoliubov transformation
Expand $\phi$ in both bases and compare: there exist coefficients $\alpha_{\omega\omega'}$, $\beta_{\omega\omega'}$ such that
$$(5.6.3)\quad \hat a^\text{out}_\omega = \int d\omega'\,[\alpha_{\omega\omega'}\,\hat a^\text{in}_{\omega'} - \beta^*_{\omega\omega'}\,\hat a^{\text{in}\dagger}_{\omega'}].$$

The in-vacuum annihilates $\hat a^\text{in}$, but not $\hat a^\text{out}$. The number expected by an out-observer is
$$(5.6.4)\quad \langle N^\text{out}_\omega\rangle = \int d\omega'\,|\beta_{\omega\omega'}|^2.$$

### §6.3.5 Computing $|\beta|^2$ — the key calculation
The Bogoliubov coefficient is determined by the analytic continuation of the out-mode around the turning point $r = r_s$. In the membrane framework this is the point where $v^2(r) = 0$ — a physical turning point, not a coordinate one. Using standard WKB-plus-analytic-continuation (the same technique used in Vol 4 Ch 7 for $S$-matrix branch cuts), the ratio is:
$$(5.6.5)\quad \frac{|\alpha_{\omega\omega'}|^2}{|\beta_{\omega\omega'}|^2} = e^{2\pi\omega/\kappa},$$
where $\kappa$ is the surface gravity of the breach, $\kappa = c^4/(4GM) = c^2/(2r_s)$. With the normalization $|\alpha|^2 - |\beta|^2 = 1$,
$$(5.6.6)\quad |\beta_{\omega\omega'}|^2 = \frac{\delta(\omega - \omega')}{e^{2\pi\omega/\kappa} - 1}.$$

### §6.3.6 The Planck distribution
Plugging (5.6.6) back into (5.6.4),
$$(5.6.7)\quad \langle N^\text{out}_\omega\rangle = \frac{1}{e^{\hbar\omega/(k_B T_H)} - 1},\qquad T_H = \frac{\hbar\kappa}{2\pi c\,k_B} = \frac{\hbar c^3}{8\pi G M k_B}.$$
This is exactly the temperature we got from the first law in Ch 5 §5.6.3. $\checkmark$

### §6.3.7 Why the two derivations agree
Consistency check: Ch 5 got (5.5.24) thermodynamically; we now got (5.6.7) microscopically. The equality is not a coincidence — it follows from the first law together with the fact that the Bogoliubov derivation *uses* the fact that the tension vanishes at $r_s$ (membrane framework) or that the Killing vector becomes null at $r_s$ (standard GR). These are the same surface.

### §6.3.8 The grey-body factor (noted, not computed)
The spectrum is modified by the propagation through $V_\text{eff}(r^*)$: some modes are backscattered. The resulting "grey-body factor" $\Gamma(\omega)$ multiplies (5.6.7). It does not affect the thermal factor but does change the total luminosity. We note it for completeness; Vol 6 will treat it in detail.

### §6.3.9 Summary of §6.3
Hawking radiation is not a mystery in the zone framework — it is a Bogoliubov transformation on brane modes in a region where the brane wave speed vanishes. The temperature is forced by the surface gravity of the breach. **The same derivation in pure GR is the standard one, and produces the same answer.** What the membrane version adds is (a) a *physical* turning point rather than a coordinate one, and (b) the essential ingredient for what follows — the bulk, with its own Hilbert space, sitting right there at the turning point.

- **Exit condition.** Reader can derive Hawking temperature as a Bogoliubov coefficient; understands why it matches Ch 5's thermodynamic derivation.

## §6.4 Entropy Bounds Revisited — ~900 words

### §6.4.1 The Bekenstein bound
State and motivate the Bekenstein bound $S \le 2\pi k_B R E/(\hbar c)$ for a system of energy $E$ and radius $R$. This bound is saturated by black holes — which is what makes (5.5.20) "special" in the first place.

### §6.4.2 The holographic bound
The weaker statement: $S \le k_B A/(4\ell_P^2)$ for any region bounded by area $A$. Also saturated by black holes. In the zone framework, this is simply the statement that the brane boundary counts its own modes, and (5.5.20) is the natural ceiling.

### §6.4.3 Why the bounds hold — zone-architecture reading
In standard GR, the holographic bound is mysterious: why should a 3D region have its information content bounded by a 2D quantity? In the zone framework, the answer is immediate: because the "information" that an exterior observer can extract lives on the *brane*, which has boundary degrees of freedom scaling as the area of the boundary. Bulk information is inaccessible to the brane observer by construction and does not enter the bound. The bound is a statement about *what a brane observer can know*, not about *what exists*.

### §6.4.4 This reframing matters
Because it tells us that the "information" in $S_\text{BH}$ is not the total information about the infallen matter. It is the information a brane observer can extract from the breach boundary by watching the radiation. The infallen matter's full information lives in the combined brane+bulk state, and the bulk share is not bounded by $A/(4\ell_P^2)$ at all — it can be much larger, limited only by the bulk entropy density and the bulk volume.

### §6.4.5 Numerical feeling
For a solar-mass black hole: $S_\text{BH}\sim 10^{77} k_B$; the total 6D bulk entropy inside the breach (if estimated as $\rho_\text{bulk} V \approx $ Waters-Below density times breach volume) is at least comparable, possibly larger. The brane-boundary share is the *visible* part; the bulk share is the *hidden* part. Total information is preserved; only the visible share is rationed.

- **Exit condition.** Reader understands the entropy bounds as statements about brane-accessible information, not about total information.

## §6.5 Where the Information Goes: The 6D Resolution — ~1700 words (central section)

### §6.5.1 The Hilbert space decomposition
Define:
$$(5.6.8)\quad \mathcal H_\text{total} = \mathcal H_\text{brane} \otimes \mathcal H_\text{bulk},$$
where $\mathcal H_\text{brane}$ is the Fock space of brane-mode occupations (Vol 4 Ch 6) and $\mathcal H_\text{bulk}$ is the Fock space of Waters-Below (and Waters-Above) field excitations (Vol 1 Ch 6).

### §6.5.2 The 4D effective theory is a reduction
A brane-bound observer (i.e., anyone at $r > r_s$) has access only to observables in $\mathcal H_\text{brane}$. Their density matrix is obtained by tracing over $\mathcal H_\text{bulk}$:
$$(5.6.9)\quad \rho_\text{brane}(t) = \text{tr}_\text{bulk}\,\rho_\text{total}(t).$$
Even if $\rho_\text{total}$ is pure, $\rho_\text{brane}$ is generally mixed. The mixing is *not* information loss — it is entanglement with an inaccessible subsystem, exactly the same as in ordinary thermodynamics (Vol 3 Ch 12 §12.5).

### §6.5.3 Theorem 5.6.2: The Mathur theorem does not apply to the zone framework
**Lemma 5.6.2.** *Premise M1 of Theorem 5.6.1 (exterior Hilbert space is complete) is violated in the zone framework, because the bulk Hilbert space is separately populated and is causally connected to the brane through the boundary coupling term of Vol 1 Ch 6.*

**Proof.** From Vol 1 Ch 6 Eq. (1.6.21), the Waters-Below field has an independent set of creation operators $\hat b^\dagger_k$ with $[\hat a_k, \hat b^\dagger_{k'}] = 0$. Therefore $\mathcal H_\text{brane}$ and $\mathcal H_\text{bulk}$ are distinct Hilbert-space factors; the brane alone is not the full Hilbert space. $\square$

### §6.5.4 Theorem 5.6.3: Unitarity of 6D evolution
**Theorem 5.6.3 (Unitarity).** *The full 6D Hamiltonian $\hat H_\text{6D}$ is self-adjoint on $\mathcal H_\text{total}$. Therefore the time-evolution operator $\hat U(t) = e^{-i\hat H_\text{6D}t/\hbar}$ is unitary, and pure states evolve to pure states.*

**Proof sketch.** The 6D action of Vol 1 Ch 4 is real and local; its Legendre transform to a Hamiltonian is a Hermitian differential operator on $\mathcal H_\text{total}$. Standard self-adjointness arguments (Reed–Simon, Vol 4 §4.3.4 reference) show it is essentially self-adjoint. Stone's theorem then guarantees unitarity of the evolution. $\square$

### §6.5.5 The mechanism in plain words
Infalling matter deposits information into $\mathcal H_\text{bulk}$ as Waters-Below field configurations (the $\Psi_\text{WB}$ mode amplitudes). Bulk-to-brane coupling (via the junction condition at the breach edge) transfers those amplitudes back to outgoing brane modes during the emission process. Over the lifetime of the black hole, every bit that fell in is emitted once; cumulatively, the full state $\rho_\text{total}$ remains pure throughout.

**[FIGURE 5.6.3 placed here.]** 4D vs 6D Hilbert space picture.
**[FIGURE 5.6.4 placed here.]** Information-flow arrow diagram.

### §6.5.6 Why this is a genuine mechanism, not a relabeling
Compare honestly with the "remnant" proposal. Remnants also say information is hidden somewhere; they fail because there is no Planck-size object with enough internal states to hold $O(S_\text{BH})$ bits. The zone framework differs in three checkable ways:

1. **The bulk has a Lagrangian.** We can compute its entropy density from Vol 1 Ch 6 and show it is large enough.
2. **The bulk is causally connected to the brane via an explicit coupling term.** The "how does the information come back out?" question has a specific answer: through the boundary coupling.
3. **The mechanism makes distinct predictions.** §6.8 will list them.

### §6.5.7 What the external observer sees
An external observer at $r \gg r_s$ cannot see the bulk directly. They see the thermal spectrum (5.6.7), with small non-thermal corrections that encode the returning information. Over the full evaporation, the accumulated density matrix of the radiation evolves from mixed-looking back to pure-looking — this is the Page curve, which is the subject of §6.6.

- **Exit condition.** Reader can state Theorems 5.6.2 and 5.6.3, and understand why they dissolve the Mathur obstruction.

## §6.6 The Page Curve as a Theorem — ~1300 words

### §6.6.1 The Page argument, standard form
Page (1993) observed: if the combined system (radiation + black hole) is in a pure random state in a Hilbert space of dimension $D = D_R \cdot D_B$, then the entanglement entropy of the radiation subsystem is
$$(5.6.10)\quad S_\text{rad} \approx \log\min(D_R, D_B),$$
up to subleading corrections in $1/\min(D_R,D_B)$.

### §6.6.2 Mapping Page to the zone framework
Let $D_R(t) = $ dimension of the Hilbert space of emitted radiation at time $t$, and $D_B(t) = $ dimension of the Hilbert space of the remaining (brane-breach + bulk-Waters-Below-inside) system at time $t$. Initially $D_R(0) = 1$, $D_B(0) = e^{S_\text{BH,initial}}$. As radiation proceeds, $D_R$ grows and $D_B$ shrinks.

The Page time $t_P$ is when $D_R(t_P) = D_B(t_P)$, i.e., half the initial entropy has been emitted:
$$(5.6.11)\quad S_\text{emitted}(t_P) = \tfrac{1}{2}S_\text{BH,initial}.$$

### §6.6.3 Theorem 5.6.4: Page curve
**Theorem 5.6.4 (Page Curve).** *Assuming 6D unitarity (Theorem 5.6.3) and Haar-random initial entanglement between brane and bulk, the entanglement entropy of the emitted brane radiation is*
$$(5.6.12)\quad S_\text{rad}(t) = \begin{cases}\log D_R(t) & t < t_P\\ \log D_B(t) & t > t_P\end{cases}$$
*and in particular returns to zero at $t_\text{end}$, the time at which the breach closes.*

**Proof.** Page (1993) + Theorem 5.6.3. The Haar assumption is not strictly needed; what matters is that the entanglement is "generic" in a technical sense. Details in the Page–Lubkin lemma of Vol 4 Ch 6 §6.9. $\square$

**[FIGURE 5.6.5 placed here.]** The Page curve plot.
**[FIGURE 5.6.6 placed here.]** Hilbert-space dimensions plot.

### §6.6.4 Why this is "information returning"
For $t > t_P$, further emission *reduces* the entanglement entropy, because the smaller of the two Hilbert-space dimensions is now the brane-breach side, and it is shrinking. Shrinking entanglement means the accumulated radiation is becoming correlated with itself — information that was "hidden" (in the entanglement with the bulk) is being revealed in the correlations among the later-emitted quanta. This is the precise sense in which "information comes back out."

### §6.6.5 Page time in numbers
For a $10\,M_\odot$ black hole: $S_\text{BH}\approx 10^{79}k_B$; evaporation lifetime $\tau_\text{evap}\approx 10^{67}$ yr; $t_P\approx \tau_\text{evap}/2$. The black hole has to lose about half its mass before the information-rich phase begins. Nobody is observing this on human timescales — but it is a firm theoretical prediction.

### §6.6.6 Why Page doesn't work for pure 4D
Important: Page's argument *requires* that the "black-hole side" of the tensor factorization has dimension $D_B(t)$ that shrinks as radiation proceeds. In pure 4D, without the bulk, the "black-hole side" is... what? The singularity? An empty set? Pure 4D cannot answer this without firewalls or fuzzballs or an invocation of Planck-scale magic. The zone framework has a concrete answer: the "black-hole side" is the combined (shrinking brane patch + shrinking bulk region inside the breach), and both shrink smoothly as the breach closes.

- **Exit condition.** Reader can state the Page curve theorem and understand what "information returning" means operationally.

## §6.7 Resolved vs. Rhetorically Resolved — A Skeptic's Audit — ~1100 words

### §6.7.1 The Skeptic's challenge
The Skeptic reviewer's question for this chapter: **is "resolved" a genuine resolution or a renaming of the mystery?** The section answers directly.

### §6.7.2 The criterion
A resolution is genuine if it (a) identifies the flawed premise in the original problem, (b) replaces it with a derived (not postulated) alternative, (c) derives the original result (Hawking spectrum) from that alternative, and (d) makes distinct, falsifiable predictions.

### §6.7.3 Comparison with partial resolutions
For each competitor, check the four criteria:

| Resolution | (a) Flawed premise identified? | (b) Replacement derived? | (c) Hawking recovered? | (d) New predictions? |
|---|---|---|---|---|
| Firewalls (AMPS 2012) | Yes — equivalence principle at horizon | No — asserted, not derived | Yes | Yes, but violates equivalence principle |
| Fuzzballs (Mathur 2005) | Yes — horizon is sharp | Partial — requires string theory | Yes | Yes, requires stringy microstructure |
| ER=EPR (Maldacena–Susskind 2013) | Yes — locality | Partial — identified only in AdS | Yes | Yes, but AdS-specific |
| Remnants | No — just hides the problem | N/A | Yes | No |
| Zone framework (this chapter) | Yes — exterior completeness | **Yes — from Vol 1 Ch 6 bulk** | Yes | Yes (§6.8) |

The zone framework satisfies all four criteria. Firewalls satisfy (a), (c), (d) but not (b). Fuzzballs satisfy (a), (b)–partial, (c), (d) but require exotic microstructure. ER=EPR is limited to AdS.

### §6.7.4 The three ways this chapter could still be wrong
Honesty requires listing them.

1. **The Waters-Below coupling might not be strong enough.** If the coupling is too weak, the bulk cannot thermalize on the Page timescale, and the Page curve would be modified. This is gap G4.
2. **The Bogoliubov computation is WKB.** Corrections at the next order in $1/M$ might change the spectrum at the level of $O(1/M)$. Gap G1.
3. **The endpoint of evaporation is non-semiclassical.** When $A \to \ell_P^2$, the chapter has no first-principles dynamics. Gap G2.

None of these affects the main theorem (5.6.3). All of them affect quantitative precision.

### §6.7.5 The essential test
If a future experiment measured the Hawking spectrum from a primordial black hole and found it to be exactly thermal with no correlations, the prediction of §6.8 would fail and the resolution would have to be revisited. This is the definition of "not merely rhetorical."

- **Exit condition.** Reader has an honest inventory of where the resolution is strong and where it is provisional.

## §6.8 Falsifiable Predictions and Endpoint Physics — ~900 words

### §6.8.1 Prediction P1: Non-thermal correlations in the Hawking spectrum
Formulate the two-point function of outgoing Hawking modes:
$$(5.6.13)\quad \langle\hat a_{\omega_1}^{\text{out}\dagger}\hat a_{\omega_2}^\text{out}\rangle_\text{correlated} = \delta(\omega_1 - \omega_2)\,n_\text{BE}(\omega_1) + \Delta_{\omega_1\omega_2},$$
where $n_\text{BE}$ is the Bose–Einstein distribution and $\Delta_{\omega_1\omega_2}$ is a non-thermal, non-diagonal piece with amplitude
$$(5.6.14)\quad |\Delta_{\omega_1\omega_2}| \sim e^{-A(t)/(8\ell_P^2)}.$$
The correlations are exponentially small in the residual entropy but are not zero.

### §6.8.2 Prediction P2: Page curve for primordial black holes
If primordial black holes of mass $\sim 10^{12}$ kg exist, they are finishing their evaporation now (lifetime $\sim 10^{10}$ yr). If one were observed throughout its final phase, the cumulative entropy of its emitted radiation should follow the Page curve, not a monotonic curve. The challenge is that we haven't detected any — but if we do, this is an in-principle test.

### §6.8.3 Prediction P3: No pure-thermal "final burst"
As $A \to \ell_P^2$, the chapter predicts a final, short, near-Planck-scale burst that carries the last $O(1)$ bits of information. This burst has a broad (non-thermal) spectrum dominated by the breach-closure dynamics. Observing such a burst (with non-thermal features) would distinguish the zone framework from remnant proposals (which predict *no* final burst because the remnant holds the last bits) and from pure-Hawking (which predicts a thermal burst at $T\to\infty$ at the very end). Gap G2.

**[FIGURE 5.6.7 placed here.]**

### §6.8.4 Prediction P4: Echoes, revisited
Ch 5 §5.8.2 predicted ringdown echoes from the breach boundary. The amplitude of those echoes is now fixed by the coupling constant derived in §6.5 — specifically by how much of the brane mode is reflected at the breach edge versus transmitted into the bulk. The natural prediction is amplitude of order unity times $e^{-\omega r_s/c}$, within LIGO/LISA sensitivity in the next generation of detectors.

### §6.8.5 The endpoint
End of evaporation is a Planck-scale phenomenon and is not derivable from the present chapter alone. We state what must happen: (i) the breach closes smoothly (the membrane re-stitches), (ii) the last $\sim S_\text{BH}/(\log 2)$ bits are emitted in the final Planck-time burst, (iii) the total emitted entropy equals the initial $S_\text{BH}$, and (iv) the final state is pure. Items (i)–(iv) are constraints from the unitarity theorem, not an endpoint derivation. Gap G2.

- **Exit condition.** Reader has four concrete, falsifiable predictions and an honest endpoint caveat.

## §6.9 The Reviewer's Ledger — ~700 words

**[FIGURE 5.6.8 placed here.]** Claim-classification table.

### §6.9.1 Derivations
- Bogoliubov coefficients (5.6.3)–(5.6.6) → Hawking spectrum (5.6.7) — from Ch 5 tension profile + brane wave equation.
- Theorem 5.6.2 (bulk factor exists) — from Vol 1 Ch 6.
- Theorem 5.6.3 (6D unitarity) — from self-adjointness of $\hat H_\text{6D}$.
- Theorem 5.6.4 (Page curve) — from Theorem 5.6.3 + Page lemma.

### §6.9.2 Inheritances
- Breach, tension profile, $S_\text{BH}$, $T_H$ from Ch 5 §5.6.
- Waters-Below field structure and coupling from Vol 1 Ch 6.
- Boltzmann–Shannon entropy identity from Vol 3 Ch 12.
- Bogoliubov transformation technique from Vol 4 Ch 6 §6.6.
- Liouville theorem from Vol 3 Ch 12.

### §6.9.3 Conjectures / gaps
- G1 (MED): WKB order in Bogoliubov.
- G2 (MED): Evaporation endpoint dynamics.
- G3 (LOW): Explicit form of correlation (5.6.13) at mode-by-mode level.
- G4 (MED): Waters-Below coupling strength sufficient for Page thermalization.

### §6.9.4 Note to the Skeptic
Direct answer to "is *resolved* genuine?" — see §6.7. The resolution satisfies the four criteria of a genuine resolution; three open gaps are quantitative, not structural.

### §6.9.5 Note to the Theologian
No theological claims in this chapter. "Information preservation" is a theorem about unitary evolution of a Hamiltonian on a Hilbert space. The word "Firmament" is used only as the Vol 1 Ch 5 name for the 3-brane.

### §6.9.6 Note to the "But Why?" Reader
Seven-question answer format, one sentence each, as in Ch 5 §5.9.5.

### §6.9.7 Forward links
- Ch 7 (Singularity Resolution) will use the brane-reopening dynamics previewed at the endpoint.
- Ch 11 (DM/DE) will revisit the Waters-Below Hilbert space at cosmological scales.
- Vol 6 will address G1–G4.

## §6.10 Problem Sets — ~600 words

**Computational:** P6.1–P6.5 on Hawking temperature, Page time, correlation amplitude, tortoise-coordinate algebra, and grey-body scaling.
**Conceptual:** P6.6–P6.9 on the Mathur theorem premises, the role of the bulk, the firewall question, and the Page curve.
**Challenge:** P6.10–P6.12 on Bogoliubov coefficient computation, Kerr extension, and zero-reflectivity limit.

## Figure Audit (Phase 2 checklist)

- [x] Fig 5.6.1 — spatial/conceptual: the paradox setup (3 panels). REQUIRED.
- [x] Fig 5.6.2 — spatial + plot: the turning point and effective potential. REQUIRED.
- [x] Fig 5.6.3 — conceptual: 4D vs 6D Hilbert space. REQUIRED (central).
- [x] Fig 5.6.4 — schematic: information flow arrows across the breach. REQUIRED.
- [x] Fig 5.6.5 — plot: the Page curve. REQUIRED.
- [x] Fig 5.6.6 — plot: Hilbert-space dimensions crossing. REQUIRED.
- [x] Fig 5.6.7 — plot: Hawking spectrum residuals. REQUIRED.
- [x] Fig 5.6.8 — table-figure: Reviewer's Ledger. REQUIRED (parallel to Ch 5 Fig 5.5.7).

All figure placeholders trace to a spec row above. Figure density: 8 figures / ~11,000 words — on the high end of the Foundations target, appropriate because this chapter is unusually spatial/conceptual.

---
*End of CHAPTER_OUTLINE.md for Vol 5 Ch 6. Ready for Phase 3: Draft.*
