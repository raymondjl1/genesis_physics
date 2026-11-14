# Expansion Ledger — Master Index

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> Master index for the Expansion Ledger: every equation in the Genesis Physics theory traced
> back to the seed `1 = 1` via the Expansion Hypothesis. Each domain has its own `LEDGER_NN_*.md`
> with one block per equation (equation · source · spine path S0–S9 · decrees D0–D6 · trace ·
> constants · status). Foundational references: `SPINE.md`, `DECREE_REGISTER.md`,
> `README_SCHEMA.md`, `EXPANSION_HYPOTHESIS_ANALYSIS.md`.

## How this ledger was built

- **Phase 0 (main agent, by hand):** the Spine (rungs S0–S9, `SPINE.md`), the Decree Register
  (D0–D6, `DECREE_REGISTER.md`), and the row schema + honesty rules (`README_SCHEMA.md`) were
  written first, so every domain tracer cites identical rung and decree IDs and the same constant
  tags (`[DERIVED ratio]` / `[SELECTED scale → D4]` / `[FIT → D5]` / `[count → D3]`).
- **Trace pass (multi-agent workflow):** one agent per domain read every equation-bearing source
  file in that domain (`.md` and `.py`, excluding `00_Archive/`, `__pycache__/`, the
  `Expansion_Ledger/` folder, and the meta-analysis note), enumerated every displayed/numbered
  equation and named key result, and wrote one trace block per equation back to `1=1`.
- **Adversarial verify pass (rerun, 2026-06-24):** a second, adversarial agent re-audited each of
  the **11** ledgers for four defect classes — (A) smuggled decrees (a decree used in the trace but
  absent from the Decrees line), (B) mislabeled constants (a dimensionful constant tagged
  `[DERIVED ratio]`, or a generic count falsely tagged `[count → D3]`), (C) missed equations, and
  (D) spine-path mismatches (a rung used in the trace but absent from the cited path). Defects were
  fixed **in place**; **no honest UNTRACEABLE or PARTIAL flag was ever weakened into a false DERIVED
  claim**, and no fabricated `derived-from-1=1-alone` chain was introduced.
- **Domains 06 (Nuclear & Particle) and 10 (Fundamental Constants) deepened:** these two were
  re-authored as **exhaustive** enumerations (replacing earlier principal-coverage drafts of ~24
  and ~28 headline blocks) — every intermediate result, definitional identity, retained failed
  attempt, and op-file computation is now its own block (108 and 97 blocks respectively). Both were
  then run through the same adversarial verify pass as the other nine.

The verify pass corrected stale header counts in **every** domain (several headers undercounted by
10–45 % because equations were appended after the header was first written), fixed smuggled D1
(the 6D manifold cited in the trace but not the Decrees line), smuggled D2 (a charge / Thomson
cross-section / Coulomb coupling hidden behind D6 or D4), and the recurring **D1-vs-D3 confusion**
(the spatial-dimension count `3` and generic apparatus/mode/lattice integers are **D1** or plain
`[count]`, **never** the topological winding `n_w=3` which is **D3**). All edits stayed inside the
target ledger files.

---

## Index table (post-verify, corrected counts)

| # | Domain | Ledger file | Equation blocks | Decrees invoked | Notes / open items |
|---|--------|-------------|----------------:|-----------------|--------------------|
| 00 | Foundations | `LEDGER_00_Foundations.md` | 61 | D0,D1,D2,D3,D4,D5,D6 | 3 UNTRACEABLE, 13 PARTIAL. Verify added EQ-FND-61 (δ_CP=π/3 from Z₆/n_w); fixed Firmament wave-operator smuggle (D6/S6) and two D1-vs-D3 mislabels. |
| 01 | Classical Mechanics | `LEDGER_01_Classical_Mechanics.md` | 105 | D0,D1,D2,D4,D5,D6 | 1 UNTRACEABLE (γ damping form/value), 5 PARTIAL. Standard CM recovered as weak-field/continuum limit. D2 enters only via imported ionic-crystal charge (EQ-CM-102/103). No D3. |
| 02 | Thermodynamics | `LEDGER_02_Thermodynamics.md` | 63 | D0,D1,D2,D3,D4,D5,D6 | 4 UNTRACEABLE, 4 PARTIAL. Verify added 3 missed equations (barometric law, T_CMB, 4D Maxwell action) and fixed systematic count-mislabeling. |
| 03 | Electromagnetism | `LEDGER_03_Electromagnetism.md` | 67 | D0,D1,D2,D3,D4,D5,D6 | 2 UNTRACEABLE (cross-domain), 6 PARTIAL. D3 confined to genuine topological quantization (flux/charge/circulation, EQ-EM-34/35/64). |
| 04 | Optics and Waves | `LEDGER_04_Optics_and_Waves.md` | 43 | D0,D1,D2,D4,D5,D6 | 3 UNTRACEABLE (Firmament σ/μ values; starlight magnitudes), 4 PARTIAL. Correctly refuses to tag generic diffraction integers as D3. No D3. |
| 05 | Quantum Mechanics | `LEDGER_05_Quantum_Mechanics.md` | 70 | D0,D1,D2,D3,D4,D5,D6 | 3 UNTRACEABLE, 7 PARTIAL. Largely honest as written; verify added Bohr magneton (EQ-QM-70) and corrected header count. |
| 06 | Nuclear and Particle | `LEDGER_06_Nuclear_and_Particle.md` | 108 | D0,D1,D2,D3,D4,D5,D6 | 2 UNTRACEABLE, 64 PARTIAL, 44 DERIVED. Exhaustive. The fermion sector: structures DERIVED given D2/D3/D6; the **numbers** split — pure counts (3 generations, color 3, δ_CP=π/3) are DERIVED/`[count → D3]`, masses/mixings are `[FIT → D5]`. |
| 07 | Relativity | `LEDGER_07_Relativity.md` | 56 | D0,D1,D4,D5,D6 | 6 UNTRACEABLE, 12 PARTIAL. **No D2/D3** (pure gravity sector — no gauge charge, no winding). Verify added 4 missed equations (geodesic/equivalence, 6D SRN metric, GW polarizations + strain, BH first law). |
| 08 | Cosmology | `LEDGER_08_Cosmology.md` | 71 | D0,D1,D2,D3,D4,D5,D6 | 4 UNTRACEABLE, 24 PARTIAL. Verify un-smuggled three hidden D2 charges (Thomson σ_T, ionization energy) and added the Hubble-tension prediction (EQ-COS-71). |
| 09 | Chemistry and Materials | `LEDGER_09_Chemistry_and_Materials.md` | 97 | D0,D1,D2,D3,D4,D5,D6 | 3 UNTRACEABLE, 8 PARTIAL. Applied membrane QM; mostly consumes domains 03/05/06. Verify added H₂ Morse curve and membrane electron energy. |
| 10 | Fundamental Constants | `LEDGER_10_Fundamental_Constants.md` | 97 | D0,D1,D2,D3,D4,D5,D6 | 1 UNTRACEABLE outright (6 equations across 4 honest-gap findings), 48 PARTIAL. Sharpest grammar/decree split: every dimensionful constant is `[SELECTED scale → D4]`. Verify fixed 14 S9-manifold-without-D1 smuggles. |
| | **TOTALS** | **11 domain ledgers** | **838** | **D0–D6 (all used)** | **32 UNTRACEABLE, 195 PARTIAL** |

> Per-domain header tables carry the authoritative within-domain breakdown. Where a domain's
> header gives a finer status census (e.g. 06: 44 DERIVED / 64 PARTIAL; 10: 36 DERIVED-as-form /
> 12 DERIVED-given-decrees / 48 PARTIAL / 1 UNTRACEABLE), that breakdown governs that domain.

---

## The headline result — the grammar / decree partition

Every one of the **838** traced equations resolves into exactly two kinds of content:

1. **Grammar + geometry (forced).** The *form* of each equation — its conservation structure (S1),
   its ratio/proportion content (S2), its real/complex continua (S3/S4, given D0), its
   vector/tensor/Hilbert structure (S5), its calculus and field operators (S6), its symmetry
   currents (S7), its topological invariants (S8), and its manifold/curvature (S9) — is **DERIVED**:
   it is forced by truth-preserving expansion of `1=1`. Dimension*less* numbers that trace to
   geometry or topology (e.g. 2/5 for a solid sphere, R=11/3, the Casimir b₀ ratio, δ_CP=π/3) are
   `[DERIVED ratio]`.
2. **Decreed inputs (selected).** Everything not forced is one of the seven decrees D0–D6, each
   cited explicitly wherever it enters. These are the framework's genuine, enumerated axioms.

### Decree-prevalence table (how many of the 11 domains invoke each decree)

| Decree | What it selects | Domains invoking it | Reach |
|--------|-----------------|--------------------:|-------|
| **D0** | completed infinity (ℚ→ℝ) | 11 / 11 | universal (every real continuum) |
| **D1** | dimension = 6 (→ 4D) | 11 / 11 | universal (every manifold / dimension count) |
| **D2** | gauge group SU(3)×SU(2)×U(1) | 10 / 11 | all but 07 (pure-gravity Relativity) |
| **D3** | winding n_w = 3 (⇒ 3 generations) | 8 / 11 | all but 01, 04, 07 |
| **D4** | scale anchor Λ_Z0 / M_Pl | 11 / 11 | **universal — every dimensionful constant** |
| **D5** | residual fitted O(1) constants | 11 / 11 | universal (each domain has data-matched O(1) values) |
| **D6** | architectural axioms (Ψ_A/Ψ_B, Firmament, sustaining) | 11 / 11 | universal (the physical content) |

The signal is clean. **D0, D1, D4, D5, D6 are universal** — they are present in all 11 domains
because every domain uses real continua (D0), lives on a manifold (D1), carries dimensionful
magnitudes that are "1 in chosen units" (D4), retains some data-matched O(1) calibration (D5), and
rests on the membrane/Waters/zone physical content (D6). **D2 is absent only from pure-gravity
Relativity (07)**, which has no gauge charge. **D3 — the one genuinely topological count — is the
narrowest: it appears in only 8 of 11 domains, and within those it is load-bearing only in the
fermion sector** (generations, color, the Z₆/n_w angle). Classical Mechanics (01), Optics (04), and
Relativity (07) invoke no winding at all.

### Per-status census (where the verify data supports it)

Across the domains that report an explicit status breakdown plus the per-domain PARTIAL/UNTRACEABLE
tallies, the global census is:

| Status | Meaning | Global count |
|--------|---------|-------------:|
| **DERIVED-as-form** / **DERIVED-given-decrees** | form forced by spine; scale/content supplied by named decrees | ~611 (838 − PARTIAL − UNTRACEABLE) |
| **PARTIAL** | form derived, but a load-bearing O(1) coefficient or value is fitted/asserted | **195** |
| **UNTRACEABLE** | a load-bearing input is on neither the spine nor the register; honestly flagged, never fabricated | **32** |

So **~73 % of traced equations are DERIVED** (form forced by grammar, scale/content by decree),
**~23 % are PARTIAL** (the form is forced but at least one O(1) number is still matched to data —
overwhelmingly concentrated in 06 Nuclear/Particle and 10 Fundamental Constants, the fitted-mass and
fitted-coupling domains), and **~4 % (32 items) are UNTRACEABLE** — each recorded with its reason in
`COVERAGE_AUDIT.md`, none dressed up as a derivation.

---

## What this partition says plainly

- **D4 (scale) is universal — every dimensionful constant is a unit.** ℏ, c, G, k_B, σ, μ, m_e, the
  Planck mass, Λ_Z0 — all of them are `[SELECTED scale → D4]`, i.e. "1 in chosen units." None of
  them is a free dimensionful prediction; fixing the single anchor Λ_Z0 = M_Pl fixes them all. The
  framework makes **no claim** to derive a dimensionful magnitude from nothing.
- **The dimensionless content traces to grammar + geometry.** Once the units are factored out (D4),
  the surviving dimensionless ratios and integers are `[DERIVED ratio]` (geometry/topology) — they
  are the genuinely forced, "of-the-Word" numbers (2/5, 11/3, the Casimir ratio, δ_CP=π/3, the
  index-theorem +3).
- **The irreducible freedom is D2/D3, localized to the fermion sector.** After D0/D1/D4 (the
  universal structural/unit decrees) and D6 (the physical content), the *only* selections that buy
  genuine physics are **D2** (which member of the SU(N) family — the gauge group) and **D3** (the
  winding n_w). D2 is the gauge structure; D3 is the single integer behind three generations. The
  fitted residue D5 is honestly held open, not claimed.
- **n_w = 3 is the one sharp open derivation (#849).** The entire generation structure rests on
  **D3: winding n_w = 3** (Postulate F, `AXIOM_GODHEAD_ZONE_Z0.md` §4). It is the narrowest decree
  (8/11 domains, load-bearing only for fermions) and the most consequential open item: deriving
  `n_w = 3` from the grammar — rather than selecting it — would collapse D3 into the spine and is the
  single most valuable target in the whole ledger. It is tracked as open problem **#849**.

*Cross-ref: `COVERAGE_AUDIT.md` (the full open-item / domain-scoping audit), `SPINE.md`,
`DECREE_REGISTER.md`, `README_SCHEMA.md`.*
