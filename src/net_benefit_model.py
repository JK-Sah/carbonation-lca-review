"""
Net-benefit condition model for CO2 mineralization in concrete.

Transparent first-order life-cycle model of the net avoided GWP of a
carbonation-cured product relative to its OPC baseline:

    dG = A + U * (1 - s/eta) - P              [kg CO2e per unit product]
    r  = dG / G_base * 100                      [% reduction vs. OPC baseline]

    A      : avoided-clinker GWP term (clinker displaced x emission factor,
             net of any added-binder burden)         [kg CO2e / m3]
    U      : permanently mineralized CO2 uptake       [kg CO2 / m3]
    eta    : uptake efficiency (fraction of delivered CO2 mineralized)  [-]
    s      : CO2 supply-chain GWP intensity (kg CO2e emitted / kg CO2 delivered)
    P      : strength-compensation or process-energy penalty  [kg CO2e / m3]
    G_base : baseline embodied GWP of the conventional OPC product  [kg CO2e / m3]

Break-even CO2 supply-chain intensity (dG = 0):   s* = eta * (1 + (A - P)/U)

NOTE ON DATA PROVENANCE: the parameter ranges used in the probabilistic
analysis are physically bounded values derived from mechanism -- stoichiometric
uptake capacity, typical binder contents, and reported carbonation efficiencies.
They are NOT fitted to any synthesis result, and none could be: the review
reports no pooled estimate. Archetypes are defined by the degree of Portland
clinker displacement (none / partial / complete), following manuscript
Section 4.4. The model is explanatory, not a source of empirical estimates.
"""
import numpy as np


def net_reduction(A, U, eta, s, P, G_base):
    """Percentage net life-cycle GWP reduction vs. OPC baseline."""
    dG = A + U * (1.0 - s / eta) - P
    return dG / G_base * 100.0


def break_even_s(A, U, eta, P):
    """Break-even CO2 supply-chain intensity s* (dG = 0)."""
    return eta * (1.0 + (A - P) / U)


# Archetype parameter ranges (uniform), derived from mechanism (see manuscript Table 4).
# A in kg CO2e/m3; U in kg CO2/m3; eta dimensionless; P in kg CO2e/m3.
# The range MIDPOINTS are the deterministic archetype values used for the
# net-benefit curves in the manuscript (Figure 4 / Table 5): A = 17.4 / 87 / 240,
# U = 12 / 40 / 40, eta = 0.60 / 0.70 / 0.70. The deterministic curves are the
# zero-penalty (P=0) central case; the distributions below add the strength
# penalty and parameter spread. This keeps the deterministic and probabilistic
# analyses on a single, consistent parameterization.
ARCHETYPES = {
    "Fresh-mix / OPC":            dict(A=(0.0, 34.8),   U=(4.0, 20.0),  eta=(0.50, 0.70), P=(0.0, 35.0)),
    "Post-cast low-Ca binder":    dict(A=(54.0, 120.0), U=(20.0, 60.0), eta=(0.60, 0.80), P=(0.0, 25.0)),
    "Slag / waste (clinker elim.)":dict(A=(180.0, 300.0),U=(20.0, 60.0), eta=(0.60, 0.80), P=(0.0, 25.0)),
}

# CO2 sourcing regimes (range of s)
SOURCING = {
    "point-source capture": (0.05, 0.35),
    "direct air capture (DAC)": (0.55, 1.20),
}

G_BASE_RANGE = (300.0, 400.0)

# Global sensitivity input space (whole technology space)
GLOBAL_BOUNDS = {
    "A (clinker displaced)": (0.0, 260.0),
    "U (mineralized uptake)": (5.0, 60.0),
    "eta (uptake efficiency)": (0.40, 0.90),
    "s (CO2 supply-chain intensity)": (0.05, 1.20),
    "P (strength penalty)": (0.0, 40.0),
    "G_base (baseline GWP)": (300.0, 400.0),
}


# ---------------------------------------------------------------------------
# Manuscript Table 4 — deterministic archetype rows at s = 0.2, G_base = 350.
# Each row states its own P; the strength-penalty case is the fourth row.
# ---------------------------------------------------------------------------
TABLE4_ROWS = [
    ("Clinker eliminated (e.g. slag/waste)",      240.0, 40.0, 0.70,  0.0),
    ("Clinker partially displaced (e.g. 30% RCF)", 87.0, 40.0, 0.70,  0.0),
    ("No clinker displaced (e.g. CO2 injection)",  17.4, 12.0, 0.60,  0.0),
    ("No clinker displaced, with strength penalty",17.4, 12.0, 0.60, 25.0),
]

if __name__ == "__main__":
    print(f"{'Archetype':<44}{'A':>7}{'U':>6}{'eta':>6}{'P':>6}"
          f"{'r at s=0.2 (%)':>16}{'s*':>8}")
    for name, A, U, eta, P in TABLE4_ROWS:
        r = net_reduction(A, U, eta, 0.2, P, 350.0)
        s_star = break_even_s(A, U, eta, P)
        print(f"{name:<44}{A:>7.1f}{U:>6.1f}{eta:>6.2f}{P:>6.1f}{r:>16.1f}{s_star:>8.2f}")
