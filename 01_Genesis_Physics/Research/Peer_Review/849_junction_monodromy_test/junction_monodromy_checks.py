"""
Numerical checks for the #849 (sharpened) junction-monodromy derivation attempt:
  "n_q = 3 because the Waters-Above phase accumulates one quantized unit of
   U(1)_A monodromy per zone junction on the canonical descent Z0 -> Firmament,
   and that descent crosses exactly three junctions."

Checks:
  1. BOOKKEEPING (Part C.ii): exact roots-of-unity Lefschetz arithmetic for the
     covering winding N = 9 (n_q = 3): ind(1) = 9, ind(g) = ind(g^2) = 0,
     per-sector equivariant index = 3 in EVERY Z3 sector (3 color-singlet
     generations + colored partners). Confirms the verified machinery the
     hypothesis would feed IF n_q = 3 were established.
  2. PHASE-BLINDNESS OF JUNCTION CONDITIONS (Part A): solve the global-vortex
     profile equation with a model zone junction at r_J (VEV/warp jump + Israel
     delta-tension term -- the only junction structures the corpus writes:
     ACTION_6D_COMPLETE Sec. 8.2/11, AXIOM_METRIC_DISCONTINUITY, op01 sigma).
     A regular finite solution exists for EVERY winding n in {1,2,3,5}:
     the junction transmits all windings and quantizes nothing.
  3. NON-ACCUMULATION / HOMOTOPY (Part A): for the referee's exactly
     Z3-invariant configuration Psi = w^3 - w0^3, the winding measured on a
     loop depends ONLY on the vortex cores it encloses, NOT on how many
     "junction surfaces" the radial descent to that loop crosses. Crossing a
     junction deposits zero monodromy unless the junction itself carries a
     vortex sheet -- which no corpus equation provides.
  4. JUNCTION-COUNT TABLE (Part B): enumeration of the descent Z0 -> Z2.2.2
     under every defensible counting convention; the count is convention-
     dependent (2, 3, 3', 4), with "3" arising only under curated conventions
     -- and the two conventions that give 3 give DIFFERENT junction sets.
  5. Z3-UNIT SUB-VERSION ARITHMETIC: if the per-junction unit is a Z3 twist
     (the only unit with any orbifold motivation), 3 junctions give
     omega^3 = 1 = the UNTWISTED condition -- zero winding information, not
     winding 3.

Pure Python 3.12 (math/cmath only, matching the race scripts). 2026-06-12.
"""
import cmath
import math

ok_all = True

# ---------------------------------------------------------------------------
print("=" * 76)
print("CHECK 1: Lefschetz bookkeeping for n_q = 3 (covering N = 9), exact")
print("=" * 76)
w = cmath.exp(2j * cmath.pi / 3)
for N in (3, 9):
    ind_1 = N
    ind_g = sum(w ** (-k) for k in range(N))
    ind_g2 = sum(w ** (-2 * k) for k in range(N))
    idx = []
    for s in range(3):
        val = (ind_1 + (w ** s).conjugate() * ind_g
               + (w ** (2 * s)).conjugate() * ind_g2) / 3
        idx.append(val)
    print(f"  N = {N}: ind(1) = {ind_1}, |ind(g)| = {abs(ind_g):.2e}, "
          f"|ind(g^2)| = {abs(ind_g2):.2e}")
    print(f"          per-sector index = {[f'{v.real:+.6f}' for v in idx]}  "
          f"(expect {N // 3} each)")
    ok = all(abs(v - N / 3) < 1e-12 for v in idx)
    ok_all &= ok
    print(f"          -> {'PASS' if ok else 'FAIL'}: index_s = N/3 = {N // 3} "
          f"in every sector")
print("  Conclusion: IF n_q = 3 (N = 9) were established, the equivariant index")
print("  yields exactly 3 zero modes per Z3 sector: 3 color-singlet generations")
print("  + colored partners, 9 = 3 x 3. The downstream machinery is sound.")

# ---------------------------------------------------------------------------
print()
print("=" * 76)
print("CHECK 2: A model zone junction transmits EVERY winding n (phase-blind)")
print("=" * 76)
print("  Profile eq. (Vol 4 Ch 10 eq. 4.10.11, dimensionless):")
print("    f'' + f'/r - n^2 f/r^2 + (w(r)^2 - f^2) f - (lam_J/h) delta_{r,rJ} f = 0")
print("  with VEV/warp jump  w(r) = 1 (r < rJ = 4),  w = 0.65 (r > rJ)  and an")
print("  Israel-type delta tension lam_J = 0.5 at the junction. These are the")
print("  ONLY junction structures the corpus writes (|Psi|^2 boundary terms,")
print("  metric/extrinsic-curvature jumps): ALL invariant under")
print("  Psi_A -> e^{i alpha} Psi_A.")


def solve_profile(n, R=20.0, M=4000, rJ=4.0, lamJ=0.5, w_in=1.0, w_out=0.65):
    """Damped Newton on the discretized radial vortex profile with a junction.

    Tridiagonal Jacobian solved by the Thomas algorithm. f(0) = 0 ghost node,
    outer Dirichlet f(R) = w_out.
    """
    h = R / M
    r = [h * (i + 1) for i in range(M)]
    wv = [w_in if ri < rJ else w_out for ri in r]
    jnode = int(round(rJ / h)) - 1
    f = [wv[i] * math.tanh(r[i]) for i in range(M)]
    f[-1] = w_out
    res = float("inf")
    for _ in range(300):
        F = [0.0] * M
        for i in range(M):
            fm = f[i - 1] if i > 0 else 0.0
            fp = f[i + 1] if i < M - 1 else w_out
            F[i] = ((fp - 2 * f[i] + fm) / h**2
                    + (fp - fm) / (2 * h * r[i])
                    - n**2 * f[i] / r[i]**2
                    + (wv[i]**2 - f[i]**2) * f[i])
        F[jnode] -= (lamJ / h) * f[jnode]
        F[-1] = 0.0
        # tridiagonal Jacobian
        lo = [1 / h**2 - 1 / (2 * h * r[i]) for i in range(M)]
        hi = [1 / h**2 + 1 / (2 * h * r[i]) for i in range(M)]
        di = [-2 / h**2 - n**2 / r[i]**2 + wv[i]**2 - 3 * f[i]**2
              for i in range(M)]
        di[jnode] -= lamJ / h
        di[-1], lo[-1], hi[-1] = 1.0, 0.0, 0.0
        # Thomas solve J df = -F
        b = di[:]
        d = [-x for x in F]
        for i in range(1, M):
            m = lo[i] / b[i - 1]
            b[i] -= m * hi[i - 1]
            d[i] -= m * d[i - 1]
        df = [0.0] * M
        df[-1] = d[-1] / b[-1]
        for i in range(M - 2, -1, -1):
            df[i] = (d[i] - hi[i] * df[i + 1]) / b[i]
        f = [f[i] + 0.8 * df[i] for i in range(M)]
        res = max(abs(F[i]) for i in range(M - 1))
        if res < 1e-10:
            break
    # gradient energy within R (finite part; the overall log divergence is the
    # usual global-vortex IR log, identical physics for the junction question)
    E = 0.0
    for i in range(M - 1):
        fp = (f[i + 1] - f[i]) / h
        rm = 0.5 * (r[i] + r[i + 1])
        fm = 0.5 * (f[i] + f[i + 1])
        E += (fp**2 * rm + n**2 * fm**2 / rm) * h
    E *= math.pi
    return f, res, E


print(f"  {'n':>3} {'max residual':>14} {'f>0, regular':>13} {'E_grad(R=20)':>13}")
for n in (1, 2, 3, 5):
    f, res, E = solve_profile(n)
    regular = all(x > 0 and math.isfinite(x) for x in f)
    okn = res < 1e-8 and regular
    ok_all &= okn
    print(f"  {n:>3} {res:>14.2e} {str(regular):>13} {E:>13.3f}   "
          f"{'PASS (solution exists)' if okn else 'FAIL'}")
print("  Conclusion: the junction (VEV jump + delta tension) admits a regular")
print("  finite solution for EVERY winding n. Nothing in the corpus's junction")
print("  conditions quantizes, forbids, or selects any value of n: they couple")
print("  only to |Psi_A| and the metric, never to the phase. No route to")
print("  'exactly +-1 unit per junction' exists in these equations.")

# ---------------------------------------------------------------------------
print()
print("=" * 76)
print("CHECK 3: Winding does not accumulate across junctions (homotopy)")
print("=" * 76)
w0 = 2.0  # cores of Psi = w^3 - w0^3 at radius 2, angles 0, +-2pi/3


def covering_winding(rho, npts=20000):
    total = 0.0
    prev = cmath.phase((rho + 0j)**3 - w0**3)
    for j in range(1, npts + 1):
        th = 2 * math.pi * j / npts
        z = rho * cmath.exp(1j * th)
        cur = cmath.phase(z**3 - w0**3)
        d = cur - prev
        while d > math.pi:
            d -= 2 * math.pi
        while d < -math.pi:
            d += 2 * math.pi
        total += d
        prev = cur
    return total / (2 * math.pi)


scenarios = [
    ("loop rho=1.9, 0 junctions crossed (descent from rho=0)", 1.9, 0),
    ("loop rho=1.9, 3 junctions crossed (rJ = 0.5, 1.2, 1.7)", 1.9, 3),
    ("loop rho=2.5, 0 junctions beyond cores", 2.5, 0),
    ("loop rho=8.0, 3 junctions crossed (rJ = 3, 4, 5)", 8.0, 3),
]
print("  Z3-invariant background Psi = w^3 - w0^3 (referee's Lemma-2 witness;")
print("  untwisted, cores at |w| = 2). Covering winding N on loops, with")
print("  hypothetical junction surfaces placed at various radii in core-free")
print("  shells (junction placement CANNOT affect the line integral):")
for label, rho, njunc in scenarios:
    Nw = covering_winding(rho)
    expect = 0 if rho < 2 else 3
    okn = abs(Nw - expect) < 1e-6
    ok_all &= okn
    print(f"   {label:<58} N = {Nw:+.6f} (expect {expect}) "
          f"{'PASS' if okn else 'FAIL'}")
print("  Conclusion: winding changes ONLY where vortex cores sit (|w| = 2),")
print("  never at junction surfaces. 'One unit per junction crossed' would")
print("  require each junction to carry a quantized vortex SHEET (a source of")
print("  vorticity localized on the interface) -- a structure present in no")
print("  corpus equation. Crossing N junctions deposits exactly 0.")

# ---------------------------------------------------------------------------
print()
print("=" * 76)
print("CHECK 4: Junction count of the descent Z0 -> Z2.2.2 by convention")
print("=" * 76)
conventions = [
    ("C1 author's list (Z0|Z1, Z1|Z2, Z2.2.3|Z2.2.2)", 3,
     "mixed granularity: coarse Z1|Z2 but fine Z2.2.3|Z2.2.2; skips Z2.1|Z2.2"),
    ("C2 full nested tree path Z0|Z1, Z1|Z2.1, Z2.1|Z2.2, Z2.2.3|Z2.2.2", 4,
     "every interface listed in canon (Table 4 + op01 sigma) that the path crosses"),
    ("C3 Table 4 registry only (Z1|Z2.1, Z2.1|Z2.2, Z2.2.3->Z2.2)", 3,
     "DIFFERENT set than C1: excludes Z0|Z1 (absent from Table 4), incl. Z2.1|Z2.2"),
    ("C4 junctions where Psi_A exists & has boundary terms (xi=xi_A, Firmament)", 2,
     "ACTION_6D Sec. 8.2: Psi_A boundary terms at xi=xi_A and the Firmament ONLY;"
     " Psi_A is not defined on Z0 or Z1 (sourced in Zone 2.3, AXIOM_WATERS_DUALITY)"),
    ("C5 primary zones (Z0, Z1, Z2) -> internal junctions between them", 2,
     "3 zones = 2 fenceposts; '3' here counts zones, not junctions"),
    ("C6 nesting depth of the membrane label Z2.2.2", 3,
     "counts subscript levels, not junctions: a notational artifact"),
]
print(f"  {'convention':<72} {'count'}")
for label, count, note in conventions:
    print(f"  {label:<72} {count}")
    print(f"      note: {note}")
counts = sorted({c for _, c, _ in conventions})
print(f"  Distinct counts across defensible conventions: {counts}")
print("  '3' appears only under C1/C3/C6 -- and C1 and C3 are DIFFERENT junction")
print("  sets, while C6 counts notation. The physically-relevant convention (C4:")
print("  interfaces the Psi_A phase can actually traverse) gives 2.")
print("  -> The count 3 is convention-dependent: NUMEROLOGY criterion met.")

# ---------------------------------------------------------------------------
print()
print("=" * 76)
print("CHECK 5: The Z3-unit sub-version self-cancels")
print("=" * 76)
unit = cmath.exp(2j * cmath.pi / 3)
acc = unit**3
print(f"  One Z3 twist per junction, 3 junctions: omega^3 = "
      f"{acc.real:+.0f}{acc.imag:+.0f}i = 1")
print("  -> three Z3 units compose to the UNTWISTED boundary condition (Team")
print("     Beta's N2, already canon-recommended) -- i.e. ZERO winding")
print("     information, not n_q = 3. The only per-junction unit with any")
print("     orbifold motivation cancels; a full-2pi unit per junction has no")
print("     corpus motivation at all. The two sub-versions are mutually")
print("     exclusive and each fails separately.")
ok_all &= abs(acc - 1) < 1e-12

print()
print("=" * 76)
print(f"ALL CHECKS {'PASS' if ok_all else 'CONTAIN FAILURES'}")
print("=" * 76)
