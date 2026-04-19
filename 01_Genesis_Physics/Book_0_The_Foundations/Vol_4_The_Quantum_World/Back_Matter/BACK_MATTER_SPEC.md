# Vol 4 Back Matter — Specification & Outline

**Product:** Foundations Vol 4, The Quantum World
**Scope:** Appendices A, B, C; Problem Sets (Ch 1–14); Bibliography
**Lifecycle phase:** Phase 1 (Spec) + Phase 2 (Outline) — this document
**Voice:** Feynman writing a textbook (match Vols 1–3 back matter register)
**Citation convention:** `(V.Ch.Eq)` with `V ∈ {1,2,3,4}`

---

## Mission

Give the Vol 4 reader — a graduate student or working physicist — a single, compact, self-contained reference for everything the volume uses or produces, with honest accounting of what the zone-architecture framework gets right, what it gets wrong, and by how much.

This is the largest back matter in the series so far (target: ~25,000 words). It must:

1. Let any reader navigate from a Vol 4 derivation back to the Vol 1–3 equation it inherits (Appendix A + reverse index).
2. Show every Standard-Model particle's zone-architecture prediction next to the experimental value, with fractional errors — including the cases where the framework is off by factors of ~10³ — with no cherry-picking (Appendix B).
3. Provide every Feynman rule used in Chapters 7, 10–14 in one compiled reference (Appendix C).
4. Give worked problem sets for every chapter with selected solutions (Ch 1–14).
5. Provide a 200+ entry bibliography covering QM, QFT, particle physics, experimental tests, Standard Model references, and zone-architecture internal sources.

---

## Requirements Traced to QUALITY_GATE.md (Vol 4)

| Req | Source | Covered by |
|-----|--------|-----------|
| Honest error reporting for all particle masses (GitHub #2) | Vol 4 CLAUDE.md, WRITING_PROMPT.md §Gaps | App B §B.4–B.6 |
| Spin-1/2 gap acknowledged (GitHub #1) | WRITING_PROMPT.md | App B §B.10, Problem P4.10.4 |
| Weak/CP gap stated (GitHub #3) | WRITING_PROMPT.md | App B §B.7, App C §C.5 note |
| Higgs gap (GitHub #25) | WRITING_PROMPT.md | App B §B.6 Higgs row |
| Running couplings precision (GitHub #26) | WRITING_PROMPT.md | App B §B.8 |
| Problem sets reference only Vols 1–4 | Vol 4 WRITING_PROMPT Continuity Checklist | Problem sets |
| 200+ bibliography entries | User instruction | Bibliography |
| Feynman rules compiled | User instruction | App C |
| Consistency with Vol 3 App A format | Vol 3 back matter | App A |

---

## Prerequisites (What the Reader Already Has)

- Full working knowledge of Vols 1–3 (classical mechanics, E&M, gauge theory, statistical mechanics)
- Vol 4 Chapters 1–14 read in sequence (problem sets never forward-reference)
- Vol 1 Appendix B (Notation Reference) — we reuse its symbol tables, do not redefine

---

## "Why" Chain the Back Matter Answers

- **Why Appendix A?** Vol 4 cites hundreds of Vol 1–3 equations; the reader must be able to find the antecedent without scrolling across four books.
- **Why Appendix B with honest errors?** The 1000× mass problem (GitHub #2) is a real, open defect. Hiding it destroys credibility; displaying it with the same care as the 0.01% W/Z predictions *is* the scientific stance of the series.
- **Why Appendix C?** Ch 7 introduces Feynman rules in context; Ch 10–14 use them repeatedly. A compiled single-page reference is standard for any QFT textbook and essential for the problem sets.
- **Why 14 problem sets?** Foundations rule: every chapter gets computational / conceptual / challenge problems. Nothing reinforces a derivation like reproducing it.
- **Why 200+ references?** The standard-model literature is vast. Anything less signals we haven't done our homework.

---

## Figure & Table Plan

This is a back-matter deliverable; figures are sparse but tables are dense.

| ID | Placement | Type | What it shows |
|----|-----------|------|---------------|
| Tbl 4.A.1 | App A §A.2 | Table | Vol 1 results used in Vol 4, by chapter |
| Tbl 4.A.2 | App A §A.3 | Table | Vol 2 results used in Vol 4, by chapter |
| Tbl 4.A.3 | App A §A.4 | Table | Vol 3 results used in Vol 4, by chapter |
| Tbl 4.A.4 | App A §A.5 | Table | Reverse index: Vol 4 chapter → prior-volume equations cited |
| Tbl 4.B.1 | App B §B.1 | Table | Fundamental constants relevant to quantum physics |
| Tbl 4.B.2 | App B §B.2 | Table | Atomic & nuclear scales |
| Tbl 4.B.3 | App B §B.3 | Table | QED precision observables (g−2, Lamb shift, α running) |
| Tbl 4.B.4 | App B §B.4 | Table | **Charged leptons — predicted vs. measured** |
| Tbl 4.B.5 | App B §B.5 | Table | **Quarks — predicted vs. measured (running MS-bar at 2 GeV)** |
| Tbl 4.B.6 | App B §B.6 | Table | **Gauge bosons & Higgs — predicted vs. measured** |
| Tbl 4.B.7 | App B §B.7 | Table | **Composite hadrons — status of calculation** |
| Tbl 4.B.8 | App B §B.8 | Table | **Neutrinos — predicted mass scale vs. upper limits** |
| Tbl 4.B.9 | App B §B.9 | Table | **CKM / PMNS mixing angles** |
| Tbl 4.B.10 | App B §B.10 | Table | **Headline honesty table: every SM parameter, error class, status** |
| Tbl 4.C.1 | App C §C.2 | Table | Propagators |
| Tbl 4.C.2 | App C §C.3 | Table | QED vertices |
| Tbl 4.C.3 | App C §C.4 | Table | QCD vertices |
| Tbl 4.C.4 | App C §C.5 | Table | Electroweak vertices |
| Tbl 4.C.5 | App C §C.6 | Table | External-line factors |
| Tbl 4.C.6 | App C §C.7 | Table | Loop rules & symmetry factors |

No pictorial figures in the back matter; every visual is a table.

---

## Appendix A: Key Results from Volumes 1–3

**Structure (mirrors Vol 3 App A):**

- §A.1 How to use this appendix — tag notation, orphan-check principle
- §A.2 Volume 1 results used in Vol 4 — grouped by Vol 1 chapter (Ch 5 Firmament, Ch 6 Waters, Ch 9 Patterns, Ch 10 Quantization, Ch 11 Thermodynamics)
- §A.3 Volume 2 results used in Vol 4 — Ch 3 EM → QED, Ch 4 Strong/Weak, Ch 5 Lagrangian → QFT, Ch 6 Gauge theory, Ch 10 Running couplings
- §A.4 Volume 3 results used in Vol 4 — classical limits, matter formation, quantum statistics
- §A.5 Reverse index — Vol 4 chapter → list of prior equations cited
- §A.6 Orphan check — every listed equation appears in the reverse index

Each equation row: equation number (boxed), full formula, one-line gloss, list of Vol 4 chapters that cite it.

---

## Appendix B: Particle Data Tables

**Structure:**

- §B.0 How to read these tables (status classes: RIGOROUS / APPROXIMATE / PHENOMENOLOGICAL / OPEN)
- §B.1 Fundamental constants (ℏ, c, e, α, α_s, G_F, sin²θ_W, Λ_QCD, v)
- §B.2 Atomic & nuclear scales (Rydberg, Bohr radius, Compton wavelengths)
- §B.3 QED precision tests (electron g−2 to 12 digits, muon g−2, Lamb shift, α(0), α(M_Z))
- §B.4 Charged leptons with mass, prediction, fractional error, status
- §B.5 Quarks (all six, running masses)
- §B.6 Gauge bosons + Higgs
- §B.7 Hadrons (proton, neutron, pions, kaons, selected baryons)
- §B.8 Neutrinos (masses, oscillation parameters, mass-ordering status)
- §B.9 CKM and PMNS matrices
- §B.10 **Headline honesty table** — every SM parameter, its status, fractional error, and GitHub blocker reference

**Critical requirement:** §B.4 must show electron as CALIBRATION (not a prediction), and must flag lepton *ratios* as the prediction, not absolute masses. §B.5 must list light quarks with their true scheme-dependent uncertainty (not 1%, which would be dishonest). §B.8 must state that the prompt's invoked "1000× error" regime lives here — neutrino absolute masses are currently predicted only by order-of-magnitude suppression arguments; any attempt to compute absolute values from the current membrane model is off by ~10³ or worse. The table must say so.

---

## Appendix C: Feynman Rules for Zone Architecture

**Structure:**

- §C.1 Preliminaries (conventions: metric signature, natural units, momentum flow, fermion arrow direction)
- §C.2 Propagators (scalar, Dirac fermion, massive vector, massless photon, gluon)
- §C.3 QED vertices (electron-photon; also scalar-photon if charged scalars appear)
- §C.4 QCD vertices (quark-gluon, 3-gluon, 4-gluon, ghost-gluon in covariant gauges)
- §C.5 Electroweak vertices (W-fermion charged-current with CKM, Z-fermion neutral-current, photon-fermion, Higgs-fermion Yukawa, triple & quartic gauge couplings)
- §C.6 External-line factors (spinors u, v, polarization vectors ε)
- §C.7 Loop rules (integration measure, Feynman parameters, dimensional regularization, fermion-loop sign, symmetry factors)
- §C.8 Zone-architecture modifications (what differs from standard QFT rules — a single boxed note pointing to Ch 7 §7.6 and Ch 8 renormalization scheme)

Every vertex factor boxed; every entry cites the equation in Chapters 6–12 where it was derived.

---

## Problem Sets — Structure

One section per chapter (14 sections). Each chapter:

- 3–5 problems
- Difficulty tiers: ★ basic / ★★ intermediate / ★★★ challenge
- Mix: ≥1 computational, ≥1 conceptual, ≥1 that forces the reader to retrace a derivation or check a limit
- Selected solutions: one problem per chapter fully worked, typically the ★★ or ★★★ problem
- Number format: `P4.Ch.N` (e.g., P4.7.3 = Vol 4, Ch 7, problem 3)

Estimated: ~55 problems total. Forward-references forbidden — Ch N problems may only use Ch 1..N material plus Vols 1–3.

---

## Bibliography — Plan

Target: **≥200 entries**, organized in sections parallel to Vols 2–3 bibliography:

- R.1 Foundational / historical QM & QFT papers (Planck, Einstein, Bohr, Heisenberg, Schrödinger, Dirac, Born, Pauli, von Neumann, Feynman, Tomonaga, Schwinger, Dyson, Yang-Mills, Goldstone, Higgs, Englert-Brout, Weinberg, Salam, Glashow, 't Hooft, Veltman, Gross-Politzer-Wilczek, etc.) — ~40 entries
- R.2 Classical QM & QFT textbooks (Dirac, Messiah, Sakurai, Griffiths, Shankar, Cohen-Tannoudji, Ballentine, Peskin-Schroeder, Weinberg I–III, Srednicki, Schwartz, Zee, Itzykson-Zuber, Ryder, Mandl-Shaw, Bjorken-Drell, Collins, Georgi) — ~30 entries
- R.3 Particle-physics / Standard-Model references (Halzen-Martin, Griffiths Particles, Cheng-Li, Kane, Langacker, Donoghue-Golowich-Holstein, Branco-Lavoura-Silva, Commins-Bucksbaum, Pokorski) — ~20 entries
- R.4 Experimental particle physics (PDG Review 2024, ATLAS/CMS measurements, LHCb, BaBar, Belle/Belle II, muon g−2 E989, electron g−2 Gabrielse/Fan, Lamb shift Lundeen, CODATA 2022, Super-K/KamLAND/SNO/Daya Bay/T2K/NOvA neutrino) — ~30 entries
- R.5 Bell-test & foundations of QM (Bell 1964, CHSH 1969, Aspect 1981/1982, Weihs 1998, Rowe 2001, Hensen 2015, Giustina 2015, Shalm 2015; decoherence: Zurek, Joos, Zeh; measurement: Wheeler, Everett, Ghirardi-Rimini-Weber) — ~20 entries
- R.6 Renormalization, RG, non-perturbative QFT (Wilson, Kadanoff, Polchinski, 't Hooft, Witten, Seiberg) — ~15 entries
- R.7 Lattice QCD & hadron physics (Wilson 1974, Creutz, Kogut-Susskind, recent FLAG averages) — ~10 entries
- R.8 Neutrino physics & CKM (Pontecorvo, Maki-Nakagawa-Sakata, Cabibbo, Kobayashi-Maskawa; oscillation reviews; 0νββ bounds) — ~15 entries
- R.9 Beyond the Standard Model (Susy reviews, extra dimensions, grand unification, proton decay limits) — ~10 entries
- R.10 Zone-architecture internal sources (Vol 1, Vol 2, Vol 3 volumes; research files: `05-QM_FROM_MEMBRANE_DYNAMICS.md`, `05-QED_PRECISION_CALCULATIONS.md`, `06-PARTICLE_MASS_SPECTRUM_V3.md`, `06-QCD_DERIVATION.md`, `06-HIGGS_DERIVATION.md`, `06-NEUTRINO_PHYSICS.md`, `06-WEAK_PARITY_CP_VIOLATION.md`, `TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md`, `SOLVE_1000X_MASS_PROBLEM.md`, etc.) — ~15 entries

Total target: ~205 entries, comfortably above 200. Citation format identical to Vol 3 bibliography (Chicago author-year, numbered within each section).

---

## Verification Criteria

- [ ] Every equation in App A §A.2–A.4 appears in §A.5 reverse index (orphan check)
- [ ] Every particle in the PDG Standard Model summary appears in App B (no silent omissions)
- [ ] Every Vol 4 chapter (1–14) has ≥3 problems
- [ ] Bibliography ≥ 200 entries, sections balanced per plan
- [ ] No forward references in problem sets
- [ ] "1000× error" regime explicitly labeled in App B §B.8 and §B.10
- [ ] Spin-1/2 fermion gap flagged (App B §B.4 note, App C §C.1 note)
- [ ] Feynman rules cross-cite Ch 6–12 equation numbers

---

*Phase 1 + Phase 2 complete. Phase 3 (draft) begins in the five component files in this folder.*
