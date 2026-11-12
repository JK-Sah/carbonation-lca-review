"""Figure 1 -- PRISMA 2020 flow diagram for the search of 23 August 2026.

Counts are written here as literals and match search/screening_log.csv,
search/fulltext_exclusions.csv and Section 4.1: 934 retrieved, 713 unique,
391 sought, 57 assessed, 40 excluded, 17 included. Full-text assessment is
incomplete and the diagram says so rather than implying a finished stage.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrow

DARK, LIGHT, CREAM, PINK, GREEN, MID = "#1f4e79", "#deebf7", "#fff2cc", "#fce4e4", "#e2f0d9", "#2e75b6"
GREY = "#f2f2f2"
FS_BOX, FS_SUB, FS_STAGE, FS_TITLE, FS_NOTE = 15, 12.5, 15, 19, 11

fig, ax = plt.subplots(figsize=(11.0, 13.6), dpi=300)
ax.set_xlim(0, 100); ax.set_ylim(0, 122); ax.axis("off")

def box(x, y, w, h, text, fc, ec=DARK, fs=FS_BOX, weight="normal", tc="black"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6,rounding_size=1.2",
                                fc=fc, ec=ec, lw=2.0))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            fontsize=fs, weight=weight, color=tc, linespacing=1.55)

def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrow(x1, y1, x2-x1, y2-y1, width=0.22, head_width=1.5,
                            head_length=1.3, length_includes_head=True, fc=DARK, ec=DARK))

def stage(y, label):
    ax.text(1.5, y, label, rotation=90, ha="center", va="center",
            fontsize=FS_STAGE, weight="bold", style="italic", color=MID)

ax.text(50, 119, "PRISMA 2020 Flow Diagram", ha="center", va="center",
        fontsize=FS_TITLE, weight="bold", color=DARK)

# ---- Identification ----
stage(101, "Identification")
srcs = [("Queries Q1–Q4\ncarbonation curing,\nmineralization\n(n = 326)", 10),
        ("Queries Q5–Q8\nCCU, uptake,\ncapture\n(n = 608)", 55)]
for txt, x in srcs:
    box(x, 95, 35, 13, txt, LIGHT, fs=FS_SUB)
    arrow(x + 17.5, 95, 47, 90.5)

box(20, 79, 54, 10.5, "Records identified, OpenAlex, 23 Aug 2026\n(n = 934)",
    DARK, fs=FS_BOX, weight="bold", tc="white")
box(78, 79, 20, 10.5, "Duplicate records\nremoved\n(n = 221)", CREAM, fs=FS_SUB)
arrow(78, 84.2, 74.5, 84.2)

# ---- Screening ----
stage(62, "Screening")
arrow(47, 79, 47, 73.5)
box(20, 61, 54, 12.5, "Unique records screened\non title and abstract\n(n = 713)",
    DARK, fs=FS_BOX, weight="bold", tc="white")
box(76.5, 57.5, 23, 19.5,
    "Records excluded\n(n = 322)\n\nNo carbonation/CO$_2$-use\nintervention: 221\n"
    "Not a cement product: 68\nNatural carbonation /\ndurability: 21\n"
    "No quantitative outcome: 7\nGeological CCS: 5", PINK, fs=11)
arrow(76.5, 67, 74.5, 67)

# ---- Eligibility ----
stage(40, "Eligibility")
arrow(47, 61, 47, 55.5)
box(20, 44, 54, 11.5, "Full-text articles sought\nfor assessment\n(n = 391)",
    DARK, fs=FS_BOX, weight="bold", tc="white")
box(76.5, 44.5, 23, 10.5, "Assessment ongoing;\nnot yet assessed\n(n = 334)", GREY, ec="#808080", fs=FS_SUB)
arrow(76.5, 49.8, 74.5, 49.8)

arrow(47, 44, 47, 38.5)
box(20, 27, 54, 11.5, "Full-text articles assessed\nfor eligibility\n(n = 57)",
    DARK, fs=FS_BOX, weight="bold", tc="white")
box(76.5, 21.5, 23, 22.5,
    "Full texts excluded\n(n = 40)\n\nNo functional unit or\nboundary (I2): 9\n"
    "Uptake-only, no LCA (X3): 7\nNo carbonation intervention: 7\n"
    "Natural carbonation (X1): 5\nReview / reanalysis (X5): 4\n"
    "Not a cement product (X7): 2\nNo GWP outcome (I5): 2\n"
    "Other (I3, X4, X6): 4", PINK, fs=10.5)
arrow(76.5, 32.7, 74.5, 32.7)

# ---- Included ----
stage(12, "Included")
arrow(47, 27, 47, 21.5)
box(20, 10, 54, 11.5, "Studies included in synthesis\n(n = 17)",
    "#548235", ec="#375623", fs=FS_BOX, weight="bold", tc="white")

ax.text(50, 5.0,
        "Single-rater screening; a coded decision is released for every one of the 713 records.\n"
        "Verbatim query strings: Supplementary S1   |   Screening log: Supplementary S5   |   "
        "Full-text exclusions: Supplementary S5",
        ha="center", va="center", fontsize=FS_NOTE, style="italic", color="#404040", linespacing=1.6)

fig.tight_layout()
for ext, kw in (("png", {}), ("tif", {"pil_kwargs": {"compression": "tiff_lzw"}})):
    fig.savefig(f"Figure1_PRISMA_FlowDiagram.{ext}", dpi=300, bbox_inches="tight",
                facecolor="white", **kw)
print("wrote Figure1_PRISMA_FlowDiagram.{png,tif}")
