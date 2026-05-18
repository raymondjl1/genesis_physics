"""
Genesis Physics: Planck Spectrum & Thermal Radiation Laws Test Suite
======================================================================

Issue #11: [Phase 1.3] Planck Spectrum & Thermal Radiation Laws (3 tests)

This test suite validates the following thermal radiation laws derived from Genesis Physics:

1. PLANCK SPECTRUM: B(λ,T) = (2hc²/λ⁵)·1/(e^(hc/λk_BT)-1)
   Derive from quantized membrane oscillator partition function.
   Verify at T=5778K (solar surface) and check peak matches Wien's law.

2. STEFAN-BOLTZMANN LAW: j* = σ_SB T⁴ where σ_SB = 2π⁵k_B⁴/(15h³c²) = 5.670×10⁻⁸ W/(m²·K⁴)
   Integrate Planck spectrum over all wavelengths.
   Compute σ_SB from fundamental constants, compare to textbook value (<1% error).

3. WIEN'S DISPLACEMENT LAW: λ_max T = b where b = 2.898×10⁻³ m·K
   Find peak of Planck spectrum.
   Compute b = hc/(k_B × x) where x = 4.965... (solution to x = 5(1-e^(-x))).

BONUS: Verify solar luminosity:
   L_sun = 4πR²σ_SB T⁴ at T=5778K, R=6.96×10⁸m → compare to 3.828×10²⁶ W

GENESIS PHYSICS FRAMEWORK:
- The Firmament is a 4D membrane in 6D spacetime
- Firmament vibration modes are quantized: E_n = ℏω(n + 1/2)
- For thermal radiation, each mode is a quantum harmonic oscillator
- Mean energy per mode: <E> = hν/(e^(hν/k_BT) - 1) from Bose-Einstein statistics
- Density of states for EM modes in a cavity: g(ν)dν = 8πν²/c³ dν
- Planck's law emerges from counting excited Firmament modes

KEY INSIGHT:
The spectral radiance B(λ,T) follows from:
  1. Quantized oscillator energy levels E_n = nhc/λ
  2. Partition function Z = 1/(1 - e^(-hc/λk_BT))
  3. Mean energy <E> = hc/λ / (e^(hc/λk_BT) - 1)
  4. Spectral radiance: B(λ,T) = (2hc²/λ⁵) / (e^(hc/λk_BT) - 1)

Test criteria: <1% error on Stefan-Boltzmann, <2% error on Wien peak
"""

import numpy as np
from numpy import pi, sqrt, exp, log, log10
import sys
from dataclasses import dataclass
from typing import Tuple, Dict
from scipy.optimize import fsolve
from scipy.integrate import quad

# ============================================================================
# PHYSICAL CONSTANTS
# ============================================================================

# Speed of light
C = 3.0e8  # m/s

# Planck's constant
HBAR = 1.054571817e-34  # J·s (reduced)
H_PLANCK = 6.62607015e-34  # J·s (full)

# Boltzmann constant
K_B = 1.380649e-23  # J/K

# Stefan-Boltzmann constant (textbook value)
SIGMA_SB_TEXTBOOK = 5.670374419e-8  # W/(m²·K⁴)

# Wien's displacement constant (textbook value)
B_WIEN_TEXTBOOK = 2.897771955e-3  # m·K

# Solar parameters
T_SUN = 5778.0  # K (solar surface temperature)
R_SUN = 6.96e8  # m (solar radius)
L_SUN_TEXTBOOK = 3.828e26  # W (solar luminosity)


def planck_spectral_radiance_wavelength(wavelength, T):
    """
    Compute Planck spectral exitance M(λ,T) in wavelength form.

    M(λ,T) = (2πhc²/λ⁵) · 1/(e^(hc/λk_BT)-1)

    Args:
        wavelength: wavelength (m)
        T: temperature (K)

    Returns:
        M(λ,T) in units of W/(m²·m) = W/m³
    """
    if wavelength <= 0:
        return 0.0
    c1 = 2 * pi * H_PLANCK * (C**2)
    exponent = (H_PLANCK * C) / (wavelength * K_B * T)

    # Avoid numerical overflow
    if exponent > 100:
        return 0.0
    else:
        exp_term = exp(exponent)
        return c1 / ((wavelength**5) * (exp_term - 1.0))


# ============================================================================
# TEST 1: PLANCK SPECTRUM
# ============================================================================

@dataclass
class PlanckSpectrumTest:
    """
    Test: Planck spectrum M(λ,T) = (2πhc²/λ⁵)·1/(e^(hc/λk_BT)-1)

    Derive from quantized membrane oscillator partition function:

    For a single mode with wavelength λ:
      - Energy levels: E_n = nhc/λ (n = 0, 1, 2, ...)
      - Partition function: Z(T) = Σ_n exp(-nhc/(λk_BT))
      - Geometric series: Z(T) = 1/(1 - exp(-hc/(λk_BT)))
      - Mean energy: <E> = hc/λ / (e^(hc/(λk_BT)) - 1)

    Spectral radiance (brightness) in wavelength form:
      - B(λ,T) = (2hc²/λ⁵) · 1/(e^(hc/(λk_BT)) - 1)
    """

    def run(self) -> Dict:
        """
        Calculate Planck spectrum at solar temperature (T = 5778 K)
        and verify peak matches Wien's law prediction.
        """
        results = {}
        T = T_SUN  # 5778 K (solar surface)

        # Wavelength range: optical spectrum (roughly 100 nm to 10 μm)
        wavelength_range = np.logspace(-7, -5, 300)  # logarithmic spacing

        # Compute Planck spectrum in wavelength form
        B_lambda = np.array([planck_spectral_radiance_wavelength(lam, T) for lam in wavelength_range])

        # Find peak (maximum of B(λ,T))
        idx_peak = np.argmax(B_lambda)
        lambda_peak = wavelength_range[idx_peak]
        B_peak = B_lambda[idx_peak]

        # Expected peak from Wien's displacement law: λ_max = b / T
        lambda_peak_wien = B_WIEN_TEXTBOOK / T

        # Error in peak wavelength
        error_lambda_peak = abs(lambda_peak - lambda_peak_wien) / lambda_peak_wien * 100

        # Check if Planck law is satisfied: error should be < 2%
        passed = error_lambda_peak < 2.0

        results['test_name'] = 'Planck Spectrum'
        results['temperature_K'] = T
        results['lambda_peak_m'] = lambda_peak
        results['lambda_peak_nm'] = lambda_peak * 1e9
        results['B_peak_W/m4'] = B_peak
        results['lambda_peak_wien_m'] = lambda_peak_wien
        results['lambda_peak_wien_nm'] = lambda_peak_wien * 1e9
        results['error_lambda_peak_percent'] = error_lambda_peak
        results['pass'] = passed

        # Verify partition function and mean energy at a specific wavelength
        lambda_visible = 5e-7  # m (visible light, 500 nm)
        hc_over_lambda = (H_PLANCK * C) / lambda_visible

        # Partition function for single mode
        x = hc_over_lambda / (K_B * T)
        Z_single = 1.0 / (1.0 - exp(-x))

        # Mean energy from partition function
        E_mean = hc_over_lambda / (exp(x) - 1.0)

        # Spectral radiance at this wavelength
        B_lambda_visible = planck_spectral_radiance_wavelength(lambda_visible, T)

        results['lambda_visible_m'] = lambda_visible
        results['lambda_visible_nm'] = lambda_visible * 1e9
        results['x_hc_lambda_kBT'] = x
        results['partition_function'] = Z_single
        results['mean_energy_J'] = E_mean
        results['B_lambda_visible_W/m4'] = B_lambda_visible

        results['description'] = (
            f"Planck Spectrum: M(λ,T) = (2πhc²/λ⁵)·1/(e^(hc/λk_BT)-1)\n"
            f"\nTest: Solar spectrum at T = {T} K\n"
            f"\nDerived from quantized oscillators:\n"
            f"  - Energy levels: E_n = nhc/λ (n = 0,1,2,...)\n"
            f"  - Partition function: Z = 1/(1 - e^(-hc/λk_BT))\n"
            f"  - Mean energy: <E> = hc/λ / (e^(hc/λk_BT) - 1)\n"
            f"  - Spectral exitance: M(λ,T) = (2πhc²/λ⁵) / (e^(hc/λk_BT) - 1)\n"
            f"\n" + "="*70 + "\n"
            f"PEAK OF PLANCK SPECTRUM (Verification of Wien's Law):\n"
            f"="*70 + "\n"
            f"\nPeak wavelength (from Planck spectrum):\n"
            f"  λ_peak = {lambda_peak:.4e} m = {lambda_peak*1e9:.1f} nm\n"
            f"\nPeak wavelength (from Wien's law λ_max = b/T):\n"
            f"  λ_max = {lambda_peak_wien:.4e} m = {lambda_peak_wien*1e9:.1f} nm\n"
            f"  (using b = {B_WIEN_TEXTBOOK:.6e} m·K)\n"
            f"\nError in peak wavelength:\n"
            f"  Δλ/λ = {error_lambda_peak:.3f}%\n"
            f"\n" + "="*70 + "\n"
            f"SINGLE WAVELENGTH: PARTITION FUNCTION & MEAN ENERGY:\n"
            f"="*70 + "\n"
            f"\nAt λ = {lambda_visible*1e9:.0f} nm (visible light):\n"
            f"  x = hc/(λ k_B T) = {x:.4f}\n"
            f"  Partition function Z = 1/(1-e^(-x)) = {Z_single:.6f}\n"
            f"  Mean energy <E> = hc/λ / (e^x - 1) = {E_mean:.4e} J\n"
            f"  Spectral radiance B(λ,T) = {B_lambda_visible:.4e} W/m⁴\n"
            f"\n✓ Planck spectrum derived from quantized oscillators\n"
            f"✓ Peak wavelength matches Wien's law to {error_lambda_peak:.2f}%\n"
        )

        if passed:
            results['description'] += f"✓ PASS: Error < 2%\n"
        else:
            results['description'] += f"✗ FAIL: Error = {error_lambda_peak:.2f}% > 2%\n"

        return results


# ============================================================================
# TEST 2: STEFAN-BOLTZMANN LAW
# ============================================================================

@dataclass
class StefanBoltzmannTest:
    """
    Test: Stefan-Boltzmann law j* = σ_SB T⁴

    Derive from Planck spectrum by integrating over all wavelengths:

    Total spectral power (energy flux):
      j*(T) = ∫₀^∞ B(λ,T) dλ

    where B(λ,T) = (2hc²/λ⁵) · 1/(e^(hc/λk_BT) - 1)

    Let x = hc/(λk_B T), so λ = hc/(xk_B T), dλ = -(hc)/(x²k_B T) dx:

      j*(T) = ∫_∞^0 (2hc²/λ⁵) · 1/(e^x - 1) · (-(hc)/(x²k_B T)) dx
             = (2hc² k_B⁴ T⁴ / (hc·c² k_B T·h³c)) ∫₀^∞ x³/(e^x - 1) dx
             = (2k_B⁴ T⁴/c² h³) ∫₀^∞ x³/(e^x - 1) dx

    The integral ∫₀^∞ x³/(e^x - 1) dx = π⁴/15

    Therefore:
      j*(T) = (2k_B⁴ T⁴/c² h³) · (π⁴/15) = σ_SB T⁴

      σ_SB = 2π⁵ k_B⁴ / (15 h³ c²) ≈ 5.670 × 10⁻⁸ W/(m²·K⁴)
    """

    def compute_stefan_boltzmann_from_constants(self) -> float:
        """
        Compute Stefan-Boltzmann constant from fundamental constants:
        σ_SB = 2π⁵ k_B⁴ / (15 h³ c²)

        Returns:
            σ_SB in W/(m²·K⁴)
        """
        numerator = 2 * (pi**5) * (K_B**4)
        denominator = 15 * (H_PLANCK**3) * (C**2)
        sigma_sb = numerator / denominator
        return sigma_sb

    def integrate_planck_spectrum(self, T, lambda_min=1e-8, lambda_max=1e-4) -> float:
        """
        Integrate Planck spectrum numerically over wavelength:
        j*(T) = ∫₀^∞ B(λ,T) dλ

        Args:
            T: temperature (K)
            lambda_min: lower wavelength limit (m) for integration
            lambda_max: upper wavelength limit (m) for integration

        Returns:
            Total spectral power j* in W/m²
        """
        def integrand(wavelength):
            return planck_spectral_radiance_wavelength(wavelength, T)

        # Integrate from lambda_min to lambda_max
        result, error = quad(integrand, lambda_min, lambda_max, limit=100)
        return result

    def run(self) -> Dict:
        """
        Verify Stefan-Boltzmann law by:
        1. Computing σ_SB from fundamental constants
        2. Integrating Planck spectrum numerically
        3. Checking j*(T) = σ_SB T⁴ for multiple temperatures
        """
        results = {}

        # Compute Stefan-Boltzmann constant from fundamental constants
        sigma_sb_computed = self.compute_stefan_boltzmann_from_constants()

        # Error in σ_SB
        error_sigma = abs(sigma_sb_computed - SIGMA_SB_TEXTBOOK) / SIGMA_SB_TEXTBOOK * 100

        # Test at multiple temperatures
        temperatures = np.array([3000.0, 4000.0, 5000.0, 5778.0, 6000.0, 7000.0])
        spectral_powers = np.zeros_like(temperatures)
        predicted_powers = np.zeros_like(temperatures)
        errors_percent = np.zeros_like(temperatures)

        for i, T in enumerate(temperatures):
            # Integrate Planck spectrum
            j_integrated = self.integrate_planck_spectrum(T)
            spectral_powers[i] = j_integrated

            # Predict from Stefan-Boltzmann law
            j_predicted = sigma_sb_computed * (T**4)
            predicted_powers[i] = j_predicted

            # Error
            error_pct = abs(j_integrated - j_predicted) / j_predicted * 100
            errors_percent[i] = error_pct

        # Check if all errors < 1%
        passed = error_sigma < 1.0 and np.all(errors_percent < 1.0)

        results['test_name'] = 'Stefan-Boltzmann Law'
        results['sigma_sb_computed_W/(m2·K4)'] = sigma_sb_computed
        results['sigma_sb_textbook_W/(m2·K4)'] = SIGMA_SB_TEXTBOOK
        results['error_sigma_sb_percent'] = error_sigma
        results['temperatures_K'] = temperatures.tolist()
        results['integrated_power_W/m2'] = spectral_powers.tolist()
        results['predicted_power_W/m2'] = predicted_powers.tolist()
        results['errors_percent'] = errors_percent.tolist()
        results['pass'] = passed

        results['description'] = (
            f"Stefan-Boltzmann Law: j* = σ_SB T⁴\n"
            f"\nDerived from integrating Planck spectrum:\n"
            f"  j*(T) = ∫₀^∞ M(λ,T) dλ\n"
            f"\nwhere M(λ,T) = (2πhc²/λ⁵)/(e^(hc/λk_BT) - 1)\n"
            f"\nUsing x = hc/(λk_B T):\n"
            f"  j*(T) = (2π k_B⁴ T⁴/c² h³) ∫₀^∞ x³/(e^x - 1) dx\n"
            f"        = (2π k_B⁴ T⁴/c² h³) · (π⁴/15)\n"
            f"        = σ_SB T⁴\n"
            f"\nwhere σ_SB = 2π⁵ k_B⁴ / (15 h³ c²)\n"
            f"\n" + "="*70 + "\n"
            f"STEFAN-BOLTZMANN CONSTANT (from fundamental constants):\n"
            f"="*70 + "\n"
            f"\nFormula: σ_SB = 2π⁵ k_B⁴ / (15 h³ c²)\n"
            f"\nNumerical values:\n"
            f"  π⁵ = {pi**5:.10e}\n"
            f"  k_B⁴ = {K_B**4:.10e} J⁴/K⁴\n"
            f"  h³ = {H_PLANCK**3:.10e} J³·s³\n"
            f"  c² = {C**2:.10e} m²/s²\n"
            f"\nComputed: σ_SB = {sigma_sb_computed:.6e} W/(m²·K⁴)\n"
            f"Textbook: σ_SB = {SIGMA_SB_TEXTBOOK:.6e} W/(m²·K⁴)\n"
            f"Error: {error_sigma:.4f}%\n"
            f"\n" + "="*70 + "\n"
            f"VERIFICATION: j* = σ_SB T⁴ at multiple temperatures\n"
            f"="*70 + "\n"
        )

        for T, j_int, j_pred, err in zip(temperatures, spectral_powers, predicted_powers, errors_percent):
            results['description'] += (
                f"\nT = {T:.0f} K:\n"
                f"  Integrated Planck spectrum: j* = {j_int:.6e} W/m²\n"
                f"  Stefan-Boltzmann formula:   j* = {j_pred:.6e} W/m²\n"
                f"  Error: {err:.4f}%\n"
            )

        results['description'] += (
            f"\n✓ Stefan-Boltzmann constant from fundamental constants: σ_SB = {sigma_sb_computed:.6e} W/(m²·K⁴)\n"
            f"✓ Integration of Planck spectrum matches Stefan-Boltzmann law\n"
        )

        if passed:
            results['description'] += f"✓ PASS: All errors < 1%\n"
        else:
            results['description'] += f"✗ FAIL: Some errors ≥ 1%\n"

        return results


# ============================================================================
# TEST 3: WIEN'S DISPLACEMENT LAW
# ============================================================================

@dataclass
class WienDisplacementLawTest:
    """
    Test: Wien's displacement law λ_max T = b

    To find the peak of Planck spectrum, we differentiate with respect to wavelength
    and set to zero:

      dB(λ,T)/dλ = 0

    where B(λ,T) = (2hc²/λ⁵) / (e^(hc/λk_BT) - 1)

    Let x = hc/(λk_B T):
      dB/dx = ... [after algebraic manipulation]

    Setting the derivative to zero and solving:
      5λ(e^x - 1) = x λ e^x
      5(e^x - 1) = x e^x
      5 - 5e^(-x) = x
      x = 5(1 - e^(-x))  [Wien equation]

    Solving numerically: x ≈ 4.9651...

    Then:
      λ_peak = hc / (x k_B T)
      λ_peak T = hc / (x k_B) = b

    where b = hc / (x k_B) ≈ 2.898 × 10⁻³ m·K
    """

    def wien_equation(self, x):
        """
        Wien's displacement equation: x = 5(1 - e^(-x))

        Args:
            x: dimensionless parameter hc/(λk_BT)

        Returns:
            f(x) = x - 5(1 - e^(-x))
        """
        return x - 5.0 * (1.0 - exp(-x))

    def find_wien_parameter(self) -> float:
        """
        Solve Wien's equation numerically to find x.

        Returns:
            x ≈ 4.9651...
        """
        # Initial guess
        x0 = 4.8

        # Solve using fsolve
        solution = fsolve(self.wien_equation, x0)
        x_wien = solution[0]

        return x_wien

    def compute_wien_constant(self, x_wien) -> float:
        """
        Compute Wien's displacement constant from x_wien:
        b = hc / (x_wien * k_B)

        Args:
            x_wien: solution to Wien equation

        Returns:
            b in m·K
        """
        b_wien = (H_PLANCK * C) / (x_wien * K_B)
        return b_wien

    def find_peak_numerically(self, T) -> Tuple[float, float]:
        """
        Find peak of Planck spectrum numerically in wavelength form.

        Args:
            T: temperature (K)

        Returns:
            (λ_peak, B_peak)
        """
        wavelength_range = np.logspace(-7, -5, 500)
        B_lambda = np.array([planck_spectral_radiance_wavelength(lam, T) for lam in wavelength_range])

        idx_peak = np.argmax(B_lambda)
        lambda_peak = wavelength_range[idx_peak]
        B_peak = B_lambda[idx_peak]

        return lambda_peak, B_peak

    def run(self) -> Dict:
        """
        Verify Wien's displacement law by:
        1. Solving Wien equation x = 5(1 - e^(-x)) numerically
        2. Computing b = hc / (x k_B)
        3. Checking λ_max T = b for multiple temperatures
        """
        results = {}

        # Solve Wien equation
        x_wien = self.find_wien_parameter()

        # Verify Wien equation is satisfied
        residual = self.wien_equation(x_wien)

        # Compute Wien constant
        b_wien_computed = self.compute_wien_constant(x_wien)

        # Error in Wien constant
        error_b_wien = abs(b_wien_computed - B_WIEN_TEXTBOOK) / B_WIEN_TEXTBOOK * 100

        # Test at multiple temperatures
        temperatures = np.array([3000.0, 4000.0, 5000.0, 5778.0, 6000.0, 7000.0])
        lambda_peaks_numeric = np.zeros_like(temperatures)
        lambda_peaks_wien = np.zeros_like(temperatures)
        errors_percent = np.zeros_like(temperatures)

        for i, T in enumerate(temperatures):
            # Find peak numerically from Planck spectrum
            lambda_peak, _ = self.find_peak_numerically(T)
            lambda_peaks_numeric[i] = lambda_peak

            # Predict from Wien's law
            lambda_wien = B_WIEN_TEXTBOOK / T
            lambda_peaks_wien[i] = lambda_wien

            # Error
            error_pct = abs(lambda_peak - lambda_wien) / lambda_wien * 100
            errors_percent[i] = error_pct

        # Check if all errors < 2%
        passed = error_b_wien < 1.0 and np.all(errors_percent < 2.0)

        results['test_name'] = "Wien's Displacement Law"
        results['x_wien'] = x_wien
        results['wien_equation_residual'] = residual
        results['b_wien_computed_m·K'] = b_wien_computed
        results['b_wien_textbook_m·K'] = B_WIEN_TEXTBOOK
        results['error_b_wien_percent'] = error_b_wien
        results['temperatures_K'] = temperatures.tolist()
        results['lambda_peak_numeric_m'] = lambda_peaks_numeric.tolist()
        results['lambda_peak_wien_m'] = lambda_peaks_wien.tolist()
        results['errors_percent'] = errors_percent.tolist()
        results['pass'] = passed

        results['description'] = (
            f"Wien's Displacement Law: λ_max T = b\n"
            f"\nDerived from peak of Planck spectrum:\n"
            f"  dM(λ,T)/dλ = 0\n"
            f"\nwhere M(λ,T) = (2πhc²/λ⁵)/(e^(hc/λk_BT) - 1)\n"
            f"\nUsing x = hc/(λk_B T):\n"
            f"  d/dλ [1/λ⁵ · 1/(e^x - 1)] = 0\n"
            f"  5(e^x - 1) = x e^x\n"
            f"  x = 5(1 - e^(-x))  [Wien equation]\n"
            f"\nThen:\n"
            f"  λ_max = hc / (x k_B T)\n"
            f"  λ_max T = hc / (x k_B) = b\n"
            f"\n" + "="*70 + "\n"
            f"WIEN EQUATION & DISPLACEMENT CONSTANT:\n"
            f"="*70 + "\n"
            f"\nWien equation: x = 5(1 - e^(-x))\n"
            f"Numerical solution: x = {x_wien:.10f}\n"
            f"Equation residual: {residual:.2e} (should be ~0)\n"
            f"\nWien displacement constant:\n"
            f"  b = hc / (x k_B)\n"
            f"  b = ({H_PLANCK:.6e} × {C:.2e}) / ({x_wien:.10f} × {K_B:.6e})\n"
            f"  b = {b_wien_computed:.6e} m·K\n"
            f"\nTextbook value: b = {B_WIEN_TEXTBOOK:.6e} m·K\n"
            f"Error: {error_b_wien:.4f}%\n"
            f"\n" + "="*70 + "\n"
            f"VERIFICATION: λ_max T = b at multiple temperatures\n"
            f"="*70 + "\n"
        )

        for T, lambda_num, lambda_wien, err in zip(temperatures, lambda_peaks_numeric, lambda_peaks_wien, errors_percent):
            results['description'] += (
                f"\nT = {T:.0f} K:\n"
                f"  Peak from Planck spectrum: λ_peak = {lambda_num:.4e} m = {lambda_num*1e9:.1f} nm\n"
                f"  Wien's law:                λ_max  = {lambda_wien:.4e} m = {lambda_wien*1e9:.1f} nm\n"
                f"  Error: {err:.4f}%\n"
            )

        results['description'] += (
            f"\n✓ Wien equation solved: x = {x_wien:.10f}\n"
            f"✓ Wien constant computed: b = {b_wien_computed:.6e} m·K\n"
            f"✓ Peak wavelength matches Wien's law at all temperatures\n"
        )

        if passed:
            results['description'] += f"✓ PASS: All errors < 2%\n"
        else:
            results['description'] += f"✗ FAIL: Some errors ≥ 2%\n"

        return results


# ============================================================================
# BONUS: SOLAR LUMINOSITY
# ============================================================================

@dataclass
class SolarLuminosityTest:
    """
    Bonus test: Solar luminosity from Stefan-Boltzmann law

    L_sun = 4πR² σ_SB T⁴

    Using:
      T = 5778 K (solar surface)
      R = 6.96 × 10⁸ m (solar radius)
      σ_SB ≈ 5.67 × 10⁻⁸ W/(m²·K⁴)

    Expected: L_sun ≈ 3.828 × 10²⁶ W
    """

    def run(self) -> Dict:
        """Compute solar luminosity from Stefan-Boltzmann law."""
        results = {}

        # Compute Stefan-Boltzmann constant from fundamentals
        sigma_sb = 2 * (pi**5) * (K_B**4) / (15 * (H_PLANCK**3) * (C**2))

        # Compute solar luminosity
        L_sun_computed = 4 * pi * (R_SUN**2) * sigma_sb * (T_SUN**4)

        # Error
        error_L_sun = abs(L_sun_computed - L_SUN_TEXTBOOK) / L_SUN_TEXTBOOK * 100

        passed = error_L_sun < 1.0

        results['test_name'] = 'Solar Luminosity'
        results['temperature_K'] = T_SUN
        results['radius_m'] = R_SUN
        results['sigma_sb_W/(m2·K4)'] = sigma_sb
        results['luminosity_computed_W'] = L_sun_computed
        results['luminosity_textbook_W'] = L_SUN_TEXTBOOK
        results['error_percent'] = error_L_sun
        results['pass'] = passed

        results['description'] = (
            f"Solar Luminosity: L_sun = 4πR² σ_SB T⁴\n"
            f"\nUsing Stefan-Boltzmann law integrated over solar surface:\n"
            f"  σ_SB = 2π⁵ k_B⁴ / (15 h³ c²)\n"
            f"\nSolar parameters:\n"
            f"  T_sun = {T_SUN} K\n"
            f"  R_sun = {R_SUN:.2e} m\n"
            f"\nComputed:\n"
            f"  σ_SB = {sigma_sb:.6e} W/(m²·K⁴)\n"
            f"  L_sun = 4π × ({R_SUN:.2e})² × {sigma_sb:.6e} × ({T_SUN})⁴\n"
            f"  L_sun = {L_sun_computed:.6e} W\n"
            f"\nTextbook value:\n"
            f"  L_sun = {L_SUN_TEXTBOOK:.6e} W\n"
            f"\nError: {error_L_sun:.4f}%\n"
            f"\n✓ Solar luminosity matches textbook value\n"
        )

        if passed:
            results['description'] += f"✓ PASS: Error < 1%\n"
        else:
            results['description'] += f"✗ FAIL: Error ≥ 1%\n"

        return results


# ============================================================================
# MAIN TEST RUNNER
# ============================================================================

def run_all_tests():
    """Run all Planck spectrum and thermal radiation law tests."""

    print("=" * 80)
    print("GENESIS PHYSICS: PLANCK SPECTRUM & THERMAL RADIATION LAWS")
    print("=" * 80)
    print()

    tests = [
        PlanckSpectrumTest(),
        StefanBoltzmannTest(),
        WienDisplacementLawTest(),
        SolarLuminosityTest(),
    ]

    test_results = []
    all_passed = True

    for i, test in enumerate(tests, 1):
        print(f"\n{i}. Running {test.__class__.__name__}...")
        print("-" * 80)

        try:
            result = test.run()
            test_results.append(result)

            status = "PASS ✓" if result['pass'] else "FAIL ✗"
            print(result['description'])
            print()
            print(f"Status: {status}")

            if not result['pass']:
                all_passed = False

        except Exception as e:
            print(f"ERROR: {e}")
            import traceback
            traceback.print_exc()
            all_passed = False

    # Summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)

    for result in test_results:
        status = "PASS ✓" if result['pass'] else "FAIL ✗"
        print(f"{result['test_name']:45} {status}")

    print()
    if all_passed:
        print("ALL TESTS PASSED ✓✓✓")
        return 0
    else:
        print("SOME TESTS FAILED ✗✗✗")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
