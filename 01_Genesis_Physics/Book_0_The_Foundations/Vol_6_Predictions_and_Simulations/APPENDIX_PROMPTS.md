# Volume 6: Predictions, Simulations, and Open Problems — Appendix Prompts

One appendix per conversation. Copy the prompt below for the component you're ready to write, paste it into a fresh conversation, and let the skill run.

**This is the capstone of the entire 6-volume Foundations Series.** 8 back-matter components, each a standalone deliverable. Build order is enforced (Appendix A → B → C → D → E → F → Bibliography → Master Index). **ALL 17 Vol 6 chapters must be complete before starting any appendix.**

**Why per-appendix prompts?** Each component is the size of a short chapter (3,000–15,000 words) and requires reading different source material. Running them in separate conversations keeps the context window focused on the sources relevant to that specific deliverable.

**Special rules unique to the back matter:**
- Appendix A is the master prediction catalog — every `P-XXX` ID referenced anywhere in the volume must appear here with a falsification threshold
- Appendix E extends Vol 1 Appendix B — never redefine a symbol that's already there
- Appendix F is NEW to the series — it's the consolidated technology readiness table
- Bibliography must exceed 400 entries, compiled from all six volumes plus Vol 6 peer-review sources
- Master Index must cross-reference every concept across all 6 volumes (by Volume.Chapter.Section, with equation numbers where applicable)
- The Consistency Auditor reviewer runs the **SERIES-WIDE** check during the back matter phase — this is the last chance to catch inconsistencies across all 2,500+ pages

**Output location:** All back-matter files go in `Vol_6_Predictions_and_Simulations/Back_Matter/` (create the folder when starting Appendix A). Filename convention matches Vol 5:
- `BACK_MATTER_SPEC.md` (created once, during Appendix A)
- `APPENDIX_A_Complete_Prediction_Index.md`
- `APPENDIX_B_Simulation_Code_Repository.md`
- `APPENDIX_C_Problem_Sets_Comprehensive.md`
- `APPENDIX_D_Selected_Solutions.md`
- `APPENDIX_E_Notation_Reference_Complete_Series.md`
- `APPENDIX_F_Technology_Application_Summary.md`
- `Bibliography.md`
- `Master_Index.md`
- `STATUS.md`

---

## Appendix A: Complete Prediction Index

```
Use the genesis-chapter-writer skill to write Foundations Vol 6: Predictions, Simulations, and Open Problems, Back Matter — Appendix A: "Complete Prediction Index".

Follow the full 6-phase lifecycle: Spec → Outline (with figure/table plan) → Draft → Self-Review → Reviewer Agents → Finalize.

This is the FIRST back-matter component written. Create BACK_MATTER_SPEC.md during Phase 1 covering all 8 back-matter components (A, B, C, D, E, F, Bibliography, Master Index) in the style of Vol 5's BACK_MATTER_SPEC.md. Subsequent appendix conversations will reference the same spec.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 6
- Vol_5_The_Cosmos/Back_Matter/BACK_MATTER_SPEC.md (format reference — match this structure)
- ALL 17 Vol 6 chapter drafts, specifically pulling every P-XXX reference:
  - Ch 1 (Matches Observation) — predictions that match experiment
  - Ch 2 (Differs from SM) — distinguishing predictions
  - Ch 3 (Novel Predictions) — zone-unique predictions
  - Ch 4 (Falsification Criteria) — kill conditions
  - Ch 9 (FTL Travel) — FTL mechanism predictions
  - Ch 10 (Energy Harvesting) — energy extraction predictions
  - Ch 11 (FTL Communication) — communication predictions
  - Ch 12 (Advanced Sensors) — sensor predictions
- Research/Foundations/UNIQUE_PREDICTIONS.md
- Research/Mathematical_Models/Test_Results/TEST_RESULTS_2026-04-05_DEFINITIVE.md

Product: Foundations Vol 6 Back Matter
Component: Appendix A — Complete Prediction Index

Special instructions: Every P-XXX prediction that appears anywhere in Vol 6 must be cataloged here. Single master table with columns:

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |
|----|-------|-----------------|----------|--------------------|-----------| -----------------|--------|-------------------------|

Status values: MATCHES / DIFFERS / NOVEL / OPEN. Group predictions by category (Structural, Forces/Couplings, Particle Physics, Relativity/GR, Cosmology, Technology—FTL, Technology—Energy, Technology—Communication, Technology—Sensors). Within each category, order by P-XXX number. Include a cross-reference index at the end mapping source equation (V.Ch.Eq) → prediction ID. Every prediction must have a quantitative falsification threshold — if you find one without a threshold in a chapter draft, flag it as a gap before finalizing. The Skeptic reviewer will check that thresholds are genuinely falsifiable (not tautological). Target length: 8,000–12,000 words (mostly table + brief per-category intros). Create BACK_MATTER_SPEC.md alongside this appendix covering all 8 components.
```

---

## Appendix B: Simulation Code Repository

```
Use the genesis-chapter-writer skill to write Foundations Vol 6: Predictions, Simulations, and Open Problems, Back Matter — Appendix B: "Simulation Code Repository".

Follow the full 6-phase lifecycle: Spec → Outline (with figure/table plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 6
- Back_Matter/BACK_MATTER_SPEC.md (from Appendix A work)
- Ch_05_Simulation_Methodology/Ch05_DRAFT.md
- Ch_06_N_Body_Simulations/Ch06_DRAFT.md
- Ch_07_Membrane_Vibration_Spectra/Ch07_DRAFT.md
- Ch_08_Reproducibility_Package/Ch08_DRAFT.md
- Research/Simulations/README.md
- Research/Simulations/SIMULATION_RESULTS.md
- Research/Simulations/run_all_simulations.sh
- Every .py file in Research/Simulations/ (membrane_vibrations.py, structure_formation.py, waters_field_sim.py)
- Research/Simulations/energy_harvesting_simulation.html

Product: Foundations Vol 6 Back Matter
Component: Appendix B — Simulation Code Repository

Special instructions: The "hand-a-skeptic-a-laptop" reference. Sections:

B.1 — Repository URL and structure (GitHub path, directory tree)
B.2 — Environment specification (Python version, full requirements.txt contents, hardware requirements, OS compatibility)
B.3 — Docker / container image (if available; if not, document the gap honestly)
B.4 — Per-simulation documentation (one subsection per simulation):
      - Purpose and what Vol 6 chapter it validates
      - Exact command to run
      - Expected runtime and resource usage
      - Expected output files and verification checksums
      - How to interpret the results
B.5 — Master run script (`run_all_simulations.sh`) — walkthrough
B.6 — Test suite (how to run `pytest` across all 9 domain directories; expected pass/fail rate from TEST_RESULTS_2026-04-05_DEFINITIVE.md)
B.7 — Troubleshooting guide (common setup issues)
B.8 — How to contribute (PR workflow, issue templates)

Reproduce exact commands verbatim — a reader pastes them into a terminal and they must work. Where reproducibility is incomplete (e.g., no Docker image yet), state it explicitly as a known gap. Do NOT claim containerization if it isn't done. Target length: 4,000–6,000 words. The Student reviewer checks whether a grad student can go from git clone to running results in under an hour.
```

---

## Appendix C: Problem Sets — Comprehensive

```
Use the genesis-chapter-writer skill to write Foundations Vol 6: Predictions, Simulations, and Open Problems, Back Matter — Appendix C: "Problem Sets — Comprehensive".

Follow the full 6-phase lifecycle: Spec → Outline (with table plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 6
- Back_Matter/BACK_MATTER_SPEC.md
- Problem sets from ALL prior volumes:
  - Vol_1/Back_Matter/ (problem sets Ch 1–N)
  - Vol_2/Back_Matter/ (problem sets Ch 1–N)
  - Vol_3/Back_Matter/ (problem sets Ch 1–N)
  - Vol_4/Back_Matter/ (problem sets Ch 1–N)
  - Vol_5/Back_Matter/Problem_Sets_with_Selected_Solutions.md
- End-of-chapter problems from all 17 Vol 6 chapter drafts (if present in ChNN_DRAFT.md)

Product: Foundations Vol 6 Back Matter
Component: Appendix C — Problem Sets (Comprehensive)

Special instructions: This is NOT a regurgitation of prior volume problem sets. It is a curated *cross-volume* problem set that integrates concepts across the entire Foundations series — problems that require reasoning across multiple volumes to solve.

Organize by difficulty tier (following Foundations convention):
- Computational (quantitative, single-volume reasoning) — target 30 problems
- Conceptual (cross-volume, qualitative reasoning) — target 40 problems  
- Challenge (research-adjacent, multi-volume integration, open-ended) — target 20 problems
- Capstone (full-series synthesis, thesis-scale scope) — target 10 problems

Distribute across domains in proportion to volume length:
- Architecture & Axioms (Vol 1) — ~10%
- Forces & Fields (Vol 2) — ~15%
- Matter & Motion (Vol 3) — ~10%
- Quantum & Standard Model (Vol 4) — ~25%
- Cosmos & GR (Vol 5) — ~20%
- Predictions, Simulations, Technology (Vol 6) — ~20%

Every problem must cite source chapters in (V.Ch) form. Every problem must be *solvable* from the series text alone — no external prerequisites beyond what's covered. Challenge problems may require numerical/computational work — reference Appendix B simulations where relevant. Capstone problems are explicitly framed as thesis prompts and should be cross-referenced with Ch 14 (Open Problems). Target length: 10,000–15,000 words. Do NOT include solutions here — those are Appendix D.
```

---

## Appendix D: Selected Solutions

```
Use the genesis-chapter-writer skill to write Foundations Vol 6: Predictions, Simulations, and Open Problems, Back Matter — Appendix D: "Selected Solutions".

Follow the full 6-phase lifecycle: Spec → Outline → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 6
- Back_Matter/BACK_MATTER_SPEC.md
- Back_Matter/APPENDIX_C_Problem_Sets_Comprehensive.md (the problems to solve)
- Any selected-solutions appendices from Vol 1–5 for format reference (e.g., Vol_5/Back_Matter/Problem_Sets_with_Selected_Solutions.md)

Product: Foundations Vol 6 Back Matter
Component: Appendix D — Selected Solutions

Special instructions: Solve approximately 40% of the Appendix C problems with full worked solutions — specifically:
- ALL Capstone problems (10) — these are research invitations; solutions show a pathway, not a closed answer
- ~50% of Challenge problems (~10) — with full derivations
- ~40% of Conceptual problems (~16) — with clear reasoning chains
- ~25% of Computational problems (~8) — worked numerical examples

For each solved problem, format as:
- Problem restatement (abbreviated)
- Given / Find / Approach
- Worked solution with intermediate steps (cite equations from Vols 1–6 as used)
- Final answer / conclusion
- Discussion (what the problem illustrates, connection to larger themes)

For unsolved problems, include a one-line hint instead of a full solution (this gives students a push without spoiling). List by problem number matching Appendix C. Capstone solutions should end with "This problem is an active research direction — see Ch 14" and cross-reference the relevant Open Problems entry. Target length: 8,000–12,000 words. The Student reviewer checks whether the worked solutions are actually pedagogically useful, not just answer keys.
```

---

## Appendix E: Notation Reference (Complete Series)

```
Use the genesis-chapter-writer skill to write Foundations Vol 6: Predictions, Simulations, and Open Problems, Back Matter — Appendix E: "Notation Reference — Complete Series".

Follow the full 6-phase lifecycle: Spec → Outline (with table plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 6
- Back_Matter/BACK_MATTER_SPEC.md
- Vol_1/Back_Matter/APPENDIX_B_Notation_Reference.md (the canonical source — THIS IS WHAT YOU EXTEND)
- Quality_Control/Reference/Symbol_and_Constants.md
- All "new symbol" or "notation" sections introduced in Vols 2–6:
  - Vol 2: any field/coupling symbols not in Vol 1
  - Vol 3: thermodynamics, fluid, entropy symbols
  - Vol 4: quantum, field-theoretic, Standard Model symbols (this is the largest expansion)
  - Vol 5: GR, cosmology, Planck-unit symbols
  - Vol 6: prediction IDs (P-XXX), simulation parameters, technology-chapter symbols (FTL, energy extraction, sensor)
- Every chapter draft in Vols 2–6 for any symbol introduced but not yet compiled

Product: Foundations Vol 6 Back Matter
Component: Appendix E — Complete Notation Reference

Special instructions: This is the DEFINITIVE notation reference for the entire 6-volume series. Extend Vol 1 Appendix B — do NOT redefine a symbol that already lives there. Instead, for each symbol, record where it FIRST appears (V.Ch) and every volume that uses it.

Organize in sections:
E.1 — How to use this appendix (scope, conventions, what's in vs. out)
E.2 — Latin letters (alphabetical, lowercase then uppercase)
E.3 — Greek letters (alphabetical by Greek name)
E.4 — Mathematical operators and relations (∇, ⊗, ⊕, ≡, ∝, ...)
E.5 — Tensor/index conventions (raised/lowered indices, Einstein summation, Levi-Civita, metric signature)
E.6 — Unit and prefix conventions (natural units policy across volumes)
E.7 — Zone-architecture-specific notation (zone labels Z0–Z5, membrane notation, Waters field symbols)
E.8 — Constants reference (table of every physical constant with value, source definition, first appearance)
E.9 — Prediction identifier scheme (P-XXX numbering rules)
E.10 — Deprecated / superseded symbols (anything used in an early volume draft then replaced — document the mapping for archive readers)

Table format for each symbol:

| Symbol | Name | Definition / Units | First Appears | Used In | Related |

Target length: 6,000–9,000 words. The Consistency Auditor runs the series-wide symbol-consistency check against THIS appendix — if any chapter uses a symbol not documented here, either add it or correct the chapter. This appendix is the arbiter.
```

---

## Appendix F: Technology Application Summary

```
Use the genesis-chapter-writer skill to write Foundations Vol 6: Predictions, Simulations, and Open Problems, Back Matter — Appendix F: "Technology Application Summary".

Follow the full 6-phase lifecycle: Spec → Outline (with table plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 6
- Back_Matter/BACK_MATTER_SPEC.md
- Ch_09_FTL_Travel/Ch09_DRAFT.md (+ Part1/2/3 if still active)
- Ch_10_Energy_Harvesting/Ch10_FINAL.md (use FINAL if present, else Ch10_DRAFT.md)
- Ch_11_FTL_Communication/Ch11_DRAFT.md
- Ch_12_Advanced_Sensors/Ch12_DRAFT.md
- Ch_16_The_Technology_Roadmap/Ch16_DRAFT.md (staged timeline)
- Research/Mathematical_Models/07_Relativity/07-FTL_MECHANISMS_FORMAL.md
- Research/Mathematical_Models/07_Relativity/07-FTL_MECHANISMS_SUMMARY.md
- Research/Papers/membrane_resonance_generator.docx
- Research/Mathematical_Models/08_Cosmology/08-ENERGY_EXTRACTION_CREATION.md

Product: Foundations Vol 6 Back Matter
Component: Appendix F — Technology Application Summary (NEW to the series)

Special instructions: This appendix is NEW — no prior volume has an equivalent. It is the consolidated reference table for every technology concept the zone-architecture framework enables. A reader (engineer, investor, program manager) should be able to find every proposed technology, its physics basis, and its readiness level in one place.

Master table columns:

| Tech ID | Name | Category | Chapter Source | Physics Basis (V.Ch.Eq) | Energy / Power | Range / Scale | TRL | Stage (Ch 16) | Key Open Problems | Prediction IDs |

Tech ID scheme: T-FTL-NN (FTL), T-NRG-NN (Energy), T-COM-NN (Communication), T-SNS-NN (Sensors).

Categories and minimum coverage:
- **FTL Travel (T-FTL-01 through T-FTL-05):** The five FTL mechanisms from Ch 9 — temporal shortcuts, dimensional bypass, zone tunneling, field distortion (Alcubierre-like), consciousness interface
- **Energy Harvesting (T-NRG-01 through T-NRG-04):** Membrane resonance generator, Waters field extraction, vacuum energy harvesting, zone boundary energy
- **Communication (T-COM-01 through T-COM-04):** Entanglement-based, zone tunneling, Waters field modulation, consciousness interface
- **Sensors (T-SNS-01 through T-SNS-05+):** Membrane vibration detectors, Waters field sensors, zone boundary detectors, life-detection-from-space, GW spectrum extensions

TRL scale (NASA convention, 1–9):
1 — Basic principles observed; 2 — Technology concept formulated; 3 — Experimental proof of concept; 4 — Component validation in lab; 5 — Component validation in relevant environment; 6 — System demo in relevant environment; 7 — System demo in operational environment; 8 — System qualified; 9 — System proven in operations.

Most zone-architecture technologies will be TRL 1–3 (honest). State the honest TRL; don't inflate.

For each technology, also provide a 2–3 paragraph narrative entry covering: what it does, how the physics works, what would have to be true to build it, and what the nearest-term experiment is. Cross-reference to the Ch 16 timeline stage (Stage 1–4).

Target length: 6,000–9,000 words. The Physicist reviewer checks each entry for physics consistency; the Skeptic checks that TRL ratings are honest and not aspirational.
```

---

## Comprehensive Bibliography

```
Use the genesis-chapter-writer skill to write Foundations Vol 6: Predictions, Simulations, and Open Problems, Back Matter — Comprehensive Bibliography.

Follow the full 6-phase lifecycle: Spec → Outline → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 6
- Back_Matter/BACK_MATTER_SPEC.md
- Bibliographies from every prior volume:
  - Vol_1/Back_Matter/Bibliography.md (or equivalent)
  - Vol_2/Back_Matter/Bibliography.md
  - Vol_3/Back_Matter/Bibliography.md
  - Vol_4/Back_Matter/Bibliography.md
  - Vol_5/Back_Matter/Bibliography.md
- Citations scattered in all 17 Vol 6 chapter drafts (extract anything in [Author Year] or numeric-ref form)
- Research/Peer_Review/critic_report.md (reference list)
- Research/Peer_Review/skeptic_analysis.md (reference list)

Product: Foundations Vol 6 Back Matter
Component: Comprehensive Bibliography (series-wide)

Special instructions: This is the MASTER bibliography for the entire Foundations series — 400+ entries minimum. Merge, deduplicate, and canonicalize every citation from Vols 1–6. Where a source appears in multiple volumes, keep ONE entry and tag which volumes cite it.

Organize in sections:
Bib.1 — Foundational physics texts (classical mechanics, EM, thermo, QM, relativity)
Bib.2 — Modern theoretical physics (QFT, Standard Model, GR, cosmology)
Bib.3 — Experimental physics & precision measurement (LIGO, Planck, LHC, atomic physics, g-2, etc.)
Bib.4 — Theoretical programs compared in Ch 15 (string theory, LQG, causal sets, constructor theory, holography)
Bib.5 — Scripture and theological sources (Genesis, biblical scholarship, theological works referenced)
Bib.6 — Philosophy of science and methodology
Bib.7 — Technology, engineering, and applied physics (for Ch 9–12, 16)
Bib.8 — Zone-architecture internal sources (Jeff Raymond's working papers, research notes published alongside the series)
Bib.9 — Online resources, databases, and simulation code repositories

Format: Chicago author-date or APA (pick one, apply consistently — match prior volumes). For each entry include volume tags: `[V1, V4, V5]` etc. showing where cited. Mark internal sources explicitly (`[Internal]`). Provide a separate reverse index: concept → entries (e.g., "Bell inequalities: [Bell 1964], [Aspect et al. 1982], [Hensen et al. 2015]").

Every citation used in the text MUST appear here; every entry here must be cited at least once. The Style Editor reviewer runs the citation-completeness audit. Target length: 15,000–25,000 words (mostly entries — this is a dense reference).
```

---

## Master Index

```
Use the genesis-chapter-writer skill to write Foundations Vol 6: Predictions, Simulations, and Open Problems, Back Matter — Master Index.

Follow the full 6-phase lifecycle: Spec → Outline → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 6
- Back_Matter/BACK_MATTER_SPEC.md
- Back_Matter/APPENDIX_A_Complete_Prediction_Index.md (for P-XXX cross-references)
- Back_Matter/APPENDIX_E_Notation_Reference_Complete_Series.md (for symbol cross-references)
- Back_Matter/APPENDIX_F_Technology_Application_Summary.md (for T-XXX cross-references)
- Per-volume indexes / TOCs from every volume:
  - Vol 1 table of contents and any existing index
  - Vol 2 — same
  - Vol 3 — same
  - Vol 4 — same
  - Vol 5 — same
  - Vol 6 — all 17 chapter drafts (use chapter headings + key subheads)
- Quality_Control/Reference/Glossary.md (if present)
- Quality_Control/Reference/Zone_Architecture.md (canonical zone terminology)

Product: Foundations Vol 6 Back Matter
Component: Master Index (series-wide, 6 volumes)

Special instructions: This is the definitive index for the entire 2,500+ page Foundations series. A reader looking up any concept, person, equation, zone, particle, or phenomenon should find every location where it appears across all 6 volumes.

Format: alphabetical, indented subentries, with locators in `V.Ch` form (and `V.Ch.§N` when a more precise subsection exists, `V.Ch.Eq(X.Y.Z)` for equation locators).

Example format:

```
entropy
  as zone-architecture consequence, V1.11.§3, V3.12.§1
  Bekenstein-Hawking, V4.7.§4, V5.8.§2
  dark sector, V5.11.§5
  derivation from Zone topology, V1.11.Eq(1.11.5), V3.12.Eq(3.12.8)
  second law, V3.12, V5.11
  see also: free energy; information; thermodynamics
```

Required entry categories:
- All **named concepts** (zone, Firmament, Waters, membrane, sustaining coupling, etc.)
- All **people** (Maxwell, Einstein, Planck, Bell, etc.)
- All **particles** (electron, photon, quark types, hypothetical zone-architecture particles)
- All **equations** that are explicitly numbered and referenced (format: "equation X.Y.Z (name)")
- All **experiments** referenced (LHC, LIGO, Planck satellite, Michelson-Morley, etc.)
- All **fields and forces** (electromagnetism, Waters field, Higgs, dark energy, dark matter, etc.)
- All **technologies** (FTL mechanisms, membrane resonance generator, etc. — cross-ref Appendix F)
- All **theorems** (Noether, Goldstone, Bell, etc.)
- All **constants** (α, ℏ, G, k_B, etc. — cross-ref Appendix C of Vol 5 for derivation chains)
- All **scripture references** cited in the series (Genesis 1:1, etc.)
- All **P-XXX prediction IDs** (cross-ref Appendix A)
- All **T-XXX technology IDs** (cross-ref Appendix F)

Also include: "see" and "see also" cross-references liberally. Distinguish primary locations (where the concept is introduced or most fully developed) using **bold** formatting on the locator.

Target length: 12,000–20,000 words. The Navigator reviewer checks whether the index actually lets a reader navigate the series — the final test is "pick a concept at random, look it up, and see if every substantive mention across 6 volumes is listed." Include 5 such spot-checks in the STATUS.md for this component.
```

---

## Usage Reminders

- **One appendix per conversation.** Each back-matter component is a standalone deliverable, and the source material is different for each.
- **Build order is enforced.** Appendix A → B → C → D → E → F → Bibliography → Master Index. Later components reference earlier ones (D references C; Master Index references A, E, F).
- **ALL 17 Vol 6 chapters must be complete** before starting Appendix A. If any chapter is still in draft/review, resolve it first.
- **The BACK_MATTER_SPEC.md is created during the Appendix A conversation** and lives in `Back_Matter/`. All subsequent appendix conversations read it.
- **Citation convention:** `(V.Ch.Eq)` with `V ∈ {1,2,3,4,5,6}` — same as the chapter drafts.
- **Output folder:** `Vol_6_Predictions_and_Simulations/Back_Matter/` — create during Appendix A.
- **Reviewer assignments for back matter:**
  - Appendix A: Physicist, Skeptic (falsifiability), Consistency Auditor
  - Appendix B: Student, Writing Coach (reproducibility clarity)
  - Appendix C: Physicist, Student, "But Why?" Reader
  - Appendix D: Student, Physicist
  - Appendix E: Consistency Auditor (**series-wide symbol check runs HERE**)
  - Appendix F: Physicist, Skeptic (honest TRLs), Navigator
  - Bibliography: Style Editor (citation completeness), Consistency Auditor
  - Master Index: Navigator (navigability spot-checks), Style Editor
- **Run the FULL test suite** (all 9 domain directories) during Appendix B or A work — report the honest pass/fail rate. Update `TEST_RESULTS_2026-04-DD.md` with the final run.
- **The Consistency Auditor's SERIES-WIDE audit** happens during Appendix E (symbols), Bibliography (citations), and Master Index (cross-references). This is the last guard rail before the series is declared complete.
- **Final step after Master Index passes:** update `STATUS.md` in `Back_Matter/` marking the Foundations Series VERIFIED and capture the final test-suite pass rate.
