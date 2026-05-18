---
product: Foundations Vol 4 — The Quantum World
chapter: 12
title: Quantum Chromodynamics
status: OUTLINE
created: 2026-04-09
---

# Chapter 12 — Detailed Outline

Target length: 9,000–14,000 words (30–40 pages). Equation block: (4.12.1)–(4.12.62+).

## §12.0 Introduction — the strong sector, honestly

- **Topic sentence:** Of the three Standard-Model chapters in Part III, the strong sector is the one where the framework has the firmest ground under its feet; this chapter earns that confidence carefully.
- **"Why" entry point:** Why is there a strong force at all? Because the η-direction has a topology that the photon direction does not.
- **Key content:** Announce two things at once: (a) QCD is in this framework a *topological* theory — the gauge group, the existence of confinement, the sign of the beta function, and the classification of hadrons are all forced by the $\mathbb{Z}_3$ orbifold already built in Vol 2 Ch 4 §4.2 and Vol 2 Ch 6; (b) there is exactly one $\mathcal{O}(1)$ matching — the overall normalization of $g_s$ at $M_Z$ — and it will be stated where it happens, not hidden. Include the roadmap figure. Set up the rigor-label vocabulary (RIGOROUS / APPROXIMATE / PHENOMENOLOGICAL / OPEN).
- **Exit condition:** The reader knows what will and won't be derived here, and which gaps are inherited from Ch 10.
- **Figures:** Fig 4.12.1 (roadmap).
- **Target length:** ~900 words.

## §12.1 $SU(3)_c$ from the three-fold η-orbifold [RIGOROUS]

- **Topic sentence:** The gauge group of the strong force is not a choice; it is the smallest Lie group whose center matches the orbifold topology of the η-circle.
- **"Why" entry point:** Why three colors, and why this particular algebra?
- **Key content:**
  1. Recap the η-geometry from Vol 2 Ch 4 §4.2: $\eta \in [0, \eta_B]$ with a hard confinement wall at $\eta = \eta_B$, and an orbifold identification $S^1_\eta/\mathbb{Z}_3$.
  2. Define winding number $n_c = \frac{1}{2\pi}\oint_\eta A\,d\eta \in \{0, 1, 2\}\pmod 3$. (4.12.1)–(4.12.2)
  3. Show the three inequivalent winding sectors form a triplet acted on by a discrete $S_3 \supset \mathbb{Z}_3$ symmetry.
  4. Lift the discrete action to a continuous compact Lie group. The unique connected compact Lie group with center $\mathbb{Z}_3$ and dimension matching the three-sector adjoint is $SU(3)$. (4.12.3)–(4.12.4)
  5. Introduce the Gell-Mann matrices $\lambda^a$ ($a = 1,\dots,8$) and the structure constants $f^{abc}$. Write $T^a = \lambda^a/2$. (4.12.5)
  6. State the fundamental ($\mathbf{3}$) and antifundamental ($\bar{\mathbf{3}}$) on which quarks and antiquarks live. (4.12.6)
- **Exit condition:** The reader has the gauge group, the generators, and the fact that the topology forced it.
- **Figures:** Fig 4.12.2 (orbifold and winding sectors).
- **Target length:** ~1,400 words.

## §12.2 Yang-Mills action from 6D KK reduction [RIGOROUS up to one $\mathcal{O}(1)$ match]

- **Topic sentence:** The 4D QCD action is what you get when you take the 6D gauge action already written down in Vol 2 Ch 5 and integrate out the $(\xi,\eta)$ directions against the zero mode of the gauge field.
- **"Why" entry point:** Why is the QCD Lagrangian built of $\text{Tr}(G_{\mu\nu}^2)$ and nothing else at leading order?
- **Key content:**
  1. Write the 6D gauge action $S_{\rm gauge}^{6D} = -\tfrac{1}{4}\int d^6x\sqrt{-g_6}\,{\rm Tr}(F_{AB}F^{AB})$. (4.12.7)
  2. Set up KK expansion: $A_M(x,\xi,\eta) = \sum_{nm} A_M^{(nm)}(x)\psi_n(\xi)\phi_m(\eta)$. (4.12.8)
  3. Pick the zero mode: $\psi_0, \phi_0$ = constants (massless mode). (4.12.9)
  4. Integrate over $\xi$ and $\eta$ against the warp factor $e^{2A+2B}$. (4.12.10)–(4.12.11)
  5. Identify $1/g_s^2 = \int d\xi\,d\eta\,e^{2A(\eta)+2B(\eta)}$ (with the warp $A = A_0 - \gamma\eta/2$). (4.12.12)
  6. Write the effective 4D action and the field-strength tensor: $G_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g_s f^{abc}A_\mu^b A_\nu^c$. (4.12.13)
  7. **Box the result:** $S_{\rm QCD} = -\tfrac{1}{4g_s^2}\int d^4x\sqrt{-g_4}\,{\rm Tr}(G_{\mu\nu}^a G^{\mu\nu a})$. (4.12.14)
  8. Give the covariant derivative on quarks: $D_\mu q = (\partial_\mu + ig_s T^a A_\mu^a)q$. (4.12.15)
  9. State the honest caveat: the overall normalization of the $\eta$-integral introduces an $\mathcal{O}(1)$ geometric constant; that constant is what gets matched to $\alpha_s(M_Z) = 0.1179$. Everything else that follows uses the matched value and predicts. This is labeled APPROXIMATE.
  10. Fill in the Gell-Mann matrix commutators (4.12.16)–(4.12.19) for the grad-student reader. (Navigator mandate.)
- **Exit condition:** The reader has the 4D action with numbered equations and understands what is matched vs derived.
- **Figures:** None — equation-dense.
- **Target length:** ~1,800 words.

## §12.3 Confinement as a topological obstruction [RIGOROUS]

- **Topic sentence:** Free quarks are not hard to see; they are topologically forbidden.
- **"Why" entry point:** Why can't a red quark fly off into space alone?
- **Key content:**
  1. Restate: a color charge corresponds to nonzero $n_c \pmod 3$. (4.12.20)
  2. Argue topologically: a configuration with nonzero total winding around the η-circle cannot be continuously extended to spatial infinity on the 4D Firmament, because any closed 2-surface enclosing the charge must have zero total winding (Stokes in the gauge-field language). (4.12.21)
  3. Consequence: the only allowed global states are color-singlets ($\sum_i n_c^{(i)} \equiv 0 \pmod 3$). This is the "confinement" statement as a topological theorem.
  4. **Box this key result** as a theorem. (4.12.22)
  5. Move from the topological statement to the energetic one: when you try to pull a red quark away from a green-blue core, the color flux is squeezed into a tube of cross-section $\sim \eta_B^2$ by the hard wall at $\eta = \eta_B$. The tube has constant cross-section, so its energy is linear in length. (4.12.23)
  6. Compute the string tension by dimensional analysis: $\sigma_{\rm QCD} \sim (\hbar c/\eta_B)^2 = (420\,{\rm MeV})^2 = 0.18\,{\rm GeV}^2/{\rm fm}$. Show the arithmetic. (4.12.24)–(4.12.25)
  7. **Box:** $V_{\rm conf}(r) = \sigma_{\rm QCD}\,r$. (4.12.26)
  8. Show the explicit chain that makes Vol 2 Ch 4's qualitative short-range claim quantitative: the short-range nuclear force between *color-singlet* nucleons comes from pion exchange, with range $r_0 = \hbar/(m_\pi c) = (197\,{\rm MeV\,fm})/(140\,{\rm MeV}) \approx 1.41$ fm. (4.12.27)–(4.12.29)
  9. Name and solve the apparent mismatch: the "short-range" of Vol 2 Ch 4 refers to the *residual* strong force between color-singlet hadrons; the *underlying* color force between colored objects is actually *infinite-range* but linearly confining. Flag this resolution explicitly — it is the Navigator reviewer's most natural confusion.
  10. **Chain-of-reasoning box:** explicit step-by-step trace from Vol 2 Ch 4 §4.4 short-range claim → (this chapter's) confinement → pion-exchange → 1.41 fm.
- **Exit condition:** The reader has the theorem, the linear potential, and the quantitative match with 1.4 fm.
- **Figures:** Fig 4.12.3 (flux tube, linear energy).
- **Target length:** ~1,800 words.

## §12.4 The heavy-quark potential and charmonium [APPROXIMATE — fermion masses inherit Ch 10]

- **Topic sentence:** Add one-gluon exchange at short distance and you have the Cornell potential, a Schrödinger problem whose ground states are the $J/\psi$ and $\Upsilon$.
- **"Why" entry point:** Why does QCD have a short-distance Coulomb-like phase at all if it is confining?
- **Key content:**
  1. At $r \ll \eta_B$, a single-gluon exchange is a tree-level diagram between two color charges in the fundamental representation. (4.12.30)
  2. The Casimir factor for the fundamental of $SU(3)$ is $C_F = (N^2 - 1)/(2N) = 4/3$. (4.12.31)
  3. The tree-level exchange gives $V_{\rm OGE}(r) = -\tfrac{4}{3}\alpha_s/r$. (4.12.32)
  4. Combine: the heavy-quark (Cornell) potential $V(r) = -\tfrac{4}{3}\alpha_s/r + \sigma_{\rm QCD}\,r$. **Box.** (4.12.33)
  5. Solve the radial Schrödinger equation (reduced mass $\mu = m_c/2$ for $c\bar c$) numerically with $\alpha_s \approx 0.3$ at the charmonium scale and $m_c = 1.27$ GeV (Ch 10 inheritance, with $\pm 0.02$ GeV error bar) to get the $1S$, $2S$, $3S$ levels. (4.12.34)–(4.12.36)
  6. Compare to PDG: $m_{J/\psi} = 3.0969$ GeV, $m_{\psi'} = 3.6861$ GeV. Framework: $\sim 3.10 \pm 0.04$ GeV, $\sim 3.68 \pm 0.05$ GeV. Label APPROXIMATE. (4.12.37)
  7. Repeat for $b\bar b$: $m_b = 4.18$ GeV, $m_\Upsilon$ prediction $\sim 9.48$ GeV vs PDG 9.4603 GeV. (4.12.38)
  8. Be explicit about what bits are inherited from Ch 10 (quark masses, with 15–99% error bars in general but much smaller for the heavy quarks) and what bits are new here (the potential itself, the Schrödinger solution).
- **Exit condition:** The reader has a concrete Schrödinger problem, the answer, and the honest error budget.
- **Figures:** Fig 4.12.4 (Cornell potential and charmonium levels).
- **Target length:** ~1,600 words.

## §12.5 Asymptotic freedom and the running coupling [RIGOROUS sign, APPROXIMATE normalization]

- **Topic sentence:** At higher energies, the effective $\eta$-integration region shrinks, and the coupling decreases; this is asymptotic freedom as a geometric fact.
- **"Why" entry point:** Why does the strong force become *weaker* at short distance, unlike electromagnetism?
- **Key content:**
  1. Recall the 4D coupling definition from §12.2: $1/g_s^2 = \int d\eta\,e^{2A+2B}$. (Back-reference.)
  2. Introduce a scale-dependent probe function $f(\eta,\mu)$ that localizes the integration to a neighborhood of size $\hbar/(\mu c)$ in $\eta$. (4.12.39)
  3. As $\mu$ increases, the localization tightens; the integral of the warp factor over the tight neighborhood gives a smaller $1/g_s^2$ — which translates to a *smaller* $g_s$ at high $\mu$ because of the sign flip in the identification... no, wait: because of the full derivation in (4.12.40), which I'll carry out explicitly. The sign of $d\alpha_s/d\ln\mu$ is negative. The derivation is a one-paragraph honest calculation. **Be careful here — the sign matters more than the coefficient.**
  4. Match the result to the standard beta function $\beta(g_s) = -\beta_0 g_s^3/(4\pi)^2$ with $\beta_0 = 11 - \tfrac{2}{3}n_f$. (4.12.41)–(4.12.42)
  5. Decompose: the $11 = \tfrac{11}{3}C_A$ with $C_A = 3$ comes from the gluon-loop contribution (gauge-boson self-interaction, a consequence of the non-abelian $f^{abc}$ term in the field strength). The $\tfrac{2}{3}n_f = \tfrac{4}{3}T_R\,n_f$ with $T_R = \tfrac{1}{2}$ comes from fermion loops. (4.12.43)–(4.12.44)
  6. **Key point:** the *sign* of the beta function is rigorous from the geometry (gluons dominate over fermions for $n_f < 16.5$), but the *normalization* of $\alpha_s$ at any fiducial scale is the $\mathcal{O}(1)$ match. Name this match: $\alpha_s(M_Z) = 0.1179 \pm 0.0010$ is taken from PDG, not computed. Label APPROXIMATE. (4.12.45)
  7. Integrate the RG equation: $1/\alpha_s(\mu) = 1/\alpha_s(M_Z) + (\beta_0/2\pi)\ln(\mu/M_Z)$. (4.12.46)
  8. Produce a table of $\alpha_s(\mu)$ at $\mu = 1$ GeV, 10 GeV, $M_Z$, 1 TeV, 10 TeV, comparing the framework (one-loop) with PDG. Honest note: the two-loop and higher corrections at $\mu = 1$ GeV are $\sim 5\%$.
  9. Define $\Lambda_{\rm QCD}$ as the scale where the one-loop $\alpha_s$ formally diverges: $\Lambda_{\rm QCD} = M_Z\exp(-2\pi/(\beta_0\alpha_s(M_Z))) \approx 200$ MeV. (4.12.47)
- **Exit condition:** The reader has the running coupling, the numerical values, and a clean sense of what is geometric and what is matched.
- **Figures:** Fig 4.12.5 (running $\alpha_s$).
- **Target length:** ~1,700 words.

## §12.6 The hadron spectrum: color singlets and Regge trajectories [RIGOROUS classification, APPROXIMATE masses]

- **Topic sentence:** Every observable strongly-interacting particle is a color singlet, and the spectrum of singlets is exactly what the $SU(3)$ tensor products say it should be.
- **"Why" entry point:** Why mesons and baryons, not dibaryons everywhere or chartreuse-quarks?
- **Key content:**
  1. Tensor products: $\mathbf{3}\otimes\bar{\mathbf{3}} = \mathbf{1}\oplus\mathbf{8}$. The $\mathbf{1}$ is the meson. (4.12.48)
  2. $\mathbf{3}\otimes\mathbf{3}\otimes\mathbf{3} = \mathbf{1}\oplus\mathbf{8}\oplus\mathbf{8}\oplus\mathbf{10}$. The $\mathbf{1}$, via $\epsilon^{abc}$, is the baryon. (4.12.49)
  3. Glueballs: pure-gluon bound states in the $\mathbf{1}$ of $\mathbf{8}\otimes\mathbf{8}$. (4.12.50)
  4. Exotic hadrons: tetraquarks ($\mathbf{3}\otimes\bar{\mathbf{3}}\otimes\mathbf{3}\otimes\bar{\mathbf{3}}$), pentaquarks ($\mathbf{3}^{\otimes 4}\otimes\bar{\mathbf{3}}$). Both contain color singlets; both are observed (LHCb 2015).
  5. Regge spectrum: in a linear potential, the rotational excitations of a string have $M^2 \propto L$, giving the famous Chew-Frautschi plot. Derive the slope from $\sigma_{\rm QCD}/\pi$. (4.12.51)–(4.12.53)
  6. Plot the four leading Regge trajectories (π, ρ, N, Δ) against PDG; the common slope $\alpha' \approx 0.9\,{\rm GeV}^{-2}$ matches experiment within 5%. (4.12.54)
  7. A brief, honest caveat: the *intercepts* of the Regge trajectories depend on the quark masses from Ch 10, so their absolute position inherits Ch 10's error bars; the *slopes* are rigorous within the linear-potential approximation.
- **Exit condition:** The reader has the classification theorem, the Regge plot, and the inheritance noted.
- **Figures:** Fig 4.12.6 (Regge trajectories).
- **Target length:** ~1,400 words.

## §12.7 The QCD precision ledger [honest totals]

- **Topic sentence:** Here is the full bill of goods and honest comparison.
- **Key content:** Produce Table 4.12.1:

  | Observable | Framework | PDG 2022 | Δ / PDG | Rigor |
  |---|---|---|---|---|
  | $\alpha_s(M_Z)$ | 0.1179 (matched) | 0.1179 ± 0.0010 | 0 (matched) | APPROXIMATE (normalization) |
  | $\sigma_{\rm QCD}$ | (420 MeV)² | (465 ± 35 MeV)² (lattice) | ~20% | APPROXIMATE |
  | $\Lambda_{\rm QCD}$ | 200 MeV | 210 ± 14 MeV | ~5% | APPROXIMATE |
  | $\beta_0$ (at $n_f=6$) | 7 | 7 | 0 | RIGOROUS |
  | $C_F$ | 4/3 | 4/3 | 0 | RIGOROUS |
  | $m_{J/\psi}$ | 3.10 ± 0.04 GeV | 3.0969 | < 0.2% | PHENOMENOLOGICAL (inherits $m_c$) |
  | $m_\Upsilon$ | 9.48 ± 0.05 GeV | 9.4603 | < 0.3% | PHENOMENOLOGICAL (inherits $m_b$) |
  | $m_\pi$ | 140 (inherited from Ch 10) | 139.6 | Ch 10 | PHENOMENOLOGICAL |
  | $m_p$ | 938 (inherited from Ch 10) | 938.3 | Ch 10 | PHENOMENOLOGICAL |
  | Regge slope $\alpha'$ | 0.88 GeV$^{-2}$ | 0.90 ± 0.04 | ~2% | APPROXIMATE |

- **Target length:** ~800 words.

## §12.8 Honest ledger — what is derived, what is matched, what is inherited

- **Key content:** Three-column visual list (see Fig 4.12.7). Short prose for each entry.
- **Target length:** ~800 words.

## §12.9 Test-suite verification [RIGOROUS]

- **Key content:** Point at `Research/Mathematical_Models/06_Nuclear_and_Particle_Physics/test_nuclear_physics.py` (which includes the confinement, Regge, and running-coupling tests) and report the current pass/fail status with honest caveats.
- **Target length:** ~400 words.

## §12.10 Handoffs to Chapter 13

- **Key content:** Ch 12 has produced the gauge structure and the confinement mechanism; Ch 13 inherits the mass eigenstates of the quarks and computes the CKM and PMNS matrices. State exactly which quantities Ch 13 will need from this chapter ($\alpha_s(\mu)$ at various scales, the singlet classification, the hadron spectrum) vs from Ch 10 (quark masses) and Ch 11 (Yukawa structure, $v$).
- **Target length:** ~500 words.

## Problem set

- See SPEC for topics. 9 problems. Computational → conceptual → challenge.
- **Target length:** ~800 words.

---

## Outline Review Checklist

- [x] Every chapter requirement maps to at least one section (Ch12-001 → §12.1; Ch12-002 → §12.2; Ch12-003 → §12.3; Ch12-004 → §12.3; Ch12-005 → §12.5; Ch12-006 → §12.5, §12.7; Ch12-007 → §12.4; Ch12-008 → §12.6; Ch12-009 → §12.6; Ch12-010 → §12.7; Ch12-011 → §12.8; Ch12-012 → §12.1, §12.2; Ch12-013 → Problem set; Ch12-014 → §12.10).
- [x] No section uses concepts not yet established (KK reduction from Ch 6, Feynman rules from Ch 7, beta function formalism from Ch 8, quark masses from Ch 10, gauge boson sector from Ch 11).
- [x] "Why" chain is unbroken (each section has a "why" entry point that is answered in prior material or in that section).
- [x] Prerequisites satisfied (see Prerequisites table in SPEC).
- [x] Figure plan complete (7 figures: roadmap, orbifold, flux tube, Cornell, running $\alpha_s$, Regge, honest ledger).

## Target total word count

~11,700 words (within the 9,000–14,000 Foundations window). 62 equations numbered (4.12.1)–(4.12.62), contiguous.
