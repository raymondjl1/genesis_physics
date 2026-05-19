# Batch B2 — Policy Lock (0516_Rev_033, 034, 035, 037, 038, 039, 129–131, 207, 208, 275–278, 334–336, plus FollowOns #840 #841)

**Date:** 2026-05-18
**Source:** Pre-execution decision interview with Jeff Raymond
**Status:** LOCKED — executor agents must follow these without re-asking
**Predecessor:** `0516_Rev_B1_POLICY_LOCK.md` (carried forward unchanged unless noted)

This document captures every policy decision required to execute Batch B2 unattended. Scope rules, commit/close protocol, and project-board mechanics from B1 carry forward verbatim. Only the additions/overrides for B2 appear below.

---

## Tasks in scope (20 items)

**Cross-cutting P0:** 033 (#133)
**Cross-cutting P1:** 034 (#134), 035 (#135), 037 (#137), 038 (#138), 039 (#139)
**Vol 2 P0:** 129 (#229), 130 (#230), 131 (#231)
**Vol 3 P0:** 207 (#307), 208 (#308)
**Vol 4 P0:** 275 (#375), 276 (#376), 277 (#377), 278 (#378)
**Vol 5 P0:** 334 (#434), 335 (#435), 336 (#436)
**FollowOns from 001:** #840 (Vol 6 FTL σ²/(2μ) dimensional fix), #841 (Vol 1 PS-10.3 solution key regen)

---

## Jeff's four judgment-call decisions (asked & locked 2026-05-18)

### Decision 1 — Task 033 — `bara` doctrine

**CANON: "ex nihilo" with lexical footnote.**

Align both AppC C.2 and C.5 to the ex-nihilo doctrinal reading. Add an explicit lexical footnote at C.2 acknowledging this is a doctrinal reading (cf. Heb 11:3) and is NOT itself encoded in the Hebrew root *bārāʾ* per the standard lexicon. C.5 is then made consistent with C.2 (no internal contradiction).

**Implementation:**
- C.2 lead: `bārāʾ` is the signature verb of divine creation; in canonical doctrine (Heb 11:3) it denotes creation *ex nihilo* — bringing into being out of no pre-existing substance.
- Footnote at C.2: "Lexicographically, the Hebrew root *bārāʾ* encodes only 'create / bring into being' and is also used of acts that shape pre-existing material (Gen 1:27 from dust, Isa 65:17 of the renewed cosmos). The ex-nihilo reading is a doctrinal synthesis grounded in Heb 11:3 and the wider canon; this Appendix adopts it as the doctrinal position while flagging that the lexical entry alone does not entail it."
- C.5: drop the "creation does not mean conjuring something from absolute nothingness" line; replace with language consistent with C.2 ("creation in the *bārāʾ* sense is ex nihilo *and* simultaneously orderly — the *tōhû wā-bōhû* state of Gen 1:2 describes the immediately post-bārāʾ unformed-but-existent material the rest of the week shapes").

### Decision 2 — Task 278 — Waters/Spirit Gen 1:2 paragraph (Vol 4 Ch 5)

**CANON: Keep, demote tone slightly.**

Preserve the structural payload (Spirit-over-Waters as a Gen 1:2 anchor for the Waters Above/Below structure). Trim the most devotional sentences. End the paragraph on the physics anchor, not on worship. Theologian + Homeschool Mom approval is preserved; Writing Coach register objection is addressed.

**Implementation rules for the executor:**
- Keep the Gen 1:2 quotation.
- Keep the structural claim ("the Spirit's hovering over the waters identifies a relational asymmetry that the bulk-field architecture of Vol 1 Ch 3–4 formalizes").
- Strike or shorten sentences that read as homiletic ("we should be moved that…", "let us pause…", etc.).
- Final sentence of the paragraph must point back to a Vol 1 chapter or to the Ch 5 derivation — not to devotional reflection.

### Decision 3 — Task 277 — "this chapter is a triumph" tone

**CANON: Suggested rewrite (verbatim).**

Replace Ch 4 §4.0 lines 257–259 with the rewrite already locked in the task master file:

> "This chapter argues that Bell inequalities are not metaphysical mysteries but structural consequences of zone topology. The derivation is incomplete in one identified step (see §4.4.3 and the Open Problems list); the structural result, however, is rigorous."

Do not retain the word "triumph" anywhere in the chapter.

### Decision 4 — Task 130 — predictions vs consistency checks

**CANON: Both → consistency checks.**

Maximize derivation honesty. Anything that has a free parameter fit to data is a **consistency check**, not a prediction. Specifically:

- **G_4** (Route 2 fits L_eff to G_N): label "consistency check"; remove from any "prediction" table.
- **α⁻¹** (K = 1.4383 fit in Vol 4 to recover the measured value): label "consistency check"; remove from any "prediction" table.

The Ch 11 §11.3.1 numerical table must be split into three columns:

1. **Predictions** — quantities derivable from the framework with no free parameters fit to that quantity's value.
2. **Consistency Checks** — quantities recovered after fitting one or more free parameters (G_4, α⁻¹, anything else identified during execution).
3. **Pending** — quantities whose derivation remains open (sin²θ_W, etc.).

Replace any "no free parameters" claim in Vol 2 with an explicit Parameter Ledger (in the back matter) listing every fitted constant, where it was fit, what it was fit to, and which downstream numbers inherit the fit.

The §2.4.2 footnote that already admits calibration is to be *promoted* to a Preface-level statement in the Vol 2 Preface, not buried as a footnote.

---

## Inherited and continuing canon (from B1 — no change)

- **Seven axioms + Postulate F.** (B1 Rev_003)
- **Five Principles, Title Case, fixed order.** (B1 Rev_004)
- **ξ_A / η_B = 3×10²⁶ m.** (B1 Rev_007)
- **Hebrew first-mention format** with macrons. (B1 Rev_006)
- **Waters Above / Waters Below pairing rule.** (B1 Rev_020)
- **Genesis 1 anchoring footnotes per chapter.** (B1 Rev_019)

These canons MUST be respected in any new content authored in B2 (e.g., new paragraphs for 037/038, rewrites for 130/131, error-budget rewrite for 336). When in doubt, defer to B1 lock.

---

## Execution scope rules (carry forward from B1 verbatim)

**Scope IN:**
- `Vol_*/Manuscript/`
- `Vol_*/Back_Matter/`
- `Vol_*/audio book/` (regenerate via preprocess_book0.py after all manuscript edits land)
- `Quality_Control/Reference/`
- `Vol_*/CHAPTER_SPEC.md`, `BOOK_SPEC.md`, `QUALITY_GATE.md`
- `Research/Foundations/`, `Research/Mathematical_Models/`

**Scope OUT:**
- `00_Archive/`, `Reviews/`, `_pre-comprehensive/`
- `*_REVIEWS.md`, `*_REVIEWER_REPORT.md`, `*_SELF_REVIEW_REPORT.md`, `*_REVIEWER_NOTES.md`, `*_SELF_REVIEW.md`, `REVIEWER_BRIEF.md`
- `BOOK_SERIES_MASTER_REVIEW_*.md`, `0516_Rev_*_TASKS.md`
- `0516_Rev_B1_POLICY_LOCK.md` and `0516_Rev_B2_POLICY_LOCK.md` themselves

**Working tree warnings:**
- DO NOT `git add -A`.
- Stage only task-edited files individually.
- No pushes between tasks; one final `git push origin master` at end.
- No amends, no force-pushes.

---

## Execution phases (recommended ordering)

**Phase A — Mechanical canon (sequential):**
- 035 (Greek index convention {0,1,2,3,5,6})
- 039 (eq tag (1.5.0) → (1.5.37))

**Phase B — Surgical fixes (parallel, file-disjoint):**
- 034 (Vol 1 Ch06 stale sign-note)
- 207 (Vol 3 Ch 9 fluctuation algebra)
- 208 (Vol 3 Ch 7 unit chain)
- #840 (Vol 6 FTL σ²/(2μ) dimensional formula — author input may be needed; if so, document gap and proceed to close as "follow-on noted; awaiting author")
- #841 (Vol 1 PS-10.3 solution key — blocked by absence of Vol 1 solutions doc; close with deferred comment if solutions doc still absent)

**Phase C — Numerical / derivation honesty (serialize within volume):**
- Vol 2: 129 → 130 → 131 (warp profile must be picked before predictions table is split; predictions table must be settled before §4.2 topology rewrite)
- Vol 4: 275 → 276 (Λ_zone must be picked before seesaw mass can be redone)

**Phase D — Cross-cutting P0 and judgment-call edits (sequential):**
- 033 (AppC bara — per Decision 1)
- 277 (Vol 4 Ch 4 triumph — per Decision 3)
- 278 (Vol 4 Ch 5 Waters/Spirit paragraph — per Decision 2)

**Phase E — Heavy rewrites (Jeff async review for Vol 5 trio):**
- 334 (ℏ derivation — λ honesty: prefer demote, not derive; if derivation is feasible from 6D Einstein equations + Ch 13 λ=3 anchor, attempt it; otherwise demote §15.1.3 / §15.2.6 headlines)
- 335 (Vol 5 Ch 12 starlight — add §3.5 obs-consistency budget; demote §§3.1–3.3 to hypothesis; verify Vol 1 R-11 κ-transition derivability)
- 336 (Vol 5 Ch 13 error budget rewrite — clean covariance table, honest α⁻¹ range)
- 037 (Vol 1 Ch 8 𝒪_sustain couplings — symmetry/dimensional argument + open-problems entry)
- 038 (Vol 1 Ch 6 G_int form motivation — lowest-order Lorentz scalar from Axiom 6 + dimensional analysis)

Phase E tasks may surface Vol 5 / Vol 1 cascading issues; if so, raise as follow-on issues rather than expanding B2 scope.

---

## Per-task execution rigor

| Phase | Tasks | Rigor |
|---|---|---|
| A | 035, 039 | Single agent + post-grep verification |
| B | 034, 207, 208 | Single agent + light validator |
| B (follow-ons) | #840, #841 | Single agent; if blocked, close with deferred-rationale comment |
| C | 129, 130, 131, 275, 276 | Planner + Executor + Independent Validator |
| D | 033, 277, 278 | Planner + Executor + Validator (judgment-call tasks: validator confirms wording matches Jeff's locked decision) |
| E | 334, 335, 336, 037, 038 | Drafter + Jeff async review before commit |

Phase E tasks are the only B2 tasks requiring asynchronous Jeff review.

---

## Commit and close protocol (carry forward from B1 verbatim)

1. Move project board item: Todo → In Progress.
2. Execute per phase/rigor matrix.
3. Validate; resolve caveats.
4. Stage task-only files individually (use `git diff --name-only --diff-filter=M` to enumerate).
5. Commit with message ending `Closes #<num>`.
6. `gh issue close <num> --reason completed -c "..."`.
7. Move project board item: In Progress → Done (via direct GraphQL mutation; see B1 lock for the exact mutation).
8. Update todo list.

**TTS regeneration:** after ALL manuscript edits land, run `cd 01_Genesis_Physics/Book_0_The_Foundations && python preprocess_book0.py`. Commit `audio book/` deltas in ONE commit with message `0516_Rev_B2: regenerate TTS preprocessing for Book 0 (all 6 vols)`.

**Final push:** single `git push origin master` after TTS commit.

---

## Project board IDs

- PROJECT_ID: `PVT_kwHOB1aXSc4BTuXV`
- STATUS_FIELD_ID: `PVTSSF_lAHOB1aXSc4BTuXVzhA7W4Y`
- Options: Todo=`f75ad846` · In Progress=`47fc9ee4` · Ready for Test=`3b23bbec` · Done=`98236657`

## Issue / item map (B2)

| Task | Issue | Item ID |
|---|---|---|
| 033 | #133 | PVTI_lAHOB1aXSc4BTuXVzgs643k |
| 034 | #134 | PVTI_lAHOB1aXSc4BTuXVzgs644I |
| 035 | #135 | PVTI_lAHOB1aXSc4BTuXVzgs644s |
| 037 | #137 | PVTI_lAHOB1aXSc4BTuXVzgs6454 |
| 038 | #138 | PVTI_lAHOB1aXSc4BTuXVzgs646g |
| 039 | #139 | PVTI_lAHOB1aXSc4BTuXVzgs647A |
| 129 | #229 | PVTI_lAHOB1aXSc4BTuXVzgs65y0 |
| 130 | #230 | PVTI_lAHOB1aXSc4BTuXVzgs65zY |
| 131 | #231 | PVTI_lAHOB1aXSc4BTuXVzgs651Q |
| 207 | #307 | PVTI_lAHOB1aXSc4BTuXVzgs66lI |
| 208 | #308 | PVTI_lAHOB1aXSc4BTuXVzgs66ns |
| 275 | #375 | PVTI_lAHOB1aXSc4BTuXVzgs67c8 |
| 276 | #376 | PVTI_lAHOB1aXSc4BTuXVzgs67dU |
| 277 | #377 | PVTI_lAHOB1aXSc4BTuXVzgs67eM |
| 278 | #378 | PVTI_lAHOB1aXSc4BTuXVzgs67eo |
| 334 | #434 | PVTI_lAHOB1aXSc4BTuXVzgs6778 |
| 335 | #435 | PVTI_lAHOB1aXSc4BTuXVzgs678o |
| 336 | #436 | PVTI_lAHOB1aXSc4BTuXVzgs679s |
| FollowOn | #840 | PVTI_lAHOB1aXSc4BTuXVzgtIjTk |
| FollowOn | #841 | PVTI_lAHOB1aXSc4BTuXVzgtIjT0 |

(Items for #840 and #841 were added to the project board at B2 kickoff; they were not on the board previously.)

---

## Open items inherited from B1 (surfaced to Jeff; not B2 execution tasks)

These are *not* B2 tasks; they need Jeff's decision either before or in parallel with B2 execution. They are listed here for tracking only.

1. **Theorem 2.4.7 anchor (B1 Rev_021).** Vol 1 Ch03 L398 cites "Theorem 2.4.7" but Ch02 §2.4 only contains Theorem 2.4.1. Decision: rename 2.4.1 → 2.4.7 (preferred — preserves Ch03 citation), or update Ch03 to cite 2.4.1.
2. **B1 Rev_019 flags** (5 items from the agent in commit `4c9405e`):
   - Vol 2 Ch 11 §11.10: ~640-word closing reflection in review voice — keep / trim / move.
   - Vol 4 Ch 11 §11.1 epigraph: Heb 1:3 vs Col 1:17.
   - Vol 5 Part IV preface title: "Chronology and Cosmological Reflection" — confirm or rename.
   - Vol 3 Ch 1 §1.1 new eq (3.1.0) numbering — confirm tag is valid (cf. B2 Rev_039 for the (1.5.0) precedent).
   - Vol 6 Ch09_DRAFT_Part3.md: confirm whether `_Part*` files are co-authoritative with the main DRAFT or are old fragments to retire.

---

**END OF POLICY LOCK.**
