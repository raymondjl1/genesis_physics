# REVIEWER-12: The Acquisitions & Production Editor — Vol 6 Review

**Reviewer:** Margaret Holloway (REVIEWER-12)
**Product:** *The Foundations of Genesis Physics*, Volume 6 — *Predictions, Simulations, and Open Problems*
**Scope:** Full volume — 17 chapters, 6 appendices (A–F), Bibliography, Master Index, Volume Preface
**Date:** 2026-05-16
**Method:** Front-matter / back-matter audit first, then bookstore-browse the middle (Ch 1, Ch 9, Ch 17 first pages), then permissions/rights pass, then positioning draft. Word limit: 2,500.

---

## Executive Verdict

**OVERALL: PASS WITH NOTES (acquirable; not yet shippable).**

This is the most acquirable volume in the Foundations Series. The author has done the unusual work of building the artifact a publisher actually wants: a consolidated, numbered prediction catalog (Appendix A, 153 entries); a reproducibility package (Appendix B); a series-wide Master Index whose Navigator spot-checks have already been done; a 400-entry bibliography; a problem set with selected solutions; and a Technology Application Summary that gives the marketing team a discrete inventory to point at. The back-matter scaffold is, frankly, better than what I see from most acquired manuscripts at the same stage.

What it does not yet have, and what blocks the production handoff, is the front-matter that turns a folder of chapters into a book object. There is no title page, no copyright page, no series-level TOC for Vol 6, no list of figures, no list of tables, no figure credit register, no permissions log, no Scripture-translation acknowledgment, no author bio, no endorsement plan, and no jacket copy. These are not nitpicks; they are the difference between something I can walk into editorial board and something I have to send back. **None of them is hard to fix.** All can be drafted in a focused two-week sprint without touching the chapter manuscripts.

Tag distribution: **C1 (must-fix-to-ship):** 6 findings. **C2 (should-fix-pre-galleys):** 7. **C3 (production polish):** 5. **C4 (post-pub / next edition):** 3.

---

## Scorecard

```
STRUCTURAL COMPLETENESS:    [ ] PASS  [X] NOTES  [ ] FAIL
TOC COHERENCE:              [ ] PASS  [X] NOTES  [ ] FAIL
CROSS-REFERENCE INTEGRITY:  [ ] PASS  [X] NOTES  [ ] FAIL
FIGURE/TABLE COMPLETENESS:  [ ] PASS  [X] NOTES  [ ] FAIL
INDEX VALIDITY:             [X] PASS  [ ] NOTES  [ ] FAIL
RIGHTS/PERMISSIONS:         [ ] PASS  [ ] NOTES  [X] FAIL
SCRIPTURE PERMISSIONS:      [ ] PASS  [ ] NOTES  [X] FAIL
MARKETABILITY/POSITIONING:  [X] PASS  [ ] NOTES  [ ] FAIL
FIRST-PAGE HOOK:            [X] PASS  [ ] NOTES  [ ] FAIL
BACK-COVER BLURB WRITABLE:  [X] PASS  [ ] NOTES  [ ] FAIL
PRODUCTION READINESS:       [ ] PASS  [X] NOTES  [ ] FAIL
ACCESSIBILITY:              [ ] PASS  [ ] NOTES  [X] FAIL
METADATA (BISAC/ISBN/etc.): [ ] PASS  [X] NOTES  [ ] FAIL

OVERALL: [ ] PASS  [X] PASS WITH NOTES  [ ] FAIL
```

Two component-level FAILs (Scripture Permissions, Accessibility) and one structural FAIL (Rights/Permissions register). Each is fixable in days. The volume is editorially acquirable today; it is not production-ready today.

---

## 1. Structural Completeness — NOTES

**C1-01 — Missing front matter (BLOCKER for production handoff).** The Vol 6 folder contains `VOLUME_PREFACE.md` and that is the only front-matter element present. A shippable volume needs: half-title; full title page with subtitle, author, and series mark; copyright page (ISBN block, CIP placeholder, translation acknowledgments, permissions block, "Printed in…" line); dedication (optional); epigraph (Genesis 1:6–7 is the obvious candidate, but it must clear translation permissions); the volume-level TOC; List of Figures; List of Tables; List of Predictions (P-001 to P-153 — this is volume-specific and a marketable feature); and the volume preface (already drafted). The preface is good; the rest does not exist as drafted files. Build them.

**C1-02 — No author bio file.** I cannot find an author bio in this volume or at the Book 0 level. The flap copy needs three sentences establishing why Jeff Raymond — aerospace systems engineer — is qualified to publish a graduate physics textbook that derives the fine-structure constant from Genesis 1. The platform must be articulated. Without this, the manuscript dies at acquisition board.

**C1-03 — No "About the Series" page.** A six-volume set needs a series page on the back end of every volume listing all six titles, publication order, and prerequisites. Newcomers must be able to find Vol 1 from Vol 6.

**C2-01 — Series-wide TOC absent.** The Master Index handles concept lookup, but there is no series-wide chapter TOC. For a 2,500-page set, this belongs at the front of every volume.

**C3-01 — Volume Preface is good prose but lives outside any masthead.** Move into the front-matter assembly when the title page is built.

## 2. TOC Coherence — NOTES

**C2-02 — Chapter count drift undisclosed in TOC artifacts.** `QUALITY_GATE.md` notes the volume expanded from 12 to 17 chapters and that the original spec is stale. There is no consolidated, public-facing TOC that reflects the 17-chapter reality with subsection-level navigation. The TOC the reader sees must be the 17-chapter TOC; the 12-chapter spec is internal history and should not surface.

**C2-03 — Part A / Part B / Part C structure (from VOLUME_PREFACE.md) is not surfaced in any TOC.** The most important structural feature of this volume — the epistemic-status partitioning into Validation / Conditional Engineering / Self-Assessment — must appear in the TOC as part headings, not only in the preface. A bookstore browser turning to the TOC must immediately see that Chapters 9–13 carry a different epistemic warranty than Chapters 1–8. Without this, every skeptic review will hammer the volume for "burying" the speculative chapters.

## 3. Cross-Reference Integrity — NOTES

**C2-04 — Known live cross-ref hazards from change log.** The 2026-05-11 change log (QUALITY_GATE.md) discloses three repaired issues: Ch 3 prediction renumber (P-068–P-088 → P-089–P-109; 56 internal references updated); Ch 6 title misnomer ("N-Body" → recommended "Large-Scale Structure"); Ψ_spirit canonicalization across Chs 9, 11, 12, 13. The renumber is the highest-risk. **Recommend a clean automated cross-reference audit pass** — every `P-0[6-8][0-9]` and `P-09[0-9]` mention across all 17 chapters, all 6 appendices, the Master Index, and the Bibliography. The Appendix C reviewer report already flags one likely follow-on issue: problem **P6.C.28 cites V6.Ch9.Eq(6.9.7)**, and Ch 9's three-part draft structure makes that equation number unstable until Ch 9 is finalized into a single file. **C1-04** elevates: collapse Ch 9 from `Ch09_DRAFT_Part1/2/3.md` into a single canonical draft file before any audit, then re-pin equation numbers.

**C2-05 — Title misnomer in Ch 6 still in chapter heading.** The change log says the editorial note was added; the title was not changed. For an acquired manuscript, fix the title — "Large-Scale Structure Simulations" is the recommendation in the change log itself. Production cannot ship a chapter whose title contradicts its contents.

**C3-02 — Multi-version draft files in Ch 9 folder.** `Ch09_DRAFT.md`, `Ch09_DRAFT_Part1.md`, `Ch09_DRAFT_Part2.md`, `Ch09_DRAFT_Part3.md` all coexist. Production typesetting needs one canonical file per chapter. Archive the part files when consolidation is complete.

## 4. Figure & Table Completeness — NOTES

**C1-05 — Figures are inline placeholders, not assets.** I sampled Ch 1, where Figure 6.1.1 appears as a bracketed `[FIGURE: Fig 6.1.1 — Zone Architecture Prediction Pipeline: Axioms → … flowchart …]` placeholder. There is no figures folder, no SVG/PNG file, no resolution information, and no credit line. A graduate textbook with no real figure assets is not a producible manuscript. Build the figure pipeline now: vector source files (preferred), 300 DPI PNG fallbacks, grayscale-legible by spec, alt-text recorded in a sidecar manifest. Until figures exist as files, the production team has nothing to typeset.

**C2-06 — No List of Tables exists.** Tables 8.3 and similar are referenced in the change log; there is no consolidated list. Generate from final manuscript.

**C2-07 — No List of Predictions (front matter).** Strongly recommend adding. The 153 predictions are this volume's hook; surfacing the list itself in the front matter is good marketing and good navigation. Appendix A is the master; the LoP is a teaser pointer.

## 5. Index Validity — PASS

**Commendation.** The Master Index (`Back_Matter/Master_Index.md`, 12,214 words) is the strongest single back-matter asset I have seen on this project. The Navigator spot-check protocol (5 of 5 documented in STATUS.md, including the in-session correction on "fine-structure constant" hyphenation) is publication-quality QA. Subentries are hierarchical. Cross-volume locator coverage looks sound on the spot-checks. The hyphenation fix shows the process is real, not theater. Continue the quarterly re-audit cadence already declared.

**C3-03 — Symbol disambiguation handled in two places.** Master Index Section "Disambiguation" overlaps Appendix E §E.3. Decide whether the index is authoritative or the appendix is, and let the other be a pointer. Current language ("Appendix E for the authoritative symbol arbitration") suggests E is authoritative — good — but verify Master Index treats σ, λ, ρ, τ, Z, Λ as pointers rather than independent rulings.

## 6. Rights & Permissions — FAIL

**C1-06 — No permissions register exists.** I cannot find a `PERMISSIONS.md` or equivalent log for: figure credit lines on non-original figures; quoted material over fair-use length; reproductions of equations from papers (most equations are derivations and clear, but the C₁–C₅ QED coefficients in Ch 1 trace to Schwinger, Kinoshita et al. — those are facts, not protected, but **table reproductions of published experimental values need credit lines**: Planck 2018, ATLAS/CMS Higgs, Gabrielse g–2, LIGO events, etc.). For each, the publisher needs either "data from [citation]" credit (usually adequate under fair-use for tabulated values) or a permission letter if a figure is reproduced. Build the register now while citations are fresh. Start from Bibliography Bib.3 (Experimental Physics, ~60 entries) — every entry that backs a figure or table needs a credit-line decision.

**C1-07 — Scripture translation not declared.** This is non-negotiable. The series is publicly framed as deriving physics from Genesis 1. Genesis 1 is quoted (the epigraph candidates, the VOLUME_PREFACE invocations of "Waters Above," etc.). The copyright page must declare which translation is primary (ESV, NIV, NASB, KJV, author's translation) and carry the publisher-mandated acknowledgment text verbatim. ESV requires a specific Crossway notice with permission for >500 verses; NIV requires Biblica/Zondervan notice; NASB requires Lockman acknowledgment. KJV is public domain in the US but not in the UK (Crown copyright). **Pick one. Get the letter. Print the notice.** Skipping this is the kind of error that triggers a stop-ship at the printer.

## 7. Marketability & Positioning — PASS

**Drafted back-cover blurb (149 words):**

> Physics has spent a century accumulating extraordinary precision and an embarrassing list of unanswered questions: *why* is the fine-structure constant 1/137? *Why* the speed of light, the proton's mass, the cosmic energy budget? Standard physics measures the numbers but cannot derive them. *The Foundations of Genesis Physics, Volume 6* — *Predictions, Simulations, and Open Problems* — is the framework's accountability statement. It catalogs 153 numbered predictions with quantitative falsification thresholds, packages every simulation for hands-on reproduction, audits where the framework matches observation, where it differs from the Standard Model, and where it makes commitments no one else has made. It is honest about the 27 open problems and the most speculative chapters (FTL transport, energy harvesting, the consciousness interface). Hand it to a skeptical physicist with a laptop. If the framework is wrong, this is the volume that will show you exactly how.

**Top three comps:** (1) Roger Penrose, *The Road to Reality* (2004) — comparable in scope/ambition; this volume is more focused and more falsifiable. (2) Sean Carroll, *The Big Picture* (2016) — comparable in willingness to take metaphysics seriously; opposite worldview. (3) Lee Smolin, *The Trouble with Physics* (2006) — the closest fellow-traveler for "honest about what is unsolved." Defensible on all three.

**One-sentence pitch:** A graduate-level reckoning that hands skeptics 153 numbered, falsifiable predictions, complete simulation code, and a candid open-problems catalog — the prove-me-wrong volume of a physics framework derived from Genesis 1.

**First-page hook (Ch 1):** PASSES. "Five volumes of derivation lie behind us… *does any of this actually match what we observe?*" earns the second page. The three-level "match" taxonomy is a strong organizing move on page one. Browsing-reader test: pass.

**C2-08 — Author bio still required (see C1-02) before positioning is fully complete.**

## 8. Production Readiness — NOTES

**C2-09 — Equation typesetting consistency unaudited.** Mixed `$$ … $$` and inline `$ … $` in the chapter samples. Confirm a single display-equation convention and that every numbered equation uses `\tag{V.Ch.N}` form. Appendix E should mandate.

**C3-04 — In-text URLs at risk of rot.** The technology summary and simulation reproducibility appendix point to GitHub. Ensure DOIs (Zenodo) are minted for the simulation repository before publication; GitHub URLs alone will rot within 10 years.

**C3-05 — Heading hierarchy clean.** Spot-check H1/H2/H3 across Ch 1, 9, 17 shows no skipped levels.

**C3-06 — File naming consistent.** `Ch{NN}_DRAFT.md` convention holds. Versioning via change log in QUALITY_GATE.md is functioning.

## 9. Accessibility — FAIL

**C1-08 — No alt-text manifest.** Without figure assets, alt-text cannot be authored. Build alongside the figure pipeline (C1-05). Every figure needs an alt-text string of one to three sentences sufficient for a screen-reader user to understand the figure's claim, plus a long-description for any conceptually load-bearing diagram. The Master Index already names ~30 figures across appendices; budget 30+ alt-text entries minimum.

**C4-01 — Equation accessibility (post-pub).** For the e-book edition, equations must render with MathML for screen readers, not as flat images. Schedule for the e-book conversion phase.

## 10. Metadata — NOTES

**C2-10 — BISAC codes proposed:** SCI055000 (Physics / Quantum Theory), SCI015000 (Physics / Astrophysics & Space Science), SCI051000 (Physics / Mathematical & Computational), and cross-listed REL106000 (Religion / Religion & Science). The cross-list is the lever for the platform-building strategy.

**C3-07 — Title is long but accurate.** *The Foundations of Genesis Physics, Volume 6: Predictions, Simulations, and Open Problems* is acceptable for a graduate textbook; trade buyers will not see this volume on a front table. Subtitle does discovery work.

**C4-02 — ISBN strategy.** Allocate separate ISBNs for print hardcover, print paperback, and e-book. Audio is not realistic for this volume (heavy equation content); deprioritize.

**C4-03 — Endorsement strategy.** Five-to-eight target endorsers should be identified now. Suggested categories: one foundations-of-physics name (Smolin, Rovelli, or similar), one Christian-physicist name (Lennox, Polkinghorne estate, or Gingerich), one experimentalist who can speak to the prediction catalog, one philosopher of science (Dawid is a natural fit given Vol 6's falsifiability stance), one engineer for the technology roadmap. Begin outreach before galleys.

---

## Broken Cross-References (high-suspicion list)

1. P6.C.28 → V6.Ch9.Eq(6.9.7) — equation number unstable until Ch 9 multi-part draft is collapsed (C1-04).
2. Any pre-2026-05-11 reference to P-068 through P-088 — should now resolve to P-089 through P-109; audit.
3. Ch 6 title "N-Body Simulations" used in any in-text cross-reference where Ch 6's actual content (perturbation theory) is the referent.

## Missing Permissions / Credits (high-suspicion list)

1. Primary Scripture translation declaration + acknowledgment block (C1-07).
2. Experimental data tables — Planck 2018, ATLAS/CMS, LIGO, g–2, fine-structure constant CODATA values. Credit lines required.
3. Comparison tables against Standard Model / ΛCDM values — confirm fair-use applicability or seek permission.
4. Any reproduced figures from Vols 1–5 cross-referenced into Vol 6.

## Top Three Production Blockers (ranked)

1. **Front matter (C1-01, C1-02, C1-03):** half-title, title page, copyright, dedication/epigraph, TOC, LoF, LoT, LoP, author bio, About the Series. **No book ships without these.** ~2 weeks of editorial work; zero new physics.
2. **Figure pipeline + alt-text manifest (C1-05, C1-08):** real figure files at 300 DPI / vector, with credit lines and accessibility metadata. ~3–4 weeks; can run in parallel with #1.
3. **Permissions register + Scripture acknowledgment (C1-06, C1-07):** one tracked log, one translation decision, one publisher letter. ~1 week once decisions made.

## Recommendation to Editorial Board

**Acquire conditional on a 6-week pre-press readiness sprint.** The intellectual content is genuinely distinctive, the back matter is best-in-class for this project, and the first-page hook earns the second page. The missing pieces are publishing infrastructure, not authorial work. Sign the deal; pay for production support; ship in Q4 2026.

— Margaret Holloway, Acquisitions & Production
