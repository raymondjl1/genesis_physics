# The Creator's Blueprint (Family Edition) — Claude Instructions

> **BOOK-NUMBER MAPPING (April 2026 repositioning):** Throughout this file and the other Family Edition docs, references to "Book 2" and "Book 1" use the **old logical numbering** (Book 1 = physicist monograph *The Firmament Equations*, Book 2 = zero-equations *Hidden Architecture of Creation*). Under the repositioning, both are consolidated into a single **Popular Science Flagship** titled *Genesis Physics: The Hidden Architecture — A Physics of the First Page*, living in the `Book_1_Hidden_Architecture/` folder (renamed April 2026 from `Book_1_The_Firmament_Equations/`). When a rule here says "every physics claim traces to Book 2" or "Book 2 for physics content," read it as "traces to the Popular Science Flagship (`Book_1_Hidden_Architecture/`)." The underlying rule is unchanged; only the consolidation is new.

You are working on **Genesis Physics: The Creator's Blueprint (Family Edition)**, a scripture-first teaching resource for homeschool families. This book wraps confirmed physics in direct Biblical quotation and teaching. It is the most explicitly Christian product in the series — and the one most likely to change a family's understanding of both the Bible and science.

## Launch Order: FIRST (flagship launch book)

**Launch order (commercial):** Family Edition (THIS BOOK) → Popular Science flagship → Foundations Series (in parallel)

The Family Edition launches first because it serves the warmest, most loyal, most word-of-mouth-driven audience (Christian homeschool families) and seeds the author platform for the popular-science flagship that follows. It is the book that generates the reviews, the community, and the email list that everything else depends on.

## Content Dependency Order: LAST

**Foundations Series → Popular Science Flagship (*The Hidden Architecture: A Physics of the First Page*, in `Book_1_Hidden_Architecture/`) → THIS BOOK**

The Family Edition is the easiest book to *launch* and the hardest book to *write correctly* — every physics claim traces upward through the popular-science flagship → the physicist monograph → Foundations for verification. This book wraps that confirmed physics in scripture. **It never invents physics and never proof-texts scripture.**

In practice this means: the underlying physics content must be locked *before* this book is drafted, even though this book reaches readers first. Parallel work on the Foundations Series and the popular-science flagship is what makes that possible.

## Before Writing

1. **Read `../AUTHOR_VOICE_AND_BACKGROUND.md`** — canonical reference for who Jeff L. Raymond is, how he sounds, and the voice pillars every chapter must satisfy. This is the single source of truth for voice across the franchise.
2. **Read `QUALITY_GATE.md`** in this folder — requirements, reviewer assignments, scripture-first rules
3. **Read `Quality_Control/BOOK_SERIES_STRATEGY.md`** — section "THE FAMILY EDITION: Genesis Physics for Families" for the 15-chapter outline
4. **Read `Development_Process/01_WRITING_PROCESS.md`** — chapter-level workflow
5. **Read the Popular Science flagship's completed chapters** (housed in `Book_1_Hidden_Architecture/` after its April 2026 repositioning, and/or `Book_2_The_Hidden_Architecture/` for archival narrative beats) — understand the physics narrative you're building on
6. **Check `Quality_Control/Reference/Biblical_References.md`** — master scripture reference list

## Research Dependencies

The Creator's Blueprint draws on two sources: **Book 2** for physics content and **Scripture/Hebrew analysis** for theological content.

### Key Reference Files
```
Book_2_The_Hidden_Architecture/Manuscript/  ← PRIMARY PHYSICS SOURCE

Quality_Control/Reference/
├── Biblical_References.md             ← Master scripture reference list
├── Glossary.md                        ← Terms consistent across series
└── Zone_Architecture.md               ← Zone architecture reference

Research/Papers/
├── hebrew_word_analysis.docx          ← Hebrew word study (CRITICAL for FE)
├── cosmological_challenges_yec.docx   ← Addressing YEC questions families will ask
├── flood_subterranean_reservoir_model.docx ← Flood geology model
├── starlight_rapid_expansion.docx     ← Starlight problem for parents who ask
└── radiometric_dating_functional_maturity.docx ← Dating questions families will raise

Research/Foundations/
├── AXIOM_OPEN_SYSTEM.md              ← Open system = God sustains creation
├── AXIOM_PHASE_TRANSITION_FALL.md    ← Fall as thermodynamic phase transition
└── AXIOM_SUSTAINING_COUPLING.md      ← Sustaining force = Colossians 1:17
```

### Research Gap Protocol

If a chapter requires:
- **Physics not covered in Book 2:** Create a Book 2 gap issue, not a Foundations issue. Fix flows downward.
- **Scripture interpretation not yet studied:** Create `Manuscript/ChXX_SCRIPTURE_GAP.md` and a GitHub issue with label `scripture-research`
- **A "But What About?" question you can't answer:** Document it honestly. Some questions are open. Parents respect honesty more than hand-waving.

```bash
gh issue create --repo raymondjl1/genesis_physics \
  --title "Scripture Gap: [topic] (FE Ch XX)" \
  --label "book:creators-blueprint,scripture-research" \
  --body "Chapter XX requires [scripture topic]. No existing analysis in Research/Papers/ or Quality_Control/Reference/."
```

## Assigned Reviewer Agents

7 reviewers assigned (from `Quality_Control/Reviewers/`):

| Reviewer | What They Check |
|----------|----------------|
| **But Why? Reader** | Does every concept explain WHY? (scripture + physics) |
| **Writing Coach** | Warm, encouraging voice? Not preachy? Not condescending? |
| **Consistency Auditor** | Physics consistent with Book 2? Scripture quoted accurately? |
| **Homeschool Mom ("Sarah")** | Could Sarah (3 kids, ages 9/14/16) teach from this? |
| **Style Editor** | Style sheet compliance, formatting, copyediting |
| **Theologian** | Biblical/exegetical accuracy, theological fidelity |
| **Navigator** | Cross-book depth calibration, series coherence |
| **The Skeptic** | NOT assigned — this book doesn't need to convince an atheist. |

(Physicist and Student are NOT assigned to The Creator's Blueprint.)

## Voice

**Canonical source:** `../AUTHOR_VOICE_AND_BACKGROUND.md` — read it before drafting any chapter. The six voice pillars (operator not professor, frontline-leader authority, cleared-community discretion, MBSE discipline, builder's honesty, quiet faith) apply across every book in the franchise.

**Family Edition voice specialization:** **Warm, encouraging teacher.** The same author voice as the rest of the franchise, turned toward the kitchen table. Like a knowledgeable parent — a field-experienced aerospace engineer who has also spent a decade working out what Genesis 1 is actually describing — guiding a family through the wonder of God's creation. Scripture leads. Physics follows. Never preachy. Never condescending. Never apologetic about either the Bible or the science.

This is NOT the popular-science flagship with Bible verses pasted in. It's a fundamentally different product: scripture-first, physics-confirming. The author's operator-not-professor credibility is what lets him speak plainly to families without talking down to them — that credibility is documented in full in `AUTHOR_VOICE_AND_BACKGROUND.md` and should show through in every chapter.

## Critical Rules

- **Scripture FIRST.** Every chapter begins with what the Bible says, then shows how physics confirms it. Not the other way around.
- **Minimum 5 scripture quotations per chapter.** Quoted accurately with book, chapter, and verse.
- **No proof-texting.** Scripture used in context, never forced to say something it doesn't say.
- **Discussion questions in every chapter.** Open-ended — no single "right answer." Promote family conversation.
- **Family activities in every chapter.** Hands-on demonstrations a family can do together.
- **"But What About?" sections.** Anticipate the questions families will ask (age of earth, dinosaurs, evolution, etc.) and address them honestly.
- **Every physics claim traces to Book 2.** And through Book 2 to Book 1 to Foundations.
- **A parent without a science degree must be able to teach from this book.** If "Sarah" can't follow it, rewrite it.
- **ZERO equations.** Same rule as Book 2.

## The "Sarah" Test

Every chapter must pass the Homeschool Mom reviewer (REVIEWER_05). Her persona:
- **Sarah**, homeschool mom, 3 kids (ages 9, 14, 16)
- Strong in faith, not strong in science
- Needs to feel confident teaching this material
- Her 14-year-old will ask hard questions
- Her 16-year-old might push back on "Bible says so" without more depth
- Her 9-year-old needs to not be bored

If Sarah can't teach from it, it fails. Period.

## Chapter Validation Workflow

For each of the 15 chapters:
1. Re-read `../AUTHOR_VOICE_AND_BACKGROUND.md` (or at minimum the voice pillars and voice test) before drafting
2. Create CHAPTER_SPEC.md from template (use scripture plan + activity plan)
3. Verify the supporting popular-science / Foundations physics chapter is complete and verified
4. Identify all scripture passages — verify accuracy against source text
5. Plan discussion questions and family activities
6. Write detailed outline → Draft → Self-review
7. **Special checks:** Scripture accuracy audit + zero-equations audit + "Sarah" readability + voice-pillar audit (matches `AUTHOR_VOICE_AND_BACKGROUND.md`)
8. Run all 7 assigned reviewer agents (especially Homeschool Mom and Theologian)
9. Update QUALITY_GATE.md chapter status

## GitHub Tasks for The Creator's Blueprint

When `gh` CLI is available, create these with label `book:creators-blueprint`:

```bash
# Planning
gh issue create --title "FE: Create BOOK_SPEC.md" --label "book:creators-blueprint,phase:planning"
gh issue create --title "FE: Verify Book 2 completeness — can all 15 chapters be written?" --label "book:creators-blueprint,book:hidden-architecture,research-gap"
gh issue create --title "FE: Build master scripture plan (all 15 chapters)" --label "book:creators-blueprint,phase:planning,scripture-research"
gh issue create --title "FE: Develop family activity inventory" --label "book:creators-blueprint,phase:planning"
gh issue create --title "FE: Compile 'But What About?' question list from common homeschool concerns" --label "book:creators-blueprint,phase:planning"

# Per chapter (15 total)
for ch in $(seq -w 1 15); do
  gh issue create --title "FE Ch ${ch}: Create spec, outline, draft, verify" \
    --label "book:creators-blueprint,phase:writing" \
    --body "1. Create CHAPTER_SPEC.md with scripture plan + activity plan\n2. Verify Book 2 source\n3. Scripture accuracy check\n4. Outline → Draft → Self-review\n5. Zero-equations audit\n6. Run 5 reviewer agents (esp. Homeschool Mom)\n7. Update QUALITY_GATE.md"
done

# Integration
gh issue create --title "FE: Full manuscript integration and teaching flow review" --label "book:creators-blueprint,phase:integration"
gh issue create --title "FE: Validation — homeschool parent test" --label "book:creators-blueprint,phase:validation"
gh issue create --title "FE: Production pipeline (Vellum, cover, KDP, ACX)" --label "book:creators-blueprint,phase:production"
```
