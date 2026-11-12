"""Does the Sobol ranking survive a different choice of priors?

Variance indices depend on the assumed input space, so the dominance of clinker
displacement is re-tested under four specifications:

    S1  uniform priors over the wide base ranges (as reported)
    S2  triangular priors peaked at modal values
    S3  clinker-displacement range halved to [0, 150] kg/m3
    S4  every parameter at +/-50% of its own midpoint, clipped to admissible
        bounds, which removes the "A has the widest range" artifact

Total-order S_T is reported for all six parameters under each (Jansen
estimator). What matters is whether the ranking holds, not whether the
percentages match.

    python src/sobol_robustness.py
"""
import numpy as np
from scipy.stats import qmc

# param order: A, U, eta, s, P, G
NAMES = ["A (clinker displaced)", "U (mineralized uptake)", "eta (uptake efficiency)",
         "s (CO2 supply-chain intensity)", "P (strength penalty)", "G_base (baseline GWP)"]
D = len(NAMES)


def model(M):
    A, U, eta, s, P, G = (M[:, i] for i in range(6))
    return (A + U * (1.0 - s / eta) - P) / G * 100.0


def uniform_inv(u, lo, hi):
    return lo + u * (hi - lo)


def tri_inv(u, lo, mode, hi):
    Fc = (mode - lo) / (hi - lo)
    left = lo + np.sqrt(u * (hi - lo) * (mode - lo))
    right = hi - np.sqrt((1.0 - u) * (hi - lo) * (hi - mode))
    return np.where(u < Fc, left, right)


# Base ranges and typical modes
BASE = [(0.0, 260.0), (5.0, 60.0), (0.40, 0.90), (0.05, 1.20), (0.0, 40.0), (300.0, 400.0)]
MODE = [60.0, 25.0, 0.65, 0.20, 5.0, 350.0]
# Physically admissible bounds (used to clip the equal-width scenario)
PHYS = [(0.0, 300.0), (0.0, 80.0), (0.40, 0.90), (0.05, 1.20), (0.0, 60.0), (300.0, 400.0)]


def make_transforms(spec):
    if spec == "base":
        return [(lambda u, lo=lo, hi=hi: uniform_inv(u, lo, hi)) for lo, hi in BASE]
    if spec == "triangular":
        return [(lambda u, lo=lo, m=m, hi=hi: tri_inv(u, lo, m, hi))
                for (lo, hi), m in zip(BASE, MODE)]
    if spec == "narrow-A":
        b = list(BASE); b[0] = (0.0, 150.0)
        return [(lambda u, lo=lo, hi=hi: uniform_inv(u, lo, hi)) for lo, hi in b]
    if spec == "equal-width":
        out = []
        for (lo, hi), (plo, phi) in zip(BASE, PHYS):
            mid = 0.5 * (lo + hi)
            w = 0.5 * mid
            nlo, nhi = max(plo, mid - w), min(phi, mid + w)
            out.append((lambda u, lo=nlo, hi=nhi: uniform_inv(u, lo, hi)))
        return out
    raise ValueError(spec)


def sobol_ST(spec, n_base=2 ** 16, seed=12345):
    tf = make_transforms(spec)
    sob = qmc.Sobol(d=2 * D, scramble=True, seed=seed)
    X = sob.random_base2(m=int(np.log2(n_base)))
    A01, B01 = X[:, :D], X[:, D:]
    A = np.column_stack([tf[i](A01[:, i]) for i in range(D)])
    B = np.column_stack([tf[i](B01[:, i]) for i in range(D)])
    yA, yB = model(A), model(B)
    varY = np.var(np.concatenate([yA, yB]), ddof=1)
    ST = np.empty(D)
    for i in range(D):
        ABi = A.copy(); ABi[:, i] = B[:, i]
        yABi = model(ABi)
        ST[i] = 0.5 * np.mean((yA - yABi) ** 2) / varY
    return np.clip(ST, 0, None)


def main():
    specs = ["base", "triangular", "narrow-A", "equal-width"]
    labels = {"base": "S1 base (uniform, wide)", "triangular": "S2 triangular priors",
              "narrow-A": "S3 narrow-A [0,150]", "equal-width": "S4 equal +/-50% width"}
    results = {s: sobol_ST(s) for s in specs}

    print("Total-order Sobol index S_T (%) by input specification")
    print("=" * 92)
    hdr = f"{'Parameter':32s}" + "".join(f"{labels[s]:>15s}" for s in specs)
    print(hdr)
    print("-" * 92)
    for i, name in enumerate(NAMES):
        row = f"{name:32s}" + "".join(f"{results[s][i]*100:14.1f}%" for s in specs)
        print(row)
    print("-" * 92)
    # ranking check
    print("\nTop driver and its S_T in each specification:")
    for s in specs:
        order = np.argsort(results[s])[::-1]
        top = NAMES[order[0]].split(" (")[0]
        second = NAMES[order[1]].split(" (")[0]
        print(f"  {labels[s]:26s}: 1) {top} ({results[s][order[0]]*100:.0f}%)  "
              f"2) {second} ({results[s][order[1]]*100:.0f}%)")


if __name__ == "__main__":
    main()
