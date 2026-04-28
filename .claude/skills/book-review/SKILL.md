---
name: book-review
description: Comprehensive, multi-reviewer book review process for the Genesis Physics series. Runs 12 reviewer personas as parallel sub-agents across chapters and volumes, produces per-chapter reports and a master rollup organized by Jeff's 7 concerns (biblical-first traceability, cross-book continuity, no unanswered "but why," self-consistency, derivation honesty, NYT-bestseller craft, and publisher readiness). Use when: review book, review chapter, review volume, QC pass, pre-publication audit, book review, full-book review, review manuscript.
---

# Book Review Skill — Genesis Physics Series

This skill turns the 12 reviewer personas in `Quality_Control/Reviewers/` into an executable, parallelizable review pipeline. It is built around Jeff Raymond's seven review concerns and the existing Quality Control infrastructure (CHAPTER_SPEC, SELF_REVIEW_REPORT, QUALITY_GATE).

---

## When to use this skill

Invoke this skill when the user asks to:
- Review a chapter, volume, or the entire book
- Run a QC pass, pre-publication audit, or "all reviewers" against a draft
- Generate per-chapter reports and a master rollup
- Check traceability, consistency, or derivation honesty across the manuscript

---

## Inputs required before running

Before starting a review run, confirm with the user:

1. **Scope:** single chapter, whole volume, or whole book
2. **Target draft(s):** which `Ch*_DRAFT.md` files (or `Source_Reference/*.docx` for appendices)
3. **Reviewer set:** default is all 12 reviewers; the user may restrict (e.g., "just REVIEWER-02 and REVIEWER-11 this pass")
4. **Output location:** default is `01_Genesis_Physics/Quality_Control/Reviews/Book_0/<Vol>/<Ch>/`
5. **Parallelism:** default runs reviewers in parallel per chapter; chapters run in parallel up to 4 at a time to avoid overwhelming context

If the user hasn't specified, use the `AskUserQuestion` tool.

---

## The 7 concerns → reviewer mapping

Every run must explicitly cover these seven concerns. If the user restricts the reviewer set, warn which concerns become uncovered.

| # | Concern | Primary reviewer(s) | Supporting |
|---|---------|---------------------|------------|
| C1 | Biblical-first traceability (every main claim to a biblical truth; every subsequent claim to a parent or biblical truth) | **REVIEWER-11** (Biblical Traceability Auditor) | REVIEWER-09 (Theologian), REVIEWER-02 (But Why) |
| C2 | Cross-book / cross-volume continuity | **REVIEWER-10** (Navigator) | REVIEWER-04 (Consistency Auditor) |
| C3 | No unanswered "but why" | **REVIEWER-02** (But Why Reader) | REVIEWER-07 (Student) |
| C4 | Self-consistency, no contradictions | **REVIEWER-04** (Consistency Auditor) | REVIEWER-01 (Physicist), REVIEWER-10 |
| C5 | Mainstream-physics derivation honesty — no cheating | **REVIEWER-01** (Physicist), **REVIEWER-06** (Skeptic) | REVIEWER-07 |
| C6 | NYT-bestseller readability and authorship craft | **REVIEWER-03** (Writing Coach) | REVIEWER-05 (Homeschool Mom), REVIEWER-08 (Style Editor) |
| C7 | Publisher / production readiness | **REVIEWER-12** (Acquisitions & Production Editor) | REVIEWER-08 |

Full rubric details are in `rubrics/seven_concerns_rubric.md`.

---

## Pipeline: per-chapter review

For each target chapter, the skill executes this pipeline:

### Step 1 — Context pack

Build a context pack the reviewer sub-agents will read. Do not load it into the main agent's context; sub-agents will read files directly. The context pack is a list of paths:

- The draft file (`Ch*_DRAFT.md`)
- The chapter's `CHAPTER_SPEC.md`
- The chapter's `SELF_REVIEW_REPORT.md` (if present)
- The volume's `BOOK_SPEC.md` and `QUALITY_GATE.md`
- `01_Genesis_Physics/Quality_Control/Reference/` (all canonical references)
- `Source_Reference/AppA_Hebrew_Analysis.docx`, `AppD_Biblical_References.docx` (for biblical/Hebrew anchors)
- The reviewer persona file (`REVIEWER_NN_*.md`)

### Step 2 — Parallel reviewer sub-agents

Launch reviewer sub-agents in parallel (single message, multiple `Agent` calls). Each sub-agent receives:

- The REVIEWER_BRIEF template (`templates/REVIEWER_BRIEF_TEMPLATE.md`) filled with the chapter identifier, the context pack paths, and the reviewer's persona file
- Instructions to produce a single markdown file conforming to `templates/PER_CHAPTER_REPORT_TEMPLATE.md`
- Output path: `Quality_Control/Reviews/Book_0/<Vol>/<Ch>/REVIEWER_NN_<ChXX>_<Reviewer>.md`

Use `subagent_type: "general-purpose"` for reviewers that need to read many files, or `subagent_type: "Explore"` for reviewers whose job is mostly searching/reading.

### Step 3 — Chapter rollup

After all reviewer sub-agents complete, run the **chapter rollup** sub-agent. Inputs: all per-reviewer reports for the chapter. Output: a single `CHAPTER_ROLLUP.md` at `Quality_Control/Reviews/Book_0/<Vol>/<Ch>/` using `templates/CHAPTER_ROLLUP_TEMPLATE.md`.

The chapter rollup must:
- Aggregate findings by **severity** (P0 blocker / P1 critical / P2 important / P3 polish)
- Aggregate findings by **concern** (C1–C7)
- Deduplicate issues raised by multiple reviewers
- Produce a single verdict: PASS / PASS WITH NOTES / FAIL
- Produce a ranked next-actions list

### Step 4 — Volume and book rollups

Once all chapters in a volume are reviewed, produce `VOLUME_ROLLUP.md` (same structure, one level up). Once all volumes are done, produce `BOOK_ROLLUP.md`. Use `templates/MASTER_ROLLUP_TEMPLATE.md`.

---

## Severity scheme

Every finding in every report must carry exactly one severity:

- **P0 (Blocker):** publication-stopping. A red-flag automatic-FAIL item from any reviewer. Cross-reference broken, decorative verse pretending to be derivational, contradiction between chapters, fabricated physics claim, forward dependency.
- **P1 (Critical):** must-fix before series ships. Weakens the argument or the credibility. Missing "why" on a main claim, unclear derivation step, weak biblical anchor, production readiness gap.
- **P2 (Important):** should-fix for quality. Unclear prose, minor notation drift, figure needs work, weak comp title.
- **P3 (Polish):** nice-to-have. Word choice, rhythm, typography.

---

## Concern tagging

Every finding must carry at least one concern tag (C1–C7). The chapter rollup groups by concern so Jeff can see at a glance which concerns are healthiest and which are weakest across chapters.

---

## Output directory structure

```
Quality_Control/Reviews/Book_0/
├── BOOK_ROLLUP.md
├── Vol_1_Architecture_of_Reality/
│   ├── VOLUME_ROLLUP.md
│   ├── Ch_01_Axioms_and_Definitions/
│   │   ├── CHAPTER_ROLLUP.md
│   │   ├── REVIEWER_01_Ch01_Physicist.md
│   │   ├── REVIEWER_02_Ch01_But_Why.md
│   │   ├── ... (one per reviewer)
│   │   └── REVIEWER_12_Ch01_Acquisitions.md
│   └── Ch_02_.../
└── Vol_2_.../
```

---

## Execution checklist (use TaskCreate)

For any run, the main agent should create a task list that mirrors this:

1. Confirm scope and inputs with the user (AskUserQuestion)
2. Inventory target chapters + verify drafts exist
3. For each chapter, in batches of up to 4 parallel chapters:
   a. Launch reviewer sub-agents in parallel
   b. Launch chapter rollup sub-agent
4. Launch volume rollup sub-agents (one per volume touched)
5. Launch the book rollup sub-agent
6. Deliver paths to all rollups to the user, highlight P0 blockers

---

## Principles

- **Sub-agents read files directly.** Do not paste drafts into sub-agent prompts. Give paths.
- **One sub-agent = one reviewer + one chapter.** Do not batch reviewers into a single sub-agent; that dilutes persona fidelity.
- **Rollups are separate sub-agents.** They do not review — they aggregate. Keep the jobs distinct.
- **Every finding has severity + concern tags.** No exceptions.
- **Respect Jeff's biblical rule precisely:** Every main claim to a biblical truth; every subsequent claim to a parent or biblical truth. REVIEWER-11 is the guardian of this rule.
- **Honesty over flattery.** Reports should celebrate strengths (REVIEWER-02 explicitly calls for this) but must not soften a FAIL into a PASS WITH NOTES.

---

## Files in this skill

- `SKILL.md` — this file
- `rubrics/seven_concerns_rubric.md` — detailed pass/fail criteria per concern
- `templates/REVIEWER_BRIEF_TEMPLATE.md` — sub-agent prompt template
- `templates/PER_CHAPTER_REPORT_TEMPLATE.md` — reviewer output format
- `templates/CHAPTER_ROLLUP_TEMPLATE.md` — per-chapter aggregation format
- `templates/MASTER_ROLLUP_TEMPLATE.md` — volume/book aggregation format
- `runbook.md` — step-by-step invocation for common scenarios
