# #849 (Sharpened) — Junction-Monodromy Derivation Attempt: n_q = 3 from Zone-Junction Counting

**Date:** 2026-06-12
**Hypothesis under test (author, 2026-06-12):** the Waters-Above phase accumulates one quantized unit of U(1)_A monodromy per zone junction traversed on the canonical descent Z₀ → Firmament (Z₂.₂.₂); the descent crosses exactly three junctions; therefore n_q = 3 is imprinted as a Day-2 creation boundary condition and conserved by superselection.
**Target:** the referee-verified sharpened question — a principle in the 6D corpus fixing the total quotient winding of the Ψ_A fiber background to n_q = 3 (covering N = 9), entering through the one door the referee left open: a topological boundary/initial condition imprinted at creation (`Research/Peer_Review/849_nw3_derivation_race/REFEREE_REPORT.md` §"sharpened open question").

---

## VERDICT (stated first, per the honesty standard)

**FAIL — with the gap precisely named.** The hypothesis fails independently at both load-bearing steps:

- **Part A (per-junction monodromy unit): FAIL.** No equation in the corpus endows a zone junction with quantized U(1)_A vorticity. Every junction condition the corpus actually writes — Israel/RS metric junctions, GHY boundary terms, brane tensions, the |Ψ|² boundary potentials, the Dirichlet modulus condition on the Firmament — is **invariant under the global phase rotation Ψ_A → e^{iα}Ψ_A** and therefore *cannot constrain the winding at all*, let alone fix it to ±1 per junction (Theorem A1 below; numerically witnessed by Check 2: a model junction transmits every winding n = 1, 2, 3, 5). Deeper than the absence of a mechanism, there is a **homotopy obstruction** (Theorem A2): winding is read on a closed loop and changes only across vortex cores, never across junction surfaces — "one unit per junction crossed" conflates an open-path phase integral (real-valued, unquantized, gauge-dependent) with a closed-loop degree (quantized, junction-count-independent). Crossing N junctions deposits exactly 0 (Check 3).
- **Part B (the junction count = 3 is forced): NUMEROLOGY.** Under six defensible counting conventions the descent count is {2, 3, 3′, 4}: the count 3 emerges only under curated conventions, the two conventions yielding 3 yield **different junction sets**, and the physically-relevant convention — interfaces the Ψ_A phase can actually traverse, given that Ψ_A is not even defined on Z₀ or Z₁ — gives **2** (Check 4, table in §B.2). Z₀|Z₁ is moreover absent from the canonical boundary registry (Zone_Architecture Table 4), so the author's candidate list mixes op01's brane with Table 4 rows at inconsistent granularity.
- **Internal self-cancellation (kill shot):** the only per-junction unit with any orbifold motivation is a Z₃ twist — and three Z₃ twists compose to ω³ = 1, the *untwisted* condition (which is already canon-recommended as Team Beta's N2): zero winding information, not n_q = 3 (Check 5). The alternative reading (a full 2π quotient unit per junction) has no corpus motivation whatsoever. The two sub-versions of the hypothesis are mutually exclusive and each fails separately.

**What survives:** the *form* of the salvage is correct. A creation boundary condition n_q = 3 IS superselection-compatible (referee result), DOES feed the verified equivariant-index machinery (n_q = 3 ⇒ N = 9 ⇒ index = 3 per Z₃ sector, re-verified exactly in Check 1), and collides with neither U(1)_Y nor color. What this attempt shows is that *junction counting does not derive that boundary condition* — it would have to be adopted directly as the (re-founded) Postulate F: "**at creation (Day 2, the dividing of the waters), the Waters-Above background is imprinted with quotient winding n_q = 3.**" That re-foundation is recommended (§D); it is one axiom, equal in strength to the current Postulate F but stated at the correct (quotient) normalization and at the correct logical location (a boundary condition, which superselection then conserves). The triadic resonances of the architecture (3 primary zones, 3 Firmament-Domain siblings, depth-3 membrane) remain what `AXIOM_GODHEAD_ZONE_Z0.md` §0 already calls them: **resonance, not derivation.**

---

## 0. Assumptions Table

| # | Assumption | Status | Source / what would establish it |
|---|------------|--------|----------------------------------|
| E1 | 6D manifold M⁶ = M⁴ × F², fiber (ξ, η); Z₃ orbifold w = ξ+iη ~ ωw, Firmament at the apex | EXISTING | `AXIOM_6D_SPACETIME.md`; `ACTION_6D_COMPLETE.md` §1.1–1.2; `RT2_SU3_Z3_ORBIFOLD.md` (SU3.1–SU3.7) |
| E2 | Ψ_A complex with vacuum S¹; π₁ winding is Postulate F's operational winding; generation loop = link of the Z₃ apex (race N1, directionally approved) | EXISTING | `AXIOM_GODHEAD_ZONE_Z0.md` §4 winding-class note; race Beta A3/A6/N1 |
| E3 | Ψ_A is Z₃-untwisted (race N2, three-way supported) | EXISTING (recommended canon) | race Beta N2 (+referee); `AXIOM_WATERS_DUALITY.md` no-SM-coupling |
| E4 | Boundary winding is superselected: a winding fixed at creation is conserved forever | EXISTING (referee-proved) | `REFEREE_REPORT.md` §3 ("winding at infinity is superselected") |
| E5 | Equivariant index: per-sector index = N/3 = n_q for N ∈ 3ℤ; characters distinct, no escape (H²(Z₃,U(1)) = 0) | EXISTING (referee-proved) | `REFEREE_REPORT.md` §1; race Beta eq. (B6)–(B8); re-verified Check 1 |
| E6 | Corpus junction conditions: [g] = 0, [K_μν] = κ₆²σγ_μν (Israel/RS); GHY term; brane tensions σ = 5k₁M⁴ (Z₀\|Z₁); boundary potentials g_bdy δ(η−η_B)Ψ_B², g′_bdy δ(ξ−ξ_A)Ψ_A²; Ψ_A\|_Firm = v_A^Firm | EXISTING — **the complete junction inventory** | `ACTION_6D_COMPLETE.md` §3.3, §4, §8.2, §11.1–11.3; `AXIOM_METRIC_DISCONTINUITY.md` (junction conditions); `op00_z0_action.py` §2, `op01_z0_axiom_statement.md` (σ) |
| E7 | Canonical descent / sustaining chain Z₀ → Z₁ → Z₂; zone tree per Zone_Architecture Tables 1, 4; boundary registry Table 4 | EXISTING | `op01_z0_axiom_statement.md` (chain); `Zone_Architecture.md` Tables 1, 4; `Glossary.md` (Z₀ → Z₁ → Z₂) |
| **H1** | **Each zone junction forces exactly ±1 quantized unit of U(1)_A monodromy on Ψ_A** | **NEW — REFUTED in §A** (Theorems A1–A2; Checks 2–3). What would establish it: a new axiom assigning each junction a unit U(1)_A vortex sheet — itself unsupported and (for the Z₃-unit reading) self-cancelling |
| **H2** | **The descent crosses exactly 3 junctions, forced** | **NEW — REFUTED in §B** (convention-dependent: {2, 3, 3′, 4}; Check 4) |

Existing assumptions used: 7 (all with file citations). New assumptions required by the hypothesis: 2 (H1, H2) — **both refuted**. The integer 3 enters the analysis only via E1's color-grounded Z₃ and via H2's junction count (tested and found unforced); no "we need 3 generations" input anywhere.

---

## Part A — Is there a per-junction monodromy unit? **NO (the make-or-break step fails)**

### A.1 The complete junction inventory and its phase-blindness

The corpus's junction physics, exhaustively (E6):

1. **Israel/RS metric junction** (`ACTION_6D_COMPLETE.md` §11.1; `AXIOM_METRIC_DISCONTINUITY.md`): [g_AB] = 0, [K_AB] = κ₆²σγ_AB. Constrains the *metric* and the brane tension. Contains no Ψ_A.
2. **GHY boundary term** (§3.3): ∫√(−h)K. Metric only.
3. **Brane tensions** (op00 §2, op01): σ = 5k₁M_{Z0}⁴ at Z₀|Z₁; σ_Firm at the Firmament. Real constants multiplying √(−γ). No Ψ_A phase.
4. **Boundary potentials** (§8.2): g_bdy δ(η−η_B)Ψ_B², g′_bdy δ(ξ−ξ_A)Ψ_A². For complex Ψ_A the canonical reading is |Ψ_A|² (the race's corpus-correction #2/#3 already flags that the action must be U(1)_A-symmetric for any vortex sector to exist at all). |Ψ_A|² is exactly invariant under Ψ_A → e^{iα}Ψ_A.
5. **Brane-localized matching** (§11.1): Ψ_A|_{ξ₀,η₀} = v_A^Firm — a condition on the **modulus**; the phase is unconstrained. (If it were read as fixing the full complex value, it would force winding **zero** on the Firmament — the opposite of the hypothesis — and would contradict the vortex sector entirely; the modulus reading is the only one consistent with Postulate F.)
6. **Field boundary conditions** (§11.2–11.3): Neumann ∂Ψ = 0 / Dirichlet Ψ = 0 / Robin. All linear conditions commuting with the global phase.

**Theorem A1 (phase-blindness).** Every junction/boundary structure in the corpus inventory above is invariant under the global U(1)_A rotation Ψ_A → e^{iα}Ψ_A. Consequently the space of finite-energy configurations satisfying all junction conditions is U(1)_A-invariant and, in particular, **carries every π₁ winding class or none**: junction conditions cannot quantize, select, or source a specific nonzero winding. ∎ (Proof: each item 1–6 is built from g, K, σ, |Ψ_A|², |∂Ψ_A|², or linear phase-covariant conditions; α-invariance is inspection. The winding is a U(1)_A-equivariant homotopy invariant; an α-invariant constraint set that admits one winding-n solution admits it for all α, and admits the analogous solution for every n by the same radial existence theory — witnessed numerically below.)

**Numerical witness (Check 2, `junction_monodromy_checks.py` — all checks pass):** the vortex profile equation with a model zone junction at r_J = 4 (VEV/warp jump 1 → 0.65 **plus** an Israel-type delta tension λ_J = 0.5) was solved by damped Newton to residual < 3.4×10⁻¹¹ for windings n = 1, 2, 3, 5 — a regular finite solution exists for **every** n. The junction transmits all windings; it forces none.

### A.2 The four candidate routes, examined and closed

1. **Phase jump from differing warp across an AdS junction.** Warp factors e^{2A}, e^{2B} (`KK_DIMENSIONAL_REDUCTION.md` eq. 1.1) are *real* and couple to |Ψ_A| and the measure. A real conformal/warp mismatch rescales the modulus profile and shifts mode masses; it cannot rotate the phase, because the phase enters the action only through |∂Ψ_A|² (and the index is conformally robust — race Beta §4.3). **Closed: no phase content.**
2. **Flux quantization of an associated 2-form through the junction 2-cycle.** The corpus contains no 2-form gauge field for Ψ_A, and U(1)_A's gauging is itself an unresolved item (race N3: op02's *twisted* operator half-commits; nothing more is written). Even granting a gauged U(1)_A: flux quantization quantizes total flux through a *closed* 2-cycle — it assigns nothing per junction unless each junction brane carries a specified localized Chern number, and no tadpole/anomaly-inflow computation exists in the corpus to fix per-brane flux to 1 (or to anything). Assigning it by hand is H1 restated, i.e. a new axiom. Also geometric mismatch: junctions are codimension-1 walls (5D hypersurfaces at ξ = ξ_A etc.); there is no canonical 2-cycle "through" them linking the apex circle. **Closed: structure absent; would-be fix = axiom.**
3. **Z₃-twisted boundary condition per interface.** Two fatal problems. (i) *Direction mismatch:* a Z₃ twist is a boundary condition in the **angular** (ψ) direction around the apex; junctions are surfaces at fixed **radial-type** coordinates (ξ = ξ_A, η = η_B, ρ = ρ_J). A condition imposed *on* a junction surface constrains Ψ_A on that surface; to encode winding it would have to specify winding-n boundary *data* on the surface's angular cycle — written nowhere. (ii) *Self-cancellation:* even granting one Z₃ unit per junction, three junctions give ω³ = 1 — the **untwisted** condition, which is precisely the already-recommended N2 and carries **zero** winding information (Check 5). The covering/quotient bookkeeping cannot rescue this: a Z₃ twist is a fractional (1/3) covering winding offset, so 3 of them = 1 full covering unit = quotient winding **1/3 of one quotient unit per three junctions** — under no normalization does "3 junctions" produce n_q = 3 (it produces twist 0, equivalently an integer-winding sector with no preferred integer). **Closed: wrong direction, and the arithmetic self-destructs.**
4. **Index/spectral flow across the junction.** Spectral flow requires a one-parameter family of operators interpolating across the junction with a specified twisting; the corpus defines no such family, and the equivariant index (E5) depends only on the **total** quotient winding — it is exactly the quantity the hypothesis is supposed to determine, so any "spectral flow fixes it" argument is circular without an independent per-junction twist (which is route 3, closed). **Closed.**

### A.3 The homotopy obstruction (why no route could have worked as stated)

**Theorem A2 (non-accumulation).** Let Ψ_A be continuous and nonvanishing on a region containing nested loops C_in, C_out and the annulus between them, and let any number of junction surfaces lie in that annulus. Then winding(C_out) = winding(C_in), independent of the number of junctions crossed. Winding changes only across zeros (vortex cores) of Ψ_A. ∎ (Standard degree theory: n(C) = (1/2π)∮_C d arg Ψ_A is a homotopy invariant of C in the domain where Ψ_A ≠ 0; junction surfaces, being phase-blind by Theorem A1, do not remove points from that domain.)

The hypothesis's picture — "the phase accumulates one unit per junction *traversed on the descent*" — conflates two different integrals:
- the **open-path** integral ∫_descent d arg Ψ_A along the radial/sustaining descent: real-valued, **not quantized**, changed by global rotations, and not the quantity any observable reads;
- the **closed-loop** degree ∮_{C_ρ} d arg Ψ_A: quantized, superselected, the input to the index — but a *single integer for the configuration*, not a sum of per-junction contributions.

For junction crossings to deposit winding, each junction would have to carry a quantized **vortex sheet** (interface-localized vorticity, δ-function in d(d arg Ψ_A) supported on the wall). No corpus equation provides one. **Numerical witness (Check 3):** on the referee's exactly Z₃-invariant background Ψ = w³ − w₀³ (untwisted, quotient charge 1), the measured covering winding is 0 inside the core radius and 3 outside, **identical whether the descent to the loop crosses 0 or 3 hypothetical junction surfaces** placed in core-free shells.

Additionally, a **domain-of-definition failure** for the descent's first two junctions: Ψ_A is a field on M⁶ — the Z₂ manifold — sourced in Zone 2.3 (`AXIOM_WATERS_DUALITY.md`: J_A(ξ) localized in Zone 2.3; `ACTION_6D_COMPLETE.md` §1.2 zone table). The corpus's Z₀ and Z₁ actions (op00, op01) contain **no Ψ_A term**. "The Ψ_A phase crosses the Z₀|Z₁ junction" is not merely unforced — it is **undefined**: there is no Ψ_A on either side of that junction to carry a phase. The same holds at Z₁|Z₂.₁. The U(1)_A monodromy can only be evaluated where Ψ_A lives: the Waters-Above bulk and the fiber around the apex.

**Part A verdict: FAIL.** The honest gap, named precisely: *the corpus contains no junction structure that couples to arg Ψ_A; establishing a per-junction unit would require a new axiom ("every zone junction carries a unit U(1)_A vortex sheet"), which is unsupported by any written equation, multiplies rather than reduces axiom count, and in its only orbifold-motivated form (Z₃ unit) composes to the trivial twist.*

---

## Part B — Is the junction count 3 forced? **NO (convention-dependent ⇒ numerology)**

### B.1 The canon interface inventory (confronting the Table 4 gap)

`Zone_Architecture.md` Table 4 (the canonical boundary registry) lists exactly five boundaries: Z₁↔Z₂.₁, Z₂.₁↔Z₂.₂, Z₂.₂.₁↔Z₂.₂.₂.₁, Z₂.₂.₂.₁↔Z₂.₂.₃, Z₂.₂.₃→Z₂.₂. **Z₀↔Z₁ is not in Table 4**; it exists in canon only via op00/op01 ("Brane tension (Z₀/Z₁ boundary): σ = 5k₁M_Planck⁴"). Note also that Table 4 contains **no row "Z₂.₂.₃ ↔ Z₂.₂.₂"** (Waters Above ↔ Firmament membrane) — the closest rows are Z₂.₂.₃→Z₂.₂ (repulsive pressure, into the *domain*, not onto the membrane) and Z₂.₂.₂.₁↔Z₂.₂.₃ (matter–energy, with *condensed matter*, not the membrane). So the author's third junction is also not a registry row as stated. The candidate list {Z₀|Z₁, Z₁|Z₂, Z₂.₂.₃|Z₂.₂.₂} therefore contains **one interface absent from the registry, one coarse-grained pair of registry rows, and one interface that exists in no source** — already a sign of curation.

### B.2 The count under every defensible convention (Check 4)

| Convention | Junction set on the descent Z₀ → Z₂.₂.₂ | Count |
|---|---|---|
| **C1** Author's list | Z₀\|Z₁, Z₁\|Z₂, Z₂.₂.₃\|Z₂.₂.₂ | **3** |
| **C2** Full nested path (every canon interface crossed: Table 4 rows + op01 brane) | Z₀\|Z₁, Z₁\|Z₂.₁, Z₂.₁\|Z₂.₂, Z₂.₂.₃\|Z₂.₂.₂ | **4** |
| **C3** Table 4 registry only (canon's explicit boundary list) | Z₁\|Z₂.₁, Z₂.₁\|Z₂.₂, Z₂.₂.₃→Z₂.₂ | **3** — but a **different set** than C1 |
| **C4** Interfaces the Ψ_A phase can actually traverse (Ψ_A defined only on Z₂; boundary terms at ξ = ξ_A and the Firmament — ACTION_6D §8.2) | ξ = ξ_A, Firmament | **2** |
| **C5** Primary zones Z₀ → Z₁ → Z₂ (the op01 sustaining chain itself) | fenceposts between 3 zones | **2** |
| **C6** Nesting depth of the membrane label Z₂.₂.₂ | (counts subscripts, not junctions) | "3" (notational) |

**The off-by-one risk, confronted:** it is realized. Counting *zones* on the chain gives 3 but *junctions between them* gives 2 (fencepost); counting every canon interface gives 4; counting only where Ψ_A exists gives 2; the membrane's depth-3 label counts notation. The two conventions that produce 3 (C1, C3) disagree about **which** three junctions — C1 needs Z₀|Z₁ (not in Table 4) and drops Z₂.₁|Z₂.₂ (in Table 4); C3 does the reverse. There is no counting rule, statable in advance without knowing the answer, under which the architecture forces 3. By the project's own standard (`AXIOM_GODHEAD_ZONE_Z0.md` §0: "presenting it as the derivation … would be numerology, which this framework's standard forbids"):

**Part B verdict: NUMEROLOGY.** The repeating triads (3 primary zones; 3 Firmament-Domain siblings Z₂.₂.₁|Z₂.₂.₂|Z₂.₂.₃; depth-3 membrane) are real structural resonances of the architecture — but they count *zones, siblings, and subscript levels*, three different object types, none of which is "junctions the Ψ_A phase must cross."

---

## Part C — Consistency of the salvageable core

Even though the junction *derivation* fails, the target it aimed at remains well-posed. For the record (and for the re-foundation in §D):

**(i) Superselection compatibility — SOUND.** The referee proved boundary winding is superselected (REFEREE_REPORT §3): finite-energy dynamics cannot change it, so a value imprinted as a creation boundary condition (Day 2) is conserved for all subsequent cosmic history. This is exactly the door the referee left open. A boundary-condition axiom n_q = 3 walks through it; the junction-counting argument was an attempt to *derive* the boundary condition and does not.

**(ii) Covering/quotient bookkeeping — VERIFIED (Check 1, exact roots of unity).** n_q = 3 on the quotient = N = 9 on the covering (N = 3n_q, race eq. B3). Lefschetz: ind(1) = 9, ind(g) = ind(g²) = 0 (< 2.1×10⁻¹⁵), per-sector equivariant index = **3 in every Z₃ sector** — 3 color-singlet generations plus colored partners, 9 = 3 colors × 3 generations from the one color-grounded Z₃, regardless of how the 9 covering cores are spatially distributed (index is topological; coincident-core fragmentation is harmless — referee §sharpened question). The factor-3 double-count that killed the original #849 sketch is avoided by stating the axiom **in quotient units (n_q), never covering units**.

**(iii) No collision with U(1)_Y or color.** Unchanged from the race's verified resolutions: hypercharge is a KK-*momentum* label on the ξ-circle (Ch 06 §6.2), the generation winding is a field-phase *degree* on the apex link — different quantum-number types on different cycles, with the residual overlap consistent via the SM's Z₆ center (race Beta §2.2). Color enters as the Z₃ *characters* grading the 9 modes (3 per sector), not as extra winding. Provisos (a)–(b) of the referee's sharpened question (fiber-topology ratification; gauge only the discrete Z₃) carry over verbatim and remain open ratification items, not new gaps introduced here.

**(iv) Scripture — canon citations only, no new numerology.** The zone architecture's Genesis grounding is already canon: Gen 1:6–8 (Day 2, Firmament divides the waters) grounds the Z₂.₂.₁/Z₂.₂.₂/Z₂.₂.₃ structure (`Biblical_References.md` Day-2 row; `Zone_Architecture.md` Tables 3, 5; `RT2_SU3_Z3_ORBIFOLD.md` §6); the Day-2 creation event at t ~ 10⁻³⁶ s is when the zone boundaries (and any boundary-condition data on them) are fixed (`AXIOM_METRIC_DISCONTINUITY.md`: Firmament properties "established during the creation epoch and fixed at the Sabbath Boundary"; `AXIOM_WATERS_DUALITY.md`: "Waters field configurations were established during the creation epoch"). Timing a winding boundary condition at Day 2 is therefore consistent with existing canon. **No new scriptural number-mapping is introduced; in particular this analysis does not claim Scripture encodes "3 junctions" — it cannot, since §B shows the architecture itself does not.**

---

## D. Recommended disposition (for the author / board)

1. **Mark the junction-monodromy mechanism CLOSED-NEGATIVE** on the board (#849 sharpened thread), recorded reasons: Theorem A1 (junction phase-blindness — no corpus equation couples to arg Ψ_A), Theorem A2 + Check 3 (winding cannot accumulate across junctions without interface vorticity, which nothing provides), Check 5 (the Z₃-unit reading self-cancels to the untwisted condition), Check 4 (count 3 convention-dependent: {2, 3, 3′, 4}).
2. **Adopt the salvage as the re-founded Postulate F** (one axiom, correctly normalized and located): *"At creation (Day 2), the Waters-Above fiber background is imprinted with total quotient winding n_q = 3; superselection conserves it."* Given it, Check 1 + the referee's verified machinery yield 3 color-singlet generations + colored partners (9 = 3×3) with no further input. This is **not weaker honesty than today's canon** — it is the same single topological axiom, but stated in quotient units (avoiding the covering double-count), as a boundary condition (compatible with the superselection theorem), and at the structural point where the Trinity *resonance* may be noted as resonance, exactly per `AXIOM_GODHEAD_ZONE_Z0.md` §0's standard.
3. **Honest framing for the books:** the trail of refuted mechanisms (energetic selection — refuted; junction counting — refuted here) is itself evidence the framework enforces its no-numerology rule. State it.

## E. Weakest link of THIS analysis (referee guidance)

The strongest place to push back is **Theorem A1's claim of exhaustiveness**: it covers every junction structure *written* in the corpus (E6 inventory), but the corpus is not closed — e.g., if U(1)_A were gauged (race N3) *and* zone branes were later assigned localized U(1)_A charge/flux by a new anomaly-inflow or tadpole computation, route A.2-2 would reopen with per-brane units fixed by consistency rather than by hand. No such computation exists today, and constructing one would itself be the new derivation (and would still face Part B's count problem: 2 branes carry Ψ_A boundary terms, not 3). Second-weakest: C2/C3's treatment of "entering Z₂ through Z₂.₁" relies on Table 4's row ordering (Z₁↔Z₂.₁ then Z₂.₁↔Z₂.₂) — but every alternative reading only adds more values to the count set {2, 3, 4}, strengthening, not weakening, the numerology verdict.

---

## Appendix — Numerical checks

Script: `C:/Users/J Raymond/AppData/Local/Temp/junction_monodromy_checks.py` (pure Python 3.12, math/cmath only, same style as the race scripts; **ALL CHECKS PASS**, run 2026-06-12):

- **Check 1** — exact Lefschetz: N = 9 ⇒ |ind(g)|, |ind(g²)| < 2.1×10⁻¹⁵, per-sector index = 3.000000 in all three sectors (and N = 3 ⇒ 1 per sector, matching the race).
- **Check 2** — model junction (VEV jump 1→0.65 at r_J = 4 + Israel delta tension λ_J = 0.5): damped-Newton solutions with residual ≤ 3.4×10⁻¹¹, regular and positive, for n = 1, 2, 3, 5 — every winding transmitted, none selected.
- **Check 3** — Ψ = w³ − w₀³ (referee's untwisted quotient-charge-1 witness): covering winding +0.000000 / +3.000000 on loops inside/outside the cores, **identical with 0 or 3 junction surfaces crossed** on the descent.
- **Check 4** — junction-count table: distinct counts {2, 3, 4} across six conventions; the two "3" conventions disagree on the junction set.
- **Check 5** — ω³ = 1 exactly: three Z₃ units = untwisted = zero winding information.

*No repository file was modified. Deliverables: this document + check script in `C:/Users/J Raymond/AppData/Local/Temp/`.*
