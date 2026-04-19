# Chapter-Level Writing Process

**Date:** April 5, 2026
**Author:** Jeff Raymond
**Purpose:** The step-by-step workflow for writing any chapter in the Genesis Physics Series — from requirements through verified draft.

---

## Overview

Every chapter follows the same lifecycle regardless of product:

```
CHAPTER_SPEC.md → Detailed Outline → Draft → Self-Review → Reviewer Agents → Revise → PASS
```

The process is requirements-driven. You don't start writing until you know what the chapter must accomplish. You don't call it done until reviewer agents agree it's done.

---

## Step 1: Load the Chapter Spec

Before writing a single word, open (or create) the chapter's `CHAPTER_SPEC.md` using the template in `03_CHAPTER_SPEC_TEMPLATE.md`.

**The spec must contain:**

- **Chapter requirements** — What must this chapter accomplish? (Traced to book requirements.)
- **Prerequisites** — What must the reader already know? (From which prior chapters?)
- **Key deliverables** — Specific derivations, analogies, scripture passages, or explanations.
- **"Why" chain** — What "but why?" questions does this chapter answer?
- **Verification criteria** — How do we know this chapter is DONE?

**Do not proceed to Step 2 until the spec is reviewed and stable.**

---

## Step 2: Detailed Outline

Plan the chapter at the section level before writing prose. This is the "detailed design review" — cheaper to fix here than in a full draft.

### 2a. Section Outline

Break the chapter into sections (typically 4-8 sections per chapter). For each section:

- **Topic sentence** — One sentence: what does this section do?
- **"Why" entry point** — How does this section connect to the reader's existing understanding?
- **Key content** — Bullet list of concepts, derivations, or passages to cover.
- **Exit condition** — What does the reader know/believe/can-do after this section?

### 2b. Product-Specific Planning

Depending on which product this chapter belongs to, add the relevant plan:

| Product | Additional Planning |
|---------|-------------------|
| **Foundations** | Derivation plan: which equations, in what order, from what starting point. Problem set plan: how many, what types, what difficulty. |
| **Book 1** | Derivation plan (less formal than Foundations). Comparison points with standard physics. |
| **Book 2** | Analogy plan: which analogies, for which concepts. Zero-equations check: flag anything that needs math and find a way to explain without it. |
| **The Creator's Blueprint** | Scripture plan: which passages, how introduced. Discussion questions. Family activity ideas. |

### 2c. Figure and Diagram Plan

**The rule: if a reader would grab a napkin to draw it, the chapter needs a figure there.**

Physics without pictures is incomplete. Every chapter must have a deliberate figure plan — not as decoration, but as essential teaching tools. A good figure replaces three paragraphs of verbal description and makes the "why" click.

#### When a Figure is REQUIRED

A figure is mandatory whenever any of these conditions are met:

1. **Spatial relationships** — Anything with geometry, topology, nesting, embedding, or relative position (zones inside zones, manifold cross-sections, boundary conditions)
2. **Before/after transformations** — Phase transitions, symmetry breaking, dimensional reduction, any process that changes state
3. **Multi-step derivations** — A flowchart or roadmap showing how pieces connect (especially for derivation chains longer than 3 steps)
4. **Conceptual models** — Abstract ideas that have a natural visual metaphor (e.g., the firmament as a vibrating membrane, Waters as interpenetrating fields)
5. **Data and predictions** — Any quantitative comparison between zone architecture predictions and experimental data (plots, tables with visual indicators)
6. **Hierarchies and taxonomies** — Zone structure, particle classification trees, force unification diagrams
7. **Equations with geometric meaning** — When an equation describes something spatial (metric tensors, curvature, field configurations), show the geometry alongside the math

#### Figure Specification Format

For each planned figure, specify:

| Field | Description |
|-------|------------|
| **Figure ID** | `Fig V.Ch.N` (e.g., Fig 1.3.2 = Vol 1, Ch 3, Figure 2) |
| **Title** | Descriptive title (appears below figure in the book) |
| **Placement** | Which section, after which paragraph or equation |
| **What it shows** | Concrete visual description — what does the reader see? |
| **Why it's needed** | What concept becomes clear through this visual that prose alone can't convey? |
| **Type** | Diagram / Schematic / Plot / Flowchart / Comparison / Cross-section / Timeline |
| **Key labels** | What must be labeled in the figure (use canonical notation from Symbol_and_Constants.md) |
| **References** | Which equations or concepts the figure illustrates |
| **Alt text** | Full text description for accessibility / audiobook adaptation |
| **Complexity** | Simple (1-2 elements) / Medium (3-5 elements) / Complex (6+ elements or 3D) |

#### Product-Specific Figure Guidance

| Product | Figure Density | Style | Notes |
|---------|---------------|-------|-------|
| **Foundations** | High (2-4 per chapter) | Technical, precise, labeled with equation refs | Every major derivation should have an accompanying geometric figure |
| **Book 1** | Medium (1-3 per chapter) | Clean, publication-quality | Equations + geometry side by side |
| **Book 2** | High (3-5 per chapter) | Illustrative, conceptual, NO equations in figures | Figures carry the explanatory load that equations carry in Foundations |
| **Creator's Blueprint** | Medium (2-3 per chapter) | Warm, approachable, family-friendly | Diagrams that a parent and child can discuss together |

#### Figure Numbering Convention

Figures follow the same convention as equations: `(V.Ch.Fig)` — e.g., Fig 1.3.2 = Vol 1, Ch 3, Figure 2. Cross-references use the full number: "As shown in Fig 1.3.2..."

#### Common Figure Types for Genesis Physics

- **Zone Nesting Diagram** — Concentric or layered structure showing Z₀ → Z₁ → Z₂ hierarchy
- **Membrane Cross-Section** — The firmament as a surface with above/below regions, curvature, and boundary conditions
- **Field Configuration** — Waters field density profiles, pressure gradients, equilibrium states
- **Derivation Roadmap** — Flowchart showing axiom → intermediate results → final theorem
- **Prediction vs. Data Plot** — Side-by-side or overlay comparing zone architecture predictions to experimental measurements
- **Symmetry Diagram** — Visual representation of symmetry operations, broken symmetries, conserved quantities
- **Timeline/Phase Diagram** — Four epochs (Creation → Edenic → Fall → Redemption) with physical parameters changing

### 2d. Outline Review

Before proceeding to drafting, review the outline against:

- [ ] Every chapter requirement has at least one section addressing it
- [ ] No section introduces concepts that haven't been established (no forward dependencies)
- [ ] The "why" chain is unbroken — every concept has its reason
- [ ] Prerequisites are satisfied by prior chapters (check their specs)

---

## Step 3: Write the Draft

Now write. Follow these principles absolutely:

### The Five Writing Laws

**1. Start with WHY.**
Before introducing any concept, explain why it matters and why it must be true. The reader should never think "but why?" without an answer on the same page or within the same section.

**2. Physical intuition before math.**
The reader should be able to *predict* the result before seeing the derivation. Build the intuition first, then confirm it with rigor. This applies to all products, not just Foundations — even Book 2 builds intuition before revealing the concept.

**3. One voice.**
Stay in the product's register throughout. Don't slip into textbook voice in Book 2. Don't slip into casual voice in Foundations. The voice is defined in each product's QUALITY_GATE.md.

| Product | Voice |
|---------|-------|
| Foundations | Graduate textbook. Precise, rigorous, but human. Like Feynman writing a textbook. |
| Book 1 | Professional monograph. Peer-to-peer with working physicists. |
| Book 2 | Intelligent conversation. Like explaining physics to a smart friend over coffee. |
| The Creator's Blueprint | Warm, encouraging teacher. Like a knowledgeable parent guiding their kids. |

**4. No forward dependencies.**
Never use a concept that hasn't been established yet in the reading order. If you need something from a later chapter, either restructure or add a brief "we'll see in Chapter N that..." placeholder — but the current argument must stand on its own.

**5. Mark uncertainty honestly.**
If something is an open problem, say so explicitly. If a derivation requires an assumption that hasn't been proven, flag it. The reader's trust is more valuable than the appearance of completeness.

### Drafting Mechanics

- **Write in order.** Start at Section 1 and proceed linearly. This catches forward-dependency violations in real time.
- **One section at a time.** Complete a section, review it against its outline entry, then move on.
- **Leave markers.** If you need to return to something, leave a `[TODO: ...]` marker. Don't break flow to solve side problems.
- **Mark figure placements.** While drafting, insert `[FIGURE: Fig V.Ch.N — brief description]` placeholders at every point where a figure is needed. Don't stop to create the figure — keep writing. The figure spec from Step 2c tells you what goes there. During self-review (Step 4), verify every placeholder has a matching spec.
- **Equations get numbers.** Every equation in Foundations and Book 1 gets a number. Reference by number, not by "the equation above."
- **Key results get boxes.** Important results, theorems, or principles get visually set apart (boxed equations, callout boxes, etc.) so they're easy to find during review.

### Word Count Targets

These are guidelines, not hard limits. Quality over quantity — but wildly exceeding these suggests the chapter is trying to do too much.

| Product | Words per Chapter |
|---------|------------------|
| Foundations | 8,000–15,000 (varies by volume) |
| Book 1 | 3,500–5,000 |
| Book 2 | 3,500–5,000 |
| The Creator's Blueprint | 4,000–6,000 |

---

## Step 4: Self-Review (Author Checklist)

Before sending to reviewer agents, run through this checklist yourself:

### Universal Checks

- [ ] **"But why?" test** — Read the chapter as a curious newcomer. Every time you encounter a claim, ask "but why?" If the answer isn't on the page or in a prior chapter, fix it.
- [ ] **Forward dependency audit** — Ctrl+F for any concept not yet introduced. Remove or restructure.
- [ ] **Notation consistency** — Check all symbols against the Series Bible / notation standard. No symbol used with two meanings.
- [ ] **Prerequisites satisfied** — Every concept the chapter relies on was covered in a prior chapter listed in the spec's prerequisites.
- [ ] **"Why" chain complete** — The chapter's assigned "but why?" questions (from the spec) are all answered.
- [ ] **Word count in range** — Check against the target. If over by more than 20%, consider splitting.
- [ ] **TODOs resolved** — Search for `[TODO` markers. Resolve all of them.
- [ ] **Figure audit** — For every spatial relationship, transformation, multi-step derivation, or conceptual model: is there a figure? If a reader would grab a napkin to draw it, it needs a figure. Check every `[FIGURE: ...]` placeholder has a complete spec.

### Product-Specific Checks

**Foundations:**
- [ ] Every derivation starts from previously established results (cite equation numbers)
- [ ] Problem sets cover the full difficulty range (computational → conceptual → challenge)
- [ ] Solutions exist for every problem (even if not included in the chapter)

**Book 1:**
- [ ] Every claim traces to Foundations (or is flagged as "derived in Foundations Vol X, Ch Y")
- [ ] Comparison with standard physics is fair — where standard physics does better, say so
- [ ] Notation is consistent with Foundations

**Book 2:**
- [ ] Zero equations. Not one. If an equation appears, it must be removed or explained in words.
- [ ] Every claim traces to Book 1 (even though the reader won't see Book 1)
- [ ] Analogies are accurate — they simplify without misleading

**The Creator's Blueprint:**
- [ ] Scripture is quoted accurately (chapter and verse cited)
- [ ] Every claim traces to Book 2
- [ ] A homeschool parent could teach from this chapter
- [ ] Discussion questions have no single "right answer" — they promote conversation

---

## Step 5: Verification (Reviewer Agents)

Run the chapter through its assigned reviewer agents. Each product has specific agents assigned in its `QUALITY_GATE.md`.

### Process

1. **Load reviewer definitions** from `Quality_Control/Reviewers/`
2. **Run each assigned reviewer** against the chapter
3. **Collect scorecards** — each reviewer produces a PASS/FAIL with specific findings
4. **Address all FAIL items** — fix the chapter, don't argue with the reviewer
5. **Re-run failed reviewers** until all PASS
6. **Update the QUALITY_GATE.md** validation status table

### Reviewer Assignment Quick Reference

| Reviewer | Foundations | Book 1 | Book 2 | Family Ed |
|----------|-----------|--------|--------|-----------|
| The Physicist | ✓ | ✓ | — | — |
| But Why? Reader | ✓ | ✓ | ✓ | ✓ |
| Writing Coach | ✓ | ✓ | ✓ | ✓ |
| Consistency Auditor | ✓ | ✓ | ✓ | ✓ |
| Homeschool Mom | — | — | — | ✓ |
| The Skeptic | ✓ | ✓ | ✓ | — |
| The Student | ✓ | — | — | — |
| Style Editor | ✓ | ✓ | ✓ | ✓ |
| Theologian | ✓ | ✓ | ✓ | ✓ |
| Navigator | ✓ | ✓ | ✓ | ✓ |

### What a PASS Looks Like

A chapter passes verification when:
- Every assigned reviewer returns PASS
- No RED FLAGS remain unresolved (red flags are automatic FAILs defined in each reviewer's spec)
- The chapter's QUALITY_GATE.md entry shows all-PASS

### What to Do When a Reviewer FAILs You

1. Read the reviewer's specific findings carefully
2. Fix the chapter — don't rationalize why the failure doesn't matter
3. If you genuinely disagree with a finding, document your reasoning in the QUALITY_GATE.md as a "noted exception" — but this should be rare
4. Re-run the reviewer to confirm the fix

---

## Step 6: Revise and Finalize

After all reviewers pass:

1. **Final read-through** — Read the chapter one more time, start to finish, as a reader (not an author)
2. **Polish prose** — Tighten sentences, improve transitions, ensure flow
3. **Update the chapter spec** — Mark verification criteria as met
4. **Update QUALITY_GATE.md** — Record final pass status with date
5. **Mark chapter as VERIFIED** — It's now ready for integration (Phase 7 in the Process Overview)

---

## The Complete Chapter Lifecycle at a Glance

```
┌─────────────────────────────┐
│  1. LOAD CHAPTER SPEC       │  ← What must this chapter do?
│     Requirements + criteria │
└──────────┬──────────────────┘
           │
┌──────────▼──────────────────┐
│  2. DETAILED OUTLINE        │  ← Plan before writing
│     Sections + derivations  │
│     + FIGURE PLAN + problems│
└──────────┬──────────────────┘
           │
┌──────────▼──────────────────┐
│  3. WRITE THE DRAFT         │  ← Start with WHY
│     Follow the Five Laws    │
└──────────┬──────────────────┘
           │
┌──────────▼──────────────────┐
│  4. SELF-REVIEW             │  ← Author checklist
│     "But why?" test first   │
└──────────┬──────────────────┘
           │
┌──────────▼──────────────────┐
│  5. REVIEWER AGENTS         │  ← Verification
│     All assigned must PASS  │◄──── FAIL? Fix and re-run
└──────────┬──────────────────┘
           │
┌──────────▼──────────────────┐
│  6. FINALIZE                │  ← Polish + record
│     Update QUALITY_GATE.md  │
└─────────────────────────────┘
```

---

## Tips from Systems Engineering

- **Requirements are not optional.** If the chapter spec says the chapter must derive F=ma, the chapter must derive F=ma. "I'll get to it later" is a defect.
- **Test early.** If you're unsure whether a derivation works, test it before writing 10 pages around it.
- **Configuration management matters.** Don't edit a chapter that's already passed verification without re-running reviewers. That's a regression.
- **Traceability is your friend.** When a reviewer asks "why is this here?" you should be able to point to a requirement. If you can't, the content is either unnecessary or the spec is incomplete.

---

*This process ensures every chapter is requirements-driven, reviewed by multiple perspectives, and verified before integration. No chapter enters the manuscript without earning its place.*
