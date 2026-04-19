# Chapter Outline — Vol 5 Ch 3
## Gravitational Waves

**Target length:** 30–40 pages (~10,000–14,000 words), 11 sections, 9 figures.

---

## §3.0 Why Another Chapter on Gravitational Waves
- **Topic sentence:** Vol 2 Ch 8 derived the linearized wave equation; it did not touch nonlinear generation, it did not propagate a binary to merger, and it did not confront LIGO data. This chapter does all three.
- **Why entry:** The reader who finished Vol 2 Ch 8 is entitled to ask, "Aren't we done with gravitational waves?" — and the answer is, "We're done with the easy quarter."
- **Key content:** Roadmap of the three regimes (inspiral / merger / ringdown), where each is calculated, and the chapter's organizational map.
- **Exit:** Reader knows what this chapter covers and what it does *not* (strong-field interiors → Ch 5; information → Ch 6).
- **Figure:** Fig 5.3.1 (three regimes of a binary merger).
- **Length:** ~800 words.

## §3.1 From Full Nonlinear (5.1.22) to the Linearized Wave Equation
- **Topic sentence:** Linearization is a statement about a particular class of nearly-flat solutions of the full Einstein equations, not an approximation to the equations themselves.
- **Why entry:** "Didn't Vol 2 Ch 8 already do this?" — Yes, but there it started from a weak-field *postulate*. Here we start from the full (5.1.22) and show the linearized theory is a *consistent truncation* of the nonlinear one.
- **Key content:** Recap of Lorenz gauge, the operator $\square$, the retarded-Green's-function solution. Cite Vol 2 Ch 8 for the detailed derivation; here, re-establish notation and emphasize the nonlinear provenance.
- **Exit:** Reader has (5.3.10): $\square \bar h_{\mu\nu} = -(16\pi G_4/c^4) T_{\mu\nu}$, traced explicitly back to (5.1.22).
- **Length:** ~900 words.

## §3.2 Plane Waves in Vacuum and Gauge Fixing
- **Topic sentence:** Vacuum plane-wave solutions of (5.3.10) have 10 components; gauge freedom kills all but 2.
- **Why entry:** "Why exactly two polarizations?" — we're going to count.
- **Key content:** Plane-wave ansatz, null wavevector, Lorenz condition (4 constraints), residual gauge freedom (4 more), final tally 10 − 4 − 4 = 2.
- **Exit:** Reader understands the TT gauge and has (5.3.18) in hand.
- **Figure:** Fig 5.3.2 (+ and × polarizations on a ring).
- **Length:** ~1,100 words.

## §3.3 Polarization Content: Standard GR and Beyond
- **Topic sentence:** The Eardley–Lee–Lightman–Wagoner classification lets us enumerate all six modes a general metric theory could have; textbook GR has two, and the zone framework *may* have three.
- **Why entry:** "Could there be more?" — yes, and we'd better know which ones.
- **Key content:** The 6-mode enumeration (2 tensor, 2 vector, 2 scalar); ring-of-test-particles pictures; why 4D diffeomorphism invariance kills 4 of them in standard GR; how the Kaluza–Klein radion resurrects the scalar breathing mode in the zone framework; mass of the radion and its effect on propagation.
- **Exit:** Reader knows the scalar-breathing-mode prediction exists and where §3.9 will quantify it.
- **Figure:** Fig 5.3.3 (six polarizations grid).
- **Length:** ~1,300 words.

## §3.4 Energy Carried by a Gravitational Wave
- **Topic sentence:** GW energy is a second-order quantity; the Isaacson averaging procedure extracts it from the nonlinear terms in the Einstein equations that linearization drops.
- **Why entry:** "If $\square h = 0$ has no source, where does the energy come from?"
- **Key content:** Second-order expansion of $G_{\mu\nu}$; short-wavelength average; definition of $T^\text{GW}_{\mu\nu}$; flux formula $F = \frac{c^3}{32\pi G_4}\langle \dot h_{ij}^\text{TT}\dot h^\text{TT,ij}\rangle$; numerical estimate for GW150914 peak.
- **Exit:** Reader has (5.3.28): the flux formula and a feel for the energy scale.
- **Length:** ~1,000 words.

## §3.5 Generation: The Quadrupole Formula
- **Topic sentence:** Retarded Green's function + multipole expansion + vanishing dipole = quadrupole radiation.
- **Why entry:** "Why quadrupole?" — linear momentum conservation.
- **Key content:** Retarded solution of $\square \bar h = \text{source}$; far-field expansion; $\int T^{00} x^i d^3r$ is fixed by CoM, kills the monopole; $\int T^{00} x^i d^3 r$ time-dependence is proportional to total linear momentum, kills the dipole; $\int T^{00} x^i x^j d^3 r$ is the first non-trivial term; resulting power formula.
- **Exit:** Reader has (5.3.38): $P = (G_4/5 c^5)\langle \dddot I_{ij}\dddot I^{ij}\rangle$; and (5.3.42): the binary specialization.
- **Figure:** Fig 5.3.4 (quadrupole radiation pattern).
- **Length:** ~1,400 words.

## §3.6 The Binary Inspiral Waveform
- **Topic sentence:** The radiation drains orbital energy; the orbit shrinks; the frequency chirps; the chirp rate, at leading order, depends only on the chirp mass.
- **Why entry:** "What does LIGO actually see?" — a frequency that climbs with a specific slope.
- **Key content:** $dE/dt = -P$; orbital-decay ODE; time-to-merger; frequency evolution $\dot f \propto f^{11/3}$; chirp-mass definition and its degeneracy-breaking role; the stationary-phase-approximation waveform.
- **Exit:** Reader has (5.3.54), the frequency-evolution ODE, and can compute the GW150914 inspiral duration.
- **Figure:** Fig 5.3.6 (frequency evolution and chirp, with GW150914 data).
- **Length:** ~1,400 words.

## §3.7 Merger and Ringdown: Beyond the Post-Newtonian Regime
- **Topic sentence:** When $v/c$ approaches 0.5 at ISCO, the post-Newtonian expansion breaks down; numerical relativity takes over through the merger, and black-hole perturbation theory takes over for the ringdown.
- **Why entry:** "Why can't we just take more post-Newtonian orders?"
- **Key content:** Breakdown estimate; effective-one-body formalism (sketch, not derived); transition to full numerical relativity for merger; black-hole perturbation theory on Kerr background; Regge–Wheeler–Zerilli equation; quasi-normal mode eigenvalues; fundamental (2,2,0) mode frequency and damping time for a Kerr remnant.
- **Exit:** Reader has (5.3.64) for the Schwarzschild fundamental QNM frequency and understands that the full GW150914 waveform is a stitched composite of three different calculational frameworks.
- **Figure:** Fig 5.3.7 (QNM complex-frequency plane with GW150914 remnant points).
- **Length:** ~1,400 words.

## §3.8 Confrontation with GW150914
- **Topic sentence:** Take every number derived above, plug in the observed GW150914 parameters, and compare to LIGO's measurement.
- **Why entry:** "Did the derivation earn its keep on real data?"
- **Key content:** Chirp mass 30.0 $M_\odot$; inspiral duration 0.20 s; final mass 64.9 $M_\odot$; radiated energy 3.0 $M_\odot c^2$; peak strain $10^{-21}$; (2,2,0) ringdown frequency 250.8 Hz; damping 4.0 ms; waveform overlap > 99.6%. Every quantity traced to its derivation equation.
- **Exit:** Reader sees that our framework reproduces the LIGO-measured quantities to within measurement precision.
- **Figure:** Fig 5.3.5 (GW150914 strain with overlaid prediction).
- **Length:** ~1,200 words.

## §3.9 Zone-Architecture Predictions Beyond Standard GR
- **Topic sentence:** The zone framework departs from textbook GR in two places — a scalar breathing mode from the internal-space radion, and a brane-tension correction to orbital decay — both testable at or just below current sensitivity.
- **Why entry:** "Where does the framework make predictions that could *fail*?"
- **Key content:** Scalar mode derivation from KK reduction; predicted amplitude $h_\phi/h_\text{tensor} \sim (v/c)^2$; numerical prediction for GW150914-like events; current LIGO/Virgo upper limit; projection to Einstein Telescope. Brane-tension correction to $da/dt$; predicted coefficient ($10^{-4}$); current phase-precision bound ($10^{-3}$); near-future reach (O4/O5 at $10^{-4}$).
- **Exit:** Reader has two concrete falsifiers, each with a numerical prediction and a sensitivity floor.
- **Figure:** Fig 5.3.8 (scalar-mode sensitivity curve).
- **Length:** ~1,200 words.

## §3.10 The Scorecard
- **Topic sentence:** Every predicted GW150914 quantity, every zone-framework falsifier, every open problem — in one color-coded table.
- **Why entry:** "What's the honest bottom line?"
- **Key content:** The 8-entry scorecard; comments on each row; research-gap list (radion mass, NR assumption, brane-tension coefficient); what Vol 6 inherits.
- **Exit:** Reader has the single page that sums up the chapter.
- **Figure:** Fig 5.3.9 (GW150914 scorecard).
- **Length:** ~1,000 words.

---

## Outline Review Checklist
- [x] Every chapter requirement (R1–R10) maps to at least one section.
- [x] No section uses a concept not yet established (Vol 1–4 and Vol 5 Ch 1–2 all cited explicitly at the point of use).
- [x] "Why" chain is unbroken — every section opens with a "but-why" question.
- [x] Prerequisites satisfied by Vols 1–4 and Vol 5 Ch 1.
- [x] Figure plan complete: 9 figures, each tied to a specific section and paragraph.
- [x] Equation-number budget: (5.3.1)–(5.3.78) ≈ 78 equations, distributed roughly 10 per section.
- [x] Word budget: 800 + 900 + 1100 + 1300 + 1000 + 1400 + 1400 + 1400 + 1200 + 1200 + 1000 ≈ 12,700 words. In range.

---

*End of CHAPTER_OUTLINE.md*
