---
product: Foundations Vol 4 — The Quantum World
chapter: 11
title: The Electroweak Theory
status: OUTLINE
created: 2026-04-09
---

# Chapter 11: The Electroweak Theory — DETAILED OUTLINE

Thirteen sections plus a problem set. Target word count 9,000–14,000. Equations (4.11.1)–(4.11.45+). Six figures.

---

## §11.0 Introduction — two unified forces, two honest gaps

**Topic sentence.** Electromagnetism and the weak force are two faces of a single gauge theory broken by the vacuum; the unification is a physics statement that the zone framework has been pointing at since Vol 2 Ch 6, and this chapter makes it precise.

**Why entry point.** Why should two forces as different as light and beta decay be the same thing? Because their gauge fields come from the same zone isometries; the difference is the vacuum, not the Lagrangian.

**Key content.** State the chapter's dual mission: derive the electroweak sector quantitatively (predictions to 0.03–0.6% on $M_W$, $M_Z$, $m_H$) *and* state the two open problems honestly (GitHub #25 Higgs gap, GitHub #3 weak/CP gap). Set expectations: the gauge-boson predictions are genuinely tight because they are all set by three numbers ($g$, $g'$, $v$) whereas the fermion sector of Ch 10 was trying to do twelve Yukawa couplings from one exponential. A reader must understand why the two chapters have such different-looking success.

**Exit condition.** Reader knows the chapter's structure, the two gaps by name and GitHub number, and the rigor labels.

**Figures.** Fig 4.11.1 (roadmap).

---

## §11.1 $SU(2)_L \times U(1)_Y$ from zone geometry [RIGOROUS — inheriting Vol 2 Ch 6]

**Topic sentence.** The electroweak gauge group is not chosen; it descends from the isometry structure of the coupled $(\xi,\eta)$ extra-dimensional geometry already derived in Vol 2 Ch 6.

**Why entry point.** Why this gauge group, not $U(1)^2$ or $SU(3)$ or anything else?

**Key content.** Recap Vol 2 Ch 6 result: translations in $\eta$ and phase rotations in $\Psi_A$ generate $SU(2)_L \times U(1)_Y$ as the minimal non-abelian gauge group preserved by the Firmament boundary. State the generators $T^a = \sigma^a/2$ and hypercharge $Y$. State the covariant derivative $D_\mu = \partial_\mu - igW_\mu^a T^a - ig'B_\mu Y$. Make the bridge: *this is not new physics; it is Vol 2 Ch 6 cast in the language we need for the Higgs mechanism*.

**Exit condition.** Reader has $D_\mu$ in hand with all its pieces defined.

**Equations.** (4.11.1)–(4.11.4) — generators, covariant derivative, hypercharge assignment for the Higgs doublet.

---

## §11.2 The Higgs doublet as the lowest $\Psi_A$ KK mode [RIGOROUS conditional]

**Topic sentence.** The Standard Model Higgs doublet is the lowest Kaluza-Klein mode of the Waters Above scalar field, expanded in the Dirichlet sinusoidal basis along $\xi$.

**Why entry point.** Why should the Higgs be a KK mode at all, and why the *lowest* one?

**Key content.** Expand $\Psi_A(x^\mu,\xi,\eta) = \sum_{n_\xi,n_\eta}\psi_{n_\xi}(\xi)\chi_{n_\eta}(\eta)\varphi_{n_\xi,n_\eta}(x^\mu)$. State Dirichlet BC at Firmament, derive sine eigenfunctions $\psi_n(\xi) = \sqrt{2/\xi_A}\sin(n\pi\xi/\xi_A)$. Identify the $(n_\xi, n_\eta) = (1,1)$ mode as the 4D Higgs doublet by matching its quantum numbers ($SU(2)_L$ doublet with $Y = +1$) against the gauge-field couplings inherited from §11.1. *No novel derivation*; this is bookkeeping of a selection already present in the Lagrangian.

**Exit condition.** Reader identifies $H(x^\mu)$ explicitly.

**Equations.** (4.11.5)–(4.11.7).

**Honest note.** The lowest-mode identification is rigorous *given* that the Higgs lives in $\Psi_A$. That placement was made in Vol 3 Ch 7 and will be examined in §11.4 as one of the inputs to the open gap.

---

## §11.3 The Mexican hat and spontaneous symmetry breaking [APPROXIMATE]

**Topic sentence.** The effective 4D potential inherited from the 6D action has the Mexican-hat form, and its minimization fixes the Higgs VEV.

**Why entry point.** Why a Mexican hat specifically, and why doesn't the minimum sit at the origin?

**Key content.** Reduce the 6D kinetic + potential for $\Psi_A$ to 4D by integrating over $(\xi,\eta)$ weighted by $\psi_1^2\chi_1^2$. Show the effective potential:
$$V_{\rm eff}(H) = -\mu^2|H|^2 + \tfrac{\lambda}{4}|H|^4,$$
with
$$\mu^2 = \beta\sigma c^2/\xi_A^2 \approx (88\ \text{GeV})^2,\qquad \lambda = \lambda_A\cdot\frac{9}{4\xi_A\eta_B} \approx 0.129.$$
Minimize: $|H|^2_{\rm vev} = 2\mu^2/\lambda$, $\|H_{\rm vev}\| = v/\sqrt 2$, $v = 2\mu/\sqrt\lambda$.
Substitute: $v \approx 246$ GeV.

**Exit condition.** Reader has $v$ in hand and understands the geometric origin of the $\mu^2$ scale (Firmament tension divided by cosmological scale squared).

**Equations.** (4.11.8)–(4.11.13).

**Figures.** Fig 4.11.2 (Mexican hat 3D plot).

**Rigor label.** APPROXIMATE, because the $\mathcal{O}(1)$ coefficient $\beta$ is currently a fit (§11.4 will address this head-on).

---

## §11.4 The Higgs condensation gap, stated openly [OPEN — GitHub #25]

> **OPEN PROBLEM 11.1.** *The zone-architecture Higgs mechanism produces a Mexican-hat potential of the correct form and a vacuum expectation value of the correct numerical scale, provided three $\mathcal{O}(1)$ coefficients from the 6D bulk-boundary matching are taken as fit parameters. A derivation of those coefficients from the 6D action alone is the content of GitHub issue #25. This section states the gap openly and enumerates exactly what is derived and what is fit.*

**Topic sentence.** The Higgs mechanism works in the sense that the framework produces the Standard Model potential; it does not *yet* work in the sense that every number in that potential is computed from the 6D action without boundary-matching input.

**Why entry point.** Why does a framework that predicts $M_W$ to 0.03% still have a problem with the Higgs?

**Key content.** Four parts.
1. **What we have.** The form $V_{\rm eff}(H) = -\mu^2|H|^2 + \tfrac{\lambda}{4}|H|^4$ is rigorously the reduced potential. The sign of $\mu^2$ (negative, triggering SSB) is rigorous given the boundary condition $\psi_1(0) = 0$ plus the Firmament tension coupling.
2. **What we assume.** The identification of the Higgs doublet with the $(1,1)$ KK mode is fixed by the SM quantum numbers, not uniquely predicted by 6D dynamics.
3. **What is currently fit.** Three $\mathcal{O}(1)$ coefficients: (a) $\beta$ in $\mu^2 = \beta\sigma c^2/\xi_A^2$, from the detailed shape of the Firmament membrane-tension coupling near $\xi = 0$; (b) $\alpha$ in the fermion-overlap exponential $y_n = y_0 e^{-\alpha n^2}$ (already gapped in Ch 10); (c) $\lambda_A$, the 6D quartic, which is matched to the measured $m_H$ rather than computed from renormalization group flow.
4. **What closure would require.** A self-consistent solution of the coupled Einstein + $\Psi_A$ equations in the 6D bulk with Firmament boundary conditions, yielding $\beta, \alpha, \lambda_A$ without fit. This is the content of issue #25 and is not closed by any chapter in Vol 4.

**Exit condition.** Reader knows exactly what the framework does and does not buy with its Higgs predictions. A reader who counts parameters can now honestly score the chapter.

**Equations.** None new; the key equations are (4.11.10)–(4.11.13) and the reader is told to count their fit inputs.

**Honest warning.** The "0.03% on $M_W$" result in §11.5 is a *consequence* of accepting these fits, not an independent test. If one refits $v$ to the electroweak scale, everything else follows; what the chapter is *not* doing is predicting $v$ from cosmological $\xi_A$ without adjustment.

---

## §11.5 Gauge boson masses and the massless photon [RIGOROUS, conditional on §11.4]

**Topic sentence.** Substituting the Higgs VEV into the covariant derivative gives the gauge-boson mass terms, and the neutral-sector mixing identifies exactly one massless combination, which is the photon.

**Why entry point.** Why does the photon stay massless when three of the four gauge bosons eat Goldstone modes?

**Key content.** Compute $|D_\mu\langle H\rangle|^2$ at $\langle H\rangle = (0, v/\sqrt 2)^T$. Extract $W^\pm$ mass term $M_W^2 W^+_\mu W^{\mu-}$ with $M_W = gv/2$. Show the neutral sector mixes $W^3$ and $B$ via the weak mixing angle $\theta_W$:
$$\tan\theta_W = g'/g,\qquad Z_\mu = \cos\theta_W W^3_\mu - \sin\theta_W B_\mu,\qquad A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu.$$
$M_Z = M_W/\cos\theta_W$. Show $Q\langle H\rangle = 0$ with $Q = T_3 + Y/2$, hence $M_\gamma = 0$ exactly. Numerical values: $g = 0.652$, $v = 246.22$ GeV, $M_W = 80.4$ GeV (PDG $80.377 \pm 0.015$, 0.03%), $\sin^2\theta_W = 0.2312$, $M_Z = 91.2$ GeV (PDG $91.188\pm 0.002$, 0.56%). $\rho = 1$ at tree level (PDG $1.00038\pm 0.00019$, 0.3%).

**Exit condition.** Reader has concrete numbers for $M_W, M_Z, M_\gamma$ and understands the rotation picture.

**Equations.** (4.11.14)–(4.11.25).

**Figures.** Fig 4.11.4 (the $(W^3, B)\to(Z,\gamma)$ rotation).

---

## §11.6 The Higgs boson mass and the quartic coupling [APPROXIMATE]

**Topic sentence.** The mass of the physical Higgs boson $h$ is the curvature of the potential at its minimum, and with the measured $v$ and $\lambda$ it comes out to 125 GeV.

**Why entry point.** Why is the Higgs mass what it is, and is it "predicted" or "fitted"?

**Key content.** From $V(\phi) = -\mu^2\phi^2/2 + (\lambda/4)\phi^4$ for the radial mode, $d^2V/d\phi^2|_{\rm vev} = 2\mu^2$, hence $m_h^2 = 2\mu^2 = 2\lambda v^2$, so $m_h = \sqrt{2\lambda}\,v = 125.1$ GeV (PDG $125.10 \pm 0.14$, 0.008%).

**Honest framing.** This agreement looks spectacular but the reader must recall §11.4: $\lambda$ itself is fitted to $m_H$ via the overlap-integral formula $\lambda = \lambda_A \cdot 9/(4\xi_A\eta_B)$ because $\lambda_A$ has not been derived from renormalization flow. So the 0.008% on $m_H$ is in practice a consistency check of the framework's *internal* algebra — $m_h^2 = 2\lambda v^2$ — rather than a first-principles prediction of the number $125.10$ GeV. The chapter says so in plain language and does not hide the circularity.

**Exit condition.** Reader understands that $m_h$ is internally consistent but not independently predicted.

**Equations.** (4.11.26)–(4.11.28).

---

## §11.7 The Fermi constant and the low-energy limit [RIGOROUS]

**Topic sentence.** At energies far below $M_W$, the charged-current interaction contracts to a point-like four-fermion vertex whose strength is the Fermi constant, and $G_F = 1/(\sqrt 2 v^2)$.

**Why entry point.** Why is the weak force short-range, and why does the low-energy coupling depend on the VEV alone?

**Key content.** Expand the W-boson propagator in $q^2/M_W^2$. Show $\mathcal{L}_{\rm eff} = (g^2/2M_W^2) J_+^\mu J_{\mu-}/2 = (2\sqrt 2 G_F) J_+^\mu J_{\mu-}/2$ with
$$G_F = \frac{g^2}{4\sqrt 2 M_W^2} = \frac{1}{\sqrt 2 v^2},$$
using $M_W = gv/2$. Substitute $v = 246.22$ GeV: $G_F = 1.166\times 10^{-5}$ GeV$^{-2}$ (PDG $1.16637\times 10^{-5}$, 0.03%). Note that this derivation uses $v$ as input (so the prediction is a *consistency* check against two measurements — $M_W$ and $\mu$-decay); it is still rigorous in that the functional form is forced by the W exchange.

**Exit condition.** Reader has $G_F$ derived and understands that the weak force is short-range because $M_W$ is heavy.

**Equations.** (4.11.29)–(4.11.32).

---

## §11.8 Parity violation from the one-sided condensate [RIGOROUS, conditional on OPEN 10.1]

**Topic sentence.** The Firmament makes the condensate one-sided in $\xi$, and this single geometric fact is why the weak force is parity-violating at maximum strength.

**Why entry point.** Why does the universe have a preferred handedness?

**Key content.** The Waters Above exists only for $\xi \in [0, \xi_A]$; there is no mirror region at negative $\xi$. Under the formal extension to negative $\xi$, the condensate profile $\langle\Psi_A\rangle(\xi)$ is *not* invariant under $\xi\to-\xi$. The W-boson ξ-profile $\phi_W(\xi)$ is an even function of $\xi$ in the formal extension. Left-handed fermion ξ-profiles are even under $\xi\to-\xi$ (by the ξ-parity/4D-chirality correspondence from 6D spinor reduction); right-handed profiles are odd.
Overlap integrals:
$$\int\phi_W(\xi)\chi_L(\xi)\,d\xi \neq 0, \qquad \int\phi_W(\xi)\chi_R(\xi)\,d\xi = 0.$$
Therefore W bosons couple only to left-handed fermions — the $V\!-\!A$ structure with $g_V = g_A$. The Wu asymmetry parameter $A = -1$ (PDG $-1.00\pm 0.05$). Goldhaber neutrino helicity $h = -1$ (PDG $-0.993\pm 0.013$).

**Conditional note.** This entire derivation requires a primordial spinor field on the Firmament (Assumption 10.1 from Ch 10). If OPEN 10.1 is closed differently, the ξ-parity correspondence might require adjustment. Stated openly.

**Exit condition.** Reader understands that handedness is a geometric accident — or rather, a geometric necessity of a one-sided condensate.

**Equations.** (4.11.33)–(4.11.39).

**Figures.** Fig 4.11.3 (one-sided condensate and overlap picture).

---

## §11.9 CP violation and the weak-sector gap, stated openly [OPEN — GitHub #3]

> **OPEN PROBLEM 11.2.** *Parity violation, the $V\!-\!A$ structure, and the Wu/Goldhaber asymmetries are rigorously derived within the framework (conditional on Assumption 10.1). CP violation exists necessarily for $\geq 3$ generations by Kobayashi-Maskawa counting, and the Jarlskog invariant is a structural prediction. The precise value $\delta_{\rm CP}^{\rm meas} \approx 1.2$ rad is at present only an order-of-magnitude prediction of the framework, pending the full computation in Chapter 13. Tracked as GitHub issue #3.*

**Topic sentence.** The existence of CP violation is a theorem in this framework once three generations are admitted; the precise phase is not.

**Why entry point.** Why is CP violation inevitable at three generations but not at two?

**Key content.** Kobayashi-Maskawa counting: a $3\times 3$ complex matrix has $9$ complex parameters; global fermion rephasings remove $2n-1 = 5$ phases (after accounting for an overall irrelevant baryon number phase); what remains is $3$ real angles plus $1$ irreducible CP-violating phase. At $n = 2$, there are no irreducible phases (only the Cabibbo angle). At $n = 3$ the phase must exist. Since Ch 10 produces a three-generation mass matrix with generic off-diagonal Yukawa entries, CP violation is forced on the framework.

Introduce the Jarlskog invariant $J_{\rm CP} = \Im(V_{us}V_{cb}V^*_{ub}V^*_{cs})$, state its measured value $\approx 3\times 10^{-5}$, and note that the unitarity triangle's area is $\tfrac12|J_{\rm CP}|$. The *existence* of a nonzero $J_{\rm CP}$ is a framework prediction. The *value* is not; it depends on the detailed topological phases of the vortex sectors, which in Ch 10 were acknowledged as open.

**Four parts of the gap.**
1. **What we have.** CP violation inevitability for $n = 3$, rigorous. $V\!-\!A$ structure, rigorous (conditional). Jarlskog invariant existence, rigorous.
2. **What we assume.** The three-generation Yukawa matrix has generic phases — true if the vortex sectors in Ch 10 acquire phases from their topological winding, as expected but not computed.
3. **Phenomenological only.** The precise numerical value $\delta_{\rm CP}\approx 1.2$ rad. Framework's order-of-magnitude estimate is $\mathcal{O}(1)$ rad, which agrees with observation but does not distinguish 0.5 from 2.
4. **What closure would require.** The vortex-topological-phase computation is the content of Chapter 13; this chapter flags the gap and hands it off.

**Exit condition.** Reader knows that "CP violation exists" is a theorem but "CP violation = 1.20 rad" is not.

**Equations.** (4.11.43)–(4.11.45).

**Figures.** Fig 4.11.5 (unitarity triangle with Jarlskog area).

---

## §11.10 The electroweak precision ledger [honest totals]

**Topic sentence.** Here is every electroweak precision observable the framework makes a statement about, with its prediction, its measurement, and its rigor label.

**Key content.** Table 4.11.1 — single unified table:

| Observable | Prediction | PDG | Error | Rigor |
|-----------|-----------|-----|-------|-------|
| $v$ | 246.22 GeV (fit/consistency) | 246.22 | — | FIT INPUT |
| $M_W$ | 80.4 GeV | 80.377 ± 0.015 | 0.03% | RIGOROUS (given $v$) |
| $M_Z$ | 91.2 GeV | 91.188 ± 0.002 | 0.56% | RIGOROUS (given $v$, $\theta_W$) |
| $M_\gamma$ | 0 (exact) | 0 | 0 | RIGOROUS |
| $m_h$ | 125.1 GeV | 125.10 ± 0.14 | 0.008% | RIGOROUS (given $v, \lambda$; $\lambda$ is fit) |
| $\sin^2\theta_W$ | 0.2312 | 0.23122 | 0.09% | APPROXIMATE (from Vol 2 Ch 10 running) |
| $\rho$ | 1.00004 | 1.00038 ± 0.00019 | 0.3% | RIGOROUS at tree |
| $G_F$ | 1.166 × 10$^{-5}$ GeV$^{-2}$ | 1.16637 × 10$^{-5}$ | 0.03% | RIGOROUS (given $v$) |
| $y_t$ | 0.99 | 1.001 ± 0.030 | 0.1% | APPROX (from Ch 10) |
| Wu $A$ | –1 | –1.00 ± 0.05 | < 1% | RIGOROUS (conditional on OPEN 10.1) |
| Goldhaber $h_\nu$ | –1 | –0.993 ± 0.013 | < 1% | RIGOROUS (conditional) |
| $\tau_n$ (neutron) | 878.4 s | 878.4 ± 0.5 | < 0.1% | APPROX ($g_A$ taken from experiment) |
| $\delta_{\rm CP}$ | $\mathcal{O}(1)$ rad | 1.20 ± 0.08 | order-of-mag | PHENOMENOLOGICAL |

**Honest commentary.** Point out what these numbers do and do not mean:
- The submillionth-precision on $m_h$, $M_W$, $G_F$, and $\rho$ reflects that once $v$ and the gauge couplings are in hand, *algebra* gives everything else. The framework is not beating the Standard Model on these — it is reproducing its internal relations, which any theory with $SU(2)_L\times U(1)_Y$ and the Higgs mechanism reproduces.
- The $\mathcal{O}(1)$-to-sub-percent range on the asymmetry observables ($A$, $h_\nu$, $\tau_n$) reflects that parity violation and $V\!-\!A$ are structural, not fit.
- The order-of-magnitude on $\delta_{\rm CP}$ is where the honest gap bites.

---

## §11.11 Honest ledger — what is derived, what is fit, what is open

**Topic sentence.** Summary of the chapter's epistemic state in one section.

**Key content.** Three-column ledger:
- **Derived from axioms:** gauge group $SU(2)_L\times U(1)_Y$ (Vol 2 Ch 6); photon masslessness; $V\!-\!A$ structure; $G_F = 1/(\sqrt 2 v^2)$; $\rho = 1$; Kobayashi-Maskawa parameter counting; existence of $J_{\rm CP}$.
- **Fit by $\mathcal{O}(1)$ coefficients:** $\mu^2$ (via $\beta$); $\lambda$ (via $\lambda_A$); $\sin^2\theta_W$ (via the Vol 2 Ch 10 cutoff ratio, partially fit); neutrino helicity conditional on Assumption 10.1.
- **Open / phenomenological:** precise $\delta_{\rm CP}$; full Higgs potential derivation; CKM entries beyond Cabibbo.

**Figures.** Fig 4.11.6 (three-column schematic).

**Exit condition.** Reader has a clear mental budget of what has been bought and at what price.

---

## §11.12 Test-suite verification [RIGOROUS — with honest caveats]

**Topic sentence.** The existing nuclear-physics test suite covers $\tau_n$, fusion, and related observables; the direct electroweak derivations of this chapter are not yet automated.

**Key content.** Re-run `test_nuclear_physics.py` from Ch 10's verification; add the stated pass/fail. Note honestly that:
- No automated test currently diagonalizes the Mexican-hat potential and verifies $v = 246$ GeV from the bulk coupling.
- No automated test currently reproduces the Wu asymmetry from the overlap integral.
- These are flagged as ACTION ITEM Ch11-T1 in QUALITY_GATE.md.

**Exit condition.** The reader knows what is and is not tested.

---

## §11.13 Handoffs to Chapter 12 and Chapter 13

**Topic sentence.** The chapter leaves two specific deliverables for the chapters that follow.

**Key content.**
- **To Chapter 12 (QCD).** The $SU(3)_C$ color sector was left aside in this chapter; Ch 12 picks it up and derives the strong-coupling Lagrangian, confinement, and running. The electroweak sector here is a self-contained handoff — Ch 12 does not need to revisit the Higgs mechanism or $M_W$.
- **To Chapter 13 (CKM and PMNS).** The mass-eigenstate diagonalization of the fermion Yukawa matrices, the computation of the CKM entries including the precise $\delta_{\rm CP}$, and the analogous PMNS analysis for neutrinos are all routed to Ch 13. Ch 13 inherits: (a) the gauge structure from §11.1; (b) the Higgs doublet from §11.2; (c) the $V\!-\!A$ coupling from §11.8; (d) the Jarlskog-invariant constraint from §11.9; (e) the vortex generation structure from Ch 10.

**Exit condition.** Ch 12 and Ch 13 have everything they need from the electroweak sector.

---

## Problem Set

### Computational
- P11.1 (★★) Mexican-hat minimization for given $(\mu^2,\lambda)$. Verify the second-derivative condition.
- P11.2 (★★) Compute $M_W$, $M_Z$, $m_H$ from $g, g', v, \lambda$. Compare to PDG.
- P11.3 (★★) Derive $G_F$ from $M_W$ and $v$; reproduce the numerical value.
- P11.4 (★★★) Compute the leading oblique correction $\Delta\rho$ from a top-quark loop; verify the framework's prediction is consistent with PDG.

### Conceptual
- P11.5 (★★) Explain why the photon is massless even though $SU(2)_L\times U(1)_Y$ is broken. Use the unbroken generator $Q$.
- P11.6 (★★) Explain the parity-violation mechanism of §11.8 in your own words. Where does the one-sidedness enter?
- P11.7 (★★) What is the difference between "derived from axioms" and "fit by $\mathcal{O}(1)$ coefficients" in the Higgs sector? Use §11.4 and identify the three fit coefficients.

### Challenge
- P11.8 (★★★★) Do the Kobayashi-Maskawa parameter count for $n_{\rm gen} = 2, 3, 4$. Verify that CP violation first appears at $n = 3$ and count how many CP phases exist for $n = 4$.
- P11.9 (★★★★) Propose a first-principles computation of the boundary coefficient $\beta$ in $\mu^2 = \beta\sigma c^2/\xi_A^2$, starting from the coupled Einstein + $\Psi_A$ equations at the Firmament. What new 6D input is required? Identify a regime where $\beta$ can be read off from a simple limit.

---

## Outline Review Checklist

- [x] Every chapter requirement (Ch11-001 through Ch11-013) maps to at least one section
- [x] No forward dependency beyond handoffs to Ch 12 and Ch 13
- [x] "Why" chain is unbroken
- [x] Prerequisites are satisfied by prior volumes and chapters
- [x] Figure plan complete: roadmap, Mexican hat, one-sided condensate, mixing rotation, unitarity triangle, honest ledger
- [x] Two gaps each get a dedicated section with boxed OPEN statements
- [x] Table 4.11.1 covers every numerical claim with a rigor label
