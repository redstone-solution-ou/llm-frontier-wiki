"""
Regenerate the 2D frontier-leaderboard chart.

Run from the repo root:

    python3 scripts/generate_frontier_chart.py

Output: wiki/assets/frontier-leaderboard.png

Re-run whenever a model's score on either axis lands or changes.
Data lives inline below so this script is the single source of
truth for the chart; if you update a score here, update the
corresponding model leaf and the leaderboard markdown in the
same commit.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D


# Vendor colour palette (colour-blind-aware; not Anthropic-only)
VENDOR_COLOURS = {
    "Anthropic": "#D97757",   # warm orange
    "OpenAI":    "#10A37F",   # OpenAI teal
    "Google":    "#4285F4",   # Google blue
    "Zhipu AI":  "#8E44AD",   # purple (open weights)
}


# Models: (label, x = Vending-Bench 2 $, y = FrontierMath Tier 4 v2 %,
#          vendor, x_kind, y_kind, x_err, y_err)
# x_kind / y_kind ∈ {"measured", "proxy", "inferred", "absent"}
#   measured  — direct score on the canonical benchmark
#   proxy     — placed via a different benchmark (e.g. DeepSWE for the
#               long-horizon axis); annotated in the legend
#   inferred  — bracketed by neighbouring measured points but no direct
#               filing (e.g. Opus 4.7 between Opus 4.6 and Opus 4.8)
#   absent    — model not in the relevant leaderboard's top-5; placed at
#               a conservative ceiling for visibility, marked with a
#               down-arrow caret
MODELS = [
    # label,              x,     y,    vendor,      x_kind,    y_kind,    xerr, yerr
    ("Claude Fable 5",    5680, 87.8, "Anthropic", "measured", "measured", None, 5.2),
    ("GPT-5.5 Pro",       6000, 78.0, "OpenAI",    "proxy",    "measured", None, 6.5),
    ("GPT-5.5",           6000, 72.5, "OpenAI",    "proxy",    "measured", None, 7.1),
    ("Claude Opus 4.8",   5787, 56.1, "Anthropic", "measured", "measured", None, 7.8),
    ("Claude Opus 4.7",   7500, 52.0, "Anthropic", "inferred", "inferred", None, None),
    ("Claude Opus 4.6",   8018, 40.0, "Anthropic", "measured", "absent",   None, None),
    ("GLM-5.1",           5634, 30.0, "Zhipu AI",  "measured", "absent",   None, None),
    ("Gemini 3 Pro",      5478, 25.0, "Google",    "measured", "absent",   None, None),
]


# Marker shape by confidence — fully measured gets a filled circle;
# anything else gets a hollow shape that signals "approximate".
def marker_for(x_kind, y_kind):
    if x_kind == "measured" and y_kind == "measured":
        return dict(marker="o", facecolor="full", edgewidth=1.5, size=180)
    if x_kind == "absent" or y_kind == "absent":
        return dict(marker="v", facecolor="hollow", edgewidth=2.0, size=180)
    return dict(marker="s", facecolor="hollow", edgewidth=2.0, size=160)


def build_chart(output_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(12, 8))

    # Empty upper-right "frontier" quadrant shading — the wiki's
    # headline observation is that no current model occupies it.
    quadrant = Rectangle(
        (7500, 80), 3500, 20,
        facecolor="#FFF3B0", alpha=0.55, zorder=0,
    )
    ax.add_patch(quadrant)
    ax.text(
        9250, 91,
        'empty "frontier" quadrant\n(no current model\nleads both axes)',
        ha="center", va="center",
        fontsize=9.5, style="italic", color="#7A6500", zorder=1,
    )

    # Plot each model
    for label, x, y, vendor, xk, yk, xerr, yerr in MODELS:
        colour = VENDOR_COLOURS[vendor]
        mk = marker_for(xk, yk)
        facecolor = colour if mk["facecolor"] == "full" else "white"

        # Confidence interval (FrontierMath ±%) — vertical error bar
        # only on measured y-values.
        if yerr is not None and yk == "measured":
            ax.errorbar(
                x, y, yerr=yerr, fmt="none",
                ecolor=colour, elinewidth=1.0, capsize=4, alpha=0.55,
                zorder=2,
            )

        ax.scatter(
            x, y,
            s=mk["size"], marker=mk["marker"],
            facecolors=facecolor, edgecolors=colour,
            linewidths=mk["edgewidth"], zorder=3,
        )

        # Label placement — offsets in display pixels so they read
        # uniformly regardless of the asymmetric data scale.
        # Tuned manually for the v0 model set; redo when models change.
        offsets_px = {
            "Claude Fable 5":  ( 18,   0),   # right of marker
            "GPT-5.5 Pro":     ( 18,   8),   # right-up
            "GPT-5.5":         ( 18,  -8),   # right-down
            "Claude Opus 4.8": (-18,   0),   # left of marker
            "Claude Opus 4.7": ( 18,   0),   # right
            "Claude Opus 4.6": ( 18,   0),   # right
            "GLM-5.1":         (-18,   0),   # left
            "Gemini 3 Pro":    (-18,  -2),   # left
        }
        dx_px, dy_px = offsets_px[label]
        ax.annotate(
            label,
            xy=(x, y),
            xytext=(dx_px, dy_px),
            textcoords="offset points",
            fontsize=9.5, color="#222",
            ha="left" if dx_px > 0 else "right",
            va="center",
        )

    # Axes
    ax.set_xlim(0, 11000)
    ax.set_ylim(0, 102)
    ax.set_xlabel(
        "Long-horizon agentic coherence  →  "
        "Vending-Bench 2 final balance, 5-run avg ($)",
        fontsize=11,
    )
    ax.set_ylabel(
        "Frontier reasoning  →  "
        "FrontierMath Tier 4 (v2) accuracy (%)",
        fontsize=11,
    )

    # Reference gridlines for the leaderboard ranks
    for x_ref, label in [
        (8018, "Opus 4.6 baseline"),
        (5500, "rank 2-4 band"),
    ]:
        ax.axvline(x_ref, color="#999", linestyle=":", linewidth=0.8, alpha=0.6)
    for y_ref in [56.1, 78.0, 87.8]:
        ax.axhline(y_ref, color="#999", linestyle=":", linewidth=0.8, alpha=0.4)

    ax.grid(True, linestyle="--", alpha=0.25)
    ax.set_axisbelow(True)

    # Title (placed above the axes so it never collides with labels)
    fig.suptitle(
        "LLM Frontier — 2D Capability Map",
        fontsize=15, fontweight="bold", x=0.06, ha="left", y=0.985,
    )
    fig.text(
        0.06, 0.95,
        "filed 2026-06-22  ·  sources: Andon Labs Vending-Bench 2, "
        "Epoch AI FrontierMath Tier 4 (v2), DeepSWE.net",
        fontsize=9.5, color="#555", ha="left", va="top",
    )

    # Legend — combine vendor colour + marker confidence
    vendor_handles = [
        Line2D([0], [0], marker="o", linestyle="",
               markerfacecolor=colour, markeredgecolor=colour,
               markersize=10, label=vendor)
        for vendor, colour in VENDOR_COLOURS.items()
    ]
    confidence_handles = [
        Line2D([0], [0], marker="o", linestyle="",
               markerfacecolor="#444", markeredgecolor="#444",
               markersize=10, label="both axes measured"),
        Line2D([0], [0], marker="s", linestyle="",
               markerfacecolor="white", markeredgecolor="#444",
               markersize=10, markeredgewidth=2,
               label="proxy / inferred placement"),
        Line2D([0], [0], marker="v", linestyle="",
               markerfacecolor="white", markeredgecolor="#444",
               markersize=11, markeredgewidth=2,
               label="absent from reasoning top-5 (y is ceiling)"),
    ]
    legend1 = ax.legend(
        handles=vendor_handles, loc="upper left",
        bbox_to_anchor=(0.005, 0.995), title="Vendor",
        framealpha=0.92, fontsize=9, title_fontsize=10,
    )
    ax.add_artist(legend1)
    ax.legend(
        handles=confidence_handles, loc="lower right",
        bbox_to_anchor=(0.995, 0.005), title="Placement confidence",
        framealpha=0.92, fontsize=9, title_fontsize=10,
    )

    # Leave headroom for suptitle / subtitle above the axes
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    out = repo_root / "wiki" / "assets" / "frontier-leaderboard.png"
    build_chart(out)
    print(f"wrote {out.relative_to(repo_root)}")
