"""Graphical abstract -- three panels.

The published evidence (what the 17 studies declare and why they cannot be
pooled), what drives the magnitude (clinker displacement), and what decides the
sign (the carbonation step itself). Values are literals matching the manuscript.

    cd src && python3 graphical_abstract.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrow, Rectangle

W, H = 13.28, 5.307
INK, GREY, BLUE, PURPLE, GREEN, RED = "#111111", "#6b6b6b", "#1f6fb4", "#8e44ad", "#1e7b34", "#b3261e"
PANEL, EDGE = "#f7f8f9", "#d7dbdf"

fig = plt.figure(figsize=(W, H), dpi=300)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 40); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 100, 40, fc="white", ec="none"))

# ── header ─────────────────────────────────────────────────────────────────
ax.add_patch(Rectangle((0, 33.2), 100, 6.8, fc="#14181c", ec="none"))
ax.text(2.6, 37.2, "When is carbonation-cured concrete actually cleaner?",
        fontsize=21, weight="bold", color="white", va="center")
ax.text(2.6, 34.6,
        "PRISMA systematic review   ·   net-benefit condition framework   ·   proposed minimum reporting set",
        fontsize=11.5, style="italic", color="#b9c0c7", va="center")

def panel(x, w, title, tcolor):
    ax.add_patch(FancyBboxPatch((x, 1.6), w, 30.2, boxstyle="round,pad=0.35,rounding_size=0.5",
                                fc=PANEL, ec=EDGE, lw=1.4))
    ax.text(x + 1.5, 29.6, title, fontsize=11.5, weight="bold", color=tcolor, va="center")

panel(2.0, 30.0, "THE PUBLISHED EVIDENCE", RED)
panel(35.0, 30.0, "WHAT DRIVES THE MAGNITUDE", BLUE)
panel(68.0, 30.0, "WHAT DECIDES THE SIGN", GREEN)
for x in (33.2, 66.2):
    ax.add_patch(FancyArrow(x, 16.5, 1.4, 0, width=0.35, head_width=1.0, head_length=0.6,
                            length_includes_head=True, fc="#9aa0a6", ec="none"))

# ── panel 1 — incommensurability ───────────────────────────────────────────
ax.text(3.5, 27.2, "17 LCAs meet full", fontsize=13.5, weight="bold", color=INK, va="center")
ax.text(3.5, 25.4, "reporting criteria —", fontsize=13.5, weight="bold", color=INK, va="center")
ax.text(3.5, 23.6, "and cannot be pooled", fontsize=13.5, weight="bold", color=RED, va="center")

rows = [("5", "functional-unit bases"),
        ("17", "different comparators"),
        ("280–540", "kg CO₂-eq/m³ baselines"),
        ("8 of 25", "papers omit unit or boundary")]
for i, (big, lab) in enumerate(rows):
    y = 19.6 - i * 3.3
    ax.text(4.6, y, big, fontsize=13, weight="bold", color=BLUE, va="center")
    ax.text(12.4, y, lab, fontsize=10.2, color=GREY, va="center")

ax.text(3.5, 5.4, "Outcomes are reported as percentages,", fontsize=9.8, color=GREY)
ax.text(3.5, 3.9, "scenario tables, ranges crossing zero,", fontsize=9.8, color=GREY)
ax.text(3.5, 2.4, "and counts of datasets by sign.", fontsize=9.8, color=GREY)

# ── panel 2 — benefit tracks avoided clinker ───────────────────────────────
ax.text(36.5, 27.3, "Benefit tracks avoided clinker,", fontsize=12.3, weight="bold", color=INK, va="center")
ax.text(36.5, 25.5, "not mineralized CO₂", fontsize=12.3, weight="bold", color=INK, va="center")

BARS = [("No clinker displaced", "3.6\u20134.6%", 4.6, GREY, 21.4),
        ("Partial displacement", "14\u201337%", 37.0, BLUE, 15.9),
        ("Clinker eliminated", "61\u201383%  \u2192  net-negative", 83.0, GREEN, 10.4)]
BAR_X, BAR_W = 36.5, 26.0
for name, lab, val, col, y in BARS:
    ax.text(BAR_X, y + 1.75, name, fontsize=10.4, weight="bold", color=INK, va="center")
    ax.text(BAR_X + BAR_W, y + 1.75, lab, fontsize=9.8, weight="bold", color=col,
            va="center", ha="right")
    ax.add_patch(Rectangle((BAR_X, y - 0.35), BAR_W, 1.35, fc="#e6e8ea", ec="none"))
    ax.add_patch(Rectangle((BAR_X, y - 0.35), BAR_W * min(val, 100) / 100.0, 1.35, fc=col, ec="none"))

ax.text(36.5, 7.2, "Every reduction above 10% involves clinker", fontsize=9.8, color=GREY)
ax.text(36.5, 5.7, "being substituted or eliminated. One study:", fontsize=9.8, color=GREY)
ax.text(36.5, 4.0, "5–8 kg CO₂-eq/t cement per 1% clinker replaced.",
        fontsize=9.8, weight="bold", color=INK)

# ── panel 3 — sign is set by process configuration ─────────────────────────
ax.text(69.5, 27.3, "Isolate the carbonation step", fontsize=12.3, weight="bold", color=INK, va="center")
ax.text(69.5, 25.5, "and the sign changes", fontsize=12.3, weight="bold", color=INK, va="center")

SX, SW = 69.5, 26.0
ROWS = [("Process electricity charged", "\u22123.1 to \u221211.3%", RED),
        ("Dry ice, at +16\u201346% cost", "+2.1 to +3.8%", GREY),
        ("Forced carbonation of RCA", "up to +37%", GREEN)]
for i, (lab, val, col) in enumerate(ROWS):
    y = 22.4 - i * 2.45
    ax.add_patch(Rectangle((SX, y - 0.42), 0.55, 1.5, fc=col, ec="none"))
    ax.text(SX + 1.3, y + 0.3, lab, fontsize=9.6, color=INK, va="center")
    ax.text(SX + SW, y + 0.3, val, fontsize=10.2, weight="bold", color=col,
            va="center", ha="right")

ax.plot([SX, SX + SW], [15.4, 15.4], color=EDGE, lw=1.1)
ax.text(SX, 14.0, "Same product, three CO\u2082 recovery routes:", fontsize=9.6, color=GREY, va="center")
ax.text(SX, 12.2, "68%   \u00b7   77%   \u00b7   71%", fontsize=12.6, weight="bold",
        color=BLUE, va="center")

ax.add_patch(FancyBboxPatch((SX - 0.6, 1.9), SW + 1.2, 8.6,
                            boxstyle="round,pad=0.3,rounding_size=0.4",
                            fc="#eef4fa", ec=BLUE, lw=1.2))
ax.text(SX + 0.4, 9.2, "PROPOSED MINIMUM REPORTING SET", fontsize=8.0, weight="bold",
        color=BLUE, va="center")
for i, f in enumerate(["Functional unit", "System boundary", "Absolute baseline GWP",
                       "CO₂ source and supply-chain intensity", "Clinker displaced"]):
    ax.text(SX + 0.7, 7.6 - i * 1.32, "•", fontsize=10, color=BLUE, va="center")
    ax.text(SX + 1.6, 7.6 - i * 1.32, f, fontsize=9.4, color=INK, va="center")

for ext, kw in (("png", {}), ("tif", {"pil_kwargs": {"compression": "tiff_lzw"}})):
    fig.savefig(f"JCLP_GraphicalAbstract.{ext}", dpi=300, facecolor="white", **kw)
print("wrote JCLP_GraphicalAbstract.{png,tif}")
