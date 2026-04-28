# Book Review — Runbook

Common invocations for the `book-review` skill. Follow these step-by-step.

---

## Prerequisites

Confirm the user has:
- A target draft or set of drafts (`Ch*_DRAFT.md` or `Source_Reference/*.docx` for appendices)
- A destination for output reports (default `Quality_Control/Reviews/Book_0/`)

If anything is unclear, use `AskUserQuestion` before launching sub-agents. Review runs are expensive — confirm before spending context.

---

## Scenario A — Single chapter, all 12 reviewers

1. Create tasks:
   - "Inventory context pack for ChXX"
   - "Dispatch 12 reviewer sub-agents for ChXX"
   - "Build chapter rollup for ChXX"
2. Inventory context pack using Glob/Read. Confirm:
   - Draft exists
   - CHAPTER_SPEC.md exists
   - SELF_REVIEW_REPORT.md (note if missing)
   - Volume's BOOK_SPEC.md and QUALITY_GATE.md
3. Dispatch **12 reviewer sub-agents in a single message** (single `Agent` message with 12 tool blocks). Each sub-agent receives a filled `REVIEWER_BRIEF_TEMPLATE.md` prompt. Output file paths are pre-assigned.
4. Wait for all 12 to return. Check that all 12 output files now exist. If any sub-agent failed or produced a malformed report, re-dispatch it.
5. Dispatch one **rollup sub-agent**. It reads all 12 reports and produces `CHAPTER_ROLLUP.md` following `CHAPTER_ROLLUP_TEMPLATE.md`.
6. Summarize for the user: verdict, P0 count, link to rollup.

Budget: ~15–25 minutes wall-clock; high context consumption.

---

## Scenario B — Single volume, all chapters

1. Create a task per chapter plus a volume rollup task.
2. Execute Scenario A for each chapter, **batched 4 chapters at a time** to avoid context pressure. Pattern:
   - Start chapters 1–4 in parallel (each chapter dispatches its own 12 reviewers; so 48 sub-agents run concurrently — acceptable, but watch context usage).
   - When all four chapter rollups are complete, start chapters 5–8.
   - Continue until the volume is done.
3. Dispatch the **volume rollup sub-agent**. Inputs: all chapter rollups in the volume. Output: `VOLUME_ROLLUP.md` at the volume level.
4. Deliver to user.

Budget: hours for a full volume. Consider running overnight via the `schedule` skill if available.

---

## Scenario C — Full Book 0 pass

1. Execute Scenario B for each of the 6 volumes.
2. Dispatch the **book rollup sub-agent**. Inputs: all 6 volume rollups. Output: `BOOK_ROLLUP.md`.
3. Deliver.

---

## Scenario D — Appendix review

Appendices are .docx, not markdown. Before dispatching reviewers:

1. Convert the target appendix to markdown using the `docx` skill (or `python-docx` via Bash) into a temporary file under `/sessions/affectionate-zen-maxwell/`.
2. Use that temporary .md as the "draft" for reviewer sub-agents.
3. Note in the chapter rollup that the source is .docx, so any formatting findings should be verified against the .docx original before acting.

REVIEWER-11 (Biblical Traceability) and REVIEWER-09 (Theologian) are especially important for AppA and AppD. REVIEWER-12 (Acquisitions) is critical for AppC (Glossary) completeness.

---

## Scenario E — Targeted re-review after revisions

1. User identifies a changed chapter and the reviewer(s) whose earlier findings may have been addressed.
2. Dispatch only those reviewers (not all 12) with a brief that includes the prior report as a context file.
3. The reviewer's task is to verify whether prior findings are resolved and to flag any new issues.
4. Update the chapter rollup in place (overwrite with a new version).

---

## Sub-agent selection guidance

- **general-purpose** for reviewers whose work spans many files and cross-references (REVIEWER-04, REVIEWER-10, REVIEWER-11, REVIEWER-12).
- **Explore** for reviewers whose work is mostly focused reading and quoting (REVIEWER-02, REVIEWER-03, REVIEWER-07).
- **Plan** for the rollup sub-agents (they synthesize, they don't edit).
- **general-purpose** for REVIEWER-01 (Physicist) and REVIEWER-06 (Skeptic) because they often need to run calculations or check derivations with Bash.

---

## Failure modes and how to handle them

- **Sub-agent returns a malformed report (wrong template).** Re-dispatch with an explicit "your prior output did not follow the template; redo to match exactly" prompt.
- **Sub-agent's review is shallow or generic.** Re-dispatch with specific pointers to the places it skipped.
- **Reviewer persona drift** (reviewer adopts another reviewer's voice). Re-dispatch with the persona file path re-emphasized.
- **Draft file missing.** Do not invent review content. The reviewer writes a one-paragraph report saying the draft does not exist and the reviewer cannot proceed.
- **Context too large for a sub-agent.** Split the chapter review by concern: dispatch the reviewer twice, once on concerns A/B and once on concerns C/D, and concatenate.

---

## What not to do

- Do not batch multiple reviewers into a single sub-agent. Persona fidelity collapses.
- Do not paste draft text into sub-agent prompts. Use paths.
- Do not have the main agent do the reviewing. It should only orchestrate.
- Do not overwrite existing `SELF_REVIEW_REPORT.md`. Reviewer output goes under `Quality_Control/Reviews/`, not next to the draft.
- Do not skip the rollup. The rollup is where dedup and cross-reviewer synthesis happen — without it, the user is left with 12 un-synthesized reports per chapter.
