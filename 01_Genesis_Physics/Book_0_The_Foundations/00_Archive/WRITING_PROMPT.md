# Book 0: The Foundations of Genesis Physics — Writing Prompt

**Use this prompt to instruct Claude Cowork to write chapters for the 6-volume Foundations Series.**

---

## Prompt

You are writing **The Foundations of Genesis Physics**, a 6-volume graduate textbook series (~750,000–900,000 words total) that derives all known physics from a zone architecture framework rooted in Genesis 1. This is the scientific backbone of the entire Genesis Physics Series — every other book rests on what you prove here.

### Before You Begin

Read these files in order — they are your operating instructions:

1. **`01_Genesis_Physics/CLAUDE.md`** — Master project instructions, philosophy, reviewer agents, what NOT to do
2. **`Book_0_The_Foundations/CLAUDE.md`** — Book 0-specific instructions, known research gaps, test suite requirements
3. **`Book_0_The_Foundations/Vol_X_[Name]/CLAUDE.md`** — Volume-specific instructions (read the one for the volume you're writing)
4. **`Development_Process/00_PROCESS_OVERVIEW.md`** — The full SE lifecycle mapped to book development
5. **`Development_Process/01_WRITING_PROCESS.md`** — Step-by-step chapter writing workflow (6 phases)
6. **`Development_Process/03_CHAPTER_SPEC_TEMPLATE.md`** — Template for every chapter spec
7. **`Quality_Control/00_SERIES_VISION.md`** — The North Star: what we're building and why
8. **`Quality_Control/01_REQUIREMENTS.md`** — 48+ requirements with acceptance criteria
9. **`Quality_Control/BOOK_SERIES_STRATEGY.md`** — Detailed chapter outlines for all 6 volumes (scroll to "BOOK 0" section)

### Research Sources — Check These Before Writing Anything

```
Research/Foundations/              ← Axiom definitions (AXIOM_*.md), validation reports
Research/Mathematical_Models/     ← 10 physics domains with derivations + Python test suites
  01_Classical_Mechanics/
  02_Thermodynamics/
  03_Electromagnetism/
  04_Optics_and_Waves/
  05_Quantum_Mechanics/
  06_Nuclear_and_Particle_Physics/
  07_Relativity/
  08_Cosmology/
  09_Chemistry_and_Materials/
  10_Fundamental_Constants/
Research/Simulations/             ← Python simulation scripts
Research/Papers/                  ← Research papers (docx)
```

Each volume has a `Source_Reference/SOURCE_MAP.md` that maps original manuscript chapters and research files to that volume's chapters.

### Reference Documents — For Consistency

```
Quality_Control/Reference/
  Glossary.md                     ← All terms — use these exact definitions
  Symbol_and_Constants.md         ← Every symbol and constant — use these exact values
  Zone_Architecture.md            ← Zone properties, boundaries, numbering
  Biblical_References.md          ← Scripture concordance
  Axiom_Summary_Cards.md          ← All 7 axioms: statement, equations, status
  Four_Epochs_Timeline.md         ← Creation → Edenic → Fall → Redemption
  Five_Principles.md              ← Canonical definitions and equations
```

### Writing Process (Follow Exactly)

For each chapter:

1. **Create CHAPTER_SPEC.md** — Use template from `Development_Process/03_CHAPTER_SPEC_TEMPLATE.md`. Fill in: mission, requirements (traced to book requirements), prerequisites, "why" chain (3–5 questions this chapter answers), key deliverables, section outline, verification criteria, assigned reviewers.

2. **Verify Research Exists** — Check `Research/` for every derivation the chapter needs. If something is missing, STOP. Create a `RESEARCH_GAP.md` note and a GitHub issue (`gh issue create --repo raymondjl1/genesis_physics --title "Research Gap: [topic]" --label "research-gap"`). Mark the spec requirement as BLOCKED.

3. **Write Detailed Outline** — 4–8 sections per chapter. Each section: topic sentence, "why" entry point, content plan, exit condition.

4. **Write Draft** — Follow the Five Writing Laws:
   - **Start with WHY** — why does this matter? Why does this have to be this way?
   - **Physical intuition before math** — explain what's happening before proving it
   - **One voice** — Feynman writing a textbook. Authoritative but human. Never dry.
   - **No forward dependencies** — never use a concept before establishing it
   - **Mark uncertainty honestly** — if something is incomplete or approximate, say so

5. **Self-Review** — Run through the author checklist in `01_WRITING_PROCESS.md`. Product-specific checks for Foundations: every derivation complete (no "it can be shown"), all notation matches Vol 1 conventions, dimensional analysis passes, limiting cases checked, problem sets included.

6. **Run Reviewer Agents** — Use the `genesis-reviewer` skill or read reviewer definitions from `Quality_Control/Reviewers/`:

   **Assigned to Foundations (10 reviewers):**
   | Reviewer | File | Focus |
   |----------|------|-------|
   | The Physicist | REVIEWER_01 | Derivation completeness, mathematical rigor |
   | The "But Why?" Reader | REVIEWER_02 | **Most critical.** Does every concept explain WHY? |
   | The Writing Coach | REVIEWER_03 | Feynman voice, readability, flow |
   | The Consistency Auditor | REVIEWER_04 | Notation, cross-references, no contradictions |
   | The Skeptic | REVIEWER_06 | Logical integrity, no circular reasoning |
   | The Student | REVIEWER_07 | Can a grad student follow and reproduce? |
   | The Style Editor | REVIEWER_08 | Style sheet compliance, formatting |
   | The Theologian | REVIEWER_09 | Biblical/exegetical accuracy |
   | The Navigator | REVIEWER_10 | Depth calibration, series coherence |

   NOT assigned: Homeschool Mom (REVIEWER_05 — Creator's Blueprint only)

7. **Revise Until All PASS** — Address every FAIL. Re-run reviewers on revised sections.

8. **Update STATUS.md and QUALITY_GATE.md** — Mark chapter status and reviewer results.

### Volume-Specific Notes

| Volume | Key Content | Pages | Critical Deliverables |
|--------|-------------|-------|----------------------|
| **Vol 1** | Axioms, zone manifold, conservation laws, thermodynamic laws | 400–500 | All axioms with motivation, zone manifold definition, notation standard locked |
| **Vol 2** | Four forces derived, Maxwell's equations, gauge theory | 400–500 | Why exactly 4 forces, hierarchy problem solved, fine structure derivation starts |
| **Vol 3** | F=ma as theorem, classical mechanics, thermodynamics | 350–450 | Newton's laws derived not postulated, all thermo laws from zone separation |
| **Vol 4** | QM, QFT, Standard Model, particle masses | 500–600 | Wave function derived, Standard Model recovered, masses calculated. **5 CRITICAL GAPS** |
| **Vol 5** | GR, cosmology, fine structure constant, fundamental constants | 400–500 | EFE recovered from 6D, fine structure from first principles, all constants derived |
| **Vol 6** | Predictions, simulations, falsification, open problems | 300–400 | Every prediction numbered with falsification threshold, code reproducible |

### Word Count Targets

- **Per chapter:** 8,000–15,000 words
- **Per volume:** 90,000–180,000 words
- **Total series:** 750,000–900,000 words

### Critical Rules

- **NEVER skip the "why."** Every concept must explain WHY before WHAT.
- **NEVER invent physics.** Everything must trace to Research/ derivations.
- **NEVER use a concept before establishing it.** No forward dependencies.
- **NEVER hand-wave derivations.** "It can be shown that" is FORBIDDEN. Show it.
- **NEVER claim a derivation is complete if the test suite fails.** Honesty is foundational.
- **Mark all research gaps explicitly.** An honest gap is better than a fake derivation.
- **Include problem sets.** Every chapter needs 20–50 problems spanning accessible to challenging.
- **Run test suites.** `python -m pytest Research/Mathematical_Models/[domain]/test_*.py -v`

### Skills Available

- **`genesis-chapter-writer`** — Guides you through the full chapter lifecycle (spec → outline → draft → self-review → reviewer verification → finalize)
- **`genesis-reviewer`** — Runs the 10 reviewer agents against a chapter draft

### GitHub Integration

When `gh` CLI is available:
```bash
gh issue create --repo raymondjl1/genesis_physics --title "[Vol X Ch Y] [description]" --label "book:foundations,vol:X"
```

---

*This prompt was generated April 6, 2026 from the complete project setup.*
