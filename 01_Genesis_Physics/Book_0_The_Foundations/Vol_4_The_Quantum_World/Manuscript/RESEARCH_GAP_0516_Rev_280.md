# RESEARCH GAP — Task 0516_Rev_280 (Issue #380)

**Volume:** Vol 4 (The Quantum World)
**Location:** Ch 10 §10.3 vs Ch 14 §14.4/§14.5 (three-generation prediction)
**Severity:** P1 — Concern C3 (internal consistency, load-bearing structural claim)
**Status:** AUTHOR-BLOCKED — requires a position decision plus a parametric-stability calculation that does not exist in the Research corpus.

## The discrepancy

The "exactly three generations" prediction carries **two conflicting rigor labels**:

| Location | Label | Stated basis |
|---|---|---|
| Ch 10 §10.3 (`Ch10_FINAL.md` line 165, 206) | **APPROXIMATE** | "the three-generation count depends on the detailed shape of $V_\xi(\xi)$ … robustly three over a *factor-of-two variation* in $V_0$ and $\eta_B$. Beyond that range, the count changes. … a prediction of *moderate* robustness." |
| Ch 14 §14.4 Prediction 14.2 / Result 14.3 (`Ch14_FINAL.md` lines 216–230) | **RIGOROUS, structural** | "a *topological* fact about the spectral structure … does not depend on any numerical input … rigorous in the same sense that Ch 13 Result 13.1 is rigorous." |

These cannot both stand. §10.3 says the count is parameter-dependent and stable only over a finite ±factor-of-two window (i.e. it *does* depend on the numerical depth of the double-well); §14.x says the count is a parameter-independent topological invariant. The suggested fix is "pick one; if RIGOROUS, harden the bound-state-count robustness analysis: quantify the parameter window outside which the count fails, and show the stability margin to ±10% variations in $V_0$ and $\eta_B$."

## Why this is AUTHOR-BLOCKED rather than SOLVED

The reconciliation cannot be made from existing work because the Research corpus does **not** support the stronger (RIGOROUS/topological) label, and the robustness margin needed to harden it is not computed anywhere:

1. **The eigenvalue table is not pinned in Research.** Ch 10 §10.3 quotes $\epsilon_1\approx0.11,\ \epsilon_2\approx0.44,\ \epsilon_3\approx0.91$ "from the test suite," but Ch 10 §10.12 (`Ch10_FINAL.md` line 580) itself discloses that **ACTION ITEM Ch10-T1** (the Sturm–Liouville bound-state count test) is **not yet implemented**, so these are "verified only by the standalone research derivations." The specific eigenvalues are not reproduced in `Research/.../06-PARTICLE_MASS_SPECTRUM_V3.md`.

2. **The Research file actively undercuts the "robust topological count" claim.** `06-PARTICLE_MASS_SPECTRUM_V3.md` (OP-03 calibration note, updated 2026-05-11) records the `op03_v0_sweep.py` finding that the symmetric double-well $V(\xi)=V_0(\xi^2-1)^2$ has a **Z₂ symmetry** that forces a bonding/antibonding degeneracy ($y_1\approx y_2$) and that "increasing $V_0$ does not fix the gap." This is an **open problem (OP-03)** in the very potential whose bound-state count Ch 14 calls a clean topological invariant. The shape of $V_\xi$ — and therefore the count — is exactly what is still under investigation.

3. **No factor-of-two / ±10% stability calculation exists to cite.** Hardening §14.x to RIGOROUS requires quantifying the parameter window in which the count is exactly three (and the margin to ±10% in $V_0,\eta_B$). That calculation is flagged but not performed (Ch10-T1; see also Problem P10.2 in `Ch10_FINAL.md` line 592, which *asks the student* to find the range of $V_0\eta_B^2/\hbar^2$ giving exactly three — i.e. the chapter itself treats the window as not-yet-determined). Inventing a margin would violate the hard rule against fabricating physics.

## Author decision required

**Option A (recommended, grounded):** Demote Ch 14 Result 14.3 from "RIGOROUS, structural" to **APPROXIMATE (moderate robustness)**, matching Ch 10 §10.3 and the actual evidentiary state (OP-03 open). The falsification claim ("a 4th generation kills the framework") can be retained, but the *certainty label* should match §10.3's honest "robust over a factor-of-two, not bulletproof." This is the only option fully supported by existing work.

**Option B:** Keep RIGOROUS in Ch 14 *only after* Ch10-T1 is implemented and a parametric-stability table is produced showing the count is exactly three over the physical window with explicit ±10% margins, AND OP-03 (the Z₂-symmetry degeneracy) is resolved so the double-well shape is settled. Until then, Ch 14's RIGOROUS label is an overclaim relative to its own cited source (Ch 10 §10.3).

The author must choose. This editor did **not** silently change the flagship structural claim's rigor label, because (a) it is a position decision on a load-bearing claim and (b) the supporting robustness analysis is genuinely absent from the corpus.

## Grounding citations
- `01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Manuscript/Ch_10_Leptons_and_Quarks_from_Firmament_Resonances/Ch10_FINAL.md` §10.3 (lines 165, 181, 206), §10.12 (line 580), Problem P10.2 (line 592)
- `01_Genesis_Physics/Book_0_The_Foundations/Vol_4_The_Quantum_World/Manuscript/Ch_14_Beyond_the_Standard_Model/Ch14_FINAL.md` §14.4 Prediction 14.2 / Result 14.3 (lines 216–230)
- `01_Genesis_Physics/Research/Mathematical_Models/06_Nuclear_and_Particle_Physics/06-PARTICLE_MASS_SPECTRUM_V3.md` OP-03 calibration note (line ~163) and `op03_v0_sweep.py`
