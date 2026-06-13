# #849 (Third Mechanism Family) — Zone-Address Hypothesis: Generation = Zone-of-Origin Depth

**Date:** 2026-06-12
**Hypothesis under test (author's refined "zone address" idea, formalized):** the three fermion generations are one and the same mode trapped, Jackiw–Rebbi style, at three different depths of the zone-hierarchy descent — a chiral zero mode localized at each zone interface where a REAL field profile (condensate, mass function, warp kink) crosses zero or kinks. The generation index = the wall/level address. If the canonical descent Z₂ → Z₂.₂ → Z₂.₂.₂ (→ Z₂.₂.₂.₁) has exactly 3 trapping interfaces **as a property of the written solutions**, the generation count is derived.
**Why this evades the earlier no-gos (and where it doesn't):** the junction phase-blindness no-go (`849_junction_monodromy_test`) says junction conditions cannot constrain the U(1)_A *phase* — but junctions are **profile-sensitive**: real sign-changing profiles do trap chiral modes (Jackiw–Rebbi 1976), so this family is not killed at the door. It must instead survive (i) the wall **inventory** of the actual corpus solutions, (ii) the **chirality-doubling** problem, and (iii) the off-by-one **count** trap (only solution-property counts admissible).

---

## VERDICT (stated first, per the honesty standard)

**FAIL — on two independent, decisive grounds; with one genuine constructive salvage.**

1. **Part A/C (wall inventory): the written corpus solutions contain exactly ONE trapping wall, not three.** The only sign-changing real profile anywhere in the written field solutions is the Ψ_B condensate kink Φ = tanh(κη′/√2) with its zero **at the Firmament** (op03, exact BVP solution); the warp-A kink (RT-1.WF Israel conditions) sits at the **same** surface. The interfaces Z₂|Z₂.₂ and Z₂.₂.₂|Z₂.₂.₂.₁ have **no written profile at all** (the first has no fields defined on the atemporal side; the second is not even a surface in (ξ,η) — condensed matter is a Day-3 phase *on* the membrane). The outer interfaces ξ_A, η_B carry δ-function modulus potentials and asymptotic conditions — no sign change. Count from solutions: **1** (Check 5). Reporting it honestly: that is not "3 with conventions to argue about"; it is 1.
2. **Part B (chirality): even granting three walls, a single real profile can NEVER trap three same-chirality modes — a theorem, not a tuning failure.** For the 1D Dirac operator in background m(y), the net chiral index is ½[sgn m(+∞) − sgn m(−∞)] ∈ {−1, 0, +1} (Callias/Jackiw–Rebbi; elementary proof in §B.3). Sign changes of a continuous function alternate up/down (IVT), so three crossings = kink–antikink–kink = **one chiral zero mode + one vector-like pair** that pairs up and gaps out (numerically verified: pair splitting ±ε with ⟨σ₃⟩ mixed, Check 3; 200-random-profile lemma sweep, Check 4). Three same-chirality walls would require **three independent profile fields with same-sign crossings** — three new axioms about field content that exist nowhere in the corpus, and which would also break "one and the same mode at three depths" (three different fields trap three different modes). The hypothesis fails *as a generation-count mechanism* in principle, independent of the inventory.
3. **The constructive salvage (real, and corpus-verified):** the **one** wall the solutions do contain is a genuine Jackiw–Rebbi derivation of something the corpus previously asserted by boundary condition: **chiral fermion localization on the Firmament membrane** (ACTION_6D §11.1's "light chiral fermions on the Firmament" upgraded from assumption to consequence of the op03 kink + Yukawa coupling; Check 2: exactly one zero mode, single chirality, analytic profile cosh^(−g√2/κ) matched to 9.8×10⁻⁷). And the author's "address" intuition survives **relocated**: the three *verified* generations (op02 v2 vortex zero modes ψ_k ~ r^k e^(−∫f), k = 0,1,2) already sit at three distinct **radial addresses in the fiber** — same wall, increasing peak radius — which is exactly the geometric input the exp(−αn²) Yukawa-overlap story needs (Check 7, model-profile feasibility). The address is radial-within-the-fiber, not depth-in-the-zone-tree.

**Classification: FAIL (Part A inventory = 1 wall; Part B chirality theorem caps net count at 1) — not NUMEROLOGY** (to its credit, the hypothesis's count criterion was honestly solution-anchored; the solutions just answer "1").

---

## 0. Assumptions Table

| # | Assumption | Status | Source / what would establish it |
|---|------------|--------|----------------------------------|
| E1 | 6D manifold M⁴ × (ξ,η); zone domains; Firmament at (ξ₀, η₀) | EXISTING | `AXIOM_6D_SPACETIME.md`; `ACTION_6D_COMPLETE.md` §1.2 |
| E2 | Ψ_B Mexican-hat sector: V_B = −(μ_B²/2)Ψ_B² + (λ_B/4!)Ψ_B⁴; VEV v_B; Firmament BC Ψ_B|_Σ = 0 | EXISTING | `ACTION_6D_COMPLETE.md` §5.3, §11.1 |
| E3 | Ψ_B condensate kink: Φ(η′) = tanh(κη′/√2), Φ(0) = 0 at the Firmament, Φ → 1 in the WB bulk; slope κ/√2; V₀ = κ²/2 derived | EXISTING (exact written solution) | `op03_condensate_bvp_solve.py` §2–3 (sign typo in the written ODE RHS — see §B.1 corpus correction — kink itself correct) |
| E4 | 6D Dirac probe fermion Ψ coupled to backgrounds; Yukawa to condensate g_YB Φ χ̄χ | EXISTING | `ACTION_6D_COMPLETE.md` §7.1, §7.3; `FERMION_EMERGENCE_FROM_MEMBRANE.md` §1.1; op03 Yukawa integrals |
| E5 | Warp solutions: A_ξ = (2/3)ln(ξ₀/ξ), A_η = −κ_B(η−η₀), Israel kinks [∂A] = −κ₆²σ/3 at the Firmament (Z₂-reflection) | EXISTING | `WARP_FUNCTION_DERIVATION_RT1WF.md` §1.4, §2.1–2.3; `B_ETA_WARP_RESOLUTION_OP2WP.md` (canonical B_η ≈ const) |
| E6 | Boundary terms: g_bdy δ(η−η_B)Ψ_B², g′_bdy δ(ξ−ξ_A)|Ψ_A|²; Ψ_A\|_Firm = v_A^Firm (modulus); Neumann/Dirichlet menus | EXISTING | `ACTION_6D_COMPLETE.md` §8.2, §11.1–11.3 |
| E7 | Verified generation machinery: index(D_A) = c₁ = n_w; three same-chirality vortex modes ψ_k ~ r^k e^(−∫f) (Weinberg vanishing); per-Z₃-sector index = n_q | EXISTING (verified) | `op02_kahler_spinor_derivation.md` §4 + `op02_aps_index_computation.py` v2; `849_nw3_derivation_race/REFEREE_REPORT.md` §1 |
| E8 | Zone tree and boundary registry; descent Z₂ → Z₂.₂ → Z₂.₂.₂ (→ Z₂.₂.₂.₁); Z₂.₂.₂.₁ = condensed matter ON the membrane | EXISTING | `Zone_Architecture.md` Tables 1, 4, §9; `Glossary.md`; `RESOLVED_Zone_Numbering_And_Terminology.md` |
| **H1** | **Each descent interface hosts a sign-changing real profile in the written solutions** | **NEW — REFUTED in §A** (inventory = 1: the Firmament only; Check 5) |
| **H2** | **Three trapped modes are same-chirality (so they count as generations)** | **NEW — REFUTED in §B** (1D index theorem: net chiral count ∈ {−1,0,+1} for any single profile; alternating walls give 1 chiral + 1 vector-like pair; Checks 3–4). What would establish it: three NEW independent profile fields with same-sign crossings + a reason the same 4D mode couples to all three — neither written nor motivated anywhere |
| **H3** | **(implicit) The trapped wall modes are the same object as the op02 spin-½ carriers** | **NEW — UNESTABLISHED, analyzed §D.1** (the wall traps the η-localization factor; the generation-bearing structure is the fiber vortex index — orthogonal factors of one wavefunction, not rivals; but then walls label *localization*, not *generation*) |

Existing: 8 (all file-cited). New required by the hypothesis: 3 — two refuted, one unestablished. The integer 3 enters this analysis only through E7's verified vortex index (where it is Postulate F's adopted n_q) — never through "we need 3."

---

## Part A — Inventory of real trapping structures in the WRITTEN solutions

### A.1 What counts (the admissibility rule, fixed in advance)

A "trapping wall" is admissible iff (i) a **real** field profile (condensate, fermion mass function, or warp derivative) is **written in the corpus as a solution** (not a hypothetical), and (ii) that profile **changes sign** (Jackiw–Rebbi) or has the kink structure required to bind a normalizable Dirac zero mode at that locus. U(1)_A-phase structures are excluded (phase-blindness no-go applies to them, not to profiles); bookkeeping interfaces with no written profile are excluded (that exclusion is exactly what the junction-monodromy FAIL teaches).

### A.2 The inventory (Check 5)

| Descent interface | Coordinates | Written profile there? | Sign change / kink? | Trapping wall? |
|---|---|---|---|---|
| Z₂ \| Z₂.₂ (Earth Prime → Firmament Domain; registry rows Z₁↔Z₂.₁, Z₂.₁↔Z₂.₂) | none written | **None.** No field equations exist on the Z₂.₁ (atemporal) side; Ψ_A, Ψ_B, warp all undefined there (op00/op01 contain no Waters terms; `Zone_Architecture.md` Table 1 marks Z₂.₁ atemporal) | — | **NO** |
| Z₂.₂ \| Z₂.₂.₂ (domain → membrane) = **the Firmament surface** | η′ = 0 (and (ξ₀,η₀)) | **Ψ_B kink** Φ = tanh(κη′/√2), Φ(0) = 0 — exact BVP solution (op03); **warp-A kink** [∂_ξA] = [∂_ηA] = −κ₆²σ/3 with Z₂ reflection (RT-1.WF §2.3) | **YES** — Φ crosses zero at η′ = 0 (odd extension under the RT-1.WF Z₂ reflection); A′ flips sign | **YES — the one wall** |
| Z₂.₂.₂ \| Z₂.₂.₂.₁ (membrane → condensed matter) | not a surface in (ξ,η) | **None.** Z₂.₂.₂.₁ is baryonic matter condensed ON the membrane (Day 3 phase transition; `Zone_Architecture.md` Table 1, §9; `RESOLVED_Zone_Numbering...`); there is no transverse coordinate to profile | — | **NO** |
| ξ = ξ_A (Waters Above outer interface) | ξ = ξ_A | δ-potential g′_bdy δ(ξ−ξ_A)\|Ψ_A\|² (ACTION_6D §8.2); Ψ_A → VEV asymptotically (§11.3); A_ξ → flat | \|Ψ_A\| ≥ 0 can touch but never **sign-change**; no kink written | **NO** |
| η = η_B (Waters Below outer interface) | η = η_B | δ-potential g_bdy δ(η−η_B)Ψ_B²; op03's kink has Φ → 1 monotonically (no second crossing); §11.2 offers Neumann/Dirichlet menus, none written as a solved sign change | even the Dirichlet option (Φ returning to 0) is a *turning point*, not a sign change — binds no chiral mode | **NO** |

**Inventory result: exactly 1 trapping wall — the Firmament.** Both real-profile structures the corpus actually solves (the condensate kink and the warp kink) sit at the *same* surface. The "three depths" do not exist in the written solutions. (Note the structural echo of the junction-monodromy Part B: there, the only interfaces Ψ_A could traverse numbered 2; here, the only interface any real profile crosses numbers 1. The architecture's triads persistently fail to materialize as *dynamical* triads.)

### A.3 Why the predecessor "3 wells" does not rescue the inventory

`TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md` Part 4.4 postulates a piecewise three-well V(ξ) ("if the three wells are deep enough…") and App C.4 admits the count holds only in the fine-tuned window 0.1 < λ < 0.5 (λ = depth × width²) — "a fine-tuning or a selection principle," its own words. Two independent problems:
1. **The wells are hypothetical** — no corpus BVP solves for them; they fail the admissibility rule by construction.
2. **The corpus's own later derivation breaks the window.** op03 *derived* V₀ = κ²/2 with κ_req = 21.78 ⇒ V₀ ≈ 237 (η_B units), giving λ = V₀·Δξ² ≈ 21 — outside (0.1, 0.5) by a factor ~40; and the Ch-10 canonical V₀ = 0.002 gives λ = 0.002, *below* the window's own floor (Check 6). The "exactly 3 bound states" claim was never satisfied by any written parameter set, before or after op03. The zone-address hypothesis cannot inherit a topological upgrade of a count that the corpus's own numbers never produced.

---

## Part B — The trapping mechanism (and the chirality kill-shot)

### B.1 The one real wall, solved (the leading candidate verified)

Setup (all corpus-written): 6D Dirac probe Ψ (ACTION_6D §7.1) Yukawa-coupled to the condensate (§7.3; op03's S_Yuk = ∫χ* g_YB Φ χ). In the η-direction the effective 1D mass profile is m(η) = g_YB Φ(η) = g_YB tanh(κη/√2) under the odd extension across the Firmament that RT-1.WF §2.3's Z₂ reflection supplies. The 1D Dirac operator H = −iσ₁∂_η + m(η)σ₂ has chiral symmetry {H, σ₃} = 0; zero modes solve ψ′ = ±m ψ:

- ψ₋ ∝ exp(−∫₀^η m) = cosh(κη/√2)^(−g√2/κ) — **normalizable** (one mode, chirality σ₃ = −1);
- ψ₊ ∝ exp(+∫₀^η m) — **not normalizable**.

**Numerics (Check 2, SUSY-pair method):** the chirality-resolved counts come from the partner Schrödinger operators H₋ = −∂² + m² − m′ (ker = chirality −) and H₊ = −∂² + m² + m′ (ker = chirality +), diagonalized at N = 8000 on a Dirichlet box. Result: H₋ lowest eigenvalue 6.2×10⁻⁶ (the zero mode, shifted only by O(h²) discretization) with the next state gapped at 1.01; H₊ lowest 1.01 (no zero mode). Index = 1 − 0 = **1**, chirality (−) only; the numeric zero-mode profile matches the analytic cosh power law to 9.8×10⁻⁷. *(Methodological honesty: a naive square-matrix block discretization of the first-order Dirac operator on a box CANNOT see this index — rank-nullity forces dim ker A = dim ker A†, and we observed exactly the predicted spurious box-edge partner before switching to the SUSY form. The continuum index lives in the operator's domain structure; the second-order formulation restores it on a Dirichlet box.)* **The Firmament wall genuinely traps one chiral zero mode.** This is the salvage of §D.5: membrane localization of chiral matter is now a *derived consequence* of the op03 kink, upgrading ACTION_6D §11.1's asserted boundary condition ("light chiral fermions on the Firmament").

> **Corpus correction (surfaced by Check 1):** `op03_condensate_bvp_solve.py` writes the BVP as Φ″ = κ²(Φ − Φ³); the tanh kink actually solves Φ″ = κ²(Φ³ − Φ) (Mexican-hat EOM sign). The script's own §2 "residual" printout evaluates to ≈ 3.1 at κ = 2 and is mislabeled "finite-difference error." Everything downstream (slope κ/√2, V₀ = κ²/2, wall width) uses the kink itself and is unaffected — but the written ODE sign should be fixed.

### B.2 Chirality doubling at multiple walls (numerical witness)

Granting, arguendo, a descent profile with three sign changes — necessarily kink–antikink–kink (see B.3) — the chirality-resolved spectrum was computed for m(y) = g·tanh(y+a)·tanh(y)·tanh(y−a) at separations a = 3, 4, 5 (Check 3): **ker H₋ = 1, ker H₊ = 0 at every separation** (one chiral zero mode), plus **one pair at ±ε** with ε = 0.137 → 0.052 → 0.019 — falling with separation but finite at any finite separation, and SUSY-matched between H₋ and H₊ to ~10⁻⁴ (the signature of a *paired*, i.e. non-chiral, level; exactly: every E ≠ 0 eigenmode of a chiral Hamiltonian has ⟨σ₃⟩ = 0, since σ₃ maps the E and −E eigenspaces onto each other). The pair is a 4D-massive **vector-like Dirac fermion**, not two further generations. The middle (anti-)wall's mode pairs with one outer mode; only the net survives. Three walls ⇒ 1 generation + 1 heavy vector-like state.

### B.3 The theorem (why no inventory could ever have fixed this)

**Lemma (crossing parity).** A continuous m(y) with m(±∞) ≠ 0 has up-crossings and down-crossings that alternate (IVT): |N_up − N_down| ≤ 1, and N_up − N_down = ½[sgn m(+∞) − sgn m(−∞)]. *(200-random-profile sweep: no counterexample — Check 4.)*

**Theorem (1D Callias/Jackiw–Rebbi index).** index(H) = ½[sgn m(+∞) − sgn m(−∞)] ∈ {−1, 0, +1}. The number of *net chiral* zero modes of a single real mass profile on a line is at most 1, **independent of how many walls the profile has**.

**Consequence for the hypothesis:** "three same-chirality wall modes from one descent profile" is impossible *in principle*. The only repairs are (i) three independent profile fields, each crossing zero once with the same orientation — three new field-content axioms, nowhere written, and fatal to "one and the same mode at three depths" (different fields trap different modes); or (ii) abandoning walls as the count mechanism. This is the wall-mechanism analogue of the equidistribution no-go that killed mechanism family 1: the natural bookkeeping caps the per-structure yield at 1.

*(Why the corpus's verified "3 same-chirality modes" is not a counterexample: op02's three modes are zero modes of the **2D** twisted Dirac operator in a winding-3 **vortex** — the 2D index is c₁ = n_w, unbounded — not of a 1D real wall profile, whose index is capped at ±1. Dimensionality and the U(1) twist, not walls, carry the multiplicity.)*

---

## Part C — Is the count forced to 3? **No: the solutions say 1 (and the theorem says ≤ 1 net)**

The admissibility rule (A.1) was fixed in advance precisely to escape the {2, 3, 3′, 4} convention trap of the junction-monodromy test — and under it the count is **not convention-dependent at all: it is 1**. Confronting the off-by-one checklist explicitly:

- **Does Z₂.₂.₂.₁ (matter) add a 4th wall?** No — it adds zero: it is not a transverse surface (A.2 row 3).
- **Does Z₂\|Z₂.₂ have any profile crossing?** No — no fields are even defined on the far side (A.2 row 1).
- **Do ξ_A / η_B sneak in?** No — modulus δ-potentials and turning points bind no chiral mode (A.2 rows 4–5).
- **Could one re-count to reach 3?** Only by counting the Ψ_B kink, the warp-A_ξ kink, and the warp-A_η kink as three walls — but all three sit at the **same surface** (the Firmament, RT-1.WF JC-ξ/JC-η) and the two warp kinks are components of one Israel condition with a single σ (eq. 2.17–2.20). Counting one surface three times is the exact bookkeeping sin the no-cheating rules forbid.

**Part C verdict: the count is a genuine solution property, and it equals 1.** FAIL is reported as FAIL.

---

## Part D — Consistency with the verified machinery

### D.1 The layering question (Part D-i — the deepest structural point)

What field is trapped, and is the wall mode the *same object* as op02's spin-½ carrier? The corpus's full zero-mode wavefunction factorizes (op02 §3 KK split D̸₆ = D̸₄ ⊗ 1 + γ⁵ ⊗ D̸_⊥):

Ψ(x, ξ, η) ≈ ψ₄D(x) ⊗ [fiber factor: vortex zero mode ψ_k(ρ, θ) ~ ρ^k e^{ikθ} e^(−∫f), k = 0, 1, 2] ⊗ [transverse factor: JR wall profile cosh^(−g√2/κ)(κη′/√2)]

The two factors are **orthogonal roles in one wavefunction, not rival mechanisms**:
- the **wall factor** (this hypothesis's mechanism) carries *localization on the membrane* — it is k-independent, hence **generation-blind**;
- the **fiber factor** (op02's verified mechanism) carries *spin-½ (Kähler), chirality (Weinberg vanishing), and the generation index k*.

So the layering is coherent — the same 6D Dirac probe supplies both factors, and the Kähler structure (op02 Theorem 1) holds for any warp B "regardless of the warp factor," so the spinor bundle exists at the wall — but coherence is exactly what *demotes* the hypothesis: in the corpus's own verified factorization, **the wall answers "where matter sits" and the fiber answers "how many kinds there are."** Walls at other depths (if they existed) would trap modes lacking the vortex factor altogether — no winding background is written off the Firmament fiber — i.e., nothing carries spin-½ generation structure at non-membrane walls. Address-in-the-tree cannot be the generation label without dismantling the verified fiber index.

### D.2 The 9-problem (color ⊗ generation)

Nominally the hypothesis's cleanest win — wall address is manifestly Z₃-blind, so color ⊗ generation independence is automatic — but the win is **vacuous**: any color-blind generation label is automatically independent of color. The race already showed the *non-trivial* version: with n_q = 3 the Z₃-equivariant index gives 3 per sector (9 = 3 × 3 from ONE triadic structure), which **dissolves** the 9-problem rather than merely not aggravating it. The wall mechanism, yielding 1, never even reaches the 9-problem.

### D.3 Postulate F (what would have happened, and what actually happens)

Had the inventory returned 3 same-chirality walls, Postulate F would have been *superseded for counting* by "the descent has 3 trapping walls" — and that statement would itself have been a **theorem of the solutions** (good) resting on three profile-field axioms (bad: axiom count rises from 1 to ≥3, each needing orientation co-alignment that B.3 shows no single field can supply). As it stands: the inventory gives 1, the theorem caps net count at 1, and **the re-founded Postulate F (n_q = 3 imprinted at Day 2, quotient units, superselection-conserved — `AXIOM_GODHEAD_ZONE_Z0.md` recommendation) remains strictly the best honest state.** The zone-address family does not touch it.

### D.4 Mass hierarchy (the bonus, honestly assessed)

The "different depths see different warp ⇒ exponentially split Yukawas" bonus dies with the wall count — but its *radial* cousin is alive and is the genuine salvage: the three **verified** modes ψ_k ~ ρ^k e^(−∫f) peak at strictly increasing radii (Check 7: r_peak = 0, 1.20, 2.07 for a model profile; toy Yukawa overlaps strictly ordered y₀ > y₁ > y₂). This is split-fermion geography (Arkani-Hamed–Schmaltz) **within the fiber**, exactly where the corpus needs it: it would *derive* the geometric input that op03's exp(−αn²) ansatz takes for granted (generation-n displacement n·Δξ), potentially upgrading Δξ = 0.3 from a fitted parameter to a property of the vortex profile — and it must be checked against the honest residuals as facts to match (electron +17%, muon −15…19%, tau anchor; heavier quarks failing at tree level), not beaten. *Not claimed here* — the model profile is not corpus-exact; this is the named deciding computation (§F).

### D.5 What the framework keeps from this test

(i) Chiral localization on the membrane: **derived** (B.1) — one wall, one chiral mode, from the written kink. (ii) A corpus correction: the op03 ODE sign typo + mislabeled residual check (B.1 note). (iii) A sharpened division of labor, now theorem-backed: **walls localize; vortices count** — the 1D index caps walls at ±1, the 2D twisted index c₁ = n_w is where multiplicity lives.

---

## Part E — Scriptural / architectural grounding check

The analysis uses only the existing canon architecture (Zone_Architecture Tables 1, 4, §9; Glossary descent Z₀ → Z₁ → Z₂; the Z₂-subtree) — no new structures, no new number-mappings. Two honest observations, stated as observations:

1. **Genesis 1:6–8 (Day 2) creates ONE dividing surface**: "let it divide the waters from the waters" — one rāqîaʿ between two waters (`Biblical_References.md` Day-2 row; Glossary rāqîaʿ entry). The written physics agrees with the written text: the corpus solutions contain exactly **one** sign-changing wall, and it is the Firmament. If anything, Scripture supports the 1-wall inventory *against* the 3-wall hope. Nothing in the canon text or architecture encodes "three trapping interfaces."
2. The architecture's real triads (3 primary zones; 3 Firmament-Domain siblings; depth-3 membrane label) remain what `AXIOM_GODHEAD_ZONE_Z0.md` §0 calls them — **resonance, not derivation** — and this test adds a third independent confirmation (after the energetics race and the junction count) that the framework's no-numerology rule is doing real work: every mechanism that tried to convert the triads into a dynamical 3 has failed on the corpus's own equations.

---

## F. Frank assessment (required): is this family more promising than the two refuted ones?

**Yes — it was the best-posed of the three, and its autopsy is the most instructive — but it is now closed for the COUNT, with a live descendant for the HIERARCHY.**

- Family 1 (Z₃ + energetics) failed on superselection — wrong *kind* of principle. Family 2 (junction monodromy) failed on phase-blindness + convention-dependent counting — wrong *object* (phases) and no advance-statable count. Family 3 (this) chose the right object (real profiles DO trap chiral modes — verified here on the corpus's own kink) and the right standard (solution-property counting, which returned a definite answer). It fails on facts and a theorem, not on framing: the solutions hold 1 wall, and 1D walls can never net more than 1.
- **The single deciding computation (for the salvage, not the original hypothesis):** compute the corpus-exact Yukawa overlaps y_k = ∫ ψ_k* Φ_B ψ_k for the three verified vortex modes ψ_k of the n = 3 background (op02 v2 profiles, real f(ρ) solved from the vortex BVP) against the op03 condensate kink + RT-1.WF warp measure, and test whether ln y_k ≈ −αk² with α ≈ 0.98 (equivalently: whether the mode peak spacing reproduces Δξ = 0.3 in η_B units). If yes: the mass-hierarchy ansatz is *derived* and the radial-address picture replaces the fine-tuned V₀ well outright. If no: exp(−αn²) stays an honest fit. Either outcome is progress; neither resurrects wall-counting.
- **Weakest link of THIS analysis:** the odd extension of the op03 kink across the Firmament. The written BVP lives on η′ ∈ [0, ∞); the sign change at η′ = 0 exists only under the Z₂ reflection that RT-1.WF §2.3 uses for the warp ("by the Z₂ reflection symmetry typically assumed"). If the author ratifies a one-sided reading instead (no field content at η′ < 0), the Firmament "wall" is a boundary rather than a crossing, the JR mode survives as a boundary-localized mode but the inventory drops from 1 to 0 sign changes — which makes the hypothesis's count *worse*, not better. Second-weakest: the C3/C4 numerics are 1D in η at fixed fiber point; a fully 2D wall+vortex computation could shift profiles quantitatively but cannot evade the index theorem (the 1D cap is topological along any descent line).

## G. Recommended disposition

1. Mark the zone-address mechanism **CLOSED-NEGATIVE for the generation count** on the #849 thread: inventory = 1 wall (Check 5), chirality cap = ±1 per profile (Checks 3–4, theorem B.3).
2. Open two constructive items: (a) **membrane chiral localization as a derived result** (B.1) — candidate for Vol 4, upgrading the §11.1 boundary condition to a theorem, with the op03 ODE sign typo fixed in passing; (b) **the radial-address Yukawa computation** (§F) as the successor task — it tests the author's address intuition in the place the verified machinery actually has addresses.
3. Postulate F (re-founded, quotient units, Day-2 boundary condition) remains the honest adopted axiom; this family neither replaces nor weakens it.

---

## Appendix — Numerical checks

Script: `C:/Users/J Raymond/AppData/Local/Temp/zone_address_checks.py` (numpy, Python 3.12). Run 2026-06-12 — **ALL 7 CHECKS PASS**. Zero-mode counting uses the SUSY-pair operators H∓ = −∂² + m² ∓ m′ (chirality-resolved kernels; see the B.1 methodological note — the naive first-order box discretization provably cannot see the index and was discarded after exhibiting the predicted spurious partner).

- **Check 1** — kink sign audit: tanh residual vs Φ″ = κ²(Φ³−Φ): 1.6×10⁻⁶ (FD level); vs op03's written RHS: 3.08 (O(1) — documented sign typo; downstream V₀ = κ²/2 unaffected).
- **Check 2** — Firmament JR wall: ker H₋ = 1 (E = 6.2×10⁻⁶ vs gap 1.01), ker H₊ = 0 ⇒ index = 1, chirality (−) only; profile matches cosh^(−g√2/κ) to 9.8×10⁻⁷.
- **Check 3** — kink–antikink–kink at a = 3, 4, 5: ker H₋ = 1, ker H₊ = 0 always; vector-like pair at ±ε = 0.137/0.052/0.019 (falling with separation, finite always, SUSY-matched ~10⁻⁴); never 3 chiral modes.
- **Check 4** — 200 random continuous profiles: N_up − N_down = ½[sgn m(+∞) − sgn m(−∞)] ∈ {−1, 0, +1} with no exception.
- **Check 5** — wall inventory over the five descent/outer interfaces: trapping walls in written solutions = **1** (the Firmament).
- **Check 6** — App-C window: λ(derived V₀ = 237.1) = 21.3 ∉ (0.1, 0.5); λ(canonical V₀ = 0.002) = 0.002 ∉ (0.1, 0.5) — the "exactly 3 bound states" window is satisfied by no written parameter set.
- **Check 7** — radial addresses of the verified modes (model profile, flagged): peak radii 0 < 1.20 < 2.07, mean radii 1.19 < 2.10 < 3.04, toy Yukawa ratios 1 : 1/1.51 : 1/2.29 strictly ordered — feasibility for the §F deciding computation only.

*No repository file was modified. Deliverables: this document + check script in `C:/Users/J Raymond/AppData/Local/Temp/`.*
