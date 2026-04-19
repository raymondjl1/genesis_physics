
```
Use the genesis-chapter-writer skill to write [PRODUCT] [VOLUME if applicable], Chapter [N]: "[Working Title]".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for this volume
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md if one already exists (skip Phase 1 if it does)
- All prior chapter drafts in this volume (for continuity and forward-dependency checking)

Product: [Foundations Vol N / Book 1 / Book 2 / The Creator's Blueprint]
Chapter: [N]
Working Title: [title]

Special instructions: [any specific emphasis, open questions to address, or constraints — or "none"]
```

---

## Example: Vol 1, Chapter 1 (Pilot Chapter)

```
Use the genesis-chapter-writer skill to write Foundations Vol 1: Architecture of Reality, Chapter 1: "Axioms and Definitions".

Follow the full 6-phase lifecycle: Spec → Outline (with figure plan) → Draft → Self-Review → Reviewer Agents → Finalize.

Before starting, read:
- The CLAUDE.md in the book folder
- The WRITING_PROMPT.md for Vol 1
- The SOURCE_MAP.md for research file mappings
- The CHAPTER_SPEC.md (already exists — skip Phase 1)
- Quality_Control/Reference/ files for canonical notation, glossary, zone architecture, and axiom summary cards

Product: Foundations Vol 1
Chapter: 1
Working Title: Axioms and Definitions

Special instructions: This is the pilot chapter for the entire series. Every notation decision, axiom statement, and equation number is permanent. Get it right.
```

---

## Usage Notes

- **One chapter per conversation.** Start fresh so the full context window is dedicated to writing.
- **Build order is enforced.** The skill won't let you write Ch 3 before Ch 2 is done, or Vol 2 before Vol 1.
- **Figures are planned in Phase 2** before any drafting starts. You'll see the full figure spec table before a word of prose is written.
- **10 reviewer agents run after the draft.** If any reviewer fails, the skill loops back to fix and re-run until all pass.
- **Special instructions** are your lever for chapter-specific guidance — things like "resolve the open question about κ-field dimensional analysis" or "keep the theological justification lighter here."
