# Next Session Continuation Prompt

Paste the block below verbatim to start the next working session.

---

## PROMPT

You are continuing work on the Genesis Physics Book 0 series. Before doing anything else, read these three files in order:

1. `01_Genesis_Physics/Book_0_The_Foundations/REMAINING_PROBLEMS.md` — the full prioritized open problems registry (31 items across T1–T4 tiers). This is the work queue.
2. `01_Genesis_Physics/Book_0_The_Foundations/BOOK_0_STATUS_REPORT.md` — master status dashboard showing what is resolved, what is in progress, and what gates what.
3. `01_Genesis_Physics/Book_0_The_Foundations/BOOK_0_FILE_MANIFEST.md` — full file inventory with roles and production status for all 553+ files.

Also read the auto-memory index at `.auto-memory/MEMORY.md` to load session context.

### What was completed in prior sessions (do not redo)

The following open problems were fully resolved on 2026-05-15 and their research notes already exist in `Research/Foundations/`:

- **OP-A_η** — Waters Below warp form A_η = B₀ − η/η_B derived from first principles (not assumed). B₀ = 28.8 derived from KK normalization. File: `OP_AETA_PSI_B_SELF_CONSISTENT.md`
- **OP-G6** — κ₆² fully derived; all three routes (KK, Israel, bulk Einstein) consistent. File: `OP_G6_KAPPA6_DERIVATION.md`
- **CT-4.β** — ħ is now a genuine first-principles prediction with zero free parameters. Chain: B₀ → κ₆² → ξ₀ → β_geom = 557 → ħ_obs.
- **RT-2.SU3** — Z₃ orbifold → SU(3)_C complete. File: `RT2_SU3_Z3_ORBIFOLD.md`
- **OP-A_ξ** — Classical sector complete (back-reaction ~ 10⁻¹²⁰). File: `OP_AXI_PSI_A_SELF_CONSISTENT.md`
- **RT-2.G** — G₄ formula correct with L_eff explicit. File: `G_N_RECONCILIATION_RT2G.md`
- **OP-2.WP** — B_η ≈ const is canonical warp form. File: `B_ETA_WARP_RESOLUTION_OP2WP.md`
- **CT-4.Λ** — Λ_zone = ħc/η_B ≈ 0.152 GeV (not 10¹⁹ GeV); n=1 Waters gives Λ_eff within 20% of observed.

A full audit of chapters, file naming, and duplicates was also completed. Key findings are in `BOOK_0_STATUS_REPORT.md`.

### Work queue for this session

Start with **Tier 1 (publication-blocking)** problems from REMAINING_PROBLEMS.md. They are:

- **T1-01** — Quantum Hadamard propagator for OP-A_ξ / OP-A_η (quantum corrections to warp forms)
- **T1-02** — Rigorous n=1 Waters suppression derivation (currently a 4-argument heuristic; needs formal proof). Need to create `Research/Foundations/N1_DERIVATION_CT4L_OPEN_WATERS.md`
- **T1-03** — Fix stale Λ_zone = 2.4×10¹⁹ GeV in `Vol_4_The_Quantum_World/Ch_07_Perturbation_Theory_and_Feynman_Diagrams/Ch07_FINAL.md`. Correct value: 0.152 GeV. This is the AUDIO PRODUCTION BLOCKER.
- **T1-04** — α_s RG running from KK scale to QCD scale. Need to create `Research/Foundations/ALPHA_S_RG_RUNNING_RT2_ALPHAS.md`
- **T1-05** — Electroweak mixing angle θ_W derivation from zone geometry

After T1, proceed to **Tier 2** problems per the registry.

### Key canonical values (do not alter without derivation)

- α⁻¹ = 137.17 ± 0.15 (crown jewel; 0.10% accuracy)
- B₀ = 28.8; e^{2B₀} = 1.77×10²⁵
- κ₆² ≈ 6.9×10⁻⁶⁶ s²/kg
- η_B = 1.3×10⁻¹⁵ m (QCD scale)
- ξ₀ ≈ 60 l_Pl
- L_A = 83.2 η_B ≈ 1.1×10⁻¹³ m
- Λ_zone = ħc/η_B ≈ 0.152 GeV
- β_geom = 557
- n=1 Waters: ρ_eff ≈ 2.93×10⁻⁴⁷ GeV⁴ (vs observed 3.5×10⁻⁴⁷, 20% match)

### Instructions

- Always read the relevant research notes before writing new derivations
- New research notes go in `Research/Foundations/`
- Chapter fixes go directly in the chapter file (edit the FINAL if it exists, otherwise the DRAFT)
- Update `BOOK_0_STATUS_REPORT.md` and `REMAINING_PROBLEMS.md` as problems are resolved
- Follow the "always answer WHY" principle — no equation without physical motivation
- The physics must trace back to the 6D action in `Research/Foundations/ACTION_6D_COMPLETE.md`
