# System Integrity Check — Agent Prompt

**Purpose:** Run a full traceability and consistency audit across the Genesis Physics project infrastructure. When complete, any Claude Cowork session opening a book folder should have everything it needs — connected, traceable, error-free — to immediately execute the book writing process defined in `Development_Process/`.

**Output:** A findings report saved to `Quality_Control/Findings/SYSTEM_INTEGRITY_AUDIT.md`, plus GitHub issues created (via Chrome interface) for every gap found.

---

## CONTEXT — READ THESE FILES FIRST

Before doing anything, read these files in order to understand the system you're auditing:

```
01_Genesis_Physics/CLAUDE.md                          ← Master instructions
01_Genesis_Physics/Development_Process/00_PROCESS_OVERVIEW.md  ← The SE lifecycle
01_Genesis_Physics/Development_Process/01_WRITING_PROCESS.md   ← Chapter-level workflow
01_Genesis_Physics/Development_Process/03_CHAPTER_SPEC_TEMPLATE.md  ← Chapter spec template
01_Genesis_Physics/Development_Process/04_BOOK_SPEC_TEMPLATE.md     ← Book spec template
01_Genesis_Physics/Quality_Control/00_SERIES_VISION.md         ← North Star
01_Genesis_Physics/Quality_Control/01_REQUIREMENTS.md          ← 48+ requirements
01_Genesis_Physics/Quality_Control/02_VALIDATION_PLAN.md       ← 4-level validation plan
01_Genesis_Physics/Quality_Control/BOOK_SERIES_STRATEGY.md     ← Chapter outlines for all products
```

These documents define "the system." Your job is to verify that the rest of the project infrastructure faithfully implements what these documents promise.

---

## AUDIT DOMAINS

You are running **seven audit domains**, each with specific checks. For every check, record: PASS, FAIL (with description), or MISSING (artifact doesn't exist yet). Think like a systems engineer doing a CDR (Critical Design Review) — if the documentation says it exists, verify it exists. If a process references a file, verify the file is there and says what the process thinks it says.

---

### DOMAIN 1: STRUCTURAL COMPLETENESS — "Does every required artifact exist?"

The process documents define a set of artifacts that must exist for each book/volume. Verify:

**1.1 — Per-Book Required Files**
For EACH of these folders: `Book_2_The_Hidden_Architecture/`, `Book_1_Hidden_Architecture/` *(renamed April 2026 from `Book_1_The_Firmament_Equations/`)*, `Book_0_The_Foundations/`, `Book_3_The_Creators_Blueprint/`:
- [ ] `README.md` exists and is up-to-date (references current series structure, not old 3-book structure)
- [ ] `STATUS.md` exists and reflects current state
- [ ] `CLAUDE.md` exists with book-specific instructions
- [ ] `QUALITY_GATE.md` exists with correct reviewer assignments per `02_VALIDATION_PLAN.md` reviewer matrix
- [ ] `BOOK_SPEC.md` exists (per `00_PROCESS_OVERVIEW.md` Phase 2 — this is REQUIRED before writing)
- [ ] `Manuscript/` directory exists
- [ ] `Source_Reference/` directory exists

**1.2 — Per-Volume Required Files (Foundations Vol 1-6)**
For EACH of: `Vol_1_Architecture_of_Reality/` through `Vol_6_Predictions_and_Simulations/`:
- [ ] `CLAUDE.md` exists with volume-specific instructions
- [ ] `QUALITY_GATE.md` exists with correct reviewer assignments
- [ ] `BOOK_SPEC.md` exists (each volume needs its own — it's a standalone textbook)
- [ ] `README.md` exists with volume overview
- [ ] `Manuscript/` directory exists and is ready for chapter files
- [ ] `Source_Reference/` directory exists

**1.3 — Series-Level Required Files**
- [ ] `Series_Bible/` directory exists at `01_Genesis_Physics/Series_Bible/`
  - [ ] `STYLE_GUIDE.md` exists (referenced by CLAUDE.md)
  - [ ] Glossary exists
  - [ ] Biblical references file exists
  - [ ] Zone tables exist
  - [ ] Notation standard exists (referenced by MATH-012, Vol 1 CLAUDE.md)
- [ ] `Development_Process/03_CHAPTER_SPEC_TEMPLATE.md` exists and is a usable template
- [ ] `Development_Process/04_BOOK_SPEC_TEMPLATE.md` exists and is a usable template
- [ ] `Quality_Control/00_SERIES_VISION.md` exists

**1.4 — Research Infrastructure**
- [ ] `Research/Foundations/` has all axiom files referenced by Vol 1 CLAUDE.md
- [ ] `Research/Mathematical_Models/` has all 10 domain subdirectories (01-10)
- [ ] `Research/Simulations/` has simulation files referenced by Vol 6 CLAUDE.md
- [ ] `Research/Papers/` exists with research papers
- [ ] `Research/Peer_Review/` exists

---

### DOMAIN 2: CROSS-REFERENCE INTEGRITY — "Does every pointer land on a real target?"

Every CLAUDE.md, README.md, and process document references specific files/folders. Verify they resolve.

**2.1 — CLAUDE.md Cross-References**
For EACH CLAUDE.md file in the project:
- [ ] Every file path referenced in the CLAUDE.md actually exists at that path
- [ ] Every folder referenced exists
- [ ] Research file mappings (e.g., Vol 2 CLAUDE.md → `03_Electromagnetism/MAXWELL_FROM_ZONE_ARCHITECTURE.md`) resolve to real files

**2.2 — Process Document Cross-References**
In `Development_Process/00_PROCESS_OVERVIEW.md`:
- [ ] The "Where the Documents Live" table (line ~302) — every path resolves
- [ ] References to `BOOK_SPEC.md`, `CHAPTER_SPEC.md`, `QUALITY_GATE.md` — do these templates/files exist where claimed?

In `Development_Process/01_WRITING_PROCESS.md`:
- [ ] References to templates (`03_CHAPTER_SPEC_TEMPLATE.md`, etc.) resolve
- [ ] References to `Quality_Control/Reviewers/` resolve
- [ ] Reviewer assignment matrix matches `02_VALIDATION_PLAN.md`

**2.3 — Quality Control Cross-References**
In `Quality_Control/01_REQUIREMENTS.md`:
- [ ] The "Traceability Matrix" source documents (line ~119) — do they exist? (e.g., `01_Scientific_Rigor_Analysis.md`)
- [ ] GAP items (GAP-001 through GAP-010) — which have been resolved vs. still open?

In `Quality_Control/02_VALIDATION_PLAN.md`:
- [ ] Reviewer agent files referenced exist in `Reviewers/`
- [ ] Reviewer count is consistent (memory says 7, but folder shows 10 files: REVIEWER_01 through REVIEWER_10)

**2.4 — QUALITY_GATE.md Consistency**
For EACH `QUALITY_GATE.md`:
- [ ] Reviewer assignments match the matrix in `02_VALIDATION_PLAN.md`
- [ ] Product type is correctly identified
- [ ] No reviewer assigned that shouldn't be (e.g., Homeschool Mom on Foundations)

---

### DOMAIN 3: RESEARCH ↔ BOOK TRACEABILITY — "Can every chapter find its research?"

This is the most critical audit. The process says "Never invent physics — everything must trace to Research/ derivations." Verify:

**3.1 — Chapter Outline → Research Mapping**
Read `Quality_Control/BOOK_SERIES_STRATEGY.md` for the chapter outlines of all products. For every chapter listed in every volume:
- [ ] Identify what research/derivation the chapter requires
- [ ] Check if that research file exists in `Research/`
- [ ] If it doesn't exist, flag as a RESEARCH GAP

**3.2 — Research → Volume Mapping (reverse direction)**
For every file in `Research/Foundations/` and `Research/Mathematical_Models/`:
- [ ] Is it referenced by at least one volume's CLAUDE.md?
- [ ] Is it mapped to a specific chapter?
- [ ] Are there orphan research files not connected to any book chapter?

**3.3 — Research File Internal Consistency**
For the key Foundations axiom files:
- [ ] Do they reference each other correctly? (e.g., does `AXIOM_MEMBRANE_MECHANICS_v2.md` reference `AXIOM_6D_SPACETIME.md` where it should?)
- [ ] Are there version conflicts? (e.g., v1 vs v2 — is it clear which to use?)
- [ ] Does `VALIDATION_REPORT_2026-04-05.md` reflect current state of research?

**3.4 — GitHub Issues ↔ Research Gaps**
- [ ] Every known research gap in the CLAUDE.md files has a corresponding GitHub issue
- [ ] GitHub issues reference the correct Research/ files
- [ ] No duplicate issues for the same gap

---

### DOMAIN 4: PROCESS PIPELINE INTEGRITY — "Can the writing process execute end-to-end?"

Walk through the SE lifecycle (Phases 1-10) from `00_PROCESS_OVERVIEW.md` and verify every handoff:

**4.1 — Phase 1 → 2 Handoff (Vision → Book Requirements)**
- [ ] `00_SERIES_VISION.md` exists and defines governing principles
- [ ] Governing principles trace to requirements in `01_REQUIREMENTS.md`
- [ ] `04_BOOK_SPEC_TEMPLATE.md` is a complete, fillable template

**4.2 — Phase 2 → 3 Handoff (Book Requirements → Chapter Architecture)**
- [ ] `03_CHAPTER_SPEC_TEMPLATE.md` is a complete, fillable template
- [ ] It references requirement IDs from `01_REQUIREMENTS.md`
- [ ] The chapter outlines in `BOOK_SERIES_STRATEGY.md` cover all requirements (no orphan requirements)

**4.3 — Phase 5 → 6 Handoff (Writing → Verification)**
- [ ] Each reviewer agent file in `Reviewers/` is a complete, usable system prompt
- [ ] Each reviewer has a scorecard template (check against scorecards in `02_VALIDATION_PLAN.md`)
- [ ] The reviewer assignment matrix is consistent across ALL documents that reference it:
  - `02_VALIDATION_PLAN.md`
  - `01_WRITING_PROCESS.md`
  - Each book's `QUALITY_GATE.md`
  - Each book's `CLAUDE.md`
  - The master `01_Genesis_Physics/CLAUDE.md`

**4.4 — Phase 6 → 7 Handoff (Verification → Integration)**
- [ ] Integration checks defined in `00_PROCESS_OVERVIEW.md` Phase 7 are actionable
- [ ] STATUS.md files have a validation tracking table format

**4.5 — Research Gap Workflow**
The CLAUDE.md defines a research gap workflow (find gap → create RESEARCH_GAP.md → create GitHub issue → mark BLOCKED). Verify:
- [ ] This workflow is referenced consistently in all relevant documents
- [ ] GitHub label `research-gap` exists in the repo (or the equivalent label scheme)

---

### DOMAIN 5: REVIEWER AGENT SYSTEM INTEGRITY — "Is the quality gate fully operational?"

**5.1 — Reviewer File Audit**
List all files in `Quality_Control/Reviewers/`. For each:
- [ ] File contains a complete persona definition (name, background, mandate)
- [ ] File contains specific evaluation criteria (not vague)
- [ ] File contains a scorecard template OR references the one in `02_VALIDATION_PLAN.md`
- [ ] File specifies which products this reviewer applies to

**5.2 — Reviewer Count Reconciliation**
The memory system and `02_VALIDATION_PLAN.md` reference 7 reviewers. The folder contains 10 files (REVIEWER_01 through REVIEWER_10). Reconcile:
- [ ] Which reviewers are canonical?
- [ ] Are REVIEWER_08, 09, 10 new additions or duplicates?
- [ ] Update the reviewer matrix in ALL documents to match the actual set

**5.3 — Reviewer ↔ Requirement Mapping**
For each requirement category in `01_REQUIREMENTS.md` (WHY, MATH, STRUCT, CON, PUB):
- [ ] At least one reviewer agent is responsible for checking requirements in that category
- [ ] No requirement category is uncovered by the reviewer system

---

### DOMAIN 6: SERIES BIBLE / REFERENCE MATERIAL — "Is the single source of truth actually single?"

**6.1 — Series Bible Existence and Completeness**
The master CLAUDE.md references `Series_Bible/STYLE_GUIDE.md`. Verify:
- [ ] The `Series_Bible/` directory exists
- [ ] `STYLE_GUIDE.md` exists and covers: zone naming, notation, voice per product, terminology standards
- [ ] Glossary exists with canonical definitions
- [ ] Biblical references file exists
- [ ] Zone architecture reference exists

Cross-check: `Quality_Control/Reference/` also contains reference materials (Glossary, Zone_Architecture, etc.). Are these duplicates of or replacements for a Series_Bible? Clarify the relationship.

**6.2 — Terminology Consistency**
Spot-check across 5+ documents:
- [ ] Zone numbering scheme is consistent
- [ ] Five Governing Principles naming/ordering is consistent
- [ ] "Membrane" vs "Firmament" vs "boundary" usage follows a standard
- [ ] Dark matter/energy pairing convention is followed

**6.3 — Constants and Symbols**
- [ ] `Quality_Control/Reference/Symbol_and_Constants.md` exists
- [ ] Values match those used in `Research/Mathematical_Models/` derivation files
- [ ] No conflicting values for the same constant across files

---

### DOMAIN 7: CLAUDE.md INSTRUCTION CHAIN — "Can a fresh Claude session bootstrap correctly?"

This is the ultimate test. Simulate what happens when Claude opens each folder:

**7.1 — Master Bootstrap**
If Claude opens `01_Genesis_Physics/`:
- [ ] `CLAUDE.md` gives clear instructions
- [ ] "Before You Write ANYTHING" checklist references files that exist
- [ ] Build order is stated
- [ ] GitHub integration instructions work (repo URL, label scheme)

**7.2 — Book-Level Bootstrap**
If Claude opens `Book_0_The_Foundations/`:
- [ ] `CLAUDE.md` gives volume-specific guidance
- [ ] Research mapping table references files that exist
- [ ] Known research gaps match current state
- [ ] Reviewer assignments are correct

If Claude opens `Book_0_The_Foundations/Vol_1_Architecture_of_Reality/`:
- [ ] `CLAUDE.md` tells Claude exactly what this volume must deliver
- [ ] Research file references ALL resolve
- [ ] Test suite commands work (paths are correct)
- [ ] GitHub issue creation commands use correct labels/format

**7.3 — Instruction Consistency**
Across ALL CLAUDE.md files:
- [ ] Build order is stated consistently (Foundations → Book 1 → Book 2 → The Creator's Blueprint)
- [ ] Voice descriptions match across all references
- [ ] Reviewer assignments don't contradict between levels
- [ ] No CLAUDE.md contradicts another CLAUDE.md

---

## OUTPUT FORMAT

### 1. Findings Report

Save to `Quality_Control/Findings/SYSTEM_INTEGRITY_AUDIT.md`:

```markdown
# System Integrity Audit — [DATE]

## Executive Summary
- Total checks performed: [N]
- PASS: [N]
- FAIL: [N]
- MISSING: [N]
- Critical issues (blocks writing process): [N]
- Non-critical issues (should fix but doesn't block): [N]

## Domain 1: Structural Completeness
### PASS
- [list items that passed]
### FAIL
- [item]: [what's wrong and what it should be]
### MISSING
- [item]: [what needs to be created, with specific instructions]

[...repeat for all 7 domains...]

## Critical Path Items
Items that MUST be resolved before any chapter writing can begin:
1. [item] — [why it blocks]
2. [item] — [why it blocks]

## Recommended Fix Order
1. [highest priority fix]
2. [next]
3. [...]

## Traceability Matrix
| Issue | Domain | Severity | GitHub Issue # | Fix Description |
|-------|--------|----------|---------------|-----------------|
```

### 2. GitHub Issues

For every FAIL or MISSING item, create a GitHub issue on the project board via Chrome interface:
- **Repository:** `raymondjl1/genesis_physics`
- **Project Board:** Genesis Physics (V2)
- **Title format:** `[INTEGRITY] Domain N.N: Brief description`
- **Labels:** `integrity-audit` + severity (`critical`, `high`, `medium`, `low`)
- **Body:** Include: what's wrong, what it should be, which documents are affected, suggested fix

### 3. Quick Fixes

If a fix is trivial (e.g., creating an empty directory, adding a missing file with obvious content), just make the fix directly and log it in the findings report as "AUTO-FIXED."

Trivial fix criteria (all must be true):
- Takes < 2 minutes
- Cannot introduce errors
- Does not require design decisions
- Examples: creating a missing directory, fixing a broken file path reference, creating a placeholder README

Do NOT auto-fix anything that requires design decisions (like writing a BOOK_SPEC.md or choosing a notation standard).

---

## EXECUTION ORDER

1. **Read all context files** listed at the top
2. **Run Domain 1** (Structural Completeness) — this gives you the lay of the land
3. **Run Domain 7** (CLAUDE.md chain) — this tells you if the bootstrap works
4. **Run Domain 2** (Cross-References) — this finds broken pointers
5. **Run Domain 3** (Research ↔ Book traceability) — this is the deepest audit
6. **Run Domain 5** (Reviewer system) — this validates the quality gate
7. **Run Domain 6** (Series Bible) — this checks the single source of truth
8. **Run Domain 4** (Process pipeline) — this verifies end-to-end flow
9. **Compile findings report**
10. **Create GitHub issues for all FAIL/MISSING items**
11. **Apply trivial auto-fixes**
12. **Final verification pass** — re-check that auto-fixes didn't break anything

---

## SUCCESS CRITERIA

When this audit is complete, the following must be true:

1. **Any Claude Cowork session** opening any book folder can immediately find: its CLAUDE.md → its QUALITY_GATE.md → the relevant Research/ files → the reviewer agents → the process documents → the Series Bible. Zero dead ends.

2. **Every requirement** in `01_REQUIREMENTS.md` traces to: a source (governing principle or analysis finding) AND at least one chapter in `BOOK_SERIES_STRATEGY.md`. No orphan requirements.

3. **Every chapter** in `BOOK_SERIES_STRATEGY.md` traces to: at least one research file OR is flagged as a research gap with a GitHub issue.

4. **Every reviewer agent** has: a complete definition file, a scorecard template, correct product assignments across ALL documents that reference it.

5. **Every CLAUDE.md** references only files that exist, states the build order correctly, and doesn't contradict any other CLAUDE.md.

6. **All gaps** are logged as GitHub issues with severity labels so they can be prioritized and tracked.
