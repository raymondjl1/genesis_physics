# Vol 4 Back Matter — Phase 5 Reviewer Agent Pass

**Date:** 2026-04-09
**Scope:** Appendix A, Appendix B, Appendix C, Problem Sets, Bibliography
**Reviewers run:** 7 personas — Physicist, But-Why Reader, Writing Coach, Consistency Auditor, Skeptic, Student, Theologian
**Verdict:** PASS with 6 MINOR items logged; 0 BLOCKERS

---

## 1. Physicist (rigor, sign conventions, dimensional sanity)

**Overall:** PASS.

- **App C propagators:** Scalar, Dirac, photon (Feynman gauge), massive vector, gluon, and ghost propagators carry correct iε prescription and momentum-space signs under the (−,+,+,+) convention declared in §C.1. No sign errors located.
- **App C QED vertex:** $-ie\gamma^\mu$ matches the sign of the Dyson-series factor used in Ch 7 §7.6 Feynman rulebook. Consistent.
- **App C QCD:** Quark-gluon $-ig_s\gamma^\mu T^a$, 3-gluon $-g_s f^{abc}$ with correct cyclic momentum convention, 4-gluon with the three $f\cdot f$ pairings. Ghost coupling carries the correct sign for Feynman-gauge cancellation of unphysical gluon polarizations.
- **App C EW:** W charged-current $-i(g/\sqrt{2})\gamma^\mu(1-\gamma^5)/2$, Z neutral-current $-i(g/\cos\theta_W)\gamma^\mu(g_V-g_A\gamma^5)$. Standard PDG forms. Yukawa carries the $-i m_f/v$ coupling consistent with Ch 11 §11.5.
- **App B fractional errors:** Verified by spot-check that reported residuals in B.4–B.8 are computed as $|{\rm pred}-{\rm exp}|/{\rm exp}$ consistently. The 1000× neutrino disclosure in §B.8 is dimensionally honest (it is stated as a ratio of absolute masses, not of mass-squared splittings — the mixing data in §B.9 has its own small-error row, correctly separated).
- **MINOR P1:** App C §C.7 symmetry-factor convention should explicitly say "divide by |Aut(G)|" rather than the loose phrasing "divide by the appropriate combinatorial factor." Not a correctness issue — a clarity issue. **Logged, defer to pre-publication pass.**

## 2. But-Why Reader

**Overall:** PASS.

- Every row in App B §B.4–B.9 that is called a "prediction" can be traced to a Vol 4 chapter via the Status class; every row called CALIBRATION is explicitly flagged as a fit, not a test.
- App C rules all back-reference to the Ch where they are derived (Ch 7 for QED structure, Ch 11 for EW, Ch 12 for QCD).
- **MINOR BW1:** Appendix A §A.3.5 (running couplings) should add a one-line "why does this matter for Vol 4?" pointer to Ch 8 (renormalization) beyond the reverse-index row. **Logged, defer.**

## 3. Writing Coach

**Overall:** PASS.

- Voice is appropriately terse for back matter — not the hortatory voice of chapter text, closer to the "reference desk" tone of Vol 3 App A.
- **MINOR WC1:** Bibliography symbol legend (📜 📘 ⚛ ⚙ ☷) appears once at the head of R.1; should be repeated at the head of the file (front-matter block) so a reader jumping to R.7 can decode the glyphs without scrolling. **Logged, defer.**

## 4. Consistency Auditor

**Overall:** PASS.

- Notation cross-checked with Vol 1 App B (ξ, η, ξ_A, η_B, Firmament, Waters Above/Below). Consistent.
- Equation-tag convention (V.Ch.Eq) used uniformly across App A §A.5 reverse index.
- Status class labels are spelled identically across §B.0, §B.4–B.9, and §B.10.
- **MINOR CA1:** Problem set P4.7.3 uses lowercase "alpha" in prose but "α" in the equation. Harmonize to α throughout. **Logged, defer.**

## 5. Skeptic (adversarial)

**Overall:** PASS (honesty strong).

- **Challenge 1:** "Does App B hide bad predictions?" — No. §B.8 (neutrinos) and §B.10 (headline honesty) put the worst failures in the reader's first two passes through the file. The 1000× neutrino error and the spin-½ blocker are impossible to miss.
- **Challenge 2:** "Does the electron $g-2$ row (§B.3) appear to be a framework prediction when it is in fact a universality argument, per Ch 7 §7.9?" — §B.3's reading note explicitly flags the caveat and cross-references Ch 7. Acceptable.
- **Challenge 3:** "Does the apparent 5% quark-mass agreement mislead?" — §B.5's "Warning: the apparent agreement is inflated" box addresses this head-on. Acceptable.
- **Challenge 4:** "Are the problem-set challenge tiers honest about unsolved problems or do they dress up research as homework?" — P4.14.3 explicitly asks the student to graph the dependency DAG of the OPEN problems, which is the right framing (the research is exposed as research).
- **No blocker from Skeptic.** This is the appendix where an adversarial reader has the most leverage, and §B.10's headline honesty survives the attack.

## 6. Student (new reader, building the framework up)

**Overall:** PASS.

- Problem set tier labels (★ ★★ ★★★) match the difficulty curve established by the Vol 3 problem sets.
- Selected solutions (P4.2.3, P4.4.2, P4.7.3, P4.10.4, P4.14.3) are the five problems a first-pass reader is most likely to get stuck on. Good curation.
- **MINOR ST1:** Chapter 8 (renormalization) problem set has only 3 problems; the student-reviewer persona would like one more ★ basic problem walking through dimensional regularization of a single diagram in explicit steps. **Logged, defer — not a blocker because Ch 7 already carries P4.7.3 Schwinger g-2 as worked solution.**
- **MINOR ST2:** App A §A.5 reverse index should add a one-line legend at the top saying "read this as: Vol 4 Ch X uses equation (V.Y.Z)." **Logged, defer.**

## 7. Theologian (Christ-is-the-answer without preaching)

**Overall:** PASS.

- None of the five back-matter files contain preaching. The theological frame is present only where it is load-bearing for the physics (e.g. zone architecture ↔ Firmament/Waters labels in App A). Back matter is the right place for this posture — reference material should read as reference material.
- No items logged.

---

## 8. Items summary

| ID | Severity | Location | Action |
|---|---|---|---|
| P1 | MINOR | App C §C.7 | Tighten symmetry-factor language to "divide by |Aut(G)|" |
| BW1 | MINOR | App A §A.3.5 | Add one-line forward pointer to Ch 8 |
| WC1 | MINOR | Bibliography head | Repeat symbol legend at top of file |
| CA1 | MINOR | Problem set P4.7.3 | Harmonize α notation |
| ST1 | MINOR | Problem set Ch 8 | Add ★ basic dim-reg problem |
| ST2 | MINOR | App A §A.5 | Add reader legend for reverse-index rows |

**Blockers:** 0.
**Minors:** 6 (all deferrable to the Vol 4 pre-publication pass, consistent with how Ch 12's 14 minors were handled).

## 9. Phase 5 verdict

**PASS.** All seven reviewer personas return non-blocking. The back matter is verified conditional on the six minors logged above. Proceed to Phase 6 (Finalize) and update `QUALITY_GATE.md`.
