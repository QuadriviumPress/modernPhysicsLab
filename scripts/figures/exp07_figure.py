"""Figures for Experiment 7, the quantum eraser and complementarity: the
apparatus schematic, and a concept figure for the V-D complementarity relation."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    beam, label, new_ax, rotation_stage, save, screen, source_dot, use_style,
)


def _polarizer(ax, xy, angle_deg, color, h=0.5):
    x, y = xy
    import numpy as np
    th = np.radians(angle_deg)
    dx, dy = np.sin(th) * h / 2, -np.cos(th) * h / 2
    ax.add_patch(Rectangle((x - 0.05, y - h / 2), 0.10, h, facecolor="#eef3f7",
                            edgecolor=color, lw=1.2, zorder=3))
    for t in [-0.3, -0.1, 0.1, 0.3]:
        ax.plot([x - 0.05, x + 0.05], [y + t * h, y + t * h], color=color, lw=0.7, zorder=4)


def eraser_layout():
    fig, ax = new_ax(figsize=(8.0, 4.4))

    laser = (-3.2, 0.0)
    slits = (-1.2, 0.0)
    analyzer = (0.6, 0.0)
    cam = (2.6, 0.0)

    from labstyle import box
    box(ax, laser, 0.85, 0.4, "532 nm\nlaser", fontsize=7.6)
    source_dot(ax, (laser[0] + 0.5, 0), color="#4caf50", ms=7, glow=False)
    beam(ax, (laser[0] + 0.6, 0), (slits[0] - 0.12, 0), color="#4caf50")

    d = 0.45
    ax.plot([slits[0], slits[0]], [-1.0, -d - 0.1], color=DARK, lw=2.2, zorder=2)
    ax.plot([slits[0], slits[0]], [-d + 0.1, d - 0.1], color=DARK, lw=2.2, zorder=2)
    ax.plot([slits[0], slits[0]], [d + 0.1, 1.0], color=DARK, lw=2.2, zorder=2)
    _polarizer(ax, (slits[0], d), 0, RED)
    _polarizer(ax, (slits[0], -d), 90, BLUE)
    label(ax, (slits[0], -1.35), "double slit,\nH / V polarizers\non each slit", fontsize=7.2)

    for dy0, c in ((d, RED), (-d, BLUE)):
        beam(ax, (slits[0] + 0.08, dy0), (analyzer[0] - 0.28, 0.15 * (dy0 / d)), color=c, lw=1.1, alpha=0.75)

    rotation_stage(ax, analyzer, r=0.42, angle_deg=45, color=PURPLE)
    ax.add_patch(Rectangle((analyzer[0] - 0.06, analyzer[1] - 0.32), 0.12, 0.64,
                            facecolor="#eef3f7", edgecolor=PURPLE, lw=1.4, zorder=4, angle=0))
    label(ax, (analyzer[0], 1.05), "rotatable\nanalyzer", fontsize=7.4, color=PURPLE)

    for dy0, c in ((0.12, RED), (-0.12, BLUE)):
        beam(ax, (analyzer[0] + 0.05, dy0), (cam[0] - 0.05, dy0 * 1.4), color=DARK, lw=0.9, alpha=0.5)

    screen(ax, cam, height=1.4)
    label(ax, (cam[0], 1.05), "camera /\nscanning photodiode", fontsize=7.4)

    label(ax, (-0.4, 1.9),
          "Analyzer aligned to H or V $\\to$ which-path is marked, fringes vanish.\n"
          "Analyzer at 45$°$ $\\to$ which-path information is erased, fringes return.",
          fontsize=7.8, color=DARK, ha="center")

    ax.set_xlim(-4.1, 3.6)
    ax.set_ylim(-2.0, 2.4)
    save(fig, "exp07-quantum-eraser-schematic")


def complementarity_figure():
    """V and D as functions of analyzer angle, and the V-D trade-off
    tracing the unit circle V^2 + D^2 = 1."""
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(8.6, 3.9))

    theta = np.linspace(0, 90, 400)
    V = np.abs(np.sin(np.radians(2 * theta)))
    D = np.abs(np.cos(np.radians(2 * theta)))

    axL.plot(theta, V, color=RED, lw=1.9, label=r"$V = |\sin 2\theta|$")
    axL.plot(theta, D, color=BLUE, lw=1.9, label=r"$D = |\cos 2\theta|$")
    axL.set_xlabel(r"analyzer angle $\theta$ (degrees)")
    axL.set_ylabel("value")
    axL.set_xlim(0, 90)
    axL.set_ylim(0, 1.05)
    axL.set_xticks([0, 15, 30, 45, 60, 75, 90])
    axL.legend(loc="center right", fontsize=9, frameon=False)
    axL.set_title("Visibility and distinguishability\nversus analyzer angle", fontsize=9.5)

    # theta in [0, 45] traces the full quarter circle once; theta in [45, 90]
    # retraces the same arc back to (D, V) = (1, 0), so only the first quarter
    # is shown, with its two distinct endpoints marked.
    axR.set_aspect("equal")
    phi = np.linspace(0, np.pi / 2, 200)
    axR.plot(np.cos(phi), np.sin(phi), color=GRAY, lw=1.0, ls=":", zorder=1)
    quarter = theta <= 45
    axR.plot(D[quarter], V[quarter], color=PURPLE, lw=2.2, zorder=2)
    axR.plot(1, 0, "o", color=DARK, ms=6, zorder=3)
    axR.plot(0, 1, "o", color=ORANGE, ms=6, zorder=3)
    label(axR, (0.78, 0.16), r"$\theta=0°$" + "\n(no fringes)", fontsize=8, color=DARK, ha="right")
    label(axR, (0.16, 1.09), r"$\theta=45°$" + "\n(full fringes)", fontsize=8, color=ORANGE)
    axR.set_xlabel(r"$D$ (distinguishability)")
    axR.set_ylabel(r"$V$ (visibility)")
    axR.set_xlim(-0.05, 1.2)
    axR.set_ylim(-0.05, 1.2)
    axR.set_title(r"$V^2 + D^2 = 1$", fontsize=9.5)

    fig.tight_layout()
    save(fig, "exp07-complementarity-concept")


if __name__ == "__main__":
    use_style()
    eraser_layout()
    complementarity_figure()
