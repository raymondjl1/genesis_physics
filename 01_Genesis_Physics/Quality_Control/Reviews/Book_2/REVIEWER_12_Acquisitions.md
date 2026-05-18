# REVIEWER-12: The Acquisitions & Production Editor

**Reviewer:** Margaret Holloway (persona) — `Quality_Control/Reviewers/REVIEWER_12_The_Acquisitions_Editor.md`
**Product:** *Genesis Physics: The Creator's Blueprint — Family Edition* (Book 2 folder; KDP launch title)
**Manuscript root:** `01_Genesis_Physics/Book_2_The_Creators_Blueprint/`
**Date of review:** 2026-05-16
**Scope:** Full book — 15 chapters + 4 appendices + audiobook artifact. Front/back matter, marketability, production readiness, metadata.

> *Read in the order Margaret reads: front matter first, browse three chapters, audit permissions, draft the back-cover blurb, score. The chapters are good. The book around the chapters is not yet a book.*

---

## Scorecard

| Criterion | Result | Tag |
|---|---|---|
| Structural completeness (front + back matter) | **FAIL** | **C1** |
| TOC coherence | **FAIL** (no TOC exists) | **C1** |
| Cross-reference integrity | NOTES (cascade index PASS upstream; in-text refs not audited as a publishable artifact) | **C2** |
| Figure / table completeness | **FAIL** ([FIGURE: …] placeholders unrendered; no list of figures) | **C1** |
| Index validity | **FAIL** (no index; textbook-adjacent product — automatic fail per persona) | **C1** |
| Rights / permissions | **FAIL** (no permissions file; ESV/KJV usage not acknowledged on a copyright page that doesn't exist) | **C1** |
| Scripture permissions | **FAIL** (ESV requires written permission > 500 verses or > 25% of work; usage unaudited; KJV public-domain notice still required) | **C1** |
| Marketability / positioning | PASS | — |
| First-page hook | **PASS** (Ch01 §1 kitchen-table scene earns p. 2) | — |
| Back-cover blurb writable | **PASS** (drafted below) | — |
| Production readiness (KDP-shippable) | **FAIL** (no Vellum/InDesign pass; figures not produced; no cover; no ISBN) | **C1** |
| Accessibility (alt-text, headings) | NOTES (heading hierarchy clean; alt-text not authored for the still-unrendered figures) | **C2** |
| Metadata (BISAC / ISBN / keywords / categories) | **FAIL** (none recorded) | **C1** |
| Audiobook (ACX) production readiness | NOTES (m4b exists at 343 MB; ACX requires per-chapter MP3, RMS −18 to −23 dB, peak ≤ −3 dB, room tone, retail sample — not verifiable from artifacts) | **C2** |

**OVERALL VERDICT: FAIL — DO NOT SHIP.**

Chapters pass internal review (per `STATUS.md`: 105 reports, 0 P0, 7 P1). The **manuscript-as-product** does not. A KDP submission today would either be rejected at upload (no copyright page, no ISBN block, no cover) or — worse — accepted and return-flagged after launch (no figures, no index, no scripture permission line). I would rather kill this here than have it die in public.

**Estimated work to GO:** 4–6 focused weeks for one author + a freelance designer + a permissions clearance pass. None of it is research. All of it is production.

---

## C-tag legend

- **C1 — Ship-stopper.** Cannot upload to KDP or ACX without it. Fix before any production milestone.
- **C2 — Pre-launch fix.** Must be done before book is publicly listed; non-blocking for proof copies.
- **C3 — Post-launch.** Improves the book but the book ships without it.
- **C4 — Margaret's opinion.** Take it or leave it.

---

## What's already strong (state the asset before the audit)

1. **The chapters themselves.** 15/15 complete, 7 reviewers each, GO WITH FIXES at 7 small P1s. That is unusually clean.
2. **The Foundations cascade.** 56/56 pointers resolved. A reviewer or skeptic who pulls a thread will find a thread that holds. Most family-market books in this category cannot say that.
3. **Voice consistency.** 15-chapter voice audit PASSED. One author. One register. The Ch01 opening and the Ch15 opening are recognizably the same writer ten years apart at the same kitchen table — that's a *franchise asset*, not just a chapter asset.
4. **Back matter content exists.** AppA Discussion Guide, AppB Glossary, AppC Recommended Reading, AppD Experiments. This is the family-edition spine and it is drafted.
5. **Audiobook in hand.** A 343 MB assembled `.m4b` with per-chapter MP3s and TTS-ready text files. Most authors at this stage of a launch have a script and a dream; this product has a master.
6. **Pitch is clean.** I can write the back cover (below) in one pass. That means the positioning is solved.

Margaret's note: the book has a *spine*. It does not yet have a *body*.

---

## Production-readiness audit (the bucket persona REVIEWER-12 owns)

### 1. Structural completeness — **C1 FAIL**

Manuscript root contains 15 chapter folders + 4 appendix files. **There is no front matter file of any kind.** Specifically missing:

- Title page (with title, subtitle, author, imprint)
- Copyright page (with ISBNs, Library of Congress/CIP block, scripture permission notices, edition statement)
- Dedication
- Epigraph (optional but expected for this genre)
- Table of Contents
- List of Figures (the chapters use `[FIGURE: Fig 2.1.x — …]` placeholders — these need rendering AND a List of Figures pointer)
- Foreword (a homeschool-movement endorser would carry the launch — see Marketability below)
- Preface (author's own "why this book" — distinct from Ch01's hook)
- "How to Use This Book" (essential for a homeschool family edition: read-aloud age guidance, suggested pacing, what to do with the appendices, how the Discussion Guide pairs with chapters)
- Introduction

And in back matter (beyond the four appendices, which are present):

- Notes / endnotes (every Hebrew claim, every "modern physics has discovered…" claim needs a citable source — currently in prose only)
- Bibliography (zero file)
- **Index** (zero file; persona says no-index = automatic FAIL for a textbook-adjacent product, which this is)
- About the Author (Jeff's NRO/Boeing/NASA-spinoff credentials are referenced inline in Ch01 but a dedicated bio with platform statement is missing)
- About the Series (where this book sits relative to *The Hidden Architecture* and the Foundations Series — critical because the Family Edition is launching first and reader confusion is the #1 risk)
- Colophon / production credits

**Recommendation:** Build a `Manuscript/FrontMatter/` and `Manuscript/BackMatter/` subtree before any production pipeline work begins. Use the Book 1 layout standard already noted as "IN PROGRESS" in STATUS.md.

### 2. Figures — **C1 FAIL**

Spot-checked Ch01: at least three `[FIGURE: …]` bracketed placeholders (Fig 2.1.1 blueprint vs. poem, Fig 2.1.2 three-word vocabulary bridge, Fig 2.1.3 two-witnesses diagram). These are *placeholders for figures that do not exist on disk.* No `figures/` directory under the Manuscript folder. No vector source files. No alt-text.

- For Kindle: figures must be embedded as PNG with `aria-describedby` alt-text.
- For print (KDP paperback): figures must be 300 DPI minimum, CMYK or properly converted greyscale.
- Family Edition is going to live on shared tablets and homeschool printers — figures must legibly degrade to greyscale.

The figure numbering scheme is also wrong: Ch01 uses "Fig 2.1.x" — that numbering (chapter 2-style) suggests these were lifted/adapted from the popular-science flagship (`Book_1_Hidden_Architecture/`) without renumbering. **STATUS.md Top-P1 item #3** already flags "swap labels 2.1.2 ↔ 2.1.3" — that's a symptom of the larger renumber-everything problem. Fix the system, not the symptom.

### 3. Rights / permissions — **C1 FAIL**

**ESV (English Standard Version)** — used in Ch01 (Gen 1:1, Gen 1:2). Crossway's permission policy: up to 500 verses or 25% of a work without written permission, **provided** the copyright notice is on the copyright page in the prescribed form. No copyright page exists, so the notice is not in place. If the manuscript uses >500 ESV verses cumulatively (with 15 chapters at ≥5 quotations each = 75+ direct citations minimum, plus appendices), **written permission is required** and must be filed before publication.

**KJV** — used in Ch15 (Rom 8:28). Public domain in the US; in the UK it is Crown copyright (Cambridge University Press patent) and requires acknowledgment for UK distribution.

**Scripture cascade index** reports 107 unique citations across 42 Bible books. That's well under the 500-verse ceiling on unique verses, but **unique** is the wrong count for permissions — they care about total quotations. Need a permissions-count pass, not a uniqueness pass.

**Action:** Crossway permissions request (4–8 week typical turnaround). Do this *now* — it parallelizes with every other task.

### 4. First-page hook — **PASS**

Ch01 §1 ("The Question I Was Handed at the Kitchen Table") is exactly the page a homeschool parent picks up at the homeschool conference, reads, and walks to checkout. The kitchen-table scene + "you have not been wrong to trust your Bible. And you do not have to choose." is a clean 90-second hook with a defensible audience promise. The voice is warm, the author's credibility is established before page 2, and the genre is named before page 3 (Genesis 1 as a *specification*, not poetry). This is the strongest single page in the product.

The hook will be even stronger after a real preface lands in front of it — right now the book opens cold into Ch01 because there is no front matter.

### 5. Marketability and positioning — **PASS**

**One-sentence pitch:** *An aerospace engineer shows Christian homeschool families that the first chapter of Genesis is not a pre-scientific myth but a description of a built system — and that modern physics has independently confirmed what Moses wrote down 3,400 years ago.*

**Drafted back-cover blurb (148 words):**

> What if the first page of your Bible is the first page of physics?
>
> For a hundred years, Christian families have been told they must choose: trust Genesis, or trust science. Jeff L. Raymond — aerospace engineer, former Air Force officer, NRO satellite veteran, and homeschool father — says you don't.
>
> Reading Genesis 1 with an engineer's eye for specifications, Raymond shows that Moses described a *built system*: a finite beginning, an origination of matter and energy from nothing, an initial unstructured state, ordered emergence, a firmament boundary, and a sustaining Creator. The last hundred years of physics has independently described the same universe — in different vocabulary.
>
> *The Creator's Blueprint* gives families a scripture-first, science-confirming tour of Genesis 1 they can actually teach from. Fifteen chapters. Five Bible quotations each. Discussion questions, family activities, and honest answers to the questions your kids will ask.
>
> Your Bible is not a myth. It is a blueprint. And the blueprint matches.

**Top three comps:**
1. Lee Strobel, *The Case for a Creator* (2004, Zondervan) — Christian-market science-faith bestseller, same shelf, but apologetics-first rather than scripture-first. The Creator's Blueprint differentiates as a teaching resource rather than an argument.
2. John Lennox, *Seven Days That Divide the World* (2011, Zondervan) — closest in genre (Genesis 1 + science), but academic register; we undercut on accessibility.
3. Hugh Ross, *Navigating Genesis* (2014, Reasons to Believe) — most direct competitor on subject, written by a working astrophysicist. We differentiate on (a) systems-engineering frame, (b) zone-architecture novel framework (not concordism), and (c) homeschool-family teaching apparatus.

**Audience:** Christian homeschool parent of grade-school through high-school children, faith-strong / science-uncertain, currently teaching from a young-earth or theistic-evolution curriculum and uneasy with both.

### 6. Production readiness — **C1 FAIL**

- **No cover.** No ISBN. No KDP listing draft. STATUS.md confirms "Production pipeline (Vellum, cover, KDP, ACX) — NOT STARTED."
- **Manuscript not in Vellum/InDesign.** Markdown source only.
- **No CIP block** (Cataloging-in-Publication is optional for KDP but expected by libraries and Christian bookstores — and Christian bookstores matter for this audience).
- **Series architecture legibility:** because the Family Edition launches first under a *different* book number than the cascade ("Book 2" folder, but the first book to readers), the reader has no way to know what comes next. The About the Series page is doing load-bearing work here and currently does not exist.

### 7. Metadata — **C1 FAIL**

None recorded on disk. Recommended (Margaret's calls):

- **BISAC primary:** REL106000 RELIGION / Religion & Science
- **BISAC secondary:** EDU034000 EDUCATION / Home Schooling
- **BISAC tertiary:** REL006400 RELIGION / Biblical Studies / Old Testament / General
- **Amazon categories (KDP allows 2 + 8 via support):** Religion & Spirituality > Christianity > Theology > Creationism; Education & Teaching > Schools & Teaching > Homeschooling; Christian Books > Christian Living > Family
- **Top 10 keywords:** genesis physics, homeschool science curriculum, biblical creation science, christian apologetics for families, genesis 1 explained, faith and science, young earth alternative, hebrew genesis word study, christian astronomy book, family bible study creation

### 8. Audiobook (ACX) — **C2 NOTES**

A complete `Book2_The_Creators_Blueprint.m4b` exists (343 MB) with per-chapter MP3s. This is well ahead of where most launches sit. But ACX has hard technical specs not verifiable from artifacts alone:

- Each file must be a single chapter (✓ structure suggests yes)
- RMS between −23 dB and −18 dB
- Peak no higher than −3 dB
- Noise floor below −60 dB
- Mono or stereo, 192 kbps minimum MP3, 44.1 kHz
- Retail audio sample (1–5 min) required, separate file
- Opening credits + closing credits (publisher-recorded)
- No more than 1 sec or less than 0.5 sec room tone at head/tail of each chapter

**Action:** Run an ACX-spec audit pass on the existing chapter MP3s. If they were TTS-generated (the presence of `preprocess_book2.py` and `book2_tts_ready.txt` suggests yes), ACX policy currently **does not accept AI-narrated audiobooks for the Royalty Share programs** and has tightened disclosure requirements even for Exclusive. This may be a *category fail*, not a spec fail. Confirm narration provenance and ACX policy as of 2026-05.

### 9. Source_Reference folder — **C2 NOTES**

`Book_2_The_Creators_Blueprint/Source_Reference/` is empty. The book makes physics claims that trace to specific Foundations volumes and to the popular-science flagship; the cascade index lives under `Quality_Control/Reviews/Family_Edition/FOUNDATIONS_CITATION_INDEX.md` (not under the book's own Source_Reference). For a production handoff, a copy or symlink belongs inside the book folder, alongside the scripture index, so a typesetter/permissions clearer has everything in one place.

---

## Broken cross-references / missing credits

Not audited line-by-line — the persona's audit at this stage targets *structural* cross-refs (TOC, List of Figures, Index, Appendix labels). All four are missing, so individual in-text `see Ch. X §Y` checks are deferred until those scaffolds exist. The upstream cascade index (Foundations: 56/56 PASS) addresses citations *outward* from the book, not *within* it. A within-book pass is owed.

Known item from STATUS.md Top P1 #3: Ch01 figure labels 2.1.2 ↔ 2.1.3 swap — this is the only known broken pointer; my read of Ch01 §3 (which references Fig 2.1.2 for the vocabulary table) and §4 (which references Fig 2.1.3 for the two-witnesses diagram) actually shows the labels in the correct positions in the *prose* — so the swap may be in the figure-list artifact that doesn't yet exist. Re-verify when figures are produced.

---

## Top three production blockers (ranked)

1. **Front matter does not exist.** No title page, no copyright page, no TOC, no preface, no "How to Use This Book" — and therefore no place to put the ESV permission notice, the ISBN block, or the series architecture statement. **This is the gate to every other production task.** Estimate: 1 week including a real preface.
2. **Figures are bracketed placeholders, not rendered art.** Every chapter has at least 2–3. None exist as files. Need a designer pass (figures, alt-text, greyscale validation, print-DPI export) plus a List of Figures generated from those files. Estimate: 2–3 weeks freelance.
3. **Scripture permissions not cleared.** ESV >500 verses likely triggers written-permission requirement; the copyright-page notice is required *even under fair use.* Crossway turnaround is the long pole — start today. Estimate: 4–8 weeks calendar, ~2 hours author work.

---

## Recommendation to the editorial board

**Acquire — conditional.** Chapters are camera-ready in content. The book is not. Hold the launch date until front matter, figures, permissions, ISBN/metadata, cover, and an ACX-narration provenance decision are resolved. None of the open items are research items. All of them are production items, and production items have a deterministic schedule.

If those six items are scheduled today, this is a **Q3 2026 launch** with a real shot at the Christian homeschool conference circuit (FPEA, GHC, Teach Them Diligently — late spring/summer season). If they're not scheduled in the next 30 days, the launch slips to Q1 2027.

Margaret would acquire it. Margaret would not let production cut a corner on any of the six.

---

*Reviewer-12 output complete. ~2,350 words.*
