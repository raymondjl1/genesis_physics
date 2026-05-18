# FIX LOG — Volume 6: Predictions and Simulations
**Revision date:** 2026-05-14
**Based on:** REVIEW_REPORT_Vol6.md (reviewers R01–R18)
**Editor:** Claude Sonnet 4.6 (automated editorial session)

Each line gives: Chapter | Section | Change | Reason

---

## VOLUME-LEVEL ADDITIONS

| Item | Change | Reason |
|---|---|---|
| VOLUME_PREFACE.md | CREATED — defines Part A (Chs 1–8, core validated physics), Part B (Chs 9–13, conditional engineering), Part C (Chs 14–17, self-assessment); explains epistemic tier structure | Reviewers R03, R07, R11 flagged absence of volume-level epistemic framing; readers need to know which chapters are established physics vs. engineering projections vs. self-assessment |

---

## CHAPTER 1 — Predictions That Match Observation

| Section | Change | Reason |
|---|---|---|
| After test suite summary table | Added prediction type taxonomy note: Type A (retroactive fit), Type B (structural prediction without tuning), Type C (novel, untested); identified which headline results fall in which tier | R01, R05: test suite table aggregated all predictions without distinguishing retrofits from genuine predictions; critical for reader assessment of evidential strength |

---

## CHAPTER 2 — Predictions That Differ

| Section | Change | Reason |
|---|---|---|
| §2.1 / chapter intro | Added note flagging the particle mass spectrum discrepancy (u quark ~370× error, d quark ~31,000× error) as "the framework's most significant open failure" | R02, R14: mass discrepancies understated; stated as "work in progress" without quantifying the scale of the error |
| §2.2 end | Added RT-6.MASS2D designation at end of "path forward" paragraph | R14: mass spectrum section does not identify the specific computational task needed; links section to the 2D eigenvalue task |

---

## CHAPTER 3 — Novel Predictions

| Section | Change | Reason |
|---|---|---|
| Before §3.7 | Added "Part B — Conditional Engineering" blockquote with standard text | R11: Part B framing absent from Chapter 3 despite content being conditional on framework validity |

---

## CHAPTER 4 — Falsification Criteria

No edits. Chapter 4 is structurally sound per the review report; falsification content is appropriately presented.

---

## CHAPTER 5 — Simulation Methodology

| Section | Change | Reason |
|---|---|---|
| §5.2 start | Added ⚠ METHODOLOGICAL NOTE about explicit Euler integrator being non-symplectic, producing ~12% artifact in Chapter 6 power spectrum; states corrected result (0.02%), designates RT-6.INT | R04, R08: methodology chapter does not warn readers about the known integrator artifact before they encounter the Ch06 results; presents a false sense of numerical validity |

---

## CHAPTER 6 — N-Body Simulations (Structure Formation)

| Item | Change | Reason |
|---|---|---|
| Chapter title | Changed from "N-Body Simulations with Zone Corrections" to "Structure Formation via Linear Perturbation Theory (and Preliminary N-Body Results)" | R04, R08: title misrepresents the chapter's primary method; the chapter's headline result comes from linear perturbation theory, not converged N-body simulation |
| Chapter Note / Result Correction | Replaced internal editorial note (2026-05-11) with explicit RESULT CORRECTION block: 12% figure is Euler integrator artifact; converged result = 0.02%; headline corrected to "Zone architecture predicts 0.02% suppression of the matter power spectrum, currently observationally indistinguishable from ΛCDM" | CRITICAL BLOCKER (R04, R08): presenting 12% as the framework's prediction when the converged result is 0.02% is a factual error; the corrected headline is more honest and more accurate |

---

## CHAPTER 7 — Membrane Vibration Spectra

| Section | Change | Reason |
|---|---|---|
| After "lightest predicted mode is 930 times heavier" | Added explicit blockquote: "The fundamental membrane mode predicts 475.5 MeV/c²; the observed electron mass is 0.511 MeV/c²; discrepancy 930×; Research Task RT-6.MASS2D" | R02, R14: the 930× discrepancy is stated then minimized; needs prominent callout so readers cannot miss it |
| After Mode 2 / proton 1.4% agreement | Added note: "Mode 2 assignment to the proton requires explaining why mode 1 is not observed; a selection rule from zone boundary conditions must be derived — RT-6.SEL; without RT-6.SEL, the Mode 2/proton identification is a numerical coincidence rather than a prediction" | R14: 1.4% agreement for Mode 2/proton presented as success without noting the Mode 1 problem; selection rule needed for the assignment to be physically meaningful |

---

## CHAPTER 8 — Reproducibility Package

| Section | Change | Reason |
|---|---|---|
| §8.8.3 end / new §8.8.4 | Added "Reproducibility Requirements (Rev. 2026-05-14)" section listing: (1) requirements.txt — Status: PENDING RT-6.REP; (2) Docker/Conda environment — Status: PENDING RT-6.REP; (3) Numerical validation thresholds — Status: PARTIAL; (4) Seed documentation — Status: PARTIAL; closes with contact instruction until items 1–2 are complete | R03, R08: §8.8 describes the packaging gap in prose but does not give machine-readable status per requirement; reviewers need explicit PENDING/PARTIAL labels to evaluate completeness for publication |

---

## CHAPTER 9 — FTL Travel

| Section | Change | Reason |
|---|---|---|
| Chapter header | Added "Part B — Conditional Engineering" blockquote | Volume epistemic tier framing; consistent with all Part B chapters |
| §9.6.7 (empirical hints) | Removed "anomalous correlations in psi experiments" from empirical hints list; replaced with: "No confirmed empirical support for consciousness-zone coupling currently exists; the hypothesis remains speculative" | CRITICAL BLOCKER (R06, R10, R15): psi experiment citation is scientifically indefensible as empirical support; removes a passage that would undermine the volume's credibility with mainstream physicists |
| §9.8.5 (experimental approaches) | Replaced "large-scale psi experiments (telepathy, remote viewing, precognition)" with "quantum-mechanical ensemble experiments seeking consciousness-correlated measurement anomalies"; added "scientifically speculative; no confirmed empirical support" note | Same reason as §9.6.7 |
| §9.8.5 weaknesses | Replaced "psi experiments hint at it" with "No confirmed empirical evidence for consciousness-zone coupling currently exists" | Same reason |
| §9.8.5 falsification discussion | Replaced "large-scale psi experiments with improved controls" with "quantum-mechanical ensemble experiments with improved controls" | Same reason |
| Table (Prediction P-098) | Changed falsification criterion from "50-year psi experiment shows zero effect" to "50-year quantum-ensemble study shows zero anomaly" | Same reason; prediction P-098 itself is retained (consciousness coupling is a legitimate framework prediction), but the falsification criterion must not cite parapsychology literature as the primary test |
| Timeline §9.9 | Changed "Consciousness hypothesis is tested (psi experiments, quantum correlations)" to "Consciousness hypothesis is tested (quantum-ensemble experiments, quantum correlations)" | Same reason |

---

## CHAPTER 10 — Energy Harvesting

| Section | Change | Reason |
|---|---|---|
| Chapter header | Added "Part B — Conditional Engineering" blockquote (with explicit RT-6.CAS reference) | Volume epistemic tier framing |
| §10.8.4 (Dielectric Scaling, after K^(1/3) prediction) | Added "DERIVATION STATUS — Research Task RT-6.CAS" blockquote: K^(1/3) is a dimensional analysis conjecture, not derived from Waters Field Equations or 6D mode structure; Lifshitz gives K^(1/2) from established QED; design basis must be treated as motivated conjecture until RT-6.CAS is resolved | R05, R09: K^(1/3) scaling presented as a "framework prediction" without indicating it is underived; a physicist reading this section cannot distinguish a firm prediction from a guess |

---

## CHAPTER 11 — FTL Communication

| Section | Change | Reason |
|---|---|---|
| Chapter header | Added "Part B — Conditional Engineering" blockquote (noting no-signaling theorem constraint) | Volume epistemic tier framing |

---

## CHAPTER 12 — Advanced Sensors

| Section | Change | Reason |
|---|---|---|
| Chapter header | Added "Part B — Conditional Engineering" blockquote (noting unconfirmed nature of signals sought) | Volume epistemic tier framing |

---

## CHAPTER 13 — Consciousness and the Zone Interface

| Section | Change | Reason |
|---|---|---|
| Chapter header | Added "Part B — Conditional Engineering (Highly Speculative)" blockquote with three explicit conditions: framework correct, consciousness couples to Zone 1, coupling measurable; states "No empirical support for consciousness-zone coupling currently exists" | R06, R10, R15: Ch13 needs stronger speculative labeling than other Part B chapters; consciousness-zone coupling is the least constrained prediction in the volume; the three-condition statement is more explicit than the standard Part B language |

Note: No psi experiment text was found in Ch13 itself; all psi experiment citations in the consciousness section were located in Ch09 (§9.6.7, §9.8.5, P-098 table, timeline) and were fixed there. Ch13's ψ notation is quantum wavefunction notation, not parapsychology references.

---

## CHAPTER 14 — Open Problems

| Section | Change | Reason |
|---|---|---|
| §14.3.5 (OP-1 difficulty) | Added "Research Sub-task OP-1.WF (Warp Function Derivation)" note: W(η) is postulated rather than derived; deriving it is a prerequisite for all three OP-1 resolution paths; tracked as RT-1.WF | R12: OP-1 section does not identify the nearest-term sub-task; OP-1.WF is the first concrete deliverable before any path to spin-½ derivation can proceed |
| §14.4.1 (OP-2 difficulty) | Added "Research Sub-task OP-2.MASS2D (2D Eigenvalue Problem)" note: current eigenvalue computation is 1D; 2D problem may shift mass scale and inter-mode ratios; prerequisite for determining whether Path A of OP-2 is genuinely resolving the gap; tracked as RT-6.MASS2D | R14: OP-2 section does not identify the 2D eigenvalue task as the most immediate computational sub-task |

---

## CHAPTER 15 — Connections to Other Programs

| Section | Change | Reason |
|---|---|---|
| Chapter header | Added "Part C — Self-Assessment" blockquote | Volume epistemic tier framing; Chapter 15 is the framework's own comparative self-evaluation |

---

## CHAPTER 16 — The Technology Roadmap

| Section | Change | Reason |
|---|---|---|
| Chapter header | Added "Part C — Self-Assessment" blockquote with explicit RT-6.CAS warning: MRG design rests on K^(1/3) Casimir scaling not yet derived; RT-6.CAS must be resolved before Phase 1 hardware testing has a confirmed theoretical baseline; notes this does not prevent Phase 1 proceeding | R09, R13: technology roadmap presents MRG design as if the underlying physics is settled; K^(1/3) is a conjecture; readers evaluating the roadmap need this stated before they read the staged plan |

---

## CHAPTER 17 — The Research Program

| Section | Change | Reason |
|---|---|---|
| Chapter header | Added "Part C — Self-Assessment" blockquote | Volume epistemic tier framing |
| §17.4.3a (new subsection) | Added "Priority Research Tasks (Rev. 2026-05-14)" listing all six RT designators: RT-6.MASS2D, RT-1.WF, RT-2.SU3, RT-6.INT, RT-6.CAS, RT-6.REP — each with description, connection to open problems, and chapter cross-references | R12, R16: research program chapter lists OP numbers but not the specific near-term computational/theoretical tasks that were designated during the editorial review; without the RT list, a researcher picking up the framework does not have a clear first step |

---

## SUMMARY OF CRITICAL FIXES

| Priority | Chapter | Fix | Status |
|---|---|---|---|
| CRITICAL BLOCKER | Ch06 | Title corrected; 12% artifact replaced with 0.02% converged result as headline | DONE |
| CRITICAL BLOCKER | Ch09 | All psi experiment citations removed/replaced with scientifically defensible language | DONE |
| HIGH | Ch07 | 930× discrepancy given prominent callout; RT-6.MASS2D designated | DONE |
| HIGH | Ch07 | Mode 2/proton selection rule gap noted; RT-6.SEL designated | DONE |
| HIGH | Ch10 | K^(1/3) Casimir scaling derivation status noted; RT-6.CAS designated | DONE |
| HIGH | Ch08 | Reproducibility requirements section with PENDING/PARTIAL status added | DONE |
| STRUCTURAL | All Part B chapters (9–13) | "Part B — Conditional Engineering" label added | DONE |
| STRUCTURAL | All Part C chapters (14–17) | "Part C — Self-Assessment" label added | DONE |
| STRUCTURAL | Volume | VOLUME_PREFACE.md created with epistemic tier explanation | DONE |
| RESEARCH TRACKING | Ch14 | OP-1.WF and OP-2.MASS2D sub-tasks added | DONE |
| RESEARCH TRACKING | Ch17 | All six priority research tasks (RT-6.MASS2D, RT-1.WF, RT-2.SU3, RT-6.INT, RT-6.CAS, RT-6.REP) listed in §17.4.3a | DONE |

---

## MINIMUM REQUIRED FOR PUBLICATION — STATUS

Per REVIEW_REPORT_Vol6.md §Minimum Required:

1. ✅ Ch06 title and result correction — DONE
2. ✅ Psi experiment citations removed from Ch09 — DONE
3. ✅ Part B/C epistemic labels on all conditional chapters — DONE
4. ✅ Volume preface distinguishing epistemic tiers — DONE
5. ✅ K^(1/3) Casimir derivation status note — DONE
6. ✅ Reproducibility requirements section with status labels — DONE
7. ✅ 930× mass discrepancy given prominent callout — DONE
8. ✅ OP-1 labeled as BLOCKER (was already present; OP-1.WF sub-task added) — DONE
9. ✅ Research tasks RT-6.MASS2D, RT-1.WF, RT-2.SU3, RT-6.CAS, RT-6.REP, RT-6.INT listed — DONE

All minimum-required items complete.

---

*End of FIX_LOG_Vol6.md*
