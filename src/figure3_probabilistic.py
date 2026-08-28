"""
Figure 3 — probabilistic net-benefit and global variance decomposition.

Panel (a) total-order Sobol indices; panel (b) Monte Carlo probability that a product is
genuinely cleaner, by archetype and CO2 sourcing. Reads results/probabilistic_results.json,
so run probabilistic_sensitivity.py first:

    cd src && python3 probabilistic_sensitivity.py && python3 figure3_probabilistic.py
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
with open(os.path.join(RES, "probabilistic_results.json")) as fh:
    R = json.load(fh)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.4), dpi=300)

# --- (a) Sobol total-order indices ---
ST = R["sobol"]["ST"]
order = sorted(ST, key=ST.get)
vals = [max(0.0, ST[k]) * 100 for k in order]
colours = ["#bdbdbd"] * len(order)
colours[-1] = "#1b7837"
ax1.barh(range(len(order)), vals, color=colours)
ax1.set_yticks(range(len(order)))
PRETTY = {"A (clinker displaced)": "$A$  clinker displaced",
          "s (CO2 supply-chain intensity)": "$s$  CO$_2$ supply-chain intensity",
          "P (strength penalty)": "$P$  strength penalty",
          "G_base (baseline GWP)": "$G_{base}$  baseline GWP",
          "eta (uptake efficiency)": r"$\eta$  uptake efficiency",
          "U (mineralized uptake)": "$U$  mineralized uptake"}
ax1.set_yticklabels([PRETTY.get(k, k) for k in order], fontsize=9)
for i, v in enumerate(vals):
    ax1.text(v + 1, i, f"{v:.1f}%", va="center", fontsize=9)
ax1.set_xlabel("Share of net-benefit variance, total-order Sobol index $S_T$ (%)", fontsize=10.5)
ax1.set_xlim(0, 100)
ax1.set_title("(a) What governs whether carbonation-cured\nconcrete is cleaner?",
              fontsize=11.5, weight="bold")
for sp in ("top", "right"): ax1.spines[sp].set_visible(False)

# --- (b) Monte Carlo probability of net benefit ---
mc = R["monte_carlo"]
archs = list(mc.keys())
regimes = ["point-source capture", "direct air capture (DAC)"]
x = np.arange(len(archs)); w = 0.38
reg_colours = {"point-source capture": "#4d9221", "direct air capture (DAC)": "#b8860b"}
for j, reg in enumerate(regimes):
    p = [mc[a][reg]["p_net_benefit"] * 100 for a in archs]
    bars = ax2.bar(x + (j - 0.5) * w, p, w, label=reg, color=reg_colours[reg])
    for b, val in zip(bars, p):
        ax2.text(b.get_x() + b.get_width() / 2, val + 1.2, f"{val:.0f}%", ha="center", fontsize=9)
ax2.axhline(50, color="#a01c14", lw=1.1, ls="--")
ax2.text(2.35, 51.5, "coin-flip", color="#a01c14", fontsize=8.5, ha="right")
ax2.set_xticks(x)
ax2.set_xticklabels(["Fresh-mix\n/ OPC", "Post-cast\nlow-Ca", "Slag / waste\n(clinker elim.)"], fontsize=9.5)
ax2.set_ylabel("Probability of a genuine net GWP reduction (%)", fontsize=10.5)
ax2.set_ylim(0, 108)
ax2.set_title("(b) Probability a product is actually cleaner,\nby CO$_2$ sourcing (Monte Carlo, n=200k)",
              fontsize=11.5, weight="bold")
ax2.legend(loc="lower right", fontsize=8.8, frameon=True)
for sp in ("top", "right"): ax2.spines[sp].set_visible(False)

fig.tight_layout()
for ext, kw in (("png", {}), ("tif", {"pil_kwargs": {"compression": "tiff_lzw"}})):
    fig.savefig(f"Figure3_ProbabilisticSensitivity.{ext}", dpi=300, bbox_inches="tight",
                facecolor="white", **kw)
print("wrote Figure3_ProbabilisticSensitivity.{png,tif}")
