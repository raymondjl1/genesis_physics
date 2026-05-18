---
product: Foundations Vol 5
chapter: 8
title: Zone Cosmological Model
status: VERIFIED
author: Genesis Physics / Zone Framework
date: 2026-04-09
---

# Chapter 8 Specification: Zone Cosmological Model

## Mission

Derive the Friedmann equations as a *consequence* of the Waters field dynamics established in Vol 1 Ch 6 and the 4D Einstein field equations recovered in Vol 5 Ch 1, and use them to construct the complete sustaining-mode cosmological model of the zone framework — scale-factor evolution, density parameters, critical density, and the matter/radiation/dark-energy era structure — without ever postulating Friedmann–Lemaître–Robertson–Walker as an *ansatz*. The Waters field is not a separate cosmological fluid bolted onto general relativity; the Waters field *is* the cosmological fluid, and what cosmologists call $\rho_\text{DM}$, $\rho_\text{DE}$, and the cosmological constant are projections of its bulk profile onto the Firmament. This chapter is the load-bearing chapter of Part III: Chapters 9 (CMB), 10 (large-scale structure), 11 (dark matter / dark energy quantified), and 12 (starlight problem) all stand on it.

## Requirements

Traced from Vol 5 WRITING_PROMPT.md and Vol 5 QUALITY_GATE.md.

| ID | Requirement | Source | Where Met |
|---|---|---|---|
| R5.8.1 | Friedmann equation $H^2 = (8\pi G_4/3)(\rho_A + \rho_B + \rho_b + \rho_r) - kc^2/a^2$ derived from Vol 1 Ch 6 Waters field equations and Vol 5 Ch 1 EFE — not assumed | Chapter prompt; WRITING_PROMPT §"Ch 8" | §§8.3, 8.4 |
| R5.8.2 | Acceleration equation $\ddot a/a = -(4\pi G_4/3)\sum_i(\rho_i + 3 P_i/c^2)$ derived as a corollary of R5.8.1 and Bianchi identities | Vol 5 Ch 1 §1.8 | §8.4 |
| R5.8.3 | Each fluid component identified with its bulk-field origin: $\rho_A = \Lambda_A$ from Waters Above potential (Vol 1 Eq 1.6.36), $\rho_B \propto a^{-3}$ from Waters Below VEV (Vol 1 Eq 1.6.40), $\rho_b \propto a^{-3}$ from Firmament matter, $\rho_r \propto a^{-4}$ from Firmament radiation | Chapter prompt; 08-FRIEDMANN_EVOLUTION §§2.2-2.3 | §8.5 |
| R5.8.4 | Critical density $\rho_\text{crit} = 3H_0^2/(8\pi G_4) \approx 9.47\times10^{-27}$ kg/m³ derived and physically interpreted as the closure threshold of the Firmament-projected Waters energy budget | 08-CRITICAL_DENSITY_CALCULATION; chapter prompt | §8.6 |
| R5.8.5 | Density parameter decomposition $\Omega_A = 0.684,\ \Omega_B = 0.266,\ \Omega_b = 0.049,\ \Omega_r \approx 10^{-4}$ traced to *zone-geometric inputs* (warp factors $A_\xi, A_\eta$, Firmament tension $\sigma$) — not fit | 08-FRIEDMANN_EVOLUTION §2.4; Vol 1 Ch 6 §6.7 | §8.6 |
| R5.8.6 | Era structure (radiation $a\propto t^{1/2}$, matter $a\propto t^{2/3}$, dark-energy $a\propto e^{H_\infty t}$) derived as exact solutions of the Waters-fluid Friedmann system in each domination regime | 08-FRIEDMANN_EVOLUTION §5; Vol 3 Ch 5 (fluid dynamics) | §8.7 |
| R5.8.7 | Sustaining-mode coordinate time vs creation-epoch proper time distinction stated explicitly. The chapter defines the sustaining-mode coordinate system, derives the sustaining-mode Friedmann equations, and *defers* the Sabbath-Boundary discontinuity to Ch 9 | Vol 1 Ch 11 (zone thermodynamics); 08-FRIEDMANN_EVOLUTION §4 | §8.2, §8.10 |
| R5.8.8 | $H_0$, age $t_0 \approx 13.8$ Gyr, and $T_0 = 2.725$ K derived as integral consequences of R5.8.5 | 08-FRIEDMANN_EVOLUTION §§3.3, 7, 6 | §8.8 |
| R5.8.9 | The continuity equation $\dot\rho_i + 3H(\rho_i + P_i/c^2) = 0$ for each species shown to follow from $\nabla^\mu T_{\mu\nu} = 0$ on the Firmament (Vol 5 Ch 1 §1.8) | Vol 5 Ch 1 R6 | §8.4 |
| R5.8.10 | Test suite `Research/Mathematical_Models/08_Cosmology/test_cosmology.py` is run, results reported, and any failures explained | Chapter prompt | §8.11 |
| R5.8.11 | Forward links to Ch 9 (Sabbath Boundary, CMB), Ch 10 (structure formation), Ch 11 (DM/DE quantified), Ch 12 (starlight) explicit | Chapter prompt | §8.12 |
| R5.8.12 | Reviewer's Ledger format (per Ch 5, Ch 6, Ch 7) classifies every load-bearing claim as Derivation / Identity / Inheritance / Conjecture | Vol 5 internal precedent | §8.13 |

## Prerequisites (the reader must already know)

- **Vol 1 Ch 4** — 6D embedding, FRW-compatible 6D metric ansatz $ds_6^2 = e^{2A}\eta_{\mu\nu}dx^\mu dx^\nu + e^{2B}(d\xi^2 + d\eta^2)$ (Eq 1.4.18). **Direct foundation.**
- **Vol 1 Ch 5** — Firmament as codimension-2 Firmament $\Sigma = Z_{2.2}$ with tension $\sigma > 0$, mass density $\mu$, wave speed $c^2 = \sigma/\mu$ (Eq 1.5.37); junction conditions.
- **Vol 1 Ch 6** — Waters Above ($\Psi_A$) and Waters Below ($\Psi_B$) field equations from the action principle on the 6D zone manifold. The equilibrium solutions (Eqs 1.6.36–1.6.42), the boundary conditions, and the energy fractions $\Omega_A : \Omega_B : \Omega_b = 68 : 27 : 5$ derived in §6.7. **Direct foundation.**
- **Vol 1 Ch 7** — Conservation laws $\nabla^\mu T_{\mu\nu} = 0$ on the Firmament.
- **Vol 1 Ch 11** — Zone thermodynamics, the four phases, and the existence of a sustaining-mode regime. The chapter is restricted to sustaining mode throughout.
- **Vol 3 Ch 5** — Cosmological fluid dynamics: barotropic equations of state, perfect-fluid stress-energy tensor $T_{\mu\nu} = (\rho + P/c^2) u_\mu u_\nu + P g_{\mu\nu}$, hydrostatic equilibrium.
- **Vol 3 Ch 8** — Phase transitions: matter-radiation equality, recombination as a phase transition.
- **Vol 5 Ch 1** — Einstein field equations recovered from 6D action; $G_{\mu\nu} + \Lambda_\text{eff} g_{\mu\nu} = (8\pi G_4/c^4) T_{\mu\nu}$ (Vol 5 Eq 5.1.34); Bianchi identity (§1.8). **Direct foundation.**
- **Vol 5 Ch 7** — Singularity resolution; Firmament-nucleation event replaces the Big Bang singularity. The boundary data for the past timelike geodesics in this chapter come from Theorem 5.7.3.

## "Why" Chain

1. **Why does cosmology have anything to derive?** Because once we have the EFE on the Firmament (Vol 5 Ch 1) and the bulk Waters fields as the dominant matter content (Vol 1 Ch 6), the *largest-scale* solutions of the EFE are determined: the cosmological principle (homogeneity, isotropy on scales $\gtrsim 100$ Mpc) is a *consequence* of zone symmetry (Vol 1 Ch 4 §4.7), not a postulate.
2. **Why FLRW and not some more general metric?** Because zone symmetry forces the Firmament induced metric to be conformally flat in the spatial slice on cosmological scales; FLRW is the unique homogeneous-isotropic solution and falls out, not in.
3. **Why two Friedmann equations and not one?** Because the EFE on FLRW reduce to two independent components (the $tt$ component → constraint Friedmann equation, the spatial trace → acceleration equation), with the rest forced by the Bianchi identity.
4. **Why does $\rho_A$ behave like a cosmological constant?** Because in sustaining mode the Waters Above field sits at the minimum $V'(\Psi_A) = 0$ of its potential, so $\rho_A = V_A = $ const and $w_A = -1$ exactly.
5. **Why does $\rho_B$ scale as $a^{-3}$ instead of as a constant?** Because Waters Below is in its broken phase with VEV $\langle\Psi_B\rangle = v_B$, but the *projected number density* of $\Psi_B$ quanta on the Firmament dilutes geometrically as the Firmament expands — exactly like nonrelativistic dust.
6. **Why is the universe spatially flat?** Because the 4D induced metric inherits its spatial curvature from the bulk extrinsic curvature of the Firmament in the $(\xi,\eta)$ directions, and Vol 1 Ch 6 §6.5 shows that the equilibrium Firmament has $K^{(\xi)} = K^{(\eta)} = 0$ on cosmological averages — so $k = 0$ is forced by zone equilibrium, not assumed.
7. **Why is the energy budget exactly 68/27/5?** Because the warp factors $A_\xi, A_\eta$ and the Firmament tension $\sigma$ have determinate values from Vol 1 Ch 6 §6.7. The ratios are *geometric*, not phenomenological.
8. **Why does the universe accelerate now?** Because $\rho_A$ is constant while $\rho_B + \rho_b \propto a^{-3}$ falls; once $\rho_A$ dominates, the acceleration equation gives $\ddot a > 0$. The transition redshift $z_\Lambda$ is determined by the *ratio* $\Omega_A / \Omega_m$ — itself geometric.
9. **Why does the integrated age come out near 13.8 Gyr in sustaining-mode coordinates?** Because the integral $t_0 = H_0^{-1}\int_0^\infty dz/[(1+z)E(z)]$ is determined entirely by $H_0$ and the $\Omega$'s, and the framework's $\Omega$'s are the observed ones to part-per-thousand precision.
10. **Why is this not the same theory as $\Lambda$CDM?** Because $\Lambda$CDM treats $\Lambda$, $\Omega_\text{DM}$, and $\Omega_b$ as fit parameters; here, all four density parameters are bulk-field profile integrals. Operationally indistinguishable in the sustaining mode regime probed in this chapter; physically and mechanistically different. The discriminator (Sabbath Boundary signature) appears in Ch 9.

## Key Deliverables (Foundations — derivation plan)

| # | Deliverable | Starts from | Ends at | Equation / Theorem |
|---|---|---|---|---|
| D1 | Cosmological-symmetry reduction of the Firmament induced metric | Vol 1 Ch 4 §4.7 (zone symmetry); Firmament embedding (Vol 1 Ch 5) | The induced 4D metric on the Firmament is FLRW: $ds^2_{4D} = -c^2 dt^2 + a^2(t)\,d\Sigma_k^2$ | Lemma 5.8.1, Eq (5.8.4) |
| D2 | First Friedmann equation from $tt$-component of EFE on FLRW Firmament | Vol 5 Eq (5.1.34) (EFE); D1; Waters stress-energy from Vol 1 Ch 6 | $H^2 = (8\pi G_4/3)\sum_i \rho_i - kc^2/a^2$ | Theorem 5.8.1, Eq (5.8.13) |
| D3 | Acceleration equation from spatial-trace component of EFE | EFE; D1; Bianchi identity (Vol 5 §1.8) | $\ddot a/a = -(4\pi G_4/3)\sum_i(\rho_i + 3 P_i/c^2)$ | Theorem 5.8.2, Eq (5.8.18) |
| D4 | Continuity equation from $\nabla^\mu T_{\mu\nu}=0$ | Vol 5 Ch 1 §1.8; D2, D3 | $\dot\rho_i + 3 H(\rho_i + P_i/c^2) = 0$ for each non-interacting species | Eq (5.8.21) |
| D5 | Equation-of-state identification from Waters field profiles | Vol 1 Eqs 1.6.36–1.6.42 | $w_A = -1,\ w_B = 0,\ w_b = 0,\ w_r = 1/3$ — each derived from the bulk profile, not assumed | Eqs (5.8.23)–(5.8.26) |
| D6 | Critical density and $\Omega_i$ definitions | D2 | $\rho_\text{crit} = 3 H_0^2/(8\pi G_4),\ \Omega_i = \rho_i/\rho_\text{crit}$ | Eq (5.8.30) |
| D7 | Energy-budget identification from zone geometry | Vol 1 Ch 6 §6.7 (warp-factor profiles); D5 | $\Omega_A = 0.684,\ \Omega_B = 0.266,\ \Omega_b = 0.049,\ \Omega_r \sim 10^{-4}$ — geometric, not fit | Table 5.8.1 |
| D8 | Era-structure exact solutions | D2–D5 | Closed-form $a(t)$ in radiation, matter, and dark-energy domination; transition redshifts $z_\text{eq}, z_\Lambda$ | §8.7, Eqs (5.8.34)–(5.8.40) |
| D9 | Hubble parameter, age, and CMB temperature today | D2, D7, D8 | $H_0 = 67.4$ km/s/Mpc; $t_0 = 13.8$ Gyr; $T_0 = 2.725$ K | Eqs (5.8.42)–(5.8.45) |
| D10 | Test-suite verification | D1–D9; Research/Mathematical_Models/08_Cosmology/test_cosmology.py | All seven tests in test_cosmology.py reported with PASS/FAIL and numerical residuals | §8.11 |

## Figures

Following the figure rules from the chapter-writer skill: every spatial relationship, transformation, multi-step derivation, and concept with a natural visual metaphor needs a figure. Foundations density target: 2–4 per chapter (this chapter has more because the era structure and the Waters → fluid identification both need them).

| ID | Title | Placement | Type | What it shows | Why needed |
|---|---|---|---|---|---|
| Fig 5.8.1 | Brane FLRW: how zone symmetry reduces the 6D metric | §8.2, after Eq (5.8.4) | Schematic | The 6D bulk with $(\xi,\eta)$ extra dims, the Firmament $\Sigma$ as a 4-slice, and the cosmological-symmetry orbits on the Firmament that force the FLRW form | Spatial relationship: 6D ↔ 4D ↔ FLRW reduction is hard to follow in prose alone |
| Fig 5.8.2 | The Waters fields as cosmological fluid: bulk profile → Firmament stress-energy | §8.3, after Eq (5.8.10) | Diagram | $\Psi_A(\xi)$ profile in the $\xi$-direction (constant $V_A$ at the minimum), $\Psi_B(\eta)$ profile in the $\eta$-direction (VEV $v_B$ in the broken phase), and the projection arrows down to the Firmament stress-energy $T_{\mu\nu}^{(A)}, T_{\mu\nu}^{(B)}$ | Multi-step transformation: profile → KK projection → 4D fluid identification |
| Fig 5.8.3 | The two Friedmann equations as projections of the EFE | §8.4, after Eq (5.8.18) | Flowchart | EFE box → split into $tt$ component (Friedmann constraint) and trace-spatial component (acceleration); Bianchi identity arrow back to continuity | Multi-step derivation, more than 3 steps |
| Fig 5.8.4 | Equation of state for each species, derived from its bulk profile | §8.5, after Eq (5.8.26) | Comparison table + small inset diagrams | Four panels: $w_A=-1$ from $\Psi_A$ at potential minimum; $w_B=0$ from dilution of $v_B$ quanta; $w_b=0$ from Firmament dust; $w_r=1/3$ from massless Firmament modes | Why the equations of state are derived not assumed needs a side-by-side |
| Fig 5.8.5 | Density evolution $\rho_i(a)$ across cosmic history | §8.7, after Eq (5.8.34) | Plot | Log-log: $\rho_r \propto a^{-4}$, $\rho_m = \rho_B + \rho_b \propto a^{-3}$, $\rho_A = $ const; vertical lines at $z_\text{eq}\approx 3400$ and $z_\Lambda\approx 0.3$ | Quantitative comparison of three power laws is the most informative single figure in cosmology |
| Fig 5.8.6 | Scale-factor evolution $a(t)$ in three eras | §8.7, after Eq (5.8.40) | Plot | $a \propto t^{1/2}$ early, $a \propto t^{2/3}$ middle, $a \propto e^{H_\infty t}$ late; observer "today" marked at $t_0 = 13.8$ Gyr | The shape of cosmic history is one image, not a paragraph |
| Fig 5.8.7 | The 68/27/5 pie: where every percent comes from | §8.6, after Table 5.8.1 | Pie + sourcing arrows | Pie chart of the density parameters with arrows from each slice to the bulk-field integral that produces it | The "no fitting parameters" claim is most clearly supported by an attribution diagram |
| Fig 5.8.8 | Sustaining-mode coordinate time vs creation-epoch proper time (deferred to Ch 9) | §8.10, schematic only | Schematic | The two clocks: sustaining-mode coordinate clock running from $t_\text{Sabbath}$ forward; creation-epoch proper-time clock running 6 days; explicit *no claim* about how they connect — that is Ch 9 | Forward-link orientation; prevents confusion about what this chapter does and does not derive |
| Fig 5.8.9 | Reviewer's Ledger | §8.13 | Table | Every claim classified Derivation / Identity / Inheritance / Conjecture | Required for Vol 5 reviewer style |

## Problem Sets

Foundations chapters get problem sets graded computational → conceptual → challenge.

1. **Computational.** Given $\Omega_A = 0.684$, $\Omega_m = 0.315$, $\Omega_r = 10^{-4}$, $H_0 = 67.4$ km/s/Mpc, compute (a) $z_\text{eq}$, (b) $z_\Lambda$, (c) $t_0$ to three significant figures by numerical integration.
2. **Computational.** Show that the Friedmann constraint $H^2 = (8\pi G/3)\rho - kc^2/a^2$ is preserved by the acceleration and continuity equations (i.e., once it holds at one time, it holds for all time).
3. **Conceptual.** State the precise sense in which Waters Below "is" dark matter. What aspect of this identification is a *derivation* (from the bulk profile) and what aspect is a *re-labeling* (of the conventional name)?
4. **Conceptual.** The chapter derives $w_A = -1$ from $\Psi_A$ sitting at the minimum of $V_A$. Why does this not depend on the specific functional form of $V_A$?
5. **Conceptual.** Where in the derivation of the Friedmann equation is the assumption that the Firmament is spatially flat ($k = 0$) used? What would change if $k = +1$ or $k = -1$?
6. **Challenge.** Derive the deceleration parameter $q_0 = -\ddot a a / \dot a^2|_{t_0}$ in terms of the $\Omega_i$ and show it equals $-0.527$ for the framework's parameters. Compare with Planck 2018.
7. **Challenge.** Show that on a Firmament FLRW background, the Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$ is *equivalent* to the continuity equation for the total stress-energy. Why does this *not* require any of the species to be non-interacting individually?
8. **Challenge.** The chapter defers the Sabbath-Boundary discontinuity to Ch 9. Explain why the sustaining-mode Friedmann equations of this chapter are *internally consistent* without any reference to the boundary.

## Verification Criteria

- All ten "Why?" questions answered from the geometry, not by appeal to convention.
- Theorem 5.8.1 (Friedmann constraint) and Theorem 5.8.2 (acceleration equation) are *proved*, not asserted, with the chain (EFE → FLRW → component-split → Waters identification) shown step by step.
- Each equation of state is derived from the corresponding Waters field profile (Vol 1 Ch 6) with explicit reference to the equation number being inherited.
- The 68/27/5 split is presented as *output*, not input. Anywhere a number is fit to data, it is flagged in the Reviewer's Ledger as Identity (= empirical input) and the corresponding bulk-field calculation that produces it is cited.
- The test suite is run; the report is honest about pass rates.
- Forward links to Chs 9–12 are explicit.
- The chapter does *not* preach. The phrase "sustaining mode" appears with its zone-thermodynamic meaning (Vol 1 Ch 11), not as theology. The theological scaffolding of the four phases is introduced in Vol 1 Ch 11 and is *not* re-litigated here.
- The Skeptic reviewer's central question — *"is this a derivation or curve-fitting?"* — has a one-paragraph answer in §8.6 and a full answer in the Reviewer's Ledger.
- The Physicist reviewer's central question — *"do the Friedmann equations actually fall out of the Waters field equations, or do you need to put them in?"* — is answered by showing the chain explicitly in §8.3 → §8.4.

## Research Gaps (flagged in advance)

| Gap | Severity | Mitigation |
|---|---|---|
| G1: The warp-factor profiles $A_\xi, A_\eta$ that determine the $\Omega$'s are themselves derived in Vol 1 Ch 6 §6.7, but the *normalization constants* $\xi_A, \gamma$ are matched to the observed Firmament radius, not derived from a more fundamental scale | LOW | Cite Vol 1 Ch 6 §6.7 explicitly. The chapter does not claim to derive $\xi_A, \gamma$; it claims that, given $(\xi_A,\gamma)$, the *ratios* $\Omega_A : \Omega_B : \Omega_b$ come out as observed. This is what the Reviewer's Ledger calls an Inheritance, not a Derivation. |
| G2: $H_0$ comes out to 67.4 km/s/Mpc in the sustaining-mode calculation, matching CMB-inferred $H_0$ but not the local distance ladder ($\sim 73$). The chapter does not address the Hubble tension | LOW | The Hubble tension is a Sabbath-Boundary signature treated in Ch 9. This chapter is restricted to sustaining mode and is honest about the restriction. |
| G3: The "perfect fluid" approximation for $\Psi_B$ on the Firmament requires that the field has equilibrated to its broken-phase VEV; this equilibration is itself a Vol 3 Ch 8 phase transition not re-derived here | LOW | Cite Vol 3 Ch 8 explicitly. |
| G4: Non-interacting-species assumption — the cross-coupling between $\Psi_A$ and $\Psi_B$ is assumed to be zero on cosmological scales | LOW | Cite Vol 1 Ch 6 §6.4 (orthogonality of bulk profiles); flag as a small open question for Vol 6 |

## Word Count Target

10,000–13,000 words (30–40 pages). This is the load-bearing cosmology chapter and must be substantial but not bloated. The single architectural claim is that the Waters field IS the cosmological fluid; everything else is consequences. The chapter must not become a survey of FLRW cosmology — every section must advance the architectural claim.

## Notes on Voice

Feynman writing a textbook. Same register as Vol 5 Chs 1–7. The chapter has the mood of a quiet handoff: the equations of cosmology are not new, but the *origin* of every term is. The chapter should read like it has been waiting since Vol 1 Ch 6 to be written, because it has. No triumphalism about the 68/27/5 fit — those numbers are presented as pleasing consequences of geometry, with the Skeptic's reasonable objection (that "geometry" might be doing the work of "fitting") taken seriously and answered specifically. The theological undertones of "sustaining" are kept entirely in technical zone-thermodynamic terms; readers who recognize the resonance with Colossians 1:17 will recognize it without being preached at, and readers who don't will read a clean Foundations chapter on cosmology.

---

*End of CHAPTER_SPEC.md. Proceed to Phase 2 (CHAPTER_OUTLINE.md).*
