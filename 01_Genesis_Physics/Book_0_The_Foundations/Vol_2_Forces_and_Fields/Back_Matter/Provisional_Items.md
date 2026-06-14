# Provisional Items Register — Foundations Vol 2

**Scope:** Volume 2 (Forces and Fields).
**Status:** Honesty register (companion to `Parameter_Ledger.md`).
**Purpose:** Enumerate every **[Provisional]** block in Vol 2 in one place — what is
flagged, where it lives, and the open problem it depends on — so a reader (or
reviewer) can see at a glance which results carry a provisional caveat and why.

This register is modeled on the Parameter Ledger honesty system. Where the
Parameter Ledger answers *"which constants are fitted to data?"*, this register
answers *"which derivations are flagged Provisional, pending an open problem?"*

---

## 1. The single open problem behind every Provisional block

Every **[Provisional]** block currently in Vol 2 traces to **one** open problem:

> **Open Problem 1.WF (warp functions).** The warp functions $A(\xi,\eta)$ and
> $B(\xi,\eta)$ in the 6D metric (Eq. 1.4.2) are not yet derived from the 6D
> Einstein equations (Ch 5, Eq. 2.5.22) self-consistently in closed form. The
> Vol 1, Ch 4 solutions are **approximate backgrounds**, not yet self-consistent
> solutions with the full stress-energy (Ch 5, Eq. 2.5.23). Until OP 1.WF is
> resolved, every coupling-constant integral that passes through a warp-factor
> integral inherits Provisional status.

These warp functions are the load-bearing input for every coupling-constant
integral in the volume. The **Provisional-cascade rule** (Ch 1 §1.2.3, the block
at Ch01 line 193) states the consequence formally: *any* downstream numerical
result that passes through a warp-factor integral is Provisional until OP 1.WF
is resolved — in particular $G_4$ (Ch 2, Ch 9), $\alpha^{-1}$ (Ch 3), and the
nuclear couplings (Ch 4).

**What is _not_ Provisional** (per the same cascade rule): the geometric
*mechanism* (forces as projected geometry, the logarithmic form of
$\alpha^{-1}$, the volume-dilution origin of the hierarchy) and the topological
force *count*. None of these depends on the detailed warp profile.

---

## 2. Register of [Provisional] blocks

| # | Chapter | Section | Line | What is flagged | Depends on |
|---|---------|---------|------|-----------------|------------|
| 1 | Ch 1 (Why Forces Exist) | §1.2.1 The Decomposition | 137 | The 6D metric (Eq. 1.4.2): warp functions $A(\xi,\eta)$, $B(\xi,\eta)$ not yet derived from the 6D Einstein equations. | OP 1.WF |
| 2 | Ch 1 (Why Forces Exist) | §1.2.3 The Coupling Constants from Geometry | 191 | The warp functions used in the coupling-constant integrals are not yet derived from the 6D Einstein equations. | OP 1.WF |
| 3 | Ch 1 (Why Forces Exist) | §1.2.3 (Provisional-cascade rule) | 193 | Volume-wide rule: every downstream number passing through a warp-factor integral inherits Provisional status ($G_4$, $\alpha^{-1}$, nuclear couplings). | OP 1.WF |
| 4 | Ch 2 (Gravity from Zone Curvature) | §2.1.2 The Metric Ansatz | 59 | Warp functions $A(\xi,\eta)$, $B(\xi,\eta)$ not yet derived from the 6D Einstein equations. | OP 1.WF |
| 5 | Ch 5 (The Zone Lagrangian) | §5.2.2 The 6D Einstein Equations | 319 | The Vol 1 Ch 4 warp solutions are approximate backgrounds; the self-consistent solution with the full stress-energy (Eq. 2.5.23) is open. All coupling integrals and numerical predictions in the chapter that depend on $A(\xi,\eta)$ or $B(\xi,\eta)$ are provisional. | OP 1.WF |
| 6 | Ch 6 (Gauge Theory from Zone Symmetries) | §6.1 Why Gauge Theory? (zone setup) | 33 | Warp functions $A(\xi,\eta)$, $B(\xi,\eta)$ not yet derived from the 6D Einstein equations in closed form. | OP 1.WF |

*(Line numbers are against the `*_DRAFT.md` manuscript files as of 2026-06-13 and
should be re-verified after any major reflow.)*

---

## 3. Relationship to the Parameter Ledger

The two registers are complementary and partly overlapping:

- The **Parameter Ledger** classifies each numerical claim as **Prediction /
  Consistency Check / Pending** based on *which constants were fitted to data*.
- This **Provisional Items Register** flags each derivation that is *contingent
  on an unresolved open problem* (currently all OP 1.WF).

A result can be both a **Consistency Check** (because it uses a fitted constant
such as $L_\text{eff}$ or $\eta_B$) **and** Provisional (because it passes
through a warp-factor integral). For example, $G_4$ in Ch 2 §2.4.2 is a
Consistency Check (it inherits the $L_\text{eff}$ fit, Parameter Ledger entry 1)
*and* Provisional (it passes through a warp-factor integral, this register
items 1–5). Neither status is removed by the other; both caveats stand until
their respective open items close.

---

## 4. Closure condition

When **OP 1.WF** is resolved — i.e., when $A(\xi,\eta)$ and $B(\xi,\eta)$ are
derived self-consistently from the 6D Einstein equations and shown to match (or
correct) the approximate Vol 1 Ch 4 backgrounds — **every** block in §2 of this
register clears simultaneously, and the cascade rule (item 3) is retired. Until
then, the numerical *agreement* of the affected couplings with experiment is
contingent on the derived warp functions matching the approximate backgrounds
used here.

---

*Honesty register. Single source of truth for Provisional status in Vol 2.
Companion to `Parameter_Ledger.md`. For the open-problem definition, see Ch 5
§5.2.2 (OP 1.WF) and the Vol 2 open-problems tracker.*
