"""Apparatus schematic for Experiment 8, tunneling by frustrated total internal reflection."""

import numpy as np
from matplotlib.patches import Arc, Polygon

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    beam, box, label, new_ax, save, source_dot, use_style,
)


def ftir_layout():
    fig, ax = new_ax(figsize=(7.6, 4.6))

    laser = (-3.0, -0.9)

    # right-angle prism: hypotenuse along the top, horizontal
    prism = np.array([[-1.4, -1.0], [1.4, -1.0], [0.0, 1.0]])
    ax.add_patch(Polygon(prism, closed=True, facecolor="#dbe9f5", edgecolor=BLUE, lw=1.5, zorder=2))
    label(ax, (0.0, -1.35), "right-angle prism ($n\\approx1.52$)", fontsize=7.6)

    # plano-convex lens pressed against the hypotenuse near the apex,
    # drawn as a shallow arc since its radius of curvature is very long
    R = 1.35
    lens_center = (0.0, 1.0 + R)
    ax.add_patch(Arc(lens_center, 2 * R, 2 * R, theta1=254, theta2=286,
                      edgecolor=RED, lw=1.6, zorder=3))
    label(ax, (0.85, 1.55), "plano-convex lens,\nlong radius $R$\n(pressed on the\nhypotenuse)", fontsize=6.8, ha="left")
    ax.annotate("", xy=(0.0, 1.02), xytext=(0.0, 1.55),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.2))
    label(ax, (-0.55, 1.45), "air gap\n$r(x)$", color=RED, fontsize=7, ha="right")

    box(ax, laser, 0.85, 0.4, "diode laser\n+ expander", fontsize=7.2)
    source_dot(ax, (laser[0] + 0.5, laser[1]), color=RED, ms=7, glow=False)

    # incident beam toward the prism's left face at the TIR angle
    entry = (-0.75, -0.35)
    beam(ax, (laser[0] + 0.6, laser[1]), entry, color=RED)

    # reflected (TIR, away from contact) and transmitted (tunneled, near contact) beams
    exit_tir = (0.85, -0.35)
    beam(ax, entry, exit_tir, color=RED, alpha=0.9)
    exit_tunnel = (0.0, -1.55)
    beam(ax, (0.0, 0.85), exit_tunnel, color=ORANGE, lw=1.2, ls="--", alpha=0.9)
    label(ax, (0.0, -1.85), "tunneled beam\n(camera / photodiode)", fontsize=6.8, color=ORANGE)

    ax.add_patch(Arc(entry, 0.7, 0.7, theta1=52, theta2=90, edgecolor=GRAY, lw=1.0))
    label(ax, (entry[0] + 0.05, entry[1] + 0.5), r"$\theta > \theta_c$", color=GRAY, fontsize=8, ha="left")

    box(ax, (2.55, -0.35), 0.9, 0.6, "USB\nmicroscope /\ncamera", fontsize=6.8)
    ax.plot([exit_tir[0] + 0.05, 2.15], [exit_tir[1], -0.35], color=GRAY, lw=1.0, ls=":")
    label(ax, (1.05, 0.05), "reflected beam\n(dark spot at contact)", fontsize=6.8, color=RED, ha="left")

    label(ax, (0.0, 2.4),
          "Reflection is total except where the lens nearly touches the prism;\n"
          "there, light tunnels across the gap and the reflected spot goes dark.",
          fontsize=8.0, color=DARK, ha="center")

    ax.set_xlim(-3.9, 3.4)
    ax.set_ylim(-2.3, 2.8)
    save(fig, "exp08-ftir-schematic")


if __name__ == "__main__":
    use_style()
    ftir_layout()
