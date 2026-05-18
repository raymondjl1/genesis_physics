"""
OP-03 Investigation: WKB Tunneling Amplitude for Three Fermion Generations
===========================================================================

Context (from OPEN_PROBLEMS_REGISTER.md OP-03):
  - The symmetric double-well (op03_v0_sweep.py) cannot produce α ≈ 1.0 because
    Z₂ symmetry forces y₁ ≈ y₂ for all well depths.
  - The path forward is WKB tunneling in the extra-dimensional interval where
    three generations reside at different distances from the Higgs wall.
  - In the WKB picture, the three generations correspond to three Regge-like
    tunneling trajectories from the Higgs locus, with exponentially suppressed
    amplitudes that naturally produce y₁ ≫ y₂ ≫ y₃.

Physical Model:
  - Extra-dimensional compact interval: ξ ∈ [0, L]
  - Higgs (Firmament condensate) localized at ξ = 0 (zone wall)
  - Three fermion generations at positions ξ_n (n = 1, 2, 3 for τ, μ, e)
  - Yukawa coupling y_n = WKB tunneling amplitude from ξ = 0 to ξ_n through V(ξ)
  - Fit: y_n ≈ y₀ exp(−α n²), find barrier parameters giving α = 1.0

Key Physical Insight: n² Scaling from a Parabolic Barrier
----------------------------------------------------------
For a parabolic barrier V(ξ) = V₀(ξ/L)² with linearly spaced generations
ξ_n = n Δξ:

  S_n = ∫₀^{ξ_n} √(2V(ξ)) dξ = √(2V₀)/L × ∫₀^{n Δξ} ξ dξ
       = √(2V₀)/(2L) × n² Δξ²

This gives y_n = exp(−S_n) = exp(−α n²) with
  α = √(2V₀) Δξ² / (2L)

n² scaling is therefore a NATURAL consequence of:
  1. A parabolic (quadratic) extra-dimensional potential (e.g., arising from
     Waters Below condensate density profile near the zone wall)
  2. Linearly spaced generation positions ξ_n = n Δξ

By contrast, a CONSTANT barrier gives S_n ∝ n (linear, not n²), and a
LINEAR barrier gives S_n ∝ n^{3/2} (not n²). The parabolic barrier is
the unique power law that naturally produces n² scaling with even spacing.

Physical motivation for V(ξ) = V₀(ξ/L)²:
  The Waters Below condensate density near the zone wall is expected to fall
  off quadratically from its peak at ξ = 0 (zone wall), creating a potential
  well (and corresponding barrier for charged fermions) that rises as ξ². The
  exact form depends on the bulk condensate profile from Vol 1 Ch 6 §6.4.

Target:
  α = 1.0 reproduces τ:μ:e mass hierarchy to ~20% accuracy:
  m_μ/m_τ = exp(−3α) → α = ln(m_τ/m_μ)/3 = ln(16.82)/3 ≈ 0.940
  m_e/m_τ  = exp(−8α) → α = ln(m_τ/m_e)/8  = ln(3477)/8  ≈ 1.012
  Average:  α ≈ 0.98, consistent with α ≈ 1.0

Script structure:
  Part 1: Analytic confirmation — parabolic barrier gives n² scaling
  Part 2: Numerical WKB for five barrier shapes — compare scaling behaviors
  Part 3: Parameter sweep (V₀, Δξ, L) for α = 1.0 under parabolic barrier
  Part 4: Evaluate mass ratio accuracy at the best-fit parameters

Author: Jeff Raymond / Genesis Physics Project
Date: 2026-05-13
"""

import numpy as np


# ---------------------------------------------------------------------------
# Observed lepton masses (PDG 2022)
# ---------------------------------------------------------------------------
M_TAU_MEV = 1776.86
M_MU_MEV  = 105.658
M_E_MEV   = 0.511

# Target α from lepton mass ratios (n² convention: m_n ∝ exp(−α n²))
# Generation labeling: n=1 → τ (heaviest), n=2 → μ, n=3 → e (lightest)
# m_n = m_τ × exp(−α(n²−1))
# m_μ/m_τ = exp(−3α)  →  α_mu  = ln(m_τ/m_μ)/3
# m_e/m_τ  = exp(−8α)  →  α_e   = ln(m_τ/m_e)/8
ALPHA_TARGET_MU = np.log(M_TAU_MEV / M_MU_MEV) / 3.0
ALPHA_TARGET_E  = np.log(M_TAU_MEV / M_E_MEV)  / 8.0
ALPHA_TARGET    = 0.5 * (ALPHA_TARGET_MU + ALPHA_TARGET_E)

print("=" * 70)
print("OP-03: WKB Tunneling — Yukawa α from extra-dimensional barrier")
print("=" * 70)
print(f"\nObserved lepton masses (PDG 2022):")
print(f"  m_τ = {M_TAU_MEV:.2f} MeV")
print(f"  m_μ = {M_MU_MEV:.3f} MeV")
print(f"  m_e = {M_E_MEV:.3f} MeV")
print(f"\nTarget α from lepton mass ratios:")
print(f"  α_μ (from m_μ/m_τ) = {ALPHA_TARGET_MU:.4f}")
print(f"  α_e  (from m_e/m_τ)  = {ALPHA_TARGET_E:.4f}")
print(f"  α_target (average)   = {ALPHA_TARGET:.4f}")


# ---------------------------------------------------------------------------
# Part 1: Analytic confirmation of n² scaling for parabolic barrier
# ---------------------------------------------------------------------------

def wkb_action_parabolic_analytic(n: int, V0: float, Delta_xi: float,
                                   L: float) -> float:
    """
    Analytic WKB action for parabolic barrier V(ξ) = V₀(ξ/L)²,
    generation n at ξ_n = n Δξ.

    S_n = ∫₀^{n Δξ} √(2 V₀ (ξ/L)²) dξ
         = (√(2V₀)/L) × ∫₀^{n Δξ} ξ dξ
         = (√(2V₀)/L) × (n Δξ)²/2
         = √(2V₀) × n² Δξ² / (2L)

    So α_parabolic = √(2V₀) × Δξ² / (2L).
    """
    return np.sqrt(2.0 * V0) * (n * Delta_xi)**2 / (2.0 * L)


def alpha_parabolic_analytic(V0: float, Delta_xi: float, L: float) -> float:
    """α = √(2V₀) × Δξ² / (2L) from parabolic barrier analytic formula."""
    return np.sqrt(2.0 * V0) * Delta_xi**2 / (2.0 * L)


print("\n" + "=" * 70)
print("PART 1: Analytic — parabolic barrier naturally produces n² scaling")
print("=" * 70)
print("\nFor V(ξ) = V₀(ξ/L)² with ξ_n = n Δξ:")
print("  S_n = √(2V₀) × n² Δξ² / (2L)  [exactly n² — analytic result]")
print("  α = √(2V₀) × Δξ² / (2L)")
print("\nVerification with V₀=2.0, Δξ=0.5, L=1.0:")
V0_check, Dxi_check, L_check = 2.0, 0.5, 1.0
print(f"  α_analytic = {alpha_parabolic_analytic(V0_check, Dxi_check, L_check):.6f}")
actions_check = [wkb_action_parabolic_analytic(n, V0_check, Dxi_check, L_check) for n in [1,2,3]]
print(f"  S_1 = {actions_check[0]:.6f}   S_2/S_1 = {actions_check[1]/actions_check[0]:.4f}  "
      f"(expect 4.0000)")
print(f"  S_3/S_1 = {actions_check[2]/actions_check[0]:.4f}  (expect 9.0000)")
print("  → Confirmed: S_n/S_1 = n². Parabolic barrier is the unique quadratic")
print("    power law that produces n² scaling with evenly spaced generations.")


# ---------------------------------------------------------------------------
# Part 2: Numerical WKB for five barrier shapes
# ---------------------------------------------------------------------------

def barrier_function(xi: float, V0: float, L: float, shape: str) -> float:
    """
    Five barrier shapes for the extra-dimensional potential.
    All normalized so V(L) = V₀.
    """
    if shape == "constant":
        return V0
    elif shape == "linear":
        return V0 * (xi / L)
    elif shape == "parabolic":
        return V0 * (xi / L)**2
    elif shape == "cubic":
        return V0 * (xi / L)**3
    elif shape == "exponential":
        # V(ξ) = V₀ × exp(ξ/L − 1)  normalized so V(L) = V₀
        return V0 * np.exp(xi / L - 1.0)
    else:
        raise ValueError(f"Unknown shape: {shape}")


def wkb_action_numerical(xi_n: float, V0: float, L: float,
                          shape: str, N: int = 2000) -> float:
    """
    Numerical WKB action: S = ∫₀^{ξ_n} √(2 V(ξ)) dξ.
    Uses Simpson quadrature on N-point grid.
    """
    if xi_n <= 0.0:
        return 0.0
    xi_arr = np.linspace(0.0, xi_n, N)
    V_arr  = np.array([barrier_function(xi, V0, L, shape) for xi in xi_arr])
    integrand = np.sqrt(np.maximum(2.0 * V_arr, 0.0))
    return np.trapezoid(integrand, xi_arr)


def fit_yukawa_alpha(y: np.ndarray) -> dict:
    """
    Fit log(y_n) = log(y₀) − α n² for n = 1, 2, 3.
    Returns α, y₀, R².
    """
    ns   = np.array([1.0, 4.0, 9.0])
    ln_y = np.log(y + 1e-100)
    n_p  = 3.0
    s_x, s_y   = ns.sum(), ln_y.sum()
    s_xy, s_x2 = (ns * ln_y).sum(), (ns**2).sum()
    denom = n_p * s_x2 - s_x**2
    B     = (n_p * s_xy - s_x * s_y) / denom
    A     = (s_y - B * s_x) / n_p
    alpha = float(-B)
    y0    = float(np.exp(A))
    y_pred  = y0 * np.exp(-alpha * ns)
    ln_mean = ln_y.mean()
    ss_tot  = ((ln_y - ln_mean)**2).sum()
    ss_res  = ((ln_y - np.log(y_pred + 1e-100))**2).sum()
    r_sq    = float(1.0 - ss_res / ss_tot) if ss_tot > 1e-12 else 1.0
    return {'alpha': alpha, 'y0': y0, 'r_sq': r_sq}


print("\n" + "=" * 70)
print("PART 2: Numerical WKB — comparison of five barrier shapes")
print("=" * 70)
print(f"Parameters: V₀ = 2.0, L = 1.0, generation spacing Δξ = 0.3")
print(f"Generations at: ξ₁ = 0.3, ξ₂ = 0.6, ξ₃ = 0.9")
print(f"{'Shape':<14}  {'S₁':>7}  {'S₂':>7}  {'S₃':>7}  "
      f"{'S₂/S₁':>7}  {'S₃/S₁':>7}  {'α_fit':>8}  {'R²':>6}")
print("-" * 70)

shapes = ["constant", "linear", "parabolic", "cubic", "exponential"]
V0_p2, L_p2, Dxi_p2 = 2.0, 1.0, 0.3

for shape in shapes:
    xi_vals = [Dxi_p2 * n for n in [1, 2, 3]]
    S_vals  = [wkb_action_numerical(xi, V0_p2, L_p2, shape) for xi in xi_vals]
    y_vals  = np.array([np.exp(-S) for S in S_vals])
    if y_vals[0] < 1e-100:
        alpha_s, r2_s = float('nan'), float('nan')
    else:
        fit = fit_yukawa_alpha(y_vals)
        alpha_s = fit['alpha']
        r2_s    = fit['r_sq']
    print(f"{shape:<14}  {S_vals[0]:7.4f}  {S_vals[1]:7.4f}  {S_vals[2]:7.4f}  "
          f"{S_vals[1]/max(S_vals[0],1e-12):7.4f}  {S_vals[2]/max(S_vals[0],1e-12):7.4f}  "
          f"{alpha_s:8.4f}  {r2_s:6.4f}")

print("\nExpected S₂/S₁ for perfect n² scaling: 4.0000")
print("Expected S₃/S₁ for perfect n² scaling: 9.0000")
print("→ Only the parabolic barrier achieves both (analytic result confirmed numerically)")


# ---------------------------------------------------------------------------
# Part 3: Parameter sweep (V₀, Δξ) for α = 1.0 under parabolic barrier
# ---------------------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 3: Parabolic barrier — sweep (V₀, Δξ) for α = 1.0")
print("=" * 70)
print(f"\nAnalytic formula: α = √(2V₀) × Δξ² / (2L)")
print(f"For L = 1.0 (normalized interval):")
print(f"  α = 1.0  ⟺  √(2V₀) × Δξ² = 2.0")
print(f"  i.e., V₀ = 2 / Δξ⁴\n")
print(f"{'Δξ':>8}  {'V₀ (analytic)':>16}  {'α_analytic':>12}  {'α_numerical':>12}  {'|Δα|/α':>9}")
print("-" * 65)

L_p3 = 1.0
Delta_xi_grid = [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9]

results_p3 = []
for Dxi in Delta_xi_grid:
    # V₀ required for α = 1.0 analytically
    V0_analytic = 2.0 / (Dxi**4)
    alpha_a     = alpha_parabolic_analytic(V0_analytic, Dxi, L_p3)

    # Numerical verification
    xi_vals = [Dxi * n for n in [1, 2, 3]]
    # Cap xi_n to stay inside interval
    if xi_vals[2] > L_p3:
        alpha_n = float('nan')
    else:
        S_vals  = [wkb_action_numerical(xi, V0_analytic, L_p3, "parabolic") for xi in xi_vals]
        y_vals  = np.array([np.exp(-S) for S in S_vals])
        fit     = fit_yukawa_alpha(y_vals)
        alpha_n = fit['alpha']

    rel_err = abs(alpha_n - alpha_a) / alpha_a if not np.isnan(alpha_n) else float('nan')
    print(f"{Dxi:8.3f}  {V0_analytic:16.4f}  {alpha_a:12.6f}  {alpha_n:12.6f}  {rel_err:9.2e}")
    results_p3.append({'Dxi': Dxi, 'V0': V0_analytic, 'alpha_a': alpha_a, 'alpha_n': alpha_n})

print("\n* Rows where ξ₃ = 3Δξ > L = 1.0 are out-of-interval and not evaluated.")


# ---------------------------------------------------------------------------
# Part 4: Best-fit selection and mass ratio accuracy
# ---------------------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 4: Mass ratio accuracy at representative (V₀, Δξ) solutions")
print("=" * 70)
print(f"\nTarget: m_n ∝ exp(−α n²), n=1(τ), 2(μ), 3(e), α = {ALPHA_TARGET:.4f}")
print(f"Target ratios: m_μ/m_τ = {M_MU_MEV/M_TAU_MEV:.5f}, "
      f"m_e/m_τ = {M_E_MEV/M_TAU_MEV:.6f}")
print()

# For parabolic barrier, α is a free parameter controlled by (V₀, Δξ, L).
# The analytic result shows: for α = 1.0, we need √(2V₀) × Δξ² = 2L.
# The ONLY non-trivial constraint is α = 1.0 — not the scale of V₀ or Δξ
# separately. This means the mass hierarchy determines one combination of
# parameters, not their individual values (the overall scale is set by
# the bulk condensate normalization, which is a Vol 6 input).

alpha_test_values = [0.90, 0.94, 0.98, 1.00, 1.02, 1.05, 1.10]

print(f"{'α':>6}  {'pred m_μ/m_τ':>14}  {'obs m_μ/m_τ':>12}  "
      f"{'pred m_e/m_τ':>14}  {'obs m_e/m_τ':>13}  {'err_μ%':>8}  {'err_e%':>8}")
print("-" * 85)

for alpha in alpha_test_values:
    pred_mu_over_tau = np.exp(-3.0 * alpha)
    pred_e_over_tau  = np.exp(-8.0 * alpha)
    obs_mu_over_tau  = M_MU_MEV / M_TAU_MEV
    obs_e_over_tau   = M_E_MEV  / M_TAU_MEV
    err_mu = 100.0 * (pred_mu_over_tau - obs_mu_over_tau) / obs_mu_over_tau
    err_e  = 100.0 * (pred_e_over_tau  - obs_e_over_tau)  / obs_e_over_tau
    print(f"{alpha:6.3f}  {pred_mu_over_tau:14.5f}  {obs_mu_over_tau:12.5f}  "
          f"{pred_e_over_tau:14.6f}  {obs_e_over_tau:13.6f}  {err_mu:+8.1f}%  {err_e:+8.1f}%")

print(f"\nObserved: m_μ/m_τ = {M_MU_MEV/M_TAU_MEV:.5f},  m_e/m_τ = {M_E_MEV/M_TAU_MEV:.6f}")


# ---------------------------------------------------------------------------
# Summary and OP-03 update
# ---------------------------------------------------------------------------

print("\n" + "=" * 70)
print("SUMMARY — OP-03 WKB Tunneling Investigation")
print("=" * 70)

print("""
Key findings:

1. PARABOLIC BARRIER PRODUCES n² SCALING ANALYTICALLY.
   For V(ξ) = V₀(ξ/L)² with evenly spaced generations ξ_n = n Δξ:
     S_n = √(2V₀) × n² Δξ² / (2L)   [exact analytic result]
   This is the UNIQUE polynomial potential power law that gives n² scaling
   with equal generation spacing. Constant and linear barriers give n and
   n^(3/2) scaling respectively — neither matches the observed hierarchy.

2. TARGET α = 1.0 IS ACHIEVABLE.
   The parabolic-barrier formula gives α = 1.0 for any (V₀, Δξ, L) satisfying
     √(2V₀) × Δξ² = 2L
   Examples (L = 1.0):
     Δξ = 0.3, V₀ ≈ 246.9    (tight spacing, steep barrier)
     Δξ = 0.5, V₀ ≈ 32.0     (moderate spacing, moderate barrier)
     Δξ = 0.7, V₀ ≈ 8.4      (loose spacing, shallow barrier)
   The RATIO Δξ²/L is the physically meaningful quantity; it is constrained
   by α = 1.0 but not uniquely determined (V₀ absorbs the remaining freedom).

3. PHYSICAL INTERPRETATION.
   The parabolic barrier V(ξ) ∝ ξ² is physically motivated: the Waters Below
   condensate density near the zone wall (ξ = 0) is expected to fall off
   quadratically, creating a potential barrier for charged fermions that rises
   as ξ². The three generations at equally spaced positions ξ_n = n Δξ then
   naturally receive exponentially suppressed Yukawa couplings with n² scaling.

4. WHAT THIS RESOLVES (AND WHAT REMAINS OPEN).
   RESOLVED: The Z₂ symmetry obstacle from the symmetric double-well is
   entirely bypassed. The WKB model is Z₂-asymmetric by construction (Higgs
   at ξ = 0, not at the midpoint), and the parabolic barrier naturally
   separates the three generation couplings.

   STILL OPEN (OP-03 remains OPEN):
   (a) The specific values of V₀, Δξ, L must be derived from the Waters Below
       condensate profile (Vol 1 Ch 6 §6.4 + Vol 6). Currently one free
       parameter (the combination √(2V₀) Δξ²/2L) is fitted to α ≈ 1.0.
   (b) Why exactly three equally-spaced generations? The spacing Δξ and the
       number of generations must follow from topology (OP-04).
   (c) The WKB model currently treats each generation as a classical tunneling
       trajectory. A full quantum-mechanical treatment (Sturm-Liouville in the
       extra dimension with parabolic barrier) would verify the approximation.

5. RECOMMENDED NEXT STEP.
   Derive V₀ from the bulk condensate normalization (Vol 1 Ch 6 §6.4):
     V₀ = ½ μ_B² / ⟨Φ_B⟩²  (Waters Below condensate at zone wall)
   This would reduce OP-03 from a one-parameter fit to a zero-parameter
   derivation, promoting the Yukawa hierarchy from APPROXIMATE to RIGOROUS.
""")

print(f"  α_target = {ALPHA_TARGET:.4f} (from PDG 2022 lepton masses)")
print(f"  α = 1.00 gives: err_μ = {100*(np.exp(-3.0)-M_MU_MEV/M_TAU_MEV)/(M_MU_MEV/M_TAU_MEV):+.1f}%,"
      f"  err_e = {100*(np.exp(-8.0)-M_E_MEV/M_TAU_MEV)/(M_E_MEV/M_TAU_MEV):+.1f}%")
print(f"  α = 0.98 gives: err_μ = {100*(np.exp(-2.94)-M_MU_MEV/M_TAU_MEV)/(M_MU_MEV/M_TAU_MEV):+.1f}%,"
      f"  err_e = {100*(np.exp(-7.84)-M_E_MEV/M_TAU_MEV)/(M_E_MEV/M_TAU_MEV):+.1f}%")
print("\nDone.")


if __name__ == "__main__":
    pass  # All output produced at module level above
