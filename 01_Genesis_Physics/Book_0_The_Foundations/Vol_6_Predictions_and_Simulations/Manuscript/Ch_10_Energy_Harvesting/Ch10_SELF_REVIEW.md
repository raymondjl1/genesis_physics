# Ch 10 Self-Review

**Date:** 2026-04-17
**Draft under review:** `Ch10_DRAFT.md` (13,520 words)
**Status:** GREEN with action items

---

## Requirements check

| Req ID | Requirement | Status | Evidence / Note |
|---|---|---|---|
| Ch10-001 | Derive MRG from Firmament mechanics (V.1.5) and Dynamic Casimir Effect | MET | §10.5.2 (TE₁₁ derivation), §10.5.3 (dynamic-Casimir boundary), §10.5.6–§10.5.7 (gross-power derivation) |
| Ch10-002 | Number every prediction P-XXX beginning P-103 | MET | P-103 through P-118 numbered contiguously, each with source and falsification threshold |
| Ch10-003 | Gross / net / waste with dimensional checks | MET | §10.5.7 (10.5.8 with explicit dimensional check), §10.5.8, §10.5.9 (10.5.11) |
| Ch10-004 | Thermodynamic consistency; external reservoir named | MET | §10.10 entire; Eq (10.10.1); P-118 bounds sustainable rate |
| Ch10-005 | Observable signatures distinguishing framework from QED | MET | §10.8 five tests; Tests 3, 4, 5 are specific framework-vs-QED signatures |
| Ch10-006 | Engineering pathway Phase 1 → 4 with cost and TRL | MET | §10.9 four phases with gate criteria and timeline |
| Ch10-007 | All four methods covered | MET | §10.5 (MRG), §10.6 (Waters-field), §10.7 (vacuum & zone-boundary) |
| Ch10-008 | Cochlea as biological existence proof | MET | §10.4 entire; OAE discussion at §10.4.4 |
| Ch10-009 | Define η; derive compatibility with Second Law | MET | §10.3.4 (definition), §10.10 (compatibility) |
| Ch10-010 | Run energy_harvesting_simulation.html and quote its outputs | PARTIAL | Simulation values (118.7 W gross, 30–65 W net, 73 °C case, 1.14 GHz TE₁₁, 50 nm gaps, 200 boundaries, K^(1/3) vs K^(1/2)) are all quoted and consistent with the HTML; simulation was not *re-run* this session — the published HTML outputs were used as ground truth. Action item: log this as a reproducibility note in the revision pass. |
| Ch10-011 | Five falsification tests with quantitative thresholds | MET | §10.8.1–§10.8.5 each with pass/fail in §10.8.6 |
| Ch10-012 | FTL energy handoff to Ch 9 | MET | §10.9.5 handoff table |
| Ch10-013 | Distinguish derived from speculative | MET | §10.4.5 (cochlea proves / does not prove), §10.6.5 (Waters-sail not tabletop), §10.7.4 (zone-boundary risk) |
| Ch10-014 | 40–50 pages (25k–32k words) | **NOT MET** | 13,520 words = ~22 pages at 600 wpp or ~27 pages at 500 wpp. Flagged as PRIMARY ACTION ITEM below. |

---

## Universal checks

- [x] "But why?" chain is explicit in §10.3, §10.5, §10.6, §10.7, §10.10
- [x] No forward dependencies: every cited result is from Vols 1–5 or Ch 1–9
- [x] Notation table included at end; consistent with Series Bible
- [ ] Word count 25k–32k: **MISS — 13.5k**
- [x] No `[TODO]` markers remain
- [x] Every figure placeholder has a matching inline specification

## Foundations-specific checks

- [x] Every derivation starts from previously established results (equation numbers cited: V.1.5, V.4.9, V.5.11, V.5.2, Ch 9 P-089..P-102)
- [x] Problem set covers full difficulty range (5 computational, 5 conceptual, 3 challenge — §10.11.4)
- [ ] Solutions written for all problems: **NOT IN DRAFT** — problems are listed but solutions not appended. Action item.
- [x] Every prediction numbered P-XXX with falsification threshold
- [x] Thermodynamic consistency verified for every positive-η claim
- [x] Simulation results quoted with source-of-truth values from `energy_harvesting_simulation.html`

---

## Action items (prioritised for revision)

1. **Expand to 25k–32k words** (add ~12k words). Highest-priority targets for expansion:
   - §10.3: more rigorous treatment of the open-system thermodynamics (+2k words) — add stat-mech bookkeeping with explicit free-energy accounting.
   - §10.5: additional engineering depth (+3k words) — derive TE₁₁ mode structure from first principles rather than citing x'_{11}; expand thermal model with radiation/convection split; expand rectenna impedance matching analysis.
   - §10.6: full derivation of Waters-sail extraction with explicit choice of gauge (+2k words); explicit integration of expansion-sail yield over realistic Ψ_A profile.
   - §10.7: expand Casimir-array scaling derivation (+1.5k words); expand zone-boundary Landau-Ginzburg-style analysis.
   - §10.8: add instrumentation appendix with specific part numbers and calibration procedure (+1k words).
   - §10.9: add staffing estimates and institutional-requirements subsection (+500 words).
   - §10.10: formal entropy-balance derivation with temperature and chemical-potential analogues for the reservoirs (+2k words).

2. **Add problem-set solutions** (3–5 pages) — draft provided problems but no worked solutions. Required by Foundations-specific verification criterion.

3. **Add reproducibility note** documenting (i) which numerical values came from `energy_harvesting_simulation.html` (all quoted values) vs. (ii) which are computed fresh in this chapter (dimensional checks, thermal budget, dielectric scaling), and (iii) the exact commit hash / version of the simulation at the time of quoting. This is a Vol-6-standard.

4. **Strengthen `P-118` derivation** — the sustainability-rate bound is presented with order-of-magnitude estimates; the Skeptic will want a closed-form accounting. Options: (a) add a subsection deriving κ_eff from first principles; (b) flag it as an open problem (Ch 14 #8) in a footnote and leave the order-of-magnitude treatment — which is defensible but less satisfying.

5. **Cochlea analogy — anticipate Theologian objection**. Current §10.4.7 is brief. Expand: make explicit that the Romans 1:20 framing is a *motivation* for looking for the MRG architecture in the Firmament, not a *proof* that it's there. Clarify that the argument doesn't depend on the theology; the theology explains why the architecture recurs.

6. **Add "what if Test 1 fails" subsection** (§10.8.6 or §10.11.5). If η = 0 experimentally, what is the salvageable content of the chapter? (Answer: all of the derivations stand as standard QED calculations; only the framework-specific interpretation changes; Waters-field and zone-boundary engineering become inaccessible.) This is the honest assessment the Skeptic will demand.

7. **Dark-energy flux sensibility check.** In §10.10.2, the `κ_eff ~ 10⁻³⁶ W/m²` order-of-magnitude looks small against the device's per-cavity-wall-area output. Recompute with the mode-volume treatment rather than surface-area treatment; confirm the bookkeeping closes, or rewrite that subsection with a clearer derivation.

---

## Strengths worth preserving

- The prediction catalogue is complete and falsifiable — P-103 through P-118 each has a numeric threshold.
- The handoff to Ch 9 (§10.9.5 table) is clean and defensible.
- The cochlea framing is structurally robust — it survives being factored out of the theological interpretation.
- The `$150 decides the framework` claim is explicit, cheap, and repeatable.
- Thermodynamic bookkeeping is stated as the chapter's governing rule at §10.1.3 and cashed out at §10.10.
- The four-stage spine (SELECT/DISRUPT/DIRECT/HARVEST) ties the cochlea, MRG, and falsification tests together.

## Overall verdict

**GREEN with two required actions:** (i) expand to target word count; (ii) add problem-set solutions. No RED flags on content, derivation, or thermodynamic consistency. Physicist should find no dimensional errors. Skeptic should find no unfalsifiable claims. Theologian-flag items are confined to §10.4.7 and §10.11.6 and are bounded.

Recommend: proceed to Phase 5 (reviewer agents) with the current draft and flag word-count + solutions as the two required revisions before Finalize.
