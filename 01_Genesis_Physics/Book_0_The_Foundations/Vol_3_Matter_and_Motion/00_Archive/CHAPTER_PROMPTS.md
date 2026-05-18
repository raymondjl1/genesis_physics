# Volume 3: Matter and Motion — Chapter Prompts

One chapter per conversation. Copy the prompt below for the chapter you're ready to write, paste it into a fresh conversation, and let the skill run.

Build order is enforced: write chapters in sequence (Ch 1 → Ch 2 → ... → Ch 12). **Volumes 1 and 2 must be complete before starting Volume 3.**

---

## Chapter 1: Newton's Laws as Theorems

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 1: "Newton's Laws as Theorems".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 1
Working Title: Newton's Laws as Theorems

Special instructions: This is the headline chapter of the entire volume — F=ma becomes a theorem, not an axiom. The derivation must trace explicitly back to Vol 1 Ch 3 (zone manifold geometry) + Vol 2 Ch 2 (gravity from zone curvature). Show the full chain: zone geometry → forces → F=ma as consequence. Source material: 01-APPLIED_GRAVITY_CALCULATIONS.md and Ch16_Observable_Laws.docx. The Physicist and Skeptic reviewers will scrutinize whether F=ma is GENUINELY derived or secretly smuggled in as an assumption. Every step in the proof must be airtight. Citation convention: (1.Ch.Eq) for Vol 1, (2.Ch.Eq) for Vol 2, (3.Ch.Eq) for this volume.
```

---

## Chapter 2: Lagrangian and Hamiltonian Mechanics

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 2: "Lagrangian and Hamiltonian Mechanics".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 2
Working Title: Lagrangian and Hamiltonian Mechanics

Special instructions: Standard material taught through the zone lens — not a generic textbook retread. Vol 1 Ch 8 (Five Principles as variational formulation) and Vol 2 Ch 5 (Zone Lagrangian) are the direct foundations. The student should see Lagrangian and Hamiltonian mechanics as natural consequences of the variational structure already established, not as new formalism imposed on top. This is 40–50 pages — the longest chapter in Part I. Cover: least action from zone principles, Euler-Lagrange equations, Legendre transform, Hamilton's equations, Poisson brackets, canonical transformations. Every result should trace back to the zone Lagrangian.
```

---

## Chapter 3: Central Force Problems

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 3: "Central Force Problems".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–2)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 3
Working Title: Central Force Problems

Special instructions: Apply the machinery from Ch 1–2 to central force problems. Source material: 01-APPLIED_GRAVITY_CALCULATIONS.md. Vol 2 Ch 2 (gravity derivation) is the direct dependency. Cover: the Kepler problem derived from zone gravity, orbital mechanics, scattering theory, the Bertrand theorem. Every orbit and every trajectory should trace back to the gravity derived in Vol 2, not to a postulated 1/r^2 force. Run test suite: Research/Mathematical_Models/01_Classical_Mechanics/test_gravity_kinematics.py.
```

---

## Chapter 4: Rigid Body Dynamics

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 4: "Rigid Body Dynamics".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–3)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 4
Working Title: Rigid Body Dynamics

Special instructions: Vol 1 Ch 7 (angular momentum conservation) is the direct foundation. Reference 04-OPTICS_FROM_MAXWELL.md for any wave/optics connections relevant to rigid body vibration modes. Cover: moment of inertia tensor, Euler's equations, precession, gyroscopes — all derived through zone conservation laws, not postulated. This is 20–30 pages — keep it focused and efficient. The Student reviewer needs to be able to solve rigid body problems using this framework.
```

---

## Chapter 5: Continuum Mechanics and Fluid Dynamics

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 5: "Continuum Mechanics and Fluid Dynamics".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–4)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 5
Working Title: Continuum Mechanics and Fluid Dynamics

Special instructions: This chapter connects BACK to the Waters field equations (Vol 1 Ch 6) — the connection must be explicit and mathematically clear. Source material: 02-WATERS_REPLENISHMENT.md and 01-MATERIAL_PROPERTIES.md. Cover: stress and strain tensors, elasticity, Navier-Stokes equations (show their relationship to the Waters PDEs), fluid dynamics, and wave propagation in continuous media. Known gap (MEDIUM severity): material properties completeness in 01-MATERIAL_PROPERTIES.md — check coverage of elasticity and specific heat; be honest about limits. Vol 5 inherits this for cosmological fluid evolution. Run test suite: Research/Mathematical_Models/01_Classical_Mechanics/test_material_properties.py.
```

---

## Chapter 6: Standing Waves and Stable Configurations

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 6: "Standing Waves and Stable Configurations".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–5)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 6
Working Title: Standing Waves and Stable Configurations

Special instructions: This is where the volume gets deeply creative — matter isn't fundamental, it's what happens when the architecture resonates. Source material: TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md, 01-MATERIAL_PROPERTIES.md, and Ch09_Matter_Formation.docx. Vol 1 dependencies: Ch 5 (Firmament vibration modes) and Ch 9 (pattern operators). Show how standing waves on the Firmament create stable configurations. Think Chladni patterns, membrane vibrations, resonance nodes. The matter formation mechanism must be consistent with TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md. Vol 4 builds on this to calculate specific particle masses.
```

---

## Chapter 7: The Origin of Mass

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 7: "The Origin of Mass".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–6)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 7
Working Title: The Origin of Mass

Special instructions: Source material: 06-PARTICLE_MASS_SPECTRUM_V3.md, 06-HIGGS_DERIVATION.md, and Ch09_Matter_Formation.docx. Vol 1 Ch 5 (Firmament) and Vol 2 Ch 6 (gauge theory) are the direct dependencies. Derive mass from the zone architecture — show how the Higgs mechanism emerges from membrane geometry rather than being postulated. Compare with the Standard Model Higgs and show where the zone framework agrees, extends, or diverges. Vol 4 inherits this to calculate specific particle masses, so the mass-generation mechanism must be precisely defined and extensible.
```

---

## Chapter 8: Phase Transitions in Zone Architecture

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 8: "Phase Transitions in Zone Architecture".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–7)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 8
Working Title: Phase Transitions in Zone Architecture

Special instructions: Bridges Part II (matter) to Part III (thermodynamics). Source material: 02-PHASE_TRANSITIONS_MOLECULAR.md. Vol 1 Ch 11 (basic thermodynamics) is the foundation. Known gap (MEDIUM severity): phase transitions molecular detail — GitHub #12 — state honest limits on what's derived vs. what needs further development. Cover: first-order and second-order transitions, critical phenomena, order parameters, and how zone architecture constrains the space of possible transitions. Vol 5 inherits this for cosmological phase transitions. Run test suite: Research/Mathematical_Models/02_Thermodynamics/test_phase_transitions.py.
```

---

## Chapter 9: The Four Laws — Complete Derivation

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 9: "The Four Laws — Complete Derivation".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–8)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 9
Working Title: The Four Laws — Complete Derivation

Special instructions: MATH IS COMPLETE — 02-LAWS_DERIVATION.md has the full derivation. Also reference Ch13_Thermodynamics.docx. Your job is to write the prose around the existing math. Vol 1 Ch 11 established the basic thermodynamic laws — this chapter EXPANDS into the complete treatment, never contradicts. The four laws must be derived, not postulated. Show the complete chain from zone separation to each law. The thermodynamic law forms here must match Vol 1 Ch 11 exactly while extending them. Run test suite: Research/Mathematical_Models/02_Thermodynamics/test_thermodynamic_laws.py.
```

---

## Chapter 10: Statistical Mechanics on the Zone Manifold

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 10: "Statistical Mechanics on the Zone Manifold".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–9)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 10
Working Title: Statistical Mechanics on the Zone Manifold

Special instructions: Source material: 02-PLANCK_DISTRIBUTION.md and 02-LAWS_DERIVATION.md. Vol 1 dependencies: Ch 10 (quantization from boundary conditions) and Ch 11 (basic thermodynamics). Cover: the partition function on the zone manifold, microcanonical/canonical/grand canonical ensembles, Planck distribution derived from zone quantization, and the classical-quantum bridge. Vol 4 inherits this framework for Fermi-Dirac and Bose-Einstein statistics. Run test suite: Research/Mathematical_Models/02_Thermodynamics/test_planck_spectrum.py.
```

---

## Chapter 11: Kinetic Theory and Transport

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 11: "Kinetic Theory and Transport".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–10)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 11
Working Title: Kinetic Theory and Transport

Special instructions: Vol 1 Ch 6 (Waters field equations) and this volume's Ch 10 (statistical mechanics) are the direct foundations. Also reference 09-CHEMISTRY_DERIVATION.md and 09-ELEMENT_PREDICTION.md for any connections to transport at the atomic/chemical level. Cover: Boltzmann transport equation, mean free path, viscosity, thermal conductivity, diffusion — all connected back to zone architecture. This is 20–30 pages — efficient and focused on the zone-architecture perspective that distinguishes this from a standard kinetic theory treatment.
```

---

## Chapter 12: Entropy, Information, and the Arrow of Time

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Chapter 12: "Entropy, Information, and the Arrow of Time".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (Ch 1–11)
- All completed Vol 1 and Vol 2 chapters

Product: Foundations Vol 3
Chapter: 12
Working Title: Entropy, Information, and the Arrow of Time

Special instructions: This is the philosophical capstone of Volume 3. Source material: 02-WATERS_REPLENISHMENT.md. Also reference Quality_Control/Reference/Four_Epochs_Timeline.md for the theological timeline. The key insight: entropy's arrow is theological — it flows from the Degradation principle (one of the Five Principles). The student should understand WHY time flows forward at the deepest level. The entropy definition must match both Vol 1 Ch 11 AND 02-WATERS_REPLENISHMENT.md. Cover: Shannon entropy, Boltzmann entropy, their equivalence on the zone manifold, information theory connections, and the arrow of time as architectural consequence. Vol 5 connects this to the cosmological timeline. The Theologian reviewer will be especially attentive here.
```

---

## After All Chapters: Back Matter

```
Use the genesis-chapter-writer skill to write Foundations Vol 3: Matter and Motion, Back Matter (Appendices A–B, Problem Sets, Bibliography).

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 3
- ALL 12 chapter drafts in this volume
- Vol 1 Appendix B (Notation Reference)
- Vol 2 Back Matter

Product: Foundations Vol 3
Back Matter Components:
- Appendix A: Key Results from Volumes 1–2
- Appendix B: Experimental Mechanics Data
- Problem Sets with Selected Solutions (Ch 1–12)
- Bibliography (100+ references)

Special instructions: Appendix A must be a concise but complete reference of every Vol 1 and Vol 2 result that Vol 3 cites — the student should be able to look up any referenced equation without flipping back to earlier volumes. Appendix B compiles all experimental data (force measurements, material properties, thermodynamic constants) used or predicted. Problem sets must reference only Vols 1–3 material — never forward-reference. The Student reviewer cares most about this volume's problem sets: can they actually SOLVE problems using the zone framework?
```

---

## Usage Reminders

- **One chapter per conversation.** Start fresh so the full context window is dedicated to writing.
- **Build order is enforced.** Vols 1–2 complete → Ch 1 → Ch 2 → ... → Ch 12 → Back Matter. No skipping.
- **Vols 1–2 are prerequisite.** Every chapter cites Vol 1 and Vol 2 equations. The skill expects completed drafts.
- **Citation convention:** `(1.Ch.Eq)` for Vol 1, `(2.Ch.Eq)` for Vol 2, `(3.Ch.Eq)` for this volume.
- **Math-complete chapter (9):** The math exists in 02-LAWS_DERIVATION.md — write prose and pedagogy around it.
- **Known gaps (Ch 4–5, Ch 8):** Material properties and phase transition detail — be honest about limits.
- **The headline test:** Does F=ma genuinely emerge as a theorem? The Physicist and Skeptic will check.
- **6 test suites** cover classical mechanics, thermodynamics, and optics — run them where noted.
- **10 reviewer agents run after the draft.** The Skeptic will be ruthless about whether F=ma is truly derived.
