# Back Matter Spec — Foundations Vol 3: Matter and Motion

**Date:** April 7, 2026
**Status:** SPEC COMPLETE
**Author:** Jeff Raymond (via Claude)
**Lifecycle Phase:** 1 — Spec

---

## Overview

The Vol 3 back matter comprises four components, each with a distinct pedagogical and reference function:

1. **Appendix A: Key Results from Volumes 1–2** — A concise but complete reference of every Vol 1 and Vol 2 equation cited anywhere in Vol 3. The student should be able to look up any referenced result without flipping back to earlier volumes.
2. **Appendix B: Experimental Mechanics Data** — All experimental data (force measurements, material properties, thermodynamic constants) used or predicted in Vol 3, with sources.
3. **Problem Sets with Selected Solutions (Ch 1–12)** — 3–5 problems per chapter spanning computational, conceptual, and challenge difficulty.
4. **Bibliography** — 100+ references spanning foundational papers, modern experiments, textbooks, and zone-specific sources.

This back matter differs from Vol 2's in one critical respect: **Appendix A is a back-reference, not a math review.** Vol 2's Appendix A was a vector-calculus / tensor toolkit. Vol 3 assumes that toolkit (and Vol 1 Appendix B's notation) and instead collects the specific equations Vol 3 cites, so the student has them at fingertip distance.

---

## Component Requirements

### Appendix A: Key Results from Volumes 1–2

| Req ID | Requirement | Acceptance Criteria |
|--------|------------|-------------------|
| BM-A01 | Every Vol 1 equation cited in Vol 3 must appear | Cross-check against all 12 chapter drafts; no orphan citations |
| BM-A02 | Every Vol 2 equation cited in Vol 3 must appear | Cross-check against all 12 chapter drafts |
| BM-A03 | Each entry must reproduce the full equation, not a placeholder | Student can read off the result without opening Vol 1/2 |
| BM-A04 | Organized by volume → chapter → equation number | Linear lookup by citation tag `(1.Ch.Eq)` or `(2.Ch.Eq)` |
| BM-A05 | Each result carries a one-line "what it says" gloss | Not just the equation — the meaning |
| BM-A06 | Cross-referenced from Vol 3 chapters | Each entry lists which Vol 3 chapters cite it |
| BM-A07 | Notation matches Vol 1 Appendix B exactly | Every symbol consistent |

### Appendix B: Experimental Mechanics Data

| Req ID | Requirement | Acceptance Criteria |
|--------|------------|-------------------|
| BM-B01 | Tabulate all material properties used | Elastic moduli, densities, yield strengths, speeds of sound — Cu, Al, Fe, Diamond, H₂O, air |
| BM-B02 | Tabulate all thermodynamic constants | k_B, N_A, R, σ_SB, c_1, c_2 Planck radiation constants; with CODATA source |
| BM-B03 | Tabulate all kinetic/transport coefficients | Viscosity, thermal conductivity, diffusion for standard gases/liquids at STP |
| BM-B04 | Planck spectrum data | CMB temperature, peak wavelength, u_total — COBE/FIRAS + Planck 2018 |
| BM-B05 | Phase transition data | Critical points (H₂O, CO₂), latent heats, Curie temperatures; electroweak scale |
| BM-B06 | Particle masses used in Ch 6–7 | e, μ, τ, u, d, s, c, b, t, W, Z, Higgs — PDG 2024 |
| BM-B07 | Orbital mechanics data | Planetary semi-major axes, periods, eccentricities — verify Kepler's 3rd law |
| BM-B08 | Zone-derived vs. measured comparison | Side-by-side with % agreement where the framework makes a prediction |
| BM-B09 | Every number cites its source | CODATA year, PDG year, NIST database, COBE/FIRAS paper, etc. |

### Problem Sets

| Req ID | Requirement | Acceptance Criteria |
|--------|------------|-------------------|
| BM-P01 | 4–5 problems per chapter (48–60 total) | Spanning computational, conceptual, and challenge |
| BM-P02 | At least 1 fully worked solution per chapter | Student can trace the reasoning |
| BM-P03 | No forward references | Problems use only Vols 1–3 (Ch 1–12) material |
| BM-P04 | Cover each chapter's major derivations | At least one problem per headline result |
| BM-P05 | Include "explain why" problems | Not just computation |
| BM-P06 | At least 3 challenge problems extending the derivations | Push the framework |
| BM-P07 | **The Student reviewer's priority** | Problems must be genuinely solvable using only the zone framework |

### Bibliography

| Req ID | Requirement | Acceptance Criteria |
|--------|------------|-------------------|
| BM-R01 | 100+ references | Foundational, textbooks, modern experiments, zone-specific |
| BM-R02 | Organized by category | (1) Foundational papers (2) Textbooks (3) Experimental papers (4) Data compilations (5) Zone-specific |
| BM-R03 | Complete citation format | Author(s), Title, Journal/Publisher, Year, DOI where available |
| BM-R04 | Every in-text citation appears | Cross-check against all 12 chapters |

---

## Prerequisites

- All 12 Vol 3 chapter drafts (all present in `Ch_01...Ch_12` folders)
- Vol 1 Appendix B (Notation Reference) — canonical authority
- Vol 1 & Vol 2 complete (as per WRITING_PROMPT.md, assumed)
- Vol 2 Back Matter (as format model)

## Verification Criteria

- [ ] All Vol 1/Vol 2 equations cited in Vol 3 appear in Appendix A
- [ ] All notation matches Vol 1 Appendix B
- [ ] Every number in Appendix B cites its source
- [ ] Problem sets reference only Vols 1–3
- [ ] Bibliography ≥ 100 entries
- [ ] No forward references to Vol 4+
- [ ] All 9 assigned Vol 3 reviewers pass
- [ ] Student reviewer's question — "Can I actually solve these?" — answered YES

---

## Lifecycle Phases

1. **Spec** — this document ✓
2. **Outline** — component layout with figure/table plan
3. **Draft** — Appendix A → Appendix B → Problem Sets → Bibliography
4. **Self-Review** — full pass using Vol 2 Self-Review as model
5. **Reviewer Agents** — 9 reviewer pass
6. **Finalize** — mark VERIFIED and deliver
