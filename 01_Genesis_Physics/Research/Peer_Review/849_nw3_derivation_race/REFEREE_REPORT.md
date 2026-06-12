# Referee Report — #849 Two-Team Derivation Race: n_w = 3 from Z₃ + Energetics

**Date:** 2026-06-12
**Procedure:** Two independent teams (Alpha: equivariant-index/geometry lead; Beta: orbifold-field-theory lead) attacked the same problem with no cross-visibility, under no-cheating rules (the integer 3 admissible only via the color-grounded Z₃; every step an equation or a hypothesis-checked theorem; honest FAIL preferred to fudged success). An independent referee then re-derived the shared weakest link from scratch, ran all check scripts, wrote independent numerics (`referee_checks.py`), and adjudicated.

## Outcome

**Both teams independently returned FAIL — and the convergence is genuine, not a shared error.**

### 1. The shared core discovery (referee-confirmed)
The three covering-space Jackiw–Rossi zero modes ψ_k ~ e^{ikθ}, k = 0,1,2, of the N=3 vortex carry exactly the three **distinct** Z₃ characters ω^{m₀−k}. The referee derived the most general background-preserving Z₃ implementation T = e^{icα}·diag(e^{is₁α}, e^{is₂α})·(θ→θ−α), which is a symmetry iff 2c+s₁+s₂ ≡ N−1 (mod 3); **every** admissible choice grades the modes by distinct characters. Escape routes closed:
- **Verdict reversal impossible:** no Wilson-line, spin-lift (g³ = (−1)^F only permutes sector labels), or projective choice (H²(Z₃,U(1)) = 0 — Schur multiplier of cyclic groups is trivial; and even a projective phase would be mode-independent) can put all 3 modes in one sector.
- **Sector mixing impossible:** the modes are non-degenerate eigenstates of the rotation that defines the quotient; off-apex cores force the regular representation (one copy of each character per orbit).
- Lefschetz bookkeeping verified by exact roots-of-unity arithmetic: ind(g) = ind(g²) = 0; **per-sector index = N/3**.

**Consequence:** the minimal allowed vortex carries **one** color-singlet generation, not three. The original #849 sketch's "index = 3" conflated covering-space and quotient bookkeeping (a factor-3 double-count).

### 2. The decisive original result (Team Beta, referee-verified constructively)
"Windings 1 and 2 are forbidden" is physically empty: **every quotient winding n ∈ ℤ is realized off-apex** by Z₃-image triples. Referee construction: Ψ ∝ (w³ − w₀³) is exactly Z₃-invariant (untwisted; deviation 1.7×10⁻¹¹) with quotient charge 1 and no apex core. This refutes both the sketch's confinement claim ("3 cannot split because 1, 2 are confined") and Alpha's stability proposition.

### 3. Step 2 (energetics) was misconceived in principle
Winding at infinity is **superselected** — finite-energy dynamics cannot change it — so energetics could never have "selected" a sector; it decides only the spatial arrangement within one. Additionally (grid-verified): the cone apex *repels* winding (apex N=3: 338.6 vs off-apex triple at d=100: 145.2, monotone decreasing), and the gauged branch has no selective regime.

## Final verdict for #849: mechanism REFUTED (closed-negative)
**n_w = 3 stands as the honest adopted axiom (Postulate F)**, exactly as `AXIOM_GODHEAD_ZONE_Z0.md` frames it.

## The sharpened open question (the genuine salvage — referee-verified sound)
> **Find a principle within the 6D corpus that fixes the total quotient (boundary) winding of the Waters-Above fiber background to n_q = 3 (covering N = 9).** Energetics cannot supply it (superselection; and coincident N=9 fragments harmlessly — the index is topological). Given n_q = 3, however the cores are distributed, the Z₃-equivariant index automatically yields **exactly 3 color-singlet generations plus their colored partners (3 per sector; 9 = 3 × 3)** — dissolving the 9-problem (3 colors × 3 generations from ONE triadic structure) — provided (a) the fiber topology is ratified so the apex loop and the hypercharge cycle are distinct, and (b) only the *discrete* Z₃ of the fiber rotation is gauged (as color triality); gauging the continuous rotation would break generation universality.

## Scores
| Criterion | Alpha | Beta |
|---|---|---|
| Rigor | 8/10 (best character derivation; Prop 3 false as stated — missed off-apex channel) | 9/10 (decisive off-apex insight; B5 asserted not derived; §5 wording overbroad) |
| Completeness (O1–O5) | 9/10 | 10/10 |
| Honesty | 10/10 | 10/10 |
| Minimality of new assumptions | 9/10 | 9/10 |
| **Total** | **36/40** | **38/40 — WINNER** |

No-cheating audit: **clean on both sides** — scripts reproduce, no smuggled 3's, theorem hypotheses verified, corpus citations accurate. Two demerits (one each) noted above; neither affects the verdict.

## Corpus corrections surfaced (carried to board #852)
1. `TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md` §1.3: E ∝ |n| should be E ∝ n² (global-vortex scaling; Ch 10 eq. 4.10.12 is correct).
2. `ACTION_6D_COMPLETE.md`: the linear G_int·Ψ_A·Ψ_B coupling explicitly breaks U(1)_A (domain walls would destroy the vortex sector); requires the |Ψ_A|²Ψ_B form.
3. `ACTION_6D_COMPLETE.md` declares Ψ_A **real** vs the complex Ψ_A = v_A e^{iθ_A} used everywhere downstream.
4. `KK_DIMENSIONAL_REDUCTION.md`: ξ/η ↔ U(1)_Y/SU(2) gauge-assignment swap vs Ch 06.
5. Ch 06 §6.4.2's region-restricted Z₃ vs RT2's full-fiber Z₃.
6. O5 disentanglement (both teams, identical): charge winding (per-particle defect lines, Q = n·e) and the generation-counting fiber winding are **two distinct π₁ invariants** — notation must separate them.

**Race artifacts:** `TEAM_ALPHA_derivation.md`, `TEAM_BETA_derivation.md`, `team_alpha_checks.py`, `team_beta_checks.py`, `referee_checks.py` (this folder). All scripts run and pass with Python 3.12.
