"""
Firmament Vibrations Spectrum Calculator
========================================

Computes eigenfrequencies and mode spectrum for the Genesis Physics membrane.

Solves the Firmament membrane wave equation:
  ρ ∂²u/∂t² = σ ∇²u + boundary corrections

Where:
  - σ = Firmament tension (6.0e98 kg/(m·s²))
  - ρ = Firmament membrane surface density (6.7e81 kg/m³)
  - ξ_A = Waters Above coherence length (3.0e26 m)
  - η_B = Waters Below coherence length (1.3e-15 m)

Computes:
  - Eigenfrequencies ω_n
  - Associated mass spectrum m_n = ℏω_n/c²
  - Comparison with observed particle masses
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from scipy.special import jn_zeros, jn
from typing import Tuple, List
import os

# Setup output directory relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Physical constants (SI)
HBAR = 1.055e-34        # J·s
C = 3.0e8               # m/s
M_PLANCK = 2.176e-8     # kg

# Membrane parameters
SIGMA = 6.0e98          # kg/(m·s²)  (tension)
MU = 6.7e81             # kg/m³  (surface density)
XI_A = 3.0e26           # m      (Waters Above scale)
ETA_B = 1.3e-15         # m      (Waters Below scale)

# Wave speed: v = sqrt(σ/μ)
WAVE_SPEED = np.sqrt(SIGMA / MU)

# Dimensionless parameter: wave speed / c
WAVE_SPEED_RATIO = WAVE_SPEED / C


class MembraneModeAnalyzer:
    """Analyzes vibration modes of the Genesis Physics membrane"""

    def __init__(self, domain_size: float = 1.0, n_points: int = 256):
        """
        Initialize membrane analyzer.

        Args:
            domain_size: Size of computational domain (dimensionless)
            n_points: Number of grid points
        """
        self.domain_size = domain_size
        self.n_points = n_points
        self.dx = domain_size / (n_points - 1)
        self.x = np.linspace(0, domain_size, n_points)

        # Eigenvalues and eigenvectors (will be computed)
        self.eigenvalues = None
        self.eigenvectors = None
        self.frequencies = None
        self.masses = None

    def _build_laplacian_1d(self):
        """Build 1D Laplacian matrix with Dirichlet BC (fixed ends)"""
        # d²/dx² with u(0) = u(L) = 0
        main_diag = -2.0 * np.ones(self.n_points)
        off_diag = np.ones(self.n_points - 1)

        laplacian = diags([main_diag, off_diag, off_diag],
                         [0, 1, -1],
                         shape=(self.n_points, self.n_points),
                         format='csr')
        laplacian /= self.dx**2

        return laplacian

    def _build_mass_matrix_1d(self):
        """Build 1D mass matrix with mu on diagonal"""
        mass = diags([np.ones(self.n_points)],
                    [0],
                    shape=(self.n_points, self.n_points),
                    format='csr')
        return mass

    def compute_eigenfrequencies_1d(self, n_modes: int = 10):
        """
        Compute 1D eigenfrequencies using FEM/FDM.

        For Firmament membrane wave equation: μ ∂²u/∂t² = σ ∇²u
        Eigenvalue problem: λ = ω²

        Solves: σ ∇²φ = -ω² μ φ
        """
        print(f"Computing 1D eigenfrequencies ({n_modes} modes)...")

        laplacian = self._build_laplacian_1d()
        mass = self._build_mass_matrix_1d()

        # Scale: we need -∇² (negative Laplacian)
        # Generalized eigenvalue problem: K φ = λ M φ
        # where K = -σ ∇² and M = μ

        # For our case: -σ/μ ∇² φ = ω² φ
        K = -SIGMA / MU * laplacian

        try:
            # Compute n_modes smallest eigenvalues
            evals, evecs = eigsh(K, k=n_modes - 1, which='SM', mode='normal')
            evals = np.abs(evals)  # Ensure positive
        except Exception as e:
            print(f"Warning: eigsh failed, using alternative method: {e}")
            # Fallback: analytical solution for 1D string
            evals = self._analytical_eigenvalues_1d(n_modes)
            evecs = None

        # Convert to frequencies: ω = sqrt(λ)
        self.eigenvalues = evals
        self.frequencies = np.sqrt(np.maximum(evals, 0))

        # Compute associated masses: m = ℏ ω / c²
        self.masses = HBAR * self.frequencies / (C**2)

        print(f"  Computed {len(self.frequencies)} eigenfrequencies")
        for i, (freq, mass) in enumerate(zip(self.frequencies[:5], self.masses[:5])):
            print(f"    Mode {i+1}: ω = {freq:.6e} rad/s, m = {mass:.6e} kg")

        return self.frequencies, self.masses

    def _analytical_eigenvalues_1d(self, n_modes: int) -> np.ndarray:
        """
        Analytical solution for 1D string with fixed ends.

        ω_n = (n π / L) * v  where v = sqrt(σ/μ)
        """
        print("  Using analytical solution for 1D string...")
        L = self.domain_size
        v = np.sqrt(SIGMA / MU)

        n = np.arange(1, n_modes + 1)
        omega = (n * np.pi / L) * v

        return omega

    def analytical_spectrum_1d(self, n_modes: int = 20) -> Tuple[np.ndarray, np.ndarray]:
        """Get analytical spectrum for comparison"""
        omega = self._analytical_eigenvalues_1d(n_modes)
        masses = HBAR * omega / (C**2)
        return omega, masses

    def compute_circular_membrane_modes(self, n_modes: int = 10):
        """
        Compute eigenfrequencies for a circular membrane.

        For circular membrane with fixed edge:
        ω_{n,m} = (λ_{n,m} / a)² * sqrt(σ/ρ)

        where λ_{n,m} are zeros of Bessel function J_n
        and a is the radius.
        """
        print(f"Computing circular Firmament modes ({n_modes} modes)...")

        a = self.domain_size  # Radius
        v = np.sqrt(SIGMA / MU)  # Wave speed

        modes = []
        frequencies = []
        masses = []

        # Collect modes (n, m) ordered by frequency
        for n in range(0, 4):  # Radial order
            zeros = jn_zeros(n, 4)  # Get zeros of J_n
            for m, zero in enumerate(zeros[:3]):  # Azimuthal order
                omega = (zero / a)**2 * v
                frequencies.append(omega)
                mass = HBAR * omega / (C**2)
                masses.append(mass)
                modes.append((n, m, zero))

        # Sort by frequency
        sorted_idx = np.argsort(frequencies)
        frequencies = np.array(frequencies)[sorted_idx]
        masses = np.array(masses)[sorted_idx]
        modes = [modes[i] for i in sorted_idx]

        self.frequencies = frequencies[:n_modes]
        self.masses = masses[:n_modes]

        print(f"  Computed {len(self.frequencies)} circular Firmament modes")
        for i, (freq, mass) in enumerate(zip(self.frequencies[:5], self.masses[:5])):
            print(f"    Mode {i+1}: ω = {freq:.6e} rad/s, m = {mass:.6e} kg")

        return self.frequencies, self.masses

    def compare_with_particles(self):
        """
        Compare predicted mass spectrum with known particle masses.

        Returns comparison table.
        """
        if self.masses is None:
            print("No mass spectrum computed yet!")
            return None

        # Known particle masses (kg)
        particles = {
            'electron': 9.109e-31,
            'muon': 1.883e-28,
            'tau': 3.167e-27,
            'up quark': 2.2e-30,
            'down quark': 4.7e-30,
            'charm quark': 2.4e-27,
            'Higgs': 2.176e-25,
            'W boson': 1.433e-25,
            'Z boson': 1.526e-25,
        }

        print("\nComparison with Known Particles:")
        print("-" * 80)
        print(f"{'Particle':<20} {'Mass (kg)':<20} {'Predicted Mode':<20} {'Ratio':<15}")
        print("-" * 80)

        for name, mass in particles.items():
            # Find closest predicted mode
            idx = np.argmin(np.abs(self.masses - mass))
            predicted = self.masses[idx]
            ratio = predicted / mass

            print(f"{name:<20} {mass:<20.6e} {predicted:<20.6e} {ratio:<15.6f}")

        return particles

    def plot_mass_spectrum(self, filename: str = "mass_spectrum.png"):
        """Plot predicted mass spectrum"""
        if self.masses is None:
            print("No masses computed yet!")
            return

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # Linear scale
        n = np.arange(1, len(self.masses) + 1)
        ax1.semilogy(n, self.masses, 'bo-', linewidth=2, markersize=8)
        ax1.set_xlabel('Mode Number (n)', fontsize=12)
        ax1.set_ylabel('Mass (kg)', fontsize=12)
        ax1.set_title('Mass Spectrum: m_n = ℏω_n/c²', fontsize=14)
        ax1.grid(True, which='both', alpha=0.3)

        # Frequency scale
        ax2.semilogy(n, self.frequencies, 'ro-', linewidth=2, markersize=8)
        ax2.set_xlabel('Mode Number (n)', fontsize=12)
        ax2.set_ylabel('Frequency (rad/s)', fontsize=12)
        ax2.set_title('Eigenfrequency Spectrum: ω_n', fontsize=14)
        ax2.grid(True, which='both', alpha=0.3)

        plt.tight_layout()
        filepath = os.path.join(OUTPUT_DIR, filename)
        plt.savefig(filepath, dpi=150)
        print(f"Saved spectrum plot to {filepath}")
        plt.close()

    def plot_comparison(self, filename: str = "spectrum_comparison.png"):
        """Plot predicted vs known particle masses"""
        if self.masses is None:
            print("No masses computed yet!")
            return

        particles = {
            'electron': 9.109e-31,
            'muon': 1.883e-28,
            'tau': 3.167e-27,
            'Higgs': 2.176e-25,
            'W boson': 1.433e-25,
            'Z boson': 1.526e-25,
        }

        fig, ax = plt.subplots(figsize=(12, 6))

        # Plot predicted spectrum
        n = np.arange(1, len(self.masses) + 1)
        ax.semilogy(n, self.masses, 'bo-', linewidth=2, markersize=8, label='Predicted (Genesis Physics)', zorder=3)

        # Overlay known particles
        for name, mass in particles.items():
            ax.axhline(mass, linestyle='--', alpha=0.5, linewidth=1.5, label=name)

        ax.set_xlabel('Mode Number (n)', fontsize=12)
        ax.set_ylabel('Mass (kg)', fontsize=12)
        ax.set_title('Predicted Particle Spectrum vs Known Particles', fontsize=14)
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, which='both', alpha=0.3)

        plt.tight_layout()
        filepath = os.path.join(OUTPUT_DIR, filename)
        plt.savefig(filepath, dpi=150)
        print(f"Saved comparison plot to {filepath}")
        plt.close()

    def print_summary(self):
        """Print summary statistics"""
        if self.frequencies is None or self.masses is None:
            print("No spectrum computed!")
            return

        print("\n" + "="*70)
        print("Firmament membrane VIBRATION SPECTRUM SUMMARY")
        print("="*70)

        print(f"\nPhysical Parameters:")
        print(f"  Firmament tension (σ):        {SIGMA:.3e} kg/(m·s²)")
        print(f"  Membrane density (μ):        {MU:.3e} kg/m³")
        print(f"  Wave speed (v = √(σ/μ)):     {WAVE_SPEED:.3e} m/s")
        print(f"  Wave speed ratio (v/c):      {WAVE_SPEED_RATIO:.6e}")

        print(f"\nEigenfrequency Spectrum (first 10 modes):")
        print(f"{'Mode':<6} {'ω_n (rad/s)':<20} {'m_n (kg)':<20} {'Log10(m_n)':<15}")
        print("-" * 70)

        for i in range(min(10, len(self.frequencies))):
            log_m = np.log10(self.masses[i]) if self.masses[i] > 0 else -np.inf
            print(f"{i+1:<6} {self.frequencies[i]:<20.6e} {self.masses[i]:<20.6e} {log_m:<15.2f}")

        print(f"\nSpectrum Properties:")
        print(f"  Frequency range:  {np.min(self.frequencies):.6e} to {np.max(self.frequencies):.6e} rad/s")
        print(f"  Mass range:       {np.min(self.masses):.6e} to {np.max(self.masses):.6e} kg")
        print(f"  Mode spacing (Δm): ~{np.mean(np.diff(self.masses)):.6e} kg")

        print("\n" + "="*70)


def run_string_spectrum():
    """Compute spectrum for 1D string (membrane edge)"""
    print("\n" + "="*70)
    print("TEST 1: 1D String Eigenfrequencies")
    print("="*70)

    analyzer = MembraneModeAnalyzer(domain_size=1.0, n_points=512)
    frequencies, masses = analyzer.compute_eigenfrequencies_1d(n_modes=15)

    analyzer.print_summary()
    analyzer.plot_mass_spectrum("spectrum_1d_string.png")

    return analyzer


def run_circular_membrane():
    """Compute spectrum for circular membrane"""
    print("\n" + "="*70)
    print("TEST 2: Circular Membrane Eigenfrequencies")
    print("="*70)

    analyzer = MembraneModeAnalyzer(domain_size=1.0)
    frequencies, masses = analyzer.compute_circular_membrane_modes(n_modes=20)

    analyzer.print_summary()
    analyzer.compare_with_particles()
    analyzer.plot_mass_spectrum("spectrum_circular.png")
    analyzer.plot_comparison("spectrum_vs_particles.png")

    return analyzer


def compare_analytical_numerical():
    """Compare analytical and numerical solutions"""
    print("\n" + "="*70)
    print("TEST 3: Analytical vs Numerical Comparison")
    print("="*70)

    analyzer = MembraneModeAnalyzer(domain_size=1.0, n_points=512)

    # Analytical solution
    omega_analytical, m_analytical = analyzer.analytical_spectrum_1d(n_modes=10)

    # Numerical solution (if it converges)
    try:
        omega_numerical, m_numerical = analyzer.compute_eigenfrequencies_1d(n_modes=10)
    except:
        print("Warning: numerical solution failed, using only analytical")
        omega_numerical = omega_analytical
        m_numerical = m_analytical

    print("\nComparison Table:")
    print(f"{'Mode':<6} {'ω (analytical)':<20} {'ω (numerical)':<20} {'Relative Error':<15}")
    print("-" * 70)

    for i in range(len(omega_analytical)):
        if i < len(omega_numerical):
            rel_err = np.abs(omega_analytical[i] - omega_numerical[i]) / omega_analytical[i]
            print(f"{i+1:<6} {omega_analytical[i]:<20.6e} {omega_numerical[i]:<20.6e} {rel_err:<15.6e}")
        else:
            print(f"{i+1:<6} {omega_analytical[i]:<20.6e} {'N/A':<20} {'N/A':<15}")

    # Plot comparison
    fig, ax = plt.subplots(figsize=(10, 6))

    n = np.arange(1, len(omega_analytical) + 1)
    ax.semilogy(n, omega_analytical, 'b-o', linewidth=2, markersize=8, label='Analytical')
    if len(omega_numerical) > 0:
        ax.semilogy(n[:len(omega_numerical)], omega_numerical, 'r--s', linewidth=2, markersize=6, label='Numerical')

    ax.set_xlabel('Mode Number (n)', fontsize=12)
    ax.set_ylabel('Frequency ω_n (rad/s)', fontsize=12)
    ax.set_title('Analytical vs Numerical Eigenfrequencies', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, which='both', alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "spectrum_comparison.png"), dpi=150)
    print("\nComparison plot saved.")
    plt.close()

    return analyzer


if __name__ == "__main__":
    print("Genesis Physics - Firmament Vibration Spectrum Calculator")
    print("="*70)

    # Run all analyses
    analyzer1 = run_string_spectrum()
    analyzer2 = run_circular_membrane()
    analyzer3 = compare_analytical_numerical()

    print("\n" + "="*70)
    print("Firmament vibration analysis complete!")
    print("="*70)
