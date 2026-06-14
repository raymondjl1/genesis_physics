# Volume Closing Handoff — Template

*Reusable closing artifact for the final chapter of every Foundations volume. Source pattern: Vol 2, Ch 11 §11.8 ("What This Volume Establishes — Bridge to Volume 3"). Standardizes the cross-volume handoff so each downstream volume inherits a precise, tabulated ledger of what it may assume.*

*Adopted from review finding `0516_Rev_203` (GitHub #303) / `0516_Rev_467` (GitHub #567). Place this section as the penultimate section of the final chapter of Vols 1, 3, 4, 5 (Vol 6 is terminal and instead hands off to the trade books). Vol 2 already carries the canonical instance.*

---

## §X.Y What This Volume Establishes — Bridge to Volume [N+1]

Volume [N] has built [one-sentence statement of what this volume completed]. Later volumes inherit specific results.

### For Volume [N+1]: [Title]

[One sentence: what the next volume does with this volume's results.]

| Vol [N] Result | Vol [N+1] Use |
|----------------|---------------|
| [Result, with chapter/eq refs] | [How the next volume uses it] |
| [Result, with chapter/eq refs] | [How the next volume uses it] |
| [Result, with chapter/eq refs] | [How the next volume uses it] |

### For Volume [N+2]: [Title]

*(Repeat one table per downstream volume that directly inherits a load-bearing result. Omit volumes that do not.)*

| Vol [N] Result | Vol [N+2] Use |
|----------------|---------------|
| [Result, with chapter/eq refs] | [How the later volume uses it] |

---

### Authoring rules

1. **Every row names a specific result and where it was established** (chapter and, where applicable, equation number) — never a vague topic.
2. **Only list results that are actually load-bearing downstream.** If a downstream volume does not use a result, it does not appear in that volume's table.
3. **No forward dependencies are created here.** This table only points *forward* to where established results are *used*; it never assumes a later result.
4. **Mirror the build-order footer** (see CHAPTER_SPEC closing block) so the "what this provides" handoff and the "what this consumed" footer are consistent.
