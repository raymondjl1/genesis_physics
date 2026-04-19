# Genesis Physics — Book Development Process

**Date:** April 5, 2026
**Author:** Jeff Raymond
**Philosophy:** Treat book development the way you'd treat a systems engineering program — requirements-driven, verification at every level, validation at the end.

---

## How to Read This Folder

This folder defines the end-to-end process for developing any book or volume in the Genesis Physics Series, from initial requirements through Amazon publication.

| Document | What It Covers |
|----------|---------------|
| **00_PROCESS_OVERVIEW.md** | You're reading it. The SE lifecycle mapped to book writing. |
| **01_WRITING_PROCESS.md** | The chapter-level workflow: requirements → draft → verify → revise → done. |
| **02_PRODUCTION_PIPELINE.md** | From finished manuscript to published on Amazon: formatting, proofs, Kindle, print, Audible. |
| **03_CHAPTER_SPEC_TEMPLATE.md** | Copy this template for every chapter. Fill in requirements, verification criteria. |
| **04_BOOK_SPEC_TEMPLATE.md** | Copy this template for every book/volume. Fill in book-level requirements, validation plan. |

---

## The SE Lifecycle Applied to Books

In systems engineering, you go through distinct phases. Here's how they map to writing a book:

```
SE Phase              │  Book Equivalent                │  Output
──────────────────────┼─────────────────────────────────┼──────────────────────
1. ConOps             │  Series Vision                  │  00_SERIES_VISION.md
2. System Requirements│  Book Requirements              │  BOOK_SPEC.md (per book)
3. Architecture       │  Chapter Outline & Allocation   │  Chapter list + CHAPTER_SPEC.md per chapter
4. Detailed Design    │  Chapter Drafting               │  Manuscript/ chapter files
5. Implementation     │  Writing + Equations + Figures   │  Draft chapters
6. Verification       │  Chapter Review (reviewer agents)│  QUALITY_GATE.md scorecards
7. Integration        │  Volume Assembly                │  Complete manuscript
8. Validation         │  Book-Level Testing             │  Does the book accomplish its goals?
9. Production         │  Formatting + Publishing        │  KDP, Kindle, proof copies, Audible
10. Deployment        │  Amazon Launch                  │  Live on Amazon
```

---

## Phase 1: Concept of Operations (Already Complete)

**Input:** The idea — "What if Genesis 1 is physics?"
**Output:** `Quality_Control/00_SERIES_VISION.md`

This is already done. The Vision document defines what we're building, why, for whom, and what "done" looks like. It also establishes the seven Governing Principles (Always Answer Why, Build Bottom-Up, No Rewrites, Honest About Limits, Scripture Without Apology, One Voice Per Product, Accessibility Required).

---

## Phase 2: System (Book) Requirements

**Input:** Vision + Analysis Findings
**Output:** One `BOOK_SPEC.md` per book/volume (use `04_BOOK_SPEC_TEMPLATE.md`)

Before writing a single word, define what the book must accomplish. This is the "requirements document" for the book. It includes:

- **Mission statement:** What is this book FOR? One sentence.
- **Target audience:** WHO reads this? One persona.
- **Success criteria:** How do we know this book WORKED? Measurable outcomes.
- **Content requirements:** WHAT topics must be covered? What's in scope, what's out?
- **Quality requirements:** Pulled from `Quality_Control/01_REQUIREMENTS.md` — which specific requirement IDs apply?
- **Constraints:** Word count target, reading level, equations yes/no, price point.
- **Dependencies:** What must exist BEFORE this book can be written? (For Book 1: Foundations complete. For Book 2: Book 1 complete. Etc.)

**Validation plan:** This is the book-level test. After the entire book is assembled, how do we test whether it accomplishes its mission? (See the BOOK_SPEC_TEMPLATE for details.)

---

## Phase 3: Architecture (Chapter Outline & Allocation)

**Input:** Book Requirements
**Output:** Chapter list + one `CHAPTER_SPEC.md` per chapter (use `03_CHAPTER_SPEC_TEMPLATE.md`)

This is where book requirements get **allocated** to chapters — just like system requirements get allocated to subsystems. Every book requirement must be traceable to at least one chapter. No chapter exists without a requirement it's fulfilling.

For each chapter, define:

- **Chapter requirements:** What must this chapter accomplish? What concepts must it introduce?
- **Prerequisites:** What must the reader already know? (From which prior chapters?)
- **Key deliverables:** Specific derivations, explanations, analogies, or scripture passages.
- **"Why" chain:** What "but why?" questions does this chapter answer?
- **Verification criteria:** How do we know this chapter is DONE? (Specific reviewer agent checks.)

**The traceability matrix:** Every book requirement maps to chapters. Every chapter requirement traces back to a book requirement. Nothing unallocated. Nothing orphaned.

---

## Phase 4: Detailed Design (Chapter Planning)

**Input:** Chapter spec
**Output:** Detailed chapter outline (section-by-section)

Before writing, plan each chapter at the section level:

- Section outline with topic sentences
- Derivation plan (for Foundations): which equations, in what order, from what starting point
- Figure/diagram plan: what visuals are needed and where
- Problem set plan (for Foundations): how many problems, what types, what difficulty range
- Scripture plan (for The Creator's Blueprint): which passages, how introduced, discussion questions

This is like a detailed design review in SE — you review the plan before building.

---

## Phase 5: Implementation (Writing)

**Input:** Detailed chapter outline
**Output:** Draft chapter in `Manuscript/` folder

Write the chapter following the process in `01_WRITING_PROCESS.md`. Key principles:

- **Start with WHY.** Before introducing any concept, explain why it matters and why it must be true.
- **Physical intuition before math.** The reader should predict the result before seeing the derivation.
- **One voice.** Stay in the product's register throughout. Don't slip.
- **No forward dependencies.** Don't use concepts that haven't been established yet.
- **Mark uncertainty.** If something is an open problem, say so explicitly.

---

## Phase 6: Verification (Chapter Review)

**Input:** Draft chapter
**Output:** Reviewer scorecards (PASS/FAIL per agent)

Run the chapter through its assigned reviewer agents (defined in `Quality_Control/Reviewers/`). Each product has a specific set of assigned reviewers (defined in the product's `QUALITY_GATE.md`).

**Process:**
1. Load the relevant reviewer agent definitions
2. Run each reviewer against the chapter
3. Collect scorecards
4. Address all FAIL items
5. Re-run until all PASS
6. Update the `QUALITY_GATE.md` validation status table

**This is the verification step** — "Did we build the chapter right?" It checks that the chapter meets its own spec.

---

## Phase 7: Integration (Volume/Book Assembly)

**Input:** All verified chapters
**Output:** Complete manuscript

Once all chapters pass verification individually, assemble them into the complete book/volume and run **cross-chapter checks** (Level 2 validation from `Quality_Control/02_VALIDATION_PLAN.md`):

- Dependency audit (no forward references)
- Notation audit (consistent symbols)
- Cumulative "why" test (read front-to-back as a learner)
- Problem set coherence (no problems requiring uncovered material)
- Readability consistency (no outlier chapters)
- Bibliography completeness (every claim cited)

Add front matter (title page, copyright, table of contents, preface) and back matter (glossary, bibliography, index, appendices, problem solutions).

---

## Phase 8: Validation (Book-Level Testing)

**Input:** Complete assembled manuscript
**Output:** Validation report — PASS or FAIL

**This is the validation step** — "Did we build the RIGHT book?" It tests whether the book accomplishes its mission as defined in the BOOK_SPEC.md.

Validation tests (from the BOOK_SPEC for each product):

- **Foundations:** Give it to a grad student. Can they derive F=ma from axioms? Can they do the problem sets? Do they understand WHY?
- **Book 1:** Give it to a physicist. Can they evaluate the framework? Do they take it seriously? Is the comparison with standard physics fair?
- **Book 2:** Give it to an intelligent friend who hates math. Can they explain zone architecture? Do they want to read more?
- **The Creator's Blueprint:** Give it to a homeschool parent. Can they teach from it? Do they feel more confident?

Also run the cascade verification:
- Every claim in Book 2 traces to Book 1
- Every claim in Book 1 traces to Foundations
- Every claim in The Creator's Blueprint traces to Book 2

---

## Phase 9: Production (Formatting & Publishing)

**Input:** Validated manuscript
**Output:** Publication-ready files in all formats

This is the manufacturing phase. Detailed in `02_PRODUCTION_PIPELINE.md`. Summary:

```
Validated Manuscript
    │
    ├──→ Interior Formatting (LaTeX or Vellum/InDesign)
    │       ├── Print-ready PDF (paperback)
    │       ├── Print-ready PDF (hardcover)
    │       └── EPUB (Kindle)
    │
    ├──→ Cover Design (professional designer)
    │       ├── Paperback cover (KDP template)
    │       ├── Hardcover cover (case-laminate template)
    │       └── Kindle cover (2560×1600px)
    │
    ├──→ Proof Copies (KDP)
    │       ├── Order up to 5 proof copies
    │       ├── Jeff reads and redlines hardcopy
    │       └── Incorporate redline edits
    │
    ├──→ Professional Copyedit
    │       └── Final polish before publication
    │
    ├──→ Kindle Upload (KDP)
    │       └── EPUB → Live on Kindle within 72 hours
    │
    ├──→ Paperback Upload (KDP Print-on-Demand)
    │       └── PDF → Live on Amazon. No inventory.
    │
    ├──→ Hardcover Upload (KDP Print-on-Demand)
    │       └── PDF → Live on Amazon. No inventory.
    │
    └──→ Audiobook Production (ACX) [Book 2 + The Creator's Blueprint]
            ├── Hire narrator via ACX marketplace
            ├── Record, edit, master to ACX specs
            └── Live on Audible within weeks of approval
```

---

## Phase 10: Deployment (Amazon Launch)

**Input:** All files uploaded, proofs approved
**Output:** Live product on Amazon

Launch checklist:
- [ ] Kindle ebook live
- [ ] Paperback live (print-on-demand — no inventory)
- [ ] Hardcover live (print-on-demand — no inventory)
- [ ] Author copies ordered (at print cost — for Jeff's personal copies)
- [ ] Audiobook live on Audible (Book 2 + The Creator's Blueprint)
- [ ] Amazon categories and keywords set
- [ ] A+ Content (Enhanced Brand Content) created for product page
- [ ] Launch email sent to subscriber list

---

## The Full Lifecycle at a Glance

```
                    ┌─────────────────────────────┐
                    │  1. VISION (ConOps)          │  ← Already complete
                    │     00_SERIES_VISION.md      │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  2. BOOK REQUIREMENTS        │  ← BOOK_SPEC.md per book
                    │     What must this book do?  │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  3. CHAPTER ARCHITECTURE     │  ← CHAPTER_SPEC.md per chapter
                    │     Allocate reqs to chapters│
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  4. DETAILED DESIGN          │  ← Section-level outline
                    │     Plan before writing      │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  5. WRITING                  │  ← Draft in Manuscript/
                    │     Start with WHY           │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  6. VERIFICATION             │  ← Reviewer agent scorecards
                    │     Did we build it right?   │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  7. INTEGRATION              │  ← Assemble + cross-chapter checks
                    │     Combine into manuscript  │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  8. VALIDATION               │  ← Does the book work?
                    │     Did we build the right   │
                    │     thing?                   │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  9. PRODUCTION               │  ← Format, proof, copyedit
                    │     Prepare for publication  │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  10. LAUNCH                  │  ← Live on Amazon
                    │     Kindle + Print + Audible │
                    └─────────────────────────────┘
```

---

## Where the Documents Live

| Document | Location | Purpose |
|----------|----------|---------|
| Vision | `Quality_Control/00_SERIES_VISION.md` | North Star — what and why |
| Series Requirements | `Quality_Control/01_REQUIREMENTS.md` | All requirements across the series |
| Validation Plan | `Quality_Control/02_VALIDATION_PLAN.md` | How to test everything |
| Strategy | `Quality_Control/BOOK_SERIES_STRATEGY.md` | Chapter outlines, timelines, content plan |
| Reviewer Agents | `Quality_Control/Reviewers/` | The test runners |
| Book Spec (per book) | `Book_X/BOOK_SPEC.md` | Book requirements + validation plan |
| Chapter Spec (per chapter) | `Book_X/Manuscript/ChXX_SPEC.md` | Chapter requirements + verification criteria |
| Quality Gate (per book) | `Book_X/QUALITY_GATE.md` | Scorecard tracking pass/fail |
| **This Process** | `Development_Process/` | How to do all of the above |

---

*This process is inspired by systems engineering lifecycle models (IEEE 15288, Vee Model) adapted for book development. The core insight: verification asks "did we build it right?" and validation asks "did we build the right thing?" Both must pass before publication.*
