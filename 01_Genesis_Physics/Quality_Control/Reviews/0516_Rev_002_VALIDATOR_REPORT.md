# 0516_Rev_002 — Validator Report

**Validator:** Independent (separate agent from executor)
**Date:** 2026-05-17
**Task:** GitHub #112 — Series-wide firmament terminology sweep
**Diff plan reviewed:** `01_Genesis_Physics/Quality_Control/Reviews/0516_Rev_002_DIFF_PLAN.md`
**Style canon line:** `REVIEWER_08_The_Style_Editor.md` line 42

---

## 1. Top-line verdict

**PASS-WITH-CAVEATS.**

The mechanical sweep landed cleanly across the bulk of the in-scope tree: 762 in-scope files (matches diff-plan exact count), 20 modified Python files all compile, thermodynamic test suite all-PASS, three target folders renamed, scripture quotations preserved, approved tokens (`Firmament Domain`, `3-brane`, Randall–Sundrum / D-brane / braneworld) intact, no `Firmament Firmament` double-rewrites. However ~200 real survivors remain (≈116 `the membrane`, ≈122 compound-modifier, ≈16 real `_brane`/standalone-`brane`), several stale orphan `_clean.txt` files exist with thousands of un-swept lines, and one policy contradiction (vault in Vol 1 Ch 1 §1.7 L580) needs orchestrator decision before commit.

P0 caveats: **3**
P1 caveats: **6**

---

## 2. Section findings

### A. Grep-guard discipline

- **A1 — standalone `\bbrane\b` survivors:** **65** lines across **13 files** (after excluding RS / braneworld / D-brane / p-brane / 3-brane / `_brane` subscripts).
  - Concentrated in stale orphan `_clean.txt` files: V6 `APPENDIX_D_clean.txt` (29), V6 `APPENDIX_E_clean.txt` (10), V6 `APPENDIX_A_clean.txt` (9), V5 `APPENDIX_A/B/Problem_Se` (9 total), V6 `APPENDIX_F_clean.txt` (2). The corresponding active long-name `*_clean.txt` files contain **zero** brane survivors — verified for V6 `APPENDIX_D_Selected_Solutions_clean.txt:0`.
  - Real in-scope manuscript survivors: V4 `Ch_06.../Ch06_REVIEWER_NOTES.md:21` and V4 `Ch_07.../Ch07_REVIEWER_NOTES.md:18` (these are `Ch{NN}_REVIEWER_NOTES.md` — not on the policy #5 exclusion list, but were untouched by the executor — see P0 caveat 2).
  - Research/Foundations real misses: `AXIOM_MEMBRANE_MECHANICS_CORRECTIONS_SUMMARY.md`, `WATERS_FIELD_EQUATIONS.md`, 1 line each.
  - Research/Mathematical_Models: `06-SPECTRUM_COMPLETIONS.md`, 1 line.
  - V2 audio book `Bibliograp_clean.txt:393` — stale orphan (active version is `Bibliography_clean.txt`).

- **A2 — `\b[Tt]he membrane\b` survivors:** **116** lines across **~60 files** (excluding `the Firmament membrane`).
  - Top hot spots: `AXIOM_MEMBRANE_MECHANICS_v2.md` (5), `09-CHEMISTRY_DERIVATION.md` (4), V5 `APPENDIX_B_clean.txt` orphan (4), V4 `Ch09_REVIEWER_NOTES.md` (4 — not on policy #5 exclusion list), `10-RESOLVED_MEMBRANE_TENSION.md` (3), `AXIOM_MEMBRANE_MECHANICS.md` (3), V5 `Problem_Se_clean.txt` orphan (3), V4 `Ch07_REVIEWER_NOTES.md` (3).
  - Sample from `AXIOM_MEMBRANE_MECHANICS_v2.md`: L262 "where ρ is the mass density of matter on the membrane.", L524 "preserves the membrane wave equation", L541 "the membrane tension resists deformation", L544 "direct consequence of the membrane's extreme stiffness", L558 "Massless particles: propagate purely along the membrane." All real misses.

- **A3 — compound-modifier survivors:** **122** lines (executor reported 45). Breakdown:
  - `membrane tension` 35 + `Membrane tension` 10 + `Membrane Tension` 1 + `MEMBRANE TENSION` 1 = **47**
  - `membrane model` 23
  - `membrane vibrational` 13 + `Membrane Vibrational` 3 = **16**
  - `membrane wave` 7 + `Membrane Wave` 2 = **9**
  - `Membrane Resonance` 8 + `membrane resonance` 0 + `Membrane resonance` 1 = **9**
  - `Membrane Vibration` 7 + `membrane vibration` 3 = **10**
  - `Membrane Mode` 2 + `membrane mode` 3 = **5**
  - `membrane oscillation` 2 + `Membrane oscillation` 2 = **4**
  - Top hot files: V6 orphan `APPENDIX_A_clean.txt` (12), V6 orphan `APPENDIX_F_clean.txt` (6), V6 orphan `APPENDIX_E_clean.txt` (6), `AXIOM_MEMBRANE_MECHANICS.md` (5), V6 `Ch_02_Predictions_That_Differ/Ch02_DRAFT.md` (5 — real manuscript hits at L107, L111, L121, L405, L453: "membrane model", "membrane model"), V6 `Ch_07_Firmament_Vibration_Spectra/Ch07_DRAFT.md` L25 `## 7.2 The Membrane Eigenvalue Problem`, L280 `BOXED RESULT: The Membrane Mass Spectrum` (section titles in the *renamed* folder still say "Membrane").
  - Note: many capitalized hits are inside `## Membrane Tension` style headings.

- **A4 — LaTeX `_brane` / `\text{brane}` survivors:** **19** lines.
  - `Research/Foundations/ENERGY_FRACTIONS_DERIVATION.md`: **13** instances of `σ_brane` (e.g. L243, L245, L338, L377, L385, L435, L506, L508, L529, L537, L542, L611) — real misses, in plain ASCII subscript form so the regex `_brane` matched.
  - `Research/Mathematical_Models/10_Derivation_Chain/derive_l_eff.py`: **3** instances `[∂_n A]_brane`, `[∂_r A]_brane`, `∂_r A|_brane` (lines 202, 357, 438) — real misses in Python comments/strings.
  - `Quality_Control/Reference/Equation_Registry.md`: **2** — both explanatory ("renamed from S_brane in 0516_Rev_002"), acceptable.
  - V6 orphan `APPENDIX_F_clean.txt:216` — `d_brane` ratio token, real (in orphan file).

- **A5 — `Firmament Firmament` double-rewrites:** **0**. PASS.

- **A6 — `vault` standalone:** **11** occurrences.
  - V1 `AppC_Hebrew_Analysis_DRAFT.md:318` — terminology gloss "stretched-out sheet or vault, the sky" — acceptable lexicographic entry.
  - V1 `Ch_01.../Ch01_DRAFT.md:580` — `"Let there be a vault between the waters..." (Genesis 1:6)` — a *scripture quotation*. Policy #8 says this was supposed to be rewritten in author prose, but it is verbatim scripture. **Contradicts** the scripture-preservation rule (policy #8 first clause). NOT FIXED. See P0 caveat 1.
  - V1 `Ch_04.../Ch04_DRAFT.md:476` — full Gen 1:6-8 block quote, intentionally preserved. PASS.
  - V1 `audio book/.../Ch01_clean.txt:554` and `Ch04_clean.txt:469` — mirror the manuscript decisions above.
  - V1 `audio book/.../AppC_Hebrew_Analysis_DRAFT_clean.txt:281`, `AppC_Hebre_clean.txt:279` — terminology gloss mirror; second one is an orphan with truncated name.
  - `Research/Foundations/RESOLVED_Zone_Numbering_And_Terminology.md`: L139, L452, L464, L501 — terminology tables listing `vault` as a *forbidden* synonym to avoid. Acceptable meta-references.

### B. Folder rename integrity

- **B1 — three folders renamed on disk:** PASS.
  - `Vol_2/.../Ch_03_Electromagnetism_from_Firmament_Wave_Propagation/` exists.
  - `Vol_4/.../Ch_10_Leptons_and_Quarks_from_Firmament_Resonances/` exists.
  - `Vol_6/.../Ch_07_Firmament_Vibration_Spectra/` exists.
  - Searched `find … -type d -name "*Membrane_Wave*" -o … "Membrane_Resonance*" -o … "Membrane_Vibration*"` — zero hits. Old folders are gone.

- **B2 — stale references to old folder names anywhere in repo:** All 15 hits are in out-of-scope locations: `/Reviews/` (10), `/00_Archive/` (3), `0516_Rev_*_TASKS.md` and `BOOK_SERIES_MASTER_REVIEW_*.md` (2). No active manuscript / Reference / Research path references the old folder names. PASS.

- **B3 — git tracking of renames:** The new folders show up as untracked (`??`) and the old chapter directories show up as `D` deletions (consistent with `mv` not `git mv`). This is acceptable per the validator brief. The deletes + untracked-adds form a logical rename when staged together. Tracked correctly = yes; just not as `R` entries.

### C. Out-of-scope safety

- **C1 — modified files outside scope (M, not D):** Only 5 such files exist.
  1. `Book_0_The_Foundations/Vol_4_The_Quantum_World/QUALITY_GATE.md` — diff is purely the cascade rename "Membrane Resonances → Firmament Resonances" in the chapter index (necessary side effect of B1). Acceptable.
  2. `Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/QUALITY_GATE.md` — diff is the same cascade rename for Ch 7 title. Acceptable.
  3. `Quality_Control/BOOK_SERIES_STRATEGY.md` — 6 lines, all cascade renames of the three chapter titles ("Electromagnetism from Membrane Wave Propagation → from Firmament Wave Propagation", etc.) plus one "speed of light as membrane property → as Firmament property". Acceptable; scope-creep but bounded.
  4. `preprocess_book0.py` — patched per policy #7. Verified benign (F1).
  5. `REVIEWER_08_The_Style_Editor.md` — patched per the diff plan's Phase 6. Line 42 now reads as authoritative.
  - **Conclusion:** No out-of-scope file was substantively modified. All five "outside Manuscript/Back_Matter/audio book/Reference/Research" edits are cascade-rename consequentials. No edits to /Reviews/ tree, master TASKS, master review, /00_Archive/, or _pre-comprehensive paths.

- **C2 — QA artifact bodies (per policy #5):** No `*_REVIEWS.md`, `*_REVIEWER_REPORT.md`, `*_SELF_REVIEW_REPORT.md`, or `REVIEWER_BRIEF.md` file inside an active chapter folder is modified. All such file paths under `git diff --name-only` show status `D` (the deletes from the pre-existing reorg) — i.e. they were deleted at the *old* location and the *new* (untracked) location's copies have not been edited by this executor. PASS.

### D. Approved-token integrity

- **D1 — `Firmament Domain` IN-SCOPE:** HEAD count 37 → working count 42. Token preserved (and slightly added to via Glossary clarification). PASS.
- **D2 — `3-brane` IN-SCOPE:** HEAD 114 → working 116. Preserved verbatim. PASS.
- **D3 — Randall–Sundrum / braneworld / RS-model / D-brane IN-SCOPE:** HEAD 173 → working 165. Drop of 8. Likely from sweep of folder names and ancillary cleanup. Within tolerance (~5%). PASS.

### E. Reference docs

- **E1 — `Glossary.md`:** Firmament Domain defined at L20 ("The full domain comprising the Firmament membrane (Z₂.₂.₂) and its immediate enclosing structure. … The two-word phrase 'Firmament Domain' is the only acceptable name for Z₂.₂."). Cross-referenced at L18 (in The Firmament entry) and L108 (Zone 2.2.2 entry). PASS.
- **E2 — `Symbol_and_Constants.md`:** L16 still reads `Firmament membrane 3-brane tension; fundamental creation parameter`. `3-brane` preserved verbatim, NOT rewritten to `3-surface`. PASS.
- **E3 — `Equation_Registry.md`:** `_Firm` subscripts present (2 occurrences). 2 `_brane` references remain, both inside explanatory text noting the rename — e.g. L51 `Note: the Firmament-sector subscript is renamed from S_brane → S_Firm in 0516_Rev_002`. Acceptable; not a regression.
- **E4 — `REVIEWER_08_The_Style_Editor.md`:** L42 now reads the locked policy verbatim, including `"Firmament Domain" (two words, capitalized) for the full Zone 2.2 region` and `"3-brane" preserved verbatim`. Forbidden list still intact: `NEVER: "dome," "vault," "sky," "brane" standalone (other than '3-brane'), "the membrane" alone, "the expanse" alone`. PASS.

### F. Audiobook regeneration

- **F1 — `preprocess_book0.py` patch:** Diff is 6 added lines in `discover_chapters()` extending the search to also look inside `vol_dir / 'Manuscript'` for `Ch_NN` folders. Pre-patch the function only searched `vol_dir` directly; post-patch it searches both. This exactly fixes the reorg-induced discovery gap. No side effects, no broader behavior change. PASS.
- **F2 — clean.txt spot check (V2 Ch03, V4 Ch10, V6 Ch07):**
  - `Vol_2/audio book/chapters/Ch03_clean.txt`: 0 brane, 0 "the membrane". PASS.
  - `Vol_4/audio book/chapters/Ch10_clean.txt`: 0 brane, 0 "the membrane". PASS.
  - `Vol_6/audio book/chapters/Ch07_clean.txt`: 0 brane, **2 "The Membrane"** (L21 `The Membrane Eigenvalue Problem.`, L264 `BOXED RESULT: The Membrane Mass Spectrum`). These are downstream of the manuscript Ch07_DRAFT.md which still has the same section titles (L25, L280). Real survivors propagated from manuscript headings.
- **F3 — stale orphan `_clean.txt` files:**
  - Vol 5 orphans (short-name): `APPENDIX_A_clean.txt`, `APPENDIX_B_clean.txt`, `APPENDIX_C_clean.txt`, `Problem_Se_clean.txt` (active ones use the full long form, e.g. `APPENDIX_A_Foundational_Equations_clean.txt`).
  - Vol 6 orphans: `APPENDIX_A_clean.txt`, `APPENDIX_B_clean.txt`, `APPENDIX_D_clean.txt`, `APPENDIX_E_clean.txt`, `APPENDIX_F_clean.txt`, `Bibliograp_clean.txt`, `Bibliography_clean.txt` (the active long-form companion exists for each: `APPENDIX_A_Complete_Prediction_clean.txt`, etc.).
  - Vol 2: `Bibliograp_clean.txt` (orphan; active is `Bibliography_clean.txt`).
  - Vol 3: `APPENDIX_A_clean.txt`, `Problem_Se_clean.txt` (orphans).
  - Vol 1: `AppC_Hebre_clean.txt` (orphan; active is `AppC_Hebrew_Analysis_DRAFT_clean.txt`).
  - **Verified orphan status:** the JSON manifests (`chapter_titles_VolN.json`) reference only the long-name versions; the short-name versions are not referenced anywhere I could find.
  - **Recommendation:** delete all of these orphans in this commit (they are pure noise and account for ~70% of the apparent A1/A3 survivors). This converts roughly 60+ "real" survivors into 0.

### G. Python correctness

- **G1 — `py_compile` on all 20 modified `.py` files under `Research/`:** all 20 OK. No syntax regressions.
- **G2 — domain test runner:** Ran `python 01_Genesis_Physics/Research/Mathematical_Models/02_Thermodynamics/test_thermodynamic_laws.py` with `PYTHONIOENCODING=utf-8`. Result: **ALL TESTS PASSED ✓✓✓** (Second Law, Third Law, Boltzmann, Carnot, Heat Capacity). Executor's "tests pass" claim verified for this subset.

### H. Specific spot-checks

- **H1 — Vol 6 Ch 15 L120:** Confirmed. Line reads `Worldsheet CFT modes plus D-brane intersections vs. topological defects on the Firmament plus membrane modes.` The RS-skip rule kept "D-brane intersections" intact (correct), but the trailing `plus membrane modes` is in author prose contrasting two programs and should have been rewritten to `plus Firmament modes` (or `plus Firmament membrane modes` if mechanics context — and given that the sentence is naming the mode-generating mechanism, mechanics-context is appropriate). **Recommended fix:** change `plus membrane modes` → `plus Firmament membrane modes` on that one line. Other lines in the same chapter (L132, L212) already use `Firmament membrane modes` correctly, so this edit aligns with the chapter's own pattern.

- **H2 — `membrane vibrational` / `membrane model` compound coverage:** Confirmed and worse than executor reported (executor said 45; I count 122). The policy #4 compound list explicitly mentioned: tension, wave, oscillation, resonance, framework, interpretation, picture, vibration. `model` and `vibrational` were not on that list but are clearly the same pattern. **Policy clarification needed** from orchestrator: confirm both go to `Firmament model` / `Firmament vibrational` (or the technical-mechanics carve-out `Firmament membrane model` / `Firmament membrane vibrational`). Once clarified, a follow-up mechanical pass will clean ≈40 lines.

- **H3 — Vol 1 Ch 4 §4.2 vault:** Verified. L476 is a verbatim block-quote of Gen 1:6-8 introduced by `Genesis 1 describes creation: > "And God said, 'Let there be a vault between the waters…'"`. Correctly preserved as scripture. NOT in author prose. PASS.

---

## 3. Caveats requiring orchestrator action (ranked by severity)

### P0 (block commit)

1. **Vol 1 Ch 1 §1.7 L580 vault** — policy contradiction. Policy #8 says "rewritten in author prose" but the line is a verbatim quotation of Genesis 1:6 with quote marks and citation. Cannot rewrite a scripture quotation in author prose without altering scripture (which policy #8's lead clause forbids). **Orchestrator must choose one of:** (a) replace the quoted scripture with an *author paraphrase* of the same idea (no quote marks, no citation), or (b) drop the requirement and leave the verbatim Gen 1:6 quote in place. The current state has the quote untouched; if (a) is the answer, the manuscript and the V1 Ch01 `_clean.txt` need a coordinated edit before commit.

2. **`Ch{NN}_REVIEWER_NOTES.md` exclusion ambiguity** — policy #5 explicitly excluded `*_REVIEWS.md`, `*_REVIEWER_REPORT.md`, `*_SELF_REVIEW_REPORT.md`, `REVIEWER_BRIEF.md`. It did NOT mention `*_REVIEWER_NOTES.md`. Files of that name in the new untracked Manuscript chapter folders (V4 Ch06/Ch07/Ch09 at least) contain combined ~10+ `brane`/`the membrane`/compound survivors. **Orchestrator must declare:** are `*_REVIEWER_NOTES.md` QA artifacts (skip) or active reference material (sweep)? Same question for `Ch*_SELF_REVIEW.md` (note: distinct from `_SELF_REVIEW_REPORT.md`).

3. **Real `_brane` LaTeX subscript misses in `ENERGY_FRACTIONS_DERIVATION.md` (13 lines) and `derive_l_eff.py` (3 lines)** — policy #1 ("subscripts everywhere → `_Firm`") was violated. These are ASCII subscripts (`σ_brane`, `[∂_n A]_brane`), not LaTeX braces, so the executor's regex likely missed them. **Required fix:** another mechanical pass on `_brane\b` (plain word, not just inside `\{…\}`).

### P1 (fix before merge, but not blockers)

4. **Section headings inside renamed folder are stale.** V6 `Ch_07_Firmament_Vibration_Spectra/Ch07_DRAFT.md` still has `## 7.2 The Membrane Eigenvalue Problem` (L25) and `BOXED RESULT: The Membrane Mass Spectrum` (L280). These propagate into the corresponding `_clean.txt`. Inconsistent with the folder name.

5. **Vol 6 Ch 15 L120** — see H1. One-line edit recommended.

6. **Compound modifier policy clarification (H2)** — `model` and `vibrational` not explicitly listed; ~40 lines pending policy decision.

7. **Stale orphan `_clean.txt` files** — ~12 files across V1/V2/V3/V5/V6 (short-name duplicates). Recommend deletion in this commit. Removes ~60+ A1/A3 "survivors" that are pure noise. If kept, they will keep showing up in every future grep audit.

8. **Real `the membrane` / compound survivors in active manuscript and Research files** (≈90 lines after orphans are removed). Hot files: `AXIOM_MEMBRANE_MECHANICS_v2.md`, `AXIOM_MEMBRANE_MECHANICS.md`, V6 `Ch_02_Predictions_That_Differ/Ch02_DRAFT.md`, `09-CHEMISTRY_DERIVATION.md`, `10-RESOLVED_MEMBRANE_TENSION.md`. Mechanical pass needed.

9. **Equation_Registry.md still mentions `S_brane` and `\mathcal{L}_\text{brane}` in two explanatory notes.** Acceptable as audit-trail commentary, but the orchestrator may want to fold those notes into a single migration note at the top of the file rather than leaving the old form inline.

---

## 4. Out-of-scope safety statement

**No out-of-scope file was substantively modified.** The five files modified outside the strict Manuscript/Back_Matter/audio book/Reference/Research roots — two Volume `QUALITY_GATE.md` files, `BOOK_SERIES_STRATEGY.md`, `preprocess_book0.py`, and `REVIEWER_08_The_Style_Editor.md` — are all either (a) explicit policy carve-outs (#7 for the preprocess script; the diff plan's Phase 6 for REVIEWER_08) or (b) load-bearing cascade renames consequent to the three B1 folder renames (the QUALITY_GATE / BOOK_SERIES_STRATEGY entries that name those chapters). Edits to `/Reviews/` tree, master TASKS, master review, `/00_Archive/`, and `_pre-comprehensive` paths: **zero** in `M` status. The huge volume of `D` and `??` status entries elsewhere in the working tree is the pre-existing reorganization that was already underway before this task — not work attributable to this executor.

---

## 5. Spot-check evidence

Three short before/after excerpts from `git diff HEAD`:

**Excerpt 1 — `Research/Foundations/AXIOM_MEMBRANE_MECHANICS_v2.md` L8, L61, L84:**
```
- > | Modern Equivalent | Elastic wave dynamics, brane cosmology | …
+ > | Modern Equivalent | Elastic wave dynamics, Firmament cosmology | …

- **Physical interpretation**: The membrane (a 4D hypersurface in 6D spacetime) has an elastic energy density. … a 4D elastic membrane has **3-brane tension** with dimensions [energy/3-volume].
+ **Physical interpretation**: The Firmament membrane (a 4D hypersurface in 6D spacetime) has an elastic energy density. … a 4D elastic membrane has **3-brane tension** with dimensions [energy/3-volume].

- Wait—this requires clarification. The classical 2D membrane wave speed is v² = T/ρ …
+ Wait—this requires clarification. The classical 2D Firmament membrane wave speed is v² = T/ρ …
```
Shows: bare `membrane` → `Firmament membrane` carve-out applied in mechanics context; standalone `brane` → `Firmament` applied; `3-brane` preserved verbatim. Exactly the locked policy.

**Excerpt 2 — `Quality_Control/BOOK_SERIES_STRATEGY.md` Ch 3 V2 row:**
```
- | 3 | *Electromagnetism from Membrane Wave Propagation* | Maxwell's equations derived from Firmament vibration modes. Speed of light as membrane property. Gauge invariance from zone symmetry. … |
+ | 3 | *Electromagnetism from Firmament Wave Propagation* | Maxwell's equations derived from Firmament vibration modes. Speed of light as Firmament property. Gauge invariance from zone symmetry. … |
```
Shows: chapter title cascade rename and inline `membrane property` → `Firmament property` correction.

**Excerpt 3 — `Book_0_The_Foundations/preprocess_book0.py` L300-319 (executor patch to `discover_chapters`):**
```
- def discover_chapters(vol_dir: Path) -> list[dict]:
-     """Return ordered list of {key, title_hint, file_path} for all chapters."""
-     chapter_dirs = sorted(
-         [d for d in vol_dir.iterdir() if d.is_dir() and re.match(r'Ch[\d_]', d.name)],
-         key=_chapter_sort_key,
-     )
+ def discover_chapters(vol_dir: Path) -> list[dict]:
+     """Return ordered list of {key, title_hint, file_path} for all chapters.
+
+     Looks in vol_dir itself AND in vol_dir/Manuscript for Ch_NN folders.
+     """
+     candidates = []
+     for d in vol_dir.iterdir():
+         if d.is_dir() and re.match(r'Ch[\d_]', d.name):
+             candidates.append(d)
+     manuscript_dir = vol_dir / 'Manuscript'
+     if manuscript_dir.exists():
+         for d in manuscript_dir.iterdir():
+             if d.is_dir() and re.match(r'Ch[\d_]', d.name):
+                 candidates.append(d)
+     chapter_dirs = sorted(candidates, key=_chapter_sort_key)
```
Shows: minimal, well-scoped patch — adds `Manuscript/` subfolder discovery while preserving existing direct-child discovery. Benign per F1.

---

**End of validator report.**
