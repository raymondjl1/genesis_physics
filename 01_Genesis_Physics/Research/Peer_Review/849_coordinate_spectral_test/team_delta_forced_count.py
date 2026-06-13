"""
TEAM DELTA — most charitable test of a GEOMETRY-FORCED finite chiral count.
===========================================================================
Before concluding, give the lead (warped-geometry) method its best shot:
is there ANY parameter-free statement in which the EXISTING throat data
(k1, L_A=83.2 eta_B, warp depth k1*L_A = 2/3) yields exactly 3 normalizable
SAME-CHIRALITY modes, with no tuned cutoff?

Candidate mechanisms tested:
 (C1) Bulk Dirac mass m_bulk = c*k (RS): number of LIGHT chiral modes localized
      before they delocalize. Count vs c. Is c forced? Is the count 3?
 (C2) 'Throat supports N bound states of a Poschl-Teller-like volcano potential'
      -- the RS graviton/fermion volcano. Count its true bound states.
 (C3) Warp depth as e-folds: N = floor(k1 L_A / something). k1 L_A = 2/3.
All honest; we report whether 3 is forced or injected.
numpy only.
"""
import numpy as np

eta_B=1.3e-15; L_A=83.2*eta_B; k1=2.0/(3.0*L_A)
kL=k1*L_A
print("="*70)
print("Most charitable test: can warp geometry FORCE a chiral count = 3?")
print("="*70)
print(f"  warp depth kL = k1*L_A = {kL:.4f}  (forced by Lambda_Z0 -> = 2/3)")

# (C3) e-fold counting
print("\n(C3) e-fold / warp-depth counting:")
print(f"     kL = {kL:.4f};  floor(kL)= {int(np.floor(kL))};  "
      f"floor(2pi kL)={int(np.floor(2*np.pi*kL))};  e^kL={np.exp(kL):.3f}")
print("     No natural integer function of kL=2/3 equals 3 without an injected")
print("     factor. A SHORT throat (kL<1) supports NO large tower at all.")

# (C2) RS 'volcano' potential bound states for the transverse mode.
# Transform mode eqn to Schrodinger form: psi'' + (E - V(z)) psi =0 with the RS
# volcano V(z). On a FINITE throat z in [z_UV,z_IR] the # of true bound states
# (E<0 normalizable) is what a 'finite count' would need. Solve via FD.
print("\n(C2) Bound states of the RS volcano on the finite throat:")
def volcano_bound_states(zUV, zIR, Nz=4000, ell=2.0):
    # V(z) = ell(ell+1)/(4 (z)^2)/... use standard RS volcano for spin field:
    # For graviton: V = (15/4)/z^2 - 3 delta(z-zUV)/... we drop deltas and just
    # count negative-energy normalizable states of V= a/z^2 on [zUV,zIR] w/
    # Dirichlet ends (a hard-wall throat). a=15/4 (graviton) or 3/4 (fermion-ish)
    z=np.linspace(zUV,zIR,Nz); h=z[1]-z[0]
    a=ell*(ell+1)
    V=a/z**2
    H=np.zeros((Nz,Nz))
    for i in range(Nz):
        H[i,i]=2/h**2+V[i]
        if i>0:H[i,i-1]=-1/h**2
        if i<Nz-1:H[i,i+1]=-1/h**2
    E=np.linalg.eigvalsh(H)
    return E
zUV=1.0/k1; zIR=np.exp(kL)/k1
E=volcano_bound_states(zUV,zIR)
nbound=int(np.sum(E<0))
print(f"     z in [{zUV:.3e},{zIR:.3e}]; volcano V=a/z^2 is POSITIVE-definite")
print(f"     -> number of E<0 (true bound) states = {nbound}")
print("     The pure-AdS volcano (1/z^2) has NO negative-energy bound states;")
print("     all modes are a positive continuum truncated by the throat ends.")
print("     => no finite '3 bound states' is forced; count is set by the IR")
print("        cutoff spacing (a tuned scale). O-tune again.")

# (C1) Bulk Dirac mass localization band: number of c-values giving a localized
# LH zero mode is 1 (the zero mode), not 3. RS gives exactly ONE chiral zero
# mode per bulk fermion (that's the whole point of RS chirality). To get 3 you
# must put in 3 bulk fermions BY HAND, or use n_w=3 winding. Neither is 'forced
# by the warp'.
print("\n(C1) RS bulk Dirac fermion chiral zero modes:")
print("     RS projects to EXACTLY ONE chiral (LH) zero mode per bulk fermion")
print("     field. 3 generations would need 3 bulk fields by hand, OR the")
print("     n_w=3 vortex twist (op02). The warp does the CHIRALITY PROJECTION")
print("     (good: solves O-chi) but NOT the multiplicity. Multiplicity = n_w.")

print("\n" + "="*70)
print("CONCLUSION: No parameter-free function of the EXISTING throat data")
print("(k1, L_A=83.2 eta_B, kL=2/3) forces the integer 3. The warp geometry")
print("FORCES CHIRALITY (one LH zero mode, mirror projected) and SCALE, but")
print("the COUNT 3 must come from the winding n_w=3 (adopted axiom), not the")
print("throat. Honest verdict on the lead method's central claim: NOT FORCED.")
print("="*70)
