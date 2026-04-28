# The Hidden Architecture: A Physics of the First Page — Writing Prompt

**Book title:** *Genesis Physics: The Hidden Architecture — A Physics of the First Page*

**Use this prompt to instruct Claude Cowork to write chapters for the Popular Science Flagship (launch order: SECOND).**

> **REPOSITIONING NOTE (April 2026):** This folder used to hold a physicist-level monograph titled *The Firmament Equations* (Brian Greene voice, 25 chapters, 40% rigorous math) at path `Book_1_The_Firmament_Equations/`. That positioning was the wrong commercial bet and the content has been repositioned as the franchise's **Popular Science Flagship** — *Genesis Physics: The Hidden Architecture — A Physics of the First Page* — the second book to ship under the Jeff L. Raymond byline. The folder has been renamed to `Book_1_Hidden_Architecture/`. The rigorous math lives in the Foundations Series; this book explains and dramatizes.

---

## Prompt

You are writing the **Popular Science Flagship** of the Genesis Physics franchise — a trade nonfiction book (~70,000–90,000 words, 14–18 chapters, final count TBD) in the *Elegant Universe* / *Reality Is Not What It Seems* lineage, aimed at intelligent laypeople (Greene / Rovelli / Sean Carroll / John Lennox readers). It is the book that establishes Jeff L. Raymond as a credible, distinct popular-science author. Your voice is **Jeff L. Raymond's, as defined in `AUTHOR_VOICE_AND_BACKGROUND.md`** — an operator-not-professor with aerospace-engineering and intelligence-community credentials, MBSE discipline, builder's honesty, and quiet faith. This is not Brian Greene and it is not Carl Sagan; it is someone who has actually built and flown systems explaining a framework he has spent a decade working out.

### Before You Begin

Read these files in order:

1. **`01_Genesis_Physics/AUTHOR_VOICE_AND_BACKGROUND.md`** — **READ FIRST.** Canonical voice and background reference for the entire franchise. Contains the author's biographical arc, the six voice pillars, voice rules, the voice test, comp authors, and three canonical author bios. Every chapter must satisfy the voice pillars and pass the voice test.
2. **`01_Genesis_Physics/CLAUDE.md`** — Master project instructions, philosophy, reviewer agents
3. **`Book_1_Hidden_Architecture/CLAUDE.md`** — Popular-science flagship instructions (includes the repositioning note, new spec, revised reviewer list)
4. **`Book_1_Hidden_Architecture/CHAPTER_PROMPTS.md`** — **Authoritative 15-chapter outline.** This is where the current chapter structure and per-chapter prompts live.
5. **`Book_1_Hidden_Architecture/README.md`** — **Archival** 25-chapter physicist outline; use for content inventory only. CHAPTER_PROMPTS.md (above) is authoritative.
6. **`Book_2_The_Hidden_Architecture/CLAUDE.md` and `README.md`** — The prior zero-equations spec; narrative beats from here may inform chapter drafting (15-chapter outline was adopted from this folder's README).
7. **`Book_1_Hidden_Architecture/STATUS.md`** — Current development status (note: may be stale relative to new positioning)
8. **`Development_Process/01_WRITING_PROCESS.md`** — Chapter writing workflow
9. **`Development_Process/03_CHAPTER_SPEC_TEMPLATE.md`** — Chapter spec template
10. **`Quality_Control/00_SERIES_VISION.md`** — The North Star
11. **`Quality_Control/BOOK_SERIES_STRATEGY.md`** — Both the original "BOOK 1" section (archival) and the "BOOK 2: The Hidden Architecture" section (source of current popular-science thinking)

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

4. **Write Draft** — Follow the Five Writing Laws plus popular-science flagship rules:
   - **Voice:** Jeff L. Raymond as defined in `AUTHOR_VOICE_AND_BACKGROUND.md` — operator-not-professor authority, frontline-leader confidence, MBSE discipline, builder's honesty, quiet faith. Wonder-driven narrative told by someone who has actually built things, not by an academic at a podium. **Re-read the voice pillars and voice test before drafting.**
   - **Math density:** Light. Conceptual diagrams and a small number of named equations only. No naked math. No derivations. Where math is needed, the Foundations Series is the encyclopedia — point readers there.
   - **Every concept explained physically and operationally.** Use analogies grounded in the kinds of systems the author actually knows (aerospace, signal processing, ISR, networked sensors). Reuse the franchise's analogy inventory; flag and fix any tired physics analogies.
   - **Every claim traces to Foundations** with citation: "(See Foundations Vol 2, Chapter 3 for the full derivation.)"
   - **Be honest about gaps.** If a derivation is incomplete in Foundations, say so. Builder's honesty is one of the voice pillars.
   - **No scripture quotation.** Implicit theology only. The Family Edition is where scripture leads.

5. **Self-Review** — Author checklist + popular-science flagship checks: voice satisfies the pillars and passes the voice test in `AUTHOR_VOICE_AND_BACKGROUND.md`, math density is light (not zero, never naked), every claim cites Foundations, analogies pass the four analogy tests, reading level is Grade 11–13.

6. **Run Reviewer Agents** — 8 assigned to the popular-science flagship (revised from the old physicist-monograph list):

   | Reviewer | File | Focus |
   |----------|------|-------|
   | The "But Why?" Reader | REVIEWER_02 | **Most critical.** WHY chain complete? |
   | The Writing Coach | REVIEWER_03 | Voice matches `AUTHOR_VOICE_AND_BACKGROUND.md`? Wonder-driven? Grade 11–13 readable? |
   | The Skeptic | REVIEWER_06 | Logical integrity, no unfalsifiable claims, credible to a Greene reader? |
   | The Consistency Auditor | REVIEWER_04 | Claims trace to Foundations, terminology matches franchise |
   | The Physicist | REVIEWER_01 | Underlying physics correct against Foundations (even where math isn't shown) |
   | The Style Editor | REVIEWER_08 | Style sheet compliance |
   | The Theologian | REVIEWER_09 | Implicit theology sound (no scripture quoted, but framework must not contradict it) |
   | The Navigator | REVIEWER_10 | Depth calibration — sophisticated for Greene reader, accessible for smart layperson |

   NOT assigned: Homeschool Mom (REVIEWER_05), Student (REVIEWER_07)

7. **Revise until all PASS.**

8. **Update STATUS.md and QUALITY_GATE.md.**

### Chapter Structure — 15 chapters, 4 parts

**Authoritative outline and per-chapter prompts:** `Book_1_Hidden_Architecture/CHAPTER_PROMPTS.md`. The 15-chapter structure was adopted (April 2026) from the archival `Book_2_The_Hidden_Architecture/README.md` popular-science outline — it's the best match for the repositioned flagship audience. The old 25-chapter physicist outline in `Book_1_Hidden_Architecture/README.md` is archival.

**Part I: The Question (Ch 1–3)** — Hook. The silence in mainstream physics. Reading Genesis 1 as engineering spec. The architecture revealed.
**Part II: The Framework (Ch 4–8)** — The firmament membrane. The hidden energy (open system). More room than three dimensions. Pattern operators. Seven days, seven patterns.
**Part III: The Payoff (Ch 9–13)** — Where matter comes from. Gravity and light. Conservation laws. Dark sector and the light-speed question. The starlight problem.
**Part IV: The Invitation (Ch 14–15)** — What this changes. The road ahead — handoff to the Family Edition (theological undertow) and Foundations Series (the math).

### Word Count Targets

- **Per chapter:** 3,500–5,000 words
- **Total book:** 70,000–90,000 words

### Critical Rules

- **Voice fidelity.** Every chapter satisfies the six voice pillars and passes the voice test in `AUTHOR_VOICE_AND_BACKGROUND.md`.
- **Light math density, never naked.** Conceptual diagrams, a small number of named equations, point readers to Foundations for derivations.
- **Every claim traces to Foundations.** Citation required even when the equation isn't shown.
- **Be honest about gaps.** Builder's honesty is a voice pillar.
- **No scripture quotation.** Implicit theology only. The Family Edition is where scripture leads.
- **Leave them wanting more.** End pointing two ways: Family Edition for readers who sense the theology, Foundations for readers who want the math.

### Skills Available

- **`genesis-chapter-writer`** — Full chapter lifecycle
- **`genesis-reviewer`** — Run reviewer agents

---

*This prompt was generated April 6, 2026 from the complete project setup.*
