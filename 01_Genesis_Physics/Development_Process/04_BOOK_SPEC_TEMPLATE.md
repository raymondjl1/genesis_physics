# Book Spec — [Book/Volume Title]

**Series:** Genesis Physics Series
**Product:** [e.g., Foundations Vol 1: Architecture of Reality]
**Date Created:** [Date]
**Status:** DRAFT | CHAPTERS ALLOCATED | WRITING | INTEGRATION | VALIDATION | PRODUCTION | PUBLISHED

---

## Mission Statement

*One sentence: What is this book FOR?*

> [e.g., "This volume establishes the mathematical foundations of zone architecture so the reader can derive all of physics from six axioms."]

---

## Target Audience

*One persona: WHO reads this?*

**Name:** [Persona name]
**Background:** [Education, interests, what they already know]
**Goal:** [What they want to get from this book]
**Tolerance:** [Math level, reading level, how much effort they'll invest]

---

## Success Criteria

*How do we know this book WORKED? Measurable outcomes.*

| # | Criterion | How to Measure | Target |
|---|----------|---------------|--------|
| 1 | [e.g., Reader can derive F=ma from axioms] | [e.g., Give to grad student, ask them to derive it] | [e.g., Successful derivation without referencing the book] |
| 2 | [Criterion] | [Measurement] | [Target] |
| 3 | [Criterion] | [Measurement] | [Target] |

---

## Content Requirements

*WHAT topics must be covered? What's in scope, what's out?*

### In Scope

| Req ID | Requirement | Rationale | Priority |
|--------|------------|-----------|----------|
| BK-001 | [Topic/deliverable] | [Why this must be in the book] | P0 / P1 / P2 |
| BK-002 | [Topic/deliverable] | [Why] | P0 / P1 / P2 |

*P0 = Must have (book fails without it). P1 = Should have (significant gap if missing). P2 = Nice to have.*

### Out of Scope

- [Topic explicitly NOT covered in this book, and why]
- [Topic deferred to another book/volume, with reference]

---

## Quality Requirements

*Which requirements from `Quality_Control/01_REQUIREMENTS.md` apply to this product?*

| Req ID | Requirement | How This Book Satisfies It |
|--------|------------|--------------------------|
| WHY-001 | [From Analysis requirements] | [Specific approach in this book] |
| MATH-003 | [From Analysis requirements] | [Specific approach] |

*List every applicable requirement ID. This is the traceability link between the Analysis system and this book.*

---

## Constraints

| Constraint | Value | Rationale |
|-----------|-------|-----------|
| Word count target | [e.g., 90,000–120,000 words] | [Based on audience tolerance and content needs] |
| Reading level | [e.g., Graduate physics / Intelligent layperson] | [Matches target audience] |
| Equations | [Yes/No — if yes, density: light/moderate/heavy] | [Product requirement] |
| Target price (Kindle) | [e.g., $9.99] | [Market positioning] |
| Target price (paperback) | [e.g., $34.99] | [Print cost + margin] |
| Target price (hardcover) | [e.g., $49.99] | [Premium positioning] |
| Trim size | [e.g., 6×9 or 7×10] | [Standard for genre/audience] |
| Audiobook | [Yes/No] | [Suitable for audio format?] |

---

## Dependencies

*What must exist BEFORE this book can be written?*

| Dependency | Required For | Status |
|-----------|-------------|--------|
| [e.g., Foundations Vols 1-5 complete] | [Content this book references] | NOT MET / MET |
| [e.g., Series Bible notation standard] | [Consistent symbols] | NOT MET / MET |

---

## Chapter Architecture

*How book requirements are allocated to chapters. Every book requirement must map to at least one chapter. No chapter exists without a requirement to fulfill.*

### Chapter List

| Ch | Working Title | Primary Requirements | Pages (est.) |
|----|-------------|---------------------|-------------|
| 1 | [Title] | BK-001, BK-002 | [est.] |
| 2 | [Title] | BK-003 | [est.] |
| 3 | [Title] | BK-004, BK-005 | [est.] |

### Traceability Matrix

| Req ID | Ch 1 | Ch 2 | Ch 3 | Ch 4 | ... |
|--------|------|------|------|------|-----|
| BK-001 | ✓ | | | | |
| BK-002 | ✓ | | ✓ | | |
| BK-003 | | ✓ | | | |

*Every requirement must have at least one ✓. Every chapter must have at least one ✓. Nothing unallocated. Nothing orphaned.*

---

## Assigned Reviewers

*From `Quality_Control/02_VALIDATION_PLAN.md` — which reviewer agents are assigned to this product?*

| Reviewer | Assigned | Mandate |
|----------|----------|---------|
| The Physicist | YES/NO | [One-line: what they check] |
| But Why? Reader | YES/NO | [What they check] |
| Writing Coach | YES/NO | [What they check] |
| Consistency Auditor | YES/NO | [What they check] |
| Homeschool Mom | YES/NO | [What they check] |
| The Skeptic | YES/NO | [What they check] |
| The Student | YES/NO | [What they check] |

---

## Validation Plan

*This is the book-level test — Phase 8 in the Process Overview. After the entire book is assembled, how do we test whether it accomplishes its mission?*

### The Ultimate Test

*Describe the real-world validation test for this book:*

> [e.g., "Give this volume to a physics grad student who has completed Vols 1-4. Ask them to derive the Einstein field equations from the axioms in Vol 1. If they can do it — understanding each step and WHY — this volume passes. If they're stuck or confused, it fails."]

### Validation Checks

| # | Test | Pass Criteria | Method |
|---|------|-------------|--------|
| 1 | [e.g., Derivation completeness] | [e.g., All derivations reproducible from stated starting points] | [e.g., Independent derivation by reviewer] |
| 2 | [e.g., "Why" coverage] | [e.g., No "but why?" goes unanswered] | [e.g., But Why? Reader full-book pass] |
| 3 | [e.g., Cascade verification] | [e.g., Every claim traces to prior volume] | [e.g., Consistency Auditor cross-reference check] |

### Cross-Product Cascade

*How this book connects to the rest of the series:*

| Direction | Relationship |
|-----------|-------------|
| **This book depends on:** | [Which books/volumes must be complete first] |
| **These books depend on this:** | [Which books/volumes reference this one] |
| **Cascade rule:** | [e.g., Every claim in Book 2 must trace to a derivation in Book 1] |

---

## Risk Register

*What could go wrong with this specific book?*

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| [e.g., Particle mass calculations don't match observation] | [H/M/L] | [H/M/L] | [e.g., Honest acknowledgment + identify what's needed to fix] |
| [Risk] | [L] | [L] | [Mitigation] |

---

## Timeline

| Milestone | Target Date | Status |
|-----------|------------|--------|
| Book spec complete | [Date] | |
| Chapter specs complete | [Date] | |
| First draft complete | [Date] | |
| All chapters verified | [Date] | |
| Integration complete | [Date] | |
| Validation passed | [Date] | |
| Production complete | [Date] | |
| Launch | [Date] | |

---

## Notes

*Any additional context, open questions, or decisions to record about this book.*

- [Note 1]
- [Note 2]

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| [Date] | Initial spec created | — |

---

*Template source: `Development_Process/04_BOOK_SPEC_TEMPLATE.md`. Copy this file to `[Book]/BOOK_SPEC.md` and fill in for each book or volume.*
