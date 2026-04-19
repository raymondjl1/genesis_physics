# Genesis Physics Series — End-to-End Validation Plan

**Date:** April 5, 2026
**Derived from:** 00_SERIES_VISION.md (what "done" looks like), 01_REQUIREMENTS.md (all requirements)
**Status:** Living document — run this plan against every chapter, every volume, every product

---

## Philosophy

This validation plan works like an end-to-end test suite for a software product. Before any chapter ships, it must pass through a panel of reviewer agents — each one a specialist critic with a specific mandate. If any reviewer flags a FAIL, the chapter goes back for revision.

Think of it as a panel of editors, each reading from a different perspective:

| Reviewer Agent | Persona | What They're Looking For |
|---------------|---------|------------------------|
| **The Physicist** | Skeptical PhD physicist, no patience for hand-waving | Mathematical rigor, complete derivations, honest error bars |
| **The "But Why?" Reader** | Intelligent person who always asks "but why?" | Whether every concept's reason is explained before or alongside its introduction |
| **The Writing Coach** | Professional developmental editor | Voice consistency, readability, flow, no jargon without definition |
| **The Consistency Auditor** | Obsessive continuity checker | Terminology, notation, cross-references, no contradictions |
| **The Homeschool Mom** | Parent teaching physics at the kitchen table | Clarity, scripture accuracy, teachability, "can I explain this to my 14-year-old?" |
| **The Skeptic** | Hostile reader looking for weaknesses | Unfalsifiable claims, circular reasoning, proof-texting, logical gaps |
| **The Student** | Graduate student working through problem sets | Learnability, worked examples, problem difficulty, "can I actually do the homework?" |

Not every reviewer runs against every product. See the matrix below.

---

## Reviewer Assignment Matrix

| Reviewer Agent | Foundations | Book 1 | Book 2 | The Creator's Blueprint |
|---------------|------------|--------|--------|---------------|
| The Physicist | **YES** | **YES** | no | no |
| The "But Why?" Reader | **YES** | **YES** | **YES** | **YES** |
| The Writing Coach | **YES** | **YES** | **YES** | **YES** |
| The Consistency Auditor | **YES** | **YES** | **YES** | **YES** |
| The Homeschool Mom | no | no | no | **YES** |
| The Skeptic | **YES** | **YES** | **YES** | no |
| The Student | **YES** | no | no | no |
| The Style Editor | **YES** | **YES** | **YES** | **YES** |
| The Theologian | **YES** | **YES** | **YES** | **YES** |
| The Navigator | **YES** | **YES** | **YES** | **YES** |

---

## Validation Levels

### Level 1: Chapter Validation (run on every chapter before it's considered draft-complete)

Each chapter must pass its assigned reviewers. A chapter PASSES when all assigned reviewers return PASS or PASS WITH NOTES. A chapter FAILS if any reviewer returns FAIL.

**Process:**
1. Author completes chapter draft
2. Each assigned reviewer agent reads the chapter
3. Each reviewer produces a scorecard (see templates below)
4. FAIL items are addressed
5. Repeat until all PASS

### Level 2: Volume Validation (run on each completed volume)

Cross-chapter checks that can only be done at the volume level:

| Check | What | Pass Criteria |
|-------|------|--------------|
| Dependency audit | Concept dependency graph has no forward references | Zero concepts used before defined |
| Notation audit | Every symbol used matches the Volume 1 notation guide | Zero notation conflicts |
| Cumulative "why" test | Read chapters in order; at no point should a reader lack the "why" for what they're reading | Reviewer reads front-to-back and flags zero "but why?" moments |
| Problem set coherence | Problems reference only material covered in current and prior chapters | Zero problems requiring uncovered material |
| Readability consistency | Flesch-Kincaid score consistent across chapters (within 2 grade levels) | No chapter is an outlier |
| Bibliography completeness | Every factual claim has a citation | Zero uncited claims |

### Level 3: Series Validation (run when multiple products are complete)

Cross-product checks:

| Check | What | Pass Criteria |
|-------|------|--------------|
| Cascade accuracy | Every claim in Book 2 has a chapter in Book 1 backing it. Every claim in Book 1 has a derivation in Foundations. | Zero unsupported claims at any level. |
| Voice separation | Products don't bleed into each other's register | Blind reviewer can identify which product a random chapter comes from |
| Cross-reference accuracy | Every "see Volume X, Chapter Y" reference points to real, relevant content | Zero broken or misleading cross-references |
| Scripture accuracy | Every Bible quotation is verbatim from a named translation. Every chapter/verse citation is correct. | Zero misquotations. Zero wrong references. |
| The "dinner table" test | A reader of Book 2 can explain the key ideas to a friend. A reader of The Creator's Blueprint can teach a lesson. | Beta readers successfully explain/teach after reading. |
| The "hostile reviewer" test | A skeptical physicist reads Book 1 and Foundations Vol 1. Can they find logical errors, unsupported claims, or dishonesty? | Zero logical errors. All limitations explicitly acknowledged. |

### Level 4: Publication Validation (run before hitting "publish" on Amazon)

| Check | What | Pass Criteria |
|-------|------|--------------|
| KDP format compliance | File passes KDP's automated checks | Zero errors in KDP previewer |
| Cover quality | Professional cover, readable at thumbnail size | Looks professional next to comparable books on Amazon |
| "Look Inside" preview | First 10% is compelling and error-free | Zero typos. Hook is strong. Formatting is clean. |
| Category placement | Books appear in correct Amazon categories | Verified post-publication |
| Audiobook quality (Book 2, FE) | ACX standards met. Clear narration. Correct pacing. | Passes ACX quality check |
| Pricing strategy | Prices competitive for category | Within range of comparable books in same categories |

---

## Reviewer Agent Scorecards

### The Physicist — Chapter Scorecard

```
CHAPTER: [name]
PRODUCT: [Foundations Vol X / Book 1]
REVIEWER: The Physicist
DATE: [date]

DERIVATION COMPLETENESS:
[ ] Every derivation is complete (no "it can be shown that")
[ ] Starting assumptions are explicitly stated
[ ] Each step follows logically from the previous
[ ] Final result includes error bars where applicable
[ ] Comparison with experimental data provided

MATHEMATICAL RIGOR:
[ ] Notation is consistent with Volume 1 conventions
[ ] All variables defined before use
[ ] Approximations identified and justified
[ ] Limiting cases checked (does this reduce to known physics?)
[ ] Dimensional analysis passes

FALSIFIABILITY:
[ ] Predictions are specific and testable
[ ] Falsification criteria stated for major claims
[ ] Honest about what hasn't been derived yet
[ ] No circular reasoning

OVERALL: [ ] PASS  [ ] PASS WITH NOTES  [ ] FAIL
NOTES: [specific items to address]
```

### The "But Why?" Reader — Chapter Scorecard

```
CHAPTER: [name]
PRODUCT: [any]
REVIEWER: The "But Why?" Reader
DATE: [date]

THE WHY TEST:
For each major concept introduced in this chapter:
[ ] The reader knows WHY before they see WHAT
[ ] The physical intuition is given before the math
[ ] No concept is introduced as "just accept this"
[ ] Every equation has a sentence explaining what it MEANS

CUMULATIVE KNOWLEDGE:
[ ] No concepts used that haven't been established in prior chapters
[ ] "What you should already know" is stated at chapter opening
[ ] Forward references are flagged as previews, not dependencies

THE "BUT WHY?" SCAN:
Read each paragraph. After each one, ask "but why?"
[ ] Every "but why?" has an answer in the preceding or current text
[ ] Zero moments where the answer is "we don't explain that"
[ ] Where the answer is "open problem," this is stated explicitly

OVERALL: [ ] PASS  [ ] PASS WITH NOTES  [ ] FAIL
NOTES: [specific "but why?" moments that need addressing]
```

### The Writing Coach — Chapter Scorecard

```
CHAPTER: [name]
PRODUCT: [any]
REVIEWER: The Writing Coach
DATE: [date]

VOICE:
[ ] Consistent with product's target voice throughout
[ ] No register shifts (technical in Book 2, devotional in Foundations)
[ ] Appropriate for target audience reading level

STRUCTURE:
[ ] Clear topic sentence / opening orientation
[ ] Logical paragraph flow
[ ] Effective transitions between sections
[ ] Satisfying chapter conclusion that motivates the next chapter

READABILITY:
[ ] Flesch-Kincaid score within target range for this product
[ ] Jargon defined at first use
[ ] Sentences varied in length and structure
[ ] No walls of text without visual breaks

ENGAGEMENT:
[ ] Reader motivation maintained throughout
[ ] Key insights highlighted effectively
[ ] Examples and analogies support understanding
[ ] Chapter doesn't feel like a slog

OVERALL: [ ] PASS  [ ] PASS WITH NOTES  [ ] FAIL
NOTES: [specific passages that need revision]
```

### The Consistency Auditor — Chapter Scorecard

```
CHAPTER: [name]
PRODUCT: [any]
REVIEWER: The Consistency Auditor
DATE: [date]

TERMINOLOGY:
[ ] Zone names match Series Bible
[ ] Five Principles naming/ordering matches canonical
[ ] Hebrew transliteration follows standard
[ ] Dark matter/energy pairings stated at first use

NUMERICAL:
[ ] Constants match canonical values
[ ] The 68/27/5 split cited consistently
[ ] No numerical contradictions with other chapters/volumes

CROSS-REFERENCES:
[ ] All "see Chapter X" references are accurate
[ ] All "see Volume Y" references point to real content
[ ] No contradictions with referenced content

FRAMEWORK LOGIC:
[ ] Zone boundary rules consistent with canonical definitions
[ ] No mechanisms that contradict established principles
[ ] Causal chains don't conflict with other chapters

OVERALL: [ ] PASS  [ ] PASS WITH NOTES  [ ] FAIL
NOTES: [specific inconsistencies found]
```

### The Homeschool Mom — Chapter Scorecard

```
CHAPTER: [name]
PRODUCT: [The Creator's Blueprint only]
REVIEWER: The Homeschool Mom
DATE: [date]

SCRIPTURE:
[ ] Direct scripture quotations are accurate (book/chapter/verse verified)
[ ] Scripture is used in context, not proof-texted
[ ] At least 5 direct quotations in this chapter
[ ] Scripture leads; physics confirms (not the other way around)

TEACHABILITY:
[ ] I could teach this to my 14-year-old after reading it
[ ] Key concepts are explained simply enough for a non-science parent
[ ] Discussion questions actually provoke good discussion
[ ] Family activity is doable with household items

OBJECTION HANDLING:
[ ] "But What About?" section addresses real questions kids ask
[ ] Answers are honest, not dismissive
[ ] Doesn't claim more certainty than the framework has earned

TONE:
[ ] Reverent without being preachy
[ ] Confident without being arrogant
[ ] Accessible without being condescending
[ ] Would feel at home in a homeschool co-op

OVERALL: [ ] PASS  [ ] PASS WITH NOTES  [ ] FAIL
NOTES: [specific teachability issues]
```

### The Skeptic — Chapter Scorecard

```
CHAPTER: [name]
PRODUCT: [any]
REVIEWER: The Skeptic
DATE: [date]

LOGICAL INTEGRITY:
[ ] No circular reasoning (assuming what's being proven)
[ ] No argument from authority ("the Bible says so, therefore physics")
[ ] No conflation of analogy with evidence
[ ] No equivocation (using a word in two different senses)

INTELLECTUAL HONESTY:
[ ] Limitations acknowledged explicitly
[ ] Alternative explanations mentioned where relevant
[ ] Not dismissive of standard physics
[ ] Error bars and uncertainties stated, not hidden

UNFALSIFIABLE CLAIMS:
[ ] Zero claims that cannot in principle be tested or refuted
[ ] Every major assertion has a stated falsification condition
[ ] "Open problem" used honestly, not as a shield

PROOF-TEXTING CHECK:
[ ] Scripture used in proper context
[ ] Hebrew word analysis is linguistically defensible
[ ] No forcing physics onto verses that don't support it

OVERALL: [ ] PASS  [ ] PASS WITH NOTES  [ ] FAIL
NOTES: [specific vulnerabilities found]
```

### The Student — Chapter Scorecard

```
CHAPTER: [name]
PRODUCT: [Foundations only]
REVIEWER: The Student
DATE: [date]

LEARNABILITY:
[ ] I could work through this chapter with a pencil and paper
[ ] Definitions are clear enough to use in problem-solving
[ ] Worked examples show the method, not just the answer
[ ] Difficulty ramps appropriately within the chapter

PROBLEM SETS:
[ ] Problems test understanding, not just calculation
[ ] At least 30% are "explain why" questions
[ ] Difficulty range: some accessible, some challenging
[ ] Selected solutions are genuinely helpful (show method, not just answer)

PREREQUISITES:
[ ] Everything I need to know is in earlier chapters or the math appendix
[ ] No hidden assumptions about background knowledge
[ ] If external math is needed, the specific reference is given

PRACTICAL:
[ ] Could I pass an exam on this material after working through the chapter?
[ ] Could I explain the key results to a classmate?
[ ] Do I understand not just WHAT but WHY?

OVERALL: [ ] PASS  [ ] PASS WITH NOTES  [ ] FAIL
NOTES: [specific learning obstacles]
```

### The Style Editor — Chapter Scorecard

```
CHAPTER: [name]
PRODUCT: [any]
REVIEWER: The Style Editor
DATE: [date]

STYLE SHEET COMPLIANCE:
[ ] Follows Series Bible terminology exactly
[ ] Notation matches Volume 1 conventions
[ ] Capitalization rules followed (Zone names, Principles, etc.)
[ ] Abbreviation usage consistent (defined at first use, used consistently after)
[ ] Heading hierarchy follows template

FORMATTING:
[ ] Equation numbering follows scheme (chapter.section.number)
[ ] Figure captions follow template
[ ] Table formatting consistent with other chapters
[ ] Footnotes/endnotes used per product convention
[ ] Citation style consistent

COPYEDITING:
[ ] No spelling or grammar errors
[ ] No orphaned references or dangling cross-links
[ ] Consistent use of Oxford comma, em-dashes, etc.
[ ] Numbers formatted consistently (spelled out vs. numeral rules)

OVERALL: [ ] PASS  [ ] PASS WITH NOTES  [ ] FAIL
NOTES: [specific style violations found]
```

### The Theologian — Chapter Scorecard

```
CHAPTER: [name]
PRODUCT: [any]
REVIEWER: The Theologian
DATE: [date]

SCRIPTURAL ACCURACY:
[ ] All Bible quotations are verbatim from a named translation
[ ] Chapter/verse references are correct
[ ] Scripture is used in proper literary and historical context
[ ] No proof-texting (pulling verses out of context to support a claim)
[ ] Hebrew word analysis is linguistically defensible

EXEGETICAL FIDELITY:
[ ] Interpretations of Genesis 1 are within defensible hermeneutical traditions
[ ] Theological claims don't contradict orthodox Christian doctrine
[ ] Framework doesn't force physics onto scripture inappropriately
[ ] Distinction maintained between "scripture says" and "framework interprets"

THEOLOGICAL TONE:
[ ] Reverent without being preachy
[ ] Confident without claiming more than scripture supports
[ ] Respectful of readers who hold different interpretive traditions
[ ] Does not dismiss mainstream theology carelessly

OVERALL: [ ] PASS  [ ] PASS WITH NOTES  [ ] FAIL
NOTES: [specific theological or exegetical concerns]
```

### The Navigator — Chapter Scorecard

```
CHAPTER: [name]
PRODUCT: [any]
REVIEWER: The Navigator
DATE: [date]

DEPTH CALIBRATION:
[ ] Content depth matches the product's target audience
[ ] Not too technical for the product (or too shallow for Foundations)
[ ] Appropriate level of mathematical detail for this product
[ ] Vocabulary complexity matches target reading level

SERIES COHERENCE:
[ ] Chapter content aligns with how this topic is treated in other products
[ ] No contradictions between this chapter and corresponding chapters in other books
[ ] Appropriate cross-references to other products where relevant
[ ] Maintains its product's unique voice while staying factually consistent

CASCADE INTEGRITY:
[ ] Claims in higher-level books trace down to lower-level derivations
[ ] Nothing promised in this chapter that isn't delivered in the expected location
[ ] Series reading paths (upward and downward) remain coherent

OVERALL: [ ] PASS  [ ] PASS WITH NOTES  [ ] FAIL
NOTES: [specific depth or coherence issues]
```

---

## Running the Validation

### When to Run

| Trigger | Validation Level |
|---------|-----------------|
| Chapter draft completed | Level 1 (Chapter) |
| All chapters in a volume done | Level 2 (Volume) |
| Book 1 completed (can compare with Foundations) | Level 3 (Series) |
| Ready to upload to Amazon | Level 4 (Publication) |
| Major revision to any published chapter | Level 1 (Chapter) re-run |

### How to Run

Each reviewer agent is implemented as a Claude sub-agent with a specific system prompt (defined in the reviewer definition files: `Reviewers/`). To validate a chapter:

1. Load the chapter content
2. Load the reviewer's system prompt
3. Load any required context (Series Bible, notation guide, prior chapters)
4. Run the reviewer agent
5. Collect the scorecard
6. Address any FAIL items
7. Re-run until PASS

### Tracking Results

Validation results are tracked in each product's `STATUS.md` file:

```
## Chapter Validation Status

| Chapter | Physicist | But Why? | Writing | Consistency | Skeptic | Student | Overall |
|---------|----------|----------|---------|-------------|---------|---------|---------|
| Ch 1    | PASS     | PASS     | NOTES   | PASS        | PASS    | PASS    | REVISE  |
| Ch 2    | PASS     | PASS     | PASS    | PASS        | PASS    | PASS    | DONE    |
```

---

## The Ultimate Test

When the entire series is complete, run this final validation:

**Give Volume 1 of the Foundations Series to a motivated graduate student with no prior exposure to zone architecture. Can they:**

1. Work through every chapter with pencil and paper?
2. Solve the problem sets?
3. Derive F=ma from axioms and explain WHY it must be true?
4. Explain to a non-physicist what zone architecture is and why it matters?
5. Identify at least one testable prediction they could design an experiment for?

**If yes: the Foundations Series works.**

**Give Book 2 to an intelligent friend who hates math. Can they:**

1. Explain the basic idea of zone architecture?
2. Tell you what dark matter and dark energy are in this framework?
3. Articulate why this matters for faith and science?
4. Want to read more?

**If yes: Book 2 works.**

**Give the The Creator's Blueprint to a homeschool parent. Can they:**

1. Teach a lesson from any chapter to their children?
2. Answer their kids' "but why?" questions?
3. Connect the physics to specific Bible passages?
4. Feel more confident in their faith, not less?

**If yes: the The Creator's Blueprint works.**

---

*This plan is the quality gate. Nothing ships without passing validation.*
