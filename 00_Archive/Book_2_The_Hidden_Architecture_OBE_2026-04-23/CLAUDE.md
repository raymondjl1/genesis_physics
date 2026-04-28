# Book 2: The Hidden Architecture of Creation — Claude Instructions (ARCHIVAL SOURCE)

> **REPOSITIONING NOTE (April 2026):** The original plan had two lay-audience books — a physicist monograph titled *The Firmament Equations* (in the folder then named `Book_1_The_Firmament_Equations/`, since renamed to `Book_1_Hidden_Architecture/`) and a zero-equations book titled *The Hidden Architecture of Creation* (this folder). That split was commercially weak: no single title was heavy enough to be a flagship, and the two competed for the same casual reader.
>
> **Under the April 2026 repositioning, the Popular Science Flagship now lives in the `Book_1_Hidden_Architecture/` folder and takes the title *Genesis Physics: The Hidden Architecture — A Physics of the First Page*.** It absorbs this folder's mandate. This folder is now a **source/archive** for the flagship — its analogy inventory, narrative hooks, zero-equations discipline, and the 15-chapter outline all feed forward. Do not draft new standalone chapters here.
>
> **Title collision warning:** "The Hidden Architecture" is now the Book 1 main title. This folder is named `Book_2_The_Hidden_Architecture/` for cross-reference stability but no longer owns that title. Any doc referring to *The Hidden Architecture* as a book title after April 2026 means the Book 1 flagship.

You are working on **Book 2: Genesis Physics — The Hidden Architecture of Creation**, the original general-audience entry point to the Genesis Physics Series (zero equations, Brian Cox meets C.S. Lewis voice). Under the repositioning its role is absorbed by the Popular Science Flagship in `Book_1_Hidden_Architecture/`.

## Launch Order: absorbed into the Popular Science Flagship (launches SECOND via `Book_1_Hidden_Architecture/`)

**Launch order (commercial):** Family Edition (`Book_3_The_Creators_Blueprint/`) → Popular Science Flagship (`Book_1_Hidden_Architecture/`, which absorbs this book) → Foundations Series (in parallel)

## Before Writing (if this folder is revived as a standalone product)

1. **Read `../AUTHOR_VOICE_AND_BACKGROUND.md`** — canonical reference for voice and author background. Single source of truth for voice across the franchise.
2. **Read `QUALITY_GATE.md`** in this folder — requirements, reviewer assignments, zero-equations rule
3. **Read `Quality_Control/BOOK_SERIES_STRATEGY.md`** — section "BOOK 2: The Hidden Architecture" for the 15-chapter outline
4. **Read `Development_Process/01_WRITING_PROCESS.md`** — chapter-level workflow
5. **Read the Popular Science Flagship's completed chapters** in `Book_1_Hidden_Architecture/` — understand the physics you're simplifying
6. **Check `Quality_Control/Reference/`** — glossary, zone architecture, biblical references, symbols

## Research Dependencies

Book 2 doesn't reference Research/ directly — it references **Book 1**, which references Foundations, which references Research. But you should still be aware of the underlying physics:

### Key Reference Files
```
Book_1_Hidden_Architecture/Manuscript/    ← PRIMARY SOURCE — simplify from here
Quality_Control/Reference/
├── Glossary.md                      ← Terms and definitions
├── Zone_Architecture.md             ← Zone architecture quick reference
├── Biblical_References.md           ← Scripture references (use sparingly in Book 2)
├── Symbol_and_Constants.md          ← Symbols and values
└── Five_Principles.md               ← Canonical principle definitions

Research/Papers/
├── hebrew_word_analysis.docx        ← Hebrew word study for creation terms
├── cosmological_challenges_yec.docx ← Addressing young earth questions
└── starlight_rapid_expansion.docx   ← Starlight problem resolution
```

### Research Gap Protocol

If a chapter requires an explanation of physics that Book 1 doesn't adequately cover:

1. **STOP.** Don't invent an explanation that isn't backed by Book 1.
2. Create `Manuscript/ChXX_RESEARCH_GAP.md` documenting what's missing
3. Flag as "Book 1 gap" — the fix is in Book 1, not here
4. Create GitHub issue: `gh issue create --repo raymondjl1/genesis_physics --title "Book 1 Gap (needed for Book 2 Ch XX): [topic]" --label "book:hidden-architecture,research-gap"`

## Assigned Reviewer Agents

4 reviewers assigned (from `Quality_Control/Reviewers/`):

| Reviewer | What They Check |
|----------|----------------|
| **But Why? Reader** | Does every concept explain WHY? (MOST IMPORTANT) |
| **Writing Coach** | Wonder-driven narrative? Engaging? Not preachy? |
| **Consistency Auditor** | Claims consistent with Book 1? Terminology matches? |
| **The Skeptic** | Would an atheist find this interesting rather than off-putting? |

(Physicist, Homeschool Mom, and Student are NOT assigned to Book 2.)

## Voice

**Canonical source:** `../AUTHOR_VOICE_AND_BACKGROUND.md` — the franchise's single source of truth for voice.

**Book 2 archival voice note:** *Brian Cox meets C.S. Lewis* was the original voice spec. Under the April 2026 repositioning, the franchise voice is Jeff L. Raymond's as defined in `AUTHOR_VOICE_AND_BACKGROUND.md` — operator-not-professor, MBSE-disciplined, builder's honesty, quiet faith. "Brian Cox meets C.S. Lewis" captures the *tonal target* (wonder-driven, lucid, not sermonic) but not the author's actual credibility profile. The flagship uses the canonical voice; analogies and narrative hooks from this folder should be adapted to it, not copied verbatim.

The secret: Christ is revealed through the beauty and order of the architecture itself, never through direct quotation or preaching. A reader who doesn't know the Bible should finish this book marveling at the design. A reader who does know the Bible should see Genesis 1 everywhere.

## Critical Rules

- **ZERO EQUATIONS.** Not one. Not even E=mc². Every concept explained in words, analogies, and images. If it can't be explained without math, it doesn't belong in this book.
- **Every claim traces to Book 1.** Even though the reader doesn't know Book 1 exists, every simplification must be faithful to the underlying physics.
- **Analogies must be accurate.** They simplify without misleading. When an analogy breaks down, say where.
- **Leave them hungry.** The reader should finish wanting Book 1 the way you want the next season of a show.
- **No forward dependencies.** Concepts build chapter by chapter. No concept used before established.
- **No scripture quotation.** Save that for the The Creator's Blueprint. This book lets the architecture speak for itself.

## Analogy Standards

Every chapter in Book 2 relies on analogies to explain physics without equations. Each analogy must:

1. **Map correctly** to the underlying physics (check against Book 1)
2. **Have clear limits** — state where the analogy breaks down
3. **Be memorable** — the reader should be able to explain this to a friend
4. **Be original where possible** — avoid overused physics analogies ("bowling ball on a trampoline" for gravity is banned)

Document all analogies in the chapter spec using the Analogy table from `Development_Process/03_CHAPTER_SPEC_TEMPLATE.md`.

## Chapter Validation Workflow

For each of the 15 chapters:
1. Create CHAPTER_SPEC.md from template (use the Book 2 analogy table)
2. Verify Book 1 source chapter is complete and verified
3. Write detailed outline → Draft → Self-review
4. **Special check: Zero-equations audit** — search for ANY mathematical notation
5. Run all 4 assigned reviewer agents
6. Update QUALITY_GATE.md chapter status

## GitHub Tasks for Book 2 — ARCHIVAL

> **LABEL NOTE (April 2026):** Under the repositioning, the `book:hidden-architecture` label now belongs to the Popular Science Flagship (`Book_1_Hidden_Architecture/`). Do **not** create new issues against Book 2 as a standalone product — its mandate is folded into the flagship. Historical issues previously opened against this folder (if any) can be audited and either closed, or relabeled to `book:hidden-architecture` and triaged into the flagship backlog.
>
> The command blocks below are **archival**; they reflect the issue structure that would have been used if Book 2 had shipped as its own product. Kept for reference only — do not run them.

```bash
# ARCHIVAL — do not run. Book 2's mandate is now the flagship's (Book_1_Hidden_Architecture/).

# Planning
gh issue create --title "Book 2: Create BOOK_SPEC.md" --label "book:hidden-architecture,phase:planning"
gh issue create --title "Book 2: Verify Book 1 completeness — can all 15 chapters be written?" --label "book:hidden-architecture,research-gap"
gh issue create --title "Book 2: Develop analogy inventory for all 15 chapters" --label "book:hidden-architecture,phase:planning"

# Per chapter (15 total)
for ch in $(seq -w 1 15); do
  gh issue create --title "Book 2 Ch ${ch}: Create spec, outline, draft, verify" \
    --label "book:hidden-architecture,phase:writing" \
    --body "1. Create CHAPTER_SPEC.md with analogy plan\n2. Verify Book 1 source\n3. Outline → Draft → Self-review\n4. Zero-equations audit\n5. Run 4 reviewer agents\n6. Update QUALITY_GATE.md"
done

# Integration
gh issue create --title "Book 2: Full manuscript integration and narrative arc review" --label "book:hidden-architecture,phase:integration"
gh issue create --title "Book 2: Validation — intelligent friend test" --label "book:hidden-architecture,phase:validation"
gh issue create --title "Book 2: Production pipeline (Vellum, cover, KDP, ACX)" --label "book:hidden-architecture,phase:production"
```
