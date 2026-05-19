# Parameter Ledger — Foundations Vol 2

**Scope:** Volume 2 (Forces and Fields).
**Status:** LOCKED 2026-05-18 (B2 policy lock, Task 0516_Rev_130, Decision 4).
**Purpose:** Replace the headline "no free parameters" / "parameter-free" claim
with an explicit, honest accounting of every constant that is **fitted to data**
in or before Vol 2, what it was fit to, and which downstream numerical claims
inherit the fit.

This ledger is the single source of truth for parameter honesty in Vol 2. Every
numerical "prediction" in Vol 2 must be classified, by reference to this ledger,
as one of three things:

- **Prediction** — derivable from the framework with no free parameter fit to
  that quantity's value (or to a quantity from which it is algebraically
  inseparable).
- **Consistency Check** — recovered after fitting one or more free parameters;
  the agreement with experiment is then a self-consistency statement, not a
  parameter-free derivation.
- **Pending** — derivation remains open.

---

## 1. Fitted Constants Inventory

| # | Constant | Fitted in | Fit to | Downstream Vol 2 numbers that inherit the fit |
|---|---|---|---|---|
| 1 | **$L_\text{eff}$** ($\approx 8.96 \times 10^{-29}$ m) | Vol 2 Ch 2 §2.4.2 (Route 2) | Newton's gravitational constant $G_N = 6.674 \times 10^{-11}\,\text{m}^3\,\text{kg}^{-1}\,\text{s}^{-2}$ (CODATA 2018) | $G_4$ in Ch 2 §2.4.2 (Route 2); $\alpha_G$ in Ch 9 §9.3.3; hierarchy ratio $\alpha_\text{em}/\alpha_G$ in Ch 9 and Ch 11 §11.3.1; all gravitational predictions in Ch 8 that use $G_4$ numerically. |
| 2 | **$K$** (= $b_\text{eff}/(2\pi) \approx 1.4383$ in Vol 2 notation; $C_1$ in Ch 9) | Vol 4 (downstream — particle content) and Vol 5 Ch 13 (definitive). In Vol 2 Ch 3 §3.7.3 / Ch 9 §9.2 it is taken as anticipatory input. | The measured fine structure constant $\alpha^{-1} = 137.035999084$ (CODATA 2018), via $b_\text{eff}$ matched to SM particle content | $\alpha^{-1}$ in Ch 3 §3.7.4 (= 137.04); $\alpha^{-1}$ in Ch 9 Eq. (2.9.27) (= 137.0); hierarchy ratio $\alpha_\text{em}/\alpha_G$ in Ch 9 and Ch 11. |
| 3 | **$\lambda$** (warp exponent, = 41 in Vol 2) | Vol 1 Ch 4 §4.1.2: derived from the Waters Above field equation as the eigenvalue of the warp-factor ODE. **Status:** derived in Vol 1, not fitted — but the eigenvalue $\lambda = 41$ depends on the chosen boundary conditions of the Waters Above potential, and those boundary conditions were chosen by Vol 1 to recover the observed cosmological hierarchy. Vol 2 treats $\lambda$ as a Vol 1 input. | (Indirectly) cosmic hierarchy via the boundary conditions of $V(\Psi_A)$ in Vol 1 | $V_\xi$ in Ch 2 §2.3, $V_\text{extra}$, $G_4$, hierarchy ratio $10^{36}$ in Ch 9 §9.3 and Ch 11 §11.3.1. |
| 4 | **$B_0$** (= 28.8) and **$\xi_0$** ($\approx 60\,\ell_\text{Pl}$) and **$\kappa_6^2$** ($= 6.9 \times 10^{-66}\,\text{s}^2/\text{kg}$) | Vol 2 Ch 2 §2.4.3, **OP-G6 closure (Rev. 2026-05-15)** | Self-consistency: the triple ($B_0$, $\xi_0$, $\kappa_6^2$) is fixed by the KK reduction normalization plus the Israel junction condition such that Eq. (2.2.38) reproduces $G_4^\text{obs}$ at the 0.5% level. Functionally these are calibrated to $G_N$ jointly with $L_\text{eff}$. | $G_4$ Route 2 closure in Ch 2 §2.4.3; the "Route 1 = Route 2" agreement claim. |
| 5 | **$\eta_B$** ($\approx 1.3 \times 10^{-15}$ m) | Vol 1 Ch 4 + Vol 2 Ch 2 inputs (set by the nuclear confinement scale). **Status:** chosen to match the nuclear scale ($\Lambda_\text{QCD}^{-1}$); not derived. Vol 2 treats $\eta_B$ as a Vol 1 input. | Nuclear confinement scale (input) | $V_\eta$, $G_4$, $\sigma_\text{QCD}$ in Ch 4 §4.3, $\alpha^{-1}$ via $\ln(\xi_A/\eta_B)$ in Ch 3 and Ch 9, hierarchy ratio. |
| 6 | **$\xi_A$** ($\approx 3 \times 10^{26}$ m) | Vol 1 Ch 4 + B1 Rev_007 lock | Cosmological horizon scale (Hubble radius); chosen to match the observed cosmological extent. | $V_\xi$, $G_4$, $\alpha^{-1}$ via $\ln(\xi_A/\eta_B)$, hierarchy ratio. |

**Reading the table.** Entries 1, 2, and 4 are unambiguously fitted constants:
their numerical values are pinned by matching a measured 4D quantity. Entries
3, 5, 6 are Vol 1 inputs whose origins are either derived eigenvalues of Vol 1
field equations or scale choices fixed at Vol 1; Vol 2 treats them as given.
The framework's parameter honesty rests on the Vol 1 ledger for entries 3, 5,
6; the Vol 2 ledger covers entries 1, 2, 4.

---

## 2. Classification of Vol 2 Numerical Claims

Apply the **Derived vs Verified** template (Vol 2 Ch 9 §9.3.4):

### 2.1 Predictions (parameter-free relative to the Vol 2 ledger above)

- **Existence of exactly four forces** (Ch 1 §1.3, Theorem 2.1.1). Topological,
  no fitted constants.
- **Functional form of the hierarchy** $\alpha_\text{em}/\alpha_G \propto
  \xi_A^{1+\lambda}/\ln(\xi_A/\eta_B)$ (Ch 9 §9.3.6). Mechanism and scaling
  exponent, not the numerical value.
- **Mercury perihelion advance, light deflection, GW chirp masses** (Ch 8, Ch
  11 §11.3.3). These use $G_4$ numerically and therefore inherit the $L_\text{eff}$
  fit, but the ratios and the form of the predictions are pure GR consequences
  once $G_4$ is supplied; the agreement is a *consistency* of zone GR with
  standard GR, with $G_4$ as the shared input.
- **Dark matter direct-detection cross-section $\sigma_\text{SI} = 0$ exactly**
  (Ch 11 §11.5.4). Topological zero; no parameter to fit.
- **Dark energy equation of state $w = -1$ exactly** (Ch 11 §11.5).
- **GW speed = EM speed** (Ch 11 §11.3.2). Both propagate on the same
  Firmament membrane.
- **Five Principles → unique Lagrangian** (Ch 5, Theorem 2.5.1).
- **Desert prediction** (Ch 11 §11.4.3). No fitted constants.

### 2.2 Consistency Checks (per B2 Decision 4)

- **$G_4 = 6.674 \times 10^{-11}\,\text{m}^3/(\text{kg}\,\text{s}^2)$** (Ch 2
  §2.4.2 Route 2; Ch 11 §11.3.1). Recovered after fitting $L_\text{eff}$ (and
  the joint $B_0, \xi_0, \kappa_6^2$ triple) to $G_N$. **Demoted from
  Prediction.**
- **$\alpha^{-1} = 137.04$ (Ch 3) / $137.0$ (Ch 9)** (Ch 11 §11.3.1).
  Recovered after fitting $K = 1.4383$ in Vol 4 to the measured $\alpha^{-1}$.
  **Demoted from Prediction.**
- **Hierarchy ratio $\alpha_\text{em}/\alpha_G = 1.236 \times 10^{36}$** (Ch 9
  §9.3.3, Ch 11 §11.3.1). Inherits both $L_\text{eff}$ (via $\alpha_G$) and
  $K$ (via $\alpha_\text{em}$). **Consistency check.**
- **$\sigma_\text{QCD} \approx 0.18\,\text{GeV}^2/\text{fm}$** (Ch 4 §4.3).
  Uses the warp factor at $\eta_B$ and a normalization constant; precision
  inherits the warp profile and $\eta_B$.
- **$\alpha_s(M_Z) = 0.118$** (Ch 4 §4.2). The boundary overlap integral
  delivers the value at 1% only after the RG running is anchored at the
  measured $\alpha_s$; the precision is therefore a consistency check on the
  geometric mechanism, not a fully parameter-free prediction. (The
  *mechanism* — that $\alpha_s$ emerges from a $\mathbb{Z}_3$ boundary
  integral — is a prediction; the 1% numerical agreement is a consistency
  check.)
- **$\Omega_\text{DM} = 0.266$, $\Omega_\Lambda = 0.684$** (Ch 11 §11.3.2).
  Anchored by the Waters field potentials; whether these are predictions or
  consistency checks depends on how $V(\Psi_A)$, $U(\Psi_B)$ are calibrated in
  Vol 1 (see Vol 1 ledger). Vol 2 quotes them.

### 2.3 Pending

- **$\sin^2\theta_W$** (Ch 11 §11.3.1; Ch 4 §4.4). Tree-level zone geometry
  gives $\approx 0.13$; the measured 0.231 requires radiative corrections
  deferred to Vol 4. **Pending Vol 4.**
- **CP-violating phase $\delta_\text{CKM}$** (Ch 11 §11.7.1). Mechanism
  present, numerical value not derived. **Pending Vol 4.**
- **Two-loop precision on gauge running** (Ch 10, Ch 11 §11.7.1). Deferred to
  Vol 4.
- **Hadron mass spectrum, non-perturbative QCD** (Ch 4 §4.3, Ch 11 §11.7.1).
  Deferred to Vol 4 / Vol 6 lattice work.

---

## 3. Replaces "No Free Parameters" Headline

Across Vol 2, instances of "no free parameters" / "parameter-free" /
"zero free parameters" claims are replaced (per Task 130) by the more honest
statement:

> "No parameters are introduced in Vol 2 beyond those already calibrated in
> Vol 1 and those listed in the Vol 2 Parameter Ledger (`Back_Matter/Parameter_Ledger.md`).
> See the Ledger for the explicit accounting of $L_\text{eff}$, $K$, and
> $(B_0, \xi_0, \kappa_6^2)$ and the downstream numbers that inherit those fits."

---

## 4. Cross-References

- **B2 Policy Lock — Decision 4:** `Quality_Control/Reviews/0516_Rev_B2_POLICY_LOCK.md`
- **§9.3.4 Derived vs Verified template:** Ch 9 §9.3.4
- **§2.4.2 L_eff calibration note (now promoted to Preface-level statement in QUALITY_GATE.md):** Ch 2 §2.4.2 and `QUALITY_GATE.md`
- **Vol 2 warp profile canon:** `Source_Reference/Canonical_Warp_Profile.md`
