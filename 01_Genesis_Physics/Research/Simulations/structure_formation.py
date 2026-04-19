"""
Structure Formation Simulator: Genesis Physics vs ΛCDM
=======================================================

Compares N-body structure formation in:
  1. Standard ΛCDM (gravity + dark energy + dark matter)
  2. Genesis Physics (gravity + Waters Above + Waters Below)

Key physics:
  - Waters Below (Ψ_B) acts as dark matter
  - Waters Above (Ψ_A) modifies dark energy
  - Coupling G_int between the two waters
  - Zone-dependent corrections to growth rates

Output:
  - Power spectrum P(k)
  - Density-contrast evolution
  - Halo mass function
  - Growth factor comparison
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.fft import fft, fftfreq
from typing import Tuple, List
import os

# Setup output directory relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Constants
G = 1.0                 # Normalized gravitational constant
C = 1.0                 # Normalized speed of light
HBAR = 1.0              # Normalized reduced Planck constant
RHO_MATTER_0 = 0.3      # Matter density parameter (Ω_m)
RHO_LAMBDA_0 = 0.7      # Dark energy density (Ω_Λ)
RHO_CRIT = 1.0          # Critical density (normalized)

# Genesis Physics parameters
ALPHA_A = 0.05          # Waters Above coupling strength
ALPHA_B = 0.1           # Waters Below coupling strength
G_INT = 0.01            # Inter-waters coupling

# Redshift range (1+z)
A_MIN = 0.3             # Scale factor minimum (high redshift)
A_MAX = 1.0             # Scale factor maximum (z=0, today)


class CosmologyModel:
    """Base cosmology model for structure formation"""

    def __init__(self, name: str = "Model"):
        self.name = name
        self.a_history = []
        self.k_history = []

    def hubble(self, a: float) -> float:
        """Hubble parameter H(a) in normalized units"""
        raise NotImplementedError

    def growth_rate(self, a: float, delta: float) -> float:
        """Growth rate of density contrast d(delta)/dt"""
        raise NotImplementedError

    def growth_factor(self, a_values: np.ndarray) -> np.ndarray:
        """Compute growth factor D+(a) by integration"""
        # Solve: d²D/da² + (2/a + H'/H²) dD/da - 3Ω_m/(2a⁵H²) D = 0
        # Initial condition: D(a_i) = a_i (matter-dominated)

        D_values = []
        dd_da_prev = 0.0
        D_prev = a_values[0]

        for i, a in enumerate(a_values):
            if i == 0:
                D_values.append(D_prev)
                continue

            da = a_values[i] - a_values[i-1]
            H = self.hubble(a)

            # RHS of growth equation
            d2d_da2 = -1.0 * (2.0/a + (H / da) / H) * dd_da_prev + 3.0*RHO_MATTER_0/(2*a**5 * H**2) * D_prev

            # Simple Euler step
            dd_da_new = dd_da_prev + d2d_da2 * da
            D_new = D_prev + dd_da_new * da

            D_values.append(D_new)
            D_prev = D_new
            dd_da_prev = dd_da_new

        return np.array(D_values)


class LambdaCDM(CosmologyModel):
    """Standard ΛCDM cosmology"""

    def __init__(self):
        super().__init__("ΛCDM")

    def hubble(self, a: float) -> float:
        """H(a) / H_0 = sqrt(Ω_m a⁻³ + Ω_Λ)"""
        return np.sqrt(RHO_MATTER_0 / a**3 + RHO_LAMBDA_0)

    def growth_rate(self, a: float, delta: float) -> float:
        """Perturbation growth in ΛCDM (linear)"""
        # d(lnδ)/dlna = d/dlna (growth factor D)
        H = self.hubble(a)
        return 1.0 / H / a * delta  # Simplified

    def power_spectrum(self, k: np.ndarray, a: float) -> np.ndarray:
        """Matter power spectrum P(k,a)"""
        # P(k,a) = P_0 * k * (D(a) / D(a=1))^2 * exp(-k²/k_c²)
        # with cutoff at nonlinear scales

        k_c = 0.5  # Cutoff wavenumber
        P_0 = 1.0

        # Growing mode (approximately linear)
        D = 1.0 / self.hubble(a)  # Approximation

        P = P_0 * k * (D**2) * np.exp(-(k / k_c)**2)
        return P


class GenesisPhysics(CosmologyModel):
    """Genesis Physics cosmology with Waters Above/Below"""

    def __init__(self):
        super().__init__("Genesis Physics")

    def hubble(self, a: float) -> float:
        """Modified Hubble parameter with Waters Above/Below"""
        # H(a) modified by Waters Above and Below contributions
        # H(a) = sqrt(Ω_m a⁻³ + Ω_Λ + Ω_A f_A(a) + Ω_B f_B(a))

        # Waters Above contribution (behaves like dark energy, positive pressure)
        omega_a = ALPHA_A / a**4  # Evolution with a⁻⁴ (radiation-like)

        # Waters Below contribution (behaves like dark matter, zero pressure)
        omega_b = ALPHA_B / a**3  # Evolution with a⁻³ (matter-like)

        H_sq = RHO_MATTER_0 / a**3 + RHO_LAMBDA_0 + omega_a + omega_b
        return np.sqrt(np.maximum(H_sq, 0.01))

    def growth_rate(self, a: float, delta: float) -> float:
        """Modified growth rate with Waters coupling"""
        H = self.hubble(a)

        # Standard ΛCDM growth
        growth_cdm = delta / H / a

        # Correction from Waters Below (enhances growth slightly)
        correction_b = G_INT * ALPHA_B / a**3 * delta

        # Correction from Waters Above (suppresses growth at late times)
        correction_a = -0.5 * ALPHA_A / a**4 * delta

        return growth_cdm + correction_b + correction_a

    def power_spectrum(self, k: np.ndarray, a: float) -> np.ndarray:
        """Modified power spectrum with Genesis Physics corrections"""
        k_c = 0.5
        P_0 = 1.0

        # Growth factor with Waters coupling
        H = self.hubble(a)
        D = 1.0 / H

        # Enhancement from Waters Below at large scales
        enhancement = 1.0 + 0.1 * ALPHA_B / a**3 * np.exp(-(k/0.1)**2)

        # Suppression from Waters Above at small scales
        suppression = 1.0 - 0.05 * ALPHA_A / a**4 * (1.0 - np.exp(-(k/1.0)**2))

        P = P_0 * k * (D**2) * np.exp(-(k/k_c)**2) * enhancement * suppression

        return P


class StructureFormationSimulator:
    """Simulate structure formation in different cosmologies"""

    def __init__(self):
        self.models = {
            'ΛCDM': LambdaCDM(),
            'GenesisPhysics': GenesisPhysics(),
        }

        self.k_values = np.logspace(-2, 1, 100)  # Wavenumbers
        self.a_values = np.linspace(A_MIN, A_MAX, 50)  # Scale factors

        self.results = {}

    def run_simulations(self):
        """Run structure formation for all models"""
        print("Running structure formation simulations...")

        for model_name, model in self.models.items():
            print(f"\n  Running {model_name}...")

            # Compute growth factor
            D = model.growth_factor(self.a_values)

            # Compute power spectra
            P_k = np.zeros((len(self.a_values), len(self.k_values)))
            for i, a in enumerate(self.a_values):
                P_k[i, :] = model.power_spectrum(self.k_values, a)

            self.results[model_name] = {
                'model': model,
                'D': D,
                'P_k': P_k,
                'k': self.k_values,
                'a': self.a_values,
            }

        print("\n  Simulations complete.")

    def compute_density_contrast(self) -> dict:
        """Compute density contrast evolution"""
        results = {}

        for model_name, data in self.results.items():
            # Convert growth factor to density contrast
            D = data['D']
            delta_lin = D / D[0] - 1.0  # Normalized to D(a_min)

            results[model_name] = delta_lin

        return results

    def compute_halo_mass_function(self, z: float = 0.0) -> dict:
        """
        Compute halo mass function dn/dM.

        Uses Press-Schechter formalism with cosmology-dependent sigma(M).
        """
        results = {}

        # Mass range
        M = np.logspace(10, 16, 100)  # Halo masses in solar masses

        # Redshift to scale factor
        a = 1.0 / (1.0 + z)

        for model_name, data in self.results.items():
            model = data['model']

            # Compute sigma(M) at redshift z
            # sigma(M) relates to power spectrum amplitude
            sigma_m = 0.1 * np.sqrt(np.mean(data['P_k'][-1, :])) * (M / 1e12)**(-0.3)

            # Press-Schechter halo mass function
            nu = 1.686 / sigma_m  # Overdensity parameter
            dn_dM = (1.0 / (sigma_m * np.sqrt(2*np.pi))) * np.exp(-nu**2 / 2.0) * (nu**2 - 1.0)

            results[model_name] = {
                'M': M,
                'sigma': sigma_m,
                'dn_dM': dn_dM,
            }

        return results

    def plot_growth_factor(self, filename: str = "growth_factor.png"):
        """Plot growth factor comparison"""
        fig, ax = plt.subplots(figsize=(11, 7))

        z_values = (1.0 / self.a_values) - 1.0

        for model_name, data in self.results.items():
            D = data['D']
            D_normalized = D / D[-1]  # Normalize to D(z=0)

            ax.plot(z_values, D_normalized, linewidth=2.5, marker='o', markersize=4,
                   label=model_name, alpha=0.8)

        ax.set_xlabel('Redshift z', fontsize=13)
        ax.set_ylabel('Growth Factor D(z) / D(0)', fontsize=13)
        ax.set_title('Structure Formation: Growth Factor Comparison', fontsize=14, fontweight='bold')
        ax.set_xscale('log')
        ax.legend(fontsize=12, loc='best')
        ax.grid(True, which='both', alpha=0.3)

        plt.tight_layout()
        filepath = os.path.join(OUTPUT_DIR, filename)
        plt.savefig(filepath, dpi=150)
        print(f"Saved growth factor plot to {filepath}")
        plt.close()

    def plot_power_spectrum(self, filename: str = "power_spectrum.png"):
        """Plot power spectrum at different redshifts"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Select representative redshifts
        z_selected = [10, 1, 0]  # High redshift to z=0
        colors = plt.cm.cool(np.linspace(0, 1, len(z_selected)))

        for i, z in enumerate(z_selected):
            a = 1.0 / (1.0 + z)
            a_idx = np.argmin(np.abs(self.a_values - a))

            for model_name, data in self.results.items():
                P_k = data['P_k'][a_idx, :]
                ax_idx = 0 if model_name == 'ΛCDM' else 1

                axes[ax_idx].loglog(data['k'], P_k, linewidth=2, color=colors[i],
                                   label=f'z={z}', marker='o', markersize=3, alpha=0.7)

        for i, model_name in enumerate(['ΛCDM', 'GenesisPhysics']):
            axes[i].set_xlabel('Wavenumber k (Mpc⁻¹)', fontsize=12)
            axes[i].set_ylabel('Power Spectrum P(k) (Mpc³)', fontsize=12)
            axes[i].set_title(f'{model_name} Power Spectrum Evolution', fontsize=13, fontweight='bold')
            axes[i].legend(fontsize=11)
            axes[i].grid(True, which='both', alpha=0.3)

        plt.tight_layout()
        filepath = os.path.join(OUTPUT_DIR, filename)
        plt.savefig(filepath, dpi=150)
        print(f"Saved power spectrum plot to {filepath}")
        plt.close()

    def plot_halo_mass_function(self, filename: str = "halo_mass_function.png"):
        """Plot halo mass function"""
        hmf = self.compute_halo_mass_function(z=0)

        fig, ax = plt.subplots(figsize=(11, 7))

        for model_name, data in hmf.items():
            ax.loglog(data['M'], np.abs(data['dn_dM']), linewidth=2.5, marker='s',
                     markersize=5, label=model_name, alpha=0.8)

        ax.set_xlabel('Halo Mass (M_sun)', fontsize=13)
        ax.set_ylabel('dn/dM (Mpc⁻³ dex⁻¹)', fontsize=13)
        ax.set_title('Halo Mass Function at z=0', fontsize=14, fontweight='bold')
        ax.legend(fontsize=12)
        ax.grid(True, which='both', alpha=0.3)

        plt.tight_layout()
        filepath = os.path.join(OUTPUT_DIR, filename)
        plt.savefig(filepath, dpi=150)
        print(f"Saved halo mass function plot to {filepath}")
        plt.close()

    def plot_density_contrast_evolution(self, filename: str = "density_contrast.png"):
        """Plot density contrast evolution"""
        fig, ax = plt.subplots(figsize=(11, 7))

        z_values = (1.0 / self.a_values) - 1.0
        deltas = self.compute_density_contrast()

        for model_name, delta in deltas.items():
            ax.plot(z_values, delta, linewidth=2.5, marker='o', markersize=4,
                   label=model_name, alpha=0.8)

        ax.set_xlabel('Redshift z', fontsize=13)
        ax.set_ylabel('Density Contrast δ(z)', fontsize=13)
        ax.set_title('Linear Density Contrast Evolution', fontsize=14, fontweight='bold')
        ax.set_xscale('log')
        ax.legend(fontsize=12)
        ax.grid(True, which='both', alpha=0.3)

        plt.tight_layout()
        filepath = os.path.join(OUTPUT_DIR, filename)
        plt.savefig(filepath, dpi=150)
        print(f"Saved density contrast plot to {filepath}")
        plt.close()

    def plot_spectrum_ratio(self, filename: str = "spectrum_ratio.png"):
        """Plot Genesis Physics to ΛCDM power spectrum ratio"""
        fig, ax = plt.subplots(figsize=(11, 7))

        gp_data = self.results['GenesisPhysics']
        lcdm_data = self.results['ΛCDM']

        z_selected = [0, 1, 5]  # Redshifts to plot
        colors = plt.cm.RdYlBu_r(np.linspace(0.2, 0.8, len(z_selected)))

        for i, z in enumerate(z_selected):
            a = 1.0 / (1.0 + z)
            a_idx = np.argmin(np.abs(self.a_values - a))

            P_gp = gp_data['P_k'][a_idx, :]
            P_lcdm = lcdm_data['P_k'][a_idx, :]

            ratio = P_gp / P_lcdm

            ax.semilogx(gp_data['k'], ratio, linewidth=2.5, color=colors[i],
                       label=f'z={z}', marker='o', markersize=4, alpha=0.8)

        ax.axhline(1.0, color='k', linestyle='--', linewidth=1, alpha=0.5)
        ax.set_xlabel('Wavenumber k (Mpc⁻¹)', fontsize=13)
        ax.set_ylabel('P(k, Genesis) / P(k, ΛCDM)', fontsize=13)
        ax.set_title('Power Spectrum Ratio: Genesis Physics vs ΛCDM', fontsize=14, fontweight='bold')
        ax.legend(fontsize=12)
        ax.grid(True, which='both', alpha=0.3)
        ax.set_ylim([0.5, 1.5])

        plt.tight_layout()
        filepath = os.path.join(OUTPUT_DIR, filename)
        plt.savefig(filepath, dpi=150)
        print(f"Saved spectrum ratio plot to {filepath}")
        plt.close()

    def print_summary(self):
        """Print summary statistics"""
        print("\n" + "="*70)
        print("STRUCTURE FORMATION SIMULATION SUMMARY")
        print("="*70)

        print(f"\nCosmological Parameters:")
        print(f"  Ω_m (matter):              {RHO_MATTER_0:.3f}")
        print(f"  Ω_Λ (dark energy):         {RHO_LAMBDA_0:.3f}")
        print(f"  Ω_Λ + Ω_m:                 {RHO_MATTER_0 + RHO_LAMBDA_0:.3f}")

        print(f"\nGenesis Physics Parameters:")
        print(f"  α_A (Waters Above):        {ALPHA_A:.6f}")
        print(f"  α_B (Waters Below):        {ALPHA_B:.6f}")
        print(f"  G_int (cross-coupling):    {G_INT:.6f}")

        print(f"\nSimulation Domain:")
        print(f"  Scale factors:             {A_MIN:.3f} to {A_MAX:.3f}")
        print(f"  Redshift range:            {(1/A_MIN - 1):.1f} to {(1/A_MAX - 1):.1f}")
        print(f"  Wavenumber range:          {np.min(self.k_values):.3e} to {np.max(self.k_values):.3e}")

        print(f"\nGrowth Factor at z=0:")
        for model_name, data in self.results.items():
            D_0 = data['D'][-1]
            D_init = data['D'][0]
            growth_ratio = D_0 / D_init
            print(f"  {model_name:<20} D(z=0)/D(z=10) = {growth_ratio:.6f}")

        print("\n" + "="*70)


def run_full_comparison():
    """Run complete structure formation comparison"""
    print("\n" + "="*70)
    print("STRUCTURE FORMATION: Genesis Physics vs ΛCDM")
    print("="*70)

    simulator = StructureFormationSimulator()
    simulator.run_simulations()
    simulator.print_summary()

    # Generate all plots
    simulator.plot_growth_factor("growth_factor.png")
    simulator.plot_power_spectrum("power_spectrum.png")
    simulator.plot_density_contrast_evolution("density_contrast.png")
    simulator.plot_halo_mass_function("halo_mass_function.png")
    simulator.plot_spectrum_ratio("spectrum_ratio.png")

    return simulator


if __name__ == "__main__":
    print("Genesis Physics - Structure Formation Simulator")
    print("="*70)

    simulator = run_full_comparison()

    print("\n" + "="*70)
    print("Structure formation simulation complete!")
    print("="*70)
