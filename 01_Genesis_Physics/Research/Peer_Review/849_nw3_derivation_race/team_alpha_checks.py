"""
TEAM ALPHA numerical checks for the n_w = 3 derivation attempt.
Three sections:
  A. Jackiw-Rossi channel counting on the COVERING space for N = 3 and N = 9
     (extends op02_aps_index_computation.py v2's method; same ODEs).
  B. Z3 equivariant decomposition of the zero modes (character assignment,
     per-sector counts, Lefschetz fixed-point consistency).
  C. Global-vortex energetics: Nielsen-Olesen profiles for n = 1,2,3,6,9,
     E(n) ~ n^2 log scaling, splitting inequalities, and the cone statement.
No external dependencies (pure Python; Thomas algorithm for the BVP).
"""
import math, cmath, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

LN10 = math.log(10.0)

# ----------------------------------------------------------------------------
# Section A: JR radial channels, inward integration (op02 v2 method, reused)
# ----------------------------------------------------------------------------
V_VEV, R0 = 1.0, 1.0
def f_profile(r):
    return V_VEV * math.tanh(r / R0)

def deriv_r(r, y, n, k):
    a, b, I = y
    fr = f_profile(r)
    return ((k / r) * a - fr * b,
            ((n - 1 - k) / r) * b - fr * a,
            (a * a + b * b) * r)

def deriv_t(t, y, n, k):
    r = math.exp(t)
    a, b, I = y
    rfr = r * f_profile(r)
    return (k * a - rfr * b,
            (n - 1 - k) * b - rfr * a,
            (a * a + b * b) * r * r)

def rk4(deriv, x, y, h, n, k):
    k1 = deriv(x, y, n, k)
    k2 = deriv(x + h/2, tuple(yi + h/2*ki for yi, ki in zip(y, k1)), n, k)
    k3 = deriv(x + h/2, tuple(yi + h/2*ki for yi, ki in zip(y, k2)), n, k)
    k4 = deriv(x + h,   tuple(yi + h*ki   for yi, ki in zip(y, k3)), n, k)
    return tuple(yi + h/6*(p + 2*q + 2*s + u)
                 for yi, p, q, s, u in zip(y, k1, k2, k3, k4))

def solve_channel(n, k, R=30.0, steps_r=5800, decades=6, steps_dec=1200):
    h = (1.0 - R) / steps_r
    y = (1.0, 1.0, 0.0)
    r = R
    for i in range(steps_r):
        y = rk4(deriv_r, r, y, h, n, k)
        r = R + (i + 1) * h
    ht = -LN10 / steps_dec
    t = 0.0
    psi = {0: math.hypot(y[0], y[1])}
    for d in range(1, decades + 1):
        for _ in range(steps_dec):
            y = rk4(deriv_t, t, y, ht, n, k)
            t += ht
        psi[d] = math.hypot(y[0], y[1])
    nu = math.log(psi[decades-1] / psi[decades]) / LN10
    return nu

print("=" * 72)
print("A. COVERING-SPACE JR CHANNEL COUNT (winding N), method of op02 v2")
print("=" * 72)
counts = {}
for N in (3, 9):
    good = []
    for k in range(-2, N + 3):
        nu = solve_channel(N, k)
        ok = nu > -0.5
        if ok:
            good.append(k)
    counts[N] = good
    print(f"  N = {N}: normalizable channels k = {good}  -> count {len(good)}")
    assert good == list(range(N)), f"channel set mismatch at N={N}"
print("  JR theorem (index = N on the covering space): verified for N = 3, 9.")

# ----------------------------------------------------------------------------
# Section B: Z3 equivariant decomposition
# ----------------------------------------------------------------------------
print()
print("=" * 72)
print("B. Z3 EQUIVARIANT DECOMPOSITION OF THE ZERO MODES")
print("=" * 72)
print("""  The orbifold generator g acts on channel k by the character
  chi(g) = omega^(m0 - k), omega = exp(2 pi i/3); m0 is a k-INDEPENDENT
  constant (spin lift + discrete Wilson line).  Only relative characters
  matter; take m0 = 0 (any other m0 permutes the sector labels).""")
omega = cmath.exp(2j * math.pi / 3)
for N in (3, 9):
    ks = counts[N]
    sector = {0: [], 1: [], 2: []}
    for k in ks:
        sector[(-k) % 3].append(k)
    print(f"\n  N = {N} (quotient winding n_q = {N//3}):")
    for s in (0, 1, 2):
        print(f"    Z3 sector n_c = {s}: channels {sector[s]}"
              f"  -> {len(sector[s])} zero mode(s)")
    # Lefschetz / equivariant character sums
    ind1 = len(ks)
    indg = sum(omega ** ((-k) % 3) for k in ks)
    indg2 = sum((omega ** 2) ** ((-k) % 3) for k in ks)
    # standard projector: ind_s = (1/3) sum_{j=0..2} omega^{-s j} ind(g^j)
    for s in (0, 1, 2):
        ind_s = (ind1 + (omega ** (-s)) * indg + (omega ** (-2 * s)) * indg2) / 3
        assert abs(ind_s.imag) < 1e-12
        assert abs(ind_s.real - len(sector[s])) < 1e-12
    print(f"    Lefschetz check: ind(1) = {ind1}, ind(g) = {indg:.3f}, "
          f"ind(g^2) = {indg2:.3f}")
    print(f"    Projector (1/3)Sum chi^-1(g^j) ind(g^j) reproduces the "
          f"per-sector counts: OK")
print("""
  RESULT: per-sector index = N/3 exactly.
    N = 3  -> (1,1,1): ONE zero mode per Z3 sector; singlet sector has 1.
    N = 9  -> (3,3,3): three per sector (3 colors x 3 generations = 9).
  No choice of m0 (Wilson line / spin lift) changes the partition: the three
  characters are a free orbit of the channel grading k -> k+1.""")

# ----------------------------------------------------------------------------
# Section C: global-vortex energetics
# ----------------------------------------------------------------------------
print()
print("=" * 72)
print("C. GLOBAL VORTEX ENERGETICS  E(n) (units 2 pi v_A^2; lambda_A v^2 = 1)")
print("=" * 72)

def solve_profile(n, R=60.0, M=6000, iters=80):
    """Newton solve  f'' + f'/r - n^2 f/r^2 - f(f^2-1) = 0, f(0)=0, f(R)=1."""
    h = R / M
    r = [i * h for i in range(M + 1)]
    rc = max(1.0, 0.8 * n)
    f = [0.0] + [ (ri ** n) / (ri ** n + rc ** n) if ri > 0 else 0.0
                  for ri in r[1:] ]
    f[M] = 1.0
    for it in range(iters):
        # residual and tridiagonal Jacobian on interior nodes 1..M-1
        lo = [0.0] * (M + 1); di = [0.0] * (M + 1); up = [0.0] * (M + 1)
        res = [0.0] * (M + 1)
        for i in range(1, M):
            ri = r[i]
            res[i] = ((f[i+1] - 2*f[i] + f[i-1]) / h**2
                      + (f[i+1] - f[i-1]) / (2 * ri * h)
                      - n**2 * f[i] / ri**2 - f[i] * (f[i]**2 - 1.0))
            lo[i] = 1.0/h**2 - 1.0/(2*ri*h)
            di[i] = -2.0/h**2 - n**2/ri**2 - 3.0*f[i]**2 + 1.0
            up[i] = 1.0/h**2 + 1.0/(2*ri*h)
        # Thomas algorithm for J * d = -res
        cp = [0.0] * (M + 1); dp = [0.0] * (M + 1)
        cp[1] = up[1] / di[1]; dp[1] = -res[1] / di[1]
        for i in range(2, M):
            mden = di[i] - lo[i] * cp[i-1]
            cp[i] = up[i] / mden
            dp[i] = (-res[i] - lo[i] * dp[i-1]) / mden
        d = [0.0] * (M + 1)
        d[M-1] = dp[M-1]
        for i in range(M - 2, 0, -1):
            d[i] = dp[i] - cp[i] * d[i+1]
        damp = 1.0 if it > 2 else 0.5
        mx = 0.0
        for i in range(1, M):
            f[i] += damp * d[i]
            f[i] = min(max(f[i], -0.1), 1.5)
            mx = max(mx, abs(d[i]))
        if mx < 1e-12:
            break
    # energy density u = f'^2 + n^2 f^2/r^2 + (1/2)(f^2-1)^2 ; E = int u r dr
    E = 0.0
    for i in range(1, M + 1):
        rim, ri = r[i-1], r[i]
        fpm = (f[i] - f[i-1]) / h
        fm = 0.5 * (f[i] + f[i-1]); rm = 0.5 * (rim + ri)
        u = fpm**2 + n**2 * fm**2 / rm**2 + 0.5 * (fm**2 - 1.0)**2
        E += u * rm * h
    return E, mx

R = 60.0
E = {}
for n in (1, 2, 3, 6, 9):
    E[n], resid = solve_profile(n, R=R)
    print(f"  n = {n}:  E(n) = {E[n]:10.4f}   (Newton residual {resid:.2e})"
          f"   E(n)/(n^2 ln R) = {E[n]/(n*n*math.log(R)):.4f}")

p69 = math.log(E[9]/E[1]) / math.log(9)
print(f"\n  scaling exponent  log[E(9)/E(1)]/log 9 = {p69:.3f}   "
      f"(global-vortex prediction ~ 2 - O(1/ln R); GAUGED would be ~ 1)")
print(f"  E(2) vs 2 E(1):  {E[2]:.3f} vs {2*E[1]:.3f}   -> "
      f"{'SPLITS' if E[2] > 2*E[1] else 'binds'}")
print(f"  E(6) vs 2 E(3):  {E[6]:.3f} vs {2*E[3]:.3f}   -> "
      f"{'SPLITS (6 -> 3+3)' if E[6] > 2*E[3] else 'binds'}")
print(f"  E(9) vs 3 E(3):  {E[9]:.3f} vs {3*E[3]:.3f}   -> "
      f"{'SPLITS (9 -> 3+3+3)' if E[9] > 3*E[3] else 'binds'}")
print("""
  CONE STATEMENT: on C/Z3 the energy of a quotient-winding-n_q vortex is
  E_cone(n_q) = (1/3) E_cover(3 n_q)  (fundamental domain = 1/3 of the disk).
  E_cone(3) vs 3 E_cone(1)  <=>  E(9) vs 3 E(3)  -> same inequality above:
  the n_q = 3 (covering N = 9) object needed for THREE singlet generations
  is unstable to splitting into three n_q = 1 (N = 3) vortices,
  each carrying ONE singlet generation.""")

print("\nALL ASSERTIONS PASSED.")
