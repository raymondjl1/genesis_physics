# Canonical Facts Registry — Genesis Physics

**Status:** Authoritative single source of truth for cross-cascade consistency (ideas → analysis → books). Created 2026-06-09 from a full Phase-0 audit that surfaced 17 cross-source conflicts. Every analysis file and every book must agree with this registry; where a source disagreed, the disposition column says how it was resolved.

**Resolution rules applied** (in precedence order):
1. An explicitly **"locked"** Reference card (`Five_Principles.md`, `Symbol_and_Constants.md`) wins on terminology/constants.
2. The **newest dated derivation** wins on physics (e.g. `PARTICLE_MASS_SPECTRUM_V3` / `MASS_SCALE_RESOLUTION` over `06-HIGGS_DERIVATION`; the RT‑1.WF/OP‑2.WP warp resolution over older KK/gravity values).
3. Root `CLAUDE.md` wins over `BOOK_SERIES_STRATEGY.md` on franchise structure.
4. **Honest/conservative status wins on resolution claims** — where an "OPEN_PROBLEMS_REGISTER" says RESOLVED but a governance `CLAUDE.md` calls it an OPEN BLOCKER, treat it as OPEN until the author ratifies otherwise (per the standing board-lag rule). Anything labeled **NEEDS-RATIFY** is the author's call; a conservative default is given so the cascade is internally consistent now.

---

## A. Franchise structure  *(RESOLVED-BY-RULE)*
- **Book 0** — *The Foundations of Genesis Physics*, 6 volumes (Architecture of Reality / Forces and Fields / Matter and Motion / The Quantum World / The Cosmos / Predictions & Simulations). Built first, in parallel; encyclopedia.
- **Book 1** — *Genesis Physics: The Hidden Architecture — A Physics of the First Page* (folder `Book_1_Hidden_Architecture/`). Popular-science flagship. Launch 2nd.
- **Book 2 (this folder `Book_2_The_Creators_Blueprint/`)** — *The Creator's Blueprint (Family Edition)*, scripture-first, **KJV throughout**, homeschool families. Launch **1st**.
- Old `Book_2_The_Hidden_Architecture/` content is **archival** (folded into Book 1). Content cascades bottom-up: Foundations → flagship → family.
- **Cascade target:** `Quality_Control/BOOK_SERIES_STRATEGY.md` is STALE (says "Family Edition last", old flagship title, treats Book 2 as live) → UPDATE to match this.

## B. Zone architecture  *(NEEDS-RATIFY — two "authoritative" cards disagree; conservative default below)*
- 6D coordinates (t,x,y,z,ξ,η); indices ∈ {0,1,2,3,5,6}; signature (+−−−−−). ξ = Waters-Above direction (cosmological); η = Waters-Below direction (nuclear). Extra dimensions are **non-compactified / cosmological-scale** (the deliberate departure from string/KK).
- **Default canonical labels** (from `RESOLVED_Zone_Numbering_And_Terminology.md` + `Glossary.md`): Z₂.₂.₁ = Waters Below (dark matter, Ψ_B, w≈0); **Z₂.₂.₂ = the Firmament membrane (4D)**; Z₂.₂.₂.₁ = Condensed/baryonic matter; Z₂.₂.₃ = Waters Above (dark energy, Ψ_A, w≈−1).
- **CONFLICT to fix:** `Quality_Control/Reference/Zone_Architecture.md` labels Z₂.₂.₂ itself as "Condensed Matter", and its simplified Zone 3/Zone 4 mapping contradicts the RESOLVED file. **Default: the membrane reading above is canonical; reconcile `Zone_Architecture.md` to it.** *(Author: confirm the membrane-vs-matter assignment of Z₂.₂.₂.)*

## C. The two phase transitions  *(RESOLVED-BY-RULE — confirmed distinct)*
- **Sabbath Boundary** (Axiom 4 / `AXIOM_METRIC_DISCONTINUITY`): metric junction, Phase 1 Creation → Phase 2 Edenic; **locks all constants (α, G, c, Λ)**; dS/dt → 0; κ_create → κ_full.
- **The Fall** (Axiom 5 / `AXIOM_PHASE_TRANSITION_FALL`): thermodynamic/κ transition, Phase 2 → Phase 3; first-order; dS/dt 0→>0 (arrow of time, decay); κ_full → κ_partial = κ_full(1−ε). **Constants do NOT change here.**
- These are **independent events**. Already cascaded into Book 1 (Ch 5/11/13/15). Source: `Four_Epochs_Timeline.md`. (Book 1 Ch13 SPEC lags — GH #845.)

## D. The Five Principles  *(RESOLVED-BY-RULE — `Five_Principles.md` is locked)*
- Name: **"Five Principles"** (never "Five Governing Principles", never lowercase).
- Canonical order/numbering: **1 Sustaining · 2 Conservation · 3 Symmetry · 4 Degradation · 5 Duality**. "Hierarchy" is NOT a principle.
- **Cascade target:** `RESOLVED_Zone_Numbering_And_Terminology.md` §5 uses the wrong name and a Degradation↔Duality-swapped order → UPDATE.

## E. Key constants & scales  *(mixed)*
| Quantity | CANONICAL value | Disposition | Stale sources to fix |
|---|---|---|---|
| Higgs VEV v | **246.22 GeV**; convention V = −μ²\|H\|² + λ\|H\|⁴, ⟨H⟩=(0,v/√2), v=μ/√λ | RESOLVED | 06-HIGGS **line 361** garbled (`2μ/√λ`→~492 fudged to 246) → fix |
| Higgs quartic λ_H | **0.129** (m_H²=2λv²) | RESOLVED | — |
| m_H | 125.1 GeV (= √(2λ)·v) | RESOLVED | — |
| M_W | **80.27 GeV** (= gv/2, g=0.652) | RESOLVED (Ch 11 corrected) | — |
| M_Z | **91.55 GeV** (= M_W/cosθ_W, cosθ_W=0.8768; measured 91.188) | RESOLVED (Ch 11 corrected) | 06-HIGGS internally 91.2 (line 41) vs 91.7 (line 574); V3 says 91.2 → fix both to 91.55 predicted |
| First KK (η) mode | **≈477 MeV** (= πℏc/η_B; hadronic scale) | RESOLVED | 06-HIGGS §1.4 still says **430 GeV** ("electroweak", retracted) → fix |
| η_B | 1.3×10⁻¹⁵ m | RESOLVED | — |
| ξ_A | 3×10²⁶ m — **distinct from** the Hubble radius (~1.4×10²⁶ m) | RESOLVED | `RESOLVED_Zone_Numbering` conflates them → fix |
| Warp index | **A_ξ(ξ) = (2/3)·ln(ξ₀/ξ)** (RT‑1.WF / OP‑2.WP resolution) | **NEEDS-RATIFY** (default = the 2/3 resolution form) | `KK_DIMENSIONAL_REDUCTION` (λ≈0.05) and `10-GRAVITATIONAL_CONSTANT_DERIVATION` (λ=41) are unreconciled → flag/update *(Author: confirm the 2/3 form is canonical)* |
| Firmament tension σ | 6.0×10⁹⁸ **kg/(m·s²)** | RESOLVED | unit drift "kg/s²" in 06-HIGGS / MEMBRANE_MASS → fix |
| Membrane density μ_m | 6.7×10⁸¹ **kg/m³** | RESOLVED | V3 §2.1 says 6.7×10⁸² kg/m² → fix |
| Energy budget | Ω_Λ 0.684 / Ω_DM 0.266 / Ω_b 0.05 (Planck 2018) | RESOLVED | — |
| H₀ | 67.4 km/s/Mpc | RESOLVED | `RESOLVED_Zone_Numbering` says 70 → fix |
| CC ρ_eff | 2.93×10⁻⁴⁷ GeV⁴ (within ~20% of observed; n=1 suppression, **rigorous derivation of n=1 PENDING**) | RESOLVED (status honest) | — |
| Fine structure α⁻¹ | one-loop **137.17** (0.095%); two-loop/UV-boundary closure to 137.036 is **OPEN** (OP-07) | RESOLVED (honest) | drop "9 sig figs / no free parameters" overclaim in `Foundations/FINE_STRUCTURE_DERIVATION.md`; reconcile the two fine-structure files |

## F. Particle mass spectrum & spin-½  *(NEEDS-RATIFY on status; values RESOLVED to honest canon)*
- **Honest residuals (canonical = Vol 4 Ch10_FINAL):** electron +17%; muon −15…19%; tau = **calibration anchor** (not a prediction); light quarks ~7%; heavier quarks fail badly at tree level; proton −0.02%, neutron +0.005% (proton credit shared with QCD). Three-generation count and charge quantization are **genuine derivational wins**. Neutrino smallness qualitative win.
- **Spin-½ from a bosonic membrane = OPEN BLOCKER (GitHub #1 / Assumption 10.1).** Every fermion result is conditional on the unproven Hopf-winding/Postulate-F assumption. **Default = OPEN.** *(Author: the OP register claims this is "resolved" conditional on the new Λ_Z0 axiom — ratify whether to present it as conditionally-resolved or open.)*
- Generation→mode mapping: **gen 3 (τ,t) → n_ξ=1; gen 1 (e,u) → n_ξ=3** (V3 corrected). 06-HIGGS §7.3 retains the reversed old mapping → fix.
- Yukawa hierarchy α: **fitted (~20% residual), not derived** (honest). → flag OP-register "FULLY RESOLVED".
- **Cascade target:** `06-PARTICLE_MASS_SPECTRUM_V3.md` claims "spin-1/2 proven" + "<1%" — contradicts Ch10_FINAL (which cites it) → UPDATE to the honest canon (GH #844). `FERMION_EMERGENCE_FROM_MEMBRANE` / OP-register OP-02 likewise.

## G. Open-problems status  *(NEEDS-RATIFY — two lists disagree)*
- Governance `CLAUDE.md` files list spin-½ (#1), mass-spectrum errors (#2), weak/CP (#3), Higgs (#25) as **OPEN**.
- `OPEN_PROBLEMS_REGISTER.md` (2026-05-14, sitting in `Book_0/00_Archive/`) marks most "RESOLVED", many *conditional on a new Λ_Z0 (Godhead-zone) axiom*.
- **Default:** treat the governance OPEN status as canonical; the register's resolutions are **claims to verify**, not settled. *(Author: ratify the register — and decide whether the Λ_Z0 axiom is adopted. If adopted, it must be added to the axiom set and cascaded.)* The register is also mis-filed in an Archive folder despite being the newest status doc — decide its home.

## H. Stale analysis to ARCHIVE  *(RESOLVED-BY-RULE)*
- `06-PARTICLE_MASS_SPECTRUM_V2.md` + the 5 `06-MASS_SPECTRUM_V2_*` files → `06_…/00_Archive` (survivor: V3). Update `Vol_4/CLAUDE.md` "Supporting analysis (5 files)" pointer.
- `Foundations/AXIOM_MEMBRANE_MECHANICS.md` (base) → archive (survivor: `_v2`, per `Book_0/CLAUDE.md`).
- Duplicate `VALIDATION_REPORT_2026-04-05.md` (active copy), redundant `TEST_RESULTS_*.docx` exports, the 3 non-latest dated `TEST_RESULTS_2026-04-05*.md` (survivor: `TEST_RESULTS_20260406_092623.md`).
- Junk: `Mathematical_Models/00_Archive/OBSERVATIONAL_PHYSICS_TEST_SUITE.md.tmp.5.*`.
- **Broken/orphaned pointers to fix:** `SOLVE_1000X_MASS_PROBLEM.md` (referenced in `Book_0/CLAUDE.md` + `Vol_4/CLAUDE.md`, file does not exist); `nuclear_physics/test_nuclear_physics.py` path in Vol 4 Ch11_FINAL (real dir is `06_Nuclear_and_Particle_Physics`).

---
**Items needing the author (ratify before lock):** B (zone Z₂.₂.₂ assignment), E (warp-index 2/3 form), F & G (spin-½ / OP-register resolution status + the Λ_Z0 axiom decision). Everything else is determinable-by-rule and is being cascaded now.
