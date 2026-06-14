# The Hidden Architecture: A Physics of the First Page — Claude Instructions

**Book title:** *Genesis Physics: The Hidden Architecture — A Physics of the First Page*
(Series mark · Main title · Subtitle)

> **REPOSITIONING NOTE (April 2026):** This folder originally housed a physicist-level monograph titled *The Firmament Equations* (~80–100K words, 25 chapters, Brian Greene voice with 40% rigorous math) at path `Book_1_The_Firmament_Equations/`. That positioning was the wrong commercial bet — the rigorous derivations belong entirely in the Foundations Series, not in a trade book. **The folder has been renamed to `Book_1_Hidden_Architecture/` and now houses the Popular Science Flagship**, *Genesis Physics: The Hidden Architecture — A Physics of the First Page*, the second book to launch under the Jeff L. Raymond byline. The GitHub label was renamed in parallel from `book:firmament-equations` to `book:hidden-architecture` (all existing issues migrated).

You are working on the **Popular Science Flagship** of the Genesis Physics franchise — a trade nonfiction book in the *Elegant Universe* / *Reality Is Not What It Seems* lineage that presents zone architecture to intelligent laypeople (the kind of reader who buys Brian Greene, Carlo Rovelli, Sean Carroll, John Lennox). It is the book that establishes Jeff L. Raymond as a credible, distinct voice in the popular-science conversation.

## Launch Order: SECOND

**Launch order (commercial):** Family Edition (`Book_3_The_Creators_Blueprint/`) → THIS BOOK → Foundations Series (in parallel)

The Family Edition launches first to seed the platform with a warm, word-of-mouth-driven Christian homeschool audience. This book launches second, riding that momentum into the much larger but cooler general popular-science market. The Foundations Series is built in parallel (it is the encyclopedia — it does not need a marketing launch; it needs to *exist* so this book can cite it).

## Content Dependency Order: SECOND (after Foundations content is ready)

**Foundations Series → THIS BOOK → Family Edition (which uses this book's confirmed physics)**

This book cannot be drafted until the Foundations Series is substantially complete on the topics it covers. Every claim in this book must have a full derivation somewhere in the Foundations volumes. This book **explains and dramatizes** — it never **invents** new physics, and it does not reproduce the math.

## Repositioned Content Spec (supersedes original Book 1 spec)

| Dimension | Old (physicist monograph) | New (popular science flagship) |
|-----------|---------------------------|-------------------------------|
| Audience | Practicing physicists | Intelligent layperson (Greene/Rovelli reader) |
| Reading level | Grade 14–16 | Grade 11–13 |
| Word count | 80,000–100,000 | 70,000–90,000 |
| Chapters | 25 | 14–18 (TBD) |
| Math density | 40% rigorous / 35% formal / 25% semi-formal | **Light. Conceptual diagrams and a small number of named equations only.** No naked math. No derivations. |
| Voice | Brian Greene, *Elegant Universe* | Jeff L. Raymond as defined in `../AUTHOR_VOICE_AND_BACKGROUND.md` — operator-not-professor, MBSE-disciplined, builder's honesty, quiet faith |
| Scripture | None | None — biblical grounding is implicit. (Explicit scripture is the Family Edition's job.) |
| What it sells | Physicist credibility | The *idea* of zone architecture, and the author |

The 25-chapter physicist outline in this folder's `README.md` is **archival** — refer to it for content inventory, but the new outline must be rebuilt for the popular-science audience before drafting resumes.

## Before Writing

1. **Read `../AUTHOR_VOICE_AND_BACKGROUND.md`** — canonical reference for voice and author background. This is the single source of truth for voice across the franchise. Every chapter must satisfy the six voice pillars and pass the voice test.
2. **Read `QUALITY_GATE.md`** in this folder — requirements, reviewer assignments, chapter validation status (note: reviewer assignments need to be revised to match the new positioning — see below)
3. **Read `Quality_Control/BOOK_SERIES_STRATEGY.md`** — both the original "BOOK 1" section (archival) and the "BOOK 2: The Hidden Architecture" section (the popular-science thinking that may now fold into this folder)
4. **Read `Development_Process/01_WRITING_PROCESS.md`** — chapter-level workflow
5. **Read `Development_Process/00_PROCESS_OVERVIEW.md`** — full SE lifecycle
6. **Read `Book_2_The_Hidden_Architecture/CLAUDE.md` and `README.md`** — the existing zero-equations spec; relevant material here likely consolidates into this folder
7. **Check Foundations volumes** — verify the derivations this book will reference are complete

## Research Dependencies

Book 1 references Foundations derivations. Before writing any chapter, verify the source derivation exists and is verified:

### Key Research Files
```
Research/Foundations/
├── AXIOM_OPEN_SYSTEM.md              ← Open system axiom (Ch 1-3)
├── AXIOM_6D_SPACETIME.md             ← 6D framework (Ch 4-5)
├── AXIOM_MEMBRANE_MECHANICS_v2.md    ← Firmament mechanics (Ch 6-8)
├── AXIOM_WATERS_DUALITY.md           ← Dark matter/energy (Ch 9-10)
├── AXIOM_PHASE_TRANSITION_FALL.md    ← Thermodynamic phases (Ch 11-12)
└── ACTION_6D_COMPLETE.md             ← Complete action (Ch 13+)

Research/Mathematical_Models/
├── 03_Electromagnetism/MAXWELL_FROM_ZONE_ARCHITECTURE.md  ← Ch 14-15
├── 01_Classical_Mechanics/APPLIED_GRAVITY_CALCULATIONS.md ← Ch 16
├── 05_Quantum_Mechanics/QM_FROM_MEMBRANE_DYNAMICS.md      ← Ch 17-18
├── 06_Nuclear_and_Particle_Physics/PARTICLE_MASS_SPECTRUM_v3.md ← Ch 19-20
├── 07_Relativity/GR_OBSERVABLES.md                        ← Ch 21
├── 08_Cosmology/CMB_POWER_SPECTRUM.md                     ← Ch 22-23
└── 10_Fundamental_Constants/DERIVE_FINE_STRUCTURE_COEFFICIENT.md ← Ch 24

Research/Peer_Review/
├── critic_report.md           ← Known criticisms to address
└── skeptic_analysis.md        ← Skeptic perspective to anticipate

Research/Papers/                ← Reference papers for context
```

### Research Gap Protocol

If a chapter requires a derivation that doesn't exist in Research/ or Foundations/:

1. **STOP.** Do not hand-wave or summarize something that hasn't been derived.
2. Create `Manuscript/ChXX_RESEARCH_GAP.md` documenting what's missing
3. Flag the chapter spec requirement as BLOCKED
4. Create GitHub issue: `gh issue create --repo raymondjl1/genesis_physics --title "Research Gap: [topic] (Book 1 Ch XX)" --label "book:hidden-architecture,research-gap"`

## Assigned Reviewer Agents (REVISED for popular-science positioning)

Reviewer assignments under the old physicist-monograph spec listed The Physicist as a top reviewer. Under the new popular-science positioning, The Physicist still validates accuracy of *claims* but not the presence of equations (because equations are largely absent). The critical reviewers shift:

| Reviewer | What They Check |
|----------|----------------|
| **The "But Why?" Reader** | Does every concept explain WHY? (MOST IMPORTANT) |
| **The Writing Coach** | Voice matches `AUTHOR_VOICE_AND_BACKGROUND.md`? Wonder-driven? Grade 11–13 readable? |
| **The Skeptic** | Would Dr. Marcus Chen find this interesting rather than off-putting? Logical integrity? |
| **The Consistency Auditor** | Claims trace to Foundations? Terminology matches the franchise? Cross-references valid? |
| **The Physicist** | Are the *claims* correct against Foundations? (Even when equations aren't shown, the physics behind them must be right.) |
| **The Style Editor** | Style sheet compliance |
| **The Navigator** | Depth calibration — sophisticated enough for a Greene reader, accessible enough for the smart layperson |
| **The Theologian** | Even though scripture isn't quoted, the implicit theology must be sound |

(Homeschool Mom and Student are NOT assigned to this book.)

QUALITY_GATE.md should be revised to match this list when the repositioning is fully implemented.

## Voice

**Canonical source:** `../AUTHOR_VOICE_AND_BACKGROUND.md` — read it before drafting any chapter. The six voice pillars (operator not professor, frontline-leader authority, cleared-community discretion, MBSE discipline, builder's honesty, quiet faith) apply across every book in the franchise.

**Popular-science flagship voice specialization:** Wonder-driven narrative, told by a credible operator (not a professor at a podium). The reader should feel they're being walked through a hidden engineering blueprint by someone who has actually built things, deployed systems in hostile environments, and worked with people who fly America's spy satellites — not by an academic who has never left the classroom. Sophisticated without being impenetrable. Confident without being grandiose. The framework, not the author, is the hero.

If a sentence sounds like Brian Greene wrote it, ask whether Jeff L. Raymond would actually say it. If not, rewrite. The author's distinct credibility (operator, MBSE pioneer, intelligence officer turned drone-program founder turned Genesis-physics builder) is the reason this book exists at all.

## Critical Rules

- **Voice fidelity.** Every chapter must satisfy the six voice pillars and pass the voice test in `AUTHOR_VOICE_AND_BACKGROUND.md`.
- **Light math density.** Conceptual diagrams and a small number of named equations only. No naked math. No derivations. The Foundations Series is the encyclopedia for the math; this book points readers there.
- **Every claim traces to Foundations.** If it's derived in Vol 3, Ch 7, cite it: "(See Foundations Vol 3, §7.3 for the full derivation.)"
- **Be honest about gaps.** If a derivation is incomplete in Foundations, say so explicitly. This earns reader trust.
- **No scripture quotation.** This book is the popular-science flagship. The framework speaks for itself. Christ is revealed through the architecture, not through quotation. (Explicit scripture is the Family Edition's job.)
- **Simplified transliteration by design.** Use diacritic-free Hebrew transliteration throughout (*raqia*, *bara*, *yom*) — no macrons or ayin marks, even at first mention. This is intentional and differs from Foundations, which uses the precise macron/ayin form (*rāqîaʿ*) at first mention. See the series-wide Transliteration Policy in `../CLAUDE.md` and the two-tier rule in Foundations Vol 1 AppC §C.20.
- **Leave them hungry.** End every chapter wanting more. End the book pointing two ways: to the Family Edition (for readers who sense the theological undertow) and to the Foundations Series (for readers who want the math).

## Chapter Validation Workflow

For each chapter (final chapter count TBD when the new outline is built):
1. Re-read `../AUTHOR_VOICE_AND_BACKGROUND.md` (or at minimum the voice pillars and voice test) before drafting
2. Create CHAPTER_SPEC.md from `Development_Process/03_CHAPTER_SPEC_TEMPLATE.md` (use the analogy table — light math, heavy analogy)
3. Verify source derivation exists in Research/ or Foundations — claims must be backed even if math isn't shown
4. Write detailed outline → Draft → Self-review
5. **Special checks:** voice-pillar audit (matches `AUTHOR_VOICE_AND_BACKGROUND.md`), math-density audit (light, not zero — but never naked), readability check (Grade 11–13)
6. Run all 8 assigned reviewer agents
7. Run relevant test suites where they validate cited Foundations claims: `cd Research/Mathematical_Models && python -m pytest [domain]/test_*.py -v`
8. Update QUALITY_GATE.md chapter status

## GitHub Tasks for Book 1

When `gh` CLI is available, create these with label `book:hidden-architecture`:

```bash
# Planning phase
gh issue create --title "Book 1: Create BOOK_SPEC.md" --label "book:hidden-architecture,phase:planning"
gh issue create --title "Book 1: Audit Foundations completeness — can all 15 chapters be written?" --label "book:hidden-architecture,research-gap"
gh issue create --title "Book 1: Map chapters to Foundations derivations" --label "book:hidden-architecture,phase:planning"

# Per chapter (15 total — see CHAPTER_PROMPTS.md for the authoritative outline)
for ch in $(seq -w 1 15); do
  gh issue create --title "Book 1 Ch ${ch}: Create spec, outline, draft, verify" \
    --label "book:hidden-architecture,phase:writing" \
    --body "1. Create CHAPTER_SPEC.md\n2. Verify Foundations source\n3. Outline → Draft → Self-review\n4. Run assigned reviewer agents\n5. Run test suites where applicable\n6. Update QUALITY_GATE.md"
done

# Integration
gh issue create --title "Book 1: Full manuscript integration and cross-chapter review" --label "book:hidden-architecture,phase:integration"
gh issue create --title "Book 1: Validation — complete book reviewer pass" --label "book:hidden-architecture,phase:validation"
gh issue create --title "Book 1: Production pipeline (formatting, cover, KDP)" --label "book:hidden-architecture,phase:production"
```

## Known Critical Issues (from Quality_Control/Findings/)

- Zone numbering inconsistency between manuscript sections — must be resolved before writing
- Some derivations reference "standard results" without showing the work — every claim needs a Foundations citation
- Notation drift between early and late chapters of existing manuscript — establish notation in Ch 1 and lock it
