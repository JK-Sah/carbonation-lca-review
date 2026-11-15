"""Figure S8 -- patent citation genealogy for CO2 mineralization in concrete.

Forty-seven documents across four generations, with the non-patent-literature
link from the 2010 academic paper into the CarbonBuilt Generation 3 filings.
Rebuilt from the figure submitted with the first version, correcting the panel
title (it read "Figure 3", which collides with the manuscript's Figure 3), the
inventor initials (S. Monkman), and the journal of the 2010 paper
(J. Mater. Civ. Eng., not Cem. Concr. Compos.).

Patent numbers and dates are transcribed from the earlier figure and have not
been re-verified against a patent database.

    cd src && python3 figureS8_patent_genealogy.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

BLUE, GREEN, YELLOW, PINK, PURPLE = "#cfe2f7", "#cfe8dc", "#fdf0cd", "#f8d7da", "#e6d5f2"
EDGE = "#1f4e79"

fig, ax = plt.subplots(figsize=(13.9, 9.9), dpi=300)
ax.set_xlim(0, 100); ax.set_ylim(0, 72); ax.axis("off")
ax.add_patch(plt.Rectangle((0, 0), 100, 72, color="#f7f9fb", zorder=0))

def box(x, y, w, h, text, fc, fs=7.4, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.35,rounding_size=0.8",
                                fc=fc, ec=EDGE, lw=1.1, zorder=2))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs,
            weight=weight, zorder=3, linespacing=1.5)

def arrow(x1, y1, x2, y2, color=EDGE, ls="-", lw=1.0):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=11,
                                 color=color, lw=lw, linestyle=ls, zorder=1,
                                 shrinkA=0, shrinkB=2))

ax.text(50, 69.2, "Figure S8. Verified Patent Citation Genealogy — CO$_2$ Mineralization in Concrete "
        "(47 documents)", ha="center", fontsize=11.6, weight="bold", color=EDGE)
ax.text(50, 66.4, "★ = S. Monkman: inventor on CarbonCure Gen 1 & 2, and author of the 2010 academic "
        "paper cited as non-patent-literature prior art in CarbonBuilt Gen 3",
        ha="center", fontsize=7.6, style="italic", color="#a01c14")

# generation bands
for y, h, fc, lab in [(52.5, 11.5, BLUE,  "Gen 0\nFoundational\n(1977–1982)"),
                      (39.0, 12.5, GREEN, "Gen 1\nPioneer\n(2010–2016)"),
                      (25.5, 12.5, YELLOW,"Gen 2\nPlatform\n(2018–2020)"),
                      (10.0, 14.5, PINK,  "Gen 3\nCurrent\n(2022–2024)")]:
    box(2.0, y, 12.5, h, lab, fc, fs=8.0, weight="bold")

# Gen 0
box(21, 55.5, 19, 8.5, "Murray (1977)\nUS 4,117,060\nCO$_2$ exposure of\ncalcareous binder", BLUE)
box(44, 55.5, 19, 8.5, "Malinowski (1982)\nUS 4,362,679\nCO$_2$ compression-\ncuring", BLUE)
# Gen 1
box(21, 41.0, 19, 9.5, "CarbonCure\nUS 8,845,940 B2 (2014)\nCO$_2$ injection\n★ Inventor: S. Monkman", GREEN)
box(44, 41.0, 19, 9.5, "Solidia Tech.\nUS 9,266,773 B2 (2016)\nWollastonite-based\nCa-silicate", GREEN)
box(70, 41.0, 22, 9.5, "Monkman & Shao (2010)\nJ. Mater. Civ. Eng. 22\nCarbonation curing of\n"
                       "slag-cement concrete [Academic]", PURPLE, fs=7.0)
# Gen 2
box(21, 27.0, 19, 9.5, "CarbonCure\nUS 10,654,756 B2 (2020)\nControlled CO$_2$ dosing\n★ Inventor: S. Monkman", YELLOW)
box(44, 27.0, 19, 9.5, "Carbicrete\nWO 2020/197826 (2020)\nSteel slag binder +\nCO$_2$ curing, zero OPC", YELLOW)
# Gen 3
box(18, 12.0, 19, 9.5, "CarbonBuilt\nWO 2023/091528 (2023)\nLow-Ca composition\nfrom solid wastes", PINK)
box(40, 12.0, 19, 9.5, "CarbonBuilt\nWO 2023/235530 (2023)\nActive carbonation\ncuring apparatus", PINK)
box(62, 12.0, 20, 9.5, "CarbonBuilt\nUS 12,157,709 B2 (2024)\nIntegrated composition\n+ process ◆ ISSUED", PINK)

# citation arrows
for a, b in [((30.5,55.5),(30.5,50.5)), ((53.5,55.5),(30.5,50.5)),
             ((30.5,55.5),(53.5,50.5)), ((53.5,55.5),(53.5,50.5)),
             ((30.5,41.0),(30.5,36.5)), ((53.5,41.0),(53.5,36.5)),
             ((30.5,27.0),(27.5,21.5)), ((30.5,27.0),(49.5,21.5)),
             ((53.5,27.0),(49.5,21.5)), ((53.5,27.0),(72.0,21.5))]:
    arrow(a[0], a[1], b[0], b[1])

# Knowledge bridge: routed as arcs drawn above the boxes, so they are not hidden
# behind the Gen 1 / Gen 2 nodes they pass over.
ax.add_patch(FancyArrowPatch((70.0, 50.5), (40.5, 50.5), arrowstyle="-|>", mutation_scale=12,
                             color="#d95f02", lw=1.7, linestyle="--", zorder=5,
                             connectionstyle="arc3,rad=0.30", shrinkA=2, shrinkB=2))
ax.add_patch(FancyArrowPatch((72.0, 41.0), (30.0, 21.6), arrowstyle="-|>", mutation_scale=12,
                             color="#b2182b", lw=1.7, linestyle="--", zorder=5,
                             connectionstyle="arc3,rad=-0.22", shrinkA=2, shrinkB=2))
ax.text(84.5, 37.5, "← NPL prior art\nin Gen 3 patents\n(verified via Justia)",
        fontsize=7.2, weight="bold", color="#b2182b", ha="center", linespacing=1.5)
ax.text(76.5, 57.5, "Knowledge bridge\n(same individual: inventor on\nCarbonCure patents and author\n"
        "of the academic prior art\ncited by CarbonBuilt)",
        fontsize=7.0, style="italic", color="#a01c14", ha="center", linespacing=1.5,
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#a01c14", lw=0.9))

handles=[plt.Rectangle((0,0),1,1, fc=c, ec=EDGE, lw=0.8) for c in (BLUE,GREEN,YELLOW,PINK,PURPLE)]
ax.legend(handles, ["Gen 0 Foundational","Gen 1 Pioneer","Gen 2 Platform","Gen 3 Current",
                    "Academic publication"], loc="lower right", fontsize=7.4, framealpha=0.95)

fig.tight_layout()
for ext, kw in (("png", {}), ("tif", {"pil_kwargs": {"compression": "tiff_lzw"}})):
    fig.savefig(f"FigureS8_PatentGenealogy.{ext}", dpi=300, bbox_inches="tight",
                facecolor="white", **kw)
print("wrote FigureS8_PatentGenealogy.{png,tif}")
