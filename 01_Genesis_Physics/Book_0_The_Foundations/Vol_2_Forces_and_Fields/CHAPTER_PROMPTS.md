# Volume 2: Forces and Fields — Chapter Prompts

One chapter per conversation. Copy the prompt below for the chapter you're ready to write, paste it into a fresh conversation, and let the skill run.

Build order is enforced: write chapters in sequence (Ch 1 → Ch 2 → ... → Ch 11). **Volume 1 must be complete before starting Volume 2.**

---

## Chapter 1: Why Forces Exist

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 1: "Why Forces Exist".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All completed Vol 1 chapters (this volume builds directly on Vol 1)

Product: Foundations Vol 2
Chapter: 1
Working Title: Why Forces Exist

Special instructions: This chapter sets the stage for the entire volume by answering the question no physics textbook answers: WHY are there forces at all? Forces are consequences of geometry, not fundamental entities. Source material: ACTION_6D_COMPLETE.md, KK_DIMENSIONAL_REDUCTION.md, and Ch10_Four_Forces.docx. Vol 1 dependencies: Ch 3 (zone manifold), Ch 4 (6D embedding), Ch 8 (five principles). Introduce the hierarchy problem here and solve it in principle — the quantitative resolution comes in Ch 9. Explain WHY exactly four forces emerge from the zone geometry. Citation convention: cite Vol 1 equations as (1.Ch.Eq).
```

---

## Chapter 2: Gravity from Zone Curvature

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 2: "Gravity from Zone Curvature".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1)
- All completed Vol 1 chapters

Product: Foundations Vol 2
Chapter: 2
Working Title: Gravity from Zone Curvature

Special instructions: Gravity is the simplest geometric consequence — start here to build confidence. Derive Newton's law from zone geometry. Calculate G from zone parameters. Explain WHY gravity is weak. Source material: 10-GRAVITATIONAL_CONSTANT_DERIVATION.md and 01-APPLIED_GRAVITY_CALCULATIONS.md. Vol 1 dependencies: Ch 4 (6D metric), Ch 6 (Waters pressure gradients), Ch 7 (conservation laws). Known gap (MEDIUM severity): gravity derivation from 6D action completeness — check if 10-GRAVITATIONAL_CONSTANT_DERIVATION.md is complete; if not, be honest about what's derived vs. what's postulated. G must match Quality_Control/Reference/Symbol_and_Constants.md. Run test suite: Research/Mathematical_Models/01_Classical_Mechanics/test_gravity_kinematics.py.
```

---

## Chapter 3: Electromagnetism from Membrane Wave Propagation

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 3: "Electromagnetism from Membrane Wave Propagation".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–2)
- All completed Vol 1 chapters

Product: Foundations Vol 2
Chapter: 3
Working Title: Electromagnetism from Membrane Wave Propagation

Special instructions: MATH IS COMPLETE — 03-MAXWELL_DERIVATION.md has the full derivation. Your job is to write the prose around the existing math. Also reference Ch15_Mathematical_Foundations.docx. Derive all four Maxwell's equations from Firmament vibrations. Show that the speed of light is a membrane property. Derive gauge invariance from zone symmetry. Begin the fine structure constant derivation (continued in Vol 5) — ensure consistency with 10-FINE_STRUCTURE_DERIVATION.md. Vol 1 dependencies: Ch 5 (Firmament vibration modes), Ch 7 (gauge symmetry from conservation). This is 50–60 pages and the longest chapter in Part I. Run test suite: Research/Mathematical_Models/03_Electromagnetism/test_em_applications.py.
```

---

## Chapter 4: The Strong and Weak Forces from Zone Boundary Effects

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 4: "The Strong and Weak Forces from Zone Boundary Effects".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–3)
- All completed Vol 1 chapters

Product: Foundations Vol 2
Chapter: 4
Working Title: The Strong and Weak Forces from Zone Boundary Effects

Special instructions: This is the most challenging chapter in Part I. Source material: 06-QCD_DERIVATION.md, 06-WEAK_PARITY_CP_VIOLATION.md, and Ch10_Four_Forces.docx. Vol 1 dependencies: Ch 3 (zone topology), Ch 5 (boundary conditions). Derive confinement from boundary conditions. Derive weak force from zone-mixing. Show WHY these forces are short-range — it must be geometric necessity, not ad hoc. KNOWN GAP (HIGH severity): weak interaction CP violation in 06-WEAK_PARITY_CP_VIOLATION.md — acknowledge this gap honestly and mark it as continued in Vol 4. Do not hand-wave; state clearly what is derived vs. what remains open.
```

---

## Chapter 5: The Zone Lagrangian

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 5: "The Zone Lagrangian".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–4)
- All completed Vol 1 chapters

Product: Foundations Vol 2
Chapter: 5
Working Title: The Zone Lagrangian

Special instructions: This chapter builds the complete Lagrangian for the zone manifold. Source material: ACTION_6D_COMPLETE.md and FIVE_PRINCIPLES_FORMALIZED.md. Also reference Ch11_Five_Principles.docx. Vol 1 dependency: Ch 8 (variational formulation from the Five Principles). Cover: the complete Lagrangian, Euler-Lagrange equations, full symmetry analysis, and a term-by-term comparison with the Standard Model Lagrangian — showing what matches, what's new, and what the zone framework predicts that the SM doesn't. Vol 3 inherits this Lagrangian for Hamiltonian mechanics.
```

---

## Chapter 6: Gauge Theory from Zone Symmetries

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 6: "Gauge Theory from Zone Symmetries".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–5)
- All completed Vol 1 chapters

Product: Foundations Vol 2
Chapter: 6
Working Title: Gauge Theory from Zone Symmetries

Special instructions: Source material: KK_DIMENSIONAL_REDUCTION.md, SYMMETRIES_MASS_INTEGRATION.md, and Ch15_Mathematical_Foundations.docx. Vol 1 dependencies: Ch 3 (manifold symmetries), Ch 4 (isometry groups). Derive U(1), SU(2), and SU(3) as subgroups of the zone manifold symmetry group. WHY these gauge groups — geometric necessity, not assumption. Recover Yang-Mills theory. This is the formal backbone that Vol 4 quantizes — the gauge structure must be precise and complete.
```

---

## Chapter 7: Classical Electrodynamics Complete

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 7: "Classical Electrodynamics Complete".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–6)
- All completed Vol 1 chapters

Product: Foundations Vol 2
Chapter: 7
Working Title: Classical Electrodynamics Complete

Special instructions: This chapter applies the formal results of Part I (Ch 3) and Part II (Ch 5–6) to deliver the full classical E&M treatment. Source material: 03-MAXWELL_DERIVATION.md and 03-APPLICATIONS.md. Everything in Jackson — radiation, waveguides, optics — but derived from zone architecture first principles, not postulated. The student should see how every result in classical electrodynamics traces back to the Firmament membrane. Maxwell's equations must match the form derived in 03-MAXWELL_DERIVATION.md exactly. Vol 3 inherits this for optics and wave mechanics.
```

---

## Chapter 8: Gravitational Field Theory

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 8: "Gravitational Field Theory".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–7)
- All completed Vol 1 chapters

Product: Foundations Vol 2
Chapter: 8
Working Title: Gravitational Field Theory

Special instructions: Go beyond the Newtonian gravity of Ch 2. Source material: GR_OBSERVABLES.md. Vol 1 dependencies: Ch 2 (gravity derivation from this volume), Ch 4 (6D metric from Vol 1). Linearize the zone field equations to recover linearized GR. Derive gravitational waves. Make LIGO predictions from zone parameters. This chapter seeds Vol 5 (full GR from zone geometry) — the linearization procedure must be clean enough that Vol 5 can extend it to the full nonlinear theory.
```

---

## Chapter 9: The Hierarchy Problem Solved

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 9: "The Hierarchy Problem Solved".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–8)
- All completed Vol 1 chapters

Product: Foundations Vol 2
Chapter: 9
Working Title: The Hierarchy Problem Solved

Special instructions: This is where the hierarchy problem introduced in Ch 1 gets its quantitative resolution. Source material: 10-COUPLING_CONSTANTS_DERIVATION.md. Derive WHY gravity is 10^36 times weaker than electromagnetism — calculate the ratio from zone parameters. The Skeptic reviewer will be watching this chapter closely: the resolution must be quantitative and derived, not hand-waving or numerology. If any step relies on an assumption rather than a derivation, flag it explicitly. This is 20–30 pages — tight and focused.
```

---

## Chapter 10: Running Couplings and Zone Energy Scales

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 10: "Running Couplings and Zone Energy Scales".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–9)
- All completed Vol 1 chapters

Product: Foundations Vol 2
Chapter: 10
Working Title: Running Couplings and Zone Energy Scales

Special instructions: Source material: 10-RUNNING_COUPLINGS_RG_FLOW.md. Vol 2 dependencies: Ch 5 (Lagrangian), Ch 6 (gauge groups). Cover: how force strengths change with energy, zone architecture predictions for unification energy, and comparison with Grand Unified Theory (GUT) predictions. KNOWN GAP (MEDIUM severity): running coupling constants precision is partial in the research file — state the honest status of what's precisely calculated vs. what's estimated. Vol 4 uses this for renormalization — the RG flow framework must be extensible.
```

---

## Chapter 11: The Force Landscape

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Chapter 11: "The Force Landscape".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–10)
- All completed Vol 1 chapters

Product: Foundations Vol 2
Chapter: 11
Working Title: The Force Landscape

Special instructions: This is the capstone chapter — bring together every derivation from the entire volume into one complete map of all four forces at all energy scales. Source: all Vol 2 derivations from Ch 1–10. Cover: the complete force landscape, LHC predictions from zone parameters, predictions beyond current experimental reach, and — critically — explicit falsification criteria. What experimental result would disprove this framework? The reader should leave this chapter with a clear picture of what the zone architecture predicts, what's been verified, and what's testable. This is 20–30 pages — concise and definitive.
```

---

## After All Chapters: Back Matter

```
Use the genesis-chapter-writer skill to write Foundations Vol 2: Forces and Fields, Back Matter (Appendices A–B, Problem Sets, Bibliography).

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 2
- ALL 11 chapter drafts in this volume
- Vol 1 Appendix B (Notation Reference)

Product: Foundations Vol 2
Back Matter Components:
- Appendix A: Vector Calculus and Tensor Analysis Review
- Appendix B: Experimental Data Tables (force measurements, coupling constants)
- Problem Sets with Selected Solutions (Ch 1–11)
- Bibliography (150+ references)

Special instructions: Appendix B (Experimental Data Tables) is critical — compile all force measurements, coupling constants, and experimental values used or predicted in the volume. Every number must cite its source (PDG, NIST, LIGO, etc.). Problem sets must reference only Vol 1 + Vol 2 material — never forward-reference to Vol 3+. All notation must match Vol 1 Appendix B exactly; any new symbols introduced in Vol 2 should be listed as additions to the notation system.
```

---

## Usage Reminders

- **One chapter per conversation.** Start fresh so the full context window is dedicated to writing.
- **Build order is enforced.** Vol 1 complete → Ch 1 → Ch 2 → ... → Ch 11 → Back Matter. No skipping.
- **Vol 1 is prerequisite.** Every chapter cites Vol 1 equations. The skill expects completed Vol 1 drafts to be readable.
- **Citation convention:** Vol 1 equations as `(1.Ch.Eq)`, Vol 2 equations as `(2.Ch.Eq)`.
- **Math-complete chapter (3):** The math exists in 03-MAXWELL_DERIVATION.md — write prose and pedagogy around it.
- **Known gaps (Ch 4, Ch 10):** Be honest about what's derived vs. open. Mark gaps for resolution in later volumes.
- **Test suites:** Run EM and gravity tests where noted — they validate the underlying math.
- **10 reviewer agents run after the draft.** The Physicist and Skeptic are especially critical for this volume.
