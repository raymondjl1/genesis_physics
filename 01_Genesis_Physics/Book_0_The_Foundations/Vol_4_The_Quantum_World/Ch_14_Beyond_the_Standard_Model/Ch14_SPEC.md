---
product: Foundations Vol 4 — The Quantum World
chapter: 14
title: Beyond the Standard Model
status: SPEC
created: 2026-04-09
---

# Chapter 14 — Beyond the Standard Model: Specification

## 1. Purpose

This is the capstone of Volume 4. Part III (Ch 10–13) has derived the Standard Model — leptons and quarks from ξ-ladder resonances (Ch 10), the electroweak theory from zone isometries (Ch 11), QCD from η-orbifold topology (Ch 12), and the CKM/PMNS mixing matrices from overlap integrals (Ch 13). Chapter 14 asks the capstone question: **what does Genesis Physics predict beyond the Standard Model, and how could it be killed?**

The chapter has three jobs:

1. **Predict BSM phenomenology.** Identify concrete, numerical predictions Genesis Physics makes that the Standard Model does not — dark matter candidates from the Waters Below, dark energy from the Waters Above, and collider signatures (cross-section patterns, rare decays, generation count bounds) testable at the LHC and next-generation machines.
2. **State falsification criteria explicitly.** For every prediction, give a number and a threshold. If X > Y is observed, the framework is wrong. No decorative predictions.
3. **Consolidate the open-problem ledger.** Every gap earlier chapters of Vol 4 left behind — the 1000× mass-scale problem, the Higgs potential O(1) coefficients, the spin-1/2 derivation, the CP phase, the fermion mass residuals — is collected here into a single research roadmap that Vol 6 will inherit as its testing suite.

## 2. Scope

- **Pages:** 20–30 (concise capstone; not a full research chapter).
- **Position:** Final chapter of Part III and of Vol 4. Directly precedes the Appendices and Problem Sets.
- **Voice:** Feynman writing a textbook — the same voice as Ch 1–13. Pedagogical but unsparing.
- **Audience:** Graduate students and professional physicists who have read Ch 1–13 of this volume and Vols 1–3.

## 3. Prerequisites

The chapter assumes the reader has completed:

- **Vol 1 Ch 5–6** (firmament and waters), **Ch 10** (quantization).
- **Vol 2 Ch 4** (strong/weak), **Ch 6** (gauge theory), **Ch 9** (explicit hierarchy-problem treatment), **Ch 10** (running couplings).
- **Vol 3 Part III** (statistical mechanics).
- **Vol 4 Ch 6–9** (QFT on the zone manifold, renormalization, Casimir).
- **Vol 4 Ch 10–13** (the entire Standard Model derivation). In particular the chapter inherits, without re-deriving, the three-bound-state count of Ch 10 §10.3, the Yukawa overlap formula of Ch 10 §10.4, the weak mixing angle of Ch 11 §11.5, and the CKM/PMNS structure of Ch 13.

## 4. Source Material

**Primary research files:**

- `Research/Mathematical_Models/06_Nuclear_and_Particle_Physics/06-REMAINING_DERIVATIONS.md` — the 1000× mass-scale problem, proposed resolution paths A–D, the boson-mass precision ledger (m_t, m_H, M_W, M_Z, ρ-parameter), the top decay-width discrepancy.
- `Research/Mathematical_Models/06_Nuclear_and_Particle_Physics/06-SYMMETRIES_MASS_INTEGRATION.md` — the consolidated symmetry→mass integration, the priority ledger of open problems (GUT, dark sector, neutrino sector, running couplings), the v_A (10^16 GeV) vs v_B (246 GeV) scale separation.

**Secondary (cited, not re-derived):**

- `06-HIGGS_DERIVATION.md`, `06-WEAK_PARITY_CP_VIOLATION.md` — inherited via Ch 11.
- `06-QCD_DERIVATION.md`, `06-SU3_YANG_MILLS_DERIVATION.md` — inherited via Ch 12.
- `06-NEUTRINO_PHYSICS.md`, `06-MATTER_ANTIMATTER_ASYMMETRY.md` — inherited via Ch 13.
- `06-PARTICLE_MASS_SPECTRUM_V3.md` — the 1000× problem in detail, inherited via Ch 10.
- `TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md` — particles as topological defects, inherited via Ch 10.

## 5. Critical Constraints (the Skeptic's Test)

The Skeptic (Dr. Marcus Chen) will test whether every prediction in this chapter is **testable or decorative**. The chapter passes the Skeptic's test only if:

- **C1.** Every BSM prediction comes with a number (or order-of-magnitude bracket), an experimental observable, and a falsification threshold. No "it would be interesting if" language without a number attached.
- **C2.** Every open problem is labeled with its inherited severity (BLOCKER, HIGH, MEDIUM) and its GitHub issue number, so the reader can audit the gap directly.
- **C3.** The hierarchy problem is not re-solved here — Vol 2 Ch 9 already addressed it. The chapter cites Vol 2 Ch 9 in one paragraph and moves on.
- **C4.** The 1000× mass-scale problem (Ch 10 BLOCKER) is named, its status stated, and the four proposed resolution paths (A–D from `06-REMAINING_DERIVATIONS.md` §9.1) listed with effort estimates. No hand-waving that it is "almost solved."
- **C5.** Dark matter candidates are discussed with specific masses, coupling regimes, and direct-detection signatures, not just labeled as "dark sector content."
- **C6.** The number of fermion generations (exactly three) is offered as a falsifiable prediction: discovery of a fourth generation kills the framework.
- **C7.** Decorative speculation about "what a future framework might achieve" is compressed into a single §14.7 handoff paragraph. The body of the chapter is predictions, not promises.

## 6. Chapter Structure

| § | Title | Pages | Role |
|---|---|---|---|
| 14.0 | The Bill Comes Due | 1.5 | Opening narrative. The Skeptic in the seminar room. What the framework owes now that Ch 10–13 are finished. |
| 14.1 | The Hierarchy Problem, Briefly | 1.5 | Brief recapitulation, citing Vol 2 Ch 9 for the full derivation. Why the membrane geometry separates v_B = 246 GeV from M_Planck ~ 10^19 GeV without fine-tuning. |
| 14.2 | Dark Matter from the Zone Architecture | 4 | Four candidate classes from the Waters and the boundary: (i) heavy KK excitations, (ii) η-boundary modes, (iii) vortex-sector dark states, (iv) radion/dilaton modes. Masses, couplings, and direct-detection signatures for each. |
| 14.3 | Dark Energy from the Waters Above | 2 | v_A ~ 10^16 GeV VEV of Ψ_A. Relation to the observed cosmological constant Λ_obs ~ 10^{-122} GeV^4. The cosmological-constant problem as an open problem, not a solved one. Handoff to Vol 5. |
| 14.4 | Predictions Testable at Colliders | 5 | Five concrete predictions: (1) boson-mass precision envelope (W/Z/H/t) with 1–2% falsification threshold, (2) exactly three generations, (3) Higgs branching-ratio pattern with allowed deviations, (4) FCNC rates at SM levels, (5) top-quark decay-width discrepancy as a signal that NNLO corrections must close a 25% gap or the framework is wrong. |
| 14.5 | The Falsification Table | 3 | A single numerical table: observable, Genesis prediction, current measurement, falsification threshold, experiment, timescale. Every entry from §14.2–§14.4 in one place. |
| 14.6 | The Research Roadmap | 4 | The consolidated open-problem ledger. All gaps from Ch 10–13 in priority order (CRITICAL / HIGH / MEDIUM / LOW), with GitHub issue numbers and effort estimates. The 1000× mass-scale problem with resolution paths A–D. The spin-1/2 BLOCKER. The CP-phase gap. GUT unification as the largest undone piece. |
| 14.7 | Handoff to Vol 5 and Vol 6 | 1 | One-paragraph handoff. Vol 5 inherits dark-sector cosmology; Vol 6 inherits the falsification table as its primary experimental test suite. |
| | Problem Set | 2 | 8–10 problems, mostly conceptual and order-of-magnitude, focused on the falsification criteria. |

**Total:** ~24 pages (within the 20–30 page bracket).

## 7. Results to be Labeled

In the same scheme used by Ch 13 — **RIGOROUS (structural)** vs. **APPROXIMATE (numerical)** vs. **OPEN** — the chapter will label:

- **Result 14.1 (RIGOROUS, structural).** Exactly three generations. Any fourth-generation discovery kills the framework.
- **Result 14.2 (RIGOROUS, structural).** The boson-mass hierarchy is not arbitrary: the ratio M_W/v is fixed by the geometric coupling g_W derived in Ch 11, and any precision shift beyond 2% falsifies the derivation.
- **Result 14.3 (APPROXIMATE).** Dark matter candidate masses from KK excitations: m > 0.95 GeV (n=1 η-mode) or > 2 GeV for accessible KK towers. No candidate exists at the typical WIMP mass (~100 GeV) from KK alone — if WIMPs are discovered in that range, they require a different sector.
- **Result 14.4 (APPROXIMATE).** Dark energy scale v_A ~ 10^16 GeV sets a characteristic GUT-adjacent scale; the framework does not yet predict its relation to Λ_obs.
- **Result 14.5 (OPEN, CRITICAL).** The 1000× fermion-mass-scale problem is unresolved. The framework is currently an effective theory at the electroweak scale, not a fundamental one.
- **Result 14.6 (OPEN, BLOCKER).** The spin-1/2 fermion derivation from the bosonic membrane (GitHub #1) remains unsolved. Without it, the fermion spectrum is assumed, not derived.

## 8. Figure Plan

Five figures, all schematic and low-complexity (no real data plots in this capstone chapter):

- **Fig 4.14.1** — Chapter roadmap. Four panels showing the four jobs of the chapter: hierarchy recap → dark sector → collider predictions → falsification ledger.
- **Fig 4.14.2** — Dark-matter candidate space. A mass-vs-coupling plot showing where the four Genesis candidate classes sit relative to WIMP, axion, and KK dark-matter windows. Current direct-detection exclusion lines overlaid.
- **Fig 4.14.3** — The cosmological-constant gap. A log-scale bar chart showing v_A (10^16 GeV), v_B (246 GeV), M_Planck (10^19 GeV), and Λ_obs^{1/4} (10^{-3} eV). Visual statement of the scale problem.
- **Fig 4.14.4** — The boson-mass precision ledger. Five bars (m_t, m_H, M_W, M_Z, ρ) showing Genesis prediction, PDG value, and the 2% falsification band. Visual restatement of §14.4.
- **Fig 4.14.5** — The research roadmap pyramid. The consolidated open-problem ledger stratified by priority (CRITICAL at the base, LOW at the apex), with GitHub issue numbers.

## 9. Equations Inherited (Not Re-derived)

- **(4.10.18), (4.10.19)** — Yukawa overlap integrals (Ch 10).
- **(4.11.22), (4.11.39)** — Charged-current Lagrangian and KM phase-counting theorem (Ch 11, reused in Ch 13).
- **(4.13.3), (4.13.4)** — CKM and PMNS definitions (Ch 13).
- **(2.9.*)** — Hierarchy-problem derivation (Vol 2 Ch 9).

New equations in Ch 14 will be numbered (4.14.1)–(4.14.~20). Most will be order-of-magnitude estimates, not precision derivations.

## 10. Voice Discipline

The chapter **must not**:

- Oversell. No claim that Genesis Physics is "close to" a final theory.
- Hide the 1000× problem behind euphemism. Say "1000×" out loud.
- Offer decorative predictions without numbers. Every prediction has a falsification threshold.
- Re-do Vol 2 Ch 9 on hierarchy. One-paragraph pointer and move on.
- Preach. No theology in the prose. The epigraph and §14.7 handoff are the only places the framework's larger intent surfaces.

The chapter **must**:

- Acknowledge every open problem earlier chapters flagged.
- Give the Skeptic nothing to attack on grounds of vagueness.
- Hand Vol 6 a clean experimental test suite.
- Close Vol 4 with a sentence that sets up Vol 5, not a sentence that sells Vol 4.

## 11. Reviewer Assignments

All six Vol 4 reviewers:

- **The Physicist** — technical soundness of BSM predictions; especially scrutinizes the dark-matter candidate masses and the falsification thresholds.
- **The Skeptic (Dr. Marcus Chen)** — CRITICAL reviewer for this chapter. Tests every prediction against C1–C7.
- **The Consistency Auditor** — checks that all inherited results from Ch 10–13 are cited correctly and that notation matches Vol 4 conventions.
- **The "But Why?" Reader** — asks why the framework predicts exactly these dark-matter candidates and not others.
- **The Writing Coach** — makes sure the capstone is not a dry list of predictions but closes the volume with appropriate weight.
- **The Student** — checks that the falsification table is usable as a study reference.

## 12. Handoff Dependencies

- **To Vol 5 (Cosmos):** Dark energy from Waters Above (§14.3), dark matter candidates (§14.2), and cosmological constant problem.
- **To Vol 6 (Predictions and Simulations):** The entire falsification table (§14.5) becomes Vol 6's primary experimental test suite. Vol 6 Chapter 1 will expand §14.5 into a full chapter.
- **To GitHub:** Issues #1, #2, #3, #25, #26 all referenced with current status. No issues closed by this chapter.

## 13. Quality Gates

- Every prediction has a number.
- Every number has a falsification threshold.
- Every open problem has a priority label and a GitHub issue.
- The chapter is 20–30 pages.
- The 1000× problem is named explicitly at least twice.
- The spin-1/2 BLOCKER is named explicitly.
- The chapter ends with a handoff, not a promise.
