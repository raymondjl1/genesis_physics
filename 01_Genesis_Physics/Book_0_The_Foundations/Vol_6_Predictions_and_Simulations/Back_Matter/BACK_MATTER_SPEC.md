# Vol 6 Back Matter — Specification & Outline

**Product:** Foundations Vol 6, Predictions, Simulations, and Open Problems
**Scope:** Appendices A, B, C, D, E, F; Bibliography; Master Index
**Lifecycle phase:** Phase 1 (Spec) + Phase 2 (Outline) — this document
**Voice:** Feynman writing a textbook, with the confidence of complete results and the humility of honest gaps (match Vol 1–5 back matter register)
**Citation convention:** `(V.Ch.Eq)` with `V ∈ {1,2,3,4,5,6}`

---

## Mission

Give the Vol 6 reader — a graduate student, a professional physicist, an experimental researcher, or the "skeptical physicist with a laptop" — a single, self-contained reference for every testable commitment the zone-architecture framework makes, every simulation that validates it, every symbol used anywhere in the 2,500+ page series, every technology it implies, and every citation that grounds it in the literature.

This is the capstone back matter of the entire six-volume Foundations Series. Unlike Vol 5's back matter (which covered five prior volumes), Vol 6's back matter covers **all six** — and introduces two entirely new reference deliverables (Appendix F, the Technology Application Summary, and the Master Index) that have no precedent in earlier volumes.

The back matter must:

1. **Catalog every testable prediction (Appendix A).** Every P-XXX identifier that appears anywhere in Vol 6 — 153 in total — must be recorded in one master table with a quantitative falsification threshold. This is the framework's single most important deliverable to the physics community: the consolidated, scrutable bet.
2. **Make the computational validation reproducible (Appendix B).** Hand a skeptic a laptop. The simulations must run. The test suite must pass where it says it passes. The gaps must be stated honestly.
3. **Integrate the physics pedagogy across six volumes (Appendices C, D).** Problem sets and selected solutions that force the reader to reason across volumes — not a regurgitation of prior problem sets.
4. **Unify the notation (Appendix E).** Extend Vol 1 Appendix B into the definitive symbol reference for the series. Arbitrate disputes.
5. **Summarize the technology implications (Appendix F).** NEW to the series. Every T-XXX technology concept from Ch 9–12 and Ch 16 in one master table, with honest TRLs.
6. **Provide the master bibliography (~400 entries).** Merged, deduplicated, canonicalized. Volume tags on every entry.
7. **Provide the master index (series-wide).** Every concept, person, equation, zone, particle, phenomenon — cross-referenced across all 6 volumes.

---

## Requirements Traced to WRITING_PROMPT.md, CLAUDE.md, and APPENDIX_PROMPTS.md

| Req | Source | Covered by |
|-----|--------|-----------|
| Every prediction numbered P-XXX with falsification threshold | WRITING_PROMPT.md §Special Rules | App A |
| 153 total predictions (P-001 through P-153) from Ch 1–4, 9–12 | Chapter drafts | App A |
| Single master table with 9 columns as specified | APPENDIX_PROMPTS.md App A | App A |
| Status values MATCHES / DIFFERS / NOVEL / OPEN | APPENDIX_PROMPTS.md App A | App A |
| Honest test-suite pass rate (97/136 PASS, 37 PARTIAL, 2 NOT YET, 0 FAIL) | TEST_RESULTS_2026-04-05_DEFINITIVE.md | App A §A.2, App B §B.6 |
| Simulation reproducibility package | CLAUDE.md Gaps table | App B |
| Cross-volume problem sets (100 problems across 4 tiers) | APPENDIX_PROMPTS.md App C | App C |
| Selected solutions (~40% of problems) | APPENDIX_PROMPTS.md App D | App D |
| Series-wide notation reference (extends Vol 1 App B) | APPENDIX_PROMPTS.md App E | App E |
| Technology Application Summary (NEW) with NASA TRL scale | APPENDIX_PROMPTS.md App F | App F |
| ≥400 bibliography entries merged across 6 volumes | APPENDIX_PROMPTS.md Bibliography | Bibliography |
| Master index with V.Ch, V.Ch.§N, V.Ch.Eq locators | APPENDIX_PROMPTS.md Master Index | Master Index |
| No forward references beyond Vol 6 | CLAUDE.md Special Rules | All components |
| Citation convention `(V.Ch.Eq)` with `V ∈ {1..6}` | APPENDIX_PROMPTS.md | All components |
| Consistency with Vol 5 back matter format | APPENDIX_PROMPTS.md | All components |

---

## Prerequisites (What the Reader Already Has)

- Working knowledge of Vols 1–5 (axioms, forces, classical mechanics, QM/QFT, Standard Model, GR, cosmology)
- Vol 6 Chapters 1–17 read in sequence (problem sets and appendices never forward-reference beyond Ch 17)
- Vol 1 Appendix B (the canonical notation reference that Appendix E extends, not supersedes)
- Familiarity with the P-XXX prediction identifier scheme (established in Ch 1 and used throughout Vol 6)
- Access to the simulation code repository (Appendix B gives exact git commands; earlier volumes do not)

---

## "Why" Chain the Back Matter Answers

- **Why Appendix A?** The 153 predictions are scattered across eight chapters (Ch 1–4, 9–12). A skeptical physicist needs one place where every commitment is recorded, grouped by category, and annotated with a falsification threshold. Without Appendix A, the framework's risk profile cannot be assessed.
- **Why Appendix B?** "This framework is computationally validated" is a claim. Appendix B is the evidence. Either the simulations run (and produce the claimed results) or they do not. The appendix cannot hide behind narrative; it must expose the code.
- **Why Appendix C (and D)?** Foundations rule: every volume has problem sets. Vol 6's distinctive contribution is *cross-volume* problems — reasoning that requires Vol 1's axioms, Vol 4's Standard Model, and Vol 5's cosmology simultaneously. These are the problems that test whether the reader has actually integrated the series.
- **Why Appendix E?** The series introduces hundreds of symbols across six volumes. A symbol introduced in Vol 2 may appear in Vol 5 with slightly different notation. Appendix E is the arbiter — the Consistency Auditor runs the series-wide symbol check against it.
- **Why Appendix F (NEW)?** The zone-architecture framework implies specific technologies (FTL mechanisms, membrane resonance generator, life-detection-from-space). Engineers, program managers, and investors need these in one table with honest TRLs. Earlier volumes handle this piecemeal; Appendix F consolidates.
- **Why the bibliography?** Six volumes across a 2,500-page series will accumulate duplicate citations in per-volume bibliographies. One consolidated, deduplicated master reference of 400+ entries replaces six separate ones for the reader who wants to follow a citation backward.
- **Why the master index?** The series is large enough that a reader cannot find every mention of "entropy" or "Bell inequality" by memory. The master index is the physical navigation substrate — without it, the series is not fully navigable.

---

## Figure & Table Plan (Back Matter Aggregate)

Back matter is table-dense, figure-sparse. Each appendix specifies its own figures and tables in its component section below; the aggregate is:

| Component | Tables | Figures |
|-----------|--------|---------|
| App A (Prediction Index) | 10 category tables + 1 master table + 1 cross-reference index | 1 summary bar chart (predictions by category × status) |
| App B (Simulation Repo) | 4 tables (simulations inventory, dependencies, test-suite results, TRL of reproducibility) | 1 directory tree diagram |
| App C (Problem Sets) | 1 table (problem distribution across tiers × volumes) | 0 |
| App D (Selected Solutions) | 1 table (solution inventory) | 0 |
| App E (Notation Reference) | 10 section tables (one per E.2–E.10) | 0 |
| App F (Technology Summary) | 1 master table (all T-XXX) + 4 category tables | 1 TRL landscape diagram |
| Bibliography | 9 section tables | 0 |
| Master Index | N/A (the index IS the table) | 0 |

No full-page pictorial figures; the back matter is a reference artifact.

---

## Appendix A: Complete Prediction Index

**Structure:**

- §A.1 How to use this appendix — column definitions, status values, precision conventions
- §A.2 Test-suite context — the 136-test validation state and how Appendix A predictions map onto test results (97 PASS / 37 PARTIAL / 0 FAIL / 2 NOT YET)
- §A.3 Category I — Structural Predictions (conservation laws, zone topology, gauge structure) — P-031 to P-034, P-042, P-050, P-051, P-081, P-082
- §A.4 Category II — Forces and Couplings — P-004 to P-006, P-056 to P-058, P-065
- §A.5 Category III — Particle Physics — P-014 to P-023, P-044 to P-048, P-052 to P-055, P-066, P-067, P-074, P-075, P-144
- §A.6 Category IV — Relativity and General Relativity — P-007 to P-013, P-059, P-060, P-068 to P-070, P-100, P-101, P-151 to P-153
- §A.7 Category V — Cosmology — P-024 to P-030, P-061 to P-064, P-076 to P-079, P-082, P-141, P-143, P-145, P-146
- §A.8 Category VI — QED and Electromagnetism — P-001 to P-003, P-040, P-041, P-043, P-049
- §A.9 Category VII — Technology: FTL — P-083, P-084, P-089 to P-102
- §A.10 Category VIII — Technology: Energy — P-085, P-086, P-103 to P-118
- §A.11 Category IX — Technology: Communication — P-087, P-088, P-119 to P-135
- §A.12 Category X — Technology: Sensors — P-136 to P-142, P-147 to P-150
- §A.13 Master table — all 153 predictions, status, confidence, timeline
- §A.14 Cross-reference index — source equation (V.Ch.Eq) → prediction ID
- §A.15 Falsification-threshold gap report — any P-XXX without a quantitative threshold (flagged during audit)

**Critical requirement:** Every P-XXX cited anywhere in Vol 6 Ch 1–4 or Ch 9–12 must have a row in the master table with a quantitative falsification threshold. The Skeptic reviewer checks that each threshold is genuinely falsifiable (not tautological: e.g., "prediction fails if it is falsified" is *not* a falsification threshold). Predictions where the chapter draft omits a numerical threshold must be flagged in §A.15 as gaps, with either (a) a proposed threshold extracted from the derivation, or (b) an explicit note that the prediction is currently unfalsifiable and recommending Ch 14 for treatment.

**Column format (every row):**

| ID | Title | Predicted Value | SM Value | Experimental Value | Precision | Source (V.Ch.Eq) | Status | Falsification Threshold |

Target length: 8,000–12,000 words (mostly table + per-category intros of 150–300 words each).

---

## Appendix B: Simulation Code Repository

**Structure:**

- §B.1 Repository URL and structure — GitHub path, directory tree
- §B.2 Environment specification — Python version (3.10+), full `requirements.txt` contents, hardware requirements, OS compatibility
- §B.3 Docker / container image — if available; honest documentation of the gap if not
- §B.4 Per-simulation documentation (one subsection each):
  - `membrane_vibrations.py` — validates Ch 7
  - `structure_formation.py` — validates Ch 6
  - `waters_field_sim.py` — validates Ch 6, Ch 3 predictions P-077/P-078
  - `energy_harvesting_simulation.html` — interactive validation for Ch 10
  - Each with: purpose, exact command, expected runtime, expected output files and checksums, interpretation guide
- §B.5 Master run script `run_all_simulations.sh` — walkthrough
- §B.6 Test suite status — how to run `pytest` across the 9 domain directories; **expected pass rate 97/136 = 71.3%** from TEST_RESULTS_2026-04-05_DEFINITIVE.md with honest PARTIAL and NOT YET accounting
- §B.7 Troubleshooting guide — common setup issues (pip versions, numpy/scipy conflicts, Python 3.12 compatibility)
- §B.8 How to contribute — PR workflow, issue templates, labeling convention (`book:foundations`, `vol:6`, `phase:*`)

**Critical requirement:** Every command in Appendix B must be verbatim-pasteable. Reproducibility gaps (no Docker image yet, absent CI badge, missing test fixtures) must be stated explicitly — no claims of containerization unless the Dockerfile exists in the repo. The Student reviewer runs the "git clone → first result in under 1 hour" test.

Target length: 4,000–6,000 words.

---

## Appendix C: Problem Sets — Comprehensive

**Structure:**

- §C.0 Prerequisites, difficulty-tier conventions, citation rules
- §C.1 Computational problems (~30 problems, ★ to ★★) — single-volume quantitative
- §C.2 Conceptual problems (~40 problems, ★★) — cross-volume qualitative reasoning
- §C.3 Challenge problems (~20 problems, ★★★) — multi-volume integration; may reference Appendix B simulations
- §C.4 Capstone problems (~10 problems, ★★★★) — thesis-scale; each explicitly cross-referenced to Ch 14 Open Problems

**Domain distribution:**

| Domain | Volumes | Target Problems | % |
|--------|---------|-----------------|---|
| Architecture & Axioms | Vol 1 | 10 | 10% |
| Forces & Fields | Vol 2 | 15 | 15% |
| Matter & Motion | Vol 3 | 10 | 10% |
| Quantum & Standard Model | Vol 4 | 25 | 25% |
| Cosmos & GR | Vol 5 | 20 | 20% |
| Predictions, Simulations, Technology | Vol 6 | 20 | 20% |

**Numbering scheme:** `P6.T.N` where T ∈ {C, Q, X, K} (Computational, Conceptual, Challenge, Capstone) and N is sequential within tier. Every problem cites source chapters in (V.Ch) form. No problem may require material outside Vols 1–6.

Target length: 10,000–15,000 words (no solutions).

---

## Appendix D: Selected Solutions

**Structure:**

- §D.0 How to use this appendix — solved vs. hint-only, citation conventions
- §D.1 Computational solutions — ~8 problems worked in full
- §D.2 Conceptual solutions — ~16 problems worked with reasoning chains
- §D.3 Challenge solutions — ~10 problems with full derivations
- §D.4 Capstone solutions — ALL 10 problems, framed as research pathways ending with "This problem is an active research direction — see Ch 14"

**Solved problem format:**

- Problem restatement (abbreviated)
- Given / Find / Approach
- Worked solution (intermediate steps, cite equations as used)
- Final answer / conclusion
- Discussion (connection to larger themes, cross-reference to Appendix A predictions where a problem validates or stress-tests one)

**Unsolved problem format:** Problem number + one-line hint.

Target length: 8,000–12,000 words.

---

## Appendix E: Notation Reference (Complete Series)

**Structure:**

- §E.1 How to use this appendix — scope (extends Vol 1 App B, does not supersede), conventions
- §E.2 Latin letters — lowercase then uppercase, alphabetical
- §E.3 Greek letters — alphabetical by Greek name (α, β, γ, δ, ε, ζ, η, θ, ι, κ, λ, μ, ν, ξ, ο, π, ρ, σ, τ, υ, φ, χ, ψ, ω)
- §E.4 Mathematical operators and relations — ∇, ⊗, ⊕, ≡, ∝, □ (d'Alembertian), 〈·〉 (expectation), etc.
- §E.5 Tensor / index conventions — raised/lowered indices, Einstein summation, Levi-Civita, metric signature (+−−−− on the 4D brane, +−−−−−− on the 6D bulk)
- §E.6 Unit and prefix conventions — natural units policy across volumes (ℏ = c = 1 in Vol 4; SI in Vol 2; units-explicit in Vol 5)
- §E.7 Zone-architecture-specific notation — Z0–Z5 (Zone labels), Firmament ($\mathcal{F}$), Waters Above ($\Psi_A$), Waters Below ($\Psi_B$), boundary scales ($\xi_A$, $\eta_B$)
- §E.8 Constants reference — table of every physical constant (α, ℏ, G, k_B, c, e, etc.) with value, source definition, first appearance
- §E.9 Prediction identifier scheme — P-XXX numbering rules, category ranges, cross-reference to Appendix A
- §E.10 Deprecated / superseded symbols — anything used in an early draft then replaced, with the canonical mapping

**Row format:**

| Symbol | Name | Definition / Units | First Appears | Used In | Related |

**Critical requirement:** Appendix E is the arbiter. If any chapter uses a symbol not in Appendix E, the chapter is inconsistent — either fix the chapter or extend Appendix E. The Consistency Auditor runs the series-wide symbol check against this appendix.

Target length: 6,000–9,000 words.

---

## Appendix F: Technology Application Summary (NEW)

**Structure:**

- §F.0 Purpose — why a technology summary, TRL scale definitions (NASA 1–9)
- §F.1 FTL Travel (T-FTL-01 through T-FTL-05) — five mechanisms from Ch 9
  - T-FTL-01: Temporal Shortcut (Mechanism 1)
  - T-FTL-02: Dimensional Bypass (Mechanism 2)
  - T-FTL-03: Zone Tunneling (Mechanism 3)
  - T-FTL-04: Field Distortion / Warp Bubble (Mechanism 4)
  - T-FTL-05: Consciousness Interface (Mechanism 5)
- §F.2 Energy Harvesting (T-NRG-01 through T-NRG-04) — from Ch 10
  - T-NRG-01: Membrane Resonance Generator (MRG)
  - T-NRG-02: Waters Above Expansion Sail
  - T-NRG-03: Vacuum Energy / Dynamic Casimir Array
  - T-NRG-04: Zone-Boundary Latent-Heat Extraction
- §F.3 Communication (T-COM-01 through T-COM-04) — from Ch 11
  - T-COM-01: Entanglement-Based Signaling (null — no-signaling; P-132)
  - T-COM-02: Zone-Tunneling Channel
  - T-COM-03: Waters-Field Modulation Channel
  - T-COM-04: Consciousness-Interface Channel
- §F.4 Sensors (T-SNS-01 through T-SNS-06) — from Ch 12
  - T-SNS-01: Membrane Vibration Interferometer (MVI)
  - T-SNS-02: Atom-Interferometer Waters-Field Sensor
  - T-SNS-03: Dark-Matter Imaging Aperture
  - T-SNS-04: LIGO Retrofit for Extended GW Polarizations
  - T-SNS-05: Life-Detection-from-Space Gravimeter (GRACE-Bio)
  - T-SNS-06: Zone-Boundary Anomaly Cosmology Cross-Correlator
- §F.5 Master table — all 18 technologies, TRL, Stage (Ch 16), prediction IDs, open problems

**Row format:**

| Tech ID | Name | Category | Chapter Source | Physics Basis (V.Ch.Eq) | Energy / Power | Range / Scale | TRL | Stage (Ch 16) | Key Open Problems | Prediction IDs |

**Critical requirement:** TRL ratings must be honest. Most zone-architecture technologies are TRL 1–3. The Skeptic reviewer checks that no TRL is inflated. The Physicist reviewer checks physics consistency for each entry. Narrative entries (2–3 paragraphs) cover: what it does, how the physics works, what would have to be true to build it, the nearest-term experiment.

Target length: 6,000–9,000 words.

---

## Comprehensive Bibliography — Plan

**Target:** ≥400 entries (minimum), organized in sections:

- Bib.1 — Foundational physics texts (~40 entries; Newton, Maxwell, Einstein, Dirac, Feynman lectures, MTW, Jackson, Goldstein, Landau-Lifshitz)
- Bib.2 — Modern theoretical physics (~60 entries; Weinberg QFT I/II/III, Peskin-Schroeder, Srednicki, Wald, Carroll, Mukhanov)
- Bib.3 — Experimental physics & precision measurement (~60 entries; Gabrielse g-2, LIGO/Virgo GW catalog, Planck 2018 I–XIII, ATLAS/CMS Higgs discovery, Super-Kamiokande, XENONnT)
- Bib.4 — Theoretical programs compared (~30 entries; Polchinski string theory, Rovelli LQG, Sorkin causal sets, Deutsch-Marletto constructor theory, holography original papers)
- Bib.5 — Scripture and theological sources (~20 entries; Genesis 1–3 editions, NRSV, biblical scholarship on creation narrative, Hebrew lexicons)
- Bib.6 — Philosophy of science and methodology (~25 entries; Popper, Kuhn, Lakatos, Feyerabend, Dawid, Maudlin)
- Bib.7 — Technology, engineering, and applied physics (~40 entries; Alcubierre 1994, Morris-Thorne wormholes, Casimir original, BCS original, NASA TRL reports)
- Bib.8 — Zone-architecture internal sources (~60 entries; Jeff Raymond working papers, `PARTICLE_MASS_SPECTRUM_SUMMARY.md`, `FTL_MECHANISMS_FORMAL.md`, `UNIQUE_PREDICTIONS.md`, `ENERGY_FRACTIONS_DERIVATION.md`, `SUSTAINING_COUPLING.md`, etc.)
- Bib.9 — Online resources, databases, and simulation repositories (~25 entries; PDG, NIST CODATA, arXiv, GitHub simulation repo, HEPData)
- Bib.10 — Reverse index (concept → entries)

**Citation format:** Chicago author-date, with volume tags `[V1, V4, V5]` showing citing volumes. Internal sources marked `[Internal]`. Class symbols: 📜 foundational, 📘 textbook, ⚛ experiment, ⚙ data compilation, ☷ zone-architecture internal.

**Critical requirement:** Every citation in Vols 1–6 appears exactly once here; every entry here is cited at least once. The Style Editor runs the citation-completeness audit.

Target length: 15,000–25,000 words.

---

## Master Index — Plan

**Format:** Alphabetical, indented subentries, with locators in `V.Ch`, `V.Ch.§N`, `V.Ch.Eq(X.Y.Z)` form. Primary (introduction / most complete development) locators in **bold**.

**Required entry categories:**

- Named concepts (zone, Firmament, Waters, membrane, sustaining coupling, zone transition, brane)
- People (Einstein, Planck, Bell, Feynman, Maxwell, Dirac, Hawking, Bekenstein, Alcubierre, ~40 entries)
- Particles (electron, photon, quark flavors, W/Z, Higgs, graviton, KK modes, ~30 entries)
- Equations (numbered and referenced, format: "equation X.Y.Z (name)")
- Experiments (LHC, LIGO, Planck satellite, Michelson-Morley, Pound-Rebka, Super-Kamiokande, JUNO, DUNE, XENONnT, DESI, Euclid, ~40 entries)
- Fields and forces (electromagnetism, Waters field Above/Below, Higgs, dark energy, dark matter, gravitation, strong, weak)
- Technologies (FTL mechanisms, MRG, life-detection gravimeter; cross-ref Appendix F)
- Theorems (Noether, Goldstone, Bell, CPT, spin-statistics, no-hair, Holevo, Tsirelson)
- Constants (α, ℏ, G, k_B, c, e, Rydberg; cross-ref Vol 5 App C derivation chains)
- Scripture references (Genesis 1:1, 1:6–8, 1:14–18, etc.)
- P-XXX prediction IDs (cross-ref Appendix A)
- T-XXX technology IDs (cross-ref Appendix F)

**Navigator spot-check requirement:** STATUS.md includes 5 randomly selected concepts; verify every substantive mention across 6 volumes is listed.

Target length: 12,000–20,000 words.

---

## Build Order and Dependencies

Enforced order (each component consumes earlier outputs):

1. **Appendix A** (FIRST; creates `BACK_MATTER_SPEC.md`) — catalogs P-XXX scheme that Appendix E §E.9 and Master Index require
2. **Appendix B** — consumes nothing downstream; independent
3. **Appendix C** — independent (sources are the series)
4. **Appendix D** — depends on Appendix C (solves its problems)
5. **Appendix E** — independent of A–D but preferred after D so all symbols from problem sets are captured; runs SERIES-WIDE symbol audit
6. **Appendix F** — depends on Appendix A (cross-references P-XXX to T-XXX) and Appendix E (T-XXX scheme)
7. **Bibliography** — depends on no appendix but compiles citations from all; runs SERIES-WIDE citation audit
8. **Master Index** — LAST; depends on A (P-XXX), E (symbols), F (T-XXX); runs SERIES-WIDE navigability audit

---

## Verification Criteria

- [ ] Every P-XXX cited in any Vol 6 chapter (Ch 1–17) appears in App A §A.13 master table
- [ ] Every row in App A has a non-empty, non-tautological "Falsification Threshold" column, OR is flagged in §A.15
- [ ] Status values are exactly one of {MATCHES, DIFFERS, NOVEL, OPEN} (no drift)
- [ ] App B commands execute end-to-end on a Python 3.10 environment
- [ ] App B §B.6 test-suite pass rate matches `TEST_RESULTS_2026-04-05_DEFINITIVE.md` (97/136, 71.3%)
- [ ] App C has ≥100 problems distributed per the domain/tier plan
- [ ] App D solves ≥40% of App C problems (ALL Capstones, ~50% Challenge, ~40% Conceptual, ~25% Computational)
- [ ] App E includes every symbol introduced in any Vol 1–6 chapter
- [ ] App E §E.9 lists every P-XXX range by chapter
- [ ] App F has honest TRLs; no entry above TRL 3 without explicit engineering evidence
- [ ] Bibliography ≥ 400 unique entries across 10 sections
- [ ] Bibliography reverse index covers all sections
- [ ] Master Index covers 100% of "Required entry categories" list
- [ ] Master Index has bold primary locators for every major concept
- [ ] No forward references beyond Vol 6 in any component
- [ ] Citation convention `(V.Ch.Eq)` with `V ∈ {1..6}` consistent across all components
- [ ] No component exceeds its target word count by more than 25%

---

*Phase 1 + Phase 2 complete. Phase 3 (draft) begins in the eight component files in this folder. Appendix A is the first deliverable.*
