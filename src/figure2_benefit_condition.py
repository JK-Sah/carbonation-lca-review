"""
Figure 2 — net-benefit condition framework.

Net life-cycle GWP reduction r as a function of CO2 supply-chain intensity s, for the
three technology archetypes of manuscript Table 4 plus the fresh-mix case carrying a
strength-compensation penalty. Reproduces Table 4 exactly at s = 0.2:
r = 76.7 / 33.0 / 7.3 / 0.1 %, with break-even s* = 4.90 / 2.22 / 1.47 / 0.22.

    cd src && python3 figure2_benefit_condition.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from net_benefit_model import TABLE4_ROWS, net_reduction, break_even_s

G_BASE = 350.0
STYLE = [("#1b7837", "-", "Slag / waste-based (clinker eliminated)"),
         ("#762a83", "-", "Post-cast low-Ca binder"),
         ("#2166ac", "-", "Fresh-mix CO$_2$ injection / OPC"),
         ("#2166ac", "--", "Fresh-mix + strength-compensation penalty")]

fig, ax = plt.subplots(figsize=(9.2, 5.0), dpi=300)
s = np.linspace(0.0, 1.2, 400)

for (name, A, U, eta, P), (colour, ls, label) in zip(TABLE4_ROWS, STYLE):
    r = np.array([net_reduction(A, U, eta, si, P, G_BASE) for si in s])
    ax.plot(s, r, colour, linestyle=ls, linewidth=2.0, label=label)

ax.axhspan(-20, 0, color="#fdecec", zorder=0)
ax.axhline(0, color="#404040", linewidth=0.9)
ax.text(0.02, -14, "NET GWP INCREASE  (carbonation curing is not cleaner)",
        fontsize=8.5, style="italic", color="#b2182b")

# CO2 sourcing regimes
ax.axvspan(0.05, 0.35, color="#eef5ea", zorder=0)
ax.text(0.20, 92, "point-source\ncapture", ha="center", fontsize=8, color="#4d7c3a")
ax.axvspan(0.55, 1.20, color="#faf3e2", zorder=0)
ax.text(0.88, 92, "direct air capture", ha="center", fontsize=8, color="#8a6d1f")

ax.set_xlim(0, 1.2); ax.set_ylim(-20, 100)
ax.set_xlabel("CO$_2$ supply-chain GWP intensity, $s$  "
              "(kg CO$_2$-eq emitted per kg CO$_2$ delivered)", fontsize=10)
ax.set_ylabel("Net life-cycle GWP reduction vs. OPC baseline (%)", fontsize=10)
ax.set_title("Net-benefit condition framework: when carbonation-cured concrete is actually cleaner",
             fontsize=11, weight="bold")
ax.legend(fontsize=8.5, loc="center left", bbox_to_anchor=(0.02, 0.52), framealpha=0.95)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
ax.grid(axis="y", color="#e6e6e6", linewidth=0.6)
ax.set_axisbelow(True)

fig.tight_layout()
for ext, kw in (("png", {}), ("tif", {"pil_kwargs": {"compression": "tiff_lzw"}})):
    fig.savefig(f"Figure2_BenefitCondition.{ext}", dpi=300, bbox_inches="tight",
                facecolor="white", **kw)
print("wrote Figure2_BenefitCondition.{png,tif}")
for name, A, U, eta, P in TABLE4_ROWS:
    print(f"  {name:44} r(0.2)={net_reduction(A,U,eta,0.2,P,G_BASE):6.1f}%  "
          f"s*={break_even_s(A,U,eta,P):5.2f}")
