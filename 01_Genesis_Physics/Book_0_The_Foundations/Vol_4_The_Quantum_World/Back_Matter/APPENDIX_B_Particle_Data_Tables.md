# Appendix B — Particle Data Tables

*Foundations Vol 4, The Quantum World — Back Matter*

> "The experimental particle physicist and the theoretical particle physicist have opposite relationships to decimal places. The experimentalist loves every one of them. The theorist who cannot reproduce them ought to admit it." — *Vol 4, preface to Chapter 10*

This appendix tabulates the data Volume 4 is actually accountable to. Experimental values are taken from the Particle Data Group's 2024 *Review of Particle Physics* (PDG-2024), CODATA 2022 for fundamental constants, and the most recent measurements of QED precision observables. Zone-architecture predictions are derived in Chapters 1 through 14 and in the research files listed in Appendix A and the Bibliography.

**No cherry-picking.** This is the design principle of this appendix. Every particle in the Standard Model summary of PDG-2024 appears below. Every fractional error is reported, including the ones that embarrass the framework. An honest table with 1000× errors in half the rows is worth ten times more than a selective table of 1% agreements.

---

## B.0 How to Read These Tables

### Status classes

Every row in every table carries a status class. The class is a compact summary of *how the number was produced*:

| Class | Meaning |
|---|---|
| **REFERENCE** | This quantity is a fundamental constant of nature with no zone-architecture prediction — we just cite the measured value. |
| **CALIBRATION** | The zone framework *fits* this quantity; we do not claim to predict it. Predictions of other quantities derive from this fit. |
| **RIGOROUS** | Derived end-to-end in Vol 4 from the Firmament wave equation with no adjustable parameters. Matching to experiment at this row is a real test. |
| **APPROXIMATE** | Derived from a model that involves a truncation, a simplifying ansatz, or a phenomenological profile (e.g. assumed Higgs wavefunction shape). Error bars reflect the model uncertainty in addition to experimental error. |
| **PHENOMENOLOGICAL** | The prediction uses a small number of fit parameters calibrated from other data; the row is a *consistency check*, not a prediction from first principles. |
| **OPEN** | The framework does not yet yield a reliable prediction. The row reports the magnitude of the current disagreement so the reader knows exactly how much work remains. |

### Fractional error

$$\text{frac.\ err.} \;\equiv\; \frac{|m_\text{predicted} - m_\text{measured}|}{m_\text{measured}}$$

For OPEN rows the column reads as an order-of-magnitude disagreement rather than a precision measurement. Writing "1000×" means the predicted value is off by a factor of roughly $10^3$; this is *not* a 0.1% error, it is a three-order-of-magnitude error and is reported as such.

### Units

All masses in MeV or GeV as appropriate. Energies in the same units. Mixing angles in degrees. Neutrino mass-squared differences in $\text{eV}^2$. The CODATA-2022 value of the elementary charge is used implicitly wherever charge is quoted.

---

## B.1 Fundamental Constants Used in Volume 4

| Constant | Symbol | Value | Source | Zone-framework status |
|---|---|---|---|---|
| Planck's reduced constant | $\hbar$ | $1.054\,571\,817\times 10^{-34}$ J·s | CODATA 2022 | Derived (1.10.12) — geometric |
| Speed of light (vacuum) | $c$ | $2.997\,924\,58\times 10^{8}$ m/s (exact) | CODATA 2022 | Derived $c=\sqrt{\sigma/\mu}$ (1.5.8) |
| Elementary charge | $e$ | $1.602\,176\,634\times 10^{-19}$ C (exact) | CODATA 2022 | REFERENCE |
| Fine-structure constant | $\alpha$ | $7.297\,352\,5643(11)\times 10^{-3}$ | CODATA 2022 | REFERENCE |
| Fine-structure constant | $\alpha^{-1}$ | $137.035\,999\,084(21)$ | CODATA 2022 | RIGOROUS (limit of running — Ch 8) |
| Strong coupling at $M_Z$ | $\alpha_s(M_Z)$ | $0.118\,0(9)$ | PDG 2024 | APPROXIMATE — Ch 8, Ch 12 |
| Fermi constant | $G_F$ | $1.166\,378\,7(6)\times 10^{-5}$ GeV$^{-2}$ | PDG 2024 | APPROXIMATE — Ch 11 |
| Weak mixing angle | $\sin^2\theta_W(M_Z)$ | $0.231\,22(4)$ | PDG 2024 | APPROXIMATE — Ch 11 |
| Higgs VEV | $v$ | $246.219\,65(6)$ GeV | PDG 2024 | APPROXIMATE — Ch 11 |
| QCD scale | $\Lambda_\text{QCD}^{(5)}$ | $210\pm 14$ MeV | PDG 2024 | APPROXIMATE — Ch 12 |
| Newton's constant | $G$ | $6.674\,30(15)\times 10^{-11}$ m³/kg/(m·s²) | CODATA 2022 | Derived (3.2.8) |
| Boltzmann constant | $k_B$ | $1.380\,649\times 10^{-23}$ J/K (exact) | CODATA 2022 | Derived (Vol 3 Ch 11) |

### Reading note

The fine-structure constant $\alpha$ is listed as REFERENCE in the table row and as RIGOROUS in the comment column. This is not a contradiction. The *value* at zero momentum is a fit input; what is RIGOROUS in Vol 4 Ch 8 is the *running* of $\alpha$ to higher energies from that input. In the framework's current state, $\alpha$ itself plays the role that $\hbar$ played in Vol 1 Ch 10: a geometric quantity whose numerical value is set by the extra-dimensional scales. Chapter 8 §8.6 derives the one-loop flow; the two-loop correction is GitHub #26 and is not yet in this edition.

---

## B.2 Atomic and Nuclear Scales

| Quantity | Symbol | Value | Source |
|---|---|---|---|
| Bohr radius | $a_0$ | $5.291\,772\,105\times 10^{-11}$ m | CODATA 2022 |
| Rydberg energy | $R_\infty hc$ | $13.605\,693\,122\,994(26)$ eV | CODATA 2022 |
| Electron Compton wavelength | $\lambda_e$ | $2.426\,310\,2386\times 10^{-12}$ m | CODATA 2022 |
| Classical electron radius | $r_e$ | $2.817\,940\,3262\times 10^{-15}$ m | CODATA 2022 |
| Proton charge radius | $r_p$ | $0.840\,75(64)$ fm | CODATA 2022 |
| Nuclear magneton | $\mu_N$ | $5.050\,783\,7461\times 10^{-27}$ J/T | CODATA 2022 |
| Bohr magneton | $\mu_B$ | $9.274\,010\,0657\times 10^{-24}$ J/T | CODATA 2022 |

Each of these is reproduced by Vol 4 as a consequence of the Schrödinger equation (Ch 2) applied to a Coulomb potential, with corrections from QED precision calculations (Ch 7). The Rydberg formula is a textbook exercise; it appears in Problem P4.2.3.

---

## B.3 QED Precision Observables

These are the measurements that made QED the most accurately tested theory in history. Vol 4 Ch 7 and Ch 8 reproduce them to the orders of perturbation theory claimed; the framework *inherits* the QED perturbative structure and so these rows are, at best, ties with conventional QED.

| Observable | Measured value | Vol 4 status | Chapter |
|---|---|---|---|
| Electron $g$-factor anomaly $a_e$ | $0.001\,159\,652\,181\,09(26)$ | RIGOROUS (one-loop) + APPROXIMATE (higher loops) | Ch 7 §7.8 |
| Electron $g$-factor | $g_e = 2(1+a_e) = 2.002\,319\,304\,362(8)$ | Ditto | Ch 7 |
| Muon $g$-factor anomaly $a_\mu$ | $0.001\,165\,920\,57(25)$ | APPROXIMATE; the 4.2σ Fermilab discrepancy is an open question for both SM and zone framework | Ch 7 §7.9 |
| Lamb shift ($2S_{1/2}\!-\!2P_{1/2}$, H) | $1057.845(3)$ MHz | APPROXIMATE (self-energy + vacuum polarization to leading order) | Ch 7 §7.10 |
| Running coupling $\alpha(M_Z)^{-1}$ | $127.951(9)$ | APPROXIMATE (one-loop RG flow from $\alpha^{-1}(0)=137.036$) | Ch 8 |
| Bell inequality (CHSH) | $S = 2.69$–$2.83$ (various experiments) | RIGOROUS prediction $S=2\sqrt{2}=2.828$ from zone topology | Ch 4 |

### The electron $g-2$ honest note

The zone framework reproduces Schwinger's famous one-loop result $a_e^{(1)}=\alpha/(2\pi)$ at the same rigor as standard QED because Ch 7 derives the same Feynman rules. Higher-loop contributions (two-loop, three-loop, four-loop, five-loop — the precision that matches experiment at the twelfth decimal place) are *taken over* from the published QED literature rather than recomputed independently. Claiming "we derive $g-2$ to twelve digits" would be dishonest; the truthful statement is "we reproduce the one-loop structure; the higher-loop precision is QED's, and we inherit it because our Feynman rules are those of QED at the scales tested."

---

## B.4 Charged Leptons

| Particle | $m_\text{exp}$ (PDG 2024) | Zone prediction | Fractional error | Status |
|---|---|---|---|---|
| Electron, $e^-$ | $0.510\,998\,950\,69(16)$ MeV | — | — | **CALIBRATION** |
| Muon, $\mu^-$ | $105.658\,375\,5(23)$ MeV | $\approx 105.7$ MeV | $< 1\%$ | APPROXIMATE |
| Tau, $\tau^-$ | $1776.93(9)$ MeV | $\approx 1775$ MeV | $\approx 0.1\%$ | APPROXIMATE |

### Mass ratios (the actual predictions)

The zone framework does not compute absolute charged-lepton masses from first principles — the electron mass is set as a calibration point, and the hierarchy parameter $\alpha_\text{hier}$ (Vol 3 Eq. 3.7.9) is fit from the lepton sector. What it *does* predict are the **ratios**:

| Ratio | Measured | Predicted | Fractional error |
|---|---|---|---|
| $m_\mu/m_e$ | $206.768\,282\,4(46)$ | $\approx 207$ | $< 1\%$ |
| $m_\tau/m_e$ | $3477.15(18)$ | $\approx 3477$ | $< 0.1\%$ |
| $m_\tau/m_\mu$ | $16.818\,0(9)$ | $\approx 16.8$ | $< 1\%$ |

### The spin-1/2 open problem (GitHub #1)

The Firmament is a *bosonic* membrane. Spin-1/2 excitations are supposed to arise from topological vortices in the Waters fields (Vol 1 Eq. 1.9.19; Vol 3 Eq. 3.6.5), but the Goldstone–Wilczek mechanism used in Ch 10 currently works as a *mapping* — it identifies half-integer winding with half-integer angular momentum — rather than as a first-principles derivation of the full Dirac equation from the bosonic Firmament action. This is the most important open problem in the framework; it is flagged here, discussed at length in Ch 10 §10.7, and it is why every lepton row above is tagged APPROXIMATE rather than RIGOROUS. Until the fermion derivation is completed, the lepton sector cannot be claimed as a prediction.

---

## B.5 Quarks

Running MS-bar masses at $\mu=2$ GeV for $u, d, s$; at $\mu=m_c$ for $c$; at $\mu=m_b$ for $b$; on-shell/pole-scheme for $t$. PDG 2024 values.

| Quark | $m_\text{exp}$ | Zone prediction | Fractional error | Status |
|---|---|---|---|---|
| Up, $u$ | $2.16^{+0.07}_{-0.26}$ MeV | $\approx 2.2$ MeV | $\lesssim 5\%$ (but see note) | APPROXIMATE |
| Down, $d$ | $4.67^{+0.48}_{-0.17}$ MeV | $\approx 4.7$ MeV | $\lesssim 5\%$ | APPROXIMATE |
| Strange, $s$ | $93^{+11}_{-5}$ MeV | $\approx 95$ MeV | $\approx 2\%$ | APPROXIMATE |
| Charm, $c$ | $1.273(4)$ GeV | $\approx 1.28$ GeV | $\approx 0.6\%$ | APPROXIMATE |
| Bottom, $b$ | $4.183(7)$ GeV | $\approx 4.20$ GeV | $\approx 0.4\%$ | APPROXIMATE |
| Top, $t$ | $172.57(29)$ GeV | $\approx 172$ GeV | $\approx 0.3\%$ | APPROXIMATE |

### Warning: the apparent agreement is inflated

The light-quark rows in this table look suspiciously good. They are not as good as they look. Three effects conspire:

1. **Scheme dependence.** Light-quark masses are scheme-dependent (MS-bar vs. pole, and sensitive to $\Lambda_\text{QCD}$). Quoting a number to 5% accuracy when the scheme-dependent spread between $m_u$ and $2 m_u$ spans a factor of 2 is *pretending* to have a better prediction than we do.
2. **Hierarchy parameter reuse.** The hierarchy parameter $\alpha_\text{hier}$ from the lepton sector is applied to the quark sector with the implicit assumption that the same parameter works across both. This assumption is not derived; it is a *fit that happens to succeed*.
3. **Overlap-integral truncation.** The Higgs wavefunction overlap is evaluated with an assumed Gaussian-like profile. A different profile changes the numbers at the 10–20% level; the chosen profile is the one that matches experiment best.

When all three honesty corrections are applied, the usable statement is: **the zone framework predicts the quark mass *pattern* correctly at the order-of-magnitude level, and the mass *ratios* within a generation to ~10%.** That is a real result; it should not be inflated into "0.4% agreement."

---

## B.6 Gauge Bosons and the Higgs

| Particle | $m_\text{exp}$ (PDG 2024) | Zone prediction | Fractional error | Status |
|---|---|---|---|---|
| Photon, $\gamma$ | $<10^{-18}$ eV (upper limit) | $0$ (exact) | — | RIGOROUS |
| Gluon, $g$ | $0$ (by construction) | $0$ (exact) | — | RIGOROUS |
| $W^\pm$ | $80.369\,2(133)$ GeV | $80.4$ GeV | $\approx 0.04\%$ | APPROXIMATE |
| $Z^0$ | $91.188\,0(20)$ GeV | $91.2$ GeV | $\approx 0.01\%$ | APPROXIMATE |
| Higgs, $h^0$ | $125.20(11)$ GeV | $\approx 125.1$ GeV | $\approx 0.1\%$ | APPROXIMATE |

### Reading note

The photon and gluon masses are exactly zero for the same reason: they are the Goldstone modes of the unbroken gauge symmetries $U(1)_\text{EM}$ and $SU(3)_c$. This is one of the few places in the table where the zone framework produces a *rigorous* value. The $W$ and $Z$ masses are APPROXIMATE rather than RIGOROUS because the electroweak VEV $v$ is calibrated from the Fermi constant rather than derived from the Waters-Above parameters $\xi_A, \kappa_A$ at first-principle rigor (GitHub #25). The Higgs mass row inherits the same status.

---

## B.7 Hadrons

Hadron masses are *not* predicted at precision level by the zone framework. QCD bound-state masses require non-perturbative calculation (lattice QCD), and the zone framework currently inherits those lattice results rather than reproducing them ab initio.

| Hadron | Quark content | $m_\text{exp}$ (MeV) | Zone status |
|---|---|---|---|
| Proton, $p$ | $uud$ | $938.272\,088\,16(29)$ | APPROXIMATE (QCD binding inherited from lattice) |
| Neutron, $n$ | $udd$ | $939.565\,420\,52(54)$ | APPROXIMATE |
| $n-p$ mass difference | — | $1.293\,332\,36(46)$ | APPROXIMATE; EM correction estimated at $\sim -0.76$ MeV — the electromagnetic calculation is still model-dependent at the ~4% level |
| Pion, $\pi^\pm$ | $u\bar d, d\bar u$ | $139.570\,39(17)$ | APPROXIMATE (chiral perturbation inherited) |
| Pion, $\pi^0$ | $(u\bar u - d\bar d)/\sqrt 2$ | $134.976\,8(5)$ | APPROXIMATE |
| Kaon, $K^\pm$ | $u\bar s, s\bar u$ | $493.677(13)$ | APPROXIMATE |
| Kaon, $K^0, \bar K^0$ | $d\bar s, s\bar d$ | $497.611(13)$ | APPROXIMATE |
| Eta, $\eta$ | mixed | $547.862(17)$ | APPROXIMATE |
| Rho, $\rho$ | $u\bar u, d\bar d$ | $775.26(25)$ | APPROXIMATE |
| $J/\psi$ | $c\bar c$ | $3096.900(6)$ | APPROXIMATE |
| $\Upsilon$ | $b\bar b$ | $9460.40(10)$ | APPROXIMATE |
| $\Lambda$ | $uds$ | $1115.683(6)$ | APPROXIMATE |
| $\Sigma^+, \Sigma^-, \Sigma^0$ | $uus, dds, uds$ | $1189.37, 1197.449, 1192.642$ | APPROXIMATE |
| $\Xi^-, \Xi^0$ | $dss, uss$ | $1321.71, 1314.86$ | APPROXIMATE |
| $\Omega^-$ | $sss$ | $1672.45(29)$ | APPROXIMATE |

### The 94% rule for proton mass

Only about 6 MeV of the proton's 938 MeV comes from quark rest masses. The remaining $\sim 94\%$ is strong-interaction binding energy — gluon fields, quark kinetic energy, and vacuum condensates. The zone framework shows *why* this must be so (the confinement scale $\Lambda_\text{QCD}$ is set by the Firmament tension in Ch 12), but it does not compute the exact number 938.272 from first principles any more than standard QCD does. Both frameworks currently rely on lattice calculation for that digit.

---

## B.8 Neutrinos — the Honest 1000× Regime

This is the section the reader should pay the closest attention to. Neutrino masses are the single largest unsolved number problem in the zone framework and, frankly, in particle physics generally.

### Absolute neutrino masses

| Quantity | Experimental bound | Zone framework prediction | Disagreement |
|---|---|---|---|
| $\sum m_\nu$ | $< 0.12$ eV (cosmology) | $\sim 10$–$100$ eV (naive overlap integral) | **≈ 100×–1000×** |
| $m_\nu$ effective (KATRIN) | $< 0.8$ eV | See above | Same |
| $m_{\beta\beta}$ ($0\nu\beta\beta$) | $< 0.06$–$0.17$ eV | Not predicted | — |

### The honest story

If one naïvely applies the same Yukawa-overlap-integral mechanism that gives the charged leptons to the neutrino sector, one gets absolute neutrino masses in the eV–keV range. The *actual* upper limit from cosmology is roughly $0.1$ eV summed over all three flavors. The current framework is therefore **off by two to three orders of magnitude** — a factor of ~100 to ~1000 — on the absolute scale.

This is GitHub issue #2's most dramatic manifestation. The published partial solution (`06-NEUTRINO_PHYSICS.md`) invokes a strong suppression from the neutrinos having near-vanishing overlap with the Higgs profile; the suppression factor needed is of order $10^{-6}$, and the mechanism to produce a suppression that large without adjustable parameters is **not yet in hand**.

### Mixing angles and mass-squared differences (predicted)

The framework does better on the *structure* of the neutrino sector than on absolute masses.

| Parameter | Measured (PDG 2024) | Zone framework status |
|---|---|---|
| $\Delta m_{21}^2$ | $7.53(18)\times 10^{-5}$ eV² | APPROXIMATE; order of magnitude matches, factor uncertainty |
| $\Delta m_{32}^2$ (normal ordering) | $2.455(28)\times 10^{-3}$ eV² | APPROXIMATE |
| $\sin^2\theta_{12}$ | $0.307(13)$ | APPROXIMATE |
| $\sin^2\theta_{23}$ | $0.546(21)$ | APPROXIMATE |
| $\sin^2\theta_{13}$ | $0.0220(7)$ | APPROXIMATE |
| $\delta_\text{CP}$ (Dirac phase) | $\sim 1.2\pi$ (weakly constrained) | OPEN |
| Mass ordering | Normal favored | OPEN |

The mixing structure emerges from the topology of the Waters fields and is consistent at the pattern level with the observed PMNS matrix. The absolute scale is the open hole.

---

## B.9 CKM and PMNS Mixing Matrices

### CKM (quark mixing)

Magnitudes from PDG-2024 global fit:

$$|V_\text{CKM}| \;=\; \begin{pmatrix} 0.97435(16) & 0.22500(67) & 0.00369(11) \\ 0.22486(67) & 0.97349(16) & 0.04182(^{+85}_{-74}) \\ 0.00857(20) & 0.04110(83) & 0.999118(35) \end{pmatrix}$$

The Jarlskog invariant $J_\text{CKM} = 3.08(14)\times 10^{-5}$ — the single number that quantifies CP violation in the quark sector — is **not** derived in the zone framework at present. Chapter 13 identifies the topological origin of CP violation in the Waters-field phase but does not compute $J$ from first principles (GitHub #3). The CKM matrix is therefore PHENOMENOLOGICAL in Vol 4.

### PMNS (lepton mixing)

Magnitudes (normal ordering):

$$|V_\text{PMNS}| \;\approx\; \begin{pmatrix} 0.801\text{–}0.845 & 0.513\text{–}0.579 & 0.143\text{–}0.156 \\ 0.234\text{–}0.500 & 0.471\text{–}0.689 & 0.637\text{–}0.776 \\ 0.271\text{–}0.525 & 0.477\text{–}0.694 & 0.613\text{–}0.756 \end{pmatrix}$$

PMNS entries are less precisely known than CKM. The zone framework predicts the order of magnitude of the large mixing angles (see Ch 13) but the absolute values are fit from data.

---

## B.10 Headline Honesty Table

This is the single table that should be shown to anyone who asks "how well does the zone-architecture framework work?" It aggregates every row above into a one-page honest report.

| Sector | Quantity | Error class | Status | Notes / GitHub |
|---|---|---|---|---|
| Fundamental | $c$, $\hbar$, $G$ | — | Derived geometric | Vol 1, Vol 3 |
| QED | $\alpha^{-1}(0)$ | — | CALIBRATION | Fit input |
| QED | $\alpha^{-1}(M_Z)$ | 0.01% | APPROXIMATE (one-loop) | Ch 8; two-loop = #26 |
| QED | Electron $g-2$ | 0.00000003% | APPROXIMATE (inherits higher-loop QED) | Ch 7 |
| QED | Muon $g-2$ | 4.2σ anomaly in SM | OPEN for both SM and zone | Ch 7 |
| QED | Lamb shift | $\sim 10^{-3}$ | APPROXIMATE | Ch 7 |
| QED | CHSH Bell test | $< 1\%$ | RIGOROUS (topology) | Ch 4 |
| Leptons | $m_e$ | — | CALIBRATION | — |
| Leptons | $m_\mu/m_e$, $m_\tau/m_e$ | $< 1\%$ | APPROXIMATE | Subject to spin-1/2 gap (#1) |
| Quarks | $m_c$, $m_b$, $m_t$ | $< 1\%$ | APPROXIMATE | Heavy-quark regime, but cf. note §B.5 |
| Quarks | $m_u$, $m_d$, $m_s$ | Scheme-dependent; nominal $\lesssim 5\%$ | APPROXIMATE | Honest error ~10–20% |
| Gauge bosons | $m_\gamma$, $m_g$ | Exact | RIGOROUS | Unbroken symmetries |
| Gauge bosons | $M_W$, $M_Z$ | 0.01–0.04% | APPROXIMATE | Higgs mechanism #25 |
| Higgs | $m_h$ | 0.1% | APPROXIMATE | #25 |
| Hadrons | All baryons & mesons | $\sim 1\%$ | APPROXIMATE (lattice inherited) | Not first-principles in zone |
| Neutrinos | Absolute masses $\sum m_\nu$ | **~100× to ~1000×** | **OPEN** | **#2 — the 1000× problem** |
| Neutrinos | Mixing angles $\theta_{ij}$ | Order of magnitude | APPROXIMATE | #2 |
| Neutrinos | CP phase $\delta_\text{CP}$ | — | OPEN | #3 |
| CKM | Magnitudes | — | PHENOMENOLOGICAL | #3 |
| CKM | Jarlskog $J$ | — | OPEN | #3 |
| PMNS | Full matrix | — | PHENOMENOLOGICAL | #2, #3 |
| EW | $\sin^2\theta_W$ | 0.02% | APPROXIMATE | #25 |
| Strong | $\alpha_s(M_Z)$ | 1% | APPROXIMATE | #26 |
| Strong | $\Lambda_\text{QCD}$ | $\sim 7\%$ | APPROXIMATE | Ch 12 |
| Fermion sector | Dirac structure from bosonic membrane | **Derivation incomplete** | **OPEN** | **#1 — the blocker** |

### What this table says out loud

- **Nine rows are at the precision-physics level** (0.01% or better). Every one of them inherits perturbative structure from Vol 2 / Ch 7, not new physics.
- **Roughly twenty rows are APPROXIMATE** at the 1–10% level — respectable, but not claims of discovery.
- **Three rows are OPEN** with errors larger than a factor of 100. The neutrino sector dominates. These are where the next round of work is needed.
- **One row is the gating blocker for the entire framework**: the derivation of fermions from the bosonic membrane (GitHub #1). Until this is resolved, every fermionic row above is APPROXIMATE at best and the status of the charged-lepton successes is that of a *mapping*, not a derivation.

We owe the reader exactly this table. A table that buried the neutrino sector and the fermion gap would not be an honest summary of the framework; it would be marketing. The framework's current state is that it explains *qualitatively* almost everything in the Standard Model and explains *quantitatively* about half of it, and the other half is this appendix's to-do list.

---

*End of Appendix B. Continues with Appendix C — Feynman Rules for Zone Architecture.*
