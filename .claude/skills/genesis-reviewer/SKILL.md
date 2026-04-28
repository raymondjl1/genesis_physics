---
name: genesis-reviewer
description: Run Genesis Physics reviewer agents against a chapter draft. Evaluates chapter quality using the 10 reviewer personas (Physicist, But Why? Reader, Writing Coach, Consistency Auditor, Homeschool Mom, Skeptic, Student, Style Editor, Theologian, Navigator). Produces scorecards with PASS/FAIL and specific findings. Use when reviewing, testing, validating, or QA-checking any Genesis Physics chapter.
---

# Genesis Physics Reviewer Agent Skill

Run one or more of the 10 reviewer agents against a chapter draft to validate quality.

## When to Use This Skill

- After completing a chapter draft
- When the user says "review", "test", "validate", "QA", "run reviewers", "check quality"
- When a chapter is ready for verification (Step 5 in the writing process)
- When the user wants to check a specific reviewer's perspective

## Process

### Step 1: Identify the Chapter and Product

Determine which chapter is being reviewed and which product it belongs to:
- **Foundations (any volume):** Vols 1-6 in `Book_0_The_Foundations/`
- **Book 1:** `Book_1_Hidden_Architecture/` *(Popular Science Flagship; folder renamed April 2026 from `Book_1_The_Firmament_Equations/`)*
- **Book 2:** `Book_2_The_Hidden_Architecture/`
- **The Creator's Blueprint:** `Book_3_The_Creators_Blueprint/`

### Step 2: Load Reviewer Definitions

Read the reviewer definitions from `01_Genesis_Physics/Quality_Control/Reviewers/`:

| # | File | Reviewer |
|---|------|----------|
| 01 | REVIEWER_01_The_Physicist.md | Mathematical rigor, derivation validity |
| 02 | REVIEWER_02_The_But_Why_Reader.md | **Most important.** "Why" chain complete? |
| 03 | REVIEWER_03_The_Writing_Coach.md | Prose quality, voice, readability |
| 04 | REVIEWER_04_The_Consistency_Auditor.md | Cross-references, notation |
| 05 | REVIEWER_05_The_Homeschool_Mom.md | Teachability (Creator's Blueprint only) |
| 06 | REVIEWER_06_The_Skeptic.md | Scientific credibility |
| 07 | REVIEWER_07_The_Student.md | Can student follow & reproduce? |
| 08 | REVIEWER_08_The_Style_Editor.md | Style sheet compliance, formatting |
| 09 | REVIEWER_09_The_Theologian.md | Biblical/exegetical accuracy |
| 10 | REVIEWER_10_The_Navigator.md | Cross-book depth calibration |

### Step 3: Check Reviewer Assignment

Not all reviewers apply to all products:

| Reviewer | Foundations | Book 1 | Book 2 | Creator's Blueprint |
|----------|-----------|--------|--------|-----------|
| Physicist | YES | YES | NO | NO |
| But Why? | YES | YES | YES | YES |
| Writing Coach | YES | YES | YES | YES |
| Consistency Auditor | YES | YES | YES | YES |
| Homeschool Mom | NO | NO | NO | YES |
| Skeptic | YES | YES | YES | NO |
| Student | YES | NO | NO | NO |
| Style Editor | YES | YES | YES | YES |
| Theologian | YES | YES | YES | YES |
| Navigator | YES | YES | YES | YES |

Only run assigned reviewers for the product. If the user asks for a specific reviewer not assigned to this product, run it but note it's not a required gate.

### Step 4: Run Each Reviewer

For each assigned reviewer:

1. **Read the full reviewer definition file** — understand their persona, mandate, must-check items, red flags
2. **Read the chapter** being reviewed
3. **Adopt the reviewer's persona** completely — think as they would think, check what they would check
4. **Evaluate against their scorecard template** from the definition file
5. **Check for RED FLAGS** — these are automatic FAILs defined in each reviewer's spec
6. **Produce a scorecard** with:
   - **PASS** or **FAIL**
   - Specific findings (line references where possible)
   - Red flags triggered (if any)
   - Recommendations for improvement

### Step 5: Produce Summary Report

After all reviewers have run, produce a summary:

```markdown
# Reviewer Report — [Chapter Title]

**Product:** [e.g., Foundations Vol 1]
**Chapter:** [e.g., Chapter 3: The Zone Manifold]
**Date:** [date]

## Results Summary

| Reviewer | Result | Red Flags | Key Finding |
|----------|--------|-----------|-------------|
| The Physicist | PASS/FAIL | 0 | [one-line summary] |
| But Why? Reader | PASS/FAIL | 0 | [one-line summary] |
| ... | ... | ... | ... |

**Overall: PASS / FAIL**

## Detailed Findings

### [Reviewer Name]
[Full scorecard and findings]

### [Reviewer Name]
[Full scorecard and findings]

## Action Items
1. [Specific fix needed]
2. [Specific fix needed]
```

### Step 6: Update Quality Gate

After review, update the chapter's entry in the product's `QUALITY_GATE.md` with the review results.

## Special Review Modes

### Quick Review (single reviewer)
If the user asks for a quick check or names a specific reviewer, run just that one.

### "But Why?" Audit (most common)
Run just REVIEWER_02 (But Why? Reader) — the single most important check across all products. Read every paragraph and ask "but why?" If the answer isn't on the page or in a prior chapter, it's a FAIL.

### Full Gate Review
Run ALL assigned reviewers. This is the full verification gate. Required before marking a chapter as VERIFIED.

### Cross-Chapter Review
Run the Consistency Auditor across multiple chapters to check cross-reference integrity and notation consistency.

## Important Notes

- **Be honest.** A FAIL is not a judgment — it's a quality signal. Better to catch issues now than after publication.
- **Be specific.** "Needs improvement" is useless. "Section 3.2, paragraph 4: claims F=ma without showing why — traces back to what derivation?" is useful.
- **Red flags are non-negotiable.** If a red flag is triggered, the chapter FAILS regardless of everything else.
- **The "But Why?" Reader is the most important reviewer.** If only one reviewer passes, it must be this one.
