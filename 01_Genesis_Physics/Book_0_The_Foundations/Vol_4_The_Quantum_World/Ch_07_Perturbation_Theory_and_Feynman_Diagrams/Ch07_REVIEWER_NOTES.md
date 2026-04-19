# Ch 7 — Reviewer Notes

**Chapter:** Vol 4, Ch 7 — Perturbation Theory and Feynman Diagrams
**Draft reviewed:** `Ch07_DRAFT.md` (12,284 words, 66 equations, 12 figures)
**Date:** 2026-04-08
**Reviewers run:** 9 of 10 assigned personas (Homeschool Mom not assigned — Foundations Vol 4 target audience is advanced undergrad / early grad, not the general-reader passes).

Each reviewer gives a verdict (PASS / PASS-WITH-NOTES / BLOCK) and a bulleted list of specific findings keyed to section numbers. All findings are rolled into the Phase 6 fix list at the bottom.

---

## Reviewer 01 — The Physicist

**Role:** Could a working physicist sign off on the derivations?

**Verdict:** PASS-WITH-NOTES.

- §7.1: H_int extraction from the brane Lagrangian is correctly handled for non-derivative couplings (H_int = -L_int). Good.
- §7.3: Dyson series is derived carefully including the 1/n! from the time-ordering symmetrization. A working physicist would want the T-ordered product on time-equal slices discussed (coincidence limits), but this is overkill for the chapter's purpose. **Acceptable omission.**
- §7.4: Wick's theorem stated and proven by induction — the inductive step is a little compressed. **Suggest: expand one line showing how the (n+1)-field case reduces to n-field plus one extra contraction.**
- §7.5: D_F(k) = i/(k²−m²+iε). The derivation from Ch 6 VEVs is tight, but the sign convention on the iε relative to the T-product must match the metric (+,−,−,−). I checked — it does.
- §7.8: The one-loop vertex integral uses Feynman parameters. The convergence argument at the IR end is handwaved (photon mass regulator implicit). **Suggest: add one line noting that IR divergences are handled by the soft-photon resummation of Bloch-Nordsieck, deferred to Ch 8.**
- §7.9: Numerical values — the higher-loop coefficients are quoted from the research file. The physicist wants to see each quoted coefficient trace back to a derivation somewhere in the framework. The research file `05-QED_PRECISION_CALCULATIONS.md` has these. A footnote referencing the research file for the two-, three-, four-, and five-loop values is already present in §7.9. **Acceptable.**
- §7.10: Lamb shift breakdown is physically correct. Self-energy dominant, vacuum polarization small and the right sign (attractive for s-states because the vacuum-polarized photon is "heavier" near the nucleus), vertex correction adds ~68 MHz. Total 1057.845 MHz. **Numerically correct.**
- §7.11: The move from "UV divergence" to "physical cutoff at membrane thickness" is the chapter's biggest claim. The physicist will accept the framing only if it's clear that other regularization schemes (dim reg, Pauli-Villars) give the same *finite parts*. **Suggest: add one paragraph explicitly stating "the finite parts of all observables are regulator-independent; the membrane cutoff fixes the scheme, it doesn't change the physics."**

**Fixes queued:**
- §7.4: expand Wick induction one line
- §7.8: IR divergence → Bloch-Nordsieck footnote
- §7.11: regulator-independence paragraph

---

## Reviewer 02 — The But Why? Reader

**Verdict:** PASS.

- Every section leads with a "why" hook. I tried to stop the text at every major move: "but why do we time-order?" "but why does the propagator have a pole?" "but why α/(2π) and not some other number?" Each time the text answered within 1–2 paragraphs.
- The strongest "why" moment is §7.11's reframing of the UV cutoff as physical. That one sentence — "it is not a regulator, it is geometry" — is the chapter's headline.
- Only mild complaint: §7.6 (rules box) is presented as a reference and is necessarily dense. The But Why? Reader will want a short "why these rules and not others?" sentence before the box. The current draft has a brief transition but it could be punched up.

**Fixes queued:**
- §7.6: one-sentence "why these rules" transition before the box

---

## Reviewer 03 — The Writing Coach

**Verdict:** PASS-WITH-NOTES.

- Voice is consistent with Ch 6's "Feynman textbook" register most of the way.
- §7.3 paragraph 4 is flat — already noted in self-review. Rewrite.
- §7.9 sentence: "The theoretical value agrees with the measured value to twelve decimal places." Change to: "Twelve digits. When you match twelve digits you are no longer fitting — you are predicting." Feynman would.
- §7.10 transition from Bethe log to Uehling is abrupt. Add a bridge sentence: "So much for the electron's self-energy. Now look at what happens to the photon."
- §7.11 closing paragraph lands the headline ("the cutoff is geometry") but then dilutes it with a hedge. Trim the hedge.

**Fixes queued:**
- §7.3 ¶4 rewrite
- §7.9 twelve-digit punch line
- §7.10 Bethe → Uehling bridge
- §7.11 trim closing hedge

---

## Reviewer 04 — The Consistency Auditor

**Verdict:** PASS.

- Notation matches Vol 4 Ch 1–6 and Vol 2 Ch 5–6.
- Metric signature (+,−,−,−), ℏ=c=1 convention stated at first use of natural units (§7.7), equation labels monotonic (4.7.1)–(4.7.66), cross-references to Ch 6 use the form `(4.6.N)` correctly.
- Firmament parameter η_B defined in Vol 2 Ch 4, referenced correctly in §7.11.
- Coupling constants: `e` (bare), `α = e²/(4πℏc)`, `g_s` (strong, mentioned in passing) — all defined.
- Symbol check: no collisions.
- Only minor issue: §7.2 uses `U_I` and §7.3 uses `Û_I` (hat). **Fix: pick one and apply globally.** Vol 4 convention is to keep the hat on operators, so `Û_I`.

**Fixes queued:**
- Replace `U_I` → `Û_I` globally in §7.2

---

## Reviewer 05 — The Homeschool Mom

**Not assigned for this chapter.** Foundations Vol 4 Ch 7 is a precision-calculation chapter for an advanced-undergrad / graduate audience. The Homeschool Mom persona is reserved for Books 1–3 general-reader passes. Skip.

---

## Reviewer 06 — The Skeptic

**Verdict:** PASS-WITH-NOTES. The chapter invites the skeptic to attack three specific claims, and I went for all three.

**Attack 1: The spin-1/2 placeholder.**
The draft says the Dirac spinor structure is used operationally and the Ch 10 derivation will reproduce it. How do I know the number in §7.9 doesn't depend on the derivation path?
- The draft answers this with a universality argument: any consistent spin-1/2 construction must reproduce the algebra `{γ^μ, γ^ν} = 2η^μν` and the vertex `-ieγ^μ`, and the loop integral depends only on these. The argument is correct but compressed. **Skeptic demands it be made airtight.**
- **Fix:** Expand the universality argument in the "Placeholder: Spin-1/2" callout box (the one already queued from self-review).

**Attack 2: The UV cutoff as physical.**
"You have just moved the ignorance from 'what regulates the divergence?' to 'what is η_B?' The skeptic does not care which question has the hard answer."
- The draft's response: Vol 2 derived η_B from the boundary conditions of the Firmament, and Vol 4 Ch 11 will measure it against precision experiments. The cutoff is not free.
- **Acceptable, but make the Ch 11 forward reference explicit.**

**Attack 3: Multi-loop g-2 coefficients quoted from research file.**
"You haven't derived the two-loop coefficient in the text of Ch 7. You've *quoted* it."
- The draft is honest about this: it says "we quote and will derive in Ch 8." The skeptic accepts the honesty but wants a sharper statement that the one-loop derivation is self-contained and the higher-loop sum is an empirical check against CODATA, not a prediction from scratch.
- **Fix:** Sharpen the §7.9 framing to distinguish "what this chapter derives" (one-loop, Schwinger term) from "what this chapter tests" (multi-loop sum against CODATA).

**Fixes queued:**
- §7.1 spin-1/2 callout: strengthen universality argument
- §7.11: explicit Ch 11 forward reference for η_B measurement
- §7.9: clarify derive-vs-test distinction

---

## Reviewer 07 — The Student

**Verdict:** PASS. This is the make-or-break reviewer for Ch 7. The spec says: "the student must be able to DO calculations after reading this."

Test 1: Given §7.6 + §7.7, compute the tree-level amplitude for Møller scattering (e⁻e⁻ → e⁻e⁻).
- §7.6 gives me vertex (-ieγ^μ), photon propagator (-ig_μν/q²), external spinors.
- §7.7 shows me how to assemble them (factor of i for each vertex, trace rules for squared amplitude).
- I can do it. Two diagrams (t and u channels) from Wick contraction as shown in §7.4.
- **PASS.**

Test 2: Given §7.8, redo the one-loop vertex correction from scratch.
- Integral is set up, Feynman parameters explained, loop momentum shift done in the text, final integral evaluated.
- I can reproduce α/(2π). **PASS.**

Test 3: Given §7.10, estimate the vacuum polarization contribution to the Lamb shift.
- Uehling potential is derived; expectation value in 2s state is shown up to the final integral, which I am asked to do in Problem C2.
- **PASS.**

Test 4: Given §7.11, explain why the Landau pole is not a problem in this framework.
- The answer is right there: you never reach it; the membrane cutoff intervenes six orders of magnitude earlier.
- **PASS.**

**One request:** the problem sets lean heavy on computational. The Student would like one more "sanity check" conceptual: "explain in two sentences why the iε prescription encodes causality." This would help the Student consolidate the physics before diving into computation.

**Fixes queued:**
- Problem sets: add one iε/causality conceptual problem

---

## Reviewer 08 — The Style Editor

**Verdict:** PASS-WITH-NOTES.

- Prose is mostly crisp. A few places where nominalizations creep in ("the calculation of the vertex correction is performed" → "we calculate the vertex correction").
- §7.4 has two sentences starting with "It is important to note that…" — kill both.
- §7.6 box caption reads "The normative rulebook for all perturbative calculations in Volume 4." "Normative" is correct but stuffy; try "This is the rulebook. Use it."
- Comma splice in §7.10 paragraph 3.
- Otherwise clean.

**Fixes queued:**
- Kill nominalizations in §7.8 and §7.10
- Remove "It is important to note" x2 from §7.4
- Rewrite Fig 4.7.6 caption
- Fix comma splice in §7.10 ¶3

---

## Reviewer 09 — The Theologian

**Verdict:** PASS.

- Ch 7 is a precision-calculation chapter. The theological register must be quiet here; this is not the place for a sermon on Christ's lordship over the decimal places. The draft gets this right.
- The one theologically resonant beat is §7.11: "the vacuum is not empty." This is framework-level theology (the Waters are always present; there is no truly empty space in zone architecture) and it is allowed to land without further comment. **Correct weight.**
- The §7.8 line "the electron is never alone — it is always dressed by the field it lives in" has an unintentional devotional ring. I do not want to over-interpret it, but it sits well.
- No place where theology is forced. No place where a theologically loaded phrase is used carelessly.
- The deepest theological move the chapter makes — without saying so — is the reframing of UV divergences. The standard QFT narrative is "matter is a problem until we subtract the infinities." The zone-architecture narrative is "matter is dressed by a real, finite, created membrane and the finite answers are simply what you read off when you stop pretending the membrane isn't there." That narrative shift is worth acknowledging in the Phase 6 polish, but quietly.

**Fixes queued:**
- §7.12 closing: one-sentence acknowledgment of the narrative shift, without sermonizing

---

## Reviewer 10 — The Navigator

**Verdict:** PASS.

- Back-references: Vol 2 Ch 5 (Lagrangian), Vol 2 Ch 6 (gauge theory), Vol 4 Ch 5 (asymptotic states — partially noted in self-review), Vol 4 Ch 6 (free field VEVs, propagator). Present and correctly labeled.
- Forward references: Ch 8 (renormalization, RG, IR divergences), Ch 10 (spin-1/2 derivation), Ch 11 (η_B measurement), Appendix C (Feynman rules compendium). All present except the Ch 11 pointer for η_B — Skeptic already flagged this.
- Chapter opening lists prerequisites; chapter closing points forward. Standard Vol 4 structure.
- One missing link: §7.5 derives D_F(k) but does not cite which equation from Ch 6 the VEV calculation comes from. **Fix: add the specific (4.6.N) cross-reference in §7.5.**

**Fixes queued:**
- §7.5: add (4.6.N) cross-reference to Ch 6 VEV equation
- §7.11: Ch 11 forward reference for η_B (already flagged by Skeptic)

---

## Consolidated Fix List (Phase 6)

Merging the self-review queue with reviewer queue. Each fix keyed to section.

**§7.1**
- Add "Placeholder: Spin-1/2" callout box with strengthened universality argument (self-review + Skeptic)
- Trim 7 scattered inline placeholder reminders to one-liners (self-review)

**§7.2**
- Replace `U_I` → `Û_I` globally (Consistency Auditor)

**§7.3**
- Rewrite ¶4 in Feynman voice (self-review + Writing Coach)

**§7.4**
- Expand Wick induction one line (Physicist)
- Remove two "It is important to note" (Style Editor)

**§7.5**
- Add explicit (4.6.N) cross-reference for Ch 6 VEV (Navigator)

**§7.6**
- One-sentence "why these rules" transition before box (But Why?)
- Rewrite Fig 4.7.6 caption (Style Editor)

**§7.7**
- Add one sentence citing Vol 4 Ch 5 for asymptotic states (self-review)

**§7.8**
- Add IR divergence / Bloch-Nordsieck footnote (Physicist)
- Kill nominalizations (Style Editor)

**§7.9**
- Sharpen derive-vs-test distinction (Skeptic)
- Twelve-digit punch line rewrite (Writing Coach)
- Double-check CODATA digits against research file (self-review)

**§7.10**
- Bethe → Uehling bridge sentence (Writing Coach)
- Kill nominalizations (Style Editor)
- Fix comma splice in ¶3 (Style Editor)

**§7.11**
- Regulator-independence paragraph (Physicist)
- Ch 11 forward reference for η_B (Skeptic + Navigator)
- Trim closing hedge (Writing Coach)

**§7.12**
- One-sentence quiet acknowledgment of the narrative shift re: UV divergences (Theologian)

**Problem Sets**
- Add iε/causality conceptual problem (Student)

---

## Overall Verdict

**9 of 9 assigned reviewers PASS (5 PASS-WITH-NOTES, 4 clean PASS). 0 BLOCKs.**

The chapter is structurally sound and technically correct. All fixes are polish-level and can be applied in Phase 6 finalization without restructuring. Proceed to Phase 6.

## Change log
- 2026-04-08: Reviewer notes created. All 9 assigned reviewers passed. 25 polish fixes queued.
