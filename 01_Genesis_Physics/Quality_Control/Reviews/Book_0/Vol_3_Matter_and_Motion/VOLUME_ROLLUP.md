# Volume Rollup — Book 0 Vol 3: Matter and Motion

**Date:** 2026-05-16
**Scope:** Aggregate of 12 reviewer reports (REVIEWER_01 through REVIEWER_12) on the 12-chapter manuscript of *Matter and Motion* and its Back_Matter.
**Concern tags (Jeff's 7 concerns, mapped):** C1 biblical-first traceability • C2 cross-book continuity • C3 no unanswered "but why" • C4 self-consistency / derivation honesty / NYT-craft / publisher-readiness (where reviewers' local C-tags differ, attributions note their reviewer-internal usage).

---

## 1. Aggregate Verdict and Per-Reviewer Table

**Aggregate verdict: PASS WITH NOTES — conditional.** 10 of 12 reviewers issue PASS or PASS WITH NOTES; 2 issue FAIL (Style Editor on auto-FAIL Red Flags; Biblical Traceability on Ch 1 orphan; Acquisitions issues a *conditional* production FAIL on missing front matter/figures/index). None of the FAILs are content-rewrite failures — all are surgical or production-sprint items. The volume is the strongest Foundations volume audited to date for derivation honesty (R-01, R-02, R-04, R-10) and graduate-textbook voice (R-03, R-07). The classical-mechanics half (Ch 1–4) is biblically unanchored at the chapter surface (R-11); the field/thermo half (Ch 5–12) is well-anchored. Two real algebraic/numerical defects survive (R-01 P0s in Ch 1 and Ch 9); one likely third (Ch 7 Eq. 3.7.10 unit chain) needs confirmation.

| # | Reviewer | Verdict | Headline |
|---|----------|---------|----------|
| 01 | The Physicist | PASS WITH NOTES | Strongest derivation-honesty doc yet; two local P0s in Ch 1 and Ch 9 |
| 02 | The "But Why?" Reader | PASS WITH NOTES | No P0s; one literal "it can be shown" in Ch 12 §12.1 (auto-FAIL trigger) needs fix |
| 03 | The Writing Coach | PASS WITH NOTES | Voice consistent; chapter-opening formula repeats 12× |
| 04 | The Consistency Auditor | PASS WITH NOTES | One zone-misnaming (Ch 5 line 306); σ-units drift inherited from Vol 1 |
| 05 | The Homeschool Mom | PASS | Wrong-audience but trustworthy foundation; reverent without preaching |
| 06 | The Skeptic | PASS WITH NOTES (conditional) | Calibration-vs-prediction in Ch 7; "convenient God" δE_κ in Ch 9 |
| 07 | The Student | PASS WITH NOTES | Two stream-of-consciousness leaks (Ch 1 lines 257, 485; Ch 6 line 464) |
| 08 | The Style Editor | **FAIL** | Auto-FAIL Red Flags: "the membrane" used alone ≥10×; Hebrew first-mention malformed in Ch 5 line 17 |
| 09 | The Theologian | PASS WITH NOTES | One C1 ("This is not theology" sentence Ch 12 §12.4); Acts 10:34 misused in Ch 4 |
| 10 | The Navigator | PASS WITH NOTES | Ch 7 forward-only ref to draftless Vol 6 Ch 14; Ch 12 voice incursion |
| 11 | Biblical Traceability | **FAIL** | Ch 1 (headline F=ma claim) has zero biblical anchor in body; Ch 2/3/4/10 silently inherit |
| 12 | Acquisitions / Production | **FAIL** (conditional) | No front matter, no index, no rendered figures, no metadata; content largely ships |

**Disagreements flagged:**
- R-05 (Homeschool Mom) and R-09 (Theologian) read Vol 3's Christological reticence as appropriate for genre; R-11 reads it as a structural orphan on Ch 1. *Resolution:* both correct — R-05/R-09 evaluate tone, R-11 evaluates traceability metadata. Fix R-11's Ch 1 anchor without changing tone.
- R-01 (Physicist) treats Ch 7 §7.3 Parameter Disclosure as a strength; R-06 (Skeptic) treats it as inadequate because §7.0 still advertises "<1% accuracy." *Both right.* Fix the headline language (R-06) while preserving the disclosure (R-01).
- R-04 (Consistency Auditor) marks "the membrane" usage acceptable when locally bound; R-08 (Style Editor) marks every standalone use as auto-FAIL. *R-08 governs* (Style Bible explicit).
- R-08 places equation-tag scheme as PASS; R-12 calls inconsistent equation-tag scheme a C1 production blocker. *Resolution:* R-12 owns the typesetter-autolink concern; sweep at copyedit.

---

## 2. Top 5 P0 Blockers (Deduped, with Attributions)

| # | Blocker | Attribution | Action |
|---|---------|-------------|--------|
| **P0-1** | **Stream-of-consciousness debugging fragments in published draft** — Ch 1 lines 257 ("Wait, I need to be more careful…") and 485 ("Hmm, I'm overcomplicating this…"); Ch 6 line 464 ("Wait, that does not work…"). Two abandoned derivation attempts left in text. | R-01 (P0-1), R-02 (F-08), R-06 (V11), R-07 (#1, #2), R-12 (implied via verified-status gap) | Delete lines 222–258 and 446–486 of Ch01_DRAFT.md; rewrite Ch06_DRAFT.md from line 464 onward. Ch 1's own SELF_REVIEW already prescribed this; execute. |
| **P0-2** | **Algebraically wrong fluctuation estimate in Ch 9** — Eqs. 3.9.11–3.9.12 have a dimensionally incoherent $\sqrt{k_BT^2\sqrt N}$ and assert $\Delta U/U \sim 10^{-10^{11.5}}$ (a number with $10^{11.5}$ digits — physical nonsense; correct value $\sim 3\times 10^{-12}$). | R-01 (P0-2) | Replace with $\Delta U \sim k_BT\sqrt N$ and $\Delta U/U \sim 1/\sqrt N \approx 3\times 10^{-12}$. One paragraph rewrite. |
| **P0-3** | **Ch 7 Eq. 3.7.10 unit chain off by ~10³** — $\hbar c \pi/\eta_B$ with $\eta_B = 1.3$ fm computes to ~477 MeV, not the claimed 430 GeV. Either $\eta_B$ is misquoted, or the "natural electroweak scale" claim collapses. R-01 calls this *potentially the most consequential finding in the review.* | R-01 (P1-4, "promote to P0 if confirmed"), R-06 (V1, V5 cluster, S5), R-11 (background) | Recompute explicitly. If confirmed, this propagates into the headline §7.0 claim and the Higgs-derivation chain. |
| **P0-4** | **Style auto-FAIL Red Flags** — (a) "the membrane" used as bare noun in ≥10 distinct passages across Ch 1/5/7/8/9/10/11/12; (b) "brane" used standalone in Ch01_SPEC line 37 and Ch01_DRAFT line 1229; (c) Ch 5 line 17 Hebrew first-mention malformed ("firmament" lowercase, missing Hebrew letters, no diacriticals, missing apostrophe on *raqia'*). Series Bible explicit auto-FAIL. | R-08 (full §3, §4) | Global search-and-replace pass: "the membrane" → "the Firmament" or "the Firmament membrane"; remove "brane" as standalone; rewrite Ch 5 line 17 to "the Firmament (רָקִיעַ, *raqia'*, 'stretched-out thing')". |
| **P0-5** | **Ch 1 carries the volume's headline claim (F=ma as theorem) with zero biblical anchor in chapter body** — no verse, no Hebrew, no Gen 1 reference; chain terminates at "Vol 1 Ch 3 axioms," not at Scripture. Ch 2/3/4 silently inherit. Ch 10 invokes "Edenic"/"Phase 2" as labels without anchor. | R-11 (P0; FAIL driver), R-05 (C2-2 adjacent), R-09 (C3-01 adjacent) | Add 1–3 paragraphs to Ch 1 §1.1 or §1.5 chaining test-particle action ← Firmament-as-*raqia'* ← Gen 1:6–7. Add one-sentence back-references in Ch 2, 3, 4, 10. Effort < 1 afternoon. |

**Honorable mentions (sub-P0, near-P0):**
- Ch 12 §12.4 "This is not theology. This is thermodynamics" — R-09 promotes to C1 (category error: three of four κ-transitions are imported theological boundary conditions). Fix: "not *merely* theology" or delete.
- Ch 6 §6.5 "DERIVATION STATUS — BLOCKED" (Jackiw-Rossi → Dirac spinor circularity) is then used downstream by Ch 7 §7.4 fermion-mass spectrum (R-06 V2, R-01 audit). Either resolve OP-1 or demote headline language.
- Ch 9 §9.3.2 δE_κ "sustaining energy input from Zone 0 (the Godhead)" inside a stated First Law — R-06 V3 "convenient God" pattern; R-09 reads as theologically sound providence claim. *Disagreement.* Resolution: provide operational definition of κ (R-06) or move δE_κ out of the conservation-law statement into a clearly labelled open-system extension.

---

## 3. P1 Critical (12 items)

| # | Item | Attribution |
|---|------|-------------|
| P1-1 | Ch 9 duplicate equation number (3.9.13) for transitivity and equipartition; (3.9.13a/b) clash | R-01 P1-1 |
| P1-2 | Ch 7 §7.0 advertises "<1% accuracy for gauge bosons" while §7.3 Parameter Disclosure concedes v is calibrated — headline contradicts disclosure | R-06 V1, R-01 P1-3, R-07 #6, R-02 F-02 |
| P1-3 | Ch 7 has two independent fitted α parameters using same symbol (α_membrane vs α_hierarchy); chapter never notes both are free | R-01 P1-3, R-06 V12, R-02 F-02 |
| P1-4 | Ch 12 §12.1 Shannon-functional-equation step: "By carefully manipulating … one can show" — literal "it can be shown that" trigger for auto-FAIL on But-Why persona | R-02 F-07 (single clearest missing why) |
| P1-5 | Ch 4 epigraph (Job 26:10) decorative; Ch 4 §4.1 line 14 Acts 10:34 ("does not show favoritism") used to motivate SO(3) Killing vectors — category leap *and* NIV instead of ESV | R-09 C2-01, C2-02 |
| P1-6 | Ch 11 §11.0 stale "Ch 5 in preparation" note — Ch 5 is in fact drafted, the note is now misleading | R-02 F-04, R-07 #8 |
| P1-7 | Ch 5 line 306 "Waters Above field Ψ_A lives in Zone 2.1" — canonical sources put Ψ_A at Zone 2.2.3; Z₂.₁ is the atemporal Spirit-realm domain | R-04 Finding 1 |
| P1-8 | σ-units drift in Ch 7 lines 21 and 158 ("kg/s²" vs canonical "kg/(m·s²)") — inherited from Vol 1 but appears in Vol 3 | R-04 Finding 2 |
| P1-9 | Ch 7 forward-only load-bearing dependency on Vol 6 Ch 14 (draftless) for spin-1/2 derivation (OP-1); fermion mass spectrum hangs on it | R-10 #26, R-06 V2/V10, R-01 audit |
| P1-10 | Ch 12 §"Connection to the Novel Series" injects pastoral register ("the universe itself cries out for a savior") into Foundations voice; also "Book 1" naming collision (means novel series, reads as physics flagship) | R-10 #32, C3-D; R-03 (voice); R-09 implicitly (no preaching) |
| P1-11 | Ch 5 cosmology-bridge table misroutes to Vol 5 Ch 3 (Grav Waves) and Vol 5 Ch 7 (Singularity Resolution) — should target Vol 5 Ch 8/10/11 | R-10 #21, #22 |
| P1-12 | Ch 6 §6.2 unresolved dimensional-check parenthetical ("60–160% uncertainty band" on a 1.9 GeV claim) left in text | R-06 V5 |

---

## 4. P2 / P3 Summary

**P2 (polish, ~12 items consolidated):**
- Ch 1 §1.4 line 359 stray-index algebra step (R-01 P2-1, R-07 #4); Ch 1 §1.5 sign-flip in Γ derivation (R-01 P2-3).
- Ch 7 §7.4 $n^2$ scaling justified by Gaussian overlap not Fourier decay (R-01 P2-2, R-02 F-13).
- Ch 9 §9.3.4 per-mole vs per-particle conventions mixed (R-01 P2-4); Ch 12 §12.4 Eq. 3.12.22 dimensional error in $\dot E_S = \kappa V$ (R-01 P2-6).
- Ch 8 §8.1 Lennard-Jones $r^{-6}$ claim "from membrane Green's function" needs softening or supplied derivation (R-01 P2-5, R-02 F-14).
- Ch 6 §6.0 / Ch 12 §12.6 sermon-voice intrusions (R-02 F-18, F-19; R-03 §10).
- Roadmap-opening formula repeats 12×; diversify Ch 6 and Ch 9 openings (R-03 §4).
- Ch 1 §1.1 cut 40% (R-03, R-07); add forward-pointing closing sentences to half-dozen chapters (R-03 §5); add §12.10 "Looking Forward" closing volume's arc (R-03 §5).
- Ch 10 invoke "Edenic" without anchor (R-11 §3.3); Ch 11 invoke Degradation Principle without naming the Fall (R-11 §3.4).
- Theological cleanups: Ch 12 §12.5 "no death" qualification (R-09 C2-03); Gen 3:19 cross-cite Romans 5:12 (R-09 C2-04); Matt 24:36 placement (R-09 C2-05); Zone 1 ≠ "God's Presence" flat identification (R-09 C3-04).
- Ch 8/9/10/11/12 add Waters Above/Below pairing on first-section uses of "dark energy"/"dark matter" (R-08 §5).
- Italicize *tohu vavohu* / standardize hyphenation (R-04 F5, R-09 C3-03).

**P3 (nits, ~10 items):**
- Roadmap figures (3.X.1) are placeholder text in all 12 chapters; need rendered art (R-01 P3-1, R-07 #10, R-12 C1-3).
- Equation-tag scheme: mix of `\tag{}` and `\text{(Eq. ...)}` (R-03 §8, R-12 C1-4).
- "Recall from Vol 1 Ch N…" repeated ~50× across volume; vary phrasing (R-03 §8).
- Em-dash density / spacing inconsistency (R-03 §8, R-08 §8).
- Front-matter notation note ($\mathcal{S}$ entropy vs $S$ action) (R-07 #13).
- DOIs to bibliography, Problem 11.1 Chapman-Enskog footnote, App A reverse-index transitional, software/trademark sweep (R-12 C4).
- Remove `Ch09_DRAFT.md.bak` from repo (R-08 §10, R-12 C2-7).
- Subsection heading Title Case vs sentence case — decide and apply (R-08 §8).

---

## 5. Findings by Concern (C1 / C2 / C3 / C4)

### C1 — Biblical-first traceability

**Status: FAIL → PASS WITH NOTES achievable in one afternoon.**
- Ch 1 carries the volume's headline claim with zero biblical anchor in body (R-11 P0). Ch 2, 3, 4 silently inherit. Ch 10 uses "Edenic"/"Phase 2" as labels with no in-chapter verse.
- Ch 5, 6, 7, 8, 9, 12 are **load-bearing anchored** — *mayim* in Ch 5, *raqia'* in Ch 6 and Ch 7, Gen 1:9 in Ch 8, Gen 2:1–3 and Gen 3:17–19 in Ch 9 and Ch 12. Ch 5 §5.1 and Ch 12 §12.5 are the templates the rest of the volume should be calibrated against (R-11 §5).
- No decorative-verse retrofits detected (R-11 §4). Failure is omission, not retrofit.
- Christological thread absent across Vol 3 (R-09 C3-01) — acceptable for genre but flag for series coherence; one paragraph nodding to Christ-as-Sustainer (Col 1:17 / Heb 1:3) in Ch 9 intro or front matter recommended.
- Appendix A has zero biblical entries (R-11 §3.5); add §A.5 "Biblical Anchors Used Across Vol 3" mapping table.

### C2 — Cross-book continuity / self-consistency

**Status: PASS WITH NOTES.**
- 27 of 33 external cross-references resolve cleanly (R-10 audit); 4 cleanups, 2 stale Vol 5 pointers, 1 forward-only blocker (Vol 6 Ch 14).
- Vol 1 / Vol 2 equation citations checked end-to-end (R-01 §4, R-04 Finding 8, R-10 table): Vol 1 Eq. 1.5.28, 1.6.13, 1.7.17, 1.7.31, 1.7.33, 1.8.3, 1.11.34–35, Vol 2 Eq. 2.2.29, 2.3.18, 2.5.20, 2.6.32 all resolve.
- σ-units drift (kg/(m·s²) vs kg/s²) inherited from Vol 1 (R-04 Finding 2, OS-1) — Vol 3 fix is two lines in Ch 7; upstream Vol 1 Ch 5 fix filed as out-of-scope.
- Glossary vs Zone_Architecture canonical-source disagreement on whether Firmament = Z₂.₂ or Z₂.₂.₂ (R-04 Finding 12, OS-2) — reconcile before next audit.
- Vol 1 Ch 11 filename non-standard (`Ch11_Thermodynamics_from_Zone_Separation.md`) (R-10 §C3-E).

### C3 — No unanswered "but why"

**Status: PASS WITH NOTES.**
- Every chapter opens with a "why" question before formalism (R-02 §2 S1–S10, R-07 §"What Worked Brilliantly"). Best-in-series for why-first discipline.
- Chain-of-why traced from Higgs mass prediction (Eq. 3.7.44) all the way back to Vol 1 / Vol 2 — UNBROKEN with one honestly-flagged fitted α (R-02 §6).
- One literal "it can be shown" trigger (R-02 F-07, Ch 12 §12.1 Shannon).
- α membrane coupling (Ch 7 §7.2) and α hierarchy parameter (Ch 7 §7.4) are both fit-then-applied; chapter is honest in pieces but does not consolidate (R-01 P1-3, R-02 F-01/F-02, R-06 V1/V12).
- Ch 7 §7.1 η_B "set independently by nuclear physics" — provenance not in chapter; circularity risk if η_B was selected to produce electroweak-scale (R-02 F-03, R-06 S5).
- Boundary-condition convention reconciliation needed between Ch 6 (periodic η) and Ch 7 (Dirichlet ξ) (R-02 F-05).

### C4 — Derivation honesty / consistency / craft / production readiness

**Status: Mixed — content honesty PASS WITH NOTES; production readiness FAIL (conditional).**
- Two real algebraic defects (Ch 1 stream-of-consciousness, Ch 9 fluctuation arithmetic) plus one likely numerical error (Ch 7 Eq. 3.7.10 unit chain) are local accidents, not systemic.
- Style auto-FAIL: "the membrane" used alone, "brane" standalone, Hebrew first-mention malformed (R-08).
- Voice consistency excellent (R-03 §2); roadmap-opening formula repeats 12×; ~half the chapters end mechanically.
- Production blockers: no front matter, no index, no rendered figures, no metadata sheet, no ISBN/BISAC, scripture translation undeclared, equation-tag scheme inconsistent (R-12 C1-1 through C1-6).
- Ch 5/7/9/10/11 are DRAFT but not VERIFIED in QUALITY_GATE (R-12 C2-5).
- Honesty-about-limits notes (Ch 7 §7.3 Parameter Disclosure, Ch 6 §6.5 Derivation Status, Ch 7 §7.4 OP-1 footnote, Ch 12 research-status note) are praised by R-01, R-06, R-07 — *preserve these; do not soften.*

---

## 6. Strengths (Preserve and Propagate)

- **Ch 1 derivation of F=ma from the test-particle action with explicit "What We Derived / What We Postulated" ledger** — R-01 S1, R-02 S2, R-06 S1, R-07 §"What Worked Brilliantly" #2. Gold-standard derivation-honesty move.
- **Ch 5 §5.0 *mayim* paragraph and Madelung transform** — R-01 S5, R-02 S10, R-03 C4, R-11 §5 (template), R-05 C1-2.
- **Ch 6 Chladni-plate opening and Gen 1:9 anchor** — R-03 C4, R-11 §5, R-05 C1-2.
- **Ch 7 §7.3 Parameter Disclosure box** — R-01 S2 (single most important honesty move; "keep this box, do not soften it").
- **Ch 9 §9.4 thermodynamic potentials with Maxwell relations traced to Vol 1 Ch 11** — R-01 S3.
- **Ch 9 §9.1 alien-civilization thought experiment** — R-02 S6.
- **Ch 11 §11.1.2 explicit time-reversal-paradox warning before molecular chaos** — R-02 S8.
- **Ch 12 §12.0 opening** ("You have lived your entire life moving forward through time") — R-03 C4 (high-water mark of volume's craft).
- **Ch 12's five Gen 1–3 anchors over four-epoch architecture** — R-11 §5, R-09 §"What Vol 3 Gets Right".
- **Appendix A reverse equation index** — R-12 ("kind of thing most textbooks promise and never deliver").
- **Problem-set typology** (computational / conceptual / challenge) hitting 30% "explain why" tier — R-07 §"What Worked Brilliantly" #5.
- **"What You Already Know" boxes at start of Ch 11** — propagate to every chapter (R-07 #4).

---

## 7. Cross-References to Other Units

- **Vol 1 Ch 5** (membrane / Firmament / σ): σ-units drift across lines 485, 727, 759, 767 — file OS-1 (R-04). Vol 3 Ch 7 inherits.
- **Vol 1 Ch 11** filename non-standard (`Ch11_Thermodynamics_from_Zone_Separation.md` instead of `Ch11_DRAFT.md`); cross-volume scripts may miss it (R-10 §C3-E).
- **Vol 2 Ch 6** (SM gauge group): Vol 3 Ch 7 cites g=0.652, g'=0.357, sin²θ_W=0.2312 — verify against Vol 2 Eq. 2.6.46–49 (R-01 §4).
- **Vol 4 App A** (α derivation): Vol 3 Ch 7 currently depends on this for headline gauge-boson "<1%" claim (R-06 condition (i)).
- **Vol 5 Ch 8 / Ch 10 / Ch 11** (cosmology bridge): Vol 3 Ch 5 currently misroutes to Vol 5 Ch 3 and Ch 7 (R-10 #21, #22).
- **Vol 6 Ch 14** (Open Problems, OP-1 spin-1/2): draftless; Vol 3 Ch 7 load-bears on it (R-10 #26, R-06 V2).
- **`Research/Foundations/TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md` + GitHub Issue #1**: canonical research-gap location for OP-1; Vol 3 Ch 7 should cite this directly (R-10 recommendation 1).
- **`Reference/Glossary.md` vs `Reference/Zone_Architecture.md`**: disagree on Firmament = Z₂.₂ vs Z₂.₂.₂; root cause of Vol 3 Ch 5 line 306 (R-04 Finding 12, OS-2).
- **Book 1 *Hidden Architecture* and pillar 2 novel series**: Ch 12 "Book 1" reference collides with new naming convention (R-10 #32).
- **Book 3 Family Edition**: Ch 1 §1.1, Ch 6 §6.0, Ch 12 §12.0 openings can be lifted verbatim as "What the grown-ups are reading" sidebars (R-05 §C4 action item 3); Vol 3 Ch 7/Ch 8 will need biblical wrapper supplied downstream (R-05 C2-1).

---

## 8. Top 10 Next Actions (Prioritized)

1. **Strip stream-of-consciousness from Ch 1 lines 222–258 and 446–486; rewrite Ch 6 from line 464.** (P0-1; R-01, R-02, R-06, R-07.) ~1 hour.
2. **Rewrite Ch 9 Eqs. 3.9.11–3.9.12** with correct $\Delta U \sim k_BT\sqrt N$ and $\Delta U/U \approx 3\times 10^{-12}$. (P0-2; R-01.) ~30 min.
3. **Recompute Ch 7 Eq. 3.7.10** unit chain; either confirm 430 GeV with corrected $\eta_B$ or flag the "natural electroweak scale" claim. (P0-3; R-01 P1-4 promoted.) ~1 hour; potentially propagates to §7.0 headline.
4. **Global style sweep**: replace standalone "the membrane" with "the Firmament" / "the Firmament membrane" across Ch 1/5/7/8/9/10/11/12; remove "brane" standalone; rewrite Ch 5 line 17 Hebrew first-mention to canonical form. (P0-4; R-08.) ~2 hours.
5. **Add Ch 1 biblical anchor** (1–3 paragraphs in §1.1 or §1.5 chaining test-particle action ← Firmament-as-*raqia'* ← Gen 1:6–7); add one-sentence back-references in Ch 2/3/4/10. (P0-5; R-11.) ~1 afternoon. Add §A.5 "Biblical Anchors Used Across Vol 3" to Appendix A.
6. **Fix Ch 7 headline language and α disambiguation**: rewrite §7.0 to lead with "given the calibrated VEV"; introduce α_σ vs α_hier symbols; consolidate Parameter Disclosure into §7.6 listing both fitted parameters. (P1-2, P1-3; R-01, R-02, R-06.) ~2 hours.
7. **Fix Ch 12 §12.4 "this is not theology" sentence** ("not *merely* theology") and excise Ch 12 §"Connection to the Novel Series" pastoral paragraphs / disambiguate "Book 1" naming collision. (R-09 C1-01, R-10 #32 C3-D.) ~30 min.
8. **Fix Ch 5 line 306 zone misnaming** (Zone 2.1 → Zone 2.2.3); fix Ch 7 σ-units (kg/s² → kg/(m·s²)); fix Ch 11 stale "Ch 5 in preparation" note; re-target Ch 5 cosmology-bridge table to Vol 5 Ch 8/10/11; resolve Ch 6 §6.2 dimensional-check parenthetical (don't publish with the flag). (P1-6, P1-7, P1-8, P1-11, P1-12; R-04, R-02, R-10, R-06.) ~2 hours.
9. **Ch 7 OP-1 redirect**: replace Vol 6 Ch 14 forward pointer with citation to `Research/Foundations/TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md` + GitHub Issue #1; add §7.0 conditionality statement for fermion-mass spectrum. (P1-9; R-10 #26, R-06 V10.) ~30 min.
10. **Production sprint (60-day)**: front matter (title page, copyright, TOC, list of figures, preface, "About this Series," "Honest Limits of Volume 3," abbreviated symbol/notation reference, author bio); commission ~25–40 figures from existing `[FIGURE: ...]` callouts; draft index; normalize equation-tag scheme; metadata sheet (BISAC/ISBN/keywords/jacket copy); declare scripture translation (ESV recommended) and file permissions if needed; verify Ch 5/7/9/10/11 through reviewer agents. (R-12 C1-1 through C1-6 plus C2-1, C2-2, C2-3, C2-6, C2-8.)

**Order-of-effort sanity check:** Actions 1–9 are content fixes totaling ~1–1.5 working days. Action 10 is the 60-day production sprint and is independent of content. Volume can be locked from a content standpoint within the week; the book-as-object follows on the publisher's standard timeline.

---

*End of Volume Rollup — Book 0 Vol 3: Matter and Motion.*
*Word count: ~2,650.*
