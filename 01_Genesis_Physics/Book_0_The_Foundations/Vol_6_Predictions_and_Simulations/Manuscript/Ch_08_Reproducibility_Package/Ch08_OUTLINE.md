# Chapter 8 Outline: Reproducibility Package

**Date:** 2026-04-11
**Status:** OUTLINE COMPLETE

---

## Section Plan

### 8.1 Why Reproducibility Is Non-Negotiable (~600 words)
- **Topic sentence:** A physics framework that can't be independently reproduced isn't physics — it's assertion.
- **"Why" entry:** Ch 5–7 presented results. This chapter makes them verifiable.
- **Key content:** Reproducibility crisis context. The "skeptic with a laptop" standard. What this chapter delivers. How long it should take (<1 hour).
- **Exit condition:** Reader understands what they'll get and why it matters.

### 8.2 Repository Structure (~800 words)
- **Topic sentence:** The simulation suite lives in a single directory with a deliberate structure.
- **Key content:**
  - Full file tree with line counts and descriptions
  - Three core modules: waters_field_sim.py, membrane_vibrations.py, structure_formation.py
  - Documentation files: README.md, SIMULATION_RESULTS.md, INDEX.txt
  - Helper scripts: run_all_simulations.sh
  - Special file: energy_harvesting_simulation.html (browser-based)
  - Output directory: generated PNG plots
  - Total: ~1,491 lines of simulation code + ~750 lines of documentation
- **Figure placement:** [FIGURE: Fig 6.8.1 — Repository Structure Diagram]
- **Exit condition:** Reader has a complete map of every file.

### 8.3 Environment Specification (~600 words)
- **Topic sentence:** Three packages, one language, no exotic dependencies.
- **Key content:**
  - Python ≥ 3.8 (tested on 3.10, 3.11)
  - NumPy ≥ 1.21 (array operations, linear algebra)
  - SciPy ≥ 1.7 (sparse eigensolvers, ODE integration)
  - Matplotlib ≥ 3.5 (visualization)
  - OS: Linux, macOS, Windows (all tested)
  - No GPU required. No network access required. No proprietary software.
  - Why these versions (compatibility, API stability)
- **Exit condition:** Reader knows exactly what they need.

### 8.4 Installation Walkthrough (~800 words)
- **Topic sentence:** From a clean machine to a working environment in under 15 minutes.
- **Key content:**
  - Step 1: Verify Python installation
  - Step 2: Create virtual environment (recommended)
  - Step 3: Install dependencies (pip install numpy scipy matplotlib)
  - Step 4: Verify installation (import test)
  - Step 5: Clone/download simulation files
  - Platform-specific notes for Linux, macOS, Windows
  - Verification command that confirms everything works
- **Figure placement:** [FIGURE: Fig 6.8.2 — Reproducibility Workflow]
- **Exit condition:** Reader has a working environment ready to run.

### 8.5 Running the Simulations — Module by Module (~1,500 words)
- **Topic sentence:** Each module runs independently with a single command.
- **Key content:**
  - **8.5.1 waters_field_sim.py** — command, 4 tests, ~30-60s runtime, 4 PNG outputs
  - **8.5.2 membrane_vibrations.py** — command, 3 analyses, ~10-20s runtime, 4 PNG outputs
  - **8.5.3 structure_formation.py** — command, comparisons, ~20-40s runtime, 5 PNG outputs
  - **8.5.4 energy_harvesting_simulation.html** — open in browser, what to expect, interactive controls
  - For each: exact command, expected console output summary, output files generated
- **Exit condition:** Reader can run every simulation.

### 8.6 Expected Outputs and Validation (~1,200 words)
- **Topic sentence:** "It ran" is not enough — here's how to know it ran correctly.
- **Key content:**
  - **Table 8.1:** waters_field_sim.py expected numerical outputs (equilibrium energy, convergence rate, energy conservation %)
  - **Table 8.2:** membrane_vibrations.py expected outputs (eigenfrequencies, mass values, analytical vs numerical error)
  - **Table 8.3:** structure_formation.py expected outputs (growth factor ratios, power spectrum ratios)
  - Cross-references: Table 8.1 → Ch 5 §5.5, Table 8.2 → Ch 7 §7.3, Table 8.3 → Ch 6 §6.3
  - Tolerance ranges: what variation is acceptable vs what indicates a problem
- **Exit condition:** Reader can verify correctness quantitatively.

### 8.7 The Master Run Script (~500 words)
- **Topic sentence:** One command to run everything.
- **Key content:**
  - run_all_simulations.sh: what it does, step by step
  - Important: the hardcoded path must be updated to the reader's local path
  - How to fix the path
  - Interpreting the summary output (PASSED/FAILED per module)
  - Exit codes: 0 = all pass, 1 = some failed
- **Exit condition:** Reader can run the full suite from a single command.

### 8.8 What's Packaged and What's Not (~600 words)
- **Topic sentence:** The simulation code is complete. The containerization is not.
- **Key content:**
  - **Packaged (green):** All three Python modules, documentation, run script, expected outputs
  - **Not packaged (yellow):** Docker container, requirements.txt with pinned versions, CI/CD pipeline
  - **Planned (gray):** Dockerfile, automated regression testing, GPU-accelerated variants
  - Why containerization matters and why it's not done yet (transparency over automation for Book 0)
  - What a future requirements.txt would contain
  - What a future Dockerfile would look like (sketch)
- **Figure placement:** [FIGURE: Fig 6.8.3 — Containerization Roadmap]
- **Exit condition:** Reader knows exactly what's complete and what's planned.

### 8.9 Troubleshooting Guide (~800 words)
- **Topic sentence:** When it doesn't work, start here.
- **Key content:**
  - **Problem 1:** Python version mismatch → diagnostic command, fix
  - **Problem 2:** Missing packages → pip install command
  - **Problem 3:** Matplotlib backend error (headless servers) → Agg backend fix
  - **Problem 4:** Path issues (run_all_simulations.sh hardcoded path) → how to update
  - **Problem 5:** Windows line endings → dos2unix or git config
  - **Problem 6:** Permission denied on .sh file → chmod +x
  - **Problem 7:** Numerical output differs slightly → floating-point tolerance explanation
  - Diagnostic checklist: 5 commands to run to identify the problem
- **Exit condition:** Reader can debug common problems.

### 8.10 Verification Checklist and Summary (~500 words)
- **Topic sentence:** The complete "did it work?" procedure.
- **Key content:**
  - Numbered verification checklist (10 items)
  - Problem sets (6 problems: 3 computational, 2 conceptual, 1 challenge)
  - Summary: what this chapter delivered, what Part II (Ch 5–8) accomplished as a whole
  - Transition to Part III (Ch 9–12): from computation to open problems and the future
- **Exit condition:** Reader has verified reproducibility end-to-end.

---

## Figure Plan

| Fig ID | Title | Type | Section | What It Shows | Why Needed | Complexity |
|--------|-------|------|---------|---------------|------------|------------|
| Fig 6.8.1 | Repository Structure | Diagram | §8.2 | File tree with module relationships, data flow arrows, and output dependencies | Reader needs spatial map before diving in | Medium |
| Fig 6.8.2 | Reproducibility Workflow | Flowchart | §8.4 | Clean machine → install → run → validate → compare with Ch 5–7 | Visual recipe card for the whole chapter | Medium |
| Fig 6.8.3 | Containerization Roadmap | Status diagram | §8.8 | Green (done) / Yellow (gap) / Gray (planned) items | Honest status at a glance | Simple |

---

## Cross-Reference Plan

| This Chapter | References | In Prior Chapter |
|-------------|-----------|-----------------|
| Table 8.1 (waters_field expected outputs) | Table 5.X, convergence results | Ch 5, §5.5–5.6 |
| Table 8.2 (membrane expected outputs) | Tables 7.1–7.3, eigenfrequencies | Ch 7, §7.3–7.4 |
| Table 8.3 (structure expected outputs) | Tables 6.1–6.3, growth factors | Ch 6, §6.3–6.4 |
| Environment specification | Simulation architecture | Ch 5, §5.2 |
| Module descriptions | Detailed methodology | Ch 5, §5.2–5.4 |

---

## Estimated Length

Total: ~7,900 words (~14 pages)
Target: 10–20 pages — within range.
