# Chapter Outline — Vol 5 Ch 1
## Einstein Field Equations Recovered

Ten sections. Total target: ~15,000 words.

---

### §1.0 Opening — Why This Chapter Matters (~600 words)

- **Topic sentence:** Vol 2 Ch 8 gave us linearized GR; this chapter closes the loop by deriving the full nonlinear Einstein field equations as a consequence of the 6D zone action.
- **"Why" entry:** The universe is not always weak-field. Mercury, binary pulsars, black holes, the expanding cosmos — each of these is a regime where $h_{\mu\nu}$ is not small. If we stopped at Vol 2 Ch 8 we would have no framework for any of them.
- **Key content:** State the end goal of the chapter (Eq. 5.1.22), preview the chain (Fig 5.1.1), and be honest about what is *not* in this chapter (numerical tests — those are Ch 2).
- **Exit condition:** Reader understands the stakes and has the roadmap.

### §1.1 What Vols 1, 2, and 3 Already Gave Us (~1,100 words)

- **§1.1.1** The 6D metric from Vol 1 Ch 4 — recall the warp-factored form (1.4.2).
- **§1.1.2** The 6D Einstein equations from Vol 1 Eq. (1.4.66); the preview of projection from Vol 1 §4.8.4; the warp-factor ODEs of Vol 1 §4.8.5.
- **§1.1.3** Vol 2 Ch 2's derivation of Newton's constant $G_4=G_6/V_\text{extra}$.
- **§1.1.4** Vol 2 Ch 8's linearized wave equation (2.8.12) — the piece we now have to extend.
- **§1.1.5** A frank statement of what we still owe: the *nonlinear* projection, all the way down to the full $G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G_4}{c^4}T_{\mu\nu}$, plus the Schwarzschild and Kerr solutions, plus the proof that energy-momentum conservation is automatic.
- **Figure 5.1.1** here: the derivation chain.
- **Exit condition:** Reader knows what's in hand and what the chapter must deliver.

### §1.2 Dimensional Reduction of the 6D Action (~2,000 words)

- **§1.2.1** Statement of the starting action: the 6D Einstein–Hilbert piece $S_\text{grav}^{(6)}=\frac{1}{2\kappa_6^2}\int d^6x\sqrt{-g_6}\,R_6$, with the full zone action of Vol 1 §4.8 sketched for context.
- **§1.2.2** The KK ansatz: insert the block-diagonal warp-factored metric (Vol 1 Eq. 1.4.2) and compute $\sqrt{-g_6}=e^{4A+2B}\sqrt{-\tilde g}\,\sqrt{\tilde h_{(2)}}$ where $\tilde g$ is the 4D induced metric and $\tilde h_{(2)}$ the 2D extra-dimensional metric.
- **§1.2.3** Decomposition of the 6D Ricci scalar: $R_6 = e^{-2A}\tilde R_4 + R_\text{extra} + (\text{derivatives of }A,B)$. This is a standard, well-documented calculation; we do the key steps and quote the textbook result for the bookkeeping terms (Duff 1994; Randall–Sundrum 1999).
- **§1.2.4** Why this decomposition works only because the metric is block-diagonal — forward-reference to Problem P1.8 (KK graviphoton).
- **§1.2.5** Integration over the extra dimensions. Define $V_\text{extra} \equiv \int d\xi\,d\eta\,e^{2A+2B}$, and show how it emerges naturally.
- **Figure 5.1.2** (KK reduction geometry).
- **Figure 5.1.3** (warp-weighted volume).
- **Equations (5.1.1)–(5.1.12).**
- **Exit condition:** Reader has the 4D effective action up to the cosmological constant piece.

### §1.3 The 4D Einstein–Hilbert Action Emerges (~1,300 words)

- **§1.3.1** Collecting terms: $S^{(4)} = \frac{1}{2\kappa_4^2}\int d^4x\sqrt{-\tilde g}\,\tilde R_4 + S_{\Lambda} + S_\text{moduli} + S_\text{matter}$, where $\kappa_4^2 = \kappa_6^2/V_\text{extra}$.
- **§1.3.2** Identification of $G_4 = G_6/V_\text{extra}$ (restating the Vol 2 Ch 2 result in the full nonlinear context).
- **§1.3.3** Why no extra vector modes appear at leading order: block-diagonal metric kills the graviphoton; the moduli scalars are frozen by the stabilizing potential of Vol 1 Ch 6 and are discussed separately in Vol 5 Ch 11.
- **§1.3.4** The "why" of Einstein–Hilbert's scalar form: it is the unique two-derivative, diffeomorphism-invariant local action built from the metric alone. Any other attempt either violates diff invariance, introduces ghosts, or is topologically trivial (Lovelock 1971 result stated without proof).
- **Equations (5.1.13)–(5.1.15).**
- **Exit condition:** Reader has a clean 4D Einstein–Hilbert action derived from the 6D starting point.

### §1.4 Variation of the Action — The Einstein Field Equations (~1,800 words)

- **§1.4.1** The variational principle recalled (Vol 3 Ch 2) and specialized to metric variations.
- **§1.4.2** Step-by-step computation of $\delta(\sqrt{-g}\,R)$, including the Palatini identity $\delta R_{\mu\nu}=\nabla_\alpha\delta\Gamma^\alpha_{\mu\nu}-\nabla_\nu\delta\Gamma^\alpha_{\mu\alpha}$, the total-derivative argument (Gibbons–Hawking–York boundary term, noted but not dwelt on).
- **§1.4.3** Variation of the matter piece: the stress-energy tensor *defined* by $T_{\mu\nu}\equiv -\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal{L}_\text{matter})}{\delta g^{\mu\nu}}$.
- **§1.4.4** The combined variation yields $G_{\mu\nu}+\Lambda_\text{eff} g_{\mu\nu}=\frac{8\pi G_4}{c^4}T_{\mu\nu}$.
- **§1.4.5** Dimensional check on the coupling constant.
- **Figure 5.1.4** (variation cartoon).
- **Equations (5.1.16)–(5.1.22).**
- **Exit condition:** The reader now has the full nonlinear EFE in hand as a *derived* consequence.

### §1.5 The Effective Cosmological Constant (~1,000 words)

- **§1.5.1** Origin: $\Lambda_\text{eff} = \Lambda_6 + \text{warp gradients} + \text{averaged bulk stress-energy}$.
- **§1.5.2** Explicit form (matching Vol 1 Eq. 1.4.79).
- **§1.5.3** Why it is small: the delicate cancellation between the bare 6D $\Lambda_6$ and the warp-factor gradient integral; the "natural" order of magnitude after cancellation is set by the Waters replenishment rate — fully quantified in Ch 11.
- **§1.5.4** Honest limit: we do not yet derive the *observed* $\Lambda_\text{obs}\approx 10^{-52}$ m$^{-2}$ here. That quantitative reconciliation is Ch 11. What we do establish is that $\Lambda_\text{eff}$ is a *calculable* function of the warp profile.
- **Equations (5.1.23)–(5.1.27).**
- **Exit condition:** Reader understands where $\Lambda_\text{eff}$ comes from and why its smallness is not a free parameter.

### §1.6 The Schwarzschild Solution (~1,800 words)

- **§1.6.1** Setup: vacuum Einstein equations $R_{\mu\nu}=0$ outside a spherically-symmetric static source.
- **§1.6.2** Spherically symmetric ansatz: most general static metric with $SO(3)$ symmetry.
- **§1.6.3** Computation of the Ricci tensor components (key steps shown; full tensor algebra referenced to Appendix A of Vol 1).
- **§1.6.4** Two equations, two unknowns — solve for the metric functions.
- **§1.6.5** Impose asymptotic flatness as a boundary condition (this is an *honest input*, not a derivation — flagged in §1.10).
- **§1.6.6** Result: the Schwarzschild metric.
- **§1.6.7** Birkhoff's theorem sketched: *any* spherically symmetric vacuum solution is automatically static. Why this is true in one paragraph (no time-dependent monopole mode in a massless spin-2 field).
- **Figure 5.1.5** (Schwarzschild embedding + metric component plots).
- **Equations (5.1.28)–(5.1.36).**
- **Exit condition:** Reader can write down the Schwarzschild metric and knows why it is forced.

### §1.7 The Kerr Metric (Stated and Justified) (~1,200 words)

- **§1.7.1** The physical question: what if the source rotates?
- **§1.7.2** Symmetry requirements: stationary + axisymmetric + asymptotically flat + vacuum.
- **§1.7.3** Statement of the Kerr solution in Boyer–Lindquist coordinates; key length scales $r_s$ and $a=J/(Mc)$.
- **§1.7.4** The Carter–Robinson uniqueness theorem stated without proof: Kerr is the unique such solution.
- **§1.7.5** Horizons, ergosphere, ring singularity — a one-page qualitative tour, tied to Fig 5.1.6. Deep exploration deferred to Ch 5–7.
- **Figure 5.1.6** (Kerr equatorial slice).
- **Equations (5.1.37)–(5.1.41).**
- **Exit condition:** Reader knows the Kerr metric and why it matters for Ch 2 (Lense–Thirring) and Ch 3 (GW).

### §1.8 Bianchi Identities and Energy-Momentum Conservation (~1,400 words)

- **§1.8.1** The geometric identity: $\nabla^\mu G_{\mu\nu}\equiv 0$, valid for *any* metric, not just solutions.
- **§1.8.2** Derivation from the twice-contracted Bianchi identity $\nabla^\mu R_{\mu\nu\rho\sigma}+\text{cyclic}=0$.
- **§1.8.3** Consequence: $\nabla^\mu T_{\mu\nu}=0$ is automatic — energy-momentum conservation is not an extra postulate; it is forced by the geometric structure of the field equations.
- **§1.8.4** Why this is profound: the EFE is *over-determined* in the counting sense; the four contracted Bianchi identities are exactly the four gauge redundancies of diffeomorphism invariance. The system has 10 equations, 4 gauge fixings, leaving 6 physical degrees of freedom — matching the 6 independent metric components after gauge-fixing (linearized count: 2 physical polarizations $\times$ 3 other degrees of freedom).
- **§1.8.5** Reconnection with Vol 1 Ch 7 (Noether): the conserved currents from Killing vectors are now seen as special cases.
- **Figure 5.1.7** (Bianchi closed-surface cartoon).
- **Equations (5.1.42)–(5.1.46).**
- **Exit condition:** Reader sees that conservation of energy-momentum is a geometric theorem, not an assumption.

### §1.9 Consistency with Vol 2 Ch 8 — Linearization Revisited (~900 words)

- **§1.9.1** Substitute $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$ into (5.1.22).
- **§1.9.2** Expand to first order; drop $\mathcal{O}(h^2)$.
- **§1.9.3** Go to harmonic gauge and recover $\Box\bar h_{\mu\nu}=-\frac{16\pi G_4}{c^4}T_{\mu\nu}$ — the Vol 2 Ch 8 result Eq. (2.8.12).
- **§1.9.4** This is the *consistency check*: the full theory derived here reduces, term for term, to what Vol 2 got by a different route (linearizing the already-4D EFE that Vol 2 Ch 2 had handed it).
- **Figure 5.1.8** (linearization recovery diagram).
- **Equations (5.1.47)–(5.1.50).**
- **Exit condition:** Reader has verified that the chapter is internally and cross-volume consistent.

### §1.10 The Reviewer's Ledger: Is This a Derivation? (~1,000 words)

- **§1.10.1** The central question the Physicist reviewer asks: *is this a genuine derivation, or is GR smuggled in somewhere?*
- **§1.10.2** The ledger: a two-column list classifying every step of the chain. Each step is marked as:
  - **D** = derived from the 6D zone action (no new input).
  - **G** = a geometric identity (true by definition of the relevant tensor).
  - **A** = an ansatz or boundary condition that introduces genuinely new information not present in the 6D action alone.
- **§1.10.3** Audit of the ledger:
  - Asymptotic flatness in §§1.6–1.7 is marked **A**. Without it, the Schwarzschild and Kerr solutions are not unique — there are cosmological extensions. We flag this as a boundary condition appropriate for *isolated* systems.
  - The matter action $S_\text{matter}$ is treated as a black box in this chapter, producing $T_{\mu\nu}$ via variation; the specific form depends on what matter lives on the Firmament (Vol 4). But the *form* of how $T_{\mu\nu}$ appears in the EFE is **D** — it is forced by the variational principle.
  - The Gibbons–Hawking–York boundary term is a **G** (it is the unique boundary term that makes the variation well-defined; it does not change the bulk equations).
  - The moduli stabilization result is imported from Vol 1 Ch 6 (the warp-factor profile is a solution of the 6D field equations); this is **D**, not new.
- **§1.10.4** The *remaining* honest limits of the chapter:
  1. We did not compute $\Lambda_\text{eff}$ numerically.
  2. We did not prove Birkhoff or Carter–Robinson from scratch.
  3. We did not discuss matter couplings.
  4. We did not derive the Kerr solution step-by-step (we stated it and cited the uniqueness theorem).
- **§1.10.5** What this chapter *did* do: it produced a verifiable chain from the 6D zone action to the full nonlinear Einstein field equations, with no postulation of GR at any step. The Schwarzschild solution was found as a solution of the derived vacuum equations. The Kerr solution was named and justified by a uniqueness theorem. Energy-momentum conservation was proved as a geometric consequence. The linearized Vol 2 Ch 8 equations were recovered exactly.
- **Figure 5.1.9** (the ledger as a table).
- **Exit condition:** Reader — and the Physicist reviewer — can see precisely which steps are derivations, which are identities, and which are ansätze.

### §1.11 Summary and Forward Connections (~400 words)

- Summary table of key results (5.1.14, 5.1.22, 5.1.25, 5.1.34, 5.1.41, 5.1.46, 5.1.50).
- Forward pointers: Ch 2 (classical tests use 5.1.34), Ch 3 (GW extends 5.1.48), Ch 4 (strong field uses 5.1.41), Ch 5 (black holes), Ch 8 (cosmology uses 5.1.22).
- Closing: the transition from "gravity as a field theory" (Vol 2 Ch 8) to "gravity as the full geometry of spacetime" (this chapter) is complete. Everything else in Vol 5 Part I is about extracting predictions.

---

**Outline review checklist:**
- [x] Every chapter requirement maps to at least one section.
- [x] No section uses concepts not yet established.
- [x] "Why" chain is unbroken.
- [x] Prerequisites are satisfied by prior chapters (Vols 1–4).
- [x] Figure plan complete — 9 figures, every spatial/conceptual/flowchart need addressed.

**Total target:** ~15,000 words; 10 sections + opening; 9 figures; 10 problem set items.
