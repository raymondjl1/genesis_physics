"""
OP-03 Investigation: V₀ Sweep for Yukawa α ≈ 1.0
=================================================

Question: What double-well depth V₀ gives the fitted Yukawa hierarchy parameter
α ≈ 1.0 as computed from the Sturm-Liouville overlap integral?

Context:
  - Double-well potential: V(x) = V₀(x²-1)², wells at x = ±1
  - Higgs profile: H(x) = exp(-((x-1)/σ_H)²/2), peaked at x = +1 (zone wall)
  - Yukawa coupling: y_n = ∫ ψ_n(x) H(x) ψ₁(x) dx
  - Exponential ansatz: y_n ≈ y₀ exp(-α n²)
  - Current calibration: V₀ = 0.002 → α ≈ 0.076 (too small by factor ~13)
  - Target: α ≈ 1.0 (needed for τ/μ/e mass hierarchy at 15-17% accuracy)

Key finding from REVIEWER_BRIEF.md:
  Root cause of α gap: with shallow wells, bonding (ψ₁, symmetric) and
  antibonding (ψ₂, antisymmetric) states have nearly equal amplitude at x=±1,
  so their Yukawa couplings are nearly equal and the hierarchy is weak.
  Deeper wells give more localized states with different spatial profiles.

This script sweeps V₀ from 0.001 to 20.0 and for each value:
  1. Solves the eigenvalue problem (finite-difference, N=500)
  2. Always uses the FIRST THREE eigenstates as the three generations
  3. Computes Yukawa overlaps y₁, y₂, y₃ and fits α
  4. Computes spectral gap ratio (ε₄-ε₃)/(ε₃-ε₂) to assess robustness
  5. Reports α vs V₀ and identifies the V₀ threshold for α = 1.0

Key: "three generations" = first three eigenstates, period.
The spectral gap is a diagnostic, not a gating criterion.

Author: Jeff Raymond / Genesis Physics Project
Date: 2026-05-11
"""

import numpy as np
from numpy.linalg import eigh


def solve_lowest_k(V0: float, k: int = 5, N: int = 500, x_max: float = 10.0):
    """
    Solve -d²ψ/dx² + V₀(x²-1)² ψ = ε ψ with Dirichlet BCs.
    Returns (eigenvalues[:k], eigenvectors[:,:k], x_array).
    Eigenvectors are L²-normalised: ∫|ψ|² dx = 1.
    """
    x    = np.linspace(-x_max, x_max, N)
    dx   = x[1] - x[0]
    V    = V0 * (x**2 - 1.0)**2
    diag = 2.0 / dx**2 + V
    off  = -1.0 / dx**2 * np.ones(N - 1)
    H_mat = np.diag(diag) + np.diag(off, 1) + np.diag(off, -1)
    eigvals, eigvecs = eigh(H_mat)

    # L² normalise
    for i in range(k):
        nrm = np.sqrt(np.sum(eigvecs[:, i]**2) * dx)
        if nrm > 0:
            eigvecs[:, i] /= nrm

    return eigvals[:k], eigvecs[:, :k], x


def spectral_gap_ratio(eps: np.ndarray) -> float:
    """
    Returns (ε₄-ε₃)/(ε₃-ε₂) — a measure of whether ε₄ is anomalously
    far from ε₃ (suggests a natural cutoff after 3 states).
    """
    g32 = eps[2] - eps[1]
    g43 = eps[3] - eps[2]
    if g32 < 1e-12:
        return float('nan')
    return g43 / g32


def compute_yukawa_alpha(eigvecs: np.ndarray, x_arr: np.ndarray,
                          sigma_H: float = 0.4) -> dict:
    """
    Compute y_n = ∫ ψ_n(x) H(x) ψ₁(x) dx for n=1,2,3,
    fit log(y_n) = log(y₀) - α n², return α and diagnostics.
    """
    dx = x_arr[1] - x_arr[0]
    H  = np.exp(-0.5 * ((x_arr - 1.0) / sigma_H)**2)

    y = []
    for k in range(3):
        integral = np.sum(eigvecs[:, k] * H * eigvecs[:, 0]) * dx
        y.append(abs(integral))
    y = np.array(y)

    result = {
        'y1': float(y[0]), 'y2': float(y[1]), 'y3': float(y[2]),
        'hierarchy_ok': bool(y[0] > y[1] > y[2] > 1e-30),
        'alpha': None, 'y0': None, 'r_sq': None,
    }

    if not result['hierarchy_ok'] or y[2] < 1e-30:
        return result

    # OLS fit on log scale: log(y_n) = log(y₀) - α n²
    ns   = np.array([1.0, 4.0, 9.0])
    ln_y = np.log(y)
    n_p  = 3.0
    s_x, s_y   = ns.sum(), ln_y.sum()
    s_xy, s_x2 = (ns * ln_y).sum(), (ns**2).sum()
    denom = n_p * s_x2 - s_x**2
    B     = (n_p * s_xy - s_x * s_y) / denom
    A     = (s_y - B * s_x) / n_p

    alpha_fit = float(-B)
    y0_fit    = float(np.exp(A))

    y_pred   = y0_fit * np.exp(-alpha_fit * ns)
    ln_mean  = ln_y.mean()
    ss_tot   = ((ln_y - ln_mean)**2).sum()
    ss_res   = ((ln_y - np.log(y_pred + 1e-30))**2).sum()
    r_sq     = float(1.0 - ss_res / ss_tot) if ss_tot > 1e-12 else 1.0

    result['alpha'] = alpha_fit
    result['y0']    = y0_fit
    result['r_sq']  = r_sq
    return result


def run_sweep():
    sigma_H = 0.4   # same as test suite

    # V₀ grid: dense near origin (where current calibration sits) and higher
    V0_values = np.concatenate([
        [0.001, 0.002, 0.003, 0.005],
        np.geomspace(0.01, 0.09, 9),
        np.geomspace(0.1,  1.0,  10),
        np.geomspace(1.0,  20.0, 15),
    ])
    V0_values = np.unique(np.round(V0_values, 6))

    print("=" * 88)
    print("OP-03 V₀ Sweep — Double-well depth vs. Yukawa α  (σ_H = 0.4, Higgs at x = +1)")
    print("Three generations = first three eigenstates of -d²/dx² + V₀(x²-1)²")
    print("=" * 88)
    print(f"{'V₀':>8}  {'ε₁':>7}  {'ε₂':>7}  {'ε₃':>7}  {'gap43/32':>8}  "
          f"{'α_fit':>8}  {'y₁':>9}  {'y₂':>9}  {'y₃':>9}  {'hier':>5}")
    print("-" * 88)

    rows = []

    for V0 in V0_values:
        eps, evec, x_arr = solve_lowest_k(V0, k=5, N=500, x_max=10.0)
        gap_ratio = spectral_gap_ratio(eps)
        res = compute_yukawa_alpha(evec, x_arr, sigma_H)

        alpha = res['alpha']
        a_str = f"{alpha:8.4f}" if alpha is not None else "    N/A "
        g_str = f"{gap_ratio:8.3f}" if not np.isnan(gap_ratio) else "     N/A"
        h_str = "  YES" if res['hierarchy_ok'] else "   NO"

        print(f"{V0:8.4f}  {eps[0]:7.4f}  {eps[1]:7.4f}  {eps[2]:7.4f}  {g_str}  "
              f"{a_str}  {res['y1']:9.5f}  {res['y2']:9.5f}  {res['y3']:9.5f}  {h_str}")

        rows.append({'V0': V0, 'eps': eps[:4].tolist(), 'gap_ratio': gap_ratio,
                     **res})

    print("=" * 88)

    # ---- Analysis ----
    valid = [(r['V0'], r['alpha']) for r in rows
             if r['alpha'] is not None and r['hierarchy_ok'] and r['alpha'] > 0]

    if not valid:
        print("\n*** No valid α (positive, hierarchy intact) found. ***")
        return rows

    V0s    = np.array([v[0] for v in valid])
    alphas = np.array([v[1] for v in valid])

    # Is α monotone in V₀?
    print("\n--- α(V₀) trend ---")
    for V0, a in zip(V0s, alphas):
        print(f"  V₀ = {V0:8.4f}   α = {a:.5f}")

    print(f"\n  Range: α ∈ [{alphas.min():.5f}, {alphas.max():.5f}]")
    mono = all(alphas[i] <= alphas[i+1] for i in range(len(alphas)-1))
    print(f"  Monotonically increasing: {mono}")

    if alphas.max() >= 1.0:
        idx = np.searchsorted(alphas, 1.0)
        if 0 < idx < len(alphas):
            V0_lo, a_lo = V0s[idx-1], alphas[idx-1]
            V0_hi, a_hi = V0s[idx],   alphas[idx]
            t  = (1.0 - a_lo) / (a_hi - a_lo)
            V0_target = float(V0_lo + t * (V0_hi - V0_lo))
            print(f"\n{'*'*60}")
            print(f"  RESULT: V₀ for α = 1.0  ≈  {V0_target:.4f}")
            print(f"  (interpolated between V₀={V0_lo:.4f},α={a_lo:.4f} "
                  f"and V₀={V0_hi:.4f},α={a_hi:.4f})")
            print(f"{'*'*60}")

            # Refine with N=700 around this region
            print(f"\n--- Refinement sweep around V₀ ≈ {V0_target:.3f} (N=700) ---")
            V0_lo_r = max(0.001, V0_lo * 0.7)
            V0_hi_r = V0_hi * 1.3
            V0_refine = np.linspace(V0_lo_r, V0_hi_r, 25)
            refine_pts = []
            for V0r in V0_refine:
                eps_r, evec_r, x_r = solve_lowest_k(V0r, k=5, N=700, x_max=10.0)
                gr = spectral_gap_ratio(eps_r)
                re = compute_yukawa_alpha(evec_r, x_r, sigma_H)
                if re['alpha'] is not None and re['hierarchy_ok']:
                    print(f"    V₀ = {V0r:.5f}   α = {re['alpha']:.6f}   "
                          f"gap43/32 = {gr:.3f}   y = ({re['y1']:.5f}, {re['y2']:.5f}, {re['y3']:.5f})")
                    refine_pts.append((V0r, re['alpha'], gr))

            if refine_pts:
                rV = np.array([p[0] for p in refine_pts])
                rA = np.array([p[1] for p in refine_pts])
                rG = np.array([p[2] for p in refine_pts])
                if rA.max() >= 1.0 and rA.min() <= 1.0:
                    i2 = np.searchsorted(rA, 1.0)
                    if 0 < i2 < len(rA):
                        t2 = (1.0 - rA[i2-1]) / (rA[i2] - rA[i2-1])
                        V0_refined = float(rV[i2-1] + t2 * (rV[i2] - rV[i2-1]))
                        # Gap ratio at this V₀
                        gap_at_target = float(rG[i2-1] + t2 * (rG[i2] - rG[i2-1]))
                        print(f"\n{'*'*60}")
                        print(f"  REFINED RESULT: V₀ for α = 1.0  ≈  {V0_refined:.5f}")
                        print(f"  Spectral gap ratio at this V₀: (ε₄-ε₃)/(ε₃-ε₂) ≈ {gap_at_target:.3f}")
                        print(f"  (A ratio > 1.5 suggests a natural cutoff after 3 states)")
                        print(f"{'*'*60}")
        elif idx == 0:
            print(f"\n  α ≥ 1.0 even at smallest V₀ = {V0s[0]:.4f}")
    else:
        print(f"\n*** α does NOT reach 1.0 in the tested range ***")
        print(f"    Max α = {alphas.max():.5f} at V₀ = {V0s[alphas.argmax()]:.4f}")
        print(f"    The symmetric double-well V₀(x²-1)² with σ_H = {sigma_H}")
        print(f"    may not be able to achieve α=1.0 while maintaining 3 generations.")
        print(f"    IMPLICATION for OP-03: Option (b) needed — different physical")
        print(f"    mechanism or modified potential shape.")

    print("\nDone.")
    return rows


if __name__ == "__main__":
    rows = run_sweep()
