# Appendix C — Feynman Rules for Zone Architecture

*Foundations Vol 4, The Quantum World — Back Matter*

> "A Feynman diagram is a picture of a term in a perturbation series, with the understanding that anyone who looks at it must be able to write down the integral. If you need a textbook open to do so, the diagram is useless." — *Feynman, paraphrased from lectures*

Chapter 7 derives the Feynman-diagram expansion from the zone-architecture Lagrangian. Chapters 10 through 14 use those rules dozens of times — for vertex corrections, tree-level cross sections, mass calculations, mixing matrices, and beyond-SM estimates. Rather than re-derive each rule in the chapter that uses it, we compile them once, here.

Every rule in this appendix is **derived** in Vol 4 Chapter 6 (second quantization), Chapter 7 (perturbation theory), or Chapter 8 (renormalization). The cross-references back to those chapters are stated for every entry so the reader can trace the rule to its origin.

This appendix is a *reference*, not a derivation. For the derivations, read Chapter 7 §§7.3–7.7.

---

## C.1 Preliminaries: Conventions

### Metric signature

Throughout Vol 4 we use the **mostly-plus** metric signature $(-,+,+,+)$, consistent with Vol 1 Appendix B. The Minkowski metric is $\eta_{\mu\nu} = \text{diag}(-1,+1,+1,+1)$. A four-vector squared is $k^2 = k^\mu k_\mu = -k_0^2 + \vec k^2$.

### Natural units

$\hbar = c = 1$. Masses, momenta, and energies are all in GeV or MeV as appropriate. Cross sections in GeV$^{-2}$, decay rates in GeV, lengths in GeV$^{-1}$.

### Momentum flow

- **Fermion arrows** indicate the flow of fermion number (particle direction), not momentum.
- **Momenta** are drawn flowing in an arbitrary but consistent direction; at each vertex the sum of incoming four-momenta equals the sum of outgoing four-momenta.
- **$+i\epsilon$ prescription** is included in every propagator denominator; we drop it explicitly in the tables for brevity but it is always there.

### Color, flavor, spinor indices

- Greek letters $\mu,\nu,\rho,\sigma,\ldots$ are spacetime indices, range $0,1,2,3$.
- Latin letters from the middle $i,j,k,\ldots$ are color or flavor indices as context demands.
- Latin letters from the start $a,b,c,\ldots$ index gauge-group generators: $a=1..8$ for $SU(3)$ (gluons), $a=1..3$ for $SU(2)$ (weak), no index needed for $U(1)$.
- Spinor indices are suppressed.

### The zone-architecture bookkeeping note

All Feynman rules below are identical in form to those of the standard-model Lagrangian, because Vol 4 Chapter 6 shows that the canonical quantization of the zone-Lagrangian (Vol 2 Ch 5) reproduces the standard-model Lagrangian term by term, with the gauge group $SU(3)_c\times SU(2)_L\times U(1)_Y$ (Vol 2 Ch 6). What differs from conventional QFT texts is not the rule itself but the *origin* of each coupling: each appears below with its derivation-chapter reference.

Spin-1/2 fields are treated as effective Dirac fermions for the purpose of writing these rules. The outstanding spin-1/2 derivation from the bosonic Firmament (GitHub #1) is a question about where these fields come from, not about what their Feynman rules are once they are in place.

---

## C.2 Propagators

Every internal line in a diagram contributes one propagator. Momenta flow along the line; for each line one writes $i\tilde D(k)$ or $i\tilde S(k)$ as listed.

### Scalar field of mass $m$

$$\boxed{\; \tilde D_F(k) \;=\; \frac{i}{k^2 - m^2 + i\epsilon} \;}$$

**Derived in:** Ch 6 §6.4 from canonical quantization of the Klein–Gordon field. The Klein–Gordon equation in turn is the 4D projection of the Firmament wave equation (1.5.1).

### Dirac fermion of mass $m$

$$\boxed{\; \tilde S_F(k) \;=\; \frac{i(\gamma^\mu k_\mu + m)}{k^2 - m^2 + i\epsilon} \;}$$

**Derived in:** Ch 6 §6.6. The numerator is $(\not k + m)$; the denominator is the Dirac operator squared.

### Photon (Feynman gauge, $\xi_\text{gauge} = 1$)

$$\boxed{\; \tilde D^{\mu\nu}_F(k) \;=\; \frac{-i\,\eta^{\mu\nu}}{k^2 + i\epsilon} \;}$$

**Derived in:** Ch 6 §6.7 and Ch 7 §7.3. In a general covariant gauge $(\xi_\text{gauge})$ it becomes

$$\tilde D^{\mu\nu}_F(k) \;=\; \frac{-i}{k^2 + i\epsilon}\left[\eta^{\mu\nu} - (1-\xi_\text{gauge})\frac{k^\mu k^\nu}{k^2}\right].$$

Feynman gauge $\xi_\text{gauge}=1$ simplifies one-loop calculations; Landau gauge $\xi_\text{gauge}=0$ simplifies IR arguments. Physical results are gauge-independent.

### Massive vector ($W^\pm, Z^0$) in unitary gauge

$$\boxed{\; \tilde D^{\mu\nu}_V(k) \;=\; \frac{-i}{k^2 - M_V^2 + i\epsilon}\left[\eta^{\mu\nu} - \frac{k^\mu k^\nu}{M_V^2}\right] \;}$$

**Derived in:** Ch 11 §11.4 (electroweak symmetry breaking). Here $M_V \in \{M_W, M_Z\}$. In $R_\xi$ gauge the $k^\mu k^\nu/M_V^2$ term is replaced by $k^\mu k^\nu(1-\xi_\text{gauge})/(k^2-\xi_\text{gauge}M_V^2)$ and there are additional Goldstone-boson propagators.

### Gluon

$$\boxed{\; \tilde D^{\mu\nu,\,ab}_F(k) \;=\; \frac{-i\,\eta^{\mu\nu}\,\delta^{ab}}{k^2 + i\epsilon} \;}$$

**Derived in:** Ch 12 §12.3. Color indices $a,b \in \{1,\ldots,8\}$. The gluon is massless, so the propagator is the same as the photon with a color Kronecker delta.

### Ghost fields (Faddeev–Popov)

$$\tilde D^{ab}_\text{ghost}(k) \;=\; \frac{i\,\delta^{ab}}{k^2 + i\epsilon}$$

**Needed in:** loops involving non-abelian gauge bosons, in covariant gauges. Discussed in Ch 8 §8.5. Ghosts never appear on external legs.

---

## C.3 QED Vertices

### Electron–photon vertex

$$\boxed{\; V_{e\gamma} \;=\; -ie\,\gamma^\mu \;}$$

**Derived in:** Ch 7 §7.5 from the QED interaction Lagrangian $\mathcal L_\text{int}=-e\bar\psi\gamma^\mu\psi A_\mu$. Here $e$ is the electron charge (positive in this convention); for a generic lepton the rule is $-iQ_\ell e\,\gamma^\mu$ with $Q_\ell$ the lepton charge in units of $e$.

### Scalar–photon vertex (for charged scalars)

$$V_{\phi\phi\gamma} \;=\; -ie(p + p')^\mu$$

where $p$ and $p'$ are the incoming and outgoing scalar momenta. **Derived in:** Ch 7 §7.6. Appears in Higgs-boson tree-level couplings and in scalar QED examples used in the problem sets.

### Seagull vertex (scalar QED)

$$V_{\phi\phi\gamma\gamma} \;=\; 2ie^2\,\eta^{\mu\nu}$$

**Derived in:** Ch 7 §7.6. Appears in charged-scalar Compton scattering; less important physically than the preceding vertex but required for gauge invariance of one-loop diagrams.

---

## C.4 QCD Vertices

### Quark–gluon vertex

$$\boxed{\; V_{qqg} \;=\; -ig_s\,t^a\,\gamma^\mu \;}$$

**Derived in:** Ch 12 §12.4. Here $g_s$ is the strong coupling ($\alpha_s = g_s^2/4\pi$), $t^a$ are the color-$SU(3)$ generators in the fundamental representation (Gell-Mann matrices divided by 2), and $a=1..8$ labels the gluon color. The flavor index is diagonal — QCD is flavor-blind.

### Three-gluon vertex

$$\boxed{\; V_{3g}^{abc,\mu\nu\rho}(k_1,k_2,k_3) \;=\; g_s\,f^{abc}\left[(k_1-k_2)^\rho\eta^{\mu\nu} + (k_2-k_3)^\mu\eta^{\nu\rho} + (k_3-k_1)^\nu\eta^{\rho\mu}\right] \;}$$

**Derived in:** Ch 12 §12.5 from the non-abelian term of the gluon field strength $G^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+g_sf^{abc}A^b_\mu A^c_\nu$. All three gluon momenta $k_1,k_2,k_3$ are taken incoming; momentum conservation sets $k_1+k_2+k_3=0$. Here $f^{abc}$ are the structure constants of $SU(3)$.

### Four-gluon vertex

$$V_{4g}^{abcd,\mu\nu\rho\sigma} \;=\; -ig_s^2\Bigl[f^{abe}f^{cde}(\eta^{\mu\rho}\eta^{\nu\sigma}-\eta^{\mu\sigma}\eta^{\nu\rho}) \;+\; f^{ace}f^{bde}(\eta^{\mu\nu}\eta^{\rho\sigma}-\eta^{\mu\sigma}\eta^{\nu\rho}) \;+\; f^{ade}f^{bce}(\eta^{\mu\nu}\eta^{\rho\sigma}-\eta^{\mu\rho}\eta^{\nu\sigma})\Bigr]$$

**Derived in:** Ch 12 §12.5 from the $f^{abc}f^{ade}$ contraction of the non-abelian field strength squared. A nuisance but essential for gauge invariance of gluon scattering at tree level.

### Ghost–gluon vertex (in covariant gauge)

$$V_{\bar cc g}^{abc,\mu} \;=\; -g_s f^{abc} k^\mu$$

**Derived in:** Ch 8 §8.5. Here $k^\mu$ is the outgoing ghost momentum. Needed only in loop diagrams with gluon self-energy or three-gluon vertex corrections.

---

## C.5 Electroweak Vertices

The Standard Model electroweak sector is built on $SU(2)_L\times U(1)_Y$; the gauge group breaks to $U(1)_\text{EM}$ via the Higgs mechanism (Ch 11). The mass eigenstates $W^\pm, Z^0, \gamma$ couple to fermions through the vertices listed here. Note that *left-handed* couplings dominate the $W$ vertex — chirality is a first-class citizen.

### Charged-current vertex ($W^\pm$–fermion)

$$\boxed{\; V_{W\bar fl f'l}^{\mu} \;=\; \frac{-ig_w}{\sqrt 2}\,\gamma^\mu P_L\,U_{ff'} \;}$$

**Derived in:** Ch 11 §11.5. Here:
- $g_w = e/\sin\theta_W$ is the weak coupling.
- $P_L = (1-\gamma^5)/2$ is the left-handed projector.
- $U_{ff'}$ is the CKM matrix element for quark transitions $u_i\leftrightarrow d_j$ or the PMNS matrix element for lepton-neutrino transitions.
- $f,f'$ label the flavor eigenstates connected by the $W$.

### Neutral-current vertex ($Z^0$–fermion)

$$\boxed{\; V_{Z\bar ff}^{\mu} \;=\; \frac{-ig_w}{2\cos\theta_W}\,\gamma^\mu\,(g_V^f - g_A^f\gamma^5) \;}$$

**Derived in:** Ch 11 §11.6, where the vector and axial couplings are
$$g_V^f = T_3^f - 2Q_f\sin^2\theta_W, \qquad g_A^f = T_3^f.$$

Here $T_3^f = \pm 1/2$ is the weak isospin and $Q_f$ is the electric charge in units of $e$. Values for each SM fermion are tabulated in Ch 11 Table 11.2.

### Photon–fermion vertex (electroweak-derived)

$$V_{\gamma\bar ff}^{\mu} \;=\; -iQ_f e\,\gamma^\mu$$

Same rule as in QED (§C.3); reproduced here because it is the $U(1)_\text{EM}$ projection of the $B_\mu$–$W^3_\mu$ mixture after electroweak symmetry breaking.

### Higgs–fermion Yukawa vertex

$$\boxed{\; V_{h\bar ff} \;=\; -i\,\frac{m_f}{v} \;}$$

**Derived in:** Ch 11 §11.7. Here $m_f$ is the fermion mass and $v=246.22$ GeV is the Higgs VEV. The coupling is proportional to the fermion mass — this is why the top quark is the dominant Higgs decay channel for massive fermions.

### Higgs–gauge-boson vertices

$$V_{hWW}^{\mu\nu} \;=\; i\,\frac{2M_W^2}{v}\,\eta^{\mu\nu}, \qquad V_{hZZ}^{\mu\nu} \;=\; i\,\frac{M_Z^2}{v}\,\eta^{\mu\nu}$$

$$V_{hhWW}^{\mu\nu} \;=\; i\,\frac{2M_W^2}{v^2}\,\eta^{\mu\nu}, \qquad V_{hhZZ}^{\mu\nu} \;=\; i\,\frac{M_Z^2}{v^2}\,\eta^{\mu\nu}$$

**Derived in:** Ch 11 §11.8 from the covariant derivative of the Higgs doublet squared.

### Triple gauge vertices ($WWZ$, $WW\gamma$)

$$V_{WW\gamma}^{\mu\nu\rho}(k,k',q) \;=\; -ie\Bigl[\eta^{\mu\nu}(k-k')^\rho + \eta^{\nu\rho}(k'-q)^\mu + \eta^{\rho\mu}(q-k)^\nu\Bigr]$$

with an analogous $WWZ$ vertex obtained by replacing $e \to e\cot\theta_W$. **Derived in:** Ch 11 §11.9 from the non-abelian $SU(2)_L$ structure. The triple-gauge couplings are what distinguish a genuine non-abelian gauge theory from a collection of massive vector fields.

### Quartic gauge vertices

Exist for $WWWW$, $WWZZ$, $WW\gamma\gamma$, $WWZ\gamma$ combinations, with standard forms given in Ch 11 Table 11.3; omitted here for brevity but listed for completeness in the chapter reference.

### CP-violation note (GitHub #3)

The $W^\pm$ vertex above includes the CKM (or PMNS) matrix which is in principle complex. The single physical CP-violating phase in the CKM matrix (the Jarlskog invariant $J$) is an *input* to the framework at this point — the zone-architecture derivation of its value from first principles is open. Chapter 13 identifies the topological origin of the phase but not its magnitude.

---

## C.6 External-Line Factors

External particles on the left or right edges of a diagram do not get propagators; they get *wavefunctions*.

| Particle | Incoming | Outgoing |
|---|---|---|
| Fermion (spin-$\tfrac12$) | $u^{(s)}(p)$ | $\bar u^{(s)}(p)$ |
| Antifermion | $\bar v^{(s)}(p)$ | $v^{(s)}(p)$ |
| Photon | $\varepsilon^{(\lambda)}_\mu(k)$ | $\varepsilon^{*(\lambda)}_\mu(k)$ |
| Massive vector ($W, Z$) | $\varepsilon^{(\lambda)}_\mu(k)$ | $\varepsilon^{*(\lambda)}_\mu(k)$ |
| Scalar (real or complex) | $1$ | $1$ |
| Gluon | $\varepsilon^{(\lambda)}_\mu(k)\,\delta^{aa_0}$ | $\varepsilon^{*(\lambda)}_\mu(k)\,\delta^{aa_0}$ |

Here $s$ labels the spin state and $\lambda$ the polarization. Spinor conventions follow Ch 6 §6.6; photon polarization sums use
$$\sum_\lambda \varepsilon^{(\lambda)}_\mu(k)\varepsilon^{*(\lambda)}_\nu(k) \;\to\; -\eta_{\mu\nu}$$
when contracted with a gauge-invariant amplitude (Ward identity). For massive vectors the polarization sum is
$$\sum_\lambda \varepsilon^{(\lambda)}_\mu(k)\varepsilon^{*(\lambda)}_\nu(k) \;=\; -\eta_{\mu\nu} + \frac{k_\mu k_\nu}{M^2}.$$

---

## C.7 Loop Rules

### Momentum integration

For each independent loop momentum $\ell$ not fixed by momentum conservation at vertices, integrate with measure

$$\int \frac{d^4\ell}{(2\pi)^4}.$$

In dimensional regularization this becomes $\int d^d\ell/(2\pi)^d$ with $d=4-\epsilon$ and Vol 4 Ch 8 §8.4 gives the standard expressions for the resulting integrals.

### Feynman parameters

For combining propagator denominators,

$$\frac{1}{A_1 A_2\cdots A_n} \;=\; (n-1)!\int_0^1 dx_1\cdots dx_n\,\delta\!\bigl(\textstyle\sum_i x_i - 1\bigr)\frac{1}{(x_1 A_1 + \cdots + x_n A_n)^n}.$$

**Derived in:** Ch 7 §7.7.

### Standard one-loop integral

$$\int \frac{d^4\ell}{(2\pi)^4}\frac{1}{(\ell^2-\Delta+i\epsilon)^n} \;=\; \frac{(-1)^n\,i}{(4\pi)^2}\frac{1}{(n-1)(n-2)}\,\Delta^{2-n} \qquad (n\ge 3)$$

with logarithmic divergences for $n=2$ handled in dimensional regularization (Ch 8 §8.4).

### Symmetry factors

Divide by the diagram's symmetry factor $S$, which is the order of the automorphism group of the diagram when internal lines are labeled. Common cases:

- Self-energy bubble in $\phi^4$ theory: $S = 2$.
- Sunset diagram in $\phi^4$: $S = 6$.
- QED vertex correction: $S = 1$.
- QED photon self-energy: $S = 1$ (the fermion loop is directed, so no $1/2$).

**Derived in:** Ch 7 §7.7.

### Fermion-loop sign

Every closed fermion loop contributes an overall factor of $-1$. **Derived in:** Ch 6 §6.6 from the anticommutation of fermion operators in Wick's theorem.

### Trace over fermion loops

For a closed fermion loop, after writing the propagators, **take the trace** of the resulting Dirac-index product:
$$\text{Loop} \;=\; -\int\frac{d^4\ell}{(2\pi)^4}\,\text{Tr}\bigl[S_F(\ell)\,\Gamma\,S_F(\ell+k)\,\Gamma'\,\cdots\bigr]$$
where $\Gamma,\Gamma',\ldots$ are the vertex factors around the loop. Useful identities:

- $\text{Tr}[\gamma^\mu\gamma^\nu] = 4\eta^{\mu\nu}$
- $\text{Tr}[\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma] = 4(\eta^{\mu\nu}\eta^{\rho\sigma}-\eta^{\mu\rho}\eta^{\nu\sigma}+\eta^{\mu\sigma}\eta^{\nu\rho})$
- $\text{Tr}[\text{odd number of }\gamma^\mu] = 0$
- $\text{Tr}[\gamma^5] = 0$, $\text{Tr}[\gamma^5\gamma^\mu\gamma^\nu] = 0$, $\text{Tr}[\gamma^5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma] = -4i\epsilon^{\mu\nu\rho\sigma}$

### Renormalization counterterms

For a renormalizable theory, divergences absorb into a finite set of counterterms. In Vol 4 Ch 8, the counterterms for QED are:

- Electron self-energy: $\delta_m$ (mass) and $\delta_Z$ (wave function)
- Photon self-energy: $\delta_3$ (photon wave function)
- Vertex: $\delta_1$ (vertex counterterm)

Ward identity: $\delta_1 = \delta_Z$, which means the charge renormalization is controlled by photon wave-function renormalization alone (Ch 8 §8.7).

---

## C.8 Zone-Architecture Notes

The rules above are identical in form to those of the standard model because Vol 4 Ch 6 shows that canonical quantization of the zone Lagrangian reproduces the standard-model Lagrangian term by term. Where the *derivations* differ from a conventional QFT text:

1. **Origin of the gauge couplings.** The $SU(3)_c\times SU(2)_L\times U(1)_Y$ gauge group is not put in by hand; it is derived from symmetries of the zone manifold in Vol 2 Ch 6 and Vol 4 Ch 6. The *values* of $g_s, g_w, g'$ at some reference scale are CALIBRATION quantities; the *running* is derived (Ch 8).

2. **Origin of fermion fields.** Dirac fermions are treated as effective fields in these rules. The ab-initio derivation from a bosonic Firmament via topological vortices (Vol 1 Ch 9 Eq. 1.9.19; Vol 3 Ch 6; Vol 4 Ch 10 §10.5) is an open problem (GitHub #1). The Feynman rules above are valid in the *effective theory* of the vortex collective modes; they will not change when the underlying derivation is completed.

3. **Origin of the Higgs.** The Higgs field and its VEV arise from the Waters-Above condensation mechanism (Ch 11 §§11.2–11.3). The shape of the Higgs potential is currently a *model* rather than a derivation from the Waters-field Lagrangian (GitHub #25); this affects Ch 11 mass predictions but not the Feynman rules, which depend only on the VEV and the assumed quadratic-plus-quartic potential shape near its minimum.

4. **Origin of the running couplings.** The beta functions are computed at one loop in Ch 8 §§8.6–8.8 from the same diagrams that appear in standard QED/QCD texts. Two-loop precision is GitHub #26 and is not yet in this edition.

In short: the Feynman rules are the standard-model Feynman rules, and Vol 4 gets no special credit for reproducing them at this level — the credit is claimed in the *Lagrangian derivations* (Vol 2 Ch 5–6 and Vol 4 Ch 6–8), not in the Feynman rules that follow from the Lagrangians.

---

*End of Appendix C. Continues with Problem Sets.*
