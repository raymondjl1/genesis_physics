#!/bin/bash

# Genesis Physics Simulation Suite - All Tests
# Runs all three simulation modules with output to stdout and files

SIMDIR="/sessions/trusting-quirky-cannon/mnt/ExodusProtocol/01_Genesis_Physics/Research/Simulations"
cd "$SIMDIR"

echo "======================================================================"
echo "Genesis Physics - Complete Simulation Suite"
echo "======================================================================"
echo ""

# Check for required modules
echo "Checking dependencies..."
python3 -c "import numpy; print('  ✓ numpy')" || exit 1
python3 -c "import scipy; print('  ✓ scipy')" || exit 1
python3 -c "import matplotlib; print('  ✓ matplotlib')" || exit 1
echo ""

echo "Running simulations..."
echo ""

# Test 1: Waters Field Evolution
echo "======================================================================"
echo "1. Waters Field Equations - Field Dynamics"
echo "======================================================================"
echo "   Output: test1_equilibrium.png"
echo "           test2_evolution_1d.png"
echo "           test3_evolution_2d.png"
echo "           test4_convergence.png"
echo ""
python3 waters_field_sim.py
RESULT1=$?
echo ""

# Test 2: Membrane Vibrations
echo "======================================================================"
echo "2. Membrane Vibration Spectrum - Particle Masses"
echo "======================================================================"
echo "   Output: spectrum_1d_string.png"
echo "           spectrum_circular.png"
echo "           spectrum_vs_particles.png"
echo "           spectrum_comparison.png"
echo ""
python3 membrane_vibrations.py
RESULT2=$?
echo ""

# Test 3: Structure Formation
echo "======================================================================"
echo "3. Structure Formation - ΛCDM vs Genesis Physics"
echo "======================================================================"
echo "   Output: growth_factor.png"
echo "           power_spectrum.png"
echo "           spectrum_ratio.png"
echo "           density_contrast.png"
echo "           halo_mass_function.png"
echo ""
python3 structure_formation.py
RESULT3=$?
echo ""

# Summary
echo "======================================================================"
echo "SIMULATION SUITE SUMMARY"
echo "======================================================================"

if [ $RESULT1 -eq 0 ]; then
    echo "✓ Waters Field Equations: PASSED"
else
    echo "✗ Waters Field Equations: FAILED"
fi

if [ $RESULT2 -eq 0 ]; then
    echo "✓ Membrane Vibrations: PASSED"
else
    echo "✗ Membrane Vibrations: FAILED"
fi

if [ $RESULT3 -eq 0 ]; then
    echo "✓ Structure Formation: PASSED"
else
    echo "✗ Structure Formation: FAILED"
fi

echo ""
echo "Generated files:"
ls -lh "$SIMDIR"/*.png "$SIMDIR"/*.md 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
echo ""
echo "Documentation:"
echo "  See SIMULATION_RESULTS.md for complete results and validation"
echo ""
echo "======================================================================"

if [ $RESULT1 -eq 0 ] && [ $RESULT2 -eq 0 ] && [ $RESULT3 -eq 0 ]; then
    echo "ALL TESTS PASSED ✓"
    exit 0
else
    echo "SOME TESTS FAILED"
    exit 1
fi
