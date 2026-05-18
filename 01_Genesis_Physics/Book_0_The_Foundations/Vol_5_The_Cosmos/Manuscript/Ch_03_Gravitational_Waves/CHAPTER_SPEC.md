# Chapter Specification — Vol 5 Ch 3
## Gravitational Waves

**Product:** Foundations Vol 5 — The Cosmos
**Chapter:** 3
**Working Title:** Gravitational Waves
**Target length:** 30–40 pages (~10,000–14,000 words)
**Voice:** Feynman writing a textbook
**Status:** DRAFT

---

## Mission

Take the full nonlinear Einstein field equations derived in Chapter 1 of this volume — the ones that issued from the 6D zone action via Kaluza–Klein reduction — and show that they possess *radiative* vacuum solutions. Extract those solutions in their two natural regimes: (i) the linearized regime far from any source, where gravitational waves propagate as small metric perturbations on a flat background, and (ii) the strongly nonlinear regime of the late inspiral, merger, and ringdown of a compact binary, where the full (5.1.22) must be integrated numerically. Compute the polarization content, the energy flux, the quadrupole generation formula, and the binary-inspiral waveform from first principles starting from (5.1.22). Predict the GW150914 chirp, compare to the LIGO/Virgo observation, and report any zone-architecture prediction that differs from textbook GR — explicitly, as a testable bound.

This chapter is the bridge between Vol 2 Ch 8 (where linearized GR was established as a weak-field fact about the 4D Einstein equations) and Vol 5 Ch 5–7 (where the strong-field black-hole interior must be handled without linearization at all). By the end of §3.10 the reader should (a) be able to derive the quadrupole formula from scratch, (b) understand why LIGO sees two polarizations and what a third or fourth would mean for the zone framework, (c) know how the (2,2,0) quasi-normal-mode frequency of a 65 $M_\odot$ Kerr remnant is computed, and (d) be able to read the published GW150914 inferred source parameters and recognize which features are "derivation output" versus "data input."

The chapter introduces no postulates. Everything traces to (5.1.22) and Vol 2 Ch 8. Where the zone architecture offers a genuine departure from textbook GR — a possible scalar breathing mode from the internal space, Firmament-tension corrections at strong field — the departure is stated, quantified, and flagged as a falsifier.

---

## Requirements (from QUALITY_GATE.md, Vol 5)

| ID | Requirement | Where Met |
|----|-------------|-----------|
| R1 | Linearized wave equation derived from full Einstein equations (5.1.22), gauge fixed, plane-wave solutions identified | §3.2 |
| R2 | Polarization content: standard GR's two transverse-traceless modes derived; the six-polarization classification for a general metric theory summarized; zone-architecture additions stated | §3.3 |
| R3 | Energy flux of a gravitational wave derived from the Isaacson effective stress-energy; numerical value for GW150914 peak reported | §3.4 |
| R4 | Quadrupole generation formula derived from retarded-wave solution of $\square \bar h_{\mu\nu}=-16\pi G_4 T_{\mu\nu}/c^4$ | §3.5 |
| R5 | Binary-inspiral waveform in the stationary-phase approximation; chirp mass as the leading waveform parameter; orbital-decay equation $da/dt = -\frac{64}{5}\frac{G_4^3}{c^5}\frac{m_1 m_2(m_1+m_2)}{a^3}$ rederived | §3.6 |
| R6 | Transition to strong field: post-Newtonian breakdown at ISCO explained; effective-one-body framework sketched; quasi-normal-mode spectrum of the final Kerr remnant computed for $(n,l,m)=(0,2,2)$ | §3.7 |
| R7 | LIGO/Virgo GW150914 comparison: chirp mass, inspiral frequency sweep, final-mass energy balance, ringdown frequency — all predicted from the derivations of §§3.5–3.7 and compared to Abbott et al. 2016 | §3.8 |
| R8 | **Zone-architecture predictions beyond standard GR:** scalar breathing mode from the internal-space radion; Firmament-tension correction to orbital decay; explicit sensitivity floors at which each would become visible to current and planned detectors | §3.9 |
| R9 | Honest scorecard: every predicted GW150914 quantity listed with predicted value, observed value, and error bar | §3.10 |
| R10 | Forward dependency link to Ch 5 (black holes as zone infrastructure) clearly flagged: the ringdown of §3.7 assumes a Kerr exterior, which Ch 5 will justify at the Firmament membrane level | §3.10 |

---

## Prerequisites (reader must already know)

- **Ch 1 of this volume:** Full nonlinear Einstein field equations $G_{\mu\nu} = 8\pi G_4 T_{\mu\nu}/c^4$ (5.1.22); the 4D coupling $G_4 = G_6/V_\text{extra}$ (5.1.17); Schwarzschild and Kerr metrics (5.1.34), (5.1.41).
- **Ch 2 of this volume:** The Hulse–Taylor binary pulsar, referenced only as an inspiral-decay data point consistent with the quadrupole formula; its full treatment was in §2.8.2.
- **Vol 2 Ch 8 (Gravitational Field Theory):** Linearized metric $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$, $|h| \ll 1$; harmonic/Lorenz gauge $\partial^\mu \bar h_{\mu\nu} = 0$; the weak-field wave equation $\square h_{\mu\nu} = -16\pi G_4 T_{\mu\nu}/c^4$. This chapter does **not** re-derive these; it takes them as inherited and extends beyond them.
- **Vol 3 Ch 5–6:** Kepler orbit, quadrupole moment of a two-body system, reduced mass, angular-frequency relation $\omega^2 = G_4(m_1+m_2)/a^3$.
- **Vol 4 Ch 2:** Retarded Green's function for the scalar wave equation — the same construction we use for the tensor equation (with appropriate index structure) in §3.5.
- **Vol 2 Ch 3:** Transverse-traceless gauge concept (introduced there for electromagnetic plane waves; extended here to the tensor case).

## Forward dependencies (what this chapter establishes, used later)

- **Ch 5 (Black Holes as Zone Infrastructure):** Reuses the (2,2,0) QNM of §3.7 as a prediction for M87* and Sgr A* ringdown spectra; takes the Kerr exterior as given and asks what the interior looks like.
- **Ch 6 (Information Paradox):** The energy-balance accounting of §3.4 (how much mass-energy is radiated) connects to the information content of the radiated GWs.
- **Ch 12 (Starlight and Chronology):** The LIGO/Virgo H₀ measurement from the sirens catalog is referenced as an independent cross-check on the cosmological timeline.
- **Vol 6 (Predictions):** The scalar-breathing-mode bound of §3.9 is one of Volume 6's headline falsifiers.

---

## "Why" chain (the but-why audit)

| Section | "But why?" question answered |
|---|---|
| 3.0 | Why a whole new chapter on GWs after Vol 2 Ch 8 already did the linearized case? Because Vol 2 Ch 8 did not touch the *nonlinear* regime that governs late inspiral and merger, and it did not touch generation at all — it only showed that $\square h = 0$ has plane-wave solutions. |
| 3.1 | Why does the linearization procedure that Vol 2 Ch 8 did on the weak-field Einstein equations carry over unchanged to the full nonlinear (5.1.22)? (Answer: because linearization is a statement about the background, not about the full equations — and any solution of the full equations that is nearly flat is a solution of the linearized ones to the same accuracy.) |
| 3.2 | Why does fixing the Lorenz gauge leave residual gauge freedom, and why does imposing the TT gauge exhaust it? (Answer: harmonic coordinates are a first-order PDE on 4 functions; there are 10 metric components; $10 - 4 - 4 = 2$ physical degrees of freedom, which is exactly the number of plus-and-cross polarizations.) |
| 3.3 | Why does textbook GR have exactly two polarizations? Why might the zone framework have more? (Answer: textbook GR: because the massless graviton of a 4D diffeomorphism-invariant spin-2 theory has two helicities. Zone framework: because the Kaluza–Klein reduction may leave a light radion — a scalar mode of the internal-space volume — that also propagates.) |
| 3.4 | Why does a gravitational wave carry energy at all, if the linearized vacuum equations $\square h = 0$ involve no source? (Answer: the energy is second-order in $h$; the Isaacson averaging procedure extracts it from the nonlinear terms in the Einstein equations that linearization drops.) |
| 3.5 | Why is the generation formula *quadrupolar* rather than dipolar as it is for electromagnetism? (Answer: because linear momentum conservation kills the dipole term, and the next term in the multipole expansion is the quadrupole.) |
| 3.6 | Why is the chirp mass — rather than the individual masses $m_1, m_2$ — the quantity LIGO measures cleanly from the inspiral? (Answer: the inspiral phase depends on $m_1$ and $m_2$ only through the combination $m_c = (m_1 m_2)^{3/5}/(m_1+m_2)^{1/5}$ to leading post-Newtonian order.) |
| 3.7 | Why does the post-Newtonian expansion break down at ISCO? (Answer: the expansion parameter $v/c$ reaches $\sim 0.4$–0.5 at ISCO; higher orders are no longer suppressed; physically, the horizons are about to merge and no two-body description can survive the topology change.) |
| 3.8 | Why is the GW150914 chirp-mass measurement quoted as $30.0 \pm 0.3 M_\odot$ but the individual masses as $m_1 = 36^{+5}_{-4}$, $m_2 = 29^{+4}_{-4}$? (Answer: because $m_c$ is set by a single phase-evolution derivative and individual masses require breaking the $m_1 \leftrightarrow m_2$ degeneracy that LIGO's detectors cannot fully resolve for an aligned-spin system.) |
| 3.9 | Why, if the zone framework predicts a scalar mode, hasn't LIGO seen it? (Answer: the scalar mode's predicted amplitude is $\lesssim 10\%$ of the tensor strain for GW150914-like events, and the O(1) detectors are not configured for scalar sensitivity; the Einstein Telescope will be.) |
| 3.10 | Why is this chapter a PASS on data if it has no *distinguishing* prediction for GW150914? (Answer: because the absence of a distinguishing prediction *is* the requirement — the whole framework has to reduce to standard GR where standard GR has been tested, and GW150914 is the strongest test. A discrepancy here would kill the framework.) |

---

## Key deliverables (Foundations = derivation plan)

### Derivation 1: Linearized wave equation (from full nonlinear)
- **Starting point:** (5.1.22), the full Einstein equations derived in Ch 1.
- **Steps:**
  1. Write $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h| \ll 1$ *in the radiation zone*; this is an exact statement about a particular solution class, not a postulate about all solutions.
  2. Compute $R_{\mu\nu}$ to first order in $h$.
  3. Impose Lorenz gauge $\partial^\mu \bar h_{\mu\nu} = 0$ where $\bar h_{\mu\nu} \equiv h_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu} h$.
  4. Obtain $\square \bar h_{\mu\nu} = -16\pi G_4 T_{\mu\nu}/c^4$.
  5. In vacuum, $\square \bar h_{\mu\nu} = 0$. Plane-wave ansatz: $\bar h_{\mu\nu} = A_{\mu\nu} e^{ik_\alpha x^\alpha}$, $k^\mu k_\mu = 0$.
- **Equation numbers:** (5.3.1)–(5.3.10)

### Derivation 2: Transverse-traceless gauge and the two polarizations
- **Starting point:** the plane-wave solutions of (5.3.10).
- **Steps:**
  1. Residual gauge freedom: $\xi^\mu$ satisfying $\square \xi^\mu = 0$ preserves Lorenz gauge.
  2. Use the 4 residual functions to set $A^\mu{}_\mu = 0$ (traceless), $A_{0\mu} = 0$ (no time components).
  3. Result: $A_{\mu\nu}$ has only spatial, transverse, traceless components — 2 independent.
  4. For a wave propagating in $\hat z$: only $A_{xx} = -A_{yy} \equiv h_+$ and $A_{xy} = A_{yx} \equiv h_\times$ survive.
  5. Physical picture: ring of test particles stretched/squeezed along the + or $\times$ axes.
- **Equation numbers:** (5.3.11)–(5.3.18)

### Derivation 3: Isaacson energy flux
- **Starting point:** Second-order expansion of the Einstein equations; nonlinear terms $(h \partial\partial h, \partial h \partial h)$ act as an effective stress-energy.
- **Steps:**
  1. Expand $G_{\mu\nu} = G^{(1)}_{\mu\nu}[h] + G^{(2)}_{\mu\nu}[h,h] + \ldots$
  2. Average over a region large compared to $\lambda_\text{GW}$ but small compared to the background curvature scale.
  3. Define $T^\text{GW}_{\mu\nu} = -\frac{c^4}{8\pi G_4}\langle G^{(2)}_{\mu\nu}\rangle$.
  4. Result: $T^\text{GW}_{tt} = \frac{c^2}{32\pi G_4}\langle \partial_t h^\text{TT}_{ij} \partial^t h_\text{TT}^{ij}\rangle$.
  5. For a plane wave of amplitude $h_0$ and angular frequency $\omega$: flux = $\frac{c^3 \omega^2 h_0^2}{32\pi G_4}$.
  6. **Numerical example:** GW150914 peak strain $h_0 \sim 10^{-21}$ at $f \sim 250$ Hz gives a flux at Earth of $\sim 10^{-3}$ W m⁻². Integrated over the wave packet and the full sphere, this corresponds to $\sim 3 M_\odot c^2$ radiated.
- **Equation numbers:** (5.3.19)–(5.3.28)

### Derivation 4: Quadrupole generation formula
- **Starting point:** Retarded Green's function solution to $\square \bar h_{\mu\nu} = -16\pi G_4 T_{\mu\nu}/c^4$.
- **Steps:**
  1. $\bar h_{\mu\nu}(t, \vec r) = \frac{4 G_4}{c^4}\int \frac{T_{\mu\nu}(t - |\vec r - \vec r'|/c, \vec r')}{|\vec r - \vec r'|}d^3 r'$.
  2. Far-field limit ($r \gg \text{source size}$, $r \gg \lambda_\text{GW}$).
  3. Multipole expansion. Dipole vanishes (linear momentum conservation). Quadrupole dominates.
  4. $h^\text{TT}_{ij}(t, \vec r) = \frac{2 G_4}{c^4 r}\ddot{I}^\text{TT}_{ij}(t - r/c)$, where $I_{ij}$ is the traceless mass quadrupole.
  5. Power radiated: $P = \frac{G_4}{5 c^5}\langle \dddot{I}_{ij}\dddot{I}^{ij}\rangle$.
  6. For a circular binary: $P = \frac{32}{5}\frac{G_4^4}{c^5}\frac{(m_1 m_2)^2 (m_1+m_2)}{a^5}$.
- **Equation numbers:** (5.3.29)–(5.3.42)

### Derivation 5: Binary inspiral waveform (stationary phase)
- **Starting point:** Orbital-decay equation from energy balance: $dE/dt = -P$ with $E = -G_4 m_1 m_2/(2a)$.
- **Steps:**
  1. Derive $da/dt = -\frac{64}{5}\frac{G_4^3}{c^5}\frac{m_1 m_2(m_1+m_2)}{a^3}$.
  2. Integrate to find time-to-merger $\tau = \frac{5 c^5}{256 G_4^3}\frac{a_0^4}{m_1 m_2(m_1+m_2)}$.
  3. Chirp mass $m_c = (m_1 m_2)^{3/5}/(m_1+m_2)^{1/5}$; the inspiral frequency evolution depends only on $m_c$ at leading order: $\dot f_\text{GW} = \frac{96}{5}\pi^{8/3}\left(\frac{G_4 m_c}{c^3}\right)^{5/3} f_\text{GW}^{11/3}$.
  4. Time-domain strain amplitude $h(t) \sim (G_4 m_c/c^2 R)(\pi f_\text{GW}/c)^{2/3}$.
- **Numerical example (GW150914):** $m_c = 30.0\,M_\odot$ predicts a 35 Hz → 150 Hz sweep in 0.2 s; LIGO observed a 35 Hz → 150 Hz sweep in 0.20 ± 0.02 s. Match.
- **Equation numbers:** (5.3.43)–(5.3.54)

### Derivation 6: Merger, ringdown, and QNMs
- **Starting point:** Regge–Wheeler / Zerilli perturbation theory on a Schwarzschild or Kerr background.
- **Steps:**
  1. Post-Newtonian expansion parameter: $v/c \sim 0.4$ at ISCO; expansion breaks down.
  2. Effective-one-body mapping: sketch the idea, cite the literature, state which parts apply unchanged to the zone framework.
  3. For the ringdown: expand the perturbation $h_{\mu\nu}$ on a Kerr background; separate into tensor spherical harmonics; obtain a Schrödinger-like radial equation; the quasi-normal modes are its complex-frequency eigenvalues.
  4. Fundamental mode for Schwarzschild: $f_{220}(M) = 0.1494 \cdot c^3/(G_4 M)$, damping $\tau_{220} = 0.074 \cdot G_4 M / c^3$.
- **Numerical example:** $M_f = 64.5 M_\odot \Rightarrow f_{220} = 250.8$ Hz, $\tau_{220} = 4.0$ ms.
- **Equation numbers:** (5.3.55)–(5.3.64)

### Derivation 7: Polarization classification and zone-architecture extras
- **Starting point:** Eardley–Lee–Lightman–Wagoner (1973) theorem: a general metric theory of gravity admits up to six polarizations (2 tensor + 2 vector + 2 scalar).
- **Steps:**
  1. State the theorem; enumerate the six modes pictorially.
  2. Textbook GR: diffeomorphism invariance kills the 4 non-TT modes. Two polarizations survive.
  3. Kaluza–Klein reduction of the 6D action: a scalar radion $\phi = \log(V_\text{extra})$ emerges. Its kinetic term is $\mathcal L_\phi = -\frac{1}{2}(\partial\phi)^2$, and the coupling to matter is $\propto \phi T^\mu{}_\mu / M_\text{Pl}$.
  4. The radion is effectively massless if the internal space volume is a flat direction of the effective potential; it is massive if the volume is stabilized. In the Goldberger–Wise stabilization scenario that our framework adopts, the radion mass is $m_\phi \sim (V_\text{extra})^{-1/2} \sim 10^{-31}$ eV — *below* LIGO's frequency floor of $\sim 10^{-13}$ eV by a huge margin. The radion is effectively massless for LIGO/Virgo frequencies.
  5. Zone-framework prediction: a **scalar breathing mode** with amplitude $h_\phi / h_\text{tensor} \sim (v/c)^2 \langle T^\mu{}_\mu\rangle/\langle T^{00}\rangle$, of order $(v/c)^2$ for compact-binary sources.
  6. For GW150914 at peak $v/c \sim 0.5$: $h_\phi/h_\text{tensor} \sim 0.25$ worst case; averaged over the inspiral, $\sim 0.05$–0.1. **Current LIGO/Virgo upper limit on scalar mode: ≲ 0.1 of tensor amplitude.** The prediction sits at or just below current bounds — the next-generation detector (Einstein Telescope, 2035) should resolve it.
- **Equation numbers:** (5.3.65)–(5.3.73)

### Derivation 8: Brane-tension correction to orbital decay
- **Starting point:** The $da/dt$ expression of Derivation 5.
- **Steps:**
  1. Include the leading correction from the 6D action: $da/dt = -\frac{64}{5}\frac{G_4^3}{c^5}\frac{m_1 m_2(m_1+m_2)}{a^3}\left[1 + c_\sigma(\sigma/M_\text{Pl}^4) + \mathcal O(v^4/c^4)\right]$.
  2. Constraint from GW150914 phase precision: $|c_\sigma(\sigma/M_\text{Pl}^4)| < 10^{-3}$.
  3. Predicted value in the zone framework: $c_\sigma(\sigma/M_\text{Pl}^4) \sim 10^{-4}$. Just below current bound, testable by O4/O5.
- **Equation numbers:** (5.3.74)–(5.3.78)

### Derivation 9: Honest GW150914 scorecard
- Table of predicted vs. observed for: chirp mass, final mass, radiated energy, peak strain, inspiral duration (35 → 150 Hz), (2,2,0) QNM frequency, (2,2,0) damping time, scalar mode amplitude.
- For each: derivation source (equation number), predicted value, observed value with error bar, fractional discrepancy, status (PASS / FRAMEWORK-EXACT / PREDICTION-PENDING).

---

## Figure plan

| ID | Title | Placement | What it shows | Why needed | Type | Complexity |
|---|---|---|---|---|---|---|
| Fig 5.3.1 | The three regimes of a binary merger | §3.0 | Horizontal timeline across a binary inspiral → merger → ringdown, with the relevant calculational framework for each: linearized GR (inspiral), numerical relativity (merger), perturbation theory on Kerr (ringdown). Arrows show where Vol 2 Ch 8 stops, where this chapter picks up, and where Ch 5 takes over. | Roadmap: readers need to see where in the merger the chapter lives. | Timeline + schematic | Medium |
| Fig 5.3.2 | Plus and cross polarizations on a ring of test particles | §3.3.2 | A circular ring of test particles, shown at five phases of a GW period, for (top) the + mode and (bottom) the × mode. Arrows show radial displacement. | Spatial: this is *the* picture of what a GW *is*. No prose replaces it. | Schematic | Medium |
| Fig 5.3.3 | The six possible polarizations of a general metric theory | §3.3.3 | A 2×3 grid: top row — 2 tensor modes (+, ×); middle row — 2 vector modes (x, y); bottom row — 2 scalar modes (breathing, longitudinal). Ring-of-test-particles picture for each. Standard GR has only the top row; zone architecture *may* have the bottom-left (breathing). | Conceptual + comparison: readers must see what a zone-architecture discovery would look like in the data. | Grid of schematics | Complex |
| Fig 5.3.4 | Quadrupole radiation pattern from an equal-mass binary | §3.5.3 | 3D angular distribution of GW luminosity $dP/d\Omega$ around a circular binary in the x–y plane. Lobes peaking along the orbital angular-momentum axis; nulls in the plane. | Spatial: the angular dependence is unfamiliar — readers expect a dipole and find a quadrupole. | 3D plot | Medium |
| Fig 5.3.5 | The GW150914 waveform: theory vs. data | §3.8.2 | Time-series strain from LIGO Hanford, with the post-Newtonian predicted waveform (using $m_c = 30\,M_\odot$) overlaid in dashed red. Time axis from −0.2 s to +0.05 s relative to merger. Three phase labels: inspiral, merger, ringdown. | Data confrontation: the most famous plot in gravitational-wave physics; the chapter earns its keep by reproducing it. | Strain plot | Medium |
| Fig 5.3.6 | Frequency evolution and chirp | §3.6.3 | Plot of $f_\text{GW}(t)$ derived from (5.3.49), with the observed GW150914 track from LIGO superimposed as a scatter of points. Inset: $\dot f$ vs $f$ on a log–log plot, showing the $f^{11/3}$ scaling. | Data + derivation: the $f^{11/3}$ slope is "the chirp" that makes the chirp-mass measurement possible. | Plot | Medium |
| Fig 5.3.7 | Quasi-normal-mode frequencies of the GW150914 remnant | §3.7.4 | Complex-frequency plane, with crosses at the predicted $(n,l,m)=(0,2,2), (1,2,2), (0,3,3), (0,4,4)$ locations for a 64.5 $M_\odot$, $\chi=0.7$ Kerr remnant. Circles with error bars at the LIGO/Virgo measured ringdown frequencies. Agreement region shaded. | Data: shows the "spectroscopy" that modern ringdown analyses perform. | Complex-plane scatter | Medium |
| Fig 5.3.8 | Scalar-breathing-mode sensitivity floor | §3.9.3 | LIGO/Virgo upper bound on a scalar GW component as a fraction of tensor amplitude vs. frequency, with the zone-framework prediction shown as a shaded band from $h_\phi/h_\text{tensor} \sim 0.05$ (average) to 0.25 (peak-velocity). Einstein Telescope projected sensitivity shown as a dashed line. | Falsifier: this is the unique zone-architecture prediction, and the plot defines the testable window. | Sensitivity curve | Medium |
| Fig 5.3.9 | GW150914 scorecard | §3.10.1 | Color-coded table (green = PASS, blue = FRAMEWORK-EXACT, gray = PREDICTION-PENDING) of 8 predicted quantities with predicted value, observed value ± error, fractional agreement. | Accountability: the chapter's honest bottom line. | Color table | Simple |

**Figure density:** 9 figures across 11 sections — at the top of the Foundations target, justified because this is a confrontation-with-data chapter and much of the reasoning is spatial and spectral (ring patterns, polarization modes, QNM complex plane).

---

## Problem sets (Foundations requirement)

### Computational
- **P3.1** Starting from (5.3.42), compute the total energy radiated by a circular binary of $m_1 = 36\,M_\odot$ and $m_2 = 29\,M_\odot$ as it decays from an initial separation $a_0 = 10^7$ km to $a_\text{ISCO} = 6 G_4 M/c^2$. Compare to the GW150914 value of $3.0 \pm 0.5 M_\odot c^2$.
- **P3.2** For a Schwarzschild black hole of mass $M$, use the fundamental QNM frequency $f_{220}(M) = 0.1494\, c^3/(G_4 M)$ to compute the expected ringdown frequency of the M87* supermassive black hole ($M = 6.5\times 10^9 M_\odot$). In what frequency band (LIGO, LISA, PTA) would this signal lie?
- **P3.3** Derive the strain amplitude $h_0$ at Earth from a circular binary at luminosity distance 410 Mpc with chirp mass $m_c = 30 M_\odot$ at $f_\text{GW} = 150$ Hz. Compare your answer to the LIGO peak strain of $\sim 10^{-21}$.
- **P3.4** Using (5.3.49), compute the time-to-coalescence for a binary with the GW150914 parameters, starting from $f_\text{GW} = 35$ Hz. Compare to the LIGO-observed inspiral duration (≈ 0.20 s).

### Conceptual
- **P3.5** Explain *why* the gravitational-radiation formula is *quadrupolar*, not dipolar. (Hint: what conservation law forces the dipole term to vanish?)
- **P3.6** In a theory with a scalar gravitational mode in addition to the two tensor modes, what would a ring-of-test-particles diagram look like? Sketch the new pattern and contrast it with the + and × patterns.
- **P3.7** Why does the post-Newtonian expansion of Derivation 5 break down at ISCO? Estimate the expansion parameter $v/c$ at $r = 6 G_4 M/c^2$ for a test particle in circular orbit, and explain what happens to the expansion when $v/c \gtrsim 0.4$.

### Challenge
- **P3.8** Reproduce the key result $\dot f \propto f^{11/3}$ of (5.3.49) starting from energy balance and the quadrupole formula, without looking up the coefficient.
- **P3.9** Show that the residual gauge freedom after imposing the Lorenz condition $\partial^\mu \bar h_{\mu\nu} = 0$ is parametrized by solutions of $\square \xi^\mu = 0$, and that this is exactly enough freedom to reach the TT gauge for a plane wave.
- **P3.10** The zone-framework scalar breathing mode has predicted amplitude $h_\phi/h_\text{tensor} \sim 0.05$ averaged over a GW150914-like inspiral. Given the LIGO O3 strain sensitivity of $\sim 10^{-23}/\sqrt{\text{Hz}}$ at 150 Hz, estimate the minimum chirp mass for which such a scalar mode would be detectable at signal-to-noise ratio 5.

---

## Verification criteria

- [ ] Every derivation cites Ch 1 (this volume) or Vol 2 Ch 8 for its starting point.
- [ ] All nonlinear steps — Isaacson averaging, post-Newtonian expansion, effective-one-body, QNM analysis — are explicitly distinguished from the linearized results inherited from Vol 2 Ch 8.
- [ ] Equation numbers (5.3.1)–(5.3.78) (approximate).
- [ ] §3.9 states zone-architecture predictions that *differ* from textbook GR, with numerical bounds and falsification thresholds.
- [ ] §3.10 reports the full GW150914 scorecard honestly.
- [ ] Word count 10,000–14,000.
- [ ] 9 figures specified; every `[FIGURE: ...]` placeholder in the draft has a matching entry here.
- [ ] Self-review report produced.
- [ ] Physicist reviewer (simulated): pass on the distinction between linearized and nonlinear regimes.
- [ ] Skeptic reviewer (simulated): pass — the scalar-mode prediction is a genuine falsifier, not a retrofitted explanation.
- [ ] Navigator reviewer (simulated): pass — the chapter's central results (quadrupole formula, chirp mass, QNM frequency) are stated in boxed equations and not buried.

---

## Research gaps

- **Radion mass prediction:** The Goldberger–Wise stabilization mechanism is adopted without a full first-principles derivation of $m_\phi$ from zone parameters. The value $m_\phi \sim 10^{-31}$ eV is an order-of-magnitude estimate; §3.9 states this explicitly. A full derivation is flagged as an open problem for Vol 6 or future work.
- **Numerical relativity:** The merger phase ($f_\text{GW} \sim 200$–300 Hz for GW150914) requires full numerical integration of (5.1.22). This chapter sketches the effective-one-body formalism and cites the published waveform catalogs, but does not carry out an independent numerical simulation. The Reviewer's Ledger of §3.10 flags this as an inherited assumption from the NR community.
- **Brane-tension coefficient:** The coefficient $c_\sigma$ in the orbital-decay correction (5.3.74) is computed at tree level in a particular truncation of the 6D effective action; higher-order terms are not accounted for. The $10^{-4}$ estimate carries a factor-of-few theoretical uncertainty.

---

*End of CHAPTER_SPEC.md*
