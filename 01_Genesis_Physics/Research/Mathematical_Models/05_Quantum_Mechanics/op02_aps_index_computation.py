"""
OP-02 Closure: Twisted Index Computation — Spin-1/2 and Three Generations
==========================================================================
Prior work (op02_kahler_spinor_derivation.md) established:
  1. The Z2 extra-dimensional 2-manifold M_perp is automatically Kähler
  2. M_perp admits a natural spinor bundle via the Dolbeault complex
  3. KK reduction gives 4D spin-1/2 fermions from Kähler Dirac zero modes
  4. GAP: The number of zero modes = index of the Dirac operator on M_perp
     TWISTED by the U(1)_A winding gauge field (the Firmament vortex).

This script closes that gap — correctly this time.

v1 (2026-05-14) computed the index of the UNTWISTED Dirac operator and got
-1/2, then asserted "+3" in prose.  That is the bug tracked as GitHub #851.
v2 computes the index of the GAUGE-TWISTED operator.  The bulk index density
then contains the first Chern class c1 = (1/2π)∮A·dl = n_w, which is exactly
the term v1 dropped — and exactly what carries the 3.

THEOREMS USED (cited, not invented — both already in the framework):
  * Jackiw–Rossi (Nucl. Phys. B190, 681 (1981)): a winding-n vortex traps
    exactly |n| normalizable fermionic zero modes.
    [Framework refs: op02_kahler_spinor_derivation.md Route 1
     ("the JR theorem gives index(D_ψ) = n_w");
     TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md Appendix A.]
  * E. J. Weinberg (Phys. Rev. D 24, 2669 (1981)): index(D_A) = n for the
    fermion–vortex system (Callias-type open-space index), with a VANISHING
    THEOREM: all n zero modes carry the SAME chirality.
  * APS I (Math. Proc. Camb. Phil. Soc. 77, 43 (1975)): on a manifold with
    boundary, index(D_A) = ∫ Â(R) ∧ ch(F) − (h + η(0))/2.  v1 used this
    formula but with ch(F) → 1 (untwisted): see §0.

Physical setup:
  - M_perp: the 2D (ξ,η)-manifold of zone Z2, with warp metric
  - The Firmament vortex: U(1)_A order parameter φ = f(r) e^{i n_w θ}
    with winding n_w (Postulate F: n_w = 3, ADOPTED zone-architecture axiom)
  - D_A: Dirac operator on M_perp twisted by the U(1)_A winding field

AXIOM DEPENDENCY (state it wherever the "3" is used):
  n_w = 3 is Postulate F, an ADOPTED axiom (Author Ratification #1,
  2026-06-11; AXIOM_GODHEAD_ZONE_Z0.md §4).  Board issue #849 tracks
  deriving it.  This script derives  index = n_w ;  it does NOT derive
  n_w = 3.

Date: 2026-05-14 (v1) | v2: 2026-06-11 — GitHub #851 fix
Status: index(D_A) = n_w COMPUTED (Chern term + explicit JR zero modes +
        numerical shooting); = 3 GIVEN Postulate F (n_w = 3)
"""

import math
import sys

# Windows consoles fall back to cp1252 when stdout is redirected; this file
# prints Unicode math symbols, so force UTF-8 (adversarial-verification fix).
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

LN10 = math.log(10.0)

print("=" * 68)
print("OP-02 CLOSURE v2: Twisted Index Computation for Zone Z2 2-Manifold")
print("(GitHub #851 fix: the index is now COMPUTED, not narrated)")
print("=" * 68)

# ─── §0  WHAT WAS WRONG IN V1 ────────────────────────────────────────────────
print("""
§0  WHAT WAS WRONG IN V1
─────────────────────────
v1 evaluated the APS formula for the UNTWISTED Dirac operator:

    index_v1 = ∫ Â(R)  −  h/2  −  η(0)/2          (no gauge twist anywhere)
             =   1/2   −  0    −  (n_w − 1)/2

For n_w = 3 this is 1/2 − 1 = −1/2, and v1's own cross-check table showed
NO winding number giving +3.  v1 then asserted "+3" in a prose paragraph
("sum over sectors / chirality projection") that was never computed.

The root cause: the physical operator is the Dirac operator TWISTED by the
U(1)_A winding gauge field of the Firmament vortex.  For a twisted operator
the APS bulk term is  ∫ Â(R) ∧ ch(F),  and in 2D

    ∫ ch(F) = c1 = (1/2π) ∮ A·dl = n_w     (first Chern class = winding)

v1 set ch(F) → 1, i.e. it dropped the Chern term entirely.  The dropped
term is exactly what carries the 3.  v1's −1/2 is the index of an operator
that does not see the vortex at all — meaningless for the twisted problem
(and its η(0) bookkeeping mixed a twisted boundary spectrum with an
untwisted bulk term, which is internally inconsistent).
""")

# Reproduce v1's number explicitly, labelled as wrong:
n_w = 3          # Postulate F (ADOPTED axiom — dependency stated in header)
A_hat_untwisted = 0.5          # χ(disk)/2, v1 §4
h_boundary      = 0            # v1 §2
eta0_v1         = n_w - 1      # v1 §3
index_v1 = A_hat_untwisted - h_boundary / 2.0 - eta0_v1 / 2.0
print(f"    v1 (UNTWISTED, WRONG for this problem):")
print(f"      index_v1 = {A_hat_untwisted} - {h_boundary}/2 - {eta0_v1}/2 "
      f"= {index_v1}   ≠ 3  ← the #851 bug")

# ─── §1  Corrected index formula: the gauge-twisted Dirac operator ───────────
print("""
§1  CORRECTED INDEX FORMULA — THE TWISTED DIRAC OPERATOR
─────────────────────────────────────────────────────────
The Firmament vortex is the U(1)_A order-parameter configuration

    φ(r, θ) = f(r) e^{i n_w θ},   f(0) = 0,   f(∞) = v

on the (ξ,η)-disk (r, θ = polar coordinates about the vortex axis).
Fermionic excitations couple to this background; the relevant operator is
the TWISTED Dirac operator D_A.  Its index:

    index(D_A) = ∫_M Â(R) ∧ ch(F)  −  (h + η(0))/2        [APS 1975]

In 2D the degree-2 part of Â(R) ∧ ch(F) is  Â_0·c1(F) + Â_2·1, so the new
(previously dropped) bulk piece is the first Chern class

    c1 = (1/2π) ∫_M F = (1/2π) ∮_{∂M} A·dl = n_w .

For the fermion–vortex system the total — bulk Chern term plus all
boundary/η corrections — is computed exactly by Weinberg (1981) and
Jackiw–Rossi (1981) [Callias-type open-space index]:

    index(D_A) = n_w        (exactly; no leftover fractional part)

Below: c1 is computed numerically two ways (§2), the JR zero modes are
constructed explicitly (§3), and the count is verified by direct numerical
integration of the zero-mode ODEs (§4–§5), including the chirality
asymmetry that makes the index +3 rather than 0 (§6).
""")

# ─── §2  The Chern term, computed ────────────────────────────────────────────
print("§2  THE CHERN TERM c1 — COMPUTED, TWO WAYS")
print("─" * 45)

# (a) winding of the order-parameter phase: (1/2π) ∮ d(arg φ)
M_seg = 3600
total_dphase = 0.0
prev = math.atan2(math.sin(n_w * 0.0), math.cos(n_w * 0.0))
for j in range(1, M_seg + 1):
    th = 2.0 * math.pi * j / M_seg
    cur = math.atan2(math.sin(n_w * th), math.cos(n_w * th))
    d = cur - prev
    # unwrap
    if d > math.pi:
        d -= 2.0 * math.pi
    elif d < -math.pi:
        d += 2.0 * math.pi
    total_dphase += d
    prev = cur
c1_phase = total_dphase / (2.0 * math.pi)
print(f"    (a) phase winding of φ = f(r)e^(i n_w θ) around the vortex:")
print(f"        c1 = (1/2π) ∮ d(arg φ) = {c1_phase:.6f}")

# (b) holonomy of the vortex gauge field A_θ(r) = (n_w/r)·a(r), a(∞)=1.
#     Standard Nielsen-Olesen-type profile a(r) = tanh²(r/r0).
def gauge_profile(r, r0=1.0):
    t = math.tanh(r / r0)
    return t * t

R_loop = 30.0
# (1/2π) ∮ A·dl = (1/2π) · A_θ(R) · 2πR = n_w · a(R)
c1_gauge = n_w * gauge_profile(R_loop)
print(f"    (b) gauge-field holonomy (1/2π)∮A·dl at r = {R_loop:.0f}:")
print(f"        c1 = n_w · a(R) = {c1_gauge:.12f}")
print(f"    Both give c1 = n_w = {n_w}.  THIS is the term v1 omitted.")

assert abs(c1_phase - n_w) < 1e-9
assert abs(c1_gauge - n_w) < 1e-9

# ─── §3  Jackiw–Rossi explicit zero-mode construction ────────────────────────
print("""
§3  JACKIW–ROSSI EXPLICIT CONSTRUCTION (cited: JR 1981; Weinberg 1981;
    framework ref: TOPOLOGICAL_DEFECT_PARTICLE_CLASSIFICATION.md App. A)
──────────────────────────────────────────────────────────────────────────
In the vortex background φ = f(r)e^{i n_w θ}, the zero-mode equation
D_A ψ = 0 separates into angular-momentum channels k ∈ Z.  In channel k
the two coupled radial amplitudes (a_k = upper, b_k = conjugate partner
carrying angular index n_w − 1 − k) obey

    a_k'(r) = (k / r) a_k(r)            −  f(r) b_k(r)
    b_k'(r) = ((n_w − 1 − k) / r) b_k(r) − f(r) a_k(r)

Near r = 0 the regular behaviours are a_k ~ r^k and b_k ~ r^{n_w−1−k};
at large r the normalizable combination decays as exp(−∫₀^r f(r')dr').
Hence the zero modes are

    ψ_k(r,θ) ≃ ( r^k e^{ikθ} ,  r^{n_w−1−k} e^{i(n_w−1−k)θ} )
               × exp(−∫₀^r f(r') dr'),     k = 0, 1, …, n_w − 1

Normalizability of ∫|ψ_k|² d²x = ∫(a_k² + b_k²) r dr requires BOTH origin
exponents ≥ 0 (an exponent of −1 already gives a log-divergent norm):

    k ≥ 0   AND   n_w − 1 − k ≥ 0   ⇔   k ∈ {0, 1, …, n_w − 1}

→ exactly n_w normalizable zero modes.  For n_w = 3 (Postulate F):
""")
for k in range(0, n_w):
    print(f"    ψ_{k}:  a ~ r^{k},  b ~ r^{n_w-1-k},  × exp(−∫f)   "
          f"→ NORMALIZABLE")
print(f"    ψ_3:  a ~ r^3,  b ~ r^(-1), × exp(−∫f)   "
      f"→ b ~ 1/r at origin: ∫|ψ|² r dr ~ ∫ dr/r DIVERGES — excluded")
print(f"    (k < 0 fails symmetrically: a ~ r^k singular)")
print(f"\n    Count: k = 0 … {n_w-1}  →  exactly {n_w} zero modes "
      f"= n_w  [JR theorem]")

# ─── §4  Numerical verification: shooting/integration of the radial ODEs ────
print("""
§4  NUMERICAL VERIFICATION (hand-rolled RK4; profile f(r) = v·tanh(r/r₀))
──────────────────────────────────────────────────────────────────────────
Method: in each channel k the decaying-at-infinity solution is unique up
to scale (a = b = e^{−v(r−R)} asymptotically).  Integrate it INWARD from
R = 30 (numerically stable direction: the unwanted growing-at-∞ branch
decays inward).  Near the origin measure the power-law exponent
ν = d ln|ψ| / d ln r.  The JR prediction is ν = min(k, n_w−1−k):
NORMALIZABLE iff ν ≥ 0; ν ≤ −1 means ∫|ψ_k|² diverges at the origin.
The norm integral N(ε) = ∫_ε^R (a²+b²) r dr is accumulated alongside;
for bad channels N(10⁻⁶)/N(10⁻³) ≫ 1 exhibits the divergence directly.
""")

V_VEV, R0 = 1.0, 1.0   # vortex profile parameters (units of 1/r0)

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
    k2 = deriv(x + h / 2, tuple(yi + h / 2 * ki for yi, ki in zip(y, k1)), n, k)
    k3 = deriv(x + h / 2, tuple(yi + h / 2 * ki for yi, ki in zip(y, k2)), n, k)
    k4 = deriv(x + h, tuple(yi + h * ki for yi, ki in zip(y, k3)), n, k)
    return tuple(yi + h / 6 * (p + 2 * q + 2 * s + u)
                 for yi, p, q, s, u in zip(y, k1, k2, k3, k4))

def solve_channel(n, k, R=30.0, steps_r=5800, decades=6, steps_dec=1200,
                  samples_at=None):
    """Integrate the decaying solution inward; return diagnostics."""
    # Stage 1: r from R down to 1 (linear grid)
    h = (1.0 - R) / steps_r
    y = (1.0, 1.0, 0.0)            # decaying asymptotics a = b at r = R
    samples = {}
    r = R
    for i in range(steps_r):
        if samples_at and any(abs(r - s) < 1e-12 for s in samples_at):
            samples[round(r, 6)] = y[0]
        y = rk4(deriv_r, r, y, h, n, k)
        r = R + (i + 1) * h
    psi_sq_at_1 = y[0] ** 2 + y[1] ** 2
    if samples_at:
        samples[1.0] = y[0]
    # Stage 2: t = ln r from 0 down to −decades·ln10 (log grid)
    ht = -LN10 / steps_dec
    t = 0.0
    psi_at_decade = {0: math.sqrt(psi_sq_at_1)}
    norm_at_decade = {0: y[2]}
    for d in range(1, decades + 1):
        for _ in range(steps_dec):
            y = rk4(deriv_t, t, y, ht, n, k)
            t += ht
        psi_at_decade[d] = math.hypot(y[0], y[1])
        norm_at_decade[d] = y[2]
    # diagnostics (I(r) = −∫_r^R … so norm-from-ε = −I(ε); all ratios safe)
    nu = math.log(psi_at_decade[decades - 1] / psi_at_decade[decades]) / LN10
    norm_1e3 = -norm_at_decade[3]
    norm_eps = -norm_at_decade[decades]
    return {"nu": nu, "norm_1e3": norm_1e3, "norm_eps": norm_eps,
            "ratio": norm_eps / norm_1e3, "psi_sq_1": psi_sq_at_1,
            "samples": samples}

# Sanity check: n_w=1, k=0 has the EXACT closed form a=b ∝ exp(−∫f) = sech(r)
# (v = r0 = 1: ∫₀^r tanh = ln cosh r).  RK4 must reproduce it.
chk = solve_channel(1, 0, samples_at=[25.0, 20.0, 15.0, 10.0, 5.0, 2.0])
ratios = [a * math.cosh(r) for r, a in sorted(chk["samples"].items())]
dev = max(abs(x / ratios[0] - 1.0) for x in ratios)
print(f"    RK4 sanity check vs exact JR mode (n_w=1, k=0: a = b ∝ sech r):")
print(f"      a_num(r)·cosh(r) constant to {dev:.2e} over r ∈ [1, 25]  ✓")
assert dev < 1e-6

def classify(n, k, res):
    expected = min(k, n - 1 - k)
    normalizable = res["nu"] > -0.5
    return expected, normalizable

print(f"""
    Channel table for n_w = {n_w} (Postulate F), f = tanh(r), R = 30:

    k    ν measured   ν predicted   normalizable?   ∫|ψ_k|² finite?
         (d ln|ψ|/d ln r at r→0)    [min(k, n_w−1−k)]
    {'-' * 64}""")

nplus = 0
for k in range(-2, 6):
    res = solve_channel(n_w, k)
    expected, ok = classify(n_w, k, res)
    if ok:
        nplus += 1
        fin = "YES (N(1e-6)/N(1e-3) = %.6f)" % res["ratio"]
    else:
        fin = "NO  (N(1e-6)/N(1e-3) = %.3g — diverges)" % res["ratio"]
    print(f"    {k:<4} {res['nu']:>+9.4f}    {expected:>+4d}          "
          f"{'YES' if ok else 'NO ':<3}             {fin}")
print(f"\n    → exactly {nplus} normalizable zero modes "
      f"(k = 0, 1, 2); k = 3 exceeds the winding bound "
      f"(partner exponent n_w−1−k = −1 → log-divergent norm)")
assert nplus == 3

# ─── §5  Cross-check: the count tracks the winding ───────────────────────────
print("""
§5  CROSS-CHECK: ZERO-MODE COUNT vs WINDING NUMBER
───────────────────────────────────────────────────
(This table replaces v1's broken cross-check, in which no n_w gave +3.)
""")
print(f"    {'n_w':<6} {'normalizable channels':<28} {'count':<7} "
      f"{'JR theorem (= n_w)'}")
print(f"    {'-' * 60}")
counts = {}
for nw in (1, 2, 3):
    good = []
    for k in range(-2, nw + 3):
        res = solve_channel(nw, k)
        _, ok = classify(nw, k, res)
        if ok:
            good.append(k)
    counts[nw] = len(good)
    flag = "  ← Postulate F" if nw == 3 else ""
    print(f"    {nw:<6} k = {str(good):<24} {len(good):<7} {nw}{flag}")
    assert len(good) == nw, f"count mismatch at n_w={nw}"
print(f"\n    Count = n_w for every winding tested: 1→1, 2→2, 3→3  ✓")

# ─── §6  Chirality: why the index is +3 and the generations are left-handed ──
print("""
§6  CHIRALITY — THE INDEX IS +3, NOT 0
───────────────────────────────────────
index(D_A) = n₊ − n₋, the count of POSITIVE-chirality zero modes minus
NEGATIVE-chirality ones.  Weinberg's vanishing theorem (PRD 24, 2669
(1981); also implicit in JR 1981) states that for winding n_w > 0 ALL
zero modes carry the same chirality: n₋ = 0.

Numerical check: the opposite-chirality zero-mode system is the same
radial system with the conjugate order parameter, i.e. winding −n_w.
Its normalizability band k ∈ {0, …, −n_w−1} is EMPTY — scan it:
""")
nminus = 0
for k in range(-5, 3):
    res = solve_channel(-n_w, k)
    _, ok = classify(-n_w, k, res)
    if ok:
        nminus += 1
    print(f"    k = {k:<3}  ν = {res['nu']:>+8.4f}  → "
          f"{'normalizable' if ok else 'NOT normalizable'}")
print(f"\n    n₋ = {nminus}  (vanishing theorem confirmed numerically)")
assert nminus == 0

index_DA = nplus - nminus
print(f"""
    index(D_A) = n₊ − n₋ = {nplus} − {nminus} = {index_DA}
    = c1 = n_w = {n_w}   ✓  (matches §2's Chern term and the JR/Weinberg
                              index theorem, as it must)

    Because all {n_w} zero modes share ONE internal chirality, KK reduction
    delivers them as 4D Weyl fermions of a single 4D chirality — with the
    framework's orientation convention, the LEFT-handed states.  That is
    the three-left-handed-generations statement (cited: JR 1981 / Weinberg
    1981 vanishing theorem; chirality assignment is convention-fixed by
    the zone orientation, not an extra assumption).
""")
assert index_DA == 3
assert index_DA == round(c1_phase)

# ─── §7  The status of n_w = 3 (replaces v1's deleted §6 numerology) ─────────
print("""
§7  THE STATUS OF n_w = 3 — HONEST STATEMENT
─────────────────────────────────────────────
v1's §6 offered three "evidences" for n_w = 3 (tri-fold symmetry from
ξ_A = 3×10²⁶ m; "three fibers → H = 3"; "the only value giving index 3").
All three were numerology or circular and have been DELETED in v2.

The honest statement:

    n_w = 3 is Postulate F — an ADOPTED zone-architecture axiom
    (Author Ratification #1, 2026-06-11; AXIOM_GODHEAD_ZONE_Z0.md §4).
    It is NOT derived from deeper principles.  Board issue #849 tracks
    deriving it from Z0/Λ_Z0; a Z₃-quantization mechanism is under
    investigation.  Until then it is one of the framework's two
    irreducible inputs (with Λ_Z0).

What THIS script establishes is the conditional:  index(D_A) = n_w
(computed in §2–§6).  GIVEN Postulate F, the generation count is 3.
Without Postulate F, the count is undetermined.
""")

# ─── §8  Summary: OP-02 closure (v2) ─────────────────────────────────────────
print("=" * 68)
print("SUMMARY — OP-02 CLOSURE (v2, GitHub #851 fixed)")
print("=" * 68)
print(f"""
Spin-1/2 (existence + statistics):
  Kähler route, op02_kahler_spinor_derivation.md Theorems 1–3:
  M_perp is Kähler → Dolbeault spinor bundle → 4D spin-1/2 KK zero modes
  with fermionic statistics.  → SPIN-1/2 DERIVED. ✓

Three generations (count):
  Twisted-index / Jackiw–Rossi route (THIS script):
    bulk Chern term      c1 = (1/2π)∮A·dl       = {c1_phase:.4f}   (§2, computed)
    explicit zero modes  ψ_k, k = 0…n_w−1        (§3, constructed)
    numerical shooting   n₊ = {nplus}, n₋ = {nminus}             (§4–§6, computed)
    index(D_A) = n₊ − n₋ = c1 = n_w             [JR 1981; Weinberg 1981]
  GIVEN Postulate F (n_w = 3, adopted axiom):
    index(D_A) = {index_DA}  →  exactly THREE same-chirality zero modes
  → THREE LEFT-HANDED GENERATIONS, COMPUTED GIVEN n_w = 3. ✓

Division of labor:
  - Kähler route (Theorems 1–3): spin-1/2 EXISTENCE + spin-statistics
  - JR/Callias twisted index (here): the COUNT = n_w

Status: OP-02 RESOLVED given Postulate F (dependency stated)
  - v1's untwisted index (−1/2) was meaningless for the twisted problem;
    the omitted Chern term carried the 3 (GitHub #851).
  - Remaining caveat (unchanged, NOT weakened): n_w = 3 is an adopted
    axiom, not derived.  Board #849 tracks deriving it.
""")
print(f"    FINAL (computed): index(D_A) = {index_DA}  →  THREE GENERATIONS"
      f"  [given Postulate F]")
print()
print("    File: op02_aps_index_computation.py | v2 2026-06-11 | "
      "GitHub #851 fixed | OP-02 RESOLVED given Postulate F")
