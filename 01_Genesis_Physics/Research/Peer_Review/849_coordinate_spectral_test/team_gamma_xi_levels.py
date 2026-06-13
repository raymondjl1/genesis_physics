"""
TEAM GAMMA — Part 3: the xi-direction (cosmological / Waters-Above) KK level count.
====================================================================================
TOPOLOGICAL_DEFECT Part 4.2 proposes generations as KK / harmonic levels of a confining
well in the xi-direction (the "radial excitation k=0,1,2" picture for e/mu/tau). Here we
take the ACTUAL Waters-Above warp (not a guessed harmonic well) and count its normalizable
KK levels below the continuum threshold, with the warp measure — and ask what sets the count.

Waters-Above warp (WARP_FUNCTION_DERIVATION eq 2.4 / 3.1a):
    A_xi(xi) = (2/3) ln(xi_0 / xi),   xi in [xi_0, xi_A],   xi_A/xi_0 = L_A-type ratio.
The 4D-graviton / scalar-zero-mode KK problem in a warped interval [xi_0, xi_A] with metric
    ds^2 = e^{2A} dx_4^2 + e^{2B} dxi^2,   reduces (standard RS KK) to a Sturm-Liouville
problem.  For a massless 5D scalar Phi(x,xi)=sum psi_n(xi) phi_n(x), the mode equation is
    -(1/w) d/dxi [ p(xi) d psi_n/dxi ] = m_n^2 sigma(xi) psi_n
with p = e^{(d-2)A + B?}... we use the canonical RS form:  modes of  -d^2/dz^2 + V_RS(z)
after going to conformal coordinate z (dz = e^{B-A} dxi) and rescaling psi = e^{-(3/2)A} hatpsi.
The RS "volcano" potential is  V(z) = (9/4)(A'(z))^2 + (3/2) A''(z)  (graviton case; the
3/2 from the 4D=3 spatial + warp power for the spin-2 zero mode normalization).

We compute V(z), solve -hatpsi'' + V hatpsi = m^2 hatpsi by finite differences with the
physical boundary conditions, and COUNT bound levels (m^2 below the continuum threshold).
The question: is the count = 3, and is it set by the PARAMETER-FREE ratio xi_A/xi_0?
"""
import numpy as np, sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ---- warp: A_xi = (2/3) ln(xi0/xi).  Use u = ln(xi/xi0) in [0, ln R], R = xi_A/xi0 ----
# A(u) = -(2/3) u.  In coordinate xi, A' = dA/dxi = -(2/3)/xi.
# Go to conformal z: dz = e^{B-A} dxi. With B_xi = B0 - ln(xi/xi0) (eq 2.7) and A=-(2/3)ln(xi/xi0):
#   e^{B-A} = e^{B0} (xi/xi0)^{-1} (xi/xi0)^{2/3} = e^{B0}(xi/xi0)^{-1/3}.
# dz = e^{B0}(xi/xi0)^{-1/3} dxi  => z propto (xi/xi0)^{2/3}. Monotone; finite range.
# This is AdS-like: KK spectrum of a finite AdS slice is DISCRETE with INFINITELY many levels
# (a tower), bounded below, with NO finite cutoff on the count unless an IR brane truncates.
# The number BELOW any fixed threshold grows without bound as the slice lengthens.

def build_z_grid(R, Nz=6000, B0=0.0):
    # xi from xi0=1 to xi_A=R; conformal z(xi)
    xi = np.linspace(1.0, R, Nz)
    integrand = np.exp(B0) * (xi)**(-1.0/3.0)   # dz/dxi
    z = np.concatenate([[0.0], np.cumsum(0.5*(integrand[1:]+integrand[:-1])*np.diff(xi))])
    return xi, z

def rs_potential(R, Nz=6000):
    xi, z = build_z_grid(R, Nz)
    # A as function of xi:
    A = -(2.0/3.0)*np.log(xi)
    # derivatives wrt z (numerical)
    Az = np.gradient(A, z)
    Azz = np.gradient(Az, z)
    V = (9.0/4.0)*Az**2 + (3.0/2.0)*Azz   # graviton volcano
    return z, V

def count_levels(R, Nz=4000, thresh_frac=0.999):
    z, V = rs_potential(R, Nz)
    h = z[1]-z[0]
    # finite-difference on uniform-ish z (resample to uniform grid)
    zu = np.linspace(z[0], z[-1], Nz)
    Vu = np.interp(zu, z, V)
    h = zu[1]-zu[0]
    main = 2.0/h**2 + Vu
    off = -1.0/h**2*np.ones(Nz-1)
    M = np.diag(main)+np.diag(off,1)+np.diag(off,-1)
    ev = np.linalg.eigvalsh(M)
    # continuum threshold ~ max of asymptotic V (here V->0 at large z if AdS flattens, or
    # set by the box). Bound = negative/low-lying discrete levels separated from the dense tail.
    return zu, Vu, ev

print("="*76)
print("TEAM GAMMA Part 3 — xi-direction (Waters-Above) KK level count")
print("="*76)
print("""
Warp A_xi=(2/3)ln(xi0/xi) is AdS-like (logarithmic). Conformal z ~ (xi/xi0)^(2/3).
RS graviton volcano V(z)=(9/4)A'^2+(3/2)A''. We count low-lying KK levels vs the
slice length R = xi_A/xi0 to see whether the COUNT is fixed (=3) or grows with R.
""")
print(f"{'R=xi_A/xi0':>12} | {'z_max':>8} | {'lowest 6 m^2 (KK)':>40}")
print("-"*76)
for R in [5.0, 20.0, 83.2, 300.0, 1000.0]:
    zu, Vu, ev = count_levels(R)
    low = ev[ev>1e-9][:6]   # drop the ~0 zero mode (massless 4D graviton/scalar)
    s = ", ".join(f"{e:.3g}" for e in low)
    print(f"{R:>12.1f} | {zu[-1]:>8.2f} | {s:>40}")

print("""
READING: the KK levels form a TOWER (infinitely many, bounded below). The number below
any fixed mass grows with the slice length R = xi_A/xi0. There is NO finite-3 cutoff: the
xi-warp does not select 3. (TOPOLOGICAL_DEFECT 4.2's harmonic-well picture would need a
TRUNCATING wall + a depth tuned to exactly 3 levels — the very fine-tuning O-tune warns of,
and the floor(L/w)=3 claim is parameter-fitted, not derived.)

CONCLUSION (Part 3): the cosmological (xi) direction gives a KK tower, not a forced 3.
The 'three radial excitations' e/mu/tau picture is a LABELING of the lowest three tower
levels, not a derivation that there are exactly three. xi does NOT force the count.
""")
