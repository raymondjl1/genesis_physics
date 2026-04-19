---
product: Foundations Vol 4 — The Quantum World
chapter: 13
title: The CKM and PMNS Matrices
status: OUTLINE
created: 2026-04-09
role: Section-by-section outline and figure plan for the Ch 13 draft. Feeds directly into Ch13_DRAFT.md. Keeps the chapter short (20–30 pages, 8,000–11,000 words), focused, and honest about what the framework predicts structurally versus numerically.
---

# Chapter 13: The CKM and PMNS Matrices — CHAPTER OUTLINE

## Global Design Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Target word count | 8,000–11,000 | Focused chapter; no structurally new physics, only closure of Ch 10–12 threads and the Ch 11 §11.9 CP gap |
| Target page count | 20–30 | Matches word budget and Vol 4 WRITING_PROMPT entry for Ch 13 |
| Equation range | (4.13.1)–(4.13.43+) | Contiguous; 43 is a floor, not a ceiling |
| Number of sections | 10 (§13.0 – §13.9) + problem set | One orientation, eight content, one handoff |
| Figures | 7 (Fig 4.13.1 – Fig 4.13.7) | Each carries a specific structural contrast; no decorative figures |
| Rigor labels used | RIGOROUS / APPROXIMATE / PHENOMENOLOGICAL / OPEN | Every numerical claim carries one |
| Voice | Feynman writing a textbook, honest about gaps | Confident on structure; explicit about precision inheritance from Ch 10 |
| Epigraph candidate | Genesis 1:14 (sun, moon, stars as sortings into classes) or Genesis 1:4 (light / dark separation) | Distinctions into ordered classes resonates with three-generation sorting; do NOT force the parallel |

---

## Section-by-Section Outline

### §13.0 — Introduction: Two Matrices, Two Sectors, One Short Chapter

**Target length:** ~700 words (≈ 2 pages)

**Topic sentence.** This chapter finishes what Chapters 10, 11, and 12 began: the three-generation structure of matter, which up to now has been stated at the level of *mass eigenvalues*, acquires its second face — the *flavor* face — and the two faces turn out not to be aligned.

**"Why" entry point.** Why should the same particle have two different labels at all? Because it is born, moves, and decays through distinct interactions, and those interactions do not all commute with the Yukawa coupling that fixes its mass.

**Key content.**
- Open with the physical puzzle: a muon neutrino born at Fermilab arrives at DUNE as a mixture of electron, muon, and tau neutrinos. A B meson decays with a small but measurable CP asymmetry. Both facts are *mixing matrix* facts.
- State that Ch 13 has two jobs, nothing more: (i) write down $V_{\rm CKM}$ and $U_{\rm PMNS}$ from the Ch 10 vortex sector and the `06-NEUTRINO_PHYSICS.md` boundary-ripple sector; (ii) close the Ch 11 §11.9 CP-phase gap (GitHub issue #3) as far as it closes today, which is *structurally* but not yet *numerically*.
- Declare the chapter's honesty commitment up front: every numerical result here inherits the 15–99% error bars of Ch 10's fermion masses. The structural results — $3\times 3$ unitarity, $J_{\rm CP}\neq 0$ — do not.
- Name the two sectors and their opposite regimes: ξ-ladder hierarchy → CKM → *small* mixing; η-boundary near-degeneracy → PMNS → *large* mixing. Preview that the same equation produces both.
- Short roadmap (three sentences) of §§13.1–13.9.

**Exit condition.** The reader knows why the chapter exists, what it will and will not deliver, and what "closing the gap" will and will not mean by the end.

**Equations.** None (or at most one, schematically: $|{\rm flavor}\rangle = U|{\rm mass}\rangle$).

**Figures.** Fig 4.13.1 (chapter roadmap).

---

### §13.1 — Flavor vs. Mass Eigenstates: Why the Two Bases Are Not Aligned

**Target length:** ~1,100 words (≈ 3 pages)

**Topic sentence.** The flavor basis is where the weak current lives; the mass basis is where the propagator lives; and the two are related by a rotation whose angles are the physical content of the mixing matrix.

**"Why" entry point.** Why do we *need* a mixing matrix at all? Because the weak-current interaction vertex is a rigid rotation of the three generations, identical for all three, whereas the Yukawa-Higgs mass matrix has entries that differ from generation to generation.

**Key content.**
- Set up the two bases cleanly. Weak-current eigenstates $(u_L, c_L, t_L)$ and $(d_L, s_L, b_L)$ come from Ch 11's $SU(2)_L$ doublets. Mass eigenstates come from diagonalizing the Yukawa overlap matrix of Ch 10 §10.4.
- Show explicitly that these are the *same Hilbert space* in two different bases — so the change of basis is necessarily unitary by conservation of probability.
- Write the charged-current vertex in flavor basis and then transform to mass basis. The $3\times 3$ matrix that shows up in the result *is* $V_{\rm CKM}$. [Eqs (4.13.1)–(4.13.4)]
- Pause to distinguish: the rotation from flavor to mass for *up-type* quarks is $U_u$; the one for *down-type* is $U_d$; the *physical* mixing matrix is $V_{\rm CKM} = U_u^\dagger U_d$, and this is all that is observable. Absolute rotations $U_u, U_d$ individually are rephasing freedom.
- State the same construction for leptons. $U_{\rm PMNS} = U_\ell^\dagger U_\nu$ where $U_\ell$ diagonalizes the charged-lepton Yukawa and $U_\nu$ diagonalizes the neutrino mass matrix (whose structural origin is entirely different — boundary ripples, not vortex ladders). This difference is the seed of §13.5.
- Flag: in the framework, $U_u$ and $U_d$ are *not* the identity and are *not* equal, because the three ξ-ladder bound states of Ch 10 §10.3 have different profiles and therefore different overlaps with the up-type Higgs vacuum expectation value versus the down-type.

**Exit condition.** The reader knows (i) what the flavor and mass bases are, (ii) why the framework does not align them, (iii) the precise definitions of $V_{\rm CKM}$ and $U_{\rm PMNS}$, and (iv) that both are $3\times 3$ unitary — the chapter's first RIGOROUS structural result.

**Equations.** (4.13.1)–(4.13.5).

**Figures.** Fig 4.13.2 (flavor eigenbasis vs mass eigenbasis geometry).

---

### §13.2 — $V_{\rm CKM}$ from ξ-Ladder Overlap Integrals

**Target length:** ~1,200 words (≈ 3–4 pages)

**Topic sentence.** The CKM matrix elements are overlap integrals between up-type and down-type vortex eigenstates on the Ch 10 ξ-ladder, weighted by the Higgs profile, and the *complex phases* of those overlaps are where CP violation is quietly born.

**"Why" entry point.** Why should these integrals be complex rather than real? Because the vortex solutions of Ch 10 §10.4 carry a topological (winding) phase that differs between the up-type and down-type sectors, and that phase survives the overlap.

**Key content.**
- Write the general overlap formula from Ch 10 §10.4, (4.10.18), and extend it to *cross-generation* overlaps. [Eqs (4.13.6)–(4.13.9)]
- Introduce the standard PDG parametrization of $V_{\rm CKM}$ in three mixing angles $(\theta_{12}^q, \theta_{13}^q, \theta_{23}^q)$ and one CP phase $\delta_{\rm CP}^q$.
- Inherit (do not rederive) the Kobayashi-Maskawa counting theorem from Ch 11 §11.9 equation (4.11.39): for $n$ generations an $n\times n$ unitary matrix has $n(n-1)/2$ mixing angles and $(n-1)(n-2)/2$ physical CP-violating phases. For $n = 3$ this gives exactly three angles and exactly one phase — matching the PDG parametrization.
- Restate the Ch 11 §11.9 result explicitly: *for fewer than three generations there is no CP phase at all*. Two generations → zero phases. Three → one. The existence of CP violation is therefore a structural consequence of the three-bound-state count on the ξ-ladder, which was itself a structural consequence of the double-well potential of Vol 1 Ch 5. Label this result **RIGOROUS**. [Eq (4.13.10)]
- Set up the explicit form of the overlap-integral CKM entry: $V_{ij}^{\rm CKM} \propto \int d\xi\,\chi_i^{u*}(\xi)\,v(\xi)\,\chi_j^{d}(\xi)$, where the $\chi$ are the ξ-ladder bound-state profiles from Ch 10 §10.3 and $v(\xi)$ is the Higgs profile on the membrane. [Eqs (4.13.11)–(4.13.13)]
- Note that the *magnitude* of $|V_{ij}|$ is pattern-correct — hierarchical — because the Ch 10 ladder eigenfunctions have hierarchically different localization scales. Precise magnitudes inherit Ch 10 error bars.
- Write one boxed result at the end of the section: the CKM matrix written as the product $U_u^\dagger U_d$, each factor in terms of overlap integrals, with the promise that the Wolfenstein expansion of §13.3 will make the hierarchy visible.

**Exit condition.** The reader has the framework formula for $V_{\rm CKM}$, understands that its nonzero CP phase is guaranteed by three generations plus KM counting, and knows the values will come out pattern-correct but not precision-correct.

**Equations.** (4.13.6)–(4.13.13).

**Figures.** None (Fig 4.13.3 belongs in §13.3).

---

### §13.3 — The Wolfenstein Hierarchy and the Jarlskog Invariant

**Target length:** ~1,300 words (≈ 3–4 pages)

**Topic sentence.** The CKM matrix has an astonishingly clean expansion in a single small parameter $\lambda \approx 0.22$, the sine of the Cabibbo angle, and this one small parameter organizes the entire quark mixing hierarchy; in the framework, $\lambda$ is the ratio of two neighboring ξ-ladder overlaps.

**"Why" entry point.** Why is there only one small parameter and not three independent ones? Because the three ξ-ladder bound states share a common localization structure; the ratios between their overlap integrals are not independent but cascade by a common factor.

**Key content.**
- Introduce the Wolfenstein parametrization: $\lambda$, $A$, $\rho$, $\eta$. [Eqs (4.13.14)–(4.13.15)]
- Derive $\lambda \approx 0.22$ as the sine of the Cabibbo angle from the Ch 10 §10.4 up-down overlap between the first two generations. Show the framework gets it within a factor of 2 — call this **APPROXIMATE**. [Eq (4.13.16)]
- State the hierarchy: $|V_{us}|\sim\lambda$, $|V_{cb}|\sim\lambda^2$, $|V_{ub}|\sim\lambda^3$. The framework produces this pattern correctly because the Ch 10 ladder profiles cascade. [Eq (4.13.17)]
- Define the Jarlskog invariant $J_{\rm CP} = {\rm Im}(V_{us}V_{cb}V_{ub}^*V_{cs}^*)$ as the one reparametrization-independent measure of CP violation in the quark sector. [Eq (4.13.18)]
- State the RIGOROUS structural result: $J_{\rm CP}\neq 0$ follows from three generations plus KM counting, independent of any numerical details. Boxed. [Eq (4.13.19)]
- Report the value: framework gives $J_{\rm CP}\sim\text{few}\times 10^{-5}$ by order of magnitude; PDG gives $J_{\rm CP} = (3.18 \pm 0.15)\times 10^{-5}$. Label **APPROXIMATE**, explain the error budget: the individual complex overlap phases inherit Ch 10's 15–99% error bars, and $J_{\rm CP}$ is a small quadruple product whose numerical magnitude depends sensitively on cancellations. [Eq (4.13.20)]
- Draw the unitarity triangle as an inset (see Fig 4.13.3). State that the framework is *consistent* with the triangle closing, but does not independently predict its three angles to precision.

**Exit condition.** The reader has the Wolfenstein expansion, knows that the hierarchical CKM pattern falls out of the framework at the tens-of-percent level, understands that $J_{\rm CP}\neq 0$ is rigorous while the value is approximate, and has seen the Ch 11 §11.9 CP phase gap begin to close.

**Equations.** (4.13.14)–(4.13.20).

**Figures.** Fig 4.13.3 (Wolfenstein hierarchy visualization with unitarity triangle inset).

---

### §13.4 — $U_{\rm PMNS}$ from η-Boundary Ripple Overlap Integrals

**Target length:** ~1,100 words (≈ 3 pages)

**Topic sentence.** The neutrino mixing matrix has the same $3\times 3$ unitary form as the CKM matrix, but the ingredients that build it come from an entirely different zone sector — the η-boundary ripple tower — and that sector is nearly degenerate in mass where the ξ-ladder is hierarchical.

**"Why" entry point.** Why aren't neutrinos just another column on the ξ-ladder? Because they have no electric charge and no color, and the Genesis Physics framework places them on the η boundary of the zone manifold rather than in its ξ bulk — the `06-NEUTRINO_PHYSICS.md` research document is explicit about this.

**Key content.**
- Briefly summarize the neutrino sector of Ch 10 §10.6 and `06-NEUTRINO_PHYSICS.md`: three boundary-ripple ground states on the η-wall, with a ladder index inherited from the boundary eigenvalue problem. The three states are nearly degenerate because the boundary potential is shallow.
- Construct the lepton mixing matrix analogously to §13.2: $U_{\rm PMNS} = U_\ell^\dagger U_\nu$. Write it in the PDG standard parametrization: three mixing angles $(\theta_{12}^\ell, \theta_{13}^\ell, \theta_{23}^\ell)$, one Dirac CP phase $\delta_{\rm CP}^\ell$, and — *if* neutrinos are Majorana — two additional Majorana phases $\alpha_{21}, \alpha_{31}$. [Eqs (4.13.21)–(4.13.24)]
- State the Dirac/Majorana ambiguity honestly: the Genesis framework is compatible with either. The η-boundary ripple construction does not fix the answer, and `06-NEUTRINO_PHYSICS.md` leaves it open. Experimental resolution is 0νββ. Label **OPEN**. [Eq (4.13.25)]
- Write the framework formula for the PMNS entries as overlap integrals of the charged-lepton ξ-ladder profile against the η-boundary ripple eigenfunctions. Note the geometry: this is a cross-sector overlap, which is why the value does not inherit the same error structure as the CKM.

**Exit condition.** The reader has the PMNS construction, knows where the Dirac/Majorana ambiguity lives, and is primed to understand why the mixing pattern is structurally different from CKM.

**Equations.** (4.13.21)–(4.13.25).

**Figures.** None (Fig 4.13.4 in §13.5).

---

### §13.5 — The Bi-Large Pattern: Hierarchy vs. Near-Degeneracy

**Target length:** ~1,200 words (≈ 3–4 pages)

**Topic sentence.** The same overlap-integral formula that produces small CKM angles in the hierarchical ξ-ladder produces large PMNS angles in the near-degenerate η-boundary tower — one mechanism, two regimes.

**"Why" entry point.** Why are neutrino mixing angles so much larger than quark mixing angles? Because large mixing is the *generic* outcome of diagonalizing a perturbation in a near-degenerate system, while small mixing is the generic outcome in a hierarchical system.

**Key content.**
- Report the PMNS mixing angles from the η-boundary overlap integrals: $\sin^2\theta_{12}\approx 0.30$, $\sin^2\theta_{23}\approx 0.50$, $\sin^2\theta_{13}\approx 0.022$. Compare to global fit: $0.304 \pm 0.013$, $0.50 \pm 0.03$, $0.0219 \pm 0.0009$. Label **PHENOMENOLOGICAL** because the framework gets the pattern from `06-NEUTRINO_PHYSICS.md` but the precise values require a full numerical solve of the boundary eigenvalue equation that Vol 4 does not redo. [Eqs (4.13.26)–(4.13.29)]
- State the mass-squared differences from the boundary eigenvalue spectrum: $\Delta m_{21}^2 \approx 7.5\times 10^{-5}$ eV², $\Delta m_{32}^2 \approx 2.5\times 10^{-3}$ eV², and the ratio $\approx 33$ — the "mild" hierarchy between solar and atmospheric splittings. Note the absolute mass scale is not pinned; cosmology bounds $\sum m_\nu < 0.12$ eV, oscillation experiments give only differences. [Eqs (4.13.30)–(4.13.32)]
- Explain the mechanism. For the quark sector: in a perturbation-theoretic expansion of the overlap matrix, the mixing angle between generations $i$ and $j$ scales like $\delta m_{ij}/(m_i + m_j)$, so a *large* mass hierarchy suppresses mixing. For the neutrino sector: the same formula with nearly degenerate $m_i$ produces order-unity mixing. The *same equation* runs in opposite limits.
- Write this explicitly as one universal formula with two regimes: $\tan 2\theta = 2V/(m_j - m_i)$ for a two-state perturbation of off-diagonal strength $V$. Hierarchy → small $\theta$. Degeneracy → $\theta\to\pi/4$. Both extremes observed. [Eqs (4.13.38)–(4.13.40)]
- Emphasize this is the chapter's *single most important mechanistic picture* (per reviewer mandate), because it explains the biggest empirical puzzle of flavor physics — why CKM and PMNS are so different — with one line of physics.
- Close the section by asking what the framework *predicts correctly here that the Standard Model does not*: the Standard Model takes both matrices as data fits; the Genesis framework derives the *regime* (hierarchy vs degeneracy) from the two different zone sectors. That is structurally more than the SM delivers, even if the numerics are not yet better.

**Exit condition.** The reader understands (i) the framework's PMNS parameter values and their PHENOMENOLOGICAL status, (ii) the mechanism that explains the size difference between CKM and PMNS angles, and (iii) why this is a structural victory for the framework even though the numerics inherit error bars.

**Equations.** (4.13.26)–(4.13.32), (4.13.38)–(4.13.40).

**Figures.** Fig 4.13.4 (PMNS bi-large pattern and near-degeneracy mechanism).

---

### §13.6 — Neutrino Oscillations and the $\delta_{\rm CP}^{\rm lepton}$ Prediction

**Target length:** ~900 words (≈ 2–3 pages)

**Topic sentence.** Neutrino oscillations are the only known window onto the PMNS phase, and the framework's prediction for $\delta_{\rm CP}^{\rm lepton}$ is a target for DUNE and Hyper-K.

**"Why" entry point.** Why should we believe a ν_μ produced at Fermilab becomes a mixture at DUNE? Because $U_{\rm PMNS}$ is nondiagonal and the three mass eigenstates propagate with different phases, so coherent flavor does not survive.

**Key content.**
- Write the three-flavor oscillation probability formula from quantum mechanics with $U_{\rm PMNS}$ as input: $P(\nu_\alpha\to\nu_\beta, L) = |\sum_i U_{\beta i}U^*_{\alpha i}\exp(-i\Delta m_i^2 L/(4E))|^2$. Reduce it to the two-flavor approximation that dominates solar and atmospheric baselines. [Eqs (4.13.33)–(4.13.37)]
- Plug in the Ch 13 PMNS parameters and the two mass splittings. Show the framework's oscillation probability for the solar ($L/E\sim 10^4$ km/GeV) and atmospheric ($L/E\sim 500$ km/GeV) regimes matches data within the error bars inherited from Ch 10 and `06-NEUTRINO_PHYSICS.md`.
- State the framework's $\delta_{\rm CP}^{\rm lepton}$ prediction: heuristic, $\sim 3\pi/2$, from the chirality asymmetry of the ξ vs η sectors. Note: (a) this is not a precision prediction; (b) the global-fit best value is in the same ballpark but the 1σ range is large; (c) DUNE and Hyper-K will measure it to high precision. Label **OPEN**.
- State the payoff: *this is a live prediction*. Unlike the CKM phase, which is already measured, $\delta_{\rm CP}^{\rm lepton}$ is a genuine target for falsification over the next decade.

**Exit condition.** The reader has the oscillation formula, knows the framework's numerical status, and sees the upcoming experimental tests.

**Equations.** (4.13.33)–(4.13.37).

**Figures.** Fig 4.13.5 (neutrino oscillation waves for solar and atmospheric baselines; $\delta_{\rm CP}$ dependence shown as shaded band).

---

### §13.7 — Closing the Ch 11 §11.9 CP Gap: What Is Now Settled, What Is Not

**Target length:** ~900 words (≈ 2–3 pages)

**Topic sentence.** Ch 11 §11.9 flagged the CP-phase derivation as the largest open gap in the electroweak chapter and routed it to Ch 13 (GitHub issue #3). Ch 13 is where that gap closes — structurally completely, numerically partially — and this section is the explicit ledger.

**"Why" entry point.** Why can't we just declare victory because $J_{\rm CP}\neq 0$? Because the experimental number is precisely measured and the framework's number has multiplicative error bars inherited all the way from the Vol 1 double-well potential.

**Key content.**
- Revisit the Ch 11 §11.9 gap statement exactly as it was written. Quote the GitHub #3 language.
- Walk the chain: three generations (Ch 10 §10.3, RIGOROUS) → $3\times 3$ unitary mixing matrix (this chapter §13.1, RIGOROUS) → KM counting (Ch 11 §11.9, RIGOROUS) → one CP phase exists (this chapter §13.3, RIGOROUS) → Jarlskog invariant nonzero (this chapter §13.3, RIGOROUS) → numerical value from overlap phases (this chapter §13.3, APPROXIMATE with inherited Ch 10 error bars).
- State explicitly what is now RIGOROUS and what is not:
  1. The CP phase *exists*. RIGOROUS.
  2. The CP phase is *one*, not zero or two. RIGOROUS.
  3. The Jarlskog invariant is nonzero. RIGOROUS.
  4. The value of $J_{\rm CP}$ is an order-of-magnitude match. APPROXIMATE.
  5. The lepton Dirac phase is predicted heuristically at $\sim 3\pi/2$. OPEN.
- Relabel GitHub issue #3 from **BLOCKER** to **APPROXIMATE**. The structural gap is *closed*; the numerical gap persists and is routed to two future improvements: (a) Vol 5 will do the sphaleron-rate calculation for $\eta_B$; (b) a refined Ch 10 derivation with tighter fermion-mass error bars would propagate directly here. [Eqs (4.13.41)–(4.13.42)]
- Short paragraph on the connection to `06-MATTER_ANTIMATTER_ASYMMETRY.md`. The chain $\delta_{\rm CP}^q\to J_{\rm CP}\to$ sphaleron rate $\to \eta_B\approx 6\times 10^{-10}$ is the framework's path to baryogenesis. Ch 13 does not compute $\eta_B$ (that is Vol 5), but it states the dependency explicitly so the chain is audit-ready. [Eq (4.13.43)]

**Exit condition.** The reader knows, to the decimal, what Ch 13 moved and what it did not. GitHub #3 is relabeled.

**Equations.** (4.13.41)–(4.13.43).

**Figures.** Fig 4.13.6 (CP-phase gap closure status map: before vs after Ch 13).

---

### §13.8 — The Ch 13 Precision Ledger

**Target length:** ~600 words (≈ 1–2 pages)

**Topic sentence.** Every numerical claim in this chapter is now collected on one page with its rigor label, and the result is a chapter whose structural deliverables are rigorous while whose numerical deliverables are not.

**"Why" entry point.** Why is this ledger the heart of the chapter? Because the Skeptic reviewer — and the reader — must be able to see in one glance exactly how much the framework has and has not done.

**Key content.**
- Table 4.13.1 with columns: *Quantity*, *Framework value*, *Experimental value*, *Rigor label*, *Source of uncertainty*. Entries include: $3\times 3$ unitarity (RIGOROUS, structural), KM one-phase count (RIGOROUS, inherited from Ch 11), $J_{\rm CP}\neq 0$ (RIGOROUS), $\lambda\approx 0.22$ (APPROXIMATE), the three CKM angles (APPROXIMATE, pattern), $J_{\rm CP}$ value (APPROXIMATE, inherits Ch 10), PMNS angles (PHENOMENOLOGICAL), PMNS mass splittings (PHENOMENOLOGICAL), PMNS Dirac phase (OPEN), PMNS Majorana phases (OPEN, and open to Dirac/Majorana), absolute neutrino mass (OPEN, from elsewhere).
- Short prose commentary on the ledger. The structural half is rigorous. The numerical half is not yet. The Skeptic's mandate is satisfied by stating this clearly rather than by manufacturing false precision.
- One sentence on the reader's recourse: Ch 10's error-bar table is the upstream source of nearly all uncertainty in this chapter; any tightening there propagates here.

**Exit condition.** The reader has a single-page honest summary of the chapter's entire quantitative claim surface.

**Equations.** None new.

**Figures.** Fig 4.13.7 (Ch 13 honest ledger, rendered as a schematic table).

---

### §13.9 — Handoff: To Ch 14, to Vol 5, and to DUNE

**Target length:** ~500 words (≈ 1–2 pages)

**Topic sentence.** Three handoffs leave this chapter pointing outward: Ch 14 inherits the structural claim that three generations is all there is; Vol 5 inherits the chain to $\eta_B$; the next decade of experiments inherits $\delta_{\rm CP}^{\rm lepton}$.

**"Why" entry point.** Why do we need three distinct handoffs? Because the structural result goes to theory, the quantitative result goes to cosmology, and the open result goes to experiment — each needs a different successor.

**Key content.**
- **Handoff to Ch 14 (Beyond the Standard Model).** The $3\times 3$ unitarity is framework-forced (three ξ-ladder bound states, no more). Any BSM physics that posits a fourth generation is a *prediction-breaker* for the Genesis framework. Ch 14 will state this as a falsification criterion.
- **Handoff to Vol 5 (Cosmological Evolution).** The chain $J_{\rm CP}^{\rm quark}\to$ sphaleron rate $\to \eta_B$ is precisely what Vol 5 Chapters on the first day of Creation will compute. The Ch 13 output is Vol 5's input.
- **Handoff to DUNE and Hyper-K.** The framework's $\delta_{\rm CP}^{\rm lepton}\sim 3\pi/2$ is a live prediction. If DUNE measures $\delta_{\rm CP}^{\rm lepton}\approx 0$ (no CP violation in the lepton sector), the framework's chirality-asymmetry argument is wrong and must be revised.
- **Handoff to 0νββ experiments.** The Dirac/Majorana ambiguity is unresolved. The framework is consistent with either. A positive 0νββ observation would fix the neutrino nature as Majorana; a tight null would tighten the framework's allowed parameter space.
- Close with one short sentence of the chapter's thematic payoff: three generations, one small parameter, one CP phase — and the rest of the numerics is honest work yet to do.

**Exit condition.** The reader knows exactly where each outstanding question goes next.

**Equations.** None new.

**Figures.** None (Fig 4.13.7 still visible from §13.8).

---

### Problem Set

**Target length:** ~500 words (≈ 1–2 pages)

Six problems as specified in Ch13_SPEC.md, grouped by tier:

| # | Tier | Problem | Skills Tested |
|---|------|---------|---------------|
| P1 | Computational | KM counting for $n = 2, 3, 4, 5$ generations: how many angles, how many phases? Reverify (4.11.39). | Discrete counting, linear algebra of unitary matrices |
| P2 | Computational | Given $\lambda = 0.22$, $A = 0.81$, $\rho = 0.15$, $\eta = 0.35$, compute $V_{\rm CKM}$ to order $\lambda^3$ and check unitarity of each row and column. | Wolfenstein expansion, matrix arithmetic |
| P3 | Computational | Compute $P(\nu_\mu\to\nu_e)$ at $L/E = 500$ km/GeV using framework PMNS parameters vs PDG. Plot the difference. | Three-flavor oscillation formula |
| P4 | Conceptual | In under 200 words, explain why three generations force CP violation while two do not. Tie it to the three-bound-state count of §10.3. | Structural reasoning |
| P5 | Conceptual | In under 200 words, explain why CKM angles are small while PMNS angles are large, in terms of hierarchy vs. near-degeneracy. | Mechanistic physical intuition |
| P6 | Challenge | Trace the chain $J_{\rm CP}^{\rm quark}\to$ sphaleron rate $\to \eta_B$. Which step introduces the largest uncertainty? Which experiment would reduce it most? | Multi-chapter synthesis, error propagation |

---

## Equation Ledger (Contiguous Count)

| Range | Section | Topic |
|-------|---------|-------|
| (4.13.1)–(4.13.5) | §13.1 | Flavor-mass basis definition; charged-current vertex; $V_{\rm CKM} = U_u^\dagger U_d$; $U_{\rm PMNS} = U_\ell^\dagger U_\nu$ |
| (4.13.6)–(4.13.10) | §13.2 | Overlap-integral CKM formula (basic form); PDG parametrization; KM counting inherited from Ch 11 (4.11.39) |
| (4.13.11)–(4.13.13) | §13.2 | Cross-generation overlap integrals; complex topological phases |
| (4.13.14)–(4.13.17) | §13.3 | Wolfenstein parameters $(\lambda, A, \rho, \eta)$; Cabibbo angle; Wolfenstein hierarchy |
| (4.13.18)–(4.13.20) | §13.3 | Jarlskog invariant definition; structural $\neq 0$ result; numerical value |
| (4.13.21)–(4.13.25) | §13.4 | PMNS standard parametrization; Majorana phases; Dirac/Majorana ambiguity statement |
| (4.13.26)–(4.13.29) | §13.5 | PMNS angles from η-boundary overlap |
| (4.13.30)–(4.13.32) | §13.5 | Neutrino mass-squared differences |
| (4.13.33)–(4.13.37) | §13.6 | Three-flavor oscillation probability |
| (4.13.38)–(4.13.40) | §13.5/§13.6 | Hierarchy-vs-degeneracy universal formula (tan 2θ) |
| (4.13.41)–(4.13.42) | §13.7 | GitHub #3 structural closure; rigor inheritance statement |
| (4.13.43) | §13.7 | Handoff to $\eta_B$ computation (Vol 5) |

Target: 43 equations minimum. Draft may extend into (4.13.44)–(4.13.48) if the hierarchy-vs-degeneracy derivation in §13.5 expands.

---

## Figure Ledger

| Fig ID | Section | One-Line Purpose |
|--------|---------|-----------------|
| Fig 4.13.1 | §13.0 | Chapter roadmap — two sectors, two matrices, one gap closure |
| Fig 4.13.2 | §13.1 | Flavor vs mass basis geometry; the charged-current rotation |
| Fig 4.13.3 | §13.3 | Wolfenstein hierarchy plot + unitarity triangle inset |
| Fig 4.13.4 | §13.5 | Bi-large PMNS pattern and near-degeneracy mechanism (with CKM hierarchy contrast inset) |
| Fig 4.13.5 | §13.6 | Three-flavor oscillation curves for solar and atmospheric baselines; $\delta_{\rm CP}^\ell$ band |
| Fig 4.13.6 | §13.7 | GitHub #3 before/after status map |
| Fig 4.13.7 | §13.8 | Ch 13 honest precision ledger (schematic table rendered as figure) |

---

## Word-Budget Check

| Section | Target | Running Total |
|---------|--------|--------------|
| §13.0 | 700 | 700 |
| §13.1 | 1,100 | 1,800 |
| §13.2 | 1,200 | 3,000 |
| §13.3 | 1,300 | 4,300 |
| §13.4 | 1,100 | 5,400 |
| §13.5 | 1,200 | 6,600 |
| §13.6 | 900 | 7,500 |
| §13.7 | 900 | 8,400 |
| §13.8 | 600 | 9,000 |
| §13.9 | 500 | 9,500 |
| Problem set | 500 | 10,000 |

Target band 8,000–11,000: **within budget** with ~1,000-word headroom for derivation expansion during drafting.

---

## Voice and Tone Notes (for the Draft Phase)

- Open conversationally, like Ch 11 and Ch 12 do: a physical puzzle in the first paragraph, a promise in the second.
- Keep the Feynman cadence: ask a question, answer it, ask the next question. Do not lecture.
- Be *comfortable* with the honesty. The Skeptic must not feel like the chapter is flinching. Lines like "the framework gets this value wrong by a factor of three, and here is exactly why" are better than evasions.
- Box the structural results (the rigorous ones). Do not box the numerical ones.
- Do not fear repetition of the inheritance note ("this number inherits Ch 10's error bars"). The reader should leave having heard it enough that they could recite it.
- Avoid any temptation to lean on the theological parallel. If Genesis 1:14 appears as an epigraph, it is because the idea of *ordered distinctions into classes* resonates — not because there is a one-to-one map from day four to generation count. Keep the resonance light.

---

## Open Questions to Resolve During Drafting

1. **Should the unitarity-triangle calculation be explicit in §13.3, or demoted to a problem?** Leaning toward demoted — it would swell §13.3 past target length, and the problem set can carry it.
2. **Should §13.4 include a brief comparison to seesaw-type neutrino-mass mechanisms in the SM?** Probably one sentence only: the Genesis framework does not use seesaw; the neutrino masses are simply the boundary-ripple eigenvalues. Do not engage at length.
3. **Where exactly to place Fig 4.13.4's "contrast with CKM hierarchy" inset?** Either inside the PMNS figure (preferred, one-glance contrast) or as a separate mini-figure. Decide during figure generation.
4. **How much of the sphaleron/baryogenesis chain to spell out in §13.7 vs leave to Vol 5.** Leaning toward one paragraph in §13.7, plus Problem P6 in the problem set. Do not try to do the sphaleron calculation here.

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-09 | Initial outline created | Phase 2 of the genesis-chapter-writer lifecycle for Vol 4 Ch 13 |
