"""
TEAM BETA numerical checks for the n_w = 3 derivation attempt.
================================================================
Four checks:
  A. Z3-equivariant zero-mode census: for covering winding N = 3, 6 solve the
     Jackiw-Rossi radial system (same ODEs as op02_aps_index_computation.py v2,
     independently re-implemented) in every angular channel k, find the
     normalizable ones, and bin them by Z3 character k mod 3.
     CLAIM TO TEST: per-sector count = N/3 (NOT: all N in the singlet sector).
  B. Lefschetz / equivariant-index arithmetic: index_s = (1/3) * sum_g
     conj(chi_s(g)) * ind_g, with ind_1 = N and ind_w computed from the mode
     characters sum_k w^{-k}.  CLAIM: ind_w = 0 for N in 3Z, so index_s = N/3
     for every sector s, independent of the spin-structure offset delta.
  C. Global-vortex energetics on the cone C/Z3 via the covering plane:
     compare quotient energy of (i) apex-centred covering-winding-3 vortex vs
     (ii) a Z3-symmetric triple of unit covering vortices at radius d from the
     apex (= ONE quotient-winding-1 vortex at distance d).  Point-vortex
     (logarithmic) energies, standard for global U(1) vortices:
       E_cover / (2 pi v^2) = sum_i n_i^2 ln(L/a) + 2 sum_{i<j} n_i n_j ln(L/d_ij)
       E_quotient = E_cover / 3   (fundamental domain = 1/3 of plane)
     CLAIM TO TEST: E(triple at d) < E(apex-3) and decreasing in d
     => the apex-pinned winding-3 configuration is UNSTABLE (anti-pinning).
  D. Gravitational backreaction: deficit angle 8 pi G mu for a global vortex
     with v_A = M_Pl.  CLAIM: >> 2 pi, i.e. flat-space energetics is outside
     its domain of validity.
"""
import math

LN10 = math.log(10.0)

# ---------- shared radial solver (independent re-implementation) ------------
V, R0 = 1.0, 1.0
def f_profile(r):
    return V * math.tanh(r / R0)

def deriv_r(r, y, N, k):
    a, b = y
    fr = f_profile(r)
    return ((k / r) * a - fr * b, ((N - 1 - k) / r) * b - fr * a)

def deriv_t(t, y, N, k):     # t = ln r grid for the small-r region
    r = math.exp(t)
    a, b = y
    rfr = r * f_profile(r)
    return (k * a - rfr * b, (N - 1 - k) * b - rfr * a)

def rk4(deriv, x, y, h, N, k):
    k1 = deriv(x, y, N, k)
    k2 = deriv(x + h/2, tuple(yi + h/2*ki for yi, ki in zip(y, k1)), N, k)
    k3 = deriv(x + h/2, tuple(yi + h/2*ki for yi, ki in zip(y, k2)), N, k)
    k4 = deriv(x + h, tuple(yi + h*ki for yi, ki in zip(y, k3)), N, k)
    return tuple(yi + h/6*(p + 2*q + 2*s + u)
                 for yi, p, q, s, u in zip(y, k1, k2, k3, k4))

def exponent_at_origin(N, k, R=30.0, steps_r=6000, decades=6, steps_dec=1500):
    """Integrate the decaying-at-infinity solution inward; return the measured
    power-law exponent nu = d ln|psi| / d ln r near r -> 0.
    JR prediction: nu = min(k, N-1-k); normalizable iff nu >= 0."""
    h = (1.0 - R) / steps_r
    y, r = (1.0, 1.0), R
    for i in range(steps_r):
        y = rk4(deriv_r, r, y, h, N, k)
        r = R + (i + 1) * h
    ht, t = -LN10 / steps_dec, 0.0
    psi = {0: math.hypot(*y)}
    for d in range(1, decades + 1):
        for _ in range(steps_dec):
            y = rk4(deriv_t, t, y, ht, N, k)
            t += ht
        psi[d] = math.hypot(*y)
    return math.log(psi[decades - 1] / psi[decades]) / LN10

print("=" * 72)
print("CHECK A: equivariant zero-mode census, binned by Z3 character k mod 3")
print("=" * 72)
for N in (3, 6):
    sectors = {0: [], 1: [], 2: []}
    for k in range(-2, N + 3):
        nu = exponent_at_origin(N, k)
        predicted = min(k, N - 1 - k)
        normalizable = nu > -0.5
        assert abs(nu - predicted) < 0.05, (N, k, nu, predicted)
        if normalizable:
            sectors[k % 3].append(k)
    counts = {s: len(v) for s, v in sectors.items()}
    print(f"  N = {N}:")
    for s in (0, 1, 2):
        print(f"    Z3 sector s = {s}:  modes k = {sectors[s]}   count = {counts[s]}")
    assert all(counts[s] == N // 3 for s in (0, 1, 2)), counts
    print(f"    -> per-sector index = {N//3} = N/3 (quotient winding); "
          f"NOT {N} in one sector.  VERIFIED")

print()
print("=" * 72)
print("CHECK B: Lefschetz arithmetic  index_s = (1/3) sum_g chi_s(g)* ind_g")
print("=" * 72)
w = complex(math.cos(2*math.pi/3), math.sin(2*math.pi/3))
for N in (3, 6, 9):
    ind = {0: complex(N, 0)}                       # g = identity
    for g in (1, 2):                               # g = w, w^2; any common
        ind[g] = sum(w**(-k*g) for k in range(N))  # offset delta drops out
    print(f"  N = {N}:  ind_1 = {ind[0].real:.0f},  |ind_w| = {abs(ind[1]):.2e},"
          f"  |ind_w2| = {abs(ind[2]):.2e}")
    for s in (0, 1, 2):
        idx = sum(w**(s*g) * ind[g] for g in (0, 1, 2)) / 3.0
        assert abs(idx - N/3) < 1e-12
    print(f"    -> index_s = {N//3} for EVERY sector s (delta-independent, "
          f"since ind_w = 0 for N in 3Z).  VERIFIED")

print()
print("=" * 72)
print("CHECK C: cone energetics — apex-pinned N=3 vs off-apex image triple")
print("=" * 72)
a, L = 1.0, 1.0e6     # core size and IR cutoff, in units of a
lnLa = math.log(L / a)
E_apex3 = 9.0 * lnLa / 3.0          # quotient units: (N^2 ln)/3
print(f"  E_quotient(apex, N_cover=3)/(2 pi v^2) = 3 ln(L/a) = {E_apex3:.3f}")
print(f"  {'d/a':>10} {'E_quotient(triple at d)':>26} {'< apex-3?':>10}")
prev = None
for d in (2.0, 10.0, 100.0, 1.0e4, 1.0e5):
    # three unit covering vortices at radius d, pairwise distance sqrt(3) d
    E_cov = 3.0 * lnLa + 2.0 * 3.0 * math.log(L / (math.sqrt(3.0) * d))
    E_q = E_cov / 3.0
    print(f"  {d:>10.0f} {E_q:>26.3f} {'YES' if E_q < E_apex3 else 'no':>10}")
    assert E_q < E_apex3
    if prev is not None:
        assert E_q < prev     # monotonically decreasing outward
    prev = E_q
print("  -> apex-pinned winding-3 is unstable: energy strictly decreases as")
print("     the winding slides off the apex (like-sign image repulsion).")
print("     VERIFIED (anti-pinning; the Step-2 selection argument inverts).")
E_apex6 = 36.0 * lnLa / 3.0
d6 = 1.0e3
E_six_units = (6.0*lnLa + 2.0*15.0*math.log(L/d6)) / 3.0   # 15 pairs, sep ~ d6
print(f"  (aside) E_q(apex, N=6) = {E_apex6:.1f}  vs  ~{E_six_units:.1f} for six")
print("     dispersed unit vortices: splitting always wins under E ~ N^2 ln.")

print()
print("=" * 72)
print("CHECK D: gravitational backreaction at v_A ~ M_Pl")
print("=" * 72)
# deficit angle of a string: delta ~ 8 pi G mu;  mu ~ 2 pi v^2 N^2 ln(L/a)
for lnfac in (10.0, 100.0):
    mu = 2*math.pi * 1.0 * 9.0 * lnfac          # v = M_Pl => G mu = mu/M_Pl^2
    delta_over_2pi = 8*math.pi*mu / (2*math.pi)
    print(f"  ln(L/a) = {lnfac:>5.0f}:  delta/(2 pi) = 4 mu/M_Pl^2 = "
          f"{delta_over_2pi:.3e}   (>> 1)")
    assert delta_over_2pi > 1.0e2
print("  -> deficit angle exceeds 2 pi by 2-3 orders of magnitude: flat-space")
print("     vortex energetics (Check C and the corpus's E ~ N^2) is formally")
print("     outside its validity domain at v_A = M_Pl.  Bound recorded.")

print()
print("ALL CHECKS PASSED.")
