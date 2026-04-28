# The Seven Concerns — Detailed Rubric

This rubric translates Jeff Raymond's seven review concerns into scoreable criteria. Every reviewer must tag every finding with at least one concern (C1–C7). Reviewers are free to raise findings outside their primary concern.

---

## C1 — Biblical-First Traceability

**Jeff's rule (verbatim intent):**
> Every main claim must trace to a biblical truth. Every subsequent claim must trace to a parent claim or to a biblical truth. No orphans. No mainstream-physics-first framings dressed up in biblical clothes.

### Pass criteria
- Every **main claim** (claim introduced without a cited parent) carries a load-bearing biblical anchor: specific verse, Hebrew etymology that actually constrains the physics, or a Genesis-1 architectural feature previously established as physical structure.
- Every **subsequent claim** names its parent explicitly — either a prior claim (by ID or clear pointer) or a biblical anchor.
- The biblical anchor is doing derivational work. Test: if the verse were deleted, the argument would no longer stand on its cited basis.
- Where the claim extrapolates beyond explicit Scripture, the chapter says so openly.

### Automatic FAIL
- A main claim with no biblical anchor
- A verse used decoratively (delete it, argument unchanged)
- A retrofit trace (prediction matches mainstream physics; biblical anchor asserted but did no derivational work)
- A subsequent claim with no named parent
- Hebrew etymology asserted to mean more than lexicons support

### Primary reviewer: REVIEWER-11
### Supporting: REVIEWER-02 (catches orphan statements), REVIEWER-09 (catches bad exegesis that would mask as a good anchor)

---

## C2 — Cross-Book / Cross-Volume Continuity

**Principle:** ideas do not pop out of nowhere. A concept introduced in Vol 3 must trace to something established in Vol 1 or Vol 2 (or explicitly introduced as new). A concept in a novel or game pillar that claims physics grounding must point to a specific Book 0 claim.

### Pass criteria
- Every concept used in a chapter has a clearly locatable introduction, either earlier in this volume, an earlier volume, or an explicit first-introduction statement.
- All cross-volume references name the volume, chapter, and (where applicable) equation or claim ID.
- No "as we will show later" that is load-bearing for the current argument.
- Vocabulary stable across volumes: the same concept is not called three different names.

### Automatic FAIL
- A concept used as if established when it has not been introduced anywhere
- A cross-volume reference pointing at content that does not exist
- Terminology drift: a concept renamed silently between volumes

### Primary reviewer: REVIEWER-10 (Navigator)
### Supporting: REVIEWER-04 (Consistency Auditor), REVIEWER-02

---

## C3 — No Unanswered "But Why?"

**Principle:** a student of this framework should never have to ask "but why?" without finding an answer in the text.

### Pass criteria
- Every major concept has its reason given before or alongside its introduction.
- No "it is well-known that..." or "it can be shown that..." left unexplained.
- Where the framework doesn't yet have an answer, the chapter says so — "this is an open problem" is always acceptable; silent punting is not.
- Physical intuition precedes formal derivation.
- Visuals exist wherever a reader would reach for a napkin to draw.

### Automatic FAIL
- A physics law presented as "that's just how it is" with no reason
- A derivation that skips a step with "the reader can verify"
- A concept whose "why" is promised for a later chapter but is load-bearing now
- Unlabeled open problems

### Primary reviewer: REVIEWER-02
### Supporting: REVIEWER-07 (Student), REVIEWER-10

---

## C4 — Self-Consistency

**Principle:** no contradictions across chapters or volumes. Same constants, same terminology, same mechanisms, same equations.

### Pass criteria
- Numerical constants identical across chapters (cross-check Reference/Symbol_and_Constants.md).
- Equation numbering consistent (Vol.Ch.Eq format for Book 0).
- Zone, firmament, waters terminology used identically.
- Causal mechanisms not quietly rewritten chapter to chapter.
- Scripture citations point to the same translation consistently.

### Automatic FAIL
- Two chapters give different values for the same constant
- A mechanism described one way in Ch 5 and differently in Ch 8 with no bridging note
- Equation numbering collisions or gaps
- Terminology that shifts silently between chapters

### Primary reviewer: REVIEWER-04
### Supporting: REVIEWER-01, REVIEWER-10

---

## C5 — Mainstream-Physics Derivation Honesty

**Principle:** where the framework claims to derive or recover a mainstream result, the derivation must be clean. No cheating. Honest acknowledgment of limiting cases, dimensional analysis, falsifiability.

### Pass criteria
- Every mainstream-result "recovery" shows the actual derivation, including the limit or approximation that produces the match.
- Dimensions check on every equation.
- Limiting cases explicit: where does this reduce to Newtonian? To GR? To QM?
- Falsifiability: what observation would distinguish this framework from the mainstream?
- Numerical predictions disclose their inputs and assumptions.
- No circular reasoning (framework parameters tuned to produce the result being "predicted").

### Automatic FAIL
- Claim of recovering a mainstream result without showing the derivation
- Dimensional errors
- Tuned-to-fit prediction presented as a derivation
- Circular reasoning
- Unfalsifiable claims presented as confirmed
- Cherry-picked data presented without acknowledgment of what's left out

### Primary reviewer: REVIEWER-01 (Physicist), REVIEWER-06 (Skeptic)
### Supporting: REVIEWER-07

---

## C6 — NYT-Bestseller Readability and Craft

**Principle:** the writing should be good enough that a NYT trade-nonfiction editor would want to acquire it. Voice, flow, hook, pacing, figure quality, paragraph structure.

### Pass criteria
- First page earns the second page. Opening hook works.
- Voice consistent throughout (Feynman-style conversational rigor for Book 0 per WRITING_PROMPT).
- Paragraphs have structure — no wall-of-text that should be broken up.
- Active voice preferred; passive voice only where appropriate.
- Figures illuminate rather than decorate.
- Pacing: dense math balanced with intuition.
- No jargon used before it's defined.
- Every chapter ends with forward momentum.

### Automatic FAIL
- A chapter whose first page does not earn the second
- Jargon stacked on jargon with no accessible on-ramp
- Paragraphs that dump equations with no prose scaffolding
- Voice shifts mid-chapter
- Figures that don't actually help understanding

### Primary reviewer: REVIEWER-03 (Writing Coach)
### Supporting: REVIEWER-05 (Homeschool Mom — for broad-audience accessibility), REVIEWER-08 (Style Editor — for mechanics)

---

## C7 — Publisher / Production Readiness

**Principle:** the manuscript must be shippable. Front matter, back matter, TOC, index, cross-references, permissions, metadata, positioning, figures.

### Pass criteria
- All front/back matter present and correct
- TOC accurate; list of figures and tables complete
- Every cross-reference resolves
- Every non-original figure has a credit line / permission on file
- Scripture translation permission acknowledged on copyright page
- Index valid and hierarchical
- Back-cover blurb writable from the manuscript
- Three defensible comps identifiable
- BISAC codes and ISBN block correct
- Figures print-ready; e-book graceful degradation confirmed
- Accessibility (alt-text, heading semantics)

### Automatic FAIL
- Broken internal cross-reference
- Missing scripture-translation permission acknowledgment
- TOC that mis-states chapter titles
- No index (for a textbook)
- Back-cover blurb you can't write from the manuscript
- Author bio that doesn't establish credibility for this book

### Primary reviewer: REVIEWER-12 (Acquisitions & Production Editor)
### Supporting: REVIEWER-08

---

## Concern-by-severity matrix

A finding in any concern can be any severity. Use this guide to keep severity calibrated:

| Severity | Meaning | Examples |
|---|---|---|
| **P0 Blocker** | Ship-stopping red flag | Decorative verse pretending to derive (C1), broken cross-ref (C7), contradictory constants (C4), fabricated result (C5) |
| **P1 Critical** | Must-fix before shipping | Weak biblical anchor (C1), unclear derivation step (C5), chapter hook that doesn't land (C6), missing index (C7) |
| **P2 Important** | Should-fix for quality | Minor notation drift (C4), prose that dumps without scaffolding (C6), weak comp title (C7) |
| **P3 Polish** | Nice-to-have | Word choice, rhythm, figure aesthetics |

Every per-chapter report must show counts across this matrix. The chapter rollup combines them.
