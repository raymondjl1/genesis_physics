# REVIEWER-01 — The Physicist — Vol 4: The Quantum World

**Persona:** Skeptical PhD physicist (REVIEWER-01)
**Scope:** Vol 4 Ch 1–14 (Manuscript/) + Back_Matter (Appendices A–C, Bibliography, Problem Sets)
**Reference inputs:** Vol 4 CLAUDE.md, Book_0 CLAUDE.md, Quality_Control/Reference/{Glossary, Symbol_and_Constants, Zone_Architecture, Axiom_Summary_Cards}, Vol 1/2/3 inherited results as listed in Appendix A.
**Tag legend:** **C1** flow / **C2** internal conflicts / **C3** cross-references / **C4** biblical-derivation traceability.

---

## Verdict

**FAIL — pass with substantial revisions required.**

There are two unrecoverable problems in the present state of the volume and a long list of recoverable ones. The unrecoverables are:

1. **Two contradictory numerical/structural formulas for ℏ coexist in the volume.** Ch 1 §1.3.2 boxes Eq. (4.1.12) using $(\eta_B/\xi_A)^2 \beta_{\rm geom}$ with β≈480 unresolved, then in the *same* §1.4 Derivation Status box and in §1.4's closing sentence claims CT-4.β is "RESOLVED with zero free parameters" via a different formula $(\xi_0/L_A)^{4/3}$. The boxed equation, the inheritance citations in Ch 2 §2.2.2 (Eq. 1.10.19), Ch 3 §3.2.2, Appendix A entry (1.10.12), and every problem in Ch 1 §1.7 still use the *superseded* form. The chapter itself admits the boxed formula "must be replaced with the correct form in the next draft revision" — that revision has not happened. A reader cannot tell which is the actual claim of the volume.

2. **Λ_zone has two values differing by ~10²⁰.** Ch 8 §8.3.2 fixes $\Lambda_{\rm zone} = \hbar c/\eta_B \approx 0.152$ GeV (152 MeV) [CT-4.Λ Resolved 2026-05-15]. Ch 9 §9.0/§9.1 uses 0.152 GeV. Ch 10 §10.1 (key-symbol table), §10.6 (4.10.29 seesaw), §10.11 (OPEN 10.2 zone-cutoff statement), and §10.5/10.6 around the running Yukawa argument all use $\Lambda_{\rm zone} \sim 2 \times 10^{19}$ GeV (Planck scale). Ch 14 §14.1 likewise treats the framework as having a Planck-mass-scale UV physics from η_B via Eq. (4.14.1). These cannot both be right with the same η_B. The neutrino-seesaw result $m_\nu \sim v^2/M_R \sim 3$ meV depends on $M_R \sim 2\times 10^{19}$ GeV; with the corrected $\Lambda_{\rm zone} = 0.152$ GeV one gets $m_\nu \sim v^2/\Lambda_{\rm zone} \sim 4 \times 10^5$ GeV, off by 17 orders of magnitude. The neutrino-smallness "structural success" of §10.10 collapses if Ch 8 is the canonical value.

These two contradictions propagate through the bulk of Part III and the entire BSM chapter. Until they are reconciled, the numerical content of the volume cannot be trusted. Everything else in this review is conditional on those being fixed.

---

## Scope (what was reviewed)

All 14 chapter manuscripts (FINAL where present, DRAFT for Ch 1–3) read in full or to representative depth (≥ first third + key derivation sections + ledger tables). Appendix A read in full; Appendices B/C and Problem Sets verified as present. Cross-checks against Symbol_and_Constants.md and Vol 1 Ch 10 inheritance claims performed.

---

## Strengths

- **Ch 2** (Schrödinger derivation): the envelope ansatz + non-relativistic scale separation is genuinely well-executed. The seven-question scorecard in §2.1/§2.5.3 is the right discipline. Step-by-step algebra is line-checkable. Error estimate $\epsilon/E_0 \sim 10^{-5}$ is quantified. **Best chapter in the volume from a rigor standpoint.**
- **Ch 3** (Uncertainty): Cauchy–Schwarz proof is clean; the 6D-projection "shadow" argument in §3.5 is the kind of architectural story the framework was promising. Honest scope note on bounded-domain corrections.
- **Ch 7, Ch 8, Ch 9**: QED precision calculations (g-2 to one part in 10¹⁰, Lamb shift) and Casimir derivation are presented at textbook standard. Ch 8's regularization comparison (cutoff vs. dim-reg vs. Pauli–Villars) is competent. Ch 9's *new* Casimir presentation correctly drops the Planck-scale vacuum number — credit for fixing the cosmological-constant gap by 10⁸⁰ orders.
- **Ch 10**: I came in expecting hand-waving on the BLOCKER and found the opposite. §10.5 names Jackiw–Rossi by its precondition (independent spinor field assumed, not derived), explicitly labels every downstream result as conditional on Assumption 10.1, and §10.9's ledger does not cherry-pick. The leave-one-out diagnostic (4.10.35–36) is the right move. *This is the most intellectually honest chapter on a hard problem I have seen in a draft physics textbook.* Whether the underlying physics works is a separate question; the *epistemic posture* is right.
- **Ch 12** (QCD): the η-orbifold→Z₃→SU(3) derivation is clean and the single explicit O(1) match (α_s at M_Z) is named. RIGOROUS/APPROX/PHEN/OPEN labels per section.
- Rigor-label discipline (RIGOROUS / APPROXIMATE / PHENOMENOLOGICAL / OPEN) used consistently in Ch 10–14 — should be retrofitted to Ch 1–9.

---

## P0 — Must-fix before any further review

| Ch, loc | Concern | Finding | Fix |
|---|---|---|---|
| Ch 1 §1.3.2 Eq. (4.1.12) boxed; §1.4 box; §1.5 summary | C2 conflict | Boxed formula uses $(\eta_B/\xi_A)^2$; the same section's CT-4.β RESOLVED box says correct form is $(\xi_0/L_A)^{4/3}$ and β_residual = 1.000. The draft explicitly says the boxed formula "must be replaced." | Rewrite §1.3.2 and §1.4 to present *one* formula (the corrected one), move the (η_B/ξ_A)² version to a "Historical Note" if at all, and re-derive numerical sanity check inline. Update Problems 1.2, 1.3, 1.10. |
| Ch 2 §2.2.2 Eq. (1.10.19); Ch 3 §3.2.2 Eq. (1.10.19) | C3 cross-ref | Both chapters cite the *superseded* ℏ formula as the canonical inheritance from Vol 1 Ch 10 §10.3, with a partially-resolved correction box that doesn't change the equation actually used downstream. | Replace (1.10.19) with the CT-4.β-resolved form everywhere, OR mark the formula as a placeholder pending Vol 1 Ch 10 revision and *do not* claim ħ is reproduced. Cannot have it both ways. |
| Ch 8 §8.3.2 (Λ_zone = 0.152 GeV) vs. Ch 10 §10.1/§10.6/§10.11 and Ch 14 (Λ_zone ~ 2×10¹⁹ GeV / Planck) | C2 conflict, **arithmetic** | $\hbar c/\eta_B$ with $\eta_B = 1.3$ fm = 1.3×10⁻¹⁵ m is **0.152 GeV**, not 2×10¹⁹ GeV. The Planck-scale number requires η_B ≈ Planck length, which contradicts Vol 1 Ch 5. | Pick one and propagate. If Λ_zone = 0.152 GeV (Ch 8), the entire §10.6 seesaw collapses (predicts m_ν ~ 10⁵ GeV) and §10.10 success #3 is **wrong**. Either re-derive the seesaw with the correct Λ, or distinguish two cutoffs (KK-tower mass ≠ EFT cutoff) with explicit formulas. |
| Ch 10 §10.6 Eq. (4.10.29) | C2 conflict / dimensional sanity | $m_\nu \sim (246\,{\rm GeV})^2 / (2 \times 10^{19}\,{\rm GeV}) \sim 3$ meV uses a M_R that is inconsistent with Ch 8's Λ_zone. | Resolve with the Λ_zone fix above; if the seesaw scale is *different* from Λ_zone (it can be), say what physical scale it is and *derive* it. |
| Appendix A §A.2.6 entry (1.10.12): "ℏ = μcξ_A² (schematic)" | C2/C3 dimensional | $[\mu c \xi_A^2] = $ (kg/m³)(m/s)(m²) = kg/(m·s) — **not** J·s. Wrong dimensions, regardless of "schematic." It also contradicts Ch 1/2/3's actual formula. | Replace with the canonical (CT-4.β-resolved) form and cite it consistently. Appendix A is the reverse-index of truth; an orphan or wrong entry here pollutes every chapter that cites it. |
| Ch 5 §5.2 ξ_A = 1.4×10²⁶ m vs. Ch 1/2/3/14 ξ_A = 3×10²⁶ m | C2 conflict | Symbol_and_Constants.md / canonical zone-architecture value is 3×10²⁶ m (Waters Above beyond the Hubble radius). Ch 5 still uses Hubble radius. Multiple chapters have explanatory footnotes about the 1.4 vs. 3 distinction; Ch 5 has none. | Update Ch 5 §5.2 and propagate. |
| Ch 6 §6.6 + Ch 10 §10.5 | C2 (architectural) | Ch 6 explicitly says "the bosonic membrane does not produce fermionic operators" (Spin-1/2 BLOCKER), then Ch 7 §7.0 uses Dirac spinors and fermion propagators as a "placeholder," then Ch 10 §10.5 honestly says every mass result is conditional on Assumption 10.1 (an undefined primordial spinor field). The reader is told a "free fermion term" exists in $\mathcal{L}_0$ (Ch 7 Eq. 4.7.2) without it being defined or sourced. | Either (a) add a §10.5-style Assumption 10.1 box to the *front* of Ch 7 §7.0 so the placeholder is owned, not just mentioned in passing, or (b) clearly forward-reference the open problem and label every numerical g-2/Lamb-shift digit as conditional. Currently the volume claims "agreement to one part in 10¹⁰" on a derivation that begins with an undefined object. |

---

## P1 — Important physics gaps that weaken the case

| Ch, loc | Concern | Finding | Fix |
|---|---|---|---|
| Ch 1 §1.3.2 Eq. (4.1.13) | C1 derivation | The "bare quantum" computation gives $\hbar_{\rm bare} \approx 2.2\times 10^{45}$ J·s, then claims suppression by (η_B/ξ_A)² brings it to $\sim 1.9\times 10^{-37}$ J·s and that the residual factor must be ~480. The Derivation Status box admits this. The *resolved* form (ξ_0/L_A)^{4/3} is asserted to give β_residual = 1.000 — but the warp-factor integral that produces the 4/3 exponent is *not shown in the chapter*, only cited to research files. | Either show the 4/3 warp-integral in §1.4 (1–2 pages), or downgrade the claim from "fully explained" to "structurally correct, full derivation in research file BETA_GEOM_DERIVATION_CT4B.md." The chapter currently asserts both. |
| Ch 1 §1.0 last paragraph | C4 biblical | Frames the entire volume as deriving postulates from "the zone architecture established in Volumes 1–3" — fine — but the Genesis 1 framing only appears in epigraphs in this chapter, not in the architecture explanation itself. By Ch 1's standard ("biblical-first traceability"), the link from Genesis 1 zone architecture → Sturm–Liouville → quantization is named but not walked through. Compare to Ch 12 §12.0's epigraph use which is also decorative. | Add 1 paragraph in §1.1 or §1.2 explicitly anchoring "bounded extra dimensions ξ, η" to the Genesis 1 firmament/waters partition, with a citation to Vol 1 Ch 3 and Quality_Control/Reference/Biblical_References.md. |
| Ch 10 §10.3 Eq. (4.10.16)–(4.10.17) | C1 / arithmetic | Dimensionless eigenvalues ε₁ ≈ 0.11, ε₂ ≈ 0.44, ε₃ ≈ 0.91 quoted "from the test suite," but §10.12 admits *no automated test for this Sturm–Liouville problem yet exists*. The three-bound-state count is then claimed to be "robust over a factor-of-two variation in V₀ and η_B" — but the supporting calculation is not in the chapter. | Either include the numerical eigenvalue table inline (it's 1 page) or label §10.3 PHENOMENOLOGICAL pending the test in ACTION ITEM Ch10-T1. Currently labeled APPROXIMATE on the basis of a calculation the reader cannot check. |
| Ch 11 §11.3 Eq. (4.11.9)–(4.11.10) | C1 derivation | $\mu^2 = \beta \sigma c^2/\xi_A^2$. With σ ≈ 6×10⁹⁸ kg/s², c² = 9×10¹⁶ m²/s², ξ_A² = 9×10⁵² m²: $\mu^2 \sim 6 \times 10^{63}$ J²/something — dimensional check not shown, and the claim that this lands at (88 GeV)² with β ~ O(1) needs to be demonstrated, not stated. The Vol 2 Ch 9 hierarchy argument the chapter relies on is also in dispute (Ch 14 §14.1 admits |η_B| is "matched, not derived"). | Add the dimensional check explicitly. State the order-of-magnitude calculation in full. If β really is O(1), show the number. If it's a 16-orders-of-magnitude hand-wave on a knob called "β", that is what the §11.4 honesty box should say plainly. |
| Ch 4 §4.0 / §4.1.2 | C1 derivation | The claim "the framework predicts CHSH = 2√2" is repeated three times in the introduction, but the actual derivation (the rest of the chapter) was not read in this pass; the introduction's tone is celebratory in a way that smells of preview-before-proof. Recommend a colleague verify §4.3–§4.5 derives 2√2 from zone topology end-to-end and does not import the singlet state by hand. | Independent verification of §4.3–§4.5 needed; flagged for re-review. |
| Ch 5 §5.3.4 Eq. (4.5.27)–(4.5.29) | C1 derivation | $N_{\rm eff} \sim \rho_{\rm env} V_{\mathcal A}$ with $\rho_{\rm env} \sim \eta_B^{-3} \sim 10^{45}\,{\rm m}^{-3}$ for a pointer volume $V_{\mathcal A} \sim 10^{-9}\,{\rm m}^3$ → $N_{\rm eff} \sim 10^{36}$. The choice $\rho_{\rm env} \sim \eta_B^{-3}$ is asserted, not derived. | Cite Vol 1 Ch 6 explicitly for the Waters mode density, or down-grade the timescale estimate to "order-of-magnitude." |
| Ch 8 §8.3.2 Λ_zone arithmetic | C1 dimensional | The 0.152 GeV result is **correct arithmetic for $\hbar c/\eta_B$ with η_B = 1.3 fm**. Good. But this implies the membrane "thickness" is the nuclear scale, which makes Λ_zone *coincident* with Λ_QCD. The chapter notes this and calls it non-coincidental. It is also exactly the scale at which the renormalization story is supposed to begin to *fail* (perturbation theory breaks at Λ_QCD). The chapter should address whether this UV cutoff at the hadronic scale is consistent with successfully using QED perturbation theory all the way up to the electroweak scale in Ch 11. | Add a paragraph in §8.3 reconciling Λ_zone ≈ Λ_QCD with QED's success at scales ≪ Λ_zone, and explicitly address why electroweak observables at ~100 GeV (Ch 11) make sense with a 152 MeV UV cutoff. This is not obvious. |
| Ch 14 §14.2 Eq. (4.14.2)–(4.14.3) | C1 / numerical | Dark-matter candidate masses $M_{1,\eta} \approx 0.95$ GeV from $\hbar c \pi/|\eta_B|$ — uses the *correct* Ch 8 formula but produces a sub-GeV candidate where the chapter then asserts $\sigma_{\rm nucleon} \sim 10^{-44}$–$10^{-42}$ cm². Where does the cross section come from? Stated, not computed. | Either show the suppression-factor calculation or label PHENOMENOLOGICAL. |
| Ch 1 §1.7 Problem 1.2 | C2 internal | Problem instructs the student to compute ħ from a formula the chapter itself flags as superseded, with $\beta_{\rm geom} = 1.16$ which the same chapter says is wrong. | Rewrite Problem 1.2 with the corrected formula (or omit), or label it explicitly as "historical exercise — see §1.4 Derivation Status." |

---

## P2 — Hand-waving and missing error bars

| Ch, loc | Concern | Finding | Fix |
|---|---|---|---|
| Ch 7 §7.9 (g-2 result) | C1 error bars | Quotes "agreement at one part in 10¹⁰" without listing the theoretical uncertainty contributions (hadronic, electroweak, higher-loop). Standard practice is to give the theoretical-prediction error bar. | Add CODATA-style breakdown: a_e^th = a_e^QED + a_e^had + a_e^EW with uncertainties on each. |
| Ch 7 §7.0 | C2 / placeholder | "Until Ch 10, we will use the Dirac structure as a placeholder. This is not a cheat." It *is* a cheat unless the reader is told at every g-2 digit that the conditional on Assumption 10.1 applies. | Insert "conditional on Assumption 10.1 (§10.5)" at each precision quote in §7.9 and §7.10. |
| Ch 11 §11.0 last para "fits four observables from three inputs" | C1 / parameter-counting | The "three inputs" (g, g', v) actually rely on β, α (overlap), λ_A — three further O(1) fits buried in (4.11.10). Total parameter count is at least six, not three. | State the full parameter list once, in §11.0 or §11.4 honestly. |
| Ch 12 §12.0 | C2 internal | "Only one O(1) match in this chapter: α_s at M_Z" — but §12.3's string tension $\sigma_{\rm QCD} \approx (420\,{\rm MeV})^2$ is also matched, not derived from σ × η_B. | Acknowledge the second match or show the derivation. |
| Ch 5 Schrödinger's-cat timescale | C1 | Standard claim "10⁻²⁰ s decoherence" not shown in the excerpt I read but commonly inserted in such chapters — verify §5.4 cites the τ_D formula end-to-end before publishing. | Spot-check §5.4. |
| Ch 6 §6.6 (Bose–Einstein from canonical commutation) | C1 | Bose–Einstein is derived; the fermionic sector is honestly deferred. But the *partition function* in §6.6 (if cited from Vol 3 Ch 10) needs an explicit cross-reference, not "by stat mech." | Add equation number. |
| Ch 14 §14.6 research roadmap RR-9 (moduli stabilization for η_B) | C1 | The framework cannot yet predict why η_B has its value — admitted. Then Ch 11 §11.3 and Ch 12 §12.3 both treat η_B as a fixed input that "lands" the electroweak scale. The "lands" is a 16-orders-of-magnitude coincidence routed to a research roadmap item. | Acceptable for now; ensure the §14.5 falsification table notes that any change in η_B falsifies every chapter that uses it. |

---

## P3 — Style and minor

- Ch 1 §1.1 epigraphs are John 1 and Psalm 139; very heavy biblical framing for a chapter whose argument is mathematical. Consider whether the **Theologian** reviewer's tolerance is exceeded. (Outside Physicist scope but flagging.)
- Ch 8 §8.3.2 HISTORICAL NOTE box: well-written, retains the failed equation transparently. Good model for other CT-correction boxes. Apply the same style to Ch 1 §1.4 (which is currently more confusing than transparent).
- Ch 10 §10.6 muon residual quoted as both "15%" and "19%" within three paragraphs (§10.6 vs. §10.9 table). Pick one and use ranges consistently.
- Ch 11 Eq. (4.11.13): "2 × 88 / √0.129 ≈ 490 / 0.359" — 490/0.359 = 1365, not 246. Arithmetic transcription error; the *correct* computation is 2 × 88 / √0.129 = 176 / 0.359 = 490. Actually that gives 490, not 246. Re-check: $v = 2\mu/\sqrt\lambda = 2(88)/\sqrt{0.129} = 176/0.3592 \approx 490$ GeV, **not** 246.22 GeV. **This is a P1 arithmetic error, not P3** — moving to P1 list. Possibly a missing factor of 2 in the convention. Fix.

---

## Cross-reference audit (C3)

- Eq. (1.10.19) cited in Ch 2 §2.2.2, Ch 3 §3.2.2 — exists in Vol 1 Ch 10 inheritance but per CT-4.β note its form is being changed. Action: pin canonical equation number in Vol 1 *before* Vol 4 ships.
- Eq. (3.7.22) cited in Ch 2 §2.5.2 with note "*pending confirmation from Vol 3 Ch 7 finalization.*" — Vol 3 Ch 7 must be finalized before Ch 2 leaves draft.
- Eq. (2.5.4) brane Lagrangian cited from Vol 2 Ch 5 in Ch 6, Ch 7. Appendix A confirms (2.5.8) = Euler–Lagrange, but no (2.5.4) is listed. Audit Appendix A for missing entries.
- Eq. (4.6.55) (Ch 6 free-field Hamiltonian) cited in Ch 7 §7.1 — verify the equation number once Ch 6 is locked.
- Appendix A entry (1.10.12) is **dimensionally wrong** (see P0 row); the reverse index in §A.5 must be re-validated after the fix.
- Vol 2 Ch 9 hierarchy result cited in Ch 14 §14.1 as Eq. (4.14.1) but Appendix A lists no (2.9.*) entries. Add or remove the dependency.

---

## Biblical-derivation audit (C4)

The volume's claim is that QM and the Standard Model are *derived* from Genesis 1 zone architecture, not merely decorated with scripture. Per the Physicist's mandate, I check whether the derivation chain actually starts at the biblical-architecture axioms.

- **Ch 1**: explicitly claims the derivation begins with bounded extra dimensions (ξ_A, η_B) of the zone manifold (Vol 1 Ch 3). The bounded dimensions are tagged in Quality_Control/Reference/Zone_Architecture.md as the Waters Above / Waters Below from Genesis 1:6–7. The link is *named* (§1.4 mentions "Genesis 1's description of the waters above as beyond our sight") but not *derived* in this volume — that's Vol 1's job. **Accept conditionally.**
- **Ch 4** (entanglement via zone topology): the architecture justification rests on Vol 1 Ch 3's biblical-zone partition. The chapter does not re-justify it. **Accept.**
- **Ch 5** (decoherence via Waters): Waters Ψ_A, Ψ_B are introduced from Vol 1 Ch 6 as the perpendicular-dimension fields. Biblical anchor is implicit through Vol 1. **Accept.**
- **Ch 10–13**: Genesis 1 epigraphs but the actual derivations are entirely group-theoretic / topological. No claim is made that, e.g., SU(3) follows from Genesis 1:9 directly; it follows from a Z₃ orbifold whose biblical anchor is at Vol 2 Ch 4. This is the correct architecture: biblical → zone-manifold-axiom (Vol 1) → group-theoretic structure (Vol 2) → Standard Model (Vol 4). **No biblical hand-waving inserted as a derivation step.** Good.

**The Physicist's biblical-derivation finding: clean.** The volume does not invoke scripture as a physics premise; it invokes scripture as the source of the *axioms whose physics is then derived*. That is the right architecture. The only weakness is that Vol 4 must trust Vol 1's biblical-zone derivation, and if Vol 1 Ch 3 ever weakens its biblical anchoring, Vol 4 loses its foundation. (Outside this review's scope — flag for Vol 1 reviewers.)

---

## Internal-consistency audit (C2) — top conflicts already triaged above. Additional minor:

- Ch 4 §4.0 says "CHSH = 2√2 is **a prediction, not a fit**"; Ch 14 §14.5's falsification table should include CHSH > 2√2 (Tsirelson violation) as a falsifier — verify in §14.5.
- Ch 10's three-generation count claim ("not two, not four. Three") is repeated in Ch 13 §13.1 and Ch 14 §14.4 as a falsifier. Falsification thresholds across these three chapters appear consistent — good.

---

## Top 5 next actions (Physicist's priorities)

1. **Lock the ℏ formula.** Pick CT-4.β-resolved (ξ_0/L_A)^{4/3} or the legacy (η_B/ξ_A)², propagate one version through Ch 1, Ch 2, Ch 3, Appendix A, and the Ch 1 problem set. *Until this is one formula, the volume is not internally consistent.* Owner: lead author. Effort: 1 day.
2. **Lock Λ_zone.** Decide whether the EFT cutoff is 0.152 GeV (Ch 8/9 number) or the KK-tower scale ~2×10¹⁹ GeV that Ch 10/14 use. They are *different physical objects* and should have different names. Rename Ch 10's quantity (e.g., $M_{KK}^{\rm max}$) and re-validate every numerical claim that used the conflated name. Critical for the neutrino-mass "structural success" in §10.10. Owner: lead author + Ch 8/Ch 10 reviewer. Effort: 2 days.
3. **Fix Appendix A (1.10.12)** dimensionally and pin it to the CT-4.β-resolved formula. Without this, the reverse-index of truth is broken. Owner: Appendix A maintainer. Effort: 1 hour for the dimensional fix; 1 day to audit every Ch citation to (1.10.12).
4. **Move the Ch 7 spinor placeholder admission to §7.0 as a boxed Assumption.** Currently the entire QED-precision testimony rests on an object whose existence is admitted as OPEN only in Ch 10 §10.5. The g-2 chapter should not lead with confidence and end without naming the conditional. Owner: Ch 7 author. Effort: 0.5 day.
5. **Recompute v in Ch 11 §11.3 Eq. (4.11.13).** $v = 2\mu/\sqrt\lambda$ with the values given (88, 0.129) is 490 GeV, not 246.22 GeV. Either the convention (factor of 2 / √2) is mishandled, or the numerical inputs μ ≈ 88 GeV and λ ≈ 0.129 are off. Until the electroweak VEV computation closes arithmetically, every Ch 11 mass prediction is suspect. Owner: Ch 11 author. Effort: 1 hour to identify, 0.5 day to propagate.

---

*Total volume status: not ready for publication. The structural ambition is high and the honesty is unusually good for a draft of this size; the arithmetic and cross-volume bookkeeping are not yet at the standard the framework's own §1.6 "Promises" demand. Address P0 and the five next-actions above; come back for re-review.*

— REVIEWER-01 (The Physicist), 2026-05-16
