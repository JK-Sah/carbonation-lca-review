"""Net-benefit condition model for CO2 mineralization in cement-based products.

    dG = A + U*(1 - s/eta) - P        kg CO2-eq per unit product
    r  = 100 * dG / G_base            % reduction against the OPC baseline
    s* = eta * (1 + (A - P)/U)        break-even supply-chain intensity, dG = 0

A is the avoided-clinker term (clinker displaced x emission factor, net of any
added binder), U the permanently mineralized uptake, eta the uptake efficiency,
s the CO2 supply-chain GWP intensity, P the strength-compensation or process
penalty, G_base the baseline embodied GWP of the conventional product.

Parameter ranges below are physically bounded and derived from mechanism --
stoichiometric uptake capacity, typical binder contents, reported carbonation
efficiencies. They are not fitted to any synthesis result, and could not be:
the review reports no pooled estimate.
"""

G_BASE_DEFAULT = 350.0


def net_reduction(A, U, eta, s, P, G_base):
    return 100.0 * (A + U * (1.0 - s / eta) - P) / G_base


def break_even_s(A, U, eta, P):
    return eta * (1.0 + (A - P) / U)


ARCHETYPES = {
    "Fresh-mix / OPC": dict(
        A=(0.0, 34.8), U=(4.0, 20.0), eta=(0.50, 0.70), P=(0.0, 35.0)),
    "Post-cast low-Ca binder": dict(
        A=(54.0, 120.0), U=(20.0, 60.0), eta=(0.60, 0.80), P=(0.0, 25.0)),
    "Slag / waste (clinker elim.)": dict(
        A=(180.0, 300.0), U=(20.0, 60.0), eta=(0.60, 0.80), P=(0.0, 25.0)),
}

SOURCING = {
    "point-source capture": (0.05, 0.35),
    "direct air capture (DAC)": (0.55, 1.20),
}

G_BASE_RANGE = (300.0, 400.0)

GLOBAL_BOUNDS = {
    "A (clinker displaced)": (0.0, 260.0),
    "U (mineralized uptake)": (5.0, 60.0),
    "eta (uptake efficiency)": (0.40, 0.90),
    "s (CO2 supply-chain intensity)": (0.05, 1.20),
    "P (strength penalty)": (0.0, 40.0),
    "G_base (baseline GWP)": (300.0, 400.0),
}

TABLE4_ROWS = [
    ("Clinker eliminated (e.g. slag/waste)",       240.0, 40.0, 0.70,  0.0),
    ("Clinker partially displaced (e.g. 30% RCF)",  87.0, 40.0, 0.70,  0.0),
    ("No clinker displaced (e.g. CO2 injection)",   17.4, 12.0, 0.60,  0.0),
    ("No clinker displaced, with strength penalty", 17.4, 12.0, 0.60, 25.0),
]


def table4(G_base=G_BASE_DEFAULT, s=0.2):
    rows = []
    for name, A, U, eta, P in TABLE4_ROWS:
        rows.append((name, A, U, eta, P,
                     net_reduction(A, U, eta, s, P, G_base),
                     break_even_s(A, U, eta, P)))
    return rows


if __name__ == "__main__":
    head = ("Archetype", "A", "U", "eta", "P", "r at s=0.2 (%)", "s*")
    print(f"{head[0]:<44}{head[1]:>7}{head[2]:>6}{head[3]:>6}"
          f"{head[4]:>6}{head[5]:>16}{head[6]:>8}")
    for name, A, U, eta, P, r, s_star in table4():
        print(f"{name:<44}{A:>7.1f}{U:>6.1f}{eta:>6.2f}"
              f"{P:>6.1f}{r:>16.1f}{s_star:>8.2f}")
