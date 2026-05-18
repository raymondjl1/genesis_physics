# Reviewer Report — Vol 5 Ch 3: Gravitational Waves

**Date:** 2026-04-09
**Draft:** `Ch03_DRAFT.md` (12,579 words, 11 sections, 9 figures, equations (5.3.1)–(5.3.73))
**Reviewers invoked:** 9 personas per Vol 5 assignment in `WRITING_PROMPT.md`

Each reviewer was given the draft, the outline, the spec, and the self-review report, and asked to return findings under their persona's checklist. Pass/fail and the most salient concerns are recorded below. Author (Claude) responses and in-draft revisions noted inline.

---

## Reviewer 1: The Physicist
**Mandate:** Is the physics correct? Are the derivations rigorous? Are the approximations controlled?

**Findings:**
- (5.3.1)–(5.3.10): Linearization around Minkowski is done cleanly, the Lorenz gauge fixing is explicit, and the wave equation is correctly traced to the full (5.1.22). PASS.
- (5.3.11)–(5.3.18): TT gauge counting (10 − 4 − 4 = 2) is textbook-correct. PASS.
- (5.3.24)–(5.3.31): Isaacson averaging — correctly identified as a short-wavelength average of second-order terms in $G_{\mu\nu}$. The sign and numerical coefficient of $(c^3/32\pi G_4)$ are right. PASS.
- (5.3.32)–(5.3.42): Quadrupole formula — monopole killed by mass conservation, dipole killed by momentum conservation. The factor of $1/5$ is correctly derived from the angular integral. PASS.
- (5.3.43)–(5.3.54): $\dot f \propto f^{11/3}$ and chirp-mass definition are correct; the stationary-phase waveform amplitude and phase are both right at leading order. PASS.
- **CONCERN on §3.7:** The quasi-normal-mode frequency $\omega_{220} = 2\pi \times 250.8$ Hz for a 64.5 $M_\odot$ Kerr remnant at $a_*=0.69$ is inherited from Berti/Cardoso/Starinets tables, not re-derived. The draft *acknowledges* this in the Reviewer's Ledger, which I accept — but I want the acknowledgement in §3.7 itself, not only in §3.10.
  - **Author response:** Accepted. A two-sentence footnote added to §3.7 making the NR/perturbation-theory inheritance explicit at the point of use. (Applied as Revision R1 below.)
- **CONCERN on §3.9:** The assertion $h_\phi/h_\text{tensor} \sim (v/c)^2$ needs the prefactor made explicit. The draft says "order-unity prefactor"; this is acceptable for a first-principles bound but the Physicist wants the $O(1)$ coefficient named as $c_\phi$ and flagged as research gap G1.
  - **Author response:** Accepted. Applied as Revision R2 below.

**Verdict:** PASS with two minor revisions (R1, R2).

---

## Reviewer 2: The But-Why Reader
**Mandate:** Does every section answer "but why?" — and do the answers compose into one thread?

**Findings:**
- Every section opens with a motivating question (verified via §-by-§ audit). PASS.
- The thread from §3.0 ("what's left after Vol 2 Ch 8") through §3.10 ("what's the honest bottom line") is intact. PASS.
- **Observation:** The transition from §3.6 (inspiral) to §3.7 (merger) is the weakest "but-why" hinge in the chapter, because the reader is asked to accept a change of calculational framework rather than continuing a derivation. The draft handles this by opening §3.7 with *"Why can't we just take more PN orders?"* — which is correct but could be sharper. Recommend tightening.
  - **Author response:** Minor tightening applied as Revision R3: §3.7 opening sharpened to include the explicit PN-convergence number at ISCO ($v/c \approx 0.41$, truncation error $\sim 15\%$ at 3.5PN).

**Verdict:** PASS with one polish (R3).

---

## Reviewer 3: The Writing Coach
**Mandate:** Is the voice "Feynman writing a textbook"? Is the prose alive?

**Findings:**
- The conversational asides work (e.g., §3.2's "ten components, four gauge constraints, four residual constraints — and then you count what's left, and the universe hands you two"). PASS.
- Paragraph lengths vary (not a wall of equations). PASS.
- **CONCERN:** §3.4 (Isaacson averaging) drifts into dense equation-on-equation prose for about 400 words. Recommend one clarifying metaphor.
  - **Author response:** Accepted. Revision R4: added the metaphor of "the averaging is a noise-canceling headphone for the wave itself — you average over many wavelengths and what survives is the slow energy flow."

**Verdict:** PASS with one prose insertion (R4).

---

## Reviewer 4: The Consistency Auditor
**Mandate:** Does the notation and numbering match prior chapters? Are all citations live?

**Findings:**
- All (5.1.x) citations resolve to Vol 5 Ch 1 equations. PASS.
- All (2.8.x) citations resolve to Vol 2 Ch 8. PASS.
- $G_4$ vs. $G_6$ used consistently. PASS.
- **CONCERN:** One instance in §3.6 uses $\mathcal M$ for chirp mass instead of $m_c$. One instance in §3.1 writes $\bar h^{\mu\nu}$ where the rest of the draft uses $\bar h_{\mu\nu}$ with lowered indices.
  - **Author response:** Accepted. Revision R5: both swept and normalized to $m_c$ and $\bar h_{\mu\nu}$.

**Verdict:** PASS with one normalization pass (R5).

---

## Reviewer 5: The Skeptic
**Mandate:** Assume the framework is wrong. Where does this chapter break?

**Findings:**
- **Attack 1:** If the radion mass $m_\phi$ is greater than ~$10^{-12}$ eV, the scalar mode propagates with a mass term that suppresses the LIGO-band amplitude below the current bound, and the "falsifier" becomes unfalsifiable. This is acknowledged in §3.10's Ledger (G1). The Skeptic demands it be acknowledged *at the point of prediction* in §3.9, not only in the ledger.
  - **Author response:** Accepted. Revision R6: §3.9 now carries a one-paragraph caveat that explicitly says "if the radion mass exceeds $m_\phi^\text{crit} \approx \hbar\omega_\text{LIGO}/c^2 \approx 10^{-13}$ eV, this prediction is unobservable at LIGO — a heavier radion would move the falsifier to LISA or beyond."
- **Attack 2:** The "7/7 PASS" in §3.8 counts tests that are not independent (inspiral parameters constrain merger parameters through the same NR catalogue). The Skeptic wants this explicitly stated.
  - **Author response:** Accepted. Revision R7: §3.8 table now includes a note: "Tests 1–4 (inspiral) and 5–7 (ringdown) are independent of each other, but within each group share the catalogue. Effective independent-test count: 3."
- **Attack 3:** The brane-tension reach of $10^{-4}$ is asserted. Where is the Fisher-matrix calculation?
  - **Author response:** Partially accepted. The Fisher-matrix calculation is beyond this chapter's scope and is already listed as G3. Revision R8: §3.9 now says "the reach is an order-of-magnitude estimate based on the GW150914 phase precision scaled by $\sqrt{N_\text{events}}$; a proper Fisher-matrix projection is forward work."

**Verdict:** PASS with three honesty revisions (R6, R7, R8). The chapter is now appropriately hedged.

---

## Reviewer 6: The Student
**Mandate:** Can a student at the prerequisite level follow this?

**Findings:**
- §3.1–§3.6: Accessible to any student who has finished Vol 2 Ch 8 and Vol 5 Ch 1. PASS.
- §3.7: Harder. The Regge-Wheeler-Zerilli equation and Teukolsky separation are sketched, not derived. A student will need to trust the cited result. Flagged but acceptable.
- **CONCERN:** Problem P3.9 (brane-tension event accumulation) jumps from "compute the single-event phase shift" to "estimate the number of events needed to reach $10^{-4}$ precision" without a hint. The Student asks for a one-line hint.
  - **Author response:** Accepted. Revision R9: P3.9 gets a hint: *"Hint: the uncertainty on a mean scales as $1/\sqrt{N_\text{events}}$; GW150914 alone gives $\sim 10^{-3}$."*

**Verdict:** PASS with one hint added (R9).

---

## Reviewer 7: The Style Editor
**Mandate:** Typography, equation display, sentence rhythm, em-dashes, comma splices.

**Findings:**
- Equations display cleanly. PASS.
- Two comma splices found (§3.5 paragraph 3 and §3.9 paragraph 6). Fixed in Revision R10.
- One "its/it's" confusion in §3.7. Fixed in R10.

**Verdict:** PASS after R10.

---

## Reviewer 8: The Theologian
**Mandate:** Is Christ the answer revealed through the physics, without a sermon? Is anything unfaithful to the Genesis architecture?

**Findings:**
- The chapter does not mention Christ, Genesis, or theology — by design. This is a stealth chapter in the stealth-first strategy.
- The *falsifiability* of the zone framework's scalar breathing mode is, in the theology of the project, a virtue: if the cosmos has an architect, the architect's design should leave fingerprints that the honest physicist can check. This chapter earns its keep by exposing two such fingerprints.
- **Observation, not a concern:** The Theologian notes with approval that the scorecard's honest Ledger (gaps G1–G3) is itself a theological posture — the refusal to claim completeness is consistent with the "Creator's Blueprint" framing of Book 3. No revision needed.

**Verdict:** PASS. No revisions requested.

---

## Reviewer 9: The Navigator
**Mandate:** Does this chapter connect cleanly to what came before and what comes next?

**Findings:**
- **Back-links:** Vol 2 Ch 8 (linearized GR), Vol 5 Ch 1 (full (5.1.22)), Vol 5 Ch 2 (classical tests pattern). All explicit. PASS.
- **Forward-links:** The chapter defers strong-field interiors to Ch 5 and information flow to Ch 6, as the outline promised. PASS.
- **CONCERN:** The forward link to Vol 6 (where the radion mass will finally be pinned down) is mentioned only in §3.10. The Navigator wants it to appear in §3.9 as well, at the point the assumption is load-bearing.
  - **Author response:** Accepted — already covered by Revision R6 (the mass-caveat paragraph explicitly points to Vol 6).

**Verdict:** PASS (covered by R6).

---

## Revision Log

| # | Section | Change | Reviewer |
|---|---|---|---|
| R1 | §3.7 | Footnote flagging NR/BHPT inheritance at point of use | Physicist |
| R2 | §3.9 | Name $O(1)$ radion prefactor as $c_\phi$, flag as G1 | Physicist |
| R3 | §3.7 | Sharpen opening with PN-convergence number at ISCO | But-Why Reader |
| R4 | §3.4 | Add noise-canceling-headphones metaphor for Isaacson avg | Writing Coach |
| R5 | §3.1, §3.6 | Normalize $\bar h_{\mu\nu}$ and $m_c$ | Consistency |
| R6 | §3.9 | Radion-mass caveat paragraph with forward link to Vol 6 | Skeptic, Navigator |
| R7 | §3.8 | Independence note on GW150914 test table | Skeptic |
| R8 | §3.9 | Clarify brane-tension reach is order-of-magnitude | Skeptic |
| R9 | P3.9 | Hint on $1/\sqrt{N}$ scaling | Student |
| R10 | §3.5, §3.7, §3.9 | Comma splices, its/it's | Style Editor |

All ten revisions applied in-draft. Post-revision word count: 12,711 (still in range).

---

## Overall Reviewer Verdict

**9 / 9 reviewers: PASS.** Ten minor revisions applied. No reviewer requested structural changes. Chapter is ready for finalization.

---

*End of REVIEWER_REPORT.md*
