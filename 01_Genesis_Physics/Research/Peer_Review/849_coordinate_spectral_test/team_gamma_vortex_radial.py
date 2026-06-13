"""
TEAM GAMMA — Spectral generation count, Part 2: the RADIAL vortex problem with the warp measure.
=================================================================================================
The op02 zero modes are  psi_k(r,theta) ~ ( r^k e^{ikθ}, r^{n-1-k} e^{i(n-1-k)θ} ) exp(-∫f),
k = 0..n-1, peaks (n=3, f=tanh) at r ≈ 0, 1.20, 2.07.  op02 counts them by NORMALIZABILITY:
the partner exponent n-1-k must be >= 0, i.e. k <= n-1.  That count = n_w (winding).

TEAM GAMMA RE-FRAME (spectral, not winding):
  Ask instead — independent of any assumed winding — how many radial bound levels does the
  ACTUAL eigenvalue problem admit, where the inner-product weight is the WARP MEASURE
  e^{4A+2B} (WARP_FUNCTION_DERIVATION) over the bounded fiber range r in [0, R_max]?
  If the COUNT is set by the geometry (R_max from L_A) rather than by n_w, we have a spectral
  (coordinate) origin of 3.  If it just reproduces n_w, the spectral picture is EQUIVALENT to
  the winding picture (complements, does not supersede).

We test BOTH normalizability criteria explicitly:
  (A) op02 criterion: origin regularity (exponent >= 0) AND large-r decay exp(-∫f).
      -> count = n_w  (winding-controlled).  [reproduce it]
  (B) warp-measure criterion: same modes, but normalizable under the FULL measure
      mu(r) = e^{4A+2B} r dr on the FINITE fiber [0,R_max], R_max set by L_A/eta_B = 83.2.
      Does the finite range CHANGE the count? (It cannot add modes; can it remove/keep 3?)

Hand-rolled numerics (numpy only).
"""
import numpy as np
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
trapz = getattr(np, "trapezoid", getattr(np, "trapz", None))

# ---- corpus parameters (cited in .md) ----
ETA_B = 1.0                 # work in eta_B units
L_A   = 83.2                # = 3/(2 k1) in eta_B units (AXIOM_GODHEAD_ZONE_Z0 table)
KAPPA_B = 1.0/ETA_B         # A_eta = -kappa_B*(eta-eta0); kappa_B = 1/eta_B (WARP doc 2.2)
# Warp on the Firmament fiber slice (the 2D extra space (xi,eta) cross-section the vortex lives in):
# A_eta = -kappa_B*r  (RS-linear, eq 2.9);  B ~ const in Waters Below (eq 2.16) => take B=0 on slice.
# measure weight for a scalar/fermion zero-mode norm:  e^{ (4A+2B) } r dr  (sqrt(-g) reduced)
def warp_weight(r):
    A = -KAPPA_B * r          # Waters-Below RS warp (linear)
    B = 0.0
    return np.exp(4*A + 2*B)  # e^{4A+2B}

def vortex_mode_profile(r, k, n, v=1.0, r0=1.0):
    """JR zero mode amplitudes (op02 §3): a~r^k, b~r^(n-1-k), times exp(-∫0^r f), f=v tanh(r/r0).
       ∫0^r v tanh(r'/r0) dr' = v r0 ln cosh(r/r0)."""
    decay = np.exp(-v*r0*np.log(np.cosh(r/r0)))   # = cosh(r/r0)^(-v r0)
    a = r**k * decay
    b = r**(n-1-k) * decay
    return a, b

def norm_op02(k, n, Rmax=60.0, N=200000):
    """op02 norm: ∫ (a^2+b^2) r dr  with FLAT measure (just r dr). Finite => normalizable."""
    r = np.linspace(1e-6, Rmax, N)
    a, b = vortex_mode_profile(r, k, n)
    integrand = (a**2 + b**2) * r
    return trapz(integrand, r)

def norm_warp(k, n, Rmax, N=200000):
    """Warp-measure norm: ∫ (a^2+b^2) * e^{4A+2B} * r dr over [0,Rmax]."""
    r = np.linspace(1e-6, Rmax, N)
    a, b = vortex_mode_profile(r, k, n)
    w = warp_weight(r)
    integrand = (a**2 + b**2) * w * r
    return trapz(integrand, r)

print("="*78)
print("TEAM GAMMA Part 2 — radial vortex modes: warp-measure vs op02 normalizability")
print("="*78)

n = 3   # we ASSUME n_w=3 here only to compare criteria on the SAME modes; the QUESTION is
        # whether the warp measure (geometry) — not n — is what bounds the count.
print(f"\nUsing n (winding) = {n} to enumerate candidate modes psi_k, k integer.")
print(f"Warp: A_eta=-kappa_B*r, kappa_B=1/eta_B; finite fiber R_max from L_A={L_A} eta_B.\n")

print("(A) op02 flat-measure criterion  ∫(a^2+b^2) r dr  (origin reg + exp decay):")
print(f"   {'k':>4} | {'origin exps (k, n-1-k)':>22} | {'norm (flat, Rmax=60)':>20} | normalizable?")
print("   "+"-"*72)
for k in range(-1, 5):
    try:
        val = norm_op02(k, n)
    except Exception as e:
        val = np.inf
    exps = (k, n-1-k)
    ok = np.isfinite(val) and (min(exps) >= 0) and val < 1e6
    print(f"   {k:>4} | {str(exps):>22} | {val:>20.4g} | {'YES' if ok else 'no'}")

print("\n(B) warp-measure criterion over FINITE fiber [0, R_max], R_max = L_A = 83.2 eta_B:")
Rmax = L_A
print(f"   {'k':>4} | {'origin exps':>14} | {'norm (warp meas)':>18} | normalizable?")
print("   "+"-"*64)
for k in range(-1, 6):
    try:
        val = norm_warp(k, n, Rmax)
    except Exception:
        val = np.inf
    exps = (k, n-1-k)
    # warp e^{4A} = e^{-4 kappa_B r} kills large-r growth for ANY power => only ORIGIN matters now
    ok = np.isfinite(val) and (min(exps) >= 0)
    print(f"   {k:>4} | {str(exps):>14} | {val:>18.4g} | {'YES' if ok else 'no'}")

print("""
CRITICAL OBSERVATION:
  The warp factor e^{4A} = e^{-4 kappa_B r} decays exponentially at large r. So large-r
  normalizability is GUARANTEED for ANY power-law mode under the warp measure — the
  exp(-∫f) vortex decay is not even needed there. Therefore the warp measure REMOVES the
  large-r constraint entirely; the ONLY surviving constraint is ORIGIN regularity:
      k >= 0  AND  n-1-k >= 0.
  That is EXACTLY the op02 / Jackiw-Rossi winding constraint k in {0,..,n-1}.

  => Under the warp measure the count is STILL  n_w  (= number of integer k in [0,n-1]).
     The geometry (R_max, warp) does NOT independently set the count to 3; the WINDING n
     does. The warp only changes WHERE the modes sit (peak radii), not HOW MANY.

CONCLUSION (Part 2): the radial spectral count is winding-controlled, NOT geometry-controlled.
The spectral/coordinate picture is EQUIVALENT to (complements) the op02 winding picture;
it does NOT supersede it. The integer 3 still enters through n_w (the adopted Postulate F),
NOT as a forced property of the warp geometry.
""")
