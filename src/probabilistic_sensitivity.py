"""
Probabilistic net-benefit analysis and global (Sobol) variance decomposition
for CO2 mineralization in concrete.

Two analyses, both on the transparent net-benefit model (net_benefit_model.py):

  E5.  MONTE CARLO net-benefit probability
       For each technology archetype and CO2 sourcing regime, the probability
       that a carbonation-cured product is genuinely cleaner (r > 0), plus the
       median and 5th-95th percentile of the % GWP reduction.

  E6.  SOBOL GLOBAL SENSITIVITY (first-order S1 and total-order ST)
       Variance-based decomposition over the whole technology input space,
       answering: which single reported parameter governs whether a product
       is cleaner? Estimators: Saltelli/Jansen (2010).

No fabricated empirical data are used; parameter distributions are expert
scenario ranges (see net_benefit_model.py docstring).

Run:  python src/probabilistic_sensitivity.py
Deps: NumPy, SciPy (scipy.stats.qmc for the Sobol sequence).
"""
import json
import os
import numpy as np
from scipy.stats import qmc

from net_benefit_model import (
    net_reduction, break_even_s, ARCHETYPES, SOURCING, G_BASE_RANGE, GLOBAL_BOUNDS,
)

RNG = np.random.default_rng(20260723)
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results")
os.makedirs(RESULTS_DIR, exist_ok=True)


# ----------------------------------------------------------------------------
# E5. Monte Carlo net-benefit probability
# ----------------------------------------------------------------------------
def _u(lo_hi, n):
    lo, hi = lo_hi
    return RNG.uniform(lo, hi, n)


def monte_carlo(n=200_000):
    out = {}
    for arch, p in ARCHETYPES.items():
        out[arch] = {}
        for regime, s_rng in SOURCING.items():
            A = _u(p["A"], n); U = _u(p["U"], n); eta = _u(p["eta"], n)
            P = _u(p["P"], n); s = _u(s_rng, n); Gb = _u(G_BASE_RANGE, n)
            r = net_reduction(A, U, eta, s, P, Gb)
            out[arch][regime] = dict(
                p_net_benefit=float(np.mean(r > 0)),
                median_r=float(np.median(r)),
                p05=float(np.percentile(r, 5)),
                p95=float(np.percentile(r, 95)),
            )
    return out


# ----------------------------------------------------------------------------
# E6. Sobol global sensitivity (Saltelli/Jansen estimators)
# ----------------------------------------------------------------------------
def sobol(n_base=2 ** 16):
    names = list(GLOBAL_BOUNDS.keys())
    d = len(names)
    los = np.array([GLOBAL_BOUNDS[k][0] for k in names])
    his = np.array([GLOBAL_BOUNDS[k][1] for k in names])

    # Sobol sequence of dimension 2d -> split into A and B sample matrices
    sob = qmc.Sobol(d=2 * d, scramble=True, seed=12345)
    X = sob.random_base2(m=int(np.log2(n_base)))       # (n_base, 2d) in [0,1)
    A01, B01 = X[:, :d], X[:, d:]
    scale = lambda M: los + M * (his - los)
    A = scale(A01); B = scale(B01)

    def f(M):
        return net_reduction(M[:, 0], M[:, 1], M[:, 2], M[:, 3], M[:, 4], M[:, 5])

    yA, yB = f(A), f(B)
    varY = np.var(np.concatenate([yA, yB]), ddof=1)

    S1, ST = {}, {}
    for i, name in enumerate(names):
        ABi = A.copy(); ABi[:, i] = B[:, i]
        yABi = f(ABi)
        # First-order (Saltelli 2010) and total-order (Jansen 1999)
        s1 = np.mean(yB * (yABi - yA)) / varY
        st = 0.5 * np.mean((yA - yABi) ** 2) / varY
        S1[name] = float(s1)
        ST[name] = float(st)
    return dict(S1=S1, ST=ST, n_base=int(n_base), var_output=float(varY))


def break_even_summary():
    """Representative break-even s* per archetype (midpoint parameters)."""
    out = {}
    for arch, p in ARCHETYPES.items():
        mid = {k: 0.5 * (v[0] + v[1]) for k, v in p.items()}
        out[arch] = float(break_even_s(mid["A"], mid["U"], mid["eta"], mid["P"]))
    return out


def main():
    print("=" * 74)
    print("E5. MONTE CARLO NET-BENEFIT PROBABILITY  (r > 0)")
    print("=" * 74)
    mc = monte_carlo()
    for arch, regimes in mc.items():
        print(f"\n  {arch}")
        for regime, r in regimes.items():
            print(f"    {regime:26s}: P(net benefit)={r['p_net_benefit']*100:5.1f}%   "
                  f"median r={r['median_r']:5.1f}%   [P5,P95]=[{r['p05']:.1f}, {r['p95']:.1f}]")

    print("\n" + "=" * 74)
    print("E6. SOBOL GLOBAL SENSITIVITY  (share of outcome variance)")
    print("=" * 74)
    sob = sobol()
    order = sorted(sob["ST"], key=sob["ST"].get, reverse=True)
    print(f"  {'Parameter':34s} {'S1 (first-order)':>18s} {'ST (total)':>14s}")
    for name in order:
        print(f"  {name:34s} {max(0,sob['S1'][name])*100:15.1f} %  {max(0,sob['ST'][name])*100:11.1f} %")

    print("\n" + "=" * 74)
    print("Representative break-even CO2 supply-chain intensity s* (midpoint params)")
    print("=" * 74)
    be = break_even_summary()
    for arch, s_star in be.items():
        print(f"  {arch:30s}: s* = {s_star:.2f}")

    with open(os.path.join(RESULTS_DIR, "probabilistic_results.json"), "w") as fh:
        json.dump(dict(monte_carlo=mc, sobol=sob, break_even=be), fh, indent=2)
    print(f"\nSaved -> results/probabilistic_results.json")


if __name__ == "__main__":
    main()
