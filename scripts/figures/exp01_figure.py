"""Apparatus schematic for Experiment 1, the Michelson interferometer."""

import numpy as np
from matplotlib.patches import Circle

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    beam, beamsplitter, box, label, mirror, new_ax, save, source_dot, use_style,
)


def michelson_layout():
    fig, ax = new_ax(figsize=(7.4, 5.4))

    laser = (-2.3, 0.0)
    bs = (0.0, 0.0)
    m_fixed = (0.0, 1.7)
    m_moving = (2.0, 0.0)
    scr = (0.0, -1.7)

    box(ax, laser, 0.62, 0.32, "laser", fontsize=8.5)
    source_dot(ax, (laser[0] + 0.35, laser[1]), color=RED, ms=7, glow=False)
    beam(ax, (laser[0] + 0.45, 0), (bs[0] - 0.17, 0), color=RED)

    beamsplitter(ax, bs, size=0.36)
    label(ax, (bs[0] + 0.05, bs[1] + 0.32), "beamsplitter", fontsize=8, ha="left")

    # transmitted arm -> movable mirror
    beam(ax, (bs[0] + 0.17, 0), (m_moving[0] - 0.22, 0), color=RED)
    mirror(ax, m_moving, angle_deg=90, length=0.7)
    label(ax, (m_moving[0], m_moving[1] + 0.32), "movable mirror\n$M_2$", fontsize=8)
    ax.annotate("", xy=(m_moving[0] + 0.55, 0.0), xytext=(m_moving[0] + 0.2, 0.0),
                arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=1.4))
    ax.annotate("", xy=(m_moving[0] + 0.55, 0.0), xytext=(m_moving[0] + 0.85, 0.0),
                arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=1.4))
    label(ax, (m_moving[0] + 0.55, 0.22), r"$d$", color=PURPLE, fontsize=9.5)
    label(ax, (m_moving[0] + 0.55, -0.35), "micrometer\ndrive", color=PURPLE, fontsize=7.5)

    # reflected arm -> fixed mirror
    beam(ax, (0, bs[1] + 0.17), (0, m_fixed[1] - 0.22), color=RED)
    mirror(ax, m_fixed, angle_deg=0, length=0.7)
    label(ax, (0.42, m_fixed[1]), "fixed mirror\n$M_1$", fontsize=8, ha="left")

    # recombined beam -> screen
    beam(ax, (0, bs[1] - 0.17), (0, scr[1] + 0.55), color=RED, alpha=0.85)

    # fringe pattern on the screen, viewed face-on
    ax.add_patch(Circle((0, scr[1]), 0.5, facecolor="white", edgecolor=DARK, lw=1.2, zorder=3))
    for r, c in zip((0.5, 0.38, 0.27, 0.16, 0.06), ("#cdd7de", RED, "#cdd7de", RED, "#cdd7de")):
        ax.add_patch(Circle((0, scr[1]), r, facecolor="none", edgecolor=c, lw=2.0, zorder=4))
    label(ax, (0, scr[1] - 0.72), "screen — circular fringes", fontsize=8)

    label(ax, (-1.15, 0.16), r"$L_2$", color=GRAY, fontsize=9)
    label(ax, (0.16, 0.85), r"$L_1$", color=GRAY, fontsize=9)

    ax.set_xlim(-3.1, 3.2)
    ax.set_ylim(-2.7, 2.5)
    save(fig, "exp01-michelson-schematic")


if __name__ == "__main__":
    use_style()
    michelson_layout()
