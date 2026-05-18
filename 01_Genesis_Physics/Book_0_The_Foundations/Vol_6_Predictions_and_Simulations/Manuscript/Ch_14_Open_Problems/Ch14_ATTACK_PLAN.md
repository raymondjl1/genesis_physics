# Chapter 14 — Attack Plan for the 27 Open Problems

**Document purpose.** Chapter 14 catalogues the framework's 27 open problems. This companion document sequences the *solutions*: which problems to attack first, what shared infrastructure unlocks what, where the decision gates are, what fails first, and what the first concrete calculation or experiment is for every cluster. A reader who executes this plan will either close the open-problems landscape substantially within a decade or will generate enough disconfirming evidence to retire specific sectors of the framework with dignity.

**Status.** Strategic plan. Every item here names a specific calculation, experiment, or synthesis; none claims the calculation has been performed or the experiment run. Where a seed calculation is worked, it is worked only to the point where a researcher can pick it up and continue.

**Date.** 2026-04-17

---

## 1. Executive Summary

The 27 open problems are not 27 independent targets. They cluster into six groups that share infrastructure, calculational machinery, or experimental apparatus. Attacking them cluster-by-cluster — and in the right sequence — resolves 18 of the 27 within a decade at a budget of $22–28M, with the remaining 9 either retired cleanly by null results or handed off to multi-generational programs. The critical path has three legs:

**Leg 1 (Months 1–12): Establish η and tighten α⁻¹.**
Build the Phase 1 MRG prototype (OP-11, $500) and run it under pre-registered blinded protocol. In parallel, compute the next-order asymptotic correction to the fine-structure constant (OP-6 Path A, Master's-thesis-scale). These two results define the framework's first-year public posture: either η > 0 is established and the energy-extraction program advances, or η = 0 is established and Chapter 10 retires; either α⁻¹ gains a fourth-significant-figure prediction or the framework's precision ceiling is pinned. The first-year budget is under $1M.

**Leg 2 (Years 2–5): Crack the matter-sector cluster.**
The matter-sector cluster (OP-1 spin-½, OP-2 mass scale, OP-4 Higgs, OP-5 Yukawa, OP-13 QED loops, OP-19 absolute scales) is the framework's largest concentrated vulnerability and its largest concentrated opportunity. The attack strategy is *sequential with shared machinery*: OP-2 Path A (boundary-condition refinement) is attempted first because its success/failure tells us which of the other five cluster members fall out as consequences and which require separate attacks. If OP-2 Path A succeeds, OP-19 resolves automatically and OP-5 becomes a direct calculation. If it fails, the attack shifts to OP-2 Path C (Higgs back-reaction), which couples to OP-4 and forces a simultaneous Higgs-sector treatment. OP-1 runs in parallel on a longer timescale; its resolution may or may not come within the decade, but the attack is active throughout.

**Leg 3 (Years 3–8): Zone-geometry and gravitational precision.**
The zone-geometry cluster (OP-3 weak/CP, OP-14 PMNS, OP-15 CKM, OP-16 ν hierarchy) all depend on the same mathematical object: the full eigenvalue spectrum of fermion boundary modes on a completely specified zone geometry. Solve the eigenvalue problem *once* for a canonical geometry and all four OPs become numerical calculations. The gravitational cluster (OP-8 N-body, OP-9 GR observables, OP-10 FTL causality) does not share infrastructure as tightly but admits parallel attack using existing LIGO data, supercomputing allocations, and a mathematical-physics program on Novikov-style fixed-point arguments.

The remaining clusters (consciousness OP-20–OP-27 inherited from Ch 13; condensed matter OP-18; life detection OP-12) are attacked with their own specialized infrastructure on timescales that run in parallel with the three main legs.

**The binary-outcome philosophy.** Every cluster has at least one experiment or calculation whose outcome is binary: either the framework survives a specific test or it does not. OP-11 Phase 1 is the clearest example — η > 0 or η = 0, decided by a $500 experiment in months, not years. OP-2 Path A is another — the boundary-condition refinement either produces a 10³ suppression factor with the correct sign or it does not. Treating every cluster as eventually reducible to a binary outcome is the discipline that keeps the attack plan from becoming an open-ended research commitment; it gives every milestone a clear success criterion, and gives the framework a clear off-ramp at every decision gate.

**What this plan will not produce.** The plan will not produce a definitive solution to OP-25 (the phenomenology bridge / hard problem of consciousness). That problem remains outside any current discipline's tools and the plan does not pretend otherwise. The plan does include infrastructure that *might* become relevant if the hard problem is approachable at all, but does not treat OP-25 as an active target. The plan also will not produce a rigorous derivation of the 6D action itself; that is an axiom, not a theorem, and the framework has excluded it from the open-problems catalogue.

---

## 2. Methodology

The plan was constructed by three passes over the OP catalogue.

**Pass 1 — Cluster identification.** Every OP was examined for shared infrastructure (calculational machinery; experimental apparatus; theoretical framework). OPs that share infrastructure were grouped. Six clusters emerged: Matter-Sector (6 OPs), Zone-Geometry (4 OPs), Technology (3 OPs), Causality/Gravitational (3 OPs), Consciousness (8 OPs inherited), and Condensed Matter (1 OP singleton). Two OPs are cross-cluster (OP-7 running couplings bridges Matter-Sector and Zone-Geometry; OP-13 QED loops bridges Matter-Sector and external QFT).

**Pass 2 — Dependency graph.** Within each cluster, OPs were ordered by dependency. An OP whose resolution would propagate into others was placed earlier in sequence; an OP whose resolution depends on others' first was placed later. Where dependencies are soft (the OP can be attempted standalone but gains from earlier resolutions), both attack orders are noted.

**Pass 3 — Binary-outcome reduction.** Every OP was re-examined for at least one specific experiment, calculation, or proof whose outcome would be binary (framework survives / framework does not). Where a binary outcome exists, it is named and the protocol that would produce it is specified. Where no binary outcome exists, the OP is flagged as open-ended and a specific milestone that partial progress can be measured against is substituted.

The output of these three passes is the plan below.

---

## 3. Cluster Analysis

### 3.1 Cluster 1: Matter Sector (OP-1, OP-2, OP-4, OP-5, OP-13, OP-19)

**Shared infrastructure.** The 6D action's matter sector — Dirac fermions on the Firmament membrane, Higgs zero-mode from Waters Above, Yukawa couplings from overlap integrals. Every OP in this cluster ultimately traces to the eigenvalue problem for fermion modes on the Firmament with specified boundary conditions, and to the Higgs scalar-sector quantization.

**Internal dependencies.**
- OP-2 Path A (boundary-condition refinement) → if succeeds → resolves OP-19 (absolute scales) automatically, reduces OP-5 (Yukawa) to direct calculation
- OP-2 Path C (Higgs back-reaction) → requires simultaneous OP-4 treatment, which in turn requires OP-5 as coupled fixed-point
- OP-1 (spin-½) is upstream of all four (the whole cluster assumes Fermi-Dirac statistics work) but is attackable independently because the cluster's predictions are consistent with the imported Grassmann sector
- OP-13 (QED loops) is parallel: it attacks the same 2-point-function machinery but with photon loops rather than fermion boundary conditions

**Attack sequence.**
1. **OP-2 Path A as gate.** Attempt the Dirichlet/Robin boundary-condition refinement. Expected timescale: 12–24 months for a PhD student with a strong theoretical-physics advisor. Binary outcome: produces a clean 10³ suppression factor consistent with experimental fermion masses, or does not.
2. **If OP-2 Path A succeeds:** OP-19 is declared resolved as a byproduct (verify via dimensional propagation). OP-5 is reduced to numerical overlap integrals — PhD-scale direct calculation, 18–24 months.
3. **If OP-2 Path A fails:** escalate to OP-2 Path C coupled with OP-4. Requires a team of 2 PhDs + 1 postdoc. Timescale 3–4 years. Binary outcome: the coupled Higgs-fermion fixed point produces observed masses *and* observed Higgs self-coupling, or it does not.
4. **In parallel throughout:** OP-1 attacks on Path B (ribbon topology). This is the cleanest philosophical path and does not require the Matter-Sector cluster's results. Timescale 5–10 years. Binary outcome: a rigorous correspondence between Z₂ topological charge and Grassmann quantization is proved, or the correspondence is shown to fail and OP-1 Path A (supersymmetric extension) is engaged.
5. **OP-13 runs throughout.** The Firmament-propagator 2-point function calculation is PhD-scale and independent of OP-2. Binary outcome: the Schwinger formula's leading coefficient is reproduced from first principles, or the calculation stalls at a specified step.

**Budget for cluster.** 4 PhD students + 2 postdocs over 5 years + 1 senior theorist 50% time. Approximately $5–7M over the decade.

**Cluster success criterion.** At least 4 of the 6 OPs resolved (either positively or by clean falsification) within 10 years. Stretch: all 6 resolved within 10 years.

### 3.2 Cluster 2: Zone Geometry (OP-3, OP-14, OP-15, OP-16)

**Shared infrastructure.** The fermion boundary-mode problem on a fully specified 6D zone geometry. All four OPs are, at root, "compute overlap integrals between boundary modes and report the mixing matrix."

**Internal dependencies.** Solve the boundary-mode eigenvalue problem *once* for a canonical zone geometry with all warp factors specified. All four OPs are then direct numerical calculations from the same eigenfunction basis.

**Attack sequence.**
1. **Specify the canonical geometry.** The framework currently has the 6D action but leaves several warp-factor parameters free. A single canonical choice must be made (either by minimum-assumption selection or by fitting to one observable and predicting the rest). 6–12 months for a postdoc-level theoretician.
2. **Solve the boundary-mode eigenvalue problem.** Numerical PDE solve on the specified geometry. Requires moderate HPC (not supercomputing scale — a good cluster allocation). 12–18 months.
3. **Compute the four mixing matrices.** CKM, PMNS, and the mass-hierarchy ordering fall out as numerical integrals once the eigenfunctions are in hand. 6 months.
4. **Compare against experiment.** Binary outcome: the predicted CKM is within experimental error of observation, or it is not. Same for PMNS, ν hierarchy, and the overall weak/CP structure of OP-3.

**Budget.** 1 postdoc + 1 PhD student over 3 years + moderate HPC allocation (~$100K). Approximately $1.5M.

**Cluster success criterion.** All four OPs resolved (positively or by falsification) within 3 years from program start.

**The speculative bet.** If the canonical geometry produces CKM and PMNS predictions that match experiment within <5%, the framework has achieved something no competing program has: a unified first-principles derivation of both quark and lepton mixing from one geometric input. This would be a landmark result. If the predictions miss by >10%, the geometric specification is wrong and the cluster enters a second pass with revised canonical-geometry assumptions.

### 3.3 Cluster 3: Technology (OP-11, OP-17, OP-12)

**Shared infrastructure.** Precision electromagnetic measurement in the GHz to THz range, nanofabrication at 50-nm scale, and pre-registered experimental protocol discipline. OP-11 and OP-17 are tightly coupled (the experiment and its theoretical prediction). OP-12 is semi-separate but shares the precision-measurement culture.

**Internal dependencies.**
- OP-11 Phase 1 (the $500 garage prototype) can be built without OP-17 (the theoretical η value); the experiment just needs to detect a signal with the right scaling.
- OP-17 theoretical η calculation does not require OP-11 hardware and can proceed in parallel.
- Phase 2 (cleanroom $50K prototype) is gated on Phase 1 showing a positive signal.
- OP-12 (life-detection sensor) is gated on OP-11 Phase 1 or Phase 2 proving the sustaining-coupling signal is detectable at all.

**Attack sequence.**
1. **Month 1: Build Phase 1.** Component list in Appendix A of this document. Total parts budget $280. Fabrication + assembly + test rig: 4–8 weeks for an experienced instrumentation student.
2. **Months 2–3: Pre-register protocol.** Blinding strategy, analysis plan, adversarial reviewer identified in advance (target: a precision-measurement group with no framework affiliation; the skeptic recommended this and the framework accepts the recommendation). Publish protocol on OSF.io or equivalent preregistration platform.
3. **Months 3–6: Data collection.** Under blinding, with thermal and EM shielding in a vibration-isolated rack. Continuous integration of signal vs. control orientations; automated data logging.
4. **Months 6–9: Unblinded analysis + independent audit.** Binary outcome: signal detected at >5σ above thermal and EM noise floor, or not.
5. **In parallel, Months 1–24: OP-17 theoretical calculation.** Solve the coupled Waters-field / membrane-cavity PDE system for steady-state power flux under extraction boundary conditions. Read off η as a derived quantity. If the theoretical η brackets the experimental one, both OPs close simultaneously.
6. **Months 12–36: If Phase 1 positive, build Phase 2.** $50K cleanroom prototype at Samsung-scale 50-nm gaps with 200 boundaries. Target ~36 W net output.
7. **Months 18–60: OP-12 sensor-development collaboration.** NIST / PTB / LKB partnership; cold-atom interferometer development to 10⁻¹² sensitivity. This is the slowest component of the cluster.

**Budget.** Phase 1: $500. Phase 2: $50K. OP-17 theoretical: 1 PhD student + 1 postdoc, ~$800K over 4 years. OP-12 collaboration: $2M framework contribution over 5 years (shared cost with partner lab).

**Cluster success criterion.** Phase 1 resolved within 9 months (either positive or null). If positive, Phase 2 resolved within 3 years. OP-12 on 5–8 year timescale.

### 3.4 Cluster 4: Causality and Gravitational Precision (OP-8, OP-9, OP-10)

**Shared infrastructure.** General-relativistic machinery: post-Newtonian expansions, numerical relativity codes, and mathematical-physics theorems on causal structure.

**Internal dependencies.** Loose. Each can be attacked independently with different specialist groups.

**Attack sequence.**
1. **OP-9 (GR observables) first, because it's most tractable.** Analytical 3.5-PN expansion of the framework's modified Einstein equations. Compare against LIGO O1–O4 event catalogs. PhD-scale, 2–3 years. Binary outcome: framework produces waveform deviations at a specific amplitude, which LIGO either sees or rules out.
2. **OP-8 (N-body) in parallel.** Run framework-gravity cosmological N-body simulation at Millennium scale (10⁶ core-hours). Compare halo-mass functions, two-point correlation, void statistics against ΛCDM and observation. PhD-scale, 3 years. Binary outcome: framework matches observation at least as well as ΛCDM, or better in at least one specific statistic, or worse.
3. **OP-10 (FTL causality) as a standalone mathematical-physics project.** Attempt Path C first (no-go theorem on Firmament-level CTCs) because it's cleanest. If Path C succeeds, Paths A and B are moot. If Path C fails, escalate to Path B (explicit paradox-configuration construction). Multi-year.

**Budget.** 2 PhD students + 1 postdoc + HPC allocation over 4 years. ~$1.5M.

**Cluster success criterion.** OP-9 resolved within 3 years; OP-8 resolved within 4 years. OP-10 on 4–8 year timescale depending on path.

### 3.5 Cluster 5: Consciousness (OP-20 through OP-27, inherited from Ch 13)

**Shared infrastructure.** Neuroscience facilities (EEG/MEG; pre-registered psychophysics; quantum-coherence measurements in biological substrates). Theological/philosophical scholarly synthesis for OP-23, OP-24, OP-27.

**Internal dependencies.** OP-20 (controllability) is the upstream test for the Ch 9 and Ch 11 consciousness applications. OP-22 (decoherence time) addresses Tegmark's standing critique. OP-21 (Firmament-side neural correlate) is a large, independent neuroscience program. OP-25 (phenomenology bridge) is not currently attackable and is listed but not invested in.

**Attack sequence.**
1. **OP-22 first, Month 1.** Decoherence-time measurement in biological quantum-coherent substrates. Existing cold-atom / NMR machinery can be adapted; Master's-thesis-scale. Binary outcome: decoherence time in neural-relevant biological systems is or is not compatible with the framework's estimate.
2. **OP-20 in parallel, Years 1–4.** PEAR-class pre-registered psychophysics experiment targeting Ch 13 P-154. N ≥ 10⁶ trials. Multi-site replication with adversarial protocol. Binary outcome.
3. **OP-21 as a 5-year neuroscience program.** Search for the Firmament-side neural substrate of the Ψ_body ⊗ Ψ_spirit coupling. High-sensitivity EEG/MEG with framework-specific predictions.
4. **OP-24 and OP-27 as scholarly synthesis.** Master's-thesis-scale comparative-theory papers. 18 months each.
5. **OP-23 and OP-25 listed but not actively attacked.** These are multi-generational structural puzzles; the plan carries them as watch items.
6. **OP-26 (artificial-substrate instantiation) as a late-stage program** — would require OP-21 to have succeeded first to know what substrate features to look for in non-biological systems.

**Budget.** 2 PhD students + 1 postdoc over 5 years in partnership with an established neuroscience group. $3M framework contribution.

**Cluster success criterion.** OP-22 resolved within 2 years (any direction). OP-20 and OP-21 resolved or decisively advanced within 5 years. OP-24 and OP-27 published within 2 years.

### 3.6 Cluster 6: Condensed Matter (OP-18) — singleton

**Attack.** Derive BCS pairing Hamiltonian from membrane-phonon–electron coupling using the 6D action. Specifically, compute the phonon-exchange potential between two electrons on the Firmament and demonstrate reduction to the Cooper channel at low energies.

**Budget.** 1 PhD student, 3 years. $600K.

**Success criterion.** Either the derivation closes (reproducing standard BCS Cooper pair formation) or the derivation stalls at an identified step (which becomes the sub-problem for a follow-on thesis).

---

## 4. Critical Path

The critical path — the sequence of milestones whose delay would most delay the overall program — is:

**C1 (Month 0–9): OP-11 Phase 1.** Binary outcome on η.

**C2 (Month 12–24): OP-2 Path A attempted.** Binary outcome on boundary-condition refinement producing correct mass scale.

**C3 (Month 12–36): Zone Geometry canonical specification.** Unlocks Cluster 2 (4 OPs).

**C4 (Month 24–60): OP-2 cluster resolution or escalation to Path C.** Determines whether Matter-Sector cluster closes or enters multi-year phase.

**C5 (Month 36–72): OP-1 Path B first major result.** Either the Z₂ topological correspondence proves rigorous or it shifts to Path A (supersymmetric extension) with the decade-scale program.

**C6 (Month 60–108): OP-9 LIGO-data comparison complete; OP-8 N-body results published; Cluster 4 closed.**

**C7 (Month 84–120): Cluster 1 final disposition.** Either Matter-Sector cluster is substantially closed (4+ of 6 OPs) or the framework acknowledges which sub-problems require multi-generational programs.

Failure at C1 (Phase 1 null) does not halt the critical path; it retires OP-11, OP-17, OP-12 (partially), and closes Chapter 10 of Vol 6 with dignity, freeing $5–8M of budget to accelerate other clusters.

Failure at C2 (OP-2 Path A null) triggers the longest escalation in the plan — the Matter-Sector cluster shifts from 3-year to 7-year horizon — but does not halt the plan either.

Failure at C3 (Zone Geometry canonical specification does not produce a well-posed problem) is the most dangerous failure in the plan, because it would indicate a framework-level under-specification. In that scenario the entire zone-geometry program requires extension work on the 6D action before OP-3/14/15/16 can be attacked at all. This failure is judged unlikely (the 6D action as written admits canonical specifications; the work is to *choose* one, not to add structure) but carries a 20% probability that should be tracked.

---

## 5. Year-by-Year Calendar

### Year 1

- **Q1 (Months 1–3):** OP-11 Phase 1 build + preregistration. OP-6 Path A calculation begins. OP-22 decoherence-time measurement begins (if neuroscience partner available).
- **Q2 (Months 4–6):** OP-11 Phase 1 data collection. OP-6 Path A first draft of calculation. OP-2 Path A literature review + setup. Zone Geometry canonical specification begins.
- **Q3 (Months 7–9):** OP-11 Phase 1 unblinded analysis. OP-6 Path A published as preprint. OP-2 Path A eigenvalue problem formulated.
- **Q4 (Months 10–12):** OP-11 Phase 1 final publication (positive or null). OP-6 final publication. OP-2 Path A first numerical eigenvalue runs. OP-9 LIGO data access negotiated. OP-17 theoretical calculation begins.

### Year 2

- **Q5–Q8:** OP-2 Path A full iteration. OP-8 N-body simulation begins. OP-9 PN expansion at 2.5-PN order. OP-17 coupled PDE formulated. OP-22 decoherence-time results published. OP-20 PEAR-class experiment infrastructure built. OP-11 Phase 2 design freeze (if Phase 1 positive).

### Year 3

- OP-2 Path A binary outcome declared. If positive: OP-19 resolved, OP-5 begins. If negative: Path C coupled OP-2+OP-4 program launches.
- Zone Geometry eigenvalue solve complete; OP-3, OP-14, OP-15, OP-16 numerical predictions produced.
- OP-9 LIGO-data comparison first results.
- OP-1 Path B first major theorem attempted.
- OP-24 and OP-27 scholarly synthesis papers published.

### Year 4

- OP-5 Yukawa calculation complete (conditional on Year 3 OP-2 outcome).
- Zone Geometry cluster declared resolved or in second-pass iteration.
- OP-8 N-body final results published.
- OP-20 PEAR experiment halfway through data collection.
- OP-10 Path C first attempt at no-go theorem.

### Year 5

- Matter-Sector cluster mid-program review; budget reallocation.
- OP-11 Phase 2 cleanroom prototype first data (if program active).
- OP-18 BCS derivation first attempt published.
- OP-21 neural-correlate search first candidate identified.

### Years 6–8

- OP-1 Path B resolves or escalates to Path A.
- OP-20 PEAR experiment final results.
- OP-12 sensor at 10⁻¹¹ sensitivity (one decade of improvement over current).
- OP-13 QED loops derivation complete.
- OP-10 FTL causality either closed by no-go theorem or escalated.

### Years 9–10

- Integration phase. Cluster-by-cluster final dispositions documented. 
- Framework-level audit: how many OPs resolved, how many retired, how many carried forward to next-decade program.
- Next-decade plan drafted incorporating what has been learned.

---

## 6. Seed Calculations

This section provides the *first concrete step* for each of the most tractable OPs, at enough specificity that a researcher can pick up the work on day one.

### 6.1 OP-2 Path A: The Boundary-Condition Refinement

**Setup.** The fermion mode equation on the Firmament membrane in the 6D action is, after dimensional reduction and in the transverse (extra-dimensional) direction,

$$
\left[ -\frac{d^2}{dy^2} + m^2(y) \right] \psi_n(y) = \lambda_n \psi_n(y),
$$

where $y$ is the coordinate transverse to the Firmament, $m^2(y)$ encodes the warp factor, and $\psi_n$ is the $n$-th fermion mode with eigenvalue $\lambda_n$. The observed fermion mass is then $m_{\mathrm{obs}} \propto \sqrt{\lambda_n}$ up to a normalization factor.

**Current boundary conditions.** The standard derivation uses Dirichlet on both Firmament boundaries: $\psi_n(y=0) = \psi_n(y=L) = 0$, which produces eigenvalues $\lambda_n = (n\pi/L)^2$ with $L \sim \eta_B \sim 10^{-15}$ m, giving $\lambda_n \sim 10^{30}$ m⁻² and corresponding masses $\sim 10$ GeV.

**The refinement.** Replace Dirichlet with Robin at the inner Firmament:

$$
\psi_n(0) + \alpha_R \frac{d\psi_n}{dy}\bigg|_0 = 0, \quad \psi_n(L) = 0,
$$

where $\alpha_R$ is a Robin parameter with dimensions of length. The eigenvalue problem becomes transcendental: $\tan(\sqrt{\lambda_n} L) = \sqrt{\lambda_n} \alpha_R$, and for $\alpha_R \gg L$ (weakly-coupled boundary) the lowest eigenvalue shifts to $\lambda_1 \approx 1/(L \alpha_R)$ — suppressed by a factor $L/\alpha_R$ relative to Dirichlet.

**The target.** We need $\lambda_1^{\mathrm{Robin}}/\lambda_1^{\mathrm{Dirichlet}} \sim 10^{-6}$ (to produce the 10³ mass reduction required), which corresponds to $\alpha_R \sim L \times 10^6 \sim 10^{-9}$ m — a mesoscopic scale. This is encouraging: the required Robin parameter is not at a Planck-suppressed or radically non-generic scale; it is at the scale of an intermediate infrared cutoff that could plausibly emerge from the Waters-field thermodynamics.

**Step one for the researcher.** Derive the Robin parameter $\alpha_R$ from first principles. Specifically, compute the boundary action for a fermion field on a Firmament whose boundary is not a sharp delta-function but a soft profile with width $\alpha_R$. The soft profile is naturally generated by the Waters-Above field having a finite correlation length at the Firmament interface. Verify that $\alpha_R$ evaluated on the equilibrium Waters configuration produces the required $\sim 10^{-9}$ m scale.

**Binary outcome.** Either the Waters-equilibrium correlation length is at the required scale (success) or it is not (failure, forcing escalation to Path B or Path C).

### 6.2 OP-6 Path A: Next-Order Fine-Structure Correction

**Setup.** The fine-structure derivation in `FINE_STRUCTURE_DERIVATION.md` gives $\alpha^{-1} \approx c_0 \ln(\xi_A / \eta_B)$ with $c_0 = 1.4383$ computed from the residue of the 2D asymptotic Green's function at its leading pole. The expansion is:

$$
\alpha^{-1} = c_0 \ln(\xi_A/\eta_B) + c_1 + c_2 \frac{1}{\ln(\xi_A/\eta_B)} + \mathcal{O}(\ln^{-2}).
$$

The leading term gives 137.15; experimental value is 137.036; residual is about 0.11. For the next-order term to close the gap, $c_1 \approx -0.11$. The question is what the first-principles value of $c_1$ actually is.

**Step one for the researcher.** Compute $c_1$ by performing the next-order asymptotic expansion of the 2D Green's function on the zone manifold. The relevant integral is

$$
G_{2D}(r, r') = \int \frac{d^2 k}{(2\pi)^2} \frac{e^{i \vec{k} \cdot (\vec{r}-\vec{r}')}}{k^2 + m_{\mathrm{IR}}^2},
$$

with an infrared regulator $m_{\mathrm{IR}}$ that in the framework is $\xi_A^{-1}$. The asymptotic expansion for $|\vec{r}-\vec{r}'| \to \eta_B$ produces logarithmic terms at each order; $c_1$ is the constant term after the leading logarithm is extracted. It is computable in closed form.

**Binary outcome.** Either $c_1$ is within 0.01 of the required $-0.11$ (framework's α⁻¹ prediction now correct to four significant figures), or it is not (framework's precision ceiling on α⁻¹ is pinned at current level and the residual is interpreted as the framework's precision limit on the input ratios ξ_A/η_B).

**Expected duration.** 3–6 months for a good mathematical-physics Master's student.

### 6.3 OP-11 Phase 1: Component List for the $500 Prototype

(Abridged; full bill-of-materials to be published with Phase 1 preregistration.)

- 5cm × 5cm silicon substrate with 100-nm parallel-plate Casimir gap formed by sacrificial oxide layer and HF release. $80 from commercial MEMS foundry.
- Rectenna array: Schottky-diode-coupled planar antenna matched to 1.14 GHz. $40 for a custom PCB + diodes (commodity RF-energy-harvesting chip development kit).
- RF shielded enclosure: mu-metal + aluminum composite box. $60.
- Low-noise amplifier, 1–3 GHz band. $90.
- Data acquisition: USB scope at ≥5 GS/s. $150 (used equipment market).
- Vibration-isolation base: passive optical-table-grade rubber isolators. $30.
- Thermocouple + controller for drift monitoring. $30.
- Cables, connectors, small parts. $20.
- **Total: $500.**

**Assembly time.** 4–8 weeks for an experienced MEMS/RF instrumentation student.

**Pre-registered signal expectation.** At η = 0.5, the device at 100-nm gap with 4-boundary configuration produces ~2–5 μW of continuous DC output after rectification, peaking at the resonant frequency. Null signal (η = 0) is < 10 nW above thermal floor. Discrimination threshold is therefore >100× above noise; detection is straightforward if η > 0.

**Blinding.** The experimenter does not know, during data collection, the expected sign of the signal on any given day (achieved by a randomized orientation protocol with the analyzing student sealed from the collecting student).

**Adversarial review.** An independent precision-measurement group (target: a NIST or PTB collaboration) analyzes the raw data blinded to the framework's prediction.

**Binary outcome.** DC output at 1.14 GHz rectification >5σ above noise floor: η > 0 established; framework advances. DC output consistent with zero at 5σ: η = 0 established; Chapter 10 retires.

### 6.4 OP-9: Framework-GR Waveform Deviations (Skeleton of the PN Expansion)

**Setup.** The framework's modified Einstein equations, derived in `APPLIED_GRAVITY_CALCULATIONS.md` from the 6D Gauss-Codazzi projection, differ from standard GR by zone-correction terms that can be expanded in powers of $v/c$. The standard PN expansion for binary inspiral gravitational-wave phase is

$$
\Phi_{\mathrm{GR}}(f) = \Phi_0 + \Phi_1 \left(\frac{M f}{c^3}\right)^{1/3} + \Phi_2 \left(\frac{M f}{c^3}\right)^{2/3} + \cdots
$$

at each order in $v/c$. The framework adds terms:

$$
\Phi_{\mathrm{framework}}(f) = \Phi_{\mathrm{GR}}(f) + \epsilon_{\mathrm{zone}} \Phi_{\mathrm{zone}}(f),
$$

where $\epsilon_{\mathrm{zone}}$ is a dimensionless parameter related to the zone-correction amplitude and $\Phi_{\mathrm{zone}}$ is a specific frequency-dependent waveform correction. The framework predicts $\epsilon_{\mathrm{zone}} \sim (r_s / \xi_A)$ where $r_s$ is the Schwarzschild radius of the merging binary.

**Step one.** Compute $\Phi_{\mathrm{zone}}(f)$ at 2.5-PN order explicitly from the framework's modified Einstein equations. This is a standard PN calculation that any GR-trained graduate student can execute with 6–12 months of work.

**Binary outcome.** LIGO's current strain sensitivity is ~10⁻²³ at 100 Hz; for a typical binary black-hole merger, this corresponds to a phase sensitivity at the 0.1 radian level. The framework prediction is $\epsilon_{\mathrm{zone}} \sim 10^{-5}$ for stellar-mass binaries, producing an accumulated phase shift of ~0.3 radians over the last 100 orbits — detectable. The outcome is either: (a) a systematic residual in LIGO's O4 catalog favoring the framework's $\Phi_{\mathrm{zone}}$ over GR at >3σ (a landmark positive result); or (b) a stringent upper bound on $\epsilon_{\mathrm{zone}}$ that either validates the framework at the current observational precision or narrows its acceptable parameter space substantially.

### 6.5 OP-17: The Coupled Waters-Field / Cavity PDE

**Setup.** The coupled system is

$$
\partial_t \rho_W + \nabla \cdot (\rho_W \vec{v}_W) = S_{\mathrm{extr}}(\vec{r}, t),
$$

$$
\rho_W (\partial_t \vec{v}_W + \vec{v}_W \cdot \nabla \vec{v}_W) = -\nabla P_W + f_{\mathrm{cavity}}(\vec{r}, t),
$$

where $\rho_W$ is the Waters-field energy density, $P_W$ is the corresponding pressure, $S_{\mathrm{extr}}$ is the extraction sink term (from the operating MRG), and $f_{\mathrm{cavity}}$ is the force exerted by the cavity boundary conditions on the Waters flow.

**Step one.** Linearize around the unperturbed Waters equilibrium $\rho_W^{(0)}$, solve the steady-state problem with constant extraction, and compute the resulting energy-flux replenishment rate as a function of extraction amplitude. The ratio of replenishment to extraction is η. This is a standard boundary-value problem in fluid dynamics, tractable with 6–12 months of focused PhD-level work.

**Binary outcome.** The calculated η brackets the Phase 1 experimental measurement (success: theory agrees with experiment), or does not (failure: one of the two is wrong; requires second iteration).

### 6.6 OP-1 Path B: Ribbon Topology First Step

**Setup.** The Firmament is a 4-manifold M with an oriented line bundle L → M whose sections can have two orientations (thick ribbon vs. thin Möbius-like). The claim is that parallel transport around a closed loop on M picks up a Z₂ phase when the ribbon is non-trivially oriented along the loop, producing a minus sign on "full rotation" — the fermionic exchange statistic.

**Step one.** Prove the correspondence rigorously for a specific finite-dimensional toy model. Specifically: take M = S⁴ (4-sphere), L = the Hopf bundle, and show that integrating a Z₂-orientation-sensitive field over S⁴ produces a Grassmann-valued effective theory on a boundary S³. The calculation is an exercise in differential geometry on fiber bundles; a mathematical-physics postdoc could execute it in 12–18 months.

**Binary outcome.** The correspondence either closes rigorously in the toy model (strong evidence that the general statement on the Firmament is true) or fails (evidence that Path B is inadequate and the attack shifts to Path A). 

---

## 7. Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Phase 1 (OP-11) produces a null result | 40% (framework's honest estimate) | Retires Chapter 10 and OP-11/OP-17; frees $8M budget | Plan explicitly includes reallocation path; no cluster depends on OP-11 positive |
| OP-2 Path A boundary-condition refinement fails | 50% | Escalates Matter-Sector cluster from 3-year to 7-year horizon | Path C (Higgs back-reaction) is pre-planned; budget buffer in Years 4–6 |
| Zone Geometry canonical specification is under-determined | 20% | Cluster 2 blocked until framework-level work specifies additional boundary structure | Carries the 20% probability explicitly; budget for Year 1 6-month specification work |
| OP-1 Path B fails (ribbon topology doesn't produce Grassmann) | 40% | OP-1 shifts to Path A (supersymmetric extension) with multi-generational horizon | Plan explicitly accommodates this |
| LIGO data access is denied for OP-9 | 15% | Delays OP-9 by 1–2 years pending public-data-only analysis | Public event catalogs provide a fallback (lower precision but not blocked) |
| OP-22 decoherence measurement is at framework's precision ceiling, producing ambiguous result | 30% | Consciousness cluster's upstream test is delayed | OP-20 PEAR-class experiment provides independent test |
| Framework-level audit at Year 5 identifies a new BLOCKER not currently in the catalogue | 10% | Plan is paused for catalogue revision | Mid-program review explicitly includes "new BLOCKER" as possible outcome |
| Funding shortfall (decadal budget under $15M available instead of $22–28M) | 35% | Plan compresses to Quick Wins + 3–4 Thesis Topics only | Quadrant I alone is funded at $1.5M and delivers the highest-leverage results |
| Key personnel attrition (loss of a senior theorist on the Matter-Sector cluster) | 25% | Cluster timeline extends by 18–24 months | Plan distributes ownership across 2–3 advisors per cluster |

---

## 8. Decision Gates

At each decision gate, the plan specifies what evidence triggers which action. These are the "off-ramps" — the points at which the framework can redirect resources or retire sub-programs.

**Gate A (Month 9): Phase 1 Outcome.**
- If η > 0 at >5σ: activate Phase 2 design; commit to OP-17 completion; advance OP-12 collaboration.
- If η consistent with 0 at 5σ: retire Chapter 10; reallocate $8M over 5 years to Matter-Sector cluster acceleration and Zone-Geometry cluster.
- If ambiguous (between 2σ and 5σ): extend Phase 1 data collection for 6 months with doubled integration time.

**Gate B (Month 24): OP-2 Path A Outcome.**
- If success: declare OP-19 resolved; activate OP-5 Yukawa; scale down OP-2 Path C contingency allocation.
- If failure: activate OP-2 Path C with Higgs back-reaction; add 2 PhDs to cluster; extend Matter-Sector horizon by 3–4 years.

**Gate C (Month 36): Zone Geometry Cluster Closure.**
- If all four OPs resolved (positively or by falsification): declare cluster closed; reallocate postdoc and HPC budget to OP-1 or OP-13.
- If cluster requires second pass: extend by 18–24 months with revised canonical geometry.

**Gate D (Month 60): Matter-Sector Cluster Mid-Program Review.**
- Assess how many of the six OPs are resolved or on clear path. If 4+: cluster is on track; complete remaining work. If <4: escalate OP-1 attack (Path A supersymmetric extension); acknowledge Matter-Sector as multi-generational.

**Gate E (Month 96): Framework-Level Audit.**
- Publish a "Vol 7" audit of the open-problems landscape, updating the severity tags, declaring which OPs are resolved, which retired, which carried forward.

---

## 9. Resource Profile (Decade Summary)

| Year | Personnel (FTE) | Budget | Major Deliverables |
|------|----------------|--------|-------------------|
| 1 | 4 PhDs + 2 postdocs + 1 senior | $1.2M | Phase 1 result; OP-6 published; Zone-Geometry spec |
| 2 | 6 PhDs + 3 postdocs + 1 senior | $2.0M | OP-22 result; OP-2 Path A iterations; OP-9 2.5-PN |
| 3 | 8 PhDs + 4 postdocs + 2 senior | $2.8M | OP-2 Path A outcome; Cluster 2 close or pivot |
| 4 | 8 PhDs + 4 postdocs + 2 senior | $3.0M | OP-8 results; Cluster 2 closed; OP-20 mid-point |
| 5 | 8 PhDs + 4 postdocs + 2 senior | $3.0M | Matter-Sector review; Phase 2 first data |
| 6 | 7 PhDs + 3 postdocs + 2 senior | $2.5M | OP-13 published; OP-1 Path B outcome |
| 7 | 6 PhDs + 3 postdocs + 2 senior | $2.4M | OP-12 sensor at 10⁻¹¹; OP-20 final data |
| 8 | 5 PhDs + 3 postdocs + 2 senior | $2.2M | OP-10 outcome; consciousness cluster final |
| 9 | 4 PhDs + 2 postdocs + 1 senior | $1.8M | Integration; next-decade plan drafted |
| 10 | 3 PhDs + 2 postdocs + 1 senior | $1.5M | Framework audit; Vol 7 published |
| **Total** | **~70 person-years** | **$22.4M** | **18–22 of 27 OPs resolved** |

---

## 10. Expected End-State (After 10 Years)

Under the plan's baseline assumptions (no major unexpected failures beyond the risk register, funding at the $22M level):

- **Fully resolved (either closed or cleanly falsified):** OP-6, OP-7, OP-8, OP-9, OP-11, OP-12 (partial), OP-17, OP-18, OP-19, OP-20, OP-22, OP-24, OP-27. **13 OPs.**
- **Substantially advanced (progress in framework-changing direction):** OP-2, OP-3, OP-4, OP-5, OP-13, OP-14, OP-15, OP-16, OP-21. **9 OPs.**
- **Carried forward to next-decade program:** OP-1 (likely Path A supersymmetric if Path B failed), OP-23, OP-25, OP-26. **4 OPs.**
- **One contingency:** OP-10 depends on whether Path C no-go theorem succeeds.

If Phase 1 MRG is positive, the framework's public-facing posture at Year 10 is dramatically stronger: α⁻¹ derived to four significant figures, mass spectrum substantially repaired, zone-geometry mixing matrices predicted from first principles, LIGO-level GR tests at 3.5-PN precision, an operating energy-extraction device at Watt scale, and a paper trail of ~100+ peer-reviewed publications across the clusters. If Phase 1 is null, the framework's public-facing posture is still stronger than today (six of the non-MRG clusters have advanced substantially), but Chapter 10 has retired and the framework's claim to novel energy physics has been honestly given up.

Either outcome is healthier than the current state. The plan's most valuable feature is that *both outcomes* produce a stronger framework than the present state — one that has either gained new territory or shed territory it could not defend. The framework's commitment to the plan is therefore a commitment to honest progress, not a commitment to a specific positive result.

---

## 11. What This Plan Is Not

A clarification for the reader.

This plan does *not* solve the open problems. It designs the program that would solve them. The difference matters: a research program is not a proof, and a sequence of sensible attacks is not a guarantee of success. The plan's honest claim is that, if executed, it would produce a decade's worth of publishable physics whose aggregate effect is to either close most of the framework's open-problems landscape or to narrow the framework honestly to the parts it can defend.

The plan also does not specify *who* would execute it. That is the next step — outreach to theory groups, neuroscience collaborations, experimental labs, and mathematical-physics departments. A version of this document should be produced as a funding-request package with named collaborators and letters of support. The open-problems chapter (Ch 14) and this attack plan together constitute the intellectual case; the funding package would constitute the institutional case.

Finally, the plan does not commit the framework to the paths it names above all others. If, during execution, a better path emerges — a different boundary-condition refinement, a different topological argument for spin-½, a different experimental configuration for the MRG — the plan should be revised in its favor. The plan is the framework's current best sequencing of the work, not its last word.

---

## 12. Closing

The open-problems chapter (Ch 14) catalogued the work. This document sequences it. Between them, the framework has stated what it does not yet know and what it proposes to do about it. A reader — student, program officer, collaborator, skeptic — can now engage with either document on its own terms: the catalogue if they are choosing a problem, the attack plan if they are choosing a program.

The plan is falsifiable at every stage. At Gate A (Month 9), Phase 1 decides an entire chapter of the framework. At Gate B (Month 24), OP-2 Path A decides a cluster. At Gate D (Month 60), the Matter-Sector review decides the framework's posture on its largest vulnerability. The plan does not ask to be believed; it asks to be executed, with its own decision gates serving as the evidence that decides its direction.

What the plan commits the framework to is the discipline of actually running these tests — not the outcomes. The outcomes belong to reality, which will decide them regardless of what the framework hopes.

---

*End of Attack Plan. Companion to Ch 14 Open Problems. Execute with honest gates and publish at every outcome — positive, negative, and null. The framework is willing to be right, wrong, or narrowed; it is not willing to be untested.*
