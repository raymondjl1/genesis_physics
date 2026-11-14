# Expansion Ledger — Coverage Audit

> **STATUS: EXPLORATORY ANALYSIS — UNRATIFIED. Modifies no axiom or theorem.**
> This audit collects the **untraceable** and **partial** items from all 11 domain ledgers and
> sorts them into (A) genuinely theory-wide open derivations and (B) domain-scoping pointers
> (items "untraceable here" but traced in another domain or held open as a known research gap).
> It is the honesty ledger: nothing is fabricated; every gap is named with a reason.
> References: `LEDGER_MASTER.md`, `SPINE.md`, `DECREE_REGISTER.md`, `README_SCHEMA.md`.

## Global tally (post-verify, corrected counts)

| Metric | Count |
|--------|------:|
| Equation blocks traced (11 domains) | **838** |
| UNTRACEABLE items | **32** |
| PARTIAL items | **195** |
| DERIVED (form forced; scale/content by decree) | **~611** (~73 %) |

Per-domain UNTRACEABLE / PARTIAL (authoritative within-domain breakdown lives in each header):

| Domain | Eqs | UNTRACEABLE | PARTIAL |
|--------|----:|------------:|--------:|
| 00 Foundations | 61 | 3 | 13 |
| 01 Classical Mechanics | 105 | 1 | 5 |
| 02 Thermodynamics | 63 | 4 | 4 |
| 03 Electromagnetism | 67 | 2 | 6 |
| 04 Optics and Waves | 43 | 3 | 4 |
| 05 Quantum Mechanics | 70 | 3 | 7 |
| 06 Nuclear and Particle | 108 | 2 | 64 |
| 07 Relativity | 56 | 6 | 12 |
| 08 Cosmology | 71 | 4 | 24 |
| 09 Chemistry and Materials | 97 | 3 | 8 |
| 10 Fundamental Constants | 97 | 1 | 48 |
| **Total** | **838** | **32** | **195** |

The PARTIAL count is dominated by **06 Nuclear/Particle (64)** and **10 Fundamental Constants
(48)** — the two fitted-mass / fitted-coupling domains. Everywhere else PARTIAL stays in single
digits or low tens, confirming that the fitted freedom (D5) is concentrated, not pervasive.

---

## Category A — genuinely theory-wide open items

These are items whose load-bearing input is on **neither the spine nor the decree register** and
that are **not** resolved by pointing at another domain. They are the framework's real open
derivations.

### A1. n_w = 3 — the winding that fixes three generations (the master open item, #849)
- **Decree:** D3 (`AXIOM_GODHEAD_ZONE_Z0.md` §4, Postulate F).
- **Why open:** S8 forces winding/index to be an *integer*; it does **not** force the value 3.
  The entire fermion generation structure (06 Nuclear/Particle EQ-NP-24/25/26/31; 00 Foundations
  EQ-FND-43/61; the δ_CP=π/3 angle) hangs on this single selected integer. Deriving n_w=3 from the
  grammar would collapse D3 into the spine. This is the **single highest-value open derivation**
  in the ledger. Tracked as open problem **#849**.

### A2. Residual fitted O(1) constants (D5) — the fermion masses and mixings
- **Where:** overwhelmingly 06 Nuclear/Particle (64 PARTIAL: Yukawa y_f, CKM A/ρ/η coefficients,
  see-saw overlaps, SEMF coefficients) and 10 Fundamental Constants (48 PARTIAL: the α two-loop
  prefactor, mass-hierarchy O(1) factors).
- **Why open:** the *structure* (GMOR, the CKM ladder, the see-saw, the Higgs mechanism) is
  DERIVED given D2/D3/D6, but specific O(1) magnitudes are still **matched to data** (`[FIT → D5]`),
  not derived. Honest residuals are on record (e.g. electron mass +17 %; heavier quarks fail at
  tree level). These are real open numerical items, not derivations.

### A3. Firmament material constants σ, μ (membrane tension / mass density)
- **Where:** 04 Optics UNTRACEABLE-01 (σ, μ "numerical values"); also underpins 02/05/09 via D6.
- **Why open:** the membrane *content* is D6, but the **numerical values** of the Firmament tension
  σ and density μ are asserted, not derived — and the source files internally disagree
  (04: μ = 6.7×10⁸² kg/m² vs `test_optics.py`: μ = 6.7×10⁸¹ kg/m³, with mismatched units). The
  disagreement is flagged UNTRACEABLE and left intact, not papered over.

### A4. The α (fine-structure) two-loop precision to 137.036
- **Where:** 10 Fundamental Constants (EQ-FC-11 hard UNTRACEABLE; EQ-FC-57/64/74/86/91 lean
  UNTRACEABLE — 6 equations across 4 honest-gap findings); cross-referenced by 09 Chemistry
  (EQ-CHEM-16, the data-matched α⁻¹=137.036 target) and 03 EM (α⁻¹=1.44 ln(ξ_A/η_B), PARTIAL).
- **Why open:** the UV boundary value is fixed given Λ_Z0 (α_6D ≈ 1.82) and the *form* of the
  running is RG grammar, but the coefficient that lands the two-loop result on 137.036 is a
  data-matched / asserted input, not derived. Honestly held open.

### A5. Membrane damping γ — form and value
- **Where:** 01 Classical Mechanics EQ-CM-52 (the lone full UNTRACEABLE in that domain,
  `01-COMPLETIONS.md` §6.1).
- **Why open:** the dissipative γ term's membrane-derived form and value are not reconstructable
  from the spine + register as written; flagged UNTRACEABLE rather than fabricated.

### A6. The δS=0 (stationary-action) status — a structural caveat, not a single equation
- **Where:** noted in `SPINE.md` (S6 rung note) and inherited by every action-principle block
  tagged "DERIVED-as-form (δS=0 borderline)" across 05/06/07/10.
- **Why open:** that the *realized* expansion is the *stationary* one (least action) may be a
  derived consequence of infinitesimal truth-preservation **or** an unlisted dynamical decree.
  It is honestly tagged borderline wherever it is load-bearing; it is not silently assumed.

---

## Category B — domain-scoping pointers (traced elsewhere, not a true gap)

These items are "untraceable **within this domain**" only because the derivation lives in another
domain or in Foundations. They are **not** theory-wide gaps — they are cross-references, recorded
here so the audit is complete.

- **EM cyclotron + spectroscopic/atomic formulas** — 03 EM UT-EM-01/02. Both explicitly tagged
  "cross-domain": cyclotron motion and atomic spectra are traced in 05 Quantum Mechanics / 09
  Chemistry, not re-derived in EM.
- **Starlight propagation magnitudes** — 04 Optics UNTRACEABLE-02/03 + 4 PARTIAL (comoving-distance
  numerics, z~10²⁶ redshift, applied geodesic EOM). The cosmological-distance machinery is the
  province of 08 Cosmology + 07 Relativity; Optics consumes it. The numerical magnitudes route to
  the cosmology/creation-event inputs (D6), not to an Optics derivation.
- **CMB blackbody temperature T_CMB = 2.725 K** — 02 Thermodynamics EQ-THERMO-62, honestly tagged
  `[FIT → D5]` (measured, cross-domain cosmology). The Planck *form* is derived; the *value* is the
  measured anchor.
- **Hubble-tension prediction** — 08 Cosmology EQ-COS-71 rests on the posited D6 Sabbath
  discontinuity (EQ-COS-25, itself UNTRACEABLE) with a fitted O(1) coefficient → D5. Scoped to the
  cosmology D6 ansatz, not a free-standing gap.
- **6D SRN-analog metric Waters profiles** — 07 Relativity EQ-REL-54, PARTIAL: the ξ/η
  Waters-profile blocks are an asserted D6 ansatz, traced to the Foundations Waters axioms, not
  derived inside Relativity.
- **Thermodynamic / cosmological charges (Thomson σ_T, ionization energy)** — formerly hidden in
  02/08; the verify pass **un-smuggled** these as D2 (EM charge) imports rather than leaving them
  mislabeled. They are now correctly scoped to the EM domain's D2, not flagged as new gaps.
- **Imported dimensionful constants ℏ, k_B, c, e²/4πε₀** — used across 01/02/05/09 but derived in
  their home domains (10 Fundamental Constants, 03 EM) and the membrane documents. Cited by D4
  (+ D6 for membrane provenance), never re-derived.

---

## Honesty issues the verify pass could not auto-fix (carried forward)

The adversarial verify pass fixed all in-place defects (smuggled decrees, mislabeled constants,
spine-path mismatches, stale header counts, missed equations) **without weakening any honest flag**.
The following are *not* fixable by re-tagging — they are genuine open physics, left honestly flagged:

1. **n_w = 3 is selected, not derived** (A1, #849) — the irreducible topological freedom.
2. **The fitted O(1) residue (D5)** in the fermion sector (A2) — 64 PARTIAL in 06, 48 in 10 — is
   matched to data, not derived; honest residuals (electron +17 %, tree-level quark failures) stand.
3. **Firmament σ, μ values are asserted and internally inconsistent** (A3) — the 04-vs-`test_optics.py`
   unit/magnitude mismatch is real and left flagged UNTRACEABLE, not reconciled by fiat.
4. **α → 137.036 two-loop precision** (A4) — UV boundary fixed by Λ_Z0; the final landing coefficient
   is data-matched. Open numerical item.
5. **δS=0 status** (A6) — action principles are tagged "DERIVED-as-form (δS=0 borderline)"; whether
   stationarity is grammar or an eighth decree is left open by design, not silently resolved.

Every remaining UNTRACEABLE (32) and PARTIAL (195) item is recorded in its domain ledger with a
reason. No chain was fabricated to remove a flag; no `derived-from-1=1-alone` claim exists anywhere
in the ledger.

*Cross-ref: `LEDGER_MASTER.md`, the 11 `LEDGER_NN_*.md` domain files, `DECREE_REGISTER.md`.*
