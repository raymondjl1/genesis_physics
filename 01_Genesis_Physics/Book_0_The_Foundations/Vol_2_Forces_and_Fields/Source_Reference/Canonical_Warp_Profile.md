# Canonical Warp Profile — Vol 2 Reference Card

**Scope:** Volume 2 (Forces and Fields).
**Status:** LOCKED 2026-05-18 (B2 policy lock, Task 0516_Rev_129).
**Upstream canon:** Vol 1 Ch 4 §4.1.2, derivation tag **RT-1.WF**.

---

## 1. The Canonical Form

The leading-order solution of the 6D Einstein equations on the Firmament slice,
derived in Vol 1 Ch 4 §4.1.2 (RT-1.WF), is

$$
A_\eta(\eta) \;=\; B_0 \;-\; \frac{\eta}{\eta_B},
\qquad
B_\eta(\eta) \;\approx\; \text{const}.
$$

That is: the four-dimensional warp factor $A_\eta$ is **linear in $\eta$**, so the
metric warp factor $e^{2A_\eta(\eta)} = e^{2B_0}\,e^{-2\eta/\eta_B}$ **decays
exponentially** with decay length $\eta_B$. The transverse-metric warp $B_\eta$ is
approximately constant on the Firmament slice.

**Numerical values (Vol 1 canon):**

| Symbol | Value | Source |
|---|---|---|
| $B_0$ | $28.8$ | Vol 1 Ch 4 §4.1.2 (RT-1.WF); also Vol 2 Ch 2 §2.4.3 (Rev. 2026-05-15, OP-G6 closure) |
| $\eta_B$ | $\approx 1.3 \times 10^{-15}$ m | Vol 1 Ch 4 (Waters Below extent); Vol 2 throughout |

---

## 2. Reconciliation with Earlier Vol 2 Forms

Several Vol 2 chapters were drafted before RT-1.WF closed and use different
functional forms for the same dimension. The canonical form above is now in
force; the earlier forms are either equivalent reparameterisations or
leading-order Taylor expansions of the canonical form near $\eta = 0$:

| Chapter | Form previously used | Status |
|---|---|---|
| Ch 2 §2.1.3 | $B_\eta(\eta) = B_0 - \gamma\eta/2$ (exponential / linear-in-$\eta$ with $\gamma = 2/\eta_B$) | **Equivalent** to canonical with $\gamma = 2/\eta_B \approx 1.5\times 10^{15}\,\text{m}^{-1}$ (the earlier label $\gamma = 10^{15}\,\text{m}^{-1}$ is the same form up to the factor-of-two convention; the warp factor $e^{2A_\eta}$ decays exponentially in either case). |
| Ch 4 §4.2 | $B(\eta) = -\gamma^2 \eta^2/2$ (Gaussian) | **Leading-order Taylor expansion** of the canonical form near $\eta = 0$: $A_\eta \approx B_0 - \eta/\eta_B + \mathcal{O}(\eta^2)$, so $e^{2A_\eta} \approx e^{2B_0}(1 - 2\eta/\eta_B + 2\eta^2/\eta_B^2 - \ldots)$. The quadratic term is the small-$\eta$ approximation that produces the manifest threefold orbifold structure in §4.2; it is **not a distinct canon**. |
| Ch 6 §6.3.2 (and Ch 6 §6.4.x referring to "1.4.27") | $B_\eta(\eta) = -\gamma^2\eta^2/2$ (Gaussian, citing 1.4.27) | **Same Gaussian = leading-order expansion of canonical**, retained only because the $\mathbb{Z}_2$ orbifold reflection $\eta \to -\eta$ at the Firmament is manifest in the symmetric Gaussian form. |
| Ch 9 §9.2 | references warp factor profile generally; uses $V_\eta \sim 1/\gamma$ | **Compatible**: the canonical $V_\eta = \int_0^{\eta_B} e^{-2\eta/\eta_B}\,d\eta = (\eta_B/2)(1 - e^{-2})$ has the same $\sim \eta_B$ scaling as the earlier $1/\gamma$ estimate. |
| Ch 11 §11.1.1 | $B_\eta(\eta) = -\eta^2/(2\eta_B^2)$ (step / near-zero quadratic) | **Same leading-order Taylor expansion** as Ch 4; valid only near $\eta = 0$. |

**Bottom line:** All five Vol 2 forms reduce to the canonical linear form
$A_\eta(\eta) = B_0 - \eta/\eta_B$ at leading order. The exponential-warp-factor
form (Ch 2) is exact; the Gaussian (Ch 4, Ch 6 §6.3.2) and the step/quadratic
(Ch 11) forms are small-$\eta$ Taylor expansions, valid in a neighbourhood of
the Firmament slice and used in those chapters because the symmetry of the
Taylor expansion makes the relevant orbifold structure manifest.

---

## 3. Open Problem Status

**OP-2.WP (Vol 2 warp profile reconciliation):** **CLOSED** 2026-05-18 by adoption
of the Vol 1 canon RT-1.WF. The four previously inconsistent forms in Vol 2 Ch 2,
Ch 4, Ch 9, and Ch 11 are reconciled as documented in §2 above. The locked
canonical form for all Vol 2 derivations going forward is
$A_\eta(\eta) = B_0 - \eta/\eta_B$ with $B_0 = 28.8$, $\eta_B \approx 1.3$ fm.

---

## 4. Downstream Numerical Inheritance

All $V_\eta$-dependent numerical results in Vol 2 (including $G_4$ in Ch 2 §2.4,
the hierarchy ratio $\alpha_\text{em}/\alpha_G$ in Ch 9, $\alpha_s(M_Z)$ in
Ch 4 §4.2, $\sigma_\text{QCD}$ in Ch 4 §4.3, and the dark-matter density
$\Omega_\text{DM} = 0.266$ in Ch 11) inherit the leading-order linear warp
profile. The numerical values quoted in those chapters were originally computed
under the Gaussian or step approximation; under the canonical exponential warp
factor they shift by $\mathcal{O}(\gamma\eta_B) \approx \mathcal{O}(1)$
corrections in the integrand, which integrate to corrections of the same order
in $V_\eta$. A downstream audit (not in scope of Task 129) is required if
chapter-level precision better than $\sim 30\%$ is claimed for any of these
quantities; the qualitative conclusions (gravity is weak, $\alpha^{-1} \approx
137$, $\sigma_\text{QCD} \sim 0.18\,\text{GeV}^2/\text{fm}$) are robust.

---

## 5. Cross-References

- **Vol 1 Ch 4 §4.1.2** — RT-1.WF derivation of $A_\eta(\eta) = B_0 - \eta/\eta_B$
  from the 6D Einstein equations.
- **Vol 2 Ch 2 §2.1.3, §2.4.3** — gravitational application; $B_0 = 28.8$
  numerical closure (Rev. 2026-05-15, OP-G6).
- **Research/Foundations/WARP_FUNCTION_DERIVATION_RT1WF.md** — full derivation,
  including the explicit integration of $V_\text{extra}$ used in Vol 2 Ch 2 and
  Ch 9.
- **Research/Foundations/METRIC_6D_SOLUTIONS.md §3.4.1** — six-dimensional
  solutions log, RS-type leading-order.
