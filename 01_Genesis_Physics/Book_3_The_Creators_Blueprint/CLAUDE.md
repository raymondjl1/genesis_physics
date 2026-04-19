# The Creator's Blueprint — Claude Instructions

You are working on **Genesis Physics: The Creator's Blueprint**, a scripture-first teaching resource for homeschool families. This book wraps confirmed physics in direct Biblical quotation and teaching. It is the most explicitly Christian product in the series — and the one most likely to change a family's understanding of both the Bible and science.

## Build Order: LAST

**Foundations Series → Book 1 → Book 2 → THIS BOOK**

The Creator's Blueprint cannot be written until Book 2 is substantially complete. Every physics claim traces upward through Book 2 → Book 1 → Foundations for verification. This book wraps that confirmed physics in scripture. **It never invents physics and never proof-texts scripture.**

## Before Writing

1. **Read `QUALITY_GATE.md`** in this folder — requirements, reviewer assignments, scripture-first rules
2. **Read `Quality_Control/BOOK_SERIES_STRATEGY.md`** — section "THE FAMILY EDITION: Genesis Physics for Families" for the 15-chapter outline
3. **Read `Development_Process/01_WRITING_PROCESS.md`** — chapter-level workflow
4. **Read Book 2's completed chapters** — understand the physics narrative you're building on
5. **Check `Quality_Control/Reference/Biblical_References.md`** — master scripture reference list

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

**Warm, encouraging teacher.** Like a knowledgeable parent guiding their kids through the wonder of God's creation. Scripture leads. Physics follows. Never preachy. Never condescending. Never apologetic about either the Bible or the science.

This is NOT Book 2 with Bible verses pasted in. It's a fundamentally different product: scripture-first, physics-confirming.

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
1. Create CHAPTER_SPEC.md from template (use scripture plan + activity plan)
2. Verify Book 2 source chapter is complete and verified
3. Identify all scripture passages — verify accuracy against source text
4. Plan discussion questions and family activities
5. Write detailed outline → Draft → Self-review
6. **Special checks:** Scripture accuracy audit + zero-equations audit + "Sarah" readability
7. Run all 5 assigned reviewer agents (especially Homeschool Mom)
8. Update QUALITY_GATE.md chapter status

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
