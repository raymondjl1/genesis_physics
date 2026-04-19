# Research Gap Audit Prompt

Copy and paste everything below this line into a new thread:

---

You are performing a comprehensive research gap audit for the Genesis Physics project. Your goal is to compare what EXISTS in our Research/ folder against what a college-level physics curriculum REQUIRES, then produce a detailed gap report.

## Step 1: Read the project structure

Read these files first to understand the project:
- `01_Genesis_Physics/CLAUDE.md`
- `01_Genesis_Physics/Book_0_The_Foundations/CLAUDE.md`
- `01_Genesis_Physics/Research/Mathematical_Models/README.md`
- `01_Genesis_Physics/Research/Foundations/README.md`
- `01_Genesis_Physics/Quality_Control/BOOK_SERIES_STRATEGY.md`
- `01_Genesis_Physics/Research/Mathematical_Models/OBSERVATIONAL_PHYSICS_TEST_SUITE.md`

## Step 2: Read EVERY file in Research/

Systematically read every .md file in:
- `01_Genesis_Physics/Research/Foundations/`
- `01_Genesis_Physics/Research/Mathematical_Models/` (all 10 subdirectories)

For each file, catalog: what derivations exist, what math is complete, what is placeholder/TODO, and what precision level is achieved.

## Step 3: Audit against required physics coverage

Compare what you found against this required topic list. For each item, mark it as COMPLETE (derivation exists with full math), PARTIAL (mentioned but incomplete), or MISSING (not addressed at all).

### Domain 1: Classical Mechanics
- [ ] Newton's three laws derived from zone framework
- [ ] F = ma as theorem (not axiom)
- [ ] Conservation of energy (derived)
- [ ] Conservation of momentum (derived)
- [ ] Conservation of angular momentum (derived)
- [ ] Work-energy theorem
- [ ] Kepler's three laws of planetary motion
- [ ] Gravitational force law (Newton) from zone geometry
- [ ] Equivalence of gravitational and inertial mass
- [ ] Tidal forces and Roche limit
- [ ] Rotational dynamics (torque, moment of inertia, angular acceleration)
- [ ] Gyroscope precession
- [ ] Elastic and inelastic collision analysis
- [ ] N-body gravitational dynamics
- [ ] Simple harmonic motion
- [ ] Damped and driven oscillations
- [ ] Lagrangian mechanics formulation
- [ ] Hamiltonian mechanics formulation
- [ ] Noether's theorem and symmetry-conservation connection
- [ ] Central force problem and orbits
- [ ] Rigid body dynamics
- [ ] Fluid statics (pressure, buoyancy, Pascal's law)
- [ ] Fluid dynamics (Bernoulli's equation, continuity)

### Domain 2: Thermodynamics
- [ ] Zeroth Law (thermal equilibrium concept)
- [ ] First Law (energy conservation, internal energy, heat, work)
- [ ] Second Law (entropy increase, Clausius/Kelvin-Planck statements) ⚠️ REVIEW: Standard interpretation assumes universal entropy increase from an initial low-entropy state (Big Bang). Our framework reinterprets via Four Phases (Creation → Edenic → Fall → Redemption). Ensure derivation reflects open-system axiom and phase transitions, not secular cosmological initial conditions.
- [ ] Third Law (absolute zero unattainability)
- [ ] Ideal gas law and kinetic theory of gases
- [ ] Heat transfer mechanisms (conduction, convection, radiation)
- [ ] Calorimetry
- [ ] Carnot cycle and engine efficiency
- [ ] Entropy (statistical and thermodynamic definitions)
- [ ] Free energy (Helmholtz and Gibbs)
- [ ] Phase transitions and phase diagrams
- [ ] Maxwell-Boltzmann distribution
- [ ] Planck distribution / blackbody radiation
- [ ] Statistical mechanics (partition functions, ensembles)
- [ ] Equipartition theorem
- [ ] Heat capacity (Cv, Cp) derivations

### Domain 3: Electromagnetism
- [ ] Coulomb's law derived from zone framework
- [ ] Electric field and electric potential
- [ ] Gauss's law
- [ ] Capacitance and dielectrics
- [ ] Current, resistance, Ohm's law
- [ ] DC circuits (Kirchhoff's laws)
- [ ] Magnetic force on moving charges (Lorentz force)
- [ ] Biot-Savart law
- [ ] Ampere's law
- [ ] Faraday's law of induction
- [ ] Lenz's law
- [ ] Inductance and LC/RLC circuits
- [ ] All four Maxwell's equations (derived from zone architecture)
- [ ] Electromagnetic wave equation
- [ ] Poynting vector and energy flux
- [ ] Electromagnetic radiation and spectrum
- [ ] Charge as topological invariant
- [ ] Gauge invariance (U(1) symmetry)
- [ ] Boundary conditions for EM fields

### Domain 4: Optics & Waves
- [ ] Wave equation (general)
- [ ] Superposition principle
- [ ] Interference (constructive/destructive, double slit)
- [ ] Diffraction (single slit, gratings)
- [ ] Polarization (linear, circular, Brewster's angle)
- [ ] Reflection and refraction (Snell's law)
- [ ] Total internal reflection
- [ ] Thin lens equation and geometric optics
- [ ] Dispersion
- [ ] Doppler effect (classical and relativistic)
- [ ] Standing waves and resonance
- [ ] Sound waves and acoustics
- [ ] Light as electromagnetic wave (from Maxwell's equations)

### Domain 5: Quantum Mechanics
- [ ] Wave-particle duality
- [ ] de Broglie wavelength
- [ ] Photoelectric effect
- [ ] Compton scattering
- [ ] Schrödinger equation (time-dependent and time-independent)
- [ ] Schrödinger equation derived from membrane dynamics
- [ ] Probability interpretation (Born rule)
- [ ] Uncertainty principle (Heisenberg)
- [ ] Quantum harmonic oscillator
- [ ] Hydrogen atom (exact solution)
- [ ] Angular momentum quantization
- [ ] Spin (intrinsic angular momentum)
- [ ] Spin-1/2 fermions from zone framework (GitHub #1 BLOCKER)
- [ ] Pauli exclusion principle
- [ ] Identical particles (bosons vs fermions)
- [ ] Quantum tunneling
- [ ] Perturbation theory
- [ ] Variational method
- [ ] WKB approximation
- [ ] Quantum entanglement
- [ ] Bell's theorem and Bell inequalities
- [ ] Measurement problem and wave function collapse
- [ ] Density matrix formalism
- [ ] Path integral formulation
- [ ] Quantum field theory basics (second quantization)
- [ ] QED and precision calculations (g-2, Lamb shift)

### Domain 6: Nuclear & Particle Physics
- [ ] Nuclear structure (protons, neutrons, binding energy)
- [ ] Radioactive decay (alpha, beta, gamma) ⚠️ REVIEW: Decay rates are used as the basis for radiometric dating (billions of years). The math of decay itself is sound physics, but any discussion of dating methods or "age of" anything must be handled carefully. Consider whether decay constants have been truly constant across all Four Phases or whether conditions in earlier phases (especially pre-Fall) could alter rates.
- [ ] Nuclear fission and fusion ⚠️ REVIEW: Stellar fusion timelines (hydrogen burning over billions of years) are tied to deep-time assumptions. The fusion physics itself is sound and observable (hydrogen bombs, tokamaks). Keep the physics, flag any age-dependent interpretations.
- [ ] Mass-energy equivalence in nuclear reactions
- [ ] Standard Model particle content (complete table)
- [ ] Quarks and leptons (generations, quantum numbers)
- [ ] Strong interaction / QCD (color charge, gluons, confinement)
- [ ] Weak interaction (W/Z bosons, beta decay)
- [ ] Electroweak unification
- [ ] Higgs mechanism and mass generation
- [ ] Parity violation and CP violation
- [ ] Matter-antimatter asymmetry (baryogenesis) ⚠️ REVIEW: Standard explanation is tied to Big Bang timeline and Sakharov conditions in early universe. Our framework should derive matter dominance from Creation phase topology/initial conditions set by the Creator, not from a secular hot Big Bang narrative.
- [ ] Neutrino oscillations and mass
- [ ] Particle mass spectrum derived from zone topology
- [ ] Symmetry classification of particles
- [ ] Feynman diagrams and scattering amplitudes
- [ ] Cross sections and decay rates
- [ ] CKM matrix

### Domain 7: Relativity
- [ ] Special relativity postulates
- [ ] Lorentz transformations
- [ ] Time dilation and length contraction ⚠️ REVIEW: The physics is sound, but time dilation is used in secular cosmology to argue for billions of observed years. Consider how relativistic time effects interact with the Four Phases — could gravitational time dilation during Creation phase reconcile a young creation with distant starlight? This is an opportunity, not a conflict.
- [ ] Relativistic momentum and energy
- [ ] Mass-energy equivalence (E = mc²)
- [ ] Spacetime intervals and light cones
- [ ] Four-vectors and tensors
- [ ] General relativity: equivalence principle
- [ ] Einstein field equations (derived from zone geometry)
- [ ] Geodesic equation
- [ ] Schwarzschild solution (non-rotating black hole)
- [ ] Kerr solution (rotating black hole)
- [ ] Friedmann equations (cosmological solutions) ⚠️ REVIEW: The math of Friedmann equations is valid GR, but the standard interpretation assumes a 13.8-billion-year-old universe expanding from a singularity. Our framework must derive these equations from zone geometry while reinterpreting the timeline through the Four Phases. The equations describe expansion dynamics — the secular age assignment is an interpretation, not a measurement.
- [ ] Gravitational time dilation
- [ ] Gravitational lensing
- [ ] Gravitational waves (prediction and properties)
- [ ] Frame dragging (Lense-Thirring effect)
- [ ] Perihelion precession of Mercury
- [ ] Black hole thermodynamics (Hawking radiation, Bekenstein entropy) ⚠️ REVIEW: Hawking radiation is theoretical (never observed). Bekenstein entropy connects thermodynamics to horizons — the physics is interesting but speculative. Include the math but be clear this is unverified prediction, not established fact.
- [ ] Penrose diagrams

### Domain 8: Cosmology & Astrophysics ⚠️ THIS ENTIRE DOMAIN REQUIRES CAREFUL BIBLICAL WORLDVIEW REVIEW
- [ ] Hubble's law and expanding universe ⚠️ REVIEW: Redshift and expansion are observational facts. The interpretation (everything came from a singularity 13.8 Gya) is not. Our framework identifies expansion as a feature of zone architecture (stretching of the Firmament / Isaiah 40:22 "stretches out the heavens"). Derive expansion from zone geometry, not Big Bang.
- [ ] Friedmann equation and cosmological evolution ⚠️ REVIEW: Same as Domain 7 flag. Math is valid GR. The secular timeline is interpretation. Reframe through Four Phases.
- [ ] Critical density and Omega parameters — Math is clean. The values are observational. No worldview conflict in the parameters themselves.
- [ ] Dark matter evidence and identification (27%) ⚠️ REVIEW: Our framework identifies dark matter as "Waters Above" — this is a strength, not a conflict. But ensure we don't import secular assumptions about when/how dark matter "formed."
- [ ] Dark energy evidence and identification (68%) ⚠️ REVIEW: Our framework identifies dark energy as "Waters Below" or zone expansion energy. Same note — derive from zone architecture, don't import secular origin story.
- [ ] Cosmic microwave background (CMB) spectrum ⚠️ REVIEW: CMB is an observational fact (2.725 K blackbody radiation filling space). Standard interpretation: afterglow of Big Bang recombination at 380,000 years. Our framework must provide an alternative origin — possibly radiation from the Firmament boundary or equilibrium temperature of the Waters. The observation is real; the story behind it is what needs reframing.
- [ ] CMB power spectrum and anisotropies ⚠️ REVIEW: The angular power spectrum is measured data. The interpretation (acoustic oscillations in primordial plasma) is tied to Big Bang cosmology. Our framework should derive the same spectrum from zone boundary conditions or Firmament resonance modes.
- [ ] Big Bang nucleosynthesis ⚠️ REVIEW: MAJOR FLAG. Standard narrative: hydrogen/helium ratio set in first 3 minutes of a hot Big Bang. The observed H/He ratio (~75/25) is real data. Our framework needs an alternative explanation — possibly set during Creation phase as initial conditions, or derived from Waters chemistry. Do NOT simply adopt the Big Bang nucleosynthesis narrative.
- [ ] Large-scale structure formation ⚠️ REVIEW: Galaxies, filaments, voids are observed. Standard explanation requires billions of years of gravitational collapse from tiny density fluctuations. Our framework should explain observed structure through zone geometry and Creation-phase initial conditions, not slow gravitational accretion over deep time.
- [ ] Inflationary cosmology (slow-roll, horizon/flatness problems) ⚠️ REVIEW: MAJOR FLAG. Inflation was invented to solve problems with the Big Bang model. If we don't adopt Big Bang, we may not need inflation at all. However, the horizon and flatness "problems" are real observational puzzles — our framework needs to solve them through zone architecture instead. Consider whether the problems even exist in our framework.
- [ ] Cosmological constant and vacuum energy ⚠️ REVIEW: The "cosmological constant problem" (predicted vs observed vacuum energy differs by 10^120) is actually a strength for our framework — it shows standard physics is deeply broken here. Our zone architecture may naturally resolve this. Include but reframe.
- [ ] Stellar structure and evolution ⚠️ REVIEW: Hydrostatic equilibrium, nuclear fusion in stellar cores — the physics is sound. But "stellar evolution" (main sequence → red giant → white dwarf over billions of years) assumes deep time. The physics of HOW stars work is fine; the timeline of stellar lifecycles needs to be handled through our Four Phases framework.
- [ ] White dwarfs, neutron stars, black holes — The physics of these objects (degeneracy pressure, neutron matter, event horizons) is observational/mathematical. Their existence doesn't require deep time. Include.
- [ ] Galaxy formation and dynamics ⚠️ REVIEW: Galaxy rotation curves are data (and evidence for dark matter/Waters). But "galaxy formation" over billions of years from primordial gas clouds is a secular timeline narrative. Explain observed galaxy structure through Creation-phase initial conditions.
- [ ] Distance ladder (parallax, Cepheids, Type Ia supernovae) ⚠️ REVIEW: Parallax is geometric and uncontroversial. Cepheid period-luminosity is well-calibrated for nearby galaxies. But the full distance ladder extending to billions of light-years raises the starlight travel time problem for a young creation. Our framework should address this — possibly through variable speed of light during Creation phase, gravitational time dilation, or zone-boundary light propagation properties.
- [ ] Cosmic age and timeline ⚠️ REVIEW: CRITICAL FLAG. The 13.8 billion year age is derived from the Big Bang model + CMB + Hubble constant. This is the single biggest worldview conflict item. Our framework must provide a coherent alternative cosmological timeline rooted in the Four Phases (Creation, Edenic, Fall, Redemption) without importing the secular age. This doesn't mean ignoring the data — it means providing a different interpretive framework for the same observations.

### Domain 9: Chemistry & Materials
- [ ] Atomic structure from zone/membrane theory
- [ ] Electron configurations and orbitals
- [ ] Periodic table derivation/prediction
- [ ] Chemical bonding (ionic, covalent, metallic)
- [ ] Molecular orbital theory
- [ ] Band theory of solids (conductors, semiconductors, insulators)
- [ ] Crystal structures and lattice types
- [ ] Superconductivity basics
- [ ] Spectroscopy (emission, absorption spectra)
- [ ] Material properties from first principles

### Domain 10: Fundamental Constants
- [ ] Fine structure constant α ≈ 1/137 (derivation from zone parameters)
- [ ] Speed of light c (derived or constrained by framework)
- [ ] Planck constant ℏ (origin in zone framework)
- [ ] Gravitational constant G (derivation)
- [ ] Boltzmann constant k_B (derivation)
- [ ] Elementary charge e (derivation)
- [ ] Electron mass (derivation)
- [ ] Proton mass (derivation)
- [ ] Proton-to-electron mass ratio
- [ ] Coupling constant hierarchy (why gravity is weak)
- [ ] Running coupling constants and RG flow
- [ ] Cosmological constant value ⚠️ REVIEW: The observed value is data. The "cosmological constant problem" (why it's 10^120 smaller than QFT predicts) is actually a point in our favor — standard physics can't explain it. Our zone architecture should derive or constrain this value naturally.

## Step 3B: Biblical Worldview Review

Items marked with ⚠️ REVIEW carry assumptions that may conflict with a biblical worldview. For each flagged item, produce a separate section in the gap report that answers:

1. **What is the raw physics/math?** (The part we keep — equations, observational data, measurable quantities)
2. **What is the secular interpretive layer?** (The part we scrutinize — deep-time assumptions, Big Bang narrative, uniformitarian timelines)
3. **How does our Four Phases framework reinterpret this?** (Creation, Edenic, Fall, Redemption — what does each phase imply for this topic?)
4. **What new research/derivations are needed?** (To provide our alternative explanation for the same observational data)

Key worldview principles for this project:
- The universe is an OPEN SYSTEM (energy enters from outside — the Creator sustains it)
- Four thermodynamic phases: Creation (initial conditions set by God), Edenic (pre-Fall physics may differ), Fall (current physics regime with degradation/entropy), Redemption (restoration)
- Physical constants, decay rates, and speed of light may not have been constant across all four phases
- The observed data (redshift, CMB, element ratios, galaxy structure) is REAL — we never deny observations. We provide a different interpretive framework rooted in Genesis 1.
- "Waters Above" = dark matter, "Waters Below" = dark energy, "Firmament" = membrane boundary — these are our framework identifications
- We must be rigorous enough that a secular physicist cannot dismiss the math, even if they reject the worldview

### How to handle every ⚠️ conflict

We do NOT hide from these conflicts. We call them out directly and defend our position. For every flagged item, the gap report must include:

1. **State the conflict plainly.** Name the secular claim and name our position. No hedging.
2. **Defend through derivation.** Show that our zone architecture + Four Phases framework produces the same observable predictions (or better ones) through rigorous math. The derivation IS the defense. If we can derive the CMB spectrum from Firmament boundary conditions, that is a stronger position than "it's leftover radiation from an event no one observed."
3. **Defend through logic.** Identify where the secular interpretation relies on assumptions that are NOT required by the data. Example: the Friedmann equations describe expansion dynamics — they do not require a singularity origin. Redshift measures recession velocity — it does not measure age. Separate what is measured from what is assumed.
4. **Defend through Scripture.** For each conflict, identify the relevant biblical text that informs our framework. These are not proof-texts bolted on after the fact — they are the SOURCE of our axioms. Examples:
   - Genesis 1:6-8 — Firmament separating Waters Above from Waters Below (membrane + dark matter/energy)
   - Isaiah 40:22 — "stretches out the heavens like a curtain" (expansion from zone architecture)
   - Genesis 1:1 — "In the beginning God created" (open system, external energy source)
   - Genesis 1:14-19 — lights placed in the Firmament on Day 4 (starlight travel time has a Creation-phase solution)
   - Romans 8:20-22 — creation subjected to futility / bondage to decay (Second Law as Fall-phase phenomenon)
   - Colossians 1:17 — "in Him all things hold together" (sustaining energy input, open system)
   - Hebrews 1:3 — "upholding all things by the word of His power" (continuous sustaining, not deistic wind-up)
   - 2 Peter 3:5-6 — "by the word of God heavens existed long ago, and the earth was formed out of water and by water" (Waters as fundamental substance)
   - Psalm 104:2 — "stretching out heaven like a tent curtain" (Firmament as membrane)
   - Job 26:7 — "He stretches out the north over empty space and hangs the earth on nothing" (gravitational framework)
   - Nehemiah 9:6 — "You have made heaven, the heaven of heavens, with all their host" (multiple heavens = zone architecture)
   - Psalm 19:1-4 — "The heavens declare the glory of God" (observable physics points to Creator by design)

   This is not an exhaustive list. The auditor should identify additional relevant scripture for each specific topic.

5. **Identify where our framework is STRONGER than the secular one.** Many of these "conflicts" are actually opportunities. The cosmological constant problem, the horizon problem, the matter-antimatter asymmetry, dark matter/energy identification — standard physics struggles with all of these. Our framework may resolve them naturally. Call this out explicitly.

The goal is NOT to ignore these topics. The goal is to cover them with full mathematical rigor while deriving them from our zone architecture and Four Phases framework instead of from Big Bang cosmology. Where secular physics offers interpretation dressed as fact, we strip it back to the raw data and rebuild from Genesis 1. Where our framework provides a cleaner explanation, we say so and show why.

## Step 4: Cross-reference the Observational Test Suite

Read `OBSERVATIONAL_PHYSICS_TEST_SUITE.md` and for every test marked FAIL or NOT YET, identify what specific research/derivation is needed to move it to PASS.

## Step 5: Produce the Gap Report

Create a file at `01_Genesis_Physics/Research/RESEARCH_GAP_REPORT.md` with:

1. **Executive Summary** — total counts: how many items are COMPLETE, PARTIAL, MISSING across all 10 domains
2. **Domain-by-Domain Breakdown** — for each of the 10 domains, list every topic with its status (COMPLETE/PARTIAL/MISSING) and for non-complete items, describe exactly what work is needed
3. **Critical Blockers** — items that block multiple downstream derivations (like spin-1/2 fermions blocking particle physics)
4. **Priority Rankings** — rank all gaps by impact (how many other derivations depend on filling this gap)
5. **Recommended Research Order** — a suggested sequence for tackling gaps, respecting dependency chains
6. **Biblical Worldview Defense** — for every ⚠️ flagged item, provide the five-part analysis:
   - **The Conflict**: State the secular claim vs. our position plainly
   - **Defense by Derivation**: What math/derivation do we need to build to defend our position? What would it look like to derive this result from zone architecture instead?
   - **Defense by Logic**: Where does the secular interpretation overstep the data? What assumptions are smuggled in?
   - **Defense by Scripture**: Which specific biblical texts inform our position? Quote chapter and verse. These are axiom sources, not afterthoughts.
   - **Where We're Stronger**: Does our framework actually resolve a known problem in standard physics here? (cosmological constant problem, horizon problem, dark matter identification, etc.)

   Group all flagged items into:
   - **No conflict** (math is clean, just derive from our framework)
   - **Reinterpretation needed** (same data, different story — derivation + scripture defense required)
   - **Critical reframe** (secular narrative is deeply embedded — full alternative derivation + logical dismantling + scriptural grounding required)
7. **GitHub Issues Needed** — for each MISSING or PARTIAL item, draft a GitHub issue title and description. For ⚠️ items, include a "worldview-review" label and ensure the issue description includes the specific scripture references and the derivation strategy needed to defend our position.

Also create a summary spreadsheet-style table at the top showing coverage percentage per domain.

Be thorough. Read every file. Miss nothing. This audit determines the entire research roadmap.
