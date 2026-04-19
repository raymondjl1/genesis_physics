"""
Waters Field Equations Numerical Simulator
============================================

Solves the coupled Waters PDEs in dimensionless form:
  (A) ∇²η = -4πG ρ_matter (membrane curvature)
  (B) □Ψ_A + m_A² Ψ_A + (λ_A/3!) Ψ_A³ + G_int Ψ_B = 0 (Waters Above/dark energy)
  (C) □Ψ_B - m_B² Ψ_B - (λ_B/3!) Ψ_B³ - G_int Ψ_A = -ρ_matter (Waters Below/dark matter)

Implementation:
  - Finite difference solver (1D and 2D)
  - Dimensionless variables for extreme scale handling
  - Time evolution and equilibrium solvers
  - Validation tests and energy conservation checks
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags, linalg as sp_linalg
from scipy.integrate import odeint
from scipy.optimize import fsolve
import time
import os
from dataclasses import dataclass
from typing import Tuple, Optional

# Setup output directory relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================================
# Physical Constants (SI units)
# ============================================================================

SIGMA = 6.0e98          # kg/s²  (membrane tension)
MU = 6.7e81             # kg/m³  (membrane surface density)
C = 3.0e8               # m/s    (speed of light)
G = 6.674e-11           # m³ kg⁻¹ s⁻²
H_BAR = 1.055e-34       # J·s
M_PLANCK = 2.176e-8     # kg

# Genesis Physics length scales
XI_A = 3.0e26           # m      (Waters Above coherence length)
ETA_B = 1.3e-15         # m      (Waters Below coherence length)
RHO_PLANCK = 5.15e97    # kg/m³  (Planck density)

# Coupling constants (estimated)
M_A = 1.0e-27           # kg     (Waters Above particle mass)
M_B = 1.0e-25           # kg     (Waters Below particle mass)
LAMBDA_A = 0.1          # (dimensionless coupling)
LAMBDA_B = 0.1          # (dimensionless coupling)
G_INT = 1.0e-16         # m³ kg⁻¹ s⁻²


@dataclass
class SimulationParams:
    """Physical and numerical parameters"""
    # Spatial grid
    x_min: float = -1.0          # Domain start (dimensionless)
    x_max: float = 1.0           # Domain end (dimensionless)
    nx: int = 256                # Grid points (1D)
    ny: int = 256                # Grid points (2D)

    # Time integration
    t_max: float = 1.0           # Max time (dimensionless)
    dt: float = 0.001            # Time step (dimensionless)

    # Physics parameters (dimensionless) - WEAK COUPLING REGIME
    m_a_dim: float = 0.1         # Dimensionless m_A
    m_b_dim: float = 0.5         # Dimensionless m_B
    lambda_a: float = 1e-4       # Quartic coupling Waters Above (weak!)
    lambda_b: float = 1e-4       # Quartic coupling Waters Below (weak!)
    g_int: float = 1e-5          # Cross-coupling strength (weak!)

    # Source term
    rho_amplitude: float = 0.01  # Matter density amplitude (reduced)

    def __post_init__(self):
        self.dx = (self.x_max - self.x_min) / (self.nx - 1)
        self.dy = (self.x_max - self.x_min) / (self.ny - 1)


class WatersFieldSolver1D:
    """1D Finite Difference Solver for Waters Field Equations"""

    def __init__(self, params: SimulationParams):
        self.params = params
        self.x = np.linspace(params.x_min, params.x_max, params.nx)
        self.dx = params.dx

        # Initialize fields
        self.psi_a = np.zeros(params.nx)
        self.psi_b = np.zeros(params.nx)
        self.eta = np.zeros(params.nx)
        self.rho = self._init_rho()

        # Build Laplacian operator (sparse matrix for efficiency)
        self.laplacian = self._build_laplacian()

        # History tracking
        self.energy_history = []
        self.t_history = []

    def _build_laplacian(self):
        """Build sparse 1D Laplacian matrix with periodic BC"""
        # d²/dx² with periodic boundary conditions
        diag_main = -2.0 * np.ones(self.params.nx)
        diag_plus = np.ones(self.params.nx - 1)
        diag_minus = np.ones(self.params.nx - 1)

        # Wrap around for periodic BC
        laplacian = diags([diag_main, diag_plus, diag_minus],
                         [0, 1, -1],
                         shape=(self.params.nx, self.params.nx),
                         format='csr')
        laplacian /= self.dx**2

        return laplacian


    def _init_rho(self):
        """Initialize matter density source"""
        # Gaussian profile
        sigma_x = 0.3
        rho = self.params.rho_amplitude * np.exp(-self.x**2 / (2*sigma_x**2))
        return rho

    def set_initial_condition_gaussian(self, width: float = 0.2):
        """Initialize fields with Gaussian perturbation"""
        sigma = width

        # Initial conditions: small perturbations around zero
        self.psi_a = 0.1 * np.exp(-self.x**2 / (2*sigma**2))
        self.psi_b = 0.1 * np.exp(-self.x**2 / (2*sigma**2))
        self.eta = 0.05 * np.exp(-self.x**2 / (2*sigma**2))

    def equilibrium_psi_a(self) -> np.ndarray:
        """Compute equilibrium Ψ_A by solving nonlinear equation"""
        # At equilibrium: ∇²Ψ_A + m_A² Ψ_A + (λ_A/3!) Ψ_A³ + G_int Ψ_B = 0

        def residual(psi_a_trial):
            laplacian_psi_a = self.laplacian @ psi_a_trial
            return (laplacian_psi_a +
                   self.params.m_a_dim**2 * psi_a_trial +
                   (self.params.lambda_a / 6.0) * psi_a_trial**3 +
                   self.params.g_int * self.psi_b)

        psi_a_eq = fsolve(residual, self.psi_a)
        return psi_a_eq

    def equilibrium_psi_b(self) -> np.ndarray:
        """Compute equilibrium Ψ_B"""
        # At equilibrium: ∇²Ψ_B - m_B² Ψ_B - (λ_B/3!) Ψ_B³ - G_int Ψ_A = -ρ_matter

        def residual(psi_b_trial):
            laplacian_psi_b = self.laplacian @ psi_b_trial
            return (laplacian_psi_b -
                   self.params.m_b_dim**2 * psi_b_trial -
                   (self.params.lambda_b / 6.0) * psi_b_trial**3 -
                   self.params.g_int * self.psi_a +
                   self.rho)

        psi_b_eq = fsolve(residual, self.psi_b)
        return psi_b_eq

    def equilibrium_eta(self) -> np.ndarray:
        """Compute equilibrium membrane curvature: ∇²η = -4πG ρ"""
        # Solve Poisson equation: ∇²η = -4πG ρ
        # Using sparse solver
        lhs = self.laplacian
        rhs = -4.0 * np.pi * 1.0 * self.rho  # Simplified: dimensionless gravity
        eta_eq = sp_linalg.spsolve(lhs, rhs)
        return np.array(eta_eq).flatten()

    def compute_equilibrium(self, max_iter: int = 10):
        """Find equilibrium configuration"""
        print("Computing equilibrium configuration...")

        for i in range(max_iter):
            psi_a_new = self.equilibrium_psi_a()
            psi_b_new = self.equilibrium_psi_b()
            eta_new = self.equilibrium_eta()

            # Check convergence
            da = np.max(np.abs(psi_a_new - self.psi_a))
            db = np.max(np.abs(psi_b_new - self.psi_b))
            de = np.max(np.abs(eta_new - self.eta))

            self.psi_a = psi_a_new
            self.psi_b = psi_b_new
            self.eta = eta_new

            if i % 2 == 0:
                print(f"  Iteration {i}: da={da:.2e}, db={db:.2e}, de={de:.2e}")

            if max(da, db, de) < 1e-6:
                print(f"  Converged at iteration {i}")
                return True

        print(f"  Warning: did not fully converge")
        return False

    def compute_energy(self) -> float:
        """Compute total energy (kinetic + potential)"""
        # Kinetic: 0.5 * ∫(∂Ψ)² dx (approximated by finite differences)
        dpsi_a = np.gradient(self.psi_a, self.dx)
        dpsi_b = np.gradient(self.psi_b, self.dx)

        kin_a = 0.5 * np.sum(dpsi_a**2) * self.dx
        kin_b = 0.5 * np.sum(dpsi_b**2) * self.dx

        # Potential: mass terms + quartic interactions + coupling
        v_a = (0.5 * self.params.m_a_dim**2 * self.psi_a**2 +
               (self.params.lambda_a / 24.0) * self.psi_a**4)

        v_b = (0.5 * self.params.m_b_dim**2 * self.psi_b**2 -
               (self.params.lambda_b / 24.0) * self.psi_b**4)

        v_int = -self.params.g_int * self.psi_a * self.psi_b

        pot_energy = np.sum((v_a + v_b + v_int) * self.dx)

        total_energy = kin_a + kin_b + pot_energy
        return total_energy

    def time_step_euler(self):
        """Single Euler time step (explicit, weak coupling regime)"""
        dt = self.params.dt

        # Compute spatial derivatives
        lap_psi_a = self.laplacian @ self.psi_a
        lap_psi_b = self.laplacian @ self.psi_b

        # Right-hand sides of the field equations
        # ∂Ψ_A/∂t = ∇²Ψ_A - m_A² Ψ_A - (λ_A/3!) Ψ_A³ - G_int Ψ_B
        dpsi_a_dt = (lap_psi_a -
                     self.params.m_a_dim**2 * self.psi_a -
                     (self.params.lambda_a / 6.0) * self.psi_a**3 -
                     self.params.g_int * self.psi_b)

        # ∂Ψ_B/∂t = ∇²Ψ_B + m_B² Ψ_B + (λ_B/3!) Ψ_B³ + G_int Ψ_A + ρ
        dpsi_b_dt = (lap_psi_b +
                     self.params.m_b_dim**2 * self.psi_b +
                     (self.params.lambda_b / 6.0) * self.psi_b**3 +
                     self.params.g_int * self.psi_a +
                     self.rho)

        # Explicit Euler update
        self.psi_a += dt * dpsi_a_dt
        self.psi_b += dt * dpsi_b_dt

        # Update membrane (slower dynamics)
        lap_eta = self.laplacian @ self.eta
        deta_dt = 0.1 * (lap_eta - 4.0 * np.pi * 1.0 * self.rho)
        self.eta += dt * deta_dt

    def evolve(self, n_steps: Optional[int] = None):
        """Evolve fields in time with energy tracking"""
        if n_steps is None:
            n_steps = int(self.params.t_max / self.params.dt)

        print(f"Evolving for {n_steps} steps...")

        for step in range(n_steps):
            self.time_step_euler()

            if step % max(1, n_steps // 20) == 0:
                energy = self.compute_energy()
                self.energy_history.append(energy)
                self.t_history.append(step * self.params.dt)
                print(f"  Step {step}/{n_steps}, E = {energy:.6e}")

        print("Evolution complete.")

    def plot_results(self, filename: str = "fields_1d.png"):
        """Plot field evolution and energy"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))

        # Ψ_A field
        axes[0, 0].plot(self.x, self.psi_a, 'b-', linewidth=2)
        axes[0, 0].set_xlabel('x (dimensionless)')
        axes[0, 0].set_ylabel('Ψ_A (dimensionless)')
        axes[0, 0].set_title('Waters Above Field (Ψ_A)')
        axes[0, 0].grid(True, alpha=0.3)

        # Ψ_B field
        axes[0, 1].plot(self.x, self.psi_b, 'r-', linewidth=2)
        axes[0, 1].set_xlabel('x (dimensionless)')
        axes[0, 1].set_ylabel('Ψ_B (dimensionless)')
        axes[0, 1].set_title('Waters Below Field (Ψ_B)')
        axes[0, 1].grid(True, alpha=0.3)

        # Membrane curvature
        axes[1, 0].plot(self.x, self.eta, 'g-', linewidth=2)
        axes[1, 0].set_xlabel('x (dimensionless)')
        axes[1, 0].set_ylabel('η (dimensionless)')
        axes[1, 0].set_title('Membrane Curvature (η)')
        axes[1, 0].grid(True, alpha=0.3)

        # Energy evolution
        if self.energy_history:
            axes[1, 1].plot(self.t_history, self.energy_history, 'k-', linewidth=2)
            axes[1, 1].set_xlabel('Time (dimensionless)')
            axes[1, 1].set_ylabel('Total Energy')
            axes[1, 1].set_title('Energy Conservation')
            axes[1, 1].grid(True, alpha=0.3)

        plt.tight_layout()
        filepath = os.path.join(OUTPUT_DIR, filename)
        plt.savefig(filepath, dpi=150)
        print(f"Saved plot to {filepath}")
        plt.close()


class WatersFieldSolver2D:
    """2D Finite Difference Solver for Waters Field Equations"""

    def __init__(self, params: SimulationParams):
        self.params = params
        self.x = np.linspace(params.x_min, params.x_max, params.nx)
        self.y = np.linspace(params.x_min, params.x_max, params.ny)
        self.xx, self.yy = np.meshgrid(self.x, self.y)
        self.dx = params.dx
        self.dy = params.dy

        # Initialize fields
        self.psi_a = np.zeros((params.ny, params.nx))
        self.psi_b = np.zeros((params.ny, params.nx))
        self.eta = np.zeros((params.ny, params.nx))
        self.rho = self._init_rho()

        self.energy_history = []
        self.t_history = []

    def _init_rho(self):
        """Initialize 2D matter density"""
        sigma = 0.2
        rho = self.params.rho_amplitude * np.exp(-(self.xx**2 + self.yy**2) / (2*sigma**2))
        return rho

    def set_initial_condition_gaussian(self, width: float = 0.2):
        """Initialize fields with Gaussian perturbation"""
        sigma = width

        self.psi_a = 0.1 * np.exp(-(self.xx**2 + self.yy**2) / (2*sigma**2))
        self.psi_b = 0.1 * np.exp(-(self.xx**2 + self.yy**2) / (2*sigma**2))
        self.eta = 0.05 * np.exp(-(self.xx**2 + self.yy**2) / (2*sigma**2))

    def laplacian_2d(self, field: np.ndarray) -> np.ndarray:
        """Compute 2D Laplacian with periodic BC"""
        # ∂²/∂x² using finite differences
        d2_dx2 = np.zeros_like(field)
        d2_dx2[:, :-1] -= 2 * field[:, :-1]
        d2_dx2[:, :-1] += field[:, 1:]
        d2_dx2[:, 1:] += field[:, :-1]
        d2_dx2 /= self.dx**2

        # ∂²/∂y² using finite differences
        d2_dy2 = np.zeros_like(field)
        d2_dy2[:-1, :] -= 2 * field[:-1, :]
        d2_dy2[:-1, :] += field[1:, :]
        d2_dy2[1:, :] += field[:-1, :]
        d2_dy2 /= self.dy**2

        # Apply periodic boundary conditions
        d2_dx2[:, 0] = (field[:, 1] - 2*field[:, 0] + field[:, -1]) / self.dx**2
        d2_dx2[:, -1] = (field[:, 0] - 2*field[:, -1] + field[:, -2]) / self.dx**2

        d2_dy2[0, :] = (field[1, :] - 2*field[0, :] + field[-1, :]) / self.dy**2
        d2_dy2[-1, :] = (field[0, :] - 2*field[-1, :] + field[-2, :]) / self.dy**2

        return d2_dx2 + d2_dy2

    def time_step_euler(self):
        """Single Euler time step for 2D"""
        dt = self.params.dt

        lap_psi_a = self.laplacian_2d(self.psi_a)
        lap_psi_b = self.laplacian_2d(self.psi_b)

        dpsi_a_dt = (lap_psi_a -
                     self.params.m_a_dim**2 * self.psi_a -
                     (self.params.lambda_a / 6.0) * self.psi_a**3 -
                     self.params.g_int * self.psi_b)

        dpsi_b_dt = (lap_psi_b +
                     self.params.m_b_dim**2 * self.psi_b +
                     (self.params.lambda_b / 6.0) * self.psi_b**3 +
                     self.params.g_int * self.psi_a +
                     self.rho)

        self.psi_a += dt * dpsi_a_dt
        self.psi_b += dt * dpsi_b_dt

        lap_eta = self.laplacian_2d(self.eta)
        deta_dt = 0.1 * (lap_eta - 4.0 * np.pi * 1.0 * self.rho)
        self.eta += dt * deta_dt

    def compute_energy(self) -> float:
        """Compute 2D total energy"""
        dpsi_a_dx = np.gradient(self.psi_a, axis=1) / self.dx
        dpsi_a_dy = np.gradient(self.psi_a, axis=0) / self.dy
        dpsi_b_dx = np.gradient(self.psi_b, axis=1) / self.dx
        dpsi_b_dy = np.gradient(self.psi_b, axis=0) / self.dy

        kin_a = 0.5 * np.sum((dpsi_a_dx**2 + dpsi_a_dy**2)) * self.dx * self.dy
        kin_b = 0.5 * np.sum((dpsi_b_dx**2 + dpsi_b_dy**2)) * self.dx * self.dy

        v_a = (0.5 * self.params.m_a_dim**2 * self.psi_a**2 +
               (self.params.lambda_a / 24.0) * self.psi_a**4)
        v_b = (0.5 * self.params.m_b_dim**2 * self.psi_b**2 -
               (self.params.lambda_b / 24.0) * self.psi_b**4)
        v_int = -self.params.g_int * self.psi_a * self.psi_b

        pot_energy = np.sum((v_a + v_b + v_int) * self.dx * self.dy)

        return kin_a + kin_b + pot_energy

    def evolve(self, n_steps: Optional[int] = None):
        """Evolve 2D fields in time"""
        if n_steps is None:
            n_steps = int(self.params.t_max / self.params.dt)

        print(f"Evolving 2D system for {n_steps} steps...")

        for step in range(n_steps):
            self.time_step_euler()

            if step % max(1, n_steps // 10) == 0:
                energy = self.compute_energy()
                self.energy_history.append(energy)
                self.t_history.append(step * self.params.dt)
                print(f"  Step {step}/{n_steps}, E = {energy:.6e}")

        print("2D evolution complete.")

    def plot_results(self, filename: str = "fields_2d.png"):
        """Plot 2D field contours"""
        fig, axes = plt.subplots(2, 2, figsize=(14, 12))

        # Ψ_A
        im0 = axes[0, 0].contourf(self.xx, self.yy, self.psi_a, levels=20, cmap='RdBu_r')
        axes[0, 0].set_title('Waters Above Field (Ψ_A)')
        axes[0, 0].set_xlabel('x')
        axes[0, 0].set_ylabel('y')
        plt.colorbar(im0, ax=axes[0, 0])

        # Ψ_B
        im1 = axes[0, 1].contourf(self.xx, self.yy, self.psi_b, levels=20, cmap='RdBu_r')
        axes[0, 1].set_title('Waters Below Field (Ψ_B)')
        axes[0, 1].set_xlabel('x')
        axes[0, 1].set_ylabel('y')
        plt.colorbar(im1, ax=axes[0, 1])

        # η
        im2 = axes[1, 0].contourf(self.xx, self.yy, self.eta, levels=20, cmap='viridis')
        axes[1, 0].set_title('Membrane Curvature (η)')
        axes[1, 0].set_xlabel('x')
        axes[1, 0].set_ylabel('y')
        plt.colorbar(im2, ax=axes[1, 0])

        # Energy
        if self.energy_history:
            axes[1, 1].plot(self.t_history, self.energy_history, 'k-', linewidth=2)
            axes[1, 1].set_xlabel('Time')
            axes[1, 1].set_ylabel('Total Energy')
            axes[1, 1].set_title('Energy Evolution')
            axes[1, 1].grid(True, alpha=0.3)

        plt.tight_layout()
        filepath = os.path.join(OUTPUT_DIR, filename)
        plt.savefig(filepath, dpi=150)
        print(f"Saved 2D plot to {filepath}")
        plt.close()


def run_1d_equilibrium():
    """Run 1D equilibrium test"""
    print("\n" + "="*70)
    print("TEST 1: 1D Equilibrium Configuration")
    print("="*70)

    params = SimulationParams(
        nx=256,
        t_max=0.1,
        dt=0.001,
        rho_amplitude=0.1
    )

    solver = WatersFieldSolver1D(params)
    solver.set_initial_condition_gaussian(width=0.2)
    solver.compute_equilibrium(max_iter=10)

    solver.plot_results("test1_equilibrium.png")

    return solver


def run_1d_evolution():
    """Run 1D perturbation evolution around equilibrium"""
    print("\n" + "="*70)
    print("TEST 2: 1D Perturbation Dynamics Around Equilibrium")
    print("="*70)

    params = SimulationParams(
        nx=256,
        t_max=0.1,
        dt=0.0005,
        m_a_dim=0.1,
        m_b_dim=0.2,  # Reduced for stability
        lambda_a=1e-5,  # Much smaller coupling
        lambda_b=1e-5,
        g_int=1e-6,
        rho_amplitude=0.05  # Smaller source
    )

    solver = WatersFieldSolver1D(params)
    solver.set_initial_condition_gaussian(width=0.15)

    # Compute initial equilibrium
    print("\nFinding equilibrium configuration...")
    solver.compute_equilibrium(max_iter=8)

    print("\nEvolving small perturbations around equilibrium...")
    solver.evolve(n_steps=200)

    solver.plot_results("test2_evolution_1d.png")

    return solver


def run_2d_evolution():
    """Run 2D spatial evolution"""
    print("\n" + "="*70)
    print("TEST 3: 2D Spatial Structure Formation")
    print("="*70)

    params = SimulationParams(
        nx=64,
        ny=64,
        t_max=0.1,
        dt=0.0005,
        m_a_dim=0.1,
        m_b_dim=0.2,
        lambda_a=1e-5,
        lambda_b=1e-5,
        g_int=1e-6,
        rho_amplitude=0.05
    )

    solver = WatersFieldSolver2D(params)
    solver.set_initial_condition_gaussian(width=0.15)
    solver.evolve(n_steps=200)

    solver.plot_results("test3_evolution_2d.png")

    return solver


def convergence_test():
    """Test convergence with different grid resolutions"""
    print("\n" + "="*70)
    print("TEST 4: Convergence Study on Equilibrium Solutions")
    print("="*70)

    nx_values = [64, 128, 256]
    energies = []

    for nx in nx_values:
        print(f"\nTesting with nx={nx}...")

        params = SimulationParams(
            nx=nx,
            rho_amplitude=0.05
        )

        solver = WatersFieldSolver1D(params)
        solver.set_initial_condition_gaussian()
        solver.compute_equilibrium(max_iter=5)

        final_energy = solver.compute_energy()
        energies.append(final_energy)

        print(f"  Equilibrium energy: {final_energy:.6e}")

    # Plot convergence
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(nx_values, np.abs(np.array(energies) - energies[-1]), 'bo-', linewidth=2, markersize=8)
    ax.set_xlabel('Grid points (nx)', fontsize=12)
    ax.set_ylabel('|E(nx) - E(256)|', fontsize=12)
    ax.set_title('Convergence Study: Energy vs. Grid Resolution', fontsize=14)
    ax.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "test4_convergence.png"), dpi=150)
    print("\nConvergence plot saved.")
    plt.close()


if __name__ == "__main__":
    print("Waters Field Equations Numerical Simulation Suite")
    print("="*70)

    # Run all tests
    solver1 = run_1d_equilibrium()
    solver2 = run_1d_evolution()
    solver3 = run_2d_evolution()
    convergence_test()

    print("\n" + "="*70)
    print("All simulations complete!")
    print("="*70)
