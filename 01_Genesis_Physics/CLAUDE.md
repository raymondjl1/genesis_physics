# Genesis Physics Series — Claude Instructions

You are working on the **Genesis Physics Series**, a nonfiction physics framework derived from Genesis 1. This project builds an alternative physics framework ("zone architecture") that derives all known physics from first principles rooted in the biblical creation account. The series secretly reveals Christ as the answer through rigorous science — never through preaching.

## Core Philosophy: ALWAYS ANSWER WHY

The #1 governing principle of this entire project: **no concept is ever introduced without explaining WHY.** A reader should never think "but why?" without finding the answer on the same page or in a prior chapter. This is non-negotiable. Standard physics tells students "memorize the answer." We derive the answer from foundations so the student knows the reason.

## Project Structure

```
01_Genesis_Physics/
├── Quality_Control/           ← Requirements, validation, reviewer agents
│   ├── 00_SERIES_VISION.md   ← North Star: what we're building and why
│   ├── 01_REQUIREMENTS.md    ← 48 requirements (WHY, MATH, STRUCT, CON, PUB)
│   ├── 02_VALIDATION_PLAN.md ← 4 validation levels + 10 reviewer agents
│   ├── BOOK_SERIES_STRATEGY.md ← Detailed chapter outlines for all products
│   ├── Reviewers/            ← 10 reviewer agent definitions
│   ├── Findings/             ← Analysis findings from manuscript reviews
│   └── Reference/            ← Quick-reference cards and summaries
├── Development_Process/       ← SE lifecycle, writing process, production pipeline
├── Research/                  ← Physics derivations, models, simulations, papers
│   ├── Foundations/           ← Axioms and foundational derivations
│   ├── Mathematical_Models/   ← 10 physics domains with test suites
│   ├── Papers/               ← Research papers (docx)
│   ├── Peer_Review/          ← Critic and skeptic analysis
│   └── Simulations/          ← Computational validations
├── Book_0_The_Foundations/            ← 6-volume graduate textbook series (BUILD FIRST)
├── Book_1_The_Firmament_Equations/    ← Physicist-level monograph (BUILD 2ND)
├── Book_2_The_Hidden_Architecture/    ← Zero equations, general audience (BUILD 3RD)
└── Book_3_The_Creators_Blueprint/     ← Scripture-first, homeschool families (BUILD LAST)
```

## Build Order (STRICT)

**Book 0 (The Foundations) → Book 1 (The Firmament Equations) → Book 2 (The Hidden Architecture) → Book 3 (The Creator's Blueprint)**

Every claim cascades upward. Never write a higher-level book before the foundation it rests on is complete. No rewrites — get it right the first time by building bottom-up.

## Before You Write ANYTHING

1. **Read the Development Process:** `Development_Process/00_PROCESS_OVERVIEW.md` — understand the full SE lifecycle
2. **Read the Quality Requirements:** `Quality_Control/01_REQUIREMENTS.md` — know what "done" means
3. **Read the Book's QUALITY_GATE.md** — know which requirements and reviewers apply
4. **Check the Research folder** — find what's already been derived. Use it. Don't reinvent.
5. **Check the Reference docs** — `Quality_Control/Reference/` for glossary, notation, zone architecture, symbols, biblical references

## When Writing a Chapter

Follow `Development_Process/01_WRITING_PROCESS.md` exactly:
1. Create a CHAPTER_SPEC.md from the template (`Development_Process/03_CHAPTER_SPEC_TEMPLATE.md`)
2. Write a detailed outline before prose
3. Draft following the Five Writing Laws (start with WHY, intuition before math, one voice, no forward deps, mark uncertainty)
4. Self-review with the author checklist
5. Run all assigned reviewer agents from `Quality_Control/Reviewers/`
6. Revise until all reviewers PASS

## When You Find a Research Gap

If writing requires physics, derivations, or data that doesn't exist in `Research/`:

1. **STOP writing.** Do not make things up or hand-wave.
2. Create a `RESEARCH_GAP.md` note in the chapter's folder documenting:
   - What's needed
   - Why it's needed (which chapter requirement depends on it)
   - What Research folder it should live in
   - Suggested approach
3. Create a GitHub issue: `gh issue create --title "Research Gap: [topic]" --label "research-gap" --body "[details]"` in the `raymondjl1/genesis_physics` repo
4. Mark the chapter spec requirement as BLOCKED

## Reviewer Agents

10 reviewer personas act as quality gates. Each is defined in `Quality_Control/Reviewers/`:

| # | Reviewer | Focus |
|---|---------|-------|
| 01 | The Physicist | Mathematical rigor, derivation validity |
| 02 | The "But Why?" Reader | **Most important.** Does every concept explain WHY? |
| 03 | The Writing Coach | Prose quality, voice, readability |
| 04 | The Consistency Auditor | Cross-reference integrity, notation consistency |
| 05 | The Homeschool Mom ("Sarah") | Teachability, family-friendliness (Creator's Blueprint only) |
| 06 | The Skeptic ("Dr. Marcus Chen") | Would an atheist physicist take this seriously? |
| 07 | The Student | Can a grad student follow and reproduce? |
| 08 | The Style Editor | Style sheet compliance, formatting, copyediting |
| 09 | The Theologian ("Dr. Ruth Abramowitz") | Biblical/exegetical accuracy, theological fidelity |
| 10 | The Navigator | Cross-book depth calibration, series coherence |

**To run a reviewer:** Read the reviewer's definition file, then evaluate the chapter from that persona's perspective. Produce a scorecard with PASS/FAIL and specific findings.

## GitHub Integration

**Repo:** `raymondjl1/genesis_physics`
**Project Board:** Genesis Physics (V2), columns: Todo | In Progress | Done

When `gh` CLI is available:
- Create issues for each task using labels from the existing label system
- Reference issue numbers in commit messages
- Move issues on the project board as work progresses
- After completing any task, run relevant tests from `Research/Mathematical_Models/` test suites

## Products at a Glance

| # | Title | Audience | Equations | Voice | Build Order |
|---|-------|----------|-----------|-------|-------------|
| 0 | **The Foundations of Genesis Physics** (6 vols) | Grad students/physicists | Heavy (LaTeX) | Feynman writing a textbook | **1st** |
| 1 | **The Firmament Equations** | Working physicists | Moderate | Brian Greene's *Elegant Universe* | **2nd** |
| 2 | **The Hidden Architecture** | Intelligent layperson | ZERO | Brian Cox meets C.S. Lewis | **3rd** |
| 3 | **The Creator's Blueprint** | Homeschool families | None | Warm, encouraging teacher | **4th** |

## What NOT to Do

- **Never skip the "why."** If you can't explain why, don't write it.
- **Never use a concept before establishing it.** No forward dependencies.
- **Never invent physics.** Everything must trace to Research/ derivations.
- **Never mix voices.** Each product has ONE voice. Stay in it.
- **Never publish without reviewer agents passing.** The quality gate is the quality gate.
- **Never rewrite a lower-level book because a higher-level book needs it different.** Fix the higher-level book instead.
