# Chapter Spec — [Chapter Title]

**Book/Volume:** [e.g., Foundations Vol 1: Architecture of Reality]
**Chapter Number:** [e.g., Chapter 3]
**Working Title:** [Title]
**Status:** DRAFT | OUTLINE COMPLETE | WRITING | VERIFICATION | VERIFIED

---

## Mission

*One sentence: What does this chapter accomplish for the reader?*

> [e.g., "This chapter derives the wave equation from first principles so the reader understands WHY waves propagate the way they do."]

---

## Requirements

*What must this chapter deliver? Every requirement traces to a book/volume requirement.*

| Req ID | Chapter Requirement | Traces To | Status |
|--------|-------------------|-----------|--------|
| ChXX-001 | [Specific deliverable] | [Book req ID, e.g., V1-003] | NOT MET / MET |
| ChXX-002 | [Specific deliverable] | [Book req ID] | NOT MET / MET |
| ChXX-003 | [Specific deliverable] | [Book req ID] | NOT MET / MET |

*Add as many rows as needed. Every row must trace to a book-level requirement. If it doesn't trace, either the chapter is doing something unnecessary or the book spec has a gap.*

---

## Prerequisites

*What must the reader already know before starting this chapter?*

| Concept | Established In |
|---------|---------------|
| [Concept name] | [Book/Volume, Chapter number] |
| [Concept name] | [Book/Volume, Chapter number] |

*If a prerequisite hasn't been covered in a prior chapter, this chapter cannot be written yet — or the chapter order needs to change.*

---

## "Why" Chain

*What "but why?" questions does this chapter answer? These are the questions a curious reader would ask that motivate this chapter's content.*

1. **Why [question]?** — Because [answer delivered in this chapter].
2. **Why [question]?** — Because [answer delivered in this chapter].
3. **Why [question]?** — Because [answer delivered in this chapter].

*Every item here must be answered in the chapter text. The "But Why?" reviewer agent will check for these specifically.*

---

## Key Deliverables

*The specific things this chapter must contain — derivations, analogies, scripture, figures, etc.*

### Derivations (Foundations / Book 1)

| # | Derivation | Starting Point | Result | Equations |
|---|-----------|---------------|--------|-----------|
| 1 | [What is derived] | [Starting from what] | [End result] | [Eq. numbers, filled after writing] |

### Analogies (Book 2)

| # | Concept | Analogy | Why It Works | Where It Breaks |
|---|---------|---------|-------------|----------------|
| 1 | [Concept] | [Analogy] | [Why accurate] | [Limitations] |

### Scripture Passages (The Creator's Blueprint)

| # | Passage | How Introduced | Connection to Physics |
|---|---------|---------------|---------------------|
| 1 | [Book Chapter:Verse] | [Context/setup] | [What it illuminates] |

### Figures and Diagrams

**The rule: if a reader would grab a napkin to draw it, the chapter needs a figure there.**

A figure is required for: spatial relationships, before/after transformations, multi-step derivation roadmaps, conceptual models, data vs. predictions, hierarchies, and equations with geometric meaning.

| Fig ID | Title | Type | Placement | What It Shows | Why It's Needed | Key Labels | Equations Referenced | Complexity |
|--------|-------|------|-----------|---------------|----------------|------------|---------------------|-----------|
| Fig V.Ch.1 | [Descriptive title] | [Diagram/Schematic/Plot/Flowchart/Comparison/Cross-section/Timeline] | [Section N, after Eq X] | [Concrete visual description] | [What becomes clear that prose alone can't convey] | [Labels using canonical notation] | [Eq numbers] | [Simple/Medium/Complex] |
| Fig V.Ch.2 | [Title] | [Type] | [Section] | [Description] | [Why needed] | [Labels] | [Eq refs] | [Complexity] |

*During drafting, insert `[FIGURE: Fig V.Ch.N — brief description]` placeholders. During self-review, verify every placeholder has a matching spec above.*

### Problem Sets (Foundations)

| Difficulty | Count | Topics Covered |
|-----------|-------|---------------|
| Computational | [#] | [Topics] |
| Conceptual | [#] | [Topics] |
| Challenge | [#] | [Topics] |

---

## Section Outline

*Planned sections for this chapter. Fill in during Phase 4 (Detailed Design).*

### Section 1: [Title]
- **Topic sentence:** [One sentence — what does this section do?]
- **"Why" entry point:** [How does this connect to what the reader already knows?]
- **Key content:** [Bullets — concepts, derivations, or passages]
- **Exit condition:** [What does the reader know/believe/can-do after this section?]

### Section 2: [Title]
- **Topic sentence:**
- **"Why" entry point:**
- **Key content:**
- **Exit condition:**

### Section 3: [Title]
- **Topic sentence:**
- **"Why" entry point:**
- **Key content:**
- **Exit condition:**

*Add more sections as needed. Typical range: 4-8 sections per chapter.*

---

## Verification Criteria

*How do we know this chapter is DONE? These are the specific checks that reviewer agents will run.*

### Universal Criteria

- [ ] Every requirement in the table above is marked MET
- [ ] "But why?" chain — every question answered in the chapter text
- [ ] No forward dependencies — no concept used that isn't established in prior chapters
- [ ] Notation consistent with Series Bible / prior chapters
- [ ] Word count within target range: [target] words
- [ ] All `[TODO]` markers resolved

### Product-Specific Criteria

**If Foundations:**
- [ ] Every derivation starts from previously established results (equation numbers cited)
- [ ] Problem sets cover full difficulty range
- [ ] Solutions written for all problems

**If Book 1:**
- [ ] Every claim traces to Foundations (or cites where it will be derived)
- [ ] Comparison with standard physics is fair and explicit

**If Book 2:**
- [ ] Zero equations in the text
- [ ] Every claim traces to Book 1
- [ ] Analogies are accurate (simplify without misleading)

**If The Creator's Blueprint:**
- [ ] Scripture quoted accurately with chapter:verse citations
- [ ] Every claim traces to Book 2
- [ ] Discussion questions promote genuine conversation
- [ ] A homeschool parent could teach from this chapter without additional resources

---

## Assigned Reviewers

*Check the product's QUALITY_GATE.md for the full reviewer assignment. List the agents who will verify this chapter:*

| Reviewer | Assigned? | Status | Date |
|----------|-----------|--------|------|
| The Physicist | YES/NO | — | — |
| But Why? Reader | YES/NO | — | — |
| Writing Coach | YES/NO | — | — |
| Consistency Auditor | YES/NO | — | — |
| Homeschool Mom | YES/NO | — | — |
| The Skeptic | YES/NO | — | — |
| The Student | YES/NO | — | — |

---

## Required Chapter-End Footer (mandatory closing block)

*Every Foundations chapter draft MUST end with the following footer block, immediately after a `---` rule. This is a hard verification gate (checked by the Consistency Auditor). Source pattern: Vol 2 Ch 5 (`0516_Rev_204` / GitHub #304, `0516_Rev_467` / GitHub #567).*

```
---

*Build order verified: Chapter [N] uses only results from [list prior volumes/chapters cited]. No forward dependencies.*

*Equation numbering: ([Vol].[Ch].N) — Volume [Vol], Chapter [Ch], Equation N.*

*Citation convention: [state how prior-volume and prior-chapter equations are referenced, e.g. Vol 1 equations as (1.Ch.Eq); prior-chapter equations by their original numbers].*
```

- [ ] **Build-order line present** and lists every prior volume/chapter this chapter depends on
- [ ] **No forward dependencies** asserted and true
- [ ] **Equation-numbering line present** and matches the scheme used in the body
- [ ] **Citation-convention line present**
- [ ] *(Final chapter of a volume only)* **Volume-closing handoff section present** — see `Quality_Control/templates/VOLUME_CLOSING_HANDOFF_TEMPLATE.md`

---

## Notes

*Any additional context, open questions, or decisions to record about this chapter.*

- [Note 1]
- [Note 2]

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| [Date] | Initial spec created | — |

---

*Template source: `Development_Process/03_CHAPTER_SPEC_TEMPLATE.md`. Copy this file to `[Book]/Manuscript/ChXX_SPEC.md` and fill in for each chapter.*
