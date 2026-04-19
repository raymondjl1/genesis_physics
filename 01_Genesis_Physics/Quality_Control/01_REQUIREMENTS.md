# Genesis Physics Series — Derived Requirements

**Date:** April 5, 2026
**Derived from:** 00_SERIES_VISION.md (governing principles), manuscript analyses (01-04), consistency audits
**Status:** Living document — update as requirements are met or new ones discovered

---

## How to Read This Document

This is the requirements specification for the Genesis Physics Series. Think of it like a software requirements doc: each requirement has an ID, a rationale ("why"), acceptance criteria (how we know it's done), and a priority. Requirements are organized by category, not by book — because the bottom-up build order means most requirements must be met in the Foundations Series before they cascade into other books.

**Requirement states:**
- **OPEN** — Not yet met
- **IN PROGRESS** — Work underway
- **MET** — Satisfied, with evidence
- **DEFERRED** — Deliberately postponed with rationale
- **N/A** — No longer applicable (with explanation)

---

## Category 1: The "Always Answer Why" Requirements

*Derived from: Governing Principle #1, Jeff's core philosophy, reader experience goals*

These are the most important requirements in the entire document. If we fail here, we've failed the whole project.

| ID | Requirement | Why | Acceptance Criteria | Priority | Status |
|----|------------|-----|-------------------|----------|--------|
| WHY-001 | Every physics law introduced must include its derivation from zone architecture axioms | Standard physics presents laws as empirical. Our series must show WHY each law exists. | Reviewer cannot find a single law statement without a preceding or accompanying derivation tracing to Volume 1 axioms. | **P0** | OPEN |
| WHY-002 | No "it can be shown that" or "it is well known that" without a citation to where it IS shown | Hand-waving disguised as rigor. | Grep for these phrases across all manuscripts. Zero hits without an accompanying reference. | **P0** | OPEN |
| WHY-003 | Every mathematical result must be preceded by the physical intuition for WHY it should be true | Math without intuition is just symbol manipulation. The reader should predict the result before seeing it. | Each derivation has a "Physical Intuition" paragraph before the formal math. | **P1** | OPEN |
| WHY-004 | Concepts must build cumulatively — no concept used before it's been established | Forward references destroy the "why" chain. | Dependency graph of concepts shows no forward references (every concept's prerequisites appear in earlier chapters/volumes). | **P0** | OPEN |
| WHY-005 | Each Foundations volume opens with "What you already know" and "What we'll derive and why" | Reader orientation. They need to know where they are in the journey. | Every volume Ch.1 has these sections. | **P1** | OPEN |
| WHY-006 | The Creator's Blueprint must answer "why" through scripture FIRST, then physics confirmation | Different audience, same principle. The "why" for this audience is "because God designed it this way." | Every The Creator's Blueprint chapter begins with scripture, then shows physics alignment. | **P1** | OPEN |
| WHY-007 | Problem sets must include "explain why" questions, not just "calculate" | Calculation without understanding is what we're replacing. | At least 30% of problems in each volume are qualitative "explain why" problems. | **P1** | OPEN |

---

## Category 2: Mathematical Rigor Requirements

*Derived from: 04_Mathematical_Framework_Analysis.md, 01_Scientific_Rigor_Analysis.md*

| ID | Requirement | Why | Acceptance Criteria | Priority | Status |
|----|------------|-----|-------------------|----------|--------|
| MATH-001 | Foundations Series rigor target: 70% rigorous / 20% formal / 10% semi-formal | Current manuscript is 10/15/75 (inverted). Framework cannot be taken seriously without rigorous math. | Independent reviewer classifies each derivation. Ratios meet target. | **P0** | OPEN |
| MATH-002 | The fine structure constant derivation must be complete end-to-end from axioms | Currently the coefficient 1.44 is empirically fitted, not derived. The crown jewel must be fully derived. | Complete derivation chain from Volume 1 axioms to α⁻¹ ≈ 137.036 with no fitted parameters. | **P0** | OPEN |
| MATH-003 | Maxwell's equations must be derived from Firmament wave propagation | Currently missing entirely. A framework claiming to unify physics cannot skip electromagnetism. | Full derivation in Foundations Vol 2. All four Maxwell equations recovered. Speed of light emerges as membrane property. | **P0** | OPEN |
| MATH-004 | Particle mass spectrum must be derived from membrane resonance modes | Currently missing. No particle masses calculated. | At least electron, proton, and neutron masses derived with <5% error. Full Standard Model spectrum attempted with error bars. | **P0** | OPEN |
| MATH-005 | The membrane tension calculation error must be resolved | 76-order-of-magnitude discrepancy flagged as "FATAL" in own critic document. Partially resolved April 4, 2026. | Single canonical value of σ with complete derivation. No internal contradictions. Verified against c² = σ/μ. | **P0** | IN PROGRESS |
| MATH-006 | Waters field equations must be specified | Currently undefined. "Waters" is named but has no governing PDEs. | Navier-Stokes-like field equations for Waters Above and Below. Boundary conditions. Equilibrium solutions. Perturbation theory. | **P0** | OPEN |
| MATH-007 | Replenishment model must include thermodynamic proof | Energy extraction depends on Waters replenishment with no rate equation. Vulnerable to perpetual motion critique. | Complete thermodynamic cycle. Rate equations. Equilibrium analysis. Explicitly addresses Second Law concerns. | **P0** | OPEN |
| MATH-008 | All four forces must be derived from membrane geometry with numerical predictions | Chapters 10-12 are stubs (1000-1500 words each). Central claims unsubstantiated. | Each force: derivation from geometry, predicted coupling strength, comparison with measured value, falsification threshold. | **P0** | OPEN |
| MATH-009 | Conservation laws must be derived via Noether's theorem on the zone manifold | Currently outlined but not derived. | Each conservation law mapped to a specific zone symmetry. Complete Noether derivation. Anomalies identified. | **P0** | OPEN |
| MATH-010 | Einstein field equations must be recovered from 6D embedding | Gravity claims must match Einstein's predictions or show testable differences. | EFE derived. Schwarzschild solution recovered. Weak-field tests (perihelion, deflection, time delay) calculated. | **P0** | OPEN |
| MATH-011 | Schrödinger equation must be derived from membrane dynamics | QM is "shut up and calculate" — our framework must show WHY the Schrödinger equation has the form it does. | Derivation from Firmament vibration modes. Born rule justified. Uncertainty principle derived geometrically. | **P0** | OPEN |
| MATH-012 | Notation must be consistent across all six volumes | Current notation shifts between sections. | Notation guide in Volume 1 Appendix. All volumes cross-checked. Symbol audit shows zero conflicts. | **P1** | OPEN |
| MATH-013 | Every numerical prediction must include error bars and comparison with experiment | Claims without error bars are assertions, not predictions. | Every derived constant has: predicted value ± uncertainty, measured value ± uncertainty, percent error, source of experimental data. | **P0** | OPEN |
| MATH-014 | At least one numerical simulation must validate each major prediction | Zero computational verification currently exists. | Simulation code in GitHub repo. Reproducible results. Comparison with analytical predictions. | **P1** | OPEN |

---

## Category 3: Structural & Writing Requirements

*Derived from: 02_Readability_Writing_Analysis.md, 03_Structural_Gaps_Analysis.md, Governing Principles*

| ID | Requirement | Why | Acceptance Criteria | Priority | Status |
|----|------------|-----|-------------------|----------|--------|
| STRUCT-001 | Each product must have exactly ONE audience and ONE voice | The original manuscript's identity crisis. Multiple audiences = no audience. | Voice audit: each product reads as a single, consistent voice throughout. No technical jarring in Book 2. No devotional jarring in Foundations. | **P0** | OPEN |
| STRUCT-002 | Foundations volumes must be usable as standalone course textbooks | This is a textbook series, not just a reference. Must be teachable. | Each volume: learning objectives, worked examples, problem sets with selected solutions, logical progression suitable for a 2-semester course. | **P0** | OPEN |
| STRUCT-003 | Book 2 must contain zero equations | Different audiences need different tools. Equations in Book 2 would lose the lay reader. | Manuscript search: zero mathematical equations. Concepts explained via analogy and metaphor only. | **P0** | OPEN |
| STRUCT-004 | The Creator's Blueprint must include direct scripture quotation in every chapter | This is the scripture-first product. The Bible leads, physics follows. | Every chapter: at minimum 5 direct scripture quotations with book/chapter/verse citations. | **P0** | OPEN |
| STRUCT-005 | The Creator's Blueprint must include discussion questions, activities, and "But What About?" sections | Homeschool families need teaching tools, not just content. | Every chapter: 5+ discussion questions, 1+ family activity, 1 "But What About?" section addressing common objections. | **P1** | OPEN |
| STRUCT-006 | Cross-references between products must be specific (title + chapter) | Vague "see the other book" is unhelpful. | Every cross-reference includes product title and chapter number. Pattern: "For the full derivation, see *Foundations Vol. 2*, Chapter 3." | **P1** | OPEN |
| STRUCT-007 | Each book/volume must have a comprehensive bibliography | Current manuscript has no bibliography. Unverifiable claims. | Foundations: 100+ references per volume. Book 1: 200+ total. Book 2: Further Reading guide. The Creator's Blueprint: Scripture Index. | **P1** | OPEN |
| STRUCT-008 | Professional diagrams must accompany all geometric and architectural concepts | Complex geometric concepts (6D embedding, zone hierarchy, membrane structure) cannot be understood from text alone. | Book 2: 15-20 illustrations. Book 1: 30-40 diagrams. Foundations: technical figures throughout. The Creator's Blueprint: simplified visuals. | **P1** | OPEN |
| STRUCT-009 | Writing must pass readability tests appropriate to each product's audience | Readability analysis showed uneven quality. | Book 2: Flesch-Kincaid Grade 10-12. Book 1: Grade 14-16. Foundations: Graduate level. The Creator's Blueprint: Grade 9-12. | **P1** | OPEN |
| STRUCT-010 | Amazon KDP formatting requirements must be met for all products | Self-publishing. Must look professional. | Each product: proper front matter (title page, copyright, ToC), back matter (index, bibliography), KDP-compliant trim size, ISBN, professional cover. | **P1** | OPEN |
| STRUCT-011 | Audiobook-targeted products (Book 2, The Creator's Blueprint) must work as spoken word | Audio listeners can't see equations or diagrams. | Book 2 and The Creator's Blueprint: no content that requires visual reference. Diagrams described in text. Companion PDF for visual elements. | **P1** | OPEN |

---

## Category 4: Consistency Requirements

*Derived from: Consistency_00_MASTER_REPORT.md, Consistency_01-03 audits*

| ID | Requirement | Why | Acceptance Criteria | Priority | Status |
|----|------------|-----|-------------------|----------|--------|
| CON-001 | Zone numbering must use a single canonical scheme across all products | Currently inconsistent: detailed nested scheme (Zone 2.2.1) vs. simplified (Zone 1/2/3/4). | One scheme defined in Series Bible. All products use it. | **P1** | OPEN |
| CON-002 | The Five Governing Principles must have a canonical naming, ordering, and definition | Varies across files. Some use "Hierarchy," some "Symmetry." Different orderings. | Single canonical list in Series Bible with divine attribute mapping. All products reference it. | **P1** | IN PROGRESS |
| CON-003 | Hebrew transliteration must be standardized | "Raqia" vs "raqia" vs "Raqia'" — inconsistent. | Transliteration standard in Series Bible. Applied consistently. | **P2** | OPEN |
| CON-004 | Firmament terminology must be standardized to "membrane" | Called "membrane," "boundary," "expanse," and "barrier" in different places. | "Membrane" canonical per Style Guide. Other terms used only in defined contexts (e.g., "expanse" when quoting traditional Bible translations). | **P2** | OPEN |
| CON-005 | Dark matter/energy pairings must always be stated | Style Guide requires "Waters Above (dark energy)" etc. Many chapters omit the pairing. | First occurrence in each chapter uses the full pairing. Subsequent uses can use either term alone. | **P2** | OPEN |
| CON-006 | Zone boundary breach conditions must be defined | Black holes, FTL, and consciousness chapters each imply different rules for zone crossing. | Single canonical set of boundary conditions in Foundations Vol 1. All other products consistent with it. | **P1** | OPEN |
| CON-007 | Matter formation timeline must reconcile "progressive gathering" with "mature creation" | Ch09 describes progressive gathering. Cosmology chapters invoke instantaneous mature creation. Contradictory. | Explicit reconciliation paragraph. Both mechanisms explained in their proper contexts. | **P1** | OPEN |
| CON-008 | FTL mechanisms must be formally derived from axioms, not listed as add-ons | Five FTL mechanisms described conceptually but never derived. Read as speculation. | Each mechanism derived from zone architecture axioms in Foundations. Energy requirements calculated. | **P1** | OPEN |
| CON-009 | The 68/27/5 split must be consistently cited with the same observational source | Core claim. Must always reference the same dataset (Planck 2018 or equivalent). | Single canonical source. Cited consistently. | **P2** | OPEN |

---

## Category 5: Publishing & Production Requirements

*Derived from: Self-publishing strategy (Amazon KDP/ACX)*

| ID | Requirement | Why | Acceptance Criteria | Priority | Status |
|----|------------|-----|-------------------|----------|--------|
| PUB-001 | All products must be formatted for Amazon KDP (Kindle + print) | Self-publishing on Amazon is the distribution strategy. | KDP-compliant files: .epub/.mobi for Kindle, print-ready PDF for paperback/hardcover. Correct trim sizes. | **P1** | OPEN |
| PUB-002 | Book 2 and The Creator's Blueprint must have Audible audiobook versions | Audiobook is a key format for these audiences. | ACX-compliant audio files. Professional narration (either AI or human narrator). Chapter markers. | **P1** | OPEN |
| PUB-003 | Each product must have a professional cover design | Self-published books are judged by their covers. Amazon browsers make decisions in 2 seconds. | Professional designer hired. Covers meet KDP specs. Series visual identity consistent across all products. | **P1** | OPEN |
| PUB-004 | Each product must have a unique ISBN | Required for professional publishing. | ISBNs purchased (Bowker). One per format per product. | **P1** | OPEN |
| PUB-005 | Professional copyedit before publication | Self-published ≠ unedited. | Each product professionally copyedited. Zero typos in first 50 pages (Amazon "Look Inside" preview). | **P1** | OPEN |
| PUB-006 | Professional interior formatting | Looks matter for credibility, especially for academic content. | Consistent typography, headers, margins. Equations properly typeset (LaTeX or equivalent). Print and ebook versions both look professional. | **P1** | OPEN |
| PUB-007 | Amazon categories and keywords optimized for discoverability | Self-publishing requires SEO thinking. | 2 BISAC categories per product. 7 backend keywords per product. A+ Content (Enhanced Brand Content) for product pages. | **P2** | OPEN |
| PUB-008 | Pre-launch email list of 500+ subscribers before Book 2 publication | Amazon algorithm rewards launch velocity. First-week sales matter. | Email list built via website, YouTube, church networks, physics blogs. 500+ subscribers at Book 2 launch. | **P2** | OPEN |

---

## Traceability Matrix

Every requirement traces back to either a Governing Principle or a finding from the manuscript analyses:

| Source | Requirements Derived |
|--------|---------------------|
| **Governing Principle: Always Answer Why** | WHY-001 through WHY-007 |
| **Governing Principle: Build Bottom-Up** | WHY-004, STRUCT-002 |
| **Governing Principle: No Rewrites** | (Build order — enforced by process, not requirements) |
| **Governing Principle: Honest About Limits** | MATH-013, WHY-002 |
| **Governing Principle: Scripture + Physics** | STRUCT-004, WHY-006 |
| **Governing Principle: One Voice Per Product** | STRUCT-001, STRUCT-003 |
| **Governing Principle: Accessibility** | STRUCT-009, STRUCT-011 |
| **01_Scientific_Rigor_Analysis.md** | MATH-002, MATH-005, MATH-006, MATH-007, MATH-008, MATH-013 |
| **02_Readability_Writing_Analysis.md** | STRUCT-001, STRUCT-009, WHY-003 |
| **03_Structural_Gaps_Analysis.md** | MATH-003, MATH-004, MATH-008, MATH-010, MATH-011, STRUCT-007, STRUCT-008 |
| **04_Mathematical_Framework_Analysis.md** | MATH-001, MATH-012, MATH-014 |
| **Consistency_00_MASTER_REPORT.md** | CON-001 through CON-009 |
| **Self-publishing decision (April 5, 2026)** | PUB-001 through PUB-008 |

---

## Open Issues / Gaps Identified

These are issues surfaced during requirements derivation that don't fit neatly into existing categories:

| # | Issue | Notes |
|---|-------|-------|
| GAP-001 | **No Book 0 folder structure for 6 volumes yet** | The Book_0_The_Foundations/ folder exists but isn't subdivided into six volume folders. Need to create Vol_1/ through Vol_6/ with Manuscript/ and Source_Reference/ subdirectories. |
| GAP-002 | **No The Creator's Blueprint folder exists** | Need to create a Book_3_The_Creators_Blueprint/ folder with the same structure as the other books. |
| GAP-003 | **Series Bible needs major update** | Style Guide was written for the monolithic manuscript. Needs updating for the series structure, six volumes, and The Creator's Blueprint. |
| GAP-004 | **No LaTeX or typesetting pipeline** | For the Foundations Series, equations must be professionally typeset. Need to decide on toolchain (LaTeX, Overleaf, Scrivener → InDesign, etc.). |
| GAP-005 | **No audiobook strategy for math-heavy content** | Book 1 has equations. Foundations Series is all equations. How do we handle audio for these? Or do we not? (Current plan: audio only for Book 2 + The Creator's Blueprint.) |
| GAP-006 | **No cover design brief** | Need a visual identity for the series before going to a designer. |
| GAP-007 | **No "reader journey" map** | Need a document showing the expected reader path through the series and what they know at each stage. Ensures WHY-004 (no forward references). |
| GAP-008 | **Biology/Abiogenesis not addressed** | The framework claims to explain creation but doesn't address the origin of life. Is this in scope or explicitly deferred? |
| GAP-009 | **No peer review strategy document** | Academic papers need to be extracted and submitted. No plan for which papers, which journals, or timeline. |
| GAP-010 | **Existing Book 2/2/3 README and STATUS files reference old 3-book structure** | Need to update individual book README.md and STATUS.md files to reflect the new series structure. |

---

*Requirements are derived from the Vision (00_SERIES_VISION.md) and validated against the manuscript analyses (01-04) and consistency audits. This document should be reviewed whenever new work is started to ensure requirements are being met.*
