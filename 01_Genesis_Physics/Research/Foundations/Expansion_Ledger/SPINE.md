# The Derivation Spine — `1=1` unfolded into the grammar of mathematics

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This is the reusable ladder every ledger entry cites. It formalizes
> `EXPANSION_HYPOTHESIS_ANALYSIS.md` into numbered **rungs S0–S9**. Each rung states what
> truth-preserving expansion **forces [DERIVED]** and, where relevant, what **[SELECTED]**
> decree it needs (decrees are enumerated in `DECREE_REGISTER.md`). An equation's trace =
> a path through these rungs + the decrees it invokes + its equation-specific algebra.

The seed is `1 = 1`. The rule is **truth-preserving expansion**: admit exactly those objects
and operations forced by requiring `1` to be re-expressible while remaining `1`, plus the
closure of the system under them.

| Rung | Expansion that forces it | What it **[DERIVED]** produces | Decree needed |
|------|--------------------------|--------------------------------|---------------|
| **S0** | `1 = 1` | the unit `1`; identity `=`; self-reference | — |
| **S1** | `1 = 1 + (1−1)` | `0`, `+`, `−`; succession → **ℕ**; **ℤ**, additive group; the split `a+(−a)` (⇒ **Duality** & **Conservation** forms) | — |
| **S2** | `1 = 1·1 = 1/1` | `·`, `/`, distributivity; ring, field; **ℚ** (ratio / proportion / *Logos*) | — |
| **S3** | unit-square diagonal `x²=1²+1²`; completion | irrationals; order; limits; **ℝ** | **D0** (completed infinity) |
| **S4** | `x² = −1`; algebraic closure | `i`; **ℂ**; rotation; **phase**; the circle; π, e, `e^{iθ}` | — |
| **S5** | independent directions of expansion | vector spaces; **dimension** (a count); matrices; **eigenvalues**; inner product; **Hilbert space** | dimension count is generic; a *specific* dim ⇒ **D1** |
| **S6** | limits on an ℝ-parameter | **derivative**, **integral**, `□` (d'Alembertian); **differential equations**; `δS=0` (variational — borderline, see note) | — |
| **S7** | identity-preserving maps | **groups**, Lie groups, algebras; **Noether** currents; **U(1)** (free from S4); the **SU(N) family** | *which* group ⇒ **D2** |
| **S8** | continuity of phase fields | `π₁(S¹)=ℤ`, `π₃(S²)=ℤ` (**winding/Hopf**); **Chern** `c₁`; **APS / Atiyah–Singer index** (integer invariants) | *which* winding value ⇒ **D3** |
| **S9** | ℂ + metric + symplectic + curvature | Riemannian / Lorentzian / **Kähler** manifolds; curvature `R`; connections; the **RS warp** as a structure | *which* manifold/profile ⇒ **D1**, **D9-profile** |

## Rung notes (for honest citation)

- **S1 is load-bearing for two governing principles.** The split `1 = a + (−a)` is the algebraic
  origin of **Duality** (complementary pair) and of **Conservation** (the parts re-sum to `1`).
  Equations expressing either principle cite **S1**.
- **S3 needs D0.** Finite truth-preserving rewriting reaches **ℚ** only; the jump to **ℝ** grants
  *completed (actual) infinity*. Treat **D0** as a mild decree. Any equation using real-valued
  continua (essentially all of them) silently depends on **D0**; cite it once per entry, not per term.
- **S6 / `δS=0` is the least-secure DERIVED step.** That the *realized* expansion is the
  *stationary* one is attractive ("infinitesimal truth-preservation") but may instead be a
  dynamical decree. Tag action-principle equations `DERIVED-as-form (δS=0 borderline)`.
- **S7 gives the family, not the member.** `U(1)` is free (phase of ℂ). `SU(2)`, `SU(3)` are
  *members* of the derived `SU(N)` family selected by **D2**.
- **S8 gives integer invariants, not their values.** That winding/index are integers is forced;
  *which* integer (e.g. `n_w=3`) is **D3**.

## How to cite a spine path

Write the path as the ordered rungs an equation stands on, then the decrees, e.g.:

> `∂_μ T^μν = 0` — **S0→S1→S6→S7**, decree **D1**. Status: DERIVED-as-form given D1.

Arithmetic, ℝ, ℂ etc. are **never re-derived** in an entry — they are cited by rung ID.

*Cross-ref: `EXPANSION_HYPOTHESIS_ANALYSIS.md` (the prose derivation), `DECREE_REGISTER.md`.*
