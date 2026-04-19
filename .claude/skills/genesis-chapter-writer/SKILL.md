---
name: genesis-chapter-writer
description: Write a Genesis Physics chapter following the full development process. Guides through spec creation, outline, drafting, self-review, and reviewer verification. Use when writing, drafting, creating, or starting a new chapter for any Genesis Physics product (Foundations, Book 1, Book 2, The Creator's Blueprint).
---

# Genesis Physics Chapter Writer Skill

Write a chapter following the complete Development Process lifecycle.

## When to Use This Skill

- When the user says "write chapter", "draft chapter", "start chapter", "create chapter"
- When beginning work on any chapter in any Genesis Physics product
- When the user wants to follow the full chapter writing workflow

## Pre-Flight Checks

Before writing anything, verify:

1. **Which product?** Foundations Vol N / Book 1 / Book 2 / The Creator's Blueprint
2. **Which chapter?** Chapter number and working title
3. **Is the prerequisite book/volume complete?** Check build order:
   - Foundations: Vol N requires Vols 1 through N-1
   - Book 1: Requires Foundations complete
   - Book 2: Requires Book 1 complete
   - The Creator's Blueprint: Requires Book 2 complete
4. **Does a CHAPTER_SPEC.md exist?** If not, create one first
5. **Are research files available?** Check the CLAUDE.md in the book folder for research mapping

## Phase 1: Chapter Specification

Read the template from `01_Genesis_Physics/Development_Process/03_CHAPTER_SPEC_TEMPLATE.md`.

Create `Manuscript/ChXX_SPEC.md` in the chapter's book folder. Fill in:

- **Mission:** One sentence — what does this chapter accomplish?
- **Requirements:** Traced to book requirements (from QUALITY_GATE.md)
- **Prerequisites:** What the reader must already know (from which prior chapters)
- **"Why" chain:** What "but why?" questions does this chapter answer?
- **Key deliverables:** Product-specific:
  - Foundations: Derivation plan (starting point → result → equation numbers)
  - Book 1: Derivation plan (less formal) + comparison with standard physics
  - Book 2: Analogy plan (concept → analogy → why it works → where it breaks)
  - The Creator's Blueprint: Scripture plan (passage → how introduced → physics connection)
- **Figures and diagrams**
- **Problem sets** (Foundations only)
- **Verification criteria**

### Research Check

For each key deliverable, search the Research/ folder:

```bash
# Example: Looking for Maxwell's equations derivation
find 01_Genesis_Physics/Research -name "*.md" | xargs grep -l "Maxwell" 2>/dev/null
```

If a required derivation/analysis is NOT found in Research/:
1. Create `Manuscript/ChXX_RESEARCH_GAP.md`
2. Mark the requirement as BLOCKED in the chapter spec
3. Create a GitHub issue if `gh` is available
4. **Do NOT proceed to drafting until the gap is resolved or the user explicitly approves writing with the gap noted**

## Phase 2: Detailed Outline

Break the chapter into sections (4-8 per chapter). For each section, document:
- Topic sentence
- "Why" entry point
- Key content
- Exit condition (what the reader knows after this section)

### Figure and Diagram Plan

**The rule: if a reader would grab a napkin to draw it, the chapter needs a figure there.**

A figure is REQUIRED whenever any of these conditions are met:
1. **Spatial relationships** — geometry, topology, nesting, embedding, relative position
2. **Before/after transformations** — phase transitions, symmetry breaking, dimensional reduction
3. **Multi-step derivations** — flowcharts or roadmaps for derivation chains longer than 3 steps
4. **Conceptual models** — abstract ideas with a natural visual metaphor
5. **Data and predictions** — quantitative comparison between zone architecture predictions and experiment
6. **Hierarchies and taxonomies** — zone structure, particle classification, force unification diagrams
7. **Equations with geometric meaning** — metric tensors, curvature, field configurations

For each planned figure, specify in the chapter spec:

| Field | Description |
|-------|------------|
| **Figure ID** | `Fig V.Ch.N` (e.g., Fig 1.3.2 = Vol 1, Ch 3, Figure 2) |
| **Title** | Descriptive title (appears below figure in the book) |
| **Placement** | Which section, after which paragraph or equation |
| **What it shows** | Concrete visual description — what does the reader see? |
| **Why it's needed** | What becomes clear through this visual that prose alone can't convey? |
| **Type** | Diagram / Schematic / Plot / Flowchart / Comparison / Cross-section / Timeline |
| **Key labels** | What must be labeled (use canonical notation from Symbol_and_Constants.md) |
| **Equations referenced** | Which equations or concepts the figure illustrates |
| **Complexity** | Simple (1-2 elements) / Medium (3-5 elements) / Complex (6+ elements or 3D) |

Product-specific figure density targets:
- **Foundations:** High (2-4 per chapter) — technical, precise, labeled with equation refs
- **Book 1:** Medium (1-3 per chapter) — clean, publication-quality
- **Book 2:** High (3-5 per chapter) — illustrative, conceptual, NO equations in figures
- **The Creator's Blueprint:** Medium (2-3 per chapter) — warm, approachable, family-friendly

### Outline Review Checklist
- [ ] Every chapter requirement maps to at least one section
- [ ] No section uses concepts not yet established
- [ ] "Why" chain is unbroken
- [ ] Prerequisites are satisfied by prior chapters
- [ ] Figure plan complete — every spatial relationship, transformation, multi-step derivation, and conceptual model has a figure spec

## Phase 3: Draft

Follow the Five Writing Laws:

1. **Start with WHY** — before introducing any concept, explain why it matters and why it must be true
2. **Physical intuition before math** — reader should predict the result before seeing the derivation
3. **One voice** — stay in the product's register:
   - Foundations: Feynman writing a textbook
   - Book 1: Brian Greene's Elegant Universe
   - Book 2: Brian Cox meets C.S. Lewis
   - The Creator's Blueprint: Warm, encouraging teacher
4. **No forward dependencies** — never use a concept not yet established
5. **Mark uncertainty honestly** — open problems are labeled, not hidden

### Figure Placeholders During Drafting

While drafting, insert `[FIGURE: Fig V.Ch.N — brief description]` placeholders at every point where a figure is needed. Don't stop to create the figure — keep writing. The figure spec from Phase 2 tells you what goes there. During self-review (Phase 4), verify every placeholder has a matching spec.

### Product-Specific Drafting Rules

**Foundations:**
- Every derivation starts from previously established results (cite equation numbers)
- Every equation gets a number
- Key results get boxes
- Problem sets: computational → conceptual → challenge

**Book 1:**
- Every equation explained physically
- Every claim traces to Foundations
- Comparison with standard physics where relevant

**Book 2:**
- **ZERO EQUATIONS.** Not one. Search the draft for any mathematical notation.
- Every claim traces to Book 1
- Analogies are the primary tool — make them accurate and memorable

**The Creator's Blueprint:**
- **Scripture FIRST.** Chapter opens with what the Bible says.
- Minimum 5 scripture quotations with book:chapter:verse
- Discussion questions (open-ended)
- Family activities (hands-on)
- "But What About?" section addressing common questions

### Word Count Targets

| Product | Per Chapter |
|---------|-----------|
| Foundations | 8,000–15,000 words |
| Book 1 | 3,500–5,000 words |
| Book 2 | 3,500–5,000 words |
| The Creator's Blueprint | 4,000–6,000 words |

## Phase 4: Self-Review

Run the author checklist from `Development_Process/01_WRITING_PROCESS.md`:

### Universal
- [ ] "But why?" test — read as a newcomer, every claim has its reason
- [ ] Forward dependency audit — no concept used before introduced
- [ ] Notation consistency — symbols match Series Bible
- [ ] Prerequisites satisfied
- [ ] "Why" chain complete
- [ ] Word count in range
- [ ] All `[TODO]` markers resolved
- [ ] **Figure audit** — For every spatial relationship, transformation, multi-step derivation, or conceptual model: is there a figure? If a reader would grab a napkin to draw it, it needs a figure. Check every `[FIGURE: ...]` placeholder has a complete spec in the chapter spec.

### Product-specific checks (per the Writing Process document)

## Phase 5: Reviewer Verification

Invoke the `genesis-reviewer` skill to run all assigned reviewer agents.

If any reviewer FAILs:
1. Read findings carefully
2. Fix the chapter
3. Re-run the failed reviewer
4. Repeat until all PASS

## Phase 6: Finalize

1. Final read-through as a reader
2. Polish prose
3. Update chapter spec — mark requirements as MET
4. Update QUALITY_GATE.md — record pass status and date
5. Mark chapter as VERIFIED

## After Chapter is Complete

Run relevant test suites if the chapter involves physics derivations:

```bash
cd 01_Genesis_Physics/Research/Mathematical_Models
python -m pytest [relevant_domain]/test_*.py -v
```

If `gh` is available, update the chapter's GitHub issue and move it to "Done" on the project board.
