#!/usr/bin/env python3
"""
Tiered Error Threshold System for Genesis Physics Tests
=========================================================

Defines a four-tier error classification system for all physics validation tests.
Each tier has its own acceptable error threshold reflecting the maturity and
complexity of the physics being tested.

Tier 1: Precision Tests (< 1% error)
    - Exact derivations from first principles
    - Fundamental constants and universal relationships
    - Well-established physics with no approximations needed
    Examples: Equivalence Principle, Kepler's 3rd Law, Compton Scattering

Tier 2: Quantitative Tests (< 10% error)
    - Well-understood physics with controlled approximations
    - Validated by centuries of experimental data
    - Small corrections or higher-order effects may be omitted
    Examples: Clausius-Clapeyron, Nuclear Binding Energy, Hawking Temperature

Tier 3: Order-of-Magnitude Tests (< 100% error)
    - Qualitative/approximate models or simplified geometries
    - Physics that emerges from combined effects
    - Complex many-body systems with reduced degrees of freedom
    Examples: Young's Modulus, BEC Critical Temperature, Superfluidity

Tier 4: Directional Tests (sign/trend only)
    - Conceptual validation of physical principles
    - Prototype simulations or exploratory models
    - Early-stage Genesis Physics extensions
    (Not yet populated; reserve tier for future use)
"""

# Error threshold percentages
TIER_1_THRESHOLD = 1.0      # percent - exacting precision
TIER_2_THRESHOLD = 10.0     # percent - well-understood physics
TIER_3_THRESHOLD = 100.0    # percent - order of magnitude / qualitative

# Classification of all existing tests by error tier
TEST_TIERS = {
    # ========================================================================
    # TIER 1: Precision Tests (< 1% error)
    # ========================================================================
    # Fundamental principles and universal laws
    "Equivalence Principle": 1,
    "Kepler's Third Law": 1,
    "Tidal Forces": 1,
    "Geodetic Precession": 1,

    # Thermodynamics - fundamental laws
    "Carnot Efficiency": 1,
    "Boltzmann Distribution": 1,
    "Stefan-Boltzmann Law": 1,
    "Wien's Displacement Law": 1,
    "Planck Spectrum": 1,

    # Astrophysics - well-measured quantities
    "Solar Luminosity": 1,
    "CMB Temperature": 1,
    "Hubble's Law": 1,

    # Electromagnetism - universal constant
    "EM Spectrum / Universal Speed": 1,

    # Electromagnetism - wave phenomena
    "Skin Effect": 1,
    "Refraction / Snell's Law": 1,

    # Quantum mechanics - photons
    "Compton Scattering": 1,

    # Relativity - predicted effects
    "Mercury Perihelion Precession": 1,
    "Light Bending": 1,
    "Frame Dragging": 1,
    "Coordinate Time Integral": 1,

    # Quantum mechanics - hydrogen atom (first-principles QM)
    "Hydrogen Atom": 1,

    # Nuclear physics - fusion (mass-energy)
    "Nuclear Fusion": 1,

    # ========================================================================
    # TIER 2: Quantitative Tests (< 10% error)
    # ========================================================================
    # Classical mechanics - derived from geometry
    "Moment of Inertia": 2,

    # Thermodynamics - phase transitions (approximations used)
    "Van der Waals Critical Point": 2,
    "Clausius-Clapeyron": 2,

    # Nuclear physics - binding and decay
    "Nuclear Binding Energy": 2,
    "Nuclear Fission": 2,

    # Relativity - weak-field effects
    "Shapiro Time Delay": 2,

    # Black holes - quantum effects
    "Hawking Temperature": 2,

    # Superconductivity - BCS theory
    "Cooper Pairing": 2,
    "Meissner Effect": 2,

    # Quantum mechanics - helium atom
    "Helium Atom": 2,

    # ========================================================================
    # TIER 3: Order-of-Magnitude Tests (< 100% error)
    # ========================================================================
    # Materials science - complex many-body
    "Young's Modulus": 3,

    # Quantum mechanics - condensed matter
    "BEC Critical Temperature": 3,
    "Superfluidity": 3,

    # Particle physics - hadronic processes
    "Jet Multiplicity": 3,

    # Atomic physics - many-electron atoms
    "Ionization Energies": 3,
    "Slater's Rules": 3,
}

# Reverse mapping: tier -> list of test names
TESTS_BY_TIER = {}
for test_name, tier in TEST_TIERS.items():
    if tier not in TESTS_BY_TIER:
        TESTS_BY_TIER[tier] = []
    TESTS_BY_TIER[tier].append(test_name)


def get_threshold(test_name: str) -> float:
    """
    Get the error threshold (%) for a given test.

    Args:
        test_name: Name of the test as it appears in TEST_TIERS

    Returns:
        Error threshold in percent. Defaults to Tier 2 (10%) if test not found.
    """
    tier = TEST_TIERS.get(test_name, 2)
    if tier == 1:
        return TIER_1_THRESHOLD
    elif tier == 2:
        return TIER_2_THRESHOLD
    elif tier == 3:
        return TIER_3_THRESHOLD
    else:
        # Unknown tier - default to Tier 2
        return TIER_2_THRESHOLD


def get_tier(test_name: str) -> int:
    """
    Get the tier classification for a given test.

    Args:
        test_name: Name of the test as it appears in TEST_TIERS

    Returns:
        Tier number (1, 2, or 3). Defaults to 2 if test not found.
    """
    return TEST_TIERS.get(test_name, 2)


def get_tier_description(tier: int) -> str:
    """
    Get a human-readable description of a tier.

    Args:
        tier: Tier number (1, 2, or 3)

    Returns:
        Description string
    """
    descriptions = {
        1: "Precision Tests (< 1% error)",
        2: "Quantitative Tests (< 10% error)",
        3: "Order-of-Magnitude Tests (< 100% error)",
    }
    return descriptions.get(tier, "Unknown Tier")


def is_test_classified(test_name: str) -> bool:
    """Check if a test has been classified in the tier system."""
    return test_name in TEST_TIERS


def get_unclassified_tests(test_names: list) -> list:
    """Return list of tests from input that have not been classified."""
    return [name for name in test_names if not is_test_classified(name)]


if __name__ == "__main__":
    # Display summary statistics
    print("Genesis Physics Test Tier System Summary")
    print("=" * 70)

    for tier in sorted(TESTS_BY_TIER.keys()):
        tests = TESTS_BY_TIER[tier]
        threshold = get_threshold(tests[0]) if tests else "N/A"
        print(f"\nTier {tier}: {get_tier_description(tier)}")
        print(f"  Threshold: {threshold}%")
        print(f"  Count: {len(tests)}")
        print(f"  Tests:")
        for test in sorted(tests):
            print(f"    - {test}")

    print("\n" + "=" * 70)
    print(f"Total classified tests: {len(TEST_TIERS)}")
