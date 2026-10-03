"""Figures for Experiment 14, a cosmic-ray muon telescope: the apparatus
schematic, and the time-dilation / length-contraction concept figure."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Polygon

from labstyle import (
    GRAY, GREEN, PURPLE, RED, DARK,
    beam, box, label, new_ax, save, use_style,
)


def muon_telescope_layout():
    fig, ax = new_ax(figsize=(6.6, 5.8))

    zenith = 25
    angle = np.radians(zenith)
    center = np.array([0.0, 0.25])
    down = np.array([np.sin(angle), -np.cos(angle)])
    across = np.array([np.cos(angle), np.sin(angle)])
    top = center - 0.72 * down
    bottom = center + 0.72 * down

    def slab(pos, width, depth, color):
        corners = [pos + a * width / 2 * across + b * depth / 2 * down
                   for a, b in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
        ax.add_patch(Polygon(corners, closed=True, facecolor=color,
                             edgecolor=DARK, lw=1.2, zorder=4))

    for off in (-0.28, 0.0, 0.28):
        start = top - 0.66 * down + off * across
        end = bottom + 0.65 * down + off * across
        beam(ax, start, end, color=RED, lw=1.2, arrow=True, alpha=0.85)

    slab(top, 1.7, 0.13, "#cfd8dc")
    slab(bottom, 1.7, 0.13, "#cfd8dc")
    slab(center, 1.5, 0.10, "#e4d9bd")

    for side in (-0.9, 0.9):
        rail_top = top + side * across
        rail_bottom = bottom + side * across
        ax.plot([rail_top[0], rail_bottom[0]],
                [rail_top[1], rail_bottom[1]], color=GRAY, lw=1.2,
                ls=(0, (4, 2)), zorder=1)

    dim_top = top - 1.12 * across
    dim_bottom = bottom - 1.12 * across
    ax.annotate("", xy=dim_bottom, xytext=dim_top,
                arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.2))
    label(ax, (-1.65, 0.2), "adjustable\nseparation", color=PURPLE,
          fontsize=7, ha="center")
    label(ax, (1.30, 1.18), "GM tube 1", fontsize=7.7, ha="left")
    label(ax, (1.30, -0.38), "GM tube 2", fontsize=7.7, ha="left")
    label(ax, (1.30, 0.28), "optional absorber\nbetween tubes",
          fontsize=7, ha="left")

    vertical = center + np.array([0.0, 1.55])
    axis = center - 1.55 * down
    ax.plot([center[0], vertical[0]], [center[1], vertical[1]],
            color=GRAY, lw=1, ls=":", zorder=1)
    ax.plot([center[0], axis[0]], [center[1], axis[1]],
            color=GRAY, lw=1, ls=":", zorder=1)
    ax.add_patch(Arc(center, 1.1, 1.1, theta1=90, theta2=90 + zenith,
                     edgecolor=GRAY, lw=1.1))
    label(ax, (-0.38, 1.05), r"$\theta$ (zenith)", color=GRAY,
          fontsize=8, ha="right")

    box(ax, (0.0, -2.2), 2.25, 0.55,
        "isolated pulse outputs\n+ coincidence unit", fontsize=7.0)
    for pos, x in ((top, -0.8), (bottom, 0.8)):
        ax.plot([pos[0], x], [pos[1], -1.93], color=DARK, lw=0.8,
                ls=":", zorder=0)
    label(ax, (0.0, 2.34),
          "The whole rigid frame rotates; aligned tracks cross both tubes.",
          fontsize=8.0, color=DARK, ha="center")

    ax.set_xlim(-2.3, 2.5)
    ax.set_ylim(-2.75, 2.7)
    save(fig, "exp14-muon-telescope-schematic")


def time_dilation_figure():
    """Two views of the same physics: (left) in the lab frame, time
    dilation stretches the muon's decay length far past the non-relativistic
    value; (right) in the muon's own frame, length contraction shrinks the
    atmosphere down to a thickness it can cross in about one lifetime."""
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(8.4, 4.6))

    atmosphere_km = 15.0
    c_tau0_km = 0.659  # c * proper lifetime
    gamma = 20.0
    dilated_km = gamma * c_tau0_km  # ~13.2 km, beta ~ 1

    axL.bar([0], [atmosphere_km], width=0.55, color="#dbe9f5", edgecolor=GRAY, zorder=1)
    axL.bar([1], [c_tau0_km], width=0.55, color=RED, zorder=2)
    axL.bar([2], [dilated_km], width=0.55, color=GREEN, zorder=2)
    axL.set_xticks([0, 1, 2])
    axL.set_xticklabels(["assumed path\n(15 km)", "counterfactual\n$c\\tau_0$\n(0.66 km)",
                          "decay length\nwith dilation\n(13.2 km)"], fontsize=7.6)
    axL.set_ylabel("distance in the lab frame (km)")
    axL.set_ylim(0, atmosphere_km * 1.15)
    axL.set_title("Lab frame: time dilation\nstretches the decay length", fontsize=9.5)

    contracted_km = atmosphere_km / gamma
    axR.bar([0], [contracted_km], width=0.55, color="#dbe9f5", edgecolor=GRAY, zorder=1)
    axR.bar([1], [c_tau0_km], width=0.55, color=PURPLE, zorder=2)
    axR.set_xticks([0, 1])
    axR.set_xticklabels(["path in muon\nframe\n(0.75 km)", "$c\\tau_0$\n(0.66 km)"],
                         fontsize=7.6)
    axR.set_ylabel("distance in the muon's frame (km)")
    axR.set_ylim(0, 1.05)
    axR.set_title("Muon's frame: length contraction\nshrinks the path", fontsize=9.5)

    fig.suptitle("Same physics, two frames", fontsize=11, y=1.02)
    fig.tight_layout()
    save(fig, "exp14-time-dilation-concept")


if __name__ == "__main__":
    use_style()
    muon_telescope_layout()
    time_dilation_figure()
