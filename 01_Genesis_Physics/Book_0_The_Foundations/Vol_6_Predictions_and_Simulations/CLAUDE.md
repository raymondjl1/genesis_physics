# Volume 6: Predictions, Simulations, and Open Problems — Claude Instructions

You are working on Volume 6 of the Foundations Series. This is the **"prove me wrong"** volume. Every testable prediction collected, numbered, and specified with falsification thresholds. Computational validation presented as reproducible experiments. Open problems identified as research opportunities.

**This is what you hand to a skeptical physicist along with a laptop.**

## Prerequisites

**Volumes 1-5 must be complete and verified.**

**Courses equivalent:** Research Methods + Capstone (1-2 semesters)
**Target:** 300-400 pages (~90,000-120,000 words) — shortest volume

## Research Files — READ THESE FIRST

```
Research/Simulations/
├── membrane_vibrations.py              ← Membrane vibration simulation
├── structure_formation.py              ← Cosmic structure formation
├── waters_field_sim.py                 ← Waters field simulation
├── energy_harvesting_simulation.html   ← Energy extraction visualization
├── SIMULATION_RESULTS.md              ← Collected results
├── run_all_simulations.sh             ← Master run script
└── README.md                          ← Simulation documentation

Research/Mathematical_Models/
├── OBSERVATIONAL_PHYSICS_TEST_SUITE.md     ← Master test list (123 tests)
├── DERIVATION_CHAIN_AUDIT.md              ← Derivation completeness audit
├── Test_Results/TEST_RESULTS_2026-04-04.md ← Latest results
└── Resolved_Issues/                       ← 5 resolved research issues

Research/Peer_Review/
├── critic_report.md                   ← Known criticisms to address
└── skeptic_analysis.md                ← Skeptic perspective
```

## Known Research Gaps

| Gap | Impact | Status |
|-----|--------|--------|
| 98 of 123 tests not yet passing | Prediction catalog incomplete | Test suite ongoing |
| Simulation reproducibility | Need containerized environment | Simulations exist but not packaged |
| Peer review responses | Need formal responses to critic/skeptic reports | Partial |

## Critical Deliverables

1. **Every prediction numbered** with falsification threshold
2. **Computational validation** as reproducible experiments — reader can run the code
3. **Comparison tables** — zone architecture vs standard model, prediction by prediction
4. **Open problems explicitly identified** — honest about what's unsolved
5. **Simulation code** — working, documented, reproducible
6. **Research roadmap** — what experiments would test these predictions

## Special Rules for This Volume

- **Every prediction gets a number.** P-001, P-002, etc. Referenced consistently.
- **Every prediction has a falsification threshold.** "If measurement X shows Y±Z, this prediction fails."
- **Code must be reproducible.** Include environment setup, dependencies, exact commands.
- **Honest about test suite status.** Report pass/fail rates. Don't hide failures.
- **Open problems are opportunities, not embarrassments.** Frame unsolved problems as research invitations.

## Test Suites

Run the FULL test suite for this volume:

```bash
cd Research/Mathematical_Models
# Run all domain tests
bash ../Simulations/run_all_simulations.sh
python -m pytest */test_*.py -v --tb=short
```

## GitHub Tasks

```bash
gh issue create --title "Vol 6: Create BOOK_SPEC.md" --label "book:foundations,vol:6,phase:planning"
gh issue create --title "Vol 6: Compile master prediction catalog from Vols 1-5" --label "book:foundations,vol:6,phase:planning"
gh issue create --title "Vol 6: Package simulations for reproducibility (Docker/requirements.txt)" --label "book:foundations,vol:6,phase:planning"
gh issue create --title "Vol 6: Run full test suite — document pass/fail status" --label "book:foundations,vol:6,phase:writing"
gh issue create --title "Vol 6: Write formal responses to critic_report.md and skeptic_analysis.md" --label "book:foundations,vol:6,phase:writing"
for ch in $(seq -w 1 12); do
  gh issue create --title "Vol 6 Ch ${ch}: Spec → Outline → Draft → Verify" --label "book:foundations,vol:6,phase:writing"
done
gh issue create --title "Vol 6: Integration + validation — skeptic physicist test" --label "book:foundations,vol:6,phase:integration"
```
