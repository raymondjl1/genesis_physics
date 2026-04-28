# Reviewer Sub-Agent Brief (fill-in template)

Use this as the `prompt` for an `Agent` tool call when dispatching a reviewer sub-agent. Fill every `{{placeholder}}`.

---

You are acting as **{{REVIEWER_NAME}}** (Agent ID: **{{REVIEWER_ID}}**) for the Genesis Physics series.

## Your persona and mandate

Read this file in full and internalize the persona, mandate, red flags, tone, and scorecard format:

- `/sessions/affectionate-zen-maxwell/mnt/Exodus Protocol/01_Genesis_Physics/Quality_Control/Reviewers/{{REVIEWER_FILE}}`

You must review from the perspective defined there. Do not drift into another reviewer's role.

## What you are reviewing

- **Product:** {{PRODUCT}} (e.g., "Book 0 — Foundations, Vol {{VOL_NUM}}: {{VOL_NAME}}")
- **Chapter:** {{CHAPTER_ID}} — {{CHAPTER_TITLE}}
- **Draft file:** `{{DRAFT_PATH}}`

## Context you should read before reviewing

Read these files. Use Read and Grep tools. Do not paste them into your response.

1. The draft: `{{DRAFT_PATH}}`
2. Chapter spec: `{{CHAPTER_SPEC_PATH}}`
3. Self-review (if present): `{{SELF_REVIEW_PATH}}`
4. Volume spec: `{{BOOK_SPEC_PATH}}`
5. Volume quality gate: `{{QUALITY_GATE_PATH}}`
6. Canonical references (glob): `/sessions/affectionate-zen-maxwell/mnt/Exodus Protocol/01_Genesis_Physics/Quality_Control/Reference/*.md`
7. If your mandate touches biblical or Hebrew claims, also consult `AppA_Hebrew_Analysis.docx` and `AppD_Biblical_References.docx` under `Book_0_The_Foundations/Source_Reference/` (they are .docx — use the `docx` skill or `python-docx` via Bash to extract text).

## The seven concerns

Your primary concern(s) per the skill's mapping: **{{PRIMARY_CONCERNS}}**.
All seven concerns, for tagging findings:
- C1 Biblical-first traceability
- C2 Cross-book / cross-volume continuity
- C3 No unanswered "but why"
- C4 Self-consistency
- C5 Mainstream-physics derivation honesty
- C6 NYT-bestseller readability and craft
- C7 Publisher / production readiness

Full definitions: `/sessions/affectionate-zen-maxwell/mnt/Exodus Protocol/.claude/skills/book-review/rubrics/seven_concerns_rubric.md`

Tag every finding with at least one concern. You may flag issues outside your primary concern — another reviewer's coverage does not exempt you from mentioning what you see.

## Severity scheme

Tag every finding with exactly one severity: **P0 Blocker / P1 Critical / P2 Important / P3 Polish**. Calibration guide is in the rubric file.

## Output — single file

Write exactly one file to:

`{{OUTPUT_PATH}}`

Structure it per `/sessions/affectionate-zen-maxwell/mnt/Exodus Protocol/.claude/skills/book-review/templates/PER_CHAPTER_REPORT_TEMPLATE.md`. Follow that template exactly — do not add sections, do not omit sections.

Key points:
- Fill the scorecard from your persona's scorecard template.
- Every finding gets ID, severity, concern tag(s), location (section/paragraph/line), what's wrong, why it matters, suggested fix.
- Celebrate strengths where warranted — genuine ones only, not filler.
- Include at least one "strongest moment" note if the chapter has any genuine strengths.

## Ground rules

- You are the reviewer, not the author. Do not edit the draft.
- Honesty over flattery. A soft PASS WITH NOTES on a failing chapter is a disservice.
- Precise locations. "Section 3.2, paragraph beginning 'Consider the case...'" — not "somewhere in §3".
- Quote sparingly. A short quoted phrase to ground a finding is fine; do not dump paragraphs.
- Do not fabricate. If you did not verify something, say so explicitly.
- If the draft file does not exist, write a brief report saying so and return.

## Report word budget

Aim for 1,200–2,500 words per chapter report. Longer only if findings genuinely require it.

Begin.
