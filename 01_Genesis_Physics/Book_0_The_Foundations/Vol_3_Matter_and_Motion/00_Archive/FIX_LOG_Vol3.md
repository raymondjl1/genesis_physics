# FIX LOG — Volume 3: Matter and Motion
**Date:** 2026-05-14  
**Scope:** Phase 1 (error corrections) and Phase 2 (honest labeling) per REVIEW_REPORT_Vol3.md

---

## Applied Fixes

| Chapter | Change | Reason |
|---------|--------|--------|
| Ch01 | No edits required — derivation chain explicit (zone action → geodesic → NR limit → Newton's 2nd Law, Eqs. 3.1.7–3.1.10 cited sequentially); problem set already present (Sets 1–3). | Reviewed against fix criteria; chapter already meets all Phase 1/2 requirements. |
| Ch02 | No edits required — problem set already present (§Problem Sets). | Reviewed against fix criteria; chapter already meets all Phase 1/2 requirements. |
| Ch03 | No edits required — numerical error percentages present for all results (Mercury 0.012%, Earth 0.011%, Moon 0.477% with explanatory note, tidal 0.066%); problem set already present (## Problems). | Reviewed against fix criteria; chapter already meets all Phase 1/2 requirements. |
| Ch04 | Expanded Chandler wobble disclosure at §4.5 (Torque-Free Precession section). Replaced one-sentence note with a blockquote explicitly stating the 41% discrepancy, its attribution to viscoelastic effects absent from rigid-body theory, the references (Munk & MacDonald 1960; Dahlen 1976) that close the gap to ~435 days, and the explicit statement that this is an expected limitation, not a falsification. | Per fix list: Chandler wobble result must be explicitly labeled with discrepancy magnitude, attribution, and falsification status. |
| Ch05 | No edits required — problem set already present (§5.10 Problem Set). | Reviewed against fix criteria. Note: superluminal sound speed issue flagged in review is a Phase 3 (polish) item not in Phase 1/2 fix list as specified in task instructions. |
| Ch06 | Added prominent BLOCKED status box at the start of §6.5 (Fermions from Vortices — The Jackiw-Rossi Mechanism). The box explains the circularity: the Jackiw-Rossi mechanism requires a pre-existing spinor field, but zone architecture is bosonic and the spinor is what needs to be derived. References Open Problem OP-1 (Vol 6 Ch 14). Notes that bosonic standing-wave results in the chapter are unaffected. | CRITICAL fix: GitHub #1 BLOCKER. Chapter was presenting spin-1/2 as derived when the derivation is circular. |
| Ch06 | Added dimensional verification note after E_η^(1) ≈ 1.9 GeV numerical result (§6.3). Note states the value requires verification and flags the factor-of-2.5 discrepancy identified by REVIEWER-17. | Per fix list: E_η^(1) value requires dimensional verification note before being cited. |
| Ch07 | Added PARAMETER DISCLOSURE blockquote immediately after the v_predicted = 246.2 GeV "Agreement" claim in §7.3 (The Vacuum Expectation Value). Disclosure explicitly states: α was chosen to match the VEV, so the VEV is a calibration not a prediction; W and Z masses are genuine predictions given the calibration but not independent confirmations; a true prediction requires deriving α from first principles. | CRITICAL fix: The "agreement better than 0.1%" claim was misleading — it is a calibration point. Required for scientific integrity per WHY-001 and MATH-013. |
| Ch07 | Added Assumption 10.1 parenthetical note immediately after the boxed fermion mass formula m_f = y_f v/√2 (Eq. 3.7.38). Note states the formula depends on Assumption 10.1 (spin-1/2 fermions from bosonic membrane) and references Open Problem OP-1. | Per fix list: fermion mass computations must be labeled as depending on Assumption 10.1. |
| Ch07 | Lepton mass ratio disclosures verified as already present: μ/e ~19% error (Eq. 3.7.46a), τ/μ ~23% error (Eq. 3.7.46c), τ/e <0.1% (Eq. 3.7.46b). No additional edit required. | Per fix list: verify disclosure present; it was. |
| Ch08 | No edits required — problem set already present (## Problem Set 8). | Reviewed against fix criteria. |
| Ch09 | Expanded the entropy production conductance L disclosure in §9.5.3. Added explicit units [k_B/s] to L definition; added "[units: W/K or equivalent — to be verified]" after the C_j definition; added Parameter Status blockquote stating L has not been computed from zone architecture and designating Research Task RT-3.L. | Per fix list: conductance L must be labeled as phenomenological; channel conductance units must be specified. |
| Ch09 | Added Research Task RT-3.κ note to the first technical definition of κ (in §9.3.2, bullet list defining κ(t)). Note explains that κ's precise microscopic definition relating it to the zone field equations is an open research item. | Per fix list: near first use of κ, add microscopic derivation pending note. |
| Ch10 | Verified Stefan-Boltzmann error percentage: 0.006% is present in the numerical validation table (line ~627). No edits required. Problem set already present (## Problems). | Reviewed against fix criteria; chapter already meets all Phase 1/2 requirements. |
| Ch11 | No edits required — problem set already present (## Problems). | Reviewed against fix criteria. |
| Ch12 | Added BLOCKER-level status correction box immediately before Eq. 3.12.48. Box states: the T-symmetry breaking term is a proposed ansatz, not a derived result; it is physically motivated but not derived from the 6D action; the arrow-of-time argument is conditional on this ansatz; designated Open Problem OP-ArT. | CRITICAL fix: Eq. 3.12.48 was already labeled "(proposed)" inline but the disclosure was insufficiently prominent for what is claimed (spontaneous T-symmetry breaking). |
| Ch12 | Added κ-mechanism research status note to the notation clarification box at the chapter opening. Note states that RT-3.κ (microscopic definition of κ) and RT-3.L (derivation of conductance L) are both open, and that entropy-rate predictions should be understood as order-of-magnitude estimates until these are resolved. | Per fix list: κ-mechanism should be consistently labeled as having microscopic derivation pending in Ch12, consistent with the note added in Ch09. |

---

## Chapters With No Changes Required

| Chapter | Reason |
|---------|--------|
| Ch01 | Derivation chain explicit; problem set present; mass postulation honestly disclosed with prominent note in §1.4 and §1.8. |
| Ch02 | Lagrangian/Hamiltonian derivation chain complete; problem set present. |
| Ch03 | Model chapter — preserved exactly. All numerical errors present; problem set present. |
| Ch05 | Problem set present. Superluminal sound speed is a Phase 3 item (add corrected formula) not required by the Phase 1/2 fix list. |
| Ch08 | Problem set present. Phase-transition disclosures (V_c 63.5% error, electroweak T_c 55% error) already present in chapter. |
| Ch10 | Stefan-Boltzmann error percentage (0.006%) present; problem set present. |
| Ch11 | Problem set present. |

---

## Summary of Critical Fixes

Three CRITICAL (near-fail) issues addressed:
1. **Ch06 §6.5** — Jackiw-Rossi BLOCKER: section now prominently warns readers the derivation is circular and is not complete.
2. **Ch07 §7.3** — Higgs VEV calibration: the 246.2 GeV "agreement" is now labeled as a calibration point, with W/Z masses correctly identified as predictions given the calibration.
3. **Ch12 §12.6** — T-symmetry breaking: Eq. 3.12.48 now has a prominent status box designating it as a proposed ansatz awaiting first-principles derivation (OP-ArT).

Two HIGH issues addressed:
4. **Ch09 §9.5.3** — Entropy conductance L: now labeled as phenomenological with Research Task RT-3.L assigned; channel conductance units specified.
5. **Ch07 §7.4** — Assumption 10.1 label added to fermion mass formula.

One MEDIUM issue addressed:
6. **Ch04 §4.5** — Chandler wobble: explicit 41% discrepancy note with references and falsification status.

---

*Fix log complete. All Phase 1 and Phase 2 items from REVIEW_REPORT_Vol3.md applied.*
