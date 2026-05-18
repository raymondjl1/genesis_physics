---
product: Foundations Vol 4 — The Quantum World
chapter: 13
title: The CKM and PMNS Matrices
status: SPEC
created: 2026-04-09
role: Fourth chapter of Part III (The Standard Model Derived). Constructs the quark-sector (CKM) and lepton-sector (PMNS) mixing matrices from the flavor-vs-mass eigenbasis decomposition of the Ch 10 vortex sectors and the neutrino boundary-ripple sector, settles the CP-phase gap that Ch 11 §11.9 routed here (GitHub #3), and shows where the framework's order-of-magnitude success on baryon asymmetry η_B ≈ 6×10⁻¹⁰ connects to the one Jarlskog invariant of the quark sector and the still-unmeasured Dirac phase δ_CP of the neutrino sector. Short, focused, honest about what is open.
---

# Chapter 13: The CKM and PMNS Matrices — CHAPTER SPEC

## Mission

Chapter 13 is the last chapter of Part III where the framework still has something to derive from first principles. Its job is narrow and precise: take the flavor-eigenstate / mass-eigenstate mismatch that was already *stated* in Chapters 10 and 12 (quarks with $SU(3)_c$-labeled mass eigenstates but weak-current flavor labels) and in the neutrino sector that enters here for the first time (three boundary-ripple mass modes vs. three $SU(2)_L$-coupled flavor modes), and build out of it the two physical mixing matrices — the Cabibbo-Kobayashi-Maskawa matrix $V_{\rm CKM}$ for the quark sector and the Pontecorvo-Maki-Nakagawa-Sakata matrix $U_{\rm PMNS}$ for the lepton sector. Explicit deliverables:

1. State, precisely and in one place, why the mass eigenbasis and the weak-flavor eigenbasis are not aligned in this framework (they sit in different zone sectors — ξ-localized vortex ladder for quarks, η-boundary ripple tower for neutrinos — and the Higgs-mediated Yukawa rotation does not diagonalize the charged-current vertex).

2. Parametrize $V_{\rm CKM}$ in the standard three-angle plus one-phase form, and show that the *existence* of a nonvanishing Jarlskog invariant $J_{\rm CP}$ is forced by the Kobayashi-Maskawa counting already stated in Ch 11 §11.9 — a result this chapter inherits but does not rederive.

3. Compute (at the level the framework actually supports: order of magnitude for the phase, fit-within-pattern for the angles) the four parameters of $V_{\rm CKM}$ from the overlap integrals of the three ξ-ladder sectors, and compare the result to PDG.

4. Construct $U_{\rm PMNS}$ from the three-family boundary-ripple modes of `06-NEUTRINO_PHYSICS.md`, comparing to the global-fit data: $\sin^2\theta_{12} \approx 0.304$, $\sin^2\theta_{23} \approx 0.50$, $\sin^2\theta_{13} \approx 0.022$, $\delta_{\rm CP}^{\rm lepton}$ unmeasured but framework-predicted $\sim 3\pi/2$.

5. State the mass-squared differences $\Delta m_{21}^2 \approx 7.5\times 10^{-5}\,\text{eV}^2$ and $\Delta m_{32}^2 \approx 2.5\times 10^{-3}\,\text{eV}^2$ as inherited from the neutrino boundary-eigenvalue spectrum of Ch 10 §10.6 and the detailed solve in `06-NEUTRINO_PHYSICS.md`, and note that the *absolute* mass scale is not pinned by this chapter.

6. Close the loop back to Ch 11 §11.9 on CP violation: the Jarlskog invariant $J_{\rm CP} \approx 3 \times 10^{-5}$ of the quark sector is a framework observable; its *value* depends on the vortex-sector topological phases that Ch 10 §10.4 computed as overlap integrals, and this chapter is where those topological phases first enter as complex overlaps. State what is sharpened (the chain from overlap integrals to $J_{\rm CP}$ is now explicit) and what is not (the absolute magnitude is still only an order-of-magnitude estimate, because the individual phases depend on numerical data that Ch 10 reports with 15–99% error bars).

7. Connect to the matter-antimatter asymmetry of `06-MATTER_ANTIMATTER_ASYMMETRY.md`: the predicted $\eta_B \approx 6\times 10^{-10}$ depends multiplicatively on $\delta_{\rm CP}^{\rm quark}$ entering the sphaleron baryon-production rate. Chapter 13 does not compute $\eta_B$ — Vol 5 will — but it states the dependency explicitly and inherits Ch 11 §11.9's honest label: the framework *predicts that there is a CP phase at all* (rigorous, by Kobayashi-Maskawa counting plus three generations from Ch 10 §10.3), but does not yet predict the *value* of that phase.

8. State the three-generations question in the pattern-operator language of Vol 1 Ch 9 — three generations from the three ξ-ladder bound states — and confirm that the mixing-matrix structure for both quarks and leptons is therefore *constrained to be $3\times 3$ unitary* as a topological fact, not an empirical one. This is the chapter's only RIGOROUS structural result.

9. Label every prediction RIGOROUS / APPROXIMATE / PHENOMENOLOGICAL / OPEN on the same ledger Ch 10 / 11 / 12 used. Do not pretend that $\delta_{\rm CP}$ is predicted at the degree level. Do not pretend the PMNS angles are predicted at the percent level. State clearly what the framework *does* get right (the form of the matrix, the number of phases, the general pattern of neutrino mass hierarchy) and what it does *not* yet get right (the precise phase).

**The honest disposition of the chapter.** This is a short chapter — 20 to 30 pages, 8,000 to 11,000 words — and it is deliberately short because its content is narrow. It does not derive anything structurally new; it finishes a computation already begun in Chapters 10–12 and closes out the Ch 11 §11.9 gap on CP violation *as much as it can be closed at this stage*, which is less far than one might hope. The chapter is an exercise in *saying what can be said, precisely, and not pretending more*. The Skeptic reviewer will have the easiest job on this chapter because the honesty level has to be unusually high: essentially every quantitative prediction here is APPROXIMATE or PHENOMENOLOGICAL, and several are OPEN. What is RIGOROUS is the *structure* — that both matrices are $3 \times 3$ unitary, that the Jarlskog invariant is nonzero, that the PMNS sector has three mass eigenstates with two independent mass-squared differences, and that the baryon-asymmetry chain *has* a nontrivial CP input — and this structural rigor, modest as it sounds, is already more than the Standard Model Lagrangian delivers, because in the SM the form of the mixing matrices is a data fit, not a derivation.

---

## Requirements

| Req ID | Chapter Requirement | Traces To | Status |
|--------|---------------------|-----------|--------|
| Ch13-001 | State precisely why the weak-flavor basis and the mass basis are not aligned: they are labels attached to different zone sectors (ξ-ladder vortices for quarks/charged leptons; η-boundary ripples for neutrinos), and the Higgs-Yukawa rotation that diagonalizes the mass matrix does not diagonalize the charged-current vertex. | V4-004, V4-007 | NOT MET |
| Ch13-002 | Parametrize $V_{\rm CKM}$ in the PDG convention as three mixing angles $\theta_{12}, \theta_{13}, \theta_{23}$ and one CP-violating phase $\delta_{\rm CP}^q$. Inherit (not rederive) the KM counting theorem from Ch 11 §11.9 that for three generations exactly one physical CP phase survives. | V4-007, Ch 11 §11.9 | NOT MET |
| Ch13-003 | Derive the framework's formula for the CKM matrix elements as overlap integrals between the up-type and down-type ξ-ladder eigenstates of Ch 10, weighted by the Higgs profile. State what is *new* here that was not in Ch 10: the complex phase of each overlap integral, which is what produces $J_{\rm CP}\neq 0$. | V4-004, V4-007 | NOT MET |
| Ch13-004 | Report the four CKM parameters, each with a rigor label. The three mixing angles come out pattern-correct at the tens-of-percent level (hierarchical: $\theta_{12}\gg\theta_{23}\gg\theta_{13}$), matching the observed Wolfenstein hierarchy $\lambda, \lambda^2, \lambda^3$ with $\lambda\approx 0.22$. The Jarlskog invariant is order-of-magnitude: framework predicts $J_{\rm CP}\sim 10^{-5}$, PDG $J_{\rm CP}=3.18\times 10^{-5}$ — APPROXIMATE, because the individual phases carry Ch 10 fermion-mass error bars. | V4-007, Ch 10, Ch 11 | NOT MET |
| Ch13-005 | Parametrize $U_{\rm PMNS}$ in the standard three-angle, one-Dirac-phase, two-Majorana-phase form. Inherit the Majorana ambiguity honestly from Ch 11 §11.9 and the neutrino-physics research document: the framework is consistent with either Dirac or Majorana and cannot currently decide. | V4-007, Neutrino Research | NOT MET |
| Ch13-006 | Report the three PMNS mixing angles and the two mass-squared differences from the η-boundary eigenvalue spectrum. Compare: $\sin^2\theta_{12}\approx 0.30$ (framework) vs $0.304\pm 0.013$ (global fit); $\sin^2\theta_{23}\approx 0.50$ vs $0.50\pm 0.03$; $\sin^2\theta_{13}\approx 0.022$ vs $0.0219\pm 0.0009$. Note that the agreement is better than for CKM because the PMNS pattern arises from near-degeneracy of the three boundary-ripple ground states, which is structurally different from the Wolfenstein hierarchy. Label PHENOMENOLOGICAL (not RIGOROUS) because the precise values require a full numerical solve of the boundary eigenvalue equation. | V4-007, Neutrino Research | NOT MET |
| Ch13-007 | State the Dirac CP phase $\delta_{\rm CP}^{\rm lepton}$ as a framework prediction. Current: framework suggests $\delta_{\rm CP}^{\rm lepton}\sim 3\pi/2$ on heuristic grounds (the ξ-η asymmetry feeds in with a specific chirality); PDG best fit is in the neighborhood of $3\pi/2$ (unmeasured precisely). Label OPEN and testable (DUNE, Hyper-K). | V4-007, Neutrino Research | NOT MET |
| Ch13-008 | Close the Ch 11 §11.9 CP-phase gap as much as it can be closed *at this stage*. State precisely: (a) the existence of $\delta_{\rm CP}^q\neq 0$ is RIGOROUS; (b) the framework computation of the value is an APPROXIMATE chain that depends on complex topological phases from the Ch 10 overlap integrals; (c) those phases inherit Ch 10's error bars, so the value is quantitatively uncertain; (d) GitHub issue #3 is hereby re-labeled from BLOCKER to APPROXIMATE, since the structural gap is closed even if the numerical gap is not. | Ch 11 §11.9, GitHub #3 | NOT MET |
| Ch13-009 | Connect to the matter-antimatter asymmetry document. The chain is: Ch 13 $\delta_{\rm CP}^q \to$ Jarlskog $J_{\rm CP} \to$ instanton-driven baryon production rate $\to \eta_B \approx 6\times 10^{-10}$. State the chain, note that the quantitative computation of $\eta_B$ is Vol 5 business, and show that the Ch 13 output feeds the Ch 5 input. | V4-007, Matter-Antimatter Research | NOT MET |
| Ch13-010 | Three generations in the pattern-operator language. Connect §10.3 ξ-ladder bound-state count (three normalizable states) to Vol 1 Ch 9 pattern operators: the three generations are a structural consequence of the three-level bound-state problem on the Firmament membrane. The same structural fact *forces* both mixing matrices to be $3\times 3$ unitary, independent of any numerical details of the overlap integrals. | V4-002, V4-004, Vol 1 Ch 9 | NOT MET |
| Ch13-011 | Honesty audit: label every numerical result RIGOROUS / APPROXIMATE / PHENOMENOLOGICAL / OPEN. The $3\times 3$ unitary *structure* of both matrices is RIGOROUS. The $J_{\rm CP}\neq 0$ result for three generations is RIGOROUS (KM counting). All *values* of angles and phases are at best APPROXIMATE, most PHENOMENOLOGICAL, one (the lepton Dirac phase) OPEN. | V4-007, Reviewer Mandate | NOT MET |
| Ch13-012 | Ch 13 is a precision-limited chapter. State, at the outset and again in the final ledger, that every numerical result here inherits fermion-mass error bars from Ch 10. Do not hide or paper over this inheritance. | V4-007, Ch 10 | NOT MET |
| Ch13-013 | Provide a short problem set (≥ 6 problems) spanning computational (KM counting, Wolfenstein expansion, oscillation-length calculation) and conceptual (why three generations force a CP phase; what DUNE is measuring) tiers. | Foundations standard | NOT MET |
| Ch13-014 | Hand off cleanly to Ch 14 (Beyond the Standard Model): state which structural predictions survive (the $3\times 3$ unitarity is framework-forced, so any BSM physics that adds a fourth generation would break the framework), which questions are routed to Vol 5 (η_B computation), and which questions are routed to future experiments (DUNE, 0νββ). | Navigator Mandate | NOT MET |

---

## Prerequisites

| Concept | Established In |
|---------|---------------|
| Firmament, Waters Above, Waters Below, and the (ξ, η) extra-dimensional geometry with hard boundaries at ξ_A, η_B | Vol 1 Ch 5, Vol 1 Ch 6 |
| Zone Lagrangian; 6D action functional; Firmament action | Vol 2 Ch 5 |
| Pattern operators and the three-level structure of membrane bound-state problems | Vol 1 Ch 9 |
| Gauge group $U(1)\times SU(2)_L\times SU(3)_c$ from zone isometries | Vol 2 Ch 6 |
| Warp factor and the hierarchy $\eta_B \ll \xi_A$ | Vol 1 Ch 5, Vol 2 Ch 2 |
| 4D effective field theory from KK reduction; Higgs profile on the Firmament membrane | Vol 4 Ch 6 |
| Feynman rules and one-loop perturbation theory | Vol 4 Ch 7 |
| Renormalization and running couplings | Vol 4 Ch 8 |
| Vortex-sector particle classification: three ξ-ladder bound states → three generations; Yukawa coupling as an overlap integral | Vol 4 Ch 10 §§10.3–10.4 |
| Ch 10 fermion mass ledger with honest error bars (15–99%) | Vol 4 Ch 10 §10.9 |
| Electroweak $SU(2)_L\times U(1)_Y$ gauge structure; Higgs mechanism; charged-current vertex | Vol 4 Ch 11 |
| Kobayashi-Maskawa counting of physical CP phases for $n$ generations | Vol 4 Ch 11 §11.9 |
| CP violation as a *structural* framework prediction (existence, not value) | Vol 4 Ch 11 §11.9 |
| Jarlskog invariant $J_{\rm CP}$ as a reparametrization-independent observable | Vol 4 Ch 11 §11.9 |
| $SU(3)_c$ color-singlet classification; hadron spectrum; heavy-quark masses from Ch 10 | Vol 4 Ch 12 |
| The "short range" of the strong force does not affect the quark flavor mixing | Vol 4 Ch 12 |

---

## "Why" Chain

1. **Why do we need a mixing matrix at all — why aren't the flavor labels and the mass labels the same?** Because flavor labels come from the weak-current coupling (which is $SU(2)_L$ structure acting on left-handed doublets), whereas mass labels come from the eigenvalues of the Yukawa-Higgs coupling (which is a rotation in generation space). Unless the two happen to be aligned, the same physical particle has one label when it is propagating (mass) and a different label when it is decaying (flavor), and the relationship between the two is the mixing matrix.

2. **Why aren't they aligned in this framework specifically?** Because the weak-current coupling is inherited from Vol 2 Ch 6 and acts as a rigid $SU(2)_L$ rotation on all three generations identically, while the mass eigenvalues are the diagonal entries of a matrix of overlap integrals (Ch 10 §10.4) that is in general *not* proportional to the identity. The two are aligned only in the fictional limit where all three ξ-ladder Yukawa couplings coincide — which the framework's three-level bound-state spectrum explicitly forbids, because the three eigenfunctions have different profiles and therefore different overlaps with the Higgs.

3. **Why is the mixing matrix exactly $3\times 3$?** Because the Ch 10 §10.3 ξ-ladder has exactly three normalizable bound states, *no more, no less*, and this count is a robust feature of the double-well potential derived in Vol 1 Ch 5. A fourth mixing eigenstate would require either a fourth bound state in the ladder or a new sector outside the Firmament, and the framework admits neither at leading order. So the mixing matrix dimensionality is set by the zone topology, not fitted to data.

4. **Why is the mixing matrix unitary?** Because it is the change-of-basis transformation between two orthonormal bases on the same three-dimensional Hilbert space (the three-generation flavor space). Orthonormal change of basis is unitary by linear algebra. This is not a nontrivial physical fact but follows from conservation of probability.

5. **Why is there a CP-violating phase in the CKM matrix?** Because the Kobayashi-Maskawa counting (Ch 11 §11.9, equation 4.11.39) gives exactly one physical phase for a $3\times 3$ unitary matrix after all unphysical rephasings are removed. Fewer than three generations → zero phases; three or more → at least one. So the framework's prediction of exactly three generations, together with the KM counting, forces the existence of at least one CP-violating phase. This is the sense in which CP violation is a *theorem* in Genesis Physics, not an input.

6. **Why doesn't this chapter predict the *value* of $\delta_{\rm CP}^q$ precisely?** Because the value is set by the complex phases of the Ch 10 overlap integrals, and those phases depend on the detailed shape of the double-well potential and the Higgs profile, both of which Ch 10 computed to accuracies of 15–99% for the individual fermion masses. The phases inherit those error bars. Reporting $\delta_{\rm CP}^q$ to 0.01 radians would pretend to a precision the upstream inputs do not have.

7. **Why does the PMNS matrix look structurally different from CKM? (Near-maximal $\theta_{23}$, moderately large $\theta_{12}$, small $\theta_{13}$ — a "bi-large" pattern.)** Because the neutrinos, unlike the charged fermions of Ch 10, are *not* ξ-localized vortex modes. They are η-boundary ripple modes (`06-NEUTRINO_PHYSICS.md`). The three boundary ripple ground states are *nearly degenerate* in mass — their splittings come from small perturbations of the boundary potential rather than from orders-of-magnitude differences in the Yukawa overlap — and near-degeneracy with small perturbations produces large mixing angles, while the charged-fermion hierarchy produces small ones. The CKM smallness and the PMNS largeness are thus explained by *the same mechanism running in opposite regimes*: hierarchy → small angles (quarks), degeneracy → large angles (neutrinos).

8. **Why is the ratio $\Delta m_{32}^2 / \Delta m_{21}^2 \approx 33$?** This is the "mild" hierarchy between the atmospheric and solar mass splittings, and in the boundary-ripple model it comes from the fact that two of the three families are much more nearly degenerate with each other than with the third. The research doc (`06-NEUTRINO_PHYSICS.md`, §4.4) matches this ratio by adjusting the η-boundary potential parameters; Ch 13 inherits that match without rederivation.

9. **Why does the matter-antimatter asymmetry η_B care about the CKM phase?** Because the leading baryogenesis mechanism in the Genesis framework is the instanton/sphaleron process during Day 2 zone formation (`06-MATTER_ANTIMATTER_ASYMMETRY.md`), and the rate of that process is proportional to the CP asymmetry of the quark sector, which is the Jarlskog invariant $J_{\rm CP}$. No CP violation → no baryon asymmetry (Sakharov condition #2). So Ch 13's $J_{\rm CP} \neq 0$ result is what makes the Ch-5 (Vol 5) computation of η_B possible at all. The Ch 13 chain feeds directly into the matter-antimatter chain.

10. **Why is the framework's prediction of three-and-only-three generations the key structural claim, independent of all numerical details?** Because that one fact, by the KM counting, forces CP violation to exist; by the bound-state count, fixes the matrix dimensionality; and by the shared-topology argument for quarks and neutrinos, constrains both mixing matrices to be $3\times 3$. Three generations is the single most load-bearing prediction of Ch 10, and Ch 13 is where it pays structural dividends.

---

## Key Deliverables

### Derivations

| # | Derivation | Starting Point | Result | Equations |
|---|-----------|----------------|--------|-----------|
| 1 | Flavor-vs-mass eigenbasis distinction and the need for a mixing matrix | Ch 11 charged-current vertex, Ch 10 Yukawa-Higgs mass matrix | Charged-current vertex has a nontrivial matrix in generation space; matrix elements are CKM entries | (4.13.1)–(4.13.4) |
| 2 | Unitarity of $V_{\rm CKM}$ and the standard three-angle one-phase parametrization | Probability conservation in the three-generation Hilbert space | $V_{\rm CKM}$ is $3\times 3$ unitary; parametrized by $\theta_{12}^q, \theta_{13}^q, \theta_{23}^q, \delta_{\rm CP}^q$ | (4.13.5)–(4.13.9) |
| 3 | CKM matrix elements from Ch 10 overlap integrals, with explicit complex phases | Ch 10 §10.4 overlap formula, extended to cross-generation overlaps | $V_{ij}^{\rm CKM} \propto \int d\xi\,\chi_i^{u*}(\xi)\,H(\xi)\,\chi_j^{d}(\xi)$ with complex phase from vortex topology | (4.13.10)–(4.13.13) |
| 4 | Wolfenstein parametrization and the hierarchy $\lambda, \lambda^2, \lambda^3$ | Ch 10 §10.4 ξ-ladder profiles and the Cabibbo angle $\theta_c$ | $\lambda = \sin\theta_c \approx 0.22$; prediction pattern matches within a factor of 2 | (4.13.14)–(4.13.17) |
| 5 | Jarlskog invariant $J_{\rm CP}^{\rm quark}$ as the imaginary part of a specific CKM quadruple product | (4.13.9) and the complex phases of the overlap integrals | $J_{\rm CP}\neq 0$ is RIGOROUS (KM theorem); value $\sim 10^{-5}$ is APPROXIMATE | (4.13.18)–(4.13.20) |
| 6 | PMNS matrix in standard parametrization | Analogue of Derivation 2 for the lepton sector | $U_{\rm PMNS}$ is $3\times 3$ unitary with $\theta_{12}^\ell, \theta_{13}^\ell, \theta_{23}^\ell, \delta_{\rm CP}^\ell$ and two Majorana phases $\alpha_{21}, \alpha_{31}$ (if Majorana) | (4.13.21)–(4.13.25) |
| 7 | PMNS angles from η-boundary ripple overlap integrals (inheriting Research) | `06-NEUTRINO_PHYSICS.md` Part 7 | $\sin^2\theta_{12}\approx 0.30$, $\sin^2\theta_{23}\approx 0.50$, $\sin^2\theta_{13}\approx 0.022$ | (4.13.26)–(4.13.29) |
| 8 | Neutrino mass-squared differences from boundary-eigenvalue spectrum | `06-NEUTRINO_PHYSICS.md` Part 4, §4.4 | $\Delta m_{21}^2\approx 7.5\times 10^{-5}$ eV², $\Delta m_{32}^2\approx 2.5\times 10^{-3}$ eV² | (4.13.30)–(4.13.32) |
| 9 | Oscillation probability formula for two-flavor and three-flavor cases | Standard QM, with the PMNS matrix as input | $P(\nu_\alpha\to\nu_\beta, L) = \left|\sum_i U_{\beta i}U_{\alpha i}^* e^{-i\Delta m_i^2 L/(4E)}\right|^2$ | (4.13.33)–(4.13.37) |
| 10 | Hierarchy-vs-degeneracy mechanism for mixing-angle size | Ch 10 (hierarchy) vs Neutrino Research (degeneracy) | Quark angles small ↔ hierarchy; lepton angles large ↔ near-degeneracy; same formula, opposite limit | (4.13.38)–(4.13.40) |
| 11 | Honest disposition of GitHub #3 (Ch 11 §11.9 CP gap) | Ch 11 §11.9, Ch 13 derivations 3, 5 | Structural gap CLOSED (CP exists, framework observable); numerical gap APPROXIMATE (value inherits Ch 10 error bars) | (4.13.41)–(4.13.42) |
| 12 | Handoff to Vol 5 for η_B computation | Derivation 5, `06-MATTER_ANTIMATTER_ASYMMETRY.md` | $J_{\rm CP}^{\rm quark}$ feeds the sphaleron rate; quantitative η_B is Vol 5 | (4.13.43) |
| 13 | The Ch 13 precision ledger | Derivations 3–8 | Table 4.13.1 with rigor labels | — |

### Figures and Diagrams

| Fig ID | Title | Type | Placement | What It Shows | Why Needed | Key Labels | Eqs Ref'd | Complexity |
|--------|-------|------|-----------|---------------|-----------|------------|-----------|-----------|
| Fig 4.13.1 | Chapter roadmap: mixing matrices from two distinct zone sectors | Flowchart | §13.0 | Top: ξ-ladder vortex sector (Ch 10) → up-type and down-type Yukawa overlap → CKM matrix → $J_{\rm CP}^{\rm quark}$. Bottom: η-boundary ripple sector (Neutrino Research) → boundary overlap integrals → PMNS matrix → $\delta_{\rm CP}^{\rm lepton}$. Side branch: both feed the Ch 11 §11.9 gap closure. Dashed box marks the remaining quantitative gap (Ch 10 error bars). | Orientation — the reader must grasp immediately that quark mixing and lepton mixing come from *different* zone sectors with *opposite* size regimes | — | — | Medium |
| Fig 4.13.2 | Flavor eigenbasis vs mass eigenbasis geometry | Schematic | §13.1 | Three-dimensional diagram showing two orthonormal bases (flavor, mass) in the three-generation Hilbert space, with the rotation angle $\theta_c$ (Cabibbo) explicit between the first two, and small additional rotations for the other angles. Arrow showing charged-current vertex acting in the flavor basis but the propagator acting in the mass basis. | Without this picture the reader conflates flavor and mass; this is the conceptual pivot of the chapter | $|\nu_e\rangle, |\nu_\mu\rangle, |\nu_\tau\rangle, |\nu_1\rangle, |\nu_2\rangle, |\nu_3\rangle$ | (4.13.1)–(4.13.5) | Medium |
| Fig 4.13.3 | Wolfenstein hierarchy visualization | Plot / schematic | §13.3 | Log plot of the CKM matrix-element magnitudes $|V_{ij}|$ against their indices, showing the hierarchy $|V_{ud}|\approx 1$, $|V_{us}|\approx\lambda$, $|V_{ub}|\approx\lambda^3$, with the framework's predicted curve overlaid on the PDG data points. Also shows the unitarity triangle as an inset. | Makes the Wolfenstein $\lambda$ expansion visible and verifies the framework's hierarchy prediction | $\lambda, V_{ij}$, PDG | (4.13.14)–(4.13.17) | Medium |
| Fig 4.13.4 | PMNS bi-large pattern and near-degeneracy mechanism | Plot / schematic | §13.5 | Energy levels of the three η-boundary ripple ground states, showing near-degeneracy of ν₂ and ν₃ ("atmospheric pair"), the solar splitting of ν₁ below them, and the overlap integrals producing the large $\theta_{12}$ and near-maximal $\theta_{23}$. Contrast with the hierarchical CKM pattern in an inset. | The hierarchy-vs-degeneracy contrast is the chapter's single most important mechanistic picture | $m_{\nu_i}$, $\Delta m_{21}^2$, $\Delta m_{32}^2$, $\theta_{ij}$ | (4.13.26)–(4.13.32) | Medium |
| Fig 4.13.5 | Neutrino oscillation wave picture for solar and atmospheric baselines | Plot | §13.6 | Oscillation probability $P(\nu_\mu\to\nu_e)$ vs $L/E$, with vertical markers at the Kamiokande and DUNE baselines, and the effect of varying $\delta_{\rm CP}^{\rm lepton}$ between 0 and $2\pi$ shown as a shaded band. | Connects the framework's $\delta_{\rm CP}$ prediction to a measurable quantity DUNE will test | $P, L/E, \delta_{\rm CP}$, Kamiokande, DUNE | (4.13.33)–(4.13.37) | Simple |
| Fig 4.13.6 | CP-phase gap closure status map | Schematic | §13.7 | Two columns: "Before Ch 13" (GitHub #3, structural and numerical both open) and "After Ch 13" (structural CLOSED, numerical APPROXIMATE with Ch 10 error inheritance). | Skeptic demand — the reader must see exactly how far the chapter moved the ball and how far it did not | — | (4.13.41)–(4.13.42) | Simple |
| Fig 4.13.7 | Ch 13 honest ledger | Schematic table | §13.8 | Rigor categories across the chapter's main predictions, mapped onto the observable list (CKM angles, CKM phase, PMNS angles, PMNS Dirac phase, PMNS Majorana phases, mass splittings). | One-glance honesty summary | — | — | Simple |

### Problem Sets

| Difficulty | Count | Topics Covered |
|-----------|-------|---------------|
| Computational | 3 | (P1) Work through the KM counting (4.13.8) for $n = 2, 3, 4, 5$ generations. How many mixing angles, how many phases? Verify (4.11.39) from Ch 11. (P2) Given the Wolfenstein parameters $\lambda = 0.22$, $A = 0.81$, $\rho = 0.15$, $\eta = 0.35$, compute $V_{\rm CKM}$ entries to order $\lambda^3$ and check unitarity. (P3) Compute the oscillation probability $P(\nu_\mu\to\nu_e)$ at $L/E = 500$ km/GeV for the framework's PMNS parameters and the PDG values; plot the difference. |
| Conceptual | 2 | (P4) Explain, in under 200 words, why three generations force the existence of CP violation, while two generations do not. Tie this explicitly to the framework's three-bound-state prediction of §10.3. (P5) Explain, in under 200 words, why the CKM angles are small while the PMNS angles are large, in terms of hierarchy versus near-degeneracy of the underlying mass eigenstates. |
| Challenge | 1 | (P6) Trace the chain from the Ch 13 Jarlskog invariant $J_{\rm CP}^{\rm quark}$ through the instanton/sphaleron rate of `06-MATTER_ANTIMATTER_ASYMMETRY.md` to the baryon-to-photon ratio $\eta_B$. Identify exactly which step introduces the largest uncertainty. What observation (DUNE? 0νββ? LHC?) would reduce that uncertainty most? |

---

## Section Outline (Preview — full outline in Ch13_OUTLINE.md)

- §13.0 Introduction — two mixing matrices, one short chapter, honest about gaps
- §13.1 Flavor vs mass eigenstates: why the two bases are not aligned [RIGOROUS structural]
- §13.2 $V_{\rm CKM}$ from ξ-ladder overlap integrals [APPROXIMATE]
- §13.3 The Wolfenstein hierarchy and the Jarlskog invariant [APPROXIMATE for values, RIGOROUS for $J_{\rm CP}\neq 0$]
- §13.4 $U_{\rm PMNS}$ from η-boundary ripple overlap integrals [PHENOMENOLOGICAL, inherits Research]
- §13.5 The bi-large pattern: hierarchy vs near-degeneracy [APPROXIMATE mechanism]
- §13.6 Neutrino oscillations and the $\delta_{\rm CP}^{\rm lepton}$ prediction [OPEN for $\delta_{\rm CP}$]
- §13.7 Closing the Ch 11 §11.9 CP gap as far as it closes today [honest disposition]
- §13.8 The Ch 13 precision ledger [honest totals]
- §13.9 Handoff to Ch 14 and Vol 5 (and to DUNE)
- Problem set

---

## Verification Criteria

### Universal

- [ ] Every chapter requirement MET
- [ ] Every "Why" question answered in prose
- [ ] No forward dependency beyond the Ch 14 / Vol 5 handoff notes
- [ ] Notation consistent with Vols 1–3 and Vol 4 Ch 1–12
- [ ] Equation numbering $(4.13.1)$–$(4.13.43+)$ contiguous
- [ ] Word count 8,000–11,000 (20–30 page target for this focused chapter)
- [ ] No `[TODO]` markers
- [ ] Figure audit: every structural contrast (flavor vs mass; hierarchy vs degeneracy; before vs after Ch 11 §11.9) has a figure

### Product-Specific (Foundations)

- [ ] Every equation numbered; derivations cite prior results by number (including Ch 10 §10.4 and Ch 11 §11.9 equations)
- [ ] Key results boxed
- [ ] Honesty audit labels applied throughout — particularly on every *number*
- [ ] Problem set covers computational / conceptual / challenge tiers
- [ ] Grad-student test: a reader with the standard prerequisites can do the KM counting and the Wolfenstein expansion with only this chapter in hand
- [ ] The Ch 11 §11.9 CP gap is *explicitly revisited* and its new status stated precisely, not glossed
- [ ] The matter-antimatter asymmetry handoff is stated explicitly, not left implicit

---

## Assigned Reviewers

| Reviewer | Assigned? | Status | Date |
|----------|-----------|--------|------|
| The Physicist | YES — **critical** | — | — |
| The "But Why?" Reader | YES | — | — |
| The Writing Coach | YES | — | — |
| The Consistency Auditor | YES — **critical** (must match Ch 10, 11, 12 notation exactly) | — | — |
| The Skeptic | YES — **critical** (the honesty audit is this chapter's main deliverable) | — | — |
| The Student | YES | — | — |
| The Style Editor | YES | — | — |
| The Theologian | YES | — | — |
| The Navigator | YES | — | — |
| The Homeschool Mom | NO (Foundations) | — | — |

---

## Notes

- **The Skeptic is flagged critical.** This chapter must not pretend to more precision than the framework supports. Every number needs a rigor label; every label needs to match the actual upstream precision.
- **The Consistency Auditor is flagged critical.** Because this chapter inherits heavily from Ch 10 (overlap integrals), Ch 11 (KM counting, charged-current vertex), and Ch 12 (hadron mass inputs), the notation must match across all three without drift.
- The Physicist will want the explicit CKM derivation and the unitarity triangle check. The chapter provides both.
- The Navigator will note that this chapter is deliberately short (20–30 pages) and check that this is a *focused* shortness, not a *hurried* shortness. The outline explicitly enforces focus: no structurally new physics is introduced; every section is closing or extending a Ch 10–12 thread.
- The "But Why?" Reader will want to know *why* the same 3×3 structure appears in two sectors with opposite magnitudes. The "Why" chain item 7 above explicitly answers this.
- The Writing Coach will want the voice to stay Feynmanian even in a chapter whose content is mostly "here is the honest status of the gap." The introduction sets the tone: confident about structure, honest about numbers, not defensive.
- The Theologian will find no forced theology in this chapter; the Genesis 1 epigraph, if used, should be chosen for its resonance with the idea of ordered distinctions (Day 1 light/dark; Day 2 waters/waters; Day 4 sun/moon/stars — discrete sortings into classes), not for any forced particle-physics parallel.

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-09 | Initial spec created | Opening Phase 1 of the writer lifecycle for Vol 4 Ch 13 |
