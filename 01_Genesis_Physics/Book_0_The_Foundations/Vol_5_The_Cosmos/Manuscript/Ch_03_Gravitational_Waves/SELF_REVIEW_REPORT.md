# Self-Review Report — Vol 5 Ch 3: Gravitational Waves

**Date:** 2026-04-09
**Author:** Claude (Genesis Chapter Writer)
**Draft file:** `Ch03_DRAFT.md`
**Target:** 10,000–14,000 words, 11 sections, 9 figures
**Measured:** 12,579 words, 11 sections (§3.0–§3.10), 9 figures (Fig 5.3.1–5.3.9)

---

## 1. Mechanical Audit (hard numbers)

| Check | Target | Measured | Status |
|---|---|---|---|
| Word count | 10,000–14,000 | 12,579 | PASS |
| Sections | 11 (§3.0–§3.10) | 11 | PASS |
| Figures | 9 (Fig 5.3.1–5.3.9) | 9 distinct | PASS |
| Equation range | (5.3.1)–(5.3.78) | (5.3.1)–(5.3.73) | PASS (under budget) |
| `[TODO]` / `[TBD]` markers | 0 | 0 | PASS |
| Problem set | P3.1–P3.10 | 10 problems | PASS |

---

## 2. The "But Why?" Test

For every section I asked: *could a curious reader who just finished §3.(n−1) turn the page and immediately know why they are reading §3.n?*

| Section | Opening "but why" hook | Answered by section end? |
|---|---|---|
| §3.0 | Didn't Vol 2 Ch 8 already do GWs? | Yes — roadmap of inspiral/merger/ringdown shows what's new |
| §3.1 | Is linearized GR consistent with nonlinear (5.1.22)? | Yes — derived as a truncation |
| §3.2 | Why exactly two polarizations? | Yes — 10 − 4 − 4 = 2 counted explicitly |
| §3.3 | Could there be more modes? | Yes — ELLW 6-mode menu enumerated; radion scalar flagged |
| §3.4 | If □h = 0 has no source, where does the energy come from? | Yes — second-order Isaacson averaging |
| §3.5 | Why quadrupole, not monopole or dipole? | Yes — conservation of mass and linear momentum |
| §3.6 | What does LIGO actually see? | Yes — chirp with $\dot f \propto f^{11/3}$ |
| §3.7 | Why not just take more PN orders? | Yes — convergence breaks at ISCO |
| §3.8 | Did the framework earn its keep on real data? | Yes — 7/7 GW150914 quantities match |
| §3.9 | Where could the framework *fail*? | Yes — two concrete falsifiers with numerical predictions |
| §3.10 | What's the honest bottom line? | Yes — scorecard + Reviewer's Ledger |

**Result:** PASS. The why-chain is unbroken.

---

## 3. Forward Dependency Audit

Does any section use a result not yet established at that point in the book?

- §3.1 uses (5.1.22) ✓ (Vol 5 Ch 1)
- §3.1 uses Lorenz gauge, retarded Green's function ✓ (Vol 2 Ch 8)
- §3.2 uses null wave vectors in Minkowski ✓ (Vol 2 Ch 3)
- §3.3 uses KK radion and 4D diffeomorphism invariance ✓ (Vol 1 Ch 4, Vol 5 Ch 1)
- §3.4 uses stress-energy pseudotensor — derived here in §3.4, not assumed
- §3.5 uses multipole expansion ✓ (Vol 2 Ch 5 / Vol 4 Ch 6)
- §3.6 uses Kepler's laws for circular binaries ✓ (Vol 2 Ch 7, Vol 5 Ch 2)
- §3.7 uses ISCO ✓ (Vol 5 Ch 1, (5.1.38))
- §3.7 cites Teukolsky / Regge-Wheeler-Zerilli as sketched (not derived — flagged honestly as inherited from external NR literature; see Reviewer's Ledger in §3.10)
- §3.8 uses all prior derivations ✓
- §3.9 uses KK reduction from Vol 1 Ch 4 and brane tension from Vol 5 Ch 1 ✓

**Result:** PASS. One honest inheritance (NR waveform catalogue) is explicitly flagged in the Reviewer's Ledger.

---

## 4. Notation Consistency

- $h_{\mu\nu}$, $\bar h_{\mu\nu}$ (trace-reversed), $h_{ij}^{\text{TT}}$ — consistent throughout
- $G_4$ for the 4D Newton constant (distinguished from $G_6$ per Vol 5 Ch 1) — consistent
- Chirp mass $m_c$ (not $\mathcal M$) — consistent with convention set in §3.6
- Quadrupole moment $I_{ij}$ (reduced) — consistent
- Radion $\phi$ with breathing-mode amplitude $h_\phi$ — consistent with Vol 1 Ch 4
- Brane tension $\sigma$ — consistent with Vol 5 Ch 1 (5.1.14)

**Result:** PASS.

---

## 5. Prerequisites Satisfied

Checked against the WRITING_PROMPT.md prerequisites table for Vol 5 Ch 3:

- [x] Vol 1 Ch 4: KK reduction and radion
- [x] Vol 2 Ch 3: Minkowski and null geometry
- [x] Vol 2 Ch 5: Multipole expansion
- [x] Vol 2 Ch 7: Kepler orbits
- [x] Vol 2 Ch 8: Linearized GR (explicitly re-established, not re-derived)
- [x] Vol 4 Ch 6: Retarded potentials
- [x] Vol 5 Ch 1: Full (5.1.22), Schwarzschild, Kerr, ISCO, brane tension
- [x] Vol 5 Ch 2: Classical tests (cited as precedent for the "plug and compare" pattern)

**Result:** PASS.

---

## 6. Figure Audit

| Fig | Caption subject | Tied to § | Purpose clear? |
|---|---|---|---|
| 5.3.1 | Three regimes timeline | §3.0 | Yes — roadmap |
| 5.3.2 | + and × polarizations on ring | §3.2 | Yes — the TT picture |
| 5.3.3 | Six-mode ELLW grid | §3.3 | Yes — what GR forbids and the framework adds |
| 5.3.4 | Quadrupole radiation pattern | §3.5 | Yes — angular distribution |
| 5.3.5 | GW150914 strain + prediction overlay | §3.8 | Yes — money plot |
| 5.3.6 | Chirp frequency evolution (data + theory) | §3.6 | Yes |
| 5.3.7 | QNM complex-frequency plane | §3.7 | Yes |
| 5.3.8 | Scalar-mode sensitivity curve | §3.9 | Yes — falsifier window |
| 5.3.9 | GW150914 scorecard | §3.10 | Yes — one-page summary |

Every figure has a caption, a section tie, and a pedagogical purpose.

**Result:** PASS.

---

## 7. Voice and Style

- "Feynman writing a textbook" — maintained ✓ (tested: every section has at least one conversational aside)
- No sermon, no preaching — ✓ (Christ-revealing content surfaces only through the framework's *falsifiability*, which is the project's stealth-discovery mode)
- No mixing of novel/game voice — ✓
- Equations numbered and cited in prose — ✓
- "Honest about limits" — ✓ (Reviewer's Ledger in §3.10 names three unresolved gaps)

**Result:** PASS.

---

## 8. Zone-Framework Distinctives (must be flagged, per user instruction)

The chapter must flag any prediction beyond standard GR's 2 TT modes.

- **Scalar breathing mode** from KK radion, §3.3 (qualitative) and §3.9 (numerical):  $h_\phi/h_\text{tensor} \sim (v/c)^2$, average prediction 0.05, just below LIGO O3 bound of 0.10, reach of Einstein Telescope. FLAGGED and quantified.
- **Brane-tension correction to orbital decay:** $\delta(da/dt)/(da/dt) \sim 10^{-4}$; current GW150914 phase precision $\sim 10^{-3}$; O4/O5 projection $\sim 10^{-4}$. FLAGGED and quantified.

**Result:** PASS. Both distinctives appear with numerical predictions *and* experimental sensitivity floors, making them true falsifiers rather than unfalsifiable add-ons.

---

## 9. Open Problems / Research Gaps (honest ledger)

Recorded in §3.10's Reviewer's Ledger:

1. **Radion mass $m_\phi$** — the predicted scalar-mode amplitude assumes $m_\phi \ll \omega_\text{GW}$; if the radion is heavy enough to suppress propagation at LIGO band, the falsifier weakens. This is a Vol 6 question.
2. **NR merger-phase inheritance** — the chapter does not re-derive numerical-relativity waveform catalogues; it inherits them from the literature and assumes the zone framework's corrections factor into a small multiplicative template correction. A first-principles NR run in the zone framework is listed as future work.
3. **Brane-tension coefficient $c_\sigma$** — the order-of-magnitude estimate $c_\sigma \sim O(1)$ is used; a precise value awaits a 6D matched-asymptotic calculation.

All three are flagged in the scorecard and deferred to named later chapters / Vol 6.

**Result:** PASS. No silent assumptions.

---

## 10. Overall Self-Assessment

**Ready for Reviewer Agents:** YES

Strengths:
- Unbroken why-chain.
- Every prediction numerical and sourced.
- Zone-framework distinctives are quantified as falsifiers, not hand-waved.
- Word count and figure count both on budget.

Weak spots to highlight to reviewers:
- §3.7's NR inheritance (the biggest "trust us" moment) — flag for Skeptic and Physicist.
- §3.3's radion mass assumption — flag for Physicist.
- Problem P3.9 (brane-tension reach) is on the harder side — flag for Student.

Proceeding to Phase 5.

---

*End of SELF_REVIEW_REPORT.md*
