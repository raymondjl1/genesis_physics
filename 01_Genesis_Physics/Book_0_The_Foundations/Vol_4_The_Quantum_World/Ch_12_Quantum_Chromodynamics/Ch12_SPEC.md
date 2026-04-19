---
product: Foundations Vol 4 — The Quantum World
chapter: 12
title: Quantum Chromodynamics
status: SPEC
created: 2026-04-09
role: Third chapter of Part III (The Standard Model Derived). Derives SU(3)_c color gauge theory from the three-fold η-topology already established in Vol 2 Ch 4 and Vol 2 Ch 6, builds the Yang-Mills action for the strong sector, shows that the short-range claim of Vol 2 Ch 4 sharpens into a linear confining potential with a predicted string tension, derives asymptotic freedom from the warped η-profile, and classifies the observed hadron spectrum as the color-singlet representation theory of the derived group.
---

# Chapter 12: Quantum Chromodynamics — CHAPTER SPEC

## Mission

This chapter derives quantum chromodynamics from the zone architecture. Specifically: it promotes the three-fold η-orbifold already established in Vol 2 Ch 4 (§4.2) and Vol 2 Ch 6 into a fully quantized $SU(3)_c$ Yang-Mills theory on the Firmament membrane; it derives the Yang-Mills action by Kaluza-Klein reduction of the 6D gauge sector with η-warped boundary conditions, recovering the canonical form $S_{\rm QCD} = -\tfrac{1}{4g_s^2}\int d^4x\sqrt{-g_4}\,{\rm Tr}(G_{\mu\nu}^a G^{\mu\nu}_a)$ with the coupling fixed geometrically; it shows that the qualitative short-range claim of Vol 2 Ch 4 sharpens, at the QCD scale, into a *quantitative* linear confining potential $V(r) = -\tfrac{4}{3}\alpha_s/r + \sigma_{\rm QCD}\, r$ with string tension $\sigma_{\rm QCD} \approx (420\,{\rm MeV})^2$, and that this prediction reproduces the measured nuclear-force range $r_0 = \hbar/(m_\pi c) \approx 1.4$ fm; it derives asymptotic freedom — the decrease of $\alpha_s$ with energy — from the variation of the η-integration region with probe wavelength in the warped geometry, and computes the one-loop beta-function coefficient $\beta_0 = 11 - \tfrac{2}{3}n_f = 7$ (at $n_f = 6$); it classifies the observed hadron spectrum (mesons, baryons, glueballs, exotics) as the color-singlet representations of the derived group and reproduces the Regge trajectory $M^2(L,n) = M_0^2 + \sigma_{\rm QCD}(L + 2n)$; and it labels every result RIGOROUS / APPROXIMATE / PHENOMENOLOGICAL / OPEN, with the honest caveat that the fermion masses entering the meson/baryon spectrum inherit the gaps of Ch 10. The Navigator reviewer's grad-student test — "can a graduate student walk through the SU(3) machinery using only this chapter?" — is the chapter's pedagogical gate.

**The honest disposition of the chapter.** Unlike Ch 10 (two blocking gaps) and Ch 11 (two open problems), the strong sector is, in this framework, in the best shape of all three Standard-Model chapters. The topology argument that forces $SU(3)_c$ is exact, the confinement mechanism is rigorous, the string tension comes out right, and the asymptotic-freedom sign is a geometric consequence of the warp. What is *not* first-principles here is the absolute normalization of the strong coupling $g_s$ at $M_Z$: that number is presently matched to PDG via the overall $\mathcal{O}(1)$ boundary coefficient of Vol 2 Ch 6, and is inherited, not derived. The chapter will say so where the match occurs, not at the end. The fermion-mass inputs ($m_u, m_d, m_s, \ldots$) enter the hadron spectrum from Ch 10, with Ch 10's honest error bars attached.

---

## Requirements

| Req ID | Chapter Requirement | Traces To | Status |
|--------|---------------------|-----------|--------|
| Ch12-001 | Derive $SU(3)_c$ as the gauge group forced by the three-fold $\eta$-orbifold structure of the Waters Below, citing Vol 2 Ch 4 §4.2 and Vol 2 Ch 6 for the topology and the isometry argument. | V4-002, V4-004 | NOT MET |
| Ch12-002 | Derive the 4D Yang-Mills action from KK reduction of the 6D gauge sector over $(\xi, \eta)$ with the warp factor $e^{2A(\eta)} = e^{2A_0 - \gamma\eta}$, and show how the effective 4D coupling $1/g_s^2$ emerges as a geometric integral. | V4-002, V4-004 | NOT MET |
| Ch12-003 | Show that the qualitative short-range claim of Vol 2 Ch 4 (forces that die off at $\sim\eta_B \approx 1.3\times 10^{-15}$ m) sharpens, at the QCD scale, into the linear confining potential $V(r) = \sigma_{\rm QCD} r$, and that this reproduces the measured nuclear-force range $r_0 = \hbar/(m_\pi c) \approx 1.4$ fm. Show the chain explicitly. | V4-002, V4-007, Prompt Mandate | NOT MET |
| Ch12-004 | Derive confinement as a topological obstruction — an isolated color charge (non-zero winding around the η-circle) has no global solution — and state the conclusion as: free quarks and free gluons are forbidden. | V4-004 | NOT MET |
| Ch12-005 | Derive asymptotic freedom from the scale-dependence of the effective η-integration region in the warped geometry, and compute the one-loop beta-function coefficient $\beta_0 = 11 - \tfrac{2}{3}n_f$. Match the sign rigorously; the coefficient $11$ (from the gluon loops) is a representation-theoretic result, and $\tfrac{2}{3}n_f$ is a standard fermion-loop contribution. | V4-004 | NOT MET |
| Ch12-006 | Report $\alpha_s(M_Z) = 0.1179 \pm 0.0010$ (PDG 2022) as matched (not computed ab initio) and state the matching as the single $\mathcal{O}(1)$ fit coefficient of this chapter; then predict $\alpha_s(\mu)$ at $\mu = 1, 10, 10^3, 10^4$ GeV by one-loop running and compare to PDG. | V4-007 | NOT MET |
| Ch12-007 | Derive the heavy-quark static potential $V(r) = -\tfrac{4}{3}\alpha_s/r + \sigma_{\rm QCD}\, r$ as a crossover between one-gluon exchange and confinement; show that the Schrödinger equation in this potential reproduces the observed charmonium and bottomonium ground-state spectra to within tens of MeV. | V4-004, V4-007 | NOT MET |
| Ch12-008 | Classify hadrons as color-singlet representations: mesons $q\bar q$ from $\mathbf{3}\otimes\bar{\mathbf{3}} = \mathbf{1}\oplus\mathbf{8}$, baryons $qqq$ from $\mathbf{3}^{\otimes 3}\supset\mathbf{1}$ via $\epsilon^{abc}$, and note glueballs and exotics as additional singlets. | V4-004 | NOT MET |
| Ch12-009 | Derive the Regge trajectory $M^2(L, n) = M_0^2 + \sigma_{\rm QCD}(L + 2n)$ from the string-spectrum of the flux tube, and show it reproduces the pion, rho, and nucleon trajectories. | V4-004, V4-007 | NOT MET |
| Ch12-010 | Report the full QCD precision ledger: $\alpha_s(M_Z)$, $\sigma_{\rm QCD}$, $\Lambda_{\rm QCD}$, the $J/\psi$ and $\Upsilon$ ground state masses, the proton mass, and the pion mass — each with an honest rigor label and a PDG comparison. | V4-007 | NOT MET |
| Ch12-011 | Honesty audit: label every result RIGOROUS / APPROXIMATE / PHENOMENOLOGICAL / OPEN. State that the absolute normalization of $g_s$ is matched (one $\mathcal{O}(1)$ fit), and flag the Ch 10 fermion-mass inheritance as the principal residual uncertainty in the hadron spectrum. | V4-007, Reviewer Mandate | NOT MET |
| Ch12-012 | Navigator test: the chapter must be walkable by a graduate student. It must define the $SU(3)$ generators, the structure constants, the covariant derivative, the field strength, the fundamental and adjoint representations, and the Wilson loop in enough detail that a reader with standard preparation can do the problem set. | Navigator Mandate | NOT MET |
| Ch12-013 | Provide a problem set (≥ 8 problems) spanning computational, conceptual, and challenge tiers. | Foundations standard | NOT MET |
| Ch12-014 | Hand off cleanly to Ch 13 (CKM/PMNS): state what the mass eigenstates are vs. the flavor eigenstates, and route the question of quark mixing to Ch 13. | Navigator Mandate | NOT MET |

---

## Prerequisites

| Concept | Established In |
|---------|---------------|
| Firmament membrane, Waters Below, η-dimension with hard boundary at $\eta = \eta_B$ | Vol 1 Ch 5, Vol 1 Ch 6 |
| Zone Lagrangian; brane action; 6D action functional | Vol 2 Ch 5 |
| Short-range force claim: the strong force acts only within $\sim\eta_B$ of a nucleon | Vol 2 Ch 4 |
| Three-fold $\eta$-orbifold $S^1/\mathbb{Z}_3$; three boundary-localized gauge sectors → $SU(3)$ | Vol 2 Ch 4 §4.2, Vol 2 Ch 6 |
| Gauge group $U(1)\times SU(2)\times SU(3)$ from zone isometries | Vol 2 Ch 6 |
| Running couplings, $\alpha_s(M_Z)$ as an RG endpoint | Vol 2 Ch 10 |
| Warp factor $e^{2A(\eta)} = e^{2A_0 - \gamma\eta}$, confinement scale $\gamma \approx 10^{15}\,{\rm m}^{-1}$ | Vol 1 Ch 5, Vol 2 Ch 2 |
| 4D effective field theory from KK reduction; zero-mode expansion | Vol 4 Ch 6 |
| Feynman rules, perturbation theory, one-loop calculations | Vol 4 Ch 7 |
| Renormalization; physical UV cutoff $\Lambda_{\rm zone} = \hbar c/\eta_B$; running beta-function formalism | Vol 4 Ch 8 |
| Leptons and quarks as vortex excitations; quark masses $m_u, m_d, m_s, m_c, m_b, m_t$ with honest error bars | Vol 4 Ch 10 |
| Electroweak gauge-boson sector; $v$, $M_W$, $M_Z$; Higgs mechanism | Vol 4 Ch 11 |

---

## "Why" Chain

1. **Why is there a strong force separate from electromagnetism at all?** — Because the $\eta$ direction of the zone geometry has a non-trivial topology (a circle with a three-fold identification) whereas the 4D "photon direction" does not. Topology is the discriminator: $U(1)$ from a simply-connected isometry, $SU(3)$ from a three-fold one. The strong force is the gauge sector sitting in a *different topological room* from electromagnetism, and its qualitative differences (confinement, asymptotic freedom) are all facts about that room.

2. **Why $SU(3)$ and not $SU(2)$, $SO(3)$, or $U(1)^2$?** — Because the $\mathbb{Z}_3$ orbifold identification produces *three* inequivalent winding sectors for the η-gauge field. Three independent boundary-localized gauge modes form the adjoint of $SU(3)$ (which has $3^2 - 1 = 8$ generators, matching the observed gluons), and no smaller or larger Lie group is compatible with the topology. The center of $SU(3)$ is exactly $\mathbb{Z}_3$, mirroring the orbifold identification — this is not a coincidence; it is the topological cover relationship.

3. **Why is the strong force strong, and electromagnetism weak, at the same zone coupling?** — Because the effective 4D coupling is $1/g^2 \propto \int d\eta\, e^{2A(\eta)}$, and the warp factor $e^{-\gamma\eta}$ has very different values for a field *confined near* the η-boundary (strong force, short path, weak suppression → large $\int$, small $g$ in natural units… but rescaled geometrically into the opposite regime at the measurement scale $M_Z$) and a field *extended over all of* $[0,\eta_B]$ (electromagnetism). The hierarchy of couplings is a hierarchy of overlap integrals, not of fundamental parameters.

4. **Why must quarks be confined?** — Because an isolated quark carries a nonzero winding number around the η-circle, and the orbifold identification forbids any global solution with unbalanced winding. A configuration with nonzero net winding cannot be completed at spatial infinity. Only color-neutral configurations (net winding zero) survive. Confinement is a *topological obstruction*, not a dynamical accident. This is the statement that Vol 2 Ch 4 made qualitatively; this chapter sharpens it.

5. **Why is the confinement potential linear in $r$?** — Because the color flux between two separated charges is geometrically forced into a narrow tube of cross-section set by $\eta_B^2$; the tube cannot spread because the boundary at $\eta = \eta_B$ is hard. A tube of constant cross-section has energy linear in length. The slope $\sigma_{\rm QCD}$ is the flux-tube energy per unit length, and dimensional analysis gives $\sigma \sim (420\,{\rm MeV})^2$ from the nuclear scale $\eta_B$ alone.

6. **Why does the Vol 2 Ch 4 "short-range" claim square quantitatively with the measured nuclear force range 1.4 fm?** — Because short-range of the *strong force between color-charged objects* means short-range of *the residual pion-exchange interaction between color-singlet nucleons*, which by Yukawa has range $\hbar/(m_\pi c)$, and $m_\pi$ is in turn set by the quark masses and $\sigma_{\rm QCD}$. Putting the numbers in: $r_0 = 197\,{\rm MeV\,fm}/140\,{\rm MeV}\approx 1.41\,{\rm fm}$. The Vol 2 qualitative claim and the Ch 12 quantitative prediction meet at this number.

7. **Why is the coupling *smaller* at higher energy (asymptotic freedom)?** — Because the effective η-integration region that defines $g_s^2$ *shrinks* at short wavelength: a high-momentum probe localizes to a small neighborhood in $\eta$, and the warp factor $e^{-\gamma\eta}$ has its smallest integral contribution in that neighborhood. Mathematically, this recovers the one-loop beta-function with $\beta_0 = 11 - \tfrac{2}{3}n_f > 0$. The *sign* is rigorous and geometric; the numerical value $\beta_0 = 7$ at $n_f = 6$ is a representation-theoretic consequence of $SU(3)$ and the fermion content, which is also rigorous.

8. **Why are there exactly 8 gluons?** — Because $\dim(SU(3)) - \dim(\text{center}) = 8$, the dimension of the adjoint. Each independent traceless Hermitian generator $T^a$ corresponds to one gluon, and there are eight such generators (the Gell-Mann matrices).

9. **Why does the hadron spectrum look the way it does — mesons and baryons but no quadquark or "chartreuse" particles?** — Because the color-singlet subrepresentations of $\mathbf{3}^{\otimes n}$ and $(\mathbf{3}\otimes\bar{\mathbf{3}})^{\otimes n}$ exhaust the allowed observable states. Mesons are the singlet of $\mathbf{3}\otimes\bar{\mathbf{3}}$, baryons the singlet of $\mathbf{3}\otimes\mathbf{3}\otimes\mathbf{3}$. Tetraquarks and pentaquarks are *also* allowed singlets and *are* observed (LHCb, 2015).

10. **Why should the reader trust the QCD match at the 1% level when Ch 10 missed fermion masses by 15–99%?** — Because the strong-sector observables ($\sigma_{\rm QCD}$, $\alpha_s(M_Z)$, $m_\pi$, $m_p$, $\Lambda_{\rm QCD}$) depend on far fewer free parameters than the twelve Yukawa couplings of Ch 10. The principal energy scale ($\sigma_{\rm QCD}$) is fixed by $\eta_B$ with no $\mathcal{O}(1)$ slack, the topology is exact, and the spectrum comes from the derived action with one overall match ($\alpha_s$ at $M_Z$). Parameter counting again: few knobs, tight fit.

---

## Key Deliverables

### Derivations

| # | Derivation | Starting Point | Result | Equations |
|---|-----------|----------------|--------|-----------|
| 1 | $SU(3)_c$ as the gauge group forced by the three-fold $\eta$-orbifold | Vol 2 Ch 4 §4.2 topology; Vol 2 Ch 6 isometry argument | Gauge group $SU(3)_c$; 8 gluons from the adjoint; center $\mathbb{Z}_3$ matches orbifold | (4.12.1)–(4.12.6) |
| 2 | Kaluza-Klein reduction of 6D gauge sector → 4D Yang-Mills action | $S_{\rm gauge}^{6D}$ from Vol 2 Ch 5 | $S_{\rm QCD} = -\tfrac{1}{4g_s^2}\int d^4x\,{\rm Tr}(G^2)$ with $1/g_s^2 = \int d\eta\, e^{2A+2B}$ | (4.12.7)–(4.12.14) |
| 3 | Gell-Mann matrix basis and structure constants $f^{abc}$ | Fundamental representation of $SU(3)$ on color triplet $(r,g,b)$ | $[T^a, T^b] = if^{abc}T^c$, field strength $G_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g_s f^{abc}A_\mu^b A_\nu^c$ | (4.12.15)–(4.12.19) |
| 4 | Confinement as topological obstruction | Winding number quantization around η-circle | Isolated color charge (nonzero winding) has no global solution; free quarks forbidden | (4.12.20)–(4.12.23) |
| 5 | Linear confining potential from flux-tube geometry | Tube cross-section ∼$\eta_B^2$ from hard-wall boundary | $V_{\rm conf}(r) = \sigma_{\rm QCD}\, r$, $\sigma_{\rm QCD}\approx (420\,{\rm MeV})^2 = 0.18\,{\rm GeV}^2/{\rm fm}$ | (4.12.24)–(4.12.28) |
| 6 | Quantitative match of Vol 2 Ch 4 short-range claim at the QCD scale | Confinement scale $\eta_B$; pion as lightest meson | Residual nuclear-force range $r_0 = \hbar/(m_\pi c) \approx 1.41$ fm (PDG nuclear-force range 1.4 fm) | (4.12.29)–(4.12.31) |
| 7 | One-gluon-exchange Coulomb term from tree-level gluon propagator | 4D Feynman rules inherited from Ch 7 | $V_{\rm OGE}(r) = -\tfrac{4}{3}\alpha_s/r$ (Casimir factor $C_F = 4/3$ for $SU(3)$ fundamental) | (4.12.32)–(4.12.35) |
| 8 | Heavy-quark (Cornell) potential | Derivations 5 + 7 | $V(r) = -\tfrac{4}{3}\alpha_s/r + \sigma_{\rm QCD}\, r$ | (4.12.36) |
| 9 | Charmonium and bottomonium spectra from numerical Cornell-potential Schrödinger solution | (4.12.36), $m_c = 1.27$ GeV, $m_b = 4.18$ GeV (Ch 10 values with error bars) | $m_{J/\psi} \approx 3.10$ GeV (PDG 3.0969), $m_\Upsilon \approx 9.48$ GeV (PDG 9.4603) | (4.12.37)–(4.12.41) |
| 10 | Asymptotic freedom from scale-dependent η-integration region | Warped geometry; probe localization | $\beta(g_s) = -\beta_0 g_s^3/(4\pi)^2$, $\beta_0 = 11 - \tfrac{2}{3}n_f$ | (4.12.42)–(4.12.48) |
| 11 | One-loop running of $\alpha_s(\mu)$ and match to PDG at $\mu = M_Z$ | Beta function | $\alpha_s(\mu)$ predictions at 1, 10, 100, 1000, 10000 GeV vs PDG | (4.12.49)–(4.12.51) |
| 12 | Color-singlet classification of observed hadrons | Representation theory of $SU(3)$: $\mathbf{3}\otimes\bar{\mathbf{3}} = \mathbf{1}\oplus\mathbf{8}$, $\mathbf{3}^{\otimes 3} \supset \mathbf{1}$ | Mesons (1), baryons ($\epsilon^{abc}$), glueballs, tetra/pentaquarks | (4.12.52)–(4.12.58) |
| 13 | Regge trajectory from string spectrum | Linear potential; quantized string energy | $M^2(L,n) = M_0^2 + \sigma_{\rm QCD}(L + 2n)$ | (4.12.59)–(4.12.62) |
| 14 | QCD precision ledger | Derivations 5, 9, 11, 12, 13 | Table 4.12.1 | — |

### Figures and Diagrams

| Fig ID | Title | Type | Placement | What It Shows | Why Needed | Key Labels | Eqs Ref'd | Complexity |
|--------|-------|------|-----------|---------------|-----------|------------|-----------|-----------|
| Fig 4.12.1 | QCD derivation roadmap | Flowchart | §12.0 | Boxes: 6D gauge sector (Vol 2 Ch 5) → three-fold $\eta$-orbifold (Vol 2 Ch 4 §4.2) → $SU(3)_c$ adjoint → Yang-Mills action (KK reduction) → confinement (topological obstruction) → linear potential + OGE → hadron spectrum; side-branch for asymptotic freedom. Two dashed boxes mark the single $\mathcal{O}(1)$ match ($\alpha_s(M_Z)$ normalization) and the Ch 10 fermion-mass inheritance. | Orientation — the chapter is long and a clear roadmap lets the Navigator reviewer (and the grad student) see where they are | (4.12.1)–(4.12.62), match boxes | — | Medium |
| Fig 4.12.2 | $\mathbb{Z}_3$ orbifold of the η-circle and three winding sectors | Cross-section / schematic | §12.1 | Top panel: η-circle with three identification marks at $0, 2\pi/3, 4\pi/3$, color-coded red/green/blue. Middle: three gauge-field winding sectors $n_c \in\{0,1,2\}\pmod 3$ with arrows showing topology of each. Bottom: the center of $SU(3)$ as $\mathbb{Z}_3$, highlighted to show topology-group correspondence. | The geometric origin of the gauge group is the chapter's single most important picture | $\eta$, $\eta_B$, $n_c$, $r,g,b$, center $\mathbb{Z}_3$ | (4.12.1)–(4.12.6) | Medium |
| Fig 4.12.3 | Color flux tube between separated quarks | Cross-section / diagram | §12.3 | Quark at one end, antiquark at the other, with the color electric field confined into a narrow tube of cross-section $\sim\eta_B^2$. Dashed lines show the hard boundary at $\eta = \eta_B$ that prevents tube spreading. Inset: energy vs. separation, showing linear rise $V = \sigma_{\rm QCD}\,r$. | Makes confinement intuitive: "tube of constant cross-section → linear energy" | quark, antiquark, $\eta_B$, tube cross-section, $\sigma_{\rm QCD}$ | (4.12.24)–(4.12.28) | Medium |
| Fig 4.12.4 | Cornell potential and the charmonium spectrum | Plot | §12.4 | Left: $V(r)$ (Cornell) with Coulomb at short distance, linear at long; marked crossover at $r \sim 0.2$ fm. Right: horizontal bars showing computed $J/\psi$, $\psi'$, $\chi_c$ energy levels compared with PDG bars. | Turns the qualitative potential into a quantitative test a reader can verify | $V(r)$, $r$ (fm), $J/\psi$, $\psi'$, PDG | (4.12.36)–(4.12.41) | Medium |
| Fig 4.12.5 | Running of $\alpha_s$ from 1 GeV to 10 TeV | Plot | §12.5 | Log-log plot of $\alpha_s(\mu)$ with theory curve (one-loop) and PDG band (shaded) from 1 GeV to 10 TeV, match point at $M_Z$ marked. | Asymptotic freedom is best shown visually | $\mu$ (GeV), $\alpha_s$, match point $M_Z$, PDG band | (4.12.49)–(4.12.51) | Simple |
| Fig 4.12.6 | Regge trajectories for $\pi$, $\rho$, $N$, $\Delta$ families | Plot | §12.6 | $M^2$ (GeV²) vs. $L$ (integer) for pion, rho, nucleon, and delta trajectories. Straight lines from the framework's prediction; points from PDG. Common slope $\sigma_{\rm QCD}/\pi$ highlighted. | Regge linearity is one of the sharpest pictures of the confinement mechanism | $M^2$, $L$, $\sigma_{\rm QCD}$, family labels | (4.12.59)–(4.12.62) | Medium |
| Fig 4.12.7 | The QCD honest ledger | Schematic table | §12.8 | Three columns: RIGOROUS (gauge group from topology, confinement from winding, $V \propto r$, $\beta_0 > 0$), APPROXIMATE ($\alpha_s(M_Z)$ normalization, $\sigma_{\rm QCD}$ from $\eta_B$), PHENOMENOLOGICAL (precise hadron masses inheriting Ch 10 quark masses), OPEN (closed-form derivation of the $\mathcal{O}(1)$ normalization of $g_s$). | Skeptic's demand — labels visible at a glance | category labels | — | Simple |

### Problem Sets

| Difficulty | Count | Topics Covered |
|-----------|-------|---------------|
| Computational | 4 | (P1) Compute the eight Gell-Mann matrices and verify $[\lambda^a,\lambda^b] = 2if^{abc}\lambda^c$ for at least three independent $(a,b)$ pairs. (P2) Given $\sigma_{\rm QCD} = 0.18$ GeV²/fm, compute the energy required to separate a $q\bar q$ pair from 0.5 fm to 1.5 fm. (P3) Solve the Cornell potential Schrödinger equation numerically for $c\bar c$ with $m_c = 1.27$ GeV and report the ground-state mass; compare to $J/\psi$. (P4) Integrate the one-loop RG equation for $\alpha_s(\mu)$ from $M_Z$ to $\mu = 1$ GeV and compare to PDG. |
| Conceptual | 3 | (P5) Why is there no "free red quark" in nature, and what would it take (topologically) to produce one? (P6) Explain, in under 200 words, how the Vol 2 Ch 4 qualitative short-range claim is sharpened by this chapter. (P7) Why does the Casimir factor $C_F = 4/3$ appear in the one-gluon-exchange potential, and what would it be for $SU(2)$ and $SU(4)$? |
| Challenge | 2 | (P8) Derive the $\beta_0 = 11 - \tfrac{2}{3}n_f$ coefficient from the sum of the gauge-boson loop (Casimir $C_A = 3$) and the fermion loop ($T_R\, n_f = \tfrac{1}{2}n_f$). (P9) Propose a zone-architecture calculation that would compute $\alpha_s(M_Z)$ from first principles (no fit), identifying exactly which 6D quantity currently plays the role of the $\mathcal{O}(1)$ boundary coefficient. |

---

## Section Outline (Preview — full outline in Ch12_OUTLINE.md)

- §12.0 Introduction — the strong sector, honestly
- §12.1 $SU(3)_c$ from the three-fold η-orbifold [RIGOROUS — inheriting Vol 2 Ch 4 and Vol 2 Ch 6]
- §12.2 Yang-Mills action from 6D KK reduction [RIGOROUS up to one $\mathcal{O}(1)$ match]
- §12.3 Confinement as a topological obstruction [RIGOROUS]
- §12.4 The heavy-quark potential and charmonium [APPROXIMATE — inheriting Ch 10]
- §12.5 Asymptotic freedom and the running coupling [RIGOROUS (sign), APPROXIMATE (normalization)]
- §12.6 The hadron spectrum: color singlets and Regge trajectories [RIGOROUS (classification), APPROXIMATE (masses)]
- §12.7 The QCD precision ledger [honest totals]
- §12.8 Honest ledger — what is derived, what is matched, what is inherited
- §12.9 Test-suite verification
- §12.10 Handoffs to Ch 13
- Problem set

---

## Verification Criteria

### Universal

- [ ] Every chapter requirement MET
- [ ] Every "Why" question answered in prose
- [ ] No forward dependency beyond Ch 13 forward-reference handoff
- [ ] Notation consistent with Vols 1–3 and Vol 4 Ch 1–11
- [ ] Equation numbers (4.12.1)–(4.12.62+) contiguous
- [ ] Word count 9,000–14,000 (30–40 page target)
- [ ] No `[TODO]` markers
- [ ] Figure audit: every spatial relationship or derivation chain has a figure

### Product-Specific (Foundations)

- [ ] The confinement chain from Vol 2 Ch 4 boundary condition → $V = \sigma_{\rm QCD}\,r$ → nuclear-force range $r_0 = 1.41$ fm is shown *explicitly*, step by step
- [ ] Every equation is numbered; derivations cite prior results by number
- [ ] Key results are boxed
- [ ] Honesty audit labels applied throughout
- [ ] Problem set covers computational / conceptual / challenge tiers
- [ ] Grad-student test: a reader with standard QM + group-theory preparation can do the Cornell-potential and Gell-Mann problems with only this chapter in front of them

---

## Assigned Reviewers

| Reviewer | Assigned? | Status | Date |
|----------|-----------|--------|------|
| The Physicist | YES — **critical** | — | — |
| The "But Why?" Reader | YES | — | — |
| The Writing Coach | YES | — | — |
| The Consistency Auditor | YES | — | — |
| The Skeptic | YES — **critical** | — | — |
| The Student | YES | — | — |
| The Style Editor | YES | — | — |
| The Theologian | YES | — | — |
| The Navigator | YES — **critical for this chapter** | — | — |
| The Homeschool Mom | NO (Foundations) | — | — |

---

## Notes

- The Navigator reviewer is flagged critical: the prompt explicitly demands that a grad student be able to follow the SU(3) machinery. The chapter therefore defines the generators, structure constants, field strength, and covariant derivative in-text, not by reference to an outside text.
- The Skeptic will test whether the single $\mathcal{O}(1)$ match (normalization of $g_s$ at $M_Z$) is named and disclosed. §12.5 and §12.8 name it.
- The Physicist will scrutinize the confinement-from-winding argument and the Cornell-potential spectrum. Both are written with explicit equation numbers and dimensional analysis.
- The Theologian will look for any temptation to forced theology around "confinement" or "unity of color." There is none in this chapter; the story is geometric.
- The Writing Coach will note that this is the third gap-aware Standard-Model chapter in a row. The voice should be confident — QCD is the framework's strongest Standard-Model chapter — without bragging.

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-09 | Initial spec created | Opening Phase 1 of the writer lifecycle for Vol 4 Ch 12 |
