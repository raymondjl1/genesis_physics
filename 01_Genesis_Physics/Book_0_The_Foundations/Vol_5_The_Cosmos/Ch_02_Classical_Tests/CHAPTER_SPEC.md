# Chapter Specification — Vol 5 Ch 2
## Classical Tests

**Product:** Foundations Vol 5 — The Cosmos
**Chapter:** 2
**Working Title:** Classical Tests
**Target length:** 30–40 pages (~10,000–14,000 words)
**Voice:** Feynman writing a textbook
**Status:** DRAFT

---

## Mission

Take the Einstein field equations derived in Chapter 1 — and the Schwarzschild metric (5.1.34) extracted from them — and confront them with every classical test that observational general relativity can throw at them. Compute each observable from first principles, compare to the best available data, report the full error bar honestly, and decide, test by test, whether the zone-architecture derivation of Chapter 1 is *predictively* correct or merely *algebraically* correct.

This chapter is where a reader who spent Chapter 1 wondering "does any of this touch reality?" gets their answer. By the end of §2.10 the reader should be able to look at each of the historical and modern confrontations of GR with the solar system, the binary pulsar, the Gravity Probe B gyroscopes, the Event Horizon Telescope image of M87*, and the LIGO chirp of GW150914, and say: **of these N tests, M agree with Genesis-Physics-derived GR at the ≲1% level; the remaining (N−M) show tensions that trace to the following sources of measurement or theoretical uncertainty, not to a failure of the framework.** The chapter makes that accounting, and it makes it honest.

The chapter does **not** introduce any new physics. Every formula it uses traces back to Chapter 1, Chapter 1 of Vol 2, or the 4D Einstein equations (5.1.22). Its job is **confrontation with data**, not derivation of new results.

---

## Requirements (from QUALITY_GATE.md, Vol 5)

| ID | Requirement | Where Met |
|----|-------------|-----------|
| R1 | Mercury perihelion precession derived from Schwarzschild geodesic, compared to observation | §2.2 |
| R2 | Solar light deflection derived from null geodesic, compared to 1919 + modern VLBI | §2.3 |
| R3 | Gravitational redshift derived from $g_{00}$, compared to Pound–Rebka and solar iron lines | §2.4 |
| R4 | Shapiro time delay derived from $g_{rr}$, compared to Viking / Cassini | §2.5 |
| R5 | Frame dragging (Lense–Thirring) derived from Kerr $g_{t\phi}$, compared to Gravity Probe B and LAGEOS | §2.6 |
| R6 | Geodetic (de Sitter) precession derived from parallel transport, compared to Gravity Probe B and lunar laser ranging | §2.7 |
| R7 | Modern PPN-framework high-precision tests summarized; Cassini bound on $\gamma$ reproduced | §2.8 |
| R8 | **Honest pass/fail accounting: full table of 11 tests with measured error bars and framework predictions; no cherry-picking** | §2.9 + §2.10 |
| R9 | Test-suite execution: `test_gr_observables.py` run, results reproduced in chapter, any test with error > 1% flagged and discussed | §2.9 |
| R10 | Known research gap (GitHub #8, GR observables precision) explicitly acknowledged and honestly characterized | §2.10 |

---

## Prerequisites (reader must already know)

- **Ch 1 of this volume:** The Einstein field equations (5.1.22); the Schwarzschild metric (5.1.34); the Kerr metric (5.1.41); Birkhoff uniqueness.
- **Vol 2 Ch 2 (Gravity from Zone Curvature):** The Newtonian limit $\nabla^2\Phi=4\pi G_4\rho$ as the leading-order reduction of (5.1.22); numerical value $G_4=6.6743\times 10^{-11}$ m³ kg⁻¹ s⁻².
- **Vol 2 Ch 8 (Gravitational Field Theory):** Linearized GR, the quadrupole radiation formula (which is reused, but not re-derived, for the Hulse–Taylor pulsar comparison in §2.8.2).
- **Vol 2 Ch 3 (Electromagnetism):** Photon as a null-geodesic probe; stationary-phase approximation for light propagation in a weak potential.
- **Vol 3 Ch 2 (Lagrangian Mechanics):** Calculus of variations; geodesic as extremum of the action $S=\int ds$.
- **Vol 3 Ch 5 (Central Force Problem):** Kepler orbit, effective potential formalism, the classical $u=1/r$ trick.
- **Vol 4 Ch 3 (Photons and Interactions):** Energy-frequency relation $E=h\nu$; gravitational redshift as a statement about photon frequency in a stationary frame.

## Forward dependencies (what this chapter establishes, used later)

- **Ch 3 (Gravitational Waves):** Reuses the binary-pulsar case study as the prototype of GW energy loss.
- **Ch 4 (Strong-Field Gravity):** Inherits the PPN-parameter framework to contrast weak-field tests with strong-field regimes.
- **Ch 5 (Black Holes as Zone Infrastructure):** Uses the M87* shadow measurement as the first observational tie-in for the membrane-puncture picture.
- **Vol 6 (Predictions):** Uses the pass/fail table of §2.9 as the GR-sector input to the overall predictions scorecard.

---

## "Why" chain (the but-why audit)

| Section | "But why?" question answered |
|---|---|
| 2.1 | Why do a whole chapter on tests after Ch 1 already showed the equations work? Because deriving an equation and confronting it with data are two different things, and the Physicist reviewer will demand both. |
| 2.2 | Why does Mercury precess at *43* arcsec/century and not, say, 4, or 4000? Where does the factor of $6\pi$ in the precession formula come from? |
| 2.3 | Why is the light-bending factor 4 rather than 2? What does the extra factor of 2 tell you about the *spatial* metric that Newton's theory misses? |
| 2.4 | Why does gravitational redshift depend only on $g_{00}$ and not on any other metric component? (Answer: because frequency is a time quantity.) |
| 2.5 | Why is the Shapiro delay *positive*? (Light slows down in a gravitational field, relative to the coordinate clock — but why does it slow down, and not speed up?) |
| 2.6 | Why does a rotating mass drag frames at all? (Answer: because the Kerr $g_{t\phi}$ is forced by stationary axisymmetry plus the Einstein equations; it cannot be set to zero.) |
| 2.7 | Why are the geodetic and Lense–Thirring precessions *different* physical effects, even though both are "precession of a gyroscope near a rotating Earth"? |
| 2.8 | Why do modern tests use the PPN framework rather than quoting "percent agreement"? (Answer: the PPN framework separates the theory-specific predictions from the parameter-specific measurement.) |
| 2.9 | Why report the *full* pass-rate table, including the tests that look awkward? (Answer: because the alternative is cherry-picking, and cherry-picking is how frameworks die in review.) |
| 2.10 | Why is the Shapiro-delay result at ~16% worst-case discrepancy not a failure? (Answer: because the "observed value" being compared against in the test script is the historic Shapiro 1964 measurement with ~few-percent error bars, not the Cassini 2003 measurement at $10^{-5}$ precision — and when compared against Cassini through the PPN $\gamma$ parameter, the agreement is at the $10^{-5}$ level. The test-script comparison is correct but uses the *wrong* reference value, and §2.10 says so plainly.) |

---

## Key deliverables (Foundations = derivation plan)

### Derivation 1: Mercury perihelion precession
- **Starting point:** Schwarzschild geodesic in the equatorial plane (5.1.34).
- **Steps:**
  1. Effective potential $V_\text{eff}(r) = -GM/r + L^2/(2r^2) - GML^2/(c^2 r^3)$.
  2. The extra $1/r^3$ term (absent in Newton) is the direct fingerprint of the Schwarzschild $g_{rr}$ component.
  3. Transform $r\to u=1/r$ and linearize around circular orbit.
  4. Obtain $u(\phi) = u_0[1+e\cos(k\phi)]$ with $k=1-3r_s/(2p)$, where $p=a(1-e^2)$.
  5. Precession per orbit: $\delta\phi = 6\pi GM/[c^2 a(1-e^2)]$.
- **Numerical comparison:** 42.98 arcsec/century derived vs. 42.98±0.04 observed (modern consolidated value). Earlier data showed 43.03 ± few.
- **Equation numbers:** (5.2.1)–(5.2.12)

### Derivation 2: Solar light deflection
- **Starting point:** Null geodesic in Schwarzschild (5.1.34).
- **Steps:**
  1. Photon effective potential; null condition $ds^2=0$.
  2. Orbit equation in $u=1/r$: $d^2u/d\phi^2 + u = 3(r_s/2)u^2$ (no Newtonian term because $V_\text{eff}$ has no $-GM/r$ for massless particles of this parametrization, only the curvature term).
  3. First-order solution: $u=\cos\phi/b + r_s(1+\sin^2\phi)/(2b^2)$.
  4. Deflection angle: $\delta\theta = 4GM/(c^2 b)$.
  5. *Bookkeeping:* factor-of-2 from $g_{00}$ plus factor-of-2 from $g_{rr}$; Newton alone would give 2.
- **Numerical comparison:** 1.7516 arcsec (grazing the Sun) vs. 1.75±0.01 from 1919 (Eddington), consolidated modern VLBI at 0.04% agreement.
- **Equation numbers:** (5.2.13)–(5.2.22)

### Derivation 3: Gravitational redshift
- **Starting point:** $g_{00} = -(1-r_s/r)$ and the definition of proper time.
- **Steps:**
  1. Two stationary observers at $r_1$ and $r_2$.
  2. Ratio of proper-time intervals $d\tau_1/d\tau_2 = \sqrt{g_{00}(r_1)/g_{00}(r_2)}$.
  3. A photon climbing from $r_1$ to $r_2$ has $\nu_1/\nu_2 = \sqrt{g_{00}(r_2)/g_{00}(r_1)}$.
  4. Weak-field: $z \approx GM(1/r_1 - 1/r_2)/c^2 = \Delta\Phi/c^2$.
- **Numerical comparisons:**
  - Pound–Rebka tower (h=22.5 m): $z=2.46\times 10^{-15}$ predicted vs. $(2.57\pm 0.26)\times 10^{-15}$ observed (1960), refined to <1% later.
  - Solar iron lines: $z=2.108\times 10^{-6}$ predicted vs. $2.12\times 10^{-6}$ observed (~0.5%).
- **Equation numbers:** (5.2.23)–(5.2.30)

### Derivation 4: Shapiro time delay
- **Starting point:** Null radial propagation in Schwarzschild, reading the coordinate-time/proper-distance relation off $g_{rr}$.
- **Steps:**
  1. Coordinate time for light between $r_1$ and $r_2$: $t = \int dr/(c\sqrt{1-r_s/r})$.
  2. Weak-field expansion: $t \approx (r_2-r_1)/c + (r_s/2c)\ln(r_2/r_1)$.
  3. For a round-trip past a massive body with impact parameter $b$: $\Delta t = (4GM/c^3)\ln(4r_1r_2/b^2)$.
  4. **Explicit note:** the log-dependence on $r_1r_2/b^2$ is the "smoking gun"; a Newtonian potential would give no delay at all.
- **Numerical comparisons:**
  - Viking (1976, solar conjunction, $b\sim 1.7\times 10^7$ m): predicted 5.61 μs round-trip vs. 5.62 ± 0.02 μs (~0.2% agreement).
  - Cassini (2003, PPN framework, $\gamma$-measurement): $\gamma = 1 + (2.1\pm 2.3)\times 10^{-5}$. Our theory predicts $\gamma=1$ exactly. Agreement: $2\times 10^{-5}$, the best weak-field test of GR in existence.
  - **Explicit note on the test-script discrepancy:** The `test_gr_observables.py` Earth–Venus-grazing case uses the 1964 Shapiro measurement (Δt ≈ 200 μs, ~5–10% error bars) as the reference and reports ~16% error. That is the *1964-era measurement precision*, not a framework failure; see §2.10.
- **Equation numbers:** (5.2.31)–(5.2.42)

### Derivation 5: Frame dragging (Lense–Thirring)
- **Starting point:** Kerr metric (5.1.41), specifically the off-diagonal $g_{t\phi}$ component.
- **Steps:**
  1. Weak-field Kerr: $g_{t\phi} = -2GJ\sin^2\theta/(c^3 r)$ (keeping only leading-order in $a/r$).
  2. Equation of motion for a test-gyroscope spin vector via parallel transport along its worldline.
  3. Lense–Thirring precession frequency: $\Omega_\text{LT} = GJ/(c^2 r^3)$ for polar orbit, $2GJ/(c^2 r^3)$ for equatorial.
  4. For Earth: $\Omega_\text{LT} \approx 39$ mas/yr at GPB orbital altitude.
- **Numerical comparison:**
  - Gravity Probe B (2011 final results): measured $37.2 \pm 7.2$ mas/yr; predicted $39.2$ mas/yr. Agreement within 1σ.
  - LAGEOS I+II (Ciufolini 2004, 2016): $99 \pm 5\%$ of GR prediction for nodal precession.
- **Equation numbers:** (5.2.43)–(5.2.52)

### Derivation 6: Geodetic (de Sitter) precession
- **Starting point:** Schwarzschild parallel transport of a gyroscope on circular orbit.
- **Steps:**
  1. Parallel-transport equation $dS^\mu/d\tau + \Gamma^\mu_{\alpha\beta}u^\alpha S^\beta = 0$.
  2. Project onto orbital basis; non-zero Christoffel symbols of Schwarzschild do the work.
  3. Result: $\Omega_\text{geo} = (3GM/2c^2 r)\cdot \omega_\text{orbit}$, or $\approx 6.6$ arcsec/yr at GPB altitude.
- **Numerical comparison:**
  - GPB: measured $6\,602 \pm 18$ mas/yr; predicted $6\,606$ mas/yr. Agreement at 0.3%.
  - Lunar laser ranging: 0.6% agreement with de-Sitter prediction for Earth-Moon system.
- **Equation numbers:** (5.2.53)–(5.2.60)

### Derivation 7: PPN framework and modern bounds
- **Starting point:** Schematic expansion of a general metric theory's static-spherical solution:
  $g_{00}=-1+2U-2\beta U^2+\ldots$, $g_{ij}=\delta_{ij}(1+2\gamma U + \ldots)$.
- **Identification:** GR (and our derivation) has $\beta=\gamma=1$.
- **Current bounds:**
  - Cassini (Shapiro PPN): $\gamma-1 = (2.1\pm 2.3)\times 10^{-5}$.
  - Mercury perihelion (combined $\beta,\gamma$): $|2\gamma-\beta-1| < 3\times 10^{-5}$.
  - MESSENGER (perihelion): $\beta-1 = (-4.1\pm 7.8)\times 10^{-5}$.
  - Lunar laser ranging (Nordtvedt effect): $\eta_N \equiv 4\beta-\gamma-3 = (4.4\pm 4.5)\times 10^{-4}$.
- **Equation numbers:** (5.2.61)–(5.2.68)

### Derivation 8: Honest pass/fail accounting (§2.9)
- Full table of all 11 tests from `test_gr_observables.py` with:
  - Test name
  - Observable and derived formula (with Ch 2 equation number)
  - Predicted value (from our code)
  - Observed value with error bar and reference
  - Fractional agreement
  - Status: PASS (<1%) / PASS-with-note (1–10%) / NEEDS-WORK (>10%) / FRAMEWORK-EXACT ($<10^{-4}$)
- Narrative discussion of each non-<1% entry.

### Derivation 9: Honest characterization of GR-observables precision gap (§2.10)
- State GitHub Issue #8 (Vol 5, MEDIUM severity).
- Characterize the three distinct sources of "imprecision" in the test suite:
  1. **Test-script reference values are historical, not current best.** (Example: Shapiro delay uses 1964 data.)
  2. **Hawking temperature test compares rounded constants, not measurement.** (Error ≪ physical.)
  3. **Gravitational time dilation test compares simplified slave-clock estimate.** (1.47% "error" is arithmetic rounding in the reference, not a framework prediction.)
- Commit to a follow-up work item: update `test_gr_observables.py` to use modern reference values and PPN-framework comparisons for the precision tests. (This is the action-closure for Issue #8.)

---

## Figure plan

| ID | Title | Placement | What it shows | Why needed | Type | Complexity |
|---|---|---|---|---|---|---|
| Fig 5.2.1 | Effective potential and Mercury's orbit | §2.2.2 | Two curves: Newtonian $V_\text{eff}(r)$ and Schwarzschild $V_\text{eff}(r)$, with the extra $1/r^3$ term shaded. Inset: unbound orbit in Schwarzschild traced over 100 periods showing the rosette. | Spatial + comparison: the rosette is the picture of Mercury's precession; the effective potentials show where the extra precession *comes from*. | Plot + trajectory | Medium |
| Fig 5.2.2 | Geometry of solar light bending | §2.3.1 | Ray trajectory grazing the Sun, with the deflection angle $\delta\theta$ marked at infinity. Labels: impact parameter $b$, Sun radius $R_\odot$, asymptotic directions. | Spatial: "the photon swings past the Sun" is the mental picture readers need. | Schematic | Simple |
| Fig 5.2.3 | Why factor 4, not factor 2 | §2.3.3 | Two panels side by side: Newtonian corpuscle (factor 2 from $g_{00}$ alone) and GR photon (factor 2 from $g_{00}$ + factor 2 from $g_{rr}$ = 4). A bar chart at right showing the contributions. | Conceptual: the famous 2+2 decomposition of the light-bending factor. | Comparison + bar | Simple |
| Fig 5.2.4 | Gravitational redshift: two observers in a tower | §2.4.1 | Pound–Rebka tower geometry, with photon emitted at the bottom and received at the top. Annotated: $\nu_\text{emit}$, $\nu_\text{obs}$, $\Delta\Phi=gh$. | Spatial: makes the tabletop GR test concrete. | Schematic | Simple |
| Fig 5.2.5 | Shapiro delay: time and space curvature | §2.5.2 | Top panel: light path past the Sun, with the integrated coordinate time $t(r)$ plotted as a function of path length. Bottom panel: log-log plot of delay vs. impact parameter showing the $\ln(r_1 r_2/b^2)$ dependence. | Spatial + data: the log scaling is the "smoking gun" and must be plotted. | Schematic + plot | Medium |
| Fig 5.2.6 | Frame dragging around a rotating Earth | §2.6.1 | Cutaway Earth with rotation axis. Ring of test gyroscopes orbiting equatorially; arrows show the $g_{t\phi}$-induced precession direction (same sense as rotation). Inset: Gravity Probe B spacecraft. | Spatial: frame dragging is genuinely unfamiliar; the cutaway is worth 1000 words. | Cutaway | Complex |
| Fig 5.2.7 | Geodetic vs. Lense–Thirring: two different effects | §2.7.3 | Two panels: (a) non-rotating mass, gyroscope precesses due to moving through curved spacetime (geodetic); (b) rotating mass, gyroscope precesses due to being dragged by the rotating field (LT). A table at right lists: source, magnitude for GPB, measured value. | Conceptual: the distinction is constantly confused and a figure locks it in. | Comparison | Medium |
| Fig 5.2.8 | PPN parameter constraints over time | §2.8.4 | Timeline plot: year on x-axis (1915–2025), $\gamma-1$ upper bound on y-axis (log scale). Data points: 1919 Eddington ($\sim 30\%$), 1976 Viking ($\sim 10^{-3}$), 2003 Cassini ($\sim 10^{-5}$). Our framework's prediction as a horizontal line at 0. | Data: shows the precision landscape has improved by 4 orders of magnitude over a century, and that GR (and our derivation) has held to the same exact value the whole time. | Timeline + data | Medium |
| Fig 5.2.9 | Honest pass-rate table — the 11-test scorecard | §2.9.1 | 11×6 table rendered as a color-coded summary: green (<1%), yellow (1–10%), red (>10%), framework exact (<10⁻⁴) highlighted. Caption: "No cherry-picking: all 11 tests reported. Two test-script entries show apparent >1% disagreement; §2.10 traces both to the choice of reference value, not to the framework." | Accountability: the chapter's central honesty device. | Color table | Simple |

**Figure density:** 9 figures across 10 sections — at the top of the Foundations target for a 30–40 page chapter, justified because this is primarily a *data-confrontation* chapter and figures carry most of the persuasive load.

---

## Problem sets (Foundations requirement)

### Computational
- **P2.1** Starting from the Schwarzschild effective potential (5.2.3), compute Mercury's perihelion precession to three significant figures. Compare with the observed value 42.98 arcsec/century. Identify which input parameter (GM, a, e) dominates the uncertainty.
- **P2.2** For a photon grazing the limb of Jupiter ($R_J=7.00\times 10^7$ m, $M_J=1.898\times 10^{27}$ kg), compute the expected deflection angle in milliarcseconds. How does this compare to the angular resolution of modern VLBI (~10 μas)?
- **P2.3** A hydrogen-maser clock is flown 10,000 km above Earth for 3 hours. Compute the gravitational-redshift frequency offset (ignoring the special-relativistic correction, which is the subject of P2.4). Compare to GPS clock corrections.
- **P2.4** Derive the Shapiro time delay for radar echoes bounced off Venus at superior conjunction. Use $r_1=1$ AU, $r_2=1.72$ AU, $b=R_\odot$. Report the one-way delay in microseconds.

### Conceptual
- **P2.5** Explain *why* the coefficient in the light-bending formula is 4, not 2. Trace the factor of 2 contribution from each of $g_{00}$ and $g_{rr}$ and show that a Newtonian "ballistic photon" would see only the $g_{00}$ piece.
- **P2.6** Gravitational redshift depends only on $g_{00}$, not on $g_{ij}$. Explain physically why. (Hint: frequency is a time-quantity.)
- **P2.7** Consider the PPN parameters $\beta$ and $\gamma$. In what sense does the Cassini bound on $\gamma-1$ at the $10^{-5}$ level constrain Genesis Physics? (Answer: our framework predicts $\gamma=\beta=1$ identically, so any non-zero measurement would immediately falsify it.)

### Challenge
- **P2.8** Show that the Lense–Thirring precession for a polar-orbit gyroscope is half that of an equatorial-orbit gyroscope at the same altitude. Use only the Kerr $g_{t\phi}$ component and parallel transport.
- **P2.9** Compute the *combined* Gravity Probe B precession (geodetic + Lense–Thirring) for a polar orbit at 642 km altitude. Compare to the reported GPB result of $6\,602 \pm 18$ mas/yr (geodetic) and $37.2 \pm 7.2$ mas/yr (frame-dragging). Discuss the measurement challenges that led to the final error bars.
- **P2.10** The `test_gr_observables.py` test script reports a 16% error on Shapiro delay. Read the test source, identify which observational reference value is being compared against, and propose a one-line change to the script that uses the Cassini 2003 $\gamma$-measurement instead. Estimate the new pass tolerance.

---

## Verification criteria

- [ ] Every derivation cites Ch 1 (this volume) or a prior volume for its starting point.
- [ ] Every predicted numerical value has a corresponding observational reference with error bars and a citation.
- [ ] Equation numbers (5.2.1)–(5.2.70) (approximate).
- [ ] §2.9 reports all 11 tests from `test_gr_observables.py`, not a subset.
- [ ] §2.10 honestly addresses GitHub Issue #8.
- [ ] At least one test with >1% "error" is explicitly discussed and the discrepancy sourced to either measurement uncertainty or reference-value staleness.
- [ ] Word count 10,000–14,000.
- [ ] 9 figures specified; every `[FIGURE: ...]` placeholder in the draft has a matching entry in this spec.
- [ ] Self-review report produced.
- [ ] Physicist reviewer (simulated): pass.
- [ ] Skeptic reviewer (simulated): pass — cannot point to cherry-picking.

---

## Research gaps

- **GitHub #8 (MEDIUM):** GR observables precision. The test-script error tolerances are loose (5–20%) and the reference values are in some cases historical (1964 Shapiro, Pound–Rebka 1960) rather than current best. §2.10 characterizes this honestly and proposes an action item.
- **Lensing Einstein-ring test** (Test 6 of the research file, Test 5 of the test script): has ambiguous "agreement" because real galaxy-cluster lenses include dark-matter substructure. §2.9 reports as PASS-with-note and the chapter does not claim sub-percent agreement.

---

*End of CHAPTER_SPEC.md*
