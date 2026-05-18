# Batch B1 — Policy Lock (0516_Rev_003 through 0516_Rev_032)

**Date:** 2026-05-17
**Source:** Pre-execution decision interview with Jeff Raymond
**Status:** LOCKED — executor agents must follow these without re-asking

This document captures every policy decision required to execute Batch B1 unattended. Each section names the issue, the canonical decision, and the scope of edits.

---

## Tasks in scope (18 tasks; 005 + 008 excluded)

P0: 003, 004, 006, 007, 023, 024, 025, 026, 027, 028, 029, 030, 031, 032
P1: 019, 020, 021, 022

**Excluded from B1:**
- **005** — `AUTHOR_VOICE_AND_BACKGROUND.md` (Jeff authors himself).
- **008** — Production readiness sprint (DEFERRED; 8–12 week external project; close issue with deferred comment).

---

## Group 1 — Canon locks (must complete first; downstream depends)

### 0516_Rev_003 — Axiom canon

**CANON: SEVEN axioms.**

1. Sustaining (κ-degradation / continuous existence)
2. Creation Complete (closed Sabbath boundary)
3. Symmetries (SO(3) spatial isotropy)
4. Humans (zone-interface consciousness; PROPOSED — see Rev_031)
5. Fall (κ-degradation epoch transition)
6. Duality (Waters Above / Waters Below)
7. **Four Thermodynamic Phases** (Creation week, Eden, Fallen, New Heavens)

Plus **Postulate F** as separate from the axiom set.

**Aliases:**
- Vol 2 may use "Open System Axiom (Axiom 1)" as shorthand AFTER canonical name on first mention per chapter.
- "Axiom 1.1" / "Axiom 1.2" sub-numbering is FORBIDDEN. Use only "Axiom 1," "Axiom 2," ... "Axiom 7" + "Postulate F."

**Files to update (canonical site = Ch1):**
- `Vol_1/Manuscript/Ch_01_*/Ch01_DRAFT.md` §1.2–§1.7, §1.8 (independence — add Ax7 counter-model), §1.10 (summary)
- `Quality_Control/Reference/Axiom_Summary_Cards.md` — already lists 7; verify names and order match
- `01_Genesis_Physics/Book_0_The_Foundations/Vol_1_Architecture_of_Reality/BOOK_SPEC.md` BK-001 line 50
- `Vol_1_Architecture_of_Reality/QUALITY_GATE.md` line 34 ("5 axioms" → "7 axioms + Postulate F")
- `Vol_1/Manuscript/Ch_03_*/Ch03_DRAFT.md` §3.0 footnote and L951 (replace fourth scheme)
- All Vol 1 CHAPTER_SPEC.md files for Ch02, 03, 04, 09, 11 (rewrite axiom references)
- Vol 1 Ch07 CHAPTER_SPEC — verify already-consistent
- `Vol_2/Manuscript/Ch_01_*/Ch01_DRAFT.md` §1.5.5 — canonical name on first mention then alias
- `Vol_2/Manuscript/Ch_05_*/Ch05_DRAFT.md` §5.1.7 and §5.4 alias drift

**Grep guards after edit:**
- `"five axioms"`, `"seven axioms"`, `"six axioms"` — all referenced counts must match 7
- `Axiom 1\.[1-9]` (sub-numbering) — should be zero in-scope

### 0516_Rev_004 — Five Principles canon

**CANON: Title-cased "Five Principles" (no qualifier).**

Order: **Sustaining → Conservation → Symmetry → Degradation → Duality.**

First-mention-per-chapter format:
> The Five Principles (Sustaining, Conservation, Symmetry, Degradation, Duality) ...

Biblical anchors per principle (per Vol 1 Ch 8):
- Sustaining → Col 1:17, Heb 1:3
- Conservation → Mal 3:6
- Symmetry → (existing footnote)
- Degradation → Rom 8:20
- Duality → Gen 1:27

**Files to update:**
- `Quality_Control/Reference/Five_Principles.md` — establish as canonical source if missing
- `Vol_2/Manuscript/Ch_05_*/Ch05_DRAFT.md` §5.4 — reorder + rename headings ("Constraint 1: Sustaining," etc.); verify later "Constraint N" refs still resolve
- `Vol_2/Manuscript/Ch_01_*/Ch01_DRAFT.md` §1.5 — reorder
- `Vol_4/Manuscript/Ch_11_*/Ch11_DRAFT.md` §11.5 — new paragraph anchoring gauge symmetries to Principle 3 (Symmetry); Noether currents to Principle 2 (Conservation)
- `Vol_4/Manuscript/Ch_10_Leptons_and_Quarks_from_Firmament_Resonances/Ch10_DRAFT.md` §10.1 — anchor matter generations to Principle 5 (Duality)
- `Vol_5/Manuscript/Ch_08_*/Ch08_DRAFT.md` §8.1 — one-sentence pointer to canonical `Reference/Five_Principles.md` with all five named in order
- `Vol_6/Manuscript/Ch_01_*/Ch01_DRAFT.md` §1.1 or Ch_04 — appendix/paragraph mapping each prediction class to Principle(s) it tests

**Casing normalization:** "five principles" / "Five Governing Principles" / any variant → "Five Principles" (Title Case).

### 0516_Rev_007 — ξ_A / η_B canonical scale

**CANON: 3×10²⁶ m.**

**Files to update:**
- `Vol_1/Manuscript/Ch_10_*/Ch10_DRAFT.md` (currently 1.4×10²⁶ m)
- `Vol_4/Manuscript/Ch_05_*/Ch05_DRAFT.md` (currently uses Hubble radius)
- `Quality_Control/Reference/Symbol_and_Constants.md` — if ξ_A/η_B listed, set to 3×10²⁶ m
- Series-wide audit: any other ξ_A / η_B numeric appearances should be 3×10²⁶ m

Add brief note in Vol 1 Ch10 explaining the choice and noting numerical proximity to Hubble radius (but not identifying them).

---

## Group 2 — Mechanical sweeps (parallel-safe after Group 1)

### 0516_Rev_006 — Hebrew first-mention format

**CANONICAL FORMAT:**
> The Firmament (רָקִיעַ, *rāqîʿaʾ*, 'stretched-out thing')

Order: Hebrew script → italic transliteration with macron diacriticals → English gloss in single quotes.

**Per-chapter rule in Vol 1 (which carries AppC); per-volume rule in Vols 2-6.**

**Macrons:** IMPLEMENT consistently. ā, ī, ō, ū where applicable. Update AppC C.20 to deliver on the macron promise.

**Apostrophe convention:** final-ayin uses straight apostrophe (`'`) or curly close-quote (`'`) — pick straight for source consistency.

**AppC corrections:**
- C.16: replace final-tsade (ץ) with medial form (צ); audit all C.1–C.18 root abstractions
- C.17/C.18: change "Qal perfect, vav-consecutive" → "Qal imperfect with vav-consecutive (wayyiqtol)"
- C.20: implement macrons consistently

**Files to update:**
- Vol 1: every chapter first-section mention; AppB §B.4.1; AppC §§C.5–C.6, C.16, C.17, C.18, C.20
- Vol 3 Ch 5 §5.0 L17 ("an expanse (the firmament, *raqia*)" → canonical form); Ch 5 §5.0 mayim → with Hebrew script; Ch 12 L380 italicize *tohu va-vohu*
- Vol 4 Ch 1 first use of "Firmament" → add `(*rāqîʿaʾ*; see Vol 1 Ch 5 §5.1)`; Ch 1 §1.3 first use of "Waters" → add `(*mayim*; Gen 1:2, 1:6–8; see Vol 1 Ch 6)`
- Vol 5 Ch 12 §2.1 line 92 standardize ordering
- Vol 6 Ch 10 L29 italicize *rāqîʿaʾ*; sweep for *mayim*, *bārāʾ*

### 0516_Rev_020 — Waters Above / Below pairing rule

**FORMAT (first mention per chapter section):**
> Waters Above (dark energy, ~68%)  /  Waters Below (dark matter, ~27%)

Sweep all in-scope files for unpaired first mentions per section; insert the parenthetical.

**Special case Vol 5 Ch 7:** uses Waters Above (positive-ξ) / Waters Below (positive-η) — geometric, not cosmological. KEEP geometric identification distinct; add footnote at first mention clarifying that the cosmological pairing (DE/DM) lives in Ch 6 / Ch 11 §11.0.

**Files:** Vol 2 all chapters; Vol 3 Ch 5 §5.5.1-2, Chs 8/9/10/11/12; Vol 4 Ch 5 §5.1, Ch 9 L71, Ch 14 §§14.2-14.3, Ch 4 L207; Vol 5 Chs 6/7/10/11; Vol 6 Ch 2 §2.3 (P-021/P-022), Ch 10 §§10.3/10.5, Ch 6, Ch 8, Ch 12 §12.4.

---

## Group 3 — Surgical fixes (parallel-safe)

### 0516_Rev_021 — Cross-volume cross-references

**Mechanical retargets (all from issue body):**

| Site | Old | New |
|---|---|---|
| Vol 1 Ch01 L462 | "Volume 5 (Consciousness and Agency)" | "Vol 6 Ch 13" |
| Vol 1 Ch04 L924 | "Volume 5 (General Relativity Derivation)" | "Volume 5 (The Cosmos), Chapter 1 (Einstein Field Equations Recovered)" |
| Vol 1 Ch04 L1168 | "Volume 2 (Dimensional Reduction and Gauge Theory)" | "Vol 2 Ch 5 + Ch 6 (KK decomposition)" |
| Vol 1 Ch10 L735 | "Vol 2 Ch 3 → Vol 2 Ch 5 (coupling constant derivation)" | "Vol 2 Ch 10 (coupling constant derivation)" |
| Vol 1 Ch10 L747 | "Vol 4 Ch 1 (relativistic QFT) → Vol 4 Ch 5 (interactions)" | "Vol 4 Ch 6 → Vol 4 Ch 7" |
| Vol 4 Ch14 §14.3 + Fig 4.14.3 | "Vol 5 Ch 12" | "Vol 5 Ch 8 + Ch 11 (§11.7)" |
| Vol 5 Chs 7/8/9/10/11 | "Vol 1 §6.7" | "Vol 1 §6.6.4" |
| Vol 5 Ch 8 §8.6.3 | Eqs (1.6.38)/(1.6.41) | Eqs (1.6.67)/(1.6.68)/(1.6.69) |
| Vol 5 Ch 4 | "Vol 6 Part V"/"Appendix J" | "Vol 6 Ch 13/TBD" |
| Vol 6 Ch09_DRAFT L76, Ch09_DRAFT_Part1 L73, Ch09_REVIEWS_SECONDARY L501 | "Volume 7" | "Ch 14 (Open Problems)" or "Ch 17" |

**Vol 1 Ch03 L393, L398, L400 missing Ch02 anchors:**
- **ADD** "Theorem 2.4.7", "Definition 2.4.5", "Definition 2.4.4" anchor labels to existing Ch02 §2.4 prose so Ch03 references resolve. Do not invent new content — only label.

### 0516_Rev_022 — Stream-of-consciousness debug fragments

**Vol 3 Ch01_DRAFT.md:**
- DELETE lines 222–258 (failed first variation)
- DELETE lines 446–486 (first non-relativistic-limit attempt)
- DELETE the "Hmm, I'm overcomplicating this..." sentence at L485
- DELETE the abandoned sign-flip algebra step around L483
- Keep only "Careful Derivation" §1.4 from L259
- Keep only "Cleaner Approach" subsection from L487
- Keep clean weak-field derivation: Γⁱ₀₀ = -(1/c²)∂ᵢΦ with explicit signature

**Vol 3 Ch06_DRAFT.md:**
- L464 "Wait, that does not work. Let me correct:" — DELETE this sentence; rewrite from correct claim forward

**Vol 4 P4.4.2 (back-matter selected solution):**
- "Actually, being careful with the signs..." — DELETE the scratch line; present clean derivation (per locked policy: CLEAN, not embrace)

---

## Group 4 — Vol 1 §9 editorial cluster (sequential; all touch Ch09)

### 0516_Rev_023 — M_Z dimensionality

**Ch09 §9.1 L46:** "stratified 4D manifold with 8 nested zones" → **"stratified 6D pseudo-Riemannian manifold (signature (−,+,+,+,+,+)) with 8 nested zones."**

Re-walk §9.2–§9.8 to verify the operator algebra (P̂₁ through P̂₇) is consistent with 6D base manifold. Flag any operator that assumed 4D action; ADD footnote noting the operator was originally written for 4D and confirm/correct.

### 0516_Rev_024 — Ψ_A/Ψ_B field type

**Ch09 §9.1 L51-52:** restate as **ℝ²** consistent with Ch06 §6.1.2.

Add brief footnote in Ch09 §9.1 pointing to Ch06 §6.1.2:
> Throughout Vol 1 Ψ_A and Ψ_B are real scalar fields. The Madelung complex representation Ψ_A e^{iφ_A} that appears in §9.X is a perturbation technique; the underlying fields remain real. Phase dynamics are formally treated in Vol 2 Ch 5.

### 0516_Rev_026 — "Theological Dimension" / codim-2 retrofit

**Ch04 §4.2.6 L470–511 (~40 lines):** demote the theological line to a naming-convention note.

Remove "three converging lines of argument" framing. Replace with:
> Gen 1:6–8 names the structure (firmament between waters above and below) and motivates its theological significance. The codimension count of the bulk extension is established independently by §4.2.1–§4.2.5 (mathematical) and Ch03 (cosmological observables). The biblical narrative is consistency-checked against the geometric structure; it does not derive it.

Specifically rewrite lines 487, 495, 507 (codim-2 claims) to drop the codim-2 retrofit.

### 0516_Rev_027 — Seven operators ↔ seven Days correspondence

**Ch09 §9.7 L13, 778–808, 1076–1086 + §9.0 promise:** re-cast as correspondence-not-derivation (~1.5 pp).

§9.0 PROMISE rewrite:
> Original (paraphrased): "we will derive why Genesis describes creation in exactly seven days."
> Replacement: "We will exhibit a correspondence between the seven phase-operators identified in §§9.1–9.6 and the seven Days of Genesis 1. The correspondence is observational, not derivational; each operator has independent physical justification."

§9.7 rewrite framing: parallel/correspondence note, not theorem. Operator math UNTOUCHED.

### 0516_Rev_030 — "Theorem 9.2" 4+2+1=7 partition

**Ch09 §9.6** rename heading from "Why Seven — Topological Counting Theorem" → **"Heuristic Counting Argument for Seven."**

Replace "Theorem 9.2" label with "Heuristic 9.2" or "Observation 9.2." Preserve the K3/Torelli rank-7 analogy but flag explicitly:
> The K3/Torelli rank-7 result is structurally suggestive but not a proof of the 4+2+1=7 partition; the partition is chosen to land on seven and corroborated by the K3 structure rather than derived from it.

---

## Group 5 — Vol 1 Ch 1 / Axiom 1 editorial cluster (sequential)

### 0516_Rev_025 — Axiom 1 verse-first restructure

**Ch01 §1.2.1–§1.2.4** (~2 pages, no equations change):

Restructure per Ch8 §8.4 pattern:
1. State biblical claim of continuous sustenance FIRST (Col 1:17, Heb 1:3, Ps 104:29 — quote and exegete)
2. Derive κ as formalization of "He upholds all things"
3. Fine-tuning evidence becomes CORROBORATION, not motivation

Test: deletion of Col 1:17 / Heb 1:3 / Ps 104:29 should break the chain of motivation — verses must be load-bearing, not decorative.

### 0516_Rev_028 — Acts 10:34 replacement

**Ch07 §7.3 L263:** excise Acts 10:34.

Replace with **Psalm 139:7–10:**
> Where can I go from your Spirit? Where can I flee from your presence? If I go up to the heavens, you are there; if I make my bed in the depths, you are there. If I rise on the wings of the dawn, if I settle on the far side of the sea, even there your hand will guide me.

Brief gloss: omnipresence across all spatial directions motivates SO(3) isotropy.

### 0516_Rev_029 — RT-1.WF "SUBSTANTIALLY RESOLVED" tone

**Ch04 §4.1.2 RT-1.WF box (L81):** tone "RESOLVED" → **"derived to leading order, with bulk corrections deferred."**

ADD a "Status of Warp-Factor Derivation" paragraph immediately after the box:
> (i) Analytically derived from 6D Einstein equations alone: [list]
> (ii) Fixed by matching c, G_4: [list — includes B_0 calibration]
> (iii) Open problems: OP-Bsep (Buchdahl separation), σ_ξ ≠ σ_η (anisotropy), [others]

### 0516_Rev_031 — Axiom 4 PROPOSED status

**Ch01 §1.8 counter-model 4:** strip "moral framework void" language; replace with honest physical admission.

Replacement:
> Counter-model 4 (Axiom 4 removed): Removing Axiom 4 does not currently have a known physical failure mode; the axiom is PROPOSED, and its consequences (zone-interface consciousness, prayer-as-BC-modification) are under investigation. The theological consequence — absence of an agent → world causation mechanism within the framework — is noted separately and is not offered as a physical falsifier.

Keep Axiom 4 IN the canon foundational seven; this is a clarification of independence-argument honesty.

### 0516_Rev_032 — Falsifiability inversion fix

**Ch01 §1.2 Eq (1.2.4) / §1.2.4:** replace "direct evidence for the precision of κ" with **"consistent with the precision of κ."**

ADD differential predictions paragraph:
> κ predicts a tiny secular drift Δc/c ~ 10⁻¹³/century (and parallel drifts in α, G); standard physics predicts Δc/c = 0 exactly. Current bounds (Δc/c < 10⁻¹⁰ over ~10¹⁰ yr; Δα/α < 10⁻¹⁷/yr from Oklo natural reactor; ΔG/G < 10⁻¹²/yr from lunar laser ranging) are consistent with both hypotheses. Discrimination requires next-generation experiments at 10⁻¹⁴ sensitivity.

This makes the §1.8 falsifiability test pass — Axiom 1 now has a clear differential prediction.

---

## Group 6 — Content authorship (heavy; runs last)

### 0516_Rev_019 — Genesis 1 anchoring (FULL SCOPE)

Per issue body, write new content:

**Vol 2:**
- Volume epigraph (Col 1:17 OR Job 38:4–7) — Jeff to pick or executor picks Col 1:17 by default
- Ch 1 §1.0 sidebar (~200 words) grounding Waters/Firmament in Gen 1:6–8 + pointing to Vol 1 Ch 3–4
- First-use footnote per chapter for "Waters Above/Below/Firmament": "Waters Above/Below and Firmament are structural objects derived in Vol 1 Ch 3–4 from Genesis 1:6–8."
- Paragraph each in Ch 2, Ch 3, Ch 4 tying geometric feature to Gen 1 architecture
- Ch 5 §5.4 table/footnote listing biblical anchor for each of Five Principles per Vol 1 Ch 8
- Ch 11 §11.9 closing reflection (~600 words total)

**Vol 3 Ch 1:** add 1–3 paragraphs in §1.1 or §1.5 chaining test-particle action → Firmament-as-*rāqîʿaʾ* → Gen 1:6–7. One-sentence back-references in Ch 2/3/4/10.

**Vol 4:** one-sentence first-use footnote in each of 10 chapters (Ch 1, 2, 3, 6, 7, 8, 9, 11, 13, 14) using Ch 10 §10.1 phrasing canonically. Develop Ch 11 §11.1 epigraph and Ch 13 §13.0 signs/seasons → flavor signatures. Ch 14 §14.7 paragraph anchoring all §14.2–§14.4 predictions to Gen 1:6–8.

**Vol 5:** one-sentence first-use footnote in Chs 1, 2, 3, 4, 6, 7, 8, 9, 10, 13, 14 (Ch 5 §5.0 phrasing canonical). One-paragraph Part-IV preface before Ch 12 announcing voice shift.

**Vol 6 Ch 9:** drop word "experimental" from Gen 1:14-18 passage; add extrapolation flag: "Scripture establishes that starlight reached Earth during creation week; we extrapolate the mechanism — bulk-geodesic shortcuts — on the assumption that ..." Plus motivation-not-derivation note to Gen 1:28 usage.

**Voice:** Jeff's canonical voice per `AUTHOR_VOICE_AND_BACKGROUND.md` (file may not exist yet — agent should approximate from existing Vol 1 prose tone). NEVER preach. Always answer why. Reverent but rigorous.

---

## Execution scope rules (apply to ALL tasks in B1)

**Scope IN:**
- `Vol_*/Manuscript/`
- `Vol_*/Back_Matter/`
- `Vol_*/audio book/` (regenerate via preprocess_book0.py after edits)
- `Quality_Control/Reference/`
- `Vol_*/CHAPTER_SPEC.md`, `BOOK_SPEC.md`, `QUALITY_GATE.md`
- `Research/Foundations/`, `Research/Mathematical_Models/`

**Scope OUT:**
- `/00_Archive/`, `/Reviews/`, `_pre-comprehensive`
- `*_REVIEWS.md`, `*_REVIEWER_REPORT.md`, `*_SELF_REVIEW_REPORT.md`, `*_REVIEWER_NOTES.md`, `*_SELF_REVIEW.md`, `REVIEWER_BRIEF.md`
- `BOOK_SERIES_MASTER_REVIEW_*.md`, `0516_Rev_*_TASKS.md`
- This policy lock document

**Working tree warnings:**
- DO NOT `git add -A` (pre-existing reorg unstaged)
- Stage only task-edited files via `git diff --name-only --diff-filter=M`
- Folder renames: use `mv` then `git rm -r --cached` old path + `git add` new path
- No pushes, no amends, no force-pushes

---

## Per-task execution rigor

| Group | Tasks | Rigor |
|---|---|---|
| 1 | 003, 004, 007 | Planner + Executor + Independent Validator |
| 2 | 006, 020 | Planner + Executor + Validator (mechanical sweeps) |
| 3 | 021, 022 | Single agent + post-grep verification |
| 4 | 023, 024, 026, 027, 030 | Plan + Executor + Light validator |
| 5 | 025, 028, 029, 031, 032 | Plan + Executor + Light validator |
| 6 | 019 | Drafter + Jeff review (asynchronous; agent produces drafts, Jeff approves before commit) |

**019 is the only task in B1 requiring asynchronous Jeff review** — all new authored content (sidebars, paragraphs) must be presented for Jeff approval before commit.

---

## Commit and close protocol (per task)

1. Move project board: Todo → In Progress.
2. Execute per group/rigor matrix.
3. Validate; resolve caveats.
4. Stage task-only files (see Working tree rules).
5. Commit with message ending `Closes #<num>`.
6. `gh issue close <num> --reason completed -c "..."`.
7. Move project board: In Progress → Done.
8. Update todo list.

For 0516_Rev_008 (deferred):
- Move project board: Todo → Done (skipping In Progress).
- `gh issue close 118 --reason completed -c "Deferred to a dedicated Production Sprint per B1 policy lock. Out of scope for manuscript-edit batches. See `0516_Rev_B1_POLICY_LOCK.md`."`

For 0516_Rev_005 (skipped — Jeff authors):
- LEAVE OPEN. Move project board: Todo → In Progress and add comment: "Author voice document being drafted directly by Jeff Raymond; tracked outside B1."

---

## Project board IDs (reproduced for unattended execution)

- PROJECT_ID: `PVT_kwHOB1aXSc4BTuXV`
- STATUS_FIELD_ID: `PVTSSF_lAHOB1aXSc4BTuXVzhA7W4Y`
- Options: Todo=`f75ad846` · In Progress=`47fc9ee4` · Ready for Test=`3b23bbec` · Done=`98236657`

## Issue/item map

| Task | Issue | Item ID |
|---|---|---|
| 003 | #113 | PVTI_lAHOB1aXSc4BTuXVzgs64sU |
| 004 | #114 | PVTI_lAHOB1aXSc4BTuXVzgs64tA |
| 005 | #115 | PVTI_lAHOB1aXSc4BTuXVzgs64uA |
| 006 | #116 | PVTI_lAHOB1aXSc4BTuXVzgs64uk |
| 007 | #117 | PVTI_lAHOB1aXSc4BTuXVzgs64vQ |
| 008 | #118 | PVTI_lAHOB1aXSc4BTuXVzgs64v4 |
| 019 | #119 | PVTI_lAHOB1aXSc4BTuXVzgs64ws |
| 020 | #120 | PVTI_lAHOB1aXSc4BTuXVzgs64xw |
| 021 | #121 | PVTI_lAHOB1aXSc4BTuXVzgs64yk |
| 022 | #122 | PVTI_lAHOB1aXSc4BTuXVzgs64y0 |
| 023 | #123 | PVTI_lAHOB1aXSc4BTuXVzgs64zM |
| 024 | #124 | PVTI_lAHOB1aXSc4BTuXVzgs64zk |
| 025 | #125 | PVTI_lAHOB1aXSc4BTuXVzgs64z4 |
| 026 | #126 | PVTI_lAHOB1aXSc4BTuXVzgs640U |
| 027 | #127 | PVTI_lAHOB1aXSc4BTuXVzgs6400 |
| 028 | #128 | PVTI_lAHOB1aXSc4BTuXVzgs641Y |
| 029 | #129 | PVTI_lAHOB1aXSc4BTuXVzgs6418 |
| 030 | #130 | PVTI_lAHOB1aXSc4BTuXVzgs642c |
| 031 | #131 | PVTI_lAHOB1aXSc4BTuXVzgs642o |
| 032 | #132 | PVTI_lAHOB1aXSc4BTuXVzgs643Q |

---

**END OF POLICY LOCK.**
