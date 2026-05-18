---
product: Foundations Vol 5
chapter: 13
title: The Fine Structure Constant from First Principles
phase: 4 — Self-Review
date: 2026-04-09
---

# Chapter 13 — Self-Review Report

## Universal Author Checklist

- [x] **"But why?" test.** Read the chapter as a newcomer. Every claim is prefaced with its reason: §13.1 asks why now, §13.2 asks why these two scales, §13.3 asks why the logarithm, §13.4 asks why KK = RG, §13.5 asks why $b_{\text{eff}}$ has four pieces, §13.6 asks why the uncertainty is what it is, §13.7 asks why the Skeptic should believe it, §13.9 asks why the limits matter, §13.10 asks why the gaps are not cracks. No paragraph asserts without explaining.
- [x] **Forward dependency audit.** Every concept used in the chapter is introduced in a prior chapter: 6D metric (Vol 1 Ch 4), warp factors (Vol 1 Ch 6), brane thickness (Vol 1 Ch 5), 6D gauge action (Vol 2 Ch 3 §3.1), KK reduction (Vol 2 Ch 3 §3.3), one-loop $\beta$-function (Vol 4 Ch 8 §8.7), SM spectrum (Vol 4 Ch 10), confinement scale (Vol 4 Ch 12 §12.3). No concept is used before it appears in the curriculum.
- [x] **Notation consistency.** Symbols match Vols 1–4: $\xi_A$, $\eta_B$, $A(\xi)$, $B(\eta)$, $f_0$, $\kappa_6$, $b_{\text{eff}}$, $\alpha^{-1}$, $L$. Equation numbering $(5.13.N)$ throughout.
- [x] **Prerequisites satisfied.** Prerequisites list in CHAPTER_SPEC.md matches what the chapter actually uses.
- [x] **"Why" chain complete.** Traced in CHAPTER_SPEC.md §"Why chain"; the chapter follows the six-step chain explicitly.
- [x] **Word count in range.** 10,923 words, within Foundations target of 8,000–15,000 and appropriate to a crown-jewel chapter at the high-middle of the range.
- [x] **All `[TODO]` markers resolved.** Zero TODO markers in the draft.
- [x] **Figure audit.** 8 figures specified with placeholders and full specs in CHAPTER_OUTLINE.md and CHAPTER_SPEC.md. Every spatial relationship (Fig 5.13.2, 5.13.3), every transformation (Fig 5.13.1 roadmap, 5.13.4 running), every multi-step derivation (Fig 5.13.1, 5.13.7 tree), every conceptual model (Fig 5.13.3, 5.13.5), every data comparison (Fig 5.13.4, 5.13.6), and every limit check (Fig 5.13.8) has a figure. Density is 8 figures per ~40 pages, at the "high" end of the Foundations target (2–4 per chapter minimum).

## Product-Specific Checks (Foundations)

- [x] **Every derivation starts from previously established results and cites equation numbers.** §13.3 cites Vol 2 Ch 3 Eq (2.3.15), Vol 1 Ch 6 Eq (1.6.18), Vol 1 Ch 4. §13.4 cites Vol 4 Ch 8 Eq (4.8.20). §13.5 cites Vol 4 Ch 8 Eq (4.8.34), Vol 4 Ch 10. §13.2 cites Vol 1 Ch 5 Eq (1.5.43), Vol 1 Ch 6 Eq (1.6.22), Vol 5 Ch 8 §8.4, Vol 4 Ch 12 §12.3.
- [x] **Every equation gets a number.** 61 numbered equations, all in the $(5.13.N)$ namespace.
- [x] **Key results get boxes.** Two boxed results: Eq (5.13.32) the master formula, and Eq (5.13.40) the numerical answer. One boxed worked example (Box 5.13.A).
- [x] **Problem sets: computational → conceptual → challenge.** Three computational (P1, P2, P3), two conceptual (P4, P5), one challenge (P6*).

## Writing Laws Check

- [x] **Law 1 — Start with WHY.** The chapter opens with Feynman's epigraph, frames the mystery, and states the claim in the first three paragraphs.
- [x] **Law 2 — Physical intuition before math.** §13.2 establishes the two scales with a log-axis picture before any equation in §13.3.
- [x] **Law 3 — One voice.** Feynman-textbook voice maintained throughout. Consistent with the voice of Ch 12 (which was the closest comparison in tone).
- [x] **Law 4 — No forward dependencies.** Confirmed above.
- [x] **Law 5 — Mark uncertainty honestly.** Section 13.10 is a dedicated gaps section; gap flags propagate to §13.5 ($b_{\text{red}}$, $b_{\text{hi}}$) and §13.6 (UV boundary). §13.6 explicitly reports two error budgets (conservative and headline). Every gap-flagged row in Table 5.13.1 and Fig 5.13.7 is explicitly yellow.

## Known Issues / Reviewer-Visible Items

The chapter deliberately carries three items that will surface in the reviewer report. I flag them here so the reviewers see them in context:

1. **Numerical slop between $b_{\text{eff}} = 9.05$ and $b_{\text{eff}} = 9.07$.** §13.5.6 explicitly notes the 0.02 discrepancy between the two-digit value quoted in the research archive and the three-digit sum of the four pieces. It is inside the error budget of $b_{\text{red}}$ and $b_{\text{hi}}$, and is explicitly flagged as part of Gap 2. This is the honest thing to do; it will look like inconsistency at a casual read and invite the Consistency Auditor's attention. I want the Consistency Auditor to see the flag and accept the honest reporting rather than silently rounding.

2. **Two error budgets (conservative and headline).** §13.6.3 reports both. This gives the chapter an unusual double-valued claim: $137.17 \pm 0.15$ (headline) and $137.17 \pm 2.5$ (conservative). The Skeptic reviewer will probably push on which one is "the" claim. The honest answer is: the conservative budget is what the chapter can claim from derivations alone; the headline budget is what the chapter can claim if the reader accepts the quasi-fixed-point argument. Both are stated.

3. **§13.5.1 formula $b_0 = (2/3)\sum_i N_c q_i^2$ gives 16/3 ≈ 5.33, not 3.67.** The chapter reconciles this by noting that 16/3 is the asymptotic value and 3.67 is the threshold-integrated value. A careful reader may want the integration worked in more detail. The full derivation is in Vol 4 Ch 8 §8.7 and is cited; the chapter does not re-derive it. I judged that re-deriving it here would double the length of §13.5 without adding new physics, and opted for the citation. If the Physicist reviewer wants the full integral written out, I will add it in revision.

## Overall

All universal and product-specific checks pass. Three reviewer-visible items are flagged. Proceeding to Phase 5 (Reviewer Verification).
