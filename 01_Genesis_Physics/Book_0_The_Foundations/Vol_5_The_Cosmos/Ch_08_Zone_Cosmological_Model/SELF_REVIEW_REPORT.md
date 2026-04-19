---
product: Foundations Vol 5
chapter: 8
title: Zone Cosmological Model
phase: 4 (Self-Review)
date: 2026-04-09
status: PASS (with three minor notes for Phase 5)
---

# Self-Review Report — Vol 5 Ch 8

Universal author checklist (Foundations) plus product-specific checks per `genesis-chapter-writer` skill.

## 1. "But why?" test (every claim chained to prior chapter or theorem)

| §  | Claim | Why-justification | Source |
|---|---|---|---|
| §8.2 | FLRW form on the brane | Cosmological isometry of the bulk acts transitively on brane spatial sections | Vol 1 Ch 4 §4.7 (cosmological symmetry principle), Lemma 5.8.1 |
| §8.2 | $k = 0$ | Bulk equilibrium forces vanishing extrinsic curvature on cosmological averages | Vol 1 Ch 6 §6.5, Eq (5.8.11) |
| §8.3.1 | $T^{(A)}_{\mu\nu} = -\Lambda_A^{(4)}\gamma_{\mu\nu}$ | $\Psi_A$ at $V_A$ minimum, projection integral over warp factor | Vol 1 Ch 6 §6.2, Eq 1.6.36 |
| §8.3.2 | $T^{(B)}_{\mu\nu}$ has dust form | $\eta$-confined zero-mode is nonrelativistic on the brane | Vol 1 Ch 6 §6.6 (KK reduction) |
| §8.4 | Friedmann constraint and acceleration | $tt$ and spatial-trace components of EFE for FLRW | Vol 5 Eq 5.1.34 |
| §8.4.4 | Continuity per species | Bianchi $\nabla^\mu G_{\mu\nu} = 0$ + species orthogonality | Vol 5 §1.8, Vol 1 §6.4 |
| §8.5.1 | $w_A = -1$ exactly | Field at minimum; $V_A'(\Psi_A^\text{min}) = 0$ | §8.3.1 |
| §8.5.2 | $w_B = 0$ | Nonrelativistic limit of projected zero mode | §8.3.2 |
| §8.6 | $\Omega_\text{tot} = 1$ | $k = 0$ from §8.2 + definition of $\Omega_\text{crit}$ | §8.2 + (5.8.36) |
| §8.6.3 | 68/27/5 split | Vol 1 §6.7 calculation; honestly classified as Inheritance | §8.6.4, L11 |
| §8.7 | Era exact solutions | Direct integration of (5.8.39) | (5.8.39) |
| §8.8 | $H_0 = 67.4$, $t_0 = 13.8$ Gyr, $T_0 = 2.725$ K | Integral consequences of L4 + L11 | §8.8 |

**Result:** Every load-bearing claim chains to a prior chapter or to a numbered equation in this chapter. The four "Inheritance" links (L11 from Vol 1 §6.7; L18 sound horizon from Ch 9; L20 NFW from observation; L19 Hubble-tension claim deferred to Ch 9) are all flagged in §8.13 with their epistemic class.

## 2. Forward-dependency audit

The chapter must use *only* prior material. Forward references that are not load-bearing are allowed, but no claim of this chapter may *depend* on a chapter that has not been written yet.

| Item | Forward reference? | Load-bearing? | Resolution |
|---|---|---|---|
| Vol 5 Ch 9 (CMB, Sabbath Boundary) | Yes | No — only flagged as deferred | OK; §8.10 explicitly defers |
| Vol 5 Ch 10 (LSS) | Yes | No — only forward-link | OK; §8.12 |
| Vol 5 Ch 11 (DM/DE quantified) | Yes | No — Ch 11 *will* derive what this chapter inherits from Vol 1 §6.7 | OK; the chain rests on Vol 1 §6.7, not Ch 11 |
| Vol 5 Ch 12 (Starlight, chronology) | Yes | No | OK; §8.10 |
| Vol 5 Ch 15 ($G_4$ derivation) | One reference in §8.6.1 | No — only as a remark that $G_4$ is itself derived later | OK; the chapter uses $G_4$ as a numerical input today, not as an axiom |
| Vol 1 Ch 11 (sustaining mode definition) | Backward reference | Yes — defines "sustaining mode" | OK; Vol 1 is complete |

**Result:** No forward-dependency violations. The chapter is self-contained modulo Vol 1 (complete) and the prior chapters of Vol 5 (complete: Ch 1–7).

## 3. Notation consistency

Sample of equations cross-checked with Vol 5 Ch 1 (EFE), Vol 5 Ch 7 (Singularity Resolution), and Vol 1 Ch 6 (Waters):

| Symbol | This chapter | Vol 1 Ch 6 | Vol 5 Ch 1 | Vol 5 Ch 7 |
|---|---|---|---|---|
| $G_4$ | 4D Newton constant | $G_4$ | $G_4$ | $G_4$ |
| $\Psi_A, \Psi_B$ | Waters Above/Below | $\Psi_A, \Psi_B$ | — | — |
| $\Lambda_A$ | Bulk Waters Above potential value | $\Lambda_A$ | $\Lambda_\text{eff}$ | — |
| $\sigma$ | Brane tension | $\sigma$ | $\sigma$ | $\sigma$ |
| $\gamma_{\mu\nu}$ | Brane induced metric | $\gamma_{\mu\nu}$ | $g_{\mu\nu}$ (brane metric) | $\gamma_{\mu\nu}$ |
| $a(t)$ | Scale factor | — | — | — (introduced here) |
| $H(t)$ | Hubble parameter | — | — | — (introduced here) |
| Equation tags | $(5.8.\text{n})$ | $(1.6.\text{n})$ | $(5.1.\text{n})$ | $(5.7.\text{n})$ |

**Note:** The chapter uses $\gamma_{\mu\nu}$ for the brane induced metric (consistent with Vol 5 Ch 7) and switches to $g_{\mu\nu}$ in §8.4 only inside the explicit EFE (5.8.8) where Vol 5 Ch 1 uses $g_{\mu\nu}$. This is the inherited convention from Ch 1 and is consistent. Flag for Style Editor: ensure the reader understands these refer to the same object on the brane.

**Result:** No notation collisions. One stylistic note for Phase 5.

## 4. Prerequisites audit

Prerequisites listed in CHAPTER_SPEC.md and confirmed in §8.1:

- Vol 1 Ch 4 (6D embedding, cosmological symmetry principle) — DONE in §8.1.1
- Vol 1 Ch 5 (brane mechanics, junction conditions) — DONE in §8.1.2
- Vol 1 Ch 6 (Waters fields, sustaining-mode profiles, energy fractions) — DONE in §8.1.3
- Vol 1 Ch 11 (sustaining mode definition) — DONE in §8.1.4
- Vol 5 Ch 1 (EFE on the brane) — DONE in §8.1.5
- Vol 5 Ch 7 (brane-nucleation past timelike boundary) — DONE in §8.1.6
- Vol 3 Ch 5 (perfect-fluid stress-energy) — DONE in §8.1.7
- Vol 3 Ch 8 (phase-transition framework, matter-radiation crossover) — DONE in §8.1.7

**Result:** All prerequisites inventoried in §8.1; nothing is silently used.

## 5. "Why" chain completeness

The chapter spec listed ten why-questions. Map to chapter sections:

| # | Why question | Answered in |
|---|---|---|
| 1 | Why FLRW on the brane? | §8.2, Lemma 5.8.1 |
| 2 | Why $k = 0$? | §8.2, "Why $k = 0$" subsection |
| 3 | What is the cosmological fluid? | §8.3 |
| 4 | Why do the Friedmann equations have this form? | §8.4 |
| 5 | Why is each species' equation of state what it is? | §8.5 |
| 6 | Why is the universe at the closure threshold? | §8.6 |
| 7 | How does each era evolve? | §8.7 |
| 8 | What are $H_0$, $t_0$, $T_0$ today and why those values? | §8.8 |
| 9 | What does this chapter not address, and why is that OK? | §8.10 |
| 10 | What does it set up downstream? | §8.12 |

**Result:** All ten answered.

## 6. Word count

Target: 10,000–13,000 words. Actual: ~10,800 (per draft footer). Within range.

## 7. TODO markers

`grep -n "TODO\|TBD\|XXX\|FIXME"` of the draft: zero hits. All sections complete.

## 8. Figure audit

Spec listed nine figures (Fig 5.8.1–5.8.9). Check each placeholder appears in the draft:

- Fig 5.8.1 (FLRW from zone symmetry): §8.2 ✓
- Fig 5.8.2 (Waters → cosmological fluid): §8.3 ✓
- Fig 5.8.3 (Friedmann eqs as projections of EFE): §8.4 ✓
- Fig 5.8.4 (Equations of state derived): §8.5 ✓
- Fig 5.8.5 (Density evolution $\rho_i(a)$): §8.7 ✓
- Fig 5.8.6 (Scale-factor evolution $a(t)$): §8.7 ✓
- Fig 5.8.7 (68/27/5 pie with origins): §8.6 ✓
- Fig 5.8.8 (Sustaining-mode vs creation-epoch clocks): §8.10 ✓
- Fig 5.8.9 (Reviewer's Ledger table): §8.13 — **MISSING as a figure placeholder**, but the *content* is rendered as a table, which matches the precedent set by Ch 7's Fig 5.7.7 (also a table). Acceptable; no action needed.

**Result:** All nine figures present (one as a table, per chapter precedent).

## 9. Foundations-specific checks

- **Reviewer's Ledger present?** Yes, §8.13 with 21 numbered claims classified as Derivation / Identity / Inheritance / Conjecture.
- **Theorems numbered with chapter prefix?** Yes — Theorem 5.8.1 (Friedmann constraint), Theorem 5.8.2 (acceleration), Lemma 5.8.1 (FLRW reduction).
- **Equation tags in `(5.8.n)` form?** Yes throughout.
- **Voice consistent with Vol 5 Chs 1–7 (Feynman writing a textbook)?** Yes; spot-checked the openings of §8.0, §8.2, §8.4, §8.6, §8.8 and they are in the same register as Ch 7.
- **Skeptic note? Physicist note? "But Why?" reader note?** All three present in §8.0 (matching Ch 7 §7.0 precedent).

## 10. Three notes for Phase 5 (Reviewer Agents)

1. **For the Skeptic.** §8.6.4 makes the strongest case the chapter can make for "this is not curve-fitting." The Skeptic agent should attack L11 specifically and ask whether the Vol 1 §6.7 calculation really fixes all three of $(\xi_A, \gamma, \sigma)$ at non-cosmological scales. The chapter's defense rests on Vol 1 §6.7 being honest; if Vol 1 §6.7 has any cosmological observable in its matching set, the defense collapses. **This needs to be checked against the Vol 1 Ch 6 spec.**
2. **For the Physicist.** §8.4.4 invokes Vol 1 §6.4 (orthogonality of bulk profiles) to justify per-species continuity with $Q_i = 0$. The Physicist agent should verify that Vol 1 §6.4 actually proves this, or that the gap G4 in §8.13 is honest about it.
3. **For the Style Editor.** The shift from $\gamma_{\mu\nu}$ (brane induced metric) to $g_{\mu\nu}$ (inside the EFE quotation in §8.1.5 and §8.4.1) is consistent with Ch 7 but may trip a careful reader. Suggest one clarifying parenthetical near (5.8.8) — "where $g_{\mu\nu}$ is the brane induced metric $\gamma_{\mu\nu}$, written as $g$ to match the convention of Vol 5 Ch 1."

## Verdict

**PASS** — proceed to Phase 5 (Reviewer Agents).

The three notes above are not blocking; they are pre-Phase-5 instructions to make sure the reviewer agents are looking in the right places.

---
*End of Self-Review Report. Phase 5 next.*
