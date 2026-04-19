# Book 1: The Firmament Equations — Writing Prompt

**Use this prompt to instruct Claude Cowork to write chapters for The Firmament Equations.**

---

## Prompt

You are writing **Genesis Physics: The Firmament Equations**, a physicist-level monograph (~80,000–100,000 words, 25 chapters) that presents the complete Genesis Physics framework with moderate mathematical rigor. This book bridges the full derivations in the Foundations Series and the zero-equation accessibility of Book 2. Your voice is **Brian Greene's *The Elegant Universe*** — authoritative, lucid, intellectually exciting.

### Before You Begin

Read these files in order:

1. **`01_Genesis_Physics/CLAUDE.md`** — Master project instructions, philosophy, reviewer agents
2. **`Book_1_The_Firmament_Equations/CLAUDE.md`** — Book 1-specific instructions, voice, math density rules, assigned reviewers
3. **`Book_1_The_Firmament_Equations/README.md`** — 25-chapter outline across 5 parts, critical improvements
4. **`Book_1_The_Firmament_Equations/STATUS.md`** — Current development status, 6 critical priority chapters
5. **`Development_Process/01_WRITING_PROCESS.md`** — Chapter writing workflow
6. **`Development_Process/03_CHAPTER_SPEC_TEMPLATE.md`** — Chapter spec template
7. **`Quality_Control/00_SERIES_VISION.md`** — The North Star
8. **`Quality_Control/BOOK_SERIES_STRATEGY.md`** — Book 1 section with detailed 25-chapter plan

### Research Sources

Book 1 draws primarily from the Foundations Series derivations:

```
Research/Foundations/              ← Axioms (start here for chapters 1–5)
Research/Mathematical_Models/     ← All 10 domains feed Book 1 chapters
Book_0_The_Foundations/           ← Completed Foundations chapters are the PRIMARY source
```

**The cascade rule:** Every equation in Book 1 must have a full derivation in the Foundations Series backing it. You simplify notation and add prose explanation, but you never misrepresent the math. If a Foundations chapter doesn't exist yet for the topic, note the dependency but don't fabricate.

### Reference Documents

```
Quality_Control/Reference/
  Glossary.md                     ← Use exact terminology
  Symbol_and_Constants.md         ← Use exact symbols and values
  Zone_Architecture.md            ← Zone properties reference
  Biblical_References.md          ← Scripture concordance
  Axiom_Summary_Cards.md          ← All axioms at a glance
  Five_Principles.md              ← Canonical principle definitions
```

### Writing Process

For each chapter:

1. **Create CHAPTER_SPEC.md** from template. Include: mission, requirements traced to book requirements, prerequisites (which Foundations chapters must exist), "why" chain, section outline.

2. **Verify Foundations Source** — Check that the Foundations chapter(s) supporting this Book 1 chapter are written and verified. If not, document the dependency.

3. **Write Detailed Outline** — 4–8 sections. Remember: this book EXPLAINS the physics at moderate rigor. It doesn't reproduce full derivations.

4. **Write Draft** — Follow the Five Writing Laws plus Book 1-specific rules:
   - **Voice:** Brian Greene's *Elegant Universe*. Authoritative, lucid, intellectually exciting.
   - **Math density:** ~40% rigorous (full equations shown), ~35% formal (key steps shown), ~25% semi-formal (result stated with physical explanation).
   - **Every equation explained physically.** Don't just show math — tell the reader what it MEANS.
   - **Every claim traces to Foundations** with citation: "(See Foundations Vol 2, Chapter 3 for the full derivation.)"
   - **Be honest about gaps.** If a derivation is incomplete in Foundations, say so. This earns physicist respect.

5. **Self-Review** — Author checklist + Book 1-specific checks: voice is Brian Greene, math density is right, every claim cites Foundations, no unexplained equations.

6. **Run Reviewer Agents** — 8 assigned to Book 1:

   | Reviewer | File | Focus |
   |----------|------|-------|
   | The Physicist | REVIEWER_01 | Math validity, derivation integrity |
   | The "But Why?" Reader | REVIEWER_02 | **Most critical.** WHY chain complete? |
   | The Writing Coach | REVIEWER_03 | Brian Greene voice, readability |
   | The Consistency Auditor | REVIEWER_04 | Notation, cross-references |
   | The Skeptic | REVIEWER_06 | Logical integrity, credibility |
   | The Style Editor | REVIEWER_08 | Style sheet compliance |
   | The Theologian | REVIEWER_09 | Biblical accuracy |
   | The Navigator | REVIEWER_10 | Depth calibration (not too technical, not too shallow) |

   NOT assigned: Homeschool Mom (REVIEWER_05), Student (REVIEWER_07)

7. **Revise until all PASS.**

8. **Update STATUS.md and QUALITY_GATE.md.**

### Chapter Structure (25 Chapters, 5 Parts)

**Part I: Why This Book Exists (Ch 1–3)** — Hook the reader, establish the problem, introduce the framework
**Part II: The Architecture (Ch 4–8)** — Zone manifold, firmament, waters, patterns, principles
**Part III: Forces and Laws (Ch 9–16)** — Four forces, classical mechanics, thermodynamics, QM, GR
**Part IV: Applications (Ch 17–22)** — Cosmology, dark matter/energy, black holes, constants, predictions
**Part V: Validation (Ch 23–25)** — Comparison with standard physics, open problems, invitation

### Critical Priority Chapters (from STATUS.md)

These 6 chapters require substantial new writing or complete rewrites:
- **Ch 11–13:** Complete rewrites (force unification, governing principles, conservation laws) — 60–80 hours each
- **Ch 15–16:** New chapters (QM from membrane dynamics, GR from 6D embedding) — 70–90 hours each
- **Ch 24:** New comparison chapter (zone architecture vs. standard physics) — 40–60 hours

### Word Count Targets

- **Per chapter:** 3,500–5,000 words
- **Total book:** 80,000–100,000 words

### Critical Rules

- **Every equation explained physically.** No naked math.
- **Every claim traces to Foundations.** Citation required.
- **Be honest about gaps.** Physicist readers will respect this more than hand-waving.
- **Moderate math density.** This is not a textbook (that's Foundations). This is an intellectual tour.
- **No scripture quotation.** That's Book 2 and Creator's Blueprint territory. Book 1 is physics.
- **Leave them wanting more.** End with hooks pointing to both Foundations (deeper math) and Book 2 (broader audience).

### Skills Available

- **`genesis-chapter-writer`** — Full chapter lifecycle
- **`genesis-reviewer`** — Run reviewer agents

---

*This prompt was generated April 6, 2026 from the complete project setup.*
