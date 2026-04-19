# Back Matter Spec — Foundations Vol 2: Forces and Fields

**Date:** April 7, 2026
**Status:** SPEC COMPLETE
**Author:** Jeff Raymond (via Claude)

---

## Overview

The Vol 2 back matter comprises four components that serve distinct pedagogical and reference functions:

1. **Appendix A: Vector Calculus and Tensor Analysis Review** — Mathematical toolkit for the volume
2. **Appendix B: Experimental Data Tables** — Every number cited or predicted, with sources
3. **Problem Sets with Selected Solutions (Ch 1–11)** — Exercises spanning the full difficulty range
4. **Bibliography** — 150+ references spanning foundational papers, textbooks, and modern experiments

---

## Component Requirements

### Appendix A: Vector Calculus and Tensor Analysis Review

| Req ID | Requirement | Acceptance Criteria |
|--------|------------|-------------------|
| BM-A01 | Cover all vector calculus used in Vol 2 | Gradient, divergence, curl, Laplacian, Stokes/Gauss theorems |
| BM-A02 | Cover tensor analysis through rank-2 | Index notation, raising/lowering, covariant derivative, Christoffel symbols |
| BM-A03 | Cover differential forms used in Vol 2 | Exterior derivative, Hodge star, wedge product — as used in Maxwell derivation |
| BM-A04 | Cover Kaluza-Klein reduction math | Extra-dimensional integration, warp factors, dimensional reduction technique |
| BM-A05 | Match Vol 1 Appendix B notation exactly | Every symbol, convention, index range must be consistent |
| BM-A06 | No new physics — math review only | Appendix A teaches math tools, not physics results |

### Appendix B: Experimental Data Tables

| Req ID | Requirement | Acceptance Criteria |
|--------|------------|-------------------|
| BM-B01 | Tabulate ALL coupling constants | G₄, α, α_s, α_w, sin²θ_W — zone-derived and measured values with errors |
| BM-B02 | Tabulate ALL force measurements | Newton's constant experiments, Gravity Probe B, LIGO, PSR B1913+16 |
| BM-B03 | Every number cites its source | PDG year, CODATA year, LIGO collaboration paper, etc. |
| BM-B04 | Include zone-derived vs. measured comparison | Side-by-side: zone prediction, experimental value, percentage agreement |
| BM-B05 | Tabulate running coupling data | α_i^{-1}(Q) at decade energy intervals from 1 GeV to 10^{16} GeV |
| BM-B06 | Include cosmological parameters | Ω_Λ, Ω_DM, Ω_b, H₀, w — zone vs. Planck 2018 |
| BM-B07 | Include membrane parameters | σ, μ, ξ_A, η_B, L_eff, λ, γ — values and uncertainties |
| BM-B08 | Include GR observable tests | Mercury precession, light deflection, Shapiro delay, frame-dragging, GW strain |

### Problem Sets

| Req ID | Requirement | Acceptance Criteria |
|--------|------------|-------------------|
| BM-P01 | 3–5 problems per chapter (33–55 total) | Spanning computational, conceptual, and challenge difficulty |
| BM-P02 | Selected solutions provided | At least 1 worked solution per chapter |
| BM-P03 | No forward references | Problems use only Vol 1 + Vol 2 (Ch 1–11) material |
| BM-P04 | Cover all key derivations | At least one problem per major derivation result |
| BM-P05 | Include "explain why" problems | Not just computation — test understanding of WHY |
| BM-P06 | Challenge problems push boundaries | At least 3 challenge problems that extend the derivations |

### Bibliography

| Req ID | Requirement | Acceptance Criteria |
|--------|------------|-------------------|
| BM-R01 | 150+ references | Spanning foundational, modern experimental, and textbook sources |
| BM-R02 | Organized by category | Foundational Papers, Textbooks, Modern Experiments, Zone-Specific |
| BM-R03 | Complete citation format | Author(s), Title, Journal/Publisher, Year, DOI where available |
| BM-R04 | Every in-text citation appears | Cross-check against all 11 chapters |

---

## Prerequisites

- All 11 Vol 2 chapter drafts (VERIFIED or in progress)
- Vol 1 Appendix B (Notation Reference) — canonical authority
- Quality_Control/Reference/Symbol_and_Constants.md

---

## Verification Criteria

- [ ] All notation matches Vol 1 Appendix B exactly
- [ ] New Vol 2 symbols listed as additions to the notation system
- [ ] Every experimental value in Appendix B cites its source
- [ ] Problem sets reference only Vol 1 + Vol 2 material
- [ ] Bibliography contains 150+ entries
- [ ] No forward references to Vol 3+
- [ ] All 9 assigned reviewers pass
