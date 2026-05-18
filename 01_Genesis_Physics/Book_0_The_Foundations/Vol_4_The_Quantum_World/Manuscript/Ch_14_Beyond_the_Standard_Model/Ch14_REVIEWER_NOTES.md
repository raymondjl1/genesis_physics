---
product: Foundations Vol 4 — The Quantum World
chapter: 14
title: Beyond the Standard Model
status: REVIEWER_NOTES
created: 2026-04-09
---

# Chapter 14 — Reviewer Agent Notes

Six Vol 4 reviewers (all of the assigned set from the Vol 4 CLAUDE.md): The Physicist, The Skeptic (Dr. Marcus Chen), The Consistency Auditor, The "But Why?" Reader, The Writing Coach, The Student. Each has reviewed the DRAFT. Notes are organized by reviewer, with issues categorized as **BLOCKING**, **IMPORTANT**, or **MINOR**.

---

## The Skeptic (Dr. Marcus Chen) — CRITICAL reviewer for this chapter

The Skeptic is the chapter's primary adversary. The chapter was written with his hand raised in the seminar room; it is only honest to let him speak first.

### Overall verdict

The chapter passes the Skeptic's essential test. Every prediction in §14.4 has a number, and every number has a falsification threshold. The research roadmap in §14.6 names its blockers without euphemism. The falsification table in §14.5 gives a single-page summary that I can carry to a colleague and say "kill any one of these and the framework is done." I accept that.

But I have four specific objections. Three are important; one is blocking.

### BLOCKING — The 2% envelope claim in Prediction 14.1 is mathematically underspecified

The draft claims that the framework's prediction is that *all five* boson-sector observables (m_t, m_H, M_W, M_Z, ρ) lie simultaneously within 2% of their current PDG values. The claim is that this is a non-trivial constraint because the framework has only two inputs (g_W and v_B) in the boson sector.

This is almost right, but "2%" is pulled out of thin air. Where does 2% come from? Why not 0.5%, which is the worst current agreement (M_Z at 0.50%)? Why not 1%, which would be a 2× margin above the current worst? And why is the threshold *per-observable* rather than on the joint? If M_W shifts by 1.8% and M_Z shifts by 1.8% *in the same direction*, the framework is almost certainly wrong — but by the current wording, it survives.

**Fix required for FINAL:** state explicitly *how* the 2% threshold was chosen, and state the joint condition. The cleanest way is: "If the current central values are preserved to within their current PDG precisions (roughly 0.5% or better for the boson masses and 0.1% for the ρ parameter), the framework's derivation survives. A shift in any single mass by more than 2%, or a joint shift in any two masses by more than 1% in the same direction, falsifies the Ch 11 §11.5 derivation at the two-sigma level."

Until this is fixed, Prediction 14.1 is not quite a clean prediction. I will accept it once the threshold is tightened and justified.

### IMPORTANT — The Class A dark-matter cross-section range is suspiciously wide

§14.2 gives $\sigma_A^{\rm ann} \sim 10^{-44}$ to $10^{-42}$ cm². That is two orders of magnitude. For a prediction I am supposed to take seriously, this is already a wide prior; combined with the mass-range uncertainty of 0.95–1.9 GeV (which is another factor of two), the prediction is essentially "somewhere in the sub-GeV to few-GeV window, with a cross-section within two orders of magnitude of the weak scale." How is this distinguishable from a generic light-dark-matter model?

**Response:** This is fair. The framework's current precision in the η-boundary coupling is the limiting factor, and the cross-section uncertainty is inherited directly. In FINAL: acknowledge in §14.2 that the Class A cross-section range is two decades wide because of the currently uncomputed η-boundary vertex structure, and that RR-7 (running couplings) and RR-8 (neutrino mass generation) share the input needed to tighten it. This is better than pretending the range is sharper than it is.

### IMPORTANT — The "no WIMP" claim in Result 14.1 is framed as structural but depends on a numerical input

The draft labels Result 14.1 as "APPROXIMATE, falsifiable" but says the no-WIMP claim is "rigorous, from the structure of the Yukawa overlap integral." This is a contradiction — either the claim is structural or it is approximate. Which is it?

If the claim is that the ξ-ladder bound states are the *only* states that get Yukawa masses, and the continuum states (Class C) do not, and the η-boundary ripples (Class B) are light, and no other sector of the framework's architecture has a vertex into SM fermions at the right strength — then the claim is indeed structural, provided that "structural" is taken to mean "no new vertex can be added without violating the derivations of Ch 10–13."

**Fix required for FINAL:** separate the structural and the approximate parts of Result 14.1. The structural part: "within the current Lagrangian of Ch 10–13, no state acquires a WIMP-like weak-scale nucleon coupling." The approximate part: the specific mass ranges and cross-sections of Classes A–D. The two should be in different sentences of the Result box.

### MINOR — The top-decay-width NNLO prediction (Prediction 14.5) is not a prediction

If the framework's prediction is "we owe ourselves a calculation," that is a research plan, not a prediction. The Skeptic cannot falsify the framework by *failing to do* the calculation. The prediction only becomes a prediction once the calculation is done.

**Response:** I disagree with this framing in part. The prediction is that when the NNLO calculation is done, it will give a value in the range [1.85, 2.15] GeV, closing the gap. A value outside that range falsifies the framework. That is a prediction; the fact that it cannot be tested until the calculation is done does not make it non-predictive, any more than the fact that a Monte Carlo prediction for a future LHC run cannot be tested until the run happens makes it non-predictive. Leave Prediction 14.5 as is, but add one sentence clarifying that the prediction is on the *outcome* of the calculation, not on whether the calculation will be performed.

### Final note from the Skeptic

The chapter is the best Vol 4 has offered me. It does not oversell. It does not hide the blockers. It gives me fourteen ways to kill the framework, and it tells me which two are unresolved theoretical debts (RR-1, RR-2) before I even have to ask. If the four fixes above are applied, I sign off.

---

## The Physicist

The Physicist is the technical-soundness reviewer. All BSM predictions are scrutinized.

### BLOCKING — none.

### IMPORTANT

**(P1)** §14.2 equation (4.14.2) gives the KK mass spectrum $M_{m,\eta} = \hbar c \cdot m\pi/|\eta_B|$ and cites "(4.6.17)" as the source. I want to verify this is consistent with Ch 6's actual equation. The form is right — it is the Dirichlet-wall mode spectrum — but the prefactor convention may differ (some chapters use $\pi$, some use $\pi/2$, depending on boundary conditions). **Fix for FINAL:** verify the exact form of (4.6.17) in Ch 6 and ensure (4.14.2) matches.

**(P2)** §14.2 Class A claims that even-$m$ KK modes are stable against decay into lighter odd-$m$ modes "over cosmological timescales." This requires a lifetime calculation the draft does not actually perform. At mass 1.9 GeV, with a weak-loop coupling, the decay width should be roughly $\Gamma \sim (g_W^2/4\pi)^2 \cdot m_{\rm mode} \sim 10^{-6}$ GeV, giving a lifetime of $\sim 10^{-18}$ s — very much *not* cosmological. Something is wrong. Either the selection rule is not η-parity but something stronger, or the Class A candidate is the $m = 2$ state with a different protection mechanism, or the claim is wrong.

**Response:** This is a real issue. The draft's Class A argument is phenomenologically thin. In FINAL: rewrite Class A to identify the actual stability mechanism. The most likely candidate is a discrete gauge symmetry from the η-orbifold (Ch 12) that protects even-$m$ modes against decay into all-SM final states; this is the same mechanism that gives KK dark matter its stability in the Appelquist-Cheng-Dobrescu construction. Cite that construction (or the zone-QFT analogue) as the stability argument. If the argument cannot be made cleanly, downgrade Class A from "candidate" to "speculative candidate pending verification of the stability mechanism" and add a sub-item to RR-10.

**(P3)** §14.3 equation (4.14.10) uses $v_A^4/(4\pi)^2$ for the loop-level vacuum energy. This is the right order of magnitude for a one-loop scalar contribution, but the actual coefficient depends on the field content running in the loop. For the $\Psi_A$ field alone, one gets $(1/64\pi^2) v_A^4$; for a full spectrum, one gets larger coefficients. The "184 orders of magnitude" claim that follows in the text is not sensitive to this, because we are doing log-scale comparisons, but the equation itself should carry a "$\sim$" rather than an "$=$" and the text should say "the $O(1)$ coefficient depends on the field content in the loop." **Fix for FINAL:** the equation already has a "$\sim$" symbol; add the field-content caveat in the surrounding prose.

### MINOR

**(P4)** §14.4 FCNC predictions (4.14.13)–(4.14.14) use Standard Model values without citation. The B_s → μμ branching ratio has been measured at LHCb at $(2.85 \pm 0.33) \times 10^{-9}$, consistent with the SM prediction of $3.66 \times 10^{-9}$ — the draft's "$\sim 3 \times 10^{-9}$" is fine for order of magnitude but could be tightened. **Fix for FINAL (optional):** add a citation to the LHCb measurement, or leave as order-of-magnitude.

**(P5)** The radion mass range in §14.2 Class D (meV scale) is consistent with a Casimir-stabilized moduli potential but would benefit from a one-line explanation of *why* Casimir gives meV. Reader can work it out from Ch 9 but the chapter could help. **Fix for FINAL:** add "the Casimir energy density in the ξ-modulus sector is of order $\hbar c / \xi_A^4 \sim 10^{-38}$ GeV⁴, which gives a modulus oscillation frequency of roughly $10^{-13}$ Hz or a quantum of energy of order $10^{-3}$ eV."

---

## The Consistency Auditor

The Consistency Auditor checks that every inherited result is cited correctly and that notation matches Vol 4 conventions.

### BLOCKING — none.

### IMPORTANT

**(CA1)** The draft has **Finding 3** from the SELF_REVIEW: RR-12 in §14.6 cites "§14.2 above" for the out-of-equilibrium baryogenesis discussion, which is not present in §14.2. This is a citation error. **Fix for FINAL:** remove the "§14.2 above" clause. Keep only the Ch 13 §13.5 reference.

**(CA2)** The equation numbering is consistent with Vol 4 convention (4.Ch.Eq). All fifteen Ch 14 equations are correctly numbered. ✓

**(CA3)** The draft cites "Ch 13 Result 13.1" in §14.4 Prediction 14.4 (the FCNC prediction). Verified: Ch 13 §13.1 Result 13.1 is indeed the 3×3 unitarity result. ✓

**(CA4)** The draft cites "Vol 2 Ch 9 §9.4" and "(2.9.31)" in §14.1. I have not verified that (2.9.31) is the correct equation number in Vol 2 Ch 9 — the Consistency Auditor recommends spot-checking this in FINAL if Vol 2 Ch 9 is available. If Vol 2 Ch 9 uses different numbering, the citation needs to be adjusted.

**Response:** Vol 2 Ch 9 is marked as complete in the project state. The specific equation number (2.9.31) is my best estimate; if Vol 2 Ch 9 has a different layout the citation should be tightened to "Vol 2 Ch 9 §9.4" without the specific equation number, which is safer. **Fix for FINAL:** soften to "equation (2.9.31) or its equivalent in Vol 2 Ch 9 §9.4" OR drop the specific equation number and cite only the section. I prefer the latter as more conservative.

**(CA5)** The draft cites "Ch 6 equation (4.6.17)" for the KK tower. This requires verification against the actual Ch 6 draft. Same comment as above: cite the section if the equation number is uncertain.

### MINOR

**(CA6)** Epigraph is 1 Corinthians 13:12 (KJV). Formatting matches Ch 13's Genesis 1:14 epigraph. ✓

**(CA7)** Chapter title "Beyond the Standard Model" matches the Vol 4 outline. ✓

**(CA8)** The problem set is numbered 14.1–14.10 (ten problems). Matches SPEC's "8–10 problems." ✓

**(CA9)** In §14.2 Class B, the draft says "In Standard Model language, these are sterile neutrinos." The convention in Ch 13 is to use "right-handed neutrinos" when they are Dirac and "sterile" when they are Majorana or otherwise decoupled from the weak current. The draft uses "sterile" consistently, which is correct for the Class B case. ✓

---

## The "But Why?" Reader

Asks why the framework predicts *these* dark-matter candidates and not others, why the boson masses are what they are, etc.

### IMPORTANT

**(BW1)** §14.2 lists four dark-matter candidate classes but does not say *why* four and not five (or three). The reader asks: is this an exhaustive classification? Are there sectors of the 6D manifold I haven't mentioned? What about the *bulk* modes of the membrane that are neither ξ-ladder bound states nor boundary ripples — aren't those a fifth candidate class?

**Response:** Good question. The bulk membrane modes are *not* a fifth class because they are what gives rise to the Standard Model in Ch 10–11; they are not dark. The ξ-ladder continuum states (Class C) are the only "bulk" sector that decouples. The η-boundary ripples (Class B) are the only boundary sector. The KK tower (Class A) is the only tower. The radion (Class D) is the only modulus. I believe the four-class enumeration is *exhaustive given the current zone architecture*, and I should say so. **Fix for FINAL:** add one sentence at the end of the §14.2 four-class introduction: "These four classes exhaust the sectors of the current 6D Lagrangian that do not directly couple to the Ch 10–11 charged-current vertices; any fifth class would require extending the architecture." This also reinforces Result 14.1's structural claim.

**(BW2)** Why does the framework predict *exactly* three fermion generations? §14.4 Prediction 14.2 states the number but not the reason — it cites Ch 10 §10.3 for the structure, but the chapter is a capstone and should remind the reader in one sentence.

**Fix for FINAL:** add to Prediction 14.2 a one-sentence reminder: "The three-generation count is the eigenvalue count of the Vol 1 Ch 5 double-well potential — three normalizable bound states, no more, no less, because the well has exactly that depth."

### MINOR

**(BW3)** The Skeptic's frame in §14.0 is effective, but I would like one sentence on why the Skeptic's question is the *right* question for a foundational framework. The draft says the Skeptic's question is "the only question that matters for a framework of this kind" but does not unpack why. One sentence: "A framework that cannot say something new is a framework that does not justify its additional machinery; a framework that can say something new but not testable is a framework that is not science." **Fix for FINAL:** optional, but would sharpen §14.0.

---

## The Writing Coach

Checks that the capstone closes the volume with appropriate weight and is not a dry list.

### IMPORTANT

**(WC1)** §14.5 (the falsification table) is the driest part of the chapter by necessity. The draft handles it reasonably by framing the table with an introductory and concluding paragraph. But the closing paragraph of §14.5 could do more. Currently it is three bullet-point observations (the sharpest knife is row 6, the most important existing tests are rows 1–5, the most uncomfortable obligation is row 14). This is informative but somewhat listlike. The reader has been through a dense chapter and deserves a more shapely landing at §14.5.

**Fix for FINAL:** rewrite the closing paragraph of §14.5 in prose, not in "if the Skeptic asks X" structure. Something like: "Fourteen rows. Half are already in the data and passed. Two are structural — they cannot be confirmed, only falsified. Five are genuine new-physics tests for the experimental community. One is an internal obligation the framework owes itself. The sharpest knife is the generation count: a fourth-generation particle at any mass, anywhere, at any collider, kills the framework in a single datum. The largest existing success is the boson-mass precision envelope, which the framework meets with zero free parameters in the boson sector. The largest existing discomfort is the top-quark decay-width gap, which the framework has not yet calculated itself out of. These three — knife, success, discomfort — frame the volume's experimental stance."

**(WC2)** §14.7 handoff is short but adequate. I would not extend it.

### MINOR

**(WC3)** The §14.0 opening paragraph is strong but runs long — nine sentences. The Skeptic's question lands well but the lead-up is dense. A small tightening would help. **Fix for FINAL:** optional, split the long paragraph into two.

**(WC4)** The chapter uses "the framework" roughly 80 times. Ch 13 uses it similarly. This is the Feynman-textbook voice and I do not object, but it is worth noting that a first-time reader of Vol 4 who opens at Ch 14 would benefit from a one-line reminder that "the framework" refers to Genesis Physics and the zone architecture of Vols 1–3. The epigraph plus §14.0 should make this clear, so this is not a required fix — just a note.

---

## The Student

Checks that the chapter is usable as a study reference, especially the falsification table.

### IMPORTANT

**(S1)** The problem set is good and exercises the right concepts (falsification thresholds, open problems, dark-matter signatures, baryogenesis). However, problem 14.5 asks the student to "estimate the nucleon-recoil cross-section from the framework's coupling structure — that is, one loop factor below the Z-boson coupling." The student does not have the Z-boson coupling to nucleons in a form they can use without consulting an external reference. **Fix for FINAL:** either give the Z-nucleon coupling as a hint in the problem, or rephrase to use the cross-section formula of (4.14.3) as the starting point.

**(S2)** Problem 14.7 asks the student to reproduce the 184-order-of-magnitude cosmological-constant mismatch, then estimate the required Z$_2$ cancellation precision. This is a good problem but the student needs to know what precision the Z$_2$ gives "naturally" (before the symmetry is softly broken). The draft does not address this in §14.3. **Fix for FINAL:** add to §14.3 one sentence: "A pure, unbroken Z$_2$ would cancel the loop energy exactly; the Z$_2$ in the framework is softly broken by the membrane boundary conditions, and the residual is what needs to be computed." This gives the student enough to attempt problem 14.7.

### MINOR

**(S3)** The §14.5 table is excellent as a study reference. I would use it directly for exam prep. No change needed.

**(S4)** The §14.6 research roadmap is useful as a "where could I do a PhD thesis in this framework?" document, but the student-facing value of it would improve if each RR item were tagged with whether it requires experimental, computational, or pure-theoretical work. This is a stretch request and not a blocker — leave as is in FINAL unless Jeff wants to add it.

---

## Consolidated fix list for FINAL

The following fixes will be applied in the FINAL pass.

| # | Source | Type | Fix |
|---|---|---|---|
| F1 | Skeptic BLOCKING | Substantive | Prediction 14.1 — tighten the 2% threshold with explicit joint-shift condition and two-sigma justification. |
| F2 | Skeptic IMPORTANT | Substantive | §14.2 Class A — acknowledge two-decade cross-section range comes from uncomputed η-boundary vertex; tie to RR-7/RR-8. |
| F3 | Skeptic IMPORTANT | Substantive | Result 14.1 — split into structural ("no new vertex") and approximate ("masses and cross-sections") parts. |
| F4 | Skeptic MINOR | Clarifying | Prediction 14.5 — add one sentence that the prediction is on the outcome of the NNLO calculation, not on whether it is performed. |
| F5 | Physicist IMPORTANT P1 | Verification | §14.2 (4.14.2) — soften citation of (4.6.17) to "Ch 6" and verify prefactor. |
| F6 | Physicist IMPORTANT P2 | Substantive | §14.2 Class A — rewrite stability argument. Cite Appelquist-Cheng-Dobrescu or zone-QFT analogue. Downgrade to "speculative candidate" if the mechanism cannot be named cleanly. |
| F7 | Physicist IMPORTANT P3 | Clarifying | §14.3 — add field-content caveat to loop vacuum energy discussion. |
| F8 | Physicist MINOR P5 | Clarifying | §14.2 Class D — one-line Casimir → meV explanation. |
| F9 | CA IMPORTANT CA1 | Citation | RR-12 — remove "§14.2 above" clause. |
| F10 | CA IMPORTANT CA4 | Citation | §14.1 — drop specific equation number "(2.9.31)"; cite Vol 2 Ch 9 §9.4 only. |
| F11 | CA IMPORTANT CA5 | Citation | §14.2 — drop specific equation number "(4.6.17)"; cite Ch 6 KK tower section. |
| F12 | But Why BW1 | Substantive | §14.2 — add "exhaustiveness" sentence at end of four-class introduction. |
| F13 | But Why BW2 | Clarifying | §14.4 Prediction 14.2 — one-sentence reminder of three-bound-state eigenvalue count. |
| F14 | But Why BW3 | Clarifying (optional) | §14.0 — one-sentence unpacking of why the Skeptic's question is the right question. Apply. |
| F15 | Writing Coach WC1 | Substantive | §14.5 closing paragraph — rewrite in prose, not in "if the Skeptic asks X" structure. |
| F16 | Writing Coach WC3 | Style (optional) | §14.0 — split long opening paragraph in two. Apply. |
| F17 | Student S1 | Clarifying | Problem 14.5 — rephrase to use (4.14.3) as starting point. |
| F18 | Student S2 | Substantive | §14.3 — add Z$_2$ softly-broken sentence for problem 14.7 support. |
| F19 | Self-Review #2 | Clarifying | §14.2 Class D — replace "EP-SENSE" with "resonant-mass detector programs". |
| F20 | Self-Review #4 | Clarifying | §14.4 Prediction 14.3 — widen charm branching-ratio uncertainty language. |

Twenty fixes. One is substantive and blocks acceptance (F1). Four others are substantive but not blocking (F2, F3, F6, F15, F18). The rest are clarifying or cosmetic. All will be applied in the FINAL pass.

**Overall verdict:** The chapter passes review conditional on the twenty fixes above. The Skeptic signs off on the blocking item (F1) and the three important items (F2, F3, F4). The Physicist signs off on P1–P5. The Consistency Auditor signs off on the citation fixes. The "But Why?" Reader signs off on the exhaustiveness and generation-count additions. The Writing Coach signs off on the §14.5 rewrite. The Student signs off on the problem-set clarifications.

Ready for FINAL pass.
