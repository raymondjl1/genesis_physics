# Book 2: The Hidden Architecture — Writing Prompt

**Use this prompt to instruct Claude Cowork to write chapters for The Hidden Architecture.**

---

## Prompt

You are writing **Genesis Physics: The Hidden Architecture of Creation**, a narrative nonfiction book (~55,000–70,000 words, 15 chapters) for intelligent laypeople. This book has **ZERO equations** — not even E=mc². Your voice is **Brian Cox meets C.S. Lewis** — wonder-driven, intellectually rigorous, deeply beautiful. The reader should finish every chapter thinking "I never knew physics could be this amazing."

### Before You Begin

Read these files in order:

1. **`01_Genesis_Physics/CLAUDE.md`** — Master project instructions, philosophy
2. **`Book_2_The_Hidden_Architecture/CLAUDE.md`** — Book 2-specific instructions, ZERO equations rule, analogy standards, voice
3. **`Book_2_The_Hidden_Architecture/README.md`** — 15-chapter outline, production notes
4. **`Book_2_The_Hidden_Architecture/STATUS.md`** — Current status, milestones, rewriting standards
5. **`Development_Process/01_WRITING_PROCESS.md`** — Chapter writing workflow
6. **`Development_Process/03_CHAPTER_SPEC_TEMPLATE.md`** — Chapter spec template
7. **`Quality_Control/00_SERIES_VISION.md`** — The North Star
8. **`Quality_Control/BOOK_SERIES_STRATEGY.md`** — Book 2 section with detailed 15-chapter plan

### Source Material

Book 2 draws from **Book 1**, not directly from Research:

```
Book_1_The_Firmament_Equations/Manuscript/  ← PRIMARY SOURCE (every claim must trace here)
Book_0_The_Foundations/Source_Reference/     ← Original manuscript for reference
Quality_Control/Reference/                  ← Glossary, zone architecture, biblical refs
```

**The cascade rule:** Every concept in Book 2 must correspond to a chapter in Book 1. Replace equations with analogies, but never say anything the equations wouldn't support. If Book 1 doesn't have the chapter yet, note the dependency.

### Reference Documents

```
Quality_Control/Reference/
  Glossary.md                     ← Simplified versions of these terms for lay audience
  Zone_Architecture.md            ← Zone properties (translate to analogies)
  Biblical_References.md          ← Scripture — use sparingly, as wonder, not proof
  Four_Epochs_Timeline.md         ← Creation → Edenic → Fall → Redemption narrative arc
```

### Writing Process

For each chapter:

1. **Create CHAPTER_SPEC.md** from template. Include: mission, Book 1 source chapter(s), "why" chain, analogy plan, figure/illustration needs.

2. **Verify Book 1 Source** — Check that the Book 1 chapter supporting this Book 2 chapter exists and is verified.

3. **Write Detailed Outline** — 4–8 sections. Plan your analogies and narrative hooks.

4. **Write Draft** — Follow the Five Writing Laws plus Book 2-specific rules:
   - **Voice:** Brian Cox meets C.S. Lewis. Wonder. Beauty. "Come see something amazing."
   - **ZERO EQUATIONS.** Not even E=mc². Not even F=ma. NOTHING with an equals sign. Describe what the math means in words and analogies.
   - **Analogies must be accurate.** Every analogy must map correctly to the physics, have clearly stated limits ("This analogy breaks down when..."), be memorable, and be original.
   - **No scripture quotation.** This is not the Creator's Blueprint. Let the wonder of the physics speak for itself. Biblical grounding is implicit, never explicit.
   - **Grade 10–12 reading level.** Flesch-Kincaid target. An intelligent 16-year-old should follow every page.
   - **Leave them hungry.** End every chapter wanting more. End the book with a hook to Book 1 ("Everything in this book can be proven mathematically").

5. **Self-Review** — Author checklist + Book 2-specific checks:
   - Zero equations scan (CTRL+F for "=" signs)
   - Analogy accuracy audit (does each analogy match the physics?)
   - Reading level check (Flesch-Kincaid)
   - Wonder test (does this chapter inspire awe?)

6. **Run Reviewer Agents** — 7 assigned to Book 2:

   | Reviewer | File | Focus |
   |----------|------|-------|
   | The "But Why?" Reader | REVIEWER_02 | **Most critical.** WHY chain complete? |
   | The Writing Coach | REVIEWER_03 | Brian Cox/C.S. Lewis voice, Grade 10–12 readability |
   | The Consistency Auditor | REVIEWER_04 | Physics consistent with Book 1? Terms correct? |
   | The Skeptic | REVIEWER_06 | No circular reasoning, no unfalsifiable claims |
   | The Style Editor | REVIEWER_08 | Style sheet compliance |
   | The Theologian | REVIEWER_09 | Biblical accuracy (even though scripture isn't quoted) |
   | The Navigator | REVIEWER_10 | Not too technical for lay audience, coherent with series |

   NOT assigned: Physicist (REVIEWER_01), Homeschool Mom (REVIEWER_05), Student (REVIEWER_07)

7. **Revise until all PASS.**

8. **Update STATUS.md and QUALITY_GATE.md.**

### Chapter Structure (15 Chapters, 4 Parts)

**Part I: The Question (Ch 1–3)** — Hook: what if physics has been hiding something? What if Genesis 1 describes real architecture?
**Part II: The Framework (Ch 4–8)** — Zone architecture explained through analogy: zones, firmament, waters, forces, matter
**Part III: The Payoff (Ch 9–12)** — Mind-blowing implications: dark matter/energy solved, starlight problem, black holes, quantum weirdness
**Part IV: The Invitation (Ch 13–15)** — What this means, what's next, the invitation to go deeper

### Analogy Standards (Critical)

Every major concept needs an analogy. Each analogy must pass four tests:
1. **Maps correctly** — the analogy's structure matches the physics structure
2. **Has clear limits** — explicitly state where the analogy breaks down
3. **Is memorable** — the reader should remember it a week later
4. **Is original** — don't recycle tired physics analogies (rubber sheet for spacetime, etc.)

### Illustration Needs

- **15–20 professional illustrations** targeted
- Plan figures during the outline phase
- Each illustration should be describable in words first (for the draft), then illustrated professionally later
- Focus on: zone architecture diagrams, Chladni pattern photos, wave demonstrations, cosmological structures

### Word Count Targets

- **Per chapter:** 3,500–5,000 words
- **Total book:** 55,000–70,000 words

### Critical Rules

- **ZERO EQUATIONS.** This is the #1 rule. Not even simple ones. Words and analogies only.
- **Every claim traces to Book 1.** Citation: "(For the mathematics behind this, see *The Firmament Equations*, Chapter X.)"
- **Wonder drives the narrative.** If a paragraph doesn't inspire awe or curiosity, rewrite it.
- **No preaching.** This is not a Christian apologetics book. It's a science book that happens to derive from Genesis.
- **Grade 10–12 reading level.** Every reader should feel smart, not lost.
- **Leave them hungry for Book 1.** The ultimate success is a reader who says "I need to see the math."

### Skills Available

- **`genesis-chapter-writer`** — Full chapter lifecycle
- **`genesis-reviewer`** — Run reviewer agents

---

*This prompt was generated April 6, 2026 from the complete project setup.*
