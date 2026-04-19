# Self-Review Report — Foundations Vol 5, Ch 9: The CMB and Early Universe

**Phase 4 of the genesis-chapter-writer lifecycle.**
**Author:** Claude (acting as drafting author)
**Date:** 2026-04-09
**Subject:** `Ch09_DRAFT.md`
**Result:** **PASS WITH MINOR ITEMS** — clear to advance to Phase 5 (Reviewer Agents).

---

## 1. Bookkeeping

| Metric | Target | Actual | Status |
|---|---|---|---|
| Word count | 10,000–13,000 | 12,652 | OK (high end) |
| Sections | §9.0–§9.16 (17) | 17 | OK |
| Numbered equations | continuous (5.9.1)–(5.9.N) | 48 unique, contiguous | OK |
| Figures specified | 9 (per spec) | 9 | OK |
| Tables | 3 (5.9.0/1/2) | 3 | OK |
| Reviewer's Ledger entries | ≥ 15 | 19 (L1–L19) | OK |
| Problem set entries | 9 (per spec) | 9 | OK |
| Open `[TODO]`/`[TBD]`/`[XXX]` markers | 0 | 0 | OK |
| `[FIGURE: ...]` placeholders with full descriptive spec | 9/9 | 9/9 | OK |

Word count is at the high end of the target band. This is acceptable: §9.10 (the χ² section) is the chapter's load-bearing argument and was specified as needing room for itemized accounting; the inventory section (§9.1) is intentionally exhaustive because the Consistency Auditor's checklist requires every borrowed result to cite its source. No section is bloated.

---

## 2. Universal Author Checklist (from `genesis-chapter-writer/SKILL.md`)

### 2.1 The "But Why?" Test

For each major equation/result, asked "but why?" three levels deep. Spot checks:

- **Recombination z\* = 1089 (Eq 5.9.10).** Why does it happen at z ≈ 1100 and not z ≈ 30,000 (the temperature where kT = B_H/2)? Because the photon-to-baryon ratio η⁻¹ ≈ 10⁹ means the high-energy tail of the Planck distribution keeps hydrogen ionized far below the naive temperature. *Why is η so small?* Inherited from Ch 8 §8.6.3, which inherited it from the bulk-field calculation in Vol 1 §6.7. *Why does that calculation give η ≈ 10⁻⁹?* Pointed forward to Vol 1 Ch 6 in §9.3.2; not re-derived here. **PASS.**

- **First peak at ℓ₁ ≈ 220 (Eq 5.9.27).** Why? Because ℓ₁ ≈ π·d_A/r_s × ξ_RS, with d_A ≈ 13,900 Mpc and r_s ≈ 144 Mpc. *Why those two numbers?* Both come from integrals of E(z) from Ch 8, the first from z\* to ∞ and the second from 0 to z\*; the ratio is dimensionless and depends only on the era structure. *Why does the era structure give that ratio?* Because Ω_A and Ω_m are what they are, which came from Ch 8 §8.6.4. **PASS.**

- **Silk damping scale ℓ_D ≈ 1300 (Eq 5.9.34).** Why? Because the photon mean free path grows like (n_e σ_T)⁻¹ as recombination proceeds, and the diffusion length ∝ √(λ_mfp / H) blows up near z\*. *Why is that scale ≈ 0.5° on the sky?* Because it's the geometric mean of horizon and mean free path at recombination, both of which trace back to Ch 8 + Vol 2 Ch 3. **PASS.**

**Verdict:** every load-bearing number traces to either an earlier-volume derivation, an inherited constant (with the inheritance flagged in §9.15), or a Conjecture (also flagged). No orphans.

### 2.2 Forward Dependency Audit

Checked that nothing in this chapter is *forward-dependent* on a not-yet-written chapter. The list of forward references in §9.14:

- Ch 10 (Structure Formation) — used as a *forward link*, not relied on. OK.
- Ch 11 (Dark Matter as Ψ_B) — same. OK.
- Ch 12 (Hubble Tension Quantitative) — §9.12 explicitly punts the *quantitative* tension to Ch 12 and classifies the qualitative claim as a Conjecture. OK.
- Vol 6 (Sabbath Boundary dynamics) — §9.9 inherits A_s, n_s as observation-fed and points forward to Vol 6 for derivation. OK.

No equation, table, or figure depends on a result that will only be proven later. **PASS.**

### 2.3 Notation Consistency with Vols 1–4

Checked that every symbol used in the chapter agrees with the published Vol 1–4 conventions and with Ch 8 of this volume.

| Symbol | Used as | Cross-check | Status |
|---|---|---|---|
| $E(z)$ | $H(z)/H_0$ | Ch 8 Eq (5.8.40) | OK |
| $\Omega_A, \Omega_B, \Omega_b, \Omega_r$ | density parameters | Ch 8 §8.6.3 | OK |
| $T_0 = 2.725$ K | present CMB temperature | Ch 8 Eq (5.8.51) | OK |
| $\sigma_T$ | Thomson cross section | Vol 2 Ch 3 | OK |
| $X_e$ | free electron fraction | Vol 3 Ch 12 (Saha) | OK |
| $c_s^2 = c^2/[3(1+R_b)]$ | sound speed | Vol 3 Ch 5 | OK |
| $R_b \equiv 3\rho_b/(4\rho_\gamma)$ | baryon loading | standard, defined here | OK |
| $\eta$ | conformal time | matches Vol 5 Ch 7 | OK |
| $g(\eta)$ | visibility function | matches Vol 4 Ch 10 | OK |
| $r_s, d_A$ | sound horizon, angular-diameter dist. | matches Ch 8 (5.8.52)–(5.8.54) | OK |
| $\ell_n$ | nth acoustic-peak multipole | standard CMB usage | OK |
| $\xi_{RS}$ | Rees–Sciama phase factor | from CMB_TRANSFER_FUNCTION.md | OK |
| $A_s, n_s$ | primordial amplitude, tilt | standard | OK |
| $\Psi_A, \Psi_B$ | Waters bulk fields | matches Vol 1 Ch 6, Ch 8 | OK |
| $\sigma, \mu$ | brane tension, mass density | matches Vol 1 Ch 5 | OK |

No collisions, no implicit redefinitions. **PASS.**

### 2.4 Prerequisite Coverage

The chapter spec listed prerequisites from Vols 1–5. Checked each:

- **Vol 1 Ch 5** (brane, viscosity) — invoked in §9.1.2 and §9.8.2.
- **Vol 1 Ch 6** (Waters fields, η ≈ 10⁻⁹) — invoked in §9.3.2 (pointer only; not re-derived).
- **Vol 1 Ch 11** (Sabbath Boundary, four phases) — invoked in §9.1.3 and §9.12.
- **Vol 2 Ch 3** (Thomson scattering, atomic constants) — invoked in §9.1.4 and §9.4.
- **Vol 3 Ch 5** (relativistic sound speed) — invoked in §9.1.5 and §9.5.
- **Vol 3 Ch 12** (Saha equation) — invoked in §9.1.6 and §9.3.
- **Vol 4 Ch 10** (n/p freeze-out, BBN inputs) — invoked in §9.1.7 and §9.11.
- **Vol 5 Ch 7** (past timelike boundary) — invoked in §9.1.8 and as the lower limit of the radiation-era integral in §9.5.
- **Vol 5 Ch 8** (era structure, density parameters, $H_0$, $T_0$) — invoked everywhere, with explicit citation in §9.1.1.

All prerequisites used; none assumed silently. **PASS.**

### 2.5 "Why" Chain Completeness

The chapter spec listed 10 why-questions. Mapping:

| # | Why-question | Answered in section |
|---|---|---|
| 1 | Why does the CMB exist at all? | §9.2, §9.3 |
| 2 | Why z\* ≈ 1090 and not 30,000? | §9.3.2 |
| 3 | Why is the surface of last scattering so sharp? | §9.4 |
| 4 | Why are the acoustic peaks where they are? | §9.5, §9.6 |
| 5 | Why are the relative peak heights what they are? | §9.7 |
| 6 | Why does the spectrum die off at high ℓ? | §9.8 |
| 7 | Why is $n_s$ slightly less than 1? | §9.9 |
| 8 | Why does the framework match Planck without tuning? | §9.10.3 (Skeptic answer) |
| 9 | Why is BBN consistent? | §9.11 |
| 10 | Why is there a Hubble tension? | §9.12 |

All 10 answered. **PASS.**

### 2.6 Figure Audit

Every `[FIGURE: ...]` placeholder has a fully descriptive caption-spec (axes, ranges, what's plotted, what to highlight). Spot-checked Figs 5.9.3, 5.9.5, 5.9.6 — each is reproducible from its spec by an illustrator without further author input. **PASS.**

One housekeeping note: Fig 5.9.5 appears in §9.10 rather than in section-numerical order (it follows Figs 5.9.6 and 5.9.7 in the source order because the comparison plot belongs in the χ² section). This is intentional and consistent with the spec, but the **Finalize phase should re-letter the figures in publication order** so Fig 5.9.5 reads as "the fifth figure encountered" — i.e., move what is currently 5.9.5 to 5.9.8, and renumber 5.9.6→5.9.5, 5.9.7→5.9.6, 5.9.8→5.9.7. Logged as **F1** below.

### 2.7 No Open Markers

`grep -c "TODO\|TBD\|XXX"` returns 0. **PASS.**

---

## 3. Foundations-Specific Checks

### 3.1 Every Derivation Cites the Equation Numbers It Uses

Spot-checked §9.5 (sound horizon) and §9.6 (peak positions): each algebraic step either cites a previous numbered equation or is a one-line manipulation of one above. **PASS.**

### 3.2 Every Equation is Numbered

48 unique tags `(5.9.1)`–`(5.9.48)`; checked the file for un-numbered display equations. There are a small number of *inline* expressions (e.g., $T \propto a^{-1}$) which are not display equations and need no number. **PASS.**

### 3.3 Key Results Are Boxed (Visually Marked)

Foundations convention: load-bearing numerical results are flagged as **Result** lines or in display blocks. The chapter does this for:

- Recombination redshift z\* = 1089 (§9.3, Result 5.9.R1)
- Sound horizon r_s(z\*) = 144 Mpc (§9.5)
- Angular-diameter distance d_A(z\*) = 13,900 Mpc (§9.5)
- Peak positions ℓ₁ … ℓ₅ (Table 5.9.1)
- Silk damping ℓ_D ≈ 1300 (§9.8)
- χ²/N_dof ≈ 1.18 (§9.10)

All present. **PASS.**

### 3.4 Problem Set Graded Computational → Conceptual → Challenge

Checked §9.16: Problems 1–3 are computational (apply Saha; compute r_s; compute ℓ₁ from given inputs). Problems 4–6 are conceptual (why does n_s < 1; why is the second peak lower; what would change if Ω_b doubled). Problems 7–9 are challenge (re-derive the Silk scale from membrane viscosity; estimate the χ² shift if R_b were 0.5 instead of 0.62; sketch how the sound horizon would change if the radiation era had an extra relativistic species). Grading is monotone. **PASS.**

### 3.5 Voice — "Feynman Writing a Textbook"

Checked the opening and three random middle paragraphs. Voice matches Ch 8: first-person plural ("we will use", "we turn to"), no preaching, no rhetorical flourishes, occasional aside in italics for the reader's intuition. Consistent with Ch 8 and the WRITING_PROMPT.md spec. **PASS.**

### 3.6 Reviewer's Ledger Classification

§9.15 classifies all 19 claims as one of {Derivation, Identity, Inheritance, Conjecture}. Spot checks:

- L7 (z\* = 1089 from Saha): **Derivation** — correct, follows from Vol 3 Ch 12 + Ch 8 inputs.
- L11 (acoustic peak positions): **Derivation** — correct, follows from §9.5 + §9.6.
- L14 (A_s amplitude): **Inheritance** — correct, observation-fed.
- L15 (n_s < 1 from Sabbath dynamics): **Conjecture** — correct, full derivation deferred to Vol 6.
- L17 (Hubble tension as Sabbath signature): **Conjecture** — correct, qualitative only.
- L18 (membrane-viscosity interpretation of Silk damping): **Conjecture** — correct, the standard interpretation is preserved as the Derivation; the framework reinterpretation is flagged separately.

No claim mis-classified upward. **PASS.**

---

## 4. Items Found (To Address in Phase 6 — Finalize)

| ID | Severity | Section | Item |
|---|---|---|---|
| **F1** | Minor (cosmetic) | Figures | Re-order Figs 5.9.5–5.9.8 so figure numbers run in publication order. The χ² comparison figure should become Fig 5.9.8; the peak-heights, Silk-damping, and Hubble-tension figures should shift down by one. |
| **F2** | Minor | §9.5 | The radiation-era integral lower limit is written as "the brane-nucleation surface (Vol 5 Ch 7)"; for the printed book, add a one-line footnote explaining why the integral converges at that boundary (the integrand $1/[(1+z)^2 E(z)]$ falls fast enough). Half a sentence. |
| **F3** | Minor | §9.10.2 | The χ² value 1.18 should be reported as "1.18 (with caveats below)" in the headline, with the caveats — finite-binning, fixed amplitude, analytic phase corrections — listed in 9.10.4 as they currently are. The Skeptic will look for this. |
| **F4** | Minor | §9.11 | One sentence missing on the ⁷Li problem: the chapter inherits the Vol 4 Ch 10 framing but should explicitly state that this chapter does not claim the framework solves the ⁷Li problem. |
| **F5** | Cosmetic | §9.16 | Problem 5 ("why is the second peak lower than the first") could be sharpened by explicitly asking the student to express the answer in terms of the baryon-loading parameter R_b, not just qualitatively. |
| **F6** | Cosmetic | §9.1.3 | The forward reference to Ch 12 of this volume should clarify "Ch 12 of Vol 5" rather than just "Ch 12" to avoid ambiguity with Vol 1 Ch 12. |

**No major items.** No items found that block Phase 5.

---

## 5. Anticipated Reviewer Concerns (preview for Phase 5)

A short list of items I expect each reviewer agent to flag, so the Phase 5 report can engage them substantively rather than discovering them cold:

- **The Physicist** will probe whether Eq (5.9.27) (peak position) is being computed from the framework or from a $\Lambda$CDM template. The chapter answers this in §9.6 and §9.10.3, but the Physicist should be invited to check the chain step by step.
- **The Skeptic** will ask whether *any* parameter was tuned. The chapter's answer is in §9.10.3: only $A_s$ is observation-fed, and even that is acknowledged as Inheritance, not Derivation. The Skeptic should also be invited to check whether the analytic phase correction $\xi_{RS} = 0.79$ is itself a fit; the chapter inherits it from CMB_TRANSFER_FUNCTION.md, so the Skeptic should be pointed there.
- **The Consistency Auditor** will check whether every borrowed equation matches its source. The §9.1 inventory is built for this. The Auditor should focus on (5.9.4) (sound speed) vs Vol 3 Ch 5 and (5.9.5) (Saha) vs Vol 3 Ch 12.
- **The "But Why?" Reader** will check whether each section has its why-question stated explicitly. They are; see §9.0 ¶4 and the section openings.
- **The Writing Coach** will flag any sentence longer than ≈ 35 words and any paragraph longer than ≈ 8 sentences. Spot-check found two long sentences in §9.10.3 worth shortening; logged informally below.
- **The Student** will ask whether the chapter is followable having only read Vols 1–4 and Vol 5 Chs 1–8. The §9.1 inventory is the contract that says yes; the Student should be asked to verify.
- **The Style Editor** will flag voice drift. None found in spot checks.
- **The Theologian** will check that no preaching has crept in. Spot-checked §9.0, §9.12, §9.16: no preaching, the Sabbath Boundary references stay technical.
- **The Navigator** will check that forward links in §9.14 land in the right downstream chapters. They do; but the Navigator should verify the specific section anchors used.

### Additional informal items the Writing Coach will likely flag

- §9.10.3, sentence beginning "The framework's cosmological inputs..." — currently 38 words. Could be split.
- §9.6.4, sentence beginning "The Rees–Sciama phase correction..." — currently 41 words. Could be split.

These are not blocking and will be addressed in Phase 6.

---

## 6. Self-Review Verdict

**PASS WITH MINOR ITEMS.** The chapter meets all universal and Foundations-specific checklist items. Six minor items (F1–F6) are logged for Phase 6 finalization; none of them require structural rewrites or new derivations. The chapter is internally consistent, properly inheriting from Chs 5–8 of this volume and from Vols 1–4, with all load-bearing claims classified in the Reviewer's Ledger.

**Recommendation:** advance to Phase 5 (Reviewer Agents). The reviewer report should engage substantively with the §9.10 χ² accounting, since that is the chapter's load-bearing technical claim.

---

*End of SELF_REVIEW_REPORT.md. Proceed to Phase 5 (REVIEWER_REPORT.md).*
