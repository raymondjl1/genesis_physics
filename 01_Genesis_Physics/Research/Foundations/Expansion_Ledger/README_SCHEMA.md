# Expansion Ledger — Schema & Rules (read before tracing)

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This defines the row format every per-domain ledger uses and the honesty rules every trace
> must obey. Reference docs: `SPINE.md` (rungs S0–S9), `DECREE_REGISTER.md` (decrees D0–D6).

## Goal

For **every equation** in the theory, show a trace that **starts at `1=1` (S0)** and reaches the
equation, citing spine rungs + decrees + equation-specific algebra. The ledger lets a reader
start from unity and walk to any equation in the framework.

## Row format (one block per equation)

```
### EQ-<DOMAIN>-<NN> — <short name>
- **Equation:** <the equation, ASCII or LaTeX-ish>
- **Source:** <file path> (<section / line / eq number if any>)
- **Spine path:** S0→S1→…→S<k>   (the ordered rungs it stands on)
- **Decrees:** D<x>, D<y>  (or “none beyond D0”)
- **Trace:** 1=1 → … → <equation>.  (1–4 sentences: the actual steps from the top cited rung
  to the result. Cite *what each decree injects and where*.)
- **Constants:** <each constant tagged> [DERIVED ratio] / [SELECTED scale → D4] / [FIT → D5] / [count → D3]
- **Status:** DERIVED-as-form | DERIVED-given-decrees | PARTIAL | UNTRACEABLE
```

## Worked example (the canonical template — copy this style)

```
### EQ-FND-01 — Energy–momentum conservation
- **Equation:** ∂_μ T^μν = 0
- **Source:** Research/Foundations/FIVE_PRINCIPLES_FORMALIZED.md (eq. 2.11)
- **Spine path:** S0→S1→S6→S7
- **Decrees:** D1 (a manifold to translate along)
- **Trace:** 1=1 → S1 gives the additive “books-balance” form a+(−a)=0 (conservation) →
  S6 supplies the operator ∂_μ → S7 (Noether) ties the action’s time-translation symmetry to a
  conserved current; applied to T^μν this is ∂_μ T^μν = 0. The only non-grammar input is D1
  (that there is a spacetime to translate in).
- **Constants:** none dimensionful.
- **Status:** DERIVED-as-form (given D1).
```

## Honesty rules (mandatory)

1. **No equation is “derived from `1=1` alone.”** Every physics equation = spine + decrees.
   Always list the decrees. Claiming otherwise is the numerology the project forbids.
2. **Tag every constant.** Dimensionful ⇒ `[SELECTED scale → D4]`. Dimensionless ratio from
   geometry/topology ⇒ `[DERIVED ratio]`. Matched-to-data ⇒ `[FIT → D5]`. Integer count ⇒ `[count → D3]`.
3. **Cite rungs; never re-derive arithmetic.** “S2” *is* the derivation of ℚ — don’t repeat it.
4. **If you can’t trace it, mark it UNTRACEABLE** with the reason. Do not fabricate a chain.
5. **Skip non-equations.** Trace displayed/numbered equations and named key results only. Skip
   prose, tables of values, and code scaffolding (but DO trace equations embedded in `.py` files).
6. **Skip archives.** Ignore any `00_Archive/`, `Archive/`, `__pycache__/`, and the
   `Expansion_Ledger/` folder itself.

## What each domain agent produces

- One file: `LEDGER_<NN>_<domain>.md` in `Foundations/Expansion_Ledger/`, beginning with the
  UNRATIFIED status banner, then all equation blocks for that domain.
- A short header table: # equations, decrees used across the domain, # UNTRACEABLE.

*Cross-ref: `SPINE.md`, `DECREE_REGISTER.md`, `EXPANSION_HYPOTHESIS_ANALYSIS.md`.*
