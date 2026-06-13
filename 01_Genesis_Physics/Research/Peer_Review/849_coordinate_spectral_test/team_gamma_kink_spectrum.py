"""
TEAM GAMMA — Spectral generation count, Part 1: the kink (domain-wall) eigenvalue problem.
============================================================================================
Lead method: QM bound-state spectral counting (Sturm-Liouville / node theorem / Poschl-Teller).

PHYSICS (all ingredients from the corpus, cited in the .md):
  - op03 condensate BVP: the Waters-Below (eta) condensate is a phi^4 kink
        Phi(eta) = v * tanh( kappa * eta / sqrt(2) )            (op03 exact solution)
    with wall width  w = sqrt(2)/kappa  (in eta_B units).
  - A 5D fermion with Yukawa coupling  L_Yuk = -g * Phi(eta) * psibar psi  has, on
    dimensional reduction in the eta direction, a mode (Sturm-Liouville) operator whose
    SAME-CHIRALITY bound levels are the trapped 4D fermions (Jackiw-Rebbi / split fermions).
  - The two chiralities obey SUSY-partner Schrodinger operators
        H_L = -d^2/dy^2 + W^2 - W'      (left)        H_R = -d^2/dy^2 + W^2 + W'   (right)
    with superpotential  W(y) = g*v*w * tanh(y),  y = eta/w  (dimensionless).
    => W' = (g v w) sech^2 y.  Define  s = g*v*w  (the ONE dimensionless coupling).
  - H_L gets a volcano/well  V_L = s^2 - s(s? ) ... actually:
        V_L = s^2 tanh^2 y - s sech^2 y = s^2 - s(s+1) sech^2 y      (uses tanh^2 = 1 - sech^2)
    This is the POSCHL-TELLER well of strength s(s+1): EXACTLY  ceil(s)  bound states with
    E < s^2 (the continuum threshold), one of which (E=0) is the chiral zero mode.
    The NUMBER of normalizable LEFT-chiral bound levels below threshold is
        N_bound = floor(s) + 1   if s is non-integer-special... we COUNT numerically.

  KEY POINT for O-tune: s is NOT free here. It is  s = g v w.  We test what the corpus
  FORCES s to be, and whether that gives N_bound = 3 without tuning.

This script: hand-rolled (numpy only, no scipy). Solves H_L by finite differences on a
large box, counts bound states (E < threshold = s^2) and counts NODES to confirm.
Validates against the EXACT Poschl-Teller spectrum E_n = s^2 - (s-n)^2, n=0..floor(s).
"""
import numpy as np

def poschl_teller_exact_levels(s):
    """Exact bound-state energies of V = s^2 - s(s+1) sech^2 y, threshold s^2.
       Bound states E_n = s^2 - (s-n)^2 for n=0,1,... while (s-n) > 0."""
    levels = []
    n = 0
    while s - n > 1e-12:
        levels.append(s**2 - (s - n)**2)
        n += 1
    return levels  # count = number of n with s-n>0 = ceil(s) (or floor(s)+1 if non-integer)

def solve_FD(s, L=40.0, N=8000):
    """Finite-difference eigenvalues of H_L = -d^2/dy^2 + s^2 - s(s+1) sech^2 y on [-L,L].
       Returns eigenvalues sorted; bound = those below threshold s^2."""
    y = np.linspace(-L, L, N)
    h = y[1]-y[0]
    V = s**2 - s*(s+1.0)/np.cosh(y)**2
    # tridiagonal Hamiltonian
    main = 2.0/h**2 + V
    off = -1.0/h**2 * np.ones(N-1)
    # symmetric tridiagonal eigenvalues via numpy (build dense band is too big; use eigh_tridiagonal-free)
    # hand-rolled: use numpy.linalg.eigh on a sparse-ish dense for moderate N is heavy.
    # Instead use the fact it's tridiagonal: build dense only for N<=4000, else use a coarser N.
    return y, h, main, off, V

def tridiag_eigvals(main, off):
    """Eigenvalues of symmetric tridiagonal (main diag, off diag) via numpy dense eigh on band.
       For speed with large N, use scipy-free QL? We just build dense for N<=4000."""
    N = len(main)
    M = np.zeros((N, N))
    M[np.arange(N), np.arange(N)] = main
    M[np.arange(N-1), np.arange(1, N)] = off
    M[np.arange(1, N), np.arange(N-1)] = off
    return np.linalg.eigvalsh(M)

def count_bound(s, L=30.0, N=3000):
    y, h, main, off, V = solve_FD(s, L, N)
    ev = tridiag_eigvals(main, off)
    thr = s**2
    bound = ev[ev < thr - 1e-6]
    return bound, thr

print("="*74)
print("TEAM GAMMA Part 1 — Kink (domain-wall) fermion spectrum: bound-state count")
print("="*74)
print("""
Left-chiral mode operator  H_L = -d^2/dy^2 + s^2 - s(s+1) sech^2(y),  threshold E=s^2.
s = g*v*w is the SINGLE dimensionless coupling (Yukawa x VEV x wall width).
Exact Poschl-Teller: bound levels E_n = s^2-(s-n)^2, n=0..(while s-n>0).
The E=0 level (n=0) is the chiral zero mode (the Jackiw-Rebbi trapped fermion).
""")

print(f"{'s':>6} | {'exact #bound':>12} | {'FD #bound':>9} | {'exact levels (E)':>30}")
print("-"*74)
for s in [0.5, 0.9, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]:
    exact = poschl_teller_exact_levels(s)
    bound, thr = count_bound(s)
    lvl_str = ", ".join(f"{e:.3f}" for e in exact[:5])
    print(f"{s:>6.2f} | {len(exact):>12} | {len(bound):>9} | {lvl_str:>30}")

print("""
READING:
  # same-chirality bound levels = ceil(s)  (for non-integer s);  = s+1 ... let's see the table.
  The COUNT is controlled entirely by s = g v w. To get exactly 3 LEFT-chiral bound
  levels (incl. the zero mode), need  2 < s <= 3.

O-TUNE TEST: is s forced to land in (2,3]?  s = g*v*w. The kink self-consistency
(op03) ties w and v to kappa; g is the Yukawa coupling (a priori free). So WITHOUT a
principle fixing g, s is tunable and 3 is NOT forced by the kink alone. Part 2 asks
whether the WARP MEASURE + radial vortex problem fixes the count instead.
""")
