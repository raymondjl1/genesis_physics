# Book 1: The Firmament Equations — Claude Instructions

You are working on **Book 1: Genesis Physics — The Firmament Equations**, a physicist-level monograph that presents zone architecture with enough mathematical rigor for a professional physicist to evaluate. This is the bridge between the Foundations Series (full derivations) and Book 2 (zero equations).

## Build Order: SECOND

**Foundations Series → THIS BOOK → Book 2 → The Creator's Blueprint**

Book 1 cannot be written until the Foundations Series is substantially complete. Every equation in this book must have a full derivation somewhere in the Foundations volumes. Book 1 **summarizes** — it never **invents** new physics.

## Before Writing

1. **Read `QUALITY_GATE.md`** in this folder — requirements, reviewer assignments, chapter validation status
2. **Read `Quality_Control/BOOK_SERIES_STRATEGY.md`** — section "BOOK 1: The Firmament Equations" for the 25-chapter outline
3. **Read `Development_Process/01_WRITING_PROCESS.md`** — chapter-level workflow
4. **Read `Development_Process/00_PROCESS_OVERVIEW.md`** — full SE lifecycle
5. **Check Foundations volumes** — verify the derivations this book will reference are complete

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
4. Create GitHub issue: `gh issue create --repo raymondjl1/genesis_physics --title "Research Gap: [topic] (Book 1 Ch XX)" --label "book:firmament-equations,research-gap"`

## Assigned Reviewer Agents

5 reviewers assigned (from `Quality_Control/Reviewers/`):

| Reviewer | What They Check |
|----------|----------------|
| **The Physicist** | Are equations correct? Do they trace to Foundations? |
| **But Why? Reader** | Does every concept explain WHY? (MOST IMPORTANT) |
| **Writing Coach** | Brian Greene voice? Accessible but rigorous? |
| **Consistency Auditor** | Notation matches Foundations? Cross-references valid? |
| **The Skeptic** | Would Dr. Marcus Chen take this seriously? |

(Homeschool Mom and Student are NOT assigned to Book 1.)

## Voice

Brian Greene's *Elegant Universe*. A physicist writing for intelligent non-physicists. Rigorous without being impenetrable. Every equation gets a physical explanation. The reader should feel like they're having a sophisticated conversation about the deepest questions in physics.

## Critical Rules

- **Every equation explained.** No orphan equations. Every equation gets a sentence explaining what it MEANS physically.
- **Every claim traces to Foundations.** If it's derived in Vol 3, Ch 7, cite it: "As derived in Foundations Vol 3, §7.3..."
- **Be honest about gaps.** If a derivation is incomplete in Foundations, say so explicitly. This earns physicist respect.
- **Moderate math density.** Equations present but always contextualized. Target: 40% rigorous, 35% formal, 25% semi-formal.
- **No scripture.** Book 1 is a physics monograph. The framework speaks for itself. Christ is revealed through the architecture, not through quotation.

## Chapter Validation Workflow

For each of the 25 chapters:
1. Create CHAPTER_SPEC.md from `Development_Process/03_CHAPTER_SPEC_TEMPLATE.md`
2. Verify source derivation exists in Research/ or Foundations
3. Write detailed outline → Draft → Self-review
4. Run all 5 assigned reviewer agents
5. Run relevant test suites: `cd Research/Mathematical_Models && python -m pytest [domain]/test_*.py -v`
6. Update QUALITY_GATE.md chapter status

## GitHub Tasks for Book 1

When `gh` CLI is available, create these with label `book:firmament-equations`:

```bash
# Planning phase
gh issue create --title "Book 1: Create BOOK_SPEC.md" --label "book:firmament-equations,phase:planning"
gh issue create --title "Book 1: Audit Foundations completeness — can all 25 chapters be written?" --label "book:firmament-equations,research-gap"
gh issue create --title "Book 1: Map chapters to Foundations derivations" --label "book:firmament-equations,phase:planning"

# Per chapter (25 total)
for ch in $(seq -w 1 25); do
  gh issue create --title "Book 1 Ch ${ch}: Create spec, outline, draft, verify" \
    --label "book:firmament-equations,phase:writing" \
    --body "1. Create CHAPTER_SPEC.md\n2. Verify Foundations source\n3. Outline → Draft → Self-review\n4. Run 5 reviewer agents\n5. Run test suites\n6. Update QUALITY_GATE.md"
done

# Integration
gh issue create --title "Book 1: Full manuscript integration and cross-chapter review" --label "book:firmament-equations,phase:integration"
gh issue create --title "Book 1: Validation — complete book reviewer pass" --label "book:firmament-equations,phase:validation"
gh issue create --title "Book 1: Production pipeline (formatting, cover, KDP)" --label "book:firmament-equations,phase:production"
```

## Known Critical Issues (from Quality_Control/Findings/)

- Zone numbering inconsistency between manuscript sections — must be resolved before writing
- Some derivations reference "standard results" without showing the work — every claim needs a Foundations citation
- Notation drift between early and late chapters of existing manuscript — establish notation in Ch 1 and lock it
