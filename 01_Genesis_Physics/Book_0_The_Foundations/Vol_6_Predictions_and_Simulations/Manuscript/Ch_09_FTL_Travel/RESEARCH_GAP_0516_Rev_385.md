# Research Gap — Task 0516_Rev_385 (Issue #485, V6-P1-16)

## Location
Vol 6, Ch 9 §9.2.1 — the load-bearing claim:
> "the $\xi$-direction (Waters Above, Zone 2.3) acts as a cyclic dimension at macroscopic scales (V.4, Ch.6, Eq (4.6.3))."

## What the reviewer asked for
Add 1–2 sentences of physical intuition for ξ-cyclicity at macroscopic scales, e.g.
"Waters Above has finite extent ξ_A; geodesics exiting at ξ_A re-enter at ξ=0 by Vol 4 Ch 6
identification, making the coordinate periodic for paths long enough to wrap."

## Why this is a GAP, not a SOLVE
The suggested intuition presupposes a **periodic / cyclic identification** of the ξ coordinate
(ξ = ξ_A identified with ξ = 0). I checked the cited source:

- **Vol 4, Ch 6, Eq (4.6.3)** (`Book_0/Vol_4_The_Quantum_World/Manuscript/Ch_06_Second_Quantization_and_Zone_Fields/Ch06_FINAL.md`, line 71) is:
  $$-\nabla^2 u_k(x) = |k|^2 u_k(x), \qquad u_k|_{\partial\mathcal{V}} = 0$$
  This is a **Dirichlet (fixed-boundary) eigenvalue problem** on a confined volume $\mathcal{V}$.
  It establishes a *confined standing-wave* mode structure — which is the **opposite** of a
  periodic/cyclic identification. A Dirichlet boundary is not a periodic identification.

Therefore:
1. The forward-cite in Ch 9 §9.2.1 appears to be a **mis-citation**: Eq (4.6.3) does not
   establish ξ-cyclicity.
2. Writing the requested intuition would require asserting a topological identification
   (ξ_A ≡ 0) that is **not derived anywhere in the located Research/Foundations or Vol 4 material**.
   Doing so would invent physics and propagate the mis-citation — barred by the HARD RULES.

Searched: Vol 4 Ch 6 (cyclic/periodic/identif/compact — only Dirichlet found);
Research/Foundations metric/KK files were not found to contain a ξ-periodicity statement
under this label.

## What is needed (for a GitHub research-gap issue)
- Either (a) locate/derive the actual source that makes ξ a cyclic/compact dimension at
  macroscopic scales (with the correct equation label), and correct the Ch 9 §9.2.1 cross-reference; or
- (b) if no such derivation exists, the ξ-cyclicity premise of FTL Mechanism 1 is **unsupported**
  and the §9.2.1 claim must be downgraded from an asserted consequence to an explicit open assumption.

## Status
RESOLVED 2026-06-13 via option (b). FTL Mechanism 1 is speculative (Part B — Conditional Engineering).
§9.2.1 edited: the ξ-closure is now stated as an **explicit open assumption** of Mechanism 1, not a
derived consequence. The mis-citation of Eq (4.6.3) is corrected in place — the text now says
plainly that Eq (4.6.3) establishes a *Dirichlet (confined standing-wave)* structure, which is
mathematically distinct from a periodic/cyclic identification ξ_A ≡ 0, and that no derivation in
Vols 1–5 promotes the confined ξ-extent to a true cyclic dimension (flagged open, → Ch 14). The
unsupported ξ_A ≡ 0 sentence was NOT written. Everything in §9.2 is now explicitly conditional on
the assumption holding.

Remaining (deeper) gap for a future research pass: actually derive (or refute) ξ-closure from the
bulk geometry. Suggested Research home: `Research/Foundations/` (metric / KK identification of the
ξ extra dimension). Until then the assumption stands as flagged.
