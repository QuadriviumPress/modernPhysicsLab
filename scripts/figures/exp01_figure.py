"""Figures for Experiment 1, the Michelson interferometer: the apparatus
schematic, and a concept figure for why the fringes are circles."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

from labstyle import (
    BLUE, GRAY, LIGHT, ORANGE, PURPLE, RED, DARK,
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


def fringe_geometry_figure():
    """Why the fringes are circles: unfolded-mirror path-difference geometry,
    and the resulting order m = 2d cos(theta)/lambda versus theta."""
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(8.6, 3.7))

    # --- Left: unfolded pair of mirror planes, a ray at angle theta ---
    axL.set_aspect("equal")
    axL.axis("off")
    d = 1.0
    half = 1.05
    axL.plot([-half, half], [0, 0], color=DARK, lw=2.2, solid_capstyle="round")
    axL.plot([-half, half], [d, d], color=DARK, lw=2.2, ls="--", solid_capstyle="round")
    label(axL, (half + 0.12, 0), r"$M_1'$", fontsize=9, ha="left")
    label(axL, (half + 0.12, d), r"$M_2'$", fontsize=9, ha="left")

    theta = np.radians(28)
    x0 = -0.55
    beam(axL, (x0 - 0.7, -0.7), (x0, 0), color=RED, arrow=True)
    beam(axL, (x0, 0), (x0 - 0.65, 0.65), color=RED, arrow=True)
    x1 = x0 + d * np.tan(theta)
    beam(axL, (x0, 0), (x1, d), color=RED, ls="--", alpha=0.75)
    beam(axL, (x1, d), (x1 - 0.65, d + 0.65), color=RED, arrow=True)
    axL.plot([x0, x0], [0, -0.32], color=GRAY, lw=0.8, ls=":")
    axL.annotate("", xy=(x0, -0.28), xytext=(x0 - 0.32 * np.sin(theta), -0.28 + 0.32 * np.cos(theta)),
                 arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))
    label(axL, (x0 - 0.22, -0.42), r"$\theta$", color=GRAY, fontsize=9)
    axL.annotate("", xy=(half + 0.55, 0), xytext=(half + 0.55, d),
                 arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.2))
    label(axL, (half + 0.75, d / 2), r"$d$", color=PURPLE, fontsize=10)
    label(axL, (0.1, -1.15), r"path difference $\Delta = 2d\cos\theta$", fontsize=8.5, color=DARK)
    label(axL, (1.35, 1.35), "rays leaving the\nsource at a fixed $\\theta$\nall pick up the same $\\Delta$",
          fontsize=7.8, color=GRAY, ha="left")
    axL.set_xlim(-1.9, 3.1)
    axL.set_ylim(-1.7, 2.0)

    # --- Right: order m(theta) = (2d/lambda) cos(theta), rings crowd at large theta ---
    lam = 632.8e-9
    d_phys = 10 * lam  # a handful of wavelengths of "extra" path at theta = 0, for a legible curve
    th_max = np.radians(60)
    th = np.linspace(0, th_max, 400)
    m = 2 * d_phys / lam * np.cos(th)
    axR.plot(np.degrees(th), m, color=RED, lw=1.8)
    m0, m1 = m[0], m[-1]
    for k in range(int(np.ceil(m1)), int(np.floor(m0)) + 1):
        axR.axhline(k, color=LIGHT, lw=0.7, zorder=0)
        idx = np.argmin(np.abs(m - k))
        if 0 < idx < len(th) - 1:
            axR.plot(np.degrees(th[idx]), k, "o", color=BLUE, ms=4.5, zorder=3)
    axR.set_xlabel(r"$\theta$ (degrees)")
    axR.set_ylabel(r"order $m = 2d\cos\theta/\lambda$")
    axR.set_title("bright rings (dots) crowd together\nat larger $\\theta$", fontsize=9)
    axR.set_xlim(0, 60)

    fig.tight_layout()
    save(fig, "exp01-fringe-geometry")


if __name__ == "__main__":
    use_style()
    michelson_layout()
    fringe_geometry_figure()
