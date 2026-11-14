"""
#848 CKM angles - DIMENSIONAL/SCALING strategy - FINAL honest summary.

Claim under test:
  sin(theta_ij) ~ exp( -alpha_w * |n_j^2 - n_i^2| )
  with alpha_w = 2/3  = the CANONICAL warp index A_xi=(2/3)ln(xi0/xi)
                        (ledger sec3, DERIVED, RATIFIED #3 -- NOT fitted)
  and n=1,2,3 the generation labels (V3 sec3.5 n_xi mode mapping).

Inputs that ARE allowed (axioms/derived): warp index 2/3; generation
labeling n^2 (from the V3 overlap-integral mode structure).
Inputs explicitly NOT used: measured CKM angles, measured quark masses,
fitted alpha_u/alpha_d (the data-importing GST path of op05).
"""
import math
exp = math.exp

aw = 2/3
steps = {"12":3, "23":5, "13":8}      # Delta(n^2) = (2^2-1^2),(3^2-2^2),(3^2-1^2)
deg   = {"12":13.04, "23":2.38, "13":0.201}
meas  = {k: math.sin(math.radians(v)) for k,v in deg.items()}

print("="*64)
print("PURE SCALE-RATIO PREDICTION  sin th_ij = exp(-(2/3)*Delta(n^2))")
print("="*64)
print(f"{'angle':6}{'Delta(n^2)':>11}{'predicted':>12}{'pred deg':>10}{'meas deg':>10}{'err':>8}")
for k in ["12","23","13"]:
    pred = exp(-aw*steps[k])
    pdeg = math.degrees(math.asin(pred))
    print(f"{'th'+k:6}{steps[k]:>11}{pred:>12.6f}{pdeg:>10.3f}{deg[k]:>10.3f}"
          f"{(pred-meas[k])/meas[k]*100:>+7.0f}%")

print("""
HONEST STATUS
-------------
DERIVED (zero free parameters), the GENUINE NEW CONTENT for #848:
  theta_23 = 2.04 deg  vs  2.38 deg measured   (-14%)   [was OPEN]
  theta_13 = 0.28 deg  vs  0.20 deg measured   (+38%)   [was OPEN]
  Both previously-OPEN angles now have a parameter-free scale prediction,
  correct to within ~15-40%, from one number: the warp index 2/3.

The same law gives theta_12 = 7.8 deg (-40%); the framework's better
Cabibbo (~13 deg, op05) used the GST relation sqrt(m_d/m_s) which IMPORTS
measured quark masses -- not a pure scale ratio, so it is NOT claimed here.

WHAT IS ASSUMED (declared, not hidden):
  - alpha_w = 2/3 is the warp index (DERIVED/RATIFIED in the framework),
    reused here as the universal mixing slope. Identifying the MIXING slope
    with the WARP index is a physical *hypothesis*, not yet a proof.
  - n^2 generation labeling (from V3 overlap-mode mapping).
  - single-slope, single-sector law: ignores the up/down cancellation and
    the O(1) Wolfenstein A and |rho-i eta| factors -> these are the residual.

NOT DERIVED: the O(1) coefficients (A~0.82, |rho-ieta|~0.38) that would turn
~15-40% into <few%. delta_CP value remains pi/3 (fitted, unchanged).
""")
