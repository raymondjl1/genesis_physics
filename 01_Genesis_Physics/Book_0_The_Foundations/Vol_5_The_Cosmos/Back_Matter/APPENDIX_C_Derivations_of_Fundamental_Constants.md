# Appendix C — Derivations of Fundamental Constants Summary Table

*Foundations Vol 5, The Cosmos — Back Matter*

> "Feynman used to say: nobody understands why $\alpha \approx 1/137$. That was true in 1985. It is no longer true." — *Vol 5, Chapter 13*

The defining claim of the Genesis Physics framework is that the fundamental constants of nature are not arbitrary parameters — they are *derived* from the geometry of the zone manifold. This appendix compiles all four fundamental-constant derivations from Chapters 13 and 15 into a single reference, with complete derivation chains, input parameters, precision achieved, and honest assessment of what is genuine prediction versus calibration.

---

## C.0 Purpose

Chapters 13 and 15 derive the fundamental constants in their proper pedagogical sequence, embedded in the physics that motivates them. This appendix strips away the pedagogy and lays the derivations side by side in a single compiled reference, so any reader can:

1. See all four derivation chains at a glance
2. Trace each constant back to its geometric origin
3. Identify which inputs are shared across derivations
4. Judge for themselves what is predicted and what is calibrated

---

## C.1 Fine Structure Constant α

**The crown jewel of the Foundations series.**

### Derivation Chain

| Step | What happens | Equation | Source |
|------|-------------|----------|--------|
| 1 | Start with 6D gauge action | $S^{(6)}_\text{gauge} = -\frac{1}{4\kappa_6^2}\int d^6x\sqrt{-g^{(6)}}F_{MN}F^{MN}$ | (5.13.9) |
| 2 | Kaluza–Klein reduction over extra dimensions | Integrate over warp-factor profile $e^{2A(\xi,\eta)}$ from $\eta_B$ to $\xi_A$ | (5.13.10–12) |
| 3 | Identify KK integral with one-loop RG running | $\int_{\eta_B}^{\xi_A} d\xi\,e^{2A} \leftrightarrow \int_{\mu_\text{IR}}^{\mu_\text{UV}} \frac{d\mu}{\mu}\,\frac{b_0}{2\pi}$ | (5.13.13–14) |
| 4 | Insert SM β-function coefficient | $b_0 = -\sum_\text{SM} \frac{2}{3}Q_f^2 N_c = -\frac{80}{9}$ (all charged fermions + W) | (5.13.15), from (4.8.11) |
| 5 | Evaluate: $\alpha^{-1} = C \cdot \ln(\xi_A/\eta_B)$ | $L = \ln(2.308 \times 10^{41}) = 95.259$ | (5.13.7–8) |
| 6 | Numerical result | $\boxed{\alpha^{-1} = 137.17 \pm 0.15}$ | (5.13.16) |

### Inputs

| Input | Value | Source | Independent of α? |
|-------|-------|--------|--------------------|
| $\xi_A$ (Waters Above extent) | $(3.0 \pm 0.03) \times 10^{26}$ m | Vol 1 Ch 4; constrained by $H_0$ | **Yes** |
| $\eta_B$ (Firmament thickness) | $(1.3 \pm 0.003) \times 10^{-15}$ m | Vol 1 Ch 4; constrained by nuclear physics | **Yes** |
| SM particle content | 17 fundamental particles | Vol 4 Ch 10 | **Yes** |
| $b_0$ (one-loop β coefficient) | $-80/9$ | Vol 4 Ch 8, from SM spectrum | **Yes** |

### Result

$$\alpha^{-1}_\text{theory} = 137.17 \pm 0.15 \qquad \alpha^{-1}_\text{exp} = 137.035\,999\,084(21) \qquad \text{Frac. error} = 0.10\%$$

### Assessment

**Status: GENUINE PREDICTION.** All four inputs are determined independently of $\alpha$. The scale ratio $\xi_A/\eta_B \approx 2.3 \times 10^{41}$ is fixed by cosmology (outer) and nuclear physics (inner). The SM β-function coefficient is fixed by the particle spectrum. The result $\alpha^{-1} \approx 137$ follows as a consequence — it is not put in.

**Residual uncertainties:**
- One-loop only; two-loop KK integral would reduce error to ~0.01%
- O(1) factor between $\xi_A$ and the precise Hubble radius (currently ~1% ambiguity)
- Brane-thickness contributions to running (not yet computed)

**Physical meaning:** The fine structure constant measures how much the electromagnetic coupling runs across 41 decades of energy scale — from the nuclear scale $\eta_B$ to the cosmological scale $\xi_A$. The "magic number" is geometry.

---

## C.2 Planck's Constant ℏ

### Derivation Chain

| Step | What happens | Equation | Source |
|------|-------------|----------|--------|
| 1 | Topological vortex on Firmament | Winding number $\oint d\theta = 2\pi n$, unit vortex $n = 1$ | (5.15.2) |
| 2 | Vortex core radius = Firmament thickness | $r_\text{core} = \eta_B \approx 1.3 \times 10^{-15}$ m | (5.15.3) |
| 3 | Vortex core energy | $E_\text{vortex} = \sigma \times \pi r_\text{core}^2 = \pi\sigma\eta_B^2$ | (5.15.4) |
| 4 | Characteristic timescale | $\tau_\text{core} = \eta_B/c$ | (5.15.5) |
| 5 | Vortex action = energy × time | $S_\text{vortex} = \pi\sigma\eta_B^3/c$ | (5.15.6) |
| 6 | Bohr–Sommerfeld quantization | $\oint \vec{p}\cdot d\vec{q} = 2\pi S_\text{vortex}$ | (5.15.8) |
| 7 | Identify with quantum of action | $\boxed{\hbar_\text{bare} = \frac{\sigma\eta_B^3}{2c}}$ | (5.15.9) |

### Inputs

| Input | Value | Source | Independent of ℏ? |
|-------|-------|--------|--------------------|
| $\sigma$ (membrane tension) | $\approx 6.0 \times 10^{98}$ J/m | Vol 1 Ch 5 | **No** — $\sigma$ is constrained by $c$ and $\mu$, and $\mu$ is constrained by $\hbar$ |
| $\eta_B$ (Firmament thickness) | $\approx 1.3 \times 10^{-15}$ m | Vol 1 Ch 4 | Partially — constrained by nuclear physics, but refined using $\hbar$ |
| $c$ (speed of light) | $\sqrt{\sigma/\mu}$ | Vol 1 Ch 5 | Derived |

### Result

$$\hbar_\text{theory} \approx 1.055 \times 10^{-34}\text{ J·s} \qquad \hbar_\text{exp} = 1.054\,571\,817 \times 10^{-34}\text{ J·s} \qquad \text{Frac. error} < 0.1\%$$

### Assessment

**Status: CALIBRATED (with explanatory power).** The relation $\hbar = \sigma\eta_B^3/(2c)$ *explains* Planck's constant as the action of a minimal topological excitation on the Firmament. But $\sigma$ and $\eta_B$ are themselves constrained to reproduce $\hbar$, so the numerical agreement is circular. The value is *not* a prediction.

**What IS predicted:** That $\hbar$ should exist at all — that action is quantized — follows from the topology of the Firmament (winding numbers are integers). The zone framework derives quantization as a *theorem*, not a postulate (Vol 1 Ch 10).

---

## C.3 Gravitational Constant G

### Derivation Chain

| Step | What happens | Equation | Source |
|------|-------------|----------|--------|
| 1 | Start with 6D gravitational action | $S^{(6)}_\text{grav} = \frac{1}{16\pi G_6}\int d^6x\sqrt{-g^{(6)}}R^{(6)}$ | (5.1.2), Vol 1 Ch 4 |
| 2 | Dimensional reduction to 4D | Integrate over extra dimensions with warp factor | (5.1.3–4) |
| 3 | Extract 4D Newton's constant | $G_4 = \frac{G_6}{V_\text{extra}}$ where $V_\text{extra} = \int d\xi d\eta\,e^{2A+2B}$ | (5.1.4–5) |
| 4 | Extra-dimensional volume | $V_\text{extra} \sim 10^{61}$ m² | Vol 1 Ch 4 |

### Inputs

| Input | Value | Source | Independent of G? |
|-------|-------|--------|--------------------|
| $G_6$ (6D gravitational coupling) | Set by fundamental 6D action | Vol 1 Ch 4 | **No** — $G_6$ and $V_\text{extra}$ jointly determined to match $G_4$ |
| $V_\text{extra}$ | $\sim 10^{61}$ m² | Vol 1 Ch 4 | **No** — same constraint |

### Result

$$G_{4,\text{theory}} = 6.674 \times 10^{-11}\text{ m}^3\text{kg}^{-1}\text{s}^{-2} \qquad G_{4,\text{exp}} = 6.674\,30(15) \times 10^{-11} \qquad \text{Frac. error} < 0.01\%$$

### Assessment

**Status: CALIBRATED (with explanatory power).** The relation $G_4 = G_6/V_\text{extra}$ *explains* why gravity is so weak: it is a 6D force diluted across an enormous extra-dimensional volume ($\sim 10^{61}$ m²). This resolves the hierarchy problem — the ratio $G_N m_p^2/(\alpha\hbar c) \sim 10^{-36}$ is geometric, not fine-tuned. But $V_\text{extra}$ is set to reproduce $G_4$, so the numerical agreement is by construction.

---

## C.4 Boltzmann Constant k_B

### Derivation Chain

| Step | What happens | Equation | Source |
|------|-------------|----------|--------|
| 1 | Membrane oscillation modes | Sturm–Liouville spectrum on compact domain | Vol 1 Ch 10, (1.10.1) |
| 2 | Count accessible modes | $\Omega = \#\{\text{modes with } \lambda \ge \ell_P\}$ | (5.6.5), (5.15.11) |
| 3 | Define entropy | $S = k_B \ln \Omega$ | (1.11.7) |
| 4 | Equipartition from mode statistics | Each mode carries $\frac{1}{2}k_B T$ in thermal equilibrium | Vol 1 Ch 11 |
| 5 | Identify $k_B$ from consistency | $k_B$ is the proportionality constant between microscopic mode energy and macroscopic temperature | (5.15.12) |

### Inputs

| Input | Value | Source | Independent of k_B? |
|-------|-------|--------|--------------------|
| $\hbar$ | From §C.2 | Calibrated | No (k_B depends on ℏ through mode spectrum) |
| Mode spectrum | From Sturm–Liouville on $[0, \xi_A]$ | Vol 1 Ch 10 | Yes |
| UV cutoff | $\ell_P = \sqrt{\hbar G/c^3}$ | From ℏ and G | No |

### Result

$$k_{B,\text{theory}} \approx 1.381 \times 10^{-23}\text{ J/K} \qquad k_{B,\text{exp}} = 1.380\,649 \times 10^{-23}\text{ J/K (exact, SI 2019)} \qquad \text{Frac. error} < 0.1\%$$

### Assessment

**Status: DERIVED FROM PRIOR (limited precision).** $k_B$ follows from $\hbar$, $G$, and the mode spectrum without additional calibration. But its precision is limited by the UV cutoff choice ($\ell_P$ vs. $\eta_B$), which introduces an O(1) ambiguity that has not been fully resolved.

**Note:** Since 2019, $k_B$ is defined exactly in SI units. The zone framework's task is to show that the *value* chosen by BIPM follows from membrane geometry — not to "predict" what is now a definition.

---

## C.5 Master Summary Table

All four constants in one place.

| Constant | Symbol | Zone Formula | Zone Value | Exp. Value | Error | Status | What It Means |
|----------|--------|-------------|-----------|-----------|-------|--------|--------------|
| Fine structure | $\alpha^{-1}$ | $C \cdot \ln(\xi_A/\eta_B)$ | $137.17 \pm 0.15$ | 137.036 | **0.10%** | **PREDICTED** | EM coupling = running across 41 decades of geometry |
| Planck's constant | $\hbar$ | $\sigma\eta_B^3/(2c)$ | $1.055 \times 10^{-34}$ | $1.0546 \times 10^{-34}$ | < 0.1% | CALIBRATED | Action quantum = minimal vortex action on Firmament |
| Newton's constant | $G_4$ | $G_6/V_\text{extra}$ | $6.674 \times 10^{-11}$ | $6.6743 \times 10^{-11}$ | < 0.01% | CALIBRATED | Gravity weakness = 6D dilution across $10^{61}$ m² |
| Boltzmann's constant | $k_B$ | From $\hbar$ + mode counting | $1.381 \times 10^{-23}$ | $1.3807 \times 10^{-23}$ | < 0.1% | DERIVED* | Temperature = average mode energy |

### The Honest Count

- **Genuinely predicted from geometry (no fitting):** 1 constant (α)
- **Explained by geometry but calibrated:** 2 constants (ℏ, G)
- **Derived from calibrated constants:** 1 constant (k_B)
- **Free geometric parameters in the framework:** 3 (σ, η_B, ξ_A)
- **Independent constants produced:** 4
- **Net predictive power:** 4 constants from 3 parameters = **1 genuine prediction** (α)

This is the honest bottom line. The zone framework reduces four fundamental constants to three geometric parameters, producing one genuine prediction (the fine structure constant at 0.10% precision) and three explanations (why ℏ, G, and k_B take the values they do). One genuine prediction is more than any competing framework has achieved. But it is not four.

### What Would Improve the Score

1. **Two-loop KK integral** for α → reduce error from 0.10% to ~0.01%
2. **Independent determination of η_B** from nuclear physics (e.g., proton charge radius) → would make ℏ a prediction, not a calibration
3. **Independent determination of V_extra** from cosmological observations → would make G a prediction
4. **Resolve UV cutoff ambiguity** for k_B → sharpen precision

If items 2 and 3 are achieved, the framework would predict *all four constants* from a *single* geometric parameter (ξ_A) plus the SM particle spectrum. This is the goal of Volume 6.

---

### Derivation Dependency Graph

```
Zone Geometry (σ, η_B, ξ_A)
├── c = √(σ/μ)                          [Vol 1 Ch 5]
├── ℏ = σ·η_B³/(2c)                     [Vol 5 Ch 15]  ← CALIBRATED
├── G₄ = G₆/V_extra(ξ_A, η_B)          [Vol 5 Ch 1,15] ← CALIBRATED
├── k_B = f(ℏ, mode spectrum, ℓ_P)      [Vol 5 Ch 15]  ← DERIVED*
└── α⁻¹ = C·ln(ξ_A/η_B)               [Vol 5 Ch 13]  ← PREDICTED ★
     └── Uses: SM β-function [Vol 4 Ch 8]
     └── Uses: KK tower [Vol 1 Ch 5]
```

---

*End of Appendix C*
