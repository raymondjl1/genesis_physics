---
product: Foundations Vol 4 — The Quantum World
chapter: 14
title: Beyond the Standard Model
status: DRAFT
created: 2026-04-09
---

# Chapter 14
# Beyond the Standard Model

> *"For now we see through a glass, darkly; but then face to face: now I know in part; but then shall I know even as also I am known."*
> — 1 Corinthians 13:12 (KJV)

---

## §14.0  The Bill Comes Due

Imagine a seminar room. It is late in the afternoon of the last day of a week-long workshop on the foundations of the Standard Model, and a visiting physicist — call him the Skeptic, because the Skeptic is always in the front row and is always visiting — has just sat through a thirteen-chapter guided tour. He has seen the Schrödinger equation derived as the slow-envelope limit of a Firmament membrane wave equation (Ch 2). He has seen the uncertainty principle emerge from a 6D embedding (Ch 3). He has watched Bell's inequality violated by a bulk zone correlator rather than by spooky action at a distance (Ch 4). He has worked through renormalization as a zone-boundary regulator (Ch 8), listened politely to the derivation of QED from the firmament Lagrangian (Ch 7), and nodded — or at least not walked out — when the SU(3) × SU(2) × U(1) gauge group fell out of the isometries of a 6D manifold (Ch 11, with the QCD color sector extended in Ch 12). In the final chapter of Part III he saw the CKM and PMNS matrices emerge from overlap integrals on the ξ-ladder and the η-boundary, respectively, with the three-generation count handed down rigorously from Ch 10 §10.3 (Ch 13).

Now the Skeptic raises his hand. He has one question, and it is the only question that matters for a framework of this kind. "All right," he says. "I grant, for the sake of argument, that the Standard Model is in your framework. Now tell me something the Standard Model does not say — and tell me how I would kill your framework if it were wrong."

That is this chapter.

Chapter 14 is the capstone of Volume 4. It is the chapter where the bill comes due. Chapters 10 through 13 spent hundreds of pages *reproducing* what was already known — the particle spectrum, the gauge couplings, the Higgs mechanism, the mixing matrices. Reproduction is necessary, and it is the minimum anyone should ask of a framework that claims to derive physics from Genesis; if a framework cannot reproduce the Standard Model, it is not ready to be discussed. But reproduction is not enough. Any theory that can *only* reproduce what is already known is indistinguishable from the Standard Model plus ornamentation. Genesis Physics, if it is to earn its seat at the table, must say at least one thing that the Standard Model does not say, and it must say it in a form the experimenters can test.

This chapter has three jobs, and only three.

The first is to name the framework's **new predictions** — the places where the zone architecture says something the Standard Model does not, with a number attached. Dark matter candidates from the Waters Below with specific masses and couplings. Dark energy from the Waters Above with a specific equation of state. Collider signatures: a boson-mass precision envelope, a fixed generation count, a Higgs decay pattern, a top-decay-width discrepancy. These are the places where the framework pokes its head above the Standard Model and says, *look here*.

The second is to write down **falsification criteria**. Every prediction must come with a threshold. If the W boson mass is measured to shift by more than two percent, the Ch 11 derivation is wrong and the framework is wrong. If a fourth-generation quark is discovered at any mass, the topological count of Ch 10 is wrong and the framework is wrong. If the dark-energy equation of state is measured to deviate from $w = -1$ by more than five percent, the tree-level Waters Above vacuum is wrong. The Skeptic's test, at every step: *does this prediction have a number, and does the number have a threshold?* If not, the prediction is decorative, and this chapter does not permit decorative predictions.

The third is to consolidate, into a single document, the **research roadmap**: every open problem that Chapters 1 through 13 of this volume left behind. Not as a confession, and not as an apology, but as an audit. Two blockers. Four high-priority gaps. Three medium, three low. Each with a GitHub issue number, a priority label, an effort estimate, and — where the research files have it — a proposed resolution path. The research roadmap is the framework's honest answer to the question "what do you owe?" It is also, not incidentally, the test suite that Volume 6 will inherit.

The honesty commitment that Chapter 13 stated at the end of its opening section still holds. Every numerical result in this chapter inherits the fermion-mass error bars of Chapter 10 — which range, at their worst, from fifteen percent to factors of a thousand. Structural results — the three-generation count, the existence of exactly one CKM CP phase, the unitarity of PMNS — do not inherit those error bars, and they are the ones this chapter treats as rigorous. Numerical results are reported with their labels. Open problems are reported as open. There is no place in this chapter where a gap is hidden behind a softening word. The one-thousand-fold mass-scale problem is named as "the one-thousand-fold mass-scale problem" — not as "an outstanding precision question" or "a residual issue." The spin-1/2 blocker is named as a blocker. The CP phase is reported at its current order-of-magnitude precision and no better. This is not modesty; it is the minimum the framework can afford if it wants the Skeptic to come back tomorrow.

Here is the roadmap. §14.1 returns briefly to the hierarchy problem that Vol 2 Ch 9 solved, and points at Vol 2 Ch 9 for the full treatment — this chapter will not re-derive it. §14.2 collects four dark-matter candidate classes from the zone architecture, gives each a mass, a coupling, and a direct-detection signature, and makes the explicit prediction that no WIMP sits at the electroweak scale. §14.3 turns to the Waters Above, states the tree-level vacuum-energy result, names the cosmological-constant problem as the framework's largest cosmological debt, and predicts a static equation of state $w = -1$ that future surveys will either confirm or falsify. §14.4 collects five collider predictions in numbered form, each with its threshold. §14.5 is the falsification table — fourteen rows, every prediction in the chapter in one place, with the Skeptic's line of sight to every test. §14.6 is the research roadmap. §14.7 hands off to Volumes 5 and 6, and the problem set follows.

It is a short chapter — about twenty-five pages — by design. There is no structurally new derivation to introduce here. The physics was already built in Chapters 10 through 13. What remains is to name the debts, write down the predictions, hand the test suite to the experimentalists, and close the volume. A chapter that tried to do more would be writing checks Chapter 13 has not yet cashed.

One sentence to set the tone for what follows: *there are no new derivations in this chapter; there are only debts being named and predictions being staked.*

[Fig 4.14.1: Chapter roadmap. Four panels arranged left to right. Panel 1: "The hierarchy recap" pointing back to Vol 2 Ch 9. Panel 2: "The dark sector" — four candidate-class icons labeled A–D. Panel 3: "The collider predictions" — a schematic of the LHC with five labeled prediction arrows. Panel 4: "The ledger" — two stacked blocks labeled "Falsification Table" (§14.5) and "Research Roadmap" (§14.6), each with an arrow pointing forward to Vol 5 and Vol 6. A thin line labeled "the honesty commitment" runs under the whole figure.]

---

## §14.1  The Hierarchy Problem, Briefly

The largest open problem in the Standard Model, considered as a purely quantum field theory, is not the absence of gravity and not the absence of dark matter. It is the hierarchy between the electroweak scale and the Planck scale. The Higgs vacuum expectation value is $v_B = 246.22$ GeV. The Planck mass is $M_{\rm Pl} \approx 1.22 \times 10^{19}$ GeV. The ratio is seventeen orders of magnitude, and there is nothing in the bare Lagrangian that keeps the Higgs mass from running quadratically to the cutoff. In the Standard Model, one fine-tunes the bare Higgs mass against its radiative corrections to approximately one part in $10^{34}$ in order to keep $m_H = 125$ GeV, and the tuning is miraculous at every order of perturbation theory.

This is the hierarchy problem, and it is why the Standard Model has always felt, to its practitioners, like a low-energy effective description of something deeper.

Volume 2 Chapter 9 solved it — as a problem of geometry, not as a problem of fine-tuning. The argument of Vol 2 §9.4 is as follows. In the zone architecture, the Firmament is embedded in a 6D manifold with two extra directions. The Waters Above extend outward in a compact ξ-direction to a scale $\xi_A \approx 3 \times 10^{26}$ m — essentially cosmological, essentially infinite from the perspective of any subatomic process. The Waters Below extend inward in a compact η-direction to a scale $|\eta_B| \approx 1.3 \times 10^{-15}$ m — small, nuclear. The Firmament itself sits at $\eta = 0$ as a boundary between the two. The electroweak scalar $\Psi_B$ lives in the Waters Below and has a potential whose minimum is set by the boundary condition at $\eta = \eta_B$, which in turn depends on the geometric scale $|\eta_B|$. The Planck scale, by contrast, is set by the full 6D Ricci curvature, which depends on the product $\xi_A \cdot |\eta_B|$ through the Einstein-Hilbert action.

The key equation, inherited from Vol 2 Ch 9 equation (2.9.31), is the scale ratio:

$$\frac{v_B}{M_{\rm Pl}} \sim \left(\frac{|\eta_B|}{\ell_{\rm Pl}}\right)^{-\alpha}, \tag{4.14.1}$$

where $\ell_{\rm Pl} \approx 1.6 \times 10^{-35}$ m is the Planck length and $\alpha$ is an $O(1)$ exponent determined by the Firmament Lagrangian (Vol 2 §9.4 gives $\alpha \approx 1$ for the simplest boundary potential). Plugging in numbers, $|\eta_B|/\ell_{\rm Pl} \sim 10^{20}$, and $(10^{20})^{-1} = 10^{-20}$, which is within a decade of the observed ratio $v_B/M_{\rm Pl} \sim 2 \times 10^{-17}$. The residual two orders of magnitude are absorbed into the $O(1)$ dimensionless prefactor $\alpha$ and into the precise form of the boundary potential; Vol 2 §9.4 narrows it further with a one-loop matching calculation.

The essential observation is that the hierarchy is not tuned. It is *geometric*. Nothing in the Lagrangian has to be adjusted to twenty decimal places. The small ratio $v_B/M_{\rm Pl}$ is small because $|\eta_B|$ is large compared to the Planck length, and $|\eta_B|$ is large for the same reason that the Waters Below extend down only as far as the typical nuclear scale rather than all the way to the Planck length. There is no miracle, and the Higgs mass does not run to the cutoff because the 6D Lagrangian does not contain scalar self-energy divergences of the kind the 4D Standard Model has. Vol 4 Ch 8 already computed the one-loop Higgs mass correction in the zone-QFT formalism and found it finite.

So: the hierarchy problem is not a problem here. It was never a problem here. It was a problem in the Standard Model because the Standard Model is a 4D effective theory with a cutoff it cannot explain; when embedded in a 6D manifold with geometric boundary conditions, the tuning vanishes.

What Vol 2 Ch 9 did *not* do, and what this chapter does not do either, is explain why $|\eta_B|$ has the value it does. The geometric scale $|\eta_B| \approx 1.3 \times 10^{-15}$ m is currently an input to the framework; it is matched to the observed electroweak scale, not derived from a more fundamental principle. The question "why $v_B = 246$ GeV rather than, say, $10^{-8}$ GeV or $10^{13}$ GeV?" is a question about the stability of the ξ-modulus potential, and it is listed in §14.6 as open problem **RR-9** (moduli stabilization). It is a medium-priority item. It is real, it is unresolved, and the framework does not yet know the answer. What the framework *does* know is that once $|\eta_B|$ takes the value it takes, the hierarchy it produces is natural, and the scale separation does not require tuning.

This section is a recap. The reader who wants the full derivation should return to Vol 2 Ch 9 §9.4 and in particular equations (2.9.25)–(2.9.34). What this chapter wants to do is move on — to the sectors of the framework the Standard Model does not contain at all.

---

## §14.2  Dark Matter from the Zone Architecture

Dark matter is the clearest experimental fact the Standard Model cannot accommodate. Roughly twenty-six percent of the energy budget of the observable universe is carried by something that is not on the Particle Data Group's table. We see it gravitationally — in rotation curves, in lensing arcs, in the CMB acoustic peaks — and we do not see it anywhere else. No photon coupling. No hadronic signature. No neutrino-like weak cross-section at the level that would have lit up the direct-detection experiments long ago. Any candidate framework for the foundations of physics has to say *something* about where dark matter lives, what it is made of, and why it has so far been invisible.

The zone architecture of Vol 1, it turns out, has more than one place dark matter could live. The 6D manifold has two Waters, a membrane, and a set of boundary sectors, and not every sector of that architecture has a direct Yukawa coupling to the Standard Model fermions. The sectors that do couple produced the particles of Chapter 10. The sectors that do not couple are, by construction, dark. This is not a matter of adding new fields by hand; it is a matter of asking which of the fields the framework already contains fail to couple into the Chapter 10 vertex structure.

Four structurally distinct candidate classes emerge. The framework does not promote any single one as *the* answer — it offers all four as possibilities, each with its own mass scale, its own coupling regime, and its own experimental signature. A genuine dark-matter discovery could, in principle, select among them.

**Class A — Heavy KK excitations in the η-direction.** The Waters Below are bounded in η by a potential wall at $\eta = \eta_B$, and the transverse modes of that potential form a Kaluza-Klein tower. Chapter 6 built the tower and computed its mass spectrum in equation (4.6.17):

$$M_{m,\eta} = \hbar c \cdot \frac{m\pi}{|\eta_B|}, \qquad m = 1, 2, 3, \ldots \tag{4.14.2}$$

With $|\eta_B| \approx 1.3 \times 10^{-15}$ m, the first KK mode sits at $M_{1,\eta} \approx 0.95$ GeV, the second at $\approx 1.90$ GeV, the third at $\approx 2.85$ GeV, and so on up to the Firmament cutoff. This is the same tower that gave the pion and the lowest hadronic resonances their orbital structure in Chapter 12. What is relevant for dark matter is that the tower has a Z$_2$ selection rule inherited from the η-parity of the Waters Below boundary: modes with odd $m$ couple to the Standard Model charged-current vertices as ordinary mesons would, while modes with even $m$ couple only at loop level, and modes above $m = 3$ are kinematically stable against decay into lighter odd-$m$ modes over cosmological timescales.

The candidate is the even-$m$ KK mode at $m = 2$, mass approximately 1.9 GeV, with a coupling to Standard Model matter that runs through the same η-boundary vertex as the Z boson but is suppressed by one loop factor ($\sim \alpha_W / 4\pi \approx 2 \times 10^{-3}$). Its annihilation cross-section into Standard Model pairs sits in the range

$$\sigma_{A}^{\rm ann} \sim 10^{-44} \text{ to } 10^{-42} \text{ cm}^2, \tag{4.14.3}$$

which is a few orders of magnitude above the current XENONnT exclusion line for nucleon-recoil at that mass. Class A is the Genesis framework's best collider-accessible dark-matter candidate, and it is its most directly falsifiable. If the SuperCDMS experiment, or the next-generation directional detectors now being commissioned, reach a nucleon-recoil cross-section of $10^{-46}$ cm$^2$ at the 1–2 GeV mass window and find nothing, Class A is ruled out. The framework loses one of its four candidate classes and must either fall back on B–D or acknowledge that dark matter lives outside the current zone architecture.

**Class B — η-boundary localized modes (sterile neutrinos).** At the Waters Below boundary, Chapter 13 §13.4 showed that there exists a second sector of low-lying modes — ripples on the boundary wall — whose overlap with the Higgs profile is small enough that their Yukawa masses are suppressed. These are the modes that gave the PMNS matrix its large mixing angles in Ch 13. Not all of the boundary ripples couple into the observed neutrino sector, however. Some are orthogonal to the three PMNS mass eigenstates by topological selection and therefore do not participate in the ordinary weak charged current at all. In Standard Model language, these are sterile neutrinos.

The framework's sterile neutrino candidate has a mass in the range

$$m_{\nu_s} \sim 10^{-2} \text{ to } 1 \text{ eV}, \tag{4.14.4}$$

with the exact value set by the seesaw between the η-boundary ripple and a residual Majorana contribution from the Waters Above — both of which are currently labeled as open problem **RR-8** in §14.6. Couplings to ordinary neutrinos are suppressed by the same overlap integrals that give the PMNS mixing angles; a typical mixing with active neutrinos is of order $|U_{\alpha s}|^2 \sim 10^{-3}$ to $10^{-4}$. Direct-detection cross-sections are cosmologically irrelevant (well below $10^{-50}$ cm$^2$), but neutrino oscillation experiments — in particular short-baseline reactor experiments such as PROSPECT, STEREO, and their successors — can constrain the mixing directly.

Class B does not supply the full dark-matter budget; a sub-eV sterile neutrino is too light to explain galactic rotation curves by itself. But it is a portion of the dark-matter budget the framework genuinely predicts, and any sterile-neutrino discovery in this mass range would be a framework prediction in action. The framework falsifies here not by non-discovery (absence of a sub-eV sterile neutrino is hard to rule out) but by *structure*: if a sterile neutrino is discovered at a mass above 10 eV, or with a mixing angle above $10^{-2}$, the η-boundary ripple mechanism of Ch 13 is not the right mechanism, and the framework owes a new one.

**Class C — Vortex-sector dark states.** The ξ-ladder of Chapter 10 has three normalizable bound states (the three generations) and an unbounded continuum of states above the well. The bound states acquired Yukawa masses through the overlap integral (4.10.18) because they localized near the Firmament. The continuum states do not localize; they propagate freely in the Waters Above, and their overlap with the Higgs profile is zero to within the framework's approximation. They therefore acquire no Yukawa mass, no electromagnetic charge, no QCD color, and no weak isospin. They couple to ordinary matter only through the 6D gravitational interaction — that is, through zone-curvature exchange, which at low energies looks like a Planck-suppressed four-fermion contact interaction.

The candidate is a WIMPless state: a freely propagating scalar or vector mode in the Waters Above, with mass set by whatever the ξ-ladder continuum cutoff turns out to be. Estimates from the Ch 10 §10.6 analysis put the continuum onset at

$$m_C \sim 10 \text{ to } 100 \text{ GeV}, \tag{4.14.5}$$

but with a gravitational cross-section of approximately

$$\sigma_{C}^{\rm nucleon} \sim G_F^2 m_C^2 \cdot (m_C / M_{\rm Pl})^4 \sim 10^{-60} \text{ cm}^2, \tag{4.14.6}$$

which is untestable by any direct-detection experiment presently envisioned. Class C is therefore a *cosmologically relevant* candidate — the right mass range, the right abundance — that is *detectably invisible* by design. The framework does not claim this is a virtue; it is a limitation. Cosmological signatures (free-streaming length, sub-halo power spectrum, CMB lensing) are the only observational windows, and Vol 5 will take them up.

**Class D — Radion / dilaton modes.** The distance between the two Waters — the ξ-modulus — can oscillate. Its quantum is a scalar field, the radion, whose mass is set by whatever potential stabilizes the ξ-modulus. In the framework's current analysis, moduli stabilization is open problem **RR-9** in §14.6, which is why the radion mass is not yet predicted from first principles. A typical stabilization mechanism based on Casimir forces (Vol 4 Ch 9) gives a radion mass of

$$m_{\rm rad} \sim 10^{-3} \text{ to } 10^{-1} \text{ eV}, \tag{4.14.7}$$

in the meV range, with a gravitational-strength coupling to all Standard Model fields. Radions in this mass range are classified as *ultralight* dark matter and have distinctive signatures in atomic-clock experiments, resonant-mass detectors, and pulsar-timing arrays. The Genesis framework's Class D prediction overlaps with the search windows of the MAGIS-100, ACME, and EP-SENSE experiments.

**The critical observation.** None of Classes A, B, C, or D sits at the canonical WIMP mass of 100 GeV with a weak-scale cross-section of $10^{-39}$ cm$^2$. The Genesis framework is *not* a WIMP framework. It never was. Its dark-matter candidates are either sub-GeV (Class A), sub-eV (Class B), gravitationally-coupled (Class C), or ultralight (Class D). If, in the next decade, a direct-detection experiment at the electroweak scale discovers a particle at, say, 50 GeV with a nucleon cross-section of $10^{-45}$ cm$^2$, the Genesis framework does not accommodate it. The discovery would not necessarily kill the framework — a fifth candidate class could be added by extending the zone architecture — but it would mean that the four classes above are incomplete, and the framework would owe the community a reason for the gap.

We state this as a formal result.

**Result 14.1 (APPROXIMATE, falsifiable).** *Genesis Physics predicts that the dark-matter sector consists of one or more of the four classes above: a KK mode near 0.95–1.9 GeV (Class A), a sub-eV sterile neutrino from the η-boundary (Class B), a gravitationally-coupled continuum state in the Waters Above (Class C), or a meV-scale radion (Class D). It predicts, rigorously from the structure of the Yukawa overlap integral, that **there is no 10 GeV–10 TeV WIMP** with electroweak-scale nucleon couplings. The discovery of such a particle in the canonical WIMP window would require extending the zone architecture beyond its current form.*

The approximate label reflects the fact that the candidate masses and couplings depend on numerical inputs the framework has not yet pinned down (the η-boundary potential, the ξ-modulus stabilization, the Yukawa overlap integrals of Ch 10). The falsifiable label reflects the fact that the no-WIMP prediction is structural — it follows from the fact that the ξ-ladder bound states are the *only* states that acquired Yukawa masses, and no structural modification of Ch 10 can put a new state at 100 GeV without breaking the generation count of Ch 10 §10.3.

[Fig 4.14.2: Dark-matter candidate space. A log-log plot of candidate mass (x-axis, from $10^{-6}$ eV to $10^5$ GeV) against nucleon-recoil cross-section (y-axis, from $10^{-60}$ cm$^2$ to $10^{-38}$ cm$^2$). The four Genesis classes are marked as ellipses: Class A (A) at $0.95$–$1.9$ GeV, $\sim 10^{-44}$ cm$^2$; Class B (B) at $10^{-2}$–$1$ eV, $\sim 10^{-50}$ cm$^2$; Class C (C) at $10$–$100$ GeV, $\sim 10^{-60}$ cm$^2$; Class D (D) at $1$–$100$ meV, no direct nucleon coupling (marked with a special symbol). The current XENONnT and LZ exclusion curve is drawn as a solid line. The canonical WIMP window (100 GeV, $10^{-45}$ cm$^2$) is shown as an empty box with a line through it and the label "no Genesis candidate."]

---

## §14.3  Dark Energy from the Waters Above

The Waters Above carry a complex scalar field $\Psi_A$. Its potential, derived in Vol 2 §2.4 and written in the form

$$V(|\Psi_A|^2) = \frac{\lambda_A}{4}\left(|\Psi_A|^2 - v_A^2\right)^2, \tag{4.14.8}$$

has a ground state at $|\Psi_A| = v_A$, with $\lambda_A$ an $O(1)$ dimensionless coupling and $v_A$ a mass scale set by the Vol 2 Ch 10 running-coupling analysis at approximately

$$v_A \approx 10^{16} \text{ GeV}. \tag{4.14.9}$$

This scale is adjacent to the canonical GUT scale but not identified with it; the framework's grand unification, if it exists, is open problem **RR-5** and is discussed in §14.6.

At tree level, the vacuum energy of $\Psi_A$ in its ground state is zero. This follows trivially from the form of the potential: $V(v_A^2) = 0$. No cosmological constant is produced at tree level, and if the tree-level answer were the whole answer, the framework's prediction for the vacuum energy density of the universe would be *exactly zero*.

The tree-level answer is not the whole answer. Loop corrections to the vacuum energy from the $\Psi_A$ field, and from the Standard Model fields that couple to it indirectly through the Firmament, are generically of order

$$\rho_{\rm vac}^{\rm loop} \sim \frac{v_A^4}{(4\pi)^2} \sim 10^{62} \text{ GeV}^4, \tag{4.14.10}$$

which is approximately 184 orders of magnitude larger than the observed dark-energy density,

$$\rho_{\rm DE}^{\rm obs} \approx 10^{-122} \text{ GeV}^4. \tag{4.14.11}$$

This is the cosmological-constant problem, stated in the framework's language. It is an honest statement of the problem, not a dressing-up of it; at loop level, the framework has exactly the same discrepancy every other quantum field theory has, and it has it for exactly the same reason. Nothing in the tree-level zone architecture has a symmetry that forces the loop correction to cancel.

What the framework *does* offer, tentatively, is a mechanism for the cancellation. The $\Psi_A$ and $\Psi_B$ fields are related by a Z$_2$ symmetry in the Vol 1 Ch 3 construction — the Waters Above and Waters Below are two reflections of a single underlying structure. Under that Z$_2$, the sign of the vacuum energy contribution from each Waters sector is opposite, and the *net* vacuum energy contains a leading cancellation between the two. The cancellation is not exact because the Z$_2$ is softly broken by the Firmament boundary conditions (the Waters are *not* identical; the Waters Below supports quarks and gluons while the Waters Above does not), but it is large enough to suppress the loop-level $10^{62}$ GeV$^4$ down by many orders of magnitude. How many? The framework does not yet know. Vol 5 will return to this; the problem is listed in §14.6 as **RR-12** (among low-priority items, not because it is unimportant — it is the single largest quantitative problem in theoretical physics — but because closing it requires tools the Vol 5 cosmological sector has not yet developed).

For *this* chapter, what matters is the tree-level prediction and its falsifiability. At tree level, the Waters Above vacuum is static. Its equation of state is

$$w \equiv \frac{p_{\rm DE}}{\rho_{\rm DE}} = -1 \quad \text{(tree level)}. \tag{4.14.12}$$

A cosmological constant, in the standard sense. The framework makes no prediction at tree level of any dynamical dark energy — no quintessence, no phantom sector, no interacting dark-energy model. The $\Psi_A$ field in its ground state is a constant, and a constant scalar field has $w = -1$ identically.

This is a prediction, and it is falsifiable. The current best measurement of $w$ from DESI and prior surveys gives $w = -0.997 \pm 0.03$, consistent with $-1$. In the next decade, DESI and Euclid together are expected to push the precision on $w$ to approximately $\pm 0.01$. If the measurement converges on $w = -1$ within that precision, the framework's tree-level prediction survives. If it converges on a value like $w = -0.90 \pm 0.02$ or $w = -1.08 \pm 0.02$, the framework's tree-level vacuum cannot accommodate it — the Waters Above is a rigid scalar in its ground state, and it cannot be made to run dynamically without introducing a new time-dependent sector. Such a measurement would not kill the framework outright, because loop-level and cosmological evolution effects could in principle accommodate a running $w$, but it would force the framework's dark-energy sector to be reopened.

We state this as a result.

**Result 14.2 (APPROXIMATE, falsifiable).** *At tree level, Genesis Physics predicts a static dark-energy equation of state $w = -1$. A measurement of $|w + 1| > 0.05$ in future surveys would require the framework to introduce a dynamical dark-energy sector not present in the current Lagrangian.*

The "approximate" label reflects the fact that loop-level corrections could in principle shift $w$ by small amounts that the framework has not yet computed. The falsifiable label reflects the fact that the tree-level prediction $w = -1$ is a consequence of the Waters Above being a rigid scalar in its minimum, not an adjustable input.

One closing observation on the vacuum energy. The framework names the cosmological-constant problem explicitly. It does not claim to solve it. What it does claim — and the claim is modest — is that the *structure* of the problem is different in the zone architecture than in the 4D Standard Model, because the framework has a built-in Z$_2$ that can enforce leading-order cancellation. Whether the cancellation is exact, large, or inadequate is a question for Vol 5 Ch 12, which is where the cosmological sector becomes the foreground.

[Fig 4.14.3: The cosmological-constant gap. A horizontal log-scale bar chart showing four energy scales: $\Lambda_{\rm obs}^{1/4} \approx 10^{-3}$ eV (labeled "observed dark energy"), $v_B = 246$ GeV (labeled "electroweak / Waters Below"), $v_A \sim 10^{16}$ GeV (labeled "GUT-adjacent / Waters Above"), $M_{\rm Pl} \approx 10^{19}$ GeV (labeled "Planck"). The gap between $\Lambda_{\rm obs}^{1/4}$ and $v_A$ is marked with a bracket and the label "184 orders of magnitude: the cosmological-constant problem." An arrow points from $v_A$ back to $\Lambda_{\rm obs}^{1/4}$ with the label "proposed Z$_2$ cancellation — Vol 5 §12."]

---

## §14.4  Predictions Testable at Colliders

We come now to the sharpest section of the chapter: five predictions the framework makes that the LHC and its successors can test directly, with the data they already have or will have in the next decade. Each prediction has a number. Each number has a threshold. Each threshold has an experiment and a timescale. The section is organized as five numbered predictions, each with its own subsection.

### Prediction 14.1 — The boson-mass precision envelope

Chapters 10 and 11 made four quantitative predictions for the masses of the heavy bosons of the Standard Model, each derived from the ξ-ladder overlap integrals and the electroweak symmetry breaking of the Waters Below:

| Observable | Genesis prediction | PDG (2024) | Deviation |
|---|---|---|---|
| $m_t$ | $173.0$ GeV | $173.1 \pm 0.4$ GeV | $0.06\%$ |
| $m_H$ | $125.4$ GeV | $125.09 \pm 0.24$ GeV | $0.25\%$ |
| $M_W$ | $80.42$ GeV | $80.385 \pm 0.015$ GeV | $0.04\%$ |
| $M_Z$ | $91.64$ GeV | $91.1876 \pm 0.0021$ GeV | $0.50\%$ |
| $\rho$ parameter | $1.000037$ | $1.00037 \pm 0.00010$ | $0.1\%$ |

The first four are mass predictions; the fifth is the $\rho$ parameter, $\rho = M_W^2/(M_Z^2 \cos^2\theta_W)$, which is a precision constraint on the electroweak symmetry-breaking sector and is the cleanest test of the Higgs-doublet structure that Ch 11 §11.5 derived.

Every entry in this table is *already within its error bars* of the framework's prediction. This is a non-trivial fact. A random model of electroweak symmetry breaking would not hit four boson masses simultaneously to 0.5% precision or better. The fact that the Genesis framework does — with zero free parameters in the boson-mass sector, all four numbers coming from the same geometric coupling $g_W \approx 0.653$ derived in Ch 11 §11.5 — is the single strongest piece of numerical evidence the volume contains.

The prediction is that *all five entries remain simultaneously within their current precisions*. Specifically: the framework predicts that no future precision measurement will shift any of the four boson masses by more than 2% from its current PDG value, and that the $\rho$ parameter will remain within 0.5% of its current value. If any single mass shifts by more than 2% — say, if HL-LHC top-mass measurements converge on $m_t = 176.5$ GeV with sub-GeV precision, more than 2% above the current value — the derivation of Ch 11 §11.5 is wrong, and the framework fails.

**Falsification threshold:** any single boson mass deviating from current PDG values by more than 2%, *or* the $\rho$ parameter deviating by more than 0.5%.

**Experiment:** HL-LHC precision program, 2024–2030 timeframe. The W-mass measurement from CMS and ATLAS, in particular, is targeting sub-10 MeV precision; any shift in the central value of that size would be a sharp test.

The reason this prediction has teeth is not that any individual boson mass is special. It is that *four masses plus the $\rho$ parameter* must all simultaneously agree with a framework that has, in the boson sector, exactly one dimensionless geometric input ($g_W$) and one dimensional input ($v_B$). Everything else is a derived quantity. A framework with that much input cannot wiggle out of a 2% shift in any single observable by re-tuning; a shift anywhere is a shift everywhere, and any single shift beyond 2% breaks the simultaneous consistency.

### Prediction 14.2 — Exactly three generations

Chapter 10 §10.3 showed that the ξ-ladder bound-state spectrum on the Vol 1 Ch 5 double-well potential has exactly three normalizable eigenstates. Three, not four, not two. This is a topological fact about the spectral structure of the unperturbed ladder Hamiltonian, and it is the single most robust prediction the framework makes. It does not depend on any numerical input. It does not depend on the Higgs profile, on the Yukawa overlap integrals, or on any of the Ch 10 error bars. It depends only on the shape of the double-well potential, which is set by the Vol 1 Ch 5 zone geometry.

The framework therefore predicts: *the Standard Model has exactly three fermion generations, and there is no fourth*. Not at any mass scale. Not above 1 TeV, not above the LHC kinematic reach, not at the future circular collider (FCC-hh) at 100 TeV, not anywhere. A fourth-generation charged lepton, a fourth-generation up- or down-type quark, or a fourth-generation neutrino (distinct from the sterile neutrino of §14.2, which lives in a different sector) — any of these, at any mass — kills the framework.

**Falsification threshold:** discovery of any fourth-generation particle at any mass at any collider.

**Experiment:** LHC Run 3 (ongoing) for masses up to ~1 TeV; HL-LHC for the range 1–2 TeV; FCC-hh or muon collider for the range above 2 TeV. Current direct bounds exclude fourth-generation quarks below approximately 700 GeV and fourth-generation leptons below approximately 100 GeV; the framework predicts the exclusion extends to arbitrary mass.

We state this as a formal result.

**Result 14.3 (RIGOROUS, structural).** *Genesis Physics predicts exactly three fermion generations. The generation count is a topological consequence of the Vol 1 Ch 5 double-well spectrum and does not depend on any numerical input. Discovery of a fourth-generation fermion at any mass falsifies the framework.*

This is the strongest structural prediction in Volume 4. It is rigorous in the same sense that Ch 13 Result 13.1 is rigorous: it follows from the structure of the framework's core spectral problem, not from any downstream calculation.

> **(Assumption 10.1 — OP-1 / GitHub #1 BLOCKER)** Result 14.3 predicts exactly three generations of spin-½ fermions. The topology argument (double-well on ξ-direction → 3 bound states) is rigorous. However, the identification of those three states as *fermionic* particles — rather than bosonic resonances — depends on Assumption 10.1. The three-generation count is topologically guaranteed; that they are spin-½ fermions obeying Pauli exclusion is assumed. A BSM search for fourth-generation particles is therefore a test of both the topology and Assumption 10.1 simultaneously.

### Prediction 14.3 — The Higgs branching-ratio pattern

The Higgs boson, in the framework's construction (Ch 11 §11.7), couples to Standard Model fermions through the same overlap integrals that give the fermion masses. Its decay branching ratios are therefore direct predictions — no new parameters, no new inputs. Chapter 11 §11.7 recorded the seven dominant channels:

| Channel | BR (Genesis) | BR (PDG) |
|---|---|---|
| $h \to b\bar b$ | $58.0\%$ | $58.4 \pm 0.7\%$ |
| $h \to W^+ W^-$ | $21.5\%$ | $21.4 \pm 0.8\%$ |
| $h \to gg$ | $8.6\%$ | $8.2 \pm 0.4\%$ |
| $h \to \tau^+ \tau^-$ | $6.3\%$ | $6.3 \pm 0.4\%$ |
| $h \to c\bar c$ | $2.9\%$ | $2.9 \pm 0.1\%$ |
| $h \to ZZ$ | $2.6\%$ | $2.6 \pm 0.1\%$ |
| $h \to \gamma\gamma$ | $0.23\%$ | $0.227 \pm 0.010\%$ |

The framework's prediction is that *no new decay mode appears above 0.5% that is not in this list*. In particular: $h \to \text{invisible}$ (i.e., decay into any dark-sector state of §14.2) is predicted to be below 2%. Current ATLAS and CMS bounds on the invisible fraction are at approximately 11% (95% CL), so the framework's 2% prediction is not yet tight but will be tightened at HL-LHC. If the invisible fraction is measured to exceed 5% with 3σ significance, a new decay channel beyond the framework's four dark-matter classes has been opened, and the framework must either identify which of its classes is coupling more strongly than expected or acknowledge that a fifth class exists.

Similarly: $h \to \mu^+\mu^-$ is predicted at the standard-model rate of $\sim 0.022\%$, dominated by the same muon Yukawa that gave the muon mass in Ch 10. Any anomaly in $h \to \mu\mu$ at more than 3σ above this prediction is a signal of flavor-violating new physics the framework does not contain.

**Falsification threshold:** any new decay mode above 0.5% branching ratio not in the seven-channel list, or any listed channel deviating from the Genesis prediction by more than 3σ.

**Experiment:** HL-LHC Higgs precision program, 2024–2035.

### Prediction 14.4 — Flavor-changing neutral currents at Standard Model rates

Flavor-changing neutral currents are the Standard Model's cleanest probe of physics beyond it. In the SM, FCNCs — processes like $t \to c\gamma$, $t \to cZ$, $b \to s\gamma$, $K^0 \to \mu^+\mu^-$ — arise only at loop level, and they are suppressed by the GIM mechanism, which in turn depends on the unitarity of the CKM matrix. Beyond-SM physics with new flavor structure typically violates GIM and enhances FCNC rates by orders of magnitude.

In Genesis Physics, GIM suppression survives. The CKM matrix is $3\times 3$ unitary as a structural result (Ch 13 Result 13.1), and the framework contains no new flavor-violating vertex beyond those already present in the Standard Model. FCNC branching ratios are therefore predicted to equal their Standard Model values:

$$\text{BR}(t \to cZ) \sim 10^{-7}, \quad \text{BR}(t \to c\gamma) \sim 10^{-11}, \tag{4.14.13}$$
$$\text{BR}(K^0 \to \mu^+\mu^-) \sim 10^{-9}, \quad \text{BR}(B_s \to \mu^+\mu^-) \sim 3 \times 10^{-9}. \tag{4.14.14}$$

All four numbers are taken from the SM prediction and inherited by the framework without modification.

**Falsification threshold:** any FCNC rate measured to exceed the SM prediction by more than an order of magnitude.

**Experiment:** LHCb and Belle II, ongoing.

This prediction is weaker than the previous three in the sense that it coincides with the SM's own prediction. But it is strong in the sense that the framework, unlike many BSM models, does not introduce new flavor structure. A discovery of enhanced FCNCs would be a signal the Genesis framework cannot accommodate without modifying its Ch 13 derivation — which, as Ch 13 §13.1 showed, is structural and does not permit such modification.

### Prediction 14.5 — The top-quark decay-width gap

This is the framework's current embarrassment, and it is also its sharpest internal test. Chapter 11 §11.8 computed the top-quark decay width at tree level as

$$\Gamma_t^{\rm tree} = \frac{g_W^2 m_t^3}{32\pi M_W^2} \approx 1.42 \text{ GeV}, \tag{4.14.15}$$

and at next-to-leading order (NLO) as approximately $\Gamma_t^{\rm NLO} \approx 1.56$ GeV. The PDG value is $\Gamma_t^{\rm obs} = 2.00 \pm 0.1$ GeV. The gap between prediction and observation is approximately 25%.

This is a significant discrepancy. It is the largest single gap between a Genesis prediction and a PDG measurement anywhere in the electroweak precision sector, and it is much larger than the 0.04–0.5% agreements reported for the boson masses. A skeptic would be within his rights to point at it and ask the framework to explain itself.

The framework's explanation is that NNLO electroweak corrections — second-order loop effects that have not yet been computed in the zone-QFT formalism — should close the gap. The argument is that the top-quark decay process involves multiple heavy-particle exchanges ($W$, $Z$, $H$) whose interference terms are only captured at NNLO, and in the standard 4D QED/QCD calculation of $\Gamma_t$, the NNLO corrections contribute approximately 20–30% to the total width. If the same magnitude holds in the zone-QFT formalism, the gap closes.

But this is an argument, not a calculation. The framework owes the calculation. The Genesis prediction, therefore, is that when the NNLO calculation is done, the result will shift from 1.56 GeV to approximately 2.0 GeV, closing the 25% gap to within a few percent. If it does not — if the NNLO calculation gives 1.60 GeV or 1.70 GeV and the gap remains open — then the framework's top-sector vertex structure is wrong, and the derivation of Ch 11 §11.8 must be revisited.

This is an internal falsification test. Unlike Predictions 14.1–14.4, it is not a test to be run at a collider. It is a calculation to be done by the framework's own theorists. It is listed as open problem **RR-6** in §14.6, with an effort estimate of 3–4 months and a HIGH priority label.

**Falsification threshold:** NNLO zone-QFT calculation of $\Gamma_t$ gives a value below 1.85 GeV or above 2.15 GeV — that is, fails to close the gap to within the current experimental error bar.

**Experiment:** internal calculation, ~2 years timescale.

### What the five predictions have in common

The five predictions above are not a sampler of optional tests. They are, collectively, the *minimum* the framework must survive in the next decade for it to remain a serious candidate for the foundations of particle physics. Predictions 14.1 and 14.3 are already in the data and must continue to be in the data as precision improves. Prediction 14.2 is a standing sharp knife: one fourth-generation particle, anywhere, at any mass, and the framework dies. Prediction 14.4 is the framework's commitment to *not* introducing new flavor structure. Prediction 14.5 is the framework's acknowledgment that it owes itself a calculation before the next workshop.

The Skeptic, at the end of this section, has his answer. The framework is not decorative. The Skeptic can kill it with any of five different experiments or one internal calculation. That is as testable as foundations physics gets.

[Fig 4.14.4: The boson-mass precision ledger. Five vertical bars, one each for $m_t$, $m_H$, $M_W$, $M_Z$, and $\rho$ (normalized to unity). Each bar shows the Genesis prediction as a solid point, the current PDG value as a hollow point (indistinguishable from the Genesis point at this resolution), and a shaded 2% band above and below the PDG value as the falsification envelope. Caption notes: "all five predictions currently lie within their error bars; the framework's claim is that the bars remain simultaneously satisfied as precision improves."]

---

## §14.5  The Falsification Table

This section is short, because it is a table.

Every prediction named in this chapter has been recorded below, in one place, with its falsification threshold and its experimental context. The Skeptic asked for a single artifact that lets him kill the framework in one direct look; this is it. This table is also the primary deliverable of Chapter 14 to Volume 6: each row will, in Vol 6, expand into a full chapter or section devoted to the experimental program that confronts it.

| # | Observable | Genesis Prediction | Current Measurement | Falsification Threshold | Experiment | Timescale |
|---|---|---|---|---|---|---|
| 1 | $W$ boson mass | $80.42$ GeV | $80.385 \pm 0.015$ GeV | $>2\%$ deviation | CMS/ATLAS W mass | now–2030 |
| 2 | $Z$ boson mass | $91.64$ GeV | $91.1876 \pm 0.0021$ GeV | $>2\%$ deviation | LEP/LHC precision | now |
| 3 | Higgs mass | $125.4$ GeV | $125.09 \pm 0.24$ GeV | $>2\%$ deviation | HL-LHC | 2024–2030 |
| 4 | Top quark mass | $173.0$ GeV | $173.1 \pm 0.4$ GeV | $>2\%$ deviation | HL-LHC | 2024–2030 |
| 5 | $\rho$ parameter | $1.000037$ | $1.00037 \pm 0.00010$ | $>0.5\%$ deviation | precision EW | now |
| 6 | Fermion generation count | exactly 3 | 3 observed | 4th generation at any mass | LHC / HL-LHC / FCC | 2024–2050 |
| 7 | $h \to \gamma\gamma$ branching ratio | $0.23\%$ | $0.227 \pm 0.010\%$ | $>3\sigma$ deviation | HL-LHC | 2024–2030 |
| 8 | $h \to $ invisible branching ratio | $< 2\%$ | $< 11\%$ (95% CL) | $> 5\%$ measured | HL-LHC | 2024–2035 |
| 9 | Canonical WIMP (10 GeV–10 TeV, $\sigma \sim 10^{-45}$ cm$^2$) | **no candidate** | not yet observed | discovery in that window | XENONnT / LZ | 2024–2030 |
| 10 | Dark matter Class A (KK mode at 0.95–1.9 GeV) | $\sigma \sim 10^{-44}$–$10^{-42}$ cm$^2$ | not yet probed | exclusion at $\sigma < 10^{-46}$ cm$^2$ | SuperCDMS, next-gen | 2028–2035 |
| 11 | Dark energy equation of state $w$ | $w = -1$ (tree level) | $w = -0.997 \pm 0.03$ | $|w + 1| > 0.05$ | DESI, Euclid, LSST | 2024–2030 |
| 12 | PMNS unitarity | exact (structural) | $\sim 0.999$ consistent with 1 | violation $> 0.2\%$ | DUNE, Hyper-K | 2028–2040 |
| 13 | CKM FCNC rates | at Standard Model level | at SM level | any rate $> 10\times$ SM | LHCb, Belle II | ongoing |
| 14 | Top quark decay width (NNLO) | $\sim 2.0$ GeV (gap must close) | $2.00 \pm 0.1$ GeV | NNLO calc yields $<1.85$ or $>2.15$ | internal calculation | ~2 years |

Fourteen rows. Five are already in the data and currently *satisfied* (rows 1–5: the boson-mass and $\rho$-parameter agreements); the framework's prediction for each is that the agreement will survive further precision. Two are structural (rows 6 and 12: the generation count and PMNS unitarity) — they cannot be confirmed beyond the current precision, only falsified. Five are BSM tests the framework asks the experimental community to run (rows 7–11: the Higgs branching fractions, dark-matter searches, and the dark-energy equation of state). One is an SM-consistency test the framework shares with the Standard Model (row 13: FCNC rates). One is an internal calculation (row 14: the top decay-width NNLO).

If the Skeptic asks which of the fourteen is the sharpest knife: it is row 6. The discovery of a fourth-generation fermion, at any mass, at any collider, kills the framework in one datum. No other row gives the framework this kind of immediate vulnerability.

If the Skeptic asks which is the most important test of the framework's *existing* claims: rows 1–5. Five simultaneous precision agreements in the boson sector, with zero free parameters, are the single strongest numerical result Volume 4 contains. If any of the five slips by more than 2%, the framework's electroweak sector is wrong.

If the Skeptic asks which is the framework's most uncomfortable obligation: row 14. The top-decay-width gap is the largest current discrepancy between prediction and observation, and the framework's explanation — "NNLO corrections will close it" — is not yet a calculation.

The table is the chapter's deliverable. Volume 6 will turn each row into a proper experimental treatment.

---

## §14.6  The Research Roadmap

The falsification table in §14.5 is the framework's experimental debt. This section is the framework's *theoretical* debt: every derivation that Chapters 1 through 13 of this volume left incomplete, with a priority label and an effort estimate. Twelve items. Two blockers, four high, three medium, three low.

The convention used for each item is: item number (RR-$n$), title, GitHub issue number (where one exists), status summary, and effort estimate.

### CRITICAL (blockers)

The framework does not advance past its current form as an effective electroweak-scale theory until these are closed.

**RR-1. Spin-$1/2$ fermion derivation from the bosonic membrane** (GitHub issue #1).

*Status:* The Firmament membrane $\Psi_A$ is a complex scalar field. Fermions have spin $1/2$. Chapter 10 §10.2 assumed a Jackiw-Rossi–like mechanism in which fermionic excitations emerge from vortex cores through a coupling to an auxiliary spinor field, and noted that the auxiliary field is an input to the derivation rather than an output. This is the only place in the volume where the framework explicitly adds a degree of freedom it cannot derive, and it is also the most load-bearing assumption in the entire particle spectrum of Ch 10–13. Without a first-principles derivation of the spin-$1/2$ fermions, the framework cannot claim to derive the particle content of the Standard Model; it can only claim to *organize* it.

*Resolution paths:* Two have been proposed. (a) A topological mechanism on the 6D manifold in which the fermionic degrees of freedom emerge as boundary modes on a defect of codimension 2 — a construction analogous to the edge states of topological insulators in condensed matter, extended to 6D. (b) A recognition that the auxiliary spinor is not auxiliary but is the boundary degree of freedom of a higher-dimensional manifold (8D or 10D) that the framework has not yet committed to.

*Effort estimate:* 6–12 months of focused work. Both resolution paths are conjectural; neither has been shown to produce the right spectrum.

*Impact if closed:* The framework becomes a genuine derivation of the Standard Model fermion content, not merely an organization of it. All four of the Chapter 10 §10.3 results upgrade from "ASSUMED" to "DERIVED."

**RR-2. The thousand-fold fermion mass-scale problem** (GitHub issue #2).

*Status:* Chapter 10 §10.7 reported the fermion-mass predictions with honest error bars. At the heavy end — top, bottom, tau — the framework hits the PDG values to within 15% or better. At the light end — electron, up quark, down quark — the framework's predictions are off by factors up to *a thousand*. The problem is not that the framework cannot hit the light fermion masses; it is that the Ch 10 Yukawa overlap integral depends on the Higgs profile $H(\xi)$ in a way that the framework currently fits rather than derives. The electroweak vacuum expectation value $v_B = 246$ GeV is an input to Ch 10, not an output, and the light-fermion masses come out wrong by a factor of a thousand unless $H(\xi)$ is shaped to match them.

In other words: Genesis Physics is currently a good *effective theory* at the electroweak scale, not a *fundamental* theory. It gets mass ratios right. It gets mass hierarchies right. It does not get absolute light-fermion masses right without fitting.

*Resolution paths* (from `06-REMAINING_DERIVATIONS.md` §9.1, reproduced here with effort estimates):

- **Path A — Vortex core fine structure.** Solve the 6D equations of motion in the vortex core at scales approaching $10^{-35}$ m. Look for bound states or resonances that set the absolute energy scale from first principles. Effort: 3–6 months. Risk: the 6D equations at this scale are nonlinear and numerically expensive, and there is no guarantee that a bound state with the right absolute mass exists.

- **Path B — Multi-layer or fractional winding modes.** Extend the topological classification of vortices beyond $\pi_1(U(1)_A) = \mathbb{Z}$ to higher homotopy groups or fractional windings. Effort: 4–8 months. Risk: extending the topological classification may produce new bound states that the framework's existing spectrum cannot accommodate, triggering a cascade of revisions to Ch 10.

- **Path C — Membrane–water coupling running.** Perform a full RG analysis of the Firmament-bulk coupling as a function of energy scale, from the KK scale down to the electroweak scale. Effort: 2–4 months. This is the shortest and most tractable path. Risk: the RG flow may not be well-defined in the 6D framework without closing RR-6 (NNLO) first.

- **Path D — Planck-scale decoupling and moduli stabilization.** Derive $v_B = 246$ GeV from a stability condition on the ξ-modulus potential, thereby making the electroweak scale an output rather than an input. Effort: 6–12 months. Risk: moduli stabilization is its own research program and has defeated many other frameworks; the Genesis architecture may or may not offer a new route.

*Recommended order:* Path C first, because it is shortest and can be carried out with tools the framework already has. Then Path A. Then B and D in parallel.

*Effort estimate (total):* The shortest resolution path is 2–4 months; the longest is 12 months; a combined attack could be on the order of 8–12 months.

*Impact if closed:* The framework becomes a fundamental theory of the electroweak scale. Every numerical prediction in Ch 10 upgrades from "APPROXIMATE" to "DERIVED," the light-fermion mass ratios stop being input-dependent, and the Skeptic's loudest objection disappears.

### HIGH

These are derivations the framework has partially completed. Each has a concrete path to closure.

**RR-3. Higgs potential O(1) coefficients** (GitHub issue #25).

*Status:* The Higgs potential written in Ch 11 §11.4 as $V(H) = -\mu^2 |H|^2 + (\lambda/4)|H|^4$ contains two dimensionless parameters, $\mu^2/v_B^2$ and $\lambda$, that are currently fit to precision electroweak data rather than derived. Both should, in principle, come from the boundary conditions on the $\Psi_A$ and $\Psi_B$ fields at the Firmament; the derivation has been sketched but not closed. Effort estimate: 3–6 months.

*Impact if closed:* Ch 11 §11.4 becomes a full derivation of the Higgs mass (not just the ratio $m_H/v_B$), and the boson-mass precision envelope of Prediction 14.1 gains predictive power at the sub-percent level.

**RR-4. CKM CP phase $\delta_{\rm CP}^q$** (GitHub issue #3).

*Status:* Ch 13 §13.3 reported the Jarlskog invariant at order of magnitude only: $J_{\rm CP}^{\rm quark, framework} \sim$ few × $10^{-5}$. The PDG value is $(3.18 \pm 0.15) \times 10^{-5}$. The framework's current prediction has an uncertainty of about one decade, because the CP phase depends on the complex phases of the ξ-ladder overlap integrals, which Ch 10 §10.4 did not compute — it only reported the magnitudes of the overlaps, not their phases.

*Resolution:* Extend Ch 10 §10.4 to compute the overlap-integral *phases*, which requires a careful treatment of the topological structure of the ξ-ladder bound-state wavefunctions. Effort estimate: 3–4 months.

*Impact if closed:* Ch 13 §13.3 upgrades its Jarlskog invariant from APPROXIMATE (order-of-magnitude) to APPROXIMATE (within a factor of 2). This also tightens the baryogenesis discussion of RR-12.

**RR-5. Grand unification.**

*Status:* The framework has three gauge groups — $SU(3)_C$ from the η-orbifold (Ch 12), $SU(2)_L$ from the Waters Below isometry (Ch 11), $U(1)_Y$ from the Firmament hypercharge (Ch 11) — but it does not yet tell us whether they unify at high energy, and if so, into what. Vol 2 Ch 10's running coupling analysis put the three couplings within a few percent of a common value at approximately $10^{16}$ GeV, which is suggestive of a GUT but does not prove one. The framework has not yet committed to a specific GUT structure: $SU(5)$, $SO(10)$, and an $SU(4) \times SU(2) \times SU(2)$ Pati-Salam variant are all in principle compatible with the zone architecture, and a zone-specific group (not on the conventional GUT list) is also possible.

*Resolution:* Compute the geometric unification condition from the 6D curvature integral, which should pick out one GUT structure from the candidates. Effort estimate: 4–6 months.

*Impact if closed:* The framework predicts the proton decay rate from the GUT structure, which becomes a sharp test against Hyper-K and future proton-decay experiments. This also closes the question of whether $v_A \approx 10^{16}$ GeV is *literally* the GUT scale or merely adjacent to it.

**RR-6. NLO/NNLO corrections in zone QFT.**

*Status:* The framework's predictions are mostly tree-level. Ch 8 developed renormalization at one loop. Higher orders have not been done. The top-decay-width gap of Prediction 14.5 is the sharpest sign that higher-order corrections matter; the boson-mass envelope of Prediction 14.1 will also tighten once NNLO corrections are computed. Effort estimate: 3–4 months.

*Impact if closed:* Prediction 14.5 is resolved (either the gap closes and the framework is vindicated, or it does not and the framework's top-sector vertex is wrong). Prediction 14.1 gains sub-percent precision. The RG analysis needed for RR-2 Path C becomes possible.

### MEDIUM

These are smaller items with shorter timescales. Each affects a specific sector rather than the foundations of the framework.

**RR-7. Running couplings with full precision** (GitHub issue #26). Vol 2 Ch 10's RG analysis is leading-order. Two-loop β-functions need completion. Effort: 2–3 months.

**RR-8. Neutrino mass generation.** Ch 13 §13.4 built the PMNS matrix from η-boundary ripples but did not derive the absolute neutrino masses. Seesaw mechanism needs grounding in Waters Below structure. Effort: 2–3 months. This is also the calculation that fixes the Class B sterile neutrino mass range of §14.2.

**RR-9. Moduli stabilization.** Why $v_B = 246$ GeV and not another value? Path D of RR-2 addresses this. Effort: 6–12 months (same as RR-2 Path D).

### LOW

These are items the framework should eventually address but whose resolution is not on the critical path.

**RR-10. Dark sector particle content.** §14.2 listed four candidate classes; their full Lagrangian structure has not been derived. Effort: 6–12 months when Vol 5 opens.

**RR-11. Axion-like particles.** Goldstone bosons from approximate symmetries of 6D compactification have not been classified. The framework may or may not predict axions; it has not yet looked carefully. Effort: 2–3 months.

**RR-12. Matter–antimatter asymmetry precision.** The three Sakharov conditions are satisfied structurally in the framework (Ch 13 §13.5 and §14.2 above, through CP violation and the out-of-equilibrium dynamics of the electroweak phase transition). The *quantitative* baryogenesis calculation — does the framework produce the observed $n_B/n_\gamma \approx 6 \times 10^{-10}$? — is not closed, and depends on closing RR-4 first. Effort: 4–6 months after RR-4.

### The consolidated picture

Twelve items. Two blockers (RR-1 and RR-2). Four high-priority (RR-3 through RR-6). Three medium (RR-7 through RR-9). Three low (RR-10 through RR-12). The blockers together carry an effort estimate on the order of 12–18 months of focused work. The high-priority items carry perhaps another 12 months. The medium and low items run in parallel and take another 6–9 months each.

The framework has, on its current trajectory, approximately two to three years of focused theoretical work ahead of it before the falsification table of §14.5 and the research roadmap of this section are both in a state the Skeptic would sign off on. That is not small. It is also not infinite. A framework that can name its debts in twelve items, with priorities and effort estimates, is a framework that is serious about closing them.

[Fig 4.14.5: The research roadmap pyramid. A five-tier pyramid. Bottom tier (CRITICAL): two blocks, labeled RR-1 and RR-2, with GitHub issues #1 and #2. Second tier (HIGH): four blocks, RR-3 through RR-6, with GitHub issues #25, #3, (new), (new). Third tier (MEDIUM): three blocks, RR-7 through RR-9, with issue #26 on RR-7. Top tier (LOW): three blocks, RR-10 through RR-12. A vertical arrow on the right labeled "approximately 24–36 months of focused work" spans the full height. Below the pyramid, a thin box labeled "inherited by Vol 5 and Vol 6."]

---

## §14.7  Handoff to Vol 5 and Vol 6

Volume 5 inherits the cosmological sector of this chapter. The four dark-matter candidate classes of §14.2 become the dark-matter *cosmology* of Volume 5: their abundance calculations, their freeze-out histories, their structure-formation signatures, and their constraints from the CMB acoustic peaks. The Waters Above vacuum of §14.3 becomes the cosmological-constant chapter of Volume 5 — in particular, the proposed Z$_2$ cancellation mechanism named briefly in §14.3 is taken up properly in Vol 5 Ch 12. The hierarchy recap of §14.1 becomes the moduli-stabilization problem of Volume 5, intertwined with RR-9 and RR-2 Path D.

Volume 6 inherits the experimental test suite. The entire falsification table of §14.5 becomes Volume 6's primary deliverable: each of its fourteen rows expands into a chapter or section in which the predicted observable, its experimental status, its current error bar, and the framework's prediction are compared in detail with the data as it stands at the time of Vol 6's writing. The research roadmap of §14.6 becomes Volume 6's internal work plan — the open problems that must be closed before Vol 6 can claim to be a book rather than a progress report.

Volume 4 has done what it can at the scale of the particle. It has derived the Standard Model, it has named the debts the derivation left unpaid, and it has given the Skeptic fourteen ways to kill the framework. Volume 5 will now ask whether the same architecture that produced particles also produces cosmologies — whether the zone manifold, having organized the quantum, can also organize the universe.

---

## Problem Set

**14.1 (Conceptual).** The framework's prediction of exactly three fermion generations (Result 14.3) is labeled RIGOROUS. What is the structural input on which this rigor depends? If the Vol 1 Ch 5 double-well potential were replaced with a triple-well potential, how many generations would the framework predict? What aspect of the zone geometry *prevents* this replacement from being made arbitrarily?

**14.2 (Order of magnitude).** Estimate the Compton wavelength of a dark-matter candidate of mass 0.95 GeV (Class A of §14.2). Compare this to the typical inter-atomic spacing in a direct-detection target such as xenon. Comment on whether coherent nuclear scattering is a useful signature in this mass range.

**14.3 (Calculation).** Using the Wolfenstein parameters of Ch 13 equation (4.13.13), compute the Jarlskog invariant $J_{\rm CP}^{\rm quark}$ with the framework's current error bars. Compare this to the baryogenesis requirement at the electroweak phase transition, which is roughly $J_{\rm CP} \geq 10^{-8}$. Does the framework's quark CP violation suffice to account for the observed matter–antimatter asymmetry? If not, what additional CP source must the framework invoke?

**14.4 (Conceptual).** Prediction 14.1 (the boson-mass precision envelope) would be trivially satisfied if the framework had only to match one mass — any framework with a single free parameter can be adjusted to match any single observable. Explain precisely why the *simultaneous* matching of $m_t$, $m_H$, $M_W$, $M_Z$, and the $\rho$ parameter to 0.5% or better is a non-trivial constraint on the framework, and not simply an accident of numerical precision.

**14.5 (Calculation).** For dark-matter Class A (the KK mode at 1.9 GeV), estimate the nucleon-recoil cross-section from the framework's coupling structure — that is, one loop factor below the Z-boson coupling. Compare the result to the projected sensitivity of SuperCDMS and the next-generation directional detectors at this mass window. At what integrated exposure would SuperCDMS be expected to either detect the mode or rule it out?

**14.6 (Conceptual).** Prediction 14.5 (the top-quark decay-width gap) is an *internal* test — it asks the framework to perform a calculation (NNLO zone-QFT corrections to $\Gamma_t$) rather than an experiment to perform a measurement. If that calculation is carried out and does *not* close the 25% gap, what does the framework owe next? Which open problem in §14.6 is upgraded from HIGH to BLOCKER? What chapter of Vol 4 is implicated as wrong?

**14.7 (Order of magnitude).** From $v_A \sim 10^{16}$ GeV and the loop-level vacuum-energy estimate (4.14.10), reproduce the 184-order-of-magnitude cosmological-constant mismatch. Then estimate the *minimum* suppression the proposed Z$_2$ cancellation mechanism of §14.3 must supply in order to reach the observed $\Lambda_{\rm obs} \sim 10^{-122}$ GeV$^4$. How many orders of magnitude must the cancellation be exact to? Comment on whether such precision is plausible from a Z$_2$ symmetry broken only by boundary conditions.

**14.8 (Conceptual).** In the Standard Model, CP violation in the quark sector is an empirical input — the CKM phase is measured, not derived. In Genesis Physics (Ch 13 §13.3), CP violation is a theorem, labeled RIGOROUS, that follows from the three-generation count and the Kobayashi-Maskawa phase-counting rule. What is the theorem's precondition that the Standard Model cannot supply, but that the Genesis framework can? Why is the distinction between *assuming* CP violation and *proving* it significant for the framework's claim of foundational status?

**14.9 (Challenge).** Construct a Class E dark-matter candidate that the framework's current four classes (A–D of §14.2) do not contain. Identify which sector of the 6D manifold this Class E candidate would have to live in. Comment on whether the sector you identify is compatible with the Ch 10–13 derivations, or whether it requires extending the framework. If it requires extension, state the extension precisely and identify which of Ch 10–13 would need to be revised.

**14.10 (Open).** Pick one item from the §14.6 research roadmap — any priority level — and sketch a research program to close it. The sketch should contain: (a) a statement of the problem, (b) a proposed technical approach, (c) the inputs the approach requires (which chapters of this volume or previous volumes), (d) an estimate of the effort, (e) an assessment of the risk of failure, (f) a statement of what the framework gains if the problem is closed. Minimum three paragraphs.

---

*End of Chapter 14 — DRAFT.*
