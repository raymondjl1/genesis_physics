"""
REFEREE independent checks for the n_w = 3 adjudication (#849).
Independent of both teams' scripts:
  A1. Character assignment derived from the symmetry algebra (exact mod-3
      arithmetic): the consistency condition 2c+s1+s2 = N-1 (mod 3) for the
      real-linear (Majorana-coupled) JR system, the resulting character
      omega^(m0-k), and a direct proof that NO admissible (c,s1,s2) puts all
      three N=3 modes in one sector (the would-be verdict reversal).
  A2. Channel count for N = 3 by OUTWARD shooting (different scheme from both
      teams' inward integration): normalizable channels = {0,1,2} exactly.
  B.  Beta's Lemma 2 constructively: Psi = (w^3 - w0^3)/|...| is exactly
      Z3-invariant (untwisted), has covering winding 3 at infinity, winding 0
      around the apex, winding 1 around [w0]: quotient charge 1 with NO apex
      core. (Refutes 'quotient charges 1,2 are forbidden'.)
  C.  Apex-vs-triple energetics WITHOUT the point-vortex formula: direct 2D
      grid integration of |grad chi|^2 for chi = arg Psi. Confirms
      E(triple at d) < E(apex N=3), monotone in d, and matches the
      point-vortex prediction both teams used.
  D.  Lefschetz sums ind(g), ind(g^2) for N = 3, 6, 9 (exact roots of unity).
"""
import math, cmath

# ---------------------------------------------------------------------------
# A1. Character assignment from first principles (exact mod-3 arithmetic)
# ---------------------------------------------------------------------------
print("=" * 74)
print("A1. CHARACTER ASSIGNMENT: independent derivation check (exact mod 3)")
print("=" * 74)
print("""  Action ansatz on the fermion (most general linear, pointwise,
  background-preserving):  T psi(rho,theta) =
      e^{ic a} diag(e^{is1 a}, e^{is2 a}) psi(rho, theta - a),  a = 2pi/3.
  Mode k of winding-N vortex: (lam * A_k(r) e^{ik th}, conj(lam) * B_k(r)
  e^{i(N-1-k) th})  [Majorana/JR conjugation structure].
  T maps mode k -> mode k with lam -> e^{i(c+s1-k)a} lam, PROVIDED the
  conjugate consistency  c+s1-k = -(c+s2-(N-1-k)) (mod 3) holds, i.e.
      2c + s1 + s2 = N - 1 (mod 3)   ... (*) k-INDEPENDENT -> a symmetry.
  Character of mode k:  omega^(m0 - k),  m0 = c + s1 (mod 3).""")

def check_consistency(N):
    # verify (*) is exactly the k-cancellation condition, for all k
    for c in range(3):
        for s1 in range(3):
            for s2 in range(3):
                lhs_ok = (2*c + s1 + s2) % 3 == (N - 1) % 3
                # k-dependence test: phase1(k) = c+s1-k ; phase2(k) must equal
                # -(c+s2-(N-1-k)) for the conjugate pair to transform as one mode
                per_k = [ ((c+s1-k) + (c+s2-(N-1-k))) % 3 for k in range(N) ]
                all_zero = all(p == 0 for p in per_k)
                assert all_zero == lhs_ok, (c, s1, s2)
    return True

for N in (3, 6, 9):
    check_consistency(N)
print("  (*) verified exhaustively over all (c,s1,s2) in Z3^3, N = 3,6,9:")
print("      the k-dependence cancels IFF 2c+s1+s2 = N-1 (mod 3);")
print("      every admissible choice acts on mode k by omega^(m0-k).")

# Verdict-reversal test: can ANY admissible (c,s1,s2) put all 3 modes of the
# N=3 vortex in ONE Z3 sector?  Characters are m0-k mod 3, k = 0,1,2.
reversal_possible = False
for m0 in range(3):
    chars = {(m0 - k) % 3 for k in range(3)}
    if len(chars) == 1:
        reversal_possible = True
assert not reversal_possible
print("  Verdict-reversal test: for every m0 (Wilson line / spin lift /")
print("  Z6 fermionic offset), the N=3 mode characters {m0, m0-1, m0-2} are")
print("  the THREE DISTINCT Z3 characters. All-in-one-sector is IMPOSSIBLE.")
print("  (A k-dependent twist omega^{+k} that would undo the grading is the")
print("   inverse rotation itself: composing it with T removes the action on")
print("   the base point, so the operator no longer implements the orbifold")
print("   identification. Projective escape: H^2(Z3,U(1)) = 0 -- Schur")
print("   multiplier of any cyclic group is trivial -- and a projective phase")
print("   is mode-independent anyway, so it cannot change RELATIVE characters.")
print("   Sector mixing: modes are non-degenerate eigenstates of the very")
print("   rotation generator that defines the quotient -> g acts diagonally.)")

# ---------------------------------------------------------------------------
# A2. Channel count by OUTWARD shooting (independent scheme)
# ---------------------------------------------------------------------------
print()
print("=" * 74)
print("A2. JR CHANNEL COUNT, N = 3, by OUTWARD shooting in rescaled variables")
print("    (p,q) = (a,b) e^{+int f}: bounded p~q <=> normalizable; e^{2r}")
print("    growth of (p-q) <=> not normalizable. Independent of the teams'")
print("    inward-integration scheme.")
print("=" * 74)
def f_profile(r):
    return math.tanh(r)

def rhs_pq(r, y, N, k):
    p, q = y
    fr = f_profile(r)
    return ((k / r) * p + fr * (p - q), ((N - 1 - k) / r) * q + fr * (q - p))

def rk4_step(r, y, h, N, k):
    k1 = rhs_pq(r, y, N, k)
    k2 = rhs_pq(r + h/2, (y[0] + h/2*k1[0], y[1] + h/2*k1[1]), N, k)
    k3 = rhs_pq(r + h/2, (y[0] + h/2*k2[0], y[1] + h/2*k2[1]), N, k)
    k4 = rhs_pq(r + h,   (y[0] + h*k3[0],   y[1] + h*k3[1]),   N, k)
    return (y[0] + h/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]),
            y[1] + h/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1]))

def integ(y, r0, R, N, k, steps=20000):
    snaps = {}
    h = (R - r0) / steps
    r = r0
    for i in range(steps):
        y = rk4_step(r, y, h, N, k)
        r += h
        if abs(r - R/2) < h:
            snaps['half'] = y
    snaps['end'] = y
    return snaps

N, R, eps = 3, 10.0, 1e-3
norm_set = []
for k in range(-2, N + 2):
    rega, regb = (k >= 0), (N - 1 - k >= 0)
    if rega and regb:
        s1 = integ((eps**k if k > 0 else 1.0, 0.0), eps, R, N, k)
        s2 = integ((0.0, eps**(N-1-k) if N-1-k > 0 else 1.0), eps, R, N, k)
        g1 = s1['end'][0] - s1['end'][1]
        g2 = s2['end'][0] - s2['end'][1]
        al, be = g2, -g1                       # cancel the growing direction
        pe = al*s1['end'][0] + be*s2['end'][0]
        ph = al*s1['half'][0] + be*s2['half'][0]
        growth = abs(pe) / max(abs(ph), 1e-300)
        print(f"    k = {k:2d}: growth-cancelled combo |p(R)/p(R/2)| = "
              f"{growth:.3e}  (bounded) -> NORMALIZABLE")
        assert growth < 10.0
        norm_set.append(k)
    else:
        # the unique regular-at-origin solution, correct leading series
        if rega:
            cb = -1.0 / (2*k + 3 - N)
            y0 = (eps**k, cb * eps**(k + 2))
        else:
            q0 = N - 1 - k
            ca = -1.0 / (q0 + 2 - k)
            y0 = (ca * eps**(q0 + 2), eps**q0)
        s = integ(y0, eps, R, N, k)
        growth = (abs(s['end'][0] - s['end'][1])
                  / max(abs(s['half'][0] - s['half'][1]), 1e-300))
        print(f"    k = {k:2d}: regular solution grows |p-q| x{growth:.2e} "
              f"over R/2->R (~e^R = {math.exp(R):.1e}) -> NOT normalizable")
        assert growth > 1e3
assert norm_set == [0, 1, 2]
print("  -> normalizable channels k = {0, 1, 2} exactly: matches op02 v2 and")
print("     both teams (independent outward scheme).  Characters (A1) then")
print("     give sectors (1,1,1): ONE color-singlet generation for N = 3.")

# ---------------------------------------------------------------------------
# B. Beta's Lemma 2: explicit off-apex quotient-charge-1 configuration
# ---------------------------------------------------------------------------
print()
print("=" * 74)
print("B. OFF-APEX IMAGE TRIPLE: Psi ~ (w^3 - w0^3), w0 = 5")
print("=" * 74)
w0 = 5.0
F = lambda w: w**3 - w0**3
# exact Z3 invariance: F(omega w) = (omega w)^3 - w0^3 = w^3 - w0^3 = F(w)
omega = cmath.exp(2j*math.pi/3)
import random
random.seed(7)
max_dev = 0.0
for _ in range(2000):
    w = complex(random.uniform(-20, 20), random.uniform(-20, 20))
    max_dev = max(max_dev, abs(F(omega*w) - F(w)))
assert max_dev < 1e-9
print(f"  Z3 invariance F(omega w) = F(w): max deviation {max_dev:.2e}")
print("  -> the configuration is UNTWISTED (n_c = 0), a well-defined field")
print("     on the quotient (no Z3 obstruction).")

def winding(center, radius, M=20000):
    tot = 0.0
    prev = cmath.phase(F(center + radius))
    for i in range(1, M + 1):
        w = center + radius * cmath.exp(2j*math.pi*i/M)
        ph = cmath.phase(F(w))
        d = ph - prev
        while d > math.pi:  d -= 2*math.pi
        while d < -math.pi: d += 2*math.pi
        tot += d
        prev = ph
    return tot / (2*math.pi)

w_inf  = winding(0.0, 100.0)       # covering winding at infinity
w_apex = winding(0.0, 1.0)         # around the apex (no vortex inside)
w_core = winding(5.0, 1.0)         # around the off-apex core w0
print(f"  covering winding at |w| = 100 : {w_inf:.6f}   (expect 3)")
print(f"  winding around apex  (r = 1)  : {w_apex:.6f}   (expect 0)")
print(f"  winding around w0    (r = 1)  : {w_core:.6f}   (expect 1)")
assert abs(w_inf - 3) < 1e-6 and abs(w_apex) < 1e-6 and abs(w_core - 1) < 1e-6
print("  -> quotient winding n_q = 3/3 = 1 realized with NO apex core and no")
print("     twisted sector: 'n_q = 1 is forbidden' is FALSE (Beta Lemma 2")
print("     CONFIRMED; the #849 sketch's '1 and 2 are confined' is refuted).")

# ---------------------------------------------------------------------------
# C. Energetics WITHOUT the point-vortex formula: direct grid integration
# ---------------------------------------------------------------------------
print()
print("=" * 74)
print("C. APEX N=3 vs IMAGE TRIPLE: direct grid integration of |grad chi|^2")
print("=" * 74)
L, a = 400.0, 1.0
def grad_energy(vortices, Nr=1500, Nth=1024):
    """integrate |sum_i n_i zhat x (r-r_i)/|r-r_i|^2|^2 over disk(L) minus
    core disks radius a; geometric radial grid."""
    r0 = 0.02
    fac = (L / r0) ** (1.0 / Nr)
    E = 0.0
    r = r0
    for i in range(Nr):
        r2 = r * fac
        rm = 0.5 * (r + r2)
        dr = (r2 - r)
        dA = rm * dr * (2*math.pi / Nth)
        for j in range(Nth):
            th = 2*math.pi*(j + 0.5)/Nth
            x, y = rm*math.cos(th), rm*math.sin(th)
            vx = vy = 0.0
            ok = True
            for (cx, cy, n) in vortices:
                dx, dy = x - cx, y - cy
                s2 = dx*dx + dy*dy
                if s2 < a*a:
                    ok = False
                    break
                vx += -n * dy / s2
                vy += n * dx / s2
            if ok:
                E += (vx*vx + vy*vy) * dA
        r = r2
    return E

lnLa = math.log(L / a)
E_apex_pred = 2*math.pi * 9.0 * lnLa
E_apex_num = grad_energy([(0.0, 0.0, 3)])
print(f"  apex N=3 :  grid = {E_apex_num:10.2f}   point-vortex = "
      f"{E_apex_pred:10.2f}   ratio {E_apex_num/E_apex_pred:.4f}")
prev = None
for d in (10.0, 40.0, 100.0):
    vs = [(d*math.cos(2*math.pi*j/3), d*math.sin(2*math.pi*j/3), 1)
          for j in range(3)]
    En = grad_energy(vs)
    Ep = 2*math.pi*(3.0*lnLa + 2*3*math.log(L/(math.sqrt(3.0)*d)))
    print(f"  triple d={d:5.0f}: grid = {En:10.2f}   point-vortex = "
          f"{Ep:10.2f}   ratio {En/Ep:.4f}   < apex? {'YES' if En < E_apex_num else 'NO'}")
    assert En < E_apex_num
    if prev is not None:
        assert En < prev
    prev = En
print("  -> CONFIRMED independently of the point-vortex formula: the apex-")
print("     centred N=3 vortex is NOT the minimum in its (n_q = 1) sector;")
print("     energy decreases monotonically as the cores move off-apex.")
print("     Beta Check C's numbers are legitimate (same L, same a, same")
print("     topological sector: total quotient winding 1 in both).")

# ---------------------------------------------------------------------------
# D. Lefschetz sums (exact)
# ---------------------------------------------------------------------------
print()
print("=" * 74)
print("D. LEFSCHETZ / EQUIVARIANT SUMS (coker = 0 by Weinberg vanishing thm)")
print("=" * 74)
for N in (3, 6, 9):
    for m0 in range(3):
        indg  = sum(omega**((m0 - k) % 3) for k in range(N))
        indg2 = sum((omega**2)**((m0 - k) % 3) for k in range(N))
        assert abs(indg) < 1e-12 and abs(indg2) < 1e-12
        for s in range(3):
            idx = (N + (omega**(-s)).conjugate().conjugate()*0 +
                   sum((omega**(-s*g)) * sum(omega**(g*((m0 - k) % 3))
                       for k in range(N)) for g in (1, 2))) / 3
            assert abs(idx - N/3) < 1e-9
    print(f"  N = {N}: ind(g) = ind(g^2) = 0 exactly; per-sector index = "
          f"{N//3} for ALL m0 and all sectors.")
print("  -> equidistribution is offset-independent (Z6 spin lift, Wilson")
print("     line, gauge embedding all drop out of the per-sector count).")

print()
print("ALL REFEREE CHECKS PASSED.")
