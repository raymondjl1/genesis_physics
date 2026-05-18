# 0516_Rev_002 — Series-Wide Firmament-Terminology Sweep — DIFF PLAN

**Issue / Task:** GitHub #112 / 0516_Rev_002
**Reviewer:** REVIEWER-08 (Style Editor), with consistency checks by REVIEWER-04
**Status:** PLAN ONLY — no edits performed.
**Style canon (locked):** Primary term is "The Firmament." Acceptable: "The Firmament membrane" in technical contexts. **Forbidden standalone:** `brane`, `the membrane`, `dome`, `vault`, `sky`, `the expanse`. Source: `01_Genesis_Physics/Quality_Control/Reviewers/REVIEWER_08_The_Style_Editor.md` line 42.

This plan is exhaustive. Every regex below was test-fired against the working tree on 2026-05-17. Counts are line-level hit counts within the in-scope set (see Scope).

---

## Scope

### IN scope (all greps confined to these roots)
```
01_Genesis_Physics/Book_0_The_Foundations/Vol_1_Architecture_of_Reality/Manuscript
01_Genesis_Physics/Book_0_The_Foundations/Vol_1_Architecture_of_Reality/audio book
01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/Manuscript
01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/audio book
01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/Back_Matter
01_Genesis_Physics/Book_0_The_Foundations/Vol_3_Matter_and_Motion/Manuscript
01_Genesis_Physics/Book_0_The_Foundations/Vol_3_Matter_and_Motion/audio book
01_Genesis_Physics/Book_0_The_Foundations/Vol_3_Matter_and_Motion/Back_Matter
01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Manuscript
01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/audio book
01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Back_Matter
01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/Manuscript
01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/audio book
01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/Back_Matter
01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Manuscript
01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/audio book
01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Back_Matter
01_Genesis_Physics/Quality_Control/Reference
01_Genesis_Physics/Research/Foundations
01_Genesis_Physics/Research/Mathematical_Models
01_Genesis_Physics/Research/Simulations
```
File-type filter: `*.md *.tex *.py *.txt *.json *.yaml *.yml *.csv`. Total in-scope file count: **762**.

### OUT of scope (always excluded; path-substring filter)
- `/00_Archive/` (any depth)
- `/Reviews/` (any depth — but this plan itself lives at `Quality_Control/Reviews/`; the *file* `0516_Rev_002_DIFF_PLAN.md` is the only edit target inside it)
- `_pre-comprehensive` (substring)
- `0516_Rev_*_TASKS.md`
- `BOOK_SERIES_MASTER_REVIEW_*`
- `/REVIEWER_*.md` (the reviewer persona docs — **except** the Style Editor doc explicitly listed in Phase 6, which the executor will update by exact path)
- All of `Book_1_Hidden_Architecture/` (per Jeff's exclusion of the Book 1 "Membrane Between Worlds" chapter; Book 1 has its own deferred sweep)
- All of `Book_2_The_Hidden_Architecture/` and `Book_3_The_Creators_Blueprint/` (archival / different style sheet)

Validator exclude regex (used in every grep below):
```
EXCL='(/00_Archive/|/Reviews/|_pre-comprehensive|0516_Rev_.*_TASKS\.md|BOOK_SERIES_MASTER_REVIEW_|/REVIEWER_)'
```

---

## 1 — Summary (counts after exclusions)

| Metric | In-scope total | Files touched |
|---|---:|---:|
| `\bbrane\b` (standalone, all) | **4 695** lines | 317 |
| `\bbrane\b` minus RS-preservation lines | **3 379** lines | 317 |
| `\b[Tt]he membrane\b` | **2 187** lines | 338 |
| `\bmembrane\b` (any, for context) | 5 862 | — |
| Randall-Sundrum / RS / braneworld family (preserve verbatim) | **162** lines | — |
| Compound-modifier matches (`membrane {tension,wave,oscillation,resonance,stiffness,fluctuation,rigidity,mode,vibration,excitation}`) | **1 386** lines | 348 |
| `\bdome\b` (in scope) | 11 | All inside reviewer/style commentary; no author-prose hits |
| `\bvault\b` (in scope) | 25 | 3 author-prose hits (see Phase 5); rest are biblical quotes or terminology tables |
| `\bsky\b` (in scope) | 106 | All biblical-quote / Hebrew analysis / atmospheric — preserve |
| `\bthe expanse\b` (in scope) | 25 | All Hebrew-translation discussion — preserve |
| LaTeX subscript total (all `…brane` subscripts) | **74** occurrences across 21 distinct forms (see Phase 3) | — |

Compound-modifier breakdown (per-modifier line count, **before** "Firmament X" remap):

| Modifier | Hits |
|---|---:|
| `membrane tension` | 465 |
| `membrane mode` | 393 |
| `membrane wave` | 191 |
| `membrane vibration` | 141 |
| `membrane resonance` | 68 |
| `membrane excitation` | 68 |
| `membrane oscillation` | 61 |
| `membrane fluctuation` | 17 |
| `membrane stiffness` | 7 |
| `membrane rigidity` | 2 |

Estimated **total replacements this commit**: standalone `brane` (3 379) + `the membrane → the Firmament` (≈1 800 after compound carve-outs) + compound `membrane X → Firmament X` (≈1 386) + LaTeX subscripts (74) + 3 folder renames + ~12 path cascade refs + 7 inline-title fixes + 4 reference-doc updates = **≈ 6 650 line-level operations** plus 3 directory operations.

---

## 2 — Phase 1: Mechanical regex passes

All passes run in this order. Each pass uses Perl-style replacement and **must respect line-level allowlists** (RS preservation, fenced code blocks, biblical quotes). The executor should implement as a Python pass with per-file read/write rather than a streaming `sed`; counts above will confirm correctness.

### 1.1 Standalone `\bbrane\b` → `Firmament`

**Regex (match):** `\bbrane\b`
**Replacement logic per match:**

1. **Skip the entire line** if it matches any of:
   - `[Rr]andall[- ]?[Ss]undrum`
   - `\bbraneworld\b`
   - `\bbrane[- ]world\b`
   - `\bRS\s+model\b`
   - `\bD-?brane\b` / `\bp-?brane\b` (string-theory external nomenclature — preserve)
2. **Skip if the match is inside a fenced code block.** Track ``` ``` toggles per file.
3. **Skip if the match is a LaTeX subscript** — i.e. preceded by `_` or `_{` or `_\text{` or `_\rm ` or `_\mathrm{`. Those are handled by Phase 3.
4. **Skip if the match is inside an inline math context** that is itself a subscript-only fragment (rare; covered by 3).
5. **Capitalization:** preserve the leading capitalization of the surrounding clause. The token `brane` is always lowercase in source today; replace with `Firmament` (capital F) when it begins a sentence, replace with `Firmament` otherwise (always capitalize — "The Firmament" is the canonical noun). When the source phrase is `the brane`, `a brane`, `our brane`, etc., the replacement is `the Firmament`, `the Firmament`, `our Firmament` (Jeff's locked-in policy 4: `the membrane → the Firmament`; same applies to `the brane`).
6. **Compound phrases** in author prose:
   - `brane sector` → `Firmament sector`
   - `brane tension` → `Firmament tension` (this duplicates Phase 2 logic; safe — idempotent)
   - `brane stiffness` → `Firmament stiffness`
   - `brane fluctuation(s)` → `Firmament fluctuation(s)`
   - `brane mode(s)` → `Firmament mode(s)`
   - `brane wave(s)` → `Firmament wave(s)` (when the prose is about mechanics use `Firmament membrane wave(s)`; Phase 2 disambiguates)
   - `brane dynamics` → `Firmament dynamics`
   - `brane stress-energy` → `Firmament stress-energy`

### 1.2 `\b[Tt]he membrane\b` → `the Firmament`

**Regex:** `\b[Tt]he membrane\b`
**Replacement:**
- Default: `the Firmament` (preserve case of "The"/"the")
- **Carve-out:** if the same line already matches `(membrane (tension|wave|oscillation|resonance|stiffness|fluctuation|rigidity|mode|vibration|excitation|mechanics|dynamics|equation|spectrum|spectra|surface|theory|action|stress|energy|coupling|bending|deflection|displacement|sigma))`, then leave the noun-phrase carve-out for Phase 2 (which rewrites the compound to `Firmament X` or `Firmament membrane X` — Phase 2 fires before this default).
- **Code-fence & RS-line skips** as above.

### 1.3 Bare `\bmembrane\b` (no determiner) — POLICY: do NOT mechanically rewrite

After 1.1, 1.2, and Phase 2, the remaining `membrane` occurrences are almost all inside:
- Compound nouns Phase 2 will have handled (`membrane tension`, etc.).
- The phrase `Firmament membrane` (already canonical-acceptable per style sheet).
- Biological references ("cell membrane," "soap-film membrane analogy," "lipid membrane") — preserve.
- Reviewer commentary (excluded by scope).

Phase 7 grep will flag any survivors for hand review. Do **not** mechanically rewrite generic `membrane` after Phases 1-2 run; the false-positive rate on biological analogies (Vol 1 Ch 5 §5.4 "soap-film" passage; Vol 6 Ch 10 cochlear-mechanics passage) is too high.

---

## 3 — Phase 2: Compound-modifier disambiguation

Rule:
- If the prose around the compound is **about membrane mechanics** (tension, wave propagation, vibration, oscillation, resonance, stiffness, rigidity, fluctuation, modes, excitation, dynamics, spectrum), use **"Firmament membrane X"** because Style Editor §42 says "The Firmament membrane" is acceptable in technical mechanics contexts.
- If the prose is **not** about mechanics (e.g. "membrane tension parameter σ" appearing in a parameter table — context is just the symbol's name), use **"Firmament tension"**.
- Practical heuristic for the executor: **apply the simple rule** "if the modifier is one of {tension, mode, wave, vibration, resonance, oscillation, fluctuation, stiffness, rigidity, excitation} **and** the same paragraph contains any of {σ, μ, dispersion, eigenfrequency, eigenmode, Nambu-Goto, Helfrich, Israel junction, sound speed, wave speed}, rewrite to `Firmament membrane X`. Otherwise rewrite to `Firmament X`."
- This heuristic is **conservative**: the executor should print every match with surrounding 1-line context to a review log; ambiguous cases (≈5% of hits — see Phase 9) get queued for hand review.

### Compound-modifier hot files (top 25 by hit count — 348 files total)

Top files (count of compound-modifier lines):
```
35 Vol_1/Manuscript/Ch_10_Quantization_from_Boundary_Conditions/Ch10_DRAFT.md
31 Vol_1/audio book/chapters/Ch10_clean.txt
28 Vol_6/Manuscript/Ch_07_Membrane_Vibration_Spectra/Ch07_DRAFT.md       ← rename per Phase 4
24 Vol_6/audio book/chapters/Ch07_clean.txt
18 Vol_6/Manuscript/Ch_03_Novel_Predictions/Ch03_DRAFT.md
17 Research/Mathematical_Models/02_Thermodynamics/test_thermodynamic_laws.py
17 Vol_6/Manuscript/Ch_07_Membrane_Vibration_Spectra/Ch07_REVIEWS.md       ← in /Reviews-style/ but excluded by ".../Reviews/" rule? — keep, see note
17 Vol_1/Manuscript/Ch_10_Quantization_from_Boundary_Conditions/CHAPTER_SPEC.md
16 Research/Mathematical_Models/10_Fundamental_Constants/10-FUNDAMENTAL_CONSTANTS_OVERVIEW.md
16 Research/Mathematical_Models/08_Cosmology/08-ENERGY_EXTRACTION_CREATION.md
16 Vol_6/audio book/chapters/Ch03_clean.txt
16 Vol_6/Manuscript/Ch_12_Advanced_Sensors/Ch12_DRAFT.md
16 Vol_1/Manuscript/Ch_11_Thermodynamics_from_Zone_Separation/Ch11_Thermodynamics_from_Zone_Separation.md
15 Vol_6/audio book/chapters/Ch12_clean.txt
15 Vol_6/Manuscript/Ch_15_Connections_to_Other_Programs/Ch15_DRAFT.md
15 Vol_3/Manuscript/Ch_07_The_Origin_of_Mass/Ch07_DRAFT.md
15 Vol_1/audio book/chapters/Ch11_clean.txt
15 Vol_1/Manuscript/Ch_05_The_Firmament_Manifold/Ch05_DRAFT.md
14 Vol_6/audio book/chapters/Ch15_clean.txt
14 Vol_6/audio book/chapters/Ch05_clean.txt
14 Vol_6/Manuscript/Ch_05_Simulation_Methodology/Ch05_DRAFT.md
14 Vol_1/audio book/chapters/Ch05_clean.txt
13 Research/Mathematical_Models/05_Quantum_Mechanics/05-QED_PRECISION_CALCULATIONS.md
13 Vol_6/Manuscript/Ch_07_Membrane_Vibration_Spectra/CHAPTER_SPEC.md
13 Vol_6/Back_Matter/Master_Index.md
```
*Note on `Ch07_REVIEWS.md`*: file name starts with `Ch07_REVIEWS` but the scope-exclude rule keys on the **path segment** `/Reviews/` (a directory), not the filename suffix `_REVIEWS.md`. So `Ch07_REVIEWS.md` and `*_REVIEWS.md` files are NOT excluded by `/Reviews/`. The Style-Editor scope brief did not explicitly exclude review reports inside chapter folders. **Recommendation:** the executor should leave per-chapter `*_REVIEWS.md` / `REVIEWER_REPORT.md` / `SELF_REVIEW_REPORT.md` files **untouched** by Phases 1–3 (these are historical QA artifacts whose value is preserving the as-of-then text), but Phase 6 reference-doc updates must still be applied. **This is a scope question flagged in Phase 9.**

Full per-file list of the 348 compound-modifier files is at `/tmp/rev002/perfile_compounds.txt` (regenerable from the regex below). Inline-listing all 348 here would 10× the size of this plan; the executor should regenerate the list as the first step of its run.

**Executor regeneration command** (canonical):
```bash
grep -rnE --include='*.md' --include='*.tex' --include='*.py' --include='*.txt' \
  '\bmembrane (tension|wave|oscillation|resonance|stiffness|fluctuation|rigidity|mode|vibration|excitation)' \
  <each in-scope root> 2>/dev/null \
| grep -vE "$EXCL" \
| tee compound_hits.log
```

### 2.1 Replacement rules table

| Source phrase | Default replacement | Mechanics-context replacement |
|---|---|---|
| `membrane tension` | `Firmament tension` | `Firmament membrane tension` |
| `membrane wave` | `Firmament wave` | `Firmament membrane wave` |
| `membrane wave equation` | (same) | `Firmament membrane wave equation` |
| `membrane oscillation` | `Firmament oscillation` | `Firmament membrane oscillation` |
| `membrane resonance` | `Firmament resonance` | `Firmament membrane resonance` |
| `membrane stiffness` | `Firmament stiffness` | `Firmament membrane stiffness` |
| `membrane fluctuation(s)` | `Firmament fluctuation(s)` | `Firmament membrane fluctuation(s)` |
| `membrane rigidity` | `Firmament rigidity` | `Firmament membrane rigidity` |
| `membrane mode(s)` | `Firmament mode(s)` | `Firmament membrane mode(s)` |
| `membrane vibration` | `Firmament vibration` | `Firmament membrane vibration` |
| `membrane excitation(s)` | `Firmament excitation(s)` | `Firmament membrane excitation(s)` |
| `membrane mechanics` | `Firmament membrane mechanics` (always mechanics ctx) | — |
| `membrane dynamics` | `Firmament dynamics` (or `Firmament membrane dynamics` if mechanics ctx) | — |
| `membrane equation` | `Firmament wave equation` (always mechanics) | — |
| `membrane spectrum/spectra` | `Firmament membrane spectrum` | — |
| `membrane bending energy` | `Firmament membrane bending energy` | — |
| `membrane stress-energy` | `Firmament stress-energy` | `Firmament membrane stress-energy` |
| `membrane displacement` | `Firmament membrane displacement` | — |
| `membrane deflection` | `Firmament membrane deflection` | — |

---

## 4 — Phase 3: LaTeX subscript renames (`*_{brane}` → `*_{Firm}`)

Per locked-in policy 1: rename **every** subscript form whose tail is `brane` (any LaTeX wrapper) to `Firm`. The dominant Lagrangian symbol `\mathcal{L}_{\rm brane}` / `\mathcal{L}_\text{brane}` → `\mathcal{L}_{\rm Firm}` / `\mathcal{L}_\text{Firm}`.

### 4.1 Distinct subscript forms found in scope (with counts)

```
14  H_\text{brane}            → H_\text{Firm}
12  rho_\text{brane}          → rho_\text{Firm}     (note: appears as \rho_\text{brane})
 6  S_\text{brane}            → S_\text{Firm}
 5  y_brane                   → y_Firm
 5  \mathcal{L}_\text{brane}  → \mathcal{L}_\text{Firm}
 4  d_brane                   → d_Firm
 4  S_brane                   → S_Firm
 4  O_\text{brane}            → O_\text{Firm}
 4  K_\text{brane}            → K_\text{Firm}
 2  s_brane                   → s_Firm
 2  r_brane                   → r_Firm
 2  \mathcal{L}_{\rm brane}   → \mathcal{L}_{\rm Firm}
 2  L_brane                   → L_Firm
 1  t_{\rm brane}             → t_{\rm Firm}
 1  int_\text{brane}          → int_\text{Firm}   (probably `\int_\text{brane}` integral limit)
 1  g_brane                   → g_Firm
 1  dS_\text{brane}           → dS_\text{Firm}
 1  V_\text{brane}            → V_\text{Firm}
 1  T_{brane}                 → T_{Firm}
 1  Psi_\mathrm{brane}        → Psi_\mathrm{Firm}  (appears as `\Psi_\mathrm{brane}`)
 1  A_brane                   → A_Firm
─────────────────────────────
74  total subscript replacements
```

### 4.2 Mechanical sed-equivalent rules (apply in order)

The executor should use these **Python regex** substitutions (not `sed`, since GNU grep 3.0 on Win10 has BRE/ERE quirks with `{}`). The regex `r'\\text\{brane\}'` is safe in Python.

```python
import re
PASS = [
  (re.compile(r'\\text\{brane\}'),    r'\\text{Firm}'),
  (re.compile(r'\\mathrm\{brane\}'),  r'\\mathrm{Firm}'),
  (re.compile(r'\{\\rm brane\}'),     r'{\\rm Firm}'),
  (re.compile(r'\{\\text brane\}'),   r'{\\text Firm}'),
  (re.compile(r'\{\\mathrm brane\}'), r'{\\mathrm Firm}'),
  # plain bracketed
  (re.compile(r'\{brane\}'),          r'{Firm}'),
  # bareword subscript: _brane immediately after a single-letter symbol or word-char
  (re.compile(r'(?<=[A-Za-z])_brane\b'), r'_Firm'),
]
```
Run order matters: process `\text{brane}` / `\mathrm{brane}` BEFORE `_brane` so the `_brane` regex doesn't fire inside `_\text{brane}` constructs (it wouldn't — `_` is followed by `\`, not by `b` — but ordering keeps the diff readable).

### 4.3 Equation_Registry.md update

`01_Genesis_Physics/Quality_Control/Reference/Equation_Registry.md` has exactly one `brane`-mentioning line:

| Line | Now | After |
|---:|---|---|
| 33 | `\| (1.5.2) \| Extrinsic Curvature \| Volume 1 \| 1 \| 5 \| Extrinsic curvature tensor K_ij of Firmament hypersurface; encodes membrane bending energy \|` | `\| (1.5.2) \| Extrinsic Curvature \| Volume 1 \| 1 \| 5 \| Extrinsic curvature tensor K_ij of Firmament hypersurface; encodes Firmament membrane bending energy \|` |

Plus: **add new entries** (or annotate existing ones) for `\mathcal{L}_\text{Firm}` (Vol 2 Ch 5 §5.4 Eq 2.5.4) and `S_\text{Firm}` (Eq 2.5.1 & 2.5.4) so the rename is documented. Phase 6 (Reference doc updates) carries this.

---

## 5 — Phase 4: Folder renames + cascade

### 5.1 `git mv` commands (run in order; do not stage other changes between them)

```bash
git mv "01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/Manuscript/Ch_03_Electromagnetism_from_Membrane_Wave_Propagation" \
       "01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/Manuscript/Ch_03_Electromagnetism_from_Firmament_Wave_Propagation"

git mv "01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Manuscript/Ch_10_Leptons_and_Quarks_from_Membrane_Resonances" \
       "01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Manuscript/Ch_10_Leptons_and_Quarks_from_Firmament_Resonances"

git mv "01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Manuscript/Ch_07_Membrane_Vibration_Spectra" \
       "01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Manuscript/Ch_07_Firmament_Vibration_Spectra"
```

### 5.2 Hard-coded path references to update after `git mv`

Exhaustive grep across the repo for the three old folder names returned only **3 references** (plus an additional reference inside Vol_4 QUALITY_GATE.md). All are listed here:

| File | Line | Current text fragment | Fix |
|---|---:|---|---|
| `01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/audio book/chapter_titles_Vol2.json` | 31 | `...\Vol_2_Forces_and_Fields\Ch_03_Electromagnetism_from_Membrane_Wave_Propagation\Ch03_DRAFT.md` | replace `Membrane` → `Firmament` in path; **note**: this path is missing the `Manuscript\` segment (stale absolute path; preserve the bug or fix as a side correction — recommend fixing since this is the audiobook source map) |
| `01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/audio book/chapter_titles_Vol4.json` | 87 | `...\Vol_4_The_Quantum_World\Ch_10_Leptons_and_Quarks_from_Membrane_Resonances\Ch10_FINAL.md` | replace `Membrane` → `Firmament` (same `Manuscript\` segment issue) |
| `01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/QUALITY_GATE.md` | 112 | `**Files:** \`Manuscript/Ch_10_Leptons_and_Quarks_from_Membrane_Resonances/\` — Ch10_SPEC.md, Ch10_OUTLINE.md, …` | replace `Membrane_Resonances` → `Firmament_Resonances` |
| `01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/audio book/chapter_titles_Vol6.json` | 70 | `...\Vol_6_Predictions_and_Simulations\Ch_07_Membrane_Vibration_Spectra\Ch07_DRAFT.md` | replace `Membrane_Vibration_Spectra` → `Firmament_Vibration_Spectra` |

That is the complete cascade. (Search: `grep -rnF "Ch_03_Electromagnetism_from_Membrane_Wave_Propagation" --include='*' 01_Genesis_Physics/` returned only the above; same for the other two folder strings.)

---

## 6 — Phase 5: Vol 1 §1.5 vault fix + Vol 2 Ch 3 inline title fix

### 6.1 Vol 1 "vault" — clarification of §-numbering

The task brief said "§1.5 vault fix." Vol 1 Ch 1 §1.5 is "Axiom 4 — Humanity as Zone Interface Operator" (line 424-495 of `Ch01_DRAFT.md`); it contains **no** standalone "vault." The only standalone-vault hit in Vol 1 Ch 1 is at **line 580**, which is inside §1.7 (Axiom 6 — Duality as Creation Method).

| File | Line | Current | After |
|---|---:|---|---|
| `Vol_1_Architecture_of_Reality/Manuscript/Ch_01_Axioms_and_Definitions/Ch01_DRAFT.md` | 580 | `In the Genesis narrative: "Let there be a vault between the waters to separate water from water" (Genesis 1:6). Two waters, separated by the vault (raqia, the Firmament). Life emerges precisely where the two waters interact, mediated by the Firmament.` | First-sentence "vault" is inside a **direct biblical quote** → preserve. Second-sentence "Two waters, separated by the vault (raqia, the Firmament)." → **Replace `vault` with `Firmament`** (style-sheet violation; this is author prose, not quote). Suggested: `Two waters, separated by the Firmament (raqia). Life emerges precisely where the two waters interact, mediated by the Firmament.` |
| `Vol_1_Architecture_of_Reality/audio book/chapters/Ch01_clean.txt` | 552 | (same content, no quote marker in TTS extract) | Both "vault" instances → `Firmament` here; TTS chunk has no quote markup to preserve. |

**Also flagged in scope but not in task brief** (executor should confirm with Jeff before touching — see Phase 9):

| File | Line | Issue |
|---|---:|---|
| `Vol_1_Architecture_of_Reality/Manuscript/Ch_04_The_6D_Embedding_Space/Ch04_DRAFT.md` | 476 | Blockquote of Gen 1:6-8 with "vault" (4× in the quote). Quote — preserve. |
| `Vol_1_Architecture_of_Reality/Manuscript/Ch_04_The_6D_Embedding_Space/Ch04_DRAFT.md` | 480 | Bullet list item: `- **Vault / Firmament** (the observable boundary)` — author prose, style-sheet violation. Recommend: `- **The Firmament** (the observable boundary; Hebrew *raqia*)`. |
| `Vol_1_Architecture_of_Reality/audio book/chapters/Ch04_clean.txt` | 469 | Same as above (TTS form). |
| `Vol_1_Architecture_of_Reality/Manuscript/AppC_Hebrew_Analysis_DRAFT.md` | 318 | `Semantic Range: An expanse, a stretched-out sheet or vault, the sky (as something beaten/stretched over the earth).` — this is Hebrew-meaning discussion. Preserve "vault, the sky" as lexical content. |
| `Vol_1_Architecture_of_Reality/audio book/chapters/AppC_Hebrew_Analysis_DRAFT_clean.txt` | 279 | Same — preserve. |
| `Vol_1_Architecture_of_Reality/audio book/chapters/AppC_Hebre_clean.txt` | 279 | Same — preserve (duplicate TTS chunk). |

### 6.2 Vol 2 Ch 3 inline title fixes

After the `git mv` in Phase 4, the following **inline title strings** inside the renamed folder must also change `Membrane` → `Firmament`:

| File (post-rename path) | Line | Current | After |
|---|---:|---|---|
| `Vol_2_Forces_and_Fields/Manuscript/Ch_03_Electromagnetism_from_Firmament_Wave_Propagation/CHAPTER_SPEC.md` | 1 | `# Chapter Spec — Electromagnetism from Membrane Wave Propagation` | `# Chapter Spec — Electromagnetism from Firmament Wave Propagation` |
| same | 5 | `**Working Title:** Electromagnetism from Membrane Wave Propagation` | `**Working Title:** Electromagnetism from Firmament Wave Propagation` |
| `…/Ch_03_…/Ch03_DRAFT.md` | 1 | `# Chapter 3: Electromagnetism from Membrane Wave Propagation` | `# Chapter 3: Electromagnetism from Firmament Wave Propagation` |
| `…/Ch_03_…/REVIEWER_REPORT.md` | 1 | `# Reviewer Report — Chapter 3: Electromagnetism from Membrane Wave Propagation` | `# Reviewer Report — Chapter 3: Electromagnetism from Firmament Wave Propagation` |
| `…/Ch_03_…/SELF_REVIEW_REPORT.md` | 1 | `# Self-Review Report — Chapter 3: Electromagnetism from Membrane Wave Propagation` | `# Self-Review Report — Chapter 3: Electromagnetism from Firmament Wave Propagation` |

**Analogous inline-title fixes** in the other two renamed chapters:

| File | Line | Fix |
|---|---:|---|
| `Vol_4_The_Quantum_World/Manuscript/Ch_10_Leptons_and_Quarks_from_Firmament_Resonances/Ch10_DRAFT.md` | 1 | `# Chapter 10: …Membrane Resonances` → `…Firmament Resonances` |
| same `Ch10_FINAL.md` | 1 | same |
| same `Ch10_SPEC.md` / `CHAPTER_SPEC.md` | 1 (working title) | same |
| `Vol_6_Predictions_and_Simulations/Manuscript/Ch_07_Firmament_Vibration_Spectra/Ch07_DRAFT.md` | 1 | `# Chapter 7: Membrane Vibration Spectra` → `# Chapter 7: Firmament Vibration Spectra` |
| same `CHAPTER_SPEC.md` | 1 & working-title line | same |
| same `Ch07_OUTLINE.md` | 1 | same |

The executor should grep each renamed folder for `Membrane (Wave Propagation|Resonances|Vibration Spectra)` to catch any straggler title references inside those folders, and apply the same fix.

**TOC / Master_Index references:**

| File | Search for | Replace |
|---|---|---|
| `Vol_6/Back_Matter/Master_Index.md` | `Membrane Vibration Spectra` | `Firmament Vibration Spectra` |
| Any Vol-level README / Manuscript index | `Electromagnetism from Membrane Wave Propagation` | `Electromagnetism from Firmament Wave Propagation` |
| Any Vol-level README / Manuscript index | `Leptons and Quarks from Membrane Resonances` | `Leptons and Quarks from Firmament Resonances` |

(Note: `Vol_6/Back_Matter/Master_Index.md` had 13 compound-modifier hits in the Phase 2 grep, so it almost certainly references the Ch_07 title — executor should verify.)

---

## 7 — Phase 6: Reference doc updates

### 7.1 `Glossary.md`

| Line | Current | After |
|---:|---|---|
| 18 | `**Firmament (Raqia, רָקִיעַ)**: From Hebrew root meaning "to beat out, stretch." The membrane created on Day 2 separating Waters Above from Waters Below. Corresponds to our observable universe (Zone 2.2.2).` | `**The Firmament (Raqia, רָקִיעַ)**: From Hebrew root meaning "to beat out, stretch." The Firmament membrane created on Day 2 separating Waters Above from Waters Below. Corresponds to our observable universe (Zone 2.2.2). Also called the **Firmament Domain** (Zone 2.2 = Z₂.₂) when referring to the full domain that includes the Firmament membrane and the layer immediately surrounding it.` |
| 48 | `**Chladni Patterns**: Vibrational modes creating nodal boundaries; membrane-oscillation model for zone creation.` | `**Chladni Patterns**: Vibrational modes creating nodal boundaries; Firmament-membrane-oscillation model for zone creation.` |
| 104 | `**Earth Prime (Zone 2)**: Primary material cosmos; temporal, accessible to observation; divided into Waters Above, Firmament, Waters Below.` | (unchanged — already canonical) |
| 106 | `**Firmament (Zone 2.2.2)**: Membrane separating Waters Above from Waters Below; our observable universe including dark and baryonic matter.` | `**The Firmament (Zone 2.2.2)**: The Firmament membrane separating Waters Above from Waters Below; our observable universe including dark and baryonic matter. The enclosing Zone 2.2 is the **Firmament Domain**.` |

**Add new glossary entry** (alphabetical position, after "Firmament"):

```
**Firmament Domain (Zone 2.2 / Z₂.₂)**: The full domain comprising the Firmament membrane (Z₂.₂.₂) and its immediate enclosing structure. Distinct from "The Firmament" (the membrane proper, Z₂.₂.₂). The two-word phrase "Firmament Domain" is the only acceptable name for Z₂.₂.
```

### 7.2 `Symbol_and_Constants.md`

| Line | Current | After |
|---:|---|---|
| 16 | `\| **σ** \| 6.0×10⁹⁸ \| kg/(m·s²) \| [ML⁻¹T⁻²] \| Membrane 3-brane tension; fundamental creation parameter \|` | `\| **σ** \| 6.0×10⁹⁸ \| kg/(m·s²) \| [ML⁻¹T⁻²] \| Firmament membrane 3-surface tension; fundamental creation parameter \|` |
| 25 | `\| **c** \| 2.998×10⁸ \| m/s \| √(σ/μ) \| Speed of light; membrane wave speed \|` | `\| **c** \| 2.998×10⁸ \| m/s \| √(σ/μ) \| Speed of light; Firmament wave speed \|` |

(Note: per Phase 3, "3-brane" → "3-surface" in this gloss because "3-brane" is a string-theory loanword that conflicts with the Firmament-terminology canon. Alternative: keep "3-brane" inside backticks as a literal external term and add "(in string-theory nomenclature)". Executor should pick one; recommend the "3-surface" rewrite for self-consistency.)

### 7.3 `Equation_Registry.md`

| Line | Change |
|---:|---|
| 33 | `…encodes membrane bending energy` → `…encodes Firmament membrane bending energy` |

**Append to the registry** (after the existing Vol 2 Ch 5 entries) two new explanatory rows:

```
| (2.5.1) | Total Zone Action — Seven Sectors | Volume 2 | 2 | 5 | S_total = S_grav + S_Firm + S_waters + S_gauge + S_matter + S_int + S_sustain. Note: the Firmament-sector subscript is renamed from S_brane → S_Firm in 0516_Rev_002. |
| (2.5.4) | Nambu-Goto + Helfrich Firmament Action | Volume 2 | 2 | 5 | S_Firm = -σ∫dᵃσ √-γ + (κ_B/2)∫dᵃσ √-γ H². Renamed from S_brane in 0516_Rev_002. |
```

(Adjust row placement to match the registry's existing chronological ordering.)

### 7.4 `Zone_Architecture.md`

| Line | Current | After |
|---:|---|---|
| 18 | `\| Z₂.₂ \| Firmament Domain \| Day 2 \| Temporal \| Observable \| 3D + time \| Membrane; observable universe \|` | `\| Z₂.₂ \| Firmament Domain \| Day 2 \| Temporal \| Observable \| 3D + time \| Firmament membrane; observable universe \|` |
| 128 | `- Z₂.₂ = Firmament Domain (observable universe membrane)` | `- Z₂.₂ = Firmament Domain (the Firmament membrane and surrounding structure; observable universe)` |

(All "Firmament Domain" instances are already canonical two-word; no rename needed — confirms policy decision 3.)

### 7.5 `Quality_Control/Reviewers/REVIEWER_08_The_Style_Editor.md`

| Line | Current | After |
|---:|---|---|
| 42 | `4. **Firmament terminology:** Primary term is "The Firmament." Acceptable: "The Firmament membrane" in technical contexts. NEVER: "dome," "vault," "sky," "brane," "the membrane" alone, "the expanse" alone.` | `4. **Firmament terminology:** Primary term is "The Firmament." Acceptable: "The Firmament membrane" in technical contexts; **"Firmament Domain" (two words, capitalized) for the full Zone 2.2 region** (distinct from the Firmament membrane Z₂.₂.₂). NEVER: "dome," "vault," "sky," "brane," "the membrane" alone, "the expanse" alone.` |
| 65 | `- "The membrane" used alone without "Firmament" qualification` | (unchanged) |

**Optional addition** to the "Tools & Resources" list (line ~72): cross-reference the new `Firmament Domain` glossary entry.

---

## 8 — Phase 7: Validator grep guards

Run **after** Phases 1-6. Each command must produce **zero output** for the commit to be considered clean (excepting documented allowlists).

```bash
export LC_ALL=C.UTF-8
EXCL='(/00_Archive/|_pre-comprehensive|0516_Rev_.*_TASKS\.md|BOOK_SERIES_MASTER_REVIEW_)'
ROOTS=(
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_1_Architecture_of_Reality/Manuscript"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_1_Architecture_of_Reality/audio book"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/Manuscript"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/audio book"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_2_Forces_and_Fields/Back_Matter"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_3_Matter_and_Motion/Manuscript"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_3_Matter_and_Motion/audio book"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_3_Matter_and_Motion/Back_Matter"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Manuscript"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/audio book"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Back_Matter"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/Manuscript"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/audio book"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_5_The_Cosmos/Back_Matter"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Manuscript"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/audio book"
  "01_Genesis_Physics/Book_0_The_Foundations/Vol_6_Predictions_and_Simulations/Back_Matter"
  "01_Genesis_Physics/Quality_Control/Reference"
  "01_Genesis_Physics/Research/Foundations"
  "01_Genesis_Physics/Research/Mathematical_Models"
  "01_Genesis_Physics/Research/Simulations"
)
```

### Guard 1 — no standalone `\bbrane\b` outside RS / code blocks / Phase 3 subscripts
```bash
for r in "${ROOTS[@]}"; do
  grep -rnE --include='*.md' --include='*.tex' --include='*.py' --include='*.txt' \
    -e '\bbrane\b' "$r" 2>/dev/null
done | grep -vE "$EXCL" \
  | grep -vE '[Rr]andall[- ]?[Ss]undrum|braneworld|brane-world|brane world|RS model|D-?brane|p-?brane' \
  | grep -vE '_brane\b|\{brane\}|brane\}'    # subscripts handled in Phase 3 (should now be 0)
```
**Expected:** zero lines.

### Guard 2 — no standalone `\b[Tt]he membrane\b`
```bash
for r in "${ROOTS[@]}"; do
  grep -rnE --include='*.md' --include='*.tex' --include='*.py' --include='*.txt' \
    -e '\b[Tt]he membrane\b' "$r" 2>/dev/null
done | grep -vE "$EXCL"
```
**Expected:** zero lines, OR only lines where "the membrane" is immediately followed by one of the technical-context modifiers AND the preceding word is `Firmament` (i.e. "the Firmament membrane" pattern — but that pattern won't match `\bthe membrane\b` since "Firmament" intervenes). Net expected: zero.

### Guard 3 — no compound modifier without `Firmament` qualifier
```bash
for r in "${ROOTS[@]}"; do
  grep -rnE --include='*.md' --include='*.tex' --include='*.py' --include='*.txt' \
    -e '\bmembrane (tension|wave|oscillation|resonance|stiffness|fluctuation|rigidity|mode|vibration|excitation)' "$r" 2>/dev/null
done | grep -vE "$EXCL" \
  | grep -vE 'Firmament membrane (tension|wave|oscillation|resonance|stiffness|fluctuation|rigidity|mode|vibration|excitation)'
```
**Expected:** zero lines.

### Guard 4 — no leftover `\text{brane}` / `\mathrm{brane}` / `{brane}` / `_brane`
```bash
for r in "${ROOTS[@]}"; do
  grep -rnE --include='*.md' --include='*.tex' --include='*.py' --include='*.txt' \
    -e '\\text\{brane\}|\\mathrm\{brane\}|\{brane\}|[A-Za-z]_brane\b|\{\\rm brane\}' "$r" 2>/dev/null
done | grep -vE "$EXCL"
```
**Expected:** zero lines.

### Guard 5 — folder rename completeness (no remaining old folder strings)
```bash
grep -rnF -e 'Ch_03_Electromagnetism_from_Membrane_Wave_Propagation' \
          -e 'Ch_10_Leptons_and_Quarks_from_Membrane_Resonances' \
          -e 'Ch_07_Membrane_Vibration_Spectra' \
          --include='*.md' --include='*.tex' --include='*.py' --include='*.txt' \
          --include='*.json' --include='*.yaml' --include='*.yml' --include='*.csv' \
          01_Genesis_Physics/ 2>/dev/null | grep -vE '/00_Archive/'
```
**Expected:** zero lines.

### Guard 6 — `vault` standalone in author prose (not in quotes / Hebrew analysis)
Use the manual list from Phase 5 §6.1 as the allowlist. Any other hit is a fail.
```bash
for r in "${ROOTS[@]}"; do
  grep -rnEi --include='*.md' --include='*.txt' -e '\bvault\b' "$r" 2>/dev/null
done | grep -vE "$EXCL" \
  | grep -vE '(raqia|"vault"|Genesis 1:6|Semantic Range|Hebrew|terminology table|RESOLVED_Zone)'
```
**Expected:** zero lines (after the explicit Phase 5 edits land).

### Guard 7 — `Firmament Domain` is two-word & capitalized when used
```bash
for r in "${ROOTS[@]}"; do
  grep -rniE --include='*.md' --include='*.txt' -e 'firmament[- ]?domain' "$r" 2>/dev/null
done | grep -vE "$EXCL" | grep -vE 'Firmament Domain'
```
**Expected:** zero lines.

---

## 9 — Risk flags and scope questions (executor must read before starting)

### R1 — `*_REVIEWS.md` / `REVIEWER_REPORT.md` / `SELF_REVIEW_REPORT.md` inside chapter folders
Scope-exclude rule `/REVIEWER_` excludes only the **persona files at `Quality_Control/Reviewers/REVIEWER_NN_*.md`** (matches `/REVIEWER_` as a path fragment). It does **not** exclude per-chapter review reports such as `Vol_6/Manuscript/Ch_07_Membrane_Vibration_Spectra/Ch07_REVIEWS.md` (no leading slash on `REVIEWER_`/`REVIEWS`). Those files contain hundreds of standalone-`brane` / `the membrane` quotations that may be **citations from the as-of-then text** that we should not rewrite (rewriting them silently invalidates historical QA evidence). **Question for Jeff:** apply Phases 1-3 inside `*_REVIEWS.md` / `*_REVIEWER_REPORT.md` / `*_SELF_REVIEW_REPORT.md` files? Recommendation: **NO** — only apply Phase 5 (folder rename / inline-title fix) and Phase 6 reference doc updates. Add an explicit exclude `--exclude='*_REVIEWS.md' --exclude='*REVIEWER_REPORT.md' --exclude='*SELF_REVIEW_REPORT.md'` to all Phase 1-3 passes.

### R2 — `*_clean.txt` audiobook chunks
The `audio book/chapters/*_clean.txt` files are **derived from Manuscript drafts** by `preprocess_book0.py`. Editing them by hand will get clobbered the next time TTS preprocessing runs. **Question for Jeff:** treat audiobook txt chunks as derivative (regenerate from Manuscript after Phases 1-3 run, do not hand-edit), or hand-edit them this commit? Recommendation: **regenerate** — easier to verify, cheaper to redo.

### R3 — `Ch01_DRAFT.md:580` is in §1.7, not §1.5
The task brief says "Vol 1 §1.5 vault fix." The only standalone-vault hit in Vol 1 Ch 1 is line 580, **§1.7 (Axiom 6 — Duality as Creation Method)**. No vault in §1.5 (Axiom 4). The Phase 5 plan applies the fix to line 580 as the apparent intent.

### R4 — Genesis 1:6-8 blockquote at Vol1 Ch4 line 476
Contains "vault" 4× inside a direct biblical quote. Style sheet forbids "vault" — but biblical quotes are historically preserved verbatim across the manuscript. Phase 5 preserves the quote and fixes only line 480 (the bullet `**Vault / Firmament**`). **Confirmation:** preserve biblical quotes verbatim regardless of style-sheet vocabulary rules.

### R5 — `Symbol_and_Constants.md` line 16 "3-brane tension"
The current gloss calls σ a "Membrane 3-brane tension." The "3-brane" is a literal string-theory term (the Firmament is geometrically a 3+1-dimensional submanifold of 6D, technically a 3-brane in the codimension-2 sense). Phase 6 §7.2 rewrites to "Firmament membrane 3-surface tension" but this **changes the technical vocabulary** in a way that may confuse readers who came from a string-theory background. Alternative: keep "3-brane" but qualify ("3-brane in string-theory geometric nomenclature, equivalently the Firmament membrane"). Recommend Jeff pick.

### R6 — Vol 1 Ch 1 line 96 inside a parameter table
`\| $c$ \| $2.998 \times 10^8$ m/s \| Derived: $c = \sqrt{\sigma/\mu}$ (membrane wave speed) \|` — this is a one-line gloss inside a numbered axiom-explanation table. The bare "membrane" is acceptable per Phase 2 mechanics-context rule (`Firmament membrane wave speed`). Flagged for executor: short-context cases like this in tables. There are ~50 such table-cell hits.

### R7 — Vol 4 Ch 13 Ch13_SPEC.md line 51 (`structural fact …on the membrane`)
Ambiguous: "the three generations are a structural consequence of the three-level bound-state problem on the membrane." Default rule: `the membrane → the Firmament`. Mechanics context? Bound-state problem **is** mechanics-flavored but the noun phrase here is positional ("on the membrane" = "on the Firmament"), not dynamical. Recommend `the Firmament`. Flagged because the executor will see many similar borderline cases.

### R8 — `derive_l_eff.py` and other `.py` files in `Research/Mathematical_Models/`
44 hits in `derive_l_eff.py` alone. Many are in Python **string literals** that get printed as derivation output, plus comments. The same Phase 1-3 rules apply, but the executor must not break Python syntax (no edits inside `# noqa: codename` lines or inside docstrings if those are imported). Recommend: process Python files exactly as Markdown — every `brane` token in a string literal or comment gets rewritten. Sanity-check with a `python -c "import ast; ast.parse(open('…').read())"` pass.

### R9 — Vol 5 Ch 5 `Ch05_DRAFT.md` line 484 ("the membrane framework")
`In the membrane framework, the breach boundary is a reflecting/leaky edge, and perturbations of the membrane near r ≳ r_+ can produce "echoes"…` — first `the membrane` is **a methodological/framework name**, second is mechanics. Default rule rewrites both. After: `In the Firmament framework, the breach boundary is a reflecting/leaky edge, and perturbations of the Firmament membrane near r ≳ r_+ can produce "echoes"…` (second instance bumps to "Firmament membrane" because mechanics context). Flagged because there are ~30 occurrences of "the membrane framework" / "the membrane interpretation" / "the membrane picture" across Vol 4 and Vol 5 where rewriting to `the Firmament framework` is **semantically right** but reads odd at first glance to a reader familiar with the old terminology. Recommend Jeff approve a one-time skim of the post-edit Vol 5 Ch 5-7 prose.

### R10 — Ten representative ambiguous excerpts for hand review

```
1. Vol_5/Manuscript/Ch_05_Black_Holes_as_Zone_Infrastructure/Ch05_DRAFT.md:484
   "In the membrane framework, the breach boundary is a reflecting/leaky edge…"
   → "In the Firmament framework, the breach boundary is a reflecting/leaky edge…"

2. Vol_4/Manuscript/Ch_13_The_CKM_and_PMNS_Matrices/Ch13_SPEC.md:51
   "…three-level bound-state problem on the membrane."
   → "…three-level bound-state problem on the Firmament."

3. Vol_6/Manuscript/Ch_10_Energy_Harvesting/Ch10_FINAL.md:224
   "The OHCs continuously inject energy into the membrane; the IHCs continuously harvest energy from it…"
   → DO NOT REWRITE — this is **cochlear-physiology context** (Organ of Corti hair cells). "membrane" here = basilar/tectorial membrane. Verify scope of biological-membrane allowlist.

4. Vol_4/Manuscript/Ch_09_The_Casimir_Effect_and_Vacuum_Energy/Ch09_REVIEWER_NOTES.md:95
   "Why is the membrane cutoff more physical than just ignoring the divergence?"
   → REVIEWER_NOTES is excluded by R1 recommendation.

5. Vol_4/Manuscript/Ch_14_Beyond_the_Standard_Model/Ch14_DRAFT.md:375
   "…from the boundary conditions on the Ψ_A and Ψ_B fields at the membrane;"
   → "…at the Firmament;" (locational, not mechanics)

6. Vol_4/Manuscript/Ch_08_Renormalization_in_Zone_Architecture/Ch08_DRAFT.md:648
   "Above the membrane scale, there are no more modes…"
   → "Above the Firmament scale, there are no more modes…"

7. Vol_6/Manuscript/Ch_14_Open_Problems/Ch14_DRAFT.md:516
   "…derive the Schwinger formula entirely from membrane physics … derive the membrane interpretation that makes the Schwinger formula…"
   → "…from Firmament physics … derive the Firmament-physics interpretation…"
   (The second "the membrane" is part of an interpretive-framework noun phrase; rewrite cleanly.)

8. Vol_4/Manuscript/Ch_10_Leptons_and_Quarks_from_Firmament_Resonances/Ch10_DRAFT.md:637  (post-rename path)
   "The framework currently requires an independent primordial spinor field on the membrane…"
   → "…on the Firmament…"

9. Vol_5/Manuscript/Ch_05_Black_Holes_as_Zone_Infrastructure/Ch05_DRAFT.md:602
   "P5.6. Why no firewall? Explain why the membrane interpretation of the horizon predicts no firewall …
    (iii) the absence of a discontinuity in the membrane degrees of freedom at the breach boundary."
   → "…the Firmament-membrane interpretation of the horizon …
      (iii) the absence of a discontinuity in the Firmament membrane degrees of freedom at the breach boundary."
   (mechanics context throughout — bump to "Firmament membrane")

10. Vol_6/Manuscript/Ch_07_Firmament_Vibration_Spectra/Ch07_DRAFT.md:51  (post-rename path)
    "This is the membrane eigenvalue problem."
    → "This is the Firmament membrane eigenvalue problem." (clear mechanics context)
```

### R11 — Python test files: `derive_l_eff.py`, `test_derivation_chains.py`, `derive_alpha_coefficient.py`, `test_thermodynamic_laws.py`
~100 hits in these four files. Need a separate audit pass: verify the test assertions don't compare against the literal string "brane" anywhere. Run pytest on each test file post-edit. Recommend the executor add this to the CI gate before merge.

### R12 — No standalone-vault hits found in §1.5 author prose
The task brief specified "§1.5 vault fix." After exhaustive grep, no standalone `vault` exists in §1.5 of Vol 1 Ch 1. The closest hit is §1.7 line 580 (handled in Phase 5 §6.1) and §4.2 line 480 (bullet "Vault / Firmament" — handled). Confirming with Jeff this is what was meant.

---

## Appendix A — Top-50 files for each pass (cut-and-paste from grep)

### A.1 Top 50 files by standalone `\bbrane\b` count (non-RS)
```
113 Vol_6/Manuscript/Ch_09_FTL_Travel/Ch09_DRAFT.md
109 Vol_5/Manuscript/Ch_07_Singularity_Resolution/Ch07_DRAFT.md
101 Vol_5/audio book/chapters/Ch07_clean.txt
 94 Vol_6/audio book/chapters/Ch09_clean.txt
 70 Vol_5/Manuscript/Ch_06_The_Information_Paradox_Resolved/Ch06_DRAFT.md
 65 Vol_6/Manuscript/Ch_09_FTL_Travel/Ch09_DRAFT_Part1.md
 65 Vol_5/Manuscript/Ch_11_Dark_Matter_and_Dark_Energy_Quantified/Ch11_DRAFT.md
 62 Vol_5/audio book/chapters/Ch06_clean.txt
 62 Vol_5/Manuscript/Ch_08_Zone_Cosmological_Model/Ch08_DRAFT.md
 59 Vol_5/audio book/chapters/Ch11_clean.txt
 57 Vol_5/audio book/chapters/Ch08_clean.txt
 56 Vol_6/Back_Matter/APPENDIX_D_Selected_Solutions.md
 54 Vol_6/audio book/chapters/APPENDIX_D_clean.txt
 54 Vol_6/audio book/chapters/APPENDIX_D_Selected_Solutions_clean.txt
 45 Research/Foundations/ACTION_6D_COMPLETE.md
 43 Research/Mathematical_Models/10_Derivation_Chain/derive_l_eff.py
 43 Vol_6/Manuscript/Ch_15_Connections_to_Other_Programs/Ch15_DRAFT.md
 42 Research/Foundations/6D_TO_4D_PROJECTION.md
 41 Vol_6/audio book/chapters/Ch15_clean.txt
 39 Vol_6/Manuscript/Ch_13_Consciousness_and_the_Zone_Interface/Ch13_DRAFT.md
 39 Vol_6/Manuscript/Ch_11_FTL_Communication/Ch11_DRAFT.md
 35 Vol_6/audio book/chapters/Ch13_clean.txt
 34 Vol_6/audio book/chapters/Ch11_clean.txt
 34 Vol_5/Manuscript/Ch_05_Black_Holes_as_Zone_Infrastructure/Ch05_DRAFT.md
 33 Research/Foundations/WARP_FUNCTION_DERIVATION_RT1WF.md
 31 Vol_5/audio book/chapters/Ch05_clean.txt
 31 Vol_5/Manuscript/Ch_06_The_Information_Paradox_Resolved/CHAPTER_OUTLINE.md
 30 Research/Foundations/METRIC_6D_SOLUTIONS.md
 29 Vol_5/audio book/chapters/Ch10_clean.txt
 29 Vol_5/Manuscript/Ch_10_Large_Scale_Structure/Ch10_DRAFT.md
 29 Vol_2/Manuscript/Ch_05_The_Zone_Lagrangian/Ch05_DRAFT.md
 27 Vol_5/Manuscript/Ch_09_The_CMB_and_Early_Universe/Ch09_DRAFT.md
 27 Vol_5/Manuscript/Ch_08_Zone_Cosmological_Model/CHAPTER_OUTLINE.md
 27 Vol_1/Manuscript/Ch_04_The_6D_Embedding_Space/Ch04_DRAFT.md
 26 Vol_6/Manuscript/Ch_09_FTL_Travel/Ch09_DRAFT_Part2.md
 26 Vol_5/audio book/chapters/Ch09_clean.txt
 25 Vol_5/Manuscript/Ch_07_Singularity_Resolution/CHAPTER_SPEC.md
 23 Research/Mathematical_Models/10_Derivation_Chain/test_derivation_chains.py
 23 Vol_5/Manuscript/Ch_13_Fine_Structure_Constant_from_First_Principles/Ch13_DRAFT.md
 23 Vol_5/Manuscript/Ch_11_Dark_Matter_and_Dark_Energy_Quantified/CHAPTER_SPEC.md
 23 Vol_5/Manuscript/Ch_07_Singularity_Resolution/CHAPTER_OUTLINE.md
 23 Vol_2/audio book/chapters/Ch05_clean.txt
 22 Vol_6/Manuscript/Ch_09_FTL_Travel/Ch09_DRAFT_Part3.md
 22 Vol_5/Manuscript/Ch_04_Strong_Field_Gravity/Ch04_DRAFT.md
 22 Vol_1/audio book/chapters/Ch04_clean.txt
 22 Vol_1/Manuscript/Ch_05_The_Firmament_Manifold/Ch05_DRAFT.md
 21 Research/Mathematical_Models/10_Derivation_Chain/derive_alpha_coefficient.py
 21 Vol_5/audio book/chapters/Ch13_clean.txt
 21 Vol_5/audio book/chapters/Ch04_clean.txt
 21 Vol_5/Manuscript/Ch_08_Zone_Cosmological_Model/CHAPTER_SPEC.md
```
(Full 317-file list: regenerable by re-running the Guard 1 inverse — `grep -rcE '\bbrane\b' …`).

### A.2 Top 50 files by `\b[Tt]he membrane\b` count
```
46 Vol_5/Manuscript/Ch_05_Black_Holes_as_Zone_Infrastructure/Ch05_DRAFT.md
42 Vol_5/audio book/chapters/Ch05_clean.txt
41 Vol_1/audio book/chapters/Ch05_clean.txt
41 Vol_1/Manuscript/Ch_05_The_Firmament_Manifold/Ch05_DRAFT.md
34 Vol_6/audio book/chapters/Ch07_clean.txt
34 Vol_6/Manuscript/Ch_07_Membrane_Vibration_Spectra/Ch07_DRAFT.md     ← rename per Phase 4
32 Vol_1/Manuscript/Ch_10_Quantization_from_Boundary_Conditions/Ch10_DRAFT.md
31 Vol_1/audio book/chapters/Ch10_clean.txt
30 Vol_5/Manuscript/Ch_07_Singularity_Resolution/Ch07_DRAFT.md
28 Vol_5/audio book/chapters/Ch07_clean.txt
27 Research/Mathematical_Models/10_Fundamental_Constants/10-RESOLVED_MEMBRANE_TENSION.md
27 Research/Mathematical_Models/10_Fundamental_Constants/10-FUNDAMENTAL_CONSTANTS_OVERVIEW.md
27 Research/Foundations/MEMBRANE_MASS_SCALE.md
27 Vol_4/Manuscript/Ch_08_Renormalization_in_Zone_Architecture/Ch08_DRAFT.md
25 Vol_4/audio book/chapters/Ch08_clean.txt
25 Vol_4/Manuscript/Ch_08_Renormalization_in_Zone_Architecture/Ch08_FINAL.md
24 Research/Mathematical_Models/05_Quantum_Mechanics/05-QED_LOOPS_DERIVATION.md
22 Research/Mathematical_Models/08_Cosmology/08-ENERGY_EXTRACTION_CREATION.md
22 Research/Foundations/AXIOM_MEMBRANE_MECHANICS_v2.md
22 Vol_4/audio book/chapters/Ch10_clean.txt
22 Vol_4/Manuscript/Ch_10_Leptons_and_Quarks_from_Membrane_Resonances/Ch10_FINAL.md  ← rename
21 Vol_4/Manuscript/Ch_10_Leptons_and_Quarks_from_Membrane_Resonances/Ch10_DRAFT.md  ← rename
18 Research/Mathematical_Models/01_Classical_Mechanics/01-NBODY_DYNAMICS.md
18 Vol_6/Manuscript/Ch_12_Advanced_Sensors/Ch12_DRAFT.md
17 Research/Foundations/AXIOM_MEMBRANE_MECHANICS.md
16 Vol_6/audio book/chapters/Ch14_clean.txt
16 Vol_6/audio book/chapters/Ch12_clean.txt
16 Vol_6/audio book/chapters/Ch10_clean.txt
16 Vol_6/Manuscript/Ch_14_Open_Problems/Ch14_DRAFT.md
15 Vol_6/Manuscript/Ch_10_Energy_Harvesting/Ch10_FINAL.md
15 Vol_6/Manuscript/Ch_10_Energy_Harvesting/Ch10_DRAFT.md
14 Research/Mathematical_Models/05_Quantum_Mechanics/05-QED_PRECISION_CALCULATIONS.md
13 Vol_6/audio book/chapters/Ch05_clean.txt
13 Vol_6/audio book/chapters/Ch03_clean.txt
13 Vol_6/Manuscript/Ch_05_Simulation_Methodology/Ch05_DRAFT.md
13 Vol_6/Manuscript/Ch_03_Novel_Predictions/Ch03_DRAFT.md
13 Vol_5/audio book/chapters/Ch15_clean.txt
13 Vol_5/Manuscript/Ch15_Why_These_Constants/Ch15_Why_These_Constants_DRAFT.md
13 Vol_4/audio book/chapters/Ch02_clean.txt
13 Vol_4/audio book/chapters/Ch01_clean.txt
13 Vol_4/Manuscript/Ch_02_The_Schrodinger_Equation_Derived/Ch02_DRAFT.md
13 Vol_4/Manuscript/Ch_01_Why_the_Universe_is_Quantum/Ch01_DRAFT.md
12 Research/Mathematical_Models/10_Fundamental_Constants/10-CONSTANTS_FROM_6D.md
12 Research/Mathematical_Models/09_Chemistry_and_Materials/09-ELEMENT_PREDICTION.md
12 Research/Mathematical_Models/05_Quantum_Mechanics/05-QM_FROM_MEMBRANE_DYNAMICS.md
12 Vol_4/Manuscript/Ch_01_Why_the_Universe_is_Quantum/Ch01_VERIFIED.md
11 Research/Mathematical_Models/06_Nuclear_and_Particle_Physics/06-MASS_SPECTRUM_V2_HIERARCHY.md
11 Vol_5/Manuscript/Ch_06_The_Information_Paradox_Resolved/Ch06_DRAFT.md
11 Vol_3/audio book/chapters/Ch07_clean.txt
```

### A.3 Top 50 files by compound-modifier count (`membrane {tension|wave|…}`)
```
35 Vol_1/Manuscript/Ch_10_Quantization_from_Boundary_Conditions/Ch10_DRAFT.md
31 Vol_1/audio book/chapters/Ch10_clean.txt
28 Vol_6/Manuscript/Ch_07_Membrane_Vibration_Spectra/Ch07_DRAFT.md         ← rename
24 Vol_6/audio book/chapters/Ch07_clean.txt
18 Vol_6/Manuscript/Ch_03_Novel_Predictions/Ch03_DRAFT.md
17 Research/Mathematical_Models/02_Thermodynamics/test_thermodynamic_laws.py
17 Vol_6/Manuscript/Ch_07_Membrane_Vibration_Spectra/Ch07_REVIEWS.md       ← flagged R1
17 Vol_1/Manuscript/Ch_10_Quantization_from_Boundary_Conditions/CHAPTER_SPEC.md
16 Research/Mathematical_Models/10_Fundamental_Constants/10-FUNDAMENTAL_CONSTANTS_OVERVIEW.md
16 Research/Mathematical_Models/08_Cosmology/08-ENERGY_EXTRACTION_CREATION.md
16 Vol_6/audio book/chapters/Ch03_clean.txt
16 Vol_6/Manuscript/Ch_12_Advanced_Sensors/Ch12_DRAFT.md
16 Vol_1/Manuscript/Ch_11_Thermodynamics_from_Zone_Separation/Ch11_Thermodynamics_from_Zone_Separation.md
15 Vol_6/audio book/chapters/Ch12_clean.txt
15 Vol_6/Manuscript/Ch_15_Connections_to_Other_Programs/Ch15_DRAFT.md
15 Vol_3/Manuscript/Ch_07_The_Origin_of_Mass/Ch07_DRAFT.md
15 Vol_1/audio book/chapters/Ch11_clean.txt
15 Vol_1/Manuscript/Ch_05_The_Firmament_Manifold/Ch05_DRAFT.md
14 Vol_6/audio book/chapters/Ch15_clean.txt
14 Vol_6/audio book/chapters/Ch05_clean.txt
14 Vol_6/Manuscript/Ch_05_Simulation_Methodology/Ch05_DRAFT.md
14 Vol_1/audio book/chapters/Ch05_clean.txt
13 Research/Mathematical_Models/05_Quantum_Mechanics/05-QED_PRECISION_CALCULATIONS.md
13 Vol_6/Manuscript/Ch_07_Membrane_Vibration_Spectra/CHAPTER_SPEC.md       ← rename
13 Vol_6/Back_Matter/Master_Index.md
13 Vol_3/audio book/chapters/Ch07_clean.txt
12 Research/Mathematical_Models/05_Quantum_Mechanics/05-QM_FROM_MEMBRANE_DYNAMICS.md
12 Research/Foundations/AXIOM_MEMBRANE_MECHANICS_v2.md
12 Research/Foundations/AXIOM_MEMBRANE_MECHANICS.md
12 Vol_6/Manuscript/Ch_07_Membrane_Vibration_Spectra/Ch07_OUTLINE.md       ← rename
12 Vol_6/Manuscript/Ch_02_Predictions_That_Differ/Ch02_DRAFT.md
11 Vol_6/Manuscript/Ch_10_Energy_Harvesting/Ch10_DRAFT.md
10 Research/Mathematical_Models/05_Quantum_Mechanics/05-CONDENSED_MATTER_DERIVATION.md
10 Vol_6/audio book/chapters/Ch02_clean.txt
 9 Research/Mathematical_Models/10_Fundamental_Constants/10-RUNNING_COUPLINGS_RG_FLOW.md
 9 Research/Mathematical_Models/10_Fundamental_Constants/10-RESOLVED_MEMBRANE_TENSION.md
 9 Research/Mathematical_Models/02_Thermodynamics/02-LAWS_DERIVATION.md
 9 Vol_6/audio book/chapters/Ch10_clean.txt
 9 Vol_6/Manuscript/Ch_10_Energy_Harvesting/Ch10_FINAL.md
 8 Research/Mathematical_Models/09_Chemistry_and_Materials/09-CHEMISTRY_DERIVATION.md
 8 Research/Mathematical_Models/06_Nuclear_and_Particle_Physics/06-MASS_SPECTRUM_V2_HIERARCHY.md
 8 Research/Mathematical_Models/05_Quantum_Mechanics/05-QED_LOOPS_DERIVATION.md
 8 Research/Foundations/MEMBRANE_MASS_SCALE.md
 8 Vol_6/Manuscript/Ch_15_Connections_to_Other_Programs/Ch15_OUTLINE.md
 8 Vol_6/Back_Matter/APPENDIX_C_Problem_Sets_Comprehensive.md
 8 Vol_2/audio book/chapters/Ch04_clean.txt
 8 Vol_2/Manuscript/Ch_04_Strong_and_Weak_Forces_from_Zone_Boundary_Effects/Ch04_DRAFT.md
 7 Research/Mathematical_Models/ACTION_PLAN.md
 7 Research/Mathematical_Models/07_Relativity/07-RESOLVED_GRAVITY_MECHANISM.md
 7 Research/Mathematical_Models/06_Nuclear_and_Particle_Physics/06-REMAINING_DERIVATIONS.md
```

(Tail of the 348-file list trails off into 1-3-hit files; regenerable via the Phase 2 grep.)

---

## Appendix B — Reference: data files this plan was built from

Saved during planner run (not committed; for executor regeneration if needed):
- `/tmp/rev002/files.txt` — full 762-file in-scope inventory
- `/tmp/rev002/perfile_brane_nonRS.txt` — 317 files with `\bbrane\b` minus RS lines
- `/tmp/rev002/perfile_themembrane.txt` — 338 files with `\b[Tt]he membrane\b`
- `/tmp/rev002/perfile_compounds.txt` — 348 files with `\bmembrane (tension|wave|…)\b`
- `/tmp/rev002/subscripts4.txt` — 21-form LaTeX subscript inventory (74 occurrences)
- `/tmp/rev002/rs_lines.txt` — 150 Randall-Sundrum / braneworld preservation lines
- `/tmp/rev002/brane_nonRS.txt` — 3 379 line-level standalone-brane (non-RS) hits

The executor should regenerate these on a fresh checkout (Bash on Windows: GNU grep 3.0 — note `\{`/`\}` quirks under `-E`; use Python regex for the actual rewriter as documented in Phase 3 §4.2).
