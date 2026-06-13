"""
#849 (third mechanism family) -- Zone-Address Hypothesis Checks
================================================================
Hypothesis under test (author, 2026-06-12): generation = zone-of-origin
address; one mode trapped Jackiw-Rebbi style at three different depths of
the zone-hierarchy descent (real-profile sign changes / kinks at zone
interfaces), so the generation count would be the number of trapping walls
in the WRITTEN corpus solutions.

Numerical method note (honesty): zero modes of the 1D Dirac operator
H = -i s1 d/dy + m(y) s2 are counted via the SUSY-pair Schroedinger
operators  H_- = a' a = -d2 + m^2 - m'   (chirality -, ker a, psi ~ e^{-int m})
           H_+ = a a' = -d2 + m^2 + m'   (chirality +, ker a', psi ~ e^{+int m})
because a naive square-matrix block discretization on a Dirichlet box
FORCES dim ker A = dim ker A' (rank-nullity) -- the continuum index is
recovered only in the second-order formulation, where Dirichlet boxes are
safe and there is no fermion doubling. (We verified the naive block method
fails exactly this way: it returns a spurious box-edge partner mode.)
Exact theorem used alongside: every E != 0 eigenmode of a chiral H has
<s3> = 0 exactly (s3 maps E to -E eigenspaces) -- gapped pairs are
automatically vector-like.

Checks (numpy; Python 3.12):
  C1  op03 kink ODE sign audit (tanh solves PHI'' = k^2(PHI^3-PHI), NOT
      the sign written in op03_condensate_bvp_solve.py docstring/RHS)
  C2  Jackiw-Rebbi zero mode at the Firmament wall (odd-extended op03
      kink): exactly ONE normalizable zero mode, single chirality
  C3  Three-wall profile (kink/antikink/kink): ONE chiral zero mode +
      ONE gapped vector-like pair -> net chiral count = 1, never 3;
      pair splitting decreases with wall separation
  C4  Crossing-parity lemma: up/down crossings of any continuous m(y)
      interlace; net index = (sgn m(+inf)-sgn m(-inf))/2 in {-1,0,+1}
  C5  Wall inventory from the written corpus profiles
  C6  App-C bound-state window vs op03-DERIVED V0 = kappa^2/2
  C7  Salvage probe: radial ADDRESSES of the three verified vortex modes
      psi_k ~ r^k e^{-int f} (op02 v2); toy Yukawa hierarchy (model
      profile, NOT corpus-exact)

Run: python zone_address_checks.py     (all checks print PASS/FAIL)
Date: 2026-06-12
"""

import numpy as np

PASS = []


def report(name, ok, detail=""):
    PASS.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"         {line}")


print("=" * 72)
print("C1  op03 kink ODE sign audit")
print("=" * 72)
# op03_condensate_bvp_solve.py writes the BVP as  PHI'' = k^2 (PHI - PHI^3)
# and claims PHI = tanh(k eta/sqrt2) solves it. Analytic fact:
#   d2/deta2 tanh(k eta/sqrt2) = k^2 (tanh^3 - tanh) = -k^2(PHI - PHI^3).
# So tanh solves PHI'' = k^2(PHI^3 - PHI)  (Mexican-hat EOM, correct kink);
# the RHS sign in the op03 docstring/check is a typo. Everything
# downstream (slope k/sqrt2, V0 = k^2/2, wall width) is unaffected.
kappa = 2.0
eta = np.linspace(-8, 8, 400001)
h = eta[1] - eta[0]
phi = np.tanh(kappa * eta / np.sqrt(2))
phi_pp = (phi[2:] - 2 * phi[1:-1] + phi[:-2]) / h**2     # 2nd-order FD
mid = slice(1, -1)
rhs_op03 = kappa**2 * (phi[mid] - phi[mid] ** 3)          # as written in op03
rhs_corr = kappa**2 * (phi[mid] ** 3 - phi[mid])          # correct sign
res_op03 = np.max(np.abs(phi_pp - rhs_op03))
res_corr = np.max(np.abs(phi_pp - rhs_corr))
report(
    "tanh kink solves PHI''=k^2(PHI^3-PHI); op03's written RHS sign is a typo",
    res_corr < 1e-5 and res_op03 > 1.0,
    f"residual vs corrected RHS : {res_corr:.3e}  (machine/FD level)\n"
    f"residual vs op03 RHS      : {res_op03:.3e}  (O(1) -- sign error)\n"
    f"NOTE op03's own §2 'residual' printout at kappa=2 actually evaluates\n"
    f"to ~{res_op03:.2f}, mislabeled 'finite-difference error'. Downstream\n"
    f"results (slope kappa/sqrt2, V0=kappa^2/2) use the kink itself: unaffected.",
)


# ---------------------------------------------------------------------------
def susy_spectra(m_func, L=30.0, N=6000, nev=6):
    """Lowest eigenvalues of H_- = -d2 + m^2 - m' and H_+ = -d2 + m^2 + m'
    on a Dirichlet box [-L, L]; returns (E_minus, E_plus, y, ground_minus)."""
    y = np.linspace(-L, L, N)
    hh = y[1] - y[0]
    m = m_func(y)
    mp = np.gradient(m, y)
    diag_kin = np.full(N, 2.0 / hh**2)
    off = np.full(N - 1, -1.0 / hh**2)
    out = []
    gs = None
    for s in (-1.0, +1.0):
        V = m**2 + s * mp
        Hmat = np.diag(diag_kin + V) + np.diag(off, 1) + np.diag(off, -1)
        w, v = np.linalg.eigh(Hmat)
        out.append(w[:nev])
        if s < 0:
            gs = v[:, 0]
    return out[0], out[1], y, gs


print()
print("=" * 72)
print("C2  Jackiw-Rebbi zero mode at the Firmament wall (op03 kink)")
print("=" * 72)
# The corpus couples the 6D Dirac probe to the condensate via Yukawa
# (op03 scripts: S_Yuk = int chi* g_YB PHI chi ; ACTION_6D_COMPLETE.md
# §7.3). Mass profile m(eta) = g_YB * PHI(eta). op03's BVP has PHI(0)=0 at
# the Firmament with the WB bulk on eta'>0; the Z2 reflection across the
# Firmament used by RT-1.WF §2.3 supplies the odd extension: a genuine
# sign-changing JR wall AT the Firmament.
g = 1.0
kap = 2.0
m_kink = lambda y: g * np.tanh(kap * y / np.sqrt(2))
# zero-mode threshold: discretization shifts the exact zero to O(h^2) ~ 1e-5;
# the physical gap is O(1). tol = 1e-3 separates them by 3 decades each way.
TOL0 = 1e-3
Em, Ep, y, gs = susy_spectra(m_kink, N=8000)
n_minus = int(np.sum(np.abs(Em) < TOL0))
n_plus = int(np.sum(np.abs(Ep) < TOL0))
# analytic zero mode: cosh(kap y/sqrt2)^(-g*sqrt2/kap)
ana = np.cosh(kap * y / np.sqrt(2)) ** (-g * np.sqrt(2) / kap)
ana /= np.max(ana)
num = np.abs(gs) / np.max(np.abs(gs))
prof_err = np.max(np.abs(num - ana))
report(
    "exactly ONE zero mode, chirality (-) only; JR profile matches analytic",
    n_minus == 1 and n_plus == 0 and prof_err < 2e-3,
    f"H_- spectrum (lowest 3): {Em[0]:.2e}, {Em[1]:.4f}, {Em[2]:.4f}  -> {n_minus} zero mode(s)\n"
    f"H_+ spectrum (lowest 3): {Ep[0]:.4f}, {Ep[1]:.4f}, {Ep[2]:.4f}  -> {n_plus} zero mode(s)\n"
    f"index = dim ker H_- minus dim ker H_+ = {n_minus - n_plus}\n"
    f"max |numeric - analytic| zero-mode profile deviation: {prof_err:.2e}",
)

print()
print("=" * 72)
print("C3  Three walls from ONE profile: vector-like doubling (kill test)")
print("=" * 72)
# m(y) with 3 sign changes (kink at -a, ANTIkink at 0, kink at +a).
# A single continuous profile CANNOT have three same-sign crossings (C4),
# so alternating walls are the only 3-wall option. Prediction: 1 exact
# chiral zero mode + 1 vector-like pair at +-eps(a), eps^2 appearing in
# BOTH H_- and H_+ (SUSY pairing of all E != 0 levels), eps -> 0 only as
# a -> inf. Exact theorem: every E != 0 mode of the chiral H has <s3> = 0
# (s3 maps E <-> -E eigenspaces) -- the pair is exactly non-chiral, i.e.
# a 4D-MASSIVE Dirac fermion, not two extra generations.
# separations chosen so the pair's eps^2 stays >> the O(h^2) ~ 1e-5
# discretization shift of the exact zero (clean scale separation)
eps_list = []
for a in (3.0, 4.0, 5.0):
    m3 = lambda yv, a=a: g * np.tanh(yv + a) * np.tanh(yv) * np.tanh(yv - a)
    Em3, Ep3, y3, _ = susy_spectra(m3, L=30.0, N=8000)
    eps = np.sqrt(max(Ep3[0], 0.0))
    eps_list.append(eps)
    tol3 = max(1e-4, 0.05 * Ep3[0])
    nm = int(np.sum(np.abs(Em3) < tol3))
    npl = int(np.sum(np.abs(Ep3) < tol3))
    pair_match = abs(Em3[1] - Ep3[0]) / max(Ep3[0], 1e-300)
    print(f"   a = {a:4.1f}: ker H_- = {nm}, ker H_+ = {npl}, "
          f"pair E = +-{eps:.3e} (SUSY match {pair_match:.1e})")
ok3 = (nm == 1 and npl == 0
       and eps_list[0] > eps_list[1] > eps_list[2] > 0
       and pair_match < 1e-2)
report(
    "3 walls -> index 1: one chiral zero + one gapped vector-like pair, never 3",
    ok3,
    f"pair splitting falls with separation ({eps_list[0]:.2e} -> {eps_list[2]:.2e})\n"
    f"but is finite at any finite separation: walls 2+3 bind a massive\n"
    f"vector-like fermion (<s3> = 0 exactly for E != 0), not two generations.",
)

print()
print("=" * 72)
print("C4  Crossing-parity lemma (why the count can NEVER be 3)")
print("=" * 72)
# Lemma: for continuous m with m(+-inf) != 0, sign changes alternate
# up/down; net index of -i s1 dy + m s2 equals
# (sgn m(+inf) - sgn m(-inf))/2 in {-1, 0, +1}.
rng = np.random.default_rng(8491)
ok_all = True
for trial in range(200):
    c = rng.normal(size=6)
    yv = np.linspace(-20, 20, 20001)
    prof = np.tanh(yv / 3) * c[0] + sum(
        c[i] * np.sin(0.3 * i * yv) * np.exp(-((yv / 14) ** 2)) for i in range(1, 6)
    )
    prof += 0.05 * np.sign(c[0]) if c[0] != 0 else 0.05
    s = np.sign(prof)
    flips = np.where(np.diff(s) != 0)[0]
    ups = sum(1 for i in flips if s[i + 1] > s[i])
    downs = sum(1 for i in flips if s[i + 1] < s[i])
    net = (np.sign(prof[-1]) - np.sign(prof[0])) / 2
    if not (abs(ups - downs) <= 1 and ups - downs == net):
        ok_all = False
        break
report(
    "200 random profiles: N_up - N_down = net index in {-1,0,+1} always",
    ok_all,
    "Three SAME-chirality JR walls require three up-crossings with no\n"
    "down-crossings -- impossible for one continuous real profile (IVT).\n"
    "=> a single-field descent can never trap 3 same-chirality modes.",
)

print()
print("=" * 72)
print("C5  Wall inventory from the WRITTEN corpus solutions")
print("=" * 72)
inventory = [
    ("Z2 | Z2.2  (Earth Prime -> Firmament Domain; registry rows Z1|Z2.1, Z2.1|Z2.2)",
     "NO  - no field solution written; Psi_A/Psi_B/warp undefined on the Z2.1 (atemporal) side"),
    ("Z2.2 | Z2.2.2  (domain -> membrane; the Firmament surface eta'=0)",
     "YES - Psi_B kink PHI=tanh(k eta'/sqrt2), PHI(0)=0 (op03) + warp-A kink (RT-1.WF JC-xi/JC-eta)"),
    ("Z2.2.2 | Z2.2.2.1  (membrane -> condensed matter)",
     "NO  - Z2.2.2.1 is matter ON the membrane (Day 3 phase), not a surface in (xi,eta); no profile"),
    ("xi = xi_A  (Waters Above outer interface)",
     "NO  - delta-potential g'_bdy|Psi_A|^2 (ACTION_6D §8.2); |Psi_A| -> VEV; modulus >= 0 never sign-changes"),
    ("eta = eta_B  (Waters Below outer interface)",
     "NO  - op03 kink has PHI -> 1 (no second crossing); §11.2 Neumann/Dirichlet menus, no written sign change"),
]
for iface, status in inventory:
    print(f"   {iface}\n      {status}")
n_walls = sum(1 for _, s in inventory if s.startswith("YES"))
report(
    f"trapping walls in written solutions = {n_walls} (hypothesis needs 3)",
    n_walls == 1,
    "The corpus's actual solutions contain exactly ONE sign-changing real\n"
    "profile -- at the Firmament. Count = 1, not 3.",
)

print()
print("=" * 72)
print("C6  App-C 3-bound-state window vs op03-DERIVED V0")
print("=" * 72)
# TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md App C.4: exactly 3 bound
# states iff lambda = depth*width^2 in (0.1, 0.5) -- explicitly a
# fine-tuned window. op03 closure DERIVES V0 = kappa^2/2 with
# kappa_req = 21.78 (alpha_obs chain) => V0 = 237 (eta_B units).
M_TAU, M_MU, M_E = 1776.86, 105.658, 0.511
alpha_obs = 0.5 * (np.log(M_TAU / M_MU) / 3 + np.log(M_TAU / M_E) / 8)
DXI, L_xi = 0.3, 1.0
kappa_req = alpha_obs / (DXI**2 / (2 * L_xi))
V0_derived = kappa_req**2 / 2
lam_canonical = 0.002 * 1.0**2       # Ch 10 canonical V0=0.002, width ~ L=1
lam_derived = V0_derived * DXI**2    # generation-spacing width 0.3
report(
    "derived V0 leaves the App-C 3-state window => radial-resonance count NOT rescued",
    not (0.1 < lam_derived < 0.5) and not (0.1 < lam_canonical < 0.5),
    f"alpha_obs = {alpha_obs:.4f}, kappa_req = {kappa_req:.2f}, V0 = kappa^2/2 = {V0_derived:.1f}\n"
    f"lambda(derived)            = V0*Dxi^2 = {lam_derived:.1f}   vs window (0.1, 0.5)\n"
    f"lambda(canonical V0=0.002) = {lam_canonical:.3f}            vs window (0.1, 0.5)\n"
    f"Under op03's own derived V0 the App-C 'exactly 3 bound states' window is\n"
    f"missed by ~40x (and the canonical value sits BELOW the floor): the well\n"
    f"count was never 3 by anything written; the zone-address hypothesis cannot\n"
    f"inherit it as a topological upgrade.",
)

print()
print("=" * 72)
print("C7  Salvage probe: radial ADDRESSES of the three verified vortex modes")
print("=" * 72)
# op02 v2 (verified): three same-chirality zero modes psi_k ~ r^k e^{-int f},
# k=0,1,2, of the n=3 vortex. They peak at increasing radius -> three
# different RADIAL addresses in the fiber (NOT zone walls). Toy hierarchy:
# Yukawa overlap with a localized weight w(r) = e^{-r/r_Y}.
# MODEL PROFILE f = v tanh(r/r0) -- not corpus-exact; feasibility only.
v_, r0_ = 1.0, 1.0
r = np.linspace(1e-6, 60, 240001)
f = v_ * np.tanh(r / r0_)
F = np.concatenate(([0.0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(r))))
peaks, means, yuk = [], [], []
r_Y = 2.0
trapz = np.trapezoid if hasattr(np, "trapezoid") else getattr(np, "trapz")
for k in range(3):
    amp2 = (r**k * np.exp(-F)) ** 2          # |psi_k|^2 (unnormalized)
    dens = amp2 * r                          # measure r dr
    norm = trapz(dens, r)
    dens /= norm
    peaks.append(r[np.argmax(amp2)])
    means.append(trapz(r * dens, r))
    yuk.append(trapz(np.exp(-r / r_Y) * dens, r))
hier = [yuk[0] / yuk[k] for k in range(3)]
report(
    "three modes sit at three distinct radial addresses; overlaps strictly ordered",
    peaks[0] < peaks[1] < peaks[2] and yuk[0] > yuk[1] > yuk[2],
    f"peak radii   r_k : {peaks[0]:.2f}, {peaks[1]:.2f}, {peaks[2]:.2f}\n"
    f"mean radii  <r>_k: {means[0]:.2f}, {means[1]:.2f}, {means[2]:.2f}\n"
    f"toy Yukawa ratios y_0/y_k: 1, {hier[1]:.2f}, {hier[2]:.2f}\n"
    f"(model profile; the corpus-exact overlap vs exp(-alpha n^2) is the\n"
    f" named deciding computation -- NOT claimed here)",
)

print()
print("=" * 72)
print(f"OVERALL: {sum(PASS)}/{len(PASS)} checks pass")
print("=" * 72)
